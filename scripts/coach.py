#!/usr/bin/env python3
"""Local scenario scheduler. No network, model calls, or transcript storage."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile

BANK = Path(__file__).resolve().parents[1] / 'assets' / 'scenarios.json'
TAGS = {'topic-drift', 'context-overload', 'unclear-action', 'attention-burden',
        'premature-advice', 'contact-pretext', 'mind-reading', 'boundary-pressure'}


def read_state(path, bank):
    if path is None or not path.exists():
        return {'version': 1, 'level': 1, 'history': []}
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('version') != 1:
        raise ValueError('Unsupported state version')
    if type(data.get('level')) is not int or data['level'] not in (1, 2, 3):
        raise ValueError('Invalid difficulty level')
    if not isinstance(data.get('history'), list):
        raise ValueError('Invalid history')
    known = {s['id']: s for s in bank}
    for row in data['history']:
        if not isinstance(row, dict) or row.get('scenario') not in known:
            raise ValueError('Invalid scenario in history')
        if row.get('module') != known[row['scenario']]['module']:
            raise ValueError('Invalid module in history')
        if type(row.get('score')) is not int or row['score'] not in (0, 1, 2):
            raise ValueError('Invalid score in history')
        tags = row.get('fingerprints')
        if not isinstance(tags, list) or any(not isinstance(t, str) or t not in TAGS for t in tags):
            raise ValueError('Invalid fingerprints in history')
        if not isinstance(row.get('at'), str):
            raise ValueError('Invalid timestamp')
    return data


def save_state(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         prefix='.coach-', delete=False) as out:
            name = out.name
            json.dump(data, out, ensure_ascii=False, indent=2)
            out.write('\n')
            out.flush()
            os.fsync(out.fileno())
        os.replace(name, path)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def choose(bank, state, module):
    history = state['history']
    counts = Counter(r['module'] for r in history)
    errors = Counter(t for r in history[-12:] for t in set(r['fingerprints']))
    candidates = [s for s in bank if module is None or s['module'] == module]
    if history and len(candidates) > 1:
        candidates = [s for s in candidates if s['id'] != history[-1]['scenario']]
    def rank(s):
        # Due weaknesses outrank coverage; least-recently practiced breaks ties.
        last = max((i for i, r in enumerate(history) if r['scenario'] == s['id']), default=-1)
        due = sum(errors[t] for t in s['fingerprints'] if errors[t] >= 2)
        return (-due, counts[s['module']], last, s['id'])
    s = min(candidates, key=rank)
    return {k: v for k, v in s.items() if k != 'challenges'} | {
        'level': state['level'], 'challenge': s['challenges'][state['level'] - 1]}


def main():
    bank = json.loads(BANK.read_text(encoding='utf-8'))
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('next', 'record', 'report'):
        p = sub.add_parser(command)
        p.add_argument('--state', type=Path, required=command != 'next',
                       help='Private local JSON file; only record writes it')
        if command == 'next':
            p.add_argument('--module', choices=sorted({s['module'] for s in bank}))
        if command == 'record':
            p.add_argument('--scenario', required=True, choices=[s['id'] for s in bank])
            p.add_argument('--score', required=True, type=int, choices=(0, 1, 2))
            p.add_argument('--fingerprints', nargs='*', default=[], choices=sorted(TAGS))
    args = parser.parse_args()
    try:
        state = read_state(args.state, bank)
        if args.command == 'next':
            result = choose(bank, state, args.module)
        elif args.command == 'record':
            if len(set(args.fingerprints)) > 2:
                raise ValueError('Record at most two fingerprints per attempt')
            scenario = next(s for s in bank if s['id'] == args.scenario)
            state['history'].append(dict(at=datetime.now(timezone.utc).isoformat(),
                scenario=args.scenario, module=scenario['module'], score=args.score,
                fingerprints=sorted(set(args.fingerprints))))
            if len(state['history']) % 3 == 0:
                scores = [r['score'] for r in state['history'][-3:]]
                if scores == [2, 2, 2]:
                    state['level'] = min(3, state['level'] + 1)
                elif scores.count(0) >= 2:
                    state['level'] = max(1, state['level'] - 1)
            save_state(args.state, state)
            result = {'recorded': True, 'attempts': len(state['history']), 'level': state['level']}
        else:
            errors = Counter(t for r in state['history'][-12:] for t in set(r['fingerprints']))
            result = {'attempts': len(state['history']), 'level': state['level'],
                      'module_counts': dict(Counter(r['module'] for r in state['history'])),
                      'recurring_fingerprints': {k: v for k, v in errors.items() if v >= 2}}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, f'Error: {exc}\n')


if __name__ == '__main__':
    main()

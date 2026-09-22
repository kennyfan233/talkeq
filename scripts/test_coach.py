"""Run: python3 -m unittest discover -s scripts -p 'test_*.py'"""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('coach.py')

class CoachTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.state = Path(self.tmp.name) / 'state.json'

    def run_cli(self, *args, ok=True):
        p = subprocess.run([sys.executable, str(SCRIPT), *args, '--state', str(self.state)],
                           capture_output=True, text=True)
        if ok:
            self.assertEqual(p.returncode, 0, p.stderr)
            return json.loads(p.stdout)
        self.assertNotEqual(p.returncode, 0)

    def record(self, score, scenario='team-1', tags=()):
        return self.run_cli('record', '--scenario', scenario, '--score', str(score),
                            '--fingerprints', *tags)

    def test_read_only_and_persistence(self):
        self.run_cli('next')
        self.assertFalse(self.state.exists())
        self.record(1)
        before = self.state.read_bytes()
        self.assertEqual(self.run_cli('report')['attempts'], 1)
        self.run_cli('next')
        self.assertEqual(before, self.state.read_bytes())
        row = json.loads(before)['history'][0]
        self.assertEqual(set(row), {'at', 'scenario', 'module', 'score', 'fingerprints'})

    def test_difficulty_bounds_and_decrease(self):
        for _ in range(9):
            self.record(2)
        self.assertEqual(self.run_cli('report')['level'], 3)
        for _ in range(9):
            self.record(0)
        self.assertEqual(self.run_cli('report')['level'], 1)

    def test_remediation_and_no_immediate_repeat(self):
        for _ in range(2):
            self.record(0, tags=('topic-drift',))
        self.assertNotEqual(self.run_cli('next')['id'], 'team-1')
        self.record(2, 'emotion-1')
        self.assertEqual(self.run_cli('next')['id'], 'team-1')
        self.assertEqual(self.run_cli('report')['recurring_fingerprints']['topic-drift'], 2)

    def test_invalid_state_and_input_preserve_file(self):
        self.state.write_text('{bad json')
        self.run_cli('record', '--scenario', 'team-1', '--score', '2', ok=False)
        self.assertEqual(self.state.read_text(), '{bad json')
        self.state.unlink()
        self.run_cli('record', '--scenario', 'team-1', '--score', '7', ok=False)
        self.assertFalse(self.state.exists())

if __name__ == '__main__':
    unittest.main()

# TalkEQ Communication & Emotional Intelligence Coach

[简体中文](README.md) | **English**

Practice clear, natural communication with realistic scenarios, specific feedback, and follow-up practice on recurring difficulties. Sessions take **5–10 minutes** by default. You can also bring a message directly for revision or review.

TalkEQ is a skill package for an AI assistant that supports skills, not a standalone chat application. Its Python script selects scenarios, stores results, and produces statistics. The host assistant interprets context, gives feedback, suggests revisions, and assigns scores.

## Contents

- [Quick start](#quick-start)
- [Nine practice modules](#nine-practice-modules)
- [Session flow and example prompts](#session-flow-and-example-prompts)
- [Language, practice habits, and reminders](#language-practice-habits-and-reminders)
- [Package structure](#package-structure)
- [Command-line usage](#command-line-usage)
- [Scoring and adaptive practice](#scoring-and-adaptive-practice)
- [Records and privacy](#records-and-privacy)
- [Extending the scenario bank](#extending-the-scenario-bank)
- [Validation and troubleshooting](#validation-and-troubleshooting)

## Quick start

### 1. Place the skill package

Extract the archive and place the complete `talkeq/` folder in a skill directory supported by your host. Keep the internal relative paths intact. The exact installation directory and loading procedure depend on your host configuration. Load the folder containing `SKILL.md`; avoid accidental nesting such as `talkeq/talkeq/`.

Do not import only `SKILL.md`: the references, scenario bank, and scripts are also part of the skill. Running the Python script requires local file access and Python execution. If the host cannot run scripts, the assistant can still use the teaching framework for conversational practice without persistent records.

### 2. Invoke the skill

In a session that can load the skill, enter:

```text
Use $talkeq to introduce the practice rules, list all nine modules with copyable prompts, and let me choose.
```

The first invocation presents the rules and full menu. Importing the files does not automatically start a session or display a welcome message. If you already specify a module in your first invocation, the assistant introduces the skill and continues into that module.

### 3. Choose a module and respond

```text
Let's practice team communication today. Give me one scenario.
```

The assistant presents one scenario at a time. You respond before receiving feedback, revise when useful, and finish with one actionable takeaway. No practice schedule or personal record is required.

## Nine practice modules

| No. | Module | Practice goals | Copyable prompt | CLI module |
| --- | --- | --- | --- | --- |
| 1 | Team communication | Group updates, key points, and clear next steps | Let's practice team communication. Give me one scenario. | `team` |
| 2 | Tasks and decisions | Separate ideas, discussions, decisions, and tasks; clarify ownership and completion criteria | Let's practice tasks and decisions. Help me make a task clear. | `tasks` |
| 3 | Information layering | Give the essential conclusion first, then add context as needed | Let's practice information layering. Help me decide how much to say. | `layering` |
| 4 | Attention boundaries | Provide necessary context and make extra reading or participation optional | Let's practice attention boundaries and avoid unnecessary reading burden. | `attention` |
| 5 | Emotional responses | Distinguish listening, empathy, advice, and action; repair misunderstandings | Let's practice responding to emotions. Give me a scenario where a friend is venting. | `emotion` |
| 6 | Pause before sending | Examine the purpose and timing of contact, and when to stop | Let's practice pausing before sending. Help me decide whether to send a message. | `pause` |
| 7 | Relationship boundaries | Express limits, say no, and respect the other person's autonomy | Let's practice expressing my boundaries and respecting someone else's. | `relationship` |
| 8 | Relationship compatibility | Discuss contact frequency, preferences, and differences | Let's practice discussing our preferences for staying in touch. | `compatibility` |
| 9 | Professional / founder communication | Introductions, client conversations, partnerships, and natural follow-ups | Let's practice professional communication with a natural self-introduction. | `professional` |

Choose a number, a module name, or a full prompt. You can switch modules at any time. The package currently contains **9 base scenarios, one per module, each with 3 levels of additional conditions**. The assistant can also generate new scenarios using the teaching framework.

## Session flow and example prompts

### A complete session

1. **Scenario:** The assistant presents the situation, question, and applicable additional condition.
2. **Response:** You write what you would say or explain what you would do.
3. **Feedback:** The assistant identifies what worked, the main issue, how the recipient might interpret it, and a specific improvement.
4. **Revision:** Try again when useful, rather than only reading a model answer.
5. **Takeaway:** Finish with one reminder you can use in a future conversation.

The assistant normally waits for your attempt before showing a model answer. Length, introversion, or a different communication style alone should not lower your score.

### Revise a real message directly

```text
Use $talkeq to revise this message while keeping a natural tone. Give me the revision first, then explain the most important change:
“Why haven't you sent me what you promised? I can't get anything done without it.”
Context: I need a teammate to confirm the page copy before I can schedule development.
```

This request goes straight to the message; no scenario exercise is required. The recipient's role, your objective, and necessary context are usually enough. You do not need real names or a complete chat transcript.

### Review a misunderstanding

```text
Help me review this exchange: what was I trying to communicate, what might the other person have heard, and what could I add to clarify things?
Here is an anonymized conversation: …
```

### Authorize mixed practice

```text
Choose a module for me today and give me one scenario. Prioritize difficulties that have appeared in this conversation.
```

Cross-module scheduling is used only when you authorize the coach to choose or request mixed practice. An explicitly selected module takes priority over recommendations based on recurring difficulties.

## Language, practice habits, and reminders

### Language

The assistant follows your current conversation language by default. You can explicitly choose another language:

```text
Use $talkeq. From now on, practice team communication with me in English.
```

Rules, menus, scenarios, and feedback use the selected language. Without a fixed preference, changing your conversation language also changes the practice language. Quoting foreign-language material alone does not change it. Paths, commands, module identifiers, scenario IDs, and record tags remain unchanged.

The bundled scenario text and script output are in Chinese. The assistant translates them for presentation in the selected language; the script has no language-selection parameter.

### Optional practice habits

Practice is on demand by default. There is no preset weekly distribution, daily frequency, or module rotation. You can request a routine:

```text
Set a practice habit: twice a day, team communication in the first session and relationship boundaries in the second, about 5 minutes each.
```

Change the frequency, switch modules, pause, or cancel at any time. Your explicit module choice for the current session overrides a routine. The current conversation can retain the arrangement. Saving it across sessions requires a private location of your choice; practice preferences must be stored separately from the script's score state file.

### Reminders

Setting a practice habit does not create reminders. Request reminders separately through a host that supports them. `coach.py` has no background service, scheduler, or notification functionality.

## Package structure

```text
talkeq/
├── README.md                         Chinese user and maintainer guide
├── README.en.md                      English user and maintainer guide
├── SKILL.md                          Skill entry point, workflow, usage, and boundaries
├── 使用说明.txt                      Brief usage instructions in Chinese
├── agents/
│   └── openai.yaml                   Display metadata, default prompt, invocation policy
├── assets/
│   └── scenarios.json                Built-in scenario bank
├── references/
│   ├── coaching-framework.md         Teaching framework and feedback principles
│   └── scoring.md                    Scoring rules and controlled difficulty tags
└── scripts/
    ├── coach.py                      Local selection, recording, and reporting tool
    └── test_coach.py                 Existing unit tests
```

Start with this README for usage. See [SKILL.md](SKILL.md) for assistant behavior, the [teaching framework](references/coaching-framework.md) for coaching detail, and the [scoring reference](references/scoring.md) for record conventions. The English README does not translate the other package files; the assistant adapts their teaching content to your selected language.

## Command-line usage

### Requirements

- Python **3.9 or later**.
- Python standard library only; no `pip install` is needed.
- The script needs no API key, makes no network requests, and does not call a language model.
- Run the commands below from the `talkeq/` directory. Quote paths that contain spaces.

These offline properties apply to the local script. Data handling in conversations with an AI assistant depends on the host; the whole experience is not necessarily offline.

### Get a scenario: `next`

Get a scenario without persistent history:

```bash
python3 scripts/coach.py next
```

Choose a module:

```bash
python3 scripts/coach.py next --module team
```

Use existing history within a selected module:

```bash
python3 scripts/coach.py next --state "/your/private/directory/coach-state.json" --module relationship
```

Both `--state` and `--module` are optional. Without `--state`, each invocation uses the initial state. Without a module restriction, the script can select from the entire bank; the assistant should have your authorization for mixed practice before using that behavior conversationally.

Main fields in the returned JSON:

| Field | Meaning |
| --- | --- |
| `id` / `module` | Scenario ID and module |
| `title` | Scenario title |
| `situation` / `question` | Background and question presented to the user |
| `focus` | Coaching objective for evaluating the response |
| `fingerprints` | Scenario tags used for scheduling, not a judgment of the user |
| `level` / `challenge` | Current difficulty and its additional condition |

`next` only reads state. It neither creates a file nor treats a presented question as a completed attempt. Repeated calls without new records may return the same scenario.

### Save a result: `record`

Use this command only after opting into persistent records. Replace the example path with a private writable location you choose, outside the skill installation directory.

```bash
python3 scripts/coach.py record \
  --state "/your/private/directory/coach-state.json" \
  --scenario team-1 \
  --score 1 \
  --fingerprints topic-drift
```

Omit `--fingerprints` when there is no difficulty to record:

```bash
python3 scripts/coach.py record \
  --state "/your/private/directory/coach-state.json" \
  --scenario team-1 \
  --score 2
```

| Argument | Required? | Meaning |
| --- | --- | --- |
| `--state` | Yes | Local JSON state path; creates the file and parent directories if missing |
| `--scenario` | Yes | A scenario ID present in the current bank |
| `--score` | Yes | `0`, `1`, or `2`, assessed by the assistant using the response |
| `--fingerprints` | No | Space-separated controlled tags, at most 2 distinct tags; defaults to an empty list |

On success, the command returns `recorded`, cumulative `attempts`, and the current `level`. Every successful call appends an attempt, including repeat practice of the same scenario. The command does not deduplicate attempts; do not blindly retry a write when its outcome is uncertain.

### View statistics: `report`

```bash
python3 scripts/coach.py report --state "/your/private/directory/coach-state.json"
```

Returns total `attempts`, the current `level`, `module_counts`, and `recurring_fingerprints` found in the most recent 12 records.

`report` is read-only. If the specified file does not exist, it reports the initial state—0 attempts and level 1—without creating it.

### View complete help

```bash
python3 scripts/coach.py --help
python3 scripts/coach.py next --help
python3 scripts/coach.py record --help
python3 scripts/coach.py report --help
```

## Scoring and adaptive practice

### The 0–2 scale

| Score | Meaning |
| --- | --- |
| 0 | The core objective was not met, or a clear boundary was crossed |
| 1 | The objective was partly met; one important revision is needed |
| 2 | The information, action, or boundary is clear, and the tone fits the situation |

A score is feedback on one response, not a measurement of personality, emotional intelligence, or relationship quality. The script stores the supplied score; it does not read the response or grade it automatically. Clarify missing context before evaluating.

### Controlled difficulty tags

Record only the 0–2 most relevant tags per attempt.

| Tag | Meaning |
| --- | --- |
| `topic-drift` | Adding unrelated topics before resolving the current issue |
| `context-overload` | Unnecessary background obscuring essential information or action |
| `unclear-action` | An actionable task lacking ownership, the task itself, or completion criteria |
| `attention-burden` | Making the recipient search for essential context that should have been provided |
| `premature-advice` | Offering advice before listening when listening is needed |
| `contact-pretext` | Manufacturing an unnecessary reason for contact to obtain a response |
| `mind-reading` | Treating ambiguous signals as certain knowledge of another person's feelings |
| `boundary-pressure` | Ignoring refusal or pressuring someone to interact |

### How selection and difficulty change

- A tag is treated as recurring when it appears in at least **2 of the most recent 12 records**.
- The selected module is applied first. If multiple candidates remain, the most recently recorded scenario is excluded, then recurring difficulties are prioritized.
- Further ranking uses cumulative module counts and how recently each scenario was practiced, with scenario ID as the final tie-breaker. Selection is deterministic, not random.
- After every **3 cumulative records**, the latest 3 scores are evaluated: three scores of 2 raise difficulty by one; at least two scores of 0 lower it by one; otherwise it stays unchanged. Difficulty is bounded to **1–3**.
- Difficulty is shared across the state file, not calculated separately for each module.

Since each module currently has one base scenario, selecting a module can repeatedly return that scenario. Difficulty changes primarily affect the additional condition. The assistant can generate more varied situations, or a maintainer can expand the bank.

## Records and privacy

Personal training records are not saved by default. Once enabled, the script generates a state file with this structure:

```json
{
  "version": 1,
  "level": 1,
  "history": [
    {
      "at": "2026-09-23T12:00:00+00:00",
      "scenario": "team-1",
      "module": "team",
      "score": 1,
      "fingerprints": ["topic-drift"]
    }
  ]
}
```

The script generates timestamps in UTC. Each record contains only a scenario ID, module, timestamp, score, and controlled tags. It does not write answers, chat transcripts, or names. The state file is not encrypted and does not contain practice preferences.

- `next` and `report` only read; `record` writes.
- Writes use a temporary file and atomic replacement, but there is no multi-process merging. Avoid concurrent writers to the same file.
- Keeping the state file lets you reuse structured history; it does not mean the assistant remembers the complete conversation.
- Deleting your selected state file clears that script's persistent records, but does not delete host chat history or other backups.
- Preserve a damaged state file while investigating. Repeated writes will not repair it; conversational practice without records can continue meanwhile.

For real relationship questions, coaching separates facts, reasonable interpretations, and unknowns. A single emoji or response delay does not establish someone's feelings. The skill is not for psychological diagnosis, manipulation, or pressuring someone into a relationship. It does not automatically send messages or upload records. Situations involving threats or coercion require attention to safety before ordinary communication exercises.

## Extending the scenario bank

Add an object to the array in [assets/scenarios.json](assets/scenarios.json). The following is an example for maintainers; **it is not included in the default bank**. English scenario text is shown here for readability; the same schema supports the existing Chinese content.

```json
{
  "id": "team-2",
  "module": "team",
  "fingerprints": ["topic-drift", "unclear-action"],
  "title": "Pre-release update",
  "situation": "One payment check remains before release. The tester is available this afternoon, and the lead wants to know today whether the release can proceed.",
  "question": "Write a group message that helps the team establish the next step.",
  "focus": "Blocker, ownership confirmation, and next update time",
  "challenges": [
    "No additional condition.",
    "The lead wants a one-sentence status update first.",
    "Another teammate simultaneously raises a feature unrelated to this release."
  ]
}
```

Maintenance guidelines:

1. Use a unique `id`. Preserve IDs referenced by existing state files and avoid changing their modules; doing so can invalidate old history.
2. Use the existing module identifiers from the table above and controlled tags from the script's `TAGS` set.
3. Provide three `challenges` strings ordered by difficulty 1, 2, and 3, and retain the other presentation and evaluation fields.
4. Design meaningfully different situations around the same objective instead of merely replacing names.
5. Assistant-generated scenarios can be used conversationally, but must be added to the bank with valid IDs before `record` can store attempts for them.

Adding tags requires updating `TAGS` in `coach.py`, the scoring reference, and relevant scenarios. Adding modules also requires updating the skill menu, teaching framework, and display documentation. There is no separate comprehensive bank-schema validator; validate the JSON and exercise affected modules after changes.

## Validation and troubleshooting

### Run existing tests

From the skill root, run:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Existing tests cover read-only behavior, persistence, difficulty bounds and decreases, recurring-difficulty scheduling, avoiding immediate repeats, and file preservation with invalid state or input. Tests use temporary directories and do not require personal records. They validate script behavior, not AI coaching quality or every custom scenario field.

After editing the bank, you can also run:

```bash
python3 -m json.tool assets/scenarios.json
python3 scripts/coach.py next --module team
```

### Nothing happens after import. Why?

Importing is not invocation. Confirm that the host loaded the complete folder, then explicitly ask `Use $talkeq to introduce the practice rules`. Reload skills or start a new session if your host requires it.

### Why does the script produce no conversation or feedback?

It returns JSON and only handles scheduling, recording, and statistics. An assistant with the skill loaded conducts the conversation, or you can inspect the output yourself. The script is not a standalone AI coach.

### Why does the same scenario keep appearing?

There is currently one base scenario per module, and `next` does not write history. Repeats are expected without records, without new results, or when selecting a single module. Ask the assistant for a fresh scenario targeting the same objective, or expand the bank.

### Why did difficulty not increase after recording a result?

Difficulty is evaluated only after every 3 cumulative records. The latest 3 must all score 2 to increase it, up to level 3. One score of 2 does not immediately raise difficulty.

### Why was `--scenario` or `--fingerprints` rejected?

Check that the scenario ID exists in the current bank, that tags belong to the controlled list, and that no more than 2 distinct tags were supplied. Run `record --help` for accepted values. Do not use the title of an ad hoc scenario as its ID.

### What should I do if the state file causes an error?

Check that its JSON is complete, `version` is 1, difficulty is 1–3, and historical scenario IDs and modules still match the current bank. Preserve and back up the original before investigating instead of overwriting it. You can also choose a new private state path to start fresh.

### Do I need internet access, an account, or a paid API?

The local script requires none of these. Conversational practice requires an AI host that can load skills. Its account, networking, and billing conditions are determined by the host; this package does not implement a model API integration.

### Can it remind me automatically or remember my previous routine?

The script cannot send reminders. Cross-session scores depend on the state file you authorized, while practice habits require separate storage. Without saved preferences, you may need to provide your routine again in a new conversation.

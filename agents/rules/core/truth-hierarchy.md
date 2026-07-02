# Truth hierarchy

When information conflicts, resolve it using this priority order:

| Priority | Source | Authority |
|---|---|---|
| 1 | Direct user prompt | Session scope |
| 2 | `agents/rules/core/*` | Stable rules |
| 3 | `agents/rules/workflows/*` | Workflow contracts |
| 4 | `agents/rules/roles/*` | Role definitions |
| 5 | `agents/state/*` | Evidence and status only |
| 6 | Archives, logs, summaries, research, backlog | Historical context only |

## Rules

- State, logs, summaries, research, and archive files may be read for context,
  evidence, and recent status.
- State files must never define behavior rules, voice rules, acceptance
  criteria, execution scope, or future run instructions.
- If `agents/state/**` contradicts `agents/rules/**`, the rule layer wins.
- If two rule files contradict each other, stop and escalate to the user or a
  system-review run.
- If a required referenced path does not exist, stop and ask. Do not fabricate
  paths.
- Archived evidence under `agents/state/archive/**` is retained proof, not a
  source for future behavior.

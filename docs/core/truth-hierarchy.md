# Truth hierarchy

When information conflicts, resolve using this strict priority order:

| Priority | Source | Mutability |
|---|---|---|
| 1 | Direct user prompt | Per-session |
| 2 | `docs/core/*` | Stable — change only via system-review |
| 3 | `docs/workflows/*` | Stable — change only via system-review |
| 4 | `docs/agents/*` | Stable — change only via system-review |
| 5 | `state/*` | Volatile — updated every sprint/hotfix |
| 6 | Backlog, logs, summaries, scratch notes | Volatile — may be outdated or contradictory |

## Rules

- Never treat agent-generated logs as canonical truth.
- If a volatile file contradicts a stable file, the stable file wins.
- If two stable files contradict each other, escalate to the user.
- If a referenced path does not exist, **stop and ask** — do not fabricate.

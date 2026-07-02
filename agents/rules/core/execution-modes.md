# Execution modes

## Purpose

Direct user wording controls execution scope before workflow defaults.
Repository workflows may add structure, but they must not widen a user's
explicit negative scope.

## Hard rules

- "Text only", "copy only", "no code", "no tests", "no site code",
  "answer only", and similar phrases are binding constraints.
- Do not escalate to sprint, run tests, write logs, update state, or touch
  undeclared files when the selected mode forbids it.
- Missing optional routes do not block answer-only or text-only work. Stop and
  ask only when a required route for the requested output is missing.
- Human-owned publication, account, outreach, and profile actions stay human
  owned; record repo-local completion separately from those external tasks.

## Modes

| Mode | Use when | Allowed writes | Validation |
|---|---|---|---|
| `answer-only` | The user asks a question or wants discussion only | none | none beyond source reading |
| `text-only` | The user requests prose, copy, docs, drafts, or wording changes | declared prose/copy files only | readback and Markdown/path checks only when relevant |
| `site-copy-only` | The user requests website wording without behavior/design changes | declared copy-bearing site HTML/JSON/XML files only | static site/content check only if structure changed |
| `implementation` | The user requests code, config, behavior, workflow, or system changes | declared files in the task contract | tests/checks by touched area |

## Forbidden by copy modes

`text-only` and `site-copy-only` must not modify CSS, JavaScript, Python,
workflows, scripts, tests, generated data, binary assets, state logs, or sprint
state unless the user explicitly asks for that operational work.

## Workflow interaction

- `operate`, `review`, and `hotfix` obey the selected mode before their normal
  steps.
- `sprint` runs only when a populated sprint contract exists or the user asks
  for sprint planning/execution.
- `system-review` may change stable instruction files only when the user asks
  to audit or refactor the agentic system itself.

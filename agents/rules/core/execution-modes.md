# Execution modes

## Purpose

Direct user wording controls execution scope before workflow defaults. Repository
workflows may add structure only inside the selected mode and run contract.

## Scope selection

Select the smallest mode that can produce the requested output. Then declare the
run contract from `agents/rules/core/run-contract.md` before choosing a workflow.

Execution mode decides whether the run acts. The run contract decides what
surface is touched and what validates it.

Human-owned publication, account, outreach, and profile actions stay human-owned;
record repo-local completion separately from those external tasks.

## Modes

| Mode | Use when | Allowed writes | Validation |
|---|---|---|---|
| `answer-only` | The user asks a question or wants discussion only | none | Source reading, citation, and reasoning review |
| `design` | The user asks to plan, structure, review, or propose work before execution | none by default; candidate artifact only if explicitly requested | Run-contract review |
| `text-only` | The user requests prose, copy, docs, drafts, or wording changes | Declared prose/copy files only | Readback and Markdown/path checks when relevant |
| `site-copy-only` | The user requests website wording without behavior/design changes | Declared copy-bearing site HTML/JSON/XML files only | Site content check when public structure changed |
| `implementation` | The user requests code, config, behavior, workflow, or system changes | Declared files in the run contract | Checks derived from the touched surface |

## Workflow interaction

- `operate`, `review`, and `hotfix` obey the selected mode and run contract
  before their normal steps.
- `plan` produces candidate plans or executable contracts according to the run
  contract.
- `sprint` executes a populated executable contract.
- `system-review` may change stable instruction files when the run contract names
  the affected rule surface.

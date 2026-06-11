# Framework Simplification Proposal

Date: 2026-06-11

## Scope

Reduce sprint verbosity, file proliferation, and unnecessary human-in-loop
assumptions while preserving auditability and safety.

## Decision 1: Review Depth

| Option | Score | Reason |
|---|---:|---|
| Two PairChecks for every non-trivial output | 4 | Safe but expensive and slow for routine artifacts. |
| Risk-tiered review depth | 9 | Matches review effort to blast radius and keeps high-risk work protected. |
| No PairCheck unless user requests it | 3 | Fast but weakens quality gates too much. |

Selected: risk-tiered review depth.

## Decision 2: Closure Model

| Option | Score | Reason |
|---|---:|---|
| Mandatory six closure outputs | 4 | Creates files even when a category is irrelevant. |
| Closure matrix with done/deferred/waived/not-applicable states | 9 | Keeps closure explicit without forcing artifact spam. |
| Free-form closure paragraph | 5 | Less verbose but weaker for agents and status export. |

Selected: closure matrix.

## Decision 3: Trace Policy

| Option | Score | Reason |
|---|---:|---|
| One Markdown file per agent/action | 3 | Traceable but file-prolific and hard for humans. |
| One compact run ledger plus specialist reports only when useful | 9 | Preserves inter-agent memory while keeping human surfaces readable. |
| No trace files, chat only | 2 | Cheap but not recoverable across agent runs. |

Selected: compact run ledger by default.

## Decision 4: Human Approval

| Option | Score | Reason |
|---|---:|---|
| Ask humans before most workflow transitions | 3 | Blocks autonomous execution and creates friction. |
| Require humans only for account/publication/private/destructive decisions | 9 | Keeps important control points without blocking routine CI/docs/site work. |
| Never require approval | 1 | Unsafe for public and account-owned actions. |

Selected: constrained human approval gates.

## Applied Stable-Doc Changes

- `docs/workflows/sprint.md`: risk-tiered review, closure matrix, compact trace,
  and human-approval gate rules.
- `docs/agents/orchestrator.md`: dispatcher-first role with direct execution
  allowed only for low-risk mechanical integration when already in scope.
- `docs/core/constraints.md`, `docs/workflows/operate.md`, and
  `docs/workflows/hotfix.md`: one shared bounded-contract definition to reduce
  duplicated workflow mechanics.
- `tests/test_workflows.py`: workflow invariant updated from mandatory
  checkbox outputs to closure-matrix dimensions and states.

## Migration Notes

- Existing sprint files can keep historical six-output sections, but new
  sprints should use the closure matrix.
- PairCheck assignments should state `skip`, `one`, or `two` based on risk.
- Public user communication should move to site/dashboard pages; Markdown logs
  remain internal planning and inter-agent evidence.

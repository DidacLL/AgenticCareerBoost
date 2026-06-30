# Workflow: Review

## Trigger

User requests maintenance review, pre-merge hygiene, or a bounded consistency
pass.

Review is read-only by default. A mutating review requires explicit wording
such as "fix", "apply", "update", or "rewrite".

## Inputs

- Changed scope, file list, or review request
- `docs/core/execution-modes.md` — selected mode and validation limits
- `docs/core/*` — stable truth (read-only)
- `docs/agents/autoagents.md` — fixed review routines
- One relevant family memory path or `none`

## Steps

1. Select readonly or mutating review from the user's wording.
2. Inspect `ContentSync` concerns first on the declared scope.
3. Inspect Markdown or LaTeX checks only when relevant to touched files.
4. In readonly review, report findings only.
5. In mutating review, each step may fix only domain-local issues; broader
   drift escalates to `system-review`.
6. Update memory only with durable heuristics and record backlog deltas if
   recurring friction was found and the selected mode permits writes.

## Outputs

- Findings by default
- Corrected files in scope only for mutating review
- Optional backlog / state delta
- Optional durable memory note

## Exit criteria

- The review mode is explicit.
- Skipped steps are justified by scope.
- No step widened silently beyond its domain.

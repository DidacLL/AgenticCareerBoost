# Workflow: Review

## Trigger

User requests maintenance review, pre-merge hygiene, or a bounded consistency
pass.

## Inputs

- Changed scope, file list, or review request
- `docs/core/*` — stable truth (read-only)
- `docs/agents/autoagents.md` — fixed review routines
- One relevant family memory path or `none`

## Steps

1. Run `ContentSync` first on the declared scope.
2. Run `MarkdownLintChecker` when scope includes Markdown, docs, site, state,
   or social content.
3. Run `LatexCompileChecker` when scope includes `content/reports/tex/**`.
4. Each step may fix only domain-local issues; broader drift escalates to
   `system-review`.
5. Update memory only with durable heuristics and record backlog deltas if
   recurring friction was found.

## Outputs

- Corrected files in scope
- Optional backlog / state delta
- Optional durable memory note

## Exit criteria

- The chain ran in fixed order.
- Skipped steps are justified by scope.
- No step widened silently beyond its domain.

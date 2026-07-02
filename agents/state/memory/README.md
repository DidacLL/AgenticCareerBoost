# state/memory/

Family-scoped long-term memory for reusable heuristics.

## Rules

- Never treat memory as source of truth for mission, workflows, sprint state,
  or backlog decisions.
- Store only durable heuristics: recurring failures, accepted defaults,
  phrasing rules, source-quality notes, CI quirks, and proven fixes.
- A mutating contract may read or update at most one declared family path.
- Create dated Markdown notes inside a family path only when the lesson is
  likely to help future runs.

## Families

- `state/memory/review/` — `ContentSync`, `MarkdownLintChecker`,
  `LatexCompileChecker`
- `state/memory/social/` — `SocialMediaInvestigator`,
  `SocialMediaPlanner`, `SocialMediaWriter`
- `state/memory/dev/` — created lazily for future technical specialties

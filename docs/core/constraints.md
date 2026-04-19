# Constraints

## Hard constraints

1. **Free / student-accessible tools only** — no paid SaaS unless a free tier
   covers the use case. List every tool publicly when used.
2. **Model-agnostic** — the system must work across chat LLMs, IDE agents,
   CLI agents, and repo-aware assistants. No vendor-specific prompt tricks
   in canonical files.
3. **Human-reviewed truth** — agents may draft, plan, and scaffold. Final truth
   and publication decisions remain human-controlled.
4. **Public inspectability** — the process is part of the proof. Hide nothing
   operational in private-only tooling.
5. **Token-aware brevity** — shorter files with better routing beat giant
   documents. Target ≤80 lines per file; many ≤30.

## Soft constraints

- Prefer checklists and dense Markdown over prose
- Prefer small reusable templates over bespoke formats
- Avoid repeated context across files
- Avoid decorative complexity and premature over-formalization

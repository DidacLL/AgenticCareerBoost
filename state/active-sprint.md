# Sprint output

## Meta

- **Sprint ID**: S-004
- **Goal**: Correct AgenticCareerBoost documentation after market-research drift, preserve the documented career strategy, and separate human-only publication/application tasks.
- **Status**: CLOSED / documentation alignment complete; website implementation excluded.
- **Run ledger**: `state/logs/S-004-docs-alignment/closure.md`

## Tasks

| # | Task | Target | Specialty | Risk | Scope | Writes | Acceptance | Memory | Evidence link |
|---|------|--------|-----------|------|-------|--------|------------|--------|---------------|
| 1 | Career guardrail | Documentation Agent | Strategy docs | high | Career direction | `docs/core/career-direction.md` | Generic backend/data-quality drift is blocked | none | `state/logs/S-004-docs-alignment/closure.md` |
| 2 | Agent routing | Orchestrator | Agent entry | standard | Entry docs | `AGENTS.md` | Career tasks route through guardrail | none | `state/logs/S-004-docs-alignment/closure.md` |
| 3 | README refresh | Documentation Agent | Repo entry | standard | Human entrypoint | `README.md` | Outdated direction is corrected | none | `state/logs/S-004-docs-alignment/closure.md` |
| 4 | Social plan correction | CommunityManager | Campaign docs | high | Relaunch plan | `content/social/plan.md` | Campaign avoids generic data/backend framing | none | `state/logs/S-004-docs-alignment/closure.md` |
| 5 | Human task queue | Documentation Agent | Manual gates | standard | Human actions | `state/human-actions.md` | Manual tasks are clear and separate | none | `state/logs/S-004-docs-alignment/closure.md` |
| 6 | Backlog/state closure | Orchestrator | Sprint state | standard | Volatile state | `state/**` | Closure matrix and backlog updated | none | `state/logs/S-004-docs-alignment/closure.md` |

## Closure matrix

| Dimension | State | Evidence |
|---|---|---|
| Repository artifact(s) | done | `docs/core/career-direction.md`, `AGENTS.md`, `README.md`, social/state docs |
| Website / repo update trace | done | no `site/**` files changed |
| Public-narrative decision | done | relaunch correction recorded |
| Formal engineering documentation | not applicable | no PDF required |
| Condensed technical backlog | done | `state/backlog.md` |
| Condensed narrative backlog | done | `state/backlog.md` |

## Backlog deltas

- Future market research must read `docs/core/career-direction.md` before recommending roles or companies.
- Human publication and application actions live in `state/human-actions.md`.
- Website implementation remains assigned to the separate website LLM.

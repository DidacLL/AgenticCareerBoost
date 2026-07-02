# S-004 documentation alignment closure

Date: 2026-06-26
Workflow: sprint / documentation alignment
Website scope: excluded
Status: closed pending PR review/merge

## Trigger

The user rejected the previous research direction because it drifted toward
backend, data engineering, and data quality. The repository already documented a
more specific strategy: agentic systems, research/applied AI, ML/data systems
only when engineering-heavy, and backend/platform only as product-company
fallback.

## Executed tasks

1. Career guardrail added.
   - File: `docs/core/career-direction.md`
   - Purpose: prevent future agents from recommending generic backend,
     data-quality, BI/reporting, consulting, or AI-hype positioning.

2. Agent entrypoint updated.
   - File: `AGENTS.md`
   - Purpose: route every role, company, LinkedIn, CV, portfolio, and campaign
     task through the career guardrail.

3. README updated.
   - File: `README.md`
   - Purpose: make the repository entrypoint less outdated and more explicit
     about the current career direction.

4. Social plan corrected.
   - File: `content/social/plan.md`
   - Purpose: align relaunch sequence with agentic proof and human-gated
     publication, not generic market positioning.

5. Human-only tasks separated.
   - File: `state/human-actions.md`
   - Purpose: list publication, LinkedIn, GitHub account, company outreach, and
     application tasks that require human action.

6. Relaunch calibration recorded.
   - File: `state/research/s004-relaunch-calibration.md`
   - Purpose: summarize accepted direction, role filters, company filters, and
     preserved avoidance rules.

7. Backlog updated.
   - File: `state/backlog.md`
   - Purpose: add S-004 technical and narrative follow-ups.

8. Sprint state updated.
   - Files: `state/active-sprint.md`, `state/current.md`
   - Purpose: close this documentation sprint and expose next manual gates.

## Review pass A — Strategy guardrail

Verdict: PASS.

Checks:

- Generic backend drift is blocked.
- Data-quality and BI/reporting drift are explicitly rejected.
- Agentic systems remain the visible differentiator.
- Research/applied AI and ML/data systems are preserved as targeted lanes.
- Backend/platform is limited to product-company fallback.

## Review pass B — Scope and human gates

Verdict: PASS.

Checks:

- No `site/**` files were modified.
- Website implementation remains assigned to the separate website LLM.
- Publication tasks are human-gated.
- Account-owned LinkedIn/GitHub changes are human-gated.
- Destructive repository actions are not executed.

## Review pass C — Documentation hygiene

Verdict: PASS.

Checks:

- README now exposes the new guardrail.
- `AGENTS.md` routes future agents through the guardrail.
- Human tasks are readable as checklists.
- Backlog records follow-up work without hiding unresolved manual tasks.
- Tables use short phrases only.

## Closure matrix

| Dimension | State | Evidence |
|---|---|---|
| Repository artifact(s) | done | docs/state/content files |
| Website / repo update trace | done | no site files changed |
| Public-narrative decision | done | relaunch correction recorded |
| Formal engineering documentation | not applicable | no PDF required |
| Condensed technical backlog | done | `state/backlog.md` |
| Condensed narrative backlog | done | `state/backlog.md` |

## Human-required tasks

The human task queue is now centralized in `state/human-actions.md`.

Priority order:

1. Confirm LinkedIn headline/About/Featured alignment.
2. Confirm GitHub account metadata and pinned repos.
3. Remove or neutralize legacy 2022 public surfaces.
4. Approve first three LinkedIn posts.
5. Select the first company outreach batch using the career guardrail.

## Acceptance

Accepted after three review passes. No second remediation round required.

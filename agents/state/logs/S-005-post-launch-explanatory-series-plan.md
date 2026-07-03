# S-005 Prevision: Post-Launch Explanatory Series

## Meta

- **Sprint ID**: S-005
- **Goal**: Explain AgenticCareerBoost after its first LinkedIn presentation by unpacking deployments, structure, history, flaws, and fixes.
- **Status**: planned candidate; not active until user approval

## Context

The first LinkedIn presentation already happened as a human-owned external
publication. It introduced the project as:

- GitHub repository as source of truth;
- small website as curated surface;
- LinkedIn as distribution, not proof;
- agentic workflow failures as part of the engineering story.

S-005 should not repeat a launch announcement. It should turn that opening into
a concise evidence-backed series.

## Tasks

| # | Task | Target | Specialty | Scope | Writes | Acceptance | Memory | Evidence link |
|---|---|---|---|---|---|---|---|---|
| 1 | Evidence inventory | Orchestrator | closure planning | Verify current public artifacts, deployment paths, reports, and S-005 premises | `agents/state/logs/S-005-*.md` only if needed | no invented LinkedIn URL; all post angles point to existing evidence | none | this file |
| 2 | Deployment post package | CommunityManager | LinkedIn planning | Draft angle, evidence links, and first-comment bundle for root vs project-path deploys and PDF loop fix | `agents/work/social/2026-07-linkedin-deployments.md` | explains root site, `/AgenticCareerBoost/`, routing, 404/static-file lesson; no body links | none | site route + routing files |
| 3 | Structure post package | CommunityManager | LinkedIn planning | Draft angle, evidence links, and first-comment bundle for repo architecture | `agents/work/social/2026-07-linkedin-structure.md` | explains `agents/`, `site/`, reports, state, validators, human-owned actions | none | README + project page |
| 4 | History post package | CommunityManager | LinkedIn planning | Draft angle, evidence links, and first-comment bundle for project history | `agents/work/social/2026-07-linkedin-history.md` | covers bootstrap, growth, context poisoning, cleanup, presentation, hardening | none | project-history PDF/source |
| 5 | Source review | PairCheck | narrative/source review | Review post packages for evidence fit, tone, and no stale kickoff framing | review note in sprint closure | PASS or scoped remediation list | none | post packages |
| 6 | Publication gate | Orchestrator | human handoff | Prepare human approval checklist and publication order | `agents/state/human-actions.md` if needed | no agent publishes; exact text remains human-approved | none | human action log |

## Post Angles

1. **Deployments** — The site has two real deployment contexts: root public
   identity and AgenticCareerBoost project path. The bug was not cosmetic; it
   showed why route generation and static file fallback must be deployment-base
   aware.
2. **Structure** — The project works because authority is split: rules define
   behavior, state records evidence, reports explain the arc, site curates the
   public surface, and LinkedIn distributes the story.
3. **History** — The useful part is not that the system never failed. It failed
   through context poisoning, over-ceremony, brittle tests, and deployment
   assumptions, then became clearer through cleanup.

## Pair-Check Assignments

| Task # | PairCheck-A | PairCheck-B | Verdict |
|---|---|---|---|
| 2-4 | Community/source review | Evidence/link review | pending |
| 6 | Human-boundary review | not required unless publication copy changes | pending |

## Closure Artifacts

- [ ] Repository artifact(s)
- [ ] Website / repo update trace
- [ ] Public-narrative decision
- [ ] Formal engineering documentation
- [ ] Condensed technical backlog
- [ ] Condensed narrative backlog

## Backlog Deltas

### Technical

- Full browser-smoke automation remains deferred.
- Report-PDF tracking policy remains deferred.

### Narrative

- First-presentation mode is closed.
- Next posts must unpack deployments, structure, and history.
- Links stay in first comments or Featured surfaces, not LinkedIn post bodies.

## CI Trace

- Commit(s): pending
- Workflow run: pending


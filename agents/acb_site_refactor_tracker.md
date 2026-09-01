# AgenticCareerBoost — Site Refactor Recovery Tracker

**Authority:** `agents/acb_site_refactor_masterplan.md`  
**Branch:** `DidacLl/siterefactor`  
**Recovery baseline:** `336573134c0aed5ce3ed5d46c1e74a615aa7769b`  
**Production cutover:** not authorized

Earlier phase-complete claims are historical and are not acceptance evidence for the current tree.

## Recovery board

| Batch | Purpose | Status | Evidence |
|---|---|---|---|
| R1 | Reset public boundary, control docs, report/site separation and route contract | IN PROGRESS | pending commit/run |
| R2 | Restore content ownership and reconstruct visual hierarchy/monitor | PENDING | — |
| R3 | Harden CV publication, metadata/indexability and objective verification | PENDING | — |
| R4 | Remove dead residue, review full diff, exact-SHA closeout | PENDING | — |
| FINAL VISUAL | User opens `localdeploy.bat` once after all objective checks pass | PENDING | user verdict |

## Non-negotiable state

- `site/` = portfolio source/assets only.
- ACB reports/research/history = repository evidence under `agents/**`, not site assets.
- `agents/**` historical material is evidence, not an active harness.
- Public CV = sole generated document artifact intentionally served by the portfolio.
- Application Tracker/dashboard = not public portfolio surfaces.
- No legacy route aliases/redirect compatibility.
- Astro/Markdown/static architecture retained.
- No external-project loader/federation.
- Retro-vintage videogame/document identity refined, not replaced by generic template styling.
- Project monitor slides derive from canonical project collection data.
- Agent owns objective verification; automation never approves aesthetics.
- One final human visual review only.
- No PR, merge, deployment, main write or root-publication-repo write.

## Defects to close

| ID | Defect | Status |
|---|---|---|
| BOUND-01 | Report catalog/evidence component is incorrectly inside portfolio | OPEN |
| BOUND-02 | Site/deploy CI incorrectly compiles/publishes ACB reports as portfolio inputs | OPEN |
| BOUND-03 | Report local build scripts still copy outputs into `site/` | OPEN |
| BOUND-04 | Root/site guidance still describes reports as site artifacts | OPEN |
| ROUTE-01 | Retired dashboard/tracker/legacy aliases still generate redirects | OPEN |
| OWN-01 | Authored page/UI copy is scattered through layouts/pages/scripts | OPEN |
| CONTENT-01 | ACB/CV/Focus migration lost useful structure/context | OPEN |
| VIS-01 | Shell is rigid and visual treatment is still glitchy/over-filtered | OPEN |
| VIS-02 | Monitor lost project metadata/links and is only an image carousel | OPEN |
| META-01 | OG/Twitter metadata incomplete | OPEN |
| SEO-01 | `robots.txt` does not respect indexable build mode | OPEN |
| CV-01 | CV artifact validation has an invalid path-prefix comparison | OPEN |
| CI-01 | Site Check does not cover every recovery HEAD | OPEN |
| CI-02 | Browser smoke misses normal HTTP 4xx/5xx responses and image decode failures | OPEN |
| DOC-01 | Root README/AGENTS were over-trimmed during refactor | OPEN |

## Verification ledger

| Recovery SHA | Site Check run | Build root | Build mirror | Static verifier | Browser smoke | Notes |
|---|---|---|---|---|---|---|
| `336573134c0aed5ce3ed5d46c1e74a615aa7769b` | `33499345620` | PASS | PASS | PASS | PASS | baseline checks were too narrow; audit found defects above |

## Final gate

Before asking for the user's visual verdict:

1. all defects above must be CLOSED or explicitly deferred by the user;
2. exact final SHA must have a green Site Check;
3. full recovery diff must be inspected for unintended scope;
4. full branch-vs-main diff must be inspected for refactor residue;
5. no production surface may have been modified.

Then the only user action is: double-click `localdeploy.bat` and give the subjective visual verdict.
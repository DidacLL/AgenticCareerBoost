# AgenticCareerBoost — Site Refactor Recovery Tracker

**Status:** CLOSED EVIDENCE RECORD — not an active harness  
**Branch used for recovery:** `DidacLl/siterefactor`  
**Recovery baseline:** `336573134c0aed5ce3ed5d46c1e74a615aa7769b`  
**Recovery acceptance milestone:** `872e6c5ed2583da8b5f87eda84f508de083969f7`  
**Post-recovery hardening:** tracked in PR #73 and branch history  
**Production cutover:** not authorized

This tracker records how the recovery was closed. It is historical evidence, not a source of current branch state or instructions for future agents. Later pre-merge maintenance work — navigation persistence, authoring simplification, shell corrections, CV ownership fixes and final audit cleanup — belongs to PR #73 and should be read from the repository itself rather than inferred from the milestone SHA above.

## Recovery result

| Batch | Result | Evidence |
|---|---|---|
| R1 — boundaries/authority | CLOSED | report/site separation, retired public scratch routes; `65a98c30…`, run `33504203240` |
| R2 — content/design recovery | CLOSED | content ownership, visual reconstruction, user-feedback pass; `34104a67…`, run `33510213693` |
| R3 — publication/verification | CLOSED | canonical/mirror policy, CV contract, hardened static/browser checks; `cc4235ed…`, run `33505819136` |
| R4 — closeout/cleanup | CLOSED | expanded CRT evidence + unused site-asset pruning; `1f9ed918…` run `33510831603`, `872e6c5e…` run `33514536384` |

## Closed defects

- **BOUND:** reports/research/history are repository evidence under `agents/**`, not portfolio files or build inputs.
- **ROUTES:** dashboard, tracker demo, old aliases and duplicate `/focus/**` surface are retired.
- **OWNERSHIP:** authored content has explicit Markdown/data owners; shared identity/UI data has one global owner.
- **CONTENT:** ACB history, CV facts/source/PDF access and historical blog context retained without turning reports into site downloads.
- **VISUAL:** banner restored to header; avatar restored; heading scale restrained; CRT/hologram character restored; normal and expanded monitor sizes corrected; Blog/CV/Contact regain useful imagery and visual variation.
- **META/SEO:** canonical, OG/Twitter metadata, robots and sitemap follow build mode.
- **CV:** source/build support is owned by `agents/cv/**`; its shared header artwork is not a site asset, and required CI compiles the actual public CV.
- **CI:** PRs touching the site or public CV receive non-deploy Site Check coverage; HTTP errors, decoded images, navigation, theme, CRT behavior, overflow and no-JS content are checked at 1920/1366/768/390.
- **CLEANUP:** obsolete renderer/DSL residue and unused `site/assets` material are no longer shipped in the portfolio tree.
- **DOCS:** root/agents guidance states privacy boundaries and clearly marks historical agent material as evidence rather than an active harness.

## Route contract

Top-level portfolio routes are Home, Projects, Blog, CV and Contact, plus static 404. Project, post and CV detail routes are discovered from their Markdown filenames; adding an entry does not require a second route registry. Role-specific presentation exists only under `/cv/*`; there is no separate Focus concept.

## Recovery verification ledger

| SHA | Site Check | Result | Purpose |
|---|---|---|---|
| `65a98c30…` | `33504203240` | PASS | first clean boundary recovery |
| `cbc6daaa…` | `33505589811` | PASS | mobile overflow corrected at source |
| `cc4235ed…` | `33505819136` | PASS | hardened root/mirror + browser contract |
| `1d1ef461…` | `33506484199` | PASS | 1920-first visual evidence |
| `34104a67…` | `33510213693` | PASS | user visual-feedback corrections |
| `1f9ed918…` | `33510831603` | PASS | expanded CRT 1920 evidence |
| `872e6c5e…` | `33514536384` | PASS | recovery asset cleanup milestone |

## Boundary after recovery

Merge/deploy/main/root-publication changes were outside this recovery record. Current integration state must be taken from PR #73 and the repository branch, not from this historical tracker.

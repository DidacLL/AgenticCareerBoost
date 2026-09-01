# AgenticCareerBoost — Site Refactor Recovery Tracker

**Status:** ENGINEERING COMPLETE — closed evidence record, not an active harness  
**Branch:** `DidacLl/siterefactor`  
**Recovery baseline:** `336573134c0aed5ce3ed5d46c1e74a615aa7769b`  
**Accepted implementation:** `872e6c5ed2583da8b5f87eda84f508de083969f7`  
**Production cutover:** not authorized

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
- **CV:** artifact destination contract is valid and checked.
- **CI:** every branch HEAD receives non-deploy Site Check; HTTP errors, decoded images, navigation, theme, CRT behavior, overflow and no-JS content are checked at 1920/1366/768/390.
- **CLEANUP:** obsolete renderer/DSL residue and unused `site/assets` material, including unused generated-image sets and alternate logos, are no longer shipped in the portfolio tree.
- **DOCS:** root/agents guidance states privacy boundaries and clearly marks historical agent material as evidence rather than an active harness.

## Final route contract

Portfolio routes are Home, Projects + four project pages, Blog + three posts, four CV views, Contact and static 404. Role-specific presentation exists only under `/cv/*`; there is no separate Focus concept.

## Verification ledger

| SHA | Site Check | Result | Purpose |
|---|---|---|---|
| `65a98c30…` | `33504203240` | PASS | first clean boundary recovery |
| `cbc6daaa…` | `33505589811` | PASS | mobile overflow corrected at source |
| `cc4235ed…` | `33505819136` | PASS | hardened root/mirror + browser contract |
| `1d1ef461…` | `33506484199` | PASS | 1920-first visual evidence |
| `34104a67…` | `33510213693` | PASS | user visual-feedback corrections |
| `1f9ed918…` | `33510831603` | PASS | expanded CRT 1920 evidence |
| `872e6c5e…` | `33514536384` | PASS | final unused-asset cleanup |

## Remaining boundary

There is no open engineering task in this recovery record. A final local look with `localdeploy.bat` can be used for the user's subjective acceptance before any production cutover. Merge/deploy/main/root-publication changes remain outside this recovery and require a separate explicit instruction.

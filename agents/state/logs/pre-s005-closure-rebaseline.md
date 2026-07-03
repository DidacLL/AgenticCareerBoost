# Pre-S-005 Closure And Rebaseline

- **Date**: 2026-07-03
- **Type**: Closure / planning rebaseline
- **Sprint ID**: none
- **S-005 status**: rebaselined, not started

## Summary

This closure records the recovery work completed after S-004.5 and before S-005.
The first LinkedIn presentation of AgenticCareerBoost has already happened as a
human-owned external action. The next sprint must therefore explain the
deployments, structure, history, flaws, and fixes instead of treating S-005 as
an initial announcement.

## Faced Issues

| Issue | Resolution | Evidence |
|---|---|---|
| Deployment-base routing escaped from `/AgenticCareerBoost/` to root paths. | Router now derives deployment base and emits base-aware app routes. | `site/assets/js/router.js`; static validation. |
| GitHub Pages 404 converted missing static files into SPA hash routes. | `404.html` stops static-file fallback instead of rewriting `/files/**` to `#/files/**`. | `site/404.html`; validator and pytest markers. |
| CV/cover-letter PDFs depended on stale committed files. | Career artifacts build from `agents/cv/artifacts.json` and deploy into `site/files/**`. | `agents/cv/artifacts.json`; local/CI build scripts. |
| AI-authored tests tried to enforce authorial LaTeX content decisions. | Tests now check integration contracts, not prose/layout/content style in user-owned TeX. | `agents/tests/test_agentic_contracts.py`. |
| Filename-based validation overfit one hotfix into architecture. | Validators read the artifact manifest and static-file behavior instead of hard-coded artifact names. | `agents/tools/validate_static_site.py`. |
| Generated TeX/PDF outputs were not consistently ignored. | Generated CV/letter outputs are ignored; report PDFs remain tracked until a later policy run. | `.gitignore`; `git check-ignore`. |
| Root site and project-path deploys behave differently. | Runtime URLs and site JSON distinguish app routes from static files under both bases. | browser smoke checks; route/file tests. |

## Technical Refactor Audit

No broader refactor is needed before S-005. The remaining architecture is
deliberately narrow:

- app routes stay app-internal;
- static files resolve through deployment-base-aware asset URLs;
- career PDFs are generated from a manifest;
- generated career artifacts are ignored;
- site validation checks behavior contracts, not authorial content.

Deferred larger items remain separate backlog concerns: GitHub Action SHA
pinning, full browser-smoke automation, `components.js` decomposition, global
dependency locking, and report-PDF artifact policy.

## Public Narrative Decision

The first published LinkedIn post framed AgenticCareerBoost as a public system
for career positioning: GitHub as source of truth, the website as curated
surface, and LinkedIn as distribution rather than proof. It also named the
failure modes directly: documentation loops, over-formalized closure, tests
running for text-only changes, and coherent copy drifting away from strategy.

S-005 must continue from that truth. The next posts should unpack:

1. deployments and routing failures;
2. repository/site/report structure;
3. development history and post-launch hardening.

No LinkedIn URL is recorded here because the exact URL was not provided.

## Closure Matrix

| Dimension | State | Evidence |
|---|---|---|
| Repository artifacts | done | Routing, CV pipeline, validation, and ignore contracts implemented before this closure. |
| Website / repo update trace | done | Project history and public project page are updated to include post-launch hardening. |
| Public-narrative decision | done | S-005 is now a post-launch explanatory series. |
| Formal engineering documentation | done | Project-history report source includes the latest recovery stage. |
| Condensed technical backlog | done | Deferred refactors remain separate; no pre-S-005 blocker. |
| Condensed narrative backlog | done | S-005 post angles are recorded in the rebaseline plan. |

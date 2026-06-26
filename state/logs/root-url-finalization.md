# Root URL finalization review

Date: 2026-06-26

## Context

The main public site moved from the AgenticCareerBoost project path to the root GitHub Pages URL:

- Main public site: `https://didacll.github.io/`
- Source project/repository: `https://github.com/DidacLL/AgenticCareerBoost`

`codex/contentupdate` was merged into `main`, but post-merge review found a small amount of residual URL drift in live static-site pages and the web CV page.

## Verification performed

- Compared `codex/contentupdate` against `main`: branch had no unmerged work and was behind `main`, confirming prior cleanup had been merged.
- Checked current public-site source on `main` for residual `https://didacll.github.io/AgenticCareerBoost/` references.
- Confirmed current root-site policy exists in `docs/link-guidelines.md`.
- Confirmed branch protection blocked direct writes to `main`, so the remaining corrections were staged through `codex/root-url-state-finalization`.
- Checked commit status through the connector; no commit status entries or PR-triggered workflow runs were visible for the current `main` commit, so final CI must be confirmed through pull-request checks.

## Follow-up branch contents

The branch `codex/root-url-state-finalization` updates:

- `site/notes/index.html`
- `site/dashboard/index.html`
- `site/projects/p3ctex/index.html`
- `site/projects/ironbank/index.html`
- `site/curriculum/index.html`
- `state/backlog.md`
- `state/current.md`

## Result

The project state now records the root-site migration as merged but not fully closed until the follow-up branch passes PR checks and merges.

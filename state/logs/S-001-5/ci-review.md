# CI review — S-001.5

- **Date**: 2026-04-27
- **Scope**: GitHub Actions deploy/lint/report checks after the first S-001.5 push
- **Verdict**: STATIC DEPLOYMENT PATH SELECTED

## Findings

1. `data/public-status.json` was being collapsed by `.github/scripts/export_status.py`: the exporter wrote an empty artifact list and selected the oldest closure row as the latest closure.
2. The Pages workflow failed at `actions/configure-pages@v5` because the repository Pages site was not enabled/configured for GitHub Actions.
3. The LaTeX workflow compiled reports and uploaded artifacts, but the auto-commit step could fail the job when another workflow moved `main`.
4. Markdown lint was enforcing prose rules against sprint research, logs, and paste-ready public-copy drafts. Those artifacts intentionally contain dense tables, bare URLs, and snippet blocks.
5. After the workflow fix, `Build and deploy site` reached `actions/configure-pages@v5` but failed with `Resource not accessible by integration` while creating the Pages site. This confirms the repository owner must enable Pages or grant an equivalent admin-level setting; the default `GITHUB_TOKEN` cannot create it.
6. Because the fair deadline is immediate, the site deployment path was changed to plain static HTML in `site/public/` published to the `gh-pages` branch. This avoids Jekyll rendering and avoids the Pages API enablement step inside Actions.

## Applied Remediation

- Status exporter now preserves closure artifacts and selects the newest closure row.
- Pages workflow now validates `site/public/` and publishes it to the `gh-pages` branch.
- LaTeX auto-commit is non-blocking; report compilation and artifact upload remain blocking.
- Markdown lint policy now suppresses rules that are noisy for generated sprint/research/public-copy artifacts while keeping the repo-wide lint job active.
- Markdown lint ignores `bootstrap/user_data.md`; it is a bootstrap input file with personal profile notes, not a public Markdown artifact.

## Remaining Action

1. Push the static site commit.
2. Confirm the `Publish static site` workflow creates/updates the `gh-pages` branch.
3. Verify `https://didacll.github.io/AgenticCareerBoost/` and the CV PDF link.
4. If the URL still returns 404, enable Pages manually with Source `Deploy from branch`, Branch `gh-pages`, Folder `/`.

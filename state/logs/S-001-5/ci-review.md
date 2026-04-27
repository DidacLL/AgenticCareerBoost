# CI review — S-001.5

- **Date**: 2026-04-27
- **Scope**: GitHub Actions deploy/lint/report checks after the first S-001.5 push
- **Verdict**: FIXES APPLIED; remote verification pending

## Findings

1. `data/public-status.json` was being collapsed by `.github/scripts/export_status.py`: the exporter wrote an empty artifact list and selected the oldest closure row as the latest closure.
2. The Pages workflow failed at `actions/configure-pages@v5` because the repository Pages site was not enabled/configured for GitHub Actions.
3. The LaTeX workflow compiled reports and uploaded artifacts, but the auto-commit step could fail the job when another workflow moved `main`.
4. Markdown lint was enforcing prose rules against sprint research, logs, and paste-ready public-copy drafts. Those artifacts intentionally contain dense tables, bare URLs, and snippet blocks.

## Applied Remediation

- Status exporter now preserves closure artifacts and selects the newest closure row.
- Pages workflow now requests Pages enablement through `actions/configure-pages`.
- LaTeX auto-commit is non-blocking; report compilation and artifact upload remain blocking.
- Markdown lint policy now suppresses rules that are noisy for generated sprint/research/public-copy artifacts while keeping the repo-wide lint job active.
- Markdown lint ignores `bootstrap/user_data.md`; it is a bootstrap input file with personal profile notes, not a public Markdown artifact.

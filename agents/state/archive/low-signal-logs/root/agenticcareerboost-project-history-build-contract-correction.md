# AgenticCareerBoost Project History Build Contract Correction

Date: 2026-07-02
Mode: system-review documentation correction
Sprint authority: none; S-005 remains untouched.

## Trigger

During review of the project-history evidence run, the user rejected an agent
note that described copying the generated PDF into `site/files/reports`.

That rejection is correct. Public human-facing report PDFs must be produced by
the LaTeX build contract itself. A manual copy is not acceptable as a separate
agent step because it hides the publication path and can leave future report
links dependent on undocumented operator behavior.

## Correction

- Treat `agents/reports/tex/build-local.ps1` and
  `agents/reports/tex/build-local.sh` as the publication path for public report
  PDFs.
- Keep `site/files/reports` as the public output location for downloadable
  reports.
- Add a regression test requiring the build scripts and public report README to
  document and enforce build-driven publication.

## Evidence boundary

This note corrects the run process. It does not restore discarded draft bodies,
does not consume S-005, and does not change `agents/state/active-sprint.md`.

## Validation status

Validated after shell execution became available again:

- `Set-Location agents\reports\tex; .\build-local.ps1 -Target all` — PASS.
  The script generated report PDFs and published them into
  `site/files/reports`; no manual public-PDF copy remains in the accepted
  process.
- `python agents/tools/export_status.py` — PASS.
- `python agents/tools/validate_static_site.py` — PASS.
- `bash agents/tools/validate_links.sh` — PASS.
- `python -m pytest agents/tests -q` — PASS.
- Browser and local PDF fetch checks — PASS.

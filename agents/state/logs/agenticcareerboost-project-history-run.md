# AgenticCareerBoost project history narrative run

- **Date**: 2026-07-02
- **Type**: Site/documentation evidence narrative run
- **Sprint ID**: none
- **S-005 status**: untouched; remains next LinkedIn campaign kickoff seed

## Summary

Expanded the AgenticCareerBoost project page from a compact status card into a
public evidence narrative. The page now explains what the project proves,
surfaces the six-stage development history, exposes every public report PDF,
and points readers from the site into formal evidence.

## Public narrative

The shared timeline for the website and later social posts is:

1. Bootstrap Launch
2. Initial Growth
3. Context Poisoning
4. End of Semester Pause
5. Failed Campaign Kickoff
6. Cleanup And Current Version

## Documentation coverage

The documentation-gap audit was written into the formal LaTeX evidence layer,
not onto the public site page. The audit lives in
`agents/reports/tex/guides/agenticcareerboost-project-history.tex` and records:

- S-000, S-001, S-001.5R, refactor, reconciliation, and project-history stages
  have formal PDF coverage.
- S-002, S-003, S-004, and S-004.5 are log-backed evidence and do not need
  standalone PDF backfill unless future public claims require it.
- Discarded profile/social draft bodies remain intentionally deleted.

## Site/runtime changes

- `site/content/projects.json` now contains the richer AgenticCareerBoost
  project narrative and all public report PDF links.
- `site/assets/js/components.js` honors `newTab: true` so report PDFs can open
  in a separate tab.
- Tests cover timeline labels, report-library exposure, and new-tab report
  metadata.

## Formal report

- Source:
  `agents/reports/tex/guides/agenticcareerboost-project-history.tex`.
- Public PDF:
  `site/files/reports/agenticcareerboost-project-history.pdf`.
- Publication path:
  `agents/reports/tex/build-local.ps1 -Target all` generated the PDF and
  published it into `site/files/reports`; no separate manual PDF copy step is
  part of the accepted process.

## Validation

Passed validation:

- `Set-Location agents\reports\tex; .\build-local.ps1 -Target all` — PASS.
  `latexmk` was unavailable locally, so the script used the documented 3-pass
  `pdflatex` fallback and published every report PDF into `site/files/reports`.
- `python agents/tools/export_status.py` — PASS; wrote
  `site\data\status.json`.
- `python agents/tools/validate_static_site.py` — PASS.
- `bash agents/tools/validate_links.sh` — PASS; 46 internal Markdown links
  checked.
- `python -m pytest agents/tests -q` — PASS; 15 tests passed.
- Browser checks — PASS for `/`, `/projects`,
  `/projects/agentic-career-boost`, `/dashboard`, and `/cv/ml`; no console
  errors, no broken images, project timeline rendered, documentation-gap text
  stayed off the public site, report links resolved under
  `/site/files/reports`, and report links used `_blank` with
  `noopener noreferrer`.
- Local PDF fetch check — PASS; every exposed report PDF returned
  `200 application/pdf`.

## Closure note

This run prepares the shared narrative for a later social-post run. It does not
publish social posts, reopen S-005, restore discarded draft bodies, or create a
new site architecture.

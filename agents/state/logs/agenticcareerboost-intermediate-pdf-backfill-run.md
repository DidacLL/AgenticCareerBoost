# AgenticCareerBoost intermediate PDF backfill run

- **Date**: 2026-07-02
- **Type**: Documentation/report backfill
- **Sprint ID**: none
- **S-005 status**: untouched

## Trigger

After the project-history narrative run, the user chose to backfill full PDFs
for the intermediate historical stages that were previously documented as
log-backed evidence only.

## Scope

Create human-facing formal PDF sources for:

- S-002R restart refresh;
- S-003 website OS clarity;
- S-004 documentation alignment;
- S-004.5 site quality.

The reports summarize existing evidence from `agents/state/logs/**`. They do
not reopen historical sprints, restore discarded draft bodies, or define future
behavior.

## Files added

- `agents/reports/tex/sprints/s002-restart-refresh.tex`
- `agents/reports/tex/sprints/s003-website-os-clarity.tex`
- `agents/reports/tex/sprints/s004-documentation-alignment.tex`
- `agents/reports/tex/sprints/s0045-site-quality.tex`

## Publication/index changes

- `README.md` now lists the intermediate PDFs.
- `agents/reports/tex/README.md` now lists the new source documents.
- `site/files/reports/README.md` now lists the expected public PDFs.
- `site/content/projects.json` exposes the new report PDFs in the
  AgenticCareerBoost evidence library with `newTab: true`.
- `agents/reports/tex/guides/agenticcareerboost-project-history.tex` now says
  the intermediate stages are backfilled with formal PDFs instead of remaining
  accepted log-only gaps.

## Evidence boundary

The reports are retrospective summaries grounded in existing logs. They are
evidence only. Current behavior remains defined by `agents/rules/**`.
`agents/state/**` and reports explain history and validation, but they do not
override execution modes, role rules, public-copy rules, or career guardrails.

Discarded profile/social draft bodies remain intentionally deleted.

## Validation status

Passed validation:

- `Set-Location agents\reports\tex; .\build-local.ps1 -Target all` — PASS.
  First run exposed a LaTeX underscore issue in the S-003 path table; the source
  was fixed and the rerun compiled all reports. The build script published the
  new report PDFs into `site/files/reports`.
- `python agents/tools/export_status.py` — PASS; wrote
  `site\data\status.json`.
- `python agents/tools/validate_static_site.py` — PASS.
- `bash agents/tools/validate_links.sh` — PASS; 50 internal Markdown links
  checked.
- `python -m pytest agents/tests -q` — PASS; 15 tests passed. First run caught
  one stale historical `docs/core/` token in the S-004 backfill, which was
  reworded to avoid reintroducing live path drift.
- Browser route/report-link checks on local server — PASS. `/`, `/projects`,
  `/projects/agentic-career-boost`, `/dashboard`, and `/cv/ml` rendered with no
  console errors or broken images. The project page renders the four new report
  titles, all report PDF links use `_blank` and `noopener noreferrer`, and all
  exposed report PDFs return `200 application/pdf`.

# AgenticSystem structure simplification run

- **Date**: 2026-07-02
- **Type**: AgenticSystem refactor run
- **Sprint ID**: none
- **S-005 status**: untouched; remains next LinkedIn campaign kickoff seed

## Summary

Collapsed internal agent material under `agents/`, kept public runtime under
`site/`, and reduced the root to platform and SEO entrypoints. Preserved origin
and sprint evidence while removing discarded drafts, stale style-book material,
manual public-status copies, duplicate root assets, and generated benchmark
pressure.

## Evidence boundaries

- `agents/rules/**` is the authoritative rule layer.
- `agents/state/**` is evidence/status only and cannot define future behavior.
- Bootstrap origin files are retained under `agents/state/archive/origin/` with
  non-authoritative headers.
- Historical logs, summaries, reports, and research remain available as proof,
  not operating instructions.

## Public artifacts

- Root Pages entrypoints: `index.html`, `404.html`, `.nojekyll`, `robots.txt`,
  `sitemap.xml`.
- Runtime source: `site/**`.
- Published reports: `site/files/reports/**`.
- Published CV: `site/files/cv/didac-llorens-cv.pdf`.
- Generated status projection: `site/data/status.json` from
  `agents/state/**`.

## Validation

- `python agents/tools/export_status.py` passed.
- `python agents/tools/validate_static_site.py` passed.
- `bash agents/tools/validate_links.sh` passed.
- `python -m pytest agents/tests -q` passed.
- `agents/reports/tex/build-local.ps1` passed for all reports and guides.
- Browser validation passed for `/`, `/projects`, `/dashboard`, `/cv/ml`, and
  `/blog` through local HTTP fallback routing with no console errors or broken
  images.

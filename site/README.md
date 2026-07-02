# site/

Canonical source for public website runtime files.

The site is plain static HTML/CSS/JS. GitHub Pages is deployed from the
repository root so root SEO entrypoints can stay at canonical URLs, while site
runtime dependencies stay under `site/`.

## Rules

- Edit HTML, CSS, and JavaScript here.
- Do not add a site generator unless a future sprint proves it is worth the
  dependency.
- Published PDFs remain in `site/files/reports/`; the published CV remains in
  `site/files/cv/`.
- Generated runtime status lives at `site/data/status.json` and comes from
  `agents/tools/export_status.py`; do not edit it by hand.

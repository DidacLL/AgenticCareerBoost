# site/

Canonical source for the public GitHub Pages site.

The site is plain static HTML/CSS/JS. GitHub Actions validates the source files
and uploads this directory directly as the Pages artifact.

## Rules

- Edit HTML, CSS, and JavaScript here.
- Do not add a site generator unless a future sprint proves it is worth the
  dependency.
- Published PDFs remain in `content/reports/build/`.
- S-002 owns the full visual rebuild; this folder is the stable source root.

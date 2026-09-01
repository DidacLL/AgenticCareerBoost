# site/

Astro source for the public static site.

Content is Markdown in src/content/; layouts and components render it at build time. Public assets stay under assets/, including generated CV and report PDFs under assets/files/. Only theme persistence and the portrait gallery use client JavaScript.

Run localdeploy.bat from the repository root for local viewing. Production deployment remains main-only; this branch does not deploy.

Generated artifacts are supplied by the production build; missing PDFs do not block local viewing.

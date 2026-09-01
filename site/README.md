# site/

Astro source for the public portfolio.

Content is Markdown in `src/content/`; layouts and components render it at build
time. Existing portfolio images stay under `assets/img/`. The selected public CV
is generated under `assets/files/cv/` for production builds.

This tree contains only material actually used by the portfolio. ACB reports,
research, tracker/status output, application material, and historical harness
evidence live outside `site/` and are not portfolio build inputs.

Only theme persistence and the monitor/gallery use client JavaScript.

Run `localdeploy.bat` from the repository root for local viewing. Generated CV
output is not required to inspect the local UI. Production deployment remains
main-only; this branch does not deploy.
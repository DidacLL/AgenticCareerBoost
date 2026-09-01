# site/

Astro source for the public portfolio.

Content is Markdown in `src/content/`; layouts and components render it at build
time. Existing portfolio images stay under `assets/img/`. The selected public CV
is generated under `assets/files/cv/` for production builds.

This tree contains only material actually used by the portfolio. ACB reports,
research, tracker/status output, application material, and historical harness
evidence live outside `site/` and are not portfolio build inputs.

Runtime JavaScript is limited to Astro's lightweight client router plus theme
persistence and the monitor/gallery. The site still renders as ordinary static
HTML and remains usable without JavaScript.

## Publishing content

The source filename owns the route slug. Do not add a `slug` field, create route
folders, edit `dist/`, or register entries in an index.

To publish a blog article, add exactly one file:

```text
src/content/posts/my-article.md
```

with the minimum frontmatter:

```md
---
title: My article
description: One sentence used by the index and page metadata.
date: 2026-09-01
---

Article body in Markdown.
```

`tags`, `image`, and `imageAlt` are optional. The filename automatically becomes
`/blog/my-article/`, the Blog index discovers it automatically, and Astro creates
the generated `dist/blog/my-article/index.html` only during the build.

Projects follow the same filename-as-slug rule under `src/content/projects/`;
their richer frontmatter controls ordering, project metadata, and imagery.

Run `localdeploy.bat` from the repository root for local viewing. Generated CV
output is not required to inspect the local UI. Production deployment remains
main-only; this branch does not deploy.

# `site/` — public portfolio

This directory is the source of the public portfolio. It is intentionally a small static-publishing system rather than a CMS or SPA application: authored Markdown and typed site data are compiled by Astro into ordinary static HTML.

The portfolio is designed to be easy to maintain, portable between `/` and a repository subpath, usable without JavaScript, multilingual without a client translation runtime, and visually distinctive without depending on a large client runtime.

## Stack

- **Astro 7.2.9**
- **`@astrojs/sitemap` 3.7.3**
- Astro components/layouts and static route generation
- TypeScript for typed configuration/data and locale helpers
- Markdown content collections
- plain CSS
- small vanilla-JavaScript behaviors for theme and CRT/gallery interaction
- Astro client navigation for persistent shell transitions
- static multilingual output: English + Spanish + Catalan
- static HTML output, directory-format routes and trailing slashes
- GitHub Actions + GitHub Pages
- Chromium browser smoke tests

Node `>=22.12` is supported locally; CI currently uses Node `24.20.0`.

## Source ownership

```text
src/content/            authored page/project/post/CV-view content and translations
src/data/site.ts        global identity, navigation, localized UI copy and shared public links
src/components/         reusable presentation primitives
src/layouts/            document/project/post/CV composition
src/views/              shared page composition used by all locales
src/pages/              thin Astro route entry points
src/lib/i18n.ts         locale/content-id ownership
src/lib/paths.ts        deployment-base and locale-aware path helpers
src/scripts/            client behavior (theme, CRT/gallery)
assets/                 only assets actually served by the portfolio
scripts/                build, route, link and browser verification
```

Public prose belongs in Markdown or the appropriate shared data owner, not hardcoded repeatedly in route/render logic.

Generated `dist/` output is not source and must never be maintained by hand.

## Publishing content

The filename owns the route slug. There is no manual content registry and no `slug` field to keep in sync.

### Languages

English is the canonical source language and keeps the original unprefixed routes:

```text
/                        English Home
/projects/p3ctex/        English project
/blog/my-article/        English article
```

Spanish and Catalan use language prefixes while preserving the same technical route segments and slugs:

```text
/es/
/es/projects/p3ctex/
/es/blog/my-article/

/ca/
/ca/projects/p3ctex/
/ca/blog/my-article/
```

The source layout mirrors that rule. English remains flat; translations use a locale directory and the **same filename**:

```text
src/content/posts/my-article.md       English
src/content/posts/es/my-article.md    Spanish
src/content/posts/ca/my-article.md    Catalan

src/content/projects/p3ctex.md        English
src/content/projects/es/p3ctex.md     Spanish
src/content/projects/ca/p3ctex.md     Catalan
```

The current publication contract requires translation parity for public pages, projects, posts and CV web views. `content-routes.mjs` fails CI if an English content ID does not have matching `es/` and `ca/` content, or if a translation invents an extra ID.

Route segments such as `projects`, `blog`, `cv` and the filename-derived slugs are intentionally not translated. This keeps links stable and makes locale switching a reversible transformation of the same semantic route.

Every language version is generated as a complete static HTML document. There is no browser-side translation lookup. Pages emit their own `lang`, canonical URL, `hreflang` alternates and `x-default` metadata.

### Blog

To publish a blog article, create the English source:

```text
src/content/posts/my-article.md
```

Minimum frontmatter:

```md
---
title: My article
description: One sentence used by the index and page metadata.
date: 2026-09-01
---

Article body in Markdown.
```

`tags`, `image`, and `imageAlt` are optional.

`my-article.md` automatically becomes `/blog/my-article/`; the Blog index discovers it from the collection and Astro creates `dist/blog/my-article/index.html` only during the build.

For the current three-language publication contract, add translations with the same filename under `posts/es/` and `posts/ca/`. No route registration is required.

### Projects

Projects follow the same filename-as-slug rule under:

```text
src/content/projects/
```

Their frontmatter additionally owns project ordering, status, repository links, imagery and structured project facts. Spanish and Catalan project sources live under `projects/es/` and `projects/ca/` with matching filenames.

Project Markdown can contain normal links, downloadable external artifacts and Markdown images. The project layout renders the Markdown body directly; a project does not need a custom Astro component merely to show screenshots or link examples.

### Other pages

Page-level authored prose lives under `src/content/pages/`. CV web views live under `src/content/cv/` and are rendered through the shared CV layout.

The Spanish and Catalan CV **web views** are translated. The generated LaTeX PDF remains the canonical English public PDF and is labelled as such from translated views.

## Static architecture

Astro is configured with:

- `output: "static"`
- `build.format: "directory"`
- `trailingSlash: "always"`
- `publicDir: "./assets"`
- deployment origin/base injected through environment variables

The same source tree therefore builds correctly for both the canonical root and the repository mirror without embedding production prefixes in authored content.

English route files and `[locale]` route files are thin wrappers around the same views. Presentation logic is not copied per language; locale selects content, UI copy and path generation.

The sitemap integration is enabled only for indexable builds. Robots/canonical/OpenGraph behavior follows the build's publication mode.

## Client behavior

The site remains static HTML. JavaScript is intentionally limited.

Astro client navigation keeps the global shell stable during internal navigation so banner/avatar/header imagery do not visibly reload on every route change. Theme state and CRT/gallery behavior are re-initialized idempotently after client-side navigation.

The ENG / CAST / CAT selector is ordinary navigation between generated static routes. JavaScript improves the transition but is not required for language switching or reading translated pages.

Without JavaScript, the authored content and ordinary navigation remain available in every language.

## Visual system

The current interface keeps the repository's existing retro-document / vintage-computing identity rather than adopting a generic portfolio template. Shared elements include:

- the 418 banner and avatar identity shell;
- tab-style primary navigation with current-section state;
- documentary rails and metadata treatment;
- CRT/holographic project monitor with scanline/phosphor/vignette treatment;
- responsive recomposition across desktop, tablet and mobile;
- ENG / CAST / CAT language control in the system rail;
- dark/light theme handling;
- print styles.

The design is implemented with plain CSS; there is no React/Vue/Svelte component runtime and no utility-CSS framework.

## CV artifact boundary

The CV generator does not belong to the site source tree.

The public PDF originates under `agents/cv/`, is compiled there, and is copied into:

```text
assets/files/cv/
```

only as a generated public artifact. The source TeX, preamble, header image and build tooling remain owned by `agents/cv/**`.

ACB reports, research, application material, tracker/status data and historical harness evidence are not site inputs.

## Local development

From the repository root:

```text
localdeploy.bat
```

The launcher checks Node `>=22.12`, installs site dependencies when needed and starts the Astro development server.

Equivalent direct commands:

```bash
npm install --prefix site --no-package-lock
npm run dev --prefix site
```

Production build:

```bash
npm run build --prefix site
```

## Verification

Two independent GitHub Actions contracts cover the site.

### `required-ci`

- validates the public CV artifact manifest;
- compiles the CV from its canonical `agents/cv/tex/` root;
- asserts the TeX source directory remains free of generated auxiliary files;
- publishes the generated CV into the portfolio artifact;
- builds Astro;
- validates generated portfolio output;
- validates repository and locale-aware Markdown links.

### `Site check`

- builds the canonical root form (`/`, indexable);
- builds the repository mirror (`/AgenticCareerBoost/`, non-indexable);
- derives EN/ES/CA project/post/CV routes from source content;
- enforces translation ID parity;
- validates `lang`, canonical, `hreflang`, `x-default`, OpenGraph, robots and sitemap behavior;
- checks internal references and image assets;
- runs Chromium navigation/theme/CRT/no-JS checks;
- switches ENG → CAST → CAT → ENG while preserving the semantic route;
- includes Spanish and Catalan pages in responsive checks so translated labels cannot silently break the shell;
- checks responsive behavior at 1920×1080, 1366×768, 768×1024 and 390×844;
- records exact-SHA build and visual-evidence artifacts.

## Publication

The GitHub Pages deployment workflow runs from `main` and publishes the repository project mirror. Deployment origin/base are supplied by `actions/configure-pages`; the source does not hardcode the Pages path.

The personal root site is a separate publication boundary and is intentionally not modified by this repository's project-mirror workflow.

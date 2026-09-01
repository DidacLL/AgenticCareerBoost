# AgenticCareerBoost

**Dídac Llorens — Software Engineer · Barcelona**  
Systems · AI workflows · data · backend · technical tooling

[Portfolio](https://didacll.github.io/) · [LinkedIn](https://www.linkedin.com/in/didacllorens/) · [GitHub profile](https://github.com/DidacLL)

[![required-ci](https://github.com/DidacLL/AgenticCareerBoost/actions/workflows/required-ci.yml/badge.svg)](https://github.com/DidacLL/AgenticCareerBoost/actions/workflows/required-ci.yml)
[![Site check](https://github.com/DidacLL/AgenticCareerBoost/actions/workflows/site-check.yml/badge.svg)](https://github.com/DidacLL/AgenticCareerBoost/actions/workflows/site-check.yml)

AgenticCareerBoost is the engineering workspace behind my public portfolio and career tooling. It combines a maintainable static site, a reproducible LaTeX CV pipeline, technical reports, local automation, and the decision/history record behind the work.

It is deliberately broader than a single demo application: the repository shows how I structure small systems around real constraints, keep public and private data boundaries explicit, automate repeatable work, and preserve enough history to make engineering decisions inspectable.

## Engineering profile

I work across software systems, AI-assisted workflows, data/backend foundations, technical tooling, and documentation. My current studies are focused on Computer Science / Software Engineering with a Machine Learning and Artificial Intelligence specialization at UOC.

Before moving into software engineering I spent fifteen years in banking and insurance operations, and I also have formal arts/design training from Escola Massana. That background affects how I approach technical work: domain rules, traceability, failure modes, operational responsibility, communication, and visual composition are not treated as afterthoughts.

## What this repository demonstrates

- **Static publishing architecture** — Markdown-authored content compiled by Astro into ordinary static HTML, with clean URLs, canonical metadata, robots/sitemap handling, and deployment-base portability.
- **Maintainable content ownership** — posts and projects are discovered from source files; a new blog article is one Markdown file, with the filename as the route slug and no manual route registry or `dist/` maintenance.
- **UI engineering without a heavy runtime** — responsive retro/document interface, persistent client navigation, theme handling, and CRT/gallery interaction using Astro plus small vanilla-JavaScript behaviors.
- **Document engineering** — a public CV authored in LaTeX, compiled from a single canonical TeX root, published through an explicit artifact manifest, and verified in CI.
- **Build and release discipline** — GitHub Actions checks canonical and project-base builds, metadata, routes, assets, responsive behavior, client navigation, no-JavaScript fallback, and Chromium smoke tests before publication.
- **Practical automation** — Python, PowerShell and shell tooling support artifact publication, local document generation, validation, and repeatable build tasks.
- **Boundary management** — portfolio source, CV source, report evidence, prototype tooling, and private application data have separate owners instead of being mixed into one public runtime.

## Stack

| Area | Current stack |
| --- | --- |
| Portfolio | Astro 7.2.9, `@astrojs/sitemap` 3.7.3, Astro components, TypeScript data/config, Markdown content collections |
| Presentation | Plain CSS, responsive layouts, small vanilla-JavaScript theme + CRT/gallery behavior, Astro client navigation |
| Output | Static HTML, directory-format routes, trailing slashes, base-aware assets and metadata |
| Delivery | GitHub Actions, GitHub Pages, Node 24.20 in CI (`>=22.12` locally), exact dependency versions |
| Browser verification | Chromium functional smoke, HTTP/image checks, responsive checks at 1920×1080, 1366×768, 768×1024 and 390×844 |
| CV pipeline | LaTeX / pdfLaTeX, `latexmk`, Python artifact manifest, generated PDF publication into the portfolio build |
| Local tooling | Python, PowerShell, Bash, repository-local scripts |

## Architecture at a glance

```text
site/src/content/**/*.md ─┐
site/src/data/site.ts ────┼─> Astro static build ─> site/dist/ ─> GitHub Pages
site/src/components/** ───┘

agents/cv/tex/*.tex
        │
        ├─> LaTeX / latexmk ─> agents/cv/build/*.pdf
        │                          │
        └──────────────────────────┴─> artifact manifest ─> site/assets/files/cv/

GitHub Actions
  ├─ required-ci: CV compile + artifact publication + Astro build + Markdown links
  ├─ Site check: root/mirror builds + metadata/routes/assets + Chromium behavior
  └─ LaTeX reports: independent report evidence build
```

The portfolio is only one output of this repository. Historical reports and project evidence remain under `agents/**`; they are not copied into `site/` unless they are intentionally part of the public website.

## Repository map

- [`site/`](site/) — source for the public Astro portfolio. See [`site/README.md`](site/README.md) for architecture, authoring and verification details.
- [`agents/cv/`](agents/cv/) — public/general CV source and reproducible build support. See [`agents/cv/README.md`](agents/cv/README.md).
- [`agents/reports/`](agents/reports/) — technical report sources and historical repository evidence, independent from the portfolio build.
- [`application-tracker/`](application-tracker/) — preserved prototype/local workflow evidence, including the simple cover-letter renderer that later informed AAAAT.
- [`agents/state/`](agents/state/) — historical decisions, research and previous run records.
- [`agents/work/social/`](agents/work/social/) — campaign/research material retained as project history.
- [`agents/rules/`](agents/rules/) and [`agents/tests/`](agents/tests/) — legacy harness material preserved as evidence, not the current control system.

## Maintaining the portfolio

The authoring model is intentionally small:

```text
new blog article
    ↓
create site/src/content/posts/my-article.md
    ↓
write frontmatter + Markdown
    ↓
commit
```

The filename becomes `/blog/my-article/`. Astro discovers it for the Blog index and static route automatically. Projects use the same filename-as-slug model. Generated `site/dist/` output is never maintained by hand.

For local viewing, run:

```text
localdeploy.bat
```

The launcher checks the local Node version, installs the pinned site dependencies when needed, and starts Astro's development server.

## CV workflow

The canonical CV compilation root is [`agents/cv/tex/`](agents/cv/tex/). The main `.tex`, shared preamble and header asset are siblings, so the document can be compiled directly from that directory in a LaTeX IDE.

Repository build helpers use the same root and redirect PDFs plus auxiliary files to `agents/cv/build/`, keeping the source directory clean. The generated public PDF is then copied into the portfolio artifact through [`agents/cv/artifacts.json`](agents/cv/artifacts.json).

## Verification and publication

The public site is built in two configurations during verification:

1. canonical root (`/`) with indexable metadata;
2. project-base mirror (`/AgenticCareerBoost/`) with non-indexable metadata.

The checks validate generated routes, canonical/OpenGraph metadata, robots/sitemap behavior, internal assets, image decoding, client-side navigation persistence, theme/CRT behavior, responsive overflow, retired-route behavior and no-JavaScript content fallback.

The repository's GitHub Pages workflow deploys the project-base mirror from `main`. The personal root site remains a separate publication boundary.

## Private boundary

This repository is also used as a local working area. Private application data must remain local and is intentionally excluded from the public project.

Do not commit live application data, tailored application documents, recruiter messages, private notes, databases, generated private letters/CVs, or material under `application-tracker/.private/`.

Public/general CV source, portfolio assets and deliberately published project evidence are the exception: they are part of the public engineering record.

## Project boundary

Application Tracker is preserved here as prototype evidence and a small local workflow, not as the current product direction. New job-search product work lives in its own repositories.

The purpose of AgenticCareerBoost is to keep the public engineering story inspectable: working code, build systems, technical documents, automation, decisions, corrections, and clear boundaries rather than a polished landing page with no source behind it.

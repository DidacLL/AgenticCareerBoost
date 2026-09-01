# AgenticCareerBoost — Site Refactor Recovery Contract

**Repository:** `DidacLL/AgenticCareerBoost`  
**Execution branch:** `DidacLl/siterefactor`  
**Frozen production baseline:** `main@aa7d57c809db41bbbf042eebbfdeba4454476295`  
**Recovery baseline:** `336573134c0aed5ce3ed5d46c1e74a615aa7769b`  
**Production cutover:** not authorized

This document replaces the earlier refactor plan. It incorporates the user's corrections and the legitimate design/boundary criticisms from the Codex conversation. Older phase claims are historical only.

## 1. Objective

Finish the Astro refactor as a clean, professional portfolio without turning the repository into a site-content dump or the design into a generic template.

The final branch must contain a static, maintainable portfolio whose source is understandable, whose content has clear owners, whose visual language is recognizably Dídac's retro-vintage videogame/document style, and whose objective behavior is verified by the agent before one final human visual review.

## 2. Repository boundaries

- `site/` contains only source/assets/artifacts that are actually part of the portfolio.
- `agents/reports/**`, research, logs and historical records are ACB repository evidence/documentation. They are not portfolio content and are not copied into `site/`.
- `agents/rules/**`, `agents/tests/**`, `agents/work/**` and `agents/state/**` are historical/work evidence, not a live harness unless explicitly reactivated by the user.
- `application-tracker/` remains local scratch/prototype evidence. The site does not expose, build or describe a live tracker demo.
- The public/general CV is the only generated document artifact intentionally served by the portfolio, with its destination owned by `agents/cv/artifacts.json`.
- AAAAT, P3CTeX and IronBank remain project entries linked to their repositories. No cross-repository loader/federation is introduced.

## 3. Architecture

Keep:

- Astro 7.2.9 static output;
- Markdown narrative with small typed frontmatter;
- Astro layouts/components;
- plain CSS;
- vanilla JS only for theme and monitor/gallery interaction;
- existing binary imagery under `site/assets/img/**`;
- one shared base-aware path helper;
- `localdeploy.bat` as the single simple local viewing entrypoint.

Do not add React, Vue, Svelte, SSR, CMS, MDX, Tailwind, a SPA router, client content loader, generic block DSL, staging host, second repository or unnecessary QA framework.

The source is deployment-agnostic. No own production origin or deployment prefix may be hardcoded in site content, components, CSS or client JS. Deployment metadata is build configuration only.

## 4. Content ownership

Use one semantic owner rather than scattered hardcoding.

- Page-specific narrative and presentation copy belongs to that page's Markdown/frontmatter.
- Project/post/CV/focus data belongs to its collection entry.
- Global identity, navigation, legal text and UI-control labels belong to `site/src/data/site.ts`.
- Components/layouts render content; they do not invent authored portfolio copy.
- Stable technical constants may stay in the module that owns them. Do not convert every literal into configuration.
- Project monitor slides are projections of the canonical project collection, never duplicated project records.

Content migration is not permission for a generic rewrite. Preserve the useful current/main narrative and factual nuance; change only content that became false because dashboard/tracker/report publication or the old JSON runtime is gone.

Historical blog posts remain historical. Do not rewrite their past architecture as present-day fact.

## 5. Public routes

The portfolio owns only these routes:

- `/`
- `/projects/`
- `/projects/agentic-career-boost/`
- `/projects/p3ctex/`
- `/projects/aaaat/`
- `/projects/ironbank/`
- `/blog/`
- the three current blog-entry routes
- `/cv/ml/`, `/cv/agentic/`, `/cv/backend/`, `/cv/print/`
- `/focus/`, `/focus/ml/`, `/focus/agentic/`, `/focus/backend/`
- `/contact/`
- static `404`

There is no compatibility layer for `/dashboard/`, `/application-tracker/`, `/curriculum/`, `/notes/` or `/hire/**`. Unknown/retired URLs receive the normal static 404.

## 6. Visual contract

The previous public site is visual evidence, not implementation source. Preserve its authored identity while fixing its defects.

Required direction:

- retro-vintage videogame / holographic technical personality;
- warm paper/grid light world and coherent dark world;
- ink-like framing, teal/terracotta/green signal palette and monospaced system language;
- wide, fluid desktop composition with readable rails and a strong document centre;
- asymmetric technical/editorial density rather than generic cards;
- 418 identity artwork retained;
- project imagery treated as actual project imagery, not blanket sepia/grayscale thumbnails;
- monitor/gallery as a deliberate CRT/holographic signature interaction;
- responsive recomposition rather than squeezing rigid desktop columns.

Monitor requirements:

- first slide is the manual portrait and links to CV + Contact;
- remaining slides derive from project entries in project order;
- project slides use project image/title/summary/tags/status and route without duplicating those values;
- monitor screen owns clipped image, restrained scanline/vignette/beam treatment and factual overlay metadata;
- expanded state is a fixed viewport dialog, not in-flow expansion;
- no procedural noise, perpetual expensive animation or blanket image colour destruction;
- motion is short transform/opacity behavior and respects reduced motion.

Do not replace this with generic SaaS/editorial/luxury/template styling, glassmorphism, giant marketing heroes, stock/generative artwork or arbitrary rounded-card design.

## 7. Recovery sequence

### R1 — Boundary and authority cleanup

- replace stale plan/tracker with this recovery contract;
- restore root repository guidance that was over-trimmed, with only the factual Astro boundary added;
- clearly mark `agents/**` evidence as repository evidence, not harness/site content;
- remove ACB report catalog/component/site links and report publication coupling;
- make report local builds output only to `agents/reports/tex/build/`;
- retain the dedicated report build workflow as repository-evidence CI;
- remove retired-route redirects and verifier expectations;
- make branch verification run for every branch HEAD.

### R2 — Content ownership and visual reconstruction

- repair collection schemas only where actual structured data requires it;
- move authored index/home/UI copy to the correct owners;
- restore CV technical facts and PDF/source access without duplicating filenames;
- restore useful focus/project relationships and ACB project history without a report-download library;
- restore legal disclosure and complete metadata;
- rebuild the shell/rails/monitor/media/responsive CSS directly, removing patch layers and unused components;
- derive monitor project slides from project collection data.

### R3 — Publication and verification hardening

- fix CV artifact path validation;
- make canonical root build indexable and mirror build non-indexable;
- make robots, sitemap and metadata follow that build mode;
- strengthen generated-site verification for routes, metadata, assets and base paths;
- strengthen browser smoke for HTTP failures, decoded images, navigation, theme, monitor and overflow at desktop/tablet/mobile;
- keep tests factual; never claim aesthetic approval from automation;
- align `site-build.yml`/`required-ci.yml` with the final portfolio-only pipeline.

### R4 — Final alignment

- remove only dead refactor/site source and stale documentation references;
- inspect the complete recovery diff and then the complete branch-vs-main diff for scope leakage;
- require a green Site Check for the exact final branch SHA;
- update tracker with real evidence;
- ask the user for one final subjective review via `localdeploy.bat`.

## 8. Verification responsibility

The agent owns objective verification. The user is not the functional QA operator.

GitHub Actions may verify factual behavior only: build success, route existence, internal links/assets, metadata, base-path portability, indexability, HTTP failures, decoded images, navigation, theme persistence, monitor controls and document-level overflow.

A green workflow never means "looks good". Visual composition, taste, hierarchy and feel remain subjective. The user performs one final local visual review only after agent-owned correction is exhausted.

## 9. Forbidden actions

Without a new explicit user instruction:

- no writes to `main`;
- no PR or merge;
- no Pages deployment;
- no write to `DidacLL/didacll.github.io`;
- no temporary branch/repository/staging service;
- no force-push/history rewrite;
- no Application Tracker development;
- no broad historical-document cleanup;
- no private application data access;
- no external-project federation/import mechanism.

## 10. Completion

This run ends with a green, reviewed development branch and one final user visual verdict. Production integration remains a separate operation.
# AgenticCareerBoost — Site Refactor Recovery Record

**Status:** CLOSED RECOVERY RECORD — not an active agent harness  
**Repository:** `DidacLL/AgenticCareerBoost`  
**Execution branch:** `DidacLl/siterefactor`  
**Frozen production baseline:** `main@aa7d57c809db41bbbf042eebbfdeba4454476295`  
**Recovery baseline:** `336573134c0aed5ce3ed5d46c1e74a615aa7769b`  
**Accepted implementation SHA:** `872e6c5ed2583da8b5f87eda84f508de083969f7`  
**Production cutover:** not authorized

This file records the completed recovery of the public-site refactor. It supersedes the earlier planning variants and must not be interpreted as a standing sprint/harness for future work. Current repository authority is the root `AGENTS.md` plus direct user instructions.

## Final architecture

- ACB remains the canonical repository/source for the portfolio and the engineering record around it.
- `site/` is a static Astro 7.2.9 portfolio: Markdown/frontmatter, Astro layouts/components, plain CSS, and vanilla JS only for theme and the CRT monitor/gallery.
- No React, Vue, Svelte, SSR, CMS, MDX, Tailwind, SPA router, custom content DSL, staging service, second repository, or cross-repository content loader is part of the implementation.
- Site source is deployment-agnostic. Own production origins and deployment prefixes are not hardcoded in authored site source.
- `site/` contains only portfolio source, build support and assets actually consumed by the portfolio. Historical ACB evidence remains under `agents/**` and is not copied into the site.
- The public/general CV is the only generated document intentionally served by the portfolio.
- Application Tracker remains local scratch/prototype evidence and is not a public site surface.
- ACB reports remain repository evidence under `agents/reports/**`; report builds do not publish PDFs into `site/`.

## Content ownership

- Page narrative/presentation copy lives in the page Markdown/frontmatter.
- Project, post and CV data lives in its collection entry.
- Global identity, navigation, legal/UI labels and shared public channel data live in `site/src/data/site.ts`.
- Components/layouts render those owners instead of inventing duplicate authored copy.
- Project monitor slides derive from the canonical project collection.
- Historical blog posts remain historical and retain explicit context where old architecture is mentioned.

## Final public routes

- `/`
- `/projects/`
- `/projects/agentic-career-boost/`
- `/projects/p3ctex/`
- `/projects/aaaat/`
- `/projects/ironbank/`
- `/blog/`
- `/blog/agents-need-receipts/`
- `/blog/static-sites-as-workbenches/`
- `/blog/sprint-review-agenticcareerboost/`
- `/cv/ml/`
- `/cv/agentic/`
- `/cv/backend/`
- `/cv/print/`
- `/contact/`
- static `404`

`/focus/**` was removed during recovery because it duplicated the role-specific CV views with a second, inconsistent filtering concept. `/dashboard/`, `/application-tracker/`, `/curriculum/`, `/notes/`, `/hire/**` and `/focus/**` are retired and receive the normal static 404.

## Final visual contract

The implementation keeps the mature document/grid shell developed during the refactor while restoring the stronger identity of the original site:

- the 418 artwork is a real horizontal header banner;
- the identity rail uses the actual portrait/avatar rather than an invented text mark;
- headings use restrained document scale rather than oversized marketing-landing typography;
- the home CRT is compact in normal state and remains a signature interaction rather than dominating the page;
- CRT presentation restores curved-screen masking, phosphor tint, scanlines, vignette and monitor framing without reusing the old fragile runtime;
- expanded CRT is a bounded fixed dialog at desktop scale, not fullscreen and not in-flow expansion;
- project imagery is shown as project imagery rather than blanket destructive filters;
- Blog, CV and Contact use relevant imagery so pages do not collapse into monotonous text/card grids;
- responsive layouts recompose at 1920×1080 (primary desktop), 1366×768, 768×1024 and 390×844.

## Verification contract

The branch Site Check owns objective verification. It builds and verifies both:

- canonical root: base `/`, indexable;
- project-base mirror: base `/AgenticCareerBoost/`, non-indexable.

It checks generated routes, metadata, canonical URLs, robots/sitemap policy, assets, HTTP responses, decoded images, ordinary navigation, theme persistence, CRT previous/next/expand/Escape behavior, no-JS authored content and horizontal overflow at the four target viewports. It also uploads the exact-SHA build and visual-evidence screenshots as ordinary Actions artifacts without deploying Pages.

Automation does not certify taste. Visual evidence from the exact SHA was reviewed during recovery, including the 1920×1080 expanded CRT state, and user feedback on banner, avatar, title scale, CRT character, monitor sizing, duplicate Focus views and sparse content was incorporated.

## Recovery outcome

The recovery removed the report→portfolio coupling, fixed CV artifact validation, corrected canonical/indexability behavior, strengthened branch verification, restored content/visual parity where the initial Astro migration had over-simplified it, removed the duplicate Focus surface, and pruned unused legacy/generated assets from `site/`.

Implementation acceptance evidence: `872e6c5ed2583da8b5f87eda84f508de083969f7`, Site Check run `33514536384` — SUCCESS.

Production integration remains a separate operation and requires explicit user authorization.
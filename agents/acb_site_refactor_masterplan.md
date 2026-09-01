# AgenticCareerBoost — Site Refactor Recovery Record

**Status:** CLOSED RECOVERY RECORD — not an active agent harness  
**Repository:** `DidacLL/AgenticCareerBoost`  
**Execution branch:** `DidacLl/siterefactor`  
**Frozen production baseline:** `main@aa7d57c809db41bbbf042eebbfdeba4454476295`  
**Recovery baseline:** `336573134c0aed5ce3ed5d46c1e74a615aa7769b`  
**Recovery acceptance milestone:** `872e6c5ed2583da8b5f87eda84f508de083969f7`  
**Post-recovery hardening:** tracked in PR #73 and branch history  
**Production cutover:** not authorized

This file records the completed recovery of the public-site refactor. It supersedes the earlier planning variants and must not be interpreted as a standing sprint/harness for future work. Current repository authority is the root `AGENTS.md` plus direct user instructions. The milestone SHA above records the end of the recovery batches; it is not intended to identify the current PR head after later pre-merge hardening.

## Final architecture

- ACB remains the canonical repository/source for the portfolio and the engineering record around it.
- `site/` is a static Astro 7.2.9 portfolio: Markdown/frontmatter, Astro layouts/components, plain CSS, and vanilla JS only for theme and the CRT monitor/gallery.
- No React, Vue, Svelte, SSR, CMS, MDX, Tailwind, custom content DSL, staging service, second repository, or cross-repository content loader is part of the implementation.
- Astro client navigation is used only to preserve the common shell and remove full-document reload glitches; the generated output remains ordinary static HTML with no-JS fallback.
- Site source is deployment-agnostic. Own production origins and deployment prefixes are not hardcoded in authored site source.
- `site/` contains only portfolio source, build support and assets actually consumed by the portfolio. Historical ACB evidence remains under `agents/**` and is not copied into the site.
- The public/general CV is the only generated document intentionally served by the portfolio. CV source dependencies remain owned by `agents/cv/**`.
- Application Tracker remains local scratch/prototype evidence and is not a public site surface.
- ACB reports remain repository evidence under `agents/reports/**`; report builds do not publish PDFs into `site/`.

## Content ownership

- Page narrative/presentation copy lives in the page Markdown/frontmatter.
- Project, post and CV data lives in its collection entry.
- Global identity, navigation, legal/UI labels and shared public channel data live in `site/src/data/site.ts`.
- Components/layouts render those owners instead of inventing duplicate authored copy.
- Project monitor slides derive from the canonical project collection.
- Historical blog posts remain historical and retain explicit context where old architecture is mentioned.
- Route slugs for posts, projects and CV views are derived from their Markdown filenames; publishing content does not require a second route registry.

## Public route model

Top-level routes are `/`, `/projects/`, `/blog/`, `/cv/*` and `/contact/`, plus static `404`. Project, post and CV detail routes are generated from the files in their corresponding Markdown collections.

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

Pull requests that touch the site or public CV receive a non-deploy Site Check. It builds and verifies both:

- canonical root: base `/`, indexable;
- project-base mirror: base `/AgenticCareerBoost/`, non-indexable.

Generated route checks derive project/post/CV routes from the same Markdown filenames that drive publication. The browser smoke checks HTTP responses, decoded images, client navigation without document reload, persistent shell nodes, theme persistence, CRT controls, no-JS authored content and horizontal overflow at the four target viewports. It also uploads exact-SHA build and visual-evidence artifacts without deploying Pages.

`required-ci` separately compiles the actual public CV, publishes its generated PDF into the site artifact, builds the canonical portfolio and validates internal Markdown links. Missing CV-owned dependencies therefore fail CI rather than silently producing a degraded document.

Automation does not certify taste. Visual evidence from exact SHAs was reviewed during recovery, and user feedback on banner, avatar, title scale, CRT character, monitor sizing, duplicate Focus views and sparse content was incorporated.

## Recovery outcome

The recovery removed report→portfolio coupling, fixed CV artifact validation, corrected canonical/indexability behavior, restored content/visual parity where the initial Astro migration had over-simplified it, removed the duplicate Focus surface, and pruned unused legacy/generated assets from `site/`. Later PR hardening improved authoring UX, persistent client navigation, shell behavior, CV source ownership and verification maintainability without changing that architecture.

Recovery acceptance evidence: `872e6c5ed2583da8b5f87eda84f508de083969f7`, Site Check run `33514536384` — SUCCESS. Current integration status belongs to PR #73 and the repository branch rather than this historical record.

Production integration remains a separate operation and requires explicit user authorization.

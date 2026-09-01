# AgenticCareerBoost — Public Site Refactor
## Frozen execution masterplan

**Status:** FINAL / executable contract after read-only repository audit  
**Repository:** `DidacLL/AgenticCareerBoost`  
**Remote baseline:** `main` at `aa7d57c809db41bbbf042eebbfdeba4454476295`  
**Execution branch:** `DidacLl/siterefactor`  
**Execution environment:** ChatGPT Classic + connected GitHub connector; user performs subjective visual review locally  
**Production cutover:** explicitly OUTSIDE this execution plan

> This document supersedes and invalidates every earlier site-refactor masterplan/tracker produced in this conversation. None of those drafts may be used as execution authority.

---

## 0. Re-baselined authority — portfolio boundary and reconstruction

This section supersedes every conflicting instruction later in this document. The Astro/Markdown/static foundation remains; the report-publication, compatibility, and visual decisions below are replaced.

### 0.1 Public boundary

- The portfolio is one public artifact in AgenticCareerBoost. It is not the public container for ACB reports, implementation logs, sprint history, tracker material, cover letters, or generated application material.
- ACB reports and proofs remain repository documentation. Do not catalog them in the site, copy them to site assets, render them through a portfolio component, or make Astro depend on their PDFs.
- The site contains only current portfolio pages, concise project narratives, direct source links, and explicitly selected public CV views. The public CV remains the sole generated site artifact, with its single target owned by agents/cv/artifacts.json.
- Existing local generated outputs under site/files are transitional legacy artifacts, not site content. Do not read, stage, or delete them during this refactor. Before closeout, classify them by artifact type and migrate only the report-document outputs to an ACB documentation build/archive location outside site; retain only the explicitly selected public CV at the final site asset path. The final site tree has no site/files report, proof, tracker, or documentation directory.
- Preserve ACB research, report sources, current documentation, and unique historical proof under agents/. The portfolio does not need to duplicate them for them to remain part of the ACB project.
- Before any documentation deletion, create a repository-only inventory that classifies each candidate as current proof, historical context, exact duplicate, or discarded proposal. Keep current proof and useful history; archive or remove only demonstrably redundant/abandoned material after that classification. Never use site cleanup as authority to delete ACB documentation. Site/files is not an ACB documentation location.

### 0.2 Replacement, not compatibility

- The site has no legacy dashboard, Application Tracker, curriculum, notes, or hire routes. Do not redirect any of them to a current page.
- Remove their redirect configuration and verifier expectations. Unknown paths use the normal static 404 response; no compatibility route is created.
- Remove ArtifactList.astro, site/src/data/reports.json, portfolio report links, and report-publication coupling from site workflows. Retain report sources, tools, documentation, and history.

### 0.3 Visual reconstruction

The pre-refactor site is visual evidence, not implementation source. Do not restore its router, JSON renderer, stylesheet, or client architecture.

Rebuild the authored retro-vintage document/game direction in clean, readable Astro/CSS/vanilla-JS:

- use a fluid wide desktop composition with readable rails; the outer grid must not disturb rail or body text;
- retain the warm/dark document world, ink borders, 418 identity, teal/terracotta/green signal palette, monospaced system labels, asymmetric density, and editorial hierarchy;
- make the gallery a real monitor: curated slides, factual screen-overlay metadata, a shared clipped image/scanline/vignette/scan-beam compositor, and a fixed viewport dialog when expanded;
- eliminate generic caption labels, blanket sepia/grayscale filters, detached scanlines, procedural noise, expensive animation, oversized image cards, and in-flow expansion;
- use only short transform/opacity motion, honor reduced motion, and recompose at breakpoints rather than preserve rigid columns;
- refine content composition and project media as part of the visual work; do not add generic portfolio cards or flatten the site into a template.

### 0.4 Execution order

A. Correct public boundaries and control documents: remove site-facing report/redirect coupling and correct misleading portfolio copy while preserving ACB documentation and local generated outputs.

B. Reconstruct visual and interaction quality: audit local rendering against the supplied screenshots and existing visual direction, then rebuild shell, rails, monitor/gallery, media treatment, and responsive behavior with clean source.

C. Align and close: remove only obsolete runtime/workflow coupling after the replacement owns the surface; verify current routes, base paths, navigation, theme, gallery, assets, console, requests, and overflow at the exact branch SHA; then perform one final agent critique before asking for final subjective local inspection.

The agent does not stop at intermediate visual gates. The user is not the functional tester and performs one final subjective visual review only after agent-owned correction is exhausted.

---
## 1. Purpose

Refactor the current browser-rendered portfolio into a simple static site whose content is authored as Markdown and whose presentation is rendered at build time with Astro.

The refactor must improve maintainability without turning the site into a generic portfolio template, without reactivating the old agentic harness, without expanding the Application Tracker scratch project, and without changing either public site during development.

The final branch must be ready for a later, separately authorized production cutover. This plan itself does **not** open a PR, merge to `main`, alter `DidacLL/didacll.github.io`, or deploy GitHub Pages.

---

## 2. Authority and evidence hierarchy

For this refactor, authority is resolved in this order:

1. The user's current explicit instructions.
2. Root `AGENTS.md`.
3. Current root `README.md` and `agents/state/current.md` where they describe present project boundaries.
4. Current source code and workflows as evidence of what exists today, not proof that it should survive.
5. Historical `agents/state/logs/**`, `agents/rules/**`, `agents/tests/**`, old sprint material and old site documentation only as historical/reference evidence.

A file existing today is **not** sufficient reason to migrate it.

Specific consequences already resolved:

- `application-tracker/` remains local scratch/evidence. Its public route and build integration are removed; its local implementation is not refactored.
- The old public dashboard/status pipeline is retired. `current.md` says there is no active sprint/process framework, while `export_status.py` still parses the superseded `**Active workflow**` / `**Active sprint**` schema.
- `site/README.md` describes the old implementation and does not veto this approved refactor.

---

## 3. Literal mutation contract

### 3.1 Planning/audit mode

Any request whose operative verb is analysis/review/audit/check/plan is read-only. No GitHub mutation is permitted.

### 3.2 Execution authorization

Repository mutation begins only after the user explicitly instructs ChatGPT to execute this masterplan.

That instruction authorizes only the writes listed in this document, only in `DidacLL/AgenticCareerBoost`, and only on `DidacLl/siterefactor` until a separate cutover authorization is given.

### 3.3 Precondition before the first write

At execution handoff, perform these read-only checks:

- `main` must still resolve to `aa7d57c809db41bbbf042eebbfdeba4454476295`.
- `DidacLl/siterefactor` must exist, descend directly from the expected baseline, and contain only the committed control documents before execution mutations.
- `main` must remain the default production source.

If any condition is false: **STOP. Do not adapt the plan silently.** Report the changed fact to the user.

### 3.4 Forbidden mutations during this plan

- no write to `main`;
- no PR creation;
- no PR merge;
- no write to `DidacLL/didacll.github.io`;
- no GitHub Pages deployment;
- no `pages: write` or `id-token: write` in branch validation;
- no repository settings/ruleset change;
- no issue creation;
- no temporary test branch;
- no temporary preview repository;
- no Vercel/Cloudflare/Netlify/staging service;
- no self-mutating CI workflow;
- no force-push/history rewrite;
- no touching private application data.

---

## 4. Verified execution capabilities and hard limits

The plan uses only the following connector capabilities that are present in this ChatGPT session and compatible with current repository permissions.

| Capability | Status | Use in this plan |
|---|---|---|
| Read repository/files/branches/commits/trees | PASS | audit and review |
| Compare refs/commits | PASS | baseline and change inspection |
| Repository permission query | PASS (`admin`) | confirms connected account access |
| Existing execution branch | PASS | use `DidacLl/siterefactor`; do not create another branch |
| Create/update/delete UTF-8 text files on a branch | PASS | implementation |
| Write workflow YAML as a text file | PASS | one non-deploy build workflow |
| Push on a non-main branch triggers branch workflow | PASS | objective compile check |
| Read workflow runs/jobs/steps/logs | PASS | inspect build result |
| Render repository PNG/JPG to GPT as an image | FAIL | never used for visual approval |
| GPT local shell/browser against user's checkout | FAIL | never claimed or used |
| Locate push-triggered workflow runs by branch/SHA and read jobs/logs | PASS | autonomous branch verification after each coherent change batch |
| Direct branch deletion action | NOT AVAILABLE | branch is retained as development history |
| Multi-file atomic Git-tree write path | EXPOSED BUT NOT CERTIFIED | not used by this literal plan |
| PR/merge | available but FORBIDDEN here | production integration is outside plan |

Because the certified text-write actions commit per file operation, this refactor accepts granular branch history rather than introducing an unverified batching mechanism or a self-writing workflow. Commit messages must use a phase prefix so the history remains readable. No squash/rewrite is performed by this plan.

---

## 5. Architecture decision

### 5.1 Chosen stack

- Astro `7.2.9`, exact direct dependency.
- `@astrojs/sitemap` `3.7.3`, exact direct dependency.
- Node 24.20.0 in GitHub Actions.
- Playwright library `1.62.1` installed **only inside branch CI with `--no-save`** for the small functional browser contract; it is not a site dependency and is not required by `localdeploy.bat`.
- Local development accepts Node `>=22.12.0`; Node 24 LTS is the recommended install.
- Astro `output: 'static'`.
- Astro `build.format: 'directory'`.
- `trailingSlash: 'always'`.
- Markdown + small typed frontmatter schemas.
- Astro components/layouts only.
- Plain CSS.
- Vanilla JavaScript only for theme persistence and the existing gallery interaction.

### 5.2 Explicitly excluded

- React, Vue, Svelte or another client UI framework;
- SSR/server adapters;
- backend/API/database;
- CMS/admin UI;
- MDX;
- Tailwind or another CSS framework;
- SPA router;
- browser-side JSON content loader;
- generic block DSL;
- Playwright as visual approval or aesthetic scoring;
- generated screenshots as a substitute for human UI review.

### 5.3 Why Astro is justified

The current site has 21 registered routes, multiple content families, four projects, three articles, four CV views, four focus routes, metadata, reusable shell structures and legacy redirects. Today these are implemented through JSON + a custom block vocabulary + data store + router + renderer + DOM component factory.

A bespoke "tiny builder" would have to recreate routing, Markdown parsing, content schemas, layouts, metadata, static generation, redirects and base-aware output. That would reproduce the accidental framework that this refactor is meant to remove.

Astro is therefore used to **delete custom infrastructure**, not to introduce an application framework.

---

## 6. Core engineering rule: single ownership, not scattered hardcoding

The site is host-agnostic and data has one owner.

### 6.1 Forbidden

- production origins such as `didacll.github.io` inside site content/components/CSS/client JS;
- deployment prefixes such as `/AgenticCareerBoost/` inside site content/components/CSS/client JS;
- an entry storing its own route when the route can be derived from its collection ID;
- project/post/profile titles duplicated inside rendering components;
- primary navigation labels duplicated across layouts;
- public-facing prose embedded in renderer logic;
- CSS values copied repeatedly when they are design tokens;
- a second route helper or second publication manifest.

### 6.2 Allowed and expected

- external GitHub/LinkedIn/project URLs are absolute because they point to genuinely external resources;
- stable technical constants live in the module that owns them;
- visual constants live in CSS design tokens;
- global identity/navigation/UI labels live in one `site.ts` data module;
- route construction lives in one `paths.ts` module;
- per-project/per-post/per-CV narrative lives in Markdown;
- per-entry structured facts live in minimal frontmatter;
- deployment origin/base are injected by the workflow at build time.

The rule is **one semantic owner**, not "turn every literal into configuration".

---

## 7. Deployment independence

The site source does not know where it will be hosted.

The workflow supplies:

- `SITE_ORIGIN` from `actions/configure-pages` output `origin`;
- `SITE_BASE` from `actions/configure-pages` output `base_path`;
- `SITE_INDEXABLE=true` only for the canonical root publication;
- `SITE_INDEXABLE=false` for the AgenticCareerBoost project mirror.

`astro.config.mjs` reads those values. Local development defaults to base `/` and non-indexable metadata mode without requiring environment setup.

Internal links and public asset links are created through one base-aware helper using `import.meta.env.BASE_URL`. Components never write host-specific or deployment-prefix-specific URLs.

Canonical URLs, OpenGraph absolute URLs and sitemap entries are the only own-site absolute URLs, and are generated at build time from deployment metadata because those formats semantically require an origin.

The project mirror is emitted with `noindex,nofollow` and without sitemap generation. The canonical root publication is indexable.

---

## 8. Binary asset decision forced by real connector capabilities

Existing PNG/JPG/logo files under `site/assets/img/**` are **not moved, renamed, regenerated or duplicated** in this refactor.

Reason: the certified connector write path is UTF-8 text. A plan that promises a binary asset migration would not be literal with the available tooling.

Astro is configured with:

```text
publicDir: './assets'
```

After the old text runtime is removed, `site/assets/` contains the existing `img/` tree plus generated public `files/` and `.nojekyll`. Astro copies them into the build artifact.

Public image URLs therefore become base-aware `/img/...` paths generated through the shared path helper. Existing binary content remains byte-for-byte untouched.

No image-CDN, binary optimizer or extra dependency is introduced. Images below the fold use native lazy loading; the identity/hero image may load eagerly. Binary optimization can be a separate future task only if explicitly requested.

---

## 9. Target source tree

```text
AgenticCareerBoost/
├─ agents/
│  ├─ acb_site_refactor_masterplan.md
│  └─ acb_site_refactor_tracker.md
├─ localdeploy.bat
├─ site/
│  ├─ .npmrc
│  ├─ package.json
│  ├─ astro.config.mjs
│  ├─ tsconfig.json
│  ├─ README.md
│  ├─ assets/                    # Astro publicDir
│  │  ├─ .nojekyll
│  │  ├─ img/                   # existing binary files, untouched
│  │  └─ files/                 # generated in CI, ignored
│  │     ├─ cv/
│  │     └─ reports/
│  └─ src/
│     ├─ content.config.ts
│     ├─ content/
│     │  ├─ pages/
│     │  │  ├─ home.md
│     │  │  └─ contact.md
│     │  ├─ projects/
│     │  │  ├─ agentic-career-boost.md
│     │  │  ├─ p3ctex.md
│     │  │  ├─ aaaat.md
│     │  │  └─ ironbank.md
│     │  ├─ posts/
│     │  │  ├─ agents-need-receipts.md
│     │  │  ├─ static-sites-as-workbenches.md
│     │  │  └─ sprint-review-agenticcareerboost.md
│     │  ├─ cv/
│     │  │  ├─ ml.md
│     │  │  ├─ agentic.md
│     │  │  ├─ backend.md
│     │  │  └─ print.md
│     │  └─ focus/
│     │     ├─ ml.md
│     │     ├─ agentic.md
│     │     └─ backend.md
│     ├─ data/
│     │  ├─ site.ts
│     │  └─ reports.json
│     ├─ lib/
│     │  └─ paths.ts
│     ├─ layouts/
│     │  ├─ BaseLayout.astro
│     │  ├─ DocumentLayout.astro
│     │  ├─ ProjectLayout.astro
│     │  ├─ PostLayout.astro
│     │  └─ CvLayout.astro
│     ├─ components/
│     │  ├─ ThemeToggle.astro
│     │  ├─ Gallery.astro
│     │  ├─ ProjectCard.astro
│     │  ├─ ArtifactList.astro
│     │  └─ Footer.astro
│     ├─ pages/
│     │  ├─ index.astro
│     │  ├─ projects/index.astro
│     │  ├─ projects/[id].astro
│     │  ├─ blog/index.astro
│     │  ├─ blog/[id].astro
│     │  ├─ cv/[id].astro
│     │  ├─ focus/index.astro
│     │  ├─ focus/[id].astro
│     │  ├─ contact.astro
│     │  ├─ 404.astro
│     │  └─ robots.txt.ts
│     ├─ scripts/
│     │  ├─ theme.js
│     │  └─ gallery.js
│     └─ styles/
│        ├─ tokens.css
│        ├─ base.css
│        ├─ site.css
│        └─ print.css
└─ .github/workflows/
   ├─ site-check.yml             # branch-only autonomous build/functional verification
   ├─ site-build.yml             # production, main-only; updated but dormant on branch
   └─ required-ci.yml            # updated but not used as a visual gate
```

No parallel `site-next/` tree is created. The Git branch is the isolation boundary; duplicating the site source would create unnecessary migration state.

---

## 10. Content model

### 10.1 Collections

`src/content.config.ts` defines exactly five build-time Markdown collections using Astro's `glob()` loader and Zod schemas:

- `pages`
- `projects`
- `posts`
- `cv`
- `focus`

### 10.2 Common schema

Every entry owns only content metadata it actually needs:

```text
title: string
description: string
label?: string
```

### 10.3 Project schema

```text
title
description
summary
order
tags[]
image            # base-independent public image identifier
imageAlt
repository?      # genuinely external URL
status?          # factual project status, not sprint status
```

There is **no `route` field**. `/projects/<id>/` is derived from the collection ID.

### 10.4 Post schema

```text
title
description
date
tags[]
```

There is no route field. `/blog/<id>/` is derived from the collection ID.

### 10.5 CV schema

```text
title
description
label
order
lanes[]
technicalBase[]
```

Profile/narrative text stays in Markdown. The selected-project section is derived from the project collection rather than duplicated inside each CV view.

### 10.6 Focus schema

```text
title
description
label
order
relatedProjectIds[]
relatedCvId
```

Relationships use collection IDs, not hardcoded own-site URLs.

### 10.7 Global data

`src/data/site.ts` is the one owner of:

- identity mark/name/location;
- primary navigation labels/order;
- external GitHub/LinkedIn/source-repository links;
- theme/gallery control labels;
- legal footer copy;
- static portrait-slide copy.

Components consume this data; they do not duplicate it.

---

## 11. Public route disposition — frozen

### 11.1 Preserve as real static pages

| Route | Final source |
|---|---|
| `/` | `pages/home.md` |
| `/projects/` | project collection index |
| `/projects/agentic-career-boost/` | project collection |
| `/projects/p3ctex/` | project collection |
| `/projects/aaaat/` | project collection |
| `/projects/ironbank/` | project collection |
| `/blog/` | post collection index |
| `/blog/agents-need-receipts/` | post collection |
| `/blog/static-sites-as-workbenches/` | post collection |
| `/blog/sprint-review-agenticcareerboost/` | post collection |
| `/cv/ml/` | CV collection |
| `/cv/agentic/` | CV collection |
| `/cv/backend/` | CV collection |
| `/cv/print/` | CV collection |
| `/focus/` | focus index |
| `/focus/ml/` | focus collection |
| `/focus/agentic/` | focus collection |
| `/focus/backend/` | focus collection |
| `/contact/` | `pages/contact.md` |

### 11.2 Retire with static redirect

| Current route | Final destination | Reason |
|---|---|---|
| `/dashboard/` | `/projects/agentic-career-boost/` | old sprint/status surface no longer matches current project model |
| `/application-tracker/` | `/projects/agentic-career-boost/` | local scratch is not a public product/demo |

### 11.3 Preserve old aliases with static redirect

| Alias | Destination |
|---|---|
| `/curriculum/` | `/cv/ml/` |
| `/notes/` | `/blog/` |
| `/hire/` | `/focus/` |
| `/hire/ml/` | `/focus/ml/` |
| `/hire/agentic/` | `/focus/agentic/` |
| `/hire/backend/` | `/focus/backend/` |

`/index.html` naturally resolves to the generated root `index.html`; `/projects/index.html` naturally resolves to the generated project index file. Trailing-slash directory routes are produced by `build.format: 'directory'` and `trailingSlash: 'always'`.

Configured redirects are generated by Astro as static redirect HTML. Redirect destinations are passed through the build's base-path helper; no deployment prefix is stored in the route table.

There is no hash router and no custom 404 route discovery.

---

## 12. Application Tracker boundary — frozen

The refactor performs only public decoupling:

- remove `/application-tracker/` as a public page;
- remove the tracker fragment from the AgenticCareerBoost project page;
- remove the public tracker link from the AAAAT page;
- remove tracker demo generation from site/CI/deploy workflows;
- remove any public copy implying a maintained tracker demo.

The refactor does **not** modify:

- `application-tracker/acb_tracker.py`;
- `application-tracker/acb_tracker_readonly.py`;
- `application-tracker/start_tracker.py`;
- `application-tracker/letter.ps1`;
- `application-tracker/render_letter.py`;
- `.private/` boundaries;
- local launcher scripts for the scratch tracker.

The scratch remains inspectable in repository history/source without being presented as a current public feature.

---

## 13. Dashboard/status boundary — frozen

The public dashboard is removed rather than ported.

Remove from the publication path:

- `/dashboard/` page;
- `statusDashboard` UI concept;
- `site/data/status.json` consumption;
- status generation step in `site-build.yml` and `required-ci.yml`;
- `.github/workflows/export-status.yml`;
- `agents/tools/export_status.py`;
- old static-site validator requirements for status/dashboard.

`agents/state/current.md`, `active-sprint.md`, `roadmap.md` and historical closure logs remain source/history documents; they are not converted into a public live dashboard.

---

## 14. Content migration/editorial contract

### 14.1 Default rule

Migrate the **current main copy**, not older draft copies. Do not perform a generic AI rewrite while changing architecture.

### 14.2 Required factual edits only

Change copy where the old architecture would become false, including:

- JSON/browser-renderer descriptions of the current site;
- public tracker-demo references;
- live dashboard/status claims;
- CV/focus descriptions that explicitly call the current publication model JSON-driven after the migration.

### 14.3 Historical posts

The three dated blog entries are historical snapshots. Preserve their substance and date. If a paragraph describes the architecture that existed when written, do not rewrite history to pretend Astro existed then. Add at most one compact context note when needed to distinguish past architecture from current architecture.

### 14.4 Voice

Public writing must remain artifact-led, technical and human. Avoid:

- AI hype;
- recruiter pitch language;
- generic portfolio slogans;
- student-first framing;
- defensive "not X but Y" loops;
- repeated claims of being "useful", "honest" or "proof" instead of showing the artifact;
- symmetrical generated prose;
- inflated production/seniority claims.

---

## 15. Visual contract — parity and cleanup, not redesign

### 15.1 Preserve

The refactor keeps the site's recognizable visual language:

- warm paper/grid light theme;
- current dark theme family;
- black/ink borders and technical document framing;
- teal active state, terracotta accent and green signal palette;
- monospaced system/index labels;
- identity/navigation rail;
- document-centered composition;
- metadata rail where useful;
- 418 banner identity artwork;
- CRT/holo/monitor treatment as a restrained signature interaction;
- current custom portrait and project imagery;
- reduced-motion behavior;
- print treatment for CV.

### 15.2 Structural CSS rewrite

The current ~41 KB monolithic stylesheet is not copied wholesale. The new CSS is reconstructed from the visual primitives above:

- `tokens.css`: palette, type, spacing, widths, borders, timing;
- `base.css`: reset, typography, links, accessibility fundamentals;
- `site.css`: shell, navigation, document sections, cards/lists, gallery, responsive rules and restrained effects;
- `print.css`: CV/document print behavior.

Delete selectors that exist only for discarded historical markup.

### 15.3 Explicit visual prohibitions

Do not introduce:

- generic SaaS cards;
- glassmorphism;
- giant marketing hero sections;
- random gradients;
- generic Tailwind-looking spacing/components;
- stock illustrations/icons;
- generated AI artwork;
- excessive rounded boxes;
- animation added only for spectacle;
- a "clean modern portfolio" redesign that erases the current identity.

### 15.4 Verification responsibility

Automated checks never approve aesthetics or subjective UX, but this does **not** transfer implementation verification to the user.

ChatGPT owns verification of every objective property it changes: source consistency, buildability, generated routes, links/assets, metadata, deployment independence, browser loading, navigation, theme behavior, gallery behavior, same-origin request failures, console/page errors, and gross horizontal overflow at the defined representative viewports.

The user owns only the judgments that cannot be observed through the current connector: visual composition, hierarchy, density, aesthetics, and whether the interaction *feels* good.

ChatGPT must not say "looks good", "UX is correct" or equivalent from automated checks. It may say exactly which objective contracts passed and which subjective visual gate remains.

---

## 16. Local visual review — intentionally trivial

The existing root `localdeploy.bat` remains the single user entrypoint. It exists only because the connected GitHub app cannot expose a private interactive branch preview to ChatGPT.

Final behavior:

1. User double-clicks `localdeploy.bat` from their current checkout.
2. The script changes directory to `site/`.
3. If Node is missing or older than 22.12, it prints one direct requirement message and exits.
4. If `node_modules/astro` is absent, it runs the dependency install once.
5. It runs `npm run dev -- --open`.
6. Astro opens the local site in the default browser.

The launcher does **not** run tests, QA, Playwright, PDFs, Python, Git operations, Docker or deployment.

### Human visual gates

There are exactly **two** human visual gates in the entire refactor:

- **V1 — visual foundation:** after the representative Home/Projects/ACB/P3CTeX shell is complete and all autonomous checks pass. This prevents migrating the whole site on top of a visually wrong foundation.
- **V2 — final site:** after all routes, content, artifacts and CI alignment are complete and all autonomous checks pass.

There is no human gate after the mechanical content-migration phase.

At V1/V2 ChatGPT reports the exact branch SHA plus the autonomous verification result. The user only opens `localdeploy.bat` and either approves the visual direction or reports what is visibly wrong. No QA checklist is delegated to the user. If useful, the user may attach screenshots to the chat; ChatGPT can inspect user-uploaded images directly and perform the visual critique itself.

---

## 17. Autonomous branch verification owned by ChatGPT

Create one `.github/workflows/site-check.yml`. Its purpose is to make the agent responsible for proving objective correctness of its branch without publishing it.

### Trigger

`push` to `DidacLl/siterefactor` for `site/**`, `localdeploy.bat`, or this workflow.

Use workflow concurrency for this branch with `cancel-in-progress: true`. Connector text writes may create several small commits; obsolete runs are cancelled and the latest branch SHA is the only result that matters. No sentinel file and no PR are required.

### Permissions

`contents: read` only. No Pages, deployment or identity-token permission.

### Verification steps

1. Checkout the exact pushed SHA.
2. Set up Node 24.
3. Install the pinned site dependencies.
4. Build the site for base `/`.
5. Run `site/scripts/verify-build.mjs` against that output.
6. Build the same source for base `/AgenticCareerBoost/`.
7. Run the same verifier against that output.
8. Install `playwright@1.62.1 --no-save` and its Chromium runtime in the GitHub runner only.
9. Run `site/scripts/browser-smoke.mjs` with Chromium against the root-base build.

`verify-build.mjs` is a single repo-local Node script using Node built-ins. It verifies only explicit architecture invariants, not aesthetic preferences:

- every PRESERVE route from the frozen route ledger has generated HTML;
- every REDIRECT route targets the frozen destination;
- RETIRE routes are not regenerated as content pages;
- internal `href`, `src`, manifest and stylesheet references resolve inside the generated artifact;
- no source file contains a hardcoded own production origin or deployment prefix;
- each public HTML page contains title, description, canonical metadata and one main content region;
- generated links/assets honor the configured base;
- the two builds contain the same semantic route set independent of base path.

`browser-smoke.mjs` is a plain Node script using the Playwright library, not a Playwright Test suite. It starts its own temporary Node HTTP server for the generated build, so no extra server package/framework is added.

The browser smoke contract is intentionally small and factual. It does not score design. It verifies:

- the Home page and every preserved route loads without an uncaught page error;
- no failed same-origin request occurs while loading representative routes;
- ordinary navigation reaches the expected URL;
- theme toggle changes theme and persists after reload;
- gallery previous/next and expand/collapse change their declared state;
- representative desktop and mobile pages do not produce document-level horizontal overflow.

No screenshot comparison, pixel threshold, accessibility score, Lighthouse score, visual "quality" heuristic or generated aesthetic verdict is permitted.

### Agent verification loop

After every coherent implementation batch, ChatGPT must:

1. read the branch head SHA;
2. locate the latest `site-check` push run for that exact SHA through the GitHub Actions read API;
3. read failed job logs/steps if any;
4. fix the concrete fault on the same branch;
5. repeat until the exact head SHA is green;
6. compare the branch with the frozen baseline and inspect the changed-path scope;
7. only then continue or present a human visual gate.

A green run permits ChatGPT to claim only the contracts above. It does not permit an aesthetic/UX claim.

## 18. Client-side JavaScript budget

The final site has only two intentional client behaviors:

1. theme persistence/toggle;
2. gallery previous/next/expand interaction.

Everything needed to understand the page exists in prerendered HTML.

Remove completely:

- `data-store.js`;
- `router.js`;
- `renderer.js`;
- `components.js`;
- `os.js`;
- old `widgets.js`;
- `gallery-model.js`.

Navigation works as ordinary links with JavaScript disabled.

---

## 19. Generated public CV and report artifacts

### 19.1 Public URL contract

Public URLs stay under:

```text
/files/cv/...
/files/reports/...
```

The underlying generated files move from old `site/files/**` build staging to:

```text
site/assets/files/cv/**
site/assets/files/reports/**
```

because `site/assets/` is Astro's public directory.

These generated outputs remain ignored by Git.

### 19.2 CV

Update `agents/cv/artifacts.json`:

```text
sitePdf: site/assets/files/cv/didac-llorens-cv.pdf
```

Update `agents/cv/tools/artifact_manifest.py` so its validation accepts only `site/assets/files/**` as the public destination.

The web CV reads the public CV target from the manifest at build time; it does not duplicate the filename in page copy.

### 19.3 Reports

Create `site/src/data/reports.json` as the single publication catalog for the 11 currently linked public reports:

- `agenticcareerboost-project-history.pdf`
- `agentic-system-guide.pdf`
- `s000-agentic-os-bootstrap.pdf`
- `s001-profile-audit-positioning.pdf`
- `s0015r-system-review.pdf`
- `s002-restart-refresh.pdf`
- `s003-website-os-clarity.pdf`
- `s004-documentation-alignment.pdf`
- `s0045-site-quality.pdf`
- `agentic-system-refactor-retrospective.pdf`
- `agentic-system-evidence-reconciliation.pdf`

The catalog owns public filename, display title and description.

Update `publish-public-reports.py` to read this catalog and copy exactly those compiled PDFs into `site/assets/files/reports/`. It no longer parses the old JSON site content or later Markdown for filenames.

The AgenticCareerBoost project page renders its evidence library from the same catalog.

### 19.4 Local launcher

Missing generated PDFs do not block local UI viewing. The local launcher does not compile LaTeX. Production/CI builds generate the files before Astro builds the final Pages artifact.

---

## 20. Production workflow changes prepared on the refactor branch

Updating the workflow files on `DidacLl/siterefactor` does not deploy because the production workflow trigger remains `push: main`.

### 20.1 ACB `.github/workflows/site-build.yml`

Keep the existing main-only deployment boundary. Replace only the obsolete site preparation steps:

1. checkout;
2. `actions/configure-pages` with `id: pages`;
3. compile public report TeX;
4. publish reports into `site/assets/files/reports/`;
5. resolve/compile public CV;
6. publish CV into `site/assets/files/cv/`;
7. setup Node 24.20.0;
8. install exact site dependencies with `npm install --prefix site --no-package-lock`;
9. build Astro with:
   - `SITE_ORIGIN = pages.outputs.origin`
   - `SITE_BASE = pages.outputs.base_path`
   - `SITE_INDEXABLE = false`;
10. upload `site/dist` as Pages artifact;
11. deploy only in the existing main-only deploy job.

Remove:

- status generation;
- Application Tracker demo generation;
- old `validate_static_site.py` invocation;
- upload of raw `site/` source.

### 20.2 `.github/workflows/required-ci.yml`

Keep its current main/PR role but replace the obsolete site steps with:

- report build/publish;
- CV build/publish;
- Node setup;
- Astro build;
- existing Markdown link validation.

Remove status/demo/old-site-validator coupling. Do not duplicate the branch browser smoke in `required-ci`; `site-check.yml` is the single owner of the non-deploy functional browser contract. No visual/aesthetic tests are added.

### 20.3 Delete obsolete workflow/tool

Delete:

- `.github/workflows/export-status.yml`;
- `agents/tools/export_status.py`;
- `agents/tools/validate_static_site.py`.

They encode the retired dashboard/old runtime architecture and would otherwise remain misleading active tooling.

Historical logs describing them remain untouched.

---

## 21. `didacll.github.io` publication surface

`DidacLL/didacll.github.io` remains completely untouched during this refactor plan.

Its current workflow is known to be incompatible with the final Astro source because it presently checks out ACB `main` and uploads `source/site` directly. It also currently differs from the ACB build pipeline.

The exact cutover requirement is frozen now so it is not rediscovered later:

When and only when the user separately authorizes production cutover, its `deploy.yml` must be changed to:

1. checkout ACB `main` into `source/`;
2. configure Pages and capture `origin`/`base_path`;
3. compile/publish the same public reports;
4. compile/publish the same public CV;
5. setup Node 24.20.0;
6. install site dependencies;
7. build `source/site` with `SITE_ORIGIN`, `SITE_BASE`, and `SITE_INDEXABLE=true`;
8. upload `source/site/dist`;
9. deploy.

It must not generate status or Application Tracker output.

This requirement is documented here, but **no root-repository write is authorized by this plan**.

---

## 22. Root/site legacy cleanup inside ACB

After Astro parity and user visual acceptance, remove old text-only web implementation files:

- root `index.html`;
- root `404.html`;
- root `.nojekyll`;
- root `robots.txt`;
- root `sitemap.xml`;
- `site/index.html`;
- `site/404.html`;
- `site/manifest.json`;
- `site/.nojekyll`;
- `site/content/**` old JSON/fragments;
- `site/assets/css/site.css`;
- all old `site/assets/js/*.js`;
- old `site/files/reports/README.md`.

The existing binary `site/assets/img/**` tree is retained.

Update `.gitignore` from old generated `site/files/**` paths to `site/assets/files/**`, and add `site/node_modules/`, `site/dist/`, `site/.astro/` if not already covered by root patterns.

Do not delete historical `agents/state/logs/**`, report sources, CV sources or Application Tracker scratch files.

---

## 23. Execution phases

### Phase 1 — Foundation and visual shell

**Goal:** establish the real architecture and a visually recognizable representative slice before migrating all content.

Operations:

1. verify Section 3.3 preconditions;
2. continue on the existing `DidacLl/siterefactor` branch, which already descends directly from the exact baseline;
3. retain this masterplan and tracker at their authoritative `agents/` paths;
4. add Astro package/config/content-schema/path/global-data foundation;
5. add Base/Document/Project layouts and minimal components;
6. reconstruct the current visual shell/tokens/theme/gallery without generic redesign;
7. migrate Home, Projects index, AgenticCareerBoost and P3CTeX;
8. update `localdeploy.bat` to the simple Astro launcher;
9. add `site/scripts/verify-build.mjs`, the minimal browser smoke contract, and `site-check.yml`;
10. locate the exact-SHA branch run and read its logs;
11. fix every objective build/link/route/browser-contract failure until the exact head SHA is green;
12. compare changed paths against baseline for scope leakage;
13. report exact green head SHA and **STOP at visual gate V1**.

Phase gate: user explicitly authorizes continuation after browsing locally.

### Phase 2 — Complete public content migration

**Goal:** eliminate the browser-renderer architecture and migrate every preserved route.

Operations:

1. migrate AAAAT and IronBank project entries;
2. migrate all three blog entries;
3. migrate all four CV views;
4. migrate focus index + three focus pages;
5. migrate Contact;
6. implement static 404;
7. implement legacy/retired-route redirects;
8. remove dashboard and Application Tracker public references;
9. remove old JSON block content and old client runtime modules;
10. remove obsolete old stylesheet only after new CSS owns all rendered selectors;
11. let branch CI verify the complete migration at the exact head SHA;
12. read/fix all objective failures until green;
13. compare changed paths against baseline and continue directly to Phase 3.

Phase gate: autonomous verification only. **No user action is required in Phase 2.**

### Phase 3 — Artifacts, CI and repository alignment

**Goal:** make the branch production-build-ready without deploying it.

Operations:

1. move generated public CV target to `site/assets/files/cv/` through manifest/tool text changes;
2. create reports publication catalog;
3. update report publisher target/catalog logic;
4. update `.gitignore` generated paths;
5. update ACB `site-build.yml` for Astro `dist` while preserving main-only deploy trigger;
6. update `required-ci.yml` for Astro build and remove obsolete status/tracker steps;
7. delete `export-status.yml`, `export_status.py`, and `validate_static_site.py`;
8. update `site/README.md`, root `README.md` only where current architecture/public-surface facts changed, and root `AGENTS.md` minimally so future agents know the approved site boundary;
9. remove the unused legacy root/site web entry files listed in Section 22;
10. run the autonomous branch verification on the final exact head SHA;
11. read/fix all objective failures until green;
12. inspect the complete branch diff against baseline for scope leakage;
13. report exact final green branch SHA and **STOP at visual gate V2**.

Phase gate: user confirms the final visual/interaction feel locally. Objective navigation/functionality has already been verified remotely by the agent.

### End state of this plan

Stop. Do not create PR. Do not merge. Do not deploy. Do not modify `didacll.github.io`.

The branch is now a reviewed production candidate. Production cutover requires a new explicit user instruction.

---

## 24. Failure handling

### Build failure

Read the exact Actions job log and fix the concrete failure only. Do not broaden into unrelated lint/test/framework work.

### User reports visual defect

Patch only the affected source/CSS/content. Let branch verification run again, fix objective regressions, then return to the same human visual gate.

### Existing unrelated defect discovered

Record it in the tracker under `Deferred`; do not repair it unless it blocks the current refactor output.

### Main changes during execution

If `main` moves after branch creation, do not silently rebase/merge. Continue the isolated branch unless the user explicitly asks to reconcile it. Production cutover will reconcile current main under a separate authorization.

### Connector capability mismatch

If an operation explicitly required by this plan is unavailable at execution time, stop before substituting a different mechanism. Report the exact missing capability.

---

## 25. Acceptance criteria

The branch is complete only when all of the following are true:

### Architecture

- every preserved public route is prerendered static HTML;
- narrative content is Markdown;
- frontmatter is small and schema-validated;
- no JSON block DSL remains;
- no client router/data-store/renderer remains;
- ordinary navigation works without JavaScript;
- only theme/gallery behavior uses client JS.

### Single ownership / portability

- no own production origin is hardcoded in site source;
- no deployment prefix is hardcoded in site source;
- internal collection routes derive from IDs/path helpers rather than duplicated entry routes;
- navigation/identity copy has one owner;
- report publication filenames have one catalog;
- CV publication target has one manifest owner;
- all internal/public-asset hrefs are base-aware.

### Public scope

- Application Tracker is no longer exposed as a public demo/product;
- dashboard/status route and pipeline are gone;
- local Application Tracker/letter renderer remains untouched;
- ACB, P3CTeX, AAAAT and IronBank project pages remain;
- blog, CV, focus and contact remain;
- public report and CV links remain represented.

### Visual

- current retro-document identity is recognizably preserved;
- no generic portfolio redesign has been introduced;
- user has locally reviewed only visual gates V1 and V2; Phase 2 required no user QA;
- GPT has not substituted automated tests for that visual judgment.

### Build and safety

- final branch exact SHA passes `site-check.yml` build, route/link/base and browser functional contracts;
- `site-check.yml` has only `contents: read`;
- no branch workflow deploys Pages;
- ACB production workflow still deploys only from `main`;
- neither public URL was changed during development;
- no write was made to `didacll.github.io`;
- no PR or merge was created by this plan.

---

## 26. Explicit out-of-scope items

- production cutover;
- redesign of the user's visual identity;
- Application Tracker development/cleanup;
- AAAAT or VCVGenerator product work;
- repo-wide agent-harness refactor;
- historical log rewrite;
- report/CV content redesign unrelated to site integration;
- cross-repository project federation/automatic metadata import;
- image transcoding/optimization that requires binary rewrites;
- analytics;
- CMS;
- staging host;
- browser automation as aesthetic QA.

---

## 27. Frozen result

The intended result is deliberately boring at the infrastructure layer:

```text
Markdown + small typed metadata
        ↓
Astro layouts/components
        ↓
static HTML + CSS + two tiny JS behaviors
        ↓
GitHub Pages deployment configuration
```

The distinctive part remains the actual site: Dídac's technical/documentary visual language, projects, reports, CV, writing and repository history.

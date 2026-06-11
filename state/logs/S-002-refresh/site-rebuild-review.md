# S-002 Site Rebuild Review — Didac Webpage Viewpoint

- **Date**: 2026-06-11
- **Agent**: Developer/SiteArchitecture sidecar
- **Scope**: Evaluate current Didac webpage only; no production edits
- **Inputs read**: `AGENTS.md`, `docs/core/{mission,marketing,brand,constraints}.md`, `state/{current,backlog}.md`, `data/{links,public-status}.json`, `site/**`, recruiter landing blueprint, relevant asset list

## Current Verdict

The current site is a credible temporary recruiter page, not the requested S-002 rebuild.

It has a human landing page, basic project evidence, JSON-LD/OG metadata, a curriculum page, and links to PDFs. It does not yet provide project deep-dive pages, repo evidence with enough verbal explanation and images, an AgenticCareerBoost dashboard page, configurable CV views via URL parameters, or print-hardened CV behavior.

## Requirement Fit

| Request | Current fit | Evidence |
|---|---:|---|
| Attractive human landing page | 6/10 | `site/index.md` has strong identity, CTAs, architecture image, and career bridge; visual system is functional but still default-card heavy. |
| Project sections/pages | 4/10 | Landing cards and `site/projects/index.md` exist; no `/projects/agentic-career-boost/`, `/projects/p3ctex/`, or repo-specific narrative pages. |
| Repo evidence with verbal explanation and images | 4/10 | Links and one routing diagram exist; evidence needs screenshots, repo excerpts, diagrams, and plain-language interpretation per project. |
| AgenticCareerBoost dashboard page | 2/10 | `data/public-status.json` exists, but no public dashboard page visualizing sprint status, blockers, artifacts, and links. |
| CV configurable by URL params and printable | 2/10 | `site/curriculum.md` and PDF link exist; no query-param filtering, no print CSS, no recruiter/ML/agentic variants. |

## Architecture Observations

- `site/` is correctly established as canonical Jekyll source.
- Current dependencies are minimal: Jekyll, `jekyll-feed`, `jekyll-seo-tag`.
- Inline CSS in `site/_layouts/default.html` is acceptable for now but will become hard to maintain during S-002.
- Existing assets are useful: routing diagrams, synchronized status diagram, recruiter landing wireframe, formal report PDFs, and screenshot sources.
- Public status data already provides the right seed for a dashboard, but it is not surfaced.
- The current site over-indexes on assertion compared with the core rule: evidence over adjectives.

## Organization Options

| Option | Recruiter clarity | Evidence fit | Maintainability | Design quality | Total |
|---|---:|---:|---:|---:|---:|
| A. Repo-based: one page per repository | 7 | 9 | 8 | 7 | 31/40 |
| B. Job-market-topic-based: ML/Data, Agentic Systems, Tooling/Docs, Backend | 9 | 7 | 6 | 8 | 30/40 |
| C. Topic-led landing with repo-backed project pages | 10 | 9 | 8 | 9 | 36/40 |

## Selected Recommendation

Use **Option C: topic-led landing with repo-backed project pages**.

The landing page should organize around recruiter mental models: ML/Data direction, Agentic Systems, Tooling/Documentation, Backend fundamentals, and operations-to-engineering value. Each topic card should point to concrete repo-backed pages. Deep pages should remain repo-based because code, commits, reports, screenshots, and PDFs are naturally repository artifacts.

This avoids forcing recruiters to decode repository names while preserving inspectable proof for peers.

## Minimal Static Implementation Plan

Use simple Jekyll/HTML/CSS/JS only. Do not add frameworks or build dependencies.

1. Extract shared CSS from `site/_layouts/default.html` into `site/assets/css/site.css`.
2. Add `site/assets/js/cv.js` for URL-param CV filtering and print preparation.
3. Rebuild `/` as a topic-led recruiter scan:
   - hero with name, role direction, Barcelona, CTAs
   - topic bands tied to evidence
   - selected project evidence preview
   - operations-to-engineering bridge
   - contact and CV actions
4. Add repo-backed project pages:
   - `/projects/agentic-career-boost/`
   - `/projects/p3ctex/`
   - `/projects/ironbank/` only if clearly labeled as older backend evidence
5. Add `/dashboard/` for AgenticCareerBoost:
   - current sprint/status from `data/public-status.json`
   - blockers
   - artifact checklist
   - links to repo, reports, site, CI/Page status when available
6. Rework `/curriculum/`:
   - default concise CV
   - `?view=ml`, `?view=agentic`, `?view=backend`, `?view=print`
   - print stylesheet with hidden nav/buttons, controlled page breaks, visible contact links
7. Add image/evidence blocks:
   - use existing diagrams and screenshots first
   - include captions that explain why each artifact proves capability
8. Keep PDFs linked from `content/reports/build/`; do not duplicate generated PDFs into site source unless a later workflow decides that.

## Content Rules For Implementation

- Lead with Dídac, not with the system name.
- Use topics for first scan; use repositories for proof.
- Avoid generic portfolio phrasing.
- Keep ML/Data direction honest: current evidence is directional until a Python ML project exists.
- Mark IronBank as older backend evidence, not the center of the profile.
- Keep AgenticCareerBoost framed as both system and case study.
- Every visible claim should link to a repo, report, diagram, screenshot, or explicit status note.

## Proposed Quality Gates

| Gate | Check |
|---|---|
| Desktop | Build locally and inspect `/`, `/projects/`, each project page, `/dashboard/`, `/curriculum/?view=ml` at 1440px and 1024px. |
| Mobile | Inspect the same pages at 390px and 430px; no overlapping nav, clipped buttons, unreadable tables, or image overflow. |
| Print CV | Browser print preview for `/curriculum/?view=print`; nav/actions hidden, links visible, sensible page breaks, no card shadows. |
| URL params | `view=ml`, `view=agentic`, `view=backend`, and unknown params all produce valid readable CV states. |
| Links | Run existing link validation; verify GitHub, LinkedIn, PDF, project, and dashboard links. |
| Build | `bundle exec jekyll build` from `site/` passes with no broken includes or missing assets. |
| Data | Dashboard handles missing `data/public-status.json` fields gracefully if copied or embedded. |
| Accessibility | Keyboard nav works, image alt text is meaningful, contrast remains acceptable in light/dark modes. |

## Blockers / Decisions

- Professional email remains unconfirmed; keep LinkedIn as primary contact until decided.
- Pages source and branch protection are still listed as pending in current state.
- ML/Data project evidence is not yet strong enough for a dominant ML-engineer claim.
- Need user decision on whether the public CV variants are role-specific only or also language-specific.

## Final Recommendation

Proceed with an S-002 static Jekyll rebuild using a **topic-led recruiter landing page plus repo-backed evidence pages**. Add the dashboard and URL-param CV as first-class pages, keep dependencies unchanged, and make print/mobile/link/build gates mandatory before publishing.

# S-002R Task 3 Implementation Note

- Date: 2026-06-11
- Scope: `site/**`
- Status: implementation trace moved out of public site source

Implemented a static Jekyll rebuild foundation: topic-led recruiter landing
page, repo-backed project pages, dashboard snapshot, configurable curriculum
views, print CSS, and site-local CSS/JS.

## Decisions

| Decision | Options scored | Selected |
|---|---|---|
| Landing organization | A. Repo-first landing: 7/10. B. Topic-led landing with repo-backed details: 9/10. C. CV-first landing: 6/10. | B |
| Dashboard data source | A. Read root `data/public-status.json` directly from Jekyll: 4/10 because `site/` is the build root. B. Copy a maintained static snapshot into `/dashboard/`: 8/10. C. Add a build script/dependency: 3/10 due no-new-dependency constraint. | B |
| Curriculum variant mechanism | A. Separate pages per variant: 6/10. B. URL-param filtering with small JS and print fallback: 8/10. C. Generate variants at build time: 4/10 due added complexity. | B |
| Styling structure | A. Keep layout CSS inline: 5/10. B. Extract one CSS file and one small JS file: 8/10. C. Introduce a design framework: 1/10 due dependency and scope constraints. | B |

## Validation Intent

Run `bundle exec jekyll build` from `site/` when local Ruby/Jekyll tools are
available. Check `/`, `/projects/`, project detail pages, `/dashboard/`, and
`/curriculum/?view=ml|agentic|backend|print`.

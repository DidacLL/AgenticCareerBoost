# S-002R Task 3 Implementation Note

- Date: 2026-06-11
- Scope: `site/**`
- Status: implementation trace moved out of public site source

Implemented a plain static site foundation: topic-led recruiter landing page,
repo-backed project pages, dashboard snapshot, configurable curriculum views,
print CSS, and site-local CSS/JS.

## Decisions

| Decision | Options scored | Selected |
|---|---|---|
| Landing organization | A. Repo-first landing: 7/10. B. Topic-led landing with repo-backed details: 9/10. C. CV-first landing: 6/10. | B |
| Dashboard data source | A. Fetch root `data/public-status.json` from the browser: 5/10 because local/file preview and CORS behavior add friction. B. Copy a maintained static snapshot into `/dashboard/`: 8/10. C. Add a build script/dependency: 3/10 due no-new-dependency constraint. | B |
| Curriculum variant mechanism | A. Separate pages per variant: 6/10. B. URL-param filtering with small JS and print fallback: 8/10. C. Generate variants at build time: 4/10 due added complexity. | B |
| Styling structure | A. Keep layout CSS inline: 5/10. B. Extract one CSS file and one small JS file: 8/10. C. Introduce a design framework: 1/10 due dependency and scope constraints. | B |

## Validation Intent

Validate required static files, then check `/`, `/projects/`, project detail
pages, `/dashboard/`, and `/curriculum/?view=ml|agentic|backend|print`.

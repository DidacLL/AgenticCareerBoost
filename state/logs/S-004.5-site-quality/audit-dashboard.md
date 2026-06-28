# S-004.5 dashboard spec packet

Status: consumed

## Findings

- The AgenticCareerBoost page needed an embedded dashboard, not only a legacy dashboard route or source-file link list.
- Dashboard content should reflect current workflow/sprint state, blockers, closure artifacts, source files, logs, reports, validation scripts, and public status.
- The public page should link to repo source only where a human needs to inspect files or history.

## Implementation actions

- Added an embedded dashboard to `site/projects/agentic-career-boost/index.html`.
- Rebuilt `site/dashboard/index.html` as the full status dashboard.
- Added `site/assets/js/dashboard.js` to fetch generated public status JSON at runtime.
- Generated public status rows from committed state files during build/validation.


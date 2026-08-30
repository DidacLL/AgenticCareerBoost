# S-004.5 site architecture audit packet

Status: consumed

## Findings

- Site source remained plain static HTML/CSS/JS and should stay that way for this sprint.
- Runtime routes needed to avoid deployment-bound origins and project-path assumptions.
- `site/sitemap.xml` could not safely encode a canonical host in source while the same artifact may be served from different public bases.
- `site/.idea/**` and similar IDE metadata must be excluded from deployed artifacts.
- Dashboard data should be generated from repository state before site validation/upload, not copied manually.

## Implementation actions

- Kept `.nojekyll` and current static upload model.
- Removed static sitemap source artifact.
- Made manifest paths runtime-relative.
- Added generated status-data validation and deployed artifact hygiene checks.


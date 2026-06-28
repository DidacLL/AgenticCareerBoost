# S-002R Orchestrator Decision Ledger

- Date: 2026-06-11
- Scope: integrate three viewpoint reviews into the next multiagent sprint
- Inputs: three sidecar reports, current state, live site check, GitHub profile evidence

## Evidence

- `state/logs/S-002-refresh/agentic-framework-review.md`: framework cost is agent fan-out and distributed trace, not file length.
- `state/logs/S-002-refresh/site-rebuild-review.md`: current site is useful but below S-002 requirements.
- `state/logs/S-002-refresh/linkedin-reactivation-review.md`: LinkedIn needs low-heat reactivation before the main campaign.
- Public site is live at `https://didacll.github.io/`.
- GitHub profile README is stale and still points to the deprecated resume site.
- LinkedIn content cannot be externally verified because of the authwall.

## Decision 1 - Sprint Shape

| Option | Fit | Simplicity | Risk | Evidence | Total |
|---|---:|---:|---:|---:|---:|
| Continue S-001.5R until all remote/account blockers close | 5 | 6 | 5 | 7 | 23 |
| Open S-002R as a restart review and planning sprint with explicit external blockers | 9 | 8 | 4 | 9 | 30 |

Selected: open `S-002R`. S-001.5R remains historically useful, but the user request is a new restart review spanning framework, site, and social.

## Decision 2 - First Implementation Priority

| Option | Fit | Simplicity | Risk | Evidence | Total |
|---|---:|---:|---:|---:|---:|
| Start with full site rebuild | 9 | 5 | 6 | 8 | 28 |
| Start with profile consistency and social reactivation drafts | 8 | 8 | 3 | 8 | 27 |
| Start with stable workflow refactor | 7 | 6 | 7 | 8 | 28 |

Selected: plan all three, execute profile consistency plus site foundation first. Framework refactor needs system-review approval before stable docs move.

## Decision 3 - Site Organization

| Option | Recruiter clarity | Evidence fit | Maintainability | Design | Total |
|---|---:|---:|---:|---:|---:|
| Repo-only project list | 7 | 9 | 8 | 7 | 31 |
| Job-market topics only | 9 | 7 | 6 | 8 | 30 |
| Topic-led landing plus repo-backed project pages | 10 | 9 | 8 | 9 | 36 |

Selected: topic-led landing plus repo-backed pages.

## Decision 4 - LinkedIn Restart

| Option | Fit | Credibility | Risk | Effort | Total |
|---|---:|---:|---:|---:|---:|
| Three low-heat posts before the campaign | 9 | 9 | 8 | 7 | 33 |
| Direct profile-audit launch post | 8 | 8 | 5 | 8 | 29 |
| Comment-only warmup | 7 | 8 | 9 | 5 | 29 |

Selected: three low-heat posts, then the main profile-audit campaign after profile consistency gates pass.

## Quality Gates

- Framework: stable docs changed only through system-review; risk-tier and closure-matrix proposal must be pair-checked before adoption.
- Site: Jekyll build, link validation, desktop/mobile visual inspection, print CV check, query-param CV check.
- Social: primary/current sources, no unpublished project details, profile consistency, human approval before publication.
- Global: pytest, markdownlint, internal links, JSON validation, public-status consistency, no stale deprecated-site links in public-facing surfaces.


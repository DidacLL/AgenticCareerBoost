# CI + Static Site Remediation

Date: 2026-06-11

## Scope

Fix PR CI failures and remove Jekyll as a dependency for the public site.

## Decision 1: Website Delivery

| Option | Score | Reason |
|---|---:|---|
| Keep Jekyll and repair build | 4 | CI already supports it, but it contradicts the requested simplicity. |
| Plain static HTML/CSS/JS | 9 | Matches project size, lowers CI friction, keeps pages hostable on GitHub Pages. |
| Add another static generator | 3 | Replaces one unnecessary dependency with another. |

Selected: plain static HTML/CSS/JS.

## Decision 2: Exported Status Repair

| Option | Score | Reason |
|---|---:|---|
| Manually edit `data/public-status.json` only | 4 | Fast but fragile; CI regenerates the file. |
| Update exporter to parse current sprint format | 8 | Keeps CI meaningful and avoids recurring drift. |
| Remove exported status check | 2 | Reduces accountability for dashboard data. |

Selected: update exporter and regenerate status.

## Decision 3: Markdownlint Failure

| Option | Score | Reason |
|---|---:|---|
| Exclude the failing draft | 5 | Fast, but hides formatting debt. |
| Format the draft to pass lint | 8 | Keeps the artifact available and preserves CI coverage. |
| Remove the draft | 3 | Too destructive for user-provided planning content. |

Selected: format the draft.

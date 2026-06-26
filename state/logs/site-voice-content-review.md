# Site voice content review

Date: 2026-06-26

## Purpose

Review and rewrite the public website text so the site sounds more like Dídac's personal technical space rather than a thin recruiter-facing CV shell.

The target voice is informal, technical, human, evidence-led, and slightly sharp where useful. The content must avoid AI-hype, generic recruiter language, student-first framing, and polished-but-empty portfolio copy.

## Scope

Updated public-facing website content only. No CSS, deployment logic, account metadata, or publication status changes.

## Files updated

- `site/index.html`
- `site/projects/index.html`
- `site/projects/agentic-career-boost/index.html`
- `site/projects/p3ctex/index.html`
- `site/projects/ironbank/index.html`
- `site/blog/index.html`
- `site/blog/agents-need-receipts/index.html`
- `site/blog/static-sites-as-workbenches/index.html`
- `site/blog/sprint-review-agenticcareerboost/index.html`
- `site/contact/index.html`
- `site/hire/index.html`
- `site/hire/agentic/index.html`
- `site/hire/ml/index.html`
- `site/hire/backend/index.html`
- `site/assets/data/blog-index.json`
- `site/assets/data/os-index.json`
- `site/sitemap.xml`
- `state/current.md`
- `data/public-status.json`

## Content decisions

- Home now frames the site as a personal workbench for readers who want more than the CV.
- Projects now explain what each artifact proves, why it exists, and where it fits in the route.
- AgenticCareerBoost gets a longer explanation of the workflow discipline, current sprint state, and the difference between the career use case and the engineering artifact.
- P3CTeX is framed as document/tooling engineering, not just a LaTeX curiosity.
- IronBank is framed honestly as older backend evidence, not a current flagship.
- Blog is now a publication and sprint-note shelf, not a placeholder archive.
- Added three local blog entries: `Agents need receipts`, `Static sites as workbenches`, and `AgenticCareerBoost sprint review`.
- Focus views now explain why each route exists and what kind of work it is meant to support.
- Contact page now states the kind of conversations that make sense and rejects vague AI/CRUD/data-maintenance drift.

## Boundary

The blog entries are local publication/project/sprint slots. External LinkedIn post URLs are not invented before publication.

## Next gate

Open PR, run required CI, inspect rendered site, then merge if static-site validation and required checks pass.

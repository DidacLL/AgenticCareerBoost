# Site voice content review

Date: 2026-06-26

## Purpose

Review and rewrite the public website text so the site sounds like Dídac's personal technical workbench rather than recruiter-facing or LLM-shaped copy.

The target voice is informal, technical, human, evidence-led, and slightly sharp where useful. The content must avoid AI-hype, generic recruiter language, student-first framing, polished-but-empty portfolio copy, sales-representative tone, and defensive justification loops.

## Scope

Public-facing website copy and supporting public JSON metadata only. No CSS, deployment logic, account metadata, or publication status changes.

## Files updated in the first voice pass

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

## Content decisions from the first pass

- Home frames the site as a personal workbench for readers who want more than the CV.
- Projects explain what each artifact proves, why it exists, and where it fits in the route.
- AgenticCareerBoost explains the workflow discipline and the difference between the career use case and the engineering artifact.
- P3CTeX is framed as document/tooling engineering, not just a LaTeX curiosity.
- IronBank is framed honestly as older backend evidence, not a current flagship.
- Blog is a publication and sprint-note shelf, not a placeholder archive.
- Focus views explain why each route exists and what kind of work it is meant to support.
- Contact page states the kind of conversations that make sense.

## Follow-up dehype pass

Branch: `codex/site-copy-dehype`

This pass removes LLM wording leakage visible after the first rewrite:

- repeated "not X, but Y" explanations;
- sales-like self-justification;
- paragraphs that explain why the page deserves to exist;
- overuse of "useful", "honest", "public proof", and similar soft persuasion words;
- symmetrical generated phrasing that sounds clean but not authored.

## Files updated in the dehype pass

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

## Dehype copy rules applied

- Lead with the artifact, not with a pitch.
- Use first person where it clarifies authorship, not as constant self-defense.
- Keep evidence words concrete: source, files, reports, checks, routes, state, commits, review gates.
- Cut recruiter-style positioning filler.
- Keep the voice technical and slightly sharp, but avoid making every paragraph a manifesto.

## Boundary

The blog entries are local publication/project/sprint slots. External LinkedIn post URLs are not invented before publication.

## Next gate

Open PR, run required CI, inspect rendered site, then merge if static-site validation and required checks pass.

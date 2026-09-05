# AGENTS.md

This repository remains Didac's personal career workspace and public proof record.
It is not a generic software product and it is not the development home for
AAAAT or VCVGenerator. It also owns source for the independent **SCVRIA Sofware**
public website surface described below.

## Scope

- Preserve the current local working data. Do not move, rename, delete, stage,
  paste, summarize, or inspect private application data unless explicitly asked.
- `application-tracker/` is scratch/prototype evidence for the later AAAAT
  redesign. Do not expand it here.
- The cover-letter renderer and `letter.ps1 <slug>` flow are valuable local
  workflow. Preserve that interface.
- `site/` is currently the Markdown-authored Astro personal portfolio. It and any
  later SCVRIA website source in this repository are public website source only;
  do not use public-site trees as storage for ACB reports, harness evidence,
  tracker output, status data, or application material.
- `agents/cv/` contains intentionally public/general CV source and build support.
  The selected public CV PDF is the only generated document intentionally served
  by the personal portfolio. CV-owned source assets stay under `agents/cv/`; site
  cleanup is not authority to move or delete dependencies of the CV build.
- `agents/reports/`, `agents/state/`, `agents/rules/`, `agents/tests/`, and
  `agents/work/` contain repository evidence, research, historical/work records,
  or legacy harness material. They are not site content and old material there is
  not current instruction unless the user explicitly reactivates it.
- Tailored letters, raw offers, private JSON, generated private PDFs, databases,
  recruiter notes, and application-specific CV variants stay local and untracked.

## Public Website Surfaces

AgenticCareerBoost remains the canonical source repository for Dídac's personal
portfolio, the existing public CV build, shared website presentation primitives,
and the SCVRIA Sofware public website surface.

- **Personal portfolio:** Dídac Llorens' professional identity, CV, projects,
  blog, and contact surface. Existing public routes, URLs, and positioning are
  compatibility-sensitive during the SCVRIA rollout.
- **SCVRIA Sofware:** an independent open-source software publisher/studio
  surface. Its brand, product content, and information architecture must remain
  semantically separate from personal career and job-search material.
- **Deployment wrappers:** `DidacLL/didacll.github.io` and
  `scvriasofware/scvriasofware.github.io` are deployment/bootstrap wrappers.
  They consume a pinned/current AgenticCareerBoost source revision and must not
  become source-of-truth copies of either website.

Until the SCVRIA site is independently online and verified, do not change the
public positioning of `didacll.github.io`, replace personal GitHub/portfolio URLs
in CV material, transfer product repositories as part of website work, remove or
rename existing public portfolio routes, or expose application-tracker,
recruiter, tailored CV/letter, offer, or other private career data. Integrating
SCVRIA into the personal portfolio is a later explicit rollout step.

SCVRIA website work does not authorize moving or rewriting the whole existing
`site/` tree; npm workspaces or package-monorepo machinery; a standalone design-
system package; React, Vue, Svelte, or another client framework; CMS, backend,
authentication/accounts, newsletter, or commerce infrastructure; repository
transfers; CV redesign; migration of personal blog content into SCVRIA; broad
cleanup unrelated to the active issue; or committing generated website artifacts
as source.

## Working Rules

- Direct user instructions override repository guidance.
- Do not use staged, unstaged, tracked, or ignored status as semantic truth.
  Classify changes by scope before changing or staging them.
- Do not develop AAAAT or VCVGenerator in this repository cleanup.
- Do not add framework machinery, package architecture, MCP servers, app
  launchers, or policy tests without explicit approval.
- Site changes use ordinary Astro routes, Markdown content and the existing
  shared data/path owners; do not recreate the old client router/content DSL.
- SCVRIA work follows the issue-scoped rollout. One phase should normally own one
  dedicated branch/PR; do not infer authorization for later phases or personal-
  portfolio integration from an earlier SCVRIA issue.
- Keep documentation short, human-readable, and honest about what is public,
  private, scratch, historical evidence, or future work.
- Use fake examples for docs and checks.

## Checks

Use operational checks relevant to the change. Historical harness tests are not
site acceptance criteria unless explicitly reactivated.

- the letter renderer can produce TeX from a fake local JSON file;
- PDF compilation may be checked only when the relevant LaTeX workflow is in scope;
- the public/general CV source remains present;
- staged paths must not include private JSON, `.private`, raw offers, databases,
  generated private PDFs, recruiter notes, or tailored application material.

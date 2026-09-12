# AGENTS.md

This repository is Didac's personal career workspace and public proof record.
It is not a generic software product and it is not the development home for
AAAAT or VCVGenerator.

## Scope

- Preserve the current local working data. Do not move, rename, delete, stage,
  paste, summarize, or inspect private application data unless explicitly asked.
- `application-tracker/` is scratch/prototype evidence for the later AAAAT
  redesign. Do not expand it here.
- The cover-letter renderer and `letter.ps1 <slug>` flow are valuable local
  workflow. Preserve that interface.
- **Tailored job-application artifacts follow
  [`agents/cv/APPLICATION_WORKFLOW.md`](agents/cv/APPLICATION_WORKFLOW.md).**
  This is active guidance, not historical harness evidence. In particular, a
  request for `CV + carta adjunta` normally means one local two-page TeX/PDF:
  page 1 is the one-page tailored CV and page 2 is the cover letter.
- `site/` is the Markdown-authored Astro portfolio. It contains only material
  actually served by the portfolio; do not use it as storage for ACB reports,
  harness evidence, tracker output, status data, or application material.
- `agents/cv/` contains intentionally public/general CV source and build support.
  The selected public CV PDF is the only generated document intentionally served
  by the portfolio. CV-owned source assets stay under `agents/cv/`; site cleanup
  is not authority to move or delete dependencies of the CV build.
- `agents/reports/`, `agents/state/`, `agents/rules/`, `agents/tests/`, and
  `agents/work/` contain repository evidence, research, historical/work records,
  or legacy harness material. They are not site content and old material there is
  not current instruction unless the user explicitly reactivates it.
- Tailored letters, raw offers, private JSON, generated private PDFs, databases,
  recruiter notes, and application-specific CV variants stay local and untracked.

## Working Rules

- Direct user instructions override repository guidance.
- For application work, read the vacancy/request and
  `agents/cv/APPLICATION_WORKFLOW.md` before drafting. Reuse the shared CV
  preamble and established layout instead of inventing a generic resume format.
- The tailored CV page remains one page. Its main column starts with the visible
  `\cvAbstract{...}` narrative opener; do not replace it with a long chronology
  or bury it below project sections.
- `\cvParserSummary`/role metadata may deliberately expose exact supported job
  vocabulary for ATS/AI retrieval, but hidden text must never add unsupported
  claims.
- Do not use staged, unstaged, tracked, or ignored status as semantic truth.
  Classify changes by scope before changing or staging them.
- Do not develop AAAAT or VCVGenerator in this repository cleanup.
- Do not add framework machinery, package architecture, MCP servers, app
  launchers, or policy tests without explicit approval.
- Site changes use ordinary Astro routes, Markdown content and the existing
  shared data/path owners; do not recreate the old client router/content DSL.
- Keep documentation short, human-readable, and honest about what is public,
  private, scratch, historical evidence, or future work.
- Use fake examples for docs and checks.

## Checks

Use operational checks relevant to the change. Historical harness tests are not
site acceptance criteria unless explicitly reactivated.

- the letter renderer can produce TeX from a fake local JSON file;
- PDF compilation may be checked only when the relevant LaTeX workflow is in scope;
- the public/general CV source remains present and compiles from the canonical
  `agents/cv/tex/` root;
- staged paths must not include private JSON, `.private`, raw offers, databases,
  generated private PDFs, recruiter notes, or tailored application material.

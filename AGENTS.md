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
  This is active guidance, not historical harness evidence.
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
- **Requested artifact formats are literal and take precedence over shorthand.**
  In this ACB workflow, the CV artifact is TeX. Do not invent a CV JSON schema.
  If the user asks for `CV en TeX + carta en JSON`, `CV + carta JSON`, or an
  equivalent formulation, deliver **two separate files**: one tailored `.tex`
  CV and one cover-letter `.json` matching the existing standalone letter input
  shape exactly. Do not append a letter page to the CV in that case.
- A plain `CV + carta adjunta` with no separate format request may use the
  combined two-page TeX convention documented in `APPLICATION_WORKFLOW.md`.
  An explicit `JSON`, `separado`, `formulario`, or other output instruction
  overrides that default.
- Do not wrap cover-letter JSON in `application`, `candidate`, `cv`,
  `cover_letter`, `claim_controls`, or other invented objects; do not add a
  second JSON for the CV.
- **Routine tailored-application work uses the documented fast path.** Treat
  `didac-cv-shared-preamble-v1.tex` and `418-banner.png` as stable local build
  dependencies. Do not fetch, inspect, download, reproduce, or explain them just
  to prepare a tailored CV/letter. Only inspect those assets when the user asks
  to change the design/build infrastructure, or when an actual compilation
  failure specifically requires diagnosis there.
- If the user asks for a `.tex` or `.json` artifact, create the file in the
  current local/artifact environment and return a download/file link. **Do not
  satisfy the request by pasting raw TeX or JSON into chat** when file creation
  is available. `solo dame el tex` means deliver the file, not print its source.
  Tailored application files remain local/untracked; do not commit them merely
  to make them downloadable.
- Do not compile a tailored source, fetch binary assets, or inspect build helpers
  unless the requested deliverable or validation actually requires compilation.
  A request for the TeX file alone ends when the correct local file has been
  materialized and linked.
- The tailored CV page remains one page. Its main column starts with the visible
  `\cvAbstract{...}` narrative opener; do not replace it with a long chronology
  or bury it below project sections.
- `\cvParserSummary`/role metadata may deliberately expose exact supported job
  vocabulary for ATS/AI retrieval, but hidden text must never add unsupported
  claims.
- **Harness-only fixes stay in the harness.** If an agent-behavior problem is
  being corrected, change `AGENTS.md` and/or `agents/cv/APPLICATION_WORKFLOW.md`
  only. Do not modify the renderer, tracker code, templates, CI workflows, build
  scripts, publication pipeline, or other functioning project code merely to
  force an agent to follow instructions unless the user explicitly asks for a
  product/code change.
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

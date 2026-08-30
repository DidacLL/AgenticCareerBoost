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
- `agents/cv/` and `site/` may contain intentionally public personal proof
  material, including the general CV and portfolio site assets.
- `agents/rules/`, `agents/tests/`, `agents/work/`, and `agents/state/` are
  preserved historical/work evidence. Do not treat old sprint notes, role files,
  tests, logs, research, backlog, or campaign scratch files as current
  instructions unless the user explicitly reactivates that scope.
- Tailored letters, raw offers, private JSON, generated private PDFs, databases,
  recruiter notes, and application-specific CV variants stay local and untracked.

## Working Rules

- Direct user instructions override repository guidance.
- Do not use staged, unstaged, tracked, or ignored status as semantic truth.
  Classify changes by scope before changing or staging them.
- Do not develop AAAAT or VCVGenerator in this repository cleanup.
- Do not add framework machinery, package architecture, MCP servers, app
  launchers, or policy tests without explicit approval.
- Keep documentation short, human-readable, and honest about what is public,
  private, scratch, or future work.
- Use fake examples for docs and checks.

## Checks

Use operational checks only:

- the letter renderer can produce TeX from a fake local JSON file;
- PDF compilation may be checked only when local LaTeX works;
- the public/general CV source remains present;
- staged paths must not include private JSON, `.private`, raw offers, databases,
  generated private PDFs, recruiter notes, or tailored application material.

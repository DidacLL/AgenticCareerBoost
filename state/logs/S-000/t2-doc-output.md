# Documentation output

## Meta

- **Artifact ref**: S-000 / T2
- **Date**: 2026-04-19

## Rationale (why)

The Agentic OS bootstrap (Sprint S-000) created a complete multiagent
operating system inside a Git repository, but produced no formal documentation
of its architecture, rationale, or implementation. This retro-documentation
closes the gap, making the system inspectable by both recruiters and
engineering peers without requiring them to read every Markdown file.

## Mechanism (what)

A single master LaTeX document (`content/reports/tex/sprints/s000-agentic-os-bootstrap.tex`)
covering 12 chapters: preface, architectural overview, truth hierarchy,
canonical truth (6 core files), workflow contracts (5 workflows), agent roles
(6 roles), output templates (4 templates), state machinery, public surfaces,
CI/CD automation, lessons and invariants, and a file manifest appendix.

Built on a shared LaTeX2e preamble (`preamble/agenticboost.sty`) with
crash-proof image inclusion, reusable TikZ diagram styles, and project-specific
macros — all reusable by every future sprint document.

## Diagrams

- `fig:routing-map` — Repository routing map (TikZ, inline)
- `fig:agent-interaction` — Agent interaction graph during sprint (TikZ, inline)
- `fig:state-lifecycle` — State file lifecycle (TikZ, inline)
- 3 screenshot placeholders for user-supplied images

## Formal document

- `content/reports/tex/sprints/s000-agentic-os-bootstrap.pdf` (built via `latex-build.yml`)

## Public-narrative hook

A complete engineering case study of a path-based multiagent OS — built from
scratch in one sprint, documented in LaTeX with architecture diagrams, and
publicly inspectable on GitHub.

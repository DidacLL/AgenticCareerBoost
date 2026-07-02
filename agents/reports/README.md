# agents/reports/

Formal engineering documentation in LaTeX.

This folder is for the published documentation side of the repo. The quick
human orientation layer stays in the root `README.md`, while this area holds
the formal PDFs and their source tree.

## What belongs where

- [README quick overview](../../README.md) - the shortest human entrypoint for
  mission, status, and navigation.
- [Human guide/manual](../../site/files/reports/agentic-system-guide.pdf) - the formal human-facing
  guide. Use this when you want the operating model explained without reading
  every contract file first.
- [S-000 case study](../../site/files/reports/s000-agentic-os-bootstrap.pdf) - the formal sprint
  report. Use this when you want the evidence-backed technical account of the
  bootstrap sprint.

## Build notes

- Catalan is permitted per `agents/rules/core/brand.md` language policy.
- Build with TeX Live from `agents/reports/tex/`.
- Local build output lands in `agents/reports/tex/build/` and stays ignored.
- Published PDFs live under `site/files/reports/` or `site/files/cv/`.
- Source template: [`agents/rules/templates/documentation-output.md`](../rules/templates/documentation-output.md)

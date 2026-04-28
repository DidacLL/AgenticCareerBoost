# content/reports/

Formal engineering documentation in LaTeX.

This folder is for the published documentation side of the repo. The quick
human orientation layer stays in the root `README.md`, while this area holds
the formal PDFs and their source tree.

## What belongs where

- [README quick overview](../../README.md) - the shortest human entrypoint for
  mission, status, and navigation.
- [Human guide/manual](build/agentic-system-guide.pdf) - the formal human-facing
  guide. Use this when you want the operating model explained without reading
  every contract file first.
- [S-000 case study](build/s000-agentic-os-bootstrap.pdf) - the formal sprint
  report. Use this when you want the evidence-backed technical account of the
  bootstrap sprint.

## Build notes

- Catalan is permitted per `docs/core/brand.md` language policy.
- Build with TeX Live through the scripts in `content/reports/tex/`.
- Local build output lands in `content/reports/tex/build/` and stays ignored.
- PRs refresh `content/reports/build/`, the only tracked PDF publication
  folder, while CI uploads the compiled PDFs as artifacts and excludes the
  smoke test from publication.
- Source template: [`docs/templates/documentation-output.md`](../../docs/templates/documentation-output.md)

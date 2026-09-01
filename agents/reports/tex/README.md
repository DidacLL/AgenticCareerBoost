# LaTeX reports — repository evidence

The documents in this tree are ACB report sources and historical technical
evidence. They are not portfolio content and the Astro site does not depend on
their PDFs.

## Build

Prerequisites: `pdflatex`; `latexmk` is optional.

Windows:

```powershell
cd agents/reports/tex
.\build-local.ps1
.\build-local.ps1 -Target s000
.\build-local.ps1 -Target guide
.\build-local.ps1 -Target smoke
.\build-local.ps1 -Target clean
```

Linux/macOS:

```bash
cd agents/reports/tex
./build-local.sh
./build-local.sh s000
./build-local.sh guide
./build-local.sh smoke
./build-local.sh clean
```

All local PDFs remain under `agents/reports/tex/build/`, which is ignored. The
dedicated `latex-build.yml` workflow compiles report sources and uploads its PDF
bundle as a GitHub Actions artifact. Neither local report builds nor CI copy
reports into `site/`.

## Structure

- `preamble/` — shared report style/macros/safe image helpers.
- `sprints/` — historical technical case-study documents.
- `guides/` — standalone project guides/history documents.
- `figures/` — report figures and source assets.
- `build/` — generated local/CI output, never portfolio source.

CV and cover-letter sources live in `agents/cv/`, not in this report tree.

## Interpretation

Report names that use sprint/agentic-system terminology describe the historical
project period in which they were written. They are evidence of the repository's
evolution, not instructions to reactivate the old harness.

## Rules

- Keep generated PDFs and LaTeX auxiliary files out of source directories.
- Preserve useful report sources/history unless the user explicitly scopes a
  documentation cleanup.
- Do not publish reports through the portfolio merely because they are public
  repository evidence.
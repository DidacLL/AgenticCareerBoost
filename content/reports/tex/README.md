# LaTeX reports — build instructions
<!-- CI: workflow_dispatch also available for manual re-runs -->

## Prerequisites

- TeX Live (full or custom with packages listed in `preamble/agenticboost.sty`)
- `pdflatex` is required
- `latexmk` is optional; local scripts fall back to `pdflatex` when it is not available

## Local build (verify before committing)

These scripts mirror the CI pipeline closely. Always run locally before pushing
to catch errors early.

**Windows (PowerShell):**

```powershell
cd content/reports/tex
.\build-local.ps1              # build all report documents
.\build-local.ps1 -Target s000 # Sprint S-000 only
.\build-local.ps1 -Target guide # Agentic system guide only
.\build-local.ps1 -Target smoke # preamble smoke test
.\build-local.ps1 -Target clean # remove build artifacts
```

**Linux / macOS (bash):**

```bash
cd content/reports/tex
./build-local.sh          # build all report documents
./build-local.sh s000     # Sprint S-000 only
./build-local.sh guide    # Agentic system guide only
./build-local.sh smoke    # preamble smoke test
./build-local.sh clean    # remove build artifacts
```

**Makefile (Unix only):**

```bash
make s000    # build Sprint S-000 document
make guide   # build the human-facing system guide
make smoke   # build the 1-page smoke test
make clean   # remove build artifacts
```

Local output lands in `build/`.

On pushes that update `content/reports/tex/`, `.github/workflows/latex-build.yml`
refreshes `content/reports/build/`, copies the published PDFs into it, and
commits them so the latest guide and report documents are visible in the
repository without opening a workflow run. The smoke test still compiles in CI
but is not promoted as a public artifact.

## Architecture

- `preamble/agenticboost.sty` — shared style; every document loads this.
- `preamble/macros.tex` — project macros (`\pathref`, `\role`, `\agent`, etc.).
- `preamble/safeimg.tex` — crash-proof image inclusion (`\screenshotfig`).
- `preamble/tikzlib.tex` — TikZ libraries and reusable diagram styles.
- `sprints/` — technical case-study documents tied to a sprint.
- `guides/` — standalone human-facing guide documents.
- `figures/` — TikZ sources and external assets.

## Document families

- `guides/agentic-system-guide.tex` — the formal human-facing manual for how to
  read and use the system.
- `sprints/s000-agentic-os-bootstrap.tex` — the bootstrap case study and
  evidence trail.

## Rules

- **Never use `\includegraphics` directly.** Use `\screenshotfig` or `\safeincludegraphics`.
- **Any recurring macro must be promoted to the shared preamble.**
- **Each sprint document is self-contained** (single PDF, single `.tex` entry point).

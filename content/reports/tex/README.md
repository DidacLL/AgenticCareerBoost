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

CI compiles the report sources and uploads the PDF bundle as an artifact. Public
PDFs in `content/reports/build/` are updated by the same PR that changes their
sources, so protected `main` never needs a bot auto-commit. The smoke test
compiles in CI but is not promoted as a public artifact. Generated PDFs and
auxiliary files must not be tracked inside `content/reports/tex/`.

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
- `guides/didac-llorens-cv.tex` — the public downloadable CV source.
- `sprints/s000-agentic-os-bootstrap.tex` — the bootstrap case study and
  evidence trail.
- `sprints/s001-profile-audit-positioning.tex` — profile audit and positioning.
- `sprints/s0015r-system-review.tex` — corrective system-review report.

## Rules

- **Never use `\includegraphics` directly.** Use `\screenshotfig` or `\safeincludegraphics`.
- **Any recurring macro must be promoted to the shared preamble.**
- **Each sprint document is self-contained** (single PDF, single `.tex` entry point).
- **Only `content/reports/build/` stores tracked PDFs.** Source folders stay
  source-only.

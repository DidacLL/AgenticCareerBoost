# LaTeX reports — build instructions
<!-- CI: workflow_dispatch also available for manual re-runs -->

## Prerequisites

- TeX Live (full or custom with packages listed in `preamble/agenticboost.sty`)
- `latexmk` (ships with TeX Live)

## Local build (verify before committing)

These scripts mirror the CI pipeline (`.github/workflows/latex-build.yml`)
exactly. Always run locally before pushing to catch errors early.

**Windows (PowerShell):**

```powershell
cd content/reports/tex
.\build-local.ps1              # build all sprint documents
.\build-local.ps1 -Target s000 # Sprint S-000 only
.\build-local.ps1 -Target smoke # preamble smoke test
.\build-local.ps1 -Target clean # remove build artifacts
```

**Linux / macOS (bash):**

```bash
cd content/reports/tex
./build-local.sh          # build all sprint documents
./build-local.sh s000     # Sprint S-000 only
./build-local.sh smoke    # preamble smoke test
./build-local.sh clean    # remove build artifacts
```

**Makefile (Unix only):**

```bash
make s000    # build Sprint S-000 document
make smoke   # build the 1-page smoke test
make clean   # remove build artifacts
```

Output lands in `build/`.

## Architecture

- `preamble/agenticboost.sty` — shared style; every document loads this.
- `preamble/macros.tex` — project macros (`\pathref`, `\role`, `\agent`, etc.).
- `preamble/safeimg.tex` — crash-proof image inclusion (`\screenshotfig`).
- `preamble/tikzlib.tex` — TikZ libraries and reusable diagram styles.
- `sprints/` — one master `.tex` per sprint.
- `figures/` — TikZ sources and external assets.

## Rules

- **Never use `\includegraphics` directly.** Use `\screenshotfig` or `\safeincludegraphics`.
- **Any recurring macro must be promoted to the shared preamble.**
- **Each sprint document is self-contained** (single PDF, single `.tex` entry point).

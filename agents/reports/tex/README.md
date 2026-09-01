# LaTeX reports — build instructions
<!-- CI: workflow_dispatch also available for manual re-runs -->

These documents are ACB report sources and historical technical evidence. They remain inspectable in the repository, but they are not portfolio content and the Astro site does not depend on their PDFs.

## Prerequisites

- TeX Live (full or custom with packages listed in `preamble/agenticboost.sty`)
- `pdflatex` is required
- `latexmk` is optional; local scripts fall back to `pdflatex` when it is not available

## Local build

The scripts mirror the dedicated report CI pipeline closely.

**Windows (PowerShell):**

```powershell
cd agents/reports/tex
.\build-local.ps1
.\build-local.ps1 -Target s000
.\build-local.ps1 -Target guide
.\build-local.ps1 -Target smoke
.\build-local.ps1 -Target clean
```

**Linux / macOS (bash):**

```bash
cd agents/reports/tex
./build-local.sh
./build-local.sh s000
./build-local.sh guide
./build-local.sh smoke
./build-local.sh clean
```

**Makefile (Unix only):**

```bash
make s000
make guide
make smoke
make clean
```

Local output lands in `build/`. The dedicated `latex-build.yml` workflow compiles the same sources and uploads its PDF bundle as a GitHub Actions artifact. Neither local report builds nor report CI copy PDFs into `site/`; generated report PDFs are repository build output rather than portfolio assets.

## Architecture

- `preamble/agenticboost.sty` — shared style; every document loads this.
- `preamble/macros.tex` — project macros (`\pathref`, `\role`, `\agent`, etc.).
- `preamble/safeimg.tex` — crash-proof image inclusion (`\screenshotfig`).
- `preamble/tikzlib.tex` — TikZ libraries and reusable diagram styles.
- `sprints/` — technical case-study documents tied to a sprint.
- `guides/` — standalone human-facing guide documents.
- `figures/` — TikZ sources and external assets.
- `build/` — generated local/CI output, never portfolio source.

CV and cover-letter sources live in `agents/cv/`, not in this report tree.

## Document families

- `guides/agenticcareerboost-project-history.tex` — public narrative bridge and documentation coverage map for the project history.
- `guides/agentic-system-guide.tex` — formal human-facing manual for reading the historical system.
- `sprints/agentic-system-evidence-reconciliation.tex` — local-vs-remote reconciliation, evidence classification, drift fixes, and validation ledger.
- `sprints/agentic-system-refactor-retrospective.tex` — refactor failure analysis and cleanup architecture retrospective.
- `sprints/s000-agentic-os-bootstrap.tex` — bootstrap case study and evidence trail.
- `sprints/s001-profile-audit-positioning.tex` — profile audit and positioning.
- `sprints/s0015r-system-review.tex` — corrective system-review report.
- `sprints/s002-restart-refresh.tex` — restart review, static-site foundation, GitHub/LinkedIn human gates, and repo-local closure.
- `sprints/s003-website-os-clarity.tex` — public route-map and website clarity report.
- `sprints/s004-documentation-alignment.tex` — career guardrail and relaunch calibration report.
- `sprints/s0045-site-quality.tex` — historical site-quality/runtime/browser-validation report.

These names describe the period in which the reports were written. They are repository evidence, not instructions to reactivate the old harness.

## Rules

- Never use `\includegraphics` directly; use `\screenshotfig` or `\safeincludegraphics`.
- Any recurring macro belongs in the shared preamble.
- Each sprint document is self-contained with one `.tex` entry point.
- Keep generated PDFs and LaTeX auxiliary files out of source directories.
- Preserve useful report sources/history unless documentation cleanup is explicitly scoped.
- Do not publish reports through the portfolio merely because they are public repository evidence.

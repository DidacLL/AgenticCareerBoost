# CI/CD evidence — T3 LaTeX build

## Artifact

- **Workflow file**: `.github/workflows/latex-build.yml`
- **Action**: `xu-cheng/latex-action@v3` (TeX Live full, free/OSS)
- **Trigger**: push to main + PR on `content/reports/tex/**`
- **Output**: PDF artifacts uploaded with 30-day retention

## Tool policy update

- Added `latexmk` and `xu-cheng/latex-action` to `docs/core/tool-policy.md`
- Both are free/OSS, no vendor lock-in

## Backlog closure

- T-003 ("Set up LaTeX build toolchain") — resolved by this task
- CI does not commit back or deploy to Pages; publication remains user-gated

## Verification

- CI green status to be confirmed on first push to main containing `content/reports/tex/`
- Actions run URL: _(pending first push)_

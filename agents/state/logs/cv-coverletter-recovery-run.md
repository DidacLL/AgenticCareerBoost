# CV / cover-letter recovery run

## Scope

- Execution mode: `implementation`.
- Workflow: bounded recovery/hardening run; does not consume S-005.
- Purpose: recover the better CV and cover-letter build path after the
  AgenticSystem refactor, adapt it to the current `agents/` architecture, and
  make public career PDFs deploy-generated instead of committed source files.

## Source evidence

- The destructive breakpoint was the AgenticSystem refactor commit that renamed
  `assets/curriculum/DidacLL_SoftwareEngineer_CV.tex` into
  `agents/reports/tex/guides/DidacLL_SoftwareEngineer_CV.site-legacy.tex`,
  added a simpler `agents/reports/tex/guides/didac-llorens-cv.tex`, and deleted
  `assets/curriculum/DidacLL_Assaia_CoverLetter.tex`.
- The safer recovered CV candidate was the `site-legacy` file: it retained the
  banner, compact layout, XMP/PDF metadata, custom PDF info fields, and a
  visible parser summary.
- The deleted Assaia letter was a useful design/content reference, but not a
  reusable template. It also contained hidden white parser text and was therefore
  not restored verbatim.

## Deepsearch triage

Fixed in this run:

- CV/source mismatch between public site links and canonical source.
- CV and public-safe cover-letter PDF deploy freshness.
- CV artifact reproducibility and onboarding under `agents/cv/`.
- Validation for old curriculum roots, hidden parser text, generated PDF
  tracking, canonical source links, and CV family completeness.

Verified as stale or already handled:

- `required-ci` already runs `python -m pytest agents/tests -q`.
- Deployment-base routing hardcoding is handled by the site-routing hotfix.

Delayed:

- GitHub Action SHA pinning.
- Global Python manifest/lock strategy.
- Frontend HTML injection sink cleanup.
- Automated browser smoke test suite.
- `components.js` modular split.
- `export_status.py` structured-data migration.
- Report PDF untracking/regeneration.
- External link linting policy.
- Broader media/PDF licensing clarification.

## Implementation summary

- Created `agents/cv/` as the canonical career artifact source family.
- Promoted the recovered CV into `agents/cv/tex/didac-llorens-cv.tex`.
- Added `agents/cv/tex/cover-letter-template.tex`.
- Added deterministic stdlib rendering via
  `agents/cv/tools/render-cover-letter.py`.
- Added public-safe example data at `agents/cv/data/examples/assaia.json`.
- Added local build scripts for Windows and Unix.
- Updated required CI and Pages deploy to generate career PDFs before static
  site validation.
- Updated public site source links to the canonical `agents/cv` CV source.
- Ignored generated CV and cover-letter PDFs while leaving report PDFs tracked.

## Closure matrix

| Gate | Status | Notes |
|---|---|---|
| Source recovery | Pending validation | Canonical CV moved to `agents/cv/tex/`. |
| Cover-letter renderer | Pending validation | Public example renders only when `publish: true`. |
| Deploy freshness | Pending validation | Workflows build PDFs before site validation/upload. |
| Static validation | Pending | `validate_static_site.py` must pass after build. |
| Pytest | Pending | `agents/tests` must pass. |
| PairCheck A | Pending | LaTeX/content public-safety review. |
| PairCheck B | Pending | CI/artifact/validation review. |


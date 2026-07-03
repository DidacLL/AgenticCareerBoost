# CV/Cover-Letter Artifact Integration Repair

## Scope

This ledger records the corrected repository-local contract for the CV and
cover-letter artifact pipeline.

- Current `agents/cv/tex/*.tex` files are user-authored source and are not
  modified by this repair.
- `agents/cv/artifacts.json` is the build and deployment contract.
- Local scripts and CI compile the manifest-declared artifacts and copy PDFs to
  `site/files/**`.
- Validation checks integration, ignored generated outputs, site links, and
  deployment-base-safe file handling.

## Closure Matrix

| Area | Status | Evidence |
|------|--------|----------|
| Source ownership | Done | LaTeX files are inputs, not CI-managed content. |
| Build integration | Done | Local scripts and workflows consume `artifacts.json`. |
| Site file links | Done | PDF/file hrefs resolve as static assets and open outside SPA navigation. |
| Validation shape | Done | Tests use manifest contracts instead of fixed artifact names. |
| S-005 | Unchanged | This run does not consume the next campaign sprint. |

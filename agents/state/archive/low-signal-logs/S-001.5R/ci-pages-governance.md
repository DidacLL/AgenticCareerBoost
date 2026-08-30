# S-001.5R CI/Pages governance evidence

## Local workflow changes

- Added `.github/workflows/required-ci.yml` with one stable aggregate required
  status named `required-ci`.
- The aggregate covers pytest, markdownlint, internal links, exported status,
  Jekyll site build, and LaTeX smoke/report compilation.
- Changed `.github/workflows/site-build.yml` from `gh-pages` branch commits to
  GitHub Pages Actions that build Jekyll from `site/` and upload `site/_site`.

## Required remote settings

These settings require repository administration rights. They were not applied
from this workspace because `gh` is not installed in the local shell and the
available GitHub connector does not expose repository ruleset or Pages-source
mutation tools:

1. Repository Settings -> Pages -> Build and deployment -> Source: `GitHub
   Actions`.
2. Branch protection or repository ruleset for `main` -> Require status checks
   before merging -> required check: `required-ci`.
3. Remove any previously required fragmented checks from the required-checks
   list, including `markdownlint`, `Check internal links (critical)`, and
   `Build LaTeX reports / build`, after the new `required-ci` workflow has run
   at least once on the default branch.

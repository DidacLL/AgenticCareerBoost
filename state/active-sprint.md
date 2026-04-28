# Sprint output

## Meta

- **Sprint ID**: S-001.5R
- **Goal**: Correct S-001.5 governance, architecture, documentation, Pages, and public-copy drift before S-002.
- **Status**: implemented locally / PR validation and remote settings pending

## Tasks

| # | Task | Target | Specialty | Scope | Writes | Acceptance | Memory | Evidence link |
|---|------|--------|-----------|-------|--------|------------|--------|---------------|
| 1 | ContentSync system audit | ContentSync | System consistency | Duplicate paths, stale refs, generated artifacts, social coupling | `state/logs/S-001.5R/content-sync.md` | Findings mapped to concrete fixes or accepted historical notes | `state/memory/review/` | `state/logs/S-001.5R/content-sync.md` |
| 2 | Repo architecture migration | Developer | System architecture | Site roots, report publication paths, tests, README refs | `site/**`, `content/reports/**`, tests, README/state refs | `site/` is canonical; source folders no longer track generated report artifacts | none | `site/README.md` |
| 3 | CI, Pages, branch protection evidence | CI/CD | Governance | Actions workflows and remote setting evidence | `.github/workflows/**`, `state/logs/S-001.5R/ci-pages-governance.md` | `required-ci` exists; Pages deploy builds `site/`; remote settings listed | none | `state/logs/S-001.5R/ci-pages-governance.md` |
| 4 | Sprint/social workflow decoupling | Developer | Workflow contracts | Marketing, sprint workflow, sprint template, tests | `docs/core/marketing.md`, `docs/workflows/sprint.md`, `docs/templates/sprint-output.md`, tests | Internal sprints can close with a public-narrative decision instead of forced social content | none | `docs/core/marketing.md` |
| 5 | Public tone and campaign repair | CommunityManager | Public content | Social plan and drafts, site/CV public copy | `content/social/**`, `site/**`, CV source | No public TODO/user-instruction wording; campaign order follows evidence, not sprint numbering | `state/memory/social/` | `content/social/plan.md` |
| 6 | Formal human documentation | Documentation | Report | S-001.5R report and missing S-001.5 explanation | `content/reports/tex/sprints/s0015r-system-review.tex`, `state/logs/S-001.5R/documentation-output.md` | Human can understand S-001.5 outputs, flaws, corrections, and next steps from the report | none | `content/reports/tex/sprints/s0015r-system-review.tex` |
| 7 | Independent review | PairCheck | System review | Changed architecture, CI, docs, public copy | `state/logs/S-001.5R/pc-*.md` | Fresh reviews record pass/partial/fail and residual risks | none | `state/logs/S-001.5R/` |
| 8 | Closure integration | Orchestrator + CI/CD | Status | Sprint state, roadmap, backlog, public status | `state/**`, `data/public-status.json` | Local implementation recorded; closure remains pending until PR `required-ci` and Pages deploy prove green | none | `state/current.md` |

## Pair-check assignments

| Task # | PairCheck-A | PairCheck-B | Verdict |
|--------|-------------|-------------|---------|
| 2, 4 | PairCheck-A | PairCheck-B | PARTIAL findings remediated locally; remote closure still pending |
| 3 | PairCheck-A | PairCheck-B | PARTIAL findings remediated locally; remote settings still pending |
| 5, 6 | PairCheck-A | PairCheck-B | PARTIAL findings remediated locally |

## Closure artifacts

- [x] Repository artifact(s) — canonical `site/`, workflow updates, report-source cleanup, contract updates
- [ ] Website / repo update trace — Pages workflow now builds Jekyll from `site/`; remote Pages deploy evidence pending
- [x] Public-narrative decision — campaign remains evidence-gated; system-review social output deferred until public surfaces are synced
- [x] Formal engineering documentation — S-001.5R report source added
- [x] Condensed technical backlog — branch protection and Pages remote settings remain explicit pending actions
- [x] Condensed narrative backlog — campaign sequencing decoupled from sprint numbering

## Backlog deltas

### Technical

- T-011 UPDATE: Replace `gh-pages` branch deployment with GitHub Pages Actions from `site/`; set Pages source to GitHub Actions after merge.
- T-012 NEW: Enable `main` ruleset/branch protection requiring PRs and the aggregate `required-ci` check.
- T-013 NEW: S-002 must build on the canonical `site/` root and avoid reintroducing rendered-source duplicates.

### Narrative

- N-016 NEW: Treat S-001.5R as a governance-proof candidate only after the PR, Pages deploy, and report PDF exist.
- N-017 NEW: Keep campaign order evidence-gated instead of sprint-number-gated.

## CI trace

- Local tests: pytest PASS; internal links PASS; markdownlint PASS; workflow YAML parse PASS; `.gitignore` dotted-name audit PASS; LaTeX all-doc build PASS via PowerShell fallback
- Local build limits: Jekyll not run locally because Ruby/Bundler is unavailable; direct `latexmk` unavailable because MiKTeX lacks Perl, but the repo fallback built all PDFs with `pdflatex`
- Workflow run: pending PR

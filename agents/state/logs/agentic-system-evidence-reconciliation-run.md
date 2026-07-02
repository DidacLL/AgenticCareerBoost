# AgenticSystem evidence reconciliation run

- **Date**: 2026-07-02
- **Type**: AgenticSystem system-review/documentation reconciliation
- **Sprint ID**: none
- **S-005 status**: untouched; remains next LinkedIn campaign kickoff seed

## Summary

Reconciled the post-refactor local review findings with the repository's formal
evidence set. The run fixed live drift, documented intentional draft deletion,
added a human-facing LaTeX report, and linked the new public PDF from the report
indexes and AgenticCareerBoost project page.

## Findings repaired

- `agents/rules/core/ci-rules.md` still described old docs-lint and Lychee
  config paths. It now matches the current blocking `required-ci` internal-link
  check and advisory `.github/lychee.toml` external-link check.
- `site/content/projects.json` still said `public-status.json`; it now says
  `status.json`.
- `agents/reports/tex/Makefile` still named the old `content/reports/tex/`
  root; it now names `agents/reports/tex/`.
- Browser validation exposed a clean-route runtime issue: deep routes loaded the
  shell without rendering because root shell assets were relative and the router
  only derived routes from hashes. Root shell assets are now root-absolute and
  the router supports direct pathname loads plus pushState navigation.
- Guard tests now cover stale public-status wording, stale CI config docs, and
  old report-root comments, plus direct clean-route shell support.

## Evidence and draft policy

- Formal reports, report sources, state logs, summaries, and research remain
  durable evidence.
- Discarded social/profile draft bodies remain intentionally deleted. They were
  candidate outputs, not retained evidence, approved copy, or future steering
  rules.
- The new report records this distinction explicitly:
  `agents/reports/tex/sprints/agentic-system-evidence-reconciliation.tex`.

## Public artifacts

- New source:
  `agents/reports/tex/sprints/agentic-system-evidence-reconciliation.tex`.
- New public PDF:
  `site/files/reports/agentic-system-evidence-reconciliation.pdf`.
- Public indexes updated:
  `README.md`, `agents/reports/tex/README.md`,
  `site/files/reports/README.md`, and `site/content/projects.json`.
- Runtime route support updated:
  `index.html`, `site/assets/js/os.js`, and `site/assets/js/router.js`.

## Tooling failures and friction recorded

- Sandboxed read-only PowerShell/Git inspection failed repeatedly during the
  review; elevated read-only commands were required.
- Escalated PowerShell did not have `git` on `PATH`; read-only Git inspection
  used `C:/Program Files/Git/cmd/git.exe`.
- Local `latexmk` was unavailable; the report build used the repository's
  three-pass `pdflatex` fallback.

## Validation

- `python agents/tools/export_status.py` passed.
- `python agents/tools/validate_static_site.py` passed.
- `bash agents/tools/validate_links.sh` passed.
- `python -m pytest agents/tests -q` passed.
- `agents/reports/tex/build-local.ps1 -Target all` passed.
- Browser/public sanity check passed for `/`,
  `/projects/agentic-career-boost`, `/dashboard`, and `/cv/ml`; no console
  errors or broken images were observed, and the new report link was visible.

## PairCheck verdict

PASS. Rules, state, public copy, report indexes, and formal report evidence now
agree: this is a traceable agentic development record, not only a polished
prompt. No sprint was consumed, no discarded draft bodies were restored, and no
new architecture folder was introduced.

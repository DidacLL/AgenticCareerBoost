# AgenticSystem alignment and evidence safety run

- **Date**: 2026-07-02
- **Type**: AgenticSystem refactor/alignment run
- **Sprint ID**: none
- **S-005 status**: untouched; remains next LinkedIn campaign kickoff seed

## Summary

Audited the post-structure-refactor diff against the intended directory model
and repaired the remaining authority/evidence drift. The run kept the structure
simple: rules remain under `agents/rules/`, evidence under `agents/state/`,
public runtime under `site/`, and root limited to platform entrypoints.

## Findings and repairs

- Root `.gitignore` had broad LaTeX patterns, including `*.[1-9]R`, that hid
  `agents/state/logs/S-001.5R/**` from Git. The root ignore file now covers
  only repo-wide noise and generated site status; TeX ignores live beside TeX
  sources.
- `agents/state/current.md` recorded the structure simplification closure as
  `2026-07-01`; it now matches the `2026-07-02` run ledger.
- `site/README.md` still pointed published reports to the old
  `content/reports/build/` path; it now points to `site/files/reports/` and
  `site/files/cv/`.
- Some workflow/role wording still treated `agents/state/active-sprint.md` as
  a task contract source. It is now a status marker and optional pointer only;
  current sprint contracts come from direct user-approved plans.
- Contract tests now cover ignored state evidence, risky root ignore patterns,
  and active-sprint non-authority wording.

## PairCheck verdict

PASS. The final rule shape matches the truth hierarchy: `agents/rules/**`
defines behavior, `agents/state/**` records evidence/status, and historical
evidence may be read for context but cannot override rules or direct user
scope. No sprint was consumed, no deleted drafts/style-book material was
restored, and no manual public-status mirror was introduced.

## Validation

- Ignored-file scan shows no ignored files under `agents/state/**`.
- Live stale-path scan found no active references to deleted poisoned sources
  or old rule roots outside intentional tests/historical evidence.
- `python agents/tools/export_status.py` passed and regenerated
  `site/data/status.json` with `last_closure_at: 2026-07-02`.
- `python agents/tools/validate_static_site.py` passed.
- `bash agents/tools/validate_links.sh` passed for 44 internal Markdown links.
- `python -m pytest agents/tests -q` passed: 10 tests.
- `git check-ignore` returned no matches for the previously hidden
  `agents/state/logs/S-001.5R/**` evidence files.

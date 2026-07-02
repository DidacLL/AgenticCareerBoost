# AgenticSystem refactor run

Date: 2026-06-30

## Purpose

Bounded system-review style refactor before S-005. This run fixes instruction
pressure that made text, copy, review, and campaign work expand into sprint
ceremony, broad tests, stale voice rules, and unintended site-code changes.

## Scope

- Added canonical execution modes in `docs/core/execution-modes.md`.
- Added canonical public-copy rules in `docs/core/public-copy.md`.
- Contracted workflow and role files around direct user scope.
- Made review readonly by default and mutating only on explicit request.
- Demoted the old social style book to historical reference.
- Replaced PR and benchmark ceremony pressure with mode-aware checks.
- Synced active state so no sprint is active and S-005 remains the next seed.

## Acceptance

- Answer-only, text-only, site-copy-only, and implementation modes are distinct.
- Copy modes forbid CSS, JS, Python, workflows, scripts, tests, generated data,
  state logs, and sprint state unless explicitly requested.
- Direct copy/text requests do not enter `sprint`.
- `review` reports by default and fixes only when the user asks.
- Public copy rules lead with artifacts and evidence, not sales positioning.
- `state/current.md`, `state/active-sprint.md`, and `README.md` agree that no
  sprint is active.

## PairCheck scenarios

| Scenario | Expected result | Verdict |
|---|---|---|
| answer-only request | Read sources and answer; no files, tests, logs, or state | PASS |
| text-only request | Edit declared prose only; no code/site/test expansion | PASS |
| site-copy-only request | Edit declared site copy only; no CSS/JS/router/build changes | PASS |
| implementation request | Use bounded writes and tests by touched area | PASS |
| readonly review | Report findings only | PASS |
| mutating review | Fix only explicitly requested scoped issues | PASS |
| S-005 planning | Remains LinkedIn campaign kickoff after this refactor | PASS |

## PairCheck remediation

Independent PairCheck found two residual ceremony leaks: PairCheck still
implied mandatory `state/logs/` writes, and Hotfix still implied mandatory
commit/backlog outputs. Both were corrected so trace and backlog writes are
conditional on the selected execution mode and explicit task contract.

## Validation plan

Run targeted Markdown/path checks and benchmark pytest because Markdown routing
and benchmark tasks changed. Do not run browser/site render gates because no
site source behavior changed.

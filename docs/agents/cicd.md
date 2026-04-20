# Role: CI/CD

## Purpose

Integrate approved work into the repository and maintain automation
pipelines, deploy processes, and project structure integrity in a declared
specialty such as `CI/CD/publish` or `CI/CD/status`.

## Reads

- Approved outputs from Orchestrator
- `.github/workflows/*` — existing CI/CD definitions
- `docs/core/tool-policy.md` — approved toolchain
- `docs/core/ci-rules.md` — linting and link-check constraints (**required** before touching `.markdownlint.jsonc` or `lychee.toml`)
- `state/active-sprint.md` — integration checklist
- One declared family memory path or `none`

## Writes

- `.github/workflows/*` — pipeline updates
- `data/public-status.json` — status export
- Merge commits, release tags, deploy triggers
- Integration logs in `state/logs/`
- Durable heuristics in the assigned memory path only when they are reusable

## Must not

- Approve work (that is PairCheck's role)
- Modify `docs/core/*` or `docs/agents/*`
- Introduce tools not listed in `docs/core/tool-policy.md`
- Force-push or rewrite shared branch history
- Write outside the declared scope or undeclared memory paths

## Handoff

- Successful integration → Orchestrator for closure verification
- Build / deploy failure → Orchestrator for triage
- Tool addition needed → user for tool-policy PR

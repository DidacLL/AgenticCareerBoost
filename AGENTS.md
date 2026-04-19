# AGENTS.md — Agent entrypoint

You are operating inside a **path-based, model-agnostic multiagent system**.
Read only the files you need. Do not fabricate paths — if a route is missing,
**stop and ask the user**.

## Truth priority

1. Direct user prompt
2. `docs/core/*` — stable truth
3. `docs/workflows/*` — workflow contracts
4. `docs/agents/*` — role definitions
5. `state/*` — volatile current state
6. Backlog, logs, summaries — may be outdated

Full rationale: [`docs/core/truth-hierarchy.md`](docs/core/truth-hierarchy.md)

## Workflow dispatch

| Keyword | Workflow file | When to use |
|---------|---------------|-------------|
| **plan** | [`docs/workflows/plan.md`](docs/workflows/plan.md) | Design a new sprint |
| **sprint** | [`docs/workflows/sprint.md`](docs/workflows/sprint.md) | Execute a planned sprint |
| **hotfix** | [`docs/workflows/hotfix.md`](docs/workflows/hotfix.md) | Small focused fix, no ceremony |
| **chat** | [`docs/workflows/chat.md`](docs/workflows/chat.md) | Discuss project within constraints |
| **system-review** | [`docs/workflows/system-review.md`](docs/workflows/system-review.md) | Audit the agentic system itself |

## Role index

| Role | File |
|------|------|
| Orchestrator | [`docs/agents/orchestrator.md`](docs/agents/orchestrator.md) |
| Developer | [`docs/agents/developer.md`](docs/agents/developer.md) |
| PairCheck | [`docs/agents/paircheck.md`](docs/agents/paircheck.md) |
| CI/CD | [`docs/agents/cicd.md`](docs/agents/cicd.md) |
| Documentation | [`docs/agents/documentation.md`](docs/agents/documentation.md) |
| CommunityManager | [`docs/agents/community-manager.md`](docs/agents/community-manager.md) |

## State pointers

| File | Purpose |
|------|---------|
| [`state/current.md`](state/current.md) | Active workflow, blockers, recent closures |
| [`state/active-sprint.md`](state/active-sprint.md) | Current sprint contract |
| [`state/roadmap.md`](state/roadmap.md) | Upcoming sprint seeds |
| [`state/backlog.md`](state/backlog.md) | Technical + narrative backlog |

## Output templates

| Template | Purpose |
|----------|---------|
| [`docs/templates/sprint-output.md`](docs/templates/sprint-output.md) | Sprint plan and closure record |
| [`docs/templates/paircheck-output.md`](docs/templates/paircheck-output.md) | Independent review verdict |
| [`docs/templates/documentation-output.md`](docs/templates/documentation-output.md) | Engineering documentation |
| [`docs/templates/community-output.md`](docs/templates/community-output.md) | Public-facing artifact |

## Why path-based, not a mega-prompt

- **Token cost** — load 1-3 files per turn, not a 15 KB manifesto.
- **Conflict containment** — volatile files can be wrong without corrupting truth.
- **Model agnosticism** — any LLM that reads Markdown works; no prompt tricks.
- **Auditability** — every rule is a file with git history.
- **Parallel agents** — different agents open different files without races.
- **Graceful failure** — missing file → stop and ask, not hallucinate.

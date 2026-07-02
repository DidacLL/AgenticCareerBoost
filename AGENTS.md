# AGENTS.md - Agent entrypoint

You are operating inside a path-based, model-agnostic multiagent system.
Read only the files you need. Do not fabricate paths. If a required route is
missing, stop and ask the user.

## Truth priority

1. Direct user prompt
2. `agents/rules/core/*` - stable truth
3. `agents/rules/workflows/*` - workflow contracts
4. `agents/rules/roles/*` - role definitions
5. `agents/state/*` - readable evidence/status only
6. Archived evidence, backlog, logs, summaries, and research - may be outdated

Full rationale: [`agents/rules/core/truth-hierarchy.md`](agents/rules/core/truth-hierarchy.md).

`agents/state/**` may be inspected for recent context, evidence, and status. It
must never define behavior rules, voice rules, acceptance criteria, or future
run scope. If state contradicts rules, the rule layer wins.

## Execution mode first

Before choosing a workflow, classify the user request using
[`agents/rules/core/execution-modes.md`](agents/rules/core/execution-modes.md).

Direct user scope controls the run. Phrases such as "answer only", "text only",
"copy only", "no code", "no tests", or "no site code" are hard negative
scopes. Do not escalate to sprint, run tests, create logs, update state, or
touch undeclared files when the selected mode forbids it.

Missing required routes still block the task. Missing optional routes do not
block answer-only or text-only work.

## Mandatory career guardrail

Before any role, employer, campaign, LinkedIn, CV, portfolio, or
market-positioning recommendation, read
[`agents/rules/core/career-direction.md`](agents/rules/core/career-direction.md).
It prevents drift into generic backend, data-quality, BI/reporting,
consulting, or AI-hype positioning.

## Workflow dispatch

| Keyword | Workflow file | When to use |
|---------|---------------|-------------|
| **plan** | [`agents/rules/workflows/plan.md`](agents/rules/workflows/plan.md) | Design a new sprint or run |
| **sprint** | [`agents/rules/workflows/sprint.md`](agents/rules/workflows/sprint.md) | Execute a populated sprint contract |
| **operate** | [`agents/rules/workflows/operate.md`](agents/rules/workflows/operate.md) | Run one bounded specialist or AutoAgent |
| **review** | [`agents/rules/workflows/review.md`](agents/rules/workflows/review.md) | Inspect by default; fix only when explicitly requested |
| **hotfix** | [`agents/rules/workflows/hotfix.md`](agents/rules/workflows/hotfix.md) | Small focused fix, no ceremony |
| **chat** | [`agents/rules/workflows/chat.md`](agents/rules/workflows/chat.md) | Discuss project within constraints |
| **system-review** | [`agents/rules/workflows/system-review.md`](agents/rules/workflows/system-review.md) | Audit or refactor the agentic system itself |

## Role index

| Role | File |
|------|------|
| Orchestrator | [`agents/rules/roles/orchestrator.md`](agents/rules/roles/orchestrator.md) |
| Developer | [`agents/rules/roles/developer.md`](agents/rules/roles/developer.md) |
| PairCheck | [`agents/rules/roles/paircheck.md`](agents/rules/roles/paircheck.md) |
| CI/CD | [`agents/rules/roles/cicd.md`](agents/rules/roles/cicd.md) |
| Documentation | [`agents/rules/roles/documentation.md`](agents/rules/roles/documentation.md) |
| CommunityManager | [`agents/rules/roles/community-manager.md`](agents/rules/roles/community-manager.md) |
| AutoAgents | [`agents/rules/roles/autoagents.md`](agents/rules/roles/autoagents.md) |

## State pointers

| File | Purpose |
|------|---------|
| [`agents/state/current.md`](agents/state/current.md) | Active workflow, blockers, recent closures |
| [`agents/state/active-sprint.md`](agents/state/active-sprint.md) | Active sprint marker or explicit no-active-sprint marker |
| [`agents/state/roadmap.md`](agents/state/roadmap.md) | Upcoming sprint seeds |
| [`agents/state/backlog.md`](agents/state/backlog.md) | Technical and narrative backlog |
| [`agents/state/memory/README.md`](agents/state/memory/README.md) | Family memory rules and paths |

## Output templates

| Template | Purpose |
|----------|---------|
| [`agents/rules/templates/sprint-output.md`](agents/rules/templates/sprint-output.md) | Sprint plan and closure record |
| [`agents/rules/templates/paircheck-output.md`](agents/rules/templates/paircheck-output.md) | Independent review verdict |
| [`agents/rules/templates/documentation-output.md`](agents/rules/templates/documentation-output.md) | Engineering documentation |
| [`agents/rules/templates/community-output.md`](agents/rules/templates/community-output.md) | Public-facing artifact |

## Directory boundaries

- `agents/` contains internal rules, evidence, reports source, tools, tests, and
  agent working material.
- `site/` contains public website runtime files, public data, downloadable
  files, and public media.
- Root contains platform entrypoints only.

## Why path-based, not a mega-prompt

- Token cost - load 1-3 files per turn, not a manifesto.
- Conflict containment - volatile evidence can be wrong without corrupting
  rules.
- Model agnosticism - any LLM that reads Markdown can participate.
- Auditability - every rule is a file with git history.
- Parallel agents - different agents open different files without races.
- Graceful failure - missing required file means stop and ask, not hallucinate.

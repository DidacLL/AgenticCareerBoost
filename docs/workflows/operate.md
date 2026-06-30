# Workflow: Operate

## Trigger

User requests a bounded non-sprint execution, correction, experiment, or
maintenance pass.

## Inputs

- The specific request or backlog item
- `docs/core/execution-modes.md` — selected mode and negative scopes
- `docs/core/constraints.md` — bounded contract fields
- `docs/core/*` — stable truth (read-only)
- One role file from `docs/agents/` or `docs/agents/autoagents.md`
- `state/current.md` — current project status
- One declared family memory path or `none`

## Steps

1. Select the execution mode from `docs/core/execution-modes.md`.
2. Write one bounded contract using `docs/core/constraints.md`.
3. Dispatch exactly one named role or AutoAgent.
4. Execute within the declared scope and writes only.
5. Update memory only with durable heuristics that help future runs.
6. If the work expands beyond the selected mode, stop and ask or re-plan. Do
   not silently escalate copy or answer work into a sprint.

## Outputs

- One bounded artifact or correction
- Optional backlog / state delta
- Optional durable memory note

## Exit criteria

- One target completed the work.
- Writes stayed inside the declared scope.
- Any escalation reason is explicit.

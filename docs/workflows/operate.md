# Workflow: Operate

## Trigger

User requests a bounded non-sprint execution, correction, experiment, or
maintenance pass.

## Inputs

- The specific request or backlog item
- `docs/core/*` — stable truth (read-only)
- One role file from `docs/agents/` or `docs/agents/autoagents.md`
- `state/current.md` — current project status
- One declared family memory path or `none`

## Steps

1. Write one contract with target, specialty, scope, writes, acceptance, and
   memory path or `none`.
2. Dispatch exactly one named role or AutoAgent.
3. Execute within the declared scope and writes only.
4. Update memory only with durable heuristics that help future runs.
5. If the work expands to multiple concerns, roles, or artifacts → escalate to
   `sprint`.

## Outputs

- One bounded artifact or correction
- Optional backlog / state delta
- Optional durable memory note

## Exit criteria

- One target completed the work.
- Writes stayed inside the declared scope.
- Any escalation reason is explicit.

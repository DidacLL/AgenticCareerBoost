# Workflow: Plan

## Trigger

User requests a new sprint plan, or the orchestrator identifies the need.

## Inputs

- `agents/rules/core/mission.md` — scope and success criteria
- `agents/state/roadmap.md` — upcoming sprint seeds
- `agents/state/backlog.md` — open technical and narrative items
- `agents/state/current.md` — blockers and recent closures

## Steps

1. Select the next sprint seed from `agents/state/roadmap.md`.
2. Decompose into discrete tasks. Every mutating task must include:
   - target role or named AutoAgent
   - specialty
   - scope
   - writes
   - acceptance
   - memory path or `none`
3. Define pair-check requirements for non-trivial tasks.
4. Define backlog requirements (technical + narrative).
5. Fill `agents/rules/templates/sprint-output.md` with the complete plan.
6. Present the plan for direct user approval before sprint execution.
7. If the user asks to persist the plan, store it as evidence and update
   `agents/state/active-sprint.md` with status plus a pointer to that plan.
8. Update `agents/state/current.md` to reflect the new active sprint status.

## Outputs

- User-approved sprint plan, in chat or in an explicitly requested evidence file
- `agents/state/active-sprint.md` — status marker and plan pointer only
- `agents/state/current.md` — updated status

## Exit criteria

- Every mutating task has target, specialty, scope, writes, acceptance, and
  memory path or `none`.
- Pair-check assignments exist for every non-trivial task.
- The plan is achievable within one sprint cycle.

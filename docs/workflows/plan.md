# Workflow: Plan

## Trigger

User requests a new sprint plan, or the orchestrator identifies the need.

## Inputs

- `docs/core/mission.md` — scope and success criteria
- `state/roadmap.md` — upcoming sprint seeds
- `state/backlog.md` — open technical and narrative items
- `state/current.md` — blockers and recent closures

## Steps

1. Select the next sprint seed from `state/roadmap.md`.
2. Decompose into discrete tasks, each with:
   - owning role (from `docs/agents/`)
   - acceptance criteria
   - expected output artifact
3. Define pair-check requirements for non-trivial tasks.
4. Define backlog requirements (technical + narrative).
5. Fill `docs/templates/sprint-output.md` with the complete plan.
6. Copy the filled template to `state/active-sprint.md`.
7. Update `state/current.md` to reflect the new active sprint.

## Outputs

- `state/active-sprint.md` — fully populated sprint contract
- `state/current.md` — updated status

## Exit criteria

- Every task has an owning role, acceptance criteria, and expected output.
- Pair-check assignments exist for every non-trivial task.
- The plan is achievable within one sprint cycle.

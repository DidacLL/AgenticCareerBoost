# Workflow: Plan

## Trigger

Use this workflow when the user asks to design a future run, sprint, campaign,
or executable contract before execution.

## Inputs

- `agents/rules/core/run-contract.md` — scope, source, write, validation, and state model
- `agents/rules/core/mission.md` — scope and success criteria
- `agents/state/roadmap.md` — candidate sprint seeds
- `agents/state/backlog.md` — candidate technical and narrative items
- `agents/state/current.md` — compact status and blockers

Load roadmap, backlog, or historical evidence only when the run contract needs
that source family.

## Plan outputs

The Plan workflow produces one of three outputs:

1. **Candidate plan** — a proposed design. It does not change active state.
2. **Executable contract** — a user-approved plan with mode, write surface,
   validation surface, review depth, and state effect.
3. **Active sprint marker** — written only when the Sprint workflow starts
   execution.

Persisting a candidate plan is evidence capture, not sprint activation.

## Steps

1. Declare the run contract.
2. Select only the seeds or evidence needed by that contract.
3. Decompose the work into discrete tasks. Each task must include:
   - requested output
   - target role or named AutoAgent
   - write surface
   - validation surface
   - review depth
   - state effect
   - memory path or `none`
4. Define pair-check or specialist review only where the review depth requires it.
5. Fill `agents/rules/templates/sprint-output.md` only for executable contracts.
6. Present the candidate plan or executable contract for direct user approval.
7. Leave `agents/state/active-sprint.md` and `agents/state/current.md` unchanged
   unless the approved next workflow declares activation or closure.

## Outputs

- Candidate plan in chat or in an explicitly requested evidence file
- Executable contract ready for Sprint or direct execution
- No active state mutation unless activation is the declared state effect

## Exit criteria

- Every task declares requested output, write surface, validation surface, review
  depth, state effect, and memory path.
- The validation surface proves the touched surface.
- Candidate plans are distinguishable from executable contracts.
- Sprint activation is delegated to the Sprint workflow.

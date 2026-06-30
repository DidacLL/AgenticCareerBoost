# Workflow: Hotfix

## Trigger

A small, focused change is needed outside a full sprint cycle.

## Inputs

- The specific issue or request
- `docs/core/execution-modes.md` — selected mode and negative scopes
- `docs/core/constraints.md` — bounded contract fields
- `docs/core/*` — stable truth (read-only)
- `state/current.md` — current project status

## Steps

1. Select the execution mode from `docs/core/execution-modes.md`.
2. Write one bounded contract using `docs/core/constraints.md`.
3. One specialist agent executes the fix.
4. Verify only the touched area required by the selected mode.
5. Append backlog or state notes only when the mode and request require them.

## Outputs

- One focused repository change when the selected mode permits writes
- Commit only when the surrounding repository workflow asks for one
- Minimal backlog note only when the selected mode or user request requires it

## Exit criteria

- The fix is complete and does not break existing artifacts.
- The fix stayed inside the declared scope and writes list.
- Backlog note recorded when required.
- If scope expanded during execution → **escalate to Plan workflow**.

## Escalation

If the hotfix touches more than one concern or requires pair-check,
convert it to a sprint via the Plan workflow.

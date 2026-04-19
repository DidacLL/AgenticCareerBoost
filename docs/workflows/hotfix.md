# Workflow: Hotfix

## Trigger

A small, focused change is needed outside a full sprint cycle.

## Inputs

- The specific issue or request
- `docs/core/*` — stable truth (read-only)
- `state/current.md` — current project status

## Steps

1. One **Developer** agent executes the fix (narrow scope, one commit).
2. Verify the change does not violate `docs/core/*` constraints.
3. Append a minimal backlog note to `state/backlog.md`.
4. Update `state/current.md` if the fix affects project status.

## Outputs

- One focused commit with descriptive message
- Minimal backlog note in `state/backlog.md`

## Exit criteria

- The fix is committed and does not break existing artifacts.
- Backlog note recorded.
- If scope expanded during execution → **escalate to Plan workflow**.

## Escalation

If the hotfix touches more than one concern or requires pair-check,
convert it to a sprint via the Plan workflow.

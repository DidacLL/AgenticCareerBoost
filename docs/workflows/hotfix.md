# Workflow: Hotfix

## Trigger

A small, focused change is needed outside a full sprint cycle.

## Inputs

- The specific issue or request
- `docs/core/*` — stable truth (read-only)
- `state/current.md` — current project status

## Steps

1. Write one bounded contract with target, specialty, scope, writes,
   acceptance, and memory path or `none`.
2. One specialist agent executes the fix (usually **Developer**; one commit).
3. Verify the change does not violate `docs/core/*` constraints.
4. Append a minimal backlog note to `state/backlog.md`.
5. Update `state/current.md` if the fix affects project status.

## Outputs

- One focused commit with descriptive message
- Minimal backlog note in `state/backlog.md`

## Exit criteria

- The fix is committed and does not break existing artifacts.
- The fix stayed inside the declared scope and writes list.
- Backlog note recorded.
- If scope expanded during execution → **escalate to Plan workflow**.

## Escalation

If the hotfix touches more than one concern or requires pair-check,
convert it to a sprint via the Plan workflow.

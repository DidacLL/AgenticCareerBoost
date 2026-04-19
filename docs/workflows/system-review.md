# Workflow: System Review

## Trigger

Scheduled review, user request, or detected inconsistency in the agentic system.

## Inputs

- All files under `docs/` — rules, workflows, agents, templates
- `state/backlog.md` — accumulated issues
- `state/logs/` — failure reports and pair-check history
- `.github/workflows/` — CI/CD definitions

## Steps

1. Audit `docs/**` for contradictions, dead routes, and token waste.
2. Check that every path referenced in `AGENTS.md` resolves to a real file.
3. Review backlog and logs for recurring failures or friction patterns.
4. Identify any files exceeding the soft 80-line target without justification.
5. Produce an issue report with proposed changes.
6. If structure changes are needed, include migration notes.

## Outputs

- Issue report (inline or as a GitHub issue)
- Proposed diffs to `docs/**` files
- Migration notes if folder structure or routing changes

## Exit criteria

- Every finding has a concrete proposed fix or an explicit "accepted" note.
- No proposed change contradicts `docs/core/truth-hierarchy.md`.
- Report reviewed by user before any changes are applied.

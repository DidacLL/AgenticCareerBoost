# Workflow: System Review

## Trigger

Scheduled review, user request, or detected inconsistency in the agentic system.

## Inputs

- All files under `agents/rules/` — rules, workflows, roles, templates
- `agents/rules/roles/autoagents.md` — fixed routine registry
- `agents/state/backlog.md` — accumulated issues
- `agents/state/logs/` — failure reports and pair-check history
- `agents/state/memory/README.md` — family memory rules
- `.github/workflows/` — CI/CD definitions

## Steps

1. Run or inspect `ContentSync` first to locate contradictions, stale routes,
   duplicate rules, and unresolved placeholders.
2. Check that every path referenced in `AGENTS.md` resolves to a real file.
3. Review backlog, logs, and family memory for recurring friction patterns.
4. Identify any files exceeding the soft 80-line target without justification.
5. Prefer deduplication and canonical references over adding new docs.
6. Produce an issue report with proposed changes and migration notes if needed.

## Outputs

- Issue report (inline or as a GitHub issue)
- Proposed diffs to `agents/rules/**` files
- Migration notes if folder structure or routing changes

## Exit criteria

- Every finding has a concrete proposed fix or an explicit "accepted" note.
- No proposed change contradicts `agents/rules/core/truth-hierarchy.md`.
- Report reviewed by user before any changes are applied.

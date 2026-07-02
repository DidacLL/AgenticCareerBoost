# Workflow: Multiagentic Sprint

## Trigger

The user explicitly asks to execute an approved sprint plan, or
`agents/state/active-sprint.md` records `status: planned` with a pointer to a
user-approved plan.

Direct copy, text, or answer requests do not enter this workflow unless the
user explicitly asks for sprint planning or sprint execution.

## Inputs

- User-approved sprint plan — current task contracts and acceptance criteria
- `agents/state/active-sprint.md` — status marker and optional plan pointer
- `agents/rules/core/execution-modes.md` — validation limits for each task
- `agents/rules/roles/*` — role definitions for instantiated agents
- `agents/rules/roles/autoagents.md` — fixed routines when the sprint contract names one
- `agents/rules/core/constraints.md` — bounded contract fields
- `agents/rules/core/*` — stable truth (read-only during sprint)

## Steps

1. **Orchestrator** reads the approved sprint plan and decomposes it into task
   contracts using the bounded-contract fields in `agents/rules/core/constraints.md`.
   The Orchestrator is dispatcher-first; it may apply low-risk mechanical
   integration edits only when already inside the declared sprint scope.
2. **Orchestrator** delegates each task to a **separate agent instance**:
   - Implementation tasks → **Developer** agent (one task per instance)
   - Documentation tasks → **Documentation** agent
   - Narrative tasks → **CommunityManager** agent
   - Fixed maintenance tasks → named **AutoAgent** from the registry
3. Each agent executes its contract, validates according to the selected
   execution mode, and reports back to the Orchestrator with output,
   assumptions, gates, and trace path.
4. Review depth is risk-tiered:
- Trivial/mechanical or copy-only: self-check unless publication, strategy, or
  core rules change.
- Standard implementation: one fresh PairCheck or equivalent source review.
- High-risk/public/core: two fresh PairCheck agents.
5. PairCheck/source-review resolution:
   - Required reviews pass → output accepted, proceed to integration.
   - Required review returns PARTIAL/FAIL → **Orchestrator creates a new
     Developer agent** with a remediation contract containing only the
     defect list and affected file paths, unless the defect is a low-risk
     mechanical integration edit already in Orchestrator scope.
   - Remediated output repeats the declared review depth.
   - If round 2 also fails → **escalate to user**. Do not loop further.
   - Two conflicting verdicts → Orchestrator resolves by reading only
     the verdict summaries, or escalates to user if unclear.
6. **CI/CD** agent integrates accepted work into repository flow.
7. **Orchestrator** verifies the closure matrix and closes the sprint only
   when each dimension is done, deferred, waived, or not applicable.

## Agent isolation rules

- The Orchestrator keeps context narrow. It reads contracts, verdicts, status,
  and enough source to integrate safely; deeper analysis remains delegated.
- Every agent instance receives only the files it needs (context budget).
- A mutating task may read at most one declared family memory path.
- No agent instance works on more than one task contract simultaneously.
- PairCheck agents are fresh when review depth requires PairCheck.

## Trace Policy

- Prefer one compact run ledger plus specialist reports that are needed for
  handoff, review, or future audit.
- Do not create a Markdown file only to narrate obvious command output.
- Human-facing status belongs in `site/` dashboard pages or concise summaries;
  Markdown logs are primarily inter-agent memory and planning evidence.

## Human Approval Gates

Human approval is required for publication, account-owned profile changes,
private/sensitive disclosure, destructive repository actions, and unresolved
second-round review failures. Routine CI, lint, static-site, and status repairs
should proceed autonomously inside the declared scope.

## Outputs

Sprint outputs are represented by the closure matrix instead of mandatory
artifact files. Evidence can be a repository artifact, dashboard entry, report,
social decision, backlog delta, or explicit waiver.

## Closure Matrix

Each sprint closes with a matrix whose dimensions are marked `done`,
`deferred`, `waived`, or `not applicable`:

- Repository artifact(s)
- Website / repo update trace
- Public-narrative decision
- Formal engineering documentation
- Condensed technical backlog
- Condensed narrative backlog

## Exit criteria

- Each closure-matrix dimension has a state and evidence link.
- `agents/state/active-sprint.md` records the sprint as closed.
- `agents/state/current.md` updated with closure summary.
- No orphan work: every artifact connects to repo, site, or social trace.

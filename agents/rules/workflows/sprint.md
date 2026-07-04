# Workflow: Multiagentic Sprint

## Trigger

Use this workflow when the user explicitly asks to execute an approved
executable contract, or when `agents/state/active-sprint.md` records an active
planned sprint with a pointer to that contract.

Sprint starts from an executable contract, not from a candidate plan. The
contract declares write surface, validation surface, review depth, and state
effect.

## Inputs

- User-approved executable contract — current task contracts and acceptance criteria
- `agents/rules/core/run-contract.md` — scope, source, write, validation, and state model
- `agents/state/active-sprint.md` — active sprint marker and optional contract pointer
- `agents/rules/core/execution-modes.md` — mode for each task
- `agents/rules/roles/*` — role definitions for instantiated agents
- `agents/rules/roles/autoagents.md` — fixed routines when the contract names one
- `agents/rules/core/constraints.md` — bounded contract fields
- `agents/rules/core/*` — stable truth for the touched surface

## Steps

1. **Orchestrator** reads the approved executable contract and decomposes it into
   task contracts using the bounded-contract fields in
   `agents/rules/core/constraints.md` and the run contract.
2. **Orchestrator** delegates each task to a **separate agent instance**:
   - Implementation tasks → **Developer** agent (one task per instance)
   - Documentation tasks → **Documentation** agent
   - Narrative tasks → **CommunityManager** agent
   - Fixed maintenance tasks → named **AutoAgent** from the registry
3. Each agent executes its contract, validates according to the declared
   validation surface, and reports back to the Orchestrator with output,
   assumptions, gates, and trace path.
4. Review depth is risk-tiered:
   - Trivial/mechanical or isolated copy: self-check unless publication,
     strategy, or core rules change.
   - Standard implementation: one fresh PairCheck or equivalent source review.
   - High-risk/public/core: two fresh PairCheck agents.
5. PairCheck/source-review resolution:
   - Required reviews pass → output accepted, proceed to integration.
   - Required review returns PARTIAL/FAIL → **Orchestrator creates a new agent**
     with a remediation contract containing only the defect list and affected
     file paths, unless the defect is a low-risk mechanical integration edit
     already in Orchestrator scope.
   - Remediated output repeats the declared review depth.
   - If round 2 also fails → escalate to user.
   - Two conflicting verdicts → Orchestrator resolves by reading only the
     verdict summaries, or escalates to user if unclear.
6. Integration follows the validation surface declared in the run contract. Code,
   site runtime, report, CV, validator, CI, and deployment surfaces may require
   tool validation. Prose, concept, and review surfaces close through review
   evidence.
7. **Orchestrator** verifies the closure matrix and closes the sprint only when
   each dimension is done, deferred, waived, or not applicable.

## Agent isolation rules

- The Orchestrator keeps context narrow. It reads contracts, verdicts, status,
  and enough source to integrate safely; deeper analysis remains delegated.
- Every agent instance receives only the files it needs.
- A mutating task may read at most one declared family memory path.
- No agent instance works on more than one task contract simultaneously.
- PairCheck agents are fresh when review depth requires PairCheck.

## Trace policy

- Prefer one compact run ledger plus specialist reports that are needed for
  handoff, review, or future audit.
- Human-facing status belongs in `site/` dashboard pages or concise summaries;
  Markdown logs are primarily inter-agent memory and planning evidence.

## Human approval gates

Human approval is required for publication, account-owned profile changes,
private/sensitive disclosure, destructive repository actions, and unresolved
second-round review failures.

## Outputs

Sprint outputs are represented by the closure matrix instead of mandatory
artifact files. Evidence can be a repository artifact, dashboard entry, report,
social decision, backlog delta, or explicit waiver.

## Closure matrix

Each sprint closes with a matrix whose dimensions are marked `done`, `deferred`,
`waived`, or `not applicable`:

- Repository artifact(s)
- Website / repo update trace
- Public-narrative decision
- Formal engineering documentation
- Condensed technical backlog
- Condensed narrative backlog

## Exit criteria

- Each closure-matrix dimension has a state and evidence link.
- State files are updated according to the declared state effect.
- No orphan work: every artifact connects to repo, site, or social trace.

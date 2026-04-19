# Workflow: Multiagentic Sprint

## Trigger

A populated `state/active-sprint.md` exists with `status: planned`.

## Inputs

- `state/active-sprint.md` — task contracts and acceptance criteria
- `docs/agents/*` — role definitions for instantiated agents
- `docs/core/*` — stable truth (read-only during sprint)

## Steps

1. **Orchestrator** reads the sprint contract and decomposes into task
   contracts. Each contract specifies: scope, acceptance criteria, owning
   role, and input files. The Orchestrator writes contracts only — it does
   not implement.
2. **Orchestrator** delegates each task to a **separate agent instance**:
   - Implementation tasks → **Developer** agent (one task per instance)
   - Documentation tasks → **Documentation** agent
   - Narrative tasks → **CommunityManager** agent
3. Each agent executes its contract, tests where appropriate, and reports
   back to the Orchestrator with output + assumptions log.
4. **Orchestrator** sends each non-trivial output to **two fresh PairCheck**
   agents (independent reviews, no shared context).
5. PairCheck resolution:
   - Both pass → output accepted, proceed to integration.
   - One or both return PARTIAL/FAIL → **Orchestrator creates a new
     Developer agent** with a remediation contract containing only the
     defect list and affected file paths. The Orchestrator must **never
     apply fixes itself**.
   - Remediated output goes to **two fresh PairCheck agents** (round 2).
   - If round 2 also fails → **escalate to user**. Do not loop further.
   - Two conflicting verdicts → Orchestrator resolves by reading only
     the verdict summaries, or escalates to user if unclear.
6. **CI/CD** agent integrates accepted work into repository flow.
7. **Orchestrator** verifies all six closure artifacts and closes the sprint.

## Agent isolation rules

- The Orchestrator must not read full file contents for analysis. It reads
  contracts, verdicts, and status — then delegates deeper work.
- Every agent instance receives only the files it needs (context budget).
- No agent instance works on more than one task contract simultaneously.
- PairCheck agents are always fresh — no prior review history.

## Outputs (all six required for closure)

- [ ] Repository artifact(s) — committed code, configs, or docs
- [ ] Website / repo update trace — site deploy or visible repo change
- [ ] Social / LinkedIn-ready artifact — in `content/social/`
- [ ] Formal engineering documentation — in `content/reports/` or inline
- [ ] Condensed technical backlog — appended to `state/backlog.md`
- [ ] Condensed narrative backlog — appended to `state/backlog.md`

## Exit criteria

- All six closure artifacts exist or are explicitly waived in backlog.
- `state/active-sprint.md` marked `status: closed`.
- `state/current.md` updated with closure summary.
- No orphan work: every artifact connects to repo, site, or social trace.

# Workflow: Multiagentic Sprint

## Trigger

A populated `state/active-sprint.md` exists with `status: planned`.

## Inputs

- `state/active-sprint.md` — task contracts and acceptance criteria
- `docs/agents/*` — role definitions for instantiated agents
- `docs/core/*` — stable truth (read-only during sprint)

## Steps

1. **Orchestrator** reads the sprint contract and decomposes work.
2. **Orchestrator** delegates tasks to **Developer** agents (one task each).
3. Each **Developer** executes, tests where appropriate, and reports back.
4. **Orchestrator** sends each non-trivial output to **two fresh PairCheck**
   agents (independent reviews).
5. If both PairChecks pass → output accepted.
   If disagreement → escalate to Orchestrator or re-delegate to Developer.
6. **CI/CD** agent integrates accepted work into repository flow.
7. **Documentation** agent emits docs and optional formal report.
8. **CommunityManager** agent emits social/narrative artifact.
9. **Orchestrator** verifies closure artifacts and closes the sprint.

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

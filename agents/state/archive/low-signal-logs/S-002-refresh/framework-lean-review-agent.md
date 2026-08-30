# Framework lean review

## Scope

Reviewed only:

- `docs/workflows/*.md`
- `docs/agents/orchestrator.md`
- `docs/agents/autoagents.md`
- `docs/core/truth-hierarchy.md`
- `state/active-sprint.md`

No stable-doc edits applied.

## Findings

1. **Sprint ceremony is heavier than risk requires.** `sprint.md` mandates separate agent instances, two fresh PairChecks for every non-trivial output, CI/CD integration, and six closure artifacts. This is safe but turns small mixed work into file-heavy orchestration.  
   Recommended change score: **9/10**.

2. **Orchestrator rules overfit to human-style delegation.** `orchestrator.md` forbids direct artifact work and deep reading even for simple routing-adjacent fixes. This preserves isolation, but assumes multiple live agents instead of one autonomous executor with auditable phases.  
   Recommended change score: **8/10**.

3. **Review and hotfix workflows duplicate bounded-contract mechanics.** `operate.md`, `review.md`, and `hotfix.md` all restate target/scope/writes/acceptance patterns. The duplicated rule surface increases drift risk.  
   Recommended change score: **7/10**.

4. **Human escalation is used where risk gates would be enough.** PairCheck round-two failure, stable-file conflict, missing route, social publication, and account actions should still stop. But low-risk lint/content sync/remediation can proceed autonomously when scope, writes, and tests are explicit.  
   Recommended change score: **8/10**.

## Decision options

| Option | Change | Safety retained | Lean score | Recommendation |
|---|---|---:|---:|---|
| 1 | Keep current framework | Maximum isolation | 3 | Reject; preserves current verbosity |
| 2 | Add a shared `bounded-contract` rule and remove duplicated workflow text | Scope/writes/acceptance remain explicit | 7 | Good first change |
| 3 | Add risk tiers: low-risk single review or self-check; high-risk two PairChecks | PairCheck preserved for high-risk work | 9 | Recommended |
| 4 | Replace six mandatory sprint outputs with a closure matrix: `done / waived / blocked` | Explicit closure evidence remains | 8 | Recommended |
| 5 | Allow Orchestrator/executor to implement low-risk routing-adjacent fixes under declared writes | Stable truth and scope gates remain | 6 | Use cautiously |

## Verdict

Adopt options **2, 3, and 4**. They reduce document repetition, log proliferation, and assumed human-in-loop while preserving the core safety model: stable truth wins, writes are declared, high-risk work gets independent review, and real conflicts still escalate.

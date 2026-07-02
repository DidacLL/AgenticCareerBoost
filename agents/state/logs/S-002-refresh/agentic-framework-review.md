# Agentic Framework Review — 2026-06-11

## Scope

- Viewpoint: Developer/SystemReview sidecar, agentic engineering framework only.
- Output: bounded temporal report; no production docs, state contracts, site, or tests changed.
- Question: reduce verbosity, file proliferation, and human-in-loop dependency while preserving traceability.

## Evidence Read

- `AGENTS.md`: path-routed, model-agnostic entrypoint; useful orientation, not canonical.
- `docs/core/mission.md`: agentic workflow design is itself a success criterion.
- `docs/core/constraints.md`: public inspectability, model agnosticism, human-reviewed truth, token-aware brevity.
- `docs/core/truth-hierarchy.md`: direct prompt and stable docs outrank volatile logs.
- `docs/workflows/system-review.md`: system changes require report first, user review before changes.
- `docs/workflows/sprint.md`: strong traceability, but high default fan-out and six closure artifacts.
- `docs/agents/orchestrator.md`: strict dispatcher model; prevents self-fix loops but creates handoff overhead.
- `docs/agents/autoagents.md`: compact registry; good candidate for automation consolidation.
- `state/current.md`, `state/active-sprint.md`, `state/backlog.md`: S-001.5R shows closure blocked by remote/user settings even after local implementation.
- Tests/CI scan: existing checks cover path refs, workflow sections, sprint closure outputs, markdownlint, internal links, required-ci.

## Diagnosis

- The docs are not materially too long: all scanned stable framework files are under the 80-line soft target; `orchestrator.md` is 78 lines and `sprint.md` is 65.
- The real cost is artifact and agent fan-out: every non-trivial sprint output gets two fresh PairChecks, remediation creates a new Developer, and closure demands six outputs.
- Human review is rightly required for final truth and publication, but remote settings and account actions currently block closure even when repo-local evidence is complete.
- Traceability is strong but distributed across active sprint, current state, backlog, role logs, PairCheck logs, CI artifacts, and reports.

## Decision 1 — Sprint Execution Granularity

| Option | Fit | Simplicity | Risk | Evidence | Notes |
|---|---:|---:|---:|---:|---|
| Keep one-agent-per-task plus mandatory two PairChecks | 6 | 4 | 7 | 8 | Maximizes independence but scales poorly for S-002-style implementation work. |
| Add risk tiers: hotfix/light/standard/high-risk, with review depth tied to tier | 9 | 7 | 4 | 8 | Preserves traceability while avoiding full ceremony for low-risk or mechanical work. |

Selected: risk-tiered sprint contracts. Default to one implementer plus automated gates for light tasks; reserve two fresh PairChecks for high-risk changes, stable-doc changes, publication artifacts, and cross-surface changes.

## Decision 2 — Trace Storage

| Option | Fit | Simplicity | Risk | Evidence | Notes |
|---|---:|---:|---:|---:|---|
| Keep separate logs for every subagent and closure dimension | 7 | 4 | 5 | 8 | Highly auditable but increases file proliferation and reviewer load. |
| Use one temporal run ledger per sprint/review with append-only sections and links to durable artifacts | 9 | 8 | 3 | 8 | Keeps dated trace in one place and links out only when outputs are substantial. |

Selected: one run ledger per workflow under `state/logs/<id>/run.md`, with bounded subreports only for substantial specialist outputs or failed reviews.

## Decision 3 — Human-In-Loop Placement

| Option | Fit | Simplicity | Risk | Evidence | Notes |
|---|---:|---:|---:|---:|---|
| Human approval at every publication/social/remote/account-dependent checkpoint | 7 | 5 | 3 | 8 | Safe but causes stalled closure when work is otherwise locally complete. |
| Human approval only for final truth, external publication, account settings, and unresolved contradictions | 9 | 8 | 4 | 9 | Matches `Human-reviewed truth` while letting agents close repo-local work with explicit waivers. |

Selected: split closure into `repo-local closed` and `external pending`. Human remains owner of truth/publication/account settings; agents may finish local work and record pending external actions.

## Decision 4 — Orchestrator Authority

| Option | Fit | Simplicity | Risk | Evidence | Notes |
|---|---:|---:|---:|---:|---|
| Orchestrator remains pure dispatcher, never implements or remediates | 8 | 5 | 4 | 8 | Good isolation, but excessive for small routing/status repairs. |
| Orchestrator may perform bounded metadata-only edits with explicit diff and gates | 8 | 7 | 5 | 7 | Reduces subagent churn, but risks role drift if not tightly scoped. |

Selected: keep pure dispatcher for production artifacts, but allow an AutoAgent such as ContentSync to perform bounded mechanical sync. Do not give the Orchestrator general implementation authority.

## Decision 5 — Closure Artifact Model

| Option | Fit | Simplicity | Risk | Evidence | Notes |
|---|---:|---:|---:|---:|---|
| Require all six closure artifacts for every sprint | 7 | 5 | 4 | 8 | Strong campaign discipline, but overfits internal engineering sprints. |
| Keep six dimensions as a closure matrix with explicit `done/deferred/waived/not-applicable` states | 9 | 8 | 3 | 8 | Preserves no-orphan rule without forcing narrative/social output each time. |

Selected: closure matrix. Every dimension must be accounted for, but only mission-relevant dimensions need new artifacts.

## Proposed Quality Gates

- `framework-line-budget`: fail if stable framework files exceed 80 lines unless they include a short `Why longer` note.
- `routing-integrity`: keep existing AGENTS path tests and internal-link validation as blocking.
- `decision-trace`: each system-review recommendation must include at least two options, scores, and selected option.
- `risk-tier-required`: every sprint task declares `risk: light|standard|high` and review depth follows the tier.
- `closure-matrix`: sprint closure must account for repo, site, narrative, formal docs, technical backlog, narrative backlog using explicit states.
- `human-gate-boundary`: any external account action or publication must be marked `human-owned`; repo-local closure cannot depend on it unless the sprint goal requires publication.
- `subreport-budget`: a workflow may create one run ledger plus only named exception reports for high-risk, failed, or externally published outputs.
- `ci-reuse`: prefer existing pytest, markdownlint, internal links, required-ci, site build, and LaTeX gates before adding new review artifacts.

## Backlog Delta

- Add `risk` and `review_depth` fields to sprint task contracts.
- Convert sprint closure outputs from mandatory checklist to stateful closure matrix.
- Define `repo-local closed / external pending / fully closed` status vocabulary.
- Add a single-run-ledger convention for `state/logs/<id>/run.md`.
- Add tests for risk tier presence and closure matrix states after the contract changes.

## Blockers

- None for this report.
- Framework changes themselves require system-review approval before editing stable docs.

# AutoAgent Registry

Fixed routines used by `operate`, `review`, and selected sprint tasks. They are
repo-defined specialists, not new top-level human roles.

Use the smallest social review chain that protects the output.

All AutoAgents obey the sealed-context boundary in
`agents/rules/core/run-contract.md`. Private user material is never operational
input for searches, tests, validators, prompts, logs, examples, or review text.

| AutoAgent | Purpose | Reads | Writes | Trigger | Escalation | Memory |
|-----------|---------|-------|--------|---------|------------|--------|
| `ContentSync` | Fix direct consistency drift, stale status propagation, duplicate rules, unresolved placeholders, and missing path refs in scope | Scoped files, `agents/rules/core/*`, `agents/state/current.md` | Scoped consistency fixes, optional backlog note | `review`, `system-review`, explicit `operate` | Core/workflow contradictions or missing routes -> `system-review` / user | `agents/state/memory/review/` |
| `MarkdownLintChecker` | Make scoped Markdown pass current CI rules without changing lint policy | Scoped `.md` files, `agents/rules/core/ci-rules.md`, link rules | Markdown-only fixes in scope | `review`, explicit `operate` | Policy change needed -> `system-review` | `agents/state/memory/review/` |
| `LatexCompileChecker` | Compile touched LaTeX targets with the existing local scripts and fix blocking compile issues | Scoped TeX files, local build scripts, figures | Scoped LaTeX / figure-path fixes | `review`, explicit `operate` | Toolchain or broad content drift -> `system-review` / user | `agents/state/memory/review/` |
| `SocialMediaInvestigator` | Produce dated, source-disciplined research on current trends and best practices | Mission, brand, marketing, current plan, approved artifacts | Dated report in `agents/work/social/research/` | Explicit `operate`, optional scheduler outside canonical files | Weak sources or mission conflict -> user | `agents/state/memory/social/` |
| `SocialMediaPlanner` | Maintain one canonical social plan aligned with mission, style, and available proof | Mission, brand, marketing, current state, investigator reports | `agents/work/social/plan.md` | Explicit `operate`, social sprint tasks | Needs brand/channel change -> `system-review` / user | `agents/state/memory/social/` |
| `SocialConceptArchitect` | Define campaign premise, reader effect, tension, evidence map, and continuity before drafting | Mission, career direction, public-copy, social plan, approved evidence | Candidate concept architecture | Required for campaign architecture; optional for isolated post edits | Missing thesis/evidence -> user | `agents/state/memory/social/` |
| `AntiSlopContrarian` | Review concepts/drafts for generic AI/social formulas, weak tension, and unsupported claims | Candidate concept/draft, public-copy | Review verdict | Required when public campaign risk is high or user flags AI-slop risk | Persistent mismatch -> user | `agents/state/memory/social/` |
| `VoiceStakeholder` | Check fit against approved public voice constraints while preserving sealed context | Candidate concept/draft, public-copy, user-approved public voice rules | Review verdict without private examples or private-source derivatives | Required when strong personal voice is needed | Confidentiality risk -> user | `agents/state/memory/social/` |
| `SocialMediaWriter` | Draft differentiated post options only when alternatives are useful for the approved gate | Approved concept architecture or `agents/work/social/plan.md`, approved artifacts, community template | Drafts in `agents/work/social/drafts/` | Explicit `operate`, social sprint tasks after required concept/review gates | Missing evidence or stale plan -> planner / user | `agents/state/memory/social/` |

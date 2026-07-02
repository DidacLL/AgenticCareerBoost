# AutoAgent Registry

Fixed routines used by `operate`, `review`, and selected sprint tasks. They are
repo-defined specialists, not new top-level human roles.

| AutoAgent | Purpose | Reads | Writes | Trigger | Escalation | Memory |
|-----------|---------|-------|--------|---------|------------|--------|
| `ContentSync` | Fix direct consistency drift, stale status propagation, duplicate rules, unresolved placeholders, and missing path refs in scope | Scoped files, `agents/rules/core/*`, `agents/state/current.md` | Scoped consistency fixes, optional backlog note | `review`, `system-review`, explicit `operate` | Core/workflow contradictions or missing routes -> `system-review` / user | `agents/state/memory/review/` |
| `MarkdownLintChecker` | Make scoped Markdown pass current CI rules without changing lint policy | Scoped `.md` files, `agents/rules/core/ci-rules.md`, link rules | Markdown-only fixes in scope | `review`, explicit `operate` | Policy change needed -> `system-review` | `agents/state/memory/review/` |
| `LatexCompileChecker` | Compile touched LaTeX targets with the existing local scripts and fix blocking compile issues | Scoped TeX files, local build scripts, figures | Scoped LaTeX / figure-path fixes | `review`, explicit `operate` | Toolchain or broad content drift -> `system-review` / user | `agents/state/memory/review/` |
| `SocialMediaInvestigator` | Produce dated, source-disciplined research on current trends and best practices | Mission, brand, marketing, current plan, approved artifacts | Dated report in `agents/work/social/research/` | Explicit `operate`, optional scheduler outside canonical files | Weak sources or mission conflict -> user | `agents/state/memory/social/` |
| `SocialMediaPlanner` | Maintain one canonical social plan aligned with mission, style, and available proof | Mission, brand, marketing, current state, investigator reports | `agents/work/social/plan.md` | Explicit `operate`, social sprint tasks | Needs brand/channel change -> `system-review` / user | `agents/state/memory/social/` |
| `SocialMediaWriter` | Draft 3 differentiated post options with pros / cons and evidence links | `agents/work/social/plan.md`, approved artifacts, community template | Drafts in `agents/work/social/drafts/` | Explicit `operate`, social sprint tasks | Missing evidence or stale plan -> planner / user | `agents/state/memory/social/` |

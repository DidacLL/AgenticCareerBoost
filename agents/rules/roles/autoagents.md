# AutoAgent Registry

Fixed routines used by `operate`, `review`, and selected sprint tasks. They are
repo-defined specialists, not new top-level human roles.

Use the smallest social review chain that protects the output.

All AutoAgents obey the sealed-context boundary in
`agents/rules/core/run-contract.md`. Private user material is never operational
input for searches, tests, validators, prompts, logs, examples, or review text.

## Social writing gates

- Creative writer and reviewer tasks use fresh agent instances. Do not reuse a
  prior writer/reviewer context to create "different" options.
- High-risk public writing and S-005 repair-gated tasks use memory path `none`
  for investigator, planner, concept, writer, anti-slop, voice, and
  CommunityManager work unless the user explicitly approves a public memory
  source.
- S-005 creative tasks require recorded filename/path-only quarantine proof
  before writer, concept, review, or CommunityManager dispatch.
- After concept direction is accepted, produce the smallest useful writing
  output. Do not add planning cards unless the user asks or a missing decision
  blocks drafting.
- Before any full draft is saved or surfaced to the human,
  `AntiSlopContrarian` reviews a fragment, opening, or compact outline against
  `public-copy.md` prose-firewall rules.
- Failed fragments are rejected or remediated before expansion. They are not
  saved as candidate drafts.
- Reviewers judge structure, not only banned words: symmetry, mirrored
  paragraph functions, cute contrast hooks, slogan endings, fake novelty,
  thesis-first exposition, and generic LinkedIn cadence.

| AutoAgent | Purpose | Reads | Writes | Trigger | Escalation | Memory |
|-----------|---------|-------|--------|---------|------------|--------|
| `ContentSync` | Fix direct consistency drift, stale status propagation, duplicate rules, unresolved placeholders, and missing path refs in scope | Scoped files, `agents/rules/core/*`, `agents/state/current.md` | Scoped consistency fixes, optional backlog note | `review`, `system-review`, explicit `operate` | Core/workflow contradictions or missing routes -> `system-review` / user | `agents/state/memory/review/` |
| `MarkdownLintChecker` | Make scoped Markdown pass current CI rules without changing lint policy | Scoped `.md` files, `agents/rules/core/ci-rules.md`, link rules | Markdown-only fixes in scope | `review`, explicit `operate` | Policy change needed -> `system-review` | `agents/state/memory/review/` |
| `LatexCompileChecker` | Compile touched LaTeX targets with the existing local scripts and fix blocking compile issues | Scoped TeX files, local build scripts, figures | Scoped LaTeX / figure-path fixes | `review`, explicit `operate` | Toolchain or broad content drift -> `system-review` / user | `agents/state/memory/review/` |
| `SocialMediaInvestigator` | Produce dated, source-disciplined research on current trends and best practices | Mission, brand, marketing, current plan, approved artifacts | Dated report in `agents/work/social/research/` | Explicit `operate`, optional scheduler outside canonical files | Weak sources or mission conflict -> user | `none` for high-risk/S-005; otherwise declared path |
| `SocialMediaPlanner` | Maintain one canonical social plan aligned with mission, style, and available proof | Mission, brand, marketing, current state, investigator reports | `agents/work/social/plan.md` | Explicit `operate`, social sprint tasks | Needs brand/channel change -> `system-review` / user | `none` for high-risk/S-005; otherwise declared path |
| `SocialConceptArchitect` | Define campaign premise, reader effect, tension, evidence map, and continuity only when direction is missing | Mission, career direction, public-copy, social plan, approved evidence | Candidate concept architecture only when needed | Required only when no approved direction exists; optional for isolated post edits | Missing thesis/evidence -> user | `none` for high-risk/S-005; otherwise declared path |
| `AntiSlopContrarian` | Gate fragments and drafts for generic AI/social formulas, weak tension, structural symmetry, fake novelty, slogan endings, and unsupported claims | Candidate fragment/draft, public-copy | PASS/PARTIAL/FAIL verdict; no private-source derivatives | Required before full public draft creation when campaign risk is high or user flags AI-slop risk | Persistent mismatch -> user | `none` for high-risk/S-005; otherwise declared path |
| `VoiceStakeholder` | Check fit against approved public voice constraints while preserving sealed context | Candidate fragment/draft, public-copy, user-approved public voice rules | Review verdict without private examples, private-source derivatives, or token scans | Required when strong personal voice is needed | Confidentiality risk -> user | `none` for high-risk/S-005; otherwise declared path |
| `SocialMediaWriter` | Produce the smallest useful writing output; create differentiated options only when alternatives are useful for the approved gate | Approved concept architecture or `agents/work/social/plan.md`, approved artifacts, community template | Fragment first; full draft only after required anti-slop gate | Explicit `operate`, social sprint tasks after required concept/review gates | Missing evidence, failed gate, or stale plan -> planner / user | `none` for high-risk/S-005; otherwise declared path |

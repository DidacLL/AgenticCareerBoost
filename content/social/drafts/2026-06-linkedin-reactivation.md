# LinkedIn Reactivation Drafts: June 2026

- Date: 2026-06-11
- Sprint: S-002R
- Task: 5 only
- Agent: bounded CommunityManager / SocialMediaWriter
- Inputs: `content/social/research/2026-06-linkedin-reactivation.md`, `content/social/style-book.md`, `docs/core/brand.md`, `docs/core/marketing.md`
- Status: draft candidates only

---

## Human Approval Gate

Do not publish, schedule, or automate any post below until a human approves:

- final post text,
- first-comment source bundle,
- profile consistency across LinkedIn, GitHub, and the public site,
- any companion image or document.

No post body contains external links. Sources belong in the first comment.

## Strategy Selection

Scoring: 1 low, 10 high. Higher total is better.

| Strategy | Recruiter fit | Peer credibility | Low-heat reentry | Source support | Effort | Total | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| A. Three low-heat technical stance posts | 9 | 9 | 9 | 9 | 7 | 43 | Selected |
| B. One long reactivation essay | 7 | 8 | 5 | 8 | 6 | 34 | Reject |
| C. Direct profile-audit launch | 8 | 8 | 4 | 7 | 8 | 35 | Defer |
| D. Comment-only warmup | 5 | 7 | 9 | 4 | 5 | 30 | Reject |

Selected: A. It rebuilds feed trust before the main campaign and keeps the account anchored in technical judgment instead of announcement energy.

## Draft 1: Agents Need Receipts

**Angle**: governance before autonomy.

**Post text**:

Agentic coding tools are getting better. That makes the boring parts more important.

Not the demos. The receipts.

If an agent edits code, I want to know:

- what files it touched
- what commands it ran
- what tests passed or failed
- what assumptions it made
- where the human review happens

That is the part of the current agentic wave I actually care about.

OpenAI's Codex framing is useful here: isolated environments, terminal logs, test outputs, citations, AGENTS.md guidance, and review before integration. The interesting pattern is not "delegate everything." It is "make delegated work inspectable."

The safety research points in the same direction from the other side. As soon as agents get sensitive access and weak approval boundaries, governance stops being paperwork and becomes part of the system design.

My rule for agentic workflows is simple:

- bounded actions before autonomy
- logs before trust
- tests before merge
- human approval before publication

That does not make agents less useful. It makes them usable.

**First comment source bundle**:

Sources behind the post:

- Human oversight of agentic systems in practice: <https://arxiv.org/abs/2606.05391>
- OpenAI Codex release notes: <https://openai.com/index/introducing-codex/>
- Anthropic agentic misalignment research: <https://www.anthropic.com/research/agentic-misalignment>
- Public repo: <https://github.com/DidacLL/AgenticCareerBoost>

**Safety notes**:

- Public-safe principles only: bounded actions, logs/tests, human review, governance before autonomy.
- No private project names or unpublished implementation details.
- No claim that current coding agents are inherently unsafe.
- Current-source anchor is the June 2026 oversight paper; vendor posts are market-context anchors.

**Approval checklist**:

- [ ] Human approves final text.
- [ ] Human verifies LinkedIn profile consistency.
- [ ] Human approves first comment.
- [ ] Human approves any companion image.

## Draft 2: Model-Agnostic Is Not Aesthetic

**Angle**: vendor convergence makes workflow portability a design constraint.

**Post text**:

I do not want an agentic workflow that only works on one model, one vendor, and one cloud surface.

That is not a philosophical preference. It is an engineering constraint.

OpenAI is pushing Codex as a cloud software engineering agent that can work on tasks in parallel, run tests, cite logs, and use repository guidance files.

Anthropic is pushing Claude Code across terminals, IDEs, SDKs, and GitHub workflows, with stronger tool use, memory, and long-running project context.

Different products. Same direction: coding agents are becoming workflow participants, not just autocomplete boxes.

That makes the orchestration layer matter.

The workflow should define:

- what context the agent can read
- what actions it can take
- what evidence it must leave
- what review gate stops it
- what happens when the model changes

If the system collapses when the model changes, the model was carrying too much of the architecture.

Model-agnostic does not mean pretending all models are equal. It means the workflow keeps control of routing, scope, evidence, and approval.

The model can be swapped.

The standards should not be.

**First comment source bundle**:

Sources behind the post:

- AIDev agent-authored pull-request dataset: <https://arxiv.org/abs/2602.09185>
- ABC-Bench agentic backend coding benchmark: <https://arxiv.org/abs/2601.11077>
- OpenAI Codex release notes: <https://openai.com/index/introducing-codex/>
- Anthropic Claude 4 / Claude Code release: <https://www.anthropic.com/news/claude-4>
- Public repo: <https://github.com/DidacLL/AgenticCareerBoost>

**Safety notes**:

- Does not rank vendors or claim one model is better.
- Keeps the claim at architecture level: routing, scope, evidence, approval.
- Avoids unpublished project details.
- Uses 2026 research as the current agentic-coding anchor; vendor posts only show product-direction convergence.

**Approval checklist**:

- [ ] Human approves final text.
- [ ] Human verifies LinkedIn profile consistency.
- [ ] Human approves first comment.
- [ ] Human approves any companion image.

## Draft 3: Skills Are Not Magic

**Angle**: context compatibility beats generic prompt/skill decoration.

**Post text**:

"Just add agent skills" is not a strategy.

SWE-Skills-Bench tested whether injected skills actually help software-engineering agents on real repository tasks. The result is a useful correction to the hype:

- 39 of 49 skills gave zero pass-rate improvement
- average gain was +1.2%
- token overhead sometimes reached 451%
- version-mismatched guidance could make performance worse

The lesson is not "skills are useless."

The lesson is narrower and more useful: context fit matters.

A good agent skill has to match the repository, the task type, the tools, the acceptance criteria, and the failure modes. Otherwise it is just more text in the context window.

For my own workflows, I would rather have:

- small role files
- explicit file paths
- clear write scope
- lightweight tests
- human review gates

than a giant universal skill pack that sounds impressive and adds no measurable lift.

Agentic systems should be judged the same way other engineering systems are judged:

What changed?

How do we know?

What broke?

Who approved it?

**First comment source bundle**:

Sources behind the post:

- SWE-Skills-Bench paper: <https://arxiv.org/abs/2603.15401>
- Phoenix-bench hardware-engineering benchmark: <https://arxiv.org/abs/2605.15226>
- ABC-Bench backend-coding benchmark: <https://arxiv.org/abs/2601.11077>
- OpenAI Codex release notes: <https://openai.com/index/introducing-codex/>
- Public repo: <https://github.com/DidacLL/AgenticCareerBoost>

**Safety notes**:

- Does not attack skill authors or tool builders.
- Benchmark claims stay tied to the paper.
- Keeps the public stance on generic design principles only.
- Phoenix-bench and ABC-Bench are only supporting anchors for context fit, executable feedback, and realistic workflow difficulty.

**Approval checklist**:

- [ ] Human approves final text.
- [ ] Human verifies LinkedIn profile consistency.
- [ ] Human approves first comment.
- [ ] Human approves any companion image.

## Recommended Order

1. Draft 1: Agents Need Receipts.
2. Draft 2: Model-Agnostic Is Not Aesthetic.
3. Draft 3: Skills Are Not Magic.

Rationale: start with governance, move to architecture, then close with benchmark discipline. This keeps the sequence technical and restrained before the larger profile-audit campaign.

## Final Pre-Publication Gate

- [ ] No external links in post body.
- [ ] No announcement cliches.
- [ ] No AI prophecy or replacement framing.
- [ ] No bitterness or dunking.
- [ ] No engagement-bait CTA.
- [ ] No private project names or unpublished details.
- [ ] First comment contains required sources.
- [ ] Human approval recorded before posting.

# LinkedIn Reactivation Review

- Date: 2026-06-11
- Agent: bounded CommunityManager / SocialResearch sidecar
- Scope: LinkedIn reactivation and social campaign viewpoint only
- Output status: recommendation, not publication copy

## Evidence Read

- Core stance: public proof first; LinkedIn is selective distribution, not the source of truth.
- Brand stance: technical, disciplined, direct; no generic AI hype, founder-LARP, or apology framing.
- Social plan: current main campaign starts with profile audit / UOC readiness / document reveal / governance proof.
- Existing drafts: strong first-post candidates exist, especially the profile/headline flaw narrative.
- Link registry: GitHub, LinkedIn, repo, and site URLs are present in `data/links.json`.
- Public site check: `https://didacll.github.io/AgenticCareerBoost/` is live and aligned around Software Engineering, ML/AI, Agentic Systems, Barcelona.
- GitHub API check: `https://api.github.com/users/DidacLL` returned public profile with 13 repos, 7 followers, Barcelona, but empty `bio`, `blog`, and `hireable`.
- LinkedIn check: `https://www.linkedin.com/in/didacllorens/` hit LinkedIn authwall; current visible profile copy could not be verified externally.
- Private stance reference was accessible; used only as background philosophy, with no unpublished specifics carried into public concepts.

## Current Discourse Anchors

- OpenAI framed Codex as a cloud software engineering agent that can work on many tasks in parallel, with AGENTS.md guidance, logs, tests, and human review as verification surfaces: https://openai.com/index/introducing-codex/
- Anthropic framed Claude 4 around coding, long-running agent workflows, parallel tools, memory, and agent APIs: https://www.anthropic.com/news/claude-4
- Anthropic's agentic misalignment work argues for caution when models get sensitive access and minimal human oversight: https://www.anthropic.com/research/agentic-misalignment
- SWE-Skills-Bench reports limited average gains from generic agent skills and strong dependence on domain fit/context compatibility: https://arxiv.org/abs/2603.15401

## Diagnosis

The main campaign is evidence-rich but too abrupt for a cold or recently inactive LinkedIn account. Posting the full profile-audit reveal first risks looking like a launch blast before the network has been re-warmed.

The better move is a short reactivation sequence that re-enters the feed with useful, restrained observations about agentic engineering, then points toward the public proof loop.

## Reactivation Strategy Options

| Option | Fit | Credibility | Evidence | Risk | Effort | Notes |
|---|---:|---:|---:|---:|---:|---|
| A. Three-post low-heat reactivation before campaign | 9 | 9 | 8 | 8 | 7 | Rebuilds presence before asking people to inspect the system. Best balance. |
| B. Direct audit reveal as first post | 8 | 8 | 9 | 5 | 8 | Strong artifact, but high self-exposure and launch energy after inactivity. |
| C. Comment-first warmup for 10 working days, no original posts | 7 | 8 | 6 | 9 | 5 | Low risk, but slow and leaves the campaign dependent on external threads. |
| D. Profile-only silent cleanup, then main campaign | 6 | 7 | 7 | 7 | 8 | Necessary hygiene, but does not rebuild feed trust. |

Selected: **Option A — three-post low-heat reactivation before campaign**.

## Selected Sequence

1. **Week 0 hygiene gate**: verify LinkedIn headline/About/Featured against site and GitHub; fix GitHub public bio/blog/hireable mismatch first if still empty.
2. **Post 1 — stance re-entry**: short text post on why "agentic" work needs governance, not theatre.
3. **Post 2 — evidence discipline**: compact post showing one public artifact or diagram, framed as inspectable work rather than announcement.
4. **Post 3 — market/learning bridge**: tie recent agent discourse to why model-agnostic, local-first, human-reviewed workflows matter for junior-accessible engineering credibility.
5. **Main campaign start**: publish the existing profile/headline flaw narrative only after the three posts have established tone and current profile consistency.

## Draft Post Concepts

### Concept 1: "Agents Need Receipts"

- Angle: React to Codex-style coding agents becoming normal by arguing that the interesting part is not delegation, but traceable work.
- Anchor: OpenAI Codex emphasizes isolated environments, terminal logs, tests, citations, AGENTS.md, and human review.
- Public-safe claim: "A useful agentic workflow should leave enough evidence for another engineer to inspect what happened."
- Companion: screenshot/crop of public `AGENTS.md` or routing diagram after safety review.
- Avoid: "AI will replace developers" framing.

### Concept 2: "Model-Agnostic Is Not Aesthetic"

- Angle: Use current Claude/OpenAI coding-agent competition to explain why provider flexibility is an engineering constraint, not a slogan.
- Anchor: OpenAI Codex and Claude 4 both push deeper agent workflows; market direction increases lock-in pressure.
- Public-safe claim: "If a workflow only works with one model, one vendor, and one cloud surface, the architecture is carrying hidden risk."
- Companion: small architecture excerpt from the public site showing path-based orchestration.
- Avoid: attacking any vendor or implying unpublished product claims.

### Concept 3: "Skills Are Not Magic"

- Angle: Ground the agent-skills conversation in SWE-Skills-Bench: generic skill packs often add overhead without improving pass rate.
- Anchor: SWE-Skills-Bench reports 39/49 skills with zero pass-rate improvement and average gain of +1.2%.
- Public-safe claim: "Context compatibility beats prompt jewelry."
- Companion: no media, or simple table: "skill / repo context / acceptance test / result".
- Avoid: dunking on skill authors; target design discipline, not people.

## Quality Gates

- Source quality: every news/paper claim must cite primary or high-credibility sources; use vendor posts for product claims, papers for benchmark/safety claims, avoid unsourced LinkedIn screenshots as evidence.
- Tone: no "excited to announce", no AI prophecy, no engagement bait, no apology for career transition, no fake seniority.
- Unpublished-project safety: do not name or describe private reference systems; public posts may only use abstract principles already safe in the public repo: model-agnostic, bounded, inspectable, evidence-first.
- Profile consistency: LinkedIn headline/About/Featured, GitHub profile, site title, and first-comment links must tell the same story before posting.
- Evidence fit: each post must point to a public artifact, public source, or public profile surface; no unsupported "I built X" without a repo/report/page behind it.
- Human authority: any claim about agents must keep human review, tests, logs, and rollback in frame.

## Backlog Delta

- Add LinkedIn authwall/manual profile verification checklist before first reactivation post.
- Fix GitHub public profile `bio`, `blog`, and `hireable` if API state remains empty.
- Prepare one public-safe image crop from routing architecture or AGENTS.md for Concept 1/2.
- Create first-comment source bundle for each reactivation post.
- Add social gate: no main campaign launch until three reactivation posts or explicit waiver.

## Blockers

- LinkedIn current profile content could not be externally verified due to authwall.
- GitHub public API suggests profile metadata is not fully synced with the site.
- Recent social research files are dated April 2026; reactivation posts should use refreshed sources above before publication.

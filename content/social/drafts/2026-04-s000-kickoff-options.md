# Sprint S-000 Kickoff Post Options

- Date: 2026-04-19
- Sprint: S-000
- Agent: CommunityManager (T6)
- Style book: content/social/style-book.md
- Research: content/social/research/2026-04-linkedin-career-agentic-landscape.md

---

## Option A — "The Contradiction Hook" (Career-change + technical reveal)

### Strategic label

Architecture-first career pivot — leads with the paradox of deep experience meeting zero tech credentials.

### Target audience emphasis

- Recruiters: 50% (scannable proof, clear capability signal)
- Engineering peers: 40% (architecture specifics invite technical engagement)
- Career-changers: 10% (relatable situation, actionable framing)

### Channel

LinkedIn (primary). GitHub README blurb variant: shorter, links to the LaTeX PDF and sprint contract.

### Full draft body (LinkedIn, 1,387 chars)

```text
I have 15 years of professional experience — none of it in tech.

So I built a multiagent system to engineer my own career transition.

Not a chatbot wrapper. Not a LangChain tutorial. A path-based operating
system where 6 specialized agents navigate a repository through file
paths and contracts. No mega-prompts. No vendor lock-in. Any LLM that
can read a file works.

Here's what the system actually does:

→ An Orchestrator decomposes sprints into tasks with formal contracts
→ Developer agents execute one task each, then two fresh PairCheck
  agents review independently — no self-approval allowed
→ Documentation agent produces LaTeX engineering reports with
  architecture diagrams
→ A CommunityManager agent turns sprint outputs into this post

The architecture is the portfolio. Every rule is a file with git
history. Every decision is diffable. Recruiters can inspect the tree
and see engineering judgment, not adjectives.

I'm 36, finishing a Software Engineering degree in Barcelona, with an
art background and 15 years managing production systems for 50K+
customers in banking. The systems changed. The thinking didn't.

The full repository — AGENTS.md entrypoint, truth hierarchy, sprint
contracts, LaTeX documentation — is open source.

Link in first comment.

What's the most unusual system you've built to solve a non-engineering
problem?

#AgenticEngineering #CareerChange #OpenSource #SystemDesign
```

### Hook / Proof / CTA breakdown

- **Hook:** "15 years of experience — none in tech" (honest admission pattern, 4.8% engagement per T4 §S1)
- **Proof:** Architecture specifics (6 agents, path-based routing, PairCheck, LaTeX), open-source repo
- **CTA:** Experience-sharing question, specific enough to filter generic replies

### Evidence links

- Repository: <https://github.com/DidacLL/AgenticCareerBoost>
- AGENTS.md: <https://github.com/DidacLL/AgenticCareerBoost/blob/main/AGENTS.md>
- S-000 LaTeX source: content/reports/tex/sprints/s000-agentic-os-bootstrap.tex
- Published S-000 PDF: <https://github.com/DidacLL/AgenticCareerBoost/blob/main/content/reports/build/s000-agentic-os-bootstrap.pdf>
- Sprint closure record: state/active-sprint.md

### KPI targets (first 7 days, cold-start adjusted)

- Profile visits: 50-150 (cold-start range; upper bound assumes network seeding via BCN Engineering / GDG Barcelona)
- Post impressions: 500-3,000 (new account with zero followers; upper bound aspirational)
- Engagement rate: 3.5%+ (T4 §3.3 sweet-spot benchmark — rate is follower-independent)
- Comments: 5-15 (substantive, not "great post!")
- Recruiter messages: 1-2 (stretch goal)
- Repo stars: 3-5 (secondary)

### Pros / Cons

| Pros | Cons |
|------|------|
| Combines two highest-scoring approaches (T4 §6.2: 23/30 + 22/30) | Long for a first post — new profiles have less reach |
| Contradiction hook is the highest-engagement opener pattern | Architecture details may lose non-technical recruiters in the middle |
| Open-source link drives profile visits and repo traffic | Requires the CI pipeline to be green before posting (evidence dependency) |
| Model-agnostic positioning is a genuine differentiator (T4 §2.3) | The "none in tech" admission may trigger unconscious bias in some recruiters |
| Every claim links to inspectable evidence | First-post cold start: no existing audience to seed initial engagement |

---

## Option B — "The Document Reveal" (Architecture artifact as native upload)

### Strategic label

Engineering-artifact-first — leads with a native PDF upload of the actual system design document, framed by a short narrative.

### Target audience emphasis

- Engineering peers: 55% (the document itself is the content)
- Recruiters: 35% (the document demonstrates engineering maturity)
- Career-changers: 10% (the meta-narrative is implicit)

### Channel

LinkedIn (primary, native PDF upload). GitHub: the PDF is published in `content/reports/build/`. Site: link to the PDF from the projects page when S-002 ships.

### Full draft body (LinkedIn, 1,192 chars)

```text
Here's the actual system design document for a model-agnostic
multiagent career system.

Not a slide deck. Not a blog summary. The real engineering
documentation — architecture diagrams, truth hierarchy, agent
contracts, workflow specifications — written in LaTeX and built
by the system it describes.

What's inside:

→ How 6 agents coordinate through file paths, not prompts
→ A strict truth hierarchy that eliminates conflicting instructions
→ Why every agent output passes through two independent reviewers
→ Sprint contracts, output templates, and state machinery
→ CI/CD automation on GitHub's free tier — including building
  this PDF automatically

The system is model-agnostic: swap the LLM, keep the orchestration.
Total infrastructure cost: a GitHub account and whatever AI you
bring.

I designed this at 36, transitioning from 15 years in banking to
software engineering. The architecture is my portfolio.

Full source and documentation are open: link in first comment.

What engineering documentation practices do you use for your
personal projects?

#SystemDesign #AgenticEngineering #LaTeX #OpenSource
```

### Hook / Proof / CTA breakdown

- **Hook:** "Here's the actual system design document" (reveal pattern + native document upload for 5-10x reach per T4 §S4)
- **Proof:** The document itself — readers can download and inspect it
- **CTA:** Question about documentation practices, invites peer-level engagement

### Evidence links

- Attached PDF: s000-agentic-os-bootstrap.pdf (native LinkedIn upload)
- Repository: <https://github.com/DidacLL/AgenticCareerBoost>
- LaTeX source: content/reports/tex/sprints/s000-agentic-os-bootstrap.tex

### KPI targets (first 7 days, cold-start adjusted)

- Profile visits: 80-200 (cold-start range; document format drives higher click-through)
- Post impressions: 1,000-5,000 (document upload algorithm boost partially offsets zero-follower penalty)
- Engagement rate: 4.0%+ (T4 §3.4: documents outperform text — rate is format-driven)
- Comments: 8-20 (engineers respond to real documentation)
- PDF downloads: 15-50
- Recruiter messages: 1-3 (stretch — document signals senior-level thinking)

### Pros / Cons

| Pros | Cons |
|------|------|
| Native PDF gets 5-10x reach per 2026 algorithm (T4 §S4) | Requires the PDF to be compiled and polished before posting |
| The document *is* the proof — no gap between claim and evidence | Less emotionally engaging than a personal narrative |
| Positions Dídac as someone who writes engineering documentation (rare, valued) | Non-technical recruiters may not open a 37-page PDF |
| LaTeX quality signals academic/research depth | Cold audience may need more personal context to care |
| Highly shareable among engineering peers | Career-change narrative is buried — may not trigger the empathy/curiosity response |

---

## Option C — "The Anti-Hype Manifesto" (Contrarian positioning)

### Strategic label

Contrarian take — directly opposes the saturated AI-hype framing while demonstrating real engineering through the contrast.

### Target audience emphasis

- Engineering peers: 60% (the opinion invites debate)
- Recruiters: 30% (the technical specifics underneath signal capability)
- Career-changers: 10% (the "don't follow the herd" angle is implicitly motivating)

### Channel

LinkedIn (primary, text-only — the opinion is the content). GitHub: no specific variant. Site: could become a blog essay in S-002.

### Full draft body (LinkedIn, 1,478 chars)

```text
I'm not an AI influencer. I'm an engineer who uses AI as tooling.

Most agentic-AI content I see on LinkedIn is framework demos or
hype threads. Here's something different: a production system I
actually use.

6 agents — Orchestrator, Developer, PairCheck (x2), Documentation,
CommunityManager — navigate a repository through file paths and
Markdown contracts. No vendor lock-in. No mega-prompts.
Model-agnostic: swap the LLM, keep the orchestration.

The system has a formal truth hierarchy that resolves conflicting
information deterministically. Every agent output gets two
independent reviews before integration. Every sprint produces 6
documented closure artifacts. CI builds LaTeX engineering reports
automatically.

Total infrastructure cost: $0. GitHub free tier and whatever AI
model you bring.

I'm 36, in Barcelona, transitioning from 15 years in financial
services to software engineering. I built this because I needed
a system that works — and because the architecture itself is the
portfolio.

The full system design is open source. The engineering is the proof.

Repo link in first comment.

What's the most interesting non-enterprise use case you've seen
for agentic AI?

#AgenticEngineering #SystemDesign #OpenSource #BuildInPublic
```

### Hook / Proof / CTA breakdown

- **Hook:** "I'm not an AI influencer. I'm an engineer who uses AI as tooling." (contradiction + opinion pattern, inferred 3.7-4.2% engagement from T4 §3.1 data)
- **Proof:** System architecture specifics, truth hierarchy, PairCheck, LaTeX CI, $0 cost
- **CTA:** Genuine curiosity question about non-enterprise agentic use cases — invites peer-level sharing

### Evidence links

- Repository: <https://github.com/DidacLL/AgenticCareerBoost>
- AGENTS.md: <https://github.com/DidacLL/AgenticCareerBoost/blob/main/AGENTS.md>
- Truth hierarchy: docs/core/truth-hierarchy.md
- LaTeX build CI: .github/workflows/latex-build.yml

### KPI targets (first 7 days, cold-start adjusted)

- Profile visits: 80-250 (cold-start range; opinion posts drive click-through if they reach critical mass)
- Post impressions: 1,000-4,000 (opinion format helps but cold-start limits reach)
- Engagement rate: 3.5-4.2%+ (inferred from T4 §3.1 contradiction/opinion hooks)
- Comments: 10-25 (the genuine-curiosity CTA invites substantive replies)
- Recruiter messages: 1-2 (opinion positioning attracts attention but is slower to convert)
- Repo stars: 5-8 (engineers who resonate will inspect the work)

### Pros / Cons

| Pros | Cons |
|------|------|
| Directly opposes the most saturated anti-pattern (AI hype) — brand-aligned | Contrarian positioning requires established credibility to fully land |
| Opinion hook invites debate and resharing (T4 §3.1: 3.7-4.2% range) | First-post + opinion is higher variance than narrative + proof |
| Positions Dídac as a practitioner, not a commentator — memorable | The anti-hype stance must be sustained across subsequent posts or looks like a one-off gimmick |
| The $0 cost and model-agnostic framing are powerful contrarian proofs | Less emotionally engaging than a personal narrative for non-technical readers |
| CTA invites genuine peer-level discussion about agentic use cases | First-post cold start limits reach regardless of content quality |

---

## Agent Recommendation

### Recommended: Option A ("The Contradiction Hook")

**Rationale:**

1. It scores highest across both primary audiences (recruiters + peers) per T4 §6.2 scoring.
2. The contradiction hook ("15 years, none in tech") is the most data-backed high-engagement pattern for a first post (honest admission at 4.8% per T4 §S1).
3. It introduces all the signature motifs (path-based routing, model-agnostic, PairCheck, LaTeX) without requiring the reader to download anything.
4. The personal narrative creates an emotional entry point; the architecture specifics create the technical proof. It works for both audiences in one post.
5. Option B (PDF reveal) is excellent but better as a second post (Thursday follow-up) once the narrative context is established.
6. Option C (anti-hype) is high-variance and risks establishing a combative first impression. Reserve the contrarian edge for post 3-4, after the audience knows who Dídac is.

**Recommended sequence:**

- Post 1 (Tuesday): Option A — establish the person + the system
- Post 2 (Thursday): Option B — the document reveal, referencing Post 1
- Post 3 (following Tuesday): Option C — the opinion piece, now backed by two prior evidence-linked posts

**But the user decides.** All three options are brand-compliant and evidence-backed.

---

*All drafts verified against content/social/style-book.md §8 (Forbidden-Tone Checklist). No violations detected. Every evidence link resolves to a file in the repository or a published repository artifact.*

# Public Voice Style Book — AgenticCareerBoost

- Date: 2026-04-19
- Sprint: S-000
- Agent: CommunityManager (T5)
- Sources: T4 research report, docs/core/brand.md, docs/core/marketing.md, bootstrap/user_data.md

---

## 1. Positioning One-Liner

> Systems engineer building model-agnostic agentic workflows — 15 years of experience, none in tech, all on purpose.

(139 characters. Combines the contradiction hook with the capability claim.)

**Source:** T4 §6.3 (recommended hook pattern) + brand.md §Positioning ("systems-minded builder, technical generalist").

---

## 2. Audience Hierarchy

| Priority | Audience | What they need | Weight |
|----------|----------|----------------|--------|
| 1 | **Recruiters** | Fast proof of capability and role-fit. Scannable evidence. Clear skill taxonomy. | 55% |
| 2 | **Engineering peers** | Visible craft, systems thinking, tooling depth. Inspectable work. | 35% |
| 3 | **Career-changers / students** | Relatable narrative, honest timeline, actionable path. | 10% |

**Source:** marketing.md §Audience (recruiters first, peers second). Weight ratios are inference from T4 §6.2 scoring.

---

## 3. User-Priority Emphasis Map

Every public artifact must foreground at least one of these priorities. Each is explicitly mapped from `bootstrap/user_data.md` §Priorities and §Interests.

| Priority | user_data.md source | How to express | Frequency |
|----------|---------------------|----------------|-----------|
| **Meaningful/career-building roles** | §Priorities: "Meaningful or Career building offers over typical backend consulting" | Frame target as "systems-aware and dynamic positions." Never mention consulting as a goal. When discussing job search, emphasize growth trajectory, not just employment. | Every post implicitly |
| **Language/technology agnostic** | §Priorities: "Language and technology agnostic, I can learn easily" | Present as deliberate engineering philosophy, not lack of specialization. "Model-agnostic by design" > "I know a bit of everything." | Every technical post |
| **Opensource + resource-aware** | §Interests: "Opensource and resource consumption aware programming" | Cite zero-cost infrastructure. Link open repos. Mention token efficiency. Frame resource awareness as engineering discipline, not budget constraint. | Every 2nd post |
| **LaTeX / unusual environments** | §Interests: "LaTeX and unexpected and complicated environments" | Show actual LaTeX output (PDF uploads). Reference formal documentation as a skill signal. Use it as a differentiator: "Yes, I write engineering docs in LaTeX. On purpose." | Every 3rd post |
| **Investigation + creative thinking** | §Interests: "Investigation, problem solving and creative thinking" | Demonstrate through architecture decisions, not abstract claims. Show the problem-solving trace, not just the solution. | Every technical post |
| **Art + postexpressionism** | §Interests: "Art (postexpresionism)" | Use sparingly as cultural accent. Visual sensibility in diagrams. Occasional metaphor. Never as primary identity. | Every 5th post max |
| **Barcelona / Catalan accent** | user_data.md §Personal data + brand.md §Language policy: "Catalan as accent, not default" | Mention Barcelona context when relevant (meetups, local market). Use a Catalan word or reference occasionally. Never force it. | When locally relevant |

**Source:** bootstrap/user_data.md §Priorities, §Interests. Frequency is inference from T4 §4.3 (art as accent) and brand.md §Language policy.

---

## 4. Voice Rules

### 4.1 Do's

| Rule | Example | Source |
|------|---------|--------|
| Lead with what you built, not who you are | "I designed a 6-agent system with formal truth hierarchy" not "Hi, I'm a career changer" | T4 §5.1: "Lead with the system, not the person" |
| Use concrete tool names and metrics | "Built with pdflatex, latexmk, and GitHub Actions. 12 files, 6 roles, 5 workflows." | T4 §4.1: concrete tool names signal technical authenticity |
| Acknowledge the career transition honestly | "I have 15 years of experience that no recruiter asked for. So I'm engineering new ones." | T4 §4.3: self-aware irony about age/transition |
| Back every claim with a link | "The full system design: [link in first comment]" | marketing.md §Artifact rules: "evidence over adjectives" |
| Write in first person, conversational register | "I spent three days on this. Here's what I learned." not "One should consider..." | T4 §4.1: first-person specificity; S6: conversation > broadcast |
| Show trade-offs, not just wins | "The system works but the token cost for the full sprint was higher than expected." | T4 §4.1: "trade-off awareness" signals maturity |
| Use arrow points (→) over numbered emoji lists | "→ Point one\n→ Point two" not "1️⃣ Point one\n2️⃣ Point two" | T4 §4.2: emoji lists are an AI-tell pattern |

### 4.2 Don'ts

| Rule | Anti-pattern rewrite | Source |
|------|---------------------|--------|
| Never use "excited to announce" | BEFORE: "Excited to announce I've completed my latest sprint!" AFTER: "Sprint S-000 closed. 6 agents, 4 TikZ diagrams, 1 PDF. Here's the architecture." | T4 §4.2: lowest-engagement opener (0.8%). brand.md: no empty self-description. |
| Never use "game-changer" or "thought leadership" | BEFORE: "This agentic system is a game-changer for career development." AFTER: "This system runs on Markdown files and whatever LLM you point at it. Total cost: $0." | T4 §4.2: buzzwords signal fluff. brand.md: technical, disciplined, direct. |
| Never apologize for being a career changer | BEFORE: "I know I don't have traditional tech experience, but..." AFTER: "I managed production systems serving 50K customers for 15 years. The systems changed; the thinking didn't." | T4 §5.5: avoid "just a junior" framing. brand.md: never "just another junior." |

### 4.3 Controlled Sarcastic Edge (Guidelines)

The sarcastic/provocative edge from brand.md is permitted in public-facing content but must follow these rules:

- **Target systems and framings, never people.** "I love how LinkedIn thinks 'Open to Work' is a strategy" — acceptable. Mocking a specific person — never.
- **Back it up immediately.** The sarcastic line is the hook; the next sentence must be substantive. One without the other fails.
- **Use at most once per post.** Two sarcastic lines in the same post reads as bitter, not sharp.
- **Never in the CTA.** The closing should be genuine and inviting.

**Source:** brand.md §Tone: "controlled sarcastic / provocative edge where appropriate. Never chaotic, never self-sabotaging."

---

## 5. Visual Rules

| Rule | Specifics | Source |
|------|-----------|--------|
| Prefer diagrams over selfies | Architecture diagrams, directory trees, flowcharts. Never stock photos. | T4 §3.4: single image (3.4%) and document (5-10x) outperform text. brand.md: technical identity. |
| Use branded PDF documents | Export architecture docs, sprint summaries as clean PDFs. Upload natively to LinkedIn. | T4 §3.4: S4 data shows native documents get 5-10x reach. |
| Screenshots with context | Terminal output, GitHub UI, CI run results. Always add a one-line caption explaining what the viewer is seeing. | T4 §3.4: code screenshots work as companion images. |
| Consistent visual style | Use the TikZ diagram styles from `preamble/tikzlib.tex` for all architecture visuals. Blue accent (#2563EB), gray for data edges, red for failure paths. | Aligns with LaTeX infrastructure (T1). Creates visual brand recognition. |
| No decorative graphics | Every image must contain information. Decorative hero images waste the viewer's time and violate brand tone. | brand.md: "technical, disciplined, direct." constraints.md: "avoid decorative complexity." |
| Screenshot convention for docs | Use `\screenshotfig` in LaTeX. Placeholder box appears if image is missing. User replaces with actual screenshots. | T1 safeimg.tex infrastructure. |

---

## 6. Recurring Hooks and Motifs

These are the signature themes that should recur across posts to build a recognizable voice:

| Motif | How to use | Example | Source |
|-------|-----------|---------|--------|
| **The Agentic OS** | Reference the system as a living artifact, not a finished product. | "The OS just closed Sprint S-000. Here's what it produced." | brand.md: "visible iteration discipline" |
| **Public proof loop** | The process is the proof. Every sprint produces inspectable artifacts. | "Every claim I make links to a commit. That's the rule." | marketing.md: "evidence over adjectives"; T4 §2.1 |
| **Path-based routing** | The architecture is the differentiator. Agents navigate files, not prompts. | "No mega-prompts. No vendor lock-in. Just Markdown files and file paths." | AGENTS.md §Why path-based; T4 §2.1 (rare framing) |
| **Engineering judgment visible in the tree** | The repo structure itself demonstrates skill. | "Recruiters can diff my decisions. That's the point." | Bootstrap plan §6: "the architecture itself is the case study" |
| **Model-agnostic ethos** | Vendor independence as principle, not convenience. | "I don't care which LLM runs the agents. I care about the orchestration." | user_data.md §Interests; T4 §2.3 (emerging differentiator) |
| **Cost transparency** | Honest about resource usage. | "Total infrastructure cost: a GitHub free tier and whatever LLM you bring." | T4 §2.3; constraints.md: free/student tools only |

---

## 7. Length and Cadence per Channel

| Channel | Format | Length | Cadence | Adaptation rule |
|---------|--------|--------|---------|-----------------|
| **LinkedIn** (primary) | Text post + companion image/PDF | 1,000–1,500 chars (sweet spot per T4 §3.3) | 2x/week: Tuesday (narrative) + Thursday (technical artifact) | Story in the post body. Link in first comment. Never external link in body. |
| **GitHub** (canonical) | README updates, PR descriptions, release notes | As needed by engineering completeness | Every sprint closure | Technical precision. Dense. No narrative padding. |
| **Site** (mirror) | Blog-style Markdown → Jekyll | 500–1,500 words | Monthly summary or per-sprint highlight | Curated and edited. Designed for recruiter scanning. AI-readable metadata. |

**Source:** marketing.md §Channels (priority order) + §Cadence rule. T4 §3.3 (length data) + §5.3 (consistency > volume).

**Critical rule (marketing.md):** Never clone identical content across channels. Same kernel, three distinct expressions.

---

## 8. Forbidden-Tone Checklist

Before publishing any public artifact, verify against this checklist. Every item traces to either brand.md or T4 anti-pattern research.

- [ ] No "excited to announce" or celebration-without-proof openers. *[brand.md: no empty self-description; T4 §4.2]*
- [ ] No AI-hype language ("game-changer," "revolutionary," "the future of X"). *[brand.md: "never generic AI hype"; T4 §2.2]*
- [ ] No founder-LARP framing ("building my startup," "CEO of my career"). *[brand.md: forbidden framing; marketing.md: anti-pattern]*
- [ ] No self-deprecating "just a junior" or apology framing. *[brand.md: "never 'just another junior'"; T4 §5.5]*
- [ ] No numbered emoji lists (1️⃣ 2️⃣ 3️⃣). *[T4 §4.2: AI-tell pattern]*
- [ ] No "Thoughts?" or "Agree?" as CTA. *[T4 §4.2: generic engagement bait; S5: AI-tell]*
- [ ] No "Follow me for more tips." *[T4 §2.2: algorithmically penalized; marketing.md: no generic self-promotion]*
- [ ] No content without linked evidence. *[marketing.md: "evidence over adjectives"; brand.md: no empty self-description]*
- [ ] No identical text across channels. *[marketing.md: explicit anti-pattern]*
- [ ] No morning-routine / productivity-manifesto content. *[T4 §2.2: zero technical signal]*
- [ ] No external links in post body (LinkedIn only). *[T4 §5.1: 60% reach penalty; place in first comment]*
- [ ] Sarcastic edge used at most once per post, targeting systems not people. *[brand.md: "controlled sarcastic edge"; §4.3 above]*

---

*Every rule in this style book traces to a documented source: brand.md, marketing.md, user_data.md, or a specific entry in the T4 research report. No rule exists without provenance.*

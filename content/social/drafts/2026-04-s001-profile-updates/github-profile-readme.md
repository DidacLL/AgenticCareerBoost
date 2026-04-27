# GitHub Profile README — Ready-to-Paste Draft

- **Sprint**: S-001 / T5
- **Agent**: CommunityManager
- **Date**: 2026-04-20
- **Target**: `DidacLL/DidacLL` repo → `README.md`
- **Inputs**: T3 profile audit, T4 positioning synthesis, brand.md, style-book.md

---

## Instructions

Copy everything below the `--- BEGIN README ---` line and paste it as the full contents of `DidacLL/DidacLL/README.md`. Remove the current content entirely.

After pasting, update the repo settings:
- **Topics**: Remove `config`, `github-config`. Do not add new topics (profile READMEs don't need them).
- **Description**: `Profile README` (or leave blank).

---

## --- BEGIN README ---

```markdown
# Dídac Llorens

Software engineering student (UOC, ML/AI specialization — graduating Feb 2027) building model-agnostic agentic systems and LaTeX tooling. 15 years of regulated-industry operations. Based in Barcelona.

## Current Focus

- **Agentic system design** — path-based multi-agent orchestration with formal truth hierarchies, inspectable architecture, and zero vendor lock-in
- **ML/AI engineering** — applied machine learning through UOC specialization coursework and portfolio projects
- **LaTeX tooling** — custom document classes, package ecosystems, and automated build pipelines for academic and engineering documentation

## Projects

| Project | Description | Stack |
|---------|-------------|-------|
| [AgenticCareerBoost](https://github.com/DidacLL/AgenticCareerBoost) | Path-based, model-agnostic multi-agent operating system — 6 agent roles, 7 workflows, formal reports, public site | Markdown, LaTeX, Python, GitHub Pages |
| [P3CTeX](https://github.com/DidacLL/P3CTeX) | Custom LaTeX document class and package ecosystem for academic document production — with test suites and agentic development workflow | LaTeX (expl3), latexmk |
| [p3cTeX-UMLST](https://github.com/DidacLL/p3cTeX-UMLST) | Extracted UML diagram and code listing packages from P3CTeX | LaTeX (pgf-umlcd, listings) |

## Tech & Interests

`Python` · `Java` · `Spring Boot` · `Kotlin` · `LaTeX` · `SQL` · `Linux` · `Git` · `Docker` · `REST APIs`

Systems design · ML/AI · Agentic workflows · Technical documentation · Resource-aware engineering · Open source

## Background

Before engineering: 15 years in banking and insurance operations — team leadership, complex case resolution, regulatory compliance, stakeholder management. I treat process discipline and failure-mode thinking as engineering skills, not soft skills.

Currently completing a CS degree with ML/AI specialization at UOC (Feb 2027). Previous training: Java Backend (IronHack), Android/Kotlin (F. Francisco Puerto), FullStack React (ITAcademy), Linux Admin (PUE).

## Contact

- LinkedIn: [linkedin.com/in/didacllorens](https://www.linkedin.com/in/didacllorens/)
- Site: [didacll.github.io/AgenticCareerBoost](https://didacll.github.io/AgenticCareerBoost/)
- Location: Barcelona, Catalonia
```

## --- END README ---

---

## Design Decisions

| Decision | Rationale | Source |
|----------|-----------|--------|
| No emoji anywhere | brand.md tone: "technical, disciplined, direct." Profile README emoji overload is an anti-pattern (T3 §2.2). | brand.md, T3 §2.2 |
| No stats widgets or visitor badges | These add visual noise without substantive signal. Recruiters do not care about streak counters. | T3 §2.2, style-book.md §5 |
| Table format for projects | Dense, scannable, recruiter-optimized. Shows project name, purpose, and stack in one glance. | style-book.md §2 (recruiter audience = 55% weight) |
| No VladScv reference | Removed per T3 §2.2 recommendation — unexplained alt account reference confuses identity chain. | T3 §2.2, §6.2 |
| No legacy site link | The legacy site is a net negative (T3 §5). All links now point to AgenticCareerBoost site. | T3 §5, T4 §5.4 |
| Background section included | Reframes the 15 years as an asset, not a gap. Uses the same framing as LinkedIn About section but adapted for GitHub's technical audience (denser, less narrative). | T4 §5.2 C3, marketing.md: "do not clone identical content across channels" |
| ML/AI mentioned in first line | Aligns with Primary Angle A (ML/Data Engineering). The degree and specialization are the strongest credential differentiators. | T4 §2 |
| MemPalace contribution not included | Pending verification of contribution scope (T3 §2.5). Add when confirmed. | T3 §2.5, `[TODO: verify and add if substantive]` |

## Alternative: Angle B Lead (Agentic Systems Forward)

If the user prefers Angle B positioning, replace the first line with:

```markdown
Software engineering student (UOC, ML/AI — Feb 2027) designing model-agnostic agentic systems. 15 years of regulated-industry operations reframed as engineering discipline. Barcelona.
```

And reorder "Current Focus" to lead with agentic system design (already first in the default version — no change needed).

---

## Checks

- [x] Tone consistent with brand.md — technical, disciplined, direct
- [x] No emoji overload
- [x] No stats widgets or visitor badges
- [x] Clean markdown formatting
- [x] Reflects T4 positioning (Primary: ML/Data, Secondary: Agentic Systems)
- [x] No legacy site link
- [x] No VladScv reference
- [x] Every claim links to evidence or marked `[TODO]`
- [x] Content adapted for GitHub (denser than LinkedIn, no narrative padding)

---

*Draft produced by CommunityManager agent, S-001 T5. Requires user review before pushing to DidacLL/DidacLL repo.*

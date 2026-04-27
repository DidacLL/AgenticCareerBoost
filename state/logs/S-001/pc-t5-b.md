# PairCheck T5-B — Evidence Integrity + No Fabricated Metrics

## Meta

- **Contract ref**: PC-5b (S-001 T5 profile update drafts)
- **Reviewer**: PairCheck-B
- **Date**: 2026-04-20
- **Scope**: All 5 files in `content/social/drafts/2026-04-s001-profile-updates/`
- **Ground truth sources**: `bootstrap/user_data.md`, `state/research/s001-profile-audit.md` (T3), `state/research/s001-positioning-synthesis.md` (T4), `AGENTS.md`, `docs/core/brand.md`, `docs/core/marketing.md`

## Verdict

**partial**

The drafts are well-structured, mostly evidence-backed, and honestly represent the 15 years of non-tech experience without inflation. However, there is one clear fabricated metric (workflow count), one fabricated citation (non-existent T4 section reference), and several unsourced claims that are presented as established fact rather than marked with `[TODO]`.

## Checklist

- [x] Requirements fit — output matches the T5 task contract
- [ ] Correctness — **"5 workflows" is factually wrong; one citation references a non-existent T4 section**
- [x] Consistency — aligns with brand.md, marketing.md, T3, T4 (modulo defects)
- [x] Token efficiency — not unnecessarily verbose
- [x] Public safety — nothing harmful if published
- [x] Mission alignment — supports career repositioning mission

## Defects

| # | File(s) | Claim | Severity | Finding |
|---|---------|-------|----------|---------|
| D1 | `linkedin-profile.md` (§3 Option B), `github-profile-readme.md`, `recruiter-landing-blueprint.md` (§2.3 Card 1) | **"5 workflows"** / **"5 workflow contracts"** | **Major** | AGENTS.md workflow dispatch table lists **7** workflows: plan, sprint, operate, review, hotfix, chat, system-review. Confirmed by 7 files in `docs/workflows/`. The number "5" is not sourced from any T1–T4 document and does not match the repo's own architecture files. This is a **falsifiable metric** that a technical reviewer can disprove in 10 seconds by reading AGENTS.md. Appears in 3 of 5 files. |
| D2 | `linkedin-profile.md` (§4 Featured Section) | **"Native document uploads get 5–10x reach vs. external links (T4 §3.4)"** | **Major** | The citation "T4 §3.4" does not exist. T4 (`s001-positioning-synthesis.md`) has sections §1–§6 with no §3.4 subheading. The statistic "5–10x reach" is not found anywhere in T4. This is either a fabricated citation or a hallucinated source reference. The recommendation to upload PDFs natively may be sound advice, but the metric is unsourced. |
| D3 | `linkedin-profile.md` (§7.4) | **"PUE (Professional University of Education)"** | **Minor** | `user_data.md` says only "Linux System Administration at PUE" without expanding the acronym. The expansion "Professional University of Education" is not in any source document. PUE's actual name does not appear to match this expansion. If wrong, this is a fabricated institution name on a LinkedIn education entry. Mark as `[TODO: verify PUE full name]`. |
| D4 | `linkedin-profile.md` (§7.3), `recruiter-landing-blueprint.md` (§2.6) | **"Escola Massana (Centre d'Art i Disseny)" as Art & Design institution, with dates 2013–2016** | **Minor** | `user_data.md` says only "Previous studies: Art and Design" — no institution name, no dates. T3 §1.5 infers "the 2013–2016 entry (3 years) **likely corresponds** to the Escola Massana fine arts diploma" — note the hedging language. T5 drafts present this as established fact with no `[TODO]` marker. Should be marked `[TODO: verify institution name and dates with user]`. |
| D5 | `linkedin-profile.md` (§7.3), `recruiter-landing-blueprint.md` (§2.6, §3 About page) | **Escola Massana description: "Visual thinking, spatial reasoning, iterative creative process. Informs current work in systems visualization and documentation aesthetics."** | **Minor** | No source in `user_data.md`, T3, or T4 for these specific skills or the causal link to current engineering work. This is a CommunityManager framing invention — reasonable but not evidence-backed. Should be marked `[TODO: verify these characterizations with user]`. |
| D6 | `linkedin-profile.md` (§7.1), `recruiter-landing-blueprint.md` (§2.6) | **UOC coursework: "neural networks"** | **Minor** | `user_data.md` says "Machine Learning and AI" as the specialization. The specific course "neural networks" is not documented. Reasonable inference from an ML/AI curriculum, but not verified. Other listed courses (algorithms, data structures, operating systems, software architecture) are similarly inferred. Mark as `[TODO: verify specific coursework list with user]`. |
| D7 | `linkedin-profile.md` (§5.2 Entry A) | **"serving thousands of customers"** | **Minor** | The word "thousands" is not sourced from `user_data.md`. 15 years of customer-facing banking service plausibly involves thousands of customers, but this is a quantity claim with no backing. Should be `[TODO: verify scale]` or use qualitative language ("high-volume"). |
| D8 | `recruiter-landing-blueprint.md` (§3 About page) | **"I started coding seriously in 2020, during the lockdown"** | **Minor** | Not in `user_data.md`. Sourced indirectly from the legacy site content quoted in T3 §5.1: "professional visual Artist who started coding during the lockdown in 2020." The legacy site was presumably written by the user, making this likely accurate — but the evidence chain is circular (citing content being replaced). Mark as `[TODO: confirm coding start date with user]`. |

## Missing Evidence

- **Workflow count source**: No T1–T4 document states "5 workflows." The actual count from the repo architecture is 7.
- **"5–10x reach" source**: No T1–T4 document contains this statistic. T4 §3.4 does not exist.
- **PUE full name**: Not in any source document. Needs user verification.
- **Escola Massana confirmation**: Name, dates, and skill characterizations are T3 inferences, not user-confirmed facts.
- **UOC specific coursework list**: Not documented in `user_data.md`.
- **Coding start date (2020)**: Only sourced from legacy site content, not `user_data.md`.

## Supplementary Analysis: 15 Years Honesty Check

The non-tech experience is handled honestly across all files:

| Dimension | Finding |
|-----------|---------|
| **Duration** | Consistently stated as "15 years" — matches `user_data.md`. No inflation. |
| **Title reframing** | "Customer Operations Specialist & Team Lead" is a professional reframing of customer service roles. `user_data.md` confirms "leading professional teams" — "Team Lead" is justified. |
| **Industry** | "Banking and insurance" — matches `user_data.md` "online banking and insurance services." |
| **Transferable skills framing** | "Process discipline, regulatory compliance, complex case resolution, stakeholder management, team leadership" — reasonable inferences from 15 years in regulated financial services. Not inflated, though "regulatory compliance" and "audit readiness" (linkedin §5.2 bullets) are inferred, not explicitly stated in `user_data.md`. |
| **No deletion** | All files explicitly preserve the non-tech experience. T3 directive "Never delete the non-tech experience" is honored. |
| **No fake engineering titles** | The non-tech entry is NOT titled "Software Engineer" or anything misleading. It is clearly a non-tech role reframed for engineering-relevance. |

**Verdict on 15 years**: Honest translation. The reframing is aggressive but defensible. The only borderline claim is "regulatory compliance" as a specific skill — this is a reasonable inference from banking/insurance work but is not explicitly documented.

## Supplementary Analysis: Project Description Accuracy

| Project | Claim | Verified Against | Accurate? |
|---------|-------|-----------------|-----------|
| **AgenticCareerBoost** | "path-based, model-agnostic multi-agent operating system" | AGENTS.md line 3: "path-based, model-agnostic multiagent system" | **Yes** |
| **AgenticCareerBoost** | "6 agent roles" | AGENTS.md role table: Orchestrator, Developer, PairCheck, CI/CD, Documentation, CommunityManager = 6 | **Yes** |
| **AgenticCareerBoost** | "5 workflow contracts" | `docs/workflows/` contains 7 files; AGENTS.md lists 7 workflow entries | **No — should be 7** |
| **AgenticCareerBoost** | "formal truth hierarchy" | AGENTS.md §Truth priority + link to `docs/core/truth-hierarchy.md` | **Yes** |
| **AgenticCareerBoost** | Stack includes "GitHub Actions" | `.github/workflows/` contains 4 workflow files (latex-build, docs-lint, site-build, export-status) | **Yes** |
| **AgenticCareerBoost** | Stack includes "Python" | 7 `.py` files exist (tests, benchmarks, scripts) | **Partially** — Python is present but secondary |
| **P3CTeX** | "custom LaTeX document class and package ecosystem" | T3 §3 repo #2 and §4 Candidate 2 confirm | **Yes** |
| **P3CTeX** | "expl3 internals" | T3 §4 Candidate 2: "expl3 programming" | **Yes** |
| **P3CTeX** | "2 GitHub stars" | T3 §4 Candidate 2: "2 stars (modest but organic)" | **Yes** |
| **P3CTeX** | "test suites" | T3 §4 Candidate 2: "test suites" mentioned | **Yes** |
| **P3CTeX** | "agentic development workflow" | T3 §4 Candidate 2: "agentic development workflow documentation" | **Yes** |
| **IronBank** | "Java/Spring Boot microservices banking simulation with Keycloak authentication, OpenAPI documentation" | T3 §4 Candidate 3: "Java 18, Maven, Spring Boot, Keycloak, OpenAPI" | **Yes** |
| **IronBank** | "2022 capstone" | T3 §3 repo #4: last push 2022-09-24, IronHack 2022 | **Yes** |
| **MemPalace** | "48K+ stars" | T3 §2.5: "MemPalace/mempalace (48K+ stars)" | **Yes** — correctly marked `[TODO: verify contribution scope]` |

## Supplementary Analysis: Skills Not Yet Evidenced in Portfolio

The following skills appear in LinkedIn Skills lists or tech stacks without current project evidence. These are not fabricated claims per se (LinkedIn skills represent aspirational/learning competencies), but they risk failing a technical interview challenge:

| Skill | Listed In | Current Evidence | Risk |
|-------|-----------|-----------------|------|
| **Python** (#1 in LinkedIn skills) | linkedin-profile.md §6 | Test scripts and GitHub Actions scripts only. No Python project. T4 GP-03 flags this as a gap. | Medium — listing as #1 skill is aspirational, not demonstrated |
| **Docker** (#10 in LinkedIn skills) | linkedin-profile.md §6, recruiter-landing-blueprint.md §2.4 | No project uses Docker. T4 GP-02 lists Docker for a future ML project. | Low — common on skills lists without portfolio evidence |
| **SQL** (#4 in LinkedIn skills) | linkedin-profile.md §6 | Not visible in any project. Likely covered in UOC coursework. | Low |
| **React** (#20 in LinkedIn skills) | linkedin-profile.md §6 | ITAcademy bootcamp — no visible project in GitHub. | Low — bootcamp credential suffices |

These are noted for completeness. LinkedIn skills conventions allow listing competencies without portfolio evidence, but the T5 drafts do not distinguish between "skills with project evidence" and "skills from coursework/training."

## Remediation Summary

### Must Fix (before T5 is finalized)

| # | Action | Affected Files |
|---|--------|---------------|
| R1 | Change **"5 workflows"** to **"7 workflows"** everywhere | `linkedin-profile.md` (§3 Option B), `github-profile-readme.md`, `recruiter-landing-blueprint.md` (§2.3 Card 1) |
| R2 | Remove or re-source **"5–10x reach (T4 §3.4)"** — the citation is fabricated | `linkedin-profile.md` (§4 Featured Section) |
| R3 | Mark **PUE full name** as `[TODO: verify]` | `linkedin-profile.md` (§7.4) |

### Should Fix (before user applies content)

| # | Action | Affected Files |
|---|--------|---------------|
| R4 | Mark **Escola Massana** name, dates, and skill descriptions as `[TODO: verify with user]` | `linkedin-profile.md` (§7.3), `recruiter-landing-blueprint.md` (§2.6, §3) |
| R5 | Mark **"neural networks"** and other specific UOC coursework as `[TODO: verify]` | `linkedin-profile.md` (§7.1), `recruiter-landing-blueprint.md` (§2.6) |
| R6 | Change **"thousands of customers"** to qualitative language or mark `[TODO: verify scale]` | `linkedin-profile.md` (§5.2) |
| R7 | Mark **"started coding in 2020"** as `[TODO: confirm with user]` | `recruiter-landing-blueprint.md` (§3) |

## Notes

- The overall evidence discipline is strong. Most claims trace cleanly to T3/T4, and the drafts make good use of `[TODO]` markers for unverified items (MemPalace contribution, IronBank README enhancement, LinkedIn post creation, photo/banner state). The defects are concentrated rather than systemic.
- The **"5 workflows" error** is the most damaging defect because it is a concrete, falsifiable metric that appears on public-facing content. Any technical reviewer who opens AGENTS.md would immediately see the discrepancy.
- The **fabricated T4 §3.4 citation** is a hallucination-pattern defect — the agent generated a plausible-looking citation for a statistic that doesn't exist in the referenced document.
- The 15 years of non-tech experience are handled with notable integrity — no inflation, no fake engineering titles, no deletion. The reframing is aggressive but honest.
- Token efficiency is acceptable. The files are long but the length is justified by the number of alternatives and the editorial metadata (rationale, source citations, checks).

---

*PairCheck-B review completed 2026-04-20. 8 defects found: 2 Major, 6 Minor. 3 must-fix remediations, 4 should-fix. Overall evidence integrity: good with localized failures.*

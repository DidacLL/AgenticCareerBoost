# PairCheck output — PC-6b: Content Alignment with T1–T4

## Meta

- **Contract ref**: T6 (LaTeX report) — PC-6b (content alignment)
- **Reviewer**: PairCheck-B
- **Date**: 2026-04-20
- **Artifact under review**: `content/reports/tex/sprints/s001-profile-audit-positioning.tex`
- **Source documents**:
  - T1: `state/research/s001-bcn-it-market.md`
  - T2: `content/social/research/2026-04-bcn-hiring-discourse.md`
  - T3: `state/research/s001-profile-audit.md`
  - T4: `state/research/s001-positioning-synthesis.md`

## Verdict

**partial**

The report is overwhelmingly faithful to the source research. All key statistics, salary ranges, age brackets, and employer names are accurate. The four positioning angles and their ranking are consistent with T4. However, there are a small number of source-attribution errors, one omitted con from a positioning angle, and selective omission of recruiter-intelligence findings from T2 §5 that would strengthen the report.

## Checklist

- [x] Requirements fit — output matches the task contract
- [x] Correctness — technically sound (with minor defects below)
- [ ] Consistency — aligns with existing repo artifacts (source-tag mismatch on R36/R37)
- [x] Token efficiency — not unnecessarily verbose
- [x] Public safety — nothing harmful if published
- [x] Mission alignment — supports `docs/core/mission.md`

## Chapter-by-Chapter Alignment Audit

### Chapter 2 (Barcelona Market) vs T1

**Statistics verified (all correct):**

| Claim in report | T1 source location | Match? |
|---|---|---|
| ~150,000 workers, 12,000+ companies in 22@ [S01] | T1 §1 line 1 | ✓ |
| VC fell 43%, deal size rose €3.2M→€4.8M | T2 §2.2 (not T1) | ✓ data, ⚠ sourced from T2 not T1 |
| Seed funding declined 34% | T2 §2.2 | ✓ |
| 180–240 day time-to-fill for senior ML | T2 §2.2 | ✓ |
| ML/Data Eng composite 4.2/5 | T1 §5 | ✓ |
| Agentic/AI Eng composite 4.3/5 | T1 §5 | ✓ |
| Backend Eng composite 2.3/5 | T1 §5 | ✓ |
| Data & AI salaries grew 10% YoY [S04] | T1 §1 ML row | ✓ |
| Dynatrace 180 positions [S07] | T1 §3 row 3 | ✓ |
| 179 DevOps openings, 26 entry-level [S09] | T1 §1 DevOps row | ✓ |
| Backend demand fell 7% in 2025 [S04] | T1 §1 Backend row | ✓ |
| All 6 salary bands in Table 2.2 | T1 §2 table | ✓ (all ranges match exactly) |
| Career-changer range €24K–€30K | T1 §2 | ✓ |
| 18-month trajectory €32K–€40K | T1 §2 | ✓ |
| BCN 5–10% above Spanish avg, 20–40% below MAD | T1 §2 | ✓ |
| Hybrid 60–65%, On-site 20–25%, Remote 15–20% | T1 §4 | ✓ |
| 70% of 22@ prefer hybrid, 91% flexibility [S25] | T1 §4 | ✓ |

**Employer shortlist changes (editorial, not error):**

The Tier 1 table replaces King (#5 in T1) and Satellogic (#10 in T1) with CaixaBank Tech (T2 §2.3) and Red Points (T2 §2.3). This is arguably a better list given T2's evidence that King hires almost exclusively at senior level, but the substitution is not flagged in the report text. See Defect #3.

**Omissions from T1 (minor):**

- T1 outlier employers paying above market (Alan €45K–€48K, Glovo equity, N26, Dynatrace Austrian/US scales) — omitted from salary section.
- T1 Tier 2 employers (Manychat, Payhawk, TravelPerk, Factorial, Glovo, Amazon, CVC, Adevinta) — omitted. Acceptable for a summary report.
- T1 "entry-level job postings in Spain fell 34% vs. 2020 [S29]" — omitted.
- T1 Frontend Developer and QA Automation salary rows — omitted from table (less relevant to positioning).

### Chapter 3 (Social/Legal) vs T2

**Statistics verified (all correct):**

| Claim in report | T2 source location | Match? |
|---|---|---|
| Manfred age distribution (14/26/33/13/13%) | T2 §1.1 table | ✓ |
| 240+ managed hires (2021–2025) | T2 §1.1 | ✓ |
| Mean hiring age 37, max 58 | T2 §1.1 | ✓ |
| Manfred quote: "Solamente un 13%..." | T2 §1.1 | ✓ |
| Spain 55+ unemployment 11.2% vs FR 5.2% / DE 2.1% | T2 §1.2 | ✓ |
| Andrea Rosales, IN3, UOC — "old at 35+" | T2 §1.3 | ✓ |
| CaixaBank Tech 500 hires/Q1 2025 [R7] | T2 §2.3 | ✓ |
| Glovo 400+ engineers, Gas/Deep Dive/Glownership [R8] | T2 §2.3 | ✓ |
| Factorial 20–40 deploys/day [R9] | T2 §2.3 | ✓ |
| Typeform "Swarms", rejected Spotify Model [R10] | T2 §2.3 | ✓ |
| BSC-CNS agentic AI + LLM-RAG role [R11] | T2 §2.3 | ✓ |
| Red Points B Corp, Junior ML Eng, multimodal AI [R14] | T2 §2.3 | ✓ |
| EU AI Act: high-risk classification [R16] | T2 §3.1 | ✓ |
| Compliance costs €150K–€500K per scale-up | T2 §3.1 | ✓ |
| Ley 10/2021 remote work threshold ≥30% | T2 §3.2 | ✓ |
| EU Pay Transparency Directive 2023/970, deadline 7 June 2026 [R20, R21] | T2 §3.3 | ✓ |
| Salary history prohibition | T2 §3.3 | ✓ |
| Més Talent Cat €15M | T2 §3.5 | ✓ |
| Forma i Insereix €7.5M | T2 §3.5 | ✓ |
| Kit Digital €3.067B, concluded Oct 2025 | T2 §3.5 | ✓ |
| Seed-funding decline −34% YoY | T2 §2.2 | ✓ |

**Source-attribution error (Defect #1):**

The report states "Ironhack Barcelona reports 94% employment at 180 days [R36, R37]" — but in T2's source registry, R36 = Adalab (90% insertion) and R37 = MigraCode Barcelona. The Ironhack 94% stat appears in T2 §4.2/§4.4 without a specific R-number. The report assigns the wrong source tags.

**Omissions from T2 (moderate aggregate significance):**

| T2 section omitted | Content | Severity |
|---|---|---|
| §1.4 AEPI + ARA.cat ageism reports | Additional age-discrimination evidence (AEPI, ARA.cat Catalan press) | Minor |
| §1.5 Career-change success stories | 5 named career changers (ages 30–40+) who transitioned successfully | Minor |
| §2.4 Top hiring by volume table | Ebury 284, Fever 245, Neoris 240, Esri 217, Okta 203, Stripe 175 | Minor |
| §3.4 GDPR impact on AI hiring | AEPD guidelines, recruitment AI market projection | Minor |
| **§5.1 CV red flags** | **RemoDevs data: responsibilities vs achievements, job hopping, buzzword stuffing** | **Moderate** |
| **§5.2 GitHub/portfolio signals** | **87% recruiters check GitHub, 40% more callbacks, 73% GitHub compensates for education** | **Moderate** |
| **§5.3 Hiring manager competencies** | **System design thinking, product understanding, AI tool fluency, tech debt** | **Minor** |
| **§5.4–§5.5 Green/red flag lists** | **Quantified achievements, T-shaped profile, video walkthroughs, birth date warning** | **Moderate** |

T2 §5 (recruiter intelligence) contains actionable operational data that is **not systematically represented** anywhere in the report. Some elements surface in the profile audit chapter and action plan, but the synthesis of what recruiters explicitly seek and reject is absent as a coherent section. This is the most significant content omission.

### Chapter 4 (Profile Audit) vs T3

**All scores and findings verified correct:**

| Report element | T3 match? |
|---|---|
| LinkedIn field-by-field scores (1/5, 1/5, 0/5, 2/5, 3/5, 2/5, 0/5, 1/5) | ✓ exact match with T3 §1.11 |
| Overall ~25% completeness | ✓ |
| GitHub bio: empty (Critical) | ✓ T3 §2.1 |
| Profile README: 4 lines, "VladScv" (Critical) | ✓ T3 §2.2 |
| All 12 repo scores (README, Commits, Showcase) | ✓ every score matches T3 §3 table |
| All 12 repo verdicts (Enhance/Archive/Rewrite) | ✓ |
| Cross-cutting: 4/12 self-deprecating, 6/12 no/single-line README, 4/12 no license | ✓ T3 §3 cross-cutting |
| Legacy site: "90s younger", "looking for a company", net negative | ✓ T3 §5.1, §5.8 |
| Cross-surface consistency: 6 dimensions, all "No" | ✓ T3 §6.1 |

Chapter 4 is the most faithful chapter — essentially a direct condensation of T3 with no discrepancies.

**Omissions from T3:**

- T3 §2.5: MemPalace contribution details (48K+ stars) — mentioned only in Ch 7 Open Decisions, not in audit chapter.
- T3 §5.2–§5.8: Detailed legacy site technical issues (SEO, AI-readable metadata, mobile responsiveness, accessibility, code structure) — summarized but not enumerated.
- T3 §6.2 #9: Bootcamp credential inconsistency across surfaces — not explicitly called out.

### Chapter 5 (Positioning) vs T4

**Angle rankings and allocations verified correct:**

| Report element | T4 match? |
|---|---|
| Angle A primary (60%) | ✓ T4 §2 |
| Angle B secondary (20%) | ✓ T4 §2 |
| Angle C tertiary (10%) | ✓ T4 §2 |
| Angle D fallback (10%, product co. only) | ✓ T4 §2 |

**Angle A pros/cons: 5 pros, 4 cons — T4 has 6 pros, 4 cons.**

- Missing pro from T4: "AgenticCareerBoost demonstrates applied ML/AI systems thinking beyond coursework" — however, this is covered in Angle B's discussion. Acceptable editorial decision.
- All 4 cons match T4 exactly. ✓

**Angle B pros/cons: 4 pros, 4 cons — T4 has 6 pros, 5 cons.**

- Missing T4 pro #5: "Path-based architecture demonstrates systems design thinking" — implicitly covered.
- Missing T4 pro #6: "Meta-nature of the project is a conversation starter" — omitted. Minor.
- **Missing T4 con #5: "No production deployment of any agentic system; the project is a portfolio artifact, not a deployed service."** This is a distinct weakness from con #3 (single project). See Defect #2.

**Angle C pros/cons: 4 pros, 4 cons — T4 has 7 pros, 6 cons.**

- Missing pros: investigation priority alignment, Catalan language advantage, BSC hires RE1. Minor condensation.
- Missing cons: "Cannot spray-and-pray", on-site presence typically required. Minor.

**Gap-to-remediation map: All 5 GP items match T4 §3 critical-path gaps. ✓**

**Rejection list: All 6 categories match T4 §4. ✓**

- Body-shop consulting ✓
- Generic CRUD backend ✓
- Unpaid internships ✓
- Relocation outside Barcelona ✓
- Below €22K ✓
- Pre-seed equity-only ✓

**T4 elements omitted:**

- §4 "Employers to Deprioritize" table (King, SEAT:CODE, Amazon, Manychat) — not in report.
- §4 Decision Heuristic for Edge Cases — converted to TikZ flowchart (creative editorial decision, consistent in logic).
- §5.5 Cross-surface consistency verification checklist — omitted.
- §6 Evidence Traceability Matrix — replaced by source registry appendix.

### Chapters 1, 6, 7 (Exec Summary, Actions, Conclusions)

All claims in these synthesis chapters trace back to T1–T4 findings already verified above. No unsourced claims found. The action plan IDs (GP-01 through GP-05, GS-01 through GS-06, GN-01 through GN-05, C1–C3, M2–M6) are consistent with T3 priority matrix and T4 gap map.

### Source Registry (Appendix)

Spot-checked 20 of ~30 source entries against T1 §6 and T2 §6. All URLs and descriptions match their source documents.

## Defects

| # | Description | Severity |
|---|-------------|----------|
| 1 | **Source-tag mismatch [R36, R37]**: Chapter 3 §Cultural Hiring Patterns cites "Ironhack Barcelona reports 94% employment at 180 days [R36, R37]" but R36 = Adalab and R37 = MigraCode in T2's source registry. The Ironhack 94% stat in T2 §4.4 lacks a dedicated R-number. Fix: either assign a correct source tag for the Ironhack stat or replace with Adalab's 90% stat and cite R36 correctly. | **Moderate** |
| 2 | **Angle B con #5 omitted**: T4 lists 5 cons for Angle B (Agentic Systems). The report includes only 4, dropping "No production deployment of any agentic system; the project is a portfolio artifact, not a deployed service." This is distinct from con #3 (single project = thin evidence): con #3 is about breadth, con #5 is about deployment maturity. The omission weakens the risk assessment for Angle B. | **Minor** |
| 3 | **Employer Tier 1 substitution not flagged**: The named employer table (Table 2.4) drops King and Satellogic from T1's Tier 1 and adds CaixaBank Tech and Red Points from T2. While editorially defensible, the change is not noted. A reader comparing the report to T1 would see a discrepancy. | **Minor** |
| 4 | **22@ company count discrepancy unresolved**: T1 states "12,000+ companies" [S01], T2 states "11,000 companies" [R6] — both citing KiTalent. The report uses T1's "12,000+" without noting the variance. | **Trivial** |

## Missing evidence

- **T2 §5 recruiter intelligence (CV red/green flags, GitHub signal data, hiring manager competencies)**: This is the most significant systematic omission. The data is actionable and directly supports the action plan's recommendations (e.g., why archive dead repos, why quantify achievements, why consistent GitHub activity matters). Consider adding a section in Chapter 3 or Chapter 4, or at minimum referencing the key statistics (87% recruiters check GitHub [R29], 40% more callbacks with active profiles [R29], 90-second initial review window [R40]) in the profile audit chapter.
- **T2 §1.5 career-change success stories**: Five documented transitions (ages 30–40+) that could strengthen the age-narrative section. Not essential but would add concrete precedent.
- **T4 §4 "Employers to Deprioritize" list** (King, SEAT:CODE, Amazon, Manychat): The rejection list is present but the softer "deprioritize" category is absent.
- **T4 §5.5 cross-surface verification checklist**: Operational but useful for the sprint closure.

## Notes

- **Overall quality is high.** The report accurately synthesizes 4 research documents (34 + 40 + ~50 + ~50 sections of evidence) into a coherent 1037-line LaTeX document. The vast majority of statistics, salary ranges, employer names, and positioning logic are faithfully reproduced.
- **The source-tag error (Defect #1) is the only factual accuracy issue.** All other defects are omissions or editorial choices.
- **Token efficiency is good.** The report condenses ~4000 lines of source material into a readable narrative without significant redundancy. Some condensation (Angle C from 7→4 pros) is aggressive but defensible.
- **Defect #1 should be fixed before PDF compilation** — the R36/R37 tags will confuse any reader who follows the source registry. A simple fix: cite the Ironhack stat with a footnote or add it to the T2 source table as R41 (or use the Ironhack URL directly).
- **Defect #2 is easy to fix** — add a 5th row to Table 5.2 (Angle B cons): "No production deployment; project is a portfolio artifact, not a deployed service [T3 §4]."

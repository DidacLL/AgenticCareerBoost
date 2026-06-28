# S-001 Positioning Synthesis + Option Map

- **Date**: 2026-04-20
- **Sprint**: S-001
- **Agent**: Developer / strategy (T4)
- **Inputs**: T1 (s001-bcn-it-market.md), T2 (2026-04-bcn-hiring-discourse.md), T3 (s001-profile-audit.md), user_data.md, brand.md, style-book.md
- **Subject**: Dídac Llorens — strategic positioning for first IT role, Barcelona

---

## Executive Summary

Three research reports converge on one conclusion: Dídac's strongest competitive advantage is **not** his Java bootcamp background — it is the combination of a formal CS degree with ML/AI specialization, 15 years of regulated-industry process discipline, and a portfolio of systems-level work (AgenticCareerBoost, P3CTeX) that no other junior candidate in the Barcelona market can replicate. The data also shows that at 36 he sits in the **peak hiring bracket** (Manfred: 33% of placements are age 36–40), which eliminates the age-anxiety narrative entirely.

The synthesis below presents four positioning angles ranked by strategic value, a gap-to-remediation map, an explicit rejection list, and a profile update strategy. Every recommendation traces to evidence from T1, T2, or T3.

---

## 1. Positioning Angles

### Angle A: "ML/Data Engineering with Domain Depth"

**One-line pitch**: ML engineering candidate with a formal AI specialization, 15 years of regulated-industry experience, and OSS portfolio discipline — not a bootcamp retread.

#### Target Role Families

| Role Family | Evidence (T1) |
|---|---|
| ML / Data Engineer | Composite score 4.2/5; strongest credential differentiation via UOC ML/AI mention; data & AI salaries grew 10% YoY [T1 §1, S04] |
| MLOps Engineer | Extension of ML lane; Wallapop actively hires MLOps [T1 §3] |
| Junior Data Scientist | Overlapping credential requirements; €25K–€35K range [T1 §2] |

#### Pros

| # | Strength | Source |
|---|---|---|
| 1 | UOC CS degree with ML/AI mention is the **single strongest credential differentiator** — most bootcamp grads lack any ML credential | T1 §1 |
| 2 | Competition is significantly lower than backend; fewer candidates hold formal ML qualifications at junior level | T1 §1, T2 §2.2 |
| 3 | Salary floor is the highest among realistic junior lanes (€24K–€32K) | T1 §2 |
| 4 | Fastest-growing demand lane in Barcelona (data & AI grew 10% YoY) | T1 §1, S04 |
| 5 | Banking/insurance domain knowledge creates genuine differentiation at fintech employers (CaixaBank Tech, N26, Payhawk, Ebury) and for EU AI Act compliance work | T2 §2.3, §3.1 |
| 6 | AgenticCareerBoost demonstrates applied ML/AI systems thinking beyond coursework | T3 §4 |

#### Cons

| # | Weakness | Source |
|---|---|---|
| 1 | Degree not conferred until Feb 2027 — some HR systems auto-filter for "completed degree" | T1 §2 |
| 2 | No production ML deployment experience; university projects and portfolio are the only evidence | T1 Appendix |
| 3 | Most ML Engineer postings request Python as primary language; Dídac's strongest language is Java | `[Inference]` from T1 §1 |
| 4 | Senior ML roles (the well-paid ones) require 3+ years or research publications — entry-level ML roles are fewer in absolute numbers than backend | T1 §1, T2 §2.2 |

#### Gap List

| # | Gap | Remediation | Sprint Target |
|---|---|---|---|
| G-A1 | No deployed ML project in portfolio | Build a small end-to-end ML pipeline project: data ingestion → training → serving → monitoring. Use Python, scikit-learn or PyTorch, and a simple deployment (FastAPI + Docker). | S-002 or S-003 |
| G-A2 | Python not visible as primary skill | Add Python-based projects to GitHub; ensure LinkedIn skills list prominently features Python | S-001 (LinkedIn), S-002 (project) |
| G-A3 | No cloud ML experience (AWS SageMaker, GCP Vertex, etc.) | Complete a cloud ML certification or build a project using a free-tier cloud ML service | S-003 or later |
| G-A4 | No Kaggle / competition track record | Optional: submit to 1–2 Kaggle competitions to build public evidence of ML capability | Low priority |
| G-A5 | Degree not yet conferred | Clearly state "UOC CS + ML/AI mention, graduating Feb 2027" on all surfaces; frame as near-completion, not gap | S-001 profile updates |

#### Named Barcelona Employer Targets

| Employer | Why | Role Type | Source |
|---|---|---|---|
| **HP (Sant Cugat)** | Active Junior ML Engineer (GenAI) posting; 0–3 yr requirement | Junior ML Engineer, Graduate AI Engineer | T1 §3, T2 §2.3 |
| **BSC-CNS** | Posts RE1 positions for ML/AI; agentic AI role directly aligned | Junior AI Software Research Engineer | T1 §3, T2 §2.3 |
| **Red Points** | Active Junior ML Engineer posting (multimodal AI: computer vision + NLP) | Junior ML Engineer | T2 §2.3 |
| **Wallapop** | Strong ML/recommendation systems team; MLOps openings | MLOps Engineer | T1 §3 |
| **CaixaBank Tech** | Hiring at scale (500/quarter), AI specialists needed; banking domain overlap is genuine advantage | Data Engineer, AI Specialist | T2 §2.3 |
| **Glovo** | Data engineering and ML for recommendations; Airflow and Aurora MySQL stack | Data/ML Engineer | T2 §2.3 |

#### Fit Against User Priorities

| Priority (user_data.md) | Fit | Notes |
|---|---|---|
| Meaningful / career-building | **5/5** | Direct path to AI/ML career; avoids CRUD trap entirely |
| Technology agnostic | **4/5** | Data pipelines are tool-agnostic by nature [T1 §5] |
| OSS / resource-aware | **3/5** | Some OSS tooling, but many production ML pipelines are proprietary |
| ML / purpose-first AI | **5/5** | Core domain |
| LaTeX / unusual environments | **3/5** | Jupyter and scientific tooling are adjacent but not LaTeX |
| Investigation / problem solving | **5/5** | ML is intrinsically investigation-driven |

#### Regulatory/Social Leverage

- **EU AI Act** (T2 §3.1): ML engineers who understand compliance obligations (data quality controls, event logging, bias audits) are in short supply. Dídac's banking regulatory background + ML credential creates an emerging "AI compliance engineering" hybrid profile — particularly valuable at CaixaBank Tech, N26, Ebury.
- **Pay Transparency Directive** (T2 §3.3): Mandatory salary bands in ML postings (transposition deadline June 2026) will eliminate information asymmetry; prohibition on salary history questions prevents anchoring to non-tech salary.
- **SOC Programs** (T2 §3.5): Més Talent Cat (€15M, levels 4–5 digital training) and SOC-FPOAN (Data Scientist specialty) offer funded training to complement UOC degree. Verify eligibility if registered at SOC.

---

### Angle B: "Agentic Systems Engineer"

**One-line pitch**: Systems engineer building model-agnostic agentic workflows with formal documentation discipline — demonstrated by a live, inspectable, multi-agent operating system.

#### Target Role Families

| Role Family | Evidence (T1) |
|---|---|
| Agentic / AI Engineering | Composite score 4.3/5 (highest priority alignment) but almost exclusively senior hiring [T1 §1] |
| Platform / Infrastructure | Composite score 4.0/5; leverages systems-aware mindset; less saturated than backend [T1 §1] |
| Developer Tooling | Moderate fit; Dynatrace R&D expansion (180 new positions) [T1 §3, S07] |

#### Pros

| # | Strength | Source |
|---|---|---|
| 1 | AgenticCareerBoost is a **live, public, inspectable system** — the single strongest portfolio artifact for any agentic engineering role in Barcelona | T3 §4 |
| 2 | BSC-CNS has posted a Junior AI Software Research Engineer role focused on **agentic AI development, LLM-RAG systems, workflow orchestration** — direct alignment | T2 §2.3 |
| 3 | Model-agnostic design philosophy differentiates from vendor-locked LangChain-only candidates | user_data.md, T1 §5 |
| 4 | Scores highest on priority alignment (4.3/5 composite) across all role families | T1 §5 |
| 5 | Path-based architecture demonstrates systems design thinking that transcends the "prompt engineer" label | T3 §4 |
| 6 | The meta-nature of the project (using agentic systems to build a career) is a conversation starter with recruiters who value novel thinking | `[Inference]` |

#### Cons

| # | Weakness | Source |
|---|---|---|
| 1 | **Entry barrier is the highest of all angles** — current agentic/AI postings require MSc/PhD or 3+ years production experience (OLX €60–85K, Keysight, NEORIS) | T1 §1 |
| 2 | Market is tiny: very few junior-accessible agentic engineering roles exist in Barcelona as of 2026 | T1 §1 |
| 3 | Risk of being perceived as "AI-hype" if positioning is not disciplined — brand.md explicitly forbids AI-hype framing | brand.md |
| 4 | AgenticCareerBoost is the **only** agentic project; a single project is thin evidence for a specialization claim | `[Inference]` |
| 5 | No production deployment of any agentic system; the project is a portfolio artifact, not a deployed service | T3 §4 |

#### Gap List

| # | Gap | Remediation | Sprint Target |
|---|---|---|---|
| G-B1 | Single agentic project is thin evidence | Build a second, smaller agentic project in a different domain (e.g., automated code review pipeline, document processing agent) | S-003 or later |
| G-B2 | No production deployment | Deploy AgenticCareerBoost outputs publicly (GitHub Pages site, PDF artifacts); document deployment pipeline | S-001/S-002 |
| G-B3 | No RAG implementation visible | Add a RAG-based component to AgenticCareerBoost or build a standalone RAG demo project | S-002 or S-003 |
| G-B4 | No benchmarking/evaluation framework | Publish benchmarks for the agentic system (task completion rates, token costs, quality metrics) | S-002 |
| G-B5 | "Agentic Systems Engineer" is not a standard job title — recruiters may not know how to classify this | Frame as "AI/ML Engineer with agentic systems specialization" in applications; use "Agentic Systems" as differentiator in conversation, not as the job title | S-001 profile updates |

#### Named Barcelona Employer Targets

| Employer | Why | Role Type | Source |
|---|---|---|---|
| **BSC-CNS** | Concrete agentic AI + LLM-RAG role posted | Junior AI Software Research Engineer | T2 §2.3 |
| **HP (Sant Cugat)** | GenAI modelling in AI Lab connected to Palo Alto team | Graduate AI Engineer | T1 §3, T2 §2.3 |
| **Dynatrace** | 180 new engineering positions; developer tooling/observability R&D | R&D Software Engineer | T1 §3 |
| **Worldsensing** | Small team (20 eng), IoT + systems engineering, resource-aware programming | Software Engineer | T1 §3 |

#### Fit Against User Priorities

| Priority | Fit | Notes |
|---|---|---|
| Meaningful / career-building | **5/5** | Cutting-edge domain |
| Technology agnostic | **5/5** | Model-agnostic by definition |
| OSS / resource-aware | **3/5** | Mix of OSS and proprietary tools |
| ML / purpose-first AI | **5/5** | Core domain |
| LaTeX / unusual environments | **3/5** | Novel tooling, but not LaTeX-adjacent |
| Investigation / problem solving | **5/5** | Architecture design is investigation |

#### Regulatory/Social Leverage

- **EU AI Act** (T2 §3.1): Agentic systems that make automated decisions in employment contexts are classified as high-risk. Engineers who understand both the technical implementation AND the regulatory constraints are scarce.
- **Recruiter green flags** (T2 §5): The project satisfies every green flag simultaneously — deployed artifact, consistent GitHub activity, documented architecture decisions, real problem solved, T-shaped depth.

---

### Angle C: "Research Engineer / Applied AI"

**One-line pitch**: CS graduate with ML/AI specialization, investigation-driven mindset, and documented engineering discipline — targeting funded research positions at Barcelona's supercomputing and research ecosystem.

#### Target Role Families

| Role Family | Evidence (T1) |
|---|---|
| Research Engineering (RE1) | Composite score 4.2/5; BSC, i2CAT, CVC, UPC regularly post junior positions [T1 §1] |
| Applied AI Researcher | Adjacent to research engineering; art background + ML creates unique profile for creative AI / computer vision research [T1 §1] `[Inference]` |

#### Pros

| # | Strength | Source |
|---|---|---|
| 1 | CS degree is the minimum requirement — Dídac meets it directly | T1 §1 |
| 2 | Investigation and problem-solving are explicitly stated priorities — research culture is the natural fit | user_data.md |
| 3 | LaTeX is **native** to research environments — P3CTeX demonstrates production-grade LaTeX competence that most candidates cannot match | T3 §4, T1 §5 |
| 4 | Art background + ML mention creates an unusual profile for computer vision, creative AI, or digital humanities research | T1 §1 `[Inference]` |
| 5 | Catalan language advantage at i2CAT, UOC IN3, and Eurecat | T1 §3, T2 §2.3 |
| 6 | BSC hires RE1 (junior research engineer) positions requiring only a CS degree and English | T1 §3 |
| 7 | BSC AI4Science Fellowships: 158 positions across a 4-year program | T2 §2.3 |

#### Cons

| # | Weakness | Source |
|---|---|---|
| 1 | Research positions are often **project-funded (temporary contracts)** — 1–3 year terms with no guarantee of renewal | T1 §1 |
| 2 | Salary range is mid-market (€25K–€32K junior) with slower growth than private sector | T1 §2 |
| 3 | Research engineering requires specific openings — cannot "spray and pray" | `[Inference]` |
| 4 | No research publications or conference presentations | `[Inference]` |
| 5 | Typically requires on-site presence for lab/infrastructure work, limiting remote flexibility | T1 §4 |
| 6 | Career progression path (RE1 → RE2 → Postdoc → PI) often requires a Master's or PhD for advancement beyond junior level | `[Inference]` |

#### Gap List

| # | Gap | Remediation | Sprint Target |
|---|---|---|---|
| G-C1 | No research publications | Not realistically closable before first job; mitigate by positioning AgenticCareerBoost documentation as "technical report" quality | Ongoing |
| G-C2 | No C++ or HPC experience (relevant for BSC) | If targeting BSC HPC positions specifically, complete a small C++ project or contribute to an HPC-adjacent OSS tool | S-003 or later |
| G-C3 | Art + ML intersection is unexploited | Build a small creative AI project (style transfer, generative art, visualization) that bridges the art background with ML skills | S-003 |
| G-C4 | No visibility in research community | Attend local research meetups (BSC open days, i2CAT events); consider submitting a poster or short paper to a local workshop | S-002+ |

#### Named Barcelona Employer Targets

| Employer | Why | Role Type | Source |
|---|---|---|---|
| **BSC-CNS** | RE1 positions in CS, AI, Earth Sciences; agentic AI role; AI4Science Fellowships | Junior Research Engineer | T1 §3, T2 §2.3 |
| **i2CAT Foundation** | RE1 positions for CS degrees; networking/5G/IoT/AI focus; Catalan institution | Junior Research Engineer | T1 §3 |
| **CVC (Computer Vision Center, UAB)** | Research assistant positions in computer vision; art + ML angle | Research Assistant | T1 §3 |
| **UOC IN3** | Research group posts research assistant positions; alumni network advantage | Research Assistant | T1 §3 `[Inference]` |
| **Eurecat** | Technology center in 22@ with applied research in data analytics and AI | Applied Research Engineer | T1 §3 |
| **UPC** | Research support technician positions (intelligent control, decentralized systems) | Research Support Technician | T1 §3 |

#### Fit Against User Priorities

| Priority | Fit | Notes |
|---|---|---|
| Meaningful / career-building | **5/5** | Investigation-driven by definition |
| Technology agnostic | **3/5** | Often locked to specific frameworks per project |
| OSS / resource-aware | **4/5** | HPC and research tools are frequently OSS |
| ML / purpose-first AI | **4/5** | Many projects are ML-adjacent |
| LaTeX / unusual environments | **5/5** | LaTeX is native; HPC is unusual |
| Investigation / problem solving | **5/5** | Core activity |

#### Regulatory/Social Leverage

- **SOC Més Talent Cat** (T2 §3.5): €15M ESF co-funded program for high-qualification training (levels 4–5) in digital sectors. If Dídac is registered at SOC, this may fund additional research-oriented training.
- **Public sector stability**: Research center contracts, while temporary, are governed by Spanish labor law with stronger protections than private-sector probation periods.

---

### Angle D: "Backend + Platform Engineer with Systems Perspective"

**One-line pitch**: Java/Spring engineer with Linux admin credentials, microservices project evidence, and systems-level documentation discipline — targeting product companies where backend meets infrastructure.

#### Target Role Families

| Role Family | Evidence (T1) |
|---|---|
| Backend Engineering | Medium-high demand but saturating at junior level; composite score 2.3/5 [T1 §1, §5] |
| Platform / Infrastructure | High demand; composite score 4.0/5; leverages Linux SysAdmin + systems interest [T1 §1] |
| DevOps / SRE | High demand; 179 openings on LinkedIn BCN, 26 entry-level; composite score 3.3/5 [T1 §1] |

#### Pros

| # | Strength | Source |
|---|---|---|
| 1 | **Most direct credential match**: Java bootcamp (Ironhack) + IronBank microservices project + Linux SysAdmin (PUE) | T1 §1, T3 §4 |
| 2 | Largest number of available positions in absolute terms | T1 §1 |
| 3 | N26 requires JVM + Spring Boot — direct match; banking domain knowledge is a genuine advantage at fintech employers | T1 §3 |
| 4 | Platform/Infrastructure lane is less saturated than pure backend and pays a premium (~€26K–€34K junior) | T1 §1 |
| 5 | Fastest path to first employment — widest funnel of openings | `[Inference]` |
| 6 | Linux SysAdmin course gives infrastructure credibility that most bootcamp grads lack | T1 §1 |

#### Cons

| # | Weakness | Source |
|---|---|---|
| 1 | **Highest risk of the "CRUD consulting trap"** — directly contradicts user priorities | T1 §5, user_data.md |
| 2 | Junior backend is the most competitive lane: hundreds of bootcamp grads compete for each opening; backend demand fell 7% in 2025 | T1 §1, S04 |
| 3 | Positions user as "one of many" Java juniors — wastes the ML/AI credential differentiation | `[Inference]` |
| 4 | IronBank project is a fork, stale (2022), with rough README — thin evidence for backend specialization claim | T3 §3, §4 |
| 5 | Does not leverage the strongest portfolio assets (AgenticCareerBoost, P3CTeX) | `[Inference]` |
| 6 | Brand.md explicitly forbids "CRUD-only backend identity box" — this angle risks exactly that framing | brand.md |

#### Gap List

| # | Gap | Remediation | Sprint Target |
|---|---|---|---|
| G-D1 | IronBank project is stale and forked | Create a clean repo (e.g., `ironbank-microservices`) with polished README, architecture docs, and setup instructions | S-002 |
| G-D2 | No Kubernetes/Terraform experience visible | Complete a small K8s deployment project or contribute to an IaC repository | S-002 or S-003 |
| G-D3 | No cloud certifications | Consider AWS Cloud Practitioner or GCP Associate as low-cost credibility signal | S-003 |
| G-D4 | No CI/CD pipeline in any project | Add GitHub Actions CI to AgenticCareerBoost and P3CTeX; document the pipeline | S-001/S-002 |
| G-D5 | No Go/Rust exposure (relevant for platform roles) | Low priority unless targeting specific platform positions | Later |

#### Named Barcelona Employer Targets

| Employer | Why | Role Type | Source |
|---|---|---|---|
| **N26** | JVM + Spring Boot requirement; banking domain overlap; above-market compensation | Backend Engineer | T1 §3 |
| **CaixaBank Tech** | 500+ hires/quarter; banking domain is the single strongest employer-fit advantage | Backend Developer, Cloud Engineer | T2 §2.3 |
| **Typeform** | Product-focused, values innovation over credentials, Backend + React stack | Backend Engineer | T1 §3 |
| **Factorial** | Barcelona unicorn, Ruby/React but values engineering culture; 20–40 deploys/day | Software Engineer | T2 §2.3 |
| **Dynatrace** | R&D expansion, Java-heavy JVM stack | R&D Engineer | T1 §3 |
| **Worldsensing** | Small team, Python + FastAPI + React; resource-aware IoT development | Full-Stack Engineer | T1 §3 |

#### Fit Against User Priorities

| Priority | Fit | Notes |
|---|---|---|
| Meaningful / career-building | **2/5** | High risk of CRUD consulting if not carefully targeted |
| Technology agnostic | **3/5** | Often locked to one stack |
| OSS / resource-aware | **3/5** | Depends on employer |
| ML / purpose-first AI | **1/5** | Not ML |
| LaTeX / unusual environments | **2/5** | Standard environments |
| Investigation / problem solving | **2/5** | Depends heavily on company; most junior backend is ticket work |

#### Regulatory/Social Leverage

- **Pay Transparency Directive** (T2 §3.3): Salary bands becoming mandatory in job postings will make it easier to filter out low-paying body-shop offers before applying.
- **Teletrabajo Law** (T2 §3.2): Backend/platform roles at product companies tend to offer hybrid arrangements; the legal framework ensures cost reimbursement for remote work.

---

## 2. Ranked Recommendation with Rationale

### Primary Positioning: Angle A — "ML/Data Engineering with Domain Depth"

**Why primary:**

1. **Strongest credential differentiation**. The UOC CS degree with ML/AI mention is the single asset that separates Dídac from the bootcamp-only candidate pool. In a market where "competition is lower than backend because most bootcamp grads lack ML credentials" [T1 §1], this is the most defensible competitive position.

2. **Largest intersection of demand and differentiation**. ML/Data Engineering demand is high and accelerating (10% YoY salary growth [T1 §1]) while junior competition is lower than backend. This is the lane where Dídac's profile is strongest *relative to the competition*, not just in absolute terms.

3. **Domain depth as multiplier**. The 15 years of banking/insurance experience is a genuine advantage — not merely "transferable soft skills" — at the six fintech and financial employers on the shortlist (CaixaBank Tech, N26, Ebury, Payhawk, Red Points, Stripe). ML + financial domain knowledge is an uncommon combination at junior level. `[Inference]`

4. **Aligns with user priorities**. Composite priority score of 4.2/5 — meaningful work, investigation-driven, direct ML path, avoids CRUD trap.

5. **Regulatory tailwind**. The EU AI Act creates demand for ML engineers who understand compliance, data quality, and bias auditing. Banking regulatory experience maps directly to AI compliance engineering. `[Inference]`

**Risk to manage**: Degree not conferred until Feb 2027. Mitigate by (a) stating "graduating Feb 2027" explicitly on all surfaces, (b) targeting employers who value portfolio evidence over checkbox credentials (HP, BSC, Red Points, scale-ups), and (c) building a deployed ML project to compensate for the missing diploma.

### Secondary Positioning: Angle B — "Agentic Systems Engineer"

**Why secondary:**

1. **Highest priority alignment** (4.3/5 composite) but **highest entry barrier**. The current market for agentic engineering roles in Barcelona is almost exclusively senior. This angle works as a *differentiator within* the primary ML positioning, not as a standalone application strategy.

2. **AgenticCareerBoost is the portfolio centerpiece regardless of angle**. Whether applying for ML, research, or platform roles, this project demonstrates systems thinking, AI engineering practice, and documentation discipline that set Dídac apart from other juniors. The agentic framing enhances any application without needing to be the primary positioning.

3. **BSC exception**: The BSC-CNS Junior AI Software Research Engineer role (agentic AI, LLM-RAG, workflow orchestration) is the single most aligned concrete opportunity in the Barcelona market. If this role is open when Dídac applies, Angle B becomes the primary positioning for that specific application.

**How to deploy**: Use Angle A as the default application posture. Deploy Angle B as a differentiator in interviews and portfolio presentations. Lead with Angle B only for explicitly agentic-AI or LLM-orchestration roles (BSC, HP GenAI Lab).

### Tertiary Positioning: Angle C — "Research Engineer / Applied AI"

**Why tertiary:**

Research engineering is the best *cultural* fit (investigation-driven, LaTeX-native, unusual environments) and scores 4.2/5 on priority alignment. However, it ranks third because:

1. Research positions are **project-funded and temporary** — they provide excellent learning but uncertain long-term employment stability.
2. Career progression beyond RE1 typically requires a Master's or PhD, which Dídac may or may not pursue.
3. The number of concurrent openings is small; this cannot be a volume-application strategy.

**How to deploy**: Monitor BSC, i2CAT, CVC, and UOC IN3 career pages continuously. Apply to specific RE1 openings when they appear. Treat research positions as high-value opportunities worth individual application effort, not as the default search strategy.

### Deprioritized: Angle D — "Backend + Platform Engineer"

**Why deprioritized:**

1. Directly contradicts user priorities — highest CRUD consulting trap risk.
2. Wastes the ML/AI credential differentiation by competing in the most saturated lane.
3. brand.md explicitly forbids "CRUD-only backend identity box."

**How to deploy**: Keep as a **fallback** if the primary job search exceeds 4 months without offers. If forced into this lane, apply exclusively to product companies (Typeform, Wallapop, N26, Factorial, Worldsensing) and never to body-shop consultancies. Emphasize the platform/infrastructure side (Linux admin, systems awareness) rather than pure backend.

### Decision Summary

| Rank | Angle | Use As | Application Volume |
|---|---|---|---|
| **Primary** | A: ML/Data Engineering with Domain Depth | Default application posture | 60% of applications |
| **Secondary** | B: Agentic Systems Engineer | Differentiator + BSC/HP-specific positioning | 20% of applications |
| **Tertiary** | C: Research Engineer / Applied AI | Targeted applications to specific RE1 openings | 10% of applications |
| **Fallback** | D: Backend + Platform Engineer | Last resort — product companies only | 10% of applications, only at product companies |

---

## 3. Gap-to-Remediation Map

### Critical Path Gaps (Must close before active applications)

| ID | Gap | Angle(s) | Remediation | Effort | Sprint |
|---|---|---|---|---|---|
| **GP-01** | Profile surfaces are fragmented, outdated, and inconsistent (LinkedIn ~25%, GitHub no bio, legacy site is net negative) | ALL | Execute profile update strategy (§5 below). Rewrite GitHub profile README, LinkedIn headline/about, pin correct repos, archive dead repos. | Medium | **S-001** |
| **GP-02** | No deployed ML project in portfolio | A, C | Build an end-to-end ML pipeline project: data → training → serving → monitoring. Python, scikit-learn/PyTorch, FastAPI, Docker. Deploy publicly. | High | **S-002** |
| **GP-03** | Python not visible as primary skill | A, B, C | Add Python-based projects to GitHub. Update LinkedIn skills. Ensure Python is prominent in profile README and CV. | Low | **S-001** (profile) / **S-002** (project) |
| **GP-04** | AgenticCareerBoost lacks benchmarks and evaluation metrics | B | Publish task completion rates, token cost analysis, quality metrics for the agentic system. | Medium | **S-002** |
| **GP-05** | IronBank project is stale, forked, rough README | D | Create clean `ironbank-microservices` repo with polished README, architecture docs, setup instructions. Only if Angle D becomes active. | Medium | **S-002** (if needed) |

### Strategic Gaps (Close within 3–6 months)

| ID | Gap | Angle(s) | Remediation | Effort | Sprint |
|---|---|---|---|---|---|
| **GS-01** | No cloud ML experience | A | Build a project using free-tier cloud ML (AWS SageMaker Studio Lab, GCP Vertex AI Workbench, or Colab → deployment) | Medium | **S-003** |
| **GS-02** | No RAG implementation visible | B | Add RAG component to AgenticCareerBoost or build standalone demo | Medium | **S-002/S-003** |
| **GS-03** | No CI/CD pipeline in any project | A, B, D | Add GitHub Actions CI to AgenticCareerBoost and P3CTeX. Document the pipeline. | Low | **S-001/S-002** |
| **GS-04** | Art + ML intersection unexploited | C | Build a creative AI project (style transfer, generative visualization, or procedural art) bridging art background with ML | Medium | **S-003** |
| **GS-05** | No visibility in research community | C | Attend BSC open days, i2CAT events, local AI/ML meetups. Consider submitting a poster or short paper. | Low (ongoing) | **S-002+** |
| **GS-06** | Second agentic project needed for Angle B depth | B | Build a smaller agentic project in a different domain (automated code review, document processing, etc.) | High | **S-003+** |

### Nice-to-Have Gaps (Close opportunistically)

| ID | Gap | Angle(s) | Remediation | Effort |
|---|---|---|---|---|
| GN-01 | No cloud certification | A, D | AWS Cloud Practitioner or GCP Associate (~€150, self-paced) | Low |
| GN-02 | No Kaggle track record | A | Submit to 1–2 competitions | Low |
| GN-03 | No C++/HPC exposure | C | Small C++ project or HPC-adjacent OSS contribution (only if targeting BSC HPC positions) | Medium |
| GN-04 | No Go/Rust exposure | D | Small project (only if targeting specific platform roles) | Medium |
| GN-05 | LinkedIn recommendations: 0 | ALL | Request 3–5 recommendations from former colleagues, bootcamp instructors, UOC peers | Low |

### Remediation Priority Waterfall

```
S-001 (NOW)
├── GP-01: Profile update (GitHub + LinkedIn + stop linking legacy site)
├── GP-03: Python visible in profiles
└── GS-03: GitHub Actions CI for existing repos

S-002 (NEXT)
├── GP-02: Deployed ML project (Python)
├── GP-04: AgenticCareerBoost benchmarks
├── GS-02: RAG component
└── GN-05: LinkedIn recommendations

S-003 (FOLLOWING)
├── GS-01: Cloud ML experience
├── GS-04: Art + ML creative project
├── GS-06: Second agentic project
└── GN-01: Cloud certification (optional)

ONGOING
├── GS-05: Research community visibility
├── GP-05: IronBank cleanup (only if Angle D activates)
└── GN-02–GN-04: Opportunistic skill-building
```

---

## 4. Explicit Rejection List

The following role types and employers should be **declined or deprioritized** in first-pass applications, per user priorities and brand constraints.

### Roles to Reject

| Category | Examples | Why Reject | Source |
|---|---|---|---|
| **Body-shop consulting / staff augmentation** | Capgemini, Accenture, NTT Data, Indra, Everis (NTT), Sopra Steria — in staff augmentation mode | High CRUD trap risk. Client-site placement with minimal agency over technology or growth. User explicitly prioritizes "meaningful or career-building offers over typical backend consulting." | user_data.md §Priorities, brand.md §Forbidden framings |
| **Generic CRUD backend at outsourcing firms** | Inetum, Aubay, Altran (Capgemini Engineering), NEORIS (junior body-shop tiers) | Saturated, low-growth, contradicts positioning. "If backend is the only offer, prioritize product companies over body-shop consultancies" [T1 §5]. | T1 §5 |
| **Unpaid internships** | Any company offering unpaid/token-stipend positions | Exploitative. At 36 with 15 years of professional experience, unpaid work undermines positioning and is economically unsustainable. Spanish labor law (Art. 8 ET) requires compensation for work that is not purely educational. | `[Inference]`, T1 §2 |
| **Roles requiring relocation outside Barcelona** | Madrid-only, remote-from-elsewhere-only | User explicitly based in Barcelona. Relocation contradicts personal constraints. | user_data.md §Personal data |
| **QA-only positions** | Manual QA, QA analyst (non-automation) | Low ceiling, low priority alignment (2.2/5 composite), does not leverage ML/AI credentials. QA automation is marginally better but still deprioritized. | T1 §5 |
| **Positions paying below €22,000 gross** | Any offer under this floor | Below €22K signals exploitation for a candidate with a CS degree (near-completion), ML specialization, and 15 years of professional experience. The realistic floor is €24K. | T1 §2 |
| **"Passion project" startups offering equity instead of salary** | Pre-seed startups with "competitive equity" language | Seed funding declined 34% YoY [T2 §2.2]. Pre-seed companies absorbing junior talent are "thinning from the bottom." Equity in a pre-seed startup is statistically worthless. | T2 §2.2 `[Inference]` |

### Employers to Deprioritize (Not Reject)

| Employer | Why Deprioritize | When to Reconsider |
|---|---|---|
| **King (Activision/Microsoft)** | Hires primarily at senior level; Director/Principal roles dominate current postings [T2 §2.3] | If junior QA or tools engineering openings appear |
| **SEAT:CODE** | 300+ experts but no evidence of junior pipeline; "digital transformation" framing risks consulting-adjacent work | If specific ML or platform roles are posted |
| **Amazon (AWS Spain)** | Madrid-focused; BCN office exists but 6,700+ new jobs are primarily Madrid | If BCN-specific roles are posted |
| **Manychat** | Hiring Senior Python Engineers; may have junior pipeline but not evidenced [T1 §3] | If junior openings appear |

### Decision Heuristic for Edge Cases

When evaluating an offer not clearly on the reject/accept list, apply this filter in order:

1. **Does the role involve building systems, not just executing tickets?** If no → reject.
2. **Will you learn something deployable in 12 months?** If no → reject.
3. **Is the employer a product company or a body-shop?** If body-shop → reject unless the assignment is genuinely technical.
4. **Is the salary ≥ €24K gross?** If no → reject unless the learning opportunity is exceptional (BSC fellowship, etc.).
5. **Does the role touch ML, data, infrastructure, or tooling?** If yes → accept. If pure CRUD → deprioritize.

---

## 5. Profile Update Strategy

The following directives are high-level strategic instructions for T5 (CommunityManager) to execute. They flow directly from the chosen positioning (Primary: ML/Data Engineering, Secondary: Agentic Systems).

### 5.1 Unified Narrative

All three surfaces (LinkedIn, GitHub, legacy site) must converge on a single coherent identity:

> **Core identity**: Software engineering student (UOC, ML/AI mention, graduating Feb 2027) with 15 years of regulated-industry process discipline, building model-agnostic agentic systems and LaTeX tooling. Based in Barcelona.

This replaces the current three contradictory identities:
- LinkedIn: "Java backend microservices dev" (2022)
- GitHub: (empty)
- Legacy site: "90s visual artist who started coding" (2022)

### 5.2 LinkedIn Directives

| Priority | Action | Rationale | Source |
|---|---|---|---|
| **C1** | Rewrite headline: `Software Engineering (UOC, ML/AI) · Agentic Systems · Python · Java · Barcelona` | Replace 2022 bootcamp language. Include ML/AI, location, and degree for LinkedIn search. Remove all emoji and code-syntax gimmicks. | T3 §1.1, brand.md |
| **C2** | Write About section (3 paragraphs): (1) Current identity — engineering student building systems, (2) Bridge — 15 years of domain expertise reframed as asset, (3) What I'm building now — agentic systems, LaTeX tooling, ML projects | The About section is the single highest-impact free-text field. Must align with Angle A positioning. | T3 §1.2 |
| **C3** | Add Experience entry: "Independent Engineering Projects" (2020–present) covering AgenticCareerBoost, P3CTeX, IronBank, UOC coursework | Makes the entire coding journey visible. Without this, the profile reads as "banker who did a bootcamp." | T3 §1.4 |
| **M1** | Pin 2–3 Featured items: AgenticCareerBoost repo/site, P3CTeX, a LinkedIn post explaining the transition | Prime real estate for linking to strongest portfolio evidence. | T3 §1.3 |
| **M2** | Rebuild Skills section: Python, Java, Spring Boot, ML/AI, LaTeX, Git, Linux, SQL, Docker, Systems Design, REST APIs, Microservices, OOP, Technical Writing, Agile | Target 15–20 skills covering both Angle A (ML) and Angle D (backend fallback). Python must be in the top 3 for Angle A. | T3 §1.6 |
| **M3** | Update Education: UOC end date → 2027; add "ML/AI specialization mention" to description; add IronHack capstone detail; frame Escola Massana as design/visual thinking background | Accuracy and credential visibility. ML/AI mention must be searchable. | T3 §1.5 |
| **M4** | Consolidate 15 years of service work into 1–2 grouped entries emphasizing: complex problem resolution, regulated environments, process discipline, team leadership | Reframes non-tech experience as asset. "Never delete the non-tech experience — it demonstrates range and reliability" [T3 §1.4]. | T3 §1.4, brand.md |
| **M5** | Request 3–5 recommendations: 1 bootcamp instructor/peer, 1–2 former banking colleagues/managers, 1 UOC professor or peer | Zero recommendations is a red flag for someone with 15+ years of experience [T3 §1.9]. | T3 §1.9, T2 §5.5 |
| **M6** | Begin posting 2x/month: Tuesday (narrative) + Thursday (technical artifact). Follow style-book.md cadence and voice rules. | Zero activity since ~2023 signals platform disengagement [T3 §1.10]. Recruiter data: consistent activity → 40% more callbacks [T2 §5.2]. | T3 §1.10, T2 §5.2, style-book.md §7 |

### 5.3 GitHub Directives

| Priority | Action | Rationale | Source |
|---|---|---|---|
| **C1** | Set bio: `Software Engineering (UOC, ML/AI 2027) · Agentic systems · LaTeX tooling · Python · Java · Barcelona` | Empty bio is the first thing a recruiter sees. 87% check GitHub before interview decisions [T2 §5.2]. | T3 §2.1 |
| **C2** | Rewrite profile README (DidacLL/DidacLL): positioning statement, current focus areas (ML, agentic systems, LaTeX tooling), key projects with links, tech stack, professional contact | Replace the broken 4-line README. Remove legacy site link. Remove VladScv reference. | T3 §2.2 |
| **C3** | Pin repos in order: (1) AgenticCareerBoost, (2) P3CTeX, (3) [new ML project when built], (4) Ironhack-IronBank (if cleaned) | Showcase strongest work first. Current pin order (if any) likely includes dead repos. | T3 §2.3 |
| **M1** | Set website to `https://didacll.github.io/`. Add LinkedIn URL. Set hireable flag. | Missing website and social links reduce discoverability [T3 §2.4]. | T3 §2.4 |
| **M2** | Archive 6–7 dead repos: FPP2024_TIPorHANG, TXTO, Didac-dev-project (after replacement site is live), art-scv-website, scv-calculator, DxM_Game_v3, FileSaver.js | Dead repos with self-deprecating descriptions ("just a...", "only for test...") actively harm the professional image [T3 §3]. | T3 §3 |
| **M3** | Add topics to all kept repos: AgenticCareerBoost (`agentic-systems`, `multiagent`, `model-agnostic`, `python`, `documentation`), P3CTeX (`latex`, `tex`, `document-class`, `open-source`), etc. | 0/12 repos have topics — this is findability metadata [T3 §3]. | T3 §3 |
| **M4** | Rewrite repo descriptions: AgenticCareerBoost ("Path-based, model-agnostic multiagent operating system for engineering career development"), P3CTeX ("Custom LaTeX document class and package ecosystem for academic document production") | Current descriptions are too casual or opaque for outsiders [T3 §4]. | T3 §4 |
| **M5** | Investigate and surface MemPalace contribution (48K+ star project) — if substantive, mention in profile README and LinkedIn | A contribution to a 48K-star project is invisible. This could be a significant credibility signal if the contribution is meaningful [T3 §2.5]. | T3 §2.5, §6.2 |

### 5.4 Legacy Site Directive

| Action | Rationale | Source |
|---|---|---|
| **Immediately**: Remove all links to the legacy site from GitHub profile README and any other controlled surface | The legacy site is a "net negative" that "actively undermines current positioning" [T3 §5]. Every link to it amplifies damage. | T3 §5 |
| **S-001**: Keep the site live but unlinked as a passive artifact | Deleting it may break external references. Keep it until the replacement is deployed. | T3 §3 |
| **S-002/S-003**: Replace with new site built from AgenticCareerBoost GitHub Pages, with AI-readable metadata, structured data (JSON-LD), proper SEO, and recruiter-optimized layout | user_data.md specifies a "landing page for recruiters" with "automated reader feeder for AI recruiters" as a project output. | user_data.md §Expected Outputs |

### 5.5 Cross-Surface Consistency Checklist

After T5 executes the profile updates, verify:

| Dimension | Must Be Consistent | Reference |
|---|---|---|
| Name format | "Dídac Llorens" on LinkedIn, "Dídac Ll." on GitHub (acceptable per brand.md) | T3 §6.1 |
| Location | "Barcelona" on all surfaces | T3 §6.1 |
| Degree | "UOC Software Engineering, ML/AI mention, graduating Feb 2027" — same year, same mention, everywhere | T3 §6.2 |
| Current identity | "Software engineering student building agentic systems and ML projects" — not "Java lover", not "visual artist who codes" | T3 §6.2 |
| Non-tech experience | "15 years of regulated-industry customer service and team leadership" — consistent number, consistent framing | T3 §6.2 |
| Key projects | AgenticCareerBoost and P3CTeX visible on ALL surfaces | T3 §6.2 |
| Contact | Professional email or LinkedIn URL — no VladScv, no dead links | T3 §6.2 |

---

## 6. Evidence Traceability Matrix

Every major recommendation in this document traces to specific evidence from T1, T2, or T3. Inferences are flagged with `[Inference]`.

| Recommendation | T1 Evidence | T2 Evidence | T3 Evidence | Inference? |
|---|---|---|---|---|
| ML/Data Engineering as primary angle | §1 (strongest credential differentiation), §2 (highest salary floor), §5 (4.2/5 composite) | §2.2 (specialist demand intensifying), §3.1 (EU AI Act creating ML compliance demand) | §4 (AgenticCareerBoost and P3CTeX support ML-adjacent positioning) | No |
| Agentic Systems as secondary angle | §1 (4.3/5 composite but almost exclusively senior), §5 (aspirational) | §2.3 (BSC agentic AI role directly aligned) | §4 (AgenticCareerBoost is the centerpiece) | No |
| Age is not a liability at 36 | Appendix (threshold is ~45) | §1.1 (Manfred: 36–40 = 33% of hires, peak bracket) | — | No |
| Reject body-shop consulting | §5 (CRUD trap risk 2.3/5) | — | — | Partially; brand.md also supports |
| Salary floor €24K | §2 (realistic first-job range €24K–€30K) | §4.3 (consistent salary data) | — | No |
| Profile is currently net negative | — | §5.2 (87% check GitHub, 40% more callbacks with active profiles) | §1.11 (~25% LinkedIn completeness), §6.2 (contradictory signals across surfaces) | No |
| Banking domain is advantage at fintech | — | §2.3 (CaixaBank Tech = most natural employer match) | — | Partially |
| EU AI Act creates opportunity | — | §3.1 (new AI compliance engineering category; compliance costs €150K–€500K per scale-up) | — | Yes (that Dídac can enter this category) |
| Research engineering as tertiary | §1 (RE1 positions accessible), §5 (4.2/5 composite) | §2.3 (BSC, i2CAT openings) | §4 (P3CTeX = LaTeX native to research) | No |

---

*Synthesis completed 2026-04-20. This document integrates evidence from three research reports (T1: 34 sources, T2: 40 sources, T3: 3-surface audit), user background data, brand constraints, and public voice rules. All inferences are explicitly flagged. No false optimism: every stated advantage has a corresponding stated risk.*


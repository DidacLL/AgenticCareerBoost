# Recruiter Landing Page — Information Architecture & Copy Drafts

- **Sprint**: S-001 / T5
- **Agent**: CommunityManager
- **Date**: 2026-04-20
- **Target**: `didacll.github.io/AgenticCareerBoost/` (Jekyll site, to be implemented in S-002)
- **Inputs**: T3 audit (§5 legacy site, §6 cross-surface), T4 positioning synthesis, brand.md, style-book.md, marketing.md
- **Scope**: Content architecture and copy only. No HTML/CSS/Jekyll code.

---

## 1. Site Information Architecture

### 1.1 Page Structure

```
/                           → Landing page (single-page recruiter flow)
/projects/                  → Project showcase (expanded detail)
/projects/agentic-career-boost/  → AgenticCareerBoost deep-dive
/projects/p3ctex/           → P3CTeX deep-dive
/about/                     → Full background narrative
/contact/                   → Contact form or redirect to LinkedIn
/assets/reports/            → PDF downloads (Agentic System Guide, sprint reports)
```

### 1.2 Navigation

| Item | Links To | Purpose |
|------|----------|---------|
| **Home** | `/` | Landing page — the default recruiter entry point |
| **Projects** | `/projects/` | Showcase page with cards for each project |
| **About** | `/about/` | Full narrative — career bridge, background, philosophy |
| **Reports** | `/assets/reports/` | Downloadable PDFs — formal engineering artifacts |
| **Contact** | `/contact/` | Professional contact information |

**Design principle**: The landing page (`/`) should be self-contained for a 90-second recruiter scan. Every other page is optional depth. A recruiter who visits only `/` should leave with: (1) who this person is, (2) what they build, (3) evidence that it is real, and (4) how to contact them.

### 1.3 User Flows

**Flow 1 — Recruiter (90 seconds)**:
`/` → scan hero → scan projects → scan skills → click LinkedIn or download PDF → leave

**Flow 2 — Engineering peer (3–5 minutes)**:
`/` → click project card → read project detail → browse GitHub repo → return

**Flow 3 — AI recruiter bot (automated)**:
`/` → parse JSON-LD structured data → extract skills, education, experience → index

---

## 2. Landing Page Sections (copy drafts)

### 2.1 Hero Section

**Purpose**: Immediate identity establishment. Who is this person, what do they do, where are they.

#### Option A — ML/Data Forward (recommended)

> **Name**: Dídac Llorens
>
> **Tagline**: Software Engineering · ML/AI · Systems Design · Barcelona
>
> **One-liner**: Building model-agnostic agentic systems and ML pipelines. Finishing a CS degree with ML/AI specialization at UOC (Feb 2027). 15 years of regulated-industry operations before engineering — process discipline and compliance thinking included.
>
> **CTA**: [View Projects] [Download CV] [LinkedIn]

#### Option B — Agentic Systems Forward

> **Name**: Dídac Llorens
>
> **Tagline**: Agentic Systems · ML/AI · Software Engineering · Barcelona
>
> **One-liner**: Designing path-based, model-agnostic multi-agent systems with formal documentation discipline. CS degree with ML/AI specialization (UOC, Feb 2027). 15 years of regulated-industry operations reframed as engineering thinking.
>
> **CTA**: [View Projects] [Download CV] [LinkedIn]

**Copy constraints**:
- No "Welcome to my portfolio" or generic greetings
- No emoji
- No "passionate about" language
- The one-liner must contain: what you build, your credential, and the career bridge — in that order
- CTA buttons should link to: `/projects/`, a downloadable PDF CV, and LinkedIn profile

---

### 2.2 About Section (Landing Page Summary)

**Purpose**: Two-paragraph identity bridge. The full narrative lives on `/about/` — this is the compressed version.

> I am completing a Software Engineering degree at UOC with a specialization in Machine Learning and Artificial Intelligence (graduating February 2027). My engineering work focuses on agentic system design, LaTeX tooling architecture, and applied ML — all open-source and publicly inspectable on GitHub.
>
> Before engineering, I spent 15 years managing customer operations in banking and insurance: team leadership, complex case resolution, regulatory compliance, stakeholder management. I build software the way I managed production teams — with documented decisions, failure-mode awareness, and process discipline that survives contact with reality.

**Copy constraints**:
- Dense. No padding sentences.
- The career bridge paragraph must reframe the non-tech experience as an active asset, never as something to apologize for.
- Must not duplicate the LinkedIn About section verbatim (marketing.md: "do not clone identical content across channels"). Same kernel, different expression.

---

### 2.3 Projects Showcase

**Purpose**: Visual cards linking to project detail pages. Each card needs a title, one-line description, key technologies, and a link.

#### Card 1: AgenticCareerBoost

> **Title**: AgenticCareerBoost
>
> **Description**: A path-based, model-agnostic multi-agent operating system. 6 agent roles, 7 workflow contracts, formal engineering reports, and a public site — all orchestrated through Markdown files and file paths. No mega-prompts. No vendor lock-in.
>
> **Stack**: Python · Markdown · LaTeX · GitHub Pages · GitHub Actions
>
> **Links**: [GitHub Repository] [Live Site] [Agentic System Guide (PDF)]
>
> **Evidence signal**: Active development (last push: today). GPL-3.0 licensed. Full README with architecture diagrams.

#### Card 2: P3CTeX

> **Title**: P3CTeX
>
> **Description**: A custom LaTeX document class and package ecosystem for academic document production. Multi-package architecture with expl3 internals, automated test suites, and an agentic development workflow. 2 GitHub stars (organic).
>
> **Stack**: LaTeX (expl3) · latexmk · Bash · GitHub Actions `[TODO: verify CI]`
>
> **Links**: [GitHub Repository] [Example Output (PDF)] `[TODO: create example output]`
>
> **Evidence signal**: Active development. GPL-3.0 licensed. Documentation in English and Catalan.

#### Card 3: IronBank Microservices (conditional)

> **Title**: IronBank — Banking Microservices Simulation
>
> **Description**: A Java/Spring Boot microservices architecture simulating a banking system. Keycloak authentication, OpenAPI documentation, multi-service design. IronHack bootcamp capstone (2022).
>
> **Stack**: Java 18 · Spring Boot · Maven · Keycloak · OpenAPI
>
> **Links**: [GitHub Repository]
>
> **Evidence signal**: Demonstrates backend engineering fundamentals. `[TODO: enhance README before featuring]`

**Note**: Only feature Card 3 if the IronBank README has been improved (see `repo-metadata-updates.md`). Until then, display only Cards 1 and 2.

#### Card 4: Future ML Project (placeholder)

> **Title**: `[TODO: ML Pipeline Project]`
>
> **Description**: End-to-end ML pipeline — data ingestion, training, model serving, monitoring. Python, scikit-learn/PyTorch, FastAPI, Docker. `[TODO: build in S-002/S-003 per T4 GP-02]`
>
> **Stack**: Python · scikit-learn/PyTorch · FastAPI · Docker
>
> **Links**: `[TODO]`

---

### 2.4 Skills & Stack Section

**Purpose**: Scannable technology inventory. Recruiters and AI bots use this for keyword matching.

#### Layout: Grouped by Category

**Languages**: Python · Java · Kotlin · SQL · LaTeX · JavaScript · Bash

**Frameworks & Tools**: Spring Boot · React · FastAPI `[TODO: add when ML project is built]` · Docker · Git · GitHub Actions · latexmk · Maven

**Domains**: Machine Learning · Agentic Systems · Systems Design · Microservices · REST APIs · Technical Documentation · Linux Administration

**Methodologies**: Agile / Scrum · OOP · Design Patterns · Test-Driven Development `[TODO: verify TDD practice evidence]`

**Copy constraint**: No self-assessment bars or percentage ratings (e.g., "Java: 85%"). These are meaningless and unprofessional. List skills as flat tags grouped by category. Let the projects section provide evidence of depth.

---

### 2.5 Experience Bridge Section

**Purpose**: Dedicated section that reframes the career transition as an asset. This is the unique selling point of the site — no other junior candidate has this section.

> **Section title**: "15 Years Before Engineering"
>
> I spent 15 years in customer-facing operations across banking and insurance before writing my first production line of code. Here is what that experience means for engineering:
>
> **Process discipline under regulation** — I operated in environments where compliance failures have legal consequences. When I design systems, I think about audit trails, data quality controls, and failure cascades — because I have seen what happens when those are missing.
>
> **Complex problem resolution at scale** — I resolved high-volume customer cases involving multi-system interactions, regulatory edge cases, and stakeholder conflicts. Debugging production issues is structurally similar to debugging production customer problems.
>
> **Team leadership in high-pressure environments** — I led and mentored teams handling real-time customer operations. Incident management, escalation protocols, and under-pressure decision-making are not soft skills I claim — they are operational reflexes.
>
> **Domain knowledge as competitive advantage** — In a market where ML systems are increasingly regulated (EU AI Act, financial data directives), understanding how compliance works from the inside is not a transferable skill — it is a technical advantage. Particularly at fintech employers (CaixaBank Tech, N26, Ebury) and research centers working on AI governance.

**Copy constraints**:
- Must NOT read as defensive or apologetic
- Each paragraph opens with the engineering benefit, not the banking history
- Specific enough to be credible, not so specific that it reads as a resume dump
- The EU AI Act reference adds strategic currency without being AI-hype

---

### 2.6 Education Section

**Purpose**: Credential display. Dense, factual, with key details visible.

| Institution | Program | Duration | Key Details |
|-------------|---------|----------|-------------|
| **UOC** (Universitat Oberta de Catalunya) | Software Engineering (Grau en Enginyeria Informàtica) — ML/AI Specialization Mention | 2021 – Feb 2027 | Coursework: ML, neural networks, algorithms, OS, software architecture. Capstone in progress. `[TODO: verify specific UOC coursework list with user]` |
| **IronHack** (Barcelona) | Java Backend Development Bootcamp | 2022 | Capstone: IronBank microservices banking simulation (Java, Spring Boot, Keycloak). |
| **BCN ITAcademy** | FullStack React Development | `[TODO: verify year]` | Full-stack web development with React. |
| **PUE** | Linux System Administration | `[TODO: verify year]` | Server management, shell scripting, networking, security. |
| **Fundación Francisco Puerto** | Android Development (Kotlin) | 2024 | Mobile development fundamentals. |
| **Escola Massana** (Centre d'Art i Disseny) | Art & Design | 2013 – 2016 | Visual thinking, spatial reasoning, iterative creative process. Informs current work in systems visualization and documentation aesthetics. `[TODO: verify institution name, dates, and skill characterizations with user]` |

---

### 2.7 Contact Section

**Purpose**: Clear, professional contact information. No friction.

> **Section title**: "Contact"
>
> I am based in Barcelona and open to opportunities in ML engineering, data engineering, agentic AI, platform engineering, and research engineering. Hybrid or remote-friendly roles preferred.
>
> → **LinkedIn**: [linkedin.com/in/didacllorens](https://www.linkedin.com/in/didacllorens/)
> → **GitHub**: [github.com/DidacLL](https://github.com/DidacLL)
> → **Email**: `[TODO: add professional email — consider creating a didacllorens@domain or using a professional alias]`
>
> For formal inquiries, LinkedIn messaging is preferred.

**Copy constraints**:
- No "Feel free to reach out!" or overly casual language
- No "I'm always happy to chat" — state availability factually
- Specify target role families so recruiters can self-qualify
- Arrow points (→) per style-book.md §4.1

---

## 3. Full About Page (`/about/`)

**Purpose**: Extended narrative for recruiters and peers who want the full story. This page is optional depth — the landing page summary (§2.2) is the compressed version.

### Copy Draft

**Title**: About Dídac Llorens

I am 36, based in Barcelona, and finishing a Software Engineering degree at UOC with a specialization in Machine Learning and Artificial Intelligence (graduating February 2027). I build tools and systems — agentic workflows, LaTeX document infrastructure, ML pipelines — and I document every decision so the reasoning is inspectable.

**The transition**

I did not start in engineering. I spent 15 years in customer-facing roles across banking and insurance — managing production teams, resolving complex cases in regulated environments, and building the kind of process discipline that most engineers only encounter through postmortem culture. I started coding seriously in 2020 `[TODO: confirm coding start date with user]`, during the lockdown, and I have not stopped since.

I do not frame this as a career change. It is a career extension. The same thinking that made me effective in production operations — systematic troubleshooting, failure-mode awareness, stakeholder communication under pressure, and respect for audit trails — is what I bring to software engineering. The systems changed; the thinking did not.

**What I build**

AgenticCareerBoost is a path-based, model-agnostic multi-agent operating system I designed to produce career artifacts with full traceability. It runs 6 agent roles across 7 workflow contracts, orchestrated through Markdown files instead of mega-prompts. Every output — this site, the formal reports, the profile updates — is produced by the system and inspectable on GitHub. The architecture itself is the case study.

P3CTeX is a custom LaTeX document class and package ecosystem I built for academic document production at UOC. Multi-package architecture, expl3 internals, automated test suites, and an agentic development workflow. It is the kind of project that does not fit on a resume but tells you everything about how I think about tooling.

**What I am looking for**

Roles where I can apply ML engineering, agentic AI design, data pipeline architecture, or systems-level thinking in environments that reward investigation over ticket velocity. Product companies, research centers, or teams building things that matter. Barcelona-based, hybrid or remote-friendly.

I care about meaningful work, technology agnosticism, and open-source principles. I care less about which language is on the job description and more about whether the team values engineering judgment.

---

## 4. AI-Readable Metadata Specification

### 4.1 JSON-LD Structured Data (Schema.org)

Place in the `<head>` of every page. This is what AI recruiter bots, Google, and LinkedIn's crawler will parse.

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Dídac Llorens",
  "alternateName": "Didac Llorens",
  "url": "https://didacll.github.io/AgenticCareerBoost/",
  "image": "[TODO: professional headshot URL]",
  "jobTitle": "Software Engineering Student",
  "description": "Software engineering student (UOC, ML/AI specialization, Feb 2027) building model-agnostic agentic systems and LaTeX tooling. 15 years of regulated-industry operations. Based in Barcelona.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Barcelona",
    "addressRegion": "Catalonia",
    "addressCountry": "ES"
  },
  "alumniOf": [
    {
      "@type": "EducationalOrganization",
      "name": "Universitat Oberta de Catalunya (UOC)",
      "url": "https://www.uoc.edu"
    },
    {
      "@type": "EducationalOrganization",
      "name": "IronHack",
      "url": "https://www.ironhack.com"
    },
    {
      "@type": "EducationalOrganization",
      "name": "Escola Massana",
      "url": "https://www.escolamassana.cat"
    }
  ],
  "knowsAbout": [
    "Machine Learning",
    "Artificial Intelligence",
    "Agentic Systems",
    "Python",
    "Java",
    "Spring Boot",
    "LaTeX",
    "Kotlin",
    "SQL",
    "Linux Administration",
    "Systems Design",
    "Microservices",
    "REST APIs",
    "Docker",
    "Git",
    "Technical Writing",
    "Software Architecture"
  ],
  "sameAs": [
    "https://www.linkedin.com/in/didacllorens/",
    "https://github.com/DidacLL"
  ],
  "seeks": {
    "@type": "Demand",
    "description": "ML Engineering, Data Engineering, Agentic AI, Platform Engineering, or Research Engineering roles in Barcelona"
  }
}
```

### 4.2 Open Graph Tags

Place in the `<head>` of every page for social media previews (LinkedIn, Slack, etc.).

```
og:title        → "Dídac Llorens — Software Engineering · ML/AI · Barcelona"
og:description  → "Software engineering student building model-agnostic agentic systems and ML pipelines. UOC CS degree with ML/AI specialization (Feb 2027). 15 years of regulated-industry experience."
og:image        → [TODO: create a branded OG image — 1200x630px, dark background, name + tagline + key project screenshots]
og:url          → "https://didacll.github.io/AgenticCareerBoost/"
og:type         → "profile"
og:locale       → "en_US"
```

### 4.3 Twitter/X Card Tags (optional)

```
twitter:card        → "summary_large_image"
twitter:title       → "Dídac Llorens — Software Engineering · ML/AI · Barcelona"
twitter:description → "Building agentic systems and ML pipelines. UOC CS + ML/AI (Feb 2027). Barcelona."
twitter:image       → [same as og:image]
```

### 4.4 Meta Description

```
<meta name="description" content="Dídac Llorens — Software engineering student (UOC, ML/AI specialization, Feb 2027) building model-agnostic agentic systems and LaTeX tooling. 15 years of regulated-industry experience. Based in Barcelona. Open to ML, data, and platform engineering roles.">
```

(248 chars — under the 320-char display limit for Google snippets)

---

## 5. SEO Considerations

### 5.1 Target Keywords

| Priority | Keyword / Phrase | Search Intent | Where to Use |
|----------|-----------------|---------------|--------------|
| 1 | `Dídac Llorens` / `Didac Llorens` | Branded search (recruiter checking name) | Title tag, H1, JSON-LD name + alternateName |
| 2 | `Dídac Llorens Barcelona developer` | Recruiter search (name + location + role) | Meta description, About section, JSON-LD |
| 3 | `software engineer Barcelona ML` | Role-based search | Skills section, meta description |
| 4 | `agentic systems engineer` | Niche search | Projects section, JSON-LD knowsAbout |
| 5 | `UOC software engineering ML AI` | Academic affiliation search | Education section, JSON-LD alumniOf |
| 6 | `AgenticCareerBoost` | Project-specific search | Projects section, page title for project page |
| 7 | `P3CTeX LaTeX` | Project-specific search | Projects section |
| 8 | `career changer software engineer Barcelona` | Identity-based search | About page (natural language, not keyword stuffing) |

### 5.2 Title Tag

```
<title>Dídac Llorens — Software Engineering · ML/AI · Agentic Systems · Barcelona</title>
```

(79 chars — under the 60-char ideal for Google but acceptable; Google truncates at ~60 chars in SERPs but displays the full title in browser tabs)

**Alternative (shorter)**:

```
<title>Dídac Llorens — ML/AI Engineer · Barcelona</title>
```

(49 chars — fits Google SERP display)

### 5.3 Canonical URL

```
<link rel="canonical" href="https://didacll.github.io/AgenticCareerBoost/" />
```

Set on every page to prevent duplicate content issues between `/` and `/index.html`.

### 5.4 Robots and Indexing

```
<meta name="robots" content="index, follow">
```

All pages should be indexable. No `noindex` tags on the landing page.

### 5.5 Sitemap

Generate a `sitemap.xml` at the root:

```
https://didacll.github.io/AgenticCareerBoost/
https://didacll.github.io/AgenticCareerBoost/projects/
https://didacll.github.io/AgenticCareerBoost/projects/agentic-career-boost/
https://didacll.github.io/AgenticCareerBoost/projects/p3ctex/
https://didacll.github.io/AgenticCareerBoost/about/
https://didacll.github.io/AgenticCareerBoost/contact/
```

### 5.6 Performance Considerations

- GitHub Pages with Jekyll is static-served — inherently fast
- Minimize image sizes (compress PNG/JPEG, consider WebP)
- No JavaScript frameworks needed for a content site
- Lighthouse target: 90+ on Performance, Accessibility, Best Practices, SEO

---

## 6. Content Differentiation from Other Surfaces

Per marketing.md: "do not clone identical content across channels."

| Content Element | Landing Page Expression | LinkedIn Expression | GitHub Expression |
|-----------------|------------------------|--------------------|--------------------|
| **Identity statement** | Extended narrative with career bridge section | 3-paragraph About section | One-line positioning in README |
| **Projects** | Visual cards with descriptions and evidence signals | Featured section links + experience bullets | Pinned repos with descriptions |
| **Skills** | Grouped tags by category | Priority-ordered endorseable skills list | Inline tech tags in README |
| **Career transition** | Dedicated "15 Years Before Engineering" section | Paragraph 2 of About section | "Background" section in README |
| **Contact** | Dedicated contact page with role preferences | Profile contact info + InMail | Bio links + social settings |
| **Evidence** | PDF downloads, project deep-dives | Uploaded PDFs in Featured | Repos, commits, contribution graph |

---

## Checks

- [x] Site IA is defined with clear page structure
- [x] All sections have copy drafts
- [x] JSON-LD structured data spec provided
- [x] Open Graph tags specified
- [x] Meta description under 320 chars
- [x] SEO keywords mapped to content locations
- [x] No HTML/CSS/Jekyll code included (content-only scope)
- [x] Content differentiated from LinkedIn and GitHub (not cloned)
- [x] Tone consistent with brand.md
- [x] No forbidden-tone checklist violations
- [x] Every claim links to evidence or marked `[TODO]`
- [x] Alternatives provided for hero section (Angle A vs Angle B)

---

*Blueprint produced by CommunityManager agent, S-001 T5. Implementation (Jekyll/HTML/CSS) deferred to S-002. All copy requires user review before implementation.*

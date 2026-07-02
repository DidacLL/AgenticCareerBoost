# S-001 Profile Audit — GitHub + LinkedIn + Legacy Site

**Date**: 2026-04-20  
**Sprint**: S-001  
**Auditor**: Developer agent  
**Subject**: Dídac Llorens (DidacLL)

---

## Executive Summary

The public online presence of Dídac Llorens shows a profile in mid-transition
between a non-tech career and a software engineering identity. The transition is
genuine and in progress, but *almost none of that progress is visible* to a
recruiter performing a 90-second scan. The GitHub profile has no bio, no
website link, a stale profile README, and a graveyard of unfinished bootcamp
repos alongside genuinely impressive LaTeX systems work. The LinkedIn headline
is frozen in 2022 bootcamp language. The legacy portfolio site is a 2022
artifact that actively undermines the candidate's current positioning. Across
all three surfaces, the narrative is fragmented, outdated, and inconsistent.

**Bottom line**: A hiring manager searching "Dídac Llorens Barcelona developer"
today would find contradictory signals, zero evidence of the agentic systems
work or the degree progress, and a presentation layer that reads "early
bootcamp grad" rather than "systems-minded engineer finishing a CS degree."

---

## Section 1: LinkedIn Audit

**Profile URL**: https://www.linkedin.com/in/didacllorens/

> **Limitation**: LinkedIn public view returned limited data. Some sections
> (About, Featured, Experience details, Skills list, Recommendations) were not
> fully rendered in the public scrape. Findings below are based on what was
> extractable. Items marked with [INFERRED] require manual verification.

### 1.1 Headline

| Field | Value |
|-------|-------|
| **Current text** | `MicroServices \|\| Back-End Developer && Java lover ❤️` |
| **Severity** | **Critical** |

**Issues**:
- Uses programmer-humor syntax (`||`, `&&`) that is invisible to LinkedIn
  search and confusing to non-technical recruiters.
- "Java lover ❤️" is unprofessional for a 36-year-old targeting meaningful
  engineering roles. It reads as a junior bootcamp graduate's first headline.
- No mention of: Software Engineering degree, systems thinking, LaTeX/tooling,
  agentic workflows, AI/ML interest, or Barcelona location.
- "MicroServices" is misspelled (should be "Microservices").
- The headline is frozen circa 2022 — it reflects IronHack bootcamp output,
  not current capabilities.

**Recommendation**: Replace with a positioning-aligned headline, e.g.:
`Software Engineering Student (UOC, Feb 2027) · Systems & Tooling · Java ·
AI/ML · Barcelona`. Remove all emoji and code-syntax gimmicks.

### 1.2 About Section

| Field | Value |
|-------|-------|
| **Current text** | Not visible in public scrape |
| **Severity** | **Critical** [INFERRED] |

**Issues**:
- If absent: critically missing. The About section is the single highest-impact
  free-text field on LinkedIn.
- If present but not rendered: verify content manually. A 2022-era About
  section would need complete rewriting.

**Recommendation**: Write a 3-paragraph About section aligned with brand.md
positioning. Lead with current identity (engineering student, systems builder),
bridge the career transition as a strength (domain breadth, customer-facing
discipline), close with what the candidate is building now (agentic systems,
LaTeX tooling, degree capstone).

### 1.3 Featured Section

| Field | Value |
|-------|-------|
| **Current content** | Not visible — likely empty |
| **Severity** | **Major** |

**Issues**:
- No featured posts, articles, or links visible.
- This is prime real estate for linking to AgenticCareerBoost, P3CTeX, the
  agentic system guide PDF, or the public site.

**Recommendation**: Pin 2–3 items: (1) AgenticCareerBoost repo or site,
(2) P3CTeX repo or a showcase PDF, (3) a LinkedIn post explaining the career
transition and what the candidate is building.

### 1.4 Experience Section

| Field | Value |
|-------|-------|
| **Current content** | Not fully visible in scrape |
| **Severity** | **Critical** [INFERRED] |

**Issues**:
- The 15 years of banking/insurance customer service is the elephant in the
  room. If presented as a raw chronological job list, recruiters will mentally
  file the candidate as "career changer, high risk."
- If experience entries lack reframing (problem-solving, process optimization,
  stakeholder management, technical troubleshooting), they waste space.
- If there is no "Software Engineering" or "Independent Projects" experience
  entry covering 2020–present, the entire coding journey is invisible.

**Recommendation**:
1. Add an experience entry for independent engineering work (2020–present)
   covering: P3CTeX, AgenticCareerBoost, bootcamp capstone projects, and
   university coursework.
2. Consolidate the 15 years of service work into 1–2 grouped entries that
   emphasize transferable skills (complex problem resolution, regulated
   environments, process discipline).
3. Never delete the non-tech experience — it demonstrates range and reliability.

### 1.5 Education Section

| Field | Value |
|-------|-------|
| **Current content** | UOC Software Engineering (2021–2026), two other entries (years only) |
| **Severity** | **Major** |

**Issues**:
- UOC end date shows 2026, but the degree completes Feb 2027. Depending on
  whether this is an auto-inferred date or user-set, it may be inaccurate.
- The ML/AI mention is not visible in the education entry.
- IronHack bootcamp (2022) is listed but may lack detail about the capstone
  (IronBank microservices project).
- The 2013–2016 entry (3 years) likely corresponds to the Escola Massana fine
  arts diploma — this is a differentiator if framed correctly, wasted space if
  not.

**Recommendation**: Update UOC end date to 2027. Add "ML/AI specialization
mention" to the description. Add IronHack capstone project detail. Frame the
Escola Massana entry as design/visual thinking background.

### 1.6 Skills Section

| Field | Value |
|-------|-------|
| **Current content** | Not visible in public scrape |
| **Severity** | **Major** [INFERRED] |

**Issues**:
- If the skills list only contains Java, Spring, HTML/CSS (bootcamp-era
  skills), it misses: LaTeX, systems design, agentic workflows, Kotlin,
  Git/GitHub, Linux administration, ML fundamentals, OOP/design patterns.

**Recommendation**: Audit and rebuild. Target 15–20 skills covering: Java,
Spring Boot, Kotlin, LaTeX, Git, Linux, Python, SQL, REST APIs, Microservices,
OOP, Design Patterns, Agile, Technical Writing, Systems Design.

### 1.7 Custom URL

| Field | Value |
|-------|-------|
| **Current** | `linkedin.com/in/didacllorens/` |
| **Severity** | **Minor** (acceptable) |

The URL is clean and professional. No action needed.

### 1.8 Profile Photo / Banner

| Field | Value |
|-------|-------|
| **Current** | Not assessed (scrape did not render images) |
| **Severity** | **Major** [INFERRED] |

**Recommendation**: Verify manually. A professional headshot and a custom
banner (engineering/tech themed, not default LinkedIn blue) significantly
improve first impressions. If using a casual or artistic photo, consider
updating to something more aligned with tech hiring norms.

### 1.9 Recommendations

| Field | Value |
|-------|-------|
| **Count** | 0 visible |
| **Severity** | **Major** |

**Issues**:
- Zero recommendations is a red flag for someone claiming 15+ years of
  professional experience. Even non-tech colleagues can attest to work ethic,
  problem-solving, and reliability.

**Recommendation**: Request 3–5 recommendations: at least 1 from a bootcamp
instructor or peer, 1–2 from former colleagues/managers in banking, and
ideally 1 from a UOC professor or project collaborator.

### 1.10 Activity / Posts

| Field | Value |
|-------|-------|
| **Recent activity** | Likes only — no original posts visible since ~2023 |
| **Severity** | **Major** |

**Issues**:
- The most recent original posts are from late 2022 / early 2023. Both are
  reshares (a personality quiz and a DuckDuckGo privacy post), not
  engineering content.
- All recent activity is passive likes, many on non-tech topics (labor rights,
  space photos). This signals disengagement from the professional platform.
- There is zero evidence of the current engineering work
  (AgenticCareerBoost, P3CTeX, degree progress, agentic systems thinking).

**Recommendation**: Begin posting 1–2 times per month. Topics: engineering
learnings, project showcases, agentic systems insights, LaTeX tooling updates.
Cross-post from the AgenticCareerBoost content pipeline.

### 1.11 Completeness Score Estimate

| Dimension | Score |
|-----------|-------|
| Headline | 1/5 |
| About | 1/5 (likely missing or stale) |
| Featured | 0/5 |
| Experience | 2/5 |
| Education | 3/5 |
| Skills | 2/5 (likely incomplete) |
| Recommendations | 0/5 |
| Activity | 1/5 |
| **Overall LinkedIn completeness** | **~25%** |

---

## Section 2: GitHub Profile Audit

**Profile URL**: https://github.com/DidacLL

### 2.1 Bio Text

| Field | Value |
|-------|-------|
| **Current** | Empty (no bio set) |
| **Severity** | **Critical** |

**Issues**:
- The bio field is completely empty. This is the first text a visitor reads.
- No indication of who this person is, what they build, or what they care
  about.

**Recommendation**: Set a concise bio, e.g.: `Software Engineering student
(UOC, 2027) · Systems tooling · LaTeX · Java · Agentic workflows · Barcelona`

### 2.2 Profile README (DidacLL/DidacLL repo)

| Field | Value |
|-------|-------|
| **Repo exists** | Yes |
| **Current content** | 4 lines: "Hi, I'm @DidacLL / I'm a software engineer on process! / Have a look to my resume at [legacy site] / Contact me at VladScv" |
| **Severity** | **Critical** |

**Issues**:
- "Software engineer on process" is grammatically broken (should be "in
  progress" or "in training").
- Links to the legacy resume site, which is a 2022 artifact that undermines
  current positioning.
- References a `VladScv` GitHub account — is this an alt? If not, it is
  confusing and unprofessional. If so, it should not be the primary contact
  method on a profile README.
- No mention of: UOC degree, P3CTeX, AgenticCareerBoost, agentic systems,
  ML/AI, or any current work.
- No formatting, no sections, no visual appeal whatsoever.
- Topics on the repo: `config, github-config` — irrelevant noise.

**Recommendation**: Complete rewrite. A profile README should include: a
one-line positioning statement, current focus areas, key projects with links,
tech stack, and a professional contact method. Remove the VladScv reference
unless there is a clear reason to keep it.

### 2.3 Pinned Repos

| Field | Value |
|-------|-------|
| **Currently pinned** | Not determinable from scrape — top repos shown: P3CTeX, Didac-dev-project, p3cTeX-UMLST, TXTO, AgenticCareerBoost, art-scv-website |
| **Severity** | **Major** |

**Issues**:
- If pinned repos include `Didac-dev-project`, `art-scv-website`, or
  `scv-calculator`, these are actively harmful to the professional image.
- If AgenticCareerBoost is not pinned, the best current work is invisible.

**Recommendation**: Pin exactly these repos (in order):
1. **AgenticCareerBoost** — demonstrates systems thinking and agentic
   engineering
2. **P3CTeX** — demonstrates LaTeX mastery, OSS discipline, documentation
3. **Ironhack-IronBank_FinalProject_vBNKsys** — demonstrates Java/Spring
   microservices (after enhancement)
4. Optionally: **p3cTeX-UMLST** if space allows (shows library extraction
   skills)

### 2.4 Location, Website, Social Links

| Field | Value |
|-------|-------|
| **Location** | Barcelona (set) |
| **Website/blog** | Empty |
| **Twitter/X** | Empty |
| **Company** | Empty |
| **Email** | Not public |
| **Severity** | **Major** |

**Issues**:
- No website link. This should point to the AgenticCareerBoost GitHub Pages
  site or the future portfolio.
- No social links at all. LinkedIn should be linked.
- "Hireable" flag is not set.

**Recommendation**: Set website to
`https://didacll.github.io/`. Add LinkedIn URL. Set
hireable flag to true. Optionally set company to "UOC (Software Engineering)".

### 2.5 Contribution Graph

| Field | Value |
|-------|-------|
| **Recent activity** | Active — 55% commits in last month, contributions to AgenticCareerBoost and MemPalace/mempalace |
| **Severity** | **Minor** |

**Issues**:
- Recent contribution graph shows activity, which is positive.
- Contributed to MemPalace/mempalace (48K+ stars) — this is a significant
  signal that is completely invisible in the profile. If this contribution is
  meaningful (not just a typo fix), it should be highlighted.
- Historical graph likely has large gaps (2023–2025 period between bootcamp
  and current work).

**Recommendation**: Verify the MemPalace contribution scope. If substantive,
mention it in the profile README and LinkedIn.

### 2.6 Follower/Following Ratio

| Field | Value |
|-------|-------|
| **Followers** | 7 |
| **Following** | 6 |
| **Severity** | **Minor** |

**Issues**:
- Very low follower count, but ratio is balanced (not follow-farming).
- This will improve organically with better profile content and activity.

### 2.7 Organization Memberships

| Field | Value |
|-------|-------|
| **Visible orgs** | Contributed to MemPalace |
| **Severity** | **Minor** |

**Issues**:
- MemPalace contribution is visible in the activity feed but not prominently
  displayed. If the candidate is a member of the org, this should be visible.

---

## Section 3: Per-Repo Scorecard

### Scoring Key

- **README quality** (0–5): 0=none, 1=one-liner, 2=basic, 3=adequate,
  4=good, 5=exemplary
- **Commit hygiene** (0–5): 0=single commit dump, 1=poor messages, 2=mixed,
  3=adequate, 4=clean, 5=exemplary conventional commits
- **Showcase-readiness** (0–5): Would a recruiter be impressed?

| # | Repo | Description | Lang | README | Commit | Topics | License | Last Push | Showcase | Verdict |
|---|------|-------------|------|--------|--------|--------|---------|-----------|----------|---------|
| 1 | **AgenticCareerBoost** | Agentic Engineering setup to update my public profile and boost my tech career | TeX | 5/5 | 4/5 | None | GPL-3.0 | 2026-04-20 | 4/5 | **Enhance** — flagship |
| 2 | **P3CTeX** | Ultimate Latex Repository for PEC solving at UOC | TeX | 5/5 | 4/5 | None | GPL-3.0 | 2026-03-21 | 4/5 | **Enhance** — flagship |
| 3 | **p3cTeX-UMLST** | pgf-umlcd + listings packages modifications | TeX | 1/5 | 2/5 | None | GPL-3.0 | 2025-09-26 | 2/5 | **Enhance** (minor) |
| 4 | **Ironhack-IronBank** | Ironhack Microservices Final Project | — | 2/5 | 2/5 | None | None | 2022-09-24 | 2/5 | **Enhance** — salvageable |
| 5 | **FPP2024_TIPorHANG** | First Android + Kotlin hello world | Kotlin | 2/5 | 1/5 | None | GPL-3.0 | 2024-06-15 | 1/5 | **Archive** |
| 6 | **TXTO** | Convenient text manager for java console apps | Java | 1/5 | 1/5 | None | GPL-3.0 | 2022-10-12 | 1/5 | **Archive** |
| 7 | **Didac-dev-project** | Main summary and self presentation website | HTML | 0/5 | 1/5 | None | GPL-3.0 | 2022-09-30 | 0/5 | **Archive** |
| 8 | **art-scv-website** | (no description) | JS | 0/5 | 1/5 | None | None | 2022-06-10 | 0/5 | **Archive** |
| 9 | **scv-calculator** | IronHack Course preWork, only for test purposes | JS | 1/5 | 1/5 | None | None | 2022-06-05 | 0/5 | **Archive** |
| 10 | **DxM_Game_v3** | Just a grupal class project | Java | 0/5 | 1/5 | None | None | 2021-12-19 | 0/5 | **Archive** |
| 11 | **FileSaver.js** | An HTML5 saveAs() FileSaver implementation | — | N/A | N/A | — | — | 2022-10-21 | 0/5 | **Archive** (fork) |
| 12 | **DidacLL** | Config files for my GitHub profile | — | 1/5 | 1/5 | config | None | 2023-06-08 | 0/5 | **Rewrite** (profile README) |

### Detailed Repo Notes

**1. AgenticCareerBoost** — The strongest current asset. Excellent README with
mermaid diagrams, clear structure, professional tone. Demonstrates systems
thinking, documentation discipline, and agentic workflow design. Weaknesses:
no topics/tags set, repo description could be more polished for external
audiences ("boost my tech career" is too casual), language detected as TeX
rather than the more interesting aspects. The linked PDFs and site are the real
showcase. **Priority: high.**

**2. P3CTeX** — Genuinely impressive. A custom LaTeX document class with
multiple packages, test suites, agentic development workflow documentation, and
a well-structured README mixing English and Catalan. Shows deep technical
competence in TeX internals, build systems, and package architecture. The
"PROCRASTRINAR ES LA UNICA ESPERANZA" ASCII art header is charming but
unprofessional for a recruiter audience — a minor tone issue. Weaknesses: no
topics/tags, the name "P3CTeX" is opaque to outsiders (derived from UOC "PEC"
assignments), no description beyond "Ultimate Latex Repository for PEC solving
at UOC" which means nothing to a non-UOC reader. **Priority: high.**

**3. p3cTeX-UMLST** — A legitimate package extraction from P3CTeX. Shows
library isolation skills. But the README is a single line, no usage
instructions, no examples. Low standalone value without context.
**Priority: low.**

**4. Ironhack-IronBank_FinalProject_vBNKsys** — The only Java/Spring
microservices project. README exists but is rough: formatting issues, localhost
references, raw screenshot embeds, no architecture explanation beyond diagram
images. The repo name is terrible for discoverability
(`Ironhack-IronBank_FinalProject_vBNKsys`). This is a fork, which reduces
its signal. However, it is the only evidence of backend Java microservices
work, which aligns with the career target. It needs significant cleanup to be
showcase-worthy, and being a fork limits how much it can be improved.
**Priority: medium.**

**5. FPP2024_TIPorHANG** — A hangman game. "Just my first Android + Kotlin
hello world." The self-deprecating description actively harms credibility.
README is minimal. No showcase value. **Archive.**

**6. TXTO** — A Java text manager utility from 2022. One-line README.
Bootcamp-era utility code. No showcase value in current positioning.
**Archive.**

**7. Didac-dev-project** — The legacy portfolio site source. No README. The
site content is analyzed in Section 5. The repo itself is dead weight.
**Archive** (but keep the GitHub Pages deployment alive until the replacement
site is ready, then redirect or sunset).

**8. art-scv-website** — No description, no README. A JavaScript site from
2022-06. Appears to be a personal art portfolio attempt. Dead project.
**Archive.**

**9. scv-calculator** — IronHack prework. "Only for test purposes." Self-
described as disposable. **Archive.**

**10. DxM_Game_v3** — "Just a grupal class project." No README. Dead group
project from 2021. **Archive.**

**11. FileSaver.js** — A fork of an existing library. No original work visible.
Forks with no meaningful contributions are noise on a profile. **Archive** or
delete.

**12. DidacLL (profile README repo)** — The most impactful repo on the entire
profile because it renders on the profile page. Currently: 4 lines of broken
English, a link to the dead legacy site, and a reference to a mysterious
VladScv account. This is the #1 priority rewrite target. **Rewrite
immediately.**

### Cross-Cutting Issues

| Issue | Severity | Count |
|-------|----------|-------|
| No topics/tags on any repo | Major | 12/12 |
| Self-deprecating descriptions ("just a...", "only for test...") | Major | 4/12 |
| No README or single-line README | Major | 6/12 |
| No license on repos that should have one | Minor | 4/12 |
| Repos with no description at all | Major | 1/12 |
| Fork with no visible contribution | Minor | 2/12 |

---

## Section 4: Showcase Candidates

Based on the repo audit, the following repos are the strongest candidates for
recruiter-facing showcases.

### Candidate 1: AgenticCareerBoost

**Why it's strong**:
- Demonstrates the exact positioning from brand.md: systems-minded builder,
  agentic workflow designer, documentation discipline.
- The README is already well-structured with clear entry points for different
  audiences (readers, recruiters, collaborators, agents).
- The formal PDFs (Agentic System Guide, S-000 case study) provide deep
  evidence of engineering thinking that goes far beyond "I built a CRUD app."
- Active development (pushed today) shows current engagement.
- The meta-nature of the project (using agentic systems to build a career
  profile) is a conversation starter.

**Improvements needed**:
- Add GitHub topics: `agentic-systems`, `multiagent`, `career-development`,
  `documentation`, `model-agnostic`, `latex`.
- Rewrite the repo description to be less casual. Current: "Agentic
  Engineering setup to update my public profile and boost my tech career."
  Better: "Path-based, model-agnostic multiagent operating system for
  engineering career development — with formal reports, public site, and
  inspectable evidence trail."
- Ensure the GitHub Pages site is polished (it's linked from the README).
- Add a screenshot or architecture diagram directly in the README for visual
  impact.

**Maps to roles**: DevOps/platform engineering, developer tooling, technical
writing, AI/ML engineering (agentic systems), any role valuing documentation
and systems thinking.

### Candidate 2: P3CTeX

**Why it's strong**:
- A real, functional, multi-package LaTeX system with tests, documentation,
  and an agentic development workflow. This is not a toy project.
- 2 stars (modest but organic) and active development.
- Demonstrates: package architecture, build systems, expl3 programming,
  testing infrastructure, technical documentation in multiple languages.
- The agentic development workflow documentation (`workflow/`) is a
  differentiator — it shows the candidate applies AI-assisted development
  methodically, not as a toy.

**Improvements needed**:
- Rewrite the repo description. "Ultimate Latex Repository for PEC solving at
  UOC" is opaque. Better: "Custom LaTeX document class and package ecosystem
  for academic document production — with agentic development workflow, test
  suites, and full documentation."
- Add topics: `latex`, `tex`, `document-class`, `academic`, `uoc`,
  `open-source`, `agentic-workflow`.
- Consider toning down the ASCII art header or adding a professional lead-in
  paragraph before it.
- Add a "Gallery" or "Example Output" section with a PDF screenshot to show
  what documents produced with P3CTeX look like.

**Maps to roles**: Developer tooling, build systems, technical writing,
open-source engineering, any role that values deep technical craftsmanship.

### Candidate 3: Ironhack-IronBank_FinalProject_vBNKsys (conditional)

**Why it could be strong**:
- The only Java/Spring Boot microservices project. Directly relevant to
  backend engineering roles.
- Uses real technologies: Java 18, Maven, Spring Boot, Keycloak, OpenAPI.
- Has architecture diagrams.

**Why it's currently weak**:
- It's a fork, not an original repo. This limits credibility.
- The README is rough and reads like a rushed bootcamp submission.
- The repo name is unprofessional and unsearchable.
- Last pushed in 2022 — stale.

**Improvements needed** (if pursuing this as a showcase):
- Since it's a fork, improvements are limited. Consider creating a new repo
  with a clean name (e.g., `ironbank-microservices`) that contains the cleaned
  code, better README, and architecture documentation.
- Rewrite the README with: project overview, architecture decisions, tech
  stack, setup instructions, what was learned.
- Add a proper license.

**Maps to roles**: Java backend developer, microservices engineer, Spring Boot
positions.

**Alternative**: If the IronBank project cannot be meaningfully improved (fork
limitation), the third showcase slot could go to a **new project** built during
S-001 or later sprints — e.g., a Java/Kotlin utility that demonstrates current
coding ability.

---

## Section 5: Legacy Site Audit

**URL**: https://didacll.github.io/AgenticCareerBoost/  
**Source**: https://github.com/DidacLL/Didac-dev-project

### 5.1 Content Quality and Relevance

| Aspect | Finding | Severity |
|--------|---------|----------|
| **Date** | "Barcelona, 2022" — frozen in time | **Critical** |
| **Self-description** | "I'm a 90s younger, professional visual Artist who started coding during the lockdown in 2020" | **Critical** |
| **Positioning** | "I'm looking for a company who could lead me to the proper way to start what would be, for sure, a great Tech career" | **Critical** |
| **Skills listed** | Java 18, Spring, WebFlux, libGDX, JS, CSS, HTML5, C, MySQL | **Major** — frozen at 2022 |
| **Experience** | "+10 years of experience working on customer service and helpdesk" | **Major** — undersells (actual: 15 years) |
| **Education** | UOC degree listed as "Current" with no expected completion date | **Major** |
| **Tone** | "Friendly :)" / "Open to new challenges" / "I love programming" | **Critical** — reads as junior/desperate |
| **Grammar** | Multiple errors: "on process", "andI'm", "by nowI'm", missing spaces | **Major** |
| **Art skills section** | Listed but irrelevant to tech hiring without framing | **Minor** |
| **Soft skills** | Generic ("Open to new challenges", "Naturally creative") | **Major** |

**Summary**: The content is a 2022 bootcamp-era self-presentation that
actively contradicts the target brand. The tone is apologetic, junior-coded,
and positions the candidate as someone begging for an opportunity rather than
someone bringing value. Every sentence would need rewriting to align with
current positioning.

### 5.2 Code/Structure Quality

| Aspect | Finding | Severity |
|--------|---------|----------|
| **Technology** | Static HTML — no framework, no build system | **Minor** (acceptable for a personal page) |
| **Markup** | Uses heading tags as visual styling, not semantic structure | **Major** |
| **Code-themed formatting** | Content wrapped in fake code syntax: `Didac Llorens(){ ... };` | **Major** — gimmicky |
| **`@Deprecated` annotation** | Used to mark previous experience | **Minor** — clever but unprofessional |

### 5.3 SEO Issues

| Aspect | Finding | Severity |
|--------|---------|----------|
| **Page title** | "Dídac CV" — not descriptive | **Major** |
| **Meta description** | Likely absent (static HTML, no meta tags visible) | **Major** |
| **Structured data** | None (no JSON-LD, no schema.org) | **Major** |
| **Alt text** | No images visible to audit | **Minor** |
| **URL structure** | `/Didac-dev-project/` — acceptable | **Minor** |
| **Canonical URL** | Likely not set | **Minor** |

### 5.4 AI-Readable Metadata

| Aspect | Finding | Severity |
|--------|---------|----------|
| **Can an AI recruiter bot extract useful info?** | Partially — plain text is parseable, but code-syntax formatting (`{`, `}`, `;`) would confuse entity extraction | **Major** |
| **Structured data for skills** | None | **Major** |
| **Contact information** | Not visible | **Major** |
| **Social/professional links** | Not visible | **Major** |

### 5.5 Mobile Responsiveness

| Aspect | Finding | Severity |
|--------|---------|----------|
| **Responsive design** | Unknown — static HTML without visible viewport meta or media queries would likely render poorly on mobile | **Major** [INFERRED] |

### 5.6 Accessibility

| Aspect | Finding | Severity |
|--------|---------|----------|
| **Semantic HTML** | Poor — headings used for visual styling | **Major** |
| **ARIA labels** | Likely none | **Major** |
| **Color contrast** | Unknown without visual render | **Minor** |
| **Keyboard navigation** | Likely basic (static page) | **Minor** |

### 5.7 Design/UX Quality

| Aspect | Finding | Severity |
|--------|---------|----------|
| **Visual design** | Code-themed aesthetic — dark background, monospace font, syntax coloring | **Minor** (subjective) |
| **User experience** | Single long scroll, no navigation, no clear CTA | **Major** |
| **Professional impression** | Reads as a bootcamp student portfolio, not a professional engineering presence | **Critical** |

### 5.8 Brand Alignment

| Brand principle | Site alignment | Severity |
|-----------------|----------------|----------|
| Systems-minded builder | Not evidenced | **Critical** |
| Technical generalist | Partially (skills listed) but outdated | **Major** |
| Agentic workflow designer | Not mentioned | **Critical** |
| Technical, disciplined tone | Violated — tone is casual, junior, apologetic | **Critical** |
| "Never 'just another junior'" | The entire site screams "just another junior" | **Critical** |
| No AI-hype | Compliant (no AI mention at all) | OK |
| No founder-LARP | Compliant | OK |

**Verdict**: The legacy site is a **net negative** for the candidate's current
positioning. It should be replaced as soon as the new site (from
AgenticCareerBoost) is ready. Until then, the profile README should stop
linking to it.

---

## Section 6: Cross-Surface Consistency

### 6.1 Narrative Consistency

| Dimension | LinkedIn | GitHub | Legacy Site | Consistent? |
|-----------|----------|--------|-------------|-------------|
| **Name** | Dídac Llorens Bravo | Didac Ll. | Didac Llorens | Partial — full name on LinkedIn, abbreviated on GitHub, no surname variant on site |
| **Location** | Barcelona, Catalonia, Spain | Barcelona | Barcelona, 2022 | Yes (but site is time-frozen) |
| **Headline/positioning** | MicroServices Backend Java lover | (empty) | 90s visual artist who codes | **No** — three completely different identities |
| **Current role/status** | Not visible | Not visible | "Looking for a company" | **No** — no consistent current narrative |
| **Education** | UOC 2021–2026 | Not mentioned | UOC "Current" | Partial — dates differ (2026 vs 2027) |
| **IronHack** | Listed (2022) | IronBank project exists | Listed | Yes |
| **Tech stack** | Java, implied backend | TeX-heavy profile | Java 18, Spring, WebFlux, JS | Partial |
| **Years of non-tech experience** | Not visible | Not mentioned | "+10 years" | Inconsistent (actual: ~15 years) |
| **Art/design background** | Not visible | Not mentioned | Prominently listed | Inconsistent |

### 6.2 Contradictions and Gaps

| # | Issue | Severity |
|---|-------|----------|
| 1 | **Three different identities**: LinkedIn says "Java backend microservices dev", GitHub says nothing, legacy site says "visual artist who started coding." A recruiter checking all three would be confused. | **Critical** |
| 2 | **No mention of agentic systems work anywhere except the AgenticCareerBoost repo itself.** This is the candidate's strongest differentiator and it's invisible. | **Critical** |
| 3 | **No mention of P3CTeX or LaTeX expertise on LinkedIn or the legacy site.** The most technically impressive work is invisible outside GitHub. | **Critical** |
| 4 | **UOC graduation date inconsistency**: LinkedIn says 2026, actual is Feb 2027. | **Major** |
| 5 | **Non-tech experience duration inconsistency**: site says "+10 years" but actual is ~15 years. | **Major** |
| 6 | **VladScv reference** in GitHub profile README is unexplained. If this is an alt account or a contact redirect, it confuses the identity chain. | **Major** |
| 7 | **MemPalace contribution** (48K+ star project) is visible in GitHub activity but not mentioned on any surface. If the contribution is meaningful, this is a massive missed opportunity. | **Major** |
| 8 | **ML/AI mention** from the UOC degree is invisible everywhere. Given the target interest in "model-agnostic AI engineering," this gap undermines the claim. | **Major** |
| 9 | **Bootcamp completion dates** are not cross-referenced: IronHack (2022), ITAcademy FullStack React (not visible anywhere), Linux Admin PUE (not visible anywhere), Fundación Francisco Puerto Android (not visible anywhere). | **Major** |
| 10 | **Legacy site is still the linked "resume"** from the GitHub profile README, but it contradicts the positioning the candidate is trying to build. Every surface that links to it amplifies the damage. | **Critical** |

### 6.3 Search Visibility: "Dídac Llorens Barcelona developer"

A recruiter searching this query would likely find:

1. **LinkedIn profile** — the strongest SEO result, but with a stale 2022
   headline and minimal content.
2. **GitHub profile** — empty bio, stale profile README, TeX-dominated repo
   list.
3. **Legacy site** — "90s visual artist looking for a company to start a tech
   career."
4. **UOC records** — possibly, but these are institutional and not controlled.

**Net impression**: "Career changer, bootcamp background, 2022 output, no
evidence of current engineering capability." This is the opposite of the
intended brand.

---

## Consolidated Priority Matrix

### Critical (Blocks Hiring) — Fix Immediately

| # | Item | Surface |
|---|------|---------|
| C1 | Rewrite GitHub profile README (DidacLL/DidacLL) | GitHub |
| C2 | Set GitHub bio | GitHub |
| C3 | Rewrite LinkedIn headline | LinkedIn |
| C4 | Write/rewrite LinkedIn About section | LinkedIn |
| C5 | Stop linking to legacy site from any surface | All |
| C6 | Add current engineering work to LinkedIn Experience | LinkedIn |
| C7 | Unify the narrative across all three surfaces | All |

### Major (Significantly Weakens Profile) — Fix in S-001

| # | Item | Surface |
|---|------|---------|
| M1 | Set GitHub website and social links | GitHub |
| M2 | Pin correct repos on GitHub | GitHub |
| M3 | Add topics/tags to all kept repos | GitHub |
| M4 | Archive 6–7 dead repos | GitHub |
| M5 | Rewrite P3CTeX and AgenticCareerBoost repo descriptions | GitHub |
| M6 | Populate LinkedIn Featured section | LinkedIn |
| M7 | Rebuild LinkedIn Skills section | LinkedIn |
| M8 | Request LinkedIn recommendations | LinkedIn |
| M9 | Rewrite LinkedIn Education entries (UOC date, ML/AI mention) | LinkedIn |
| M10 | Begin LinkedIn posting cadence | LinkedIn |
| M11 | Fix self-deprecating repo descriptions | GitHub |
| M12 | Investigate and document MemPalace contribution | GitHub/LinkedIn |
| M13 | Verify and surface all bootcamp credentials consistently | All |

### Minor (Polish Items) — Fix When Convenient

| # | Item | Surface |
|---|------|---------|
| m1 | Add license to repos missing one | GitHub |
| m2 | Improve p3cTeX-UMLST README | GitHub |
| m3 | Add profile photo/banner assessment | LinkedIn |
| m4 | Clean up DidacLL/DidacLL repo topics | GitHub |

---

*End of audit. This report is evidence-based and reflects the state of all
surfaces as of 2026-04-20. Items marked [INFERRED] require manual verification
due to scraping limitations on LinkedIn.*


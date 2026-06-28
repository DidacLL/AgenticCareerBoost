# Repository Metadata Updates — All Public Repos

- **Sprint**: S-001 / T5
- **Agent**: CommunityManager
- **Date**: 2026-04-20
- **Target**: All public repos under `github.com/DidacLL`
- **Inputs**: T3 profile audit (§3 per-repo scorecard), T4 positioning synthesis

---

## Overview

The T3 audit identified 12 public repositories. This document provides a verdict, updated metadata, and action items for each. Repos are organized into three categories: **Keep & Enhance**, **Rewrite** (profile README), and **Archive**.

### Verdict Summary

| Category | Repos | Count |
|----------|-------|-------|
| **Keep & Enhance** | AgenticCareerBoost, P3CTeX, p3cTeX-UMLST, Ironhack-IronBank | 4 |
| **Rewrite** | DidacLL (profile README) | 1 |
| **Archive** | FPP2024_TIPorHANG, TXTO, Didac-dev-project, art-scv-website, scv-calculator, DxM_Game_v3, FileSaver.js | 7 |

### Pinned Repos (new order)

After applying all verdicts, pin these repos in this order:

| Pin # | Repo | Why |
|-------|------|-----|
| 1 | **AgenticCareerBoost** | Flagship. Systems thinking, agentic engineering, documentation discipline. |
| 2 | **P3CTeX** | Technical depth. LaTeX mastery, package architecture, OSS discipline. |
| 3 | **Ironhack-IronBank_FinalProject_vBNKsys** | Only Java/Spring evidence. Backend credibility for Angle D. |
| 4 | **p3cTeX-UMLST** | Library extraction. Shows modular thinking. (Optional — unpin if a new ML project is built.) |

---

## Keep & Enhance

### 1. AgenticCareerBoost

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Enhance** — flagship | |
| **Description** | `Agentic Engineering setup to update my public profile and boost my tech career` | `Path-based, model-agnostic multi-agent operating system for engineering career development — formal reports, public site, inspectable evidence trail` |
| **Website** | Current public site | `https://didacll.github.io/` |
| **Topics** | None | `agentic-systems` · `multiagent` · `model-agnostic` · `career-development` · `documentation` · `latex` · `python` · `systems-design` |

**Additional actions**:
- Confirm the GitHub Pages site is polished and accessible
- Consider adding an architecture diagram or screenshot directly in the README for visual impact (style-book.md §5: "prefer diagrams over selfies")
- The description change reframes the repo for external audiences — "boost my tech career" is too casual for recruiter scanning

**Source**: T3 §3 (repo #1), T3 §4 (Candidate 1), T4 §5.3 M4.

---

### 2. P3CTeX

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Enhance** — flagship | |
| **Description** | `Ultimate Latex Repository for PEC solving at UOC` | `Custom LaTeX document class and package ecosystem for academic document production — test suites, agentic dev workflow, multi-language docs` |
| **Website** | None | Add only after a demo page or PDF gallery exists |
| **Topics** | None | `latex` · `tex` · `document-class` · `expl3` · `academic` · `open-source` · `agentic-workflow` · `uoc` |

**Additional actions**:
- Consider toning down or moving the ASCII art header ("PROCRASTRINAR ES LA UNICA ESPERANZA") — it is charming but unprofessional for a recruiter audience. Options: (a) move it below the professional lead-in paragraph, (b) reduce its visual dominance, (c) keep it as a deliberate cultural signal if that tradeoff is accepted.
- Add a "Gallery" or "Example Output" section with a PDF screenshot showing what P3CTeX-produced documents look like
- The description change removes UOC jargon ("PEC") that means nothing to non-UOC readers

**Source**: T3 §3 (repo #2), T3 §4 (Candidate 2), T4 §5.3 M4.

---

### 3. p3cTeX-UMLST

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Enhance** (minor) | |
| **Description** | `pgf-umlcd + listings packages modifications` | `UML diagram and code listing LaTeX packages — extracted from P3CTeX for standalone use` |
| **Website** | None | None needed |
| **Topics** | None | `latex` · `uml` · `pgf` · `listings` · `tex-package` |

**Additional actions**:
- Expand the README to include: what the package does, installation instructions, a minimal usage example, and a link back to P3CTeX
- Low priority — focus on the two flagships first

**Source**: T3 §3 (repo #3).

---

### 4. Ironhack-IronBank_FinalProject_vBNKsys

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Enhance** — salvageable (conditional) | |
| **Description** | `Ironhack Microservices Final Project` | `Java/Spring Boot microservices banking simulation — Keycloak auth, OpenAPI docs, multi-service architecture (IronHack 2022 capstone)` |
| **Website** | None | None (localhost project) |
| **Topics** | None | `java` · `spring-boot` · `microservices` · `keycloak` · `openapi` · `banking` · `bootcamp-project` |

**Additional actions**:
- This is a fork, which limits improvement options. Consider creating a new repo (`ironbank-microservices`) with cleaned code, better README, and architecture documentation if Angle D (Backend) becomes an active application strategy
- If keeping the fork: rewrite the README with a proper project overview, architecture decisions, tech stack table, and setup instructions. Remove localhost references and raw screenshot embeds
- Add a license (MIT or Apache 2.0 recommended for portfolio projects)
- The repo name is unprofessional and unsearchable, but cannot be changed since it is a fork

**Priority**: Medium. Execute only if Backend + Platform applications become active, or if a recruiter specifically asks about Java/Spring experience.

**Source**: T3 §3 (repo #4), T3 §4 (Candidate 3).

---

## Rewrite

### 5. DidacLL (Profile README repo)

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Rewrite** — #1 priority | |
| **Description** | `Config files for my GitHub profile` | `Profile README` (or leave blank) |
| **Topics** | `config` · `github-config` | Remove all topics |
| **README** | 4 lines of broken English, legacy site link, VladScv reference | **Full rewrite** — see `github-profile-readme.md` in this directory |

**Actions**:
1. Replace the entire README.md content with the draft from `github-profile-readme.md`
2. Remove the topics `config` and `github-config`
3. Confirm the profile renders correctly after push

**Source**: T3 §3 (repo #12), T3 §2.2, T4 §5.3 C2.

---

## Archive

> **Archive** = make the repo private or use GitHub's archive feature (Settings → Danger Zone → Archive this repository). Archived repos remain accessible via direct URL but do not appear in the profile's public repo list and cannot accept new issues/PRs.

> **Important**: Do NOT delete any repos. Archive them. Deletion is irreversible and may break external references.

### 6. FPP2024_TIPorHANG

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Archive** | |
| **Current description** | `First Android + Kotlin hello world` | N/A (archiving) |
| **Reason** | Self-deprecating description ("just my first"). No showcase value. A hangman game does not support any target positioning angle. The Kotlin/Android skill is captured in LinkedIn education section instead. |

**Source**: T3 §3 (repo #5).

---

### 7. TXTO

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Archive** | |
| **Current description** | `Convenient text manager for java console apps` | N/A (archiving) |
| **Reason** | Bootcamp-era utility from 2022. One-line README. No showcase value in current positioning. Java skill is better demonstrated by IronBank and AgenticCareerBoost. |

**Source**: T3 §3 (repo #6).

---

### 8. Didac-dev-project

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Archive** (but keep GitHub Pages live temporarily) | |
| **Current description** | `Main summary and self presentation website` | N/A (archiving) |
| **Reason** | Legacy portfolio site. T3 §5 verdict: "net negative for current positioning." Content is frozen at 2022, tone is apologetic and junior-coded, contradicts target brand on every dimension. |

**Special handling**:
- **Do NOT archive yet if GitHub Pages is still the primary web presence.** Wait until the AgenticCareerBoost site is fully deployed and linked from all surfaces.
- **Immediately**: Remove all links to this site from other surfaces (GitHub profile README, LinkedIn, etc.). The site can exist passively but should not be discoverable from any controlled surface.
- **After replacement site is live**: Archive the repo and optionally add a redirect.

**Source**: T3 §3 (repo #7), T3 §5, T4 §5.4.

---

### 9. art-scv-website

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Archive** | |
| **Current description** | (none) | N/A (archiving) |
| **Reason** | No description, no README. Personal art portfolio attempt from 2022. Dead project with no engineering signal. |

**Source**: T3 §3 (repo #8).

---

### 10. scv-calculator

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Archive** | |
| **Current description** | `IronHack Course preWork, only for test purposes` | N/A (archiving) |
| **Reason** | Self-described as disposable ("only for test purposes"). IronHack prework with no showcase value. Actively harmful to professional image. |

**Source**: T3 §3 (repo #9).

---

### 11. DxM_Game_v3

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Archive** | |
| **Current description** | `Just a grupal class project` | N/A (archiving) |
| **Reason** | Self-deprecating description ("just a"). Dead group project from 2021. No README. No engineering signal. |

**Source**: T3 §3 (repo #10).

---

### 12. FileSaver.js

| Field | Current | Updated |
|-------|---------|---------|
| **Verdict** | **Archive** (or delete) | |
| **Current description** | `An HTML5 saveAs() FileSaver implementation` | N/A (archiving) |
| **Reason** | Fork of an existing library with no visible original contribution. Forks without meaningful contributions are noise on a profile. |

**Note**: Deleting a fork is acceptable since the original repo still exists. However, archiving is safer if there is any doubt.

**Source**: T3 §3 (repo #11).

---

## Cross-Cutting Actions

These actions apply to ALL kept repos:

| # | Action | Repos Affected | Priority |
|---|--------|----------------|----------|
| 1 | **Add topics/tags** (as specified above) | AgenticCareerBoost, P3CTeX, p3cTeX-UMLST, IronBank | High — 0/12 repos currently have topics |
| 2 | **Remove self-deprecating descriptions** | FPP2024 ("just my first"), scv-calculator ("only for test"), DxM ("just a") — all being archived, so descriptions become moot | Resolved by archiving |
| 3 | **Add license to repos missing one** | IronBank (no license), p3cTeX-UMLST (has GPL-3.0 — OK) | Low |
| 4 | **MemPalace contribution deferred** | Profile README, LinkedIn | Medium — use only after contribution scope is documented precisely |
| 5 | **Update AgenticCareerBoost language detection** | AgenticCareerBoost | Low — GitHub detects TeX as primary language due to LaTeX files. Consider adding a `.gitattributes` file to classify `.tex` files or ensure Python files are prominent enough for detection. |

---

## Execution Order

1. **Immediately (S-001)**:
   - Rewrite DidacLL/DidacLL profile README (repo #5 / File 2 of T5)
   - Update AgenticCareerBoost description and topics (repo #1)
   - Update P3CTeX description and topics (repo #2)
   - Remove legacy site links from all controlled surfaces
   - Pin repos in new order: AgenticCareerBoost → P3CTeX → IronBank → p3cTeX-UMLST

2. **Soon (S-001, secondary)**:
   - Archive: FPP2024_TIPorHANG, TXTO, art-scv-website, scv-calculator, DxM_Game_v3, FileSaver.js
   - Update p3cTeX-UMLST description and topics
   - Update IronBank description and topics
   - Confirm MemPalace contribution scope before using it publicly

3. **When replacement site is live (S-002)**:
   - Archive Didac-dev-project
   - Update all website links to new site URL

---

## Checks

- [x] Every repo has a verdict (Keep/Archive/Enhance/Rewrite)
- [x] Every kept repo has a new description
- [x] Every kept repo has topics/tags
- [x] No self-deprecating descriptions remain on visible repos
- [x] Pin order reflects T4 positioning priorities
- [x] Execution order respects dependencies (e.g., don't archive Didac-dev-project until replacement site is live)
- [x] No repos deleted (archived only)

---

*Draft produced by CommunityManager agent, S-001 T5. All archiving and metadata changes require explicit review before execution.*


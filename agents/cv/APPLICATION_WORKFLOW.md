# Tailored application workflow

This file is active guidance for agents preparing job-application material for Dídac from this repository. It defines the local CV/cover-letter workflow; it is not a request to commit real application material.

Direct user instructions still have highest authority. Real offers, recruiter messages, tailored CVs/letters, private JSON and generated private PDFs remain local and untracked.

## Default deliverable semantics

Interpret the user's requested artifact before writing:

| User request | Default output |
| --- | --- |
| `CV` | one-page tailored CV TeX |
| `CV + carta`, `CV + carta adjunta`, `CV con carta` | one TeX document that renders as **page 1 CV + page 2 cover letter** |
| `carta` / separate cover letter | use the local `application-tracker/letter.ps1 <slug>` renderer when a standalone letter artifact is wanted |
| platform form/text-box letter | one-page CV TeX plus the letter/form text separately; do not add a second PDF page unless requested |

`Carta adjunta` therefore means a second page in the same application document by default, not a separate JSON file, separate PDF, or another workspace.

Produce the requested local artifact directly. Do not redirect an application-artifact request into site publication, AAAAT development, another workspace, or a different product flow.

## Canonical CV architecture

Tailored CVs reuse the public CV system rather than inventing a new template:

```tex
\documentclass[a4paper,10pt]{article}
\input{didac-cv-shared-preamble-v1.tex}

\cvsetup
  {role label}
  {headline}
  {evidence-backed parser keywords}
  {evidence-backed parser summary}

\begin{document}
  \cvheader
  ...
\end{document}
```

The source should compile from `agents/cv/tex/`, where the shared preamble and `418-banner.png` are siblings. Tailored variants remain local/untracked unless the owner explicitly promotes one.

### Page-one rule

The tailored CV is **one page**. Do not solve overflow by growing it into a multi-page CV. Reduce repetition and select evidence.

The main column begins with `\cvAbstract{...}` immediately after `\small`. The abstract is the narrative opener and should establish the candidate's direction and strongest fit in a compact paragraph. Do not replace it with a generic profile section or bury it below project history.

A normal tailored page contains:

1. header;
2. concise rail with complementary scan information;
3. `\cvAbstract{...}`;
4. three or four selected projects / evidence blocks;
5. a short role-fit or engineering-depth section;
6. concise prior professional background where relevant;
7. education.

The rail is a secondary scan surface, not a second summary. Avoid repeating the abstract verbatim in the rail.

Use the existing design and shared macros. Do not create a new visual language, generic ATS template, giant skills inventory, multi-column redesign, or long chronological resume unless explicitly asked.

## Tailoring rules

Tailor by selecting and reframing true evidence, not by copying the vacancy into the CV.

- Prefer 3--4 projects whose real implementation evidence answers the role.
- Keep professional employment, project work, academic work and familiarity distinct.
- Do not convert project/academic years into `professional experience` unless the question explicitly allows general hands-on experience.
- UOC degree is in progress; expected completion is February 2027. Do not state it as completed.
- English is advanced / B2+ unless stronger evidence is supplied.
- Do not claim practical AWS, Azure, Microsoft 365 or another platform merely because the vacancy requests it.
- Real Docker/Kubernetes, GitHub Actions, Python, TypeScript, Java/Spring, Linux, testing and project evidence may be used where relevant.
- Prior banking, insurance, telecom, support and incident work is useful domain/operational evidence but must not be represented as software-engineering employment.
- Application language normally follows the vacancy language unless the user asks otherwise.

Do not lead with gaps. Omit unsupported requirements from the CV and, only when strategically useful, contextualize one important ramp-up area positively in the letter.

## Abstract and parser summary are separate surfaces

`\cvAbstract{...}` is visible human-facing narrative. `\cvParserSummary` is an ATS/AI-readable support surface.

Both must be truthful, but they serve different purposes:

- **Abstract:** compact, natural, role-specific explanation of direction and evidence.
- **Parser summary:** explicit machine-readable wording that makes supported skills, role family and project evidence easy to retrieve.

`\cvsetup` role keywords and role summary should therefore use exact vacancy vocabulary when that vocabulary is genuinely supported. Never keyword-stuff unsupported tools into hidden text or metadata. The parser surface may make true evidence easier to find; it must not create new claims.

When an employer explicitly states that AI/ATS systems review applications, it is legitimate to be especially deliberate about the parser summary, metadata and exact supported terminology.

## Cover letter in a combined document

When the user asks for `CV + carta adjunta`, finish the one-page CV, then use `\newpage` and render a one-page letter in the **same TeX document**.

The letter should normally:

- address the actual company/role;
- explain why the concrete engineering problem is relevant;
- select two or three pieces of evidence rather than restating the whole CV;
- distinguish junior professional software/AI status from the owner's much longer prior professional experience;
- show mature judgment and ownership without presenting the candidate as senior if the role is junior;
- avoid servile language, vacancy paraphrase, exaggerated enthusiasm and generic `fast learner` claims;
- avoid recruiter-visible claim-control/meta language;
- avoid salary discussion unless requested;
- fit on one page.

For roles strongly related to agentic engineering, do not reduce the story to `uses Codex/Claude`. ACB, AAAAT/VCVGenerator and MADRE provide deeper evidence around provider-independent orchestration, context/authority boundaries, anti-drift design, runtime behavior, local inference, validation and replaceable execution clients.

## Evidence selection reminders

Use repository evidence before novel strong claims. Common project angles include:

- **AgenticCareerBoost:** career-engineering workspace, agentic workflow experiments, job-offer/application support, social/research work, multilingual Astro portfolio, LaTeX CV/document pipeline, Git/GitHub Actions, privacy boundaries and inspectable engineering history.
- **AAAAT + VCVGenerator:** local-first domain application, Electron/React/TypeScript/SQLite, candidature/professional information, independently useful CV/letter tooling, bounded optional AI, typed/validated operations, product authority and anti-drift governance.
- **MADRE:** Python/FastAPI runtime, durable execution, scheduling/recovery, idempotency/retry/cancel, local inference, capability selection, SDK/security boundaries and model/provider independence.
- **P3CTeX:** LaTeX2e/expl3 engineering, reusable document APIs, deterministic rendering and regression testing.
- **IronBank:** Java/Spring Boot, REST, persistence, microservice/backend foundations.

Do not flatten ACB into only an old coding-agent harness. Its active repository is broader career tooling and public engineering infrastructure; the historical richer harness is evidence where relevant, not the whole project.

## Local compilation

For a tailored TeX variant, compile from the canonical TeX root so sibling assets resolve:

```powershell
Push-Location agents/cv/tex
latexmk -r ../latexmkrc -pdf -interaction=nonstopmode -halt-on-error -outdir=../build -auxdir=../build <tailored-source>.tex
Pop-Location
```

If `latexmk` is unavailable, use the existing pdfLaTeX-compatible setup and keep generated auxiliaries out of the source directory.

Do not add a tailored application to `artifacts.json` or publish it to the portfolio unless the owner explicitly asks.

## Separate letter renderer

The existing `application-tracker/letter.ps1 <slug>` flow remains the local standalone-letter path. It is useful when the platform wants a separate cover letter artifact.

It is **not** the default for `CV + carta adjunta`, because that request means one combined two-page application document unless the user or application platform says otherwise.

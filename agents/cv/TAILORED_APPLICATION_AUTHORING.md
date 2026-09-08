# Tailored application authoring

## Scope boundary

This guide applies **only** when the active task is to create or tailor application material for a specific vacancy, for example:

- a private role-specific CV using the shared ACB LaTeX preamble;
- a private cover-letter JSON for the existing `application-tracker` renderer;
- a combined private CV + cover-letter `.tex` when the user explicitly wants both in one document.

Do **not** apply this guide to unrelated ACB work. In particular, it does not govern:

- publishing, redesigning, or maintaining the portfolio site;
- the public/general CV build or artifact-publication pipeline;
- research or development of Application Tracker, AAAAT, or VCVGenerator;
- repository cleanup, CI maintenance, reports, market research, or other agent workflows.

This document is an authoring convention for private application outputs, not a new product architecture or repository-wide policy.

## Private-output boundary

Tailored CVs, real vacancy text, recruiter data, application-specific JSON, and generated private PDFs remain local and untracked. Reuse the public shared preamble, but do not add real tailored application material to the repository.

Do not change `artifacts.json`, the public CV publication flow, or `application-tracker` implementation merely to produce a private application unless the user explicitly asks for those changes.

## Claim discipline

Tailor aggressively, but never manufacture experience.

- Distinguish a skill that is known, used in a project, used professionally, adjacent, or merely requested by the vacancy.
- Inspect current repository evidence when a technical claim matters; do not rely on stale notes if the code can answer the question.
- Do not present coursework or personal projects as professional production experience.
- Do not present an in-progress degree as completed.
- Do not use hidden PDF metadata or ATS keywords to smuggle unsupported technologies in as apparent skills.
- If a requested technology is absent, normally omit it from the CV rather than advertising the absence. Explain one material transition point in the letter only when it helps the application remain accurate.

The visible CV is a case for the candidate, not an audit report. Do not add sections such as `Current gaps`, `Missing skills`, `Not claimed`, or similar defensive disclaimers to the first page.

## CV structure

A tailored CV normally remains **one page**. It should be dense enough to look complete without becoming a wall of text.

Use the shared preamble:

```tex
\documentclass[a4paper,10pt]{article}
\input{didac-cv-shared-preamble-v1.tex}
```

Use `\cvsetup{...}` for the role-specific headline and metadata, then keep the two-column architecture already established by the shared preamble.

### Visual reading order

The main column is the reader's primary entry point. The narrow rail is supporting scan information, not the narrative introduction.

Immediately after `\small` in the main-column minipage, place a short unheaded opening with `\cvAbstract{...}`:

```tex
\begin{minipage}[t][\BodyHeight]{\MainWidth}
  \small

  \cvAbstract{
    A concise role-specific introduction that establishes the candidate's
    direction, strongest evidence, and relevant professional maturity.
  }

  \mainsection{Backend engineering}
  ...
\end{minipage}
```

`\cvAbstract` is the actual opening statement of the CV. It should usually be one compact paragraph and should answer, at a glance, why this profile makes sense for this role.

Do **not** copy the rail `Profile` paragraph into `\cvAbstract`. The two areas have different jobs:

- **Rail profile:** compact identity/scan layer; short technical direction plus useful context.
- **`\cvAbstract`:** narrative opening; role-specific value proposition and strongest evidence.
- **First `\mainsection`:** advance the story into engineering focus, domain fit, or selected work; do not introduce the candidate a third time.

### Density and selection

Aim for balanced visual density across the page.

- Do not solve overflow by stripping the CV until large empty areas remain.
- Do not fill whitespace by restating every vacancy requirement.
- Prefer 3–4 selected projects with enough detail to show what was actually built.
- Prefer concrete engineering nouns and decisions over generic claims such as `passionate`, `innovative`, or `fast learner`.
- Add a short professional-transfer section when prior banking, insurance, telecom, support, incidents, risk, or regulated-operations experience materially strengthens the role.
- Keep the rail useful: stack, engineering practices, domain strengths, languages, and links. It should support scanning without competing with the main body.

Project descriptions should state evidence: architecture, services, persistence, APIs, validation, automation, CI, testing, documents, or other real work. Do not turn the project block into a description of the vacancy.

## Cover-letter modes

Choose exactly the delivery mode the user requests.

### Separate cover letter

When the cover letter is separate, create:

1. the tailored CV `.tex`; and
2. an application-specific JSON compatible with the preserved `application-tracker` renderer.

The JSON shape is the one documented in `application-tracker/USAGE.md`, including:

```text
slug
output_pdf
candidate_name
headline
email
portfolio_url
github_url
linkedin_url
recipient
role
location
greeting
paragraphs
closing
public_note
parser_summary
keywords
```

Keep the real JSON private/local. The repository workflow remains:

```powershell
cd application-tracker
.\letter.ps1 <slug>
```

### Combined CV + cover letter

When the user asks for `CV + cover letter together`, `carta conjunta`, or equivalent, produce one `.tex` with:

- page 1: tailored CV;
- page 2: cover letter after `\newpage`.

Do not also create a JSON letter unless the user asks for both formats.

### No cover letter requested

Do not invent one merely because a vacancy exists. If the portal only asks for a short message, write the short message instead.

## Cover-letter writing

The letter should add information rather than repeat the CV.

- Match the vacancy/application language unless the user instructs otherwise.
- Be direct, credible, technically precise, and specific to the candidate's evidence.
- Do not paraphrase the employer's own job description back to them.
- Do not write generic junior enthusiasm about AI, software, innovation, or learning.
- Use projects to explain concrete decisions, implementation choices, ownership, or transferable engineering practice.
- Use prior professional experience when it gives real domain or operational credibility.
- If one required technology is a material gap, address it once and briefly in context; explain the transferable foundation without apologising or listing every missing tool.

A strong letter generally answers: what relevant work has already been done, what judgement or transferable experience the candidate brings, and why this particular role is a coherent next environment for that work.

## Final authoring checks

Before delivering a tailored application artifact:

- the CV is one page unless the user explicitly asked for another format;
- an integrated letter starts on page 2;
- `\cvAbstract` is present at the top of the main column and does not duplicate the rail profile;
- the page is neither visibly sparse nor cramped;
- visible sections sell evidence and fit rather than advertise gaps;
- project claims are supported by current evidence;
- unsupported vacancy technologies are not inserted as hidden ATS claims;
- the degree remains described as in progress when applicable;
- real tailored outputs remain local and untracked;
- public CV/build/site/application-tracker product workflows were not changed as a side effect of authoring the application.

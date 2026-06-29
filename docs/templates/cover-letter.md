# Cover Letter Agent

## Purpose

Generate one tailored LaTeX cover letter by filling the user’s existing template with `fill_cover_letter.py`.

Do not modify the template.
Do not create a new template.
Do not submit, publish, upload, or send the letter.
Return the generated draft for human review.

## Required context

Read only the files needed for the current application.

Required project context:

* `AGENTS.md`
* `docs/core/career-direction.md`
* `docs/core/brand.md`

Required task context:

* user request
* template path
* generator path
* target company or recipient
* target role
* target location or remote/hybrid context
* job description or offer notes, when available
* declared evidence sources: CV, portfolio, website, posts, reports, or project notes

## Placeholder source of truth

Before writing values, inspect the current template:

```bash
python fill_cover_letter.py path/to/template.tex --list
```

Use the detected placeholder list as the source of truth.

Expected current keys:

```json
{
  "PDF-TITLE": "",
  "PDF-SUBJECT": "",
  "LLM-IDENTITY": "",
  "LLM-STACK": "",
  "LLM-STRENGTHS": "",
  "LLM-SKILLS": "",
  "LLM-CONCLUSION": "",
  "TO": "",
  "ROLE": "",
  "LOCATION": "",
  "CONTENT": ""
}
```

## Generation workflow

1. Extract the company, role, location, and application context.
2. Read the career direction and brand files.
3. Select only evidence-backed fit points.
4. Create one values JSON file for the target application.
5. Fill every detected placeholder.
6. Generate the `.tex` file:

```bash
python fill_cover_letter.py path/to/template.tex \
  --values path/to/values.json \
  --output path/to/generated-cover-letter.tex
```

7. Use `--escape` when values are plain text:

```bash
python fill_cover_letter.py path/to/template.tex \
  --values path/to/values.json \
  --output path/to/generated-cover-letter.tex \
  --escape
```

8. Use `--raw-key CONTENT` only when `CONTENT` intentionally contains LaTeX commands.

## Writing rules

* Keep the letter specific to the company and role.
* Lead with inspectable proof.
* Prioritize systems thinking, agentic workflows, technical documentation, tooling, architecture, backend/platform work, and applied AI engineering when relevant.
* Keep the tone professional, direct, technically grounded, and aligned with the project brand.
* Avoid generic junior positioning.
* Avoid CRUD-only positioning.
* Avoid AI-influencer language.
* Avoid empty motivation claims.
* Avoid unsupported company claims.
* Avoid invented experience, metrics, seniority, achievements, or role requirements.

## Field guidance

| Field            | Guidance                                     |
| ---------------- | -------------------------------------------- |
| `PDF-TITLE`      | Short metadata title.                        |
| `PDF-SUBJECT`    | One-line application subject.                |
| `LLM-IDENTITY`   | Compact professional identity.               |
| `LLM-STACK`      | Relevant technologies for this role only.    |
| `LLM-STRENGTHS`  | Strongest evidence-backed differentiators.   |
| `LLM-SKILLS`     | Concrete skills mapped to the role.          |
| `LLM-CONCLUSION` | Final fit thesis.                            |
| `TO`             | Company, team, recruiter, or hiring manager. |
| `ROLE`           | Exact role title or honest normalized title. |
| `LOCATION`       | City, remote, hybrid, or relocation context. |
| `CONTENT`        | Main body of the letter.                     |

## Quality gate

Before returning the result:

* The generator runs successfully.
* No unresolved `::KEY::` placeholder remains.
* Every detected placeholder has a value.
* The template formatting is preserved.
* The letter is tailored to the target role.
* Strong claims are backed by declared evidence.
* The output is ready for user review, not automatic submission.

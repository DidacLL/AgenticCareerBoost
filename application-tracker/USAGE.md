# Local Letter Workflow

This is the current simple workflow for producing a **standalone** tailored cover letter from local data.

For the broader application workflow — one-page tailored CVs, parser summaries, claim discipline, combined documents, and explicit TeX + JSON requests — use [`../agents/cv/APPLICATION_WORKFLOW.md`](../agents/cv/APPLICATION_WORKFLOW.md).

## Important format rule

Within ACB, the CV artifact is TeX. There is no CV JSON format.

If the user asks for `CV en TeX + carta en JSON`, `CV + carta JSON`, or equivalent wording, create two separate local files:

1. the tailored one-page CV as `.tex`;
2. the cover letter as `.json` using the exact schema below.

Do not invent an application wrapper or a second JSON for the CV. An explicit JSON request for the letter overrides the default combined `CV + carta adjunta` convention.

If the user asks only for the JSON letter source, materialize the `.json` file and stop there unless rendering is also requested.

## Render A Letter

From `application-tracker/`:

```powershell
.\letter.ps1 example-slug
```

The script expects:

```text
.private/example-slug.json
```

It writes generated files to:

```text
.private/generated/
```

Use fake data when documenting or checking this flow. Real offer data, recruiter
messages, notes, generated PDFs, and tailored JSON stay local.

## Exact input shape

The machine-readable contract is [`letter-input.schema.json`](letter-input.schema.json).
For ACB-generated cover-letter JSON, use exactly these top-level fields and no wrapper objects or additional metadata:

```json
{
  "slug": "example-slug",
  "output_pdf": "example-cover-letter.pdf",
  "candidate_name": "Example Candidate",
  "headline": "Software Engineer",
  "email": "example@example.invalid",
  "portfolio_url": "https://example.invalid",
  "github_url": "https://example.invalid/github",
  "linkedin_url": "https://example.invalid/linkedin",
  "recipient": "Example Hiring Team",
  "role": "Software Engineer",
  "location": "Remote",
  "greeting": "Dear Example Hiring Team,",
  "paragraphs": ["This is fake example content."],
  "closing": "Sincerely,",
  "public_note": "Generated from fake local data.",
  "parser_summary": "Fake summary for validation.",
  "keywords": ["software", "engineering"]
}
```

The complete key set is therefore:

- `slug`
- `output_pdf`
- `candidate_name`
- `headline`
- `email`
- `portfolio_url`
- `github_url`
- `linkedin_url`
- `recipient`
- `role`
- `location`
- `greeting`
- `paragraphs`
- `closing`
- `public_note`
- `parser_summary`
- `keywords`

Do not add `application`, `candidate`, `cv`, `cover_letter`, `claim_controls`, vacancy-analysis data, or any other top-level fields to the letter JSON generated for this workflow.

## Notes

- `render_letter.py` creates the TeX source from this JSON input.
- `letter.ps1` runs the renderer and then `pdflatex`.
- If LaTeX is not available, keep the generated TeX and compile later.
- Application Tracker code here is prototype material for AAAAT and documents
  the current local standalone-letter workflow.

# Local Letter Workflow

This is the current simple workflow for producing a tailored cover letter from
local data.

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

## Input Shape

The renderer reads explicit JSON fields such as candidate identity, role,
recipient, paragraph text, keywords, and output filename. Keep real inputs in
`.private/`.

For public examples, use a synthetic slug and synthetic company:

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

## Notes

- `render_letter.py` creates the TeX source.
- `letter.ps1` runs the renderer and then `pdflatex`.
- If LaTeX is not available, keep the generated TeX and compile later.
- Application Tracker code here is prototype material for AAAAT, not the target
  architecture.

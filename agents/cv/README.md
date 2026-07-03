# CV and cover-letter artifacts

Canonical sources for public career PDFs live here.

## Files

- `tex/didac-llorens-cv.tex` - public CV source.
- `tex/cover-letter-template.tex` - reusable cover-letter template.
- `tools/render-cover-letter.py` - deterministic stdlib renderer for JSON data.
- `data/examples/*.json` - public-safe example inputs. Only files with
  `publish: true` are rendered by the default build.

## Build

Windows:

```powershell
cd agents/cv
.\build-local.ps1
```

Unix:

```bash
cd agents/cv
./build-local.sh
```

The build renders cover-letter TeX into `build/generated/`, compiles the CV and
public examples, and publishes generated PDFs to:

- `site/files/cv/didac-llorens-cv.pdf`
- `site/files/cover-letters/*.pdf`

Generated PDFs are deploy artifacts, not source files. Do not edit generated
TeX or PDFs by hand; change the canonical `.tex` template or JSON data instead.

## Safety rules

- Do not restore `assets/curriculum/`.
- Do not use hidden white text, zero-width boxes, off-page text, or transparent
  parser stuffing.
- Parser summaries must be visible, low-prominence, selectable, and auditable.
- Keep positioning aligned with `agents/rules/core/career-direction.md`.

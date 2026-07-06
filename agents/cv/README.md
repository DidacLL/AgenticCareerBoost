# CV artifacts and local cover-letter tool

User-owned sources and the build contract for public career PDFs live here.

## Files

- `tex/` - user-authored LaTeX sources. Build and CI rules do not rewrite them.
- `artifacts.json` - public career artifact manifest used by local scripts and CI.
- `tools/render-cover-letter.py` - deterministic stdlib renderer for explicit local cover-letter JSON input.
- `data/**/*.json` - private or local cover-letter data. These files are not public deploy requirements by default.

## Public build

The default public build validates `artifacts.json`, compiles the public CV artifact declared there, and copies the generated PDF to the manifest-declared `site/files/**` destination.

Cover letters are application-specific private working documents. They are not rendered, compiled, or published by default CI merely because a local JSON exists.

## Local cover-letter rendering

Use the renderer explicitly for a selected local/private JSON file when preparing an application-specific letter:

```bash
python tools/render-cover-letter.py --input data/examples/example.json
```

Generated TeX and PDFs are build artifacts, not editable source files. Do not edit generated TeX or PDFs by hand; change the canonical `.tex` template or the selected local JSON data instead.

## Source ownership

- The current LaTeX files are human-authored source and remain under direct developer control.
- Tests and CI validate public integration, generated public artifacts, and deploy paths; they do not enforce prose, layout, or content style inside private cover letters.
- Keep positioning aligned with `agents/rules/core/career-direction.md`.

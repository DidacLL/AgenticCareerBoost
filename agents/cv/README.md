# CV and cover-letter artifacts

User-owned sources and the build contract for public career PDFs live here.

## Files

- `tex/` - user-authored LaTeX sources. Build and CI rules do not rewrite them.
- `artifacts.json` - public artifact manifest used by local scripts and CI.
- `tools/render-cover-letter.py` - deterministic stdlib renderer for JSON data.
- `data/**/*.json` - cover-letter data. Only manifest entries with
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

The build validates `artifacts.json`, renders manifest-declared cover-letter
TeX into `build/generated/`, compiles every published artifact, and copies PDFs
to the manifest-declared `site/files/**` destinations.

Generated TeX and PDFs are deploy artifacts, not editable source files. Do not
edit generated TeX or PDFs by hand; change the canonical `.tex` template or JSON
data instead. CI builds the public PDFs before validating/uploading the site
artifact.

## Source ownership

- The current LaTeX files are human-authored source and remain under direct
  developer control.
- Tests and CI validate integration, generated artifacts, and deploy paths; they
  do not enforce prose, layout, or content style inside the LaTeX sources.
- Keep positioning aligned with `agents/rules/core/career-direction.md`.

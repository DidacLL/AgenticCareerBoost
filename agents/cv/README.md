# CV artifacts

User-owned sources and the build contract for public career PDFs live here.

## Files

- `tex/` - user-authored LaTeX sources for public career PDFs. Build and CI rules do not rewrite them.
- `artifacts.json` - public career artifact manifest used by local scripts and CI.
- `tools/artifact_manifest.py` - public CV artifact manifest helper.

## Public build

The default public build validates `artifacts.json`, compiles the public CV artifact declared there, and copies the generated PDF to the manifest-declared `site/files/**` destination.

Application-specific letters are local working documents. Their tooling lives under `application-tracker/` and is not part of the public CV build.

## Source ownership

- The current CV LaTeX files are human-authored source and remain under direct developer control.
- Tests and CI validate public integration, generated public artifacts, and deploy paths.
- Keep positioning aligned with `agents/rules/core/career-direction.md`.
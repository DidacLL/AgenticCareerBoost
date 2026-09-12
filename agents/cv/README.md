# `agents/cv/` — public CV source and build pipeline

This directory owns the public/general CV and its build tooling. It is deliberately independent from the portfolio source tree: the site consumes a generated PDF artifact, but it does not own the TeX source, shared preamble, header artwork, or compilation rules.

For tailored job applications, read [`APPLICATION_WORKFLOW.md`](APPLICATION_WORKFLOW.md). It is the active local workflow for one-page tailored CVs, combined CV + cover-letter documents, parser summaries, claim discipline and local compilation.

## Canonical source root

The single LaTeX source/compilation root is:

```text
agents/cv/tex/
```

It contains:

```text
didac-llorens-cv.tex
didac-cv-shared-preamble-v1.tex
418-banner.png
```

The main document includes the preamble as a sibling and the preamble loads the banner as a sibling. There are no `site/` dependencies and no dual working-directory search paths.

That means `didac-llorens-cv.tex` can be opened and compiled directly from `agents/cv/tex/` in a LaTeX IDE.

## CV composition contract

The shared preamble owns the stable visual language and reusable macros. In particular:

- `\cvsetup{role}{headline}{keywords}{summary}` owns role-specific metadata;
- `\cvAbstract{...}` is the visible narrative opener for the main column;
- `\cvParserSummary` is the ATS/AI-readable support surface and includes the evidence-backed role summary/keywords;
- `\cvheader`, `\project`, `\mainsection`, `\railsection`, `\cvMainLinks`, `\cvBeforeEngineering` and `\cvEducation` keep variants on the same design system.

A tailored CV should remain one page and reuse this composition rather than becoming a generic multi-page resume. When the requested deliverable is `CV + carta adjunta`, the default local artifact is one TeX/PDF with the one-page CV first and the one-page letter after `\newpage`.

## Build outputs

Repository build helpers use the same TeX root but redirect generated material to:

```text
agents/cv/build/
```

This includes the public PDF and LaTeX auxiliary output. Known residues such as `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, `.toc`, bibliography state and related temporary files are removed from the source directory before/after scripted builds.

The source directory should therefore remain source-only.

## Local build

Windows:

```powershell
cd agents/cv
.\build-local.ps1
```

Bash:

```bash
cd agents/cv
./build-local.sh
```

Both helpers:

1. validate `artifacts.json`;
2. resolve the public CV source;
3. compile from `agents/cv/tex/`;
4. write generated output under `agents/cv/build/`;
5. publish the selected public PDF to the portfolio artifact path declared by the manifest;
6. keep the TeX source directory clean.

Direct IDE compilation remains valid independently of these helper scripts.

For a local tailored variant that is intentionally not in `artifacts.json`, compile it directly from `agents/cv/tex/` with the command documented in `APPLICATION_WORKFLOW.md`; do not add it to the publication manifest merely to build it.

## Artifact manifest

[`artifacts.json`](artifacts.json) is the small contract between the CV subsystem and publication.

It records:

- the public CV source;
- the expected generated PDF under `agents/cv/build/`;
- the public site artifact destination under `site/assets/files/cv/`;
- whether the artifact is intentionally published.

[`tools/artifact_manifest.py`](tools/artifact_manifest.py) validates that contract and performs the publication copy. It does not generate CV content.

## CI contract

`required-ci` compiles the real public CV from `agents/cv/tex/`, using the same source geometry as the IDE/local scripts. Generated PDF/auxiliary output is redirected to `agents/cv/build/`.

The workflow then explicitly checks that `agents/cv/tex/` was not polluted by build artifacts before publishing the generated public PDF into the site build.

This test exists because a manifest/path check alone is not enough to prove the TeX document still compiles.

## Public/private boundary

Allowed here:

- the public/general CV source;
- shared public LaTeX support;
- the CV-owned header artwork;
- build helpers and artifact-manifest tooling;
- intentionally public-safe material;
- public workflow documentation that contains no live application data.

Keep out of commits:

- tailored CV variants for individual applications;
- generated private PDFs;
- raw job offers or recruiter material;
- private notes/data;
- application-specific JSON;
- unrelated CV-generator product development.

Tailored/local variants may reuse the shared preamble, but they remain ignored unless explicitly promoted to public source.

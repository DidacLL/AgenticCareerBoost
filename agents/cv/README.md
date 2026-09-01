# CV LaTeX Area

This folder keeps the public/general CV LaTeX workflow and related build
material. It is independent from the portfolio source tree.

The canonical TeX root is `agents/cv/tex/`. The public document,
`didac-llorens-cv.tex`, includes `didac-cv-shared-preamble-v1.tex` as a sibling,
and the shared header artwork is the sibling asset `418-banner.png`. There are
no `site/` dependencies and no working-directory-dependent path prefixes inside
the TeX sources.

This means the public CV can be opened and compiled directly from
`agents/cv/tex/` in a LaTeX IDE. The repository build helpers use the same TeX
root; they only redirect generated PDFs and auxiliary files to
`agents/cv/build/` so `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`,
`.synctex.gz`, and similar files do not accumulate beside the sources. The
helpers also remove known auxiliary residues from `tex/` before and after a
build.

Tailored/local variants may also use the shared preamble, but they stay ignored
unless they are intentionally promoted to public proof.

## Boundaries

Allowed here:

- public/general CV source;
- shared LaTeX support when it is intentionally public or supports local CV
  maintenance;
- build helpers for intentional public CV artifacts;
- fake or public-safe examples.

Keep out of commits:

- tailored CV variants for specific applications;
- generated private PDFs;
- private application notes;
- raw offer material;
- private JSON/data.

CV generator product work lives outside this repository. This folder documents
the public CV source and the local LaTeX support used by current CV work.

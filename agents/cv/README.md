# CV LaTeX Area

This folder keeps the public/general CV LaTeX workflow and related build
material. It is part of the public career proof in this repository.

The canonical public source is the monolithic general CV:
`tex/didac-llorens-cv.tex`.

`tex/didac-cv-shared-preamble-v1.tex` is preserved as useful support for
local/tailored CV work and future cleanup. It is not the public CV architecture
yet; a dedicated CV cleanup should decide if and when to split the canonical
source.

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

VCVGenerator is future work together with AAAAT. Do not implement it in this
cleanup branch.

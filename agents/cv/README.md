# CV LaTeX Area

This folder keeps the public/general CV LaTeX workflow and related build
material. It is part of the public career proof in this repository.

The canonical public source is `tex/didac-llorens-cv.tex`. It uses the shared
support file `tex/didac-cv-shared-preamble-v1.tex`, so the public CV and the
current LaTeX workflow are represented by the same tracked code. The shared
header artwork is CV-owned source material at `tex/418-banner.png`; it does not
belong to the portfolio asset tree.

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

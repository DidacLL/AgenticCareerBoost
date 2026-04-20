# content/reports/

Formal engineering documentation in LaTeX.

- Catalan is permitted per `docs/core/brand.md` language policy.
- Build with TeX Live: `pdflatex` or `lualatex`.
- Local build output lands in `content/reports/tex/build/`.
- CI promotes published PDFs into `content/reports/build/` on pushes that
  update `content/reports/tex/`.
- Source template: [`docs/templates/documentation-output.md`](../../docs/templates/documentation-output.md)

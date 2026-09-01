---
title: P3CTeX
description: A LaTeX2e/expl3 document toolkit built to turn UOC PEC work into fast, reproducible, professional technical documents.
subtitle: The project I built so formatting a PEC would stop competing with the actual engineering work.
label: 01A / PROJECT
summary: An extensible document class and package suite for UOC work: official-style structure, source listings, resilient screenshots, data-driven tables, UML class models, reusable metadata, and deterministic builds.
order: 1
tags: [LaTeX2e, expl3, TeX programming, UML, Document tooling]
image: img/P3CTeXLogo.png
imageAlt: P3CTeX logo
repository: https://github.com/DidacLL/P3CTeX
status: Active / flagship project
---
P3CTeX started from a very practical problem: I did not want to spend the last hour before a UOC deadline fixing margins, covers, screenshot sizes, table formatting, code blocks, or the same document metadata again. I wanted to write the work, compile it, and get a document I was happy to submit.

It began as a UOC-oriented LaTeX template and grew into the project here I am most proud of: a document class, a core package, independent feature libraries, internal `expl3` code, manuals, examples, regression tests, and a TeX Directory Structure that can be registered as a proper local package tree.

The practical result is simple: PECs and technical reports can be produced very quickly while keeping consistent typography, reusable structure, references, figures, source code, diagrams and polished output. The interesting engineering is everything underneath that convenience.

## A small TeX software ecosystem

`P3CTeX.cls` owns the document-level behaviour and UOC metadata. `pxCORE` acts as the aggregation layer, while focused libraries provide features independently:

- **pxGDX** — the design system: colours, typography and shared visual conventions.
- **pxSRC** — robust figure/screenshot inclusion, image pairs and numbered image sequences. Missing assets can render as placeholders instead of breaking an in-progress document.
- **pxTAB** — tables generated from list-style data with reusable presets for headers, grids, stripes, widths, captions and layout.
- **pxPRP** — named property maps and registries used as structured state from ordinary LaTeX commands.
- **pxUML** — UML class/object modelling on top of TikZ/pgf-umlcd, with a registry that separates the model from where and how it is drawn.

The public APIs remain usable from normal LaTeX2e documents; the internals can use `expl3`, token lists, key families and data structures where that makes the implementation cleaner.

## UML that behaves like a model

`pxUML` is one of my favourite parts of the project. A class is registered with attributes, operations, inheritance, object type (`class`, `interface`, `enumclass`, etc.) and optional implementation information. The same stored definition can then be drawn in different positions or styles without rewriting the model.

That makes object-oriented coursework much less mechanical. Classes, interfaces, inheritance and relations such as associations, composition and aggregation can be described once and rendered as a proper UML diagram. It is much closer to working with an object model than manually drawing boxes in a diagram editor.

## Built for the way PECs are actually written

A large part of coursework is iterative: screenshots arrive late, diagrams change, tables grow, and a report must remain compilable while pieces are still missing. P3CTeX has features specifically for that workflow instead of treating the document as a final static page.

That is why `pxSRC` can preserve a figure slot when an image is not ready, why image lists can consume sequential captures, why metadata and cover configuration live in reusable keys, and why tables and UML structures are expressed as data rather than repeated visual markup.

TeX programming is also very different from mainstream application code. Macro expansion, token streams and the LaTeX2e/expl3 boundary force a different way of thinking about APIs and state. Building something maintainable in that environment is a large part of why I still enjoy working on P3CTeX.

## See it working

- [Open the compiled P3CTeX showcase PDF](https://github.com/DidacLL/P3CTeX/blob/main/examples/P3CTeX-example.pdf)
- [Read the source of the showcase](https://github.com/DidacLL/P3CTeX/blob/main/examples/P3CTeX-example.tex)
- [Open the minimal UOC template output](https://github.com/DidacLL/P3CTeX/blob/main/examples/UOCTemplates/MinimalTemplate/PAC1/MinimalTemplatePAC.pdf)
- [Open the extended UOC template output](https://github.com/DidacLL/P3CTeX/blob/main/examples/UOCTemplates/ExtendedTemplate/PAC1/ExtendedTemplatePAC.pdf)
- [Read the pxUML API/manual source](https://github.com/DidacLL/P3CTeX/blob/main/tex/doc/pxUML.tex)

The repository contains the package sources, manuals, examples and test suites. The compiled examples are the quickest way to understand why the project exists; the `.sty`, `.cls` and `.code.tex` files show the depth behind the output.

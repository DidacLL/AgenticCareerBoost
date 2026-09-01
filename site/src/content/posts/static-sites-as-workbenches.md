---
title: Static sites as workbenches
description: Why static publishing works well for a personal technical site when content, presentation, and generated output have clear owners.
date: 2026-06-27
tags: [Static site, Content model, Maintenance]
image: img/routing-map.png
imageAlt: Content and route map for the portfolio
---
A static site does not have to mean hand-maintained HTML, and a maintainable site does not automatically need a server-side application.

For a personal technical portfolio, most pages are documents. Projects, notes, profile text and contact information change when I edit them; they do not need a database request every time somebody opens the page. Compiling those sources to HTML is a very good fit.

The useful boundary is between authored content and presentation. A blog post should be a source document. A layout should know how blog posts look. Navigation should live in one shared owner. The generated `dist/` tree should be disposable. If adding an article requires copying a page template or registering the same slug in three places, the source model is already leaking implementation details into authoring.

This is why I eventually moved this portfolio to Astro. Astro is not valuable here because I wanted a framework; it is useful because it can act as a compiler. Markdown remains the thing I write, components own repeated structure, and the output is still ordinary static HTML.

There is still room for client-side behaviour. Theme persistence, the CRT/gallery and smooth internal navigation make the site nicer to use. The important part is that none of them owns the content and none of them is required to read the page. With JavaScript disabled, the document should still be a document.

Static publishing also makes deployment portability testable. The same source can be built for `/` or for a project subpath, and broken assumptions about canonical URLs, assets or redirects show up during the build rather than becoming runtime state.

The result I want is deliberately boring to operate: write a Markdown file, commit it, build it, publish static files. The interesting engineering belongs in the source model and the checks, not in making publication feel complicated.

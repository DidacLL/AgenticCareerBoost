---
title: AgenticCareerBoost
description: Engineering workspace behind this portfolio, combining static publishing, document builds, CI, local automation, and preserved project history.
subtitle: The repository where I build and maintain this site and the supporting automation around it.
label: 01C / PROJECT
summary: Markdown-authored Astro publishing, GitHub Actions, generated document artifacts, local utilities, validation, and the development record behind the portfolio.
order: 3
tags: [Astro, Markdown, GitHub Actions, Automation]
image: img/routing-map.png
imageAlt: AgenticCareerBoost site and repository routing map
repository: https://github.com/DidacLL/AgenticCareerBoost
status: Active / portfolio source
---
AgenticCareerBoost is the repository behind this site and the collection of small tools, document workflows and experiments that grew around maintaining my public technical work.

The current version is intentionally simple at the public boundary. Portfolio content is Markdown. Astro turns it into static HTML. A small amount of client JavaScript keeps navigation smooth and runs the theme and CRT/gallery interactions. GitHub Actions builds the site at both root and project-base paths, checks metadata and assets, compiles document artifacts, and exercises the result in Chromium.

## The repository is larger than the website

I use ACB as a working engineering repository, so not every useful file belongs in the public site. The `site/` tree contains only what the portfolio actually serves. Technical reports, historical decisions and earlier workflow material remain under `agents/`; local application data stays outside Git entirely.

That separation took several iterations to get right. Earlier versions tried to make too much repository state part of the public runtime. The current design keeps source ownership explicit: content owns prose, shared data owns global identity and navigation, components own presentation, and generated output is treated as disposable build material.

## Agent-assisted work with inspectable state

The project has also been a place to experiment with agent-assisted engineering. The part I kept is not a permanent orchestration framework; it is the discipline of leaving useful state behind: small changes, source files, validation results, decisions and enough history to understand why something changed.

Older rules, reports and workflow documents remain in the repository because they are useful evidence of that evolution, but they are not an active harness that new work must obey.

## Where the experiments went

The first application-tracking experiments lived here because ACB was the convenient place to test them. Once that idea became substantial software, it moved into [AAAAT](https://github.com/DidacLL/AAAAT). Keeping that boundary is more useful than letting this repository grow into a monolith simply because the experiments started here.

ACB is therefore best understood as the source and engineering history of the portfolio itself: static publishing, automation, validation, technical documents, and the corrections that made those pieces maintainable.

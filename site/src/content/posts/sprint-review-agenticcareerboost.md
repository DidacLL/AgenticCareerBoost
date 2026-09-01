---
title: Refactoring a portfolio without turning it into an app
description: Lessons from replacing a browser-rendered content runtime with static Astro while keeping the site's visual identity and small interactive pieces.
date: 2026-06-28
tags: [Astro, Refactoring, Static publishing]
image: img/routing-architecture.png
imageAlt: Routing architecture from the portfolio refactor
---
The first version of this portfolio had a custom browser runtime: JSON content, a route registry, a renderer, reusable components and enough JavaScript to make the site behave like a small application.

It worked. It was also the wrong maintenance model for a site whose main job is to publish documents.

The refactor was less about choosing Astro than about deciding what each kind of source should own. Project prose and blog posts moved to Markdown. Shared identity and navigation got one data owner. Layouts and components kept presentation. Deployment origin and base path became build inputs. Generated HTML stopped being something worth thinking about while authoring.

The difficult part was preserving the parts of the old site that actually gave it character. The CRT monitor, paper/grid treatment, banner, identity rail and compact navigation were worth keeping. The custom content runtime was not. Treating those two things as separate decisions made the migration much easier to reason about.

I also did not want smooth navigation to require turning the site back into an SPA. Astro's client router is enough to avoid the visible image/header reloads that made page changes feel cheap, while every route still has a complete static HTML document and remains readable without JavaScript.

The other lesson was that static sites still need serious verification once they have more than a handful of pages. This build checks both root and subpath deployments, generated routes, metadata, images, retired URLs and browser behaviour. Chromium runs the navigation, theme and CRT interactions and checks responsive overflow at several viewport sizes.

The final authoring test is much simpler than any of those checks: publishing a new article should mean creating one Markdown file. If the architecture is sophisticated but that operation becomes annoying, the architecture has failed its user — in this case, me.

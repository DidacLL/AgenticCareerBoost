---
title: Static sites as workbenches
description: Static publishing, route structures, and plain files for personal technical work.
date: 2026-06-27
tags: [Static site, Content model, Maintenance]
image: img/routing-map.png
imageAlt: Routing map from the earlier static site architecture
---
A static site does not need to become a pile of copied pages.

Plain HTML, CSS, JavaScript, and JSON can be enough when the site has one shell, one route registry, and reusable components.

The maintainable boundary is simple: content files describe the work; components describe reusable structures; the shell owns navigation, theme, and routing.

That keeps deployment boring and updates human-sized. Adding a project or article should be a data change, not a new folder full of duplicated markup.

*Context: this is a historical note from before the Astro migration.*

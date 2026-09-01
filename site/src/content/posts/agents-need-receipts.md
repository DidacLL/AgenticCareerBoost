---
title: Agents need receipts
description: Why agent-assisted engineering needs durable artifacts, exact state, and reviewable changes instead of relying on chat history.
date: 2026-06-27
tags: [Agents, Review, Workflow]
image: img/sprint-paircheck-loop.png
imageAlt: Pair-check workflow diagram
---
Agent-assisted work becomes useful when the result survives the conversation that produced it.

A transcript is a poor engineering artifact. It is long, difficult to diff, easy to lose, and full of intermediate claims that may never have become true. The useful output is smaller: the committed source, the exact test result, the decision that changed an interface, the source used for a factual claim, or the issue that still remains open.

I think of those things as receipts. They let another person — or me six months later — answer basic questions without reconstructing a chat session: What changed? Why? Against which state? What was actually verified? What is still uncertain?

This matters more with LLM-assisted work because fluent summaries can hide an astonishing amount of ambiguity. A model can say that a build passed, that a file was updated, or that two implementations are equivalent. The repository should make those statements independently checkable.

The practical rules I keep coming back to are simple:

- make changes small enough to review;
- record decisions in the system that owns them, not only in conversation;
- attach verification to the exact revision it verified;
- keep generated output reproducible instead of treating it as source;
- preserve uncertainty when something has not actually been checked.

That does not require a large agent framework. In many cases a branch, a diff, a test run and a short note are better institutional memory than another layer of orchestration.

The point of using an agent is to get useful work done faster. The point of the receipts is to make sure the speed does not come at the cost of knowing what the system actually contains.

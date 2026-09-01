---
title: AAAAT
description: Local-first desktop software for managing job applications, source material, conversations, documents, and optional bounded AI assistance.
subtitle: A native Python workspace that keeps the application record local and remains fully useful with no AI connected.
label: 01B / PROJECT
summary: "A wxPython/SQLite desktop application centred on the candidature: offer source, status, notes, next actions, reusable context, generated documents, local artifacts, and provider-neutral optional assistance."
order: 2
tags: [Python, wxPython, SQLite, Local-first, PyInstaller]
image: img/AAAATlogo.png
imageAlt: AAAAT logo
repository: https://github.com/DidacLL/AAAAT
status: 1.0 / active
---
AAAAT is a desktop application I built because a real job search quickly becomes a mess of spreadsheets, notes, browser tabs, chat histories, PDFs and half-finished drafts. The useful information belongs together, but I did not want the solution to become another cloud account or an AI wrapper.

The candidature is the central record. It connects the original opportunity, current stage, next action, notes, research, conversation preparation, reusable professional context, generated text and the files that were actually used for that application.

## Local first means local ownership

The authoritative workspace is a user-selected local directory backed by SQLite and local artifacts. Normal tracking, editing, search, preparation, rendering, backup and restore work without an LLM, a network connection, Git or a source checkout.

The desktop UI is built with wxPython and packaged with PyInstaller as native Windows, macOS and Linux applications. The application is intended to be opened and used as software, not run as a developer demo from a terminal.

## AI is optional and deliberately bounded

AAAAT can work with an external AI host, but the application keeps authority over its own data. A connected host gets purpose-scoped context and a deliberately small operation set instead of general database access, internal IDs, workspace paths or arbitrary record browsing.

The integration is provider-neutral: AAAAT does not require API keys, model names or a provider SDK. The same application remains complete when nothing is connected. That separation between useful software and optional model assistance is one of the architectural decisions I care most about in the project.

## Operational views instead of a generic dashboard

Smart View is designed for the information needed during a recruiter call or an urgent preparation pass. Detailed View exposes the complete candidature record. User View contains reusable professional context. The application also keeps generated files and provenance next to the record that produced them.

- [See the desktop workspace with fictional data](https://github.com/DidacLL/AAAAT/blob/main/docs/assets/aaaat-desktop.svg)
- [Read the implemented architecture](https://github.com/DidacLL/AAAAT/blob/main/docs/architecture.md)
- [Read the optional AI integration contract](https://github.com/DidacLL/AAAAT/blob/main/docs/ai-integration.md)

AAAAT grew out of an earlier tracker experiment inside AgenticCareerBoost, but it became its own project once the product boundaries were clear enough to deserve an independent repository and release process.

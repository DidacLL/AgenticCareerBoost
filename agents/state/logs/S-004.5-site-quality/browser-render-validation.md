# S-004.5 browser/render validation

Status: passed locally with Microsoft Edge headless against `http://127.0.0.1:8765/`

## Routes checked

| Route | Desktop 1366px | Mobile 390px | Notes |
|---|---:|---:|---|
| Home | pass | pass | No horizontal overflow; runtime canonical and social image resolved from served origin |
| Projects | pass | pass | No overflow; metadata runtime-filled |
| AgenticCareerBoost project | pass | pass | Dashboard state `ready`; desktop dashboard tiles distribute horizontally; mobile stacks cleanly |
| Dashboard / legacy status route | pass | pass | Dashboard state `ready`; status tiles and lists render from generated JSON |
| Blog | pass | pass | No overflow; legal disclosure present |
| CV | pass | pass | No overflow; CV filtering validated separately |
| Contact | pass | pass | Desktop contact cards render as three horizontal columns; mobile stacks with full readable width |

## Acceptance checks

- No horizontal overflow on the seven target routes at 1366px and 390px.
- Runtime canonical, Open Graph URL, and social images are derived from the served local origin, not a committed deployment URL.
- Each route has one `.legal-disclosure` footer, and it is outside `main`.
- AgenticCareerBoost and Dashboard routes load generated status data and reach `data-dashboard-state="ready"`.
- Closed-state dashboard smoke shows `No active sprint` / `idle`, no overflow, and legal disclosure outside `main`.
- Contact desktop card positions at 1366px: three equal-width cards across the content area.
- Theme toggle survives soft navigation from Home to Projects: route changed to `/projects/index.html`, theme remained `dark`, and only one OS rail/document/meta set remained.
- CV filter buttons use pushState and in-place filtering: switching ML to Agentic preserved an in-page marker, set `?view=agentic`, marked the Agentic button active, and updated visible sections. Browser back restored `?view=ml` and active ML state.
- Post-review layout correction: Contact, Projects, and CV preview rows were rechecked at 540px and 390px after replacing mobile vertical preview cards with compact horizontal flex rows. At 390px, Contact rows measured 72-79px tall, Projects rows 79-98px, CV artifact rows 79px, and all checked pages had zero horizontal overflow.
- CV selected-work cards were rechecked after changing the CV grid to auto-fit with a readable minimum width; the visible ML card measured 671px at 1180px viewport, 475px at 540px, and 325px at 390px.

## Tool note

The bundled Playwright Chromium binary was unavailable in this environment, so the render gate launched the installed Microsoft Edge executable through Playwright.

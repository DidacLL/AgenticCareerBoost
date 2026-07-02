# Browser And Print Validation

Date: 2026-06-11

## Scope

Close the remaining rendered browser and print-preview site gates without
adding project dependencies.

## Decision: Validation Method

| Option | Score | Reason |
|---|---:|---|
| Install Playwright | 5 | Strong automation, but adds tooling friction for a static site gate. |
| Use installed browser headless mode | 9 | No project dependency; can produce screenshots and PDF print output. |
| Keep source-only validation | 4 | Already done, but too weak for layout/print acceptance. |

Selected: installed browser headless mode if available.

## Evidence

- Browser: Microsoft Edge headless via Chrome DevTools Protocol.
- Local URL root: `http://127.0.0.1:4173/AgenticCareerBoost/`.
- Desktop landing screenshot: PASS.
- Mobile landing screenshot: PASS after CSS fixes; CDP metrics reported
  `scrollWidth=390` and `clientWidth=390`.
- Dashboard desktop screenshot: PASS.
- CV `?view=ml` screenshot: PASS after `[hidden]` CSS fix; only ML/Data
  target tags and evidence remain visible.
- CV `?view=print` PDF: PASS, generated nonempty PDF artifact.

## Fixes Applied

- Added `[hidden] { display: none !important; }` so URL-param CV filtering
  is not overridden by display rules.
- Stacked mobile action buttons below 520px.
- Replaced `width: min(...)` with `width` plus `max-width` for compatibility.
- Added grid-item `min-width: 0` and visual max-width guards.
- Refreshed dashboard copy to match current sprint status.

## Verdict

PASS. Rendered desktop, mobile, dashboard, configurable CV, and print-PDF gates
are proven without adding site dependencies.

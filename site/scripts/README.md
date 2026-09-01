# Site build checks

`content-routes.mjs` derives dynamic portfolio routes directly from the Markdown filenames in `src/content/posts/`, `src/content/projects/`, and `src/content/cv/`. Adding content must not require a second route registry in test code.

`verify-build.mjs` checks the generated static artifact for routing, metadata, deployment-base portability and indexability. `browser-smoke.mjs` performs representative browser interaction and responsive checks against the generated artifact.

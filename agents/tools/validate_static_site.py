"""Validate the canonical site/ Pages artifact."""

from __future__ import annotations

import json
import os
from pathlib import Path


def repo_root() -> Path:
    override = os.environ.get("ACB_REPO_ROOT")
    if override:
        return Path(override).resolve()
    return Path(__file__).resolve().parents[2]


ROOT = repo_root()
SITE = Path(os.environ.get("ACB_SITE_ROOT", ROOT / "site")).resolve()

REQUIRED = [
    "index.html",
    "404.html",
    ".nojekyll",
    "manifest.json",
    "assets/css/site.css",
    "assets/js/os.js",
    "assets/js/data-store.js",
    "assets/js/router.js",
    "assets/js/renderer.js",
    "assets/js/components.js",
    "assets/js/widgets.js",
    "content/site.json",
    "content/pages.json",
    "content/projects.json",
    "content/blog.json",
    "content/cv.json",
    "content/fragments/legal-disclosure.html",
    "data/status.json",
]

RUNTIME_FILES = [
    "index.html",
    "404.html",
    "assets/js/os.js",
    "assets/js/router.js",
    "assets/js/renderer.js",
    "assets/js/components.js",
    "assets/js/widgets.js",
    "assets/js/data-store.js",
]

FORBIDDEN_DEPLOYMENT_TOKENS = [
    "/AgenticCareerBoost",
    "didacll.github.io",
]


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED:
        if not (SITE / relative).is_file():
            failures.append(f"missing site artifact file: site/{relative}")

    index = SITE / "index.html"
    if index.is_file():
        text = index.read_text(encoding="utf-8")
        for token in ("assets/css/site.css", "assets/js/os.js", "manifest.json"):
            if token not in text:
                failures.append(f"site/index.html missing {token}")

    for relative in RUNTIME_FILES:
        path = SITE / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN_DEPLOYMENT_TOKENS:
            if token in text:
                failures.append(f"site/{relative} hardcodes deployment path/token: {token}")

    router = SITE / "assets" / "js" / "router.js"
    components = SITE / "assets" / "js" / "components.js"
    widgets = SITE / "assets" / "js" / "widgets.js"
    data_store = SITE / "assets" / "js" / "data-store.js"
    if router.is_file():
        router_text = router.read_text(encoding="utf-8")
        if "new URL(import.meta.url)" not in router_text:
            failures.append("site/assets/js/router.js must derive deployment base from import.meta.url")
        if 'pushState({}, "", routeHref(route))' not in router_text:
            failures.append("site/assets/js/router.js must push base-aware routeHref(route)")
    if components.is_file():
        components_text = components.read_text(encoding="utf-8")
        if "window.location.hash" in components_text:
            failures.append("site/assets/js/components.js must not bypass router with window.location.hash")
    fallback = SITE / "404.html"
    if fallback.is_file():
        fallback_text = fallback.read_text(encoding="utf-8")
        for token in (
            "candidateBases(normalizedPath)",
            "hasSiteContent(candidate)",
            "content/site.json",
            "routeForBase(normalizedPath, base)",
            "${window.location.origin}${base}#${route}",
        ):
            if token not in fallback_text:
                failures.append(f"site/404.html missing deployment-base discovery marker: {token}")
    if widgets.is_file():
        widgets_text = widgets.read_text(encoding="utf-8")
        if "routeHref(slide.route)" not in widgets_text:
            failures.append("site/assets/js/widgets.js must use routeHref for gallery route links")
        if "hashHref" in widgets_text:
            failures.append("site/assets/js/widgets.js must not generate hash route hrefs")
    if data_store.is_file() and "hashHref" in data_store.read_text(encoding="utf-8"):
        failures.append("site/assets/js/data-store.js must not expose a second internal route href helper")

    for relative in ("site.json", "pages.json", "projects.json", "blog.json", "cv.json"):
        path = SITE / "content" / relative
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"site/content/{relative} invalid JSON: {exc}")

    if failures:
        print("Static site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Static site validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

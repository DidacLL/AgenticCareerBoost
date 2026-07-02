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

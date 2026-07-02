"""Validate the root-upload static site and its public runtime files."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlsplit


def repo_root() -> Path:
    override = os.environ.get("ACB_REPO_ROOT")
    if override:
        return Path(override).resolve()
    return Path(__file__).resolve().parents[2]


ROOT = repo_root()
SITE = Path(os.environ.get("ACB_SITE_ROOT", ROOT / "site")).resolve()

REQUIRED_ROOT = [
    "index.html",
    "404.html",
    ".nojekyll",
    "robots.txt",
    "sitemap.xml",
]

REQUIRED_SITE = [
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

PUBLIC_REF_KEYS = {"href", "image", "bannerImage", "legalFragment", "src", "status"}
ALLOWED_SCHEMES = {"https", "mailto", "tel"}


def read_json(path: Path, failures: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        failures.append(f"{path.relative_to(ROOT).as_posix()} invalid JSON: {exc}")
        return {}


def walk(node: object, path: str = "$"):
    yield path, node
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk(value, f"{path}[{index}]")


def normalize_route(value: str) -> str:
    route = str(value or "/").split("#", 1)[0].split("?", 1)[0]
    route = route if route.startswith("/") else f"/{route}"
    return route.removesuffix("/index.html").rstrip("/") or "/"


def validate_site_ref(ref: str, failures: list[str], context: str) -> None:
    if not ref or ref.startswith("#"):
        return
    parsed = urlsplit(ref)
    if parsed.scheme:
        if parsed.scheme not in ALLOWED_SCHEMES:
            failures.append(f"{context} uses unsupported scheme: {ref}")
        return
    if parsed.netloc:
        failures.append(f"{context} uses protocol-relative URL: {ref}")
        return
    if parsed.path.startswith("/"):
        failures.append(f"{context} must use site-relative public paths, not root paths: {ref}")
        return
    target = (SITE / parsed.path).resolve()
    try:
        target.relative_to(SITE)
    except ValueError:
        failures.append(f"{context} escapes site root: {ref}")
        return
    if parsed.path and not target.is_file():
        failures.append(f"{context} missing public file: {ref}")


def main() -> int:
    failures: list[str] = []

    for item in REQUIRED_ROOT:
        if not (ROOT / item).is_file():
            failures.append(f"missing root entrypoint: {item}")
    for item in REQUIRED_SITE:
        if not (SITE / item).is_file():
            failures.append(f"missing site runtime file: site/{item}")

    index = (ROOT / "index.html")
    if index.is_file():
        text = index.read_text(encoding="utf-8")
        for token in ("site/assets/css/site.css", "site/assets/js/os.js", "site/manifest.json"):
            if token not in text:
                failures.append(f"index.html missing {token}")

    site_data = read_json(SITE / "content/site.json", failures)
    route_set = {
        normalize_route(item.get("path", ""))
        for item in site_data.get("routes", [])
        if isinstance(item, dict)
    } if isinstance(site_data, dict) else set()
    if "/" not in route_set:
        failures.append("site/content/site.json must define the home route")

    for relative in ("site.json", "pages.json", "projects.json", "blog.json", "cv.json"):
        path = SITE / "content" / relative
        data = read_json(path, failures)
        for pointer, value in walk(data):
            if not isinstance(value, str):
                continue
            key = pointer.rsplit(".", 1)[-1].split("[", 1)[0]
            if key == "route" and normalize_route(value) not in route_set:
                failures.append(f"site/content/{relative}:{pointer} unknown route: {value}")
            if key in PUBLIC_REF_KEYS:
                if key == "href" and normalize_route(value) in route_set and not urlsplit(value).scheme:
                    continue
                validate_site_ref(value, failures, f"site/content/{relative}:{pointer}")

    if failures:
        print("Static site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Static site validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

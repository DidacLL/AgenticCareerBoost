"""Validate the plain static single-shell GitHub Pages source."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"

REQUIRED_FILES = [
    "index.html",
    "404.html",
    ".nojekyll",
    "manifest.json",
    "robots.txt",
    "sitemap.xml",
    "assets/css/site.css",
    "assets/data/public-status.json",
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
]

SHELL_SLOTS = [
    "data-os-rail",
    "data-system-banner",
    "data-doc-tabs",
    "data-page-content",
    "data-os-meta",
    "data-legal-disclosure",
]

REQUIRED_CSS_TOKENS = {
    "--border-hairline",
    "--font-size-body",
    "--font-size-h1",
    "--font-size-h2",
    "--grid-size-site",
    "--grid-size-os",
    "--monitor-bg",
    "--monitor-phosphor",
    "--space-card",
    "--button-height",
}

ALLOWED_EXTERNAL_HOSTS = {
    "github.com",
    "www.linkedin.com",
}

DEPLOYMENT_BOUND_HOST = "didacll.github.io"
HTML_BLOB = re.compile(r"<(article|aside|div|footer|header|main|nav|section|ul|ol|li|p|h[1-6]|strong|small)\b", re.I)
PUBLIC_TEXT_TAGS = re.compile(r"<(h1|h2|h3|p|strong|small|article|li)\b", re.I)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_json(path: Path, failures: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation reports parse errors cleanly.
        failures.append(f"{rel(path)} is invalid JSON: {exc}")
        return {}


def normalize_route(route: str) -> str:
    clean = str(route or "/").split("#", 1)[0].split("?", 1)[0]
    clean = clean if clean.startswith("/") else f"/{clean}"
    clean = clean.removesuffix("/index.html").rstrip("/")
    return clean or "/"


def is_external(ref: str) -> bool:
    parsed = urlsplit(ref)
    return bool(parsed.scheme or parsed.netloc)


def validate_external(ref: str, failures: list[str], context: str) -> None:
    parsed = urlsplit(ref)
    if parsed.scheme != "https":
        failures.append(f"{context} uses non-https external URL: {ref}")
        return
    if parsed.netloc not in ALLOWED_EXTERNAL_HOSTS:
        failures.append(f"{context} uses unapproved external host: {ref}")


def validate_local_file(ref: str, source: Path, failures: list[str], context: str) -> None:
    if not ref or ref.startswith("#") or ref.startswith("mailto:") or ref.startswith("tel:"):
        return
    if DEPLOYMENT_BOUND_HOST in ref:
        failures.append(f"{context} contains deployment-bound URL: {ref}")
        return
    if is_external(ref):
        validate_external(ref, failures, context)
        return

    parsed = urlsplit(ref)
    if not parsed.path:
        return
    path = unquote(parsed.path)
    if path.startswith("/"):
        target = (SITE / path.lstrip("/")).resolve()
    else:
        target = (source.parent / path).resolve()
    try:
        target.relative_to(SITE.resolve())
    except ValueError:
        failures.append(f"{context} escapes site root: {ref}")
        return
    if not target.is_file():
        failures.append(f"{context} references missing file: {ref}")


def walk_json(node: object, path: str = "$"):
    yield path, node
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk_json(value, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_json(value, f"{path}[{index}]")


def validate_json_content_hygiene(name: str, data: object, failures: list[str]) -> None:
    for path, value in walk_json(data):
        if isinstance(value, str) and HTML_BLOB.search(value):
            failures.append(f"{name}:{path} contains HTML markup; move complex markup to content/fragments")
        if isinstance(path, str) and path.endswith((".contentHtml", ".metaHtml")):
            failures.append(f"{name}:{path} uses escaped route HTML instead of structured content")


def validate_refs(name: str, data: object, source: Path, route_paths: set[str], failures: list[str]) -> None:
    file_ref_keys = {"href", "image", "bannerImage", "legalFragment", "src"}
    route_ref_keys = {"route", "path"}
    for path, value in walk_json(data):
        if not isinstance(value, str):
            continue
        key = path.rsplit(".", 1)[-1]
        if "[" in key:
            key = key.split("[", 1)[0]
        if key in file_ref_keys:
            if key == "href" and normalize_route(value) in route_paths and not is_external(value):
                failures.append(f"{name}:{path} uses href for an internal route; use route")
            else:
                validate_local_file(value, source, failures, f"{name}:{path}")
        elif key == "status" and ("/" in value or value.endswith(".json")):
            validate_local_file(value, source, failures, f"{name}:{path}")
        elif key in route_ref_keys:
            if key == "route" and normalize_route(value) not in route_paths:
                failures.append(f"{name}:{path} references unknown route: {value}")
        elif DEPLOYMENT_BOUND_HOST in value:
            failures.append(f"{name}:{path} contains deployment-bound URL: {value}")


def validate_single_shell(failures: list[str]) -> None:
    for file in SITE.rglob("*.html"):
        relative = file.relative_to(SITE).as_posix()
        if relative in {"index.html", "404.html"} or relative.startswith("content/fragments/"):
            continue
        failures.append(f"{rel(file)} is a route HTML artifact; single-shell site may only deploy site/index.html and site/404.html")

    for unsafe in (SITE / ".idea", SITE / ".vscode"):
        if unsafe.exists() and any(path.is_file() for path in unsafe.rglob("*")):
            failures.append(f"{rel(unsafe)} must not be part of the deployed artifact")

    index = (SITE / "index.html").read_text(encoding="utf-8")
    for slot in SHELL_SLOTS:
        if slot not in index:
            failures.append(f"site/index.html missing shell slot {slot}")
    body = index.split("<body", 1)[-1]
    if PUBLIC_TEXT_TAGS.search(body):
        failures.append("site/index.html contains visible route content; keep route copy in site/content")
    if 'type="module"' not in index or "assets/js/os.js" not in index:
        failures.append("site/index.html must load the module runtime from assets/js/os.js")


def validate_manifest(failures: list[str]) -> None:
    manifest = read_json(SITE / "manifest.json", failures)
    if not isinstance(manifest, dict):
        return
    for key in ("start_url", "scope"):
        if manifest.get(key) != ".":
            failures.append(f"site/manifest.json {key} must be '.'")
    for index, icon in enumerate(manifest.get("icons", [])):
        if isinstance(icon, dict) and isinstance(icon.get("src"), str):
            validate_local_file(icon["src"], SITE / "manifest.json", failures, f"site/manifest.json.icons[{index}].src")


def validate_content_model(failures: list[str]) -> tuple[dict, dict, dict, dict, dict]:
    site = read_json(SITE / "content/site.json", failures)
    pages = read_json(SITE / "content/pages.json", failures)
    projects = read_json(SITE / "content/projects.json", failures)
    blog = read_json(SITE / "content/blog.json", failures)
    cv = read_json(SITE / "content/cv.json", failures)
    data_files = {
        "site/content/site.json": site,
        "site/content/pages.json": pages,
        "site/content/projects.json": projects,
        "site/content/blog.json": blog,
        "site/content/cv.json": cv,
    }

    for name, data in data_files.items():
        validate_json_content_hygiene(name, data, failures)

    routes = site.get("routes", []) if isinstance(site, dict) else []
    if not isinstance(routes, list) or not routes:
        failures.append("site/content/site.json routes must be a non-empty list")
        return site, pages, projects, blog, cv

    route_paths = [normalize_route(item.get("path", "")) for item in routes if isinstance(item, dict)]
    if len(route_paths) != len(set(route_paths)):
        failures.append("site/content/site.json has duplicate route paths")
    route_set = set(route_paths)

    source_maps = {
        "pages": set((pages.get("pages") or {}).keys()) if isinstance(pages, dict) else set(),
        "projects": {"index"} | {item.get("id") for item in projects.get("items", []) if isinstance(item, dict)} if isinstance(projects, dict) else set(),
        "blog": {"index"} | {item.get("id") for item in blog.get("items", []) if isinstance(item, dict)} if isinstance(blog, dict) else set(),
        "cv": {item.get("id") for item in cv.get("views", []) if isinstance(item, dict)} if isinstance(cv, dict) else set(),
    }
    for item in routes:
        if not isinstance(item, dict):
            failures.append("site/content/site.json routes entries must be objects")
            continue
        source = item.get("source")
        item_id = item.get("id")
        if source not in source_maps:
            failures.append(f"site/content/site.json route {item.get('path')} has unknown source {source}")
        elif item_id not in source_maps[source]:
            failures.append(f"site/content/site.json route {item.get('path')} references missing {source} item {item_id}")

    for legacy, target in (site.get("legacyRoutes") or {}).items():
        if normalize_route(target) not in route_set:
            failures.append(f"site/content/site.json legacy route {legacy} targets unknown route {target}")

    for name, data in data_files.items():
        validate_refs(name, data, SITE / "index.html", route_set, failures)
    return site, pages, projects, blog, cv


def validate_css(failures: list[str]) -> None:
    css = (SITE / "assets/css/site.css").read_text(encoding="utf-8")
    missing = sorted(token for token in REQUIRED_CSS_TOKENS if token not in css)
    if missing:
        failures.append(f"site/assets/css/site.css missing design tokens: {', '.join(missing)}")


def validate_runtime_content_boundary(site: dict, pages: dict, projects: dict, blog: dict, cv: dict, failures: list[str]) -> None:
    js_text = "\n".join(path.read_text(encoding="utf-8") for path in (SITE / "assets/js").glob("*.js"))
    content_strings: set[str] = set()
    schema_keys = {".type", ".collection", ".layout", ".control", ".source", ".id"}
    for data in (site, pages, projects, blog, cv):
        for path, value in walk_json(data):
            if isinstance(value, str) and len(value) >= 8 and not value.startswith(("assets/", "content/", "https://")):
                if value.startswith("/"):
                    continue
                if any(path.endswith(key) for key in schema_keys):
                    continue
                if re.search(r"\.(json|pdf|tex|md|html)$", value):
                    continue
                content_strings.add(value)
    for value in sorted(content_strings, key=len, reverse=True):
        literal = re.compile(rf"['\"]{re.escape(value)}['\"]")
        if literal.search(js_text):
            failures.append(f"site/assets/js hardcodes content string from data: {value[:80]}")
            break


def validate_public_status(failures: list[str]) -> None:
    root_status = ROOT / "data/public-status.json"
    site_status = SITE / "assets/data/public-status.json"
    if not root_status.is_file():
        failures.append("data/public-status.json missing")
        return
    root_data = read_json(root_status, failures)
    site_data = read_json(site_status, failures)
    if root_data != site_data:
        failures.append("data/public-status.json and site/assets/data/public-status.json must match")


def main() -> int:
    failures: list[str] = []
    for required in REQUIRED_FILES:
        if not (SITE / required).is_file():
            failures.append(f"Missing required site file: {required}")

    validate_single_shell(failures)
    validate_manifest(failures)
    site, pages, projects, blog, cv = validate_content_model(failures)
    validate_css(failures)
    validate_runtime_content_boundary(site, pages, projects, blog, cv, failures)
    validate_public_status(failures)

    if failures:
        print("Static site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Static site validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

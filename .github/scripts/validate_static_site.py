"""Validate the plain static GitHub Pages source."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"
BASE_PATH = "/AgenticCareerBoost"

REQUIRED_FILES = [
    "index.html",
    "projects/index.html",
    "projects/agentic-career-boost/index.html",
    "projects/p3ctex/index.html",
    "projects/ironbank/index.html",
    "blog/index.html",
    "dashboard/index.html",
    "curriculum/index.html",
    "contact/index.html",
    "notes/index.html",
    "hire/index.html",
    "hire/ml/index.html",
    "hire/agentic/index.html",
    "hire/backend/index.html",
    "assets/css/site.css",
    "assets/data/blog-index.json",
    "assets/data/notes-index.json",
    "assets/data/os-index.json",
    "assets/js/cv.js",
    "assets/js/os.js",
    "manifest.json",
    "robots.txt",
    "sitemap.xml",
    ".nojekyll",
]

REF_PATTERN = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
JSON_REF_KEYS = {
    "href",
    "src",
    "route",
    "canonical",
    "stylesheet",
    "blogIndex",
    "legacyNotesIndex",
    "notesIndex",
    "heroImage",
    "portraitImage",
    "avatarImage",
    "cvPdf",
    "cvTex",
    "cvTexSource",
    "repository",
    "thumbnail",
    "source",
    "cv",
}
JSON_REF_LIST_KEYS = {"scripts", "assets", "sameAs"}
ALLOWED_EXTERNAL_PREFIXES = (
    "https://didacll.github.io/AgenticCareerBoost/",
    "https://github.com/DidacLL",
    "https://www.linkedin.com/in/didacllorens/",
    "https://raw.githubusercontent.com/DidacLL/AgenticCareerBoost/main/assets/diagrams/",
    "https://github.com/DidacLL/AgenticCareerBoost/raw/main/content/reports/build/",
    "https://github.com/DidacLL/AgenticCareerBoost/tree/main/content/reports/build",
    "https://github.com/DidacLL/AgenticCareerBoost/blob/main/data/public-status.json",
)


def route_target(ref: str, source: Path) -> Path | None:
    parsed = urlsplit(ref)
    if parsed.scheme or parsed.netloc:
        return None
    if not parsed.path:
        return None

    if parsed.path.startswith(f"{BASE_PATH}/") or parsed.path == f"{BASE_PATH}/":
        relative = unquote(parsed.path.removeprefix(BASE_PATH)) or "/"
        base = SITE
    elif parsed.path.startswith("/"):
        return (ROOT / "__invalid_root_relative_static_site_ref__").resolve()
    else:
        relative = unquote(parsed.path)
        base = source.parent

    if relative.endswith("/"):
        relative = f"{relative}index.html"
    return (base / relative.lstrip("/")).resolve()


def is_allowed_external(ref: str) -> bool:
    parsed = urlsplit(ref)
    if not parsed.scheme and not parsed.netloc:
        return True
    if parsed.scheme != "https":
        return False
    return any(ref.startswith(prefix) for prefix in ALLOWED_EXTERNAL_PREFIXES)


def validate_local_ref(ref: str, source: Path, failures: list[str], context: str) -> None:
    parsed = urlsplit(ref)
    if parsed.scheme or parsed.netloc:
        if not is_allowed_external(ref):
            failures.append(f"{context} references unapproved external URL: {ref}")
        return
    if parsed.path.startswith("/") or ".." in Path(parsed.path).parts:
        failures.append(f"{context} uses unsafe local ref: {ref}")
        return
    target = route_target(ref, source)
    if target is None:
        return
    try:
        target.relative_to(SITE.resolve())
    except ValueError:
        failures.append(f"{context} escapes site root: {ref}")
        return
    if not target.is_file():
        failures.append(f"{context} references missing file: {ref}")


def iter_json_refs(node: object, parent_key: str = ""):
    if isinstance(node, dict):
        for key, value in node.items():
            if isinstance(value, str) and key in JSON_REF_KEYS:
                yield key, value
            elif isinstance(value, list) and key in JSON_REF_LIST_KEYS:
                for item in value:
                    if isinstance(item, str):
                        yield key, item
            yield from iter_json_refs(value, key)
    elif isinstance(node, list):
        for item in node:
            yield from iter_json_refs(item, parent_key)


def validate_os_index(failures: list[str]) -> None:
    path = SITE / "assets/data/os-index.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation should report parse errors cleanly.
        failures.append(f"assets/data/os-index.json is invalid JSON: {exc}")
        return

    required_keys = {"version", "site", "assets", "routes", "projects", "rolePaths"}
    missing = required_keys.difference(data)
    if missing:
        failures.append(f"assets/data/os-index.json missing keys: {', '.join(sorted(missing))}")

    if not isinstance(data.get("routes"), list) or not data["routes"]:
        failures.append("assets/data/os-index.json routes must be a non-empty list")
    if not isinstance(data.get("projects"), list) or not data["projects"]:
        failures.append("assets/data/os-index.json projects must be a non-empty list")
    if not isinstance(data.get("rolePaths"), list) or not data["rolePaths"]:
        failures.append("assets/data/os-index.json rolePaths must be a non-empty list")

    site_root_source = SITE / "index.html"
    for key, ref in iter_json_refs(data):
        validate_local_ref(ref, site_root_source, failures, f"assets/data/os-index.json:{key}")


def validate_slot_index(path: Path, failures: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation should report parse errors cleanly.
        failures.append(f"{path.relative_to(SITE)} is invalid JSON: {exc}")
        return

    label = path.relative_to(SITE)
    required_keys = {"version", "updated", "source", "slots"}
    missing = required_keys.difference(data)
    if missing:
        failures.append(f"{label} missing keys: {', '.join(sorted(missing))}")
    if not isinstance(data.get("slots"), list):
        failures.append(f"{label} slots must be a list")

    site_root_source = SITE / "index.html"
    for key, ref in iter_json_refs(data):
        validate_local_ref(ref, site_root_source, failures, f"{label}:{key}")


def validate_manifest(failures: list[str]) -> None:
    path = SITE / "manifest.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        failures.append(f"manifest.json is invalid JSON: {exc}")
        return
    for icon in data.get("icons", []):
        if isinstance(icon, dict) and isinstance(icon.get("src"), str):
            validate_local_ref(icon["src"], SITE / "index.html", failures, "manifest.json:icons.src")


def validate_html_head(text: str, html_file: Path, failures: list[str]) -> None:
    required = [
        'rel="canonical"',
        'property="og:title"',
        'property="og:description"',
        'property="og:image"',
        'name="twitter:card"',
        'name="twitter:image"',
    ]
    for needle in required:
        if needle not in text:
            failures.append(f"{html_file.relative_to(ROOT)} missing head metadata: {needle}")


def html_files() -> list[Path]:
    return sorted(SITE.rglob("*.html"))


def main() -> int:
    failures: list[str] = []

    for required in REQUIRED_FILES:
        path = SITE / required
        if not path.is_file():
            failures.append(f"missing required file: site/{required}")

    ref_count = 0
    for html_file in html_files():
        text = html_file.read_text(encoding="utf-8")
        validate_html_head(text, html_file, failures)
        for match in REF_PATTERN.finditer(text):
            ref = match.group(1)
            if not is_allowed_external(ref):
                failures.append(f"{html_file.relative_to(ROOT)} references unapproved external URL: {ref}")
                continue
            target = route_target(ref, html_file)
            if target is None:
                continue
            ref_count += 1
            try:
                target.relative_to(SITE.resolve())
            except ValueError:
                failures.append(f"{html_file.relative_to(ROOT)} escapes site root: {match.group(1)}")
                continue
            if not target.is_file():
                failures.append(
                    f"{html_file.relative_to(ROOT)} references missing route: {match.group(1)}"
                )

    validate_os_index(failures)
    validate_slot_index(SITE / "assets/data/blog-index.json", failures)
    validate_slot_index(SITE / "assets/data/notes-index.json", failures)
    validate_manifest(failures)

    if failures:
        print("Static site validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Static site validation passed: {len(REQUIRED_FILES)} required files, "
        f"{len(html_files())} HTML files, {ref_count} internal refs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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
    "dashboard/index.html",
    "curriculum/index.html",
    "contact/index.html",
    "notes/index.html",
    "hire/index.html",
    "assets/css/site.css",
    "assets/data/notes-index.json",
    "assets/data/os-index.json",
    "assets/js/cv.js",
    "assets/js/os.js",
    ".nojekyll",
]

REF_PATTERN = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
JSON_REF_KEYS = {"href", "src", "route", "canonical", "stylesheet", "notesIndex", "heroImage", "portraitImage", "cvPdf", "cvTex"}
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

    required_keys = {"version", "site", "assets", "panels", "routes"}
    missing = required_keys.difference(data)
    if missing:
        failures.append(f"assets/data/os-index.json missing keys: {', '.join(sorted(missing))}")

    if not isinstance(data.get("panels"), list) or not data["panels"]:
        failures.append("assets/data/os-index.json panels must be a non-empty list")
    if not isinstance(data.get("routes"), list) or not data["routes"]:
        failures.append("assets/data/os-index.json routes must be a non-empty list")

    site_root_source = SITE / "index.html"
    for key, ref in iter_json_refs(data):
        validate_local_ref(ref, site_root_source, failures, f"assets/data/os-index.json:{key}")


def validate_notes_index(failures: list[str]) -> None:
    path = SITE / "assets/data/notes-index.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation should report parse errors cleanly.
        failures.append(f"assets/data/notes-index.json is invalid JSON: {exc}")
        return

    required_keys = {"version", "updated", "source", "slots"}
    missing = required_keys.difference(data)
    if missing:
        failures.append(f"assets/data/notes-index.json missing keys: {', '.join(sorted(missing))}")
    if not isinstance(data.get("slots"), list):
        failures.append("assets/data/notes-index.json slots must be a list")
    validate_local_ref(str(data.get("source", "")), SITE / "index.html", failures, "assets/data/notes-index.json:source")


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
    validate_notes_index(failures)

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

"""Validate the plain static GitHub Pages source."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"
BASE_PATH = "/"

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
    "assets/data/public-status.json",
    "assets/js/cv.js",
    "assets/js/os.js",
    "manifest.json",
    "robots.txt",
    ".nojekyll",
]

REF_PATTERN = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
JSON_REF_KEYS = {
    "href",
    "src",
    "route",
    "canonical",
    "stylesheet",
    "publicStatus",
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
    "https://github.com/DidacLL",
    "https://www.linkedin.com/in/didacllorens/",
    "https://raw.githubusercontent.com/DidacLL/AgenticCareerBoost/main/assets/diagrams/",
    "https://github.com/DidacLL/AgenticCareerBoost/raw/main/content/reports/build/",
    "https://github.com/DidacLL/AgenticCareerBoost/tree/main/content/reports/build",
    "https://github.com/DidacLL/AgenticCareerBoost/blob/main/data/public-status.json",
)
DEPLOYMENT_BOUND_HOST = ".".join(("didacll", "github", "io"))
UNSAFE_DEPLOYED_PARTS = {".idea", ".vscode", ".DS_Store"}
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


def route_target(ref: str, source: Path) -> Path | None:
    parsed = urlsplit(ref)
    if parsed.scheme or parsed.netloc:
        return None
    if not parsed.path:
        return None

    if parsed.path.startswith("/"):
        relative = unquote(parsed.path.lstrip("/")) or "index.html"
        base = SITE
    else:
        relative = unquote(parsed.path)
        base = source.parent

    if relative.endswith("/"):
        relative = f"{relative}index.html"
    return (base / relative).resolve()


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
    if ".." in Path(parsed.path).parts:
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
    assets = data.get("assets", {})
    if isinstance(assets, dict):
        for key in ("publicStatus",):
            if key not in assets:
                failures.append(f"assets/data/os-index.json missing assets.{key}")

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
    for key in ("start_url", "scope"):
        if data.get(key) != ".":
            failures.append(f"manifest.json {key} must be '.' so deployment base is runtime-relative")
    for icon in data.get("icons", []):
        if isinstance(icon, dict) and isinstance(icon.get("src"), str):
            validate_local_ref(icon["src"], SITE / "index.html", failures, "manifest.json:icons.src")


def validate_public_status(failures: list[str]) -> None:
    root_path = ROOT / "data/public-status.json"
    site_path = SITE / "assets/data/public-status.json"
    try:
        root_data = json.loads(root_path.read_text(encoding="utf-8"))
        site_data = json.loads(site_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        failures.append(f"public status JSON is invalid: {exc}")
        return
    if root_data != site_data:
        failures.append("data/public-status.json and site/assets/data/public-status.json must match")
    required_keys = {"schema_version", "updated", "sources", "sprint_id", "workflow", "status", "artifacts", "blockers"}
    missing = required_keys.difference(site_data)
    if missing:
        failures.append(f"assets/data/public-status.json missing keys: {', '.join(sorted(missing))}")


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


def validate_no_deployment_bound_host(failures: list[str]) -> None:
    scanned_suffixes = {".html", ".xml", ".txt", ".json", ".js", ".css"}
    for path in SITE.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in scanned_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if DEPLOYMENT_BOUND_HOST in text:
            failures.append(
                f"{path.relative_to(ROOT)} hardcodes deployment host {DEPLOYMENT_BOUND_HOST}; "
                "site pages and deploy metadata must derive the public base at runtime"
            )


def validate_css_tokens(failures: list[str]) -> None:
    path = SITE / "assets/css/site.css"
    text = path.read_text(encoding="utf-8")
    for token in sorted(REQUIRED_CSS_TOKENS):
        if token not in text:
            failures.append(f"assets/css/site.css missing required design token: {token}")
    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if "px" in stripped and not stripped.startswith("--") and not stripped.startswith("@media"):
            failures.append(f"assets/css/site.css:{line_number} uses raw px outside token/breakpoint definitions")
        if re.search(r"font-size\s*:[^;]*(vw|vh|vmin|vmax)", stripped):
            failures.append(f"assets/css/site.css:{line_number} uses viewport units for font-size")
        if "height: contain" in stripped:
            failures.append(f"assets/css/site.css:{line_number} uses invalid declaration height: contain")
        if "!important" in stripped:
            allowed = "[hidden]" in text[max(0, text.find(line) - 120):text.find(line)] or "display: none !important" in stripped
            allowed = allowed or "animation" in stripped or "transition" in stripped or "scroll-behavior" in stripped
            if not allowed:
                failures.append(f"assets/css/site.css:{line_number} uses non-gate allowlisted !important")


def tracked_site_files() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "site"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:  # noqa: BLE001
        return [
            path.relative_to(ROOT).as_posix()
            for path in SITE.rglob("*")
            if path.is_file()
        ]
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def validate_deployed_artifact_hygiene(failures: list[str]) -> None:
    for tracked in tracked_site_files():
        parts = set(Path(tracked).parts)
        if parts.intersection(UNSAFE_DEPLOYED_PARTS):
            failures.append(f"tracked deployed artifact should be ignored/removed: {tracked}")


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
                failures.append(f"{html_file.relative_to(ROOT)} missing file for ref: {match.group(1)}")

    validate_os_index(failures)
    validate_public_status(failures)
    validate_slot_index(SITE / "assets/data/blog-index.json", failures)
    validate_slot_index(SITE / "assets/data/notes-index.json", failures)
    validate_manifest(failures)
    validate_css_tokens(failures)
    validate_deployed_artifact_hygiene(failures)
    validate_no_deployment_bound_host(failures)

    if failures:
        print("Static site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Static site validation passed ({len(html_files())} HTML files, {ref_count} local refs).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Validate the canonical site/ Pages artifact."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
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

CV_REQUIRED = [
    "README.md",
    "latexmkrc",
    "build-local.sh",
    "build-local.ps1",
    "artifacts.json",
    "tools/artifact_manifest.py",
]


def git_executable() -> str | None:
    found = shutil.which("git")
    if found:
        return found
    windows_git = Path("C:/Program Files/Git/cmd/git.exe")
    if windows_git.exists():
        return str(windows_git)
    return None


def read_manifest(failures: list[str]) -> list[dict]:
    path = ROOT / "agents" / "cv" / "artifacts.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"agents/cv/artifacts.json invalid JSON: {exc}")
        return []
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        failures.append("agents/cv/artifacts.json must declare at least one artifact")
        return []
    public = []
    for item in artifacts:
        if item.get("publish") is not True:
            continue
        kind = item.get("kind")
        if kind == "cover-letter":
            failures.append(
                "cover letters are private/local documents and must not be published by agents/cv/artifacts.json"
            )
            continue
        if kind != "cv":
            failures.append(f"unsupported public CV artifact kind in manifest: {kind}")
            continue
        public.append(item)
    if not public:
        failures.append("agents/cv/artifacts.json must declare at least one public CV artifact")
    return public


def safe_relative(value: object) -> Path | None:
    text = str(value or "").strip()
    if not text:
        return None
    path = Path(text)
    if path.is_absolute() or ".." in path.parts:
        return None
    return path


def walk_json(node, pointer="$"):
    if isinstance(node, dict):
        for key, value in node.items():
            yield from walk_json(value, f"{pointer}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from walk_json(value, f"{pointer}[{index}]")
    else:
        yield pointer, node


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
        for token in ("isStaticFileHref", 'attrs.target = "_blank"', "attrs.download"):
            if token not in components_text:
                failures.append(f"site/assets/js/components.js missing file-link marker: {token}")
    fallback = SITE / "404.html"
    if fallback.is_file():
        fallback_text = fallback.read_text(encoding="utf-8")
        for token in (
            "candidateBases(normalizedPath)",
            "hasSiteContent(candidate)",
            "content/site.json",
            "routeForBase(normalizedPath, base)",
            "isStaticFileRoute(clean)",
            "File not found.",
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

    cv_root = ROOT / "agents" / "cv"
    for relative in CV_REQUIRED:
        if not (cv_root / relative).is_file():
            failures.append(f"missing CV artifact source file: agents/cv/{relative}")

    artifacts = read_manifest(failures)
    manifest_site_paths: set[str] = set()
    manifest_cv_source_urls: set[str] = set()
    generated_paths: list[str] = []
    for item in artifacts:
        kind = item.get("kind")
        source = safe_relative(item.get("source"))
        build_pdf = safe_relative(item.get("buildPdf"))
        site_pdf = safe_relative(item.get("sitePdf"))
        if kind != "cv":
            failures.append(f"unsupported public CV artifact kind in manifest: {kind}")
        if source is None or build_pdf is None or site_pdf is None:
            failures.append(f"CV artifact manifest entry has unsafe or missing paths: {item}")
            continue
        if build_pdf.parts[:1] != ("build",):
            failures.append(f"CV artifact buildPdf must stay under agents/cv/build: {build_pdf}")
        if site_pdf.parts[:2] != ("site", "files"):
            failures.append(f"CV artifact sitePdf must stay under site/files: {site_pdf}")
        if kind == "cv":
            if not (cv_root / source).is_file():
                failures.append(f"missing CV source declared by manifest: agents/cv/{source.as_posix()}")
            manifest_cv_source_urls.add(f"https://github.com/DidacLL/AgenticCareerBoost/blob/main/agents/cv/{source.as_posix()}")
        site_output = ROOT / site_pdf
        if not site_output.is_file():
            failures.append(f"missing generated public career PDF: {site_pdf.as_posix()}")
        manifest_site_paths.add(site_pdf.as_posix().removeprefix("site/"))
        generated_paths.extend([site_pdf.as_posix(), f"agents/cv/{build_pdf.as_posix()}"])
        if source.parts[:1] == ("build",):
            generated_paths.append(f"agents/cv/{source.as_posix()}")

    for relative in ("site.json", "pages.json", "projects.json", "blog.json", "cv.json"):
        path = SITE / "content" / relative
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"site/content/{relative} invalid JSON: {exc}")

    cv_json = SITE / "content" / "cv.json"
    if cv_json.is_file():
        cv_text = cv_json.read_text(encoding="utf-8")
        for url in manifest_cv_source_urls:
            if url not in cv_text:
                failures.append("site/content/cv.json must link the manifest-declared CV source")

    for relative in ("cv.json", "projects.json"):
        path = SITE / "content" / relative
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            stale_site_curriculum = "site/assets/" + "curriculum/"
            for token in ("assets/curriculum/", stale_site_curriculum):
                if token in text:
                    failures.append(f"site/content/{relative} contains stale CV/curriculum token: {token}")

    route_paths = set()
    site_json = SITE / "content" / "site.json"
    if site_json.is_file():
        try:
            route_paths = {item["path"] for item in json.loads(site_json.read_text(encoding="utf-8")).get("routes", [])}
        except Exception:
            route_paths = set()

    public_pdf_paths: set[str] = set()
    for json_file in (SITE / "content").glob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding="utf-8"))
        except Exception:
            continue
        for pointer, value in walk_json(data):
            if not isinstance(value, str):
                continue
            key = pointer.rsplit(".", 1)[-1].split("[", 1)[0]
            if key == "route" and value.startswith("/files/"):
                failures.append(f"site/content/{json_file.name}:{pointer} file path stored as app route: {value}")
            if key == "href" and value.startswith("#/files/"):
                failures.append(f"site/content/{json_file.name}:{pointer} file link uses hash route: {value}")
            if key == "href" and value.startswith("files/"):
                local = value.split("#", 1)[0].split("?", 1)[0]
                if local.startswith("files/cover-letters/"):
                    failures.append(
                        f"site/content/{json_file.name}:{pointer} cover-letter links are private/local only: {value}"
                    )
                    continue
                if local.lower().endswith(".pdf"):
                    public_pdf_paths.add(f"site/{local}")
                if value in route_paths:
                    failures.append(f"site/content/{json_file.name}:{pointer} file link collides with app route: {value}")
                if not (SITE / local).is_file():
                    failures.append(f"site/content/{json_file.name}:{pointer} missing file link: {value}")
                if value in manifest_site_paths and '"newTab": true' not in json_file.read_text(encoding="utf-8"):
                    failures.append(f"site/content/{json_file.name}:{pointer} generated PDF links must opt into newTab")

    git = git_executable()
    if git is None:
        failures.append("git executable is required for generated artifact validation")
    else:
        tracked_site_files = subprocess.run(
            [git, "ls-files", "site/files"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        tracked_public_pdfs = [path for path in tracked_site_files if path.lower().endswith(".pdf")]
        if tracked_public_pdfs:
            failures.append(f"public site PDFs must be generated, not tracked: {', '.join(tracked_public_pdfs)}")

        if public_pdf_paths:
            ignored_public_pdfs = subprocess.run(
                [git, "check-ignore", "--no-index", *sorted(public_pdf_paths)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            ).stdout.splitlines()
            missing_ignored_public_pdfs = sorted(public_pdf_paths - set(ignored_public_pdfs))
            if missing_ignored_public_pdfs:
                failures.append(
                    "public site PDF output paths must be ignored by .gitignore: "
                    + ", ".join(missing_ignored_public_pdfs)
                )

        if generated_paths:
            tracked = subprocess.run(
                [git, "ls-files", *generated_paths],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.splitlines()
            if tracked:
                failures.append(f"generated public career PDFs must not be tracked: {', '.join(tracked)}")
            ignored = subprocess.run(
                [git, "check-ignore", "--no-index", *generated_paths],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            ).stdout.splitlines()
            if set(ignored) != set(generated_paths):
                failures.append("generated public career PDF paths must be ignored by .gitignore")

    if failures:
        print("Static site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Static site validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

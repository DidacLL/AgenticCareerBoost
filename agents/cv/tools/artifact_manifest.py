"""Read the CV artifact manifest used by local builds and CI."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


CV_ROOT = Path(__file__).resolve().parents[1]
ROOT = CV_ROOT.parents[1]
DEFAULT_MANIFEST = CV_ROOT / "artifacts.json"
COVER_LETTER_MESSAGE = (
    "cover letters are private/local working documents; render one explicitly "
    "with agents/cv/tools/render-cover-letter.py --input"
)


def as_relative_path(value: object, field: str) -> Path:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"missing manifest field: {field}")
    path = Path(text)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{field} must be a repository-relative safe path: {text}")
    return path


def load_manifest(path: Path = DEFAULT_MANIFEST) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise ValueError(f"{path}: artifacts must be a non-empty list")
    return artifacts


def published(path: Path = DEFAULT_MANIFEST) -> list[dict]:
    return [item for item in load_manifest(path) if item.get("publish") is True]


def public_artifacts(path: Path = DEFAULT_MANIFEST) -> list[dict]:
    artifacts = []
    for item in published(path):
        kind = item.get("kind")
        if kind == "cover-letter":
            raise ValueError(COVER_LETTER_MESSAGE)
        if kind != "cv":
            raise ValueError(f"unsupported public artifact kind: {kind}")
        artifacts.append(item)
    if not artifacts:
        raise ValueError(f"{path}: manifest must declare at least one public CV artifact")
    return artifacts


def build_roots(path: Path = DEFAULT_MANIFEST) -> list[str]:
    roots = []
    for item in public_artifacts(path):
        source = as_relative_path(item.get("source"), "source")
        roots.append(source.as_posix())
    return roots


def data_inputs(path: Path = DEFAULT_MANIFEST) -> list[Path]:
    public_artifacts(path)
    return []


def copy_published(path: Path = DEFAULT_MANIFEST) -> None:
    for item in public_artifacts(path):
        build_pdf = as_relative_path(item.get("buildPdf"), "buildPdf")
        site_pdf = as_relative_path(item.get("sitePdf"), "sitePdf")
        source = CV_ROOT / build_pdf
        destination = ROOT / site_pdf
        if not source.is_file():
            raise FileNotFoundError(f"missing built artifact: {source.relative_to(ROOT)}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        print(f"published {destination.relative_to(ROOT).as_posix()}")


def validate(path: Path = DEFAULT_MANIFEST) -> None:
    for item in public_artifacts(path):
        kind = item.get("kind")
        source = as_relative_path(item.get("source"), "source")
        build_pdf = as_relative_path(item.get("buildPdf"), "buildPdf")
        site_pdf = as_relative_path(item.get("sitePdf"), "sitePdf")
        if build_pdf.parts[:1] != ("build",):
            raise ValueError(f"buildPdf must be under agents/cv/build: {build_pdf}")
        if site_pdf.parts[:2] != ("site", "files"):
            raise ValueError(f"sitePdf must be under site/files: {site_pdf}")
        if site_pdf.suffix.lower() != ".pdf" or build_pdf.suffix.lower() != ".pdf":
            raise ValueError(f"artifact outputs must be PDFs: {site_pdf}")
        if kind == "cv" and not (CV_ROOT / source).is_file():
            raise FileNotFoundError(f"missing CV source: {source}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["roots", "data", "publish", "validate"])
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "roots":
        print("\n".join(build_roots(args.manifest)))
    elif args.command == "data":
        print("\n".join(path.relative_to(CV_ROOT).as_posix() for path in data_inputs(args.manifest)))
    elif args.command == "publish":
        copy_published(args.manifest)
    elif args.command == "validate":
        validate(args.manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

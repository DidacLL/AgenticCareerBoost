"""Render one local letter TeX source from one JSON input."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

TRACKER_ROOT = Path(__file__).resolve().parent
DEFAULT_TEMPLATE = TRACKER_ROOT / "templates" / "letter-template.tex"
DEFAULT_OUTPUT_DIR = TRACKER_ROOT / ".private" / "generated"

SPECIALS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def latex_escape(value: object) -> str:
    return "".join(SPECIALS.get(char, char) for char in str(value))


def safe_output_tex_name(value: object) -> str:
    text = str(value).strip()
    path = Path(text)
    if not text or path.is_absolute() or len(path.parts) != 1 or ".." in path.parts or "/" in text or "\\" in text:
        raise ValueError(f"output_pdf must be a plain filename: {text}")
    return path.with_suffix("").name + ".tex"


def load_letter(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ["output_pdf", "candidate_name", "headline", "recipient", "role", "location", "greeting", "paragraphs", "closing"]
    missing = [key for key in required if not data.get(key)]
    if missing:
        raise ValueError(f"missing required fields: {', '.join(missing)}")
    if not isinstance(data["paragraphs"], list):
        raise ValueError("paragraphs must be a list")
    return data


def render(input_path: Path, template_path: Path, output_dir: Path) -> Path:
    data = load_letter(input_path)
    output_path = output_dir / safe_output_tex_name(data["output_pdf"])
    output_dir.mkdir(parents=True, exist_ok=True)
    values = {
        "PDF_TITLE": latex_escape(f"{data['candidate_name']} -- Letter -- {data['role']}"),
        "CANDIDATE_NAME": latex_escape(data["candidate_name"]),
        "HEADLINE": latex_escape(data["headline"]),
        "RECIPIENT": latex_escape(data["recipient"]),
        "ROLE": latex_escape(data["role"]),
        "LOCATION": latex_escape(data["location"]),
        "GREETING": latex_escape(data["greeting"]),
        "BODY_PARAGRAPHS": "\n\n".join(latex_escape(item) for item in data["paragraphs"]),
        "CLOSING": latex_escape(data["closing"]),
    }
    rendered = template_path.read_text(encoding="utf-8")
    for key, value in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    output_path.write_text(rendered, encoding="utf-8", newline="\n")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    print(render(args.input.resolve(), args.template.resolve(), args.output_dir.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

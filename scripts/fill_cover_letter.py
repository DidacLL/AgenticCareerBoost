#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


KEY_RE = re.compile(r"::([A-Za-z0-9][A-Za-z0-9_-]*)::")

LATEX_ESCAPE = {
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


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing file: {path}") from None


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def keys_from(template: str) -> list[str]:
    return sorted(set(KEY_RE.findall(template)))


def escape_latex(value: str) -> str:
    return "".join(LATEX_ESCAPE.get(char, char) for char in value)


def load_values(path: Path | None) -> dict[str, str]:
    if path is None:
        return {}

    try:
        data = json.loads(read(path))
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in {path}: {error}") from None

    if not isinstance(data, dict):
        raise SystemExit("Values file must contain a JSON object.")

    return {
        str(key): "" if value is None else str(value)
        for key, value in data.items()
    }


def parse_set(items: list[str]) -> dict[str, str]:
    values: dict[str, str] = {}

    for item in items:
        if "@=" in item:
            key, file_path = item.split("@=", 1)
            if not key:
                raise SystemExit(f"Invalid --set value: {item}")
            values[key] = read(Path(file_path))
            continue

        if "=" not in item:
            raise SystemExit(f"Invalid --set value: {item}. Use KEY=VALUE or KEY@=file.txt")

        key, value = item.split("=", 1)
        if not key:
            raise SystemExit(f"Invalid --set value: {item}")

        values[key] = value

    return values


def apply_escape(values: dict[str, str], raw_keys: set[str]) -> dict[str, str]:
    return {
        key: value if key in raw_keys else escape_latex(value)
        for key, value in values.items()
    }


def render(template: str, values: dict[str, str], allow_missing: bool) -> str:
    missing: set[str] = set()

    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            missing.add(key)
            return match.group(0)
        return values[key]

    output = KEY_RE.sub(replace, template)

    if missing and not allow_missing:
        raise SystemExit("Missing values: " + ", ".join(sorted(missing)))

    unresolved = keys_from(output)
    if unresolved and not allow_missing:
        raise SystemExit("Unresolved placeholders: " + ", ".join(unresolved))

    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("template", type=Path)
    parser.add_argument("--values", type=Path)
    parser.add_argument("--set", action="append", default=[])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--init-values", type=Path)
    parser.add_argument("--allow-missing", action="store_true")
    parser.add_argument("--escape", action="store_true")
    parser.add_argument("--raw-key", action="append", default=[])

    args = parser.parse_args()

    template = read(args.template)
    detected_keys = keys_from(template)

    if args.list:
        print("\n".join(detected_keys))
        return 0

    if args.init_values:
        skeleton = {key: "" for key in detected_keys}
        write(args.init_values, json.dumps(skeleton, indent=2, ensure_ascii=False) + "\n")
        return 0

    if args.output is None:
        raise SystemExit("--output is required unless using --list or --init-values")

    values = load_values(args.values)
    values.update(parse_set(args.set))

    if args.escape:
        values = apply_escape(values, set(args.raw_key))

    output = render(template, values, args.allow_missing)
    write(args.output, output)

    extra = sorted(set(values) - set(detected_keys))
    if extra:
        print("Ignored extra values: " + ", ".join(extra), file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
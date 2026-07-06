"""Render one local letter TeX source from one JSON input."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    print(args.input)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

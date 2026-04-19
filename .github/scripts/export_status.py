"""Parse state/ front-matter and write data/public-status.json."""

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def extract_field(text: str, field: str) -> str:
    match = re.search(rf"\*\*{field}\*\*:\s*(.+)", text)
    return match.group(1).strip() if match else ""


def main() -> None:
    current = (ROOT / "state" / "current.md").read_text(encoding="utf-8")
    sprint = (ROOT / "state" / "active-sprint.md").read_text(encoding="utf-8")

    workflow = extract_field(current, "Active workflow") or "none"
    sprint_id = extract_field(sprint, "Sprint ID")
    status_raw = extract_field(sprint, "Status") or "idle"

    closures = re.findall(
        r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\w+)\s*\|", current
    )
    last_closure_at = closures[-1][0] if closures else str(date.today())
    last_closure_type = closures[-1][1] if closures else "unknown"

    blockers_field = extract_field(current, "Blockers")
    blockers = [] if blockers_field.lower() in ("none", "") else [blockers_field]

    roadmap = (ROOT / "state" / "roadmap.md").read_text(encoding="utf-8")
    seed_match = re.search(r"\|\s*S-\d+\s*\|(.+?)\|", roadmap)
    next_seed = seed_match.group(0).strip("| ").strip() if seed_match else ""

    payload = {
        "sprint_id": sprint_id or None,
        "workflow": workflow,
        "status": status_raw,
        "last_closure_at": last_closure_at,
        "last_closure_type": last_closure_type,
        "artifacts": [],
        "blockers": blockers,
        "next_sprint_seed": next_seed,
    }

    out = ROOT / "data" / "public-status.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()

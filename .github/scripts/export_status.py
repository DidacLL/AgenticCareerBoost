"""Parse state files and write data/public-status.json."""

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def extract_field(text: str, field: str) -> str:
    match = re.search(rf"\*\*{field}\*\*:\s*(.+)", text)
    return match.group(1).strip() if match else ""


def is_none_like(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in {"", "none", "null", "n/a"}


def extract_closure_artifacts(text: str) -> list[dict[str, str | bool]]:
    artifacts = []
    in_section = False
    for line in text.splitlines():
        if line.strip() == "## Closure artifacts":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        match = re.match(r"- \[(x| )\]\s+(.+)", line)
        if not match:
            continue
        checked = match.group(1) == "x"
        label = match.group(2).strip()
        artifacts.append({"complete": checked, "label": label})
    if artifacts:
        return artifacts

    in_section = False
    for line in text.splitlines():
        if line.strip() == "## Closure matrix":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if not in_section:
            continue
        match = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if not match:
            continue
        dimension, state, evidence = (part.strip() for part in match.groups())
        if dimension in {"Dimension", "---"} or set(dimension) == {"-"}:
            continue
        state_normalized = state.lower()
        complete = state_normalized in {"done", "complete", "completed", "pass", "passed", "closed"}
        artifacts.append(
            {
                "complete": complete,
                "label": f"{dimension} — {state}: {evidence}",
            }
        )
    return artifacts


def split_blockers(value: str) -> list[str]:
    normalized = value.strip().lower()
    if normalized in ("none", "") or normalized.startswith("none for "):
        return []
    return [part.strip().rstrip(".") for part in value.split(";") if part.strip()]


def main() -> None:
    current = (ROOT / "state" / "current.md").read_text(encoding="utf-8")
    sprint = (ROOT / "state" / "active-sprint.md").read_text(encoding="utf-8")

    workflow = extract_field(current, "Active workflow") or "none"
    active_sprint = extract_field(current, "Active sprint")
    sprint_id = None if is_none_like(active_sprint) else extract_field(sprint, "Sprint ID")
    status_raw = extract_field(sprint, "Status") if sprint_id else "idle"
    status = status_raw or "idle"

    closures = re.findall(
        r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^|]+?)\s*\|", current
    )
    last_closure_at = closures[0][0] if closures else str(date.today())
    last_closure_type = closures[0][1] if closures else "unknown"

    blockers = split_blockers(extract_field(current, "Blockers"))

    roadmap = (ROOT / "state" / "roadmap.md").read_text(encoding="utf-8")
    next_seed = ""
    for sprint_id_match, title, focus in re.findall(
        r"\|\s*(S-\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", roadmap
    ):
        if "closed" in focus.lower():
            continue
        next_seed = f"{sprint_id_match}: {title}"
        break

    payload = {
        "sprint_id": sprint_id,
        "workflow": workflow,
        "status": status,
        "last_closure_at": last_closure_at,
        "last_closure_type": last_closure_type,
        "artifacts": extract_closure_artifacts(sprint),
        "blockers": blockers,
        "next_sprint_seed": next_seed,
    }

    out = ROOT / "data" / "public-status.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()

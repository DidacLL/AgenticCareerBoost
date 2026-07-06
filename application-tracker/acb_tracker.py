"""Local SQLite application tracker with an HTML dashboard."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sqlite3
from datetime import date, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

TRACKER_ROOT = Path(__file__).resolve().parent
REPO_ROOT = TRACKER_ROOT.parent
DEFAULT_HOME = TRACKER_ROOT / ".private"
DB_NAME = "applications.sqlite"
STATUSES = [
    "found",
    "evaluating",
    "ready_to_apply",
    "applied",
    "follow_up",
    "interview",
    "technical_test",
    "offer",
    "rejected",
    "rejected_by_me",
    "archived",
]


def private_home() -> Path:
    configured = os.environ.get("ACB_APPLICATION_TRACKER_HOME")
    path = Path(configured).expanduser() if configured else DEFAULT_HOME
    return path.resolve()


def assert_safe_home(path: Path) -> None:
    resolved = path.resolve()
    try:
        resolved.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return
    try:
        resolved.relative_to(DEFAULT_HOME.resolve())
    except ValueError as exc:
        raise SystemExit(
            "Application Tracker data inside this repository must stay under "
            "application-tracker/.private/. Set ACB_APPLICATION_TRACKER_HOME for an external store."
        ) from exc


def db_path() -> Path:
    home = private_home()
    assert_safe_home(home)
    return home / DB_NAME


def connect() -> sqlite3.Connection:
    path = db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    home = private_home()
    assert_safe_home(home)
    (home / "attachments").mkdir(parents=True, exist_ok=True)
    (home / "generated").mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id TEXT PRIMARY KEY,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                source TEXT,
                source_url TEXT,
                location TEXT,
                remote_mode TEXT,
                status TEXT NOT NULL DEFAULT 'found',
                priority TEXT NOT NULL DEFAULT 'medium',
                created_at TEXT NOT NULL,
                applied_at TEXT,
                last_touch TEXT NOT NULL,
                next_action TEXT,
                notes TEXT
            );

            CREATE TABLE IF NOT EXISTS offer_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                raw_text TEXT NOT NULL,
                cleaned_text TEXT,
                captured_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS company_research (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT REFERENCES applications(id) ON DELETE CASCADE,
                company TEXT NOT NULL,
                summary TEXT,
                business_model TEXT,
                red_flags TEXT,
                sources_json TEXT,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                verdict TEXT,
                fit_score INTEGER,
                risk_score INTEGER,
                effort_score INTEGER,
                reasoning TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS form_answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                question TEXT NOT NULL,
                draft_answer TEXT,
                submitted_answer TEXT,
                submitted_at TEXT
            );

            CREATE TABLE IF NOT EXISTS cover_letters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                draft_text TEXT,
                submitted_text TEXT,
                version TEXT,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS interview_guides (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                guide_text TEXT NOT NULL,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS stack_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                term TEXT NOT NULL,
                meaning TEXT,
                why_it_matters TEXT,
                my_positioning TEXT,
                refresh_needed INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS call_cards (
                application_id TEXT PRIMARY KEY REFERENCES applications(id) ON DELETE CASCADE,
                call_signals TEXT,
                technical_reading TEXT,
                pitch TEXT,
                smart_question TEXT,
                risk_to_avoid TEXT,
                prepare_first TEXT,
                prepare_later TEXT,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS glossary_terms (
                term TEXT PRIMARY KEY,
                category TEXT,
                short_definition TEXT,
                detail TEXT,
                interview_angle TEXT,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS application_keywords (
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                term TEXT NOT NULL REFERENCES glossary_terms(term) ON DELETE CASCADE,
                importance TEXT NOT NULL DEFAULT 'recognize',
                PRIMARY KEY (application_id, term)
            );

            CREATE TABLE IF NOT EXISTS application_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                application_id TEXT NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
                kind TEXT NOT NULL,
                path TEXT NOT NULL,
                label TEXT,
                notes TEXT,
                created_at TEXT NOT NULL
            );
            """
        )
    print(f"initialized {db_path()}")


def slugify(value: str) -> str:
    text = value.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "application"


def make_id(company: str, role: str) -> str:
    base = f"{date.today().isoformat()}-{slugify(company)}-{slugify(role)}"
    candidate = base
    with connect() as conn:
        index = 2
        while conn.execute("SELECT 1 FROM applications WHERE id = ?", (candidate,)).fetchone():
            candidate = f"{base}-{index}"
            index += 1
    return candidate


def read_text_arg(value: str | None, file_value: str | None) -> str:
    if file_value:
        return Path(file_value).expanduser().read_text(encoding="utf-8")
    if value is None:
        raise SystemExit("provide --text or --file")
    return value


def read_optional_text(value: str | None, file_value: str | None) -> str | None:
    if file_value:
        return Path(file_value).expanduser().read_text(encoding="utf-8")
    return value


def listify(value: object) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def create_application(args: argparse.Namespace) -> None:
    init_db()
    now = datetime.now().isoformat(timespec="seconds")
    app_id = args.id or make_id(args.company, args.role)
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO applications (
                id, company, role, source, source_url, location, remote_mode,
                status, priority, created_at, last_touch, next_action, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                app_id,
                args.company,
                args.role,
                args.source,
                args.source_url,
                args.location,
                args.remote_mode,
                args.status,
                args.priority,
                now,
                now,
                args.next_action,
                args.notes,
            ),
        )
    print(app_id)


def ingest_offer(args: argparse.Namespace) -> None:
    init_db()
    text = read_text_arg(args.text, args.file)
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        require_app(conn, args.id)
        conn.execute(
            "INSERT INTO offer_snapshots(application_id, raw_text, cleaned_text, captured_at) VALUES (?, ?, ?, ?)",
            (args.id, text, args.cleaned_text, now),
        )
        touch(conn, args.id, args.next_action)
    print(f"stored offer snapshot for {args.id}")


def set_research(args: argparse.Namespace) -> None:
    init_db()
    now = datetime.now().isoformat(timespec="seconds")
    summary = read_optional_text(args.summary, args.summary_file)
    business_model = read_optional_text(args.business_model, args.business_model_file)
    red_flags = read_optional_text(args.red_flags, args.red_flags_file)
    with connect() as conn:
        app = require_app(conn, args.id)
        conn.execute(
            """
            INSERT INTO company_research(application_id, company, summary, business_model, red_flags, sources_json, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                args.id,
                args.company or app["company"],
                summary,
                business_model,
                red_flags,
                args.sources_json,
                now,
            ),
        )
        touch(conn, args.id, args.next_action)
    print(f"stored company research for {args.id}")


def add_form_answer(args: argparse.Namespace) -> None:
    init_db()
    draft_answer = read_optional_text(args.draft_answer, args.draft_file)
    submitted_answer = read_optional_text(args.submitted_answer, args.submitted_file)
    if draft_answer is None and submitted_answer is None:
        raise SystemExit("provide --draft-answer/--draft-file or --submitted-answer/--submitted-file")
    with connect() as conn:
        require_app(conn, args.id)
        conn.execute(
            """
            INSERT INTO form_answers(application_id, question, draft_answer, submitted_answer, submitted_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (args.id, args.question, draft_answer, submitted_answer, args.submitted_at),
        )
        touch(conn, args.id, args.next_action)
    print(f"stored form answer for {args.id}")


def attach_file(args: argparse.Namespace) -> None:
    init_db()
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        require_app(conn, args.id)
        conn.execute(
            """
            INSERT INTO application_files(application_id, kind, path, label, notes, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (args.id, args.kind, args.path, args.label, args.notes, now),
        )
        touch(conn, args.id, args.next_action)
    print(f"attached file reference for {args.id}: {args.path}")


def update_application(args: argparse.Namespace) -> None:
    init_db()
    updates = []
    values: list[object] = []
    for field in ["status", "priority", "next_action", "notes", "applied_at"]:
        value = getattr(args, field)
        if value is not None:
            updates.append(f"{field} = ?")
            values.append(value)
    updates.append("last_touch = ?")
    values.append(datetime.now().isoformat(timespec="seconds"))
    values.append(args.id)
    with connect() as conn:
        require_app(conn, args.id)
        conn.execute(f"UPDATE applications SET {', '.join(updates)} WHERE id = ?", values)
    print(f"updated {args.id}")


def add_text(args: argparse.Namespace) -> None:
    init_db()
    text = read_text_arg(args.text, args.file)
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as conn:
        require_app(conn, args.id)
        if args.kind == "evaluation":
            conn.execute(
                "INSERT INTO evaluations(application_id, verdict, fit_score, risk_score, effort_score, reasoning, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (args.id, args.verdict, args.fit_score, args.risk_score, args.effort_score, text, now),
            )
        elif args.kind == "cover-letter":
            conn.execute(
                "INSERT INTO cover_letters(application_id, draft_text, submitted_text, version, created_at) VALUES (?, ?, ?, ?, ?)",
                (args.id, text, args.submitted_text, args.version, now),
            )
        elif args.kind == "interview-guide":
            conn.execute(
                "INSERT INTO interview_guides(application_id, guide_text, created_at) VALUES (?, ?, ?)",
                (args.id, text, now),
            )
        touch(conn, args.id, args.next_action)
    print(f"stored {args.kind} for {args.id}")


def import_seed(args: argparse.Namespace) -> None:
    init_db()
    seed_path = Path(args.file).expanduser().resolve()
    data = json.loads(seed_path.read_text(encoding="utf-8"))
    now = datetime.now().isoformat(timespec="seconds")
    imported = 0
    with connect() as conn:
        for term in data.get("glossary", []):
            name = str(term.get("term", "")).strip()
            if not name:
                continue
            conn.execute(
                """
                INSERT INTO glossary_terms(term, category, short_definition, detail, interview_angle, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(term) DO UPDATE SET
                    category = excluded.category,
                    short_definition = excluded.short_definition,
                    detail = excluded.detail,
                    interview_angle = excluded.interview_angle,
                    updated_at = excluded.updated_at
                """,
                (
                    name,
                    term.get("category"),
                    term.get("short_definition"),
                    term.get("detail"),
                    term.get("interview_angle"),
                    now,
                ),
            )
        for app in data.get("applications", []):
            company = str(app.get("company", "")).strip()
            role = str(app.get("role", "")).strip()
            if not company or not role:
                raise ValueError(f"{seed_path}: every application needs company and role")
            app_id = str(app.get("id") or make_id(company, role)).strip()
            existing = conn.execute("SELECT created_at FROM applications WHERE id = ?", (app_id,)).fetchone()
            created_at = existing["created_at"] if existing else app.get("created_at") or now
            conn.execute(
                """
                INSERT INTO applications (
                    id, company, role, source, source_url, location, remote_mode,
                    status, priority, created_at, applied_at, last_touch, next_action, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    company = excluded.company,
                    role = excluded.role,
                    source = excluded.source,
                    source_url = excluded.source_url,
                    location = excluded.location,
                    remote_mode = excluded.remote_mode,
                    status = excluded.status,
                    priority = excluded.priority,
                    applied_at = excluded.applied_at,
                    last_touch = excluded.last_touch,
                    next_action = excluded.next_action,
                    notes = excluded.notes
                """,
                (
                    app_id,
                    company,
                    role,
                    app.get("source"),
                    app.get("source_url"),
                    app.get("location"),
                    app.get("remote_mode"),
                    app.get("status", "applied"),
                    app.get("priority", "medium"),
                    created_at,
                    app.get("applied_at"),
                    now,
                    app.get("next_action"),
                    app.get("notes"),
                ),
            )
            card = app.get("call_card") or {}
            conn.execute(
                """
                INSERT INTO call_cards (
                    application_id, call_signals, technical_reading, pitch, smart_question,
                    risk_to_avoid, prepare_first, prepare_later, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(application_id) DO UPDATE SET
                    call_signals = excluded.call_signals,
                    technical_reading = excluded.technical_reading,
                    pitch = excluded.pitch,
                    smart_question = excluded.smart_question,
                    risk_to_avoid = excluded.risk_to_avoid,
                    prepare_first = excluded.prepare_first,
                    prepare_later = excluded.prepare_later,
                    updated_at = excluded.updated_at
                """,
                (
                    app_id,
                    card.get("call_signals"),
                    card.get("technical_reading"),
                    card.get("pitch"),
                    card.get("smart_question"),
                    card.get("risk_to_avoid"),
                    card.get("prepare_first"),
                    card.get("prepare_later"),
                    now,
                ),
            )

            conn.execute("DELETE FROM application_keywords WHERE application_id = ?", (app_id,))
            for term in app.get("keywords", []):
                name = str(term).strip()
                if not name:
                    continue
                conn.execute(
                    """
                    INSERT INTO glossary_terms(term, category, short_definition, detail, interview_angle, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(term) DO NOTHING
                    """,
                    (name, "unclassified", "", "", "", now),
                )
                conn.execute(
                    "INSERT OR IGNORE INTO application_keywords(application_id, term, importance) VALUES (?, ?, ?)",
                    (app_id, name, "recognize"),
                )

            if "offer_text" in app or "offer_snapshots" in app:
                conn.execute("DELETE FROM offer_snapshots WHERE application_id = ?", (app_id,))
                snapshots = []
                if app.get("offer_text"):
                    snapshots.append({"raw_text": app.get("offer_text"), "cleaned_text": app.get("offer_cleaned_text")})
                snapshots.extend(listify(app.get("offer_snapshots")))
                for snapshot in snapshots:
                    raw_text = snapshot if isinstance(snapshot, str) else snapshot.get("raw_text") or snapshot.get("text")
                    if not raw_text:
                        continue
                    cleaned_text = None if isinstance(snapshot, str) else snapshot.get("cleaned_text")
                    captured_at = now if isinstance(snapshot, str) else snapshot.get("captured_at") or now
                    conn.execute(
                        "INSERT INTO offer_snapshots(application_id, raw_text, cleaned_text, captured_at) VALUES (?, ?, ?, ?)",
                        (app_id, raw_text, cleaned_text, captured_at),
                    )

            if "company_research" in app:
                conn.execute("DELETE FROM company_research WHERE application_id = ?", (app_id,))
                for research in listify(app.get("company_research")):
                    if not research:
                        continue
                    conn.execute(
                        """
                        INSERT INTO company_research(application_id, company, summary, business_model, red_flags, sources_json, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            app_id,
                            research.get("company", company),
                            research.get("summary"),
                            research.get("business_model"),
                            research.get("red_flags"),
                            research.get("sources_json") or json.dumps(research.get("sources", []), ensure_ascii=False),
                            research.get("updated_at") or now,
                        ),
                    )

            if "evaluations" in app:
                conn.execute("DELETE FROM evaluations WHERE application_id = ?", (app_id,))
                for evaluation in listify(app.get("evaluations")):
                    if not evaluation:
                        continue
                    conn.execute(
                        "INSERT INTO evaluations(application_id, verdict, fit_score, risk_score, effort_score, reasoning, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (
                            app_id,
                            evaluation.get("verdict"),
                            evaluation.get("fit_score"),
                            evaluation.get("risk_score"),
                            evaluation.get("effort_score"),
                            evaluation.get("reasoning"),
                            evaluation.get("created_at") or now,
                        ),
                    )

            if "form_answers" in app:
                conn.execute("DELETE FROM form_answers WHERE application_id = ?", (app_id,))
                for answer in listify(app.get("form_answers")):
                    if not answer or not answer.get("question"):
                        continue
                    conn.execute(
                        "INSERT INTO form_answers(application_id, question, draft_answer, submitted_answer, submitted_at) VALUES (?, ?, ?, ?, ?)",
                        (
                            app_id,
                            answer.get("question"),
                            answer.get("draft_answer"),
                            answer.get("submitted_answer"),
                            answer.get("submitted_at"),
                        ),
                    )

            if "cover_letters" in app:
                conn.execute("DELETE FROM cover_letters WHERE application_id = ?", (app_id,))
                for letter in listify(app.get("cover_letters")):
                    if not letter:
                        continue
                    if isinstance(letter, str):
                        draft_text = letter
                        submitted_text = None
                        version = None
                        created = now
                    else:
                        draft_text = letter.get("draft_text") or letter.get("text")
                        submitted_text = letter.get("submitted_text")
                        version = letter.get("version")
                        created = letter.get("created_at") or now
                    if not draft_text and not submitted_text:
                        continue
                    conn.execute(
                        "INSERT INTO cover_letters(application_id, draft_text, submitted_text, version, created_at) VALUES (?, ?, ?, ?, ?)",
                        (app_id, draft_text, submitted_text, version, created),
                    )

            if "interview_guides" in app:
                conn.execute("DELETE FROM interview_guides WHERE application_id = ?", (app_id,))
                for guide in listify(app.get("interview_guides")):
                    text = guide if isinstance(guide, str) else guide.get("guide_text") or guide.get("text")
                    if not text:
                        continue
                    created = now if isinstance(guide, str) else guide.get("created_at") or now
                    conn.execute(
                        "INSERT INTO interview_guides(application_id, guide_text, created_at) VALUES (?, ?, ?)",
                        (app_id, text, created),
                    )

            if "generated_files" in app or "files" in app:
                conn.execute("DELETE FROM application_files WHERE application_id = ?", (app_id,))
                for file_item in listify(app.get("generated_files")) + listify(app.get("files")):
                    if not file_item:
                        continue
                    if isinstance(file_item, str):
                        kind = "generated"
                        path = file_item
                        label = None
                        notes = None
                        created = now
                    else:
                        kind = file_item.get("kind", "generated")
                        path = file_item.get("path")
                        label = file_item.get("label")
                        notes = file_item.get("notes")
                        created = file_item.get("created_at") or now
                    if not path:
                        continue
                    conn.execute(
                        "INSERT INTO application_files(application_id, kind, path, label, notes, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                        (app_id, kind, path, label, notes, created),
                    )

            imported += 1
    print(f"imported {imported} applications from {seed_path}")


def require_app(conn: sqlite3.Connection, app_id: str) -> sqlite3.Row:
    row = conn.execute("SELECT * FROM applications WHERE id = ?", (app_id,)).fetchone()
    if row is None:
        raise SystemExit(f"unknown application: {app_id}")
    return row


def touch(conn: sqlite3.Connection, app_id: str, next_action: str | None = None) -> None:
    if next_action is None:
        conn.execute("UPDATE applications SET last_touch = ? WHERE id = ?", (datetime.now().isoformat(timespec="seconds"), app_id))
    else:
        conn.execute(
            "UPDATE applications SET last_touch = ?, next_action = ? WHERE id = ?",
            (datetime.now().isoformat(timespec="seconds"), next_action, app_id),
        )


def list_applications(args: argparse.Namespace) -> None:
    init_db()
    query = "SELECT * FROM applications"
    values: list[object] = []
    clauses = []
    if args.status:
        clauses.append("status = ?")
        values.append(args.status)
    if args.search:
        clauses.append("(company LIKE ? OR role LIKE ? OR notes LIKE ?)")
        pattern = f"%{args.search}%"
        values.extend([pattern, pattern, pattern])
    if clauses:
        query += " WHERE " + " AND ".join(clauses)
    query += " ORDER BY created_at DESC"
    with connect() as conn:
        rows = conn.execute(query, values).fetchall()
    for row in rows:
        print(f"{row['status']:14} {row['priority']:7} {row['id']} :: {row['company']} — {row['role']}")


def latest_by_id(rows: list[sqlite3.Row], key: str) -> dict[str, dict]:
    return {row[key]: dict(row) for row in rows}


def rows_by_id(rows: list[sqlite3.Row], key: str) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for row in rows:
        grouped.setdefault(row[key], []).append(dict(row))
    return grouped


def application_payload() -> dict:
    init_db()
    with connect() as conn:
        applications = [dict(row) for row in conn.execute("SELECT * FROM applications ORDER BY created_at DESC")]
        counts = {
            row["status"]: row["total"]
            for row in conn.execute("SELECT status, COUNT(*) AS total FROM applications GROUP BY status")
        }
        latest_text = {}
        for table, key, field in [
            ("evaluations", "evaluation", "reasoning"),
            ("cover_letters", "cover_letter", "draft_text"),
            ("interview_guides", "interview_guide", "guide_text"),
        ]:
            rows = conn.execute(
                f"SELECT application_id, {field} AS value, MAX(id) AS latest_id FROM {table} GROUP BY application_id"
            ).fetchall()
            for row in rows:
                latest_text.setdefault(row["application_id"], {})[key] = row["value"]

        call_cards = {
            row["application_id"]: dict(row)
            for row in conn.execute("SELECT * FROM call_cards")
        }
        keywords: dict[str, list[str]] = {}
        for row in conn.execute("SELECT application_id, term FROM application_keywords ORDER BY term COLLATE NOCASE"):
            keywords.setdefault(row["application_id"], []).append(row["term"])
        glossary = {
            row["term"]: dict(row)
            for row in conn.execute("SELECT * FROM glossary_terms ORDER BY term COLLATE NOCASE")
        }
        offers = latest_by_id(
            conn.execute(
                "SELECT * FROM offer_snapshots WHERE id IN (SELECT MAX(id) FROM offer_snapshots GROUP BY application_id)"
            ).fetchall(),
            "application_id",
        )
        research = latest_by_id(
            conn.execute(
                "SELECT * FROM company_research WHERE id IN (SELECT MAX(id) FROM company_research GROUP BY application_id)"
            ).fetchall(),
            "application_id",
        )
        form_answers = rows_by_id(
            conn.execute("SELECT * FROM form_answers ORDER BY id").fetchall(),
            "application_id",
        )
        files = rows_by_id(
            conn.execute("SELECT * FROM application_files ORDER BY created_at DESC, id DESC").fetchall(),
            "application_id",
        )

    for item in applications:
        app_id = item["id"]
        item["texts"] = latest_text.get(app_id, {})
        item["call_card"] = call_cards.get(app_id, {})
        item["keywords"] = keywords.get(app_id, [])
        item["offer"] = offers.get(app_id)
        item["research"] = research.get(app_id)
        item["form_answers"] = form_answers.get(app_id, [])
        item["files"] = files.get(app_id, [])
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "statuses": STATUSES,
        "counts": counts,
        "applications": applications,
        "glossary": glossary,
    }


def dashboard_html(payload: dict) -> str:
    data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    timestamp = html.escape(payload["generated_at"])
    template = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Application Tracker</title>
  <style>
    :root { font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #111827; background: #f8fafc; }
    body { margin: 0; }
    header { padding: 1.2rem 1.4rem; background: #111827; color: white; }
    main { padding: 1rem; display: grid; gap: 1rem; grid-template-columns: minmax(0, 1.6fr) minmax(320px, .9fr); align-items: start; }
    .toolbar { display: flex; gap: .75rem; flex-wrap: wrap; align-items: center; grid-column: 1 / -1; }
    input, select { padding: .55rem .65rem; border: 1px solid #cbd5e1; border-radius: .55rem; background: white; }
    .board { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: .85rem; }
    .column { background: #e5e7eb; border-radius: .85rem; padding: .7rem; min-height: 10rem; }
    .column h2 { font-size: .86rem; text-transform: uppercase; letter-spacing: .08em; color: #334155; margin: .2rem .15rem .65rem; }
    .card { background: white; border: 1px solid #dbe3ef; border-radius: .75rem; padding: .75rem; margin-bottom: .65rem; box-shadow: 0 1px 2px rgba(15, 23, 42, .06); cursor: pointer; }
    .card h3 { margin: 0 0 .25rem; font-size: .95rem; }
    .meta { color: #64748b; font-size: .82rem; }
    .side { display: grid; gap: 1rem; position: sticky; top: 1rem; }
    .detail, .glossary { background: white; border: 1px solid #dbe3ef; border-radius: .85rem; padding: 1rem; }
    .detail h2, .glossary h2 { margin-top: 0; }
    .field { margin: .75rem 0; }
    .field strong { display: block; color: #334155; font-size: .78rem; text-transform: uppercase; letter-spacing: .06em; margin-bottom: .2rem; }
    .keywords { display: flex; gap: .35rem; flex-wrap: wrap; margin-top: .5rem; }
    .keyword { border: 1px solid #cbd5e1; border-radius: 999px; background: #f8fafc; padding: .28rem .52rem; font-size: .78rem; cursor: pointer; }
    .keyword:hover { background: #e2e8f0; }
    pre { white-space: pre-wrap; background: #f1f5f9; padding: .8rem; border-radius: .65rem; overflow: auto; max-height: 28rem; }
    .empty { color: #64748b; font-style: italic; }
    .rows { display: grid; gap: .55rem; }
    .row { border: 1px solid #e2e8f0; border-radius: .6rem; padding: .55rem; background: #f8fafc; }
    @media (max-width: 950px) { main { grid-template-columns: 1fr; } .side { position: static; } }
  </style>
</head>
<body>
<header>
  <h1>Application Tracker</h1>
  <div>Generated __GENERATED_AT__</div>
</header>
<main>
  <section class="toolbar">
    <input id="search" type="search" placeholder="Search company, role, notes, keywords, offer text">
    <select id="status"><option value="">All statuses</option></select>
  </section>
  <section id="board" class="board"></section>
  <aside class="side">
    <section id="detail" class="detail"><p class="empty">Select an application.</p></section>
    <section id="glossary" class="glossary"><p class="empty">Click a keyword to load its definition.</p></section>
  </aside>
</main>
<script type="application/json" id="payload">__PAYLOAD__</script>
<script>
const payload = JSON.parse(document.getElementById('payload').textContent);
const board = document.getElementById('board');
const detail = document.getElementById('detail');
const glossary = document.getElementById('glossary');
const search = document.getElementById('search');
const statusFilter = document.getElementById('status');

for (const status of payload.statuses) {
  const option = document.createElement('option');
  option.value = status;
  option.textContent = `${status} (${payload.counts[status] || 0})`;
  statusFilter.appendChild(option);
}

function matches(app) {
  const needle = search.value.trim().toLowerCase();
  if (statusFilter.value && app.status !== statusFilter.value) return false;
  if (!needle) return true;
  const card = app.call_card || {};
  const offer = app.offer || {};
  const research = app.research || {};
  const haystack = [
    app.company, app.role, app.notes, app.next_action,
    card.call_signals, card.technical_reading, card.pitch,
    offer.raw_text, offer.cleaned_text,
    research.summary, research.business_model, research.red_flags,
    ...(app.keywords || [])
  ];
  return haystack.some(value => String(value || '').toLowerCase().includes(needle));
}

function renderBoard() {
  board.textContent = '';
  const visible = payload.applications.filter(matches);
  for (const status of payload.statuses) {
    const column = document.createElement('section');
    column.className = 'column';
    const title = document.createElement('h2');
    title.textContent = status;
    column.appendChild(title);
    for (const app of visible.filter(item => item.status === status)) {
      const card = document.createElement('article');
      card.className = 'card';
      card.innerHTML = `<h3>${escapeHtml(app.company)} — ${escapeHtml(app.role)}</h3>
        <div class="meta">${escapeHtml(app.priority)} · ${escapeHtml(app.last_touch || '')}</div>
        <div class="meta">${escapeHtml(app.next_action || 'No next action')}</div>
        ${keywordButtons(app.keywords || [], 5)}`;
      card.addEventListener('click', event => {
        if (!event.target.closest('[data-term]')) renderDetail(app);
      });
      wireKeywordButtons(card);
      column.appendChild(card);
    }
    board.appendChild(column);
  }
}

function renderDetail(app) {
  const texts = app.texts || {};
  const card = app.call_card || {};
  const offer = app.offer || {};
  const research = app.research || {};
  detail.innerHTML = `<h2>${escapeHtml(app.company)} — ${escapeHtml(app.role)}</h2>
    <p><strong>Status:</strong> ${escapeHtml(app.status)} · <strong>Priority:</strong> ${escapeHtml(app.priority)}</p>
    <p><strong>Source:</strong> ${escapeHtml(app.source || '')} ${app.source_url ? `<a href="${escapeAttr(app.source_url)}" target="_blank" rel="noreferrer">open</a>` : ''}</p>
    <p><strong>Location:</strong> ${escapeHtml(app.location || '')} · <strong>Remote:</strong> ${escapeHtml(app.remote_mode || '')}</p>
    <p><strong>Next action:</strong> ${escapeHtml(app.next_action || '')}</p>
    <p><strong>Notes:</strong> ${escapeHtml(app.notes || '')}</p>
    ${keywordButtons(app.keywords || [], 80)}
    ${callField('Call signals', card.call_signals)}
    ${callField('Technical reading', card.technical_reading)}
    ${callField('Pitch', card.pitch)}
    ${callField('Smart question', card.smart_question)}
    ${callField('Risk to avoid', card.risk_to_avoid)}
    ${callField('Prepare first', card.prepare_first)}
    ${callField('Prepare later', card.prepare_later)}
    <h3>Literal offer snapshot</h3><pre>${escapeHtml(offer.raw_text || 'No offer text stored yet.')}</pre>
    <h3>Company research</h3>
    ${callField('Summary', research.summary)}
    ${callField('Business model', research.business_model)}
    ${callField('Red flags', research.red_flags)}
    ${callField('Sources JSON', research.sources_json)}
    <h3>Form answers</h3>${renderFormAnswers(app.form_answers || [])}
    <h3>Generated/private files</h3>${renderFiles(app.files || [])}
    <h3>Evaluation</h3><pre>${escapeHtml(texts.evaluation || 'No evaluation stored.')}</pre>
    <h3>Cover letter</h3><pre>${escapeHtml(texts.cover_letter || 'No cover letter stored.')}</pre>
    <h3>Interview guide</h3><pre>${escapeHtml(texts.interview_guide || 'No interview guide stored.')}</pre>`;
  wireKeywordButtons(detail);
}

function callField(label, value) {
  if (!value) return '';
  return `<div class="field"><strong>${escapeHtml(label)}</strong><div>${escapeHtml(value)}</div></div>`;
}

function renderFormAnswers(items) {
  if (!items.length) return '<p class="empty">No form answers stored.</p>';
  return `<div class="rows">${items.map(item => `<div class="row"><strong>${escapeHtml(item.question)}</strong><pre>${escapeHtml(item.submitted_answer || item.draft_answer || '')}</pre></div>`).join('')}</div>`;
}

function renderFiles(items) {
  if (!items.length) return '<p class="empty">No file references stored.</p>';
  return `<div class="rows">${items.map(item => `<div class="row"><strong>${escapeHtml(item.kind)}</strong><div>${escapeHtml(item.label || '')}</div><code>${escapeHtml(item.path)}</code>${item.notes ? `<p>${escapeHtml(item.notes)}</p>` : ''}</div>`).join('')}</div>`;
}

function keywordButtons(terms, limit) {
  if (!terms.length) return '';
  return `<div class="keywords">${terms.slice(0, limit).map(term => `<button class="keyword" type="button" data-term="${escapeAttr(term)}">${escapeHtml(term)}</button>`).join('')}</div>`;
}

function wireKeywordButtons(root) {
  for (const button of root.querySelectorAll('[data-term]')) {
    button.addEventListener('click', event => {
      event.stopPropagation();
      renderGlossary(button.dataset.term);
    });
  }
}

function renderGlossary(term) {
  const item = payload.glossary[term];
  if (!item) {
    glossary.innerHTML = `<h2>${escapeHtml(term)}</h2><p class="empty">No definition stored for this term yet.</p>`;
    return;
  }
  glossary.innerHTML = `<h2>${escapeHtml(term)}</h2>
    ${callField('Category', item.category)}
    ${callField('Meaning', item.short_definition)}
    ${callField('Detail', item.detail)}
    ${callField('Interview angle', item.interview_angle)}`;
}

function escapeHtml(value) {
  return String(value ?? '').replace(/[&<>"]/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch]));
}
function escapeAttr(value) { return escapeHtml(value).replace(/'/g, '&#39;'); }

search.addEventListener('input', renderBoard);
statusFilter.addEventListener('change', renderBoard);
renderBoard();
</script>
</body>
</html>
"""
    return template.replace("__GENERATED_AT__", timestamp).replace("__PAYLOAD__", data)


def export_dashboard(args: argparse.Namespace) -> None:
    payload = application_payload()
    output = Path(args.output).expanduser() if args.output else private_home() / "dashboard.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(dashboard_html(payload), encoding="utf-8", newline="\n")
    print(output)


class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path not in {"/", "/dashboard.html"}:
            self.send_error(404)
            return
        content = dashboard_html(application_payload()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format: str, *args: object) -> None:
        return


def serve_dashboard(args: argparse.Namespace) -> None:
    init_db()
    server = ThreadingHTTPServer((args.host, args.port), DashboardHandler)
    print(f"serving http://{args.host}:{args.port}")
    server.serve_forever()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.set_defaults(func=lambda args: init_db())

    new = sub.add_parser("new")
    new.add_argument("--id")
    new.add_argument("--company", required=True)
    new.add_argument("--role", required=True)
    new.add_argument("--source")
    new.add_argument("--source-url")
    new.add_argument("--location")
    new.add_argument("--remote-mode")
    new.add_argument("--status", choices=STATUSES, default="found")
    new.add_argument("--priority", default="medium")
    new.add_argument("--next-action")
    new.add_argument("--notes")
    new.set_defaults(func=create_application)

    offer = sub.add_parser("ingest-offer")
    offer.add_argument("--id", required=True)
    offer.add_argument("--text")
    offer.add_argument("--file")
    offer.add_argument("--cleaned-text")
    offer.add_argument("--next-action")
    offer.set_defaults(func=ingest_offer)

    set_offer = sub.add_parser("set-offer")
    set_offer.add_argument("--id", required=True)
    set_offer.add_argument("--text")
    set_offer.add_argument("--file")
    set_offer.add_argument("--cleaned-text")
    set_offer.add_argument("--next-action")
    set_offer.set_defaults(func=ingest_offer)

    research = sub.add_parser("set-research")
    research.add_argument("--id", required=True)
    research.add_argument("--company")
    research.add_argument("--summary")
    research.add_argument("--summary-file")
    research.add_argument("--business-model")
    research.add_argument("--business-model-file")
    research.add_argument("--red-flags")
    research.add_argument("--red-flags-file")
    research.add_argument("--sources-json")
    research.add_argument("--next-action")
    research.set_defaults(func=set_research)

    form = sub.add_parser("add-form-answer")
    form.add_argument("--id", required=True)
    form.add_argument("--question", required=True)
    form.add_argument("--draft-answer")
    form.add_argument("--draft-file")
    form.add_argument("--submitted-answer")
    form.add_argument("--submitted-file")
    form.add_argument("--submitted-at")
    form.add_argument("--next-action")
    form.set_defaults(func=add_form_answer)

    file_ref = sub.add_parser("attach-file")
    file_ref.add_argument("--id", required=True)
    file_ref.add_argument("--kind", required=True)
    file_ref.add_argument("--path", required=True)
    file_ref.add_argument("--label")
    file_ref.add_argument("--notes")
    file_ref.add_argument("--next-action")
    file_ref.set_defaults(func=attach_file)

    update = sub.add_parser("update")
    update.add_argument("--id", required=True)
    update.add_argument("--status", choices=STATUSES)
    update.add_argument("--priority")
    update.add_argument("--next-action")
    update.add_argument("--notes")
    update.add_argument("--applied-at")
    update.set_defaults(func=update_application)

    add = sub.add_parser("add-text")
    add.add_argument("--id", required=True)
    add.add_argument("--kind", choices=["evaluation", "cover-letter", "interview-guide"], required=True)
    add.add_argument("--text")
    add.add_argument("--file")
    add.add_argument("--verdict")
    add.add_argument("--fit-score", type=int)
    add.add_argument("--risk-score", type=int)
    add.add_argument("--effort-score", type=int)
    add.add_argument("--submitted-text")
    add.add_argument("--version")
    add.add_argument("--next-action")
    add.set_defaults(func=add_text)

    seed = sub.add_parser("import-seed")
    seed.add_argument("--file", required=True, help="Local JSON seed with applications and glossary terms")
    seed.set_defaults(func=import_seed)

    listing = sub.add_parser("list")
    listing.add_argument("--status", choices=STATUSES)
    listing.add_argument("--search")
    listing.set_defaults(func=list_applications)

    export = sub.add_parser("export-dashboard")
    export.add_argument("--output")
    export.set_defaults(func=export_dashboard)

    dashboard = sub.add_parser("dashboard")
    dashboard.add_argument("--host", default="127.0.0.1")
    dashboard.add_argument("--port", type=int, default=8765)
    dashboard.set_defaults(func=serve_dashboard)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

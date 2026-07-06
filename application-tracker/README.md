# Application Tracker

Local application tracking tools for Agentic Career Boost.

Runtime records are stored under `application-tracker/.private/` by default, or in the path set with `ACB_APPLICATION_TRACKER_HOME`.

## No-CLI launch

On Windows, open the tracker by double-clicking one of these files:

```text
application-tracker/Open Application Tracker.cmd
application-tracker/Open Application Tracker Read Only.cmd
```

The first launcher opens the full local tracker with Raw intake enabled. The second launcher opens the same tracker dashboard in read-only mode, with Raw intake/write controls removed.

Both launchers start the local server and open the browser automatically.

## CLI commands

```bash
python application-tracker/acb_tracker.py init
python application-tracker/acb_tracker.py new --company "Example" --role "AI Automation Specialist"
python application-tracker/acb_tracker.py raw-intake --company "Example" --role "AI Automation Specialist" --kind offer --file path/to/original-offer.txt
python application-tracker/acb_tracker.py set-offer --id 2026-07-06-example-ai-automation-specialist --file path/to/original-offer.txt
python application-tracker/acb_tracker.py set-research --id 2026-07-06-example-ai-automation-specialist --summary-file path/to/company-summary.txt
python application-tracker/acb_tracker.py add-form-answer --id 2026-07-06-example-ai-automation-specialist --question "Why this role?" --draft-file path/to/answer.txt
python application-tracker/acb_tracker.py attach-file --id 2026-07-06-example-ai-automation-specialist --kind cover-letter-pdf --path application-tracker/.private/generated/example-cover-letter.pdf
python application-tracker/acb_tracker.py import-seed --file path/to/local-seed.json
python application-tracker/acb_tracker.py list
python application-tracker/acb_tracker.py export-dashboard
python application-tracker/acb_tracker.py dashboard
python application-tracker/render_letter.py --input path/to/local-letter.json
```

`import-seed` is intended for local/private migration files. Do not commit real application data or generated SQLite files. The dashboard loads application call cards, literal offer snapshots, raw intake records, company research, form answers, private/generated file references, and keyword definitions from the local database. Clicking a keyword chip opens its definition panel during recruiter calls.

The tracker supports partial-first records: create the application with company and role, paste raw owned data through the local dashboard form or `raw-intake`, then let an agent complete company research, call cards, form answers, cover letters, interview guides, and file references in later passes.

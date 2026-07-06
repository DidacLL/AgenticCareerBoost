# Application Tracker

Local application tracking tools for Agentic Career Boost.

Runtime records are stored under `application-tracker/.private/` by default, or in the path set with `ACB_APPLICATION_TRACKER_HOME`.

Basic commands:

```bash
python application-tracker/acb_tracker.py init
python application-tracker/acb_tracker.py new --company "Example" --role "AI Automation Specialist"
python application-tracker/acb_tracker.py import-seed --file path/to/local-seed.json
python application-tracker/acb_tracker.py list
python application-tracker/acb_tracker.py export-dashboard
python application-tracker/acb_tracker.py dashboard
python application-tracker/render_letter.py --input path/to/local-letter.json
```

`import-seed` is intended for local/private migration files. Do not commit real application data or generated SQLite files. The dashboard loads application call cards and keyword definitions from the local database; clicking a keyword chip opens its definition panel during recruiter calls.

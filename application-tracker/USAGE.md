# Application Tracker usage guide

This tracker is for private job-application work. Use it locally for real data. Do not commit real applications, offers, recruiter messages, form answers, cover letters, generated PDFs, or SQLite files.

## One tracker surface

There should not be a separate fake Application Tracker applet. The tracker dashboard is the same human-facing surface in both local modes:

- full local mode: the tracker serves the dashboard, writes real data to `.private`, and shows Raw intake;
- read-only local mode: the tracker serves the same dashboard from the same local data, but removes Raw intake and write controls.

The public website can document this workflow inside the AgenticCareerBoost project page, but it cannot read your local private tracker store.

## No-CLI local launch

On Windows, double-click one of these files:

```text
application-tracker/Open Application Tracker.cmd
application-tracker/Open Application Tracker Read Only.cmd
```

The first launcher opens the full local tracker with Raw intake enabled. The second launcher opens the same tracker dashboard in read-only mode. Both start the local server and open the browser automatically.

## Local private mode

Use this mode for real applications. The dashboard runs from your machine and writes to:

```text
application-tracker/.private/applications.sqlite
```

or to the folder configured with:

```bash
ACB_APPLICATION_TRACKER_HOME=/path/to/private/tracker-home
```

The full local dashboard includes a Raw intake form. That form posts to the local `/raw-intake` route and writes into the private SQLite database.

## Public/deployed site mode

The deployed site does not run the tracker and does not load fake applications. It exposes an Application Tracker section inside the AgenticCareerBoost project page that explains the local launch flow and privacy boundary.

The public site must not pretend to be connected to your private tracker. It must not expose Raw intake, save, upload, or private-data capture controls.

## Fast capture workflow

Use the Raw intake form in the full local dashboard when you have incomplete information.

Examples:

- You only remember company and role.
- You have the literal offer text but not the analysis yet.
- You have a recruiter email or LinkedIn message.
- You have a form question you need to answer later.
- You have a generated cover letter, PDF, or local file path.

The Raw intake form saves the data as `needs_agent`. If the item is a literal job offer and company/role are provided, the tracker also creates or updates the application and stores the offer snapshot.

## Agent enrichment workflow

1. Open the full local tracker.
2. Paste raw owned data into the Raw intake form.
3. Keep source URLs and notes when available.
4. Ask an agent to inspect the local tracker state and complete missing fields.

The agent should use the raw intake records as evidence and fill only derived tracker fields:

- application status and next action
- call signals
- technical reading
- company research
- evaluation
- form answers
- cover letter draft
- interview guide
- keywords and glossary terms
- generated/private file references

The agent must not assume missing details when the raw text is insufficient. It should leave those cells empty or mark them for manual follow-up.

## Minimal manual capture

From the full local dashboard, paste:

```text
Company: recruiter or company name
Role: approximate role title
Kind: Literal job offer / recruiter email / form question / note
Raw text: the text you own or received
Notes: what the agent should infer later
```

The same can be done from CLI when needed:

```bash
python application-tracker/acb_tracker.py raw-intake \
  --company "Example" \
  --role "AI Automation Specialist" \
  --kind offer \
  --file path/to/original-offer.txt \
  --notes "Infer missing tracker cells from this offer."
```

## What belongs in the tracker

Store real private content locally:

- literal offer text
- recruiter emails or messages
- company analysis
- evaluations
- draft and submitted form answers
- cover-letter text
- interview guides
- local paths to generated files

Keep generated binary/source files under `.private/generated/` or another private folder. Store paths in the tracker, not public artifacts in the repository.

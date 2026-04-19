# Workflow: Chat

## Trigger

User initiates a discussion about the project.

## Inputs

- `docs/core/*` — mission, brand, constraints (read-only)
- `state/current.md` — current status for context

## Steps

1. Load stable truth from `docs/core/*` and current state.
2. Discuss the topic within project constraints.
3. At session end, produce a concise summary.
4. Optionally write the summary to
   `state/summaries/YYYY-MM-DD-chat-<slug>.md`.

## Outputs

- Conversation responses respecting project tone and constraints
- Optional: session summary file in `state/summaries/`

## Exit criteria

- The user's question is answered or the discussion reaches closure.
- A concise summary is offered.
- **No file edits** occurred except the optional summary.
- Chat never silently promotes itself to a sprint.

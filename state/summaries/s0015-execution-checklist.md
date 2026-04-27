# S-001.5 Execution Checklist

- **Sprint**: S-001.5
- **Date**: 2026-04-27
- **Purpose**: Human-applied public profile cleanup sequence before the UOC fair

## Local Repo Changes

- [x] S-001 local artifacts preserved.
- [x] S-001.5 target shortlist created.
- [x] GitHub cleanup package created.
- [x] LinkedIn/JobTeaser profile kit created.
- [x] Outreach kit created.
- [x] Recruiter landing page rebuilt as static HTML.
- [x] Formal curriculum page added.
- [x] Downloadable CV PDF added.
- [x] State files updated to record S-001.5 closure.

## Deploy Site

Uses a static `gh-pages` branch to avoid the failing `actions/configure-pages` path.

1. Review local changes.
2. Commit and push S-001 and S-001.5 artifacts. **Done**: `a1db91d`, `8642f6d`, `10bb463`, `e812508`.
3. Push `site/public/**` so `.github/workflows/site-build.yml` publishes the static site to `gh-pages`. **Done**: `f601700`; workflow green.
4. Set repository Settings → Pages → Build and deployment → Source: Deploy from branch → Branch: `gh-pages` / root.
5. After GitHub finishes publishing, open `https://didacll.github.io/AgenticCareerBoost/`.
6. Confirm introduction, projects, curriculum, contact links, and CV PDF link.

## Apply On GitHub Profile

Requires user-controlled account action.

1. Clear GitHub status `Out sick`.
2. Update profile bio, website, company, location, LinkedIn social link, and hireable flag.
3. Replace `DidacLL/DidacLL` README with the S-001.5 profile README.
4. Update descriptions/topics for AgenticCareerBoost, P3CTeX, p3cTeX-UMLST, IronBank, and DidacLL.
5. Pin repos in order: AgenticCareerBoost, P3CTeX, IronBank, p3cTeX-UMLST.
6. Archive low-signal repos only after confirming each archive dialog.
7. Do not delete repositories.

## Apply On LinkedIn

Requires user-controlled account action.

1. Replace headline with the S-001.5 headline.
2. Replace About section with the S-001.5 About text.
3. Add Featured links: AgenticCareerBoost, recruiter landing page, P3CTeX, and optionally the Agentic System Guide PDF.
4. Add/update Independent Projects & Research experience entry.
5. Reorder skills with Python, Machine Learning, and Java near the top.
6. Do not publish posts until the linked public artifacts are live.

## Apply On JobTeaser / UOC Career Center

Requires user-controlled account action.

1. Update personal summary using the JobTeaser kit.
2. Add GitHub, LinkedIn, and recruiter landing page links.
3. Upload/update CV only after user review.
4. Prioritize Tier A and Tier B companies from the target shortlist.
5. Request interviews selectively, using the outreach kit.

## External Actions Needing Confirmation

- If GitHub does not auto-publish `gh-pages`, enable Pages with Source `Deploy from branch`, Branch `gh-pages`, Folder `/`.
- GitHub profile/settings save.
- GitHub repository metadata changes.
- GitHub repository archive confirmations.
- LinkedIn profile edits and post publication.
- JobTeaser profile edits.
- Sending messages, interview requests, applications, or CV uploads.

## Fair-Day Operating Loop

1. Open target shortlist.
2. For each company, classify: apply now, request interview, save for later, reject/deprioritize.
3. Use the shortest relevant pitch.
4. Record each contact and next step in a new fair log if the sprint continues.
5. Avoid volume applications to generic consulting roles.

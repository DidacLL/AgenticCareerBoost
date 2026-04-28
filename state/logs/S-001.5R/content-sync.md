# ContentSync Audit — S-001.5R

## Scope

System-review audit of S-001.5 drift before S-002.

## Findings

| Finding | Fix applied or status |
|---|---|
| Direct `main` commits bypassed PR gates. | Added aggregate `required-ci`; recorded required remote ruleset/Page settings in `ci-pages-governance.md`. |
| Site source existed in `site/starter/`, `site/public/`, and `content/site/`. | Promoted `site/` as canonical Jekyll source; removed tracked duplicate source/rendered files. |
| Report PDFs and auxiliary files were tracked inside `content/reports/tex/`. | Removed tracked generated artifacts from source folders; kept public PDFs in `content/reports/build/`. |
| Root `.gitignore` ignored dotted names such as `s001.5`. | Replaced broad LaTeX template with scoped repo rules and narrow TeX-local ignores. |
| Sprint closure forced social output even for internal/system work. | Updated marketing and sprint contracts to use a public-narrative decision. |
| Social campaign sequence followed sprint numbering. | Updated `content/social/plan.md` to follow evidence availability. |
| Public copy contained TODO/user-instruction risks and unsupported fintech/regtech emphasis. | CommunityManager cleaned owned drafts and softened regulated-domain claims. |
| `scripts/validate-links.sh` failed in local Bash due CRLF. | Added `.gitattributes` and normalized the script to LF. |

## Accepted Historical Notes

- Older S-000/S-001.5 logs still mention `site/starter`, `site/public`, and
  `gh-pages` because they document the state at that time.
- S-001.5R report explains those paths as historical flaws rather than current
  canonical structure.

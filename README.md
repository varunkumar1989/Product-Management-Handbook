# Product Management Master Handbook

A visual, interactive Product Management study system built from your 55-lecture course study guide (`Expanded_PM_AI_and_Tools_Study_Guide.pdf`, which fully contains the Visual edition) and extended to the 12 Product Core modules.

## Open it
- **Live (public, anyone with the link):** https://pm-master-handbook-varun.netlify.app — Netlify project `pm-master-handbook-varun`. To publish changes: rebuild, then run `netlify deploy --prod --dir html/Interactive-PM-Handbook --site pm-master-handbook-varun --no-build`.
- **Interactive site:** `html/Interactive-PM-Handbook/index.html` — works offline straight from disk (no server, no API keys).
- **Entry point listing everything:** `index.html` in this folder.
- **All links in one file:** [`LINKS.md`](./LINKS.md): live pages and PDFs for every module, plus the resume and case-study portfolio.
- **PDFs:** `pdf/` — the complete handbook (444 pages, page-numbered contents, 527 bookmarks), 12 module PDFs, and separate PDFs for the Framework Library, Case Studies, Practical Projects and Interview Handbook.

## What's inside
| Part | Contents |
|---|---|
| 12 modules | Fundamentals · Strategy · Discovery · Prioritisation · UX · Communication · Analytics · Growth · Tech & System Design · LLMs/RAG · Vibe Coding · Agentic AI |
| Framework Library | 29 frameworks + a "which framework should I use?" selection guide |
| Case Study Library | 12 cases (food delivery, ride-hailing, e-commerce, streaming, music, messaging, collaboration, card onboarding, payments, learning, PLG, AI finance assistant) |
| Practical Projects | 5 end-to-end portfolio projects with datasets and model solutions |
| Interview Handbook | 106 questions in 13 categories, scorecard and practice worksheet |
| Templates | 10 reusable templates (PRD, one-pager, experiment plan/readout, launch checklist, stakeholder map/DACI, research kit, RICE/WSJF/roadmap, metrics/OKR/KPI tree, AI PRD/eval, decision log/retro) + the Module 11 starter app |
| Datasets | 11 synthetic CSVs (see `datasets/README.md`) |
| Glossary | 175 searchable terms |

## Honesty rules used throughout
- **"From your course notes"** boxes preserve your study guide's content, including its own corrections of inaccurate lecture statements.
- **"Hypothetical"** boxes and labels mark invented numbers. No real company results are claimed; company names are used only as widely known illustrations.
- Lectures 44 and 54 had no recordings and are not summarised.
- The curriculum screenshot was not received; module titles come from your brief and are **provisional**.

## Rebuild after editing
Edit Markdown in `content/`, then from this folder:

```bash
python -I _build/build.py
```

```bash
python -I -X utf8 _build/pdf.py
```

```bash
python -I -X utf8 _build/validate.py
```

See `PROGRESS.md` for architecture, status and known gaps; `validation-reports/` for test results; `source-coverage-matrix.md` and `curriculum-gap-analysis.md` for source traceability.

## Folder map
```
content/            Markdown sources (modules, frameworks, cases, projects, interview, pages, glossary)
html/Interactive-PM-Handbook/   generated website (self-contained, incl. pdf/ and downloads/)
pdf/                generated PDFs
templates/          reusable templates + vibe-coding-starter app
datasets/           synthetic CSV datasets
cases/ diagrams/ interview-preparation/ references/   pointers (content lives in content/ and the generated outputs)
validation-reports/ link, SQL, site, functional and PDF QA reports
_build/             build scripts, chart generator, CSS/JS
_source/            text extracted from your source PDFs
```

# PROGRESS — Product Management Master Handbook

_Last updated: 23 October 2026. This file is the resume point for future work._

## Toolchain (installed per-user via winget/pip)
Python 3.12, Node 24 LTS, PyMuPDF, Playwright (drives the installed **Microsoft Edge**; no browser download), `markdown`, `pymdown-extensions`, `pyyaml`, `pillow`.
If `python` isn't found in a new terminal, run: `$env:Path = [Environment]::GetEnvironmentVariable('Path','User') + ';' + [Environment]::GetEnvironmentVariable('Path','Machine')`.

## Commands (from this folder)
| Command | What it does |
|---|---|
| `python -I _build/build.py` | content/ → website, print HTML, root index.html, diagrams/*.svg |
| `python -I -X utf8 _build/pdf.py [Name…]` | print HTML → pdf/ (TOC page numbers filled, bookmarks rebuilt); re-run build.py afterwards to copy PDFs into the site |
| `python -I -X utf8 _build/validate.py` | SQL examples, internal links/anchors, external links → validation-reports/ |
| `python -I -X utf8 _build/pdf_qa.py` | blank pages, text past margins, bookmarks, links → validation-reports/pdf-qa.md |
| `python -I -X utf8 _build/site_test.py` | 28 functional browser tests → validation-reports/functional-tests.md |
| `python -I _build/make_datasets.py` | regenerate synthetic datasets (seeded) |

## Architecture
- `content/modules/mNN-*.md` — one file per module (YAML front matter + Markdown).
- `content/{frameworks,cases,projects,interview}/*.md` — several entries per file, separated by `<!-- item -->`.
- Fenced blocks: ```` ```chart ```` (YAML → SVG/HTML via `_build/charts.py`: funnel, bar, hbar, line, heatmap, scatter/2×2, normal curve, steps, layers, tree, loop, pareto, concentric, canvas, compare, phone wireframes), ```` ```quiz ````, ```` ```formula ````.
- Callouts: `!!! level1|level2|level3|source|hypo|example|tip|warning|question`; collapsible answers: `??? answer "…"`, `??? question "…"`.

## Status
| Deliverable | Status | Evidence |
|---|---|---|
| Source assessment, coverage matrix, gap analysis | Done | `source-coverage-matrix.md`, `curriculum-gap-analysis.md` |
| 12 modules | Drafted, built, checked | 12 pages, 127 inline visuals (charts, diagrams, canvases, wireframes, comparison figures), a quiz on every page, exercises with model answers |
| Framework library | Done | 29 frameworks + selection guide |
| Case studies | Done | 12 cases (+ a full AI support case inside Module 12) |
| Practical projects | Done | 5 projects, 5 dedicated datasets, model solutions |
| Interview handbook | Done | 106 questions, each with what's tested / approach / model answer / trade-offs / mistakes / 60-second version; scorecard and worksheet |
| Templates | Done | 10 Markdown templates + runnable vibe-coding starter (tested at 375 px, no JS errors) |
| Datasets | Done | 11 synthetic CSVs |
| Glossary | Done | 175 terms |
| Interactive site | Done | 28/28 functional tests pass (search, quizzes, progress, theme, filters, glossary, downloads, back-to-top, mobile menu, no horizontal scroll at 375 px) |
| PDFs | Done | Complete handbook 444 pp; 12 module PDFs; 4 library PDFs; 0 blank pages, 0 margin overflows flagged |
| Links | Done | 73/73 external links returned OK on the last check; 0 broken internal links |
| SQL examples | Done | 7/7 run against the datasets |
| Standalone diagrams | Done | 126 SVGs in `diagrams/` |

## Known gaps and limits (be aware before relying on them)
1. **Curriculum screenshot not received.** Module titles are from your brief and marked provisional; no screenshot-vs-PDF comparison was possible.
2. **Teaching structure applied proportionately.** Every module has three-level explanations, worked examples, visuals, mistakes, interview angles, exercises with answers, key takeaways, a quiz and resources — but not every *sub*-topic carries all 18 elements of the brief.
3. **Not every metric has its own chart.** (Modules 6 and 11 were expanded to 12 and 9 visuals on 23 Oct 2026.) E.g., ARPU/ARPPU, GMV, NRR and payback use formula panels and worked tables rather than individual charts.
4. **No real product screenshots by design.** All UI images are clearly labelled illustrative wireframes. No Figma file was created (the Figma connector needs authorisation via /mcp).
5. **Hosted publicly on Netlify** at https://pm-master-handbook-varun.netlify.app (team-login protection switched off on request, 23 Oct 2026). It still works locally from `file://` too.
6. **Human review recommended.** Numbers in examples were re-computed by script and SQL outputs come from real query runs, but the prose has not had an independent human/editorial review.
7. **Fast-changing facts** (AI tool features, prices, cloud product names) are described generically with links to official docs; re-check before relying on them.
8. Lectures **44** and **54** had no recordings and are not summarised.

## Ideas for the next iteration
- Verify module titles against the curriculum screenshot and adjust.
- Add charts for remaining metrics; add more worked datasets per module.
- Host the site (GitHub Pages) and add a version changelog.
- Add spaced-repetition flashcards generated from the glossary.

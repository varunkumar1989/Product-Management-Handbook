# Source Coverage Matrix

Maps every part of the source PDFs to the handbook module(s) that absorb it.

**Sources analysed (all pages, via text extraction in `_source/`):**

| ID | File | Pages | Notes |
|----|------|-------|-------|
| S1 | `Expanded_PM_AI_and_Tools_Study_Guide.pdf` | 95 | Base source. Lectures 1–55, picture lessons, dictionary, references, 28-chapter tools companion (pp. 73–87), 15 additional PM topics (pp. 88–95). |
| S2 | `Complete_Visual_PM_AI_and_Tools_Study_Guide.pdf` | 87 | Word-level diff against S1: **0 words appear only in S2**. S2 = S1 minus the "Additional PM Topics" section. Treated as fully covered by S1. |
| S3 | `PM_Technology_Practical_Companion.pdf` | 15 | Found in the same folder (not attached). Its table of contents matches S1 companion chapters 1–28. Not separately mapped. |
| C  | Curriculum screenshot (12 Product Core modules) | – | **Not received.** The 12 module titles from the brief are used and marked *provisional* until verified against the screenshot. |

**Source-quality note.** S1 is a set of study notes written from auto-generated lecture transcripts. It repeatedly flags where the instructor's statements were inaccurate (e.g. RAG requires a vector DB; LoRA is a model; Ansoff quadrant mix-ups; RICE "reach − impact = churn"). The handbook keeps those corrections (as "Source-flagged misconceptions") rather than the original claims. Lectures **44** and **54** have no recording, so nothing is claimed about their content.

## A. Lecture-to-module map (S1 pp. 1–66)

| Lecture | S1 page | Primary module | Also feeds |
|---|---|---|---|
| L1 Orientation | 1 | M1 | – (course logistics only; no PM content) |
| L2 Intro to PM | 2 | M1 | M6 (career), Interview |
| L3 User understanding & research | 3 | M3 | M1 |
| L4 Favourite product critique | 4 | M3 | Interview (product sense) |
| L5 Journey mapping & user flows | 5 | M3 | M5 |
| L6 Market research with GenAI | 6 | M3 | M2 (TAM/SAM/SOM), M10 |
| L7 Guesstimates | 8 | M3 | Interview (estimation) |
| L8 Product case studies | 9 | M4 | Interview (product design) |
| L9 Competitor analysis | 10 | M2 | M3 |
| L10 Product strategy & BYDP intro | 11 | M2 | M1 |
| L11 Improving YouTube Shorts | 12 | M3 | Cases |
| L12 Development methodologies | 13 | M1 | M9 (Agile, CI/CD) |
| L13 Vision, roadmap, Jira | 15 | M2 | M4, M6 |
| L14 PRDs, Confluence, AI docs | 16 | M6 | M10 |
| L15 Ride-hailing surge pricing | 17 | M8 | M2 (pricing), Cases |
| L16 UI/UX, Figma, AI design | 18 | M5 | M11 |
| L17 Prioritization frameworks | 20 | M4 | – |
| L18 PM career Q&A | 21 | Interview | M1 |
| L19 Product teardown | 22 | M3 | Cases |
| L20 MVP | 23 | M4 | M11 |
| L21 North Star & metrics | 24 | M7 | M2 |
| L22 Interview prep 1 | 26 | Interview | M7 (metric drop RCA) |
| L23 GTM strategy | 27 | M8 | M2 |
| L24 Strategy frameworks (Ansoff, Five Whys, STAR) | 28 | M2 | M4, M6, Interview |
| L25 AARRR | 29 | M7 | M8 |
| L26 Acquisition, activation, monetisation | 30 | M8 | M2 (pricing), M7 |
| L27 Hypothesis-driven dev / A/B | 32 | M7 | M4 |
| L28 Product teardown (Claude) | 33 | M3 | M10 (AI eval) |
| L29 Technical basics | 34 | M9 | – |
| L30 Technical PM mock interview | 35 | Interview | M9 |
| L31 Quick-commerce AOV case | 36 | M7 | Cases |
| L32 Build Your Own Product guidance | 38 | Projects | M4 |
| L33 APIs, integrations, testing | 39 | M9 | – |
| L34 SQL fundamentals | 40 | M7 | M9 |
| L35 Vectors & analytics demo | 41 | M10 | M7 (GA setup) |
| L36 Facebook Groups case | 43 | M8 | Cases |
| L37 What is AI PM | 44 | M10 | M1 |
| L38 Framing AI problems | 45 | M10 | M4 |
| L39 Prompting frameworks | 46 | M10 | M11 |
| L40 AI PRDs & data requirements | 47 | M10 | M6 |
| L41 Dating product case | 49 | M8 | M10, Cases |
| L42 Intro to vibe coding | 50 | M11 | – |
| L43 Vibe-coding an MVP | 51 | M11 | M4 |
| L44 Interview Prep 4 | 52 | Interview | **Recording unavailable – not covered** |
| L45 RAG and workflow | 52 | M10 | M12 |
| L46 MCP & workflows | 54 | M12 | M9 |
| L47 LLMs & fine-tuning | 55 | M10 | – |
| L48 Agents & prototype | 56 | M12 | M11 |
| L49 Agents part 2 | 58 | M12 | M11 |
| L50 Document-QA prototype | 59 | M10 | M11, M12 |
| L51 AI ethics & orchestration | 60 | M12 | M10 |
| L52 AI PM mock interview 1 | 61 | Interview | M10 |
| L53 AI PM mock interview 2 | 62 | Interview | – |
| L54 Agent competition | 64 | M12 | **Recording unavailable – not covered** |
| L55 BYDP capstones | 64 | Projects | M12 |

## B. Picture lessons, dictionary, references (S1 pp. 66–72)

| Source item | Handbook destination |
|---|---|
| Picture lesson: LLM | M10 §LLM inference + diagram |
| Picture lesson: Vectors & embeddings | M10 §Embeddings |
| Picture lesson: RAG | M10 §RAG pipeline diagram |
| Picture lesson: AI agents & safe actions | M12 §Agent loop |
| Picture lesson: API & MCP | M9 §APIs, M12 §MCP |
| Picture lesson: Product discovery & design | M3, M5 |
| Dictionary (≈20 terms) | Glossary (all terms retained, expanded) |
| Selected references (7) | `references/` – links re-verified before publishing |

## C. Practical companion (S1 pp. 73–87)

| # | Chapter | Module |
|---|---|---|
| 1 | Think like a PM | M1 |
| 2 | Discovery, interviews, segmentation | M3 |
| 3 | Journeys, flows, UX critique | M3, M5 |
| 4 | Requirements & prioritization | M4, M6 |
| 5 | KPIs & worked funnel | M7 |
| 6 | Experiments | M7 |
| 7 | How websites/apps work | M9 |
| 8 | APIs, JSON, webhooks | M9 |
| 9 | Data, databases, events | M7, M9 |
| 10 | AI / ML / GenAI | M10 |
| 11 | LLMs, tokens, context windows | M10 |
| 12 | Embeddings & similarity | M10 |
| 13 | RAG | M10 |
| 14 | Agentic AI & safe automation | M12 |
| 15 | MCP vs API | M12 |
| 16 | AI evaluation, privacy, security | M10, M12 |
| 17 | Figma for PMs | M5 |
| 18 | Jira | M6, M9 |
| 19 | Confluence | M6 |
| 20 | Claude workflows | M11 |
| 21 | ChatGPT workflows | M11 |
| 22 | Gemini workflows | M11 |
| 23 | Lovable | M11 |
| 24 | GitHub for PMs | M11 |
| 25 | n8n | M12 |
| 26 | Replit | M11 |
| 27 | Automating an existing website safely | M12 |
| 28 | Tool selection & 30-day plan | M11 + Resources |

## D. Additional PM topics (S1 pp. 88–95)

| # | Topic | Module |
|---|---|---|
| 1 | Vision, strategy, roadmap | M2 |
| 2 | Goals, OKRs, outcomes | M2 |
| 3 | North Star & metric trees | M7 |
| 4 | Retention, cohorts, activation | M7 |
| 5 | Pricing & value | M2, M8 |
| 6 | Unit economics & contribution margin | M7 |
| 7 | CAC & LTV | M7 |
| 8 | Market sizing & segmentation | M2 |
| 9 | Positioning & competitive analysis | M2 |
| 10 | GTM & launch planning | M8 |
| 11 | Stakeholder alignment & trade-offs | M6 |
| 12 | Delivery, dependencies, tech debt | M4, M9 |
| 13 | Incidents, reliability, monitoring | M9 |
| 14 | Accessibility & inclusive design | M5 |
| 15 | PM templates (problem, experiment, decision, launch) | Templates |

## E. Status of the new handbook

All 12 modules, the framework library, case library, projects, interview handbook, templates and glossary are written and built (see `PROGRESS.md`). Each module file under `content/modules/` carries a `sources:` header naming the lectures and companion chapters it preserves; preserved content appears in green-grey **"From your course notes"** boxes, so every row above can be audited in the built pages.

| Module | Source lectures / chapters absorbed (from the header of each module file) |
|---|---|
| M1 | L1, L2, L12, L20; Companion 1; Extra 1, 11, 15 |
| M2 | L6, L9, L10, L13, L23, L24; Extra 1, 2, 5, 8, 9, 10 |
| M3 | L3, L4, L5, L6, L7, L8, L11, L19, L28, L36; Companion 2, 3; picture lesson "discovery" |
| M4 | L8, L17, L20, L24, L27, L43; Companion 4; Extra 12 |
| M5 | L5, L16, L27; Companion 3, 17; Extra 14; picture lesson "discovery" |
| M6 | L13, L14, L18, L22, L24, L30, L52, L53; Companion 18, 19; Extra 11, 15 |
| M7 | L21, L25, L26, L27, L31, L34, L35; Companion 5, 6, 9; Extra 3, 4, 6, 7 |
| M8 | L15, L23, L25, L26, L36, L41; Extra 5, 10, 13 |
| M9 | L12, L29, L30, L33, L34; Companion 7, 8, 9, 18, 24; Extra 12, 13 |
| M10 | L35, L37, L38, L39, L40, L45, L47, L50, L51; picture lessons; Companion 10–13, 16 |
| M11 | L42, L43, L48, L49, L50; Companion 20–24, 26, 28 |
| M12 | L46, L48, L49, L50, L51, L54 (unavailable), L55; picture lessons; Companion 14, 15, 25, 27 |
| Interview | L18, L22, L30, L44 (unavailable), L52, L53 |
| Projects | L32, L55 |

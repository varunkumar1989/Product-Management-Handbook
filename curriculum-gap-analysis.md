# Curriculum Gap Analysis

Comparison of the existing study guide (S1) against the 12-module Product Core curriculum in the brief. Module titles are **provisional** because the curriculum screenshot did not arrive.

Legend — **Strong**: taught with examples in S1 · **Partial**: mentioned or taught shallowly · **Missing**: not in S1 (added as independent material in the handbook, labelled "Independent / verified reference", never as course content).

## Module by module

| Module | Strong in S1 | Partial | Missing from S1 (handbook adds) |
|---|---|---|---|
| **M1 Fundamentals** | PM role & specialisations, MVP, Agile/Scrum/Kanban, career paths | PM vs PO vs BA, PLG vs SLG | PM vs Project Mgr / Designer / PMM comparison tables, product lifecycle (PLC), operating models, outcome vs output, discovery vs delivery, platform vs feature, B2B vs B2C, common mistakes |
| **M2 Strategy** | Vision/strategy/roadmap, Ansoff, competitor analysis, TAM/SAM/SOM, positioning, pricing basics, OKRs | SWOT (named), North Star | Porter's Five Forces (announced but untaught in L24), PESTLE, STP, value propositions, BMC, Lean Canvas, Blue Ocean, moats / network effects, build-buy-partner, portfolio strategy |
| **M3 Discovery** | Personas, interviews, journey maps, market research, guesstimates, teardown | JTBD (referenced only), segmentation | Interview scripts, survey bias, Opportunity Solution Trees, affinity mapping, assumption mapping, triangulation, review mining |
| **M4 Prioritization** | RICE, impact/effort, MoSCoW, Five Whys, MVP, hypothesis dev | Dependencies | Kano, ICE, weighted scoring, Cost of Delay, WSJF, Pareto, fishbone, first principles, systems thinking, risk-adjusted prioritisation, experiment prioritisation |
| **M5 UX & Design** | UI vs UX, Figma basics, wireframe vs prototype, accessibility, usability testing | Journey vs flow | Nielsen heuristics, Fitts/Hick/Jakob, Gestalt, cognitive load, IA, design systems, responsive/mobile, error & empty states, UX metrics (HEART), handoff |
| **M6 Communication** | PRDs, decision notes, stakeholder trade-offs, STAR, estimates without blame | Jira/Confluence | Pyramid Principle, PREP, storytelling with data, negotiation, conflict resolution, exec reviews, dialogue scripts |
| **M7 Analytics** | Metrics definition, North Star, AARRR, funnels, A/B basics, AOV, SQL SELECT/WHERE, cohorts, CAC/LTV, contribution margin | Event instrumentation, GA4 demo | DAU/MAU stickiness, ARPU/ARPPU, payback, GMV, p-values, CIs, Type I/II, power & sample size, SQL joins/aggregation/window functions, Excel, Power BI, Mixpanel/Amplitude, experiment readouts |
| **M8 Growth** | GTM, acquisition/activation/monetisation, revenue models, case discussions | Pricing, referral | Growth loops, lifecycle marketing, PLG, freemium economics, upsell, churn reduction, launch retros, scaling, fintech/SaaS/consumer launch plans |
| **M9 Tech 101** | Frontend/backend, APIs, HTTP methods/codes, SQL, CI/CD, webhooks, dev/staging/prod | Vector DBs | How the internet works, REST vs GraphQL, authN vs authZ, OAuth, caching, LB, queues, CDN, scaling, availability, security basics, system design (payments, food delivery, ride-hailing, notifications, onboarding) |
| **M10 LLM / RAG** | LLM basics, tokens, embeddings, RAG, fine-tuning vs RAG, prompting, AI PRDs, evals, ethics | Context windows | Transformer/attention (conceptual), vector DB options, hallucination mitigation, model selection, cost-latency trade-offs, LLM eval methods, monitoring, governance, RAG/inference diagrams |
| **M11 Vibe Coding** | Concept, Lovable/Replit/Claude/GitHub workflows, prototype ≠ production, security cautions | Cursor/Copilot/Bolt (named only in brief) | HTML/CSS/JS fundamentals, Git fundamentals, DB connection, deployment, testing generated code, **end-to-end hands-on project** |
| **M12 Agentic AI** | Agent definition, tool use, MCP vs API, orchestration, approval checkpoints, n8n, prompt-injection cautions | Memory, multi-agent (L49 doesn't teach it despite LMS text) | Agent architectures, memory systems, evaluation/observability, permission boundaries, failure recovery, cost/latency, agentic business models, **financial-services support case** |

## Other brief requirements vs S1

| Requirement | S1 status | Action |
|---|---|---|
| 12 named real-company case studies | Only classroom exercises (YouTube Shorts, Blinkit AOV, Facebook Groups, Uber surge, Amazon RICE, Zomato persona, Claude teardown, dating) | Build 12 cases; where verified company data is unavailable, label as **hypothetical scenario**. No invented company results. |
| Framework library (29 frameworks) | ~10 appear | Build all 29 with visual, example, limits, template |
| 5 end-to-end projects | Capstone list only | Build 5 with datasets and model solutions |
| 100+ interview questions | Mock interview summaries (L22, L30, L52, L53); L44 missing | Build ≥100 with scoring rubric |
| Hands-on exercises | Light | Add per-topic exercises + answers |

## Known weaknesses in S1 to correct (not reproduce)

Already flagged inside S1 itself — kept as "Source-flagged misconceptions":
RICE (reach − impact ≠ churn; effort is the denominator); Ansoff quadrant labels; "all AI needs RAG/vector DB"; LoRA is a technique not a model; retrieval ≠ fine-tuning; vector DBs are not 3-D file stores; CORS ≠ all UI–API traffic; white-labeling ≠ dropshipping; sprint ≠ always two weeks; MVP ≠ prototype ≠ public launch; unicorn = $1B valuation, not revenue.

Additional observations made while reading S1:
- Dated product claims (pricing, plans, features of Figma Make, Lovable, Replit, n8n, Claude, ChatGPT, Gemini) go stale quickly → the handbook states capabilities generically and links to current official docs.
- S1 contains no worked statistics (p-values, CIs, power). M7 adds these with computed examples.
- S1 contains no SQL beyond `SELECT … WHERE`. M7/M9 add GROUP BY, JOIN, window functions on a provided sample dataset.

## Provisional titles to verify against the screenshot
All 12 module titles, especially M11 "Vibe Coding for Product Managers" and M12 "Agentic AI and AI Systems" (likely truncated in the screenshot per the brief).

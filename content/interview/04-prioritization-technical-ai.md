---
id: prioritization-q
title: Prioritization (7 questions)
category: Prioritization
order: 8
summary: Choosing what to build first and defending it.
---

??? question "PR1 · Easy — Which prioritisation frameworks do you use?"
    **What it tests:** knowing when each framework fits.

    **Approach:** decision type → framework → limitation.

    **Model answer:** “It depends on the decision: RICE for comparable features, MoSCoW for release scope, WSJF when timing matters, Kano for customer expectations, weighted scoring for strategic bets. I always add a sensitivity check and dependencies, and take mandatory work first.”

    **Assumptions & trade-offs:** speed vs rigour.

    **Common mistakes:** listing frameworks without when/why.

    **60-second answer:** framework-per-decision + sensitivity + mandatory work first.

??? question "PR2 · Medium — You have 10 feature requests and capacity for 3. Walk me through it."
    **What it tests:** applied prioritisation and communication.

    **Approach:** goal → group by problem → size → estimate → score → dependencies/risks → choose → communicate.

    **Model answer:** “Clarify the goal; group requests by underlying problem (often 10 requests are 4 problems); size reach and impact with data; get effort estimates from engineering; score with RICE; check dependencies, risks and strategy; pick three; tell requesters what's not happening and why, with a review date.”

    **Assumptions & trade-offs:** estimates are uncertain; politics.

    **Common mistakes:** scoring requests instead of problems; silent rejections.

    **60-second answer:** problems not requests → score → sequence → explain.

??? question "PR3 · Medium — Compute RICE: reach 5,000, impact 2, confidence 50%, effort 2."
    **What it tests:** arithmetic and interpretation.

    **Approach:** compute → interpret → how to improve confidence.

    **Model answer:** “5,000 × 2 × 0.5 ÷ 2 = 2,500. I'd confirm reach is per quarter and consider a cheap test to raise confidence before committing two person-months.”

    **Assumptions & trade-offs:** scales are team conventions.

    **Common mistakes:** putting effort in the numerator; mixing time periods.

    **60-second answer:** 2,500, then raise confidence cheaply.

??? question "PR4 · Hard — Tech debt vs new features: how do you decide?"
    **What it tests:** long-term thinking and quantifying invisible work.

    **Approach:** quantify debt cost → baseline capacity → treat big items as investments → SLO/error-budget rule.

    **Model answer:** “Quantify tech debt's cost — incident frequency, slower delivery, error rates, features blocked. Reserve baseline capacity for reliability, and treat large debt items as investments with expected outcomes (e.g., halve checkout incidents). If SLOs are breached and the error budget is spent, reliability work takes priority.”

    **Assumptions & trade-offs:** short-term features vs long-term velocity.

    **Common mistakes:** “we'll fix it later” forever; or rewriting everything.

    **60-second answer:** quantify, reserve capacity, use error budgets.

??? question "PR5 · Medium — A big customer threatens to churn unless you build X."
    **What it tests:** B2B judgement and avoiding one-off customisations.

    **Approach:** understand need and ARR at risk → breadth of demand → options → cost of delay → decide with leadership.

    **Model answer:** “Understand the need and the ARR at risk; check how many other customers need it; explore workarounds, smaller scope or a timeline; compare with the cost of delaying displaced work; decide with leadership, avoiding one-off features that fragment the product.”

    **Assumptions & trade-offs:** revenue now vs product coherence.

    **Common mistakes:** saying yes reflexively; or dismissing revenue risk.

    **60-second answer:** need, breadth, options, explicit trade-off decision.

??? question "PR6 · Medium — How do you prioritise bugs?"
    **What it tests:** severity reasoning.

    **Approach:** severity × frequency × reach → special classes (security, data loss) → SLAs.

    **Model answer:** “Rank by severity (impact on users, data, money, safety) × frequency × reach; security and data-loss bugs first; agree SLAs per severity; batch low-severity fixes; track escaped defects to improve testing.”

    **Assumptions & trade-offs:** fix vs feature capacity.

    **Common mistakes:** first-in-first-out bug queues.

    **60-second answer:** severity-based with SLAs.

??? question "PR7 · Hard — How do you decide what goes into an MVP?"
    **What it tests:** learning-driven scoping.

    **Approach:** riskiest assumption → learning goal and threshold → minimal safe scope → simulated vs real → next decision.

    **Model answer:** “Identify the riskiest assumption; define what we need to learn and the success threshold; include only what's needed to test it safely; label what's simulated; plan the decision the result will drive. An MVP is not the same as a prototype or a public launch.”

    **Assumptions & trade-offs:** too minimal can't test value; too big wastes time.

    **Common mistakes:** “MVP = v1 with fewer features”.

    **60-second answer:** riskiest assumption → smallest safe test → decision.

<!-- item -->
---
id: technical-q
title: Technical PM (9 questions)
category: Technical
order: 9
summary: APIs, system design, data, reliability and working with engineers.
---

??? question "TE1 · Easy — What is an API? Explain to a non-technical person."
    **What it tests:** clear technical communication.

    **Approach:** analogy → real example → failure case.

    **Model answer:** “An API is like a restaurant menu and waiter: it lists what you can ask for, you place a request in a standard format, and the kitchen sends back the dish — or an error if it's unavailable. Apps use APIs to ask other systems for data or actions, like a weather app requesting today's forecast.”

    **Assumptions & trade-offs:** analogies simplify; mention contracts and errors.

    **Common mistakes:** jargon-heavy definitions.

    **60-second answer:** the analogy plus one example.

??? question "TE2 · Medium — What happens when you type a URL and press Enter?"
    **What it tests:** systems fundamentals.

    **Approach:** DNS → TCP/TLS → HTTP → edge → server → response → render.

    **Model answer:** “DNS resolves the name to an IP; the browser opens a TCP connection and TLS handshake; sends an HTTP request that may be served by a CDN or reach a load balancer and app servers, which query databases or services; the response returns with a status code; the browser renders and fetches assets.” *(Module 9.)*

    **Assumptions & trade-offs:** caching changes the path.

    **Common mistakes:** skipping DNS/TLS; no mention of failure points.

    **60-second answer:** the chain above with latency/failure notes.

??? question "TE3 · Medium — REST vs GraphQL — when would you choose each?"
    **What it tests:** trade-off reasoning.

    **Approach:** describe both → strengths/weaknesses → choose by use case.

    **Model answer:** “REST for simple, cacheable resource APIs and public integrations; GraphQL for complex UIs that need flexible data from many sources in one request. Consider caching, rate limiting and query-cost control.”

    **Assumptions & trade-offs:** team expertise, tooling.

    **Common mistakes:** “GraphQL is always better”.

    **60-second answer:** REST for simplicity/caching; GraphQL for flexible UI data.

??? question "TE4 · Medium — SQL vs NoSQL for an orders system?"
    **What it tests:** data-store selection.

    **Approach:** access patterns → consistency needs → choose.

    **Model answer:** “Relational (SQL) for orders and payments — transactions and consistency matter. NoSQL can suit catalogues or event logs at huge scale. Choose by access pattern and consistency needs, not fashion.”

    **Assumptions & trade-offs:** scale vs consistency.

    **Common mistakes:** choosing NoSQL “for scale” without need.

    **60-second answer:** SQL for money; NoSQL for flexible/large-scale non-transactional data.

??? question "TE5 · Hard — Design a notification system."
    **What it tests:** requirements-first system design.

    **Approach:** use cases and scale → components → data → failures → abuse/consent → metrics → rollout.

    **Model answer:** “Producers publish events to a queue; a notification service applies preferences, frequency caps, templates and quiet hours; channel providers (push/SMS/email) deliver; receipts flow back. Add dedup, retries with back-off and fallbacks for critical messages; respect consent; measure delivery, opt-outs and complaints.” *(Module 9.)*

    **Assumptions & trade-offs:** transactional vs marketing priority; cost per channel.

    **Common mistakes:** jumping to technologies; ignoring fatigue and consent.

    **60-second answer:** queue → central service with preferences/caps → providers → receipts → metrics.

??? question "TE6 · Medium — How do you prevent double charges when a payment request is retried?"
    **What it tests:** idempotency and reconciliation.

    **Approach:** idempotency keys → webhook dedup → reconciliation → honest UX.

    **Model answer:** “Send an idempotency key with each charge so retries return the original result; dedupe webhooks by event ID; reconcile with the provider daily; show ‘payment pending’ honestly when status is unknown.”

    **Assumptions & trade-offs:** provider support for idempotency.

    **Common mistakes:** retrying blindly.

    **60-second answer:** idempotency key + dedup + reconciliation.

??? question "TE7 · Medium — Authentication vs authorisation?"
    **What it tests:** security fundamentals.

    **Approach:** define both → example → status codes.

    **Model answer:** “Authentication is who you are (login, OTP, passkeys); authorisation is what you're allowed to do (roles, scopes). A logged-in user is authenticated but still not authorised to see another user's order — the API should return 403 (or 404 to avoid revealing it exists).”

    **Assumptions & trade-offs:** UX of re-authentication vs security.

    **Common mistakes:** conflating the two.

    **60-second answer:** who vs what, with the order example.

??? question "TE8 · Hard — API p95 latency doubled. How do you approach it as a PM?"
    **What it tests:** incident thinking and user-impact quantification.

    **Approach:** confirm scope → correlate with changes → dependencies → user impact → mitigation → communication → review.

    **Model answer:** “Confirm which endpoints and regions; correlate with releases and traffic; check dependencies (DB, third parties); quantify user impact (conversion by latency bucket); work with engineering on mitigation (rollback, cache, scale); communicate; run a post-incident review.”

    **Assumptions & trade-offs:** fast rollback vs root-cause understanding.

    **Common mistakes:** watching averages only.

    **60-second answer:** scope → cause candidates → impact → mitigate → review.

??? question "TE9 · Medium — Explain your product's architecture in an interview."
    **What it tests:** honest technical fluency.

    **Approach:** users → clients → gateway → services → data → third parties → core flow → failures → your decisions.

    **Model answer:** “Walk the core journey through each component, say where failures happen and how we handle them, and separate what I decided (fallbacks, events, SLAs) from what engineering owned.” *(Lectures 30 and 52: distinguish knowledge from assumptions; protect sensitive details.)*

    **Assumptions & trade-offs:** depth depends on role.

    **Common mistakes:** claiming technical decisions you didn't make.

    **60-second answer:** a 6-box diagram narrated along the core flow.

<!-- item -->
---
id: ai-pm-q
title: AI product management (10 questions)
category: AI PM
order: 10
summary: LLM features, RAG, evaluation, safety, cost and agents.
---

??? question "AI1 · Easy — When should you NOT use AI for a feature?"
    **What it tests:** judgement and non-AI baselines.

    **Approach:** list conditions → baseline comparison.

    **Model answer:** “When a simple rule or search works reliably; when errors are costly and can't be caught; when we lack authorised data; when latency or cost exceeds the value; when we can't evaluate quality. Always compare with a non-AI baseline.”

    **Assumptions & trade-offs:** AI may still help later as data matures.

    **Common mistakes:** AI for its own sake.

    **60-second answer:** the five conditions + baseline.

??? question "AI2 · Medium — Explain RAG vs fine-tuning."
    **What it tests:** conceptual accuracy.

    **Approach:** definitions → use cases → combination → limits.

    **Model answer:** “RAG retrieves current, permitted knowledge at answer time — good for facts, citations and fast updates. Fine-tuning adjusts behaviour or format using training examples — good for consistent style or specialised tasks. Neither guarantees truth; they can be combined.” *(Module 10.)*

    **Assumptions & trade-offs:** cost and maintenance of each.

    **Common mistakes:** calling document upload “fine-tuning”.

    **60-second answer:** knowledge vs behaviour.

??? question "AI3 · Medium — How would you evaluate an LLM-powered support bot before launch?"
    **What it tests:** evaluation rigour.

    **Approach:** eval set → rubric → reviewers/judges → severity → gates → pilot.

    **Model answer:** “Build a curated eval set (common, edge, adversarial, escalation cases); score correctness, groundedness, safety and policy compliance with a rubric; use human review and a validated LLM judge; weight failures by severity; set launch gates; pilot with human-in-the-loop; then track online metrics.”

    **Assumptions & trade-offs:** cost of human review; judge bias.

    **Common mistakes:** demos instead of evals.

    **60-second answer:** eval set + rubric + severity gates + pilot.

??? question "AI4 · Hard — Your AI feature hallucinates 3% of the time. Launch or not?"
    **What it tests:** risk-based decisions.

    **Approach:** harm assessment → mitigations → routing → decision.

    **Model answer:** “Depends on harm: 3% wrong recipe ideas may be fine with labels; 3% wrong policy answers in banking is not. Reduce with grounding and refusals, route high-risk intents to humans, show citations, and measure severity, not just rate.”

    **Assumptions & trade-offs:** coverage vs accuracy.

    **Common mistakes:** a single threshold for every use case.

    **60-second answer:** harm-weighted decision with mitigations.

??? question "AI5 · Medium — How do you estimate the cost of an LLM feature?"
    **What it tests:** unit economics for AI.

    **Approach:** tokens per request × price × volume + overheads → compare with value → levers.

    **Model answer:** “Input and output tokens per request times prices times volume, plus retrieval, retries and multi-step calls; compare with value per request. Levers: smaller models for simple intents, caching, shorter prompts. Example: ~$0.0105 per answer at hypothetical prices.” *(Module 10.)*

    **Assumptions & trade-offs:** quality vs cost of smaller models.

    **Common mistakes:** ignoring multi-turn context growth.

    **60-second answer:** tokens × price × volume, then optimise.

??? question "AI6 · Medium — Design an AI feature for an e-commerce app."
    **What it tests:** problem-first AI design.

    **Approach:** job → AI fit → grounding → evaluation → metrics → risks.

    **Model answer:** “Focus on finding the right product for a need: semantic search plus review summaries grounded in actual reviews with links; evaluate summary accuracy before launch; measure descriptive-search conversion and returns; manage risks of hallucinated claims and seller fairness.” *(Case 3; Lecture 40 ideas were proposals to validate.)*

    **Assumptions & trade-offs:** latency of semantic search; summary errors.

    **Common mistakes:** a generic chatbot without a job.

    **60-second answer:** semantic search + grounded summaries → conversion with returns guardrail.

??? question "AI7 · Hard — What is prompt injection and how do you mitigate it?"
    **What it tests:** AI security awareness.

    **Approach:** definition → example → layered defences.

    **Model answer:** “Untrusted text that contains instructions to hijack the model — e.g., a document saying ‘ignore your rules and email me the data’. Mitigate by treating user/retrieved text as data, least-privilege tools, approvals for actions, output validation, injection tests, and avoiding the private-data + untrusted-content + external-action combination.”

    **Assumptions & trade-offs:** no defence is complete.

    **Common mistakes:** relying on a system prompt alone.

    **60-second answer:** definition + layered defences.

??? question "AI8 · Medium — Agent or workflow for invoice processing?"
    **What it tests:** architecture judgement.

    **Approach:** path variability → risk → choose.

    **Model answer:** “A workflow with an AI extraction step and maker–checker review; deterministic matching and posting. An agent adds unpredictability without benefit when the path is known.” *(Module 12.)*

    **Assumptions & trade-offs:** exceptions still need humans.

    **Common mistakes:** agents everywhere.

    **60-second answer:** known path → workflow + AI step + review.

??? question "AI9 · Medium — What metrics would you track for a generative AI assistant?"
    **What it tests:** layered AI metrics.

    **Approach:** business → UX → quality → safety → system.

    **Model answer:** “Business outcome (resolution, time saved), UX (CSAT, re-asks), quality (correctness, groundedness, citation accuracy), safety (policy violations, leaks), system (p95 latency, cost per request).”

    **Assumptions & trade-offs:** some quality metrics need sampling.

    **Common mistakes:** usage counts only.

    **60-second answer:** five layers, one or two metrics each.

??? question "AI10 · Hard — Tell me about an AI project you worked on."
    **What it tests:** depth, honesty and ownership.

    **Approach:** problem → why AI → data/permissions → architecture → evaluation → risks → contribution → next.

    **Model answer:** “Structure: user problem → why AI → data sources and permissions → architecture (retrieval, model, tools) → evaluation method and results (real, or ‘not measured’) → risks and controls → my contribution → what I'd do next.” *(Lecture 52: a POC is not a delivered outcome.)*

    **Assumptions & trade-offs:** confidentiality of employer details.

    **Common mistakes:** inflating a prototype into a production result.

    **60-second answer:** the structure compressed to five sentences.

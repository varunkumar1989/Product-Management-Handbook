---
id: selection-guide
title: "Framework selection guide: which framework should I use?"
category: Guide
order: 0
summary: Match your product problem to the right framework, and know when not to use one.
---

Frameworks are thinking tools: they organise evidence and make reasoning visible. They never replace evidence or judgement. Start from **the decision you need to make**, then pick the lightest framework that helps.

```chart
type: compare
title: Given this problem, which framework?
headers: ["If your question is…", "Reach for", "Why", "Avoid"]
rows:
  - ["Who is the customer and what are they trying to get done?", "JTBD, Customer Journey Map", "Frames demand around progress in a situation", "Demographic personas alone"]
  - ["Which customer problem should we pursue for our outcome?", "Opportunity Solution Tree", "Links outcome → opportunities → solutions → tests", "Jumping to features"]
  - ["Is our idea worth pursuing at all?", "Lean Startup / Build-Measure-Learn, assumption testing", "Cheapest test of riskiest assumption", "Building the full product first"]
  - ["What should we build first?", "RICE / ICE (comparable items); WSJF (time-critical)", "Explicit, comparable scoring", "Scores as facts; ignoring dependencies"]
  - ["What fits in this release?", "MoSCoW", "Scope negotiation against a date", "Ranking within a category"]
  - ["Which features delight vs are expected?", "Kano", "Customer expectation categories", "Small or unsegmented samples"]
  - ["Choose among few strategic bets", "Weighted scoring, Cost of Delay", "Encodes strategic criteria and urgency", "Reverse-engineered weights"]
  - ["Where are we in the market? Should we enter?", "SWOT, PESTLE, Porter's Five Forces", "Structured environment scan", "Lists without so-what"]
  - ["How does our business create and capture value?", "Business Model Canvas, Value Proposition Canvas", "Makes the model and fit explicit", "Treating cells as facts"]
  - ["What single metric aligns the team?", "North Star Framework (+ metric tree), OKRs", "Focus with drivers and guardrails", "One metric without guardrails"]
  - ["Where is the growth funnel leaking?", "AARRR", "Stage-by-stage diagnosis", "Generic definitions"]
  - ["How do we measure UX quality?", "HEART", "Goals → signals → metrics", "Tracking all five by default"]
  - ["Did the change work?", "Hypothesis testing, A/B testing", "Causal evidence with uncertainty", "Underpowered tests; peeking"]
  - ["Why did this happen?", "Five Whys, fishbone, Pareto", "Root causes and focus", "Single-chain blame"]
  - ["Are we stuck in assumptions or loops?", "First principles, systems thinking", "Rebuild from fundamentals; see feedback loops", "Over-theorising simple issues"]
  - ["How should we explore a fuzzy problem?", "Design Thinking, Double Diamond", "Diverge then converge with users", "Workshops without real users"]
caption: Start from the decision. If a framework doesn't change what you would do, skip it.
```

**Decision tree in words:** *Unclear problem?* → discovery frameworks (JTBD, journey, OST, Design Thinking). *Clear problem, many options?* → prioritisation (RICE/ICE/WSJF/MoSCoW/Kano). *Strategic direction?* → SWOT/PESTLE/Porter/canvases. *Measuring?* → North Star, AARRR, HEART, OKRs. *Proving causality?* → hypothesis and A/B testing. *Something broke?* → Five Whys, fishbone, Pareto.

!!! tip "Interview tip"
    Name a framework only after you have clarified the problem, then *use* it (show a few real scores or boxes) and state its limitation. Interviewers reward applied judgement, not vocabulary.

<!-- item -->
---
id: swot
title: SWOT
category: Strategy
order: 10
summary: Strengths, weaknesses (internal), opportunities, threats (external) — then turn them into actions.
---

```chart
type: canvas
title: SWOT model
cols: 2
cells:
  - {title: "Strengths (internal, helpful)", tone: g, text: ["Capabilities, assets, advantages"]}
  - {title: "Weaknesses (internal, harmful)", tone: r, text: ["Gaps, constraints, liabilities"]}
  - {title: "Opportunities (external, helpful)", tone: b, text: ["Trends, unmet needs, partners"]}
  - {title: "Threats (external, harmful)", tone: w, text: ["Competitors, regulation, cost shifts"]}
caption: Follow with TOWS: S×O (use strengths to seize), W×O (fix to seize), S×T (use strengths to defend), W×T (avoid).
```

**Use when:** framing a strategy discussion, market entry, annual planning. **Don't use when:** you need prioritised actions or quantified trade-offs — SWOT alone produces lists.

**Worked example (hypothetical):** regional food-delivery entrant — S: restaurant relationships; W: small marketing budget; O: office-lunch subscriptions; T: incumbents' promo wars. **TOWS action:** S×O → launch office-lunch subscriptions through existing restaurant partners; W×T → don't compete on discounts.

**Limitations:** subjective, static, often evidence-free; items mix levels of importance. Always attach evidence and rank items.

**Template:** for each quadrant list ≤ 5 items, each with *evidence* and *importance (H/M/L)*; then write 3 TOWS actions with owners. **Deep dive:** Module 2.

<!-- item -->
---
id: pestle
title: PESTLE
category: Strategy
order: 11
summary: Scan the macro environment — Political, Economic, Social, Technological, Legal, Environmental.
---

```chart
type: canvas
title: PESTLE model
cols: 3
cells:
  - {title: "Political", text: ["Government policy, stability, trade"]}
  - {title: "Economic", text: ["Rates, inflation, income, demand"]}
  - {title: "Social", text: ["Demographics, behaviour, trust"]}
  - {title: "Technological", text: ["Infrastructure, platforms, AI"]}
  - {title: "Legal", text: ["Data protection, consumer law, licensing"]}
  - {title: "Environmental", text: ["Climate, sustainability expectations"]}
caption: Mark each factor as tailwind or headwind, rate impact × certainty, and assign a watcher.
```

**Use when:** entering a new market or country; long-range planning; regulated products. **Don't use when:** you need customer-level insight (use research) or competitor detail (use competitor analysis).

**Worked example (hypothetical):** fintech lending in a new market — *Legal:* data-protection consent and lending disclosures (high impact, high certainty → design consent flows early); *Technological:* digital ID infrastructure (tailwind → faster KYC); *Economic:* rising interest rates (headwind → stricter credit policy).

**Limitations:** can become a long list with no prioritisation; factors interact; needs expert input for legal/regulatory items. **Template:** factor · description · tailwind/headwind · impact (1–5) · certainty (1–5) · implication · owner. **Deep dive:** Module 2.

<!-- item -->
---
id: porter
title: Porter's Five Forces
category: Strategy
order: 12
summary: Assess industry attractiveness via rivalry, entrants, substitutes, buyer and supplier power.
---

```chart
type: layers
title: Five Forces model
rows:
  - ["Threat of new entrants"]
  - ["Supplier power", "Competitive rivalry", "Buyer power"]
  - ["Threat of substitutes"]
edges:
  - ["Threat of new entrants", "Competitive rivalry"]
  - ["Supplier power", "Competitive rivalry"]
  - ["Buyer power", "Competitive rivalry"]
  - ["Threat of substitutes", "Competitive rivalry"]
caption: Stronger forces mean lower structural profit potential. Ask which force your product can weaken.
```

**Use when:** deciding whether to enter a market, explaining margin pressure, positioning against structural threats. **Don't use when:** analysing a single feature, or in fast-changing ecosystems without considering complements and platforms.

**Worked example (hypothetical):** food delivery — rivalry high (promotions), buyer power high (low switching costs), supplier power medium–high (restaurants multi-home), substitutes high (cooking, dining out), entrants medium (density is hard). **Implication:** invest in habit/loyalty (reduce buyer power) and partner tools (reduce supplier churn).

**Limitations:** static snapshot; industry boundaries are fuzzy; ignores network effects and complementors. **Template:** force · rating (L/M/H) · evidence · trend · product lever. **Deep dive:** Module 2.

<!-- item -->
---
id: bmc
title: Business Model Canvas
category: Strategy
order: 13
summary: Nine blocks describing how an organisation creates, delivers and captures value.
---

```chart
type: canvas
title: Business Model Canvas (structure)
cols: 5
cells:
  - {title: "Key partners", rows: 2, text: ["Who helps us?"]}
  - {title: "Key activities", text: ["What must we do well?"]}
  - {title: "Value propositions", rows: 2, tone: b, text: ["What value for whom?"]}
  - {title: "Customer relationships", text: ["How do we relate?"]}
  - {title: "Customer segments", rows: 2, tone: v, text: ["For whom?"]}
  - {title: "Key resources", text: ["What do we need?"]}
  - {title: "Channels", text: ["How do we reach them?"]}
  - {title: "Cost structure", span: 2, tone: w, text: ["Major costs"]}
  - {title: "Revenue streams", span: 3, tone: g, text: ["How we earn"]}
caption: Fill right side (customers, value) first; then left (how you deliver); then costs and revenue.
```

**Use when:** describing or redesigning a business model; comparing models; onboarding stakeholders to the economics. **Don't use when:** you're still searching for a problem (use Lean Canvas) or need financial detail (build a model).

**Worked example:** see the meal-planning app canvas in Module 2. **Limitations:** static; doesn't show competition or sequencing; cells are assumptions until tested. **Template:** the nine headings with *assumption / evidence / test* for each cell. **Deep dive:** Module 2.

<!-- item -->
---
id: vpc
title: Value Proposition Canvas
category: Strategy
order: 14
summary: Fit customer jobs, pains and gains with your products, pain relievers and gain creators.
---

```chart
type: canvas
title: Value Proposition Canvas (structure)
cols: 2
cells:
  - {title: "Value map: Products & services", tone: b, text: ["What we offer"]}
  - {title: "Customer profile: Jobs", tone: v, text: ["Functional, emotional, social jobs"]}
  - {title: "Value map: Pain relievers", tone: b, text: ["How we remove pains"]}
  - {title: "Customer profile: Pains", tone: v, text: ["Obstacles, risks, frustrations"]}
  - {title: "Value map: Gain creators", tone: b, text: ["How we create gains"]}
  - {title: "Customer profile: Gains", tone: v, text: ["Outcomes and benefits sought"]}
caption: Fit = your relievers and creators address the most important pains and gains (ranked by customers, not by you).
```

**Use when:** shaping a new offering or repositioning; aligning product and marketing on what matters. **Don't use when:** you have no customer research yet — the right side would be guesses.

**Worked example (hypothetical):** busy parents — job: feed the family on budget; top pain: surprise grocery bills; reliever: price estimate before shopping; gain creator: weekly budget tracker. **Test:** smoke test with the promise “Know your weekly grocery cost in 5 minutes”.

**Limitations:** easy to fill with assumptions; doesn't capture competition. **Template:** rank top 3 jobs, pains, gains with evidence; map each reliever/creator to a ranked pain/gain. **Deep dive:** Module 2.

<!-- item -->
---
id: north-star
title: North Star Framework
category: Metrics
order: 15
summary: One metric that captures recurring customer value, broken into input drivers with guardrails.
---

```chart
type: tree
title: North Star with inputs (generic)
root:
  label: "North Star: recurring value delivered"
  children:
    - label: "Breadth: how many users get value"
    - label: "Depth: how much value each gets"
    - label: "Frequency: how often"
    - label: "Efficiency / quality: how well"
caption: Inputs are what teams own; guardrails (complaints, refunds, wellbeing) sit beside the tree.
```

**Use when:** aligning several teams on a shared outcome; moving from output to outcome culture. **Don't use when:** a product has distinct, unrelated value streams (use separate goals) or the metric can't be measured reliably yet.

**Worked example (hypothetical):** food app NSM = completed problem-free orders per active customer per month; inputs = activation, order frequency, payment success, on-time delivery; guardrails = refund rate, complaint rate.

**Limitations:** can be gamed (Goodhart's law); one metric never tells the whole story; may need revisiting as strategy changes. **Template:** NSM definition (numerator, denominator, window) · why it reflects value · 3–5 input metrics with owners · 2–3 guardrails · review cadence. **Deep dive:** Module 7.

<!-- item -->
---
id: okrs
title: OKRs (Objectives and Key Results)
category: Strategy
order: 16
summary: A qualitative objective with 2–4 measurable key results; initiatives are bets to move them.
---

```chart
type: layers
title: OKR structure
rows:
  - ["Objective (qualitative direction)"]
  - ["KR1 (metric, baseline → target)", "KR2", "KR3 (guardrail)"]
  - ["Initiative A", "Initiative B", "Initiative C"]
edges:
  - ["Objective (qualitative direction)", "KR1 (metric, baseline → target)"]
  - ["Objective (qualitative direction)", "KR2"]
  - ["Objective (qualitative direction)", "KR3 (guardrail)"]
  - ["KR1 (metric, baseline → target)", "Initiative A"]
  - ["KR2", "Initiative B"]
  - ["KR1 (metric, baseline → target)", "Initiative C"]
caption: Shipping an initiative is not achieving a key result; the KR measures the outcome.
```

**Use when:** quarterly focus and alignment; outcome-based planning. **Don't use when:** as a task list, an individual performance score, or with 10+ objectives.

**Worked example:** O: make checkout trustworthy for first-time buyers. KR1: completion 70% → 76% (new users). KR2: payment-failure recovery 20% → 35%. KR3 (guardrail): complaint rate ≤ 1.3%. Initiatives: early fee display; payment retry.

**Limitations:** sandbagging or unrealistic stretch; metric gaming; overhead. **Template:** Objective · KRs (metric, baseline, target, date, owner) · initiatives · weekly confidence score (0–10). **Deep dive:** Module 2.

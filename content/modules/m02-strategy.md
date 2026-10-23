---
id: m02
n: 2
title: Product Strategy and Strategic Thinking
subtitle: Turn business objectives into focused product choices — markets, positioning, moats, pricing, OKRs and go-to-market.
summary: Vision to roadmap, SWOT/Porter/PESTLE, TAM-SAM-SOM, STP, canvases, moats, Blue Ocean, build-buy-partner, pricing, OKRs and portfolio strategy.
hours: 10
status: drafted
sources: "Lectures 6, 9, 10, 13, 23, 24; Extra topics 1, 2, 5, 8, 9, 10"
---

!!! hypo "About examples"
    Company names appear only as widely known illustrations of a concept. Numbers in worked examples are **hypothetical**. Never quote them as facts about a real business.

## What strategy is (and is not)

**Strategy** is a set of **choices** about where to play (which customers, problems, markets), how to win (why customers pick you over alternatives) and what *not* to do — backed by the capabilities and economics to sustain it. A strategy that does not exclude anything is not a strategy.

!!! level1 "Level 1 · Beginner"
    Strategy answers: *Who are we helping? With what? Why us rather than the alternatives? And how will we know it is working?* A list of features is not a strategy.

!!! source "From your course notes (Lecture 10)"
    Product strategy involves **choices**: whom the product serves, which problem it addresses, why customers would choose it, and how it can achieve business outcomes. Use user research and competitor research to inform those choices. A vision is the future you hope to create; strategy is the choice of whom to serve, which problem to solve and how to win sustainably; a roadmap turns strategic choices into planned outcomes and work. *Test whether the segment actually has the need, then track whether the choice delivers value and supports the business.*

### Vision, mission, strategy, roadmap

| Layer | Question | Time horizon | Example (hypothetical food app) |
|---|---|---|---|
| **Mission** | Why do we exist and what do we do? | Enduring | “Make everyday meals easy and trustworthy.” |
| **Vision** | What future are we trying to create? | 3–10 years | “Nobody is ever surprised by the price of dinner.” |
| **Strategy** | Where do we play and how do we win? | 1–3 years | “Win budget-conscious urban households with transparent total prices and reliable delivery.” |
| **Objectives / OKRs** | What measurable results show progress? | Quarter/year | “Raise checkout completion from 70% to 76% without raising complaints.” |
| **Roadmap** | What outcomes and bets, in what likely order? | Next 2–4 quarters | “Q1 price transparency; Q2 reliability of payments; Q3 repeat-order shortcuts.” |

### Strategy versus roadmap

A **roadmap** is *derived from* strategy; it is not strategy. A strategy says “we will win on trust and price clarity”; the roadmap lists the bets that express it. If a roadmap can be read as a list of unrelated requests, the strategy is missing.

!!! source "From your course notes (Lecture 13; Extra topic 1)"
    A roadmap communicates priorities and direction over time. The class distinguishes a **feature-based** roadmap from a **goal-based** (outcome-based) one. Build it collaboratively with engineering, design, stakeholders and customers; discuss dependencies, capacity, estimates and risks. *It is an evolving plan, not a guarantee.* The lecturer sometimes described vision as unchanging and cross-functional input as unnecessary — in practice strategy and vision can evolve and involvement depends on the organisation.

```chart
type: compare
title: Feature roadmap versus outcome roadmap
headers: ["", "Feature roadmap", "Outcome (goal-based) roadmap"]
rows:
  - ["Lists", "Features with dates", "Problems/outcomes with metrics, grouped Now / Next / Later"]
  - ["Implied promise", "“We will ship X by June”", "“We will try to move metric Y by solving problem Z”"]
  - ["Strength", "Easy to communicate; fits fixed-scope contracts", "Keeps teams focused on results; adapts as you learn"]
  - ["Risk", "Output without outcome; locks in solutions", "Stakeholders may feel dates are missing; needs trust and good metrics"]
  - ["Use when", "Regulatory deadlines, committed integrations", "Most product bets under uncertainty"]
caption: Most mature teams use outcome roadmaps for bets and a short list of committed, date-bound items for obligations.
```

## From business objective to product decision (the cascade)

PMs translate company goals into product choices through a **cascade**. Worked example:

```chart
type: layers
title: Cascade from business objective to a shipped bet (hypothetical)
labels: ["Business", "Product strategy", "Goal (OKR)", "Bet", "Experiment"]
rows:
  - ["Grow profitable orders 20% this year"]
  - ["Win on price transparency for budget-conscious households"]
  - ["KR: checkout completion 70% → 76%; complaints ≤ 1.3%"]
  - ["Show delivery fee early in the cart"]
  - ["A/B test on 10,000 users per arm for 14 days"]
edges:
  - ["Grow profitable orders 20% this year", "Win on price transparency for budget-conscious households"]
  - ["Win on price transparency for budget-conscious households", "KR: checkout completion 70% → 76%; complaints ≤ 1.3%"]
  - ["KR: checkout completion 70% → 76%; complaints ≤ 1.3%", "Show delivery fee early in the cart"]
  - ["Show delivery fee early in the cart", "A/B test on 10,000 users per arm for 14 days"]
caption: Every layer should be traceable upward (why are we doing this?) and downward (how will we test it?). A bet that cannot be linked up the chain is a candidate to drop.
```

**Method:** (1) restate the business objective with a number; (2) diagnose the biggest lever (funnel, cohort, unit economics); (3) choose a segment and problem; (4) define the strategic bet; (5) set outcome metrics and guardrails; (6) pick the cheapest experiment that reduces the biggest risk.

## Market analysis

Market analysis answers: how big, how fast, who competes, what is changing, and where are the gaps. Use **secondary research** (reports, filings, company databases, news) to frame the landscape and **primary research** (interviews, surveys) to learn what customers actually do.

!!! source "From your course notes (Lecture 6)"
    Primary research gathers new evidence directly (interviews, surveys, moderated focus groups); secondary research analyses existing information (reports, articles, company databases such as Crunchbase and Tracxn). Ask an AI research tool a specific question, specify geography, stage and audience, and **open and verify the cited sources and dates.** *The claim that “surveys don't work in India” or that “90% of responses are biased” was not substantiated;* sampling, incentives and question design can introduce bias but do not make surveys invalid.

### Market sizing: TAM, SAM, SOM

* **TAM** — total addressable market: demand if you captured everything your product could serve.
* **SAM** — serviceable available market: the part you can actually serve with your offering, geography and channels.
* **SOM** — serviceable obtainable market: what you can realistically win in a stated period.

Prefer **bottom-up** sizing (users × frequency × price) over “1% of a huge market”.

!!! hypo "Worked example — bottom-up market sizing for a meal-planning app (hypothetical, one city)"
    | Step | Assumption | Value |
    |---|---|---:|
    | Households in the city | assumed | 2,000,000 |
    | Smartphone-using households that order or cook regularly | 60% | 1,200,000 |
    | **TAM** (all of them, annual price ₹1,200) | 1,200,000 × ₹1,200 | **₹144 crore ≈ ₹1.44 billion** |
    | Households within the service area and income band that fit | 25% of 1,200,000 | 300,000 |
    | **SAM** | 300,000 × ₹1,200 | **₹36 crore ≈ ₹360 million** |
    | Realistic capture in year 1 (marketing reach, conversion) | 4% of SAM households | 12,000 |
    | **SOM** | 12,000 × ₹1,200 | **₹1.44 crore ≈ ₹14.4 million** |

    State the unit (₹/year), the time period and each assumption. Then show a low and high case (e.g., 2% and 6% capture → ₹0.72 crore to ₹2.16 crore). The weakest assumption is usually the capture rate — validate it with a pilot.

```chart
type: concentric
title: TAM → SAM → SOM (hypothetical meal-planning app, annual)
rings:
  - ["TAM", "₹144 crore", "All regularly-ordering/cooking smartphone households in the city at ₹1,200/year."]
  - ["SAM", "₹36 crore", "Households in the service area and income band that fit the offering."]
  - ["SOM", "₹1.44 crore", "12,000 households we can realistically win in year one."]
caption: Hypothetical illustration. Circle sizes show nesting, not exact area proportions. TAM/SAM/SOM are estimates under explicit assumptions, not proof of demand.
```

!!! source "From your course notes (Extra topic 8; Lecture 6)"
    A hypothetical city with 100,000 potential users: if 20,000 are in the delivery area and fit the criteria, they may form the serviceable market; if you assume 2,000 could be acquired in a period, document the evidence and constraints. *Avoid multiplying an enormous market by an arbitrary one-percent share without evidence.* The shampoo figures in class were illustrative, not verified. A **unicorn** is a private company valued at $1 billion or more, not one with $1 billion revenue.

## Competitive intelligence

!!! source "From your course notes (Lecture 9)"
    The goal is to understand the market and find meaningful gaps — *not to copy every feature.* **Direct** competitors offer closely comparable solutions to similar users; **indirect** competitors solve the same need differently; **substitutes** compete for the same outcome, time or budget (streaming vs cinema vs games vs sleep). Classification depends on the need being analysed. A different channel can still be a threat (gift buyers choosing a quick-commerce item over waiting for a watch). *Compare the alternatives, not only your own product.*

**Process:** (1) define the customer job; (2) list alternatives incl. “do nothing”, spreadsheets, manual workarounds; (3) compare on a few user-relevant dimensions; (4) record evidence and date; (5) ask “which differences actually matter to customers?”

```chart
type: compare
title: Competitor comparison skeleton (hypothetical student-budgeting app)
headers: ["Dimension", "Our idea", "Bank app tracker", "Spreadsheet", "Messaging a friend / nothing"]
rows:
  - ["Setup time", "5 min", "Already there", "30+ min", "None"]
  - ["Auto-categorises spend", "Yes (planned)", "Yes", "No", "No"]
  - ["Shared budgets with a flatmate", "Yes (planned)", "Rare", "Manual", "Chat"]
  - ["Price", "Free + paid tier", "Free", "Free", "Free"]
  - ["Evidence level", "Hypothesis", "Observed (date: ____)", "Observed", "Interviews"]
caption: Hypothetical. Always fill the evidence row and the date; competitor features change quickly. “Do nothing” is a real competitor.
```

### SWOT

**SWOT** organises **S**trengths and **W**eaknesses (internal) and **O**pportunities and **T**hreats (external). It is a summary tool, not an analysis: each item needs evidence, and the real value is the *so-what* — which strengths address which opportunities, which weaknesses expose which threats.

```chart
type: canvas
title: SWOT for a hypothetical regional food-delivery entrant
cols: 2
cells:
  - {title: "Strengths (internal)", tone: g, text: ["Strong restaurant relationships in 2 cities", "Reliable payments flow (99.5% success, internal data)", "Lean team; fast shipping cadence"]}
  - {title: "Weaknesses (internal)", tone: r, text: ["Small marketing budget", "No loyalty programme yet", "Limited late-night coverage"]}
  - {title: "Opportunities (external)", tone: b, text: ["Rising demand for transparent pricing", "Office-lunch subscriptions", "Partnerships with co-working spaces"]}
  - {title: "Threats (external)", tone: w, text: ["Well-funded incumbents can match promotions", "Delivery-partner cost inflation", "Regulatory change on platform fees"]}
caption: Hypothetical. Convert it into TOWS actions — e.g. (S×O) use restaurant relationships to launch office-lunch subscriptions; (W×T) avoid promo wars where marketing budget is weakest.
```

!!! source "From your course notes (Lecture 9)"
    Support claims with evidence and flag unknowns. *The instructor noted that one group's SWOT described Ola but missed a direct side-by-side competitor comparison.*

### Porter's Five Forces

Porter's Five Forces assesses the structural attractiveness of an industry: **rivalry among existing competitors, threat of new entrants, threat of substitutes, bargaining power of buyers, and bargaining power of suppliers.** High force intensity → lower profit potential.

```chart
type: layers
title: Porter's Five Forces
rows:
  - ["Threat of new entrants"]
  - ["Bargaining power of suppliers", "Rivalry among existing competitors", "Bargaining power of buyers"]
  - ["Threat of substitutes"]
edges:
  - ["Threat of new entrants", "Rivalry among existing competitors"]
  - ["Bargaining power of suppliers", "Rivalry among existing competitors"]
  - ["Bargaining power of buyers", "Rivalry among existing competitors"]
  - ["Threat of substitutes", "Rivalry among existing competitors"]
caption: Rate each force low / medium / high with evidence, then ask which force you can influence (e.g., raise switching costs to reduce buyer power).
```

!!! hypo "Worked example — Five Forces for food-delivery marketplaces (hypothetical, qualitative)"
    | Force | Assessment | Why (illustrative) | Product implication |
    |---|---|---|---|
    | Rivalry | High | Few large players; promotions and speed compete directly | Differentiate beyond discounts (reliability, trust) |
    | New entrants | Medium | Software is easy; supply density and brand are hard | Win density in chosen micro-markets |
    | Substitutes | High | Cooking, offline dining, grocery delivery | Anchor on convenience *and* price clarity |
    | Buyer power | High | Low switching costs for consumers; multi-homing | Build habit loops, loyalty, saved preferences |
    | Supplier power | Medium–high | Restaurants and delivery partners can multi-home | Better tools and fair economics for partners |

    *Limitation:* Five Forces is a static industry snapshot; it ignores complements and fast technology change. Use it to frame, then validate with data.

!!! source "From your course notes (Lecture 24)"
    Porter's Five Forces was announced but **not substantially taught** in the recording; this section is independent reference material.

### PESTLE

**PESTLE** scans the macro environment: **P**olitical, **E**conomic, **S**ocial, **T**echnological, **L**egal, **E**nvironmental.

```chart
type: canvas
title: PESTLE scan — hypothetical fintech lender entering a new market
cols: 3
cells:
  - {title: "Political", text: ["Regulatory stance on digital lending", "Stability of financial policy"]}
  - {title: "Economic", text: ["Interest-rate trend", "Consumer credit demand", "Inflation and income growth"]}
  - {title: "Social", text: ["Trust in digital finance", "Financial literacy", "Mobile-first behaviour"]}
  - {title: "Technological", text: ["Digital KYC and identity infrastructure", "Fraud-detection capabilities", "Open banking APIs"]}
  - {title: "Legal", text: ["Data protection and consent", "Consumer-lending disclosure rules", "Licensing requirements"]}
  - {title: "Environmental", text: ["Paperless onboarding", "Energy footprint of data centres"]}
caption: Hypothetical checklist. Mark each factor as tailwind or headwind, rate impact and certainty, and assign an owner to watch the big ones. Seek qualified legal advice for regulatory interpretation.
```

## Segmentation, Targeting and Positioning (STP)

* **Segment** — divide the market into groups with shared needs/behaviours (not just demographics).
* **Target** — choose which segment(s) to serve first, based on need severity, size, strategic fit, reachability and ability to pay.
* **Position** — define how the product sits in the target's mind relative to alternatives.

!!! source "From your course notes (Lectures 3, 26; Extra topic 9)"
    Segment beyond demographics: package size, affordability, distribution, brand perception, motivations. These are *hypotheses to research, not assumptions that apply to everyone in a place or income group.* **Positioning** explains which users a product serves, the problem it solves and why it may be a better choice than relevant alternatives; competitors include doing nothing, a spreadsheet or asking a person. Validate whether users care about the proposed difference and whether it is accurate before presenting it as fact.

```formula
Positioning statement:
For [target customer] who [need/job],
[Product] is a [category] that [key benefit].
Unlike [primary alternative], [Product] [reason to believe / differentiator].
```

!!! example "Example (hypothetical)"
    For **busy parents** who need predictable weekly food costs, **PlanPlate** is a meal-planning app that shows an accurate weekly grocery estimate. Unlike collecting recipes and prices by hand, PlanPlate does it in one tap — *reason to believe:* price estimates refresh from partner stores daily (to be validated).

### Value propositions

A **value proposition** states the benefit a customer gets and why it beats alternatives. The **Value Proposition Canvas** pairs the **customer profile** (jobs, pains, gains) with your **value map** (products/services, pain relievers, gain creators). Fit exists when your relievers and creators address the pains and gains that matter most.

```chart
type: canvas
title: Value Proposition Canvas (hypothetical meal-planning app)
cols: 2
cells:
  - {title: "Value map · Products & services", tone: b, text: ["Weekly plan generator", "Grocery list with price estimate", "Pantry tracker"]}
  - {title: "Customer profile · Jobs", tone: v, text: ["Feed the family without overspending", "Avoid last-minute takeout", "Reduce food waste"]}
  - {title: "Value map · Pain relievers", tone: b, text: ["Price estimate before shopping", "Use-up-leftovers suggestions"]}
  - {title: "Customer profile · Pains", tone: v, text: ["Surprise grocery bills", "Planning takes 45+ minutes", "Wasted food"]}
  - {title: "Value map · Gain creators", tone: b, text: ["Weekly budget tracker", "One-tap reorder of favourites"]}
  - {title: "Customer profile · Gains", tone: v, text: ["Predictable weekly cost", "Time saved", "Healthier meals"]}
caption: Hypothetical. Fit is a hypothesis until interviews and a smoke test show customers prioritise those pains and gains.
```

## Business models: Business Model Canvas and Lean Canvas

The **Business Model Canvas** (Osterwalder) describes nine building blocks. The **Lean Canvas** (Ash Maurya) adapts it for startups: it replaces Key Partners, Key Activities, Key Resources and Customer Relationships with **Problem, Solution, Key Metrics, Unfair Advantage**.

```chart
type: canvas
title: Business Model Canvas (hypothetical meal-planning app)
cols: 5
cells:
  - {title: "Key partners", rows: 2, text: ["Grocery chains (price feeds)", "Payment gateway", "Recipe creators"]}
  - {title: "Key activities", text: ["Price-data integration", "Recommendation quality", "Customer research"]}
  - {title: "Value propositions", rows: 2, tone: b, text: ["Plan a week in 5 minutes", "Know the cost before you shop"]}
  - {title: "Customer relationships", text: ["Self-serve app", "Email tips; in-app help"]}
  - {title: "Customer segments", rows: 2, tone: v, text: ["Busy parents", "Budget-conscious households"]}
  - {title: "Key resources", text: ["Price database", "Engineering team", "Brand trust"]}
  - {title: "Channels", text: ["App stores", "Parent communities", "Referrals"]}
  - {title: "Cost structure", span: 2, tone: w, text: ["Engineering and data costs", "Price-data licences", "Acquisition spend"]}
  - {title: "Revenue streams", span: 3, tone: g, text: ["Premium subscription (₹1,200/year)", "Affiliate fees from partner grocers (disclosed)"]}
caption: Hypothetical. Fill the canvas in pencil: every cell is an assumption to test, starting with customer segments and value proposition.
```

```chart
type: canvas
title: Lean Canvas (same idea)
cols: 5
cells:
  - {title: "Problem", rows: 2, tone: r, text: ["Weekly meal planning takes too long", "Grocery costs are unpredictable", "Existing alternatives: spreadsheets, notes"]}
  - {title: "Solution", text: ["Auto-plan + price estimate", "Pantry tracker"]}
  - {title: "Unique value proposition", rows: 2, tone: b, text: ["Plan a week of meals with a reliable cost estimate in 5 minutes"]}
  - {title: "Unfair advantage", text: ["Exclusive price feed (to be validated)"]}
  - {title: "Customer segments", rows: 2, tone: v, text: ["Early adopters: budget-conscious parents in one city"]}
  - {title: "Key metrics", text: ["Plans created / week", "Week-4 retention", "Free→paid conversion"]}
  - {title: "Channels", text: ["Parent groups", "Referrals"]}
  - {title: "Cost structure", span: 2, tone: w, text: ["Data licences, engineering, acquisition"]}
  - {title: "Revenue streams", span: 3, tone: g, text: ["Subscription; affiliate"]}
caption: Use the Lean Canvas when you are still searching for a problem–solution fit; use the BMC for an established model with partners and relationships to describe.
```

## Differentiation, competitive advantage and moats

**Differentiation** gives customers a reason to choose you that rivals cannot easily copy. A **competitive advantage** is durable only if it resists imitation; such protective features are often called **moats**.

| Source of advantage | What it means | How it works | Fragility |
|---|---|---|---|
| **Network effects** | Product becomes more valuable as more people use it | Direct (messaging) or cross-side (riders ↔ drivers; buyers ↔ sellers) | Local not global; can reverse; multi-homing weakens it |
| **Switching costs** | Cost (money, time, data, learning) of changing | Integrations, data lock-in, workflows, contracts | Customers resent lock-in; regulators may require portability |
| **Economies of scale** | Unit costs fall with volume | Purchasing, infrastructure, density | Needs sustained volume |
| **Brand and trust** | Customers prefer you under uncertainty | Reliability, safety, reputation | One incident can damage it |
| **Data advantage** | More usage → better model/personalisation | Learning from behaviour | Only if data is proprietary, relevant and used well |
| **Proprietary tech / IP / regulation** | Legal or technical barriers | Patents, licences | Time-limited; can be designed around |
| **Distribution** | Cheap access to customers | Embedded in other products, partnerships | Platform risk |

!!! level3 "Level 3 · Senior PM"
    “Network effects” is an overused claim. Test it: does the *marginal user make existing users better off*, and is that effect strong enough to beat a rival's promotions? In marketplaces, the effect is usually **local** (density in a city), so a global user count hides weakness. Ask what happens if a rival subsidises both sides for a quarter.

### Blue Ocean Strategy

**Blue Ocean Strategy** (Kim & Mauborgne) advises creating uncontested market space by making competition irrelevant, using a **strategy canvas**: plot competitive factors on the x-axis and offering level on the y-axis, then use the **Eliminate–Reduce–Raise–Create** grid to reshape value.

```chart
type: line
title: Strategy canvas — hypothetical "predictable-price" food delivery vs two incumbents
xs: ["Price clarity", "Restaurant variety", "Delivery speed", "Promotions", "Loyalty perks", "Reliability"]
series:
  "Incumbent A": [3, 9, 8, 9, 7, 6]
  "Incumbent B": [4, 8, 8, 8, 6, 6]
  "Our concept": [9, 5, 6, 2, 3, 9]
ylabel: "offering level (1–10)"
ymax: 10
caption: Hypothetical scores for illustration, not research. The concept raises price clarity and reliability, reduces promotions and variety, and so avoids head-on rivalry. Scores must be validated with customer data before use in a decision.
```

## Build, buy or partner

| Option | Choose when | Advantages | Risks |
|---|---|---|---|
| **Build** | Core differentiator; unique requirements; long-term control matters | Control, IP, tailored experience | Slow, costly, maintenance burden |
| **Buy** (license / acquire) | Commodity capability; speed matters; mature vendors exist | Fast, proven | Vendor lock-in, integration cost, ongoing fees, limited customisation |
| **Partner** | Capability sits outside your core; shared upside; distribution access | Faster market access, shared risk | Dependency, revenue share, misaligned incentives |

**Decision questions:** Is it core to our differentiation? How fast do we need it? What is the total cost of ownership over 3 years (including maintenance and vendor fees)? What is the switching cost if the vendor fails? What data and compliance obligations apply? Could we start by buying and later build once learning proves the need?

!!! example "Example (hypothetical)"
    A food-delivery startup considers building its own maps and routing. Verdict: **buy/partner** (commodity, huge fixed cost), and **build** its own order-batching logic because that is where its cost advantage lives.

## Strategic trade-offs

Strategy is about saying no. Typical explicit trade-offs: growth vs profitability; breadth vs depth; speed vs quality; acquisition vs retention; customer-specific requests vs platform consistency; exploit the core vs explore a new bet. A useful practice: write **“We will not…”** statements (e.g., “We will not compete on discount depth; we will compete on transparency and reliability”).

!!! source "From your course notes (Lecture 24, Extra topic 11)"
    For any strategic choice, describe the target, evidence, costs, risks and **what would make you change your mind.** Stakeholders have different incentives; clarify the shared outcome, evidence, constraints and decision rights instead of promising every request.

### Growth options: the Ansoff matrix

!!! source "From your course notes (Lecture 24)"
    Existing product/existing market = **market penetration**; new product/existing market = **product development**; existing product/new market = **market development**; new product/new market = **diversification.** The distinction is relative to the company; examples can be debatable. *The instructor initially gave inconsistent quadrant labels; this is the standard mapping.*

```chart
type: canvas
title: Ansoff matrix with a hypothetical study-app company
cols: 2
cells:
  - {title: "Market penetration (existing product, existing market)", tone: g, text: ["Raise usage among current students with streaks and reminders"]}
  - {title: "Market development (existing product, new market)", tone: b, text: ["Sell the current study app to a new school or country"]}
  - {title: "Product development (new product, existing market)", tone: v, text: ["Add a tutoring service for current users"]}
  - {title: "Diversification (new product, new market)", tone: w, text: ["Launch a career-coaching app for adults"]}
caption: Risk generally increases away from the top-left. Treat each option as a hypothesis to test with evidence.
```

## Pricing and monetisation strategies

* **Pricing** — how much and on what terms customers pay. **Monetisation** — the broader way the product earns revenue.
* Anchor on **value to the customer**, then check cost, competitor prices, willingness to pay and trust. Cost-plus alone ignores value.

| Model | How it works | Best when | Watch out for |
|---|---|---|---|
| **One-time purchase** | Pay once | Simple tools; low ongoing cost | No recurring revenue; support cost continues |
| **Subscription** | Recurring access fee | Ongoing value; predictable costs | Churn; need steady value delivery |
| **Freemium** | Free tier + paid upgrades | Viral/low marginal cost products | Free users cost money; conversion often small — model it |
| **Usage-based** | Pay for consumption | Value scales with use (APIs, cloud) | Unpredictable bills; metering complexity |
| **Tiered** | Good/Better/Best plans | Different segments value different features | Poor tier design confuses or leaves money on the table |
| **Marketplace / transaction fee** | Take rate on transactions | Two-sided platforms | Disintermediation; fee fairness |
| **Advertising** | Advertisers pay for attention | Large audiences | Conflicts with user experience; privacy |
| **Licensing / enterprise** | Per-seat, per-usage or per-deal | B2B with high value | Long sales cycles; custom demands |
| **Affiliate** | Paid for referred outcomes | Content/recommendation products | Trust and disclosure |

!!! source "From your course notes (Lecture 26; Extra topic 5)"
    The class compared subscriptions, freemium, advertising, affiliate, usage-based, licensing and transaction/marketplace models; models can be combined. *Tiered pricing and hybrid monetisation are different but can coexist.* **License fees can be per user, usage-based or otherwise structured; cloud pricing is not universally per seat.** **White-labelling concerns branding another supplier's product; dropshipping concerns fulfilment directly by a supplier — they are not the same.** A free trial should disclose when payment begins and how to cancel. Do not interpret stated willingness to pay as guaranteed purchases. A data product requires appropriate legal, security and privacy protections.

!!! hypo "Worked example — a simple price-test decision"
    Plan A: ₹99/month; Plan B: ₹149/month. In a pilot of 2,000 visitors each: A converts 5.0% (100 payers → ₹9,900/month), B converts 3.5% (70 payers → ₹10,430/month). B earns ₹530 more revenue per month but with 30 fewer customers. If monthly churn is higher for B or support cost per customer is fixed, A may be better long-term; if costs are per user, B wins. The pilot is a signal; it needs a significance check (Module 7) and a view on churn and strategy (market share vs margin).

## Objectives and Key Results (OKRs)

An **objective** is a qualitative direction; **key results** are measurable changes that indicate progress; **initiatives** are the work you believe might move the key results. OKRs are not a task list or an automatic performance score.

```chart
type: compare
title: Good and weak OKR examples (hypothetical)
headers: ["", "Weak", "Better"]
rows:
  - ["Objective", "Improve checkout", "Make checkout trustworthy for first-time buyers"]
  - ["Key result", "Ship fee display", "Increase checkout completion from 70% to 76% for new users by end of quarter while complaint rate stays ≤ 1.3%"]
  - ["Why", "Output, not outcome", "Measurable baseline, target, population and guardrail"]
  - ["Initiative", "—", "Early fee display; payment retry; remove one form field"]
caption: If the release happens but completion does not improve, the initiative shipped but the key result has not been achieved.
```

**Tips:** 3–5 objectives max; 2–4 KRs each; stretch but plausible (many teams aim for ~70% achievement on ambitious KRs); review weekly; separate committed deliverables from aspirational goals; pair outcomes with guardrails.

## Product portfolio strategy

Larger organisations manage **multiple products** and must allocate resources across them.

* **BCG growth-share matrix** — classifies products by market growth and relative market share into **Stars** (high/high), **Cash cows** (low growth/high share), **Question marks** (high growth/low share) and **Dogs** (low/low). It guides investment but oversimplifies and depends on how markets are defined.
* **Three Horizons** — H1 optimise the core, H2 build emerging businesses, H3 explore future options; allocate effort and expectations differently (the commonly cited “70/20/10” split is a rule of thumb, not a law).
* **Portfolio questions:** Which products share customers or infrastructure? Where do we cannibalise ourselves? Which should we sunset to free capacity?

```chart
type: scatter
title: Hypothetical product portfolio — growth vs relative share (bubble = revenue)
points:
  - {label: "Core app", x: 1.6, y: 6, size: 24, group: "Cash cow"}
  - {label: "Subscription", x: 0.9, y: 18, size: 14, group: "Star"}
  - {label: "Grocery delivery", x: 0.5, y: 22, size: 11, group: "Question mark"}
  - {label: "Legacy loyalty", x: 0.3, y: 3, size: 7, group: "Dog"}
xlabel: "Relative market share (1.0 = leader)"
ylabel: "Market growth (%/yr)"
xmax: 2
ymax: 25
quad: ["Question marks", "Stars", "Dogs", "Cash cows"]
caption: Hypothetical values. The quadrant boundaries (relative share 1.0, growth ~12%) are a convention; the real work is the investment decision for each product.
```

## Go-to-market (GTM) strategy

GTM is the plan for getting a product to the right people and helping them use it. Module 8 covers launch plans in depth; here are the strategic pieces.

!!! source "From your course notes (Lecture 23; Extra topic 10)"
    GTM is the plan for reaching and serving a market — for a new product, an existing product entering a new market, or another launch. **Start with the business case and timing** (why now, who benefits, market conditions, seasonality, competition). **Define the audience and proposition** (personas, positioning, differentiators, messaging, pricing and rationale). **Plan distribution and launch support** (channels, sales and support readiness, onboarding, budget, owners). Set measurable success metrics and adjust the roadmap using feedback. In the cricket-equipment exercise, the instructor challenged learners to consider *partner incentives, sponsorship costs and likely return — not just list channels.* Pilot with a small group before a public launch; assign owners and a rollback owner.

```chart
type: steps
title: GTM strategy in six questions
steps:
  - ["Why now?", "Business case, timing, readiness"]
  - ["Who?", "Segments, personas, use cases"]
  - ["What promise?", "Positioning, value proposition, messaging"]
  - ["How priced?", "Model, price points, rationale"]
  - ["Which channels?", "Direct, partner, community, paid, product-led"]
  - ["How measured?", "Success metrics, review cadence, owners"]
caption: Answer in order; each answer constrains the next. A launch is not the finish line — plan for learning and adjustment.
```

## Strategy in practice: a worked mini-case

!!! example "Hypothetical: choosing a segment for a budgeting app"
    **Context.** A small team can build one thing this quarter. Three candidate segments: students, young professionals, freelancers.
    **Evidence (hypothetical).** 12 interviews per segment; pain severity (1–5): students 4.1, young professionals 3.2, freelancers 4.5. Estimated serviceable users: students 200k, professionals 500k, freelancers 80k. Reachability: students via campus (high), professionals (medium), freelancers via communities (medium). Willingness to pay (stated; to be validated): ₹0, ₹100/month, ₹250/month.
    **Scoring (1–5 scores, weights: pain 35%, size 20%, reach 20%, willingness to pay 25%).** Pain is the interview score above; the other criteria are converted to 1–5 — size: students 3, professionals 5, freelancers 1; reach: 5, 3, 3; willingness to pay: 1, 3, 5. Students: 4.1×.35 + 3×.2 + 5×.2 + 1×.25 = 1.435 + 0.6 + 1.0 + 0.25 = **3.29**. Professionals: 3.2×.35 + 5×.2 + 3×.2 + 3×.25 = 1.12 + 1.0 + 0.6 + 0.75 = **3.47**. Freelancers: 4.5×.35 + 1×.2 + 3×.2 + 5×.25 = 1.575 + 0.2 + 0.6 + 1.25 = **3.63**.
    **Decision.** Start with **freelancers** (pain and willingness to pay are highest) while the small serviceable base is acceptable for a first version; plan a second wave for professionals. **Risks:** small market; stated willingness to pay is unreliable — test with a priced pilot. **What would change our mind:** if pilot conversion is below 3% or if freelancers churn after tax season.

## Source-flagged corrections

* Strategy ≠ roadmap ≠ vision; they are layers.
* Ansoff labels: see above.
* Five Whys and first principles are related but different (Module 4).
* A survey preference is not proof of purchase; PMF needs behavioural evidence.
* Segmenting by largest size alone does not prove fit.

## Exercises with model answers

!!! question "Exercise 1 · Size a market"
    Estimate the annual SOM for a language-learning app in one city: 3,000,000 residents; 40% aged 18–40; 20% of those would consider paying for an app; annual price ₹2,000; you believe you can win 5% of the considering users in year one. Show TAM, SAM, SOM and name the shakiest assumption.

??? answer "Model answer"
    Residents aged 18–40: 3,000,000 × 0.40 = 1,200,000. Considering payers: 1,200,000 × 0.20 = 240,000. **SAM (users who would consider)**: 240,000 → ₹2,000 × 240,000 = ₹48 crore. Taking TAM as all 18–40 residents = 1,200,000 × ₹2,000 = **₹240 crore**. **SOM**: 5% × 240,000 = 12,000 users → **₹2.4 crore**. Shakiest assumption: the 5% capture rate (and the 20% “would consider” which is stated intent). Run a landing-page test with a real price to refine both. Present a range (3%–7% → ₹1.44–3.36 crore).

!!! question "Exercise 2 · Positioning"
    Write a positioning statement for a budgeting app for freelancers, naming the alternative it competes with.

??? answer "Model answer (example)"
    For **freelancers** who struggle with irregular income, **IncomeSmooth** is a budgeting app that forecasts cash flow across months. Unlike spreadsheets and bank apps that assume a fixed salary, IncomeSmooth builds a safe monthly allowance from your average income and warns you before tax and low-income months. Reason to believe: forecasts use the user's own 12-month history (to be validated with beta users).

!!! question "Exercise 3 · Build, buy or partner"
    A fintech wants in-app identity verification. Recommend and justify.

??? answer "Model answer"
    **Buy/partner** with an established KYC provider: identity verification is regulated, commodity-like and expensive to build and maintain; speed to market matters. Retain control of the onboarding UX and data handling, check vendor compliance and uptime SLA, plan for vendor switching (abstraction layer), and review data-protection obligations. Revisit building in-house only if unit cost at scale or differentiation justifies it.

## Interview perspective

??? question "“What is your product strategy for X?” — structure"
    1. Clarify the company goal and stage. 2. Choose the segment and the problem (with evidence). 3. State the positioning and why you win (differentiation/moat). 4. Name the top 2–3 bets and *what you won't do.* 5. Define the North Star, outcome metrics and guardrails. 6. Highlight biggest risks and how you'd test them. 7. Note what evidence would change your mind. Keep it to 2–3 minutes before drilling down.

??? question "“How would you decide between building and partnering?” — 60-second answer"
    “I start with whether it's core to differentiation. If it's commodity or regulated, I lean to buy or partner for speed and lower risk, and compare three-year total cost, vendor lock-in, data/compliance obligations and the cost of switching later. If it's what makes us different — like our routing logic — I build. I'd often start with a partner to learn, keep a clean abstraction layer, and revisit once volume or differentiation justifies building.”

## Key takeaways

* Strategy = **choices** (who, what, why us, what not). Roadmaps follow strategy.
* Use frameworks (**SWOT, Five Forces, PESTLE, STP, canvases**) to *organise thinking*, then validate with evidence.
* Size markets **bottom-up**, show a range and name the weakest assumption.
* Moats are specific: network effects, switching costs, scale, brand, data — test each claim.
* **Price on value**, check unit economics, and run price tests with significance and churn in view.
* OKRs: objective (direction) + measurable key results + guardrails; not a task list.
* Always write down **what would change your mind.**

## Check your understanding

```quiz
- q: "Which best describes a roadmap?"
  options:
    - "A guarantee of dates for specific features"
    - "A communicated plan of outcomes and likely work, derived from strategy"
    - "The company's mission statement"
    - "A list of all customer requests"
  answer: 1
  why: "A roadmap communicates priorities and direction over time; it is evolving and follows strategy."
- q: "In the Ansoff matrix, selling the current product to a new market is…"
  options:
    - "Market penetration"
    - "Product development"
    - "Market development"
    - "Diversification"
  answer: 2
  why: "Existing product + new market = market development."
- q: "Which sizing approach is preferred?"
  options:
    - "1% of a huge market"
    - "Bottom-up: users × frequency × price, with a range"
    - "The biggest number you can cite"
    - "Competitor revenue only"
  answer: 1
  why: "Bottom-up estimates expose assumptions you can test. Arbitrary percentages of a giant market are not evidence."
- q: "A strong network effect exists when…"
  options:
    - "Many people have downloaded the app"
    - "Each additional user makes the product more valuable for existing users, enough to resist rivals"
    - "The product is popular on social media"
    - "The company has many partners"
  answer: 1
  why: "Network effects mean marginal users add value to others; they are often local and can be weakened by multi-homing."
- q: "Which is a well-formed key result?"
  options:
    - "Launch the new checkout"
    - "Improve conversion"
    - "Increase checkout completion from 70% to 76% for new users this quarter, complaints ≤ 1.3%"
    - "Make the team happy"
  answer: 2
  why: "A key result has a baseline, target, population, time frame and often a guardrail."
- q: "Which is a substitute rather than a direct competitor?"
  options:
    - "Another food-delivery app"
    - "Cooking at home instead of ordering"
    - "A rival's identical subscription"
    - "A copy-cat app with same features"
  answer: 1
  why: "Substitutes meet the same need (a meal) in a different way and compete for the same outcome, time or budget."
```

## Recommended resources

* [Strategyzer: Business Model Canvas](https://www.strategyzer.com/library/the-business-model-canvas) and [Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas).
* [Harvard Business Review: The Five Competitive Forces That Shape Strategy](https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy) (Michael Porter).
* [Blue Ocean Strategy — official site](https://www.blueoceanstrategy.com/).
* [Lean Canvas (Ash Maurya)](https://leanstack.com/lean-canvas).
* [Atlassian: Product management](https://www.atlassian.com/agile/product-management) — roadmap and strategy guides.
* [What Is OKR? — Google re:Work](https://rework.withgoogle.com/guides/set-goals-with-okrs/steps/introduction/).

## Product-market fit: definitions and how to measure it

!!! source "From your class deck (Week 8 · Product Launch, Growth and Monetisation)"
    The deck compares four well-known ideas of product-market fit (PMF): a compelling value hypothesis for a cohort that truly values it; building something people want (a "deep well" of users who badly have the problem); a problem worth solving plus a solution that solves it well enough; and users who love it so much they tell others. It measures PMF with retention, referral and revenue signals, and shows the "how would you feel if you could no longer use it?" survey with a 40% benchmark.

| View | Core idea | What to check |
|---|---|---|
| **Value hypothesis** | A specific group of customers values what you offer | Can you name the group and what they would pay or switch for? |
| **Build what people want** | Look for a small group with a deep, urgent problem | Are a few people extremely happy, or many mildly interested? |
| **Problem-market fit, then problem-solution fit** | First prove the problem matters, then that your solution works | Which of the two are you testing right now? |
| **Love and word of mouth** | Users recommend it without being paid to | Organic referrals, waitlists, unprompted praise |

**Why growth alone is a weak signal:** paid growth can hide poor retention. Investors and teams who dig into retention numbers soon see whether the product really fits.

### Measuring PMF

| Signal | Evidence of fit | Warning sign |
|---|---|---|
| **Retention** | Curves flatten for at least one cohort | Curve slides to zero |
| **Referral** | High NPS, organic invites, viral coefficient near or above 1, a waiting list | All growth is paid |
| **Revenue** | Strong free-to-paid conversion, revenue growing without heavy discounts | Heavy discounting to close |
| **Survey** | At least 40% say they would be "very disappointed" without the product | Most say "somewhat disappointed" or "not disappointed" |

### A process for improving PMF (the "supporter segmentation" approach)

1. **Segment the "very disappointed" supporters** and find what they have in common (role, use case, industry). Describe the ideal high-expectation customer.
2. **Read feedback from the on-the-fence group** to learn what stops them from becoming supporters.
3. **Build a roadmap in two halves:** deepen what supporters already love, and fix what the on-the-fence users miss. Use simple cost-benefit scoring.
4. **Repeat each quarter** and treat the PMF score as a headline metric. One widely cited example reported lifting the supporter share from about 22% to about 58% with this loop.

!!! warning "Do not treat 40% as a law"
    The 40% line is a rule of thumb from one survey method. Use it with retention and revenue evidence, and with enough responses (at least 40 to 100 from active users).

## MVP: learning at the lowest cost

!!! source "From your class deck (Week 8)"
    An MVP is the version that gets the most learning for the least effort. It is not a low-quality product and not just a list of the cheapest features. The deck contrasts building a final product in one go with building parts that validate hypotheses on the way, and shows how to define an MVP by listing and prioritising hypotheses and choosing inexpensive tests.

### How to define an MVP in four steps

1. **List the hypotheses** that must be true: problem-market fit (is this a real, frequent problem?) and problem-solution fit (will this solution work and be used?).
2. **Prioritise** the riskiest, most important hypotheses first.
3. **Choose the cheapest test for each:** existing data, user research, a landing page, a concierge or manual service, a wizard-of-oz prototype, an AI-built prototype, or a small cohort release.
4. **Ship, measure, decide:** set the success metric and threshold before you start, then continue, change or stop.

| Test type | Cost | Strength of evidence |
|---|---|---|
| Existing data or desk research | Very low | Weak to medium |
| Interviews and surveys | Low | Medium (people say, not do) |
| Landing page or fake door | Low | Medium to strong (real behaviour) |
| Manual or concierge version | Medium | Strong |
| Coded prototype to a small cohort | Higher | Strongest |

!!! hypo "Worked example · an AI dish recommender for a food-delivery app (hypothetical)"
    Idea: suggest what to order for users who cannot decide.
    | Hypothesis | Cheapest test | Success metric |
    |---|---|---|
    | Many users struggle to choose | Look at time from open to order and abandoned sessions; add a small "Can't decide?" prompt and count taps | Share of users tapping the prompt |
    | Users will accept outside suggestions | Show "top 5 ordered nearby" and an LLM chat suggestion | Acceptance rate of suggestions |
    | Users will like personalised picks | Run a model only for heavy users (50+ orders) at dinner time | Share who accept and then order |
    Start with the narrowest cohort where the model is likely to work, then widen.

!!! warning "Common MVP mistakes"
    Calling a broken product an MVP; building many features instead of one riskiest test; no success threshold; ignoring that the cost of building has fallen with AI tools, which makes smaller, faster tests possible.

## Experimentation: causation, A/B design and biases

!!! source "From your class deck (Week 8)"
    Correlation can mislead (ice-cream sales and sunstroke both rise in summer). A/B experiments apply randomised controlled testing to establish cause and effect. Steps: form a hypothesis (population, treatment, outcome metric), decide sample size, create random groups, run the test. The deck adds bias warnings, a sanity (A/A) test, and a four-part experimentation framework: define hypotheses, define the minimum viable test, prioritise tests, analyse results.

| Step | What to do | Watch out for |
|---|---|---|
| **Hypothesis** | "For [population], changing [treatment] will change [outcome metric] because [reason]" | Keep the treatment minimal so you know what caused the change |
| **Sample size** | Larger when the expected effect is small, the metric is noisy, or you want stricter confidence (p-value 0.05 is common) | Stopping early when the number looks good |
| **Random groups** | Assign users by chance and keep the groups comparable | Sample not representative (one city), allocation depending on earlier behaviour, treated and control users interacting in a social product |
| **Run** | Run long enough to cover weekly cycles | Seasonality, novelty effects |
| **Guardrails** | Watch metrics that must not get worse (latency, complaints, refunds) | Winning the primary metric but hurting trust |

**Sanity (A/A) test:** show two groups the same experience, or change something irrelevant such as a settings page, and check that outcome metrics do not move significantly. It proves the setup is sound before the real test.

**How to need fewer users:** test a larger change, choose a more sensitive leading metric, narrow the population to a segment with high variance explained, or use more precise methods such as CUPED where your data team supports them.

!!! hypo "Worked example · discount for new restaurants (hypothetical)"
    *Hypothesis:* new-restaurant discount codes will raise 30-day orders per user among users who ordered in the past 60 days. *Population:* eligible active users in two cities. *Treatment:* a Rs 75 discount on the first order from a restaurant listed in the last 30 days. *Outcome:* orders per user; guardrails: average order value, contribution margin, repeat orders from regular restaurants (cannibalisation). *Biases to avoid:* only testing in one city, assigning the offer to users who browsed new restaurants (self-selection), and group contamination through referral codes.

### Experimentation framework for a team

1. Write well-structured hypotheses around key problems.
2. Turn each into a **minimum viable test** (the smallest valid experiment).
3. **Prioritise** tests by impact, confidence and effort; keep a backlog.
4. **Analyse and archive** results so learning compounds, including failed tests.

## Scaling: expansion, distribution and early customers

!!! source "From your class deck (Week 8)"
    The deck presents a product-market expansion grid, a map of distribution channels (direct, ecosystem, partnerships) and playbooks for acquiring early customers for consumer and business products.

### Product and market expansion grid

| | **Existing market / customers** | **New market / customers** |
|---|---|---|
| **Existing product** | Deepen: grow share, usage and frequency (lowest risk) | Expand: adjacent geographies, segments, languages |
| **New product** | Add product lines for current customers | Diversify (highest risk) |

Choose moves that use your **strategic assets**: brand, technology, data, customer base, operations, team.

!!! example "Worked example · an online retailer's expansion path"
    First books for existing online shoppers (current product, current customers) → more categories after perfecting operations (adjacent customers) → an open seller marketplace (new product, adjacent customers) → renting out its own cloud infrastructure (new product, new customers). Each step reused a strength: logistics, customer base, then engineering scale.

!!! example "Worked example · a social network's expansion path"
    One university first, then other universities, then schools and workplaces (adjacent markets that were easy to seed), then the general public. Later it added groups, messaging and a marketplace to deepen engagement before an enterprise version.

### Distribution channels

| Type | How it works | Examples |
|---|---|---|
| **Direct** | You control sales and delivery | Self-serve website or app, company sales team for enterprises, direct-to-consumer stores |
| **Ecosystem** | Others bring customers to you | App stores and marketplaces, resellers and system integrators, affiliates and influencers |
| **Partnerships** | Your product is built into someone else's | Pre-installed apps (OEM), API partners (a maps API inside a delivery app), telecom bundles (a video subscription inside a data plan) |

Pick channels by customer behaviour, deal size and cost to serve: low-price products need low-touch channels; high-price products can afford sales teams.

### Acquiring the first customers

| | Consumer products | Business (B2B) products |
|---|---|---|
| **Start with** | Friends, communities, niche forums, a launch on product-hunt-style sites, creators | Founder-led outreach, warm introductions, design partners |
| **Offer** | Early-access invite, waitlist, referral perks | Free pilot with success criteria, discounted founding-customer plan |
| **Learn** | Cohort retention, qualitative feedback | Time to first value, security and procurement blockers |
| **Do not** | Spend heavily on ads before retention is proven | Customise endlessly for one customer |

## Product-led growth in depth

!!! source "From your class deck (Week 8)"
    PLG means self-serve entry, fast time to value, growth through loops and sales that assists later. It changes how sales, marketing, customer success and operations work, and its advantages include efficiency, a stronger growth engine, lower acquisition cost and quicker time to value. The deck distinguishes viral, user-generated-content and hook loops, and shows how loops combine into a flywheel.

### PLG across the company

| Function | What changes |
|---|---|
| **Sales** | Focuses on **product-qualified leads (PQLs)**: accounts that hit usage thresholds (for example a team nearing its free limit) |
| **Marketing** | Uses user-generated content, in-product communities, branded shareable output, viral content |
| **Customer success and support** | Mostly self-serve help; proactive messages at moments of confusion or risk |
| **Operations** | Product usage data drives operations, for example order data helping a delivery service promise short delivery times |

### Why teams choose PLG

* **Organisational efficiency:** every function works through the product, which forces alignment (a famous messaging app served hundreds of millions of users with a very small team, mostly engineers).
* **Stronger growth engine:** a siloed funnel leaks; a sales promise the product cannot keep leads to churn.
* **Lower CAC:** the product sells and onboards, so acquisition cost drops.
* **Faster time to value:** tailored onboarding gets users to the "aha" quickly.

### Growth loops

A **loop** is a closed system: an input goes through steps, produces an output, and that output feeds the next input. Loops compound; funnels do not.

| Loop | How it works | Example |
|---|---|---|
| **Viral / referral** | Users invite others inside the product; the invitee becomes a user who invites more | Referral bonus on both sides; "invite your contacts" prompts |
| **User-generated content (UGC)** | Users create content that search or social shares bring new visitors to | Reviews, posts, templates, public profiles |
| **Retention (hook) loop** | Trigger → action → variable reward → investment | Feed: open, scroll, find something interesting, like and follow, which tunes the feed |
| **Paid loop** | Revenue funds acquisition that brings more revenue | Works only if payback is short |

### Growth flywheel

A **flywheel** stacks several loops so momentum builds. Example for a marketplace: better customer experience → more customers → more sellers → more choice → better experience; and a second loop: more customers → lower unit cost → lower prices → better experience → more customers.

!!! hypo "Worked example · PLG ideas for a food-delivery product (hypothetical)"
    * **Viral loop:** group ordering with split payment, where each invited friend becomes a user.
    * **UGC loop:** dish photos and reviews that surface in search.
    * **Hook loop:** a weekly "tonight's picks" notification, with taps tuning future picks.
    * **Cross-functional:** support uses live order data to message customers before they complain; operations uses demand data to staff kitchens and riders.
    * **Metrics:** invites per user, invite acceptance, k-factor, time to first order, repeat rate.

## Revenue models

!!! source "From your class deck (Week 8)"
    A **revenue model** describes how money flows from customers to the business; a **pricing model** describes how much to charge. A product can have several of each, one per user type. The deck covers transaction, subscription and advertising models, plus data and API, donations and the razor-and-blades model.

| Family | Variants | Works well when | Example |
|---|---|---|---|
| **Transaction** | Direct sale; fee or commission | Purchases are infrequent or high value | Phones, marketplaces, accommodation platforms |
| **Subscription** | Fixed tier; variable (usage-based); freemium | Value is recurring | Streaming tiers; cloud pay-as-you-go; productivity suites |
| **Advertising** | CPM (per 1,000 impressions), CPC (per click), CPA (per action) | Very high volume of attention | Search, video and social platforms |
| **Data and API** | Data licensing; API access fees | You own valuable data or a capability | Financial data providers; maps and messaging APIs |
| **Donations or crowdfunding** | Voluntary support | Open-source and non-profit | Encyclopaedias, open-source projects |
| **Razor and blades** | Cheap device, profitable consumable | Repeat consumables | Printers and ink |
| **Hybrid** | Mix of the above | Different users value different things | Marketplace: commission + ads + subscription for sellers |

**How to choose:** (1) define the value for each customer group and whether they would pay; (2) understand usage patterns: one-time, regular, irregular; (3) pick the model that fits the pattern and supports the strategy; (4) test it with a small group before committing.

!!! example "Worked example · revenue models for a navigation product (hypothetical)"
    | User | Model | Why |
    |---|---|---|
    | Consumers | Advertising (in maps and search) | Frequent, high-volume use; their data also improves the product |
    | Local businesses | Freemium subscription | Value shows quickly in a free tier; premium tools for visibility |
    | Vehicle makers | Licence or subscription | One-time integration deals, recurring features |
    | Developers | Usage-based API pricing with a free tier | Cost scales with calls; free tier drives adoption |

## Pricing models and tactics

!!! source "From your class deck (Week 8, appendix)"
    The deck groups pricing models into value-based, cost-based, competitive, psychological and dynamic pricing, plus pay-what-you-want.

| Model | Idea | Variants and examples | Use when |
|---|---|---|---|
| **Value-based** | Price from perceived value and willingness to pay | **Premium** (signal quality), **skimming** (high at launch, then lower), **good-better-best** tiers, **value-added** extras (seat choice, priority support) | Differentiated or specialised products |
| **Cost-based** | Cost plus markup | **Full-cost** (all costs, unit profit) vs **direct-cost** (variable only, profit at scale) | High-volume, price-sensitive goods; ignores willingness to pay |
| **Competitive** | Based on rivals | **Penetration** (low entry price or first-order discount), **parity** (match rivals), **loss leader** (sell below cost to win other purchases) | New entrants, crowded markets; avoid prolonged predatory use |
| **Psychological** | Shape perception | **Charm** (99 instead of 100), **anchor** (high-priced option makes others look fair), **decoy** (a weaker option that makes another look better), **bundle** | Retail and subscriptions; avoid gimmicks |
| **Dynamic** | Prices move with conditions | **Surge** (demand and supply), personalised pricing (ethical and legal risks) | Limited inventory, lopsided demand |
| **Pay what you want** | Customer chooses | Tips and fan support; donation-style models | Creators, non-profits, secondary revenue |

!!! warning "Ethics and trust"
    Personalised pricing based on device or personal traits can feel unfair and may breach consumer rules. Dynamic pricing needs transparency (show why), caps in emergencies, and regular review of effects on loyalty.

!!! hypo "Worked example · choosing price tiers (hypothetical)"
    A note-taking app offers Free, Pro (Rs 199 a month) and Team (Rs 499 per user per month). Pro is highlighted as "most popular" (anchor on Team), the annual plan is two months free (bundle and commitment), and the free tier has a cap that heavy users hit within weeks (value-based). Track free-to-paid conversion, downgrade rate and revenue per user, and test price points on new sign-ups only.


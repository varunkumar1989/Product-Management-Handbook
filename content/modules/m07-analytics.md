---
id: m07
n: 7
title: Product Analytics and Metrics
subtitle: Choose the right metrics, calculate them correctly, run experiments you can trust, and turn data into decisions.
summary: KPIs, funnels, retention, unit economics, A/B testing statistics, instrumentation, SQL/Excel and dashboards — with formulas, worked data and charts.
hours: 12
status: drafted
sources: "Lectures 21, 25, 26, 27, 31, 34, 35; Companion ch. 5, 6, 9; Extra topics 3, 4, 6, 7; class deck: Analytics and Metrics"
---

!!! hypo "About the data in this module"
    Every number is **hypothetical or synthetic**. Hand-worked examples use round numbers so you can follow the arithmetic. SQL examples run against the synthetic files in `datasets/` (`users.csv`, `events.csv`, `orders.csv`, …) and every output shown was produced by actually running the query. None of it is real company data, and no benchmark here should be quoted as an industry norm.

## Product analytics fundamentals

**Product analytics** is the practice of measuring how people use a product so that teams can find problems, size opportunities, test changes and verify outcomes.

!!! level1 "Level 1 · Beginner"
    A metric is a number that describes something about your product. Analytics is choosing the *right* numbers, calculating them the *same way every time*, and using them to decide what to do next.

Every useful metric needs five parts defined — otherwise two people will calculate it differently and argue:

```formula
Metric definition = event/population  +  numerator  +  denominator  +  time window  +  exclusions
Example: Checkout completion = users who placed an order ÷ users who started checkout,
         same 7-day window, excluding internal test accounts and bots.
```

```chart
type: steps
title: From product behaviour to decision
steps:
  - ["Question", "What decision are we trying to make?"]
  - ["Metric", "Define numerator, denominator, window, exclusions"]
  - ["Instrument", "Track the events; test in staging"]
  - ["Analyse", "Segment, compare, check data quality"]
  - ["Decide & learn", "Act, then re-measure and record the learning"]
caption: Start from the decision, not from the data you happen to have. Dashboards that answer no decision become wallpaper.
```

!!! source "From your course notes (Lecture 21)"
    Define what is being measured, for whom and over what period, and compare against a relevant baseline or target. Users and revenue alone are not sufficient measures of every product's success. **Correlation alone does not prove that a change caused an outcome.** If an outcome misses its target, check data quality, user feedback, usability and context before removing a feature; revisit a metric when it no longer measures the intended outcome — not merely to make results look better.

## Choosing KPIs

A **KPI** (key performance indicator) is a metric chosen to assess progress toward an important goal. Not every metric is a KPI.

| Concept | Meaning | Example (food ordering) |
|---|---|---|
| **Leading indicator** | Early signal that predicts a later result; you can influence it quickly | Share of new users who place a first order within 7 days |
| **Lagging indicator** | Result that confirms what already happened | 90-day retention, quarterly revenue |
| **Input metric** | A driver the team directly controls | Payment success rate, time-to-first-order |
| **Output / outcome metric** | The result the inputs are meant to move | Orders per active customer |
| **Guardrail metric** | Must not get worse while you optimise something else | Complaint rate, refund rate, cancellation rate |
| **Vanity metric** | Looks good, drives no decision | Total registered users (all time) |

### The North Star Metric and metric trees

A **North Star Metric (NSM)** is a single measure of the recurring value users get from the product that also supports sustainable business results. It focuses teams; it never replaces guardrails.

!!! source "From your course notes (Extra topic 3)"
    A north star is a team's chosen measure of recurring value delivered, not a universal number. A **metric tree** breaks a high-level outcome into smaller drivers so a team can investigate changes. Pair it with guardrails such as refunds and delivery complaints. *A single metric never tells the entire story.* Do not claim causality merely from a breakdown.

```chart
type: tree
title: Metric tree for a food-ordering product (hypothetical)
root:
  label: "North Star: completed, problem-free orders per active customer per month"
  children:
    - label: "Active customers"
      children:
        - label: "New customers activated"
        - label: "Returning customers"
    - label: "Order frequency"
      children:
        - label: "Cart-to-order conversion"
        - label: "Repeat-order interval"
    - label: "Problem-free rate"
      children:
        - label: "Payment success rate"
        - label: "On-time delivery rate"
caption: Each branch is a lever a team can own. Guardrails (refunds, complaints, cancellations) sit beside the tree. "Problem-free" must be defined precisely, e.g. no refund and no complaint within 48 hours.
```

**How to choose an NSM — a checklist**

1. Does it reflect value *delivered to the user* (not just value captured by the company)?
2. Is it tied to a repeatable behaviour (not a one-off)?
3. Is it sensitive enough that a good team can move it in a quarter?
4. Can it be measured reliably today?
5. Does it predict long-term business health (retention, revenue)?
6. Can you name two guardrails that stop gaming it?

!!! level3 "Level 3 · Senior PM"
    NSMs fail when they become targets without guardrails (Goodhart's law): optimising “time in app” can produce addictive design and wellbeing harm. Senior PMs pressure-test an NSM by asking *“how could a team hit this number while harming users or the business?”* and add the guardrail that blocks that path. They also revisit the NSM when strategy or product stage changes.

## AARRR (Pirate Metrics)

AARRR examines the path from discovering a product to recommending it: **Acquisition → Activation → Retention → Revenue → Referral.**

```chart
type: steps
title: AARRR with example metrics
steps:
  - ["Acquisition", "How do people find us? Visits, sign-ups, CAC by channel"]
  - ["Activation", "First meaningful value: first order placed within 7 days"]
  - ["Retention", "Do they return? Week-N retention of a signup cohort"]
  - ["Revenue", "How do we earn? Orders, AOV, ARPU, contribution margin"]
  - ["Referral", "Do they bring others? Invites sent, referral-sourced signups"]
caption: Stages can run in parallel, and the order is not a company-stage sequence. AARRR is a diagnostic lens, not a substitute for product-specific definitions.
```

!!! source "From your course notes (Lecture 25)"
    - **Activation** should be an early action showing meaningful value — *first payment is only one example*; the right event depends on the product.
    - **Retention** can mean returning or continuing to receive value; recurring subscription payment is one example, not the only one.
    - Funnel arithmetic: if **800 of 1,000** visitors complete a step, conversion is **80%** and drop-off **20%**. If **600 of 800** return, retention is **75%** and loss **25%**.
    - **Churn** needs a defined starting group, behaviour and time period; non-payment alone does not mean every free user has churned.
    - The lecture's “20–30% ideal activation” and one-to-one referral claims are **not universal benchmarks**.
    - Analytics shows *where* behaviour changes; interviews and tests help explain *why*.

### Acquisition and activation

* **Acquisition metrics:** visits, sign-ups, installs, cost per acquisition by channel, share of traffic by channel. Always compare channels on *quality* (activation and retention), not just volume.
* **Activation:** pick an event that **correlates with long-term retention** *and* represents real value. Test it by comparing retention of users who did vs did not reach it — remembering correlation is not causation (see below).
* **Time-to-value:** how long from sign-up to the activation event. Shortening it usually raises activation.

!!! example "Worked example · defining activation (hypothetical)"
    For a reading app, candidate events: *signed up*, *opened a book*, *finished a first chapter*, *read on 3 different days in week one*. The team compares 4-week retention of users who did each. Hypothetically, “finished a first chapter” predicts retention far better than “opened a book,” so it becomes the activation event. The next step is an *experiment* to see if nudging users toward finishing a first chapter actually improves retention — not an assumption.

## Funnel analysis and drop-off

A **funnel** counts how many distinct users (or sessions) get through an ordered series of steps. **Step conversion** compares each step with the previous one; **overall conversion** compares with the top.

```formula
Step conversion  = users at step n ÷ users at step n−1
Drop-off         = 1 − step conversion
Overall conversion = users at last step ÷ users at first step
```

!!! hypo "Hypothetical worked funnel (10,000 visits)"
    | Step | Users | Step conversion | Drop-off | % of top |
    |---|---:|---:|---:|---:|
    | Visits | 10,000 | – | – | 100% |
    | Menu viewed | 6,200 | 62.0% | 38.0% | 62.0% |
    | Added to cart | 2,480 | 40.0% | 60.0% | 24.8% |
    | Checkout started | 1,736 | 70.0% | 30.0% | 17.4% |
    | Order placed | 1,388 | 80.0% | 20.0% | 13.9% |

    Interpretation: the **largest absolute loss** is visit → menu (3,800 users) and the **lowest step conversion** is menu → cart (40%). The best place to investigate is not automatically the biggest percentage drop; weigh how fixable each step is and how many users it affects.

```chart
type: funnel
title: Checkout funnel (hypothetical, 10,000 visits)
stages: [["Visits", 10000], ["Menu viewed", 6200], ["Added to cart", 2480], ["Checkout started", 1736], ["Order placed", 1388]]
caption: Hypothetical numbers. Percentages on the right are relative to the previous step. A steep step is a prompt to investigate, not a diagnosis.
```

!!! source "From your course notes (Companion ch. 5)"
    Of 300 checkout starters, 240 complete: **80% completion, 20% abandonment.** Cart-to-order of 240 ÷ 400 = **60%**. These use different starting populations, so *their percentages should not be mixed.*

**Funnel pitfalls**

* **Sessions vs users:** counting sessions can inflate steps for repeat visitors. State which one you use.
* **Strict vs loose order:** must a user hit steps in order, within X minutes?
* **Time window:** a user who adds to cart today and buys tomorrow — is that a conversion?
* **Segmenting is essential:** an overall funnel can hide that mobile-web users convert at half the rate of app users.

!!! tip "Interview perspective — “Checkout conversion dropped. What do you do?”"
    1. Clarify the metric definition and window. 2. Check data quality (tracking change? outage?). 3. Segment: platform, app version, geography, payment method, new vs returning, channel. 4. Compare to seasonality. 5. Look at internal changes (releases, price/fee, promo, partner outage) and external ones (competitor, holiday). 6. Form hypotheses, rank by likelihood × impact, propose the first checks. Always say what you would look at *first* and why.

## Engagement: DAU, WAU, MAU and stickiness

```formula
DAU = distinct users with a qualifying action on a given day
WAU / MAU = same over a 7-day / 28–30-day window
Stickiness = DAU ÷ MAU   (average DAU over the period ÷ MAU for the same period)
```

“Active” must mean a *meaningful* action (e.g., viewed a menu or placed an order), not merely “opened the app”.

!!! hypo "Worked example"
    Average DAU = 12,000; MAU = 48,000 → **stickiness = 25%** — on average a monthly user is active about 7.5 days a month (0.25 × 30). Whether 25% is good depends entirely on how often the product's job occurs: a banking app opened monthly differs from a messaging app used daily.

```chart
type: line
title: DAU and MAU trend (hypothetical, thousands)
xs: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
series:
  "MAU (k)": [40, 42, 44, 46, 48, 51]
  "Avg DAU (k)": [9.2, 10.1, 10.9, 11.5, 12, 13.3]
ylabel: "users (thousands)"
caption: Hypothetical. Stickiness (DAU ÷ MAU) moves from 23% in January to 26% in June — engagement is deepening, not just growing.
```

## Retention, cohorts and churn

**Retention** measures how many users in a defined **cohort** are still active in a later window. A cohort groups users by a shared starting event (e.g., signup week).

```formula
Retention (week k) = cohort users active in week k ÷ cohort size
Churn rate (period) = customers lost during the period ÷ customers at start of the period
Net revenue retention (NRR) = (start MRR + expansion − contraction − churned MRR) ÷ start MRR
```

!!! source "From your course notes (Extra topic 4)"
    Of 100 users who signed up in week one, 25 order again in a specified later seven-day window → **25% for that window.** Users who ordered on day one but never returned are not “retained” unless your definition says so. State cohort start, qualifying action, time zone and exact return window. A correlation between activation and retention does not prove the activation action causes retention.

### Reading a cohort heatmap

The heatmap below uses the **synthetic dataset** `cohort_retention_weekly.csv`: each row is a signup-week cohort; each column is the share of that cohort that placed a delivered order *k weeks after signup*.

```chart
type: heatmap
title: Weekly cohort ordering rate (synthetic dataset)
rows: ["Wk 1 (n=51)", "Wk 2 (n=67)", "Wk 3 (n=50)", "Wk 4 (n=54)", "Wk 5 (n=75)", "Wk 6 (n=74)"]
cols: ["Week 0", "Week 1", "Week 2", "Week 3", "Week 4"]
matrix:
  - [17.6, 7.8, 11.8, 3.9, 3.9]
  - [11.9, 13.4, 4.5, 9.0, 4.5]
  - [14.0, 12.0, 2.0, 4.0, 6.0]
  - [13.0, 9.3, 11.1, 1.9, 7.4]
  - [10.7, 8.0, 4.0, 8.0, 8.0]
  - [18.9, 5.4, 6.8, 5.4, 1.4]
vmax: 25
rowhead: "Signup cohort"
caption: Synthetic data. Darker = higher share ordering. Read across for one cohort's decay; read down a column to see whether newer cohorts retain better. With cohorts of 50–75 users, one or two users move a cell by 2–4 points — noise is large, so avoid over-reading differences.
```

**How to read it:** (1) *Across a row* — the shape of decay and whether it flattens. (2) *Down a column* — are newer cohorts better after a product change? (3) *Diagonals* show calendar effects (holiday, outage). Small cohorts produce noisy cells.

!!! warning "Retention pitfalls"
    * **Survivorship:** averaging only active users hides churn.
    * **Mixed definitions:** “active” in Week 1 vs “ordered” in Week 1.
    * **Blended cohorts:** comparing a fresh paid-ads cohort to an organic one without segmenting.
    * **Small samples:** see the caption above.

## Monetisation metrics: GMV, AOV, ARPU, ARPPU

```formula
GMV  = Σ value of orders in the period (define: before/after discounts, refunds, cancellations)
AOV  = total order value ÷ number of orders (same definition, same period)
ARPU = revenue in the period ÷ active users in the period
ARPPU = revenue in the period ÷ paying users in the period
```

!!! source "From your course notes (Lecture 31)"
    **AOV** = total order value ÷ number of orders for a chosen period; it does not by itself measure profit or user happiness. Example: ₹200, ₹300, ₹400 → ₹900 ÷ 3 = **₹300**. Compare similar customers; check discounts and delivery costs; **a higher AOV alone does not prove improved profitability or experience.**

!!! hypo "Worked example — GMV is not revenue"
    A marketplace processes 100,000 delivered orders at an AOV of ₹400 → **GMV ₹40,000,000**. The platform's *net revenue* is only what it keeps: commission, fees, ad income less the discounts it funds. Quoting GMV as “revenue” inflates the picture.

!!! hypo "Worked example — ARPU vs ARPPU"
    Revenue ₹2,400,000; monthly active users 48,000; paying users 9,600.
    ARPU = 2,400,000 ÷ 48,000 = **₹50**. ARPPU = 2,400,000 ÷ 9,600 = **₹250**. Payer conversion = 9,600 ÷ 48,000 = **20%**. Note ARPU = payer conversion × ARPPU (0.20 × 250 = 50). A freemium PM can raise ARPU by converting more users *or* by raising what payers spend — different levers, different risks.

### Decomposing AOV (the quick-commerce case)

```formula
AOV = items per order × average price per item
```

To raise AOV, a team can raise items per order (relevant add-on suggestions, bundles, free-delivery thresholds) or price per item (assortment, premium options). The course case compared a quick-commerce AOV with a competitor's.

```chart
type: tree
title: Issue tree for "Why is our AOV lower than a competitor's?" (hypotheses, not findings)
root:
  label: "AOV gap"
  children:
    - label: "Fewer items per order"
      children:
        - label: "Weak cart recommendations"
        - label: "Delivery-fee threshold set too low or unclear"
    - label: "Lower price per item"
      children:
        - label: "Assortment skews cheap"
        - label: "Customer-mix difference"
    - label: "Measurement differences"
      children:
        - label: "Different AOV definition"
        - label: "Discounts treated differently"
caption: Every leaf is a hypothesis to test with data. Start with definitions (the cheapest cause to rule out), then segment baskets by customer type.
```

!!! source "From your course notes (Lecture 31)"
    Participants discussed fee thresholds, inexpensive add-ons, near-expiry discounts, bundles and loyalty rewards. **These were hypotheses, not validated causal findings.** Check contribution margin, discount and delivery costs, conversion, repeat purchase and customer trust — not AOV alone. Assess whether each idea genuinely helps customers rather than encouraging unwanted spending.

## Unit economics: contribution margin, CAC, LTV, payback

**Unit economics** looks at the money earned and spent for *one unit* — an order, a customer, a subscription.

```formula
Contribution margin = revenue − variable costs attributable to the unit
CAC       = acquisition spend ÷ new customers acquired (define which costs)
LTV (simple) = monthly contribution per customer ÷ monthly churn rate
Payback period = CAC ÷ monthly contribution per customer
```

!!! hypo "Worked example — contribution per order"
    | Line | ₹ per order |
    |---|---:|
    | Average order value | 400 |
    | Commission (20% of AOV) | 80 |
    | Delivery fee collected | 30 |
    | Platform fee | 5 |
    | **Platform revenue per order** | **115** |
    | Delivery partner cost | −70 |
    | Payment processing (2% of AOV) | −8 |
    | Support cost allocation | −6 |
    | Promotion funded by the platform | −15 |
    | **Contribution per order** | **16** (4.0% of AOV; 13.9% of revenue) |

    Without the ₹15 promotion, contribution would be ₹31. If the promotion lifts orders by less than the contribution it burns, it destroys value. *More orders at negative contribution make the business worse.*

```chart
type: bar
title: From order value to contribution (hypothetical ₹ per order)
cats: ["Platform revenue", "Delivery cost", "Payment fees", "Support", "Promotion", "Contribution"]
series:
  "₹ per order": [115, 70, 8, 6, 15, 16]
fmt: inr
caption: Revenue of ₹115 less four costs (₹70 + ₹8 + ₹6 + ₹15 = ₹99) leaves ₹16. Bars for costs are shown as positive magnitudes.
```

!!! source "From your course notes (Extra topics 6, 7)"
    Contribution margin is *not* net profit. With ₹100 revenue and ₹65 attributable cost, contribution is ₹35 (35%); with a ₹15 promotion it falls to ₹20. Campaign example: ₹10,000 spent to acquire 100 qualified customers → simple **CAC ₹100**; at ₹40 contribution per month, simple undiscounted **payback is 2.5 months** *only if that contribution persists and other costs are excluded.* Avoid blindly copying LTV-to-CAC benchmarks.

!!! hypo "Worked example — LTV, CAC and payback"
    Monthly contribution per paying customer ₹120; monthly churn 5%; CAC ₹800.
    LTV (simple) = 120 ÷ 0.05 = **₹2,400**. LTV : CAC = 2,400 ÷ 800 = **3.0**. Payback = 800 ÷ 120 = **6.7 months**.
    Sensitivity: if churn is 8% instead of 5%, LTV = 120 ÷ 0.08 = ₹1,500 and the ratio falls to **1.9** — churn is the lever the whole calculation hangs on. Real LTV models discount future cash and use cohort retention curves rather than a constant churn.

!!! level3 "Level 3 · Senior PM"
    Executives care about **payback period** and **cash** as much as LTV : CAC, because LTV is a forecast while cash is real. Present base, low and high scenarios, state which costs are in CAC (paid media only vs fully loaded), and show how sensitive the answer is to churn and to retention flattening. Never present a precise LTV to two decimals from three months of data.

## Experiment design and A/B testing

An **A/B test** randomly assigns eligible users to **control** (current experience) and **variant** (change), then compares a pre-agreed metric. Random assignment is what makes the groups comparable, so differences can be attributed to the change.

```chart
type: steps
title: A/B test lifecycle
steps:
  - ["Hypothesis", "We believe [change] will improve [metric] for [users] because [reason]"]
  - ["Design", "Unit of randomisation, eligibility, primary metric, guardrails, MDE"]
  - ["Size & plan", "Sample size, duration (full weekly cycles), stop rule"]
  - ["Run & monitor", "Check assignment balance and data quality; do not peek-and-stop"]
  - ["Analyse & decide", "Effect size, confidence interval, guardrails, segments, cost"]
caption: Decide the metric, duration and guardrails before launch. The most common failure is deciding afterwards.
```

!!! source "From your course notes (Lecture 27, Companion ch. 6)"
    - A/B testing compares variants against a defined outcome; it differs from alpha/beta release testing.
    - Specify hypothesis, target users, control and treatment, primary metric, guardrails, sample requirements and duration; randomly assign eligible users; compare rates using consistent definitions.
    - Choose the **unit of randomisation** and make sure one person is not repeatedly switching groups. Compare **completed orders per eligible user, not just clicks.**
    - A higher observed conversion is not automatically a reliable winner: consider uncertainty, sample size, practical impact, implementation cost, accessibility, safety and compliance.
    - **A preference poll is not an A/B test.** Confidence level does not mean the probability a variant will work, and no test proves safety with 100% certainty.
    - If traffic is too low, run usability research or a different appropriately sized test instead of claiming proof.

**When not to A/B test:** too little traffic; irreversible or safety/legal changes; strong network effects (a marketplace treatment can contaminate control — consider geo or switchback tests); changes whose value only appears over months.

## Hypothesis testing, p-values and confidence intervals

### The idea

* **Null hypothesis (H₀):** there is **no real difference** between control and variant.
* **Alternative (H₁):** there is a difference.
* **p-value:** if H₀ were true, how often would you see a difference *at least this large* purely by chance? It is **not** the probability that the variant works, and it does not measure the size or importance of the effect.
* **Significance level α:** the threshold you fix in advance (commonly 0.05). If p < α, you reject H₀.
* **Confidence interval (CI):** a range of effect sizes consistent with the data; a 95% CI is produced by a procedure that captures the true effect in 95% of repeated experiments. It tells you *how big* the effect might be.

!!! hypo "Fully worked example — early fee display"
    Control: 10,000 eligible users, 7,000 complete an order (**70.0%**). Variant (fee shown early): 10,000 users, 7,250 complete (**72.5%**).

    **Step 1 — difference:** 72.5% − 70.0% = **+2.5 percentage points** (relative lift 2.5 ÷ 70 = 3.6%).

    **Step 2 — pooled proportion:** p̂ = (7,000 + 7,250) ÷ 20,000 = 0.7125.

    **Step 3 — standard error (pooled):** SE = √[ p̂(1 − p̂) × (1/10,000 + 1/10,000) ] = √(0.7125 × 0.2875 × 0.0002) = **0.006401**.

    **Step 4 — test statistic:** z = 0.025 ÷ 0.006401 = **3.906**.

    **Step 5 — p-value (two-sided):** p ≈ **0.00009** → far below 0.05, so we reject H₀.

    **Step 6 — 95% CI for the difference** (unpooled SE = 0.006398): 0.025 ± 1.96 × 0.006398 = **[+1.25, +3.75] percentage points.**

    **Decision:** the effect is statistically distinguishable from zero and the plausible range is positive. Check the guardrail: complaints were 118 vs 121 per 10,000 users (1.18% vs 1.21%) — no meaningful change. Then ask about practical significance: is +1.2 to +3.8 points of completion worth the cost of shipping and maintaining the change? (Dataset: `ab_test_checkout.csv`.)

```chart
type: normal
title: The observed z = 3.91 falls far inside the rejection region
z_crit: 1.96
observed: 3.91
caption: If there were truly no difference, a z-statistic this extreme would be very rare (p ≈ 0.00009). Shaded tails = α = 0.05 (two-sided).
```

```formula
Two-proportion z-test
  p̂ = (x₁ + x₂) / (n₁ + n₂)
  SE = √[ p̂ (1 − p̂) (1/n₁ + 1/n₂) ]
  z = (p₂ − p₁) / SE
  95% CI for difference = (p₂ − p₁) ± 1.96 × √[ p₁(1−p₁)/n₁ + p₂(1−p₂)/n₂ ]
```

!!! source "From your course notes (Lecture 27)"
    The classroom example compared **23/100 with 37/100** and showed how a stricter significance threshold changes the conclusion. Check it: p̂ = 0.30, SE = √(0.3 × 0.7 × 0.02) = 0.0648, z = 0.14 ÷ 0.0648 = **2.16**, two-sided **p ≈ 0.031.** That is significant at α = 0.05 but **not at α = 0.01** — the same data, a different threshold, a different conclusion. With only 100 users per arm, the 95% CI is very wide (about +1.4 to +26.6 points), so the data is also consistent with a small effect. *Statistical significance is not a guarantee, and a small sample gives imprecise estimates.*

### Type I and Type II errors, and power

| | H₀ true (no real effect) | H₀ false (real effect) |
|---|---|---|
| **Reject H₀** (“we found an effect”) | **Type I error** (false positive), probability α | Correct — probability = **power** (1 − β) |
| **Do not reject H₀** | Correct | **Type II error** (false negative), probability β |

* **Power** is the probability of detecting a real effect of a given size. Conventional target: **80%**.
* **MDE (minimum detectable effect)** is the smallest effect worth detecting; smaller MDE → much bigger sample.

### Sample size

```formula
n per arm = (z_{1−α/2} + z_{power})² × [ p₁(1−p₁) + p₂(1−p₂) ] ÷ (p₂ − p₁)²
α = 0.05 two-sided → z = 1.96;  power 80% → z = 0.8416
```

!!! hypo "Worked example — sizing the checkout test"
    Baseline 70%; we care about detecting +2 points (72%). n = (1.96 + 0.8416)² × [0.70×0.30 + 0.72×0.28] ÷ 0.02² = 7.849 × 0.4116 ÷ 0.0004 ≈ **8,077 users per arm.**
    Other MDEs (same baseline, α = 0.05, power 80%): +1 point needs ≈ **32,600 per arm**; +5 points needs ≈ **1,250 per arm.** Halving the MDE roughly quadruples the sample.

```chart
type: line
title: Power to detect a +2-point lift (70% → 72%) by sample size per arm
xs: ["500", "1,000", "2,000", "4,000", "6,000", "8,077", "12,000"]
series:
  "Power": [10.3, 16.5, 28.6, 50.5, 67.5, 80.0, 92.7]
ylabel: "power (%)"
fmt: pct
ymax: 100
caption: Computed from the normal approximation. Below ~8,000 users per arm, a real +2-point effect is more likely missed than found. Running underpowered tests wastes time and teaches teams false lessons.
```

### Practical rules for trustworthy experiments

* **Fix the sample size or use a sequential method designed for peeking.** Stopping the moment p < 0.05 inflates false positives (the “peeking problem”).
* **Run full weekly cycles** to cover weekday/weekend behaviour.
* **Check sample ratio mismatch (SRM):** if you planned 50/50 and observed 52/48 with large counts, assignment may be broken and results untrustworthy.
* **Pre-register one primary metric;** treat others as secondary. Testing many metrics or segments without correction creates false positives (multiple comparisons).
* **Separate statistical from practical significance.** A tiny, “significant” lift may not justify the cost; a larger, “non-significant” one may merit a bigger test.
* **Novelty effects:** an early lift may fade. Where stakes are high, hold out a group longer.

!!! tip "Interview perspective"
    “How would you know if an A/B result is real?” → fixed hypothesis and metric; adequate power; random assignment verified; check guardrails and SRM; look at the CI, not just the p-value; consider practical impact, cost and risk; and if traffic is too low, use qualitative research or a longer or larger test.

## Correlation versus causation

Two things moving together does not mean one causes the other. Causes of misleading correlation: **confounding** (a third factor drives both), **reverse causation**, **selection bias**, and **Simpson's paradox**.

!!! hypo "Worked example — Simpson's paradox from an unbalanced split"
    A team compares two checkout designs but, due to a faulty rollout, the variant gets mostly desktop traffic.

    | Segment | Control (conv / users) | Variant (conv / users) |
    |---|---|---|
    | Desktop (high converting) | 60 / 200 = **30.0%** | 232 / 800 = **29.0%** |
    | Mobile (low converting) | 64 / 800 = **8.0%** | 15 / 200 = **7.5%** |
    | **Overall** | 124 / 1,000 = **12.4%** | 247 / 1,000 = **24.7%** |

    The variant looks **twice as good overall** yet is **slightly worse in both segments.** The overall gap comes from the *traffic mix*, not the design. The cure is correct randomisation (and segment-aware analysis), not trusting the aggregate.

!!! source "From your course notes (Lecture 21; Extra topic 4)"
    Correlation alone does not prove causation. A relationship between activation and retention may be useful but does not prove the activation action *causes* retention. To test causality, run an experiment.

## Segmentation in analytics

Always ask “for whom?” Useful cuts: acquisition channel, platform/app version, geography, new vs returning, plan/tier, cohort, device class, behavioural segments (power users vs casual). Use the synthetic data to see it:

```chart
type: hbar
title: Share of signups that became buyers, by acquisition channel (synthetic dataset)
items: [["Organic (n=370)", 38.4], ["Search ads (n=130)", 37.7], ["Referral (n=106)", 30.2], ["Paid social (n=194)", 26.3]]
fmt: pct
caption: Synthetic data. Channels with high volume are not necessarily high quality; compare conversion and, in real life, retention and CAC before reallocating spend. These are small samples; do not generalise.
```

## Event instrumentation and data quality

**Instrumentation** is adding tracking so product behaviour becomes data. Do it from a **tracking plan** written *before* development.

| Event name | Fires when | Key properties | Owner |
|---|---|---|---|
| `checkout_started` | User opens the checkout screen | `cart_value`, `item_count`, `platform` | Checkout team |
| `fee_displayed` | A delivery fee/estimate is shown | `fee_amount`, `is_estimate`, `source` | Pricing |
| `payment_attempted` | User taps Pay | `method`, `amount` | Payments |
| `payment_succeeded` / `payment_failed` | Gateway responds | `method`, `error_code` (no card data) | Payments |
| `order_placed` | Backend confirms the order | `order_id`, `amount` | Orders |

A well-formed event (illustrative):

```json
{
  "event": "checkout_started",
  "timestamp": "2026-03-14T18:22:05+05:30",
  "anonymous_id": "a1b2-c3d4",
  "properties": { "cart_value": 520, "item_count": 3, "platform": "ios" }
}
```

**Data quality checklist**

* **Naming convention** (`object_action`, snake_case) and a single owner of the schema.
* **Test in staging** before release; compare dashboard totals with the authoritative system (orders table).
* **Deduplicate** (retries, double fires) and **handle bots/internal traffic.**
* **Time zones** and clock skew: define the reporting zone.
* **Late and lost events:** mobile events batch and can arrive late; define a lag window.
* **Privacy:** minimise personal data; never put card details, emails or phone numbers into analytics events; honour consent and retention rules.

!!! source "From your course notes (Lecture 35; Companion ch. 9)"
    **Do not send personal identifiers such as email addresses or phone numbers to Google Analytics** — privacy and platform rules apply. Request a tracking plan before development, test events in staging, compare dashboards with the authoritative order system, minimise personal data, limit access, honour retention rules, and never send card details to an analytics event. Decide what you want to learn **before** setting up the tool; low use alone is not enough reason to remove a feature.

## SQL for Product Managers

Many PM interviews and day-to-day questions need basic SQL. These queries run against the synthetic dataset (`users`, `events`, `orders`). They use portable SQL; date functions differ by database (SQLite uses `strftime`, PostgreSQL uses `DATE_TRUNC`, BigQuery uses `DATE_TRUNC` / `FORMAT_DATE`).

!!! source "From your course notes (Lecture 34)"
    Relational databases organise data in tables of rows and columns; SQL lets an authorised user select, filter and combine data. `SELECT * FROM Customers WHERE Country='UK' AND City='London'` — `AND` requires both conditions, `OR` either. Check whether **cancelled orders, time zones or missing values** change the answer, and do not expose personal details unnecessarily. *Contrary to a claim in the lecture, many PMs do query data and some interviews test SQL or joins.*

**1 · Basics: GMV, AOV and counts (delivered orders only)**

```sql
SELECT COUNT(*)                 AS delivered_orders,
       SUM(amount_inr)          AS gmv_inr,
       ROUND(AVG(amount_inr),2) AS aov_inr
FROM orders
WHERE status = 'delivered';
```

Result: `320 | 122874 | 383.98`. (GMV here excludes cancelled orders — a definition you must state.)

**2 · Cancellation rate**

```sql
SELECT COUNT(*) AS orders,
       SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled,
       ROUND(100.0 * SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2) AS cancel_pct
FROM orders;
```

Result: `334 | 14 | 4.19`.

**3 · Monthly active buyers and GMV (GROUP BY)**

```sql
SELECT strftime('%Y-%m', order_date) AS month,
       COUNT(DISTINCT user_id)       AS active_buyers,
       SUM(amount_inr)               AS gmv_inr
FROM orders
WHERE status = 'delivered'
GROUP BY month
ORDER BY month;
```

Result: `2026-01 | 55 | 23128`, `2026-02 | 107 | 45400`, `2026-03 | 136 | 54346`.

**4 · Funnel by distinct users**

```sql
SELECT event_name, COUNT(DISTINCT user_id) AS users
FROM events
GROUP BY event_name
ORDER BY users DESC;
```

Result: app_open 792 → view_menu 716 → add_to_cart 423 → checkout_start 322 → payment_success 284.
Step conversions: 716/792 = 90.4%, 423/716 = 59.1%, 322/423 = 76.1%, 284/322 = 88.2%. *This counts users who ever reached a step, so it is not a strict ordered funnel.*

**5 · JOIN: which acquisition channels produce buyers?**

```sql
SELECT u.acquisition_channel,
       COUNT(DISTINCT u.user_id) AS users,
       COUNT(DISTINCT o.user_id) AS buyers,
       ROUND(100.0 * COUNT(DISTINCT o.user_id) / COUNT(DISTINCT u.user_id), 1) AS buyer_pct
FROM users u
LEFT JOIN orders o ON o.user_id = u.user_id AND o.status = 'delivered'
GROUP BY u.acquisition_channel
ORDER BY buyer_pct DESC;
```

Result: organic 370/142 (38.4%), search_ads 130/49 (37.7%), referral 106/32 (30.2%), paid_social 194/51 (26.3%). *A LEFT JOIN keeps users with no orders; an INNER JOIN would silently drop them and overstate conversion.*

**6 · Repeat purchase (subquery)**

```sql
SELECT COUNT(*) AS buyers,
       SUM(CASE WHEN n >= 2 THEN 1 ELSE 0 END) AS repeat_buyers,
       ROUND(100.0 * SUM(CASE WHEN n >= 2 THEN 1 ELSE 0 END) / COUNT(*), 1) AS repeat_pct
FROM (SELECT user_id, COUNT(*) AS n
      FROM orders WHERE status = 'delivered' GROUP BY user_id);
```

Result: `274 | 44 | 16.1`.

**7 · Window function: rank customers by spend**

```sql
SELECT user_id, SUM(amount_inr) AS spend,
       RANK() OVER (ORDER BY SUM(amount_inr) DESC) AS rnk
FROM orders WHERE status = 'delivered'
GROUP BY user_id
ORDER BY rnk
LIMIT 5;
```

Result: U0648 (1,229), U0483 (1,210), U0246 (1,160), U0665 (1,040), U0751 (1,039).

**SQL habits PMs should build:** state the metric definition in a comment; check row counts before and after JOINs (duplicates inflate sums); filter to the right status; be explicit about time zones; never `SELECT *` on personal data; sanity-check totals against an authoritative dashboard.

??? answer "Practice: write the query (answers)"
    *Q: Average discount per delivered order?* `SELECT ROUND(AVG(discount_inr),2) FROM orders WHERE status='delivered';`
    *Q: GMV by city, highest first?* `SELECT city, SUM(amount_inr) AS gmv FROM orders WHERE status='delivered' GROUP BY city ORDER BY gmv DESC;` — Result: Mumbai 40,089; Delhi 34,279; Bengaluru 34,022; Pune 14,484.
    *Q: Users who started checkout but never paid?* Use `checkout_start` users minus `payment_success` users (e.g. `NOT IN` or `LEFT JOIN … WHERE p.user_id IS NULL`).

## Excel for product analytics

Excel is enough for quick funnels, cohorts and A/B maths.

| Task | Formula |
|---|---|
| Step conversion | `=C3/C2` |
| AOV | `=SUM(Amount)/COUNT(OrderID)` |
| Conditional sum / count | `=SUMIFS(Amount, Status,"delivered", City,"Mumbai")`, `=COUNTIFS(Status,"cancelled")` |
| Retention % | `=ActiveInWeek/CohortSize` |
| z for two proportions | `=(p2-p1)/SQRT(pp*(1-pp)*(1/n1+1/n2))` where `pp=(x1+x2)/(n1+n2)` |
| Two-sided p-value | `=2*(1-NORM.S.DIST(ABS(z),TRUE))` |
| Pivot table | Insert → PivotTable: rows = channel, values = count of orders, average of amount |
| Lookup | `=XLOOKUP(user_id, Users[user_id], Users[city])` |

Build a **tracking sheet** per experiment: hypothesis, dates, n, conversions, z, p, CI, guardrails, decision. It doubles as a decision log.

## Dashboards and tools: Power BI, Mixpanel, Amplitude, GA4

| Tool | Best for | Notes |
|---|---|---|
| **Mixpanel / Amplitude** | Event-based **product analytics**: funnels, retention, cohorts, user paths, segmentation, often with experimentation add-ons | Needs a good tracking plan; self-serve for PMs |
| **Google Analytics 4 (GA4)** | Web/app traffic and acquisition; events with parameters; “key events” (formerly called conversions) | Do not send personal identifiers; sampling and thresholds can apply to reports |
| **Power BI** | Business dashboards over many sources (SQL, Excel, APIs) with a data model and DAX measures | Good for exec reporting; refresh schedule and access control matter |
| **SQL + notebooks** | Custom analysis, joins, reproducible work | Needs data access and review |
| **Spreadsheet** | Fast calculations and small tests | Easy to break silently; document formulas |

!!! source "From your course notes (Lecture 35)"
    The instructor demonstrated setting up an analytics property and web data stream, adding a tracking tag and viewing recent users and page activity. Compare activity across pages and time periods but **validate definitions, data quality and sample size** before deciding what to change. **Reconcile metric definitions when reports disagree.** Setup screens change; follow current official documentation.

**A simple Power BI measure** (DAX), to show the idea:

```text
Conversion Rate = DIVIDE( DISTINCTCOUNT(Orders[user_id]), DISTINCTCOUNT(CheckoutStarts[user_id]) )
```

**Dashboard design rules:** start with the decision; one headline metric per question; show the trend *and* the target; include definitions and “last refreshed”; put guardrails next to the metric they protect; avoid pie charts for more than 3–4 parts; annotate releases and incidents.

## Experiment readout template (worked example)

!!! example "Readout: Early fee display (hypothetical)"
    **Decision requested:** Ship early fee display to 100% of users? **Recommendation:** Yes, with a 5% holdout for 4 weeks.
    **Hypothesis:** Showing the delivery fee in the cart (not only at payment) will increase checkout completion by reducing surprise.
    **Design:** randomised by user; 10,000 eligible per arm; 14 days; primary = completed orders ÷ eligible users; guardrails = complaint rate, payment failures, AOV.
    **Result:** 70.0% → 72.5% (+2.5 pts; 95% CI +1.25 to +3.75; z = 3.91; p < 0.001). Complaints 1.18% vs 1.21% (n.s.). No SRM detected (10,000 vs 10,000).
    **Segments (exploratory, not powered):** directionally positive on new and returning users.
    **Risks / caveats:** novelty effect possible; estimate accuracy depends on the fee service; two-week window.
    **Next steps:** staged rollout; monitor the estimate error rate; re-run on high-fee cities.

## Source-flagged corrections

* The lecture's *20–30% “ideal” activation* and referral claims are not universal benchmarks.
* A single page-load time cannot by itself establish API latency; browser rendering, network and other components also contribute.
* A **preference poll is not an A/B test**; **confidence level is not the probability a variant will work.**
* A confidence interval is not a probability statement about a single experiment's true value (frequentist interpretation).
* **GMV ≠ revenue ≠ profit.** Define each.

## Metric anatomy and the mental model for product metrics

!!! source "From your class deck (Week 6 · Analytics and Metrics)"
    A metric is a quantifiable measure of success or failure against a goal; the important few are KPIs. Every metric has four parts: **definition, value, time grain and cohort**. Good metrics link what users want to what the business wants. The deck's mental model: identify users and stakeholders → find each one's job to be done → pick metrics that show the job is done → pick metrics that show support for the business goal → add guardrail metrics.

### The four parts of any metric

| Part | Question | Example |
|---|---|---|
| **Definition** | What exactly is counted or measured? | "Orders completed and not cancelled within 24 hours" |
| **Value** | What is the number? | 18,400 |
| **Time grain** | Over what period? | Per day, per week, 4 weeks after sign-up |
| **Cohort** | For which slice of users? | New users in Pune who signed up in March |

A metric written without all four parts ("retention is 40%") cannot be compared or trusted. Always ask: *40% of whom, measured when, counting what?*

### A five-step mental model

1. **List users and stakeholders.** A product often has several (creators, viewers, advertisers).
2. **Write each group's job to be done** in one sentence.
3. **Choose a metric that shows the job is done** for that group (user value metric).
4. **Choose a metric that shows support for the business goal** (revenue, growth, cost), tied to the company's mission or profit goal.
5. **Add guardrail (counter) metrics** that catch harm from over-optimising: for example watch time up but session-ending complaints up.

!!! example "Worked example · a short-video product (hypothetical numbers)"
    | Stakeholder | Job to be done | User value metric | Business metric |
    |---|---|---|---|
    | Creator | Build a following | Followers gained per month, reach per post | Creators posting weekly |
    | Viewer | Find fun, relatable videos | Watch time per session, shares and saves | Daily active viewers, ad impressions |
    | Advertiser | Reach the right people | Cost per qualified action | Ad revenue |
    **Guardrails:** overall time spent outside the product, reports and blocks per 1,000 videos, complaint rate, creator churn.

!!! example "Worked example · a maps and navigation product (hypothetical)"
    *Scope first:* focus on drivers and local businesses; tourists, government and developers are out of scope for this exercise.
    * **Drivers:** job = reach the destination by the fastest, safest route. Metric = share of trips completed on an optimal route (a scorecard of time, traffic, tolls and road quality). A simpler proxy: share of trips cancelled or rerouted.
    * **Local businesses:** job = be found and turn visits into sales. Metric = place visits and calls, directions requests, website clicks.
    * **Company:** advertising and subscription revenue from merchants.
    * **Input → output chains:** road disruptions reported correctly → share of optimal routes; businesses who claim their profile → profile interactions → place visits.

When a goal is vague ("lead a good life", "make users happy") no single metric works. Break the goal into parts and measure each.

## The ladder of metrics: input and output, leading and lagging, North Star

!!! source "From your class deck (Week 6)"
    Input metrics measure what you control; output metrics measure the results you get. Leading metrics predict the future; lagging metrics confirm the past. A North Star (or "one metric that matters") signals success. Good metric work lays these out as a ladder.

| Pair | Meaning | Example |
|---|---|---|
| **Input metric** | Something the team can directly influence | Invites sent, high-quality listings added, notifications delivered |
| **Output metric** | The result of the inputs | Sign-ups from invites, bookings made |
| **Leading metric** | Early signal of later success | Daily active users, views on listings, week-1 activation |
| **Lagging metric** | Final result, slow to move | Revenue, annual retention, renewals |

A metric can be both: *input* to a higher metric and *output* of a lower one, and *leading* for revenue but *lagging* for activity. Draw the chain, do not memorise the labels.

!!! example "Worked example · a stays marketplace (hypothetical)"
    * **North Star:** number of successful, completed stays.
    * **Input metrics:** high-quality listings added; host response time; photo quality score.
    * **Output metrics:** searches that lead to a booking; bookings made.
    * **Leading:** views per listing, wish-list adds. **Lagging:** commission revenue, repeat-booking rate.

!!! example "Worked example · a music streaming product (hypothetical)"
    A **magic moment** such as "follows 10 artists in the first week" predicts later habit. Chain: app installs → magic moment → playlist creation → monthly active users → total listening time (North Star) → subscription revenue and ad revenue. Recommendation quality sits underneath as an input that lifts listening time.

**Choosing a North Star:** it should reflect value delivered to users, correlate with long-term revenue, be measurable weekly, and be something the team can influence. Pair it with 3 to 5 input metrics and 1 or 2 guardrails.

## AARRR in practice, retention curves and HEART

!!! source "From your class deck (Week 6)"
    AARRR asks five questions: are people interested (acquisition), using the product (activation), coming back (retention), bringing others (referral), and generating revenue. The deck adds the **magic moment** idea for activation, retention-curve shapes as a sign of product-market fit, and the **HEART** framework (Happiness, Engagement, Adoption, Retention, Task success).

### Worked example · AARRR and HEART for a credit-card payments app (hypothetical)

| Stage | Question | Example metric |
|---|---|---|
| Acquisition | Are people interested? | App installs, sign-ups from each channel |
| Activation | Did they reach the magic moment? | Users who link a card and pay a first bill |
| Retention | Do they repeat the key action? | Users paying 3 consecutive bills |
| Referral | Do they recommend it? | Invites accepted, referral-code sign-ups, rewards shared |
| Revenue | Do they generate revenue? | Users redeeming rewards at partner merchants, partner fees |

| HEART | Example metric |
|---|---|
| **H**appiness | App-store rating, CSAT after a payment |
| **E**ngagement | Users who paid a bill and used at least one reward in the month |
| **A**doption | New users completing the first bill payment |
| **R**etention | Users with 3 consecutive on-time payments |
| **T**ask success | Share of users who avoid a late fee |

### The magic moment

Find the earliest action that predicts retention and design onboarding to push users toward it. Examples: a social product found that people who followed enough accounts early tended to stay; a file-sync product saw that users who uploaded one file tended to return. **Test, do not copy:** compare retention of users who did the action versus those who did not, and remember correlation is not causation, so confirm with an experiment.

### Reading retention curves

| Shape | What it suggests |
|---|---|
| Nearly flat line near 100% | Rare, very sticky product or a tiny, committed group |
| Steep early drop, then a long flat tail | A core group loves it; focus on getting more of the right users in and activating them faster |
| Flat, dip, then recovery | Seasonal or event-driven use; understand the trigger |
| Steady decline to zero (50%, 25%, 10%...) | No product-market fit yet; fix value before spending on growth |

A curve that **flattens** (even at 15 to 20%) is a sign of product-market fit for that group; a curve that never flattens is a warning.

## Metrics cheat sheet and the hierarchy of analytics

!!! source "From your class deck (Week 6)"
    The deck groups metrics into business, product, feature and engineering sets, and shows a "hierarchy of analytics tools" and a product-analytics tool tutorial.

| Group | Examples |
|---|---|
| **Business: revenue** | Revenue, ARPU, LTV, ARR, GMV, AOV |
| **Business: costs and profit** | CAC, COGS, marketing cost, fixed and variable cost, gross margin, net margin, unit contribution |
| **Product: acquisition** | Installs, downloads, sign-ups, unique visitors, bounce rate |
| **Product: activation** | DAU, WAU, MAU, session count, conversion rate |
| **Product: engagement** | Engaged users, session length, feature usage |
| **Product: retention** | Day-1 / Day-7 / Week-4 retention, week-on-week, month-on-month, churn |
| **Product: satisfaction** | CSAT, NPS, store rating, support tickets, bugs |
| **Feature** | Adoption (first-time and repeat), usage funnel, heatmap, task completion, task success and failure rate, time and steps to complete, cognitive load |
| **Engineering: speed** | Page load time, time to interactive, cold and warm start, end-to-end action latency (actual and perceived) |
| **Engineering: reliability** | Action and API reliability, availability, MTTR (mean time to repair), MTBF (mean time between failures), downtime, API throttling rate |

!!! tip "Why PMs should know engineering metrics"
    A slow or unreliable product loses users no matter how good the feature is. Put one latency and one reliability metric next to every funnel you own, and ask engineers for p95 and p99, not only the average.

### Hierarchy of analytics

| Level | Question | Typical tools and methods |
|---|---|---|
| **Descriptive** | What happened? | Dashboards, funnels, cohort tables (Mixpanel, Amplitude, GA4, Power BI) |
| **Diagnostic** | Why did it happen? | Segmentation, drill-downs, session replays, interviews |
| **Predictive** | What will happen? | Forecasts, churn and propensity models |
| **Prescriptive** | What should we do? | Experiments, recommendation and optimisation systems |

Start at the bottom and climb only when the lower level is trusted: a predictive model on messy events wastes time.

## OKRs: objectives and key results

!!! source "From your class deck (Week 6)"
    Objectives are inspiring, concrete, action-oriented goals. Key results are specific, time-bound, measurable and verifiable outcomes. OKRs cascade: a company or higher-team objective is broken into a team's objective, 3 to 5 key results, and initiatives that deliver them. The deck recommends the book *Measure What Matters*.

| Part | Rule of thumb | Poor example | Good example |
|---|---|---|---|
| **Objective** | Qualitative, ambitious, memorable | "Improve onboarding" | "Make the first day delightful for every new customer" |
| **Key result** | Numeric, time-bound, outcome not activity | "Launch new tutorial" | "Raise day-7 activation from 38% to 48% by end of Q2" |
| **Initiative** | The work you do | | Redesign onboarding checklist; add a sample dataset |

!!! example "Worked example · OKRs for a video-meeting product (hypothetical)"
    **Objective:** meetings feel as smooth as being in the room.
    * KR1: reduce meeting disconnections by 30% for all calls this year.
    * KR2: lift join-success rate from 96% to 98.5% on mobile.
    * KR3: keep audio-quality complaints under 2 per 1,000 meetings.
    **Initiatives:** better reconnect logic, network-quality indicators, adaptive bitrate tuning.

!!! example "Worked example · cascading OKRs for a streaming company (hypothetical)"
    Company vision: help creators earn a living from their work and help fans find music they love.
    * **Creator-tools team objective:** make releasing an album effortless. KR: cut the average time to release from 10 days to 7 days this year.
    * **Recommendations team objective:** make discovery delightful. KR: raise average session length by 20% this year.
    Each team's objective rolls up to the company vision, and each KR rolls up to the team's North Star.

**Common mistakes:** too many OKRs (more than 3 objectives per team), key results that are tasks ("ship feature X"), sandbagged targets, no guardrail, and using OKRs for performance reviews so that people hide bad news. Aim for ambitious targets where 60 to 70% achievement is a good outcome, and review monthly.

## Exercises with model answers

!!! question "Exercise 1 · Funnel diagnosis"
    A funnel shows: Visit 20,000 → Product page 12,000 → Cart 3,000 → Checkout 2,100 → Order 1,680. (a) Compute step conversions. (b) Which step is lowest? (c) Name three hypotheses and the data you would pull for each.

??? answer "Model answer"
    (a) 60.0%, 25.0%, 70.0%, 80.0%; overall 8.4%. (b) Product page → Cart at **25%**. (c) H1: add-to-cart is hard to find on mobile — segment by device and check click heatmaps/events. H2: prices or fees not clear until cart — compare with sessions where a fee estimate was shown earlier; run a usability test. H3: wrong traffic mix (new channel bringing low-intent users) — split by acquisition channel. State the largest absolute loss is Visit→Product page (8,000), but the product page is a browsing step; the cart step is more actionable.

!!! question "Exercise 2 · Is the test result real?"
    Control: 4,000 users, 600 conversions. Variant: 4,000 users, 660 conversions. Compute the lift, z-statistic, p-value and 95% CI. Would you ship?

??? answer "Model answer"
    p₁ = 15.0%, p₂ = 16.5%; diff = +1.5 pts (relative +10%). Pooled p̂ = 1,260/8,000 = 0.1575; SE = √(0.1575 × 0.8425 × (2/4,000)) = 0.008141; z = 0.015/0.008141 = **1.84**; p ≈ **0.066** (two-sided) → not significant at 0.05. Unpooled SE = √(0.15×0.85/4,000 + 0.165×0.835/4,000) = 0.008155 → 95% CI ≈ **−0.1 to +3.1 pts**, which includes zero. Do not claim a win; the effect might be real but the test is underpowered for a 1.5-point effect (roughly 9,250 per arm would be needed at 80% power). Options: extend the test to the planned size, or accept the uncertainty if the change is cheap and reversible.

!!! question "Exercise 3 · Unit economics"
    Subscription: ₹300/month price; gross margin 70%; monthly churn 6%; CAC ₹1,500. Compute LTV (simple), LTV:CAC and payback. Which assumption would you stress-test?

??? answer "Model answer"
    Monthly contribution ≈ 300 × 0.70 = ₹210. LTV = 210 ÷ 0.06 = **₹3,500**. LTV:CAC = 3,500 ÷ 1,500 = **2.33**. Payback = 1,500 ÷ 210 = **7.1 months**. Stress-test churn (e.g., 9% → LTV ₹2,333, ratio 1.56) and whether churn is really constant — real cohorts usually churn faster in month 1 and flatten.

!!! question "Exercise 4 · Pick a North Star"
    Choose an NSM for a language-learning app and name two guardrails and one way the team could game it.

??? answer "Model answer"
    NSM: *learners who complete ≥ 3 lessons per week* (value = actual learning). Guardrails: lesson quality rating / test scores; 30-day retention; complaints about notification spam. Gaming: making lessons trivially short or sending aggressive streak-guilt notifications to inflate lesson counts — hence the quality and wellbeing guardrails.

## Interview perspective

??? question "“How would you measure the success of a new feature?” — structure"
    1) Goal and user: what outcome and for whom. 2) **Primary metric** (outcome), 3) **input/leading metrics** that explain it, 4) **guardrails**, 5) **how you will measure causally** (A/B or phased rollout), 6) **timeframe** and success threshold, 7) **segments** to check, 8) **decision rule** (ship, iterate, stop). Close with what you would do if the result is inconclusive.

??? question "“Our retention is dropping. How do you investigate?” — 60-second answer"
    “I'd first confirm the definition and whether it's real — check tracking and seasonality. Then I'd see *which* cohorts: new vs old users, by channel, platform, geography. If new cohorts are weaker, I'd look at acquisition quality and onboarding changes; if everyone is weaker after a date, at releases or competitor moves. I'd pair the quantitative cut with 5–8 interviews of recently churned users to learn why, form two or three hypotheses, and test the cheapest first. I'd also check guardrails so a fix doesn't hurt revenue or satisfaction.”

## Key takeaways

* A metric is only as good as its **definition** (event, numerator, denominator, window, exclusions).
* Use **leading + lagging** metrics, an NSM with a **metric tree**, and **guardrails**.
* Funnels, cohorts and segmentation show **where** things change; research and experiments show **why** and **whether it works**.
* **GMV ≠ revenue ≠ profit.** Check contribution margin and CAC payback before celebrating growth.
* Experiments need **pre-registered metrics, adequate power, clean randomisation and guardrails.** p-values are not the probability a variant works; CIs show effect size.
* **Correlation is not causation** — Simpson's paradox is the standard warning.
* Instrument from a **tracking plan**, validate data quality, and keep personal data out of analytics events.

## Check your understanding

```quiz
- q: "A funnel has 800 of 1,000 visitors completing a step. What are step conversion and drop-off?"
  options:
    - "80% and 20%"
    - "20% and 80%"
    - "100% and 0%"
    - "Cannot tell without revenue"
  answer: 0
  why: "Step conversion = 800 ÷ 1,000 = 80%; drop-off = 1 − 0.80 = 20%."
- q: "AOV is best defined as…"
  options:
    - "Total revenue ÷ number of users"
    - "Total order value ÷ number of orders"
    - "Profit ÷ orders"
    - "GMV ÷ MAU"
  answer: 1
  why: "AOV = total order value ÷ number of orders for the same period and definition. It says nothing by itself about profit."
- q: "A test gives p = 0.03. Which statement is correct?"
  options:
    - "There is a 97% chance the variant is better."
    - "If there were truly no difference, results this extreme would occur about 3% of the time."
    - "The effect is large."
    - "The result will replicate 97% of the time."
  answer: 1
  why: "A p-value is a probability about the data under the null hypothesis. It is not the probability the variant works and says nothing about effect size."
- q: "Which change makes the required sample size per arm increase the most?"
  options:
    - "Halving the minimum detectable effect"
    - "Raising power from 80% to 85%"
    - "Doubling traffic"
    - "Using one more guardrail"
  answer: 0
  why: "Sample size scales roughly with 1/(effect size)², so halving the MDE roughly quadruples the sample."
- q: "LTV (simple) = ₹120 ÷ 0.05 is ₹2,400. If churn rises to 8%, LTV becomes…"
  options:
    - "₹960"
    - "₹1,500"
    - "₹2,400"
    - "₹3,840"
  answer: 1
  why: "120 ÷ 0.08 = ₹1,500. LTV is very sensitive to churn."
- q: "In Simpson's paradox, the overall result is reversed relative to every segment because of…"
  options:
    - "Rounding"
    - "Unequal segment mix between groups"
    - "Too many users"
    - "Using a two-sided test"
  answer: 1
  why: "When the variant gets a different mix of high- and low-converting segments, the aggregate can mislead; proper randomisation and segmenting fix it."
- q: "Which should NOT be sent as an analytics event property?"
  options:
    - "cart_value"
    - "platform"
    - "card_number"
    - "item_count"
  answer: 2
  why: "Card details (and typically emails and phone numbers) must never go into analytics tools."
```

## Recommended resources

* [Google Analytics Help](https://support.google.com/analytics) — events, key events, privacy.
* [Mixpanel Docs](https://docs.mixpanel.com/) · [Amplitude Docs](https://amplitude.com/docs) — product analytics concepts and setup.
* [Power BI documentation](https://learn.microsoft.com/power-bi/) — dashboards and DAX.
* [Evan Miller: A/B testing tools and sample-size calculator](https://www.evanmiller.org/ab-testing/) — practical references for sample size and sequential testing.
* [Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments*](https://experimentguide.com/) — the standard book on online experimentation.
* [SQLBolt](https://sqlbolt.com/) — free interactive SQL lessons.

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


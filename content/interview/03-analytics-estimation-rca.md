---
id: analytics
title: Product analytics (10 questions)
category: Analytics
order: 5
summary: Metrics, funnels, experiments, SQL and interpreting data.
---

??? question "AN1 · Easy — What metrics would you track for a food-delivery app?"
    **What it tests:** metric hierarchy and guardrails.

    **Approach:** North Star → inputs → economics → guardrails.

    **Model answer:** “North Star: completed, problem-free orders per active customer per month. Inputs: activation, order frequency, cart conversion, payment success, on-time delivery. Economics: AOV, contribution per order, CAC payback. Guardrails: refunds, complaints, cancellations.” *(Module 7.)*

    **Assumptions & trade-offs:** “problem-free” needs a precise definition.

    **Common mistakes:** listing 20 unrelated metrics; vanity metrics like total downloads.

    **60-second answer:** NSM + 4 inputs + 2 economics + 3 guardrails.

??? question "AN2 · Medium — Define activation for a team-collaboration product."
    **What it tests:** linking an early behaviour to long-term value.

    **Approach:** candidate events → correlation with retention → causal test.

    **Model answer:** “An event reflecting team value that predicts retention, e.g., ‘a workspace with ≥ 3 members exchanging messages in a channel within 7 days.’ Validate by comparing retention of activated vs not, then run an experiment to see whether helping teams reach it improves retention.”

    **Assumptions & trade-offs:** correlation ≠ causation; too-easy activation events are meaningless.

    **Common mistakes:** using sign-up as activation.

    **60-second answer:** team-level value event, validated against retention, tested causally.

??? question "AN3 · Medium — An A/B test shows +3% conversion with p = 0.04. Ship?"
    **What it tests:** experiment hygiene beyond the p-value.

    **Approach:** pre-registration → power and duration → SRM → guardrails → CI and practical value → novelty → decision.

    **Model answer:** “Check: was this the pre-registered primary metric? Adequate power and full weeks? Any sample ratio mismatch? Guardrails flat? Does the low end of the confidence interval still justify the cost? Is there a novelty risk or a segment that reverses? If all good, ship with a holdout; if not, extend or rerun.”

    **Assumptions & trade-offs:** speed of shipping vs certainty.

    **Common mistakes:** shipping on p < 0.05 alone; peeking.

    **60-second answer:** p is necessary, not sufficient — check design, guardrails, CI and cost.

??? question "AN4 · Medium — Explain p-value and confidence interval to a non-technical stakeholder."
    **What it tests:** clarity and correctness under simplification.

    **Approach:** plain-language definitions → why the CI matters for decisions.

    **Model answer:** “The p-value tells us how surprising our result would be if the change actually did nothing — small means unlikely to be pure chance. The confidence interval gives the range of effect sizes consistent with our data, like ‘between +1 and +4 points’. It's the range that matters for the business decision.”

    **Assumptions & trade-offs:** simplification loses nuance; avoid saying “95% chance the variant is better”.

    **Common mistakes:** misdefining p as the probability the variant works.

    **60-second answer:** the two sentences above.

??? question "AN5 · Medium — How would you calculate retention and what pitfalls exist?"
    **What it tests:** cohort thinking and definitional rigour.

    **Approach:** cohort → active definition → window → formula → pitfalls.

    **Model answer:** “Group users by signup week; define ‘active’ as a meaningful action; retention in week k = active users in week k ÷ cohort size. Pitfalls: mixed definitions, small cohorts, survivorship bias, seasonality, counting any app open as active.”

    **Assumptions & trade-offs:** rolling vs bracketed windows.

    **Common mistakes:** averaging across different cohorts without care.

    **60-second answer:** cohort ÷ active-in-window, with clear definitions and pitfalls.

??? question "AN6 · Hard — DAU grew 10% but revenue fell 5%. Explain possible reasons."
    **What it tests:** decomposition and segment thinking.

    **Approach:** revenue = active users × payer conversion × ARPPU → check each by segment.

    **Model answer:** “Mix shift (new users are free or low spenders), pricing/promotion changes, payment failures, lower conversion of engaged users, refunds, or measurement changes. Decompose revenue = active users × payer conversion × ARPPU and check each component by segment and date.”

    **Assumptions & trade-offs:** some reasons are healthy (deliberate acquisition of free users).

    **Common mistakes:** jumping to one story without decomposing.

    **60-second answer:** decompose, segment, check payments and pricing.

??? question "AN7 · Medium — Write SQL for conversion from checkout start to payment."
    **What it tests:** practical SQL and definitional awareness.

    **Approach:** count distinct users per step → ratio → note funnel strictness.

    **Model answer:**

        SELECT ROUND(100.0 * COUNT(DISTINCT CASE WHEN event_name='payment_success' THEN user_id END)
               / COUNT(DISTINCT CASE WHEN event_name='checkout_start' THEN user_id END), 1) AS pct
        FROM events;

    On the synthetic dataset this returns 284 ÷ 322 = **88.2%** (users who ever reached each step).

    **Assumptions & trade-offs:** a strict funnel needs ordering and a time window per user.

    **Common mistakes:** counting events instead of users; dividing by the wrong step.

    **60-second answer:** distinct users at each step, ratio, mention ordering/time windows.

??? question "AN8 · Medium — Correlation vs causation — give a product example."
    **What it tests:** causal reasoning.

    **Approach:** example → confounder → how to test.

    **Model answer:** “Users of feature X retain better, but power users may both use X and retain for other reasons (confounding). Test with a randomised experiment or a credible quasi-experiment. Simpson's paradox shows how an uneven traffic mix can reverse conclusions.”

    **Assumptions & trade-offs:** experiments aren't always possible; use holdouts or staggered rollouts.

    **Common mistakes:** claiming a feature “drives” retention from a correlation.

    **60-second answer:** example → confounder → experiment.

??? question "AN9 · Hard — How would you measure the success of a recommendation system?"
    **What it tests:** online vs offline evaluation and long-term thinking.

    **Approach:** offline metrics → online metrics → long-term holdout → guardrails.

    **Model answer:** “Offline: precision/recall@k on historical data. Online: click-through and, more importantly, downstream outcomes (purchases, listening time, satisfaction) via A/B tests; diversity and novelty; long-term retention via holdout. Guardrails: complaints, returns, filter bubbles, creator/seller fairness.”

    **Assumptions & trade-offs:** clicks vs satisfaction; short vs long term.

    **Common mistakes:** optimising CTR alone.

    **60-second answer:** offline + online outcomes + holdout + guardrails.

??? question "AN10 · Medium — What would you put on a PM dashboard for a new feature?"
    **What it tests:** dashboard design tied to decisions.

    **Approach:** exposure → adoption → outcome → guardrails → segments → context.

    **Model answer:** “Exposure (who saw it), adoption (who used it), the primary outcome, guardrails, segment cuts, release annotations, data freshness and metric definitions.”

    **Assumptions & trade-offs:** too many charts dilute focus.

    **Common mistakes:** no definitions; no guardrails.

    **60-second answer:** the list above, one headline per question.

<!-- item -->
---
id: estimation
title: Estimation / guesstimates (8 questions)
category: Estimation
order: 6
summary: Structured estimates with assumptions, two methods and a range.
---

??? question "ES1 · Medium — Estimate daily ride-hailing trips in a large Indian metro."
    **What it tests:** structure, assumptions, sanity checks.

    **Approach:** clarify definitions → top-down → bottom-up → reconcile → range.

    **Model answer:** “Top-down: 20M population → 14M adults → 8% weekly users = 1.12M × 3 trips/week ≈ 480k/day. Bottom-up: 55,000 active drivers × 9 trips ≈ 495k/day. Range 450k–500k; sanity check ≈ 3.4% of adults ride daily.” *(Module 3; course Lecture 7 — practice figures, not company data.)*

    **Assumptions & trade-offs:** share of weekly users and trips per driver are the most uncertain.

    **Common mistakes:** inconsistent definitions (cancelled rides); no range.

    **60-second answer:** two methods, reconciled, range, key assumptions.

??? question "ES2 · Medium — How many food-delivery orders happen per day in a city of 10 million?"
    **What it tests:** segmentation and supply-side checks.

    **Approach:** households → eligible → frequency → adjust → supply check.

    **Model answer:** “10M ÷ 4 = 2.5M households; 60% with smartphones in delivery zones = 1.5M; 30% order at least weekly = 450k; 2.5 orders/week = 1.125M/week ≈ 160k/day; +20% for offices/single residents ≈ 190k/day. Range 150k–250k. Supply check: 15,000 couriers × 12 orders/day = 180k ✓.”

    **Assumptions & trade-offs:** household size and frequency vary by city.

    **Common mistakes:** skipping the supply check.

    **60-second answer:** ≈ 190k/day (150k–250k) with demand and supply methods.

??? question "ES3 · Easy — How many school lunches are bought daily at a 1,000-student school?"
    **What it tests:** basic decomposition.

    **Approach:** students × attendance × buying rate.

    **Model answer:** “1,000 × 60% at school × 50% buying = 300 lunches (course example). Discuss day-of-week and seasonal variation.”

    **Assumptions & trade-offs:** attendance and buying rates.

    **Common mistakes:** no stated assumptions.

    **60-second answer:** 300, with the three assumptions named.

??? question "ES4 · Medium — Estimate the annual revenue of a coffee chain with 200 outlets."
    **What it tests:** revenue modelling.

    **Approach:** per-outlet daily revenue → annualise → scale → range.

    **Model answer:** “400 cups/day × ₹220 average ticket = ₹88,000; + 25% food ≈ ₹1.1 lakh/day; × 360 days ≈ ₹3.96 crore per outlet; × 200 ≈ ₹790 crore/year. Range ₹600–950 crore.”

    **Assumptions & trade-offs:** outlet mix (airport vs suburb) changes footfall a lot.

    **Common mistakes:** treating all outlets as identical without saying so.

    **60-second answer:** ≈ ₹790 crore with per-outlet logic and a range.

??? question "ES5 · Medium — How many smartphones are sold in India per year?"
    **What it tests:** replacement-cycle reasoning.

    **Approach:** installed base ÷ replacement cycle + new users − second-hand.

    **Model answer:** “Assume ~700M users; ~3-year replacement → ~230M; + ~15M new users ≈ 245M; −30% for second-hand and multi-device effects ≈ 170M new devices (range 140–190M). Check against industry reports in real life.”

    **Assumptions & trade-offs:** user base and replacement cycle are the biggest levers.

    **Common mistakes:** population × penetration without replacement logic.

    **60-second answer:** base ÷ cycle + new − second-hand ≈ 170M.

??? question "ES6 · Hard — Estimate yearly image storage for a messaging app."
    **What it tests:** technical estimation.

    **Approach:** DAU × senders × images × size → annualise → replication.

    **Model answer:** “100M DAU × 20% sending × 5 images × 0.2 MB = 20 TB/day ≈ 7.3 PB/year before replication; ×3 replication ≈ 22 PB. Retention and deletion policies matter.”

    **Assumptions & trade-offs:** compression, media expiry, end-to-end encryption effects.

    **Common mistakes:** forgetting replication and retention.

    **60-second answer:** ≈ 7 PB/year raw, ~22 PB replicated.

??? question "ES7 · Medium — How many EV chargers does a city need?"
    **What it tests:** demand-to-capacity reasoning.

    **Approach:** EVs × share without home charging × sessions/week ÷ sessions per charger/week → peak adjustment.

    **Model answer:** “Example: 100,000 EVs × 40% without home charging × 2 sessions/week = 80,000 sessions/week; one fast charger can handle ~10 sessions/day ≈ 70/week → ~1,150 chargers; add 30% for peaks and geography ≈ 1,500 (range 1,200–2,000).”

    **Assumptions & trade-offs:** charger speed mix; utilisation targets.

    **Common mistakes:** ignoring peaks and location coverage.

    **60-second answer:** sessions needed ÷ sessions per charger, plus peak buffer.

??? question "ES8 · Easy — Estimate the number of piano tuners in a city."
    **What it tests:** the classic Fermi method.

    **Approach:** pianos × tunings/year ÷ tunings per tuner per year.

    **Model answer:** “A city of 5M with 2M households; 2% with pianos = 40,000 + 2,000 institutional; tuned once a year = 42,000 tunings; a tuner does ~4/day × 250 days = 1,000/year → about 40–45 tuners.”

    **Assumptions & trade-offs:** piano ownership varies widely by city.

    **Common mistakes:** chasing the “right” number instead of showing method.

    **60-second answer:** ≈ 40 tuners with explicit assumptions.

<!-- item -->
---
id: rca
title: Root cause analysis (8 questions)
category: Root cause analysis
order: 7
summary: Metric drops and anomalies — clarify, check data, segment, hypothesise, verify.
---

??? question "RC1 · Medium — Daily orders dropped 15% yesterday. What do you do?"
    **What it tests:** structured diagnosis.

    **Approach:** clarify the metric and window → data integrity → internal changes → external factors → segment → hypotheses → verify.

    **Model answer:** “First confirm it's real — did order *events* fall but the orders table didn't? Compare with the same day last week. Segment by platform, city, new/returning, payment method and restaurant. If only Android in one city dropped, check the latest release and payment-gateway logs there. Rank hypotheses by likelihood × impact and check the cheapest first.” *(Lecture 22: ask exactly which metric fell before an RCA.)*

    **Assumptions & trade-offs:** speed of diagnosis vs thoroughness.

    **Common mistakes:** jumping to a cause; skipping data-quality checks.

    **60-second answer:** real? → when/where/who → internal vs external → hypotheses → verify.

??? question "RC2 · Medium — The app-store rating fell from 4.4 to 4.1. Why?"
    **What it tests:** qualitative + quantitative investigation.

    **Approach:** review mining by date/version → crash data → policy changes → rating-prompt changes.

    **Model answer:** “Tag reviews by date and app version; correlate with releases; check crash rates; check whether a policy change (e.g., fees) triggered anger; check whether rating prompts changed (sampling bias). Fix the top cause and monitor.”

    **Assumptions & trade-offs:** ratings lag reality; vocal minorities.

    **Common mistakes:** responding to reviews without diagnosing.

    **60-second answer:** reviews by version + crashes + policy + prompt changes.

??? question "RC3 · Hard — Sign-ups up 20%, activation down 8 points. Explain."
    **What it tests:** mix-shift reasoning.

    **Approach:** segment activation by channel and cohort → check onboarding and tracking changes.

    **Model answer:** “Likely mix shift — a new channel bringing lower-intent users; or an onboarding change; or a change to the activation event's tracking; or a bug for one segment. If a new channel explains it, the funnel isn't broken — the traffic is different, and channel ROI should be judged on activated users.”

    **Assumptions & trade-offs:** volume vs quality of acquisition.

    **Common mistakes:** “fix onboarding” without segmenting.

    **60-second answer:** segment by channel/cohort; mix shift is the first suspect.

??? question "RC4 · Medium — Session length increased but retention decreased. Is that good?"
    **What it tests:** metric interpretation.

    **Approach:** possible meanings → checks.

    **Model answer:** “Not necessarily. Users may be struggling (tasks taking longer), or a minority binges while others leave. Check task success, segment by cohort, look at satisfaction and support tickets.”

    **Assumptions & trade-offs:** engagement vs efficiency products differ.

    **Common mistakes:** celebrating longer sessions.

    **60-second answer:** longer may mean harder; check success and cohorts.

??? question "RC5 · Medium — Ride cancellations spiked in one city."
    **What it tests:** marketplace diagnosis.

    **Approach:** supply → events/weather → pricing → app versions → ETA accuracy → payment modes.

    **Model answer:** “Check drivers online vs demand, local events or weather, pricing changes, driver-app bugs, ETA accuracy and payment-mode mismatches; segment by time and area; talk to operations.”

    **Assumptions & trade-offs:** rider vs driver cancellations need separate analysis.

    **Common mistakes:** treating all cancellations as one metric.

    **60-second answer:** split by who cancelled, when, where; check supply and changes.

??? question "RC6 · Medium — Payment success rate fell from 95% to 91%."
    **What it tests:** technical-business diagnosis.

    **Approach:** split by method, issuer, error code, app version → provider status → mitigation.

    **Model answer:** “Split by card/UPI/wallet, issuer/bank, error code and app version; check the gateway status and recent changes (3-D Secure flow, SDK update); contact the provider; mitigate with routing or retries; communicate with support.”

    **Assumptions & trade-offs:** some failures are customer-side (insufficient funds).

    **Common mistakes:** assuming it's always the gateway.

    **60-second answer:** decompose by method/issuer/error → recent changes → mitigate.

??? question "RC7 · Hard — In a community product, group creation is down. Diagnose."
    **What it tests:** defining meaningful metrics and community dynamics.

    **Approach:** define the metric → measurement → segment → discovery/moderation/competition hypotheses → test.

    **Model answer:** “Define the metric (new groups that become active?), check measurement, segment by country, platform and entry point; examine discovery changes, spam/moderation enforcement changes, and competition. Test hypotheses with data and interviews.” *(Course Lecture 36 case — hypotheses, not facts about any company.)*

    **Assumptions & trade-offs:** fewer but better groups may be fine.

    **Common mistakes:** optimising raw group counts.

    **60-second answer:** define meaningful creation → segment → hypotheses → test.

??? question "RC8 · Medium — Customer complaints doubled after a redesign."
    **What it tests:** owning a regression.

    **Approach:** read and tag → identify flows → usability test → accessibility check → fix or roll back.

    **Model answer:** “Tag complaints to flows; run a quick usability test on the new design; check for accessibility regressions; consider rollback or targeted fixes; compare task success before and after.”

    **Assumptions & trade-offs:** change aversion vs real problems — look at behaviour, not only sentiment.

    **Common mistakes:** dismissing complaints as change aversion.

    **60-second answer:** tag → test → fix or roll back → measure.

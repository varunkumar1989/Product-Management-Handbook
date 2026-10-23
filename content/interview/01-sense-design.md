---
id: product-sense
title: Product sense (8 questions)
category: Product sense
order: 1
summary: Favourite products, critiques, what makes products good, and quick improvement instincts.
---

??? question "PS1 · Easy — What is your favourite product and why?"
    **What it tests:** product taste, user empathy, ability to articulate value and trade-offs.

    **Approach:** product + user + job → why it works (2–3 design/business reasons) → one meaningful weakness with evidence → improvement + metric.

    **Model answer:** “Google Maps for commuting. My job is ‘get to work on time with least stress.’ It works because (1) live traffic turns uncertainty into an ETA I trust, (2) it re-routes proactively, (3) it combines modes. A weakness for me: on crowded metro lines it doesn't tell me how full trains are, so I can't choose a less crowded one. I'd test showing crowding levels from anonymised, aggregated data, measuring route-choice changes and satisfaction, with privacy as a guardrail.”

    **Assumptions & trade-offs:** crowding data availability and accuracy; privacy vs usefulness; added screen complexity.

    **Common mistakes:** listing features; choosing a product you can't critique; no user or metric.

    **60-second answer:** job → two reasons it works → one improvement → how you'd measure it.

??? question "PS2 · Easy — What makes a product great?"
    **What it tests:** principles over buzzwords; whether you connect user value to business sustainability.

    **Approach:** define “great” (value, usability, viability, trust) → evidence signals → one example.

    **Model answer:** “A great product reliably helps a specific user make progress on an important job, with as little effort and risk as possible, in a way the business can sustain. Signals: users return without being pushed (retention curves flatten), they recommend it, and the economics improve with scale. Example: a payments flow that just works at checkout — invisible reliability is a feature.”

    **Assumptions & trade-offs:** “great” differs by segment; delight vs simplicity; growth vs trust.

    **Common mistakes:** “beautiful design” alone; ignoring economics or reliability.

    **60-second answer:** the definition above plus one example and one signal.

??? question "PS3 · Medium — Critique the onboarding of an app you used recently."
    **What it tests:** observation, heuristics, prioritisation.

    **Approach:** goal of onboarding (time-to-value) → walk the steps → friction tied to heuristics → top fix → metric.

    **Model answer:** “A budgeting app asked for bank linking, notifications and goals before showing anything useful. Heuristic: visibility and user control — I had no idea what value I'd get. Biggest fix: show a sample dashboard immediately and ask for bank linking in context when I tap ‘see my spending’. Metric: activation (first budget created within 3 days); guardrails: permission grant rate, privacy complaints.”

    **Assumptions & trade-offs:** linking later may reduce data completeness; fewer upfront questions vs personalisation.

    **Common mistakes:** critiquing visuals only; no prioritised fix; no measurement.

    **60-second answer:** the job of onboarding → biggest friction → one fix → activation metric.

??? question "PS4 · Medium — Which product do you think is badly designed, and how would you fix it?"
    **What it tests:** constructive critique and empathy for constraints.

    **Approach:** acknowledge constraints → specific user problem → evidence → fix → trade-off.

    **Model answer:** “Many parking-payment apps: you must register, add a card and find a zone code while standing in the street. Constraint: municipalities require identification and payment records. Fix: a QR on the meter that opens a lightweight web flow with wallet payment, with optional account creation later. Trade-off: less data capture; mitigate with optional emailed receipts.”

    **Assumptions & trade-offs:** municipal rules allow guest payment; enforcement systems can read a plate-based session.

    **Common mistakes:** mocking the product; ignoring why it is that way.

    **60-second answer:** constraint → user pain → QR guest flow → trade-off.

??? question "PS5 · Medium — How would you improve YouTube Shorts?"
    **What it tests:** narrowing a broad prompt; multi-sided thinking (viewers, creators, advertisers); wellbeing guardrails.

    **Approach:** clarify goal (engagement? creator retention?) → pick a segment → pain → solutions → metric + guardrails.

    **Model answer:** “I'd focus on new viewers whose first Shorts feel irrelevant — they leave before personalisation kicks in. Ideas: a lightweight topic picker after the first few swipes; a ‘not interested’ that visibly teaches the feed; separation of short vs long results in search. I'd A/B the topic picker; primary: day-7 return rate of new viewers; guardrails: session-satisfaction surveys and time-spent spikes among younger users.”

    **Assumptions & trade-offs:** new-viewer churn is a real problem (verify with data); a picker adds friction.

    **Common mistakes:** optimising only watch time; proposing features for every stakeholder at once. *(Course link: Lecture 11 — ideas were participants' hypotheses.)*

    **60-second answer:** segment → cold-start pain → topic picker test → day-7 return + wellbeing guardrail.

??? question "PS6 · Medium — Should Netflix let users stop a title from leaving the catalogue?"
    **What it tests:** feasibility and business constraints (content rights) alongside user empathy.

    **Approach:** validate the need → identify constraints → reframe to the underlying job → alternatives → metric.

    **Model answer:** “The need is real — losing a show mid-watch is frustrating — but licences expire contractually, so a ‘keep’ button is usually infeasible. Better: warn earlier (‘leaving in 14 days’), a ‘finish before it leaves’ row, and use the count of mid-watch members as a signal in licence negotiations.”

    **Assumptions & trade-offs:** licence terms vary; early warnings could increase churn intent if users dislike departures.

    **Common mistakes:** proposing something contractually impossible without acknowledging it. *(Course link: Lecture 4.)*

    **60-second answer:** need → constraint → alternatives → metric (completion before departure).

??? question "PS7 · Hard — What product would you build for elderly users to manage medicines?"
    **What it tests:** empathy, accessibility, safety, multi-stakeholder design.

    **Approach:** users (elderly person, caregiver, pharmacist) → jobs → constraints (vision, dexterity, tech comfort) → solution → safety → metrics.

    **Model answer:** “Start with a caregiver-set schedule and a very simple ‘taken’ confirmation (large button, voice option); missed-dose alerts to a caregiver after a grace period; pharmacy refill reminders. Avoid medical advice; partner with pharmacists for dose data. Metrics: doses confirmed on time; caregiver alerts resolved. Guardrails: false alarms, privacy consent.”

    **Assumptions & trade-offs:** a caregiver exists and consents; autonomy vs oversight; device choice (phone vs smart dispenser).

    **Common mistakes:** complex app UI; giving medical advice; ignoring consent.

    **60-second answer:** caregiver schedule + one-tap confirmation + alerts; adherence metric; safety guardrails.

??? question "PS8 · Hard — What is a product you think will fail, and why?"
    **What it tests:** judgement under uncertainty, humility, use of criteria.

    **Approach:** state criteria (job, alternatives, switching costs, economics) → apply → what would change your mind.

    **Model answer:** “I'd question standalone AI gadgets that duplicate phone capabilities: the job (quick answers) is already served by phones; the device adds cost and charging burden; switching costs favour phones. It could succeed only if it serves a job phones do badly — hands-free contexts or accessibility. I'd watch day-30 retention and daily use versus phone usage.”

    **Assumptions & trade-offs:** future capabilities could change the picture; niche success is still success.

    **Common mistakes:** snark; no criteria; certainty without evidence.

    **60-second answer:** criteria → why it struggles → when it could win → signal to watch.

<!-- item -->
---
id: product-design
title: Product design (9 questions)
category: Product design
order: 2
summary: Design a product or feature for a user group under constraints.
---

??? question "PD1 · Medium — Design a search engine for children under 14."
    **What it tests:** user segmentation (child vs parent), safety, trade-offs.

    **Approach:** clarify age bands and purpose (school vs fun) → users (child, parent, teacher) → needs → design → safety → metrics.

    **Model answer:** “Focus on 8–12-year-olds doing homework. Needs: readable results, trustworthy sources, no unsuitable content, parents' reassurance. Design: curated educational sources first, reading-level summaries, image search with strict filtering, ‘ask a grown-up’ prompts for sensitive topics, a parent dashboard with privacy-preserving summaries. Filtering is imperfect — don't promise complete safety; add a report button; no personalised ads. Metrics: task success (found an answer); parent trust score; guardrail: unsafe-content reports.”

    **Assumptions & trade-offs:** curation narrows coverage; children's privacy rules limit data use; engagement must serve learning, not screen time.

    **Common mistakes:** one persona only; promising 100% safety. *(Course link: Lecture 8.)*

    **60-second answer:** 8–12 homework segment → curated, readable, safe results → parent controls → task success + safety guardrail.

??? question "PD2 · Medium — Help a professional regain control of an overflowing inbox after a holiday."
    **What it tests:** framing the job; AI risk management.

    **Approach:** define the job → triage needs → design → AI risks and controls → metrics.

    **Model answer:** “Job: find what's urgent and relevant without reading everything. Design: a ‘Catch-up’ view grouped by people I work with, deadlines and mentions; AI thread summaries with links to originals; bulk actions with preview and undo. Risks: misclassifying an important email, wrongly auto-archiving, exposing confidential data to AI — keep human review for bulk actions, test accuracy, respect permissions. Metric: time to clear important items; guardrail: ‘missed important email’ reports.”

    **Assumptions & trade-offs:** summaries may miss nuance; automation vs control.

    **Common mistakes:** fully automatic archiving; ignoring data protection. *(Course link: Lecture 8.)*

    **60-second answer:** catch-up view + summaries + safe bulk actions; time-to-clear metric with a missed-email guardrail.

??? question "PD3 · Medium — Design a feature to reduce food-delivery checkout abandonment."
    **What it tests:** funnel thinking, UX states, measurement.

    **Approach:** locate the drop (funnel) → cause (research) → design incl. failure states → experiment.

    **Model answer:** “First confirm where users drop — say, the payment step. If research shows fee surprise, show an estimated total in the cart with ‘est.’ labels, refresh on address change, and an honest ‘Estimate unavailable’ fallback if the fee service fails. A/B test with checkout completion as primary; complaints and payment errors as guardrails.” *(See Modules 5 and 7.)*

    **Assumptions & trade-offs:** estimates may differ from final fees; showing fees earlier could reduce add-to-cart.

    **Common mistakes:** redesigning everything; forgetting failure states.

    **60-second answer:** funnel → fee surprise → early total with fallback → A/B with guardrails.

??? question "PD4 · Hard — Design a dating feature for a large social network."
    **What it tests:** two-sided trust, safety, privacy, ethical monetisation.

    **Approach:** goals and segments → core flows → safety/privacy → monetisation → metrics and guardrails.

    **Model answer:** “Segment by intention (serious vs casual). Core: opt-in profile separate from the main profile, verified identity, mutual-interest reveal, events-based matching. Safety: consent, harassment reporting, location fuzzing, age verification, no exposure of private conversations. Monetisation: freemium features that don't compromise safety (no paying to message strangers). Metric: mutual matches that lead to conversations; guardrails: reports per 1,000 users, blocks.”

    **Assumptions & trade-offs:** separation from the main network vs leveraging its graph; compatibility scores may bias choice.

    **Common mistakes:** engagement-only metrics; AI-invented targets. *(Course link: Lecture 41.)*

    **60-second answer:** intentions → safe opt-in profiles + mutual reveal → ethical freemium → quality-match metric with safety guardrails.

??? question "PD5 · Medium — Design an ATM for the visually impaired."
    **What it tests:** accessibility and inclusive design.

    **Approach:** users and contexts → tasks (withdraw, balance) → barriers → design → testing.

    **Model answer:** “Audio guidance via a headphone jack, a tactile keypad with raised markers, phone-based pre-staging (set the withdrawal in the app, then tap card/phone), screen blanking for privacy, consistent layouts and generous timeouts. Test with visually impaired users; measure task success and time; guardrail: fraud and shoulder-surfing incidents.”

    **Assumptions & trade-offs:** hardware retrofit cost; privacy vs audible prompts (use headphones).

    **Common mistakes:** designing without involving visually impaired users; relying on colour or screens alone.

    **60-second answer:** audio + tactile + phone pre-staging + privacy; test with real users.

??? question "PD6 · Medium — Design a parking app for a busy city."
    **What it tests:** user segmentation, data constraints, operational realism.

    **Approach:** segments → jobs → features → data/partners → metrics → risks.

    **Model answer:** “Users: daily commuters vs occasional visitors. Jobs: find a spot quickly, pay easily, avoid fines. Features: live availability (sensors/partner garages), reserve and pay, extend remotely, reminders before expiry. Metrics: time to park, successful reservations, fine reduction (self-reported). Risks: inaccurate availability → show confidence levels.”

    **Assumptions & trade-offs:** data coverage limits; reserving spots may need operator agreements.

    **Common mistakes:** assuming perfect real-time data; ignoring payment regulations.

    **60-second answer:** commuter focus → find, pay, extend → time-to-park metric → data-confidence risk.

??? question "PD7 · Hard — Design a product to help small restaurants reduce food waste."
    **What it tests:** B2B empathy, data feasibility, business value.

    **Approach:** user (owner/chef) → job → simplest solution → data needs → metrics.

    **Model answer:** “Job: prepare and order the right quantities. Start with a simple demand forecast from past sales + weather + local events, giving suggested prep quantities; later add a marketplace for end-of-day surplus. Low integration first (POS export/CSV). Metrics: waste % by weight, margin; guardrail: stock-outs.”

    **Assumptions & trade-offs:** restaurants record sales consistently; forecasts vs chef intuition (keep human control).

    **Common mistakes:** heavy integrations first; ignoring stock-out risk.

    **60-second answer:** forecast-based prep suggestions → waste % metric with stock-out guardrail.

??? question "PD8 · Medium — Design a feature to increase channel-creation quality in a team-chat tool."
    **What it tests:** B2B UX, findability, experiment design at account level.

    **Approach:** problem evidence → design at the moment of creation → metric → experiment unit.

    **Model answer:** “Suggest similar existing channels when someone types a new channel name; offer naming templates and pre-filled purposes; improve directory search. Primary metric: duplicate-channel rate; secondary: channel-message share. Randomise by workspace to avoid contamination.” *(See Case 7 and Project 3.)*

    **Assumptions & trade-offs:** suggestions must respect private-channel permissions; small extra friction at creation.

    **Common mistakes:** blocking creation; randomising at user level in a team product.

    **60-second answer:** similar-channel suggestions + templates → duplicate rate → workspace-level A/B.

??? question "PD9 · Hard — Design an emergency feature for a ride-hailing app."
    **What it tests:** safety-critical design and handling false positives.

    **Approach:** stakeholders → scenarios → features → failure modes → compliance → metrics.

    **Model answer:** “Users: rider, driver, emergency contacts, safety operations. Features: an SOS button that shares live location with emergency services/contacts per local rules, trip sharing, unusual-stop detection with a check-in prompt, and a safety centre. Design for false positives without delaying urgent calls; offline/poor-network fallback (SMS). Metrics: time to response, check-in resolution; guardrails: false alarms, privacy.”

    **Assumptions & trade-offs:** emergency-service integration varies by city; automation vs user control.

    **Common mistakes:** treating it like a growth feature; ignoring local emergency integration.

    **60-second answer:** SOS + sharing + anomaly check-ins; response-time metric; false-alarm and privacy guardrails.

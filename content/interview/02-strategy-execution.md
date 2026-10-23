---
id: product-strategy
title: Product strategy (8 questions)
category: Product strategy
order: 3
summary: Market entry, competition, growth options, build/buy/partner and long-term bets.
---

??? question "ST1 · Medium — Should a food-delivery company launch grocery delivery?"
    **What it tests:** strategic fit, unit economics, capabilities.

    **Approach:** goal → customer need → market size → right to win (assets) → economics → risks → test plan.

    **Model answer:** “It's product development in an existing market (Ansoff). Assets: customer base, courier network, app. Need: fast top-ups for urban households. Economics differ: lower AOV and margin, inventory and dark stores. I'd pilot in two dense neighbourhoods with a limited assortment, measure repeat rate, contribution per order and cannibalisation of food orders, and scale only if contribution turns positive within ~6 months.”

    **Assumptions & trade-offs:** growth vs margin; focus vs expansion; operational complexity.

    **Common mistakes:** “yes, big market”; ignoring unit economics and cannibalisation.

    **60-second answer:** Ansoff framing → assets → different economics → limited pilot with contribution gate.

??? question "ST2 · Hard — How should a travel marketplace respond to a sudden collapse in travel (e.g., a pandemic)?"
    **What it tests:** strategy under crisis; demand and supply thinking.

    **Approach:** what changed (demand, rules, trust) → segments still travelling → protect supply → product moves → metrics. *(Your course raised an Airbnb-during-COVID question in Lecture 10 without developing an answer; this is an independent, hypothetical approach — not a description of what any company did.)*

    **Model answer:** “Focus on demand that still exists — nearby getaways and long stays for remote workers; adapt search to flexible destinations and monthly stays; strengthen trust with cleaning standards and flexible cancellation; support hosts with clear refund rules. Measure booking recovery by segment, host retention and refund disputes.”

    **Assumptions & trade-offs:** flexible cancellation increases host risk; cash preservation vs investment.

    **Common mistakes:** only cost-cutting; ignoring the supply side.

    **60-second answer:** shift to surviving segments, rebuild trust, protect hosts, measure recovery by segment.

??? question "ST3 · Medium — How would you enter a new country with a fintech product?"
    **What it tests:** market-entry structure, regulatory awareness.

    **Approach:** PESTLE → segment → licence/partner model → localisation → pilot → economics.

    **Model answer:** “Scan regulation, payments infrastructure and trust (PESTLE); choose a beachhead segment; partner with a licensed local bank first rather than seeking a licence; localise language, KYC documents and payment methods; pilot in one city. Key risks: regulatory timelines and new fraud patterns. Metrics: activation, fraud rate, CAC payback.”

    **Assumptions & trade-offs:** partner dependency vs speed; local compliance cost.

    **Common mistakes:** copying the home-market product; ignoring licensing.

    **60-second answer:** PESTLE → partner-led entry → localise → pilot with fraud and payback gates.

??? question "ST4 · Medium — A competitor launched a cheaper version of our product. What do you do?"
    **What it tests:** composure, segmentation, evidence before reaction.

    **Approach:** measure the threat → understand why customers switch → options → choose by margin and strategic segment.

    **Model answer:** “Don't react instantly. Check churn and win/loss by segment, interview switchers, and see whether price or features drive it. Options: hold price and sharpen value messaging; launch a lighter tier for price-sensitive users; bundle; raise switching value ethically. Choose based on margin impact and which segment matters strategically.”

    **Assumptions & trade-offs:** price cuts are hard to reverse; a light tier can cannibalise.

    **Common mistakes:** automatic price cut; ignoring segments.

    **60-second answer:** measure → understand → targeted response, not a blanket price cut.

??? question "ST5 · Hard — Should a music-streaming service expand into podcasts or audiobooks?"
    **What it tests:** platform expansion logic, economics, differentiation.

    **Approach:** reframe the job → benefits → costs → strategy → metrics. *(Hypothetical analysis.)*

    **Model answer:** “Frame it as expanding from ‘music’ to ‘audio companionship’. Benefits: more listening time, differentiation, ad inventory. Costs: content and rights, discovery complexity. Strategy: invest in discovery and creator tools rather than only exclusives. Measure incremental listening time and retention, not catalogue size.”

    **Assumptions & trade-offs:** exclusives are expensive; cluttered UX for music-only users.

    **Common mistakes:** measuring success by catalogue size.

    **60-second answer:** job expansion → discovery-led strategy → incremental listening and retention.

??? question "ST6 · Medium — Build, buy or partner for identity verification?"
    **What it tests:** build/buy/partner reasoning.

    **Approach:** is it core? → speed → total cost → compliance → lock-in.

    **Model answer:** “Buy or partner: identity verification is regulated and commodity-like, and speed matters. Keep control of the onboarding UX and data handling, check vendor compliance and uptime, build an abstraction layer to switch vendors, and revisit building only if scale economics or differentiation justify it.”

    **Assumptions & trade-offs:** vendor cost at scale; data residency.

    **Common mistakes:** building commodity capabilities; ignoring exit costs.

    **60-second answer:** commodity + regulated → partner, with an abstraction layer and a review point.

??? question "ST7 · Medium — What is the moat for a ride-hailing company?"
    **What it tests:** understanding of network effects and their limits.

    **Approach:** list candidate moats → test each → conclude on durability.

    **Model answer:** “Local network effects (density cuts wait times), brand trust and safety record, data for pricing and ETAs, and driver relationships. Weaknesses: riders and drivers multi-home, and regulation. So the moat is local and must be continuously defended with reliability and driver economics.”

    **Assumptions & trade-offs:** subsidies by rivals can erode density quickly.

    **Common mistakes:** saying “network effects” without testing them.

    **60-second answer:** local density + trust + data; weakened by multi-homing; defend city by city.

??? question "ST8 · Hard — How would you set a 3-year vision and strategy for a B2B SaaS product?"
    **What it tests:** long-range thinking, sequencing, measurable strategy.

    **Approach:** vision → beachhead → adjacent segments → product pillars → GTM motion → metrics → what we won't do.

    **Model answer:** “Vision: the customer future (e.g., ‘every team closes the loop on decisions’). Strategy: win a beachhead, then adjacent segments; three product pillars; integrations as a platform; GTM from PLG to sales-assist; pricing evolution; an NSM with guardrails; explicit ‘won't do’ list. Validate yearly with retention, NRR and win/loss.”

    **Assumptions & trade-offs:** focus vs breadth; platform investment vs features.

    **Common mistakes:** a feature list dressed up as strategy.

    **60-second answer:** vision → beachhead → pillars → GTM → NSM → annual validation.

<!-- item -->
---
id: execution
title: Execution (8 questions)
category: Execution
order: 4
summary: Delivery, trade-offs, launches, incidents, and making things happen.
---

??? question "EX1 · Medium — Your launch is slipping by three weeks. What do you do?"
    **What it tests:** ownership, communication, trade-offs.

    **Approach:** root cause → options (scope, date, resources) → recommend → communicate → record.

    **Model answer:** “Find out why — scope growth, a dependency or quality issues. Options: cut scope to keep the date, add people (rarely helps late), or move the date. Choose by cost of delay and quality risk. Tell stakeholders immediately with impact and the new plan; update the decision log.”

    **Assumptions & trade-offs:** some dates are contractual; quality cuts create debt.

    **Common mistakes:** hiding the slip; promising dates for engineers.

    **60-second answer:** root cause → scope-vs-date options → recommendation → early communication.

??? question "EX2 · Medium — How do you write good user stories and acceptance criteria?"
    **What it tests:** requirement clarity and testability.

    **Approach:** INVEST stories → Given/When/Then criteria → non-functional and analytics needs → Ready/Done.

    **Model answer:** “Stories describe user value: ‘As a first-time buyer, I want to see my estimated total in the cart so I can decide before paying.’ Criteria cover the happy path, edge cases, errors, accessibility and analytics events, in Given/When/Then form. I review them with engineering and QA before sprint planning.” *(Module 6.)*

    **Assumptions & trade-offs:** detail vs flexibility; documentation overhead.

    **Common mistakes:** solution-prescriptive stories; untestable criteria (“fast”, “intuitive”).

    **60-second answer:** INVEST + Given/When/Then + states + events, reviewed with the team.

??? question "EX3 · Medium — Engineering says a feature will take 3 months; leadership wants it in 1."
    **What it tests:** negotiation and scope slicing.

    **Approach:** understand drivers → slice → defer risk → options with trade-offs → joint escalation.

    **Model answer:** “Understand what drives the estimate; find the smallest valuable slice; defer non-essential risk behind a flag; present options (1-month slice, 3-month full) with trade-offs; never commit dates on engineers' behalf. If needed, escalate jointly with an options paper.”

    **Assumptions & trade-offs:** a slice may need rework later.

    **Common mistakes:** pressuring engineers; promising leadership the impossible.

    **60-second answer:** slice + options + joint decision.

??? question "EX4 · Hard — A production incident is causing payment failures. What is your role as PM?"
    **What it tests:** incident leadership without overstepping.

    **Approach:** support the incident lead → quantify impact → communicate → remediate customers → review.

    **Model answer:** “Engineering leads the fix. I quantify user and business impact, coordinate communications (support, status page, leadership), decide customer remediation (refunds, messaging), and ensure a blameless post-incident review whose prevention items get prioritised.” *(Extra topic 13: don't declare it over just because the dashboard looks better briefly.)*

    **Assumptions & trade-offs:** speed vs accuracy of communications.

    **Common mistakes:** debugging instead of coordinating; skipping the review.

    **60-second answer:** impact, comms, remediation, review.

??? question "EX5 · Medium — How do you decide when a feature is ready to launch?"
    **What it tests:** quality bar and launch discipline.

    **Approach:** acceptance → quality gates → measurement → support → rollout plan.

    **Model answer:** “Acceptance criteria met; QA/UAT, performance, accessibility, security and privacy reviews done; tracking validated; support ready; rollout plan with flag and rollback owner; success and guardrail thresholds defined.”

    **Assumptions & trade-offs:** perfect vs good enough for a staged rollout.

    **Common mistakes:** launching without measurement or rollback.

    **60-second answer:** gates + measurement + rollback + support.

??? question "EX6 · Medium — How do you manage dependencies across teams?"
    **What it tests:** coordination and risk management.

    **Approach:** map early → agree interfaces → track → sequence → escalate with options.

    **Model answer:** “Map dependencies with owners, dates and risks; agree interface contracts; track them on a shared board; sequence work to unblock the critical path; hold short syncs; escalate early with options when blocked.”

    **Assumptions & trade-offs:** coordination overhead vs surprise risk.

    **Common mistakes:** discovering dependencies at integration time.

    **60-second answer:** map, contract, track, sequence, escalate early.

??? question "EX7 · Easy — What is the difference between Definition of Ready and Definition of Done?"
    **What it tests:** Agile fundamentals.

    **Approach:** define both → example → why both matter.

    **Model answer:** “Ready = criteria a team may use before starting an item (clear, estimated, testable). Done = shared quality criteria for completed work (tested, reviewed, documented, deployed per team rules).” *(Lecture 22.)*

    **Assumptions & trade-offs:** an over-strict Ready can block flow.

    **Common mistakes:** treating them as the same checklist.

    **60-second answer:** Ready = can start; Done = truly finished.

??? question "EX8 · Hard — After launch, adoption is low. What do you do?"
    **What it tests:** diagnosis and willingness to iterate or stop.

    **Approach:** measurement → exposure → segments → interviews → decide (improve, reposition, sunset).

    **Model answer:** “Check tracking; check exposure (did people even see it?); segment by user type; interview users who saw it but didn't use it; compare with the original hypothesis. Then improve onboarding or placement, iterate on value, or sunset. Low use alone isn't enough to remove a feature — persistent low value is.”

    **Assumptions & trade-offs:** sunk cost; maintenance cost of unused features.

    **Common mistakes:** adding promotions without understanding why.

    **60-second answer:** verify → exposure → why → decide.

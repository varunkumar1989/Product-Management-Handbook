---
id: m06
n: 6
title: Effective Communication and Stakeholder Management
subtitle: Lead without authority — structure your thinking, write clear PRDs, align stakeholders, negotiate trade-offs and communicate with every function.
summary: Pyramid Principle, SCQA, STAR, PREP, storytelling with data, stakeholder maps, RACI/DACI, negotiation, conflict, PRDs, one-pagers, user stories, exec reviews and real dialogue scripts.
hours: 9
status: drafted
sources: "Lectures 13, 14, 18, 22, 24, 30, 52, 53; Companion ch. 18, 19; Extra topics 11, 15"
---

!!! hypo "About the dialogues"
    Conversations in this module are **illustrative scripts** written to model technique. They are not transcripts of real meetings.

## Why communication is the PM's core tool

PMs rarely have formal authority over the people who build, sell or support the product. Influence comes from **clarity, evidence, trust and consistency.** Most PM failures are communication failures: unclear problems, unshared trade-offs, surprises, or decisions nobody wrote down.

**Principles**

1. **Start with the answer** (then support it).
2. **Know your audience** — what decision do *they* need to make, and what do they care about?
3. **Make trade-offs explicit** — options, cost, benefit, risk.
4. **Separate facts, assumptions and opinions** — label each.
5. **Write it down** — decisions, owners, dates.
6. **No surprises** — share bad news early, with a plan.
7. **Listen more than you talk** — especially with customers and engineers.

## Structured problem-solving communication

### The Pyramid Principle and SCQA

Barbara Minto's **Pyramid Principle**: lead with the governing thought (answer), group supporting arguments (ideally mutually exclusive and collectively exhaustive, **MECE**), and support each with evidence. **SCQA** frames the opening: **Situation → Complication → Question → Answer.**

```chart
type: tree
title: Pyramid structure for a recommendation (hypothetical)
root:
  label: "Recommendation: show the delivery fee in the cart this quarter"
  children:
    - label: "It addresses our biggest checkout leak"
      children:
        - label: "30% leave at the payment step (analytics)"
        - label: "6 of 8 interviewees cite fee surprise"
    - label: "It's cheap and low-risk"
      children:
        - label: "2 person-months; behind a feature flag"
        - label: "Fallback designed if the fee service fails"
    - label: "We can prove it worked"
      children:
        - label: "A/B test, 10k users per arm, 14 days"
        - label: "Guardrail: complaint rate ≤ 1.3%"
caption: The answer comes first; each branch is a reason; leaves are evidence. Executives can stop reading at any level and still have the point.
```

```chart
type: steps
title: SCQA — how to open any update, memo or pitch
steps:
  - ["Situation", "Shared, uncontroversial context"]
  - ["Complication", "What changed or what's wrong"]
  - ["Question", "The question this raises"]
  - ["Answer", "Your recommendation — then the pyramid of support"]
caption: Executives should be able to stop after the Answer and still act. Everything after it is supporting evidence.
```

!!! example "SCQA opening (hypothetical)"
    **Situation:** Checkout completion is 70% and is our largest growth lever this quarter. **Complication:** 30% of users leave at the payment step, and research says the fee surprises them. **Question:** What should we change first? **Answer:** Show the full fee breakdown in the cart, tested as an A/B experiment over two weeks.

### Executive summaries

An executive summary fits on one screen: **the ask/decision, the recommendation, why (2–3 bullets with numbers), risks and mitigations, what you need (people, money, decision by date).** Put it at the top of every doc.

!!! example "Executive summary template"
    **Decision needed by 15 May:** approve 2 engineers for 6 weeks to test early fee display.
    **Recommendation:** run an A/B test; ship only if checkout completion rises ≥ 2 points with no rise in complaints.
    **Why:** the payment step loses 30% of starters; 6/8 users cite fee surprise; est. +2,160 orders/month (range 720–4,320).
    **Risks:** fee estimate inaccuracy → label as estimate, fallback text; delay to loyalty work by 3 weeks.
    **Not doing:** loyalty redesign until Q3.

### STAR and PREP

* **STAR** (behavioural answers): **Situation, Task, Action, Result** — with *your* actions and a real result (or say it wasn't measured).
* **PREP** (quick opinions and updates): **Point, Reason, Example, Point** — great for meetings and 60-second answers.

```chart
type: compare
title: Choosing a communication structure
headers: ["Situation", "Structure", "Shape", "Typical length"]
rows:
  - ["Recommendation to leadership", "Pyramid + SCQA", "Answer → reasons → evidence", "1 page / 3 minutes"]
  - ["Behavioural interview story", "STAR", "Situation → Task → Action → Result", "2 minutes"]
  - ["Opinion in a meeting or stand-up", "PREP", "Point → Reason → Example → Point", "30–60 seconds"]
  - ["Feedback to a colleague", "SBI", "Situation → Behaviour → Impact → ask", "2 minutes"]
  - ["Bad news / incident", "What · impact · cause · plan · next update", "Facts first, then plan", "5 sentences"]
caption: Pick the structure by audience and purpose. All five put the most important information first.
```

!!! source "From your course notes (Lectures 18, 24)"
    Use STAR for experience-based interviews: explain the **Situation, your Task, the Actions you personally took, and the Result**, ideally with evidence. The instructor called the last part “reaction” but explained it as the result. *Tell the story naturally; do not invent outcomes.* If results were not measured, say so rather than inventing numbers.

!!! example "PREP in a stand-up (hypothetical)"
    **Point:** We should delay the loyalty launch by a week. **Reason:** payment errors spiked 3× after Tuesday's release. **Example:** 412 failed attempts yesterday vs ~130 normal. **Point:** let's fix payments first, then launch loyalty next Wednesday.

## Storytelling with data

Data persuades when it answers a question for a specific audience. Principles (in the spirit of Cole Nussbaumer Knaflic's *Storytelling with Data*):

1. **Lead with the takeaway as the chart title** (“Checkout loses most users at payment”), not “Funnel Q1”.
2. **Choose the right chart:** trend → line; comparison → bar; part-to-whole with few parts → stacked bar; distribution → histogram; relationship → scatter. Avoid 3D and pie charts with many slices.
3. **Remove clutter;** highlight the one thing that matters with colour.
4. **Give context:** baseline, target, comparison period, sample size.
5. **Show uncertainty** (ranges, confidence intervals).
6. **End with the action** you want.

```chart
type: hbar
title: Checkout loses the most users at the payment step (hypothetical)
items: [["Cart → Checkout start", 30], ["Checkout start → Address", 8], ["Address → Payment step", 6], ["Payment step → Order placed", 30]]
fmt: pct
highlight: 3
caption: Drop-off at each step (% of users entering the step). The title states the takeaway; colour highlights the step the recommendation targets. Hypothetical data.
```

## Stakeholder mapping and influence

**Stakeholder mapping** identifies who matters and how to engage them. The **power–interest grid**: *manage closely* (high power, high interest), *keep satisfied* (high power, low interest), *keep informed* (low power, high interest), *monitor* (low, low).

```chart
type: scatter
title: Power–interest grid for a checkout redesign (hypothetical)
points:
  - {label: "VP Product", x: 8, y: 9}
  - {label: "Head of Payments", x: 9, y: 7.5}
  - {label: "Finance", x: 4, y: 8}
  - {label: "Legal / Compliance", x: 3, y: 7}
  - {label: "Customer Support", x: 8.5, y: 4}
  - {label: "Marketing", x: 6, y: 3.5}
  - {label: "Restaurant partners", x: 3, y: 2.5}
xlabel: "Interest in this initiative (1–10)"
ylabel: "Power over the outcome (1–10)"
xmax: 10
ymax: 10
quad: ["Keep satisfied", "Manage closely", "Monitor", "Keep informed"]
caption: Hypothetical placement. Re-map as the project changes; a low-interest, high-power stakeholder (Legal) can block a launch late if ignored.
```

**Decision-rights frameworks**

* **RACI** — **R**esponsible (does the work), **A**ccountable (one person owns the outcome), **C**onsulted (two-way input), **I**nformed (kept updated).
* **DACI** — **D**river (runs the decision process), **A**pprover (one person decides), **C**ontributors, **I**nformed. Useful for product decisions.

```chart
type: compare
title: DACI for "Ship early fee display?" (hypothetical)
headers: ["Role", "Who", "What they do"]
rows:
  - ["Driver", "PM, Checkout", "Frames options, gathers evidence, schedules the decision"]
  - ["Approver", "Head of Product", "Makes the call by the agreed date"]
  - ["Contributors", "Design, Eng lead, Analytics, Payments, Legal", "Provide input, risks, estimates"]
  - ["Informed", "Support, Marketing, Sales", "Told the decision and its implications"]
caption: One approver per decision. Writing this down before the debate prevents most escalations.
```

**Influence without authority — what actually works:** shared goals (“we both want fewer failed payments”), evidence, reciprocity (help others hit *their* goals), early involvement (“co-authors defend what they wrote”), credibility through follow-through, and making it easy to say yes (clear asks, small first steps).

## Cross-functional collaboration

| Partner | What they need from you | What you need from them | Common friction |
|---|---|---|---|
| Engineering | Clear problem, priorities, early involvement, stable scope | Estimates, risks, technical options | Late requirement changes; dates set without them |
| Design | Problem, evidence, constraints, time to explore | Flows, prototypes, research partnership | Solution-first requests; skipping research |
| Data / Analytics | Questions, decisions, tracking needs early | Definitions, analysis, experiment design | Ad-hoc requests with no decision attached |
| Marketing / PMM | Positioning inputs, launch dates, user value | Messaging, launch plans, market feedback | Late notice; overpromising |
| Sales | Roadmap context, honest timelines | Customer feedback, deal blockers | Promising features to close deals |
| Support / Ops | Release notes, known issues, training | Ticket trends, customer pain | Launches without support readiness |
| Legal / Compliance | Early sight of data use and claims | Risk assessment, approvals | Brought in at the last minute |

## Negotiation and conflict resolution

**Negotiation** principles (from *Getting to Yes*, Fisher & Ury): separate the **people** from the problem; focus on **interests**, not positions; invent **options** for mutual gain; use **objective criteria**; know your **BATNA** (best alternative to a negotiated agreement).

!!! example "Interests, not positions (hypothetical)"
    **Position (Sales):** “We need custom reports for Client X by June.” **Interest:** keep a renewal worth ₹40 lakh; client's finance team needs monthly numbers. **Options:** scheduled CSV export (2 weeks), template report in existing tool (1 week), full custom reports (3 months). **Objective criteria:** revenue at risk, number of other clients asking, engineering cost. **Outcome:** ship the scheduled export now; evaluate custom reports in Q3 planning.

```chart
type: canvas
title: Positions versus interests (hypothetical Sales vs Product example)
cols: 2
cells:
  - {title: "Sales position", tone: r, text: ["“Build custom reports for Client X by June.”"]}
  - {title: "Product position", tone: r, text: ["“Not this quarter — checkout comes first.”"]}
  - {title: "Sales interest", tone: g, text: ["Keep a ₹40 lakh renewal", "Client's finance team needs monthly numbers"]}
  - {title: "Product interest", tone: g, text: ["Hit the checkout-completion goal", "Avoid one-off custom features"]}
  - {title: "Options that serve both", tone: b, span: 2, text: ["Scheduled CSV export in 2 weeks (meets the client's job)", "Custom reports evaluated in Q3 with evidence from other clients"]}
caption: Positions collide; interests usually overlap. Find the options in the bottom row before arguing about the top row.
```

**Conflict modes** (Thomas–Kilmann): competing, collaborating, compromising, avoiding, accommodating.

```chart
type: scatter
title: Thomas–Kilmann conflict modes
points:
  - {label: "Competing", x: 2, y: 9}
  - {label: "Collaborating", x: 9, y: 9}
  - {label: "Compromising", x: 5.5, y: 5.5}
  - {label: "Avoiding", x: 2, y: 2}
  - {label: "Accommodating", x: 9, y: 2}
xlabel: "Cooperativeness (attention to the other side's concerns)"
ylabel: "Assertiveness (attention to your own concerns)"
xmax: 10
ymax: 10
caption: Conceptual positions, not measurements. No mode is always right — match it to stakes, time and relationship.
```

PMs default to **collaborating** for important, high-trust issues; **compromising** for time-bound trade-offs; **accommodating** on low-stakes items to build goodwill; **avoid** only for trivia.

**A conflict-resolution sequence:** (1) restate each side's interest until they agree you understood; (2) agree on the shared goal and decision criteria; (3) lay out options with evidence; (4) decide — or escalate *together* with a joint summary; (5) document and move on.

## Decision-making meetings

* **Before:** circulate a one-page decision brief 24–48 hours ahead (context, options, recommendation, evidence, open questions); state the decision type (decide, consult, inform).
* **During:** confirm the decision and decider; walk through options and trade-offs; invite dissent explicitly (“what would make this wrong?”); decide or agree what information is missing.
* **After:** within 24 hours send the decision, rationale, owner, next steps and review date.

```chart
type: steps
title: Anatomy of a decision meeting
steps:
  - ["Pre-read (T−48h)", "1-page brief: context, options, recommendation"]
  - ["Frame (5 min)", "Decision, decider, criteria"]
  - ["Options (15 min)", "Trade-offs and evidence"]
  - ["Dissent (10 min)", "“What would make this wrong?”"]
  - ["Decide (5 min)", "Or name the missing information"]
  - ["Record (T+24h)", "Decision, rationale, owner, review date"]
caption: Most of the work happens before and after the meeting. If nobody read the pre-read, spend the first five minutes reading it together.
```

!!! source "From your course notes (Extra topic 11)"
    Before a meeting, share a one-page decision brief. During the meeting name the options, trade-offs and open questions. Afterward record the **decision, accountable owner, rationale and next review date.** *Disagreement is useful when it reveals an overlooked risk.*

## Writing PRDs

A **PRD** aligns the team on the problem and intended solution. It is a living document, sized to the team's needs.

!!! source "From your course notes (Lecture 14; Companion ch. 4, 19)"
    The demonstrated PRD includes **objective, target users, goals, success metrics, requirements, design links, out-of-scope items and open questions.** Choose metrics that reflect the particular problem (business, user and technical measures); sample targets are not validated forecasts. **Use AI for a first draft, not a source of truth** — check invented assumptions, numbers, privacy and accuracy before sharing. A Confluence page can link to Jira items and design files; version history explains what changed; **access permissions should match the audience.** Discuss estimates without blame: ask engineers about complexity, testing, risks and dependencies, then explain trade-offs.

```chart
type: canvas
title: PRD skeleton
cols: 2
cells:
  - {title: "1 · Summary & decision", tone: b, text: ["One paragraph: problem, proposal, expected impact", "Status, owner, reviewers, last updated"]}
  - {title: "2 · Problem & evidence", tone: v, text: ["Who, what task, why it's hard", "Data, research, quotes (with sample sizes)"]}
  - {title: "3 · Goals & success metrics", tone: g, text: ["Primary outcome metric and target", "Leading indicators; guardrails"]}
  - {title: "4 · Users & use cases", text: ["Segments/personas", "Key scenarios and edge cases"]}
  - {title: "5 · Scope", text: ["In scope / out of scope", "Assumptions and dependencies"]}
  - {title: "6 · Requirements", text: ["User stories + acceptance criteria", "Non-functional: performance, security, accessibility, privacy"]}
  - {title: "7 · Design & analytics", text: ["Links to flows/prototypes", "Tracking plan (events, properties)"]}
  - {title: "8 · Launch & risks", tone: w, text: ["Rollout plan, flags, rollback", "Risks + mitigations; open questions; decision log"]}
caption: The full reusable template is in the Templates library. Keep the summary on top; link rather than duplicate detail.
```

!!! example "Mini-PRD: Show estimated total before checkout (hypothetical)"
    **Problem.** First-time mobile buyers abandon at payment; 30% of checkout starters leave at that step; 6 of 8 interviewees said the fee surprised them.
    **Goal.** Checkout completion for first-time buyers 70% → 76% this quarter; guardrail: complaint rate ≤ 1.3%; payment-error rate unchanged.
    **In scope.** Item total + estimated delivery/platform fees and taxes in the cart; “est.” labels; refresh on address change; fallback “Estimate unavailable” with retry.
    **Out of scope.** Changing the fee policy; personalised fees.
    **User story.** *As a first-time buyer, I want to see my estimated total in the cart so that I can decide before I start paying.*
    **Acceptance criteria (Gherkin).**
    *Given* an eligible address, *when* the user opens the cart, *then* show item price, estimated fees, taxes and estimated total.
    *Given* the fee service fails, *when* the cart loads, *then* show “Estimate unavailable” and a keyboard-accessible Retry, and never display an invented fee.
    *Given* the user changes the address, *when* the cart reloads, *then* the estimate refreshes within 2 seconds (p95).
    **Non-functional.** WCAG 2.2 AA; no PII in analytics events; works on 3G within 3 s (p95).
    **Analytics.** `fee_displayed` {fee_amount, is_estimate, source}; `fee_estimate_failed` {error_code}.
    **Rollout.** Feature flag; A/B 50/50; 14 days; kill switch owner: Eng lead.
    **Open questions.** Should the fee estimate include surge? Legal wording for “estimate”?

```chart
type: layers
title: How a PRD connects to delivery tools
rows:
  - ["One-pager (why this, why now)"]
  - ["PRD in Confluence / Docs (problem, metrics, scope)"]
  - ["Figma designs", "Jira epic", "Tracking plan"]
  - ["User stories + acceptance criteria", "QA test cases"]
  - ["Release, experiment readout, decision log"]
edges:
  - ["One-pager (why this, why now)", "PRD in Confluence / Docs (problem, metrics, scope)", "approved"]
  - ["PRD in Confluence / Docs (problem, metrics, scope)", "Figma designs"]
  - ["PRD in Confluence / Docs (problem, metrics, scope)", "Jira epic"]
  - ["PRD in Confluence / Docs (problem, metrics, scope)", "Tracking plan"]
  - ["Jira epic", "User stories + acceptance criteria"]
  - ["User stories + acceptance criteria", "QA test cases"]
  - ["User stories + acceptance criteria", "Release, experiment readout, decision log"]
caption: The PRD explains why and what; Jira tracks how and when. Link them both ways so a reader can trace any ticket back to the problem it solves.
```

### User stories and acceptance criteria

* **User story:** *As a [user], I want [capability] so that [benefit].*
* **INVEST** checklist: Independent, Negotiable, Valuable, Estimable, Small, Testable.
* **Acceptance criteria:** testable conditions, often written **Given / When / Then.**
* **Definition of Ready** (criteria before work starts) vs **Definition of Done** (quality criteria for completed work).

### Writing one-pagers

A **one-pager** pitches an idea before a full PRD: problem, why now, who, proposed approach, expected impact (with range), cost, risks, the ask. If you can't write it on one page, the idea isn't clear yet. (Amazon popularised the related **PR/FAQ** — a mock press release and FAQ written before building — as a way to test whether the customer benefit is compelling.)

### Jira and Confluence in the workflow

!!! source "From your course notes (Lecture 13; Companion ch. 18, 19)"
    Jira helps teams track work items, workflows and delivery: projects contain work; boards present items by status; teams use stories, tasks, bugs and epics — *terminology and workflows vary.* **A sprint is a Scrum time-box, not a mandatory feature of every team.** Beginner exercise: create a work item “Show estimated total before checkout” with user, outcome, scope and acceptance criteria; move it through the existing workflow. Review boards for blocked and ageing items; **discuss causes rather than treating story points as individual productivity.** Confluence organises pages in spaces; a page can hold a PRD, decision log, research summary or launch checklist; link Jira items; record the decision and date when scope changes; **pages are not automatically safe for every audience.**

## Engineering collaboration

* **Involve engineers in discovery** — they often see the simplest solution.
* **Ask for estimates as ranges with assumptions,** not commitments on the spot.
* **Story points** are relative effort for a team's planning — not a productivity score and not comparable across teams.
* **Trade scope, not quality:** offer smaller slices before asking for overtime.
* **Respect technical debt** — reserve capacity; understand the cost of delay of not fixing it.
* **Be available** during the sprint to answer questions quickly.

!!! example "Dialogue — negotiating scope with an engineering lead (illustrative)"
    **PM:** “Our goal is to stop the fee surprise for first-time buyers this quarter. What's the simplest version you'd build?”
    **Eng lead:** “Showing a static fee is easy. A live estimate needs the pricing service — three weeks, and it's flaky at peak.”
    **PM:** “What if v1 shows the estimate when the service responds within 500 ms and otherwise ‘Estimate unavailable’? Would that cut the time?”
    **Eng lead:** “Then it's about ten days. We'd add a cache later.”
    **PM:** “Great. Let's take that, put it behind a flag and A/B it. I'll update the PRD and note the cache as a follow-up. Anything else risky?”
    **Eng lead:** “Analytics events — let's define them now so QA can check them.”
    *Why it works:* goal first, asks for the simplest option, trades scope not quality, records the follow-up.

## Communicating with every function — dialogue examples

!!! example "With senior leadership (illustrative)"
    **VP:** “Why isn't loyalty on the Q2 roadmap?”
    **PM:** “Short answer: checkout completion is a bigger, faster lever. We lose 30% of buyers at payment; fixing that is worth an estimated 2,000+ orders a month, and it takes 6 weeks. Loyalty only helps people who complete checkout. I'd like your approval to run the checkout test first, and I'll bring a loyalty proposal to the Q3 review with the test results.”
    *Technique:* answer first, number, trade-off, specific ask, follow-up date.

!!! example "With design (illustrative)"
    **PM:** “Six of eight users missed the fee. I'm not attached to any layout — what are the options you see?” **Designer:** “A breakdown in the cart, or a sticky total bar.” **PM:** “Can we test both with five users next week and decide using task success?”

!!! example "With analytics (illustrative)"
    **PM:** “The decision is whether to ship early fee display. I need: completion per eligible user by variant, complaint rate, and a power estimate for detecting +2 points.” **Analyst:** “At 70% baseline that's about 8,000 users per arm.” **PM:** “Then we run 14 days. Can we pre-register the metric definitions in the doc?”

!!! example "With operations / support (illustrative)"
    **PM:** “From Monday, 50% of users will see an estimated fee in the cart. Here's the help article and three macros. If customers say ‘the fee changed’, tag it `fee_estimate` — I'll review tags daily during the test.”

!!! example "With a customer (illustrative)"
    **Customer:** “Your app always surprises me with fees.” **PM:** “I'm sorry — that's exactly what we're trying to fix. Could you walk me through the last time it happened? What did you expect to see?” *(Listen; don't defend; don't promise dates.)* “Thank you. We're testing a change that shows the full estimate earlier; may I follow up to get your feedback?”

## Handling conflicting priorities and difficult stakeholders

**Conflicting priorities:** bring them to a common yardstick (the goal and a framework such as RICE or cost of delay), make trade-offs visible, escalate *jointly* if needed with a one-page options paper, and record the decision.

**Difficult stakeholders — patterns and responses**

| Pattern | Response |
|---|---|
| The HiPPO (highest-paid person's opinion) | Ask for the goal behind the idea; propose a test; show data respectfully |
| The bulldozer (“just build it”) | Acknowledge urgency; show cost of delay of displaced work; offer a smaller slice |
| The silent blocker | 1:1 conversation; ask what would make them comfortable; involve early |
| The scope-creeper | Refer to the agreed scope and decision log; queue new asks for the next cycle |
| The customer-promiser (sales) | Shared rule: no commitments without PM sign-off; give roadmap themes, not dates |

!!! source "From your course notes (Extra topic 11)"
    Stakeholders have different incentives: sales may want a customer request, engineering may need reliability work, users may want a faster experience. **Clarify the shared outcome, evidence, constraints and decision rights instead of promising every request.**

## Customer empathy

Empathy is *understanding the customer's situation and feelings well enough to make better decisions* — not agreeing with every request. Practise it through regular customer calls, listening to support calls, reading tickets, using the product as a new user, and shadowing operations.

## Giving and receiving feedback

**SBI model:** **Situation** (when/where), **Behaviour** (observable, not judgement), **Impact** (effect on you, team, user). Then ask, listen and agree next steps.

!!! example "SBI (illustrative)"
    “In yesterday's review (S), the PRD's success metric changed from completion to clicks without a note (B). Engineering built tracking for the old metric and lost a day (I). Could we add a change log to the PRD so everyone sees updates?”

**Receiving feedback:** thank, clarify, don't defend in the moment, decide what to act on, close the loop.

```chart
type: compare
title: Tiered stakeholder communication cadence (example)
headers: ["Audience", "Format", "Cadence", "Contents"]
rows:
  - ["Leadership", "One-page update", "Weekly / fortnightly", "Metrics vs target, decisions needed, risks"]
  - ["Cross-functional partners", "Channel post + sync", "Weekly", "Progress, blockers, upcoming asks"]
  - ["Support & sales", "Release notes + FAQ", "Per release", "What changed, how to explain it, known issues"]
  - ["Whole company", "Demo / newsletter", "Monthly", "Outcomes and learnings"]
  - ["Anyone affected by an incident", "Incident message", "Immediately, then on a schedule", "Impact, plan, next update time"]
caption: Match depth and frequency to each audience's decisions. No surprises — risks go out early, through the channel the audience actually reads.
```

## Leadership communication and executive product reviews

Executives want: **the decision you need, how it serves the strategy, the numbers, the risks, and what you're not doing.** Prepare for an exec review:

1. **One-page memo** at the top (or a 6-page narrative memo in memo-culture companies).
2. **Metrics vs targets** with honest status (green/amber/red with reasons).
3. **Learnings** — what surprised you, what you stopped.
4. **Decisions needed** — clearly listed.
5. **Appendix** for detail; anticipate the three hardest questions.

**Delivering bad news:** state it plainly, the impact, the cause (if known), what you're doing, what you need, when you'll update next.

## Exercises with model answers

!!! question "Exercise 1 · Rewrite an update with the Pyramid Principle"
    Original: “We did lots of analysis this week. We looked at funnels, did interviews, talked to payments, and engineering thinks it's 2 months. Fees might be a problem. Also loyalty is pending.”

??? answer "Model answer"
    “**Recommendation:** test showing the delivery fee in the cart, starting next sprint. **Why:** (1) 30% of checkout starters leave at payment; (2) 6 of 8 interviewees cite fee surprise; (3) engineering estimates a simplified v1 at ~2 weeks (full live estimate ~2 months). **Ask:** approve the two-week v1 and an A/B test; loyalty moves to Q3.”

!!! question "Exercise 2 · Acceptance criteria"
    Write three Given/When/Then criteria for “saved addresses”.

??? answer "Model answer"
    *Given* a logged-in user with no saved addresses, *when* they complete an order with a new address, *then* offer “Save this address” (unchecked by default). *Given* a user with saved addresses, *when* they open checkout, *then* show up to 5 most recent addresses with the last used pre-selected. *Given* a saved address fails validation, *when* it is selected, *then* show a plain-language error and an Edit option without losing the cart.

!!! question "Exercise 3 · Stakeholder map"
    For launching a fintech card-application redesign, place six stakeholders on a power–interest grid and give one engagement action each.

??? answer "Model answer (example)"
    Manage closely: Head of Risk (co-design KYC changes), Compliance (review copy and consent). Keep satisfied: CFO (monthly KPI summary). Keep informed: Customer Support (training and macros), Marketing (launch messaging). Monitor: partner bank's ops team (notify of timeline). Re-map after the pilot.

## Interview perspective

??? question "“Tell me about a time you influenced without authority.” — STAR model answer outline"
    **S:** Team wanted to build a feature a large client requested; I believed checkout reliability was more urgent. **T:** Align sales, engineering and my VP on priorities. **A:** Pulled funnel data and support tags, quantified lost orders, met sales to understand the client's real need, proposed a 2-week workaround for the client, and presented options with a recommendation. **R:** We fixed payment retries first; failed-payment recoveries rose (state the real measured number — or say it wasn't measured); the client accepted the workaround and renewed. **Learning:** start with shared goals and offer options. *Mistake to avoid:* inventing results or describing only what the team did.

??? question "“How would you communicate a delayed launch to executives?” — 60-second answer"
    “I'd tell them as soon as I know, in one message: the launch will slip by two weeks; the cause is a payment-gateway certification we underestimated; the impact is roughly X orders and no customer-facing risk; options are to launch without the new payment method or wait; my recommendation is to wait because the old flow is the main pain point; and I'll update them every Friday until launch. Then I'd document the learning for future estimates.”

## Key takeaways

* **Answer first** (Pyramid/SCQA); support with MECE reasons and evidence.
* Use **STAR** for stories and **PREP** for quick points; never invent outcomes.
* Make **decision rights** explicit (RACI/DACI) and write decisions down.
* Negotiate on **interests**, with options and objective criteria.
* PRDs are **living alignment tools**: problem, metrics, scope, testable requirements, risks.
* Tailor to each function's needs; **no surprises.**

## Check your understanding

```quiz
- q: "The Pyramid Principle recommends…"
  options:
    - "Building up to the conclusion at the end"
    - "Starting with the answer, then grouped supporting arguments"
    - "Listing all data first"
    - "Using only charts"
  answer: 1
  why: "Lead with the governing thought, then MECE support and evidence."
- q: "In DACI, who makes the final decision?"
  options:
    - "Driver"
    - "Approver"
    - "Contributors"
    - "Informed"
  answer: 1
  why: "The Approver decides; the Driver runs the process."
- q: "Which is a well-formed acceptance criterion?"
  options:
    - "The page should be fast."
    - "Given an eligible address, when the cart opens, then show the estimated total."
    - "Make the cart better."
    - "Users will like it."
  answer: 1
  why: "Acceptance criteria are specific and testable, often Given/When/Then."
- q: "Focusing on interests rather than positions means…"
  options:
    - "Agreeing to every request"
    - "Understanding the need behind a demand to find better options"
    - "Refusing to negotiate"
    - "Escalating immediately"
  answer: 1
  why: "Interests reveal options that satisfy the underlying need."
- q: "Story points are best described as…"
  options:
    - "A measure of individual productivity"
    - "Relative effort estimates for a team's planning"
    - "Hours of work"
    - "Comparable across all teams"
  answer: 1
  why: "Story points are team-relative planning estimates, not productivity scores."
```

## Recommended resources

* Barbara Minto, *The Pyramid Principle* — [publisher page](https://www.barbaraminto.com/).
* Cole Nussbaumer Knaflic, [*Storytelling with Data*](https://www.storytellingwithdata.com/).
* Fisher, Ury & Patton, *Getting to Yes* — [Harvard Program on Negotiation](https://www.pon.harvard.edu/).
* [Atlassian: DACI decision-making framework](https://www.atlassian.com/team-playbook/plays/daci).
* [Atlassian Support: Create a Jira work item](https://support.atlassian.com/jira-software-cloud/docs/create-a-work-item-and-a-subtask/) and [Use Jira and Confluence together](https://support.atlassian.com/confluence-cloud/docs/use-jira-and-confluence-together/) (from your course notes).
* [Center for Creative Leadership: SBI feedback model](https://www.ccl.org/articles/leading-effectively-articles/closing-the-gap-between-intent-vs-impact-sbii/).

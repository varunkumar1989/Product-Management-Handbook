---
id: m03
n: 3
title: Problem Discovery and Market Research
subtitle: Find problems worth solving: research methods, interviews and surveys, personas, jobs-to-be-done, journeys, synthesis and evidence quality.
summary: Customer discovery end to end — with interview scripts, bias checklists, JTBD, journey maps, opportunity solution trees, review mining and assumption testing.
hours: 10
status: drafted
sources: "Lectures 3, 4, 5, 6, 7, 8, 11, 19, 28, 36; Companion ch. 2, 3; Picture lesson 'Product discovery and design'"
---

!!! hypo "About examples"
    Personas, quotes, review counts and estimates are **invented** to teach technique. They are not research findings about any real product or user group.

## What discovery is

**Product discovery** is the work of learning *what is worth building* before (and while) building it: who has the problem, how painful it is, how they cope today, and whether your idea would be chosen and used. **Customer discovery** focuses on understanding customers; **problem validation** tests that the problem is real, frequent and painful enough to matter.

!!! level1 "Level 1 · Beginner"
    Discovery = talking to people and watching what they do, so you build the right thing. If you can only ask “Would you use my idea?”, you will mostly hear polite yeses.

!!! source "From your course notes (Lectures 6, 8; Picture lesson)"
    **Validate the problem before investing heavily in a solution.** Ask whether the need is real, who experiences it, how people solve it today and whether the opportunity is worth pursuing. *A solution is a hypothesis to test, not a guaranteed success.* Start with a user and a task; ask about a recent real experience; watch the task where appropriate; look for repeated difficulties. **Do not assume an idea is useful simply because someone says it sounds nice.**

```chart
type: steps
title: A discovery cycle
steps:
  - ["Frame", "Problem hypothesis and target segment"]
  - ["Collect", "Interviews, observation, data, reviews, support tickets"]
  - ["Synthesise", "Affinity map, themes, journey, JTBD"]
  - ["Test", "Assumption tests, prototypes, smoke tests"]
  - ["Decide", "Pursue, pivot or stop — and record why"]
caption: Discovery repeats; each loop is cheap relative to building. Most teams under-invest in Synthesise and Decide.
```

## Research methods: qualitative and quantitative, primary and secondary

Two different axes — *do not confuse them*:

| | Qualitative (why / how) | Quantitative (how many / how much) |
|---|---|---|
| **Primary** (you collect it) | Interviews, observation, diary studies, usability tests, moderated focus groups | Surveys, A/B tests, instrumented behaviour in your own product |
| **Secondary** (already exists) | Support tickets, app-store reviews, forums, published case studies | Market reports, public statistics, company databases, benchmarks |

!!! source "From your course notes (Lecture 6)"
    **Qualitative and quantitative describe the kind of evidence, not alternatives to primary research.** Interviews give qualitative insight into *why*; a well-designed survey can estimate *how common* a behaviour is. Both can be primary. A **focus group** is a moderated research discussion — *not another name for a target audience.* Ten interviews reveal useful clues but do not establish the habits of an entire city.

```chart
type: compare
title: Choosing a method by question
headers: ["Question you have", "Best-fit method", "What you get", "What you don't get"]
rows:
  - ["Why do users abandon checkout?", "Interviews + session observation", "Reasons, context, language", "How common each reason is"]
  - ["How many abandon at the fee step?", "Funnel analytics", "Counts and rates", "Why"]
  - ["Which of three designs is clearer?", "Usability test (5–8 per round)", "Where people struggle", "Statistical proof"]
  - ["Which price converts better?", "A/B or priced pilot", "Behaviour at scale", "Reasons behind it"]
  - ["How big is the segment?", "Bottom-up sizing + survey", "An estimate with assumptions", "Proof of demand"]
  - ["What do users say publicly about rivals?", "Review mining", "Themes and vocabulary", "Representative opinion"]
caption: Mix methods: use analytics to find *where*, interviews to learn *why*, experiments to test *whether the fix works* (triangulation).
```

## Customer interviews

### Principles

1. **Ask about the past, not the future.** “Tell me about the last time you ordered lunch” beats “Would you use an app that…?”
2. **Seek stories, then specifics:** what triggered it, what alternatives they considered, what happened, how they felt, what they did next.
3. **Stay neutral:** don't pitch; don't lead; tolerate silence.
4. **Recruit for contrast:** include people who tried and churned, people who never tried, power users — not only fans.
5. **Consent and privacy:** explain purpose, record only with permission, remove identifying details in notes.
6. **Debrief fast:** write observations separately from interpretations within 24 hours.

!!! source "From your course notes (Lecture 3; Companion ch. 2)"
    Interview a student who buys lunch. Ask *“Tell me about the last time you ordered lunch.”* If they say they missed delivery fees, watch where they expected to see the price. **Five interviews can reveal problems but cannot establish their population frequency.** Recruit a range of users including those who abandoned and those who did not; get consent; avoid leading questions; remove identifying information; compare themes with quantitative data.

### Question design

| Weak (leading / hypothetical) | Stronger (past behaviour, neutral) |
|---|---|
| “Would you pay for faster delivery?” | “Last time you were in a hurry, what did you do about food?” |
| “Do you find our checkout confusing?” | “Walk me through placing your last order. What did you look at first?” |
| “Don't you hate hidden fees?” | “How did you decide whether the total was acceptable?” |
| “Is price important to you?” | “Tell me about a time you decided *not* to order because of the cost.” |
| “What features do you want?” | “What did you do the last time this didn't work?” |

### Sample interview script (45 minutes)

!!! example "Script: ordering food after work (hypothetical study)"
    **Opening (5 min).** “Thanks for your time. I'm learning how people decide about dinner on weekdays. There are no right answers; I'm not testing you. May I record audio for my notes only? I'll remove names.”
    **Warm-up (5 min).** “Tell me about your typical weekday evening.”
    **Core story (20 min).** “Think about the last time you ordered food from an app on a weekday. What was happening before you opened it?” → “What did you do first?” → “What else did you consider?” → “What were you looking at when you decided?” → “Was there a moment you almost gave up?” → “What did you do next?”
    **Probe the friction (10 min).** “You mentioned the total changed at the end — what did you expect to see?” → “How did that feel?” → “What did you do?”
    **Wrap-up (5 min).** “Is there anything I should have asked?” → “Who else should I speak to?” → thank, explain next steps.
    **Don't:** pitch your idea, ask about features, or suggest answers.

### Recording the evidence

Use a two-column note sheet: **Observation** (what they did/said, verbatim where possible) | **Interpretation** (your hypothesis). Tag each observation with the participant ID and the journey stage.

## Surveys and questionnaire bias

A **survey** estimates *how common* something is — if the sample is representative and the questions are neutral.

**Common biases and fixes**

| Bias | What happens | Fix |
|---|---|---|
| **Leading question** | Wording nudges the answer (“How great was…?”) | Neutral wording; balanced scales |
| **Double-barrelled** | Two questions in one (“fast and cheap?”) | One idea per question |
| **Social desirability** | People give flattering answers | Anonymity; behaviour (“last week, how many times…?”) |
| **Acquiescence** | Tendency to agree | Mix positively and negatively worded items; use specific choices |
| **Order effects** | Earlier questions prime later ones | Randomise; put sensitive items last |
| **Sampling / self-selection** | Respondents differ from the population | Define the frame; track response rate; compare with known figures |
| **Hypothetical bias** | Stated intent ≠ behaviour | Prefer behavioural questions; validate with a real action |
| **Incentive bias** | Rewards attract the wrong people | Screen carefully; use modest incentives |

!!! source "From your course notes (Lecture 6; Lecture 10)"
    *The claim that “90% of survey responses are biased” was not substantiated;* sampling, incentives and question design can introduce bias but do not make surveys inherently invalid. **A survey preference is not proof that respondents will purchase.**

**Sample survey questions (rewritten)**

* Bad: “Do you agree our app is easy and fast to use?” → Good: “In the past 7 days, how many times did you place an order? (0 / 1 / 2–3 / 4+)” and “How easy or difficult was it to find the total price on your last order? (Very difficult … Very easy)”.
* Bad: “Would you use a feature that tells you about fees?” → Good: “When you last saw a price at checkout, was the total different from what you expected? (Yes, higher / Yes, lower / No / Don't remember)”.

## Customer segmentation and personas

A **segment** is a group sharing a *relevant* need or behaviour. A **persona** is an illustrative profile of a segment — a communication aid, not proof everyone acts alike. Prefer **behavioural and need-based** segments over purely demographic ones.

!!! source "From your course notes (Lecture 3)"
    A target audience is a group a product or message is intended to reach. **The buyer and end user can be different** (FirstCry: a parent may buy while a child uses). Build and validate personas with research, *not guesses.* **There is no universal rule that every product needs two or three personas**, and choosing the largest segment alone does not prove product–market fit. The iPhone-user personas in class were exercise assumptions, not claims about all iPhone users. When needs conflict, consider market size, severity of need, strategic fit, feasibility and reachability; persona overlap is normal.

```chart
type: canvas
title: Persona template filled with a hypothetical example
cols: 3
cells:
  - {title: "Name & context", tone: b, text: ["“Asha”, 31, product analyst", "Works late 3–4 days a week", "Uses food apps on her commute"]}
  - {title: "Goals & motivations", tone: g, text: ["A reliable dinner without planning", "Keep weekday spend predictable"]}
  - {title: "Behaviours (from interviews)", tone: v, text: ["Re-orders favourites; checks total before paying", "Abandons if total jumps at last step"]}
  - {title: "Pains / frustrations", tone: r, text: ["Fees appear late", "Delivery estimates drift", "Unclear refund path"]}
  - {title: "Needs from the product", tone: b, text: ["Clear total early", "Trustworthy ETA", "One-tap reorder"]}
  - {title: "Evidence & confidence", tone: w, text: ["8 interviews (Mar 2026, hypothetical)", "Confidence: medium", "Open questions: what happens at month-end?"]}
caption: A persona is only as good as its evidence. Always record sample size, date and confidence, and update it when research changes.
```

## Jobs to Be Done (JTBD)

**JTBD** frames demand as **people “hiring” a product to make progress in a particular circumstance.** A **job statement** has the form:

```formula
When [situation], I want to [motivation / progress], so I can [desired outcome].
```

* Jobs have **functional**, **emotional** and **social** dimensions.
* The *competition* is whatever else gets hired for the job — including doing nothing.
* Uncover jobs from **switching stories**: what triggered the move, alternatives considered, what pushed them away from the old solution (push), what pulled them to the new one (pull), what anxieties held them back, what habits kept them in place — the **four forces**.

!!! example "Example (hypothetical): lunch"
    *When I'm in back-to-back meetings and have 15 minutes, I want to get a filling lunch without leaving my desk or being surprised by the cost, so I can stay focused and not blow my budget.*
    **Competing alternatives:** order in, ask a colleague to pick up, eat a snack, skip lunch, bring food. **Anxieties:** “Will it arrive in time? Will the price change?” **Implication:** reliability and total price clarity matter more than restaurant variety for this job.

```chart
type: canvas
title: The four forces of switching (hypothetical switch to a new meal-planning app)
cols: 2
cells:
  - {title: "Push (away from the current way)", tone: r, text: ["Wasted groceries", "Planning takes an hour"]}
  - {title: "Pull (toward the new solution)", tone: g, text: ["Weekly plan with a price estimate"]}
  - {title: "Anxiety (about the new solution)", tone: w, text: ["Will estimates be accurate? Will it fit our diet?"]}
  - {title: "Habit (of the present way)", tone: b, text: ["Family's recipe notebook; saved lists in notes app"]}
caption: A product wins when push + pull outweigh anxiety + habit. Discovery asks about each force; design and onboarding reduce anxiety.
```

!!! source "From your course notes (Lecture 21)"
    Jobs to be done asks what *progress users want to make in a situation*; first-principles thinking breaks a problem down to fundamental assumptions. The recording mainly refers learners to further material for these concepts — this section is independent reference material.

## Pain-point identification

List pains with **severity** (how bad), **frequency** (how often), **breadth** (how many people) and **current workaround** (the clearest sign of real pain: people already spend effort to solve it). Rank by severity × frequency × breadth, then by whether you can credibly solve it.

## Customer journey mapping and user flows

!!! source "From your course notes (Lecture 5; Companion ch. 3)"
    A **journey map** follows the *whole experience*, including actions, thoughts and feelings, across touchpoints; a **user flow** focuses on paths and decisions inside an interface; one journey can contain many flows. A **workflow** focuses on the sequence of activities, systems and decisions. Start with a concrete task, map the steps and important branches; use the appropriate level of detail. AI can brainstorm a first draft (give it problem, users, features, constraints) — **check it against the real product and do not copy it blindly.** Add the key branches: valid/invalid address, payment failure, retry, cancellation — and label the desired outcome for each. A remembered login session is not necessarily single sign-on.

```chart
type: steps
title: Journey: weekday dinner order (hypothetical, one persona)
steps:
  - ["Trigger", "Gets home late; no food planned"]
  - ["Search & compare", "Browses menus, compares ETA and price"]
  - ["Cart & total", "Reviews cart; fee appears late"]
  - ["Pay", "Chooses payment method; occasional failure"]
  - ["Wait & track", "Watches ETA; anxious if it drifts"]
  - ["Receive & reflect", "Eats; rates; decides whether to reorder"]
caption: Journey stages are the rows of a map; add rows for actions, thoughts, emotions, touchpoints, pain points and opportunities.
```

```chart
type: line
title: Emotion curve across the journey (hypothetical, from 8 interviews)
xs: ["Trigger", "Search", "Cart & total", "Pay", "Wait", "Receive"]
series:
  "Average mood (1 = frustrated, 5 = delighted)": [2.5, 3.6, 2.1, 2.4, 2.8, 4.1]
ylabel: "mood"
ymin: 1
ymax: 5
caption: Hypothetical. The two lowest points — the cart total and payment — point to where discovery and design effort should focus.
```

### Opportunity Solution Trees (OST)

Teresa Torres's **Opportunity Solution Tree** connects a **desired outcome** to the customer **opportunities** (needs, pains, desires) and then to **solutions** and **experiments**. It prevents jumping from outcome straight to a favourite feature.

```chart
type: tree
title: Opportunity Solution Tree (hypothetical)
root:
  label: "Outcome: raise checkout completion 70% → 76%"
  children:
    - label: "Opportunity: surprised by total at the end"
      children:
        - label: "Solution: show fee early (A/B test)"
        - label: "Solution: running total in cart"
    - label: "Opportunity: payment fails with no recovery"
      children:
        - label: "Solution: retry with another method"
        - label: "Solution: save cart and notify"
    - label: "Opportunity: long form on first order"
      children:
        - label: "Solution: guest checkout / fewer fields"
caption: Each solution should be paired with the cheapest experiment that tests it. Compare opportunities (not just solutions) when you prioritise.
```

## Competitor research, review mining and support-ticket analysis

**Review mining** turns public reviews and support tickets into themes and a vocabulary. **Method:** (1) sample reviews across ratings and dates; (2) code each into themes (one review can have several); (3) count and read representative quotes; (4) note sampling limits; (5) turn themes into hypotheses.

!!! hypo "Worked example — coding 40 synthetic app reviews"
    | Theme | Mentions | Share of 40 reviews |
    |---|---:|---:|
    | Late delivery | 11 | 27.5% |
    | Fees / total unclear | 9 | 22.5% |
    | Food quality | 7 | 17.5% |
    | App crashes at payment | 6 | 15.0% |
    | Slow support | 4 | 10.0% |
    | Good discounts (positive) | 3 | 7.5% |

```chart
type: hbar
title: Themes in 40 synthetic reviews (hypothetical)
items: [["Late delivery", 11], ["Fees / total unclear", 9], ["Food quality", 7], ["App crashes at payment", 6], ["Slow support", 4], ["Good discounts (positive)", 3]]
caption: Synthetic data for teaching coding. With 40 reviews you can form hypotheses, not estimate the share of all customers. Reviews over-represent extreme experiences.
```

!!! source "From your course notes (Lecture 39)"
    The class sampled a public dataset, asked an AI tool for sentiment and potential themes (reliability, pricing, safety, support). **Review individual comments and sampling bias; a small sample cannot establish the full market's sentiment.** Public datasets can be real, synthetic or mixed — check provenance and licence. Never upload confidential data without authorisation.

## Behavioural analytics and observation

* **Behavioural analytics** (funnels, cohorts, session replays where permitted) shows *what* people do at scale (Module 7).
* **Observational research** — watching users perform tasks (in context if possible) reveals what they cannot articulate: workarounds, hesitations, misreadings. Think-aloud usability testing is a form of observation.
* Always combine: analytics finds *where*; observation and interviews find *why*.

## Research synthesis

### Affinity mapping

Write each observation on a note; cluster by similarity (silently first, then discuss); name clusters as **insights** (“Users distrust totals that change at the end”), not topics (“Pricing”); count participants per cluster.

```chart
type: canvas
title: Affinity map output (hypothetical, 8 participants)
cols: 3
cells:
  - {title: "Insight A · 6 of 8", tone: r, text: ["“The total jumped at the end.”", "“I didn't see delivery fee until payment.”", "“I wasn't sure what I was paying.”"]}
  - {title: "Insight B · 4 of 8", tone: w, text: ["“If payment fails I start over.”", "“I switched to cash once.”"]}
  - {title: "Insight C · 3 of 8", tone: b, text: ["“I just want to reorder my usual.”", "“Saved addresses save me time.”"]}
caption: Hypothetical. Report counts as “6 of 8 participants”, never percentages from a handful of interviews.
```

### Assumption mapping and hypothesis generation

List every assumption behind the idea (desirability, usability, feasibility, viability). Plot on **importance** (how fatal if wrong) vs **evidence** (how much we know). Test the **important, low-evidence** assumptions first.

```chart
type: scatter
title: Assumption map (hypothetical meal-planning app)
points:
  - {label: "Parents plan weekly", x: 2, y: 8.5}
  - {label: "Users trust price estimates", x: 1.5, y: 9}
  - {label: "Grocers share price data", x: 1.8, y: 7.5}
  - {label: "Users pay ₹1,200/yr", x: 2.5, y: 8}
  - {label: "App stores allow affiliate links", x: 8, y: 3}
  - {label: "Users want recipes", x: 7, y: 6}
xlabel: "Evidence we have (1 = none, 10 = strong)"
ylabel: "Importance if wrong (1–10)"
xmax: 10
ymax: 10
quad: ["Test first", "Keep monitoring", "Ignore for now", "Fine"]
caption: Hypothetical. Top-left (important, little evidence) is where experiments should start.
```

**Hypothesis template:** *We believe that [change/solution] for [segment] will [expected outcome/metric] because [reason/evidence]. We will know we are right when [measurable signal].*

## Problem validation and evidence quality

**Triangulation** means reaching a conclusion from multiple independent kinds of evidence. Grade evidence honestly:

| Strength | Evidence | Example |
|---|---|---|
| **Strong** | Observed behaviour at scale; randomised experiments; paid pilots | Conversion lift in an A/B test; people paying a real price |
| **Medium** | Repeated behaviour in small samples; consistent interview themes; usability test patterns | 6 of 8 users miss the fee in a task |
| **Weak** | Stated intent, opinions, single anecdotes, AI-generated claims, “I would use this” | Survey says 80% “would try” |

!!! source "From your course notes (Lectures 6, 28, 41)"
    Label comparisons based on impressions as **hypotheses**; support material claims with suitable research, sources and methodology. **Do not present AI-generated target numbers as evidence** — one team acknowledged the tool invented its metrics. **A student's own experience is a starting point, not proof of a widespread problem.**

## Guesstimates (estimation)

A **guesstimate** breaks an unknown number into smaller numbers you can explain, state assumptions for, and sanity-check — and gives a **range**.

!!! source "From your course notes (Lecture 7)"
    Clarify the question first (geography, typical day vs special event, ride types, whether cancelled requests count — *keep definitions consistent*). Break into measurable assumptions; **explain and sanity-check** each; compare **top-down and bottom-up**; communicate a range and the assumptions that matter most. The class estimates were **practice figures, not verified Uber statistics.** *There is no single right answer, but arithmetic errors, inconsistent definitions or implausible assumptions make an estimate weak.* Simple example: 1,000 students × 60% at school × 50% buying lunch = 300 lunches.

!!! hypo "Worked example — daily ride-hailing trips in a large metro (practice numbers, not facts)"
    **Top-down:** metro population 20 million → adults 70% = 14.0 million → people who use ride-hailing at least weekly: 8% = 1.12 million → 3 trips per week each = 3.36 million trips/week → **≈ 480,000 trips/day.**
    **Bottom-up (supply check):** active drivers per day 55,000 × 9 completed trips per driver per day = **≈ 495,000 trips/day.**
    **Reconcile:** two independent approaches land within ~3% — *this raises confidence but both rest on assumptions I invented.* Give a range: **450k–500k/day**, and name the most uncertain assumptions (share of weekly users, trips per driver). Sanity check: 480k trips/day ÷ 14M adults ≈ 3.4% of adults ride each day — plausible for a big city.

**Structure to use in interviews:** clarify → choose approach (top-down or bottom-up) → segment → state assumptions → compute → sanity-check → give range → discuss what would change it.

## Product critique and teardown

A **teardown** studies a product from the outside to understand users, goal, journey, strengths and possible improvements. Separate **observations** from **assumptions**; an outsider cannot know a company's internal data.

!!! source "From your course notes (Lectures 4, 19, 28)"
    A critique explains **the user, the task, the difficulty and the expected benefit.** Suggested teardown sequence: product context and problem → vision/purpose → personas → user and market research → journey and pain points → prioritised opportunities → proposed solution → success metrics (adapt it to the question). Each claim needs evidence and each change needs a test. Student proposals in class (Myntra, Amazon, X, ChatGPT, Netflix) were *proposals and observations, not verified gaps.* Consider constraints such as content rights and contracts.

!!! example "Teardown skeleton (use for any product)"
    1. **Product & user:** what job; for whom; business model (assumption, label it).
    2. **Journey:** 5–7 stages; where does it help; where does it hurt (evidence: your own walk-through, reviews, tests).
    3. **Opportunity:** one problem; evidence; who is affected; size (assumption).
    4. **Solutions:** 2–3 options incl. a non-AI/simple one.
    5. **Choice:** impact/effort/risk; recommendation.
    6. **Measurement:** primary metric; guardrails; experiment.
    7. **Risks and unknowns.**

## Discovery exercises

!!! question "Exercise 1 · Rewrite the questions"
    Rewrite three poor interview questions and explain the bias in each: (a) “Do you think our onboarding is too long?” (b) “Would you pay ₹99/month for this?” (c) “What features would make you love this app?”

??? answer "Model answer"
    (a) Leading and closed → “Walk me through your first time setting up the app. Where did you hesitate?” (b) Hypothetical bias → “What do you pay for today to solve this? How did you decide it was worth it?” (c) Solution-seeking; customers aren't product designers → “Tell me about the last time this task went badly. What did you do?”

!!! question "Exercise 2 · Evidence grading"
    You have: (1) 8 interviews, 6 mention surprise at fees; (2) a funnel showing a 30% drop at the fee step; (3) a survey where 78% say they “like transparent pricing”. Rank the evidence and state what you would do next.

??? answer "Model answer"
    (2) funnel = behavioural, scalable (strong *that* a drop exists, not why). (1) interviews = medium (consistent reasons, small sample). (3) survey = weak (stated preference, hypothetical). Next: segment the funnel (device, new/returning), run a usability task on the fee screen, then test early fee display in an A/B experiment with a complaint guardrail.

!!! question "Exercise 3 · Estimate"
    Estimate how many cups of coffee are sold in a city of 5 million in a day. Show two methods and a range.

??? answer "Model answer (example)"
    **Top-down:** 5M × 70% adults = 3.5M; 55% drink coffee ≈ 1.9M; 1.8 cups/day from cafés/vending/home? Only 35% bought outside → 1.9M × 1.8 × 0.35 ≈ **1.2M purchased cups/day**. **Bottom-up:** 2,500 cafés × 250 cups = 625k + 1,500 kiosks × 300 = 450k + vending/office 100k ≈ **1.18M**. Range 0.9–1.4M. Sensitive to share who buy outside and cups per café.

## Source-flagged corrections

* Qualitative/quantitative ≠ primary/secondary.
* Focus group ≠ target audience.
* Persona count is not fixed; personas must be evidence-based.
* “Surveys don't work in some country” is unsupported; design matters.
* AI summaries of research need source checking.

## Interview perspective

??? question "“How would you validate a problem before building?” — 60-second answer"
    “I'd start with a clear problem hypothesis and target segment, then interview 8–10 people who've recently experienced it, asking about their last real experience and what they do today. I'd look at available data to size and locate the problem, mine reviews or support tickets for patterns, and write down the assumptions that could kill the idea. For the riskiest assumption I'd run the cheapest test — a prototype or a smoke test with a real price — and decide in advance what result would make me continue, pivot or stop.”

??? question "“Tell me about a product you love and how you'd improve it.”"
    *Tests:* product sense, empathy, prioritisation, honesty about evidence. *Structure:* user + job → why it works → one meaningful pain (with evidence you'd gather) → 2–3 solutions → pick one with trade-offs → metric + guardrail + experiment. *Mistakes:* naming five features, ignoring constraints (content rights, privacy, cost), assuming your own experience is universal.

## Key takeaways

* Discovery reduces **risk** by learning *before* building. Treat solutions as hypotheses.
* Ask about **past behaviour**; recruit for contrast; separate observation from interpretation.
* Match method to question; **triangulate** (analytics → interviews → experiment).
* Surveys estimate frequency but suffer from bias — design carefully.
* Use **JTBD**, journey maps, OSTs and assumption maps to structure what you learn.
* Grade evidence honestly; label hypotheses and AI-generated claims.

## Check your understanding

```quiz
- q: "Which is an example of secondary quantitative research?"
  options:
    - "A survey you design and send"
    - "A published market report with spending figures"
    - "Five customer interviews"
    - "A usability test"
  answer: 1
  why: "Secondary research uses existing information; quantitative means numeric evidence. A published report fits both."
- q: "Which interview question is best?"
  options:
    - "Would you use an app that shows fees early?"
    - "Don't you hate surprise fees?"
    - "Tell me about the last time the total changed at checkout."
    - "Which features do you want?"
  answer: 2
  why: "It asks about a specific past experience, is neutral and invites a story."
- q: "In the four forces of switching, 'anxiety' refers to…"
  options:
    - "Frustration with the current solution"
    - "Attraction to the new solution"
    - "Worries about trying the new solution"
    - "Inertia of habit"
  answer: 2
  why: "Push and pull move people toward switching; anxiety and habit hold them back."
- q: "6 of 8 interviewees mention the fee surprise. How should you report it?"
  options:
    - "75% of customers dislike hidden fees"
    - "6 of 8 interviewed participants mentioned it; frequency in the population is unknown"
    - "It's statistically significant"
    - "Ignore it; the sample is too small"
  answer: 1
  why: "Small qualitative samples reveal themes, not population percentages."
- q: "On an assumption map, which should you test first?"
  options:
    - "High importance, low evidence"
    - "Low importance, high evidence"
    - "Low importance, low evidence"
    - "High importance, high evidence"
  answer: 0
  why: "Assumptions that would sink the idea and that you know little about carry the most risk per test."
- q: "A guesstimate gives 480k/day top-down and 495k/day bottom-up. The right conclusion is…"
  options:
    - "The answer is exactly 487,500"
    - "Confidence is higher but both depend on assumptions; give a range"
    - "Both are wrong"
    - "Use the larger number"
  answer: 1
  why: "Agreement of independent methods raises confidence, but communicate a range and the key assumptions."
```

## Recommended resources

* [Nielsen Norman Group: Heuristic evaluations](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/) (from your course list) and [user interviews](https://www.nngroup.com/articles/user-interviews/).
* [Product Talk: Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-tree/).
* Rob Fitzpatrick, *The Mom Test* — asking good questions about past behaviour ([book site](https://www.momtestbook.com/)).
* [Jobs to Be Done — Christensen Institute](https://www.christenseninstitute.org/jobs-to-be-done/).
* [Google Cloud / Google: Gen AI glossary](https://cloud.google.com/learn/what-is-artificial-intelligence) for AI-assisted research caveats.

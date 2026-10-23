---
id: jtbd
title: Jobs to Be Done (JTBD)
category: Discovery
order: 20
summary: People "hire" products to make progress in a specific situation; understand the job, not the demographic.
---

```chart
type: canvas
title: JTBD model — job statement and the four forces
cols: 2
cells:
  - {title: "Job statement", tone: b, span: 2, text: ["When [situation], I want to [motivation], so I can [expected outcome]."]}
  - {title: "Push (away from today)", tone: r, text: ["Frustrations with the current way"]}
  - {title: "Pull (toward new)", tone: g, text: ["Attraction of the new solution"]}
  - {title: "Anxiety (about new)", tone: w, text: ["Fears and uncertainties"]}
  - {title: "Habit (of today)", tone: v, text: ["Inertia, sunk costs, routines"]}
caption: Switching happens when push + pull > anxiety + habit.
```

**Use when:** discovering demand; understanding competition broadly (including non-consumption); positioning. **Don't use when:** you need usability detail (use testing) or market sizing.

**Worked example (hypothetical):** *When I'm in back-to-back meetings with 15 minutes to eat, I want a filling lunch at my desk without surprise costs, so I can stay focused and on budget.* Competitors: snacks, colleagues, skipping lunch. Implication: reliability and price clarity beat variety.

**How to run:** interview recent switchers about the *timeline* of their decision (first thought → passive looking → active looking → decision → first use); map forces; write 2–4 job statements; validate frequency with data.

**Limitations:** interpretive; job statements can become vague slogans; needs good interviewing. **Template:** job statement · situation triggers · desired outcomes (measurable) · current alternatives · push/pull/anxiety/habit evidence. **Deep dive:** Module 3.

<!-- item -->
---
id: journey-map
title: Customer Journey Mapping
category: Discovery
order: 21
summary: Visualise a persona's stages, actions, thoughts, emotions, touchpoints and pain points end to end.
---

```chart
type: line
title: Journey emotion curve (hypothetical)
xs: ["Aware", "Consider", "Purchase", "Wait", "Use", "Support"]
series:
  "Emotion (1–5)": [3.2, 3.6, 2.3, 2.6, 4.0, 2.1]
ylabel: "emotion"
ymin: 1
ymax: 5
caption: Rows of a full map: stages · actions · thoughts · emotions · touchpoints · pain points · opportunities. Low points are where to look first.
```

**Use when:** aligning teams on the end-to-end experience; finding cross-channel gaps (app + support + delivery). **Don't use when:** you need screen-level flow detail (use a user flow) or have no research to base it on.

**Worked example (hypothetical):** weekday dinner journey — lowest points at “cart total” (fee surprise) and “support” (slow refunds). Opportunities: show total early; proactive refund status.

**Limitations:** can become a beautiful poster nobody uses; averages hide segment differences. **Template:** columns = stages; rows = actions, thoughts/quotes, emotion score, touchpoints, pains, opportunities, owners, metrics. **Deep dive:** Modules 3 and 5.

<!-- item -->
---
id: ost
title: Opportunity Solution Tree
category: Discovery
order: 22
summary: Connect a desired outcome to customer opportunities, candidate solutions and the experiments that test them.
---

```chart
type: tree
title: OST model
root:
  label: "Desired outcome (metric)"
  children:
    - label: "Opportunity A (customer need)"
      children:
        - label: "Solution A1 → experiment"
        - label: "Solution A2 → experiment"
    - label: "Opportunity B"
      children:
        - label: "Solution B1 → experiment"
caption: Compare opportunities before solutions; test multiple solutions per opportunity.
```

**Use when:** continuous discovery with a clear outcome; avoiding solution-first thinking; communicating why you're working on something. **Don't use when:** you lack an agreed outcome, or the work is mandatory (compliance).

**Worked example:** outcome = checkout completion 70% → 76%; opportunities: fee surprise, payment-failure dead ends, long first-order form; solutions and tests as in Module 3.

**Limitations:** requires ongoing research to stay true; can grow unwieldy. **Template:** outcome · opportunities (from interviews, with evidence) · ≥ 3 solutions per chosen opportunity · assumption tests. **Deep dive:** Module 3.

<!-- item -->
---
id: design-thinking
title: Design Thinking
category: Design
order: 23
summary: Empathise, define, ideate, prototype, test — an iterative, human-centred problem-solving approach.
---

```chart
type: steps
title: Design Thinking stages
steps:
  - ["Empathise", "Understand people"]
  - ["Define", "Frame the problem"]
  - ["Ideate", "Generate options"]
  - ["Prototype", "Make it tangible"]
  - ["Test", "Learn with users"]
caption: Non-linear; testing often loops back to Define or Ideate.
```

**Use when:** ambiguous problems, new experiences, cross-functional workshops. **Don't use when:** the problem and solution are well understood and the risk is delivery, not discovery.

**Worked example:** checkout redesign — empathise (interviews: fee surprise) → define (“first-time buyers can't see total before paying”) → ideate (8 concepts) → prototype (2 Figma variants) → test (6 users; task success 50% → 83%).

**Limitations:** workshops without real users become theatre; can neglect business viability and feasibility. **Template:** problem statement · research insights · how-might-we questions · concepts · prototype plan · test tasks · learnings. **Deep dive:** Module 5.

<!-- item -->
---
id: double-diamond
title: Double Diamond
category: Design
order: 24
summary: Discover and define the right problem, then develop and deliver the right solution — diverge, converge, twice.
---

```chart
type: steps
title: Double Diamond (Design Council)
steps:
  - ["Discover (diverge)", "Research widely; question assumptions"]
  - ["Define (converge)", "Synthesise into a clear problem"]
  - ["Develop (diverge)", "Explore many solutions; co-design"]
  - ["Deliver (converge)", "Test, refine, launch"]
caption: First diamond = right problem; second = right solution. Teams often skip the first.
```

**Use when:** planning a discovery-to-delivery project and explaining to stakeholders why time goes into problem definition. **Don't use when:** for small iterative changes.

**Worked example:** a fintech onboarding project spends 3 weeks in Discover (interviews, funnel analysis), converges on “document upload fails on low-end phones,” then explores 5 solutions and delivers camera guidance + save-and-resume.

**Limitations:** looks linear; real work loops. **Template:** for each diamond: activities, outputs, decision gate, owner. **Deep dive:** Module 5.

<!-- item -->
---
id: lean-startup
title: Lean Startup
category: Discovery
order: 25
summary: Reduce waste by testing business hypotheses with MVPs, validated learning and pivot-or-persevere decisions.
---

```chart
type: canvas
title: Lean Startup principles
cols: 3
cells:
  - {title: "Validated learning", tone: b, text: ["Progress = what you learned with evidence"]}
  - {title: "MVP", tone: v, text: ["Smallest experiment to test a key assumption"]}
  - {title: "Innovation accounting", tone: g, text: ["Baseline → tune → measure progress on actionable metrics"]}
  - {title: "Pivot or persevere", tone: w, text: ["Change strategy based on evidence, not ego"]}
  - {title: "Actionable vs vanity metrics", tone: r, text: ["Cohort-based, causal metrics over totals"]}
  - {title: "Small batches", text: ["Ship small, learn fast"]}
caption: Popularised by Eric Ries (The Lean Startup, 2011).
```

**Use when:** high uncertainty about customer, problem, solution or business model. **Don't use when:** in highly regulated or safety-critical contexts where an “MVP” cannot be released without full assurance (use prototypes and simulations instead).

**Worked example:** meal-planning app — leap-of-faith assumptions: parents plan weekly; trust price estimates; will pay ₹1,200/yr. MVP sequence: fake door (demand) → concierge (value) → priced pilot (willingness to pay). Pivot if pilot conversion < 3%.

**Limitations:** misread as “ship low quality”; startup framing may not fit enterprise constraints. **Template:** assumptions ranked by risk · experiment per assumption · success threshold · decision. **Deep dive:** Module 4.

<!-- item -->
---
id: build-measure-learn
title: Build–Measure–Learn
category: Discovery
order: 26
summary: The Lean Startup feedback loop — minimise total time through the loop.
---

```chart
type: loop
title: Build–Measure–Learn loop
nodes: ["Ideas", "Build (MVP / prototype)", "Product", "Measure (data)", "Data", "Learn (decide)"]
kind: R
center: "Minimise loop time"
caption: Plan in reverse: decide what you need to learn, what to measure, then what to build.
```

**Use when:** iterating toward fit; structuring sprints around learning goals. **Don't use when:** measurement is impossible within a useful time frame (use qualitative tests instead).

**Worked example:** learn whether early fee display reduces surprise → measure task success in 6 usability sessions and later checkout completion in an A/B test → build a two-screen prototype, then a flagged feature.

**Limitations:** “Build” first framing can encourage building before learning; loops need clear decision rules. **Template:** learning question · metric and threshold · smallest build · result · decision (pivot/persevere/stop). **Deep dive:** Modules 4 and 7.

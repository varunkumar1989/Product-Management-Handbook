---
id: aarrr
title: AARRR (Pirate Metrics)
category: Metrics
order: 40
summary: Acquisition, Activation, Retention, Revenue, Referral — diagnose where growth leaks.
---

```chart
type: funnel
title: AARRR as a funnel (hypothetical monthly numbers)
stages: [["Acquisition: sign-ups", 10000], ["Activation: first order in 7 days", 4200], ["Retention: ordered again in 30 days", 1900], ["Revenue: ≥ 3 paid orders", 950], ["Referral: invited a friend", 240]]
caption: Hypothetical. Stages can overlap in time; referral can feed acquisition in a loop.
```

**Use when:** diagnosing a growth problem; organising a metrics dashboard; growth-team planning. **Don't use when:** applied with generic definitions — each stage must be defined for *your* product.

**Worked example:** activation (42%) and 30-day retention (45% of activated) are the biggest levers; improving activation by 5 points adds ~500 activated users/month at the same acquisition spend.

**Limitations:** linear view of a non-linear journey; ignores user value quality; no guardrails by default. **Template:** stage · event definition · metric · current · target · owner · top hypothesis. **Deep dive:** Module 7.

<!-- item -->
---
id: heart
title: HEART
category: Metrics
order: 41
summary: Google's UX metrics framework — Happiness, Engagement, Adoption, Retention, Task success — with Goals → Signals → Metrics.
---

```chart
type: compare
title: HEART with Goals–Signals–Metrics (example: search feature)
headers: ["Dimension", "Goal", "Signal", "Metric"]
rows:
  - ["Happiness", "Users find search satisfying", "Post-search rating", "Avg rating; % positive"]
  - ["Engagement", "Users rely on search", "Searches per active user", "Weekly searches per user"]
  - ["Adoption", "New users try search", "First search", "% new users searching in week 1"]
  - ["Retention", "Users keep searching", "Repeat search", "% searchers searching again next week"]
  - ["Task success", "Users find what they want", "Click/add-to-cart after search", "Search success rate; time to result"]
caption: Pick the dimensions that match your goal; you rarely need all five.
```

**Use when:** defining UX success for a feature or redesign. **Don't use when:** you need business-outcome metrics only (pair with North Star/AARRR).

**Worked example:** checkout redesign — Task success (completion rate, errors), Happiness (CSAT), Adoption (first-time buyer completion).

**Limitations:** survey-based happiness is noisy; engagement can conflict with wellbeing. **Template:** dimension · goal · signal · metric · baseline · target. **Deep dive:** Module 5.

<!-- item -->
---
id: hypothesis-testing
title: Hypothesis Testing
category: Experimentation
order: 42
summary: State a null hypothesis, set α in advance, compute a test statistic and p-value, report the effect with a confidence interval.
---

```chart
type: normal
title: Two-sided test at α = 0.05
z_crit: 1.96
observed: 2.16
caption: The course example (23/100 vs 37/100) gives z ≈ 2.16, p ≈ 0.031 — significant at 0.05, not at 0.01.
```

```formula
z = (p₂ − p₁) ÷ √[ p̂(1 − p̂)(1/n₁ + 1/n₂) ],   p̂ = (x₁ + x₂)/(n₁ + n₂)
p-value = P(result at least this extreme | H₀ true)
```

**Use when:** deciding whether an observed difference is likely to be more than noise. **Don't use when:** samples are tiny, assignment isn't random, or you're fishing across many metrics without correction.

**Worked example:** 7,000/10,000 vs 7,250/10,000 → z = 3.91, p ≈ 0.00009, 95% CI +1.25 to +3.75 pts (Module 7).

**Limitations:** p-values are widely misread (not the probability the variant works); significance ≠ importance. **Template:** H₀/H₁ · α · test · sample size/power · result (effect, CI, p) · decision. **Deep dive:** Module 7.

<!-- item -->
---
id: ab-testing
title: A/B Testing
category: Experimentation
order: 43
summary: Randomly assign users to control and variant, compare a pre-registered metric with guardrails.
---

```chart
type: steps
title: A/B testing workflow
steps:
  - ["Hypothesis", "Change, metric, segment, reason"]
  - ["Design", "Randomisation unit, MDE, guardrails"]
  - ["Size", "Sample per arm; duration in full weeks"]
  - ["Run", "Check SRM and data quality; don't peek-and-stop"]
  - ["Decide", "Effect + CI, guardrails, cost, segments"]
caption: Pre-register the primary metric and stop rule.
```

**Use when:** enough traffic, reversible change, measurable short-term outcome. **Don't use when:** low traffic, strong network effects/contamination, legal or safety changes, or long-horizon outcomes.

**Worked example:** sizing for 70% → 72% at α 0.05 and 80% power: ≈ **8,077 users per arm** (Module 7).

**Limitations:** novelty effects, interference between users, multiple-testing false positives, only measures what you instrument. **Template:** hypothesis · population · variants · primary metric · guardrails · MDE · n per arm · duration · analysis plan · decision rule. **Deep dive:** Module 7.

<!-- item -->
---
id: five-whys
title: Five Whys
category: Problem solving
order: 44
summary: Ask "why?" repeatedly to move from a symptom toward a systemic cause — verifying each step with evidence.
---

```chart
type: steps
title: Five Whys model
steps:
  - ["Problem", "Observable symptom"]
  - ["Why 1", "Immediate cause (evidence?)"]
  - ["Why 2", "Underlying cause (evidence?)"]
  - ["Why 3–4", "Process or system cause"]
  - ["Why 5", "Root cause hypothesis → test"]
caption: Around five, not exactly five. Each answer must be checked with data.
```

**Use when:** post-incident reviews, recurring defects, metric drops. **Don't use when:** problems have many interacting causes (use fishbone/systems thinking) or the exercise turns into blame.

**Worked example:** late orders → riders wait → food not ready → optimistic prep estimates → estimates ignore kitchen load → add live load signal (Module 4).

**Limitations:** single causal chain; depends on knowledge in the room. **Template:** problem · why 1–5 with evidence · root cause · countermeasure · owner · verification. **Deep dive:** Module 4.

<!-- item -->
---
id: pareto
title: Pareto Analysis
category: Problem solving
order: 45
summary: Sort causes by frequency (or impact) and focus on the vital few that drive most of the effect.
---

```chart
type: pareto
title: Complaint categories (synthetic, 100 complaints)
items: [["Late delivery", 38], ["Wrong items", 22], ["Fee confusion", 15], ["Payment failure", 12], ["App bugs", 8], ["Other", 5]]
caption: The top four categories account for 87% of complaints.
```

**Use when:** many issues compete for attention; support or defect triage. **Don't use when:** severity varies hugely (weight by impact, not count) or categories are poorly defined.

**Worked example:** fixing late delivery and wrong items addresses 60% of complaints; but payment failures may be more severe per case — weight by cost or harm before deciding.

**Limitations:** “80/20” is a heuristic, not a law; frequency ≠ importance. **Template:** category · count · % · cumulative % · severity weight · owner. **Deep dive:** Module 4.

<!-- item -->
---
id: first-principles
title: First Principles Thinking
category: Problem solving
order: 46
summary: Break a problem into fundamental truths and rebuild the solution, instead of reasoning by analogy.
---

```chart
type: steps
title: First-principles process
steps:
  - ["Goal", "What outcome do we need?"]
  - ["Assumptions", "List what we believe is fixed"]
  - ["Challenge", "Law of nature or just habit?"]
  - ["Fundamentals", "Keep only true constraints"]
  - ["Rebuild", "Design from the fundamentals"]
caption: Useful when an industry “standard” may be habit rather than necessity.
```

**Use when:** stuck in incremental thinking; cost structures seem fixed; designing something new. **Don't use when:** the problem is routine and well-solved — conventions (Jakob's law) exist for good reasons.

**Worked example:** “30-minute delivery promise because competitors promise it” → fundamentals: customers want reliability; costs are travel and wait → promise an honest live-load window instead.

**Limitations:** time-consuming; risk of ignoring hard-won conventions. **Template:** goal · assumption list · evidence for each · which are real constraints · new design options. **Deep dive:** Module 4.

<!-- item -->
---
id: systems-thinking
title: Systems Thinking
category: Problem solving
order: 47
summary: Map feedback loops, delays and side effects so you don't optimise one metric while breaking another.
---

```chart
type: loop
title: Balancing loop — notifications and fatigue (conceptual)
nodes: ["More notifications", "Short-term engagement up", "Notification fatigue", "Opt-outs and uninstalls rise"]
kind: B
center: "Balancing loop"
caption: The more you push, the more fatigue limits future reach. Guardrail: opt-out rate.
```

**Use when:** metrics move in unexpected directions; marketplaces; growth tactics with side effects; policy changes. **Don't use when:** a simple, isolated bug (use Five Whys).

**Worked example:** surge pricing increases supply (reinforcing for availability) but raises cancellations and mistrust (balancing) — add caps and fare transparency.

**Limitations:** diagrams can become complex; hard to quantify. **Template:** variables · links (+/−) · loops (R/B) · delays · leverage points · guardrail metrics. **Deep dive:** Module 4.

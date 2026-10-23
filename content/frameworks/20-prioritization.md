---
id: rice
title: RICE
category: Prioritization
order: 30
summary: Reach × Impact × Confidence ÷ Effort — compare comparable initiatives with explicit estimates.
---

```chart
type: hbar
title: RICE scores for a hypothetical backlog
items: [["Show delivery fee early", 32000], ["Order-again shortcut", 28000], ["Payment retry", 14400], ["Saved addresses", 12500], ["Dark mode", 8000], ["Voice ordering", 600]]
highlight: 0
caption: From datasets/rice_backlog.csv (hypothetical). Run a sensitivity check before trusting the order.
```

```formula
RICE = Reach × Impact × Confidence ÷ Effort
Impact scale: 3 massive · 2 high · 1 medium · 0.5 low · 0.25 minimal
Confidence: 100% high · 80% medium · 50% low      Effort: person-months (> 0)
```

**Use when:** many comparable items, some data on reach. **Don't use when:** comparing mandatory work, platform investments with diffuse reach, or items with unknowable impact.

**Worked example:** fee early = 40,000 × 2 × 0.8 ÷ 2 = **32,000**; voice ordering = 8,000 × 2 × 0.3 ÷ 8 = **600** (see Module 4 for all six and the stakeholder script).

**Limitations:** false precision; bias toward high-reach items; confidence is subjective. **Template:** feature · reach (unit, period, source) · impact (scale + rationale) · confidence (evidence) · effort (eng estimate) · score · notes on dependencies/risks. **Deep dive:** Module 4.

<!-- item -->
---
id: ice
title: ICE
category: Prioritization
order: 31
summary: Impact × Confidence × Ease (1–10 each) — fast ranking, popular for growth experiments.
---

```chart
type: hbar
title: ICE scores (hypothetical)
items: [["Show fee early", 448], ["Order-again shortcut", 432], ["Payment retry", 360], ["Saved addresses", 315], ["Dark mode", 192], ["Voice ordering", 42]]
caption: I × C × E on 1–10 scales. Some teams average the three instead of multiplying.
```

**Use when:** quick triage of experiment ideas with similar audiences. **Don't use when:** reach varies widely (use RICE) or decisions are high-stakes and need more rigour.

**Worked example:** fee early I8 × C8 × E7 = **448**; voice I7 × C3 × E2 = **42**.

**Limitations:** very subjective; easy to game; ignores reach and dependencies. **Template:** idea · hypothesis · I (why) · C (evidence) · E (effort note) · score · owner. **Deep dive:** Module 4.

<!-- item -->
---
id: moscow
title: MoSCoW
category: Prioritization
order: 32
summary: Must, Should, Could, Won't (this time) — negotiate scope for a fixed release or time-box.
---

```chart
type: canvas
title: MoSCoW model
cols: 4
cells:
  - {title: "Must", tone: r, text: ["Release fails without it"]}
  - {title: "Should", tone: w, text: ["Important, painful to omit"]}
  - {title: "Could", tone: b, text: ["Nice if time allows"]}
  - {title: "Won't (this time)", tone: v, text: ["Explicitly out of scope"]}
caption: Agree the release period and why each item sits where it does.
```

**Use when:** fixed-date releases, contract scope, MVP definition. **Don't use when:** ranking many items against each other (it doesn't order within categories).

**Worked example:** early-fee release — Must: estimate + labels + fallback; Should: refresh on address change; Could: “add ₹X to avoid fee” nudge; Won't: fee-policy change.

**Limitations:** “Must” inflation; no numeric basis. Guideline: keep Musts to roughly 60% or less of capacity. **Template:** item · category · rationale · owner · dependency. **Deep dive:** Module 4.

<!-- item -->
---
id: kano
title: Kano Model
category: Prioritization
order: 33
summary: Classify features as must-be, performance, attractive, indifferent or reverse based on satisfaction.
---

```chart
type: line
title: Kano curves (conceptual)
xs: ["None", "Basic", "Some", "Good", "Excellent"]
series:
  "Must-be": [-5, -1.5, -0.5, -0.2, 0]
  "Performance": [-5, -2.5, 0, 2.5, 5]
  "Attractive": [0, 0.2, 0.8, 2.5, 5]
ylabel: "satisfaction"
ymin: -5
ymax: 5
caption: Conceptual. Delighters decay into must-bes over time as expectations rise.
```

**Use when:** deciding what makes a competitive baseline vs a differentiator; planning releases that balance basics and delight. **Don't use when:** you lack enough respondents per segment, or need cost/feasibility trade-offs.

**Worked example:** payment confirmation = must-be; faster checkout = performance; surprise free dessert = attractive; dark mode = indifferent for most, performance for night-shift users.

**Limitations:** survey wording sensitivity; categories shift; ignores cost. **Template:** feature · functional question · dysfunctional question · answer distribution · category (see the evaluation table in Module 4). **Deep dive:** Module 4.

<!-- item -->
---
id: weighted-scoring
title: Weighted Prioritization (Scoring)
category: Prioritization
order: 34
summary: Score options against weighted strategic criteria and compare totals.
---

```chart
type: bar
title: Weighted scores (hypothetical)
cats: ["Payment retry", "Show fee early", "Saved addresses", "Voice ordering"]
series:
  "Weighted score (1–5)": [4.15, 3.95, 2.95, 1.8]
caption: Weights: impact 35%, revenue 25%, strategic fit 20%, ease 20%.
```

```formula
Score = Σ (weight_i × score_i)      weights sum to 100%
```

**Use when:** choosing among a few strategic initiatives where criteria differ from pure reach/effort. **Don't use when:** weights are set after seeing scores, or with too many criteria.

**Worked example:** payment retry 5×.35 + 4×.25 + 4×.20 + 3×.20 = **4.15** (Module 4 has all four).

**Limitations:** subjective scores; hides trade-offs inside a total. Test sensitivity by shifting weights ±10 points. **Template:** criteria + weights (agreed first) · anchored 1–5 scales · scores with rationale · total · sensitivity notes. **Deep dive:** Module 4.

<!-- item -->
---
id: cost-of-delay
title: Cost of Delay
category: Prioritization
order: 35
summary: Quantify the value lost per unit of time by not having something — make urgency explicit.
---

```chart
type: line
title: Cumulative value lost by delaying a feature worth ₹50,000/week (hypothetical)
xs: ["0 wk", "2 wk", "4 wk", "6 wk", "8 wk", "10 wk"]
series:
  "Value lost (₹ thousands)": [0, 100, 200, 300, 400, 500]
ylabel: "₹ thousands"
caption: Linear urgency profile. Others include fixed-date (value drops to zero after a deadline) and decaying (first-mover advantage).
```

```formula
Cost of Delay = value per unit time × delay
CD3 = Cost of Delay ÷ duration   (do highest first)
```

**Use when:** arguing for capacity, sequencing time-sensitive work, comparing urgent vs important. **Don't use when:** value per time can't be estimated even roughly.

**Worked example:** a 6-week delay of a ₹50,000/week feature costs **₹3,00,000** — compared with the ₹1,20,000 cost of a contractor to accelerate it.

**Limitations:** estimates are uncertain; urgency profiles differ. **Template:** item · value/week (range) · urgency profile · expected delay · CoD · duration · CD3. **Deep dive:** Module 4.

<!-- item -->
---
id: wsjf
title: WSJF (Weighted Shortest Job First)
category: Prioritization
order: 36
summary: Cost of Delay ÷ job size, using relative scores — favours small, urgent, valuable work.
---

```chart
type: hbar
title: WSJF ranking (hypothetical)
items: [["C · Gateway timeout fix", 6.67], ["A · Fee shown early", 3.2], ["B · Loyalty redesign", 2.0], ["D · Platform refactor", 1.63]]
highlight: 0
caption: Relative scales (e.g., 1, 2, 3, 5, 8, 13, 20). Scale each component across all jobs at once.
```

```formula
WSJF = (User/business value + Time criticality + Risk reduction/opportunity enablement) ÷ Job size
```

**Use when:** scaled-agile planning with many teams and competing epics. **Don't use when:** job sizes are unknown or political.

**Worked example:** C: (5 + 13 + 2) ÷ 3 = **6.67**; B: (13 + 8 + 5) ÷ 13 = **2.0** — the small urgent fix goes first.

**Limitations:** relative scores are subjective; can starve big strategic work. **Template:** job · value · time criticality · RR/OE · CoD · size · WSJF. **Deep dive:** Module 4.

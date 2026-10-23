---
id: m11
n: 11
title: Vibe Coding for Product Managers
subtitle: Use AI coding tools to turn ideas into testable prototypes — safely — and know exactly where a prototype ends and production engineering begins.
summary: Tools (Claude Code, Cursor, Copilot, Replit, Lovable, Bolt), prompt-to-prototype, Git/GitHub, HTML/CSS/JS, APIs, data, deployment, debugging, testing, security — plus a complete idea-to-deployed-prototype project.
hours: 10
status: drafted
sources: "Lectures 42, 43, 48, 49, 50; Companion ch. 20, 21, 22, 23, 24, 26, 28"
---

!!! warning "Tool details change fast"
    Features, pricing, credits and plan limits of AI coding tools change frequently. This module describes **categories and workflows** and links to official docs. Verify current terms in your own account before relying on any capability.

## What vibe coding means

**Vibe coding** is building software by describing what you want in everyday language and letting an AI coding tool write and change the code, iterating by testing the result and giving feedback. The term was popularised by Andrej Karpathy in early 2025.

!!! source "From your course notes (Lecture 42)"
    Vibe coding uses everyday-language instructions with an AI coding tool to create or change software. **The output can be useful but may contain mistakes or security problems.** Ask for a small app, try adding and removing data, then reload to see whether data was *actually saved*. Review generated code, permissions and dependencies; test real flows; **do not publish private data or assume a generated screen is production ready.** *The lecture's rigid distinction between “agentic AI” and “AI agents,” and its claim that app builders do not use models, are misleading — categories overlap.* Signing in with GitHub does not itself guarantee repository synchronisation.

!!! level1 "Level 1 · Beginner"
    Think of the AI as a very fast junior developer who never gets tired, sometimes misunderstands, and occasionally invents things. You are the product owner and tester: you describe, check, and decide.

## PM use cases

| Use case | Why it helps | Watch out for |
|---|---|---|
| Clickable/working prototypes for user tests | Test value and usability in days, not weeks | Users may think it's real — label it |
| Internal tools (dashboards, calculators) | Remove manual work | Data access and security |
| Data exploration scripts | Answer questions without waiting | Wrong joins, unverified numbers |
| Demos for stakeholders | Make an idea tangible | Demo ≠ feasible at scale |
| Learning technical concepts | Build to understand APIs, DBs | Don't ship learning code |
| Automating workflows | Save time on repetitive tasks | Unapproved access to company systems |

## AI coding tools — categories

| Category | Examples | Best for | PM-level caution |
|---|---|---|---|
| **Browser app builders** | Lovable, Bolt (bolt.new), Replit Agent | Prompt-to-app prototypes with hosting | Generated backends/auth need review; lock-in; costs |
| **AI code editors (IDEs)** | Cursor, VS Code + GitHub Copilot, Windsurf | Working in a real codebase with AI help | Need basic Git and code-reading skills |
| **Terminal / agentic coding tools** | Claude Code, OpenAI Codex CLI, GitHub Copilot agent mode | Multi-file changes, running tests, explaining code | Review every command and diff; permissions |
| **Inline completion** | GitHub Copilot suggestions | Faster typing for developers | Suggestions can be subtly wrong |
| **General assistants** | Claude, ChatGPT, Gemini (with artifacts/canvas features) | Small single-file prototypes, explanations | Move real work to a proper repo/environment |

```chart
type: scatter
title: Where AI coding tool categories sit (conceptual)
points:
  - {label: "General assistants", x: 1.8, y: 8.5, group: "Low setup"}
  - {label: "Browser app builders", x: 3.5, y: 9, group: "Low setup"}
  - {label: "AI code editors (IDEs)", x: 7, y: 6, group: "Needs a dev environment"}
  - {label: "Terminal / agentic tools", x: 8.5, y: 6.5, group: "Needs a dev environment"}
  - {label: "Inline completion", x: 8, y: 3, group: "Needs a dev environment"}
xlabel: "Control over code, environment and review (1–10)"
ylabel: "Speed from idea to something clickable (1–10)"
xmax: 10
ymax: 10
quad: ["Fast prototypes, less control", "Fast and controllable", "Slow, low control", "Controlled, needs skills"]
caption: Conceptual placement by category, not a benchmark of specific products. PMs often start top-left and move right as a prototype becomes something engineers will own.
```

!!! source "From your course notes (Companion ch. 20–23, 26)"
    **Claude:** request a small responsive prototype with dummy data; specify pages, flows, accessibility, error states and *no real payments*; preview it; then move to an approved environment for data, authentication, security review and deployment. **ChatGPT / Gemini:** use as tutor and drafter; verify facts; check account and organisational policies before uploading files. **Lovable:** a generated application is *not automatically secure, correct, accessible or production ready*; iterate one change at a time; map data ownership, authentication and access rules before connecting a backend; use test accounts and mock payments; review server-side authorisation and secret handling with an engineer. **Replit:** separate development from production; store secrets in approved secret management; review dependencies; set up monitoring and backups; confirm ownership, hosting costs and rollback before publishing. *Never paste real customer data into an unreviewed prototype.*

## Prompt-to-prototype workflow

```chart
type: steps
title: Prompt-to-prototype loop
steps:
  - ["Brief", "Problem, user, hypothesis, 3 core flows, constraints"]
  - ["Plan", "Ask the AI for a simple plan and stack; edit it"]
  - ["Build small", "One feature per prompt; run it"]
  - ["Test", "Happy path, errors, mobile, keyboard, reload"]
  - ["Commit", "Save a working version in Git"]
  - ["Repeat / deploy", "Next feature; deploy to a test URL"]
caption: Small steps with a working, committed version after each one is the single most important habit — it makes mistakes cheap to undo.
```

!!! source "From your course notes (Lectures 43, 48, 49)"
    Choose a familiar product or idea, identify a few core features, **build them in small increments and test each step.** *A screen containing a form is not necessarily connected to persistent storage* — verify the backend, permissions and data flow; a code repository is not automatically the application's live database. Tell the assistant your experience level and preferred technologies, ask for a simple plan, and refine from working pieces instead of accepting unnecessary complexity. When something fails, **report the actual symptoms**, inspect server and database setup, and ask the assistant to investigate.

**A good build prompt (template)**

```text
Context: I'm a PM testing a hypothesis: [one sentence]. Users: [who].
Build: a single-page web app using plain HTML, CSS and JavaScript (no frameworks, no build step).
Core flows: 1) … 2) … 3) …
Data: fictional sample data only; store state in localStorage.
Must handle: empty state, loading state, an error state where [service] fails (show a clear message, never invent data).
Accessibility: labels for inputs, keyboard operable, visible focus, buttons ≥ 44px tall, colour contrast ≥ 4.5:1.
Constraints: no external API keys, no real payments, no personal data. Mark the page "Prototype".
Output: index.html, style.css, app.js. Then explain how to run it and list what is simulated.
```

## Git and GitHub fundamentals

!!! source "From your course notes (Companion ch. 24; Lectures 49, 50)"
    A **repository** is a project folder with version history; a **branch** isolates work; a **commit** records a snapshot; a **pull request** proposes changes for discussion and review; a **merge** incorporates approved changes. *A merged PR is not necessarily deployed or validated in production.* Check repository visibility and **remove secrets before pushing**; if a secret is exposed, rotate it — deleting it from the latest file doesn't remove it from history. Create an appropriately private repository, review contents, push only when ready; **don't move employer code or data into personal accounts.**

```bash
git init
```

```bash
git add index.html style.css app.js README.md
```

```bash
git commit -m "Fee-Clear Cart: first working prototype"
```

```bash
git checkout -b fee-fallback
```

```bash
git push -u origin fee-fallback
```

| Concept | What to remember |
|---|---|
| `.gitignore` | List files never to commit (`.env`, `node_modules/`, data exports) |
| Commit messages | Say *why*, not just *what* |
| Branch + PR | Even solo, a PR gives a reviewable diff and history |
| Revert | `git revert <commit>` undoes a change safely by adding a new commit |
| Secrets | Use environment variables / secret managers; never in code or screenshots |

```chart
type: layers
title: A safe Git workflow for a prototype
rows:
  - ["main branch (always working)"]
  - ["feature branch: fee-fallback"]
  - ["Commit 1: fallback text", "Commit 2: retry button", "Commit 3: tests pass"]
  - ["Pull request: description + how tested"]
  - ["Review → merge to main → deploy test URL"]
edges:
  - ["main branch (always working)", "feature branch: fee-fallback", "git checkout -b"]
  - ["feature branch: fee-fallback", "Commit 1: fallback text"]
  - ["Commit 1: fallback text", "Commit 2: retry button"]
  - ["Commit 2: retry button", "Commit 3: tests pass"]
  - ["Commit 3: tests pass", "Pull request: description + how tested", "git push"]
  - ["Pull request: description + how tested", "Review → merge to main → deploy test URL"]
caption: Each commit is a save point you can return to. Main stays deployable; experiments live on branches.
```

## HTML, CSS and JavaScript fundamentals

* **HTML** gives structure and meaning: headings, lists, buttons, forms. Semantic HTML (`<button>`, `<label>`, `<main>`) is also what makes pages accessible.
* **CSS** controls presentation: layout (flexbox, grid), colour, spacing, responsive rules (`@media`).
* **JavaScript** adds behaviour: respond to clicks, update the page, call APIs, store data.

```html
<label>Delivery area
  <select id="area"><option value="near">Within 3 km</option></select>
</label>
<button id="pay" type="button" disabled>Pay</button>
```

```css
.pay { width: 100%; min-height: 44px; background: #2563EB; color: #fff; }
@media (max-width: 480px) { .wrap { padding: 12px; } }
```

```javascript
document.getElementById("pay").addEventListener("click", () => {
  document.getElementById("result").textContent = "Simulated order placed (no payment taken).";
});
```

## Building basic web applications, API integrations and databases

**Calling an API from JavaScript** (illustrative; a real API needs its own URL, authentication and terms):

```javascript
async function getForecast(city) {
  const res = await fetch(`https://api.example.com/forecast?city=${encodeURIComponent(city)}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);   // handle 4xx/5xx explicitly
  return res.json();
}
```

```chart
type: layers
title: Where secrets may and may not live
labels: ["Browser", "Server", "Provider"]
rows:
  - ["Your web page (public: anyone can read the code)"]
  - ["Serverless function (holds the API key in a secret store)"]
  - ["Third-party API (weather, payments, AI model)"]
edges:
  - ["Your web page (public: anyone can read the code)", "Serverless function (holds the API key in a secret store)", "request without key"]
  - ["Serverless function (holds the API key in a secret store)", "Third-party API (weather, payments, AI model)", "request with key"]
caption: The browser never sees the key. If an AI tool puts a key in app.js, move the call server-side and rotate the key.
```

Key rules: **never put secret API keys in frontend code** (anyone can read them) — call such APIs from a server or serverless function; handle failures, timeouts and rate limits; respect API terms.

**Data storage ladder for prototypes:**

| Option | Good for | Limits |
|---|---|---|
| Hard-coded sample data | Pure UX tests | Nothing persists |
| `localStorage` | Single-user demo persistence in one browser | Not shared, not secure, can be cleared |
| Spreadsheet/Airtable via an automation | Small shared datasets | Rate limits, access control |
| Managed backend (e.g., Supabase/Firebase) | Real multi-user prototypes with auth | **Configure access rules (e.g., row-level security) before real data**; costs |
| Your company's systems | Production | Requires engineering, security, compliance |

!!! source "From your course notes (Lectures 40, 43, 49)"
    Supabase is a broader platform with PostgreSQL and optional vector capabilities. **Database selection depends on actual workloads;** a vector database is not a replacement for a transactional database. A rental-management prototype used Python/FastAPI, HTML/CSS and SQLite; external payment integration was a possible extension, *not demonstrated as complete.* Use payment-provider **test environments** for prototypes; never handle real card details without safeguards; never store passwords in plaintext.

## Deployment fundamentals

* **Static hosting** (no server code): GitHub Pages, Netlify, Vercel, Cloudflare Pages — upload HTML/CSS/JS, get a URL.
* **App hosting** (server code + database): Replit deployments, Render, Railway, Vercel/Netlify functions, cloud providers.
* **Environments:** keep a *test* URL separate from anything real users rely on.
* **Before sharing a link:** remove secrets, check visibility, add a “prototype” banner, confirm data handling, and know how to take it down.

!!! source "From your course notes (Lecture 42; Lecture 35)"
    The demo connected a project to a Git repository and published a test URL — **verify the actual integration and visibility settings, then test the real user journey.** *A public prototype link alone does not establish exclusive ownership or access control.*

## Debugging and testing AI-generated code

```chart
type: loop
title: Debugging loop with an AI coding assistant
nodes: ["Reproduce the bug", "Read the real error (console, network, logs)", "Describe exact symptom to the AI", "Ask for the cause before a fix", "Apply the smallest fix", "Re-test and commit"]
kind: R
center: "One change per loop"
caption: The most common failure is skipping step 2 and asking the AI to “fix it” without evidence — it then guesses and changes unrelated code.
```

**Debugging loop:** reproduce → read the actual error (browser **Console**, **Network** tab, server logs) → tell the AI the exact symptom and error text → ask it to explain the cause before changing code → apply the smallest fix → re-test → commit.

**Testing generated code** (as a PM you can always do the first three):

1. **Manual test plan:** happy path, empty state, error states, invalid input, reload/persistence, mobile width, keyboard-only, slow network.
2. **Acceptance criteria** from your PRD, checked one by one.
3. **Ask the AI to write tests** — then read them: do they test behaviour you care about, or just that the code runs?
4. **Automated tests** (unit/integration/end-to-end) for anything that will live longer than a demo.
5. **Peer review** of the diff before merging.

## Security risks of generated code

| Risk | Example | Mitigation |
|---|---|---|
| **Exposed secrets** | API key hard-coded in `app.js` | Server-side calls; secret manager; scan repos |
| **Broken access control** | Any logged-in user can read all records | Server-side authorisation; DB access rules (e.g., RLS); test with two accounts |
| **Injection / XSS** | Rendering user text with `innerHTML` | Escape output; parameterised queries |
| **Insecure dependencies** | Outdated or non-existent (hallucinated) package names | Verify packages exist and are reputable; pin versions; scan |
| **Over-permissive tools** | Agent runs destructive commands | Review commands; least privilege; sandbox |
| **Data leakage** | Pasting customer data into prompts | Use dummy data; approved tools only |
| **Missing rate limits** | OTP/login endpoints can be abused | Rate limit; monitoring |

!!! warning "A note on the starter project"
    The Fee-Clear Cart prototype uses `innerHTML` only with its own fixed menu data. If you add user-entered text (e.g., notes), render it with `textContent` instead — that is exactly the kind of change an AI tool may get wrong.

## Prototyping versus production development — and when engineering review is necessary

| Prototype | Production |
|---|---|
| Answers a learning question | Serves real users reliably |
| Fictional or test data | Real, regulated data |
| One happy path + key errors | All edge cases, scale, monitoring |
| Can be thrown away | Must be maintained |
| PM can own | Engineering owns; PM partners |

```chart
type: steps
title: The readiness ladder — what each rung requires
steps:
  - ["Clickable mock", "Fictional data; PM-owned; label 'prototype'"]
  - ["Working prototype", "Local storage, simulated services; test users"]
  - ["Internal tool", "Real but non-sensitive data; approved tools; access control"]
  - ["Pilot with customers", "Engineering review, security, privacy, monitoring"]
  - ["Production", "Owned by engineering: tests, SLOs, on-call, compliance"]
caption: Every step up adds obligations. Vibe coding is fastest on the first two rungs; from rung 3 upward engineering and security must be involved.
```

**Engineering review is necessary before:** any real user data or personal information; authentication or payments; integration with company systems; anything customers rely on; anything public under the company's name; anything that runs automated actions (emails, money movement); any code that will be reused in production.

## Building and validating MVPs with vibe coding

Use the speed to **test assumptions**, not to skip discovery: (1) pick the riskiest assumption; (2) build the smallest prototype that tests it; (3) put it in front of 5–8 target users with a task; (4) measure behaviour (task success, time, errors) and listen; (5) decide: iterate, pivot, or stop. *A polished demo is not evidence of demand.*

!!! source "From your course notes (Lectures 32, 43, 55)"
    Label the prototype's **real and simulated functions**; a polished screen does not prove that a service works. Show the problem, target user, evidence, solution, prototype, business model, success measures and the next validation step. **Distinguish a clickable demo from a working integration, and planned outcomes from measured results. Never publish invented testimonials as if they were real.**

## Hands-on project: from idea to deployed prototype

**Project:** *Fee-Clear Cart* — test whether showing the full estimated total in the cart reduces checkout surprise. The finished starter code is in `templates/vibe-coding-starter/` (open `index.html`; it runs offline). It was tested in a browser at 375 px width: adding items, changing the area, simulated fee failure (“Estimate unavailable”, Pay disabled, Retry), and the simulated order message all behave as specified, with no console errors.

```chart
type: steps
title: Project milestones
steps:
  - ["1 · Brief", "Hypothesis, users, flows, success metric"]
  - ["2 · Prompt", "Use the build-prompt template"]
  - ["3 · Review", "Read the code; check states and accessibility"]
  - ["4 · Test", "Run the checklist; fix one issue per prompt"]
  - ["5 · Version", "Git commits on a branch; PR to main"]
  - ["6 · Deploy", "GitHub Pages test URL with 'Prototype' banner"]
  - ["7 · Validate", "5 user sessions; measure task success"]
  - ["8 · Decide", "Write a 1-page readout: keep, change, stop"]
caption: Each milestone has a concrete artefact. Total time for a first-timer: roughly one weekend.
per_row: 4
```

```chart
type: phone
title: Fee-Clear Cart — the starter app's two key states
screens:
  - name: "Cart with estimate"
    items: [["bar", "Your cart"], ["row", "Veg biryani × 1|₹260"], ["row", "Raita × 1|₹60"], ["row", "Delivery fee|₹25 (est.)"], ["row", "Platform fee|₹5"], ["row", "Taxes (est.)|₹16"], ["row", "Estimated total|₹366"], ["btn", "Pay ₹366"]]
    notes: ["Total shown before paying.", "'est.' labels where numbers can change.", "Button repeats the total."]
  - name: "Fee service fails"
    items: [["bar", "Your cart"], ["row", "Delivery fee|Estimate unavailable"], ["row", "Estimated total|—"], ["warn", "We couldn't load the fee. Retry"], ["btn", "Pay (disabled)"]]
    notes: ["No invented number.", "Pay is disabled until a fee loads.", "Retry is a real, focusable button."]
caption: Values match the tested build (subtotal ₹320, near area, 5% illustrative tax). This is the teaching prototype in templates/vibe-coding-starter, not a real product.
```

```chart
type: layers
title: How the starter app is put together
rows:
  - ["index.html (structure, labels)", "style.css (layout, focus, 44 px targets)"]
  - ["app.js (state, rendering, events)"]
  - ["Simulated fee service (300 ms delay, can fail)", "localStorage (cart persists per browser)"]
edges:
  - ["index.html (structure, labels)", "app.js (state, rendering, events)"]
  - ["style.css (layout, focus, 44 px targets)", "app.js (state, rendering, events)"]
  - ["app.js (state, rendering, events)", "Simulated fee service (300 ms delay, can fail)"]
  - ["app.js (state, rendering, events)", "localStorage (cart persists per browser)"]
caption: Three files, no server, no keys. Replacing the simulated service with a real API is the step that requires a server-side function and engineering review.
```

**Step 1 — Brief (example).** Hypothesis: first-time buyers who see the full estimated total in the cart will complete checkout more confidently. Users: busy office workers ordering dinner on mobile. Flows: add items; see estimated total; handle fee-service failure. Metric for the user test: % of participants who correctly state the total *before* tapping Pay (target ≥ 5 of 6).

**Step 2 — Prompt.** Use the template above. Ask for plain HTML/CSS/JS and a simulated fee service with a failure mode.

**Step 3 — Review.** Read `app.js`: find where the fee is fetched; confirm that on failure it shows “Estimate unavailable” and disables Pay (it does — `feeState.status = "error"`). Check labels, focus styles and button height in `style.css`.

**Step 4 — Test.** Run the checklist in the starter's README (add/remove, area change, failure + retry, keyboard-only, reload persistence, 375 px width).

**Step 5 — Version.** Commit after each working step; push to a branch; open a PR describing what changed and how you tested it.

**Step 6 — Deploy.** Public GitHub repo (dummy data only) → Settings → Pages → Deploy from branch `main` / root → share the URL **with the Prototype banner visible.** Do not add analytics that collect personal data; if you need behaviour data, observe sessions or log anonymous counts with consent.

**Step 7 — Validate.** Five or six moderated sessions: “You want this biryani and raita delivered 5 km away. How much will you pay in total? Now place the order.” Record task success, hesitations and quotes.

**Step 8 — Decide.** Readout: what you tested, results (e.g., “5 of 6 stated the correct total before paying; 1 missed the ‘est.’ label”), what you'll change, what remains unproven (real fee accuracy, real conversion), and the next test (A/B in the real product — Module 7).

### Portfolio presentation

Include: the problem and hypothesis; a 60-second screen recording; the live prototype link; what is simulated; test method and **real** results (or “not measured”); what you learned; how a production version would differ (security, data, scale); and your role (be specific about what the AI generated vs what you decided and tested).

## Exercises with model answers

!!! question "Exercise 1 · Spot the problems"
    An AI-generated app stores an API key in `app.js`, renders user comments with `innerHTML`, and saves data only to `localStorage`. You plan to share it with 50 customers. What must change?

??? answer "Model answer"
    (1) Move the API call server-side (serverless function) and rotate the exposed key. (2) Render comments with `textContent` or sanitise to prevent XSS. (3) `localStorage` means each customer sees only their own browser's data — if shared data is intended, add a backend with access rules. (4) Add a prototype banner, privacy notice, and get engineering/security review because real customers are involved.

!!! question "Exercise 2 · Write the debugging prompt"
    The page shows the cart but the total never appears. Console: `TypeError: Cannot read properties of undefined (reading 'price')`. Write your prompt to the AI.

??? answer "Model answer"
    “When I add 'Paneer wrap' the total never appears. Console error: `TypeError: Cannot read properties of undefined (reading 'price')` at `subtotal()` in app.js. Before changing code, explain the likely cause. I suspect the cart contains an id not present in MENU. Propose the smallest fix and a test I can run to confirm. Don't change any other behaviour.”

!!! question "Exercise 3 · Prototype or production?"
    Your vibe-coded internal dashboard reads the company's live orders database. Who needs to be involved and why?

??? answer "Model answer"
    Engineering (data access method, read-only replica, performance), security/IT (credentials, access control, approved tools), data/privacy (PII exposure, retention), and the data owner (permission). Even read-only access to production data is a production concern; use an approved read-only replica or an extract with minimised fields.

## Interview perspective

??? question "“How do you use AI coding tools as a PM?” — 60-second answer"
    “I use them to make ideas testable quickly — clickable prototypes with fictional data that I put in front of users within days. I write a short brief with the hypothesis, flows, states and accessibility needs, build in small steps, test each one, and keep everything in Git. I label what's simulated, never use real customer data, and I hand off to engineering for anything with real data, auth, payments or customers relying on it. The value is faster learning, not shipping AI-written code to production unreviewed.”

??? question "“Walk me through a prototype you built.” — structure"
    Problem and hypothesis → users → what you built (stack, scope, what's simulated) → how you tested it (sessions, metrics) → results (real numbers or “not measured”) → what you'd do next → what engineering would need to productionise it. Be explicit about your contribution versus the AI's.

## Key takeaways

* Vibe coding accelerates **learning**; it doesn't remove the need for **engineering judgment**.
* Work in **small, tested, committed steps**; describe symptoms precisely when debugging.
* Know **HTML/CSS/JS, Git, APIs and storage** well enough to review what the AI produced.
* **Never put secrets in frontends**, never use real customer data in unreviewed prototypes, and label simulations.
* Bring in **engineering review** before real data, auth, payments, integrations or public company use.

## Check your understanding

```quiz
- q: "Where should a secret API key live in a web prototype?"
  options:
    - "In app.js so it's easy to find"
    - "In a server-side function or secret manager"
    - "In the README"
    - "In localStorage"
  answer: 1
  why: "Anything in frontend code is visible to users; secrets must be server-side."
- q: "A form appears to save data, but after reload it's gone. Most likely…"
  options:
    - "The AI tool is broken"
    - "The UI isn't connected to persistent storage"
    - "The browser is too old"
    - "It's an accessibility issue"
  answer: 1
  why: "A screen with a form isn't necessarily wired to storage; verify the data flow."
- q: "Which practice makes AI-assisted coding mistakes cheapest to undo?"
  options:
    - "One huge prompt for the whole app"
    - "Small steps with a commit after each working step"
    - "Never testing"
    - "Editing production directly"
  answer: 1
  why: "Small committed increments let you revert precisely."
- q: "When is engineering review required?"
  options:
    - "Never for prototypes"
    - "Before real user data, auth, payments, integrations or public company use"
    - "Only for mobile apps"
    - "Only if the AI says so"
  answer: 1
  why: "These introduce security, privacy, reliability and legal obligations."
- q: "Rendering user-entered text with innerHTML risks…"
  options:
    - "Slow performance only"
    - "Cross-site scripting (XSS)"
    - "Nothing"
    - "Rate limiting"
  answer: 1
  why: "innerHTML can execute injected markup; use textContent or sanitisation."
```

## Recommended resources

* [MDN: Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development) — HTML, CSS, JavaScript basics.
* [GitHub Docs: Hello World](https://docs.github.com/en/get-started/using-github/hello-world) and [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart).
* [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/overview) · [Cursor docs](https://docs.cursor.com/) · [GitHub Copilot docs](https://docs.github.com/en/copilot).
* [Lovable docs](https://docs.lovable.dev/introduction/welcome) and [Replit Agent docs](https://docs.replit.com/features/agent/overview) (from your course notes).
* [OWASP Top 10](https://owasp.org/www-project-top-ten/) — common web security risks.

---
id: m17
n: 17
title: Replit and Other AI App Builders
subtitle: Build and host full-stack apps in the browser with Replit Agent, and know when to choose Bolt, v0, Cursor, GitHub Copilot or Figma Make instead.
summary: Replit's workspace, Agent and Assistant, checkpoints, secrets, built-in database, deployments and scheduled jobs, pricing, three labs, and a side-by-side guide to Bolt, v0, Cursor, Windsurf, GitHub Copilot, Firebase Studio, Figma Make and Claude artifacts.
hours: 5
status: drafted
sources: "Replit docs (docs.replit.com) and pricing; vendor docs for Bolt, v0, Cursor, GitHub Copilot; independent 2026 pricing reviews; checked 23 Oct 2026"
---

!!! warning "Fast-moving tools"
    App builders change pricing and features monthly. Treat the comparisons as a starting point and check each vendor's pricing page. Screens are **illustrative wireframes**.

## Replit in one picture

**Replit** is a complete coding environment in your browser: editor, terminal, database, hosting and an AI **Agent** that can build a full-stack app (front end, back end and database) from a description. Nothing to install, and it works on a phone too.

```chart
type: window
title: The Replit workspace
app: "Replit"
url: "replit.com/@you/feedback-hub"
sidebar: ["[1] Agent", "Files", "Database", "Secrets", "Deployments", "Git"]
main:
  - ["user", "Build a customer feedback hub: a public form, an admin table with filters, and a weekly theme summary."]
  - ["ai", "[2] Plan: Node + React app, PostgreSQL table 'feedback', admin page with password… Shall I start?"]
  - ["ok", "Checkpoint 3 saved · app running"]
  - ["input", "Message Agent…"]
panel:
  - ["tabs", "*Preview|Console|Shell"]
  - ["img", "[3] Running app"]
  - ["btn", "[4] Deploy"]
notes:
  - "Agent builds whole features; the Assistant makes quick edits and answers questions about the code."
  - "Agent proposes a plan first. Read it and remove what you don't need before it starts."
  - "Every Agent step saves a checkpoint you can roll back to, including the database."
  - "Deploy publishes the app on a replit.app address or your own domain."
caption: Secrets hold API keys; the Database tab shows a PostgreSQL database you can query.
```

### What it costs (checked 23 Oct 2026)

| Plan | Price | Notes |
|---|---|---|
| **Starter** | Free | Daily Agent credits, one published app, limited Agent capability |
| **Core** | about $20 a month billed yearly (about $25 monthly) | Monthly usage credits, more apps, collaborators, custom domains |
| **Pro / Teams** | about $100 a month | For teams with heavier use |

Replit uses **effort-based pricing**: a bigger Agent task costs more than a small one, and usage beyond your plan's credits is billed. Set a **usage alert** in billing settings. Check [replit.com/pricing](https://replit.com/pricing).

## Level 1 · Build your first app

!!! level1 "Level 1 · Beginner"
    1. Sign up at replit.com, click **Create**, and describe the app to Agent (use the five-part prompt from Class 16: what and who, pages, look, data, not now).
    2. Review Agent's plan, remove extras, and approve.
    3. Test in the preview. Ask for one change per message.
    4. If a change goes wrong, **roll back** to the previous checkpoint.

## Level 2 · Data, secrets and quality

!!! level2 "Level 2 · Working PM"
    * **Database**: ask "Store feedback in the database with date, customer segment, text and theme." Use the Database tab to view rows and run SQL such as `SELECT theme, COUNT(*) FROM feedback GROUP BY theme;`.
    * **Secrets**: add `ANTHROPIC_API_KEY` under Secrets. Ask Agent to read it from the environment in server code only.
    * **Ask for tests**: "Add tests for the form validation and run them."
    * **Admin protection**: "Protect the admin page with login; never show admin data on public pages."
    * **Explain the code**: ask Assistant "Which file handles the form? Explain in plain language."

## Level 3 · Deploy, schedule and integrate

```chart
type: workflow
title: Weekly AI theme digest on Replit
nodes:
  - ["trigger", "Scheduled deployment", "Every Monday 09:00"]
  - ["data", "Read last week's feedback", "SQL query on the database"]
  - ["ai", "Claude summarises themes", "API key from Secrets"]
  - ["output", "Post to Slack", "Incoming webhook URL in Secrets"]
per_row: 4
caption: Replit's scheduled deployments run a script on a timetable. The same digest can also be built in n8n (Class 20).
```

!!! level3 "Level 3 · Advanced"
    * **Deployments**: choose the type the app needs: static site, autoscale web app (scales with traffic), reserved machine (always on) or scheduled job.
    * **Custom domain**: Deployments → Settings → link your domain and add the DNS records shown.
    * **GitHub**: connect Git to push the code to a GitHub repository, then work on it with Claude Code (Class 15).
    * **Integrations**: Slack incoming webhooks, Stripe in test mode, the Claude API through Secrets.

## Labs

!!! example "Lab 1 · Feedback hub (Free, 30 minutes)"
    Build the feedback form and admin table from the picture above with sample data. Roll back once on purpose, to learn checkpoints.

!!! example "Lab 2 · Database and SQL (20 minutes)"
    Store submissions in the database. Run a `GROUP BY theme` query in the Database tab and ask Agent to show the counts on the admin page as a bar chart.

!!! example "Lab 3 · Weekly digest to Slack (Core or API, 40 minutes)"
    Create a Slack incoming webhook in your practice workspace. Add it and your Claude key as Secrets. Ask Agent for the scheduled job in the workflow above. Run it manually once and check the Slack message.

## The other AI app builders

```chart
type: compare
title: Choosing an AI app builder (checked 23 Oct 2026)
headers: ["Tool", "Best for", "Backend and data", "Free to start", "Get the code out"]
rows:
  - ["Lovable", "Polished MVPs with login and database", "Lovable Cloud or Supabase", "Yes, 5 credits a day", "GitHub sync"]
  - ["Replit", "Full-stack apps, scripts, scheduled jobs, hosting", "Built-in PostgreSQL", "Yes, daily credits", "Git / GitHub"]
  - ["Bolt.new", "Fast in-browser apps, many frameworks", "Supabase and others", "Yes, token-limited", "Download or GitHub"]
  - ["v0 (Vercel)", "Beautiful UI and Next.js apps", "Vercel integrations", "Yes, limited credits", "Deploy to Vercel or copy code"]
  - ["Figma Make", "Turning designs into working prototypes", "Light; prototype focus", "Starter plan limits", "Copy code"]
  - ["Claude artifacts", "One-page tools and clickable concepts", "None (front end only)", "Yes", "Copy or download"]
  - ["Cursor / Windsurf", "AI code editors for real codebases", "Whatever your code uses", "Free tiers", "Your own repository"]
  - ["GitHub Copilot", "Coding help and agents inside GitHub and editors", "Whatever your code uses", "Free tier", "Your own repository"]
  - ["Firebase Studio", "Google stack apps with Firebase backend", "Firebase", "Yes", "Your own repository"]
  - ["Claude Code", "Building and changing real repositories", "Whatever your code uses", "With Pro or API", "Your own repository"]
caption: For a PM, the usual path is Claude artifacts or Lovable for the first concept, then Claude Code on the GitHub repository once the project gets serious.
```

```chart
type: tree
title: Which builder should I open?
root:
  label: "What are you making?"
  children:
    - label: "A clickable concept for tomorrow"
      children:
        - label: "Claude artifact or Figma Make"
    - label: "An MVP with login and data"
      children:
        - label: "Lovable (or Bolt)"
    - label: "Backend jobs, scripts, hosting in one place"
      children:
        - label: "Replit"
    - label: "Changes to an existing codebase"
      children:
        - label: "Claude Code, Cursor or Copilot"
caption: You can switch later. Builders that sync to GitHub keep your options open.
```

## Common mistakes

* **No usage alerts**: effort-based pricing can surprise you. Set alerts on day one.
* **Secrets in code**: use the Secrets tab or environment variables.
* **Public admin pages**: protect anything with customer data behind login.
* **Tool-hopping**: pick one builder per project and finish the MVP first.

## Exercises with model answers

!!! question "Exercise · Pick the builder"
    (a) A pricing-page concept for a design review in two hours. (b) A nightly script that emails a sales summary. (c) Add a "save for later" feature to your company's existing web app.

??? answer "Model answer"
    (a) **Claude artifact** or **Figma Make**: fast, no backend needed. (b) **Replit** scheduled deployment or an **n8n** workflow (Class 20). (c) **Claude Code**, Cursor or Copilot on the existing repository, with engineering review, because it changes production code.

## Key takeaways

* **Replit** gives you editor, AI Agent, database, secrets and hosting in one browser tab.
* **Checkpoints** make experiments safe; **usage alerts** keep costs safe.
* Choose a builder by **what you are making**; prefer tools that **export to GitHub**.

## Check your understanding

```quiz
- q: "In Replit, what lets you undo an Agent step, including database changes?"
  options:
    - "Secrets"
    - "Checkpoints and rollback"
    - "Deployments"
    - "The Shell"
  answer: 1
  why: "Agent saves checkpoints you can roll back to."
- q: "Which tool is designed to change an existing production codebase?"
  options:
    - "Claude artifacts"
    - "Figma Make"
    - "Claude Code or Cursor"
    - "A landing page builder"
  answer: 2
  why: "Coding agents and AI editors work inside your existing repository."
```

## Recommended resources

* [Replit docs](https://docs.replit.com) · [Replit pricing](https://replit.com/pricing)
* [Bolt.new](https://bolt.new) · [v0 by Vercel](https://v0.dev) · [Cursor docs](https://docs.cursor.com) · [GitHub Copilot docs](https://docs.github.com/en/copilot)
* Replit's official YouTube channel for Agent walkthroughs

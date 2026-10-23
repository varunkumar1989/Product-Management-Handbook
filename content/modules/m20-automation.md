---
id: m20
n: 20
title: "Automation with Zapier, Make and n8n"
subtitle: Connect Gmail, Slack, Google Sheets, forms and AI so routine work runs by itself, and learn to choose between Zapier, Make and n8n.
summary: Automation building blocks (triggers, actions, filters, branches, loops, webhooks, schedules, credentials), connecting Gmail and Slack step by step, Zapier from first Zap to agents, Make scenarios with routers and iterators, n8n from self-hosting to AI agents and MCP, costs, error handling, and six labs including AI email triage and a tool Claude can call.
hours: 10
status: drafted
sources: "Zapier, Make and n8n docs and pricing pages; Slack API docs; Google OAuth docs; checked 23 Oct 2026"
---

!!! warning "Use practice accounts"
    Automations act without asking. Build every lab with a **practice Gmail and a practice Slack workspace**, and never point a test at real customers. Screens are **illustrative wireframes**.

## The building blocks

Every automation tool uses the same ideas with different names.

```chart
type: compare
title: Same idea, three names
headers: ["Idea", "What it means", "Zapier", "Make", "n8n"]
rows:
  - ["Automation", "The whole flow", "Zap", "Scenario", "Workflow"]
  - ["Trigger", "What starts it", "Trigger", "Trigger module (first)", "Trigger node"]
  - ["Action", "A step that does something", "Action", "Module", "Node"]
  - ["Condition", "Only continue if…", "Filter", "Filter on a route", "IF / Filter node"]
  - ["Branch", "Different paths for different cases", "Paths (paid)", "Router", "Switch / IF node"]
  - ["Loop", "Repeat for each item", "Looping (paid)", "Iterator + Aggregator", "Loop Over Items"]
  - ["Webhook", "Start from another app's HTTP call", "Webhooks by Zapier (paid)", "Custom webhook", "Webhook node"]
  - ["Schedule", "Run at set times", "Schedule by Zapier", "Scheduling", "Schedule Trigger"]
  - ["AI step", "Ask a model to classify, summarise or decide", "AI by Zapier / Agents", "AI modules", "AI Agent and chat model nodes"]
  - ["Billing unit", "What you pay for", "Tasks (successful actions)", "Credits", "Executions (cloud); free self-hosted"]
caption: Learn the ideas once, and you can use any of the three tools.
```

```chart
type: workflow
title: The shape of most automations
nodes:
  - ["trigger", "Something happens", "New email, form, row, schedule, webhook"]
  - ["logic", "Check it", "Filter: only invoices, only VIPs"]
  - ["ai", "Understand it", "Classify, extract fields, summarise"]
  - ["action", "Do something", "Add row, create ticket, draft reply"]
  - ["output", "Tell someone", "Slack message, email, WhatsApp"]
per_row: 5
caption: Start with trigger → action. Add the check, the AI step and the notification once the basic flow works.
```

## Choosing the tool

```chart
type: compare
title: Zapier vs Make vs n8n (checked 23 Oct 2026)
headers: ["", "Zapier", "Make", "n8n"]
rows:
  - ["Ease for beginners", "Easiest", "Medium (visual canvas)", "Medium to hard"]
  - ["Free tier", "100 tasks a month, two-step Zaps", "1,000 credits a month, 2 active scenarios, 15-minute minimum interval", "Community Edition free to self-host (you pay the server)"]
  - ["First paid tier", "Professional", "Core", "Cloud Starter, about €20 to €24 a month"]
  - ["App integrations", "8,000+", "2,000+", "Hundreds of nodes plus any API via HTTP Request"]
  - ["Complex logic", "Paths, loops on paid plans", "Strong: routers, iterators, data stores", "Strongest: code, branches, sub-workflows"]
  - ["AI agents", "Zapier Agents, AI steps", "AI modules and agents", "AI Agent node with memory and tools; MCP"]
  - ["Data stays with you", "No (cloud)", "No (cloud)", "Yes, if self-hosted"]
  - ["Best for", "Quick wins for non-technical teams", "Visual, multi-branch flows on a budget", "Power users, AI agents, high volume, privacy"]
caption: A good path is Zapier for your first two automations, then n8n for anything with AI agents or high volume. Check each pricing page before paying.
```

## How to connect Gmail and Slack (step by step)

### Gmail

```chart
type: steps
title: Connecting Gmail
steps:
  - ["Zapier or Make", "Add a Gmail step → Sign in with Google → Allow. Done."]
  - ["n8n Cloud", "Gmail node → Credential → Sign in with Google → Allow."]
  - ["n8n self-hosted", "Needs your own Google OAuth app (next picture)."]
  - ["Test", "Send yourself an email and run the trigger once."]
caption: Use a practice Gmail first. Google may show an 'unverified app' warning for self-made OAuth apps; that's expected for personal testing.
```

```chart
type: steps
title: Google OAuth app for self-hosted n8n (one time, 15 minutes)
steps:
  - ["Google Cloud console", "console.cloud.google.com → create a project"]
  - ["Enable APIs", "Enable the Gmail API (and Sheets, Drive, Calendar if needed)"]
  - ["Consent screen", "OAuth consent screen → External → add yourself as a test user"]
  - ["Credentials", "Create OAuth client ID → Web application"]
  - ["Redirect URL", "Paste the redirect URL shown in n8n's Gmail credential screen"]
  - ["Paste into n8n", "Copy the client ID and secret into the n8n credential → Sign in"]
per_row: 3
caption: The exact menu names in Google Cloud change occasionally. n8n's docs page for Google credentials has the current steps.
```

### Slack

```chart
type: steps
title: Connecting Slack
steps:
  - ["Simplest", "Zapier / Make: add a Slack step → sign in → choose the workspace → Allow"]
  - ["Incoming webhook", "Post-only: create a Slack app, turn on Incoming Webhooks, copy the URL"]
  - ["Bot token", "api.slack.com/apps → Create app → add scopes such as chat:write, channels:history"]
  - ["Install", "Install to workspace → copy the Bot User OAuth token (starts xoxb-)"]
  - ["Invite the bot", "In the channel type /invite @your-bot"]
  - ["Use in n8n", "Slack credential → paste token; Slack node → send message"]
per_row: 3
caption: Give the bot only the scopes it needs. A bot that only posts needs chat:write, not access to every message.
```

## Zapier · Basic to advanced

```chart
type: window
title: A two-step Zap: Gmail to Slack
app: "Zapier"
url: "zapier.com/editor"
main:
  - ["bar", "[1] 1. Trigger · Gmail · New email matching search"]
  - ["input", "Search string: from:boss@example.com is:important"]
  - ["bar", "[2] 2. Action · Slack · Send channel message"]
  - ["input", "Channel: #practice-alerts"]
  - ["input", "Message: Important email from {{From}}: {{Subject}}"]
  - ["btn", "[3] Test step"]
  - ["ok", "[4] Publish Zap"]
notes:
  - "Choose the app and the event that starts the Zap, sign in, and set options."
  - "Map fields from the trigger into the action. The {{…}} pills are data from step 1."
  - "Test each step with real sample data before publishing."
  - "Publish turns it on. Check Zap history for runs and errors."
caption: Free plans allow two-step Zaps like this one. Multi-step Zaps, filters on paths and webhooks need a paid plan.
```

!!! level1 "Zapier Level 1"
    Build the Gmail → Slack Zap above. Then a second: **Google Forms → Google Sheets** (new response → add row).

!!! level2 "Zapier Level 2 (paid)"
    * Add a **Filter** (only continue if Subject contains "invoice").
    * Use **Formatter** to clean text, dates and numbers.
    * Add **Paths** for different cases (VIP vs normal).
    * Add an **AI step** (AI by Zapier) to summarise or classify before posting.

!!! level3 "Zapier Level 3"
    * **Webhooks by Zapier** to receive data from your Lovable or Replit app.
    * **Zapier Agents** for multi-step tasks described in plain language.
    * **Zapier MCP** gives Claude access to Zapier's app actions as tools.
    * **Tables and Interfaces** for small internal tools without a separate database.

## Make · Basic to advanced

```chart
type: window
title: A Make scenario with a router
app: "Make"
url: "make.com/scenarios/lead-router"
main:
  - ["text", "[1] Canvas: modules are circles joined by lines; data flows left to right."]
  - ["row", "Google Forms · Watch responses|Trigger"]
  - ["row", "Router|splits into 2 routes"]
  - ["row", "Route A (filter: budget > ₹50,000) → Slack #sales-vip|"]
  - ["row", "Route B (all others) → Google Sheets add row|"]
  - ["btn", "[2] Run once"]
  - ["toggle", "[3] Scheduling: every 15 minutes|on"]
panel:
  - ["bar", "Module settings"]
  - ["input", "Map: {{1.email}}, {{1.budget}}"]
  - ["bar", "Operations used: 3 credits"]
notes:
  - "Each module is one app action. Click between modules to add a filter."
  - "Run once with a test response and inspect the bubbles showing data in and out of each module."
  - "Turn on scheduling. On the free plan the shortest interval is 15 minutes."
caption: Iterators split a list into items; aggregators combine items back into one bundle. Data stores keep small tables between runs.
```

!!! level2 "Make essentials"
    **Router** for branches, **filters** on each route, **iterator + aggregator** for lists (for example every attachment in an email), **error handlers** (resume, ignore, rollback) on risky modules, and **data stores** for memory between runs. Watch your **credit** use per run on the scenario's history page.

## n8n · Basic to advanced

### Getting n8n

| Option | How | Cost |
|---|---|---|
| **On your laptop** | Install Node.js, then run `npx n8n` and open http://localhost:5678 | Free |
| **Docker** | `docker run -it --rm -p 5678:5678 n8nio/n8n` | Free |
| **Small cloud server** | Docker on a small VPS or a free-tier VM (runs 24/7) | Server cost only |
| **n8n Cloud** | Sign up at n8n.io | Paid plans after a trial |

Claude.ai cannot reach `localhost`. For the MCP lab use n8n Cloud, a server, or a tunnel (for example Cloudflare Tunnel or ngrok's free tier).

```chart
type: window
title: The n8n editor
app: "n8n"
url: "localhost:5678/workflow/email-triage"
sidebar: ["Overview", "*Workflows", "Credentials", "Executions", "Templates"]
main:
  - ["row", "[1] Gmail Trigger · on new email|→"]
  - ["row", "AI Agent · Anthropic chat model|→"]
  - ["row", "Switch · category|→"]
  - ["row", "Slack · send message / Sheets · append row|"]
  - ["btn", "[2] Test workflow"]
  - ["toggle", "[3] Active|on"]
panel:
  - ["bar", "Node: Slack"]
  - ["input", "Channel: #practice-alerts"]
  - ["input", "[4] Text: {{ $json.output }}"]
notes:
  - "Nodes run left to right. Click + to add a node; pick apps, logic or AI nodes."
  - "Test workflow runs it once. Each node shows its input and output data, which is the best way to debug."
  - "Active turns on the triggers so it runs automatically."
  - "Expressions in {{ }} insert data from earlier nodes. $json is the current item's data."
caption: Executions shows every past run with its data, so you can see exactly where and why something failed.
```

### AI agents in n8n

```chart
type: layers
title: The n8n AI Agent node
rows:
  - ["Input: chat message, email text, or webhook data"]
  - ["AI Agent node: instructions (system prompt)"]
  - ["Chat model (Anthropic Claude, Gemini, OpenAI…)", "Memory (last N messages)", "Tools (Sheets, HTTP, Gmail, code)"]
  - ["Output: answer or action result"]
edges:
  - ["Input: chat message, email text, or webhook data", "AI Agent node: instructions (system prompt)"]
  - ["AI Agent node: instructions (system prompt)", "Chat model (Anthropic Claude, Gemini, OpenAI…)"]
  - ["AI Agent node: instructions (system prompt)", "Memory (last N messages)"]
  - ["AI Agent node: instructions (system prompt)", "Tools (Sheets, HTTP, Gmail, code)"]
  - ["AI Agent node: instructions (system prompt)", "Output: answer or action result"]
caption: Add an Anthropic credential with your Claude API key to use Claude as the chat model. Free alternatives for practice include Gemini's free tier and local models through Ollama.
```

### n8n and MCP

* **MCP Server Trigger** node: turns a workflow into an MCP server that exposes the **tool nodes attached to it** (for example a Custom n8n Workflow Tool that runs another workflow). Add its production URL to Claude (Settings → Connectors → Add custom connector) or to Claude Code (`claude mcp add --transport http …`). Claude can then call your workflow as a tool.
* **MCP Client Tool** node: lets an n8n AI agent use tools from other MCP servers.
* Protect MCP and webhook URLs with **authentication** (header token), so only you can trigger them.

## Labs

!!! example "Lab 1 · Gmail → Slack in Zapier (Free, 15 minutes)"
    Build the two-step Zap shown above with a practice Gmail and Slack. Send yourself a matching email and check Slack within a few minutes.

!!! example "Lab 2 · Form → Sheet → route in Make (Free, 30 minutes)"
    1. Create a Google Form with Name, Email and Budget.
    2. Make: Watch responses → Router → Route A filter Budget > 50000 → Slack; Route B → Sheets add row.
    3. Submit two test responses and check both routes.

```chart
type: workflow
title: Lab 3 · AI email triage in n8n
nodes:
  - ["trigger", "Gmail Trigger", "Every minute, label: inbox"]
  - ["ai", "AI Agent (Claude)", "Classify: urgent / invoice / newsletter / other; extract sender, amount, due date"]
  - ["logic", "Switch on category", "One branch per category"]
branch:
  paths:
    - ["urgent", [["output", "Slack alert", "#practice-alerts with summary"]]]
    - ["invoice", [["action", "Sheets: add row", "Sender, amount, due date"], ["action", "Gmail: add label", "Invoices"]]]
caption: Ask the AI step to reply in JSON with fixed fields, so the Switch node can read the category reliably.
```

!!! example "Lab 3 · AI email triage (n8n, 45 minutes)"
    1. Gmail Trigger (practice account) → AI Agent with the Anthropic chat model.
    2. Instructions: "Classify the email as urgent, invoice, newsletter or other. Reply only with JSON: {category, sender, amount, due_date, summary}." Turn on structured output or add a Structured Output Parser.
    3. Switch on `{{ $json.output.category }}` → Slack for urgent; Sheets + Gmail label for invoices.
    4. Send four test emails, one per category. Check each lands correctly in Executions.

!!! example "Lab 4 · Morning digest (n8n, 30 minutes)"
    Schedule Trigger 08:30 → Google Calendar (today's events) + Gmail (unread from the last 12 hours) → AI Agent "Write a 120-word brief with what to prepare" → Slack DM to yourself.

```chart
type: workflow
title: Lab 5 · A tool Claude can call
nodes:
  - ["trigger", "MCP Server Trigger", "Gives Claude a URL that lists and runs the tools attached below"]
  - ["action", "Tool: Custom n8n Workflow Tool", "Name log_bug; inputs title, severity"]
  - ["trigger", "Sub-workflow starts", "Execute Workflow Trigger receives title, severity"]
  - ["action", "Google Sheets: append row", "Bugs sheet"]
  - ["output", "Slack: notify #practice-bugs", "Title and severity"]
per_row: 5
caption: The MCP Server Trigger doesn't pass data to a next node like other triggers; it exposes the tool nodes connected to it. The workflow tool calls a small sub-workflow that does the work. Add the trigger's production URL to Claude as a custom connector.
```

!!! example "Lab 5 · Give Claude a tool (n8n Cloud or server, 30 minutes)"
    1. Build a small sub-workflow: **Execute Workflow Trigger** (inputs `title`, `severity`) → Google Sheets append row → Slack message.
    2. In a second workflow add an **MCP Server Trigger** and attach a **Custom n8n Workflow Tool** that calls the sub-workflow. Name it `log_bug` and describe it and its two inputs clearly, because Claude reads that description.
    3. Turn on authentication in the trigger, activate the workflow and copy the production URL.
    4. Claude → Settings → Connectors → Add custom connector → paste the URL (add the token if asked).
    5. In a chat: "Log a bug: checkout button overlaps on small screens, severity high." Approve the tool call and check the sheet and Slack.

!!! example "Lab 6 · Leads from your Lovable app (45 minutes)"
    Webhook node (copy its URL) → in your Lovable app (Class 16), ask Lovable to POST each new signup to that URL from a server function → n8n adds the lead to Sheets, asks Claude to score it, and alerts Slack for high scores. Class 21 adds a WhatsApp welcome message.

## Reliability and safety

* **Test with sample data**, then turn on. Keep the first week on "notify me" rather than "act".
* **Error alerts**: in n8n set an **error workflow** that posts failures to Slack; in Make add error handlers; in Zapier turn on error notifications.
* **No duplicates**: store an ID (email ID, form response ID) and skip items you've already processed.
* **Rate limits and costs**: add waits for big batches; set API spend limits; watch task, credit and execution counts.
* **Privacy**: only send the fields the AI step needs. Don't put customer personal data into tools your company hasn't approved.
* **Document** each automation: what it does, owner, accounts used, how to switch it off.

## Exercises with model answers

!!! question "Exercise 1 · Design the flow"
    Every support email mentioning "refund" should create a row in a Refunds sheet and alert #support-leads if the amount is over ₹5,000. Sketch the nodes.

??? answer "Model answer"
    Gmail Trigger (search "refund") → AI step extracts order ID and amount as JSON → Sheets append row → IF amount > 5000 → Slack alert to #support-leads. Add duplicate protection on the email ID and an error workflow.

!!! question "Exercise 2 · Pick the tool"
    A non-technical ops team wants three simple automations this week. A growth team wants an AI agent processing 50,000 events a month and keeping data on company servers. Which tools?

??? answer "Model answer"
    Ops team: **Zapier** (fastest to learn; free or Professional depending on steps). Growth team: **self-hosted n8n** (no per-task fees at high volume, AI Agent node, data stays on company infrastructure), with an engineer to run the server.

## Key takeaways

* Every automation is **trigger → (check) → (AI) → action → notify**.
* **Zapier** for quick wins, **Make** for visual branching on a budget, **n8n** for AI agents, volume and privacy.
* Connect Gmail and Slack with **sign-in connectors** in Zapier and Make; n8n self-hosted needs a **Google OAuth app** and a **Slack bot token**.
* **MCP Server Trigger** turns an n8n workflow into a tool Claude can call.

## Check your understanding

```quiz
- q: "What do you need to connect Gmail to self-hosted n8n?"
  options:
    - "Only your Gmail password"
    - "A Google OAuth client ID and secret from a Google Cloud project"
    - "A Slack bot token"
    - "Nothing"
  answer: 1
  why: "Self-hosted n8n needs your own OAuth app; n8n Cloud, Zapier and Make provide one."
- q: "Which Slack scope does a bot need just to post messages?"
  options:
    - "admin"
    - "chat:write"
    - "users:read.email"
    - "files:write"
  answer: 1
  why: "chat:write is enough to post; give bots the least access they need."
- q: "How can Claude call one of your n8n workflows?"
  options:
    - "Email it the workflow file"
    - "Use an MCP Server Trigger and add its URL as a custom connector"
    - "Share your n8n password"
    - "It can't"
  answer: 1
  why: "The MCP Server Trigger exposes the workflow as a tool over MCP."
- q: "Why ask the AI step to answer in JSON?"
  options:
    - "It's shorter"
    - "Later nodes can reliably read fixed fields such as category"
    - "Slack requires JSON"
    - "It's cheaper"
  answer: 1
  why: "Structured output makes branching and mapping predictable."
```

## Recommended resources

* [Zapier help](https://help.zapier.com) · [Make help](https://www.make.com/en/help) · [n8n docs](https://docs.n8n.io) · [n8n workflow templates](https://n8n.io/workflows/)
* [n8n Google credentials guide](https://docs.n8n.io/integrations/builtin/credentials/google/) · [Slack: creating an app](https://api.slack.com/start/quickstart)
* Official YouTube channels of n8n, Make and Zapier for feature walkthroughs; see Class 23 for creator channels

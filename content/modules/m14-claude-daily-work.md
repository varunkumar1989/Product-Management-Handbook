---
id: m14
n: 14
title: "Claude for Daily PM Work: Basic to Advanced"
subtitle: Use Claude every day for writing, research, analysis and prototypes, then connect it to Gmail, Calendar, Drive, Slack, GitHub and your own tools.
summary: Plans and apps, prompting that works, files and data analysis, Projects, artifacts and published prototypes, research, memory, styles and skills, connectors and custom MCP connectors, the API and Console, a daily PM routine, six labs, and where to keep learning.
hours: 8
status: drafted
sources: "Claude docs and Help Center (docs.claude.com, support.claude.com), Anthropic Academy, connectors getting-started guide; checked 23 Oct 2026"
---

!!! warning "Feature names move around"
    Claude ships new features often, and menus get renamed. If a button in a lab has moved, search the [Claude Help Center](https://support.claude.com) for the feature name. Screens below are **illustrative wireframes**, not screenshots.

## What Claude is and where you can use it

**Claude** is Anthropic's AI assistant. You talk to it in plain language, give it files, and it writes, analyses, researches, codes and builds small apps. The same account works in several places:

```chart
type: canvas
title: Where you can use Claude
cols: 3
cells:
  - title: "Web: claude.ai"
    text: ["Every feature", "Best for long work sessions", "Artifacts, Projects, connectors"]
    tone: b
  - title: "Desktop app (Mac, Windows)"
    text: ["Same as web, plus local extensions", "Keyboard shortcut to open quickly", "Works with files on your laptop"]
    tone: v
  - title: "Mobile app (iOS, Android)"
    text: ["Voice mode for hands-free thinking", "Photo of a whiteboard → summary", "Good for quick capture"]
    tone: g
  - title: "Claude Code"
    text: ["Terminal, IDE, desktop and web", "Works inside code repositories", "Class 15"]
    tone: w
  - title: "Inside other apps"
    text: ["Slack, browser extension and others where your plan offers them", "Check Settings → Connectors and the Help Center"]
    tone: r
  - title: "API (Claude Console)"
    text: ["Build Claude into your own app or bot", "Pay per use", "Used in Classes 20 to 22"]
    tone: b
caption: Start on the web or desktop app. Add the others when a task needs them.
```

### Plans

| Plan | Who it is for | What you get (checked 23 Oct 2026) |
|---|---|---|
| **Free** | Trying Claude | Chat, file upload, limited daily messages, some connectors |
| **Pro** | Individual PMs | More usage, Projects, more models, **Claude Code included** |
| **Max** | Heavy daily users | 5× or 20× Pro usage, priority access, early features |
| **Team / Enterprise** | Companies | Admin controls, shared Projects, single sign-on, data controls |

Chat and Claude Code draw from the **same usage pool** on Pro and Max, so a long coding session leaves less chat time that day. Check [claude.com/pricing](https://claude.com/pricing) for current limits.

## Level 1 · Your first hour with Claude

!!! level1 "Level 1 · Beginner"
    Goal: get one genuinely useful result (a meeting summary, an email, a first PRD draft) and learn the four habits that make answers better.

### The anatomy of a good prompt

Most weak answers come from missing context, not from a weak model. Use four parts:

```chart
type: steps
title: The four-part prompt
steps:
  - ["Context", "Who you are, the product, the audience"]
  - ["Task", "One clear verb: summarise, draft, compare, critique"]
  - ["Input", "Paste or attach the material: notes, CSV, PDF"]
  - ["Format", "Length, structure, tone, what to leave out"]
caption: Example — "I'm a PM at a food-delivery app (context). Turn these interview notes into the top five problems with a quote for each (task). Notes attached (input). Use a table, plain English, max 200 words (format)."
```

```chart
type: window
title: A first chat in Claude
app: "Claude"
url: "claude.ai/new"
sidebar: ["+ New chat", "*Chats", "Projects", "Artifacts", "Settings"]
main:
  - ["bar", "Interview synthesis"]
  - ["user", "[1] I'm a PM at a food-delivery app. Turn the attached notes into the top 5 problems, with one quote each. Table, max 200 words."]
  - ["img", "interview-notes.pdf (attached)"]
  - ["ai", "[2] Here are the five problems… (table with Problem, Evidence, Quote, How many users)"]
  - ["input", "[3] Reply… e.g. 'Now rank them by frequency and add a confidence column'"]
notes:
  - "Write the four parts: context, task, input, format. Attach files with the paperclip or drag and drop."
  - "Read the answer critically. Check quotes against the source, because AI can misquote."
  - "Improve by replying, not by starting again: ask for a change, a different format, or a shorter version."
caption: Use the pencil on your own message to edit and resend; use retry on Claude's answer to get a different version.
```

### Four habits for Level 1

1. **Give the source material.** Attach the PDF, CSV or notes instead of asking from memory.
2. **Ask for a format.** Tables, bullet lists, "max 150 words", "for a VP audience".
3. **Iterate in the same chat.** "Shorter", "more specific", "add a risks section".
4. **Start a new chat for a new topic.** Long mixed chats get slower and less focused.

### Files Claude can read

PDFs, Word documents, slides, spreadsheets and CSVs, images and screenshots, and plain text or code files. Claude can **run code to analyse data files**: upload a CSV and ask for averages, a chart or a cohort table.

!!! tip "Data analysis prompt"
    "Here is `orders.csv`. 1) Describe the columns. 2) Weekly order count and average order value. 3) A line chart of both. 4) Three observations a PM should act on. Show the method, so I can check it."

## Level 2 · Features working PMs use every week

!!! level2 "Level 2 · Working PM"
    Goal: stop re-explaining your product in every chat, produce documents and prototypes you can share, and research with sources.

### Projects: your product's memory

A **Project** is a workspace with **custom instructions** and **knowledge files** that every chat inside it can use. Make one Project per product or per big initiative.

```chart
type: window
title: Setting up a Project
app: "Claude"
url: "claude.ai/projects"
sidebar: ["+ New chat", "Chats", "*Projects", "Artifacts"]
main:
  - ["bar", "Project: FoodApp · Checkout"]
  - ["text", "Chats in this project"]
  - ["row", "Interview synthesis — week 42|Today"]
  - ["row", "PRD v2: split payments|Yesterday"]
  - ["input", "[3] Start a chat in this project…"]
panel:
  - ["bar", "[1] Instructions"]
  - ["text", "You are my PM co-pilot for FoodApp checkout. Users: urban 22–35. Always flag assumptions. Use British spelling."]
  - ["bar", "[2] Knowledge"]
  - ["row", "strategy-2026.pdf|PDF"]
  - ["row", "personas.md|Doc"]
  - ["row", "checkout-funnel.csv|CSV"]
notes:
  - "Instructions: who Claude is in this project, your users, rules (tone, spelling, 'always cite the source file')."
  - "Knowledge: upload the strategy, personas, PRDs, research and metrics. Keep files current; delete stale ones."
  - "Every chat started here sees the instructions and knowledge, so you never paste context again."
caption: On Team plans you can share a Project with colleagues so everyone uses the same context.
```

### Artifacts: documents, code and clickable prototypes

When Claude produces something substantial (a document, a diagram, a web page, a small app), it appears as an **artifact** in a panel beside the chat. You can edit it by asking for changes, see versions, copy or download it, and **publish** it to get a link you can share.

```chart
type: window
title: An artifact prototype beside the chat
app: "Claude"
sidebar: ["Chats", "Projects", "*Artifacts"]
main:
  - ["user", "Build a clickable mobile prototype of a split-bill screen: items list, 'split with' picker, total per person. Sample data only."]
  - ["ai", "[1] I've built the prototype. Tap a friend to add them; totals update."]
  - ["user", "[2] Make the total sticky at the bottom and add a 'Request on UPI' button."]
panel:
  - ["tabs", "*Preview|Code"]
  - ["img", "Live prototype: Split bill"]
  - ["row", "Paneer tikka|₹320"]
  - ["row", "You + Asha|₹160 each"]
  - ["btn", "[3] Publish"]
notes:
  - "Ask for 'sample data only' and 'mobile-first'. Claude writes HTML, CSS and JavaScript and shows a live preview."
  - "Change it in plain words. Each change creates a new version you can go back to."
  - "Publish gives a link for stakeholders. Check what is public before sharing, and never put real customer data in a prototype."
caption: Artifacts are ideal for clickable concepts and one-page tools. For a real product with login and a database, move to Lovable (Class 16) or Claude Code (Class 15).
```

### Research with sources

Turn on **web search** (and **Research**, where your plan offers it) for questions that need current information: competitors, regulations, market sizes. Research runs many searches and returns a report with citations.

!!! warning "Always open the sources"
    Click at least three citations and confirm the claim is really there. AI research can misread a source or rely on a weak one. Mark any number you could not verify as "unverified" in your document.

### Styles, memory and skills

* **Styles** set how Claude writes (concise, formal, explanatory, or a custom style learned from your own writing samples).
* **Memory and past-chat search** (where enabled) let Claude recall earlier work. You can view, edit or turn memory off in Settings.
* **Skills** are packaged instructions (and sometimes scripts) that teach Claude a repeatable task, such as your company's PRD format or a spreadsheet report. Claude loads a skill when the task matches. You can use Anthropic's skills and create your own.

## Level 3 · Connect Claude to your apps

!!! level3 "Level 3 · Advanced"
    Goal: let Claude read your email, calendar, documents and Slack, act with your approval, and use your own tools through MCP.

### Connectors

**Connectors** give Claude permission to use another app on your behalf. Go to **Settings → Connectors**, click **Connect** next to a service, sign in, and approve the permissions.

```chart
type: window
title: Connecting Gmail, Calendar, Drive and Slack
app: "Claude · Settings"
url: "claude.ai/settings/connectors"
sidebar: ["Profile", "Appearance", "*Connectors", "Capabilities", "Privacy", "Billing"]
main:
  - ["bar", "Connectors"]
  - ["row", "Gmail|[1] Connect"]
  - ["row", "Google Calendar|Connected ✓"]
  - ["row", "Google Drive|Connected ✓"]
  - ["row", "Slack|Connect"]
  - ["row", "GitHub|Connect"]
  - ["row", "Notion · Figma · others|Browse"]
  - ["btn", "[2] Add custom connector"]
notes:
  - "Click Connect, sign in to the other app and approve. On Team and Enterprise plans an admin may need to enable a connector first."
  - "Custom connector: paste the URL of a remote MCP server (for example your own n8n workflow, Class 20) to give Claude new tools."
caption: Gmail: Claude can search, read and draft emails, but it does not send them for you. Each action asks for your approval unless you change that setting.
```

```chart
type: steps
title: Turning a connector on for one chat
steps:
  - ["Open a chat", "New chat or inside a Project"]
  - ["Tools menu", "Click the tools / + icon under the message box"]
  - ["Enable", "Toggle Gmail, Calendar, Drive or Slack on"]
  - ["Ask", "'Summarise unread emails from my manager this week'"]
  - ["Approve", "Allow each action, or allow for this chat"]
caption: If Claude says it cannot reach a tool, the connector is usually disconnected. Reconnect it in Settings → Connectors.
```

### What PMs do with connectors

| Connector | Daily use | Example prompt |
|---|---|---|
| **Gmail** | Triage, find decisions, draft replies | "Find every email about the payments launch this month. List decisions and open questions, then draft a reply to the latest thread." |
| **Google Calendar** | Prep and planning | "What meetings do I have tomorrow? For each, what should I prepare, based on related Drive docs?" |
| **Google Drive** | Search and summarise docs | "Compare the Q3 and Q4 roadmap docs and list what moved." |
| **Slack** | Catch up and draft updates | "Summarise #checkout-squad since Monday: decisions, blockers, who is waiting on me." |
| **GitHub** | Read code and issues | "Read the open issues labelled 'checkout' and group them by theme." |
| **Notion / Figma** | Specs and designs | "Pull the requirements from the Split Bill PRD in Notion and check the Figma file covers each one." |

### Custom connectors and MCP

**MCP (Model Context Protocol)** is an open standard that lets an AI assistant use tools from another system. A **remote MCP server** has a URL. Add it under **Settings → Connectors → Add custom connector**, and Claude gets that server's tools. In Class 20 you will build an **n8n workflow with an MCP Server Trigger** and add it to Claude, so you can say "log this bug to our tracker" and n8n does it.

### The API and Claude Console

To put Claude **inside your own app, bot or automation**, you use the **Claude API**:

1. Sign in at [console.anthropic.com](https://console.anthropic.com) (separate billing from your claude.ai plan).
2. Add a payment method and **set a monthly spend limit**.
3. Create an **API key** and store it in a secret store (never in a chat or frontend code).
4. Test prompts in the **Workbench**, then use the key in n8n, Make, Zapier, Lovable or code.

## A daily routine for PMs

```chart
type: compare
title: A day with Claude
headers: ["Time", "Task", "Feature", "Prompt starter"]
rows:
  - ["09:00", "Inbox and calendar brief", "Gmail + Calendar connectors", "'Brief me: urgent emails, today's meetings, what to prep'"]
  - ["10:00", "Synthesise user interviews", "Project + file upload", "'Top themes with quotes and counts; flag contradictions'"]
  - ["11:30", "Draft or tighten a PRD section", "Project + PRD skill or template", "'Critique this scope against our strategy file'"]
  - ["13:00", "Analyse a metric drop", "File upload + analysis", "'Explain the conversion drop by segment; show the method'"]
  - ["15:00", "Prototype an idea for design review", "Artifact", "'Clickable mobile prototype, sample data, three states'"]
  - ["16:30", "Competitor or market question", "Research with citations", "'How do the top 3 rivals handle refunds? Cite sources'"]
  - ["17:30", "Weekly or daily update", "Slack connector", "'Draft my update from #squad and my notes, 120 words'"]
caption: Keep one Project per product, so every task in this list starts with the right context.
```

## Labs

!!! example "Lab 1 · Build your product Project (20 minutes)"
    1. Projects → **New project** → name it after your product.
    2. Write instructions: product in one line, users, goals this quarter, writing rules, "flag assumptions".
    3. Upload three files: a strategy or vision doc, personas, and one metrics CSV (use `datasets/orders.csv` from this handbook if you have nothing).
    4. Ask: "Using only the knowledge files, what are the three biggest risks to this quarter's goal?"
    5. Check the answer cites the files. If it invents facts, add to the instructions: "Answer only from the knowledge files; say 'not in files' otherwise."

!!! example "Lab 2 · Interview synthesis (30 minutes)"
    1. Inside your Project, attach five interview notes (real or written by you).
    2. Prompt: "Affinity-map these interviews: themes, number of users per theme, one quote each, and the job-to-be-done behind each theme."
    3. Follow up: "Which theme is most likely to change our roadmap? What would we need to believe?"
    4. Save the result as an artifact document and publish it for your team.

!!! example "Lab 3 · A clickable prototype you can share (30 minutes)"
    1. Prompt: "Build a mobile-first clickable prototype for [feature]: three screens, sample data only, a 'Prototype · not real' label."
    2. Ask for two changes, one at a time.
    3. Ask for an edge case: "Add the empty state and an error state."
    4. Click **Publish**, open the link in a private window, and check it works on your phone.

!!! example "Lab 4 · Morning brief from Gmail and Calendar (15 minutes)"
    1. Settings → Connectors → connect **Gmail** and **Google Calendar** (use a practice account first).
    2. In a new chat, turn both on in the tools menu.
    3. Prompt: "Brief me for today: meetings with what to prep, emails that need a reply from me, and anything with a deadline this week."
    4. Ask Claude to **draft** two replies. Open Gmail and check the drafts are there. Claude drafts; you review and send.

!!! example "Lab 5 · Weekly Slack update (15 minutes)"
    1. Connect **Slack** (practice workspace).
    2. Prompt: "Read #practice-squad from the last 7 days. Draft a weekly update: shipped, in progress, blocked, decisions needed. 120 words."
    3. Edit the draft yourself before posting. You own what you send.

!!! example "Lab 6 · Give Claude a custom tool (advanced, after Class 20)"
    1. Build the n8n "log a bug to Google Sheets" workflow with an **MCP Server Trigger** (Class 20, Lab 5).
    2. Copy its production URL.
    3. Claude → Settings → Connectors → **Add custom connector** → paste the URL.
    4. In a chat: "Log a bug: checkout button overlaps on small screens, high priority." Approve the tool call, then check the sheet.

## Prompt library for PMs

| Job | Prompt |
|---|---|
| PRD critique | "Act as a skeptical engineering lead. List the 10 questions you'd ask about this PRD, then rewrite the scope section to answer them." |
| Prioritisation | "Score these 12 ideas with RICE. Show your assumptions for reach and effort, and mark which ones are guesses." |
| Metrics | "Build a KPI tree for 'weekly active ordering users'. Include input metrics I can move this quarter." |
| Stakeholders | "Rewrite this update for (a) the CEO in 3 lines, (b) engineers with the technical detail." |
| Interview prep | "Ask me one PM interview question at a time on product sense. After my answer, score it and show a stronger answer." |
| Release notes | "Turn these merged pull request titles into customer-friendly release notes, grouped by benefit." |

## Common mistakes

* **No context**: asking "write a PRD" with no product, users or goal. Use a Project.
* **Trusting numbers and quotes without checking**: always verify against the source.
* **Pasting confidential data into a personal plan**: follow your company's AI policy; use Team or Enterprise for work data.
* **One endless chat**: start a new chat per task; keep long-lived context in the Project.
* **Letting Claude send on your behalf too early**: keep approvals on for email and Slack actions.

## Where to find official help and sources

* **Docs**: [docs.claude.com](https://docs.claude.com) (API, prompting, tools, MCP, Claude Code).
* **Help Center**: [support.claude.com](https://support.claude.com) (features, plans, connectors, troubleshooting).
* **Claude Academy** (free; formerly Anthropic Academy at anthropic.com/learn, which reportedly now redirects there): courses including *Claude 101*, *AI Fluency*, *Building with the Claude API*, *Introduction to MCP* and *Claude Code in Action* at [academy.claude.com](https://academy.claude.com).
* **Prompt engineering guide**: in the docs, under "Prompt engineering".
* **Cookbook**: [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) for API examples.
* **Anthropic on YouTube**: official talks and feature walkthroughs.

## Exercises with model answers

!!! question "Exercise 1 · Fix the prompt"
    "Write a PRD for a loyalty program." Rewrite it using the four-part prompt.

??? answer "Model answer"
    "I'm the PM for a grocery delivery app in Indian metros; 60% of orders come from repeat users (context). Draft a one-page PRD for a points-based loyalty program aimed at increasing 90-day retention (task). Use our PRD template and strategy file in this Project (input). Sections: problem, goals and metrics, users, scope in and out, risks, open questions; max 600 words; flag every assumption (format)."

!!! question "Exercise 2 · Which feature?"
    You need (a) a shareable clickable concept for tomorrow's design review, (b) Claude to remember your product's personas in every chat, (c) a summary of last week's Slack decisions. Which Claude feature solves each?

??? answer "Model answer"
    (a) An **artifact**, published as a link. (b) A **Project** with the personas in knowledge files and the instructions. (c) The **Slack connector**, enabled in that chat.

## Key takeaways

* Good results come from **context, a clear task, source material and a format**.
* **Projects** hold context; **artifacts** turn answers into shareable documents and prototypes.
* **Connectors** let Claude work with Gmail, Calendar, Drive, Slack, GitHub and more, with your approval.
* **Custom connectors (MCP)** and the **API** extend Claude to your own tools and apps.

## Check your understanding

```quiz
- q: "You keep pasting the same personas and strategy into every chat. What should you use?"
  options:
    - "A longer prompt"
    - "A Project with instructions and knowledge files"
    - "The API"
    - "A new account"
  answer: 1
  why: "Projects give every chat inside them the same instructions and files."
- q: "With the Gmail connector, what does Claude do with a reply you ask for?"
  options:
    - "Sends it immediately"
    - "Creates a draft for you to review and send"
    - "Posts it to Slack"
    - "Nothing; Gmail is read-only"
  answer: 1
  why: "Claude can search, read and draft in Gmail, but it does not send on your behalf."
- q: "How do you give Claude a tool from your own n8n workflow?"
  options:
    - "Paste the n8n password into a chat"
    - "Add the workflow's MCP server URL as a custom connector"
    - "Upload the workflow as a PDF"
    - "It is not possible"
  answer: 1
  why: "Remote MCP servers are added as custom connectors in Settings → Connectors."
- q: "Where should your Claude API key live when you use it in an automation?"
  options:
    - "In the chat"
    - "In the automation tool's credential store"
    - "In a public GitHub repository"
    - "In the artifact code"
  answer: 1
  why: "Keys belong in secret or credential stores, never in chats or shared code."
```

## Recommended resources

* [Claude Help Center](https://support.claude.com) · [Claude docs](https://docs.claude.com) · [Claude Academy](https://academy.claude.com)
* [Connectors: getting started](https://claude.com/docs/connectors/getting-started)
* [Claude Console](https://console.anthropic.com) for API keys and spend limits
* [Anthropic cookbook on GitHub](https://github.com/anthropics/anthropic-cookbook)

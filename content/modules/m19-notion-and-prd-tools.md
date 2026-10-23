---
id: m19
n: 19
title: Notion, PRD Tools and AI Documentation
subtitle: Build a product workspace in Notion, write and critique PRDs with AI, turn specs into tickets, and connect your docs to Claude.
summary: Notion pages, blocks and databases, views, relations and templates, a PM product hub, Notion AI and its pricing, the Notion MCP server and Claude connector, a comparison of PRD tools (ChatPRD, Notion AI, Confluence with Rovo, Coda, Linear, Jira Product Discovery, Productboard, Claude Projects), an AI-assisted PRD workflow, and six labs.
hours: 6
status: drafted
sources: "Notion Help Center and pricing; vendor pages for ChatPRD, Atlassian, Linear, Coda, Productboard; Module 6; handbook templates 01, 02 and 09; checked 23 Oct 2026"
---

!!! warning "Plans and AI features change"
    Notion's AI packaging changed several times in 2026. Check [notion.com/pricing](https://www.notion.com/pricing) before buying. Screens are **illustrative wireframes**.

## Notion in one page

**Notion** is a workspace for documents and databases. Everything is a **page** made of **blocks** (text, headings, checklists, tables, images, embeds). A **database** is a collection of pages with properties, shown in different **views**. PMs use Notion for PRDs, roadmaps, research repositories, meeting notes and decision logs.

### Plans (checked 23 Oct 2026)

| Plan | Price | AI |
|---|---|---|
| **Free** | $0 | A limited AI trial |
| **Plus** | per member, monthly | A limited AI trial |
| **Business** | about $20 per member a month | **Full Notion AI**: AI writing and Q&A, AI meeting notes, enterprise search, research mode, agents |
| **Enterprise** | custom | Business features plus admin and security controls |

Custom AI **agents** can use a separate credit meter on top of the plan. If your company already pays for Claude, you can do much of the AI work with the **Claude connector** instead (Lab 4).

## Level 1 · Pages, blocks and databases

```chart
type: window
title: A Notion roadmap database (board view)
app: "Notion"
url: "notion.so/product-hub/roadmap"
sidebar: ["Product hub", "*Roadmap", "PRDs", "Research", "Decisions", "Meeting notes"]
main:
  - ["tabs", "*Board|Table|Timeline|Calendar"]
  - ["row", "Now · Split payments (RICE 42)|Asha"]
  - ["row", "Now · Saved addresses (RICE 35)|Ravi"]
  - ["row", "Next · Loyalty points (RICE 28)|Meena"]
  - ["row", "Later · Group ordering (RICE 19)|—"]
  - ["btn", "[1] + New"]
panel:
  - ["bar", "[2] Properties"]
  - ["row", "Status|Now"]
  - ["row", "Quarter|Q4 2026"]
  - ["row", "Owner|Asha"]
  - ["row", "RICE score|42"]
  - ["row", "PRD|↗ Split payments PRD"]
notes:
  - "Each card is a page. Click + New and choose a template so every item starts with the same structure."
  - "Properties hold the data you filter and sort by. 'PRD' is a relation that links to the PRDs database."
caption: Same data, four views: board for stand-ups, table for scoring, timeline for planning, calendar for launches. The roadmap items are hypothetical.
```

!!! level1 "Level 1 · Beginner"
    * Type **/** to insert any block (heading, to-do, toggle, table, callout, database).
    * Drag the **⋮⋮** handle to move blocks; turn any block into another type.
    * Create a database with **/database**. Add properties: Status (select), Owner (person), Quarter (select), Score (number).
    * Add **views** with **+** next to the view tabs, each with its own filter and sort.
    * Share a page with **Share**; choose who can view, comment or edit.

## Level 2 · A product hub that runs itself

```chart
type: layers
title: A PM product hub in Notion
labels: ["Strategy", "Planning", "Evidence", "Execution"]
rows:
  - ["Vision and OKRs page"]
  - ["Roadmap database", "PRDs database"]
  - ["Research repository (interviews)", "Metrics snapshots"]
  - ["Decision log", "Meeting notes", "Launch checklist"]
edges:
  - ["Vision and OKRs page", "Roadmap database"]
  - ["Roadmap database", "PRDs database", "relation"]
  - ["Research repository (interviews)", "PRDs database", "evidence"]
  - ["PRDs database", "Decision log", "decisions"]
caption: Relations connect the databases, so a PRD shows the roadmap item it belongs to and the interviews that support it.
```

!!! level2 "Level 2 · Working PM"
    * **Templates**: create a PRD template inside the PRDs database (use `templates/01-prd-template.md` from this handbook). Every new PRD starts complete.
    * **Relations and rollups**: link PRDs to roadmap items and interviews; roll up "number of supporting interviews" onto each PRD.
    * **Linked views**: show "My open PRDs" or "This quarter's roadmap" on your personal home page.
    * **Buttons and automations**: a button that creates this week's meeting note; a database automation that notifies Slack when Status changes to "Launched".
    * **Integrations**: embed Figma frames, link GitHub pull requests, sync Jira or Linear issues.

## Level 3 · Notion AI and connecting to Claude

!!! level3 "Level 3 · Advanced"
    Goal: let AI fill properties, summarise research, draft and critique PRDs, and work with your Notion pages from Claude and Claude Code.

### Notion AI (Business plan)

* **Ask** questions across your workspace: "What did we decide about refunds?"
* **Write and edit** inside a page: draft, shorten, change tone, translate.
* **AI autofill** database properties, for example a "Theme" and "Sentiment" for every interview note.
* **AI meeting notes**: transcribe and summarise meetings into action items.
* **Research mode** and **agents** for multi-step tasks across pages.

### Claude with Notion

```chart
type: workflow
title: Two ways to connect Claude and Notion
nodes:
  - ["action", "Claude.ai connector", "Settings → Connectors → Notion → Connect"]
  - ["ai", "Ask in chat", "'Draft a PRD page in Product hub/PRDs from this brief'"]
  - ["output", "New Notion page", "Review and edit in Notion"]
  - ["action", "Claude Code MCP", "claude mcp add --transport http notion https://mcp.notion.com/mcp"]
  - ["ai", "Ask in the repository", "'Compare the code with the PRD in Notion'"]
  - ["output", "Gap list or code changes", "Linked back in the PRD"]
per_row: 3
caption: You choose which pages the connection can access when you sign in. Start with a practice teamspace.
```

## PRD tools compared

```chart
type: compare
title: Tools for writing and managing PRDs (checked 23 Oct 2026)
headers: ["Tool", "Strength", "AI help", "Best when"]
rows:
  - ["Notion + Notion AI", "Docs and databases in one place", "Draft, autofill, Q&A, meeting notes", "Your team already lives in Notion"]
  - ["Claude Projects + a PRD skill", "Strongest reasoning and critique", "Draft, critique, rewrite, tickets", "You want quality writing and review; export to any tool"]
  - ["ChatPRD", "Purpose-built AI PRD assistant", "PRD drafts, coaching, templates", "You want a guided PRD writer"]
  - ["Confluence + Atlassian Rovo", "Enterprise wiki linked to Jira", "Draft, summarise, search", "Your company runs on Jira"]
  - ["Coda", "Docs with formulas and tables", "AI columns and writing", "PRDs that need live calculations"]
  - ["Linear (docs and projects)", "Fast issue tracking with project docs", "Summaries and drafting", "Engineering uses Linear"]
  - ["Jira Product Discovery", "Ideas, insights and prioritisation", "Summaries via Rovo", "Discovery feeding a Jira delivery team"]
  - ["Productboard", "Feedback to roadmap", "Feedback insights", "High volume of customer feedback"]
  - ["Google Docs + Gemini / Word + Copilot", "Familiar documents", "Drafting inside the doc", "Company uses Google or Microsoft suites"]
caption: The tool matters less than the habit: one template, linked evidence, explicit decisions, and a review loop.
```

## An AI-assisted PRD workflow

```chart
type: workflow
title: From evidence to tickets with AI
nodes:
  - ["data", "Evidence", "Interviews, metrics, tickets"]
  - ["ai", "Problem statement", "Claude: 'Who, what pain, how often, why now'"]
  - ["ai", "PRD draft", "Template 01; flag assumptions"]
  - ["ai", "Critique", "Eng, design, legal, support personas"]
  - ["human", "Review meeting", "Decide open questions; log decisions"]
  - ["ai", "Stories and acceptance criteria", "Given / When / Then"]
  - ["output", "Tickets", "Linear or Jira via connector or MCP"]
  - ["human", "Launch and learn", "Metrics review; update PRD"]
per_row: 4
caption: AI drafts and critiques; the PM owns the decisions and the final words. For AI features add an evaluation plan (template 09).
```

!!! tip "The critique prompt that finds gaps"
    "Review this PRD as four people: a skeptical engineering lead, a designer, a lawyer and a support lead. For each, list the top three questions and risks. Then list missing edge cases and any requirement that isn't testable."

## Labs

!!! example "Lab 1 · Product hub in Notion (Free, 40 minutes)"
    1. Create a page "Product hub" with sub-pages for Roadmap, PRDs, Research and Decisions.
    2. Make Roadmap a database with Status, Owner, Quarter and RICE score; add board, table and timeline views.
    3. Add five sample items.

!!! example "Lab 2 · PRD template (20 minutes)"
    1. In the PRDs database, create a template from `templates/01-prd-template.md`.
    2. Relate PRDs to Roadmap items.
    3. Create one PRD from the template for "Split payments".

!!! example "Lab 3 · Research repository with AI tagging (30 minutes)"
    1. Create an Interviews database: Date, Segment, Notes, Theme, Sentiment.
    2. Paste five interview notes.
    3. With Notion AI (Business): set Theme and Sentiment to AI autofill. Without it: ask Claude to tag the notes and paste the results back.

!!! example "Lab 4 · Claude writes into Notion (15 minutes)"
    1. In Claude: Settings → Connectors → Notion → Connect; allow the Product hub pages.
    2. "Create a PRD page in Product hub/PRDs for 'Saved addresses' using the template structure. Mark every assumption."
    3. Open Notion, review and edit the page.

!!! example "Lab 5 · PRD to tickets (20 minutes)"
    1. Ask Claude: "Turn the Split payments PRD into user stories with Given/When/Then acceptance criteria, grouped into three releases."
    2. If you use Linear or Jira, connect it and create the tickets in a test project; otherwise paste into a table.

!!! example "Lab 6 · Compare two PRD assistants (30 minutes)"
    Write the same one-paragraph brief into Claude (with Template 01) and into ChatPRD or Notion AI. Compare structure, accuracy, assumptions flagged and edits needed. Note which you'd use for what.

## Common mistakes

* **A PRD graveyard**: no template, no status, no owner. Use a database with Status and Owner.
* **AI-written PRDs nobody reviewed**: always run the critique and a human review meeting.
* **Unlinked evidence**: relate PRDs to interviews and metrics, so decisions can be traced.
* **Sharing too widely**: check page permissions before connecting AI tools.

## Exercises with model answers

!!! question "Exercise · Make it testable"
    Rewrite this requirement with acceptance criteria: "Split bill should be easy."

??? answer "Model answer"
    "As a diner, I can split a bill equally or by item among up to 10 people." **Given** a bill of ₹1,200 and three people splitting equally, **when** I confirm, **then** each person is asked for ₹400. **Given** item-wise split, **when** an item is unassigned, **then** I see 'Assign all items' and cannot confirm. **Given** amounts that don't divide evenly, **then** the remainder is added to the payer's share and shown clearly.

## Key takeaways

* Notion = **pages + databases + views**. Relations turn separate lists into a connected product hub.
* Use **one PRD template**, link **evidence**, log **decisions**.
* AI drafts and critiques; **you decide**. Connect Claude through the **connector** or **MCP**.

## Check your understanding

```quiz
- q: "Which Notion feature links a PRD to its roadmap item?"
  options:
    - "A toggle block"
    - "A relation property"
    - "A callout"
    - "Page cover"
  answer: 1
  why: "Relations connect pages across databases."
- q: "What makes a requirement testable?"
  options:
    - "Using the word 'easy'"
    - "Acceptance criteria such as Given / When / Then"
    - "A longer paragraph"
    - "Adding an emoji"
  answer: 1
  why: "Acceptance criteria state observable conditions and outcomes."
```

## Recommended resources

* [Notion Help Center](https://www.notion.com/help) · [Notion pricing](https://www.notion.com/pricing) · [Notion MCP](https://developers.notion.com/docs/mcp)
* [ChatPRD](https://www.chatprd.ai) · [Atlassian Rovo](https://www.atlassian.com/software/rovo) · [Linear docs](https://linear.app/docs)
* Handbook templates: 01 PRD, 02 one-pager, 09 AI PRD and evaluation

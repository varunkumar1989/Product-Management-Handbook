---
id: m13
n: 13
title: AI Tools Landscape and Your Starter Stack
subtitle: Which AI tool to use for which job, what each one costs, what you need before you start, and how the AI Tools Lab classes fit together.
summary: The map of AI tools a PM uses in 2026 (assistants, coding agents, app builders, design, docs and PRD tools, automation, chatbots and voice agents), the free and paid tiers, the accounts and setup you need, safety basics, and a study plan for the 11 AI Tools Lab classes.
hours: 4
status: drafted
sources: "Official product pages, docs and pricing pages (checked 23 Oct 2026); Module 11 (vibe coding); Module 12 (agentic AI)"
---

!!! warning "Prices and features change every month"
    Every price, free limit and feature name in the AI Tools Lab was checked on **23 October 2026** against official pages or, where noted, several independent reviews. AI tools change quickly, so **check the official pricing page before you pay or teach from these numbers**. Screens in this lab are **illustrative wireframes** that show the layout and the order of clicks. They are not real screenshots, and button names may differ slightly in the live product.

## How to use the AI Tools Lab

The AI Tools Lab is a set of hands-on classes. Each class follows the same pattern, so you can practise straight from the PDF:

1. **What the tool is and when to use it**, in plain words.
2. **What you need**: account, plan, cost, other tools.
3. **Level 1 (basic)**: your first result in under an hour.
4. **Level 2 (intermediate)**: the features working PMs use every week.
5. **Level 3 (advanced)**: connecting the tool to other apps, automating, and shipping.
6. **Labs**: numbered steps with a picture of each screen or workflow.
7. **Mistakes, exercises with model answers, a quiz and resources.**

```chart
type: steps
title: The AI Tools Lab classes in suggested order
steps:
  - ["13 · Landscape", "This class: the map, costs and setup"]
  - ["14 · Claude daily work", "Chat, Projects, files, connectors, artifacts"]
  - ["15 · Claude Code", "Build, edit, repositories, automation"]
  - ["16 · Lovable", "Prompt-to-app with database and login"]
  - ["17 · Replit and others", "Replit Agent, Bolt, v0, Cursor"]
  - ["18 · Figma", "Design, prototype, Figma Make, MCP"]
  - ["19 · Notion and PRD tools", "Docs, databases, AI PRDs"]
  - ["20 · Automation", "Zapier, Make and n8n"]
  - ["21 · Business chatbots", "WhatsApp, Slack and website bots"]
  - ["22 · Voice agents", "Phone agents for businesses"]
  - ["23 · Learning paths", "Courses, channels, 90-day plan"]
per_row: 4
caption: Classes 14 and 15 are the foundation. After them you can take 16 to 22 in any order, depending on what you need to build.
```

## The AI tools map

AI tools for PMs fall into eight groups. Most real projects combine two or three groups, for example **Claude** to write the spec, **Lovable** to build the app and **n8n** to connect it to Gmail and Slack.

```chart
type: canvas
title: The eight groups of AI tools a PM uses
cols: 4
cells:
  - title: "1 · AI assistants"
    text: ["Claude, ChatGPT, Gemini, Microsoft Copilot", "Think, write, analyse files, research", "Class 14"]
    tone: b
  - title: "2 · Coding agents"
    text: ["Claude Code, Cursor, GitHub Copilot, Codex", "Edit real code and repositories", "Class 15"]
    tone: v
  - title: "3 · App builders"
    text: ["Lovable, Replit, Bolt, v0, Figma Make", "Prompt to working web app", "Classes 16 and 17"]
    tone: g
  - title: "4 · Design"
    text: ["Figma, FigJam, Figma Make", "Screens, prototypes, design systems", "Class 18"]
    tone: w
  - title: "5 · Docs, PRDs and planning"
    text: ["Notion, ChatPRD, Confluence, Linear, Jira", "Specs, wikis, roadmaps", "Class 19"]
    tone: b
  - title: "6 · Automation"
    text: ["Zapier, Make, n8n", "Connect Gmail, Slack, Sheets, CRMs", "Class 20"]
    tone: v
  - title: "7 · Chatbots"
    text: ["WhatsApp Business Platform, Botpress, Voiceflow, n8n", "Answer customers in chat", "Class 21"]
    tone: g
  - title: "8 · Voice agents"
    text: ["Vapi, Retell AI, ElevenLabs Agents, Twilio", "Answer and make phone calls", "Class 22"]
    tone: w
caption: Pick the group by the job. Pick the tool inside the group by cost, the integrations you need and what your team already uses.
```

## Which tool for which job

```chart
type: compare
title: Job-to-tool chooser
headers: ["If you want to…", "Start with", "Free to try?", "Upgrade when"]
rows:
  - ["Write a PRD, summarise interviews, analyse a CSV", "Claude (Projects + file upload)", "Yes", "You hit message limits or need Claude Code"]
  - ["Change code in a real repository", "Claude Code", "Needs Pro or API", "Daily use: Max or a team plan"]
  - ["Build a clickable app with login and a database", "Lovable", "Yes (5 credits a day)", "You need private projects or a custom domain"]
  - ["Build and host a full-stack app in the browser", "Replit Agent", "Yes (limited)", "You publish more than one app"]
  - ["Design screens and a click-through prototype", "Figma", "Yes (Starter)", "You need Dev Mode or more files"]
  - ["Keep specs, roadmaps and research in one place", "Notion", "Yes", "You need full Notion AI (Business plan)"]
  - ["Send a Slack alert when an email arrives", "Zapier", "Yes (100 tasks a month)", "You need multi-step Zaps"]
  - ["Build complex automations cheaply", "n8n (self-hosted)", "Yes (free software)", "You want managed cloud hosting"]
  - ["Answer customers on WhatsApp", "A WhatsApp BSP + n8n or Botpress", "Trial credits only", "Real customer traffic (per-message fees)"]
  - ["Answer phone calls with AI", "Vapi or Retell AI", "Trial credits", "Any real calls (per-minute fees)"]
caption: Free tiers are enough to learn every tool in this lab. Real customer traffic (messages and calls) always costs money.
```

## What it costs: free versus paid

!!! tip "The rule for this lab"
    You can complete **every Level 1 lab for free**. Most Level 2 labs are free too. Paid tools appear only where real messages, phone calls, or production hosting are involved, and each class says so clearly.

```chart
type: compare
title: Free and paid tiers at a glance (checked 23 Oct 2026; verify before paying)
headers: ["Tool", "Free tier", "First paid tier", "What you pay for"]
rows:
  - ["Claude", "Free plan with limited messages", "Pro, about $20 a month", "More usage, Claude Code, more models; Max for heavy use"]
  - ["Claude API", "No free tier for production", "Pay per token", "Building your own apps and bots on Claude"]
  - ["Lovable", "5 credits a day (max 30 a month), public projects", "Pro, about $25 a month (100 credits)", "Private projects, custom domain, more credits"]
  - ["Replit", "Starter: daily Agent credits, 1 published app", "Core, about $20 to $25 a month", "More Agent work, more apps, collaborators"]
  - ["Figma", "Starter: limited files and AI credits", "Professional, about $16 a month per full seat", "Dev Mode, MCP server, more Figma Make use"]
  - ["Notion", "Free plan, limited AI trial", "Business, about $20 per member a month", "Full Notion AI, agents, meeting notes"]
  - ["Zapier", "100 tasks a month, two-step Zaps", "Professional", "Multi-step Zaps, more tasks"]
  - ["Make", "1,000 credits a month, 2 active scenarios", "Core", "More credits and scenarios"]
  - ["n8n", "Community Edition is free to self-host", "Cloud Starter, about €20 to €24 a month", "Managed hosting; you pay the server if self-hosting"]
  - ["WhatsApp Business Platform", "No free tier for templates", "Per delivered template message", "Marketing, utility, authentication messages; check Meta's rate card"]
  - ["Voice agents (Vapi, Retell)", "Trial credits", "Usage, roughly $0.07 to $0.30 a minute all-in", "Speech-to-text, AI model, voice, phone line"]
caption: Figures are rounded and come from the official pricing pages where available, otherwise from several 2026 reviews. Indian rupee prices vary by tax and billing region.
```

## What you need before you start

```chart
type: steps
title: One-time setup for the whole lab (about 45 minutes)
steps:
  - ["Google account", "Gmail, Drive, Sheets, Calendar for the automation labs"]
  - ["Claude account", "claude.ai, Free or Pro; install the desktop app"]
  - ["GitHub account", "github.com; needed for Claude Code, Lovable and Replit sync"]
  - ["Password manager", "Save every account and API key safely"]
  - ["Slack workspace", "Free workspace just for practice"]
  - ["Practice folder", "One folder on your laptop: AI-Tools-Lab"]
per_row: 3
caption: Use a practice Gmail and a practice Slack workspace, so a mistake in a lab never emails a real customer or posts in a real company channel.
```

**Hardware and software:** any laptop from the last five years works. For Claude Code you also need a terminal (built into macOS and Windows) and, for some installs, **Node.js** from nodejs.org. Nothing in this lab needs a powerful computer, because the AI runs in the cloud.

## Accounts, API keys and safety

Many labs connect one app to another. There are three ways apps connect, and you will meet all three:

```chart
type: layers
title: Three ways tools connect to each other
labels: ["Easiest", "Middle", "Most control"]
rows:
  - ["Built-in connector or integration: click Connect, sign in, approve"]
  - ["API key or OAuth credential pasted into an automation tool"]
  - ["MCP server: lets an AI assistant use another app's tools"]
caption: Connectors are what you use most. API keys appear in n8n, chatbots and voice agents. MCP (Model Context Protocol) is how Claude and Claude Code use tools such as Figma, Notion, GitHub and your own n8n workflows.
```

!!! warning "Five safety rules for every lab"
    1. **Never paste an API key into a chat, a document, a prompt, or frontend code.** Keep keys in the tool's secret store (n8n credentials, Lovable or Replit secrets, Netlify environment variables).
    2. **Use test data.** Do not upload customer data, salary data or anything under NDA to a free AI plan. Check your company's AI policy first.
    3. **Approve actions one by one** until a workflow has run correctly at least ten times.
    4. **Turn off what you no longer use.** Disconnect connectors and delete unused API keys.
    5. **Set spending limits** on every paid API (Anthropic Console, OpenAI, Twilio, Vapi) before your first test.

## A starter stack for three budgets

```chart
type: canvas
title: Starter stacks
cols: 3
cells:
  - title: "₹0 a month (learning)"
    text: ["Claude Free", "Lovable Free", "Figma Starter", "Notion Free", "Zapier Free or n8n on your laptop", "Telegram bot for chat practice", "Voice agent trial credits"]
    tone: g
  - title: "About $45 a month (serious PM)"
    text: ["Claude Pro (includes Claude Code)", "Lovable Pro", "Figma and Notion free tiers", "n8n self-hosted on a small server", "Pay-as-you-go API with a $10 limit"]
    tone: b
  - title: "Team or client work"
    text: ["Claude Team or Max", "Lovable or Replit paid", "Figma Professional", "Notion Business", "n8n Cloud or Make Core", "WhatsApp BSP and a voice agent platform on usage billing"]
    tone: v
caption: Start at ₹0. Upgrade one tool at a time, only when a free limit is actually blocking you.
```

## How the classes connect: one example project

The capstone that ties the lab together is a **small business assistant** for a hypothetical clinic. Each class adds one piece:

```chart
type: workflow
title: Capstone: a clinic's AI front desk, built across the lab
nodes:
  - ["human", "PRD in Notion", "Class 19: problem, users, scope"]
  - ["ai", "Spec and copy with Claude", "Class 14: Project with clinic FAQs"]
  - ["action", "Design in Figma", "Class 18: booking screens"]
  - ["action", "Build app in Lovable", "Class 16: bookings database and login"]
  - ["trigger", "New booking", "Class 20: n8n webhook"]
  - ["output", "WhatsApp confirmation", "Class 21: template message"]
  - ["ai", "Voice agent answers calls", "Class 22: books or reschedules"]
  - ["action", "Code fixes with Claude Code", "Class 15: repository and deploy"]
per_row: 4
caption: Hypothetical project for practice. Use test phone numbers and made-up patients only.
```

## Exercises with model answers

!!! question "Exercise 1 · Pick the tools"
    A D2C brand wants: a landing page with a waitlist form, an email to each signup, and a weekly Slack summary of signups. Which tools would you use, free first?

??? answer "Model answer"
    Landing page and form: **Lovable** (free tier) or **Claude artifacts** for a quick static page. Email and Slack: **Zapier** (free covers a two-step "new form row → send email" Zap) plus a second Zap for the weekly summary, or one **n8n** workflow that does both. Summary text: an **AI step** (Claude via n8n, or Zapier's AI step). Paid only when signups exceed the free task limits.

!!! question "Exercise 2 · Spot the risk"
    A teammate pasted the company's OpenAI API key into a Lovable prompt so the app "can talk to AI". What is wrong, and what should they do?

??? answer "Model answer"
    The key is now in the chat history and may end up in frontend code where any visitor can read it. **Revoke the key immediately**, create a new one, and store it as a **secret** (Lovable Cloud or Supabase secrets) used only by a server-side function. Set a spending limit on the new key.

## Key takeaways

* Choose the tool group by the **job**, and the tool by **cost, integrations and team fit**.
* Every Level 1 lab is **free**. Messages, calls and production hosting are what cost money.
* Keep **secrets out of prompts and frontend code**, use **test data**, and set **spending limits**.
* Connectors, API keys and **MCP** are the three ways tools talk to each other.

## Check your understanding

```quiz
- q: "Which group would you use to change code inside an existing GitHub repository?"
  options:
    - "AI assistants such as the Claude chat app"
    - "Coding agents such as Claude Code"
    - "Automation tools such as Zapier"
    - "Voice agents"
  answer: 1
  why: "Coding agents read, edit and commit code in a real repository."
- q: "What usually costs money even when you are only testing a WhatsApp or phone bot with real people?"
  options:
    - "Writing the prompt"
    - "Designing the flow in Figma"
    - "Delivered messages and call minutes"
    - "Creating a Google account"
  answer: 2
  why: "Messaging and telephony are billed per message or per minute."
- q: "Where should an API key for an automation live?"
  options:
    - "In the prompt so the AI can see it"
    - "In a shared Google Doc"
    - "In the tool's credential or secret store"
    - "In the website's JavaScript"
  answer: 2
  why: "Credential stores keep keys encrypted and out of chats and frontend code."
```

## Recommended resources

* [Claude pricing](https://claude.com/pricing) · [Lovable pricing](https://lovable.dev/pricing) · [Replit pricing](https://replit.com/pricing) · [Figma pricing](https://www.figma.com/pricing/)
* [Notion pricing](https://www.notion.com/pricing) · [Zapier pricing](https://zapier.com/pricing) · [Make pricing](https://www.make.com/en/pricing) · [n8n pricing](https://n8n.io/pricing/)
* [WhatsApp Business Platform pricing (Meta)](https://developers.facebook.com/docs/whatsapp/pricing)
* [Model Context Protocol](https://modelcontextprotocol.io/) — the standard behind Claude's connectors.

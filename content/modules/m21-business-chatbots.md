---
id: m21
n: 21
title: "AI Chatbots for Business: WhatsApp, Slack and Web"
subtitle: Design, build, test and price AI chatbots that answer customers on WhatsApp, help employees in Slack, and sit on a website, with safe handoff to people.
summary: Chatbot types and channels, the WhatsApp Business App versus the WhatsApp Business Platform, Business Solution Providers, Meta's requirements (business portfolio, templates, 24-hour window, opt-in), per-message pricing, the bot architecture with n8n and Claude, no-code builders, Slack, Telegram and website bots, knowledge bases and tools, human handoff, guardrails, privacy, evaluation, metrics, costs and six labs.
hours: 8
status: drafted
sources: "Meta WhatsApp Business Platform docs and pricing page; BSP documentation; n8n WhatsApp, Telegram and Slack node docs; Module 10 (RAG) and Module 12 (agents); handbook dataset support_eval_set.csv; checked 23 Oct 2026"
---

!!! warning "Messaging rules and prices change"
    Meta updates WhatsApp pricing and policies several times a year. Always check the [official pricing page](https://developers.facebook.com/docs/whatsapp/pricing) and your provider's rates before launch. Examples use **hypothetical businesses**; screens are **illustrative wireframes**.

## What a business chatbot does

A business chatbot answers questions and completes simple tasks in a chat channel: order status, booking an appointment, store hours, return policy, lead capture. An **AI chatbot** uses a language model (such as Claude) plus your business's **knowledge** and **tools**, so it can understand free-text questions instead of only menu buttons.

```chart
type: canvas
title: Channels and when to use them
cols: 3
cells:
  - title: "WhatsApp"
    text: ["Where Indian customers already are", "Orders, bookings, reminders, support", "Needs the Business Platform for automation"]
    tone: g
  - title: "Website chat widget"
    text: ["Pre-sales questions, lead capture", "Fully under your control"]
    tone: b
  - title: "Instagram / Messenger"
    text: ["D2C brands, creators", "Same Meta platform family"]
    tone: v
  - title: "Slack or Microsoft Teams"
    text: ["Internal bots: HR policy, IT help, sales enablement"]
    tone: w
  - title: "Telegram"
    text: ["Free and quick to set up", "Perfect for practice and communities"]
    tone: r
  - title: "Voice (phone)"
    text: ["Calls instead of chat", "See Class 22"]
    tone: b
caption: The AI part is the same across channels. What changes is the channel's rules, costs and setup.
```

## WhatsApp: App or Platform?

```chart
type: compare
title: WhatsApp Business App vs WhatsApp Business Platform
headers: ["", "WhatsApp Business App", "WhatsApp Business Platform (API)"]
rows:
  - ["Who it is for", "Small shops replying by hand", "Businesses automating or scaling"]
  - ["Cost", "Free app", "Per delivered template message, plus any provider fee"]
  - ["Automation", "Greeting, away message, quick replies only", "Full bots, AI, integrations"]
  - ["Users", "Phone plus a few linked devices", "Unlimited agents through a provider's inbox"]
  - ["Setup", "Download and verify the number", "Meta business portfolio, number, display name, templates"]
  - ["AI chatbot", "Not supported directly", "Yes, via webhooks to n8n, a provider or your code"]
caption: For an AI chatbot you need the Business Platform, used directly through Meta's Cloud API or through a Business Solution Provider.
```

### Direct Cloud API or a Business Solution Provider (BSP)?

* **Meta Cloud API directly**: no middleman fee; you connect it to n8n or your own code. Best when someone technical owns it.
* **A BSP** (for example Twilio, Gupshup, Interakt, WATI, AiSensy, 360dialog): onboarding help, a shared team inbox, broadcast tools and no-code flow builders; they add a monthly fee or a markup per message.

### What Meta requires

```chart
type: steps
title: Getting a business onto the WhatsApp Business Platform
steps:
  - ["Meta business portfolio", "business.facebook.com; business verification raises your limits"]
  - ["Phone number", "A number not active in the WhatsApp app (or migrate it)"]
  - ["Display name", "Reviewed by Meta; must match your business"]
  - ["Templates", "Business-started messages need pre-approved templates"]
  - ["Opt-in", "Customers must agree to receive your messages"]
  - ["Webhook", "Where incoming messages are sent: n8n, a BSP or your server"]
per_row: 3
caption: For testing, Meta's developer dashboard gives you a test number that can message a small list of your own verified phone numbers.
```

**The 24-hour customer service window.** When a customer messages you, a 24-hour window opens in which you can reply freely. Outside that window, a business can only start the conversation with an **approved template**.

### Pricing basics (checked 23 Oct 2026)

* Since July 2025 Meta charges **per delivered template message**. The rate depends on the template **category** (marketing, utility, authentication) and the recipient's **country**. Marketing costs the most; authentication (OTP) the least.
* Rates differ by country. Several 2026 guides quote India authentication messages at a fraction of a rupee and marketing messages at a few times that. Use Meta's current rate card, not a blog.
* Independent guides report that from **1 October 2026** Meta began charging for some messages inside the 24-hour window that used to be free (service and utility replies). **Confirm this on Meta's pricing page** before you forecast costs.
* Add the **BSP's fee** and the **AI model's cost** (a few paise to a few rupees per conversation, depending on length and model).

## How an AI WhatsApp bot works

```chart
type: workflow
title: AI WhatsApp assistant for a clinic (hypothetical)
nodes:
  - ["trigger", "Customer messages on WhatsApp", "'Can I move my appointment to Friday?'"]
  - ["action", "WhatsApp Cloud API webhook", "Message arrives in n8n (WhatsApp Trigger)"]
  - ["ai", "AI Agent (Claude)", "Instructions, last 10 messages as memory"]
  - ["data", "Knowledge base", "FAQ, prices, hours (Sheet or vector store)"]
  - ["action", "Tools", "find_booking, reschedule_booking (Sheets or your app's API)"]
  - ["logic", "Needs a human?", "Complaint, medical question, low confidence"]
branch:
  paths:
    - ["no", [["output", "Reply on WhatsApp", "Confirm new time; send summary"]]]
    - ["yes", [["human", "Handoff", "Slack alert + provider inbox; tell customer a person will reply"]]]
caption: The bot answers only from the knowledge base and acts only through named tools. Anything sensitive goes to a person.
```

```chart
type: phone
title: The customer's view
screens:
  - name: "Reschedule"
    items:
      - ["bar", "Sunrise Physio"]
      - ["text", "You: Can I move my appointment to Friday?"]
      - ["text", "Bot: I found your booking for Wed 23 Oct, 10:00. Friday has 11:00 or 16:30. Which works?"]
      - ["btn", "11:00"]
      - ["btn", "16:30"]
    notes: ["Bot finds the booking with a tool", "Quick-reply buttons reduce typing"]
  - name: "Handoff"
    items:
      - ["bar", "Sunrise Physio"]
      - ["text", "You: My knee is much worse after the session."]
      - ["warn", "Connecting you to our team"]
      - ["text", "Bot: I'm sorry to hear that. A physiotherapist will reply here within 30 minutes. If it's an emergency, call 112."]
    notes: ["Health concerns always go to a person", "Say what happens next and when"]
caption: Hypothetical clinic and messages, for practice only.
```

## No-code options

| Tool | What it is | Good for |
|---|---|---|
| **BSP flow builders** (Interakt, WATI, AiSensy, Gupshup) | Menus, forms and AI replies inside the provider | Fast WhatsApp launch for SMBs |
| **Botpress** | Visual bot builder with AI and many channels | Multi-channel bots with knowledge bases |
| **Voiceflow** | Conversation design and AI agents, chat and voice | Teams designing complex flows |
| **Chatbase** | Train a bot on your website or documents | Website FAQ bot in minutes |
| **Intercom Fin, Zendesk AI** | AI agents inside support suites | Companies already on those helpdesks |
| **n8n + Claude** | Build exactly what you need | Custom tools, privacy, low running cost |

## Slack, Telegram and website bots

* **Slack internal bot**: create a Slack app with the Events API and bot scopes (`app_mentions:read`, `chat:write`), connect it to n8n's Slack Trigger, and answer from your HR or IT policy documents. Restrict it to the channels it's invited to.
* **Telegram practice bot**: message **@BotFather**, send `/newbot`, copy the token, add it to n8n's Telegram Trigger. It's free and takes ten minutes, ideal for learning before WhatsApp.
* **Website widget**: the "Ask us" button from Class 16 (Lovable server function + Claude), or a Botpress or Chatbase embed code pasted into your site.

## Design the bot before you build it

!!! level2 "The one-page bot spec"
    1. **Job**: the top 10 questions and 3 tasks the bot handles (from real support tickets).
    2. **Not allowed**: medical, legal or financial advice; refunds above a limit; anything about other customers.
    3. **Knowledge**: the exact documents and their owner; how often they're updated.
    4. **Tools**: each action with inputs, and whether it needs confirmation.
    5. **Handoff**: when, to whom, within what time, and what the customer is told.
    6. **Tone and language**: for example English and Hindi, friendly and short.
    7. **Privacy**: what data is stored, for how long, and the opt-out keyword ("STOP").
    8. **Success metrics**: containment rate, resolution rate, handoff rate, CSAT, cost per conversation.

## Guardrails, privacy and quality

!!! warning "Rules that protect customers and the business"
    * **Answer only from the knowledge base**; say "I'm not sure, let me connect you" otherwise.
    * **Confirm before acting** ("Shall I move it to Friday 11:00?").
    * **Never collect** card numbers, passwords or OTPs in chat.
    * **Get opt-in** before marketing messages and honour opt-outs immediately.
    * Follow data-protection law (in India, the **DPDP Act**): collect the minimum, explain the purpose, delete on request.
    * **Log conversations** for quality review, with access limited to staff who need it.

### Evaluate before launch

Use `datasets/support_eval_set.csv` from this handbook (or 50 real anonymised questions): run every question through the bot, then score **correct, safe, handed off when it should, tone**. Fix the knowledge base or instructions, and re-run until it passes your bar (see template 09 for the evaluation plan).

## Costs at a glance (illustrative)

| Item | Typical cost driver |
|---|---|
| WhatsApp template messages | Per delivered message by category and country |
| BSP | Monthly plan or per-message markup |
| AI model | Per token; short FAQ chats are cheap, long ones cost more |
| n8n | Free self-hosted (server cost) or a cloud plan |
| People | Staff to handle handoffs and keep knowledge current |

## Labs

!!! example "Lab 1 · Telegram FAQ bot (free, 40 minutes)"
    1. Create a bot with @BotFather and copy the token.
    2. n8n: Telegram Trigger → AI Agent (Claude, or Gemini free tier) with instructions and a 15-line FAQ pasted into the system prompt → Telegram "send message".
    3. Test ten questions, including two it should refuse.

!!! example "Lab 2 · WhatsApp test number (free test, 45 minutes)"
    1. Create an app at developers.facebook.com, add the **WhatsApp** product, and use the provided **test number**. Add your own phone as a recipient.
    2. n8n: add a WhatsApp credential (access token and phone number ID) and a WhatsApp Trigger; register its webhook URL in the Meta dashboard.
    3. Reuse the Lab 1 AI Agent and reply with the WhatsApp node.
    4. Message the test number from your phone and check the reply.

!!! example "Lab 3 · Knowledge base and a booking tool (45 minutes)"
    1. Put FAQs in a Google Sheet (question, answer, category). Give the agent a **Sheets tool** to look them up.
    2. Add a Bookings sheet and a tool `find_booking(phone)`; then `reschedule_booking(id, new_time)` with confirmation required.
    3. Test the reschedule conversation from the phone picture above.

!!! example "Lab 4 · Human handoff (20 minutes)"
    Add an IF node: if the agent sets `handoff: true` (complaint, health issue, low confidence), post the conversation to Slack #practice-support and send the customer the handoff message.

!!! example "Lab 5 · Slack HR policy bot (30 minutes)"
    Create a Slack app with Events and the scopes above, connect n8n's Slack Trigger, and answer from a 2-page policy document. Mention the bot in a channel and ask three questions.

!!! example "Lab 6 · Evaluate (30 minutes)"
    Run 30 questions from `support_eval_set.csv` through your bot with a loop in n8n, write answers to a sheet, and score them. Fix the top two failure patterns and re-run.

## Exercises with model answers

!!! question "Exercise · Template or free reply?"
    (a) A customer asked about delivery 2 hours ago; you reply with tracking. (b) You want to tell all past customers about a Diwali sale. (c) You send an OTP to log in.

??? answer "Model answer"
    (a) Inside the 24-hour window, so a normal reply (check whether your country's current rules charge for it). (b) A **marketing template**, approved by Meta, only to opted-in customers. (c) An **authentication template**.

## Key takeaways

* AI chatbots need **knowledge, tools, guardrails and a handoff to people**.
* WhatsApp automation needs the **Business Platform** (direct Cloud API or a **BSP**), approved **templates**, the **24-hour window** and **opt-in**.
* Pricing is **per delivered template message** by category and country, plus provider and AI costs.
* Practise on **Telegram** for free, then use Meta's **test number** before going live.
* **Evaluate** with a question set and track containment, handoffs and CSAT.

## Check your understanding

```quiz
- q: "Which WhatsApp option supports an AI chatbot connected to n8n?"
  options:
    - "WhatsApp Business App"
    - "WhatsApp Business Platform (Cloud API or BSP)"
    - "Personal WhatsApp"
    - "WhatsApp Web"
  answer: 1
  why: "Automation and webhooks require the Business Platform."
- q: "A business wants to message a customer who last wrote 3 days ago. What's needed?"
  options:
    - "Nothing"
    - "An approved template message"
    - "A voice call"
    - "A new phone number"
  answer: 1
  why: "Outside the 24-hour window, businesses can only start with an approved template."
- q: "A customer describes a worsening injury to a clinic bot. The bot should…"
  options:
    - "Give treatment advice"
    - "Hand off to a person and give emergency guidance"
    - "Ignore it"
    - "Offer a discount"
  answer: 1
  why: "Health concerns are out of scope for the bot and must reach a qualified person."
```

## Recommended resources

* [WhatsApp Business Platform docs](https://developers.facebook.com/docs/whatsapp) · [Pricing](https://developers.facebook.com/docs/whatsapp/pricing)
* [n8n WhatsApp node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/) · [n8n Telegram node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/)
* [Botpress](https://botpress.com) · [Voiceflow](https://www.voiceflow.com) · [Slack Events API](https://api.slack.com/apis/events-api)
* Module 10 (RAG) for knowledge bases; Module 12 (agents) for tool safety

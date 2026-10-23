---
id: m22
n: 22
title: Voice Agents for Businesses
subtitle: Build AI phone agents that answer and make calls for clinics, salons, shops and service companies, with the right platform, phone number, tools, costs and legal care.
summary: Voice agent use cases, how a call works (telephony, speech-to-text, the AI model, text-to-speech, turn-taking), platforms (Vapi, Retell AI, ElevenLabs Agents, Bland, Synthflow, Twilio) and Indian telephony providers, real per-minute costs, phone numbers and regulations, conversation design, tools through n8n, handoff to humans, testing and metrics, and five labs.
hours: 7
status: drafted
sources: "Vendor docs and pricing pages for Vapi, Retell AI, ElevenLabs, Twilio; independent 2026 pricing comparisons; TRAI and FCC public guidance; Module 12; checked 23 Oct 2026"
---

!!! warning "Costs and rules vary by country"
    Per-minute prices change often and depend on the voice, AI model and phone carrier. Telecom and consent rules differ by country. Check each vendor's pricing page and get legal advice before calling real customers. Examples are **hypothetical**; screens are **illustrative wireframes**.

## What a voice agent does

A **voice agent** is an AI that talks on the phone (or in a browser or app). It listens, understands, answers, and can take actions such as booking an appointment, then hands the call to a person when needed.

```chart
type: canvas
title: Good first use cases
cols: 3
cells:
  - title: "Receptionist"
    text: ["Answer after-hours calls", "Hours, prices, directions", "Book or reschedule"]
    tone: g
  - title: "Reminders"
    text: ["Appointment and delivery reminders", "Confirm or reschedule in the call"]
    tone: b
  - title: "Lead qualification"
    text: ["Call back web leads within minutes", "Ask 3–5 questions, book a sales call"]
    tone: v
  - title: "Order and status lines"
    text: ["Where is my order?", "Return policy, store stock"]
    tone: w
  - title: "Surveys and feedback"
    text: ["Short NPS or post-visit calls", "Summaries to a sheet"]
    tone: r
  - title: "Not a good first use"
    text: ["Medical or legal advice", "Debt collection without legal review", "Anything needing judgement or empathy at length"]
    tone: r
caption: Start with short, repetitive calls where the caller's goal is clear and mistakes are easy to fix.
```

## How a call works

```chart
type: layers
title: Inside a voice agent call
labels: ["Phone", "Listen", "Think", "Speak", "Act"]
rows:
  - ["Caller", "Phone number (Twilio, Plivo, Exotel or the platform)"]
  - ["Speech-to-text: turns speech into words in real time"]
  - ["AI model (Claude or others) with instructions, memory and tools"]
  - ["Text-to-speech: a natural voice speaks the reply"]
  - ["Tools: check calendar, book, look up order", "Transfer to a human", "Post-call summary"]
edges:
  - ["Phone number (Twilio, Plivo, Exotel or the platform)", "Speech-to-text: turns speech into words in real time"]
  - ["Speech-to-text: turns speech into words in real time", "AI model (Claude or others) with instructions, memory and tools"]
  - ["AI model (Claude or others) with instructions, memory and tools", "Text-to-speech: a natural voice speaks the reply"]
  - ["AI model (Claude or others) with instructions, memory and tools", "Tools: check calendar, book, look up order"]
caption: Voice platforms join these pieces, handle interruptions (barge-in) and pauses, and keep the delay to about a second. Some setups use a single speech-to-speech model instead of separate listen and speak steps.
```

## Platforms

```chart
type: compare
title: Voice agent platforms (checked 23 Oct 2026; verify pricing)
headers: ["Platform", "Style", "Pricing model", "Typical all-in cost per minute", "Good for"]
rows:
  - ["Vapi", "Developer platform, very flexible", "Platform fee (about $0.05/min) plus your chosen speech, model, voice and phone providers", "about $0.13 to $0.32", "Custom builds, choosing each component"]
  - ["Retell AI", "Developer-friendly with a strong dashboard", "Usage per minute, phone line included", "about $0.07 to $0.31", "Fast setup, receptionists and outbound"]
  - ["ElevenLabs Agents", "Best-known for natural voices", "Plans with included minutes, extra minutes billed; phone carrier separate", "about $0.08 and up", "Voice quality, many languages"]
  - ["Bland AI", "Enterprise phone agents", "Per minute", "varies", "High-volume calling"]
  - ["Synthflow", "No-code builder", "Plans with minutes", "varies", "Non-technical teams"]
  - ["Twilio (ConversationRelay and others)", "Build-your-own on a phone platform", "Telephony plus your AI costs", "varies", "Engineering teams wanting full control"]
caption: All-in cost includes speech-to-text, the AI model, the voice and the phone line. Figures are ranges from several 2026 comparisons, not quotes.
```

**Phone numbers in India.** Providers such as **Exotel**, **Plivo** and **Knowlarity** offer Indian virtual numbers and connect to voice platforms (often via SIP). Indian numbers require KYC documents. International platforms may offer Indian numbers only through a partner, so check availability before choosing a platform.

**Indian languages.** Check each platform's supported languages and test Hindi and regional-language calls with real speakers. Accents, code-mixing (Hinglish) and background noise affect accuracy.

### What it costs: a worked example

A clinic receives **1,000 calls a month, averaging 3 minutes**. At **$0.15 per minute** all-in, that is 1,000 × 3 × $0.15 = **$450 a month** (about ₹38,000 at ₹84 to the dollar), plus a phone number fee, the platform's plan, and staff time for handoffs. Compare it with the cost of missed calls and of staff answering them.

## The law and consent (summary, not legal advice)

!!! warning "Before any real call"
    * **Tell callers it's an AI** at the start, and say if the call is recorded.
    * **Outbound calls** need prior consent. In India, commercial calls fall under **TRAI's commercial communication rules** (registration, DND preferences, consent). In the US, the FCC treats AI-generated voices in robocalls as "artificial" under the **TCPA**, so prior express consent is required.
    * **Personal data**: collect the minimum, store recordings securely and delete them on schedule (India's **DPDP Act**, GDPR in Europe).
    * Offer a **human option** ("press 0 or say 'agent'") and honour do-not-call requests.

## Designing the conversation

```chart
type: steps
title: A good receptionist call (salon, hypothetical)
steps:
  - ["Greet and disclose", "'Hi, this is Ria, the AI assistant for Glow Salon. How can I help?'"]
  - ["Understand", "Ask one question at a time; short sentences"]
  - ["Look up", "Tool: check_availability(service, date)"]
  - ["Confirm", "Read back service, date, time, name and phone"]
  - ["Act", "Tool: book_appointment(...); send SMS or WhatsApp confirmation"]
  - ["Close or hand off", "Anything else? Transfer to staff for complaints or unclear requests"]
per_row: 3
caption: Read back every detail before acting. Spoken numbers and names are easy to mishear.
```

!!! tip "Voice prompt rules"
    * Replies under **two sentences**; no lists, tables or URLs (they don't work in speech).
    * Say numbers the way people speak them ("four-thirty in the afternoon").
    * Handle silence ("Are you still there?") and interruptions gracefully.
    * Give a clear way out: "If you'd like to talk to someone, just say 'staff'."
    * Never guess. "I'm not sure, let me get a colleague to call you back."

## Build it: platform + n8n tools

```chart
type: window
title: A voice platform's agent setup
app: "Voice agent dashboard"
sidebar: ["*Agents", "Phone numbers", "Tools", "Calls & logs", "Billing"]
main:
  - ["bar", "Agent: Glow Salon receptionist"]
  - ["input", "[1] Instructions: You are Ria, the AI receptionist for Glow Salon…"]
  - ["row", "Model|Claude (or another LLM)"]
  - ["row", "[2] Voice|Warm female, Indian English"]
  - ["row", "Transcriber|Real-time, en-IN + hi-IN"]
  - ["row", "[3] Tools|check_availability, book_appointment"]
  - ["row", "Transfer number|+91 ••• staff line"]
  - ["btn", "[4] Talk to agent (test in browser)"]
panel:
  - ["bar", "First message"]
  - ["text", "Hi, this is Ria, the AI assistant for Glow Salon. How can I help today?"]
  - ["bar", "Post-call webhook"]
  - ["input", "https://your-n8n/webhook/call-summary"]
notes:
  - "Instructions are the system prompt: role, scope, tone, rules and when to transfer."
  - "Pick a voice and transcription language your callers use; test with real speakers."
  - "Tools call your n8n webhooks, which read or write Google Calendar, Sheets or your app."
  - "Test in the browser for free before you buy a phone number."
caption: Names and layout differ between Vapi, Retell AI and ElevenLabs, but every platform has these settings.
```

```chart
type: workflow
title: The tool behind 'check_availability' (n8n)
nodes:
  - ["trigger", "Webhook from the voice platform", "service, date"]
  - ["action", "Google Calendar: get events", "Salon calendar for that date"]
  - ["logic", "Find free slots", "Code or Filter node"]
  - ["output", "Respond to webhook", "'Free at 11:00 and 16:30'"]
per_row: 4
caption: Keep tool responses short and plain, because the agent reads them aloud. Respond within a couple of seconds or callers hear silence.
```

## Labs

!!! example "Lab 1 · Browser test call (free trial credits, 30 minutes)"
    1. Sign up for Vapi, Retell AI or ElevenLabs Agents and create an agent from a receptionist template.
    2. Write the instructions and first message for Glow Salon (hypothetical), with hours, prices and three services.
    3. Click **talk/test** and make five test calls, including one where you interrupt and one where you ask for a human.

!!! example "Lab 2 · Availability and booking tools (60 minutes)"
    1. Build the n8n `check_availability` workflow above and a `book_appointment` workflow that creates a Google Calendar event.
    2. Add both as tools in the voice platform, with clear descriptions and parameters.
    3. Test a full booking. Check the calendar event appears.

!!! example "Lab 3 · Post-call summary (20 minutes)"
    Set the platform's post-call webhook to an n8n workflow that writes caller, intent, outcome and summary to a Sheet and posts transfers to Slack.

!!! example "Lab 4 · Inbound phone number (paid, 20 minutes)"
    Buy or import a phone number (platform or Twilio; in India via a provider such as Exotel or Plivo, which needs KYC). Attach it to the agent and call it from your phone. Add the AI disclosure and recording notice to the first message.

!!! example "Lab 5 · Test plan (30 minutes)"
    Write 20 test scenarios (booking, rescheduling, unclear request, background noise, Hindi caller, angry caller, wrong number). Run them, score each (resolved, transferred correctly, mistakes), fix the instructions and re-test.

## Metrics

| Metric | What it tells you |
|---|---|
| **Containment / resolution rate** | Share of calls fully handled by the agent |
| **Correct transfer rate** | It handed off the calls it should have |
| **Booking conversion** | Calls that ended in a booking |
| **Response latency** | Time from caller stopping to agent speaking; aim for about a second |
| **Transcription accuracy** | Mis-heard names and numbers |
| **Average handle time and cost per call** | Efficiency and budget |
| **CSAT or complaints** | Caller experience |

## Exercises with model answers

!!! question "Exercise · Price it"
    A car service centre gets 600 calls a month, 4 minutes each. Platform quotes $0.12 a minute all-in. Staff handle 20% of calls after transfer. Monthly AI cost?

??? answer "Model answer"
    600 × 4 × $0.12 = **$288** a month for agent minutes (assuming the transfer happens after most of the call; transferred minutes may continue to be billed until the agent leaves the call). Add the number rental and platform plan, and staff time for the 120 transferred calls.

!!! question "Exercise · Fix the script"
    The agent says: "Our services include haircut ₹500, colour ₹2,500, spa ₹1,800, visit glowsalon.com/book or press 1 for…" What's wrong?

??? answer "Model answer"
    Too long, a list and a URL in speech. Better: "We do haircuts, colour and spa treatments. Which one are you interested in?" Then give the one price asked for, and offer to book or send a WhatsApp link.

## Key takeaways

* A voice agent = **phone + speech-to-text + AI model + text-to-speech + tools + handoff**.
* Choose **Retell AI or ElevenLabs** for speed, **Vapi or Twilio** for control, a **no-code** builder for non-technical teams.
* Budget **all-in per-minute** cost, not the headline platform fee.
* **Disclose AI**, get **consent** for outbound calls, and follow local telecom and privacy rules.
* **Read back details**, keep replies short, and test with real speakers before going live.

## Check your understanding

```quiz
- q: "Why can the all-in cost be several times the platform's headline per-minute fee?"
  options:
    - "Taxes only"
    - "Speech-to-text, the AI model, the voice and the phone line are billed too"
    - "Because of the logo"
    - "It can't"
  answer: 1
  why: "Each component has its own per-minute or per-token price."
- q: "What should an outbound sales voice agent have before calling?"
  options:
    - "A funny greeting"
    - "Prior consent from the person and compliance with telecom rules"
    - "A longer script"
    - "A website"
  answer: 1
  why: "Consent and telecom regulations apply to automated and AI calls."
- q: "Which reply style works best on a phone call?"
  options:
    - "A bulleted list with links"
    - "Short sentences, one question at a time"
    - "A long paragraph"
    - "A table"
  answer: 1
  why: "Listeners can't scan; short, single questions are easiest to follow."
```

## Recommended resources

* [Vapi docs](https://docs.vapi.ai) · [Retell AI docs](https://docs.retellai.com) · [ElevenLabs Agents docs](https://elevenlabs.io/docs) · [Twilio Voice](https://www.twilio.com/docs/voice)
* [TRAI](https://www.trai.gov.in) for Indian commercial-communication rules · [FCC on AI-generated voices in robocalls](https://www.fcc.gov)
* Module 12 (agentic AI) for tool safety and evaluation

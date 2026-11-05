## Follow one tap through the system: the OTP login walkthrough

!!! source "From your class deck (Week 9 · Tech 101 and System Design)"
    The deck uses an OTP login to show how one user action travels through frontend, API, backend, database and a third-party service, and how each layer can fail. It then repeats the idea for a referral flow and a payment flow.

A one-time-password (OTP) login looks simple. Here is what really happens, and the questions a PM should ask at each step.

| Step | What the user sees | What the system does | PM questions |
|---|---|---|---|
| **1. Enter number** | A phone field and a "Get OTP" button | **Frontend** checks the format (10 digits), disables the button, shows a loader | What if the user mistypes? Is autofill supported? Which country codes? |
| **2. Request sent** | Loading spinner | **API call** sends the number to the server over HTTPS | What if the network drops? Do we retry safely? |
| **3. Backend logic** | Nothing | Validates the request, checks rate limits (to stop abuse), creates a random code with a short expiry | How many OTPs per number per hour? How long is a code valid? |
| **4. Database** | Nothing | Stores the code (hashed), attempts and status; finds or creates the user record | What do we store, for how long, and who can see it (privacy)? |
| **5. Third-party SMS service** | An SMS arrives | The backend calls an SMS provider, which routes through carriers | What if delivery is slow? Is there a fallback (voice call, email, WhatsApp)? |
| **6. Verify** | User types the code | API checks code, expiry and attempts; issues a session token | What after 3 wrong tries? Can the screen auto-read the SMS? |
| **7. Logged in** | Home screen | Frontend stores the token; later requests include it | What if the token is stolen? How long does a session last? |

**Common failure points:** SMS delay (vendor or carrier), wrong-code attempts, expired codes, rate limits blocking real users, regional blocks (do-not-disturb rules), and long flows that lose users. A good PM designs for the failure paths, not only for the success path.

### Why one flow helps you understand everything

Every product action (place an order, send a message, pay a bill) follows the same chain: **user action → frontend → API → backend logic → database → third-party services → response back to the screen**. When something is slow or broken you can ask: *which layer?*

!!! tip "A question to ask in standups"
    "Is the problem on the screen, in the request, in our logic, in our data, or with a vendor?" This one question turns vague bugs into assignable work.

## Requests, responses and status codes as user experience

Every API call is a **request** (what the app asks) and a **response** (what the server answers). The **status code** says how it went, and each family implies a different user experience.

| Code family | Examples | Meaning | What the user should see |
|---|---|---|---|
| **2xx success** | 200 OK, 201 Created | It worked | Confirmation and the next step |
| **3xx redirect** | 301, 302 | Look elsewhere | Usually invisible |
| **4xx client problem** | 400 bad input, 401 not logged in, 403 not allowed, 404 not found, 429 too many requests | The request was wrong or limited | A specific, helpful message: "Enter a valid 10-digit number", "Please log in again", "Too many tries, wait 30 seconds" |
| **5xx server problem** | 500, 502, 503, 504 | Our side failed | An apology, a safe retry and no lost data: "We could not place your order. You were not charged." |

!!! tip "Do not design only the happy path"
    List every error code your flow can return and write the message, the retry rule and the support path for each. A generic "Something went wrong" is a design bug.

### Internet vs web, client vs server

* The **internet** is the global network of connected computers. The **web** is one service that runs on it: pages and apps requested with HTTP.
* The **client** (browser or app) asks; the **server** answers. Many products also have **servers talking to servers** (your backend to a payment gateway).
* Slowness can come from the device, the network, the server, the database or a vendor. Ask for timing at each hop.

## Data, memory and speed: databases, compute and mobile constraints

### Databases as the product's memory

A product's features are only as good as what it remembers: users, orders, preferences, history. Think of the database as the **memory** and the backend as the **brain**.

| Store type | Shape | Good for | Product examples |
|---|---|---|---|
| **SQL (relational)** | Tables, rows, joins | Orders, payments, accounts, reports: anything needing consistency | Order history, wallet balance |
| **Document** | JSON-like documents | Flexible, nested data | Product catalogue, user profiles |
| **Key-value** | One key, one value, very fast | Sessions, carts, counters, caches | Logged-in session, rate-limit counters |
| **Graph** | Nodes and relationships | Connections and recommendations | "People you may know", fraud rings |
| **Wide-column / time-series** | Huge write volumes | Events, sensor data, chats | Order status events |
| **Vector** | Meaning as numbers | AI search | Semantic search for help articles |

**PM rule:** choose by **access pattern and correctness needs**, not fashion. Many products use several stores.

### Compute, memory and why products become slow

* **Compute (CPU/GPU)** does the work; **memory (RAM)** holds what it is working on right now; **storage** keeps data long-term.
* A feature gets slow when it needs more computing than provisioned, loads too much data into memory, or makes many small calls in sequence.
* Fixes: better queries and indexes, caching, doing work in the background, smaller payloads, scaling servers. Ask engineers which applies and what each costs.

### Web vs mobile: same logic, different constraints

| | Web | Mobile app |
|---|---|---|
| **Updates** | Instant for all users | Needs an app-store release; users update slowly |
| **Network** | Usually stable | Weak, switching networks, offline moments |
| **Device** | Large screen, keyboard | Small screen, touch, battery, camera, GPS, push notifications |
| **Distribution** | Link and search | App stores and installs |
| **Design implication** | Responsive layouts | Thumb reach, offline states, background limits |

Implication for requirements: specify behaviour **per platform** (what happens with no network, with an old app version, with a low-end device).

## Caching, CDNs, async work and observability: making products feel fast and reliable

| Technique | What it does | PM implication |
|---|---|---|
| **Caching** | Keeps recent answers close for quick reuse | Faster pages and lower cost, but data can be stale; decide how fresh each screen must be |
| **CDN** | Serves images, video and static files from servers near the user | Faster loads for a country-wide audience; plan for cache refresh when assets change |
| **Asynchronous processing** | Slow work (sending email, generating invoices, video processing) happens in the background while the user continues | Show "we are working on it" and notify when done; handle failure and retry |
| **Polling vs webhooks** | **Polling:** keep asking "is it done?". **Webhook:** the other system tells you when it is | Webhooks are faster and cheaper but need retry and security design; polling is simple but wasteful |
| **Logging** | Records what happened (events, errors) | Needed to debug and audit; decide what is logged and for how long (privacy) |
| **Monitoring and alerts** | Watches metrics (errors, latency) and alerts people | Define SLAs and what "healthy" means; ask for dashboards in your launch checklist |

!!! hypo "Worked example · why 'order placed' is asynchronous (hypothetical)"
    After you tap Pay, the screen shows "Order received" within a second. In the background: payment is confirmed by the gateway, the restaurant is notified, a delivery partner is searched and a confirmation SMS is sent. If the gateway confirms late, the order stays "pending" and the app polls or waits for a webhook. A PM decides what to show in each state and when to give up and refund.

## Functional and non-functional requirements

!!! source "From your class deck (Week 9)"
    The deck separates **functional requirements** (what the system should do) from **non-functional requirements** (NFRs: how well it should do it), uses a messaging app as the example, and contrasts weak and strong requirements.

| | Functional requirement (FR) | Non-functional requirement (NFR) |
|---|---|---|
| **Question** | What can the user do? | How fast, safe, available, scalable? |
| **Messaging example** | Send text and photos; see delivery ticks; receive notifications | Messages delivered within 2 seconds on 4G; end-to-end encryption; works at 100 million daily users; 99.95% availability |

### Main NFR categories (use as a checklist)

| Category | Question to ask |
|---|---|
| **Performance** | How fast must key actions be? (page load, search, checkout) |
| **Scalability** | How much growth and spikes must we handle? |
| **Availability and reliability** | Allowed downtime? What if a component fails? |
| **Security and privacy** | Who can access what? Encryption, consent, retention? |
| **Compliance** | Which laws and rules apply? (data protection, payments, accessibility) |
| **Monitoring and logging** | What must be measured and kept for audits? |
| **Extensibility** | How easily can we add features, partners, languages? |
| **Usability and accessibility** | Which devices, languages and accessibility standards? |

### Weak vs strong requirements

| Weak | Strong |
|---|---|
| "The app should be fast." | "Search results appear within 2 seconds at the 95th percentile on a 4G connection." |
| "Users can upload a photo." | "Users can upload a JPEG or PNG up to 10 MB; a progress bar shows; failures show a retry; the image is scanned for malware." |
| "The system should be secure." | "Passwords are hashed; sessions expire after 30 days of inactivity; admin access needs two-step login; all access is logged." |

Strong requirements are **specific, measurable, testable and tied to a user or business reason**.

## Technical trade-offs, build vs buy and architecture choices

Every technical choice trades one good thing for another. A PM does not pick the technology but must understand the trade-off and the product impact.

| Trade-off | What is in conflict | Questions to ask |
|---|---|---|
| **Speed vs accuracy** | Faster response vs a better answer | Is a good-enough answer in 1 second better than a perfect one in 10? |
| **Cost vs performance** | Lower bills vs a faster experience | What does each extra 100 ms cost and earn? |
| **Build vs buy** | Control and differentiation vs speed and maintenance | Is this core to our advantage? Total cost over 3 years? Exit options? |
| **Real-time vs delayed** | Instant updates vs simplicity and cost | Which screens truly need real-time? |
| **Security vs convenience** | More checks vs less friction | Where is the risk high enough to justify friction? |
| **MVP vs scale** | Ship quickly vs build for growth | What will break at 10x, and when will we need to fix it? |

### Build vs buy checklist

* **Build** when it is core to your differentiation, needs deep control, or vendors do not fit. Cost: team time, maintenance, security.
* **Buy** when it is a commodity (payments, maps, SMS, identity, analytics) and speed matters. Cost: fees, lock-in, data sharing, vendor risk.
* **Check:** uptime history, pricing at 10x volume, data export, privacy terms, support, and a fallback if the vendor fails.

### Monolith vs microservices (a delivery example)

A food-delivery product starts as a **monolith**: ordering, restaurants, payments and delivery in one codebase, simple and quick to build. As teams and traffic grow it splits into **microservices** (orders, restaurants, payments, tracking, notifications) that scale and release independently. The cost is complexity: more network calls, harder debugging, data consistency problems and more operations work. Split when team size, release speed or scale requires it, not before.

## Delivery management for PMs: sprint planning, backlog grooming and estimation

| Practice | Purpose | PM contribution |
|---|---|---|
| **Backlog grooming (refinement)** | Make upcoming work ready: clear, small, estimated, with acceptance criteria and dependencies | Write the problem and acceptance criteria; split large items; remove stale ones; flag dependencies |
| **Sprint planning** | Choose what the team commits to for the next 1 to 2 weeks | Bring ordered priorities and the sprint goal; accept that capacity is limited; protect time for bugs and tech debt |
| **Estimation** | Understand effort and uncertainty | Use ranges and confidence (story points or t-shirt sizes); ask what makes an item uncertain; do not treat an estimate as a promise |

**Estimation tips:** large items hide risk, so split them; consider testing, review, deployment, analytics and dependencies; build in a buffer; re-estimate when learning changes the picture.

**Sprint planning inputs and outputs:** inputs are the ordered backlog, team capacity, recent velocity and known dependencies; outputs are a sprint goal, a committed list and a plan for risks.

## Worked system cases for PMs

### Case 1: A referral flow

A user shares a code; a friend installs the app, signs up and completes a first action; both get a reward.

| Layer | What happens | PM decisions |
|---|---|---|
| **Frontend** | Share sheet, deep link, code entry | Where to put entry, how to explain the reward |
| **API and backend** | Validates the code, links friend to referrer, checks the reward rules | Eligibility, limits per user, fraud checks (same device, same payment method) |
| **Database** | Stores referral links and states (invited, installed, qualified, rewarded) | Retention of data; audit trail |
| **Third parties** | Attribution service, messaging, payments for payout | Vendor reliability; attribution gaps on some platforms |
| **Metrics** | Invites per user, invite-to-install, install-to-qualify, cost per referred user, fraud rate | Guardrails: reward abuse, support tickets |

Edge cases: the friend already has an account; the code is shared publicly; the referrer deletes their account; the reward fails to credit.

### Case 2: Payment succeeded but the restaurant never received the order

| Question | Answer pattern |
|---|---|
| What happened? | Payment confirmed, but the order message to the restaurant failed or was not acknowledged |
| What does the customer see? | "We are confirming your order with the restaurant" with a timer, never a silent success |
| What should the system do? | Retry the message, alert the restaurant by another channel (call or alternate app), re-route or cancel and **auto-refund** after a set time |
| What do we track? | Rate of unacknowledged orders, time to detect, refund rate, support contacts |
| What is the guardrail? | No double charge; clear status; the customer is notified at each change |

### Case 3: Delivery fails mid-journey

Design a **fallback ladder**: reassign to another delivery partner → offer a new ETA → offer a partial or full refund → compensate with a credit if the delay is large. Each step has a trigger (time threshold), a message, an owner (system, support, ops) and a metric (percentage resolved without a human). This keeps trust when the system fails.

## Practice brief: design a personalised learning recommendation system

!!! source "From your class deck (Week 9 assignment)"
    The brief asks for a recommendation system for an online education platform to improve engagement, completion and satisfaction for three personas (learners, instructors, platform admins), covering requirements, system design, trade-offs and assumptions. Use the outline below as a structure; write your own answers.

| Step | What to deliver |
|---|---|
| **1. Goals and personas** | Business goals (engagement, completion, satisfaction targets), needs of learners, instructors and admins |
| **2. Functional requirements and user stories** | "As a learner, I see recommended next courses based on my goals and progress" |
| **3. Non-functional requirements** | Performance, scalability, availability, compliance, security and data retention, monitoring and logging, extensibility; 1 or 2 per category, each measurable |
| **4. Core system design** | Frontend (web, mobile), backend (recommendation service, user profile service, catalogue), data stores, events and analytics, third-party integrations; draw a block diagram |
| **5. Trade-off analysis** | For example personalisation vs privacy, or accuracy vs latency: what conflicts, how you prioritise, your decision and why |
| **6. Assumptions and future work** | Data availability, cold-start approach, instructor controls, fairness checks, A/B testing plan, next improvements |
| **7. Deliverables** | A detailed PDF covering steps 1 to 6 and a short video walkthrough of your reasoning and trade-offs |

Write it in your own words; copying AI-generated solutions weakens your interview story.


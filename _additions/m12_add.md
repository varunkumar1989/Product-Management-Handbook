## From vibe coding to agentic coding and full-stack builds

!!! source "From your class deck (Week 11-12 · AI Systems in Action)"
    The sequence runs from vibe coding, to agentic coding (an AI agent plans, writes, runs and fixes code across files), to building a full-stack web app, then deploying it with free tools, and finally automating workflows and measuring the economics of AI systems. The live build is a small e-commerce store with customer and admin sides.

### How a website works (the stack in one view)

| Layer | Job | Typical choices |
|---|---|---|
| **Frontend** | Pages and interactions the user sees | A component framework, routing, a state store, responsive design |
| **Backend / API** | Business logic, validation, security | A server framework exposing REST endpoints |
| **Database** | Persistent data | A managed SQL database |
| **Hosting** | Where each part runs | Static hosting for the frontend, a service host for the backend |
| **Source control** | Safe history and collaboration | Git with a hosted repository |

### An end-to-end playbook (what to do, in order)

1. **Create accounts** for source control, a managed database/backend service, a backend host, a frontend host and an AI-powered coding editor; install the editor and a Git client first.
2. **Create a repository** for the project.
3. **Create the database project:** name it, choose a region close to users, use a strong password made of letters, numbers and underscores.
4. **Write one clear build prompt** that lists the frontend stack, backend stack, customer features (home, product list, product detail, cart, checkout, order confirmation), admin features (login, dashboard, product management, orders) and quality requirements: folder structure, error handling, input validation, loading states, README, health endpoints, environment validation, API docs, default admin credentials for local testing only, migrations, seed data, one-command database initialisation and seeding. State that no manual SQL should be required.
5. **Approve the agent's plan and changes** after reading them; do not accept blindly.
6. **Configure the backend environment** variables (port, database connection using the pooled connection string, SSL on, keys). **Never commit secrets** to the repository.
7. **Initialise the database** with the migration command, then **start the backend** and **start the frontend**; open the local address.
8. **Verify locally** with a customer path and an admin path; change default credentials.
9. **Commit and push** to the repository.
10. **Deploy the backend** to a service host: set the root folder, build and start commands and environment variables; check the health URL and a sample API route in the browser.
11. **Deploy the frontend** to a static host: set base directory, build command and publish folder; set the API base URL as an environment variable; if page refreshes show "not found", add a single-page-app redirect rule (all routes to the main page).
12. **Test in production** end to end, then monitor logs and costs.

!!! warning "A prototype is not a production system"
    Free tiers sleep or limit usage, default admin credentials are unsafe, and generated code needs review for authentication, input validation, payment handling and privacy. Treat this build as a learning project or a pilot until engineers harden it.

### Design essentials to give the agent

Point to platform design guidelines and component libraries so the agent builds familiar patterns (menus, actions, forms), and attach screenshots of apps you admire. Consistency and standard components make the result feel professional.

## Automation vs agents, layers of an AI system and workflow tools

| | Automation | Agent |
|---|---|---|
| **Behaviour** | Fixed steps | Decides what to do next |
| **Example** | Send a chat alert whenever a survey score is below 7 | Read the feedback, classify the topic and route it to the right team, deciding the destination |
| **Risk profile** | Predictable, easy to test | Flexible, needs guardrails and evaluation |

**Layers of an AI system:** interface (what users touch) → workflow (logic that sequences steps) → model or API (the AI) → data (forms, databases, documents) → infrastructure (cloud, accelerators) → monitoring (logs and dashboards). When something fails, locate the layer.

### Workflow automation concepts (node-based tools)

| Term | Meaning | Analogy |
|---|---|---|
| **Trigger** | The event that starts the workflow | "An event happens" |
| **Node / step** | One action in the flow | A task in a process |
| **Workflow** | The whole sequence | A process blueprint |
| **JSON** | Structured data passed between nodes (key-value pairs) | The note passed along |
| **API** | An application's interface | A waiter taking your order to the kitchen |
| **Webhook** | A system pushes an event to you | An announcement when your food is ready |

**Starter flow:** form response → sheet row → AI step (summarise and classify sentiment) → chat message to the product channel. **Practice builds:** competitor-analysis digest, feature-request tagger, lead or feature-request classifier that posts a notification and updates a backlog. Deliverable: a screenshot of the flow plus the prompt used.

## AI economics: token costs, margins and monetisation patterns

**Cost of an AI feature** = (input tokens × input price) + (output tokens × output price) + infrastructure (cloud, accelerators, storage) + people and tooling. Margins depend on usage volume, reuse (caching) and model choice.

!!! hypo "Worked example · a rough token budget (hypothetical prices)"
    Suppose a model costs about 5 per million input tokens and 15 per million output tokens (currency units are illustrative). A support answer using 3,000 input tokens and 400 output tokens costs 3,000 × 5 / 1,000,000 + 400 × 15 / 1,000,000 = 0.015 + 0.006 = 0.021 units. At 1 million answers a month, that is about 21,000 units before infrastructure and review costs. Check real prices; they change often and differ by model.

### Monetisation patterns for AI features

| Pattern | How it works | Example |
|---|---|---|
| **Add-on** | Paid extra on an existing plan | An AI writing assistant inside a notes or documents product |
| **Subscription** | Monthly fee for an AI-first product | A content-generation tool with templates |
| **Per action / outcome** | Charge per result | A support bot priced per resolved conversation (reported at around one dollar per resolution by one vendor; check current prices) |
| **Bundled / embedded** | Included free to raise stickiness | AI summaries inside a meeting or commerce platform |
| **Usage-based API** | Pay per token or call | Developer platforms |

**Copilot vs bundled:** a commonly quoted rule of thumb is to **charge separately if fewer than about 70% of users use the feature** (it is a premium for power users) and to **bundle it if more than about 70% use it** (it drives retention). Treat it as a heuristic and test.

### Cost-versus-value matrix

| | Low cost to serve | High cost to serve |
|---|---|---|
| **High value** | **Scale**: invest and promote | **Re-evaluate**: optimise cost or price it |
| **Low value** | **Ignore**: leave as is | **Kill**: remove or redesign |

## Evaluating AI systems for business value

**Automation is not impact; evaluation turns demos into products.** Evaluate to connect AI performance to business outcomes, detect drift, errors and waste, and justify ROI.

| Metric | How to test | PM action |
|---|---|---|
| **Accuracy** | Score 10 to 50 sample outputs against a reference | Tune prompt, retrieval or data |
| **Latency** | Measure average and p95 response time | Optimise steps, caching, model choice |
| **Cost** | Read token and infrastructure logs | Estimate cost per task and ROI |
| **Bias and fairness** | Compare results across segments | Document risks, add guardrails |
| **Hallucination** | Fact-check a sample against sources | Improve retrieval and instructions |
| **Containment / resolution** | Share of tasks solved without a human | Improve coverage; keep escalation easy |
| **User satisfaction** | CSAT after interactions | Fix weak journeys |

!!! example "Worked example · evaluating a support bot (hypothetical)"
    Metrics: **containment rate** (tickets the bot resolved), **CSAT** on bot-resolved tickets, and **cost per resolution**. If the bot resolves 55% of tickets at CSAT 4.3 and costs 0.4 per resolution versus 3 per human ticket, savings are clear, but also track **re-contact within 48 hours** to avoid counting unresolved chats as wins.

!!! source "Reported results are context, not proof"
    Vendor case studies (faster code completion, faster content generation) show direction, but your results depend on your tasks and users. Measure in your own product.

### Collaborating with AI and ML teams

* **Define inputs and outputs early** (what data goes in, what must come out, what counts as correct).
* **Share and version prompts** with engineers.
* **Co-track logs and cost** in one dashboard.
* Agree on an **evaluation set** and on what triggers a rollback.


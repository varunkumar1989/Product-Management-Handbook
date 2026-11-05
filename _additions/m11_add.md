## Why PMs need vibe coding, and how it differs from traditional coding

!!! source "From your class deck (Week 10-11 · Vibe Coding for PMs)"
    Traditional product building makes PMs wait weeks for design and engineering time, slows hypothesis testing and makes early visualisation hard. Vibe coding lets a PM build faster prototypes, communicate better with engineers and designers, test product logic before sprint planning and automate recurring PM tasks. The deck's workflow is **Prompt → Test → Refine**.

| Factor | Traditional coding | Vibe coding |
|---|---|---|
| **Language** | Programming syntax | Natural language |
| **Workflow** | Write → compile → debug | Describe → test → refine |
| **Users** | Engineers | Builders and PMs |
| **Goal** | Precision and robustness | Speed and exploration |
| **Output quality** | Reviewed, tested, maintainable | Fast prototype that needs review before production |

Key attitude: **aim for progress, not perfection.** The process is iterative; you fail fast and learn fast.

## The first prompt is the most important prompt

!!! source "From your class deck (Week 10-11)"
    The first prompt sets the direction, like the angle of a rocket launch: a small error early becomes a large one later. Treat it like a short PRD. The deck's recipe: a one-line overview, details of the core MVP functionality (including login, authentication and database at this stage), and style details with screenshots. Refine the prompt with a chat assistant first, and start over if the first result is not at least 60 to 70% of what you wanted.

### A recipe for the first prompt

1. **One-line overview:** what you are building and for whom.
2. **Core MVP functionality:** the main use case only; include login, user accounts and data storage if you need them.
3. **Style:** colours, tone, layout, and **screenshots** of apps you like.
4. **Success criteria:** "The app succeeds if the user can ___."

!!! tip "Refine before you build"
    Paste your first prompt into a chat assistant and ask: "Rewrite this prompt to be more concise and detailed." Then take the improved version to the builder tool.

### A basic first-prompt template

```
I need a [type of application] with [list of features]. It will be used by
[target audience] to solve [core problem]. It succeeds if the user can
[achieve X].
Start with the main page containing: [detailed page requirements].
Use a modern, clean, responsive design. Show clear loading, success and
error states, and confirmation messages. Use sample data for now.
```

### Working rules that save time and credits

| Rule | Why |
|---|---|
| **Give at most about three things per prompt** | AI makes more mistakes when asked to do many things at once |
| **Start with an MVP and iterate by version** | Easier to test and to understand what broke |
| **Revert to the previous version when stuck** | Faster than debugging a tangle |
| **Start over if the first result is under 60 to 70% right** | A better PRD and screenshots usually beat patching |
| **Save each prompt and result** | You learn what works and can reuse it |
| **Do not begin with a huge PRD** | Large, heavy prompts create bugs; build in slices |

### Where to find screenshots and inspiration

* Products similar to what you want: assistants for chat apps, large social products for feeds and profiles, forums for discussion layouts, and the builder tool's own interface for tools.
* Design galleries and component libraries (Dribbble, Behance, community component sites) for layouts, styles and components.
* Official design guidelines from platform makers for menus, actions and components.

## Live demo ideas, limits and PM use cases

Good first builds (idea → prompt → working app in minutes): a calculator, a task tracker, a weather fetcher that calls an external API, a meeting-notes organiser, a feature-prioritisation scorer.

| PM use case | What you can build |
|---|---|
| **Internal tool** | Meeting-notes organiser, decision log |
| **Dashboard** | Metrics from a spreadsheet |
| **Prototype** | An onboarding flow to test with users |
| **Automation** | Slack alerts, email reports |

### The limits of building with AI

* Limited control over backend logic and depth.
* Debugging complex systems is hard; you may not understand what the code does.
* Often missing version control, automated tests and security review.
* **Not production-grade by default:** treat output as a prototype until engineers review security, scale and compliance.

## Debugging mindset and reliable AI-built apps

!!! source "From your class deck (Week 10-11, Day 2)"
    AI mistakes are communication gaps. Do not rewrite everything: fix one issue at a time, ask the AI to explain its code, and iterate like a conversation. Best practices: save prompt versions, keep each prompt to one clear outcome, add acceptance criteria and test inputs after every major change.

| Problem | Likely cause | Fix |
|---|---|---|
| Code error | Missing context | Provide the error message, steps and the step-by-step logic you expect |
| Wrong output format | Vague instruction | Specify the exact format (columns, order, units) |
| Unexpected behaviour | Overloaded prompt | Break into sub-tasks; do one at a time |
| Slow or laggy app | Too many dependencies or heavy loops | Simplify the flow; ask the tool to optimise a specific part |
| Fix breaks another thing | No tests or versions | Revert; add acceptance criteria and test each change |

**Debug prompt template:** "When I [action] on [screen], I expect [result] but I get [result]. The console shows [error]. Explain the likely cause first, then propose a fix. Do not change anything else."

**Acceptance criteria examples:** "The total count updates immediately after adding an item", "An empty title shows an error and does not save", "Data is still there after refreshing the page".

## Give your app a memory: databases, APIs and connectors

!!! source "From your class deck (Week 10-11, Day 2)"
    The frontend shows data; the backend stores it. A managed backend service gives an instant database and login without writing SQL: define data like a spreadsheet. Apps connect to other apps through APIs (weather, saving tasks, updating a spreadsheet). The hands-on mini task: create a table, link it to the app and add and read entries.

| Concept | Plain meaning | Example |
|---|---|---|
| **Frontend** | What the user sees and clicks | A task list |
| **Backend** | Code and data behind the scenes | Saving the task |
| **Database table** | A spreadsheet-like store of records | Tasks: title, status, owner, created at |
| **Authentication** | Who is this user? | Email login |
| **API connector** | Your app calls another service | Weather data, a spreadsheet, a chat tool |
| **Secret / API key** | A password for a service | Keep on the server side, never in the front-end |

### Mini project: add memory to a notes app

1. Ask the builder to create a notes app with sample data.
2. Create a table (for example **Notes**: id, text, created_at, user).
3. Connect the app to the table with the tool's data connection feature.
4. Test: add a note, refresh, confirm it persists; add a second user and confirm they do not see each other's notes.
5. Add one API connector (for example a weather lookup or a spreadsheet export) and test failure messages.

You have just built a full-stack app without writing code. Next: security review, backups and a decision on whether it stays a prototype.

## Project ideas and how to show your skills in interviews

**Project ideas:** a feature-prioritisation dashboard; a team task notifier (chat tool plus database); a product-feedback summariser (spreadsheet plus an AI model); a release-notes generator; a meeting-actions tracker.

**Deliverable:** a working demo plus your **prompt documentation** (versions, what changed and why).

| Interviewers look for | How to show it |
|---|---|
| **Problem framing** | A one-paragraph problem statement and user; a clear first prompt |
| **Quality of prompts** | Structured prompts with acceptance criteria and examples |
| **Debugging logic** | A log of issues, causes and fixes; one rollback you made on purpose |
| **Product thinking** | Metrics, what you cut, what you would test next, and what engineers must harden |
| **Honest limits** | Security, scale and data privacy gaps you identified |


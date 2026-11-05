## Why PMs must understand LLMs, and how they predict the next word

!!! source "From your class deck (Week 10 · LLMs and RAG for PMs)"
    The deck's message: software can now understand natural language, so products move from "you search" to "it recommends" to "it collaborates". PMs bridge human needs and machine capabilities, so they need a simple mental model of how an LLM works (data → training → inference), the AI product landscape and the parts of an AI system.

**What is hard for people is often easy for AI, and the reverse.** Writing a poem about heartbreak is easy for a language model; counting chairs in a messy room from a camera is surprisingly hard. Knowing which tasks fit the technology is a core PM skill.

### The simplest accurate picture

* An LLM is a **giant statistical prediction machine**. Given the text so far, it predicts the most likely **next token**, adds it, and repeats.
* Example: "Where there's a will, there's a ..." The model assigns high probability to "way", lower to others. It outputs **probability, not truth**.
* It learns patterns of grammar, reasoning style, code, writing styles and many factual associations from huge text collections.
* **Temperature** controls randomness: low gives focused, repeatable answers; high gives more varied, creative answers.

### Neural network basics without the maths

| Idea | Plain meaning |
|---|---|
| **Neuron** | A small unit that takes numbers in, weighs them and passes a number on |
| **Weight** | How strongly one input influences the result (learned) |
| **Bias** | A learned offset that shifts the result up or down |
| **Parameters** | All the weights and biases together; modern LLMs have billions or more |
| **Training** | Show the model text, compare its prediction with the real next word, nudge the parameters to reduce the error, repeat billions of times (like learning to balance by falling and adjusting) |
| **Inference** | Using the trained model to answer new prompts |

!!! example "A tiny numeric picture"
    One neuron receives inputs 5 and 5 with weights 5 and 5, plus a bias of 10: 5×5 + 5×5 + 10 = 60. Change one weight and the output changes. An LLM does this across billions of numbers, which is why individual parameters cannot be read like rules.

## LLM vocabulary, tokens and embeddings you can try yourself

| Term | PM-friendly meaning |
|---|---|
| **Token** | A chunk of text (a word or part of a word) that the model processes; cost and limits are counted in tokens |
| **Parameter** | A learned number inside the model; more parameters usually means more capability and more cost |
| **Model** | The trained "brain" that predicts the next token given context |
| **Temperature** | Randomness setting |
| **Context window** | How much text the model can consider at once (the prompt, history and documents together) |
| **NLP** | Natural language processing: computers working with human language |

### How an LLM "reads" text

1. **Tokenisation:** "It is raining outside" is split into tokens and each gets an ID, for example [132, 234, 545, 678]. Try an online tokenizer to see how your text splits; non-English and code often use more tokens, which raises cost.
2. **Embeddings:** each token becomes a long list of numbers (a **vector**) that captures meaning. Words used in similar ways land close together: "king" near "emperor". Visual embedding explorers let you see clusters.
3. **Layers of processing** use these vectors to predict the next token.

### Common pitfalls to design around

| Pitfall | What it means | Product response |
|---|---|---|
| **Hallucination** | Confident but wrong output | Ground answers in sources (RAG), show citations, add review for risky tasks |
| **Bias** | The model reflects imbalances in its training data | Test across groups, add guardrails, keep humans in the loop for sensitive decisions |
| **Overfitting** | A model memorises its training data and performs poorly on new data (mostly a risk in fine-tuned or custom models) | Hold out test data, evaluate on realistic new examples |
| **Stale knowledge** | The model does not know recent events | Retrieval, browsing or regular updates |

## Prompt engineering for PMs: the quality ladder, PREP and CRISPE

!!! source "From your class deck (Week 10, Day 2)"
    A prompt is a creative brief, not a question. It carries role, context and constraints, and its quality depends on clarity and specificity. The deck shows a four-rung quality ladder (vague, clear, contextual, strategic), the **PREP** framework (Purpose, Requirements, Examples, Parameters), a six-part framework (Context, Role, Instruction, Specification, Performance, Example), tone switching, and the habit of iterating and testing.

### The prompt quality ladder

| Rung | Example | Why it improves |
|---|---|---|
| **Vague** | "Write about my product." | No audience, goal or format |
| **Clear** | "Describe my scheduling tool for remote teams." | Names the product and audience |
| **Contextual** | "Describe my scheduling tool for remote teams who struggle with handoffs between time zones." | Adds the pain point |
| **Strategic** | "Write three benefit-led taglines for a scheduling tool for async remote teams, each under 8 words, for a landing-page hero." | Adds goal, constraints and format |

### PREP

| Letter | Meaning | Example |
|---|---|---|
| **P**urpose | What deliverable, for what use | "Describe a new feature for our team app in a release note" |
| **R**equirements | Must-include points, audience, tone | "Focus on speed and teamwork; for busy managers" |
| **E**xamples | Show what good looks like | "Assign, track, and celebrate milestones, all in one view." |
| **P**arameters | Length, format, style limits | "Upbeat tone, three sentences maximum" |

### The six-part framework (CRISPE-style)

| Part | What you give | Example |
|---|---|---|
| **C**ontext | Who you are, the situation, goals, audience | "I'm a career coach writing short posts for aspiring PMs" |
| **R**ole | Who the AI should act as | "Act as a senior content strategist" |
| **I**nstruction | The task and why | "Write one post from this idea, built for high retention" |
| **S**pecification | Format, length, tone, must-haves | "Hook under 8 words; short sentences; no emojis; a closing question" |
| **P**erformance | Success criteria and what to avoid | "Scannable and engaging; avoid corporate tone and long paragraphs" |
| **E**xample | A sample of the style you want | One short sample post |

### Tone is a powerful parameter

The same description can be professional ("An assistant that drafts efficient, brand-correct emails in seconds"), playful ("Your cheeky inbox sidekick") or inspirational ("Communicate with clarity and purpose"). Generate three tones, test with real users or teammates, and keep a short **voice guide** for your brand.

### Iterate and test

1. Run the prompt on **5 to 10 realistic inputs**, not one.
2. Note failures (missed constraint, wrong tone, made-up facts).
3. Change **one thing at a time** and re-run.
4. Save versions and results; keep your best prompt and test set together.

## RAG for PMs: grounded answers and a mini product assistant

!!! source "From your class deck (Week 10)"
    RAG = retrieval plus generation: find relevant material first, then let the model answer using it. Benefits for PMs: consistent support answers from documentation, faster competitor and market research, instant internal knowledge retrieval. The deck's task: design a RAG flow that answers product questions from FAQs or documents and returns a clear answer in a chat tool or sheet.

| Scenario | Benefit of RAG |
|---|---|
| Support chatbot | Answers stay consistent with current policy documents |
| Product research | Faster synthesis of competitor pages and reports |
| Internal tools | Instant answers from wikis and past decisions |

**Simplified pipeline:** documents → split into chunks → embed and index → user question → find the most relevant chunks → build a prompt with the question and chunks → model answers with citations → log and evaluate.

!!! hypo "Worked design · a mini product assistant (hypothetical)"
    * **Input:** your FAQ, release notes and pricing page.
    * **Retrieval:** embed each section; for a question like "Does the Pro plan include export?" fetch the top 3 sections.
    * **Prompt:** "Answer only from the context. If the answer is not there, say you do not know and suggest contacting support. Cite section titles."
    * **Output:** a short answer plus source links, posted to a team chat channel.
    * **Evaluate:** 30 real questions; measure correct answers, "I don't know" correctness, citation accuracy and time saved.
    * **Risks:** outdated documents (re-index on change), private data (access controls), over-trusting answers (show sources).

## Designing a system prompt for a PRD-writing assistant

!!! source "From your class deck (Week 10 assignments)"
    One assignment asks for a reusable **system prompt** that makes a model act as an expert PM and writer of PRDs, specifying role, PRD structure, tone and depth, formatting, guardrails and clarifying-question behaviour, then using it to produce a PRD for a product of your choice. Prompt engineering is framed as **process design**. The second brief gives a hard product problem (detecting and handling fast-mobilising content on a social platform without becoming a censor) to be worked through with that system prompt.

### What a system prompt for a PRD writer should specify

| Element | What to write |
|---|---|
| **Role** | "You are a senior product manager with 10+ years in consumer and B2B products." |
| **Structure** | Problem statement; goals and non-goals; users and personas; user stories; scope and requirements; success metrics and guardrails; risks and dependencies; rollout plan; open questions |
| **Tone and depth** | Concise, plain language, business-facing; technical detail only when needed |
| **Formatting** | Headings, tables for metrics, numbered user stories, a one-paragraph summary at the top |
| **Guardrails** | Do not invent metrics or data; mark assumptions; flag missing information; include edge cases, privacy and abuse cases |
| **Clarifying behaviour** | Ask 3 to 5 scoping questions before drafting; if the user says "just draft", write with explicit assumptions listed |
| **Output checks** | Before finishing, check that every goal has a metric and every risk has a mitigation |

### A starter system prompt (adapt it)

```
You are a senior product manager who writes clear, testable PRDs.
Before drafting, ask 3-5 short questions about users, problem, goals,
constraints and timeline. If the user asks you to proceed, draft using
clearly labelled assumptions.
Structure: 1 Summary; 2 Problem and evidence; 3 Goals and non-goals;
4 Users and personas; 5 User stories with acceptance criteria;
6 Requirements (functional, non-functional); 7 Success metrics (primary,
secondary, guardrail) in a table; 8 Risks, dependencies and open questions;
9 Rollout plan and experiment design.
Rules: never invent data or metrics; mark unknowns as "Open question";
cover edge cases, privacy, abuse and failure states; keep sentences short.
```

### Approach to a hard product brief

For a prompt like the "fast-mobilising content" problem: define the harm precisely, list stakeholders (creators, viewers, regulators, moderators), set **signals** (velocity of sharing, unverified source, coordinated accounts) and **graduated responses** (labels, slowing reshare, human review) with clear lines against censorship, define metrics and guardrails (reach of verified content, false-positive rate, appeal outcomes), plan experiments and transparency reporting. Use AI to brainstorm, but make sure the final reasoning, structure and judgement are yours.


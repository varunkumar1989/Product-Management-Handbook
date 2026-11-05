---
id: aips
title: AI product sense (86 questions)
category: AI product sense
order: 9
summary: 86 AI product-sense questions across improvement, growth, launch, design, strategy, safety and metrics, each with an approach, model answer and 60-second version.
---

!!! source "About this question bank"
    The 86 prompts follow a widely shared community question bank of AI product-sense interview questions compiled by Aakash Gupta (Product Growth newsletter), grouped into seven themes. **The answers, approaches and mistakes lists are written by Varun Kumar for SkillNavora.** All company names are used only as familiar examples, and every number inside a question is a **hypothetical scenario figure**, not a claim about a real company. Treat the model answers as structures to adapt in your own words; interviewers reward reasoning, trade-offs and metrics, not memorised text.

!!! tip "How to answer any AI product-sense question"
    **Clarify** the goal and constraints (users, time, team, risk). **Diagnose** with data you would pull. **Choose** two or three levers and say what you would not do. **Design** the experience and the guardrails. **Measure** with a primary metric and guardrails. **Close** with risks and a sequencing plan.

## Product improvement

??? question "AIPI1 · Hard — ChatGPT image generation has 175M WAU. How would you get it to 350M in 3 months with 3 engineers?"
    **What it tests:** Growth thinking under a tight resource limit.

    **Approach:** Find the biggest lever: new-user reach, repeat use, or sharing. Pick two cheap, high-leverage bets.

    **Model answer:** “Assume the base is mostly people who already chat with the product. I would split WAU growth into (1) activation of existing chat users who never tried images, (2) resurrection of lapsed image users, and (3) sharing loops that bring new people. With 3 engineers I would do: an in-chat nudge that offers an image when a conversation naturally calls for one (greetings, birthdays, logos, slides); one-tap templates and style presets that remove the blank-prompt problem; and share links that open a ready-to-edit image with the prompt attached, so every shared picture is an acquisition ad. I would measure image-attempt rate per active user, first-image completion, shares per image and new users from shared links. Cut anything needing new model work. Doubling in three months is aggressive, so I would tell leadership the realistic range and what must be true for the top of it.”

    **Common mistakes:** Proposing new models or big features that three engineers cannot ship in a quarter.

    **60-second answer:** Existing users, lapsed users, sharing loops; nudge, templates, shareable edit links.

??? question "AIPI2 · Medium — Claude's code assistant has a 40% thumbs-down rate from non-technical users. You have 2 months and 5 engineers. What would you build?"
    **What it tests:** Segment-specific diagnosis and focus.

    **Approach:** Understand why non-technical users are unhappy before building; fix the experience for their job.

    **Model answer:** “I would first read a sample of 100 thumbs-down sessions with reasons. Likely causes: jargon-heavy answers, code they cannot run, missing context, and no way to check the result. Then I would design a mode for non-technical users: plain-language explanations, a 'run it for me' preview, step-by-step setup, safe defaults, and questions asked back when the request is vague. Add a quick reason picker on thumbs-down (too technical, did not work, wrong idea, too slow). Success is thumbs-down rate under 25%, task completion measured by 'did it run', and week-2 return. I would ship an explain-first template in month one and the guided run flow in month two, with evals built from the labelled failures.”

    **Common mistakes:** Treating all users alike; building before reading the failures.

    **60-second answer:** Diagnose with thumbs-down reasons, build a guided plain-language mode, measure task completion.

??? question "AIPI3 · Medium — Users spend 30 seconds with ChatGPT's 'thinking' feature, but 60% abandon before seeing results. How would you improve this?"
    **What it tests:** Latency and perceived-wait design.

    **Approach:** Reduce real wait, reduce perceived wait, reduce cost of leaving.

    **Model answer:** “Three levers. Real time: route easy questions to a faster path and show 'quick answer now, deeper answer in a moment'. Perceived time: show meaningful progress (what is being checked, partial reasoning summary, a first draft streaming), not a spinner. Cost of waiting: let the user keep chatting, get a notification when the deeper answer is ready, and save the result so leaving does not lose work. Instrument abandonment by second (when do they leave?), by question type, and by device. Target: abandonment under 30% without lowering answer quality. Test with an A/B on progress messaging first because it is cheapest.”

    **Common mistakes:** Only speeding up the model; ignoring perceived wait.

    **60-second answer:** Faster path, honest progress, background completion with notification; measure abandonment curve.

??? question "AIPI4 · Medium — Gemini's image generation is 50% slower than competitors. You can't change the model. What do you do?"
    **What it tests:** Product-layer solutions to a technical limit.

    **Approach:** Make slowness feel and matter less; match speed to need.

    **Model answer:** “Without touching the model I can still change the experience: stream low-resolution previews early and sharpen, so users see progress within a second; let users start several prompts in parallel; offer a fast draft mode and a quality mode; generate in the background and show results in a gallery; cache and reuse popular prompts; pre-compute style variants for common requests; and warm capacity at peak. I would also improve first-try success with prompt suggestions, since fewer retries reduce total waiting. Metrics: time to first visual, time to accepted image, abandonment during generation, and images per session.”

    **Common mistakes:** Telling users to wait; promising a model fix outside your control.

    **60-second answer:** Previews, parallel and background generation, draft vs quality modes, fewer retries.

??? question "AIPI5 · Hard — ChatGPT has a 25% hallucination rate on factual questions. You have 3 months. How do you reduce this without access to the research team?"
    **What it tests:** Product-level reliability levers.

    **Approach:** Ground, detect, show, and recover.

    **Model answer:** “At product level: route factual questions to retrieval or browsing with citations; require a source before stating specifics; add a self-check pass that flags unsupported claims and says 'I am not sure' instead; show sources inline and highlight low-confidence statements; offer a 'verify' action; and give users an easy report button feeding an eval set. Build an evaluation set of factual questions by domain, measure hallucination by type, and attack the biggest bucket first (dates, numbers, citations, recent events). Success is a falling rate on the eval set plus rising trust measures, not just fewer complaints. Be careful that abstaining too often hurts helpfulness, so track both.”

    **Common mistakes:** Promising zero hallucinations; ignoring the helpfulness cost of refusing.

    **60-second answer:** Ground with retrieval, require sources, flag uncertainty, evals by error type.

??? question "AIPI6 · Medium — Claude's context window is 200K tokens, but only 5% of users use more than 10K. How would you drive adoption of long-context features?"
    **What it tests:** Feature adoption and use-case discovery.

    **Approach:** Find jobs that need long context; make it effortless to bring in material.

    **Model answer:** “Users do not know what long context can do. I would identify jobs that benefit: summarising big documents, comparing contracts, analysing a code repository, reviewing meeting archives, research across many PDFs. Then reduce effort: drag-and-drop of folders, connectors to drives and repos, pre-built workflows ('compare these two contracts'), and examples shown in the empty state. Add guidance on cost and speed, and a clear indicator of how much context is used. Measure share of users who upload more than one document, sessions over 10K tokens, retention of those users and task success. Target segments first (legal, finance, research, engineering).”

    **Common mistakes:** Marketing the number of tokens instead of the jobs it solves.

    **60-second answer:** Jobs-led workflows, easy ingestion, templates, targeted segments.

??? question "AIPI7 · Hard — Anthropic wants to add image understanding to Claude. You have 6 months and a team of 8. What do you build?"
    **What it tests:** Scoping a new capability.

    **Approach:** Pick the top jobs, define MVP, plan phases and risks.

    **Model answer:** “I would start from jobs where images matter: reading screenshots and UI bugs, documents and charts, handwritten notes, product photos, receipts. Month 1 to 2: ship image upload in chat with reliable reading of text, charts and screenshots, plus clear limits (no identifying real people, privacy handling). Month 3 to 4: workflows for the top two jobs (for example chart-to-insight and screenshot-to-bug report) and API access. Month 5 to 6: polish, evals, accessibility, mobile capture, and enterprise controls. Evals cover accuracy on charts and OCR, safety on sensitive images, and latency. Metrics: share of users sending images, task success, repeat use, API adoption. Risks: privacy, misuse, hallucinated details; mitigate with guardrails and uncertainty language.”

    **Common mistakes:** Building everything at once; ignoring safety and evaluation.

    **60-second answer:** Jobs first, MVP with reading screenshots and charts, workflows next, evals and safety throughout.

??? question "AIPI8 · Medium — ChatGPT voice mode has 80M MAU but only 20M WAU. How would you increase weekly usage?"
    **What it tests:** Habit formation and use-case fit.

    **Approach:** Find the moments voice is better than typing and build triggers for them.

    **Model answer:** “Voice wins when hands or eyes are busy or speaking is faster: driving, cooking, walking, learning languages, brainstorming. A 25% weekly ratio suggests many people tried it but have no habit. I would learn the top use cases from sessions, then build triggers and surfaces: a lock-screen or widget shortcut, car integrations, routines ('daily briefing', 'practice a language for 5 minutes'), smarter wake-up by context, and better interruption handling and speed. Add gentle reminders tied to the user's own use pattern. Metrics: weekly active ratio, sessions per week, session length, and retention of users who adopt a routine.”

    **Common mistakes:** Generic push notifications; ignoring that voice has specific contexts.

    **60-second answer:** Find contexts, add shortcuts and routines, improve latency, measure weekly ratio.

??? question "AIPI9 · Medium — Your AI writing assistant has 10M users but only 500K pay for premium. How would you 3x paid conversions in Q4?"
    **What it tests:** Monetisation analysis.

    **Approach:** Diagnose the funnel, fix value moments and paywall, test pricing.

    **Model answer:** “Today's rate is 5%. I would find who converts (profession, usage pattern, features) and where free users hit friction. Quick wins: move the paywall to moments of proven value (after a successful rewrite, at a word or credit limit), improve premium previews so users feel the benefit, add annual and student plans, offer team plans for workplaces, and send lifecycle emails to heavy free users. Test price points and trial lengths. Guard against hurting free retention and word of mouth. Target 15% paid uplift per test, tracked by cohort, with revenue and churn as outcome metrics. Three times in a quarter is ambitious, so set milestones and say which levers are most likely.”

    **Common mistakes:** Cutting the free tier harshly; changing price without testing.

    **60-second answer:** Segment converters, paywall at value moments, plans and trials, test and watch churn.

??? question "AIPI10 · Medium — Users iterate on AI-generated content 1.2 times on average. How would you increase it to 4+ iterations?"
    **What it tests:** Engagement quality.

    **Approach:** Ask whether more iterations is actually good; then improve the refinement loop.

    **Model answer:** “First check that iteration is a good goal: more iterations could mean poor first results. I would define success as final-output acceptance and time to a good result. Then make refinement easy and rewarding: one-tap refinements (shorter, warmer, add example), suggested next edits, side-by-side versions with history, inline editing, and a 'make it more like this' reference. Show what changed. Measure iteration depth alongside acceptance, saved or exported outputs and satisfaction. If acceptance falls while iterations rise, I would rethink the target.”

    **Common mistakes:** Chasing iteration count without checking quality.

    **60-second answer:** Define good outcome, make refinement one-tap, suggest next edits, track acceptance.

??? question "AIPI11 · Hard — Your AI code assistant has a 60% activation rate but 70% week-1 churn. You have 8 weeks. What's your plan?"
    **What it tests:** Retention diagnosis.

    **Approach:** Understand why activated users leave; fix the first-week value loop.

    **Model answer:** “Activated users tried it but left, so value was not sustained. Weeks 1 to 2: analyse cohorts by what they did and by language and editor, interview churned users, and read sessions around the last use. Likely causes: wrong or slow suggestions, setup friction, trust issues, no new use cases beyond autocomplete. Weeks 3 to 6: ship fixes for the top two causes (for example faster suggestions with better context from the repo, an onboarding checklist that teaches three high-value workflows, and in-editor tips). Weeks 7 to 8: test improvements with a holdout and lifecycle messages for day 2, 4 and 6. Success: week-1 churn under 55% and increase in days used per week.”

    **Common mistakes:** Adding features before understanding why users left.

    **60-second answer:** Cohort and interview diagnosis; fix quality and onboarding; test with holdout.

??? question "AIPI12 · Medium — Google Search is adding AI summaries, but users scroll past them. How would you increase engagement?"
    **What it tests:** Product-market fit inside an existing surface.

    **Approach:** Understand when summaries are helpful; improve relevance, trust and placement.

    **Model answer:** “Users scroll past when the summary is irrelevant, untrustworthy or slower than the first result. I would segment query types: where summaries help (how-to, comparisons, definitions) and where they do not (navigational, shopping). Show summaries only when confidence and usefulness are high, with visible sources, expandable detail, and follow-up questions. Test placement and length. Metrics: summary engagement, query reformulation rate, successful-session rate, ad and publisher outcomes, and satisfaction. Remember the business tension with link traffic and ads, so balance engagement with ecosystem health.”

    **Common mistakes:** Forcing summaries on every query; ignoring publishers and ads.

    **60-second answer:** Show when useful and trusted, add sources and follow-ups, measure successful sessions.

??? question "AIPI13 · Medium — Your AI meeting assistant transcribes perfectly, but users only review 10% of transcripts. How would you increase utility?"
    **What it tests:** Moving from output to outcome.

    **Approach:** Users do not want transcripts; they want decisions, actions and answers.

    **Model answer:** “Transcripts are raw data. Utility comes from summaries, action items, decisions and follow-ups delivered where people work. I would generate a short recap with owners and deadlines, push action items to task tools and chat, send a post-meeting email, allow questions across past meetings, and highlight moments relevant to each person. Measure share of meetings where recaps are opened, actions created and completed, search usage and weekly active users. Ask for one-tap corrections to improve trust. Review of transcripts matters less than follow-through.”

    **Common mistakes:** Improving transcription accuracy when accuracy is already high.

    **60-second answer:** Recap, action items, integrations, ask-across-meetings; measure follow-through.

??? question "AIPI14 · Hard — Midjourney generates better images than DALL-E, but you have ChatGPT's distribution. How do you compete?"
    **What it tests:** Strategy with distribution advantage.

    **Approach:** Compete where distribution beats raw quality; close the gap where it matters.

    **Model answer:** “Distribution means most users meet image generation inside a chat they already use, with no new account. I would compete on workflow rather than pure image quality: conversation-based iteration ('make the sky darker'), editing existing images, brand and character consistency, integration with documents and slides, and speed. Segment users: casual creators care about convenience, professionals care about control and quality. For professionals I would improve quality with style controls and reference images, accepting I may not win them fully. Measure share of image tasks done in-chat, retention versus standalone tools, and conversion of image users to paid. Be honest about what quality gap is acceptable.”

    **Common mistakes:** Claiming quality parity; ignoring convenience as a real advantage.

    **60-second answer:** Win on convenience and workflow, close quality gap for pros with controls, track in-chat share.

??? question "AIPI15 · Medium — Your AI tutoring app has great learning outcomes but only 15% retention after 2 weeks. What would you build?"
    **What it tests:** Habit design for education.

    **Approach:** Outcomes are good, so the problem is motivation and routine.

    **Model answer:** “Learning is effortful, so I would build motivation and routine: a clear goal and plan, daily short sessions, streaks and progress visuals, reminders at the learner's chosen time, quick wins early, social or parent accountability, and a weekly summary of progress for learners and parents. Make the next step obvious on return. Test goal setting during onboarding and a 5-minute daily mode. Measure day-7 and day-14 retention, sessions per week, and learning outcomes to ensure habit features do not dilute learning.”

    **Common mistakes:** Adding gamification that distracts from learning.

    **60-second answer:** Goals, short daily sessions, reminders, progress; protect outcomes.

??? question "AIPI16 · Medium — ChatGPT's mobile app has half the engagement of web. You have 1 designer and 3 engineers. What do you prioritize?"
    **What it tests:** Platform-specific prioritisation.

    **Approach:** Find mobile-specific friction and strengths.

    **Model answer:** “Mobile has different jobs: quick questions, voice, photos, on-the-go tasks. Gaps are often keyboard friction, long answers on small screens, slower loads and weaker multi-step work. I would prioritise: faster launch and response, voice and camera as first-class entry points, widgets and shortcuts, concise answer formats and better copy, share and handoff to web for heavy tasks. Instrument session starts, time to first prompt and drop-offs by screen. With a small team, pick two bets for 8 weeks, ship, measure, and iterate.”

    **Common mistakes:** Copying the web layout to mobile.

    **60-second answer:** Mobile jobs first: speed, voice, camera, shortcuts; measure time to first prompt.

??? question "AIPI17 · Hard — Enterprise customers want Claude to remember company context across conversations. You have 4 months. How do you build this?"
    **What it tests:** Enterprise memory and trust.

    **Approach:** Scope memory, control, security, and phased delivery.

    **Model answer:** “Enterprise memory means company knowledge, not personal chat history. Phase 1 (month 1 to 2): admin-managed knowledge sources (documents, wiki, tickets) with retrieval and citations, per-team spaces and permissions. Phase 2 (month 3): project-level memory of decisions and preferences that users can view, edit and delete. Phase 3 (month 4): audit logs, retention policy, data residency options, and analytics. Principles: least privilege, no cross-customer leakage, no training on customer data, clear visibility of what is remembered. Evals: retrieval accuracy, permission leaks (must be zero), freshness. Metrics: weekly active teams, answers with citations used, security review pass rate.”

    **Common mistakes:** Treating memory as a feature without permissions and governance.

    **60-second answer:** Knowledge connectors, project memory with controls, audit and retention; zero-leak evals.

??? question "AIPI18 · Medium — Your AI translation tool is 95% accurate, but users don't trust it for important documents. How do you build trust?"
    **What it tests:** Trust design for AI.

    **Approach:** Trust needs evidence, control and recovery, not a better number.

    **Model answer:** “Users judge risk, not average accuracy. I would show what is uncertain (highlight low-confidence phrases), offer glossary and terminology control, side-by-side original and translation with alignment, back-translation checks, and a human review option for critical documents. Provide certification or reviewer marketplace for legal and medical use. Share quality evidence by domain, not a single number. Track document types where users abandon, re-translation requests, review uptake and satisfaction for important documents.”

    **Common mistakes:** Quoting accuracy; no way to verify or escalate.

    **60-second answer:** Show uncertainty, enable verification, offer human review, publish domain-level evidence.

## Product growth

??? question "AIPG1 · Hard — Claude has 50M MAU. How would you get to 100M in 6 months without increasing the research team?"
    **What it tests:** Growth model decomposition.

    **Approach:** Split into acquisition, activation and retention; use distribution and product levers, not research.

    **Model answer:** “Doubling in six months needs about 12% monthly growth. I would model sources: new users (organic, referral, partnerships), reactivation, and reduced churn. Levers that need no research headcount: partnerships and integrations (browsers, phones, productivity suites, education), shareable outputs and artifacts that bring people in, templates for the top ten jobs to improve activation, student and team programmes, localisation for large markets, and lifecycle messaging for dormant users. Prioritise by size and speed, run experiments weekly, and watch quality and cost so growth does not degrade the product. I would give a range and name the two bets that carry most of the upside.”

    **Common mistakes:** Listing tactics without a growth model.

    **60-second answer:** 12% monthly growth; partnerships, shareable outputs, templates, localisation, reactivation.

??? question "AIPG2 · Hard — Your AI code assistant has 5M developers. GitHub Copilot has 50M. How do you compete with 1/10th the budget?"
    **What it tests:** Competitive strategy under constraints.

    **Approach:** Pick a wedge where you can win; avoid fighting on their strengths.

    **Model answer:** “I would not compete on breadth or distribution. Choose a wedge: a segment with unmet needs (for example large legacy codebases, a specific language or framework, security-sensitive teams, or agentic multi-file workflows), best quality and trust in that wedge, and word-of-mouth through developer communities and open-source maintainers. Offer superior context handling, transparent pricing, and integration with tools they already use. Grow through bottom-up adoption with a team plan, then enterprise. Measure retention, weekly active developers in the wedge, NPS and expansion within teams.”

    **Common mistakes:** Trying to match features and spend.

    **60-second answer:** Pick a wedge, win trust and quality there, grow bottom-up, then expand.

??? question "AIPG3 · Hard — ChatGPT has 800M MAU but a 20% DAU/MAU ratio. How would you double daily usage in one quarter?"
    **What it tests:** Habit and frequency.

    **Approach:** Understand why most users are occasional; create daily use cases.

    **Model answer:** “A 20% ratio means most users come a few times a month. Doubling is a big ask, so I would find high-frequency jobs (writing, coding, study help, planning, quick answers) and build daily triggers: morning briefings, tasks and reminders, memory that makes the product more personal, integrations into calendars and email, widgets and voice shortcuts, and notifications when long tasks finish. Target segments with natural daily need (students, professionals). Measure DAU/MAU by cohort and use case, sessions per user and retention. Honestly, the goal may be a smaller uplift in one quarter; I would set a target range and sequence experiments.”

    **Common mistakes:** Spamming notifications.

    **60-second answer:** Find daily jobs, add routines, memory and integrations; measure DAU/MAU by use case.

??? question "AIPG4 · Hard — You're launching an AI image generator in a market dominated by Midjourney. What's your GTM strategy?"
    **What it tests:** Go-to-market against an entrenched leader.

    **Approach:** Pick a segment, a differentiator and a channel.

    **Model answer:** “Choose a differentiated position, not a generic 'better images'. Options: ease for non-designers (inside tools people already use), commercial-safe licensed training for brands, consistency across characters and campaigns, or speed and price. Target a specific segment such as marketers or e-commerce sellers. Go-to-market: integrate into tools they use (slides, design apps, store builders), offer templates for their jobs, partner with agencies, and use showcase communities. Free credits to try, team plans to convert. Measure activation (first usable image), weekly use, paid conversion and share of outputs used in published work.”

    **Common mistakes:** Competing on quality claims alone.

    **60-second answer:** Segment plus differentiator plus channel; integrations, templates, trial credits.

??? question "AIPG5 · Hard — Your AI writing assistant has 100K users. Grammarly has 30M. How do you get to 1M users in 6 months?"
    **What it tests:** Scale-up from small base against an incumbent.

    **Approach:** Find a growth loop and a segment the incumbent serves poorly.

    **Model answer:** “10x in six months needs a loop, not just ads. I would target a niche where generic grammar help is not enough (academic writing, sales emails, fiction, non-native English professionals) and build a shareable output or collaboration loop (documents shared with reviewers, citations, templates). Add distribution through browser extensions, integrations with email and docs, creators and communities, and campus programmes. Optimise onboarding to reach a first win in two minutes. Track activation, week-4 retention, referral rate and cost per activated user. If retention is weak, fix it before scaling acquisition.”

    **Common mistakes:** Buying growth with poor retention.

    **60-second answer:** Niche plus loop; extensions, integrations, creators; fix retention first.

??? question "AIPG6 · Hard — Perplexity has grown to 10M MAU in 2 years. You're building an AI search competitor. What's your growth strategy?"
    **What it tests:** Entering a competitive category.

    **Approach:** Differentiate by job, vertical or trust; use distribution wedges.

    **Model answer:** “General search is dominated by incumbents. I would pick a vertical or job where AI answers beat links: research, shopping, travel, finance or health information with trusted sources. Differentiators: transparent sourcing, depth, freshness, and workflow (save, export, collaborate). Growth: browser default and extension, shareable answer pages that rank in search, partnerships with publishers and creators, and communities of professionals. Measure answer satisfaction, return rate, queries per user and citation click-through. Monitor cost per query because search at scale is expensive.”

    **Common mistakes:** A 'better answers' pitch with no wedge.

    **60-second answer:** Vertical wedge, trusted sources, shareable answer pages, extension, watch cost per query.

??? question "AIPG7 · Medium — Your AI productivity tool has a 2% viral coefficient. How would you get to 1.0+ in 3 months?"
    **What it tests:** Understanding virality.

    **Approach:** Viral coefficient = invites per user x conversion. Improve both and the product's shareable moments.

    **Model answer:** “A coefficient of 1.0 means each user brings one new user, which is very hard. I would map the loop: when does a user share, how many people see it, how many convert? Increase invites per user by building collaboration (shared workspaces, shared outputs), and increase conversion by making the invited experience excellent (landing page with context, no signup friction). Add rewards where value-aligned. Realistically I would aim for a meaningful increase (say from 0.02 to 0.2) and combine virality with paid and partnership channels, and I would say honestly that 1.0 is rarely reached. Track invites sent, accepted, activated and time to second use.”

    **Common mistakes:** Promising 1.0; adding generic referral bonuses without a natural shared moment.

    **60-second answer:** Map the loop, add collaboration and shareable output, optimise invitee conversion, set realistic target.

??? question "AIPG8 · Hard — ChatGPT Plus has 10M subscribers at $20/month. You're building Claude Pro. How do you get to 5M subscribers?"
    **What it tests:** Subscription growth strategy.

    **Approach:** Define target users, value gap, conversion funnel, and constraints.

    **Model answer:** “Reaching half of a leader's paid base needs a clear reason to pay. I would identify segments with strong willingness to pay (developers, writers, analysts, students) and give them value that is hard to match: long context, strong writing and coding, projects with persistent knowledge, and reliable limits. Improve free-to-paid conversion with usage limits at value moments, trials, annual and team plans, and workplace purchases. Expand distribution through partnerships and integrations. Estimate the funnel: free users x conversion rate; 5M paid at 5% conversion requires 100M monthly free users, so growth and conversion both matter. Track conversion, churn and revenue per user.”

    **Common mistakes:** Ignoring the free-user base needed for the target.

    **60-second answer:** Segments with willingness to pay, differentiated value, conversion funnel math.

??? question "AIPG9 · Medium — Your free AI product has great retention but 99% never convert to paid. How do you increase paid conversion?"
    **What it tests:** Monetisation of retained users.

    **Approach:** Find why free is enough; create a paid tier worth paying for.

    **Model answer:** “High retention means value exists; the paid tier does not add enough or is gated badly. I would identify power users and what they do, interview users who hit limits, and design premium value for them: higher limits, advanced models or features, collaboration, history and exports, priority speed, and integrations. Place the upgrade at value moments rather than blocking early use. Test pricing, trials and annual plans. Watch free-user experience, since over-gating hurts retention. Target segments such as professionals and teams first. Metrics: conversion by segment, revenue per user, churn and impact on retention.”

    **Common mistakes:** Paywalling core value early.

    **60-second answer:** Segment power users, premium features, upgrade at value moments, test pricing.

??? question "AIPG10 · Medium — An AI health app has 1M downloads, but 80% never complete onboarding. You have 6 weeks to fix activation."
    **What it tests:** Onboarding funnel diagnosis.

    **Approach:** Measure each step; reduce friction; deliver value earlier.

    **Model answer:** “Week 1: instrument the funnel step by step and watch sessions to see where people stop (permissions, long forms, sensitive questions, account creation). Week 2 to 4: shorten and reorder: show value first (a quick insight or plan), ask only what is needed, explain why sensitive data is requested, allow skip and later completion, and add progress indicators and trust signals (privacy, credentials). Test variants. Week 5 to 6: roll out winners and add reminders for incomplete onboarding. Success: completion from 20% to 40%, plus quality of activation (first meaningful action). For health, keep safety and privacy high.”

    **Common mistakes:** Cutting questions that are needed for safe advice.

    **60-second answer:** Funnel diagnosis, value before asks, trust signals, experiments, reminders.

??? question "AIPG11 · Medium — Your AI meeting assistant has 500K users but only 50K use it weekly. How would you increase weekly active usage?"
    **What it tests:** Frequency and habit.

    **Approach:** Make usage automatic and outcomes visible.

    **Model answer:** “Weekly use falls when users must remember to start the tool. I would automate: connect to calendars and join meetings by default, deliver recaps and action items automatically to email and chat, and send weekly digests across meetings. Add team features so colleagues rely on it, search across past meetings, and manager views. Learn from the 10% who are active: what workflow do they use? Build onboarding around that. Metrics: share of meetings recorded, recap opens, actions created, weekly active ratio.”

    **Common mistakes:** More features rather than automation.

    **60-second answer:** Auto-join, auto-deliver recaps, team features; copy what active users do.

??? question "AIPG12 · Hard — You're launching an AI tutoring app against Khan Academy and Duolingo. What's your differentiation strategy?"
    **What it tests:** Positioning against strong incumbents.

    **Approach:** Choose a specific learner and outcome; use AI where it creates a clear advantage.

    **Model answer:** “Incumbents have content, brand and habit loops. Differentiate with personalised one-to-one tutoring that adapts to a learner's gaps, explains in their own words, handles any question, and supports exam goals (for example board exams, entrance tests, job interviews) in local languages. Trust matters: accuracy checks, teacher and parent views, and safety for minors. Start with one subject and market, prove learning outcomes, then expand. Metrics: learning gain, weekly active learners, retention and referrals from parents and teachers.”

    **Common mistakes:** Promising to replace teachers; ignoring accuracy and safety.

    **60-second answer:** Specific learner and exam goal, adaptive tutoring, local language, outcomes proof.

??? question "AIPG13 · Hard — Your AI design tool has PMF with designers but wants to expand to marketers. How do you grow into this segment?"
    **What it tests:** Segment expansion.

    **Approach:** Understand marketer jobs; adapt product, messaging and channels.

    **Model answer:** “Marketers need speed, brand consistency, templates and collaboration, not pixel control. Research their top jobs (social posts, ads, landing pages, campaigns). Build templates, brand kits, one-click resizing, approvals, scheduling integrations and analytics links. Change messaging to outcomes (more content in less time). Channels: marketing communities, agencies, integrations with ad and email tools, and partnerships. Beware of confusing the core designer experience. Run a pilot with 20 teams, measure activation (first campaign asset published), team seats and retention.”

    **Common mistakes:** Marketing the designer product unchanged.

    **60-second answer:** Learn marketer jobs, add templates and brand kits, outcome messaging, pilot.

??? question "AIPG14 · Hard — ChatGPT's growth plateaued at 800M MAU. You need to find 200M new users. Where do they come from?"
    **What it tests:** Market sizing and growth vectors.

    **Approach:** Identify under-penetrated segments and barriers.

    **Model answer:** “Think by barrier: awareness, access, language, usefulness and trust. Candidates: non-English and emerging markets (local languages, lighter apps, cheaper plans, voice), older adults and non-tech workers (simple use cases), students and schools, workplaces where tools are blocked (enterprise offerings), and devices and operating system integrations. For each, estimate the size and conversion barrier, and pick two or three bets. Measure reach, activation and retention per segment, and watch quality and cost of serving at scale.”

    **Common mistakes:** Assuming the same users will use it more instead of finding new groups.

    **60-second answer:** Segments by barrier: language, access, age, enterprise, devices; size and prioritise.

??? question "AIPG15 · Hard — Your AI customer support tool has 10% of the market. Zendesk is adding AI features. How do you defend and grow?"
    **What it tests:** Defending against incumbents.

    **Approach:** Differentiate on outcomes and depth; lock in via integration and data.

    **Model answer:** “Incumbents bundle AI. Defend by being clearly better at resolution quality, not feature count: measurable automation rates, accuracy with citations, handoff quality, multilingual support and fast setup. Deepen integrations with order, billing and CRM systems so the AI can act, not just answer. Provide analytics that tie support to revenue and retention. Pricing aligned to outcomes (per resolution). Grow with case studies and vertical templates. Build switching cost through data, workflows and trust, not lock-in tactics. Watch churn and win rates versus the incumbent.”

    **Common mistakes:** Competing only on price.

    **60-second answer:** Outcome quality, actions via integrations, analytics, outcome pricing.

??? question "AIPG16 · Hard — You're building an enterprise AI product. How do you grow from 10 customers to 100 in one year?"
    **What it tests:** Enterprise sales and product-led motion.

    **Approach:** Repeatable ICP, proof, pipeline and delivery capacity.

    **Model answer:** “Define the ideal customer profile from the best of the 10: industry, size, use case and buyer. Package a repeatable offer with a clear ROI story and a 30-day pilot. Build proof: case studies, references, benchmark results. Channels: outbound to the ICP, partners and system integrators, marketplaces, and community. Ensure onboarding and support can scale (templates, security documentation, self-serve admin). Track pipeline, pilot to contract conversion, time to value, expansion and churn. Adding ten customers a month needs a funnel of qualified opportunities; plan capacity so quality does not collapse.”

    **Common mistakes:** Custom work for every customer.

    **60-second answer:** ICP, repeatable pilot and ROI proof, partners, scalable onboarding.

## Product launch

??? question "AIPL1 · Hard — OpenAI wants to build an AI scheduling assistant. You have 8 months and a team of 10. What do you build?"
    **What it tests:** 0-to-1 product scoping.

    **Approach:** Define user and job, MVP, phases, risks and success metrics.

    **Model answer:** “Start with a user: busy professionals coordinating meetings across calendars and time zones. Jobs: find a time, handle conflicts, protect focus time, and reschedule. MVP (months 1 to 3): connect calendars, propose times by email or chat, respect preferences, and ask before acting. Months 4 to 6: negotiation with external guests, travel and buffer awareness, team availability. Months 7 to 8: scale, admin controls, analytics. Principles: user approval for changes, transparent reasoning, privacy of calendar data. Metrics: scheduling success without back-and-forth, time saved, weekly active users, trust (undo rate). Risks: errors causing missed meetings, privacy, integration breadth.”

    **Common mistakes:** Building everything at once; no approval controls.

    **60-second answer:** Focused MVP with approval, grow to negotiation, track success and undo rate.

??? question "AIPL2 · Hard — Anthropic wants to compete with Cursor for AI code editors. What's your product strategy?"
    **What it tests:** Competitive product strategy.

    **Approach:** Find the wedge, advantages and sequencing.

    **Model answer:** “Competitors win on editor experience and speed. A strategic angle: lean on model strengths in long context and reasoning for large repositories, agentic multi-file changes with strong review and safety, and deep integration with existing editors and terminals instead of forcing a new editor. Start with developers who value reliability on big codebases. Features: repo understanding, test-driven edits, clear diffs, permissions, team policies. Distribution: bottom-up developer adoption, enterprise security. Metrics: accepted changes, task completion, weekly active developers, retention and team expansion.”

    **Common mistakes:** Copying the editor feature by feature.

    **60-second answer:** Wedge on big codebases and agentic reliability; integrate rather than replace; measure accepted changes.

??? question "AIPL3 · Medium — You're launching an AI meeting assistant in a market with Otter, Fireflies, and Grain. How do you differentiate?"
    **What it tests:** Crowded-market positioning.

    **Approach:** Choose a segment, a unique outcome and a channel.

    **Model answer:** “Transcription is a commodity. Differentiate on outcomes and a segment: for example sales teams (CRM updates and coaching), product teams (decisions and tasks into planning tools), or healthcare and legal (compliance). Add privacy and compliance features, accuracy with domain vocabulary, and automation of follow-ups. Channel: integrations and marketplaces plus vertical communities. Measure activation (first useful recap), recurring use, and workflow completions (CRM updated, tasks created).”

    **Common mistakes:** Pitching better transcription.

    **60-second answer:** Pick a segment and outcome, integrate follow-up workflows, add compliance.

??? question "AIPL4 · Medium — Google wants to add AI features to Gmail. You have 6 months for v1. What do you ship?"
    **What it tests:** Feature prioritisation for a huge-scale product.

    **Approach:** High-frequency jobs, low risk, high trust, rollout safety.

    **Model answer:** “Pick jobs people do daily: summarise long threads, draft and polish replies, extract actions and dates, search in natural language, and triage. v1 should be assistive, not autonomous: drafts that users edit and send, with clear controls. Roll out gradually to opted-in users, with privacy promises (no training on personal emails without consent), enterprise admin controls and an easy off switch. Evals: tone, accuracy of summaries, safety. Metrics: adoption, edit rate of drafts, time saved, satisfaction and complaints.”

    **Common mistakes:** Auto-sending emails; ignoring privacy.

    **60-second answer:** Thread summaries, drafts, search, actions; opt-in, privacy and admin controls.

??? question "AIPL5 · Hard — Design an AI-powered search product for e-commerce that could challenge Google Shopping."
    **What it tests:** Product concept with marketplace dynamics.

    **Approach:** Use AI where search fails: intent, comparison and trust. Address supply and distribution.

    **Model answer:** “Shoppers struggle with vague intent, comparison and trust. An AI shopping search could understand natural requests ('a gift for a runner under 3,000'), ask clarifying questions, compare products with sources, combine reviews and price history, and explain trade-offs. Supply: partner with retailers via feeds and affiliate links, keep prices and stock fresh. Trust: transparent ranking, labelled ads, authentic reviews. Challenges: product data quality, sponsored placement, distribution. Start with a category (electronics) and a trusted brand angle. Metrics: successful purchase sessions, return rate, revenue per session, and trust ratings.”

    **Common mistakes:** Ignoring data supply and monetisation conflicts.

    **60-second answer:** Intent understanding, comparison, trust; start in one category; partner for data.

??? question "AIPL6 · Medium — You're building an AI tutoring product for high school students. What's your MVP and launch strategy?"
    **What it tests:** MVP definition in education.

    **Approach:** One subject, one goal, proof of learning, safety.

    **Model answer:** “MVP: one subject (for example maths) and one exam goal. Core: diagnostic test to find gaps, step-by-step guided practice rather than just answers, explanations in plain language, and progress tracking. Safety: age-appropriate content, no personal data collection beyond need, parental visibility. Launch: pilot with a few schools or tutoring centres, collect learning gains, then open to students with parent involvement. Metrics: improvement on pre/post tests, sessions per week, retention, and parent satisfaction. Pricing later, after proving outcomes.”

    **Common mistakes:** Giving answers without teaching.

    **60-second answer:** One subject, diagnostic, guided practice, safety, pilot with outcome measurement.

??? question "AIPL7 · Hard — Microsoft wants to build an AI project management tool using GPT-4. What would you build in 12 months?"
    **What it tests:** Phased roadmap.

    **Approach:** Integrate into existing workflows; AI for planning, tracking and reporting.

    **Model answer:** “Quarter 1: AI for creating plans from goals, breaking work into tasks, and drafting status updates from activity. Quarter 2: risk and dependency detection, workload balancing and estimates based on history. Quarter 3: natural-language queries across projects, auto-generated reports for executives, meeting-to-task flows. Quarter 4: automation and approvals, enterprise governance, and extensibility. Principles: humans confirm changes, transparency of sources, permissions. Metrics: time saved on planning and reporting, accuracy of estimates, weekly active teams, expansion. Risks: poor data quality and trust in estimates.”

    **Common mistakes:** Autonomous scheduling without oversight.

    **60-second answer:** Plan generation, status drafts, risk detection, query and reports; governance.

??? question "AIPL8 · Medium — Design an AI customer support product for SMBs. How is it different from enterprise solutions?"
    **What it tests:** Segment-specific design.

    **Approach:** SMBs need speed, low cost and simplicity.

    **Model answer:** “SMBs have small teams, limited technical skills and tight budgets. The product should set up in an hour: connect website, help docs and email, answer common questions, hand off to humans with context, and work across chat and WhatsApp. Pricing is simple and predictable. Enterprises need complex integrations, compliance, analytics and customisation. For SMBs, provide templates by industry, pre-built answers, and a dashboard showing resolved questions and time saved. Metrics: setup time, automation rate, CSAT, retention.”

    **Common mistakes:** Building enterprise features for SMBs.

    **60-second answer:** Fast setup, templates, simple pricing, human handoff.

??? question "AIPL9 · Medium — You're launching an AI creative writing tool. Sudowrite and Jasper exist. What's your angle?"
    **What it tests:** Differentiation in a crowded space.

    **Approach:** Pick a specific writer and workflow.

    **Model answer:** “Choose a segment (novelists, screenwriters, marketers, students) and a workflow that tools handle poorly: for example long-form consistency (characters, world and style memory), outline-to-draft with revision tracking, or collaboration with editors. Offer control (style sliders, rewriting suggestions) and keep the writer's voice. Address trust: ownership of content and no training on user text. Channels: writer communities and creators. Metrics: words written with the tool, project completion, retention.”

    **Common mistakes:** A general 'write anything' pitch.

    **60-second answer:** Specific writer, long-form memory, voice control, ownership promise.

??? question "AIPL10 · Hard — Stripe wants to build an AI fraud detection. You have 4 months for beta. What's the scope?"
    **What it tests:** Scoping an ML product with high stakes.

    **Approach:** Start narrow; measure cost of errors; include human review.

    **Model answer:** “Scope the beta to one fraud type and a subset of merchants with good data (for example card-not-present fraud). Build a scoring model using transaction, device and behaviour signals with explainable reason codes; integrate with existing rules and let merchants choose actions (allow, review, block). Include a feedback loop of disputes and chargebacks, monitoring dashboards and a rollback plan. Run in shadow mode first, then limited live use. Metrics: fraud caught, false positives, approval rate, review workload, latency. Define thresholds from the cost of fraud versus lost sales.”

    **Common mistakes:** Blocking transactions with no review or explainability.

    **60-second answer:** One fraud type, shadow mode, reason codes, merchant controls, cost-based thresholds.

??? question "AIPL11 · Medium — Build an AI-powered job search platform. How is it different from LinkedIn?"
    **What it tests:** Differentiation against a network.

    **Approach:** LinkedIn has network and supply; compete on job-seeker experience and outcomes.

    **Model answer:** “Do not replicate the network. Focus on the seeker's workflow: understand skills and goals, find matched roles from many sources, tailor applications, prepare for interviews, and track progress. Trust matters: show why a role matches, avoid spammy listings, and protect privacy. Sell to seekers first with a free core and paid coaching, then employers who want quality candidates. Metrics: interviews per applicant, time to offer, retention, and employer response rates.”

    **Common mistakes:** Trying to build a professional network.

    **60-second answer:** Seeker workflow, matching with explanations, tailored applications, outcomes.

??? question "AIPL12 · Medium — You're designing an AI personal finance advisor for Gen Z. What's your product thesis?"
    **What it tests:** Thesis and product principles.

    **Approach:** Define the user insight and the trust approach.

    **Model answer:** “Gen Z often lacks financial guidance and distrusts institutions. The thesis: a friendly coach that turns messy money into simple next steps (budget, save, invest basics, debt) using their data with consent. Features: spend insights, goals, automated small savings, and clear explanations. Guardrails: no personalised investment advice without regulation, transparent fees, security, and clear limits. Monetise through partnerships or subscription, avoiding conflicts of interest. Metrics: savings rate, active goals, retention and financial confidence.”

    **Common mistakes:** Giving regulated advice without compliance.

    **60-second answer:** Coach for next steps, insights and automation, trust and compliance.

??? question "AIPL13 · Hard — Create an AI legal document assistant for small law firms. What's your go-to-market?"
    **What it tests:** Regulated vertical GTM.

    **Approach:** Trust, accuracy and workflow fit decide adoption.

    **Model answer:** “Small firms value saved time but fear errors. Product: drafting and review of common documents (contracts, NDAs), clause comparison with sources, and redline suggestions, all with lawyer review. Go-to-market: start with a niche practice area, partner with bar associations, offer a pilot with measurable time saved, and build credibility via expert advisors and accuracy reports. Pricing per seat with usage limits. Provide confidentiality guarantees, audit logs and no training on client data. Metrics: hours saved per matter, adoption per lawyer, error rate found in review, renewal.”

    **Common mistakes:** Marketing it as replacing lawyers.

    **60-second answer:** Niche practice area, lawyer-in-the-loop, confidentiality, measurable time saved.

??? question "AIPL14 · Hard — Design an AI medical diagnosis assistant for primary care doctors. What are your constraints?"
    **What it tests:** High-stakes AI product thinking.

    **Approach:** Constraints: safety, regulation, liability, workflow, evidence.

    **Model answer:** “Constraints: patient safety (errors can harm), regulatory approval as a medical device in many regions, data privacy (health data laws), clinical validation with real evidence, explainability, liability and the doctor's final responsibility, integration with records and workflow, bias across populations, and clinician trust. Design as decision support: suggest possible diagnoses and next tests with evidence and uncertainty, never final answers. Start with narrow conditions where evidence is strong. Evaluate with clinicians, prospective studies and monitoring. Metrics: diagnostic accuracy support, time saved, clinician satisfaction and safety events.”

    **Common mistakes:** Presenting AI as the decision maker.

    **60-second answer:** Decision support, narrow scope, evidence, regulation, privacy, bias, clinician in control.

## Product design

??? question "AIPD1 · Hard — Design a conversation flow for an AI therapist bot. What guardrails do you need?"
    **What it tests:** Safety-critical conversational design.

    **Approach:** Define scope, user safety, escalation, privacy and honesty about limits.

    **Model answer:** “State clearly that it is a wellbeing support tool, not a clinician. Flow: welcome with scope and privacy, a short check-in, supportive listening and evidence-based exercises (breathing, journaling, cognitive reframing), and goal tracking. Guardrails: detect crisis language and immediately show local emergency and helpline options and encourage contacting a person; never diagnose or give medication advice; avoid dependency by encouraging real-world support; age gating; strict privacy (minimal data, encryption, deletion on request); human review of risky cases; and clinician-reviewed content. Test with safety evals and expert panels. Metrics: user wellbeing scores, crisis handoff accuracy, harmful-response rate (target zero), and retention without over-reliance.”

    **Common mistakes:** Letting the bot act like a licensed therapist; weak crisis handling.

    **60-second answer:** Scope and disclaimers, supportive exercises, crisis detection with handoff, privacy, clinician review.

??? question "AIPD2 · Medium — How would you design UI for an AI image editor that combines generation and editing?"
    **What it tests:** Interaction design for creative tools.

    **Approach:** Support both prompts and direct manipulation; keep control and history.

    **Model answer:** “Combine a canvas with a prompt bar. Users can generate, then select regions to edit by painting or clicking, with prompts like 'replace the sky'. Provide layers, undo history, versions side by side, and sliders for strength. Offer presets and reference images, and show non-destructive edits. Make costs and time clear. For beginners, suggested edits; for pros, fine controls. Measure first-image success time, edits per project, export rate and retention.”

    **Common mistakes:** Chat-only editing with no direct manipulation or history.

    **60-second answer:** Canvas plus prompt, region edits, layers, history, versions, presets.

??? question "AIPD3 · Medium — Design an AI-powered email composer for busy executives. What's the UX?"
    **What it tests:** Workflow design and trust.

    **Approach:** Speed, control, tone, and safety around sending.

    **Model answer:** “Executives want fast, in-voice drafts. Offer one-tap draft from a short intent ('decline politely, offer next week'), learn tone from past sent emails, show a clear diff for edits, and let them adjust length and tone quickly. Surface key facts from the thread and calendar, flag commitments and sensitive content, and never auto-send. Include shortcuts and mobile-first layouts, delegation to assistants, and an undo send. Metrics: time to send, edit rate, adoption and satisfaction.”

    **Common mistakes:** Auto-sending without review.

    **60-second answer:** Intent-to-draft, voice learning, diffs, flags, never auto-send.

??? question "AIPD4 · Medium — Create an interaction model for an AI code review tool that works in VS Code."
    **What it tests:** Developer workflow integration.

    **Approach:** Fit existing review habits, minimise noise, give evidence.

    **Model answer:** “Provide inline comments with severity, explanation and a suggested fix as a diff that can be applied or dismissed. Group by type (bug, security, style, performance), allow configuration of rules, and learn from dismissed suggestions to reduce noise. Show reasoning and references to code and docs. Support a summary of the change, test suggestions and a pre-commit mode. Keep it fast and optional. Metrics: accepted suggestion rate, bugs caught, review time saved, and false-positive rate.”

    **Common mistakes:** Flooding developers with low-value comments.

    **60-second answer:** Inline severity-labelled comments, apply-as-diff, learn from dismissals, config.

??? question "AIPD5 · Medium — Design how users would control 'creativity vs accuracy' in an AI writing assistant."
    **What it tests:** Control design for probabilistic systems.

    **Approach:** Translate technical settings to user goals; show effects.

    **Model answer:** “Avoid exposing 'temperature'. Offer a simple mode choice (Precise, Balanced, Creative) with plain descriptions, and context-sensitive defaults (precise for summaries, creative for brainstorming). Provide a slider only in advanced settings, with examples of how outputs change. For factual content, add source-backed mode with citations. Allow regenerate and compare variants. Test comprehension and satisfaction.”

    **Common mistakes:** Exposing raw model parameters.

    **60-second answer:** Named modes, smart defaults, examples, source-backed option.

??? question "AIPD6 · Medium — How would you design loading states for an AI feature that takes 45 seconds?"
    **What it tests:** Latency UX.

    **Approach:** Set expectations, show progress, allow multitasking.

    **Model answer:** “Tell users upfront ('about 45 seconds'), show meaningful progress steps (reading, analysing, drafting), stream partial results where possible, allow users to continue other work or leave and get notified, and provide a cancel option. Use skeletons and animations sparingly. If failure is possible, explain and offer retry with saved input. Measure abandonment and satisfaction by wait time.”

    **Common mistakes:** Indefinite spinner with no information.

    **60-second answer:** Upfront estimate, step progress, streaming, background with notification, cancel and retry.

??? question "AIPD7 · Medium — Design a feedback mechanism for users to improve AI outputs over time."
    **What it tests:** Feedback loops.

    **Approach:** Make it low-effort, informative and visible in effect.

    **Model answer:** “Provide thumbs with optional reasons (wrong, unhelpful, unsafe, style), inline edit tracking (what users change tells more than a vote), and a 'remember this' option for preferences. Show that feedback matters ('we will use shorter replies'). Feed labelled failures into an evaluation set and prompt or model improvements. Protect privacy and let users opt out. Metrics: feedback rate, quality trend, repeat issues.”

    **Common mistakes:** Collecting votes nobody uses.

    **60-second answer:** Thumbs plus reasons, edit signals, preferences, visible effect, eval pipeline.

??? question "AIPD8 · Medium — Create an onboarding flow for users who've never used AI before."
    **What it tests:** Inclusive onboarding.

    **Approach:** Reduce fear, show value fast, teach by doing.

    **Model answer:** “Start with a friendly explanation of what it can do and what it cannot, then offer three real tasks to try with one tap (write a message, plan a trip, explain a document). Provide example prompts, plain language, and guardrails explained simply (it can make mistakes, check important facts). Offer a short guided first success and a help hub. Use progressive disclosure for advanced features. Measure completion, first successful task and week-1 return.”

    **Common mistakes:** Long tutorials and jargon.

    **60-second answer:** Plain intro, tap-to-try tasks, example prompts, expectations about mistakes.

??? question "AIPD9 · Hard — Design how an AI scheduling assistant would handle conflicts and preferences."
    **What it tests:** Complex decision UX.

    **Approach:** Collect preferences, explain trade-offs, ask for confirmation.

    **Model answer:** “Capture preferences (work hours, focus blocks, travel buffers, priority people) and rank importance. When a conflict arises, propose options with trade-offs ('move A to Thursday; B is lower priority'), explain reasoning, and ask for confirmation before changing others' invites. Learn from choices over time. Provide an undo and an audit trail, and respect others' privacy. Metrics: conflicts resolved without manual effort, undo rate and satisfaction.”

    **Common mistakes:** Silently rescheduling meetings.

    **60-second answer:** Preference model, ranked options with reasons, confirm before change, undo.

??? question "AIPD10 · Hard — How would you design a 'confidence indicator' for AI-generated medical advice?"
    **What it tests:** Uncertainty communication in high-stakes domains.

    **Approach:** Avoid false precision; guide action.

    **Model answer:** “Avoid a percentage unless calibrated. Use clear levels linked to actions: 'well supported by guidelines', 'limited evidence', 'seek a clinician'. Show sources, what information was missing, and red-flag symptoms prompting urgent care. Always include a path to a professional. Test with users and clinicians for comprehension and for reducing risky behaviour. Track whether users take appropriate action and whether the indicator is calibrated against expert review.”

    **Common mistakes:** A single number that looks scientific but is not calibrated.

    **60-second answer:** Levels tied to actions, sources, missing-info prompts, clinician path, calibration.

??? question "AIPD11 · Hard — Design a collaboration model for multiple users working with one AI assistant."
    **What it tests:** Multi-user AI design.

    **Approach:** Shared context, permissions, attribution, conflicts.

    **Model answer:** “Use shared workspaces where the assistant sees agreed context and each message is attributed to a person. Provide roles and permissions, private versus shared threads, and visibility of what the AI used. Handle conflicting instructions with explicit ownership (who can approve changes) and a change log. Allow asking the assistant to summarise decisions and tasks. Metrics: active teams, shared artifacts produced, and conflicts resolved.”

    **Common mistakes:** One chat thread for everyone with no attribution.

    **60-second answer:** Shared workspace, attribution, permissions, approvals, change log.

??? question "AIPD12 · Medium — Create UI for an AI data analyst that generates SQL and visualizations."
    **What it tests:** Trust and transparency for data tools.

    **Approach:** Show the query, the data, assumptions and allow edits.

    **Model answer:** “Layout: question box, generated answer with chart, and a panel showing the SQL, tables used, filters and assumptions. Allow editing the SQL or the question, switching charts, and exporting. Validate queries (row counts, sample data) and warn about ambiguous definitions with a metrics glossary. Provide permissions and data governance. Metrics: answers accepted without edits, accuracy on a test set, time to insight.”

    **Common mistakes:** Black-box numbers with no way to inspect.

    **60-second answer:** Answer plus SQL and assumptions, editable, validation, governed definitions.

## Product strategy

??? question "AIPS1 · Hard — You're CEO of Anthropic. What should your product strategy be for the next 3 years?"
    **What it tests:** Company-level strategic thinking.

    **Approach:** Vision, differentiation, segments, moats, sequencing and risks.

    **Model answer:** “A plausible strategy: be the most trusted and capable AI for work, focusing on high-value professional and enterprise use (coding, analysis, writing, agents) where reliability and safety are paid for. Year 1: strengthen core developer and enterprise offerings and make agentic workflows dependable. Year 2: deepen integrations and data connections, expand consumer and team products where retention is strong. Year 3: platform ecosystem with partners and controls for regulated industries. Moats: model quality, trust and safety, enterprise relationships and workflow integration. Risks: compute costs, competition, regulation. I would define metrics: revenue from enterprise and API, retention, and trust measures.”

    **Common mistakes:** A vague 'build the best AI' with no focus or sequencing.

    **60-second answer:** Trusted work AI, coding and agents first, enterprise depth, ecosystem later; moats and metrics.

??? question "AIPS2 · Hard — Google has Gemini. Should they integrate it into every product or keep it separate?"
    **What it tests:** Platform integration strategy.

    **Approach:** Distribution advantage vs fragmentation, quality and trust.

    **Model answer:** “Both: a standalone product for exploration and deep tasks, plus embedded features where they clearly improve workflows (search, email, docs, maps). Integration uses distribution but risks cluttered, inconsistent experiences and trust problems if quality varies. Set shared standards: a common model platform, design patterns and safety evaluations, with product teams choosing where AI adds real value. Measure usage and satisfaction by surface and prune weak integrations.”

    **Common mistakes:** Putting AI everywhere regardless of value.

    **60-second answer:** Hybrid: standalone plus embedded where valuable; shared platform and standards.

??? question "AIPS3 · Hard — OpenAI has ChatGPT, DALL-E, Sora as separate products. Should they combine them?"
    **What it tests:** Product portfolio strategy.

    **Approach:** User jobs, discoverability, cost and focus.

    **Model answer:** “Users' jobs cross modalities (write, illustrate, animate), so a unified entry point with modality as capability is attractive: one conversation, shared context and history, one subscription. Keep specialised surfaces for professionals who need controls (video editing tools). Technical and cost differences matter, so combine experiences while keeping separate backend services. Measure cross-modal use, retention and revenue per user. Risk: overloading the main product.”

    **Common mistakes:** Merging everything into one interface without considering pro workflows.

    **60-second answer:** Unify entry and context, keep pro surfaces, measure cross-modal usage.

??? question "AIPS4 · Medium — You're PM of GitHub Copilot. Microsoft just launched 365 Copilot. How do you think about product portfolio?"
    **What it tests:** Portfolio coherence within a company.

    **Approach:** Define distinct jobs, shared platform, avoid cannibalisation.

    **Model answer:** “Copilot for developers and Copilot for office work serve different users and workflows. I would define clear boundaries (code and engineering workflows versus documents and email), share the underlying platform for models, identity, security and billing, and create bridges where jobs overlap (documentation, project updates, requirements to code). Align branding and pricing so customers understand bundles. Metrics: adoption per persona, cross-product usage and enterprise expansion.”

    **Common mistakes:** Overlapping features and confusing pricing.

    **60-second answer:** Distinct jobs, shared platform, bridges at overlaps, coherent packaging.

??? question "AIPS5 · Hard — Anthropic's Claude is 'safer', but OpenAI's ChatGPT has more users. How do you win as Anthropic?"
    **What it tests:** Competitive positioning.

    **Approach:** Choose where safety and reliability are decisive.

    **Model answer:** “Do not chase mass consumer reach on its terms. Win segments where trust is a purchase driver: enterprises, regulated industries, coding and agents where mistakes are costly. Demonstrate reliability with evidence, offer controls and compliance, and make products that excel at long, complex work. Grow consumer usage through strong core experiences and partnerships, but let enterprise and developers lead. Metrics: enterprise revenue, retention, share of coding workloads and customer trust measures.”

    **Common mistakes:** Marketing safety without product proof.

    **60-second answer:** Win trust-sensitive segments, prove reliability, partner for reach.

??? question "AIPS6 · Medium — Should an AI company build one general model or multiple specialized models?"
    **What it tests:** Technical-strategic trade-off.

    **Approach:** Quality, cost, latency, maintenance and customer needs.

    **Model answer:** “General models offer breadth and easier maintenance; specialised models can be cheaper, faster and better in narrow domains. A common strategy is a family: a frontier general model plus smaller, faster or domain-tuned variants, with routing. Decide by customer needs (cost-sensitive high volume tasks, regulated domains), evaluation results and operational complexity. Measure quality per cost and latency by task.”

    **Common mistakes:** Choosing by ideology instead of task evidence.

    **60-second answer:** Model family with routing; specialise where evals and economics justify it.

??? question "AIPS7 · Hard — You're PM at Meta. How should Llama (open source) fit into Meta's product strategy?"
    **What it tests:** Open-source strategy.

    **Approach:** What does Meta gain from openness?

    **Model answer:** “Meta's core business is attention and engagement across its apps, so cheap, widely available models reduce dependence on competitors and attract developer ecosystems, talent and standards. Llama supports Meta's own products (assistants, ads tools, creator features) while the open ecosystem improves tooling. Decide what to keep open and what to differentiate: integration with Meta's data and surfaces. Risks: misuse, enabling competitors. Metrics: ecosystem adoption, product usage of Meta AI features and cost savings.”

    **Common mistakes:** Treating open source as charity.

    **60-second answer:** Reduce dependence, build ecosystem, differentiate through product integration.

??? question "AIPS8 · Hard — Your AI startup has a great model but no distribution. OpenAI has worse tech but ChatGPT distribution. What's your strategy?"
    **What it tests:** Startup strategy against incumbent distribution.

    **Approach:** Find a wedge where quality matters more than convenience.

    **Model answer:** “Do not fight head-on for general users. Find a segment where model quality changes outcomes (specific domain, language, latency, privacy, or cost) and sell to them directly. Use distribution partnerships: be embedded in tools others already use through APIs and plugins. Build a product around the model (workflow, data, integrations) so value is not only the model. Show proof via benchmarks on customer tasks. Metrics: wins in the chosen segment, retention and expansion.”

    **Common mistakes:** Assuming a better model sells itself.

    **60-second answer:** Niche where quality decides, partner for distribution, build workflow moat.

??? question "AIPS9 · Medium — Should AI products be priced per-seat (like SaaS) or per-usage (like APIs)?"
    **What it tests:** Pricing strategy.

    **Approach:** Value metric, cost structure, buyer preferences.

    **Model answer:** “Per-seat is predictable and easy to buy but misaligns with cost when AI does work without a user or usage varies widely. Per-usage aligns with cost and value but is unpredictable for buyers. A hybrid is common: seat plus included usage and overage, or outcome-based pricing where results are measurable. Choose based on how value scales, cost per task and customer preference; test with pilots.”

    **Common mistakes:** Copying SaaS pricing despite variable costs.

    **60-second answer:** Hybrid seat plus usage; outcome pricing where measurable; test with pilots.

??? question "AIPS10 · Hard — You're PM at Notion. How should you integrate AI throughout the product versus building standalone AI features?"
    **What it tests:** Integration strategy in a workflow product.

    **Approach:** Embed where the work happens; keep standalone where new jobs exist.

    **Model answer:** “Notion's strength is knowledge and workflow in one workspace. AI should be woven into docs, databases and search (drafting, summarising, filling properties, answering from workspace data), so value appears in context. A standalone assistant makes sense for cross-workspace questions and automation. Prioritise by frequency and value, respect permissions and privacy, and make AI results editable. Pricing as an add-on or bundled depends on adoption. Metrics: AI feature usage per active user, retention and expansion.”

    **Common mistakes:** Bolting on a chatbot unrelated to the workflow.

    **60-second answer:** Embed in docs and databases, standalone assistant for cross-workspace tasks, respect permissions.

??? question "AIPS11 · Hard — Microsoft owns OpenAI's tech. Google built Gemini in-house. Which strategy is better for the next 5 years?"
    **What it tests:** Strategic comparison.

    **Approach:** Speed, control, dependency, ecosystem and risk.

    **Model answer:** “Partnering gave Microsoft speed to market and frontier capability with less upfront research risk, at the cost of dependence and shared economics. Building in-house gives Google control, integration with hardware and data, and cost advantages at scale, but demands heavy investment and execution. Over five years the winner depends on model quality parity, distribution, cost per query and flexibility; a hedged approach (own models plus partnerships) reduces risk. I would judge by product performance, margins and ecosystem adoption rather than origin.”

    **Common mistakes:** Declaring a winner without criteria.

    **60-second answer:** Compare on speed, control, dependency, cost; hedge strategy.

??? question "AIPS12 · Medium — Your AI company needs to decide: improve the model or ship more features? How do you decide?"
    **What it tests:** Prioritisation between platform and product.

    **Approach:** Where is the binding constraint on user value?

    **Model answer:** “Diagnose why users are not getting value: model quality (errors, capability limits) or product gaps (workflow, UX, integrations). Use evaluation data and user research. If quality blocks key use cases, model improvements have the highest leverage; if users are happy with quality but cannot complete jobs, features win. Balance with a portfolio: allocate a share to model and platform and a share to product, and review quarterly. Metrics: task success, retention drivers and cost.”

    **Common mistakes:** Treating it as either-or without evidence.

    **60-second answer:** Find the binding constraint with evals and research; portfolio allocation.

## Safety and ethics

??? question "AISE1 · Hard — Users are using ChatGPT to write phishing emails. How do you stop this without breaking legitimate use?"
    **What it tests:** Dual-use safety trade-offs.

    **Approach:** Detect intent and patterns; add friction by risk; protect benign users.

    **Model answer:** “Use layered defences: intent and content classifiers for clear phishing attempts, policies that refuse impersonation of institutions or credential harvesting, rate limits and account signals for abuse, and monitoring for patterns across accounts. Provide safe alternatives (security awareness training templates). Keep false positives low for marketing and security professionals with verified accounts and clear usage policies. Measure abuse detection, false-positive rate on benign emails and user complaints. Iterate with red teaming.”

    **Common mistakes:** Blocking all email writing or ignoring dual use.

    **60-second answer:** Layered classifiers, policies, rate limits, verified pro paths, red teaming.

??? question "AISE2 · Hard — Your AI image generator is being used to create deepfakes. You have 2 weeks to ship a solution. What do you do?"
    **What it tests:** Rapid safety response.

    **Approach:** Triage, quick mitigations, then longer-term controls.

    **Model answer:** “Within two weeks: block generation of real people's likeness for sensitive categories (public figures in deceptive contexts, sexual content, minors), add detection and prompt filters, enable reporting and rapid takedown, add visible and invisible watermarking or provenance metadata, and rate-limit suspicious accounts. Communicate policy clearly. Longer term: consent-based likeness features, partnerships on detection standards, audits. Metrics: abuse volume, time to takedown and false positives.”

    **Common mistakes:** Only relying on terms of service.

    **60-second answer:** Likeness blocks, filters, provenance, reporting and takedown, rate limits, comms.

??? question "AISE3 · Hard — An AI product you built is showing bias against certain demographics. How do you fix it at the product layer?"
    **What it tests:** Mitigating bias without retraining.

    **Approach:** Measure, mitigate and monitor at the product layer.

    **Model answer:** “Measure with slice-based evaluation across demographics and contexts. Product-layer fixes: adjust prompts and instructions, add post-processing rules and output checks, improve retrieval data, apply thresholds by use case, offer human review for high-stakes decisions, and show uncertainty. Provide user feedback channels and publish limitations. Monitor continuously and escalate model-level issues to research. Metrics: disparity measures and complaint rates.”

    **Common mistakes:** Assuming a single fix removes bias.

    **60-second answer:** Slice evals, prompt and rule mitigations, human review, monitoring.

??? question "AISE4 · Hard — Design a content moderation system for an AI chatbot that millions of kids will use."
    **What it tests:** Child safety design.

    **Approach:** Strict policies, layered filters, parental controls, escalation.

    **Model answer:** “Design for the strictest standards: age-appropriate model and content settings, input and output classifiers for sexual, violent, self-harm and grooming content, topic restrictions, no personal data collection beyond need, and parental controls and reports. Add crisis detection with safe responses and escalation, human review of flagged conversations, audit logs, and regular red teaming with child safety experts. Comply with children's privacy laws. Metrics: violation rate, false negatives found in audits, escalation response time and parent satisfaction.”

    **Common mistakes:** Relying on a single filter.

    **60-second answer:** Layered filters, restricted topics, crisis handling, parental controls, audits and compliance.

??? question "AISE5 · Hard — Your AI hiring tool is 95% accurate but has subtle gender bias. How do you address this?"
    **What it tests:** Fairness in high-stakes decisions.

    **Approach:** Quantify, mitigate, change the decision role of AI, and govern.

    **Model answer:** “Accuracy is not enough. Measure outcomes by gender (selection rates, error rates), investigate causes (data, features such as proxies, labels), and mitigate: remove proxies, rebalance, set fairness constraints, and calibrate. Change the product role to decision support with human review, explanations and audit logs. Comply with employment laws and notify candidates. Monitor continuously and run external audits. If bias persists, pause use for that decision step.”

    **Common mistakes:** Shipping because overall accuracy is high.

    **60-second answer:** Measure by group, mitigate causes, human oversight, audits, legal compliance.

??? question "AISE6 · Hard — Users are jailbreaking your AI model to generate harmful content. What product solutions do you implement?"
    **What it tests:** Adversarial safety.

    **Approach:** Defence in depth; monitor and adapt.

    **Model answer:** “Layers: stronger system instructions, input and output classifiers, refusals with safe alternatives, rate limits and account-level enforcement, detection of known jailbreak patterns, red teaming and bug bounties, and rapid patching with evaluation sets built from discovered attacks. Monitor for novel attacks and share learnings with the safety team. Balance safety with usability by tracking false refusals. Metrics: jailbreak success rate on a test suite, time to patch and benign refusal rate.”

    **Common mistakes:** A single filter; ignoring false refusals.

    **60-second answer:** Layered defences, red teaming, evals from attacks, rapid patching, monitor false refusals.

??? question "AISE7 · Hard — Your AI health advisor sometimes gives dangerous medical advice. How do you ship while staying safe?"
    **What it tests:** Shipping in high-risk domains.

    **Approach:** Narrow scope, guardrails, human oversight, evidence.

    **Model answer:** “Narrow the scope to low-risk guidance (education, lifestyle, preparing for visits), route symptoms with red flags to urgent care and clinicians, ground answers in vetted sources with citations, add disclaimers and clear limits, and use clinician-reviewed evaluation sets with zero tolerance for dangerous failures. Include human escalation and incident response. Release gradually with monitoring. If safety cannot meet thresholds, do not ship that capability. Metrics: dangerous response rate on evals, escalation accuracy and user outcomes.”

    **Common mistakes:** Shipping with a disclaimer only.

    **60-second answer:** Narrow scope, vetted sources, red-flag escalation, clinician evals, staged release.

??? question "AISE8 · Medium — Design a system to make AI-generated content transparently labeled while keeping good UX."
    **What it tests:** Transparency design.

    **Approach:** Label clearly, consistently and unobtrusively; combine visible and technical signals.

    **Model answer:** “Use visible, consistent labels (a small badge or caption) on AI-generated or AI-edited content, with a details view explaining what was generated. Add invisible provenance (watermarks and content credentials) that persist when shared. Let creators label and disclose easily, and automate labelling for content created inside the product. Design for context: strong labels for realistic media and news-like content, lighter for obvious creative work. Test comprehension and ensure labels do not harm usability. Metrics: label coverage and user understanding.”

    **Common mistakes:** Burying disclosure or relying only on removable labels.

    **60-second answer:** Visible labels plus provenance, easy creator disclosure, context-based prominence.

## Metrics and pricing

??? question "AIMP1 · Hard — Design a full metrics framework for an AI code assistant. What's the north star?"
    **What it tests:** Metrics design for an AI product.

    **Approach:** North star, input metrics, quality, trust, economics and guardrails.

    **Model answer:** “North star: weekly number of developers who ship code with accepted AI help, or accepted suggestions that survive to merge (a quality-adjusted measure). Inputs: activation (first accepted suggestion), suggestions shown and accepted, acceptance by language and task, latency. Quality: code that survives review, test pass rate, bugs introduced, edit distance. Trust: opt-out rate, satisfaction, frequency of reverts. Business: retention, seats and expansion, cost per active developer. Guardrails: security issues, license and copyright flags, developer productivity measured independently.”

    **Common mistakes:** Using acceptance rate alone.

    **60-second answer:** North star: merged AI-assisted code; inputs, quality, trust, economics, guardrails.

??? question "AIMP2 · Hard — How would you price ChatGPT if you were launching it today? What's your pricing strategy?"
    **What it tests:** Pricing from first principles.

    **Approach:** Costs, value, segments, competition and willingness to pay.

    **Model answer:** “Start with cost per use (inference is a real marginal cost) and value by segment. Offer a free tier to build the market with limits, a paid individual plan priced near comparable subscriptions that gives higher limits and better models, team and enterprise plans with admin and security, and API usage pricing for developers. Test price points and bundles, use usage caps to protect margin, and consider regional pricing. Track conversion, churn, gross margin and the free-to-paid ratio.”

    **Common mistakes:** Setting price without understanding marginal cost.

    **60-second answer:** Free tier, individual plan, team and enterprise, API; test and protect margin.

??? question "AIMP3 · Hard — Your AI API costs $0.10 per request but competitors charge $0.01. How do you compete?"
    **What it tests:** Competing at a price gap.

    **Approach:** Understand quality difference, reduce cost, differentiate, segment.

    **Model answer:** “First check if the offerings are comparable on quality, latency and reliability. If yes, reduce cost: model optimisation, caching, smaller models for easy requests, batching and better infrastructure. If you are better, segment customers for whom quality matters, justify price with outcomes (accuracy, support, SLAs), and offer volume tiers. Consider a lite product at a lower price. Show total cost of ownership including errors and rework. Metrics: win rate, margin and churn.”

    **Common mistakes:** Matching price and losing money.

    **60-second answer:** Compare quality, cut cost, segment on value, tiered product line.

??? question "AIMP4 · Hard — Create a freemium model for Claude where 98% of users stay free but you're still profitable."
    **What it tests:** Unit economics of freemium.

    **Approach:** Control cost per free user, monetise the high-value 2%.

    **Model answer:** “Model it: if free users cost X per month and 2% pay Y, profitability requires Y x 2% > X, so keep free usage cheap (smaller models, limits, caching, lower priority) and make paid value high (higher limits, best models, long context, projects, team features). Use enterprise and API revenue to subsidise. Reduce abuse. Track cost per free user, conversion, revenue per paying user, and margin by cohort. Free serves marketing and data on use cases rather than being a charity.”

    **Common mistakes:** Ignoring the cost of free users.

    **60-second answer:** Cheap free tier, valuable paid tier, enterprise and API subsidy, monitor unit economics.

??? question "AIMP5 · Hard — What metrics would tell you if an AI product has product-market fit vs traditional products?"
    **What it tests:** PMF measurement for AI.

    **Approach:** Traditional signals plus AI-specific quality and trust.

    **Model answer:** “Traditional signals still apply: retention curves that flatten, organic growth, the 'very disappointed' survey, and willingness to pay. AI-specific: task success and acceptance rates, repeat use for the same job, edit distance, reliance behaviours, and cost per successful task, because high usage can hide poor quality or unsustainable cost. Also watch novelty decay (usage spikes then drops). Segment by use case to find where PMF exists.”

    **Common mistakes:** Using usage growth alone.

    **60-second answer:** Retention and survey plus task success, repeat jobs, cost per success, novelty decay.

??? question "AIMP6 · Hard — Design an A/B test to measure if a new AI feature actually improves user outcomes (not just engagement)."
    **What it tests:** Experiment design.

    **Approach:** Outcome metrics, guardrails, randomisation and duration.

    **Model answer:** “Define the outcome (time to complete tasks, task success, resolution, conversion, quality ratings) rather than clicks. Randomise users, keep the treatment minimal, pre-register primary and guardrail metrics (errors, complaints, latency, cost), and run long enough to cover weekly cycles and novelty effects. Measure outcomes with independent signals such as human-rated quality or downstream results (fewer support tickets, successful purchases). Segment by user type, check sample ratio, and compute confidence intervals. Decide using impact and cost.”

    **Common mistakes:** Measuring engagement only.

    **60-second answer:** Outcome metrics, randomisation, guardrails, novelty-aware duration, independent quality signal.


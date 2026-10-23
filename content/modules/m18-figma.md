---
id: m18
n: 18
title: Figma and AI Design Tools
subtitle: Design screens, build click-through prototypes, run workshops in FigJam, generate working prototypes with Figma Make, and hand designs to Claude Code through Figma's MCP server.
summary: Figma's products and pricing, the interface, frames, auto layout, components and variants, prototyping, comments and handoff in Dev Mode, FigJam for journey maps and affinity mapping, Figma AI and Figma Make, the Figma MCP server with Claude Code, five labs and PM best practices.
hours: 6
status: drafted
sources: "Figma Help Center, Figma pricing page and MCP collection docs; DeepLearning.AI Claude Code course (Figma MCP project); Module 5; checked 23 Oct 2026"
---

!!! warning "Illustrative screens"
    Figma's interface is updated often. Screens below are **illustrative wireframes**; search the [Figma Help Center](https://help.figma.com) if a menu has moved.

## Figma's products

```chart
type: canvas
title: The Figma family
cols: 3
cells:
  - title: "Figma Design"
    text: ["Screens, components, design systems", "Click-through prototypes"]
    tone: b
  - title: "FigJam"
    text: ["Whiteboard for workshops", "Journey maps, affinity maps, retros"]
    tone: g
  - title: "Dev Mode"
    text: ["Specs, measurements and code hints for engineers", "Includes the MCP server"]
    tone: v
  - title: "Figma Make"
    text: ["Prompt or design → working prototype", "AI writes the code"]
    tone: w
  - title: "Figma Slides"
    text: ["Presentations built from design files"]
    tone: r
  - title: "Community"
    text: ["Free templates, UI kits, plugins", "Start from a kit instead of from zero"]
    tone: b
caption: PMs mostly use FigJam for workshops, Figma Design to review and sketch, and Figma Make for quick working prototypes.
```

### What it costs (checked 23 Oct 2026)

| Plan | Price | Notes |
|---|---|---|
| **Starter** | Free | Limited files, a daily AI credit allowance, 3 Figma Make files |
| **Professional** | about $16 a month (full seat); about $12 (Dev seat); about $3 (Collab seat) | Unlimited files, Dev Mode, MCP server, monthly AI credits |
| **Organization / Enterprise** | from about $55 a month per full seat | Design systems at scale, admin controls |

**Viewing and commenting are free**. A PM who only reviews and comments can use a free or Collab seat. Check [figma.com/pricing](https://www.figma.com/pricing/).

## Level 1 · The interface and your first screens

```chart
type: window
title: The Figma Design editor
app: "Figma"
url: "figma.com/design/split-bill"
sidebar: ["[1] Layers", "Frame: Home", "  Header", "  Item list", "  Total bar", "Frame: Split", "Assets"]
main:
  - ["tabs", "Move|Frame (F)|Shape (R)|Text (T)|Comment"]
  - ["img", "[2] Canvas: three phone frames side by side"]
  - ["text", "Tip: press F, then pick a phone size from the right panel to create a frame."]
panel:
  - ["tabs", "*Design|Prototype"]
  - ["bar", "[3] Auto layout"]
  - ["row", "Direction|Vertical"]
  - ["row", "Gap|16"]
  - ["row", "Padding|24"]
  - ["bar", "Fill · Stroke · Effects"]
notes:
  - "Layers panel: every frame, group and element. Name layers clearly, for example 'Total bar'."
  - "Canvas: your screens. Use frames sized to a phone or desktop."
  - "Properties panel: size, auto layout, colours, text styles. The Prototype tab adds clicks between screens."
caption: Core shortcuts include F (frame), R (rectangle), T (text), Shift+A (add auto layout).
```

!!! level1 "Level 1 · Beginner"
    * **Frames** are screens. Start with a phone frame (for example 390 × 844).
    * **Auto layout** (Shift+A) stacks items with consistent gaps and padding, and resizes when content changes. Use it for buttons, cards and lists.
    * **Components** are reusable elements (a button, a card). Change the main component and every copy updates.
    * **Styles and variables** keep colours, text sizes and spacing consistent.
    * **Start from a UI kit** in Figma Community, so you are not drawing buttons from scratch.

## Level 2 · Prototypes, reviews and handoff

### Click-through prototypes

```chart
type: steps
title: Make a clickable prototype
steps:
  - ["Prototype tab", "Switch from Design to Prototype in the right panel"]
  - ["Connect", "Drag the + handle from a button to the next screen"]
  - ["Interaction", "On click → Navigate to; animation Smart animate"]
  - ["Flow start", "Set the first screen as the flow's starting point"]
  - ["Present", "Click Play; share the prototype link"]
caption: Test the prototype with five users before anyone writes code (Module 3: usability testing).
```

!!! level2 "Level 2 · Working PM"
    * **Variants** group versions of a component (button: default, hover, disabled), so states are designed, not forgotten.
    * **Comments**: press C and click to leave feedback on an exact spot; mention people with @.
    * **Dev Mode** shows engineers measurements, colours, assets and code hints. Mark frames **Ready for dev**.
    * **Branching** (paid plans) lets designers explore without breaking the main file.
    * **PM review checklist**: every state designed (empty, loading, error, success)? Copy final? Accessible contrast and tap sizes? Edge cases from the PRD covered?

### FigJam for workshops

```chart
type: canvas
title: FigJam boards PMs run
cols: 3
cells:
  - title: "Affinity map"
    text: ["Paste interview quotes as stickies", "Group into themes", "Vote with stamps"]
    tone: g
  - title: "User journey map"
    text: ["Stages across the top", "Actions, thoughts, pain points, opportunities"]
    tone: b
  - title: "Prioritisation 2×2"
    text: ["Impact versus effort", "Move stickies live with the team"]
    tone: v
  - title: "Retro"
    text: ["Went well, didn't, try next", "Timer and voting"]
    tone: w
  - title: "Flow diagram"
    text: ["Shapes and connectors for user or system flows"]
    tone: r
  - title: "AI in FigJam"
    text: ["Summarise or sort stickies; generate a first board from a prompt (where available)"]
    tone: b
caption: Templates for all of these are in FigJam's template picker and Figma Community.
```

## Level 3 · Figma AI, Figma Make and MCP

!!! level3 "Level 3 · Advanced"
    Goal: go from idea or design to a working prototype, and let Claude Code build directly from your Figma frames.

### Figma AI

Figma's AI features (they vary by plan and change often) help with tasks such as generating a first draft of a layout, renaming layers, rewriting or translating text, removing image backgrounds and searching for similar designs. Each use spends **AI credits** from your plan.

### Figma Make: prompt to working prototype

```chart
type: window
title: Figma Make
app: "Figma Make"
sidebar: ["[1] Prompt", "Attach frames", "Versions", "Publish"]
main:
  - ["user", "Turn the attached three Split Bill frames into a working prototype. Totals must recalculate when I add a friend. Sample data."]
  - ["ai", "[2] Building… The prototype uses your frames' layout and colours. Try adding a friend in the preview."]
  - ["user", "[3] Add an error state when a split doesn't add up to the bill total."]
panel:
  - ["tabs", "*Preview|Code"]
  - ["img", "Working prototype"]
  - ["btn", "Share link"]
notes:
  - "Start from a prompt, or attach existing frames so the result matches your design."
  - "Make writes real code. Test interactions in the preview."
  - "Ask for edge cases and states, one per message."
caption: Make is ideal for testing behaviour (calculations, flows) that a click-through prototype can't show.
```

### Figma MCP server + Claude Code

The **Figma MCP server** lets Claude Code (and other AI tools) read your design: layout, components, variables and assets. Claude can then build the screen in code to match.

```chart
type: workflow
title: From Figma frame to code with Claude Code
nodes:
  - ["human", "Select a frame in Figma", "Copy link to selection"]
  - ["action", "Add Figma MCP to Claude Code", "claude mcp add (see Figma's MCP docs for the URL)"]
  - ["ai", "Prompt Claude Code", "'Implement this frame: <link>. Use our components.'"]
  - ["ai", "Claude reads the design", "Layout, variables, assets"]
  - ["output", "Code that matches", "Review in the browser"]
  - ["human", "Compare and fix", "Screenshot side by side"]
per_row: 3
caption: Full access needs a seat with Dev Mode (a full or Dev seat); other seats have monthly limits. Claude.ai also has a Figma connector for reading files in chat.
```

## Labs

!!! example "Lab 1 · Three screens with auto layout (Free, 40 minutes)"
    1. Duplicate a free mobile UI kit from Figma Community.
    2. Create three phone frames: Bill, Split with friends, Request payment.
    3. Build the list items and buttons with auto layout and one Button component with three variants.

!!! example "Lab 2 · Clickable prototype and usability test (30 minutes)"
    1. Connect the three screens in the Prototype tab.
    2. Present and share the link.
    3. Test with two people using the think-aloud method. Note where they hesitate.

!!! example "Lab 3 · FigJam affinity map (30 minutes)"
    1. Open a FigJam affinity-map template.
    2. Paste 20 interview quotes as stickies (use Class 14 Lab 2 output).
    3. Group them into themes, name each theme, and vote on the top two.

!!! example "Lab 4 · Figma Make prototype (Free or paid, 30 minutes)"
    1. Open Figma Make, attach your three frames.
    2. Ask for a working prototype with live total recalculation.
    3. Add one edge case, then share the link.

!!! example "Lab 5 · Claude Code builds from Figma (Professional, 40 minutes)"
    1. Follow Figma's MCP guide to add the server to Claude Code.
    2. Copy the link to your Bill frame.
    3. Ask Claude Code: "Implement this frame as a responsive HTML page."
    4. Compare with the design and ask for fixes until it matches.

## PM best practices

* **Low fidelity first**: boxes and real copy before colour and polish.
* **Design the states**, not just the happy path.
* **Name layers and frames** so engineers and AI tools understand them.
* **Comment, don't redesign**: describe the problem; let the designer solve it.
* **Keep one source of truth**: link the Figma file in the PRD, and the PRD in the Figma file.

## Exercises with model answers

!!! question "Exercise · What to use"
    (a) Run a 45-minute remote workshop to sort 60 interview quotes. (b) Show a stakeholder how the split-bill calculation behaves with three people. (c) Hand a finished screen to engineering.

??? answer "Model answer"
    (a) **FigJam** affinity map. (b) **Figma Make** (a click-through prototype can't calculate). (c) Mark the frame **Ready for dev** in **Dev Mode**, and optionally let engineers use the **MCP server** with their coding agent.

## Key takeaways

* **Frames, auto layout and components** are the three skills that make Figma easy.
* **Prototype and test** before building. **FigJam** is your workshop room.
* **Figma Make** turns designs into working prototypes; the **MCP server** lets Claude Code build from your frames.

## Check your understanding

```quiz
- q: "Which feature makes a list of cards keep consistent spacing as items change?"
  options:
    - "Comments"
    - "Auto layout"
    - "Dev Mode"
    - "FigJam stamps"
  answer: 1
  why: "Auto layout stacks items with fixed gaps and padding and resizes with content."
- q: "You need to show a live calculation in a prototype. Use…"
  options:
    - "A click-through prototype"
    - "Figma Make"
    - "A FigJam board"
    - "A PDF export"
  answer: 1
  why: "Figma Make writes working code, so values can be calculated."
- q: "What gives Claude Code direct access to a Figma frame's layout and variables?"
  options:
    - "Exporting a PNG"
    - "The Figma MCP server"
    - "A Slack message"
    - "Figma Slides"
  answer: 1
  why: "The MCP server exposes design context to AI coding tools."
```

## Recommended resources

* [Figma Help Center](https://help.figma.com) · [Figma pricing](https://www.figma.com/pricing/)
* [Figma MCP server collection](https://help.figma.com/hc/en-us/articles/35280808976151-Figma-MCP-collection-Overview)
* [Figma's official YouTube channel](https://www.youtube.com/@Figma) and Figma Community UI kits
* Module 5 (UX and design collaboration) for the theory behind these labs

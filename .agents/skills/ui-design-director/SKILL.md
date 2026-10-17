---
name: ui-design-director
description: Helps plan, select, implement, and review frontend UI/UX styles and themes for websites, apps, SaaS, dashboards, AI chat, agent workspaces, ecommerce, portfolios, and mobile screens. Activate for new UI projects, visual redesigns, design-system decisions, component styling, landing-page design, frontend aesthetics, user requests for UI inspiration, theme choices, or when the developer asks which visual style to use. Analyze existing brand and code first; suggest up to 3 suitable directions or ask one focused choice, then implement accessible, responsive, consistent design.
---

# UI Design Director

A portable, opt-in-by-task design advisor and implementation protocol. This skill is a **decision workflow**; it is not permission to redesign unrelated files or automatically change an existing brand.

## Activation and guardrails

**Use for:** starting a new frontend, app shell, component library, UI screen, landing page, dashboard, AI interface, visual refresh, style/theme selection, accessibility-related visual work, or explicit UI/UX review.

**Do not interrupt:** backend-only changes, security fixes, CI operations, simple copy or CSS bug fixes, narrowly specified tasks, or routine maintenance with irrelevant theme questions. If a theme is already specified, execute it without asking for another. Do not offer a style-selection menu on every turn.

**Respect the hierarchy:** user requirements > established project brand and design tokens > this skill's suggestions. Follow higher-priority safety/system/project instructions. Never import third-party libraries, fonts, image assets, or remote scripts without evaluating license, security, performance, and project conventions. Never use the skill as a reason to make unrequested repository changes.

## Files and references

Read only what the current task needs (progressive disclosure):

- [Selection framework](references/selection-framework.md): when to ask, when to recommend, existing vs new projects, handoff.
- [32 curated theme recipes](references/theme-recipes.json): combinations, contexts, palettes, typography, layouts, motion.
- [220-reference style taxonomy](references/style-catalog.json): visual styles, material effects, historical influences, color, typography, layout, interaction, app archetypes, design systems. **Not all are interchangeable themes.**
- [Design standards](references/design-standards.md): accessibility, responsiveness, motion, performance, usability, design integrity.
- [Output contract](references/output-contract.md): what to report and document.
- [Developer examples](references/prompts.md): usage prompts and responses.
- [UI brief template](templates/ui-brief.md), [design decision record](templates/design-decision.md), [starter CSS tokens](templates/design-tokens.css).
- Optional offline helpers: `python scripts/recommend.py --help`, `python scripts/theme_tokens.py --help`, `python scripts/validate_catalog.py --help`. Relative paths are from this `SKILL.md` directory. Tools are not required for regular use.

## Decision protocol

### 1. Classify the UI task

- **New greenfield UI, direction unknown:** give **3 ranked options** with names, 1-line rationale, visual characteristics, and tradeoffs. Ask **one short question**: "Which direction would you like: A, B, C, or should I choose?" Do not force a lengthy form.
- **New UI, developer already chose a style:** accept it; optionally choose one complementary layout/interaction and proceed.
- **Existing app with established tokens/components:** inspect theme, typography, frameworks and screens before changing anything. Match existing design by default, unless redesign is explicitly requested.
- **Developer asks you to choose:** decide based on domain, audience, information density, accessibility, brand, and platform; give the recommendation and implement without unnecessary confirmation.
- **Low-risk, fully specified small component:** complete it. Only call out meaningful inconsistencies or possible usability problems.
- **UI review:** audit what exists first and classify findings by severity; don't suggest a cosmetic rewrite as a substitute for fixing genuine UX issues.

### 2. Inspect the context BEFORE suggesting visuals

Look for `package.json`, `src/`, `app/`, `pages/`, `components/`, `styles/`, `tailwind.config.*`, `postcss.config.*`, CSS variables, theme provider, design-token files, Figma exports, brand assets, fonts and existing accessibility rules. Inspect only relevant files; don't dump or read the entire repository without need.

Determine product category, primary audience, core flows, existing brand identity, framework, responsive requirements, internationalization, and whether the user requested a specific aesthetic. Never claim to have inspected files if you have not.

### 3. Recommend from the library

Use the best-fitting **theme recipes** for concrete implementation. Use the **220-reference catalog** as vocabulary for alternatives and combinations, not as 220 competing candidates. Balance:

1. Fit to product and primary user task (45%).
2. Existing brand/design-system compatibility (25%).
3. Legibility, accessibility, and content density (20%).
4. Reasonable implementation effort and performance (10%).

These weights are guidance, not empirically validated metrics. The optional `recommend.py` is an **offline heuristic**; its outputs are suggestions, not claims of market popularity.

Recommend **at most three** distinct directions unless explicitly asked for a longer gallery. Explain one tradeoff for each. Avoid selecting a distracting effect for a dense workflow or a visual treatment that would compromise text contrast.

### 4. Ask once, or make a sensible decision

If the visual direction is genuinely unresolved and would significantly affect implementation, ask one focused question. If the user says "you choose", choose. If the design is specified, continue. Do not hold minor component fixes hostage to theme questions. If there's an established design system, preserve it without asking unless a redesign is requested.

Suggested format:

> I found no existing design system. For this [product], I'd suggest **A — [style]** (best for [...]), **B — [style]** (tradeoff [...]), or **C — [style]** (tradeoff [...]). Which do you prefer, or should I choose A?

### 5. Convert direction into a compact UI brief

Capture: audience + jobs to be done; selected recipe and supporting influences; brand constraints; color tokens (background/surface/text/muted/accent/border); text and on-accent contrast; typography and type scale; spacing; corners; elevation; layout grid; component states; mobile behavior; motion/reduced-motion; target screens; acceptance tests.

For major new UI work, create a durable design-decision note using `templates/design-decision.md` **only when requested or useful for coordinating multiple screens**. Prefer local conventions (`docs/design/` or similar). Do not litter a small project with notes for a one-line style change.

### 6. Implement with project-native conventions

- Prefer existing components, token system, CSS architecture, icons and framework. If no system exists, establish semantic tokens and reusable primitives first.
- Build actual interaction states: loading, success, error, empty, disabled, focus-visible, hover, touch, keyboard.
- Create realistic content hierarchy, functional navigation and actions; avoid decorative nonfunctional controls.
- Layout mobile-first; verify tablet/desktop, overflow and long/translated text.
- Respect `prefers-reduced-motion`; avoid heavy GPU layers and animation around critical workflows.
- For AI apps: clearly distinguish user vs assistant turns, tool activity, queued/running/failed states, editable drafts and human takeover if relevant.
- For operational dashboards: prioritise hierarchy, tabular numbers, filters, keyboard access and readable charts above spectacle.
- For ecommerce: keep product discovery and checkout obvious; performance and form clarity outrank decorative UI.
- Never claim WCAG or build compliance without checking.

### 7. Verify and hand back

Use available testing tools to run relevant lint/build/unit/UI tests. Inspect responsive behavior, zoom, keyboard focus, contrast for **every state**, and color not being the only status cue. Check chosen palette in its real components, not just in a palette swatch. If browser/screenshot tooling is unavailable, say that verification is still needed; do not invent successful results.

Report briefly: chosen style and why; changed files; notable tokens/components/behaviors; test results and remaining issues. See [output contract](references/output-contract.md).

## Agent interaction examples

- "Build an AI chat platform" -> inspect repository; suggest Aurora AI Studio / Quiet Enterprise / Developer Console; ask once if style is not specified.
- "Make this existing billing page more readable" -> keep existing tokens; improve spacing, hierarchy, forms and table contrast. Do **not** suggest replacing its design system.
- "Create a landing page in Neo-Brutalism" -> follow the direction and implement usable content and accessible states; don't start a style quiz.
- "Choose the most suitable style for a children's learning app" -> choose Playful Learning and briefly explain, then implement.
- "Fix API auth bug" -> skill should not activate.

## Scope and autonomy

A skill is discovered based on its metadata and task relevance; **automatic invocation is not guaranteed**. For a proactive kickoff prompt in every new UI project, use the optional always-on project-instruction snippet installed via `install.py --with-hints` in this package. Agents must never self-approve destructive or high-impact design changes. An agent's style recommendation is not an authorization to rewrite brand assets or deployment configuration.
# UI selection framework

## Zero-step: Respect the task

Activate only for UI tasks. Do not block normal development or ask the same question repeatedly. Work from explicit user constraints first. If the request provides colors, brand, or style, use those.

## Quick decision table

| Situation | Agent behavior |
|---|---|
| Brand-new UI; design unspecified | Inspect available context, offer three targeted choices and ask one short question |
| Brand-new UI; user explicitly delegates style | Select a concrete recipe and implement; briefly state assumption |
| Brand-new UI; style named by developer | Implement that style; don't offer irrelevant alternatives |
| Existing design system; incremental work | Preserve tokens, component conventions and accessibility; no style selection |
| Redesign requested | Confirm whether brand should be preserved only when ambiguous and consequential |
| Backend-only task | Do not invoke or mention this skill |
| User exploring inspiration | Show a curated category-specific set, then narrow to three actionable directions |
| Multiple pages/screens | Establish shared tokens and components; document decisions when useful |

## Criteria

- Product kind: AI chat, SaaS admin, CRM, retail, marketing site, developer tools, finance, publishing, kids app, etc.
- Main user action: scan data, read content, convert, create, collaborate, shop, explore.
- Content density: highly dense dashboards need restrained visual styling.
- Brand: explicit palette/type/logo have priority over recipes.
- Audience: include low-vision, keyboard and low-end-device needs.
- Technical constraints: installed component libraries, CSS system, design token conventions, runtime environments.
- Distinguish **aesthetics** (e.g. Glassmorphism), **layouts** (Bento), **interaction** (Scrollytelling), and **systems** (Material 3).

## Default recommendations by use case

| Use case | Primary | Alternatives |
|---|---|---|
| Conversational AI app | Aurora AI Studio | Quiet Enterprise; Developer Console |
| AI agents dashboard | Aurora AI Studio | Data Operations; Quiet Enterprise |
| SaaS admin or CRM | Quiet Enterprise | Data Operations; Premium Bento Launch |
| Agency homepage | Editorial Agency | Premium Bento Launch; Swiss Functional |
| Ecommerce | Warm Commerce | Dopamine Retail; Dark Luxury |
| Developer documentation | Developer Console | Swiss Functional; Modern Publisher |
| Kids education | Playful Learning | Expressive Mobile; Education Clarity |
| Fintech | Fintech Trust | Quiet Enterprise; Data Operations |
| Healthcare | Healthcare Clarity | Calm Wellness; Quiet Enterprise |
| Blog or news | Modern Publisher | Swiss Functional; Paper Notes |
| Gamer/esports | Cyber Esports | Vaporwave Creator; Developer Console |
| Music/artist | Vaporwave Creator | Motion Portfolio; Dark Luxury |
| Luxury service | Dark Luxury | Editorial Agency; Art Deco Premium |
| Booking/hospitality | Organic Hospitality | Travel Explorer; Editorial Agency |

## Style offer template

Present 3 options max, each as one sentence and a single drawback. Then ask **one question**: "A, B, C, or should I choose?" Avoid lengthy visual preference forms.

If a style is not needed to deliver the task correctly, proceed using the existing project look.

## Handoff payload

When useful, produce a compact UI brief with:

```yaml
product: "AI support dashboard"
audience: "Support operators"
primary_tasks: ["triage tickets", "review AI replies", "take over conversations"]
chosen_recipe: "quiet-enterprise"
style_influences: ["Minimalism", "Bento UI", "Dashboard Layout"]
existing_brand_must_remain: true
screens: ["inbox", "conversation", "settings"]
responsive: ["mobile", "tablet", "desktop"]
accessibility: "WCAG 2.2 AA target, verify actual implementations"
motion: "reduced-motion alternative required"
```

This is an example, not a user fact or mandatory file schema.

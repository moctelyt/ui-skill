# Skill usage prompts

## Trigger naturally

- "Create an onboarding dashboard for my AI startup. Suggest styles before you code."
- "Build an e-commerce landing page. Pick a suitable UI direction."
- "I want a modern SaaS UI but I don't know its theme. Present three choices."
- "We're creating a children's learning app; pick a playful visual design that remains accessible."
- "Audit our existing component library and improve its coherence without rebranding it."

## Explicit invocation

- "Use the ui-design-director skill to recommend three styles for a real-estate website."
- "Use ui-design-director. The theme is already selected: editorial minimalism. Build it."
- "Use ui-design-director to create an accessible design decision brief."

## Developer response examples

**User:** "Start a new AI chat app."

**Agent:** "For a conversational AI workspace, I recommend A — Aurora AI Studio (expressive but can become visually busy), B — Quiet Enterprise (best for high-density workflows, less distinctive), C — Developer Console (great for technical users, potentially too utilitarian). Which direction do you prefer, or should I choose A?"

**User:** "Build it. You choose."

**Agent:** "I'll use Aurora AI Studio with subdued aurora backgrounds and readable message surfaces. I'll first inspect the existing project and reuse its UI stack."

**User:** "Update the Save button on our current admin panel."

**Agent:** "I'll match the existing component system and improve its focus, disabled and saving states." *(No theme question.)*

## Optional CLI assistance

```bash
python scripts/recommend.py --project "AI chat dashboard" --mood "premium dark" --top 3
python scripts/recommend.py --project "kids education app" --top 3 --json
python scripts/theme_tokens.py --list
python scripts/theme_tokens.py --recipe aurora-ai
python scripts/validate_catalog.py
```

All scripts use only the Python standard library. `theme_tokens.py` prints CSS by default and writes only with an explicit `--output` path.

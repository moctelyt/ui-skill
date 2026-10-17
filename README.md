# UI Design Director

**An installable Agent Skill for Codex, Google Antigravity, VS Code Copilot, and supported Visual Studio Copilot.**

Provides a cross-agent process to inspect the frontend, propose appropriate visual directions, obtain developer choice only when needed, implement a coherent design system and verify functionality, responsive behavior and accessibility. Includes:

- **220 UI references** in 10 correctly distinguished categories: visual styles, effects, historical aesthetics, mood, colors, typography, layout, interaction, application archetypes and established systems.
- **32 actionable theme recipes** with practical combinations, palettes, typography, layouts, audiences and motion guidance.
- `SKILL.md` with rules for **ask / suggest / implement / review** and preserving existing apps.
- Offline Python recommendation CLI, CSS theme-token generator and contrast/catalog validator; no dependencies beyond Python 3.9+.
- Optional always-on trigger hints for `AGENTS.md` and `.github/copilot-instructions.md` (only if opted in).
- A local visual explorer to filter styles and inspect recipe palettes.

> **Important:** Agent skills are context-dependent and auto-invocation is **not guaranteed**. Enable optional project hints to improve proactive use, or explicitly ask the assistant to use the skill. This package does **not** install an editor extension or guarantee a popup in the IDE.

## 1. Installation: per project or globally

Extract the ZIP somewhere **outside** the target project's repo. In a terminal, from the extracted folder, choose **one** approach.

**Option A — Global installation for your local coding agents:**

```bash
python install.py --scope global
```

This installs two **personal** skill copies: `~/.agents/skills/ui-design-director/` (Codex, VS Code and Visual Studio) and `~/.gemini/config/skills/ui-design-director/` (Antigravity). It does not modify any repository or global agent instruction files. Your agents can discover the skill in new local projects according to their normal discovery behavior.

**Option B — Install into a specific team project:**

```bash
# macOS/Linux/Windows with Python; point to the root of your actual codebase
python install.py --target /path/to/your-project --with-hints
```

Windows PowerShell example:

```powershell
python .\install.py --target "C:\path\to\your-project" --with-hints
```

`--with-hints` is only for project installation. It appends or refreshes a marked, brief instruction block inside `AGENTS.md` and `.github/copilot-instructions.md` **without replacing other content**. If you don't want to modify these files, omit this flag.

Safe options:

```bash
python install.py --scope global --dry-run
python install.py --target /path/to/your-project --dry-run --with-hints
python install.py --target /path/to/your-project --force --with-hints
```

`--force` first **backs up** an existing skill folder before replacing it. By default, the installer refuses to overwrite an existing installation. For global updates, use `python install.py --scope global --force`. It does not modify source-code files, package manifests, or editor settings.

## 2. Shared skill discovery

| Agent platform | Project skill path | Notes |
|---|---|---|
| **OpenAI Codex** | `.agents/skills/ui-design-director/SKILL.md` | User scope: `~/.agents/skills/`. |
| **Google Antigravity IDE/app** | `.agents/skills/ui-design-director/SKILL.md` | User scope: `~/.gemini/config/skills/`; legacy project `.agent/skills` still recognized. |
| **VS Code GitHub Copilot** | `.agents/skills/ui-design-director/SKILL.md` | User scope: `~/.agents/skills/`; also supports project `.github/skills`. |
| **Visual Studio 2026 Copilot** | `.agents/skills/ui-design-director/SKILL.md` | User scope: `~/.agents/skills/`; requires Visual Studio 2026 **18.5+** and Copilot subscription. |

All four can use the same directory when the relevant agent-skills capability is available. Restart the IDE/agent conversation if the skill was installed while running. In VS Code, `/skills` can help inspect discovered skills.

### How to invoke it

**Automatic (task-matched):** "Create a new AI dashboard" or "Redesign this landing page" may activate the skill based on the skill description. Invocation varies by platform.

**Explicit (recommended for initial testing):**

```text
Use the ui-design-director skill. Review this repository and propose three UI directions for our app before making any design changes.
```

**Delegate the selection:**

```text
Use ui-design-director. Choose the best visual style for this CRM dashboard, keep the existing brand, and implement an accessible responsive UI.
```

**Existing UI without rebranding:**

```text
Use ui-design-director to improve the existing settings page. Preserve the current theme and component system.
```

## 3. Architecture

```text
ui-design-director/
├── README.md
├── LICENSE
├── install.py                           # non-destructive repository installation
├── .agents/skills/ui-design-director/
│   ├── SKILL.md                         # agent entrypoint and decision behavior
│   ├── references/
│   │   ├── style-catalog.json           # 220 references in 10 categories
│   │   ├── theme-recipes.json           # 32 curated recipes and semantic colors
│   │   ├── selection-framework.md       # how and when to recommend/ask
│   │   ├── design-standards.md          # usability/accessibility/responsiveness
│   │   ├── output-contract.md           # consistent agent handoff
│   │   └── prompts.md                   # example developer conversations
│   ├── scripts/
│   │   ├── recommend.py                 # offline theme recommendation heuristic
│   │   ├── theme_tokens.py              # print or export starter CSS tokens
│   │   └── validate_catalog.py          # data integrity and core color contrast
│   └── templates/
│       ├── ui-brief.md
│       ├── design-decision.md
│       └── design-tokens.css
├── explorer/index.html                  # searchable visual reference and swatches
└── tests/test_skill.py                  # offline smoke tests
```

## 4. Typical lifecycle

1. **Recognize** new UI work from task description; don't interrupt backend-only work.
2. **Inspect** current framework, tokens, brand, components and existing screens.
3. **Recommend** 3 suitable visual directions with tradeoffs if the style is unknown.
4. **Ask once** for A/B/C or delegated choice only if style is consequential and unresolved.
5. **Implement** selected direction using native project conventions, semantic tokens and complete component states.
6. **Verify** build, keyboard, mobile, responsive behavior, contrast, reduced-motion, feedback and error states.
7. **Report** chosen direction, actual changes, tests performed and unverified items.

## 5. Offline assistant scripts

Use these from the installed skill folder or from the package itself:

```bash
cd .agents/skills/ui-design-director
python scripts/recommend.py --project "AI chat dashboard" --mood "premium dark" --top 3
python scripts/recommend.py --project "ecommerce fashion" --json
python scripts/theme_tokens.py --list
python scripts/theme_tokens.py --recipe aurora-ai
python scripts/theme_tokens.py --recipe aurora-ai --output /tmp/aurora-ui.css
python scripts/validate_catalog.py
```

The ranking is a **simple reproducible keyword heuristic**, not a measured trend or marketing claim. It suggests options; the agent must still inspect the project and consider visual, technical and human needs. The theme generator provides **starter tokens**, not a certified accessible design. Colors were validated for base/foreground combinations and must be retested in real interfaces.

## 6. Visual explorer

Open `explorer/index.html` locally in any modern browser. Filter the 220 styles by category and text search, inspect 32 recipe palettes, and copy starter prompts. It does not fetch data or require a backend.

## 7. Quality and safety

- Never force a new theme on an established UI when the developer only requested a small fix.
- Never auto-install dependencies or external assets simply because a recipe mentions an aesthetic.
- Never assume a decorative trend fits every audience. Dense, clinical, financial and operational workflows prioritize comprehension.
- Honor accessibility goals (WCAG 2.2 AA where applicable), keyboard behavior, reduced motion, responsive usability, performance and source license.
- Don't claim a preview was tested unless tools actually rendered it.

## 8. Local tests

```bash
python -m unittest discover -s tests -v
python .agents/skills/ui-design-director/scripts/validate_catalog.py
```

## Official references (verified October 2026)

- Codex / VS Code: https://code.visualstudio.com/docs/agents/guides/customize-copilot-guide
- Antigravity: https://www.antigravity.google/docs/skills?tab=ide
- VS Code: https://code.visualstudio.com/docs/agent-customization/agent-skills
- Visual Studio: https://learn.microsoft.com/en-us/visualstudio/ide/copilot-agent-skills?view=visualstudio
- OpenAI skills overview: https://github.com/openai/skills
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

### License

MIT. No fonts or third-party images are bundled. Recipe descriptions and names are original guidance; named design systems remain trademarks of their owners.
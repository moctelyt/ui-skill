# Frontend design standards checklist

Apply relevant items to the actual product; this is not a substitute for testing.

## Accessible visuals

- Target WCAG 2.2 AA where applicable. Test text contrast **at least 4.5:1 for normal text and 3:1 for large text**; disabled/inactive text has exceptions but should remain understandable.
- Visual boundaries for important interactive components and meaningful nontext indicators generally need **3:1 non-text contrast** against adjacent colors.
- Provide visible keyboard focus, semantic labels, logical tab order and keyboard-operable dialogs, menus and forms.
- Minimum WCAG 2.2 AA pointer target **24 x 24 CSS px** or appropriate spacing exceptions; prefer larger comfortable touch targets, e.g. 44 x 44 where practical.
- Never use color alone for status; pair with labels/icons/patterns. Provide visible error guidance and status messages.
- Keep readable typography at 200% zoom and responsive reflow for narrow screens when applicable.
- `prefers-reduced-motion` should suppress decorative transitions, parallax, rapid zoom and constant movement. Avoid seizures-inducing flashes.
- Don't place readable text across low-contrast photographs, glass, neon, gradients or overlays without robust backing.

## Layout and performance

- Design mobile-first, then test tablet, laptop and wide desktop. Check 320px-ish narrow viewports, long content, localized strings, forms and overflowing tables.
- Use a semantic typographic scale, consistent spacing tokens (e.g. 4/8-based) and reusable layout patterns.
- Avoid layout shifts: provide image dimensions/aspect-ratios and stable skeletons. Lazy-load noncritical assets.
- Prefer CSS and lightweight vector art to heavy visual engines; use WebGL/3D only for justified goals with fallback.
- Preserve readable line lengths for long-form body content (~45–85 characters, context-dependent).
- Responsive navigation must be operable without hover. Avoid hover-only essential controls.

## Component specification

Each major component has: default, hover where applicable, focus-visible, active/pressed, disabled, loading, error, success, empty and high-contrast semantics. Don't require every state where logically irrelevant.

## Product-specific rules

- **Dashboards:** status first, meaningful data labels, clear ranges and units, data tables with headers and sortable semantics.
- **AI chat:** role differentiation, streaming and loading feedback, retry/error paths, citation/tool transparency if available, and user control over actions.
- **Forms/checkout:** explicit validation, no surprise totals, accessible autocomplete, clear confirmation and safe retry semantics.
- **Marketing:** the offer, evidence and primary CTA must remain obvious; visual effects must not block content.
- **Children:** age-appropriate readability and controls, avoid manipulative engagement design.

## Verification sequence

1. Run existing lint/typecheck/build and relevant tests when possible.
2. Review mobile, tablet and desktop layouts in browser/device tooling when available.
3. Keyboard-only traverse key flows; confirm visible focus and correct modal trapping/return focus.
4. Run contrast checks for key surfaces/text, states and overlays; test light/dark separately.
5. Check reduced motion, zoom, overflow, long strings, empty/error/loading scenarios.
6. Report test outcomes accurately; if manual browser testing was unavailable, list it as remaining verification.

Useful authoritative references: https://www.w3.org/TR/WCAG22/ and https://www.w3.org/WAI/ .

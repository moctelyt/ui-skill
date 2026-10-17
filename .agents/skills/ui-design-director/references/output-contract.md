# Agent output contract

## When asking the developer to choose

Provide:

1. One sentence acknowledging the actual product and its audience.
2. Three ranked visual directions: title, concise rationale, and one tradeoff each.
3. A single question: "Which direction do you want: A, B, C, or should I choose?"

Do not dump the 220-item style library unless asked. Do not ask multiple independent questions as a gate to normal work.

## When proceeding with a direction

Keep design recommendations compact. For larger implementations, state:

- **Direction:** selected recipe and supporting style/layout influences.
- **Reason:** fitness for audience, information density, brand and task.
- **Tokens:** background, surface, text, muted text, accent, border; typography and spacing.
- **Blueprint:** components/screens and key responsive behaviors.
- **States:** loading, empty, errors, focus, motion reduction.
- **Validation:** what will be run and what will require human visual inspection.

## Completion report

```text
UI direction: [chosen and reason]
Files changed: [paths]
Implemented: [screens / components / interactions]
Validation: [command/result and tested UI states]
Remaining: [unverified areas or known issues]
```

Never claim user approval until received; never claim screenshot or accessibility validation that did not happen.

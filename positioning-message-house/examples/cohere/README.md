# Worked example: a message house for Cohere

> **Real company, public data, illustrative.** Built from the repo's own Cohere ICP and voice
> guide; not an official Cohere document.

The fifth run on the Cohere spine. The ICP supplied the demand-side truth (the security gate as
the structural veto), the voice guide constrained every cell (possessive contrast, plain over
jargon, the Avoid list), and the generation system is a real script.

| File | What it is |
|---|---|
| `message-house.md` | The human document: the security-gate bet with its falsifier, three pillars, the 12-cell matrix, the spine, the pressure-test |
| `house.json` | The structure: every cell with its committee audience, when-we-win / when-we-lose, objections mapped to pillars |
| `battlecard.md` | Generated: bet, pillars with proof, when-we-lose included on purpose, objection table |
| `objection-handling.md` | Generated: each objection with the role that raises it and the pillar the response stands on |

## Reproduce the assets

```
python3 ../../scripts/generate_assets.py house.json
```

Deterministic: edit the house, regenerate, and the battlecard cannot drift from the positioning.

## The two judgment moments

- **The bet is falsifiable and the falsifier is named:** if hyperscaler residency promises clear
  security reviews at high rates, the category bet weakens to a feature, and the house says so.
- **When-we-lose ships in the battlecard:** public-API-comfortable buyers and
  general-purpose-primary seekers are named as losses, straight from the ICP's disqualifiers,
  because a battlecard that never loses is not believed.

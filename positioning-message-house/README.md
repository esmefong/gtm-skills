# Positioning Message House

Turn positioning into an operating system for messaging: one falsifiable category bet, two to
three pillar messages, and a matrix that translates them into each go-to-market function's
language at their moment in the buyer's journey.

## What it does

Consumes the ICP from [`icp-research`](../icp-research/) (triggers, committee, decision criteria,
barriers) and the voice from [`brand-voice-guide`](../brand-voice-guide/), then builds:

1. **The bet:** one falsifiable claim about where the category is going, grounded in the ICP's
   demand-side reality, with the falsifier and the settling metric named.
2. **The pillars:** two or three messages in the brand voice, each with proof.
3. **The matrix:** the same messages translated per function (marketing, sales, product, customer
   success) at their buyer-journey moments, each cell addressed to a named committee role.
4. **The generated assets:** `scripts/generate_assets.py` (stdlib-only) emits the battlecard and
   objection-handling doc from the structured house, so downstream assets cannot drift from the
   positioning.

The principle underneath: **consistency comes from everyone standing on the same
messages; specificity comes from translation, not from four teams inventing four stories.**

## What it does NOT do

No platitude bets (if nobody could argue the opposite, it is not a bet), no cells that invent new
claims, and no battlecards that never lose: `when_we_lose` is a required field, sourced from the
ICP's disqualifiers, and the generator refuses a house without it.

## Who it's for

Product marketers, founders, and GTM teams whose functions each tell their own version of the
story, and who need one narrative that survives contact with the whole buying committee.

## How to use it

1. Copy this folder into `~/.claude/skills/positioning-message-house/`.
2. Point it at your ICP and voice: *"Build a message house for us."* It names the bet, shows you
   the pillars before translating, fills the matrix committee-aware, and generates the assets.
3. Regenerate assets anytime:

```
python3 scripts/generate_assets.py house.json
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and five-phase workflow |
| `references/output-template.md` | The house.json schema, the document format, the translation quality bar |
| `scripts/generate_assets.py` | Deterministic battlecard + objection-doc generator |
| `examples/cohere/` | The full house for Cohere: the security-gate bet, three pillars, a 12-cell matrix, and the generated assets |

## Composes with

- [`icp-research`](../icp-research/): the bet's grounding, the committee each cell addresses, the
  disqualifiers behind when-we-lose.
- [`brand-voice-guide`](../brand-voice-guide/): every pillar and cell obeys the voice's writing
  standard.
- [`outbound-engine`](../outbound-engine/): sequences draw their middle arguments from the same
  pillars, so outreach and positioning stay one story.

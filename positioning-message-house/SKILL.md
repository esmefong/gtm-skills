---
name: positioning-message-house
description: >
  Build a positioning message house for a company: one falsifiable category bet, two to three
  message pillars, and a translation matrix that carries the same messages across go-to-market
  functions (marketing, sales, product, customer success) at their buyer-journey moments, plus a
  generation system that emits battlecards and objection-handling docs from the structured house.
  Consumes the ICP from icp-research (triggers, committee, decision criteria, how-to-win) and the
  voice from brand-voice-guide. Use whenever the user says "message house", "messaging framework",
  "positioning framework", "messaging matrix", "core narrative", "category narrative", "align our
  messaging", "battlecard", or wants one story translated across teams instead of four teams
  inventing four stories.
---

# Positioning Message House

Turn positioning into an operating system for messaging: one category bet everyone stands on, a
small set of pillar messages, and a matrix that translates them into each function's language at
their moment in the buyer's journey. The whole design enforces one principle: **consistency
comes from everyone standing on the same messages; specificity comes from translation, not from
four teams inventing four stories.**

The output is structured, so the downstream assets (battlecards, objection docs) are generated
from the house rather than drifting away from it.

## What this consumes

| Input | From | What it provides |
|---|---|---|
| ICP | `icp-research` (`icp.md`) | Triggers, buying committee, decision criteria, barriers, how-to-win |
| Voice directory | `brand-voice-guide` | Tonal pillars and the writing standard every cell obeys |
| Offerings list | The user, or the ICP's product context | What the pillars stand on |

No ICP? Gather the minimum first: the bet must be grounded in a demand-side truth, not invented in
a workshop. No voice guide? Draft plain and say so.

## The workflow

Five phases. Show the user the bet and pillars (end of Phase 2) before translating the matrix.

### Phase 1: Load and frame

Read the ICP and voice. Pull the raw material the house is built from: the primary trigger
(why buyers move), the committee (who must hear what), the decision criteria (what they weigh),
the barriers (what the messaging must answer), and the how-to-win section if present.

### Phase 2: Name the bet, then the pillars

**The category bet** is one falsifiable claim about where the category is going and where this
company must stand. The quality bar: someone credible could argue the opposite. "AI will transform
our industry" is a platitude; "the category will be won at the security gate, not the benchmark"
is a bet. Ground it in the ICP's demand-side reality and name what would falsify it.

**The pillars** are two or three messages, each one sentence in the brand voice, each carrying
proof. More than three and the house becomes a brochure.

### Phase 3: Translate the matrix

For each pillar, write one cell per function at that function's buyer-journey moment:

| Function | Moment | The cell answers |
|---|---|---|
| Marketing | Awareness / consideration | Why should the buyer care now? (the trigger) |
| Sales | Objection / evaluation | What does the skeptic in the room need to hear? (the committee's barriers) |
| Product | Roadmap / activation | What must the product visibly do to keep the message true? |
| Customer success | Retention / expansion | How does the message continue after the sale? |

Rules: every cell is the *same message translated*, never a new claim; cells speak to the
committee roles from the ICP (the sales row answers the economic buyer and the gatekeeper, not
just the champion); every cell obeys the voice's writing standard.

### Phase 4: The spine and the honest assessment

Write the **spine**: one short section on why the house holds together and which shared buying
moment every function serves. Then the **pressure-test**: what would falsify the bet, which
pillar is weakest and why, and the one metric that would settle it. A message house without a
falsifier is a poster.

### Phase 5: Generate the downstream assets

Encode the house as `house.json` (`references/output-template.md`) and run
`scripts/generate_assets.py`: it emits the battlecard (bet, pillars with proof, when-we-win /
when-we-lose, objection responses) and the objection-handling doc, deterministically, from the
same structure. Assets generated from the house cannot drift from it; that is the point.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/generate_assets.py` | Emits battlecard.md and objection-handling.md from house.json | None | None |

## Failure modes to avoid (the quality bar)

- **A platitude bet.** If no credible person would argue the opposite, it is not a bet.
- **Invention instead of translation.** A matrix cell that introduces a new claim breaks the
  spine; four stories is the disease this skill treats.
- **Champion-only messaging.** The sales row must answer the veto holders and the economic buyer;
  the ICP committee says who they are.
- **Feature lists in cells.** Every cell is a message with a reader, not a capability inventory.
- **Voice drift.** Cells obey the brand's writing standard; hype words that fail the voice fail
  the house.
- **No falsifier.** The pressure-test section is required, with the win/loss metric named.
- **When-we-lose left out.** The battlecard states where the company loses, from the ICP's
  disqualifiers. Pretending otherwise reads as marketing to the exact people this must convince.

## Bundled references

- `references/output-template.md`: the house.json schema, the message-house document format, and
  the translation quality bar. Read at Phases 3-5.
- `examples/cohere/`: the full house for Cohere built from the repo's own ICP and voice: the
  security-gate bet, three pillars, a 12-cell matrix, and the battlecard and objection doc the
  script generated from it.

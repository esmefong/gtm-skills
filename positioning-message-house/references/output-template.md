# Output template

Three artifacts: the human document (`message-house.md`), the structure (`house.json`), and the
generated assets (`battlecard.md`, `objection-handling.md`) that `scripts/generate_assets.py`
emits from the structure. Edit the house, regenerate the assets; never edit the assets.

## `house.json` (the structure)

```json
{
  "generated": "2026-07-21",
  "brand": "Cohere",
  "icp_source": "icp-research/examples/cohere/icp.md",
  "bet": {
    "claim": "One falsifiable sentence about where the category is going and where we stand.",
    "grounding": ["The ICP or evidence lines the bet rests on"],
    "falsifier": "What observation would prove the bet wrong",
    "metric": "The number that settles it"
  },
  "pillars": [
    {
      "id": "pillar-id",
      "name": "Short name",
      "message": "One sentence, in the brand voice.",
      "proof": ["Named, dated proof points"]
    }
  ],
  "matrix": [
    {
      "pillar": "pillar-id",
      "function": "marketing | sales | product | customer-success",
      "moment": "awareness | evaluation | activation | expansion",
      "audience": "which committee role this cell addresses",
      "message": "The pillar message, translated for this function and moment."
    }
  ],
  "when_we_win": ["Situations where this positioning wins, from the ICP"],
  "when_we_lose": ["Situations where it loses, from the ICP's disqualifiers. Required."],
  "objections": [
    {
      "objection": "The barrier, in the buyer's words",
      "from": "which committee role raises it",
      "response": "The answer, built from a pillar, in the brand voice",
      "pillar": "pillar-id"
    }
  ],
  "pressure_test": ["What to test, which pillar is weakest, what would change the house"]
}
```

Field rules: 2-3 pillars; every matrix cell names its `audience` from the ICP committee; every
objection maps to a pillar (an objection no pillar answers means the house is missing a pillar or
the objection means the deal is out of ICP); `when_we_lose` is required and comes from the ICP's
disqualifiers.

## `message-house.md` (the human document)

```markdown
# Message house: [Brand]

[One line: built from which ICP and voice, on what date.]

## The bet
[The claim, its grounding, and its falsifier, in a short paragraph each.]

## The pillars
[Per pillar: name, the one-sentence message, proof points.]

## The matrix
[One table per pillar, or one table with pillars as columns: function rows, each cell the
translated message with its audience noted.]

## The spine
[Why the house holds: the shared buying moment every function serves; translation not invention.]

## Pressure-test
[The falsifier, the weakest pillar and why, the metric that settles it, what to test first.]
```

## The translation quality bar

A cell passes when four things are true: it is recognizably the **same message** as the pillar
(a reader could match them blind); it is written for its **moment** (an awareness cell creates
recognition, an evaluation cell answers the skeptic, an activation cell commits the product, an
expansion cell continues the story); it addresses its **named audience** from the committee; and
it survives the **voice standard** (the brand's Avoid list applies to every cell). A cell that
needs a new claim to work is not a translation, and the new claim either becomes a pillar or gets
cut.

## Generated assets

`battlecard.md`: the bet, the pillars with proof, when-we-win / when-we-lose, and the objection
table with responses. `objection-handling.md`: the objections expanded one per section, with the
role that raises each, the response, and the pillar it stands on. Both carry a generated-from
notice so nobody edits them directly.

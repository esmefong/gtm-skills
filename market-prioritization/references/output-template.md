# Output template

Two artifacts: the decision document (`prioritization.md`) and the model (`markets.json`) that
`scripts/prioritize.py` scores and stress-tests. Keep the model with the document so any ranking
can be re-derived and re-argued.

## `markets.json` (the model)

```json
{
  "generated": "2026-07-21",
  "brand": "Cohere",
  "constraint": "Two markets can be resourced with dedicated GTM capacity over the next 4 quarters.",
  "icp_source": "icp-research/examples/cohere/icp.md",
  "criteria": [
    {
      "id": "buying_readiness",
      "family": "access",
      "weight": 20,
      "inverted": false,
      "rationale": "One defending sentence: why this weight and not less."
    }
  ],
  "knockouts": [
    { "id": "channel_locked", "desc": "Entry controlled by an exclusive competitor arrangement" }
  ],
  "markets": [
    {
      "name": "Canadian public sector",
      "scores": { "buying_readiness": 5 },
      "evidence": [
        {
          "criterion": "buying_readiness",
          "value": "Federal partnership on public-service AI; sovereign compute investment",
          "source": "https://www.canada.ca/...",
          "date": "2025-08"
        }
      ],
      "knockouts_hit": [],
      "notes": "Anything a reader needs that the scores do not carry."
    }
  ]
}
```

Field rules: weights sum to 100; every criterion carries a `rationale` (an undefended weight is
decoration); `inverted: true` marks criteria where lower reality scores higher (cycle length, cost
to serve, risk), and scores are always entered so **5 is good**; every non-obvious score cites
evidence; knockout hits are recorded with evidence and the market stays visible in the output.

## What the script computes

- **Weighted score** per market, normalized to 100.
- **Knockout enforcement:** hit markets are excluded from the ranking and reported separately.
- **Sensitivity analysis:** each weight is perturbed (default plus and minus 10 points,
  redistributed proportionally), the ranking recomputed, and every pair that swaps order recorded.
  Markets are then classified:
  - **robust:** position never changes across all tested weightings.
  - **contested:** swaps with at least one other market; the script names the criterion whose
    weight drives the swap.
- **The decisive criterion** for each contested pair, which is the question worth researching
  instead of debating.

## `prioritization.md` (the decision document)

```markdown
# Market prioritization: [Brand]

**Constraint:** [what capacity is being allocated, over what period]
**Model:** [n] markets, [n] criteria, weights defended below. Scored [date].

## The weights, and why
| Criterion | Family | Weight | Why this weight |
|---|---|---|---|

## Ranking
| # | Market | Score | Robustness | Strongest criterion | Weakest |
|---|---|---|---|---|---|
[Robustness is robust or contested-with-X, from the script.]

## What the sensitivity analysis says
[Which leaders hold under every tested weighting, which pairs swap, and for each contested pair,
the one criterion whose weight decides it and the evidence that would settle it.]

## The decision
[What to resource now, given the constraint, and the explicit reasoning.]

## Deprioritized, and why
| Market | Why not now | What would bring it back |
|---|---|---|
[Required section. Includes knockouts, marked as such.]

## Revisit triggers
[Events that force a re-run, plus the calendar cadence.]
```

The deprioritized table is the part leadership actually needs. A prioritization that only says yes
has not prioritized anything, and the "what would bring it back" column is what stops the same
argument from recurring every quarter.

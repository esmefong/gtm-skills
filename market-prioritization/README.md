# Market Prioritization

Rank candidate markets against weighted criteria, then report which rankings actually survive an
argument about the weights.

## What it does

Feed it a slate of markets (segments, verticals, geographies, use cases) and a capacity constraint,
and it builds a criteria model across five families (opportunity, fit, access, economics, risk),
forces a one-sentence defense of every weight, scores each market with evidence per cell, applies
knockouts, and then runs **sensitivity analysis**: each weight is perturbed and the ranking
recomputed, so every market comes back labeled robust or contested, and every contested pair comes
back with the one criterion that decides it.

It is opinionated about one thing: **the weights are the strategy, and a ranking that flips under a
small, reasonable change in weights is not a decision, it is a preference.**

The output ends with the section leadership actually needs: the deprioritized markets, the reason
for each, and what would bring them back.

## What it does NOT do

It does not rank accounts (that is [`account-sourcing`](../account-sourcing/), which runs inside
the markets this skill picks), and it does not forecast. Scores are structured judgments, never
revenue projections dressed as arithmetic.

## Who it's for

Founders, GTM leaders, and product marketers with more opportunities than capacity, who need a
defensible answer to "where do we focus," including a defensible no.

## How to use it

1. Copy this folder into `~/.claude/skills/market-prioritization/`.
2. Give it the slate and the constraint: *"We can resource two of these next year. Which two?"*
   It builds the criteria model, shows you the weights before any scoring, then scores and
   stress-tests.
3. Re-run anytime the model changes:

```
python3 scripts/prioritize.py markets.json --json sensitivity.json
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and six-phase workflow |
| `references/criteria-library.md` | The five criteria families, standard criteria, scoring anchors, knockouts, how to weight well |
| `references/output-template.md` | The markets.json schema and the decision-document format |
| `scripts/prioritize.py` | Weighted scoring, knockout enforcement, ranking, and sensitivity analysis |
| `examples/cohere/` | Eight markets ranked, one knocked out on a competitor channel lock, and a second-place coin flip the analysis refuses to call |

## Composes with

- [`icp-research`](../icp-research/) upstream: grounds the fit criteria and supplies disqualifiers
  that often become knockouts.
- [`account-sourcing`](../account-sourcing/) downstream: the chosen markets become the boundary of
  the account universe.
- [`positioning-message-house`](../positioning-message-house/): a chosen market is the audience the
  category bet is made for.

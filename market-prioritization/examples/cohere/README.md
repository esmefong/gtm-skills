# Worked example: market prioritization for Cohere

> **Real company, public data, illustrative.** Built from the repo's own Cohere ICP and
> account-sourcing run; not an official Cohere document. Scores are relative judgments with cited
> evidence, never forecasts.

Eight markets ranked against six defended weights, with the ranking stress-tested.

| File | What it is |
|---|---|
| `markets.json` | The model: criteria with defended weights, knockouts, and per-market scores with evidence |
| `prioritization.md` | The decision document: weights, ranking, what sensitivity says, the decision, the deprioritized list, revisit triggers |
| `sensitivity.json` | The script's full output: scores, ranking, contested pairs, decisive criteria |

## Reproduce

```
python3 ../../scripts/prioritize.py markets.json --json sensitivity.json
```

## Why this example is worth reading

- **The sensitivity analysis changed the answer.** Financial services (88.0) and sovereign telecom
  (87.0) are one point apart and swap whenever three different weights move. A model that reported
  "financial services wins" would have manufactured confidence out of a rounding difference. The
  output instead names the single question that decides it: are sovereign telcos customers or
  channel?
- **The knockout is real and evidenced.** Japan is ready and fits, and it is still removed: the
  dominant channel is contracted to a competitor (the SoftBank and OpenAI joint venture). It stays
  visible in the output so the exclusion is a decision rather than a silence.
- **A disqualified market is on the slate on purpose.** Mid-market SaaS scores 44 and ranks last,
  which makes the ICP's disqualifier visible in the ranking instead of assumed.
- **The composition is direct.** The ICP supplied fit and disqualifiers, the account-sourcing run
  supplied readiness evidence and the competitor lock, and the markets chosen here define the
  universe boundary for the next sourcing run.

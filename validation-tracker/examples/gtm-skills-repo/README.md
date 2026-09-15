# Worked example: this repository tracking itself

> **Everything here is real.** The metrics are this repo's actual weekly shipping and commit
> counts, checkable against the public git history; the decisions are the ones actually made
> while building it, dated and reasoned. The only fabricated file is `decisions-broken.json`,
> which exists so the check has something to refuse.

The example the other nine skills earned: the operating rhythm that built them, recorded in its
own format.

| File | What it is |
|---|---|
| `metrics.json` | Two metrics (skills shipped, commits to main) over nine weeks, floors and targets, zeros included |
| `decisions.json` | Eight real decisions, D0 through D7: the Cohere consolidation superseding the original per-brand plan, the roadmap resequence, the cadence raise, the review pause, the resume |
| `decisions-broken.json` | The refusal demo: one dangling supersession, one undocumented miss |

## Reproduce

```
python3 ../../scripts/weekly_check.py metrics.json decisions.json
python3 ../../scripts/weekly_check.py metrics.json decisions-broken.json
```

## What the run shows

- **Two zero weeks, both covered.** The weeks ending Aug 9 and Aug 30 went below floor, and the
  log contains the decisions that explain them (D6, the review pause; D7, the resume). Managed
  misses, not drift, and the check can tell the difference mechanically.
- **A supersession that reads as history.** D0 ("a different company per example") is superseded
  by D3 ("consolidate on Cohere") and stays in the log, so the reasoning trail survives the
  reversal.
- **The broken log is refused with reasons**: a supersession pointing at a decision that does not
  exist, and the Aug 30 miss left undocumented when D7 is removed. The difference between the
  two files is the difference between an audited system and a tidy story.

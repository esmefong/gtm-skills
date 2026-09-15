# Validation Tracker

The weekly operating rhythm for a GTM system: metrics with floors and targets set in advance, a
deterministic weekly check, and an append-only decision log where every pivot is written down
with its rationale.

## What it does

1. **Bands before results.** Each metric carries a floor (below this, act) and a target, set
   before the period; the weekly check compares actuals against them, zeros included.
2. **An append-only decision log.** Pivots, pauses, and reversals are entries with rationale and
   revisit dates; reversals supersede rather than overwrite, so the log reads as the system's
   true history.
3. **The coverage rule, enforced mechanically.** `scripts/weekly_check.py` validates the log's
   integrity (unique ids, chronological order, supersessions that resolve) and fails on the
   **undocumented miss**: any below-floor week with no decision logged inside the window. A miss
   someone wrote about is managed; a miss nobody wrote about is drift.
4. **Revisits come due.** Entries with revisit dates surface in the weekly run until reaffirmed
   or superseded.

The two claims underneath: **a metric without a benchmark is a mood, and a pivot without a
written decision is a drift.**

## What it does NOT do

It does not set your strategy (it records and audits it), it does not smooth zeros, and it does
not let history be edited: supersession is the only way a decision changes.

## Who it's for

Founders and GTM leaders running the motion the rest of this repo builds, who want "why are we
doing it this way" to have an answer with a date on it.

## How to use it

1. Copy this folder into `~/.claude/skills/validation-tracker/`.
2. Set 3-6 metrics with bands, start the log, then weekly: *"Run the validation check."*
3. Run it yourself anytime:

```
python3 scripts/weekly_check.py metrics.json decisions.json
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and the four-phase weekly ritual |
| `references/operating-rhythm.md` | Band-setting guidance, both schemas, the coverage rule's exact mechanics |
| `scripts/weekly_check.py` | Band check, log integrity, undocumented-miss detection, due revisits |
| `examples/gtm-skills-repo/` | This repository tracking itself: real weekly numbers, the eight real decisions that built it, and a broken log the check refuses |

## Composes with

Every other skill here: the metrics it tracks are the ones [account-sourcing](../account-sourcing/),
[outbound-engine](../outbound-engine/), and the rest produce, and its decision log is where their
strategy changes get recorded. It is the skill that operates the system.

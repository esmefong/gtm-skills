---
name: validation-tracker
description: >
  Run a weekly GTM operating rhythm: metrics with explicit floor and target bands, a deterministic
  weekly check of actuals against them, and an append-only decision log where every pivot, pause,
  and strategy change is written down with its rationale and revisit date. The script validates
  the log's integrity (append-only, supersession links resolve) and enforces the coverage rule:
  a week below floor with no logged decision inside the window is flagged as an undocumented
  miss. Use whenever the user says "operating rhythm", "weekly review", "track our benchmarks",
  "are we on track", "decision log", "why did we change strategy", "validation tracker", "weekly
  metrics check", or wants progress and pivots recorded instead of remembered. Works for any
  motion the other skills in this repo set up, and for any team that ships weekly.
---

# Validation Tracker

The operating rhythm that keeps a GTM system honest week over week. Two claims drive the design:
**a metric without a benchmark is a mood, and a pivot without a written decision is a drift.**
The tracker holds both: bands that say what good looks like before the week happens, and an
append-only log where every change of course is recorded with its reasoning, so the system's
history can be audited instead of reconstructed.

## What this consumes

| Input | Why | If missing |
|---|---|---|
| Metrics with bands | 3-6 metrics, each with a floor (below this, act) and target (aim here), set before the period | Help set them; a benchmark set after the results is a rationalization |
| Weekly actuals | The numbers, honestly, zeros included | A missing week is recorded as missing, never smoothed |
| The decision log | Every prior pivot with rationale | Start one now; entry one is why these metrics and bands |

## The workflow

Four phases, run weekly. The whole ritual is thirty minutes; the value is in never skipping it.

### Phase 1: Record the week

Append the week's actuals to `metrics.json`. Zeros are data: a zero week recorded honestly is
the input the coverage rule exists for. No retroactive edits to prior weeks; corrections are new
entries with notes.

### Phase 2: Run the check

`scripts/weekly_check.py` compares every metric against its bands and validates the decision
log: chronological order, unique ids, supersession links that resolve, and **coverage**: any week
with a metric below floor must have a decision logged within the window (default 21 days), or the
check fails with an undocumented miss. The rule's point is not punishment; it is that a miss
someone wrote a decision about is a managed miss, and a miss nobody wrote about is a drift.

### Phase 3: Decide, in writing

When the check demands a decision, or strategy changes for any reason, append to the log: what
was decided, the rationale at the time, what it supersedes, and when to revisit. Entries are
never edited or deleted; a reversed decision gets a new entry that supersedes the old one, so the
log reads as the true history of the system's thinking.

### Phase 4: Revisit on schedule

Entries with revisit dates come due; the weekly run lists them. A revisit produces either a
reaffirmation (log it, one line) or a supersession (log the new decision). Either way the log
stays the single place where "why are we doing it this way" has an answer with a date on it.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/weekly_check.py` | Band check per metric, append-only log validation, undocumented-miss detection, due revisits | None | None |

## Failure modes to avoid (the quality bar)

- **Bands set after results.** Floors and targets are commitments, not descriptions.
- **Smoothed zeros.** The zero week is the most informative row in the file.
- **Edited history.** The log is append-only; supersession is the only way a decision changes.
- **The undocumented miss.** Below floor with nothing written down is the failure mode this
  whole skill exists to catch, and the script fails on it mechanically.
- **Decision theater.** An entry without a rationale and a revisit condition is a announcement,
  not a decision.
- **Metrics sprawl.** More than six metrics and the ritual dies; track what would change behavior.

## Bundled references

- `references/operating-rhythm.md`: the weekly ritual, the band-setting guidance, the
  metrics.json and decisions.json schemas, and the coverage rule's exact mechanics.
- `examples/gtm-skills-repo/`: this repo tracking itself. Every metric and decision in the
  example is real and checkable against the public git history, including two zero weeks and the
  decisions that cover them, plus a deliberately broken log the check refuses.

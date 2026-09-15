# The operating rhythm

The weekly ritual, the schemas, and the coverage rule. Thirty minutes, same day each week.

## Setting bands

Per metric: a **floor** (below this, something must change or be decided) and a **target** (what
a good week looks like). Set both before the period starts. Anchors: last quarter's median makes
a defensible floor; the plan's requirement makes the target. If floor and target are equal, the
metric is a pass/fail gate, which is fine. Three to six metrics; each one must be capable of
changing a decision, or it is reporting, not tracking.

## `metrics.json`

```json
{
  "name": "gtm-skills repo",
  "as_of": "2026-09-04",
  "miss_decision_window_days": 21,
  "metrics": [
    {
      "id": "skills_shipped",
      "description": "Complete skills pushed to main in the week",
      "unit": "skills/week",
      "floor": 1,
      "target": 2,
      "weekly": [
        { "week_ending": "2026-07-12", "value": 1 }
      ]
    }
  ]
}
```

Weeks are append-only. A week with no data gets `"value": null` and a note, never a guess.

## `decisions.json`

```json
{
  "decisions": [
    {
      "id": "D3",
      "date": "2026-07-20",
      "decision": "Consolidate all worked examples on one company",
      "rationale": "Depth on one spine compounds; scattered examples prove nothing twice",
      "supersedes": "D0",
      "revisit": null
    }
  ]
}
```

Rules the script enforces: ids unique; dates non-decreasing in file order (append-only);
`supersedes` resolves to an earlier id; superseded entries are reported as such, never removed.
Rules the human enforces: every entry has a rationale written at decision time, and reversals are
new entries, not edits.

## The coverage rule (exact mechanics)

For every week where any metric's value is below its floor, there must exist a decision whose
date falls in the window `(week_ending, week_ending + miss_decision_window_days]`. One decision
can cover multiple concurrent misses. A miss with no covering decision fails the check as an
**undocumented miss**. The rule encodes the difference between a managed miss (someone looked at
the zero and chose a course) and a drift (nobody did).

## The weekly output

The script prints: a band table per metric (latest value, status, misses to date), the decision
log's integrity verdict, undocumented misses if any, and revisits due. Paste it into the weekly
note; the numbers argue so the meeting doesn't have to.

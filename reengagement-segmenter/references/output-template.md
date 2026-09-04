# Output template

Two artifacts: the machine-readable audience (`audience.json`, which the script segments in
place) and the human report (`segments.md`). Sequences per segment follow outbound-engine's
formats and gate.

## `audience.json` (the input the script segments)

```json
{
  "generated": "2026-09-04",
  "brand": "Cohere",
  "as_of": "2026-09-04",
  "dormancy_horizon_months": 24,
  "records": [
    {
      "account": "Meridian Trust (fictional)",
      "role": "Head of AI platform",
      "last_meaningful_activity": "2025-11-14",
      "lifecycle_reached": "security_review",
      "stated_reason": "price",
      "unsubscribed": false,
      "complaint": false,
      "competitor_contract_until": null,
      "icp_disqualifiers": [],
      "evidence": [
        {
          "field": "stalled_gate",
          "value": "Deal paused at security review; residency question unanswered at the time",
          "source": "internal: opportunity notes",
          "date": "2025-11"
        }
      ]
    }
  ]
}
```

Field rules: `stated_reason` is the CRM's label (may be empty, may be wrong); `evidence[].field`
carries blocker tags from the taxonomy (`stalled_gate`, `never_activated`, `timing_deferral`,
`lost_to_incumbent`, `price_objection`, `trust_damage`); sources are internal by nature here and
say so. The script writes back `segment`, `lane`, and `flags` per record.

## What the script computes

Exclusions first (opt-out, complaint, active competitor contract, ICP disqualifier, dormancy
horizon, too-recent), then blocker assignment by taxonomy precedence over the evidence tags, then
**conflict detection**: a record whose `stated_reason` maps to a different blocker than its
evidence gets `segment: "conflict"` and both candidates in `flags`, because that resolution is
judgment work, not bookkeeping. Records with no blocker evidence get `drifted`. Output: per-record
assignments written back, a count table, and the conflict list.

## `segments.md` (the report)

```markdown
# Reengagement segments: [Brand]

[Provenance line: records, as-of date, what changed on our side that makes reengagement timely.]

## The map
| Segment | Count | Why-now | Motion | Owner |
[One row per active segment plus the leave-alone lane.]

## Conflicts and how they were resolved
[Per conflict: the stated reason, the evidence, the call, the reasoning. Required when any exist.]

## The leave-alone lane
| Record | Reason |
[Every excluded record with its gate. Required.]

## Sequences
[Per active segment: the sequence file, its gate verdict verbatim, or "signal watch, no sequence"
with the trigger that would change it.]
```

The report is honest about asymmetry: some segments get sequences, some get a signal watch, some
get one diagnostic question, and the leave-alone lane gets documented restraint.

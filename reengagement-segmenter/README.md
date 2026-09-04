# Reengagement Segmenter

Turn a lapsed list into distinct segments by the blocker that actually stalled each relationship,
plan one motion per segment, and document the records you choose to leave alone.

## What it does

Point it at dormant pipeline, lapsed customers, or a cold list with whatever evidence exists per
record, and it:

1. **Runs the exclusions first.** Opt-outs, complaints, active competitor contracts, ICP
   disqualifiers, and the dormancy horizon go to a leave-alone lane with a reason per record,
   before any messaging thought happens.
2. **Segments by blocker, not recency.** A taxonomy of seven blockers (never-activated,
   stalled-gate, timing, lost-to-incumbent, price, trust, drifted), each requiring evidence,
   with `scripts/segment_audience.py` doing the bookkeeping deterministically.
3. **Flags contradictions instead of smoothing them.** A record whose CRM label disagrees with
   its thread is a conflict the script detects and a judgment call the report logs.
4. **Plans asymmetrically.** Segments whose blocker actually moved get short, gated sequences
   (two to three touches through [outbound-engine](../outbound-engine/)'s no-send gate); the rest
   get a signal watch, one diagnostic question, or a named human.

The argument underneath: **win-back blasts fail because they treat silence as one condition, when
silence is the least informative signal a contact can send.**

## What it does NOT do

It does not message the excluded (opt-outs are permanent exits), it does not sequence trust
damage (that gets a named human), and it does not invent a why-now: no change on your side or
theirs means a watch, not a message.

## Who it's for

Sales and lifecycle teams sitting on dormant pipeline or a lapsed list, who want fewer, sharper
messages than the blast, plus a defensible record of restraint.

## How to use it

1. Copy this folder into `~/.claude/skills/reengagement-segmenter/`.
2. Point it at the records: *"Segment our dormant pipeline for reengagement."* It gates, segments,
   flags conflicts, and plans per segment.
3. Run the segmenter yourself anytime:

```
python3 scripts/segment_audience.py audience.json --table
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and five-phase workflow |
| `references/blocker-taxonomy.md` | The segments, required evidence, exclusion gates, and sequence archetype per segment |
| `references/output-template.md` | The audience.json schema and the segment-report format |
| `scripts/segment_audience.py` | Deterministic segmentation with conflict detection |
| `examples/cohere/` | A dormant-pipeline pass on labeled synthetic records: one conflict resolved in writing, one gated sequence, and a documented leave-alone lane |

## Composes with

- [`icp-research`](../icp-research/): disqualifiers feed the exclusion gates; triggers supply the
  why-now watches.
- [`brand-voice-guide`](../brand-voice-guide/): sequences are drafted in the extracted voice.
- [`outbound-engine`](../outbound-engine/): every reengagement sequence runs through its gate; the
  example's PASS is produced by that script, unmodified.

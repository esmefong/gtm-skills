---
name: reengagement-segmenter
description: >
  Segment a lapsed audience by the actual blocker that stalled each relationship, then plan a
  distinct reengagement motion per segment, including the segment that should be left alone.
  Works on dormant pipeline, lapsed customers, cold trial users, or an inactive list. Applies a
  blocker taxonomy (never activated, timing, lost to incumbent, price, trust damage, drifted,
  unknown), enforces hard exclusions first (unsubscribed, complaints, active competitor
  contracts), flags records whose stated reason contradicts their evidence, and drafts sequences
  through the outbound-engine gate. Use whenever the user says "win-back", "reengagement",
  "re-engage", "lapsed customers", "dormant accounts", "stalled deals", "gone quiet", "cold
  pipeline", "churned users", or wants to revive a list without blasting it. Consumes icp-research
  and brand-voice-guide; sequences inherit outbound-engine's no-send discipline.
---

# Reengagement Segmenter

Turn "the lapsed list" into distinct audiences with distinct reasons for silence, and treat the
reason as the segment. The design rests on one argument: **win-back blasts fail because they treat
silence as one condition, when silence is the least informative signal a contact can send.** A
deal stalled at security review, a user who never reached value, and a buyer who signed with the
incumbent all look identical in a recency report and need three different messages, or none.

The other half of the argument is the repo's standing one: the most valuable output of a
reengagement pass is often the list of people you decide not to contact, documented.

## What this consumes

| Input | From | What it provides |
|---|---|---|
| The lapsed records | CRM export, deal notes, product events, support history | The evidence each blocker call rests on |
| ICP | `icp-research` | Disqualifiers (bad-fit lapse is leave-alone, not win-back), triggers for the why-now |
| Voice directory | `brand-voice-guide` | The register sequences are written in |
| What changed on your side | The user | Reengagement needs a why-now; "we miss you" is not one |

The last row is the load-bearing one. A reengagement sequence exists because something changed:
your product closed the gap that stalled them, their situation visibly shifted, or a trigger from
the ICP fired. No change, no sequence; that cohort waits.

## The workflow

Five phases. Show the user the segment map (end of Phase 3) before any drafting.

### Phase 1: Assemble the evidence, not just the list

Pull the lapsed records with whatever evidence exists per record: last meaningful activity,
lifecycle stage reached, stated reasons (closed-lost fields, cancellation surveys), and observed
behavior (support tickets, usage before silence, emails). First-party evidence is messy and
contradictory; that is expected and handled in Phase 3, not smoothed over.

### Phase 2: Run the exclusions first

Before any blocker reasoning, apply the hard gates from `references/blocker-taxonomy.md`:
unsubscribed or do-not-contact, complaint history, active competitor contracts, ICP disqualifiers,
and the dormancy horizon. These records go to the **leave-alone lane with reasons**, which ships
in the deliverable. Reengaging someone who opted out is not a growth motion, it is a compliance
incident.

### Phase 3: Assign blockers, honestly

Tag each surviving record with a blocker from the taxonomy, citing the evidence. Three rules:

- **The evidence outranks the label.** When the CRM says "price" but the thread shows a security
  stall, the record is flagged as a conflict and resolved by judgment, with the resolution
  written down. `scripts/segment_audience.py` detects these conflicts mechanically.
- **Unknown stays unknown.** A record with no blocker evidence goes to the diagnostic segment,
  whose sequence asks one honest question instead of assuming a reason.
- **The script does the bookkeeping.** Deterministic rules (exclusions, recency bands, tag
  precedence, conflict detection) run mechanically; the judgment calls are yours and get recorded.

### Phase 4: Plan one motion per segment

Each blocker has its own sequence archetype in the taxonomy: the never-activated get the value
they missed, the timing-stalled get a low-pressure trigger watch, the security-stalled get the
specific thing that changed, the diagnostic segment gets one question. Two universal rules:
reengagement sequences are **shorter than cold ones** (two to three touches), and every sequence
opens with the why-now change, not with an apology for the silence.

### Phase 5: Draft, gate, package

Draft in the brand voice and run every sequence through `outbound-engine`'s
`sequence_gate.py`: the freshness check applies to the why-now change, the slop list catches
"just checking in" (the canonical reengagement failure), and the voice Avoid list holds. Package
per `references/output-template.md`: the segment map with counts, the per-segment plans, the
conflict log, and the leave-alone lane with reasons.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/segment_audience.py` | Deterministic segmentation: exclusions, recency bands, blocker tags, conflict flags, counts | None | None |

## Failure modes to avoid (the quality bar)

- **One blast to the whole list.** The disease this skill treats.
- **"Just checking in."** The outbound gate catches it mechanically; do not write it.
- **Guessing the blocker.** No evidence means the diagnostic segment, not your best story.
- **Reengaging the excluded.** Unsubscribes and complaints are permanent exits from this motion.
- **Apologizing for the silence.** Open with what changed, not with the gap.
- **A hidden leave-alone lane.** The records you chose not to contact, with reasons, are output.
- **Trusting the CRM label over the thread.** Stated reasons are hypotheses; conflicts get logged.

## Bundled references

- `references/blocker-taxonomy.md`: the segments, the evidence each requires, the exclusion
  gates, and the sequence archetype per segment. Read at Phases 2-4.
- `references/output-template.md`: the audience.json schema the script consumes and the segment
  report format. Read at Phases 3-5.
- `examples/cohere/`: a dormant-pipeline pass in Cohere's voice on synthetic records (fictional
  counterparties, labeled, with real contradictions), the segment map, and a gated sequence for
  the security-stall segment.

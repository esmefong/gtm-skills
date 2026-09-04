# Blocker taxonomy

The segments, the evidence each requires, the exclusions that run first, and the sequence
archetype per segment. The segment is the blocker, never the demographic or the recency band;
recency decides eligibility, the blocker decides the message.

## Exclusions (run before any blocker reasoning)

| Gate | Rule | Lane |
|---|---|---|
| Opt-out | Unsubscribed, do-not-contact, or consent expired (CASL and kin) | leave-alone, permanent |
| Complaint | Support escalation, public complaint, or a relationship that ended badly | leave-alone unless a human owner explicitly sponsors an apology-first motion |
| Committed elsewhere | Evidence of an active competitor contract inside its term | leave-alone until the renewal window |
| Bad fit | Hits an ICP disqualifier | leave-alone; a bad-fit lapse is the ICP working, not a loss |
| Too cold | Beyond the dormancy horizon (default 24 months) with no strong signal | archive; a 3-year-old contact is a cold prospect, not a reengagement |
| Too warm | Active in the last 90 days | not lapsed; leave to the live motion |

Leave-alone is a documented lane with a reason per record, not a silent filter.

## The blockers

| Segment | What happened | Evidence required | Sequence archetype |
|---|---|---|---|
| `never-activated` | Bought or signed up, never reached value | Lifecycle shows entry without the activation event | Show the unreached value with one concrete path to it; never re-pitch what they already bought |
| `stalled-gate` | The deal died at a specific gate (security review, legal, procurement) | The stall stage and gate named in notes or thread | Lead with the specific thing that changed at that gate since; this is the highest-yield segment when a real change exists |
| `timing` | Right fit, wrong moment (budget cycle, reorg, paused initiative) | A stated or evidenced deferral | One low-pressure note per trigger event; put the account on signal watch, not on a cadence |
| `lost-to-incumbent` | Chose the default or a competitor | A named alternative in the record | Door-open only; message on real differentiating news, never on "reconsider us"; respect contract terms |
| `price` | Cost or packaging objection | A stated price objection | Reengage only when the economics actually changed (new tier, new packaging); otherwise timing-watch |
| `trust` | Product or service let them down, short of a complaint | Ticket history, a bad rollout, a churned champion's notes | Human-owned, not sequenced; the skill flags these for a named owner |
| `drifted` | Engaged, then silence, no stated reason | Absence of the above | Diagnostic: one honest question offering the likely reasons, one reply resolves the segment |
| `conflict` | The stated reason contradicts the evidence | CRM label vs. thread disagree | Resolve by judgment before drafting; the resolution is logged. The script flags these mechanically |

## Universal sequence rules

- **Two to three touches.** These contacts already know you; persistence reads as pressure.
- **Open with the change, not the gap.** The first line names what is different now. Never
  apologize for the silence and never say "just checking in" (the gate catches it anyway).
- **One segment, one why-now.** A sequence whose why-now applies to every segment belongs to no
  segment.
- **The gate applies.** Every sequence runs through outbound-engine's `sequence_gate.py`:
  freshness on the why-now change, slop and voice checks, one ask per touch, role-level only.
- **Reply handling beats touch three.** A diagnostic reply re-segments the record; route it, do
  not keep sequencing.

## Precedence

When multiple blockers have evidence, the order is: exclusions, then `trust`, then `stalled-gate`,
then `lost-to-incumbent`, then `price`, then `timing`, then `never-activated`, then `drifted`.
Trust outranks everything because messaging past damage compounds it; the stall gate outranks the
rest because it is the most specific and therefore the most answerable.

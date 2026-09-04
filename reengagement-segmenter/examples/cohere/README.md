# Worked example: segmenting Cohere's dormant pipeline

> **Synthetic counterparties, labeled; real machinery.** This is the one example in the repo whose
> records are fictional, and that is the evidence standard working, not slipping: pipeline history
> is private, and fabricating it about real companies would cross the never-invent line. The
> contradictions in the data are deliberate, so this example also serves as the repo's
> messy-first-party-input demonstration. Cohere's voice, ICP, and the June 2026 sovereign
> infrastructure change are real and cited.

| File | What it shows |
|---|---|
| `audience.json` | 13 records with the mess left in: a CRM label that contradicts the thread, a record with no evidence at all, an opt-out, an active competitor contract, one too cold and one too warm |
| `segments.md` | The map: 7 to reengage across 7 different motions, the conflict resolved in writing, and 5 held back with reasons |
| `reeng-sequence.json` | The stalled-gate sequence: 3 touches in Cohere's voice, opening with the June change, gated by outbound-engine and passing |
| `cohere-avoid.txt` | The voice ban list the gate enforces, from the voice guide |

## Reproduce

```
python3 ../../scripts/segment_audience.py audience.json --table
python3 ../../../outbound-engine/scripts/sequence_gate.py reeng-sequence.json --as-of 2026-09-04 --avoid cohere-avoid.txt
```

## The three judgment moments

- **The conflict call:** Meridian's CRM says price, the notes say security stall. The thread
  outranks the label, the resolution is logged, and the discarded hypothesis stays in the record.
- **One sequence, not seven:** only the stalled-gate segment's blocker demonstrably moved (the
  residency answer), so only it earns a sequence this pass. Timing gets a watch, drifted gets a
  question, trust gets a human.
- **The leave-alone lane ships:** an opt-out, a contract, and an ICP disqualifier, each with its
  reason. Documented restraint is the deliverable the blast never produces.

# Worked example: outbound for Cohere's sourced accounts

> **Real companies, public data, illustrative.** These sequences are demonstrations built from
> public evidence, not official Cohere communications. Targeting is role-level throughout; no
> individual is named and no contact details exist anywhere in the artifacts.

This example runs the composed system end to end: the ICP defined who and why
(`icp-research/examples/cohere/`), the voice defined how it sounds
(`brand-voice-guide/examples/cohere/`), account-sourcing produced the list with signals and routing
(`account-sourcing/examples/cohere/`), and this skill turns two of those accounts into decisions.

## The two artifacts

| File | What it shows |
|---|---|
| `telus-sequence.md` / `.json` | A gate-passing partner-motion sequence: 5 touches, 21 days, written in Cohere's voice on a 70-day-old signal, with per-line provenance and named judgment calls (the rival partnership deliberately unnamed) |
| `cibc-no-send.md` + `cibc-draft-rejected.json` | The refusal: the strongest-looking bank on the list, refused because its signal is 420 days stale. The test draft also trips the slop check ("congrats on the") and Cohere's own Avoid list ("revolutionary"), mechanically |
| `cohere-avoid.txt` | The gate's ban file, taken directly from the voice guide's writing standard |

## Reproduce the gate

```
python3 ../../scripts/sequence_gate.py telus-sequence.json --as-of 2026-07-21 --avoid cohere-avoid.txt
python3 ../../scripts/sequence_gate.py cibc-draft-rejected.json --as-of 2026-07-21 --avoid cohere-avoid.txt
```

The first passes; the second fails with three reasons. Same inputs, same verdicts, every run.

## Why the refusal leads

A reviewer who only ever sees sends has no reason to trust any of them. The CIBC verdict is the
proof that the TELUS sequence means something: the engine declined a better-scored account because
the timing was wrong, and it documented what would change the answer.

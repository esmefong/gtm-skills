# Outbound Engine

Turn a sourced account and its live signal into outreach worth sending, in the brand's own voice,
with every load-bearing line traceable to its source. Or refuse, with reasons.

## What it does

The final stage of the repo's composed GTM system. It consumes a qualified account from
[`account-sourcing`](../account-sourcing/) (the signal, the owner lane, the entry role), the ICP
from [`icp-research`](../icp-research/) (triggers, buying committee, how-to-speak rules), and the
voice directory from [`brand-voice-guide`](../brand-voice-guide/), then:

1. **Gates the send.** Signal freshness, signal-to-trigger mapping written out in two sentences,
   committee safety (never cold the veto holder), and lane eligibility. Weak sends get a no-send
   verdict with reasons and the signal that would flip it.
2. **Picks the motion** from the ICP's buying reality: enterprise-ABM (five touches, low volume,
   call ask) or velocity, with a partner variant.
3. **Drafts in the brand's voice** with per-line provenance: every opener traces to a dated
   signal, every argument to an ICP trigger, every register choice to a voice pillar, and every
   deliberate omission to a named judgment call.
4. **Verifies mechanically.** `scripts/sequence_gate.py` (stdlib-only, no keys) enforces
   freshness, touch caps, word counts, one ask per touch, annotation coverage, the universal slop
   list ("congrats on the", "just following up"), and the brand's own Avoid words, read straight
   from the voice guide.

It is opinionated about one thing: **the scarce asset in outbound is trust, and the engine
protects it by refusing weak sends.** The refusal is a first-class deliverable.

## What it does NOT do

No contact harvesting: targeting is role-level, and finding the person, the address, and the legal
basis (CASL and kin) is the sender's downstream step. No volume blasting: the enterprise motion is
five touches to one role. No drafting for the reject pile: disqualified, nurture, and
existing-relationship lanes are refused at the gate.

## Who it's for

GTM, sales, and partnership teams sitting on a sourced account list who want outreach that survives
a practitioner's sniff test, and a system that says no when the timing is wrong.

## How to use it

1. Copy this folder into `~/.claude/skills/outbound-engine/`.
2. Point it at an account: *"Draft outreach for TELUS from the sourced list."* It gates, routes,
   drafts, annotates, and runs the mechanical check.
3. Verify any sequence yourself:

```
python3 scripts/sequence_gate.py telus-sequence.json --as-of 2026-07-21 --avoid cohere-avoid.txt
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and five-phase workflow |
| `references/gates-and-motions.md` | The judgment checks, the motion archetypes, the compliance floor |
| `references/output-template.md` | The sequence.json schema and the annotated-sequence format |
| `scripts/sequence_gate.py` | The deterministic send/no-send gate |
| `examples/cohere/` | The composed system end to end: a gate-passing TELUS partner sequence in Cohere's voice, and a no-send verdict for CIBC with the gate's output verbatim |

## Composes with

- [`account-sourcing`](../account-sourcing/) upstream: accounts, signals, lanes, entry roles.
- [`icp-research`](../icp-research/) for triggers and the committee; [`brand-voice-guide`](../brand-voice-guide/)
  for the voice and the Avoid list the gate enforces.

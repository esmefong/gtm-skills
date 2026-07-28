# Output template

Two artifacts per account: the annotated human-readable sequence (`<account>-sequence.md`) and the
machine record (`<account>-sequence.json`) that `scripts/sequence_gate.py` verifies. A no-send
verdict replaces both with `<account>-no-send.md`.

## `sequence.json` (the gate's input)

```json
{
  "generated": "2026-07-21",
  "brand": "Cohere",
  "account": "TELUS",
  "motion": "enterprise-abm",
  "lane": "Partnerships",
  "target_role": "VP, AI Infrastructure / enterprise AI product",
  "signal": {
    "detail": "Sovereign AI Factory expansion: Kamloops plus two Vancouver sites",
    "source": "https://www.rcrwireless.com/20260512/carriers/telus-ai-data-centers",
    "date": "2026-05-12"
  },
  "trigger_mapping": "The expansion is public sovereign AI capacity; sovereign capacity sells on the model layer that runs privately on it, which is the ICP's data-residency trigger from the supply side.",
  "touches": [
    {
      "n": 1,
      "channel": "email",
      "day": 0,
      "subject": "Models for the factory",
      "body": "...",
      "ask": "20-minute call",
      "ask_type": "call",
      "annotations": [
        { "type": "signal", "ref": "rcrwireless 2026-05-12: Kamloops + Vancouver expansion" },
        { "type": "icp_trigger", "ref": "data-residency / sovereignty trigger, supply side" },
        { "type": "voice", "ref": "possessive-contrast pillar" },
        { "type": "judgment", "ref": "competitor partner unnamed: channel conflict" }
      ]
    }
  ]
}
```

Field rules: `motion` is `enterprise-abm | velocity`; `signal.date` is required and drives the
freshness check; `trigger_mapping` is required and capped at two sentences; every touch carries
`ask`, `ask_type`, and at least one annotation; `target_role` is a role, never a person.

## Annotation types

| Type | What it traces |
|---|---|
| `signal` | The dated public fact a line references |
| `icp_trigger` | Which ICP trigger the logic instantiates |
| `icp_committee` | Why this role, or why a role was avoided |
| `voice` | Which voice pillar or writing-standard rule shaped the line |
| `evidence` | An account-sourcing evidence entry used in the body |
| `rule` | A sequence rule applied (one ask, flat close, spacing) |
| `judgment` | A deliberate choice, especially what was left out and why |

## `<account>-sequence.md` (the human artifact)

```markdown
# Outreach sequence: [Brand] to [Account]

[One line: role targeted, motion, signal with date, and the gate result.]

**Trigger mapping:** [the two-sentence logic]
**Gate:** [script output summary: PASS, checks run]
**Compliance note:** [one line: confirm legal basis before send]

## Touch 1: email, day 0
**Subject:** ...
[Body]
**Ask:** ...
> Provenance: [signal ...] [icp_trigger ...] [voice ...] [judgment ...]

[Repeat per touch. After the final touch:]

## Judgment calls
[The choices a reviewer should see: what was deliberately not said, which roles were not touched,
what would change the sequence.]
```

## `<account>-no-send.md` (the refusal artifact)

```markdown
# No-send verdict: [Brand] to [Account]

**Verdict:** do not send. [Which gate checks failed, with the numbers.]
**Why this account still matters:** [tier, score, standing evidence]
**What would change the verdict:** [the specific signal or freshness that flips it]
**Next step:** [the concrete action: fresh sweep, wait for trigger, route to nurture]
```

The refusal is written with the same care as a sequence. It is the artifact that proves the engine
has judgment; a reviewer who sees only sends has no reason to trust any of them.

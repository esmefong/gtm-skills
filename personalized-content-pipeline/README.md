# Personalized Content Pipeline

Produce branded, per-customer content from structured briefs, with a durable state file per
customer so the system remembers what it already said, which language survived review, and what
this customer must never hear again.

## What it does

Give it a brief (asset type, goal, cited facts) and it:

1. **Opens the customer's state file first**: the asset log, approved language, do-not-say rules
   with reasons, and corrections that supersede stale facts. First contact creates the file.
2. **Reconciles the brief against the state**: conflicts are flagged, corrections win over
   incoming facts, and the do-not-say list is absolute.
3. **Drafts in the brand voice, personalizing from facts**: every customer-specific line traces
   to a cited fact from the brief or state, in the register
   [`brand-voice-guide`](../brand-voice-guide/) extracted.
4. **Gates twice**: [`content-quality-check`](../content-quality-check/)'s linter for the
   universal floor, then `scripts/state_guard.py` for the per-customer floor: do-not-say
   violations, repeated openings, unfilled tokens, stale facts, superseded values.
5. **Closes the loop**: the shipped asset is appended to the state, so the next asset starts
   smarter.

The claim underneath: **personalization that scales is state, not adjectives.** A line that would
survive with the customer's name swapped out is not personalized.

## What it does NOT do

No flattery personalization, no silent do-not-say overrides (the list changes only by explicit
state edit with a reason), and no contact details: audiences stay role-level, as everywhere in
this repo.

## Who it's for

Customer marketing, ABM, and account teams producing the same asset types across many customers,
who want the tenth asset for a customer to be sharper than the first instead of a repeat of it.

## How to use it

1. Copy this folder into `~/.claude/skills/personalized-content-pipeline/`.
2. Bring a brief: *"Draft the QBR one-pager for [customer]."* It opens the state, drafts, gates,
   and logs.
3. Run the guard yourself anytime:

```
python3 scripts/state_guard.py draft.md state.json --brief brief.json
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and five-phase workflow |
| `references/output-template.md` | The brief, state, and asset schemas, and what the guard checks |
| `scripts/state_guard.py` | The deterministic per-customer gate, plus `--log` to append shipped assets |
| `examples/cohere/` | A second-touch TELUS asset whose state inherited the outbound sequence's judgment call, and a rejected draft refused for violating it |

## Composes with

- [`brand-voice-guide`](../brand-voice-guide/): the voice every asset is written in.
- [`content-quality-check`](../content-quality-check/): the first of the two gates.
- [`outbound-engine`](../outbound-engine/) and [`account-sourcing`](../account-sourcing/):
  sequences and account records seed the state; judgment calls made there persist here.

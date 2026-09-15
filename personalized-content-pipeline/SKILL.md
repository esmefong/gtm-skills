---
name: personalized-content-pipeline
description: >
  Produce branded, voice-checked content per customer or per account from a structured brief, with
  durable per-customer state. Every asset draws on a state file that carries the relationship's
  memory forward: what was already produced, which language is approved, which facts and phrases
  are banned for this customer, and which corrections must never regress. Drafts in the brand
  voice, personalizes from cited facts rather than flattery, and gates every asset twice: through
  content-quality-check's linter and through a deterministic state guard that blocks repeated
  openings, banned phrases, stale facts, and unfilled tokens. Use whenever the user says
  "per-customer content", "per-account content", "ABM content", "personalize this for", "QBR
  deck copy", "customer one-pager", "onboarding content for", "account-specific page", or wants
  the same asset type produced across many customers without drift or repetition. Consumes
  brand-voice-guide and content-quality-check; pairs with account-sourcing's account records.
---

# Personalized Content Pipeline

Produce content per customer the way a good account team would: remembering everything already
said, honoring every correction, and personalizing from facts rather than flattery. The design
rests on one claim: **personalization that scales is state, not adjectives.** Mail merge with a
nicer voice fails on the second asset, because the system has forgotten what the first one said,
which judgment calls were made, and what this customer told you never to say again.

The unit of the skill is therefore not the asset but the **customer state file** that outlives it.

## What this consumes

| Input | From | What it provides |
|---|---|---|
| The brief | The user, structured per `references/output-template.md` | Asset type, goal, audience, and the cited facts personalization may use |
| Customer state | This skill (created on first contact) | Asset log, approved language, do-not-say rules, corrections |
| Voice directory | `brand-voice-guide` | The register every asset is written in |
| Account record (optional) | `account-sourcing` | Evidenced public facts, entry role, motion notes |

## The workflow

Five phases. The state file opens every run and closes every run.

### Phase 1: Load the state, or create it

On first contact with a customer, create `state.json` from the template: empty asset log, any
known approved language, any inherited judgment calls (an outbound sequence's documented
omission, a legal-cleared phrase, a correction from a call). On every later run, read it before
reading the brief; the state is the senior colleague who has worked this account longest.

### Phase 2: Reconcile the brief against the state

- Every fact the brief supplies gets checked against the state's facts. A conflict (the brief
  says 60,000 GPUs, the state's correction says the customer disputes that figure) is flagged and
  resolved by judgment, and the resolution is written into the state.
- The **do-not-say list is absolute**: phrases, claims, and topics recorded there do not appear
  in the draft regardless of what the brief asks for. Overriding one is a state edit with a
  reason, never a silent exception.
- Facts carry dates; the state guard flags personalization built on stale ones.

### Phase 3: Draft from facts, in the voice

Write the asset in the brand's voice. The personalization rule mirrors the outbound engine's
provenance discipline: **every customer-specific line traces to a cited fact in the brief or
state.** "As a leader in your space" is flattery; "your Kamloops expansion" is a fact with a
source. Reuse the state's approved language deliberately; it has already survived review.

### Phase 4: Gate twice

1. `content-quality-check`'s linter, with the brand Avoid file: the universal quality floor.
2. This skill's `scripts/state_guard.py`: the per-customer floor. It blocks do-not-say
   violations, an opening that repeats any previous asset's opening, unfilled merge tokens, and
   facts older than the freshness window. Same draft, same verdict, every run.

An asset that fails either gate is revised, not excused.

### Phase 5: Close the loop

Log the shipped asset into the state (`state_guard.py --log` appends it deterministically):
date, type, opening line, facts used. Add any new approved language and any new judgment calls.
The next asset for this customer starts smarter than this one did.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/state_guard.py` | Deterministic per-customer gate: do-not-say, repeated openings, unfilled tokens, stale facts; `--log` appends the shipped asset to state | None | None |

## Failure modes to avoid (the quality bar)

- **Adjective personalization.** A line that would survive with the customer's name swapped out
  is not personalized; cut it or ground it in a fact.
- **The forgotten judgment call.** Decisions made in one asset (an omission, a framing) bind the
  next; that is what the state is for.
- **Silent do-not-say overrides.** The list changes only by explicit state edit with a reason.
- **Repetition across assets.** The customer reads everything; the guard catches reused openings
  mechanically, and the editor watches for reused arguments.
- **Stale facts.** A why-now fact past the freshness window needs re-verification, not reuse.
- **State that only grows.** Corrections supersede; log the supersession instead of stacking
  contradictory entries.

## Bundled references

- `references/output-template.md`: the brief schema, the state.json schema, and the asset
  format. Read at Phases 1-2 and 5.
- `examples/cohere/`: a second-touch ABM one-pager for TELUS built from real cited public facts,
  a state file that inherited the outbound sequence's judgment calls, a rejected draft the state
  guard refuses with reasons, and both gate outputs verbatim.

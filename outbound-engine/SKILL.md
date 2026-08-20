---
name: outbound-engine
description: >
  Turn a sourced account and its live signal into outreach worth sending, or refuse with reasons.
  Consumes account-sourcing output (a qualified account with a dated signal, an owner, and an entry
  role), the ICP from icp-research (triggers, buying committee, how-to-speak rules), and the voice
  directory from brand-voice-guide, then drafts a committee-aware sequence in the brand's voice with
  per-line provenance. A mechanical no-send gate rejects weak sends: stale signals, weak
  signal-to-trigger mapping, banned voice, fake familiarity, missing asks. Use whenever the user
  says "outbound", "cold outreach", "write to this account", "draft a sequence", "outreach
  sequence", "ABM sequence", "signal-based outreach", "cold email", or wants sourced accounts turned
  into messages. Role-level targeting only: it never harvests individuals or contact details.
---

# Outbound Engine

Turn a qualified account with a live signal into outreach worth sending, in the brand's own voice,
with every load-bearing line traceable to its source. One conviction sits under every phase:
**the scarce asset in outbound is trust, and the engine protects it by refusing weak sends.** A
"do not send, here is why" verdict is a first-class deliverable, not a failure.

Inboxes are full of AI-personalized noise. What separates outreach that works is judgment (send
only when the signal genuinely predicts the buyer's situation) and provenance (every claim in the
message has a source). Both are enforced here, the second mechanically.

## What this consumes (the composed system)

| Input | From | What it provides |
|---|---|---|
| Account record with signal | `account-sourcing` (`accounts.json`) | Who, the dated why-now, the owner lane, the entry role |
| ICP | `icp-research` (`icp.md`) | Triggers, buying committee, decision criteria, how-to-speak rules |
| Voice directory | `brand-voice-guide` | Tonal pillars, writing standard, the Avoid list |

No account-sourcing run? The skill accepts a manual account + signal, but it applies the same
evidence standard: a signal without a date and source does not pass the gate. No voice directory?
It drafts in a plain professional register and says so; it never invents a brand voice.

## Hard boundaries

- **Role-level only.** Sequences target a role ("Head of AI / ML platform lead"), never a named
  individual. Contact discovery, email finding, and consent verification are downstream steps for
  the sender's tools and legal basis, not this skill.
- **Only qualified accounts.** Records with status `disqualified` or lanes `Nurture`, `Do not
  pursue`, or `Existing relationship` are refused at the gate. The reject pile exists for a reason.
- **Compliance is the sender's floor.** The sequence ships with a compliance note (consent regimes
  like CASL are stricter than opt-out regimes); confirm the legal basis before any send.

## The workflow

Five phases. The gate comes second, deliberately: most of the engine's value is deciding *whether*
to send before polishing *what* to send.

### Phase 1: Load and frame

Read the account record, the ICP, and the voice directory. Note the owner lane and entry role from
the routing fields, and the motion the ICP's journey implies. State what is being attempted in one
line: "[Brand] to [role] at [account], because [signal], via [motion]."

### Phase 2: The gate (send / no-send)

Run the judgment checks in `references/gates-and-motions.md`, then encode the draft and run the
mechanical gate:

- **Status and lane:** qualified accounts in an outreach-eligible lane only.
- **Signal freshness:** the why-now must be recent (default: 90 days). Last year's platform launch
  is context, not a reason to write today.
- **Signal-to-trigger mapping:** the signal must instantiate one of the ICP's named triggers, with
  the logic written out. "They raised money, so they might buy things" is name-dropping, not
  mapping. If the mapping needs more than two sentences to justify, it is weak.
- **Committee safety:** the target role must be the ICP's champion or entry persona. Never cold
  the veto holder (for a security-gated ICP, never cold the CISO).

Any failure produces a **no-send verdict with reasons and a next step** (refresh the signal, run a
sweep, wait for the trigger). Write it up; it is the deliverable.

### Phase 3: Route and structure

Pick the motion from the ICP's buying reality (`references/gates-and-motions.md`): enterprise-ABM
(low volume, multi-threaded, research-heavy, call ask) when the committee is large and the journey
runs through analysts and procurement; velocity (shorter, higher volume) for PLG and SMB motions.
Plan the thread: primary track to the champion role, one optional exec air-cover touch, and spacing
across 2-4 weeks. One ask per touch, a call as the default first ask.

### Phase 4: Draft in the voice, with provenance

Write each touch against the voice directory: tonal pillars for register, the writing standard's
Do half for mechanics, the Avoid half as a ban list. Ground every load-bearing line:

- **Openers come from the signal**, specific and dated, without fake familiarity. Reference the
  public fact, not a pretended relationship.
- **The middle comes from the ICP:** the trigger's logic, the success factors, the how-to-speak
  rules. Address the champion's real barrier, not the product's feature list.
- **The ask is one clear next step**, a call by default, and the final touch closes flat: no guilt,
  no "just checking in."

Then annotate: each touch carries provenance references (signal, ICP trigger, voice pillar,
judgment call) so a reviewer can trace every line to its source. Judgment calls get named
explicitly (what was deliberately left out, and why).

### Phase 5: Verify mechanically and package

Encode the sequence as `sequence.json` (`references/output-template.md`) and run
`scripts/sequence_gate.py`: it checks freshness, touch caps, word counts, one-ask, annotation
coverage, banned phrases (the universal slop list), the voice's own Avoid words, and role-level
targeting, then passes or fails with reasons. A sequence that fails gets fixed or refused, never
shipped. Package the annotated human-readable sequence plus the JSON.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/sequence_gate.py` | Deterministic gate: freshness, caps, word counts, asks, annotations, slop phrases, voice Avoid words | None | None |

The split holds across the repo: judgment and drafting are reasoning work; enforcement is
deterministic, repeatable, and auditable. The gate reads the voice guide's Avoid list as its ban
file, which is the voice directory feeding the machine directly.

## Failure modes to avoid (the quality bar)

- **Signal name-dropping.** "Congrats on the raise" with no trigger logic is the signature of AI
  slop. The mapping must be written out or the send refused.
- **Fake familiarity.** No pretended relationships, no "I have been following your work."
- **Cold-touching the veto holder.** The CISO hears from security proof, not from a sequence.
- **Stale signals.** A dated why-now older than the gate window is context, not outreach fuel.
- **Multiple asks, or none.** One ask per touch; a call is the default first ask.
- **Voice drift.** The brand's Avoid list is binding; hype words fail the gate mechanically.
- **Sending to the reject pile.** Disqualified, nurture, and existing-relationship lanes are
  refusals, not loopholes.
- **Volume worship.** An enterprise-ABM motion is five touches to one role, not a 20-touch blast
  to the committee.

## Bundled references

- `references/gates-and-motions.md`: the judgment checks behind the gate, the motion archetypes
  with touch structures, and the compliance and deliverability floor. Read at Phases 2-3.
- `references/output-template.md`: the `sequence.json` schema the gate script consumes and the
  annotated-sequence format. Read at Phases 4-5.
- `examples/cohere/`: the composed system end to end. A gate-passing partner-motion sequence for
  TELUS written in Cohere's extracted voice with per-line provenance, and a no-send verdict for
  CIBC (the list's strongest-looking bank) because its signal is 14 months stale. The refusal is
  the point.

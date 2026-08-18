---
name: content-quality-check
description: >
  Editorial QA pass that catches AI tells, template language, hollow hedges, weak closers, and
  brand-voice violations in any draft before it publishes. Runs a deterministic linter
  (slop phrases, LLM-overrepresented words, "not just X, it's Y" reframes, em-dash chaining,
  rhetorical-question openers, announcement cliches, the brand's own Avoid list) and then an
  editorial judgment pass (throat-clearing openers, closers that restate the open, claims without
  proof, specificity, voice-pillar conformance). Reports findings by severity with line references
  and a fix per flag; rewrites only on request. Use whenever the user says "review this draft",
  "QA this post", "check for AI tells", "does this sound AI-written", "editorial review", "content
  quality check", "de-slop this", or is about to publish copy. Enforces the standard that
  brand-voice-guide builds; works standalone with the universal checklist when no voice directory
  exists.
---

# Content Quality Check

The QA gate a draft passes before it publishes. This skill is opinionated about one thing:
**readers now pattern-match AI tells in seconds, and every tell that ships spends the brand's
credibility.** The check exists to catch what the writer can no longer see in their own draft.

It reports before it rewrites. The deliverable is a severity-tagged review with a fix per flag;
wholesale rewriting happens only when asked, because the writer owns the draft.

## What this consumes

| Input | Why | If missing |
|---|---|---|
| The draft | The thing under review | Required |
| Channel and audience | Calibrates length, register, and which rules bind hardest | Ask in one line |
| Voice directory (optional) | `brand-voice-guide` output: the pillars to check conformance against and the Avoid list the linter enforces | Run with the universal checklist only, and say so |

The division of labor across the repo holds: `brand-voice-guide` builds the standard, this skill
enforces it on drafts, and `outbound-engine` carries its own sequence-specific gate (this skill
can still review sequence copy as prose).

## The workflow

Four phases. Mechanical first, judgment second, so the model's attention goes where the machine
cannot.

### Phase 1: Intake and calibration

Read the draft, note channel and audience, and locate the voice directory if one exists (pillars
from `voice-core.md`, banned words from the Avoid section of `writing-standard.md`). State the
bar being applied: universal checklist only, or universal plus brand standard.

### Phase 2: Mechanical sweep

Run `scripts/check_content.py` on the draft, with `--avoid` pointing at the brand's Avoid words
when available. The linter catches everything a machine can catch deterministically: slop phrases,
LLM-overrepresented words, "not just X, it's Y" reframes, "let's dive in" openers, announcement
cliches, em-dash chaining, rhetorical-question openers, empty-intensifier density, weak-closer
formulas, and the brand's own banned words. Same draft, same flags, every run.

### Phase 3: Editorial judgment pass

Read the draft as an editor, against `references/detection-checklist.md` section C, for what no
regex can see:

- **The opener:** does the first line earn attention, or does it throat-clear and stage-set?
- **The closer:** does it end flat and forward, or restate the opening as a summary?
- **Proof:** does every claim carry a number, a name, or evidence, or does it float? Flag
  unproven claims as "needs proof"; verifying truth is the writer's job, naming the gap is ours.
- **Specificity:** concrete nouns and real examples over abstractions ("the 300-row
  questionnaire" beats "operational inefficiencies").
- **Template shape:** does the structure read as a filled-in listicle or a piece with an argument?
- **Voice conformance** (when a directory exists): would this pass the brand's distinctiveness
  test, and does each section sound like the pillars or merely avoid the banned words?

### Phase 4: Report, then revise on request

Deliver the review: verdict (**publish / revise / rework**), the linter output verbatim, judgment
findings with line references, and a concrete fix per flag. If the user asks for the revision,
apply the fixes, re-run the linter until clean, and hand back a before/after so the changes are
inspectable. The final gate is mechanical PASS plus an editor's clear.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/check_content.py` | Deterministic content linter: universal tells plus the brand's Avoid list, severity-tagged with line numbers | None | None |

## Failure modes to avoid (the quality bar)

- **Silent rewriting.** The review comes first; the writer decides what to accept.
- **Flag-counting without fixes.** Every flag ships with its fix, or it is nagging, not QA.
- **Enforcing taste as rule.** The checklist distinguishes severities; a LOW is advisory and says
  so. Real lists of three real things are not tricolon abuse.
- **Universal-only when a standard exists.** If the brand has a voice directory, checking against
  the generic list alone is a half-done job.
- **Missing the structural tells.** A draft can pass every word-level check and still read as a
  template; the judgment pass exists for exactly that.
- **Grading truth.** "Needs proof" is a finding; fact-checking the proof is out of scope and
  said so.

## Bundled references

- `references/detection-checklist.md`: the full catalog, severity-tagged: A (mechanical, the
  linter's spec), B (word and phrase lists), C (judgment checks). Read at Phases 2-3.
- `examples/cohere/`: a deliberately slop-ridden Cohere announcement draft, the review that
  catches 20+ flags across both passes, and the revised draft in Cohere's actual voice that the
  linter passes clean.

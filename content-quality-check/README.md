# Content Quality Check

The QA gate a draft passes before it publishes: a deterministic linter for AI tells and template
language, then an editorial judgment pass for everything a regex cannot see.

## What it does

Point it at any draft (a post, a landing page, an email, an announcement) and it runs two passes:

1. **Mechanical sweep** (`scripts/check_content.py`, stdlib-only): "not just X, it's Y" reframes
   (cross-line, contractions included), "let's dive in" openers, announcement cliches,
   rhetorical-question openers, em-dash chaining, hollow hedges, LLM-overrepresented words,
   intensifier density, weak closers, and, when a [`brand-voice-guide`](../brand-voice-guide/)
   directory exists, the brand's own Avoid list at HIGH severity. Verdict with line numbers, same
   flags every run.
2. **Editorial judgment pass**: does the opener earn attention or throat-clear, does the closer
   recap, does every claim carry proof, is anything specific, is the structure a template, and
   does the piece pass the brand's own distinctiveness test.

The deliverable is a review with a fix per flag. It rewrites only when asked, because the writer
owns the draft.

## What it does NOT do

It does not build the voice standard (that is `brand-voice-guide`; this skill enforces it), it
does not fact-check the proof behind claims (it flags "needs proof" and says so), and it does not
silently rewrite.

## Who it's for

Anyone publishing under a brand: founders, marketers, and content teams who want the tells caught
before readers catch them.

## How to use it

1. Copy this folder into `~/.claude/skills/content-quality-check/`.
2. Point it at a draft: *"QA this post before I publish."* It sweeps, judges, and reports.
3. Run the linter yourself anytime:

```
python3 scripts/check_content.py draft.md --avoid your-avoid-words.txt
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and four-phase workflow |
| `references/detection-checklist.md` | The full catalog: mechanical checks, the word and phrase lists, and the judgment checks, severity-tagged |
| `scripts/check_content.py` | The deterministic linter |
| `examples/cohere/` | A slop-ridden announcement (23 flags), the review, and the revision in Cohere's voice that passes clean |

## Composes with

- [`brand-voice-guide`](../brand-voice-guide/): its writing-standard Avoid list is this skill's
  HIGH-severity ban file; its pillars are the conformance bar in the judgment pass.
- [`outbound-engine`](../outbound-engine/): sequences carry their own gate; this skill reviews any
  other content the system produces.

---
name: brand-voice-guide
description: >
  Extract a brand's voice from its real writing and build a structured voice directory a team (or
  an AI agent) can write from consistently. Harvests existing content — homepage, blog, posts,
  emails, changelog — into voice-core rules, per-channel guidance, and a writing standard whose Avoid
  section names the banned words and voice-killing patterns, each grounded in verbatim samples.
  Interviews the user only to fill what the
  samples can't answer. Use whenever the user says "brand voice", "voice guide", "tone of voice",
  "voice and tone", "brand voice guide", "define our voice", "extract our voice", "style guide",
  "voice standard", or wants to document how their brand sounds so content stays on-brand at scale.
  Works across industries and channels. Builds the guide; it does not police drafts — that is the
  job of a separate content-quality-check skill.
---

# Brand Voice Guide

Extract how a brand actually sounds from what it has actually written, and turn it into a directory
that a copywriter, a new hire, or a Claude agent can produce on-brand content from. This skill is
opinionated about one thing: **a voice guide is extracted from real writing, not invented from
adjectives.** "We're bold, human, and authentic" describes nothing. A verbatim line the brand wrote,
and a rule named from it, describes everything.

The output is a **directory of reference files** (not a single essay), so it can be consulted
modularly at the moment of writing — the voice-core rules always, the relevant channel file for the
piece at hand. It mirrors the structure a production content system consults before generating a word.

## What this builds (and what it doesn't)

- **It builds** the voice directory: `voice-core.md` (the character), `writing-standard.md` (the
  concrete rules — a *Do* half and a severity-tagged *Avoid* half), per-channel files,
  `real-examples.md`, plus light `about-company.md` / `icp.md` context.
- **It does not check drafts.** Governing new content against the guide (AI tells, template language,
  brand-rule violations) is the job of a separate `content-quality-check` skill. This skill produces
  the standard that skill enforces — the *Avoid* section of `writing-standard.md` is the part it reads.

## Inputs (harvest first, ask only for the gaps)

The skill is harvest-first: it extracts as much as possible from existing writing before asking the
user anything. Collect what exists; note what's missing.

| Input | Why it matters | If missing |
|---|---|---|
| Brand / product one-liner | Anchors what "on-brand" means | Ask; don't proceed without it |
| Writing samples (the harvest) | The evidence base — voice is extracted from these | Interview mode (see Phase 3) |
| Active channels + which are intentional | Determines which channel files to build | Ask; build files only for intentional channels |
| Existing ICP / audience | Voice is aimed at a reader | If `icp-research` was run, drop its output in as `icp.md`; else gather lightly |
| A published piece the brand is proud of | The clearest signal of the "real" voice | Ask the user to name one |

The single most useful ask: **"Point me at the two or three things you've published that felt most
like you — and one thing in your space that makes you cringe."** The contrast defines the voice.

## The workflow

Five phases. Harvest builds the draft; the interview only fills gaps; the Avoid rules come last.
Show the user the tagged samples (end of Phase 2) and the draft files (Phase 4) before finalizing.

### Phase 1 — Scope and intake

1. Confirm the brand one-liner and who the writing is for (reader/ICP).
2. List every channel the brand publishes on, and mark each **intentional** (a real voice, published
   with purpose) vs. **passive** (occasional, cross-posted without thought). Build channel files only
   for intentional ones. A brand whose Discord is its community needs `voice-discord.md` more than a
   twice-a-year Instagram needs `voice-instagram.md`.
3. Inventory the writing samples on hand; if there's little to no published content, switch to
   **interview mode** (Phase 3 does the discovery instead of the harvest).

### Phase 2 — Harvest (extract voice from the samples)

Run the extraction passes in `references/extraction-passes.md`. In short: read everything and pull,
**verbatim**, the language that could only come from this brand. Do not paraphrase — the specificity
is the value. Capture:

- How they describe what they do (exact phrases), and any stated belief that could start an argument.
- The **voice patterns that repeat**: how pieces open, how they close, sentence length and rhythm,
  the relationship to the reader (explain / challenge / accompany), where the writing is most alive
  vs. most performed.
- **Channel differences**: how the register shifts between, say, email and LinkedIn.
- Recurring **mechanics**: preferred verbs and nouns, banned words, capitalization and number habits.

Output of this phase: a tagged bank of verbatim lines, grouped by the file each will feed. Show it.

### Phase 3 — Interview to fill gaps (only what samples can't answer)

Some things rarely appear in polished content. Ask targeted questions from
`references/question-bank.md` only where the harvest came up empty. The highest-value ones:

- **The contrarian belief.** "What does the brand believe that most competitors won't say out loud —
  the thing you'd say at dinner that might start an argument?"
- **The relationship decision.** "If the brand were a person at a dinner table, what role does it
  play?" Offer contrast pairs when they stall (mentor vs. peer; simplify vs. sit-in-complexity;
  projects-confidence vs. owns-the-uncertainty; challenges the reader vs. meets them where they are).
  The *defense* of the choice is more useful than the choice.
- **Who it's NOT for**, and **what the brand would never say** even if it worked for others.
- **The one-sentence summary.** "Write the sentence you'd want someone to say about the brand after
  three months of your content," then push once: "which word in that isn't quite true?"

In interview mode (no content to harvest), Phase 3 carries the whole discovery: work the question bank
front to back, and lean on the AI-draft-reaction technique below to surface anti-patterns.

### Phase 4 — Build the directory

Assemble each file using `references/output-templates.md`. Non-negotiable rules:

- **Every file contains at least one real, verbatim sample the brand produced.** A voice file with no
  real language is a horoscope. If you can't ground a file, it's a gap, not a guess.
- **Every tonal pillar gets a named rule plus a verbatim do (and ideally a don't).**
- **Use the brand's exact words** for rules ("we never sound like a professor who needs to impress
  you" goes in verbatim, not softened to "avoids academic tone").
- Build channel files one at a time; when a brand has 4+ channels, do the 2-3 highest-frequency ones
  first and add the rest in a second pass rather than producing shallow files for all of them.

### Phase 5 — The Avoid rules (last) and verification

Build the **Avoid** section of `writing-standard.md` last, because an "avoid" only has meaning against
a defined voice. It's the single home for banned words and voice-killing patterns (there is no separate
anti-patterns file). Build it from three sources (detail in `references/output-templates.md`):

1. A **universal starter list** of generic/AI tells, which the user confirms or overrides.
2. The **AI-draft-reaction**: generate a short, styleless AI draft on one of the brand's own topics
   and have the user mark every line that makes them wince. These brand-specific tells are the most
   valuable ones and appear on no universal list.
3. The **one industry phrase** the brand refuses to use.

Tag each entry with severity (HIGH/MEDIUM/LOW) so the future `content-quality-check` skill can act on
it. Then verify: read back the key decisions ("here's who you told me you are / who you're for / how
you show up / what you never do — anything that doesn't sound exactly like you?"), and run the
**distinctiveness test** on every voice file: *if a line could be lifted onto a competitor's site
unchanged, it isn't voice — rewrite or cut it.* Close with a Gaps note (what's assumed vs. grounded).

## Output

A directory, built with `references/output-templates.md`:

```
brand-voice/
├── about-company.md          # what it does, why it exists, the contrarian belief
├── icp.md                    # who it writes for (drop in icp-research output if you have it)
├── voice-core.md             # the character: tonal pillars (each with a verbatim sample), sentence
│                             #   rules, "persona we are NOT", the distinctiveness test
├── writing-standard.md       # the concrete rules — Do (words to use, formatting, caps, numbers) and
│                             #   Avoid (banned words + voice-killing patterns, severity-tagged; built last)
├── voice-<channel>.md        # one per INTENTIONAL channel: structure, hook patterns used/avoided,
│                             #   length targets, formatting
└── real-examples.md          # a small library of in-voice lines to reference for shape
```

Channel files are added only for channels the brand actively and intentionally publishes on. There is
one home for "don't": the Avoid section of `writing-standard.md` (no separate anti-patterns file).

## Composes with other skills

- **icp-research** — if it's been run, use its output as `icp.md` instead of re-gathering. Cross-link.
- **content-quality-check** (planned) — the enforcement side. This skill's `voice-core.md` and the
  Avoid section of `writing-standard.md` are what it checks drafts against.

## Failure modes to avoid (the quality bar)

- **Adjective soup** — "bold, human, authentic." Describes nothing. Every rule needs a verbatim sample.
- **Describing instead of extracting** — writing what the voice *should* be rather than naming what it
  already *is* in the samples.
- **Horoscope files** — a voice file with no real brand language in it.
- **Generic that survives the swap** — a line that could sit on a competitor's site unchanged. Rewrite.
- **Avoid rules written first** — they're meaningless before the voice is defined; build them last.
- **A file per dead channel** — build only for channels published with intent.
- **Paraphrasing the user's exact words** — the specificity is the whole value; keep it verbatim.

## Bundled references

- `references/extraction-passes.md` — the harvest engine: what to collect, and the passes that draft
  each file. Read at Phase 2.
- `references/question-bank.md` — the gap-filling questions, mapped to each file. Read at Phase 3.
- `references/output-templates.md` — the exact shape of every file, plus the universal Avoid starter
  list. Read at Phase 4/5.
- `examples/` — two worked examples built from real public copy. Each is a brand folder holding the
  harvest (`input.md`) and the **full multi-file voice directory** the skill produced
  (`brand-voice/`): `examples/linear/` (terse, engineer-precise) and `examples/notion/` (warm,
  playful-clear). Same category, different voices — the contrast shows the skill capturing what's
  actually distinctive.

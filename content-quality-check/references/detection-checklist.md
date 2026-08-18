# Detection checklist

The full catalog the QA pass runs. Section A is the linter's spec (mechanical, deterministic).
Section B holds the word and phrase lists it scans for. Section C is the judgment pass, the checks
no regex can run. Severities: **HIGH** blocks publishing until fixed, **MEDIUM** means revise
unless deliberate and defensible, **LOW** is advisory.

Calibration note: these patterns are flagged because they are over-represented in generated text
and template writing, not because any single instance is a crime. The linter counts and locates;
the editor decides. Severity encodes how rarely the pattern survives a good edit.

## A. Mechanical checks (what the linter enforces)

| Check | Severity | Why |
|---|---|---|
| "Not just X, it's Y" reframe (also "more than just") | HIGH | The signature faux-insight construction; a claim pretending to be a revelation |
| "Let's dive in / let me break down" openers | HIGH | Telegraphs a generated answer, not a written piece |
| Announcement cliche ("thrilled/excited/proud to announce") | HIGH | The most template opener in corporate writing |
| Rhetorical-question opener | HIGH | Banned by the house writing standard; openers earn attention with a claim, not a quiz |
| Em-dash chaining (3+ in one paragraph) | HIGH | Models lean on em dashes to fake cadence; humans rarely cluster them |
| Brand Avoid-list words (when a voice directory exists) | HIGH | The brand already decided; the linter just remembers |
| Hollow stage-setting phrases (section B) | MEDIUM | Words that fill space before the point |
| LLM-overrepresented words (section B) | MEDIUM | Individually innocent, collectively a fingerprint |
| Empty intensifiers above 1 per 200 words | MEDIUM | "Truly" and "genuinely" weaken the thing they decorate |
| Weak-closer formulas ("in conclusion", "in summary") | MEDIUM | A close should land forward, not recap |
| Exclamation in the final line | LOW | The flat close is the house pattern; hype endings read as reach |
| Single-word tricolons ("faster, smarter, and safer"), 2+ per piece | LOW | Threes are the model's default rhythm; verify each is a real list of real things |
| Question-then-answer scaffolding, repeated | LOW | Fine once; twice reads as an outline that never became prose |

## B. The lists

**Stage-setting and hollow hedges (MEDIUM):** "in today's fast-paced world", "in today's rapidly
evolving", "in the ever-evolving landscape", "in the realm of", "in the world of", "navigating the
complexities of", "it's important to note", "it's worth noting", "at the end of the day", "when it
comes to", "in an era of".

**LLM-overrepresented words (MEDIUM):** delve, delving, leverage (as a verb), seamless, seamlessly,
robust, unlock, unleash, empower, elevate, harness, transformative, revolutionize, game-changer,
game-changing, cutting-edge, testament, tapestry, beacon, pivotal, supercharge.

**Empty intensifiers (MEDIUM, density-checked):** truly, genuinely, absolutely, incredibly, really.

**Weak closers (MEDIUM):** "in conclusion", "in summary", "to sum up", "ultimately, ", "the future
of ... is here".

When a brand voice directory exists, append the Avoid words from its `writing-standard.md`; those
scan at HIGH because the brand already made the decision.

## C. Judgment checks (the editorial pass)

1. **The opener earns attention or it goes.** A first line that stage-sets, defines the topic, or
   asks the reader a question is throat-clearing. The test: delete the first paragraph and see if
   the piece gets better. It usually does.
2. **The closer moves forward.** A close that restates the opening is a summary, not an ending.
   The house pattern is the flat close: one concrete forward statement, no hype, no recap.
3. **Claims carry proof.** Every superlative and every outcome claim needs a number, a name, or a
   source within reach. Flag as "needs proof"; do not fact-check the proof itself, and say so.
4. **Specific beats abstract.** "Operational efficiency gains" is filler; "the 300-row security
   questionnaire that ate an engineer's week" is writing. Flag abstractions where a concrete
   exists.
5. **Template shape.** Uniform paragraph lengths, a numbered list where an argument should be,
   sections that could be reordered without loss: the structure of a filled-in template rather
   than a piece with a spine.
6. **Voice conformance** (when a directory exists). Two tests from the brand's own guide: the
   distinctiveness test (could a competitor ship this line unchanged?) and pillar conformance
   (does the register match the pillars, or does it merely avoid the banned words?).
7. **One idea per paragraph.** Paragraphs that pivot mid-way are drafts of two paragraphs.
8. **Hedge stacking.** "Can potentially help to" is three hedges deep; pick a claim and make it.

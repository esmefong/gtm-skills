# Output templates

The exact shape of every file in the voice directory. Fill each from harvested language and interview
answers. **Every file must contain at least one real, verbatim sample the brand produced** — a voice
file with no real language is a horoscope. Copy the headings; keep samples in the brand's exact words.

The directory:

```
brand-voice/
├── about-company.md
├── icp.md
├── voice-core.md             (the character)
├── writing-standard.md       (the concrete rules: Do + Avoid — built after the voice is defined)
├── voice-<channel>.md        (one per intentional channel)
└── real-examples.md
```

Build channel files only for channels the brand publishes on with intent.

Two files carry the "don't" guidance together, on purpose: `voice-core.md` defines the *character*,
`writing-standard.md` holds the *concrete rules*. There is exactly one home for banned words and
voice-killing patterns — the Avoid section of `writing-standard.md` — so nothing is listed twice.

---

## `voice-core.md` — the anchor file (the character)

```markdown
# Voice — Core (Universal)
Applies to every channel. Channel files may extend; never contradict.

## 1. Tonal pillars
[3-5 named pillars. Each is a short name + one line + a VERBATIM sample the brand actually wrote.]
- **[Pillar name].** [One-line definition.] Sample: *"[verbatim line from the brand]"*

## 2. Sentence-level rules
[The rhythm that recurs in the real writing. e.g. default length, one idea per sentence, cut filler.]

## 3. Persona we are NOT
[3-5 adjacent voices the brand is often mistaken for but deliberately isn't. Sharpens by contrast.]

## 4. The distinctiveness test
[One sentence. e.g. "If a line could be lifted onto a competitor's site unchanged, rewrite it."]
```

The pillars are the heart. Name what's *distinctive*, not what's nice — "warm" is generic; "explains
the hard thing without dumbing it down" is a pillar. Each needs a real sample or it isn't earned.
(Specific banned words live in `writing-standard.md`, not here — keep voice-core about character.)

---

## `writing-standard.md` — the concrete rules (Do + Avoid)

Built *after* the voice is defined, because an "avoid" only has meaning against a defined voice. Holds
both the positive mechanics and the single, severity-tagged list of what to avoid.

```markdown
# Writing Standard
The concrete rules. Apply after the voice rules in voice-core.md.

## Do

### 1. Words we use        [signature verbs and concrete nouns, with an in-voice sample line]
### 2. Sentence rules      [active voice, contractions, one idea per paragraph, etc.]
### 3. Formatting          [bullets, bold, code, links, emoji policy]
### 4. Capitalization      [headline case, product/feature naming]
### 5. Numbers             [digits vs. words, currency/percent formatting, rounding]

## Avoid
The single home for banned words and voice-killing patterns. Tag severity so the future
content-quality-check skill can act on it: HIGH (never ship) / MEDIUM (revise unless intentional) /
LOW (advisory). For each, say what the brand does *instead*.

### Banned words
[Brand-specific words to avoid, with why. e.g. "leverage (v.), seamless, revolutionary."]

### Voice-killing patterns
- **[Pattern].** Severity. Why it breaks this voice: [...]. Instead: [what the brand does]. [+ example]
```

Build the Avoid section from three sources, in order:
1. **Universal starter list** (below) — confirm each as banned for this brand, or mark a deliberate
   exception with a one-line reason.
2. **AI-draft-reaction** — the brand-specific tells the user flagged in a styleless AI draft. These are
   the most valuable; record what the brand does *instead*.
3. **The one industry phrase** the brand refuses to use.

### Universal starter list (seed, then let the brand override)
Generic and AI tells to test against. *(The deep, evolving AI-tells detector is the separate
`content-quality-check` skill's job — keep only the ones that matter for this brand's voice.)*
- "It's not just X, it's Y" faux-insight reframes
- Em-dash chaining (3+ in a paragraph)
- "Let me / Let's [verb]" openers ("let's dive in")
- Tricolon triplets ("faster, smarter, more reliable")
- Hollow hedges ("in today's fast-paced world", "navigating the complexities of")
- Overused words: *delve, leverage (v.), seamless, robust, unlock, empower, elevate, game-changer,
  revolutionary, transformative, ecosystem (vague)*
- Empty intensifiers (*truly, absolutely, genuinely*) more than ~1 per 200 words
- Announcement clichés ("we're thrilled to announce")
- Question-then-answer scaffolding used repeatedly
- A closing summary that just restates the opener

---

## `voice-<channel>.md` — one per intentional channel

```markdown
# Voice — [Channel]
Extends `voice-core.md`. Use for [what this channel is for / who reads it].

## 1. Structure
[The shape a piece takes here: opener → middle → close. What the opener does; how it closes.]

## 2. Length + format
[Length targets, formatting habits — line breaks, emoji policy, tags, bold usage.]

## 3. Hook patterns we use
[2-4 named opener patterns, each with a verbatim sample.]

## 4. Hook patterns we avoid
[Openers that break the voice on this channel.]

## 5. Content mix
[The promotional / educational / personal ratio, and what "worked" looks like here — real metric of
success, not vanity.]
```

---

## `about-company.md` and `icp.md`
Keep these light — voice context, not a full brand or audience study. `about-company.md`: the plain-
sentence what, the origin frustration, proudest specifics, and the **contrarian belief** (prime voice
fuel). `icp.md`: the specific reader in their own words — or, if `icp-research` was run, drop its
output in here directly.

## `real-examples.md`
A small library (5-10) of in-voice lines to reference for *shape*, tagged by channel. What to learn
from each: how it opens, its rhythm, the one move that makes it sound like this brand and no other.

# Extraction passes (the harvest engine)

How to pull a voice out of existing content. This is the default engine of the skill: extract as much
as possible before asking the user anything. Adapted from a content-harvest method that builds ~80% of
a voice directory from published writing alone. Read this at Phase 2.

If the brand has little or no published content, skip to interview mode (`question-bank.md`) — there's
nothing to harvest.

---

## Step 1 — Collect everything

Gather (or ask the user to point you at) whatever exists, then sort by channel:

- The homepage, About page, and every page with a call to action (each conversion page gets its own pass)
- The last ~15-20 social posts per active channel
- The last ~5-10 emails / newsletter issues
- Published articles, blog posts, changelog entries, docs with personality
- Transcripts of talks, podcasts, or videos (how they talk when not writing is often the clearest voice)
- Sales decks or one-pagers, if any

Note which pieces the user volunteered vs. which you found. Volunteered pieces reveal what they're
proudest of — weight them.

---

## Step 2 — Run the passes

Each pass reads the whole corpus with one question in mind and drafts specific files. Capture language
**verbatim**; never paraphrase into a description.

### Pass 1 — Company + audience signals → `about-company.md`, `icp.md`
Look for: how they describe what they do (exact phrases), who they address and how, the problems they
name, any numbers or named outcomes, and any stated belief or position that could start an argument.
*(If `icp-research` has already produced an ICP, use it as `icp.md` and skip the audience half here.)*

### Pass 2 — Voice patterns → `voice-core.md`
Look for what *repeats*:
- **Openers.** What does the first line almost always do — state a fact, take a stance, name a problem,
  greet? (Distinctive brands rarely greet.)
- **Closers.** Summary, forward momentum, a provocation, a question?
- **Sentence rhythm.** Short and declarative? Long and layered? A signature alternation?
- **Relationship to the reader.** Do they explain, challenge, or accompany?
- **Aliveness.** Mark the lines where the writing is most alive vs. most performed/corporate. The alive
  ones are the real voice; the performed ones are what to cut.
Name the patterns. Draft the tonal pillars from what recurs, each with a verbatim sample.

### Pass 3 — Channel-specific habits → `voice-<channel>.md`
Sort by channel and note what changes: does the register shift between email and LinkedIn? What does
the subject-line vocabulary reveal? Which content types dominate each channel? What does the brand never
seem to do on each? Draft one file per intentional channel.

### Pass 4 — Conversion pages → `voice-landing-page.md` (one per distinct page)
For each page with a CTA: what is the headline doing (claiming / questioning / naming the problem /
stating the outcome)? Where does it open (problem / outcome / who-it's-for)? What proof appears, and in
what order? What does the CTA imply about the reader's next step? Flag any line incongruent with the
rest of the voice. If existing page copy is weak, note it as a gap for the interview.

### Pass 5 — Avoid audit → the Avoid section of `writing-standard.md`
Here the universal starter list (in `output-templates.md`) is *your* audit tool, not a client
worksheet. Mark each item **present** (recurs across multiple pieces), **absent** (never appears — the
brand is already avoiding it), or **intentional exception** (appears but reads as deliberate). Only
promote a pattern to the Avoid section if it recurs, not on a single instance.

Then generate one short, styleless AI draft on a core brand topic and compare it line by line to the
real content. Every point where the brand's real writing is clearly stronger is an anti-pattern
candidate — record what the brand does *instead*. The absence of a generic pattern in their writing is
itself signal: they're already avoiding it.

---

## Step 3 — Flag the gaps

Before going to the user, list what the content couldn't tell you. Common gaps (they become the
Phase 3 interview questions):

- The contrarian belief — rarely stated outright in polished content.
- The reader's emotional state at the moment of discovery.
- What the brand avoids *by choice* vs. *by habit*.
- Channel rules the brand follows consciously but never wrote down.

---

## Step 4 — Draft, then confirm

Build each file from the harvest, using the brand's words wherever possible. Where you must paraphrase,
ask: *does this still sound like them?* Present the drafts plus only the gap questions. One focused
round of corrections finalizes each file — if a file needs more than one round, the extraction was too
shallow; go back to the source material, not to the user.

# Brand Voice Guide

Extract how a brand actually sounds from what it has actually written, and turn it into a directory a
team — or a Claude agent — can produce on-brand content from.

## What it does

Feed it a brand's real writing (homepage, blog, posts, emails, changelog) and it builds a **voice
directory**: `voice-core.md` (tonal pillars, each anchored to a verbatim sample), a
`writing-standard.md` (the concrete rules — a *Do* half and a severity-tagged *Avoid* half),
per-channel files, and `real-examples.md`. It harvests everything it can from the samples first, then
interviews you only to fill the gaps.

It's opinionated about one thing: **a voice guide is extracted from real writing, not invented from
adjectives.** "Bold, human, authentic" describes nothing; a line the brand actually wrote, and a rule
named from it, describes everything.

## What it does NOT do

It builds the standard; it doesn't police drafts. Checking new content against the guide (AI tells,
template language, brand-rule violations) is the job of a separate `content-quality-check` skill. This
skill produces the standard that one enforces.

## Who it's for

Founders, marketers, and content teams who need their voice documented so it survives new hires,
freelancers, and AI drafting. Works across industries and channels.

## How to use it

1. Copy this folder into `~/.claude/skills/brand-voice-guide/`.
2. Point it at your writing: *"Build a voice guide from our homepage, last 15 posts, and recent
   newsletters."*
3. It harvests, shows you the tagged samples, asks a few gap questions, and builds the directory —
   every file grounded in your real language.

No published content yet? It runs in interview mode and builds the guide from a guided conversation.

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and workflow |
| `references/extraction-passes.md` | The harvest engine — passes that draft each file from samples |
| `references/question-bank.md` | Gap-filling / interview questions, mapped to each file |
| `references/output-templates.md` | The exact shape of every file + a universal Avoid starter list |
| `examples/linear/` | **Linear** — the harvest (`input.md`) + the full voice directory it produced (`brand-voice/`); terse, engineer-precise |
| `examples/notion/` | **Notion** — the harvest + full voice directory; warm, playful-clear |

The two examples are the same category with clearly different voices — read the guides side by side to
see the skill capturing what's actually distinctive.

## Composes with

- [`icp-research`](../icp-research/) — drop its output in as the `icp.md` context file.
- `content-quality-check` (planned) — the enforcement side that checks drafts against this guide.

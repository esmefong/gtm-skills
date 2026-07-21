# GTM Skills

Reusable AI skills for the operational side of go-to-market: finding the buyer, positioning to them,
sounding like the brand, reaching them, and prioritizing where effort goes. Built in the Claude Code
skill format. Each skill is a folder with a SKILL.md spec and a worked example showing real input and
output. Copy a folder into `~/.claude/skills/` and it runs.

Each skill turns a repeatable go-to-market motion into something a team, or an AI agent, can run.
Generalized from GTM systems I've built in production and sanitized so they work for any company.

## Skills

| Skill | What it does | Status |
|---|---|---|
| [icp-research](icp-research/) | Turns raw first-party and public signal into an operational ICP: situation triggers, a how-to-win plan, and (for team buyers) a buying-committee map and account scoring rubric | Shipped |
| [brand-voice-guide](brand-voice-guide/) | Extracts a brand's voice from its real writing into a structured voice directory: tonal pillars, per-channel rules, and a writing standard with a severity-tagged list of what to avoid, all grounded in verbatim samples | Shipped |
| account-sourcing | Turns an ICP into a ranked target-account list with receipts: translates ICP criteria into queries on public sources (job postings, press, funding), scores and disqualifies accounts, and tags each with a dated why-now signal. Consumes icp-research | Next |
| outbound-engine | Drafts committee-aware outreach for sourced accounts: maps each live signal to the ICP's triggers, writes sequences in the brand voice, and refuses weak sends with a no-send gate. Consumes account-sourcing, icp-research, and brand-voice-guide | Planned |
| positioning-message-house | Builds a positioning message house for a company: one core bet translated into a message matrix across offerings and go-to-market functions, plus a generation system that emits battlecards and objection docs | Planned |
| market-prioritization | Weighted model that scores and routes accounts or markets against your ICP and criteria | Planned |
| content-quality-check | Editorial QA pass that catches template language, weak closers, and AI tells before publishing | Planned |
| reengagement-segmenter | Segments a lapsed audience by their actual blocker and drafts a sequence per segment | Planned |
| personalized-content-pipeline | Produces branded, voice-checked content per customer from a structured brief, with per-customer state | Planned |
| validation-tracker | Weekly operating rhythm: checks progress against benchmarks and keeps an append-only decision log | Planned |

## Why these exist

Case studies for the systems behind these skills are at [esmefong.com](https://esmefong.com).

## License

MIT

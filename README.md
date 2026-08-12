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
| [account-sourcing](account-sourcing/) | Turns an ICP into a ranked target-account list with receipts: translates ICP criteria into queries on public sources, scores and disqualifies accounts, tags dated why-now signals, and routes each account to an owner with a next action. Ships with runnable scoring, hiring-signal, and briefing scripts. Consumes icp-research | Shipped |
| [outbound-engine](outbound-engine/) | Drafts committee-aware outreach for sourced accounts: maps each live signal to the ICP's triggers, writes voice-matched sequences with per-line provenance, and refuses weak sends with a mechanical no-send gate. Consumes account-sourcing, icp-research, and brand-voice-guide | Shipped |
| [positioning-message-house](positioning-message-house/) | Builds a positioning message house: one falsifiable category bet translated into a message matrix across go-to-market functions, committee-aware and voice-checked, plus a generator that emits battlecards and objection docs from the structured house | Shipped |
| [market-prioritization](market-prioritization/) | Ranks candidate markets against weighted criteria, then runs sensitivity analysis to report which rankings survive an argument about the weights, with knockouts and a deprioritized list with reasons | Shipped |
| content-quality-check | Editorial QA pass that catches template language, weak closers, and AI tells before publishing | Planned |
| reengagement-segmenter | Segments a lapsed audience by their actual blocker and drafts a sequence per segment | Planned |
| personalized-content-pipeline | Produces branded, voice-checked content per customer from a structured brief, with per-customer state | Planned |
| validation-tracker | Weekly operating rhythm: checks progress against benchmarks and keeps an append-only decision log | Planned |

## Why these exist

Case studies for the systems behind these skills are at [esmefong.com](https://esmefong.com).

## License

MIT

# GTM Skills

Reusable AI skills for go-to-market work, in the Claude Code skill format. Each skill is a folder with
a SKILL.md spec and a worked example showing real input and output. Copy a folder into
`~/.claude/skills/` and it runs.

These are generalized from marketing systems I ran in production as a solo marketer across three brands:
ICP research, brand voice documentation, content quality review, and lifecycle segmentation. Sanitized
so they work for any team.

## Skills

| Skill | What it does | Status |
|---|---|---|
| [icp-research](icp-research/) | Turns raw first-party and public signal into an operational ICP: situation triggers, a how-to-win plan, and (for team buyers) a buying-committee map and account scoring rubric | Shipped |
| [brand-voice-guide](brand-voice-guide/) | Extracts a brand's voice from its real writing into a structured voice directory: tonal pillars, per-channel rules, and a writing standard with a severity-tagged list of what to avoid, all grounded in verbatim samples | Shipped |
| content-quality-check | Editorial QA pass that catches template language, weak closers, and AI tells before publishing | Planned |
| reengagement-segmenter | Segments a lapsed audience by their actual blocker and drafts a sequence per segment | Planned |
| personalized-content-pipeline | Produces branded, voice-checked content per customer from a structured brief, with per-customer state | Planned |
| market-prioritization | Weighted ranking model that scores candidate markets or segments against your criteria | Planned |
| validation-tracker | Weekly operating rhythm: checks progress against benchmarks and keeps an append-only decision log | Planned |

## Why these exist

Case studies for the systems behind these skills are at [esmefong.com](https://esmefong.com).

## License

MIT

# ICP Research

Turn raw customer signal into an Ideal Customer Profile a copywriter, a media buyer, and a sales rep
can all act on the same day.

## What it does

Feed it your raw research (interview transcripts, survey exports, community/Slack threads, review-site
text, sales-call notes, funnel data) and it produces an **operational ICP**, not a persona poster:

- Situation triggers ("why now") that drive top-of-funnel messaging
- 1-4 buyer segments defined by situation, not demographics
- A **How to Win** plan (USP, narrative, differentiation, channels)
- Insight-to-action routing and a validation plan with a refresh cadence
- **When the buyer is a team:** an **account-level ICP + scoring rubric** with explicit
  disqualifiers, and a **buying-committee map** (champion, economic buyer, technical buyer, end
  user, blocker)

It leads with one principle: **you sell into a situation, not to a demographic.**

## Who it's for

Founders, product marketers, and GTM teams who need an ICP grounded in real customer language rather
than internal opinion. It works **across industries**: consumer/lifestyle, prosumer, B2B SaaS,
fintech, and enterprise. The situation-first core is industry-neutral; the buying-committee and
account-ICP modules switch on only when a team is the buyer.

## How to use it

1. Copy this folder into `~/.claude/skills/icp-research/`.
2. In Claude Code, point it at your research: *"Build an ICP from these interviews and community
   threads."*
3. It runs a five-phase workflow (scope, extract, synthesize, operationalize, validate) and shows
   you its tagged signal and draft segments before writing the final document.

No raw material yet? It can run in hypothesis mode (clearly labelling every assumption) or help you
gather signal first. See `references/research-sources.md`.

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and workflow |
| `references/frameworks.md` | The 5 Rings of Buyer Insight, JTBD + Four Forces, demand-side selling, buying committee |
| `references/output-template.md` | The exact ICP document structure it fills |
| `references/research-sources.md` | How to gather each input, incl. the community/Slack monitoring method + ethics |
| `examples/notion/` | **Notion**: the raw public VoC dump (`input.md`) and the ICP produced from it (`icp.md`); profiles an **individual buyer and a team buyer** in one doc (modules off, then on) |
| `examples/linear/` | **Linear**: the raw dump plus a **team-buyer** ICP (`icp.md`) with the account-ICP and buying-committee modules switched on; built by the opt-in public-data sweep |

## Method credits

Built on the [5 Rings of Buyer Insight](https://www.buyerpersona.com/) (Adele Revella / Buyer Persona
Institute), [Jobs-to-be-Done and the Four Forces](https://jobstobedone.org/) (Bob Moesta, Clayton
Christensen), and demand-side selling (Moesta, Ryan Singer).

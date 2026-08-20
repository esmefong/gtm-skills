# GTM Skills

[![verify](https://github.com/esmefong/gtm-skills/actions/workflows/verify.yml/badge.svg)](https://github.com/esmefong/gtm-skills/actions/workflows/verify.yml)

Built by [Esme Fong](https://esmefong.com). I spent 14 years building data and growth systems, most
recently an AI-enabled marketing operating system across three brands as a solo marketer, which cut
content production cycle time by 50%. This repo is the reusable machinery from those systems,
rebuilt in public: the research, sourcing, outreach, positioning, and quality layers of a
go-to-market engine, each one runnable and checked. I build things like this for teams that want
their GTM to run as a system; I'm at [linkedin.com/in/esmefong](https://linkedin.com/in/esmefong)
and the case studies behind these skills are at [esmefong.com](https://esmefong.com).

Each skill is a folder in the Claude Code skill format: a `SKILL.md` spec an AI agent can execute
(a disciplined SOP with judgment rules baked in), reference docs, worked examples, and plain Python
scripts. If you use Claude Code, copy a folder into `~/.claude/skills/` and it runs. If you don't,
every script is standard-library Python with no API keys and runs anywhere, and every example reads
as a document.

## One company, end to end

All worked examples run on one real company, **Cohere**, from public data only. This is a standing
demonstration, not client work, and I have no affiliation with Cohere; every claim in the examples
carries a cited public source and date. The thread: [icp-research](icp-research/) defines who buys
and why. [account-sourcing](account-sourcing/) turns that ICP into a ranked, evidenced account
list. [outbound-engine](outbound-engine/) turns a live signal into a sequence, or refuses to send.
[brand-voice-guide](brand-voice-guide/) extracts the voice that
[positioning-message-house](positioning-message-house/) writes in and
[content-quality-check](content-quality-check/) enforces. [market-prioritization](market-prioritization/)
decides which markets the whole engine points at.

**Start here:** the sourcing run's
[account-list.md](account-sourcing/examples/cohere/account-list.md), where a review pass catches
the model's own evidence-grading error and demotes two tier-1 accounts. Then the
[CIBC no-send verdict](outbound-engine/examples/cohere/cibc-no-send.md), where the outreach engine
refuses the strongest-looking bank on its own list. (Notion appears as a second example in the two
research skills to show the engines generalize beyond one buyer shape.)

## Verify it in 60 seconds

Every pipeline regenerates from checked-in data; `./verify.sh` reruns all of them and diffs the
outputs, and CI runs it on every push. The fastest single check is the outbound gate:

```bash
cd outbound-engine/examples/cohere
python3 ../../scripts/sequence_gate.py telus-sequence.json --as-of 2026-07-21 --avoid cohere-avoid.txt
python3 ../../scripts/sequence_gate.py cibc-draft-rejected.json --as-of 2026-07-21 --avoid cohere-avoid.txt
```

The first sequence passes. The second is refused with reasons:

```
FAIL: Cohere -> CIBC (enterprise-abm)
  - signal is 420 days old (max 90): stale why-now, refuse or refresh
  - touch 1: slop phrase 'congrats on the'
  - touch 1: voice Avoid word 'revolutionary'
```

The engine refusing its own strongest-looking account is the point: these skills encode when not
to act, which is the judgment most AI GTM tooling skips.

## Skills

| Skill | What it does | Status |
|---|---|---|
| [icp-research](icp-research/) | **Raw research signal to an operational ICP.** Situation triggers, a how-to-win plan, and for team buyers a buying-committee map and scoring rubric | Shipped |
| [brand-voice-guide](brand-voice-guide/) | **Real writing to a voice directory.** Tonal pillars with verbatim samples, per-channel rules, a severity-tagged Avoid list | Shipped |
| [account-sourcing](account-sourcing/) | **ICP to a ranked account list with receipts.** Public-evidence scoring, visible disqualifications, routed owners; scoring, hiring-signal, and briefing scripts | Shipped |
| [outbound-engine](outbound-engine/) | **Live signal to a sequence, or a refusal.** Voice-matched touches with per-line provenance behind a mechanical no-send gate | Shipped |
| [positioning-message-house](positioning-message-house/) | **One falsifiable bet to a message matrix.** Committee-aware translation across GTM functions; generates battlecards and objection docs | Shipped |
| [market-prioritization](market-prioritization/) | **A market slate to a defensible short list.** Weighted scoring plus sensitivity analysis showing which rankings survive an argument about the weights | Shipped |
| [content-quality-check](content-quality-check/) | **A draft to a publish or revise verdict.** AI-tell linter plus an editorial pass, enforcing the brand's own Avoid list | Shipped |
| reengagement-segmenter | Segments a lapsed audience by their actual blocker and drafts a sequence per segment | Planned |
| personalized-content-pipeline | Branded, voice-checked content per customer from a structured brief | Planned |
| validation-tracker | Weekly operating rhythm: benchmarks and an append-only decision log | Planned |

## How these were built

With Claude Code, openly, and then held to the same standard the skills preach: every script runs
against its checked-in example and regenerates it exactly, the worked examples document their own
corrections (a self-audit in account-sourcing demoted two tier-1 accounts when the evidence grading
was caught), and this README clears the repo's own AI-tell linter with zero high or medium flags. The methods come from systems I
ran in production; the examples here are public-data demonstrations of the same machinery.

## License

MIT

# Account Sourcing

Turn an ICP from a strategy document into pipeline: a ranked list of real accounts worth pursuing,
each with public evidence for why, a routed owner and next action, and a visible reject pile.

## What it does

Feed it an account-level ICP (ideally from [`icp-research`](../icp-research/)) and it runs the
first deliverable of go-to-market engineering: translate the ICP into a query spec, map each
criterion to a public source that can answer it, build the account universe, enrich and score with
evidence (value, source, date per fact), visibly disqualify, tag dated why-now signals, and route
every account to an owning team with a specific next action.

It is opinionated about two things: **an account belongs on the list only if you can point to the
evidence, and a list that shows no rejects is hiding its judgment.**

Three runnable, key-free scripts ship with it:

| Script | What it does |
|---|---|
| `scripts/score_accounts.py` | Deterministic scoring: accounts + rubric in, ranked tiers and disqualifications out |
| `scripts/hiring_signal.py` | Live check of public ATS job boards (Greenhouse, Lever, Ashby) for ICP-relevant postings |
| `scripts/render_briefing.py` | Executive briefing from the data: lanes per owning team, next action per card, rejects with reasons |

The output layers deliberately: `accounts.json` (data, feeds Clay or a CRM), `account-list.md`
(working doc with method, self-audit, and gaps), `briefing.html` (the generated executive layer).
Edit the data, not the page.

## What it does NOT do

It does not draft outreach (that is the planned `outbound-engine`, which consumes this skill's
output), and it does not harvest individuals: sourcing stays at the account level, with entry roles
named from the ICP's buying committee. It is built for products bought by organizations; for
individual-buyer products, sourcing means channels and communities, which the ICP's journey section
already maps.

## Who it's for

Founders and GTM, growth, and RevOps teams who need the target-account layer built: the list, the
scoring, the signals, and the routing, grounded in citable evidence rather than a bought CSV.

## How to use it

1. Copy this folder into `~/.claude/skills/account-sourcing/`.
2. Point it at your ICP: *"Build a target account list from our ICP."* It compiles the query spec,
   shows you the source plan, sources and scores the universe, and routes the result.
3. Rerun the scoring or regenerate the briefing anytime from the data:

```
python3 scripts/score_accounts.py accounts.json rubric.yaml --table
python3 scripts/render_briefing.py accounts.json --company "Acme" --accent "#2f5d50"
```

## What's in here

| File | What it is |
|---|---|
| `SKILL.md` | The skill spec and six-phase workflow |
| `references/source-map.md` | Which public source answers which ICP criterion, evidence tiers, ATS endpoints, ethics |
| `references/output-template.md` | The deliverable structure plus the accounts.json and rubric.yaml schemas |
| `scripts/` | The three runnable scripts above, standard library only |
| `examples/cohere/` | A full worked run for Cohere: real accounts, real evidence, a self-audit that demoted two tier-1 rows, and the rendered briefing |

## Composes with

- [`icp-research`](../icp-research/): its account-level ICP is this skill's query spec, and its
  buying committee supplies the entry role per account.
- `outbound-engine` (planned): consumes the qualified accounts and their signals to draft
  committee-aware, voice-matched outreach with [`brand-voice-guide`](../brand-voice-guide/).

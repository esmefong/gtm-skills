# Market prioritization: Cohere

**Constraint:** two markets can carry dedicated GTM capacity over the next four quarters; the rest
get coverage at best.
**Model:** 8 markets, 6 criteria, weights defended below. Scored 2026-07-21 from the repo's own ICP
and account-sourcing run.

> **Real company, public data, illustrative.** A demonstration of the skill, not an official Cohere
> document. Scores are relative judgments with cited evidence, not forecasts.

## The weights, and why

| Criterion | Family | Weight | Why this weight |
|---|---|---|---|
| `buying_readiness` | Access | 25 | The constraint is four quarters, so live mandates beat a larger market still forming an opinion |
| `icp_match` | Fit | 20 | The ICP is unusually sharp (data constraint plus security veto); markets without it default to the hyperscaler regardless of what we do |
| `channel_access` | Access | 20 | This ICP buys through analysts, partners, and procurement, so an existing route in is worth more than in a self-serve motion |
| `competitive_position` | Access | 15 | Below readiness because the specialist position is only defensible where the gate exists |
| `deal_size` | Economics | 10 | Low on purpose: nearly every market here is enterprise-sized, so it barely discriminates |
| `regulatory_risk` | Risk | 10 | Inverted and modest: regulation usually creates our demand rather than blocking it |

## Ranking

| # | Market | Score | Robustness |
|---|---|---|---|
| 1 | Canadian public sector | 96.0 | **robust** |
| 2 | Canadian financial services | 88.0 | contested with sovereign telecom |
| 3 | Sovereign telecom partnerships | 87.0 | contested with financial services and DACH |
| 4 | DACH regulated enterprise | 82.0 | contested with sovereign telecom |
| 5 | Canadian healthcare and insurance | 73.0 | robust |
| 6 | US regulated enterprise | 64.0 | robust |
| 7 | Mid-market SaaS | 44.0 | robust |
| - | Japan enterprise | knocked out | `channel_locked` |

## What the sensitivity analysis says

Perturbing each weight by plus and minus 10 points:

- **Canadian public sector holds first place under every tested weighting.** The federal
  relationship, structural sovereignty requirements, and an unworked provincial and agency layer
  make it the one unambiguous answer on this slate. Resource it.
- **Second place is a coin flip.** Financial services (88.0) and sovereign telecom (87.0) are one
  point apart, and they swap whenever `channel_access`, `competitive_position`, or `icp_match`
  moves. Treating an 88 as a decision over an 87 would be false precision.
- **The decisive question is named:** telecom versus financial services turns on `icp_match`, and
  the underlying question is whether sovereign telcos are **customers or channel**. The ICP
  describes their regulated customers, not the telcos themselves, which is why the score is a 3.
  If the partnership motion is judged as distribution (one deal reaching many regulated buyers)
  rather than as an end sale, telecom wins the slot outright.
- **DACH swaps with telecom on the same criterion,** for the same reason.

## The decision

**Resource Canadian public sector, and settle the telecom-versus-financial-services question before
committing the second slot.** That question is answerable in weeks, not quarters: ask whether one
sovereign telecom partnership would reach more qualified regulated buyers than a direct financial
services motion, using the account-sourcing run as the denominator. The model's job here was to
narrow eight markets to one decision and one question, not to pretend the second slot was already
decided.

Note the compounding option: financial services and telecom are not fully independent, since a
telecom partnership is a route into the same regulated buyers. If the partnership motion proves out,
it may deliver a large share of the financial services opportunity as a side effect.

## Deprioritized, and why

| Market | Why not now | What would bring it back |
|---|---|---|
| DACH regulated enterprise | Strong fit and newly enterable post-merger, but access is still forming and capacity is two | A first reference win, or evidence the Aleph Alpha footprint shortens the sales cycle materially |
| Canadian healthcare and insurance | Perfect ICP fit, slower clock; the insurance half is already covered inside financial services | Provider-side budgets landing, or a provincial health-system mandate |
| US regulated enterprise | Biggest market, worst fit for the wedge: hyperscaler incumbency is strongest and their residency guarantees clear many US reviews | This is the category bet's falsifier; if US security reviews start rejecting hyperscaler residency, the market reopens |
| Mid-market SaaS | An ICP disqualifier: comfortable on public APIs with no data constraint | A regulatory shift that imposes data constraints on mid-market SaaS |
| Japan enterprise | **Knocked out.** Sovereignty demand is real and the market is ready, but the dominant channel is contracted to a competitor (SB OAI Japan, the 50-50 SoftBank and OpenAI venture) | A narrowing of the JV's scope, or a different channel partner with equivalent reach |

## Revisit triggers

Re-run when any of these land: a sovereign partnership announcement (it can move telecom from
contested to decided), a competitor channel lock in another geography (a new knockout), a US
security-review trend that speaks to the falsifier, or a regulation that changes a market's data
constraints. Calendar cadence otherwise: quarterly.

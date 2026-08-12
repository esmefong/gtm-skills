# Criteria library

The criteria to choose from, their scoring anchors, and how to weight them. Read at Phases 2-3.
Pick 4-7 total, spread across families; more than seven and the model stops discriminating because
everything scores near the middle.

## The five families

Every prioritization model answers five questions. A model missing a whole family is usually the
one that produces a bad decision.

| Family | The question | Typical weight range |
|---|---|---|
| **Opportunity** | How much is there to win? | 20-30 |
| **Fit** | Can we actually serve it well? | 20-30 |
| **Access** | Can we get in? | 15-25 |
| **Economics** | Is the money good once we do? | 15-25 |
| **Risk** | What could make this a trap? | 10-20 |

Weights sum to 100. Set them before scoring, and write one defending sentence each.

## Standard criteria and their anchors

Score 1-5. Anchor the scale before scoring so a 4 means the same thing in every row.

### Opportunity

**`market_size`**: addressable spend or account count in the segment.
1 = negligible · 2 = small but real · 3 = meaningful · 4 = large · 5 = the biggest on the slate.

**`growth`**: direction and speed of the underlying demand.
1 = shrinking · 2 = flat · 3 = growing with the economy · 4 = clearly outpacing · 5 = a structural
wave (a regulation, a technology shift, a budget cycle creating new demand).

### Fit

**`icp_match`**: how closely the segment matches the ICP's triggers and profile.
1 = fails core criteria · 3 = partial match, adaptation needed · 5 = the ICP describes them exactly.

**`product_readiness`**: can the product serve this market today, without a build?
1 = needs a new product · 2 = major gaps · 3 = gaps with workarounds · 4 = ready with minor
adaptation · 5 = ready now, with references.

**`reference_proof`**: do we have credible proof for this audience?
1 = none · 3 = adjacent proof that transfers with explanation · 5 = named customers in exactly this
segment.

### Access

**`channel_access`**: do routes to this buyer exist for us?
1 = no route · 2 = cold only · 3 = one working channel · 4 = several, including partners ·
5 = existing partnerships or platform positions that carry us in.

**`competitive_position`**: how contested is it, and how do we stack up?
1 = entrenched incumbent, no wedge · 3 = contested with a real differentiator · 5 = a gap the
competition structurally cannot serve.

**`buying_readiness`**: is this market in-market now, or later?
1 = no budget or mandate · 3 = interest without urgency · 5 = active mandates, live budget, public
initiatives.

### Economics

**`deal_size`**: typical contract value relative to the slate.
1 = lowest · 5 = highest.

**`sales_cycle`**: speed to revenue (**inverted**: faster scores higher).
1 = 18+ months, heavy procurement · 3 = 3-9 months · 5 = weeks.

**`cost_to_serve`**: delivery, support, and compliance burden (**inverted**: lighter scores higher).
1 = heavy custom deployment and ongoing burden · 3 = standard · 5 = self-serve or near-zero
marginal cost.

**`expansion_potential`**: does one win open more?
1 = one-and-done · 3 = normal expansion · 5 = land-and-expand with a referenceable network effect.

### Risk

**`regulatory_risk`** (**inverted**): 1 = a regime we cannot currently meet · 3 = manageable with
work · 5 = no meaningful barrier.

**`concentration_risk`** (**inverted**): 1 = a handful of buyers or one gatekeeper controls entry ·
5 = many independent buyers.

**`switching_risk`** (**inverted**): 1 = deep incumbent lock-in with long contracts · 5 = low
switching friction.

Inverted criteria are scored so **5 is always good**. Never mix directions inside one model; that
is the most common arithmetic error in this genre.

## Knockouts

Separate from scoring. A knockout is a binary condition that removes a market from consideration
regardless of score:

- No legal right to operate, or a compliance regime the product cannot meet.
- A channel locked by an exclusive competitor arrangement.
- A hard product dependency that does not exist and is not on the roadmap.
- The strategy explicitly excludes it (a stated no from leadership, recorded).

Knockouts are recorded with evidence, exactly like scores, because a knockout is the strongest
claim in the model. A market removed by knockout still appears in the output, marked, so the
decision is visible rather than silent.

## Choosing weights well

- **Start from the constraint.** If capacity is one market next quarter, `buying_readiness` and
  `product_readiness` deserve more weight than `market_size`: you need a win now, not a big
  someday.
- **Weight what differentiates.** If every market on the slate is large, `market_size` carries no
  information; spend the weight on criteria where the markets actually differ.
- **Beware the double count.** `icp_match` and `product_readiness` often overlap; if two criteria
  move together in every row, merge them or reduce their combined weight.
- **Defend or drop.** One sentence per weight. If the sentence is "it seemed important," the
  criterion is decoration.

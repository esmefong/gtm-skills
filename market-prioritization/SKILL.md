---
name: market-prioritization
description: >
  Rank candidate markets, segments, verticals, or geographies against weighted criteria and report
  how robust the ranking is. Builds a criteria model from strategy (opportunity, fit, access,
  economics, risk), scores each market with evidence per cell, runs sensitivity analysis to show
  which rankings survive a reasonable argument about the weights, and names the deprioritized
  markets with reasons. Use whenever the user says "market prioritization", "which market should we
  enter", "segment prioritization", "vertical strategy", "expansion strategy", "TAM by segment",
  "where should we focus", "scoring model", or has more opportunities than resources. Consumes
  icp-research where available and feeds account-sourcing, which sources accounts inside the
  markets this skill picks.
---

# Market Prioritization

Turn "we could go after all of these" into a defensible short list: markets ranked against weighted
criteria, every score evidenced, and an honest statement of which rankings are robust and which are
coin flips. Its core claim: **the weights are the strategy, and a
ranking that flips under a small, reasonable change in weights is not a decision, it is a
preference.**

Most prioritization theater argues about scores. The real argument is about what matters and how
much, so this skill makes the weights explicit, forces them to be defended, and then tests whether
the answer depends on them.

## What this ranks (and what it doesn't)

- **It ranks markets:** segments, verticals, geographies, use cases, customer sizes, any set of
  addressable opportunities competing for the same finite go-to-market capacity.
- **It does not rank accounts.** Accounts inside a chosen market are `account-sourcing`'s job. Run
  this first to decide where to hunt, then that to decide whom.
- **It is not a forecast.** Scores are relative judgments with evidence, not predictions. The
  output is a prioritization and its confidence, never a revenue projection dressed as arithmetic.

## Inputs (ask for what is missing)

| Input | Why it matters | If missing |
|---|---|---|
| Candidate markets (5-20) | The set being ranked | Help enumerate: current customers' segments, adjacent verticals, geographies, use cases |
| Strategic constraint | What capacity is being allocated (headcount, quarters, budget) | Ask; a prioritization with no constraint is a wish list |
| Criteria and weights | The strategy, made explicit | Start from `references/criteria-library.md` and force a defense of each weight |
| ICP | Fit scoring is grounded in it | Use `icp-research` output where it exists |
| Evidence sources | Market sizing, competitive presence, regulatory facts | Public sources; same evidence standard as the rest of the repo |

The most useful ask: **"If you could only enter one of these next quarter, which would you pick,
and what would have to be true for you to be wrong?"** The instinct names the front-runner; the
second half names the criteria that actually matter.

## The workflow

Six phases. Show the user the weights (end of Phase 2) before scoring anything: once scores exist,
people rationalize weights to protect them.

### Phase 1: Define the slate and the constraint

List the candidate markets at a consistent altitude (do not mix "healthcare" with "Ontario dental
clinics"). Name the constraint: how many can actually be resourced, over what period. A slate of 12
with capacity for 2 is a different exercise than capacity for 6.

### Phase 2: Build the criteria model and defend the weights

Pick 4-7 criteria from `references/criteria-library.md` across the five families: **opportunity**
(size, growth), **fit** (ICP match, product readiness), **access** (channels, partnerships,
proof), **economics** (deal size, cycle, cost to serve), **risk** (competition, regulation,
concentration). Then set weights summing to 100 and **write one sentence defending each**. A weight
nobody can defend is a weight nobody believes.

Also set **knockouts**: conditions that disqualify a market regardless of score (no legal right to
operate, a channel locked by an exclusive competitor deal, a compliance regime the product cannot
meet). Knockouts prevent a market from scoring well on paper while being unenterable in fact.

### Phase 3: Score with evidence

Score each market on each criterion, 1-5, with a source and date per cell. Anchor the scale before
scoring (`references/criteria-library.md` has anchors per criterion) so a 4 means the same thing in
every row. Unknown stays unknown: an unscored cell is a research task, not a 3.

### Phase 4: Compute, then stress the ranking

Run `scripts/prioritize.py`: it applies weights, enforces knockouts, ranks, and then runs
**sensitivity analysis**, perturbing each weight and reporting which pairs of markets swap order.
The output distinguishes:

- **Robust leaders:** hold the top under every tested weighting. Decide on these.
- **Contested:** rank flips under plausible weight changes. Do not spend a quarter arguing; name
  the one criterion whose weight decides it and go settle that question with evidence.
- **Robust laggards:** never rise. Deprioritize honestly and say why.

### Phase 5: Write the decision, including the no

Produce the ranked table with evidence, the sensitivity read, and the **deprioritized list with
reasons**, which is the section leadership actually needs: a prioritization that only says yes has
not prioritized anything. For each deprioritized market, name what would bring it back.

### Phase 6: Set the revisit trigger

Prioritization decays as the market moves. Name the events that force a re-run (a competitor locks
a channel, a regulation lands, a partnership opens a geography) and a calendar cadence, typically
quarterly. Record the decision so the next re-run can see what changed and why.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/prioritize.py` | Weighted scoring, knockouts, ranking, and sensitivity analysis (which rankings survive weight perturbation) | None | None |

Judgment (which criteria, what weights, what each score means) is reasoning work; the arithmetic
and the robustness test are deterministic, so nobody has to trust a spreadsheet nobody audited.

## Composes with other skills

- **icp-research** (upstream, optional): the ICP grounds the fit criteria and supplies disqualifiers
  that often become knockouts.
- **account-sourcing** (downstream): sources accounts inside the markets this skill selects. The
  handoff is direct: prioritized markets become the sourcing universe's boundary.
- **positioning-message-house**: a market chosen here is the audience the bet is made for.

## Failure modes to avoid (the quality bar)

- **Weights set after scores.** The order matters: weights first, defended, then scoring.
- **Undefended weights.** If nobody can say why access is 25 and not 15, the model is decoration.
- **Precision theater.** Scores are 1-5 with anchors, not 87.3. A weighted model's job is to
  structure an argument, not to manufacture false accuracy.
- **No sensitivity check.** Reporting a winner without testing whether it survives a reasonable
  reweighting is the most common failure in this genre.
- **Mixed altitudes.** Comparing a continent to a city block produces nonsense rankings.
- **No knockouts.** A market that cannot be legally or practically entered should never appear at
  the top on the strength of size alone.
- **All yes, no no.** The deprioritized list with reasons is required output.
- **A forecast in disguise.** Never convert scores into revenue numbers; the model does not know
  that and saying so protects everyone.

## Bundled references

- `references/criteria-library.md`: the five criteria families, the standard criteria within each,
  scoring anchors, and how to choose and weight them. Read at Phases 2-3.
- `references/output-template.md`: the `markets.json` schema the script consumes and the decision
  document format. Read at Phases 3-5.
- `examples/cohere/`: eight markets ranked for Cohere from the repo's own ICP and sourcing run,
  with a knockout applied, robust leaders separated from contested pairs, and the deprioritized
  list.

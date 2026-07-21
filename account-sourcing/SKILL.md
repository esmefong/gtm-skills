---
name: account-sourcing
description: >
  Turn an ICP into a ranked target-account list with receipts. Takes the account-level ICP (ideally
  produced by icp-research), translates its criteria into queries against public sources (job
  postings, press, funding databases, registries, tech lookups), builds the account universe, scores
  and visibly disqualifies against the ICP rubric, and tags each surviving account with a dated
  why-now signal. Every account carries public evidence; no account is invented. Use whenever the
  user says "build a target account list", "account sourcing", "TAM list", "list building", "find
  companies to sell to", "who should we go after", "turn our ICP into a list", "prospect list",
  "account universe", or "lead sourcing". Ships with three key-free scripts: a deterministic account
  scorer, a live hiring-signal detector for public ATS job boards, and an executive briefing
  renderer. For products bought by organizations; consumes icp-research output and feeds
  outbound-engine.
---

# Account Sourcing

Turn an ICP from a strategy document into pipeline: a ranked list of real accounts worth pursuing,
each with public evidence for why, and a visible reject pile. This skill is opinionated about one
thing: **an account belongs on the list only if you can point to the evidence, and a list that shows
no rejects is hiding its judgment.**

The first deliverable companies expect from go-to-market engineering is exactly this: the target
account list, mapped to ICP criteria, scored, and refreshed. Outreach comes later and depends on it.

## What this builds (and what it doesn't)

- **It builds** the account layer: a ranked, evidenced account list (`account-list.md`), a
  machine-readable handoff (`accounts.json`) shaped for Clay, a CRM, or a sequencer, and the scoring
  rubric used (`rubric.yaml`).
- **It does not draft outreach.** Signal-to-message work belongs to `outbound-engine`, which consumes
  this skill's output. It also does not harvest individuals: sourcing stays at the account level,
  with a suggested entry role per account taken from the ICP's buying committee. People come later,
  at outreach time, at role level.

## Fit and limits

Built for products **bought by organizations** (a team or committee buys). For individual-buyer
products, "accounts" is the wrong unit: sourcing there means finding channels and communities, which
the ICP's journey section already maps. Say so and stop rather than forcing an account frame.

## Inputs (ask for what is missing)

| Input | Why it matters | If missing |
|---|---|---|
| Account-level ICP | The criteria, disqualifiers, and committee come from here | Run `icp-research` first, or gather a minimal version: what they sell, who buys, 2-3 disqualifiers |
| Target list size | Sets depth vs. breadth; default 25-50 evidenced accounts over thousands of thin rows | Default to 25-50 |
| Geography / segment constraints | Bounds the universe | Ask |
| Suppression list | Existing customers, partners, open opportunities must be excluded | Ask; note as a gap if none provided |
| Seed lists (optional) | Competitor customers, event exhibitors, association rosters accelerate Phase 3 | Proceed without |

The single most useful ask: **"Name your 5 best current customers, and name who should never be on
this list."** The first seeds lookalikes; the second sharpens disqualifiers and suppression.

## The workflow

Six phases. Show the user the query spec and source plan (end of Phase 2) and the scored draft with
its disqualifications (end of Phase 4) before packaging.

### Phase 1: Compile the query spec

Read the ICP and extract, verbatim, the account-level criteria: firmographics, technographics,
behavioral signals, and disqualifiers. Convert each into a machine-actionable statement with a
target value ("employee count 1,000+", "regulated sector: finance, government, health, telecom",
"hiring for AI platform roles"). Criteria that no public source can observe get downgraded to
**verify-later**, never guessed.

### Phase 2: Map criteria to sources

For each criterion, pick the public source that can actually answer it, using
`references/source-map.md`. The output of this phase is a source plan: criterion, source, query, and
the evidence tier the source provides. Job postings answer the most (stack, initiative, timing) and
are the default first stop. Show the query spec and source plan to the user before sourcing.

### Phase 3: Build the universe

Assemble candidate accounts from seed strategies: lookalikes of best customers, competitor customer
pages, category and association lists, event exhibitor and speaker lists, registry and filing
sweeps, and job-board sweeps for the ICP's signature roles. Dedupe by domain. Apply the suppression
list. Cap the universe at roughly 3-4x the target list size so scoring stays evidence-grade.

### Phase 4: Enrich, score, disqualify

For each candidate, fill the rubric fields with **evidence: value, source, and date per field**.
Unknown stays unknown. Then score:

- Judgment lives with you: whether an account meets a criterion, and on what evidence.
- Arithmetic lives with the script: `scripts/score_accounts.py` reads `accounts.json` plus
  `rubric.yaml`, applies weights, hard disqualifiers, and tier thresholds deterministically, and
  emits the ranked list. Same inputs, same output, auditable.

Disqualifications are output, not noise: every rejected account keeps its reason. A list with no
rejects has not been judged. Show the scored draft to the user.

### Phase 5: Signal-tag the survivors

For the qualified tier, attach dated why-now signals: hiring (live postings for ICP-relevant roles),
funding or financial events, leadership changes, announced initiatives, regulatory shifts.
`scripts/hiring_signal.py` checks public ATS job boards (Greenhouse, Lever, Ashby JSON endpoints, no
keys) for ICP-relevant postings live. A signal without a date and source does not count.

### Phase 6: Package, route, and set the cadence

Assemble the deliverable per `references/output-template.md`: the ranked table with receipts, the
disqualified table with reasons, gaps and verify-laters, and `accounts.json` for handoff. Then
route: author `owner_team` and `next_action` per account, because a list without owners and actions
is notes, not work product, and render the executive briefing
(`scripts/render_briefing.py`, brand-flavored accent only, disclaimer always on). Set the refresh
cadence: signals decay in weeks, firmographics in quarters. A list without a refresh rhythm is a
snapshot, not a system.

## The receipts rule

Every scored field cites its source and date. Evidence tiers (defined in the source map): primary
sources outrank press, press outranks directories. Load-bearing decisions need primary or reputable
secondary evidence. **No account is ever invented, and no fact is ever assumed.** An honest
"verify" beats a confident guess.

## Scripts

| Script | What it does | Network | Keys |
|---|---|---|---|
| `scripts/score_accounts.py` | Deterministic scoring: accounts + rubric in, ranked tiers and disqualifications out | None | None |
| `scripts/hiring_signal.py` | Live check of public ATS JSON boards for ICP-relevant postings per company | Public endpoints only | None |
| `scripts/render_briefing.py` | Executive briefing from accounts.json: lanes by owning team, next action per card, rejects with reasons, self-contained HTML | None | None |

The split is deliberate: judgment and evidence-gathering are reasoning work; scoring math and live
checks are deterministic work that should be repeatable and auditable.

## Composes with other skills

- **icp-research** (upstream): its account-level ICP section is this skill's query spec, and its
  buying committee supplies the entry role per account.
- **outbound-engine** (downstream, planned): consumes the qualified accounts and their signals to
  draft committee-aware, voice-matched outreach.
- **market-prioritization** (sibling, planned): ranks markets and segments; this skill ranks accounts
  within them.

## Failure modes to avoid (the quality bar)

- **Invented accounts.** The cardinal sin. Every account exists; every fact cites.
- **Unanswerable criteria.** A criterion no public source can observe produces guesses; downgrade it
  to verify-later in Phase 1.
- **No rejects.** A list with no disqualifications has not been judged; it has been collected.
- **Undated evidence.** A signal without a date is trivia; last year's funding round is not a
  why-now.
- **Volume worship.** 500 thin rows lose to 30 evidenced ones; the cap exists for a reason.
- **Suppression neglect.** Sourcing your own customers embarrasses everyone downstream.
- **One-and-done.** No refresh cadence means the list is already decaying.

## Bundled references

- `references/source-map.md`: which public source answers which ICP criterion, evidence tiers, query
  patterns, tool mapping, and access ethics. Read at Phase 2.
- `references/output-template.md`: the exact deliverable structure, the `accounts.json` schema, and
  the `rubric.yaml` format the scorer consumes. Read at Phase 4 and 6.
- `examples/cohere/`: a worked example sourcing real accounts for Cohere from public evidence,
  scored against the Cohere ICP from `icp-research`, rejects included.

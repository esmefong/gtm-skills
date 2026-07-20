---
name: icp-research
description: >
  Turn raw research signals into an operational Ideal Customer Profile, in any industry.
  Ingests interview transcripts, survey exports, community/Slack threads, review sites,
  sales-call notes, and funnel data, then produces an ICP document built on situation triggers
  and a how-to-win plan. Use whenever the user says "ICP research", "ideal customer profile",
  "build a buyer persona", "profile our target buyer", "who should we sell to", "audience
  research", "customer segmentation", "voice of customer", or asks to turn interviews /
  community threads / reviews into personas. Works for consumer/lifestyle, B2B SaaS, fintech,
  and enterprise alike: the situation-first core is industry-neutral, and it adds a
  buying-committee map and account-level scoring rubric only when the buyer is a team. Built on
  the 5 Rings of Buyer Insight (Revella), Jobs-to-be-Done and the Four Forces (Moesta /
  Christensen), and demand-side selling.
---

# ICP Research

Turn raw customer signal into an ICP a copywriter, a media buyer, and a sales rep can all act
on the same day. This skill is opinionated about one thing: **you sell into a situation, not to
a demographic.** Everything below is built to find, name, and operationalize the situations that
make someone unable to ignore the product.

The output is not a persona poster. It is an operating document: the situations that create
demand, and a plan for what to do with them. The core is the same whether the buyer is one
person or a company. When the buyer is a team, the skill adds two modules on top: the buying
committee that has to say yes, and an account-level rule a rep can score in 30 seconds. When the
buyer is an individual (consumer, prosumer, lifestyle), those modules are skipped and the
emotional core carries more weight. Neither is the "default"; the skill reads the situation and
adapts.

## When this runs well vs. badly

Run it when the user has *raw material* (or can get it): interviews, survey responses, community
threads, review-site text, sales-call notes, funnel data. The skill's whole value is turning
real customer language into structure. The skill can also **gather public voice-of-customer signal
itself** (Reddit, G2/Capterra, forums) when the company or its competitors are publicly discussed —
this is an opt-in step, offered and confirmed in Phase 1, and it is how the `examples/` ICP was
built. If there is no raw material at all, say so plainly and either (a) run in "hypothesis mode"
clearly labelling every claim as assumed and naming the validation step, or (b) gather public
signal and/or help the user collect first-party signal (see `references/research-sources.md`).

Never invent quotes or pass off assumption as evidence. A weaker ICP that is honest about its gaps
beats a confident one built on nothing. Every ICP this skill produces ends with a **Gaps** section.

## Inputs (ask for what is missing)

Collect these before starting. If some are missing, proceed with what exists and record the
absence in Gaps rather than stalling.

| Input | Why it matters | If missing |
|---|---|---|
| Company / product one-liner | Anchors what "fit" means | Ask; do not proceed without it |
| Industry + motion | Sets committee depth (see Industry adaptation) | Infer from the product, confirm with user |
| Business model | B2B vs. B2C changes the whole output shape | Ask |
| Raw research signal (first-party) | The evidence base | Run hypothesis mode, or gather first |
| Existing customers / won deals | Who already fits | Note as a gap |
| Competitors / alternatives | Decision criteria are comparative; also seeds the public sweep | Ask for the top 2-3 |
| Public data sweep (opt-in) | Bootstraps or supplements when public discussion exists | Offer it in Phase 1; only run if the user confirms |

The single most useful thing to ask for: **"Who recently switched to you, or seriously
considered you and didn't?"** Those two groups produce the richest signal.

## The workflow

Five phases. Do them in order. Show the user your work at the end of Phase 2 (the tagged signal)
and Phase 3 (the draft segments) before writing the final document, so they can correct course.

### Phase 1 — Scope and intake

1. Confirm the company one-liner, industry, motion, and — the pivotal question — **who actually
   buys: one person, or a team?** This decides whether the committee and account-ICP modules apply.
2. Branch on **Industry adaptation** (below) to decide how deep those modules go, if at all.
3. Inventory the first-party signal on hand and label each source by type and recency. Interviews and
   community threads are your richest sources; funnel data is the honesty check on what people
   *say* vs. *do*.
4. **Offer the public-data sweep, and get explicit confirmation before running it** (see below).
5. State the confidence level up front: is this an evidence-grounded ICP or a hypothesis to test?

#### The public-data sweep (opt-in)

Beyond the user's own inputs, the skill can gather **publicly available voice-of-customer signal** —
Reddit, G2/Capterra and other review sites, community forums, comparison articles — for the product
and its competitors, the way the `examples/` ICP was built from Notion's public discussion. It is
especially useful when first-party data is thin, when you need category language, or to cover
competitors that the user's own interviews won't.

**Always confirm before searching.** Tell the user what you'd look for and ask permission, because
some products are confidential, and public search has a time/token cost the user should opt into. A
good prompt: *"Want me to also pull public discussion about [product] and [competitors] from Reddit,
G2, and forums to enrich this? I'll anonymize handles and cite sources."* Confirm scope: which
product(s) and competitors, and which sources.

**When you do run it:**
- **Anonymize and cite.** Remove handles, mark quotes as representative/lightly edited, list sources.
  Public sources only. (Full ethics in `references/research-sources.md`.)
- **Label it as secondary.** Public data skews toward vocal enthusiasts and churners and is often
  about competitors, so weight it *below* first-party research and tag it as directional in the Gaps.
- **Handle a thin footprint gracefully.** If the product isn't publicly discussed (stealth, niche,
  brand new), say so and fall back to first-party inputs or hypothesis mode rather than forcing it.
- Fold the findings into the Phase 2 tagged quote bank alongside first-party signal, clearly marked
  by source.

### Phase 2 — Signal extraction (tag against the 5 Rings + Four Forces)

Read every source and pull **verbatim** language, tagged to a ring. Preserve the customer's exact
words and trace each to its source and date. This is the step that makes the output feel real
instead of templated. Full definitions are in `references/frameworks.md`; the five rings:

- **Priority Initiative** — the trigger. What made them reject the status quo and spend time,
  budget, or political capital *now*?
- **Success Factors** — what winning looks like *to them* (often more emotional than product teams expect).
- **Perceived Barriers** — what almost stopped them; why they doubt any solution, or prefer a rival's.
- **Decision Criteria** — the attributes they actually weigh when comparing options (not the ones you wish they used).
- **Buyer's Journey** — where they looked, who they trusted, what sequence of touchpoints moved them.

For each persona, also map the **Four Forces** of the switch: Push (of the current situation),
Pull (of the new solution), Anxiety (of switching), Habit (of the present). A switch happens only
when Push + Pull > Anxiety + Habit. Naming the anxiety and habit is usually where the real
marketing work is.

Output of this phase: a tagged quote bank, grouped by ring, with sources. Show it to the user.

### Phase 3 — Synthesis (cluster into situations and segments)

1. Cluster the tagged signal into **recurring situations**, not demographic buckets. Order clusters
   by frequency (most common trigger first).
2. Define **1-4 ICPs / segments** from those clusters. More than 4-5 and the ICP stops being
   operable. Each ICP is a situation, not a job title.
3. **If the buyer is a team**, separate the **account level** (which companies) from the **role
   level** (which people inside them), and draft both. **If the buyer is an individual**, there is
   one buyer; skip the account/role split and lean into the emotional core and the situation.
4. Draft each segment against the output template. Show the draft segment list to the user before
   finalizing.

### Phase 4 — Operationalize

This is what separates an ICP veterans respect from a persona nobody uses. Always produce **How to
Win** and **Insight-to-action routing**. Add the **account-level ICP** and **buying-committee map**
only when the buyer is a team.

1. **How to Win** (always) — the USP ("why you, why now"), the narrative that mirrors the buyer's
   journey, the 1-2 dimensions of real differentiation, and the channels the journey actually runs
   through.
2. **Insight-to-action routing** (always) — map each finding to where it gets used (triggers → hero
   copy and targeting; barriers → FAQ and objection handling; criteria → comparison pages; journey →
   channel strategy). If a finding doesn't route to an action, it is trivia, cut it.
3. **Account-level ICP + scoring rubric** *(team buyers only)* — firmographics, technographics,
   behavioral signals, and **explicit disqualifiers** ("if they use X, deprioritize"; "if under $Y
   ARR, not fit"). The test: a rep can answer "does this account qualify?" in 30 seconds.
4. **Buying-committee map** *(team buyers only)* — the roles that have to say yes, who champions, who
   can veto, who influences whom, and the objection pattern for each. (For an individual buyer, the
   nearest analog is any gatekeeper or approver — a partner, a parent, a manager with the budget —
   captured as a lightweight recipient/approver persona, not a full committee.)

### Phase 5 — Validation plan

1. Turn each ICP into a **hypothesis with a metric and a threshold** ("if leads from situation X
   convert at 2x baseline, this ICP is validated").
2. Name the **next validation step** for every gap (a cohort of interviews, an ad test, a keyword
   check, a win/loss review).
3. Set a **refresh cadence** (quarterly deep-dive, monthly pulse, always-on community + funnel
   intake). ICP work is a loop, not a deliverable. See `references/research-sources.md`.

## Output

Assemble the final document using `references/output-template.md`. Its core is industry-neutral
(Who / Trigger / Before / Success / Barriers / How to speak to them / Where to find them / Who we
are NOT for / Gaps); the account-ICP and buying-committee sections are modules you include only for
team buyers. Lead every profile with the situation. Keep customer quotes verbatim and attributed.
End with Gaps, honest about validated vs. hypothesized, and the next validation step.

## Industry adaptation

The situation-first spine is constant across every industry. What flexes is whether the buyer is one
person or a group, and how much weight the emotional core carries. No industry is the "default."

- **Consumer / lifestyle (B2C)** — an individual buyer, deciding largely on emotion and situation.
  No committee; at most a gatekeeper or approver (a partner, a parent). Weight the emotional core
  and the trigger heavily; demographics are a secondary lens. Behavioral signals live on social
  platforms and communities, not in a CRM.
- **Prosumer / individual within a company** — still one buyer buying for themselves, but the "job"
  is professional. Same individual shape as B2C, with success factors framed around work outcomes.
- **B2B SaaS** — a team buys. Full buying committee (Economic Buyer, Champion, Technical Buyer, End
  User, Blocker) plus an account-level ICP. Technographics matter (current stack signals fit and
  integration cost). Note: PLG products often start as an *individual* adoption and only later
  become a team purchase — profile both motions.
- **Fintech / regulated** — everything in B2B SaaS, plus **Compliance / Risk as a structural veto
  holder**. Expect longer cycles, more stakeholders, and a regulatory review gate. Lead messaging
  with risk mitigation and regulatory fit.
- **Enterprise** — larger committee, procurement and security review as formal gates, multi-year
  cycles. Multi-thread; document who influences whom.

Many products span more than one of these (a tool sold to individuals *and* teams). When they do,
profile each motion as its own segment; the worked example in `examples/` does exactly this. If
unsure which applies, infer from the product and confirm with the user in Phase 1.

## Failure modes to avoid (the quality bar)

Veteran marketers judge ICP work by whether it avoids these. Check the final document against the list.

- **Demographic theater** — age, title, a stock photo, a coffee order. Situations drive decisions; demographics describe the pond.
- **Assumption dressed as evidence** — personas built from internal opinion and job descriptions, not customer language. If it isn't traceable to a source, label it a hypothesis.
- **Product-centric framing** — describing how the customer fits into your world instead of how you fit into theirs.
- **No disqualifiers** — an ICP with no "not for" is not operable; every edge-case account becomes a debate.
- **One hero persona in a team sale** — resonates with the champion, gets killed by IT or compliance. When the buyer is a group, map the whole committee.
- **Personas nobody uses** — a beautiful doc that never touches copy, targeting, or a sales call. Operationalize (Phase 4) or don't bother.
- **Frozen in time** — no refresh cadence. Titles, stacks, and triggers shift; the ICP has to keep up.

## Bundled references

- `references/frameworks.md` — the 5 Rings, JTBD and the Four Forces, demand-side selling, and the
  buying-committee model, with the interview method. Read when you need the full definition of a ring
  or force.
- `references/output-template.md` — the exact document structure to fill. Read before assembling the
  final ICP.
- `references/research-sources.md` — how to gather each input type, including the community/Slack
  monitoring method, plus research ethics and sanitization. Read when the user needs to collect signal
  or is working from community data.
- `examples/` — worked examples built from real, public voice-of-customer data, one folder per company
  (each with `input.md` + the produced `icp.md`). **`examples/cohere/`** is the primary example: an
  enterprise buyer with a full buying committee where security and compliance are a structural veto.
  **`examples/notion/`** is a second example showing the engine generalize across buyer shapes (an
  individual buyer and a team buyer in one document). The output is named `icp.md` so it drops straight
  into a `brand-voice-guide` directory as its audience context.

# Source map

Which public source answers which ICP criterion. This is the skill's engine room: Phase 2 turns the
query spec into a source plan using this map, and Phase 4's evidence standard comes from it. The map
is tool-agnostic; the commercial tools that automate parts of it are listed at the bottom.

## The evidence standard

Every fact recorded about an account carries three things: **value, source, date.** Sources rank in
three tiers:

| Tier | What it is | Examples |
|---|---|---|
| **A: primary** | The account speaking for itself | Their job postings, newsroom/press releases, filings, docs, engineering blog, own site |
| **B: reputable secondary** | Verified third-party reporting | Established press, funding databases, earnings transcripts, government registries |
| **C: directional** | Aggregated or inferred | Directories, "top X" listicles, review-site inference, tech-lookup tools |

Load-bearing decisions (qualify, disqualify, signal-tag) need Tier A or B. Tier C can nominate a
candidate or suggest a verify-later, never confirm one. Unknown stays unknown.

## Criterion classes and their sources

### 1. Firmographics (industry, size, geography, stage)

| Source | What it answers | Notes |
|---|---|---|
| Company site + about page | What they do, where they operate | Tier A; the baseline check |
| LinkedIn company page | Headcount band, locations | Tier B; bands are approximate |
| Funding databases (Crunchbase-class) and funding press | Stage, raise dates, investors | Tier B; date every round |
| Public filings (SEC/SEDAR), annual reports, earnings transcripts | Size, segments, stated initiatives for public companies | Tier A; earnings calls name initiatives verbatim |
| Industry association member lists, government vendor registries | Sector membership, regulated status | Tier B |
| Conference exhibitor and sponsor lists | Category presence, budget existence | Tier B; also a seed source |

### 2. Technographics (stack, infrastructure, integrations)

| Source | What it answers | Notes |
|---|---|---|
| **Job postings** | Stack named in requirements, team structure, initiatives | Tier A and the single richest source; see class 3 |
| Tech-lookup tools (BuiltWith/Wappalyzer-class) | Web-facing stack | Tier C; front-end only, verify before load-bearing use |
| Engineering blogs and talks | Infrastructure choices, build-vs-buy posture | Tier A |
| Vendor case studies and customer-logo pages | Who uses what today | Tier A for the vendor relationship; also feeds suppression and competitor-displacement lists |
| Integration marketplaces and partner directories | Ecosystem membership | Tier B |

### 3. Hiring signals (the highest-value class)

Job postings reveal three things at once: **initiative** (a Head of AI posting means an AI mandate),
**stack** (tools named in requirements), and **timing** (posted date). They are also the most
queryable source, because major ATS platforms expose public JSON:

| ATS | Public endpoint pattern | Notes |
|---|---|---|
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs` | JSON, no auth; add `?content=true` for descriptions |
| Lever | `https://api.lever.co/v0/postings/{company}?mode=json` | JSON, no auth |
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/{board_name}` | JSON, no auth; some companies disable it |

`scripts/hiring_signal.py` automates this class: given companies and their ATS slugs plus ICP-relevant
role keywords, it returns live matching postings with dates. LinkedIn and aggregator boards cover
companies without a public ATS board, at Tier B and with more manual effort.

### 4. Funding and financial events

Funding announcements (database + press), earnings transcripts, and investor pages. A raise is a
budget signal and a growth-pressure signal; date it, and treat rounds older than two quarters as
context rather than why-now.

### 5. Initiatives, press, and regulatory signals

Newsroom and PR feeds, executive interviews, conference speaker lists (speaking about X means
investing in X), government RFP portals (a posted RFP is the loudest possible in-market signal in
public sector), and regulatory changes that create the ICP's situation (a new data-residency rule
manufactures demand for anyone selling sovereignty).

### 6. Leadership changes

New-hire press releases and exec announcements. A new leader in the function you sell into is a
tooling-decision window; date it, and pair it with what the leader has said publicly about their
mandate.

### 7. Competitor and review-site inference

Reviews of competitor products (G2/Capterra-class) surface accounts feeling a pain right now, and
reviewer firmographics narrow who they are. Tier C on identity (reviews are often anonymized to
segment level): use them to nominate candidate segments, then confirm the account by another source.

### 8. Suppression sources

The client's own customer-logo page, case-study index, and partner list, plus their CRM export when
available. Run these against the universe before scoring; sourcing an existing customer is the
cheapest failure to prevent.

## Worked illustration (Cohere ICP criteria)

| ICP criterion | Source | Query shape | Tier |
|---|---|---|---|
| "Hiring a Head of AI / GenAI lead" | ATS JSON boards, LinkedIn jobs | Role-keyword sweep across regulated-sector companies | A |
| "Announced GenAI mandate" | Newsroom, press, earnings transcripts | "[company] generative AI initiative" within last 2 quarters | A/B |
| "Regulated sector" | Industry classification, registries | Sector membership lists: banking, gov, health, telecom | B |
| "Data-residency requirement" | Regulatory press, RFP portals, jurisdiction | Sovereignty rules by country + posted RFPs naming residency | B |
| Disqualifier: "comfortable on public APIs" | Engineering blog, job postings | Stack mentions of public LLM APIs in production | A |

## Industry adaptation: the criterion picks the source

The map is industry-agnostic across organization buyers, but the source mix shifts with the
segment's public footprint. Tech and mid-market+ companies are richest in classes 2-4 (ATS boards,
funding databases, engineering blogs). Regulated enterprise leans on class 1 and 5 (filings,
registries, earnings calls, RFP portals). Local and traditional SMBs rarely run a public ATS: for
them, swap toward business registries and licensing databases, maps and places listings, franchise
directories, chamber and association rosters, and review platforms. Phase 2 always starts from the
criterion and asks which source can answer it, never the reverse.

## Where commercial tools slot in

The map runs manually or with an agent at small scale. At production scale, each class maps to a
tool: **Clay** (waterfall enrichment automates classes 1-2 and orchestrates the rest),
**Crunchbase/PitchBook** (class 4), **BuiltWith** (class 2, Tier C), **Apollo/ZoomInfo** (contact
layer, used downstream at outreach time, not here), and the **CRM or warehouse** (class 8,
suppression). The skill's output schema is shaped so any of these can consume it.

## Access ethics

Public pages and public APIs only. Respect terms of service and robots directives; nothing behind
authentication walls. Source at the account level: no harvesting of individuals' personal data at
this stage (entry roles are named as titles, and people enter the picture only at outreach, at role
level). Keep privacy law in view for downstream use: consent-based regimes like CASL are stricter
than opt-out regimes, and the sourcing record (evidence, dates) is what makes downstream compliance
defensible.

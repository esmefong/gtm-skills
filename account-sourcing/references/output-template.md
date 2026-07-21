# Output template

The deliverable is three canonical files plus a rendered briefing. `account-list.md` is the working
doc; `accounts.json` is the machine handoff (Clay, CRM, sequencer, or `outbound-engine`);
`rubric.yaml` is the scoring config, kept with the output so every ranking is reproducible; and
`briefing.html` is the executive layer, generated from the data by `scripts/render_briefing.py`
(lanes by owning team, next action per account, rejects with reasons, disclaimer always rendered).

```
sourcing-output/
├── account-list.md     # working doc: the ranked list with receipts, rejects included
├── accounts.json       # machine-readable handoff, one record per account
├── rubric.yaml         # the weights, disqualifiers, and thresholds used
└── briefing.html       # generated executive briefing; edit the data, not the page
```

## `account-list.md` (copy the headings)

```markdown
# Target accounts: [Company]

[One line: built from which ICP, on what date, at what target size.]

**Method:** [universe size sourced] candidates from [seed strategies], scored against `rubric.yaml`,
[n] qualified / [n] disqualified / [n] verify-later. Evidence tiers per `source-map.md`.

## Query spec used
[The criteria and disqualifiers extracted from the ICP, with target values. Verbatim where possible.]

## Ranked accounts

| # | Account | Score | Tier | Fit evidence (source, date) | Why-now signal (dated) | Entry role |
|---|---|---|---|---|---|---|
[Top accounts only, at the agreed target size. Every evidence cell cites source and date. Entry role
comes from the ICP's buying committee.]

## Disqualified

| Account | Reason (which disqualifier, what evidence) |
|---|---|
[Every rejected account keeps its reason. This table is a required section, not an appendix.]

## Verify later
[Candidates where a load-bearing fact could not be confirmed at Tier A/B. What to check, and where.]

## Gaps
[What the sourcing could not see: criteria with no observable source, segments under-covered,
suppression list missing. Honest accounting, same rule as every skill in this repo.]

## Refresh cadence
[Signals: re-check weekly or biweekly (hiring and press decay fast). Firmographics: quarterly.
Name the owner and the trigger for a full re-run.]
```

## `accounts.json` (schema, annotated)

One record per account, qualified and disqualified alike. Field names are load-bearing:
`scripts/score_accounts.py` writes `score`, `tier`, `status`, and `disqualifiers_hit`; everything
else is authored during enrichment.

```json
{
  "generated": "2026-07-21",
  "icp_source": "icp-research/examples/cohere/icp.md",
  "rubric": "rubric.yaml",
  "accounts": [
    {
      "name": "Example Bank",
      "domain": "examplebank.com",
      "status": "qualified",
      "score": 82,
      "tier": 1,
      "scores": { "firmographic": 34, "technographic": 18, "signal": 30 },
      "disqualifiers_hit": [],
      "evidence": [
        {
          "field": "industry_regulated",
          "value": "retail banking",
          "source": "https://example.com/registry-entry",
          "date": "2026-06-30",
          "evidence_tier": "B"
        }
      ],
      "signals": [
        {
          "type": "hiring",
          "detail": "Head of AI Platform posting, Toronto",
          "source": "https://boards-api.greenhouse.io/v1/boards/examplebank/jobs",
          "date": "2026-07-14"
        }
      ],
      "entry_persona": "Head of AI / ML platform lead",
      "owner_team": "Sales",
      "next_action": "Route to the enterprise AE; open on the platform-buyer signal.",
      "suppressed": false
    },
    {
      "name": "Example Startup",
      "domain": "examplestartup.io",
      "status": "disqualified",
      "score": 0,
      "tier": null,
      "scores": {},
      "disqualifiers_hit": ["public_api_comfortable"],
      "evidence": [
        {
          "field": "public_api_comfortable",
          "value": "production use of public LLM APIs described on engineering blog",
          "source": "https://examplestartup.io/blog/how-we-built-x",
          "date": "2026-05-02",
          "evidence_tier": "A"
        }
      ],
      "signals": [],
      "entry_persona": null,
      "suppressed": false
    }
  ]
}
```

Rules: `status` is one of `qualified | disqualified | verify`. Disqualified records keep their
evidence; that is what makes the reject table auditable. Suppressed accounts stay in the file with
`"suppressed": true` so the suppression itself is visible.

Routing fields, authored at Phase 6: `owner_team` names the lane that owns the account (Sales,
Partnerships, ABM and field, Nurture; for rejects, Do not pursue or Existing relationship), and
`next_action` is the specific step that owner takes, phrased so it can be executed without reading
the rest of the report. The briefing renderer groups by the first and leads each card with the
second; a list without owners and actions is notes, not work product.

## `rubric.yaml` (the scorer's config)

The judgment (does this account meet this criterion, on what evidence) is authored per account into
`evidence` and per-criterion points. The script only aggregates: sum weighted points, apply hard
disqualifiers, cut tiers, sort. Same inputs, same ranking, every run.

```yaml
# Weights sum to 100 across categories.
weights:
  firmographic: 40
  technographic: 25
  signal: 35

criteria:
  firmographic:
    - id: industry_regulated
      desc: "Regulated or sensitive-data sector (finance, gov, health, telecom)"
      points: 20
    - id: size_1000_plus
      desc: "1,000+ employees"
      points: 20
  technographic:
    - id: hybrid_infra
      desc: "On-prem or hybrid infrastructure in evidence"
      points: 25
  signal:
    - id: hiring_ai_lead
      desc: "Live posting for Head of AI / GenAI-lead role"
      points: 20
    - id: genai_mandate
      desc: "Publicly announced GenAI initiative, last 2 quarters"
      points: 15

disqualifiers:
  - id: public_api_comfortable
    desc: "Production use of public LLM APIs with no data constraint"
  - id: existing_customer
    desc: "On the suppression list"

tiers:
  tier1: 75
  tier2: 55
verify_below: 40
```

Category points are the maximum available in that category; an account earns a criterion's points
only when its `evidence` array contains a Tier A/B entry for that criterion's `id`. The example
values above are the Cohere rubric; swap the criteria for any other ICP and the machinery is
unchanged.

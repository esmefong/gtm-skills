# Target accounts: Cohere

Built from the Cohere ICP (`icp-research/examples/cohere/icp.md`) on 2026-07-21, at worked-example
scale (16 evidenced records; the skill's default is 25-50).

**Method:** universe seeded from lookalikes of Cohere's public customers (RBC to other Canadian
financial institutions, Bell and STC to sovereign-minded telecoms) plus sovereign-AI press sweeps
across regulated sectors, then a second sweep beyond the household names. 16 accounts evidenced and
scored against `rubric.yaml` by `scripts/score_accounts.py`: **11 qualified (1 tier 1, 8 tier 2,
2 tier 3), 5 disqualified.** Evidence tiers per `references/source-map.md`. Every claim below
carries a source and date in `accounts.json`.

**Who consumes this list:** per the ICP, Cohere's buyers move through analysts, partners, and
procurement rather than cold sequences. This list is built for that motion: ABM and field-marketing
planning, event and analyst targeting, and partner-coverage decisions. The motion column marks which
lane each account belongs to; none of it is an SDR blast list.

## Query spec used

From the ICP's account-level section: regulated or sensitive-data sector (finance, government,
health, telecom) 20 pts; 1,000+ employees 20 pts; on-prem, hybrid, or sovereign infrastructure in
evidence 25 pts; live Head-of-AI hiring 20 pts; announced GenAI mandate 15 pts. Disqualifiers:
comfortable on public APIs; committed to a competing model provider or exclusive in-house build;
existing Cohere customer or partner (suppression). Tiers at 75/55, verify below 40.

## Ranked accounts

| # | Account | Score | Tier | Motion | Fit evidence (source, date) | Why-now signal (dated) | Entry role |
|---|---|---|---|---|---|---|---|
| 1 | TELUS | 80 | 1 | Platform partner | Sovereign AI Factory Rimouski, own release, 2025-09 (A); telecom + scale (B) | Expansion: Kamloops + 2 Vancouver sites, 60,000+ GPUs by 2032 (2026-05-12) | VP AI infrastructure (Bell channel conflict noted) |
| 2 | CIBC | 55 | 2 | Customer | Big Five bank (B); CIBC AI platform enterprise-wide, own newsroom, 2025-05-27 (A) | In-house platform live: a platform buyer that needs private model supply | Head of AI / ML platform lead |
| 3 | TD Bank Group | 55 | 2 | Customer | Big Five bank (B); AI Prism June 2025, $1B AI value target (B) | 2026 framed as year of agentic AI | Head of AI (note: in-house strength via Layer 6) |
| 4 | Manulife | 55 | 2 | Customer | Insurer (B); GenAI to 100 percent of workforce, own newsroom (A); 43 use cases live | Enterprise AI platform buildout; $1B value target by 2027 | Head of AI / ML platform lead |
| 5 | Desjardins Group | 55 | 2 | Customer | North America's largest financial co-operative (B); AI assistant Alvie live for all members, multi-year Exagens AI contract (B) | Member-facing AI live at co-op scale, transformation program active | Head of AI / ML platform lead |
| 6 | BMO | 55 | 2 | Customer | Big Five bank (B); Institute for Applied AI and Quantum, Lumi Assistant (B, 2026-04) | Institute launch signals sustained investment | Head of AI / ML platform lead |
| 7 | Scotiabank | 55 | 2 | Customer | Big Five bank (B); AI routes 90 percent of commercial email (B, 2026-04) | Annual-meeting AI commitments | Head of AI / ML platform lead |
| 8 | Intact Financial | 55 | 2 | Customer | P&C insurer (B); approx. $200M AI returns for 2025 (B, 2026-02) | Proven AI ROI, scaling investment | Head of AI / ML platform lead |
| 9 | Swisscom | 55 | 2 | Platform partner | Telecom + scale (B); FastwebAI Suite sovereign GenAI launch, trade press (B); infra claim regraded, see self-audit | Group sovereign AI motion; DACH adjacency to the Aleph Alpha merger | VP AI infrastructure |
| 10 | Sun Life | 40 | 3 | Customer | Insurer + scale confirmed (B); no mandate evidence found this sweep | None yet | Head of AI / ML platform lead |
| 11 | Telefonica | 40 | 3 | Platform partner | Telecom + scale (B); infra and mandate claims regraded, see self-audit | Pending primary-source confirmation | VP AI infrastructure |

## Self-audit: the review regrade

The first pass scored Swisscom and Telefonica at 80 (tier 1) on sovereign-AI-factory evidence drawn
from an undated NVIDIA partner-marketing page. Review caught the inconsistency: the source map
classifies vendor partner listings as Tier C (nominate, never confirm), and Tier C cannot carry
load-bearing points. The three affected entries were regraded to C and the scorer rerun: Swisscom
dropped to 55 (its GenAI mandate held via trade press), Telefonica to 40 (verify both claims against
primary sources). TELUS kept tier 1 because its factory evidence is its own press release. The
regrade is the standard working as designed: the ranking moved rather than the standard bending.

## Disqualified

| Account | Reason (disqualifier, evidence) |
|---|---|
| SoftBank Corp | Committed elsewhere: SB OAI Japan, 50-50 JV with OpenAI selling Crystal intelligence exclusively in Japan (own press, 2025-11-05, A) |
| BNP Paribas | Committed elsewhere: group-wide multi-year Mistral agreement covering all models, extended 3 years, approx. 100 use cases live (own press, A) |
| RBC | Suppressed: publicly named Cohere customer |
| Bell Canada | Suppressed: Bell AI Fabric partnership runs Cohere North; $220M sovereign GPU deal (2026-06) |
| Government of Canada | Suppressed: federal partnership agreement on public-service AI (2025-08) plus up to $240M sovereign compute investment |

The suppression rows are the run's first save: two of the most obvious "targets" in Canadian
regulated AI are already Cohere relationships, and a list built without the suppression pass would
have led outreach straight into them.

## Verify later: the surprise ring

The household names above are table stakes; the accounts a sales team does not already know are the
real sourcing value. Candidates nominated by the ICP logic whose evidence did not clear Tier A/B in
this sweep, with the rationale to pursue each:

- **ATB Financial** (Alberta crown financial institution: regulated, provincially owned, AI-forward
  history). Next: newsroom and job-board sweep.
- **Interac** (Canadian payments rail: data cannot leave the country almost by definition). Next:
  confirm employee scale and any GenAI program; scale may fail the 1,000+ criterion honestly.
- **OTPP and CPPIB** (pension funds: enormous sensitive-data estates, sophisticated tech orgs).
  Next: earnings letters and tech-hiring sweeps.
- **Provincial governments** (Ontario, Quebec, BC: sovereignty requirements without the federal
  suppression). Next: RFP portal sweeps, the loudest public-sector signal available.
- **EU mid-tier banks and insurers** (post-Aleph-Alpha DACH footprint). Next: a dedicated
  European sweep; BNP's Mistral lock-in suggests moving before more of the market signs.
- **Rogers, Orange, Telenor** (telco pattern-matches). Next: primary-source infrastructure checks,
  applying the self-audit lesson above.

- **Hiring signals (all accounts):** no `hiring_ai_lead` criterion was granted anywhere, so every
  score above is un-boosted by hiring. The ATS JSON check was run honestly and came back empty for
  this segment (below). Next: LinkedIn Jobs sweeps per account, Tier B.

```
$ python3 scripts/hiring_signal.py --company greenhouse:telus:TELUS \
    --company greenhouse:bmo:BMO --company greenhouse:manulife:Manulife \
    --keywords "head of ai,ai platform,machine learning lead,genai"
TELUS: board unreachable or disabled (HTTP Error 404: Not Found)
BMO: board unreachable or disabled (HTTP Error 404: Not Found)
Manulife: board unreachable or disabled (HTTP Error 404: Not Found)
```

Large regulated enterprises sit on Workday and custom ATS, which expose no public JSON. The script's
sweet spot is tech and mid-market (verified live against Greenhouse, Lever, and Ashby boards during
testing); for this segment, hiring evidence comes from LinkedIn sweeps instead.

## Production scale

This run is 16 hand-evidenced records; a production motion needs hundreds per quarter. The split
that scales: the rubric and evidence standard stay fixed; candidate generation and per-account
evidence gathering parallelize across agents or a Clay waterfall (each account is an independent
research task against the source map); the scorer stays the deterministic core so every ranking
remains reproducible and auditable. Judgment concentrates where it belongs: setting criteria,
regrading evidence, and reading the rejects.

## Gaps

- **Hiring criterion unexercised.** See above; scores move if LinkedIn sweeps land.
- **Rubric v2 needs first-party criteria.** The public ICP cannot see qualification logic an
  internal session would add: cloud-incumbent alignment as a modifier (Azure gravity pulls to
  OpenAI, AWS to Bedrock), in-house build strength as a negative modifier (the TD/Layer 6 pattern),
  and SI/consulting-partner overlap (who Accenture and Deloitte are steering). This rubric is the
  best public approximation, and it knows it.
- **Infrastructure evidence is thin for banks and insurers.** The tier-2 cluster at exactly 55 is
  honest: their hybrid or sovereign posture was not evidenced at Tier A/B this sweep. Deeper
  enrichment could promote several to tier 1.
- **Some dates are retrieval dates.** Undated sources carry the check date, marked as such.
- **Universe breadth.** Canada-weighted plus European telcos; healthcare and non-Canadian government
  are unexplored, and the SoftBank JV implies Japan is channel-locked and needs its own strategy.

## Refresh cadence

Signals: re-check every two weeks (hiring and press decay fast); the ATS check is scriptable per
run. Firmographics: quarterly. Full re-run trigger: any Cohere partnership announcement (it moves
accounts to suppression), any competitor lock-in announcement (it moves accounts to disqualified),
or a material ICP revision.

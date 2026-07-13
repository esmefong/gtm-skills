# Ideal Customer Profile — Linear

Who Linear is for. Anchor product, positioning, and go-to-market to these.

> **Real company, public data.** Built from Linear's **public** voice-of-customer discussion (G2,
> "Linear vs Jira" comparisons and migration write-ups, Product Hunt). See `input.md` for the
> raw signal and sources. Quotes are representative and lightly edited from public discussion,
> handles removed.
>
> **This example exercises the team-buyer branch.** Linear is bought by a software team, so the
> account-level ICP and buying-committee modules switch on. (Compare `../notion/icp.md`, which shows
> an *individual* buyer with those modules off.) Built by the skill's opt-in public-data sweep with
> no first-party data — so confidence is directional; see Gaps.

**Data sources:** public-data sweep only — G2 review summaries, "Linear vs Jira" comparison and
migration write-ups, Product Hunt (July 2026). **Confidence:** directional; public data skews toward
vocal switchers and enthusiasts, and much of it is comparative (vs. Jira). No first-party data.

---

## Account-level ICP

The company that fits. A rep should be able to score a new account in 30 seconds.

**Firmographics:** software-building companies — VC-backed startups through scale-ups, ~10-500
employees with a real engineering org; product- and velocity-conscious. **Technographics:**
GitHub/GitLab, Slack, modern CI/CD and deploy stack, Figma; *not* deeply invested in Atlassian's
ecosystem. **Behavioral signals (in-market):** rapid engineering hiring, recent funding, public
complaints about Jira, a newly hired VP/Head of Engineering (tooling changes follow leadership
changes), migrating off legacy tooling. **Disqualifiers:** non-software orgs needing general
work-management and reporting → deprioritize; large enterprises standardized on Jira with heavy
custom workflows, JQL reporting, and compliance/audit needs → walk (the "afraid it becomes Jira"
trap); orgs where PM/ops, not engineering, owns the tracker → weak fit.

---

## Buyer profile 1: The team escaping Jira (primary)

*The dominant situation in the data: an engineering team has hit a friction threshold with Jira and
a champion decides to move.*

### Who they are
An engineering lead, EM, or founding engineer at a fast-moving software team, plus the developers
who live in the tracker daily. Builders who feel their tool is taxing their focus. The champion is
technical and usually not the budget holder.

### The trigger (why now)
- **Jira friction crosses a pain threshold.** *"Linear is fast in a way that makes you realize how
  slow Jira had become"* — latency and ceremony pile up (a bug report *"48 seconds in Jira, 11 in
  Linear"*) until a new eng leader or a fed-up team says enough. (Source A)
- **Onboarding pain.** *"New developers need days to become proficient with Jira"* vs. *"hours"* in
  Linear. (Source A)
- **Low team morale with the tracker itself.** Satisfaction *"3.2/10"* before the switch. (Source A)

### What they're doing before they find us
Suffering Jira (slow, over-configured, low satisfaction), or duct-taping GitHub Issues +
spreadsheets + Slack for planning.

### What success looks like for them
- **The tool gets out of the way.** *"The biggest driver wasn't any single feature — it was the
  feeling that the tool got out of the way"* (satisfaction 3.2 → 7.8). This is the emotional core.
- **Devs stay in flow.** *"Incredibly fast… Command-K lets you jump anywhere without leaving the
  keyboard"*; *"work right from their terminal without constantly context switching."* (Source B)
- **More shipping, less tracker-wrangling.** *"Spend more time shipping instead of managing the
  tracker."* (Source B)

### What almost stops them (barriers + Four Forces)
- **Anxiety — too minimal for leadership.** *"Too minimal if you need advanced reporting… I miss
  custom dashboards like JQL."* (Source B)
- **Anxiety — eng-only.** *"It's built for software development; teams outside engineering find it
  too specialized."* (Source B)
- **Anxiety — bloat/brand fear.** *"Afraid it becomes Jira"* one day. (Source C)
- **Habit — Jira is entrenched org-wide,** and migration is real work (*"we migrated 2,000 issues"*).
  (Source A/C)
- **Economic — per-seat cost** *"expensive for larger orgs."* (Source C)

Push (Jira pain) + Pull (speed/DX) usually beat Anxiety + Habit *once a champion has leadership air
cover* and the team has felt the speed in a trial.

### How they compare options (decision criteria, in priority order)
Speed/latency → developer experience and GitHub integration → opinionated simplicity vs.
configurability → reporting depth → per-seat price → engineering-only vs. whole-org fit.

### The buying committee
| Role | KPI | Top barrier | What wins them | Veto power |
|---|---|---|---|---|
| **Champion** — eng lead / EM / founding eng | Team velocity & morale | "Will leadership fund it, and will non-eng go along?" | Speed + DX their team feels in a trial | Drives the deal |
| **End users** — developers | Stay in flow | "Another migration" | Keyboard-first, terminal/GitHub-native workflow | Adoption makes or breaks it |
| **Economic buyer** — VP Eng / CTO / founder | Output per dollar | Per-seat cost at scale | Velocity/shipping ROI story, not a feature list | Can block on price |
| **Blocker** — PM/ops or IT on Atlassian; non-eng leads wanting reporting | Cross-team reporting, standardization | "Too eng-only; weak dashboards" | A reporting roadmap; keep eng as the wedge | Stalls org-wide rollout |

**System read:** developers pull it in bottom-up; the engineering leader champions and often holds
budget; the veto is whoever owns org-wide standardization and reporting (PMO/IT, or a
reporting-hungry exec). Win the team first, then arm the champion with a velocity-ROI story for
finance and a reporting answer for the blocker.

### How to speak to them
- **Lead with speed and "gets out of the way,"** not feature breadth.
- **Talk to developers in their language** — keyboard-first, GitHub-native, works from the terminal.
- **Meet the bloat fear head-on:** "opinionated on purpose," and mean it.
- **Don't pitch a Jira-style everything-tracker** — that invites the reporting/customization objection.

### Where to find them (journey + channels)
Discovery through Linear's design-led brand, X/Twitter, Product Hunt, and dev word of mouth; active
evaluation through "Linear vs Jira" comparison and migration content. The motion is bottom-up trial,
so optimize for a team reaching the speed "aha" fast. **Channels:** brand/design content, dev
communities, comparison + migration SEO, trial activation.

---

## Buyer profile 2: The greenfield team choosing fresh (secondary)

A new startup or newly formed team picking a tracker from scratch, with no Jira scar tissue. The
Habit barrier is near zero (nothing to migrate), so the sale is pure Pull: speed, DX, "start clean
and stay fast." High-fit and low-friction, but a smaller pool. Validate volume before dedicated
spend (see Gaps).

---

## Who Linear is NOT for
- **Non-software orgs / whole-company work management** needing general reporting → ClickUp/Asana territory.
- **Enterprises standardized on Jira** with heavy custom workflows, JQL reporting, and compliance/audit needs → high-friction, low-fit.
- **Teams that want maximal configurability** — Linear's opinionation is a deliberate mismatch for them.

---

## How to win

**USP — why you, why now.** *The issue tracker that's fast enough to get out of your team's way, so
engineers ship instead of managing tickets.* Urgency lives in the buyer's situation: Jira friction
has crossed a threshold.

**Narrative.** Start in their world (the tracker is a tax on focus), name the shift (a tool built for
how engineers actually work), land the win (the tool disappears and shipping speeds up). Sourced from
the "got out of the way" satisfaction story.

**Differentiation (1-2 axes only).** (1) raw speed/performance, (2) developer experience —
GitHub-native, keyboard-first. Compete there; do *not* fight Jira on configurability and reporting,
which is where the objections live.

**Channel strategy.** Design-led brand, developer word of mouth, comparison/migration SEO, and
bottom-up team trials engineered to hit the speed "aha" quickly.

---

## Insight-to-action routing

| Research finding | Routes to |
|---|---|
| "Realize how slow Jira had become" trigger | Hero copy, "Linear vs Jira" pages, paid search |
| "Gets out of the way" success factor | Benefit copy, onboarding promise, testimonial selection |
| "Too minimal" reporting + eng-only barrier | Reporting-roadmap content, honest scope in sales, FAQ |
| "Could become Jira" bloat fear | Brand positioning ("opinionated on purpose") |
| Per-seat cost at scale | Pricing-page framing (velocity ROI), champion enablement |
| Journey (Product Hunt, X, comparison content, bottom-up) | Community/brand strategy, trial activation |

---

## Validation plan

**Hypotheses.**
- *If teams that hit the speed "aha" in their first session convert at ≥2x baseline,* optimize the
  whole funnel around first-session activation.
- *If greenfield teams retain and expand better than migrators,* weight acquisition toward new teams.

**Next validation step per gap.** See Gaps.

**Refresh cadence.** Weekly community + review scan, monthly interviews with recent switchers *and*
churners (the ones who left Linear are as informative as the ones who joined), quarterly re-cut.

---

## Gaps in this document
- **Public-data only, no first-party.** Skews toward vocal switchers and enthusiasts; lost deals and
  the quiet middle are under-sampled. *Next:* win/loss interviews, especially teams that evaluated
  Linear and stayed on Jira.
- **Committee is inferred** from motion patterns, not interviews. *Next:* validate who actually holds
  budget and veto across 5-8 real deals.
- **Pricing threshold unknown** — where per-seat cost flips the decision. *Next:* win/loss pricing
  analysis by team size.
- **Quotes are representative/aggregated** from public reviews and comparison articles, not a verified
  verbatim sample. *Next:* a tagged, dated, sourced VoC pass before betting spend on any one message.

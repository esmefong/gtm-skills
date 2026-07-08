# Research sources

How to gather the raw signal the skill runs on. No single method gives the full picture: interviews give
depth, surveys give scale, behavioral data gives honesty, and community monitoring gives you the market's
own vocabulary. Use as many as you can. Read this when a user needs to collect signal, or is working from
community data.

Treat research as an engine, not a one-time project. The strongest ICP work runs these on a loop and
routes every finding to an action.

---

## 1. Customer and near-buyer interviews

The richest source. Unscripted 30-45 minute recorded calls, one opening question, then follow the story.
Full method in `frameworks.md` (§1). Who to talk to:

- Recent buyers (last ~90 days) — the decision is fresh.
- People who considered you and chose a competitor.
- People who considered you and did nothing.
- People who bought a competitor without considering you.
- Deals that stalled or dropped mid-funnel.

The non-buyers carry the barriers you most need. Offer a small incentive with a calendar deadline to
drive scheduling. Transcribe and tag within 48 hours while it's fresh.

---

## 2. Surveys (scaled, passive intake)

Short (3-5 questions), sent automatically to new customers in their first week, capturing the triggering
situation in the buyer's own words at peak motivation. Keep it situation-focused:

- "What was happening in your work or life that made you decide to act *now* vs. later or never?"
- "What other options did you seriously consider?"
- "What almost stopped you?"
- "How did you first hear about us?"
- Optional: "Open to a 15-minute call?"

Over time these build a dataset that reveals patterns without an interview for every data point.

---

## 3. Sales / success call debriefs

After every discovery call, demo, or onboarding, log 2-3 sentences: what situation is this person in,
what's their biggest concern, what decided it (or what's holding them back). Sales talks to far more
prospects than research ever will; minimal structured notes turn every call into a data point, and it's
often the only window into people who never agree to a formal interview.

---

## 4. Community and channel monitoring (the natural-language method)

A recurring scan of the places your buyers already talk to each other: Slack and Discord communities,
subreddits, niche forums, X/LinkedIn, and review sites (G2, Capterra, Trustpilot). This is where you get
the market's real vocabulary, because people speak more freely to peers than to a vendor on a call.

This method deserves special attention because it is often the fastest way to an authentic ICP and it
scales without recruiting anyone. It was the primary source behind more than one ICP the author has
shipped in production.

**How to run it:**

1. **Find the room.** Identify 2-4 places the target audience congregates *as peers*, not as your
   prospects. For B2B: an industry Slack/Discord, the relevant subreddit, the review-site category page.
   For consumer: the platform and hashtags where the situation gets discussed.
2. **Monitor on a cadence** (a weekly pass is plenty). You're not after volume; you're after *recurring
   language, emotional triggers, and situations* that line up with or challenge what interviews tell you.
3. **Capture verbatim.** Pull the exact phrases people use for their situation ("I feel like I'm falling
   behind," "we finally outgrew the spreadsheet," "walking on eggshells"). Also capture: complaints about
   incumbents and competitors, "just switched / just bought" posts and what drove the decision, and the
   questions that reveal gaps in understanding.
4. **Map to the 5 Rings.** Sort captured language into Priority Initiative, Success Factors, Perceived
   Barriers, Decision Criteria, and Journey. Build the ICP *in the community's own words* rather than
   imposing your terminology.
5. **Let it validate continuously.** Because the scan runs weekly, shifts in the market's concerns surface
   quickly, which makes this a validation channel as well as a discovery one.

**Why it works:** community discourse is unscripted and emotionally honest, it catches situations in the
moment (someone posts about a barrier right after they hit it), and it hands you marketing vocabulary that
already resonates because the audience is the one who wrote it.

**Review sites specifically:** G2 / Capterra reviews are a goldmine of decision criteria and barriers in
buyer language. A line like "we had to implement it ourselves because their team was overbooked" is a
capacity signal, not a product complaint. Read raw reviews of both you and your competitors and mine for
patterns.

**Running this actively (the skill's opt-in public-data sweep).** The skill can perform this monitoring
itself with web search — pulling public discussion of the product and its competitors on demand, rather
than waiting for the user to collect it. This is **opt-in**: offer it and confirm scope before searching
(see `SKILL.md`, "The public-data sweep"), because some products are confidential. Two rules when you do:
weight public signal **below first-party** research (it over-represents vocal enthusiasts and churners,
and often describes competitors), and mark it as directional in the Gaps. Everything in "Ethics and
sanitization" below applies: public sources only, anonymize, cite.

---

## 5. Behavioral and funnel data (the honesty check)

What people *do*, not just what they say. Which pages high-intent visitors dwell on, which email topics
drive clicks from leads who eventually convert, where interested people abandon the funnel, and whether
lead sources convert at different rates. The gap between what buyers *say* mattered and what their
behavior shows is often where the most useful insight lives (they claim they cared about depth, but they
spent ten minutes on pricing and thirty seconds on the docs).

---

## Research cadence

| Rhythm | Frequency | Scope | Output |
|---|---|---|---|
| Deep dive | Every 3-5 months | Full 5-ring analysis, ~20-30 interviews | Updated situation map, revised ICPs, new positioning hypotheses |
| Pulse check | Monthly | 3-5 interviews with recent buyers / drop-offs | Validated/invalidated hypotheses, language updates, barrier alerts |
| Passive intake | Always on | Surveys, call debriefs, community monitoring, funnel data | Steady signal feeding the reviews above |

---

## Ethics and sanitization

- **Public spaces only, and read the room's rules.** Monitor communities you can legitimately access, and
  respect each platform's terms and norms. Many communities are fine with observation; some are not.
- **Anonymize.** When you quote community or interview language in a deliverable, strip names, handles,
  and any detail that could identify a person. Capture the *language and the situation*, not the individual.
- **Never fabricate.** Do not invent quotes or attribute language no one said. If you're demonstrating or
  working without data, label every claim a hypothesis and name the validation step.
- **Handle customer data with care.** Real interview transcripts and customer records are sensitive. Keep
  them out of any public artifact, and out of shared examples.

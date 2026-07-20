# Ideal Customer Profile: Cohere

Who Cohere is for. Anchor product, positioning, and go-to-market to these.

> **Real company, public data.** Built from Cohere's public positioning, press/analyst coverage, and
> enterprise-LLM buyer frameworks (see `input.md` for sources). No first-party data, and enterprise
> buyers leave less public voice than consumer ones, so this is directional. Gaps are listed at the end.
>
> **This example exercises the enterprise team-buyer path in full:** an account-level ICP plus a
> buying committee where **security and compliance are a structural veto**, not a footnote. It also
> shows demand-side honesty: Cohere is usually the *specialist / secondary* vendor, and the ICP is
> built around where that wins rather than pretending Cohere is the default primary.

**Data sources:** Cohere site, TechCrunch/eMarketer/IntuitionLabs, Sacra, and 2026 enterprise-LLM
selection frameworks (July 2026). **Confidence:** directional; skews to analyst/press framing.

---

## Account-level ICP

The company that fits. A rep should be able to score a new account in 30 seconds.

**Firmographics:** large enterprises (1,000+ employees, often 5,000+) in **regulated or sensitive-data
sectors**: financial services, government and public sector, healthcare and insurance, telecom.
Frequently global or non-US, where **data residency and sovereignty** are live requirements.
**Technographics:** existing cloud plus on-prem/hybrid infrastructure; internal knowledge to build
retrieval and agents on; often a policy that forbids sending data to public LLM APIs. **Behavioral
signals (in-market):** a leadership GenAI / AI-transformation mandate; a recent Head of AI / GenAI
hire; a GenAI pilot blocked at security review; a data-residency or in-country requirement.
**Disqualifiers:**
- **Comfortable using public APIs, no data constraint** → they'll default to OpenAI or Anthropic;
  deprioritize.
- **Wants one general-purpose *primary* model** (frontier reasoning, coding, broad ecosystem) → that's
  OpenAI/Anthropic; Cohere is the specialist, not the default primary.
- **Consumer, SMB, or individual developers** → wrong scale and motion entirely.

---

## Buyer profile 1: The regulated enterprise that can't send its data out (primary)

*The dominant situation: a GenAI mandate collides with a hard data constraint. The AI lead champions
it; security and compliance decide it.*

### Who they are
An AI/ML lead, data-science lead, or AI-transformation lead inside a large regulated enterprise (a
bank, a government agency, a telecom, a health insurer). They have a mandate to ship GenAI and a real
use case, but the data is sensitive, regulated, or must stay in-country. They are not the budget
holder, and they cannot ship anything security and legal won't clear.

### The trigger (why now)
- **A GenAI mandate meets a use case public APIs can't touch.** *"Legal won't let us run this on a
  public API."* Leadership wants GenAI shipped; the data can't leave the environment. (Source D)
- **A pilot stalls at security review.** A promising OpenAI/Azure pilot fails compliance or data-
  governance sign-off. (Source D)
- **A data-residency / sovereignty requirement.** *"Data must stay in-country."* Government, finance,
  or a non-US market forces on-prem or regional deployment. (Source A/B)

### What they're doing before they find us
Running limited internal pilots; stuck between "must adopt GenAI" and "can't send data out"; leaning on
the hyperscaler already in their stack (Azure OpenAI, Bedrock); or blocked and waiting on security.

### What success looks like for them
- **Ship GenAI on sensitive data without the data leaving their environment**, and pass security and
  compliance. Cohere "never sees or interacts with a customer's data" in private deployment. (Source A)
- Strong **retrieval on their own internal knowledge** (RAG), which is Cohere's recognized specialty. (Source B)
- **Multilingual** coverage for a global or non-English operation.

### What almost stops them (barriers + Four Forces)
- **Anxiety: "is a specialist vendor good enough vs OpenAI/Anthropic?"** Model quality clusters, but
  the perception risk is real. (Source B/C)
- **Anxiety: deployment complexity.** On-prem / air-gapped / VPC is harder than calling a hosted API.
- **Habit: default to the incumbent hyperscaler.** Azure OpenAI and Bedrock also offer data residency
  and are already in the stack: *"nobody got fired for buying Microsoft."* (Source C) This is the
  single biggest force to overcome.
- **Push + Pull** (the data constraint plus private deployment and RAG fit) beat these only once
  security/compliance is convinced the private-deployment story is real.

### How they compare options (decision criteria, in priority order)
1. **Private / on-prem / air-gapped deployment** ("bring the model to your data").
2. **Data residency / sovereignty** guarantees.
3. **Security and compliance posture** (the gate).
4. **RAG / retrieval quality on their own data**, and **multilingual** coverage.
5. Cost, flexibility, exit options. (Raw model quality is late on the list; it clusters.)

### The buying committee
For Cohere's buyers, security and compliance is not an influencer, it is the gate the whole value
proposition is built to pass.

| Role | KPI | Top barrier | What wins them | Veto power |
|---|---|---|---|---|
| **Champion**: Head of AI / ML / data-science lead | Ship the GenAI mandate | "Will security clear it, and is a specialist good enough?" | A private-deployment path that passes the gate + RAG fit on their data | Drives the deal |
| **Economic buyer**: CIO / CDO / CFO | ROI on the AI mandate, vendor risk | "Why not just use the hyperscaler we already pay?" | Sovereignty/control story + a clean secondary-vendor fit | Can block on cost/risk |
| **Technical buyer**: CTO / VP Eng / ML platform lead | Integration, deployment, stability | "On-prem/air-gapped is complex" | Deployment support, reference architectures | Can veto on fit |
| **Security / Compliance / Legal**: CISO, data governance | Data never leaves; audit and residency hold | "Prove the data is truly private/in-country" | Private-deployment proof, certifications, air-gapped option | **Structural veto** |
| **End users**: developers / data scientists | Build the RAG/agent app | "Is the retrieval actually good?" | Retrieval quality, docs, multilingual | Adoption drag if ignored |

**System read:** the AI lead champions; the hyperscaler-incumbent habit is the economic buyer's default;
and **security/compliance is the make-or-break gate**. Cohere wins by being the vendor that clears the
gate the others can't, not by out-modeling them. Arm the champion with the private-deployment proof for
security and a "specialist secondary, not rip-and-replace" story for the CIO.

### How to speak to them
- **Lead with "the AI you're actually allowed to deploy,"** not "the best model." The situation is a
  data constraint, so private / sovereign / on-your-data is the hook.
- **Address the security gate first,** not in an FAQ: private deployment, air-gapped option, data never
  leaves, residency. That is the whole sale.
- **Own the specialist frame.** Retrieval and multilingual on your own data, as a strong secondary in a
  multi-vendor stack. Do not claim to be the general-purpose primary; it invites the wrong comparison.

### Where to find them (journey + channels)
Enterprise and analyst channels (Gartner-style research), cloud marketplaces and partnerships (Oracle,
AWS), sovereign-AI and government procurement channels, and direct enterprise sales. Not community
forums; these buyers move through analysts, partners, and RFPs.

---

## Buyer profile 2: The multi-vendor platform team adding a specialist (secondary)

*An enterprise already running a primary-secondary LLM router adds Cohere for a specific workload:
retrieval/embeddings, multilingual, or a private-deployment carve-out the primary can't serve.* The
trigger is a concrete workload where the primary underperforms or isn't allowed. Smaller and more
technical than ICP 1, but it matches the market reality that Cohere is "often the right secondary
choice." Validate the size of this motion before investing (see Gaps).

---

## Who Cohere is NOT for
- **Enterprises comfortable with public APIs**, no data-residency constraint. They default to
  OpenAI/Anthropic and Cohere will lose on model perception.
- **Teams wanting a single general-purpose primary** for frontier reasoning, coding, or the broadest
  ecosystem. That is not Cohere's frame.
- **Consumer, SMB, and individual developers.** Wrong scale, motion, and price.

---

## How to win

**USP: why you, why now.** *The enterprise AI you're actually allowed to ship: private, sovereign, and
deployed on your own data, purpose-built for retrieval and multilingual.* Why now sits in the buyer's
situation: a GenAI mandate blocked by a hard data constraint.

**Narrative.** Start in their world: leadership wants GenAI, you have the use case, but the data can't
leave your environment and the public-API pilot failed security review. Cohere brings the model to your
data, clears the gate, and is built for retrieval on your internal knowledge.

**Differentiation (1-2 axes only).** (1) Private / sovereign / deployable-anywhere, and (2) enterprise
RAG + multilingual. Compete there. Do not fight OpenAI/Anthropic on general model quality or ecosystem
maturity; that comparison is a loss.

**Channel strategy.** Analyst relations, cloud partnerships (Oracle, AWS), sovereign/government
procurement, and direct enterprise sales with security-led proof.

---

## Insight-to-action routing

| Research finding | Routes to |
|---|---|
| "GenAI mandate blocked by a data constraint" trigger | Hero copy, enterprise sales opener, analyst briefings |
| "Ship on sensitive data, pass the gate" success factor | Security-led collateral, reference architectures, case studies |
| Hyperscaler-default habit (biggest barrier) | "Specialist secondary, not rip-and-replace" narrative, CIO enablement |
| Security/compliance gate | Private-deployment proof, certifications, air-gapped demos, DPAs |
| RAG + multilingual decision criteria | Retrieval benchmarks on customer data, multilingual proof |
| In-market signals (mandate, blocked pilot, residency) | Account targeting for sales and the outbound-engine |

---

## Validation plan

**Hypotheses.**
- *If accounts with a hard data-residency/sovereignty constraint convert at materially higher rates than
  general enterprise accounts, the "can't send data out" situation is the primary ICP* (public framing
  strongly implies it).
- *If a majority of wins are secondary-vendor (router) deals rather than primary, ICP 2 deserves its own
  motion and messaging.*

**Next validation step per gap.** See Gaps.

**Refresh cadence.** Quarterly, because the enterprise-LLM landscape and the primary/secondary dynamics
shift fast; re-check win/loss against OpenAI, Anthropic, and the hyperscalers each quarter.

---

## Gaps in this document
- **No first-party data; analyst/press-sourced.** Enterprise buyers leave little public voice, so the
  triggers and committee are inferred, not from real win/loss interviews. *Next:* win/loss interviews,
  especially deals lost to a hyperscaler at security review.
- **Primary-vs-secondary split is unmeasured.** The "usually secondary" claim is from analyst framing.
  *Next:* internal data on what share of wins are primary vs. router-secondary.
- **Sector-specific ICPs not broken out.** Finance, government, and healthcare likely differ on the
  compliance gate and buying process. *Next:* a per-vertical cut.
- **Quotes are representative/aggregated** from public writing, not a verified verbatim sample. *Next:*
  a tagged, dated, sourced VoC pass with real practitioners before betting spend.

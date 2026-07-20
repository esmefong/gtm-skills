# Raw research dump: Cohere (worked example input)

> **Real company, public data.** This profiles [Cohere](https://cohere.com) using **public**
> sources: Cohere's own site, press/analyst coverage, enterprise-LLM buyer frameworks, and
> practitioner commentary. Cohere sells to large enterprises, so the "voice of customer" here is more
> analyst/press/case-study sourced than consumer-forum sourced. Claims are paraphrased from public
> writing with sources cited at the bottom. Built by the skill's opt-in public-data sweep (no
> first-party data), so confidence is directional; see the Gaps in `icp.md`.

**Product:** Cohere builds enterprise AI: large language models (Command), embeddings and retrieval
(Embed, Rerank), and **North**, an enterprise agent platform that runs in a customer's own
environment. Toronto-based. **Positioning:** private, secure, deployable-anywhere AI for enterprises
with sensitive or regulated data ("bring the model to your data"). **Top alternatives buyers name:**
OpenAI (often via Azure OpenAI), Anthropic, and the hyperscaler-hosted options (AWS Bedrock, Azure,
Google Vertex) that also offer regional deployment.

---

## Source A: Who buys, and the use cases (press + Cohere)

- Named enterprise customers include Oracle, RBC, Bell, LivePerson, STC Group, Fujitsu, and LG,
  using the models for document summarization, chatbot automation, intelligent search, and data
  analysis in **highly regulated sectors**.
- North (launched Aug 2025) can run on an organization's **on-premise infrastructure, hybrid clouds,
  VPCs, or air-gapped environments**. "Operating on an organization's private infrastructure ensures
  Cohere never sees or interacts with a customer's data."
- Explicit target framing: "companies in highly regulated sectors like finance, government, or
  healthcare," and "governments and regulated industries seeking AI solutions that keep data within
  national borders" (sovereign AI).

## Source B: The decision criteria enterprises actually use (buyer frameworks, 2026)

- The enterprise procurement question has shifted from "which model is best" to "which combination of
  contracts, capabilities, and exit options fits our risk profile." Public benchmarks are "nearly
  useless" because frontier models cluster within a few points.
- For **regulated industries, data residency is often a hard constraint.** Deployment location,
  privacy guarantees, and compliance posture outweigh raw model quality.
- Cohere's recognized strength: **enterprise RAG / retrieval.** "Command R+ handles generation,
  Embed v4 leads on multilingual retrieval, and the API is purpose-built for retrieval workflows."

## Source C: The competitive reality (the honest, important one)

- "Smaller specialty vendors like Cohere are still relevant for specific niches but are **rarely the
  primary vendor** for an enterprise, and are **often the right secondary choice**."
- Most enterprise 2026 production systems "use 2-3 providers via a router pattern, not a single
  vendor": a primary vendor handles 70-80% of traffic, a second handles the rest.
- The default gravity is toward the incumbent hyperscaler: Azure OpenAI and AWS Bedrock also offer
  regional deployment and data-residency guarantees, and they're already in the enterprise's stack.

## Source D: The committee signals (from enterprise-AI buying discourse)

- Recurring stakeholders in a regulated GenAI purchase: an **AI/ML or data-science lead** who
  champions it; a **CIO/CDO** who owns the budget and mandate; **security, compliance, and legal**
  (data governance, CISO) who must clear it; and **procurement**. Security/compliance is described as
  the gate that blocks public-API pilots in regulated firms.
- Common trigger language: a leadership "GenAI mandate," a use case that "legal won't let us run on a
  public API," and "data can't leave our environment / must stay in-country."

## Source E: Signals an account is in-market (for the future outbound-engine)

- A regulated enterprise announces a GenAI / AI-transformation initiative, or hires a Head of AI /
  GenAI lead.
- A GenAI pilot stalls or fails security/compliance review on a public API.
- A data-residency or sovereignty requirement (government, finance, health, or a non-US market).
- Cohere's own signals: North launched Aug 2025; large funding rounds; cloud partnerships (Oracle, AWS).

---

## Sources
- [Cohere: Enterprise Data Commitments](https://cohere.com/enterprise-data-commitments) and [Security](https://cohere.com/security)
- [Cohere's North agent platform: TechCrunch](https://techcrunch.com/2025/08/06/coheres-new-ai-agent-platform-north-promises-to-keep-enterprise-data-secure/)
- [Cohere launches private AI platform: eMarketer](https://www.emarketer.com/content/cohere-launches-private-ai-platform-sensitive-enterprise-data)
- [Cohere enterprise AI profile: IntuitionLabs](https://intuitionlabs.ai/articles/cohere-enterprise-ai-llm-profile)
- [OpenAI vs Anthropic vs Cohere: Sacra](https://sacra.com/research/openai-vs-anthropic-vs-cohere/)
- [Enterprise LLM Selection Framework 2026: Wolyra](https://wolyra.ai/enterprise-llm-selection-framework-2026/)

# Research brief

- **Working title:** Trustworthy agent memory: governance of LLM-agent memory in regulated industries (finance)
- **Research question(s):** How should the persistent memory of LLM agents (what they store, recall, update and forget across sessions and clients) be designed, evaluated and governed so it meets the requirements of regulated financial services? Sub-questions (to be sharpened after the review):
  1. What memory behaviors create regulatory or trust risk (leakage across clients or information barriers, stale/contaminated recall, poisoning, non-erasable personal data, unauditable decisions)?
  2. Which technical mechanisms (provenance, access control, retention/erasure, integrity checks, audit logging) mitigate them, and at what cost to agent utility?
  3. How can compliance of agent memory be measured (benchmark / evaluation protocol)?
  4. How do these map onto regulatory obligations (EU AI Act, GDPR right to erasure, SR 26-2 / OCC 2026-13 model risk management (replaced SR 11-7 on 2026-04-17; excludes GenAI/agentic AI), MiFID II / SEC & FINRA record-keeping, DORA)?
- **Field / sub-area:** AI in finance; LLM agents; AI governance, security and privacy
- **PI expertise & angle:** Both industry practitioner and academic; knows practical constraints in financial institutions. Interested in all four angles: technical mechanisms, evaluation/benchmark, governance & regulation, attacks & risks. The literature review should decide the primary angle.
- **Goal & target venue / deadline:** Not decided. Framing and venue (ML venue, FinTech venue, or industry) to be chosen after the gap analysis.
- **Review breadth (PI, 2026-09-24): broad.** In addition to the core topic, the review covers:
  (a) the regulatory landscape relevant to agent memory in finance (financial conduct, record-keeping,
  model-risk, data-protection, AI-specific and operational-resilience rules, plus standards and regulator
  statements on GenAI and agents), across EU, UK, US and major APAC jurisdictions;
  (b) agent evaluation metrics and benchmarks in general, and memory benchmarks in particular;
  (c) evaluation methods and metrics for trustworthiness and memory governance (privacy/leakage,
  contextual integrity, erasure/unlearning verification, provenance/auditability, integrity under poisoning,
  staleness/consistency, compliance checking);
  (d) industry practice: memory products/platforms and how financial institutions govern GenAI and agents today.
- **Scope in:** Persistent/long-term memory of LLM agents (vector stores, episodic/semantic memory, memory-management agents, shared multi-agent memory); financial use cases (advisory, KYC/AML, trading assistants, customer service, compliance ops). Adjacent regulated domains (healthcare, legal) as transfer sources.
- **Scope out (initially):** General LLM training-data privacy unrelated to agent memory; model weights governance except where it overlaps memory (e.g., unlearning).
- **Resources:** API-based LLMs only (modest budget), laptop compute. Public/synthetic data by default; proprietary internal data may be possible subject to institutional approval, so design must not depend on it.
- **Preferences:** Empirical contribution that is credible to both ML and finance/regulatory audiences.
- **Ethics / data constraints:** No real customer data without approval; synthetic client profiles for experiments. Keep proprietary material out of any shared artifact.
- **Success looks like:** A clearly novel contribution (e.g., a benchmark or mechanism with evidence) mapped to concrete regulatory requirements, publishable and usable in practice.

# arXiv:2603.11768 — Governing Evolving Memory in LLM Agents: SSGM framework (Lam, Li, Zhang, Zhao, 2026-03-12)
Tags: mechanisms, core. Read: full text via arXiv HTML (WebFetch-assisted), 2026-09-24.

- **Problem:** As memory becomes self-evolving (consolidation, summarisation), it drifts, gets corrupted and leaks. Surveys cover efficiency but not governance.
- **Method:** Conceptual architecture that decouples memory evolution from execution. (1) Write gate: NLI-based consistency check against protected core facts. (2) Temporal decay: a Weibull freshness score prunes stale entries. (3) Read gate: access-scoped retrieval (ABAC) for multi-tenant settings. (4) Reversible reconciliation: mutable active memory paired with an immutable episodic log, used to correct drift periodically.
- **Risk taxonomy:** stability (semantic/procedural/goal drift), validity (hallucination, temporal obsolescence), efficiency (latency, index bloat), safety (poisoning, privacy leakage).
- **Results:** None. Formal definitions plus a bounded-drift theorem (proof sketch). Hypotheses H1–H3 are left for future testing.
- **Stated limitations:** latency–safety trade-off; stability–plasticity conflict; graph-consistency scalability.
- **Critique:** A useful vocabulary (write gate / read gate / immutable log) that matches what regulated firms would ask for. It has no implementation or evidence, so cite it as a framing only. The "immutable log + mutable view" pattern conflicts with erasure duties, and the paper does not discuss this.

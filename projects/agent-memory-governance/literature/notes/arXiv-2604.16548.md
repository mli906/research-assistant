# Survey: long-term memory security in LLM agents across the memory lifecycle (arXiv:2604.16548, v3 2026-09-22)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Framework.** Six phases (Write, Store, Retrieve, Execute, Share & Propagate, Forget & Rollback) x four objectives (Integrity, Confidentiality, Availability, Governance). About 90 papers kept from 200+ screened.
- **Findings.** Defenses cluster at Write and Retrieve. Store, Share/Propagate and Forget/Rollback are sparse. No benchmark covers the whole lifecycle. Post-deletion verification has not been evaluated empirically.
- **Proposal.** "Verifiable Memory Governance" with five primitives: write authorization, provenance visibility, principal-scoped retrieval, rollbackability, verified forgetting. Security must be anchored in storage-time provenance.
- **Critique.** This is the closest competitor to any "governance of agent memory" framing, so the PI must position against it. It is not finance-specific and does not map to regulation. My taxonomy in partials/threats.md reuses its phase axis.

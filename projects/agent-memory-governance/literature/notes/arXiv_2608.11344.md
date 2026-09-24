# Governing Agentic AI in FinTech (arXiv:2608.11344), Han 2026
Read: abstract only (2026-09-24). Facet: regulation.
- Claim: the binding constraint is verifiability, not capability. Defines a "Verifiability Gap" (the verification that delegated authority demands minus the explainability/reproducibility retained after a decision), indexed to verifier, evidentiary standard and audit lag.
- Evidence (per abstract): provider model releases change historical financial actions. The frontier API rejects sampling controls and exposes no seed. Under tightest controls: local model 320/320 reproduced, hosted 319/320 and 959/960. Orchestration architecture acts as a latent policy layer; no execution record repeated across configurations.
- Relevance: record-keeping rules (SEC 17a-4(f) audit-trail and MiFID Del. Reg. 2017/565 Art. 72) require re-creating records, not re-running decisions. The paper shows that replay is not a substitute for retaining the actual memory state, prompts and outputs at decision time. This supports snapshotting what the agent recalled.
- Critique: single author, preprint; the finance tasks may be synthetic (unknown from abstract).

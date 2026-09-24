# Governance at the Boundary: Fiducia-bench, agent decomposition vs policy compliance (arXiv:2608.16055)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core, finance.

- **Question.** Does the agent finish *within policy*? Governability means escalating when obligated, abstaining when required, and leaving an auditable trail.
- **Data.** KYC/AML; 5 seed scenarios expanded to 100 synthetic variants (persona attributes, jurisdictions, amounts, ownership %). Policy packs and a verification harness, open source under CC BY 4.0.
- **Metrics.** Governed success (completion with no critical violation and correct escalation); fact attenuation (discovered facts missing from handoffs); propagation loss (facts that fail to trigger a required action); authority diffusion (which component caused the violation).
- **Results.** On Qwen2.5-32B at constraint distance 2, the single loop attenuated 0% of facts, the 3-stage pipeline 56%, and orchestrator + scoped subagents 85%. gpt-4.1-mini had lower rates (3%/6%) with the same ordering. Absolute governed success is very low (1.3%).
- **Limitations (stated).** No frontier models; KYC/AML only; handoff prompts not optimized.
- **Critique.** It is the only finance benchmark found that scores escalation, abstention and audit trail as first-class outcomes. It is single-episode with no persistent memory. Handoff attenuation is structurally the same as shared-memory write/read loss, so extending it to cross-session memory would be natural (my observation).

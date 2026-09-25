# MUTE: reliable data deletion in self-improving federated agent networks (arXiv:2607.28829)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core.

- **Problem.** In closed-loop self-improving federated agents, deleted data has already shaped the deployed policy, which then collected later "retained" trajectories. Retraining on the retain set leaves an **"influence echo"**: "the forgotten behavior may return and its membership signal may become visible again."
- **Method.** A server ledger records deployment version, collection window and aggregation weight. Influence is traced along aggregation and collection edges. Erasure then combines model-side negative preference optimisation on LoRA adapters with data-side quarantine or down-weighting of high-influence retained trajectories.
- **Data.** VLA policies (MiniVLA, π₀). **Parameters only**: there are no text skills or procedural memory.
- **Metrics and results.**
  - Behavioural Leakage Index (MIA AUC): about 0.51–0.54.
  - Influence Regeneration Rate: about 0.085–0.123.
  - Communication: 234.6 → 54 adapter uploads.
- **Limitations (implied; no limitations section).** Depends on a complete ledger; η is an upper bound; no Byzantine analysis.
- **Critique.** This is the **conceptual template for erasure propagation through derived experience**: deleted client data shapes later traces, which shape skills. The PI's setting is the non-parametric analogue (text skills), which MUTE does not cover. Its ledger idea maps onto skill lineage.

# arXiv:2606.18829 — GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents (Ren et al., 2026-06-17)
Tags: mechanisms, core (also evaluation). Read: full text via arXiv HTML (WebFetch-assisted), 2026-09-24.

- **Problem:** Memory benchmarks assume a single user. Institutional assistants have many principals, roles and deletion requests.
- **Method:** 91 long episodes, 2,218 hidden checkpoints, about 13.4 principals per episode, in medical, office, education and household domains. Metrics: utility U, access violations A, forgetting failures F. Combined score MGS = U·(1−A)·(1−F). Baselines: long-context, RAG-naive, RAG-policy, A-Mem, Mem0, ReMem-I/S. Backbones include GPT-5.4, DeepSeek-V4-Pro and Llama-4-Maverick.
- **Results (e.g., GPT-5.4, medical):** long-context U 91.4%, A 10.4%, F 2.3%, MGS 80.1%. Mem0 U 38.1%, A 28.1%, F 5.6%, MGS 25.8%. RAG-policy cuts leakage but over-refuses. ReMem takes more than 260 s per checkpoint. No method is strong on all three dimensions.
- **Stated limitations:** forgetting checked at the interface only (not physical erasure); GPT-4o judge (97.7% human agreement); soft attacks, not adversarial; baselines untuned.
- **Critique:** This is the closest existing benchmark to what a finance memory-governance benchmark would need. There is **no finance domain** and no information-barrier (Chinese-wall) structure. Retention *obligations* (must-keep) are not modelled alongside deletion. That is a clear gap to build on.

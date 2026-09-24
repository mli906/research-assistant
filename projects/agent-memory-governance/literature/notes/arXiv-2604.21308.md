# CI-Work: Benchmarking contextual integrity in enterprise LLM agents (arXiv:2604.21308)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Design.** Enterprise information flows in 5 directions (downward, upward, lateral, diagonal, external); each case has an Essential Set and a Sensitive Set in the retrieval context. 125 seeds (25 manual, 100 synthetic) and 1,000 entries; sensitive types include financial, legal/compliance, HR and customer data.
- **Metrics.** Leakage Rate (share of sensitive entries disclosed), Violation Rate (any disclosure), Conveyance Rate (share of essential entries disclosed = utility).
- **Results.** Across 9 LLMs, violation is 15.8–50.9% and leakage up to 26.7%. Conveyance correlates with violation (r=0.40); larger models leak more ("inverse scaling"); user pressure doubles violations; defense prompts cost 9% conveyance. Judge agreement with humans is 83–91%, biased toward precision (misses ~10% of subtle leaks).
- **Critique.** The closest CI benchmark to information-barrier settings (organizational hierarchy). It lacks persistent memory across sessions and explicit legal norms such as Chinese walls. Released at aka.ms/ci-work.

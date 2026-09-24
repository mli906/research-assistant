# Establishing Best Practices for Building Rigorous Agentic Benchmarks (ABC) (arXiv:2507.02825)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Contribution.** The Agentic Benchmark Checklist: task validity (solvable iff the capability is present), outcome validity (the grader reflects real success), and reporting.
- **Audit.** 10 benchmarks: 7 have task-validity issues, 7 have outcome-validity issues, and all 10 have reporting gaps. Examples: τ-bench scores empty responses as passing on unsolvable tasks (up to 38% overestimation) and accepts list-all-answers (40%); KernelBench ~31% overestimation; OSWorld underestimates by 28%; WebArena 1.4–5.2% from string matching and judges. CVE-Bench fixes reduced overestimation by 33%.
- **Critique.** Relevant to designing a governance benchmark: "abstain/refuse" must not be a free pass (the τ-bench flaw is exactly an abstention exploit, which a privacy/forgetting benchmark would reward). Report over-refusal as its own metric.

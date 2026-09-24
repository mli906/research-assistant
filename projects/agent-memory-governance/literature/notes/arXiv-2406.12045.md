# τ-bench: tool-agent-user interaction in real-world domains (arXiv:2406.12045)
Read: abstract + ABC audit (arXiv:2507.02825) findings. Tags: evaluation, core.

- **Design.** Simulated user (LLM) × agent with domain APIs and a policy document (retail, airline). Success is checked by comparing the final DB state with an annotated goal state.
- **Metric.** pass^k: the probability that all k i.i.d. trials succeed, a reliability/consistency metric (contrast pass@k).
- **Results (per abstract).** GPT-4o succeeds on <50% of tasks; pass^8 <25% in retail. Successor τ²-bench (arXiv:2506.07982) adds dual control.
- **Caveats.** ABC (arXiv:2507.02825) shows outcome-validity flaws: empty responses pass unsolvable tasks, and list-all answers pass. arXiv:2608.11323 finds agent main effects explain <3% of variance on τ²-bench.
- **Relevance.** pass^k is the right primitive for compliance: a control that works 1 time in 8 is not a control. Policy-document compliance is the closest general-agent analogue to regulatory rule adherence.

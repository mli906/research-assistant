# A-MemGuard: proactive defense for agent memory (arXiv:2510.02373, 2025-09)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Method.** Consensus validation across parallel reasoning paths drawn from retrieved memories, plus a separate "lessons" memory of detected failures to break self-reinforcing error loops.
- **Results.** EHRAgent direct poisoning ASR 100% to 2.13%. MMLU/MINJA 0.667 to 0.256 (GPT-4o-mini). About 7.8K tokens per EHRAgent task (vs 8.0K for an LLM-auditor baseline). Reports the best benign accuracy among the defenses it compares.
- **Limitations.** Needs enough benign history for consensus to work (cold start).
- **Critique.** Token overhead is compared only to another LLM defense, not to an undefended baseline. Consensus-based defenses are in principle open to collusive/salami attacks (arXiv:2608.01637), which were not tested.

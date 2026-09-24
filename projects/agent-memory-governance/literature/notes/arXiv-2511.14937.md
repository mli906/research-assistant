# CIMemories: compositional contextual-integrity benchmark for persistent memory (arXiv:2511.14937)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Problem.** CI benchmarks use small, simple contexts; persistent memory accumulates many attributes, and the same attribute is needed in one task and inappropriate in another.
- **Data.** 10 synthetic profiles (Faker + GPT-OSS-120B life events), ~147 attributes each across 9 domains including **finance**, 46 task contexts per profile. Labels from GPT-5 under three Westin privacy personas, kept only where all three agree.
- **Metrics.** Violation@n: attribute-level worst case, whether an attribute is ever revealed in an inappropriate task over n tasks/samples (≈1−(1−p)^n). Completeness: share of necessary attributes conveyed.
- **Results.** Violation rates range from 14.8% (GPT-4o) to 69.1% (Qwen-3 32B). Violations accumulate: GPT-5 goes from 0.1% (1 task) to 9.6% (40 tasks) and 25.1% (5 samples of the same prompt). There is a violation–completeness trade-off, and a "granularity failure": models find the right domain but cannot separate necessary from unnecessary details.
- **Limitations (stated).** Synthetic profiles; single-turn, no tool use; only 10 profiles.
- **Critique.** Violation@n is the right shape of metric for regulators, since worst case over repeated use is what counts. Labels are LLM-generated (not human- or regulation-grounded). License CC BY-NC-SA 4.0 (the non-commercial clause matters for industry reuse).

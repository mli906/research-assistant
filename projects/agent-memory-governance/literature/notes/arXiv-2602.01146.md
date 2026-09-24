# PersistBench: When should long-term memories be forgotten by LLMs? (arXiv:2602.01146)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Problem.** Two memory-induced safety failures: cross-domain leakage (memory from one domain influences unrelated queries) and memory-induced sycophancy.
- **Data.** 500 samples (200 leakage / 200 sycophancy / 100 beneficial-use control), generated with MCTS (Gemini-2.5-Pro), filtered on held-out models, and all checked by 6 human annotators; 4–16 memories per sample.
- **Metric.** Failure Rate with an LLM judge (5-point scale, ≥3 = fail; 3 inferences per safety sample).
- **Results.** Across 18 models the median FR is 53% for cross-domain leakage, 97.8% for sycophancy and 16.5% for beneficial-use failure. Leakage ranges from 4.0% (GPT-5.2) to 91% (Qwen3-235B-Think). Beneficial use correlates only weakly with safety (r=−0.38).
- **Limitations (stated).** Synthetic memories; abstracts away the extraction/write path; no tools/agents.
- **Critique.** Includes a benign control set, which lets over-restriction be measured (good practice). It measures model behavior given memories, not memory-system governance. License CC BY 4.0.

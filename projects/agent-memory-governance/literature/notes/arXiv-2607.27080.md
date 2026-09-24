# MemSecBench: tracking agent memory poisoning from persistence to consequence and repair (arXiv:2607.27080)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Design.** Write–Execute–Forget lifecycle with 7 checkpoints adjudicated by deterministic checks, judge models and programmatic gates rather than agent self-report. 310 task packages from 48 contexts (code/science, daily life, office). 24 configurations: harnesses OpenClaw and Hermes; memory Native, Mem0, Mem0-Graph, A-MEM; LLMs DeepSeek-V4-Pro, MiniMax-M3, GPT-5.5.
- **Metrics.** MPSR (write accepted and malicious semantics persist), MESR (adoption given persistence), E2E-ASR (passes all write and execute checkpoints), SRSR (selective repair without benign-memory loss).
- **Results.** Average MPSR 84.2%, E2E-ASR 50.3%, SRSR 56.1%. Adoption is the main bottleneck (76.1% recall vs 53.7% adoption). No backend is uniformly safer; Mem0's E2E-ASR swings ±13.5 points with the harness.
- **Limitations (stated).** Synthetic; no defenses compared; judge 90.6% agreement with humans; cases drafted with GPT-5.5.
- **Critique.** SRSR is one of the very few metrics that measure *repair* (targeted removal with preservation of benign memories), which is the same measurement shape as verified erasure. The harness-dependence finding means memory-backend results do not transfer across harnesses.

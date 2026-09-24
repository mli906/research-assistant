# From Untrusted Input to Trusted Memory: systematic study of memory poisoning (MPBench) (arXiv:2606.04329, 2026-06-03)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Contribution.** Four write channels: explicit instruction-executed, system-prompt-policy-driven, compaction-driven, experience-to-procedure (skills). Nine structural vulnerabilities across model, prompt and architecture layers. Six attack classes, split into strong-signal (explicit/conditional command insertion, salience-driven compaction) and weak-signal (policy-conformant fact injection, false precedent, skill-procedure insertion).
- **MPBench.** 3,240 attack cases and 2,997 benign cases across 7 domains; agents OpenClaw and HERMES on GPT-OSS-120B.
- **Results.** HERMES: ASR 66.7%, cross-session retrieval success 64.7% (conditional commands 92.8%). OpenClaw: ASR 34.3%, RSR 17.4%. More aggressive memory-write designs are more exploitable. Prompt-injection detectors (PIGuard, DataFilter, CommandSans, PromptArmor): best TPR 67.7%; about 58% on strong-signal attacks but only **about 25% on weak-signal** attacks; retraining adds under 10 pp.
- **Limitations.** Single model; static context delivery.
- **Critique.** The weak-signal class (policy-conformant facts, false precedent) is exactly how a finance attack would look, e.g. "client X is pre-approved for margin". Detectors built for prompt injection do not transfer to it.

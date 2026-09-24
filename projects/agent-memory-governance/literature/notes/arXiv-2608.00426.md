# MAPLE-Guard: memory-link poisoning in multi-agent systems (arXiv:2608.00426, 2026-08-01)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Threat.** One poisoned write is retrieved again later, promoted into shared memory and reused by other agents. No malicious message crosses a visible edge at the moment of harm.
- **Method.** Gates at write, retrieval (value-aware scoring), promotion (private to shared) and cross-agent reuse. Deterministic gates need no extra guard-LLM calls.
- **Setup.** 8 agents, 3 of them attacker-controlled; star/chain/tree topologies; benchmarks MMLU-MINJA, LongMemEval-MemoryGraft, AppWorld-AgentPoison, CSQA-PromptInject, InjectAgent; models Qwen3.5-122B-A10B and gemma-4-31B.
- **Results.** LongMemEval ASR 38.2% to 0.9% (MDSR 54.0% to 74.3%). AppWorld ASR 34.7% to 0.2% (MDSR 42.5% to 99.8%). InjectAgent 20.6% to 4.9%. Benign cost about 1-4 pp MDSR.
- **Limitations.** Assumes reliable provenance metadata; low-and-slow payloads can stay under per-event thresholds.
- **Critique.** The promotion gate maps directly onto an information-barrier (Chinese-wall) control between desks. Adaptive attackers are not evaluated.

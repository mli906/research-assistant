# Poisoning Agentic Alpha: adversarial vulnerabilities in multi-agent trading systems (arXiv:2608.24069, 2026-08-25)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Setup.** Trading pipeline with Analyst team, Research team, Trader and Risk manager; four topologies (linear, centralized, decentralized, hybrid). Q1-2026 data, BTC-USD/MSFT/NVDA/TSLA/AAPL, 61 trading days (305 asset-days). Black-box adversaries limited to source data and prompts.
- **Results.** Jailbreak (risk manager) ASR 98.9% but median $0 impact. Persuasive researcher: 47.6% success, -$60 expected value per attempt. Data poisoning (news): 20.5% success. Cumulative return degradation **1.45-12.38 pp** depending on architecture. No architecture is inherently robust.
- **Memory.** Agents do use a `past_memory` reflection slot, but **memory is not attacked on its own**. Persistence of poisoned lessons is untested.
- **Limitations.** One backbone; large caps only; no transaction costs.
- **Critique.** This is the closest finance paper found, and it shows the gap directly: a finance memory-poisoning study (poisoned reflections that persist across trading days) does not appear to exist yet. Attack success and dollar impact are decoupled, which is a useful metric lesson.

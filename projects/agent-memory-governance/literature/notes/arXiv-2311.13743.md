# FinMem: LLM trading agent with layered memory and character design (arXiv:2311.13743)
Read: full text (ar5iv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core. Also published in AAAI Spring Symposium proceedings (doi:10.1609/aaaiss.v3i1.31290, per SciSpace).

- **Memory.** Three long-term layers keyed to information half-life: shallow = daily news (Q=14 days), intermediate = 10-Q (Q=90), deep = 10-K plus extended reflections (Q=365). Retrieval score = recency (exp(-δ/Q_l)) + relevancy (embedding cosine) + importance (base 40/60/80 with a layer-specific degradation). Reflections promote critical events to deeper layers. In training, the agent sees next-day prices to learn news-to-price links; in testing it does not.
- **Data.** TSLA, NFLX, AMZN, MSFT, COIN; train Aug 2021–Oct 2022, test Oct 2022–Apr 2023.
- **Results.** TSLA cumulative return 61.78% vs 33.34% (DQN, best baseline); Sharpe 2.68 vs 0.97. Gains on NFLX are marginal (36.45% vs 35.51% buy-and-hold).
- **Limitations.** Single stocks; short test window; sensitive to top-K; degrades in volatile downturns.
- **Critique.** This is the foundational finance-memory design. Its memory is **market knowledge, not client data**, so the governance issues are provenance, staleness and look-ahead leakage (training uses future prices, and LLM pretraining overlaps the test period; see arXiv:2605.28359 on memorisation contamination). There is no access control, deletion or audit. Decay-by-layer is an interesting precedent for retention schedules.

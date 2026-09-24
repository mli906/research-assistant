# Sell Me This Stock: unsafe recommendation drift in LLM agents (arXiv:2603.12564)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core.

- **Problem.** In multi-turn advisory, manipulated tool data pushes recommendations outside the client's risk profile, and standard metrics (NDCG) do not notice ("evaluation blindness").
- **Setup.** 23-turn advisory dialogues replayed from Conv-FinRe (arXiv:2602.16990); 8 models (Qwen2.5-7B up to frontier). The agent keeps a **4-field structured memory**: risk tolerance, goals, constraints, last 5 decisions, updated via validated JSON. Attacks: risk-score inversion, metric scaling, biased headlines.
- **Results.** NDCG stays ~1.0 while suitability violations occur in 65–99% of turns. 80% of risk-score citations reproduce the manipulated value. **95% of violations come from current-turn contamination, not from memory.** Self-verification cuts violations 71% on clean data but fails under contamination. A parametric cross-check detects 99–100% of the contamination on Sonnet, yet the agent still recommends the unsafe stocks. SAE steering recovers <6%.
- **Limitations.** 10-ticker universe; simple memory; hardcoded tools.
- **Release.** Code and data tarballs; license CC BY-NC-ND 4.0 (restricts derivatives, so check before building on it).
- **Critique.** This is a strong "suitability as a metric" template (MiFID II Art. 25 / Reg BI style). Memory is a small factor here, so the open question is persistence: does contamination written into memory carry over to later sessions? That is the governance-relevant extension.

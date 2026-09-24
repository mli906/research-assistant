# Conv-FinRe: conversational and longitudinal benchmark for utility-grounded financial recommendation (arXiv:2602.16990)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core. TheFinAI group.

- **Data.** 10 human participants. Onboarding questionnaire follows **MiFID II Art. 25 suitability** guidance. A 30-day trading simulation on 10 S&P 500 stocks (Aug–Sep 2025 prices); advisory dialogues are synthesised from real decision trajectories. 230 prefix-conditioned instances; conversations of 4–26 turns.
- **Tasks and metrics.** Stock ranking judged against 4 views (user choice, rational utility from inverse-optimised risk parameters, momentum, risk sensitivity): uNDCG, MRR/HR@K, expert alignment (Kendall τ).
- **License.** CC BY 4.0; HF collection TheFinAI/conv-finre; GitHub The-FinAI/Conv-FinRe.
- **Critique.** This is the substrate used by arXiv:2603.12564. It is valuable because the client profile is grounded in a suitability questionnaire, which gives a legally meaningful reference for "what the agent should remember". It is very small (10 users) and within-session only. It could be extended into multi-session, multi-client suitability-memory tests.

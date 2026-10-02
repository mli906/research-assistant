# Project state

- **Stage:** 1 - lit review done (2026-10-01); next `/find-gaps`
- **Last updated:** 2026-10-01
- **last_radar:**

## PI research taste
- Thinks in four pillars: representation of state, incomplete observation, dynamics, use.
- Prefers starting from a narrow, well-defined problem; sees problem definition as the hard part.
- Cares about practical finance use cases (scenarios, firm fundamentals, supply chain) and data realism.

## Early scan (2026-10-01, 56 records tagged `scan`: arXiv since 2026-04-01 + SciSpace; abstracts only)
1. ~~No finance-specific JEPA found~~ **Superseded by review:** ICML 2026 poster (Mahns/Balestriero/Assran) learns a JEPA market-state embedding for US equities; also Fin-JEPA (SSRN). See literature/review.md §1.
2. JEPA for time series is contested: arXiv:2609.31680 finds gains vary by backbone (some degrade); arXiv:2609.25541 finds a JEPA term trails value-only training on 147 tabular datasets. Positive: HEPA arXiv:2605.11130 (incl. volatility regimes) and Distributed JEPA arXiv:2609.17029 (robust to missing data).
3. Action-conditioned JEPA world models are exploding (≈25 hits in 6 months, mostly robotics/driving); theory now exists on generalization (arXiv:2606.27014) and causal-state identifiability (arXiv:2609.31161), directly relevant to the counterfactual pillar.
4. Partial observability: UWM-JEPA arXiv:2605.25313 carries belief over hidden state in rollouts; matches pillar 2.
5. Evaluation: FinStressTS arXiv:2606.03184 is a synthetic finance benchmark with known mechanisms, a candidate for controlled tests where real data only shows one path.

## Next step
1. PI reads review.md (esp. §1, §5 wedge table, §10 challenges, §11 gaps) and the ICML 2026 paper.
2. `/find-gaps jepa-finance-world-model`; must check every gap against the ICML paper's full text (OpenReview BZfkxSasd3).
3. Re-run `/radar` when arXiv API recovers (frontier sweep incomplete).

## Open questions for the PI
- Compute budget: estimate to be produced after the review (checkpoint 3 before any GPU spend).
- Which academic subscriptions exactly (WRDS modules, Bloomberg/Refinitiv), and any alt-data vendors already licensed?

- Wedge preference after the review: (b) firm-fundamentals nowcasting/imputation (scout recommendation), (a) macro with identified shocks, or (c) supply chain?
- Which WRDS modules exactly (Compustat Snapshot for point-in-time?)

## Decisions log
| Date | Decision | By | Rationale |
|------|----------|----|-----------|
| 2026-10-01 | Project created: JEPA world model for finance | PI | New direction in AI-in-finance |
| 2026-10-01 | Target: finance-AI venue (ICAIF/KDD-type); wedge decided by the review | PI | Use case and evaluation matter most; keep options open |
| 2026-10-01 | Data: public + academic subscriptions + alt data + proprietary (with approval; never sole basis) | PI | Breadth of access; reproducibility |
| 2026-10-01 | Compute undetermined; budget estimate after review | PI | Depends on chosen wedge and model size |
| 2026-10-01 | Brief confirmed. Start tabular/time-series; multi-modal (SEC filings + internal docs: text, tables, figures) as later extension | PI | Prove JEPA beats strong tabular/TS baselines before paying multi-modal cost |
| 2026-10-01 | No PI materials for inputs/ yet | PI | — |
| 2026-10-01 | Lit review done: 427 records, review.md + partials (methods, finance, eval-data) + industry.md, 35 notes | assistant (3 lit-scouts) | Spot-check of 5 claims: DSGE-Gym '100x' corrected to ~40x; SPLICE extraction numbers not in abstract; others supported |
| 2026-10-01 | Finance-JEPA prior work exists (ICML 2026 market-state JEPA); claims of 'first JEPA for finance' ruled out | assistant | Found by finance scout, verified on ICML page |

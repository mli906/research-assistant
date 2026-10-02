# Project state

- **Stage:** 2 - gaps done; PI chose G1, G5, G3 (2026-10-01); next `/ideate`
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
1. `/ideate` on G1 (firm-statement PIT benchmark, G2 merged as arm), G5 (supply-chain + disaster natural experiments, K5 revived), G3 (identified-shock macro diagnostic). Ideas must assume free SEC XBRL as-filed data until WRDS/Revere access is confirmed; G5 ideas need a public-data fallback (Compustat Segments / SEC customer disclosures).
2. Ideation should include a cheap pilot that decides the framing (JEPA-as-method vs benchmark-with-JEPA-arm), e.g. G1 step 0 headroom test + small JEPA vs value-objective comparison.
3. Re-run `/radar` with short arXiv queries.

## Open questions for the PI
- Compute budget: estimate to be produced after the review (checkpoint 3 before any GPU spend).
- Which academic subscriptions exactly (WRDS modules, Bloomberg/Refinitiv), and any alt-data vendors already licensed?

- Data access (PI checking): WRDS modules (Compustat Snapshot, CRSP, I/B/E/S, Segments), FactSet Revere. Until confirmed, design on free SEC XBRL as-filed data.

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
| 2026-10-01 | Keep all three use cases (macro scenarios, firm fundamentals, supply chain) open for gap analysis | PI | Decide after gaps |
| 2026-10-01 | Gap analysis done. ICML 2026 paper read in FULL TEXT (PMLR 306 PDF via Lacuna mirror; note `notes/icml2026-mahns-latent-market-states.md`); Fin-JEPA full text (author LaTeX). New closest prior for (b): Forma/ProForma-20Q arXiv:2608.11327 (ICAIF '26 companion). Ranked: G1 latent-vs-value objective on firm statements under point-in-time structured masks (b); G3 identified-shock action conditioning + LP/Proxy-DFM + DSGE-Gym (a); G2 cross-frequency market→fundamentals nowcast (b); G4 honest scaled market-state JEPA eval (pilot); G5 network firm state + natural experiments (c). 11 candidates killed/merged. +36 papers tagged `gaps-check` | assistant (gap-analyst) | See gaps.md §4; awaiting PI choice (checkpoint 2) |
| 2026-10-01 | Tool note: `lit.py arxiv` ANDs all tokens, so long queries return empty (looked like rate limiting); short 2-3 term queries work | assistant | Use short queries |
| 2026-10-01 | Adversarial pass on top 5 gaps: G1 survives narrowed; G2 weakened, merge into G1; G3 weakened, diagnostic only; G4 weakened, pilot only; G5 survives narrowed if link data; K5 revived inside G5. Realistic deliverable = benchmark/diagnostic paper with a JEPA arm | assistant (reviewer) | reviews/gaps-adversarial.md; folded into gaps.md |
| 2026-10-01 | Checkpoint 2: pursue G1, G5, G3 into ideation | PI | All three use cases represented |
| 2026-10-01 | Framing (JEPA-as-method vs benchmark-with-JEPA-arm) to be decided after a pilot | PI | Reviewer's cross-cutting objection; wants evidence first |
| 2026-10-01 | Data access unknown; default to free SEC XBRL as-filed | PI | PI to check WRDS/Revere entitlements |

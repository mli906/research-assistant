# FinVerse: financial time-series benchmark (arXiv:2608.03259)
Aug 2026. Read: arXiv HTML via summarising fetch tool (2026-10-01).
- **Scale:** 116,897 series / 171.1M observations (daily to annual) across FX, commodities, crypto, indices, fixed income, macro indicators, equities, ETFs and firm fundamentals; evaluation set 60,232 target series (17.4M obs, 75 category-frequency units) from 2020-01-01; training 66,134 series (100.3M obs) pre-2020.
- **Evaluation:** three lenses (point-wise hit-ratio/MASE; cross-sectional IC; portfolio backtest with equal-weight long-only top 10%); 11 metric families, 78 metrics; 43 TSFMs.
- **Findings:** FinVerse ranks correlate only r=0.40 with GIFT-Eval; model size weakly related to performance. Top: Reverso Small overall, TiRex 1.1 point-wise, Chronos-2 Synth portfolio.
- **Limits (authors):** weekly/monthly/quarterly series normalised to standard periods, not reporting calendars; some indicators timestamped at measurement rather than release date (point-in-time leakage); US-centric; simple portfolio rule.
- **Use for us:** largest finance TS evaluation bed with a train-before-2020 / test-after-2020 split, usable as a baseline arena; but it does not fix release-date leakage, so macro/fundamental series from it should not be used for nowcasting claims without ALFRED/EDGAR re-timestamping. Confidence: medium.

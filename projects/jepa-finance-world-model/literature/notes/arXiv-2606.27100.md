# Pretrained Time-Series Foundation Models for Financial Return Forecasting (Noguer i Alonso, Pereira Franklin) - arXiv:2606.27100

Read: full text via arXiv HTML through WebFetch (summariser-extracted). Accessed 2026-10-01. Frontier (June 2026).

**Method.** Zero-shot TimeGPT/TimeGPT-LH, TimesFM-2.5, Moirai-2.0, Chronos, Chronos-2 vs per-ticker NBEATS, NHITS, PatchTST, iTransformer, KAN on five US equities (AAPL, AMZN, GOOG, JPM, META), daily adjusted close 2014-09 to 2026-02; eval 2024-08-22 to 2026-02; H=20, L=512; rolling-origin, 10 windows; MAE, skill vs zero-return random walk, DM test (HLN).
**Results.** Pretrained TSFMs take 8 of 10 task-level wins (Moirai-2.0, TimesFM-2.5 best average rank); iTransformer wins META. Skill scores ~1e-3; only 2 DM rejections (Chronos/AMZN, Moirai-2.0/GOOG). Authors: gains "small and sparse"; an information-theoretic bound puts exploitable signal in daily returns near 0.5%.
**Critique.** Five mega-cap stocks, one 18-month test period, MAE (not aligned with MSE training), no pretraining-contamination analysis (TimesFM/TimeGPT corpora overlap with test dates is possible). Contradicts the sign of Rahimikia et al. (arXiv:2511.18578) on zero-shot value; difference is MAE vs R2_OOS and per-ticker vs cross-section: the two papers are not comparable. Confidence in "TSFMs help on returns": low.

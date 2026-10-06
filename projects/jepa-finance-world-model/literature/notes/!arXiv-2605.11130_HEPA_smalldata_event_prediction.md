# arXiv:2605.11130 HEPA: Horizon-Conditioned Event Predictive Architecture for Time Series
Read: HTML full text via WebFetch extraction (2026-10-01).
- **Method:** causal Transformer encoder (d=256, 2 layers, 4 heads, patch 16, instance norm), horizon-conditioned MLP predictor, linear event head. JEPA pretraining with SIGReg (alpha=0.1), no EMA. Per-dataset pretraining, under 1 min on one A10G.
- **Data:** 14 benchmarks over 11 domains (C-MAPSS turbofan, spacecraft telemetry, cardiac, cyberattack, TEP, power, climate, air quality, **VIX volatility regimes**, ...). Small scale, per-dataset.
- **Results (h-AUROC):** wins 10/14 at 100% labels; matches or exceeds Chronos-2 on most; loses to iTransformer on MBA (0.75 vs 0.84) and to MAE on SMAP/ETTm1. Label efficiency: 92% of full-label h-AUROC with 2 of 85 engines on C-MAPSS-1; at 10% labels wins 6/14.
- **Limitations (authors):** weak on sensor-localised events; theory bound vacuous when events lack extended precursors.
- **Critique/relevance:** closest published evidence that JEPA+SIGReg is cheap and label-efficient on small time-series data, includes a financial regime-event task (VIX). Event prediction, not full-state dynamics. Self-reported; the exact VIX protocol and leakage controls unknown.

# arXiv:2511.09783 Koopman Invariants as Drivers of Emergent Time-Series Clustering in JEPAs (AAAI)
Read: HTML full text via WebFetch extraction (2026-10-01).
- **Claim:** idealised JEPA loss (linear predictor g(z)=Mz, EMA target approx = online encoder, data = finite mixture of ergodic regimes) is minimised when the encoder represents regime indicator functions = Koopman eigenfunctions with eigenvalue 1; M must act as identity.
- **Evidence:** synthetic, 18 regimes (sinusoids, AR/MA, trends, pulses), 180,000 context-target pairs, context 768, horizon 256. JEPA K-means cluster purity 65.48% vs 38.81% for comparable autoencoder; M within 2.34% Frobenius of identity.
- **Limitations (authors):** linear predictor; EMA not analysed; synthetic with immiscible regimes; gradual/hierarchical regimes outside theory.
- **Relevance:** gives a mechanism for *why* a JEPA might encode market regimes (volatility/macro regimes) and what it ignores (within-regime variation, i.e. what many finance tasks need). Purity 65% on synthetic data with known regimes is modest. Interpretation for finance is speculation.

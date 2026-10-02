# Mahns, Balestriero, Assran (2026). Joint-Embedding Predictive Learning of Latent Market States in U.S. Equities. ICML 2026 (PMLR 306), poster.

**Read: FULL TEXT, 22 pages incl. appendices A-E** (2026-10-01). OpenReview (https://openreview.net/forum?id=BZfkxSasd3) blocks scripted access with a browser challenge, and PMLR 306 is not online yet. The PDF was obtained from the Lacuna index (https://lacuna.tiptreesystems.com/pdf/art_e2656409e671b9dc25ec927512a47764). Its header reads "Proceedings of the 43rd International Conference on Machine Learning, Seoul, South Korea. PMLR 306, 2026", so it is the camera-ready version. Text was extracted with pypdf; check numbers against the PDF before quoting them in a paper.
**Library status:** no arXiv id or DOI found (arXiv API author search "Mahns" returned nothing; WebSearch found no preprint). Not in `papers.jsonl` because `lit.py` cannot fetch OpenReview ids. Cite as the ICML poster URL until PMLR 306 is published, then `lit.py fetch` the PMLR DOI/URL.
**Affiliations:** Johns Hopkins (Mahns), Brown (Balestriero), Mila/Meta (Assran).

## What it does
- **Data.** Daily OHLCV from Massive.com (commercial vendor, formerly Polygon). NYSE/NASDAQ/NYSE American, **top 512 equities by average dollar volume**, chosen on the training period only and then frozen (never rebalanced). Raw data Oct 2017-Oct 2025 (2,010 trading days). Splits: **train 2018-2022, val 2023, test 2024-2025** (451 raw test days; n=365 for some probes). Split-adjusted **price returns, no dividends**. Between 480 and 512 assets are active per day; missing assets get a validity mask. Normalisation statistics come from training data only.
- **Features.** F=28 per equity (Table 7): returns and horizon structure, realised and EWMA volatility, candle geometry, volume and liquidity, market-relative quantities. All are trailing-window values computed only from information available up to day t.
- **Tokenizer.** Set Transformer (row-wise MLP → 2 ISAB blocks with m=32 inducing points → PMA with K=24 seeds → SAB). It maps each day's unordered cross-section to **K=24 "factor tokens", d=128**. It is permutation-invariant, and missing assets are handled through attention masks. It is trained jointly with the JEPA and is not part of the EMA target.
- **Temporal JEPA.** Clips of L=21 days over an L×K time-token grid. Context encoder and predictor are 6-layer transformers with 4 heads (predictor hidden width 64). The target encoder is an EMA copy (0.996→0.9999). Positional encoding uses **lag-aware Fourier features of calendar distance** plus a slot embedding. A **multi-stride curriculum** s∈{1,3,7,21} gives horizons of 20/60/140/420 trading days.
- **Masking.** Contiguous in time and random over slots, mixing time-span×slot masks, full-day masks and full-slot masks. Minimum visible ratio 0.3; "causal masking probability 0.3".
- **Loss.** ℓ1 on LayerNorm'd target embeddings at masked tokens. Anti-collapse comes only from EMA plus stop-gradient (no SIGReg/VICReg).
- **State.** z_t is the mean-pooled final-timestep tokens, z_t ∈ R^128.
- **Compute.** 1×H100, 200 epochs, ~12 h, ~20 GB peak memory. Small.

## Evaluation (7 tests; all probes are linear: ridge or logistic)
1. **kNN retrieval** (k=20, ±21-day exclusion): Spearman ρ of 0.78 for RV21, 0.68 for PC1 share and 0.11 for market return.
2. **Linear probes, contemporaneous:** R² of 0.42 for corr_mean, 0.45 for pc1_share and 0.36 for eff_rank.
3. **Mantel test** of latent distance against correlation-matrix distance (gap ≥63 days): JEPA 0.35 [0.16, 0.54], **vol-only baseline 0.44**, time-only baseline −0.10, spectrum oracle 0.68. *A volatility-only baseline beats JEPA here.*
4. **Transition prediction** (will a geometry metric rise above the 90th-percentile change over the next 21 days; 21-day purge). Baselines: an 18-feature handcrafted persistence set, HAR, a Gaussian HMM, and a capacity-matched MAE. Table 17: JEPA's only clear gain is recovery eff_rank UP (AUC 0.690→0.800, AP 0.139→0.324). Stress corr_mean UP gets AUC +0.12 but AP only +0.008. **Adding JEPA hurts** recovery pc1_share DOWN (AP 0.837→0.360) and recovery corr_mean DOWN (AP −0.136).
5. **Displacement δ_t = ||z_t − z_{t−1}||:** large on crash and VIX-spike days (Cohen's d 0.92-1.47) and **not on FOMC days (N=66, p=.63) or CPI days (N=89, p=.79)**. Its top-1% enrichment ties |SPX return| at 14.96×. **Added to a standard risk bundle, the gain is not significant** (ΔAUC −0.002 [−.006, .003]). Appendix D.2: displacement is "contemporaneous rather than anticipatory".
6. **HMM regime probe:** JEPA accuracy 0.633 vs 0.895 from the observables themselves.
7. **Cross-modal check with GDELT news topics:** Δ(252)=0.0069 [0.0015, 0.0131] on train+val and 0.0077 on test. Small absolute effects.
8. **Ablations.** JEPA beats MAE on every structure descriptor (kNN R² mean 0.34 vs 0.25). Structured masking leaks less direction than random masking (direction ρ 0.14 vs 0.19). Retraining with the 8 explicit volatility inputs removed lowers Mantel to 0.32 and halves the recovery AUC gain (+0.24→+0.14), but both effects persist.

## What it does NOT do (checked against the full text)
- **No forecasting of the state.** No decoded multi-step forecast of volatility or correlation, and no comparison of state forecasts with HAR/DCC/GARCH. HAR serves only as a reference for transition classification.
- **No TSFM baselines** (Chronos, TimesFM, Moirai, Kronos), no tabular FMs and no SIGReg/LeJEPA variant. The learned baseline is MAE only.
- **No firm-level or entity-level states.** The state is a single market-level vector per day, and per-firm token outputs are never evaluated.
- **No fundamentals, macro series, mixed frequency or irregular inputs.** Daily OHLCV only.
- **Partial observability is engineering, not a study.** Missing assets are masked; there is no experiment on how robust the state is to missing data or on inferring unobserved entities.
- **No action conditioning, no counterfactuals, no identified shocks.** FOMC and CPI are used only as event labels, and the embedding does not respond to them.
- **No generative or scenario component** and no uncertainty quantification.
- **One market, one era (2018-2025), one universe (top-512 ADV), one split.** No multi-seed variance is reported (pypdf text search found no seed study; L confidence on that absence).
- **No data-size scaling study.** Raw train ≈1,250 days.

## Stated limitations and future work (verbatim, full text)
- Scope: "Relative to established econometric and handcrafted descriptors, the embedding is *complementary rather than uniformly superior*."
- Data: "the top-ADV filter excludes less liquid securities, limiting conclusions to highly traded equities." "we evaluate only U.S. equities from 2018–2025 ... We leave exploration of generalization to other markets or eras for future work."
- §5.1 Forecasting/counterfactual: "Exploring the possibility of such counterfactual prediction using latent representations of the equities and high-level labels—such as news headlines or sentiment signals derived from prediction markets—is a natural extension of this work. In this setting, alternative policy decisions or information shocks can be treated as interventions on the latent action space, enabling 'what-if' analyses of market dynamics without requiring explicit reconstruction in input space."
- §5.1 Scaling: "Computational constraints limited our exploration of larger or more advanced tokenizers, deeper encoders, more complex stride curricula, ablations across features, higher-fidelity or denser data, and longer context windows." "we primarily utilize ridge/logistic regression, nonlinear decoders might recover more signal."
- §5.1 Interpretability: "there are economically meaningful periods in which correlation structure shifts without large changes in volatility (e.g., sectoral rotations or factor crowding). A natural extension is to ... design objectives that emphasize changes in correlation shape conditional on volatility."
- Impact statement: "The method is descriptive rather than predictive"; "not designed to detect or anticipate abrupt market stress".

## Implications for this project
- **This paper occupies** "JEPA market-state embedding from equity cross-sections, evaluated by probes." Anything at that level, such as a regime embedding or a displacement stress indicator, is incremental unless it adds forecasting, actions or entities.
- **The authors flag action-conditioned counterfactuals as their own next step.** Expect competition from a well-resourced group on "action-conditioned market JEPA". Their framing (news or prediction-market labels as interventions) has **no identification argument**. That is where we can differentiate: identified monetary shocks with LP/VAR validation.
- **Useful negative evidence.** The state does not move on FOMC or CPI days, which means raw announcement-day "actions" are invisible to a price-only market state. Surprise magnitudes (Bauer-Swanson / Jarocinski-Karadi) or macro inputs are probably needed.
- **Reusable design pieces:** set tokenizer with validity masks (relevant to firm panels with missing firms), lag-aware Fourier time encoding (relevant to irregular timestamps), and a multi-stride curriculum.
- **Honest-evaluation precedent.** Even this strong group reports that JEPA is "complementary rather than uniformly superior", loses to a vol-only baseline on Mantel, and adds nothing over a risk bundle. That lowers the bar for what counts as a publishable honest result and confirms the "JEPA doesn't beat simple baselines" risk.

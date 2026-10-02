# Gap analysis: JEPA world models for finance

Project `jepa-finance-world-model`. Written 2026-10-01 by the gap-analyst agent at stage 2 (`/find-gaps`).

**Inputs read:** `brief.md`, `STATE.md`, `literature/review.md`, the `partials/finance.md` partial, `industry.md` (via review), all relevant `notes/`, and `inputs/INDEX.md` (empty: no PI materials).

**Library:** 455 records, of which 36 are new and tagged `gaps-check`. All were added through `lit.py fetch | add`; no metadata was typed by hand.

## How to read this file

**Reading-depth labels**
- **FT**: I read the full text myself from the PDF via pypdf on 2026-10-01. Quotes are verbatim.
- **FT-ext**: full text read earlier through a WebFetch summariser (an existing note). Numbers in these need a PDF check.
- **abs**: abstract only (weak evidence).
- **web**: web page only; the item is not in the library.

**Confidence labels:** H/M/L. Every gap carries two separate ratings:
- *open*: nobody has done it.
- *payoff*: doing it will produce a result worth publishing.

**Gap template.** Each gap gives:
1. Statement
2. Evidence
3. Assumption challenged
4. Falsifier (what would show the gap is not real)
5. Why it matters
6. Closest prior work and how it differs
7. Search log and whether anyone is on it
8. Feasibility
9. First pilot
10. Risks
11. Confidence

---

## 0. What changed since `review.md` (read this first)

### 0.1 The closest prior work has now been read in full
**ICML 2026 paper** (Mahns, Balestriero, Assran). PMLR 306, camera-ready, 22 pp.
- Note: `literature/notes/icml2026-mahns-latent-market-states.md`.
- OpenReview blocks scripted access, but the PDF was available through the Lacuna index.
- It has no arXiv or DOI version, so it is cited by URL. The facts below come from the full text.

**What it does**
- Data: top-512 US equities by average dollar volume, daily OHLCV, 2018-2025. Train 2018-22, val 2023, test 2024-25. Price returns only.
- Model: a Set-Transformer tokenizer (K=24 factor tokens) feeds a temporal V-JEPA-style encoder (EMA target, ℓ1 loss, block masks over a time×slot grid, multi-stride curriculum). It is trained on 1×H100 for about 12 h.

**What it finds**
- The embedding encodes second-moment "risk geometry".
- Linear probes give R² of 0.36-0.45 on correlation geometry.
- Retrieval ρ is 0.78 for realised volatility and 0.11 for market direction.
- **A volatility-only baseline beats JEPA on the Mantel geometry test** (0.44 vs 0.35).
- JEPA adds value only for "diversification recovery" (AUC 0.690→0.800).
- It *hurts* two of four transition tasks (AP 0.837→0.360 on pc1_share DOWN).
- Embedding displacement adds nothing over a standard risk bundle (ΔAUC −0.002 [−.006, .003]).
- **The state does not move on FOMC days (p=.63) or CPI days (p=.79)** (Table 3).

**What it does not do**
- No forecasting of the state.
- No TSFM or tabular-FM baselines.
- No firm-level states, no fundamentals, no macro inputs, no mixed frequency.
- No action-conditioning and no scenarios.
- One universe, one era, one split.

**Stated limitations and future work (verbatim, FT)**
- "the embedding is complementary rather than uniformly superior".
- "the top-ADV filter excludes less liquid securities".
- "We leave exploration of generalization to other markets or eras for future work."
- "Computational constraints limited our exploration of larger or more advanced tokenizers ... higher-fidelity or denser data, and longer context windows".
- Their future work names **action-conditioned counterfactuals**, with "news headlines or sentiment signals derived from prediction markets" serving as "interventions on the latent action space".

**Consequence.** The authors have publicly staked out action-conditioned market JEPAs. This is a competition risk for any gap at the *market-state* level.

### 0.2 Fin-JEPA has now been read in full
- Source: the author's LaTeX in the GitHub repo; the note is updated.
- Setup: per-stock (not cross-sectional) daily technical features, SIGReg. The **only baseline is identity** (+10.1% latent MSE).
- Return signal is null (AUC ≈ 0.49-0.50).
- Verbatim: "Baseline comparisons ... PCA-64, LSTM autoencoder, VAE, and TS2Vec ... These experiments have not been run."
- It occupies none of the gaps below.

### 0.3 A strong new closest-prior for use case (b): Forma
**Forma / ProForma-20Q** (arXiv:2608.11327, FT, Aug 2026; companion to an ICAIF '26 paper per its GitHub README, web).
- **Model:** a ~0.9M-parameter tuple-set transformer over (account, quarter, value) tokens. Training uses a **masked-tuple Gaussian likelihood** (a value-space, reconstructive objective) with identity-aware grouped masking.
- **Task:** forecasts 78 Compustat line items 1-20 quarters ahead. It beats elastic net, random forests, FFNNs, chained GBMs, a zero-shot TSFM and frontier LLMs.
- **Compute:** about 16.5 A100-hours per seed.

**Its stated limitations (FT, verbatim)**
- "We do not incorporate stock market or analyst data as additional features".
- Results are scoped to "quarterly U.S. filings, these 78 accounting items, and horizons of 1–20 quarters".
- "Long-horizon evaluation conditions on realized survivors".

**What it does not do**
- It uses `comp.fundq`, not as-filed point-in-time data.
- It is a **forecasting** benchmark, not a partial-observation or nowcasting benchmark.

**Why it matters here.** Any firm-fundamentals JEPA must beat Forma. Forma also gives the cleanest available JEPA test: the *same* architecture with a latent objective instead of a value objective.

**Licence.** The weights are released under a non-commercial licence (web, GitHub README). This matters for an industry-affiliated PI (see Questions for the PI).

### 0.4 Other new closest-priors found by the novelty searches
| Id | What it does | Read | Relevance |
|---|---|---|---|
| arXiv:2609.32741 | Heterogeneous-graph patch transformer forecasting the quarterly fundamentals of semiconductor firms from a 15,186-firm supply-chain graph. Supervised; "preliminary experiments on 116 focal semiconductor firms" | FT | Closest prior for use case (c) |
| arXiv:2608.07037 | Accounting Graph Transformer: masked ledger tokens on an accounting-relation graph. Intuit, small businesses with 12-24 months of history | FT, skim | Private-firm-like data, supervised |
| arXiv:2607.24410 | CD-DFM: fundamentals → latent → covariance; zero-shot onboarding of unseen assets | FT, skim | Fundamentals-to-risk state |
| arXiv:2411.05791 | Benchmark of 22 models for company-fundamentals forecasting | abs | Baselines |
| doi:10.1145/3604237.3626909 | NMTucker, ICAIF '23 | abs | Shows tensor completion of firm panels is an ICAIF topic |
| arXiv:2508.01861 | ACT-Tensor; SciSpace lists an ICAIF '25 DOI | abs | Same |

### 0.5 Two more negatives read in full
- **arXiv:2207.13071 (Chen-McCoy, FT).** They admit their own random-masking test "can 'cheat'" because "accounting predictors are typically missing together". The mean-imputation ceiling is shown for *return predictors* scored by *portfolio returns*. It does not cover imputing raw fundamentals.
- **arXiv:2609.25541 (tabular JEPA, FT).** One run per arm. Its stated future work (verbatim): "whether the latent term buys robustness rather than accuracy, at short contexts or under noise, is testable". This points JEPA at *heavy, structured missingness*, not clean accuracy.

### 0.6 Tool note
`lit.py arxiv` ANDs every token. Long natural-language queries therefore return **empty output that looks like a rate-limit failure but is not one**. Short queries of 2-3 terms worked all session (about 30 queries logged below).

---

## 1. Map: where the ICML paper sits and where the openings are

| Pillar | (a) Macro scenarios / identified shocks | (b) Firm fundamentals under partial observation | (c) Supply chain / network |
|---|---|---|---|
| **1. Representation** | (ICML: market state from prices only) | **G1**: latent vs value objective on statement tuple-sets | **G5**: network-conditioned firm state |
| **2. Partial observability** | merged into G3 (macro ragged edge) | **G1** (source- and entity-level masks), **G2** (cross-frequency nowcast from market data) | G5 (hidden links) |
| **3. Dynamics / action** | **G3**: identified-shock action conditioning, LP/Proxy-DFM + DSGE-Gym validation | killed: firm counterfactual what-ifs (K5) | G5 (propagation, natural experiments) |
| **4. Use / evaluation** | G6: scenario generator with tail fidelity | G1/G2 evaluation protocol (point-in-time, structured masks) | G5 (event studies) |
| cross-cutting | **G4**: honest market-state JEPA evaluation (scaling, eras, liquidity, forecasting), *closest to the ICML turf* | | |

---

## 2. Gaps

### G1. Latent-space vs value-space self-supervision for firm financial statements under realistic partial observation (use case b; pillars 1, 2, 4)

**1. Statement.** Nobody has tested whether a JEPA (latent-target) objective beats the value-space masked objective that currently wins on firm statements (Forma). The test that matters uses the same tuple-set architecture and the same data, with **point-in-time, source-structured and entity-level masks**. Entity-level masks hide an entire firm's statements: a simulated private firm.

**2. Evidence**
- Forma (arXiv:2608.11327, FT) is value-space only. It uses `comp.fundq` rather than as-filed data, no market data, and forecasting rather than masking-based inference. Its masking is designed to stop the model "learn[ing] accounting algebra" (identity-aware grouped masking). That is the same shortcut problem that JEPA theory describes.
- Chen-McCoy (arXiv:2207.13071, FT): "81% are also missing book-to-market in every previous month"; "about 90% are also missing earnings-to-price". Their random masks "can 'cheat'". So *no published masking benchmark* for firm data respects block or source missingness.
- The tabular JEPA (arXiv:2609.25541, FT) loses to value-only training on iid tables. It names robustness under noise and short context as the open question.
- Theory: "JEPA Learns What the Mask Leaves Unrecoverable" (arXiv:2609.32481, abs) says JEPA helps only when the masked target cannot be recovered by low-level priors (persistence, identities). The idealised Koopman view says JEPA encodes regime indicators (arXiv:2511.09783, FT-ext).
- Retaining the JEPA predictor as a "partial-view operator" closes the gap at heavy masking (arXiv:2607.16274, abs).

**3. Assumption challenged.**
- In finance ML: "missing fundamentals are best handled by mean or last-value imputation". That is true for return predictors, but untested for statement inference with own-history and market context.
- In JEPA work: "latent prediction is preferable when inputs are noisy". The three 2026 time-series and tabular evaluations contradict it.

**4. Falsifier.** Either of these would show the gap is not real:
- (i) A paper that already trains a latent-target (non-reconstructive) objective on firm statement panels and evaluates it under structured masks.
- (ii) Evidence that structured-mask headroom is nil. Example: Last-Observed plus industry-size means come within noise of the best value-space model on entity-level masks. The gap would then exist but be empty, and the pilot step 0 below tests exactly this.

**5. Why it matters**
- *Practitioners:* private-firm and credit analysis, KYC, supplier risk, and data vendors filling holes all need statement estimates when disclosure is missing or late. The PI's case (b) is exactly this.
- *ML:* this is the first clean, matched-architecture test of the JEPA-vs-reconstruction hypothesis in a domain whose structure is known (exact accounting identities plus soft latent economics). It speaks directly to the open question raised by arXiv:2609.31680 and arXiv:2609.25541.

**6. Closest prior and the difference**
- Forma: value-space; forecasting rather than partial observation; not point-in-time.
- ACT-Tensor (arXiv:2508.01861) and NMTucker (doi:10.1145/3604237.3626909): tensor completion of characteristics with random masks (abs).
- BLLP (doi:10.1093/rfs/hhae036): latent-factor imputer (abs).
- AGT (arXiv:2608.07037): supervised forecasting, small businesses.
- CUBAN (doi:10.1109/bigdata62323.2024.10825106) and Buckmann et al. (arXiv:2505.08662): text or LLM-hidden-state estimates of firm values (abs).
- None uses a latent-target objective, and none evaluates under source- or entity-structured, point-in-time masks.

**7. Search log** (2026-10-01)
- SciSpace: "self-supervised or masked latent models impute or nowcast missing firm-level accounting fundamentals" → NMTucker, ACT-Tensor, Forecasting Company Fundamentals, MICE-for-fundamentals. All are value-space.
- SciSpace: "private company revenue from alternative data" → Fleder-Shah (doi:10.1145/3366694), AMS, CUBAN. None is latent-target.
- arXiv since 2025-10-01: "imputation fundamentals", "missing firm characteristics" (0 hits), "company fundamentals forecasting", "financial statement forecasting" (→ Forma, AGT), "masked modeling financial panel", "JEPA forecasting".
- Date-sorted JEPA sweep since 2026-07-01 (200 titles): no finance or tabular-panel JEPA beyond arXiv:2609.25541.
- WebSearch: "JEPA financial statements OR company fundamentals" → nothing.
- *Anyone on it?* Not visible. The risk is the Forma group (UT Austin), which could swap its objective at any time; their paper does not mention JEPA. **Open: H.**

**8. Feasibility**
- *Data:* ProForma-20Q rebuilds from WRDS with one command (needs the PI's WRDS Compustat). Public fallback: SEC Financial Statement Data Sets (as-filed, 2009+, free), which also give true filing timestamps and avoid restatement leakage.
- *Compute:* Forma costs about 16.5 A100-h per seed. A JEPA arm plus a value arm, 3 seeds each at 3 data sizes, comes to roughly 300 GPU-h at full scale. A 10%-scale pilot needs about 30 GPU-h.
- *Code:* Forma and ProForma-20Q code are public (web). The weights are non-commercial.

**9. First pilot (two steps; step 0 needs no GPU)**
- **Step 0, headroom test (CPU, about 1 week).** On as-filed SEC FSDS or Compustat, build three mask regimes:
  - random cell;
  - source-block (a whole statement for a firm-quarter);
  - entity-level (all of a firm's statements, with peers and industry visible).

  Score cross-sectional mean, Last-Observed, industry-size mean, a BLLP-style factor imputer, TabPFN/TabICL, and Forma's released model (research use only) by change-space R² and CRPS. *Decision rule:* if no learned model beats Last-Observed plus industry means by a pre-set margin on entity-level masks, drop the entity-level arm.
- **Step 1, matched objective swap.** Use the Forma architecture with a JEPA objective (EMA target or SIGReg) and a probe or decoder head, against the value objective. Match tokens, steps and seeds; use 3 data fractions; pre-register. Include the "retain the predictor" readout (arXiv:2607.16274) and a mask-recoverability score (arXiv:2609.32481) as the mechanism analysis.

**10. Risks**
- **"JEPA doesn't beat simple baselines"** (arXiv:2609.31680, arXiv:2609.25541, arXiv:2609.16071; and in finance itself, ICML's vol-only baseline). Prior probability that JEPA beats the value objective outright: speculation, about 30%.
- *Mitigation:* the paper is built so that the benchmark, the structured-mask protocol and the mechanism analysis (when the latent objective helps, as a function of unrecoverable content) carry it even if the result is null. ICAIF publishes this kind of work (Forma at ICAIF '26).
- **Mean-imputation ceiling** (arXiv:2207.13071): strongest on entity-level masks. Step 0 measures it before any GPU is spent.
- Licence: Compustat cannot be redistributed. A public SEC FSDS arm is needed for reproducibility (brief constraint).

**11. Confidence.** Open: **H**. Payoff: **M** (benchmark plus mechanism: H; a JEPA win: L-M). Tractability for this PI: **H** if WRDS Compustat is available.

---


> **Adversarial review of G1 (reviewer, 2026-10-01; full text in `reviews/gaps-adversarial.md`).**
>
> **Verdict: survives narrowed (M).**
> - **Forma already handles masks.** Forma (arXiv:2608.11327) already supports arbitrary conditioning patterns at inference without retraining. It also excludes market data deliberately, "so that Forma can be applied to private firms", so its authors already claim the private-firm use case.
> - **Fair comparison.** Scoring Forma on structured masks it wasn't trained on would be a straw man. Retrain both arms on the same mask distribution.
> - **Entity-level masks are ill-posed.** With every statement of a firm hidden, the best possible prediction is a peer mean. Replace them with realistic private-firm observation patterns, e.g. revenue only, or revenue plus headcount.
> - **Pure latent objective is risky.** It collapsed on tables (arXiv:2609.25541), so the JEPA arm will in practice be a value-plus-latent hybrid.
> - **Missing "why JEPA here" argument.** Accounting values are exact and the metric is in value space, so the "detail" a JEPA discards is the target.
> - **Narrowing:** lead with the point-in-time structured-mask benchmark. Make JEPA one hypothesis among several.

### G2. Cross-frequency firm state: nowcasting not-yet-filed fundamentals from the daily market cross-section (use case b; pillars 1, 2)

**1. Statement.** No model learns a firm-level state in which the *daily market view* serves as context and the *quarterly fundamentals view* serves as target, and then uses it to nowcast a quarter's statement between quarter-end and the filing date. This is a mixed-frequency, multi-view JEPA in its natural form: the views differ in frequency and modality, and prediction happens in latent space.

**2. Evidence**
- Forma (FT): "We do not incorporate stock market or analyst data as additional features."
- The ICML paper (FT) uses OHLCV only. Its tokenizer pools firms into 24 market tokens; per-firm states are never evaluated, and there are no fundamentals.
- The supply-chain model (arXiv:2609.32741, FT) fuses quarterly fundamentals with monthly macro, but not daily prices.
- CD-DFM (arXiv:2607.24410, FT skim) goes the other way: from fundamentals to a covariance state.
- So the two halves exist separately; the cross-view link does not.

**3. Assumption challenged.** That firm state must come from that firm's own disclosures. Prices aggregate information about unreleased fundamentals. The accounting literature on prices leading earnings is not yet in the library; fetch it before any claim.

**4. Falsifier.** A published learned model that uses daily returns or prices plus statement history to nowcast *full-statement* or multi-item fundamentals before filing, at a point-in-time cut-off.
- *Partial overlap already exists:* ML earnings-surprise and revenue-surprise models with alternative data (AMS, ICDE 2020, via SciSpace, not stored; Fleder-Shah doi:10.1145/3366694, abs).
- The novelty is therefore narrow: a *latent firm state across frequencies* plus point-in-time full-statement nowcasting, scored against analyst consensus. It is not "predict earnings from prices".

**5. Why it matters**
- *Practitioners:* credit and equity analysts nowcast quarters continuously, and analyst consensus is the incumbent. A model that beats consensus on items analysts do not cover (working capital, capex) is directly useful.
- *ML:* a natural test of whether cross-view latent prediction extracts low-SNR cross-frequency signal where reconstruction must model noisy daily returns. The ICML JEPA-vs-MAE result hints yes for second moments.

**6. Closest prior and the difference.** ICML (market-level, prices only); Forma (statements only, no market data); AMS and Fleder-Shah (supervised, single target, alternative data); the I/B/E/S consensus as a practice benchmark.

**7. Search log.**
- arXiv: "nowcasting firm revenue" (0), "earnings nowcasting" (0), "company fundamentals forecasting", "firm panel transformer".
- SciSpace: the two G1 queries above, plus the "private company revenue" query.
- WebSearch: the "JEPA financial statements" query.
- *Anyone on it?* Not found. **Open: M-H.** The accounting and finance literature on ML earnings prediction is large and was not swept exhaustively.

**8. Feasibility.**
- Data: CRSP daily, Compustat quarterly with `rdq` report dates, the CRSP-Compustat link, and I/B/E/S for the baseline. All are WRDS modules that need PI confirmation.
- Public fallback: SEC FSDS filing timestamps plus free daily prices. Survivorship needs care.
- Compute: modest. The set tokenizer from ICML trains in about 12 H100-h.

**9. First pilot.**
- Universe: S&P 1500, 2005-2024.
- For each firm-quarter, nowcast Δrevenue, Δoperating income and Δworking capital at k = 5, 20 and 40 trading days after quarter-end, using only information dated before t.
- Arms: (a) Forma-style history only; (b) + per-firm market path since quarter-end, via cross-view JEPA; (c) + peer cross-section; (d) I/B/E/S consensus.
- Metric: change-space R² by k; DM tests against consensus.

**10. Risks.**
- Consensus is a hard baseline.
- Price information about revenue may be weak relative to earnings.
- Leakage traps: `rdq` versus actual 8-K timing, restatements, and survivorship (the leakage checklist in `partials/eval-data.md` applies).
- The JEPA-null risk is as in G1; the benchmark result still stands.

**11. Confidence.** Open: **M-H**. Payoff: **M**. Tractability: **M** (depends on CRSP, Compustat and I/B/E/S access).

---


> **Adversarial review of G2 (2026-10-01).**
>
> **Verdict: weakened (M-H); merge into G1 as an arm.**
> - **Prior work:** Kamp et al. (ICDMW 2013) already nowcast earnings from stock prices and beat analysts.
> - **ML-vs-analysts literature:** Chen-Cho-Dou-Lev is already in the library. van Binsbergen et al. 2023 now carries an Expression of Concern, after Zhang-Zhu-Linnainmaa 2025 found look-ahead bias.
> - **Leak in the pilot:** a horizon of 40 trading days after quarter-end is past the earnings announcement for most firms. Gate on `rdq`, the announcement date.

### G3. Identified-shock action-conditioning for a macro-financial latent world model, validated against LP/Proxy-DFM impulse responses and off-path in DSGE-Gym (use case a; pillars 3, 4)

**1. Statement.** Every action-conditioned JEPA so far conditions on controllable actions (robots) or on raw labels. None conditions on *econometrically identified* shocks such as high-frequency monetary surprises. None validates its implied responses against local-projection or Proxy-DFM impulse responses. None reports off-path counterfactual error in DSGE-Gym.

**2. Evidence**
- ICML (FT), §5.1 future work: action-conditioning using "news headlines or sentiment signals derived from prediction markets" as "interventions", with no identification argument. Table 3: FOMC p=.63 and CPI p=.79, so announcement *dates* are invisible to a price-only state.
- DSGE-Gym (arXiv:2607.03144, FT-ext) evaluates ridge, MLP, LSTM, Transformer and NextLat. NextLat is a latent-prediction model of the same family as JEPA, so "no JEPA" is narrow (reviewer correction). Its stated limitation: structure versus coverage is "not disentangled".
- Theory, all FT-ext:
  - Identifiability needs "sufficiently diverse" action-induced changes (arXiv:2609.31161).
  - Passive prediction cannot identify counterfactuals (arXiv:2605.01694).
  - Teacher forcing makes actions inert, ‖H1‖/‖H0‖≈0.03 (arXiv:2605.25313).
  - Command-conditioned latents can ignore commands (arXiv:2609.16071).
  - Identifiability of controlled world models also depends on action-excitation margins (arXiv:2607.22430, abs).
- Econometric bar:
  - Proxy-DFM beats Proxy-VAR on non-invertible shocks (arXiv:2307.06145, FT-ext).
  - Shock series: doi:10.1086/723574, doi:10.1257/mac.20180090, doi:10.1257/mac.20130329.
  - Information effect: doi:10.1093/qje/qjy004.
  - Policy-rule counterfactuals hold only within a model family (doi:10.3982/ecta21045, arXiv:2409.09577).
- BISTRO (BIS WP 1337, web) does conditional forecasting on *assumed paths of observed variables*. Per the abstract page, it does not do impulse-response or counterfactual evaluation.

**3. Assumption challenged.** That "what-if" from a learned world model needs either a simulator (Do-JEPA, arXiv:2609.37378) or gives up identification. The middle path is to condition on externally identified shocks and test against the econometric estimates. That turns the claim into a falsifiable "conditional forecast given an identified shock".

**4. Falsifier.**
- (i) The ICML group, or anyone else, posts an action-conditioned financial or macro JEPA validated against LP or VAR impulse responses.
- (ii) Feasibility rather than reality: HFI shock series are too short or weak. About 280 FOMC events since 1988 with small surprise variance means the action-excitation condition (arXiv:2607.22430) fails, and any learned response collapses toward zero, which is the inert-action failure.

**5. Why it matters.**
- *Practitioners:* central banks and banks' scenario teams want shock-conditioned paths for many variables, including the market state. The Fed and ECB still hand-design narrative paths (finance partial §4.2, web).
- *ML:* the first world-model test where the "action" is identified by an external instrument rather than chosen by an agent. It is a clean place to test the action-identifiability theory on real data.

**6. Closest prior and the difference.**
- DSGE-Gym: synthetic, no JEPA.
- ICML: no actions.
- BISTRO: path-conditioning, no impulse-response validation (web).
- Proxy-DFM: linear and factor-based, no learned nonlinear state.
- Goulet Coulombe-Klieber (arXiv:2505.12422, abs): ML impulse responses as proximity-weighted local projections, not world models.
- Neural VAR impulse responses (arXiv 1903.09395, web, not stored).

**7. Search log.**
- SciSpace: "neural network ... impulse responses to identified monetary policy shocks ... vs LP/VAR"; "JEPA or latent world model ... macroeconomic ... vs DFM".
- arXiv since 2025-10: "monetary policy shock neural network" (0), "impulse response deep learning" (no macro hits), "macroeconomic world model", "DSGE world model" (only DSGE-Gym), "counterfactual economic simulator" (Equilibrium World Models arXiv:2606.23463 is a *solver*, not learned from data).
- WebSearch: "action-conditioned world model monetary policy shocks impulse responses".
- *Anyone on it?* Not found, but the ICML authors list action-conditioned market JEPAs as next work. **Open: M-H, and the window may be short.**

**8. Feasibility.**
- Data is all public: FRED-MD with ALFRED vintages; shock series published by the authors; a daily market-state embedding (re-implement ICML on CRSP or free prices); and DSGE-Gym environments (arXiv code).
- Compute: small; the models are about 1M parameters.
- Data size is the binding constraint: about 400 months of macro data.

**9. First pilot (synthetic first, then real).**
- **(A) DSGE-Gym NK/RBC.**
  - Compare an action-conditioned JEPA (latent transition taking the shock as action) with and without counterfactual-coverage training data.
  - Baselines: the benchmark's MLP, LSTM, Transformer and NextLat.
  - Metrics: on-path error, 5σ tail error, and impulse-response recovery against the DSGE oracle.
  - Include the teacher-forcing ablation.
- **(B) Real data.**
  - Rollouts with the shock set to +1 s.d. versus 0, from 1990-2019 states.
  - Compare the implied responses of IP, unemployment, CPI, credit spreads and market-state geometry with LP and Proxy-DFM responses and their bands.
  - Pre-register sign and shape tests.
  - Hold out 2020-2024.

**10. Risks.**
- JEPA-null risk (high here: small n).
- Inert-action risk.
- The information effect contaminates the "action".
- Competition from the ICML group.
- A reviewer may say "just run a Proxy-DFM". The answer is that the latent state carries market geometry and nonlinear state dependence, which needs pre-registration and a state-dependence test.
- Nothing here licenses "what if the rate were 5%". That claim is restricted per McKay-Wolf (doi:10.3982/ecta21045).

**11. Confidence.** Open: **M-H**. Payoff: **M** (DSGE-Gym arm: H publishable as a benchmark entry; real-data impulse-response agreement: L-M). Tractability: **M**.

*Merged into G3:*
- the macro ragged-edge JEPA nowcaster versus a DFM (review gap 2, macro half);
- the "synthetic economy with actions and confounders" (review gap 4).

Reasons are given in §3.

---


> **Adversarial review of G3 (2026-10-01).**
>
> **Verdict: weakened (M); keep only as a diagnostic paper.**
> - **Prior work:** neural networks already learn nonlinear impulse responses to identified shocks (arXiv:2412.07649).
> - **Rank condition:** a single scalar monetary shock cannot meet the action-diversity condition in arXiv:2609.31161.
> - **Weak test:** "agreement with LP bands" has little power to tell models apart.
> - **DSGE-Gym arm:** shocks there are exogenous by construction, so it doesn't test identification.
> - **Overstated claim in this file:** NextLat, a latent-prediction model of the same family as JEPA, is already in DSGE-Gym. So "no JEPA in DSGE-Gym" is technically true but overstated.

### G4. Honest, scaled evaluation of market-state JEPAs: forecasting the state, across eras, liquidity tiers and training sizes, against HAR, TSFM and MAE (cross-cutting; pillars 1, 4)

**1. Statement.** No study tests whether a JEPA market state *forecasts* second-moment quantities (realised volatility, correlation concentration, effective rank) better than HAR, DCC, TSFMs or MAE. No study asks how that depends on training-set size, era (pre-2018, 2008, 2020) or liquidity tier. The ICML paper evaluates description only, on one universe and one split.

**2. Evidence.**
- ICML (FT): "descriptive rather than predictive"; the only learned baseline is MAE; HAR and HMM appear only in classification tasks; "we evaluate only U.S. equities from 2018–2025"; "top-ADV filter excludes less liquid securities"; no seed study found.
- Against JEPA: the vol-only baseline wins on Mantel, and adding JEPA hurts two transition tasks.
- Fin-JEPA (FT): baselines "have not been run".
- Generic negatives: arXiv:2609.31680 (sign flips across backbones, FT-ext); arXiv:2609.16071 (no gain over matched from-scratch training, FT-ext).
- TSFMs versus HAR on realised volatility: no uniform gain; only TTM beats Log-HAR everywhere, narrowly (arXiv:2607.05291, abs).
- FinStressTS: classical models win at low SNR (arXiv:2606.03184, FT-ext).

**3. Assumption challenged.** That a JEPA market embedding which *describes* regimes is also a useful *dynamic state*: predictive, robust across eras, and data-efficient.

**4. Falsifier.** A multi-era, multi-universe evaluation of a JEPA market state against HAR and TSFMs on state forecasting. None was found. A follow-up by the ICML authors is plausible.

**5. Why it matters.**
- *Practitioners:* risk desks need forecasts, not embeddings.
- *ML:* calibrates whether JEPA's inductive bias pays off in the one finance setting where it has shown signal.

**6. Closest prior and the difference.** ICML (descriptive, one era); covariance-forecasting deep learning such as RCM-NBEATSx and geometric deep learning (SciSpace hits, not stored), which is supervised rather than SSL state; TSFM-versus-HAR (arXiv:2607.05291).

**7. Search log.**
- SciSpace: "deep learning or foundation models forecast realized covariance/correlation better than DCC/HAR". The supervised literature is crowded.
- arXiv: "realized covariance forecasting", "volatility foundation model", "JEPA forecasting".
- WebSearch: the ICML title, which surfaced Eigen-JEPA (a GitHub-only synthetic-data project, web, 0 stars, unevaluated on real data).
- **Open: H for the specific analysis, L for the general topic** (state forecasting is crowded).

**8. Feasibility.**
- Data: CRSP daily (WRDS), or free daily prices for a first pass.
- Compute: about 12 H100-h per training run (ICML's figure); a sweep is roughly 100-200 GPU-h.
- No code release was found for ICML, so re-implementation risk is M.

**9. First pilot.**
- Re-implement the ICML pipeline on CRSP 1995-2024.
- Universes: top-512, mid-cap and small-cap.
- Rolling splits covering 2008 and 2020.
- Add 21-day-ahead forecasts of realised volatility, corr_mean and eff_rank.
- Compare JEPA probe, MAE probe, HAR and Log-HAR, DCC, Chronos-2 (arXiv:2510.15821), TTM (arXiv:2401.03955), and a supervised model trained from scratch.
- Sample-size curve.
- Bonus: a test-time-adaptation arm under regime shift (transfer from JEPA-TTT arXiv:2610.00722, abs). Speculative.

**10. Risks.**
- Closest to the ICML group's turf. Novelty is "rigorous extension", which ICAIF or a workshop may accept and ICML or NeurIPS likely would not.
- High JEPA-null risk, but a null here is informative and cheap.

**11. Confidence.** Open: **H** (specific analyses, from full text). Payoff: **M-L** standalone, **H** as the project's calibration pilot.

---


> **Adversarial review of G4 (2026-10-01).**
>
> **Verdict: weakened (M-H).**
> - **Weak as a paper:** it replicates a paper that calls itself "descriptive rather than predictive".
> - **Limited use as a pilot:** it calibrates G3 (market level), not G1 (firm statements). Run it only if G3 is chosen.

### G5. Network-conditioned firm state for supply-chain propagation, validated on natural experiments (use case c; pillars 1, 3)

**1. Statement.** No self-supervised firm-network state exists in which context is the history of neighbours (suppliers and customers) plus own history and the target is the firm's own fundamentals embedding. None is validated out of sample against *natural-experiment* propagation estimates (disaster shocks).

**2. Evidence.**
- arXiv:2609.32741 (FT): supervised; "preliminary experiments on 116 focal semiconductor firms"; no SSL; no natural-experiment validation. Its own review says prior work "rarely estimates the financial consequences for connected firms".
- Sato-Mizuno (doi:10.1007/s12626-022-00123-x, abs): ML sales-growth model with partial dependence, checked against Hurricane Sandy.
- Barrot-Sauvagnat (doi:10.1093/qje/qjw018) and Carvalho et al. (doi:10.1093/qje/qjaa044) give the identified propagation estimates (abs).
- The agent-based model (doi:10.1038/s41893-019-0351-x, abs) needs Japan-wide data.
- Graph-JEPA exists generically (web) but has no firm-network application.
- Causal caution: under interdependence, causal effects are "not uniquely defined objects" (arXiv:2601.00279, abs). Identification of networks needs "spectral heterogeneity" (arXiv:2604.04961, abs).

**3. Assumption challenged.** That propagation needs either a structural agent-based model on proprietary transaction data or supervised GNNs on curated graphs, rather than an SSL state on sparse public links.

**4. Falsifier.**
- A graph-SSL firm state validated against disaster-propagation estimates.
- Or evidence that Compustat customer-segment links are too sparse. Only customers above 10% of sales are disclosed, with a large-cap tilt (finance partial §7). Then the gap is real but not tractable on public data.

**5. Why it matters.** Supplier-risk teams, credit analysts and the PI's case (c). For ML: graph JEPA on a real economic network with an external causal benchmark.

**6. Closest prior.** arXiv:2609.32741 (supervised, 116 firms), arXiv:2407.18772 (customs data, proprietary; FT-ext), GNN link prediction (finance partial §7).

**7. Search log.**
- SciSpace: "GNN or self-supervised graph models predict firm-level propagation of supply chain shocks".
- arXiv: "supply chain graph learning", "production network shock propagation".
- WebSearch: "graph JEPA supply chain network firms".
- **Open: M-H.**

**8. Feasibility.**
- Data: Compustat Segments (WRDS; sparse), or FactSet Revere (PI access unknown).
- Disaster data: public (FEMA); the Barrot-Sauvagnat sample design is published.
- Tractability: **L-M**, pending data.

**9. First pilot.** Build the Compustat customer-link graph for 1990-2024. Test whether adding neighbour-state context improves 1-2 quarter forecasts of *customers'* sales growth after supplier-county disasters, compared with Forma without the graph and with a supervised GNN. Check against the published propagation magnitudes.

**10. Risks.** Data sparsity, causal over-reach (arXiv:2601.00279), JEPA-null.

**11. Confidence.** Open: **M-H**. Payoff: **M**. Tractability: **L-M** on public data.

---


> **Adversarial review of G5 (2026-10-01).**
>
> **Verdict: survives narrowed, conditional on link data (M).**
> - **Prior work:** the supervised version exists. Yang et al., IJDRR 2024, use a GNN on flood shocks to predict firm sales.
> - **Why it's the best identification setting:** disasters are exogenous, frequent, firm-level shocks with published effect estimates (Barrot-Sauvagnat `doi:10.1093/qje/qjw018`). That suits the PI's "world model with identification" goal better than G3 does.
> - **Revive K5:** average firm-level effects of exogenous shocks are identified, so firm-level counterfactuals belong here.

### G6. JEPA-latent scenario generators with tail and extremal-dependence fidelity (use case a; pillars 3, 4)

**1. Statement.** No one has tested a JEPA latent combined with a generative head (SPLICE, Branch-JEPA style) on financial or macro data for calibration, tails and cross-sectional extremal dependence, against diffusion and flow generators and stress-scenario methods.

**2. Evidence.**
- SPLICE (arXiv:2605.00126, FT-ext): electricity only. Its authors say it "degrades on zero-inflated/bimodal loads (64-d latent loses fine structure)".
- Branch-JEPA (arXiv:2607.05238) and Flow-JEPA (arXiv:2608.29029): robotics.
- arXiv:2608.13056 (abs) shows misspecified extremal dependence distorts joint-stress probabilities. That gives the evaluation criterion.
- Forma can pin future paths, giving value-space firm scenarios (FT).
- BISTRO offers path-conditioned macro forecasts (web).

**3-11. In brief.**
- *Falsifier:* a JEPA-plus-sampler evaluated on financial tails.
- *Searches:* arXiv "financial scenario generation", "stress scenario generation"; SciSpace (review stage); WebSearch (via the BISTRO check). Open: **M-H**.
- *Payoff:* **L-M**. JEPA latents being deterministic and smooth is exactly the wrong bias for tails. The ICML embedding misses stress onsets (FT).
- *Tractability:* M.
- **Not top-5.** Revisit after G1 or G3 yields a working latent dynamics model.

---

### G7. Joint predictive latent over filing text, tables and figures (multimodal extension; pillar 1)

- *Statement:* nothing learns a joint latent of filings in JEPA style; the field uses LLM embeddings as features (review §2, abstracts).
- *New enabler:* the Stanford EDGAR Filings Dataset (arXiv:2606.18192, abs): a 152B-token layout-faithful snapshot.
- *Open:* M (coverage was deliberately light).
- *Payoff:* unknown until G1 or G2 shows the tabular latent is worth extending.
- **Deferred** by the PI's decision (tabular first). Kept so it is not lost.

---

## 3. Merged and killed candidates

| # | Candidate (source) | Verdict | Why |
|---|---|---|---|
| K1 | "First JEPA for finance" or a market-regime embedding | **Killed** | Done: ICML (FT), Fin-JEPA (FT), Eigen-JEPA (web) |
| K2 | JEPA return or trading signal | **Killed** | Fin-JEPA AUC ≈0.50 (FT); ICML direction ρ=0.11 (FT); returns studies `doi:10.2139/ssrn.5770562`, arXiv:2606.27100, arXiv:2609.20554; also out of scope per the brief |
| K3 | Predicting stress onsets from a JEPA state | **Killed as a headline** | ICML: "not designed to detect or anticipate abrupt market stress"; displacement is "contemporaneous rather than anticipatory" (FT). Slow-feature theory (arXiv:2511.09783) predicts this. Keep only as a reported negative inside G4 |
| K4 | Collapse and usefulness diagnostics for financial latents (review gap 6) | **Merged** into every gap's evaluation layer | Not a paper on its own: arXiv:2608.20516 exists, and RankMe/LiDAR are standard |
| K5 | Firm-level counterfactual "what-ifs" (PI case b) | **Killed** as causal | Not identifiable from observational panels (finance partial §5.5; arXiv:2605.01694; arXiv:2601.00279). Allowed only as *disclosed conditional scenarios* (Forma-style pinning), not as effects |
| K6 | Standalone synthetic economy with latent firm states, actions and confounders (review gap 4) | **Merged** into G3 (DSGE-Gym arm) | DSGE-Gym (arXiv:2607.03144) has a Firm environment; FINESSE (arXiv:2609.11993) and CausalProfiler (SciSpace, not stored) cover generic synthetic causal benchmarks. Building a new world is infrastructure, not a gap, unless G3 shows DSGE-Gym is insufficient |
| K7 | Objectives for "correlation shape conditional on volatility" | **Killed** for us | It is the ICML authors' own stated future work (FT) and incremental on their turf |
| K8 | Macro ragged-edge JEPA nowcaster versus DFM (review gap 2, macro half) | **Merged** into G3 as the state-estimation layer | MACROCAST shows an honest ceiling of only ~3% RMSFE gain over AR(1) pooled (arXiv:2606.28670, FT-ext). About 800 monthly observations; DFM and GDPNow are strong. A JEPA nowcaster alone is unlikely to win; LiveMacroEval (arXiv:2608.30110, abs) shows LLM nowcasting also competing |
| K9 | Test-time adaptation under regime shift (transfer of JEPA-TTT arXiv:2610.00722) | **Merged** into G4 as a robustness arm | Speculative; no finance evidence; better as an ablation than a paper |
| K10 | Pre-registered JEPA vs reconstructive vs supervised study across sample sizes on financial panels (review gap 1) | **Split** into G1 (firm panels) and G4 (market panels) | It is a design principle for both rather than one gap |
| K11 | Irregular or informatively-missing inputs (review gap 2, firm half) | **Merged** into G1 and G2 | Forma's tuple-set already handles absent items natively (FT). ICML's lag-aware calendar-distance encoding (FT) and Timeflies (arXiv:2606.13571, abs) partly address irregularity. What remains open is the *JEPA objective under structured masks*, which is G1 |

---

## 4. Ranked top 5

| Rank | Gap | Use case | Novelty vs ICML | ICAIF fit | Data | Pilot cost | Main risk | Open / payoff |
|---|---|---|---|---|---|---|---|---|
| **1** | **G1** Latent vs value objective on firm statements under point-in-time, structured partial observation | (b) | **High**: different entity, data and objective question | **High**: Forma ICAIF '26, ACT-Tensor ICAIF '25, NMTucker ICAIF '23 | WRDS Compustat, or free SEC FSDS | Step 0 CPU-only; step 1 ~30 GPU-h pilot | JEPA null; mean/Last-Observed ceiling on entity masks | **H / M** |
| **2** | **G3** Identified-shock action-conditioning, LP/Proxy-DFM + DSGE-Gym validation | (a) | Medium-high: same *idea* the ICML authors flagged, but with identification and validation they lack | High: scenario and stress-test audience | All public | Small GPU; mostly CPU | Inert actions; small n; competition | **M-H / M** |
| **3** | **G2** Cross-frequency firm state: market view → unreleased fundamentals | (b) | High: neither ICML nor Forma links the views | High | CRSP + Compustat (`rdq`) + I/B/E/S | ~20-50 GPU-h | Consensus baseline; leakage | **M-H / M** |
| **4** | **G4** Honest scaled evaluation and state forecasting of market-state JEPAs | cross | Low-medium (extension) | Medium (workshop or ICAIF) | CRSP or free prices | ~100-200 GPU-h sweep | Derivative; null | **H / M-L** (H as the calibration pilot) |
| **5** | **G5** Network-conditioned firm state, natural-experiment validation | (c) | High | Medium-high | Compustat Segments or FactSet Revere (unknown) | Medium | Link sparsity; causal over-reach | **M-H / M** |

### Reviewer re-ranking (adversarial pass, 2026-10-01; the PI decides)
**Order with richer link data (e.g. FactSet Revere):**
1. **G1, narrowed.** A point-in-time structured-mask benchmark; JEPA is one hypothesis, alongside a value-plus-latent hybrid; G2 is merged in as an arm.
2. **G5, narrowed.** Conditional on link data; K5 (firm-level counterfactuals) is revived here.
3. **G3**, as a diagnostic paper.

Without richer link data, G3 moves to second and G5 to third. G4 becomes a pilot only, and only if G3 is chosen.

**Cross-cutting objection:** every gap is "an existing pipeline with a JEPA objective". With four negative results (arXiv:2609.31680, 2609.25541, 2609.16071, and the ICML paper's volatility-only result), the realistic deliverable is a **benchmark or diagnostic paper with a JEPA arm**. The PI should accept that explicitly (§5 Q6).

### Rationale
1. **G1 ranks first** because it does best on all four criteria at once.
   - It is clearly away from the ICML paper: firm-level, fundamentals, partial observation.
   - It has an incumbent public benchmark and code (ProForma-20Q and Forma) that make a *matched* JEPA test possible, which no earlier finance JEPA had.
   - The venue has accepted three neighbouring papers.
   - Its first step costs no GPU and answers the mean-imputation-ceiling question before money is spent.
   - It still yields a publishable artefact (structured-mask point-in-time benchmark plus a mechanism analysis) if JEPA does not win. That hedges the main risk the brief and the three 2026 negative results raise.
2. **G3 ranks second** because it carries the most scientific weight for the PI's "world model" ambition and use case (a). Every input is public.
   - It ranks below G1 because small n, inert-action risk and a credible competitor make a positive real-data result less likely.
   - The DSGE-Gym arm is the safe floor: a benchmark entry with off-path tail and coverage analysis.
3. **G2 ranks third.** It is novel and practitioner-relevant, and it reuses G1's infrastructure; G1 and G2 could become one paper with two arms. It depends on three WRDS modules and must beat analyst consensus.
4. **G4 ranks fourth** as a paper but **first as a pilot to run early**. It is cheap and re-creates the ICML setup, so every later JEPA claim has a calibrated reference point. On its own it risks being read as a replication.
5. **G5 is the best option for use case (c)**, but tractability depends on data the PI has not confirmed. If FactSet Revere is available it moves up to about third. On Compustat Segments alone it stays fifth or below.

**Use-case coverage.** (a) → G3 (ranked 2); (b) → G1 and G2 (ranked 1 and 3); (c) → G5 (ranked 5).

**Suggested sequencing (assistant view; the PI decides at checkpoint 2):**
1. G1 step 0 (CPU) and the G4 mini-replication (a few GPU-hours on free data), run in parallel.
2. Then G1 step 1.
3. G3's DSGE-Gym arm as a second track.

---

## 5. Questions for the PI
1. **WRDS entitlements.** Do you have Compustat Fundamentals Quarterly *and* Compustat Snapshot (point-in-time)? Also CRSP daily, I/B/E/S and Compustat Segments (customer links)? Any FactSet Revere access? This decides G1's main data, G2's feasibility and whether G5 moves up.
2. **Proprietary data (RockAI or employer).** Is there any *private-firm* financial data with real ground truth, such as lending or KYC statements? It would turn G1's simulated-private-firm arm into a real validation, used as a secondary, never sole, basis per the brief.
3. **Licences.** Forma's weights are non-commercial. Is research use under your academic affiliation acceptable, or must we retrain from the public code? Do the same constraints apply to code you would reuse at RockAI?
4. **Appetite for causal claims.** Should G3 be framed strictly as "conditional forecasts given identified shocks, validated against LP/Proxy-DFM", or do you want to attempt policy-rule counterfactuals (McKay-Wolf conditions)? I recommend the former.
5. **Competition tolerance.** The ICML authors list action-conditioned market JEPAs as future work. Are you comfortable racing them on G3, or should we take firm-level ground (G1, G2) first?
6. **Null-result tolerance.** Would you publish "JEPA does not beat a value-space objective; here is the benchmark and why", as the honest outcome of G1? This changes how hard we invest in tuning.
7. **Compute and timing.** Which GPU class, and what rough budget? (Pilots here are 30-200 GPU-h.) Which venue and deadline? ICAIF '27 versus a KDD applied-data-science track changes how much G1 and G2 need to be finished.
8. **Use case (c) priority.** If the supply-chain data is thin, are you willing to defer (c) to an extension of G1 and G2 (peer context as a feature)?

---

## 6. Search log (all 2026-10-01)

**arXiv** (`lit.py arxiv`, `--since 2025-10-01` unless noted; short queries)
- Date-sorted sweep: "JEPA" `--since 2026-07-01 --sort date --max 200`.
- Topic queries:
  - imputation fundamentals; missing firm characteristics (0); nowcasting firm revenue (0); earnings nowcasting (0)
  - mixed-frequency nowcasting; ragged edge nowcasting; irregularly sampled JEPA (0)
  - monetary policy shock neural network (0); impulse response deep learning; macroeconomic world model
  - financial scenario generation; stress scenario generation
  - supply chain graph learning; production network shock propagation
  - realized covariance forecasting; volatility foundation model
  - private firm financials; JEPA forecasting
  - DSGE world model; synthetic economy benchmark; counterfactual economic simulator
  - company fundamentals forecasting; financial statement forecasting
  - point-in-time financial benchmark; firm panel transformer; SEC filings XBRL
  - masked modeling financial panel; self-supervised financial representation
- An author search for "Mahns" returned nothing, so there is no arXiv version of the ICML paper.
- Long multi-term queries returned 0 because of AND-ing and were re-run short (see §0.6).

**SciSpace** (7 queries)
- firm fundamentals SSL imputation
- private-firm revenue from alternative data
- neural impulse responses vs LP/VAR
- JEPA or latent world model for macro vs DFM
- GNN supply-chain shock propagation
- deep learning covariance forecasting vs DCC/HAR
- synthetic economies for counterfactual benchmarking

**WebSearch** (9 queries)
- ICML title arXiv
- Mahns JEPA pdf or GitHub
- PMLR Mahns
- JEPA financial statements or fundamentals
- action-conditioned world model monetary shocks
- JEPA macro nowcasting
- graph JEPA supply chain
- ProForma-20Q
- BIS BISTRO

**Full texts obtained this stage** (PDF via pypdf):
- ICML 2026 (Lacuna mirror)
- Fin-JEPA (author's LaTeX)
- arXiv:2207.13071
- arXiv:2609.25541
- arXiv:2608.11327
- arXiv:2609.32741
- arXiv:2607.24410 (skim)
- arXiv:2608.07037 (skim)

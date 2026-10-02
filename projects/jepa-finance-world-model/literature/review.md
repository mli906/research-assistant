# Literature review: JEPA world models for finance
Project `jepa-finance-world-model`. Compiled 2026-10-01 from three facet partials:
- `partials/methods.md`: JEPA family and latent world models.
- `partials/finance.md`: finance and econometrics.
- `partials/eval-data.md`: evaluation and datasets.
- `industry.md`: industry practice.
The partials are the topic files and hold the detail, tables and screened-out lists. This file is the synthesis.

**Library.** 427 records in `papers.jsonl`.

| Tag | Records |
|---|---|
| finance | 178 |
| eval-data | 135 |
| methods | 107 |
| scan | 56 |
| core | 19 |
| industry | 9 |
| withdrawn | 1 |

The finance records also carry sub-tags: fin-rep, fin-causal, fin-dyn, fin-partial, fin-supply, fin-tab and fin-multimodal. There are 35 close-read notes in `notes/`.

**Recency window.** Frontier = since 2025-10-01; foundations = any date.

**Reading depth.** "Full text" means arXiv HTML read through WebFetch, which returns a model-written extraction. The 2026-10-01 spot-check caught one wrong number and one doubtful one in those extractions (section 12). Every number must be re-checked against the PDF before it goes into a paper. "(abs)" = per abstract only. "(web)" = web page, not in the library.

**Coverage caveats.**
- The arXiv API was rate-limited for most of the session, so the date-sorted arXiv sweep for the finance facet was not done. Frontier items came from WebSearch, OpenAlex id lookups and SciSpace.
- OpenAlex search ran out of its daily quota.
- Recall for 2025-10 to 2026-10 is good but not exhaustive. Re-run `/radar` once arXiv recovers.

Confidence labels: H (high), M (medium), L (low).

## 1. Bottom line
1. **Finance JEPA is no longer empty ground (H that it exists).** Closest prior work: an ICML 2026 poster by Mahns, Balestriero and Assran, "Joint-Embedding Predictive Learning of Latent Market States in U.S. Equities" (web: https://icml.cc/virtual/2026/poster/65643; OpenReview BZfkxSasd3; abstract only).
   - Method: a permutation-invariant tokenizer maps each day's cross-section of US equities to factor tokens, and a temporal JEPA predicts masked days, giving a daily market-state embedding.
   - Findings: the embedding tracks second-moment structure (realised volatility, correlation concentration, effective factor dimension) and tracks direction only weakly. It predicts gradual recoveries but not sudden stress onsets. Its regimes align with news topics.
   - The authors are central JEPA researchers: Balestriero co-wrote LeJEPA and Assran led I-JEPA and V-JEPA.
   - Also present: a single-author Fin-JEPA (`doi:10.2139/ssrn.6855118`; no abstract in the record; README per web: 367K params, 6,230 equities, "weak-to-negligible" trading signal) and an unevaluated, agent-generated "FinJEPA" on Hugging Face.
   - **Implication:** "first JEPA for finance" is not available as a claim. Room remains for:
     - firm-level panels with partial observation;
     - mixed-frequency or irregular inputs;
     - action-conditioning backed by an identification argument;
     - honest head-to-head comparison against econometric models, time-series foundation models (TSFMs) and tabular foundation models.
2. **JEPA on time series and tables is not reliably better than simple alternatives (M-H).** Three independent 2026 evaluations are negative or mixed:
   - sign flips across 9 backbones × 11 benchmarks (arXiv:2609.31680);
   - trails value-only training on 147 tabular datasets (arXiv:2609.25541, abs);
   - no in-domain gain over matched from-scratch training, and worse than a reconstructive latent state-space model (RSSM) (arXiv:2609.16071).

   The positive reports use small benchmarks and baselines the authors chose (TS-JEPA, CF-JEPA, HEPA, T-JEPA). The best small-data positive result is HEPA, arXiv:2605.11130: 92% of full-label performance with 2% of labels, including a VIX regime task. HEPA does event prediction, not state dynamics.
3. **Return forecasting is the wrong headline (H).**
   - Zero-shot TSFMs give negative out-of-sample R² on daily returns. Finance-native pretraining from scratch helps (`doi:10.2139/ssrn.5770562`; the abstract confirms the direction, and the numbers come from the note).
   - Independent tests find gains over a random walk "small and sparse" (arXiv:2606.27100).
   - Training on future data even *hurt* return forecasts in 18 of 20 cells (arXiv:2609.20554).
   - A world model should be judged on **state** targets: volatility, correlation structure, regimes, fundamentals. That matches what the ICML paper found its embedding captures.
4. **Counterfactual "what-if" is the riskiest pillar (H on the logic).** Two independent literatures agree.
   - ML theory:
     - Recovering the causal state needs diverse, exogenous actions and an invertible observation map (arXiv:2609.31161).
     - Passive prediction cannot identify counterfactual dynamics (arXiv:2605.01694).
     - Teacher-forced action-conditioning makes the actions inert (arXiv:2605.25313).
     - Clean effect estimates need paired rollouts from a restorable simulator (Do-JEPA, arXiv:2609.37378).
   - Econometrics:
     - Effects are identified only for identified shocks, via high-frequency instruments, local projections (LPs) and structural VARs (Gertler-Karadi `doi:10.1257/mac.20130329`; Nakamura-Steinsson `doi:10.1093/qje/qjy004`).
     - Counterfactuals under an alternative policy rule hold only within a model family and under policy invariance (McKay-Wolf `doi:10.3982/ecta21045`; arXiv:2409.09577).
     - Small VARs fail on non-invertible shocks where a factor-model state succeeds (arXiv:2307.06145).

   **Defensible claim:** "conditional forecast given an identified shock," validated against LP/VAR impulse responses. "What if the policy rate were 5%" holds only under stated assumptions.
5. **Learned world models break off the training path (H, per abstract).**
   - DSGE-Gym (arXiv:2607.03144) has eight environments built from dynamic stochastic general equilibrium (DSGE) models, scaling up to the ECB's 230-variable model. Learned world models match on-path dynamics but reach 5σ tail RMSE up to ~40× the on-path level.
   - Training on data generated by the DSGE models across rare and counterfactual states halves tail error and cuts policy-regime error 10-280×.
   - No JEPA was trained in it, which is a direct opening.
6. **Scenario generation needs an add-on (H).** JEPA predictors are deterministic. Available templates:
   - SPLICE, arXiv:2605.00126: JEPA latent → flow-matching/diffusion bridge → decoder → adaptive conformal bands. It is tested on electricity load only. Abstract numbers: CRPS 0.161, 93-95% coverage.
   - Branch-JEPA (K latent futures, Energy Score; arXiv:2607.05238).
   - VJEPA (variational, theory-heavy; arXiv:2601.14354).
   - Flow-JEPA is deterministic at inference (arXiv:2608.29029).

   Nobody has tested a JEPA generator for tail calibration or cross-sectional dependence on real stochastic data.
7. **Partial observability has theory, not evidence (M).**
   - Theory and toy results: belief-carrying JEPAs (UWM-JEPA, arXiv:2605.25313), the HMM view of JEPA (arXiv:2608.13621), and NextLat converging to belief states (arXiv:2511.05963).
   - **No JEPA handles irregular, mixed-frequency or informatively missing inputs**, which is exactly the shape of firm data. LeNEPA explicitly assumes regular sampling (arXiv:2607.00958).
   - Finance warning: cross-sectional-mean imputation is competitive with EM for firm characteristics, because missingness comes in blocks and observed data say little about missing values (arXiv:2207.13071, abs, confirmed in spot-check). Any imputer, JEPA included, is capped by this.
8. **Data scarcity is real at the entity level (H).**
   - Public firm panels: ~10³-10⁴ firms × ~70 quarters (SEC XBRL from 2009, as-filed) or ~10² quarters (Compustat).
   - Macro: ~10² series × ~800 months, with ALFRED vintages.
   - Private-firm financials are essentially unavailable publicly.
   - This is orders of magnitude below V-JEPA 2's 1M+ hours of video.
   - Response seen in 2026: synthetic pretraining plus real-vintage fine-tuning. MACROCAST (arXiv:2606.28670) is a leakage-free macro TSFM that beats AR(1) on ~80% of series-horizon pairs and beats BVAR and DFM.
9. **Evaluation pitfalls are specific and testable (H).**
   - Centred rolling windows and full-bar execution inflate Sharpe by ~4-30 units (arXiv:2605.23959). Centred context/target masks are common in JEPA, so the harness needs a leak unit test.
   - Pretraining contamination: only 6% of 401 datasets were never in any TSFM's pretraining data (arXiv:2510.13654).
   - Collapse can be invisible to probes and effective rank (arXiv:2608.20516).
   - Probe R² can be flat while decision quality differs by 43 points (arXiv:2608.18746).
10. **Industry (M-H).**
    - No verified "financial world model" product exists.
    - JEPA momentum is in robotics: V-JEPA 2 is open for commercial use, and AMI Labs raised $1.03B with no finance vertical.
    - Finance-specific TSFMs are the real baselines: Kronos, FinCast, EXAONE Finance (synthetic-only pretraining, licence CC BY-NC-ND).
    - Closest institutional analogue for scenarios: BIS **BISTRO** (WP 1337, 2026), a macro foundation model with conditional forecasting. It is not in the library, and its details are unverified.
    - Supervisors still hand-design a few narrative stress paths (Fed 2026; ECB 2026 reverse geopolitical test).

## 2. Pillar 1: representing the current state
- **Families.** Each competes for "state of a financial system".

  | Family | Examples | What it gives |
  |---|---|---|
  | General TSFMs | Chronos(-2), TimesFM, Moirai, TTM | forecasts, not states |
  | Finance TSFMs | Kronos `doi:10.1609/aaai.v40i30.39730`, FinCast, PLUTUS arXiv:2408.10111 | finance-native pretraining |
  | Contrastive asset embeddings | arXiv:2407.18645 | asset embeddings |
  | Latent-factor asset pricing | IPCA `doi:10.1016/j.jfineco.2019.05.001`; autoencoder asset pricing `doi:10.1016/j.jeconom.2020.07.009` | low-dimensional state: factors and loadings |
  | Tabular foundation models | TabPFN v2 `doi:10.1038/s41586-024-08328-6`, TabICL arXiv:2502.05564 | in-context predictors |

  Full taxonomy: `partials/finance.md` §2.
- **Tabular foundation models are strongest at small n**, which is the PI's regime. In credit data, TabICL had the best average AUC, with the edge concentrated below ~5,000 rows (`doi:10.48550/arxiv.2605.18147`). TabPFN matches or beats gradient-boosted trees (GBDT) on 1.1M company-years for distress prediction (arXiv:2605.10896, with firm-grouped rather than temporal CV). They are the baselines a firm-fundamentals JEPA must beat.
- **What JEPA tends to learn:**
  - In linear models, it prefers high-influence features and filters low-influence noise (arXiv:2407.03475, abs).
  - It fails when the nuisance noise is fixed (arXiv:2211.10831, abs), so slow macro levels and firm fixed effects are the expected failure mode (M, our transfer).
  - In the Koopman view, idealised JEPAs encode regime indicators rather than within-regime variation (arXiv:2511.09783).
  - What the latent encodes depends on the prediction targets, so the fundamentals must be in the *target* views (arXiv:2607.27017).
- **Multi-modal (planned extension).** Nothing found learns a joint predictive latent of filing text, tables and figures; the field uses LLM embeddings as features (FETILDA `doi:10.1145/3657299`, CUBAN `doi:10.1109/bigdata62323.2024.10825106`, FinLLaVA arXiv:2408.11878; all abs). That makes the extension potentially novel. Coverage of this theme is deliberately light (L-M).

## 3. Pillar 2: incomplete observation
- **The incumbent is the dynamic factor model (DFM) with a Kalman filter.** It handles ragged edges and mixed frequency (Giannone-Reichlin-Small `doi:10.1016/j.jmoneco.2008.05.010`; Banbura-Modugno `doi:10.1002/jae.2306`). It is what the Atlanta Fed's GDPNow and the NY Fed nowcast use operationally (web).
- **Deep versions:**
  - D2FM (arXiv:2007.11887) beats a DFM in real time (abs).
  - NCDENow (arXiv:2409.08732).
  - A transformer DFM with a conventional factor prior helps in small samples (arXiv:2601.12039, abs), which supports "structured prior + learned latent".
- **Gap (M):** no JEPA or masked-latent nowcaster has been compared with a DFM on ragged-edge real-time data.
- **Missing firm characteristics:**
  - Mean imputation is competitive (arXiv:2207.13071).
  - A structured imputer shows 70%+ of firms affected (`doi:10.1093/rfs/hhae036`, abs).
  - Tensor completion (arXiv:2508.01861, abs).
- **Private firms:** only alt-data proxies exist: job postings, search intensity, card spend and 10-K text (`partials/finance.md` §3.2). No benchmark with held-out ground truth was found (M; search incomplete). Design idea, not literature: use public firms as a *simulated private-firm benchmark* by masking disclosed fundamentals.

## 4. Pillar 3: dynamics, actions and counterfactuals
- **Robotics recipe.** Large passive pretraining (V-JEPA 2: >1M h video) plus a small action-labelled set (<62 h robot data) gives a plannable action-conditioned model (arXiv:2506.09985, abs). Finance lacks both the passive corpus and controllable actions.
- **Latent-action models do not transfer.** LAPO arXiv:2312.10812, LAPA arXiv:2410.11758 and the in-the-wild variants assume the observed change is caused by an agent's action and map latent actions to real actions with a few labels. Rate decisions and wars are endogenous and rare: on the order of 8 FOMC meetings a year (M).
- **Generalisation theory.** JEPA risk bounds planning regret, and small data favours a small latent dimension (arXiv:2606.27014). The multi-step bound assumes deterministic dynamics.
- **Econometric bar for counterfactuals.** See bullet 4 of the bottom line and `partials/finance.md` §5.
  - Identified shocks available as "actions": Romer-Romer `doi:10.1257/0002828042002651`, Gertler-Karadi, Bauer-Swanson `doi:10.1086/723574`, Jarocinski-Karadi `doi:10.1257/mac.20180090`.
  - Their validity is contested: the information effect, and instrument-validity tests.
- **Market generators** (GAN, signature, VAE, diffusion, order-flow models; `partials/finance.md` §4.1) target return distributions, not latent state. A JEPA generator must beat them on proper scoring rules: CRPS, Energy Score and tail calibration.

## 5. Pillar 4: uses, and which wedge is tractable
The finance scout ranked the PI's three candidate uses (`partials/finance.md` §8; confidence M):

| | (a) Macro scenarios | (b) Firm-fundamentals nowcast/imputation | (c) Supply chain |
|---|---|---|---|
| Public point-in-time data | FRED-MD/ALFRED vintages | SEC XBRL as-filed; Compustat Snapshot (WRDS) | sparse, large-firm-biased links; transactions proprietary |
| Ground truth | conditional forecasts and IRFs only | **mask disclosed values; held-out quarters** | link prediction; propagation only via natural experiments (Barrot-Sauvagnat `doi:10.1093/qje/qjw018`; Carvalho et al. `doi:10.1093/qje/qjaa044`) |
| Baselines to beat | DFM, BVAR, MACROCAST, growth-at-risk `doi:10.1257/aer.20161923` | cross-sectional mean, structured imputer, TabPFN/TabICL | GNN link prediction, input-output models |
| Causal burden | high | low (if nowcasting) | high |

The scout recommends **(b) as the first wedge**, framed as latent-state inference under partial observation and evaluated by masking. **(a)** would follow, with identified shocks as actions. **(c)** would be an extension where graph context is a feature.

My view: the ICML paper sits at the *market-state* level, so (b) also differentiates us from it. That is a point for `/find-gaps` to test, not a decision.

## 6. Evaluation and data (essentials; full detail in `partials/eval-data.md`)
- **Three evaluation layers:**
  1. Representation health: RankMe, LiDAR, probes with control tasks, and instance-level retrieval, because collapse can hide (arXiv:2608.20516).
  2. Dynamics: latent *and* decoded error normalised by persistence, AR, HAR and DFM, with Diebold-Mariano and Giacomini-Rossi tests.
  3. Use: a decision-aligned metric.
- **Harness template:** MACROCAST-style real-time harness (arXiv:2606.28670): ALFRED vintages and delayed actuals. For firms: EDGAR as-filed data with filing timestamps, every input gated by its release time.
- **Leakage checklist (L1-L11):** centred windows, normalisation fitted on the full sample, execution timing, survivorship, restatements, reporting lag, data and parameter contamination, LLM memorisation, multiplicity, and CV misuse. Each comes with a control.
- **Multiplicity:** pre-register, keep a trial ledger and report deflated metrics. The factor-zoo literature disagrees on how bad the problem is: `doi:10.1093/rfs/hhy131` vs `doi:10.1111/jofi.13249`.
- **Synthetic arena:** FinStressTS (arXiv:2606.03184; AR/HAR/DLinear beat Transformers at low SNR). **Missing: a synthetic economy with actions, confounders and latent firm states**, which is a candidate contribution (M).
- **Dataset table** (scale, licence, point-in-time support): `partials/eval-data.md` §4.
  - JKP factors are CC BY-NC and have a Common Task Framework.
  - SEC Financial Statement Data Sets are free and as-filed from 2009.
  - WRDS data cannot be redistributed.

## 7. What changed in the last 12 months
- Finance JEPAs appeared: the ICML 2026 poster, Fin-JEPA (2026) and the agent-generated FinJEPA.
- Independent negative or neutral JEPA-for-time-series and tabular results appeared, all in September 2026.
- Explicit anti-collapse regularisers replaced EMA heuristics: LeJEPA/SIGReg arXiv:2511.08544 and LeWorldModel arXiv:2603.19312. Time-series JEPAs adopted SIGReg.
- Theory arrived: JEPA generalisation (arXiv:2606.27014), causal-state identifiability (arXiv:2609.31161), the HMM view (arXiv:2608.13621) and JEPA-SCORE as a density estimate (arXiv:2510.05949).
- Counterfactual world-model tooling appeared: Do-JEPA and DSGE-Gym.
- Finance-native and leakage-free TSFMs appeared: Kronos, EXAONE Finance and MACROCAST. Tabular foundation models got their first finance benchmarks (TabPFN-3; credit and distress studies).
- Regulation: SR 26-2 replaced SR 11-7 on 2026-04-17. The reported exclusion of generative and agentic AI is from trade press and should be verified in the OCC PDF.

## 8. Academia vs industry
- **Academia** supplies JEPA theory and recipes, mostly from robotics and vision; NYU/Meta and the LeCun and Balestriero groups are central. It also supplies the econometrics of identification and nowcasting.
- **Industry labs** release general TSFMs (Amazon, Google, Salesforce, Datadog) and finance TSFMs (LG EXAONE, Kronos authors). Their claims are self-benchmarked, and independent tests find small gains.
- **Banks and funds** publish research areas, not models or metrics (J.P. Morgan, Two Sigma).
- **Central banks** use DFM/BVAR baselines on real-time vintages, which is more realistic evaluation than most ML papers. BIS BISTRO is the one macro foundation model.
- **Net:** academia lacks entity-level point-in-time data, and industry has it but doesn't publish. A paper that is leakage-clean on public data and shows how to use proprietary data is valuable to both sides.

## 9. Top must-reads
1. **ICML 2026 latent market states (web).** The closest prior work. Get the full paper from OpenReview and read it first.
2. **arXiv:2609.31680:** "Does JEPA pretraining help time series forecasting?" The backbone-dependence result defines the null to beat.
3. **arXiv:2607.03144 (DSGE-Gym):** a counterfactual benchmark for economic world models with no JEPA entry yet.
4. **arXiv:2609.31161 + arXiv:2605.01694:** when action-conditioned JEPAs recover causal states, and why passive prediction cannot.
5. **arXiv:2605.00126 (SPLICE):** the closest recipe for JEPA + sampling + calibrated uncertainty, applied to imputation.

Runners-up:
- arXiv:2606.28670: the MACROCAST harness.
- arXiv:2605.11130: HEPA, small-data positive.
- `doi:10.2139/ssrn.5770562`: TSFMs on returns.
- arXiv:2207.13071: the mean-imputation ceiling.
- arXiv:2608.20516: hidden collapse.

## 10. Challenges to the PI's framing
- "JEPA predicts the joint distribution" → it predicts embeddings and does not model a distribution (brief note). A density reading exists only through the anti-collapse term, in vision (arXiv:2510.05949).
- "Predictable features imply causality" → predictable ≠ causal. Identification needs exogenous, diverse actions (arXiv:2609.31161) or econometric identification (§4).
- "Use JEPA for counterfactual firm what-ifs" → not identifiable from observational firm panels without an exogenous intervention. Synthetic control and matrix completion identify only the effects of discrete, observed interventions (`partials/finance.md` §5.5).
- "Data scarcity" → confirmed, and specifically at the entity level. It argues for small models, synthetic pretraining and pooling across entities rather than a large JEPA.

## 11. Open problems → candidate gaps for `/find-gaps`
1. A pre-registered test of JEPA vs reconstructive SSL vs supervised training across training-set size on non-stationary financial panels, with AR/HAR/DFM/TabPFN baselines. No such study exists (H).
2. A JEPA that handles irregular, mixed-frequency, informatively missing inputs and is evaluated as a nowcaster or imputer against a DFM and the mean-imputation ceiling (H that it's absent).
3. An action-conditioned JEPA trained on identified shocks, evaluated against LP/VAR impulse responses and in DSGE-Gym off-path (M-H).
4. A synthetic economy with latent firm states, actions and hidden confounders for testing counterfactual validity (M).
5. Distributional fidelity of JEPA-based scenario generators (calibration, tails, cross-sectional dependence) vs diffusion/flow generators (M).
6. Collapse and usefulness diagnostics for financial latents (M).
7. A joint predictive latent over filing text, tables and figures, for the later multi-modal stage (L-M).

These must be checked against the ICML 2026 paper's full text before any novelty claim.

## 12. Verification log (2026-10-01, merge step)
Claims checked against the `papers.jsonl` abstracts:

| Claim (source) | Result | Action |
|---|---|---|
| DSGE-Gym "100× worse off-path" (methods partial) | **Wrong.** The abstract says "5σ tail RMSE up to ~40× the on-path level"; "10-280×" is correct | Corrected in `partials/methods.md` and here |
| SPLICE "CRPS 0.182 vs 0.197; beats VAE by 25.1%" (methods partial) | **Not in abstract.** The abstract gives CRPS 0.161 (-18.3%) and coverage of 93-95%. The extraction may come from an ablation table | Abstract numbers used; extraction flagged as unverified |
| Mean imputation competitive with EM (finance partial, arXiv:2207.13071) | Supported verbatim by the abstract | none |
| TSFMs zero-shot poor on returns, from-scratch finance pretraining helps (`doi:10.2139/ssrn.5770562`) | Direction supported by the abstract; the specific R² numbers are only in the note | Recheck the numbers against the PDF before citing |
| MACROCAST beats AR(1) ~80%, BVAR and DFM, with no leakage (arXiv:2606.28670) | Supported by the abstract; "pooled ratio 0.971" is from the note only | Same |

**Lesson:** WebFetch extractions can misstate numbers. Any number in the paper must come from the PDF or the abstract.

## 13. Not yet in the library / to do
- The ICML 2026 Mahns/Balestriero/Assran paper. It has no arXiv id or DOI found, and `lit.py` cannot fetch OpenReview ids, so it is cited by URL. Add it when an arXiv or DOI version is found.
- Also pending:
  - BIS BISTRO (WP 1337)
  - FinTSB (arXiv:2502.18834)
  - SiRE (arXiv:2208.10375)
  - FinEmbedDiff (arXiv:2406.01618)
  - Tail-GAN
  - arXiv:2506.15705
  - arXiv:2605.05404
  - `10.3982/qe1511`
  - arXiv:2602.10098, arXiv:2501.14622, arXiv:2604.22801
- Fin-JEPA (`doi:10.2139/ssrn.6855118`) has no abstract in its record.
- Tool issue: `lit.py fetch 10.48550/arXiv.<id>` routes to the arXiv API instead of OpenAlex.
- Screened-out lists: see §10 of `partials/methods.md`, §12 of `partials/finance.md` and §7 of `partials/eval-data.md`. Nothing was removed from `papers.jsonl` except 12 wrong-paper hits deleted by the finance scout after title checks.

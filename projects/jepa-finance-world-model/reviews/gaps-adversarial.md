# Adversarial review of `gaps.md` (top 5)

Project `jepa-finance-world-model`. Written 2026-10-01 by the reviewer agent, acting as an ICAIF/NeurIPS reviewer and devil's advocate. I had no part in writing `gaps.md`, and I did not edit it.

**Read:** `brief.md`, `STATE.md`, `gaps.md` (all sections), `literature/review.md`, and the notes `icml2026-mahns-latent-market-states.md`, `arXiv-2207.13071.md`, `arXiv-2607.03144.md` and `arXiv-2609.31161.md`. I also read the `papers.jsonl` records for arXiv:2608.11327 (Forma) and arXiv:2609.32741.

**Full text grepped myself** (pypdf extractions left in the session scratchpad by the gap-analyst):
- Forma, arXiv:2608.11327 (there is no note for it in `notes/`; that gap should be fixed)
- the ICML 2026 paper
- arXiv:2609.25541

**Library.** I added 7 records tagged `gaps-adversarial` via `lit.py fetch | add`, with titles checked against the fetched metadata:
- `doi:10.1109/icdmw.2013.115`
- `doi:10.1093/rfs/hhac085`
- `doi:10.2139/ssrn.4899584`
- `arXiv:2412.07649`
- `doi:10.1016/j.ijdrr.2024.104664`
- `doi:10.1093/jjfinec/nbae026`
- `doi:10.1111/fima.12480`

**Labels.** "abs" = per abstract or search snippet only; "FT" = full text I grepped myself; "spec" = my speculation.

---

## 0. Spot-checks of numbers `gaps.md` relies on

| Claim in gaps.md | Source checked | Result |
|---|---|---|
| Forma costs ~16.5 A100-h per seed | Forma FT: "Each seed trains in ≈16.5 hours on a single NVIDIA A100-SXM GPU; the five-seed run cost ≈$120" | Correct. Compute is *trivially cheap*, so pilot cost is not a ranking criterion for G1 |
| Forma uses `comp.fundq`, has no market data | FT: "The raw panel is Compustat Fundamentals Quarterly (comp.fundq)"; "We exclude stock returns, analyst forecasts, and other listed-firm features **so that Forma can be applied to private firms**" | Correct, but gaps.md omits *why* Forma excludes them (see G1 and G2) |
| ICML: FOMC N=66, p=.63 | ICML FT, Table 3 | Correct |
| ICML: recovery eff_rank AUC 0.690→0.800 | ICML FT | Correct |
| ICML: Mantel JEPA 0.35 | ICML FT, Table 2 | Correct |
| arXiv:2609.25541: JEPA trails value-only; one run per arm | FT: "in one run per arm, the JEPA arm trails ... 32:70 ... 8:24" | Correct, but incomplete. The JEPA arm there is **value loss + latent term**, and a pure latent objective "collapsed ... the encoder to a constant map" in their earlier runs. This matters for G1 |
| DSGE-Gym "no JEPA evaluated" | `notes/arXiv-2607.03144.md`; `partials/methods.md` l.52 | **Overstated.** NextLat (arXiv:2511.05963) is a next-latent self-prediction auxiliary objective, i.e. a JEPA-family latent predictor. It is already in DSGE-Gym and fails off-path like the other models |

---

## Cross-cutting objection, which applies to all five gaps

Every top-5 gap is defined as "X has been done, but not with a JEPA objective / under condition Y". That is **combinatorial novelty**. An ICAIF or NeurIPS reviewer's first line will be "this is swapping the loss on an existing pipeline". The problem is made worse by the project's own evidence base, all of it negative for JEPA on non-visual data:
- arXiv:2609.31680: gains change sign across 9 backbones (FT-ext).
- arXiv:2609.25541: the JEPA arm trails on 147 tables (FT).
- arXiv:2609.16071: no in-domain gain over matched from-scratch training (FT-ext).
- The ICML paper itself: a volatility-only baseline beats JEPA on Mantel, and JEPA hurts 2 of 4 transition tasks (FT).

Each gap's fallback is "the benchmark carries the paper if JEPA is null". So the realistic project is **a benchmark or evaluation project with a JEPA arm**, not a JEPA project. The brief's success criterion ("a JEPA approach that beats strong baselines") is unlikely to be met in any of the five (spec, but grounded in the four results above). The PI should accept this explicitly at checkpoint 2 (it is gaps.md §5 Q6), because it changes which gap is best: **the gap with the most valuable benchmark wins, not the gap with the most JEPA-friendly story.**

There is also a missing "why JEPA at all" argument. JEPA's claimed advantage is that it ignores unpredictable low-level detail (arXiv:2609.32481, abs: JEPA helps when the target is not recoverable from low-level priors). Quarterly accounting values are *not* noisy pixels. They are exact, identity-bound numbers, and the evaluation metric (change-space R², CRPS) is in value space. In G1 and G2 the "low-level detail" a JEPA would discard *is the target*. None of the gaps state a mechanism-level reason why latent prediction should help on these targets beyond "it's an open question".

---

## G1. Latent vs value objective on firm statements under point-in-time, source-block and entity-level masks

**1. Is it really open?**

Searches I ran:
- SciSpace: "self-supervised masked or joint-embedding pretraining on firm financial statement panels improve imputation or forecasting of missing accounting line items".
  - Hits: ACT-Tensor (arXiv:2508.01861, ICAIF '25 DOI 10.1145/3768292.3770408), NMTucker (doi:10.1145/3604237.3626909), a contrastive SSL for journal entries (doi:10.1145/3490354.3494373, abs, audit data, not statements) and CoSTCo tensor completion for analyst forecasts (doi:10.1109/ICDMW51313.2020.00059, abs). All are value-space or contrastive.
- WebSearch: "self-supervised pretraining financial statements foundation model accounting line items 2026" and "estimating private firm financial statements from partial disclosures ... masked public firms". Nothing latent-target.
- WebSearch: Forma / ProForma-20Q and the forma-lab-mccombs GitHub README. The README has no roadmap mentioning private firms, market data, imputation or SSL (https://github.com/forma-lab-mccombs/forma-release, accessed 2026-10-01).
- arXiv since 2026-06-01: "JEPA tabular", "JEPA financial", "financial statements forecasting". Only Forma, AGT (arXiv:2608.07037) and arXiv:2609.25541 came up.

**Verdict on openness:** literally open (H). Nothing applies a latent-target objective to statement panels.

**But the gap shrinks on three points:**
- **(a) Forma already supports partial-observation inference.** Its stated design is "Unreported items contribute no token (nothing is imputed)". Pinned-future masking trains it "to condition on chosen realizations", and "Arbitrary conditioning patterns can therefore be specified at inference time without retraining" (FT).
  - So the "source-block mask" benchmark is an *evaluation protocol on top of a released model*, not a new capability.
  - Fairness problem: Forma was trained with masks of p=0.05 on historical singletons, identity groups at 0.1, and the future block (FT, hyper-parameter table). Scoring it on whole-statement masks without retraining it on those masks is a **straw man**. Any JEPA arm trained on structured masks would win for the wrong reason.
- **(b) Forma is already positioned as the private-firm tool.** It deliberately excludes listed-firm features "so that Forma can be applied to private firms" (FT). G1's "simulated private firm" framing is therefore squarely in the Forma group's declared use case.
- **(c) The BLLP latent-factor imputer is already wired in.** Forma's tabular baselines use it ("imputed via the local XS estimator of Bryzgalova et al.", FT). The G1 baseline stack is mostly already built by the competitor.

**2. Who could scoop it?**
- The Forma group (UT Austin McCombs, Travis L. Johnson et al.; industry-funded per the paper's acknowledgements, FT) is best placed. They own the architecture, data pipeline, benchmark and venue (companion ICAIF '26 paper per the proforma-20q README, web). A "partial-statement / private-firm" follow-up is a natural next paper for them. The "JEPA objective" swap is not, so the *JEPA arm* is unlikely to be scooped, but the *structured-mask benchmark* could be.
- I found no JEPA group working on accounting data.

Scoop risk: **M** for the benchmark (gaps.md says low), **L** for the JEPA arm.

**3. Does it matter?**
- **Strongest so-what objection:** "You added a JEPA auxiliary loss to Forma, and it didn't help (or helped 0.3 pp). Why is this a paper?" This is near-certain to be the shape of the result for two reasons:
  - arXiv:2609.25541 (FT) shows that on tables a *pure* latent objective collapsed. The trainable version is a value-plus-latent hybrid, which trails.
  - G1's evaluation is in value space, so the JEPA arm needs a value head anyway. In practice G1 is "value objective ± latent auxiliary", which is the definition of swapping the loss.
- **What practitioners would care about:** the *benchmark*. That is point-in-time statements with realistic, source-structured missingness plus a private-firm-like observation pattern, and an honest answer to whether learned models beat Last-Observed plus industry means. Credit and KYC teams and data vendors care about that. ICAIF has a track record of accepting such work: NMTucker '23, ACT-Tensor '25 and Forma '26.

**4. Fatal flaws and hidden assumptions**
- **(i) The entity-level mask is ill-posed as written.** If *all* of a firm's statements are hidden and only "peers and industry" are visible, the model has no firm-specific input. The best possible predictor is a conditional peer mean, and every learned model collapses to it. The test is degenerate, not merely hard.
  - *Fix:* define private-firm-like observation patterns that real private firms actually have. Examples: revenue only; revenue plus headcount; annual-only totals; a lagged single year (as in credit files). Mask everything else.
  - If the PI has proprietary private-firm data (gaps.md Q2), use it only to *choose realistic patterns*, never as the sole basis.
- **(ii) Point-in-time is hygiene, not novelty.** Reviewers will not credit "as-filed" as a contribution unless you show it changes conclusions. *Fix:* report the fundq-vs-as-filed delta as a measured leakage effect, as Forma did for slot leakage ("≈0.7pp of test R²", FT).
  - Compustat restatement behaviour in `fundq` should be verified against WRDS documentation before it is claimed. I did not verify it (L).
- **(iii) The SEC FSDS fallback is a large hidden cost.** XBRL tag heterogeneity (custom tags, sign conventions, extension elements) means mapping to 78 Forma items is weeks of work, and that is the price of the reproducibility arm (spec, based on general XBRL experience; not quantified in gaps.md).
- **(iv) Is the null publishable?** A null on "JEPA auxiliary vs value" alone: workshop at best. A null *plus* a benchmark showing where learned models beat Last-Observed and peer means under realistic patterns: ICAIF-plausible.
- **(v) Simpler latent models are missing from the comparator list.** The list should include a firm-panel state-space or DFM-style latent model, IPCA-style characteristic factors (`doi:10.1016/j.jfineco.2019.05.001`), and the BLLP imputer. If "latent state" is the claim, a linear-Gaussian latent state is the first baseline a finance reviewer will ask for.

**5. Verdict: SURVIVES NARROWED (confidence M).**
- Reframe as **"a point-in-time, structured-partial-observation benchmark for firm statements"**, with the realistic observation patterns from (i).
- Make the main question "which inductive biases help under which observation pattern". Arms: Forma retrained on the same structured masks (mandatory, for fairness), value + JEPA auxiliary, linear state-space, BLLP, TabPFN, Last-Observed and peer means.
- JEPA becomes one pre-registered hypothesis, not the headline.
- Keep step 0 (CPU headroom) exactly as gaps.md proposes. It is the best idea in the file.

---

## G2. Pre-filing fundamentals nowcast with the daily market cross-section as context

**1. Is it really open? No, not as framed.**

Searches I ran:
- SciSpace: "Do daily stock returns and market prices help ML models predict a firm's quarterly earnings or revenue before the financial statements are filed, compared with analyst consensus".
  - Top hit: **Kamp, Boley and Gärtner, "Beating Human Analysts in Nowcasting Corporate Earnings by Using Publicly Available Stock Price and Correlation Features"** (ICDMW 2013, `doi:10.1109/icdmw.2013.115`; also SDM 2014; abs). It nowcasts earnings from stock prices and pairwise correlations and beats analysts on the S&P 100 over 2008-2012. That is G2's core claim, including the word "nowcasting", published 13 years ago.
  - Also: distributional earnings forecasts just before announcements (Dichev et al., doi:10.31235/osf.io/4b2y8, abs) and Twitter-based earnings prediction (doi:10.2139/SSRN.2782236, abs).
- WebSearch on ML vs analyst earnings forecasts:
  - Chen-Cho-Dou-Lev, JAR 2022 (`doi:10.1111/1475-679x.12429`). This is **already in the library, and gaps.md does not engage with it.**
  - Cao and You, FAJ 2024 (web: https://rpc.cfainstitute.org/research/financial-analysts-journal/2024/fundamental-analysis-via-machine-learning).
  - **van Binsbergen-Han-Lopez-Lira, RFS 2023** (`doi:10.1093/rfs/hhac085`). A random forest on fundamentals, past returns, macro and analyst data forecasts earnings against analysts. It now carries an **Expression of Concern** (web: https://academic.oup.com/rfs/advance-article/doi/10.1093/rfs/hhag017/8502599).
  - **Zhang-Zhu-Linnainmaa, "Man versus Machine Learning Revisited"** (RFS 38(12), 2025; `doi:10.2139/ssrn.4899584`; abs/web). They find **look-ahead bias** in that pipeline, and removing it erases the alpha; linear models do as well. They release a look-ahead-free earnings-forecast dataset (https://github.com/yandi-zhu/Man-versus-Machine-Learning-Revisited).
- arXiv since 2026-06-01: "earnings nowcasting". 0 hits.

**What survives:**
- (a) **Full-statement, non-EPS items** (working capital, capex, balance-sheet items) that consensus does not cover.
- (b) **Firms with no or thin analyst coverage**, where consensus does not exist.
- (c) A latent cross-frequency firm state as the mechanism.

(a) and (b) are real but niche. (c) is the swap-the-loss objection again.

**2. Who is on it?**
- The accounting and finance ML-earnings community (Lev, Linnainmaa, Lopez-Lira and others) owns the framing, and they publish in JAR, RFS and FAJ, not at ICAIF.
- Forma explicitly will *not* add market data (FT: the exclusion is a design choice for private-firm use). That leaves the "Forma + market view" niche open, but only because its owners consider it the wrong direction for their use case.

**3. Does it matter?**
- **Strongest objection:** "Analysts already impound price information; a model that nowcasts EPS from prices reproduces consensus less well." This is the classic analyst-superiority-from-information argument (spec; I did not fetch the Brown et al. 1987 line of work).
- For ICAIF, a nowcast that beats consensus on *EPS* would be interesting but has been claimed before (Kamp et al.). One that beats a *naive* baseline on capex for uncovered firms is useful but modest.

**4. Fatal flaws and hidden assumptions**
- **(i) The window is short, and the pilot as written leaks.**
  - Earnings press releases (8-K, captured by Compustat `rdq`) usually come out a few weeks after quarter-end, and the 10-Q deadline is 40-45 days.
  - The pilot's k = 40 *trading* days after quarter-end (~2 calendar months) is past announcement for most firms, so the target is already public (spec on exact distributions; verify with `rdq`).
  - k must be defined relative to each firm's own `rdq`, with nowcasts strictly before it, and pre-announcements/guidance treated as information.
- **(ii) Field precedent for leakage.** The van Binsbergen → Zhang-Zhu-Linnainmaa episode shows that this exact setting (ML earnings forecasts vs analysts) has already produced a high-profile look-ahead failure, now under an Expression of Concern. Reviewers will be primed for it.
- **(iii) Survivorship and coverage.** Using I/B/E/S restricts the sample to covered firms, while the useful niche (b) is uncovered firms. The baseline and the niche do not overlap.
- **(iv) Is JEPA the right tool?** Ridge or GBM on lagged fundamentals plus returns-since-quarter-end is the obvious baseline and is probably strong. Zhang-Zhu-Linnainmaa found linear models match random forests.

**5. Verdict: WEAKENED (confidence M-H). Do not run it as a standalone paper.**
- Narrow it to "a market-context arm inside the G1 benchmark".
  - Does adding the daily market view (returns since quarter-end, peer returns) to statement history improve nowcasts of *non-EPS items* for *low-coverage firms*, at horizons strictly before `rdq`?
  - Baselines: the Zhang-Zhu-Linnainmaa look-ahead-free forecasts where available, and ridge/GBM.
- Cite Kamp et al. and Chen-Cho-Dou-Lev as prior work.

---

## G3. Identified-monetary-shock action conditioning, checked against LP/Proxy-DFM and DSGE-Gym

**1. Is it really open? Partly.** The *JEPA* combination is open; the substance is not.

Searches I ran:
- SciSpace: "neural network or ML models estimate state-dependent impulse responses to high-frequency identified monetary policy shocks ... compared with local projections".
  - **Hauzenberger-Huber-Klieber-Marcellino, "Machine Learning the Macroeconomic Effects of Financial Shocks"** (`arXiv:2412.07649`, abs). Neural networks learn *nonlinear impulse responses to structural shocks* (sign asymmetries). It was not in the library.
  - Goulet Coulombe-Klieber (arXiv:2505.12422, abs): ML impulse responses as proximity-weighted LPs.
  - State-dependent LP theory (Gonçalves-Herrera-Kilian-Pesavento, doi:10.24149/wp2205, abs): consistency fails when the state depends on current or future outcomes.
  - Smooth LP (Barnichon-Brownlees) and Cloyne-Jordà-Taylor state-dependent LP (abs).
- WebSearch: "action-conditioned world model macroeconomics monetary policy shocks deep learning 2026". Only DSGE-Gym (arXiv:2607.03144) and Hauzenberger et al. matched; no JEPA.
- WebSearch on BISTRO (BIS WP 1337, March 2026; https://www.bis.org/publ/work1337.pdf). WebFetch summary of the BIS page: it does conditional forecasting on assumed paths of explanatory variables, and the page mentions no impulse responses and no LP/VAR comparison. This matches gaps.md (web; L-M, since only the page was summarised).
- arXiv since 2026-06-01: "JEPA macroeconomic" (0), "monetary policy world model" (only the LLM nowcasting paper arXiv:2608.30110), "market world model". The last returned two position papers, arXiv:2606.10044 "Business World Model" and arXiv:2608.06020 "Economic World Models". Per abstract both are conceptual blueprints and neither pre-empts G3.

**Conclusion:** "learned nonlinear model, conditioned on an identified shock, compared with LP" exists (arXiv:2412.07649). What G3 adds is (a) a latent state that includes market geometry and (b) the JEPA objective. That is again a swap of model class.

**2. Who could scoop it?**
- The ICML group states this as future work (FT §5.1, verbatim in the note). Their framing is news or prediction-market labels as "interventions", with no identification argument.
- Central-bank ML groups are better placed on the econometrics: BIS (BISTRO team), the OeNB (Klieber), and Goulet Coulombe.

Scoop risk on the *idea*: M-H. Scoop risk on the *identified* version: M.

**3. Does it matter?**
- **Strongest objection (macro reviewer):** "Your world model's IRF agrees with the LP on the same 30 years of data with the same shock series. That is internal consistency, not validation. If it disagrees, the LP is not ground truth either. What did we learn?"
  - LP bands on monthly HFI-shock responses are wide (spec, but standard). Agreement-within-bands has low power to discriminate any model from any other.
  - gaps.md's "pre-register sign and shape tests" does not fix the power problem.
- **Strongest objection (ML reviewer):** the DSGE-Gym arm duplicates an existing entry. NextLat is a latent-predictive model already in DSGE-Gym (see §0), and the benchmark already shows flexible models fail off-path. A JEPA row in that table is incremental.

**4. Fatal flaws and hidden assumptions**
- **(i) The identification theory gaps.md cites works against the plan.**
  - arXiv:2609.31161 (per the note, FT-ext) needs actions inducing "sufficiently diverse" changes, a rank condition on action-variation matrices.
  - A **scalar** monetary surprise cannot satisfy a rank condition for a ~10²-dimensional latent. Component-wise identifiability of the latent is ruled out by construction, not merely "at risk" (M; I read only the note's summary of the theorem).
  - What *can* be identified is the response of chosen observables to the shock, which is exactly what LP already gives.
- **(ii) The DSGE-Gym arm does not test the identification story.** In DSGE-Gym, shocks are exogenous by construction, so there is no confounding. It tests off-path extrapolation, not identification. gaps.md lists it as the "safe floor", but as an *identification* paper it is off-topic.
- **(iii) The data are tiny.** About 400 months of macro data (gaps.md's own figure). There are ~280 FOMC events, and most surprises are tiny (gaps.md cites the action-excitation concern itself, arXiv:2607.22430, abs).
  - The ICML embedding does not move on FOMC days (FT, p=.63), so "market-state geometry" as a response variable is likely a null.
  - Expect the inert-action failure (arXiv:2605.25313, FT-ext) as the modal result.
- **(iv) Shock predictability.** HFI surprises are partly predictable from public data (Bauer-Swanson's own finding, `doi:10.1086/723574`; spec on exact magnitude). If the world model's state contains those predictors, the shock-as-action is confounded *inside* the model unless it is orthogonalised first.
- **(v) Is the null publishable?** "A learned latent world model cannot recover identified monetary IRFs from US data" could be a useful negative for ICAIF, but only if it comes with a diagnosis (inert actions, rank deficiency) rather than just a bad fit.

**5. Verdict: WEAKENED (confidence M).** It survives only if narrowed to a **diagnostic paper**: "when can a learned latent world model reproduce identified impulse responses, and why it goes inert".
- Synthetic first: DSGE-Gym NK with *known* shock structure, varying the number and diversity of shock types to test the rank condition empirically. This is a genuine use of arXiv:2609.31161 on economic data.
- Then real data, with LP/Proxy-DFM *and* the Hauzenberger et al. neural IRF as baselines.
- Drop "market-state geometry" as a primary response variable (the ICML FOMC null).

Rank it below G1. Its claim to second place rested on the "world model ambition", which this evidence does not support.

---

## G4. Re-implementation and calibration study of the ICML market-state JEPA

**1. Is it really open?** The specific analyses are open (H). The topic is crowded.

Searches I ran:
- WebSearch: "Mahns Balestriero Assran JEPA market states follow-up 2026". Only the ICML poster and its Lacuna page; no follow-up or code found (accessed 2026-10-01).
- SciSpace: "self-supervised representations of the equity cross-section improve forecasting of realized volatility or correlation matrices vs HAR and DCC". Results are supervised only:
  - graph-augmented HAR, JFEC 2024 (`doi:10.1093/jjfinec/nbae026`, abs: significant gains over HAR up to 1 month);
  - RCM-NBEATSx (doi:10.2139/ssrn.4529219, abs);
  - geometric deep learning, arXiv:2412.09517 (abs);
  - LSTM-MF, doi:10.1002/for.70021 (abs).
- WebSearch: "self-supervised market state embedding forecast realized volatility correlation HAR". Found the TSFM-vs-HAR comparison (arXiv:2607.05291, in library) and nothing SSL.

**2. Who could scoop it?**
- **The ICML authors**, almost by definition: they have the code, data vendor and pipeline. Their stated future work covers scaling, denser data and other markets/eras (FT).
- Any re-implementation without released code cannot attribute discrepancies, because there are differences in data vendor (Massive.com vs CRSP), universe and features.

**3. Does it matter?**
- **Strongest objection:** "A replication of a poster that already says its embedding is 'descriptive rather than predictive' and 'complementary rather than uniformly superior' (FT). Confirming that HAR wins is expected." The supervised covariance-forecasting literature (above) already beats HAR in places, so the JEPA state would need to beat *graph-HAR*, not just HAR.
- Workshop-level as a paper.

**4. Fatal flaws and hidden assumptions**
- **(i) The "calibration pilot for everything" rationale is weak.** A market-level OHLCV JEPA calibrates nothing about G1's statement tuple-sets (different data, architecture and target). It is relevant only to G3, which uses the market-state embedding. gaps.md's "run G4 in parallel with G1 step 0" therefore spends effort on the wrong track unless G3 is chosen.
- **(ii) Realised-vol targets from daily CRSP need range-based estimators.** True RV needs intraday data, which ICML's vendor may give but CRSP does not. That is another unattributable difference (spec).

**5. Verdict: WEAKENED (confidence M-H).**
- Drop it as a paper candidate.
- Keep a *single-run* mini-replication (~12 H100-h per the ICML compute figure, FT) **only if G3 is pursued**, since G3 needs the embedding as an input.

---

## G5. Supply-chain-conditioned firm state vs disaster natural experiments

**1. Is it really open? Less than gaps.md says.** The supervised version, including validation against disasters, exists.

Searches I ran:
- SciSpace: "GNNs or self-supervised graph models of supplier-customer networks validated against natural disaster shocks ... to firm sales".
  - Sato-Mizuno (doi:10.1007/s12626-022-00123-x; in library; abs): an ML sales-growth model checked against Hurricane Sandy.
  - Inoue-Todo agent-based models (doi:10.1038/s41893-019-0351-x; abs).
  - Upstream propagation of earthquake shocks, Chinese listed firms (`doi:10.1111/fima.12480`, abs).
  - Kashiwagi-Todo-Matous on Hurricane Sandy (RePEc, abs).
- WebSearch: "graph neural network supplier customer network firm sales forecasting natural disaster propagation".
  - **Yang, Ogawa, Ikeuchi, Shibasaki and Okuma, "Post-hazard supply chain disruption: Predicting firm-level sales using graph neural network"** (IJDRR 110, 2024; `doi:10.1016/j.ijdrr.2024.104664`; abs). A GNN using inter-firm relations and hazard damage predicts post-flood sales and beats baselines without the network. **This is the supervised core of G5, already done** (Japan data).
  - Also arXiv:2606.29290 (supply-chain propagation of LLM text embeddings for returns; title only).
- arXiv since 2026-06-01: "supply chain self-supervised". No relevant hits.

What remains open: (a) SSL (JEPA) instead of supervised, which is swap-the-loss; (b) **US public-data** setting; (c) validation of *counterfactual* responses (disaster vs no-disaster rollouts) against a Barrot-Sauvagnat-style DiD estimate, rather than forecast accuracy.

**2. Who could scoop it?**
- Hur and Samtani (arXiv:2609.32741, FT per gaps.md) already fuse disaster signals into a 15,186-firm graph. Adding a natural-experiment check is a small step for them.
- The Japanese TSR-data groups (Todo, Inoue, Mizuno) own the data-rich version.

**3. Does it matter?** Yes, more than G3 on the identification axis, and gaps.md under-weights this.
- Natural disasters are *plausibly exogenous, frequent, firm-level* shocks with many treated units and published identified estimates: Barrot-Sauvagnat (`doi:10.1093/qje/qjw018`) and Carvalho et al. (`doi:10.1093/qje/qjaa044`).
- That is a much better setting for the PI's "action-conditioned world model with an identification argument" than ~280 scalar monetary surprises (G3).
- **Strongest objection:** "Compustat customer links only include customers above 10% of sales. You are learning a graph state on a sparse, large-firm-biased skeleton, and the GNN already exists."

**4. Fatal flaws and hidden assumptions**
- **(i) Data.** Compustat Segments links are sparse and large-cap-tilted (gaps.md). FactSet Revere access is unknown. Without richer links the "network state" is mostly empty for most firms.
- **(ii) Effect vs forecast.** Comparing a model's forecast error with a DiD ATT is apples to oranges. The model must produce paired disaster/no-disaster rollouts, and the estimand must match (average effect on customers' sales growth over h quarters). This is doable but must be designed in, not bolted on.
- **(iii) Interference.** Under network interference, effects are "not uniquely defined objects" (arXiv:2601.00279, abs). The estimand must be the specific exposure mapping that Barrot-Sauvagnat use.

**5. Verdict: SURVIVES NARROWED, conditional on data (confidence M).**
- Reframe as "**exogenous-shock-conditioned firm-network state, validated against published natural-experiment estimates**", with the supervised GNN (Yang et al. design) and Forma-without-graph as baselines.
- JEPA vs supervised is one hypothesis, not the headline.
- If the PI has FactSet Revere or similar, this is the best home for the "world model + identification" ambition. If not, it stays low.

---

## Re-ranking (reviewer view; the PI decides)

| New rank | Gap | gaps.md rank | Verdict | Why it moved |
|---|---|---|---|---|
| 1 | **G1 narrowed**: point-in-time structured-partial-observation benchmark for firm statements; JEPA auxiliary as one arm; G2's market-context arm merged in | 1 (+3) | Survives narrowed, M | Most valuable artefact if JEPA is null; cheap (Forma ≈$120 per 5 seeds, FT); but needs a well-posed entity mask and a fairly retrained Forma |
| 2 | **G5 narrowed**: exogenous-disaster-conditioned network firm state vs DiD estimates | 5 | Survives narrowed, M; **conditional on link data** | Best identification setting of the five; supervised prior exists, so the novelty is the counterfactual validation |
| 3 | **G3 narrowed to a diagnostic**: rank-condition and inert-action study, DSGE-Gym then LP | 2 | Weakened, M | Prior neural IRF work (arXiv:2412.07649); a scalar shock violates the rank condition; LP agreement has low power; NextLat is already in DSGE-Gym |
| — | **G2** merged into G1 as an arm | 3 | Weakened, M-H | Kamp et al. 2013/14 pre-empt the core claim; the ML-earnings literature and its look-ahead controversy apply |
| — | **G4** pilot only, and only if G3 is chosen | 4 | Weakened, M-H | Replication of a self-described descriptive poster; calibrates nothing about G1 |

If the PI has no FactSet Revere access, G3-diagnostic moves to 2 and G5 to 3.

## Candidates I think were wrongly killed or merged

- **K5 (firm-level counterfactual what-ifs), partially wrongly killed.** It was killed as "not identifiable from observational panels". That holds for *endogenous* actions. For **exogenous shocks** (disasters, perhaps tariff or trade shocks with published identified estimates), firm-level average responses *are* identified. K5 should be revived *inside* G5 as "conditional effects of exogenous shocks on firm statements", using Forma-style pinning plus a shock input. This also gives use case (b) a counterfactual arm the PI asked for.
- **K8 (macro ragged-edge JEPA nowcaster): kill agreed.** MACROCAST's ~3% ceiling (arXiv:2606.28670, FT-ext) and the DFM/GDPNow incumbents make it a poor bet.
- **K6 (synthetic economy): agreed it is merged,** but note that G3-diagnostic needs a *controllable shock-diversity* knob. If DSGE-Gym does not expose it, K6 partly returns as infrastructure.
- **K1-K4, K7, K9-K11: agreed.**

## Missing references the gap file should add (now in `papers.jsonl`, tag `gaps-adversarial`)

- `doi:10.1109/icdmw.2013.115`: Kamp et al. (G2 pre-emption).
- `doi:10.1093/rfs/hhac085` and `doi:10.2139/ssrn.4899584`: ML vs analysts, and the look-ahead correction (G2 leakage precedent).
- `arXiv:2412.07649`: neural nonlinear IRFs (G3 prior).
- `doi:10.1016/j.ijdrr.2024.104664`: GNN post-hazard firm sales (G5 prior).
- `doi:10.1111/fima.12480`: upstream earthquake propagation (G5 validation targets).
- `doi:10.1093/jjfinec/nbae026`: graph-HAR covariance forecasting (G4 baseline).
- Also write `notes/arXiv-2608.11327.md`. Forma is the single most important prior for the top gap and has no note.

## Questions the PI must answer before `/ideate`

1. Do you accept that the realistic deliverable is a benchmark or diagnostic paper with a JEPA arm? If you require a "JEPA wins" headline, none of the five is a good bet (spec, grounded in the four negative results cited above).
2. FactSet Revere (or any richer supplier-customer data)? This decides whether G5 is rank 2 or rank 4.
3. Do you have real private-firm observation patterns (which fields a lender actually sees)? They are needed to make G1's entity-level arm well-posed.

Sources (web, accessed 2026-10-01):
- [Forma arXiv page](https://arxiv.org/abs/2608.11327)
- [forma-release README](https://github.com/forma-lab-mccombs/forma-release)
- [ProForma-20Q](https://github.com/forma-lab-mccombs/proforma-20q)
- [BIS WP 1337 BISTRO](https://www.bis.org/publ/work1337.pdf)
- [ICML poster](https://icml.cc/virtual/2026/poster/65643)
- [RFS Expression of Concern](https://academic.oup.com/rfs/advance-article/doi/10.1093/rfs/hhag017/8502599)
- [MvML Revisited code](https://github.com/yandi-zhu/Man-versus-Machine-Learning-Revisited)
- [IJDRR GNN paper](https://www.sciencedirect.com/science/article/pii/S2212420924004266)
- [Cao & You FAJ](https://rpc.cfainstitute.org/research/financial-analysts-journal/2024/fundamental-analysis-via-machine-learning)
- [ICAIF 2026](https://icaif2026.org/)

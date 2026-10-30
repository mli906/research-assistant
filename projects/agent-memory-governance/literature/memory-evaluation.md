# The agent-memory evaluation space: a comprehensive review  ·  *landscape hub*

Facet: `memory-eval` (new, opened 2026-10-30). This is the **whole** memory-evaluation space, organized by *what is being measured*, and the **hub** of the project's four evaluation notes — read them as one landscape through this file.

### The evaluation landscape — four notes, one body

| Note | Role | Owns |
|---|---|---|
| **`memory-evaluation.md`** (this file) | **Hub / landscape index** | The full space by evaluation target (§0 map), representative metrics + formulas per silo, meta-evaluation pitfalls, metric-family reference, `/radar` plan |
| [`evaluation.md`](evaluation.md) | Governance deep-dive | Benchmark catalog; operations × governance-properties matrix; governance metrics (privacy, erasure, isolation, integrity, provenance, freshness-as-compliance). Expands §11 |
| [`eval-procedural-skills.md`](eval-procedural-skills.md) | Procedural deep-dive | Skill-distillation eval beyond success rate; regression gates; formation quality; general-vs-finance. Expands §7 |
| [`partials/evaluation.md`](partials/evaluation.md) | Working partial | The raw `evaluation`-facet query plan + source partial behind `evaluation.md` |

Navigation rule: **start here** for "what is measured and how"; follow the pointer in a silo to the deep-dive note that owns it. Each deep-dive note carries a one-line banner back to this hub.

- **Scope.** LLM/agent memory evaluation across capability *and* governance: retrieval/recall, retention-vs-selection, dynamics (update/staleness/conflict/forgetting), action/decision grounding, continual/test-time learning, cost/efficiency, personalization, multimodal/embodied, operation-level diagnosis, judge-based evaluation, meta-evaluation.
- **Base.** Library synthesis as of the 2026-09-24 `evaluation` scout + the 2026-10-22 radar + a 2026-10-30 capability-side sweep (12 queries, `--since 2026-09-15`): 22 records newly tagged `memory-eval`, library → 958.
- **Evidence labels.** ids = in-library records. `full`/`abs` as in the other partials. Confidence on my judgments in brackets.
- **Confidentiality.** No `inputs/` (RockAI) text used.

---

## 0. Map of the space (the organizing table)

What memory evaluations actually measure, and where each is covered.

| # | Evaluation target | Core question | Maturity | Section |
|---|---|---|---|---|
| 1 | **Retrieval / recall quality** | Can it find the right memory? | High (saturating) | §1 |
| 2 | **Retention vs selection** | What to keep vs what to surface — disentangled | Emerging | §1.2 |
| 3 | **Dynamics: update / staleness** | Does it stay current, drop superseded facts? | Fast-growing | §2.1 |
| 4 | **Dynamics: conflict** | Does it rank valid over contradictory evidence? | Medium | §2.2 |
| 5 | **Dynamics: forgetting** | Can it forget selectively / on request? | Medium | §2.3 |
| 6 | **Action / decision grounding** | Does memory improve *decisions/actions*, not just QA? | Emerging, important | §3 |
| 7 | **Continual / test-time learning** | Does it improve over a task stream without forgetting? | Fast-growing | §4 |
| 8 | **Cost / efficiency / Pareto** | Accuracy *per* token/$/latency/storage | Low→rising | §5 |
| 9 | **Personalization** | Right knowledge for *this* user's circumstances | Fast-growing | §6 |
| 10 | **Procedural / skills** | Learns & reuses procedures (→ [`eval-procedural-skills.md`](eval-procedural-skills.md)) | Very crowded | §7 |
| 11 | **Multimodal / embodied / spatial** | Memory over video, egocentric, physical state | Emerging | §8 |
| 12 | **Operation-level diagnosis** | *Where* it fails: encode vs retrieve vs generate | Low | §9 |
| 13 | **Judge / reward-model evaluation** | Can a model judge memory management? | Low | §10 |
| 14 | **Governance / trustworthiness** | Privacy, erasure, isolation, integrity, provenance (→ [`evaluation.md`](evaluation.md)) | Medium | §11 |

**The field's own recurring critique, in one line:** most memory benchmarks are **conversational QA where the question itself signals what to retrieve, scored on accuracy alone, ignoring cost** — and that is exactly what the 2026 wave (DolphinBench, "What Should an Agent Remember", Mem2ActBench, VibeMemBench) is trying to escape. [high]

---

## 1. Retrieval / recall quality — and the retention/selection split

### 1.1 The recall core
- **IR + QA metrics:** recall@k, precision, MRR, nDCG; QA F1 / accuracy (often LLM-judged). These are the PI SciSpace template's M05–M08 (retrieval) and M01–M04 (task/accuracy).
- **Long-term dialogue recall:** LoCoMo (arXiv:2402.17753), LongMemEval (arXiv:2410.10813), **DiaLong** (reminiscence in long-context dialogue, 100 human convos, arXiv:2610.25463), BEAM (up to 10M tokens, arXiv:2510.27246).
- **Caveat:** LoCoMo/LongMemEval are **near saturation** (91.4% in arXiv:2512.12818) and vendor numbers on them are not comparable (Zep 84% vs Mem0 58% re-run — [`evaluation.md`](evaluation.md) §4.6). Recall accuracy alone is no longer discriminative.

**Metrics.**
- `Recall@k = |relevant ∩ retrieved_k| / |relevant|` · `Precision@k = |relevant ∩ retrieved_k| / k`
- `MRR = (1/|Q|) Σ_q 1/rank_q` (rank of first relevant) · `MAP = (1/|Q|) Σ_q AP_q`
- `nDCG@k = DCG@k / IDCG@k`, where `DCG@k = Σ_{i=1..k} rel_i / log2(i+1)`
- QA: `EM` (exact match); token-`F1 = 2PR/(P+R)`; **QA accuracy (LLM-judge)** = fraction judged correct (inherits judge-validity caveat §10).

### 1.2 Disentangling retention from retrieval (the conceptual advance)
Memory competence is two decisions, and conflating them confounds benchmarks:
- **"What Should an Agent Remember?"** (arXiv:2610.00366) crosses **retention** (what to keep as info arrives) × **selection** (what to surface at query) on 300 seeded episodes; holding access fixed, query-aware selection lifts required-fact recall **+15.5pp** (95% CI reported). A model of how to separate the two.
- **"Stale, Misattributed, or Late"** (arXiv:2610.10265) measures **pre-generation** failures — obsolete value / wrong person / missed serving deadline — showing temporal validity is primarily a *construction*-time property, not a retrieval one.
- **MemBubble** (arXiv:2610.25127) adds a side-effect axis: memory-driven personalization can **reduce response diversity** (a filter-bubble cost that accuracy never captures).

**Metrics.**
- **Retention coverage** = (required facts retained) / (required facts) — a *construction*-time property.
- **Selection precision/recall** at query time, holding the store fixed; "What Should an Agent Remember" reports required-fact recall `Δ = +15.5pp` from query-aware selection vs recency.
- **Pre-generation failure rate** (Stale/Misattributed/Late) = fraction of memory blocks that are obsolete ∨ wrong-entity ∨ past-deadline before generation.
- **Response diversity** (MemBubble): `distinct-n` = unique n-grams / total n-grams, or entropy `H = −Σ p_i log p_i`; memory effect `= diversity_with − diversity_without`.

---

## 2. Memory dynamics

### 2.1 Update / staleness / freshness
- Knowledge-update accuracy (LongMemEval), FactConsolidation (MemoryAgentBench, arXiv:2507.05257), **FAMA** forgetting-aware accuracy penalizing obsolete-memory use (Memora, arXiv:2604.20006), **STALE** implicit invalidation Type I/II (arXiv:2605.06527), per-fact age trajectories (MemTrace, arXiv:2606.17328).
- **PACMI** (arXiv:2610.05732): provenance-aware **cascading invalidation** — dependency tracking of downstream records when a memory goes stale, while preserving it as historical evidence. (Bridges freshness ↔ provenance; also relevant to G1 retain-vs-erase.)

**Metrics.**
- **Knowledge-update accuracy** = accuracy on items whose answer changed after an update.
- **Stale-use rate** = (answers relying on superseded memory) / (answers) — lower is better.
- **FAMA** (Forgetting-Aware Memory Accuracy, arXiv:2604.20006): conceptually `accuracy − λ · (obsolete-memory-use rate)` — penalizes reliance on invalidated memory; exact weighting per source.
- **STALE** (arXiv:2605.06527): per-dimension accuracy on implicit-invalidation Type I/II, premise resistance, invalidation-policy adaptation (IPA).
- **Cascade correctness** (PACMI): fraction of dependent records correctly invalidated on a source update, with historical-preservation rate.

### 2.2 Conflict / contradiction
- **MemConflict** (arXiv:2605.20926): ranks valid vs conflicting evidence; answer correctness often diverges from retrieval/ranking of valid memory. Contradiction detection = template M12.

**Metrics.**
- **Conflict-resolution rate** = (conflict cases where the valid fact is chosen) / (conflict cases).
- **MemConflict** separates answer quality from retrieval/ranking of valid memory (named CRS / UOCS / SEH@K / SRS; definitions not in abstract — verify in full text before use).
- **Contradiction rate** = fraction of outputs internally or memory-inconsistent (template M12).

### 2.3 Forgetting / selective retention
- Selective forgetting (MemoryAgentBench), **ForgetEval** control-plane ops supersede/release/purge (arXiv:2606.15903), **"Can Agents Forget When Asked?"** memory-unlearning benchmark for agents (arXiv:2610.18052). Note: in capability framing "forgetting" is often a *loss*; in governance it is a *requirement* — the sign flip is the G1 tension in miniature ([`evaluation.md`](evaluation.md) §3, PI template M16 vs M26).

**Metrics.**
- **Selective-forgetting accuracy** = correctly-removed to-forget items ∧ correctly-retained keep items (a joint rate, so a store that forgets everything does not win).
- **Retention loss / forgetting curve** (capability sense) = `a_before − a_after` on retained material (template M16).
- **ForgetEval**: per-category pass rate for supersede / release / purge, with $/run and latency.
- Governance forgetting (erasure completeness, deletion-recovery, `leak@k`) → §11 / [`evaluation.md`](evaluation.md) §3.

---

## 3. From recall to action / decision (the most consequential shift)

Recall ≠ competence. The strongest 2026 finding is that QA scores overstate real memory utility:
- **MemoryArena** (arXiv:2602.16313): near-perfect LoCoMo collapses to **40–60% on decision tasks**.
- **Mem2ActBench** (arXiv:2601.19935): applying memory to tool **actions** (selection/argument grounding), not passive QA.
- **VibeMemBench** (arXiv:2609.23570): does memory improve **executable repository coding** (111 targets from SWE-rebench)? Isolates memory's downstream effect, which repo benchmarks and recall benchmarks each miss.
- **DolphinBench** (arXiv:2609.24971): real-world actions depending on recall over time; explicitly rejects the "question signals the fact to retrieve" format and scores on the **Pareto frontier** (see §5).
- **Retrieval admissibility** — **"The Right Memory in the Wrong Context"** (arXiv:2610.07309): a memory can be *relevant but inadmissible* (another principal, policy, lifecycle state); recall and final-answer accuracy hide it. This is the capability-side framing of the project's isolation/governance concern — worth citing as the bridge between the two branches. [high relevance to the project]

**Metrics.**
- **Goal-completion / task-success rate** `GCR = successes / tasks`.
- `pass@k = 1 − C(n−c, k)/C(n, k)` (≥1 of k succeeds; optimistic) vs **`pass^k`** = P(all k succeed) (worst-case; the right one for high-stakes — [`eval-procedural-skills.md`](eval-procedural-skills.md)).
- **Decision accuracy** on decision (not QA) items (MemoryArena).
- **Tool-selection / argument-grounding accuracy** (Mem2ActBench).
- **Memory lift** `Δ = metric_with_memory − metric_without` (VibeMemBench resolve-rate on SWE-rebench targets).
- **Inadmissible-exposure rate** = requests where inadmissible memory entered the prompt (2610.07309) — note a correct answer can still fail this.

---

## 4. Continual / test-time learning
- **Evo-Memory** (arXiv:2511.20857): self-evolving memory across a task stream. **ReTTT** (arXiv:2610.23942): reflection-driven test-time training into parametric memory. **Memp** (arXiv:2508.06433): build/retrieve/update with deprecation.
- Framing finding: **"Are Self-Evolving Agents Continual Learners?"** (arXiv:2610.25858) casts memory evolution as continual learning — so the metrics of interest become forward transfer and **catastrophic forgetting of earlier tasks**, not single-task success.

**Metrics** (continual-learning canon, Lopez-Paz & Ranzato; `a_{i,j}` = accuracy on task j after training through task i):
- **Average accuracy** `ACC = (1/T) Σ_i a_{T,i}`.
- **Backward transfer** `BWT = (1/(T−1)) Σ_{i<T} (a_{T,i} − a_{i,i})` — negative = catastrophic forgetting.
- **Forward transfer** `FWT = (1/(T−1)) Σ_{i>1} (a_{i−1,i} − b_i)` — gain on unseen tasks vs random baseline `b_i`.
- **Stream success** = success rate over the task stream at test time (Evo-Memory).

## 5. Cost / efficiency / the Pareto frontier (the under-reported axis)
- **MERIT** (arXiv:2609.05441): marginal utility of memory with **$ and tokens per operation** on a preregistered grid.
- **DolphinBench** (arXiv:2609.24971): maps the **accuracy–cost Pareto frontier**, refusing to let systems buy accuracy with unreasonable cost/latency — directly answers the pitfall that "benchmarks rarely require anything beyond accuracy."
- **"Persistent Memory in Multi-Agent Inference: What It Costs, What It Buys"** (arXiv:2610.07782): a persistent tier bought **no** accuracy at n=100/arm and added cost — a cautionary null.
- Template M13–M15 (latency, tokens, storage); write-path cost can flip conclusions (MemDelta, per Consensus review). **Few governance benchmarks report cost jointly with CIs** (GateMem and MERIT are the exceptions — [`evaluation.md`](evaluation.md) §3).

**Metrics.**
- **Raw cost:** tokens/op, `$`/op, **latency p95/p99**, storage footprint (MB); include *write-path* cost, not just read.
- **Accuracy-per-cost** `= accuracy / cost` (cost-normalized score).
- **Marginal utility** (MERIT) `= (success_with − success_without) / cost_added`.
- **Pareto-optimality** (DolphinBench): point `(acc, cost)` is on the frontier iff no other point has `acc' ≥ acc` ∧ `cost' ≤ cost` (one strict); report the frontier, not a single number.

## 6. Personalization / user modeling
- **ColaBench** (arXiv:2610.30989): memory-guided **knowledge acquisition** — identify needed external knowledge from history *and* apply it to the user's circumstances.
- **"Why Bother Me Again?"** (arXiv:2610.30485): interaction-preference memory. **CUE-Mem** (arXiv:2609.32574): long-term user memory via **implicit cues** in multimodal conversations. **PDEU-Bench** (arXiv:2609.34930): personalized planning lifecycle for tool-calling agents. **FinPerMA** (arXiv:2608.04095): investor-preference memory with post-shock update (the finance instance).
- Template M24 (personalization). Persona-as-skill risks sit in [`eval-procedural-skills.md`](eval-procedural-skills.md) / skills §2.1.

**Metrics.**
- **Personalized / suitability accuracy** = fraction of responses appropriate to the user's stated/implied circumstances (ColaBench scores knowledge-selection *and* situated application).
- **Preference-consistency rate** = fraction of turns consistent with the user's known preferences; **re-ask rate** (Why Bother Me Again) = fraction of already-known preferences re-queried (lower is better).
- **Implicit-cue recall** (CUE-Mem) = recall of user facts inferable only from implicit multimodal cues.
- Pair with **response-diversity** (§1.2) to guard against filter-bubble over-personalization.

## 7. Procedural / skills
Fully in [`eval-procedural-skills.md`](eval-procedural-skills.md) (SkillEvolBench, EngramBench, RSE-Bench, regression gates, retrieval-at-scale, formation quality). Cross-ref only.

## 8. Multimodal / embodied / spatial memory (fast-emerging)
- **DSV-Mem** (arXiv:2610.08102): multimodal memory in professional workflows with revisions and authority updates. **CUE-Mem** (multimodal implicit cues). **"Retrieved but Not Delivered"** (arXiv:2609.32590): multimodal memory delivery.
- Embodied/spatial: **EmbodiedMemory-Bench** (arXiv:2609.28236), **EMBER-Bench** cross-event causal memory (arXiv:2610.05013), **4DMemory** spatiotemporal (arXiv:2610.32332), **ProactEgoMem** proactive memory in streaming egocentric video (arXiv:2610.30089), OpenVLHarness (arXiv:2610.26860). Mostly out-of-scope for finance but they pioneer *decision/causal* memory metrics worth borrowing.

**Metrics.**
- **Delivery rate** (Retrieved but Not Delivered) = (memories retrieved *and* correctly used) / (relevant memories) — exposes the retrieve→use gap.
- **Cross-event causal accuracy** (EMBER) = accuracy on questions requiring linking causally-related events across the horizon.
- **Spatiotemporal recall** (4DMemory) = recall conditioned on (location, time); **proactive-trigger precision/recall** (ProactEgoMem) for firing on the right future cue.

## 9. Operation-level diagnosis & reliability framing
- **EvalMem** (arXiv:2609.22231): diagnoses *where* memory fails — encoding vs retrieval vs generation (per-examiner pass rates). The diagnostic complement to end-to-end scores.
- **MEMTRACK** (arXiv:2510.01353): state tracking across multi-platform events (correctness, efficiency, redundancy).
- **Agentic Cognitive Depth** (arXiv:2610.04168): trajectory-level criteria beyond success (context sensitivity, temporal continuity, metacognition).
- **TWIST** (arXiv:2609.28575): intervention quality in conversational memory (human-validated) — quality, not just recall.

**Metrics.**
- **Per-stage pass rate** (EvalMem): `encode-pass`, `retrieve-pass`, `generate-pass` — localizes *where* a failure occurs rather than only that it occurred.
- **Redundancy rate** (MEMTRACK) = duplicated/near-duplicate stored items / total.
- **Cognitive-depth profile** (Agentic Cognitive Depth): per-criterion scores C/T/M/A/Mc, reported as a vector, not a scalar.

## 10. Judge / reward-model-based evaluation
- **MemoryRewardBench** (arXiv:2601.11969): can reward models judge memory management? Relevant because so many memory benchmarks are LLM-judged.
- **Judge-validity caveats** (carry from [`evaluation.md`](evaluation.md) §4.3): validity compounds ≤ V1·V2·V3; ~82% of surveyed papers use mismatched/absent IRR. Any memory benchmark with an LLM judge inherits this.

**Metrics.**
- **RM/judge accuracy** = agreement with human/gold labels on memory-management decisions (MemoryRewardBench).
- **Inter-rater reliability** `IRR` = Cohen's κ (2 raters) or Krippendorff's α (≥2); report it or the score is uncalibrated.
- **Compounded validity** upper bound `V ≤ V_gen · V_sim · V_judge` across task-generation, user-simulation and judgment stages.

## 11. Governance / trustworthiness (the already-synthesized branch)
Full treatment in [`evaluation.md`](evaluation.md): privacy/isolation (CIMemories, PersistBench, AgentLeak, GateMem), erasure (ForgetEval, Ghost Echoes, leak@k, TOFU/MUSE), integrity/poisoning (AgentPoison, MemSecBench, MemForm arXiv:2610.14431), provenance/audit (DEMM-Bench, Fiducia-bench), and the operations × governance-properties matrix. Note the capability↔governance bridges surfaced above: **retrieval admissibility** (arXiv:2610.07309) ≈ isolation; **PACMI** ≈ freshness+provenance; **forgetting** sign-flip ≈ G1.

**Metrics** (representative; full set in [`evaluation.md`](evaluation.md) §3):
- Isolation: **`Violation@n`** = worst-case leakage over n tasks (CIMemories); **CSLR** = cross-scope canary-hit rate (target 0); Channel Leakage Rate (AgentLeak).
- Erasure: **erasure completeness** `EC = 1 − (recoverable after delete)/(deleted)`; **`leak@k`** = P(unlearned content resurfaces in k samples); deletion-recovery leakage.
- Integrity: **`ASR`** variants `= successful attacks / attempts` (ASR-r retrieval, ASR-a action, ASR-t target) with benign-utility cost.
- Provenance: **lineage coverage** `MLC = (records with complete lineage)/(records)`; property-sufficiency accuracy (DEMM-Bench).
- These are **worst-case / tail** metrics by design — the opposite of the mean-accuracy habit in §§1–3.

## 12. Meta-evaluation & validity pitfalls (apply to all of the above)
Carried from [`evaluation.md`](evaluation.md) §4, with the capability-side additions:
1. **QA-signal leakage:** the question reveals what to retrieve → inflated recall; fixed by action/stream formats (DolphinBench, Mem2ActBench, "What Should an Agent Remember").
2. **Accuracy-only / cost-gaming:** systems buy accuracy with cost/latency unless the frontier is scored (DolphinBench, MERIT).
3. **Recall ≠ decision competence** (MemoryArena 40–60%).
4. **Saturation & non-comparable vendor numbers** (LoCoMo/LongMemEval).
5. **Harness dependence** (memory effects reverse across harnesses, arXiv:2607.27080).
6. **Judge validity compounds** (§10).
7. **Mostly synthetic & LLM-labeled**; construct validity vs real deployment unestablished.
8. **Pre-generation failures hidden by final-answer scoring** (Stale/Misattributed/Late).

## 13. Metric families (reference; maps to PI SciSpace template M01–M26)
Task/accuracy (M01–04) · retrieval IR (M05–08) · completeness/integrity (M09–10) · factuality/contradiction (M11–12) · efficiency: latency/tokens/storage (M13–15) · continual learning (M16–20) · procedural (M21–22) · temporal consistency (M23) · personalization (M24) · safety/privacy (M25–26). The template is **24/26 utility-side, 2/26 governance** — i.e. it is a good skeleton for §§1–9 and must be paired with [`evaluation.md`](evaluation.md) for §11. **Formulas for the representative metrics live inline under each silo (§§1–11).** The minimum-reporting rule (N, CIs, baseline, k, judge+rubric, latency percentile, memory-store version) applies throughout.

## 14. Maturity, crowding, and gaps (my read; confidence bracketed)
- **Crowded & saturating:** long-term dialogue recall (§1.1). Stop proposing recall-only benchmarks. [high]
- **Hottest, highest-value:** action/decision grounding (§3), cost/Pareto (§5), personalization (§6) — all moving from "recall" to "useful, affordable, situated." [high]
- **Under-built:** operation-level diagnosis (§9), judge-of-memory validity (§10), retention/selection disentanglement (§1.2). [medium]
- **Project-relevant bridges:** retrieval **admissibility** (arXiv:2610.07309) and provenance-aware invalidation **PACMI** (arXiv:2610.05732) are capability-framed versions of the project's isolation and freshness/provenance concerns — citing them lets the governance contribution land in the capability community's vocabulary. [high]
- **Still empty:** a benchmark that is simultaneously **action-grounded + cost-aware + governance-scored + finance-situated** — the intersection the project targets (unchanged from [`evaluation.md`](evaluation.md) §7 and [`eval-procedural-skills.md`](eval-procedural-skills.md) §3). [high]

**Recommendation.** Use this as the evaluation *landscape* section; keep [`evaluation.md`](evaluation.md) as the governance deep-dive and [`eval-procedural-skills.md`](eval-procedural-skills.md) as the procedural deep-dive. The one framing worth adopting project-wide: **score memory on the accuracy–cost Pareto frontier of a decision/action task, with a governance overlay** — DolphinBench + MemoryArena + GateMem fused, in finance.

---

## 15. Query plan (reusable by `/radar`, facet `memory-eval`)

| Sub-facet | arXiv (`lit.py arxiv --since`) | SciSpace |
|---|---|---|
| Recall / long-term | `("long-term memory" OR multi-session) benchmark (LLM OR agent OR dialogue)` | "benchmarks for long-term conversational memory" |
| Retention vs selection | `(retention OR "what to remember" OR "bounded memory") agent benchmark` | — |
| Dynamics | `(staleness OR "knowledge update" OR conflict OR invalidation OR forgetting) memory benchmark agent` | "how is memory staleness/conflict/forgetting evaluated" |
| Action / decision | `agent memory benchmark (decision OR action OR tool OR executable OR downstream)` | "benchmarks measuring whether memory improves agent decisions not QA" |
| Cost / Pareto | `agent memory (cost OR efficiency OR latency OR Pareto OR "marginal utility") benchmark` | — |
| Personalization | `personal* memory benchmark agent (preference OR user OR situated)` | — |
| Multimodal / embodied | `(multimodal OR embodied OR egocentric OR spatial) memory agent benchmark` | — |
| Diagnosis / judge | `(operation-level OR diagnosis OR "reward model") memory evaluation agent` | — |
| Governance | → reuse [`evaluation.md`](evaluation.md)/[`partials/evaluation.md`](partials/evaluation.md) query plan |

# Evaluation methods, benchmarks and metrics for agent memory governance

Facet tag: `evaluation`. Cleaned at synthesis on 2026-09-24 from `partials/evaluation.md`, which also holds the query plan for `/radar`. The main review is `review.md`: §2 is the operations × properties matrix and §8 the convergent gaps.
- **Recency.** arXiv was searched `--since 2025-06-01`, with results up to 2026-09-22. SciSpace has no hits after about 2026-01. Foundations have no date limit. Web sources were accessed 2026-09-24.
- **Records.** 170 library records carry the `evaluation` tag. 16 of them are evaluation-`core`, with notes in `literature/notes/`.
- **Read levels.** "full" means arXiv HTML read through a fetch tool that returns an extracted summary. "(abstract)" means the claim rests on the abstract only.

**Synthesis edits.**
- Added arXiv:2605.14744 (§2d). It was untagged in the library and tagged at synthesis; per abstract only.
- Cross-referenced the MemClaw path-dependent leakage result (arXiv:2606.24535; verified against the full text by the orchestrator) in the isolation row of §3.
- Snowballing note: forward citation snowballing was not run for this facet because of arXiv rate limits. Backward snowballing from the key benchmarks was run.

Section numbers follow the partial. §1, the query plan, is in `partials/evaluation.md`.

---

## 2. Benchmark catalog


Columns: **Mem?** = does the benchmark exercise persistent/long-term memory. **Gov?** = which governance dimension it measures, if any (P = privacy/isolation, E = erasure/forgetting-on-request, F = freshness/staleness, I = integrity/poisoning, A = provenance/audit, C = rule/policy compliance). **Fin?** = finance data or tasks. Availability was taken from the paper where I read it; "n/r" = not recorded (abstract only).

### 2a. General agent evaluation and safety

| Name | Year | What it measures | Metrics | Data | Mem? | Gov? | Fin? | Availability | id |
|---|---|---|---|---|---|---|---|---|---|
| HELM | 2022 | Holistic LM eval across scenarios × metrics | accuracy, calibration, robustness, fairness, toxicity, efficiency | many public datasets | no | – | partial | open | arXiv:2211.09110 |
| AgentBench | 2023 | LLM-as-agent across 8 environments | success rate | synthetic/sim envs | no | – | no | open | arXiv:2308.03688 |
| τ-bench / τ²-bench | 2024/25 | Tool-agent-user tasks under domain policy docs | DB end-state match; **pass^k** | simulated users; retail/airline/telecom | no | C | no | open | arXiv:2406.12045, arXiv:2506.07982 |
| METR time horizon | 2025 (TH1.1 2026) | Task length (human time) at 50%/80% agent success | logistic fit → time horizon | SW/research tasks | no | – | no | tasks partly private | arXiv:2503.14499; metr.org |
| HAL (Holistic Agent Leaderboard) | 2025 | Standardized harness, cost-aware multi-benchmark | accuracy vs $ cost; log inspection | 9 benchmarks, 21,730 rollouts | no | – | no | open | arXiv:2510.11977 |
| AgentHarm | 2024 | Harmful multi-step agent tasks; jailbreak robustness | harm score, refusal rate | 110 (440 aug.) synthetic tasks, 11 harm categories | no | – | fraud category | HF (UK AISI) | arXiv:2410.09024 |
| ST-WebAgentBench | 2024 | Safety/trust policy adherence of web agents (enterprise) | **Completion under Policies** (CuP) | WebArena-based | no | C | no | open | arXiv:2410.06703 |
| Agent-SafetyBench | 2024 | 8 risk categories, 10 failure modes | safety score | 349 envs, 2,000 cases | no | – | no | GitHub | arXiv:2412.14470 |
| R-Judge | 2024 | Can LLMs judge risk in agent traces | F1 / accuracy vs human labels | 162 records | no | – | no | GitHub | arXiv:2401.10019 |
| AgentDojo / InjecAgent | 2024 | Prompt-injection robustness with utility | ASR, benign utility, utility-under-attack | synthetic tool envs | no | I | banking suite (AgentDojo) | open | arXiv:2406.13352, arXiv:2403.02691 |
| PBSuite | 2025 | Multi-turn adherence to custom org behavioral policies | failure rate | 300 policies, 30 industries | no | C | yes (industry policies) | n/r | arXiv:2511.05018 |
| SafeClawBench | 2026 | Separates semantic, audit-evidence and sandbox harm | staged ASR | 600 adversarial tasks incl. memory writes | partial | I, A | no | n/r | arXiv:2606.18356 |
| AgentLAB | 2026 | Adaptive long-horizon attacks incl. memory poisoning | ASR | synthetic | partial | I | no | n/r | arXiv:2602.16901 |
| READY | 2026 | Enterprise deployment qualification (reliability, oversight, cost) | qualification procedure over workflow success | enterprise workflows | no | – | no | n/r | arXiv:2609.02095 |

### 2b. Memory benchmarks

| Name | Year | What it measures | Metrics | Data | Mem? | Gov? | Fin? | Availability | id |
|---|---|---|---|---|---|---|---|---|---|
| LoCoMo | 2024 | Very long-term dialogue memory (~300 turns, up to 35 sessions) | QA F1, event summarization, multimodal generation | LLM-generated + human-edited | yes | – | no | open | arXiv:2402.17753 |
| LongMemEval | 2024 | Extraction, multi-session, temporal, **knowledge update**, **abstention** | QA accuracy (LLM judge), recall@k | 500 Qs in scalable chat histories | yes | F (update) | no | open | arXiv:2410.10813 |
| LongMemEval-V2 | 2026 | Environment-experience memory for web agents | task/QA accuracy (abstract) | web envs | yes | – | no | n/r | arXiv:2605.12493 |
| MemBench | 2025 | Factual vs reflective memory, participation vs observation | accuracy, recall, capacity, efficiency | synthetic | yes | – | no | open | arXiv:2506.21605 |
| MemoryAgentBench | 2025 | Accurate retrieval, test-time learning, long-range understanding, **selective forgetting** | accuracy/F1/Recall@5 | 2,071 Qs, 103K–1.44M tokens; new EventQA, FactConsolidation | yes | F | BANKING77 only | MIT code / CC BY data | arXiv:2507.05257 |
| BEAM ("Beyond a Million Tokens") | 2025 | Coherent conversations up to 10M tokens, broad memory abilities | per-ability accuracy | synthetic | yes | F | no | n/r | arXiv:2510.27246 |
| MEMTRACK | 2025 | Memory and state tracking across multi-platform (Slack/Linear/Git-like) events | correctness, efficiency, redundancy (abstract) | synthetic enterprise | yes | F | no | n/r | arXiv:2510.01353 |
| Evo-Memory | 2025 | Test-time learning with self-evolving memory across task streams | task success over stream | multiple datasets | yes | – | no | n/r | arXiv:2511.20857 |
| Mem2ActBench | 2026 | Applying memory to tool actions, not passive QA | tool selection / argument grounding | synthetic | yes | – | no | n/r | arXiv:2601.19935 |
| Memora (+ FAMA metric) | 2026 | Remember / reason / recommend over weeks–months | **Forgetting-Aware Memory Accuracy** (penalizes obsolete memory use) | synthetic + human checks | yes | F | no | n/r | arXiv:2604.20006 |
| MemConflict | 2026 | Ranking valid vs conflicting memory evidence | fitness-for-use diagnostics (abstract) | synthetic | yes | F | no | n/r | arXiv:2605.20926 |
| STALE | 2026 | Implicit invalidation (Type I/II); premise resistance; policy adaptation | accuracy per dimension (LLM judge, 95.8% human agreement) | 400 scenarios / 1,200 queries, ≤150K tokens | yes | F | no | CC BY 4.0 | arXiv:2605.06527 |
| MemTrace | 2026 | Per-fact ("knowledge point") behavior vs memory age etc. | per-fact trajectories | synthetic | yes | F | no | n/r | arXiv:2606.17328 |
| EvalMem | 2026 | Operation-level diagnosis: encoding vs retrieval vs generation | per-examiner pass rates | existing benchmarks | yes | – | no | n/r | arXiv:2609.22231 |
| MERIT | 2026 | Marginal utility of memory for tool-using agents, with **cost metering** | dependent-task success, $ and tokens per op, corruption | 23,440 episodes, preregistered grid | yes | F, I (corruption) | no | n/r | arXiv:2609.05441 |
| ForgetEval | 2026 | Control-plane forgetting ops (supersede / release / purge) | category pass rate, $/run, latency | 1,000 templated + 385 adversarial | yes | **E**, F | no | n/r | arXiv:2606.15903 |
| Agent-native memory study | 2026 | Data-management view: storage, extraction, retrieval, maintenance cost | accuracy + system cost | 12 systems × 5 workloads | yes | F | no | n/r | arXiv:2606.24775 |
| GroupMemBench | 2026 | Multi-party / group memory | QA accuracy (abstract) | synthetic | yes | P (partial) | no | n/r | arXiv:2605.14498 |
| DynamicMem | 2026 | Drifting heterogeneous profiles over months | accuracy (abstract) | synthetic | yes | F | no | n/r | arXiv:2606.22877 |
| LoCoMo-Plus | 2026 | Latent constraints under cue–trigger disconnect | judge-based | extends LoCoMo | yes | – | no | n/r | arXiv:2602.10715 |
| FinPerMA | 2026 | Event-grounded investor preference memory (post-shock update) | accuracy; MCQ accuracy | 2,994 Qs, 276 personas, synthetic | yes | F | **yes** | n/r | arXiv:2608.04095 |
| MemoryRewardBench | 2026 | Can reward models judge memory management | RM accuracy | 8K–128K contexts | yes | – | no | n/r | arXiv:2601.11969 |

### 2c. Trustworthiness and memory-governance evaluation

| Name | Year | What it measures | Metrics | Data | Mem? | Gov? | Fin? | Availability | id |
|---|---|---|---|---|---|---|---|---|---|
| DecodingTrust | 2023 | 8 trust dimensions incl. privacy (PII, training-data leakage) | per-dimension scores | public + synthetic | no | P | no | open | arXiv:2306.11698 |
| TrustLLM | 2024 | 6 dims: truthfulness, safety, fairness, robustness, privacy, ethics | 30+ datasets | public | no | P | no | open | arXiv:2401.05561 |
| Carlini et al. extraction | 2020 | Training-data extraction | # verbatim memorized extractions | GPT-2 | no | P | no | – | arXiv:2012.07805 |
| ConfAIde | 2023 | CI reasoning, 4 tiers | leakage rate, correlation with human norms | vignettes | no | P | no | open | arXiv:2310.17884 |
| PrivacyLens (+ Live) | 2024/25 | CI in agent actions (seed → vignette → trajectory) | leak rate, helpfulness | crowdsourced seeds | no | P | no | open | arXiv:2409.00138, arXiv:2509.17488 |
| MAGPIE | 2025 | Multi-agent CI where private info is task-essential | leakage %, task completion, manipulation | 200 tasks | no | P | partial | n/r | arXiv:2510.15186 |
| CI-Work | 2026 | Enterprise information flows (up/down/lateral/external) | Leakage Rate, Violation Rate, **Conveyance Rate** | 125 seeds / 1,000 entries | no | P | financial info types | aka.ms/ci-work | arXiv:2604.21308 |
| MPCI-Bench | 2026 | Multimodal paired CI (privacy–utility pairs) | paired accuracy | synthetic | no | P | no | n/r | arXiv:2601.08235 |
| **CIMemories** | 2025 | CI of persistent memory across many tasks | **Violation@n**, Completeness | 10 profiles × ~147 attrs × 46 contexts | yes | P | finance attributes | CC BY-NC-SA | arXiv:2511.14937 |
| **PersistBench** | 2026 | Cross-domain memory leakage, memory sycophancy, beneficial use | Failure Rate (judge) | 500 human-verified | yes | P | no | CC BY 4.0 | arXiv:2602.01146 |
| PrivacyBench | 2025 | Secret preservation in RAG personal assistants | leak % per interaction (abstract) | socially grounded synthetic | yes (RAG) | P | no | n/r | arXiv:2512.24848 |
| **AgentLeak** | 2026 | Leakage across 7 channels incl. shared memory | ELR, CLR, ASR, TSR | 1,000 scenarios, 4,979 traces | yes (C5) | P | **yes** | CC BY 4.0 | arXiv:2602.11510 |
| CalBench / OCELOT | 2026 | Coordination–privacy trade-off; cumulative inference-leakage budgets | leakage vs cost | synthetic | no | P | no | n/r | arXiv:2605.09823, arXiv:2606.12341 |
| **GateMem** | 2026 | Multi-principal shared memory: utility, access control, active forgetting | **MGS = U·(1−A)·(1−F)**, over-refusal, cost | 91 episodes / 2,218 checkpoints | yes | P, E | no | GitHub/HF | arXiv:2606.18829 |
| SovereignPA-Bench | 2026 | Personal agents: privacy, consent, evidence, manipulation resistance | multi-dim (abstract) | executable | yes | P, C | no | n/r | arXiv:2607.05363 |
| Forgetful but Faithful (MaRS) | 2025 | Privacy-aware retention/forgetting policies | 6 forgetting-policy metrics (abstract) | synthetic | yes | E, P | no | n/r | arXiv:2512.12856 |
| TOFU / MUSE | 2024 | Unlearning (fictitious authors; six-way eval) | forget quality, model utility, MIA/privacy leakage | synthetic / news, books | no (weights) | E | no | open | arXiv:2401.06121, arXiv:2407.06460 |
| leak@k | 2025 | Unlearned knowledge resurfacing under sampling | **leak@k** | TOFU/MUSE/WMDP | no | E | no | – | arXiv:2511.04934 |
| Athena | 2020 | Hypothesis-testing verification of deletion (backdoor canaries) | FP/FN of verification | image/text models | no | E | no | – | arXiv:2003.04247 |
| **Ghost Echoes** | 2026 | Residual influence of deleted vectors (HNSW) | centroid drift, vocab shift, latency oracle | 500 synthetic records; 5 vector DBs | yes (vector store) | **E** | no | synthetic only | arXiv:2608.20352 |
| Agentic unlearning (SBU) | 2026 | Joint parameter + memory unlearning; "backflow" | forget/retain accuracy (abstract) | medical QA | yes | E | no | n/r | arXiv:2602.17692 |
| AgentPoison / PoisonedRAG | 2024 | Memory/KB poisoning | ASR-r (retrieval), ASR-a (action), ASR-t (target), benign acc. | QA/driving/EHR agents | yes | I | no | open | arXiv:2407.12784, arXiv:2402.07867 |
| **MemSecBench** | 2026 | Poisoning lifecycle: write → execute → selective repair | MPSR, MESR, E2E-ASR, **SRSR** | 310 packages, 24 configs | yes | I, E (repair) | no | released | arXiv:2607.27080 |
| MemEvoBench | 2026 | Memory "misevolution" drift under misleading exposure | safety drift (abstract) | synthetic | yes | I | no | n/r | arXiv:2604.15774 |
| MemGauge / Price of Safety | 2026 | Stage-wise utility–risk trade-off; benign-traffic cost of defenses | clean vs poisoned utility and ASR; 95% CIs | 11 LLMs, 2 memory benchmarks | yes | I | no | n/r | arXiv:2608.30177, arXiv:2609.22818 |
| DEMM-Bench | 2026 | Are runtime records **sufficient** to reconstruct decision-level properties | Property Sufficiency Accuracy; overclaim rate | 64 cases, 8 evidence regimes | no | **A** | no | deposited package | arXiv:2606.20634 |
| Partial Evidence Bench | 2026 | Authorization-limited evidence: answers that look complete but are silently filtered | correctness, completeness awareness, gap-report quality, unsafe completeness | 72 tasks (incl. due diligence, compliance audit) | no | P, A | partial | n/r | arXiv:2605.05379 |
| ALCE / RAGAS | 2023 | Citation quality; RAG faithfulness | citation recall/precision; faithfulness, context precision | QA | no | A | no | open | arXiv:2305.14627, arXiv:2309.15217 |
| Cited-but-not-verified | 2026 | Source attribution in deep-research reports | citation validity rates | parsed reports | no | A | no | n/r | arXiv:2605.06635 |
| RegOps-Bench (RefWalk) | 2026 | Regulatory compliance QA with per-rule attribution | retrieval recall, citation accuracy | national R&D regs + HIPAA | no | A, C | no | n/r | arXiv:2605.29742 |
| OmniCompliance-100K | 2026 | Rule-grounded real-world compliance cases | classification accuracy | 74 regulations, 12,985 rules, 106,009 cases (incl. financial security) | no | C | partial | n/r | arXiv:2603.13933 |
| LogiSafetyGen | 2026 | Implicit regulatory compliance in tool calls (LTL oracles) | violation rate | fuzzed traces | no | C | no | n/r | arXiv:2601.08196 |
| MAC-Bench | 2026 | Procedural compliance under pressure (Goodhart) in multi-agent systems | violation rates | dynamic | no | C | no | n/r | arXiv:2606.07805 |
| Bench-2-CoP | 2025 | Coverage of EU AI Act Code of Practice risks by existing benchmarks | coverage share | 194k benchmark items (abstract) | no | C (meta) | no | n/r | arXiv:2508.05464 |

### 2d. Finance agent benchmarks with safety / compliance dimensions

| Name | Year | What it measures | Metrics | Data | Mem? | Gov? | Fin? | Availability | id |
|---|---|---|---|---|---|---|---|---|---|
| FinanceBench | 2023 | Financial QA over filings (capability baseline) | accuracy | real filings | no | – | yes | open sample | arXiv:2311.11944 |
| **FinVault** | 2026 | Execution-grounded financial agent security | ASR; benign false positives | 31 regulatory-case sandboxes, 963 cases | no (state DB) | I, C | yes | GitHub | arXiv:2601.07853 |
| **Fiducia-bench** | 2026 | Governability: escalate / abstain / audit trail under decomposition | governed success, fact attenuation, propagation loss, authority diffusion | KYC/AML, 100 synthetic tasks | no | C, A | yes | CC BY 4.0 | arXiv:2608.16055 |
| **ReguSim / ReguBench** | 2026 | Rule grounding of trading agents; LLM monitors | rejected attempts, breach %, monitor F1, false-accept | 191 scenarios, 49,440 synthetic records (US/CN/HK-inspired) | no | C, A | yes | promised | arXiv:2608.19974 |
| CNFinBench | 2025 | Capability–compliance–safety triad; multi-turn adversarial | HICS (Harmful Instruction Compliance Score) | Chinese finance | no | C | yes | n/r | arXiv:2512.09506 |
| FIN-Bench (RCA) | 2025 | Risk-concealment multi-turn red teaming | ASR (93.18% avg) | Chinese finance | no | C | yes | n/r | arXiv:2509.10546 |
| FinGuard | 2026 | Detect regulatory non-compliance in finance interactions | detection F1 (abstract) | Chinese regulations | no | C | yes | n/r | arXiv:2605.29427 |
| Price of Agreement | 2026 | Sycophancy in agentic finance | accuracy drop under rebuttal | finance tasks | no | – | yes | n/r | arXiv:2604.24668 |
| FinLake-Bench (Profit Mirage) | 2025 | Look-ahead information leakage in back-tests | leakage-robust returns | market data | no | (validity) | yes | n/r | arXiv:2510.07920 |
| FinEvo-Bench | 2026 | Longitudinal self-evolving agents on institution procedures | multi-aspect scores | 120 tasks, 6 domains | yes (experience) | C (procedures) | yes | n/r | arXiv:2608.06144 |
| FinToolBench / FinGAIA / AMA / StockBench / FinBench | 2025–26 | Capability: tool use, workflows, live trading, calibrated forecasting | accuracy; returns, drawdown, Sortino; calibration | real markets | AMA uses memory agent | – | yes | mostly open | arXiv:2603.08262, arXiv:2507.17186, arXiv:2510.11695, arXiv:2510.02209, arXiv:2607.16229 |
| Standard Benchmarks Fail (position) | 2025 | Argues finance agents should be audited on their risk profile | "safety budget" | 6 agents, 3 tasks | no | – | yes | – | arXiv:2502.15865 |
| Governance-task decoupling (mechanical enforcement) | 2026 | Rationale-level policy compliance, text-only vs mechanical governance | 5 governance metrics; uninformative deferrals 27% → reduced 73%; MCC 0.43 → 0.88 (abstract) | synthetic banking domain | no | C, A | yes | n/r | arXiv:2605.14744 |

---

## 3. Metrics taxonomy: governance property → existing metrics

| Governance property (finance reading) | Existing metrics (id) | Maturity | Where nothing exists (my observation) |
|---|---|---|---|
| **Retain-when-required** (keep records for the mandated period, e.g. record-keeping rules; do not "forget" regulated facts) | Recall/QA accuracy over long histories (arXiv:2402.17753, arXiv:2410.10813); per-fact age curves (arXiv:2606.17328); GateMem utility U (arXiv:2606.18829); CI "completeness"/"conveyance" (arXiv:2511.14937, arXiv:2604.21308) | Medium for recall | **No metric scores *mandated* retention**: whether a record that must be kept (and must stay retrievable for audit) survives consolidation, summarization or compression. arXiv:2609.05767 shows compression drops safety-critical facts. Every forgetting metric treats forgetting as always good. |
| **Forget-when-required** (erasure on request, purpose-limited retention) | GateMem F: post-deletion recovery rate (arXiv:2606.18829); ForgetEval category pass rates (arXiv:2606.15903); MemSecBench SRSR, which is repair without collateral loss (arXiv:2607.27080); Ghost Echoes centroid drift / latency oracle (arXiv:2608.20352); leak@k (arXiv:2511.04934); TOFU/MUSE forget quality + MIA (arXiv:2401.06121, arXiv:2407.06460); Athena hypothesis-test verification (arXiv:2003.04247) | Low–medium; fragmented | No protocol checks erasure **end-to-end across all derived artifacts** (summaries, embeddings, reflections, caches, logs, fine-tune data). arXiv:2602.17692 names this "backflow". Interface-level checks (GateMem) and index-level checks (Ghost Echoes) have never been combined. There is no statistical certification (confidence bound on residual influence) for memory stores. |
| **Isolation** (cross-client, information barriers/Chinese walls, role-based access) | Access-control violation A (arXiv:2606.18829); Violation@n (arXiv:2511.14937); cross-domain leakage FR (arXiv:2602.01146); Channel Leakage Rate incl. memory channel (arXiv:2602.11510); Leakage/Violation/Conveyance (arXiv:2604.21308); unsafe-completeness (arXiv:2605.05379); read-path-dependent leakage in production shared memory, 72/164 on semantic search vs 0/80 on propagation (arXiv:2606.24535, full; orchestrator-verified); extraction rate from RAG (doi:10.18653/v1/2024.findings-acl.267, arXiv:2411.14110) | Medium (active area) | No benchmark encodes **legal information-barrier rules** (e.g. research vs trading desk, MNPI) or cross-*client* isolation in a shared advisory memory. Enterprise CI (CI-Work) is the closest match but has no persistent memory. |
| **Integrity** (resistance to poisoning, no silent corruption) | ASR variants: AgentPoison ASR-r/a/t (arXiv:2407.12784); MPSR/MESR/E2E-ASR (arXiv:2607.27080); benign-case utility cost with CIs (arXiv:2609.22818); stage-wise utility–risk (arXiv:2608.30177); FinVault ASR + benign FP (arXiv:2601.07853) | Medium, but see validity problems (arXiv:2609.25173) | No agreed denominator or unit. Detection and **attribution** of poisoning (vs model failure) are unmeasured; arXiv:2605.22842 shows attribution systems blamed the model in all 64 cases. |
| **Provenance / auditability** (reconstruct who/what/why for a decision; record-keeping evidence) | DEMM-Bench Property Sufficiency Accuracy + overclaim (arXiv:2606.20634); Fiducia-bench audit-trail and authority diffusion (arXiv:2608.16055); citation precision/recall (arXiv:2305.14627, arXiv:2605.29742, arXiv:2605.06635); ReguSim evidence-hit and false-accept (arXiv:2608.19974); success-provenance audits (arXiv:2607.24054) | Low | No metric for **memory lineage**: can one trace an answer back to the memory writes (source, time, principal, consent basis) that caused it, and does that trace survive update and consolidation? |
| **Freshness** (stale KYC/suitability facts, superseded rules) | Knowledge-update accuracy (arXiv:2410.10813); FactConsolidation (arXiv:2507.05257); FAMA (arXiv:2604.20006); STALE SR/PR/IPA (arXiv:2605.06527); temporal misgrounding on versioned law (arXiv:2608.09393); FinPerMA post-shock (arXiv:2608.04095); AUROC of stale-vs-duplicate separation (arXiv:2606.26511) | Medium (fast-growing in 2026) | Freshness with respect to **external authoritative sources** (sanctions lists, regulatory changes) rather than in-conversation updates is untested for memory agents. |
| **Utility and cost** (governance must not destroy usefulness) | Task success; pass^k (arXiv:2406.12045); CuP (arXiv:2410.06703); over-refusal (arXiv:2606.18829); Conveyance (arXiv:2604.21308); $/token metering (arXiv:2609.05441, arXiv:2510.11977) | High for capability | Few governance benchmarks report utility, cost and a governance score **jointly with CIs**. GateMem and MERIT are the exceptions. |

---

## 4. Methodological pitfalls (with evidence)

1. **Outcome-validity exploits, especially free abstention.** ABC found flaws in 7 of 10 major agent benchmarks. On τ-bench, empty or "list-all" responses inflate scores by up to 38–40% (arXiv:2507.02825). In a privacy or forgetting benchmark, refusal is the trivial exploit, so over-refusal must be scored (GateMem does this; arXiv:2606.18829).
2. **ASR is underspecified.** 65.3% of 259 security papers report no variance; only 29.7% of judge-based papers validate the judge; at n=100 the minimum detectable difference is ≈18 pp (arXiv:2609.25173, analytical).
3. **Judge validity compounds.** Validity can fall to ≤ V1·V2·V3 across task generation, user simulation and judgment; ~82% of 55 papers use mismatched or absent IRR (arXiv:2608.00794). See also judge-reliability stress tests (arXiv:2603.05399, arXiv:2606.29920, arXiv:2609.12191) and the original MT-Bench judge biases (arXiv:2306.05685).
4. **Leaderboards rank specialization, not capability.** The agent main effect is <3% of variance on TheAgentCompany, τ²-bench and AppWorld (arXiv:2608.11323). Safety scores are confounded with capability, and F1 admits a constant baseline (0.690 on R-Judge, above 5 of 21 models) (arXiv:2607.28685).
5. **Contamination for agents that search.** Agents can retrieve benchmark answers during evaluation (arXiv:2606.05241, arXiv:2508.13180). HAL logs show agents searching HuggingFace for the benchmark (arXiv:2510.11977). Finance back-tests leak future information (arXiv:2510.07920).
6. **Vendor memory numbers are not comparable.** Zep reported 84% on LoCoMo; Mem0 re-ran it and got 58.44%; Zep's rebuttal gives 75.14% (GitHub getzep/zep-papers issue #5; Zep blog "Is Mem0 really SOTA", accessed 2026-09-24). A 2026 Mem0 blog lists vendor LoCoMo claims of 88–96%, several disputed. These are industry claims, not peer reviewed. LoCoMo/LongMemEval are nearing saturation (e.g., 91.4% LongMemEval in arXiv:2512.12818).
7. **Harness dependence.** Memory-backend safety effects reverse across harnesses (Mem0 ±13.5 pp E2E-ASR; arXiv:2607.27080). Results for a memory component alone do not transfer.
8. **Output-only auditing misses internal leaks.** 41.7% of traces with safe outputs leak via inter-agent messages or memory (arXiv:2602.11510).
9. **Stated ≠ enacted compliance.** Showing an LLM monitor the trader's rationale almost doubles false accepts (25% → 46.9%) (arXiv:2608.19974). Trace or schema presence overclaims evidence sufficiency in 75% of cases (arXiv:2606.20634).
10. **Greedy-decoding evaluation of forgetting is optimistic.** Knowledge resurfaces under sampling (leak@k, arXiv:2511.04934). Violations accumulate over tasks and samples (Violation@n, arXiv:2511.14937). API-level deletion checks pass 100% while semantic residue persists (arXiv:2608.20352).
11. **Nearly all governance benchmarks are synthetic and LLM-labeled.** Labels come from LLM personas (CIMemories) or LLM-drafted cases (MemSecBench, GateMem). Construct validity against actual legal obligations is not established. Bench-2-CoP reports that existing benchmarks barely cover the EU AI Act Code-of-Practice risk areas (arXiv:2508.05464, abstract).
12. **Metric definitions are time-bound.** Evaluation scores are "perishable knowledge claims" (arXiv:2607.26191, abstract). METR itself flags measurements above 16 h as unreliable and corrected a regularization error in March 2026 (metr.org/time-horizons, accessed 2026-09-24).

---

## 5. Industry evaluation practice and standards (web; accessed 2026-09-24)

- **UK AISI Inspect** (open-source eval framework, with Meridian Labs) and **inspect_evals** (200+ pre-built evals, incl. GAIA, SWE-bench, Cybench, AgentHarm; sandboxed agent tools and a trace viewer): https://inspect.aisi.org.uk/ ; https://github.com/UKGovernmentBEIS/inspect_evals ; https://www.aisi.gov.uk/blog/inspect-evals. It is the de facto government/lab harness and has no memory-governance evals as far as the listing shows (not exhaustively checked).
- **METR time horizons.** TH1.1 (Jan 2026) expanded to 31 long tasks. Methodology: fit a logistic curve of success vs human task time. There was a March 2026 correction, and measurements above 16 h are flagged unreliable: https://metr.org/time-horizons/ ; https://metr.org/blog/2026-1-29-time-horizon-1-1/ . Paper: arXiv:2503.14499.
- **HAL** (Princeton) is the academic counterpart of vendor harnesses: cost-aware, with log inspection (arXiv:2510.11977).
- **NIST AI RMF 1.0, MEASURE function** (US; voluntary framework, published Jan 2023). **NIST AI 600-1 Generative AI Profile** (July 2024) adds measurement actions for provenance, red-teaming, privacy, prompt-injection/poisoning resilience and TEVV construct validity: https://www.nist.gov/itl/ai-risk-management-framework . I did not read the official PDF; the subcategory details come from secondary summaries in search results. The regulation scout should cite the MEASURE subcategory numbers from the NIST text.
- **ISO/IEC 42001:2023** (AI management system; published international standard, certifiable) and **ISO/IEC 24029** robustness series: TR 24029-1:2021 overview; 24029-2:2023 formal methods (https://www.iso.org/standard/79804.html); 24029-3 statistical methods at DIS stage (https://www.iso.org/standard/86901.html). The texts are paywalled and I did not read them. None define memory-specific metrics as far as their public scope statements show.
- **Memory vendors** (Mem0, Zep, Letta) self-report on LoCoMo/LongMemEval and dispute each other's numbers (see pitfall 6). Mem0's 2026 benchmark guide: https://mem0.ai/blog/ai-memory-benchmarks-in-2026 .
- **Industry vs academia difference (observation).** Industry reports recall accuracy, latency and token cost. Academic 2026 work has moved to governance properties (GateMem, CIMemories, MemSecBench), but on synthetic data with no deployment evidence. No vendor publishes erasure-verification or isolation results for its memory product that I found.

---

## 6. What changed in the last 12 months (since ~2025-09)

- Memory benchmarks moved from **recall** (LoCoMo, LongMemEval) to **update/staleness** (STALE, Memora/FAMA, MemConflict, MemTrace, FinPerMA), **action utility and cost** (Mem2ActBench, MERIT), and **governance**: GateMem is the first benchmark, as far as I found, to combine utility, access control and deletion in one score (June 2026).
- Privacy evaluation moved from single-turn CI (ConfAIde) to **persistent-memory CI** (CIMemories, PersistBench) and **multi-channel leakage** (AgentLeak).
- Poisoning evaluation moved from single-shot ASR to **lifecycle** metrics including repair (MemSecBench) and **benign-traffic cost** with confidence intervals (arXiv:2609.22818).
- A strong **meta-evaluation** wave appeared: ABC, validity audits of safety benchmarks, ASR validity, G-theory reliability and compounding judge validity.
- Finance moved from capability benchmarks to **execution-grounded safety** (FinVault) and **governability** (Fiducia-bench, ReguSim), still without persistent memory.

---

## 7. Gaps (my observations; confidence in brackets)

1. **No benchmark combines persistent memory × finance governance.** Finance safety benchmarks (FinVault, Fiducia-bench, ReguSim, CNFinBench) have no cross-session memory. Memory-governance benchmarks (GateMem, CIMemories, AgentLeak) have no finance-specific obligations (information barriers, suitability, record retention). AgentLeak includes a finance domain, but only as a leakage context. [high: searched with ≥6 phrasings across arXiv/SciSpace; closest are arXiv:2606.18829 and arXiv:2602.11510]
2. **The retention-vs-erasure conflict is untested.** Every forgetting metric rewards forgetting. Finance needs *both* mandated retention (record-keeping) and erasure (GDPR Art. 17, subject to legal-obligation exemptions). No metric scores correct handling when the two conflict, or legal holds. [high]
3. **End-to-end erasure verification across derived memory artifacts** (summaries, reflections, embeddings, index topology, logs) with a statistical guarantee does not exist. The available pieces are GateMem F (interface), Ghost Echoes (index), MemSecBench SRSR (repair) and leak@k (sampling). [medium-high]
4. **Memory lineage/provenance metrics** that trace an agent decision back to the memory writes behind it (source, principal, time, consent) are missing. DEMM-Bench measures evidence sufficiency for runtime records, not memory. [medium]
5. **Cross-client isolation in shared institutional memory** (the advisor serving many clients) is only partially covered: GateMem does multi-principal roles in non-finance domains, and CIMemories does a single user. [medium]
6. **Reliability reporting**: governance benchmarks rarely report pass^k-style worst-case-over-trials or CIs. CIMemories Violation@n and arXiv:2609.22818 are the exceptions. A compliance metric should be worst-case/tail, not mean. [medium]
7. **Construct validity against actual regulation**: labels come from LLM personas, not legal text or compliance-officer adjudication. Rule-grounded datasets exist (OmniCompliance-100K, RegOps-Bench) but are not connected to memory behavior. [medium]

---

## 8. Key groups (from author lists I saw; incomplete)

- UW/AI2/CMU privacy and CI: Mireshghallah, Sap, Choi, Shokri (ConfAIde); Stanford SALT, Diyi Yang (PrivacyLens); Microsoft (PrivacyLens-Live, CI-RL, CI-Work).
- UK AISI and Gray Swan (AgentHarm, Inspect); ETH SPY Lab (AgentDojo); Princeton (HAL, AI Agents That Matter); Sierra (τ-bench); METR.
- Memory benchmarks: UCLA/Tencent (LongMemEval), Snap/UNC (LoCoMo), UCSD (MemoryAgentBench).
- Finance: aifinlab (FinVault), The Fin AI / Ananiadou group (AMA, InvestorBench), SUFE (CNFinBench).

## 9. Screening notes / tool issues

- arXiv API returned HTTP 429 on two queries (`LongMemEval OR LoCoMo …` first attempt; `memory benchmark survey …`); the first was retried successfully. `"right to be forgotten" … evaluation` returned 0 hits.
- arXiv HTML and PDF for FinVault (arXiv:2601.07853) and the HTML for DEMM-Bench (arXiv:2606.20634) returned 404, so those notes are abstract-only.
- arXiv:2509.10224 ("Empirical Evaluation of Memory-Erasure Protocols") turned out to be about IoT device memory erasure, so I screened it out: removed the `evaluation` tag and added `screened-out-offtopic`.
- SciSpace hits with no arXiv/DOI match were not recorded.

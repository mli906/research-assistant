# Procedural memory from traces, promotion to shared skills, and its governance: partial review (facet tag `skills`)

- **Scout and date.** lit-scout (skills facet), 2026-09-25.
- **Recency cutoffs.**
  - arXiv was searched through 2026-09-23 (newest relevant hit: arXiv:2609.28693).
  - The SciSpace index lags: its newest hits here are from 2026-01.
  - OpenAlex was used for foundations and supply-chain grey literature.
  - Web sources were accessed 2026-09-25.
- **Library.**
  - 174 new records, bringing `literature/papers.jsonl` from 707 to 881.
  - 21 existing records were re-tagged, so 196 records now carry `skills`.
  - 14 are also tagged `core`, with notes in `literature/notes/arXiv-<id>.md`.
- **Evidence labels.**
  - **full** = arXiv HTML read through the fetch tool, which returns an extracted summary rather than a line-by-line read.
  - **abs** = per abstract only.
  - Legal labels: **[V]** = checked against the official text or an official-text host (Cornell LII for the CFR, accessed 2026-09-25); **[M]** = background knowledge, not verified here; check with counsel.
- **Confidentiality.**
  - No content from `inputs/` or from the "PI design" fields of `gaps.md` was used in any query.
  - Memoria (arXiv:2512.12686) is public.
  - One line in §10 refers to the PI's internal design by control number only. **Strip it before sharing.**

---

## 1. Query plan (reusable by `/radar`)

| Facet | arXiv (`lit.py arxiv`, `--since 2025-06-01`; "date" = `--sort date`) | SciSpace question | Web |
|---|---|---|---|
| Mechanisms: trace → procedure → skill | `("skill library" OR "skill libraries") AND (agent OR LLM)`; `"procedural memory" AND (agent OR LLM)`; `("workflow memory" OR "experience memory" OR "experience library") AND agent`; `("skill induction" OR "skill discovery" OR "skill abstraction" OR "skill distillation") AND (LLM OR agent)`; `("agent workflow memory" OR "workflow induction" OR "agent KB" OR "experience transfer") AND agent` | "How do LLM agents distill reusable workflows or skills from past interaction trajectories (e.g., Agent Workflow Memory, ExpeL, Voyager skill library)?" | Anthropic Agent Skills / agentskills.io; OpenAI Codex skills; LangMem procedural memory; Foundry procedural memory; AgentCore episodic reflections |
| Promotion gates and verification | `("self-evolving" OR "self-improving") AND agent AND (skill OR experience) AND (verification OR verifier OR audit)`; `(skill OR "procedural memory") AND agent AND (admission OR promotion OR gating OR "human review" OR approval)` | "How should self-improving LLM agents verify, audit, or approve newly learned skills before deploying them…?" | Claude "Skills for enterprise" governance page |
| Packaging and ecosystem | `("agent skills" OR "agentic skills" OR "SKILL.md")`; `"agent skills"` (date); `("agent skills" OR "skill library") AND (benchmark OR evaluation)` | — | — |
| Cross-user sharing and privacy | `(skill OR "procedural memory" OR "experience reuse") AND (multi-user OR "cross-user" OR federated OR shared)`; `(skill OR experience OR workflow) AND agent AND (tenant OR "multi-tenant" OR "cross-tenant" OR "cross-user")`; `(skill OR workflow OR "procedural memory") AND (privacy OR leakage OR "differential privacy") AND agent AND (trajectories OR traces)`; `(skill OR workflow OR procedure) AND agent AND ("differential privacy" OR "k-anonymity" OR anonymization OR redaction)`; `"agent skills" AND (privacy OR leakage OR confidential)`; `(trajectory OR trace) AND (skill OR procedure) AND ("membership inference" OR extraction OR "data leakage") AND agent`; `(SkillClaw OR "collective skill" OR "shared skill library" OR "skill sharing") AND agent` | "Can procedural knowledge or skills learned by an LLM agent from one user's data leak private information to other users when shared?"; "How can LLM agents share learned experiences or workflows across multiple users or organizations while preserving privacy…?" | — |
| Erasure / unlearning propagation | `(skill OR "procedural memory") AND (unlearning OR erasure OR forgetting OR revocation) AND agent`; `("machine unlearning" OR unlearn) AND agent AND (memory OR experience OR skill) AND (derived OR propagation OR cascade)`; `agent AND (skill OR experience OR "procedural memory") AND (unlearning OR "right to be forgotten" OR GDPR)`; `(skills OR "agent skills") AND (erasure OR deletion OR "data subject" OR GDPR)` (date) | "How can machine unlearning remove the influence of specific user data from agent memory, experience libraries, or derived skills?" | — |
| Poisoning, backdoors, supply chain | `("agent skills" OR "skill marketplace" OR "skill supply chain") AND (security OR malicious OR poisoning)`; `("experience" OR "memory") AND agent AND (poisoning OR backdoor) AND (skill OR workflow OR procedure)`; OpenAlex `agent skills security supply chain marketplace malicious` (cited) | "What security risks and malicious skills exist in agent skill marketplaces and the SKILL.md agent skills ecosystem?" | ClawHavoc / ClawHub incident; Snyk ToxicSkills |
| Provenance, change control, drift | `(skills OR "procedural memory") AND agent AND (provenance OR lineage OR governance OR "change control")`; `"skill" AND agent AND (drift OR regression OR "continual") AND (library OR memory)`; `"skills" AND ("model risk" OR "change management" OR "software supply chain" OR SBOM OR signing) AND agent`; `(skill OR experience) AND (lineage OR provenance OR attribution) AND (trajectory OR trace) AND agent` (date) | — | — |
| Finance / regulated | `(skill OR "agent skills") AND (finance OR financial OR compliance OR regulated OR banking)`; `(skill OR workflow OR "procedural memory") AND (enterprise OR regulated OR bank OR advisory OR healthcare) AND governance AND agent` (date) | — | 17 CFR 275.206(4)-7 and 204-2 (LII); FINRA 2026 oversight report; FCA/FSB agentic statements |

In total: 39 arXiv queries, 6 SciSpace questions, 3 OpenAlex queries, 1 id fetch of 7 foundational papers, and 14 web searches or fetches.

---

## 2. Taxonomy: how skills are formed, represented, promoted and governed

### 2.1 Formation (trace → procedure)

| Pattern | What is distilled | Examples (id) |
|---|---|---|
| Exemplar storage | whole trajectories retrieved as exemplars | Synapse (arXiv:2306.07863, abs) |
| Insight/rule extraction | natural-language lessons from successes and failures | ExpeL (arXiv:2308.10144, abs); AutoManual (arXiv:2405.16247, abs); ReasoningBank (arXiv:2509.25140, abs); JEF Hinter (arXiv:2510.04373, abs); SR-Fraud boundary rules (arXiv:2609.27287, full, existing note) |
| Workflow induction | reusable sub-routines abstracted from trajectories | AWM (arXiv:2409.07429, abs); WISE-Flow from *historical service interactions* (arXiv:2601.08158, abs); LEGOMem (arXiv:2510.04851, abs); Memp (arXiv:2508.06433, abs) |
| Programmatic skill induction | executable code or API skills, verified on the fly | Voyager (arXiv:2305.16291); ASI (arXiv:2504.06821, abs); SkillWeaver (arXiv:2504.07079, abs) |
| Package-level skill evolution | SKILL.md directories refined or created from traces | Trace2Skill (arXiv:2603.25158, abs); SkillClaw (arXiv:2604.08377, full); Designer-RSI (arXiv:2609.22086, full); online CUA skills (arXiv:2609.04869, abs); SkillCommit (arXiv:2608.15165, abs) |
| Persona/preference skills | a *person's* style and preferences as a skill | AntiSkillBench (arXiv:2608.03700, full); developer-specific skills (arXiv:2608.10319, abs); CounterPersona defence (arXiv:2609.15097, abs) |
| Parametric internalisation | procedures moved into weights or activations | Neural Procedural Memory (arXiv:2606.29824); TokMem (arXiv:2510.00444, not stored); ILWS distils instruction deltas into weights (arXiv:2509.00251, abs); Fed-SE LoRA (arXiv:2512.08870, abs) |

The unifying view is the "Experience Compression Spectrum": memory, then skills, then rules, with compression rising from 5–20× to 50–500× to 1,000×+. Its authors found a cross-community citation rate below 1% (arXiv:2604.15877, abs). Memory-Skill Isomorphism (arXiv:2609.16669, abs) argues that one SKILL.md carrier can hold both.

### 2.2 Representation

- Natural-language prose: SKILL.md, rules, playbooks.
- Structured prose with contracts: Contractual Skills/GovernSpec (arXiv:2605.22634, abs); AIP execution graphs (arXiv:2606.04781, abs); SIGIL typed harnesses (arXiv:2607.27309).
- Code or API functions: Voyager, ASI, SkillWeaver.
- Skill graphs: ASG-SI (arXiv:2512.23760, full); SE-GoS (arXiv:2609.08228).
- Parametric: adapters, activation steering.

The representation determines what "erasure" and "leakage" mean. Prose and code can be inspected, diffed and re-derived. Parametric skills inherit machine-unlearning semantics; see MemoRepair's LUNE operator (arXiv:2605.07242, full).

### 2.3 Promotion (who decides that a candidate becomes a reusable skill)

| Gate type | Mechanism | Examples |
|---|---|---|
| None / LLM self-judgment | the evolver decides | many self-evolving papers; ReasoningBank (self-judged success, abs) |
| Utility gate on held-out replay | admit if it beats the incumbent | SkillClaw nightly validation (full); SkillWeaver/ASI execution verification (abs) |
| **Regression-aware gate** | admit only with no or bounded regressions | Designer-RSI "no prompt lost ∧ some prompt won" (full); GRASP hard regression budget (arXiv:2605.29668, abs); FRAMES anti-regression guarantee (arXiv:2608.01772, abs); AgentDevel flip-centred gating (arXiv:2601.04620, abs); SkillCommit behavioural validation (abs) |
| **Statistical admission** | confidence bound on benefit | SR-Fraud one-sided Wilson bounds, admission cap, retirement rule (arXiv:2609.27287, full) |
| **Verifier and contract gate with audit evidence** | replay, interface contracts, evidence bundle, append-only log | ASG-SI (full; no empirical evaluation) |
| **Provenance-diversity gate** | require support from ≥3 users and clusters, reject majority dominance | PoisonedEvolution pilot defence (arXiv:2608.05563, full) |
| Human / maker-checker | separate author and reviewer | Claude enterprise guidance "Skill authors should not be their own reviewers" (industry, §7); SR-Fraud optional human review |
| Security scan | static, LLM or runtime scanning before publish | Claude Enterprise skill scanning; SkillScan (arXiv:2601.10338); registry scanners (arXiv:2609.12001) |

### 2.4 Governance (after promotion)

- **Lineage and provenance.**
  - FederatedSkill decision logs (full).
  - ASG-SI evidence bundles (full).
  - MemoRepair provenance graph (full).
  - SkillTrace, for reuse or clone auditing of marketplace skills (arXiv:2608.05204, abs).
  - RedAct watermarks (full).
  - Registry signing and checksums (industry).
- **Drift and retirement.**
  - Skill drift framed as contract violation (arXiv:2605.10990, abs).
  - Library drift (arXiv:2605.19576, abs).
  - "Blind curator": judge bias disables retirement (arXiv:2607.07436, abs).
  - Coalition-aware reliability (arXiv:2608.22610, abs).
  - Safe skill retirement (arXiv:2609.29543, abs).
- **Revocation, unlearning and repair.**
  - OBLIVION (full).
  - MemoRepair (full).
  - MUTE, parametric (arXiv:2607.28829, full).
  - Agentic tool unlearning (arXiv:2608.21544, abs).
  - K-Bench (arXiv:2609.12808, abs).
- **Lifecycle frameworks.**
  - SkillsVote (arXiv:2605.18401, abs).
  - SkillOps (arXiv:2605.13716, abs).
  - SkillHone decision history (arXiv:2606.08671, abs).
  - Human-governed maintenance study (arXiv:2609.05677, abs).
  - Surveys: the lifecycle survey (arXiv:2607.10113, full-partial) and the systems SoK (arXiv:2608.29596, full-partial).

---

## 3. Comparison table (systems that form or promote skills)

The columns are: trace source; skill representation; promotion gate; cross-user?; provenance; unlearning; evaluation. "—" means absent. Unless marked "full", entries are per abstract.

| System (id) | Trace source | Skill representation | Promotion gate | Cross-user? | Provenance | Unlearning | Evaluation |
|---|---|---|---|---|---|---|---|
| Synapse (arXiv:2306.07863) | own trajectories | exemplar trajectories | — | no | — | — | MiniWoB++, Mind2Web |
| ExpeL (arXiv:2308.10144) | own trajectories | NL insights + exemplars | — | no | — | — | benchmarks not named in stored abstract |
| AutoManual (arXiv:2405.16247) | own interaction | rule manual | rule optimisation online | no | — | — | ALFWorld (others per abstract truncated) |
| Voyager (arXiv:2305.16291) | own exploration | code skill library | self-verification | no | — | — | Minecraft |
| AWM (arXiv:2409.07429) | offline or online queries | NL workflows | — (induced on the fly) | no | — | — | Mind2Web +24.6%, WebArena +51.1% rel. |
| ASI (arXiv:2504.06821) | own web interaction | programmatic skills | execution verification | no | — | — | WebArena |
| SkillWeaver (arXiv:2504.07079) | self-exploration | API skills | honing/testing | skills transferable across agents | — | — | WebArena, real sites |
| Agent KB (arXiv:2507.06229) | many agent *frameworks* | shared experience KB | — | **cross-agent** (not cross-user) | — | — | GAIA, SWE-bench |
| Memp (arXiv:2508.06433) | own trajectories | steps + scripts | update/deprecate rules | transfer to weaker model | — | deprecation | TravelPlanner, ALFWorld |
| ReasoningBank (arXiv:2509.25140) | own successes and failures (self-judged) | reasoning strategies | self-judgment | no | — | — | web browsing + software engineering (per abstract) |
| WISE-Flow (arXiv:2601.08158) | **historical service interactions** | workflows with prerequisites | — | implicitly (service logs) | — | — | ToolSandbox, τ²-bench |
| ASG-SI (arXiv:2512.23760, full) | successful trajectories | skill graph with interfaces | verifier replay + contract checks | no | **evidence bundles, append-only audit** | — | none (reference implementation only) |
| SkillClaw (arXiv:2604.08377, full) | **8 users' sessions** | SKILL.md | nightly utility validation | **yes, synced to all users** | — | — | WildClawBench, 6 days |
| FederatedSkill (arXiv:2606.03143, full) | local client trajectories | semantic skill diffs | server evolution agent | **yes (federated, personalised)** | **decision logs per source patch** | — | benchmarks + empirical privacy audit (no DP) |
| Fed-SE (arXiv:2512.08870) | client high-return trajectories | LoRA (parametric) | trajectory filtering | yes (federated) | — | — | 5 environments, +10% vs FedIT |
| FICAL (arXiv:2412.08054) | client data | "knowledge compendiums" (text) | — | yes (federated) | — | — | tool-learning tasks |
| Designer-RSI (arXiv:2609.22086, full) | **real user briefs (1,406)** | NL skills | matched replay gate; k_min=3 occurrences | **yes, pooled traffic** | — | — | GenEval2 72.7→99.3% |
| SkillsVote (arXiv:2605.18401) | open corpus + trajectories | Agent Skills | verifiability profiling + attribution | ecosystem | attribution of outcomes to skills | — | synthesised verifiable tasks |
| GRASP (arXiv:2605.29668) | own failures | bounded skill library | **net improvement under hard regression budget** | no | — | — | MedAgentBench 40.6→88.8% |
| FRAMES (arXiv:2608.01772) | enterprise production feedback | skills for policy-bound workflows | Pareto + **anti-regression guarantee** | within firm | "preserving auditability" | — | internal production + τ-bench |
| SkillCommit (arXiv:2608.15165) | experience stream | hierarchical skills | behavioural validation before abstraction | no | instance patches kept | — | — |
| MSCE (arXiv:2607.16621) | step traces | policies with evidence links | positive estimated gain | no | **evidence links retained** | — | EvoAgentBench, LoCoMo |
| SR-Fraud (arXiv:2609.27287, full) | matured production errors | human-readable rules | **Wilson bound + cap + optional human review** | aggregate over customers | versioned weekly | conservative retirement | proprietary 9-week stream |
| MemoRepair (arXiv:2605.07242, full) | agent memory incl. skills | prose/chain/neural skills | validate successor before republish | no | **provenance graph required** | **cascade repair on delete/correct** | ToolBench, MemoryArena |

---

## 4. Governance-risk table (promotion of per-client procedural memory into shared skills)

"Metric exists?" asks whether a published metric measures the risk *for skills*. Finance obligations are labelled [V] or [M].

| Risk | Mechanism exists? | Metric exists? | Finance / regulated obligation | Evidence ids |
|---|---|---|---|---|
| **Cross-client leakage through skill text** (client specifics baked into a procedure) | Partial. Local distillation prompted to omit IDs and values (FederatedSkill), privacy sanitisation (AntiSkillBench), redaction preserving audit evidence (RedAct). **No DP or k-anonymity guarantee in any skill paper found.** | Yes, single-user only: Skill Coverage, Field QA, VocabGain (AntiSkillBench: 55–66% coverage) | Reg S-P safeguards and disposal of customer information [M]; fiduciary confidentiality [M]; GDPR Arts 5(1)(b), 6(4) purpose compatibility for reuse across clients [M] | arXiv:2606.03143, arXiv:2608.03700, arXiv:2606.10813, arXiv:2609.15097 |
| **Behavioural leakage** (a skill reveals specifics through behaviour even if its text is hidden) | Prompt defences fail against trajectory inference | Yes, for proprietary skills: SigLeak F1/utility; RedAct NST/RPI | same as above | arXiv:2607.25560, arXiv:2604.21829, arXiv:2606.10813 |
| **Memorisation / whitewashing** (abstraction hides sensitive or malicious content from detectors) | — | Detection drop 98.5% → 11.4% (SkillJack, malicious content, not PII) | — | arXiv:2608.03509 |
| **Erasure propagation to derived skills** | Partial. Cascade repair via a provenance graph (MemoRepair, single-agent, staleness motivation); taint-based anti-re-derivation (OBLIVION, capability revocation); ledger-based influence tracing (MUTE, parametric only) | Leak%/Stale-use% (MemoRepair); ASR/IWE of resurrection (OBLIVION); BLI/IRR (MUTE); persistence after source deletion (SkillJack: **80%**) | GDPR Art. 17 [M]; CCPA deletion [M]; tension with 204-2(a)(17) five-year retention of procedures [V] if skills are procedures; see §5 | arXiv:2605.07242, arXiv:2608.08264, arXiv:2607.28829, arXiv:2608.03509 |
| **Partial-contribution removal** (one skill built from many clients; one client erases) | **None found** | **None** | same | — |
| **Poisoning via traces** | Provenance-diversity gate (≥3 users/clusters, pilot); extraction-time review; runtime monitoring | Skill embedding rate (91% on SkillClaw at 10% support); trigger rate; persistence | FINRA 2026 names agents that "may unintentionally store… or misuse" data (per review, [V]); FSB 2026 names memory poisoning [V per review] | arXiv:2608.05563, arXiv:2608.08303, arXiv:2608.03509, arXiv:2512.16962 |
| **Skill supply chain / marketplaces** | Scanners (SkillScan, MalSkills, SkillFortify), permission frameworks (SkillGuard, SkillScope), registry + runtime composition | Many: vulnerability prevalence 26.1% (42k skills); 13.4% critical (Snyk); MaliciousSkillBench; SkillTester | Third-party / vendor risk management [M]; DORA ICT third-party for EU entities [M] | arXiv:2601.10338, arXiv:2602.06547, arXiv:2605.11418, arXiv:2604.03070, arXiv:2609.12001, arXiv:2603.00195 |
| **Provenance / lineage to source traces** | Decision logs, evidence bundles, provenance graphs, watermarks | Lineage-completeness sensitivity (MemoRepair: 1% missing edges → 17.7% leak); SkillTrace reuse detection | 204-2 books and records [M]; AI Act Art. 12 logging for high-risk only [per review] | arXiv:2606.03143, arXiv:2512.23760, arXiv:2605.07242, arXiv:2608.05204 |
| **Approval / change control** | Regression gates (GRASP, FRAMES, Designer-RSI, AgentDevel); statistical admission (SR-Fraud); maker-checker (industry guidance only) | Flip accounting W→C/C→W; gate rejection rates (43–49%) | 206(4)-7(b) annual review, (c) CCO [V]; SR 26-2 scope excludes GenAI/agentic [V per review] | arXiv:2608.17684, arXiv:2609.22086, arXiv:2605.29668, arXiv:2609.27287 |
| **Drift / regression after promotion** | Contract-based drift detection; outcome-driven retirement; periodic re-evaluation (industry) | Drift false-alarm rates (0/599 no-drift); library-drift diagnostics; regression counts | 206(4)-7(b) annual review [V]; ongoing monitoring (SR 26-2-style) [M] | arXiv:2605.10990, arXiv:2605.19576, arXiv:2607.07436, arXiv:2608.17684 |
| **Security drift from promotion** (capability ↑ and unauthorised actions ↑) | — | Exposure, conditional ASR, unauthorised state change (e-banking) | suitability / best-interest conduct [M]; unauthorised transactions | arXiv:2608.17684 |

---

## 5. Finance and regulated relevance

**Is a promoted skill a "model", a "record", or a "policy and procedure"?** No regulator has answered this. Nothing was found on agent skills or procedural memory specifically; the closest statements are FINRA 2026 on agents and FSB/FCA on agentic AI generally. Three readings:

1. **Policy and procedure (Advisers Act).**
   - Rule 206(4)-7(a) requires "written policies and procedures reasonably designed to prevent violation", (b) annual review "of the adequacy… and the effectiveness of their implementation", and (c) a designated CCO [V: 17 CFR 275.206(4)-7 via Cornell LII, accessed 2026-09-25].
   - Consider a promoted skill that encodes a compliance step, such as a pre-trade suitability check sequence or a KYC refresh routine. Arguably it is *part of the implementation* of those procedures. Then it falls within the annual review and CCO administration [M: interpretation, not guidance].
   - Consequence: **Rule 204-2(a)(17)(i)** requires "a copy of the investment adviser's policies and procedures… that are in effect, or at any time within the past five years were in effect" [V: LII]. Retention is ≥5 years under 204-2(e)(1) [V: LII].
   - If skills are procedures, **every promoted version must be retained for five years**. That collides directly with GDPR erasure of client data embedded in a skill. This is GP1's retain-vs-erase tension, now at the skill level.
2. **Model.**
   - US bank model-risk guidance SR 26-2 / OCC 2026-13 superseded SR 11-7 and scopes out GenAI and agentic AI [per review.md, V].
   - The classical definition covers quantitative methods producing estimates [M]. Prose procedures fit poorly; a statistically admitted rule set like SR-Fraud fits better.
   - RIAs have no model-risk rule [M]. So "model" is a *voluntary* framing: useful for change control (validation, versioning, monitoring), not mandated.
3. **Record / communication.**
   - A skill containing client-specific content derived from advice interactions may itself be (or embed) a record "relating to" advice under 204-2 [M: counsel; the same open question as G7 in review.md].
   - Reg S-P (as amended in 2024) governs customer information safeguards and disposal [M: compliance dates not verified here].

**Finance-specific evidence on skills is thin.**
- One simulated e-banking audit shows that promotion raises utility and also unauthorised financial state changes (0.583 → 0.685, 3/3 lineages; arXiv:2608.17684, full).
- One production fraud system uses statistically gated rule admission (arXiv:2609.27287, full).
- Finance skill *mechanisms* exist without governance: ASDA financial skill distillation (arXiv:2603.16112, abs); FactorMiner (arXiv:2602.14670, abs); FinAcumen (arXiv:2606.17642, abs); EvolveTrade (arXiv:2609.17632, abs).
- FRAMES (arXiv:2608.01772, abs) is the only "policy-governed enterprise workflow" skill-evolution paper, and it is document auditing, not finance.
- Adjacent healthcare governance papers: medical skill audit (arXiv:2604.20441), healthcare skills governance (arXiv:2605.02709), clinical harness (arXiv:2606.26494), all abs.
- A financial-institution GenAI risk-control framework (arXiv:2607.04103, abs) does not address skills.

---

## 6. Evaluation: benchmarks and metrics

| Property | Benchmarks / metrics | ids |
|---|---|---|
| Skill quality / usefulness | SkillsBench (curated skills 33.9 → 50.5% pass, +16.6 pp; LLM-authored ≈ +0.0 pp per arXiv:2605.19576); SWE-Skills-Bench; SkillTester; skill coverage as test adequacy | arXiv:2602.12670, arXiv:2603.15401, arXiv:2603.28815, arXiv:2606.20659 |
| Formation from experience | SkillEvolBench (180 tasks, episodic → procedural); SkillFlow; SkillGenBench; AFTER (382 enterprise tasks, cross-role/-model transfer) | arXiv:2605.24117, arXiv:2604.17308, arXiv:2605.18693, arXiv:2606.23127 |
| Reuse / retrieval | SkillRet; procedural memory retrieval benchmark; skill shadowing | arXiv:2605.05726, arXiv:2511.21730, arXiv:2605.24050 |
| Regression / change control | W→C vs C→W flip counts; gate rejection rates; execution-grounded state checks | arXiv:2608.17684, arXiv:2609.22086, arXiv:2601.04620 |
| Drift | contract-violation detection; library-drift diagnostics; procedural memory under change | arXiv:2605.10990, arXiv:2605.19576, arXiv:2609.09774 |
| Leakage (personal) | Skill Coverage / Field QA / VocabGain | arXiv:2608.03700 |
| Leakage (proprietary) | NST / RPI; SigLeak F1 and utility recovery; skill-stealing ASR | arXiv:2606.10813, arXiv:2607.25560, arXiv:2604.21829 |
| Unlearning / revocation | resurrection ASR/IWE (AgentForgetBench); Leak%/Stale-use% after cascade; BLI/IRR; K-Bench K-Score; persistence after source deletion | arXiv:2608.08264, arXiv:2605.07242, arXiv:2607.28829, arXiv:2609.12808, arXiv:2608.03509 |
| Poisoning / supply chain | SER; trigger rate; MaliciousSkillBench; MalSkillBench; SkillVetBench; SkillSec-Eval | arXiv:2608.05563, arXiv:2608.19901, arXiv:2606.07131, arXiv:2606.15899, arXiv:2607.13987 |

**Missing metrics.**
- **Cross-client** leakage from a shared skill built from N clients' traces, e.g. per-client canary recovery from the shared skill or from other clients' sessions.
- **Partial-erasure** fidelity: after client i's erasure, is the re-derived skill indistinguishable from one built without i?
- **Promotion cost** in regulated units: reviewer hours, false rejections.

---

## 7. Industry practice (accessed 2026-09-25)

| Source | What it says (relevant to promotion governance) |
|---|---|
| Anthropic, "Skills for enterprise" (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise) | Risk tiers (code execution, network, hardcoded credentials…); an 8-step review checklist; evaluation gates (triggering, isolation, coexistence, instruction following, output quality); **"Establish separation of duties: Skill authors should not be their own reviewers"**; version pinning ("a new version uploaded by anyone in the workspace immediately changes what production agents run"); checksums and signed commits. Enterprise skill scanning does **not** cover the API, pre-existing skills, or CMEK/ZDR/HIPAA-configured orgs. Nothing on skills derived from user data. |
| Claude Help Center, provisioning (https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization) | Admin-provisioned skills are on by default for all users; owners add or remove org-wide skills (per search snippet). |
| Agent Skills open standard (https://agentskills.io/home; https://github.com/agentskills/agentskills) | SKILL.md format published as an open standard (per secondary press, Dec 2025); adopted by OpenAI Codex, GitHub Copilot, Cursor and others. |
| OpenAI Codex skills (https://developers.openai.com/codex/skills; https://github.com/openai/skills) | Skills are directories with SKILL.md, invoked explicitly or selected by description. |
| Microsoft Foundry memory (https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage, doc dated 2026-08-05; https://devblogs.microsoft.com/foundry/memory-build2026/) | **Procedural memory** (public preview): "Agent trajectories are ingested and audited to identify successful patterns". It is enabled per memory store with a default TTL. Memory is partitioned by `scope`: per user via `{{$userId}}`, or "a static `scope` value" if "you don't need per-user isolation". A static scope therefore makes procedural memory **shared across users**. There is no documented review or approval of extracted procedures. |
| AWS AgentCore episodic memory (https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/episodic-memory-strategy.html) | Reflections can be stored at `/strategy/{id}/`, "across all episodes and across all actors". The docs warn: **"Because reflections can span multiple actors within the same memory resource, consider the privacy implications of cross-actor analysis… Consider using guardrails… or reflecting at the actor level."** This is the only vendor we found that states the cross-user risk of procedural distillation, and it offers no mechanism beyond scoping or guardrails. |
| LangMem (https://www.langchain.com/blog/langmem-sdk-launch) | Procedural memory is the evolving system prompt, updated by a prompt optimiser from feedback (per search snippet). |
| ClawHavoc incident (https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html; secondary press) | 341 of 2,857 ClawHub skills (11.9%) were malicious (Atomic Stealer via fake prerequisites), disclosed by Koi Security on 2026-02-01. Later counts reached 1,184 packages from 12 publishers (Antiy, per secondary press). |
| Snyk ToxicSkills (https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) | 3,984 skills scanned (ClawHub and skills.sh, as of 2026-02-05): 13.4% critical, 76 confirmed malicious payloads. The publishing barrier was "a SKILL.md Markdown file and a GitHub account that's one week old. No code signing." |
| FINRA 2026 Annual Regulatory Oversight Report (https://www.finra.org/sites/default/files/2025-12/2026-annual-regulatory-oversight-report.pdf) | First treatment of AI agents; agents "may unintentionally store, explore, disclose, or misuse sensitive or proprietary information" (per search snippet, consistent with review.md [V]). Nothing on learned procedures. |
| FCA / FSB (https://www.burges-salmon.com/articles/102n7kt/…; secondary) | The FCA CEO calls agentic AI a "profound step change", with oversight through existing frameworks. The FSB 2026 consultation covers AI lifecycle management including agentic AI. Nothing skill-specific. |

**Industry vs academia.**
- Industry governs **authored skills** as software: review, separation of duties, pinning, scanning.
- Industry ships **learned procedural memory** (Foundry, AgentCore, LangMem) with scoping and TTL but no promotion review.
- AWS alone flags the cross-user privacy of reflections.
- Academia has promotion gates for *utility*, *regression* and *integrity*, but not for *privacy or erasure* across users.

---

## 8. What changed in the last 12 months (2025-10 → 2026-09)

1. **The ecosystem exploded.** The SKILL.md open standard (Dec 2025) was adopted cross-vendor. Marketplaces grew to hundreds of thousands of skills. The first mass supply-chain incident (ClawHavoc, Feb 2026) triggered about 40+ security papers in 2026: scanners, benchmarks, supply-chain studies. arXiv:2609.17274 measures a wave that "had crested" by mid-2026.
2. **Self-evolving skills went from single-agent to collective.**
   - SkillClaw (2026-04) syncs skills learned from many users.
   - FederatedSkill (2026-06) federates skill diffs.
   - Designer-RSI (2026-09) evolves skills from real user traffic.
   - Foundry procedural memory (Build 2026) and AgentCore cross-actor reflections productise it.
3. **Attacks moved to the promotion step itself.** Trajectory poisoning of skill evolution appeared in 2026-08: PoisonedEvolution, Query-Only TBA (arXiv:2608.08303) and SkillJack. SkillJack showed derived skills outlive source deletion (80%).
4. **Gates became regression-aware and statistical.** GRASP, FRAMES, AgentDevel, Designer-RSI and SR-Fraud (2026-01 → 2026-09) replaced "LLM decides".
5. **Skill unlearning and repair appeared**: MemoRepair (2026-05), OBLIVION (2026-08), MUTE (2026-07), agentic tool unlearning (2026-08). None is framed as a data-subject erasure of *multi-client-derived* skills.
6. **Personal-data leakage into skills was measured for the first time**: AntiSkillBench (2026-08), CounterPersona (2026-09).
7. **The first finance-domain audit of self-evolution** (arXiv:2608.17684, 2026-08).

---

## 9. How crowded is each sub-area (judgment from this sample; counts are records we screened, not exhaustive)

| Sub-area | Crowding | Basis |
|---|---|---|
| Skill evolution / induction mechanisms | **Very crowded** | about 80+ papers since 2026-01 in our queries alone; new ones weekly |
| Skill marketplace security (malicious skills, scanners, supply chain) | **Very crowded** | about 40+ papers in 2026, several benchmarks |
| Trajectory poisoning of skill evolution | Emerging, fast (3 papers in 2026-08) | arXiv:2608.05563, arXiv:2608.08303, arXiv:2608.03509 |
| Promotion gates (regression, statistical) | Moderate | about 8 papers |
| Lifecycle governance / provenance frameworks | Moderate, mostly position or design papers | SkillsVote, SkillOps, ASG-SI, AIP, surveys |
| Skill unlearning / cascade repair | Sparse but active | 4 papers (2026-05 → 2026-08) |
| Privacy of skills distilled from user data | **Sparse** | AntiSkillBench, CounterPersona (single-user); FederatedSkill (empirical, no guarantee); P2Skill (a different problem: cloud-local PII routing) |
| Cross-client leakage bounds + erasure propagation for shared skills | **Empty** in what we searched | see §10 |
| Finance / regulated skill governance | **Nearly empty** | arXiv:2608.17684 (simulation), SR-Fraud (rules); no regulator guidance |

---

## 10. Gaps I noticed (labelled; confidence in brackets)

**Scoop check on the combined claim:** "governed promotion of per-client procedural memory into shared skills, with erasure propagation and leakage bounds, in a regulated setting."
- Searched with 12+ differently phrased arXiv queries, 2 SciSpace questions and vendor documentation.
- **No paper covers it.** Every component exists in isolation:

| Component | Closest work | Same / partial / different |
|---|---|---|
| Cross-user promotion mechanism | SkillClaw (full), FederatedSkill (full), Designer-RSI (full) | **same** mechanism; none governs privacy or erasure |
| k-distinct-source promotion threshold | PoisonedEvolution provenance-diversity gate (full) | **partial**: integrity motivation, pilot only, not privacy |
| Leakage measurement for skills | AntiSkillBench (full) | **partial**: single-user persona, no bound, no cross-client |
| Leakage *bound* | none (FederatedSkill is explicitly empirical, "no formal guarantee") | **different / absent** |
| Erasure propagation to derived skills | MemoRepair (full), OBLIVION (full), MUTE (full) | **partial**: staleness, capability revocation, parametric; none handles partial removal of one client from a multi-client skill |
| Regulated / finance promotion | arXiv:2608.17684 (full), SR-Fraud (full) | **partial**: no privacy, no erasure, no legal mapping |

**Verdict: not scooped as of 2026-09-25 [medium-high].** Scoop risk within about 3–6 months is **medium**. FederatedSkill's authors name poisoning as next; MemoRepair's could add multi-user; PoisonedEvolution's gate could be re-used for privacy. Novelty must come from the **combination plus finance obligations plus measurement**, because each component alone is occupied.

- **S1. Leakage bounds for skills built from many clients' traces** [high that it is absent; medium that it is tractable].
  - No skill paper provides DP, k-anonymity or an empirical cross-client leakage bound.
  - Evidence that distillation does not anonymise: 55–66% persona coverage (arXiv:2608.03700), whitewashing (arXiv:2608.03509), behavioural leakage (arXiv:2607.25560).
  - The industry analogue is AgentCore's cross-actor reflection warning.
- **S2. Erasure propagation from a client's traces to shared skills, including partial-contribution removal** [high absence].
  - MemoRepair withdraws whole cascades in a single agent.
  - Nobody tests "remove client i, re-derive, compare with a counterfactual skill built without i".
  - Nobody tests whether a skill whose support falls below k after erasure must be demoted.
  - SkillJack's 80% persistence after source deletion is the motivating number.
  - MemoRepair's 1% → 17.7% lineage sensitivity shows that lineage completeness is the binding constraint.
- **S3. One support-counting invariant for privacy, integrity and erasure** [medium; speculation].
  - "Promote only if supported by ≥k distinct clients" is simultaneously a k-anonymity-style privacy control, a Sybil or poisoning control (PoisonedEvolution), and an erasure trigger (demote or re-derive when support drops below k).
  - No paper connects the three.
  - Risk: Sybil clients defeat both the privacy and the integrity readings. Needs a threat model.
- **S4. Retention vs erasure at the skill level** [medium; legal parts [M]].
  - If a promoted skill is part of 206(4)-7 procedures, 204-2(a)(17)(i) requires keeping every version for 5 years [V].
  - If it embeds EU client data, GDPR Art. 17 applies [M].
  - This is GP1 specialised to skills; nobody has modelled it. It argues for **skills that are provably client-data-free at promotion time**, retained as records, with client-specific evidence kept in an erasable side store.
- **S5. Change control of promoted skills in finance** [medium].
  - Only one simulated finance audit exists (arXiv:2608.17684), and it shows promotion raising unauthorised financial actions.
  - There is no study of maker-checker cost or false-rejection burden, and no mapping to annual review or CCO duties. Industry guidance (Anthropic) prescribes separation of duties for *authored* skills but says nothing for *learned* ones.
- **S6. Behaviour-level cross-client leakage** [medium].
  - SigLeak shows skills are recoverable from trajectories. Nobody measures whether client A's specifics surface in client B's sessions through a shared skill.
  - The existing GP2 cross-client leakage benchmark could add this probe.
- **Relation to gaps.md N4 ("Memory → skill promotion governance: killed").** The kill rationale was that "mechanisms exist" and salience for RIA advisory is low.
  - Full-text reads now show the mechanisms cover *utility, regression, integrity and capability revocation*, not *cross-client privacy or data-subject erasure*.
  - Salience changed on 2026-09-25, when the PI put cross-user skill promotion in scope.
  - Recommendation: revive N4 as the **intersection of GP2 (cross-client leakage) and GP4 (erasure propagation)**, applied to derived skills, not as a standalone gap. [medium-high]
- **Relation to PI materials (CONFIDENTIAL; strip before sharing).** `inputs/INDEX.md` records that the PI's internal design already names a PROMOTE operation under dual control, a Promotion Regression Rate metric and compliance-aware promotion (C29), and lists "no mature policy for memory-to-skill promotion" as open. The literature supplies metrics for regression (flip accounting), integrity (SER) and revocation (OBLIVION/MemoRepair). It supplies **none** for cross-client leakage or partial erasure. That is where the PI's design has no external prior art to lean on, and also where a contribution would be novel.

---

## 11. Tool notes

- `lit.py arxiv` worked for all 39 queries. Some boolean queries drift to unrelated hits (for example "skill library" returned AI-for-science papers); screened manually.
- The shared scratchpad already contained another agent's query files (`ax/`). I moved mine to a separate folder; nothing was overwritten.
- SciSpace returned mostly ≤2026-01 papers (index lag). The unlearning question returned only generic machine-unlearning surveys (not stored).
- OpenAlex: the skills-mechanism query returned nothing. The model-risk query returned mostly off-topic records (not stored). The supply-chain query returned Zenodo grey literature (not stored except arXiv-backed items).
- eCFR redirected to a bot-check page, so the CFR text was taken from Cornell LII.
- Microsoft's Build blog was silent on procedural-memory scope; the scope semantics come from the Learn documentation.
- The 2608.29596 and 2607.10113 extractions were truncated, so those reads count as partial full-text.

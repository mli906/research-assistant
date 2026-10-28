# Evaluation of procedural memory and skill distillation: beyond success rate, and general vs finance

Facet: cross-cut of `skills` × `evaluation`. Companion to [`partials/skills.md`](partials/skills.md) §3/§6 (skill-formation systems and their eval), [`evaluation.md`](evaluation.md) §2–§5 (benchmark catalog, metric taxonomy, pitfalls, industry), and the PI eval-metrics materials indexed in [`../inputs/INDEX.md`](../inputs/INDEX.md) (SciSpace metric catalog M01–M26; M21–M22 are the procedural-memory metrics).

- **Question answered.** When an agent distills procedural memory / skills from traces, what is actually evaluated beyond task "success rate", what benchmark datasets exist, and how should the evaluation focus differ between general and finance-specific tasks?
- **Base date.** Synthesis of the library as of the 2026-09-25 `skills` scout and the 2026-09-24 `evaluation` synthesis. Refreshed by `/radar` — see §7 for the dated delta.
- **Evidence labels.** `full` = arXiv HTML read via fetch tool (extractive summary); `abs` = abstract only. Confidence on judgments in brackets.
- **Confidentiality.** No `inputs/` (RockAI) text is used here. The PI's internal metric acronyms (MLC, EC, CSLR, …) are referenced only by the public precedents they map to.

---

## 1. Success rate dominates skill-distillation eval — and that is itself a finding

Down the "Evaluation" column of the skill-formation comparison in [`partials/skills.md`](partials/skills.md) §3, nearly every system is scored on **downstream task success rate** (or pass@k) on a general agent benchmark:

- AWM (arXiv:2409.07429), ASI (arXiv:2504.06821), SkillWeaver (arXiv:2504.07079), ReasoningBank (arXiv:2509.25140) → WebArena / Mind2Web success rate.
- Voyager (arXiv:2305.16291) → Minecraft milestones; Agent KB (arXiv:2507.06229) → GAIA / SWE-bench pass@k; Memp (arXiv:2508.06433) → ALFWorld / TravelPlanner accuracy.

Success rate is the default because the implicit claim of procedural memory is "the agent gets *better* with experience," and success rate is the cheapest proxy for "better." Its weaknesses are documented in [`evaluation.md`](evaluation.md) §4: success/ASR are underspecified (65.3% of security papers report no variance; arXiv:2609.25173), free-abstention exploits inflate scores up to 38–40% on τ-bench (arXiv:2507.02825), LoCoMo/LongMemEval are saturating (91.4% in arXiv:2512.12818), and leaderboards mostly rank *specialization* not capability (agent main effect <3% of variance; arXiv:2608.11323). So success rate is both dominant and shallow. [high]

## 2. What is measured beyond success rate (distinct to procedural memory)

A skill library is **cumulative and mutable** — unlike read-only QA memory — so a second axis has emerged that scores the *dynamics* of the library, not just end-task score.

| Dimension | Why distinct to procedural memory | Metrics / benchmarks (id) | Evidence |
|---|---|---|---|
| **Efficiency / cost** | Payoff is "same result, fewer steps/tokens/$"; success hides it | steps/tokens reduction (ASI arXiv:2504.06821); $/case accuracy–cost Pareto (ESCROW/FRAMES arXiv:2608.01772); cost metering, dependent-task success (MERIT arXiv:2609.05441) | full/abs |
| **Regression / non-monotonicity** | Signature failure: a new skill fixes some tasks and silently breaks others; absent for read-only memory | W→C vs C→W flip accounting; hard regression budget (GRASP arXiv:2605.29668); anti-regression guarantee (FRAMES/ESCROW); "no prompt lost ∧ some won" (Designer-RSI arXiv:2609.22086); flip-centred gate (AgentDevel arXiv:2601.04620) | full/abs |
| **Formation quality** | Can traces be distilled into *good* procedures at all? | SkillEvolBench (episodic→procedural, arXiv:2605.24117); SkillsBench (curated +16.6pp vs **LLM-authored ≈ +0.0pp**, arXiv:2602.12670); skill coverage as test adequacy (arXiv:2606.20659) | abs |
| **Transfer / generalization** | Does a skill move to a new task, weaker model, another agent? | Memp (→weaker model); SkillWeaver (cross-agent); AFTER (cross-role/-model, arXiv:2606.23127); SkillsVote frozen-library transfer (arXiv:2605.18401) | abs |
| **Decision-grounding vs QA** | QA F1 overstates procedural competence | MemoryArena: near-perfect LoCoMo → **40–60% on decision tasks** (arXiv:2602.16313); Mem2ActBench (tool selection / argument grounding, not passive QA, arXiv:2601.19935) | abs |
| **Reliability / worst-case** | A skill working 90% but failing catastrophically 10% is unacceptable | pass^k worst-of-k (τ-bench arXiv:2406.12045); Violation@n accumulates over trials (arXiv:2511.14937) | full/abs |
| **Drift / retirement over time** | Libraries degrade as they grow; retirement can be disabled by judge bias | library-drift diagnostics (arXiv:2605.19576); contract-violation drift (arXiv:2605.10990); "blind curator" (arXiv:2607.07436); safe retirement (arXiv:2609.29543) | abs |
| **Retrieval / reuse** | Right skill found and applied under progress state | SkillRet (arXiv:2605.05726); progress-alignment at retrieval (WISE-Flow arXiv:2601.08158); skill shadowing | abs |
| **Governance** (project angle) | Leakage, erasure-propagation, poisoning — absent from capability eval | AntiSkillBench coverage/Field-QA/VocabGain (arXiv:2608.03700); SER poisoning (PoisonedEvolution arXiv:2608.05563); persistence after deletion (OBLIVION arXiv:2608.08264, MemoRepair arXiv:2605.07242, SkillJack 80% arXiv:2608.03509) | full/abs |

One-line framing: **general skill-distillation eval has moved from "did it succeed" → "did it get cheaper, does it transfer, and does promotion avoid regressions" — but almost always still on general-domain benchmarks.** [high]

## 3. General vs finance: the evaluation axis changes meaning

The driver is the **asymmetric cost of errors**. In a general web task the failure mode is "task not completed" (symmetric, recoverable). In finance a wrong trade/advice/disclosure is far costlier than a missed one and must be *provable* after the fact. That reorients evaluation:

| Shift | General focus | Finance focus | Evidence (id) |
|---|---|---|---|
| Central statistic | mean success rate / pass@k | **worst-case / harmful-action rate**; promotion can raise utility *and* unauthorized state changes jointly (0.583→0.685) | arXiv:2608.17684 (full); FinVault ASR + benign FP arXiv:2601.07853 |
| Success definition | task completed | **"completed within the rules"**: governed success, breach %, rejected-attempt rate, violation rate, HICS | Fiducia-bench arXiv:2608.16055; ReguSim arXiv:2608.19974; CNFinBench arXiv:2512.09506; FinGuard arXiv:2605.29427 |
| Evidence | — (rarely scored) | **auditability / provenance scored** (record-keeping): audit-trail sufficiency, authority diffusion, versioned auditable diff | Fiducia-bench; ESCROW arXiv:2608.01772; DEMM-Bench arXiv:2606.20634 |
| Adversarial | prompt-injection robustness | **sycophancy under rebuttal, risk-concealment red-teaming, "stated ≠ enacted"** (showing monitor the rationale nearly doubles false accepts 25%→46.9%) | Price of Agreement arXiv:2604.24668; FIN-Bench arXiv:2509.10546; arXiv:2608.19974 |
| Validity traps | contamination / benchmark retrieval | **look-ahead leakage in backtests** | Profit Mirage arXiv:2510.07920 |
| Error cost | missed = cheap | **over-blocking / benign false-positive scored** (over-refusal is a real cost) | FinVault benign FP; over-refusal GateMem arXiv:2606.18829 |

**Critical caveat (= [`evaluation.md`](evaluation.md) §7 gap 1 and [`partials/skills.md`](partials/skills.md) §10):** the two circles barely intersect **for procedural memory**. Finance safety benchmarks (FinVault, Fiducia-bench, ReguSim, CNFinBench) are **stateless / state-DB — no cross-session memory or skills**. Skill / procedural-memory benchmarks are **almost all general-domain, scored on success rate**. The finance + skill-formation evidence is three thin points:

- one simulated e-banking self-evolution audit (arXiv:2608.17684, full) — promotion ↑ utility *and* ↑ unauthorized financial state changes;
- one production fraud rule-admission system (SR-Fraud: one-sided Wilson bounds + admission cap + retirement, arXiv:2609.27287, full);
- FinEvo-Bench (longitudinal self-evolution on institution procedures, arXiv:2608.06144, abs); plus ESCROW/FRAMES on FinDAS document auditing (not core finance).

So the PI's intuition — "finance should evaluate differently" — is correct **and under-served**; that mismatch is the project's opening. [high that the intersection is near-empty; searched ≥6 phrasings across arXiv/SciSpace per the two source reviews]

## 4. Benchmark / dataset landscape at a glance

- **General skill / procedural eval:** WebArena, Mind2Web, ALFWorld, GAIA, SWE-bench, Terminal-Bench, MiniWoB++ (capability); SkillEvolBench, SkillsBench, AFTER (formation/transfer); MemoryArena, Mem2ActBench (decision-grounding).
- **Memory benchmarks drifting toward dynamics:** MemoryAgentBench (test-time learning + selective forgetting, arXiv:2507.05257), Evo-Memory (arXiv:2511.20857), MERIT (marginal utility + cost, arXiv:2609.05441), MemConflict/STALE (staleness, arXiv:2605.20926 / arXiv:2605.06527).
- **Finance (no persistent memory):** FinVault, Fiducia-bench, ReguSim, CNFinBench, FIN-Bench, FinanceBench (arXiv:2311.11944).
- **Finance + experience/memory:** FinEvo-Bench (arXiv:2608.06144), FinPerMA (investor-preference memory, arXiv:2608.04095); production: SR-Fraud, ESCROW.

## 5. Industry picture ([`evaluation.md`](evaluation.md) §5, [`partials/skills.md`](partials/skills.md) §7)

- **Memory vendors (Mem0, Zep, Letta):** report only recall accuracy, latency, token cost — and the numbers are not comparable (Zep 84% vs Mem0 re-run 58.44% on the same LoCoMo; Zep rebuttal 75.14%). No vendor publishes erasure, isolation or regression results for learned procedures.
- **Procedural-memory products (Foundry, AWS AgentCore, LangMem):** ship scoping + TTL but **no promotion review or distillation eval**. AgentCore alone flags the cross-actor privacy risk of reflections.
- **Authored-skill governance (Anthropic enterprise; Snyk/ClawHub scanners):** evaluate skills as *software* — triggering, isolation, output quality, maker-checker, vulnerability scans — but nothing on skills *learned from user data*.

Net: industry evaluation of procedural memory is almost entirely utility-side; governance and finance-grounded eval are a research frontier, not a product feature.

## 6. Pitfalls to carry into any eval we design ([`evaluation.md`](evaluation.md) §4)

1. Score **over-refusal / benign false-positives** — in a governance or compliance setting, refusal is the trivial exploit.
2. **ASR / success underspecified** — report N, CIs/bootstrap, k, judge model + rubric, latency percentile, memory-store version (matches the SciSpace template minimum-reporting rule and the PI's pinned-config rule).
3. **Judge validity compounds** (≤ V1·V2·V3); validate the judge and report IRR.
4. **Harness dependence** — memory-backend safety effects reverse across harnesses (Mem0 ±13.5pp E2E-ASR, arXiv:2607.27080); a skill result alone does not transfer.
5. **Contamination** — agents that search can retrieve benchmark answers; finance back-tests leak future information.
6. **Greedy decoding is optimistic for forgetting/leakage** — resurfaces under sampling (leak@k, arXiv:2511.04934); accumulates over trials (Violation@n).

## 7. My read + the opening

It is not merely that general vs finance "focus differently" — the **evaluation axis changes meaning.** General: the library is judged on *capability gain* (success↑, cost↓, transfer, no regression). Finance: the same library must be judged on *bounded harm and provability* (worst-case harmful-action rate, rule-grounding, audit-trail sufficiency, over-blocking cost) and on the **conflict** the governance work centers on — promotion raising utility *and* unauthorized actions at once. No existing benchmark measures a *learned, promoted skill* against finance obligations with worst-case + auditability + regression jointly.

Likely strongest contribution [med, speculative]: a **finance skill-promotion eval that pairs a capability delta with a tail-risk / compliance delta under a regression budget**, on execution-grounded tasks — i.e. take the finance-safety benchmarks' *scoring philosophy* (ASR, governed success, audit-trail, benign FP) and apply it to the skill-formation *setting* that only general benchmarks currently occupy.

---

## /radar delta

_(appended by `/radar`; newest first)_

### 2026-10-22 (window: since 2026-09-25) — full digest: [`radar-2026-10-22.md`](radar-2026-10-22.md)

23 new records added (library → 921). The eval field moved hard toward the §2 dimensions, still general-domain; the **finance × procedural-memory × governance-eval gap in §3 is intact** (medium scoop risk). Fold-ins:

- **§2 regression / non-monotonicity:** add **SAGE** (arXiv:2609.36043) — statistical acceptance gate; the naive "keep any edit that raises the aggregate" rule admits *permanent regressions*. A general-domain sibling of SR-Fraud; now a baseline for any promotion-gate contribution.
- **§2 formation quality / value of a skill:** add **Reliable Memory from Unstable Growth** (arXiv:2610.18427) — values playbook lessons by *measured causal effect* (randomized experiments); same procedure can write a playbook **69.6 pts below** no-playbook. Closest method for a promotion-regression metric. Pairs with **More Memory, Worse Agents** (arXiv:2610.27406, abstractions propagate errors) and the cautionary cost study **Persistent Memory in Multi-Agent Inference** (arXiv:2610.07782, persistent tier buys *no* accuracy at n=100/arm).
- **§2 retrieval / reuse:** add **Lost in Implicit Routing** (arXiv:2610.18522) — skill-routing collapse at scale: with 1,000 irrelevant skills loaded-skill recall 73.6%→27.4%. Retrieval is a first-class failure mode as libraries grow.
- **§2 decision-grounding / criteria beyond success:** **Agentic Cognitive Depth** (arXiv:2610.04168, trajectory-level criteria); **DSV-Mem** (arXiv:2610.08102, professional workflows with authority updates).
- **§4 new benchmarks:** **PraxisMemBench** (arXiv:2610.20022, personal × procedural memory interaction — closest to our question); **EngramBench** (arXiv:2609.39284, separates abstraction from contamination/rote leakage — attacks pitfall 5); **RSE-Bench** (arXiv:2610.19910, skill self-evolution under non-adversarial noise).
- **§3/§6 governance eval:** **MemJoin** (arXiv:2610.24359, latent cross-session / *compositional* leakage) and **MemForm** (arXiv:2610.14431, memory-formation poisoning across 5 interfaces) are the new precedents for the composition-leakage and write-path-integrity gaps. **Runaway Reaction** (arXiv:2610.05943) shows benign skills compose into malicious behavior despite passing isolation vetting.
- **§6 eval-validity:** **Auditing WebArena-Lite** (arXiv:2610.01491) finds auto-evaluator false negatives — reinforces pitfalls 1/9 (outcome-only scoring is unreliable).
- **§3 finance/regulated-adjacent (still no finance+skill+memory eval):** **JusticeAxis** (arXiv:2610.00353, rigid-rule vs ungrounded-discretion legal judgment) and **Frontier Autolab** (arXiv:2609.36739, organizational memory with temporal/look-ahead leakage).

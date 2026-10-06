# Phase 1 plan: offline trace→skill distillation + capability/governance harness

**Status:** draft for PI iteration (2026-10-06). Not pre-registered. This is a build+demo plan, not the `/design-experiments` pre-registration — that comes once the stack is standing and the question is frozen.
**Target:** internal demo + results by end of Q4 2026 (~12 weeks), as the seed for a Phase-2 paper. Not a paper for Q4.

## 0. Framing (why this, not "skills help")
"Distil skills from traces and show uplift" is very crowded (skills survey §9: ~80+ papers since 2026-01; AWM +51% WebArena; SkillClaw, ReasoningBank, ASI, SkillEvolBench, AFTER). So:
- **The pipeline is scaffolding we assemble from released code, not a new method.**
- **The contribution (Phase 2 paper) is the measurement:** capability uplift *and* governance/safety regressions, in finance, with a component/distiller ablation by task type. The under-occupied axes (skills survey §9): finance/regulated skill governance ("nearly empty"), capability-vs-safety together (arXiv:2608.17684 found promotion raised unauthorized financial state changes 0.583→0.685), and component decomposition.
- Continuity: the Phase-2 privacy/erasure work (ideas I1/I2/I5) plugs into the *same* harness as extra governance dimensions.

## 1. Stack (reuse first)
| Layer | Choice | Status | Notes |
|---|---|---|---|
| General trace→skill benchmark | **SkillEvolBench** (arXiv:2605.24117, `aiot-mlsys-lab/skillevolbench`, skillevolbench.github.io) | released; API-based (Bedrock Claude ok), Docker, Py3.12 | 180 tasks / 6 envs / 5 latent skill families × 6; T1–T3 acquisition, T4–T6 frozen eval; stressors = context shift / adversarial shortcut / composition. Baselines built in: no-skill, raw-trajectory RAG, self-gen (zero-shot + experience), curated (static + revision). **License not shown — resolve before fork/publish.** |
| Finance env (agentic) | **AgentDojo banking suite** (`ethz-spylab/agentdojo`, MIT) | **verified running, 16/16 ground-truth replay** | 16 user tasks, 9 injection tasks, 11 tools; gives unauthorized-state-change + injection-susceptibility metrics; same env as the e-banking audit arXiv:2608.17684. |
| Finance env (controlled) | **Synthetic RIA rebalancing** (`code/probes/`) | built; deterministic oracle | 7 hidden house-rules; no-skill beatable (≥30/40 fail), skill can matter; enables the policy-authored control. |
| Default distiller | SkillEvolBench self-gen (its own skill-author call) | in benchmark | the native arm. |
| Alt distiller(s) for ablation | **SkillClaw** (`AMAP-ML/SkillClaw`, MIT, Bedrock ok) | runs; adapter needed | summariser→grouping→create/evolve→verifier. Optionally AWM (`zorazrw/agent-workflow-memory`, Apache-2.0) and ReasoningBank (`google-research/reasoning-bank`, Apache-2.0). |
| Promotion gate | utility gate + **regression-aware gate** (reimpl. GRASP/Designer-RSI "no task lost ∧ some won"; arXiv:2605.29668, arXiv:2609.22086) | to build (~small) | logs lineage (skill→source traces) from day 1 → Phase-2 erasure hook. |
| Transfer complement (stretch) | **AFTER** (arXiv:2606.23127, `DavydenkoGr/AFTER`, HF dataset) | released | 382 enterprise tasks, 6 roles; local/cross-task/cross-role/cross-model regimes. Closest to a professional/finance-flavoured transfer bench. |

## 2. Pipeline (maps to the components the PI listed)
traces → [1 normalize/cluster] → [2 select exemplars] → [3 extract rules] → [4 induce workflow/code] → [5 promotion gate] → skill store → retrieval@inference, with a **held-out regression suite + safety probes** around stage 5. Stages 1–4 are distiller-internal (toggled for the ablation); stage 5 is where governance lives.

## 3. Experimental matrix (Phase-1 minimal)
- **Benchmarks:** SkillEvolBench (general) + AgentDojo banking + synthetic RIA (finance). AFTER if time.
- **Conditions per task:** {no-skill, raw-trajectory/few-shot, distilled-skill} + {policy-authored} on the RIA task (the honest control the ideation reviewer demanded).
- **Ablation (start here):** distiller family (self-gen vs SkillClaw vs AWM) × task category (SkillEvolBench's 5 skill families and its context-shift / shortcut / composition stressors; AgentDojo vs RIA). Full component-on/off ablation is a stretch goal.
- **Metrics:**
  - Capability: frozen-set pass rate vs baselines.
  - Regression: W→C vs C→W flip accounting on the frozen set; gate rejection rate; skill-shadowing as library grows (motivated by arXiv:2605.24050, up to 21% degradation).
  - Safety/governance (finance): unauthorized-state-change rate, injection-susceptibility (AgentDojo); suitability violations (RIA oracle).
  - Cost/efficiency: tokens, $, steps.
  - Provenance: lineage completeness (skill→traces).

## 4. Rough timeline (12 weeks)
1. **W1–3:** stand up SkillEvolBench on Bedrock Claude; reproduce its no-skill vs self-gen baselines (sanity). Wire AgentDojo banking + RIA to a shared metrics harness.
2. **W4–7:** integrate SkillClaw as an alt distiller (adapter); build the regression-aware gate + lineage log; add finance safety metrics.
3. **W8–10:** run the matrix (baselines + distiller×category ablation) on general + finance.
4. **W11–12:** analysis, demo, results table; write findings as the Phase-2 paper seed.

## 5. Open checks before locking (do first)
1. **SkillEvolBench license** — not visible on the repo; resolve before forking/publishing results.
2. **Distiller pluggability** — read SkillEvolBench's self-gen baseline to confirm a custom skill-author can be swapped in without a rewrite.
3. **Paper-angle novelty radar (for Phase 2, not blocking Phase 1):** read arXiv:2608.14036 "Demystifying Agent Skills: Why They Work—Until They Don't" (directly adjacent to the capability-vs-safety angle; now in library, tag `skills-demo-scout`) and arXiv:2608.14036-style follow-ups; confirm no one has published the finance capability-vs-safety + component-ablation combination.

## 6. Open PI decisions (carried)
- **Null/mixed result acceptance** — undecided; revisit at the analysis checkpoint (checkpoint 4). Given §9 and arXiv:2608.17684 it's a live outcome.
- **General benchmark** — SkillEvolBench selected as primary (purpose-built for trace→skill); AFTER as transfer stretch. (PI's "handy dataset aligned with the trace→skill task" → SkillEvolBench.)
- API key needed to run any generation (budget not a concern per PI; checkpoint 3 still applies before the big run).

## 7. Deferred (Phase 2+)
Online trace ingestion + skill enhancement; privacy/erasure governance (I1 support-threshold/lineage, I2 cross-client leakage, I5 resurrection) as harness dimensions; adaptive/generalizable; proprietary RIA traces (with approval, never sole basis); the paper.

# Auditing self-evolution in financial agents (arXiv:2608.17684)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core. Two independent researchers.

- **Setting.** AgentDojo Banking suite (simulated e-banking: 15 task families, 9 injection goals, 11 tools). The study audits SkillOpt, Agent Workflow Memory (AWM) and ReasoningBank after one offline benign evolution pass. Executor: Qwen 3.7 Flash, temperature 0, 3 lineages.
- **Protocol.** Byte-identical benign acquisition trajectories, sealed evaluation endpoints, execution-grounded checks on terminal financial state, and independent state replay.
- **Results (static → evolved).**
  - SkillOpt: utility 0.741 → 0.837; exposure 0.820 → 0.943; conditional ASR 0.605 → 0.562; total ASR 0.496 → 0.530; **unauthorised state change 0.583 → 0.685**. It had 23 wrong→correct gains against **10 correct→wrong regressions**.
  - ReasoningBank: utility 0.859 with 25 gains and 9 regressions.
  - AWM literal port: 0.319 utility, but this was an execution-interface artefact. 380/540 rollouts emitted text actions and executed zero tools. After fixing the tags: utility 0.756, ASR 0.575.
  - Direction was consistent in 3/3 lineages for SkillOpt utility, exposure and unauthorised change.
- **Limitations (stated).** One executor, one simulated environment, 3 lineages with no significance claims, one pass. System differences are confounded.
- **Critique.** This is the **only finance-domain evidence** that promoting learned procedures raises capability *and* the rate of unauthorised financial actions, while regressing previously-correct cases. This is the model-risk argument for gated promotion. It makes no regulatory mapping and has no cross-user data or privacy dimension. It is a methodological template (per-case flip accounting, execution-grounded harm) for any promotion-gate evaluation.

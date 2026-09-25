# SkillClaw: collective skill evolution across users (arXiv:2604.08377)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core. Alibaba (DreamX / AMAP-ML).

- **Problem.** Skills in deployed agents (OpenClaw) stay static; users rediscover the same workflows and failures. Goal: turn *cross-user* interaction into skill updates.
- **Method.** Sessions (prompt, actions, environment/user feedback, final response) are grouped per invoked skill across users. An "agentic evolver" chooses Refine / Create / Skip, treating successful sessions as invariants and failed sessions as targets. Nightly validation in idle user environments: a candidate is accepted only if it beats the deployed skill on the corresponding validation tasks. Accepted skills are **synchronised to all users**.
- **Data.** WildClawBench, 60 tasks in 6 domains; 8 concurrent users; 6-day run.
- **Results.** Search & Retrieval 22.73 → 34.55%; Creative Synthesis 11.57 → 21.80%; Safety & Alignment 24.00 → 32.00%; Social Interaction 54.01 → 60.34%.
- **Limitations (stated).** Small-scale test: few users, short horizon, limited feedback.
- **Critique.** This is the reference design for **per-user traces promoted into a shared skill pool**. The paper has **no** discussion of privacy, PII, consent, isolation, deletion, provenance or security (checked in full text). Its only gate is a utility gate. PoisonedEvolution (arXiv:2608.05563) attacks exactly this pipeline, with 91% skill embedding at 10% attacker support. For the PI, it is the natural "ungoverned promotion" baseline.

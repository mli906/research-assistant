# Designer-RSI: procedural memory evolved from user traffic (arXiv:2609.22086)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core. Adobe and Brown.

- **Setting.** A frozen frontier model drives professional design software (230+ tools). An external bank of natural-language skills evolves from **real user briefs**: 1,406 briefs from user traffic plus LLM-augmented variants, and 1,869 auto-graded trajectories over 5 rounds.
- **Mechanism.**
  - *Widen*: a recurring uncovered subtask seen **k_min = 3** times is distilled into a candidate skill.
  - *Deepen*: contrast a skill's failed and successful executions.
  - **Matched replay gate**: ship only if (no prompt lost) and (at least one prompt won) on frozen contexts, judged pairwise.
- **Results.**
  - Bank grew from 76 to 139 skills.
  - The gate rejected 100/231 rewrites (43%) and 67/136 mints (49%).
  - GenEval2 execution success on Claude-Sonnet-4 rose from 72.7% to 99.3%.
  - Widen + deepen combined gave a 58.5% win rate vs 49.4/48.6% for either alone.
- **Limitations (stated).** The replay gate is local: "rejecting observed regressions on the replay set does not guarantee monotonic improvement over the full user-traffic distribution."
- **Critique.** This is a production-like **trace-to-shared-skill pipeline built from many users' data**, with a regression gate. It has **no discussion of privacy, consent, provenance to source briefs, or deletion** (checked). Its k_min = 3 counts *occurrences*, not *distinct users*, so it gives no anonymity property. This is concrete evidence that industry labs promote user-derived procedures with a utility gate only.

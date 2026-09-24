---
name: design-experiments
description: Turn the chosen idea into pre-registered hypotheses and an experiment plan with budget.
argument-hint: [project-slug]
---
Arguments: $ARGUMENTS (default: most recently modified project).

1. Confirm the chosen idea from `STATE.md`.
2. Delegate to `experiment-designer`.
3. Have `reviewer` critique the design as a skeptical reviewer would ("what would make me reject
   this paper even if the results are positive?"). Apply fixes.
4. Present: the hypotheses (one line each), the pilot experiment, the main experiments,
   total compute/time/cost, and the risks.
5. **Checkpoint:** PI approves the plan, the budget, and the held-out harness in
   `experiments/sealed.staging/` (if any). Then:
   - set `**Status:** pre-registered <date>` in each hypothesis and commit (a hook then freezes
     everything above the Deviations log);
   - `python3 tools/seal.py seal projects/<slug>` (only with the PI's explicit OK).
   From then on, changes are appended to the Deviations log with date and reason.

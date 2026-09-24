---
name: find-gaps
description: Identify research gaps and open directions from the project's literature base.
argument-hint: [project-slug]
---
Arguments: $ARGUMENTS (default: most recently modified project).

1. Make sure `literature/review.md` exists. If it doesn't, offer `/lit-review` first.
2. Delegate to `gap-analyst` with the project path.
3. Have the `reviewer` agent do a quick adversarial pass on the top 5 gaps in `gaps.md`
   (is it really open? who is already working on it? does it matter?).
   Fold its objections into `gaps.md` under each gap.
4. Update `STATE.md`. Present the ranked top 5 with a sentence each, including confidence.
5. **Checkpoint:** ask the PI which gaps to pursue (AskUserQuestion, multiSelect),
   or whether their own intuition points somewhere else. Record the choice in `STATE.md`.

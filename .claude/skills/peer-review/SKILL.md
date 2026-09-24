---
name: peer-review
description: Simulated top-venue peer review of an idea, design, or paper draft (artifact-aware, error-hunt first), plus a revision plan.
argument-hint: [project-slug] [target: paper | design | idea] [venue]
---
Arguments: $ARGUMENTS (default target: paper; venue from `brief.md`).

1. Launch **3 `reviewer` agents in parallel**, each told to review the artifacts, not just the manuscript,
   and each given a different required focus:
   (a) methods/soundness: statistics, the error hunt, fidelity, held-out usage, baselines;
   (b) domain expert: novelty against the literature (independent search), related work, citation sampling;
       for this PI's area, also regulatory accuracy;
   (c) skeptical generalist: significance, overclaiming, clarity, and whether a practitioner would care.
   Each writes its own section of `reviews/round-<N>.md` without seeing the others (this prevents converging on the same view).
   If the PI has given access to a model from another vendor, one review may come from it.
2. Meta-review (you): consensus weaknesses, disagreements, and a likely decision. Check that each
   reviewer's score is consistent with its flagged concerns (the cap rules in `reviewer.md`).
   Say plainly that simulated scores are not evidence of quality and must not be optimized.
3. Draft `reviews/response-<N>.md`: every weakness → planned action (new experiment, text change,
   rebuttal argument) → effort → which command does it.
4. Present the verdict, the top 3 must-fix issues, and the revision plan. **Checkpoint:** the PI picks what to do.

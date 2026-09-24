---
name: peer-review
description: Simulated top-venue peer review of an idea, design, or paper draft, plus a revision plan.
argument-hint: [project-slug] [target: paper | design | idea] [venue]
---
Arguments: $ARGUMENTS (default target: paper; venue from `brief.md`).

1. Launch **3 `reviewer` agents in parallel**, each with a different persona passed in the prompt:
   (a) methods/soundness expert, (b) domain expert focused on novelty and related work,
   (c) skeptical generalist focused on significance and clarity. Each writes a section
   of `reviews/round-<N>.md`.
2. Write the meta-review yourself: consensus weaknesses, disagreements, and a
   likely decision.
3. Draft `reviews/response-<N>.md`: every weakness → planned action (new experiment,
   text change, rebuttal argument) → effort → which command does it.
4. Present the verdict, the top 3 must-fix issues, and the revision plan. **Checkpoint:** PI picks what to do.

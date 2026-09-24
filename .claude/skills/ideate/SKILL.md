---
name: ideate
description: Brainstorm, novelty-check, and rank research ideas for selected gaps; optionally a live brainstorm with the PI.
argument-hint: [project-slug] [gap numbers or a seed idea]
---
Arguments: $ARGUMENTS (default: most recently modified project, gaps chosen in `STATE.md`).

1. If the PI gave a seed idea, include it and treat it with the same rigor. Don't flatter it.
2. Delegate to `ideator` with the project path and chosen gaps.
3. Send the top 3 to `reviewer` for a fatal-flaw pass. Revise or drop based on the result.
4. Present the top 3 as short pitches with novelty delta, key experiment, risk and scores,
   plus your recommendation.
5. **Checkpoint:** the PI picks an idea (or asks for a live brainstorm: go back and
   forth, build on their suggestions, and push back where warranted). Record the decision
   and rationale in `STATE.md`. Suggest `/design-experiments`.

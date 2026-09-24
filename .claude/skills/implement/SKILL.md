---
name: implement
description: Implement and run the experiment plan (pilot first), with a reproducible codebase and lab log.
argument-hint: [project-slug] [experiment id, e.g. pilot | E2 | reproduce <paper>]
---
Arguments: $ARGUMENTS (default: next pending experiment in `experiments/plan.md`).

1. Delegate to `research-engineer` with the project path and the specific experiment.
2. After the pilot, evaluate the go/no-go criteria from the plan and report to the PI
   before starting the main runs.
3. For each completed experiment: results table, figure paths, and a one-paragraph
   interpretation against the pre-registered prediction.
   **Checkpoint:** don't declare a hypothesis supported or refuted until the PI has seen the analysis.
4. If results are negative or surprising, say so plainly and propose next steps
   (debug, redesign, pivot to `/ideate`, or write it up as a negative result).
5. Update `STATE.md` and `experiments/log.md`.

---
name: implement
description: Implement and run the experiment plan (pilot first), with a reproducible codebase, run manifests with fidelity audit, sealed held-out evaluation, and lab log.
argument-hint: [project-slug] [experiment id, e.g. pilot | E2 | reproduce <paper>]
---
Arguments: $ARGUMENTS (default: next pending experiment in `experiments/plan.md`).

1. Delegate to `research-engineer` with the project path and the specific experiment.
2. After each run, **check fidelity yourself**: `python3 tools/fidelity.py projects/<slug>`.
   Show the PI any deviation (planned vs actual), including approved ones. Undeclared deviations
   are a stop-the-line event: investigate before interpreting any result.
3. After the pilot, evaluate the go/no-go criteria and report to the PI before main runs.
4. Held-out evaluation only through `python3 tools/seal.py run`, only for frozen systems,
   within the pre-registered budget of evaluations. Report the count.
5. For each completed experiment: results table, figure paths, and a one-paragraph
   interpretation against the pre-registered prediction.
   **Checkpoint:** don't declare a hypothesis supported or refuted until the PI has seen the analysis.
6. If results are negative or surprising, suspect the evaluator first, then say so plainly and
   propose next steps (debug, redesign, pivot to `/ideate`, or write up as a negative result).
7. Update `STATE.md`, `experiments/log.md`, `experiments/failures.md`.

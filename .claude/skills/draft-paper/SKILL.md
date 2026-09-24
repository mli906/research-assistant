---
name: draft-paper
description: Draft or revise the paper in LaTeX from project artifacts, with verified citations.
argument-hint: [project-slug] [section | "full" | "revise"]
---
Arguments: $ARGUMENTS (default: full draft for the most recently modified project).

1. Delegate to `paper-writer`. For "revise", pass it the latest `reviews/round-N.md`.
2. Run `python3 tools/lit.py verify projects/<slug>/paper` yourself and fix every problem.
3. Cross-check every number in the paper against `experiments/results/`.
4. Try to build the PDF. Report the page count and any build problems.
5. Present: the contribution sentence, outline, anything the draft had to hedge, and
   suggest `/peer-review`.

---
name: draft-paper
description: Draft or revise the paper in LaTeX from project artifacts, with numbers generated from results and citations verified against the library.
argument-hint: [project-slug] [section | "full" | "revise"]
---
Arguments: $ARGUMENTS (default: full draft for the most recently modified project).

1. Make sure analysis scripts have regenerated `paper/generated/` from the current results.
2. Delegate to `paper-writer`. For "revise", pass it the latest `reviews/round-N.md` and `response-N.md`.
3. Run yourself, and fix every problem:
   - `python3 tools/lit.py verify projects/<slug>/paper` (online: ids resolve, titles match, all cited papers are in the library);
   - `python3 tools/check_numbers.py projects/<slug>/paper` (no hand-typed result numbers);
   - `python3 tools/fidelity.py projects/<slug>` (deviations disclosed in the paper?).
4. Build the PDF. Report the page count and any build problems.
5. Present: the contribution sentence, outline, what the draft had to hedge, and the disclosed
   deviations. Suggest `/peer-review`.

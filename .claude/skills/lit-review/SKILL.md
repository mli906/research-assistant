---
name: lit-review
description: Run a systematic literature + industry-practice review for a project (SciSpace, arXiv, OpenAlex, web).
argument-hint: [project-slug] [optional focus or "refresh"]
---
Arguments: $ARGUMENTS. If no slug is given, use the project most recently modified in `projects/`.

1. Read `projects/<slug>/brief.md` and `STATE.md`.
2. Delegate to the `lit-scout` agent with the project path, the brief's scope,
   and the recency window (default: frontier = last 12 months; foundations = any date).
   For broad topics, split the facets across 2–3 `lit-scout` agents in parallel
   (e.g. academic methods / evaluation & benchmarks / industry practice). Each
   agent writes its own partial notes, and you merge them.
   If "refresh" is passed, search only since the last review date in `STATE.md`, and append.
3. Check the output yourself: spot-check 3 claims in `review.md` against
   `papers.jsonl` abstracts. Fix or flag anything unsupported.
4. Update `STATE.md`. Present to the PI: landscape in ~10 bullets, the frontier
   (what changed recently), top 5 must-read papers with links, and the academia-vs-industry
   picture. Suggest `/find-gaps` next.

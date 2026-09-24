---
name: ideate
description: Brainstorm, novelty-check, tournament-rank and feasibility-probe research ideas for selected gaps; optionally a live brainstorm with the PI.
argument-hint: [project-slug] [gap numbers or a seed idea]
---
Arguments: $ARGUMENTS (default: most recently modified project, gaps chosen in `STATE.md`).

1. If the PI gave a seed idea, or `inputs/` contains exploratory ideas, include them with the same rigor.
   Don't flatter them.
2. Delegate to `ideator` with the project path and chosen gaps → `ideas.md` (no scores).
3. **Tournament** (the ideator never judges its own ideas):
   - `python3 tools/rank.py pairs I1 I2 ... > ideas/pairs.jsonl` (both orders, to control position bias).
   - Launch 2–3 `reviewer` agents in parallel as judges, each with a different persona (methods
     rigor; domain/regulatory impact; practitioner feasibility). Each judges every pair on
     `significance`, `novelty (from the overlap table)` and `feasibility` and appends JSON lines
     to `ideas/judgments.jsonl`.
   - `python3 tools/rank.py score ideas/judgments.jsonl` overall and per `--criterion`. If position
     consistency is low, say so. The ranking is then weak evidence.
4. **Feasibility probe** for the top 2–3: at most 1 hour or $5 of API each. Check that the data exists and is
   accessible, run the key baseline on 10–20 items, and check the key mechanism is implementable
   (a tiny spike in `code/probes/`). Record the findings in `ideas.md`. Execution-grounded feasibility
   is better evidence than judged feasibility.
5. `reviewer` fatal-flaw pass on the top 3.
6. Present the top 3 as short pitches with the overlap-table verdict, tournament results, probe results,
   risk and cost, plus your recommendation. **Checkpoint:** the PI picks (or asks for a live
   brainstorm: go back and forth, build on their suggestions, and push back where warranted).
   Record the decision and rationale in `STATE.md`. Suggest `/design-experiments`.

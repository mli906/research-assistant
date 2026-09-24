---
name: research-new
description: Start a new research project - interview the PI, write the brief, scaffold the workspace.
argument-hint: <topic or research question>
---
Start a new research project on: $ARGUMENTS

1. Propose a short kebab-case slug. Create `projects/<slug>/` by copying
   `templates/project/` (`cp -R templates/project projects/<slug>`), then
   `git init` inside `projects/<slug>/code`.
2. Interview the PI briefly (use AskUserQuestion, max 4 questions, and skip anything
   already stated): field/sub-area and their expertise; goal (paper at which
   venue/deadline, thesis chapter, internal R&D, grant); resources (compute, data
   access, time, collaborators); preferences (theory vs empirical, risk appetite),
   and anything off-limits.
3. Fill in `brief.md` and initialize `STATE.md` (stage 0 done, decisions logged with date).
4. Do a quick 3-query scan (SciSpace + `python3 tools/lit.py arxiv --since <6 months ago>`)
   and report 3–5 early observations about the landscape. This checks the scope before the
   full review.
5. **Checkpoint:** show the brief and ask the PI to confirm or adjust scope. Suggest `/lit-review` next.

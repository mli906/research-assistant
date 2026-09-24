# Research Assistant (Claude Code)

Open this folder in Claude Code (`cd ~/research-assistant && claude`) and run:

```
/research-new <your topic>     frame the project, write the brief
/lit-review                    academic + industry survey (SciSpace, arXiv, OpenAlex, web)
/find-gaps                     gaps with evidence and confidence  → you choose
/ideate [seed idea]            brainstorm + novelty check + critique → you choose
/design-experiments            pre-registered hypotheses + plan + budget → you approve
/implement [pilot|E1|...]      reproducible code, runs, lab log
/draft-paper [section|revise]  LaTeX draft, citations fetched and verified
/peer-review                   3 simulated reviewers + meta-review + revision plan
/research-status  /radar       where are we; what's new since last time
```

Or just talk to it: "let's brainstorm around gap 2", "reproduce paper X", "why did E3 fail?".
See `CLAUDE.md` for the rules the agents follow (no fabricated citations or results,
pre-registration, human checkpoints).

Optional: `export S2_API_KEY=...` (free from semanticscholar.org) for citation snowballing;
`brew install tectonic` to build PDFs.

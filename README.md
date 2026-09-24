# Research Assistant (Claude Code)

Open this folder in Claude Code (`cd ~/research-assistant && claude`) and run:

```
/research-new <your topic>     frame the project, write the brief
/ingest                        catalog your own materials dropped in projects/<slug>/inputs/
/lit-review                    academic + industry survey (SciSpace, arXiv, OpenAlex, web)
/find-gaps                     gaps with evidence and confidence  → you choose
/ideate [seed idea]            brainstorm + per-claim novelty check + pairwise tournament + feasibility probe → you choose
/design-experiments            pre-registered hypotheses + plan + budget → you approve
/implement [pilot|E1|...]      reproducible code, runs with planned-vs-actual audit, sealed held-out eval, lab log
/draft-paper [section|revise]  LaTeX draft; numbers generated from results; citations verified against the library
/peer-review                   3 simulated reviewers + meta-review + revision plan
/research-status  /radar       where are we; what's new since last time
```

Or just talk to it: "let's brainstorm around gap 2", "reproduce paper X", "why did E3 fail?".
See `CLAUDE.md` for the rules the agents follow (no fabricated citations or results,
pre-registration, human checkpoints).

Your materials: put SciSpace reviews, surveys, notes and prototypes in `projects/<slug>/inputs/` and run
`/ingest`. Paper lists exported from SciSpace, Zotero or elsewhere (CSV/RIS/BibTeX) go in `literature/imports/`.

Zotero: enable Settings > Advanced > "Allow other applications on this computer to communicate
with Zotero", and the agents can pull collections and read your PDFs' full text.

Integrity checks run automatically as hooks (see `CLAUDE.md` > Automatic checks).
The audit of this pipeline against autoresearch literature is in `meta/pipeline-review.md`.

Optional: `export S2_API_KEY=...` (free from semanticscholar.org) for citation snowballing;
`brew install tectonic` to build PDFs.

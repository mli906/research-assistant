# Attack Success Rate Is Not a Number: measurement validity in agentic AI security evaluation (arXiv:2609.25173)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Argument.** ASR is a family of metrics with 6 design choices that are rarely reported: unit (injection/task/trajectory), success oracle, trials/nondeterminism, attacker adaptivity, defense knowledge, and partial-success binarization.
- **Evidence.** Meta-analysis of 259 arXiv papers (Feb 2025–Sep 2026): 65.3% report no variance or repeats; 30.9% disclose decoding; 24.7% use LLM judges, and only 29.7% of those validate against humans; 30.5% evaluate adaptive attackers; 2.3% define partial success. Analytically, at 100 instances the minimum detectable difference at 80% power is ≈18.2 pp, and 5-pp defense differences are mis-ranked ≈21% of the time.
- **Recommendation.** A 10-item reporting checklist, including benign utility alongside ASR.
- **Limitations (stated).** arXiv/English only; automated coding (κ=0.75); analysis is analytical, not empirical.
- **Critique.** Directly applicable to memory-poisoning evaluation, where almost all papers report single-run ASR.

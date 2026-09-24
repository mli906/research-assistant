# Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research (arXiv:2412.06966)
Read: abstract + arXiv abstract page only (2026-09-24). Facet: regulation.
- Problem: policy discourse treats "unlearning" as a remedy for privacy (GDPR Art. 17), copyright and safety in generative models.
- Argument: two goals are conflated: (1) removing information from model parameters; (2) suppressing certain outputs. Neither maps cleanly onto legal erasure; unlearning is a poor general-purpose policy tool. Large interdisciplinary author team (ML, law, policy).
- Relevance to agent memory: strengthens the case that erasure obligations for agents should be met at the *memory/store layer* (explicit, addressable records) rather than by parameter unlearning. It also warns that "output suppression" (guardrails) is not deletion, which matters when a regulator asks whether data was erased or only hidden.
- Critique: policy paper, no finance-specific analysis; says nothing about external memory stores, where deletion is more tractable but, see arXiv:2606.18497, not trivial either.

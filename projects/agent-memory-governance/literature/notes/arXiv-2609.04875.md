# Forgetting Without Restarting: execution-state unlearning for stateful agents (arXiv:2609.04875, 2026-09-04)
Read: arXiv HTML full text via fetch tool. Tags: threats, core.

- **Definition.** After a forget request for z seen at step tau, the agent must be indistinguishable from a twin that never saw z (exact, or epsilon under sampling).
- **Theory.** Everything before tau is shared for free. Without token-level attribution, everything after tau is tainted; an exact unlearner needs at least T-tau+1 transitions, and their selective replay meets that bound.
- **Empirics.** Deleting the memory record leaves any-leak at **0.86-1.00** (no better than no deletion). Instruction-based forgetting fails under 6 probes (Leak@probes 1.00). Source redaction: **80%** of episodes still act on the revoked preference with zero string leakage. Selective replay: 0.00 leakage, 9x fewer recomputed tokens than a full reset.
- **Limitations.** Runtime state only (not weights); needs snapshot-replayable tools; cannot undo external side effects.
- **Critique.** This gives a formal basis for a GDPR Art. 17 claim of "erasure" in agent memory, and shows that a record-delete API is not erasure. Cost grows with the time since the target was observed, so erasure is expensive for long-lived client agents.

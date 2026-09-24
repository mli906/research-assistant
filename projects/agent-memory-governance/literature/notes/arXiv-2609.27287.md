# SR-Fraud: outcome-supervised reflective LLM agent for payment fraud (arXiv:2609.27287)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core. Authors from Coinbase and Ohio State.

- **Design.** A *stateless* request-time decision agent scores each transaction from a "Hybrid Episodic Window" (recent user sequence plus velocity summaries). Weekly, an offline reflection agent proposes boundary rules from **matured** errors, with a 2-cycle label-maturation lag. A **deterministic verifier** (one-sided Wilson bounds) admits rules into a human-readable "expert knowledge state", with an admission cap per cycle and a conservative retirement rule. An optional human-review gate precedes deployment.
- **Data.** Proprietary production stream: 16,140 transactions over 9 weeks, 813 fraud cases (case-control sample). Not releasable.
- **Results vs CatBoost.** +4.5 precision, +12.3 recall, +8.0 F1, +11.7 dollar-weighted recall. On a burst week, +41.7 recall.
- **Limitations.** No multiple-testing correction; single proprietary stream; no repeated full-stream runs.
- **Critique.** This is a good **governed memory-write** pattern: learned memory is gated by statistical verification, versioned weekly and human-readable. It maps well to model-change management under SR 11-7. It also shows the industry separating per-request statelessness from slow, audited memory updates. It is not about client memory.

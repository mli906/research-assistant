# Stateless Decision Memory for Enterprise AI Agents (DPM) (arXiv:2604.20158)
Read: full text (arXiv HTML, 2026-09-24, via WebFetch extraction). Tags: finance-apps, core.

- **Claim.** Regulated deployments (underwriting, claims, tax exams) prefer RAG over stateful memory because they need four properties: **deterministic replay, auditable rationale, multi-tenant isolation, statelessness for horizontal scale**. Stateful memory architectures violate these by construction.
- **Method.** Deterministic Projection Memory: an append-only immutable event log plus one task-conditioned projection at decision time (temperature 0). There are no intermediate memory writes.
- **Data.** 10 synthetic cases (5 mortgage under ECOA/Reg B, 5 insurance claims), 26–28k characters each; a single model (Claude Haiku 4.5).
- **Results.** Under a tight budget (20x compression), factual precision is 0.907 vs 0.392 for incremental summarization (h=1.17, p=0.001) and reasoning coherence is 0.800 vs 0.267. The two are at parity under moderate and loose budgets. DPM is 7.4–14.9x faster (1 call vs 82–96).
- **Limitations.** n=10; one model family; same-model judge; API nondeterminism.
- **Release.** Code at github.com/vasundras/stateless-decision-memory-enterprise-ai-agents; CC BY-NC-ND 4.0.
- **Critique.** This is the clearest statement of *why* regulated industry avoids agent memory, and the four properties map directly onto SR 11-7 and record-keeping obligations. It is weak empirically (n=10), and it does not handle cross-session client memory (preferences), deletion, or consent. A "log + projection" design also makes erasure easy to reason about, which is worth testing.

# Dependency-Guided Rollback Repair for memory-augmented agents (arXiv:2608.10502, 2026-08-11)
Read: arXiv HTML full text via fetch tool. Tags: threats, core (also mechanisms).

- **Problem.** Post-failure recovery. Deleting a faulty memory leaves claims, actions and memories derived from it in place; a full reset destroys benign state.
- **Method.** A typed memory-to-action provenance graph. Trace downstream nodes, keep items with independent trusted support, deactivate unsupported state, and replay only the answer-relevant steps.
- **Benchmark.** 150 cases (shopping, travel, support) with 4 fault types: poisoned, stale, wrong-user, summary-drift. Plus 50 trajectories adapted from LongMemEval-V2.
- **Results.** Recovery 85.3% vs 77.3% for the best baseline (LLM-judge). 100% faulty removal, 100% benign preservation, replay ratio 12.3% vs 21.7%, 5.7 vs 9.8 LLM calls. Transfer set: 68.0% vs 54.0%.
- **Limitations.** Needs a fully instrumented runtime; cannot undo external side effects.
- **Critique.** The "wrong-user" fault type is cross-client contamination, directly relevant to finance. Irreversible side effects (executed trades) are the real open problem.

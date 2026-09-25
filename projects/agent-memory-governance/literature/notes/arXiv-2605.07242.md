# MemoRepair: barrier-first cascade repair in agentic memory (arXiv:2605.07242)
Read: full text (arXiv HTML via WebFetch extraction, 2026-09-25). Tags: skills, core (already in library).

- **Problem (cascade update).** "When a source artifact is deleted, corrected, or invalidated ... descendants derived from that source can remain visible." Descendants include summaries, cached outputs, **prompt skills, chain procedures and neural skills**.
- **Method.** A provenance graph with influence edges. On a repair event (delete, correct, migrate), withdraw the whole cascade C(F) (non-servable). Build successors with remove, recompute, regen or param operators (LUNE for neural skills). Republish only if the successor validates, with predecessor closure.
- **Data.** ToolBench and MemoryArena.
- **Results.**
  - Leak% is 0 vs 69.8–94.3% for cascade-unaware systems; stale-use% is 0 vs 92.4–99.7%.
  - It recovers 91.1–94.3% of repair-all at 0.57–0.76 cost.
  - Neural skills: forget-set suppression 86.4%, validation pass 84.9% (full retrain 92.5%).
- **Limitations (stated).** "Relies on complete influence provenance". **Dropping 1% of edges yields 17.7% leak.** Validation is not semantic correctness. There is no exact parameter erasure.
- **Critique.** This is the **closest existing mechanism for erasure propagation to derived skills**, but it is motivated by staleness and correction, not GDPR. It is single-agent, has no multi-user or shared skills and no legal retention. The 1% → 17.7% sensitivity is a strong argument that lineage completeness is the binding constraint. When one skill is derived from many clients, partial-contribution removal (as opposed to withdrawal) is not modelled.

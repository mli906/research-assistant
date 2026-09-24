# Ghost Echoes: semantic erasure failure in retrieval-backed applications (arXiv:2608.20352)
Read: full text (arXiv HTML), accessed 2026-09-24. Tags: evaluation, core.

- **Problem.** Vector DBs implement API-visible deletion correctly, yet deleted records leave measurable residual influence on retrieval via HNSW graph topology.
- **Method/data.** Black-box, API-only query induction (NES). Controls: no delete, unrelated-cluster delete, and same-cluster non-target delete (the main baseline). ChromaDB, 500 synthetic healthcare records, MiniLM embeddings, 18 targets × 3 seeds. Cross-checked on FAISS, Pinecone, Weaviate and Milvus.
- **Metrics.** Centroid drift of the top-K context, vocabulary shift (Jaccard), vanish-token residue, Hallucination Adoption Potential, differential latency.
- **Results.** API deletion excludes the IDs 100% of the time (270 trials), but target-deletion drift is 3.7× the same-cluster control (0.152 vs 0.041; 53/54 pairs, p<0.001). Detection accuracy is 61.1% with 5 queries; there is a +15.7 ms latency oracle. Full index rebuild does not remove the drift in their setting. Their proposed ITEP primitive reduces drift by 99.2% in a controlled setting.
- **Limitations (stated).** Primarily one backend; shows retrieval drift, not reconstruction of content.
- **Critique.** The most concrete *erasure verification* protocol for vector memory found. It shows "deletion succeeded at the API" ≠ "no residual influence". The rebuild result is surprising and needs replication. Single author group, synthetic data.

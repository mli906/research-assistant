# Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases (arXiv:2606.18497)
Read: abstract only (arXiv page, 2026-09-24). Facet: regulation (also mechanisms).
- Problem: vector-DB "delete" usually tombstones a record and leaves the embedding bytes in index files, which raises compliance questions under GDPR Art. 17 (and HIPAA).
- Method: three HNSW implementations analysed; they attempt to reconstruct attributes from soft-deleted vectors via raw index files.
- Results (per abstract page): exact name recovery 25.5% and locations 46.4% (Wikipedia BLP); 100% age/gender markers (Synthea); 99% facial identity (image embeddings). Mitigation "Epoch Key Rotation" (crypto-shredding) cuts PII recovery to 0% at ~0.005 ms/record and issues ECDSA-signed deletion proofs.
- Relevance: direct evidence that an agent-memory "forget" operation can be legally non-compliant even when the API reports success. Crypto-shredding is also the standard route for reconciling immutable/WORM retention with erasure. The signed deletion proofs point to "evidence of erasure", which record-keeping regimes may themselves require to be retained.
- Critique: not yet peer reviewed. Whether residual bytes amount to non-erasure in law (vs. "beyond use") is unsettled; see the EDPB CEF 2025 report on backups and anonymisation workarounds.

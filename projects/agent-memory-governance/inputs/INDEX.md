# PI materials index

> **CONFIDENTIALITY.** Files 1 and 2 (RockAI) are the PI organisation's internal work and are **CONFIDENTIAL**. They name the operating entity and its platform. Their text, framework names (C1–C33, MVGM, the metric acronyms, "authority collapse" framing as applied here), entity facts and distinctive claims must **never** go into WebSearch/WebFetch, SciSpace queries, or any published artifact. Fetching public papers by DOI/arXiv id is fine. This index is itself confidential: it stays on this machine.
>
> Files 3–5 are AI-generated (SciSpace, Consensus). They are **context, not evidence**: trace any claim to the primary paper in `literature/papers.jsonl` before relying on it.

- **Ingested:** 2026-09-25 (`/ingest`). Five files, all read in full.
- **Library effect:** 106 identifiers resolved (every DOI/arXiv id in the five files, plus 4 uncited named papers and the NIST AI 100-2e2025 report). The result is 105 library records tagged `pi-input`: 65 new, 40 already in the library from the review. See §7.
- **Cross-reference keys:** G1–G12 = `literature/review.md` §8. Governance properties = `literature/evaluation.md` §3.

---

## 1. RockAI_Agent_Memory_Regulatory_Governance_Research_Memo_v5.docx

- **Type/class:** `pi-survey` (regulatory and technical research memorandum; 19 sections plus Appendices A–E; about 14.7k words).
- **Provenance:** RockAI research (the PI's organisation). The memo is "current through 21 September 2026", and its source-currency register was verified on 17 Sept 2026. It is v5 and records one design-review revision (C28–C33 added). No author is named. It carries a "not legal advice" disclaimer.
- **Sensitivity:** **CONFIDENTIAL.** It names the operating entity, its platform, and internal scope decisions (§6.4).
- **Summary:**
  - The memo maps GDPR, the EU AI Act (as amended by Omnibus 2026/1744), SEC Reg S-P, Advisers Act 204-2, the Treasury FS AI RMF, SR 26-2, DORA/FSB, NIST/ISO, US state ADMT law, DPA/UK guidance and APAC circulars onto the memory lifecycle.
  - It concludes that no regime names "agent memory", but that the combined rules imply a concrete architecture: an organisation-owned **governance gateway above replaceable backends** (Memoria, Graphiti, Mem0, Zep).
  - It specifies a 33-control catalogue, a metadata contract, a 9-state lifecycle, an interface × actor threat matrix, nine backend admission gates, and about 14 governance metrics paired with utility.
  - It closes with a roadmap (Phases 0–3), open research questions, and 12 draft principles.
- **Key claims** (cited = memo reference [R#]; uncited = no reference given):
  - Persistence changes the risk model through duration, derivation, reuse and propagation. So memory is "a regulated data-processing subsystem, not merely an LLM feature". *Uncited (argument).*
  - GDPR is the most direct legal anchor. Its principles map onto write, store, derive, retrieve, update, delete and export. *Cited R1–R3.* Derived representations (embeddings, KG edges) should be presumed personal data. *Cited R2 (EDPB Op. 28/2024); reinforced by R40 (EDPB Guidelines 02/2026 draft).*
  - AI Act dates under Omnibus 2026/1744 (in force 27 Jul 2026): Annex III high-risk from 2 Dec 2027, Annex I from 2 Aug 2028, Art. 50(2) legacy from 2 Dec 2026, sandboxes to 2 Aug 2027. Art. 5 and Arts 51–55 are unchanged. *Cited R4, R33.*
  - SR 26-2 (Apr 2026) expressly excludes GenAI and agentic AI and is "a governance analogue", not the rule. *Cited R8.*
  - Reg S-P amendments are binding for RIAs, with large-entity compliance since 3 Dec 2025. *Cited R5–R6.*
  - Advisers Act 204-2 retention conflicts with default TTLs. The answer is "not 'U.S. retain, EU erase'": retention is resolved at the record level, and a record can be retained but restricted. *Cited R13 for 204-2; the resolution itself is uncited.*
  - Graphiti CVE-2026-32247 (Cypher injection, CVSS 8.1, patched in 0.28.2) is "a concrete, real-world demonstration" of the cross-tenant-leak and deletion threats. *Cited R9–R10.* CVE-2026-90601 (REST auth bypass) was unpatched as of 17 Sept 2026. *Cited R26.*
  - Soft-deleted HNSW vectors are physically reconstructible. *Cited R25 (Ghost Vectors); supported per abstract.*
  - Authority collapse was found in 48 of 49 consolidator × backbone configurations. *Cited R27 (arXiv:2608.01679); supported per abstract.*
  - Memory Contagion: bias propagates "even when the consolidation mechanism itself performs perfectly", with "no observed safe threshold". *Cited R29 (arXiv:2606.23195).* **Overstated vs the abstract.** Contagion appears for length bias on older models only. Newer models (including Claude) were immune, and authority bias failed to propagate in all 15 experiments.
  - Memoria reports 87.1% accuracy and a −38.7% latency change (deck slide 17). *Cited R23.* **Not in the abstract; unverified.**
  - MemoryArena: near-perfect LoCoMo scores collapse to 40–60% on decision tasks. *Cited R50, but R50 is arXiv:2603.07670, a survey. MemoryArena itself is arXiv:2602.16313.* The abstract says only "perform poorly"; the numbers are unverified.
  - Metric provenance (§15.0): "Three metrics (lineage coverage, purpose violation rate and effective-policy coverage) have no direct precedent." *Uncited.* This is **disputed**; see §6(e).
  - CSLR should "adopt [the] MemLeak formalism". *Cited R46.* **Construct mismatch:** MemLeak (arXiv:2606.29788) measures post-deletion recovery from retained multimodal artifacts, not cross-tenant retrieval. Its abstract reports dual-annotator validation, not a "3-model LLM ensemble".
  - EC is aligned with FORGETEVAL-Adv, which "maps to real GDPR erasure incidents". *Cited R47.* The 13 configurations are supported per abstract. The GDPR-incident mapping is not in the abstract.
  - FRR borrows "Over-memory / Under-memory paired rates". *Cited R49 (arXiv:2608.19564).* The abstract reports an "erroneous persistence" rate; the over/under naming is not in the abstract.
  - Certified graph unlearning (GNNDelete; range-null-space arXiv:2508.02044) and Agentic Unlearning (arXiv:2602.17692) offer "formal, provable guarantees" and a path for C2. *Cited R28.*
  - MOSS makes retrieval symbolic and reproducible, so memory is "auditable by construction". *Cited R32; supported per abstract. Note that its evidence is a single-researcher deployment.*
  - MCP has no memory primitive. memorywire, Portable Agent Memory and a W3C Community Group (chartered July 2026, with a regulatory crosswalk) are emerging. *Cited R30.*
- **Frameworks, controls and metrics proposed** (details in §6(a–b)):
  - five governance planes;
  - controls C1–C33 with P0/P1/P2 priorities;
  - MVGM (minimum viable governed memory) per scope tier;
  - a minimum metadata contract with design-review fields (`effective_policy_hash`, `assertion_type`, `evidence_count`/`evidence_refs`, `last_retrieved_at`/`retrieval_count`, `notice_ref`);
  - a "trust tuple";
  - a derivation-risk ladder;
  - a 9-state lifecycle with transition rules;
  - an interface × actor threat matrix;
  - 9 admission gates with canaries and re-run triggers;
  - the metrics MLC, EC, CSLR, SMUR, UIR, PVR, Restriction Escape, Deletion Recovery Leakage, Promotion Regression, Backend Substitution Time, ACR, FRR, GLO, EPC, TTE and consolidation-review rejection rate, plus utility pairing.
- **The PI's own positions, hypotheses and ideas:**
  - Two inline margin notes (not memo prose) read as the PI's live questions:
    - §3: *"How to quantify necessary or say minimization? Risk tiering, low risk"*. How do you operationalise GDPR necessity and minimisation? Their tentative answer is risk tiering.
    - §15.0: *"Market scenario: internal knowledge of pretrained memory, or from the new conversation?"*. Should governance scope include parametric/pretrained knowledge, or only memory written from new interactions?
  - "Governance should be converted into backend conformance tests and measurable indicators". This is testable governance, not documentation.
  - "a store that remembers nothing would otherwise score perfectly on every governance ratio" → utility pairing; "Over-blocking is the failure mode nobody measures."
  - "Conflict resolution must not rely on recency alone… newer evidence may be lower-authority". Principle 20: "Do not let recency substitute for authority."
  - "TopK(similarity | authorized) is the right formula, but post-filtering a top-k result set silently destroys recall."
  - Consolidation is "a write path with no user in the loop". It should run in diff-and-approve mode.
  - "Hard barriers require physical partitioning". Filters suffice only for soft scopes.
  - Whether MOSS-style auditable-by-construction retrieval outperforms logging over probabilistic retrieval is "an open, testable question".
  - Adapting certified graph unlearning to Graphiti's bi-temporal edges and "formally characterizing exactly what guarantee it provides" is a Phase 3 research task.
  - The MVGM pilot on one real internal workflow by end of Q4 2026 would give production traces for drift, calibration and contagion research.
  - "a policy-aware memory layer can become a research differentiator". Memory should optimise "authority, uncertainty, permissible use, retention, information barriers, contamination risk and reversibility", not just relevance.
  - Contributing to the W3C memory-interop CG, because "a production deployment with real governance requirements is a scarce input".
- **Internal inconsistencies noticed:**
  - The executive-summary numbering repeats "9."
  - The §17 open questions are numbered 8–15, plus one unnumbered bullet. The §18 principles are numbered 16–27. These look like list-continuation artifacts from the .docx.
  - The deck and memo disagree on some details; see file 2.

## 2. RockAI_Agent_Memory_Governance_Framework_v7_with_speaker_notes.pptx

- **Type/class:** `slides` (37 slides with full speaker notes, about 11.7k words). A 45-minute internal talk.
- **Provenance:** RockAI research, "Updated 17 September 2026", v7. The speaker is presumably the PI. The notes are in the first person ("I'd put the first one to leadership this month").
- **Sensitivity:** **CONFIDENTIAL.** It names the entity, its RIA status, its platform and its internal roadmap.
- **Summary:**
  - This is the presentation version of the memo, with the same architecture, controls, contract, lifecycle, threat matrix, gates, metrics and roadmap.
  - The notes add the PI's emphasis and rhetoric, and some facts not in the memo:
    - "We are a registered investment adviser, not a bank holding company";
    - Treasury FS AI RMF: 230 control objectives, 4 adoption stages, 100+ institutions;
    - Reg S-P: 30-day breach notification, and an "enforcement precedent Nov 2025 (M Holdings)";
    - AI Act Art. 26(6) logs kept ≥6 months;
    - NIST AI 100-2e2025 "now names agent memory poisoning";
    - Graphiti "defaults to OpenAI for extraction";
    - a roadmap: Q3 foundation, Q4 build and prove, Q1 2027 harden.
  - It ends with six open decisions and names the next artifact: "Governance Specification v0.1".
- **Key claims (additional to the memo):**
  - "No regulation anywhere names 'agent memory'… That is not the same as saying it's unregulated." *Uncited (argument).*
  - Binding for this entity: GDPR, the AI Act, Reg S-P and DORA. SR 26-2 is "grey… analogue only". *Cited on the slides to official sources.*
  - "The EU AI Act's high-risk obligations no longer land in August 2026… If you've seen the old date in any internal material, it's superseded." *Cited (Omnibus).*
  - NIST AI 100-2e2025 names agent memory poisoning, indirect prompt injection and tool/supply-chain attacks. *Cited.* The NIST report was added to the library as doi:10.6028/nist.ai.100-2e2025 (Crossref title truncated). The content claim is **not verified here**.
  - Reg S-P "enforcement precedent Nov 2025 (M Holdings)". *Uncited detail;* not in `regulation.md`. **Verify.**
  - The threat matrix draws on the "SSGM three-interface framing". *Uncited on the slide; resolved to arXiv:2603.11768 (SSGM), which is already in the library.*
  - Deck inconsistencies:
    - slide 20 is titled "C1–C27" although the catalogue runs to C33;
    - slide 35 says "Backend admission tests (7 gates)" but slide 32 lists nine;
    - slide 30 points to memo "Section 11" for the contract, which is §10.
- **Frameworks and controls:** as in the memo. The visual additions are the risk-escalation ladder (session → memory → graph → platform risk) and six "governance intercept points" (WRITE, DERIVE, RETRIEVE, USE, RESTRICT, ERASE).
- **The PI's own positions (quotations from the speaker notes):**
  - The core thesis: "persistent memory turns transient AI output into a governed data-processing subsystem". A stored answer "retrieved into a decision three weeks later by a different agent… [is] a record".
  - "A memory that's easy to write and hard to govern isn't an asset, it's a liability with a retrieval API." Most libraries "treat the last three [stages] as afterthoughts. That's precisely backwards from a regulator's point of view."
  - "'agents must not call backends directly' is a policy; 'agents cannot call backends directly' is an architecture… under deadline pressure, any governance layer that can be routed around will be."
  - On Memoria (the in-house system): "We should assume Memoria does this [authority collapse] until we've tested that it doesn't." Keep "Memoria as a genuine fallback rather than a stepping stone to full vendor dependence".
  - "no longer true is not legally erasable; restricted is not deleted; retained for legal hold is not usable by agents."
  - "A list finds the threats you already thought of. A matrix finds the cells you left empty."
  - "a store that remembers nothing scores perfectly on all six originals… Otherwise the framework optimises toward an empty store, and nobody notices because the dashboard is green."
  - On metric provenance: "the names and ratios are ours, but most of the constructs are borrowed… Lineage coverage, purpose violation rate and effective-policy coverage… are our contribution."
  - "research owning evaluation without production data is a well-known way for the research-engineering split to fail". The PI would argue "hardest" for the MVGM pilot.
  - The division of labour: "engineering owns backend implementation; research owns evaluation, control policies, conformance metrics, and governance-aware memory intelligence." This is the PI's stated research remit.
  - Scope: the single most important decision is whether memory stays internal or feeds the platform. It "sets the external oversight tier". "I'd put the first one to leadership this month."
  - Standards engagement: "If we want to shape how oversight of memory-driven decisions gets operationalised, that window is this week" (prEN 18229-3, closed 22 Sept).

## 3. SciSpace_agent_memory_evaluation_template.xlsx

- **Type/class:** `data` (evaluation template: a README sheet, a Metric Catalog M01–M26, a Source Register S1–S9, and an empty Evaluation Log).
- **Provenance:** AI-generated with SciSpace. Undated; its sources run to 2026-07-13, which suggests about Sept 2026. It appears to accompany file 4.
- **Sensitivity:** not confidential (AI-generated from public papers).
- **Summary:**
  - A metric catalogue for agent memory. Each metric has a formula or operationalisation, an "evidence status" caveat, memory type, unit, direction and source.
  - The catalogue is honest that many formulas are "recommended operationalization" rather than taken from the source.
  - The minimum-reporting rule requires N, CIs or bootstrap intervals, the baseline, k, the judge model and rubric, the latency percentile and the memory-store version. This matches `evaluation.md` §4 pitfalls and the PI's "pinned configuration" rule.
  - Coverage is overwhelmingly utility-side: 24 of 26 metrics. Governance is thin: only M25 (leakage) and M26 (deletion compliance).
- **Key claims:**
  - Every formula is marked as either literature-backed or "recommended operationalization". *Cited S1–S9.*
  - **Source attribution for M25 and M26 is weak.** They cite S2 (Mem0) and S3 (Zep). Per the abstracts, those papers evaluate LoCoMo/DMR/LongMemEval accuracy, latency and tokens, not leakage or deletion.
- **Metric families:** task success and accuracy (M01–M04); retrieval quality (M05–M08); memory completeness and integrity (M09–M10); factuality and contradiction (M11–M12); efficiency (M13–M15: latency, tokens, storage); continual learning (M16–M20); procedural memory (M21–M22); temporal consistency (M23); personalisation (M24); safety and privacy (M25–M26).
- **Mapping to the governance properties in `evaluation.md` §3 / review:**

  | Governance property | Template metrics | Comment |
  |---|---|---|
  | Retain-when-required | M09 completeness; M16 forgetting; M19 average accuracy | Here "forgetting" is a *loss*. This is the opposite sign to M26: the G1 tension in miniature. Nothing scores *mandated* retention surviving consolidation. |
  | Forget-when-required | M26 deletion compliance | It includes paraphrase and derived-memory checks and re-verification after re-index, cache and backup. That is good, but a single ratio has no physical-layer check. The PI's EC and TTE go further. |
  | Isolation | M25 leakage rate | Generic. No barrier, cross-client or composition construct. The PI's CSLR, PVR and C30 cover more. |
  | Integrity (poisoning) | none (M10 is structural integrity, not adversarial) | Gap. |
  | Provenance / auditability | none (M10 orphan-node rate is a weak proxy) | Gap. The PI's MLC and EPC fill it. |
  | Freshness | M12 contradiction; M23 temporal consistency | No authority-aware staleness. The PI's SMUR and ACR go further. |
  | Utility and cost | M01–M08, M13–M15, M17, M21–M22, M24 | Strong. The template can supply the "utility pairing" half of the PI's metric set. |

- **The PI's use of it:** none stated. It was probably collected as the utility-side complement to the memo's governance metrics. It is **not cited** in the memo or deck.

## 4. SciSpace_agent_memory_eval_metrics.pdf

- **Type/class:** `ai-generated-review` (SciSpace "systematic literature review" print-out; **43 pages**, not 8).
- **Provenance:** SciSpace, printed 2026-09-24 16:36. The query was "evaluation metrics for agent memory across the full spectrum of applications, including AI in finance". The funnel reports 188 candidates, 182 relevant and 50 "highly relevant".
- **Sensitivity:** not confidential.
- **Summary:**
  - Five metric themes, each with a paper count: goal completion (48/50), retrieval precision (45/50), conflict resolution (40/50), memory efficiency (35/50), temporal consistency (30/50) and governance/privacy (14/50).
  - Conclusions: evaluation is fragmented; finance compliance is overlooked; there is no standard "minimal evaluation card".
  - It proposes a drift-tracking benchmark, a "Compliance-Aware Memory Benchmark", privacy-preserving memory audits, and Pareto-optimal benchmarking.
- **Quality warning:** the per-study results table (pp. 9–20) gives **identical boilerplate text for every one of about 40 studies**. It is templated, not extracted, so the "48/50 papers" style counts are not credible. It cites GraphMem twice with two DOIs (zenodo .18131571/.18131572). It includes a 2016 RL paper (Memory Lens). There are no regulation sources.
- **Key claims** (all cited to the review's own refs; spot-checks in §8):
  - Up to 88.8% goal completion for memory-augmented agents (Alshikh 2025; Yu 2025).
  - Graph-based memory beats vector RAG on retrieval precision (ibrahim 2026; Rasmussen 2025).
  - "explicit newer-over-older fact handling is a necessary mechanism" (ibrahim; Bousetouane). This **contradicts the PI's "do not let recency substitute for authority"**.
  - Financial research agents need logic-tree evaluation (Sun 2025; Huang 2025).
  - Evaluation "often overlook[s] the specific regulatory and compliance constraints inherent in financial domains" (Sinha 2025; Mohammadi 2025). This is consistent with G3.
- **Metrics proposed:** goal completion rate, retrieval precision, conflict resolution rate, memory efficiency, temporal consistency score, and a "minimal evaluation card".
- **The PI's use of it:** none stated. It was generated the day after the project brief, apparently as breadth for the evaluation facet. It adds **nothing on governance metrics** beyond what `evaluation.md` has.

## 5. Concensus_agent_memory_eval_metrics.pdf

- **Type/class:** `ai-generated-review` (Consensus Deep Search report; 10 pages). The filename misspells "Consensus".
- **Provenance:** Consensus.app. Undated; the latest reference is dated 2026-08-29, so it was generated in or after late Aug 2026. It reports "73.3K retrieved → 79 included" from one search.
- **Sensitivity:** not confidential.
- **Summary:**
  - Agent-memory evaluation needs a metric stack. The IR formulas (Accuracy, P/R/F1, Recall@K, MRR, MAP, nDCG) are standardised.
  - Newer metrics are benchmark-local and cover forgetting and conflict (FAMA; MemConflict CRS/UOCS/SEH@K/SRS), use and retention (MemGUI IRR/MTPR/FRR; StreamMemBench stages; MemGround MFU/MFCO), longitudinal behaviour (SeqMem-Eval), efficiency (footprint, latency, write-path cost) and governance (Chen 2026: PR, AER, Privacy-Utility AUC, FRS; Memory Worth).
  - The main open problem is standardising evidence-use and forgetting metrics.
- **Quality warning:**
  - The "consensus meter" failed ("Requires at least 5 papers").
  - The coverage-gap matrix (Fig. 7) marks every cell "GAP", so it is uninformative.
  - One title mismatch: it cites arXiv:2606.24595 as "MEMPROBE: Probing Long-Term Agent Memory…", but the arXiv title is "MemAudit: Auditing Long-Term Agent Memory via Hidden User-State Recovery" (the benchmark inside is called MEMPROBE).
  - Otherwise the references are real and resolve.
- **Key claims** (cited; spot-checks in §8):
  - FAMA penalises obsolete or invalidated memory (Uddin 2026).
  - MemConflict separates answer quality from retrieval and ranking of valid memory (Tao 2026).
  - FRS measures post-deletion residue in derived tiers (Chen 2026).
  - Memory Worth converges to p⁺(m) (Şimşek 2026).
  - Write-path cost can flip conclusions (MemDelta, Wang 2026).
- **Relevant to the PI's metric set:**
  - Chen 2026 (arXiv:2606.10062) FRS is a closer published precedent for the PI's **EC** than MemLeak. It shows raw-only deletion leaves derived summaries recoverable in about 20% of cases.
  - Memory Worth (arXiv:2604.12007) is a per-memory utility signal relevant to the PI's minimisation question and to `retrieval_count`.
  - FAMA (arXiv:2604.20006) and MemConflict (arXiv:2605.20926) are precedents for **SMUR**.
  - Several of these papers were not in the review library before this ingest.

---

## 6. What the PI already has

### (a) Governance framework in brief
- **Architecture.** Agent → **Memory Governance Gateway** (policy, risk and audit engines) → Common Memory API (write, derive, retrieve, restrict, erase, export) → replaceable engines (Memoria, the in-house reference; Graphiti; Mem0/Zep) → pinned storage and model providers.
  - The gateway is the only holder of backend credentials, with mTLS and network policy ("impossible, not prohibited").
  - Authorisation is an index-level pre-filter, and there is a stated p95 overhead budget.
  - Background and consolidation jobs are identified actors, running in diff-and-approve mode.
  - Hard barriers get physical partitions.
- **Five planes:**

  | Plane | Question | Controls |
  |---|---|---|
  | Data governance | What may be remembered? | C11, C12, C13, C16, C19 |
  | Memory integrity | What does it mean? | C1, C6, C15, C20, C22 |
  | Access and use | Who may use it? | C17, C21, C23, C30, C32 |
  | Lifecycle | How does it change or disappear? | C2, C7, C14, C24, C25, C28, C29 |
  | Ops and third party | Can we trust the stack? | C3, C5, C10, C18, C26, C27, C31, C33 |

- **Controls C1–C33** (P0 = before production).
  - **15 P0 controls:** C1 lineage, C2 erasure propagation, C3 audit trail, C5 OSS governance, C10 security, C11 provider pinning, C13 purpose binding, C16 inferred-memory classification, C17 isolation, C19 barriers/MNPI, C20 source authority, C21 purpose-bound use, C23 operation authorisation, C24 lifecycle states, C26 version lineage.
  - **Also P0 or conditionally P0:** C28 consolidation jobs, C30 composition leakage (where barriers apply), C31 notices (where ADMT applies), C32 agent identity.
  - **MVGM for an internal pilot:** C1, C3, C5, C11, C13, C17, C24, C28. Investment workflows add C19, C20, C21, C23, C30 and C32. Client-facing deployments add all P0 controls plus C31.
- **Metadata contract.** Identity, content (derivation_type, assertion_type), provenance (source authority, parents, evidence_count), trust, governance (purpose, legal basis, sensitivity, barrier, `notice_ref`, `effective_policy_hash`), temporal fields (valid_from/to, review_at, last_retrieved_at), lifecycle state, technology lineage and operations.
  - A **trust tuple** combines derivation, authority, assertion_type, confidence and verification.
  - A **derivation ladder** runs observed → stated → extracted → inferred → predicted → derived-from-derived.
- **Lifecycle.** Nine states: ACTIVE, PENDING_VERIFICATION, DISPUTED, QUARANTINED, RESTRICTED, SUPERSEDED, EXPIRED, HELD, DELETED.
  - Restrictive states propagate to children immediately.
  - Hold release, reactivation and promotion need dual control.
  - A DISPUTED item becomes RESTRICTED at its deadline.
  - DELETED is terminal.
  - Each operation (WRITE, READ, UPDATE, RESTRICT, CORRECT, DELETE, EXPORT, PROMOTE) has a defined governance sequence.
- **Threat model.** A matrix of interfaces (ingestion, consolidation, retrieval) × actors (external content, agent/sub-agent, background job, insider, backend/provider). It adds:
  - extractor-prompt injection;
  - safety-memory dilution;
  - confused deputy;
  - membership inference and embedding inversion;
  - poisoning by volume;
  - re-embedding drift;
  - audit-log tampering and shadow copies;
  - bias contagion.
- **Assurance.** Nine admission gates: supply chain, data flow, security, privacy/rights, memory quality, operations, evidence, performance and human oversight.
  - A pass requires a fixture, an oracle, a threshold and pinned versions.
  - Canary memories are planted per tenant, barrier and state.
  - Erasure is verified at the physical layer.
  - Named adversarial protocols: AuthMem-style, contagion and dilution.
  - Re-run triggers are defined.

### (b) Evaluation metric set
- **Governance ratios:**
  - MLC: lineage coverage, target → 100%.
  - EC: erasure completeness, verified at the raw index.
  - CSLR: cross-scope leakage, measured by canary hits, target 0.
  - SMUR: stale-memory use. Attribution means "in context and referenced in output".
  - UIR: unsupported inference, below the evidence threshold.
  - PVR: purpose violations, target 0.
  - Restriction Escape Rate and Deletion Recovery Leakage (after restore), both target 0.
  - Promotion Regression Rate.
  - Backend Substitution Time.
  - ACR: authority collapse, where assertion type or authority escalates without new evidence.
  - EPC: effective-policy coverage, target 100%.
  - TTE: time-to-erasure.
  - Consolidation-review rejection rate.
- **Utility and cost counterweights.**
  - FRR: false restriction, i.e. authorised, relevant memories that were blocked.
  - GLO: p95 governance latency.
  - Every ratio is paired with governed vs ungoverned recall@k and with task success with memory on vs off.
- **PI's stated provenance.**
  - Constructs borrowed from MemLeak and Carlini canaries (CSLR), FORGETEVAL and Ghost Vectors (EC), AuthMem-Bench (ACR), and memory-commitment over/under rates (FRR).
  - Claimed as new: MLC, PVR and EPC.
- **Complement.** The SciSpace template (file 3) supplies the standard utility-side formulas: retrieval P/R/MRR/nDCG, accuracy, latency, tokens and storage.

### (c) The PI's regulatory reading vs `literature/regulation.md`

**Where they agree.** The memo is current through 2026-09-21 and matches our reading on the load-bearing 2026 changes.
- It never references SR 11-7. It treats **SR 26-2 (17 Apr 2026)** as the model-risk guidance, with the GenAI and agentic carve-out and the >$30bn focus.
- It uses the **Omnibus 2026/1744** dates: OJ publication 24 Jul, in force 27 Jul, Annex III 2027-12-02, Annex I 2028-08-02, Art. 50(2) 2026-12-02.
- It matches us on the Reg S-P compliance dates, the CPPA ADMT dates and the data-level (not entity-level) GLBA carve-out, the Colorado SB 26-189 re-enactment, EDPB Op. 28/2024 and Guidelines 02/2026, and the HKMA GenAI circular.
- **No statement predating SR 26-2 or the Omnibus was found.** The deck explicitly warns that the old August 2026 high-risk date is superseded.

**Outdated or time-expired statements to flag:**
1. **prEN 18229-3 comment window "open until 22 Sept 2026".** The deck says "that window is this week". It is **closed** as of 2026-09-25.
2. **"FCA AI engagement… external publication pending"** (memo §6.5 and App. E, "verified 17 Sept 2026"). `regulation.md` records the **FCA Mills Review published 2026-07-06** [V press release]. If that is the output the memo is waiting for, the register entry is stale. Verify.
3. **Graphiti CVE-2026-90601 "unpatched, fix PR #1739 unmerged"** (status as of 17 Sept). This needs re-checking before any reliance. It was **not** looked up here, to keep confidential context off the web; a plain public CVE lookup is fine if the PI wants one.
4. **MAS.** The memo cites only the MindForge handbook, dated "Mar 2026". We have the handbook as 2026-01 and the toolkit as 2026-03-20. The memo omits the **MAS AIRG** guidelines (consultation closed 2026-01-31; MAS said on 2026-08-05 they "will be finalised soon") and the SAFR agentic framework.
5. **UK automated decisions.** The memo reasons from GDPR Art. 22 and cites the Dutch AP. For UK operations, **UK GDPR Art. 22 was replaced by Arts 22A–22D from 2026-02-05 (DUAA 2025)**. The memo does not reflect this.
6. **Advisers Act 204-2 is treated as stable.** The **SEC recordkeeping modernisation (17a-4 and 204-2)** is at proposed-rule stage on the Spring 2026 agenda, flagged deregulatory. It could narrow what memory must be retained.

**Substantive differences (not dating errors):**
- **Retention vs erasure (G1).** The memo resolves this "at the record level" with RESTRICTED/HELD states. It does not address that **GDPR Art. 17(3)(b) exempts only retention required by Union or Member State law**. A US 204-2 retention duty over EU data subjects' memory is exactly the unreconciled cross-border case in `regulation.md` §2 and review G1. The memo also does not cite **AMLR Art. 77 retain-then-delete** or the **17a-4(f)(2) audit-trail alternative**, both of which are partial reconciliations in our review.
- **Entity perimeter.**
  - The memo is RIA-centred: Reg S-P, 204-2, Treasury FS AI RMF, DORA and the entity's platform.
  - Our review is broker-dealer and bank-centred: 17a-4, FINRA 4511/3110/5280, §15(g), MiFID 16(7), MAR Art. 9/18, FINRA 2026 oversight report, PRA SS1/23.
  - Neither covers the other. In particular, **neither document cites the Advisers Act §204A MNPI-policies duty**, which is the RIA analogue of §15(g) and the natural legal hook for C19 [M, background knowledge; verify].
- **AI Act log retention.** Deck slide 10 says deployers keep logs "≥ 6 months (Art. 26(6))". For financial institutions, **Arts 19(2) and 26(6) fold logs into financial-services documentation**, which in practice means years (`regulation.md` §1b). The deck is incomplete here.
- **Colorado SB 26-189.** The memo omits the **exemption for prudentially regulated FIs** and the 3-year record duty.
- **Items the memo has that `regulation.md` lacks.** These are review omissions to back-fill:
  - **Treasury FS AI RMF (19 Feb 2026)**;
  - DORA **CTPP designation (18 Nov 2025)** and concentration/substitutability as memory risks;
  - **prEN 18229-1/-3 and prEN 18282** (harmonised standards for Art. 12 logging and cybersecurity);
  - **AEPD agentic-AI guidance (18 Feb 2026)**;
  - **ICO–FCA vulnerability-data statement (27 Mar 2026)**;
  - EDPB–EDPS Joint Opinion 1/2026;
  - **HK SFC GenAI circular (high-risk designation for AI investment advice/research) and SFC AI-cyber circular (2 Jun 2026)**;
  - **IMDA agentic framework (Jan 2026)**;
  - Reg S-P as the hook for OSS memory-library oversight;
  - CVE-level supply-chain evidence.

  None of these has been verified by us yet; all need `[V]` checks. Use only public identifiers when searching, never memo text.
- **Items `regulation.md` has that the memo lacks.** EDPB CEF 2025 erasure report (backups, anonymisation as a workaround), FINRA 2026 GenAI/agents section ("may unintentionally store"), FSB 2026 consultation naming memory poisoning, CJEU *EDPS v SRB*, ESMA AI statement ¶23–24, and the withdrawal of the CFPB circulars.
- **Unverified PI facts to check before any external use:**
  - "M Holdings" Reg S-P enforcement (Nov 2025);
  - Treasury FS AI RMF "230 control objectives / four stages";
  - DORA CTPP list "nineteen providers";
  - AI Act sandbox deferral to 2 Aug 2027;
  - NIST AI 100-2e2025 naming agent memory poisoning.

### (d) The PI's stated open questions and ideas (seeds for `/ideate`)

**Open questions** (memo §17, verbatim headings):
- no standard memory object;
- no accepted memory-erasure benchmark;
- no lineage standard for consolidation and promotion;
- no settled governance model for inferred memory;
- no clear boundary between memory and a regulated record;
- no standard for purpose-aware retrieval;
- no standard governance-metric set, and "no published metric pairs governance ratios with utility to prevent the empty-store degenerate optimum";
- no mature policy for memory-to-skill promotion;
- platform criticality can change over time.

**Margin questions:**
- how to quantify "necessary" (minimisation), with risk tiering as the tentative answer;
- whether governance covers pretrained or parametric knowledge or only conversation-derived memory.

**Explicit research ideas:**
1. **Governed write policy.** Learn what to remember subject to purpose, sensitivity, authority, expected utility and cost. This links to the minimisation question and to Memory Worth, arXiv:2604.12007.
2. **Trust-aware reconciliation.** Resolve conflicts by authority, validity, confidence and verification rather than recency (C20, ACR).
3. **Certified graph unlearning on a bi-temporal KG** (Graphiti), with a formal statement of the guarantee (C2).
4. **Compliance-aware promotion** from episode to fact to skill (C29).
5. **Drift observability**, including upstream bias-contagion sampling (C6, C33).
6. **Automated policy enforcement** "without delegating legal interpretation to the model" (G12).
7. **Auditable-by-construction** (MOSS-style symbolic retrieval) vs logging over probabilistic retrieval, stated as "an open, testable question".
8. **Canary-based conformance** as the measurement method for leakage, restriction escape and deletion recovery.
9. **Utility-paired governance metrics** (FRR, GLO) against the empty-store optimum.
10. **MVGM pilot traces** as the data source for research. This is a possible route around G3 and G11's synthetic-data problem, subject to data-approval constraints in `brief.md`.

**Open decisions for leadership** (deck slide 36):
- scope: internal-only vs feeding the platform;
- bank-supervised entity status;
- approved providers per data class;
- record-level retention;
- barrier map;
- gate sign-off and the p95 budget.

### (e) Agreement and disagreement with review gaps G1–G12

| Gap | PI coverage | Effect on our novelty |
|---|---|---|
| G1 retention vs erasure | **Design-level:** C7, RESTRICTED/HELD states, "not US retain, EU erase". Misses the 17(3)(b) Union-law limit. No metric scores both obligations. | A lifecycle state machine is *not* novel for us. An **evaluation that scores correct joint handling of retention and erasure** remains open. |
| G2 barriers and isolation | **Design:** C17, C19, physical partitions, **C30 composition leakage**, canary CSLR. No evaluation and no legal-rule encoding. | The architecture idea is taken. A **barrier-rule benchmark or measurement** remains open, and so does the PI's composition-leakage framing (see new gaps). |
| G3 no finance memory eval | **Not addressed.** The test suite is generic, with no finance fixtures. The MVGM pilot could supply real traces. | Still open. The PI's gates and metrics could define the benchmark's scoring. |
| G4 deletion ≠ forgetting | **Strong:** C2, C25, physical-layer check, deletion receipt, EC/TTE/Deletion Recovery Leakage, and the certified-graph-unlearning idea. | Metric and protocol design overlaps heavily. Novelty remains in a **cross-layer verified-erasure study with guarantees**. The field is fast-moving; FRS (arXiv:2606.10062) is a close precedent the PI did not cite. |
| G5 utility cost of governance | **Strong conceptually:** utility pairing, FRR, GLO, p95 budget, performance gate. | The claim that governance ratios must be utility-paired is not novel (GateMem already does it; see `evaluation.md`). The **empirical stateless vs governed vs ungoverned cost study** is still open, and it tests the PI's core bet. |
| G6 auditability / lineage | **Strong design:** C1, C3, C26, MLC, EPC, `effective_policy_hash`, audit-log tampering in the threat matrix, "no shadow store". | MLC is *defined* but not validated. A validated lineage metric remains open, but we would be building on the PI's definition. |
| G7 record classification | **Named as open question 12;** no answer. | Same gap; mostly legal. |
| G8 authorisation continuity through consolidation | **Ahead of the review:** C28 diff-and-approve, restrictive inheritance, `assertion_type`, ACR, and **AuthMem-Bench (arXiv:2608.01679), which the review missed**. It shows collapse in 48/49 configurations and that persisted authority labels cut unauthorised actions from 16.9% to 0.0% (per abstract). | **Novelty sharply reduced.** The closest-work list for G8 must add arXiv:2608.01679. What remains: finance authority hierarchies (system-of-record vs client remark) and barrier-scope continuity. |
| G9 purpose limitation per item | **Design:** C13, C21, purpose fields, PVR, the "significant decision" flag. | PVR is claimed "no precedent", but CI-style violation metrics (CIMemories Violation@n, CI-Work, GateMem A) are close. Mechanism and evaluation are still open. |
| G10 suitability and staleness vs authoritative sources | **Partial:** C20 source hierarchy, SMUR, "recency ≠ authority". Preference drift vs manipulation is only in C9. | Staleness against systems of record is partly specified by the PI. The manipulation angle is still open. |
| G11 evidence quality | **Methodologically aligned:** pinned versions, fixture/oracle/threshold, judge-sensitivity noted, canaries. | Agreement; no novelty impact. |
| G12 regulation-as-code | **Partial:** policy engine, `effective_policy_hash`, and Phase 3 "automated policy enforcement". | Open; the PI frames it as a research frontier. |

**Where the PI's materials disagree with the review:**
- **Stateless vs persistent.** Review §1.7 finds that regulated industry deliberately chooses stateless agents. The PI's whole programme bets that governed persistent memory is deployable now. G5 is the experiment that adjudicates this.
- **Metric precedents.**
  - The PI says PVR has no precedent; `evaluation.md` lists CI violation metrics.
  - The PI anchors CSLR on MemLeak (a construct mismatch). Isolation precedents in `evaluation.md` are GateMem A, AgentLeak CLR and MemClaw search_leak_rate (arXiv:2606.24535).
  - The PI's EC misses FRS (arXiv:2606.10062) and GateMem F.
- **Memory Contagion is over-generalised** in the memo relative to its abstract (see file 1).
- **Retention vs erasure.** The PI thinks it can be resolved at the record level. The review finds the cross-border case unreconciled.
- **SciSpace vs PI on conflict resolution.** SciSpace (file 4) calls newer-over-older "necessary"; the PI rejects recency as authority. The review's freshness row and AuthMem-Bench side with the PI.

**New gap candidates the review missed.** These are candidates only. Each needs the novelty protocol, and confidence is low until searched. Searches must use generic public phrasing, never memo text.
1. **Composition (context-assembly) leakage.** Individually authorised memories jointly reveal a barrier-crossing inference; this is the classic database aggregation/inference problem applied to prompt assembly. The review treats isolation per item. [low–med]
2. **Authorisation pre-filter vs post-filter recall loss, and governance latency (GLO).** Governed top-k under authorisation predicates in vector and graph stores. The Graphiti `group_id` is only a coarse partition. [low]
3. **Backbone or embedder change breaks restriction scopes** ("re-embedding drift"): restrictions and filters computed under old embeddings no longer bind the same records. [low; possibly novel]
4. **Memory → skill promotion governance.** Procedural memory is executable, so it needs a promotion gate, regression testing and reversal. The review has this only as a single-facet mention of RL memory managers. [low–med]
5. **Supply chain and third-party risk of memory backends.** Covers OSS CVEs, provider egress defaults, concentration and substitutability (Backend Substitution Time), and portability standards (memorywire, Portable Agent Memory, W3C CG). The review has industry products but no supply-chain facet. [med that it is under-covered in our review]
6. **Non-human identity and confused deputy in multi-agent memory writes** (C32). Partly adjacent to the review's multi-principal work. [low]
7. **Quantifying minimisation or "necessity" for memory writes** (the PI's margin question), for example via per-memory value signals such as Memory Worth. [low]
8. **Subject-facing transparency per memory record.** ADMT access-to-logic, UK Arts 22A–D and Art. 15(1)(h) explanations when consolidated memory drove a decision. [low]
9. **Epistemic status (assertion type) as a first-class memory attribute** in finance: a tentative client remark vs an instruction. AuthMem-Bench covers the general case; the finance instruction/suitability version is untested. [low–med]

---

## 7. Citations resolved (`--source pi-input`, `--tag pi-input`)

| Source | Ids resolved | New to library | Already in library |
|---|---|---|---|
| Memo (R23, R25, R27–R30, R32, R46–R50) | 15/15 arXiv | 6 (AuthMem-Bench 2608.01679, graph unlearning 2508.02044, Memory Contagion 2606.23195, Secret Sharer 1802.08232, canary audits 2605.18891, Remember/Verify/Ask 2608.19564) | 9 |
| Deck | all arXiv ids are a subset of the memo's | — | — |
| Template S1–S9 | 9/9 | 5 | 4 |
| SciSpace review | 47/47 (DOIs, arXiv and Zenodo) | 32 | 15 |
| Consensus review | 35/35 | 19 | 16 |
| Uncited named papers, via `lit.py arxiv` exact-title search | 4: GNNDelete 2302.13406, Memory Lens 1611.06928, MemoryArena 2602.16313, SSGM 2603.11768 | 3 | 1 (SSGM) |
| NIST AI 100-2e2025 (doi:10.6028/nist.ai.100-2e2025) | 1 | 1 | 0 |
| **Total** | **106 identifiers → 105 records** | **65** | **40** |

Note that some identifiers appear in more than one source, so the source rows sum to more than the totals.

- **Not resolvable as papers** (regulatory, official or web sources, recorded only here):
  - memo R1–R22, R24, R26, R31 (Mem0 blog), R33–R45, R51 (Future AGI blog);
  - the Databricks April 2026 report;
  - the W3C CG charter.
- **Title and version quirks:**
  - arXiv:2606.24595 is cited by Consensus as "MEMPROBE" but titled "MemAudit" on arXiv.
  - The SciSpace "Du et al. 2025" (arXiv:2505.00675) now carries the title "Rethinking Memory in LLM based Agents…".
  - The DREAM Zenodo DOI resolves to "DREAM v3".
  - The Mohammadi ACM DOI resolves to arXiv:2507.21504.

## 8. Spot-checks of the AI-generated reviews (against abstracts in `papers.jsonl`)

**SciSpace (file 4):**
1. **"memory-augmented agents… up to 88.8% goal completion" (Alshikh 2025, arXiv:2511.08242): partially supported and misattributed.** 88.8% is the *average GCR of a "Hybrid" agent in a simulated* white-paper experiment on generic agent architectures. It is not a memory result.
2. **"graph-based memory architectures significantly improve retrieval precision compared to standard vector-based RAG" (Rasmussen 2025, Zep, arXiv:2501.13956): not supported as stated.** Zep reports DMR 94.8% vs MemGPT 93.4% (1.4 pp) and up to 18.5% accuracy gains on LongMemEval vs "baseline implementations". There is no retrieval-precision comparison with vector RAG. The other citation is a duplicate-DOI Zenodo preprint.
3. **"financial research agents require specific logic-tree based evaluation" (Sun 2025; Huang 2025): half supported.** FinResearchBench (arXiv:2507.16248) is a logic-tree Agent-as-a-Judge, so it supports the claim. Wealth-Voyager (doi:10.1145/3766918.3766944) is a multi-agent wealth framework with a live case study and no logic-tree evaluation, so it does not.

**Verdict for SciSpace:** 0 of 3 claims fully supported. The per-study table is templated boilerplate. Treat as low reliability.

**Consensus (file 5):**
1. **FAMA "penalizes use of obsolete or invalidated memory" (Uddin 2026, arXiv:2604.20006): supported** (abstract: "penalizes reliance on obsolete or invalidated memory"; "frequent reuse of invalid memories").
2. **MemConflict separates final-answer quality from retrieval and ranking of valid memory, with CRS/UOCS/SEH@K/SRS (Tao 2026, arXiv:2605.20926): supported in substance** ("answer correctness often diverging from memory retrieval and ranking"). The four metric names are not in the abstract, so they are unverified at abstract level.
3. **PR, AER, Privacy-Utility AUC and FRS for post-deletion residue (Chen 2026, arXiv:2606.10062): supported** (PR, AER and FRS are named; a "privacy-utility frontier"; raw-only deletion leaves summaries recoverable in about 20% of cases). "AUC" is not named in the abstract.
- **Extra check:** the Memory Worth formula p⁺(m) = Pr[y=+1 | m ∈ M_t] (arXiv:2604.12007) is supported. The abstract adds a caveat that the review omits: the quantity is associational, not causal.

**Verdict for Consensus:** 3 of 3 supported in substance, with minor metric-name details unverifiable from abstracts. Moderate reliability. The coverage-gap figure and the consensus meter are uninformative.

**PI memo claims checked while resolving** (per abstract): AuthMem-Bench 48/49 ✔; Ghost Vectors ✔; MOSS ✔; FORGETEVAL 13 configurations ✔ (GDPR mapping ✘); Memory Contagion over-generalised ✘; MemLeak as a CSLR formalism is a construct mismatch ✘; Memoria's 87.1%/−38.7% is not in the abstract (?); MemoryArena's 40–60% is not in the abstract (?).

# Literature review: governance of LLM-agent memory in regulated finance

- **Project:** `agent-memory-governance`. **Stage:** 1 (survey), synthesis of five scout partials.
- **Compiled:** 2026-09-24.
- **Library:** `literature/papers.jsonl`, 609 records. Facet tags: threats 193, mechanisms 175, evaluation 170, finance-apps 88, regulation 31. 68 records are `core`, with notes in `literature/notes/`.
- **Companion files:**
  - `regulation.md`: regulation matrix, tensions, and the verify-with-counsel list.
  - `evaluation.md`: benchmark catalogue, property-to-metric map, and pitfalls.
  - `industry.md`: products, financial-institution deployments, transfer patterns, and incidents.
  - `partials/*.md`: the full scout reports, including query plans for `/radar`.

**How to read the citations.**
- Items are cited by `papers.jsonl` id. Web and regulatory items are cited by URL.
- **"full"** means the scout read the arXiv HTML through a fetch tool that returns an extracted summary. That is thorough skimming of method, results and limitations, not a line-by-line reading.
- **"abstract"** means the claim rests on the abstract only.
- Regulatory claims carry the regulation scout's labels:
  - **[V]** verified against the official text;
  - **[Vm]** verified against a verbatim mirror;
  - **[S]** secondary source only;
  - **[M]** background knowledge, not re-verified.
- Nothing here is legal advice.

---

## 1. Executive summary

1. **The field has split into two communities that rarely cite each other.** Memory systems (Mem0, Zep, Letta, MemOS; arXiv:2504.19413, arXiv:2501.13956, arXiv:2310.08560, arXiv:2507.03724) optimise recall and cost. The memory-security community (about 60 attack papers and about 58 defence papers in our sample) optimises attack success rate (ASR). Compliance requirements enter mainly through a handful of 2026 papers on governance, forgetting and multi-principal memory.
2. **In the last 12 months, forgetting stopped being a way to save tokens and became a correctness and compliance property.** "Delete the record" does not mean erasure. Residue is shown in five places:
   - storage: arXiv:2606.18497 (abstract);
   - index topology and retrieval drift: arXiv:2608.20352 (full);
   - derived runtime state (summaries, KV cache, plans): arXiv:2609.04875 (full);
   - correlated multimodal memory: arXiv:2606.29788 (abstract);
   - revoked facts that are still retrieved and acted on: arXiv:2609.08258 (full).

   The first cross-product forgetting benchmark appeared in June 2026 (arXiv:2606.15903, full).
3. **Multi-principal memory governance became a named problem in 2026.**
   - Benchmarks: GateMem, which combines utility, access control and forgetting in one score (arXiv:2606.18829, full); CIMemories (arXiv:2511.14937, full); CI-Work (arXiv:2604.21308, full); AgentLeak (arXiv:2602.11510, full).
   - Mechanisms: authorization-before-context (arXiv:2608.17148, abstract); authorization continuity (arXiv:2609.25563, abstract); Collaborative Memory (arXiv:2505.18279, full).
   - Production evidence: MemClaw's own evaluation found that the semantic-search path leaked on 72/164 cross-fleet probes, although its abstract reports "zero cross-fleet leakage" on the propagation path (arXiv:2606.24535, full, verified by the orchestrator).
4. **Memory poisoning is crowded.**
   - About 6–10 new attack papers a month since 2026-05.
   - The frontier has moved to realistic persistence: environment-injected, dormant, collusive, and on deployed harnesses (arXiv:2609.13889, arXiv:2608.01637, arXiv:2605.01970).
   - Defences moved to formal and cryptographic authority, such as origin-bound action gates (arXiv:2606.24322, full) and signed mutation logs (arXiv:2608.02843, abstract).
   - A new attack alone is no longer a contribution.
5. **Evaluation moved from recall to governance and to meta-evaluation.**
   - Memory benchmarks now test update and staleness (arXiv:2605.06527) and cost (arXiv:2609.05441).
   - Governance benchmarks appeared, as listed above.
   - A validity wave shows that ASR and judge-based scores are routinely under-specified (arXiv:2609.25173, arXiv:2507.02825, arXiv:2608.00794).
   - Almost every governance benchmark is synthetic and labelled by LLMs.
6. **Finance is the missing domain.**
   - Finance safety benchmarks (FinVault arXiv:2601.07853, Fiducia-bench arXiv:2608.16055, ReguSim arXiv:2608.19974) have no persistent memory.
   - Memory-governance benchmarks have no finance obligations: no information barriers, suitability or record retention.
   - The only finance client-memory benchmark, FinPerMA (arXiv:2608.04095, full), measures utility only.
   - No finance paper attacks persistent memory.
7. **Industry deliberately avoids persistent memory in regulated settings.**
   - Ryt Bank's regulator-approved agent is "stateless, session-bound" (arXiv:2510.07645, full).
   - Stateless Decision Memory argues that regulated deployments need deterministic replay, auditable rationale, isolation and statelessness (arXiv:2604.20158, full; n=10).
   - None of the 10 institutions checked discloses how agent memory is scoped per client, retained or erased (`industry.md`).
8. **Vendors ship API-level deletion and namespace scoping, and several say that derived memories survive deletion of the source chat.** This applies to ChatGPT (snippet only), Claude, M365 Copilot and Zep. Microsoft 365 Copilot memory is outside Purview retention and "doesn't generate audit log entries" (`industry.md`).
9. **Regulation changed materially in 2026.**
   - US SR 26-2 / OCC 2026-13 (2026-04-17) superseded SR 11-7 and **scoped out generative and agentic AI** [V; independently corroborated by the orchestrator].
   - The EU Digital Omnibus on AI, Reg. (EU) 2026/1744, was published in the OJ on 2026-07-24 and entered into force on 2026-07-27. It moved Annex III high-risk obligations, including credit scoring, to **2027-12-02** [S, corroborated].
   - The FINRA 2026 oversight report names agents that "may unintentionally store" sensitive data as a risk [V].
   - The FSB consultation (2026-06-10) names memory poisoning [V].
   - No regulator says whether an agent memory entry is a "record", a "communication" or a "log".
10. **The legal tensions are real but partly reconcilable.**
    - GDPR Art. 17(3)(b) exempts retention required by *EU or Member State* law [Vm].
    - The EU AMLR Art. 77 mandates **retain-then-delete** [Vm].
    - SEC 17a-4(f)(2) permits an audit-trail alternative to WORM storage [Vm].
    - The unreconciled parts are cross-border retention (US rules are not "Union law"), classification of memory items, and how to log *what was recalled* without copying personal data.
11. **Six convergent gaps were flagged independently by at least three scouts** (§8):
    - retention vs erasure;
    - information barriers in shared memory;
    - no finance-specific memory evaluation or threat study;
    - deletion that does not forget, and end-to-end erasure verification;
    - the utility cost of stateless vs governed memory, and defence cost in regulatory units;
    - audit and lineage, including audit-log attacks and recall logging.

    Six more are flagged by two facets.
12. **Evidence quality is thin.**
    - Most frontier governance papers are 2026 arXiv preprints, often single-author, evaluated on self-built harnesses, with no third-party replication.
    - The abstract-vs-full-text gap in arXiv:2606.24535 is a concrete warning.
    - SciSpace coverage stops around 2026-01, and law-review coverage is weak.

---

## 2. The problem space: memory operations × governance properties

### 2.1 Unified model

We model agent memory with seven **operations** and seven **governance properties**.

**Operations**, which merge arXiv:2505.00675's six operations, arXiv:2604.16548's lifecycle stages and the regulation scout's S/R/C/Sh/M/F/L legend:
- **Store** (S): formation or write.
- **Retain** (R): persistence over time, TTL and expiry.
- **Recall** (C): retrieval into context, then action.
- **Share** (Sh): promotion or propagation across agents, users or tenants, including consolidation into shared tiers.
- **Modify** (M): update, rectify, consolidate, supersede.
- **Forget** (F): delete, erase, unlearn, roll back.
- **Log** (L): audit, provenance record, explanation.

**Properties**, with the finance reading:
- **Retain-when-required** (RR): books and records, suitability or KYC evidence, AI Act logs.
- **Forget-when-required** (FR): erasure, storage limitation, minimisation.
- **Isolation** (ISO): cross-client, cross-tenant, information barriers, need-to-know.
- **Integrity** (INT): poisoning, tampering, silent corruption.
- **Provenance/auditability** (PROV): who wrote what, from where, and what the agent knew when it acted.
- **Freshness** (FRESH): stale KYC, superseded policy, revoked facts.
- **Utility** (UTIL): task value and cost.

### 2.2 Coverage grid (the key artifact)

Each cell rates the state of the evidence across facets.
- ● means mechanisms **and** metrics exist, with at least some full-text evidence.
- ◐ means partial: mechanisms without metrics, or metrics without mechanisms, or only abstract-level evidence.
- ○ means essentially nothing was found.
- "—" means the cell is not meaningful.

A **§** mark means at least one binding finance or data-protection obligation attaches directly. The rating is our synthesis from the partials, not a count.

| Operation ↓ / Property → | RR | FR | ISO | INT | PROV | FRESH | UTIL |
|---|---|---|---|---|---|---|---|
| **Store** | ○ § | ◐ § | ◐ § | ● | ◐ § | ◐ | ● |
| **Retain** | ◐ § | ◐ § | ◐ | ◐ § | ◐ § | ◐ | ◐ |
| **Recall** | ◐ § | ● § | ● § | ● | ○ § | ● § | ● |
| **Share** | ○ | ○ § | ◐ § | ◐ | ◐ | ○ | ◐ |
| **Modify** | ◐ § | ◐ § | ○ | ◐ | ◐ § | ● § | ◐ |
| **Forget** | ○ § | ● § | ◐ | ◐ | ◐ | — | ◐ |
| **Log** | ◐ § | ○ § | ○ | ○ § | ◐ § | — | ◐ |

The pattern is that **the empty cells cluster where a finance obligation attaches**. Examples are retaining mandated records through consolidation (Store×RR, Forget×RR), erasure across shared copies (Share×FR), lineage of recall (Recall×PROV), and the integrity and privacy of the audit log itself (Log×INT, Log×FR). Integrity and recall-side isolation are the best-covered cells.

### 2.3 Cell detail

Only cells with content are listed. The columns are **Mechanisms / Threats / Metrics / Obligations**. The obligation codes point to `regulation.md` §1.

**Store**

| Cell | Mechanisms | Threats | Metrics | Obligations |
|---|---|---|---|---|
| Store×RR | Append-only event log plus a single projection at decision time (arXiv:2604.20158, full); commit-on-write snapshots (arXiv:2607.27773, full) | Consolidation or compression drops safety-critical facts (arXiv:2609.05767, abstract); structured memory systems discard preference signals (arXiv:2608.04095, full) | **None scores mandated retention** (evaluation §3) | SEC 17a-3 records to be made [M]; MiFID II 16(6)/(7) [M]; suitability and KYC information (MiFID 25(2), Reg BI) [M] |
| Store×FR (minimise at write) | Stateless session design (arXiv:2510.07645, full); consent and minimum-necessary as run-time attributes (arXiv:2504.17669, full, healthcare); edge-side placeholder redaction (arXiv:2605.09530, abstract) | Implicit extraction: >95% of ChatGPT profile entries were extracted without an explicit prompt (arXiv:2609.14697, abstract); FINRA's "may unintentionally store" risk [V] | None specific | GDPR 5(1)(b)(c), 25 [Vm/M]; Reg S-P [S] |
| Store×ISO | Private/public classification at write (arXiv:2609.12320, abstract); per-item audience tag (arXiv:2608.17148, abstract); private and shared tiers with time-varying ACL graphs (arXiv:2505.18279, full) | Query-only injection into shared memory: MINJA (arXiv:2503.03704, full), MAFIA (arXiv:2608.03844, abstract) | Visibility-classification accuracy of 96.0% (arXiv:2609.12320, abstract) | Exchange Act §15(g) [V]; FINRA 5280(b) [V] |
| Store×INT | Write gates (arXiv:2603.11768, full, conceptual; arXiv:2608.00426, full); origin binding (arXiv:2606.24322, full); signed entries and Merkle log (arXiv:2605.14421, full); transactional commit (arXiv:2607.23929, full) | Threat classes T1–T7 (`partials/threats.md` §2): backdoor, query-only, environment-injected, dormant, collusive, forged precedent, multimodal | MPSR (arXiv:2607.27080); injection success rate (ISR) vs execution (arXiv:2605.08442, full); detector TPR 67.7%, weak-signal about 25% (arXiv:2606.04329, full) | AI Act Art. 15 robustness [M]; FSB names "memory poisoning" [V] |
| Store×PROV | Per-fragment immutable provenance (arXiv:2505.18279); writer identity and scope on every object (arXiv:2606.24535); derivation DAG (arXiv:2605.14421) | Provenance laundering through summarisation or tool echo (arXiv:2607.29167, abstract; arXiv:2606.24322) | Content detection 68% and lineage 47% on laundered writes (arXiv:2606.24322) | ESMA ¶23–24 "data sources used" [V]; MiFID Del. Reg. 72 [S] |
| Store×FRESH | Bi-temporal edges (arXiv:2501.13956, abstract) | Temporal memory contamination (arXiv:2605.17830, abstract) | — (tested at recall) | GDPR 5(1)(d) accuracy [Vm] |
| Store×UTIL | Learned extraction and consolidation (arXiv:2601.04463; arXiv:2508.19828) | — | LoCoMo, LongMemEval (arXiv:2402.17753, arXiv:2410.10813); write-time defences show no detectable accuracy cost at ±4.5 pp (arXiv:2609.22818, full) | — |

**Retain**

| Cell | Mechanisms | Threats | Metrics | Obligations |
|---|---|---|---|---|
| Retain×RR | Immutable logs (arXiv:2603.11768, arXiv:2605.14421); version history (arXiv:2607.27773). **Industry:** M365 Copilot memory outside Purview retention; AgentCore raw events expire after at most 365 days (`industry.md`) | A read-time reranker falsely quarantines 33.6% of legitimate memories (arXiv:2609.22818, full) | **None** | SEC 17a-4(b)(4), 3 years, WORM or audit trail [Vm]; FINRA 4511, 6 years [V]; MiFID II 16(7), 5–7 years [M]; AMLR Art. 77, 5 years after the relationship [Vm]; AI Act Arts 19 and 26(6), ≥6 months or folded into financial-services documentation [Vm]; Colorado SB 26-189, 3 years [V] |
| Retain×FR | TTL and decay (arXiv:2601.18642, abstract; Foundry store TTL); privacy-aware retention policies (arXiv:2512.12856, abstract) | Backups and "anonymisation as a workaround" (EDPB CEF 2025 [V]) | Six forgetting-policy metrics (arXiv:2512.12856, abstract) | GDPR 5(1)(e) [Vm]; **AMLR 77 delete at expiry** [Vm] |
| Retain×ISO | Epoch-key crypto-shredding (arXiv:2606.18497, abstract); key-separated pseudonymised archives (CJEU C-413/23 P [S]; EDPB draft 02/2026 [V]) | Insider (A3) access to archives | — | GDPR 5(1)(f) [Vm] |
| Retain×INT | Merkle or hash-chained stores (arXiv:2605.14421; arXiv:2608.02843) | Self-state file tampering (arXiv:2607.17986, abstract) | — | DORA RTS Art. 12 tamper-protected logs [Vm] |
| Retain×PROV | Version history, 17a-4(f)(2) audit-trail option | — | Version Recall@1 (arXiv:2607.27773) | 17a-4(f)(2) [Vm] |
| Retain×FRESH | Decay (arXiv:2601.18642) | Accumulated staleness and interference (arXiv:2608.07622, abstract) | Per-fact age trajectories (arXiv:2606.17328, abstract) | KYC refresh [M] |
| Retain×UTIL | Stateless vs full memory: FinPerMA no-memory 18.2–31.2% vs full context 40.1–46.9% (arXiv:2608.04095, full); DPM parity at moderate budgets (arXiv:2604.20158, full) | — | **The utility cost of "stateless" vs governed memory has not been measured** | Consumer Duty: forgetting context can itself harm the customer [M] |

**Recall**

| Cell | Mechanisms | Threats | Metrics | Obligations |
|---|---|---|---|---|
| Recall×RR | Deterministic replay from a log (arXiv:2604.20158) | Hosted-API replay is non-reproducible (arXiv:2608.11344, abstract) | DPM factual precision and reasoning coherence (arXiv:2604.20158); DEMM-Bench evidence sufficiency (arXiv:2606.20634, abstract) | 17a-4(f)(3) prompt production [Vm]; ECOA/Reg B reasons [M]; UK Art. 22C review [S]; Colorado 30-day explanation [V] |
| Recall×FR | Retrieval-time validity filter (arXiv:2609.08258, full); traversal-safe deletion (arXiv:2609.19456, abstract, **title/abstract mismatch**); ITEP (arXiv:2608.20352) | Revoked fact returned leads to unsafe action 42–44% (arXiv:2609.08258); drift 3.7× the control after correct API delete (arXiv:2608.20352, full) | GateMem F (arXiv:2606.18829); leak@k (arXiv:2511.04934); Ghost Echoes centroid drift and latency oracle | GDPR 17 [Vm] |
| Recall×ISO | Namespaces and ACL read gates (industry); all-participants rule (arXiv:2509.14608, full); authorization-before-context (arXiv:2608.17148); history-dependent Brewer–Nash access (doi:10.1109/secpri.1989.36295, abstract) | Extraction T10 (arXiv:2502.13172, full); contextual-integrity violations T12; cross-tenant T13; **MemClaw search path 72/164** (arXiv:2606.24535); Mem0 A = 28.1% (arXiv:2606.18829) | GateMem A; Violation@n (arXiv:2511.14937); PersistBench FR (arXiv:2602.01146); AgentLeak CLR (arXiv:2602.11510); CI-Work leakage, violation and conveyance (arXiv:2604.21308) | §15(g) [V]; FINRA 5280(b) [V]; MAR Art. 9 [V]; GDPR 5(1)(b) [Vm] |
| Recall×INT | A-MemGuard (arXiv:2510.02373, full); act gate (arXiv:2606.24322); certified smoothed retrieval (arXiv:2606.12703, abstract); RAGDefender (arXiv:2511.01268, abstract) | Coordinated poisoning takes 10/10 top-k (arXiv:2608.16044, abstract) | ASR-r/a/t (arXiv:2407.12784) | AI Act Art. 15 [M] |
| Recall×PROV | Citation and attribution in RAG (arXiv:2305.14627) | Misattribution: poisoning blamed on the model in 64/64 cases (arXiv:2605.22842, abstract) | **No memory-lineage metric** (evaluation §3) | AI Act Art. 12 logging (interpretation) [Vm]; Reg B [M] |
| Recall×FRESH | Supersession (arXiv:2606.24535); revocation filter (arXiv:2609.08258) | Stale suitability or KYC (T14) | STALE (arXiv:2605.06527, full); LongMemEval knowledge update; FAMA (arXiv:2604.20006, abstract); FinPerMA post-shock | Suitability [M]; GDPR accuracy [Vm] |
| Recall×UTIL | Retrieval depth | Retrieval depth raises utility and risk together (arXiv:2608.30177, full) | Over-refusal (GateMem); read-time reranker −4.4 pp (arXiv:2609.22818) | — |

**Share**

| Cell | Mechanisms | Threats | Metrics | Obligations |
|---|---|---|---|---|
| Share×FR | **None found** for propagating deletion to derived or shared copies | Derived memory survives source deletion (vendors; `industry.md`) | — | GDPR 17(2) [Vm] |
| Share×ISO | Promotion gates (arXiv:2608.00426, full); authorization continuity (arXiv:2609.25563, abstract); platform mediation of propagation (arXiv:2609.19226, abstract, tagged at synthesis); policy-governed propagation (arXiv:2606.24535); purpose-bound mediation (arXiv:2506.22815, abstract); ethical-wall sync in legal tech (Harvey+Intapp, `industry.md`) | Multi-agent propagation T8; tool-side extraction despite isolation, 80% (arXiv:2607.23444, full) | AgentLeak internal channels: 41.7% of traces with safe outputs leak internally (arXiv:2602.11510); relevance retrieval leaks 53.0% (arXiv:2506.22815, abstract) | §15(g), 5280(b), MAR 9 and 18 [V/M]; SAR confidentiality (finance partial) |
| Share×INT | Cross-agent gates (arXiv:2608.00426) | Contagion across a simulated trading floor (arXiv:2609.19789, abstract); trust laundering (arXiv:2609.17648, abstract) | — | FSB contractual rollback rights [V] |
| Share×PROV | Provenance on propagated objects: 50/50 chains reconstructed (arXiv:2606.24535) | Provenance collapse (arXiv:2605.25869, abstract) | — | ESMA ¶24 [V] |
| Share×UTIL | Shared tiers cut resource calls by 59–61% (arXiv:2505.18279) | — | — | DORA / EBA third-party register [Vm/S] |

**Modify**

| Cell | Mechanisms | Threats | Metrics | Obligations |
|---|---|---|---|---|
| Modify×RR | Version control and rollback (arXiv:2607.27773); git-backed memory (arXiv:2606.14470, abstract); AGM revision graph (arXiv:2603.17244, abstract); Zep invalidates rather than deletes (`industry.md`) | — | Version R@1 of 12.0→20.5% (LoCoMo) and 24.3→39.4% (MAB) (arXiv:2607.27773) | MiFID Del. Reg. 72(1) "prior contents easily ascertained" [S]; 17a-4(f)(2) [Vm] |
| Modify×FR | Supersede plus archive (regulation T3) | — | — | GDPR Art. 16 rectification [M]; Colorado right to correct [V] |
| Modify×INT | Transactional commit and cascade repair (arXiv:2607.23929); rollback repair 85.3% (arXiv:2608.10502, full) | Preference drift vs manipulation: CAPTURE 11.5% → **24.7% under adaptive attack** (arXiv:2609.02265, abstract); forged precedent T6 | Repair without collateral loss (SRSR, arXiv:2607.27080) | Suitability updates [M] |
| Modify×PROV | Derivation DAG repair (arXiv:2607.23929): only declared provenance is protected | Consolidation launders origin (T9) | — | ESMA ¶24 [V] |
| Modify×FRESH | Temporal supersession | Contradiction detection only 49% because of dedup ordering (arXiv:2606.24535) | STALE; MemConflict (arXiv:2605.20926, abstract) | GDPR 5(1)(d) [Vm] |
| Modify×UTIL | RL memory managers (arXiv:2508.19828, arXiv:2601.01885, arXiv:2604.01560) optimise task reward only | — | — | — |

**Forget**

| Cell | Mechanisms | Threats | Metrics | Obligations |
|---|---|---|---|---|
| Forget×FR | API delete (all vendors); epoch-key crypto-shredding (arXiv:2606.18497, abstract); provenance-guided selective replay (arXiv:2609.04875, full); mutation-time LLM hook (arXiv:2606.15903, full); semantic deletion (arXiv:2606.29788, abstract); agentic unlearning of parameters and memory (arXiv:2602.17692, abstract) | T16: storage residue (25.5% of names, 100% of age/gender markers, 99% of faces recovered, arXiv:2606.18497, abstract); runtime residue 0.86–1.00 (arXiv:2609.04875); correlated recovery 18.3% (arXiv:2606.29788, abstract) | ForgetEval pass rates: deterministic 63–68% vs LLM hook 91.7–94.2% (arXiv:2606.15903); GateMem F; Leak@probes (arXiv:2609.04875); leak@k | GDPR 17 [Vm]; CCPA 1798.105 [V]; EDPB CEF 2025 [V] |
| Forget×RR | **No mechanism reconciles erase with retain.** The split-store pattern (erasable working memory plus a restricted, crypto-shreddable compliance archive) is proposed but untested (mechanisms §8) | Over-forgetting legitimate records (arXiv:2609.22818) | **None**: every forgetting metric rewards forgetting | GDPR 17(3)(b)(e) [Vm]; AMLR 77 [Vm]; 17a-4 [Vm] |
| Forget×ISO | Per-tenant deletion (Weaviate tenant delete; Foundry `delete_scope`; Mem0 `delete_all` without a filter now errors) | Prefix-matched namespaces (LangGraph `namespace_prefix`; AgentCore advises a trailing slash) | — | — |
| Forget×INT | Selective repair of poisoned memory (arXiv:2607.27080; arXiv:2608.10502) | — | SRSR | — |
| Forget×PROV | Signed deletion proofs (arXiv:2606.18497, abstract); information-provenance graph (arXiv:2606.29788, abstract) | Undeclared derivations escape repair (arXiv:2607.23929) | — | Evidence of erasure is itself a record (regulation T4) |
| Forget×UTIL | Replay costs 9.3× fewer tokens than a reset, and cost grows with T−τ+1 (arXiv:2609.04875); LLM hook takes 2.3 s per case (arXiv:2606.15903) | — | $/run (arXiv:2606.15903) | — |

**Log**

| Cell | Mechanisms | Threats | Metrics | Obligations |
|---|---|---|---|---|
| Log×RR | Agent Flight Recorder (arXiv:2609.01931, abstract); Right to History (arXiv:2602.20214, abstract); NovaFabric (arXiv:2609.12582, abstract). **Industry:** M365 Copilot memory actions are not audited in Purview | — | Fiducia-bench audit trail (arXiv:2608.16055, full) | AI Act 12, 19, 26(6) [Vm]; FINRA 2026 "track and log agent actions" [V]; FSB logging [V]; ESMA ¶24 [V]; DORA RTS 12 [Vm] |
| Log×FR | Hashes or pointers instead of content (our observation; no source) | Recall logs duplicate personal data outside the memory store (regulation T5) | — | AI Act 19(1) defers to data-protection law [Vm]; GDPR 5(1)(c) [Vm] |
| Log×INT | Merkle/RFC 6962 logs (arXiv:2605.14421); Ed25519-signed mutation (arXiv:2608.02843) | **No attack study on memory audit logs.** Closest: MAFIA cuts audit-agent detection from 83.3% to ≤7.4% (arXiv:2608.03844, abstract); SafeClawBench audit-evidence harm (arXiv:2606.18356, abstract) | — | DORA RTS 12 [Vm]; 17a-4(f) [Vm] |
| Log×PROV | Lineage-guided enforcement (arXiv:2605.14421) | Accurate-but-misleading logs via laundering (T9) | DEMM-Bench: trace presence overclaims sufficiency in 75% of cases (arXiv:2606.20634, abstract); ReguSim: showing the rationale raises false accepts from 25% to 46.9% (arXiv:2608.19974, full) | ESMA ¶24 [V]; Reg B [M] |
| Log×UTIL | Sub-ms Merkle overhead (arXiv:2605.14421); 4.9 ms per signed transition (arXiv:2608.02843, abstract); 1.3 µs act gate (arXiv:2606.24322) | — | — | — |

---

## 3. Mechanisms (condensed from `partials/mechanisms.md`)

**Taxonomy.** Memory forms, functions and dynamics follow arXiv:2512.13564 (full, skim) and arXiv:2505.00675.
- Forms:
  - flat fact stores (Mem0 arXiv:2504.19413);
  - temporal knowledge graphs (Zep arXiv:2501.13956, A-MEM arXiv:2502.12110);
  - OS-style tiers (MemGPT arXiv:2310.08560, MemOS arXiv:2507.03724);
  - parametric or KV memory (arXiv:2402.04624, arXiv:2609.23466, arXiv:2603.04428).
- Functions: factual, episodic and procedural (arXiv:2304.03442, arXiv:2303.11366, arXiv:2305.16291).
- Dynamics: RL-learned management (arXiv:2508.19828, arXiv:2601.01885, arXiv:2604.01560) and forgetting for efficiency (arXiv:2601.18642).
- Topology: single-user, multi-agent shared (arXiv:2507.07957), or multi-principal (arXiv:2505.18279, arXiv:2609.12320, arXiv:2606.18829).

**Governance mechanism families.** Full table in the partial, §2b.

1. **Scope-read and isolation.**
   - Private/shared tiers with time-varying bipartite ACL graphs and per-fragment provenance (arXiv:2505.18279, full). Resource calls fall 59–61%, but there is no adversarial leakage test.
   - Microsoft's "all participants" rule, shipped in Copilot Tuning (arXiv:2509.14608, full, no quantitative evaluation).
   - The anti-monotone audience rule (arXiv:2608.17148, abstract).
2. **Authorised write and commit.**
   - Write/read gates with an immutable log (arXiv:2603.11768, full, conceptual).
   - Transactional belief commit with cascade repair (MemTX arXiv:2607.23929, full): success 0.756–0.956, and the only method with zero downstream harm on all backbones.
   - A human-in-the-loop governance channel in a vendor-neutral wire format (arXiv:2606.01138, abstract).
3. **Provenance and integrity.**
   - Signed entries, a Merkle log, a derivation DAG and an action gate (MemLineage arXiv:2605.14421, full): ASR 0/0/0, sub-ms overhead.
   - Signed authorised mutation (arXiv:2608.02843, abstract).
   - Origin-bound authority checked in TLA+ (arXiv:2606.24322, full): ASR 0% on all channels; 1.3 µs gate.
   - These come from the poisoning-defence community, not the compliance community.
4. **Erase with derivatives.**
   - Epoch-key rotation (arXiv:2606.18497, abstract): 0% PII recovery at about 0.005 ms per record, with signed deletion proofs.
   - Execution-state unlearning by selective replay (arXiv:2609.04875, full): leakage 0.00 vs 0.86–1.00 for a record delete, at 9.3× fewer tokens than a reset.
   - Where the LLM sits in the forgetting control plane (arXiv:2606.15903, full).
   - Semantic deletion over an information-provenance graph (arXiv:2606.29788, abstract).
   - Traversal-safe ANN deletion (arXiv:2609.19456, abstract; **the arXiv title does not match the abstract, so check before citing**).
5. **Versioning and rollback**: ChronoMem (arXiv:2607.27773, full), GitOfThoughts (arXiv:2606.14470, abstract), AGM revision (arXiv:2603.17244, abstract).
6. **Data-model framing.** GEM defines six correctness conditions for memory as governed evolving state. It argues that no record-level system satisfies them (arXiv:2605.26252, full, argument only).
7. **Regulated-industry designs.**
   - Deterministic Projection Memory: an append-only log plus one projection at decision time (arXiv:2604.20158, full).
   - Statistically gated, versioned memory writes for fraud detection (SR-Fraud arXiv:2609.27287, full; Coinbase).
   - An organisation-scoped runtime for financial SOC workflows (arXiv:2605.30604, abstract, tagged at synthesis).

**Frontier, 2025-09 → 2026-09.**
- Forgetting became a correctness property.
- Multi-principal governance was named as a problem.
- Cryptographic provenance arrived.
- Database and transaction semantics entered memory design (arXiv:2605.26252, arXiv:2607.23929).
- The first production negative results appeared (arXiv:2606.24535).
- RL-learned and parametric memory grew fast; both make erasure and audit harder and are not covered by the governance papers.

---

## 4. Threats (condensed from `partials/threats.md`)

**Taxonomy.** Stages follow the lifecycle survey arXiv:2604.16548 (full): Write, Store, Retrieve, Execute, Share, Forget. Adversaries range from an outsider controlling content (A0) through a query-only tenant (A1), a malicious tool or vendor (A2), an insider (A3) and a compromised peer agent (A4) to no adversary (N). There are **18 threat classes, T1–T18**; see the partial's §2 table, which includes a finance reading for each. The key classes for this project:
- **Query-only cross-user injection (T2).**
  - MINJA reaches ISR about 98.2% and ASR about 76.8% (arXiv:2503.03704, full).
  - **The literature disagrees here.** A realistic replication with pre-existing legitimate memories "dramatically reduces" effectiveness (arXiv:2601.05504, abstract).
  - MAFIA evades auditing agents (arXiv:2608.03844, abstract).
- **Environment-injected and dormant poisoning (T3, T4).**
  - Trojan Hippo fires on finance, health and identity topics and persists for 100+ sessions (arXiv:2605.01970, full).
  - PMPA works on OpenClaw and Claude Code (arXiv:2609.13889, abstract).
- **Collusive or salami poisoning (T5)**: arXiv:2608.01637 (abstract). Admission filters are provably bypassable (arXiv:2608.16044, abstract).
- **Forged precedent and experience grafting (T6)**: MemoryGraft arXiv:2512.16962. The finance reading is "compliance check already done" recorded as a precedent.
- **Multi-agent propagation and provenance laundering (T8, T9)**: arXiv:2608.00426, arXiv:2605.22842, arXiv:2607.29167.
- **Extraction (T10, T11).**
  - MEXTRA (arXiv:2502.13172, full).
  - SPORE: 80% extraction through tools despite per-user isolation (arXiv:2607.23444, full).
- **No-adversary contextual-integrity leakage (T12).**
  - CIMemories: up to 69% attribute-level violations, and GPT-5 violations accumulate from 0.1% to 9.6% over 40 tasks (arXiv:2511.14937, full).
  - CI-Work: 15.8–50.9% violation rate (arXiv:2604.21308, full).
- **Stale, revoked or deleted data coming back (T14, T16)**: arXiv:2609.08258, arXiv:2609.04875, arXiv:2606.29788.
- **Audit-log integrity (T18).** Mechanisms exist, but there are **no attack papers**.

**Defences and their cost.**
- MAPLE-Guard cuts ASR from 38.2% to 0.9% for 1–4 pp of benign loss and no extra LLM calls (arXiv:2608.00426, full).
- A-MemGuard reports EHR ASR falling from 100% to 2.13% at about 7.8K tokens per task (arXiv:2510.02373, full).
- The revocation filter reaches 0.0% unsafe action (arXiv:2609.08258).
- Content detectors are weak: TPR ≤67.7% (arXiv:2606.04329).
- Storage-time success does not predict execution (arXiv:2605.08442, full).
- Only one study isolates **benign-traffic cost** (arXiv:2609.22818, full, n=5 conversations). Write-time defences cost nothing detectable. A read-time reranker costs −4.4 pp and falsely quarantines 33.6% of legitimate memories.
- The threats scout's synthesis, at medium confidence: **authority at action time (origin-bound gates) plus retrieval-time validity** works better than content detection.

**Crowding.**
- Very crowded: poisoning attacks and defences.
- Moderate and growing: contextual integrity and extraction.
- Suddenly crowded: lifecycle benchmarks (MemPoison arXiv:2607.14651, MemSecBench arXiv:2607.27080, MemRiskBench arXiv:2609.14976, MPBench, MemEvoBench, all from 2026-07 to 2026-09).
- Sparse but accelerating: erasure verification.
- Very sparse: preference drift vs manipulation (arXiv:2609.02265 only).
- **Empty: finance-specific persistent-memory threats.** The finance attack papers target feeds and messages, not memory (arXiv:2608.24069, full; arXiv:2609.19789, arXiv:2601.07853).

**Standards and incidents.** Details and URLs are in `industry.md`.
- OWASP ASI06 "Memory & Context Poisoning" (2025-12-09).
- MITRE ATLAS AML.T0080 (the official page returned 404, so the id was confirmed only via Microsoft Learn and CSA).
- The Microsoft Zero-Trust catalogue (2026-07-28).
- **Microsoft's in-the-wild "AI Recommendation Poisoning" (2026-02-10)**, with finance and crypto sites among those using it.
- FINOS RI-27, whose finance scenarios are hypothetical.
- **No documented incident of a financial institution's agent memory being poisoned or leaking across clients was found.**

---

## 5. Evaluation (condensed; full catalogue in `evaluation.md`)

- **General agent evaluation**:
  - τ-bench pass^k (arXiv:2406.12045);
  - ST-WebAgentBench Completion-under-Policy (arXiv:2410.06703);
  - AgentDojo, which has a banking suite (arXiv:2406.13352);
  - HAL, a cost-aware harness (arXiv:2510.11977);
  - METR time horizons (arXiv:2503.14499).
- **Memory benchmarks.** Recall: LoCoMo (arXiv:2402.17753), LongMemEval (arXiv:2410.10813, abstract), MemoryAgentBench with selective forgetting (arXiv:2507.05257, full). In 2026 they moved to:
  - staleness: STALE (arXiv:2605.06527, full) and FAMA (arXiv:2604.20006);
  - action utility and cost: MERIT, 23,440 episodes (arXiv:2609.05441, abstract);
  - finance client memory: FinPerMA (arXiv:2608.04095, full), utility only.

  LoCoMo and LongMemEval are nearing saturation. Vendor LoCoMo claims conflict: Zep reports 84% and Mem0's re-run 58.44%; see `industry.md`.
- **Governance benchmarks.**
  - GateMem, MGS = U·(1−A)·(1−F) (arXiv:2606.18829, full). With GPT-5.4 in the medical domain, long context scores MGS 80.1% vs Mem0 25.8%.
  - CIMemories, Violation@n.
  - PersistBench (arXiv:2602.01146, full).
  - AgentLeak, which has a finance domain as a leakage context (arXiv:2602.11510, full).
  - ForgetEval (arXiv:2606.15903).
  - Ghost Echoes (arXiv:2608.20352, full).
  - MemSecBench, which adds repair via SRSR (arXiv:2607.27080, full).
  - DEMM-Bench, evidence sufficiency (arXiv:2606.20634, abstract).
- **Finance governance benchmarks without memory.**
  - FinVault: ASR up to 50% (arXiv:2601.07853, abstract, because the HTML returned 404).
  - Fiducia-bench, KYC/AML governability (arXiv:2608.16055, full).
  - ReguSim (arXiv:2608.19974, full).
  - CNFinBench (arXiv:2512.09506).
  - Governance-task decoupling in a synthetic banking domain (arXiv:2605.14744, abstract, tagged at synthesis).
- **Property → metric map** (see `evaluation.md` §3):
  - Freshness and isolation are the most mature.
  - Forget-when-required is fragmented: interface-level and index-level checks have never been combined.
  - Provenance/audit has no memory-lineage metric.
  - **Retain-when-required has no metric at all.**
- **Pitfalls** (see `evaluation.md` §4):
  - refusal is a free exploit in privacy and forgetting benchmarks (arXiv:2507.02825);
  - ASR is under-specified: 65.3% of 259 papers report no variance (arXiv:2609.25173);
  - judge validity compounds across pipeline stages (arXiv:2608.00794);
  - memory-backend effects reverse across harnesses (arXiv:2607.27080);
  - output-only audits miss internal leaks (arXiv:2602.11510);
  - greedy decoding overstates forgetting (arXiv:2511.04934);
  - construct validity against actual law has not been established (arXiv:2508.05464, abstract).

---

## 6. Finance applications (condensed from `partials/finance-apps.md`)

- **Use cases where memory matters, by regulatory sensitivity.**
  - Wealth and advisory copilots are very high: suitability, communications record-keeping, consent. Examples: arXiv:2512.02230 (full) and the Morgan Stanley Debrief deployment.
  - Client-facing advice or robo-advice is very high: suitability, profiling, vulnerability. FinPerMA; Sell Me This Stock shows 65–99% suitability violations under tool manipulation (arXiv:2603.12564, full); Conv-FinRe (arXiv:2602.16990, full).
  - AML/SAR investigation is extreme. Co-Investigator reuses prior SARs as memory without access or retention analysis (arXiv:2509.08380, full).
  - Fraud (SR-Fraud arXiv:2609.27287) and credit or claims (arXiv:2604.20158) are high.
  - Trading research is low on personal data but high on look-ahead contamination and model risk: FinMem (arXiv:2311.13743, full), TradingAgents (arXiv:2412.20138), and AMA (arXiv:2510.11695).
- **Deployment reality.**
  - Banks disclose adoption and human oversight (JPMorgan LLM Suite, Goldman GS AI Assistant, BNY Eliza with "digital employees" that have credentials and supervisors, BofA EricaAssist, DBS role-based CSO Assistant).
  - None discloses how its agent memory is governed.
  - Retention statements concern the *model vendor* (zero data retention, "no training").
  - Ryt Bank chose no persistent memory (arXiv:2510.07645).
  - A UK bank's pre-deployment validation uses single-session customer digital twins (arXiv:2607.26060, full). **The abstract says only "a leading UK bank". A specific bank attribution appeared in the scout's tool extraction but is not supported by the arXiv page, so no bank is named here.**
- **Transfer from other domains.**
  - HIPAA "minimum necessary" and consent as run-time attributes (arXiv:2504.17669, full).
  - Legal-tech ethical walls synced from the system of record into the AI platform (Harvey+Intapp, 2026-07-23, vendor page; it does not say whether memory is covered).
  - Ambient-scribe "delete after sign-off" retention. This collides with finance record-keeping.
  - MedMemoryBench "trap events" (arXiv:2605.11814, full).
  - In the other direction, finance papers lead on model-risk-style change control of memory (arXiv:2609.27287, arXiv:2604.20158).
- **Usable data (all synthetic or small).**
  - FinPerMA: 276 personas; **licence not stated**.
  - Conv-FinRe: CC BY 4.0, 10 real users.
  - CRMArena-Pro: CC BY-SA, confidentiality queries (arXiv:2505.18878, full).
  - Wealth-management workflows (arXiv:2512.02230).
  - PersonaLedger: synthetic transactions (arXiv:2601.03149, abstract).
  - InvestLogicBench: 151 real investors; licence and privacy to verify (arXiv:2608.06108, abstract).
  - Two artifacts are CC BY-NC-ND and cannot be modified: arXiv:2603.12564 and arXiv:2604.20158.
- **SR 11-7 is superseded.** The brief and the finance-apps partial refer to SR 11-7. Since 2026-04-17, SR 26-2 supersedes it and excludes GenAI and agentic AI (`regulation.md` §1d). The model-risk framing of the brief should be updated. PRA SS1/23 (UK) is the model-risk hook that remains technology-agnostic [S].

---

## 7. Regulation (summary; full matrix in `regulation.md`)

- **Matrix scope.** It covers these instrument families across EU, UK, US, Singapore and Hong Kong, each mapped to the memory operations it affects:
  - data protection: GDPR, UK DUAA, CCPA/CPPA, Reg S-P;
  - AI-specific: AI Act and the omnibus, Colorado SB 26-189, NIST, ISO 42001;
  - record-keeping and conduct: SEC 17a-3/17a-4, FINRA 4511/3110/2210, MiFID II and Del. Reg. 2017/565, ESMA, AMLR;
  - model risk and resilience: SR 26-2, PRA SS1/23, DORA, EBA, EIOPA, MAS, HKMA;
  - information barriers: §15(g), FINRA 5280, MAR 9 and 18, MiFID conflicts;
  - consumer protection: Consumer Duty, Mills Review, ECOA/Reg B, suitability.
- **Seven tensions (T1–T7)**:
  - retention vs erasure within the EU (partly reconciled by 17(3)(b) and AMLR 77);
  - cross-border retention vs erasure (US rules are not "Union law"; a legal reading, not a sourced conclusion);
  - immutability vs rectification (reconcilable by supersede-with-history);
  - forget that doesn't forget;
  - logging obligations that create new personal data;
  - shared memory vs information barriers (no regulator guidance or scholarship found);
  - retaining context for explainability vs minimisation.
- **2026 changes.**
  - SR 26-2 / OCC 2026-13 (2026-04-17), with its GenAI/agentic carve-out.
  - Reg. (EU) 2026/1744: OJ 2026-07-24, in force 2026-07-27, Annex III moved to 2027-12-02.
  - Both were verified from the regulator page (SR 26-2 [V]) or secondaries, and **independently corroborated by the orchestrator via multiple law-firm and industry sources**.
  - Other 2026 items: UK Arts 22A–D (2026-02-05); the Colorado SB 26-189 re-enactment (effective 2027-01-01); the FINRA 2026 report; the FSB consultation; the FCA Mills Review; EDPB CEF 2025 on erasure.
- **2027 cluster.** Colorado and CPPA ADMT take effect 2027-01-01, AMLR 2027-07-10, and AI Act Annex III 2027-12-02.
- **Not verified.** MAS AIRG content is **unverified** because the consultation PDF could not be extracted. 15 items are on the verify-with-counsel list (`regulation.md` §6).

---

## 8. Cross-facet tensions and convergent gaps

These are **evidence dossiers, not rankings or research proposals**; the order carries no priority. "Flagged by" lists the scouts that raised the gap independently in their own gap sections. Confidence is ours, based on how many independent searches support the absence. "Anyone on it?" lists the closest existing work. Section references such as "threats §8.4" point to `partials/<facet>.md`. `evaluation.md` and `regulation.md` keep the partials' section numbers.

### G1. Retention vs erasure ("forget for behaviour, retain for audit")
- **Flagged by:** mechanisms §8.2, threats §8.4, evaluation §7.2, regulation T1/T2/T3 and gaps 1 and 6, finance-apps §6.6. That is all five facets.
- **Evidence:**
  - Every forgetting mechanism and metric treats forgetting as good (arXiv:2606.15903, arXiv:2606.18829, arXiv:2609.04875).
  - Versioning and immutable logs keep everything (arXiv:2607.27773, arXiv:2605.14421).
  - The law contains partial reconciliations: GDPR 17(3)(b) [Vm], AMLR 77 retain-then-delete [Vm], and the 17a-4(f)(2) audit-trail option [Vm].
  - The cross-border case is unresolved: 17a-4 and FINRA 4511 are not "Union law".
  - Vendors: M365 Copilot memory sits outside Purview retention, and AgentCore raw events expire after at most 365 days, which is less than the 3–7 year mandates.
  - Healthcare's delete-after-sign-off collides with finance record-keeping (finance-apps §4).
- **Confidence:** high that no paper or benchmark models both obligations together.
- **Anyone on it?** No paper found. Adjacent: DPM log plus projection (arXiv:2604.20158); crypto-shredding (arXiv:2606.18497); the email-archive analogue (doi:10.1007/s11623-019-1206-3, German, abstract); blockchain vs GDPR (doi:10.1093/idpl/ipy009).

### G2. Information barriers and cross-client isolation in shared memory
- **Flagged by:** mechanisms §8.1 and §8.4, threats §8.2, evaluation §7.5, regulation T6 and gap 2, finance-apps §6.7.
- **Evidence:**
  - An arXiv search for "information barrier" + memory returned nothing relevant (mechanisms, finance).
  - Legal duties turn on arrangements that "effectively prevent" information flow: §15(g) [V], FINRA 5280(b) [V], MAR 9 [V].
  - Relevance retrieval leaks 53.0% of private items (arXiv:2506.22815, abstract).
  - MemClaw's search path leaked 72/164 while GET-by-id bypassed sub-tenant scope (arXiv:2606.24535, full).
  - 41.7% of traces with safe outputs leak internally (arXiv:2602.11510).
  - Consolidation can carry restricted facts across scopes (arXiv:2609.25563, abstract; arXiv:2607.29167, abstract).
  - The formal model exists: Brewer–Nash, history-dependent access (doi:10.1109/secpri.1989.36295).
  - Legal tech ships wall sync (Harvey+Intapp), but it is unclear whether memory is covered.
  - Whether an AI component belongs on a MAR Art. 18 insider list is open.
- **Confidence:** high for absence in what was searched. Medium overall, because law-review coverage is weak.
- **Anyone on it?** Near neighbours in non-finance domains: GateMem (arXiv:2606.18829), AIM/MUMBench (arXiv:2609.12320), authorization-before-context (arXiv:2608.17148), AkasicMEM (arXiv:2609.25563, dated 2026-09-22, so very recent), PAPC (arXiv:2609.19226), PiSAs (arXiv:2607.05318), and Collaborative Memory (arXiv:2505.18279). None models desks, MNPI, wall-crossing or client-by-client need-to-know.

### G3. No finance-specific memory evaluation or threat study
- **Flagged by:** mechanisms §8.1, threats §8.1, evaluation §7.1, finance-apps §6.4.
- **Evidence:**
  - Finance safety benchmarks lack persistent memory (arXiv:2601.07853, arXiv:2608.16055, arXiv:2608.19974, arXiv:2512.09506).
  - Memory-governance benchmarks lack finance obligations.
  - FinPerMA, Conv-FinRe and the wealth-management benchmark measure utility only.
  - Trading-agent attacks leave the `past_memory` slot unattacked (arXiv:2608.24069, full).
  - CRMArena-Pro tests confidentiality only as refusal of a direct request (arXiv:2505.18878).
  - There is no "trap event" analogue to MedMemoryBench (arXiv:2605.11814): sanctions hits, vulnerability flags, powers of attorney.
- **Confidence:** high. The evaluation scout searched with ≥6 phrasings.
- **Anyone on it?** Closest are FinPerMA (as a base) and AgentLeak's finance domain. Note that lifecycle benchmarks are proliferating, five in three months, so a new generic benchmark would be marginal (threats §8.9).

### G4. Deletion ≠ forgetting: end-to-end, verifiable erasure across derived artifacts
- **Flagged by:** mechanisms §8.3, threats §8.4 and T16, evaluation §7.3, regulation T4 and gap 4.
- **Evidence:** the residue layers are each covered by a separate paper:
  - storage (arXiv:2606.18497, abstract);
  - index topology (arXiv:2608.20352, full; arXiv:2609.19456, abstract, metadata mismatch);
  - runtime state (arXiv:2609.04875, full);
  - multimodal correlation (arXiv:2606.29788, abstract);
  - revocation (arXiv:2609.08258, full);
  - control-plane placement (arXiv:2606.15903, full);
  - parameters plus memory "backflow" (arXiv:2602.17692, abstract);
  - sampling resurfacing (arXiv:2511.04934).

  Regulation side: the EDPB CEF 2025 identifies backups and "anonymisation as a workaround" as recurring failures [V], and unlearning is not legal removal (arXiv:2412.06966, abstract). Vendors state that derived memories survive source deletion.
- **Confidence:** medium-high that no cross-layer protocol with a statistical guarantee exists.
- **Anyone on it?** Yes, actively. This is the fastest-moving gap (2026-06 to 2026-09); a cross-layer paper could appear at any time. The Chakraborttii group (Ghost Vectors, Ghost Echoes) and the ForgetEval author are the most active.

### G5. Utility cost of governance: stateless vs governed memory, and defence cost in regulatory units
- **Flagged by:** finance-apps §6.2, threats §8.3, evaluation §7.6 and §3 (utility row), mechanisms §5 (latency–safety trade-off stated as open by arXiv:2603.11768).
- **Evidence:**
  - Regulated deployments choose statelessness (arXiv:2510.07645, arXiv:2604.20158).
  - Memory helps substantially in advisory (FinPerMA: no memory 18–31% vs full context 40–47%).
  - Only one benign-cost study exists (arXiv:2609.22818, n=5, ±4.5 pp).
  - Nobody measures false quarantine or erasure of *legitimate client records* as a compliance harm, or the confirmation burden of maker-checker-style gates (acknowledged but unmeasured in arXiv:2606.24322).
  - Few governance benchmarks report utility, cost and governance jointly with confidence intervals; GateMem and MERIT are the exceptions.
- **Confidence:** medium-high.
- **Anyone on it?** Partial: GateMem's joint score, MERIT's cost metering (arXiv:2609.05441), and MemGauge's knob trade-offs (arXiv:2608.30177).

### G6. Auditability of memory: lineage metrics, recall logging vs minimisation, and audit-log attacks
- **Flagged by:** threats §8.5 and T18, evaluation §7.4, mechanisms §8.5, regulation T5 and gap 3.
- **Evidence:**
  - Many tamper-evident mechanisms exist (arXiv:2605.14421, arXiv:2608.02843, arXiv:2609.01931, arXiv:2602.20214) but have not been evaluated against supervisory expectations.
  - **No attack study on memory audit logs.** The closest are MAFIA evading auditing agents (arXiv:2608.03844, abstract) and accurate-but-misleading laundering (arXiv:2605.22842, arXiv:2607.29167).
  - No memory-lineage metric; DEMM-Bench covers runtime records, not memory (arXiv:2606.20634).
  - Logging mandates (AI Act 12/19/26(6), DORA RTS 12, ESMA ¶24, FINRA 2026, FSB) give no method for logging *what was recalled* without copying personal data.
  - Industry: no product documents a memory-operation audit log, and M365 Copilot explicitly does not create one.
- **Confidence:** medium overall. High for the absence of audit-log attack papers; medium for lineage metrics.
- **Anyone on it?** Mechanism side only: MemLineage (arXiv:2605.14421), Right to History (arXiv:2602.20214), and Fiducia-bench's audit-trail metric (arXiv:2608.16055).

### G7. Classification: which memory items are "records", "communications" or "logs"?
- **Flagged by:** regulation gap 1, finance-apps §6.6, mechanisms §6 (derived memory survives deletion, so is it a record?).
- **Evidence:**
  - No official text classifies agent memory (regulation §2, "Not found").
  - The off-channel enforcement analogy says the retention duty follows the content, not the tool [S].
  - FINRA names "unintentionally store" but stops there [V].
  - The SEC Spring 2026 agenda may narrow "business as such" [S].
- **Confidence:** high for the absence of official guidance. This is a legal question more than a technical one.
- **Anyone on it?** Not found.

### G8. Authorization continuity through consolidation and derivation
- **Flagged by:** mechanisms §8.4, threats T9 and §8.2, regulation T6.
- **Evidence:** Consolidation moves private fragments into shared tiers (arXiv:2505.18279). Laundering (arXiv:2607.29167, arXiv:2605.16746, both abstract). AkasicMEM (arXiv:2609.25563, abstract). No quantitative study of how often summarisation carries restricted facts across scopes in realistic multi-client workloads.
- **Confidence:** medium. This overlaps G2 and is kept separate because it concerns *derived* rather than retrieved items.
- **Anyone on it?** AkasicMEM (very recent) and PAPC (arXiv:2609.19226).

### G9. Consent and purpose limitation at the memory-item level
- **Flagged by:** mechanisms §8.6, finance-apps §4 (HIPAA pattern), regulation (GDPR 5(1)(b), T1 purpose reading).
- **Evidence:** No mechanism attaches purpose or consent metadata to memory items and enforces it at recall; arXiv:2606.26627 (full) lists policy representation as open. The HIPAA framework does it for healthcare context access (arXiv:2504.17669). More than 95% of ChatGPT profile entries are implicitly extracted (arXiv:2609.14697, abstract).
- **Confidence:** medium.
- **Anyone on it?** arXiv:2504.17669 (healthcare); SovereignPA-Bench, consent dimension (arXiv:2607.05363, abstract).

### G10. Suitability-consistent memory: preference drift vs manipulation, and staleness against authoritative sources
- **Flagged by:** threats §8.7, finance-apps §6.5, evaluation §3 (freshness row).
- **Evidence:**
  - CAPTURE is the only paper on preference drift vs manipulation, and its poisoning success roughly doubles under an adaptive attacker (arXiv:2609.02265, abstract).
  - FinPerMA's post-shock gap widens from 8.0 to 13.0 pp.
  - Sell Me This Stock shows evaluation blindness to suitability drift (arXiv:2603.12564).
  - Freshness against external sources (sanctions lists, rule changes) is untested for memory agents.
- **Confidence:** medium.
- **Anyone on it?** FinPerMA (utility framing only).

### G11. Evidence quality: adaptive attackers, independent replication, construct validity
- **Flagged by:** threats §8.6, mechanisms §8.8, evaluation §7.7 and §4.
- **Evidence:**
  - Governance mechanisms are evaluated on self-built harnesses (arXiv:2606.24535, arXiv:2607.23929, arXiv:2605.14421, arXiv:2606.15903).
  - The abstract-vs-full-text gap in arXiv:2606.24535 shows why this matters.
  - Adaptive attacks are rarely tested.
  - Labels come from LLM personas, not legal text (evaluation pitfall 11).
  - ASR under-specification (arXiv:2609.25173).
- **Confidence:** medium-high.
- **Anyone on it?** The meta-evaluation papers only.

### G12. Regulation-as-code for memory operations
- **Flagged by:** regulation gap 8, mechanisms §5 (policy representation open, arXiv:2606.26627).
- **Evidence:**
  - Rule-encoding work targets rule text: arXiv:2505.19804; arXiv:2609.20016 (AI Act Arts 8–15 in Rego); doi:10.1093/ojls/gqad014 on the limits.
  - Nothing encodes retention classes, barrier labels and purpose tags as checkable policies on memory reads and writes.
  - Compliance datasets exist but are not connected to memory behaviour (arXiv:2603.13933, arXiv:2605.29742; evaluation §7.7).
- **Confidence:** medium.

**Single-facet gaps**, recorded but not cross-validated:
- Governance of RL-learned and parametric memory managers (mechanisms §8.7).
- SAR/AML memory as a blind spot (finance-apps §6.3).
- The US model-risk vacuum under SR 26-2 (regulation gap 5).
- The 2027 timeline cluster (regulation gap 7).
- Storage ≠ execution metrics (threats §8.8).
- Tail or worst-case compliance metrics (evaluation §7.6).

### Cross-facet disagreements to carry forward
- **MemClaw leakage (arXiv:2606.24535).** The abstract says "zero cross-fleet leakage" on the propagation path. The full text (Table 2, §8.1) reports search_leak_rate = 72/164 = 0.439 on the semantic-search path. Both are true for different paths; the orchestrator verified this against the full text. The mechanisms scout's table correctly shows 72/164; any abstract-only citation of this paper would be wrong.
- **MINJA effectiveness.** ISR about 98% (arXiv:2503.03704) vs "dramatically reduced" with realistic legitimate memory (arXiv:2601.05504, abstract).
- **Write-time filtering.** It appears "free" on benign traffic (arXiv:2609.22818) but ineffective against execution (arXiv:2605.08442), laundering (arXiv:2606.24322) and coordinated poisoning (arXiv:2608.16044).
- **Read level of Ghost Echoes (arXiv:2608.20352).** The mechanisms scout marked it abstract-only; the evaluation scout read it in full. We use the full-text reading.
- **Ghost Vectors (arXiv:2606.18497)** appears in the mechanisms comparison table without an abstract-only mark. Per its note it was **read per abstract only**, so all of its numbers are abstract-level.
- **Contradiction handling in MemClaw.** It is presented as a supersession mechanism (mechanisms), but detection was only 49% because of dedup ordering. Both views are in the paper.

---

## 9. Top 15 must-read papers

All 15 were read "full" in the sense defined at the top: fetch-tool extraction of the arXiv HTML, not a line-by-line reading.

| # | id | Why | Read |
|---|---|---|---|
| 1 | arXiv:2606.18829 (GateMem) | The only benchmark scoring utility × access control × forgetting jointly, with over-refusal; the natural template to extend to finance | full |
| 2 | arXiv:2609.04875 (execution-state unlearning) | Shows record deletion leaves 0.86–1.00 leakage in derived state; provenance-guided replay fixes it at a stated cost | full |
| 3 | arXiv:2606.24535 (MemClaw) | Rare production negative results. Leakage depends on the read path; the abstract-vs-full-text gap (orchestrator-verified) | full |
| 4 | arXiv:2604.16548 (memory security survey) | Lifecycle taxonomy of attacks and defences used across this review | full |
| 5 | arXiv:2511.14937 (CIMemories) | Contextual integrity of persistent memory; Violation@n shows leakage accumulating over tasks; includes finance attributes | full |
| 6 | arXiv:2604.20158 (Stateless Decision Memory) | The clearest statement of why regulated industry avoids agent memory (replay, audit, isolation); weak n=10 | full |
| 7 | arXiv:2608.04095 (FinPerMA) | The only finance client-memory benchmark; post-shock staleness design; utility-only; licence unstated | full |
| 8 | arXiv:2609.08258 (Revoked but Still Authoritative) | Revoked facts are acted on 42–44% of the time across five memory products; a deterministic filter fixes it | full |
| 9 | arXiv:2606.15903 (control-plane forgetting) | First cross-product forgetting benchmark (13 configurations incl. Mem0, Letta, Graphiti) | full |
| 10 | arXiv:2608.20352 (Ghost Echoes) | The most concrete black-box erasure-verification protocol for vector memory | full (evaluation scout) |
| 11 | arXiv:2606.24322 (TMA-NM) | Origin-bound authority at action time with TLA+ checking; the defence pattern that survives laundering | full |
| 12 | arXiv:2602.11510 (AgentLeak) | Internal-channel leakage (memory, inter-agent) invisible to output audits; has a finance domain | full |
| 13 | arXiv:2609.22818 (Price of Safety) | The only benign-traffic cost study of memory defences; 33.6% false quarantine | full |
| 14 | arXiv:2505.18279 (Collaborative Memory) | The foundational multi-user memory design with time-varying ACLs and provenance | full |
| 15 | arXiv:2605.26252 (Is Agent Memory a Database?) | GEM correctness conditions; a data-management framing that fits record-keeping | full (argument paper) |

Non-paper must-reads, all [V]:
- SR 26-2, footnote 3: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
- FINRA 2026 report, GenAI section: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
- EDPB CEF 2025 on erasure: https://www.edpb.europa.eu/news/news/2026/edpb-identifies-challenges-hindering-full-implementation-right-erasure_en
- FSB sound practices consultation: https://www.fsb.org/uploads/P100626.pdf

---

## 10. Key groups, labs and companies

- **Memory systems:**
  - Letta/MemGPT (UC Berkeley origin);
  - Mem0;
  - Zep/Graphiti;
  - MemTensor/MemOS;
  - Microsoft Research (participant-aware access, CI-Work, PrivacyLens-Live);
  - Accenture Center for Advanced AI (Collaborative Memory);
  - Purdue, Bertino group (ChronoMem).
- **Forgetting and erasure:** the Chakraborttii group (Ghost Vectors, Ghost Echoes); several single-author 2026 papers (ForgetEval arXiv:2606.15903, MutMem arXiv:2608.02843, arXiv:2605.30771), which are not peer reviewed.
- **Memory security:**
  - Zhen Xiang, Jiliang Tang and Pengfei He (MINJA, MEXTRA);
  - Bo Li, Dawn Song and Chaowei Xiao (AgentPoison);
  - Jinyuan Jia and Neil Gong (PoisonedRAG);
  - industry: Microsoft Defender/AIRT, Palo Alto Unit 42, Cisco (OWASP ASI06 lead), Zenity, Embrace The Red.
- **Privacy and contextual integrity:** Mireshghallah, Sap, Choi, Shokri (ConfAIde; CIMemories with Meta/Google co-authors); Stanford SALT (PrivacyLens).
- **Evaluation:**
  - UK AISI (Inspect, AgentHarm);
  - ETH SPY Lab (AgentDojo);
  - Princeton (HAL);
  - Sierra (τ-bench);
  - METR;
  - UCLA/Tencent (LongMemEval), Snap/UNC (LoCoMo), UCSD (MemoryAgentBench).
- **Finance:**
  - The Fin AI / Ananiadou group (AMA, InvestorBench, Conv-FinRe);
  - aifinlab (FinVault);
  - SUFE (CNFinBench);
  - Coinbase (SR-Fraud);
  - Ryt Bank / ILMU (Malaysia);
  - Salesforce AI Research (CRMArena-Pro).
- **Standards and industry bodies:** FINOS (AI Governance Framework), FSB, IOSCO, MAS Project MindForge, NIST CAISI.

---

## 11. Coverage and limitations

**Sources and cutoffs.**
- arXiv was searched from 2025-06-01 to 2026-09-22/24; the newest hits are 2026-09-22 (threats) and 2026-09-23 (finance-apps).
- The SciSpace index lags, and its newest hits date from about 2026-01.
- OpenAlex was used for foundations and law; its coverage of law reviews and SSRN is weak.
- Semantic Scholar forward snowballing ran only on a few seeds (FinMem, Collaborative Memory, Ghost Vectors, MINJA, AgentPoison) and was capped at 25 results.
- The evaluation scout skipped forward snowballing because of arXiv rate limits.
- Web and regulator sources were accessed 2026-09-24.
- `inputs/INDEX.md` does not exist, so there were no PI materials to build on.

**Reading depth.**
- 68 `core` records have notes. About 54 were read "full" via tool-extracted HTML summaries. **This is thorough skimming, not a line-by-line reading.**
- Every other citation is per abstract.
- The following **core** items are abstract-only:
  - arXiv:2606.18497 (Ghost Vectors);
  - arXiv:2601.07853 (FinVault; HTML 404);
  - arXiv:2410.10813 (LongMemEval);
  - arXiv:2412.06966, arXiv:2607.21345, arXiv:2608.11344;
  - doi:10.1109/secpri.1989.36295;
  - the regulation-facet DOIs, whose abstracts were in several cases not retrieved.
- The abstract-vs-full-text discrepancy in arXiv:2606.24535 (zero leakage vs 72/164 by path) shows that abstract-only claims about *governance results* are risky.

**Unverified or flagged items.**
- **arXiv:2607.26060.** The scout's tool extraction attributed the paper to a specific UK bank. The arXiv abstract page lists no affiliations and says only "a leading UK bank" (checked by the orchestrator). Cite it as "a leading UK bank (per abstract)".
- **arXiv:2609.19456.** The arXiv title ("Beyond Private Training: The New Landscape of AI Privacy") does not match the abstract (TSD-AUDIT, traversal-safe deletion). The metadata is as returned by arXiv. Check before citing.
- **ChatGPT memory FAQ**: HTTP 403; the row in `industry.md` is built from search-result snippets. Re-verify.
- **MAS AIRG consultation content** is unverified because PDF text extraction failed. Its status ("will be finalised soon", PQ reply 2026-08-05) is [V].
- **MITRE ATLAS AML.T0080** official page returned 404; the id was confirmed via Microsoft Learn and CSA.
- The **NIST CAISI RFI** page was blocked, so whether it mentions memory is unknown.
- **Morgan Stanley Debrief** and **OpenAI case-study** content came from snippets (timeout or 403).
- **UBS Red** came from a Microsoft case-study snippet.
- The **Salesforce 30-day audit retention** claim comes from third parties and is unverified.
- **ABA ambient-scribe** content came from snippets.
- **EUR-Lex, consilium and iso.org** blocked automated access. EU texts are verified against mirrors [Vm] or secondaries [S].
- **Reg. (EU) 2026/1744**: the OJ date is resolved to publication on 2026-07-24 and entry into force on 2026-07-27, per the orchestrator's corroboration. Final article wording is still to be checked against the OJ.
- Zenodo preprints (e.g. doi:10.5281/zenodo.18346036, doi:10.5281/zenodo.18136347, doi:10.5281/zenodo.18110491) are recorded, unreviewed and low-assurance.

**Tool failures.**
- The arXiv API returned HTTP 429 on several queries across scouts; one legal query in finance-apps never succeeded.
- Boolean-heavy arXiv queries often returned 0, especially for "information barrier". The absence claims in G2 therefore rest partly on weak search tooling.
- WebFetch could not parse many PDFs; a stdlib extractor worked for SR 26-2, FINRA, ESMA, FSB and HKMA.

**Library housekeeping at synthesis.**
- Three previously untagged in-scope records were tagged with `lit.py tag`: arXiv:2609.19226 → mechanisms; arXiv:2605.30604 → finance-apps; arXiv:2605.14744 → finance-apps and evaluation.
- 16 other untagged records (early-scan leftovers such as surveys on mental health, GUI agents and edge diffusion) were **not synthesised** because they are off-topic or peripheral.
- Three records are `screened-out-offtopic`. Two of them are the MemGuard false positives the threats scout reported: arXiv:2609.04547 and arXiv:2603.26797.
- Partials cite two items that were deliberately not added to the library: TIEM (arXiv 2608.13024, finance-apps snowball) and the LAVR Zenodo preprint (regulation). They are not cited in this synthesis.

**Dropped from the synthesis.**
- Most of the roughly 500 facet-tagged records appear only in the partials' tables. This review cites about 200. The partials remain the complete record, and nothing was deleted from `papers.jsonl`.
- The query plans live in the partials, for `/radar`.

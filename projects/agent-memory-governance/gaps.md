# Research gaps: governance of LLM-agent memory in regulated finance (RIA context)

- **Stage:** 2, gaps. **Draft 2026-09-25**, awaiting an adversarial pass and the PI's choice.
- **Author:** gap-analyst agent.
- **Inputs read:** `brief.md`; `STATE.md`; `literature/review.md` (in full); `regulation.md`; `evaluation.md`; `industry.md`; the gap sections of all five partials; 35 notes in `literature/notes/`; `inputs/INDEX.md` (in full).
- **New full-text reads for this stage:**
  - arXiv:2608.01679 (AuthMem-Bench); note written.
  - arXiv:2606.10062 (FRS); note written.
  - arXiv:2608.10509 (MAP-Graph), limitations section only.
- **Checks run:**
  - 13 arXiv recency queries (`--since 2026-06-01 --sort date`);
  - 10 SciSpace questions;
  - 29 new records added with `--tag gaps-check`, and 10 existing records re-tagged.
- **CONFIDENTIAL. Stays on this machine.** This file compares gaps with the PI's internal governance design. That design is referred to only as "the PI design", with its control numbers (C#). None of its text was used in any search. Before any part of this file is shared, strip every "PI design covers" field.
- **Evidence labels:**
  - **full** = full text or a project note based on full text;
  - **abstract** = per abstract, weak;
  - **[M]** = background legal knowledge, not verified here; check with counsel.
- **Entity perimeter.** The PI's entity is an RIA, not a bank or broker-dealer, so the relevant anchors differ from the review's bank-centred reading:
  - Advisers Act Rule 204-2 books and records, and the SEC's proposed 204-2 modernisation [S, Spring 2026 agenda];
  - Advisers Act §204A MNPI policies [M];
  - Reg S-P;
  - fiduciary duty and suitability-type care obligations [M];
  - GDPR, for EU data subjects.

  GDPR Art. 17(3)(b) exempts only retention required by *Union or Member State* law [Vm]. It does **not** cover a 204-2 duty.

---

## 0. How the candidates were generated: the nine lenses

Each lens was applied to G1–G12 (review §8), to the ingest agent's nine new candidates (N1–N9, INDEX §6(e)), to the PI's stated open questions, and to the single-facet items.

| Lens | What it surfaced | Feeds |
|---|---|---|
| 1. Stated limitations | **GateMem** checks forgetting "at the interface only". Its soft attacks are not adversarial (full). **FRS** (arXiv:2606.10062): the canary grammar sacrifices "ecological validity"; embedding- and cache-level residue is named as the next step (full). **AuthMem-Bench**: metadata "cannot recover information omitted during consolidation", and the focal proposition was retained in only 139/350 cases (full). **Price of Safety** (arXiv:2609.22818): ±4.5 pp resolution, one backbone, no attacks, act-time defences not measured (full). **Collaborative Memory** (arXiv:2505.18279): concurrency and role churn unexplored; no adversarial leakage test (full). **MemSecBench**: backend effects reverse across harnesses (full). **MAP-Graph**: synthetic, templated, one four-agent round; 9.11% impermissible allows remain in the high-risk group (full). **MemLineage** (arXiv:2605.14421): single host, prevention only (full). **Execution-state unlearning** (arXiv:2609.04875): runtime state only (full). **Ghost Echoes**: primarily one backend (full). **FinPerMA**: synthetic, one seed, utility only (full). **DPM** (arXiv:2604.20158): n=10, one model family (full). | GP1, GP2, GP3, GP4, GP5, GP6, GP7 |
| 2. Contradictions | **Stateless vs governed memory.** Industry and regulated papers choose statelessness (arXiv:2510.07645, arXiv:2604.20158, full); the PI's programme bets on governed persistence. **Recency vs authority.** SciSpace's "newer-over-older is necessary" (AI review) contradicts AuthMem-Bench and arXiv:2608.25553. **Write-time filtering.** It looks free on benign traffic (arXiv:2609.22818) but fails against false assertions: 0/360 poisoned memories rejected (arXiv:2608.21230, abstract). **MINJA.** ASR is high in the original (arXiv:2503.03704, full) and "dramatically reduced" in a realistic replication (arXiv:2601.05504, abstract). **MemClaw.** Zero leakage per the abstract vs 72/164 on the search path per the full text (arXiv:2606.24535). **Ghost Echoes.** Index rebuild does not remove drift, which contradicts the usual "rebuild = erase" engineering assumption (full). | GP5, GP7, GP8 |
| 3. Evaluation gaps | No metric scores mandated retention (evaluation §3). Forgetting metrics are interface-only *or* index-only, never combined. There is no memory-lineage metric. Finance benchmarks have no memory, and memory benchmarks have no finance obligations. Refusal is a free exploit (arXiv:2507.02825, full). Most papers are single-run and unvalidated for ASR (arXiv:2609.25173, full). Nearly all labels are LLM-generated. | GP1, GP4, GP5, GP6 |
| 4. Assumption gaps | Single principal (AuthMem-Bench, CIMemories, STALE). "Forgetting is always good" (every forgetting metric). "API delete = erasure". "Recency = authority". Output-only audit is sufficient (refuted by arXiv:2602.11510, full). The backend is fixed, with a stationary model and embedder (refuted by arXiv:2609.05339, abstract, and arXiv:2607.27080, full). Per-item authorisation is sufficient, i.e. no aggregation. English-only. | GP1, GP2, GP3, GP7 |
| 5. Transfer gaps | Brewer–Nash and database inference control → memory composition (GP2). HIPAA minimum-necessary as a run-time attribute (arXiv:2504.17669, full) → purpose-bound memory (GP9). MedMemoryBench "trap events" (arXiv:2605.11814, full) → finance must-retain facts (GP1/GP8). Filtered-ANN research from databases (arXiv:2606.14193, arXiv:2606.16341, abstract) → governed recall (GP5). Crypto-shredding → retention-compatible erasure (GP1). Differential testing from software engineering → backend conformance (GP7). | GP1, GP2, GP5, GP7, GP9 |
| 6. Academia ↔ industry | Vendors publish no erasure or isolation results. Four vendors say derived memories survive source deletion (`industry.md`). M365 Copilot memory is outside Purview retention and audit. No financial institution discloses how it governs memory. Industry treats poisoning as an operational control problem, academia as an attack-optimisation problem. | GP1, GP4, GP6, GP7 |
| 7. Scale / resource | Governance results come from tiny stores: 200 records (SPORE), 50–500 (MemGauge), n=5 conversations (Price of Safety), n=10 (DPM). Scaling to 10^7+ vectors is stated as open (arXiv:2606.18497, abstract). No study runs at firm scale (thousands of clients, years of records). | GP2, GP4, GP7 |
| 8. Theory ↔ empirics | GEM's impossibility observations are untested (arXiv:2605.26252, full, argument only). The execution-state unlearning lower bound is not tested on multi-client stores. The TMA-NM proof covers a bounded model only. There is no formal account of composition leakage for context assembly; the survey arXiv:2606.26627 (abstract) says only information-flow control covers compositional and cross-session inference. | GP2, GP4 |
| 9. Recency (last ~6 months) | Very long context windows re-open "do we need a store at all?": long-context has the best MGS in GateMem (80.1% vs Mem0 25.8%, full). Frequent model and embedder upgrades create migration risk (arXiv:2609.05339, abstract). Skills and procedural memory are proliferating (arXiv:2608.29596, arXiv:2609.16669, abstract). There is a burst of governed-memory mechanisms (GPM arXiv:2608.12476, MAP-Graph, AkasicMEM, all 2026-08/09) but no shared benchmark with finance obligations. The SEC 204-2 modernisation is proposed, so the retention scope may shift. | GP5, GP7, all |

---

## 1. Summary table (surviving gaps)

Ranking is in §4. Legend:
- **Evidence** = strength of the evidence that the gap exists.
- **Novelty** = novelty against the published literature as of 2026-09-25.
- **PI design** = how far the PI's internal design covers the gap. All of it is untested.
- **Tractability** = for this PI: an RIA with API-only compute and synthetic data by default.

| id | One-line gap | Evidence | Novelty vs literature | PI design covers | Tractability | Contribution type | Confidence |
|---|---|---|---|---|---|---|---|
| **GP1** | No evaluation scores *joint* correctness of mandated retention and erasure/restriction, including mandated facts silently lost in consolidation | Strong (full: evaluation §3, GateMem, AuthMem-Bench 139/350, FRS, SSGM note) | **High**: no paper models both obligations together | Partial (retention and hold states, record-level retention) plus a legal blind spot (17(3)(b)) | High | Benchmark + legal-technical analysis | High (gap); med (payoff) |
| **GP2** | Cross-client need-to-know and information barriers in shared memory, including history-dependent access and aggregation (composition) leakage, are unmeasured | Strong (full: CI-Work, GateMem, Collaborative Memory, MemClaw; regulation T6) | High for the barrier/finance framing; medium for composition (IFC literature) | Partial (isolation, barrier, composition-leakage controls; canary leakage metric) | High | Benchmark + formal model | High (finance/barrier); med (composition) |
| **GP7** | No portable conformance suite shows whether governance guarantees survive a backend, harness or embedder swap; read-path and backend dependence is documented but unsystematised | Strong (full: MemSecBench harness reversal, arXiv:2609.08258 across 5 products, MemClaw GET-by-id bypass) | Medium-high: differential testing of memory backends against a governance contract is absent | **Full, untested** (9 admission gates, canaries, substitution time) | High | Conformance suite + empirical study | Med-high |
| **GP5** | The utility cost of governance (stateless vs governed vs ungoverned) on finance tasks, with governance-induced harms (false restriction, over-refusal, filtered-recall loss, latency), is not measured | Strong (full: Price of Safety limitations, FinPerMA, DPM, TMA-NM confirmation burden) | Medium: GateMem, MemGauge and Price of Safety are partial; no finance or stateless-baseline study | **Full metric design, untested** (false-restriction and latency metrics, utility pairing) | High | Empirical study | High |
| **GP4** | No cross-layer, statistically certified erasure test covering text, derived tiers, embeddings/index, caches, backups/restore and re-index/migration | Strong (full: FRS, Ghost Echoes, execution-state unlearning, ForgetEval, GateMem) | Medium and **shrinking fast**: each layer has a paper | **Full, untested** (physical-layer erasure check, time-to-erasure, recovery after restore) | High | Measurement study + protocol | Med (high scoop risk) |
| **GP6** | No validated memory-lineage metric; no method for logging *what was recalled* under minimisation; no attack study on memory audit trails; no per-record explanation test | Medium-strong (full: evaluation §3, MemLineage limits, ReguSim; T18 empty) | Medium-high (attacks); medium (lineage metric; new mechanisms appearing) | Full design (lineage coverage, effective-policy coverage), untested | Medium | Metric validation + attack study | Med |
| **GP3** | Scope/authority continuity through consolidation *in multi-principal stores* and under finance authority lattices | Medium (full: AuthMem-Bench scope; MAP-Graph limits) | **Low-medium**: AuthMem-Bench, MAP-Graph, AkasicMEM, GPM cover most of it | Full design (consolidation review, assertion type, authority-collapse metric), untested | High | Empirical study; best as a module of GP2 | Med |
| **GP8** | Suitability-consistent memory: staleness against systems of record, and preference drift vs manipulation, across sessions | Medium (full: Sell Me This Stock, STALE, FinPerMA; CAPTURE abstract) | Medium-low (generic staleness is crowded); the finance persistence angle is open | Partial (source hierarchy, stale-memory-use metric) | High | Benchmark module | Med-low |
| **GP9** | Purpose binding and a quantitative notion of "necessary" (minimisation) at memory-write time | Medium (full: HIPAA framework, FRS summarisation; abstract: arXiv:2609.14697, arXiv:2510.03662) | Medium; the legal definition is contested | Partial design (purpose binding, purpose-violation metric, risk tiering idea) | Medium | Formal model + mechanism | Low-med |

---

## 2. Full entries

### GP1. Joint retention and erasure correctness ("keep what you must, forget what you may")
*Merges G1, the technical half of G7, and the retain-side failure of consolidation.*

- **Statement.** No benchmark or mechanism evaluation checks that a memory system, given one history:
  1. keeps records it is obliged to keep, for the mandated period and retrievable for audit, through consolidation, summarisation, supersession and erasure requests;
  2. removes or restricts from operational recall what must be forgotten;
  3. deletes at retention expiry.
- **Evidence.**
  - "No metric scores *mandated* retention… Every forgetting metric treats forgetting as always good" (evaluation.md §3, synthesis of full-text reads).
  - GateMem models deletion but not must-keep obligations (note arXiv_2606.18829, full; our critique, not a stated limitation).
  - AuthMem-Bench: consolidators retained the focal proposition in only **139 of 350** cases, and metadata "cannot recover information omitted during consolidation" (arXiv:2608.01679, full). That is a direct measurement of retain-side loss, although not framed as such.
  - Compression drops safety-critical facts (arXiv:2609.05767, abstract).
  - SSGM's immutable-log-plus-mutable-view pattern "conflicts with erasure duties, and the paper does not discuss this" (note arXiv_2603.11768, full).
  - DPM does not handle deletion or consent (note, full).
  - FRS shows tombstone redaction drives derived-tier residue to zero (arXiv:2606.10062, full). That is a candidate retain-compatible erasure, untested against record-keeping.
  - Legal side:
    - 17(3)(b) covers only EU/Member State law [Vm];
    - AMLR 77 retain-then-delete [Vm];
    - 17a-4(f)(2) audit-trail option [Vm];
    - **Advisers Act 204-2** (books and records incl. written communications relating to advice; 5-year retention, first 2 in an appropriate office [M]);
    - the SEC modernisation is proposed [S].
  - Vendors: M365 memory is outside Purview retention; AgentCore raw events are kept ≤365 days (`industry.md`).
- **Assumption challenged.** Forgetting is monotonically good; a delete request maps to a single state change.
- **What would show the gap is not real.** A published benchmark or metric that jointly scores mandated retention and erasure or restriction on one history. The candidates to check are:
  - **GPM** (arXiv:2608.12476; abstract only, HTML unavailable). It claims "non-revival after retraction or deletion" and a bitemporal ledger. If its ReleaseBench also scores must-retain obligations, GP1's benchmark claim shrinks to the finance/RIA instantiation. **Read its PDF before ideation.**
  - **Reversible forgetting** (arXiv:2608.18177, abstract): active, dormant and retired states. This is about obsolescence, not legal retention.
- **Why it matters / who benefits.**
  - Every regulated firm with EU clients or data subjects plus US record-keeping. For an RIA serving EU persons, 204-2 retention does not fall under 17(3)(b), so a design that "restricts instead of deleting" needs another legal basis [M, counsel].
  - DPAs (EDPB CEF 2025 names retention-period determination and backups).
  - Vendors, who currently cannot show compliance.
- **What makes it hard.**
  - Ground truth needs a record classification: which memory items are 204-2 records? That is G7, a legal question.
  - Scoring "retrievable for audit but not for operational recall" requires two access paths.
  - Cross-border law is unsettled, so labels must be parameterised by jurisdiction scenario, not asserted as law.
- **Anyone on it?** arXiv 2026-06+ (`retention/record-keeping ∧ erasure ∧ agent memory`) returned no paper modelling both obligations. Closest:
  - arXiv:2608.18177 (reversible forgetting, enterprise; abstract);
  - arXiv:2608.07429 (TEPA: revoked history preserved for audit; abstract);
  - arXiv:2608.12476 (GPM; abstract).

  SciSpace returned only a 2006 records-management patent (mandatory minimum retention) and generic forgetting papers, none of them recorded. **Not scooped as of 2026-09-25.**
- **PI design covers: partial (untested).**
  - It has retention and hold lifecycle states, record-level retention, and "restricted is not deleted".
  - It misses the 17(3)(b) limit, AMLR 77 and the 17a-4(f)(2) analogue.
  - It has no metric that scores both obligations.
  - Head start: the 9-state lifecycle gives the benchmark its state space.
- **Contribution type.**
  - A benchmark ("retention-aware forgetting"): must-keep, must-restrict and must-delete labels on synthetic RIA client histories, with erasure requests, legal holds and expiry events.
  - A legal-technical analysis of the cross-border case.
  - Venues:
    - ML datasets-and-benchmarks track or FinTech (ICAIF) for the benchmark;
    - law and tech (e.g. CLSR, or a FAccT/CSLAW-type venue) for the analysis.
- **Minimum viable evidence (API-only).**
  - About 200 synthetic client histories, generated by an API LLM with deterministic label rules.
  - 3–4 OSS backends (Mem0, Graphiti, Letta, LangGraph store), run locally with API LLMs.
  - Metrics:
    - mandated-record survival after N consolidation cycles;
    - operational-recall leak of erased items (leak@k);
    - archive retrievability;
    - expiry deletion.
  - Estimated cost: tens to low hundreds of USD. **Speculation**; needs a budget check at checkpoint 3.
- **Tractability for this PI.** High. The PI holds the lifecycle design and knows 204-2. Needs counsel for record classification.
- **Confidence.** High that the gap exists. Medium on payoff, given benchmark proliferation (5 lifecycle benchmarks in 3 months). The finance-obligation mapping is what differentiates it.

### Adversarial review (reviewer, 2026-09-25)

- **Strongest objection: the legal premise is probably much narrower than claimed.**
  - **Channel archive.** 204-2 retention attaches to (a)(7) written communications *sent or received* that relate to advice, orders, receipts or performance, and to a list of specific books. For an RIA these are captured at the channel: the email/chat archive, notetakers routed to Smarsh or Global Relay, and M365 Copilot prompts and responses under Purview retention and holds (`industry.md` addendum, 2026-09-25).
  - **Memory as a derived copy.** An agent-memory item extracted or consolidated from an archived communication is a derived copy or index, not the record. If every memory item is lineage-bound to an archived original, then erasure or expiry in the memory tier does **not** breach 204-2. The retention-vs-erasure conflict **dissolves at the memory layer and moves to the archive**. There it is an old records-management problem (email archives: doi:10.1007/s11623-019-1206-3, abstract; large-scale RTBF with retention policies: arXiv:1910.13784, abstract), not an agent-memory problem.
  - **Evidence behind the premise.** It rests on labels that are weak:
    - 204-2 scope and periods are **[M]** in both regulation.md and this file.
    - regulation.md §2 found **no official text classifying agent memory as books and records** ("Not found").
    - The "duty follows the content" argument is an off-channel *analogy* [S].
    - 17a-4(b)(4) [Vm] is a broker-dealer rule and does not bind this RIA.
    - Two law-firm views read this session: Skadden (2024) says content that merely "exists or is stored in the application" is "likely not" within 204-2(a)(7) [S]. Cooley (2026-04-24) says untransmitted AI notes may still be required records under *other* categories: (a)(3) order memoranda, (a)(16) performance, (a)(17)(ii) compliance review [S].
  - **The must-keep evidence is a construct slide.** AuthMem-Bench's 139/350 is consolidation *fidelity* loss, not loss of a legally mandated record.
- **Where the conflict survives (legal-technical residue worth studying):**
  1. Memory is the **sole carrier** of a required record. Examples: agent-authored order memoranda or performance workings never transmitted (Cooley's categories); facts captured from unrecorded calls or ambient notes whose raw source is deleted.
  2. **Resurrection.** Memory purged on erasure is re-derived when the archive is re-ingested, re-indexed or restored.
  3. **Holds.** A litigation or exam hold must suspend memory purge only when memory is the carrier.
  4. **EU-law retention** (MiFID 16(7), AMLR 77 [Vm/M]) for EU-regulated entities. This does not apply to this RIA.
- **Threatening prior work:**

  | Work | Read level | Covers | Doesn't cover |
  |---|---|---|---|
  | GPM, arXiv:2608.12476 | Full; note written | The *mechanism pattern* GP1 proposes: a public-view non-revival barrier after retraction or deletion, plus a separately routed audit view that keeps deleted content. Deterministic tests: 3,600-case self-designed suite | It **does not** score mandated retention, expiry, legal hold or record classes. Deletion is whole-user. It explicitly disclaims media, backup and crypto erasure, and says "append-only audit and deletion rights remain in tension" |
  | MAP-Graph, arXiv:2608.10509 | Full; note | "Mark, don't delete, keep lineage for audit" | No retention semantics |
  | AkasicMEM, arXiv:2609.25563 | Full; note | §5.1 proposes derived memory "should inherit the most restrictive" source retention period, and verifiable deletion by semantic probing | Not evaluated |
  | TEPA, arXiv:2608.07429 | Abstract | Revoked history kept for audit | — |
  | MutMem-V2, arXiv:2609.01235 | Abstract | "Retention-preserving, cryptographically authorized mutation" | V1 is not in the library. **Read before ideation** |
  | arXiv:2507.00343 | Abstract; DB community | Erasure under data dependencies, with proactively computed retention times | — |
  | Microsoft Purview | Vendor documentation | Retain-then-delete plus holds for AI interactions | Not for memory |
- **Importance.**
  - A CCO would ask "is the memory a record?" before anything else. Once told that memory is a purgeable cache over the archive, most CCOs would consider the problem solved by architecture.
  - A DPA would care about purge completeness and resurrection, which is GP4 territory.
  - An ML reviewer would see "retention labels" as author-asserted rules.
- **Verdict: survives-narrowed (legal premise weakened).**
  - Confidence is high that no published benchmark jointly scores retain, erase, expiry and hold on agent memory.
  - Confidence is **low-medium** that the joint obligation is a real legal conflict *inside memory* for this RIA.
- **Suggested sharpening.** Reframe as **lineage-complete memory: can agent memory be a provably purgeable derivative of the regulated archive?** Score:
  - (a) *archive coverage*: every memory item that is, or feeds, a record-class item has an archived original;
  - (b) *purge completeness* on erasure or expiry across derived tiers;
  - (c) *no resurrection* on re-ingest, re-index or restore;
  - (d) *hold precedence*;
  - (e) *sole-carrier detection*: memory items with no archived source.

  Also:
  - Run a naive "memory = cache over archive, purge by lineage" baseline first. If it scores near-perfectly, GP1 is a checklist, not research.
  - Drop AuthMem 139/350 as evidence of *legal* retain-side loss.
- **Counsel must confirm before labels are frozen:**
  1. Which memory-item classes, if untransmitted, fall under any 204-2(a) category.
  2. Whether agent-to-client messages composed from memory are fully captured by the firm's archive.
  3. Whether holding the archived original while erasing the memory copy satisfies Art. 17 for EU persons. Also which basis supports retaining the archive against an Art. 17 request, given that 17(3)(b) does not cover US law [Vm] (candidates: 17(3)(e) or Art. 6(1)(f)).
  4. Whether memory used as the working client profile for suitability is itself a "book or record".
  5. The status and scope of the 204-2 modernisation proposal [S].

### GP2. Cross-client need-to-know, information barriers and composition leakage in shared memory
*Merges G2 and N1 (aggregation from individually authorised memories).*

- **Statement.** No study measures whether shared agent memory in a multi-client advisory firm keeps client-A information out of client-B contexts, or MNPI out of the wrong function, under realistic consolidation. None covers history-dependent (Brewer–Nash) access or aggregation, where each item is authorised but the assembled context reveals a restricted inference.
- **Evidence.**
  - "I found no regulator guidance and no academic paper that addresses information barriers for shared AI memory or RAG indices" (regulation.md T6).
  - GateMem has no finance domain and no Chinese-wall structure (note, full).
  - CI-Work "lacks persistent memory across sessions and explicit legal norms such as Chinese walls" (note, full).
  - Collaborative Memory "does not test leakage adversarially", and its transformations of shared fragments are an unmeasured laundering channel (note, full; stated limitations: concurrency and role churn).
  - MemClaw: search-path leak 72/164, and GET-by-id bypassed sub-tenant scope (arXiv:2606.24535, full, orchestrator-verified).
  - AgentLeak: 41.7% of traces with safe outputs leak internally (full).
  - The mere presence of secrets in context leaks through benign outputs (arXiv:2608.19857, abstract), which argues for exclusion *before* context assembly.
  - Composition: the survey arXiv:2606.26627 says only IFC covers "compositional and cross-session inference leakage, the two least-protected risks" (abstract). No memory benchmark tests aggregation.
- **Assumption challenged.** Per-item authorisation implies safe context; isolation is per user, not per client relationship or per function.
- **What would show the gap is not real.** A benchmark with (i) multi-client or finance-function barriers and (ii) aggregation probes over persistent memory. GateMem, MUMBench (arXiv:2609.12320) and CI-Work each lack at least one of these (per notes and abstracts). MAP-Graph and AkasicMEM are mechanisms without barrier semantics.
- **Why it matters.**
  - For an RIA: client confidentiality under Reg S-P and fiduciary duty; MNPI policies under Advisers Act §204A [M]; and the defensibility of any shared "firm memory".
  - For broker-dealers and banks: §15(g), FINRA 5280 and MAR 9 turn on arrangements that "effectively prevent" flow [V].
- **What makes it hard.**
  - Aggregation leakage needs a ground-truth inference model: what B can infer from items {x, y}.
  - Barrier rules differ by firm.
  - LLM judges miss subtle leaks (CI-Work: about 10% missed, full).
  - Canaries help with exact leakage, not inference.
- **Anyone on it?** arXiv 2026-06+ returned nothing on barrier or aggregation in agent memory; the closest hits were generic (MemRiskBench arXiv:2609.14976 includes "cross-user leakage" in 120 scripted episodes, abstract). SciSpace:
  - PermLLM (arXiv:2505.22860; access control for fine-tuned LLMs, not memory);
  - AAC vision (arXiv:2510.11108);
  - participant-aware access (arXiv:2509.14608, full; no quantitative evaluation);
  - a Zenodo SoK on authorization-first retrieval (doi:10.5281/zenodo.18346036, low assurance).

  **No one on the finance-barrier plus composition combination.**
- **PI design covers: partial (untested).** Isolation, barrier/MNPI, composition-leakage and agent-identity controls; physical partitions for hard barriers; a canary-based cross-scope leakage metric. There is no evaluation, no encoding of legal rules and no formal model of aggregation. Its canary metric anchors on MemLeak, which is a construct mismatch (INDEX §1); the right precedents are GateMem A, AgentLeak CLR and MemClaw search_leak_rate.
- **Contribution type.**
  - Benchmark: a synthetic RIA with many clients, a research/PM function and wall-crossing events.
  - Formal model: history-dependent access plus aggregation over context assembly.
  - Optional mechanism baseline: authorization-before-context plus aggregation guard.
  - Venues: security (USENIX Security, CCS, PETS) or ICAIF.
- **Minimum viable evidence.**
  - A synthetic firm: 50–100 clients, 5 advisers, 1 research function.
  - Canaries plus inference probes.
  - Backends × {pre-filter, post-filter, authorization-before-context, physical partition}.
  - Metrics:
    - Violation@n (worst case over tasks);
    - composition-leak rate;
    - over-refusal.
- **Tractability.** High. Barrier salience for an RIA is **medium**: fewer desk walls than a broker-dealer. Cross-client confidentiality is **high** for any adviser. Frame it as "need-to-know across clients", with MNPI as the stress case.
- **Confidence.** High for the finance/barrier absence. Medium for novelty of the composition slice, since IFC theory exists outside memory.

### Adversarial review (reviewer, 2026-09-25)

- **Strongest objection: the generic version is already measured, and industry already ships barrier enforcement for AI.**
  - **PiSAs** (arXiv:2607.05318, full; note written; in the library but not cited in this entry) has a per-attribute *visibility matrix* of who may legitimately see each item. It measures cross-user spillage through shared memory: adding hybrid memory moves violations into memory, with visibility violations of 63–90%, and prompt defences cut only 28–29% of them.
  - GateMem (multi-principal), MemClaw, MAP-Graph (full; ancestry-propagated permission filter, 0% leakage on its synthetic suite) and Governed Memory (arXiv:2603.17787, abstract: "zero cross-entity leakage across 500 adversarial queries", in production) cover cross-principal isolation in shared memory.
  - **AkasicMEM** (arXiv:2609.25563, full; note) §5.3 publishes an evaluation plan almost identical to this benchmark: a synthetic organisation with principals, a timeline of revocations and deletions, leakage against derivation depth, and over-restriction. §5.2 names disclosure "in aggregate" as unsolved. A DB group with its own system is therefore likely to publish first.
  - Industry: Intapp Walls enforced inside Harvey and Copilot (2026), and Harvey names persistent cross-matter agent context as *the* wall risk (`industry.md` addendum). regulation.md T6 ("no… paper addresses information barriers for shared AI memory") holds for *academic evaluation* only, not practice.
- **Importance.**
  - For an RIA, cross-client confidentiality is normally solved by **per-client or household partitioning**. If memory is partitioned, measured leakage is trivially zero and the study is uninteresting.
  - The problem only exists if the firm wants *cross-client shared* memory: house views, research notes, lessons learned across clients. The PI must show that need, or reviewers will ask "why share at all?"
  - MNPI barriers have medium-low salience for an RIA (PI question Q4).
- **Tractability and trust.**
  - Aggregation ground truth ("what can B infer from {x, y}?") judged by an LLM will not be trusted: PiSAs and CI-Work both report judge limits, and GPM's judge gate failed. Canaries catch only verbatim leakage.
  - Inference control has a DB literature (e.g. arXiv:2507.00343 on inference through dependencies, abstract) that reviewers will expect to be engaged.
- **Verdict: survives-narrowed.**
  - Generic cross-user leakage in shared memory is **taken**.
  - What survives:
    1. **history-dependent (Brewer–Nash) access** over a *persistent* store with wall-crossing and cleansing events (MAP-Graph resets per task; PiSAs is scenario-scoped);
    2. **aggregation leakage** from individually authorised items;
    3. a comparison of enforcement points (pre-filter, post-filter, partition, context-assembly guard), which PiSAs explicitly leaves out;
    4. finance semantics.
  - Scoop risk is high (AkasicMEM). Confidence: medium.
- **Suggested sharpening.**
  - Lead with (1) and (2).
  - Make per-client partitioning a mandatory baseline, and report the utility it forfeits. That is the only honest motivation for shared memory.
  - Build *deterministic composition canaries*: a restricted fact Z that follows by a fixed rule from X, held in client A's scope, and Y, held in a shared scope. Leakage is scored by exact recovery of Z, not by a judge.
  - Cite and position against PiSAs and AkasicMEM explicitly.

### GP7. Backend-invariant governance: a portable conformance suite for memory backends
*Merges N5 (backend supply chain and substitutability), G11 (independent replication), N3 (embedder or model migration breaking restrictions) and the promotion-regression slice of N4.*

- **Statement.** Governance properties turn out to depend on the backend, the harness and the read path. No test suite checks whether one governance contract (a gateway above swappable backends) yields the same isolation, revocation, erasure and retention guarantees across backends and across model or embedder migrations.
- **Evidence.**
  - "Memory-backend safety effects reverse across harnesses (Mem0 ±13.5 pp E2E-ASR)" (arXiv:2607.27080, full).
  - "No system enforces revocation at retrieval by default" across Graphiti, Zep, mem0, langmem and cognee (arXiv:2609.08258, full).
  - MemClaw: leakage differs by read path; GET-by-id bypassed scope (arXiv:2606.24535, full).
  - GateMem: Mem0 access-violation 28.1% vs long-context 10.4% (full).
  - Vendor docs: Zep deletion "does not regenerate… summaries"; LangGraph and AgentCore namespace prefix collisions (`industry.md`).
  - Migration: "mixed embedding versions may break retrieval"; compressed notes are model-coupled (arXiv:2609.05339, abstract).
  - Frameworks provide no native memory integrity (arXiv:2606.12797, abstract).
  - The evidence for third-party replication is essentially nil (mechanisms partial §8.8).
- **Assumption challenged.** A governance layer's guarantees are backend-independent; the embedder and model are stationary.
- **What would show the gap is not real.** A published cross-backend conformance or differential-testing suite for governance properties. MemTools (arXiv:2607.21404, abstract) standardises interfaces for research, not governance. Runtime-independent agents (arXiv:2609.00546, abstract) preserve continuity, not restrictions. ForgetEval covers forgetting only, across 13 configurations (full).
- **Why it matters.**
  - DORA concentration and substitutability, and third-party oversight under Reg S-P for RIAs [S].
  - Exit plans.
  - Every firm that treats its memory vendor as swappable.
  - Directly tests the PI's "impossible, not prohibited" architectural thesis.
- **What makes it hard.**
  - Backends expose different primitives: soft vs hard delete, bitemporal vs flat.
  - Equivalence classes of "same guarantee" must be defined.
  - Harness confounds.
- **Anyone on it?**
  - arXiv: MemTools (arXiv:2607.21404), runtime-independent agents (arXiv:2609.00546), memory portability (arXiv:2609.05339). All are utility or continuity, not governance.
  - SciSpace: nothing relevant (privacy frameworks, SEAgent MAC arXiv:2601.11893).
  - **Not scooped.**
- **PI design covers: full (untested).** Nine admission gates each with fixture, oracle, threshold and pinned versions; canaries planted per tenant, barrier and state; a substitution-time metric; re-run triggers. **This is the PI's biggest head start.** The gap is exactly the empirical validation the design lacks.
- **Contribution type.**
  - A conformance suite (open-source harness).
  - A cross-backend empirical study ("same contract, different guarantees").
  - Venues: security or systems (USENIX Security, an SE testing venue, industry tracks), or ICAIF for the finance framing.
- **Minimum viable evidence.**
  - Four OSS backends plus two embedders plus two LLMs.
  - About 30 conformance tests drawn from GP1, GP2 and GP4 (revocation, cross-scope read via every path, physical erasure, restriction survival after re-embedding, consolidation scope).
  - Report a pass/fail matrix and per-cell failure rates with CIs.
  - Laptop plus API.
- **Tractability.** High. The OSS backends run locally. Naming the in-house backend in a paper is a confidentiality decision for the PI.
- **Confidence.** Medium-high. The risk is that reviewers see it as "engineering". Mitigate with a finding-driven framing: how often do guarantees break under swap or migration, and why.

### Adversarial review (reviewer, 2026-09-25)

- **Strongest objection: prior art exists, and the finding may be true by construction.**
  - **(a) A cross-backend study with a backend-agnostic guard already exists** for one property. arXiv:2609.08258 (full note) tests five systems (Graphiti, Zep, mem0, langmem, cognee). It shows none enforces revocation by default and that a store-level filter drives unsafe actions to 0.0% over 1,620 trials. That is "same contract, different backends" for revocation. MemSecBench (arXiv:2607.27080, full) crosses harness × backend × LLM (24 configurations). GPM runs a three-engine differential (full). memorywire (arXiv:2606.01138, abstract) provides a wire format with forget and expire operations over five backend adapters.
  - **(b) Tautology.** If a gateway mediates every read and write, backend invariance holds *by construction* for mediated paths. The only failures left are side channels: backend-internal consolidation, derived summaries, direct APIs, re-index. Enumerating them reads to ML reviewers as engineering and to security reviewers as a pen-test.
  - **(c) Staleness.** Pass/fail matrices for fast-moving OSS versions are out of date by publication.
  - **(d) The PI's head start may not be usable.** The gateway and the in-house backend may not be publishable (Q2, Q8).
- **Importance.** DORA-style substitutability is real. DORA binds only EU financial entities [M]. The PI's deck lists DORA as binding for this entity (INDEX §2), so counsel should confirm whether an EU-regulated affiliate is in scope. For the US RIA itself the hook is Reg S-P service-provider oversight [S], which is weaker. A CCO would value a vendor-assessment checklist, but that is not a research paper.
- **Verdict: weakened.** It survives only as the programme's *infrastructure*, plus one narrow research question.
- **Suggested sharpening.**
  - Centre it on **migration**: do restrictions, erasures and scopes survive an embedder, model or index upgrade, a re-index or a backend swap? No governance-side study exists; arXiv:2609.05339 is utility-only (abstract).
  - Report a **mutation score**: seed known governance bugs into each backend adapter and measure the fraction the suite detects. That gives the conformance suite a falsifiable quality metric instead of a pass/fail table.
  - Include arXiv:2609.08258's guard as an external baseline.

### GP5. The cost of governance: stateless vs governed vs ungoverned memory on finance tasks
*Merges G5 and N2 (the recall loss of authorisation pre-filtering vs post-filtering, and governance latency).*

- **Statement.** Nobody has measured, on finance advisory tasks, what governed memory costs relative to (a) a stateless session design, (b) stateless replay from a governed log, and (c) ungoverned memory. The measurement should cover both sides:
  - the benefit side: task success and suitability;
  - the harm side: false restriction of legitimate client facts, over-refusal, filtered-recall loss, latency, and user-confirmation burden.
- **Evidence.**
  - Price of Safety states its limits: ±4.5 pp resolution, one backbone, no attacks, act-time defences not measured, latency not reported. Its read-time reranker falsely quarantines 33.6% of legitimate memories (arXiv:2609.22818, full).
  - FinPerMA: no memory 18.2–31.2% vs full context 40.1–46.9% (full).
  - DPM matches at moderate budgets but n=10 (full).
  - Ryt: stateless by design (full).
  - TMA-NM: confirmation burden "not measured in a real workflow" (note, full).
  - GateMem: RAG-policy cuts leakage but over-refuses (full).
  - MemGauge: management is the cheapest control point; there is no privacy or cost axis (full).
  - AuthMem-Bench: predicted labels cost no task success (full), but on τ-bench only.
  - Filtered-recall loss is a studied database problem (arXiv:2606.14193, arXiv:2606.16341, abstract). The governance-specific low-selectivity case (one client's slice) is unmeasured for agent memory.
- **Assumption challenged.** Governance is free (vendors), or governance is unaffordable, hence statelessness (regulated deployments).
- **What would show the gap is not real.** A study reporting utility and governance jointly with CIs across stateless, governed and ungoverned conditions in finance. GateMem does the joint score, but in non-finance domains and without a stateless-replay arm.
- **Why it matters.** It adjudicates the PI's central bet against industry practice (review §1.7; INDEX "Where the PI's materials disagree"). A model-risk or compliance function would ask this first.
- **What makes it hard.**
  - Suitability "utility" needs a rubric.
  - Many confounds: token budget, model, harness.
  - Need adequate n. At n=100 the minimum detectable difference is about 18 pp (arXiv:2609.25173, full), so hundreds of episodes per arm are required.
- **Anyone on it?** arXiv: arXiv:2608.21230 (utility under poisoning, abstract), Price of Safety, MemGauge. SciSpace: A-MemGuard, DRIFT and ASB, all attack-centred. **No finance or stateless-comparison study.**
- **PI design covers: full metric design (untested).** A false-restriction-rate counterweight, a p95 governance-latency metric, every ratio paired with governed/ungoverned recall and memory on/off. The claim that utility pairing is novel is not (GateMem does it). The empirical study is novel.
- **Contribution type.**
  - Empirical study, possibly with a reusable harness.
  - Venues: ICAIF or a FinNLP-type workshop; an ML empirical track.
- **Minimum viable evidence.**
  - Extend FinPerMA-style personas (licence unstated; otherwise regenerate synthetically) to about 300 episodes per arm.
  - 5 arms: stateless, log+projection, ungoverned store, governed pre-filter, governed post-filter.
  - 2 API models.
  - Report task success, a suitability-violation rate, false restriction, latency, tokens and $, with bootstrap CIs.
- **Tractability.** High. It is the cheapest decisive pilot.
- **Confidence.** High that the gap exists. Medium that effects will be large enough to be interesting; a null result would still be publishable with the right framing and informative for the PI.

### Adversarial review (reviewer, 2026-09-25)

- **Strongest objection: the result would be gateway-specific, is probably a predictable null, and does not address why industry chose statelessness.**
  - **Prior "no cost" findings.** Several studies already report little or no benign-traffic cost:
    - AuthMem-Bench: predicted labels cost no task success (full);
    - GPM: byte-identical clean-task pools (full);
    - Price of Safety: write-time defences within ±4.5 pp (full).
  - **Where the cost actually appears.** Real cost appears only when a restricted fact is *needed*, which is the intended behaviour. Filtered-recall loss is a known ANN property (arXiv:2606.14193 and arXiv:2606.16341, abstract), and latency is an implementation detail.
  - **Why industry chose statelessness.** Ryt and DPM chose statelessness plausibly because of retention, supervision and erasure burden, not utility (speculation, consistent with notes). A utility comparison therefore does not adjudicate the PI's bet against industry; a compliance-effort comparison would.
- **Trust.**
  - A "suitability" utility score on synthetic advisory tasks needs a rubric and an LLM judge. GPM's LongMemEval judge gate failed (κ 0.07–0.81). Finance practitioners will not accept a judge's suitability call without a validated rubric.
  - At an 18 pp MDE per 100 episodes (arXiv:2609.25173), roughly 5 arms × 2 models × 300 episodes is feasible via API, but it needs a checkpoint-3 budget.
- **Prior work.**
  - GateMem (joint governance and utility, non-finance; full).
  - Price of Safety (full).
  - DPM, stateless (full; n=10).
  - AkasicMEM §5.3, which lists over-restriction against an ungoverned baseline as a planned measure.
  - MAP-Graph, which reports clean-TSR alongside safety (full).
- **Verdict: survives (the gap is real) but weakened on importance and novelty.** It is a supporting arm, not a flagship.
- **Suggested sharpening.**
  - Measure **governance-induced suitability failures**: a legitimately needed, recent client fact that is falsely restricted, stale or scope-blocked leads to an unsuitable recommendation. Score deterministically against a seeded client profile.
  - Make the stateless arm **"stateless replay from the regulated archive"**, which ties it to the reframed GP1.
  - Pre-register equivalence margins (TOST) so that a null result is informative.

### GP4. Cross-layer, certified verification of erasure
*Merges G4 and the resurrection slice of N3 (re-index or embedding migration resurrecting deleted or restricted items).*

- **Statement.** Each residue layer has its own paper; none tests all of them end to end on a real product with a statistical guarantee. The layers are:
  - text-derived tiers (FRS);
  - index topology (Ghost Echoes);
  - storage (Ghost Vectors);
  - runtime state (execution-state unlearning);
  - multimodal (MemLeak);
  - interface (ForgetEval, GateMem).

  Backup restore and re-index or migration are untested.
- **Evidence.**
  - FRS's authors name "probing embedding- and cache-level residue beyond the text surface" as next work and concede low ecological validity (arXiv:2606.10062, full).
  - Ghost Echoes: "primarily one backend"; rebuild does not remove drift (full).
  - GateMem: interface-only forgetting (stated, full).
  - ForgetEval: interface-level, with no storage check (full).
  - Execution-state unlearning: runtime state only (stated, full).
  - Ghost Vectors: storage residue plus epoch-key shredding (abstract).
  - EDPB CEF 2025: backups and "anonymisation as a workaround" [V].
- **Assumption challenged.** API delete equals erasure; a rebuild or re-index is clean.
- **What would show the gap is not real.** A paper combining at least three layers on one system with a confidence bound. None is found yet, but **this is the fastest-moving sub-area** (Chakraborttii group; the FRS authors' stated plan is exactly this extension).
- **Why it matters.** A test "a DPA or auditor would accept" (regulation gap 4). The CCPA and GDPR erasure duties apply if the RIA holds California or EU consumer data (the GLBA data-level carve-out applies to much RIA client data [V/M]).
- **What makes it hard.**
  - Defining residue for paraphrasable facts.
  - Statistical certification needs many trials.
  - Physical-layer access differs by backend.
- **Anyone on it?**
  - arXiv: FRS (arXiv:2606.10062), execution-state unlearning (arXiv:2609.04875), MemLeak (arXiv:2606.29788), OBLIVION (arXiv:2608.08264, cross-surface coherent erasure for *skills*, abstract), ANN in-place deletion (arXiv:2607.29173, abstract).
  - SciSpace: machine-unlearning surveys and patents on deletion verification, all older.
  - **Partially occupied; high scoop risk within about 3 months.**
- **PI design covers: full (untested).** An erasure-propagation control, physical-layer verification, deletion receipt, completeness, time-to-erasure, and recovery-after-restore metrics. Head start on protocol design; no data.
- **Contribution type.**
  - Measurement study plus a protocol, with a hypothesis-test certificate.
  - Venues: privacy/security (PETS, USENIX); a law-and-tech companion on "what counts as erased".
- **Minimum viable evidence.** Across 3 backends and 5 layers (text tier, index, raw file, cache, backup-restore), plus a re-embedding migration: canary and paraphrase probes with a hypothesis test à la Athena (arXiv:2003.04247, in library). Local compute is enough.
- **Tractability.** High technically, and the physical-layer work is laptop-feasible. Strategically risky because of crowding.
- **Confidence.** Medium: the combined gap is real today, but its lifetime is short. It is best used as **one axis of GP7**, not as a standalone paper.

### Adversarial review (reviewer, 2026-09-25)

- **Strongest objection: the area is crowded, and "certified" overclaims.**
  - **MemoRepair** (arXiv:2605.07242, abstract; in the library but **not cited in this entry**) formalises cascade invalidation across summaries, cached outputs, embeddings, skills and tool procedures after deletion or correction. It reports invalidated-memory exposure falling from 69.8–94.3% to 0% given complete influence provenance. That is the "derived tiers" layer end to end.
  - Other occupied layers: SuperLocalMemory 4.0 (arXiv:2608.08253, abstract) claims "verified erasure" under fault injection; FRS (full), Ghost Vectors and Ghost Echoes, execution-state unlearning (full) and OBLIVION (abstract) each hold one layer; arXiv:2507.00343 (abstract) covers inference-aware erasure in databases.
  - "Certified erasure" is not certifiable by sampling probes. The absence of paraphrase residue can only be bounded relative to a probe distribution, and nothing in `regulation.md` suggests a DPA would accept a hypothesis test as proof (speculation).
  - **The novel layers are the least tractable with API-only compute.** Backup/restore and managed-service internals are precisely the layers an API-only project cannot access. On local OSS backends a backup is a file copy, which is trivial to test.
- **Importance.** High for DPAs (EDPB CEF 2025 names backups [V]). For a US-only RIA it is lower unless California or EU persons are in scope (Q1).
- **Verdict: weakened.** Keep it only as an axis of the reframed GP1: purge completeness and **resurrection** via re-ingest, re-index, restore and migration. MemoRepair and FRS do not test resurrection from an archive.
- **Suggested sharpening.**
  - Replace "certified" with "probe-relative detection power (with stated probe family)".
  - Focus on resurrection paths.
  - Use MemoRepair and FRS as baselines rather than competing with them.

### GP6. Memory lineage, recall logging under minimisation, audit-trail attacks and per-record explanation
*Merges G6 and N8 (per-record transparency for automated decisions).*

- **Statement.** Four open problems:
  - there is no validated metric that traces an agent decision back to the memory writes that caused it (source, principal, time, basis) and survives consolidation;
  - there is no method for logging *which memory was recalled* without copying personal data;
  - there is no attack study against memory audit trails;
  - there is no test of whether per-record explanations (ADMT access, UK Art. 22C, Colorado) are faithful.
- **Evidence.**
  - "No metric for memory lineage" (evaluation.md §3).
  - MemLineage: single host, prevention only, fallback "Trusted" (note, full).
  - ReguSim: showing the rationale raises monitor false accepts from 25% to 46.9% (full), so a rationale is not evidence.
  - DEMM-Bench overclaims sufficiency in 75% of cases (abstract).
  - Audit-log integrity: mechanisms exist, but "nobody attacks memory audit trails" (threats §6, synthesis).
  - Regulation T5: no source says how to log recall without copying (full synthesis).
  - New mechanisms that do not validate a metric: ECHO (arXiv:2608.21755, abstract), D²ACCI (arXiv:2608.17756, abstract), LLM audit trails (arXiv:2601.20727, abstract).
- **Assumption challenged.** Logging equals auditability; a trace equals causal lineage.
- **What would show the gap is not real.** A lineage metric validated against counterfactual ablation (does removing the traced memory flip the decision?), or a published audit-log attack on agent memory.
- **Why it matters.**
  - SEC exam production under 204-2 and 17a-4(f)(3) [Vm/M].
  - AI Act Art. 12/19.
  - Colorado explanation duty (note the prudentially regulated FI exemption; an RIA is likely *not* prudentially regulated [M]).
- **What makes it hard.**
  - Ground-truth "influence" needs counterfactual re-runs, which means API cost and hosted-API nondeterminism (arXiv:2608.11344, abstract).
  - Legal explanation standards are vague.
- **Anyone on it?** arXiv: ECHO, D²ACCI, MAP-Graph (retains affected lineage), Token-Flow Firewall (arXiv:2607.08395, abstract). SciSpace: audit trails (arXiv:2601.20727), RAGE, constitution mining (Zenodo). **The lineage metric is weakly occupied; audit-log attacks are open.**
- **PI design covers: full design (untested).** A lineage control, audit trail, version lineage, lineage-coverage and effective-policy-coverage metrics (claimed as new; a lineage-coverage ratio has no published precedent found), an effective-policy hash, and audit-log tampering in the threat matrix.
- **Contribution type.**
  - Metric validation (counterfactual) plus an attack study on audit trails.
  - Venues: security, or FAccT for the explanation part.
- **Minimum viable evidence.** 200 decisions × leave-one-memory-out ablations, which is affordable with small models via API. Two tampering and laundering attacks against a hash-chained log plus consolidation.
- **Tractability.** Medium (API cost of the ablations; nondeterminism).
- **Confidence.** Medium.

### GP3. Scope and authority continuity through consolidation in multi-principal memory
*Merges G8, N9 (epistemic status: remark vs instruction) and N6 (agent identity and confused-deputy writes).*

- **Statement.** Two things are untested:
  - whether client, barrier and purpose scopes survive LLM consolidation in multi-client stores;
  - whether consolidation respects a finance authority lattice: system of record > signed client instruction > client remark > adviser note > agent inference.
- **Evidence.**
  - AuthMem-Bench covers *source* authority for a *single principal* on τ-bench/APIGen (full; 48/49 configurations collapse).
  - MAP-Graph covers propagation of restrictions through derivations, but synthetic and templated, with 9.11% impermissible allows (full).
  - AkasicMEM (abstract) and GPM (abstract) are mechanisms.
  - Confused deputy in multi-agent systems: SEAgent (arXiv:2601.11893, abstract); TMA-NM origin binding (full).
- **Assumption challenged.** One principal per memory; authority equals speaker role.
- **What would show the gap is not real.** Already mostly shown for the generic case. What remains real only if multi-client scope loss under consolidation is non-trivial on real backends.
- **Why it matters.** A tentative client remark ("I might sell") recorded as an instruction is a suitability and trade-authorisation failure.
- **Anyone on it?** AuthMem-Bench, MAP-Graph, AkasicMEM, GPM, Memory Provenance Laundering (arXiv:2607.29167). **Crowded since 2026-08.**
- **PI design covers: full (untested).** Diff-and-approve consolidation, assertion type, an authority-collapse metric, restrictive inheritance, agent identity.
- **Contribution type.** Empirical study. **Best folded into GP2's benchmark as a "consolidation" condition.** Venue: as GP2.
- **Minimum viable evidence.** AuthMem-style paired items with scope labels, on 4 backends.
- **Tractability.** High.
- **Confidence.** Medium that a standalone paper would be judged novel: low-medium.

### GP8. Suitability-consistent memory: staleness against systems of record, and drift vs manipulation
*G10.*

- **Statement.** It is untested whether a persistent advisory memory:
  - stays consistent with authoritative client records (risk profile, restrictions, life events) across sessions;
  - distinguishes genuine preference drift from manipulation.
- **Evidence.**
  - Sell Me This Stock: 95% of suitability violations came from current-turn contamination, *not memory*, and persistence is open (full).
  - FinPerMA: post-shock gap widens from 8.0 to 13.0 pp (full).
  - STALE: premise resistance near zero (full).
  - Stale inherited constraints produce stale-consistent decisions in 74.7–77.3% of episodes (arXiv:2608.25553, abstract).
  - CAPTURE: an adaptive attacker doubles poisoning success (abstract).
- **Assumption challenged.** Recency equals authority; in-conversation updates are the only updates.
- **What would show the gap is not real.** A cross-session suitability benchmark keyed to an external system of record.
- **Anyone on it?** Generic staleness is crowded: STALE, TEPA (arXiv:2608.07429), StateAuditor (arXiv:2608.01619), FAMA, MemConflict. For finance: FinPerMA (utility only) and FinEvo-Bench (arXiv:2608.06144, self-evolving agents with a compliance rubric, abstract). **The finance-persistence angle is open but narrow.**
- **PI design covers: partial.** Source-authority hierarchy, stale-memory-use metric, "recency ≠ authority". Drift vs manipulation only in a single control.
- **Contribution type.** A benchmark module. Venue: ICAIF.
- **Tractability.** High.
- **Confidence.** Medium-low as a standalone; good as a GP1/GP5 task family.

### GP9. Purpose binding and quantified minimisation at write time
*Merges G9, N7 (quantifying "necessary") and G12 (regulation-as-code for memory operations).*

- **Statement.** Two missing pieces:
  - no operational, testable definition of "necessary" for a memory write, e.g. counterfactual utility over a purpose-specific task distribution;
  - no evaluated mechanism that enforces purpose tags at recall "without delegating legal interpretation to the model".
- **Evidence.**
  - Policy representation (purpose, recipient, consent) is listed as open (arXiv:2606.26627; mechanisms partial §5).
  - The HIPAA framework is toy-scale with no persistent memory (full).
  - Over 95% of ChatGPT profile entries are implicitly extracted (arXiv:2609.14697, abstract).
  - Key-fact summarisation cuts extraction 64–76% with little utility loss (arXiv:2606.10062, full). That is effectively a minimisation result, but it is not framed legally.
  - Minimisation has been operationalised for prompts (arXiv:2510.03662, abstract) and recommender systems (arXiv:2005.13718, abstract), not for agent memory.
  - Memory Worth is associational only (arXiv:2604.12007, abstract).
  - Regulation-as-code targets rule text (arXiv:2609.20016, abstract; doi:10.1093/ojls/gqad014 on the limits).
- **Assumption challenged.** Store everything and filter later; "relevance" stands in for "necessity".
- **What would show the gap is not real.** An agent-memory paper that defines and measures necessity against a stated purpose. SP-Mem (arXiv:2608.16551, abstract) separates PII values but does not define necessity.
- **PI design covers: partial.** Purpose binding and purpose-bound use controls, a purpose-violation metric, and the PI's own margin question (risk tiering). The claim that the purpose-violation metric has no precedent is disputed (CI violation metrics).
- **Contribution type.**
  - A formal model plus a mechanism ("governed write policy").
  - Venues: law and tech, or FAccT; ML if the mechanism is strong.
- **Tractability.** Medium. The legal definition is contested, so it needs a legal co-author for credibility.
- **Confidence.** Low-medium.

---

## 3. Killed or merged candidates (with reasons)

| Candidate | Verdict | Reason |
|---|---|---|
| **G3** No finance memory evaluation | **Merged** as the *setting* of GP1/GP2/GP5/GP8 | True (high evidence), but it is a domain, not a research question. A generic "finance memory benchmark" is marginal with 5 lifecycle benchmarks in 3 months (threats §8.9). Finance *obligations* are the differentiator. |
| **G7** Record classification | **Merged** into GP1 (legal analysis) | Primarily a legal question with no technical experiment. Counsel must answer it before GP1's labels are final. |
| **G11** Evidence quality / replication | **Merged** into GP7 and all study designs as a requirement | A methodological standard, not a gap to own. |
| **G12** Regulation-as-code | **Merged** into GP9 | Weak evidence (abstract-level); overlaps purpose binding. |
| **N1** Aggregation leakage | **Merged** into GP2 | Same benchmark; it is GP2's most novel slice. |
| **N2** Pre- vs post-filter recall loss | **Merged** into GP5 as one arm | The mechanism is well studied in filtered-ANN research (arXiv:2606.14193, arXiv:2606.16341). Only the governance framing is new, which is an engineering measurement, not a paper. |
| **N3** Embedding migration breaks restrictions | **Merged** into GP7 (restriction survival) and GP4 (resurrection) | Plausible, but mostly an implementation bug class. Metadata filters do not depend on embeddings. The real risk is re-index pipelines that drop metadata or re-ingest deleted sources, which is a conformance test. Utility-side migration is covered by arXiv:2609.05339 (abstract). |
| **N4** Memory → skill promotion governance | **Killed** as standalone; one promotion-regression test kept in GP7 | Mechanisms exist: SR-Fraud's Wilson-bounded rule admission (full), ASG-SI verifier-backed skill promotion (arXiv:2512.23760, abstract), OBLIVION skill revocation (arXiv:2608.08264, abstract), a skills lifecycle/security SoK (arXiv:2608.29596, abstract). Low salience for RIA advisory workflows. |
| **N5** Backend supply chain / substitutability | **Promoted** into GP7 | Reframed from a risk-register item into a testable conformance question. The CVE side is operational security, not research. |
| **N6** Agent identity / confused deputy | **Merged** into GP3 | Confused deputy in multi-agent LLM systems is studied (SEAgent arXiv:2601.11893, abstract); origin binding (TMA-NM, full). |
| **N7** Quantifying minimisation | **Merged** into GP9 | Same research object. |
| **N8** Per-record transparency | **Merged** into GP6 | Explanation presupposes lineage. |
| **N9** Epistemic status (remark vs instruction) | **Merged** into GP3, largely **pre-empted** | AuthMem-Bench already separates user statement, assistant suggestion, third-party report and standing rule (full). The finance lattice is a thin delta. |
| RL-learned memory managers under governance | **Killed** | API-only compute cannot train them; single-facet; weak evidence. |
| SAR/AML memory | **Killed** for this PI | Bank/BD-centred. RIA AML programme obligations have uncertain timing [M]. No usable data. |
| Parametric/pretrained knowledge in scope (PI margin question) | **Killed** as a gap; recommend explicit scope-out | Out of the brief's scope. Unlearning of weights is a separate, crowded field (arXiv:2412.06966). |
| US model-risk vacuum; 2027 timeline cluster | **Killed** as research gaps | Context for motivation sections, not research questions. |
| Storage ≠ execution; tail metrics | **Merged** into study-design requirements | Methodological. |

---

## 4. Ranked top 5 and reasoning

The ranking weighs:
- (a) evidence strength from full text or notes;
- (b) novelty against the literature *and* the risk of being scooped;
- (c) the PI's head start;
- (d) RIA relevance and API-only tractability;
- (e) whether it yields a clean empirical contribution credible to both ML and finance audiences (brief).

| Rank | Gap | Why here | Confidence |
|---|---|---|---|
| **1** | **GP1 Joint retention and erasure** | The only gap flagged by all five scouts. Absence is confirmed again in 2026-06+ arXiv. It is directly RIA-relevant (204-2 plus EU clients), and it exposes a blind spot in the PI's own design (17(3)(b)). It rests on full-text limitation evidence (AuthMem-Bench 139/350 retention; GateMem; SSGM; FRS). Risk: GPM (arXiv:2608.12476) must be read in full first. | High (gap) / med (payoff) |
| **2** | **GP2 Cross-client need-to-know, barriers and composition** | Strong full-text evidence and high novelty for the finance framing. Composition is a genuinely under-protected risk per a 2026 survey. For an RIA, frame it as cross-client confidentiality, with MNPI as the stress case. | High / med |
| **3** | **GP7 Backend-invariant conformance** | Largest PI head start (full design, untested). Strong full-text evidence of backend and read-path dependence. Not scooped. It is also the vehicle that makes GP1, GP2 and GP4 reusable. | Med-high |
| **4** | **GP5 Cost of governance** | Cheapest decisive experiment. It adjudicates the PI's core bet against industry statelessness and rests on stated limitations in Price of Safety. Novelty is medium (partial precedents), so on its own it is a solid empirical paper rather than a flagship. | High (gap) / med (novelty) |
| **5** | **GP4 Cross-layer certified erasure** | Real today, with named next steps in FRS's own conclusion and a strong PI head start. But it is the fastest-moving sub-area, so scoop risk is high. It is ranked in the top 5 **as a component**, not a standalone paper. | Med |

Just below the cut: GP6 (lineage/audit; medium tractability because counterfactual ablations are costly), then GP3 (largely pre-empted), GP8 and GP9.

**Evidence basis check (top 5 must rest on full text or notes).** GP1, GP2, GP7, GP5 and GP4 each cite at least two stated limitations or measured absences from full-text reads or project notes (listed in their entries). None of the top 5 relies on abstract-only evidence for its core claim.

### How the gaps combine into one research programme

**One benchmark plus a conformance harness that also evaluates a mechanism.** Working name (generic, public-safe): *a governance conformance benchmark for agent memory under adviser obligations*.
1. **Environment.** A synthetic multi-client advisory firm:
   - clients in US and EU jurisdiction scenarios;
   - advisers, a research function, a compliance function;
   - dated events: erasure requests, legal holds, retention expiry, wall-crossings, risk-profile updates, model/embedder upgrades.
   - Every item carries labels: record class, retention period, scope, barrier, purpose, authority.
2. **Task families.**
   - T1 retain/erase joint (GP1);
   - T2 cross-client, barrier and composition leakage (GP2, plus GP3 consolidation conditions);
   - T3 physical and derived erasure incl. restore and migration (GP4);
   - T4 suitability consistency (GP8, optional).
3. **Conditions.**
   - Backends: Mem0, Graphiti, Letta, LangGraph store.
   - Governance: none / vendor-native / a reference governance gateway.
   - Stateless baselines: session-only, and log-plus-projection (DPM-style).

   Together these answer GP7 (does the same gateway yield the same guarantees on every backend?) and GP5 (what does it cost?).
4. **Metrics.** Every governance ratio is paired with a utility or over-restriction counterweight. Use worst-case-over-n (Violation@n), bootstrap CIs, and deterministic oracles where possible (canaries, state checks) rather than LLM judges.
5. **Mechanism evaluated by the benchmark.** A retention-aware, scope-preserving gateway: record-class-aware erasure (tombstone or crypto-shred in the operational tier; restricted archive for mandated records), authorisation-before-context, and scope inheritance through consolidation. The benchmark's value is showing where vendor-native controls fail and what the gateway fixes at what cost. **Whether to publish a generic version of the PI's gateway is the PI's confidentiality decision** (question Q2).
6. **Staging.**
   - **Pilot** (smallest decisive experiment): GP1 T1 plus GP7 on 2 backends × {native, gateway}, about 50 histories. If vendor-native backends already handle retention-vs-erasure correctly (unlikely given arXiv:2609.08258), GP1 collapses. That is a clean kill test.
   - **Then:** GP2 plus GP5 arms.
   - **Last:** GP4 layers.
   - The programme can yield 2–3 papers: a benchmark and conformance paper (ML D&B or security); an empirical cost study (ICAIF); a legal-technical companion on cross-border retention vs erasure (law and tech).

---

## 5. Open questions for the PI (answers that would change the ranking)

1. **EU data subjects.** Will the entity's memory stores hold data on EU (or UK or California) persons?
   - If none, GP1's cross-border half drops. GP1 stays a 204-2 retention-vs-client-deletion-request problem, which is weaker, and GP2 or GP7 may move to #1.
2. **Publishing the architecture.** May a generic, de-branded version of the gateway design appear in a paper or open-source harness?
   - If no, GP7 must be framed as a design-agnostic conformance suite and the mechanism arm drops. GP5 and GP1 rise.
3. **Pilot traces.** Is internal pilot data (the planned internal workflow pilot) realistically approvable within the project timeline, even as aggregate statistics?
   - If yes, GP6 (lineage validation) and GP5 gain real-trace credibility and move up.
4. **MNPI and barriers.** Does the entity actually operate barriers (e.g. access to issuer MNPI via clients, private markets, expert networks), or only client confidentiality?
   - This decides whether GP2 leads with "barriers" or "cross-client need-to-know".
5. **Counsel.** Can counsel confirm, before labels are frozen:
   - which memory-item classes are 204-2 records;
   - the 17(3)(b) reading for US retention of EU persons' data;
   - the status of the SEC 204-2 modernisation?

   GP1's construct validity depends on this.
6. **Venue preference.**
   - ML benchmark track or security: favours GP7 and GP2.
   - FinTech/ICAIF: favours GP5 and GP1.
   - Law and tech: favours GP1's legal half and GP9.
7. **Mechanism vs measurement appetite.** Does the PI want a mechanism paper (favours GP9 or a GP1 gateway) or a measurement/benchmark paper (favours GP1, GP2, GP7)?
8. **Backends in scope.** Can the in-house backend be tested (unnamed) alongside the OSS backends? That strengthens GP7's external validity.

### Newly found prior work that threatens novelty (read before `/ideate`)

- **arXiv:2608.12476 (GPM, 2026-08-12).** Bitemporal governed memory with "non-revival after retraction or deletion" and a 3,600-case release benchmark. Threatens GP1 and GP3. **Abstract only; HTML unavailable. Read the PDF.**
- **arXiv:2608.01679 (AuthMem-Bench).** Pre-empts N9 and the generic G8. Leaves scope continuity and the retain-side loss.
- **arXiv:2606.10062 (FRS).** Closest precedent for derived-tier erasure (GP4) and for the PI's erasure-completeness metric. Its authors plan the embedding/cache extension.
- **arXiv:2608.10509 (MAP-Graph)** and **arXiv:2609.25563 (AkasicMEM).** Restriction propagation through derivation (GP3).
- **arXiv:2609.14976 (MemRiskBench).** Cross-user leakage, revoked-memory reuse and constraint decay in one scripted benchmark. Raises the bar for any generic risk benchmark; finance obligations and retention are absent.
- **arXiv:2607.03510 (CAGE-1).** An enterprise agent governance-evaluation framework (abstract). Check whether it operationalises memory validity and replay.
- **arXiv:2609.05339 (memory portability across model upgrades).** Utility side of migration; relevant to GP7.

---

## Adversarial review of the combined programme

*Reviewer, 2026-09-25. Idea-critique mode, so no scores. Full-text reads this pass: GPM, MemRiskBench, CAGE-1, MAP-Graph, AkasicMEM and PiSAs (notes written). Six records were added with `--tag gaps-check`: arXiv:2607.05844, arXiv:2606.06240, arXiv:2507.00343, arXiv:1910.13784, arXiv:2601.06627, arXiv:2609.06543. Seven existing records were re-tagged. Industry findings are appended to `industry.md`. No confidential content was used in any search.*

### Fatal or near-fatal flaws

1. **The flagship's legal premise may dissolve** (see GP1 review).
   - Evidence that agent memory items are 204-2 records is [M]/[S] only; no official text classifies agent memory.
   - Industry practice for RIAs is "archive the communication, treat AI output as derived".
   - If counsel confirms that memory is a derivative, the "keep what you must" half of T1 has no legal ground truth for most items, and the benchmark's "compliance" labels become the authors' assertions.
   - *Preempt:* get counsel's answers (GP1 review, items 1–5) **before** designing labels. Reframe T1 as lineage-complete purgeable memory, with sole-carrier detection as the only must-retain obligation inside memory.
2. **Self-evaluation circularity.**
   - The benchmark, its labels and the reference gateway would all come from the same control catalogue, so the gateway will pass by construction.
   - This is the main weakness of GPM (a self-designed 3,600-case suite with a 100% pass), and reviewers will say the same here.
   - *Preempt:*
     - external baselines: arXiv:2609.08258's guard, MAP-Graph's released design, the GPM artifact (PolyForm Noncommercial; check the licence);
     - test families authored by someone outside the gateway design (e.g. compliance staff);
     - mutation testing of the suite;
     - report the gateway's failures, not only its passes.
3. **The pilot kill test is not a kill test.**
   - §4 says GP1 collapses if vendor-native backends "already handle retention-vs-erasure correctly". But no OSS backend has any notion of a record class or retention period, so they will fail by definition.
   - That is a straw man guaranteed to "succeed".
   - *Replace with:* a naive "memory = cache over archive, purge by lineage id" baseline. If it passes T1 on two backends, GP1 is an engineering checklist and the programme should pivot to GP2's aggregation and history-dependence slice.
4. **Crowding and timing.**
   - Five lifecycle benchmarks appeared in three months.
   - AkasicMEM §5.3 publishes nearly the same evaluation design (a synthetic organisation, governance-event timeline, leakage vs derivation depth, over-restriction).
   - A fintech lab (MemRiskBench) is active.
   - The realistic window is about three months. A four-family × four-backend × three-governance × two-stateless × migration matrix cannot ship in that window.
   - *Preempt:* one sharp paper first.

### Likely ML-reviewer objections, and how to preempt them

- **"Synthetic, templated, self-labelled; measures conformance to your own spec."**
  - Use deterministic oracles (canaries, lineage ids, state checks) where possible.
  - Where a judge is unavoidable (paraphrase, aggregation, suitability), pre-register a judge-agreement gate against human labels (κ ≥ 0.8, as GPM did) and report its failure honestly.
  - Release generators and seeds.
- **"OSS backends at toy scale; known failures (Mem0 leaks, revocation ignored) are already published."**
  - Cite GateMem, arXiv:2609.08258 and MemSecBench, and do not re-report their findings.
  - Contribute the untested axes: persistence across sessions, migration or re-index resurrection, history-dependent access, aggregation.
  - Scale the store to firm-like sizes (10^4–10^5 items across hundreds of clients).
- **"Benchmark of everything."** Pick one question per paper and state the falsifiable hypothesis up front.
- **"Single run, small n."** Budget for the 18 pp MDE per 100 episodes (arXiv:2609.25173), use Violation@n with bootstrap CIs, and run at least two LLM families.

### Likely finance-practitioner objections, and how to preempt them

- **"We already archive everything (Smarsh or Global Relay; Purview for Copilot) and partition memory by client. What does this tell me?"**
  - Show a failure the archive-plus-partition architecture does *not* catch: resurrection on re-index, sole-carrier records, cross-client leakage through firm-level shared notes, aggregation.
  - If you cannot, the programme has no practitioner audience.
- **"The SEC examines records, not memory."** Put the legal-classification analysis (counsel-reviewed) first, and scope claims to the record classes counsel confirms.
- **"The EU scenario is irrelevant to a US RIA with no EU clients."** Answer Q1 before building jurisdiction scenarios. Otherwise, drop them.
- **"Walls are a vendor feature now (Intapp in Harvey and Copilot)."** Position the work as the first *evaluation* of such enforcement for persistent agent memory, not as a new mechanism.
- **"Synthetic RIA histories don't look like our CRM notes, meeting summaries and emails."**
  - Have compliance staff review the scenario templates.
  - If the pilot is approved (Q3), validate that a small number of *aggregate* statistics (e.g. memory items per client, share derived from archived sources) match the synthetic generator.

### Recommended re-scoping (reviewer's view; the PI decides)

- **Paper 1 (pilot-sized, decisive).** *Is agent memory a purgeable derivative of the regulated archive?* This merges reframed GP1, GP4 resurrection and GP5's stateless-replay-from-archive arm. It runs on two to three backends, with native vs lineage-bound purge vs stateless replay. Metrics:
  - archive coverage;
  - sole-carrier rate;
  - purge completeness across derived tiers;
  - resurrection after re-index or restore;
  - utility and latency vs stateless replay.
- **Paper 2.** *History-dependent access and aggregation leakage in persistent shared advisory memory* (narrowed GP2). Per-client partitioning is the mandatory baseline, the scoring uses deterministic composition canaries, and it is explicitly positioned against PiSAs and AkasicMEM.
- **Infrastructure (not a standalone paper unless migration results are striking).** GP7's conformance harness with a mutation score.

**Bottom line.**
- None of the top five is killed.
- GP1 and GP2 survive only in narrowed forms.
- GP7 and GP4 are weakened to components.
- GP5 survives as a supporting arm.
- The single biggest threat is **construct validity of "compliance"**: legal labels that counsel may not endorse, evaluated on a benchmark authored by the mechanism's designers.

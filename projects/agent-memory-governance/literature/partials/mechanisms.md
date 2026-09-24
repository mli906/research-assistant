# Partial review: memory mechanisms and architectures (facet tag `mechanisms`)

Scout: lit-scout (mechanisms facet). Date: 2026-09-24. Library: `literature/papers.jsonl`. 174 records carry the `mechanisms` tag. 14 of them were read closely by this scout and tagged `core`. Another 10 mechanisms-tagged records are `core` for other scouts. Notes for the core papers are in `literature/notes/arXiv_<id>.md`.
Recency cutoffs: arXiv searched 2025-06-01 → 2026-09-24; SciSpace (index lag of months; newest hit 2026-01); OpenAlex most-cited (any date); S2 forward citations (2026-09-24); web and product docs accessed 2026-09-24.
Reading depth: "full text" means the arXiv HTML was retrieved and read with WebFetch-assisted extraction of method, results and limitations, not a line-by-line reading. Anything else is marked *(abstract only)*.

---

## 1. Query plan (reusable by `/radar`)

| Facet | Queries (arXiv boolean unless stated) |
|---|---|
| Surveys / taxonomy | `("agent memory" OR "memory mechanism") AND (survey OR taxonomy) AND LLM`; SciSpace: "How do LLM agents manage long-term memory, including episodic, semantic and procedural memory, consolidation and forgetting?" |
| Architectures | `("long-term memory" OR "episodic memory" OR "procedural memory") AND "LLM agent"`; `(MemGPT OR "memory management" OR "memory consolidation" OR "hierarchical memory") AND (LLM OR agent)` |
| Graph / temporal memory | `("graph memory" OR "temporal knowledge graph" OR "memory graph") AND agent` |
| Parametric / KV / memory-OS | `("parametric memory" OR "KV cache memory" OR "memory layer" OR "memory operating system")` |
| Shared / multi-agent / multi-user | `("shared memory" OR "multi-agent memory" OR "multi-user memory" OR "collaborative memory") AND LLM` |
| Forgetting / deletion / unlearning | `(forgetting OR deletion OR unlearning OR erasure) AND ("agent memory" OR RAG OR "vector database")`; `("machine unlearning" OR "right to be forgotten" OR "right to erasure") AND (RAG OR retrieval OR "agent memory" OR vector)`; SciSpace: "How can data be deleted or unlearned from RAG systems and vector databases to satisfy the right to erasure?" |
| Access control / tenancy | `("access control" OR permission OR tenant OR isolation) AND ("agent memory" OR RAG)`; SciSpace: "What access control and multi-tenant isolation mechanisms protect RAG and agent memory from cross-user leakage?" |
| Provenance / audit | `(provenance OR lineage OR "audit log" OR auditability) AND ("agent memory" OR "LLM agent" OR RAG)`; SciSpace: "How can provenance, audit logging and integrity verification be implemented for persistent memory of LLM agents?" |
| Integrity / versioning | `(integrity OR "authorized mutation" OR versioning OR rollback OR signed) AND "agent memory"` |
| Privacy-preserving memory | `("privacy-preserving" OR "differential privacy" OR encryption OR redaction) AND memory AND LLM agent`; SciSpace DP/encryption/redaction question |
| Consent / purpose / CI | `("purpose limitation" OR consent OR "contextual integrity" OR "information barrier") AND (memory OR agent) AND LLM` |
| Conflict / staleness | `("knowledge conflict" OR staleness OR "memory update" OR outdated) AND ("agent memory" OR "long-term memory")`; SciSpace staleness question |
| Foundations | OpenAlex `--sort cited`: "memory large language model agent", "machine unlearning survey", "retrieval augmented generation privacy", "vector database management system survey" |
| Snowball | `lit.py cites` on arXiv:2505.18279 (Collaborative Memory) and arXiv:2606.18497 (Ghost Vectors) |

The query "information barrier" returned nothing relevant on arXiv (see Gaps).

---

## 2. Taxonomy

Two axes: the **memory mechanism** (how memory is represented and evolves) and the **governance operation** applied to it. The mechanism axis follows arXiv:2512.13564 (forms/functions/dynamics) and arXiv:2505.00675 (six operations). The governance axis is our synthesis.

### 2a. Mechanism axis
- **Forms:** token-level text/records (flat stores, e.g., Mem0 arXiv:2504.19413); graph/temporal-KG (Zep/Graphiti arXiv:2501.13956, HippoRAG arXiv:2405.14831, A-MEM arXiv:2502.12110, SGMem arXiv:2509.21212, graph-memory survey arXiv:2602.05665); hierarchical/tiered OS-style (MemGPT arXiv:2310.08560, MemOS arXiv:2507.03724, H-MEM arXiv:2507.22925, TiMem arXiv:2601.02845, EverMemOS arXiv:2601.02163); parametric/latent (MemoryLLM arXiv:2402.04624, RPMem arXiv:2609.23466, parametric memory scaling arXiv:2606.04536); KV-cache memory (arXiv:2603.04428, BIO-MEMART arXiv:2609.08566); filesystem memory (arXiv:2607.26637).
- **Functions:** factual/user profile; experiential/episodic (Generative Agents arXiv:2304.03442, Reflexion arXiv:2303.11366); procedural/skills (Voyager arXiv:2305.16291, arXiv:2606.23127, arXiv:2512.18950, arXiv:2512.10696); working memory.
- **Dynamics:** formation/extraction (ProMem arXiv:2601.04463); consolidation and reflection (sleep-time compute arXiv:2504.13171, TRUSTMEM arXiv:2606.25161, reconsolidation arXiv:2609.16053); learned memory management by RL (Memory-R1 arXiv:2508.19828, AgeMem arXiv:2601.01885, DeltaMem arXiv:2604.01560); forgetting for efficiency (FadeMem arXiv:2601.18642, FSFM arXiv:2604.20300, rate-distortion view arXiv:2607.08032); retrieval.
- **Topology:** single-user; multi-agent shared (MIRIX arXiv:2507.07957, arXiv:2603.10062 computer-architecture view, INMS arXiv:2404.09982); multi-user/multi-principal (Collaborative Memory arXiv:2505.18279, AIM arXiv:2609.12320, GateMem arXiv:2606.18829).

### 2b. Governance-operation axis (what regulated deployments need)
| Operation | Mechanism families found | Representative ids |
|---|---|---|
| **Scope-read** (tenancy, need-to-know, information barriers) | namespace/tenant partitioning; ABAC/RBAC read gates; time-varying permission graphs; "all participants" rule; audience-before-context | arXiv:2505.18279, arXiv:2509.14608, arXiv:2608.17148, arXiv:2606.24535, arXiv:2609.12320, arXiv:2609.25563 *(abstract only)*, doi:10.5281/zenodo.18346036 *(abstract only)* |
| **Authorise-write / commit** | write gates (NLI consistency), transactional belief commit, human-in-the-loop write review, signed authorised mutation | arXiv:2603.11768, arXiv:2607.23929, arXiv:2608.02843 & arXiv:2609.01235 *(abstract only)*, arXiv:2606.01138 *(abstract only)* |
| **Provenance / lineage** | immutable per-fragment provenance; derivation DAG with trust propagation; evidence-before-belief stores; provenance firewall | arXiv:2605.14421, arXiv:2607.29167 *(abstract only)*, arXiv:2605.30771 *(abstract only)*, arXiv:2608.29606 *(abstract only)* |
| **Erase / forget-with-derivatives** | API delete; crypto-shredding of vectors; traversal-safe ANN deletion; execution-state unlearning (replay); semantic deletion hooks; machine unlearning | arXiv:2606.18497, arXiv:2609.19456 *(abstract only)*, arXiv:2609.04875, arXiv:2606.15903, arXiv:2606.29788 *(abstract only)*, arXiv:2608.20352 *(abstract only)*, arXiv:1912.03817, doi:10.1145/3603620 |
| **Retain / expire** | TTL/decay (Weibull, exponential); store-level default TTL; event expiry | arXiv:2603.11768, arXiv:2601.18642, arXiv:2512.12856 *(abstract only)*; industry table §6 |
| **Version / rollback** | commit-on-write snapshots with semantic rollback; git-backed memory; AGM belief-revision graph with immutable revisions | arXiv:2607.27773, arXiv:2606.14470 *(abstract only)*, arXiv:2603.17244 *(abstract only)* |
| **Integrity / attest** | Ed25519 signing, Merkle logs (RFC 6962), hash-chained audit trails, signed deletion proofs | arXiv:2605.14421, arXiv:2608.02843, doi:10.3390/electronics15010056 *(abstract only)*, arXiv:2601.20727 *(abstract only)* |
| **Conflict / staleness resolution** | temporal supersession, bi-temporal edges, revocation of stale memories, dependency-scoped plan validation | arXiv:2501.13956, arXiv:2606.24535, arXiv:2608.07429, arXiv:2609.03340, arXiv:2605.06527 (all abstract only except arXiv:2606.24535) |
| **Privacy transforms** | edge-side placeholder redaction; inference-leakage budgets; IFC; privacy-aware remember/reveal | arXiv:2605.09530, arXiv:2606.12341, arXiv:2608.16551 (abstract only); survey arXiv:2606.26627 |
| **Data-model framing** | memory as a governed evolving state (trajectory correctness) | arXiv:2605.26252 |

---

## 3. Comparison table (core and closely related)

| id | Mechanism | Data / setting | Metric | Key result |
|---|---|---|---|---|
| arXiv:2505.18279 | Private/shared tiers; bipartite time-varying ACL graphs; immutable provenance per fragment | MultiHop-RAG (2,556 q), synthetic business (200 q), SciQAG (100 q) | accuracy, resource calls | −59–61% resource calls at 75% overlap, accuracy ~0.90; no adversarial leakage test |
| arXiv:2606.24535 | Scoped retrieval, supersession, provenance, propagation (production MemClaw) | ArgusFleet: 192 leakage probes, 200 contradictions, 50 chains | leak rate, detection, chain recovery | provenance 50/50; search-path leak 72/164; GET-by-id bypassed sub-tenant scope; contradiction detection 49% |
| arXiv:2606.18829 | Benchmark for multi-principal memory governance | 91 episodes, 2,218 checkpoints, 4 domains | MGS = U(1−A)(1−F) | GPT-5.4 medical: long-context MGS 80.1% vs Mem0 25.8% (A = 28.1%) |
| arXiv:2509.14608 | "All-participants" access rule; biclique selection for fine-tuning | case studies; deployed in Copilot Tuning | none | no quantitative evaluation |
| arXiv:2606.18497 | Storage-layer analysis of soft delete; Epoch Key Rotation | Chroma, FAISS, Weaviate; BLP, Synthea, LFW | reconstruction rate | names 25.5%, age/gender 100%, faces 99.17% from deleted vectors; EKR gives 0% at 2.5 ms/500 deletes |
| arXiv:2609.04875 | Execution-state unlearning via provenance-guided selective replay | LongMemEval, ToolSandbox, AgentDojo; 3 open 7–8B models | Leak@probes, CAD, recomputed tokens | memory-delete leaves leakage 0.86–1.00; replay 0.00 at 9.3× fewer tokens than reset |
| arXiv:2606.15903 | Placement of an LLM in the forgetting control plane | ForgetEval 1,000 + 385 adversarial; 13 configs incl. Mem0, Letta, LangGraph, Graphiti, A-MEM | pass rate | deterministic 63–68%; mutation-time LLM hook 91.7–94.2% at 2.3 s/case |
| arXiv:2605.14421 | Signed entries + Merkle log + derivation DAG + action gate | deterministic harness (3 poisoning workloads); AgentDojo bridge | ASR, overhead | ASR 0/0/0 vs signatures-only 0/1/1; sub-ms overhead |
| arXiv:2607.23929 | Transactional belief commit, action gating, cascade repair | 90 + 56 case suites; refund pipeline; 5 backbones | success, downstream harm | 0.756–0.956; only method with zero harm on all backbones |
| arXiv:2607.27773 | Commit-on-write snapshots, NL semantic rollback | LoCoMo, MemoryAgentBench | version Recall@1, rollback QA | R@1 12.0→20.5% (LoCoMo), 24.3→39.4% (MAB) |
| arXiv:2605.26252 | GEM: state-level operators and 6 correctness conditions; MemState | prototype only | none | no record-level system satisfies GEM (argument) |
| arXiv:2603.11768 | SSGM write gate / decay / read gate / immutable log | none | none | conceptual; bounded-drift theorem |
| arXiv:2609.12320 *(abstract only)* | Private/public classification + index-level ACL | MUMBench (4 domains) | visibility acc., op accuracy | 96.0% visibility, 58.8% strict op accuracy |
| arXiv:2608.02843 *(abstract only)* | Signed, authorised weight mutation with no-fork chain | LongMemEval, LoCoMo, PoisonedRAG N=100 | accuracy, poison disclosure | 91.8% LongMemEval; 0/100 poison in top-5; 4.9 ms per signed transition |
| arXiv:2606.29788 *(abstract only)* | Information Provenance Graph for deletion affordance | multimodal memory | residual recovery | text-deleted facts recovered 18.3% via correlated text, 12.0% via images; semantic deletion → 2.0% |

---

## 4. Frontier: what changed in the last 12 months (2025-09 → 2026-09)

1. **Forgetting moved from an efficiency trick to a correctness and compliance property.** Three separate lines show that "delete the record" is not erasure:
   - residue in storage: arXiv:2606.18497; traversal-time scoring of deleted vectors in arXiv:2609.19456 *(abstract only)*;
   - residual retrieval drift after correct deletion: arXiv:2608.20352 *(abstract only)*;
   - residue in derived runtime state (summaries, KV cache, plans): arXiv:2609.04875; in images: arXiv:2606.29788.
   The first cross-product forgetting benchmark appeared (arXiv:2606.15903).
2. **Multi-principal memory governance became a named problem**, with benchmarks (GateMem arXiv:2606.18829, MUMBench in arXiv:2609.12320, CI-Work arXiv:2604.21308, PiSAs arXiv:2607.05318) and mechanisms: audience-before-context (arXiv:2608.17148), authorization continuity across derivations (AkasicMEM arXiv:2609.25563, 2026-09-22, abstract only), Harness-MU (arXiv:2606.21856).
3. **Cryptographic provenance and integrity for memory**: signed, Merkle-logged entries (arXiv:2605.14421), authorised mutation with portable verification (arXiv:2608.02843, arXiv:2609.01235), non-malleable origin-bound authority (arXiv:2606.24322). These mostly come from the poisoning-defence community, not from compliance.
4. **Database and transaction semantics** entered agent memory: GEM (arXiv:2605.26252), MemTX (arXiv:2607.23929), ChronoMem versioning (arXiv:2607.27773), GitOfThoughts (arXiv:2606.14470), AGM belief revision (arXiv:2603.17244), and a vendor-neutral wire format with an HITL governance channel (arXiv:2606.01138).
5. **Production evidence** is starting to appear: MemClaw's negative results (arXiv:2606.24535), plus the Microsoft participant-aware rule shipped in Copilot Tuning (arXiv:2509.14608).
6. On the mechanism side, **RL-learned memory management** (arXiv:2508.19828, arXiv:2601.01885, arXiv:2604.01560) and **parametric/KV memory** (arXiv:2609.23466, arXiv:2603.04428) grew quickly. Both make erasure and audit harder, and the governance papers above do not yet cover them.

## 5. Open problems stated by the authors themselves
- Trustworthy memory is listed as a future direction, with no concrete agenda (arXiv:2512.13564).
- Latency–safety and stability–plasticity trade-offs of write and read gates (arXiv:2603.11768).
- Dynamic ACLs, ACL misconfiguration, and fine-grained ACLs that leave no authorised user (arXiv:2509.14608); concurrency and rapid role churn (arXiv:2505.18279).
- Cross-tenant evaluation, independent replication, and pipeline-ordering conflicts between dedup and contradiction handling (arXiv:2606.24535).
- Erasure scope: no guarantee for model weights or committed external side effects (arXiv:2609.04875); forward secrecy and scale up to 10^7–10^10 vectors (arXiv:2606.18497); interface-level vs certified physical forgetting (arXiv:2606.18829).
- Branching histories, concurrency, and realistic rollback intents (arXiv:2607.27773).
- Only declared provenance is protected, so undocumented derivations escape repair (arXiv:2607.23929); prevention without recovery, single host (arXiv:2605.14421).
- Native engines for governed memory; privacy under retrieval-induced state change; verifiable erasure (arXiv:2605.26252).
- Policy representation (purpose, recipient, consent); deletion across caches and derived artifacts; "evidence sufficient for regulated deployments" (arXiv:2606.26627).

## 6. Industry practice (accessed 2026-09-24)

| Product | Memory model | Deletion / retention | Isolation | Audit | Source |
|---|---|---|---|---|---|
| **Mem0** (platform/OSS) | LLM-extracted facts (+ optional graph) | delete by id, batch (≤1000), `delete_all` by user/agent/run/metadata filter; `delete_all` with no filters now raises an error; docs say it "satisfies user erasure (GDPR/CCPA)". Hard vs soft delete not stated on the page | metadata scoping (`user_id`, `agent_id`, `run_id`) | not documented on the delete page | https://docs.mem0.ai/core-concepts/memory-operations/delete |
| **Letta** | MemGPT-style in-context memory blocks + archival (vector) memory | developers delete archival passages via SDK/API; archival memory is "agent-immutable"; no retention settings documented | "Identities" API exists; scoping not described on the page | not documented | https://docs.letta.com/guides/agents/archival-memory/ ; https://docs.letta.com/api/resources/agents/subresources/passages/methods/delete |
| **Zep / Graphiti** | bi-temporal knowledge graph; superseded facts *invalidated*, not deleted | deleting an episode removes edges/nodes only if no other episode references them; "does not regenerate the names or summaries of nodes shared with other episodes"; an invalidated fact stays invalidated after its episode is deleted | per-user graphs | not documented on the page | https://help.getzep.com/deleting-data-from-the-graph |
| **LangGraph Store / LangMem** | JSON documents under tuple namespaces (+ semantic search) | `delete(namespace, key)`; TTL not documented on the store page (MongoDB store adds TTL indexes per vendor blog) | namespaces; `namespace_prefix` matches **by prefix** | not documented | https://docs.langchain.com/oss/python/langgraph/stores |
| **ChatGPT memory** | saved memories + "reference chat history" | deleting a chat does not delete memories derived from it; logs of deleted memories may be kept up to 30 days; turning off chat-history reference schedules deletion within 30 days | per account | not described | https://help.openai.com/en/articles/8590148-memory-faq (fetch returned HTTP 403; statements taken from search-result snippets of the official page, **re-verify**) |
| **Claude memory** | per-topic memory entries; separate memory space per project | users view/edit/delete topics; deleting or expiring a chat does **not** remove memory derived from it; org-level off "permanently deletes all memory data"; incognito chats neither read nor write memory | project-separated | enterprise retention applies to incognito chats and chat search | https://support.claude.com/en/articles/11817273 |
| **Gemini app** | memory learned from past chats ("Personal Intelligence") | "short delay" before a deleted chat stops being used; toggle off | not available for work/school accounts | n/a | https://support.google.com/gemini/answer/16598469 |
| **Microsoft 365 Copilot memory** (preview; page dated 2026-09-02) | saved memories, inferred chat-history details, custom instructions, stored in a hidden Exchange mailbox folder | **Purview retention policies/labels do not apply**; saved memories kept until the user deletes them; deleting chats removes chat-history traces within 7 days; admin off → chat-history details deleted after 30 days; admins can eDiscover/delete via Purview + Graph | mailbox security (Customer Lockbox, encryption at rest) | "**Memory and personalization actions don't generate audit log entries in Purview**"; admins cannot restrict what goes into memory | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory |
| **Microsoft Foundry Agent Service memory** (preview; page dated 2026-06-02) | user-profile, chat-summary, **procedural** memory; LLM consolidation and conflict resolution | item-level CRUD; store-level default TTL; `delete_scope` per user; "remember-or-forget" commands | `scope` (e.g., `{{$userId}}`); must be set explicitly for low-level APIs; no VNet support | not described; recommends Content Safety prompt-injection detection against memory corruption | https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory |
| **AWS Bedrock AgentCore Memory** | short-term raw events + long-term records extracted by strategies | raw-event expiry up to 365 days, fixed at write time; long-term records persist until explicitly deleted (DeleteMemoryRecord) | actor/session/namespace; IAM condition keys `bedrock-agentcore:namespace`/`namespacePath`; trailing slash advised to avoid prefix collisions | via AWS (CloudTrail not checked) | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-create-a-memory-store.html |
| **Salesforce Agentforce / Einstein Trust Layer** | grounding via Data Cloud; no documented long-term agent memory on the page | zero data retention agreements with LLM providers; masking | secure data retrieval (not detailed) | "audit trail and feedback" (details not on page; secondary sources cite 30-day retention, unverified) | https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html |
| **Pinecone** | vector index | delete by id / id prefix / whole namespace (serverless: no delete-by-metadata); compaction drops deleted records asynchronously (per search snippet) | namespace-per-tenant; "physical isolation" in serverless | not documented | https://docs.pinecone.io/guides/index-data/implement-multitenancy |
| **Weaviate** | vector DB | "Deleting a tenant deletes all associated objects" (shard removed); object-level deletes are append-style per arXiv:2606.18497 | one shard per tenant; tenant offload to S3 | not on the page | https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy |

**Industry vs academia.** Vendors give *API-level* deletion, namespace scoping and TTL. Academia shows that these are insufficient in three ways:
- (i) deleted data persists in storage and in derived state (arXiv:2606.18497, arXiv:2609.04875, arXiv:2606.29788);
- (ii) natural-language deletion is brittle (arXiv:2606.15903);
- (iii) read-path scope enforcement is inconsistent (arXiv:2606.24535; Mem0 A = 28.1% in arXiv:2606.18829).

Several vendors say explicitly that **derived memories survive deletion of the source conversation** (ChatGPT, Claude, M365 Copilot, Zep). Enterprise-grade **retention-policy and audit integration for memory is missing** in the most finance-relevant product (M365 Copilot: no Purview retention, no audit log entries). Memory is excluded from HIPAA and custom-retention Claude organisations, and from Google work accounts, which suggests vendors themselves see memory as not yet compliant for regulated tenants. That last point is our inference.

---

## 7. Key groups / labs (from the records)
- Accenture Center for Advanced AI (arXiv:2505.18279).
- Microsoft Research India/Redmond (arXiv:2509.14608).
- Purdue, Bertino group (ChronoMem arXiv:2607.27773).
- Letta/MemGPT (UC Berkeley origin, arXiv:2310.08560).
- Mem0 (arXiv:2504.19413); Zep (arXiv:2501.13956).
- MemTensor/MemOS (arXiv:2507.03724).
- Chakraborttii group (Ghost Vectors, Ghost Echoes).
- Many frontier governance papers are single-author or small teams (e.g., arXiv:2606.15903, arXiv:2608.02843, arXiv:2605.30771). They are not peer-reviewed, so weight them accordingly.

---

## 8. Gaps I noticed (my observations; confidence in brackets)

1. **No finance-specific memory-governance mechanism or benchmark** [high]. GateMem covers medical, office, education and household; MUMBench and CI-Work cover enterprise and general settings. None models information barriers between, e.g., research/advisory and trading, or client-by-client need-to-know with wall-crossing events. Searches for "information barrier" + memory returned nothing relevant.
2. **Retention obligations vs erasure are never modelled together** [high]. Every forgetting paper optimises "forget". Record-keeping rules (the regulation scout will map SEC/FINRA and MiFID II specifics) require *keep, immutably, for N years*. No mechanism reconciles "erase personal data from the agent's working memory and derivatives" with "keep a tamper-evident record of what the agent knew when it acted". Versioning (arXiv:2607.27773) and immutable logs (arXiv:2603.11768, arXiv:2605.14421) keep everything; unlearning (arXiv:2609.04875) removes everything downstream. A split design is untested: erasable working memory plus a retained, access-restricted, crypto-shredded compliance record.
3. **Erasure with derivatives across layers is unsolved end to end** [high]. Storage residue, index traversal, retrieval drift, derived summaries, KV cache, images and parametric memory are each covered by a separate paper. None measures a full stack. A deletion-verification protocol spanning these layers looks open (overlap check needed with the evaluation scout).
4. **Authorization continuity through consolidation** [med]. Collaborative Memory transforms private fragments into shared memory, and provenance laundering (arXiv:2607.29167) and AkasicMEM (abstract only) point to the issue. No quantitative study measures how often consolidation or summarisation carries restricted facts across scopes in realistic multi-client workloads.
5. **Industry audit gap** [med-high, based on docs]. Among the products checked, only Mem0 documents a delete surface with compliance language, and none documents a memory-operation audit log in its product docs. M365 Copilot says so explicitly. Academic audit proposals (Merkle logs, hash chains) have not been evaluated against supervisory expectations.
6. **Consent and purpose limitation at the memory level** [med]. Beyond contextual-integrity benchmarks, we found no mechanism that attaches purpose/consent metadata to memory items and enforces it at recall. arXiv:2606.26627 lists policy representation as open.
7. **Evaluation of learned (RL) memory managers under governance constraints** [med]. Memory-R1, AgeMem and DeltaMem optimise task reward only. Nobody reports leakage, deletion compliance or auditability for learned write/delete policies.
8. **Independence of evidence** [med]. Many governance mechanisms are evaluated on self-built harnesses (MemClaw/ArgusFleet, MemTX suite, MemLineage deterministic harness, ForgetEval). Third-party replication is essentially absent.

## 9. Flags
- Record arXiv:2609.19456: the arXiv title ("Beyond Private Training: The New Landscape of AI Privacy") does not match its abstract (TSD-AUDIT, traversal-safe deletion). The metadata is as returned by arXiv. Check before citing.
- Several SciSpace hits are Zenodo preprints (e.g., doi:10.5281/zenodo.18346036 SoK authorization; doi:10.5281/zenodo.18136347 MemoryFlow). They are recorded but unreviewed and low-assurance.
- ChatGPT memory FAQ could not be fetched (HTTP 403); its row uses search snippets of the official page.

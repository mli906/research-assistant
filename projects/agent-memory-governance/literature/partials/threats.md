# Threats, attacks, risks and defenses for agent memory: partial review (facet tag `threats`)

- Scout: lit-scout (threats facet). Date: 2026-09-24.
- Recency cutoffs: arXiv searched through 2026-09-22 (the newest hit). SciSpace index lags by months; its newest hit here is 2026-01. Web sources were accessed 2026-09-24.
- Library: 195 records tagged `threats` in `literature/papers.jsonl`, 16 of them also tagged `core`, with notes in `literature/notes/arXiv-<id>.md`.
- Evidence levels: "full" means I read the arXiv HTML through the fetch tool, which returns an extracted summary, not a line-by-line read. Everything else is per abstract.
- Known false positives: `arXiv:2609.04547` (a MemGuard for memory-bandwidth regulation in real-time systems) and `arXiv:2603.26797` (MemGuard-Alpha, about training-data memorization in financial forecasting, not agent memory) are wrongly tagged `threats`. Ignore them. `lit.py` has no untag command.
- `inputs/INDEX.md` does not exist, so there were no PI materials to build on.

---

## 1. Query plan (reusable by `/radar`)

| Facet | Queries (arXiv `lit.py arxiv`, since 2025-06-01 unless noted) | SciSpace question |
|---|---|---|
| Poisoning / injection | `(memory poisoning OR memory injection) AND (agent OR "LLM agent")`; same with `--sort date`; `(memory poisoning OR memory injection OR memory extraction OR memory leakage) AND agent --since 2026-08-01 --sort date`; `"A-MemGuard" OR "memory injection attack" OR "MemoryGraft" OR "SpAIware" OR "InjecMEM"` | "How can attackers poison the long-term memory or knowledge base of LLM agents…?" |
| Multi-agent propagation | `"multi-agent" AND memory AND (poisoning OR contamination OR propagation)` | — |
| Extraction / privacy / CI | `"memory extraction" OR ("memory" AND "privacy leakage" AND agent)`; `"contextual integrity" AND (agent OR memory)`; `(cross-session OR cross-user OR cross-tenant) AND leakage AND (memory OR agent)` | "What privacy risks arise from persistent memory in LLM assistants…across users or sessions?" |
| Forgetting / unlearning | `(unlearning OR deletion OR forgetting) AND "agent memory"`; `(unlearning OR erasure OR deletion) AND (agent memory OR RAG) AND (verification OR residual OR recover)` | "How can deleted or unlearned data be recovered from RAG systems or agent memory…?" |
| Stale / hallucinated / error propagation | `agent memory AND (stale OR hallucinated OR self-reinforcing OR error propagation)` | — |
| RAG-poisoning defenses (adjacent) | `(RAG OR retrieval) AND poisoning AND (defense OR certified)` | "What defenses protect RAG and agent memory against knowledge corruption, and what is their utility cost?" |
| Provenance / audit / tamper | `memory AND agent AND (provenance OR integrity OR tamper OR audit log)`; `(tamper-evident OR hash chain OR signed) AND (audit log OR audit trail) AND agent` | — |
| Taxonomies / standards | `(taxonomy OR survey OR SoK) AND agent AND memory AND (security OR threat)`; `OWASP AND (agentic OR LLM) AND (memory OR threat)` | "What taxonomies of security threats for agentic AI explicitly cover memory poisoning…?" |
| Finance | `(financial OR finance OR trading OR banking) AND agent AND (memory OR poisoning)` | "What are the security risks of LLM-based agents in financial services…?" |
| Web (industry/standards) | OWASP ASI06; MITRE ATLAS AML.T0080; Unit 42 memory poisoning; Rehberger ChatGPT/Gemini memory; NIST CAISI agent RFI; FINOS/FS-ISAC memory poisoning; bank AI data-leak incidents | — |
| Snowball | `lit.py cites` on MINJA (arXiv:2503.03704) and AgentPoison (arXiv:2407.12784) | — |

---

## 2. Threat taxonomy

**Axes.**
- **Memory stage.** The lifecycle phases follow arXiv:2604.16548: Write, Store, Retrieve, Execute, Share/Propagate, Forget/Rollback.
- **Adversary capability (my labels).**
  - **A0**: outsider who controls content the agent reads (web, email, document, social feed).
  - **A1**: ordinary user or tenant with query-only access.
  - **A2**: malicious or compromised tool or third-party vendor.
  - **A3**: insider or anyone with write access to the store.
  - **A4**: compromised peer agent in a multi-agent system.
  - **N**: no adversary (benign failure).
- **Impact.** I = integrity / unsafe action, C = confidentiality, A = availability / utility, G = governance / compliance (auditability, erasure, record-keeping).

| # | Threat class | Main stage(s) | Adversary | Impact | Representative evidence (ids) | Finance reading (my interpretation) |
|---|---|---|---|---|---|---|
| T1 | Direct / backdoor memory poisoning (optimized triggers) | Write (direct), Retrieve | A3 | I | AgentPoison arXiv:2407.12784; XAMT arXiv:2512.15790; PoisonedRAG arXiv:2402.07867 | Poisoned policy/KB store behind a client-service or credit agent |
| T2 | Query-only injection into shared memory (cross-user) | Write, Retrieve | A1 | I | MINJA arXiv:2503.03704; MAFIA arXiv:2608.03844 (audit-evading); InjecMEM arXiv:2608.23471; ER-MIA arXiv:2602.15344; realistic replication arXiv:2601.05504 | One client's sessions shape advice given to another client |
| T3 | Indirect / environment-injected persistent poisoning | Write (via summarization/compaction), Execute | A0 | I, C | eTAMP arXiv:2604.02623; Zombie Agents arXiv:2602.15654; Sleeper arXiv:2605.15338; PMPA on OpenClaw and Claude Code arXiv:2609.13889; WhisperBench arXiv:2607.05189; Cross-session stored PI arXiv:2606.04425; PipePoison arXiv:2609.00523; IBIA arXiv:2608.22061; Unit 42 Bedrock PoC (web) | An email or research note seeds a durable "fact" or instruction into an advisor copilot |
| T4 | Dormant, topic-triggered exfiltration | Write, Execute | A0 / A2 | C | Trojan Hippo arXiv:2605.01970 (fires on finance/health/identity topics, persists 100+ sessions); SpAIware / Gemini (web) | Banking details are exfiltrated when the client later discusses savings or loans |
| T5 | Collusive / fragmented ("salami") poisoning | Write, Store (composition) | A0 / A1 | I | MemCollusion arXiv:2608.01637; Coverage-not-containment arXiv:2608.16044 (coordinated vector-store poisoning) | Individually benign notes that together justify a policy exception |
| T6 | Forged reasoning / false precedent / experience grafting | Write (procedural/episodic), Execute | A0 / A3 | I | MemoryGraft arXiv:2512.16962; FARMA arXiv:2607.05029; MemMorph (tool-selection) arXiv:2605.26154; EVOMAL self-poisoning skills arXiv:2608.25776; MPBench weak-signal classes arXiv:2606.04329 | "Compliance check already done" recorded as precedent; maker-checker skipped |
| T7 | Structured / multimodal memory poisoning | Write, Retrieve | A0 | I | ShadowMerge (graph memory) arXiv:2605.09033; MemVenom arXiv:2606.10742; Visual Inception arXiv:2604.16966; Visual memory injection arXiv:2602.15927 | KYC documents or images as a carrier |
| T8 | Multi-agent propagation / shared-memory promotion / trust laundering | Share/Propagate | A4, A0 | I, G | MAPLE-Guard arXiv:2608.00426; Trust propagation arXiv:2609.17648; Misattribution Gap arXiv:2605.22842; Subagent inheritance arXiv:2605.08460; Flooding spread arXiv:2407.07791; Contagion on trading floor arXiv:2609.19789; Poisoning Agentic Alpha arXiv:2608.24069 | Contagion from a research desk into a trading or risk agent; a wrong root-cause attribution in the incident report |
| T9 | Provenance laundering (summarization, tool echo, fake corroboration) | Write/Store (consolidation) | A0 | I, G | TMA-NM arXiv:2606.24322; PPMF arXiv:2607.29167; memory laundering (toxicity) arXiv:2605.16746; provenance-role collapse arXiv:2605.25869 | Undermines audit trails: the origin of a "client instruction" is lost |
| T10 | Memory extraction (black-box) and membership inference | Retrieve, Execute | A1 | C | MEXTRA arXiv:2502.13172; ADAM arXiv:2604.09747; MRMMIA arXiv:2605.27825; embedding inversion (Eguard) arXiv:2411.05034 | Extraction of other clients' holdings or queries |
| T11 | Tool-side extraction despite per-user isolation | Execute (tool args) | A2 | C | SPORE arXiv:2607.23444; Claw in Plain Sight arXiv:2608.20658; You Told Me To Do It arXiv:2603.11862 | Third-party/outsourcing risk (vendor APIs) |
| T12 | Contextual-integrity violations / cross-context & cross-audience leakage (no attacker) | Retrieve, Execute | N (or A1 prying) | C, G | CIMemories arXiv:2511.14937; PersistBench arXiv:2602.01146; PiSAs arXiv:2607.05318; CI-Work arXiv:2604.21308; AgentLeak arXiv:2602.11510; Authorization-before-context arXiv:2608.17148; ChatGPT health-memory audit arXiv:2609.14697; CIPL arXiv:2609.21686 | Information-barrier (Chinese wall) breaches; MNPI crossing desks |
| T13 | Cross-tenant retrieval leakage | Retrieve | A1 / N | C | Multitenant enterprise retrieval arXiv:2605.05287; Governed shared memory (MemClaw) arXiv:2606.24535; AIM / MUMBench arXiv:2609.12320 | Shared vendor platforms serving multiple institutions |
| T14 | Stale / hallucinated / contaminated memory and error propagation | Store, Retrieve, Execute | N | I, A | HaluMem arXiv:2511.03506; Temporal validity arXiv:2606.26511; Spatial staleness arXiv:2608.04574; Memory interference arXiv:2608.07622; Misevolution arXiv:2604.15774; Temporal memory contamination arXiv:2605.17830; Sycophancy amplification arXiv:2606.10949; Silent failures in production arXiv:2606.14589; MemRiskBench arXiv:2609.14976 | Stale suitability/KYC profile; outdated risk limits applied |
| T15 | Preference drift vs manipulation | Write (update), Store | A0 / A1 vs N | I, G | CAPTURE arXiv:2609.02265 | Legitimate change in risk appetite vs a social-engineered change (suitability) |
| T16 | Revocation and deletion failures (data that "comes back") | Forget/Rollback | N (A1 for probing) | C, G | Revoked-but-authoritative arXiv:2609.08258; Execution-state unlearning arXiv:2609.04875; MemLeak arXiv:2606.29788; Control-plane placement arXiv:2606.15903; OBLIVION arXiv:2608.08264; MEMOREPAIR cascade arXiv:2605.07242; quantization undoes LLM unlearning arXiv:2410.16454 | GDPR Art. 17 erasure vs retention; withdrawn advice or superseded policy still acted on |
| T17 | Self-state / configuration-file tampering (agent's own files) | Store | A0 via agent, A3 | I, G | Self-state attacks arXiv:2607.17986; OWASP "MemoryTrap" blog (web) | Persistent compromise of a desktop coding or ops agent |
| T18 | Audit-log / evidence integrity | Store (logs) | A3 | G | *Mechanisms only*: Agent Flight Recorder arXiv:2609.01931; NovaFabric arXiv:2609.12582; MutMem arXiv:2608.02843; Mandato arXiv:2608.14074; Right to History arXiv:2602.20214; Auditable Agents arXiv:2604.05485. The only threat-side mention is incident reporting noting attacks on reporting infrastructure, arXiv:2609.24515 | Books-and-records (SEC 17a-4 / MiFID II record-keeping) evidentiary value |

---

## 3. Attack and defense comparison (reported numbers; "full" = close-read, otherwise per abstract)

### 3a. Attacks

| Attack (id) | Setting / data | Adversary | Reported result | Read |
|---|---|---|---|---|
| AgentPoison arXiv:2407.12784 | Driving, QA, EHRAgent | A3 | ASR >80% at poison rate <0.1%, benign impact <1% | abstract |
| MINJA arXiv:2503.03704 | EHRAgent, RAP, QA; GPT-4/4o | A1 | ISR about 98.2%, ASR about 76.8%, utility drop <2% | full |
| MINJA replication, EHR arXiv:2601.05504 | MIMIC-III; GPT-4o-mini, Gemini-2.0-Flash, Llama-3.1-8B | A1 | Pre-existing legitimate memories "dramatically reduce" effectiveness | abstract |
| MAFIA arXiv:2608.03844 | Audited agents, large memory pools | A1 | ASR up to 90.7%; audit detection cut from 83.3% to ≤7.4% | abstract |
| PMPA arXiv:2609.13889 | OpenClaw, Claude Code | A0 | ISR / cross-session ASR 73.7/55.5% (OpenClaw), 66.9/81.7% (Claude Code) | abstract |
| MemCollusion arXiv:2608.01637 | OpenClaw, 48 scenarios | A0 | Memory save rate 81.3%, ASR 75.0%; survives dilution and memory-level defenses | abstract |
| MPBench arXiv:2606.04329 | OpenClaw, HERMES; GPT-OSS-120B | A0 | ASR 34.3% / 66.7%; weak-signal attacks detected at about 25% | full |
| Injection-execution dissociation arXiv:2605.08442 | 9 open + 21 frontier models | A0 | Storage >97.5%, execution 0-95%, uncorrelated | full |
| Trojan Hippo arXiv:2605.01970 | Window, RAG, explicit, Mem0 | A0/A2 | ASR up to 85-100%; persists 100+ sessions | full |
| SPORE arXiv:2607.23444 | LTM frameworks, Dify/Coze+Mem0 | A2 | Extraction 80.0% (vs MEXTRA 3.0%) | full |
| MEXTRA arXiv:2502.13172 | EHRAgent, RAP, 200 records | A1 | 50 / 26 unique queries from 30 prompts | full |
| CIMemories arXiv:2511.14937 | Frontier LLMs, 100+ attributes per user | N | Up to 69% attribute-level violations; GPT-5 rises from 0.1% to 9.6% over 40 tasks, and to 25.1% with 5 repeats | abstract |
| CI-Work arXiv:2604.21308 | Enterprise workflows | N | Violation rate 15.8-50.9%, leakage up to 26.7% | abstract |
| Revoked facts arXiv:2609.08258 | Graphiti, Zep, mem0, langmem, cognee | N | Unsafe action 44.2% / 42.1% where the revoked fact is returned; 81% without a prompt rule | full |
| Execution-state residue arXiv:2609.04875 | Stateful agents | N | Record delete leaves any-leak at 0.86-1.00; 80% still act on a redacted preference | full |
| MemLeak arXiv:2606.29788 | Multimodal memory | A1 probing | Deletion appears to work on direct probing (<1% recovery), but retained correlated text still allows 18.3% recovery (images also leak) | abstract |
| Poisoning Agentic Alpha arXiv:2608.24069 | 4 trading topologies, Q1-2026 | A0 | Return loss 1.45-12.38 pp; jailbreak ASR 98.9% with median $0 impact | full |
| FinVault arXiv:2601.07853 | 31 finance sandboxes, 963 cases | A0/A1 | ASR up to 50.0%; best system still 6.7% (not memory-specific) | abstract |

### 3b. Defenses

| Defense (id) | Stage / type | Attack(s) | Security result | Utility / cost | Read |
|---|---|---|---|---|---|
| A-MemGuard arXiv:2510.02373 | Retrieve/execute; consensus + lessons memory | AgentPoison, MINJA | EHR ASR 100% to 2.13%; MMLU 0.667 to 0.256 | About 7.8K tokens per task (vs 8.0K for an LLM-auditor baseline); cold-start limitation | full |
| MAPLE-Guard arXiv:2608.00426 | Write, retrieve, promotion, cross-agent gates | MINJA, MemoryGraft, AgentPoison, others | ASR 38.2% to 0.9% (LongMemEval); 34.7% to 0.2% (AppWorld) | About 1-4 pp benign MDSR loss; no extra LLM calls | full |
| TMA-NM arXiv:2606.24322 | Write-time origin binding + act gate; TLA+ checked | Direct and laundered poisoning; MemMorph, MemoryGraft, Trojan Hippo | ASR 0% on all channels (content detection 68%, lineage 47% on laundered) | 100% legitimate actions authorized; gate latency 1.3 µs; user confirmations needed when corroborators are scarce | full |
| SMSR arXiv:2606.12703 | Signed memory + smoothed retrieval (certified) | Multi-session memory poisoning | "First certified" bound claimed | not extracted | abstract |
| MutMem arXiv:2608.02843 | Ed25519-signed mutation log | Tampering; PoisonedRAG | 0/100 poison in top-5 | LongMemEval 91.8%; 4.865 ms median per signed transition | abstract |
| Revocation guard arXiv:2609.08258 | Retrieval-time validity filter | Stale/revoked facts | Unsafe action 0.0% over 1,620 trials (store filter) | Deterministic; negligible | full |
| Rollback repair arXiv:2608.10502 | Forget/rollback | Poisoned, stale, wrong-user, drift | Recovery 85.3% vs 77.3% | 5.7 LLM calls; 12.3% replay | full |
| Selective replay unlearning arXiv:2609.04875 | Forget | Residual state | 0.00 leakage | 9x fewer tokens than reset; cost ∝ T−τ+1 | full |
| CAPTURE arXiv:2609.02265 | Update / belief tracking | Preference poisoning | Poison success 11.5%; **24.7% under an adaptive attacker** | Accepts 83.5% of genuine updates | abstract |
| Trojan Hippo defenses arXiv:2605.01970 | Write policies, IFC | Trojan Hippo | 0-5% (write restrictions), 0% (IFC), 20-30% (length limit) | Breaks plan recall, memory updates or email workflows | full |
| MPBench PI detectors arXiv:2606.04329 | Write-time classifiers | 6 classes | Best TPR 67.7%; weak-signal about 25% | Retraining <10 pp gain | full |
| Injection-execution defenses arXiv:2605.08442 | Filters, hardening, sandbox | Persistent injection | Filters fail; hardening 77.8% ASR; sandbox 0% for 8/9 models but inverts on one | Sandbox removes recall | full |
| RAGDefender arXiv:2511.01268 | Post-retrieval (RAG) | Knowledge corruption | Gemini ASR 0.89 to 0.02 | "No additional model training or inference" | abstract |
| EcoSafeRAG arXiv:2505.13506 | Context-diversity detection (RAG) | Corpus poisoning | SOTA claimed | 1.2x latency, 48-80% fewer tokens than vanilla RAG | abstract |
| Coverage ≠ containment arXiv:2608.16044 | (Negative result) admission-time filters | Coordinated poisoning | m=10 documents take 10/10 top-k on BGE-large | n/a | abstract |
| MemPot arXiv:2602.07517 | Honeypots + SPRT detection | Extraction | Theoretical detection guarantees | not extracted | abstract |
| SPORE defenses arXiv:2607.23444 | Response filter, prompt hardening | Tool-side extraction | 80% to 54.0% / 32.5% | — | full |
| PrivacyChecker arXiv:2509.17488 | CI-based mitigation | CI leakage | 36.08% to 7.30% (DeepSeek-R1); 33.06% to 8.32% (GPT-4o) | "preserving helpfulness" | abstract |

---

## 4. Defense cost evidence (what exists)

1. **Benign-traffic utility.** Only one paper isolates it: arXiv:2609.22818 (full).
   - Write-time sanitization, provenance and anomaly detection have no detectable accuracy cost at ±4.5 pp.
   - A read-time consistency reranker costs −4.4 pp and **falsely quarantines 33.6% of legitimate memories**.
   - Token overhead is 0-2.7% per defense and 4.1% stacked, roughly additive.
   - Latency is not reported.
2. **Utility loss from structural restrictions** (arXiv:2605.01970, full). Blocking writes after contact with an untrusted source, or applying information-flow control, gets ASR to about 0%. The price is losing whole workflows (plan recall, email sending). This cost is qualitative, not a metric.
3. **Latency of cryptographic and deterministic controls.**
   - Origin-bound act gate: 1.3 µs vs about 2 s for an LLM detector (arXiv:2606.24322).
   - Signed memory mutation: about 4.9 ms median (arXiv:2608.02843, per abstract).
   - Deterministic gates in MAPLE-Guard need no extra LLM calls (arXiv:2608.00426).
4. **LLM-based defenses.**
   - A-MemGuard uses about 7.8K tokens per task and is reported only against another LLM defense (arXiv:2510.02373).
   - EcoSafeRAG claims a 1.2x latency cost but reduces tokens.
5. **Repair and erasure cost.**
   - Selective replay scales with T−τ+1: erasing something learned long ago is expensive, though still 9x cheaper than a full reset (arXiv:2609.04875).
   - Rollback repair uses 5.7 LLM calls per case (arXiv:2608.10502).
6. **Design-knob trade-offs** (arXiv:2608.30177, full).
   - The management/consolidation policy can cut ASR by up to 62 pp at a 3-5 pp utility cost.
   - Retrieval depth raises utility and risk together, so it cannot be "free".
7. **Adaptive-attacker cost of security** (arXiv:2609.02265): poisoning success roughly doubles, from 11.5% to 24.7%, when the attacker has the released weights.

My reading: cost evidence is thin and uneven. It is one benign-cost study with n=5 conversations, and no study reports cost in regulatory units, such as the rate of false quarantine of legitimate client facts, which would itself be a record-keeping and suitability failure.

---

## 5. Frontier timeline (monthly for 2026; from this sample)

The counts are records in my sample by publication month, not a census. Searches were weighted toward recent months with `--sort date`, so treat them as a lower bound on activity.

| Month | # in sample | Notable items |
|---|---|---|
| ≤2025-05 (foundations) | 16 | ConfAIde arXiv:2310.17884; PoisonedRAG arXiv:2402.07867; AgentPoison arXiv:2407.12784; Flooding spread arXiv:2407.07791; ASB arXiv:2410.02644; MEXTRA arXiv:2502.13172; MINJA arXiv:2503.03704. Web: ChatGPT SpAIware (2024-09) and Gemini memory attack (2025-02-10, embracethered.com) |
| 2025-06 to 2025-12 | 22 | DRIFT arXiv:2506.12104; A-MemGuard arXiv:2510.02373; agentic security surveys arXiv:2510.23883, arXiv:2506.23844; CIMemories arXiv:2511.14937; HaluMem arXiv:2511.03506; MemoryGraft arXiv:2512.16962; XAMT arXiv:2512.15790. Web: Unit 42 Bedrock memory-poisoning PoC (2025-10-09); MITRE ATLAS AML.T0080 "AI Agent Context Poisoning" (.000 Memory, .001 Thread), reported as added Oct 2025 (secondary sources); **OWASP Top 10 for Agentic Applications with ASI06 Memory & Context Poisoning (2025-12-09)** |
| 2026-01 | 3 | MINJA realistic replication arXiv:2601.05504; FinVault arXiv:2601.07853; Promptware kill chain arXiv:2601.09625. Web: NIST CAISI RFI on AI-agent security (Federal Register 2026-01-08; page blocked to fetch, per search snippet) |
| 2026-02 | 9 | Zombie Agents arXiv:2602.15654; ER-MIA arXiv:2602.15344; MemPot arXiv:2602.07517; AgentLeak arXiv:2602.11510; PersistBench arXiv:2602.01146; AgentSys arXiv:2602.07398. Web: **Microsoft "AI Recommendation Poisoning", the first in-the-wild commercial memory poisoning report** (2026-02-10) |
| 2026-03 | 8 | Memory poisoning & secure MAS arXiv:2603.20357; Observable channels arXiv:2603.22751; AgentSCOPE arXiv:2603.04902; Perplexity response to NIST arXiv:2603.12230. Web: CSA ATLAS agentic gap note proposing a separate "Memory Persistence Across Sessions" technique (2026-03-27) |
| 2026-04 | 9 | eTAMP arXiv:2604.02623; ADAM arXiv:2604.09747; MemEvoBench arXiv:2604.15774; **lifecycle survey arXiv:2604.16548**; CI-Work arXiv:2604.21308; Visual Inception arXiv:2604.16966 |
| 2026-05 | 29 | Trojan Hippo arXiv:2605.01970; Injection-execution dissociation arXiv:2605.08442; ShadowMerge arXiv:2605.09033; Sleeper arXiv:2605.15338; Misattribution Gap arXiv:2605.22842; MemMorph arXiv:2605.26154; MRMMIA arXiv:2605.27825; MEMOREPAIR arXiv:2605.07242. Web: OWASP "Memory is a feature…" / MemoryTrap (2026-05-13); CB Financial shadow-AI 8-K (2026-05-11) |
| 2026-06 | 22 | MPBench arXiv:2606.04329; Cross-session stored PI arXiv:2606.04425; SMSR (certified) arXiv:2606.12703; TMA-NM (TLA+) arXiv:2606.24322; MemLeak arXiv:2606.29788; Governed shared memory arXiv:2606.24535; Always-on survey arXiv:2606.30306 |
| 2026-07 | 13 | FARMA arXiv:2607.05029; WhisperBench arXiv:2607.05189; PiSAs arXiv:2607.05318; MemPoison benchmark arXiv:2607.14651; SPORE arXiv:2607.23444; MemSecBench arXiv:2607.27080; MIND arXiv:2607.28103; PPMF arXiv:2607.29167; Self-state attacks arXiv:2607.17986. Web: Microsoft Learn Zero-Trust "AI memory/context poisoning" catalog (ms.date 2026-07-28) |
| 2026-08 | 29 | MAPLE-Guard arXiv:2608.00426; Salami arXiv:2608.01637; MutMem arXiv:2608.02843; MAFIA arXiv:2608.03844; Rollback repair arXiv:2608.10502; Coverage≠containment arXiv:2608.16044; Authorization-before-context arXiv:2608.17148; InjecMEM arXiv:2608.23471; Poisoning Agentic Alpha arXiv:2608.24069; MemGauge arXiv:2608.30177 |
| 2026-09 (to 09-22) | 35 | PipePoison arXiv:2609.00523; CAPTURE arXiv:2609.02265; Execution-state unlearning arXiv:2609.04875; Revoked-but-authoritative arXiv:2609.08258; MemSentry arXiv:2609.08747; PMPA arXiv:2609.13889; ChatGPT health-memory audit arXiv:2609.14697; MemRiskBench arXiv:2609.14976; SoK trading agents arXiv:2609.19705; Contagion trading floor arXiv:2609.19789; CIPL arXiv:2609.21686; Price of Safety arXiv:2609.22818; cross-dimensional taxonomy arXiv:2609.23894 |

**What changed in the last 12 months.** The field moved through these stages:
1. Single-shot, optimized attacks (AgentPoison, MINJA).
2. Realistic black-box persistence: environment-injected, dormant, collusive, and attacks on deployed harnesses (OpenClaw, Claude Code).
3. Lifecycle-level questions: what gets executed vs stored, laundering through consolidation, propagation across agents, revocation, erasure and repair.
4. Formal and cryptographic defenses (TLA+-checked origin authority, certified retrieval, signed mutation) and cost-of-defense measurement, from 2026-06 onward.

Standards bodies caught up: ASI06 (2025-12), ATLAS AML.T0080 (2025-10), MS Zero-Trust catalog (2026-07).

---

## 6. How crowded is each sub-area (my judgment from this sample)

| Sub-area | # in sample | Crowding | Notes |
|---|---|---|---|
| Poisoning / injection attacks | about 60 | **Very crowded.** About 6-10 new papers per month since 2026-05 | Novelty now comes from threat-model realism (deployed harnesses, stealth, collusion). A new attack alone is not a contribution |
| Poisoning defenses (detection, provenance, gates, crypto) | about 58 | **Crowded and fragmented** | Few head-to-head comparisons on a shared harness; adaptive attacks rarely tested |
| Extraction / privacy / contextual integrity | about 34 | Moderate, growing | CI benchmarks proliferating (CIMemories, PiSAs, CI-Work, AgentSCOPE, PersistBench) |
| Lifecycle benchmarks | about 5 | Suddenly crowded (2026-07 to 09) | MemPoison, MemSecBench, MemRiskBench, MPBench, MemEvoBench |
| Stale / hallucinated / error propagation | about 11 | Moderate-sparse | Mostly reliability framing, little security framing |
| Forgetting / revocation / erasure verification | about 9 | **Sparse but accelerating** (2026-06 to 09) | Strong pieces: arXiv:2609.04875, arXiv:2609.08258, arXiv:2606.29788 |
| Audit-log integrity | about 12 | Mechanisms moderate, **attacks absent** | Tamper-evident logging is proposed, but nobody attacks memory audit trails |
| Preference drift vs manipulation | 1 | **Very sparse** | CAPTURE only |
| Finance-specific memory threats | about 7 finance-related, **0 memory-specific** | **Empty** | Finance papers attack data feeds and inter-agent messages, not persistent memory |

---

## 7. Industry, standards and incidents (URL, accessed 2026-09-24)

- **OWASP Top 10 for Agentic Applications**, released 2025-12-09. ASI06 is "Memory & Context Poisoning"; the Gemini memory attack is its example. ASI07 (insecure inter-agent comms) and ASI08 (cascading failures) are adjacent. https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/ . Follow-up by the ASI06 lead (Cisco) on "MemoryTrap" (poisoned memory files and hooks in developer workflows), 2026-05-13: https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface/
- **MITRE ATLAS AML.T0080 "AI Agent Context Poisoning"** (.000 Memory, .001 Thread), plus AML.T0070 RAG Poisoning. The official page https://atlas.mitre.org/techniques/AML.T0080 returned **404** on fetch. The IDs were confirmed via Microsoft Learn (below) and a CSA note. CSA (2026-03-27) argues ATLAS treats memory as in-session manipulation and proposes a separate persistence technique: https://labs.cloudsecurityalliance.org/agentic/csa-research-note-atlas-agentic-gap-analysis-20260327/
- **Microsoft Learn, Zero Trust AI attack catalog #4 "AI Memory / Context Poisoning"** (ms.date 2026-07-28). Maps to OWASP LLM04, LLM08 (Vector & Embedding Weaknesses), LLM01, LLM02 and ATLAS T0080/T0070. Controls listed: privileged memory writes, schema-bound memory, sanitization, versioning, rollback, periodic purge, cross-agent isolation, trust scoring. https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/ai-memory-context-poisoning
- **Microsoft Defender research, "AI Recommendation Poisoning"** (2026-02-10). **Documented in-the-wild** use: 31 companies across 14+ industries, 50+ attempts in 60 days, using "Summarize with AI" links that tell the assistant to "remember [Company] as a trusted source". **Finance and crypto sites are among them.** https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/
- **Palo Alto Unit 42**, Amazon Bedrock Agents memory poisoning via session summarization (**PoC**, 2025-10-09): https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/
- **J. Rehberger (Embrace The Red)**, Gemini memory poisoning via delayed tool invocation (2025-02-10; Google rated it low likelihood/low impact). It references the earlier ChatGPT SpAIware (2024). **PoC.** https://embracethered.com/blog/posts/2025/gemini-memory-persistence-prompt-injection/
- **FINOS AI Governance Framework, RI-27 "Agent State Persistence Poisoning"** (AIR-SEC-027). Gives finance examples: transaction-approval bias, loan-risk corruption, fee-waiver manipulation, trading-signal suppression, compliance-override persistence. Mitigations: AIR-PREV-022 isolation, AIR-DET-004 observability. It maps to ASI06 and the IOSCO toolkit. **These examples are hypothetical, not incidents.** https://air-governance-framework.finos.org/risks/ri-27_agent-state-persistence-poisoning.html
- **NIST CAISI** RFI on security considerations for AI agents (Federal Register 2026-01-08, comments due 2026-03-09). The page was **blocked on fetch**, so I have not verified whether it mentions memory. See Perplexity's public response, arXiv:2603.12230. NIST AI 600-1 was **not checked** for memory-specific language; I leave that to the regulation scout.

**Finance incidents.**
- **Documented but not memory-specific:** CB Financial Services (Community Bank, PA) filed an 8-K Item 1.05 on 2026-05-11. An employee put customer SSNs and DOBs into an unapproved AI app, and the bank got the vendor to exclude the data from training. This is retention and vendor-side memory of customer data, not agent memory. https://www.americanbanker.com/news/a-bank-breaks-its-silence-on-its-shadow-ai-breach
- **Documented, in-the-wild, finance among the targets:** Microsoft AI Recommendation Poisoning (above).
- **Anecdotal or hypothetical:** FINOS RI-27 scenarios, and vendor blogs claiming months-long compromise. I found **no documented incident of a financial institution's agent memory being poisoned or leaking across clients.**

---

## 8. Gaps I noticed (my observations; confidence in brackets)

1. **No finance-specific memory-threat study** [high]. Trading and financial-agent security papers (arXiv:2608.24069, arXiv:2609.19789, arXiv:2609.19705, arXiv:2601.07853) attack feeds, prompts and messages. None tests a poisoned reflection or lesson that persists across trading days, or cross-client memory contamination in advisory or KYC. arXiv:2608.24069 has a `past_memory` slot but does not attack it.
2. **Information barriers as a memory property** [med-high]. CI and multi-user work (PiSAs arXiv:2607.05318, AIM arXiv:2609.12320, Authorization-before-context arXiv:2608.17148, MAPLE-Guard's promotion gate) comes close. Nobody evaluates Chinese-wall or MNPI separation of shared agent memory, or measures leakage *between desks or clients* under realistic consolidation.
3. **Defense cost in regulatory units** [high]. Only arXiv:2609.22818 measures benign cost, with n=5 and ±4.5 pp resolution and no latency. No one measures false quarantine or erasure of *legitimate client records* as a compliance harm, or the user-confirmation burden of maker-checker-style gates (arXiv:2606.24322 acknowledges it but does not measure it in a real workflow).
4. **Erasure vs retention conflict** [high]. Execution-state unlearning (arXiv:2609.04875), revocation (arXiv:2609.08258) and MemLeak (arXiv:2606.29788) show that record deletion is not forgetting. No work deals with the finance-specific tension between GDPR Art. 17 erasure and mandatory retention (e.g. SEC 17a-4, MiFID II record-keeping), i.e. "forget for behavior, retain for audit".
5. **Audit-trail attacks** [med]. Many tamper-evident logging mechanisms exist (arXiv:2609.01931, arXiv:2609.12582, arXiv:2608.02843), but I found no attack study on agent memory audit logs. That includes laundering that makes the log *accurate but misleading* (provenance collapse, arXiv:2605.22842, arXiv:2607.29167).
6. **Adaptive-attacker evaluation of defenses is rare** [med-high]. CAPTURE shows poisoning success roughly doubles, from 11.5% to 24.7% (arXiv:2609.02265). Collusive and weak-signal attacks (arXiv:2608.01637, arXiv:2606.04329) beat detectors, but most defenses are not tested against them.
7. **Preference drift vs manipulation** [med]. There is one paper (arXiv:2609.02265). This maps directly to suitability and risk-profile updates in advice, so it is a natural finance angle.
8. **Storage ≠ execution metrics** [med]. Evaluations often report injection success; arXiv:2605.08442 shows it is uncorrelated with execution. Governance metrics should score action-level harm and dollar impact, and arXiv:2608.24069 shows ASR and dollar impact also decouple.
9. **Benchmark proliferation without a shared harness** [med]. Five lifecycle benchmarks appeared in about three months (2026-07 to 09). A contribution now needs a regulatory-requirement mapping, not just another benchmark, or it will be marginal. This agrees with the survey's "no full-lifecycle benchmark" claim (arXiv:2604.16548), though that claim is now weakening.
10. **Where the literature disagrees**:
    - MINJA's high ASR (arXiv:2503.03704) drops sharply once memory holds realistic legitimate records (arXiv:2601.05504).
    - Write-time filtering looks "free" on benign traffic (arXiv:2609.22818) but ineffective against execution (arXiv:2605.08442) and laundering (arXiv:2606.24322).
    - Admission-time filters are provably bypassable by coordinated poisoning (arXiv:2608.16044).
    - The practical answer seems to be authority-at-action (origin-bound gates) plus retrieval-time validity, not content detection. This is my synthesis, confidence medium.

**Key groups visible:**
- Zhen Xiang / Jiliang Tang / Pengfei He (MINJA, MEXTRA).
- Bo Li / Dawn Song / Chaowei Xiao (AgentPoison).
- Mireshghallah / Chaudhuri et al. at Meta/Google (CIMemories, ConfAIde).
- Jinyuan Jia / Neil Gong lines on RAG poisoning (PoisonedRAG, UniC-RAG).
- Industry: Microsoft Defender/AIRT, Palo Alto Unit 42, Cisco (OWASP ASI06 lead), Zenity (with MITRE ATLAS), FINOS.

**Industry vs academia.** Industry frames memory poisoning as an operational control problem (write governance, versioning and rollback, isolation, telemetry: Microsoft Learn, FINOS). Academia focuses on attack optimization and detector accuracy. Industry reports actual abuse (Microsoft 2026-02) that academia has not studied as a measurement problem.

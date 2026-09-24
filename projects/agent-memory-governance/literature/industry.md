# Industry practice: agent memory governance (products, financial institutions, transfer domains, incidents)

This file merges the industry material from all five scout partials (mechanisms §6, threats §7, evaluation §5, regulation §3, finance-apps §3–4). It was compiled on 2026-09-24. The main review is `review.md`.

**Access date.** Every URL was accessed on **2026-09-24** unless the row says otherwise. Where a fetch failed (403, 404, timeout), the row says so and the content comes from search-result snippets of the official page. Treat those rows as lower confidence.

**Source type labels:**
- **TD**: official technical or product documentation.
- **PR**: institution press release or newsroom item.
- **INS**: institution essay or insight page.
- **VEN**: vendor marketing page or case study.
- **COV**: press coverage.
- **RES**: institution-authored research paper, cited by `papers.jsonl` id.
- **STD**: standards body or industry consortium.
- **REG**: regulator or supervisory publication.
- **SEC-R**: security research blog or disclosure.
- **FIL**: regulatory filing.
- **ORG**: non-profit research organisation page.

Industry claims are not peer reviewed. Vendor statements describe documented behaviour, not verified behaviour.

---

## 1. Memory products and platforms: deletion, retention, isolation, audit

| Product | Memory model | Deletion | Retention | Isolation | Audit | Source (type; accessed) |
|---|---|---|---|---|---|---|
| **Mem0** (platform/OSS) | LLM-extracted facts, with optional graph | Delete by id; batch (≤1000); `delete_all` by user, agent, run or metadata filter; `delete_all` with no filter now raises an error. The docs say this "satisfies user erasure (GDPR/CCPA)". Hard vs soft delete not stated | Not stated on the page | Metadata scoping (`user_id`, `agent_id`, `run_id`). Independent evaluation: access-control violation A = 28.1% in GateMem (arXiv:2606.18829) | Not documented on the delete page | https://docs.mem0.ai/core-concepts/memory-operations/delete (TD; 2026-09-24) |
| **Letta** | MemGPT-style in-context blocks plus archival vector memory | Developers delete archival passages via SDK/API; archival memory is "agent-immutable" | No retention settings documented | "Identities" API exists; scoping not described | Not documented | https://docs.letta.com/guides/agents/archival-memory/ ; https://docs.letta.com/api/resources/agents/subresources/passages/methods/delete (TD; 2026-09-24) |
| **Zep / Graphiti** | Bi-temporal knowledge graph. Superseded facts are *invalidated*, not deleted | Deleting an episode removes edges and nodes only if no other episode references them. It "does not regenerate the names or summaries of nodes shared with other episodes". An invalidated fact stays invalidated after its episode is deleted | Not stated | Per-user graphs | Not documented | https://help.getzep.com/deleting-data-from-the-graph (TD; 2026-09-24) |
| **LangGraph Store / LangMem** | JSON documents under tuple namespaces, with semantic search | `delete(namespace, key)` | TTL not documented on the store page. A MongoDB vendor blog describes TTL indexes (not verified) | Namespaces. `namespace_prefix` matches **by prefix**, a collision risk | Not documented | https://docs.langchain.com/oss/python/langgraph/stores (TD; 2026-09-24) |
| **ChatGPT memory** | Saved memories plus "reference chat history" | Deleting a chat does **not** delete memories derived from it. Turning off chat-history reference schedules deletion within 30 days | Logs of deleted memories may be kept for up to 30 days | Per account | Not described | https://help.openai.com/en/articles/8590148-memory-faq. **Fetch returned HTTP 403; row built from search-result snippets of the official page; re-verify** (TD-snippet; 2026-09-24). Independent audit: over 95% of profile entries are implicitly extracted (arXiv:2609.14697, abstract) |
| **Claude memory** | Per-topic memory entries, with a separate memory space per project | Users view, edit and delete topics. Deleting or expiring a chat does **not** remove memory derived from it. Turning memory off at org level "permanently deletes all memory data". Incognito chats neither read nor write memory | Enterprise retention applies to incognito chats and chat search. Memory is unavailable for HIPAA and custom-retention organisations (mechanisms partial) | Project-separated | Not described | https://support.claude.com/en/articles/11817273 (TD; 2026-09-24) |
| **Gemini app** | Memory learned from past chats ("Personal Intelligence") | "Short delay" before a deleted chat stops being used; toggle off | Not stated | **Not available for work or school accounts** | n/a | https://support.google.com/gemini/answer/16598469 (TD; 2026-09-24) |
| **Microsoft 365 Copilot memory** (preview; page dated 2026-09-02) | Saved memories, inferred chat-history details and custom instructions, stored in a hidden Exchange mailbox folder | Deleting chats removes chat-history traces within 7 days. When an admin turns memory off, chat-history details are deleted after 30 days. Admins can run eDiscovery and delete via Purview and Graph | **Purview retention policies and labels do not apply**. Saved memories are kept until the user deletes them | Mailbox security (Customer Lockbox, encryption at rest). Admins cannot restrict what goes into memory | "**Memory and personalization actions don't generate audit log entries in Purview**" | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory (TD; 2026-09-24) |
| **Microsoft Foundry Agent Service memory** (preview; page dated 2026-06-02) | User-profile, chat-summary and **procedural** memory, with LLM consolidation and conflict resolution | Item-level CRUD; `delete_scope` per user; "remember-or-forget" commands | Store-level default TTL | `scope` (e.g. `{{$userId}}`), which must be set explicitly for low-level APIs. No VNet support | Not described. Recommends Content Safety prompt-injection detection against memory corruption | https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory (TD; 2026-09-24) |
| **AWS Bedrock AgentCore Memory** | Short-term raw events plus long-term records extracted by strategies | `DeleteMemoryRecord` for long-term records | Raw-event expiry up to **365 days**, fixed at write time. Long-term records persist until explicitly deleted | Actor, session and namespace. IAM condition keys `bedrock-agentcore:namespace`/`namespacePath`. A trailing slash is advised to avoid prefix collisions | Via AWS; CloudTrail coverage not checked | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-create-a-memory-store.html (TD; 2026-09-24) |
| **Salesforce Agentforce / Einstein Trust Layer** | Grounding via Data Cloud; no documented long-term agent memory on the page | n/a | Zero-data-retention agreements with LLM providers; masking | "Secure data retrieval" (not detailed) | "Audit trail and feedback", with no detail on the page. The 30-day audit retention cited by third parties is **unverified** | https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html (TD; 2026-09-24) |
| **Pinecone** | Vector index | Delete by id, id prefix or whole namespace (serverless has no delete-by-metadata). Compaction drops deleted records asynchronously (per search snippet) | Not stated | Namespace per tenant; "physical isolation" in serverless | Not documented | https://docs.pinecone.io/guides/index-data/implement-multitenancy (TD; 2026-09-24) |
| **Weaviate** | Vector DB | "Deleting a tenant deletes all associated objects" (the shard is removed). Object-level deletes leave recoverable residue per arXiv:2606.18497 (abstract) | Tenant offload to S3 | One shard per tenant | Not on the page | https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy (TD; 2026-09-24) |
| **Anthropic, Claude for Financial Services** | n/a (product launch) | n/a | Data "not used for training" by default | n/a | "Financial modeling with full audit trails"; no memory detail | https://www.anthropic.com/news/claude-for-financial-services (VEN; 2025-07-15 launch; accessed 2026-09-24) |

**Patterns (synthesis).**
1. Vendors offer **API-level deletion, namespace scoping and TTL**. The academic evidence shows these are insufficient in three ways:
   - residue persists in storage and derived state (arXiv:2606.18497, abstract; arXiv:2609.04875, full; arXiv:2608.20352, full);
   - natural-language deletion is brittle (arXiv:2606.15903, full);
   - read-path scope enforcement is inconsistent (arXiv:2606.24535, full).
2. At least four vendors say **derived memories survive deletion of the source conversation**: ChatGPT (snippet), Claude, M365 Copilot and Zep.
3. **Retention-policy and audit integration for memory is missing** in the most finance-relevant product, M365 Copilot.
4. Memory is **excluded** from HIPAA and custom-retention Claude organisations and from Google work accounts. Our inference is that vendors themselves do not yet consider memory ready for regulated tenants.
5. **Prefix-matching namespaces** (LangGraph, AgentCore) are a documented source of accidental cross-scope reads.

---

## 2. Financial institutions: GenAI and agent deployments and what they disclose about memory

| Institution | System | Date | Memory / retention / audit / oversight disclosures | Source (type; accessed 2026-09-24) |
|---|---|---|---|---|
| Morgan Stanley | AI @ Morgan Stanley Debrief (GPT-4) | 2024-06 | Generates meeting notes **"with client consent"**, drafts an email the FA edits, and **saves a note into Salesforce**. OpenAI zero data retention is cited as key to internal trust | https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch (PR; **fetch timed out, content from search snippet**); https://openai.com/index/morgan-stanley/ (VEN; **403, snippet**) |
| JPMorgan Chase | LLM Suite (OpenAI and Anthropic models), agentic phase | 2025-09 | About 250k staff with access; updated every 8 weeks with business data; goal of "every employee… personalised AI assistant". **No memory or retention disclosure found** | https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html (COV) |
| Goldman Sachs | GS AI Assistant; Devin pilot | 2025-06/07 | Firmwide to about 46.5k staff; Devin under human-developer supervision. No memory disclosure | https://fortune.com/2025/06/24/goldman-sachs-internal-ai-assistant ; https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html (COV) |
| BNY | Eliza; "digital employees" | 2025-10; 2025-12 | "Over 100 digital employees with distinct personas, **credentials and supervisors**". Responsible AI covers data usage, guardrails and continuous oversight. No memory disclosure | https://www.bny.com/corporate/global/en/insights/unlocking-potential-enterprise-ai-platform-bny.html (INS); https://www.googlecloudpresscorner.com/2025-12-08-BNY-Collaborates-with-Google-Cloud-to-Advance-its-Eliza-AI-Platform-with-Gemini-Enterprise (PR) |
| Bank of America | Erica; EricaAssist (employee agent) | 2026-03; 2026-07-21 | Erica: 20.6M users and about 700M interactions in 2025. EricaAssist "recommend[s] next steps based on the employee's role and **the client's relationship with the bank**", with "human oversight, transparency, and accountability". **No retention or memory detail** | https://newsroom.bankofamerica.com/content/newsroom/press-releases/2026/07/bank-of-america-enhances-ericaassist-with-generative-ai-to-help-.html (PR) |
| DBS | CSO Assistant; digibot/Joy agentic | 2024; 2025-10-29; 2026-07-28 | CSO Assistant uses **role-based access**, tailoring answers to user permissions. PURE framework; "audit trails, fallback mechanisms". Agentic features act "solely on instructions initiated by authenticated customers", with escalation to humans. **No conversation-retention disclosure** | https://www.dbs.com/artificial-intelligence-machine-learning/artificial-intelligence/agentic-ai-is-here-are-we-ready-to-govern-it.html (INS); https://www.dbs.com/newsroom/DBS_Gen_AI_enabled_virtual_assistants_reach_10_million_customers_and_go_agentic (PR) |
| HSBC | Gemini Enterprise Agent Platform; internal agents | 2026-06 | Strengthening model-risk, data and technology controls; "human accountability central". No memory disclosure | https://www.theasianbanker.com/updates-and-articles/hsbc-expands-google-cloud-ai-partnership-with-100-million-use-case-threshold ; https://qa-financial.com/hsbc-tightens-controls-as-ai-use-expands/ (COV; **via search snippets**) |
| UBS | Red (Azure OpenAI plus AI Search over about 60k documents) | 2025 | About 90% of FA teams use it; 380 live use cases at end-2025. No memory disclosure | https://www.microsoft.com/en/customers/story/19796-ubs-azure (VEN; **snippet, not fetched**) |
| Ant Group | Maxiaocai AI financial manager; "Ah Bao" Alipay agent | 2024-09; 2026-06 | 70M MAU claimed (Aug 2024); fund purchases "after providing authorization". No memory disclosure | https://www.antgroup.com/en/news-media/press-releases/1725552000000 (PR); https://www.caixinglobal.com/2026-06-17/ant-revamps-alipay-with-ai-assistant-in-biggest-app-overhaul-102454831.html (COV) |
| Ryt Bank (Malaysia) | Ryt AI (in-house ILMU LLM) | 2025-10 | **Stateless, session-bound memory**: all context is discarded at session end. Human Approve/Edit on every transfer; 2FA above RM250. Serves more than 50k users | arXiv:2510.07645 (RES, full) |
| A leading UK bank (per abstract; unnamed) | Customer digital-twin validation of a customer-service chatbot | 2026-05 | Synthetic customer agents grounded in anonymised real conversations and transactions; single-session only; no persistent-memory tests. **The abstract names no bank, so none is named here** | arXiv:2607.26060 (RES, full) |
| Coinbase | SR-Fraud (research) | 2026-09 | Statistically gated, versioned memory writes; stateless decision with gated offline updates; production-stream evaluation | arXiv:2609.27287 (RES, full) |
| Unnamed "global fintech" | Co-Investigator AI for AML/SAR drafting | 2025-09 | Reuses prior approved SARs and typologies as memory; **no access-control, retention or cross-subject leakage analysis** | arXiv:2509.08380 (RES, full) |

**Patterns.**
- Banks disclose *adoption* and *human oversight*. **None of the 10 institutions** (Morgan Stanley, JPMorgan, Goldman, BNY, BofA, DBS, HSBC, UBS, Ant, Ryt) discloses how agent conversation memory is retained, scoped per client or erased.
- Retention statements concern the **model vendor** (zero data retention, "no training"), not the bank's own agent memory.
- The one technical deployment paper from a regulated bank (Ryt) chose **no persistent memory**.

**Sector surveys and adoption signals.**

| Item | Date | Finding | Source (type) |
|---|---|---|---|
| BoE/FCA third AI survey | 2024-11-21 | 118 firms; 75% using AI; about 1/3 of use cases are third-party; only 34% claim "complete understanding" of their AI [S] | https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024 (REG) |
| FSB "Monitoring Adoption of AI…" | 2025-10-10 | Monitoring at an early stage; FIs exploring agentic AI; third-party concentration [S] | https://www.fsb.org/2025/10/monitoring-adoption-of-artificial-intelligence-and-related-vulnerabilities-in-the-financial-sector/ (REG) |
| FINRA 2026 Annual Regulatory Oversight Report | 2025-12 | Member-firm GenAI use is mostly summarisation and information extraction. Agent-specific controls are expected, including "track and log agent actions and decisions". Agents "may unintentionally store… sensitive… information" [V] | https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai (REG) |
| Evident AI Index | 2025 | Only 9 of 50 large banks had documented an agentic use case in pilot or production [S, low confidence] | https://evidentinsights.com/ai-index/ (VEN, analyst) |

---

## 3. Industry and supervisory governance frameworks relevant to agent memory

| Framework | Date | Memory-relevant content | Source (type) |
|---|---|---|---|
| FSB "Sound Practices for Responsible Adoption of AI" (consultation) | 2026-06-10 (comments to 2026-07-22) | Names "memory poisoning". Calls for "enhanced documentation and logging… prompt versioning… chain-of-thought logging", contractual rights where vendors control rollback and configuration, audit trails of agent transactions, kill switches, and review of rubber-stamping [V] | https://www.fsb.org/2026/06/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai-consultation-report/ ; https://www.fsb.org/uploads/P100626.pdf (REG) |
| IOSCO Supervisory Toolkit for AI in Capital Markets (FR/02/2026) | 2026-05-25 | Non-binding lifecycle toolkit covering GenAI and agentic AI [S] | https://www.iosco.org/library/pubdocs/pdf/IOSCOPD823.pdf (REG) |
| FINOS AI Governance Framework v2.0; RI-27 "Agent State Persistence Poisoning" | 2025-11 (v2.0); extension 2025-10 | 46 risks and mitigations including an agentic catalogue. RI-27 gives finance scenarios (transaction-approval bias, loan-risk corruption, fee-waiver manipulation, trading-signal suppression, compliance-override persistence), which are **hypothetical, not incidents**. Mitigations: AIR-PREV-022 isolation and AIR-DET-004 observability | https://air-governance-framework.finos.org/ ; https://air-governance-framework.finos.org/risks/ri-27_agent-state-persistence-poisoning.html ; https://www.finos.org/blog/finos-ai-governance-framework-v2.0-addressing-agentic-ai-risks-in-a-rapidly-evolving-landscape (STD) |
| MAS Project MindForge: AI Risk Management Operationalisation Handbook and Toolkit | Handbook 2026-01; toolkit announced 2026-03-20 | A 24-firm consortium. The MAS PQ reply (2026-08-05) cites a "Safeguards for Agentic Finance at Runtime (SAFR)" framework: agent authorisation, human-oversight activation, decision recording [V PQ; S detail] | https://www.mas.gov.sg/news/media-releases/2026/mas-partners-industry-to-develop-ai-risk-management-toolkit-for-the-financial-sector (REG) |
| MAS proposed Guidelines on AI Risk Management (AIRG) | Consultation 2025-11-13 to 2026-01-31 | Covers agentic AI. **Content on memory unverified**, because consultation PDF extraction failed | https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management (REG) |
| DBS PURE framework (institution) | 2025-10-29 | Role-based access; audit trails; fallback mechanisms | See §2 (INS) |
| SR 26-2 carve-out (practice signal) | 2026-04-17 | US banks must govern GenAI and agents through enterprise risk management, not model-risk management. Expect bank MRM teams to publish their own agent frameworks [V; corroborated by the orchestrator] | https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm (REG) |

Not covered: Big-4 and consultancy frameworks, the IIF/EY survey, and bank MRM white papers. These are worth one `/radar` pass.

---

## 4. Transfer patterns from legal and healthcare

| Pattern | Source domain and evidence | Finance status (our observation) | Source (type; accessed 2026-09-24) |
|---|---|---|---|
| **Ethical walls synced from the system of record into the AI platform.** Block when access cannot be confirmed; log every enforcement event in both systems | Legal: Harvey and Intapp Walls (2026-07-23). The page does **not** say whether memory or history is covered | Banks have information barriers (MNPI, research vs banking), but there is **no public evidence that agent memory inherits barrier policies**. This is the most direct transfer | https://www.harvey.ai/blog/harvey-intapp-ethical-walls (VEN) |
| **Consent and "minimum necessary" as run-time attributes** on every context or memory access, with a cumulative-disclosure risk score | Healthcare: HIPAA agent framework (45 CFR 164.502(b), 164.312(b)) | Finance has purpose limitation (GDPR, GLBA/Reg S-P) but no agent paper enforces it per memory read | arXiv:2504.17669 (RES, full) |
| **Ambient-scribe retention discipline.** Delete raw audio and the interim transcript after the clinician signs the note; patient opt-out. Vendor practice ranges from 60 s to 90 days | Healthcare: ABA Health Law 2026 | Analogous to Debrief-style meeting notes, but finance record-keeping (SEC 17a-4, MiFID II Art. 16(7)) may *require* keeping communications. The conflict is under-studied | americanbar.org (**403 on fetch; content via snippets**) |
| **Architectural enforcement of professional duties**: refuse unauthorised authority; do not learn from client data | Legal: doi:10.5281/zenodo.18110491 (preprint, abstract); confidentiality duties doi:10.1017/s1744552325000047 | Finance guardrail papers enforce *output* constraints, not *memory-write* constraints (arXiv:2604.01483, arXiv:2608.28646) | RES |
| **Memory benchmarks with safety-critical "trap events"**, proxy speakers and streaming checkpoints | Healthcare: MedMemoryBench (arXiv:2605.11814, full, CC BY 4.0) | Finance has FinPerMA only; there is no trap-event analogue (sanctions hit, vulnerability flag, power of attorney, exclusion list) | RES |
| Finance → other domains: model-risk-style change control of memory | Finance: gated, versioned writes (arXiv:2609.27287); deterministic replay from an append-only log (arXiv:2604.20158); provenance and validity metadata (arXiv:2606.01886) | More developed in finance than in clinical papers | RES |

---

## 5. Incidents, disclosures and threat standards

| Item | Date | Status | What happened / content | Source (type; accessed 2026-09-24) |
|---|---|---|---|---|
| Microsoft Defender, "AI Recommendation Poisoning" | 2026-02-10 | **Documented, in the wild** | 31 companies across 14+ industries made 50+ attempts in 60 days, using "Summarize with AI" links that tell the assistant to "remember [Company] as a trusted source". **Finance and crypto sites among them**. The first in-the-wild commercial memory-poisoning report | https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/ (SEC-R) |
| CB Financial Services (Community Bank, PA), 8-K Item 1.05 | 2026-05-11 | **Documented; not agent memory** | An employee put customer SSNs and DOBs into an unapproved AI app; the bank got the vendor to exclude the data from training. This is vendor-side retention of customer data | https://www.americanbanker.com/news/a-bank-breaks-its-silence-on-its-shadow-ai-breach (COV of FIL) |
| Palo Alto Unit 42: Bedrock Agents memory poisoning via session summarisation | 2025-10-09 | **PoC** | Indirect prompt injection persisted into long-term memory | https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/ (SEC-R) |
| Embrace The Red (J. Rehberger): Gemini memory poisoning via delayed tool invocation; earlier ChatGPT SpAIware (2024) | 2025-02-10 | **PoC** | Google rated it low likelihood and low impact | https://embracethered.com/blog/posts/2025/gemini-memory-persistence-prompt-injection/ (SEC-R) |
| OWASP Top 10 for Agentic Applications, **ASI06 Memory & Context Poisoning** | 2025-12-09 | Standard | Uses the Gemini attack as its example. ASI07 (inter-agent comms) and ASI08 (cascading failures) are adjacent | https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/ (STD) |
| OWASP "Memory is a feature…" / MemoryTrap | 2026-05-13 | Standard commentary | Poisoned memory files and hooks in developer workflows | https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface/ (STD) |
| MITRE ATLAS AML.T0080 "AI Agent Context Poisoning" (.000 Memory, .001 Thread); AML.T0070 RAG Poisoning | Reported added 2025-10 | Standard | **The official page returned 404.** The ids were confirmed via Microsoft Learn and CSA | https://atlas.mitre.org/techniques/AML.T0080 (STD; 404) |
| CSA research note: ATLAS agentic gap analysis | 2026-03-27 | Commentary | Argues ATLAS treats memory as in-session manipulation and proposes a separate "Memory Persistence Across Sessions" technique | https://labs.cloudsecurityalliance.org/agentic/csa-research-note-atlas-agentic-gap-analysis-20260327/ (STD) |
| Microsoft Learn Zero Trust AI attack catalogue #4, "AI Memory / Context Poisoning" | ms.date 2026-07-28 | Vendor guidance | Controls: privileged memory writes, schema-bound memory, sanitisation, versioning, rollback, periodic purge, cross-agent isolation, trust scoring. Maps to OWASP LLM01/02/04/08 and ATLAS T0080/T0070 | https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/ai-memory-context-poisoning (TD) |
| NIST CAISI RFI on security of AI agents; AI Agent Standards Initiative | RFI 2026-01-08; initiative 2026-02-17 | Voluntary | **The RFI page was blocked on fetch**, so whether it mentions memory is unknown. See Perplexity's public response, arXiv:2603.12230 | https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative (REG) |

**Bottom line.** No documented incident was found of a financial institution's *agent memory* being poisoned or leaking across clients. The in-the-wild evidence covers consumer assistants, with finance sites among the attackers (Microsoft, 2026-02). The finance scenarios in FINOS RI-27 are hypothetical.

---

## 6. Industry evaluation practice

| Item | Content | Source (type; accessed 2026-09-24) |
|---|---|---|
| Vendor LoCoMo claims | Zep reported 84%; Mem0's re-run got 58.44%; Zep's rebuttal gives 75.14%. A 2026 Mem0 blog lists vendor claims of 88–96%, several disputed. **Not peer reviewed; not comparable** | GitHub getzep/zep-papers issue #5; Zep blog "Is Mem0 really SOTA"; https://mem0.ai/blog/ai-memory-benchmarks-in-2026 (VEN) |
| UK AISI Inspect and inspect_evals | Open-source evaluation framework with 200+ evaluations (GAIA, SWE-bench, Cybench, AgentHarm). **No memory-governance evaluations** as far as the listing shows (not exhaustively checked) | https://inspect.aisi.org.uk/ ; https://github.com/UKGovernmentBEIS/inspect_evals (TD) |
| METR time horizons (TH1.1) | 31 long tasks. A March 2026 correction; measurements above 16 h are flagged unreliable | https://metr.org/time-horizons/ ; https://metr.org/blog/2026-1-29-time-horizon-1-1/ (ORG) |
| NIST AI 600-1; ISO/IEC 42001, 24029 | Measurement actions for provenance, privacy and poisoning resilience. The ISO texts are paywalled and were not read. None defines memory-specific metrics per public scope statements | https://www.nist.gov/itl/ai-risk-management-framework ; https://www.iso.org/standard/42001 (STD) |

**Industry vs academia.** Industry reports recall accuracy, latency and token cost. Academia moved to governance properties in 2026 but works on synthetic data with no deployment evidence. **No vendor publishes erasure-verification or isolation results for its memory product.** Industry frames memory poisoning as an operational control problem (Microsoft Learn, FINOS), whereas academia optimises attacks and detectors.

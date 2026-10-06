# Phase 1B plan: agent-memory threat model → guardrails for Memoria

**Status:** draft for PI iteration (2026-10-06). Planning only, no code yet (per PI).
**Goal:** a finance-specific agent-memory threat taxonomy, mapped to guardrail designs, implemented as a demoable subset on Memoria for a Q4 stakeholder demo, and seeding a Phase-2 paper. Sits under the agent-memory-governance umbrella; the Phase-1A skill-distillation build is one slice of it (skill promotion = threats T6/T8).

> **CONFIDENTIALITY.** This file may name RockAI/Memoria, C1–C33, MVGM and memo metric acronyms — it stays on this machine. The **paper and any web/SciSpace query stay de-branded** (gateway-above-backends, unnamed backend), consistent with the 2026-09-25 publication decision.

## 0. Why this is tractable
Most of the taxonomy already exists and only needs reconciling:
- **Literature:** `literature/partials/threats.md` §2 — T1–T18 classes with stage/adversary(A0–A4)/impact(I,C,A,G), measured attacks (§3a) and defenses with efficacy+cost (§3b); finance readings written.
- **Structure:** `literature/review.md` §2 — 7 operations (Store/Retain/Recall/Share/Modify/Forget/Log) × 7 properties (RR/FR/ISO/INT/PROV/FRESH/UTIL), with finance-obligation marks.
- **PI memo:** interface×actor threat matrix (SSGM framing, arXiv:2603.11768), six intercept points (WRITE/DERIVE/RETRIEVE/USE/RESTRICT/ERASE), C1–C33 controls (P0/P1/P2), ~14 governance metrics paired with utility.
The job is the connective chain: **threat → finance scenario → guardrail (with a measured target) → intercept point → metric → Memoria-fit → demo.** The paper differentiator is **G3: no finance-specific memory threat/eval study exists** — so the contribution is empirically-evaluated guardrails in finance, not the taxonomy.

## 1. Architectural scoping (decisive)
Memoria today = **per-user / per-session; shared memory NOT enabled; it runs consolidation.** So:
- **Current-Memoria threats:** injection, authority collapse (consolidation), revocation/erasure failure, staleness, single-user contextual-integrity.
- **Shared-tier threats (only bite once sharing is on):** collusion/salami, multi-agent inconsistency/propagation, cross-client leakage, cross-client contagion.
Stakeholder framing for the shared-tier set: **"what breaks the day we enable shared memory → guardrails needed first."** Aligns with the memo's "biggest decision = internal vs platform."

## 2. The key artifact — threat → guardrail → intercept → metric
Guardrail "→target" numbers are the literature defense's reported efficacy (re-verify vs PDF before quoting). Metric column pairs a known literature metric with the memo metric to cross-walk (exact C## and metric expansions to be confirmed against memo §6(a)/§15 — not guessed here).

| Threat (taxonomy) | Finance example | Guardrail (defense → target) | Intercept | Metric (lit → memo xwalk) | Memoria-fit | Demo |
|---|---|---|---|---|---|---|
| **Memory injection** T1/T2 (MINJA 2503.03704; MAFIA 2608.03844; InjecMEM 2608.23471) | seeded "fact"/instruction in an advisor copilot | write-time origin-binding + act gate (TMA-NM 2606.24322 → 0% ASR); note content-filters fail on laundering/coordinated (2608.16044) | WRITE / USE | ASR + utility pairing → INT metric | **Current** | **Ready** (MINJA repo `dsh3n77/MINJA` + toy harness) |
| **Authority collapse** (consolidation) (AuthMem-Bench 2608.01679; Authorization Laundering 2609.01836) | advice-only/restricted fact consolidated into an authoritative rule, used beyond permitted scope | carry source-authority + authorized-use constraint through consolidation; authority-at-action check | DERIVE / USE | authority-preservation (AuthMem-Bench) → ACR(memo) | **Current** (robust: 48/49) | Reimplement-easy; **highest internal relevance** |
| **Revocation / deletion failure** T16 (revoked-facts 2609.08258; exec-state residue 2609.04875; MemLeak 2606.29788) | GDPR erasure / withdrawn advice still acted on | retrieval-time validity filter (unsafe 44%→0%); selective-replay unlearning (0 leakage); tombstone + journal replay | RESTRICT / ERASE | Deletion-Recovery-Leakage, FRR, TTE (memo); unsafe-action rate (lit) | **Current** | **Ready-ish** (repro across Graphiti/Zep/Mem0/LangMem/cognee) |
| **Staleness / authority-over-recency** T14/T15 (MemRiskBench 2609.14976; temporal validity 2606.26511; CAPTURE 2609.02265) | stale KYC / superseded risk limit applied | validity/authority filter; recency≠authority (memo Principle 20); adaptive-attacker test (CAPTURE: 11.5%→24.7%) | RETRIEVE | freshness/validity → FRESH; `last_retrieved_at` metadata | **Current** | Reimplement |
| **Contextual-integrity / cross-client leakage** T12/T13 (CIMemories 2511.14937; MemClaw 2606.24535; AIM/MUMBench 2609.12320) | information-barrier (Chinese-wall) breach | authorization-before-context (2608.17148); CI filter (PrivacyChecker 33%→8%); physical partition for hard scopes | RETRIEVE | attribute-violation rate (lit) → CSLR, Restriction-Escape (memo) → ISO | Current (cross-context) + **Shared-tier** (cross-client) | Ready-ish (CIMemories) |
| **Collusion / salami** T5 (Salami/MemCollusion 2608.01637; Coverage≠Containment 2608.16044) | individually-benign notes that jointly justify a policy exception | composition-aware admission + k-distinct-source gate; note admission-filters provably bypassable | WRITE / DERIVE | save-rate/ASR under dilution → INT | **Shared-tier** | Reimplement (OpenClaw scenarios) |
| **Multi-agent shared-memory inconsistency / propagation** T8 (MAPLE-Guard 2608.00426; Misattribution Gap 2605.22842; finance: Poisoning Agentic Alpha 2608.24069, Contagion-Trading-Floor 2609.19789) | research-desk bias contaminating a trading/risk agent | memory-link enforcement + cross-agent promotion gate (MAPLE-Guard 38%→0.9%) | SHARE | propagation ASR; misattribution rate → PROV/ISO | **Shared / multi-agent tier** | Reimplement (MAPLE-Guard best-specified) |
| **Contagion via consolidation** (Memory Contagion 2606.23195) | evaluator bias propagating through consolidated memory | diff-and-approve consolidation; bias monitor | DERIVE | contagion rate → consolidation-review metric | Current (consolidation) | ⚠️ **Weak live** — see §4 |
| **Audit-log / provenance integrity** T18/T9 (mechanisms: 2609.01931, 2608.02843; laundering: 2605.22842, 2607.29167) | books-and-records evidentiary value; "client instruction" origin lost | signed/append-only mutation log; lineage-at-write | LOG / all | lineage-completeness → MLC, GLO, EPC, PVR (memo) | **Current** (cross-cutting) | Reimplement |

Full T1–T18 and all defenses: `literature/partials/threats.md`. Exact C## and memo-metric expansions: cross-walk against memo §6(a)/§15 (follow-up; see §7).

## 3. Vendor practice: baseline-to-adopt vs gap-to-own
Source: `literature/industry.md` §1 (accessed 2026-09-24; some rows carry re-verify flags).

**Baseline to adopt (vendors ship it; reuse at the gateway):**
- Deletion APIs by id/scope (Mem0, AgentCore, Foundry, Letta, LangGraph, Pinecone/Weaviate).
- Namespace/scope isolation metadata (Mem0 user/agent/run; AgentCore actor/session/namespace + IAM; Foundry `scope`).
- TTL / retention primitives (AgentCore ≤365d; Foundry store-TTL).
- Encryption + infra access control (M365 mailbox/Lockbox; AgentCore IAM); PII masking (Salesforce Trust Layer).
- Control checklist to implement: **Microsoft Zero Trust AI catalog #4** (privileged writes, schema-bound memory, sanitization, versioning, rollback, periodic purge, cross-agent isolation, trust scoring).

**Gap to own (the gateway's job; vendors don't ship it):**
- **Memory-op audit logging** — absent almost everywhere; M365 memory generates *no* Purview audit entries and sits outside Purview retention. → our LOG plane.
- **Verified + propagated erasure** — ChatGPT/Claude/M365/Zep: derived memories survive source deletion; residue recoverable. → RESTRICT/ERASE plane, T16 guardrail.
- **Information barriers** — shipped only in legal (Harvey+Intapp Walls: enforce at retrieve/context/output, matter-centric isolation). Not in any finance memory product. → ISO plane, T12/13 guardrail.
- **Real isolation** — namespace prefix-collisions (LangGraph, AgentCore warnings); 28.1% access-control violation measured on Mem0-style scoping (GateMem 2606.18829). "Hard barriers need physical partitioning" (memo). → ISO plane.
- **Write-path poisoning defense** — vendors punt to generic content-safety. → WRITE plane, T1–T3 guardrail.
- **Tell:** vendors gate memory *off* for regulated tenants (Claude: no HIPAA/custom-retention orgs; Gemini: no work/school). They don't consider it ready for your environment — which is the whole opportunity.

## 4. Caveats
- **Contagion may not reproduce.** Ingest note caught the memo overstated Memory Contagion (2606.23195): it fired only for *length* bias on *older* models; newer models (incl. Claude) immune; authority bias 0/15. → keep as a **monitored-risk metric**, not a hero demo. **Authority collapse (48/49) is the robust one to lead with.**
- **Shared-tier threats need a shared store** Memoria doesn't have yet → demo on a shared-scope stand-in, or frame as pre-sharing risk.
- Vendor rows are as of 2026-09-24; optional `/radar` refresh before lock.

## 5. Recommended Q4 demo cut (PI to confirm)
**Front line (current-Memoria, robust, finance-clear, ready/easy):**
1. Memory injection (ready code) — "someone poisoned the copilot."
2. Authority collapse (reimplement-easy, highest internal relevance).
3. Revocation/erasure failure (multi-backend repro) — GDPR "data comes back."
4. Cross-client / info-barrier leakage (CIMemories) — RIA-confidentiality hero.

**Second segment:** collusion + multi-agent as "what breaks when we enable shared memory" (needs a shared-scope stand-in).
**Caveat slide:** contagion as a measured, model-dependent risk.

**Demo structure (every threat, three beats):** run attack → guardrail blocks it → **show utility / over-blocking cost** (the memo's "nobody measures over-blocking").

## 6. Open decisions (PI)
1. **Demo substrate:** prototype guardrails on open backends (Graphiti/Mem0 — where repros run) then port to Memoria [working default], or straight at Memoria?
2. **Cut:** the 4-up front line [working default], or promote collusion/multi-agent into the headline (commits us to a shared-memory stand-in)?
3. **Phase-1A (skill distillation) vs 1B (this):** parallel (shared gateway/harness) or sequence? Both are Q4.

## 7. Next steps
1. (quick) Cross-walk the table's threats to exact **C## controls and memo metrics** by reading memo §6(a)/§15 — completes the "guide guardrail design for Memoria" ask.
2. (optional) `/radar` to refresh vendor rows + catch last-2-weeks papers.
3. On PI sign-off of the cut + substrate → `/design-experiments` to pre-register the demo (attacks, guardrails, metrics, utility pairing) before any build.

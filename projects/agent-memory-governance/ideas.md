# Research ideas: governance of LLM-agent memory and promoted skills in regulated finance (RIA context)

> **CONFIDENTIAL. Stays on this machine.** This file develops and compares ideas with the PI's internal (proposed, unimplemented) governance framework, referred to as "the PI design" and by control number (C#) only. Its text and names were never used in an external query. Before any part is shared, strip every "PI seed" note and every C# reference.

- **Stage:** 3, `/ideate` step 2 (ideator). **Date:** 2026-09-25.
- **No scores and no ranking.** Survivors are numbered I1–I9 in the order they were written, not by merit. The tournament (step 3) ranks them.
- **Inputs read:** `brief.md`; `STATE.md` (incl. PI answers of 2026-09-25); `gaps.md` in full (incl. both adversarial reviews and the programme critique); `literature/partials/skills.md` in full; `literature/review.md` §1, §2.2, §8; `regulation.md` §2, §6; `evaluation.md` §3–4; `inputs/INDEX.md` in full; notes for arXiv:2604.08377, 2608.05563, 2608.03509, 2608.03700, 2605.07242, 2608.08264, 2606.03143, 2608.17684, 2512.23760, 2609.25563, 2608.12476, 2609.08258, 2609.22086, 2609.27287, 2607.05318, 2606.10062.
- **New full-text reads this stage** (arXiv HTML via fetch tool, extracted summary, so "full" in the sense of `skills.md`): FinSkillOps (arXiv:2609.19680), restore-counterfactual eviction audit (arXiv:2609.08279), Forgetful-but-Faithful / FiFA (arXiv:2512.12856), AIReg-Bench (arXiv:2510.01474), data minimisation for prompts (arXiv:2510.03662). Abstract only: arXiv:2609.01519, 2609.06815, 2609.26242, 2607.13070, 2512.11907, 2605.11946, 2609.20455.
- **Checks run:** 33 arXiv queries (`--since 2025-09-01`, each run with both `--sort relevance` and `--sort date`); 5 SciSpace questions; 8 WebSearch queries (plus 2 for ICAIF facts). 13 new records added with `--tag ideation-check` (library now 894). No `inputs/` content or PI-design terms in any external query; queries used generic public phrasing only.
- **Evidence labels:** as in `gaps.md`: **full**, **abstract**, **[M]** background legal knowledge, check with counsel.

---

## 0. What changed since `gaps.md`, and the design rules every idea must obey

**Changed facts (PI, 2026-09-25).**
1. The PI design is a **proposal** (nothing implemented). It is a seed source and open design space, not prior art. Its ideas (gateway over swappable backends, metadata contract, 9-state lifecycle, admission gates with canaries, utility-paired metrics, "authority not recency", compliance-aware promotion under dual control) may be developed and published in de-branded form.
2. The in-house memory, **Memoria (arXiv:2512.12686, public)**, is per-user, per-session: no shared memory. So the realistic place where one client's data meets another client is **not** a shared fact store (GP2 as written) but **derived artifacts that are shared by design**: procedural memory promoted to skills reused across users and clients. This moves the centre of gravity of the programme to N4' (= GP2 ∩ GP4 on derived skills).
3. RIA, **probably no MNPI barriers**: GP2' = client confidentiality and need-to-know.
4. Legal classification is **unknown pending specialists** (is a memory item or a promoted skill a 204-2 record, e.g. a 204-2(a)(17) "policies and procedures" copy? does 17(3)(b) apply?). EU (GDPR, AMLR Art. 77, MiFID II), UK and California are reference regimes alongside US.
5. Venue likely ICAIF. API LLMs only (no key yet); public/synthetic data by default; approved pilot traces possible later.

**ICAIF format facts (checked 2026-09-25).**
- ICAIF '26 (Milan): paper deadline **2026-08-02, extended to 2026-08-09**; notification 2026-09-27; main conference 2026-11-16/17; **workshop paper submission 2026-10-01**; limit **8 pages total incl. figures and references**, two-column ACM template, **double-blind**, **no supplementary material or appendices accepted**. Topics include "trustworthy and responsible AI in finance … security, and privacy", "AI governance, computational regulation, and compliance", "AI agents and multi-agent systems". Sources: https://icaif2026.org/call-for-papers.html and https://icaif2026.org/important-dates.html (accessed 2026-09-25).
- ICAIF '25 (Singapore): deadline 2025-07-18, 8 pages, notification 2025-09-26 (https://icaif25.org/calls-for-papers/, accessed 2026-09-25).
- **Implication.** The main-track target is realistically **ICAIF '27, deadline probably mid-July to early August 2027** (extrapolated from two years; speculation, confirm when the CFP appears). The ICAIF '26 **workshop** deadline (2026-10-01) is 6 days away, too soon for any empirical idea here. The 8-page, no-appendix limit favours **one sharp question per paper**; a benchmark-of-everything will not fit. Programme ideas must be sliceable.

**Design rules applied to every survivor (from the adversarial reviews).**
- **R-law (policy-configurable legal ground truth).** No idea hinges on one legal reading. Record classes, retention periods, hold and erasure semantics live in a declarative **policy file**; experiments run under ≥2 readings (e.g. "skill = 204-2(a)(17) procedure, retain 5y" vs "skill = derived cache, purge"; EU-controller vs US-only). The claim tested is *conformance to a declared policy*, plus *how outcomes change across policies*; legal correctness of each policy is delegated to counsel.
- **R-label (independent labels).** Deterministic oracles first (canaries, lineage ids, state checks). Where judgment is needed, labels come from people outside the mechanism design (compliance staff or a law-student panel), with agreement reported, and a counsel-adjudicated subset.
- **R-baseline (fair, strong baselines).** Never compare only against OSS backends that have no retention concept. Always include (a) the strongest published mechanism for the property, (b) a naive-but-reasonable engineering baseline (per-client partitioning; cache-over-archive purge by lineage id), and (c) "no sharing / stateless".
- **R-measure.** Prefer framing as a measurement or characterisation study where a mechanism would pass by construction.
- **R-scoop.** Position explicitly against AkasicMEM (arXiv:2609.25563), GPM (arXiv:2608.12476), MemoRepair (arXiv:2605.07242), OBLIVION (arXiv:2608.08264), PiSAs (arXiv:2607.05318).

---

## 1. Divergence: gap × strategy grid (raw ideas R1–R24)

Rows are the gaps in scope; columns are the ideator strategies. "PI seed" marks ideas taken directly from the PI design or the PI's stated open questions (`inputs/INDEX.md` §6(d)).

| Gap ↓ / Strategy → | Invert an assumption | Combine two methods | Import from another field | Change unit of analysis | New benchmark / evaluation | Theory for an empirical puzzle | Scale up / down | Make it cheaper | Real deployment constraint | Negative result worth proving |
|---|---|---|---|---|---|---|---|---|---|---|
| **N4' governed skill promotion** | R4 skills as retained procedure records, evidence erasable | **R1** support-counting gate: one k-distinct-client invariant for privacy + Sybil + erasure (PI seed: compliance-aware promotion, PROMOTE dual control) | R3 SISA-style sharded skill derivation for exact partial erasure (from ML unlearning) | R14 the shared skill, not the shared fact store, is the cross-client channel | **R2** cross-client leakage + post-erasure persistence benchmark for skill pipelines | R24 formal support/leakage bound for k-client promotion | R20 harm-regression gate on e-banking tasks at more lineages | R5 LLM pre-screen to cut maker-checker review hours with bounded miss rate | R5 (same) | R6 "sanitisation prompts do not anonymise procedures" |
| **GP2' client confidentiality** | — (folded into R14) | R15 deterministic composition canaries + Brewer–Nash history | R15 (DB inference control) | R14 | R15 | — | — | — | per-client partitioning baseline (rule R-baseline) | — |
| **GP4 derived-artifact erasure** | R9 "rebuild = erase" is false: resurrection paths | R3 | R3 | R9 skill re-derivation as a resurrection path | R9 | — | — | — | backup/restore on local stacks only | R9 |
| **GP1 retain + erase + hold** | R7 memory as purgeable derivative of the archive (reviewer's reframe) | R4 + R7 | records management (retain-then-delete, AMLR 77) | R4 (skill level) | **R8** policy-parameterised retention/erasure conformance (PI seed: lifecycle states, metadata contract) | — | — | R7 naive cache-over-archive baseline | R8 regimes as config | R7 "if naive baseline passes, GP1 is a checklist" |
| **GP7 backend-agnostic contract** | — | R10 mutation testing + differential testing | software-engineering mutation analysis | R11 migration events as the unit | R10 (PI seed: gateway, 9 admission gates, canaries) | — | — | — | R11 model/embedder upgrade | — |
| **GP5 utility cost** | R12 cost = governance-induced *harm*, not lost accuracy (PI seed: FRR, utility pairing, "authority not recency") | R12 + stateless replay from archive | clinical equivalence trials (TOST) | R12 per-decision suitability | R12 | R13 empty-store degenerate optimum, formalised (PI seed) | — | — | stateless is what regulated industry ships | R13 |
| **GP6 lineage / audit** | — | R17 lineage coverage validated by leave-one-out (PI seed: lineage coverage) | — | R17 skill lineage | R17 | — | — | — | R21 symbolic-retrieval vs logged-probabilistic auditability (PI seed) | — |
| **GP9 minimisation** | R18 necessity = counterfactual utility (PI seed: governed write policy; margin question) | R18 + Memory Worth | data minimisation for prompts | R18 per memory item | — | — | — | — | — | — |
| **Cross-cutting: construct validity** | R19 "compliance" labels are policy- and annotator-dependent | — | legal annotation practice (expert panels, α) | R19 | **R19** | — | — | — | counsel availability | R19 |
| **GP3 / GP8 (remnants)** | R16 finance authority lattice in consolidation (PI seed "authority not recency") | — | — | — | — | — | — | — | — | — |
| **PI seeds with no gap row** | R22 certified graph unlearning on a bitemporal KG (PI seed) | — | — | — | — | — | — | — | — | R23 drift/bias-contagion observability (PI seed) |

**Empty cells.** Theory is almost empty: only R13 and R24 (no formal bound exists anywhere for leakage through LLM-written procedures, and one would be weak). Scale-up is thin: the one scale idea (R20) is incremental. "Make it cheaper" has only R5 and R7. GP2' has few independent ideas because, after the Memoria fact, it collapses into the skills channel (R14). GP3/GP8 produced only R16, which AuthMem-Bench (arXiv:2608.01679) largely pre-empts.

**Near-duplicates.** R2 ≈ R6 (same measurement; R6 is its expected finding). R14 ≈ R1/R2 (framing, not a separate study). R9 ≈ R7 (resurrection is an axis of the purgeable-derivative study). R10 ≈ R11 (migration is the most interesting mutation class). R4 ⊂ R1 in mechanism but distinct in question (retention side). R20 ⊂ R1 (harm regression is one gate axis). R17 overlaps R1 (lineage completeness is R1's binding constraint).

**Raw list (one line each).**
- **R1** (PI seed) Support-counting promotion: promote a candidate skill only if supported by traces from ≥k distinct clients (distinct client relationships, not sessions), with lineage to each contributing trace; erasure of client i decrements support and triggers demotion or re-derivation; the same count doubles as Sybil resistance.
- **R2** Measure cross-client leakage (planted canaries and finance attributes) and post-erasure persistence in existing open skill-evolution pipelines.
- **R3** Exact partial erasure for multi-client skills via sharded derivation (SISA analogue), with a counterfactual "derived-without-i" oracle.
- **R4** Split each promoted skill into a client-free procedure (retainable as a versioned procedure under one legal reading) and an erasable evidence side-store; test separation and audit reconstruction after erasure.
- **R5** Maker-checker cost of promotion: can an LLM pre-screen reduce human review hours with a bounded miss rate?
- **R6** Negative result: sanitisation prompts leave client specifics in procedures.
- **R7** Is agent memory a provably purgeable derivative of the regulated archive? (archive coverage, sole-carrier rate, purge completeness).
- **R8** (PI seed) Policy-parameterised retention/erasure/hold conformance benchmark.
- **R9** Resurrection paths: re-ingest, re-index, restore, embedder migration, consolidation replay, skill re-derivation.
- **R10** (PI seed) Mutation-scored conformance suite for a backend-agnostic governance contract.
- **R11** Do restrictions and erasures survive model/embedder/index migration?
- **R12** (PI seed) Governance-induced suitability failures vs stateless replay from archive, with equivalence testing.
- **R13** (PI seed) Formalise the empty-store degenerate optimum; show single-ratio dashboards reorder systems.
- **R14** Reframe cross-client confidentiality around shared skills.
- **R15** Deterministic composition canaries + history-dependent access in shared advisory memory.
- **R16** (PI seed) Authority-lattice-aware reconciliation for advisory memory.
- **R17** (PI seed) Validate lineage coverage by leave-one-memory-out ablation.
- **R18** (PI seed) Necessity as counterfactual utility for memory writes.
- **R19** Construct validity of compliance labels across legal readings and annotators.
- **R20** Harm-regression-bounded promotion gate on simulated banking tasks.
- **R21** (PI seed) Auditable-by-construction symbolic retrieval vs logging over probabilistic retrieval.
- **R22** (PI seed) Certified graph unlearning on a bitemporal KG.
- **R23** (PI seed) Drift and bias-contagion observability.
- **R24** Formal leakage bound for k-client promotion.

---

## 2. Convergence: clusters → survivors

| Survivor | Built from | Gap(s) | Kind | PI seed? |
|---|---|---|---|---|
| **I1** Support-counted, lineage-bound promotion of multi-client traces to shared skills | R1, R14, R20, R17, R24 (as a stated limitation) | N4' (= GP2' ∩ GP4 on skills), GP6 | **Programme-level anchor** (mechanism + measurement), ICAIF main track | **Yes** (compliance-aware promotion; PROMOTE under dual control; gateway; metadata contract) |
| **I2** "Do promoted skills remember clients?" leakage and post-erasure persistence in skill-evolution pipelines | R2, R6 | N4', GP2', GP4 | **Small, fast, low-risk** measurement paper | No (enables the PI seed) |
| **I3** Exact partial-contribution erasure for multi-client skills | R3, R9 (skill slice) | GP4 on skills | Mechanism + evaluation | Partly (erasure propagation control) |
| **I4** Retain the procedure, erase the client: retention-compatible erasure at skill level | R4, R8 (skill slice) | GP1 ∩ N4' | Measurement + design pattern, policy-configurable | **Yes** ("restricted is not deleted"; lifecycle states; record-level retention) |
| **I5** Purgeable-derivative memory and resurrection paths | R7, R9 | GP1 (reframed), GP4 | Measurement study; naive-baseline-first kill test | Partly (erasure verification, recovery-after-restore) |
| **I6** Mutation-scored conformance for a backend-agnostic governance contract under migration | R10, R11 | GP7 | Conformance suite + empirical study | **Yes** (gateway over swappable backends; admission gates; canaries) |
| **I7** Governance-induced suitability failures vs stateless replay | R12, R13, R16 (as a failure class) | GP5, GP8 remnant | Empirical study, equivalence-tested | **Yes** (false-restriction and utility pairing; "authority not recency"; empty-store optimum) |
| **I8** Whose compliance? Construct validity of memory-governance labels across legal readings and annotators | R19, R8 | Cross-cutting (the programme's biggest threat) | Measurement study + labelled resource | Partly (metadata contract fields as label schema) |
| **I9** Necessity as counterfactual utility for advisory memory writes | R18 | GP9 | Formal definition + measurement | **Yes** (governed write policy; "how to quantify necessary") |

At least one programme-level idea (I1) and at least one small, fast, low-risk paper (I2; I8 is a second candidate) are present.

---

## 3. Survivors

### I1. Support-counted, lineage-bound promotion: governing the step where one client's data becomes everyone's skill (programme anchor; PI seed)

**Pitch.** Skill evolution from many users' traces (SkillClaw, Designer-RSI, FederatedSkill; Foundry procedural memory and AgentCore cross-actor reflections in industry) is where per-client data becomes shared. Current promotion gates check only utility, regressions or integrity. We propose and evaluate one **support-counting invariant** that serves three governance purposes at once: a candidate skill is promoted only if (i) it is supported by traces from ≥k *distinct client relationships* with no single client dominating, (ii) every promoted version carries complete lineage to its supporting traces, and (iii) it passes a deterministic client-canary leakage gate. When a client's traces are erased (or expire under the configured policy), support is recomputed: skills that fall below k are demoted and re-derived without that client (I3 supplies the re-derivation). The same count is the Sybil/poisoning control of PoisonedEvolution and a k-anonymity-style privacy floor. The paper measures what this buys and costs against the strongest published gates, on synthetic multi-client advisory workflows, with a regulated-units cost (reviewer load, false rejections).

**Gaps addressed.** N4' (GP2' ∩ GP4 on derived skills: `skills.md` §10 S1, S2, S3, S5); GP6 (lineage completeness as the binding constraint); GP5 (utility/harm pairing of the gate).

**Atomic claims.** (C1, core) A single support-count invariant jointly addresses cross-client leakage, trace poisoning and erasure propagation for shared skills. (C2, core) Measured on multi-client advisory traces: leakage, poisoning, post-erasure persistence and utility/harm under the gate vs strongest baselines. (C3) Finance/regulated setting with policy-configurable legal readings. (C4) Promotion cost in regulated units.

**Searches** (≥3 per claim; generic phrasing): arXiv a1, a2, a3, b2 (both sorts); SciSpace Q1 ("skills… learned from many users' traces… bounding privacy leakage and supporting deletion"); WebSearch "shared agent skills learned from multiple users privacy erasure right to be forgotten"; "k-anonymity threshold promote pattern only if observed across multiple users… sybil poisoning"; "procedural memory learned from customer interactions shared across tenants privacy governance". Plus the 39 queries in `skills.md` §1.

**Overlap table.**

| Claim | Closest paper (id, read level) | Same / partial / different | Evidence |
|---|---|---|---|
| C1 invariant for privacy + integrity + erasure | PoisonedEvolution (arXiv:2608.05563, full) | **partial** | Provenance-diversity gate "requiring three users and clusters, rejects majority dominance" cut embedding 25/25 → 0/25; integrity only, "preliminary", no privacy or erasure reading |
| C1 | FederatedSkill (arXiv:2606.03143, full) | **partial** | Per-client attribution via decision logs; local sanitisation; "no formal guarantee"; no deletion of past contributions |
| C1 | Designer-RSI (arXiv:2609.22086, full) | **different** | k_min = 3 counts *occurrences*, not distinct users; utility gate only; no privacy, provenance or deletion |
| C2 measurement on multi-client traces | SkillClaw (arXiv:2604.08377, full) | **different** | Cross-user sync of skills from 8 users; no privacy, isolation, deletion or provenance (checked in full text) |
| C2 | AntiSkillBench (arXiv:2608.03700, full) | **partial** | Persona-skill leakage 55–66% coverage, but single-user, no cross-client, no k, no erasure |
| C2 | MemoRepair (arXiv:2605.07242, full) | **partial** | Cascade withdrawal on delete (Leak% 0 vs 69.8–94.3%), single agent; "1% missing edges → 17.7% leak"; no multi-client partial removal |
| C3 finance setting | FinSkillOps (arXiv:2609.19680, full, **new**) | **partial** | Finance (SEC-filing QA) skill promotion with zero-regression and false-trigger gates (6/33 promoted); single deployment, **no privacy, cross-client isolation, erasure or regulatory mapping**; expert review route "not staffed" |
| C3 | E-banking self-evolution audit (arXiv:2608.17684, full) | **partial** | Promotion raises unauthorised state change 0.583 → 0.685; no cross-user data, privacy or legal mapping |
| C4 promotion cost | Designer-RSI; FinSkillOps | **partial** | Gate rejection rates (43–49%; 27/33 refused) reported; no reviewer-hours or false-rejection cost in regulated terms |

**Verdict.** Novel at the contribution level on **C1** (no paper connects the count to privacy and erasure; PoisonedEvolution is the only use of ≥k distinct users and is integrity-only) and **C2** in the multi-client-with-erasure form. C3 and C4 are partial (FinSkillOps is new and close on finance governance, but covers none of privacy/erasure). Confidence: medium-high that it is unscooped today; scoop risk medium within 3–6 months (FederatedSkill, MemoRepair and PoisonedEvolution groups each one step away; `skills.md` §10).

**Key experiment sketch.**
- *Data.* Synthetic RIA advisory firm: 100–300 synthetic clients with profiles (risk tolerance, restrictions, holdings, life events) and **per-client high-entropy canaries plus finance-attribute canaries** in traces; 6–10 recurring procedural task families (e.g. rebalancing proposal with restriction check, KYC refresh, fee disclosure preparation, account-transfer checklist) in a tool sandbox with checkable terminal state (AgentDojo-Banking-style, as in arXiv:2608.17684). A small public anchor: run one family on AgentDojo Banking to connect to the e-banking audit.
- *Pipeline.* A SkillClaw-style evolver (open code if licence permits; otherwise re-implemented from the paper) over pooled traces, nightly promotion cycles.
- *Arms / baselines (R-baseline).* (a) SkillClaw utility gate (ungoverned); (b) FinSkillOps-style zero-regression + false-trigger gate; (c) FederatedSkill-style local sanitised distillation; (d) PoisonedEvolution provenance-diversity gate; (e) MemoRepair-style cascade withdrawal on erasure; (f) **per-client skills only (no sharing)**, which is the honest "why share at all?" baseline; (g) the support-counted gate (ours) at k ∈ {1,3,5,10}.
- *Events.* Erasure requests for a random 5–10% of clients; retention expiry under two policy files (R-law); a Sybil attacker contributing 10% of traces via m fake clients.
- *Metrics.* Per-client canary recovery from skill text and from other clients' sessions (deterministic); attribute-inference accuracy; skill embedding rate of poison (SER); post-erasure persistence (share of skills still carrying an erased client's canaries); utility (task success) and harm (unauthorised state change; W→C / C→W flip accounting); gate rejection rate; lineage completeness.
- *Construct validity (R-label).* All primary metrics are deterministic (canaries, sandbox state). Task families and the leakage taxonomy reviewed by compliance staff not involved in gate design; "harm" defined by sandbox state rules written before the gate.

**Minimal publishable result.** On one task family, show a Pareto frontier over k: leakage and SER fall to near zero at some k while utility stays within a pre-registered margin of ungoverned sharing and above per-client-only skills; and show that without lineage, erasure leaves client canaries in X% of promoted skills (with lineage, near zero). A null (k needed for privacy destroys the utility gain of sharing) is also publishable and decision-relevant ("don't share procedural memory across clients").

**What would kill it.** (1) Per-client-only skills match shared skills on utility: then sharing has no business case and the governance question is moot (check early; this is the probe). (2) Utility collapses at any k ≥ 3 because advisory procedures are client-idiosyncratic. (3) Sybil clients defeat the count cheaply in the RIA setting (clients are KYC'd, so Sybils are harder than in open marketplaces: argue and test). (4) A FederatedSkill or MemoRepair follow-up publishes multi-client erasure first.

**Rough cost.** 300 clients × ~20 traces × ~8k tokens ≈ 50M tokens for trace generation and evolution per arm-cycle set; 7 arms × 3 seeds on 1–2 families. With a mid-priced API model at roughly $3 per M blended tokens (speculation; verify at checkpoint 3): **~$300–900**. Time: **8–12 weeks** (sandbox + generator 3 wks, pipelines 3 wks, runs 2 wks, analysis/writing 2–4 wks).

**Feasibility probe (≤1 h, ≤$5).** (a) Check that SkillClaw and FederatedSkill code is public and licensed for research reuse (GitHub search, read licence). (b) With one API model, generate 20 synthetic client traces for one task family with planted canaries, run one distillation step with a SkillClaw-style prompt, and grep the resulting skill for canaries and attributes. (c) Check whether a per-client-only skill for the same family (5 traces) is as good as the pooled one on 10 held-out tasks. Kill signal: pooled ≈ per-client.

**ICAIF fit.** Strong: "trustworthy AI in finance… privacy", "AI governance… compliance", "AI agents". One family + one mechanism + frontier fits 8 pages. Programme: I2 is its measurement precursor, I3 its erasure component, I4 its retention component.

---

### I2. "Do promoted skills remember clients?" Cross-client leakage and post-erasure persistence in skill-evolution pipelines (small, fast, low-risk)

**Pitch.** A measurement paper, no new mechanism. Take 3–4 published trace-to-skill pipelines (SkillClaw-style cross-user evolver, AWM workflow induction, ReasoningBank-style strategy memory, FederatedSkill-style sanitised local distillation) and feed them synthetic multi-client advisory traces with planted per-client canaries and finance attributes. Measure (a) how much client-specific content survives into shared skills (text and behaviour in *other* clients' sessions), (b) whether sanitisation prompts remove it, and (c) how much persists after the source client's traces are deleted. Expected (and itself useful) finding: distillation does not anonymise, and deletion does not propagate.

**Gaps addressed.** N4' (S1, S2, S6 in `skills.md` §10); GP2' (confidentiality through shared artifacts); GP4 (erasure persistence).

**Atomic claims.** (C1, core) First *cross-client* leakage measurement for shared skills built from many clients. (C2, core) Post-erasure persistence of *client data* (not poison) in derived skills. (C3) Finance-attribute canaries; sanitisation as a tested defence.

**Searches.** arXiv b1, b2, b3 (b3 returned nothing), a1; SciSpace Q1; WebSearch "shared agent skills… privacy erasure", "procedural memory… shared across tenants privacy".

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 cross-client leakage | AntiSkillBench (arXiv:2608.03700, full) | **partial** | Measures personal-data coverage in persona skills (55–66%), but **one person's** histories; no cross-user pooling |
| C1 | FederatedSkill (arXiv:2606.03143, full) | **partial** | Empirical privacy audit of skill patches reports no leakage; numbers not visible; "no formal guarantee"; not adversarial per client |
| C1 | PiSAs (arXiv:2607.05318, full) | **partial** | Cross-user spillage via shared *memory* (63–90% visibility violations), not via promoted skills |
| C2 persistence after deletion | SkillJack (arXiv:2608.03509, full) | **partial** | 80% of skill-mediated **attacks** persist after deleting source records; poison, not client data |
| C2 | MemoRepair (arXiv:2605.07242, full) | **partial** | Cascade-unaware systems leak 69.8–94.3% after deletion; single agent, staleness framing |
| C3 sanitisation | RedAct (arXiv:2606.10813, abstract) / AntiSkillBench defences (full) | **partial** | Sanitisation "leaves personality information exposed"; proprietary-skill focus in RedAct |

**Verdict.** Novel on **C1** in the cross-client form and **C2** for client data in pooled skills; every component measurement exists for single-user or poison settings. Confidence: high that no paper measures it today; scoop risk medium (it is the obvious next paper for AntiSkillBench or FederatedSkill authors).

**Key experiment sketch.** Same synthetic client generator as I1 (shared infrastructure). 100 clients, 2 task families, 4 pipelines × {no sanitisation, sanitisation prompt, FederatedSkill-style local distillation} × 3 seeds. Probes: exact canary recovery from skill text (deterministic); behavioural recovery (client B's session elicits client A's canary or attribute) with fixed probe prompts; attribute inference by an attacker model with a pre-registered chance baseline. Deletion: remove 10 clients' traces, re-run the pipeline's normal maintenance cycle (not a full rebuild), re-probe. Baselines: per-client-only skills (leakage 0 by construction, utility reported); full rebuild without deleted clients (persistence 0 by construction, cost reported). Labels are deterministic, so construct validity rests on canary design; include paraphrase canaries (key facts) as a second family, following FRS's stated limitation (arXiv:2606.10062).

**Minimal publishable result.** A table: pipeline × sanitisation → cross-client canary recovery and post-deletion persistence, with CIs. Even "sanitisation reduces verbatim leakage to ~0 but attribute inference stays above chance" is a result.

**What would kill it.** All pipelines already leak ~0% because generalising prompts abstract away specifics (then it becomes a short negative-result note, still informative for the PI's promotion policy). Or a near-identical paper appears (monitor via `/radar`).

**Rough cost.** ~10–20M tokens: **~$50–150** (speculation). **3–5 weeks.**

**Feasibility probe (≤1 h, ≤$5).** Probe (b) of I1 is exactly this probe. Also confirm AWM and ReasoningBank code availability.

**ICAIF fit.** Good as a short empirical paper or an ICAIF '27 workshop paper; stronger as the "motivation" section of I1. Could also target a privacy workshop earlier.

---

### I3. Exact partial-contribution erasure for skills derived from many clients

**Pitch.** When client i asks for erasure, a shared skill built from 40 clients' traces must lose i's influence without discarding the other 39 clients' contributions. MemoRepair withdraws the whole cascade; OBLIVION revokes capabilities. Nobody tests "remove client i, re-derive, compare with a skill that never saw i". We import SISA-style sharding from machine unlearning: derive each skill from client shards and aggregate, so erasure re-derives one shard. We define **partial-erasure fidelity**: the distance between the post-erasure skill and a counterfactual oracle skill derived without i, measured behaviourally on held-out tasks and by canary absence, with the oracle's own sampling variance as the equivalence margin (the evolver is stochastic, so "identical" is the wrong target).

**Gaps addressed.** GP4 on skills; N4' (S2 partial-contribution removal: "None found" in `skills.md` §4).

**Claims.** (C1, core) Partial-contribution removal from a multi-source LLM-authored skill, with a counterfactual-oracle fidelity metric. (C2) Sharded derivation as the mechanism, compared with withdraw-all, full rebuild and LLM "edit-out" of the client's influence. (C3) Cost/latency of erasure in re-derivation calls.

**Searches.** arXiv c1, c2, c3 (both sorts); SciSpace Q2 (deletion propagation to derived artifacts); WebSearch "skill agent unlearning remove one user's contribution from shared skill re-derive counterfactual".

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 | MemoRepair (arXiv:2605.07242, full) | **partial** | Remove/recompute/regen operators on a provenance graph; successor validated before republish; but withdraw-and-rebuild of a *single-agent* cascade, "partial-contribution removal… not modelled" (our note) |
| C1 | OBLIVION (arXiv:2608.08264, full) | **different** | Capability revocation of a whole skill with taint-based anti-re-derivation; no data-subject or partial removal |
| C1 | Temporal unlearning vs exact retraining oracles (arXiv:2609.26242, abstract, **new**) | **partial (method)** | Uses paired retrained-without-period oracles as the unlearning target, for forecasters on market data; not skills or agents |
| C2 | SISA (Bourtoule et al.; not yet in library, background) | **partial (method)** | Sharded exact unlearning for model training; never applied to LLM-authored prose skills |
| C2 | Skill Shapley valuation (arXiv:2608.04562, abstract) / Counterfactual trace auditing (arXiv:2605.11946, abstract, new) | **partial** | Leave-one-out credit for *units of a skill*, not for *contributing clients*; no erasure |

**Verdict.** Novel on **C1** (the problem and metric). The mechanism (C2) is an import, so novelty is in its adaptation to non-parametric, LLM-authored artefacts and the stochastic oracle. Confidence: medium-high unscooped. Risk: reviewers may see it as "just rebuild without i"; the answer is the cost comparison and the fidelity metric.

**Key experiment sketch.** Reuse I1's generator and evolver. Build skills from 20–60 clients; erase 1, 5, 10 clients. Arms: full rebuild (gold, expensive), sharded derivation (s ∈ {4, 8} shards), MemoRepair-style withdraw-and-regenerate, LLM edit-out ("remove anything derived from these traces"), no-op. Metrics: canary absence (deterministic); behavioural distance to oracle on held-out tasks (success-rate difference, TOST against oracle-vs-oracle variance over 5 oracle seeds); utility retained vs no-op; LLM calls per erasure. Sharding's utility cost (skills from fewer traces each) must be reported.

**Minimal publishable result.** Sharded derivation reaches oracle-equivalent fidelity at a fraction of full-rebuild calls, while LLM edit-out leaves measurable residue. Or the negative: edit-out is as good, which simplifies practice.

**What would kill it.** Full rebuild is cheap enough at firm scale (skills are small; nightly rebuild is standard in SkillClaw), making partial erasure a non-problem. Estimate rebuild cost at 10^3–10^4 clients before building.

**Rough cost.** ~$100–300 (speculation), **5–7 weeks**; shares infrastructure with I1.

**Feasibility probe (≤1 h, ≤$5).** Measure oracle variance: derive the same skill 5 times from the same 20 client traces and 5 times without one client; check whether the between-condition difference is detectable above within-condition noise with a feasible number of held-out tasks (if not, the fidelity metric has no power and the idea needs canary-only scoring).

**ICAIF fit.** Medium alone (more ML/privacy); strong as a section of I1.

---

### I4. Retain the procedure, erase the client: retention-compatible erasure at the skill level (PI seed)

**Pitch.** If a promoted skill that encodes a compliance step is a "policy and procedure", one legal reading requires keeping every version for five years (204-2(a)(17)(i) [V per `skills.md`]; counsel unknown), while an EU client's erasure request may reach client data embedded in it. The PI design's "restricted is not deleted" and record-level retention point to a pattern: promote only **client-data-free procedure text** (retainable, versioned, auditable), and keep client-specific evidence (the traces that justified promotion, the ASG-SI-style evidence bundle) in a **separate erasable store linked by pointers**. The research question is empirical, and policy-configurable: *can the split be achieved and verified*, i.e. (a) how much client information remains in the "clean" procedure (residual leakage), (b) whether the promotion decision can still be reconstructed for audit after the evidence of erased clients is purged (audit reconstructability), under ≥2 legal policy files (skill = retained procedure vs skill = purgeable derivative) and 3 regimes (US-only RIA, EU-controller, California).

**Gaps addressed.** GP1 ∩ N4' (`skills.md` S4); GP6 (auditability after erasure); ASG-SI's unresolved tension ("evidence bundles may contain sensitive data… requiring… retention policies").

**Claims.** (C1, core) The retention-vs-erasure tension formulated and measured at the skill level. (C2) A split-artifact pattern with two verifiable properties (residual client content; audit reconstructability after purge). (C3) Outcomes compared across declared legal policies rather than one asserted reading.

**Searches.** arXiv d2, d3 (both empty), a3, c2; SciSpace Q2; WebSearch "shared agent skills… right to be forgotten". Plus `gaps.md` GP1 searches.

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 | GPM (arXiv:2608.12476, full) | **partial** | Public view + separately routed audit view keeps deleted content; "append-only audit and deletion rights remain in tension"; facts, not skills; no retention periods or record classes |
| C1 | ASG-SI (arXiv:2512.23760, full) | **partial** | Evidence bundles and append-only audit for promoted skills; privacy/retention of bundles named but not addressed; no evaluation |
| C2 | FederatedSkill (arXiv:2606.03143, full) | **partial** | Prompts distillation to omit IDs and values (client-free intent) with decision logs; no erasure, no audit-after-purge |
| C3 | AkasicMEM (arXiv:2609.25563, full) | **partial** | §5.1: derived memory inherits most restrictive retention; not evaluated; no multiple legal readings |
| C3 | Forgetful-but-Faithful (arXiv:2512.12856, full, **new**) | **different** | Policy-driven forgetting with audit trail and provenance; single agent; "does not model conflicting retention requirements… legal holds" |

**Verdict.** Novel on **C1** (skill-level formulation, no paper) and **C3** (policy-parameterised comparison). C2 is a design pattern whose parts exist. Confidence: medium. Main risk is importance, not novelty: if counsel says skills are not records, half of the tension disappears, which is exactly why the result is reported per policy.

**Key experiment sketch.** On I1's promoted skills: (a) residual client content in the procedure after "clean-room" promotion (canaries, attribute inference; deterministic); (b) purge the evidence store for erased clients, then have an independent reviewer (and a scripted checker) try to answer fixed audit questions ("why was v3 promoted? which checks passed? which clients supported it?") from what remains, under each policy file; (c) count policy conflicts (items both must-retain and must-erase) per regime. Baselines: keep-everything (audit perfect, erasure fails), purge-everything (erasure perfect, audit fails), GPM-style restricted audit view.

**Minimal publishable result.** The per-policy conflict table plus residual-leakage and audit-reconstructability numbers for the split pattern vs the three baselines.

**What would kill it.** Counsel and compliance reviewers agree that promoted skills are neither records nor personal data once cleaned, making the tension empty; or residual leakage in "clean" procedures is irreducible (then the pattern fails and the finding becomes "do not promote client-derived procedures under EU clients").

**Rough cost.** Marginal on I1: ~$50–100; **3–4 weeks** incl. reviewer time (reviewer hours are the scarce resource).

**Feasibility probe (≤1 h, ≤$5).** Draft two policy files (YAML) and 10 audit questions; ask the PI's compliance contact whether the questions are the ones an examiner would ask (no API cost).

**ICAIF fit.** Good for the governance/compliance topic; best as a section of I1 or a short companion; the law-and-tech angle could go to a CSLAW/FAccT-type venue.

---

### I5. Is agent memory a purgeable derivative of the regulated archive? Purge completeness and resurrection paths

**Pitch.** The reviewer's reframing of GP1: industry practice for RIAs is "archive the communication, treat AI memory as derived". If that holds, retention-vs-erasure dissolves at the memory layer, *provided* (a) every memory item has an archived original (archive coverage), (b) purge on erasure/expiry reaches all derived tiers, and (c) nothing resurrects the purged item when the archive is re-ingested, the index is rebuilt, a backup is restored, the embedder is migrated, or skills are re-derived. We measure these on open backends plus a Memoria-like per-user summary + KG design (public paper), **starting with the naive baseline** "purge by lineage id over a cache of the archive". If it passes, GP1 is a checklist and we say so (a negative result worth publishing briefly); if it fails on resurrection or sole-carrier items, we have the finding.

**Gaps addressed.** GP1 (reframed), GP4 (resurrection), GP5 (stateless replay arm).

**Claims.** (C1, core) Resurrection of purged personal data via re-ingest/re-index/restore/migration/re-derivation in agent memory stacks. (C2, core) Sole-carrier rate: fraction of memory items with no archived source (the only in-memory must-retain obligation). (C3) Policy-configurable record classes and regimes.

**Searches.** arXiv d1, d2, d3, e3/e6/e8 (several empty); SciSpace Q2; WebSearch "agent memory deletion resurrected after reindex backup restore re-ingestion".

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 | OBLIVION (arXiv:2608.08264, full) | **partial** | Resurrection of *revoked skills* from residual carriers (ASR 1.0 undefended); capability, not personal data; no archive re-ingest or backup restore |
| C1 | FRS (arXiv:2606.10062, full) | **partial** | Derived-tier residue after deletion modes; text surface only; no re-ingest/restore |
| C1 | Ghost Echoes (arXiv:2608.20352, full) | **partial** | Index rebuild does not remove drift; one backend; no re-ingest path |
| C1 | Restore-counterfactual audit (arXiv:2609.08279, full, **new**) | **different** | "Restore" means reinstating evicted evidence to diagnose capacity eviction; no erasure or resurrection |
| C2 | (none found) | **different** | No paper measures archive coverage or sole-carrier items in agent memory |
| C3 | GPM (arXiv:2608.12476, full) | **partial** | Deletion barrier + audit view; whole-user deletion; disclaims backup and media erasure |

Industry signal (web, not peer reviewed, accessed 2026-09-25): practitioner blogs and GitHub issues report deleted items returning via retry queues, backups and rebuild jobs (e.g. digitalapplied.com "Deleting AI Agent Memory: Where Stored Copies Survive"; holon-run/holon issue #3145). This supports plausibility, not evidence.

**Verdict.** Novel on **C1** (resurrection of personal data through archive/index/restore/migration paths) and **C2** (sole-carrier measurement). Confidence: medium; GP4 is the fastest-moving area, so scoop risk is high (FRS authors named embedding/cache residue as next).

**Key experiment sketch.** Synthetic RIA client histories with an archive (email/chat store) as system of record; memory built by 3 stacks (Mem0, Graphiti, a Memoria-like summary+KG re-implementation from the public paper; LangGraph store optional). Events: erasure, expiry under two policy files, hold. Resurrection triggers: archive re-ingest, full re-index, backup restore, embedder swap, consolidation replay, skill re-derivation (links to I1). Metrics: archive coverage; sole-carrier rate (items generated from unrecorded channels, e.g. ambient notes, agent inferences); purge completeness per tier (canary + paraphrase probes, FRS-style); resurrection rate per trigger; hold precedence. Arms: vendor-native delete; naive lineage purge (the kill test); lineage purge + tombstone/deny-list at ingest; stateless replay from the archive (no memory at all).

**Minimal publishable result.** A trigger × stack resurrection matrix showing at least one common operational path (re-ingest or restore) resurrects purged data under naive lineage purge, and that an ingest-time tombstone fixes it. Or: naive purge passes everywhere → short negative result ("memory can be a purgeable derivative; here is the checklist").

**What would kill it.** Naive lineage purge + ingest dedup passes all triggers on all stacks (likely outcome for re-index; less likely for restore). Then GP1 collapses to a checklist, as the reviewer predicted.

**Rough cost.** ~$50–150 API (extraction calls); local compute; **4–6 weeks.**

**Feasibility probe (≤1 h, ≤$5).** On one local Mem0 install: add 20 facts from 5 synthetic "emails", delete 1 client via API, then re-run ingestion over the same email folder and query. Does the fact come back? (Takes ~30 min; this is the kill test in miniature.)

**ICAIF fit.** Medium-good ("compliance"); the RIA archive framing is practitioner-credible. Security/privacy venues are an alternative.

---

### I6. Same contract, different guarantees? A mutation-scored conformance suite for backend-agnostic memory governance, centred on migration (PI seed)

**Pitch.** The PI design's architectural bet is a governance gateway over swappable backends with admission gates checked by fixtures, oracles and canaries. The reviewer's objection: for mediated paths, invariance holds by construction; failures live in side channels (backend-internal consolidation, derived summaries, direct APIs, re-index) and in migrations. We therefore make the paper about **the test suite's power, not the gateway's pass rate**: (a) define a backend-agnostic governance contract (write, derive, retrieve, restrict, erase, export with record-class metadata); (b) build a conformance suite; (c) **seed governance bugs** (mutants) into backend adapters and migration pipelines (drop metadata on re-index, soft-delete only, scope check on search but not GET-by-id, summaries not regenerated, stale embeddings after model swap) and report the **mutation score**; (d) have the suite and the mutants written by **different people** (R-label); (e) run it on ≥3 open backends across one embedder and one model migration, with arXiv:2609.08258's store-level guard as an external baseline.

**Gaps addressed.** GP7 (weakened version sharpened as the reviewer asked); construct validity; infrastructure for I1/I5.

**Claims.** (C1, core) Mutation analysis as the adequacy measure of a memory-governance conformance suite. (C2, core) Governance-property survival across embedder/model/index migration. (C3) Cross-backend differential results for the same contract.

**Searches.** arXiv e1, e2, e3 (empty), e4, e5, e7, e8 (empty); WebSearch "mutation testing guardrail test suite adequacy LLM agent governance policies 2026".

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 | Mutation testing of task-based chatbots (arXiv:2509.01389, abstract, new) | **partial (method)** | Mutation testing for chatbot test suites; no governance properties or memory |
| C1 | GateTruth (arXiv:2608.12635, abstract) | **partial (method)** | Mutation testing to audit benchmark rigour, in RTL design; confirms the method's use for "does the benchmark have teeth" |
| C1 | Falsifiable release gates (arXiv:2607.13070, abstract, new) | **partial** | "A deliberately broken model yields the shortest counterexample, so the checker demonstrably has teeth" for a runtime's safety invariants; not memory governance |
| C2 | Memory portability across upgrades (arXiv:2609.05339, abstract) | **partial** | Utility-side migration only |
| C3 | Revocation study (arXiv:2609.08258, full) | **partial** | Five backends, one property (revocation), store-level filter 0.0% unsafe; not a contract suite |
| C3 | MemSecBench (arXiv:2607.27080, full) / memorywire (arXiv:2606.01138, abstract) | **partial** | Harness × backend safety; wire format over five adapters; neither measures governance-suite adequacy |

**Verdict.** Novel on **C1** in this domain (mutation score for memory-governance conformance) and **C2** (governance-side migration). C3 is partial. Confidence: medium. Risks: "engineering" perception and staleness of OSS versions (mitigate by releasing the mutant set, which does not go stale).

**Key experiment sketch.** 3 backends (Mem0, Graphiti, LangGraph store), 1 embedder swap, 1 LLM swap; ~40 contract tests; ~60 mutants in 6 classes authored by a second engineer from a bug taxonomy drawn from published failures (MemClaw GET-by-id, Zep summary non-regeneration, revocation not enforced); report mutation score per test family, per-backend failure rates with CIs, and which mutant classes survive (the suite's blind spots).

**Minimal publishable result.** Mutation score of a naive suite (API-level checks only) vs the full suite (physical/derived-tier + migration checks), showing that API-level suites miss most side-channel mutants.

**What would kill it.** Reviewers judge it a software-testing exercise with no finance content (ICAIF fit weak); or the PI decides the gateway design cannot be published (then the suite must stay design-agnostic, which is still possible).

**Rough cost.** Mostly engineering; API ~$30–80. **5–8 weeks.**

**Feasibility probe (≤1 h, ≤$5).** Write 3 contract tests and 3 mutants against a local Mem0 adapter; check that each mutant is killed only by the physical-layer test, not the API test.

**ICAIF fit.** Weak-to-medium as a standalone ICAIF paper; better at an SE/security venue or as infrastructure inside I1/I5.

---

### I7. When governance hurts the client: governance-induced suitability failures vs stateless replay (PI seed)

**Pitch.** GP5 as sharpened by the reviewer. The cost of governance that matters to a fiduciary is not a few points of QA accuracy but **an unsuitable recommendation caused by governance**: a legitimately needed, recent client fact that is falsely restricted, scope-blocked, erased too eagerly, or out-ranked by a newer but lower-authority note ("authority not recency", PI seed). We seed client profiles with deterministic suitability constraints (risk band, restricted securities, liquidity need, recent life event), run advisory tasks under ungoverned memory, governed memory (pre-filter, post-filter, restriction lifecycle), recency-only vs authority-aware reconciliation, and **stateless replay from the archive**, and score suitability violations deterministically against the seeded profile. Pre-registered equivalence margins (TOST) make a null informative.

**Gaps addressed.** GP5; GP8 remnant (staleness against system of record); the PI's empty-store degenerate optimum (R13 reported as a secondary analysis: rank the arms by governance ratio alone vs paired).

**Claims.** (C1, core) Governance-induced harm measured as deterministic suitability violations in finance. (C2, core) Stateless replay from archive as a first-class comparator. (C3) Recency-only vs authority-aware reconciliation effect on suitability.

**Searches.** arXiv f1–f8 (mostly empty); SciSpace Q5 ("utility cost of access control… worse personalised financial advice… stateless"); WebSearch covered via GP5 in `gaps.md`.

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 | Price of Safety (arXiv:2609.22818, full) | **partial** | Benign-traffic cost of defences (±4.5 pp), reranker falsely quarantines 33.6% of legitimate memories; no finance, no suitability |
| C1 | GateMem (arXiv:2606.18829, full) | **partial** | Joint utility/governance with over-refusal; non-finance |
| C1 | FinPerMA (arXiv:2608.04095, full) | **partial** | Finance client memory, utility only (no memory 18–31% vs full context 40–47%) |
| C2 | Stateless Decision Memory (arXiv:2604.20158, full) | **partial** | Argues stateless replay for regulated deployments; n=10; no governed-memory comparison |
| C3 | AuthMem-Bench (arXiv:2608.01679, full) | **partial** | Authority collapse in 48/49 configurations; τ-bench, single principal, no suitability |
| C3 | Stale inherited constraints (arXiv:2608.25553, abstract) | **partial** | 74.7–77.3% stale-consistent decisions; not finance suitability |

**Verdict.** Novel on **C1** (the harm construct in finance) and **C2** in combination; C3 partial. Confidence: medium. Importance risk: the reviewer noted industry's statelessness is about compliance burden, not utility; the paper must say it measures only the utility/harm side.

**Key experiment sketch.** 300 episodes per arm × 5 arms × 2 models (for ~18 pp MDE at n=100 per `evaluation.md`; 300 gives ~10 pp). Suitability oracle: a rule checker over the seeded profile and the recommended action (no LLM judge for the primary metric); an LLM judge only for a secondary "quality" score, validated against compliance-staff labels on 100 items (κ reported). Also report false-restriction rate, tokens, latency.

**Minimal publishable result.** TOST equivalence (or not) of governed vs ungoverned on suitability violations, with the failure breakdown (restriction vs staleness vs authority).

**What would kill it.** Governed and stateless arms are equivalent and ungoverned is not better: then "governance is free here" (still reportable, but less interesting); or the suitability rule checker is judged too simplistic by compliance reviewers.

**Rough cost.** ~3,000–6,000 episodes × ~15k tokens ≈ 45–90M tokens: **~$150–400** (speculation). **5–7 weeks.**

**Feasibility probe (≤1 h, ≤$5).** Write 5 seeded profiles with one suitability rule each; run 20 episodes with a restricted-but-needed fact under a pre-filter; check the rule checker flags the expected violations and that the ungoverned arm avoids them.

**ICAIF fit.** Strong (finance-native construct, suitability). It is the most "finance" of the survivors.

---

### I8. Whose compliance? Construct validity of memory-governance labels across legal readings and annotators

**Pitch.** Every governance benchmark in this area (ours included) scores systems against "compliance" labels that the authors assert. We turn the programme's biggest threat into a contribution: build a set of ~300 memory-governance events for an adviser (erasure request on an item that fed a recommendation; retention expiry on a derived summary; hold during an exam; a promoted skill with client traces; cross-client house note), and label the correct action (keep / restrict / erase / hold / escalate) under (a) rule-derived labels from ≥3 declared policy files (US RIA reading A/B, EU controller, California), (b) LLM judges, and (c) independent humans: compliance professionals and law-trained annotators, with a counsel-adjudicated subset. Report inter-annotator agreement, where readings diverge, and how system rankings on an existing benchmark change when labels change.

**Gaps addressed.** Cross-cutting (evaluation pitfall 11: "construct validity against actual legal obligations is not established"); enables R-law and R-label for I1, I4, I5, I7.

**Claims.** (C1, core) Measured disagreement (humans vs rules vs LLMs, and across legal readings) for agent-memory governance actions. (C2) Sensitivity of benchmark conclusions to label source. (C3) A reusable counsel-adjudicated label set with policy files.

**Searches.** arXiv g1–g5 (mostly empty), h-series irrelevant; SciSpace Q3 ("do benchmark labels for regulatory compliance… agree with legal experts"); WebSearch "mutation testing guardrail… construct validity" (returned 2609.01519).

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 | AIReg-Bench (arXiv:2510.01474, full, **new**) | **partial** | 3 legal experts per sample on AI Act compliance of documentation; Krippendorff α = 0.651 ("subjectivity of legal judgements"); not memory, not data-protection/records actions |
| C1 | Bench-2-CoP (arXiv:2508.05464, abstract) | **different** | Coverage of benchmark questions vs AI Act taxonomy; not label validity |
| C2 | Guardrail construct-validity failures (arXiv:2609.01519, abstract, new) | **partial** | Guardrail effects in agent commerce collapse under protocol standardisation; economics outcomes, not legal labels |
| C2 | Meta-evaluation (arXiv:2608.00794, 2609.25173; per `evaluation.md`) | **partial** | Judge validity and ASR under-specification; not legal-label source |

**Verdict.** Novel on **C1** for agent-memory governance actions (AIReg-Bench shows the method and the moderate agreement to expect, in a different object). Confidence: medium. Strategic value is high because it defends the whole programme.

**Key experiment sketch.** Events generated from templates and reviewed for plausibility; policy files written by the team and reviewed by counsel; 5–8 human annotators (compliance staff at the PI's organisation if permitted, plus hired law students), 3 per event; 3 LLM judges. Metrics: α per event type; confusion between sources; rank correlation of 3–4 memory systems under each label source (using I5 or GateMem-style runs).

**Minimal publishable result.** Agreement table + the specific event types where legal readings flip the correct action + one demonstration that a benchmark's winner changes with the label source.

**What would kill it.** No access to qualified annotators (then it degrades to rules-vs-LLM, much weaker); or counsel refuses to adjudicate (keep annotator-only results, clearly labelled).

**Rough cost.** API ~$20–50; human time is the cost (e.g. 300 events × 3 annotators × 2 min ≈ 30 annotator-hours). **4–6 weeks**, gated on recruiting.

**Feasibility probe (≤1 h, ≤$5).** Draft 20 events and 2 policy files; label them yourself under each policy and with one LLM; count flips. If <10% flip across policies, the "reading-dependence" story is weak and C1 rests on human disagreement alone.

**ICAIF fit.** Good ("computational regulation and compliance"); also FAccT/CSLAW. Small enough for a short paper.

---

### I9. Necessity as counterfactual utility: a testable definition of minimisation for advisory memory writes (PI seed)

**Pitch.** The PI's margin question: how to quantify "necessary"? Define an item's necessity for a declared purpose as its **counterfactual utility**: the drop in task success over a purpose-specific task distribution when the item is withheld from memory. A governed write policy then stores only items whose estimated necessity exceeds a threshold, and we measure what minimisation buys downstream (smaller erasure surface, less cross-client leakage into skills, fewer canaries exposed) and what it costs (utility, suitability violations from I7's oracle). Risk tiering (the PI's tentative answer) becomes a threshold that varies by data sensitivity.

**Gaps addressed.** GP9; links to I1 (less client data in traces → less to leak into skills) and I5 (smaller purge surface).

**Claims.** (C1, core) A counterfactual-utility definition of necessity for *persistent memory writes*, estimated cheaply. (C2) Measured governance benefit (erasure surface, leakage) vs utility cost. (C3) Purpose-specific, sensitivity-tiered thresholds.

**Searches.** arXiv h1–h5 (h3 only productive); SciSpace Q4 ("how can data minimisation or necessity be quantified for what a personalised LLM assistant stores in memory").

| Claim | Closest (id, read) | S/P/D | Evidence |
|---|---|---|---|
| C1 | Data minimisation for prompts (arXiv:2510.03662, full, **new read**) | **partial** | Formal minimisation as privacy-max under utility constraint; **single-prompt spans only, "not stored or persistent memory"** |
| C1 | Structured personalisation as matroids (arXiv:2512.11907, abstract, new) | **partial** | Submodular selection of user facts under disclosure/utility trade-off with constraints; disclosure per query, not write-time memory |
| C1 | Memory Worth (arXiv:2604.12007, abstract) | **partial** | Per-memory outcome association p⁺(m); "associational, not causal" |
| C2 | FRS (arXiv:2606.10062, full) | **partial** | Key-fact summarisation cuts extraction 64–76% with little utility loss: a minimisation result not framed legally |

**Verdict.** Novel on **C1** only in the transfer from prompts to write-time persistent memory with a purpose distribution; this is a thinner delta than I1–I5. Confidence: low-medium. Kept because it is an explicit PI seed and it feeds I1.

**Key experiment sketch.** On I7's synthetic advisory clients: estimate per-item necessity via leave-one-out on 20 purpose tasks (or a cheaper proxy: judge-predicted necessity, validated against the leave-one-out ground truth on a subset); arms: store-all, relevance-only, FRS key-fact summarisation, necessity-threshold at 3 levels, sensitivity-tiered. Metrics: stored items per client, canary exposure, I7 suitability violations, task success.

**Minimal publishable result.** The utility–minimisation frontier and whether a cheap necessity predictor tracks the counterfactual ground truth.

**What would kill it.** FRS-style key-fact summarisation already dominates; or leave-one-out estimates are too noisy with API nondeterminism (arXiv:2608.11344, abstract) to rank items.

**Rough cost.** Leave-one-out is expensive: ~$200–500 (speculation). **5–7 weeks.**

**Feasibility probe (≤1 h, ≤$5).** For 3 clients × 30 items × 5 tasks, compute leave-one-out necessity twice with the same seed settings; check test–retest correlation. Low correlation → drop or switch to a proxy.

**ICAIF fit.** Medium (privacy in finance); law-and-tech framing also possible.

---

### How the survivors combine (programme view; not a ranking)

- **Anchor:** I1 (governed promotion), with I2 as its measurement precursor (can be written first), I3 as its erasure mechanism and I4 as its retention component. All share one synthetic multi-client advisory generator with canaries, one skill-evolution harness and the policy files.
- **Fact-memory arm:** I5 (purgeable derivative / resurrection) and I7 (harm of governance). They share the archive-backed client histories.
- **Cross-cutting enablers:** I8 (label validity) supplies R-label/R-law for all; I6 (mutation-scored conformance) supplies the test harness.
- Given ICAIF's 8-page limit, each of I1, I2, I5, I7, I8 is sized as one paper.

---

## 4. Dropped ideas (with reasons)

| Raw idea | Fate | Reason |
|---|---|---|
| R2, R6 | **Merged → I2** | Same measurement; R6 is I2's expected finding. |
| R14 | **Merged → I1/I2** | A framing (shared skills are the realistic cross-client channel given per-user Memoria), not a study. |
| R20 harm-regression gate | **Merged → I1** as a gate axis | Regression-aware gates are moderately crowded (GRASP, FRAMES, Designer-RSI, FinSkillOps arXiv:2609.19680 with zero-regression gates in finance); the e-banking flip/harm accounting is used as a metric in I1. |
| R17 lineage validation | **Merged → I1** (lineage completeness) | For skills, lineage completeness is the binding constraint (MemoRepair 1% → 17.7%); a standalone counterfactual lineage metric (GP6) is costly with hosted-API nondeterminism. PI seed retained inside I1. |
| R24 formal leakage bound | **Dropped** (kept as a stated limitation of I1) | A meaningful bound on what an LLM-written procedure reveals is not available; a DP mechanism over prose skills would destroy utility or be vacuous. Revisit only if a parametric skill representation is used. |
| R3, R9 (skill slice) | **→ I3** | — |
| R7, R9 | **→ I5** | — |
| R8 policy-parameterised benchmark | **Split** into R-law (a rule for all ideas) and I8 | As a standalone benchmark it is "benchmark of everything" and passes-by-construction; its useful core is the policy-file idea and the label-validity study. PI seed (lifecycle states, metadata contract) survives as the label/policy schema. |
| R10, R11 | **→ I6** | — |
| R12, R13 | **→ I7** | R13 (empty-store optimum, PI seed) is a secondary analysis, not a paper: GateMem already pairs utility with governance. |
| R15 composition canaries + Brewer–Nash | **Dropped for now** | With per-user Memoria and no MNPI walls, there is no shared fact store in which composition leakage arises; AkasicMEM (arXiv:2609.25563) announces this exact evaluation; PiSAs covers generic spillage. Revive only if the PI enables firm-level shared notes. The deterministic-composition-canary technique can be reused in I2 (compose A's and B's contributions in one skill). |
| R16 authority-lattice reconciliation (PI seed) | **Merged → I7** as a failure class | AuthMem-Bench (arXiv:2608.01679) pre-empts the general mechanism (48/49 collapse; labels fix it); the finance delta is best measured by its suitability consequence in I7. |
| R4 | **→ I4** | — |
| R5 maker-checker pre-screen | **Dropped** | Needs real reviewer time and real candidate skills; with synthetic data the "review hours" are not credible. Promotion cost is reported inside I1 (rejection rates, reviewer-minutes per candidate on a small sample). Revisit with approved pilot traces. |
| R18 | **→ I9** | — |
| R19 | **→ I8** | — |
| R21 symbolic vs logged-probabilistic auditability (PI seed) | **Dropped** | Interesting but under-specified ("auditable" needs the lineage metric GP6 lacks); single-researcher MOSS evidence; no finance hook stronger than I1/I4's audit reconstructability, which covers the audit question for skills. |
| R22 certified graph unlearning on a bitemporal KG (PI seed) | **Dropped** | Construct mismatch: certified graph unlearning (GNNDelete, arXiv:2508.02044) removes influence from *GNN parameters*; a bitemporal KG built by LLM extraction is symbolic, where deletion is exact and the real problem is derived edges and re-extraction, i.e. I5's resurrection and MemoRepair's cascade. A formal statement of what deleting an edge guarantees is a small section in I5, not a paper. |
| R23 drift / bias-contagion observability (PI seed) | **Dropped** | Memory Contagion (arXiv:2606.23195) shows contagion for length bias on older models only; newer models were immune and authority bias did not propagate (per INDEX §1). Low expected effect; needs production traces. |
| RL-learned governance, SAR/AML memory, parametric scope | **Stay killed** (as in `gaps.md`) | Unchanged reasons. |

---

## 5. Newly found prior work (added with `--tag ideation-check`)

| id | Title (short) | Read | Bearing |
|---|---|---|---|
| arXiv:2609.19680 | FinSkillOps: self-evolving skills for SEC-filing QA | full | **Closest finance skill-governance paper.** Zero-regression, false-trigger gates, versioned retirement; 6/33 promoted. Single deployment; no privacy, erasure, cross-client or regulatory mapping. Partial overlap with I1 C3/C4; a baseline for I1. |
| arXiv:2609.06815 | Typed Federated Artifacts (SYNAPSE1) | abstract | Shares tool-routing knowledge across agents with "per-field privacy (described here, but [not] measured)". Adjacent to I1/I2; not skills-from-clients with erasure. |
| arXiv:2609.26242 | Temporal unlearning vs exact retraining oracles (market data) | abstract | Method precedent for I3's counterfactual oracle; finance domain, forecasters not skills. |
| arXiv:2607.13070 | Falsifiable release gates for self-improving systems | abstract | Deliberately broken models show the checker "has teeth"; method precedent for I6. |
| arXiv:2609.08279 | Restore-counterfactual audit of forgetting | full | Capacity eviction, not erasure. Different from I5 despite the name. |
| arXiv:2609.01519 | Construct validity failures in guardrail evaluation | abstract | Supports I8's premise (guardrail effects collapse under protocol control). |
| arXiv:2512.12856 | Forgetful but Faithful (MaRS / FiFA) | full | Policy-based forgetting with audit trail; single agent; explicitly no legal retention or holds. |
| arXiv:2512.11907 | Structured personalisation as matroids, data-minimal agents | abstract | Closest for I9's selection formulation (per-query disclosure). |
| arXiv:2510.01474 | AIReg-Bench | full | Legal-expert labels, α = 0.651: the expected agreement level for I8. |
| arXiv:2606.19242 | Runtime compliance verification for AI agents | abstract only in fetch record | Not examined further; check for I8/I6 relevance. |
| arXiv:2605.16309 | ANNEAL governed symbolic patch learning | abstract | Governed process-knowledge edits with provenance and rollback; single agent, no privacy. |
| arXiv:2609.02246 | LLM-as-judge is not an oracle for self-improving agents | abstract | Production lessons: deterministic gates over judges; supports I1's deterministic metrics. |
| arXiv:2605.11946, arXiv:2609.20455 | Counterfactual trace auditing of skills; SkillAA attribution-guided rollback | abstract | Leave-one-out credit for skill *units*, not clients; no privacy or erasure (checked). |
| arXiv:2508.05464, arXiv:2509.01389 | Bench-2-CoP; mutation testing of chatbots | abstract | Background for I8, I6. |

**Threat summary.** No new paper pre-empts a core claim of any survivor. The closest new threat is **FinSkillOps** (finance + governed promotion, but no privacy/erasure). The standing threats remain AkasicMEM (for anything benchmark-like on derivation/leakage), PoisonedEvolution and FederatedSkill (for I1), MemoRepair and OBLIVION (for I3/I5), and AntiSkillBench (for I2).

---

## 6. Questions for the PI raised by ideation

1. **Is cross-client skill sharing actually wanted?** I1–I4 assume the firm would share procedural memory across clients. If the realistic plan is per-client or per-adviser skills only, I1's business case weakens and I2 becomes the main contribution ("don't, and here is why").
2. **Annotators.** Can compliance staff (not involved in the design) label ~300 events and review task templates (I8, R-label)? This is the single most useful non-API resource.
3. **Counsel.** Can counsel adjudicate ~50 events under 2–3 declared policies (I4, I8), without being asked for a firm legal position?
4. **Timeline.** ICAIF '27 main track (deadline likely mid-2027) vs a faster venue for I2 (e.g. a privacy or agents workshop). Which matters more?
5. **Publishing the gateway.** Needed only for I6's mechanism half; I6 can run design-agnostic.

---

## 7. Feasibility probes (2026-09-25)

`/ideate` step 4. **Constraint: no LLM API key**, so every part that needs no generation was done, and the parts that need generation are scripted and stubbed with a hard cap. The code is in `code/probes/` (git commits `ff14df3`, `72398aa`, `b3b0087`; `README.md` there), and `pytest` passes 28/28. External queries used only public paper and product names (no `inputs/` content, no PI-design terms). Repo metadata comes from the GitHub REST API; "last commit" is the default-branch HEAD, accessed 2026-09-25.

### 7.1 Code and data availability (I1, I2)

| Artefact | Code / data | Licence | Last commit | Runs on API models? | Notes |
|---|---|---|---|---|---|
| SkillClaw (arXiv:2604.08377) | https://github.com/AMAP-ML/SkillClaw (2.6k stars) | **MIT** | 2026-08-17 | **Yes**: any OpenAI-compatible endpoint, or AWS Bedrock (so Claude via Bedrock) | `evolve_server/` has two engines (workflow, agent). Shared storage can be `local`, OSS or S3, so it runs on one laptop. Its create-skill prompt has **no privacy instruction** and asks for "concrete API endpoints, ports, command patterns, and payload examples" (read in `evolve_server/pipeline/execution.py`), so leakage is plausible (speculation until measured). The prompt is vendored with attribution. |
| FederatedSkill (arXiv:2606.03143) | https://github.com/UCSB-NLP-Chang/FederatedSkill | **Apache-2.0** (the LICENSE file is Apache 2.0; GitHub shows NOASSERTION) | 2026-06-23 | Yes: Dashscope, Anthropic and others via LiteLLM | Needs Docker images with CLI agents (claude-code, qwen-code, …) and the 1.6 GB HF dataset `zhang-ziao/SkillFlow-Task` (licence "other", not gated). Heavy but usable. |
| PoisonedEvolution (arXiv:2608.05563) | **No code found** (no link in the full text; GitHub search and web search came up empty) | — | — | — | The provenance-diversity gate ("≥3 users and clusters, reject majority dominance") is simple to re-implement from the paper. |
| SkillJack (arXiv:2608.03509) | https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/SkillJack | Repo is Apache-2.0, but the subfolder README says "for research purposes only" (**ambiguous: treat as research-only**) | subfolder 2026-08-05 | Yes (OpenAI-compatible) | Ships 150 poisoned and clean AppWorld trajectories. |
| AntiSkillBench (arXiv:2608.03700) | https://github.com/yonglixiang/AntiSkillBench is a project page only: "Benchmark code: Coming soon". Dataset: https://huggingface.co/datasets/yonglixiang/AntiSkillBench | Code: none. Dataset: **gated (auto-approve)**, licence not visible without login | 2026-08-05 | — | The paper promises release "upon formal publication". I2's AntiSkillBench-style baseline must be rebuilt from the paper's metric definitions. |
| MemoRepair (arXiv:2605.07242) | **No code found** | — | — | — | Uses a public ToolLLaMA LoRA only. Cascade withdrawal is easy to re-implement over our lineage ids. |
| FinSkillOps (arXiv:2609.19680) | **No code found** | — | — | — | Its gates (zero-regression, false-trigger) must be re-implemented from the paper. |
| E-banking audit (arXiv:2608.17684) | "Code and audit artifacts will be released upon publication" (full text) | — | — | — | Its environment is public: see the AgentDojo row. |
| AgentDojo Banking suite | https://github.com/ethz-spylab/agentdojo; PyPI `agentdojo` 0.1.35 | **MIT** | 2026-06-02 | Yes | **Ran locally**: suite v1.2.2 loads (16 user tasks, 9 injection tasks, 11 tools, matching arXiv:2608.17684), and ground-truth replay gives **16/16 utility** with no LLM (`scripts/agentdojo_banking_groundtruth.py`). |
| AWM (I2 pipeline) | https://github.com/zorazrw/agent-workflow-memory | Apache-2.0 | 2025-12-22 | — | Available. |
| ReasoningBank (I2 pipeline) | https://github.com/google-research/reasoning-bank | Apache-2.0 | 2026-08-05 | — | Available. |

**Re-implementing SkillClaw's evolver is unnecessary**, because the MIT code runs on a local filesystem. If a slimmed evolver is wanted for control (no Nacos registry, no proxy), the core loop is summariser → skill grouping → create/evolve prompt → optional verifier. SkillClaw's `evolve_server/` is about 230 KB of Python (workflow engine 45 KB; summariser, execution and verifier together about 60 KB). A faithful minimal re-implementation would be **about 400–600 LOC, 2–3 days**, reusing its prompts under MIT. The probe already reuses the create-skill prompt verbatim.

### 7.2 LLM-free scaffold (I1, I2): built and tested

- **Generator.** Synthetic RIA clients (random-syllable surnames, `99…` accounts, `example.com` emails, risk model, ESG restrictions, life event). Each client has a 12-symbol Crockford-base32 canary (2^60 values), planted as a "client reference code" in the CRM tool result and the adviser narration. Traces use a SkillClaw-like session schema (`turns[].prompt_text/response_text/tool_calls/tool_results`; validate it against a SkillClaw-recorded session before feeding its evolver).
- **Task family with a deterministic oracle.** "Rebalancing with restriction check" has 7 house rules that are *not* stated in the task prompt: 2% cash buffer, whole shares, restricted names sold and never bought, ±3pp drift band, $100 minimum ticket, legacy positions liquidated, hold on a pending ACATS transfer. The reference solver passes the checker on 240/240 generated cases. A textbook proportional rebalance fails ≥30/40, so the no-skill baseline is beatable and a skill can matter.
- **Detector.** Canary hits are exact, normalised (case and separators) or partial (≥7 contiguous symbols). The detector also matches name, surname (≥6 letters), account number or last 4 digits, DOB in 7 formats, portfolio value and email. Life events count as `quasi`: they are low-entropy and shared across clients, so the first stub run showed they must not count as foreign-client leaks. Measured: no exact or normalised false positives on 200k random characters against 300 clients. Metrics include canary recovery, identifying leak and post-erasure persistence.
- **Generation interface.** `StubBackend` (deterministic "leaky" and "abstract" distillers) runs the full pipeline today. `AnthropicBackend` uses the official SDK with adaptive thinking and a server-side refusal fallback. `BudgetGuard` reserves each call's worst-case cost before the call (at the highest listed price when a fallback could serve it) and refuses any call that would breach the cap.

### 7.3 I1 kill test ("per-client ≈ pooled?"): ready, not run

`code/probes/scripts/i1_killtest.py --backend anthropic --model claude-opus-5 --max-usd 5`
- Design: 20 clients. The pooled skill comes from 41 traces (2 per client; the pool is guaranteed ≥2 of each edge case). Each of the 5 target clients gets a per-client skill from its own 5 traces. There are 10 held-out tasks (5 common, 5 edge cases), each run under {no skill, own per-client skill, pooled skill}. The sanitised pooled skill is distilled for the leakage scan, which is I2 probe (b).
- **Cost (the script's estimate, prices cached 2026-06-24): 37 calls, about 121k input tokens, expected $2.12, worst case $4.26 on `claude-opus-5`. Hard cap $5**, enforced per call. The script refuses `--max-usd > 5` and refuses to start if the expected cost exceeds 80% of the cap.
- Pre-registered kill signal: pass(pooled) − pass(per-client) ≤ 1/10. With n = 10 this is a smoke signal, not a test.
- Checkpoint 3 applies: the PI approves the spend.
- **Design caveat (important).** In a templated world, pooling helps *exactly when* per-client histories miss rare edge cases. The size of that effect is a parameter (`--p-edge`), not a finding. The probe can falsify "pooling helps" (for example, if the model infers the house rules from a few traces anyway), but it cannot establish that real advisory procedures share enough structure across clients. That is PI question §6.1 plus pilot traces.

### 7.4 I5 local resurrection checks: run, results

Setup: an archive (system of record) of 6 synthetic client emails with per-client canaries, and memory built from it. Client C0002 is erased. "Visible" means the erased canary is returned by the API, or is present in the named files or table.

| Trigger (test) | Chroma 1.5.9 | Mem0 OSS 2.2.0 (`infer=False`, Chroma store) | LangGraph 1.2.12 | Git-backed memory (Letta MemFS semantics, plain git) |
|---|---|---|---|---|
| API after native delete | raw items gone; **multi-client digest (client_id=firm) still quotes the client** | gone | Store item gone | working tree clean |
| Residue after delete | **`embeddings_queue` WAL table keeps the full add payload**; it disappeared only after 5,000 further writes flushed the segment (a low-traffic collection could keep it indefinitely) | **`history.db` keeps the deleted text as `old_memory`, and the public `Memory.history(id)` returns it** | **5/6 thread checkpoints still carry the text** | **`git log -p` shows it; earlier clones keep it even after the origin rewrites history + gc** |
| Re-ingest from archive | naive upsert **resurrects**; ingest-time tombstone blocks it | naive `add()` **resurrects**; tombstone blocks it | — | — |
| Snapshot / backup restore | naive restore **resurrects**; replaying the erasure journal fixes it; backup media still hold the item | — | **time-travel replay from an earlier checkpoint re-writes the erased memory** | checking out an earlier commit restores it |
| Re-embed migration | from the live collection: no; rebuilt from the archive: **resurrects** | — | — | — |
| Derived summary | delete by client_id misses it; lineage purge (source ids) catches it | — | — | — |
| Quoted copy (adviser reply quotes client) | **delete by client + source-id tombstone misses it** (content-level purge needed) | — | — | — |

Reproduce with `resurrection/*.py`; `tests/test_resurrection.py` pins these outcomes. The Chroma result is the same with the hashing embedder and with Chroma's local ONNX all-MiniLM-L6-v2. **A local embedding model works without sentence-transformers.** sentence-transformers 6.1.0 is also installable on Python 3.12 (torch 2.14; resolver dry-run only).

**From docs and code (not run):**
- **Graphiti 0.30.2.** `remove_episode()` deletes edges only when the episode is the edge's *first* episode (`edge.episodes[0]`). It deletes nodes only when no other episode mentions them. It does **not** regenerate surviving entity-node summaries, saga summaries (incremental `summarize_saga`) or communities, and it does not undo edge invalidations the episode caused. Derived text from the erased episode can therefore persist. This can be tested **LLM-free** by writing `EpisodicNode`, `EntityNode` and `EntityEdge` objects directly through the embedded **Kuzu** driver (about 2–3 h). `add_episode` itself needs an LLM.
- **Letta.** The Python server was retired to the `archive` branch (`letta-ai/letta` README). Current Letta (`letta-code`, Apache-2.0, TypeScript) keeps agent memory as a **git repository per agent** ("Every memory edit is committed", docs.letta.com/concepts/memfs). "Dreaming" subagents rewrite memory in git worktrees. Agent export exists (`GET /v1/agents/{id}/export`, with `scrub_messages`). Conversation transcripts are separate. Our git emulation shows the consequence.
- **Mem0.** There is no tombstone or deny-list anywhere in `mem0/`. With `infer=True`, re-ingest runs LLM extraction, and the ADD/UPDATE decision is taken against *existing* memories only, so a deleted fact is simply re-added. This needs a key to confirm, including paraphrased resurrection.
- **LangGraph.** `BaseStore` has TTL (`default_ttl`, `refresh_ttl`) but no erasure journal. Checkpointers keep full state history per thread until `delete_thread`.

### 7.5 Archive side (RIA archiving vendors; public pages, accessed 2026-09-25)

- **Global Relay** (Slack Marketplace listing, https://slack.com/marketplace/A2J6HGDB2-global-relay-archive-for-slack): Global Relay is the processor and the customer is the controller that decides retention. There is "automatic deletion of your archived data at the end of the applicable Retention Term (subject to any applicable legal holds)"; administrators "may also place legal holds"; and "upon written direction by Customer … Global Relay will securely delete or destroy Archived data", for example "to comply with applicable law (e.g. GDPR, CCPA etc.)". Standard Definitions (https://www.globalrelay.com/policies/standard-definitions/) define the Retention Term "until final disposition"; the disposition details sit in the MTOS §13.3 (not read). Legal-hold product page: https://www.globalrelay.com/solution/legal.
- **Smarsh** (https://www.smarsh.com/archive/): "immutable WORM storage for SEC 17a-4, configurable legal holds, and defensible deletion"; policy-based retention by group, region, message type or risk category. Retention-policy walkthrough: https://www.smarsh.com/product-spotlight/connected-suite-spotlight-series-retention-policies-and-data-storage/. That page says nothing on hold precedence or individual erasure.
- **Modelling implication.** In the model, the archive is authoritative, retention-scheduled and hold-aware, and deletes on controller instruction (per record, not per derived copy). Neither vendor describes propagating a deletion to downstream copies such as AI memory, so the derived tier's purge is the firm's job. That supports I5's framing. How WORM/17a-4 immutability interacts with a GDPR erasure is a legal question [M]. Backup-media handling is not described publicly.

### 7.6 Verdicts

| Idea | Verdict | Reason |
|---|---|---|
| **I1** | **Amber** | All infrastructure is feasible: SkillClaw (MIT, maintained, local, API models), FederatedSkill (Apache-2.0), AgentDojo (MIT, runs), and the scaffold and oracle are built. Three baselines have no code (PoisonedEvolution, MemoRepair, FinSkillOps), but each is small to re-implement. **The kill question is unanswered**: it needs about $2 of API. Even a pass only shows "pooling *can* help when edge cases are rare per client"; the business case still depends on PI Q1 and real traces. |
| **I2** | **Green** (feasibility); outcome open | Everything needed is public or built: SkillClaw, AWM and ReasoningBank code; detector; generator; sanitised arm. SkillClaw's own prompt asks for concrete examples and has no privacy guard, which makes a non-zero leak plausible (untested). Minus: AntiSkillBench code is unreleased and its dataset is gated, so that baseline is rebuilt from the paper. The kill case ("~0% leak") is decided by the same ≤$5 run. |
| **I5** | **Amber** | A local, LLM-free test bed works for 4 stacks. As predicted, naive re-ingest and restore resurrect data, and a tombstone or journal replay fixes both. **This part is a checklist** (the stated kill criterion, partly met). What survives as research: (a) *residue in derived and log tiers* that a native delete leaves behind (Mem0 history returned by API, Chroma WAL, LangGraph checkpoints plus time-travel replay, git history and clones, Graphiti summaries per code); (b) the *quoted-copy / subject-vs-source lineage* gap; (c) LLM-mediated re-derivation (Mem0 `infer=True`, Graphiti, consolidation), which needs a key (about $0.5–1: roughly 40 extraction and update calls). Scoop risk stays high (FRS, OBLIVION). Several findings are vendor-fixable engineering issues; frame them as a measured matrix plus a checklist, not a mechanism. |

**Still blocked on an API key:** I1/I2 kill-test run (≤$5; expected $2.12). Mem0 `infer=True` re-ingest and paraphrase resurrection. Graphiti extraction path. Behavioural leakage probes (client B's session eliciting client A's canary). LLM-generated (non-templated) traces.

---

## 8. Fatal-flaw review of top 3 (reviewer, 2026-09-25)

*`/ideate` step 5, idea-critique mode, so no scores. Read: §§0–7 of this file (I1, I2, I5 in full), the "why" fields of all 378 judgments, `STATE.md`, `gaps.md` (GP1 review and programme review), `skills.md`, and `code/probes/scripts/i1_killtest.py`. Scoop checks: 13 arXiv queries (`--since 2026-08-01 --sort date`, one with relevance) and 3 WebSearches, all in generic public wording with no `inputs/` content or PI-design terms. Added with `--tag ideation-check`: arXiv:2609.29144, arXiv:2609.07131. Re-tagged: arXiv:2609.04875, arXiv:2609.12320.*

**About the tournament.** The three judges come from one model family and all read the same ideas.md text, so they share its framing. Their "why" fields agree on novelty but point opposite ways on significance: the regulatory judge ranks I7 and I5 above I2 because "I2 matters only if the firm really shares skills". I1 ranks 1st on significance, and that rank assumes a premise nobody has checked (below). Read 0.84 vs 0.81 as a tie.

### 8.1 I1: support-counted, lineage-bound promotion

**Fatal / near-fatal flaws**
1. **The written-policy confound (near-fatal, not yet tested).** The probe's task family requires 7 house rules (cash buffer, whole shares, restricted names, drift band, minimum ticket, legacy liquidation, ACATS hold). These are *firm policies*. An RIA must already keep them in writing under 206(4)-7 [V] and retain them under 204-2(a)(17) [V]. A skill written from the policy manual carries no client data, cannot leak, and has no erasure problem. The probe keeps the rules out of the prompt, so the agent can learn them only from client traces. That setup *creates* the need I1 then governs. Every arm list in I1 lacks the obvious baseline: **"policy-authored skill"**, meaning a compliance officer writes the SKILL.md (or it is distilled from the policy text alone). If that arm matches pooled skills, pooling's business case is limited to *tacit* know-how that is missing from written procedures. Whether such know-how exists is an empirical question about real traces, and synthetic data cannot answer it.
2. **The pooling benefit is an artefact of the templated generator. It also has a volume confound.** In `i1_killtest.py` the pooled skill sees 41 traces and each per-client skill sees 5. "Pooled > per-client" therefore mixes *cross-client* sharing with *8× more data*. With templated traces the gap is fixed in advance: it equals P(edge case in the pool) − P(edge case in the client's own 5 traces), which `--p-edge` sets. The §7.3 caveat already admits the probe cannot show that pooling helps in reality. It also cannot separate sharing from volume. **Change the probe before spending the $5.** Add (a) a volume-matched pooled arm (5 traces from 5 different clients) and (b) the policy-authored arm. Recompute the budget: the extra distil and exec calls probably push the worst case above the $5 cap, so drop the sanitised exec arm or trim held-out tasks.
3. **The "one invariant for three purposes" claim (C1) is overclaimed.** A support count of k says nothing about the *content* of a skill. A skill supported by 10 clients can still quote one client's rare restriction verbatim, which is k-anonymity misapplied to prose. Leakage is actually controlled by the canary gate. The canary gate and the canary-recovery metric use the same detector, so the leakage result holds by construction: the circularity `gaps.md` warned about. The Sybil reading is weak for KYC'd RIA clients. The realistic integrity threat is a *dominant* high-volume client or adviser, not fake clients.
4. **Size.** Seven arms, three baselines with no code (PoisonedEvolution, MemoRepair, FinSkillOps re-implemented), Sybil and erasure events, two policy files. That cannot fit 8 pages with no appendix, and every judge ranked I1 5th–6th on feasibility. The fairness of re-implemented baselines is an easy line of attack for reviewers.

**Closest prior work (updated).** PoisonedEvolution (≥3-user gate, integrity only), FederatedSkill, MemoRepair, FinSkillOps: unchanged. **New: *Scope Before You Persist* (arXiv:2609.29144, abstract).** Retrieving each accepted skill edit only within its originating task family raises utility from 0.713 (global memory) to 0.816, and cuts harmful deployments from 6/8 to 0. The global store falls *below the static agent* (0.775). The scope there is task family, not client, but a reviewer will cite it as evidence that pooled procedural memory can hurt. It supports making "scoped vs pooled" an empirical question, not an assumption. No new paper connects distinct-client support to privacy or erasure; the WebSearch found only FederatedSkill, AntiSkillBench, SigLeak and PiSAs. **Not scooped.**

**Three likely ICAIF reviewer objections, and how to preempt them**
1. *"Why learn firm procedures from client traces instead of writing them down?"* Add the policy-authored arm, and limit claims to procedure content that is absent from it. Report the share of skill content attributable to written policy vs traces.
2. *"Synthetic, templated, and the leakage gate is scored by its own detector."* Use held-out leakage detectors the gate never sees: attribute inference by an attacker model against chance, paraphrase canaries, rare-attribute identifiability. Paraphrase the traces with an LLM so that pattern-matching templates does not work. Run two model families.
3. *"k-anonymity on prose gives no guarantee, and the Sybil model is unrealistic."* Call k a *support threshold*, not a privacy guarantee. Report empirical leakage and utility as functions of k. Replace Sybils with a dominant-client scenario.

**Verdict: park as a standalone paper; keep as paper 2, conditional on paper 1 and on PI Q1.**

### 8.2 I2: do promoted skills remember clients?

**Fatal / near-fatal flaws**
1. **Verbatim leakage is a prompt artefact, so the headline result is predictable.** SkillClaw's create prompt asks for "concrete … examples", so it will leak (§7.1). A sanitisation prompt will bring verbatim canaries to about 0. A table of "prompt A leaks, prompt B doesn't" is the result reviewers expect and will call obvious (all three judges: "expected finding").
2. **The canary measures the wrong construct.** A 12-character "client reference code" is exactly what an abstracting distiller drops. Real leakage in advisory skills looks like *rare edge cases turned into rules*: "if the client restricts XYZ and has a pending ACATS…". The detector deliberately classes life events and other low-entropy attributes as `quasi` and does not count them. That choice is right for false positives, but it leaves the real risk out of the headline metric.
3. **Post-erasure persistence is trivial as specified.** Deleting traces and then running the maintenance cycle leaves existing skills untouched, so persistence is about 100% by construction (SkillJack already reports 80%). The non-trivial question is the *counterfactual*: does re-deriving without client i still produce i's specific content, because other clients share it, so it is no longer personal to i?
4. **Relevance depends on whether sharing is wanted** (the regulatory judge's point). Partial mitigation: the risk is vendor-agnostic. Foundry procedural memory with a static scope, and AgentCore cross-actor reflections, already ship it (`skills.md` §7).

**The structural point that makes it a paper.** Pooling helps *because* it brings in rare edge cases that a client's own history lacks (§7.3). A rare edge case is also the most identifying content a skill can contain. **The utility of pooling and cross-client identifiability share one source: rarity.** Measured as a function of edge-case rarity and the support threshold k, this is a result, not a truism. It could come out as "the gain from pooling is mostly on cases supported by fewer than k clients, so a privacy floor removes it". It could also come out the other way. Either way it decides I1.

**Closest prior work.** AntiSkillBench (single-user persona leakage, 55–66%); PiSAs (cross-user spillage via shared memory, not skills); FederatedSkill (privacy audit with no numbers); SkillJack (persistence of poison). New: **AgentLeak (arXiv:2609.07131, abstract)**, which clones capability from execution differences. That is procedural behaviour leaking through behaviour, from a proprietary agent to an attacker. It supports the behavioural-probe design; it does not cover client data. **AIM / MUMBench (arXiv:2609.12320)** classifies memory as private or public across users and evaluates deletion. It covers facts, not skills. A reviewer may name it as the multi-user benchmark to beat, so cite it. **Not scooped in the cross-client skill form.** Risk remains medium: this is the obvious next paper for the AntiSkillBench or FederatedSkill groups.

**Three likely reviewer objections, and how to preempt them**
1. *"Leakage depends on the prompt."* Run ≥3 pipelines with their *own unmodified* prompts (SkillClaw, AWM, ReasoningBank), plus each with a sanitisation addendum. Report per pipeline and do not average.
2. *"Canaries are unrealistic."* Make the rare-attribute canary the primary metric: attacker identifies the client among N candidates vs 1/N, run as a dose-response over rarity. Keep random canaries as a secondary, deterministic floor.
3. *"So what? It's diagnosis only."* Include the utility side (pooled vs per-client vs policy-authored vs volume-matched) and a simple support-threshold arm. The paper then gives a decision ("pool only procedures supported by ≥k clients; here is what that costs"), not only a diagnosis.

**Verdict: proceed, widened into the first paper (see §8.4).** As specified in §3 it is too thin for ICAIF main track. With the utility arms and the rarity sweep it has a real question.

### 8.3 I5: purgeable derivative and resurrection

**What the probes did to it.** Re-ingest and restore resurrection are fixed by an ingest-time tombstone and an erasure-journal replay: a checklist, as predicted. Practitioner systems already ship tombstones and verified erasure (e.g. SuperLocalMemory 4.0, arXiv:2608.08253; open-source PRs implementing purge plus tombstone compaction, found by WebSearch).

**Fatal flaws of what remains**
1. **Residue (surviving claim a) is largely pre-empted.** *Execution-state unlearning* (arXiv:2609.04875, full, already in the library but **missing from I5's overlap table**) shows that record deletion leaves derived-state leakage of 0.86–1.00, and fixes it with provenance-guided replay from checkpoints. FRS (text residue), Revoked-but-Authoritative (arXiv:2609.08258, backend comparison) and MemLeak cover the rest. The specific hits (Mem0 `history()` returning deleted text, the Chroma WAL, LangGraph checkpoints, git history) are real but are **vendor bug classes**: soft-delete audit tables, write-ahead logs, versioned state. An ICAIF reviewer will read them as a bug report. The Mem0 history-API finding deserves responsible disclosure regardless.
2. **Sole-carrier rate (C2) cannot be measured on synthetic data.** The fraction of memory items with no archived source is a parameter of the generator, the same way pooling benefit is a parameter in I1. It becomes a finding only with real deployment traces (pilot approval, PI Q3 in `gaps.md`). Without them C2 is empty.
3. **Hold precedence and archive coverage** rest on the unresolved legal classification (PI answer 1). This conflicts with R-law.

**What survives.** (b) The **subject-vs-source lineage gap**. Purge keyed by data subject or source record misses a client's data quoted inside *another* record (the quoted-copy row in §7.4). This is small and concrete, and it transfers directly to skills: a skill derived from client B's traces that quote client A. (c) LLM-mediated re-derivation (Mem0 `infer=True`, Graphiti summaries), which is still untested and needs a key.

**Is there a paper-worthy core?** Not for the ICAIF main track. At most a practitioner short or workshop paper: "a trigger × tier resurrection matrix for four stacks, plus an erasure checklist". Novelty is low and it would be scooped quickly (the FRS authors named embedding and cache residue as their next step).

**Verdict: park as a standalone paper; fold the useful parts into paper 1.** In the skill setting, skills are one more derived tier. Paper 1's erasure section should include (i) re-derivation after deletion as a resurrection trigger, (ii) skill-store restore and versioning (SkillClaw's local/S3 storage, git-backed skills) as a residue tier, and (iii) quoted-copy cross-attribution. That is one table row and one paragraph, reusing `resurrection/` code.

### 8.4 Combinations and recommended plan

**Is "I2 then I1" the right sequence?** It is the right *order* but the wrong *split*. As written, I2 cannot tell whether I1 is worth doing, because I2 has no utility arms. I1's kill test cannot tell either, because it confounds volume and ignores written policy. Put the decisive parts of both into paper 1. Make I1 (the support-threshold mechanism, lineage, erasure re-derivation) paper 2, and do paper 2 only if paper 1 finds a non-empty frontier and the PI wants sharing.

**Paper 1 (first; ICAIF '27 main track; an earlier privacy or agents workshop is optional).**
- **Working title:** *Does pooling client traces into shared agent skills pay for its privacy cost?*
- **Core question:** When skills are distilled from many clients' advisory traces, how does the utility gained from pooling relate to cross-client identifiability? How much of that gain survives (a) a support threshold and (b) replacing learned content with a policy-authored skill?
- **Decisive experiment:** a rarity sweep. Edge-case rarity p_edge ∈ {0.02, 0.08, 0.3}; 2 task families (rebalancing, plus KYC refresh or account transfer); 3 pipelines with their own prompts (SkillClaw, AWM, ReasoningBank) × {raw, sanitised}. Arms: none, per-client, volume-matched pooled, full pooled, pooled with support threshold k ∈ {1, 3, 5}, policy-authored. Outcomes: deterministic task pass; rare-attribute identifiability vs 1/N (primary leakage metric, detector held out from any gate); verbatim canaries (floor); behavioural recovery in other clients' sessions; and, for 10 erased clients, persistence under maintenance vs counterfactual re-derivation (the I5 fold). Traces paraphrased by an LLM; two model families; bootstrap CIs.
- **Pre-registered decision:** if pooled ≤ policy-authored + margin, or the gain disappears at k ≥ 3, the result is *"don't pool client traces; write the procedure"*. That is publishable and closes I1.
- **Minimal ICAIF '27 version:** 1 family, 2 pipelines, 3 rarity levels, 5 arms, 1 model family plus a spot check on a second; one figure (utility gain vs identifiability, coloured by k) and one table (erasure persistence). Rough cost $100–250 (speculation); 8–10 weeks.

**Paper 2 (conditional):** I1 narrowed to the support threshold plus lineage-bound re-derivation, with the dominant-client scenario and without Sybils or the seven-arm matrix.

**I5:** no paper. Fold into paper 1 as above; report the Mem0 finding to the maintainers.

**What the PI's answer to "is cross-client skill sharing actually wanted?" must say for I1 to proceed.** All four must hold:
1. The firm intends shared (firm-, team- or adviser-level) procedural memory that is **learned from traces containing client data**, not only skills authored from written policies or internal operations logs.
2. The PI can name ≥1 concrete procedure whose useful know-how is **not in the written policies and procedures** (tacit custodian, transfer or exception handling). Without one, the policy-authored baseline wins by argument.
3. Promotion would be automatic or semi-automatic at a volume where per-skill human review is impractical. If compliance reviews every skill by hand, the gate is the reviewer, and I1's mechanism has no role.
4. The PI accepts "don't share" as a publishable outcome.

If the answer is "no, per-client only" or "shared skills are authored by compliance only", park I1 permanently. Paper 1 still stands as a vendor-agnostic measurement (Foundry and AgentCore already ship cross-user procedural memory) but loses the in-house motivation. If the answer is "undecided", paper 1 is the evidence that decision needs, which is the strongest framing.

**Scoop check result (2026-09-25).** Nothing new pre-empts I1 or I2 in the cross-client form. Scope Before You Persist (arXiv:2609.29144) is the most relevant new paper, as evidence against assuming pooling helps. For I5, the threat was already in the library but not cited against it (arXiv:2609.04875).

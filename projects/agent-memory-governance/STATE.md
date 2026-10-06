# Project state

- **Stage:** 3→4 transition - PI pivoted to a capability-first Phase-1 build: offline trace→skill distillation + capability/governance harness (demo for Q4). See `experiments/phase1-plan.md`. Privacy/erasure ideas (I1/I2/I5) deferred to Phase 2.
- **Last updated:** 2026-10-06
- **last_radar:**

## PI research taste
- Wants breadth first: regulation, evaluation metrics and trustworthiness evaluation included in the review.
- Interested in all four angles (mechanisms, evaluation, governance, attacks); the framing is decided after the gaps.

## Early scan (2026-09-24, 55 records: arXiv ×47, SciSpace ×8; titles/abstracts only)
See chat summary; to be superseded by literature/review.md.

## PI answers to gap questions (2026-09-25)
1. 204-2 classification / GDPR 17(3)(b): **unknown; PI will confirm with specialists.** → ideas must not hinge on one legal reading; treat record classes as configurable policy.
2. MNPI information barriers: **probably not** (RIA). → GP2 reframed from MNPI walls to client confidentiality / need-to-know.
3. EU/UK/California: **use as reference regimes** (don't ignore).
4. De-branded gateway, pilot traces, unnamed in-house backend: **yes, aim is publication.**
5. Venue: **ICAIF likely** (not fixed).
6. RockAI framework is **proposed only, nothing implemented**, so it's open ground for ideation, not prior art.
   Memoria (arXiv:2512.12686; IEEE 11330332) is **per-user, per-session storage; shared memory not enabled.**
   **New scope:** procedural memory distilled from traces and **promoted to skills** (reusable across users) is in scope.

## Next step (updated 2026-10-06)
**Phase 1 build toward a Q4 demo** (PI pivot 2026-10-06; `experiments/phase1-plan.md`):
1. Resolve the two blockers in plan §5: SkillEvolBench license; distiller pluggability (read its self-gen baseline).
2. Provide an API key (Bedrock Claude); stand up SkillEvolBench, reproduce no-skill vs self-gen baselines.
3. Wire AgentDojo banking + synthetic RIA to a shared metrics harness (capability + regression + finance safety).
4. Then `/design-experiments` to pre-register the frozen question + matrix before the big run (checkpoint 3 spend).
**Second Phase-1 thread opened (2026-10-06): agent-memory threat model → guardrails for Memoria** (`experiments/threat-model-and-guardrails-plan.md`). Reconciled threat→guardrail→intercept→metric table + vendor baseline-to-adopt vs gap-to-own built from existing review material (threats.md T1–T18, review §2 grid, PI memo). Recommended Q4 demo cut: injection, authority collapse, revocation/erasure, cross-client leakage (front line); collusion + multi-agent as 'what breaks when sharing is enabled'; contagion as a model-dependent caveat. Open: demo substrate (open backend→port to Memoria [default] vs straight at Memoria); 4-up cut vs promote shared-tier; parallel vs sequence with the skill-distillation thread. Quick follow-up: cross-walk table to exact C##/memo metrics (memo §6a/§15).

Carried-open PI decisions: null/mixed-result acceptance (revisit at checkpoint 4); AFTER as a stretch transfer bench; **how finance-forward Phase 1 should be** — SkillEvolBench-general-first (current default) vs promoting AFTER + leaning harder on the synthetic RIA (PI to steer).

---
### Archived (Stage 3 ideation outcome, superseded by the 2026-10-06 pivot; revive for Phase 2)
**Checkpoint 2 (PI): pick the paper.** Ideation, tournament, probes and a fatal-flaw pass are all done (`ideas.md` §§3,7,8). The reviewer's recommended plan (ideas.md §8.4):
- **Paper 1 (recommended):** *Does pooling client traces into shared agent skills pay for its privacy cost?* — merges the decisive parts of I2 (leakage diagnosis) + I1 (support threshold/utility arms) + the I5 erasure fold. Rarity sweep is the decisive experiment. A "don't pool, write the procedure" result is publishable. ICAIF '27 main track; rough $100–250, 8–10 weeks (speculation).
- **Paper 2 (conditional on Paper 1 + PI Q1):** I1 narrowed to support-threshold + lineage-bound re-derivation.
- **I5:** no standalone paper; folded into Paper 1. Report the Mem0 `history()` finding to maintainers (responsible disclosure).

**Blocking PI decision:** the 4 conditions in §8.4 for Paper 1 to keep its *in-house* motivation (is trace-learned cross-client skill sharing actually wanted; is there ≥1 procedure whose know-how is not in written policy; is promotion automatic at scale; is "don't share" acceptable). If "no/per-client only", Paper 1 still stands as a vendor-agnostic measurement (Foundry/AgentCore ship cross-user procedural memory) but loses the in-house hook. If "undecided", Paper 1 is the evidence for that decision — the strongest framing.

Once the PI picks: `/design-experiments agent-memory-governance` on the chosen paper (needs an API key for the kill-test; see §7.6 "still blocked").

## Open questions for the PI
- (gaps, 2026-09-25) EU/UK/CA data subjects in scope? May a de-branded gateway design be published? Pilot traces approvable? Does the entity run MNPI barriers or only client confidentiality? Counsel on 204-2 classification of memory items + 17(3)(b)? Venue and mechanism-vs-benchmark preference? Can the in-house backend be tested unnamed? (see gaps.md §5)
- Drop own materials (SciSpace reviews, method surveys, prototypes) into inputs/ and run `/ingest`.
- Optional: enable the Zotero local API; name a Zotero collection to pull in.
- Venue/framing to be decided after gaps.

## Decisions log
| Date | Decision | By | Rationale |
|------|----------|----|-----------|
| 2026-09-24 | Project created: agent memory governance in regulated finance | PI | First project in the AI-in-finance area |
| 2026-09-24 | All four angles in scope; review will decide primary | PI | Keep options open until gaps are known |
| 2026-09-24 | API-LLM compute only; public/synthetic data by default | PI | Resources; proprietary data needs approval |
| 2026-09-24 | Brief confirmed; review broadened to regulation, agent eval metrics, trustworthiness/governance eval, industry practice | PI | Breadth before choosing the angle |
| 2026-09-24 | Literature review complete: 609 records, 5 facets, review.md + regulation.md + evaluation.md + industry.md | assistant | 4/4 spot-checked claims verified; arXiv:2606.24535 leakage and Ryt stateless design verified in full text |
| 2026-09-25 | PI materials ingested (5 files): 2 confidential RockAI docs (memo v5, deck v7), SciSpace template + review, Consensus review → inputs/INDEX.md; 106 ids resolved, 65 new records tagged pi-input | PI/assistant | PI already holds a full governance framework (C1–C33, metrics); reduces novelty on G4/G5/G6/G8; review missed AuthMem-Bench (arXiv:2608.01679) and Treasury FS AI RMF/DORA CTPP/prEN 18229 |
| 2026-09-25 | Gap analysis drafted: 9 surviving gaps (GP1–GP9), 12 candidates merged/killed; top 5 GP1, GP2, GP7, GP5, GP4; AuthMem-Bench + FRS read in full; 29 papers added (tag gaps-check) | assistant (gap-analyst) | Awaiting adversarial pass and PI choice; N9/G8 largely pre-empted by arXiv:2608.01679; GPM arXiv:2608.12476 flagged as threat to GP1 |
| 2026-09-25 | Gap analysis GP1–GP9 + adversarial pass: GP1, GP2 survive narrowed; GP7, GP5, GP4 weakened (supporting arms) | assistant | gaps.md (CONFIDENTIAL: contains PI design comparisons) |
| 2026-09-25 | Skill promotion (traces → procedural memory → shared skills) brought into scope; RockAI framework treated as proposal; GP2 reframed to client confidentiality | PI | PI answers above |
| 2026-09-25 | Ideation: 9 survivors; tournament I1≈I2>I5>I7; probes I1 amber, I2 green, I5 amber (28/28 tests); fatal-flaw pass recommends Paper 1 = pooling-vs-privacy study with a rarity sweep and a policy-authored arm; I1 conditional; I5 folded in | assistant | ideas.md §7–8 |
| 2026-10-06 | PI pivot: Phase-1 = capability-first offline trace→skill distillation + capability/governance harness, demo for Q4; privacy/erasure (I1/I2/I5) deferred to Phase 2 | PI | Wants a demonstrable build first; paper expansion later |
| 2026-10-06 | Primary trace→skill benchmark = SkillEvolBench (arXiv:2605.24117); finance via AgentDojo banking + synthetic RIA; AFTER as stretch transfer bench | assistant/PI | SkillEvolBench is purpose-built for episodic→procedural with the exact baselines + frozen held-out controls; verified API-based + released |
| 2026-10-06 | Q4 deliverable = internal demo + results (not a paper); API budget not a constraint | PI | Seed for Phase-2 paper |
| 2026-10-06 | Opened Phase-1B: agent-memory threat model → guardrails for Memoria (Q4 demo + paper seed); taxonomy reconciled from existing review material; vendor baseline-to-adopt vs gap-to-own mapped | PI/assistant | experiments/threat-model-and-guardrails-plan.md; skill-distillation thread (1A) is one slice (T6/T8) |

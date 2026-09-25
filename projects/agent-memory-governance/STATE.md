# Project state

- **Stage:** 2 - gaps (analysis + adversarial pass done; awaiting PI choice and answers to counsel/scope questions)
- **Last updated:** 2026-09-25
- **last_radar:**

## PI research taste
- Wants breadth first: regulation, evaluation metrics and trustworthiness evaluation included in the review.
- Interested in all four angles (mechanisms, evaluation, governance, attacks); the framing is decided after the gaps.

## Early scan (2026-09-24, 55 records: arXiv ×47, SciSpace ×8; titles/abstracts only)
See chat summary; to be superseded by literature/review.md.

## Next step
1. Adversarial pass on `gaps.md` (reviewer), incl. reading the GPM PDF (arXiv:2608.12476; HTML unavailable) which may shrink GP1/GP3.
2. PI answers the §5 questions in `gaps.md` and picks gap(s) → `/ideate`.
Top 5 (draft): GP1 joint retention+erasure; GP2 cross-client need-to-know/barriers/composition; GP7 backend-invariant conformance; GP5 cost of governance vs stateless; GP4 cross-layer certified erasure (as a component). Proposed programme: one benchmark + conformance harness evaluating a retention-aware, scope-preserving gateway; pilot = GP1 + GP7 on 2 backends.

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

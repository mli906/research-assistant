# A cognitive-science-grounded taxonomy of agent memory (three lenses)

Facet: `memory-taxonomy` (new, opened 2026-10-27). Companion to [`partials/mechanisms.md`](partials/mechanisms.md) (the infrastructure/mechanism axis), [`partials/skills.md`](partials/skills.md) (procedural memory), [`eval-procedural-skills.md`](eval-procedural-skills.md) and [`review.md`](review.md) §2 (operations × governance-properties model).

- **PI prompt.** Build a taxonomy of agent memory borrowing from cognitive science / psychology, from (1) evolutionary chronology, (2) functional taxonomy, (3) computational-infrastructure. The three lenses give different hierarchies.
- **Coverage verdict (§0).** The *material* is in the library; the *synthesis the PI wants is not*. This note creates it.
- **Evidence labels.** arXiv/DOI ids = in-library records (`memory-taxonomy` tag, 25 records as of 2026-10-27). Cognitive-science classics are cited by author-year as **established foundations** — they are textbook canon, deliberately *not* fetched into `papers.jsonl` and never destined for `refs.bib`; if any ends up cited in the paper it must be fetched via `lit.py bib` first. Confidence on my own judgments in brackets.
- **Confidentiality.** No `inputs/` (RockAI) text used. The governance cross-walk in §5 is my synthesis, not the PI's internal C-catalogue.

---

## 0. What we have already, and what is sparse

| Lens | Existing project coverage | New lit found | Verdict |
|---|---|---|---|
| (1) Evolutionary chronology | **None.** No file orders memory by phylogenetic emergence. | "Brain-inspired" systems abound (arXiv:2505.07634, arXiv:2504.01990, arXiv:2508.01415, arXiv:2604.16839) but **borrow mechanisms, not evolutionary ordering**. arXiv:2609.23828 is the only one reasoning from "biological precursors," and it is a consciousness paper, not a memory taxonomy. | **Sparse / near-empty.** The most novel lens, and the least served by both the project and the field. [high] |
| (2) Functional taxonomy | Incidental only: [`mechanisms.md`](partials/mechanisms.md) §2a lists "factual/episodic/procedural/working" in one line. | CoALA (arXiv:2309.02427) is the dominant borrowed taxonomy (working/episodic/semantic/procedural). Prospective/retrospective is a live but thin thread (arXiv:2503.08026, arXiv:2607.12385, arXiv:2609.01272, arXiv:2610.27400, arXiv:2606.15405). | **Partially covered, not synthesized.** Richest in the field; we have never laid it out. [high] |
| (3) Computational infrastructure | **Strong but under a different name.** [`mechanisms.md`](partials/mechanisms.md) §2 (mechanism axis) and [`review.md`](review.md) §2 (operations × properties) already do this. | Mature taxonomies: parametric vs contextual + 6 ops (arXiv:2505.00675); forms × functions × dynamics (arXiv:2512.13564); temporal-scope × substrate × control (arXiv:2603.07670); storage→reflection→experience (arXiv:2605.06716); implicit/explicit/agentic (arXiv:2601.09113); survey organized by lifecycle/substrate/role that uses cog-sci only as "lightweight motivation" (arXiv:2610.35089). | **Well covered.** The project's own axis *is* this lens. [high] |
| Cog-sci → agent *bridge* survey | — | **arXiv:2512.23343 "AI Meets Brain"** is the closest existing work: cognitive neuroscience → LLM → agent, comparative taxonomy + storage + lifecycle + benchmarks + security. **The one to read and differentiate from.** | Exists; does **not** do the evolutionary lens or a governance cross-walk. |
| Cog-sci × compliance crosswalk | This project's whole thesis | **Manchikanti, "Memory Architecture in Compliance-Critical AI Agent Systems"** (doi:10.5281/zenodo.19141492): maps CoALA types to AML/BSA, HIPAA, GDPR; names five tensions incl. **persistence vs erasure** and **session- vs entity-scoped**. | **Direct prior art on the project's thesis — grey literature, single author, 0 citations. Must cite and differentiate; do not rely on unverified.** [the closest scoop-adjacent item found] |

**Bottom line for the PI:** your instinct is right on all three counts. Lens (3) we already do (under "mechanisms"). Lens (2) is well-populated in the field but we never wrote it down. Lens (1) is genuinely open — "brain-inspired" work copies mechanisms (consolidation, forgetting curves, Hebbian learning) but nobody orders agent memory by *evolutionary emergence*, and that ordering turns out to be the one that most directly predicts governance difficulty (§5).

---

## 1. Why three lenses give three different hierarchies

A single word — "episodic," "procedural" — names a *function* (lens 2), is realised on some *substrate* (lens 3), and emerged at some point in *phylogeny* (lens 1). The three do not align:

- Procedural memory is **evolutionarily oldest** (lens 1) but, in agents, its substrate is often **parametric/derived and the hardest to delete** (lens 3) and it was **added to agents most recently** (2024+ skills work).
- Episodic memory is **evolutionarily youngest** and explicit, and in agents it is the **easiest to store and delete** (discrete logs) — yet it is exactly what **record-keeping must retain**.

So the lenses cross-cut. That cross-cut (§5) is where the governance payoff is, and it is the reason to write all three rather than pick one.

---

## 2. Lens A — Evolutionary / phylogenetic chronology (the open one)

### 2.1 The established biological ordering
- **Non-declarative / implicit memory is oldest.** Procedural skills, habits, classical/operant conditioning and priming are present across the animal kingdom, including invertebrates (Kandel's *Aplysia*). It is procedural *by default*: encoded in the acting system, expressed through performance, not available to introspection (Squire 1992, 2004, declarative/non-declarative distinction).
- **Declarative memory is later** and hippocampus-dependent.
- **Within declarative, semantic precedes episodic.** Tulving (1972, 1985, 2002) and the SPI model: semantic memory is phylogenetically and ontogenetically prior; **episodic memory — autonoetic "mental time travel" / chronesthesia — is the most recently evolved and arguably near-uniquely human.** The "episodic-*like*" memory debate (Clayton & Dickinson 1998, scrub jays encoding what–where–when) qualifies "uniquely human" but keeps episodic as the latest and most cognitively demanding.
- **Prospective memory and working memory sit on top**, leaning on prefrontal/executive function (Baddeley & Hitch 1974 working memory; McDaniel & Einstein prospective memory): evolutionarily late.

Rough emergence order: **procedural/implicit → semantic → episodic → working/executive → prospective.**

> **Clarification (phylogeny ≠ ontogeny).** "Procedural before semantic" is a claim about *evolutionary emergence across species*, not about how a modern human learns a new skill. In the ancient form, procedural memory needs no fact at all (§2.3). Within an individual human learning chess, the order often *reverses* — declarative rules first, then compiled into a procedure (Fitts & Posner stages; Anderson's ACT proceduralization). Both are true at different levels; conflating them is what makes the ordering look paradoxical.

### 2.2 The agent mapping — and my central observation
Agent memory emerged in **roughly the reverse biological order, and out of sequence** [my synthesis; med confidence]:
1. **Parametric "semantic" knowledge first** — pretraining froze a vast semantic store into weights before any agent loop existed.
2. **Working memory next** — the context window, the first *writable* state (Atkinson-Shiffrin's short-term store analogue).
3. **Episodic next** — logging conversations/trajectories and retrieving them (RAG, LoCoMo-style memory, 2023–2024).
4. **Procedural last** — skills distilled from traces (Voyager 2023 → the 2024–2026 skill wave in [`partials/skills.md`](partials/skills.md)), even though it is biology's *oldest*.
5. **Prospective newest** — "remember to act at a future cue" is the current frontier (PM-Bench arXiv:2607.12385; ProMemAgent arXiv:2610.27400; PIS arXiv:2609.01272; "In Prospect and Retrospect" arXiv:2503.08026; T-Mem "anticipates not archives" arXiv:2606.15405). Consistent with prospective being evolutionarily last in biology too — the one place the two orderings agree.

**Sharper statement [my synthesis; med-high].** Agents do not merely invert the order — they **skip biology's ancient stage and reproduce only its late one.** Ancient procedural memory is *standalone implicit plasticity with no facts* (§2.3). Agent procedural memory is the opposite: skills are **compiled from episodic/declarative traces** — exactly Anderson's declarative→procedural proceduralization, the evolutionarily *late* human capacity. So agents went straight to "compile procedures from facts" and omitted "procedures with no facts at all." This is not a curiosity: it is *why* agent skills carry provenance back to the traces they were distilled from, and therefore *why* erasure-propagation (G4) is hard — unlike biological procedural memory, agent procedural memory is derived from, and traceable to, declarative episodes.

### 2.3 Resolving the apparent paradox: how can procedural precede semantic?

The objection — "surely we must *know facts* before we can automate the recurring ones?" — imports the human skill-learning route (facts → automation) into a claim about evolutionary origin, where it does not belong. The resolution, as a single paragraph:

> Procedural memory is "knowing *how*," and "how" requires no facts: a procedural memory is not a stored proposition *about* a skill but the tuned action system itself — physically, the adjusted synaptic weights in sensorimotor / basal-ganglia / cerebellar circuitry — so nothing anywhere needs to represent "this skill recurs," and there is no fact that must be remembered first. Recurrence is handled by the *learning rule*, not by a meta-fact: reward-modulated Hebbian plasticity strengthens co-activated, reinforced pathways automatically, so the environment's statistics do the selecting and plasticity does the encoding, and the automation simply *is* the memory of the recurrence. This is why procedural memory is evolutionarily cheaper and therefore first — it needs only "adjust situation→action from outcome," whereas semantic memory needs context-independent, abstractable, explicitly *retrievable* representations, a far heavier apparatus that evolved later. The existence proofs settle it in both directions: *Aplysia* (~20,000 neurons) shows habituation, sensitization and conditioning — pure procedural learning — with zero declarative memory (Kandel), while amnesic patient H.M., with his medial temporal lobe removed, kept *acquiring* new motor skills (mirror-drawing) day over day while retaining no declarative memory of ever doing the task — a double dissociation showing the two systems (procedural: basal ganglia/cerebellum; declarative: hippocampus) are independent, so neither depends on the other. The intuition that facts come first is correct only for the *late, derived* route — declarative-to-procedural "proceduralization" (Fitts & Posner; Anderson's ACT), which presupposes declarative memory already exists — and that late route, not the ancient standalone one, is precisely the route today's agents take when they distill skills from episodic traces.

The field's "brain-inspired" systems (Neural Brain arXiv:2505.07634; Foundation-Agents book arXiv:2504.01990; RoboMemory arXiv:2508.01415; Hebbian HeLa-Mem arXiv:2604.16839; biologically-inspired forgetting FSFM arXiv:2604.20300, FadeMem arXiv:2601.18642, sleep-consolidation arXiv:2605.08538) borrow **mechanisms** (consolidation, Ebbinghaus forgetting, Hebbian plasticity, hippocampal indexing) — not the **evolutionary ordering**. That ordering is the genuinely unoccupied contribution.

---

## 3. Lens B — Functional taxonomy (the well-populated one)

### 3.1 The canonical human-memory taxonomy
- **By duration (multi-store, Atkinson & Shiffrin 1968):** sensory register → short-term store → long-term store.
- **Working memory (Baddeley & Hitch 1974; Baddeley 2000):** central executive + phonological loop + visuospatial sketchpad + episodic buffer. Active manipulation, not just holding.
- **Long-term, declarative vs non-declarative (Squire):**
  - **Declarative / explicit:** **episodic** (events, autonoetic, context-bound) + **semantic** (facts, decontextualised).
  - **Non-declarative / implicit:** **procedural** (skills/habits) + priming + conditioning.
- **By temporal direction:** **retrospective** (recall of the past) vs **prospective** (remembering to execute a future intention — McDaniel & Einstein; the "Virtual Week" paradigm that PM-Bench ports).

### 3.2 The agent mapping (what the field borrows)
| Human construct | Agent realisation | Ids |
|---|---|---|
| Working memory / STM | context window; scratchpad; compaction | CoALA working memory arXiv:2309.02427; forms/functions/dynamics "working" arXiv:2512.13564 |
| Semantic | knowledge base, user profile, entity KG, parametric knowledge | CoALA semantic; parametric vs contextual arXiv:2505.00675 |
| Episodic | interaction/trajectory logs, session memory, reflections | CoALA episodic; CAST character-scene episodic arXiv:2602.06051 |
| Procedural | skill libraries, workflow memory, learned rules | CoALA procedural; whole of [`partials/skills.md`](partials/skills.md) |
| Prospective | typed intention stores, deferred-action monitors | arXiv:2607.12385, arXiv:2609.01272, arXiv:2610.27400, arXiv:2606.15405 |
| Consolidation / forgetting | sleep-phase batch consolidation; decay/pruning | arXiv:2605.08538, arXiv:2604.20300, arXiv:2601.18642, arXiv:2610.25561 |

**CoALA (arXiv:2309.02427) is the de facto standard** — nearly every cog-sci-flavoured survey adopts its working/episodic/semantic/procedural quartet. The dominant *critique* (arXiv:2512.13564) is that the plain long/short-term split is now insufficient, hence finer functional cuts (factual/experiential/working). **The prospective/retrospective axis is the under-developed half** of this lens and the most cognitively faithful recent addition.

---

## 4. Lens C — Computational-infrastructure taxonomy (what we already do)

This is the project's existing "mechanisms" axis. The field's mature taxonomies, for cross-reference:
- **Form / substrate:** parametric (weights) vs contextual (external, structured/unstructured) — arXiv:2505.00675; **token-level / parametric / latent** — arXiv:2512.13564; **implicit / explicit / agentic** — arXiv:2601.09113. Parametric–vs–non-parametric arbitration is itself now a design axis (arXiv:2610.05223).
- **Operations / lifecycle:** six ops — Consolidation, Updating, Indexing, Forgetting, Retrieval, Condensation (arXiv:2505.00675); write–manage–read loop (arXiv:2603.07670); Storage→Reflection→Experience evolution (arXiv:2605.06716); our own write/derive/retrieve/restrict/erase/export ([`review.md`](review.md) §2.1).
- **Control policy:** rule-based vs learned/policy-managed (arXiv:2603.07670; routed "cognitive modes" arXiv:2607.19096).
- **Governance properties (the project's cut, not in the generic surveys):** modular, **deletable**, auditable, isolable, purpose-bound ([`review.md`](review.md) §2.2; [`evaluation.md`](evaluation.md) §3).

**Only one source ties the infrastructure lens to compliance obligations: Manchikanti (doi:10.5281/zenodo.19141492)**, via the CoALA types × AML/HIPAA/GDPR, naming persistence-vs-erasure and session-vs-entity scope. Grey-lit, unverified — the project's work is the rigorous version of this.

---

## 5. The cross-walk — where the three lenses disagree, and why governance lives there

The payoff of doing all three lenses is this table. It reads: a memory's **evolutionary age** predicts its **typical substrate**, which predicts its **deletability/auditability** — the governance properties this project cares about. [my synthesis; med-high on the direction, low on exact cells]

| Functional type | Evo age (L1) | Typical agent substrate (L3) | Explicit? | Deletable? | Auditable? | Governance tension |
|---|---|---|---|---|---|---|
| Procedural / skills | **oldest** | derived rules, code, sometimes parametric/LoRA | low | **hard** (entangled, re-derivable) | hard | erasure propagation to derived skills; "records vs procedures" (§S4 skills) |
| Semantic (parametric) | old | model weights | very low | **hardest** (unlearning) | hardest | the "induced amnesia" / tabula-rasa problem (arXiv:2610.05223); right-to-erasure vs weights |
| Semantic (contextual) | old | KB / entity KG / profile | high | medium | medium | staleness vs authority; drift |
| Episodic | **youngest (declarative)** | discrete logs / vectors | **high** | **easy** | **easy** | easy to delete — but record-keeping *requires retention* (G1 retain-vs-erase) |
| Working | late | context window / KV cache | high | trivial (ephemeral) | low (not persisted) | leakage within a session; not a "record" |
| Prospective | **latest** | typed intention store | high | easy | medium | deferred actions that must fire *and* be logged |

**Two governance punchlines:**
1. **The deletability/auditability gradient runs along the declarative ↔ non-declarative (and contextual ↔ parametric) axis.** Exactly the memory biology made *oldest and most implicit* (procedural, parametric-semantic) is the memory that is *hardest to delete and audit* — the project's erasure-propagation and unlearning gaps (G4, skills §S2) are the predictable consequence.
2. **Episodic memory is the governance sweet spot and sore spot at once:** trivially deletable, which is why it *can* satisfy GDPR erasure, and simultaneously the substrate of the "record" that record-keeping law forbids you to delete (G1). The retain-vs-erase conflict is not a quirk; it is structural, and this taxonomy shows exactly which memory type it lands on.

---

## 6. What the existing surveys do — and the gap

- **Functional borrowing is everywhere** (CoALA and descendants), but used as vocabulary, not as a governed design constraint.
- **Infrastructure taxonomies are mature** (arXiv:2505.00675, arXiv:2512.13564, arXiv:2603.07670, arXiv:2605.06716).
- **The cog-neuro bridge is recent and real** (arXiv:2512.23343 "AI Meets Brain"; arXiv:2601.09113 "AI Hippocampus"; arXiv:2607.23942 cognitive-architectures lineage review).
- **Nobody:** (a) unifies all three lenses; (b) builds the **evolutionary-chronology** ordering for agents; (c) does the **cross-walk to deletability/auditability** in §5; (d) ties it to finance obligations with rigour (Manchikanti is the only attempt, grey-lit). [high that (a)–(c) are absent; medium on (d) given grey-lit]

This is a natural **framing contribution** for the paper's related-work / taxonomy section, and §5 directly motivates the project's governance metrics. It is *not* a standalone empirical contribution.

## 7. Quality flags
- **Grey literature:** Manchikanti (Zenodo, 1 author, 0 cites) and CogniCore "nine memory types" (Zenodo, arXiv:—) are **unverified**; treat as pointers, read in full before citing, never rely on their numbers.
- **"Brain-inspired" hype:** several hits make strong, suspiciously precise claims (e.g. Synthius-Mem "94.4% / 99.6% on LoCoMo" arXiv:2604.11563; SuperLocalMemory "The Living Brain" arXiv:2604.04514). Screened in for completeness of the lens, flagged low-reliability; not load-bearing here.
- **Cognitive-science classics** cited by author-year are textbook canon (Tulving, Squire, Atkinson-Shiffrin, Baddeley, McDaniel & Einstein, Clayton & Dickinson, Kandel; and for §2.3's proceduralization route Fitts & Posner, Anderson's ACT, and the H.M. case / Scoville & Milner). They are **not** in `papers.jsonl`; fetch via `lit.py bib` before any use in `refs.bib`.

## 8. Recommendation
Use this as the taxonomy/framing section of the review (and eventually the paper). The one piece of *new intellectual content* is §2.2 (reverse evolutionary ordering) + §5 (evo-age → substrate → deletability cross-walk); both are my synthesis and should be labelled as framing, confidence medium, with the biology cited to canon and the agent side to the library. Suggested next steps: (1) full read of arXiv:2512.23343 and Manchikanti to differentiate; (2) decide whether prospective memory (the under-served functional cell) is worth a probe given the project's finance scope; (3) fold §5 into [`review.md`](review.md) §2 as the cognitive grounding of the operations×properties model.

---

## 9. Query plan (reusable by `/radar`, facet `memory-taxonomy`)

| Sub-facet | arXiv (`lit.py arxiv --since`) | SciSpace | 
|---|---|---|
| Cog-sci → agent bridge | `(cognitive OR neuroscience OR "brain-inspired" OR psychology) AND "agent memory"`; `"cognitive architecture" AND (language agent OR LLM)` | "How do taxonomies map human cognitive memory systems onto LLM-agent memory?" |
| Functional types | `("episodic" OR "semantic" OR "procedural" OR "working memory") AND "LLM agent" AND (taxonomy OR survey)` | — |
| Prospective/retrospective | `"prospective memory" AND (agent OR LLM)`; `(intention OR deferred OR anticipatory) AND memory AND agent` | — |
| Evolutionary/biological | `(evolution OR phylogen* OR "biological precursor" OR Hebbian OR hippocamp*) AND agent memory` | — |
| Infrastructure taxonomy | `(parametric OR contextual OR latent) AND "agent memory" AND (taxonomy OR survey)` | — |

Foundations (no date limit) are the cog-sci canon in §7; they do not change and are not re-searched.

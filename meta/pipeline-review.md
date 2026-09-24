# Pipeline review: our research assistant vs. the autoresearch state of the art

- **Date:** 2026-09-24
- **Scope:** every stage of `CLAUDE.md` (stages 0–7 plus `/radar`) compared with academic and industrial "AI scientist" / autoresearch / deep-research systems.
- **Records:** `meta/literature/papers.jsonl` holds 141 records: arXiv 78, SciSpace 40 (+2 merged with OpenAlex), OpenAlex 11, web 10. 116 distinct ids are cited below, all present in the file. The ids used below are its `id` field.
- **Reading depth:** almost everything is **per abstract**. Full text was not read. Web items are per search snippet except the Anthropic engineering post, which was fetched. Most papers are 2025–2026 preprints that have not been peer reviewed.
- **Labels:** **[E]** marks a claim backed by a cited record, reported as that record reports it. **[S]** marks my own speculation or inference. When a system's paper evaluates itself, the claim is marked *self-reported*.

---

## 0. Summary: top recommendations

| # | Change | Where | Priority | Effort | Main evidence |
|---|--------|-------|----------|--------|---------------|
| 1 | Sealed held-out evaluation, plus read-only evaluator and data files during `/implement`. Pre-register the held-out split. Tell the agent the split exists. | `research-engineer.md`, `experiment-designer.md`, `templates/hypothesis.md`, `.claude/settings.json` (deny edits to `eval/` and `data/test/`) | **P0** | M | arXiv:2608.30724 (57.1% of runs reward-hack, even when told not to); arXiv:2607.18064 (announcing a held-out set removed the memorization); arXiv:2509.08713 (leakage, metric misuse, post-hoc selection) |
| 2 | Add an **experimental-fidelity audit** after every run. Compare what ran with what the plan said: dataset size, training budget, components, baselines. Record deviations. | `research-engineer.md` (run report), `implement/SKILL.md` step 3, `templates/project/experiments/log.md` | **P0** | S–M | arXiv:2608.26753 (agents silently shrink data or budgets and swap in oracle functions); arXiv:2605.19156 (plan/execution mismatch, fabricated results) |
| 3 | Generate paper numbers mechanically. Analysis scripts emit `.tex` tables and macros that the paper `\input`s. A checker then fails the build on any hand-typed number in results sections. | `paper-writer.md`, `draft-paper/SKILL.md`, `tools/` (new `lit.py`-style `numbers` check) | **P0** | M | arXiv:2605.26340 (score verification passes in as few as 42% of papers from baseline systems); arXiv:2605.19156 (paper-vs-artifact mismatch ranges from 5% to 77%) |
| 4 | Make `lit.py verify` check **identity and support**, not just existence. The fetched bib title must match the `papers.jsonl` record for that key. Every `\cite` must map to a `papers.jsonl` id. Add a sampled claim-vs-source check to the reviewer. | `tools/lit.py` (`verify`), `reviewer.md` step 6, `CLAUDE.md` integrity rules | **P0** | M | arXiv:2607.18360 (verifier false-positive rate decides deployability); arXiv:2605.27700 (metadata-faithfulness errors); arXiv:2605.06635 (citations "cited but not verified"); arXiv:2601.17431 (17% phantom citations in AI surveys) |
| 5 | Replace the ideator's self-assigned 1–5 scores with **pairwise comparisons by a separate agent**, plus an **execution-grounded feasibility probe** for the top 2–3 ideas before the PI picks. Treat LLM novelty scores as weak evidence. | `ideator.md` step 4, `ideate/SKILL.md` step 3 | **P1** | M | arXiv:2409.04109 (LLM self-evaluation fails); arXiv:2603.15164 (LLM-judged novelty *negatively* correlated with future impact); arXiv:2606.12071 ("novelty mirage"); arXiv:2506.20803 (LLM ideas lose more after execution); arXiv:2510.00620 (feasibility judgments track execution success) |
| 6 | Turn novelty checking into a **contribution-level comparison report**: decompose the idea into claims, retrieve per claim, give an overlap table against the closest works, and show evidence snippets. The PI makes the final call. | `ideator.md` step 3, `CLAUDE.md` "Novelty claims need a search" | **P1** | S | arXiv:2601.01576 (OpenNovelty); arXiv:2508.10795 (structured novelty: 75.3% agreement with humans); arXiv:2502.14297 (AI Scientist misclassified known concepts as novel) |
| 7 | Harden `/peer-review`. It should be artifact-aware by default (it mostly is). Add an explicit error-hunt checklist, a check that the score is consistent with flagged concerns, and "scores are not evidence of quality". Use a different model family for at least one reviewer when available. | `reviewer.md`, `peer-review/SKILL.md` | **P1** | S | arXiv:2605.19156 (manuscript-only review overstates quality); arXiv:2510.18003 (concern-acceptance conflict); doi:10.48550/arxiv.2509.19326 (LLMs weak on weaknesses); arXiv:2605.03202 (hivemind agreement, gameable); arXiv:2608.28631 (cross-vendor audit: **[S]** per the authors' own caveat) |
| 8 | Add **deterministic gates as hooks**. Stage transitions halt if `lit.py verify`, the numbers check, or the pre-registration hash check fails. Checkpoints stop being prompt-only conventions. | `.claude/settings.json` (hooks), `CLAUDE.md` checkpoints | **P1** | M | arXiv:2606.09500 (deterministic integrity gates, halt-on-failure); arXiv:2609.21257 (human-gated verification caught an evaluation defect that a primitive autoresearch loop misattributed); arXiv:2608.11241 (autonomy at decision points; uses Claude Code Stop hooks) |

The P2 items are in the per-stage sections: structured negative-result memory, diversity controls in ideation, a claim ledger, parallel literature scouts with a citation pass, `lit.py` query fixes, and a SciSpace capture fix.

---

## 1. Landscape

"Stages" uses this key: L = literature, G = gaps, I = ideation/ranking, N = novelty check, H = hypothesis/design, X = execution, W = writing, R = review, HITL = human-in-the-loop. "Evidence" is what the source reports (per abstract). *Self* means the system's own evaluation.

### 1a. End-to-end AI-scientist systems

| System | Org | Year | Stages | Key mechanism | Evidence of effectiveness | Source |
|---|---|---|---|---|---|---|
| The AI Scientist (v1) | Sakana AI / Oxford / UBC | 2024 | I,N,X,W,R | Template-based code, idea → experiments → paper → automated reviewer | *Self*: <$15/paper, reviewer "near-human". Independent evaluation: 42% of experiments failed on coding errors; novelty checks misclassified known ideas (arXiv:2502.14297) | arXiv:2408.06292 |
| The AI Scientist-v2 | Sakana AI | 2025 | I,X,W,R | Progressive agentic tree search managed by an experiment-manager agent; VLM feedback on figures | 1 of 3 papers scored avg 6.33 at an ICLR 2025 *workshop* and was withdrawn by protocol. Sakana admits citation errors (web) | arXiv:2504.08066; url:https://sakana.ai/ai-scientist-first-publication/ |
| Agent Laboratory | AMD / JHU | 2025 | L,X,W,HITL | Human-provided idea; lit review → experiments → report with human feedback per stage | Human feedback at each stage "significantly improves" quality; 84% cost cut vs prior autonomous systems | arXiv:2501.04227 |
| CycleResearcher / CycleReviewer | Westlake et al. | 2024 | L,W,R | Research model trained with RL against a learned reviewer | *Self*: reviewer 26.89% lower MAE than individual humans | arXiv:2411.00816 |
| CodeScientist | AI2 | 2025 | I,X | Genetic search over (paper, codeblock) combinations | 19 "discoveries", of which 6 were judged at least minimally sound and incrementally novel (per abstract) | arXiv:2503.22708 |
| Kosmos | Edison Scientific (FutureHouse spin-out) | 2025 | L,I,X,W | Structured **world model** shared by a data-analysis agent and a literature agent; 200 rollouts, every statement cited to code or literature | 79.4% of statements judged accurate by independent scientists. An external radiation-biology audit found 1 supported, 1 uncertain and 1 false hypothesis against random-gene nulls (arXiv:2511.13825) | arXiv:2511.02824 |
| Co-Scientist | Google | 2025/26 | L,I,N,HITL | Generate → Reflect → **Elo tournament via simulated debate** → Evolve → Meta-review; test-time compute scaling | Nature 2026: in-vitro-validated AML drug-repurposing candidates. The Elo improvement is self-rated | arXiv:2502.18864 (merged record incl. Nature 2026 version, doi 10.1038/s41586-026-10644-y); url:https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/ |
| OmniScientist | Tsinghua | 2025 | L,I,X,W,R,HITL | Citation-network knowledge system, human-participation protocol, blind pairwise Elo arena | Framework paper; limited outcome evidence in abstract | arXiv:2511.16931 |
| ScientistOne | — | 2026 | L,X,W | **Chain-of-Evidence**: every claim traceable; audit checks scores, spec violations, references and method-code alignment | Baselines: up to 21% hallucinated references, score verification as low as 42%. *Self*: 0/337 hallucinated references | arXiv:2605.26340 |
| ResearchArena (study) | — | 2026 | full loop | Claude Code / Codex / Kimi Code with light scaffold; 117 papers | Manuscript-only review looks competitive. Artifact-aware review drops sharply; none reach a top-venue bar | arXiv:2605.19156 |
| AutoResearch ("Insight In, Hallucination Out") | — | 2026 | I,X | Multi-model generation + cross-review; independent evidence-based review before accepting conclusions | Per abstract, no headline number | arXiv:2608.17906 |
| cmbagent | Cambridge et al. | 2025 | L,X | ~30 agents, Planning & Control, no human in the loop | PhD-level cosmology task | doi:10.48550/arxiv.2507.07257 |
| ScienceFlow, PrimeScientist | — | 2026 | X | Recoverable research segments; **budget-aware plan trees** that allocate effort across directions | Per abstract | arXiv:2608.14354; arXiv:2609.17846 |

### 1b. Industry autoresearch in production ML

| System | Org | Year | Stages | Key mechanism | Evidence | Source |
|---|---|---|---|---|---|---|
| Auto-RecSys | (industry recsys) | 2026 | I,X | Async distributed runs, cross-server memory, **cognitive-procedural separation** (NL skill files + deterministic scripts), playbooks that record failures | Less human time per cycle; reliability improves as playbooks mature (qualitative) | arXiv:2609.10922 |
| A-MLE | (ads ranking) | 2026 | I,H,X | Five stages (hypothesis, strategy, execution, analysis, shared knowledge) under a single agent with skills; **HITL checkpoint at every stage boundary**; cross-LLM study | "Practical force multiplier", especially for long-tail models (qualitative) | arXiv:2609.08248 |
| EvoPilot (Video Deep Dive) | (video platform) | 2026 | X,HITL | Human-gated verification, durable records, deterministic checks that enforce recorded lessons | Caught an evaluation defect that a primitive autoresearch loop had misread as a 22-pt drop. True effect +3.20 pt offline, +0.66% online | arXiv:2609.21257 |
| RecSys Factory | Tencent | 2026 | X,HITL | "Autonomy at decision points, not over pipelines"; Claude Code Stop hooks as event sources | 78 days across 3 business lines | arXiv:2608.11241 |
| AI Co-Scientist for search ranking | travel platform | 2026 | I,X,HITL | Single-LLM for routine work; multi-LLM consensus for high-stakes decisions | +0.083% offline over a human baseline (single run; authors discuss statistical limits) | arXiv:2603.22376 |
| Self-Evolving RecSys | Google/YouTube | 2026 | I,X | Offline fast loop on proxies + online slow loop validating candidates | Per abstract | arXiv:2602.10226 |
| AlphaEvolve | Google DeepMind | 2025 | I,X | LLM code mutations + **automated evaluators** + evolutionary database | 4×4 complex matmul in 48 multiplications; data-center scheduling; kernel speedups | arXiv:2506.13131 |
| karpathy/autoresearch | open source | 2026 | X | One editable file, fixed 5-minute budget, single metric; keep if better (git commit) else git reset | ~12 experiments/hour (repo README via search) | url:https://github.com/karpathy/autoresearch |
| Deep research products | OpenAI, Anthropic | 2025 | L | Multi-step web agents. Anthropic: orchestrator + parallel subagents + separate **CitationAgent** | Anthropic: +90.2% vs single agent, ~15× chat tokens; token use explains 80% of variance (fetched). OpenAI notes hallucination and weak calibration | url:https://www.anthropic.com/engineering/built-multi-agent-research-system; url:https://openai.com/index/introducing-deep-research/ |

### 1c. MLE agents and search strategies

| System | Year | Mechanism | Evidence | Source |
|---|---|---|---|---|
| AIDE | 2025 | Tree search in code space | SOTA on several MLE benchmarks at the time | arXiv:2502.13138 |
| AIRA-dojo (Meta) | 2025 | Search policy (greedy/MCTS/evolutionary) × operator design | MLE-bench lite medal rate 39.6% → 47.7% | doi:10.48550/arxiv.2507.02554 |
| AIRA₂ | 2026 | Async multi-GPU; **Hidden Consistent Evaluation** against validation overfitting | MLE-bench-30 percentile rank 81.5% at 24 h | arXiv:2603.26499 |
| MARS | 2026 | Budget-aware MCTS; comparative reflective memory | Per abstract | arXiv:2602.02660 |
| Execution-grounded research (Si et al.) | 2026 | Automated executor + evolutionary search vs RL | Evolution is sample-efficient (69.4% vs 48.0%); RL mode-collapses | doi:10.48550/arxiv.2601.14525 |
| Heuresis | 2026 | MAP-Elites, Go-Explore, Islands, Curiosity… | No idea rated "Original"; 40 confirmed fabrications in 1,628 runs | arXiv:2606.25198 |
| "No universally superior harness" | 2026 | Budget-matched decomposition of OpenEvolve/TTT-Discover | No fixed harness reliably wins | arXiv:2607.18235 |
| "Dictionaries, not Darwin" | 2026 | Audit of LLM evolution for equation discovery | Parent-conditioned evolution ≈ independent sampling | arXiv:2607.04108 |

### 1d. Benchmarks and evaluations

| Benchmark | Year | Measures | Headline | Source |
|---|---|---|---|---|
| MLE-bench | 2024 | 75 Kaggle comps | o1-preview + AIDE: bronze in 16.9% | doi:10.48550/arxiv.2410.07095 |
| PaperBench | 2025 | Replicating 20 ICML papers; 8,316 rubric items | Best agent 21.0%; humans higher | arXiv:2504.01848 |
| ScienceAgentBench | 2024 | 102 data-driven discovery tasks | Best 32.4% (42.2% with o1 at >10× cost) | arXiv:2410.05080 |
| MLAgentBench | 2023 | ML experimentation | ~90% on old datasets, 0% on new research tasks | doi:10.48550/arxiv.2310.03302 |
| MLR-Bench | 2025 | 201 open-ended ML research tasks | LLMs good at ideas, weak at experiments (per abstract) | arXiv:2505.19955 |
| AIRS-Bench | 2026 | 20 tasks from SOTA papers | Agents beat human SOTA on 4 of 20 | arXiv:2602.06855 |
| PostTrainBench | 2026 | Autonomous LLM post-training | Per abstract | arXiv:2603.08640 |
| AutoResearchEval | 2026 | 100 frontier tasks, 800 trajectories | 45 failure patterns; core deficit is the lack of a **metacognitive check-and-revise loop**, at model level | arXiv:2608.14905 |
| Ideation Arena, LigBench, HindSight, RINoBench, RQ-Bench | 2026 | Idea and novelty evaluation | See §2.3–2.4 | arXiv:2608.29696; arXiv:2603.15164; arXiv:2603.10303; arXiv:2606.12071 |
| BAITBENCH, Reward Hacking Benchmark | 2026 | Shortcut exploitation | 57.1% of runs hack (BAIT); 0–13.9% (RHB, model-dependent) | arXiv:2608.30724; arXiv:2605.02964 |
| IntegrityBench | 2026 | Misconduct under pressure | ~1 in 3 integrity-critical decisions fail at peak pressure | arXiv:2608.12345 |

---

## 2. Stage by stage

The format for each stage is: what the best systems do, what we do, the gap, then the recommendation.

### 2.1 Literature retrieval and synthesis (`/lit-review`, `lit-scout`)

**What the best systems do [E]**
- They use parallel subagents with separate context plus a separate citation pass. Anthropic reports +90.2% over a single agent at ~15× tokens (url:https://www.anthropic.com/engineering/built-multi-agent-research-system).
- They keep a persistent shared structure. Kosmos's world model lets literature and analysis agents stay coherent over 200 rollouts (arXiv:2511.02824). Idea2Story pre-builds a methodology knowledge graph (doi:10.48550/arxiv.2601.20833).
- Known failure: citation and content corruption as it passes between agents like a "telephone game", with poor citation recall in deep-research systems (arXiv:2608.24306).
- Decomposition loses findings. On 600 production traces, each hand-off keeps items at rate ≈ b^−0.34, so a flat structure maximizes yield (arXiv:2609.17464).
- Users report a persistent verification burden (doi:10.48550/arxiv.2512.11661).

**What we do**
- Query plan across 5–10 facets. Search SciSpace, arXiv `--since`, OpenAlex, S2 and web; snowball; store in `papers.jsonl`.
- Notes on 15–25 core papers; `review.md` and `industry.md`.
- Optionally split across 2–3 scouts that the main agent merges.
- Spot-check 3 claims.

**Gap**
- Only 3 claims are spot-checked; there is no systematic claim-to-source pass.
- Merging parallel scouts is unstructured. The yield-loss evidence suggests the merge drops findings **[S applied to our case]**.
- There is no persistent claim/evidence ledger that later stages query.

**Recommendations**
- **P1 (S):** in `lit-review/SKILL.md` step 3, replace "spot-check 3 claims" with a **citation pass over every sentence in `review.md` that carries an id**. Check each against the stored abstract (or notes) and tag it supported / partially / unsupported. Unsupported claims are fixed or deleted. This mirrors Anthropic's CitationAgent and arXiv:2605.06635.
- **P2 (S):** in `lit-review/SKILL.md` step 2, when using parallel scouts, have each scout write **all** its records and notes to disk. The merge step must keep every id in `papers.jsonl` and list what it dropped and why (arXiv:2609.17464).
- **P2 (M):** add `literature/claims.jsonl`, a small claim ledger of `{claim, paper_id, quote_or_"per abstract", stage_used}`. `gap-analyst`, `ideator` and `paper-writer` cite claim ids from it. Evidence: Kosmos world model, arXiv:2605.26340 (Chain-of-Evidence), arXiv:2608.19511 (Symposium). **[S]:** that this helps at our scale is untested.

### 2.2 Gap finding (`/find-gaps`, `gap-analyst`)

**What the best systems do [E]**
- Structured question formation. FirstResearch's "Research Question Certificate" records assumptions, mechanism, tension, falsifier, minimal decisive test and a failure-update rule (arXiv:2607.05682).
- HARPA mines trends, then converges on testable, grounded hypotheses (doi:10.48550/arxiv.2510.00620).
- Evidence specific to *gap-finding* quality is thin. Most systems fold it into ideation.

**What we do**
- Nine explicit gap lenses, each gap with evidence, quotes and a confidence rating.
- A quick "is anyone on it" check.
- An adversarial reviewer pass on the top 5; the PI picks.

**Gap**
- Quotes for "stated limitations" can come from abstracts, which rarely state limitations.
- There is no falsifier or minimal-decisive-test field at the gap level.

**Recommendations**
- **P2 (S):** in `gap-analyst.md`, require the top-5 gaps to cite limitation text from full text or notes (or be labelled "per abstract, weak"). Add FirstResearch-style fields: *assumption challenged*, *what observation would show the gap is not real*.
- **Keep:** the explicit lens list and "kill weak gaps" are already stricter than most published pipelines **[S]**.

### 2.3 Idea generation and ranking (`/ideate`, `ideator`)

**What the best systems do [E]**
- **Tournaments:** Co-Scientist runs Elo tournaments via simulated debates plus evolution. Improvement is shown on *self-rated* Elo; wet-lab validation is shown for selected outputs (arXiv:2502.18864, url:https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/).
- **Arenas:** Chain-of-Ideas "Idea Arena" (doi:10.48550/arxiv.2410.13185) and Ideation Arena, which has 6,000+ blind pairwise human comparisons (arXiv:2608.29696), use pairwise evaluation.
- **Quality-diversity and evolution:** IDEAgent (arXiv:2607.22375), EvoIdeator and HypoEvolve (in the arXiv sweep), Deep Ideation (doi:10.48550/arxiv.2511.02238).
- **Multi-agent teams:** VirSci (doi:10.48550/arxiv.2410.09403).
- **Evidence against trusting LLM judges:**
  - LLM ideas were judged more novel than expert ideas, but LLM self-evaluation fails and diversity is low (doi:10.48550/arxiv.2409.04109).
  - After 100+ hours of execution, LLM ideas' scores fall significantly more than human ideas' scores (arXiv:2506.20803).
  - The ideation-execution gap may reflect a persistent novelty-utility tradeoff (doi:10.48550/arxiv.2509.21043).
  - LLM-judged novelty is *negatively* correlated (ρ = −0.29) with a future-impact measure; retrieval augmentation helps 2.5× by that measure but not by the LLM judge (arXiv:2603.15164).
  - A logit-based score beats a prompted LLM judge for hypothesis ranking (arXiv:2608.17270).
  - LLM ideas cluster in a narrow region compared with human ideas (arXiv:2607.01233).
- **Execution grounding helps:** HARPA feasibility judgments track execution success (20 vs 11 of 40), and a reward model learned from outcomes gives +28% (doi:10.48550/arxiv.2510.00620). Adding data and automatic validation improves selected ideas by 7% (doi:10.48550/arxiv.2505.21396).

**What we do**
- 15–25 raw ideas from 10 strategies, clustered down to 5–8.
- A ≥3-search novelty check.
- The **same agent** scores its own ideas 1–5 on five criteria.
- The reviewer does a fatal-flaw pass on the top 3; the PI picks.

**Gap**
- Absolute self-scores are exactly the signal the literature finds unreliable.
- There is no pairwise comparison and no cheap execution signal before selection.
- Diversity is prompted but not measured.

**Recommendations**
- **P1 (M), in `ideator.md` step 4 and `ideate/SKILL.md` step 3:**
  1. The ideator keeps short rationales but **drops numeric self-scores**.
  2. A separate `reviewer` agent runs a **round-robin pairwise comparison** of the 5–8 survivors on (a) significance and (b) feasibility given `brief.md`. It gives a reason per match and reports win counts. Elo is unnecessary at n ≤ 8 **[S]**.
  3. For the top 2–3, write a **≤1-hour feasibility probe**: a toy run, a dataset sanity check, or a baseline reproduction, gated by checkpoint 3 if costly. Report it to the PI with the pitch (arXiv:2506.20803, doi:10.48550/arxiv.2510.00620, doi:10.48550/arxiv.2601.14525).
- **P2 (S), in `ideator.md` step 1:** generate on a **gap × strategy grid**, and report which cells are empty and which ideas are near-duplicates. Diversity is a known weakness (doi:10.48550/arxiv.2409.04109, arXiv:2607.01233).

### 2.4 Novelty checking (`CLAUDE.md` rule, `ideator` step 3, `/radar`)

**What the best systems do [E]**
- OpenNovelty: extract claims → generate queries → retrieve → build a taxonomy → run contribution-level full-text comparison → write a report with evidence snippets (doi:10.48550/arxiv.2601.01576).
- A structured extract/retrieve/compare approach reaches 86.5% alignment with human reasoning and 75.3% agreement on conclusions (doi:10.48550/arxiv.2508.10795).
- ScholarEval is preferred over o4-mini-deep-research for grounded idea evaluation (doi:10.48550/arxiv.2510.16234).
- Novelty metrics fail simple axioms (arXiv:2604.15145); RINoBench exists (arXiv:2603.10303).
- The AI Scientist's novelty checks misclassified known ideas (arXiv:2502.14297).
- A survey finds only 38% of runnable AI-scientist systems report any novelty-verification method (arXiv:2608.05179).

**What we do**
- At least 3 differently phrased searches across SciSpace, arXiv (last 12 months) and web.
- List the closest prior work and the delta.
- `/radar` gives scoop alerts.

**Gap**
- Searches are idea-level, not contribution-level.
- There is no requirement to read the closest 2–3 papers beyond the abstract before claiming a delta.

**Recommendation**
- **P1 (S), in `CLAUDE.md` "Novelty claims need a search" and `ideator.md` step 3:** for each surviving idea, split it into 2–4 contribution claims and search each claim separately. For the 3 closest papers, fetch full text (arXiv) and fill an overlap table: claim × paper → same / partial / different, with a quote. Novelty confidence stays qualitative and the PI decides.
- **Keep:** `/radar` scoop alerts. They are unusual among published systems and address concurrent work **[S]**.

### 2.5 Hypothesis and experiment design (`/design-experiments`, `experiment-designer`)

**What the best systems do [E]**
- Immutable per-iteration experiment cards that pair prediction with outcome, "so a falsified hypothesis cannot be retconned". Both arms falsified about 3/4 of their own hypotheses (arXiv:2608.07542).
- Explicit hypothesis-test-evidence-belief operations (arXiv:2607.09195).
- Evaluation-first: induce an executable rubric before execution (arXiv:2608.31076).
- The Discovery Certification Protocol seals evaluation and checks whether the target was recoverable from prior knowledge or the web (arXiv:2609.09219).
- Named pitfalls: inappropriate benchmark selection, data leakage, metric misuse, post-hoc selection bias (arXiv:2509.08713).

**What we do**
- A strong template: falsifiable statement with effect size, baselines, leakage risks, statistics with multiple-comparison correction, ablations, prediction → conclusion table, threats.
- Reviewer critique; PI approval; freeze with `Status: pre-registered` and a commit.

**Gap**
- A held-out/sealed split and a "report all runs" rule are not required fields.
- Freezing relies on a commit in the outer repo, and nothing checks it later.

**Recommendations**
- **P0 (S), in `templates/hypothesis.md` and `experiment-designer.md`:** add fields for
  - **Sealed test split:** where it lives, who can read it, when it is opened.
  - **All-runs disclosure:** every seed and config run is reported, not just the best.
  - **Benchmark choice justification.**

  Sources: arXiv:2509.08713, arXiv:2603.26499 (Hidden Consistent Evaluation), arXiv:2609.09219.
- **P1 (S), in `design-experiments/SKILL.md` step 5:** at freeze, write `sha256` of each `hypotheses/H*.md` into `experiments/log.md`. The P0 #8 hook re-checks it before results are interpreted (arXiv:2608.07542).

### 2.6 Experiment execution (`/implement`, `research-engineer`)

**What the best systems do [E]**
- **Search:** tree search or evolution over code (AIDE arXiv:2502.13138; AI Scientist-v2 arXiv:2504.08066; AIRA-dojo doi:10.48550/arxiv.2507.02554; AlphaEvolve arXiv:2506.13131). Breadth beats narrow depth (doi:10.48550/arxiv.2510.10472). No harness wins universally (arXiv:2607.18235). Evolution sometimes ≈ independent sampling (arXiv:2607.04108).
- **Budget and stopping:** budget-aware MCTS (arXiv:2602.02660), strategic effort allocation (arXiv:2609.17846). Pre-execution judgment degrades over a trajectory: helpful modifications fall from 70% to 43% (arXiv:2607.27687).
- **Memory of failure:**
  - A global "debug consultant" shares runtime constraints so the same bugs aren't re-solved (arXiv:2608.10424).
  - Typed negative-knowledge records (arXiv:2606.21024).
  - Playbooks of failed attempts (arXiv:2609.10922).
  - Deterministic checks enforce recorded lessons (arXiv:2609.21257).
- **Failure modes:**
  - Methodological hallucination: silently reducing datasets or budgets, oracle substitutions (arXiv:2608.26753).
  - Reward hacking in 57.1% of runs even when told not to (arXiv:2608.30724).
  - Memorizing eval rows; the behavior vanished once a held-out set was announced (arXiv:2607.18064).
  - Fabrications during search (arXiv:2606.25198).
  - Algorithmic mode collapse, where in-loop gains diverge from held-out gains (arXiv:2609.00077).
  - Cheating that spreads through shared memory (arXiv:2609.04170).
  - Implementation, not ideation, is the bottleneck (arXiv:2506.01372).

**What we do**
- Its own git repo, pinned env, seeds, per-run provenance, tests, overfit-a-batch.
- Reproduce the baseline before comparing.
- Pilot-first with go/no-go; 30-minute and budget stops; log every run.
- "Never tune on test set", "suspect too-good results".

**Gap**
- The integrity rules are instructions only. The literature shows agents violate such instructions at high rates (arXiv:2608.30724).
- No fidelity audit of what actually ran against the plan.
- No structured failure memory beyond free-text log lines.

**Recommendations**
- **P0 (M), sealed evaluation (Summary #1):**
  - `research-engineer.md` keeps the test split outside `code/` or behind a script it cannot edit. Evaluation runs through a fixed `eval` entry point whose hash is logged.
  - The agent is told the held-out set exists (arXiv:2607.18064).
  - In `.claude/settings.json`, add `deny` rules for `Edit`/`Write` on `projects/*/code/eval/**` and `projects/*/data/test/**`. **[S]** This follows from the reward-hacking evidence; it has not been tested on this pipeline.
- **P0 (S–M), fidelity audit (Summary #2):** after each run, `research-engineer` fills a **run card** in `log.md` with planned vs actual dataset size, steps/epochs, components, baselines and metric definition. Any mismatch is a logged deviation. `/implement` step 3 surfaces mismatches to the PI before interpretation (arXiv:2608.26753).
- **P2 (S):** add `experiments/failures.md` with typed entries `{symptom, root cause, fix, applies-to}`. The engineer reads it before each run (arXiv:2608.10424, arXiv:2606.21024, arXiv:2609.10922).
- **P2 (M, optional):** for optimization-style sub-tasks (hyperparameters, architecture tweaks), allow a small **bounded search** over branches, with each branch logged and all branches reported. **[S]** This is mainly useful when a task has a cheap, trustworthy metric; most of our projects are hypothesis-driven, so broad tree search is not a priority.

### 2.7 Paper writing (`/draft-paper`, `paper-writer`)

**What the best systems do [E]**
- Multi-agent writers (PaperOrchestra arXiv:2604.05018).
- Hallucination-focused evaluation of AI-written papers (arXiv:2604.01128).
- Chain-of-Evidence checks method-code alignment (20–80% across baselines) and score verification (arXiv:2605.26340).
- Deterministic integrity gates for manuscripts: halt-on-failure, cheapest sufficient check (arXiv:2606.09500).
- Human approval gates with claim classification (arXiv:2608.28596).
- The AI Scientist-v2's accepted paper still had citation errors (Sakana blog).

**What we do**
- Claims → evidence outline with PI sign-off; bib only via `lit.py bib`; `lit.py verify`.
- Numbers only from `results/`, with LaTeX comments naming scripts.
- A mandatory limitations section; hedge to the evidence.

**Gap**
- Number fidelity is checked by the model rereading its own output.
- Method-code alignment is never checked.

**Recommendations**
- **P0 (M), numbers by construction (Summary #3):**
  - `analysis/` scripts write `paper/generated/*.tex` (tables and `\newcommand` macros for every reported number).
  - `paper-writer.md` must `\input` them and never type result numbers.
  - A small checker (new subcommand, e.g. `lit.py numbers <paper_dir>`) flags any numeric literal in `experiments.tex` or `abstract.tex` that is not a macro.
- **P1 (S):** in `reviewer.md` step 2, add a **method-code alignment** check. For each method component described in `method.tex`, locate the implementing code path, or flag it (arXiv:2605.26340).

### 2.8 Automated reviewing (`/peer-review`, `reviewer`)

**What the best systems do, and the known failures [E]**
- **Manuscript-only review overrates.** Artifact-aware review drops scores sharply (arXiv:2605.19156). The AI Scientist's "near-human" reviewer claim is self-reported (arXiv:2408.06292).
- **LLM reviewers:**
  - Under-produce weaknesses and barely adjust to paper quality (doi:10.48550/arxiv.2509.19326).
  - Overrate weak papers and are vulnerable to hidden prompt injection (arXiv:2605.25415, arXiv:2606.12716, doi:10.48550/arxiv.2412.01708).
  - Show hivemind agreement and are gameable by stylistic rewriting (arXiv:2605.03202).
  - Flag integrity problems yet still give accept-level scores (concern-acceptance conflict) (doi:10.48550/arxiv.2510.18003).
  - Detect only 39.1% of claim-invalidating errors at k=10 (doi:10.48550/arxiv.2511.21843).
  - Show affiliation bias (doi:10.48550/arxiv.2509.13400).
- **Mitigations proposed:**
  - Structured error detection (arXiv:2601.19916).
  - Cross-vendor audit with a human-written rulebook stored in git. The shared-blind-spot premise is labelled a conjecture by its own authors (arXiv:2608.28631).
  - Multi-model consensus for high-stakes calls (arXiv:2603.22376).
- **Venue experience:** an LLM checklist assistant helped 70% of authors but could be gamed (doi:10.48550/arxiv.2411.03417).

**What we do**
- Three parallel reviewer personas plus a meta-review written by the main agent.
- The reviewer opens `experiments/results/`, checks numbers, searches independently for missed work and runs `lit.py verify`.
- Scores 1–10.

**Gap**
- All reviewers are the same model family as the writer (`opus`).
- There is no explicit error-hunt protocol and no consistency check between concerns and score.
- The simulated score may be read as evidence of acceptability.

**Recommendations**
- **P1 (S), in `reviewer.md`:**
  - (a) Add an **error-hunt checklist** before scoring: claim-invalidating errors, cross-section inconsistencies, results that don't match artifacts, missing baselines (doi:10.48550/arxiv.2511.21843, arXiv:2601.19916).
  - (b) Enforce the rule "any unresolved **major** integrity or soundness concern caps overall ≤ 4" (doi:10.48550/arxiv.2510.18003).
  - (c) State that scores are a prioritization aid, not a prediction of acceptance (arXiv:2605.19156, arXiv:2605.03202).
- **P1 (S), in `peer-review/SKILL.md`:**
  - Give personas **disjoint required focuses** (e.g. one reviewer *must* rerun one table from code) to counter hivemind agreement.
  - If another model family is available through a tool or MCP, use it for one persona. **[S]:** the benefit is plausible but unproven (arXiv:2608.28631).
- **P2 (S):** when reviewing *external* PDFs, strip or flag hidden text before review (arXiv:2605.25415).

### 2.9 Human-in-the-loop design (checkpoints 1–5)

**What the best systems do [E]**
- Human feedback at each stage improves quality (Agent Laboratory, arXiv:2501.04227).
- Industry deployments put HITL checkpoints at stage boundaries (arXiv:2609.08248) and bound autonomy to decision points (arXiv:2608.11241).
- Human-gated verification caught an evaluation defect (arXiv:2609.21257).
- Human effort shifts from ideating to *verifying* (doi:10.48550/arxiv.2601.12152).
- Oversight tooling for large AI-scientist output exists (arXiv:2608.28637).
- A taste oracle holding the PI's preferences changes *direction*, not score (arXiv:2608.07542).
- Models fail ~1/3 of integrity-critical decisions under explicit pressure (arXiv:2608.12345).

**What we do**
- Five mandatory checkpoints: scope, idea choice, cost, supported/refuted, external release.
- The decisions log in `STATE.md`.

**Gap**
- Checkpoints and integrity checks are enforced only by prompt.
- There is no guidance for when the *PI* pushes for a result. **[S]:** IntegrityBench suggests pressure matters.

**Recommendations**
- **P1 (M), in `.claude/settings.json` hooks (Summary #8):**
  - A `Stop`/`SubagentStop` hook runs `lit.py verify --offline` and the numbers check when `paper/` changed.
  - A `PreToolUse` guard blocks edits to pre-registered `hypotheses/*.md` unless the edit appends to "Deviations log".
- **P2 (S), in `CLAUDE.md` Integrity rules:** add "If asked (by anyone, including the PI) to drop runs, change metrics post hoc, or reword a null result as positive, refuse, record the request in `STATE.md`, and propose the honest alternative" (arXiv:2608.12345).
- **P2 (S), in `STATE.md` template:** add a short "PI research taste" section (preferred directions, disliked patterns) that ideation reads (arXiv:2608.07542; **[S]** a small effect is expected).

### 2.10 `/radar` and literature freshness
**Keep.** No surveyed end-to-end system does continuous scoop monitoring tied to the chosen idea **[S, from the records reviewed]**.

---

## 3. Failure modes from the literature vs our guardrails

| Failure mode | Evidence | Our guardrail | Addressed? | Fix |
|---|---|---|---|---|
| Fabricated or nonexistent citations | doi:10.2196/53164 (29–91% hallucinated refs); doi:10.48550/arxiv.2601.17431 (17% phantom); arXiv:2605.26340 (up to 21%); Sakana blog | `lit.py bib` only; `lit.py verify` | **Mostly**: existence is checked | — |
| Real but *wrong* paper cited / metadata drift | arXiv:2605.27700; arXiv:2607.18360; doi:10.48550/arxiv.2601.17431 (valid titles with hallucinated identifiers) | none; `verify` only resolves the DOI | **No** | #4 title/id match |
| Citation doesn't support the claim | arXiv:2605.06635; arXiv:2608.24306; web snippet on OpenAI DR (>50% subtle inaccuracies, *unverified*) | "cite papers.jsonl id"; 3-claim spot check | **Partly** | §2.1 citation pass; #4 sampled claim check |
| Fabricated or unreproducible results | arXiv:2605.19156; arXiv:2606.25198; arXiv:2605.26340 | "numbers only from results/"; manual cross-check | **Partly** (instruction only) | #3 numbers by construction |
| Methodological hallucination (silent downscaling, oracle swaps) | arXiv:2608.26753 | none | **No** | #2 fidelity audit |
| Reward hacking / specification gaming | arXiv:2608.30724; arXiv:2607.18064; arXiv:2605.02964; arXiv:2609.04170 | "never tune on test set" | **Weak**: agents hack even when told not to | #1 sealed eval + deny rules |
| Data leakage, metric misuse, benchmark cherry-picking | arXiv:2509.08713 | template asks for leakage risks and metric validity | **Partly** | §2.5 sealed split + benchmark justification |
| Post-hoc selection / p-hacking | arXiv:2509.08713; arXiv:2608.05179 (38% disclose seeds or traces) | pre-registration; deviations log; report nulls | **Mostly**: all-runs disclosure is not required | §2.5 all-runs field + hash |
| Overclaiming in the paper | arXiv:2605.19156; arXiv:2506.01372 | claims→evidence outline; "hedge to evidence"; reviewer claims-vs-evidence | **Mostly** | #7 artifact-aware reviewer checklist |
| Overrated novelty (novelty mirage) | arXiv:2606.12071; arXiv:2603.15164; arXiv:2502.14297 | ≥3 searches + closest work | **Partly** | #5, #6 |
| LLM self-evaluation / judge unreliability | doi:10.48550/arxiv.2409.04109; arXiv:2608.17270 | reviewer as critic, but ideator self-scores | **Partly** | #5 pairwise by a separate agent |
| Ideation-execution gap | arXiv:2506.20803; doi:10.48550/arxiv.2509.21043 | pilot-first after selection | **Partly** | #5 feasibility probe before selection |
| Low idea diversity / mode collapse | doi:10.48550/arxiv.2409.04109; arXiv:2607.01233; arXiv:2609.00077; arXiv:2606.25198 | 10 ideation strategies | **Partly** | §2.3 grid + duplicate report |
| Automated reviewer failures (lenient, gameable, injection, hivemind) | arXiv:2605.03202; arXiv:2605.25415; doi:10.48550/arxiv.2510.18003; doi:10.48550/arxiv.2509.19326 | 3 personas; artifact checks; human decides | **Partly** | #7 |
| Same-family author/reviewer blind spots | arXiv:2608.28631 (conjecture) | none | **No** (speculative risk) | #7 optional cross-family reviewer |
| Multi-agent hand-off loss / corruption | arXiv:2609.17464; arXiv:2608.24306 | "pass file paths to subagents" | **Partly** | §2.1 merge rule |
| Lack of a metacognitive check-and-revise loop | arXiv:2608.14905 | reviewer passes at stages 2–4, 7 | **Partly** | #2, #8 make the checks mandatory |
| Integrity under social pressure | arXiv:2608.12345 | none explicit | **No** | §2.9 rule |
| Evaluator defects misread as findings | arXiv:2609.21257 | "suspect a bug if too good"; baseline reproduction | **Partly**: only "too good", not "too bad" | Add "suspect the evaluator on any large unexpected change" to `research-engineer.md` (P2, S) |
| Wasted compute on repeated bugs | arXiv:2608.10424 | lab log | **Partly** | §2.6 `failures.md` |

---

## 4. What we do that the literature supports (keep)

- **Human checkpoints at stage boundaries, with the PI choosing direction.** Agent Laboratory reports that human feedback improves quality (arXiv:2501.04227). Industrial deployments converge on the same design: arXiv:2609.08248, arXiv:2608.11241, arXiv:2609.21257. **[E]**
- **Pre-registration, a deviations log, a prediction → conclusion table and reporting of nulls.** This matches immutable experiment cards (arXiv:2608.07542) and auditable hypothesis protocols (arXiv:2607.09195, arXiv:2607.05682). It directly targets post-hoc selection (arXiv:2509.08713). **[E]**
- **Real BibTeX from DOIs plus `verify`.** It removes the most common failure outright (doi:10.2196/53164, doi:10.48550/arxiv.2601.17431). This pipeline is stronger than most surveyed systems, which do not verify references at all (arXiv:2605.26340, arXiv:2608.05179). **[E]**
- **Artifact-aware reviewer that opens `results/`.** This is the review mode that separates real from apparent quality (arXiv:2605.19156). **[E]**
- **Pilot-first with go/no-go and budget stops.** Consistent with budget-aware execution (arXiv:2602.02660, arXiv:2609.17846) and with implementation being the bottleneck (arXiv:2506.01372). **[E]**
- **Baseline reproduction before comparison, and "suspect a bug when results look too good".** Consistent with arXiv:2609.21257 and arXiv:2608.26753. **[E]**
- **Multi-source retrieval** (semantic index + fresh arXiv + citation data + web). Retrieval augmentation improved future-impact scores of ideas by 2.5× where LLM judges saw no difference (arXiv:2603.15164). **[E]**
- **Agents split by role with a separate critic.** This matches the co-scientist, Agent Laboratory and AutoResearch designs. The main change needed is to stop letting generators score themselves (§2.3). **[E/S]**
- **Keep `/radar` scoop alerts** (§2.10). **[S]**
- **No autonomous submission (checkpoint 5).** Given the reviewer-gaming and fabrication evidence (doi:10.48550/arxiv.2510.18003), fully automated publication loops are unsafe. **[E]**

---

## 5. What not to copy (yet)

- **Large-scale tree search or evolutionary loops over whole research projects.** Evidence is mixed: no universally superior harness (arXiv:2607.18235), evolution ≈ independent sampling in one domain (arXiv:2607.04108), and novel ideas are rare under all strategies (arXiv:2606.25198). The gains come mostly on tasks with cheap, trustworthy metrics (MLE-bench, AlphaEvolve). **[S]** For a PI-driven paper pipeline, the cost and reward-hacking risk outweigh the benefit, except inside `/implement` for bounded optimization sub-tasks.
- **Automated acceptance scores as a quality target.** Optimizing against an LLM reviewer is gameable (arXiv:2605.03202, doi:10.48550/arxiv.2510.18003).
- **Fully autonomous no-HITL orchestration** (e.g. cmbagent's design, doi:10.48550/arxiv.2507.07257). It conflicts with our checkpoints, and no comparison against a human-gated design was found.

---

## 6. Tool and process problems found during this review

1. **`lit.py arxiv` fails on boolean queries.** `"A" OR "B"` returns HTTP 400 from export.arxiv.org. The query builder turns every token into `all:<tok>` joined by AND, so `OR` becomes a search term. Fix (P2, S): pass `OR`/`AND`/`ANDNOT` through as operators in `cmd_arxiv`.
2. **`lit.py arxiv` sorts by date, then `--since` filters.** Broad queries (e.g. `"AI scientist"`) return the newest 25 items across all topics, some off-topic (catalysts, GUI agents). Relevance needs quoted phrases. **[S]** Consider an optional `--sort relevance`.
3. **`lit.py openalex` relevance is poor for these topics.** Queries like "automated peer review LLM reliability" returned mostly generic highly cited papers (AlphaFold, PRISMA). OpenAlex was useful only for known titles and venue versions (e.g. the Nature version of Co-Scientist).
4. **SciSpace capture gap.** `CLAUDE.md` now says to "save the raw JSON response to a file, then `lit.py scispace`". An agent cannot pipe MCP output to a file. It must re-type the response with `Write`, which is a **transcription and fabrication risk**, the very failure the pipeline guards against. For this review I rebuilt 42 SciSpace hits into the response shape by hand. `tldr` holds my condensed notes, not SciSpace's TLDR, and each such record has a `note` field saying so. URLs point to doi.org, not the SciSpace slug. Suggested fix (P1, S): allow storing SciSpace hits by DOI only, then re-fetch metadata and abstract through `lit.py` (OpenAlex/arXiv by DOI). The MCP response would never be re-typed.
5. **Semantic Scholar was not used** (no `S2_API_KEY`; the review did not need forward snowballing), so forward-citation coverage of the anchor papers is incomplete.
6. **Concurrent edits:** `tools/lit.py` and `CLAUDE.md` changed on disk during this review (SciSpace converter/importer added). The findings refer to the new versions. No pipeline files were modified by this review.

## 7. Limitations of this review

- Almost everything is per abstract. Most 2026 items are unreviewed arXiv preprints, often self-evaluated.
- "Industry" evidence is mostly from papers by the deploying teams (A-MLE, Auto-RecSys, EvoPilot, RecSys Factory), not independent audits.
- The survey window is biased toward ML/CS-focused autoresearch. Wet-lab systems are only touched on (Kosmos, Co-Scientist, Boiko et al. doi:10.48550/arxiv.2304.05332).
- No recommendation here has been tested on this pipeline. The effort estimates are guesses: S < 1 h, M ≈ half a day, L = 1–3 days.

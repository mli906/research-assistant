# LongMemEval: benchmarking chat assistants on long-term interactive memory (arXiv:2410.10813)
Read: abstract (and secondary use in MemoryAgentBench and vendor reports). Tags: evaluation, core.

- **Design.** 500 curated questions embedded in freely scalable chat histories (variants S ≈115K tokens, M ≈1.5M; per paper). Five abilities: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, abstention.
- **Results (per abstract).** Commercial assistants and long-context LLMs drop ~30% accuracy over sustained interactions. Proposes an index–retrieve–read design space (session decomposition, fact-augmented keys, time-aware query expansion).
- **Relevance.** De facto standard alongside LoCoMo (arXiv:2402.17753). Vendors now report 90%+ (e.g., Hindsight arXiv:2512.12818 reports 91.4%), so it is nearing saturation. The successor LongMemEval-V2 (arXiv:2605.12493) exists. It has no privacy, deletion or access-control dimension; "abstention" is the only governance-adjacent ability.

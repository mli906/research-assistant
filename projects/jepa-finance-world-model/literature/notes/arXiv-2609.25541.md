# arXiv:2609.25541 A JEPA Recipe for Tabular Foundation Models
Read: abstract page only (HTML full text 404 at access time 2026-10-01; PDF fetch not parseable). Treat details as "per abstract".
- **Setting:** tabular foundation model with a JEPA latent term added to value-prediction training.
- **Reported (per abstract):** the latent term collapsed in earlier runs, taking the encoder to a constant map. Fix = (1) value head reads the encoder field rather than predictor output; (2) EMA-difference target; (3) both arms trained to a plateau rule instead of a fixed budget.
- **Result (per abstract):** across 147 real tabular datasets the JEPA arm trails the value-only arm: classification 32 wins / 70 losses (29:63 after name-normalisation), regression 8 wins / 24 losses; margin small on classification, wider on regression. Costs 1.42x steps and 1.66x wall-clock to plateau.
- **Critique:** honest negative result and directly on-topic for a tabular/time-series first modality. Cannot judge dataset sizes, seeds, or whether SIGReg-type regularisation instead of EMA would change the picture. Must read full text (TODO when HTML/PDF available).

## Update 2026-10-01 (gap analysis): FULL TEXT read (arXiv PDF via pypdf, 16 pp.; Jeon, Cho, Suh, Modulabs)
- Setting: a TabPFN-style prior-fitted model trained on synthetic tables; iid tables, no temporal structure. **One run per arm.**
- Verbatim: "The recipe does not beat the value-only arm at convergence, and we do not claim that it does." "the latent term ... collapsed in our earlier runs and took the encoder with it to a constant map."
- Stated limitation: "The suite likewise scores every dataset at one context and feature budget, so behaviour at other budgets is not measured."
- **Stated future work (verbatim):** "whether the latent term buys robustness rather than accuracy, at short contexts or under noise, is testable on the same checkpoints ... since a latent target may discard what a value target must reproduce, and noise is where such a difference wo[uld show]". This supports testing JEPA under heavy, structured missingness and low SNR rather than on clean accuracy.

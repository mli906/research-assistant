# arXiv:2609.25541 A JEPA Recipe for Tabular Foundation Models
Read: abstract page only (HTML full text 404 at access time 2026-10-01; PDF fetch not parseable). Treat details as "per abstract".
- **Setting:** tabular foundation model with a JEPA latent term added to value-prediction training.
- **Reported (per abstract):** the latent term collapsed in earlier runs, taking the encoder to a constant map. Fix = (1) value head reads the encoder field rather than predictor output; (2) EMA-difference target; (3) both arms trained to a plateau rule instead of a fixed budget.
- **Result (per abstract):** across 147 real tabular datasets the JEPA arm trails the value-only arm: classification 32 wins / 70 losses (29:63 after name-normalisation), regression 8 wins / 24 losses; margin small on classification, wider on regression. Costs 1.42x steps and 1.66x wall-clock to plateau.
- **Critique:** honest negative result and directly on-topic for a tabular/time-series first modality. Cannot judge dataset sizes, seeds, or whether SIGReg-type regularisation instead of EMA would change the picture. Must read full text (TODO when HTML/PDF available).

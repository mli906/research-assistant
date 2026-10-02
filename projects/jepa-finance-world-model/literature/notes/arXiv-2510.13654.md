# Rethinking evaluation in the era of TSFMs: (un)knowns (arXiv:2510.13654; first posted as "Time Series Foundation Models: Benchmarking Challenges and Requirements")
Meyer, Mueller, Oct 2025. Read: arXiv HTML via summarising fetch tool (2026-10-01).
- **Direct leakage:** across 22 TSFMs only 6% of 401 datasets were never used in any model's pretraining or fine-tuning ("one model's pretraining corpus is another's test set"); cited cases of >50% better scores from undetected contamination.
- **Indirect (temporal-overlap) leakage:** correlated series sharing a period let a model exploit common drivers; examples: model trained on DAX through the 2020 crash gained ~37% on S&P 500 over the same period; Madrid transport 43% gain from temporal overlap alone.
- **Requirements proposed:** genuinely novel test sets; a strict global post-training test period after all training cutoffs of all compared models.
- **Limits:** effect sizes documented only in isolated cases; magnitude in real TSFM settings "largely unknown".
- **Use for us:** for any finance-pretrained model, the test window must start after every pretraining series ends, including *other assets/countries* over the same dates (a cross-sectional/global-factor leak that per-series purging misses). Confidence: medium.

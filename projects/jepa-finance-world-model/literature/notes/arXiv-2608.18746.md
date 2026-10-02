# Decision-metric alignment in latent world models (arXiv:2608.18746)
Read: arXiv HTML via summarising fetch tool (2026-10-01).
- **Core claim:** decodability of task variables from the latent (information sufficiency, linear-probe R^2) does NOT imply that Euclidean latent goal-distance ranks action sequences by true task progress (decision-metric alignment).
- **Diagnostics:** Plan-Real Spearman (rank correlation of latent cost vs real cost over random candidate plans) and CEM-stage Spearman (same at iteration 0 / 15 / elite).
- **Setup:** LeWM (ViT-Tiny) on PushT, Reacher, Cube (OGBench), TwoRoom. Variants incl. DA-LeWM with inverse-dynamics and goal-action heads.
- **Numbers:** PushT after 1 epoch: LeWM 49.3% online success, Plan-Real Spearman +0.280; DA-LeWM 92.7%, +0.412. After 10 epochs DA-LeWM: PushT 98.7%, Reacher 87.3%, Cube 80.7%, TwoRoom 96.0%. Linear-probe R^2 changed <=0.03 across non-collapsed variants despite large success gaps.
- **Limits (authors):** four short-horizon simulated tasks, one run per config, ViT-Tiny, Euclidean costs, CEM; Spearman loses power under ties; alpha=0.1 fixed.
- **Use for us:** direct warning that probing a finance latent for "recession state" or "leverage" is necessary but not sufficient; the evaluation must also rank interventions/scenarios by realised outcomes (e.g. rank candidate scenario paths by realised loss). Confidence: medium.

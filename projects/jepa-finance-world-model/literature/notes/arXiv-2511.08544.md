# arXiv:2511.08544 LeJEPA (SIGReg)
Read: HTML extraction (2026-10-01).
- **Claim/theory:** isotropic Gaussian is the optimal embedding distribution for minimising worst-case downstream (k-NN, kernel) risk (Thm 1). SIGReg = sketched Epps-Pulley characteristic-function test along M random 1-D slices (recommended M=1024, 17 quadrature points on [-5,5]); linear time/memory; lambda about 0.05; no stop-gradient, no EMA/teacher, no schedules.
- **Evidence:** ~50 models in 8 architecture families stable (91.5-95% on ImageNet-10 linear probe); ViT-H/14 79% ImageNet-1K linear. In-domain small-data: Galaxy10 LeJEPA ConvNeXt-V2 Nano 82.72% full / 29.42% 1-shot vs DINOv2 ViT-S transfer 78.34% / 21.05%.
- **Limits:** assumptions of smooth densities; O(1/N) minibatch bias; lambda/view-count tuning. Vision only.
- **Relevance:** regulariser used by HEPA, Phys-JEPA and 2609.31680; makes JEPA training cheap on small data. Whether an isotropic-Gaussian target is sensible for heavy-tailed, non-stationary financial embeddings is untested (speculation).

---
title: "Can neurons speak? Semantic narration of vision at single-cell resolution (NEURRATOR)"
authors: Marin-Llobet, Hakim, Matias, Murthy, Li, Ba
year: 2026
venue: arXiv (preprint)
url: https://arxiv.org/abs/2606.18667
subfield: ai-neural-modeling
tags: [single-cell-decoding, neural-captioning, CLIP, LLaVA, cell-type-probe, Neuropixels, mouse, visual-cortex, SAE]
---

## 解决了什么问题
高级视觉皮层里单个神经元编码什么，一直难以参数化；近年改用深度网络嵌入当替代，但那是黑箱，研究者还得人工把高维激活翻成语义假设。能否把单神经元活动**直接读成自然语言**、并细到单神经元 / 单细胞类型的分辨率，此前是空白——已有电生理解码要么重建低层刺激特征、要么停在不透明的嵌入坐标里。

## 核心方法
NEURRATOR：一个 12.8M 参数的编码器（多尺度 Conv1D 前端 + transformer + 注意力加权池化 + 576 个可学习 patch query 跨注意力）把**任意子集神经元的动作电位**映射到冻结 CLIP ViT-L/14 的 576×1024 patch 嵌入；再用一个 forward hook（PatchInjector）替换冻结 LLaVA-1.5-7B 的视觉塔输出，由其 LLaMA-2-7B 解码器生成一句对所见场景的旁白。**语言侧零训练**（CLIP 只在训练时给监督目标，测试时不输入图像）。损失 = 0.5·MSE + 0.5·(1−cos)。编码器对输入子集通用（集合式池化 + 20% dropout），所以**推理时可把输入限制到单神经元、某脑区或某分子定义细胞类型**，用同一个训练好的模型查询。数据：小鼠，公开 Allen Brain Observatory Visual Coding–Neuropixels（侵入式皮层内、记录单神经元动作电位）16 个 session，被动观看自然电影，属再分析。

## 关键数据
- **held-out 帧语义连贯**：解码旁白与参考 caption 的 SBERT 相似度 0.367 ± 0.180，对随机句子地板 0.020（p<0.001）；front-only 外推 0.170 vs 0.062。
- **泛化到没见过的图像**：18 张留出的 Natural Scenes，tiger 帧解为 “a tiger walking through the grass”（+0.68）。
- **scaling law**：旁白质量随神经元数（log 轴）单调上升；V1 最高效，约 30 个神经元越过随机 caption 基线（≈0.27），高级视觉区 / LGd 在 50–100，峰值 ~0.45 未饱和；海马（非视觉对照）始终压在基线附近 —— 排除“语言模型不看输入也能瞎编”。
- **细胞类型分歧**：按解剖区 pooling 全塌成一簇（两两 0.69–0.79）；按细胞类型 pooling 分开（PV–SST 0.58，VIP 0.34/0.41）。同一帧 PV/SST 讲“车/停车场”、VIP 讲“暗房间/光影”。仅凭旁白文本的分类器 76% 认出来源细胞类型（随机 33%，p<10⁻⁴）。
- **SAE 概念分解**：PV → 小而圆物体、SST → 车辆、VIP → 场景光照氛围；bootstrap 重采样 200 次稳定。

## 为什么是 milestone
整条「神经→图像/语言重建」线此前清一色是**人类 fMRI、体素/群体级**（每个体素平均 10⁴–10⁶ 神经元）——见 [[miyawaki-2008-visual-image-reconstruction]]、[[horikawa-2017-generic-decoding-dnn-features]]、[[takagi-2023-stable-diffusion-reconstruction]]、[[ferrante-2023-brain-captioning]]、[[tang-2023-semantic-language-reconstruction]]。NEURRATOR 首次把“把神经活动旁白成自由文本”推到**单神经元分辨率**（细 ~3 个数量级），并把**细胞类型从分类目标变成可用自然语言查询的功能探针**。延续 [[horikawa-2017-generic-decoding-dnn-features]] 的“神经→预训练网络特征空间”思路、[[defossez-2023-meta-meg-speech]] 的对比对齐。局限（作者自列）：单物种 / 仅视觉皮层、细胞类型分析靠跨小鼠拼的 pseudo-mouse（未验证单只动物内成立）、概念验证为相关性、旁白天花板受限于 CLIP（读不出 CLIP 表示不了的东西——作者视“联合训练瓶颈以发现 CLIP 之外的概念”为最有前景的下一步）。

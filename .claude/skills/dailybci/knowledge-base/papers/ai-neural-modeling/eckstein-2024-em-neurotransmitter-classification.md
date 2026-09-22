---
title: "Neurotransmitter classification from electron microscopy images at synaptic sites in Drosophila melanogaster"
authors: Eckstein N, Bates AS, Champion A, et al. (末位作者 Funke J)
year: 2024
venue: Cell 187:2574-2594
url: https://doi.org/10.1016/j.cell.2024.03.016
subfield: ai-neural-modeling
tags: [connectome, Drosophila, neurotransmitter, electron-microscopy, 3D-CNN, synaptic-sign, FlyWire, hemibrain]
---

## 解决了什么问题

电镜连接组给出连接，却不给连接的正负号（由递质隐含）。果蝇中枢约 7,000 个细胞类型里只有约 700 个的递质已知，逐个用免疫组化/RNA 检测无法扩展到全脑。

## 核心方法

- **标签**：从 21 项研究汇编 356 个递质证据可靠的细胞类型（免疫组化为主、RNA 表达为辅，借 GAL4/split-GAL4 定位），在 FAFB 与 hemibrain 电镜数据中找到对应神经元（FAFB 3,025 个重建/211,564 个突触；hemibrain 5,902 个/840,535 个）；一般不纳入报道有共释放的类型。
- **模型**：3D VGG 式卷积网络，输入为以突触前位点为中心、边长 640 nm 的电镜图像块，输出六类递质（乙酰胆碱、谷氨酸、GABA、血清素、多巴胺、章胺）之一。按整个神经元划分训练/验证/测试集（约 70/10/20）。
- **汇总**：对一个神经元（>30 个突触前位点）的逐突触预测投票取多数。

## 关键数据

- 摘要：单突触准确率 **87%**，神经元 **94%**，已知细胞类型 **91%**（FAFB 全脑）；hemibrain 单突触 78%、神经元 91%。
- 血清素最不可靠（FAFB-FlyWire 33%，hemibrain 38%），源于训练标签少。视叶虽基本未用作训练，约 29,000 个胆碱能神经元 96% 判对。
- 可解释性分析找到超微结构差异并经盲法人工分割证实：乙酰胆碱突触间隙更亮，谷氨酸囊泡大于 GABA，谷氨酸 T-bar 暗于乙酰胆碱。
- 发育上同一 hemilineage 基本只表达一种快速递质（作者类比 Dale 原则称 Lacin's law）。

## 为什么是 milestone

为全脑连接组提供了可用的递质/正负号层，Shiu 2024 等全脑模型直接以它定符号。边界要记清：它预测的是**递质**，不是作用方向；兴奋还是抑制由突触后受体决定（果蝇谷氨酸可兴奋可抑制），把递质映射成正负号是下游模型另加的规则。

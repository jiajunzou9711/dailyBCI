---
title: "Network structure of cerebral cortex shapes functional connectivity on multiple time scales"
authors: Honey, Kötter, Breakspear, Sporns
year: 2007
venue: PNAS 104:10240–10245
url: https://doi.org/10.1073/pnas.0701519104
subfield: brain-encoding-models
tags: [whole-brain-model, connectome, functional-connectivity, macaque, time-scales]
---

## 解决了什么问题
静息态功能连接（不同脑区活动的相关结构）被反复观察到，但它与底层解剖连接的关系不清楚：功能连接到底是解剖连接的直接反映，还是另有来源。这个问题无法只靠观测回答，需要一个能生成活动的模型。

## 核心方法
以猕猴新皮层的解剖连接矩阵为骨架，在每个节点上放非线性群体动力学，仿真出活动时间序列，再用信息论方法从仿真活动中提取功能网络，并在**不同时间窗长度**下分别考察。这样可以直接问：解剖结构如何在不同时间尺度上塑造功能连接。

## 关键数据
- 猕猴解剖连接数据 + 仿真。
- **分钟量级**长窗：恢复出的功能网络与底层结构网络高度重合，功能枢纽与结构枢纽对应。
- **秒量级**：功能拓扑出现明显变化，瞬时耦合呈现两个反相关的簇，经由前额与顶叶枢纽相连。
- **百毫秒量级**：出现锁相事件，其统计规律受解剖约束，并由此生成较慢尺度上观察到的功能连接模式。

## 为什么是 milestone
第一次用生成模型说清"结构决定功能"这句话在**不同时间尺度上含义不同**：长时间平均看结构主导，短时间看则有大量结构无法解释的动态。这为静息态功能连接的解释设了边界，也是此后全脑模型的标准检验任务（能否从结构连接再现实测功能连接）。

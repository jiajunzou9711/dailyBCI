---
title: "A task-optimized neural network replicates human auditory behavior, predicts brain responses, and reveals a cortical processing hierarchy"
authors: Kell, Yamins, Shook, Norman-Haignere, McDermott
year: 2018
venue: Neuron
url: https://doi.org/10.1016/j.neuron.2018.03.044
subfield: brain-encoding-models
tags: [task-optimized-network, auditory-cortex, fMRI, encoding-model, spectrotemporal-filters, processing-hierarchy]
---

## 解决了什么问题
听觉神经科学长期用**人手设计的特征**（谱时滤波器、音位范畴）解释皮层对自然声音的反应。本文检验另一条路：让网络只为完成生态上真实的任务而训练，看它自己长出的表征能否解释皮层。

## 核心方法
训练层级神经网络完成**语音识别与音乐识别**两个任务（输入声波，输出词或音乐类型）。**训练中不出现音素、不使用任何手工中间表征。** 再用编码模型把网络内部层激活线性映射到 fMRI 体素反应，与传统谱时滤波器模型做**受控对照**：预测目标、回归框架、评估方式全部相同，唯一变动的是特征来源。

## 关键数据
- 网络在两个任务上**达到人的水平**，且**犯与人相似的错误**，尽管未为此优化。
- 表现最好的网络出现**早期共享处理、其后分成语音与音乐两条通路**的结构。
- **网络特征预测 fMRI 体素反应在整个听觉皮层都明显优于传统谱时滤波器模型。**
- **层级对应**：初级听皮层由网络**中间层**最佳预测，非初级由**晚层**最佳预测。

## 为什么是 milestone
它给出了两个此后被反复重演的模板：**①「换一组特征，其他不变」的受控对照**；**②「顺序对不对得上」的层级对应**。第二条比第一条更有分量——事前四种结果（同一层最优 / 顺序相反 / 无规律 / 顺序一致）中只有一种符合对应假设，且皮层先后由解剖连接与反应潜伏期独立确定。**强度边界**：结论是「解释皮层反应**不必**先假定手工设计的层级」，未证明这些层级不存在；支持的是表征阶段排序一致，不支持机制相似。视觉侧的对应工作是 [[yamins-2014-performance-optimized-models]]；把这两个模板抬到音素与词性一级的是 [[nastase-2026-language-population-code]] 引用的 Goldstein 2025。

---
title: "Natural Language Processing with Dynamic Classification Improves P300 Speller Accuracy and Bit Rate"
authors: Speier W, Arnold C, Lu J, Taira RK, Pouratian N
year: 2012
venue: Journal of Neural Engineering
url: https://doi.org/10.1088/1741-2560/9/1/016004
subfield: non-invasive
tags: [P300-speller, language-model, HMM, error-correction, dynamic-stopping]
---

## 解决了什么问题
P300 speller需要多次重复刺激才能获得可靠的字符分类，重复次数与准确率、拼写速度之间存在直接权衡；此前系统多把EEG分类和语言层面的合理性判断分开处理，未充分利用"英文文本本身高度可预测"这一先验信息去弥补EEG分类的不确定性。

## 核心方法
把隐马尔可夫模型(HMM)风格的语言模型整合进P300 speller的在线动态分类流程：EEG分类器给出的字符概率分布与语言模型给出的字符转移概率联合决策，并据此动态决定何时已有足够置信度停止当前字符的刺激重复(dynamic stopping)，而非固定重复次数。

## 关键数据
论文报告在健康受试者P300拼写任务中，引入语言模型的动态分类相比传统固定重复次数的静态分类，同时提升了拼写准确率和信息传输率(bit rate)（具体数值见原文）。

## 为什么是 milestone
是"语言模型直接参与P300输出纠错/动态决策"这一路线较早、影响较大的实证工作之一，确立了"EEG分类置信度×语言先验联合决策"的基本范式，是LM辅助BCI拼写这条线的奠基实证。

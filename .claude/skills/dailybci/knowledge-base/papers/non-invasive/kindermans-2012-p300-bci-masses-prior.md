---
title: "A P300 BCI for the Masses: Prior Information Enables Instant Unsupervised Spelling"
authors: Kindermans PJ, Verschore H, Verstraeten D, Schrauwen B
year: 2012
venue: Advances in Neural Information Processing Systems (NIPS) 25
url: https://proceedings.neurips.cc/paper/2012
subfield: non-invasive
tags: [P300-speller, language-model, Bayesian-prior, zero-calibration, unsupervised]
---

## 解决了什么问题
P300 speller在实际使用前通常需要为每位用户单独采集有监督校准数据来训练分类器，这个校准过程耗时且对新用户不友好；如何让系统在完全无监督标注的情况下就能可用，是P300 speller走向"大众化"部署的主要障碍之一。

## 核心方法
用贝叶斯框架把语言模型(字符/词先验)直接作为拼写目标推断的先验信息，与未经监督训练的EEG似然联合更新后验分布，让系统仅凭语言先验的强约束就能在完全无校准、无监督标签的情况下即时纠正/收敛到正确拼写结果。

## 关键数据
论文在健康受试者P300拼写任务上验证：无需任何有监督校准阶段，系统仍能达到可用的拼写准确率(具体数值见原文)，纠错主要依赖语言模型先验而非重新训练分类器。

## 为什么是 milestone
把语言模型的角色从"事后纠错"扩展为"替代监督训练的核心先验来源"，是LM深度介入BCI拼写解码流程(而不仅是文本后处理)的代表性早期工作，与Speier 2012一起构成本子线两条主要路线(动态分类纠错 vs 贝叶斯先验免校准)。

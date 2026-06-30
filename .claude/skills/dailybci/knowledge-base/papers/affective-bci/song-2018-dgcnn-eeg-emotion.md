---
title: "EEG Emotion Recognition Using Dynamical Graph Convolutional Neural Networks"
authors: Song, T., Zheng, W., Song, P., Cui, Z.
year: 2018
venue: IEEE Transactions on Affective Computing 11(3):532-541
url: https://doi.org/10.1109/TAFFC.2018.2817622
subfield: affective-bci
tags: [DGCNN, graph-neural-network, deep-learning, channel-relationship, EEG]
---

## 解决了什么问题
此前 EEG 情绪解码多把各电极特征当作独立向量或固定网格，忽略了电极间(脑区间)的功能连接关系。本文把 EEG 通道布局当作图来建模，让网络学出"哪些电极该联动"。

## 核心方法
**动态图卷积神经网络(DGCNN)**：把 EEG 各通道作为图的节点，用一个**可训练的邻接矩阵**表示通道间关系——邻接矩阵不是预设的，而是随训练动态更新，从而自动发现对情绪判别有用的脑区连接结构。节点特征用微分熵(DE)。

## 关键数据
- 在 SEED、DREAMER 等数据集上相比当时的非图方法取得更优情绪分类准确率(具体见原文 IEEE TAC 11(3):532–541)。
- 学到的邻接矩阵揭示了与情绪相关的通道连接模式，提供一定可解释性。

## 为什么是 milestone
DGCNN 是把**图神经网络**引入 EEG 情绪识别的代表性地标，开启了此后大量基于图/连接结构的 EEG 情绪深度学习工作。它沿用 [[zheng-2015-seed-differential-entropy]] 的 DE 特征与 SEED 基准，把建模重心从"单通道特征"推进到"通道间关系"，与 [[zheng-2016-transfer-learning-affective]] 的跨被试线一起，构成深度学习时代 aBCI 的两条主轴(表示学习 / 域适应)。

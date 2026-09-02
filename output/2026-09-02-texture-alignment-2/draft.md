# 2026-09-02 · DNN–脑对齐由纹理统计驱动（下篇：四组证据 + 闭环 + 边界）

**上篇**：`output/2026-09-01-texture-alignment/`（卡①–⑪，已发）
**张力类型**：② 纠错型（延续上篇；本篇给证据与落点）
**主引论文**：Loke J, Sörensen LKA, Groen IIA, Cappaert N, Scholte HS. (2026). Shared texture-like representations underlie deep neural network alignment with human visual processing. Current Biology 36:1–8. doi:10.1016/j.cub.2026.08.008
**电极模态**：非侵入式 **EEG**，17 个后部电极（Oz、O1…）。人类，52 名被试进入分析。
**本地文件**：`papers/loke-2026-cub.pdf`、`papers/loke-2026-fulltext.txt`、`papers/lk-p{2,3,4,5}-lo.png`、`papers/lk-p2-hi.png`

## 卡序（2026-09-02 定，暂定）
封面 / 目录 / ①前情 / ②纹理条件对齐最高(Fig 2B) / ③纹理特征也能预测原图 EEG(Fig 3A) / ④去掉背景纹理对齐整体下降 / ⑤物体信息可解码(200类, 随机0.5%) / ⑥对齐与物体信息走反向象限(Fig 4) / ⑦对齐峰值落在 100–200 ms / ⑧200 ms 后的天花板缺口(Fig 3B) / ⑨闭环·裂缝一 / ⑩闭环·裂缝二 / ⑪形状偏好为何不冲突 / ⑫引申与强度边界 / ⑬作者自列四条局限 / 尾卡 = 16 张
（2026-09-02 改：原 ⑦ 拆成 ⑦ 时间窗 + ⑧ 天花板缺口，后续顺延）

**论文自己的结果小节顺序（照此走，勿改）**：
1. Texture-synthesized images maximize DNN-EEG alignment
2. Texture-synthesized features generalize to natural images
3. Object information is decodable from EEGs but does not drive alignment with the DNN
4. DNN-brain alignment is dominated by early feedforward processing
（讨论）Shared texture sensitivity, not object processing, drives DNN-brain alignment → Limitations and conclusion

## 已定稿

### 卡① 上一期停在哪个问题上
〔文风说明：本卡经用户指定，采用 khazix-writer skill 的口吻试写（口语化、无冒号/破折号/双引号）。与项目默认的「科学平实」规则有冲突，已向用户说明，用户选择暂用此版。〕

上一期最后停在一个问题上。

DNN 跟人脑视觉皮层能对上，那个对上的分数，到底是脑子里的哪一块在撑着。是局部的图像统计，还是物体本身的信息。

作者的办法挺直接的，把这两样东西拆到不同的图片里去。纹理合成图只留局部统计，用 VGG-19 conv1_1 的 Gram 矩阵去匹配，全局形状全打散；只留物体图反过来，形状留着，背景抠掉。人这边戴 EEG 看这三种图，17 个后部电极，52 个被试。模型这边权重冻住，同一批图跑一遍。两边各自算成一张 200×200 的表，再比。

三种图里，纹理合成那一种对上得最好。

下面四组结果，是这个结论的依据。

*（配图：暂无。备选 `papers/loke-fig1B.png`，但该图已用于上篇卡⑦，重复使用需评估）*

## 讨论中
- [ ] 卡②–⑩ 逐张讨论
- [ ] 文风最终定调：khazix 口吻是只用于卡①，还是全篇统一？（若全篇统一，需重跑落稿自检 grep，多条禁用词规则将失效）
- [ ] 封面标题、目录卡、尾卡

## 备用素材
见上篇 `output/2026-09-01-texture-alignment/draft.md` 的「备用素材」节（主结果、跨条件泛化、解码、时间窗、作者四条局限均已核实）。

### 卡② 三种图片，纹理合成那一种对齐最高
〔文风：延续卡① 的 khazix 口吻〕

先看最直接的一组。

三种图片各自跟 DNN 比一遍，看谁跟脑响应对得上。分数是 0 到 500 毫秒里那条相关曲线下的面积，除以噪声天花板的上界，读出来就是个百分比。

纹理合成图约 85%，原图约 44%，只留物体图约 55%¹。

差距很大。而且五个架构、21 个模型初始化全朝同一个方向，从 AlexNet 到 ViT-B/16，一个例外都没有¹。

反直觉的地方在这儿。纹理合成图是那种你一眼看不出画的什么的图，物体早就被打散了。可偏偏是它，跟脑子对得最好。

不过先别急着下结论。这种图是特意造出来的，模型赢在它上面，也可能只是因为它简单。

*（配图：Loke Fig 2B，待裁。Fig 2B = 噪声天花板上界归一化后的 AUC）*

〔出稿硬约束：**Fig 2A 的绝对 AUC 下，原图与只留物体无显著差异**；归一化后（2B）才是 44 vs 55。不得写成「去掉背景反而变好」。〕
〔W = 0 的处理：已按项目规则换成实义说法「21 个模型初始化全朝同一个方向」。原文 W = 0, r = 0.87, p < 0.001（Bonferroni 校正），配对单位 = 21 个模型初始化（STAR Methods, Sample size 行）。〕
〔末段「也可能只是因为它简单」为我加的替代解释，论文未明写，用户 2026-09-02 确认保留。〕

### 卡③ 纹理特征拿去预测原图的脑响应，比只留物体特征还好
〔文风：延续 khazix 口吻〕

所以作者换了个搭法。这回人只看原图，EEG 那一份固定不变，换的是喂给网络的图。

网络分别看原图、纹理合成图、只留物体图，各自的中间层激活算成 RDM，去拟合人看原图时的 RDM。

第一名是原图特征，这不意外，两边来自同一批图。第二名是纹理特征，它跟第一名的峰值完全重合，都在 138 毫秒达到 r = 0.20，差别只在峰之外的那段曲线¹。

第三名才是只留物体的特征。它输给了纹理特征¹。

论文自己都说这个结果反直觉。你把三种图摆一起，原图和只留物体明显是更像的一对，都能一眼认出企鹅，纹理合成图跟谁都不像。可预测原图脑响应的时候，最不像的那个反而更管用。

*（配图：Loke Fig 3A 最左栏，待裁）*

〔核实：Friedman χ²(2)=30.48, p<0.001；纹理 vs 原图 W=17, r=0.78, p<0.001（原图特征 AUC 更高）；原图 vs 只留物体 W=1, r=0.87, p<0.001；纹理 vs 只留物体 W=42, r=0.65, p=0.002。峰值 identical，Pearson r=0.20 at 138 ms。counterintuitive 为原文用词。〕

### 卡④ 抠掉背景没有提纯物体信号，只是让对应整体变弱
〔文风：延续 khazix 口吻〕

作者的解释是，抠掉背景，抠掉的正是撑着对齐的那个东西。

当初做只留物体这个条件，隐含的预期是提纯。把无关背景去掉，剩下更干净的物体信号，对齐应该更清楚才对。

实际不是这样。背景在自然图里占了大部分面积，全图的局部统计大半来自它。抠掉背景等于抠掉了大半个统计结构，物体信号并没有被提纯出来，只是整体的对应变弱了¹。

还有一条旁证。把只留物体的图再做一次纹理合成，形状没了，背景本来也没有，这种特征在三种 EEG 上对齐都很差¹。两边都缺，就没得对了。

纹理这一侧的证据到这儿给完了。但有个问题还没回答，人脑到底有没有在处理物体。

*（配图：暂无，或用 Fig S3。待定）*

〔核实：原文 "removing the background texture reduces the overall DNN-EEG correspondence rather than isolating a stronger object-related signal"；旁证为 Figure S3（texture-synthesized object-only features 在三种 viewing condition 下对齐均差）。另：其余两栏中对齐由 matching features 主导，但 object-only 的最佳匹配对齐仍远低于 texture-synthesized。〕

### 卡⑤ 先证明这份 EEG 里确实有物体信息
〔文风：延续 khazix 口吻〕

到这儿有个反驳绕不开。

会不会这份 EEG 里压根就没有物体信息。

这个质疑不算抬杠。17 个后部电极偏早期视觉源，每张图只闪 100 毫秒，被试做的还是跟图片内容无关的注视点变色检测。这种条件下说没测到物体信息在起作用，完全可能只是因为根本没测到物体信息。

所以作者先去把它读出来。取每个时间点的 17 维 EEG 模式，训一个分类器猜这一试次是 200 个物体概念里的哪一个。随机水平 0.5%，三种条件全部显著高于随机¹。

数看着小，但分母是 200。峰值能到 1% 以上，说明物体信息确实在里面。

反驳排除了。接下来才好问真正的问题。

*（配图：暂无，或用 Fig S4 时间进程。手上无补充材料，倾向纯文字卡）*

〔核实：原文 "all conditions yielded above-chance decoding across 200 object categories"，时间进程见 Figure S4。Fig 4 横轴取值：起点约 0.45–0.55%（随机水平附近），峰值可达约 1.25%。〕

### 卡⑥ 物体信息与对齐走进了相反的象限
〔文风：延续 khazix 口吻〕

真正的问题是，脑子里的物体信息和对齐，是同涨同落还是相反。

作者把两个量画进同一张图。横轴是那一刻的解码准确率，纵轴是那一刻的对齐，0 到 300 毫秒连成一条轨迹，三个条件三条。

三条起点全挤在左下角。然后分岔。

蓝线是纹理条件，往左上冲，130 毫秒对齐爬到 0.35，横轴还不到 0.9。红线绿线是原图和只留物体，往右下走，横轴推到 1.2 附近，纵轴只到 0.2 上下¹。

按共享物体识别计算那套说法，红绿两条必须爬得最高，它们物体信息最多。结果它们爬得最低。

论文在这里直接下了结论。对齐来自纹理类图像统计，不来自物体相关加工¹。

*（配图：`papers/loke-fig4.png`，Loke et al. 2026 Fig 4。600 dpi 投影定界已裁，标题/两轴/图例/四象限标注齐全）*

〔核实：Fig 4 为**配对**搭法（看什么图用什么图的 DNN 特征），与 Fig 2 同；交叉搭法只在 Fig 3。轨迹颜色：original 红 / texture-synthesized 蓝 / object-only 绿；浅色早、深色晚；圆点 0 ms、方块 300 ms。原文结论句 "DNN-brain alignment arises from texture-like image statistics and not from object-related processing"。〕

### 卡⑦ 对齐的峰值落在刺激后 100 到 200 毫秒
〔文风：延续 khazix 口吻〕

第四组结果换了个问法，不问是什么成分，问发生在什么时候。

把对齐那条曲线沿时间摊开，三种条件的峰值全都落在刺激后 100 到 200 毫秒¹。

这个窗口有明确的生理对应，就是前馈激活扫过 V1 到 V4（初级到第四视觉皮层，primary to fourth visual area）的那一段¹。信号第一次自下而上穿过视觉层级，反馈和循环加工还没接上。

所以对齐主要发生在早期前馈这一段。

但真正值得看的是 200 毫秒之后。

*（配图：暂无，或与卡⑧ 共用 Fig 3B）*

### 卡⑧ 200 毫秒之后，模型漏掉了一块真实存在的信号
〔文风：延续 khazix 口吻〕

200 毫秒之后进入循环加工主导的窗口¹，三条曲线都从峰值掉下来。

光看这个掉下来，说明不了什么。曲线低有两种成因，得看它离天花板还差多远。天花板就是被试之间共有的那部分方差，模型顶多解释到这儿。

看中间那张，被试看的是纹理图。灰带压得最低，彩线几乎贴着灰带下沿走¹。能解释的解释完了，没剩什么。

再看左边和右边，被试看的是原图和只留物体图。灰带明显更高，上沿一直在 0.2 以上，彩线却掉到 0.1 以下。中间空出一大块¹。

所以晚期那部分跟物体相关的信号是真实存在的，被试之间也很一致。现有的前馈架构就是没抓住它¹。

*（配图：`papers/loke-fig3B.png`，Loke et al. 2026 Fig 3B。600 dpi 投影定界已裁，三个子图/标题/两轴/面板字母 B 齐全）*

〔核实：原文 "Time-resolved alignment (Figure 3B) peaks within 100–200 ms of stimulus onset, which is consistent with afferent feedforward activity in V1–V4"；"After 200 ms, the window dominated by recurrent processing, the noise ceiling is higher in the natural and object-only viewing conditions than in the texture-synthesized viewing condition"；"alignment in the texture-synthesized condition approaches the lower noise-ceiling bound, whereas a larger gap persists for the original and object-only viewing conditions"；"later object-related neural signals in the natural and object-only conditions are less well-explained by current feedforward architectures"。灰带 = 噪声天花板区间（上下界）。〕

### 卡⑨ 裂缝一：改进落在了不参与对齐的地方
〔文风：延续 khazix 口吻〕

回到上篇留下的两处裂缝。

第一处，把网络的识别准确率做上去，脑预测性不跟着涨，有时候还往下走。

现在有解释了。对齐骑在纹理统计上，你把识别准确率提上去，改进的是网络里跟物体相关的那部分表征，而那部分恰好不在两边共享的范围内。

改进落在了不参与对齐的地方，分数自然不动¹。

这一句顺带回答了一个方法论问题。Brain-Score 那类分数为什么在模型越做越强的时候反而失灵。它测的一直是早期统计那一段，模型这些年变强的地方在别处。

还有第二处裂缝。

*（配图：暂无，纯文字卡）*

〔核实：原文 "This dissociation also explains why boosting object recognition accuracy does not consistently improve neural predictivity.8,9 Improvements to representations in DNNs that are not shared with the brain leave the alignment unchanged."
「Brain-Score 这类分数为什么失灵」一句为我的引申，论文未点名 Brain-Score；Linsley 2023 用的是 Brain-Score 标准流程，可回溯。出稿前决定保留或改中性。〕

### 卡⑩ 裂缝二：算局部统计这件事，初始化那一刻就在发生
〔文风：延续 khazix 口吻〕

第二处，权重完全没训练过的网络，脑预测性也高于随机。

作者的解释一样直接。如果对齐靠的是对纹理类统计的共同敏感性，那么架构的精巧程度和训练，两样都不是必需的¹。

往下拆一层。随机权重的卷积核仍然是一组滤波器，卷积这个操作对局部的空间结构本来就有选择性的响应，哪怕核里的数是随机的。训练改变的是这些滤波器有多挑，但提取局部统计这件事，在初始化那一刻就已经在发生了。

所以没训练的网络能拿到非零的对齐分数，它不需要学会任何东西。

这里得收着说。这条讲的是训练不是必需条件，不是训练不重要。Conwell 2024 给每个架构都配了随机初始化的对照，训练带来的提升是全篇最大最稳的一项²。没有训练不会归零，但有训练确实高得多。

*（配图：暂无，纯文字卡）*

〔核实：原文 "helps to explain why even untrained networks achieve above-chance neural prediction scores.9–11 If alignment reflects a shared sensitivity to texture-like statistics rather than learned object recognition, then neither architectural sophistication nor training is required to capture it."
「随机卷积核本身就是滤波器」一层为我加的机制说明，论文未展开。
Conwell 数据：N=64 随机初始化对照，cRSA β=0.30、veRSA β=0.56，均 p<0.001（上篇卡④已核）。〕

〔⚠ 参考文献编号待最终排序。当前暂定 ¹=Loke 2026、²=Conwell 2024；Yamins 2014、Linsley 2023 若在卡⑨/⑪ 出现需一并排入，按正文首次出现顺序重编。〕

### 卡⑪ 人靠形状认东西，和纹理驱动的对齐并不冲突
〔文风：延续 khazix 口吻〕

读到这儿会有个反问。人认东西靠的是形状，这是行为实验反复测到的形状偏好²。那对齐由纹理撑着，不就矛盾了吗。

作者的回应挺关键的。形状偏好是整条加工链的行为读出¹。你要测行为，得等信号一路走完，测到的是链条末端的结果。

而现有的 DNN 擅长的是链条前端那一段，也就是 100 到 200 毫秒的前馈扫过¹。

前端由纹理统计主导，末端表现出形状偏好，这两件事可以同时成立。它们说的根本不是同一段¹。

所以这篇没有推翻形状偏好，它只是把对齐这个分数定位到了链条的哪一节上。

*（配图：暂无，纯文字卡）*

〔核实：原文 "These findings might appear at odds with the human behavioral shape bias24: if the visual system ultimately prioritizes shape for object recognition, then a strong DNN-EEG alignment driven by texture statistics may seem paradoxical. Yet the shape bias is a behavioral readout of the full processing hierarchy.13,15 Current DNNs primarily excel at capturing this early, feedforward stage of visual processing rather than the full processing chain."
Loke 引 shape bias 的出处是 ref 24 = Hermann KL, Chen T, Kornblith S. (2020). The origins and prevalence of texture bias in convolutional neural networks. NeurIPS 33:19000–19015。本卡 ² 暂指该文，最终编号待排。〕

### 卡⑫ 这篇削弱了什么，又没削弱什么
〔文风：延续 khazix 口吻〕

所以这篇到底改了什么，得说准。

论文自己的结论句是带限定的。当前 DNN 与早期人类视觉响应之间的对应，由纹理类图像统计承载；而那些响应里确实存在的物体相关信号，网络没有捕捉到¹。

三个限定词要划出来。一个是早期，说的不是整个视觉系统。一个是确实存在，物体信号在那儿，只是没被抓住，前面那道天花板缺口就是证据。还有一个是当前，指的是现在这批前馈架构。

被削弱的是那个解释，也就是对齐等于共享物体识别计算。没被推翻的是两边确有共同之处这件事，共同之处在，改写的是它落在哪一段。

作者最后给的是方向。要推进以物体为中心的视觉模型，就需要能捕捉晚期那段物体相关加工的架构，比如显式地表征全局形状¹。

*（配图：暂无，纯文字卡）*

〔核实：原文结论 "the correspondence between current DNNs and early human visual responses is carried by texture-like image statistics, while the object-related signals present in those responses go uncaptured by the networks. Advancing models of object-centered vision will therefore require architectures that capture this later, object-related processing."；"for instance by explicitly representing global shape" 出自讨论段。
强度边界与上篇卡⑪ 一致：削弱的是解释，未证伪「存在共同之处」。〕

### 卡⑬ 作者自己列的四条局限
〔文风：延续 khazix 口吻〕

作者自己列了四条局限，值得照抄。

一，RSVP 加无关任务可能偏向前馈。被试从头到尾没被要求认东西，所以不能假定纹理优势会原样推广到显式识别任务上¹。

二，纹理合成把背景和物体的纹理一起打乱了，两者各占多少分不出来¹。

三，17 个后部电极偏浅层，对前部下颞叶（anterior inferotemporal cortex）这类深部结构不敏感。用全部电极重跑排名不变，但物体信息这个度量确实是不完整的¹。

四，这条最实在。去掉全局形状的同时也去掉了语义，200 毫秒之后的自上而下反馈可能被削弱，纹理条件的高对齐也许有一部分来自反馈变少¹。作者的反驳是，纹理优势的峰值落在 100 到 200 毫秒，早于循环加工主导的窗口，反馈变少解释不了它¹。

*（配图：暂无，纯文字卡）*

〔核实：四条均照 Limitations and conclusion 段原文。第一条原文另有一句「Task demands can modulate the magnitude and temporal profile of early visual responses without necessarily determining their overall representational structure」，卡上未收，属可删细节。第三条 Figure S5。第四条作者自提自驳，**必须两半都写**，只写质疑或只写反驳均失真。〕

## 待办（内容已全部落稿，2026-09-02）
- [ ] 参考文献最终排序（当前 ² 在卡⑩=Conwell、卡⑪=Hermann 冲突）
- [ ] Step 6 三层事实核查表
- [ ] 封面标题讨论（3–5 候选）
- [ ] 裁 Fig 2B、Fig 3A（Fig 4、Fig 3B 已裁好）
- [ ] 目录卡 + 尾卡
- [ ] 一次性渲染全套图卡
- [ ] 发布三件套（小红书标题 / 话题标签 / 公众号摘要两版）

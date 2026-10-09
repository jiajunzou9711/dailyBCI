# Neuralink 精读评论与公众号段落素材

## 读论文笔记

本文用于分块保存用户在精读中的评论，以及据此整理的公众号段落。暂按讨论顺序记录，全文读完后统一组织逻辑与递进。

落稿原则：最大程度保留用户原意、基本思路、侧重点和表达强度，仅对口语、不通顺处作轻微润色或书面化。用户未表达的观点不加入正文。教学解释留在对话中；写入草稿的补充内容以用户明确选择为准。

当前按独立条目积累重要原文内容和用户评论，暂不决定最终位置与文章结构。最终可以采用清单形式，也可以组织成连贯的段落。条目编号仅用于记录。

## 已定稿

### 01｜实验室实现与居家稳定使用的难度不同

很多人质疑马斯克和 Neuralink 的设备缺乏新的技术创新，认为它实现的功能，几十年前就已经在实验室里实现了。

但我觉得，在实验室里实现一次，与在真实的居家场景中稳定使用，难度完全处在不同的数量级。前者可能更多涉及科学上的难度，后者则更多涉及工程上的难度。工程上的难度一定不比科学上的小。

### 02｜维持控制需要持续校准

Neuralink 在文中报告，用户平均每周需要花 55 分钟进行校准，仅仅是为了维持对设备的控制。校准时，用户需要完成一系列规定任务，提供训练数据，让解码器，也就是将神经活动转化为控制指令的模型，适应当前的神经信号。随着信号变化，解码器的表现会下降，用户需要重复校准，恢复原有的控制效果。[1]

在旧系统下，用户通常每天开始使用前要校准约 10 分钟。有的用户隔几天才校准一次，校准时间少了，控制效果也随之下降；很少有解码器能连续用上几天以上。[1]

换用预训练模型后，Neuralink 报告 [1]：

- 即使是一察觉性能下降就重新校准的用户，也能连续一周以上不需要校准；
- 一位用户用同一个解码器，连续 5 天达到 10 BPS；
- 部分解码器保持良好性能超过 3 周；
- 一位研究参与者的解码器，在一年半以后仍然可以控制；
- 部分用户的校准时间从每天 10 分钟降到每周 10 分钟。

除了校准次数变少，每次校准所需的数据也变少了：30 秒带标签的嵌入数据，效果约等于 3.5 分钟的原始动作电位数据，训练出的解码器在一个月后的数据上仍然适用。[1]

【配图：图 4，figures/fig4.png。解码器性能（R²）随校准数据量的变化，左为次日、右为次月，蓝线为嵌入、橙线为原始动作电位。[1]】

机械臂任务上的改进同样明显。Neuralink 在模拟环境中测试了机械臂控制，用户要同时控制 7 个及以上自由度。这类解码器比光标解码器失效得更快：一个原本表现很好的解码器，可能 6 天后就无法使用，用户只能花更多时间重新校准。建在嵌入上的解码器，一周后仍然可以控制，用户重新校准时可以跳过前面几个阶段。[1]

来源备注：55 分钟为公司报告的平均值；改进后各项均为个例或"部分用户"，原文未给人数与分布；"30 秒≈3.5 分钟"与第 07 条重复，统稿时保留一处；"一年半以后仍可控制"对应原文图 5（20 个月前的校准）；原文此处未交代统计人数、统计时段或个体差异。最终统稿时保持“Neuralink 在文中报告”的归属表述。

### 03｜不同功能需要各自的解码器

原文还提到，打字、游戏等不同功能，都需要各自的解码器。用户要使用多项功能，就需要训练、校准多个解码器。功能越多，需要反复校准的工作也越多，这进一步增加了重复校准的负担。[1]

来源备注：这段描述对应原文开篇介绍的既有系统；后文将讨论一个神经编码器支持多项任务的方案。最终组织全文时保留这一时间与方法背景。

### 04｜224 亿个动作电位是怎么检测出来的

Neuralink 在文中报告，临床试验开始后的两年里，参与者累计上传了超过 5 万小时未标注（unlabeled）、自由状态（freeform）下的神经数据；仅第一位参与者就记录了超过 9,000 小时，共 224 亿个动作电位。[1]

这是非常海量的数据，但它们全部未经标注。

**我的评论**：据 Neuralink 报告，参与者在居家自由使用中累计记录了超过 5 万小时的皮层内放电数据。以往的人类皮层内记录，多来自研究人员在场、时长有限的实验 session [17]；这批数据的规模和采集场景都不同，理应被好好分析。我认为它至少在三个方向上值得期待：对脑本身的理解、解码的准确性，以及更长远的类脑算法开发。目前这批数据未公开。

这些动作电位怎么检测出来的，原文没有交代。我查了 Neuralink 的公开资料：2019 年的技术论文写明，信号经在线算法实时检测动作电位，且他们通常不做动作电位分选（spike sorting）[2]；人体试验的公开更新只提到，曾把记录算法调得对神经群体信号更灵敏，没有给出检测细节[3]；2021 年的猴子实验更新写明，Link 上的算法在每个电极上自动检测动作电位，每 25 ms 按电极计数后发送，同样没有提到分选[19]。由此推断，他们大概率只是给每个通道拉一条阈值线，没有做 spike sorting。所以这 224 亿个动作电位，应理解为各通道上超过阈值的放电事件总数，并未区分到单个神经元。

来源备注：[2] 为大鼠实验与早期 System A/B，非人体 N1；[19] 为猴子实验；该文只说用"在线检测算法"、通常不分选，未写明是简单电压阈值。"拉一条阈值线"属推论，统稿时保持"推断/大概率"的强度。2026 年原文写"each recording channel gets its own learned embedding … when it fires"（按通道输入事件），与"不分选"一致。

### 05｜Neuralink 试验汇总，与本文数据的关系

以官网为准，媒体报道单独标出。

| 试验 | 患者 | 植入部位 | 恢复的功能 / 解码的信息 | 状态 |
|---|---|---|---|---|
| PRIME（美国）及 CAN-PRIME、GB-PRIME、UAE-PRIME（加拿大、英国、阿联酋）[4] | 脊髓损伤或 ALS 导致双手功能丧失 | 运动皮层手结区（hand knob，位于中央前回 precentral gyrus）[1] | 控制电脑：光标移动、点击；尝试动手指打字（ALS 患者 Jake 最高约 40 词/分钟）[5] | 进行中 |
| CONVOY [4] | 从 PRIME 参与者中招募 | 同上 | 控制辅助机械臂 | 进行中 |
| VOICE [6] | ALS、原发性侧索硬化（PLS）、脊髓损伤、卒中导致的严重言语障碍 | 官网只写"参与言语产生的脑区"，未给具体脑区 | 把想说的话输出为文字或语音 | 官网称"recently launched"[5]；媒体报道 2026 年 1 月已有人植入，官方未核实 [8] |
| Blindsight [7] | 严重视力障碍 | 视觉皮层，做电刺激而非记录 | 产生人工视觉 | 官网标为即将开始（upcoming） |

截至 2026-01-28，官网报告全部试验共入组 21 人，未按试验拆分人数。[5]

和本文的关系：

- 已核实：文章写明 Link 记录手结区；所有在线结果都来自单个参与者数据预训练的模型；评测全是光标、点击和模拟机械臂。[1]
- 不确定：开头"5 万小时"说的是"our participants"，没说是否包含 VOICE 患者。[1]

来源备注：试验编号——PRIME NCT06429735、CONVOY NCT06710626、VOICE NCT07224256（均见 [4][6]）。

### 06｜这些数据为什么一直没用上：监督学习与自监督学习

Neuralink 在文中提到，这 5 万小时数据此前几乎都没有用上，原因是它们没有标签。[1]

以往的解码器都靠监督学习（supervised learning）训练。训练数据是成对的"神经活动—意图动作"，意图动作就是标签。标签只能在校准时获得：屏幕上的目标由系统给定，可以假定用户的意图是朝目标移动。日常自由使用时，系统不知道用户想把光标移到哪里，所以记录下来的神经活动没有对应的标签。

这次 Neuralink 用的是自监督学习（self-supervised learning），训练目标从神经数据本身构造。他们的做法是给模型一半通道的活动，让它预测另一半通道的活动，全程不需要意图标签。[1] 这一步叫预训练（pretraining），含义和大语言模型的预训练相同：先在大量无标签数据上学习，再用少量带标签的数据训练具体任务。

预训练的产物是嵌入（embedding），即神经活动的一种新表示。最后仍要用少量校准数据，在嵌入上训练解码器。

### 07｜预训练要解决什么问题

神经信号会随时间漂移，建在原始动作电位上的解码器会随之失效，用户只能反复校准。Neuralink 的思路是用海量无标签数据做预训练，得到一个编码器。编码器把每天都在漂移的动作电位，转成跨天保持稳定的嵌入，原文称之为"drift-robust"。[1] 解码器建在稳定的嵌入上，就能更准、用得更久，需要的标签数据也更少。

预训练并没有取消校准，只是让校准次数更少、每次更短。原文报告，30 秒带标签的嵌入数据，效果约等于 3.5 分钟的原始动作电位数据；部分用户的校准时间从每天 10 分钟降到每周 10 分钟。[1]

### 08｜编码器按患者单独训练

目前每位患者的编码器只用本人数千小时的记录做预训练。原文写明，本文所有在线使用结果，都来自用单个参与者数据预训练的模型。[1]

跨患者训练还在探索中。用多人数据合训的模型，在线表现目前不比单人模型好；但只用 P9 数据训练的模型迁移到 P2 时，冻结 99% 的权重，表现仍超过 P2 原有的解码器。[1]

### 09｜第一条假设：神经活动是动力学系统

Neuralink 为建模提出了五条假设。第一条是：神经群体活动最适合用动力学系统（dynamical system）描述。[1]

动力学系统指一个状态按固定规则随时间演化。放到神经群体上，计算神经科学的主流看法是：上千个通道的放电由一个低维的潜在状态（latent state）生成。潜在状态由上一时刻的潜在状态和当前输入决定；观测到的放电，是潜在状态经过映射再加上噪声。[9] 原文的措辞是"commonly believed"，这是领域内的主流假设，并未被证明。

据此，他们选用了 Mamba 架构。[10] Mamba 属于状态空间模型（state space model），结构本身就是隐状态逐步更新：每一步用上一时刻的隐状态和当前的放电，算出新的隐状态，和上面的假设形式一致。这类内置在模型结构里的假设，在机器学习里叫归纳偏置（inductive bias）。

Mamba 还满足一条工程约束：推断（inference）开销恒定、延迟低。[1][10] 每一步只更新一个固定大小的隐状态，计算量不随使用时长增长。光标是闭环控制，延迟必须足够低，用户才会觉得光标跟手。原文没有给出具体的延迟指标。

来源备注：[9] 为 Neuralink 原文为第一条假设所引文献，此处沿用，不展开 LFADS 本身。

### 10｜第二条假设：把每次放电当作一个 token

传统做法是把时间切成等长的时间窗，统计每个通道在每个窗里检测到几个动作电位。每个窗得到一个向量，长度等于通道数，第 i 个数永远对应第 i 个通道。这种格式有两个前提：通道数固定，通道顺序固定。

Neuralink 借鉴了 POYO 的做法 [11]：每检测到一次放电，就生成一个词元（token），内容是哪个通道、在什么时刻放电。通道身份用一个向量表示，叫通道嵌入（channel embedding），它的数值由训练学出。没有放电的通道不生成 token，模型看不到它。[1] 这样一来，同样一段时间，放电多就有很多 token，放电少就只有几个，输入长度不再固定。

后面的 Mamba 每一步需要固定大小的输入，这一步交给基于 Perceiver 的输入层 [12]。Perceiver 内置一组数量固定的潜在向量，对全部输入 token 做交叉注意力（cross-attention），无论输入有多少个 token，输出大小都相同。[1] POYO 本身就建立在 PerceiverIO 架构上 [11]，Neuralink 把它接到了 Mamba 前面。原文没有画出两者的具体连接方式，这个顺序是根据"input layer"一词推断的。

这一设计让多人数据可以合起来训练。[1] 固定向量格式下，不同患者的通道数不同，同一位置记录的也是不同神经元，数据无法直接合并。改用 token 后，每位用户有自己的一张通道嵌入表，模型其余部分在用户之间共用。

这种架构使跨用户合训成为可能。目前多人合训的模型在线表现与单人模型持平，尚未更好；但已有跨用户迁移的成功案例：只用 P9 数据训练的模型迁移到 P2，冻结 99% 的权重，表现超过 P2 原有的解码器。[1]

来源备注：原文为 "perform no better than their single-participant counterparts"（持平，非更差）；P9→P2 为原文 "In one experiment" 所举一例，原文未称仅此一例。"POYO 建立在 PerceiverIO 上"已核对 POYO 原文（"an architecture that builds on the PerceiverIO"）。

### 11｜第三条假设：通道之间存在可利用的结构

第三条假设是：不同通道的放电之间存在可预测的相关。[1] 这和第一条假设相连：如果上千个通道的放电都由同一个低维潜在状态生成，它们就会一起变化，知道一部分通道的活动，就能推测其余通道。原文为这条假设引了 POYO [11] 和 NDT2 [13]。

这条假设决定了预训练目标的设计。Neuralink 从三条约束出发反推训练目标 [1]：

- 部署时的解码器必须完全因果，在时刻 t 只能用 t 及之前的数据；
- 用户的未来意图，超过一定时间范围就无法预知；
- 动作电位数据自相关很强，同一通道相邻时间窗的计数很接近。

逐一对照候选目标：遮住中间时刻、用前后数据补全，用到了未来数据；预测较远的未来，受意图变化影响，无法预测；预测下一时刻，模型只要沿用同一通道刚才的值，误差就已经很小，学不到群体状态。只有"同一时刻遮住一半通道"同时满足三条约束。

他们的做法是：给模型一半通道的活动，让它预测另一半通道的放电，误差按泊松回归（Poisson regression）计算。[1] 动作电位计数是非负整数，计算神经科学常把它建模为泊松分布 [14]：模型对每个被遮通道输出一个放电率，用泊松似然衡量预测和实际计数的差距。

被遮通道的活动完全不输入，模型只能从可见的一半推断两者共有的潜在状态，再由潜在状态预测被遮的一半。所以这个训练目标让模型的嵌入成为对群体潜在状态的估计。[1]

来源备注：原文术语为 "spatially masked auto-Poisson regression"，"auto" 原文未定义，可能指统计学的 auto-Poisson 模型或自回归，正文只写泊松回归。三条约束对候选目标的排除是本文的推导，原文只列约束与最终选择。"被遮通道历史也不输入"按原文 "feed the model half the channel set" 理解。

### 12｜第四条假设：意图落在一个稳定的子空间里

先交代图 2 所在的模型。前三条假设组合成一个神经编码器：每次放电先转成 token，经 Perceiver 输入层汇总成固定大小的表示，再经过多层 Mamba 逐时刻更新，最后由输出头预测被遮那一半通道的放电。预训练阶段，整个模型用来做这个预测任务；使用阶段，编码器中间产生的嵌入交给解码器，解码器只用少量校准数据训练。[1] 原文没有给出层数，也没有说明解码器取的是哪一层的嵌入。

第四条假设是：和运动意图有关的神经活动，落在一个跨天稳定的低维子空间里。[1] 群体活动可以看作 N 维空间中的点，N 是通道数，但实际活动主要集中在少数几个方向张成的子空间里。电极记录到的具体神经元每天都在变化，这个子空间和其中的潜在动态却可以长期保持一致。Gallego 等人在猴子运动皮层记录长达 2 年，记录到的神经元在逐渐更替，低维潜在动态保持稳定，基于潜在动态的解码器在整个时段都可靠 [15]；Karpowicz 等人把漂移的数据对齐到同一组潜在动态上，在猴子数据中实现了数周到数月无需监督重新校准的稳定解码 [16]。

Neuralink 认为，他们的预训练模型"似乎支持"这条假设（原文为"seem to support"）。图 2 把每天的平均嵌入投影到前两个主成分上，按记录日着色，约覆盖 190 天：浅层的点按天排成一条曲线，表示随时间漂移；中间层的颜色混在一起，第 0 天和第 190 天落在同一区域；到了输出端，按天排列又重新出现。[1]

这份证据的范围有限：只看了前两个主成分和每天的平均值，没有给出定量指标；表示稳定也不等于它包含意图信息；图注也没说明数据来自哪位参与者。这条假设的依据主要还是前作，以及后文解码器寿命变长的在线结果。

【配图：图 1 动图，figures/fig1_trajectories_paired_3h.mp4。原图注：Cursor motion replayed through decoders of increasing age, contrasting spike-based and embedding-based decoders.[1]】

【配图：图 2，figures/fig2.png。[1]】

来源备注：三个子图原文未标注层名，正文只点名"middle layers"与"final output"，左图为浅层属推断。输出端按天排列重新出现的原因原文未解释，未写入正文。Neuralink 原文参考文献把 Karpowicz 2025 的文章号写作 4283，此处按 PubMed 记为 4662。

### 13｜第五条假设：一个编码器服务多个任务

第五条假设是：一个预训练好的神经编码器，可以同时服务多个任务。[1] 编码器把放电转成嵌入，所有任务共用；每个任务另有一个小解码器，把嵌入映射成具体输出，比如光标速度、点击或机械臂的各个自由度。如果这条成立，新增一项功能时，只需要在已有嵌入上训练一个小解码器，不必每项功能都从头训练、单独校准。

原文的论证分两步。一是类比：同一只手可以写字、演奏乐器、开车，不需要为每件事换一个"附件"。二是解剖依据：Neuralink 的植入设备 Link（即 N1 Implant）记录的是手结区的活动，这里的神经活动本身就要支持手的多种动作。[1] 原文为此引了 Willett 等人 2020 年的研究：他们在 BrainGate 受试者的手结区发现，这一区域以组合方式表征全身各部位的动作，不只是手。[18] 这一步属于类比论证：同一群神经元支持多种动作，并不能直接推出同一个编码器的嵌入能支持多个解码器，后者要靠实验检验。

原文后文里，建在嵌入上的解码器覆盖了光标移动、点击、模拟机械臂（7 个及以上自由度），以及屏幕上光标和目标位置的读出。[1] 这和本条假设的方向一致，但原文没有写明这些结果用的是同一个编码器，也没有和"每个任务单独训练编码器"做对照。

还要区分另一个更远的目标：用一个解码器处理所有手部任务，原文称之为"An API for the motor cortex"，放在"Future directions"中，目前没有证据。[1]

来源备注：Willett 2020 标题称该区域为"premotor cortex"，Neuralink 原文写"motor cortex"，正文统一用"手结区"，不写具体分区。"四类结果是否来自同一编码器实例"原文未写明。

### 14｜校准时的标签从哪里来

（统稿位置：放在第 03 条之后，第 15 条紧随其后。）

校准是一种监督学习，需要"神经活动—意图"的配对数据。意图无法直接测量，标签都来自任务提示：系统提示用户"现在尝试做 X"，就把 X 当作这段神经活动的标签。不同任务的标签形式不同：

| 任务 | 标签类型 | 常见做法（领域内的例子） |
|---|---|---|
| 光标移动 | 连续的二维速度 | 开环：光标自动移向目标，用户想象自己在控制它，光标的实际速度被当作意图速度 [19]；闭环再校准：用户先用初步的解码器控制光标，假定意图始终指向目标，把解码出的速度方向改成指向目标作为标签（ReFIT）[20] |
| 点击 | 离散类别：点 / 不点、点击类型 | 光标停在目标上时提示用户尝试点击，提示的时刻作为点击标签 |
| 机械臂 | 连续的多自由度速度 | 先让用户看着机械臂自动运动并想象控制它，再逐步过渡到用户自己控制 [21] |
| 言语 | 序列：音素或文字 | 屏幕上提示句子，用户尝试说出；神经活动和音素序列的时间对齐由算法估计 [22] |

这些做法的共同前提是：用户确实在按提示尝试动作。这个前提不总成立，所以标签本身带有噪声。

来源备注：表中为领域内的通行做法，Neuralink 原文未说明各任务的具体校准流程；原文只提到机械臂解码器可以"skip the early stages of calibration"，说明其校准分阶段进行 [1]。点击一行为通行做法的概括，未挂具体文献。[20] 为猴子数据。

### 15｜旧的解码方式，以及它为什么需要频繁校准

Neuralink 没有公开人体试验系统用的解码器。能找到的最接近的说明，是 2021 年猴子实验的更新 [19]：Link 每 25 ms 统计一次各电极的动作电位计数，电脑把计数按 25 ms 到 250 ms 的多个时间尺度累加，再对这些特征做加权求和，得到每个控制维度的速度，对时间积分后得到光标位置。这是一个线性解码器。校准就是收集一批"计数特征—按任务设计推定的意图速度"的配对数据，用回归求出这组权重。人体系统是否沿用这种方式，原文和此前的更新都没有说明。

这种解码器需要频繁校准，原因在于它的权重直接绑定在具体电极上。比如 A 电极向上运动时放电多，权重就给 A 一个正值。如果几天后 A 电极附近的神经元发生了变化，放电减少，或者换成了另一个神经元，这个权重就不再对应原来的意图，解码出的速度随之出现偏差。神经信号的这种漂移每天都在发生，于是权重需要重新估计，也就是重新校准。

新的方式在中间加了一层编码器。编码器先把各电极的放电转成跨天稳定的嵌入，解码器的权重建在嵌入上，而不是具体电极上。只要嵌入保持稳定，解码器就能用得更久，重新校准时需要的数据也更少。[1]

两种方式的区别可以概括为：旧系统每次校准，都是用几分钟带标签的数据，直接在原始计数上重新拟合解码器；新系统先用数千小时无标签的日常记录，以自监督方式训练一个编码器（每位受试者一个，训练一次），此后每次校准，只用少量带标签数据在嵌入上训练解码器。正因为编码器的训练不需要标签，才能用上这么多天的数据。[1] 原文没有说明校准时编码器是否完全固定，"编码器不动、只训解码器"是按"decoders trained on learned embeddings"所做的推断。

本文所有在线结果都来自这种单人模型。跨受试者训练他们已经试过：多人合训模型的在线表现目前不比单人模型好；但有一次跨受试者迁移成功，只用 P9 数据训练的模型迁移到 P2，冻结 99% 的权重，表现超过 P2 原有的解码器。[1] 所以准确的说法是：跨受试者训练做过，在线效果还没有超过单人模型。

来源备注：[19] 为猴子实验（2021），不代表人体系统。跨受试者一段与第 08、10 条内容重复，统稿时保留一处。"权重绑定电极导致漂移失效"是按线性解码器的结构做的推导，与 Gallego 2020 报告的"直接建在神经活动上的固定解码器性能明显下降"一致 [15]。

### 16｜从解码"怎么动"到解码"想去哪"

运动皮层编码的不只是肌肉活动和运动速度。以下是代表性研究：

- 光标或手的**位置**：猴子运动皮层同时表征位置和速度 [23]；
- **决策**：猴子在两个候选目标之间选择时，背侧运动前区（dorsal premotor cortex，PMd）先同时表征两个选项，收到提示后，被选中的那个信号增强，另一个被抑制，群体活动能预测猴子最终的选择 [24]；
- **运动准备**：猴子在动作开始前，运动皮层就已经出现准备活动，这些活动位于不驱动肌肉输出的"零空间"（null space）里 [25]；
- **错误信号**：猴子在 BCI 光标任务中出错时，运动前区和初级运动皮层出现结果错误信号，可以在试次结束前解码出来 [26]；
- **全身动作**：人类手结区还以组合方式表征全身各部位的动作 [18]。

直接解码目标早有先例：2006 年，Santhanam 等人在猴子的 PMd 上，从运动计划阶段的活动中直接解码目标位置，信息传输率达到 6.5 bits/s [27]。

Neuralink 在这条方向上做了初步尝试：用无状态的线性模型，直接从嵌入中读出光标和目标在屏幕上的坐标（图 7）[1]。在此基础上，他们设想了"光标瞬移"（cursor teleportation）：预测用户想去的目标，把光标一步移到那里，省去拖动的时间。初步测试中，这种方式明显缩短了光标移动时间，信息传输率超过 10 BPS（图 8）[1]，达到健全人用鼠标的水平（约 8–10 BPS）[5]。

【配图：图 8 动图，figures/fig8_p23_slingshot.mp4。原图注：10 BPS control driven by predicted target location.[1]】

**我的评论**：这是全文最让我兴奋的部分。解码对象从运动的速度变成运动的目标，BCI 就不必再模仿鼠标的操作逻辑。

Neuralink 也写明了局限：目前还不能做到像素级精确地预测目标（"We can't yet predict the intended target with pixel-perfect precision"）[1]。

Neuralink 在文末还提出了一个设想：给运动皮层建立统一的接口，原文称"An API for the motor cortex"。所有手部动作意图共用一个解码器，用户只需校准一次，开发者在同一个接口上开发应用。[1]

**我的评论**：这是一个不错的构想，野心也很大。运动皮层控制手部运动，手部动作又能完成各种任务，所以理论上，手能完成的事，BCI 也有可能完成；结合上面的研究，运动皮层编码的不只是手的运动，手完成不了的事，也有可能通过 BCI 完成。目前已实现的还只是光标、点击和模拟机械臂，这个设想尚无实验证据。

来源备注：[23]–[27] 均为猴子数据；API 设想与第 13 条末段重复，统稿时保留一处；[24][25][27] 的记录部位为 PMd 或运动皮层。"10 BPS"为原文"initial testing"的结果，原文未给测试人数。

### 17｜零校准，还是闭环协同适应

Neuralink 在"Future directions"中提出了"零校准"（zero-shot calibration）的设想：如果模型能泛化到所有人，用户术后醒来，设备就能直接匹配其意图，不需要任何校准。[1]

**我的评论**：如果系统真的好用，花点时间校准也没什么不行。我认为更值得追求的，是算法和使用者相互适应的过程：闭环、双向、实时，由 AI 辅助。对算法来说，用户可以边用边被校准，比如想往左、光标却往右，这一次就应当成为一条重要的训练数据，实时调整解码器；反过来，算法也可能重塑用户的运动想象方式，想往左却往右时，用户也可以调整自己的想象方式，看能否纠正过来。

这一方向在领域里称为协同适应（co-adaptation），已有十多年的研究基础：解码器可以在用户自由使用时，根据最终的选择反推意图，在后台持续重新校准（人）[28]；解码器固定时，用户会逐渐形成稳定的神经活动模式（猴）[29]，而这种学习受原有群体结构的约束（猴）[30]；闭环的解码器适应和大脑可塑性可以相互配合，形成熟练控制（猴）[31]。

实时自我校准的核心难点是推定意图：光标往右时，系统并不知道用户想往左。常见做法是根据目标位置推定 [20]、根据用户事后的纠正推定 [28]，或直接从神经活动中解码错误信号 [26]。

零校准和闭环适应并不冲突：前者决定第一次使用时的起点，后者负责之后的长期维持。Neuralink 在"One-shot calibration"一点中也写到，要让一次校准维持一年以上，"would require decoders that adapt as neural signals change"。[1] 据公开资料，目前的系统仍是用户察觉性能下降后自行发起校准，没有证据表明已有实时闭环的自动校准。[1]

来源备注："想往左、光标却往右"为用户原话中的例子，保留。"目前没有实时闭环自动校准"是依据原文"recalibrate at the first sign of declining performance"及此前公开更新所做的推断，公开资料未提及不等于未做。

## 讨论中

暂无。

## 备用素材

原文全部图已存入 figures/（来源均为 [1]）：图 1 fig1_trajectories_paired_3h.mp4（不同"年龄"解码器回放光标轨迹，动作电位 vs 嵌入）；图 2 fig2.png（每日平均嵌入 PCA）；图 3 fig3_p15_11_32_record_composite_legend.mp4（P15 创纪录 11.32 BPS）；图 4 fig4.png（解码器性能 vs 校准数据量，次日/次月）；图 5 fig5_p1_20_month_board.mp4（20 个月前的校准仍可控制）；图 6 fig6_p9_webgrid_100x100_no_bps.mp4（P9 在 100×100 网格上的精细控制）；图 7 fig7_p18_position_both_decay_dark.mp4（位置读出）；图 8 fig8_p23_slingshot.mp4（按预测目标位置控制，10 BPS）。

此前讨论提到公司早期便强调居家产品方向，尚待核查早期官方材料。用户本轮确认的第 01 条已按其选定的两段文字保存，未加入这一额外表述。

## 参考文献

1. Neuralink. Pretraining on 50,000 Hours of Unlabeled Brain Data. 2026-10-01. https://neuralink.com/updates/pretraining-on-50000-hours/
2. Musk, E., & Neuralink. (2019). An integrated brain-machine interface platform with thousands of channels. Journal of Medical Internet Research 21(10):e16194.
3. Neuralink. PRIME Study Progress Update — User Experience. 2024. https://neuralink.com/updates/prime-study-progress-update-user-experience/
4. Neuralink. Neuralink for Device Control. 访问于 2026-10-03. https://neuralink.com/trials/device-control/
5. Neuralink. Two Years of Telepathy. 2026-01-28. https://neuralink.com/updates/two-years-of-telepathy/
6. Neuralink. Neuralink for Speech Restoration. 访问于 2026-10-03. https://neuralink.com/trials/speech-restoration/
7. Neuralink. Clinical Trials. 访问于 2026-10-03. https://neuralink.com/trials/
8. Notebookcheck. Neuralink brain implant brings back the voice of ALS patient with thought-to-speech BCI. 2026. https://www.notebookcheck.net/Neuralink-brain-implant-brings-back-the-voice-of-ALS-patient-with-thought-to-speech-BCI.1406566.0.html
9. Pandarinath, C., et al. (2018). Inferring single-trial neural population dynamics using sequential auto-encoders. Nature Methods 15:805–815.
10. Gu, A., & Dao, T. (2023). Mamba: Linear-time sequence modeling with selective state spaces. arXiv 2312.00752.
11. Azabou, M., et al. (2023). A unified, scalable framework for neural population decoding. Advances in Neural Information Processing Systems 36.
12. Jaegle, A., et al. (2021). Perceiver: General perception with iterative attention. Proceedings of the 38th International Conference on Machine Learning 139:4651–4664.
13. Ye, J., et al. (2023). Neural Data Transformer 2: Multi-context pretraining for neural spiking activity. Advances in Neural Information Processing Systems 36.
14. Dayan, P., & Abbott, L. F. (2001). Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems. MIT Press. 第 1 章.
15. Gallego, J. A., et al. (2020). Long-term stability of cortical population dynamics underlying consistent behavior. Nature Neuroscience 23:260–270.
16. Karpowicz, B. M., et al. (2025). Stabilizing brain-computer interfaces through alignment of latent dynamics. Nature Communications 16:4662.
17. Hochberg, L. R., et al. (2006). Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442:164–171.
18. Willett, F. R., et al. (2020). Hand knob area of premotor cortex represents the whole body in a compositional way. Cell 181:396–409.e26.
19. Neuralink. Pager Plays MindPong. 2021. https://neuralink.com/updates/pager-plays-mindpong/
20. Gilja, V., et al. (2012). A high-performance neural prosthesis enabled by control algorithm design. Nature Neuroscience 15:1752–1757.
21. Collinger, J. L., et al. (2013). High-performance neuroprosthetic control by an individual with tetraplegia. The Lancet 381:557–564.
22. Willett, F. R., et al. (2023). A high-performance speech neuroprosthesis. Nature 620:1031–1036.
23. Wang, W., et al. (2007). Motor cortical representation of position and velocity during reaching. Journal of Neurophysiology 97:4258–4270.
24. Cisek, P., & Kalaska, J. F. (2005). Neural correlates of reaching decisions in dorsal premotor cortex: specification of multiple direction choices and final selection of action. Neuron 45:801–814.
25. Kaufman, M. T., et al. (2014). Cortical activity in the null space: permitting preparation without movement. Nature Neuroscience 17:440–448.
26. Even-Chen, N., et al. (2017). Augmenting intracortical brain-machine interface with neurally driven error detectors. Journal of Neural Engineering 14:066007.
27. Santhanam, G., et al. (2006). A high-performance brain–computer interface. Nature 442:195–198.
28. Jarosiewicz, B., et al. (2015). Virtual typing by people with tetraplegia using a self-calibrating intracortical brain-computer interface. Science Translational Medicine 7:313ra179.
29. Ganguly, K., & Carmena, J. M. (2009). Emergence of a stable cortical map for neuroprosthetic control. PLoS Biology 7:e1000153.
30. Sadtler, P. T., et al. (2014). Neural constraints on learning. Nature 512:423–426.
31. Orsborn, A. L., et al. (2014). Closed-loop decoder adaptation shapes neural plasticity for skillful neuroprosthetic control. Neuron 82:1380–1393.

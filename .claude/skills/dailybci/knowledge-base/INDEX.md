# DailyBCI Knowledge Base

Last updated: 2026-08-05
Total papers: 372

## speech-decoding (19 papers)
- [Guenther 2009](papers/speech-decoding/guenther-2009-wireless-bmi-speech.md) — 首个无线BMI实时语音合成，单电极元音合成，概念验证
- [Leuthardt 2011](papers/speech-decoding/leuthardt-2011-ecog-speech-bci.md) — 首个ECoG语音信号BCI控制，开创用说话意图控制BCI的ECoG路线
- [Bouchard 2013](papers/speech-decoding/bouchard-2013-sensorimotor-speech-organization.md) — 发现语音运动皮层编码发音动作（非声学特征），奠定articulatory decoding基础
- [Herff 2015](papers/speech-decoding/herff-2015-brain-to-text.md) — 首次brain-to-text连续解码，phone→LM→text框架，后续路线的起点
- [Anumanchipalli 2019](papers/speech-decoding/anumanchipalli-2019-speech-synthesis-neural-decoding.md) — 首次从脑活动合成可理解语音，确立两阶段解码范式（神经→运动→声音）
- [Makin 2020](papers/speech-decoding/makin-2020-machine-translation-cortex-text.md) — 首个encoder-decoder框架brain-to-text，引入sequence-to-sequence范式
- [Moses 2021](papers/speech-decoding/moses-2021-neuroprosthesis-anarthria.md) — 首次在瘫痪失语患者解码语音（PANCHO研究），50词，15词/分钟，NEJM
- [Willett 2023](papers/speech-decoding/willett-2023-high-performance-speech.md) — Phoneme-level解码，62词/分钟，125k词汇 WER 23.8%（50词词汇表 WER 9.1%），证明phoneme路线可扩展
- [Metzger 2023](papers/speech-decoding/metzger-2023-speech-avatar-neuroprosthesis.md) — 78词/分钟+虚拟头像面部动画，首个多模态speech BCI
- [Luo 2023](papers/speech-decoding/luo-2023-stable-als-speech-bci.md) — ALS患者3个月无校准稳定使用，证明ECoG长期临床可行性
- [Card 2024](papers/speech-decoding/card-2024-accurate-rapidly-calibrating.md) — 97.5%准确率，125k词汇，<30分钟校准，8个月稳定，NEJM
- [Silva 2024](papers/speech-decoding/silva-2024-bilingual-speech-neuroprosthesis.md) — 首个双语speech BCI，发现跨语言共享articulatory表征
- [Wairagkar 2025](papers/speech-decoding/wairagkar-2025-instantaneous-voice-synthesis.md) — **皮层内** brain-to-voice：256 电极直合成语音波形(不经文本)+闭环音频反馈，端到端约 80–130ms；首次实时解出**副语言**维度(语调/重音/三级音高可唱旋律/语速)。听者六选一中位 100%，但**开放转写音素错误率仍 43.6%**(人类单被试 T15，Nature 644:145-152)
- [Littlejohn 2025](papers/speech-decoding/littlejohn-2025-streaming-brain-to-voice.md) — 同年 brain-to-voice 的**另一条路线**：Chang 组高密度 **ECoG** + 流式 RNN-Transducer，80ms 增量在线合成，声音个性化到伤前嗓音(人类单被试 BRAVO-3「Ann」，脑桥卒中，Nat Neurosci 28:902-912)。**与 Wairagkar 2025 务必区分**：模态/团队/病因全不同
- [Kunz 2025](papers/speech-decoding/kunz-2025-imagined-speech-decoding.md) — Cell：motor cortex inner speech表征+实时self-paced inner-speech BCI proof of concept（4名参与者表征分析，3名实时解码；50词WER 14-33%，125k词WER 26-54%）
- [Yoon 2026](papers/speech-decoding/yoon-2026-deep-neural-ensembles.md) — 深度集成首次实时闭环验证(WER 33.7%→26.0%)；提出伪集成单解码器降算力，把优化轴从精度扩到可部署性
- [Card 2026](papers/speech-decoding/card-2026-longterm-independent-bci.md) — 皮层内语音+光标BCI首次家庭自主长期使用：ALS患者19个月/3801小时/18.3万句、研究员不在场、保住全职工作；transformer达99.2%词准确率，信号18个月余弦相似度>0.6(同一患者T15，Nature Medicine)
- [Wairagkar 2026](papers/speech-decoding/wairagkar-2026-brain2voice2-voice-synthesis.md) — 脑-语音合成首次跨过可懂度门槛：多模态因果Transformer(四路互补目标:连续声学/离散RVQ token/音素/自监督)+多尺度对抗，听者WER 5.24% vs前作43.75%(8×)、79%句零错；治回归损失抹糊辅音的根本问题(同队Wairagkar 2025续作，人类单被试T15，bioRxiv)

- [Fogg 2026](papers/speech-decoding/fogg-2026-generalizable-speech.md) — **首次证明皮层内语音表征跨人共享到「解码器可整个冻结」的程度**：六名 BrainGate2 参与者数据合池训一个 transformer 音素解码器，对**每一位**都优于其单人模型(相对 WER 均降 51.1%；**T17 从 65.6%→23.1%**，把一个不可用的解码器拉回 2023 年 SOTA 水平)；闭环实时降 55.9%。承重设计是 **frozen-decoder 适配**——解码器全冻、新用户只训一个线性映射+tanh(约 0.26M，占全模型约 0.4%)，**T22 90 试次/约 17 分钟→WER 10.2%**，同数据从零训 SU 为 76.9%；左半球模型可适配到右半球。缩放 1→4 人 17.6%→9.5% **未饱和**。已排除深度(SU 加深不受益)与句子重叠(去重后仍胜出)两个混淆。**边界**：T15-Large 仅 14.3%(本人数据极多时收益缩水)、六人小样本、全英语、同一皮层内系统与脑区(人类 6 名，bioRxiv)

## semantic-decoding (12 papers)
语义解码：从神经活动读出"此刻想的是哪个概念"，而非"嘴要怎么动"。与 speech-decoding 的根本差别是解码层级——后者 17 篇全押在发音/音素层(articulatory)，本线目标是概念层。milestone 抽取自 **Rybář & Daly 2022 (J Neural Eng 19, PRISMA 系统综述)** 的引用，理论侧锚定 Patterson 2007 / Ralph 2017 两篇 Nat Rev Neurosci。
**两条硬约束，评估本线任何新工作时先过一遍：**
1. **"颅内高伽马能否解出语义范畴"在 2011 年已被肯定回答**([[wang-2011-ecog-semantic-decoding]])，2011 年后任何"首次证明颅内可解语义"的说法都需仔细核边界；真增量必须落在别处(更多范畴/跨模态泛化/未训练概念外推/实时闭环/自然语境)。
2. **方法学最高标杆是 [[rupp-2017-ecog-semantic-attributes]]**(12 范畴 + 零样本外推 + 约等于全脑 fMRI)。只做封闭集 N 选一分类、无属性空间无外推的新工作，方法学上其实落后于 2017 年。
- [Rybář & Daly 2022](papers/semantic-decoding/rybar-2022-semantic-decoding-review.md) — **本子领域 milestone 抽取源**(J Neural Eng 19，PRISMA 跨模态系统综述)：作者自陈是首篇跨神经成像模态、以量化解码器效能为重点的语义解码综述。用**信息传输率**作统一标尺衡量各模态解码器，把评价标准从"显著高于随机"推向"作为通信通道够不够用"。发在 BCI 核心期刊本身即说明语义解码已被接编进神经工程议程
- [Patterson 2007](papers/semantic-decoding/patterson-2007-semantic-knowledge-representation.md) — 理论地基(Nat Rev Neurosci 8:976–987)：hub-and-spoke 架构，模态特异皮层为辐条、**前颞叶(ATL)** 为模态无关枢纽；关键论据是语义性痴呆的**跨模态跨类别**语义崩解。给语义解码提供"电极该放哪"的空间先验
- [Mitchell 2008](papers/semantic-decoding/mitchell-2008-predicting-noun-meanings.md) — 范式起点(Science 320:1191–1195)：万亿词语料的动词共现向量表词义→线性映射到 fMRI，可预测**从未扫描过**的名词激活(60 名词验证显著)。确立"不解码是哪个词、解码词义向量再检索"这条此后通用的路线(zero-shot 祖先)
- [Liu 2009](papers/semantic-decoding/liu-2009-fast-object-decoding-intracranial.md) — 颅内单试次范畴解码奠基(Neuron 62:281–290，11 人/912 电极)：刺激后**最早 100ms** 即可单试次解出物体范畴，且对深度旋转/尺度稳健。证明颅内场电位的范畴信息单试次可提取(实时 BCI 前提)。**归位：解的是视觉物体范畴，偏知觉侧**
- [Simanova 2010](papers/semantic-decoding/simanova-2010-eeg-object-categories.md) — 非侵入侧起点(PLoS ONE 5:e14465)：头皮 EEG 单试次范畴解码，但**模态落差显著**——物体线描图 89%，听觉/书面词仅部分被试显著。提示 EEG 可读成分很大程度是知觉驱动而非概念枢纽；此后评估任何语义解码都要问"准确率来自概念还是刺激的知觉表面属性"
- [Wang 2011](papers/semantic-decoding/wang-2011-ecog-semantic-decoding.md) — **"语义 BCI"提法的源头之一**(EMBC 2011:6294–6298，4 人 ECoG)：图片命名任务，高伽马 60–120Hz，LIFG + pSTG 稳健激活，GNB/SVM 可预测语义范畴；明确提出 semantic-based BCI 服务重度交流障碍者。**摘要无准确率数值，引用时勿编造**；概念验证级而非性能级
- [Huth 2016](papers/semantic-decoding/huth-2016-semantic-maps.md) — 自然语流 + 体素级编码模型画出连续语义地图(Nature 532:453–458)，语义选择性**平铺整个皮层**、跨双侧广布。推论对颅内不友好：sEEG/ECoG 只采样到这张大地图的稀疏片段，是颅内准确率长期低于全脑 fMRI 的结构性原因
- [Ralph 2017](papers/semantic-decoding/ralph-2017-semantic-cognition-review.md) — 理论整合(Nat Rev Neurosci 18:42–55)：语义认知 = **表征**(ATL 枢纽)+**控制**(IFG/pMTG 网络按语境调制取出哪些属性)，双分离由语义性痴呆 vs 语义通达障碍证据支撑。推论：同一概念的神经模式随任务/语境变，解码器可能学到任务态而非概念；且 **LIFG 属控制网络而非表征枢纽**，在那里解出的东西未必等于概念表征本身
- [Rupp 2017](papers/semantic-decoding/rupp-2017-ecog-semantic-attributes.md) — **本线方法学标杆**(NeuroImage 148:318–329)：ECoG 命名 12 语义范畴，训高维**属性编码模型**映射谱-时特征，对**未训练物体**零样本解码达**与全脑 fMRI 相当**；高伽马 70–110Hz 在基底枕颞关联三个语义维度(人造-有生命/典型大-小/场所-工具)。唯一把 Mitchell 2008 属性+零样本范式完整搬进人类 ECoG 的工作
- [Pereira 2018](papers/semantic-decoding/pereira-2018-universal-decoder.md) — 把 Mitchell 范式推到逻辑终点(Nat Commun 9:963)：语义空间采样选训练刺激→**单概念训练、解码句子**，覆盖具体+抽象、两独立数据集，可区分语义相似句。**抽象概念 + 句子级至今仍是颅内的空白**
- [Nagata 2022](papers/semantic-decoding/nagata-2022-abstract-concrete-semantics.md) — 颅内线上**唯一以词(非图片)为刺激**的代表作(Cereb Cortex 32:5544–5554)：ECoG 高伽马 + SVM 单试次分抽象/具体词 **73.1±7.5%**；避开了"解出的其实是视觉特征"这个软肋，并把抽象性带进颅内。**注意是二分类(随机 50%)，约 0.16 bit/试次，作通信通道远不够；引用务必带"二分类"，勿与多分类准确率直接比大小**
- 邻线交叉引用(条目在 ai-neural-modeling)：[[tang-2023-semantic-language-reconstruction]](首次非侵入 fMRI 语义重建连续语言，Pereira 2018 直系后继)、[[ismail-2026-naturalistic-word-meaning]](人类单神经元词义编码，21 患者/871h 被动自然语音，10 类语义解码 20.9% vs 随机 10%)
- [Quian Quiroga 2005](papers/semantic-decoding/quian-quiroga-2005-concept-cells.md) — 人类内侧颞叶概念细胞：特定概念只激活极少数高度选择性神经元，且跨呈现形式不变。**稀疏编码使「撒一批电极」的冗余逻辑失效**，靶向精度要求由此回归

## motor-bci (21 papers)
- [Georgopoulos 1986](papers/motor-bci/georgopoulos-1986-population-vector.md) — Population vector理论，证明运动方向可从神经群体活动数学读出
- [Chapin 1999](papers/motor-bci/chapin-1999-real-time-robot-control.md) — 首个实时BMI，大鼠用神经信号控制机械臂，开启闭环控制时代
- [Wessberg 2000](papers/motor-bci/wessberg-2000-real-time-trajectory-prediction.md) — 首次灵长类3D手运动轨迹实时解码+远程机器人控制
- [Serruya 2002](papers/motor-bci/serruya-2002-instant-neural-control.md) — 猴子7-30个神经元即时光标控制，临床级电极，为人体试验铺路
- [Taylor 2002](papers/motor-bci/taylor-2002-direct-cortical-control-3d.md) — 首个闭环3D神经假肢控制，无需肢体运动
- [Carmena 2003](papers/motor-bci/carmena-2003-bmi-cortical-ensemble-learning.md) — 首次同时解码reaching+grasping，皮层可塑性在BMI学习中重组
- [Hochberg 2006](papers/motor-bci/hochberg-2006-braingate-first-human.md) — 首个人类intracortical BCI（BrainGate），瘫痪患者思维控制光标
- [Velliste 2008](papers/motor-bci/velliste-2008-prosthetic-arm-self-feeding.md) — 猴子用皮层信号控制假肢手臂自主进食，首个复杂功能性任务
- [Gilja 2012](papers/motor-bci/gilja-2012-refit-kalman-filter.md) — ReFIT-KF闭环算法，光标性能翻倍接近真实手臂，证明算法是关键瓶颈
- [Hochberg 2012](papers/motor-bci/hochberg-2012-reach-grasp-robotic-arm.md) — 人类首次BCI控制机器人手臂3D reach-and-grasp，瘫痪患者自主饮咖啡
- [Collinger 2013](papers/motor-bci/collinger-2013-7dof-robotic-arm.md) — 7自由度机器人手臂控制，13周训练达到高性能，证明高维解码可行
- [Aflalo 2015](papers/motor-bci/aflalo-2015-posterior-parietal-motor-imagery.md) — 首个人类后顶叶皮层BCI，从PPC解码运动意图
- [Bouton 2016](papers/motor-bci/bouton-2016-neural-bypass.md) — 首个neural bypass：BCI+FES恢复瘫痪患者自身手部分级运动
- [Vansteensel 2016](papers/motor-bci/vansteensel-2016-fully-implanted-ecoG-bci.md) — 首个完全植入式BCI，locked-in ALS患者家庭使用
- [Ajiboye 2017](papers/motor-bci/ajiboye-2017-reach-grasp-fes.md) — BCI+FES恢复完整上肢reach-and-grasp，患者自主进食饮水
- [Willett 2021](papers/motor-bci/willett-2021-handwriting-bci.md) — 手写解码BCI，90字符/分钟，开辟精细运动意图解码新范式
- [Flesher 2021](papers/motor-bci/flesher-2021-bidirectional-bci.md) — 首个双向BCI：运动解码+触觉反馈，抓取任务时间减半
- [⚠ Unverified Willett 2024](papers/motor-bci/willett-2024-finger-click-bci.md) — 已隔离：当前DOI/PubMed/arXiv均未能核实，不作为motor-bci milestone使用
- [Neuralink 2024](papers/motor-bci/neuralink-2024-prime-n1-first-human.md) — 首个全植入无线1024通道BCI人体试验，患者日常使用>10h
- [BrainGate 2023](papers/motor-bci/braingate-2023-long-term-safety.md) — 17年14名参与者长期安全数据，信号仅下降7%，支撑临床扩展
- [Conlan 2026](papers/motor-bci/conlan-2026-ifg-grasp-decoding.md) — 首次在人类额下回(IFG，猕猴F5同源区)皮层内记录中用析因设计拆分抓法/物体/交互三因素：抓法解码显著主导(41.1-41.8% vs 33.3%随机)，物体贡献弱且更早、movement期已不显著；补上"非M1皮层内电极靶点"这条此前空白的线(与Ajiboye 2017对照，同组·bioRxiv)

## electrode-hardware (27 papers)
- [Wise 1970](papers/electrode-hardware/wise-1970-silicon-microprobe.md) — 首次用IC工艺制造多位点神经探针，开启微加工电极时代
- [Campbell 1991](papers/electrode-hardware/campbell-1991-utah-array.md) — Utah阵列发明，100通道3D硅电极，BCI临床试验的硬件基石
- [Rousche 1998](papers/electrode-hardware/rousche-1998-chronic-biocompatibility.md) — 首次系统验证Utah阵列慢性植入可行性，揭示胶质瘢痕核心挑战
- [Kim 2010](papers/electrode-hardware/kim-2010-dissolvable-silk-electrode.md) — 可溶解丝蛋白基底+超薄共形电极，开创暂态基底柔性电极策略
- [Viventi 2011](papers/electrode-hardware/viventi-2011-flexible-ecog.md) — 360通道柔性ECoG，有源多路复用解决高密度引线瓶颈
- [Borton 2013](papers/electrode-hardware/borton-2013-wireless-broadband.md) — 首个全频段宽带无线神经接口，100通道24Mbps植入式传输
- [Liu 2015](papers/electrode-hardware/liu-2015-syringe-injectable-mesh.md) — 注射式网状电子器件，力学匹配脑组织，颠覆刚性探针范式
- [Oxley 2016](papers/electrode-hardware/oxley-2016-stentrode-endovascular-array.md) — Stentrode血管内电极阵列，开辟不开颅的endovascular BCI路线
- [Luan 2017](papers/electrode-hardware/luan-2017-ultraflexible-nanoelectronic-probes.md) — 超柔性纳米探针实现无胶质瘢痕神经集成，证明力学匹配是根本方案
- [Jun 2017](papers/electrode-hardware/jun-2017-neuropixels.md) — Neuropixels探针，CMOS工艺单根960位点，改变大规模记录可及性
- [Musk/Neuralink 2019](papers/electrode-hardware/musk-2019-neuralink-threads.md) — 1024通道全无线BCI平台，柔性线程+手术机器人+定制ASIC
- [Obaid 2020](papers/electrode-hardware/obaid-2020-cmos-microwire-arrays.md) — 微线阵列直接集成CMOS芯片，展示大规模穿透式记录的片上读出路线
- [Simeral 2021](papers/electrode-hardware/simeral-2021-braingate-wireless.md) — 首次intracortical BCI家庭无线化使用，24小时连续运行
- [Paradromics 2025](papers/electrode-hardware/paradromics-2025-acute-connexus-human.md) — Connexus 首次人类急性植入/记录/完整取出(<20分钟)，为后续 Connect-One 长期植入试验铺路；高密度皮层内阵列 + 胸部收发器路线
- [Hettick 2025](papers/electrode-hardware/hettick-2025-layer7-cortical-interface.md) — Layer 7高密度皮层表面阵列，推动微创、可逆的临床ECoG路线
- [Steinmetz 2021](papers/electrode-hardware/steinmetz-2021-neuropixels-2.md) — Neuropixels 2.0：四针脚/5120电极点/384同时通道，确立此后的事实标准规格；也留下「电极点远多于同时通道」这个瓶颈
- [Chang 2026](papers/electrode-hardware/chang-2026-neuropixels-quad-base.md) — Quad Base：几何与5120电极点全不动，同时通道384→1536(双探针3072)；用同一份记录自我抽子集作对照，证明一次8针脚同时记录检出的跨区Granger连接数超过四次连续2针脚记录的总和(总通道数相同)。推论：少通道会系统性低估脑区间耦合(小鼠)
- [Jung 2025](papers/electrode-hardware/jung-2025-bisc-wireless-subdural-bci.md) — BISC无线无电池subdural interface：65,536电极、1,024通道，探索超大规模皮层表面接口
- [Bourhis 2026](papers/electrode-hardware/bourhis-2026-tft-backplane.md) — 显示式有源矩阵TFT背板(a-IGZO直接长在聚酰亚胺)：256通道(16×16)柔性皮层表面阵列，布线O(n)→O(√n)、温升<2°C、封装投影寿命>38年、大鼠30天稳定；确立"柔性有源(非转印硅)"一格(Dayeh组·UCSD)
- [Li 2026](papers/electrode-hardware/li-2026-skull-microhole-hybrid-bci.md) — "颅骨微孔电极"新微创模态:超声自限打 300–800 μm 微孔(不取材料、对软硬膜不切削、终止检测 34ms/16μm)+单点 Pt/Ir 电极皮下植入、远端贴硬膜外(不穿硬膜)、有源电子体外经隔皮欧姆传导耦合;大鼠上 SEP/SSVEP 信噪比与各频段功率抬 2.6–8.9×、刺激侧仅仿真(TI 深部聚焦)。在"头皮 EEG↔硬膜外 ECoG"间插一格:点 vs 片、微孔 vs 骨瓣(对照 [[neo-2024]]);范式提出型,大鼠记录+仿真,企业参与(中山大深圳×深圳BrainXess,bioRxiv)
- [Poncelet 1992](papers/electrode-hardware/poncelet-1992-human-brain-motion.md) — **人体**相位对比 MRI：心动周期内脑组织相对颅骨峰值位移 0.1–0.5 mm，是 50 µm 单单元区的 2–10 倍。讨论临床植入的机械环境时以此为准(非大鼠数据)
- [Gilletti 2006](papers/electrode-hardware/gilletti-2006-brain-micromotion.md) — 大鼠开颅后界面处直测微动：呼吸 10–30 µm、心跳 2–4 µm，有硬膜时更小。慢性微创伤的机械源头；与 Poncelet 1992 测的不是同一个量，引用须标条件
- [Lacour 2016](papers/electrode-hardware/lacour-2016-soft-implantable-neuroprostheses.md) — 力学失配的标准综述：硅约 165 GPa vs 脑 1–10 kPa，相差约 10⁷–10⁸ 倍，应变集中到界面。把失配从「生物相容性」重定位为力学设计问题
- [Biran 2005](papers/electrode-hardware/biran-2005-neuronal-kill-zone.md) — kill zone 定量：电极周围 100 µm 内神经元密度降约 40%，4–8 周内最近健康神经元可退到数百微米。慢性失效的机制从「信号被挡住」改写为**信号源被推走**
- [Savya 2022](papers/electrode-hardware/savya-2022-astrocyte-reactivity-dynamics.md) — 星胶反应时空动力学(大鼠)：第 1 周激活达峰、约 500 µm，第 3 周约 700 µm，第 6 周致密包裹趋稳。给出慢性相的时间与空间刻度
- [Ludwig 2006](papers/electrode-hardware/ludwig-2006-pedot-coating-chronic.md) — PEDOT 涂层慢性记录：信噪比与可用单单元数均优于对照。**几何足印与有效表面积可分离**的实证落地——涂层只涨后者，故不必一味把电极做小
- [Kinaci 2020](papers/electrode-hardware/kinaci-2020-dura-cross-species.md) — 10 物种同法比较硬脑膜厚度：人 564 µm vs 大鼠 49 µm（差 11.5 倍），猪 304 µm 最接近；大鼠/绵羊/山羊/马仅单一纤维血管层。**动物硬膜无法代表人**的定量依据

## signal-processing (11 papers)
- [Wu 2006](papers/signal-processing/wu-2006-kalman-filter.md) — Kalman filter贝叶斯连续解码，奠定motor BCI实时状态估计基线
- [Sussillo 2012](papers/signal-processing/sussillo-2012-rnn-closed-loop-decoder.md) — FORCE RNN闭环decoder，证明非线性时序模型可超越velocity Kalman filter
- [Gilja 2012](papers/signal-processing/gilja-2012-refit-kalman-filter.md) — ReFIT-KF用闭环反馈意图重训decoder，目标获取时间约减半
- [Jarosiewicz 2015](papers/signal-processing/jarosiewicz-2015-self-calibrating-bci.md) — RTI自校准intracortical BCI，让decoder从自然打字行为中持续更新
- [Sussillo 2016](papers/signal-processing/sussillo-2016-robust-neural-variability.md) — 面向未来神经变异的鲁棒decoder训练，强调长期泛化而非单日准确率
- [Pandarinath 2018](papers/signal-processing/pandarinath-2018-lfads.md) — LFADS序列自编码器，从spikes中恢复single-trial潜在神经动力学
- [Willett 2021](papers/signal-processing/willett-2021-handwriting-rnn.md) — RNN解码imagined handwriting，把motor BCI通信转化为字符序列识别
- [Moses 2021](papers/signal-processing/moses-2021-speech-decoding-language-model.md) — 词级speech decoder + language model，首次实时恢复瘫痪失语患者句子输出
- [Willett 2023](papers/signal-processing/willett-2023-phoneme-rnn-language-model.md) — Phoneme RNN + language model，将speech BCI扩展到125k词汇和高速输出
- [Metzger 2023](papers/signal-processing/metzger-2023-multimodal-speech-avatar-decoder.md) — 多模态speech/avatar decoder，把神经解码从文本扩展到声音与表情控制
- [Card 2024](papers/signal-processing/card-2024-rapid-calibration-speech.md) — 快速校准speech decoder + online adaptation，推进临床可用的高准确率通信

## non-invasive (39 papers)
- [Farwell 1988](papers/non-invasive/farwell-1988-p300-speller.md) — P300 speller范式，6×6矩阵，定义非侵入BCI通信范式
- [Wolpaw 1991](papers/non-invasive/wolpaw-1991-mu-rhythm-cursor.md) — 首个mu节律EEG光标控制，确立SMR-BCI路线
- [Pfurtscheller 1997](papers/non-invasive/pfurtscheller-1997-motor-imagery-erd.md) — Motor imagery ERD/ERS，建立运动想象BCI神经生理学基础
- [Birbaumer 1999](papers/non-invasive/birbaumer-1999-thought-translation-device.md) — Thought Translation Device，首次locked-in患者非侵入通信，Nature
- [Wolpaw 2002](papers/non-invasive/wolpaw-2002-bci-review.md) — BCI领域定义性综述，建立标准术语和系统架构，8000+引用
- [Blankertz 2006](papers/non-invasive/blankertz-2006-berlin-bci-zero-training.md) — Berlin BCI零训练范式，CSP+机器学习，训练负担从用户转向算法
- [Chen 2015](papers/non-invasive/chen-2015-high-speed-ssvep-speller.md) — SSVEP speller 5.32 bits/sec，60字符/分钟，非侵入BCI速度纪录，PNAS
- [Lawhern 2018](papers/non-invasive/lawhern-2018-eegnet.md) — EEGNet跨范式通用CNN，成为EEG深度学习标准基线
- [Defossez 2023](papers/non-invasive/defossez-2023-meta-meg-speech-decoding.md) — Meta FAIR用MEG解码语音，72.5% top-10准确率，非侵入语音BCI探索
- [Brain2Qwerty 2026](papers/non-invasive/brain2qwerty-2026-meg-typing-decoding.md) — Meta FAIR用MEG解码"打字时脑活动"逐句成文：v1(Nat Neurosci,同步,CER 32%)→v2(preprint,异步,WER 39%≈61%词准确率)；CTC去掉按键时刻依赖(同步→异步/离线→在线)、三层+微调LLM、准确率随数据对数线性(r=−0.99)未见顶；接Defossez同组MEG(感知→产出)，局限:MEG大扫描仪+健康人真打字、迁移未证
- [Ding 2025](papers/non-invasive/ding-2025-finger-mi-healthy.md) — 首次用头皮EEG实时控制individual-finger级机械手(健康熟练者，2指80.6%/3指60.6%)：把"逐指"从皮层内推到非侵入，He组非侵入逐指线起点
- [Ding 2026](papers/non-invasive/ding-2026-finger-mi-stroke.md) — 首次在零经验中风患者用头皮EEG实现实时逐指机械手控制：2指83.5%/3指61.4%(随机50%/33%)、患侧≈健侧(d=0.18/0.42)、低频delta是信号；中风把精细运动编码重组成双侧/分散/低频，EEGNet跟住(He组，naïve中风≈其2025 Nat Commun健康熟练者)

### OPM / 可穿戴 MEG 硬件线 (OPM-MEG instrumentation)
脑磁图(MEG)的**仪器**这一格：从 SQUID(必须泡液氦、刚性阵列、被试不能动)换成光泵磁力计(OPM，室温工作、可贴头皮、可随头移动)之后，MEG 的哪些结构性限制被解开、又派生出哪些新限制。与 non-invasive 里既有的 MEG 条目(Defossez 2023、Brain2Qwerty 2026)分工明确：那些讲**用 MEG 解码什么**，本线讲**MEG 这台机器本身**。milestone 抽取自 **Brookes et al. (2022, Trends Neurosci 45:621-634)** 的引用。建于 2026-08-02。
**三条硬约束，评估本线任何新工作时先过一遍：**
1. **"贴近头皮"与"允许运动"是两件被分开解决的事**，别混为一谈：前者靠 scanner-cast 定制头模([[boto-2017-room-temperature-opm-meg]])，后者靠主动场置零线圈([[holmes-2018-biplanar-nulling-coils]])。宣称"信号更强"和宣称"能自由活动"承重在不同证据上。
2. **"测到信号"≠"能做源定位"。** 源定位要求整个阵列、且每个传感器沿已知方向测量([[tierney-2019-opm-quantum-origins]])。[[zhang-2020-unshielded-earth-field-meg]] 在无屏蔽地磁场下测到了 alpha 与 M100，但只有 2 通道、未做源定位——这两步之间隔着很大一段。
3. **截至 2022 年综述，"脱离被动屏蔽室"和"被试在房间里走动"仍是公开问题**([[brookes-2022-opm-meg-review]] Outstanding Questions)。任何声称跨过这两条的新工作，需核它跨的是哪一条、跨到什么程度。
- [Cohen 1972](papers/non-invasive/cohen-1972-squid-meg.md) — MEG 的起点：用 **SQUID** 首次实用化地测到人脑自发磁场活动。同时定下此后半个世纪的技术底座与全部结构性限制——传感器泡在约 4 K 液氦里，因而必须刚性固定、离头皮约 2 cm、被试不能动
- [Allred 2002](papers/non-invasive/allred-2002-serf-magnetometer.md) — 整条 OPM 路线的**物理前提**：提出 **SERF(自旋交换弛豫自由)** 工作区，靠加热蒸气使碰撞快到不破坏自旋相干，消除限制灵敏度的自旋交换弛豫。也埋下 OPM 的两个先天代价——传感器发热、且**只在近零场工作(动态范围约 3 nT)**，后者正是可穿戴 OPM 必须配主动屏蔽的根本原因
- [Sander 2012](papers/non-invasive/sander-2012-chipscale-opm-meg.md) — 把 OPM 从"物理可行"推到"**几何上可阵列化**"：用芯片级原子磁力计测到人脑磁信号，此后 MEG 用的 OPM 才被做成约乐高积木大小的自包含单元，可穿戴头盔由此成立
- [Iivanainen 2017](papers/non-invasive/iivanainen-2017-on-scalp-arrays.md) — 定量算清"贴近头皮"的取舍(仿真)：相对 SQUID 磁强计，法向 OPM 阵列信号功率高 **7.5×**、点扩散小 **2.4×**、信息容量明显更高，但**单偶极子定位精度三者相当**。收益主要在信号强度与分辨多源的能力。法向 vs 切向的体电流削减差异(**10% vs 72%**)解释了后续系统为何普遍测垂直头皮分量
- [Boto 2017](papers/non-invasive/boto-2017-room-temperature-opm-meg.md) — 从仿真走向**人体实测**：室温 OPM + 按解剖定制的 3D 打印 scanner-cast 贴近头皮，与同被试常规 SQUID MEG 对照。**但传感器仍刚性固定、被试仍需静止**——"可穿戴"要到下一步才成立
- [Holmes 2018](papers/non-invasive/holmes-2018-biplanar-nulling-coils.md) — 把瓶颈从传感器转到**磁场环境工程**，并给出此后的标准解法：双平面"指纹"绕线线圈生成三个均匀场 + 五个一阶梯度做主动置零。Bx 从 **21.8→0.47 nT**、dBx/dz 从 **7.4→0.55 nT/m**；置零后头模转动 **±34°**、平移 **±9.7 cm**，阵列上场变化仅约 **1 nT**。限制：只在头部上方**固定体积**内补偿，且仍在被动屏蔽室**内**
- [Boto 2018](papers/non-invasive/boto-2018-wearable-meg-nature.md) — **可穿戴 MEG 奠基**(Nature 555:657-661)：OPM 头盔 + 主动置零合成一套系统，被试点头/伸展/喝水/打乒乓球时完成毫秒级记录。头动幅度 **>±10 cm**(常规 **<2 mm**)，残余场降约 **50×**、主梯度降约 **35×**，传感器噪声约 **15 fT/√Hz**；原型 **13 通道**、连接性演示 **26 通道**。**边界**：仍在被动屏蔽室内、场置零只覆盖固定体积，不允许在房间里走动
- [Hill 2019](papers/non-invasive/hill-2019-lifespan-compliance.md) — 把 OPM 的收益扩到"**能扫的人群更广**"(lifespan compliance)：头盔可按头围贴合定制，破掉常规 MEG"一码通吃刚性壳"导致的小头者信号弱、覆盖不均。截至 2022 综述**仍无 0–1 岁婴儿 OPM-MEG 研究**(头盔重量婴儿承受不了)
- [Tierney 2019](papers/non-invasive/tierney-2019-opm-quantum-origins.md) — 本线**方法学参考点**(NeuroImage 199:598-608)：从量子原理到多通道 MEG 数据处理的整链，重点是传感器标定与位置/朝向共配准。确立那条硬前提——**能否做源定位取决于能否稳定确定传感器几何**
- [Zhang 2020](papers/non-invasive/zhang-2020-unshielded-earth-field-meg.md) — 另一条技术路线：放弃 SERF、改用可覆盖地磁场的 **AM-NMOR 标量磁力计**做双传感器梯度计，在**未屏蔽地磁场**下测到闭眼 alpha(7–13 Hz)与听觉诱发场 M100，梯度噪声约 **4 fT/cm·√Hz**。**关键边界：仅 2 通道、未做源定位**(北京大学 Hong Guo 组)
- [Brookes 2022](papers/non-invasive/brookes-2022-opm-meg-review.md) — **本子线 milestone 抽取源**(Trends Neurosci 45:621-634，开放获取)。梳理 OPM 物理、屏蔽技术与应用；屏蔽链条 **60 µT(地磁)→5 nT(被动)→200 pT(被动+主动)**，屏蔽因子约 **300 000**；OPM 噪声本底约 **7–10 fT/√Hz** vs SQUID 约 **2–5 fT/√Hz**，明确指出 OPM 尚未达到 SQUID 噪声本底、**深部源 SQUID 可能仍占优**。Outstanding Questions 直接列出"可重构线圈让零场体积跟着人走""行走等大幅运动尚未演示""屏蔽仍笨重昂贵"

### 听觉注意解码 / neuro-steered hearing (AAD line)
- [Mesgarani & Chang 2012](papers/non-invasive/mesgarani-2012-attended-speaker-cortical.md) — 人类ECoG首证听觉皮层选择性重建被注意说话者，AAD的神经科学地基
- [Ding & Simon 2012](papers/non-invasive/ding-2012-auditory-object-encoding.md) — MEG显示皮层包络追踪把被注意语音编码为"auditory object"，非侵入证据
- [O'Sullivan 2015](papers/non-invasive/osullivan-2015-single-trial-eeg-aad.md) — 首次单试次头皮EEG解码听觉注意（包络重建），整条EEG-AAD路线的奠基石
- [Van Eyndhoven 2017](papers/non-invasive/vaneyndhoven-2017-eeg-informed-speaker-extraction.md) — 首次AAD+被注意说话者提取耦合，跑通神经导向助听假体流水线
- [Han 2019](papers/non-invasive/han-2019-speaker-independent-aad.md) — 说话者无关AAD，无需干净源，DNN分离+皮层匹配泛化到未见说话者（人类iEEG）
- [Vandecappelle 2021](papers/non-invasive/vandecappelle-2021-cnn-locus-attention.md) — CNN短窗(1-2s)直接解码注意方位，从慢速包络重建转向快速空间解码
- [Debener 2015](papers/non-invasive/debener-2015-around-ear-eeg.md) — 耳周柔性印刷电极(cEEGrid)+手机，可穿戴/微型化EEG记录的奠基
- [Geirnaert 2021](papers/non-invasive/geirnaert-2021-aad-review-benchmark.md) — AAD定义性综述+统一基准，提出MESD性能指标，本线milestone抽取来源
- [Geirnaert 2022](papers/non-invasive/geirnaert-2022-unsupervised-time-adaptive-aad.md) — 无监督+时间自适应AAD，免逐人标注，走向实际部署的实用性milestone
- [Jayaram & Barachant 2018](papers/non-invasive/jayaram-2018-moabb-benchmarking.md) — MOABB：首个聚合多公开EEG数据集+统一评估框架，暴露EEG领域可重复性危机，EEGDash的直接前驱

### 自定步调/异步控制 (self-paced / idle-state detection)
BCI连续控制中"用户能否自主起停、系统能否识别非控制态"这条子线。milestone抽取自Mason et al. 2007综述。
- [Mason 2007](papers/non-invasive/mason-2007-comprehensive-survey-bci-designs.md) — 系统分类BCI接口设计(同步/异步)，定义self-paced为独立设计维度，本子线milestone抽取来源综述
- [Borisoff 2004](papers/non-invasive/borisoff-2004-lf-asd-asynchronous-brain-switch.md) — LF-ASD异步脑开关改进版，早期"意图性脑开关"实证，确立idle-state误报是异步BCI核心问题(UBC Birch组)
- [Scherer 2007](papers/non-invasive/scherer-2007-self-paced-graz-bci.md) — Graz组3类自定步调运动想象BCI，显式区分IC/NC两态，虚拟环境导航+Google Earth真实闭环验证，今日候选(Müller-Putz组)概念前驱

### 语言模型辅助拼写纠错 (LM-assisted spelling / error correction)
把语言模型用于非侵入BCI拼写系统的纠错/免校准，与speech-decoding线的LM+解码器范式呼应但应用在更慢速的P300拼写场景。milestone抽取自Mora-Cortes et al. 2014综述。
- [Mora-Cortes 2014](papers/non-invasive/mora-cortes-2014-language-model-bci-spelling-review.md) — 系统综述LM在BCI拼写中的应用分类(预测补全 vs 纠错、静态vs动态界面)，本子线milestone抽取来源
- [Speier 2012](papers/non-invasive/speier-2012-nlp-dynamic-classification-p300.md) — 首次证明HMM+语言模型动态分类显著提升P300拼写器准确率和比特率，LM纠错路线奠基实证
- [Kindermans 2012](papers/non-invasive/kindermans-2012-p300-bci-masses-prior.md) — 贝叶斯语言先验让P300拼写器免校准、无监督即可用，把LM角色从事后纠错扩展到替代监督训练

## invasive-recording (21 papers)
- [Kennedy 1998](papers/invasive-recording/kennedy-1998-first-human-intracortical-bci.md) — 首次人类慢性intracortical记录用于BCI，Neurotrophic Electrode
- [Leuthardt 2004](papers/invasive-recording/leuthardt-2004-first-ecog-bci.md) — 首次证明ECoG可用于BCI控制，确立ECoG作为记录模态的"最优平衡点"
- [Schalk 2008](papers/invasive-recording/schalk-2008-ecog-2d-control.md) — 首次ECoG 2D控制，发现high-gamma具有cosine方向调谐特性
- [Ray 2011](papers/invasive-recording/ray-2011-high-gamma-origin.md) — 证明high-gamma反映群体放电率（非节律振荡），ECoG特征选择的理论基础
- [Chestek 2011](papers/invasive-recording/chestek-2011-long-term-signal-stability.md) — 系统量化intracortical信号慢性退化，证明threshold crossing优于sorted单元
- [Buzsáki 2012](papers/invasive-recording/buzsaki-2012-extracellular-fields-origin.md) — 定义性理论框架：所有胞外信号（EEG/ECoG/LFP/spikes）的生物物理起源
- [Flint 2013](papers/invasive-recording/flint-2013-lfp-long-term-bmi.md) — LFP-based BMI性能可比spikes，11个月稳定无需重训练
- [NEO 2024](papers/invasive-recording/neo-2024-epidural-minimally-invasive-bci.md) — 首个无线无电池硬膜外人体BCI，eECoG作"第四类模态"，C4完全SCI患者9个月家用信号不降反升，驱动脑-脊髓康复（清华×博睿康）
- [NEO 2025](papers/invasive-recording/neo-2025-fine-grained-2d-cursor.md) — 硬膜外微创BCI实现精细二维光标控制，发现双侧/多效应器表征，ITR 36.7 bpm、记录稳定>18个月
- [Jafri 2026](papers/invasive-recording/jafri-2026-white-matter-signals.md) — 把"白质触点=灰质衰减副本"这个默认证伪：谱参数化拆出 offset(总功率)/exponent(1/f斜率)，衰减只能动前者——实测两者双降(exponent 2.46 vs 2.77)且 **19 人无一例外**；delta 中心频率位移(2.40 vs 2.00 Hz)更是完全免疫于幅度缩放。白质复杂度更高，仅凭信号分类组织 AUC 0.92。给 [[buzsaki-2012]] 的理论补上实证："生成机制不同"对了(灰=慢突触电流/白=快轴突动作电位)，"那里什么都没有"错了。前作见条目内(Mercier 2017/Greene 2021/**Li 2021=解码增益出处**/Revell 2026)。**本篇不做解码**；束归位为作者自陈 putative 且主文无方法、FA 相关仅 rho=0.12(19人/1717触点，36%在白质，bioRxiv)

### sEEG 植入精度 / 立体定向 (implantation accuracy & stereotaxy)
"电极到底能放多准"这条子线——侵入式记录的隐形地基：所有颅内 BCI/认知研究都搭在癫痫术前评估的临床基础设施上，采样到哪个解剖结构由植入精度决定。milestone 抽取自 Cardinale et al. 2016 (J Clin Neurophysiol, 系统综述) + Abbas et al. 2026 (Acta Neurochir, meta 分析) 两篇。
**这条线最有价值处：它把"机器人比框架更准"这个看似常识的判断变成了证据分裂、需逐项拆混杂的实证问题。当前最好的合并结论是"机器人买到的是时间，不是精度"。**
- [Bancaud & Talairach 1970](papers/invasive-recording/bancaud-1970-seeg-functional-stereotaxic-exploration.md) — sEEG 的起点与命名来源：立体定向慢性植入深部电极、在自然发作期三维采样，确立 Talairach 方法学；今天几乎所有人类颅内认知/语义研究的临床基础设施由此而来(完整方法学专著见 Talairach 1974, Neurochirurgie 20 Suppl 1:1–240)
- [Cardinale 2013](papers/invasive-recording/cardinale-2013-seeg-500-procedures-accuracy.md) — 定义性精度基准(米兰 Niguarda，500 台/6496 根)：靶点误差中位数传统流程 2.69mm→新流程(无框架无标记+多模态规划+机器人) 1.77mm，入点 1.43→0.78mm，主要并发症 2.4%。**关键：提升来自整包流程变更，无法归因到机器人单一变量**
- [González-Martínez 2016](papers/invasive-recording/gonzalez-martinez-2016-robot-assisted-seeg.md) — 机器人辅助 sEEG 代表性技术论文(Cleveland Clinic，ROSA，100 人/101 台/1245 根)：靶点误差中位数 1.7mm、入点 1.2mm，与 Cardinale 2013 新流程互证"现代流程靶点误差约 1.7–1.8mm"；总并发症 4%。**前瞻观察、无对照组**，不证明机器人更准
- [Mullin 2016](papers/invasive-recording/mullin-2016-seeg-safety-meta-analysis.md) — 首次系统汇总 sEEG 并发症(PRISMA)：总 1.3%(95%CI 0.9–1.7)、出血 1.0%、感染 0.8%、死亡 0.3%；侵入式 BCI 讨论风险时的参照系(注：临床 sEEG 留置 1–2 周即取出，不可直接外推到慢性植入)
- [Cardinale 2016](papers/invasive-recording/cardinale-2016-seeg-implantation-review.md) — 系统综述(milestone 抽取源)：指认本领域核心麻烦是**精度指标定义不统一**(欧氏/径向/深度/靶点/入点误差混用)导致跨研究比较失效；此诊断到 2026 年仍成立
- [Iordanou 2019](papers/invasive-recording/iordanou-2019-approach-angle-accuracy.md) — 首次把"精度取决于轨迹几何"落成硬数字：斜行(>30°)径向误差 2.05mm vs 正交(<30°) 1.45mm，p<0.001(约差 41%)；机器人不是精度恒定的黑盒
- [Vakharia 2021](papers/invasive-recording/vakharia-2021-robot-vs-manual-rct.md) — **本线唯一 RCT**(UCL·Duncan 组，32 人，单盲随机，CONSORT)，结论反直觉：机器人 iSYS1 **更快**(螺栓 6.36 vs 9.06 min，p<0.0001)但手动 PAD **更准**(靶点 1.16 vs 1.58mm，p=0.004；角度误差 1.71° vs 2.13°，p=0.023)。证据等级最高，解读任何机器人 vs 框架对比的必备对照
- [Abbas 2026](papers/invasive-recording/abbas-2026-robot-vs-frame-meta-analysis.md) — 最新最大合并证据(8 项回顾队列/758 人，检索至 2025-09)：精度**无显著差异**(深度 MD 0.24mm、径向 MD 0.07mm，CI 均跨 0)、安全性无差异，机器人只是**显著更快**(总手术 −32.58min、每根 −6.55min)。与唯一 RCT 汇成一致图景：**机器人买到时间不是精度**；单中心回顾性报告"机器人更准"时应先追问选择偏倚与年代流程混杂
- [Thurairajah 2026](papers/invasive-recording/thurairajah-2026-seeg-accuracy-3000-trajectories.md) — 当代最大规模实证盘点(单中心回顾队列，260 人/**3176 条轨迹**/12 年，人类)，把这条线从"设备之争"推进到"逐轨迹因素分解"：① 精度更多是**轨迹几何**属性——同批病人/同台机器人/同颞叶内误差随进针角度差 **2.8 倍**(海马后部 1.18mm@10.4° ↔ 颞极 3.28mm@33.9°)，角度是可规划因素中相关最强(ρ=0.28)、每变 30° 增约 1mm、cutpoint 22.25°(但 AUC 仅 0.67)；组织状态也相关(硬化海马 1.58 vs 正常 1.12mm)；② **15% 天花板**——所有已测因素多变量 R²=0.150，毫米级不确定性大体是技术固有属性。**边界**：本文"机器人更准(2.19 vs 2.76mm)"是单中心回顾、框架组为历史对照(2013–17)有年代混杂(作者自陈)，与 [[vakharia-2021-robot-vs-manual-rct]]/[[abbas-2026-robot-vs-frame-meta-analysis]] 汇成"设备之争被混杂放大、几何才是主因";只称"相关"未验证力学机制;**不做解码**，经"植入定位"母题接 BCI(2026-07-17 日报主文章;催生待做专题 ⑥ 精度/容差/回避三路线)
- [Henze 2000](papers/invasive-recording/henze-2000-extracellular-spike-distance.md) — 胞内+胞外同步标定「距离 vs 动作电位幅度」的地面真值(麻醉大鼠 CA1)：可分离单单元约 <50 µm，分离阈值 SNR 3–4 倍/约 50–60 µV。听力半径由定性直觉变成可引用数字
- [Lindén 2011](papers/invasive-recording/linden-2011-lfp-spatial-reach.md) — LFP 空间可及范围建模：不相关输入约 250–500 µm，输入相关同步时同相叠加可达毫米级，且频率依赖。**半径主导权在「源同不同步」而非电极**，解释了文献分歧

## functional-ultrasound (11 papers)
功能超声成像(fUS/fUSI)：用超快多普勒读取神经血管耦合下的脑血容量变化。信号层级是血流动力学(与 fMRI 同类的间接信号)，但空间分辨率达亚毫米、时间分辨率亚秒，且不穿刺皮层，因此在 BCI 记录模态谱系里占据"皮层内电生理 vs 非侵入成像"之间的一格。milestone 抽取自 Wang et al. (2023) *The Emergence of Functional Ultrasound for Noninvasive Brain–Computer Interface* (Research/AAAS, PMC10427153) 与 Deffieux et al. (2018, Curr Opin Neurobiol) 两篇综述，BCI 解码线的近期三篇(Norman/Griggs/Rabut)为综述后补充。
关键约束：**成人颅骨挡住超声**，所以人体 fUS 必须有声窗——新生儿囟门 / 术中开颅 / 植入声学透明颅骨置换物。这条约束决定了这条线的全部临床形态。

### 方法学地基
- [Montaldo 2009](papers/functional-ultrasound/montaldo-2009-plane-wave-compounding.md) — 相干平面波复合：一次发射整个平面波 + 多角度相干叠加，把帧率推到每秒数千帧而不牺牲画质；fUS 的物理前提(非神经科学论文)
- [Macé 2011](papers/functional-ultrasound/mace-2011-functional-ultrasound-brain.md) — fUS 原始方法论文：超快多普勒成像脑血容量瞬态变化，大鼠触须诱发响应+癫痫样传播；整条模态的起点
- [Errico 2015](papers/functional-ultrasound/errico-2015-ultrasound-localization-microscopy.md) — 超声定位显微(ULM)：微泡逐个定位突破衍射极限，>500 fps、深度>10 mm 分辨 <10 µm 脑微血管(大鼠)；分辨率上限的另一条线

### 清醒 / 行为下记录
- [Sieu 2015](papers/functional-ultrasound/sieu-2015-fus-eeg-mobile-rats.md) — 首次在清醒自由活动大鼠做 fUS 并同步 EEG(迷宫 theta + 自发癫痫两个概念验证)，把 fUS 变成行为下可用的记录手段
- [Blaize 2020](papers/functional-ultrasound/blaize-2020-fus-deep-visual-cortex-nhp.md) — 2 只清醒猕猴深部视皮层(V1/V2/V3，距状沟/月状沟内)视网膜拓扑成像，分辨出类眼优势柱模式；确立"介观"定位

### 人体：声窗决定形态
- [Demené 2017](papers/functional-ultrasound/demene-2017-fus-human-newborns.md) — 首次人体 fUS：经新生儿囟门 + 同步视频 EEG，检出睡眠状态相关脑血容量变化、定位癫痫起始灶(UfD 200 µm / EEG 1 ms)
- [Imbault 2017](papers/functional-ultrasound/imbault-2017-intraoperative-human-fus.md) — 首次成人人脑 fUS：术中开颅提供声窗，250 µm/1 ms，定位脑沟深部任务诱发激活(清醒与全麻患者)
- [Rabut 2024](papers/functional-ultrasound/rabut-2024-human-acoustic-cranial-window.md) — 声学透明 PMMA 颅骨置换物做成永久声窗：1 名成人(TBI 后颅骨重建)在手术室之外清醒 fUSI，约 200 µm 分辨率，游戏任务的映射与解码；把人体 fUS 从"一次性机会"变成可重复会话

### BCI 解码线
- [Norman 2021](papers/functional-ultrasound/norman-2021-single-trial-decoding-fus.md) — 首次把 fUS 当 BCI 记录模态检验：猕猴硬膜外记录 PPC(100 µm)，从运动前延迟期信号**单试次**离线解出运动方向与效应器
- [Griggs 2024](papers/functional-ultrasound/griggs-2024-closed-loop-ultrasonic-bmi.md) — 首个**闭环**超声 BMI：2 只恒河猴用 PPC 的 fUS 流控制至多 8 个运动方向；用既往会话预训练解码器，跨天(相隔数月)立即可控、免大规模重校准
- [Lin 2026](papers/functional-ultrasound/lin-2026-human-cranial-window-effector-mapping.md) — 人体 fUSI 首次做到单指级躯体拓扑 + 单试次 + 跨会话解码：装声学透明 PMMA 颅骨窗的成人(同 Rabut 2024 的被试)，300 µm 体素同覆 M1/S1/SMG，五指质心间距 1.49–5.82 mm、单试次解码约 78%(机会 20%)；反预期仅 BA 1 显著解码。血流类换空间不换时间(0.6 Hz、需 block 设计)的例证(Andersen/Shapiro 组·Caltech)

## sensory-feedback (14 papers)
- [Romo 1998](papers/sensory-feedback/romo-1998-icms-tactile-discrimination.md) — 首次ICMS产生与自然触觉不可区分的人工触觉感知
- [Dhillon 2005](papers/sensory-feedback/dhillon-2005-peripheral-nerve-sensory-feedback.md) — 首次周围神经接口提供截肢者触觉和本体感觉反馈
- [Tabot 2013](papers/sensory-feedback/tabot-2013-biomimetic-icms-touch.md) — 仿生ICMS模式恢复接近自然水平的触觉辨别，确立"仿生刺激"原则
- [Raspopovic 2014](papers/sensory-feedback/raspopovic-2014-bidirectional-sensory-prosthesis.md) — 首个实时双向感觉假肢，截肢者无视觉辨别物体硬度和形状
- [Tan 2014](papers/sensory-feedback/tan-2014-long-term-stable-touch.md) — 周围神经接口提供>1年稳定自然触觉感知，解决长期稳定性瓶颈
- [Flesher 2016](papers/sensory-feedback/flesher-2016-first-human-icms-s1.md) — 首次人类S1皮层ICMS恢复触觉，感觉自然、按体感觉排列、稳定数月
- [Osborn 2021](papers/sensory-feedback/osborn-2021-icms-object-identification.md) — IEEE EMBC：人类S1 ICMS触觉反馈支持无视觉物体识别，从感觉诱发推进到信息传递

### 刺激安全与电荷注入限值 (stimulation safety & charge-injection limits)
这条线服务 ICMS(感觉反馈/双向 BCI),同样支撑 neuromodulation 的 DBS/SCS。
- [McCreery 1990](papers/sensory-feedback/mccreery-1990-charge-density-charge-per-phase.md) — 实证奠基:电荷密度×每相电荷协同决定刺激损伤阈值(猫皮层),Shannon判据的数据基础
- [Shannon 1992](papers/sensory-feedback/shannon-1992-safe-levels-model.md) — Shannon方程 k=log(D)+log(Q),k=1.85安全/损伤分界,最广引用的刺激安全判据(宏电极)
- [Merrill 2005](papers/sensory-feedback/merrill-2005-electrical-stimulation-protocols.md) — 定义性电化学教程:可逆/不可逆法拉第反应、water window、电荷平衡双相波形设计
- [Cogan 2008](papers/sensory-feedback/cogan-2008-stimulation-recording-electrodes.md) — 电极材料电荷注入容量(TiN/Pt/IrOx)定义性综述,把安全限值落到具体材料
- [McCreery 2010](papers/sensory-feedback/mccreery-2010-chronic-icms-neuronal-loss.md) — ICMS专属慢性损伤实证:微电极长时刺激致尖端≥150µm神经元丢失(猫),把宏电极判据推到微电极
- [Cogan 2016](papers/sensory-feedback/cogan-2016-tissue-damage-thresholds.md) — 重审Shannon判据:源于宏电极、未必适用微电极,当代微刺激安全再评估起点
- [Iliasov 2026](papers/sensory-feedback/iliasov-2026-microbubble-icms-safety.md) — 子簇首篇"在体实时血管成像看ICMS损伤":清醒小鼠双光子,气泡面积随电流~二次方增长、≥60µA急转BBB破裂;把电解微气泡从被动标志重定位为主动致损机制,给柔性电极ICMS机制性安全窗(何飞组·光机所×复旦华山)

## neuromodulation (52 papers)
- [Benabid 1991](papers/neuromodulation/benabid-1991-dbs-tremor-suppression.md) — 开创现代DBS疗法，高频VIM刺激长期抑制帕金森震颤，可逆可调
- [Limousin 1998](papers/neuromodulation/limousin-1998-stn-dbs-parkinson.md) — 确立STN-DBS作为晚期帕金森标准治疗，UPDRS运动评分改善~50%
- [Morrell 2011](papers/neuromodulation/morrell-2011-rns-closed-loop-epilepsy.md) — 首个闭环脑刺激RCT（RNS），191名癫痫患者，2013年FDA批准
- [Rosin 2011](papers/neuromodulation/rosin-2011-closed-loop-dbs-superior.md) — 首次证明闭环DBS优于开环DBS，用更少刺激获得更大改善
- [Little 2013](papers/neuromodulation/little-2013-adaptive-dbs-human.md) — 首次人类闭环自适应DBS，用beta振荡作为生物标志物，刺激量减半
- [Scangos 2021](papers/neuromodulation/scangos-2021-closed-loop-depression.md) — 首次个性化闭环神经调控治疗难治性抑郁症
- [Shirvalkar 2023](papers/neuromodulation/shirvalkar-2023-chronic-pain-biomarker.md) — 首次从颅内慢性记录预测慢性疼痛状态，OFC为关键生物标志物
- [Liu 2026](papers/neuromodulation/liu-2026-device-accelerometry-adbs.md) — 首个在大规模人体慢性数据(11 名 PD，>1900h，Summit RC+S)系统指出 aDBS 经典标志物 STN beta 的两个独立失效：关刺激时"总 beta"混叠周期(↑)/非周期(↓)、开刺激后周期 beta 与症状解耦；提出植入器自带加速度计作抗刺激的行为学标志物(解码 Acc R≈0.49/0.56 > 全神经 0.44/0.47)，推进 little-2013 的 beta-aDBS 范式(bioRxiv)

### 刺激空间选择性 / 电流聚焦 (current steering & field shaping)
"用电流几何/时空结构而非移动电极来控制激活区"这条母题，服务 SCS / DBS / 外周刺激；为本期 ACM(焦点式深部刺激)的纵向前作与横向对照。milestone 抽取自 Liang et al. 2023 (Neuromodulation) 的 SCS 计算模型系统综述。
- [Rattay 1986](papers/neuromodulation/rattay-1986-activating-function.md) — "激活函数"(∂²Ve/∂x²)：从胞外电场预测哪段轴突被激活的数学地基，所有刺激空间选择性建模的理论源头
- [Coburn 1980](papers/neuromodulation/coburn-1980-2d-scs-fem.md) — 首个 SCS 有限元模型(2D)，奠定"背柱 vs 背根谁先被激活"建模问题，SCS 建模线起点
- [Struijk & Holsheimer 1996](papers/neuromodulation/struijk-holsheimer-1996-transverse-tripole.md) — 横向三极双通道：靠多触点电流配比把激活区横向 steering，临床 current-steering 奠基理论
- [Capogrosso 2013](papers/neuromodulation/capogrosso-2013-epidural-stim-model.md) — 首个真实 3D 硬膜外 SCS 模型，证明优先募集背根 afferent，靶向时空刺激(Wagner/Lorach)的建模引擎
- [Rowald 2022](papers/neuromodulation/rowald-2022-spatiotemporal-epidural.md) — MRI 个体化 + 软件电流 steering 靶向躯干/腿运动池，完全 SCI 患者 1 天内恢复站立行走，临床级 current-steering 标杆(人体)
- [Grossman 2017](papers/neuromodulation/grossman-2017-temporal-interference.md) — 时间干涉(TI)：两路高频场深部干涉出低频包络，表面电极聚焦激活深部、放过浅层，ACM"深部聚焦"概念近亲(小鼠)
- [Stoney 1968](papers/neuromodulation/stoney-1968-current-distance-relationship.md) — 刺激侧基本定律：阈值随距离**平方**增长 I_th(r)=I₀+k·r²，10 µA 约激活 85 µm 内(猕猴运动皮层)。与记录的被动衰减分属两套物理——刺激半径可由电流调
- [Histed 2009](papers/neuromodulation/histed-2009-sparse-distributed-activation.md) — 双光子直接观察(小鼠)：微刺激激活的是**稀疏、分布很广**、有时远在毫米外的神经元，机制是直接激活**轴突/过路纤维**而非旁边胞体。改写刺激的空间图景

### 经颅振荡干预 / 非侵入夹带 (transcranial oscillation entrainment)
"用外加弱电磁场夹带内源节律、把振荡从相关性推到因果性"这条线，服务 tACS / kTMP 等非侵入调控。核心张力恒定：**脑内场强够不够**。milestone 抽取自 Wischnewski et al. (2023, Prog Neurobiol; PMC8909135) 的 tACS 机制综述 + 各源头论文回溯。建于 2026-07-20。
- [Terzuolo & Bullock 1956](papers/neuromodulation/terzuolo-bullock-1956-imposed-voltage-gradient.md) — 弱胞外电压梯度可改变神经元放电节律的最早定量测量，全部经颅电磁调控的物理起点(无脊椎动物)
- [Deans 2007](papers/neuromodulation/deans-2007-ac-field-sensitivity.md) — 定量拆开单细胞 vs 网络敏感度：DC 场 0.18 mV per V/m；50 Hz、1 V/m 峰峰值改变放电时相(71% 脑片)，对应胞体仅约 **70 µV**、低于膜电位噪声——网络的涌现性质比单神经元更敏感(大鼠脑片)
- [Fröhlich & McCormick 2010](papers/neuromodulation/frohlich-mccormick-2010-endogenous-fields.md) — 把内源电场从"副产物"改判为可能引导皮层活动的因素；实时正/负反馈电场直接证出活动↔电场的闭环(离体新皮层)
- [Ozen 2010](papers/neuromodulation/ozen-2010-tes-entrains-cortical-populations.md) — 首次在完整在体脑测到经颅电刺激夹带神经元：**1 mV/mm** 即足以相位偏置放电；且夹带比例依赖行为状态(大鼠，Buzsáki 组)
- [Reato 2010](papers/neuromodulation/reato-2010-low-intensity-stimulation.md) — "弱场→相干微小扰动→网络动力学放大"机制，胞内验证 **0.2 V/m** 处的相位夹带共振；把效应量问题改写成"取决于网络动力学状态"(大鼠脑片+模型)
- [Antal 2008](papers/neuromodulation/antal-2008-tacs-weak-aftereffects.md) — tACS 影响人类运动学习的最早报告(仅 10 Hz 显著)，同时诚实划出局限：常规参数下对皮层兴奋性的后效明显弱于 tDCS，MEP/EEG 均无显著改变(人类 N=50)
- [Zaehle 2010](papers/neuromodulation/zaehle-2010-tacs-enhances-alpha.md) — tACS 与人脑内源振荡相互作用的**首个直接电生理证据**(枕叶个体 alpha 功率上升)，确立 entrainment 与 STDP 两条机制路线(人类 N=10)
- [Pogosyan 2009](papers/neuromodulation/pogosyan-2009-beta-tacs-slows-movement.md) — 20 Hz tACS 减慢自主运动：**健康人身上振荡↔运动行为因果关系的首个直接证据**。判断新颖度的关键基准——人类 beta 因果证据 2009 年即存在(人类，Peter Brown 组)
- [Wischnewski 2019](papers/neuromodulation/wischnewski-2019-nmda-beta-tacs.md) — 20 Hz beta tACS 后效持续 ≥60 分钟，被 NMDA 拮抗剂完全消除；证出 tACS 可诱导 NMDA 介导的可塑性，把机制从"刺激期夹带"扩展到"刺激后可塑性"(人类)
- [Vöröslakos 2018](papers/neuromodulation/voroslakos-2018-direct-effects-tes.md) — **本线最具批判性的一篇**：人体尸体脑颅内直测，头皮电流约 **75%** 被衰减、需 ≥**1 mV/mm** 才影响放电、要在脑内产生 1 V/m 约需头皮 **6 mA**(远高于常规 1–2 mA)。把"场强不足"从顾虑变成有数字的硬约束(大鼠+人体尸体，Buzsáki/Berényi)
- [Krause 2019](papers/neuromodulation/krause-2019-tacs-entrains-primate-neurons.md) — 人体常规参数 tACS 在猕猴深部结构测得 0.28/0.35 V/m，稳定影响放电**时刻**而不改变放电**率**；把 tACS 的作用形式收窄为调时序(猕猴 N=2)
- [Johnson 2020](papers/neuromodulation/johnson-2020-dose-dependent-tacs-spike-timing.md) — 清醒猕猴单神经元记录测出**剂量依赖**夹带，并归纳出两类响应(burst 性增加 / 相位夹带)；剂量-反应是走向可控协议的前提(猕猴)
- [Labruna 2025](papers/neuromodulation/labruna-2025-ktmp-method.md) — kTMP 方法学奠基：改用**磁感应**产生连续千赫兹窄带电场绕开头皮电流瓶颈，10 分钟在 M1 诱导约 **2.0 V/m**、提升皮层兴奋性且几乎无体感(仅听觉音调，便于双盲)；诚实报告 AM 相对非调制无额外增益(人类，Ivry/Peterchev，eLife)

### 经颅超声神经调控 (transcranial ultrasound stimulation, TUS/tFUS)
"用聚焦声波无创调控神经活动"这条线。相对经颅电磁刺激的卖点是**深部可及 + 毫米级聚焦**（TMS 打不深、tES 场强被头皮分流）。这条线的历史张力与 tACS 那条完全不同：**tACS 争的是"脑内场强够不够"，TUS 争的是"测到的效应到底是不是超声直接作用"**——2018 年两篇 Neuron 指出啮齿类的超声诱发反应可由**间接听觉通路**解释，此后听觉掩蔽/致聋/包络平滑成为必须的对照。**评估任何新的 TUS 工作，先过三关：① 有没有听觉对照（掩蔽或致聋或平滑包络）；② 有没有报告脑内原位剂量估计与声学仿真靶点验证（ITRUSST 六类参数）；③ 读数是不是 MEP/SEP 这类个体内外波动大的量、样本量够不够。** 三关不过的阳性结果要打折扣，三关都过的阴性结果要认真对待。milestone 抽取自 Sarica et al. (2022, Brain Stimul) 人体系统综述 + 一篇 2025 年 tFUS 运动感觉系统统合综述(PMC12664190)，各源头论文逐篇回溯 PubMed 核实卷期页。建于 2026-08-05。
- [Fry 1958](papers/neuromodulation/fry-1958-reversible-cns-changes-ultrasound.md) — 整条线的起点：**猫**外侧膝状体核照射 20–120 秒，视皮层诱发电位初级响应降到不足 1/3、次级响应几近归零，**30 分钟完全恢复**、无组织学病灶。两个限制正是此后七十年的题目——**必须去掉颅骨**、作用位点未知(Science)
- [Tyler 2008](papers/neuromodulation/tyler-2008-remote-excitation-ultrasound.md) — 现代起点之一：小鼠海马脑片/离体全脑，低强度低频超声经**电压门控 Na⁺/Ca²⁺ 通道**兴奋神经元并触发 SNARE 介导的突触传递。离体标本没有听觉外周，故机制结论不能直接外推到在体经颅(PLoS ONE)
- [Tufail 2010](papers/neuromodulation/tufail-2010-transcranial-pulsed-ultrasound.md) — 推到**在体 + 经颅 + 有行为输出**(小鼠运动皮层引出运动、深部激活完整海马)；给出最常被引的两个数：横向分辨率约 **2 mm**、温升 **<0.01 °C**(即非热机制)、TTX 敏感。但其运动读数正是 2018 年听觉混淆争议的核心(Neuron)
- [Yoo 2011](papers/neuromodulation/yoo-2011-region-specific-modulation-fmri.md) — 兔 + MRI 引导 + fMRI 读数，确立三个此后成标配的动作：影像引导靶向、影像读数、**"效应双向"框架**(同一技术既可兴奋也可抑制，方向取决于参数)；组织学无损伤(NeuroImage)
- [King 2013](papers/neuromodulation/king-2013-effective-parameters.md) — 第一份定量剂量—反应规则(小鼠)：成功率随声强与时长上升、暗示 **50–150 ms 的幅度积分窗**、运动反应呈**全或无**(只改概率不改强度)；反直觉的一条是**连续波不比脉冲差**(Butts Pauly 组·Stanford)
- [Deffieux 2013](papers/neuromodulation/deffieux-2013-monkey-visuomotor.md) — **首次在清醒非人灵长类因果调制行为**：2 只猕猴反扫视潜伏期被显著改变且依赖刺激半场，把这条线从"引出肌肉抽动"推到"干预有认知内容的任务"(Curr Biol)
- [Legon 2014](papers/neuromodulation/legon-2014-human-s1-tfus.md) — **人体 TUS 开篇**：打 S1 衰减 SEP 幅度、改变诱发振荡频谱、提升感觉辨别；最承重的是空间对照——**焦点前后移 1 cm 效应即消失**。确立 SEP/MEP 读数 + 焦点位移对照两个标准动作(Nat Neurosci)
- [Kubanek 2016](papers/neuromodulation/kubanek-2016-ion-channel-currents.md) — 机械→电转换的单通道直接证据：爪蟾卵母细胞表达 K2P(TREK-1/TREK-2/TRAAK)与 NaV1.5，超声调制电流**平均最高约 23%**、加阻断剂即消失；提出 **sonogenetics**。注意频率 10 MHz 远高于经颅常用的 0.2–0.7 MHz(Sci Rep)
- [Sato 2018](papers/neuromodulation/sato-2018-indirect-auditory-mechanism.md) — **方法学地震(一)**：小鼠宽场钙成像看到的激活图样符合**间接听觉通路**而非焦点处直接调控，与可听声引发的图样相似、都像惊跳反射，**化学致聋后双双减弱**(Neuron)
- [Guo 2018](papers/neuromodulation/guo-2018-cochlear-pathway.md) — **方法学地震(二)**，同期同刊独立验证：豚鼠电生理测得广泛激活，**切断听神经或去除耳蜗液后激活消失**，指认**耳蜗通路**。不同物种/技术/干预的双重独立验证，是该问题被迅速接受的原因(Neuron)
- [Legon 2018](papers/neuromodulation/legon-2018-human-thalamus.md) — 人体**深部靶点**第一份系统证据(N=40)：打感觉丘脑抑制 **P14** 成分(发生源在 VPL，故能把效应定位到丘脑)；同时把 **CT+MRI 个体颅骨声学建模**推成标准动作(Hum Brain Mapp)
- [Mohammadjavadi 2019](papers/neuromodulation/mohammadjavadi-2019-auditory-elimination.md) — **关键反驳与修正**：混淆的物理来源是**矩形包络的陡边沿**；平滑边沿即可消除听觉反应而**不影响运动反应**，遗传性耳聋小鼠上运动反应仍在。把争论精确化成可操作的工程问题(Brain Stimul)
- [Verhagen 2019](papers/neuromodulation/verhagen-2019-offline-primate.md) — **离线效应范式**：猕猴 **40 秒刺激 → 效应持续 >1 小时**，被刺激区与全脑的相互作用变得更选择性，SMA/FPC 各自可分离；诚实报告两点——**脑膜腔室也有信号变化**、效应暂时且无微结构改变(eLife)
- [Folloni 2019](papers/neuromodulation/folloni-2019-deep-primate.md) — 猕猴**杏仁核与 ACC**：这两个深部靶点是现有可逆干预最难触及的，TUS 后它们与互联区的相关性专门减弱、效应局灶可分离，且明确排除听觉混淆解释(Neuron)
- [Braun 2020](papers/neuromodulation/braun-2020-auditory-confound-masking.md) — 把听觉混淆搬到**人**并给出解法：18 名被试**能听见 TUS、能区分有无刺激试次**(即未掩蔽的人体实验做不到盲)；经耳机播放掩蔽音后辨别率降到随机、听觉 EEG 成分消失(Brain Stimul)
- [Fomenko 2020](papers/neuromodulation/fomenko-2020-parameter-systematic-human.md) — 人体侧最完整的**参数—效应图谱**(N=16，TUS 与 TMS 线圈耦合)：**更长声照时长 + 更短占空比 → 抑制更强**，且增强 GABA_A 介导的 SICI；诚实报告行为效应在加近体感阈主动对照后不再成立(eLife)
- [Zeng 2022](papers/neuromodulation/zeng-2022-theta-burst-tus.md) — 人体**可塑性诱导**：80 秒 theta burst 图样 TUS → 皮质脊髓兴奋性升高 **≥30 分钟**，而**等声照时长的规则图样与伪刺激均无变化**——承重变量是时间图样而非总能量；打枕叶不影响 M1(Ann Neurol)
- [Mohammadjavadi 2022](papers/neuromodulation/mohammadjavadi-2022-sheep-lgn-vep.md) — **大动物这一格**：绵羊(n=9)MRI 引导打 LGN，视觉诱发电位 N70/P100 峰峰幅度**可逆抑制**；用 **MR-ARFI** 实测声致微位移并证明**位移大小与抑制程度相关**——这条线少见的声学剂量↔神经效应定量对应。是 [[scott-2026-tus-human-lgn-null]] 的**同实验室同靶点同读数纵向前作**(Sci Rep)
- [Martin 2025](papers/neuromodulation/martin-2025-256-element-human-lgn.md) — 人体深部 TUS 的**硬件代际更新**：256 阵元头盔式相控阵(555 kHz)+ 立体定向 + 个体化规划 + 实时 fMRI 监测，打人 **LGN** 使视皮层活动显著升高且跨个体可重复；theta burst 方案后效**≥40 分钟**，对照证实靶点特异。是 [[scott-2026-tus-human-lgn-null]] 最关键的**横向对照**(Oxford·Treeby/Stagg，Nat Commun)
- [Scott 2026](papers/neuromodulation/scott-2026-tus-human-lgn-null.md) — 这条线**第一份「三关全过」的人体阴性结果**:25 人打左侧 LGN、逐试次随机三档 PRF(4.875/48.75/487.5 Hz,脉冲 20.5/2.05/0.205 ms,占空比 10%,原位 ISPPA 16.2±3.6 W/cm²),SSVEP 幅度/潜伏期/知觉行为**三个读数均未检出效应**,靶向精度与活动变化无相关。四项设计创新(频率标记与 PRF 谐波不重叠、同侧未受声半视野作内部对照、**改焦点深度 70→30 mm 而非关机**、白噪声掩蔽实现双盲)使它难以被「漏了某个对照」解释掉;检出力下限 f≥0.264,焦点峰值略偏浅、两名被试未重合。**必须与 [[fry-1958-reversible-cns-changes-ultrasound]]（猫·去颅骨）、[[mohammadjavadi-2022-sheep-lgn-vep]]（同实验室·绵羊·阳性）、[[martin-2025-256-element-human-lgn]]（人·256阵元·阳性）并读**(UCSF×Stanford,bioRxiv)
- [Sarica 2022](papers/neuromodulation/sarica-2022-human-tus-systematic-review.md) — 人体侧**基准盘点**(截至 2022-01)：35 项研究、**677 名被试**，无严重不良反应，轻度症状 **3.4%(14/425)**；效应呈参数依赖，作者定性为"仍处早期阶段"。引用现状时注意时间戳与分母(Brain Stimul)
- [Martin 2024](papers/neuromodulation/martin-2024-itrusst-reporting-standards.md) — ITRUSST **报告标准**：六类必报参数(换能器/驱动设置/自由场声学/脉冲时序/**脑内原位暴露估计**/强度)。承认领域分歧有相当部分源于"说不清到底打了多少剂量到脑内哪里"(Brain Stimul)
- [Aubry 2025](papers/neuromodulation/aubry-2025-itrusst-biophysical-safety.md) — ITRUSST **安全阈值**：机械指数 MI/MI_tc **≤1.9**；热效应满足任一即可——峰值温升 **≤2 °C** 或绝对温度 **≤39 °C**、或热剂量脑 **2 CEM43**/骨 16/皮肤 21、或给定时长的 TI 取值。明确声明共识 ≠ 标准 ≠ 监管(Brain Stimul)

## optical-bci (9 papers)
光学脑机接口：用钙成像(而非电极)读出神经活动来驱动闭环解码。相对电生理 BCI 的独有能力是**知道每个参与细胞的身份、层次、类型与空间位置**，因而既是工程路线也是研究工具；代价是钙信号相对动作电位的时间分辨率与信噪比。milestone 抽取自 Hira R. (2024, Neurophotonics 11:033405) 的多光子闭环/BMI 综述。建于 2026-07-20。
- [Fetz 1969](papers/optical-bci/fetz-1969-operant-conditioning-cortical-units.md) — BCI 的思想原点：猕猴经操作性条件反射把**新分离**单神经元的放电提高到基线 **50%–500%**，证明神经活动可被任意调控、不必绑定自然运动输出。本线全部工作沿用这套范式、只把电极换成光学记录(猕猴)
- [Ghosh 2011](papers/optical-bci/ghosh-2011-miniaturized-fluorescence-microscope.md) — miniscope 硬件起点：**1.9 g** 集成荧光显微镜，自由活动小鼠上约 0.5 mm² 视野同时追踪 >200 个浦肯野细胞。单光子宽场是其可及性来源，也带来先天代价——离焦背景荧光(小鼠，Schnitzer 组)
- [Ziv 2013](papers/optical-bci/ziv-2013-long-term-place-codes.md) — 表征漂移的奠基观察：跨周追踪同一批 CA1 细胞，每天参与表征的是不同子集、任两天仅重叠 **15–25%**，但重叠部分保持位置野即足以维持准确空间表征。对 BCI 的含义是解码基底本身在换人(小鼠)
- [Clancy 2014](papers/optical-bci/clancy-2014-optical-neuroprosthetic-learning.md) — **首个双光子钙成像 BMI**，开创光学 BCI 线：小鼠用 2/3 层神经元活动差控制听觉光标，学习伴随空间局部化网络的精细放电相关性改变(小鼠，Carmena 组)
- [Hira 2014](papers/optical-bci/hira-2014-single-neuron-operant-conditioning.md) — 强化推到**单神经元**：15 分钟内提高目标神经元活动而不改变前肢运动；非目标神经元受双向调制，方向由奖励与活动的**相对时刻**决定、**与空间距离无关**(小鼠)
- [Mitani 2018](papers/optical-bci/mitani-2018-inhibitory-neuron-bci.md) — 首次把**细胞类型**作为 BCI 自变量：PV/SOM/VIP 三类中间神经元都能学会，但策略亚型特异(PV 压低 N−，SOM/VIP 抬高 N+)。电极分不清这三类(小鼠，Komiyama 组)
- [Zhang 2018](papers/optical-bci/zhang-2018-closed-loop-all-optical.md) — 闭环**全光学**：成像在线读出 + 双光子光遗传实时定制写入，行为进行中操纵回路。对应电生理双向接口的光学版本，但精度到单细胞(小鼠，Häusser 组)
- [Trautmann 2021](papers/optical-bci/trautmann-2021-optical-bci-macaque.md) — 光学 BCI 推进到**非人灵长类**：胞体因光子散射不可及，改成像顶树突接入 PMd/M1，在线解码运动方向；CLARITY 回溯确认许多树突来自第 5 层输出神经元(含疑似 Betz 细胞)(猕猴，Shenoy/Deisseroth 组)
- [Abdeladim 2026](papers/optical-bci/abdeladim-2026-holographic-mesoscope.md) — 把 [[zhang-2018-closed-loop-all-optical]] 的全光学读写从**单视野推到跨脑区**(Nat Neurosci 29:2023–2035)。解法是**两级寻址**：SLM 可及范围(约 950×990 µm，接近该放大倍率理论极限)尺寸不变，加一对振镜(±9°→样品面 ±1.4 mm)把它整体平移，视野切成 81 个 350 µm 格；光刺激视野达 **3.2×3.2 mm²**，约为此前十倍。绕开"做更大 SLM"(更大偏折角需更细像素，代价是衍射效率下降+像素串扰)。实测 PPSF 横向 **23–38 µm**、轴向 **35–77 µm**，目标细胞 **70%** 显著响应。两个承重结果：①**跨区可解**——刺激 LM，完全排除 LM 区后仅用其他视区仍解出写入的是哪一组，**0.65±0.02**(随机 0.5)；②**符号翻转**——同一次扰动 follower cells 净影响本地 **−0.19±0.02**、下游 **+0.1±0.01**(P=4.97×10⁻²⁶)。**本地净抑制属确证([[chettih-2019]] 等)，新的是两者能同批试次同时测出**。边界：结论依赖 follower cells 界定、朝向传递效应量小(0.271 vs 0.243, P=0.04)、"首台"措辞正刊已收窄(小鼠，Adesnik 组·UC Berkeley)

## locomotion (6 papers)
- [Harkema 2011](papers/locomotion/harkema-2011-epidural-stimulation-standing.md) — 首次硬膜外脊髓刺激恢复完全瘫痪者站立和步进，颠覆不可恢复教条
- [King 2015](papers/locomotion/king-2015-eeg-bci-overground-walking.md) — 首次EEG-BCI驱动FES实现截瘫者地面行走
- [Donati 2016](papers/locomotion/donati-2016-bmi-neurological-recovery.md) — Walk Again Project：BMI步态训练诱导慢性SCI部分神经恢复
- [Capogrosso 2016](papers/locomotion/capogrosso-2016-brain-spine-interface-primate.md) — 首个脑-脊髓接口恢复灵长类瘫痪肢体行走
- [Wagner 2018](papers/locomotion/wagner-2018-targeted-epidural-walking.md) — 靶向时空硬膜外刺激恢复人类SCI患者行走
- [Lorach 2023](papers/locomotion/lorach-2023-brain-spine-interface-human.md) — 首个人类脑-脊髓接口实现自然行走，稳定运行>1年

## rehabilitation (5 papers)
- [Daly 2008](papers/rehabilitation/daly-2008-bci-neurorehabilitation-review.md) — 定义BCI作为康复工具（非辅助设备）的理论框架，Lancet Neurology
- [Ramos-Murguialday 2013](papers/rehabilitation/ramos-murguialday-2013-bci-stroke-controlled-trial.md) — 首个BCI卒中康复对照试验，证明闭环时间锁定是驱动神经可塑性的关键
- [Ang 2015](papers/rehabilitation/ang-2015-bci-robot-stroke-rct.md) — RCT验证BCI+康复机器人对卒中康复有效，扩展BCI康复执行器选择
- [Frolov 2017](papers/rehabilitation/frolov-2017-bci-exoskeleton-multicenter-rct.md) — 最大规模BCI康复多中心RCT（74人），证明跨机构推广可行性
- [Biasiucci 2018](papers/rehabilitation/biasiucci-2018-bci-fes-lasting-recovery.md) — BCI-FES康复效果持续6-12个月，EEG连接变化为神经可塑性客观证据

## clinical-regulatory (12 papers)
- [Huggins 2011](papers/clinical-regulatory/huggins-2011-bci-user-needs.md) — 首次系统调查BCI用户需求，定义准确率≥90%、速度≥15字母/分钟等临床标准
- [Yuste 2017](papers/clinical-regulatory/yuste-2017-four-ethical-priorities.md) — Nature评论：四大神经伦理优先领域，催生NeuroRights Foundation
- [Ienca 2017](papers/clinical-regulatory/ienca-2017-neurorights-framework.md) — 系统提出四项神经权利（认知自由、心理隐私、心理完整性、心理连续性）
- [Chile 2021](papers/clinical-regulatory/chile-2021-neurorights-constitution.md) — 全球首个将神经权利写入宪法的国家，2023年最高法院首个司法判例
- [Oxley 2023](papers/clinical-regulatory/oxley-2023-switch-trial-safety.md) — Synchron SWITCH试验：首个血管内BCI人体安全数据，JAMA Neurology
- [Rubin 2023](papers/clinical-regulatory/rubin-2023-braingate-safety-profile.md) — BrainGate 14人×17年安全数据，安全性与已批准DBS相当，Neurology
- [Synchron 2024](papers/clinical-regulatory/synchron-2024-command-feasibility.md) — COMMAND：首个FDA IDE永久植入BCI研究，6/6安全终点达标
- [Mokienko 2024](papers/clinical-regulatory/mokienko-2024-intracortical-implants-review.md) — 皮层内植入式BCI综述来源，梳理运动控制、电脑/平板、文本输入、语音恢复等临床能力演进；用于 Paradromics/Connexus 补库的抽取基准
- [Precision 2025](papers/clinical-regulatory/precision-2025-layer7-510k.md) — FDA K242618：Layer 7-T皮层电极/BCI组件获传统510(k) clearance（Class II, product code GYC），边界是短期皮层记录/刺激工具而非永久植入通信系统PMA
- [Neuracle/NEO 2026](papers/clinical-regulatory/neuracle-2026-neo-nmpa-approval.md) — 中国NMPA批准博睿康NEO硬膜外BCI手部运动功能代偿系统上市；公开中文来源支持"获批上市的植入式BCI三类医疗器械"框架，注册证编号/医保范围仍需继续核
- [Paradromics 2026](papers/clinical-regulatory/paradromics-2026-connect-one-first-implant.md) — Connect-One 早期可行性研究首例长期 Connexus 植入(报道称 FDA IDE、随访最长6年)，高密度皮层内全植入 BCI 进入 speech restoration 临床分支
- [Przepiorka 2025](papers/clinical-regulatory/przepiorka-2025-dural-tenting-rct.md) — 490 例多中心 RCT：择期幕上开颅**省略预防性硬膜悬吊线非劣**（因血肿再手术 0.8% vs 0.4%）。沿用数十年的标准步骤被首次随机检验

## ai-neural-modeling (22 papers)
- [Pandarinath 2018](papers/ai-neural-modeling/pandarinath-2018-lfads.md) — LFADS序列VAE，从spikes中恢复single-trial潜在动力学，Nature Methods
- [Ye 2021](papers/ai-neural-modeling/ye-2021-neural-data-transformer.md) — NDT首次将Transformer应用于神经spike数据，推理速度比RNN快6倍
- [Ye 2023](papers/ai-neural-modeling/ye-2023-ndt2-multi-context.md) — NDT-2跨session预训练，证明预训练+微调范式在神经数据上有效，NeurIPS 2023
- [Azabou 2024](papers/ai-neural-modeling/azabou-2024-mtm-universal-translator.md) — MtM三维度掩码自监督，跨脑区跨细胞类型联合建模，NeurIPS 2024
- [Azabou 2023](papers/ai-neural-modeling/azabou-2023-poyo.md) — **POYO**：把单个动作电位当 token（神经元嵌入 + 发放时刻）+ cross-attention/PerceiverIO 主干，解掉"跨 session 神经元无对应"的结构性障碍；7 只非人灵长类 / 158+ session / 27,373+ 单元 / 100+ 小时，可 few-shot 适配对应未知的新 session。是 [[azabou-2024-mtm-universal-translator]] 与 [[azabou-2025-poyo-plus]] 的 tokenization 源头
- [Azabou 2025](papers/ai-neural-modeling/azabou-2025-poyo-plus.md) — POYO+ 多 session 多任务 foundation model；tokenization 沿用 POYO(2023)：每个 token = 神经元嵌入 + 时间，摆脱"输入维度=神经元个数"的锁死，迁移新 session 只需学新单元嵌入。训练于 Allen Brain Observatory **双光子钙成像**(>10 万神经元/6 脑区，非 spike)，故增设幅值投影层；ICLR 2025。属 stitching 路线，增益来自结构假设+锚点
- [Defossez 2023](papers/ai-neural-modeling/defossez-2023-meta-meg-speech.md) — Meta FAIR对比学习将MEG映射到wav2vec表征空间，非侵入语音解码新范式
- [Yang 2023](papers/ai-neural-modeling/yang-2023-biot-biosignal-transformer.md) — BIOT：首个跨数据集生物信号基础模型(EEG+ECG+体动)，patch tokenization+masked自监督，NeurIPS 2023
- [Jiang 2024](papers/ai-neural-modeling/jiang-2024-labram-large-brain-model.md) — LaBraM：首个大规模EEG基础模型，2500h/20数据集VQ频谱预训练，跨任务微调全超SOTA，ICLR 2024 Spotlight
- [Liu 2026](papers/ai-neural-modeling/liu-2026-eeg-fm-benchmark.md) — EEG-FM首次系统评测：12个开源FM×13数据集×9范式；larger≠better，专家模型仍有竞争力，指明数据瓶颈
- [Aristimunha 2026](papers/ai-neural-modeling/aristimunha-2026-eegdash-open-data-platform.md) — EEGDash：791公开数据集/五模态/86k小时做成零代码可训练；审计揭示"合规≠可用"(ρ=−0.05)，脑电基础模型缺的数据基础设施一环

### 神经解码→图像/语言重建 (visual & language reconstruction line)
- [Miyawaki 2008](papers/ai-neural-modeling/miyawaki-2008-visual-image-reconstruction.md) — 首次从fMRI重建所见图像本身(多尺度局部解码器拼10×10对比图案)，开"看图重建"先河(人类)
- [Horikawa 2017](papers/ai-neural-modeling/horikawa-2017-generic-decoding-dnn-features.md) — generic decoding：解码层级DNN特征泛化到训练外类别，看到的与想象的都可解；"神经→预训练网络特征空间"范式祖先(人类fMRI)
- [Shen 2019](papers/ai-neural-modeling/shen-2019-deep-image-reconstruction.md) — 端到端深度图像重建：优化图像逼近解码DNN特征+自然图像生成先验，确立"神经→特征→生成"三段式(人类fMRI)
- [Ozcelik 2023](papers/ai-neural-modeling/ozcelik-2023-latent-diffusion-scene-reconstruction.md) — 潜在扩散做自然场景重建，"低层潜在+CLIP语义"双路条件，NSD基准(人类fMRI)
- [Takagi 2023](papers/ai-neural-modeling/takagi-2023-stable-diffusion-reconstruction.md) — 仅线性映射+现成Stable Diffusion做高分辨率重建，扩散era标志性极简路线(人类fMRI)
- [Scotti 2023 (MindEye)](papers/ai-neural-modeling/scotti-2023-mindeye-fmri-to-image.md) — 对比学习+扩散先验把fMRI对齐CLIP，刷新fMRI-to-image SOTA；"对齐"为核心训练目标(人类fMRI)
- [Tang 2023 (Huth)](papers/ai-neural-modeling/tang-2023-semantic-language-reconstruction.md) — 首次非侵入(fMRI)语义重建连续语言(gist非逐字)，神经→语言祖先，提出mental privacy(人类fMRI)
- [Ferrante 2023 (Brain Captioning)](papers/ai-neural-modeling/ferrante-2023-brain-captioning.md) — 把脑活动解码成图像+文本caption，NEURRATOR"自然语言旁白"最直接祖先(人类fMRI；与候选2 Toschi同线)
- [Marin-Llobet 2026 (NEURRATOR)](papers/ai-neural-modeling/marin-llobet-2026-neurrator-single-cell-narration.md) — 首次把"神经活动→自由文本旁白"推到单神经元级(小鼠Neuropixels)：动作电位→冻结CLIP→冻结LLaVA零语言端训练；同一画面PV/SST讲车、VIP讲光影，把细胞类型从分类目标变成可用语言查询的功能探针(76%认型)
- [Ciferri 2026 (Alignment not Complexity)](papers/ai-neural-modeling/ciferri-2026-alignment-not-complexity.md) — 受控对照证明 fMRI 解码"训练目标>架构深度"：线性+对比(CL)在图像/语言/音乐三模态全面胜过岭回归与非线性MLP；MSE最低(岭回归)反而检索最差，因对比只优化方向/几何对齐；线性化归因 Nozari&Bassett 2024(人类fMRI；与 [[ferrante-2023-brain-captioning]] 同组)
- [Ismail 2026 (naturalistic word meaning)](papers/ai-neural-modeling/ismail-2026-naturalistic-word-meaning.md) — 首次从**被动录的日常自然语音**(21患者/871h/527万词)估计**人类单神经元**对词义的编码：Behnke-Fried 微丝深部电极，全自动转录+区分说话人+检动作电位，无人工标注/分选；编码全患者显著、10类语义解码20.9%(随机10%)；自己说>环境语音2.42×(注意力)、自动化≈人工精标；把神经→语义从受控刺激推到零控制日常语音+百万词级(Baylor·Hayden/Sheth/Provenza，bioRxiv)

## brain-encoding-models (14 papers)
**预测脑活动本身**这一格——与全库其余子领域方向相反：那些是"从脑活动读出外界"（解码），本线是"给定外界或给定当前状态，预测脑活动会是什么"。建于 2026-08-04。本线分两条互不相同的研究纲领，评估任何新工作前先判定它落在哪一条：
- **A · 编码模型（刺激 → 脑响应）**：前向映射，问"给定这个刺激，各体素/电极响应多大"。milestone 抽取自 **Naselaris et al. (2011, NeuroImage 56:400–410)**。
- **B · 全脑动力学模型（当前状态 → 后续演化）**：时间演化，问"给定此刻的脑状态与连接结构，接下来怎么走"。milestone 抽取自 **Breakspear (2017, Nat Neurosci 20:340–352)**。

**四条硬约束，评估本线任何新工作时先过一遍：**
1. **必须在留出的、训练中未出现过的刺激上评估**，且优先看大候选集 identification 而非分类准确率（[[naselaris-2011-encoding-decoding-fmri]] 定的准则）。只报告训练分布内拟合度的工作，方法学上落后于 2008 年。
2. **"更大的模型/更多数据"本身能带来对数线性增益**（[[antonello-2023-scaling-laws-encoding]]：125M→30B 约 +15%）。一项新工作的增益若能被换更大骨干解释掉，就不构成方法学增量。
3. **B 线的两个零假设**：静息态慢波动可由连接组+传导延迟+噪声直接产生（[[deco-2009-coupling-delay-noise]]）；"结构决定功能"在长时间窗成立、短时间窗大量动态无法由结构解释（[[honey-2007-network-structure-shapes-fc]]）。任何赋予自发活动功能意义的说法都需先排除这两条。
4. **自称"因果"要核它的因果性来自哪里**——来自实验操纵 + 生成模型反演（[[friston-2003-dynamic-causal-modelling]]），还是仅来自时序上的先后（后者不构成因果）。

### A · 编码模型线
- [Kay 2008](papers/brain-encoding-models/kay-2008-identifying-natural-images.md) — 路线起点(Nature 452:352–355)：对每个体素拟合 Gabor 感受野编码模型（空间位置/朝向/空间频率调谐），据此在大候选集中指认被试看的是**哪一张从未测量过的新自然图像**；性能超过只用视网膜拓扑的模型，说明空间调谐不足以解释。把 fMRI 解码从"已知类别选一"推进到"对未见刺激泛化"(人类)
- [Naselaris 2011](papers/brain-encoding-models/naselaris-2011-encoding-decoding-fmri.md) — **A 线 milestone 抽取源**(NeuroImage 56:400–410)：把编码与解码写进同一形式框架，论证编码模型**指定了完整前向生成过程、原则上可推出最优解码器**，而解码器不唯一确定编码模型，故编码模型更一般、可证伪性更强。确立三条评价准则：特征空间的选择即科学假设、必须在留出刺激上评估、identification 严于分类
- [Nishimoto 2011](papers/brain-encoding-models/nishimoto-2011-reconstructing-movies.md) — 把编码模型扩到**时间维度**(Curr Biol 21:1641–1646)：运动能量模型把"视觉快、BOLD 慢"这一错配显式拆成两级（时空 Gabor → 血流动力学卷积），配自然影片先验的贝叶斯解码器。百万量级候选片段中把刺激时刻定位在 **±1 秒内的比例 95%**。今日全部"自然主义刺激 + 编码模型"工作的问题设定源头(人类fMRI)
- [Yamins 2014](papers/brain-encoding-models/yamins-2014-performance-optimized-models.md) — 确立"**任务优化即模型搜索**"(PNAS 111:8619–8624)：不手工设计特征，改在物体识别任务上优化分层网络、取各层激活作特征空间。识别性能与单个 IT 单元预测力强相关；高性能网络输出层预测 IT、**中间层预测 V4**。此后语言/语音编码模型全部沿用此范式。**边界：层级对应是相关证据，不等于机制等同**(猕猴)
- [Schrimpf 2021](papers/brain-encoding-models/schrimpf-2021-neural-architecture-language.md) — 语言侧变成可比较的基准问题(PNAS 118:e2105646118)：**43 个**模型 × fMRI+ECoG+阅读时间统一评测；最好的 transformer 解释句子诱发响应中**接近 100% 的可解释方差**；**下一个词预测**能力（而非其他语言任务）预测神经与行为拟合；架构本身即有实质贡献。**引用须带"可解释方差"这一限定**(人类)
- [Caucheteux & King 2022](papers/brain-encoding-models/caucheteux-2022-brains-algorithms-converge.md) — 与 Schrimpf 2021 独立同结论(Commun Biol 5:134，**102 名**被试/400 句/fMRI+MEG)：脑-模型相似度主要取决于**从上下文预测词**的能力。两条独立证据链使该结论比任一单篇更可靠；MEG 把结论从"哪里像"扩到"什么时候像"。作者与 [[defossez-2023-meta-meg-speech]]、[[brain2qwerty-2026-meg-typing-decoding]] 同组(人类)
- [Antonello 2023](papers/brain-encoding-models/antonello-2023-scaling-laws-encoding.md) — 缩放规律(NeurIPS 2023)：脑预测性能随模型规模**对数线性**提升，OPT/LLaMA **125M→30B** 区间编码性能约 **+15%**；放大 fMRI 训练集规模有同样的对数线性行为；声学模型(HuBERT/WavLM/Whisper)提升幅度相当。**与 EEG 侧 [[liu-2026-eeg-fm-benchmark]] 的 "larger≠better" 形成对照——缩放行为不能跨模态假定**(人类fMRI，3被试)
- [Tuckute 2024](papers/brain-encoding-models/tuckute-2024-driving-suppressing-language-network.md) — 编码模型从"描述"变成"**控制**"(Nat Hum Behav 8:544–561)：先在 **1000 句**上拟合 GPT 类编码模型，再反用它挑出预测会最大化/最小化语言网络响应的新句子，在**新被试**身上实测兑现；**意外性与语言良构性**是响应强度的主要决定因素。**本线与 BCI 最接近的一格**——首次给 BCI 的输入侧（如何设计刺激驱动特定回路）提供可计算的设计工具(人类fMRI)

### B · 全脑动力学线
- [Wilson & Cowan 1972](papers/brain-encoding-models/wilson-cowan-1972-excitatory-inhibitory.md) — 神经质量模型奠基(Biophys J 12:1–24)：把局部皮层抽象成耦合的兴奋/抑制两群体，状态变量取**平均发放率**，群体输入-输出用 sigmoid。给出稳定不动点、迟滞与极限环振荡，为皮层节律提供群体层面解释。**注意术语**：此处"群体"指解剖邻近的局部群体，与 population-dynamics 子领域的"记录到的神经元群体状态空间"是不同概念
- [Jansen & Rit 1995](papers/brain-encoding-models/jansen-rit-1995-coupled-cortical-columns.md) — 把群体模型接到**可测观测量**(Biol Cybern 73:357–366)：皮层柱 = 锥体细胞群 + 兴奋性/抑制性中间神经元群，锥体群膜电位作 EEG 代理输出；同一模型在不同参数下既产生类 alpha 自发节律、又在脉冲输入下产生类视觉诱发电位波形。这一步使模型可被 EEG 数据证伪，是 DCM 的 EEG/MEG 版生成模型的直系祖先
- [Friston 2003](papers/brain-encoding-models/friston-2003-dynamic-causal-modelling.md) — **DCM**：生成模型 + 贝叶斯反演正式接合(NeuroImage 19:1273–1302)。参数分三组：外源输入对状态的影响、状态间内在耦合、允许输入**调制**耦合的双线性参数；由此把"有效连接"与"实验操纵引起的连接变化"变成可估计量。把 fMRI 实验重新理解为对脑区间整合过程的实验操纵
- [Honey 2007](papers/brain-encoding-models/honey-2007-network-structure-shapes-fc.md) — "结构决定功能"在**不同时间尺度上含义不同**(PNAS 104:10240–10245，猕猴连接组+仿真)：分钟级长窗功能网络与结构网络高度重合、枢纽对应；秒级出现两个反相关簇经前额/顶叶枢纽相连；百毫秒级为受解剖约束的锁相事件，并生成慢尺度上的功能连接。此后全脑模型的标准检验任务由此确立
- [Deco 2009](papers/brain-encoding-models/deco-2009-coupling-delay-noise.md) — 静息态波动的结构性零假设(PNAS 106:10302–10307)：**38 个**耦合振子、时延取自灵长类通路长度；时延耦合导致涌现两组 40 Hz 振子，网络响应性在传导速度 **1–2 m/s**、耦合接近下限时最优，并存在使网络出现**随机共振**的特征噪声尺度。把传导延迟与噪声正式确立为全脑模型不可省略的参数
- [Breakspear 2017](papers/brain-encoding-models/breakspear-2017-dynamic-models-review.md) — **B 线 milestone 抽取源**(Nat Neurosci 20:340–352)：梳理平均场/神经场/全脑网络三层与模型反演这一环。已被建模的现象：癫痫、脑病、睡眠、麻醉、静息态网络、人类 alpha 节律、多模态融合。明确本线与 A 线的分工——A 问"给定刺激脑活动是什么"，B 问"给定当前状态接下来怎么演化"

## population-dynamics (15 papers)
- [Sadtler 2014](papers/population-dynamics/sadtler-2014-neural-constraints-learning.md) — 流形内模式易学、流形外学不会，奠定"神经流形约束学习"范式（猴，皮层内BCI），Nature
- [Gallego 2017](papers/population-dynamics/gallego-2017-neural-manifolds-movement.md) — 定义性框架综述，确立neural manifold/neural modes作为群体运动控制的统一语言，Neuron
- [Golub 2018](papers/population-dynamics/golub-2018-learning-neural-reassociation.md) — 流形内学习机制=neural reassociation（重配已有模式而非生成新模式），Nat Neurosci
- [Oby 2019](papers/population-dynamics/oby-2019-new-activity-patterns-long-term.md) — 流形外经长期训练可长出新活动模式，定义"短期重配 vs 长期重塑"对照，PNAS
- [Gallego 2020](papers/population-dynamics/gallego-2020-long-term-stability-dynamics.md) — 低维潜在动力学跨~2年稳定（单神经元在换），BCI长期免校准的群体动力学基础，Nat Neurosci
- [Gallego 2018](papers/population-dynamics/gallego-2018-preserved-manifold-multiple-behaviors.md) — 多种运动行为共享同一被保留流形，证明流形是通用低维底座，Nat Commun
- [Busch 2025](papers/population-dynamics/busch-2025-human-noninvasive-manifold-bci.md) — bioRxiv：在人类无创(fMRI)验证流形约束学习；流形内ΔBrainControl +49.3/+16.4可学，流形外−0.4学不会(N=18)
- [de Vicente 2026](papers/population-dynamics/devicente-2026-circuit-specific-volitional-learning.md) — 首次把流形-BCI学习搬出运动皮层、进海马CA3并与M1对比：两区学得一样好(p=0.453 n.s.)但动力学分叉(M1流过/CA3折返)，RNN证差异源于环路架构→principled degeneracy，bioRxiv
- [Micou 2026](papers/population-dynamics/micou-2026-hippocampal-bmi-navigation.md) — 海马 CA1 闭环 BMI 导航:250-500 个 CA1 神经元实时解码推动 400 cm VR 轨道;旧跑轮地图直接接入 BMI 失效,重新训练后恢复;superposed 细胞 3.1%(586/18,902) 指向新旧位置地图并行叠加,bioRxiv
- [Rigotti 2013](papers/population-dynamics/rigotti-2013-mixed-selectivity.md) — 猕猴前额叶非线性混合选择性：消除单细胞对某变量的选择性后，该变量仍可从群体解出。「信息住在群体、不锁在单个神经元」的关键实证，也解释复杂认知为何高维
- [Ziv 2013](papers/population-dynamics/ziv-2013-hippocampal-place-code-drift.md) — 表征漂移硬实证(小鼠 CA1，长期钙成像)：同一熟悉环境每天换一批位置细胞，任意两天仅约 15–25% 重叠；但这一小撮稳定核心已足够维持数周空间表征
- [Stringer 2019](papers/population-dynamics/stringer-2019-high-dimensional-visual-cortex.md) — 小鼠 V1 对自然图像的群体响应高维，特征谱呈幂律(第 n 主成分方差 ∝ 1/n)，且是「保持编码平滑前提下维度尽可能高」的结果。高维是被优化到极限的设计
- [Degenhart 2020](papers/population-dynamics/degenhart-2020-bci-stabilization-alignment.md) — 无监督对齐稳定 BCI：把当天活动对齐回参考日的低维空间，**不需新标签**即维持性能。划清「漂移可救 / 物理包裹不可救」的界线
- [Li 2024](papers/population-dynamics/li-2024-behaviorally-relevant-dimensionality.md) — 分离行为相关信号(猕猴)：原始主子空间 26/64/45 维，**行为相关仅 7/13/9 维**。运动 BCI 冗余成立的定量基础。注意该文主张是「行为占据的空间比想象更高维」，勿简化引用
- [Manley 2024](papers/population-dynamics/manley-2024-unbounded-dimensionality-scaling.md) — 至多约 100 万神经元的皮层范围记录：**维度随神经元数持续增长、未见饱和**。给「低维」结论加上记录尺度这一限定条件

## performance-variability (8 papers)
BCI 性能变异性：认知状态/注意/信号状态。横跨非侵入(心理-注意因素)与皮层内(信号非平稳-神经状态)两支。
- [Vidaurre & Blankertz 2010](papers/performance-variability/vidaurre-2010-bci-illiteracy.md) — "BCI illiteracy"影响约15–30%使用者；提出协同自适应+在线自校准从机器侧解inefficiency，无需离线校准，把"用不了"重定义为"机器可适应"(EEG/SMR)
- [Grosse-Wentrup & Schölkopf 2013](papers/performance-variability/grosse-wentrup-2013-smr-bci-performance-variations.md) — SMR-BCI性能变异综述，把γ频段注意网络活动指认为同一被试内表现波动的关键神经相关物，将"注意"落到可测神经生理量
- [Perge 2013](papers/performance-variability/perge-2013-intraday-signal-instabilities.md) — 皮层内日内信号不稳定的奠基实证(人类3名四肢瘫，BrainGate)：84%单元日内放电率显著变化、85%为生理性、不稳定致56%评估出现方向性解码偏置
- [Jeunet 2015](papers/performance-variability/jeunet-2015-predicting-mi-bci-performance.md) — 首次系统证明用户稳定特质(空间能力+人格/动机)可预测MI-BCI表现，把性能变异从"随机噪声"推向"可测个体差异"(EEG)
- [Downey 2018](papers/performance-variability/downey-2018-intracortical-recording-stability.md) — 人类皮层内记录稳定性(2名长期使用者，Pitt/Chase·Collinger)：动作电位单元日内可变、波形特征可预测稳定性，把放电率漂移与神经状态变化关联(今日候选方法学前身)
- [Dunlap 2020](papers/performance-variability/dunlap-2020-intracortical-signal-disruptions-review.md) — 皮层内BMI信号中断的定义性综述：按影响时长×可补偿性提出四类框架(瞬时/可逆/不可逆可补偿/不可逆不可补偿)+各类补偿策略
- [Niu 2025](papers/performance-variability/niu-2025-cognitive-state-eeg-bci-review.md) — 最新定义性系统综述(PRISMA，25项)：年龄/认知/注意/心理状态对EEG-BCI有效性的影响；P300/SSVEP更鲁棒、MI对认知与年龄更敏感
- [Canario 2026](papers/performance-variability/canario-2026-attentional-load-ibci.md) — 极少数在人类皮层内BCI主动操纵注意负荷(双任务N-Back)的工作：负荷经EEG/准确率/自评确证抬高,但光标控制基本不掉、运动意图信号保住;最差(植入约8年的P2)成功率跌<10% vs EEG-BCI约20%;脆弱性跟信号质量/植入年限走而非分心本身(匹兹堡Chase·Collinger组,2名四肢瘫,Utah阵列)

## passive-bci (9 papers)
被动脑机接口 / 神经自适应(neuroadaptive)。把自发认知状态(错误感知/工作负荷/期望违背)当作隐式输入让机器适应,区别于把认知状态当噪声的 performance-variability、把情绪当对象的 affective-bci。抽取源=Zander & Kothe 2011(定义"passive BCI"三分类)。主线：框架→隐式信号机制(ErrP/ERN)→真实环境工作负荷→神经自适应闭环地标→操作环境部署。
- [Parra 2003](papers/passive-bci/parra-2003-response-error-correction.md) — 最早闭环之一：单试次检出错误相关负波(ERN)自动纠错,人机绩效平均+21%(人类EEG),Ferrez 2008 的前驱
- [Kohlmorgen 2007](papers/passive-bci/kohlmorgen-2007-workload-real-driving.md) — 真实道路驾驶中实时检测高心理负荷→即时削减车载信息流,最早走出实验室的工作负荷型 passive BCI 之一(人类EEG,MIT Press)
- [Ferrez & Millán 2008](papers/passive-bci/ferrez-2008-error-related-potentials.md) — 确立"交互错误电位(interaction ErrP,机器误解用户意图时诱发)",给出可复现波形+单试次检出,passive BCI 纠错的核心信号机制(人类EEG,IEEE TBME)
- [Zander & Kothe 2011](papers/passive-bci/zander-2011-passive-bci.md) — 定义框架(抽取源)：提出"passive BCI",把 BCI 分 active/reactive/passive,整条线的命名与概念原点(J Neural Eng,综述)
- [Zander 2016](papers/passive-bci/zander-2016-neuroadaptive-cursor.md) — 地标闭环：无任何显式指令,从 mPFC 单试次 ERP 解码"期望违背"(幅度线性对应)→机器自动把光标引向用户内心目标,"neuroadaptive"由此定名(人类EEG,PNAS)
- [Aricò 2016](papers/passive-bci/arico-2016-adaptive-automation-atc.md) — 走向部署：EEG 工作负荷指数触发自适应自动化,贴近真实空管(ATC)任务里验证"监测→触发→负荷下降"完整闭环(人类EEG,Front Hum Neurosci)
- [Dehais 2022](papers/passive-bci/dehais-2022-dual-passive-reactive-bci.md) — dual passive-reactive BCI：把被动(监测隐式状态)+反应(SSVEP 主动选择)合成双向闭环"人机共生"混合范式,拓宽 passive BCI 的通道组合(人类EEG,Front Neuroergonomics)
- [Reddy 2024](papers/passive-bci/reddy-2024-eye-brain-computer-interface.md) — eye-brain-computer interface：用前瞻性 ERP 的刺激前负波(SPN)在 XR 里做隐式选择确认,论证 SPN 由选择意图而非反馈驱动;gaze+EEG 目标选择的同期横向对照(离线,人类EEG,CHI '24)
- [Pan 2026](papers/passive-bci/pan-2026-vr-gaze-intent.md) — 首个动态 VR 游戏中实时闭环解码交互意图(gaze+被动EEG,人类23人)：affordance 稳在77.8–83.5%、approach-avoidance 仅价值两极时可解(coins vs bombs 80.8%)、价值模糊塌回随机(59%);离线66.3→在线69.6;划出"可解码信号=效价,意图仅在绑定强价值时连带可解"的能力边界(Zander/Klug 组,bioRxiv)

## affective-bci (7 papers)
情感脑机接口 / EEG 情绪解码(aBCI)。多为 passive BCI——检测而非主动控制情感状态。主线：理论原点→神经生理地基→benchmark 数据集→特征/深度学习→跨被试·跨数据集泛化。
- [Picard 1997](papers/affective-bci/picard-1997-affective-computing.md) — 专著《Affective Computing》提出"情感计算"概念与研究纲领，确立维度情绪模型(valence/arousal)+生理信号优先，整个领域理论原点
- [Davidson 1992](papers/affective-bci/davidson-1992-frontal-asymmetry-emotion.md) — 额叶 EEG alpha 不对称↔趋近/回避动机，把情绪落到可由 EEG 测量的神经生理量，EEG-情绪解码的神经生理地基
- [Mühl 2014](papers/affective-bci/muhl-2014-affective-bci-survey.md) — 定义 aBCI 的奠基综述(本子领域 milestone 抽取源)，框定问题结构与"个体差异+EEG非平稳"核心障碍
- [Koelstra 2012](papers/affective-bci/koelstra-2012-deap-dataset.md) — DEAP：经典多模态(EEG+外周)情绪 benchmark 数据集，32被试，valence/arousal/dominance/liking 标注
- [Zheng & Lu 2015](papers/affective-bci/zheng-2015-seed-differential-entropy.md) — SEED 数据集 + 微分熵(DE)特征，发现 gamma 频段与情绪最相关；与 DEAP 并列两大基准
- [Zheng & Lu 2016](papers/affective-bci/zheng-2016-transfer-learning-affective.md) — 首次把迁移学习/跨被试域适应引入 EEG 情绪识别(TPT)，开启跨被试·跨数据集泛化线(今日候选直接前驱)
- [Song 2018](papers/affective-bci/song-2018-dgcnn-eeg-emotion.md) — DGCNN 动态图卷积，可训练邻接矩阵建模 EEG 通道间关系，EEG 情绪深度学习地标

## shared-autonomy-bci (8 papers)
共享自主/共享控制:把神经解码指令与自主辅助(视觉引导、导航、AI副驾驶)按置信度融合,而非单纯提升解码精度。理论(策略混合/POMDP/深度RL)与BCI应用(皮层内/EEG)两条并行主线。milestone 抽取自 Farhadi et al. 2025 综述(arXiv 2506.16044)引用。
- [Dragan 2013](papers/shared-autonomy-bci/dragan-2013-policy-blending.md) — 策略混合形式化,把辅助表示为用户策略与预测自主策略的融合,共享控制理论基石,IJRR
- [Muelling 2017](papers/shared-autonomy-bci/muelling-2017-autonomy-infused-teleoperation-bci.md) — 首批皮层内人类BCI+共享自主实证(匹兹堡,2名被试7自由度机械臂),把纯BCI"做不到"的日常任务变可行
- [Downey 2016](papers/shared-autonomy-bci/downey-2016-blending-bmi-vision-guided.md) — 同源团队:BMI到达+视觉引导抓取分工,紧邻物体抓取准确率92%,证明收益来自"分工"而非整体提升解码
- [Javdani 2018](papers/shared-autonomy-bci/javdani-2018-hindsight-optimization.md) — 事后优化近似求解POMDP形式化的共享自主,与策略混合并列两大理论范式,IJRR(原RSS 2015)
- [Reddy 2018](papers/shared-autonomy-bci/reddy-2018-deep-rl-shared-autonomy.md) — 深度强化学习端到端学习共享自主,方法论从手工设计转向数据驱动,RSS
- [⚠ Unverified Ghasemi 2022](papers/shared-autonomy-bci/ghasemi-2022-shared-autonomy-eeg-bci.md) — 已隔离：当前DOI和题名未能核实，不作为shared-autonomy-bci milestone使用
- [Beraldo 2022](papers/shared-autonomy-bci/beraldo-2022-shared-intelligence-teleoperation-bmi.md) — EEG-BMI"共享智能"遥操作远程呈现机器人,机器人自主处理低层执行,IEEE THMS
- [Saussus 2026](papers/shared-autonomy-bci/saussus-2026-confidence-modulated-navigation.md) — 首次机制性刻画共享控制"何时失灵":置信度调制AI副驾驶把执行失败率37%→4%,但目标中途突变(Respawn)时反而80%→67%,离线回放+先验重置证明失灵是算法性的而非解码问题(2只恒河猴,bioRxiv)

## emg-motor-unit (6 papers)
外周肌电 / 运动单位解码→神经驱动。非脑接口，但与 BCI 主线在"神经接口/假肢控制"端相接。主线：共同驱动概念→盲源分解技术→神经驱动框架→人机接口应用。
- [De Luca & Erim 1994](papers/emg-motor-unit/deluca-1994-common-drive.md) — 提出"共同驱动/共同突触输入"概念，运动神经元协同放电的理论原点，整条线的理论基石
- [Holobar & Zazula 2007](papers/emg-motor-unit/holobar-2007-convolution-kernel-compensation.md) — 卷积核补偿(CKC)盲源分解，让 HD-sEMG 无创读出单运动单位放电序列的核心引擎
- [Farina, Merletti & Enoka 2014](papers/emg-motor-unit/farina-2014-neural-strategies-surface-emg.md) — 定义性框架：厘清表面肌电能/不能读出的神经信息，确立运动单位放电→神经驱动的正确用法与解释边界
- [Farina & Negro 2015](papers/emg-motor-unit/farina-negro-2015-common-synaptic-input.md) — 把共同驱动形式化为可计算的神经驱动框架(共同低频成分经肌肉低通传为力)，"放电序列→共同成分→力/控制"因果链
- [Negro 2016](papers/emg-motor-unit/negro-2016-convolutive-bss-decomposition.md) — 通用卷积盲源分解，把 CKC 推成可验证·社区标准方法(openhdemg 算法核心)，今日候选工具链源头
- [Farina 2017](papers/emg-motor-unit/farina-2017-manmachine-interface-motor-neurons.md) — 用脊髓运动神经元放电时序作控制命令驱动假肢(6名TMR截肢者，离线)，把运动单位解码推向真正的神经接口，本线最 BCI-relevant 地标

## cancer-neuroscience (10 papers)
神经科学 × 肿瘤：神经元活动如何经旁分泌/电与突触整合驱动胶质瘤，以及用神经记录读出/监测肿瘤状态。与 BCI 主线在"植入式神经接口"硬件端相接（同一电极换用途做疾病监测）。milestone 抽取自 Mancusi & Monje 2023 (Nature) 综述引用。
- [Venkatesh 2015](papers/cancer-neuroscience/venkatesh-2015-neuronal-activity-glioma-nlgn3.md) — 首次证明神经元活动驱动胶质瘤生长，鉴定活动调控旁分泌因子 NLGN3/BDNF，整条线起点(小鼠+人异种移植，Cell)
- [Venkatesh 2017](papers/cancer-neuroscience/venkatesh-2017-targeting-nlgn3-dependency.md) — 胶质瘤强依赖 NLGN3，阻断 ADAM10 切割释放可抑瘤，把通路推向治疗靶点(Nature)
- [Pan 2021](papers/cancer-neuroscience/pan-2021-nf1-activity-optic-glioma-initiation.md) — 神经元活动不仅促生长、还驱动 NF1 视路低级别胶质瘤的起始与维持，跨亚型跨阶段(小鼠，Nature)
- [Venkatesh 2019](papers/cancer-neuroscience/venkatesh-2019-electrical-synaptic-integration-glioma.md) — 电生理核心：神经元与胶质瘤间 AMPA 真突触 + 钾诱发电流随场电位增大(神经越活跃肿瘤电流越强)，"神经活动追踪肿瘤"的机制基础(Nature)
- [Venkataramani 2019](papers/cancer-neuroscience/venkataramani-2019-glutamatergic-input-glioma.md) — 独立团队与 Venkatesh 2019 背靠背，确证神经元→胶质瘤谷氨酸能真突触驱动进展(Nature)
- [Venkataramani 2022](papers/cancer-neuroscience/venkataramani-2022-glioblastoma-hijacks-invasion.md) — 肿瘤微管网络：胶质母细胞瘤劫持神经元样机制侵袭、缝隙连接耦合成网接收突触输入(Cell)
- [Derks 2018](papers/cancer-neuroscience/derks-2018-oscillatory-activity-glioma-survival.md) — "用神经活动读出肿瘤"最早人体证据：MEG 脑振荡与 NLGN3 相关、预测无进展生存期(人类)
- [Krishna 2023](papers/cancer-neuroscience/krishna-2023-glioblastoma-remodelling-human-circuits.md) — 人体地标：胶质母细胞瘤重塑人脑功能连接，高整合区伴认知下降、生存更短(术中记录+功能连接，Nature)
- [Mancusi & Monje 2023](papers/cancer-neuroscience/mancusi-2023-neuroscience-of-cancer-review.md) — 定义性框架综述，本子领域 milestone 抽取来源(Nature)
- [Stroud 2026](papers/cancer-neuroscience/stroud-2026-glioma-neural-monitoring.md) — 首批把 cancer neuroscience 机制做成慢性植入监测器件：<2g 头帽+微丝电极在自由活动小鼠(人 GBM/DIPG 异种移植)慢性记录 LFP，gamma 功率随肿瘤生长升高(跨 GBM+DIPG)、高 γ 上升速率预测个体生长率(交叉验证 R²=0.88)、化疗组轨迹带治疗反应信号；开辟"cancer neurotechnology"监测分支(Coherence Neuro×Monje，bioRxiv，小鼠概念验证)

## presurgical-mapping (7 papers)
术前无创功能定位：把术中直接皮层电刺激(DCS)所做的语言/运动皮层定位，用无创手段(MEG 激活成像、navigated TMS 干扰法)搬到术前，供神经外科规划。信号性质与 BCI 主线不同(不是控制、是定位)，但共用"皮层功能作图"的方法学，且 TMS/MEG 属非侵入模态。目前先建语言区一条线。milestone 抽取自 Sollmann/Ille et al. (2022, J Pers Med 12:1589) 综述 + Krieg et al. (2017) 共识。
- [Ojemann 1989](papers/presurgical-mapping/ojemann-1989-dcs-language-mapping.md) — 直接皮层电刺激语言定位金标准(117 例)：语言区高度个体化、呈 <Broca-Wernicke 的小马赛克，确立"必须逐人定位"，所有无创法的对照基准
- [Pascual-Leone 1991](papers/presurgical-mapping/pascual-leone-1991-tms-speech-arrest.md) — 首次用 TMS 无创诱发言语中断做语言偏侧化、与 Wada 一致；TMS 语言定位线起点(定位不精催生 navigated TMS)
- [Papanicolaou 2004](papers/presurgical-mapping/papanicolaou-2004-meg-wada-language.md) — MEG 作 Wada 无创替代做语言偏侧化(100 例，与 Wada 一致率 87%、灵敏度 98%)；MEG 术前语言线代表
- [Picht 2013](papers/presurgical-mapping/picht-2013-ntms-vs-dcs-language.md) — 首个 nrTMS 语言定位对照 DCS 金标准：高灵敏(~90%)、低特异(~24%)、高阴性预测值(~84%)，确立 nTMS 强在排除、弱在精确阳性
- [Tarapore 2013](papers/presurgical-mapping/tarapore-2013-ntms-megi-language.md) — nrTMS(干扰法)+MEGI(激活法)联合对照 DCS，两者互补；今日候选(MEG 引导 TMS 时机)的直接方法学前作
- [Krieg 2017](papers/presurgical-mapping/krieg-2017-ntms-mapping-protocol.md) — 赫尔辛基工作组共识协议，标准化 nTMS 运动/语言作图；本子领域标准化基石与 milestone 抽取源
- [Autti 2026](papers/presurgical-mapping/autti-2026-meg-informed-ntms-timing.md) — 用个人 MEG 语音激活时序个体化 nrTMS 的发放时机(PTI):best PTI 与 MEG 峰值显著正相关(Combined R=0.713，best PTI 平均早于峰值 132 ms)，把 nrTMS 个体化从"只调空间"推进到"空间+时间"，让被动 MEG 配置主动 TMS 的采集参数(非并联出第二张图)；仅额叶/语言产出区成立;概念验证(健康人 N=13、未对照 DCS、特异度收益待证)(赫尔辛基/Aalto·bioRxiv)

## visual-prosthesis (7 papers)
视觉假体 / 视网膜电刺激：给因感光细胞退化(RP/AMD)致盲者，电刺激存活的内层视网膜(神经节细胞/双极细胞)重建视觉。与 BCI 主线在"植入式电极+电刺激神经组织"硬件端相接。三条临床路线：视网膜上(epiretinal，刺激神经节细胞)、视网膜下(subretinal，刺激双极细胞)、光伏视网膜下(无线近红外供能)。另有一条 Chichilnisky 组"精准刺激"研究线(MEA 单细胞级刺激→空间电流成形→规避轴突束)，是今日候选 3 的直系。深层源头是皮层视觉假体(Foerster 1929/Brindley & Lewin 1968 的皮层光幻视)。milestone 抽取自 Retinal Prostheses: Engineering and Clinical Perspectives (2023, PMC10347280) + Expert Rev Ophthalmol (2025) 综述。
- [Humayun 1996](papers/visual-prosthesis/humayun-1996-retinal-stimulation-phosphenes.md) — 首次在盲人(RP/AMD)视网膜电刺激诱发可分辨光幻视，证明可绕过死掉的感光细胞刺激存活内层；整条线人体起点
- [Sekirnjak 2008](papers/visual-prosthesis/sekirnjak-2008-high-res-rgc-stimulation.md) — Chichilnisky 组：MEA 在安全电荷下单节细胞级高分辨刺激(离体猕猴)；"精准刺激"研究线起点
- [Zrenner 2011](papers/visual-prosthesis/zrenner-2011-alpha-ims-subretinal.md) — Alpha-IMS 视网膜下 1500 光电二极管芯片，盲人读字母组词/辨物/读钟面；视网膜下(双极细胞)路线代表
- [Humayun 2012](papers/visual-prosthesis/humayun-2012-argus-ii-trial.md) — Argus II 国际试验(30 例)，2013 年成为首个 FDA 批准的视网膜假体；视网膜上(epiretinal)路线里程碑
- [Jepson 2014](papers/visual-prosthesis/jepson-2014-spatially-patterned-stimulation.md) — 多电极空间电流成形(current steering)提升刺激的细胞类型选择性，把单细胞刺激推向阵列协同(Chichilnisky 组)
- [Grosberg 2017](papers/visual-prosthesis/grosberg-2017-axon-bundle-activation.md) — 指认轴突束激活为 epiretinal 假体的核心分辨率上限(512 电极离体猕猴)；正是候选 3 生物物理建模要规避的问题
- [Palanker 2020](papers/visual-prosthesis/palanker-2020-prima-photovoltaic.md) — PRIMA 无线光伏视网膜下假体首次人体(5 例 GA/AMD)，约 20/420、达像素间距；光伏路线里程碑

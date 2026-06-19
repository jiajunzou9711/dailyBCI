# DailyBCI Knowledge Base

Last updated: 2026-06-19
Total papers: 153

## speech-decoding (16 papers)
- [Guenther 2009](papers/speech-decoding/guenther-2009-wireless-bmi-speech.md) — 首个无线BMI实时语音合成，单电极元音合成，概念验证
- [Leuthardt 2011](papers/speech-decoding/leuthardt-2011-ecog-speech-bci.md) — 首个ECoG语音信号BCI控制，开创用说话意图控制BCI的ECoG路线
- [Bouchard 2013](papers/speech-decoding/bouchard-2013-sensorimotor-speech-organization.md) — 发现语音运动皮层编码发音动作（非声学特征），奠定articulatory decoding基础
- [Herff 2015](papers/speech-decoding/herff-2015-brain-to-text.md) — 首次brain-to-text连续解码，phone→LM→text框架，后续路线的起点
- [Anumanchipalli 2019](papers/speech-decoding/anumanchipalli-2019-speech-synthesis-neural-decoding.md) — 首次从脑活动合成可理解语音，确立两阶段解码范式（神经→运动→声音）
- [Makin 2020](papers/speech-decoding/makin-2020-machine-translation-cortex-text.md) — 首个encoder-decoder框架brain-to-text，引入sequence-to-sequence范式
- [Moses 2021](papers/speech-decoding/moses-2021-neuroprosthesis-anarthria.md) — 首次在瘫痪失语患者解码语音（PANCHO研究），50词，15词/分钟，NEJM
- [Willett 2023](papers/speech-decoding/willett-2023-high-performance-speech.md) — Phoneme-level解码，62词/分钟，125k词汇，证明phoneme路线可扩展
- [Metzger 2023](papers/speech-decoding/metzger-2023-speech-avatar-neuroprosthesis.md) — 78词/分钟+虚拟头像面部动画，首个多模态speech BCI
- [Luo 2023](papers/speech-decoding/luo-2023-stable-als-speech-bci.md) — ALS患者3个月无校准稳定使用，证明ECoG长期临床可行性
- [Card 2024](papers/speech-decoding/card-2024-accurate-rapidly-calibrating.md) — 97.5%准确率，125k词汇，<30分钟校准，8个月稳定，NEJM
- [Silva 2024](papers/speech-decoding/silva-2024-bilingual-speech-neuroprosthesis.md) — 首个双语speech BCI，发现跨语言共享articulatory表征
- [Wairagkar 2025](papers/speech-decoding/wairagkar-2025-instantaneous-voice-synthesis.md) — 80ms延迟流式语音合成，个性化声音，接近自然对话节奏
- [Kunz 2025](papers/speech-decoding/kunz-2025-imagined-speech-decoding.md) — 首次实时解码imagined speech，打破"内心语言不可解码"假设
- [Yoon 2026](papers/speech-decoding/yoon-2026-deep-neural-ensembles.md) — 深度集成首次实时闭环验证(WER 33.7%→26.0%)；提出伪集成单解码器降算力，把优化轴从精度扩到可部署性
- [Card 2026](papers/speech-decoding/card-2026-longterm-independent-bci.md) — 皮层内语音+光标BCI首次家庭自主长期使用：ALS患者19个月/3801小时/18.3万句、研究员不在场、保住全职工作；transformer达99.2%词准确率，信号18个月余弦相似度>0.6(同一患者T15，Nature Medicine)

## motor-bci (20 papers)
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
- [Willett 2024](papers/motor-bci/willett-2024-finger-click-bci.md) — 手指点击解码，实现网页浏览等日常数字任务，BCI走向实用
- [Neuralink 2024](papers/motor-bci/neuralink-2024-prime-n1-first-human.md) — 首个全植入无线1024通道BCI人体试验，患者日常使用>10h
- [BrainGate 2023](papers/motor-bci/braingate-2023-long-term-safety.md) — 17年14名参与者长期安全数据，信号仅下降7%，支撑临床扩展

## electrode-hardware (15 papers)
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
- [Hettick 2025](papers/electrode-hardware/hettick-2025-layer7-cortical-interface.md) — Layer 7高密度皮层表面阵列，推动微创、可逆的临床ECoG路线
- [Jung 2025](papers/electrode-hardware/jung-2025-bisc-wireless-subdural-bci.md) — BISC无线无电池65536电极subdural BCI，探索超大规模皮层表面接口

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

## non-invasive (21 papers)
- [Farwell 1988](papers/non-invasive/farwell-1988-p300-speller.md) — P300 speller范式，6×6矩阵，定义非侵入BCI通信范式
- [Wolpaw 1991](papers/non-invasive/wolpaw-1991-mu-rhythm-cursor.md) — 首个mu节律EEG光标控制，确立SMR-BCI路线
- [Pfurtscheller 1997](papers/non-invasive/pfurtscheller-1997-motor-imagery-erd.md) — Motor imagery ERD/ERS，建立运动想象BCI神经生理学基础
- [Birbaumer 1999](papers/non-invasive/birbaumer-1999-thought-translation-device.md) — Thought Translation Device，首次locked-in患者非侵入通信，Nature
- [Wolpaw 2002](papers/non-invasive/wolpaw-2002-bci-review.md) — BCI领域定义性综述，建立标准术语和系统架构，8000+引用
- [Blankertz 2006](papers/non-invasive/blankertz-2006-berlin-bci-zero-training.md) — Berlin BCI零训练范式，CSP+机器学习，训练负担从用户转向算法
- [Chen 2015](papers/non-invasive/chen-2015-high-speed-ssvep-speller.md) — SSVEP speller 5.32 bits/sec，60字符/分钟，非侵入BCI速度纪录，PNAS
- [Lawhern 2018](papers/non-invasive/lawhern-2018-eegnet.md) — EEGNet跨范式通用CNN，成为EEG深度学习标准基线
- [Defossez 2023](papers/non-invasive/defossez-2023-meta-meg-speech-decoding.md) — Meta FAIR用MEG解码语音，72.5% top-10准确率，非侵入语音BCI探索
- [Ding 2025](papers/non-invasive/ding-2025-finger-mi-healthy.md) — 首次用头皮EEG实时控制individual-finger级机械手(健康熟练者，2指80.6%/3指60.6%)：把"逐指"从皮层内推到非侵入，He组非侵入逐指线起点
- [Ding 2026](papers/non-invasive/ding-2026-finger-mi-stroke.md) — 首次在零经验中风患者用头皮EEG实现实时逐指机械手控制：2指83.5%/3指61.4%(随机50%/33%)、患侧≈健侧(d=0.18/0.42)、低频delta是信号；中风把精细运动编码重组成双侧/分散/低频，EEGNet跟住(He组，naïve中风≈其2025 Nat Commun健康熟练者)

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

## invasive-recording (9 papers)
- [Kennedy 1998](papers/invasive-recording/kennedy-1998-first-human-intracortical-bci.md) — 首次人类慢性intracortical记录用于BCI，Neurotrophic Electrode
- [Leuthardt 2004](papers/invasive-recording/leuthardt-2004-first-ecog-bci.md) — 首次证明ECoG可用于BCI控制，确立ECoG作为记录模态的"最优平衡点"
- [Schalk 2008](papers/invasive-recording/schalk-2008-ecog-2d-control.md) — 首次ECoG 2D控制，发现high-gamma具有cosine方向调谐特性
- [Ray 2011](papers/invasive-recording/ray-2011-high-gamma-origin.md) — 证明high-gamma反映群体放电率（非节律振荡），ECoG特征选择的理论基础
- [Chestek 2011](papers/invasive-recording/chestek-2011-long-term-signal-stability.md) — 系统量化intracortical信号慢性退化，证明threshold crossing优于sorted单元
- [Buzsáki 2012](papers/invasive-recording/buzsaki-2012-extracellular-fields-origin.md) — 定义性理论框架：所有胞外信号（EEG/ECoG/LFP/spikes）的生物物理起源
- [Flint 2013](papers/invasive-recording/flint-2013-lfp-long-term-bmi.md) — LFP-based BMI性能可比spikes，11个月稳定无需重训练
- [NEO 2024](papers/invasive-recording/neo-2024-epidural-minimally-invasive-bci.md) — 首个无线无电池硬膜外人体BCI，eECoG作"第四类模态"，C4完全SCI患者9个月家用信号不降反升，驱动脑-脊髓康复（清华×博睿康）
- [NEO 2025](papers/invasive-recording/neo-2025-fine-grained-2d-cursor.md) — 硬膜外微创BCI实现精细二维光标控制，发现双侧/多效应器表征，ITR 36.7 bpm、记录稳定>18个月

## sensory-feedback (7 papers)
- [Romo 1998](papers/sensory-feedback/romo-1998-icms-tactile-discrimination.md) — 首次ICMS产生与自然触觉不可区分的人工触觉感知
- [Dhillon 2005](papers/sensory-feedback/dhillon-2005-peripheral-nerve-sensory-feedback.md) — 首次周围神经接口提供截肢者触觉和本体感觉反馈
- [Tabot 2013](papers/sensory-feedback/tabot-2013-biomimetic-icms-touch.md) — 仿生ICMS模式恢复接近自然水平的触觉辨别，确立"仿生刺激"原则
- [Raspopovic 2014](papers/sensory-feedback/raspopovic-2014-bidirectional-sensory-prosthesis.md) — 首个实时双向感觉假肢，截肢者无视觉辨别物体硬度和形状
- [Tan 2014](papers/sensory-feedback/tan-2014-long-term-stable-touch.md) — 周围神经接口提供>1年稳定自然触觉感知，解决长期稳定性瓶颈
- [Flesher 2016](papers/sensory-feedback/flesher-2016-first-human-icms-s1.md) — 首次人类S1皮层ICMS恢复触觉，感觉自然、按体感觉排列、稳定数月
- [Hughes 2021](papers/sensory-feedback/hughes-2021-icms-object-identification.md) — 首次证明人类可仅通过ICMS触觉反馈识别物体，从感觉诱发到信息传递

## neuromodulation (7 papers)
- [Benabid 1991](papers/neuromodulation/benabid-1991-dbs-tremor-suppression.md) — 开创现代DBS疗法，高频VIM刺激长期抑制帕金森震颤，可逆可调
- [Limousin 1998](papers/neuromodulation/limousin-1998-stn-dbs-parkinson.md) — 确立STN-DBS作为晚期帕金森标准治疗，UPDRS运动评分改善~50%
- [Morrell 2011](papers/neuromodulation/morrell-2011-rns-closed-loop-epilepsy.md) — 首个闭环脑刺激RCT（RNS），191名癫痫患者，2013年FDA批准
- [Rosin 2011](papers/neuromodulation/rosin-2011-closed-loop-dbs-superior.md) — 首次证明闭环DBS优于开环DBS，用更少刺激获得更大改善
- [Little 2013](papers/neuromodulation/little-2013-adaptive-dbs-human.md) — 首次人类闭环自适应DBS，用beta振荡作为生物标志物，刺激量减半
- [Scangos 2021](papers/neuromodulation/scangos-2021-closed-loop-depression.md) — 首次个性化闭环神经调控治疗难治性抑郁症
- [Shirvalkar 2023](papers/neuromodulation/shirvalkar-2023-chronic-pain-biomarker.md) — 首次从颅内慢性记录预测慢性疼痛状态，OFC为关键生物标志物

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

## clinical-regulatory (9 papers)
- [Huggins 2011](papers/clinical-regulatory/huggins-2011-bci-user-needs.md) — 首次系统调查BCI用户需求，定义准确率≥90%、速度≥15字母/分钟等临床标准
- [Yuste 2017](papers/clinical-regulatory/yuste-2017-four-ethical-priorities.md) — Nature评论：四大神经伦理优先领域，催生NeuroRights Foundation
- [Ienca 2017](papers/clinical-regulatory/ienca-2017-neurorights-framework.md) — 系统提出四项神经权利（认知自由、心理隐私、心理完整性、心理连续性）
- [Chile 2021](papers/clinical-regulatory/chile-2021-neurorights-constitution.md) — 全球首个将神经权利写入宪法的国家，2023年最高法院首个司法判例
- [Oxley 2023](papers/clinical-regulatory/oxley-2023-switch-trial-safety.md) — Synchron SWITCH试验：首个血管内BCI人体安全数据，JAMA Neurology
- [Rubin 2023](papers/clinical-regulatory/rubin-2023-braingate-safety-profile.md) — BrainGate 14人×17年安全数据，安全性与已批准DBS相当，Neurology
- [Synchron 2024](papers/clinical-regulatory/synchron-2024-command-feasibility.md) — COMMAND：首个FDA IDE永久植入BCI研究，6/6安全终点达标
- [Precision 2025](papers/clinical-regulatory/precision-2025-layer7-510k.md) — 首个BCI通过FDA 510(k)获批，开创快速监管通道
- [Neuracle/NEO 2026](papers/clinical-regulatory/neuracle-2026-neo-nmpa-approval.md) — 中国NMPA颁发全球首张侵入式BCI注册证（三类），首个商业获批并接入医保的半侵入BCI，36例临床全部抓握改善（2026-03-13）

## ai-neural-modeling (19 papers)
- [Pandarinath 2018](papers/ai-neural-modeling/pandarinath-2018-lfads.md) — LFADS序列VAE，从spikes中恢复single-trial潜在动力学，Nature Methods
- [Ye 2021](papers/ai-neural-modeling/ye-2021-neural-data-transformer.md) — NDT首次将Transformer应用于神经spike数据，推理速度比RNN快6倍
- [Ye 2023](papers/ai-neural-modeling/ye-2023-ndt2-multi-context.md) — NDT-2跨session预训练，证明预训练+微调范式在神经数据上有效，NeurIPS 2023
- [Azabou 2024](papers/ai-neural-modeling/azabou-2024-mtm-universal-translator.md) — MtM三维度掩码自监督，跨脑区跨细胞类型联合建模，NeurIPS 2024
- [Azabou 2025](papers/ai-neural-modeling/azabou-2025-poyo-plus.md) — POYO+多session多任务foundation model，Allen Institute全量数据，ICLR 2025
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

## population-dynamics (8 papers)
- [Sadtler 2014](papers/population-dynamics/sadtler-2014-neural-constraints-learning.md) — 流形内模式易学、流形外学不会，奠定"神经流形约束学习"范式（猴，皮层内BCI），Nature
- [Gallego 2017](papers/population-dynamics/gallego-2017-neural-manifolds-movement.md) — 定义性框架综述，确立neural manifold/neural modes作为群体运动控制的统一语言，Neuron
- [Golub 2018](papers/population-dynamics/golub-2018-learning-neural-reassociation.md) — 流形内学习机制=neural reassociation（重配已有模式而非生成新模式），Nat Neurosci
- [Oby 2019](papers/population-dynamics/oby-2019-new-activity-patterns-long-term.md) — 流形外经长期训练可长出新活动模式，定义"短期重配 vs 长期重塑"对照，PNAS
- [Gallego 2020](papers/population-dynamics/gallego-2020-long-term-stability-dynamics.md) — 低维潜在动力学跨~2年稳定（单神经元在换），BCI长期免校准的群体动力学基础，Nat Neurosci
- [Gallego 2018](papers/population-dynamics/gallego-2018-preserved-manifold-multiple-behaviors.md) — 多种运动行为共享同一被保留流形，证明流形是通用低维底座，Nat Commun
- [Busch 2026](papers/population-dynamics/busch-2026-human-noninvasive-manifold-bci.md) — 首次在人类无创(fMRI)验证流形约束学习：流形内ΔBrainControl +49.3/+16.4可学、流形外−0.4学不会(N=18)，Nat Neurosci
- [de Vicente 2026](papers/population-dynamics/devicente-2026-circuit-specific-volitional-learning.md) — 首次把流形-BCI学习搬出运动皮层、进海马CA3并与M1对比：两区学得一样好(p=0.453 n.s.)但动力学分叉(M1流过/CA3折返)，RNN证差异源于环路架构→principled degeneracy，bioRxiv

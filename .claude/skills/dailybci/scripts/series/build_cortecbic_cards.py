# -*- coding: utf-8 -*-
"""日报 2026-08-29「CorTec Brain Interchange–BCI2000 平台」: 15 张图卡。"""
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-29-cortec-bic-closed-loop")
FIGS = os.path.join(OUT, "figs")
CROP = os.path.join(PROJECT, "papers", "crop")
os.makedirs(OUT, exist_ok=True)
P = lambda *a: os.path.join(*a)
REF = "Lampert et al. 2026, bioRxiv"

gen = CardGenerator(date="2026.08.29")

# ---------- 01 封面 ----------
gen.cover_card(
    "闭环神经调控平台",
    "配置与验证全公开",
    "一台可植入的双向器件接进开源软件，从台架一路验到人体。",
    P(OUT, "01-cover.png"),
    concept_image=P(CROP, "cover-fig4A.png"),
    concept_height=610, title_size=100, title_top=80,
)

# ---------- 02 目录 ----------
gen.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["2026 年 8 月 28 日上线的 bioRxiv 预印本《A Translational Platform for Brain-Computer "
     "Interfaces and Adaptive Neuromodulation》。一作与共同通讯 Frederik Lampert、"
     "共同通讯 Kai J. Miller，均在 Mayo Clinic 神经外科；作者中包含 **Gerwin Schalk**——"
     "BCI2000 系统 2004 年 IEEE TBME 论文的第一作者³。",
     "方法：把 CorTec 的全植入双向器件接进开源的 BCI2000，做台架与盐水表征、"
     "五只犬的长期植入（累计 2,296 个植入日）、以及一例人体演示。"],
    P(OUT, "02-toc.png"), figure_height=640, annot_size=27,
)

# ---------- 03 ① ----------
gen.text_card(
    "① 少刺激反而更好，这是闭环的理由",
    ["现在临床在用的神经调控大多是开环的：按预设参数一直放电，不管患者此刻的脑活动是什么样。"
     "这套方式在运动障碍和癫痫上已是成熟疗法¹。",
     "那么一个直接的问题是：这些电是不是都有必要。人体上的一个对照来自 **8 名**晚期帕金森患者²——"
     "用丘脑底核（subthalamic nucleus）局部场电位里的 **beta 振荡功率**作触发信号，"
     "只在功率超过阈值时才给刺激。运动评分改善 **66%**（非盲）/ **50%**（盲评），"
     "比传统持续刺激分别高出 **29%**（p=0.03）和 **27%**（p=0.005）；"
     "同时**刺激时间减少 56%**，能耗相应下降。持续放电里有相当一部分并不必要。",
     "自适应刺激由此定义：按实时的神经活动决定何时给刺激。剩下的问题是，"
     "研究者要真正实现一个这样的闭环，手上得有什么。"],
    P(OUT, "03-card1.png"),
)

# ---------- 04 ② ----------
gen.figure_card(
    P(CROP, "fig01-full.png"), f"{REF}, Fig. 1",
    ["如上图，这套生态由三部分构成。**左侧是植入部分**：BIC 主机，外接皮层表面电极与深部电极。"
     "**中间是体外部分**：磁吸在体表的圆盘头件隔着皮肤感应供电；旁边带两根线的小盒子是通信单元，"
     "一端接头件、一端接电脑。**右侧是计算机**，跑开源的 BCI2000¹。",
     "图上两个规格需要参照系。**32 通道**：同类可植入双向器件里，Medtronic 的 Percept PC 与 "
     "Summit RC+S 都只有 4 个感测通道⁴；32 显得少，是因为拿它对比读单神经元的皮层内阵列"
     "（犹他阵列 96–100 通道）。**1 kHz 采样**：这台接的是 ECoG 片与 DBS 电极，读的是场电位，"
     "硬件通带 2–325 Hz¹。"],
    P(OUT, "04-card2.png"), figure_height=440, title="论文的产出是一套公用的基础设施", title_num="②",
)

# ---------- 05 ③ ----------
gen.figure_card(
    P(CROP, "c03-imped.png"), f"{REF}, Fig. 2H",
    ["验证的第一级在台架和盐水里，量的是平常厂商不公布、论文也很少报的参数。论文说这套测评"
     "本身可以当作蓝图：以后要表征任何一台可植入神经调控设备，都该量这几项¹。",
     "**延迟**：以往的报告只给一个合并的总延迟。这篇把它拆成两段分别测——采集延迟 "
     "**10.89 ± 1.59 ms**，刺激延迟最快的一种模式 **11.45 ± 1.19 ms**，"
     "相加得到闭环干预的**理论硬件下限约 22 ms**¹。",
     "**阻抗**：如上图，把设备接到已知元件值的测试电路上（右侧三个电路图），"
     "让它照常发出 220 µA 的小电流脉冲去测。纯电阻的 997.7 Ω 读成 **1021 Ω**；"
     "而理论 **100 Ω** 读成 **46 Ω**。低阻端与在体无关（慢性电极在 kΩ 量级，坏道判据是超过 10 kΩ），"
     "所以论文给的是用法：这个读数应当读作电极完整性的指示，它不是精确的电学测量值¹。"],
    P(OUT, "05-card3.png"), figure_height=330, title="闭环最快 22 ms，阻抗只能看趋势", title_num="③",
)

# ---------- 06 ④ ----------
gen.figure_card(
    P(CROP, "c04-elec.png"), f"{REF}, Fig. 5B",
    ["这台主机本体不带电极，接什么由实验决定。如上图，**#2 号（Billy）接深部电极**，"
     "目标是海马（hippocampus）与丘脑前核（anterior nucleus of thalamus）；"
     "**#3 号（Strelka）接硬膜外 ECoG**；**#4、#5 号是两者的混合配置**¹。",
     "植入方式：主机放在**肩胛区**，电极导线经皮下隧道通到颅骨植入位点。表面电极经颅骨开口贴在"
     "**硬膜外**、不穿硬膜；深部电极立体定向置入目标结构¹。",
     "规模：五只犬六台设备，累计 **2,296 个植入日**，最长一台超过**三年**¹。"],
    P(OUT, "06-card4.png"), figure_height=470, title="一台主机，接过三种电极配置", title_num="④",
)

# ---------- 07 ⑤ ----------
gen.figure_card(
    P(CROP, "c05-chan.png"), f"{REF}, Fig. 6B",
    ["如上图，各台设备的可用通道数走势并不一致：**蓝线（#1 号）随时间逐渐下降**，"
     "从 32 掉到不足 20；#2、#3、#4 号在随访期内保持稳定或有改善。"
     "无线链路本身很稳，各设备平均丢包率都低于 **5%**¹。",
     "论文接着追问通道为什么坏。它写明有一部分属于电路故障，但**多数与机械变化相关**，"
     "三条证据指向同一处：阻抗随时间渐变、信号质量同步劣化、以及术后 CT 直接看到**电极移位**。"
     "作者归因于犬自由活动时导线承受的应力¹。",
     "这个发现已经产生后果：新一代电极据此改用**绞合导线**¹。"],
    P(OUT, "07-card5.png"), figure_height=470, title="通道失效多为机械原因", title_num="⑤",
)

# ---------- 08 ⑥ ----------
gen.figure_card(
    P(CROP, "c06-map.png"), f"{REF}, Fig. 7A",
    ["**#1 号是在植入约两年后做的功能映射，#3 号约一年后**¹。选这么晚的时间点是有意的："
     "这一步要支撑的结论正是长期记录足够稳定。",
     "如上图，每行对应一类刺激，红点是显著激活的电极，指标是 65–175 Hz 宽带激活的 r²。"
     "**视觉最强**（上两行，r² = 0.27–0.38），定位在枕叶（occipital lobe）。"
     "**运动响应弱但定位干净**（#1 号最大 r² 只有 0.08），集中在感觉运动皮层"
     "（sensorimotor cortex）。**听觉最不可靠**（r² 仅 0.01–0.07）¹。",
     "能读出信号只是一半。这台设备还要能写。"],
    P(OUT, "08-card6.png"), figure_height=560, title="植入两年后仍能读出任务相关响应", title_num="⑥",
)

# ---------- 09 ⑦ ----------
gen.figure_card(
    P(CROP, "c07-sites.png"), f"{REF}, Fig. 8（左）",
    ["实验对象是 #4 号犬（自发癫痫），睡眠期进行。如上图，绿圈与橙圈是两处记录位点，"
     "黄色闪电是丘脑（thalamus）刺激位点¹。",
     "**记录位点是任意选的。** 论文写明这两处与癫痫病灶无关，是实验中看在线频谱临时挑的。"
     "这一步要验的正是任意特征都能当控制信号¹。",
     "**控制信号怎么算**：1 秒窗上用自回归模型估频谱功率，取出控制频段——梨状叶"
     "（piriform lobe）**20–24 Hz**、皮层（cortex）**75–85 Hz**——再相对前 **30 秒**做 z 分数归一化。"
     "**触发判据**是超过阈值并**持续 0.5 秒**；刺激为丘脑 **250 µA**。"
     "每次刺激后有 **2.5 秒不应期**，防止刺激自身触发下一次¹。"],
    P(OUT, "09-card7.png"), figure_height=430, title="闭环怎么配：任意两个位点当触发源", title_num="⑦",
)

# ---------- 10 ⑧ ----------
gen.figure_card(
    P(CROP, "c08-loop.png"), f"{REF}, Fig. 8（右）",
    ["上图两个方框是两个位点的记录，绿框是皮层的 75–85 Hz，橙框是梨状叶的 20–24 Hz。每框三行："
     "**原始信号**、**时频图**（那几道**竖直空白**是刺激期间被排除的时段）、"
     "**在线处理的输出**——黑线是归一化控制信号，红色虚线是阈值，橙色竖线是刺激¹。",
     "**黑线越过红线之后，刺激随即发出**，这就是闭环闭合的那一刻。图上这个例子里，"
     "从神经事件起始到刺激发出约 **1.5 秒**，该延迟主要由频谱分析的窗长决定¹。",
     "论文给的是一个代表性示例，没有报告触发次数或误触发率。这一步验的是可行性，不是性能。"],
    P(OUT, "10-card8.png"), figure_height=450, title="输出越过阈值线，刺激随即发出", title_num="⑧",
)

# ---------- 11 ⑨ ----------
gen.figure_card(
    P(CROP, "c09-bsep.png"), f"{REF}, Fig. 10A–C",
    ["这一步验的是双向能力的另一半：刺激下去以后，能不能在别处读到反应。#5 号犬，"
     "经丘脑（thalamus）的方向性 DBS 导线给**单脉冲电刺激**——**3 mA**、脉宽 **200 µs**，"
     "在皮层电极上记录¹。",
     "如上图，同一个刺激位点在三个皮层记录位点引出的诱发响应，形态与幅度各不相同；"
     "灰色是单次试次，粗线是平均。改变方向性 DBS 导线上激活的电极段，响应也随之改变，"
     "且**刺激方向朝向记录位点时响应更大**¹。",
     "**一个反直觉的发现**：在体最好的记录配置是**不指定硬件参考电极、只用地电极**，"
     "这样才不会在刺激期间让放大器饱和；而这与他们在盐水台架上的结果相反¹。"],
    P(OUT, "11-card9.png"), figure_height=430, title="在体最好的记录配置与台架上相反", title_num="⑨",
)

# ---------- 12 ⑩ ----------
gen.figure_card(
    P(CROP, "c10-human.png"), f"{REF}, Fig. 11A–B",
    ["**这一步没有在人体植入任何东西。** 如上图，用的是 **benchtop 版本**的 BIC，"
     "接到患者**外置的 sEEG 导线**上。受试者是 1 名 34 岁男性药物难治性癫痫患者，"
     "因临床评估已植入立体定向脑电（sEEG）电极，位置完全由临床决定¹。",
     "先用临床放大器做运动筛查，选出任务相关调制最强的一对双极导联；"
     "再把采集切换到 BIC，用 **72.5–112.5 Hz** 的高频活动做实时一维光标控制。"
     "结果：真实运动 30 试次命中 11、超时 16；运动想象 26 试次命中 5、超时 21。"
     "论文如实称之为仅为中等的解码性能¹。",
     "这里要分清两种闭环。光标控制闭合的是**人—设备—屏幕**这一环，"
     "与 ⑦⑧ 里神经信号触发刺激的闭环是两件事。**这一步验的是 BIC 作为采集设备"
     "能否驱动一个既有的实时 BCI 范式。**"],
    P(OUT, "12-card10.png"), figure_height=360, title="人体这一步验的是采集链路加软件", title_num="⑩",
)

# ---------- 13 ⑪ ----------
gen.text_card(
    "⑪ 数据、代码、手术流程全部公开",
    ["论文说自己的产出是一套基础设施，那就要让别人真的拿得到。开放的东西分三处¹。",
     "**数据在两个公共库各存一份。** OpenNeuro 上的 ds004624（BIDS 格式，含 iEEG 与 MRI，"
     "**1,976 个文件、19.31 GB**）；DANDI Archive 上的 000571（**68,210 个文件、21.6 GB**，CC0 许可）。"
     "同一批记录按两种社区标准各存一遍，让不同工具链的人都能直接读。",
     "**代码在 GitHub**（GPL-3.0），用途是复现论文的分析与图。",
     "**文档挂在 BCI2000 Wiki 上**：安装编译说明、全部配置项，还包括**犬的手术流程**、"
     "闭环刺激的具体做法，以及怎么把惯性测量单元与设备做时间同步。"],
    P(OUT, "13-card11.png"),
)

# ---------- 14 ⑫ ----------
gen.text_card(
    "⑫ 局限性",
    ["论文自己写明四条¹。",
     "**闭环那一步只验了可行性**：给出的是代表性示例，没有报告触发次数、误触发率或灵敏度。",
     "**人体那一步的解码性能仅为中等**：受试者训练时间有限，且电极位置完全由临床决定、未为 BCI 优化。",
     "**脑刺激诱发电位的可靠采集仍是持续挑战**，需要在硬件、刺激方案与信号处理三方面继续改进伪迹抑制。",
     "**犬模型自身带来的限制**：磁吸头件会间歇脱落、且需要感应供电，因此只能分场次记录，"
     "做不到连续监测。论文强调这几条反映的是这个动物模型的特点，不是技术本身的固有限制。"],
    P(OUT, "14-card12.png"),
)

# ---------- 15 尾卡 ----------
gen.tail_card(
    ["¹ Lampert F, et al. (2026). A translational platform for brain-computer interfaces and "
     "adaptive neuromodulation: technical characterization, long-term validation, and implementation "
     "of the CorTec Brain Interchange–BCI2000 ecosystem. bioRxiv 2026.08.27.747359.",
     "² Little S, et al. (2013). Adaptive deep brain stimulation in advanced Parkinson disease. "
     "Ann Neurol 74:449–457.",
     "³ Schalk G, McFarland DJ, Hinterberger T, Birbaumer N, Wolpaw JR. (2004). BCI2000: a "
     "general-purpose brain-computer interface (BCI) system. IEEE Trans Biomed Eng 51:1034–1043.",
     "⁴ Zhu B, Shin U, Shoaran M. (2021). Closed-loop neural prostheses with on-chip intelligence: "
     "a review and a low-latency machine learning model for brain state detection. "
     "IEEE Trans Biomed Circuits Syst 15:877–897."],
    P(OUT, "15-tail.png"),
    lead_paragraphs=[
        "这篇的读者主要是同行——它真正的产出，是把「怎么验一台可植入神经调控设备」"
        "写成了一份可以照做的清单。",
        "对不做这一行的人，能带走的是三个已经被量化的边界：**闭环的硬件下限约 22 ms**、"
        "**阻抗读数只能看趋势**、**通道失效多为机械原因**。",
    ],
)
print("done")

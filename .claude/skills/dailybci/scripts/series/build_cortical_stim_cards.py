"""第二期:电刺激视皮层能做到什么 —— 图卡装配。
卡片标题与目录卡逐条对应(① ~ ⑧),便于读者导航。
"""
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
from card_generator import CardGenerator

PROJECT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-11-cortical-stim")
FIGS = os.path.join(OUT, "figs")
PAPERS = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

g = CardGenerator(date="2026.08.11")
P = lambda *a: os.path.join(*a)


# 01 封面
g.cover_card(
    "给视皮层通电", "看见分立的光点",
    "电极点得亮光点,却拼不成一幅图像。决定输出的是皮层自身的结构。",
    P(OUT, "01-cover.png"),
    concept_image=P(PAPERS, "cover-fig7c.png"),
    concept_height=560, title_size=124, title_top=90,
)

# 02 目录 + 来源
g.figure_card(
    P(FIGS, "toc.png"), "本期路线",
    ["本期不解读单篇论文。正文引用 **10 篇**同行评审文献,以及 **6 项**试验注册记录、监管文件与公司公告,"
     "逐条列于尾卡,**两个证据层级分开标注**。",
     "封面图为同时刺激 4 个相邻电极时,一位盲人参与者报告看到的 3 个光点,"
     "取自 Fernández 等 2021 年 **J Clin Invest**。"],
    P(OUT, "02-toc.png"), figure_height=650,
)

# 03 ①
g.figure_card(
    P(PAPERS, "fig5a-phosphene-map.png"), "Fig. 5A · Fernández et al., J Clin Invest 2021",
    ["给人的初级视皮层通电,人会看见一个孤立的光点,称作**光幻视**——眼睛和视神经全程不参与¹。"
     "它有多大只能由患者自述:小的像针尖,"
     "大的像手臂伸直时指间捏着的一枚 **20 毫米硬币**²。",
     "如上图,画的是一位盲人参与者的**视野**。每个编号圆圈是一个电极诱发的光点落进视野的位置,"
     "黄色是术前推算的预期落点,标定尺代表 **1 度**³。二者吻合良好:"
     "皮层上相邻的位置,对应视野中相邻的位置。",
     "位置可预测¹,于是最自然的方案成立了:铺一片电极,把摄像头的像素亮度直接映射成刺激强度。"
     "往下先弄清一件事:上图那些位置,是怎么测出来的。"],
    P(OUT, "03-phosphene-map.png"), figure_height=415,
    title="电流打进 V1,人会看见一个光点", title_num="①",
)

# 04 ②
g.figure_card(
    P(FIGS, "fig-eye.png"), "眼动补偿的两笔账",
    ["要读懂上一张的坐标,先看正常人为什么觉得世界不动。眼睛右转 10 度,物体在视野中的位置随之左移 10 度;"
     "大脑把这段位移与眼位相加,两者抵消,世界纹丝未动。",
     "这套补偿可以自己验:隔着眼皮**轻推**眼球,世界会晃——这次少了「我要转眼」那道指令的副本。"
     "光幻视正相反:电极把视野中的位置钉死,大脑却照常加上眼位,"
     "**补偿了一个并不存在的位移**,光幻视于是跟着眼睛走⁴。",
     "所以位置只能在「眼位为零」的前提下测:要求她保持视线朝向正前方,消掉眼位偏移;"
     "板子中央设一个摸得到的凸起,给她一个报告位置的坐标原点³。"
     "这套「电极对应像素」的方案叫 **1-to-1 mapping**,至今仍是常规策略⁵。"],
    P(OUT, "04-eye-position.png"), figure_height=370,
    title="坐标建立在「眼位不动」这个假定上", title_num="②",
)

# 05 ③
g.figure_card(
    P(PAPERS, "fig5a-top.png"), "Fig. 5A 上半 · Fernández et al., 2021",
    ["扣掉眼位后,每个电极对应的视网膜拓扑位置是稳定的⁴。**但稳定不等于可推算**——原文的结论是,"
     "光幻视位置在大尺度上与视网膜拓扑一致,却**未显示出与各电极位置之间清晰的规整对应**³。",
     "如上图,右边是 96 个电极规整的方阵,左边是它们诱发的光幻视落点³。"
     "**规整的输入,换来一片没有对应秩序的落点。** 同一个电极也不止对应一个位置:"
     "加大电流会在关于水平子午线**镜像**的位置多出一个光点¹ ⁶。",
     "原本的答案来自猕猴运动皮层:阈值电流随距离**平方**增长,10 µA 约激活尖端 **85 µm** 以内⁷。"
     "而小鼠皮层的双光子观察显示:被激活的神经元**稀疏、散得很开、有时远在毫米之外**——"
     "电流抓住的是**轴突**⁸。以上说的都是单个电极。"],
    P(OUT, "05-no-mapping.png"), figure_height=370,
    title="电极排布规整,光点落点散乱", title_num="③",
)

# 06 ④
g.figure_card(
    P(PAPERS, "fig7-multielectrode.png"), "Fig. 7 · Fernández et al., 2021（C/D/E/B 重排）",
    ["同时点亮多个电极,问题换一种形式:50 对电极的同时刺激里,**76.4%** 只诱发出**一个**光点。"
     "要稳定看到两个,必须放弃「同时」——两次刺激**错开超过 250 ms**,"
     "她才有 90% 的概率看到两个分立光点³。而普通视频每秒几十帧。",
     "如上图,每格右上是被刺激的电极,左下是她画下的知觉。图 C:**4 个电极,看到 3 个点**;"
     "图 D:12 个电极,一条横线;图 E:同为 8 个电极,横排出横线、竖排出竖线。",
     "排布确实影响结果,但结果不是输入的副本。4 个相邻电极同时刺激,阈值比单电极低 **28%**³;"
     "同时诱发三个以上光幻视,它们会**变成共面**²。四条否定摆完,该问的是:那到底由什么决定。"],
    P(OUT, "06-not-independent.png"), figure_height=420,
    title="同时点亮四个,她看见三个", title_num="④",
)

# 07 ⑤
g.figure_card(
    P(FIGS, "fig-decides.png"), "输出由什么决定",
    ["要把「像素」模型换掉,得说清输出由什么决定。**13 名人类被试、93 个电极**给出一条:"
     "光幻视的大小**随电流迅速饱和**;决定它的是被激活的那块皮层面积,以及它在视野地图上的位置⁹。",
     "如上图,左列是模型认为由输入决定的四件事,右列是实际的决定因素——**右列全是皮层自己的性质**。"
     "**电刺激是对一个高度组织化的系统施加一次扰动,系统按自己的结构响应;"
     "你能得到的结果,落在皮层允许的那一组状态里。**",
     "**本期只能说到这里**:那组状态有多大、能不能被系统地找出来,本期给不出答案。"
     "往下只剩两条路——放弃「同时呈现多个点」,或者先摸清系统的响应再挑刺激。"],
    P(OUT, "07-what-decides.png"), figure_height=410,
    title="能得到什么,由皮层的结构决定", title_num="⑤",
)

# 08 ⑥
g.figure_card(
    P(PAPERS, "bc-f0002.jpg"), "Fig. 1 · Beauchamp et al., Cell 2020",
    ["另一组人给出了第一条路的答案。他们本想比较「依次」与「同时」哪个更能传形状,"
     "**结果对照做不成**:同时刺激 5 个电极,被试只看到 **2 个大光斑**,换一组仍是 2 个¹⁰。",
     "如上图。**图 A**:多个探针同时压进手掌摆出字母,只得到一团无定形的感觉;"
     "**图 B**:用一个探针按笔顺划过去,字母就出来了。**图 C、D** 把同一件事搬到皮层¹⁰。",
     "这条路走通了:**硬膜下表面电极**,盲人被试**只用 6 个电极**、未经指导即能画出对应形状,"
     "最高 **每分钟 86 个形状**¹⁰。但它绕过了问题,没有解决问题——轨迹仍要由人依据光幻视图手工设计。"],
    P(OUT, "08-dynamic-tracing.png"), figure_height=460,
    title="放弃「同时」,改用时间描摹", title_num="⑥",
)

# 09 ⑦
g.figure_card(
    P(FIGS, "fig-systems.png"), "三套有人体数据的皮层视觉假体",
    ["这条路线在产业侧有对应的系统。**Orion 视觉皮层假体**的早期可行性研究 2017 年 11 月启动、"
     "2025 年 3 月完成,**入组 6 例**:60 个微电极植入脑表面,配无线供电的植入式脉冲发生器¹¹。",
     "厂商 2026 年 1 月的会议报告给出:**全部 6 例**视功能显著改善;设备全程可用,"
     "**失效电极少于 4%**;**1 例严重不良事件**——早期的一次癫痫发作,调参数后未再出现¹²。"
     "另两套在研系统 CORTIVIS 与 ICVP 均在招募中,各计划 5 例¹³。",
     "做 Orion 的公司,前身正是**视网膜假体 Argus II 的厂商**。2019 年 Argus II 停产时全球已有"
     "**超过 350 名**使用者;公司随后资金耗尽、裁员,植入体不再提供维修与更换¹⁴。"
     "**一个能工作的植入体,可以因为公司的经营状况变成使用者身上的死物。**"],
    P(OUT, "09-systems.png"), figure_height=370,
    title="有人体数据的,规模都是个位数", title_num="⑦",
)

# 10 ⑧
g.figure_card(
    P(FIGS, "fig-blindsight.png"), "一手信息与二手转述",
    ["上面三套都有人体数据,声量最大的那个还没有。要说的是**哪些能核实、哪些不能**。",
     "如上图,官网的一手信息只有左列这些:已获 **FDA 突破性设备认定**(2024 年 9 月);"
     "视觉试验标注为「**Upcoming trial**」,即尚未开始;技术描述只有摄像头、无线传输与植入体;"
     "适应症点名「**眼或视神经**的损伤或疾病」¹⁵。右列那些官网上都没有,来自社交媒体与媒体转述。",
     "这项认定容易被误读。FDA 指南写明:它**不改变上市许可的标准**,"
     "提供的是开发与审评期间的加速沟通通道,**不是批准**¹⁶。所以 Blindsight 目前处在"
     "**有监管通道、尚无人体数据**的阶段。"],
    P(OUT, "10-blindsight.png"), figure_height=410,
    title="Neuralink 的 Blindsight 只有一项认定", title_num="⑧",
)

# 11 收尾
g.text_card(
    "每一次进展,都来自换掉一个假设",
    ["回看这条线上的每一次实质进展,形式一样:**把一个关于皮层的错误假设换掉**。"
     "从表面电极换成皮层内穿刺电极,换掉的是「要用毫安级电流才能驱动」,阈值随之低了约三个数量级²;"
     "从同时刺激换成依次描摹,换掉的是「多个电极能拼出图案」¹⁰。",
     "现在轮到下一个:**编码方案由人来设计**。上一条路走通了,但轨迹仍要先测出光幻视图、"
     "再由人决定怎么走。而更基本的问题还没有答案——**这个系统到底能被推到哪些状态?**",
     "**本期局限**:人体证据几乎全部来自个位数被试;「电流抓住的是轴突」来自小鼠与猕猴,"
     "**在人身上尚未直接验证**;文中并列引用的**皮层内 Utah 阵列**与**硬膜下表面电极**并不可直接比较。",
     "**下一期 · 把编码交给模型去学**",
     "· 同一块阵列既刺激又记录,能不能学出「什么刺激产生什么活动」",
     "· 刺激能诱发的群体活动,被约束在多大的范围里",
     "· 记录到的活动,会比刺激参数更能预测被试看到了什么吗"],
    P(OUT, "11-closing.png"),
)

# 12 尾卡 A:同行评审文献
g.tail_card(
    ["¹ Brindley GS, Lewin WS. (1968). The sensations produced by electrical stimulation "
     "of the visual cortex. J Physiol 196:479–493.",
     "² Schmidt EM, Bak MJ, Hambrecht FT, et al. (1996). Feasibility of a visual prosthesis "
     "for the blind based on intracortical microstimulation of the visual cortex. Brain 119:507–522.",
     "³ Fernández E, Alfaro A, Soto-Sánchez C, et al. (2021). Visual percepts evoked with an "
     "intracortical 96-channel microelectrode array inserted in human occipital cortex. "
     "J Clin Invest 131:e151331.",
     "⁴ Caspi A, Barry MP, Patel UK, et al. (2021). Eye movements and the perceived location of "
     "phosphenes generated by intracranial primary visual cortex stimulation in the blind. "
     "Brain Stimul 14:851–860.",
     "⁵ Moure P, Granley J, Grani F, et al. (2026). Deep learning-based control of electrically "
     "evoked activity in human visual cortex. Neuron.",
     "⁶ Dobelle WH, Mladejovsky MG. (1974). Phosphenes produced by electrical stimulation of "
     "human occipital cortex, and their application to the development of a prosthesis for "
     "the blind. J Physiol 243:553–576."],
    P(OUT, "12-refs-a.png"),
    lead_paragraphs=["**参考来源分两个证据层级**:¹–¹⁰ 为同行评审文献,¹¹–¹⁶ 为试验注册记录、"
                     "监管文件、公司公告与媒体报道。"],
)

# 13 尾卡 B
g.tail_card(
    ["⁷ Stoney SD, Thompson WD, Asanuma H. (1968). Excitation of pyramidal tract cells by "
     "intracortical microstimulation: effective extent of stimulating current. "
     "J Neurophysiol 31:659–669.",
     "⁸ Histed MH, Bonin V, Reid RC. (2009). Direct activation of sparse, distributed populations "
     "of cortical neurons by electrical microstimulation. Neuron 63:508–522.",
     "⁹ Bosking WH, Sun P, Ozker M, et al. (2017). Saturation in phosphene size with increasing "
     "current levels delivered to human visual cortex. J Neurosci 37:7188–7197.",
     "¹⁰ Beauchamp MS, Oswalt D, Sun P, et al. (2020). Dynamic stimulation of visual cortex "
     "produces form vision in sighted and blind humans. Cell 181:774–783.e5.",
     "",
     "¹¹ ClinicalTrials.gov. NCT03344848（Orion 早期可行性研究）.",
     "¹² Vivani Medical / Cortigent 新闻稿（2026-01-29）,NANS 2026 年会报告.",
     "¹³ ClinicalTrials.gov. NCT02983370（CORTIVIS）; NCT04634383（ICVP）.",
     "¹⁴ Second Sight / Vivani 公司公告与媒体调查报道（2019–2022）.",
     "¹⁵ Neuralink 官方网站,视觉假体试验页（2026-08 访问）.",
     "¹⁶ U.S. FDA. Breakthrough Devices Program 最终指南（2023-11-14）."],
    P(OUT, "13-refs-b.png"),
)

print("done ->", OUT)

"""期二「一个阴性结果」图卡装配 (2026-08-06)。"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator  # noqa: E402

PROJECT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-06-tus-null")
FIG = os.path.join(OUT, "figs")
PAP = os.path.join(PROJECT, "papers")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.08.06")

# 01 封面
gen.cover_card(
    "超声打丘脑",
    "25 人三类读数，一项都没测到",
    "把靶点温升压在 0.5 °C 以内之后,此前报告过的效应没有出现。",
    os.path.join(OUT, "01-cover.png"),
    concept_image=os.path.join(PAP, "scott2026-cover-mri.png"),
    concept_height=700, title_top=95,
)

# 02 目录
gen.figure_card(
    os.path.join(FIG, "toc.png"), "本期路线",
    ["2026 年 8 月 bioRxiv 预印本,Stanford 与 UCSF 团队。25 名健康成人,经颅聚焦超声打"
     "外侧膝状体核(LGN,视觉通路上的丘脑中继核团),同时记录稳态视觉诱发电位与对比度"
     "增量检测行为。"],
    os.path.join(OUT, "02-toc.png"), figure_height=640,
)

# 03 WHY
gen.text_card(
    "无创把作用点送进丘脑，这个承诺兑现了吗",
    ["临床上真正想调控的脑区几乎都在深部:帕金森的丘脑底核、难治性抑郁的膝下扣带回、"
     "癫痫的海马。现在能动它们的只有深部脑刺激,代价是开颅手术加终身植入物。",
     "经颅聚焦超声要做的事很明确:**不开颅、不植入,把作用点送到深部核团**。它凭的是"
     "两条物理性质。经颅磁刺激的磁场随深度衰减很快,打深部时沿途浅层受到的刺激更强;"
     "经颅电刺激的电流大部分被头皮和颅骨分流。声波在软组织里衰减小得多,而且能聚焦——"
     "能量在焦点处叠加,路径上强度低。这项研究的换能器实测焦斑是 **0.5 × 0.5 × 2 厘米**。",
     "一篇 2022 年的系统综述统计了 35 项人体研究、677 名被试,并指出**过半的人体研究"
     "发表于 2020 年之后**¹。那么它兑现了吗。"],
    os.path.join(OUT, "03-why.png"),
)

# 04 直接回答
gen.text_card(
    "写这条路线安全标准的实验室，自己没测到效应",
    ["这项研究出自 Stanford 与 UCSF。作者中的 Kim Butts Pauly 是国际经颅超声刺激安全与"
     "标准联盟两份共识文件的作者——2024 年的**报告标准**²与 2025 年的**生物物理安全"
     "共识**³;本文引作对照的绵羊实验、以及确立平滑脉冲包络可消除听觉混淆的那项工作,"
     "同样出自她的实验室。",
     "结果是:25 名健康成人,**三类读数、在线与离线、三个参数条件,全部未检出效应**。"
     "论文摘要写的是未能检出超声对稳态视觉诱发电位幅度、潜伏期或知觉行为的任何影响,"
     "讨论部分写明三个预设假设一个都没找到证据。",
     "判据沿用上一期讲过的那套:真实的定点调控应当只出现在「打 LGN × 被超声覆盖的"
     "半视野」这一格。任何四格齐动的变化都属于全局效应,支持不了定点调控的主张。"
     "先看这一格里发生了什么。"],
    os.path.join(OUT, "04-answer.png"),
)

# 05 在线结果
gen.figure_card(
    os.path.join(PAP, "scott2026-p15-0.png"), "Fig. 6 · SSVEP 幅度",
    ["如上图,三列是三个脉冲重复频率,上排红色是未被超声覆盖的半视野,下排蓝色是被覆盖的"
     "半视野;每格三个点分别是打浅层对照、打 LGN、只放掩蔽音。纵轴为相对基线的比值。",
     "**18 个误差棒全部与 1.0 这条虚线相交**,彼此也全部重叠。关键的一项是「靶点 × "
     "半视野」交互,它检验左右差异会不会随打不打 LGN 而改变,结果是 **p = 0.763**。"
     "知觉行为的同一项是 p = 0.761。",
     "图里唯一接近显著的是半视野**主效应**(p = 0.070)。它的含义是左右两侧整体略有差别,"
     "这在任何左右对比实验里都会出现,与超声打没打中无关。在线没有,那么累积起来的后效呢。"],
    os.path.join(OUT, "05-online.png"), figure_height=560,
)

# 06 离线
gen.text_card(
    "唯一显著的下降，来自疲劳",
    ["**离线效应必须查。** 这条路线上一批被广泛引用的结果就是离线的——猕猴身上 40 秒"
     "刺激换来一小时以上的效应,人的运动皮层 80 秒换来至少 30 分钟。",
     "实验设了三个**都不开超声**的时间点,分布在整场刺激的之前、之中、之后。结果出现了"
     "整篇唯一一个显著的主效应:**成绩随时间下降(p = 0.022)**。但两半视野同步下降——"
     "半视野主效应 p = 0.725,半视野 × 时间点交互 p = 0.065,都不显著。论文的判断是这与"
     "疲劳一致。脑电侧的幅度与潜伏期则连时间效应都没有。",
     "**这一格说明了对照设计的作用。** 如果只做一个条件、只测一半视野,实验后成绩显著下降"
     "完全可以被写成超声降低了知觉敏感度。是另外半个视野同步下降,把这个解释否掉的。"
     "那会不会是平均值掩盖了个别人身上的真实效应。"],
    os.path.join(OUT, "06-offline.png"),
)

# 07 剂量-反应
gen.figure_card(
    os.path.join(PAP, "scott2026-p15-1.png"), "Fig. 7 · 剂量与效应",
    ["这个可能性必须排除。每个人的颅骨衰减不同,同样的输入进到脑内的强度差别很大——"
     "仿真估计的范围是 **8.5 到 20.5 W/cm²**。如果超声真的起作用,剂量高的人效应应当更大。",
     "**这项检验不依赖平均值。** 一个真实的物理机制,很难做到既有效又完全不随剂量变化。"
     "如上图,每个灰点是一名被试,横轴是他 LGN 处的估计强度,纵轴是他自己的交互值。",
     "**三个参数条件下拟合线的斜率符号来回翻转**(4.8 Hz 向下、48 Hz 向上、488 Hz 基本"
     "水平),R² 最高只有 0.065。行为数据在 4.8 Hz 出现过一个 p = 0.037,但那条拟合线穿过"
     "零点、方向讲不通,作者自己把它排除了。"],
    os.path.join(OUT, "07-dose.png"), figure_height=420,
)

# 08 颅骨差异
gen.text_card(
    "同一台机器，进到每个人脑里差 2.4 倍",
    ["剂量与效应无关。不过这里出现了一个更基础的问题:这个剂量估计本身可靠吗。这项研究给"
     "所有 25 名被试用的是同一个自由场强度 68 W/cm²,而实际到达 LGN 的强度估计为 "
     "**8.5 到 20.5 W/cm²,最高的人是最低的人的 2.4 倍**。",
     "后果比它听上去严重。剂量说不清,实验之间就无法比较:同一个协议在甲身上可能不够、"
     "在乙身上可能过量,两人的数据却被平均在一起。**阴性结果可能只是没打够,阳性结果可能"
     "来自个别打得特别足的人。**",
     "临床上这件事直接决定成败。经颅磁共振引导聚焦超声治疗震颤时,25 名患者的回顾分析显示"
     "**颅骨密度比与靶点最高温度正相关(r² = 0.263)**⁴——颅骨性质单独就解释了靶点温度约"
     "四分之一的变异,条件差的患者加到额定功率也烧不上去。差别这么大,来源却相当集中。"],
    os.path.join(OUT, "08-skull-variability.png"),
)

# 09 颅骨机制
gen.figure_card(
    os.path.join(FIG, "fig-skull.png"), "颅骨的三层结构",
    ["如上图,成人颅骨是三层:外板与内板是致密的皮质骨,中间的**板障**是多孔的松质骨。"
     "1978 年在新鲜人颅骨上逐层切开测量的经典工作给出结论:**决定成人颅骨声学损耗的"
     "主导因素是中间这层板障**⁵。",
     "**多孔是关键。** 声波在孔隙构成的微结构里被**散射**,方向被打乱;在孔隙界面上还发生"
     "**纵波与横波之间的模式转换**,而转成横波的能量基本无法再有效传入脑内。板障的厚度与"
     "孔隙率,在人与人之间差别最大。",
     "领域的应对分两步。个体化建模:颅骨声学性质可从高分辨率影像反推,用于逐阵元的相位"
     "校正⁶。报告规范:国际共识把脑内原位剂量估计列为必报项²——只报自由场强度等于没报"
     "剂量。剂量之后,还有位置。"],
    os.path.join(OUT, "09-skull-mechanism.png"), figure_height=470,
)

# 10 靶点核查
gen.figure_card(
    os.path.join(PAP, "scott2026-p20-1.png"), "Fig. 13 · 靶点核查",
    ["阴性结果绕不开这个问题:如果根本没打中,没有效应就只等于没打中。换能器位置全程由"
     "神经导航在线记录,可按实测位置重跑仿真。",
     "如上图,红色椭圆是跨被试平均的声束半高全宽轮廓,黑十字是焦点峰值,灰圆是各人的 LGN。"
     "**除两名被试外,LGN 都落在半高全宽体积之内。** 但灰圆整体偏在十字右侧,焦点峰值"
     "比 LGN 略浅,因为 70 毫米已是这个换能器的最大转向深度。",
     "把几个尺度并起来看,容错空间就清楚了:**LGN 直径约 0.5 厘米,焦斑横向宽度 0.5 厘米,"
     "红外神经导航的定位误差约 0.5 厘米**⁷。论文如实承认,他们没有靶点准确性的实测证据,"
     "有可能在一部分被试身上没打中。"],
    os.path.join(OUT, "10-targeting.png"), figure_height=420,
)

# 11 温度（核心）
gen.text_card(
    "压住温度，是为了证明机械作用",
    ["剂量、位置都追问过了。剩下的那一项,是论文自己抛出来的。这条路线七十年来把不发热"
     "当成必须守住的底线。原因很直接:一旦加热,测到的神经活动变化就能被解释成温度所致,"
     "而机械作用是这条路线的核心主张。",
     "这项研究把温度压得很低,而且是刻意的:热学仿真显示靶点**最大温升 0.5 °C、热剂量 "
     "CEM43 低于 0.25**,远低于国际共识的非显著风险阈值³。",
     "问题在于,丘脑对极小的升温就很敏感。论文引用的证据是丘脑对 **0.5 至 1 °C** 的"
     "升温即高度敏感,那篇工作的标题本身就主张聚焦超声的可逆神经抑制由热机制介导⁸。而论文"
     "接着写道:1958 年那项猫的经典实验⁹与 2022 年他们自己的绵羊实验¹⁰,用的强度与占空比"
     "都高于人体研究常用值,因此靶点温度很可能是升高的。",
     "**避免发热本是为了证明机械作用。而当温度被彻底压住之后,效应也一起消失了。**"],
    os.path.join(OUT, "11-temperature.png"),
)

# 12 边界
gen.text_card(
    "这个结果否掉了什么，没否掉什么",
    ["上面那句话很容易被读过头,所以边界要划清楚。**它否掉的是**:在这组参数、这个靶点、"
     "这几个读数下,不存在稳健且可重复的效应。前作报告的效应被描述为可逆抑制、跨个体高度"
     "可重复,若真是那个量级,这项研究应当看得见。",
     "**它没有否掉**:更高的剂量、更精确的定位、更长时间尺度的后效、以及微弱效应。同年"
     "另一项人体研究用 256 阵元相控阵配合扫描仪内定位,在同一靶点报告了效应¹¹,硬件条件"
     "与本研究相差一个代际。",
     "**作者本人把话说得更满**:他们主动指出所用仿真软件可能高估了脑内强度,并写道若有实测"
     "的剂量与靶点作用证据,效应有可能在他们的数据里被揭示出来。在阴性结果论文里主动说自己"
     "可能漏检,这个坦率程度不多见。"],
    os.path.join(OUT, "12-boundary.png"),
)

# 13 尾卡一
gen.tail_card(
    ["¹ Sarica C, et al. (2022). Human studies of transcranial ultrasound neuromodulation: "
     "a systematic review of effectiveness and safety. Brain Stimul 15:737–746.",
     "² Martin E, et al. (2024). ITRUSST consensus on standardised reporting for "
     "transcranial ultrasound stimulation. Brain Stimul 17:607–615.",
     "³ Aubry JF, et al. (2025). ITRUSST consensus on biophysical safety for transcranial "
     "ultrasound stimulation. Brain Stimul 18:1896–1905.",
     "⁴ Chang WS, et al. (2016). Factors associated with successful magnetic "
     "resonance-guided focused ultrasound treatment. J Neurosurg 124:411–416.",
     "⁵ Fry FJ, Barger JE. (1978). Acoustical properties of the human skull. "
     "J Acoust Soc Am 63:1576–1590."],
    os.path.join(OUT, "13-tail-1.png"),
    lead_paragraphs=[
        "这条路线要往前走,缺的东西作者自己指出来了:**实测的剂量与靶点作用证据**。目前"
        "所有人报的脑内剂量都来自仿真,而仿真对焦点位置预测得好、对剂量预测得没那么好。",
        "在拿到实测之前,一项阳性结果和一项阴性结果之间,很难判断分歧究竟出在生物学,"
        "还是出在剂量。"],
)

# 14 尾卡二
gen.tail_card(
    ["⁶ Aubry JF, et al. (2003). Experimental demonstration of noninvasive transskull "
     "adaptive focusing based on prior computed tomography scans. J Acoust Soc Am 113:84–93.",
     "⁷ Phipps MA, et al. (2024). Practical targeting errors during optically tracked "
     "transcranial focused ultrasound using MR-ARFI and array-based steering. "
     "IEEE Trans Biomed Eng 71:2740–2748.",
     "⁸ Darrow DP, et al. (2019). Reversible neuroinhibition by focused ultrasound is "
     "mediated by a thermal mechanism. Brain Stimul 12:1439–1447.",
     "⁹ Fry FJ, Ades HW, Fry WJ. (1958). Production of reversible changes in the central "
     "nervous system by ultrasound. Science 127:83–84.",
     "¹⁰ Mohammadjavadi M, et al. (2022). Transcranial ultrasound neuromodulation of the "
     "thalamic visual pathway in a large animal model and the dose-response relationship "
     "with MR-ARFI. Sci Rep 12:19588.",
     "¹¹ Martin E, et al. (2025). Ultrasound system for precise neuromodulation of human "
     "deep brain circuits. Nat Commun 16:8024.",
     "主文章 Scott MTW, et al. (2026). Effects of transcranial focused ultrasound "
     "stimulation to human lateral geniculate nucleus on visual perception and steady-state "
     "visual evoked potentials. bioRxiv 10.64898/2026.07.30.741804."],
    os.path.join(OUT, "14-tail-2.png"),
)

print("done ->", OUT)

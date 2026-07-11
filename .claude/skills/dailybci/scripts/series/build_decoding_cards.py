import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from card_generator import CardGenerator

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-decoding-four-axes")
FIG = os.path.join(OUT, "figs")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.06.26", platform="xiaohongshu")

gen.cover_card(
    "神经解码的四个轴",
    "一张坐标系读懂任何方法",
    "把看似几十种的神经解码方法,压成四条**互相独立**的轴——掌握它们,见到任何方法都能一秒定位。",
    os.path.join(OUT, "01-cover.png"),
    source="方法论特别篇 · 不绑某篇论文。四条轴:① 信号模态(从什么信号读)② 解码目标(读出什么数学对象)③ 编码层级(信息住在哪层)④ 模型类别(映射什么形式)。下面逐轴从第一性原理拆开。",
)

gen.figure_card(
    os.path.join(FIG, "fig0-overview.png"), "四轴总览",
    [
        "先把整张地图铺开:一个解码器,本质就是 神经信号 → 你想读出的量 的一个映射。",
        "如上图,四条轴各管一个问题、各有分枝;任何具体方法 = 每条轴上**各取一个点**的组合。",
        "四轴互相独立、自由组合。下面从第一条轴——你从什么信号读起——开始。",
    ],
    os.path.join(OUT, "02-overview.png"), figure_height=470,
)

gen.figure_card(
    os.path.join(FIG, "figA-gradient.png"), "轴 A · 信号模态",
    [
        "第一条轴问:**从什么信号读**。底层只有两个源——神经元的电活动(快),和它带来的血流(慢)。",
        "如上图,沿电活动这一支,**离神经元越远、信号被空间平均得越厉害**:皮层内能分辨单神经元(~50–150 µm¹),ECoG 只剩局部群体(~1–5 mm¹),头皮 EEG 是大群体(~cm²)。距离一个量,同时定了空间分辨率和你能触及的编码层。",
        "血流那一支空间可细到 µm–mm,但时间被锁在秒级³⁴⁵。信号定了,接着问:读成什么?",
    ],
    os.path.join(OUT, "03-axisA.png"), figure_height=460,
)

gen.figure_card(
    os.path.join(FIG, "figB-reg-vs-clf.png"), "轴 B · 解码目标",
    [
        "信号有了,第二条轴问:**输出是什么数学对象**——这决定它是回归还是分类。",
        "如上图,**本质区别不是答案多少个,而是输出空间有没有度量**。左:连续输出有距离,能说『差多远』→ 用距离打分(回归);右:裸标签之间没有距离,只能问『多有信心是它』→ 用概率打分(分类)。",
        "关键在底部:两者同源——都在估计 p(y|x)、最大化对真答案的信心(极大似然)⁶;生成/重建只是它们的高阶组合。接着问:信息住在哪层?",
    ],
    os.path.join(OUT, "04-axisB.png"), figure_height=470,
)

gen.figure_card(
    os.path.join(FIG, "figC-manifold.png"), "轴 C · 编码层级",
    [
        "第三条轴问:**信息住在哪一层**——单个神经元的调谐,还是一大群的集体模式。**两层都真实,不是谁取代谁。**",
        "如上图左,**单神经元层**有深厚历史:V1 的朝向调谐、M1 的方向调谐都来自个体细胞,把许多细胞的调谐**加权求和(群体矢量)**就能解码,在低级皮层至今有力。上图右是**群体层**:整群瞬时活动看成 N 维空间一个点,因高度相关被压在**低维流形**上。",
        "用哪一层,取决于模态与脑区:要下到单神经元必须皮层内,非侵入只能停在群体层;群体层的低维流形还能跨年稳定⁷。最后一问:用什么数学形式读?",
    ],
    os.path.join(OUT, "05-axisC.png"), figure_height=430,
)

gen.figure_card(
    os.path.join(FIG, "figD-nonlinearity.png"), "轴 D · 模型类别",
    [
        "最后一条轴问:线性还是非线性?更准的问法是——**到底需不需要非线性?**",
        "如上图:**信息若已线性可读,就根本不需要**。发放率→运动方向近似线性,线性解码器**直接读**(①,如群体矢量)。只有当判别信息藏在信号的**高阶结构**里(如 EEG 的频带功率 = 电压的二次量),才必须先做一步**固定的非线性变换**(算功率/协方差)把它摊成线性可读(②),或干脆交给**训练出的非线性网络**(③)。",
        "所以看任何解码器先问:需不需要非线性?需要的话,它住在固定特征变换里、还是训练模型里?神经解码里线性常常够用——因为很多编码本就近似线性可读。",
    ],
    os.path.join(OUT, "06-axisD.png"), figure_height=430,
)

gen.tail_card(
    [
        "¹ 皮层内/ECoG 分辨率:Human intracortical recording & neural decoding review, PMC5815832",
        "² EEG 分辨率:EEG-Based BCIs review, PMC5839510",
        "³ fNIRS:Pinti et al. 2020, Ann. N.Y. Acad. Sci.",
        "⁴ 7T fMRI 亚毫米:Simultaneous EEG-fMRI at 7T, PMC12587055",
        "⁵ fUS:Functional ULM, Nature Methods, 2022",
        "⁶ 回归/分类同源(极大似然):Bishop, Pattern Recognition & Machine Learning, 2006",
        "⁷ 群体流形与跨年稳定:Gallego et al., Neuron 2017 / Nat Neurosci 2020",
    ],
    os.path.join(OUT, "07-tail.png"),
    lead_paragraphs=[
        "四条轴互相独立、自由组合。领域里真正的功夫,往往不在'又发明一种方法',而在**四个抉择**上见高下:",
        "**用什么信号源**换来什么时空分辨率(A);**把意图读成哪种数学对象**(B);**下沉到哪一层去读**——单个神经元还是群体(C);**让非线性住在特征里还是模型里**(D)。",
        "读懂一种神经解码,就是看清它在这四处各自怎么取舍。把它钉到这四条轴上,它便不再神秘。",
    ],
)

print("cards written to", OUT)

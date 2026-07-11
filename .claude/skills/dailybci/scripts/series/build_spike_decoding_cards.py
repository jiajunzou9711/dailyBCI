import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from card_generator import CardGenerator

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(os.path.dirname(HERE))
PROJECT = os.path.abspath(os.path.join(SKILL, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-spike-population-decoding")
FIG = os.path.join(OUT, "figs")
os.makedirs(OUT, exist_ok=True)

gen = CardGenerator(date="2026.06.27", platform="xiaohongshu")

# 01 cover
gen.cover_card(
    "群体 spike 解码",
    "一条把『编码』用到尽的脊柱",
    "从最朴素的群体矢量,到逼近信息极限的贝叶斯——同一条主线:**把神经元的编码模型用得越来越足**。",
    os.path.join(OUT, "01-cover.png"),
    source="方法论特别篇 · 不绑某篇论文。只讲**生成式**一支:先弄清『神经元如何编码』,再反推出意图;判别式(SVM/RNN 等)留待下篇。主要参考 Dayan & Abbott《Theoretical Neuroscience》第 3 章。",
)

# 02 material
gen.figure_card(
    os.path.join(FIG, "fig01-material.png"), "原料 · r(t)",
    [
        "先把原料钉死:群体里 N 个神经元,各自吐出**动作电位序列**——一串离散的放电时刻。",
        "如上图,要做数学第一步是**分箱**:在每个时间窗里数每个神经元发了几个动作电位,得到一个 N 维**发放率向量 r**;时间推进就是一串 r(t)。",
        "这个 r(t) 是群体解码**唯一的原料**。解码 = 找一个映射 **r → 意图 z**。整条脊柱都在回答:这个映射怎么造。",
    ],
    os.path.join(OUT, "02-material.png"), figure_height=440,
)

# 03 purpose (text)
gen.text_card(
    "为什么这么做:解码是验证编码的工具",
    [
        "造映射之前先问:为什么这么做?生成式这条线的**科学目的是搞懂编码**——神经元到底如何把外界变量变成放电。",
        "解码在这里是**验证编码的工具**:若能从放电把意图读回来,就反过来支持『信息确实在那、这个编码描述站得住』。",
        "但要守住一步:**解码准 ≠ 证明大脑就是这么编、这么读的**(够用 ≠ 唯一机制)。守住这条,开始爬脊柱。",
    ],
    os.path.join(OUT, "03-purpose.png"),
)

# 04 spine overview
gen.figure_card(
    os.path.join(FIG, "fig03-spine.png"), "脊柱总览",
    [
        "整条脊柱只有四级:**群体矢量 → OLE → ML → 贝叶斯**。",
        "如上图,从下往上,每一级都是上一级**某条简化假设被松开**:先只用偏好方向,再用相关结构,再用完整噪声,最后加上先验。",
        "主线就一句:**把编码模型用得越来越足**。先看最朴素的底座——群体矢量。",
    ],
    os.path.join(OUT, "04-overview.png"), figure_height=500,
)

# 05 population vector
gen.figure_card(
    os.path.join(FIG, "fig04-popvector.png"), "第一级 · 群体矢量",
    [
        "第一级**群体矢量**:最朴素的反推。",
        "如上图,每个神经元朝自己的**偏好方向**(放电最猛的方向)投一票,长度 = 当前发放率;把所有矢量**加起来**,合矢量指向的就是解码出的方向。",
        "它能 work,但**暗含假设:神经元均匀铺开、互不相关、同样可靠**(Q∝I)。真实数据这三条都破——于是要把权重选对。",
    ],
    os.path.join(OUT, "05-popvector.png"), figure_height=480,
)

# 06 OLE
gen.figure_card(
    os.path.join(FIG, "fig05-ole.png"), "第二级 · OLE",
    [
        "第二级 **OLE(最优线性估计)**:不再写死贡献方向。",
        "如上图,它用**最小二乘**解出每个神经元的最优权重 **w = Q⁻¹L**:L 是各神经元的调谐(信号),**Q⁻¹** 是发放率相关矩阵的逆,**给冗余、相关的神经元降权**,不让同一份信息被重复计数。",
        "但 OLE 只用了放电的**均值与相关(二阶统计)**,等于暗设高斯噪声,没用上噪声的真实形状。下一级补这个缺口。",
    ],
    os.path.join(OUT, "06-ole.png"), figure_height=460,
)

# 07 ML
gen.figure_card(
    os.path.join(FIG, "fig06-ml.png"), "第三级 · ML",
    [
        "第三级 **ML(最大似然)**:把**完整的 p(r|s)** 用起来。",
        "如上图,真实动作电位计数接近 **Poisson**。ML 在所有可能意图里挑那个『让实测放电最可能发生』的;它对放电**天然非线性**,且有个反直觉结论——**信息藏在调谐曲线最陡处,不在峰顶**(意图稍动,陡坡上放电变化最大)。",
        "数据够多时,ML **渐近逼近信息天花板**(Cramér–Rao)。只差最后一块:先验。",
    ],
    os.path.join(OUT, "07-ml.png"), figure_height=460,
)

# 08 Bayesian
gen.figure_card(
    os.path.join(FIG, "fig07-bayes.png"), "第四级 · 贝叶斯",
    [
        "第四级 **MAP / 完整贝叶斯**:把手头剩下的信息也用上。",
        "如上图,若我们对意图本就有**先验**(并非全然无知),贝叶斯把它乘进来:**后验 = 似然 × 先验**(成正比)。取后验峰值 = MAP;保留**整条后验** = 完整贝叶斯,还附带**不确定度**。",
        "至此脊柱收口:从偏好方向,一路用到相关、噪声、先验——信息**用到最尽**。",
    ],
    os.path.join(OUT, "08-bayes.png"), figure_height=430,
)

# 09 tail
gen.tail_card(
    [
        "¹ Dayan & Abbott. Theoretical Neuroscience. MIT Press, 2001(第 3 章 群体解码:群体矢量 / OLE / ML / 贝叶斯)",
        "² Georgopoulos, Schwartz & Kettner. Science, 1986(群体矢量 population vector)",
        "³ Bishop. Pattern Recognition and Machine Learning. Springer, 2006(生成式与极大似然)",
    ],
    os.path.join(OUT, "09-tail.png"),
    lead_paragraphs=[
        "回看整条脊柱,主线只有一句:**把编码模型用得越来越足**。群体矢量用偏好方向,OLE 加相关,ML 加完整噪声,贝叶斯加先验与不确定度——每一级都不是新发明,而是上一级某条假设的松绑。",
        "也别忘那条澄清:这一支的产品是**理解编码**;解码得好,说明信息在那、模型站得住,但不替你证明大脑真实的读出方式。",
        "而这只是**生成式**半张地图。对面还有**判别式**——SVM、逻辑回归、RNN,它们绕过编码模型、直接拟合 r→z,是另一套逻辑。那是下一篇的事。",
    ],
)

print("cards written to", OUT)

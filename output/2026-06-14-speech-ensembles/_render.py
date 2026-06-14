import sys, os
sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator

OUT = "output/2026-06-14-speech-ensembles"
FIG = "papers"
gen = CardGenerator(date="2026.06.14", platform="xiaohongshu")

# 1 — cover (hook title + provenance/author block)
gen.cover_card(
    "能用意念“说话”之后",
    "下一关是“别说错字”",
    "脑机接口已能让瘫痪者每分钟说约 65 个词;难点变成了准确率——错一个关键词,整句意思就翻车。",
    f"{OUT}/01-cover.png",
    source=(
        "2026 年 6 月 · bioRxiv 预印本《Neural decoding of speech using deep neural ensembles》。"
        "Stanford / UC Davis / BrainGate 团队,通讯作者 Francis Willett"
        "(Stanford 神经假体实验室——2023 年 62 词/分语音 BCI 的一作)。"
        "方法:让十个解码器集成“投票”,并提出“伪集成”降算力。"
    ),
)

# 2 — text: bottleneck is errors
gen.text_card(
    "瓶颈不是速度,是“错字”",
    [
        "现在让瘫痪者“开口”,速度已能到每分钟约 65 个词,接近正常说话。",
        "卡住的是准确率——而且错误不平等:高频虚词错了影响不大,错一个承载意思的关键词,整句就翻车。",
        "论文里的例子:“sixty(六十)”被解成“six(六)”;“reference(参考)”被解成“weapon(武器)”。",
    ],
    f"{OUT}/02-text.png",
)

# 3 — figure Fig.1c (leaderboard) + what is ensemble; text points at the figure
gen.figure_card(
    f"{FIG}/speech-ensembles-fig1c.jpg",
    "Fig. 1c 丨脑信号转文字竞赛榜单(红=集成方法)",
    [
        "如上图,错误率最低的几根柱子——LightBeam 4.98、BraIn-to-text 5.10——全是红色(集成方法);灰色单模型(如 Baseline GRU 9.76)明显更高。",
        "什么是集成?同一个解码器从十个不同随机起点各训一遍,各自在不同地方犯错;十个一起出结果、再由一个“裁判”大模型合成一句,随机错被投票抵消。",
        "(跑赢基线的 9 个方法里,7 个用了集成。)",
    ],
    f"{OUT}/03-figure1.png",
)

# 4 — text: why not used before
gen.text_card(
    "这么好,为什么一直没真用上?",
    [
        "1丨从没在实时闭环里验证过——之前都是离线刷榜:数据录好慢慢算,要多少时间和算力都有。真用时人要边想边说、即时看到反馈,离线赢≠在线能用。",
        "2丨太贵——十个解码器同时跑,这篇直接铺了 20 台云服务器。",
        "3丨慢——把十句合成一句要花时间。",
    ],
    f"{OUT}/04-text.png",
)

# 5 — figure Fig.2a (system diagram) + how + result; text walks the diagram
gen.figure_card(
    f"{FIG}/speech-ensembles-fig2a.jpg",
    "Fig. 2a 丨本地即时 + 云端集成的闭环架构",
    [
        "如上图左半“边说边解码”:本地一个解码器把神经信号转成即时的部分文字(“hello…”),神经数据同时经 VPN 持续上云。",
        "右半“说完再定稿”:云端十个解码器的集成各出一个假设,最后由 Merger 大模型合成最终那句(“Hello world!”)。",
        "靠这个分工,大词表错误率 33.7%→26.0%,语速没掉(约 65 词/分)。(被试 T12:6 片 64 通道皮层内微电极阵列,扎进双侧语音运动皮层。)",
    ],
    f"{OUT}/05-figure2.png",
)

# 6 — text: the cost + lead into pseudoensemble
gen.text_card(
    "代价:每句多等 5.25 秒",
    [
        "精度是用延迟换的:集成让“最终那句话”平均晚 5.25 秒才出现,其中“裁判”大模型占最大头(约 2.77 秒)。论文没回避这笔账。",
        "但作者紧接着问:能不能不用十个解码器,也拿到集成的好处?他们的答案,叫“伪集成”——",
    ],
    f"{OUT}/06-text.png",
)

# 7 — figure Fig.4c-f (bars) + pseudoensemble; text points at the bars
gen.figure_card(
    f"{FIG}/speech-ensembles-fig4cf.jpg",
    "Fig. 4c–f 丨基线 vs 完整集成 vs 伪集成(四名被试)",
    [
        "如上图,每名被试三根柱:灰=不集成(基线)、红=完整集成、紫=伪集成。红柱总是最低,集成确实更准(如 T16:20.6%→14.2%)。",
        "紫柱(伪集成)落在灰、红之间:只用一个解码器、给输入加随机噪声造出多样性,就追回完整集成三到六成的收益,算力却降一个量级——为床旁、断网场景铺路。",
    ],
    f"{OUT}/07-figure4.png",
)

# 8 — tail
gen.tail_card(
    [
        "¹ Yoon et al., bioRxiv 2026",
        "   Neural decoding of speech using deep neural ensembles",
        "   (作者声明为首次实时闭环验证)",
        "",
        "² Willett et al., Nature 2023",
        "",
        "³ Card et al., NEJM 2024",
    ],
    f"{OUT}/08-tail.png",
)

print("done")

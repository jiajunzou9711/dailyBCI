# -*- coding: utf-8 -*-
"""日报 2026-10-10 · 光遗传视觉修复（Sahel 2021 Nat Med；NEJM 2026 仅用摘要）—— 卡片生成
用法：python3 build_optovision_cards.py [卡片文件名 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
EP = os.path.join(PROJ, "output", "2026-10-10-optogenetic-vision")
FIG = os.path.join(EP, "figs")
OUT = os.path.join(EP, "cards"); os.makedirs(OUT, exist_ok=True)
def f(n): return os.path.join(FIG, n + ".png")

only = set(sys.argv[1:])
def want(name): return not only or name in only

gen = CardGenerator(date="2026.10.12")

if want("01-cover.png"):
    gen.cover_card("一针病毒加眼镜", "盲人能找到物体",
                   "一名晚期视网膜色素变性患者接受光遗传注射，戴上刺激眼镜后，在 **92%** 的试次中找到并摸到了桌上的笔记本¹。",
                   os.path.join(OUT, "01-cover.png"),
                   concept_image=f("cover"), concept_height=420, title_size=120, title_top=70,
                   source="2021 年 5 月 Nature Medicine《Partial recovery of visual function in a blind patient after optogenetic therapy》· Sahel & Roska")

if want("02-toc.png"):
    gen.figure_card(f("toc"), "本期路线", [
        "2021 年 5 月 24 日，Nature Medicine 在线发表《Partial recovery of visual function in a blind patient after optogenetic therapy》。通讯作者 José-Alain Sahel（Institut de la Vision，巴黎；匹兹堡大学眼科）与 Botond Roska（巴塞尔分子与临床眼科研究所）。Roska 组 2008、2010 年曾在小鼠上把光敏通道分别装在 ON 双极细胞与残存视锥上。",
        "方法：PIONEER 试验中 1 名晚期 RP 患者，单眼玻璃体内注射编码 ChrimsonR 的 AAV，配合投光眼镜，做三项视觉测试并同步记录头皮脑电。"],
        os.path.join(OUT, "02-toc.png"), figure_height=560, annot_size=27)

C = [
 dict(n="①", t="视网膜色素变性晚期，感光细胞死了，下游还在", fig="retina_rp", lab="示意图：视网膜的三级结构（自制）", fh=430, out="03.png", a=[
   "视网膜色素变性（retinitis pigmentosa, RP）是一类遗传性致盲病，已知致病基因超过 71 个，全球患者超过 200 万¹。",
   "如上图，视网膜对光的处理分三级。RP 损毁的主要是最下面的感光细胞：到了晚期，感光细胞大量死亡，眼睛对光失去反应，上面两级和视神经在相当程度上还存活。",
   "致病基因这么多，很难逐个做基因替代。目前获批的只有针对 RPE65 这一个基因的疗法¹。"]),
 dict(n="①", t="人体修复靠植入电极，光遗传仍停在动物实验", out="04.png", a=[
   "下游细胞既然还在，一条思路是绕过死掉的感光细胞，直接给存活的视网膜通电。",
   "- **Argus II**：外置摄像头采集画面，处理器驱动贴在视网膜表面的 60 个电极。多中心试验纳入 30 名盲人，以 RP 患者为主²；2013 年获 FDA 批准。这篇试验论文的作者里，就有本期主论文的通讯作者 Sahel²。",
   "- **PRIMA**：把光伏芯片植入视网膜下方。病种换成了地图状萎缩，满 12 个月随访的 32 人中，26 人视力改善达到有临床意义的标准³。",
   "这两种方案都要通过手术把电极放进眼内。",
   "另一条思路是光遗传（optogenetics）：把一种光门控离子通道的基因送进存活的神经元，让它们直接对光产生反应。小鼠⁴与活体猕猴⁵中已有证据，在盲人身上能否恢复可用的视觉，此前没有答案。"]),
 dict(n="②", t="本周 NEJM 报告了 10 名患者的安全性与光敏度", out="05.png", a=[
   "2026 年 10 月 7 日，Sahel 与 Roska 领衔的团队在 NEJM 发表了 PIONEER 试验 10 名晚期 RP 患者的结果⁶。论文摘要报告：",
   "- **安全性（主要终点）**：10 人中有 9 人出现眼部不良事件，其中 1 例为严重事件：注射后视网膜中央动脉一过性阻塞，用药后数分钟内缓解⁶。",
   "- **光敏度**：7 人光敏度提高，提高幅度为 2.0 到 62.3 倍；其中 6 人的提高达到有临床意义的程度⁶。",
   "这项研究测的是光敏度。患者能不能用恢复的信号找到、数出、摸到物体，要回到 2021 年《Nature Medicine》上的第一例报告¹。作者称，这是神经退行性疾病中光遗传治疗后出现部分功能恢复的首例报告¹。"]),
 dict(n="②", t="PIONEER 试验先看安全，再看患者能否看见", out="06.png", a=[
   "- **试验设计**：PIONEER 由 GenSight Biologics 发起，是多中心、开放标签、非随机的 1/2a 期剂量递增试验¹。",
   "- **目的**：主要检验「病毒载体注射 + 刺激眼镜」是否安全、能否耐受；次要比较戴镜和不戴镜时的视觉与视觉运动功能¹。",
   "- **为什么只报告一人**：截至 2020 年底已有 7 名患者接受注射。受新冠疫情影响，只有这一名完成了注射后的持续训练（共 15 次），其余患者还没能做功能评估¹。",
   "- **这名患者**：男性，58 岁，确诊 RP 40 年，入组时视力只剩光感，致病基因为 USH2A¹。",
   "戴上眼镜后，他在 **92%**（36/39）的试次里感知、定位并摸到了桌上的笔记本；不戴眼镜时，每个物体与对比度的组合只试了 1 次，都没有感知到¹。这一水平和 Argus II 相近，能找到、定位较大的物体²，还谈不上看清细节。PRIMA 的病种和衡量指标都与此不同，后文再逐项对照。"]),
 dict(n="③", t="一次眼内注射，让中央凹的神经节细胞表达 ChrimsonR", fig="retina_opto", lab="示意图：注射与刺激的位置（自制）", fh=340, out="07.png", a=[
   "ChrimsonR 是一种红移的通道视紫红质，即光门控阳离子通道：受光时通道打开，细胞去极化并发放动作电位。它最敏感的波长约 590 nm，琥珀光比蓝光对视网膜更安全，引起的瞳孔收缩也更少¹。",
   "如上图，编码 ChrimsonR 的基因装进改造过的 AAV2.7m8，在视力较差的眼做一次玻璃体内注射（5.0×10¹⁰ 个病毒基因组），主要感染中央凹的神经节细胞¹。剂量先在非人灵长类上确定；这名患者 84 周随访中没有出现眼内炎症或其他不良事件¹。",
   "注射后 4.5 个月开始训练。这些细胞要被激活，光要足够强，波长要接近 590 nm。"]),
 dict(n="③", t="眼镜把画面中的亮度变化转成 595 nm 光脉冲", fig="ed1b", lab="Extended Data Fig. 1b：头戴单元正面与背面", fh=300, out="08.png", a=[
   "如上图，眼镜正面中央是相机，背面对着治疗眼的是投影器¹。需要眼镜有两个原因：",
   "1. **光强**：非人灵长类中，表达 ChrimsonR 的神经节细胞要到 10¹⁵ photons·cm⁻²·s⁻¹ 才开始被激活，眼镜的输出范围按此设定¹。",
   "2. **波长**：光源峰值 595 nm，对准 ChrimsonR 的敏感峰¹。",
   "相机每个像素只在亮度变化超过阈值时报告一个事件，有事件的位置投一个 16.6 ms 的光脉冲¹。所以患者收到的画面只有一种颜色、每个点只有亮和灭两档。他能用这样的画面做到什么，下面三项测试给出了答案。"]),
 dict(n="④", t="戴镜后能找到较大的物体，物体变小或变多时成功率明显下降", fig="t1", lab="Table 1（戴镜、只用治疗眼的三列）", fh=430, out="09.png", a=[
   "注射后 4.5 个月开始训练，又过约 7 个月，患者才报告戴镜后视觉有改善¹。如上表：",
   "- 笔记本：感知、定位、触摸合计成功 **36/39（92%）**；",
   "- 订书钉盒：**16/45（36%）**，物体大小的影响显著（P<0.001）；对比度从 40% 到 100% 无显著差别¹。",
   "桌上放 2 到 3 个杯子时，他数对 12/19 次¹。不戴镜的两种条件（表中略去）每格只试 1 次，都是 0/1¹。下一项测试在他作答的同时记录了脑电。"]),
 dict(n="④", t="戴镜时他回答「有」，绝大多数时候桌上确实有杯子", fig="t3", lab="Table 3（戴镜、只用治疗眼的三列）", fh=330, out="10.png", a=[
   "桌上 80 cm 处放或不放一个杯子，患者睁眼后有 15 秒按键回答有或无¹。如上表：有杯子的 32 次里他答「有」21 次，没杯子的 31 次里误答「有」3 次¹。按此计算，他每次答「有」，87.5% 的时候桌上确实有杯子（自算，原文未直接给出）。",
   "不戴镜时（表中略去），他答「有」的次数在有杯子和没杯子时一样多，3 对 3、2 对 2¹。",
   "论文报告的戴镜正确率是 41%，低于 50%：没作答被计为错误，而他看不到时多半不按键¹。"]),
 dict(n="④", t="戴镜睁眼时，从枕区脑电能解码出桌上有没有杯子", fig="f2b", lab="Fig. 2b", fh=400, out="11.png", a=[
   "脑电用 48 通道非侵入式头皮 EEG 记录。作者只取枕区（O1、Oz、O2，位于视皮层上方）α 频段（8–14 Hz）的功率，训练线性分类器区分有无杯子¹。",
   "如上图，最左一柱是戴镜睁眼，准确率 **78%**，显著高于红色虚线标出的 50%；戴镜闭眼降到 39%，不戴镜四组都不显著¹。有杯子时枕区 14 Hz 的 α 功率下降，论文解释为视皮层兴奋性升高、刺激被感知的标志¹。",
   "闭眼对照提示，解码依赖眼睛收到的光。把这些结果放到电极方案旁边，就能看出它处在什么水平。"]),
 dict(n="⑤", t="光遗传目前的效果和 Argus II 在同一层级", fig="table10", lab="三种方案的对照（自制，数据见各文献）", fh=520, out="12.png", a=[
   "如上表，光遗传的物体任务目前只有一名患者的数据¹，达到的程度是找到、定位较大的物体，与 Argus II 相近²。PRIMA 以视力表视力改善为主要终点，32 人中 26 人达标，但它的患者周边视力还在，芯片只补中央³⁷。几项试验的病种、人数和指标都不同，这张表只能比较层级，不能排出高下。",
   "同一试验在 2026 年的 NEJM 上报告了 10 名患者，测的是安全性与光敏度；据摘要，物体任务未作报告⁶。"]),
 dict(n="⑤", t="光遗传省去了植入手术，但注射本身也有风险", out="13.png", a=[
   "两条路线都不依赖患者携带的是哪种基因突变。第一个差别在创伤：",
   "- **PRIMA**：要通过手术把芯片放到视网膜下方。首次人体试验中，5 人里有 2 人芯片位置偏离，一人进了脉络膜，一人偏离中心 2 mm⁷。38 人的试验里，19 人共发生 26 起严重不良事件，其中 81% 发生在术后 2 个月内³。",
   "- **光遗传**：只需一次玻璃体内注射，不植入任何硬件¹。但注射同样有风险：NEJM 的 10 人中，1 人注射后出现视网膜中央动脉一过性阻塞⁶。",
   "第二个差别在信号从视网膜的哪一级进入。"]),
 dict(n="⑤", t="ChrimsonR 装在神经节细胞上，视网膜内部的处理被跳过", fig="pathway", lab="示意图：两条通路的对比（自制）", fh=560, out="14.png", a=[
   "如上图，正常视觉中光先经感光细胞、双极细胞再到神经节细胞；本篇让神经节细胞直接感光，前两级被跳过¹，ON / OFF 分化、中心-周边拮抗和颜色处理也随之缺失。",
   "早年的动物研究曾把通道装在 ON 双极细胞⁸ 或残存视锥⁹ 上，目的就是保留更多视网膜内部的处理。本篇没有说明为什么选神经节细胞。这些比较都建立在一名患者的数据上。"]),
 dict(n="⑥", t="这项研究有五点局限性", out="15.png", a=[
   "1. **只有一名患者。** 物体任务和 EEG 的数据都来自同一个人。截至 2020 年底另有 6 名患者已经注射，受新冠疫情影响，都还没有做功能评估¹。",
   "2. **对照条件试次极少。** 不戴镜时每个物体与对比度的组合只试了 1 次¹，「不戴镜看不见」的统计基础比「戴镜能看见」弱得多。",
   "3. **适用范围有限。** 这名患者入组时还有光感，治疗眼全程保留光感¹。完全没有光感的患者是否同样有效，这项研究没有给出数据。",
   "4. **EEG 解码的规模小、任务简单。** 共 63 个试次，训练和测试来自同一次实验¹，只解码「桌上有没有杯子」。",
   "5. **恢复的视觉层级有限。** 画面单色、只有亮灭两档¹；没有测视力表视力；训练约 7 个月后才开始报告改善¹。"]),
 dict(n="⑥", t="这一例能支持的结论，以及还没有回答的问题", out="16.png", a=[
   "能支持的结论：在一名晚期 RP 患者身上，光遗传加刺激眼镜恢复了一部分视觉功能。他能用这种视觉找到并定位较大的物体，戴镜睁眼时枕区脑电的变化也与此相符¹。",
   "不能支持的结论：",
   "- 这种疗法对多数患者有效；",
   "- 视力能恢复到可以阅读或辨认面孔的程度。",
   "还没有回答的问题，回到开头那项 10 人研究：它给出了安全性和光敏度的数据，7 人光敏度提高⁶。这 10 人能不能完成物体任务，要等全文或后续报告。"]),
]

for c in C:
    if not want(c["out"]):
        continue
    o = os.path.join(OUT, c["out"])
    if c.get("fig"):
        gen.figure_card(f(c["fig"]), c["lab"], c["a"], o, figure_height=c["fh"],
                        title=c["t"], title_num=c["n"])
    else:
        gen.text_card(None, c["a"], o, heading_lines=[f'{c["n"]} {c["t"]}'])

REFS = [
    "1. Sahel JA, et al. (2021). Partial recovery of visual function in a blind patient after optogenetic therapy. Nature Medicine 27:1223–1229.",
    "2. Humayun MS, et al. (2012). Interim results from the international trial of Second Sight's visual prosthesis. Ophthalmology 119:779–788.",
    "3. Holz FG, et al. (2026). Subretinal photovoltaic implant to restore vision in geographic atrophy due to AMD. New England Journal of Medicine 394:232–242.",
    "4. Bi A, et al. (2006). Ectopic expression of a microbial-type rhodopsin restores visual responses in mice with photoreceptor degeneration. Neuron 50:23–33.",
    "5. McGregor JE, et al. (2020). Optogenetic restoration of retinal ganglion cell activity in the living primate. Nature Communications 11:1703.",
    "6. Sahel JA, et al. (2026). Optogenetic therapy for restoring aspects of visual function. New England Journal of Medicine 395:1399–1408.",
    "7. Palanker D, et al. (2020). Photovoltaic restoration of central vision in atrophic age-related macular degeneration. Ophthalmology 127:1097–1104.",
    "8. Lagali PS, et al. (2008). Light-activated channels targeted to ON bipolar cells restore visual function in retinal degeneration. Nature Neuroscience 11:667–675.",
    "9. Busskamp V, et al. (2010). Genetic reactivation of cone photoreceptors restores visual responses in retinitis pigmentosa. Science 329:413–417.",
]
if want("17-tail.png"):
    gen.tail_card(REFS, os.path.join(OUT, "17-tail.png"))

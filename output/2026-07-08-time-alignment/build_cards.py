import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, ".claude/skills/dailybci/scripts")
from card_generator import CardGenerator


OUT = "output/2026-07-08-time-alignment"
FIG = os.path.join(OUT, "figs")
os.makedirs(FIG, exist_ok=True)

gen = CardGenerator(date="2026.07.08", platform="xiaohongshu")


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/STHeiti Medium.ttc" if bold else "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_TITLE = font(38, True)
F_LABEL = font(28, True)
F_SMALL = font(23)
F_NUM = font(30, True)

COL = {
    "bg": "#FFFFFF",
    "ink": "#1A1A1A",
    "body": "#444444",
    "muted": "#777777",
    "line": "#D8DEE6",
    "blue": "#2F6DB5",
    "red": "#C64F4F",
    "green": "#2E7D62",
    "amber": "#A36A00",
    "pale": "#F4F7FA",
}


def canvas(name, title=None):
    img = Image.new("RGB", (900, 560), COL["bg"])
    d = ImageDraw.Draw(img)
    if title:
        d.text((44, 30), title, fill=COL["ink"], font=F_TITLE)
    return img, d


def text_center(d, box, text, fnt, fill=COL["ink"]):
    x0, y0, x1, y1 = box
    bb = d.textbbox((0, 0), text, font=fnt)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text((x0 + (x1 - x0 - w) / 2, y0 + (y1 - y0 - h) / 2), text, fill=fill, font=fnt)


def rounded(d, box, fill, outline=COL["line"], width=2, radius=18):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(d, start, end, fill=COL["ink"], width=4):
    d.line([start, end], fill=fill, width=width)
    ang = math.atan2(end[1] - start[1], end[0] - start[0])
    size = 13
    pts = [
        end,
        (end[0] - size * math.cos(ang - 0.45), end[1] - size * math.sin(ang - 0.45)),
        (end[0] - size * math.cos(ang + 0.45), end[1] - size * math.sin(ang + 0.45)),
    ]
    d.polygon(pts, fill=fill)


def save(img, name):
    path = os.path.join(FIG, name)
    img.save(path)
    return path


def fig_causality():
    img, d = canvas("causality", "因果边界决定模型能不能上线")
    y = 260
    d.line([(70, y), (830, y)], fill=COL["line"], width=4)
    for x, label, color in [(210, "意图准备", COL["blue"]), (450, "行为事件", COL["ink"]), (690, "感觉反馈", COL["red"])]:
        d.ellipse((x - 11, y - 11, x + 11, y + 11), fill=color)
        text_center(d, (x - 75, y + 30, x + 75, y + 75), label, F_LABEL, color)
    d.arc((155, 145, 455, 300), 195, 338, fill=COL["blue"], width=5)
    arrow(d, (418, 177), (451, 253), COL["blue"], 5)
    d.text((150, 118), "合法预测：事件前信号", fill=COL["blue"], font=F_SMALL)
    d.arc((448, 145, 745, 300), 202, 340, fill=COL["red"], width=5)
    arrow(d, (710, 178), (690, 250), COL["red"], 5)
    d.text((545, 118), "时间泄漏：事件后信号", fill=COL["red"], font=F_SMALL)
    d.text((118, 425), "训练时偷看未来，离线准确率会变漂亮；闭环预测时，这些未来证据还不存在。", fill=COL["body"], font=F_SMALL)
    return save(img, "01-causality.png")


def fig_two_clocks():
    img, d = canvas("two_clocks", "对齐就是把行为时间投到神经时间")
    rounded(d, (70, 115, 830, 205), COL["pale"])
    d.text((95, 145), "行为时钟", fill=COL["muted"], font=F_LABEL)
    d.line((250, 160, 790, 160), fill=COL["line"], width=4)
    for x, t in [(330, "cue"), (520, "press"), (710, "reward")]:
        d.ellipse((x - 9, 151, x + 9, 169), fill=COL["amber"])
        text_center(d, (x - 48, 174, x + 48, 205), t, F_SMALL, COL["amber"])
    rounded(d, (70, 330, 830, 420), COL["pale"])
    d.text((95, 360), "神经时钟", fill=COL["muted"], font=F_LABEL)
    d.line((250, 375, 790, 375), fill=COL["line"], width=4)
    for x in range(280, 790, 42):
        d.line((x, 367, x, 383), fill=COL["blue"], width=2)
    arrow(d, (520, 215), (520, 320), COL["blue"], 4)
    d.text((560, 255), "同一事件必须变成\n神经 sample index", fill=COL["blue"], font=F_SMALL)
    return save(img, "02-two-clocks.png")


def fig_ttl():
    img, d = canvas("ttl", "TTL 用电平边沿标记事件")
    d.line((90, 415, 820, 415), fill=COL["line"], width=3)
    d.line((120, 345, 350, 345), fill=COL["ink"], width=5)
    d.line((350, 345, 350, 205), fill=COL["ink"], width=5)
    d.line((350, 205, 575, 205), fill=COL["ink"], width=5)
    d.line((575, 205, 575, 345), fill=COL["ink"], width=5)
    d.line((575, 345, 800, 345), fill=COL["ink"], width=5)
    d.text((80, 196), "5V", fill=COL["muted"], font=F_SMALL)
    d.text((80, 335), "0V", fill=COL["muted"], font=F_SMALL)
    arrow(d, (350, 430), (350, 220), COL["blue"], 4)
    d.text((282, 450), "rising edge\n事件样本点", fill=COL["blue"], font=F_SMALL)
    arrow(d, (575, 430), (575, 222), COL["red"], 4)
    d.text((535, 450), "falling edge\n另一种语义", fill=COL["red"], font=F_SMALL)
    return save(img, "03-ttl.png")


def fig_trial_chain():
    img, d = canvas("trial_chain", "一个 trial 是状态转移链")
    xs = [95, 220, 345, 470, 595, 720, 825]
    labels = ["cue", "delay", "move", "press", "hold", "reward", "feedback"]
    colors = [COL["blue"], COL["muted"], COL["green"], COL["amber"], COL["muted"], COL["red"], COL["blue"]]
    y = 275
    for i in range(len(xs) - 1):
        arrow(d, (xs[i] + 34, y), (xs[i + 1] - 34, y), COL["line"], 4)
    for x, label, color in zip(xs, labels, colors):
        d.ellipse((x - 31, y - 31, x + 31, y + 31), fill="#FFFFFF", outline=color, width=5)
        text_center(d, (x - 54, y + 48, x + 54, y + 88), label, F_SMALL, color)
    d.text((105, 430), "不同事件切出不同神经问题：提示、准备、启动、执行、结果和反馈。", fill=COL["body"], font=F_SMALL)
    return save(img, "04-trial-chain.png")


def fig_errors():
    img, d = canvas("errors", "delay、jitter、drift 性质不同")
    y0 = 140
    rows = [
        ("delay", "每次都晚 20 ms", COL["blue"]),
        ("jitter", "有时晚 5 ms，有时晚 35 ms", COL["red"]),
        ("drift", "越录越久，两条时间轴越走越散", COL["amber"]),
    ]
    for i, (name, desc, color) in enumerate(rows):
        y = y0 + i * 125
        d.text((80, y - 10), name, fill=color, font=F_LABEL)
        d.line((230, y, 800, y), fill=COL["line"], width=3)
        for x in [330, 470, 610]:
            d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=COL["ink"])
        if name == "delay":
            for x in [350, 490, 630]:
                d.ellipse((x - 7, y + 28, x + 7, y + 42), fill=color)
        elif name == "jitter":
            for x, dy in [(338, 20), (505, 45), (622, 14)]:
                d.ellipse((x - 7, y + dy, x + 7, y + dy + 14), fill=color)
        else:
            for x, dy in [(332, 15), (500, 35), (668, 58)]:
                d.ellipse((x - 7, y + dy, x + 7, y + dy + 14), fill=color)
        d.text((230, y + 55), desc, fill=COL["body"], font=F_SMALL)
    return save(img, "05-errors.png")


def fig_sync_layers():
    img, d = canvas("sync_layers", "三层硬件同步各管一件事")
    items = [
        ("Event TTL", "标记具体事件", COL["green"]),
        ("Sync pulse", "估计 offset 和 drift", COL["blue"]),
        ("Shared clock", "统一时间尺子", COL["amber"]),
    ]
    for i, (title, desc, color) in enumerate(items):
        y = 125 + i * 125
        rounded(d, (80, y, 820, y + 82), "#FFFFFF", outline=color, width=4)
        d.text((120, y + 18), title, fill=color, font=F_LABEL)
        d.text((390, y + 22), desc, fill=COL["body"], font=F_SMALL)
    d.text((110, 500), "Open Ephys 文档也强调：精确同步依赖共享硬件 sync line。", fill=COL["body"], font=F_SMALL)
    return save(img, "06-sync-layers.png")


def fig_mux():
    img, d = canvas("mux", "高通道系统常见“组内串行、组间并行”")
    groups = [(80, "ADC 1", ["ch1", "ch2", "ch3"]), (350, "ADC 2", ["ch13", "ch14", "ch15"]), (620, "ADC 3", ["ch25", "ch26", "ch27"])]
    for gx, adc, chs in groups:
        for i, ch in enumerate(chs):
            y = 130 + i * 64
            rounded(d, (gx, y, gx + 95, y + 42), "#FFFFFF")
            text_center(d, (gx, y, gx + 95, y + 42), ch, F_SMALL, COL["body"])
            d.line((gx + 95, y + 21, gx + 145, 226), fill=COL["line"], width=3)
        rounded(d, (gx + 145, 198, gx + 245, 254), COL["pale"], outline=COL["blue"], width=3)
        text_center(d, (gx + 145, 198, gx + 245, 254), adc, F_SMALL, COL["blue"])
    for x, lab in [(202, "step 1"), (472, "step 1"), (742, "step 1")]:
        d.ellipse((x - 11, 335, x + 11, 357), fill=COL["green"])
        text_center(d, (x - 52, 368, x + 52, 400), lab, F_SMALL, COL["green"])
    d.text((100, 460), "组间可在同一节拍并行；同一 ADC 组内仍要排队扫描。", fill=COL["body"], font=F_SMALL)
    return save(img, "07-mux.png")


def fig_software():
    img, d = canvas("software", "软件对齐最后回到 sample index")
    xs = [135, 220, 305, 390, 475, 560, 645]
    vals = [0, 0, 0, 1, 1, 1, 0]
    for i, (x, v) in enumerate(zip(xs, vals)):
        d.text((x - 8, 155), str(i), fill=COL["muted"], font=F_SMALL)
        rounded(d, (x - 30, 200, x + 30, 260), "#FFFFFF", outline=COL["blue"] if v else COL["line"], width=3)
        text_center(d, (x - 30, 200, x + 30, 260), str(v), F_NUM, COL["blue"] if v else COL["muted"])
    arrow(d, (390, 305), (390, 262), COL["green"], 4)
    d.text((333, 318), "0→1\nrising edge", fill=COL["green"], font=F_SMALL)
    d.text((110, 430), "relative_sample = spike_sample − event_sample", fill=COL["ink"], font=F_LABEL)
    d.text((110, 480), "先用整数样本点做减法，最后再换算成 ms/s。", fill=COL["body"], font=F_SMALL)
    return save(img, "08-software.png")


paths = {
    "causality": fig_causality(),
    "two_clocks": fig_two_clocks(),
    "ttl": fig_ttl(),
    "trial": fig_trial_chain(),
    "errors": fig_errors(),
    "sync": fig_sync_layers(),
    "mux": fig_mux(),
    "software": fig_software(),
}


gen.cover_card(
    "BCI 解码",
    "先要校准时间",
    "神经信号和行为事件对不齐，模型可能学到未来的反馈。",
    os.path.join(OUT, "01-cover.png"),
)

gen.figure_card(
    paths["causality"],
    "因果边界",
    [
        "神经解码首先要保证因果关系成立。",
        "Spike 是神经元动作电位，常在毫秒级发生；population activity 是群体神经活动，常在几十到几百毫秒内形成可解码模式。",
        "如果事件时间错位，模型可能用动作之后的反馈信号去“预测”动作本身。下一步要找到神经数据自己的时间轴。",
    ],
    os.path.join(OUT, "02-causality.png"),
)

gen.figure_card(
    paths["two_clocks"],
    "两条时间轴",
    [
        "行为事件必须投到神经采集系统的时间轴上。",
        "行为电脑、相机和任务程序都有自己的时间；神经采集系统也有自己的采样时钟。",
        "真正的问题在于 cue、press、reward 这些事件落在神经 sample index 的哪一个点。要把事件放进这条坐标，最常用的硬件语言就是 TTL。",
    ],
    os.path.join(OUT, "03-neural-axis.png"),
)

gen.figure_card(
    paths["ttl"],
    "TTL pulse",
    [
        "TTL pulse 把“事件发生”压缩成一次高低电平跳变。",
        "TTL 是 transistor-transistor logic，晶体管-晶体管逻辑；实验里通常指 0/5V 或类似电平脉冲。",
        "神经采集系统记录 rising edge 或 falling edge，把它变成 event sample。TTL 只保证电信号边沿清楚，行为学意义还需要单独定义。",
    ],
    os.path.join(OUT, "04-ttl.png"),
)

gen.text_card(
    "事件定义决定神经问题",
    [
        "TTL 准确记录的是硬件定义的事件。",
        "以常见的啮齿类动物行为实验为例，一次按杆可以拆成运动准备、爪子接触、lever 位移、开关闭合、达到阈值、奖励发放。",
        "如果研究 movement onset，开关闭合的 TTL 可能已经偏晚；如果研究 press threshold，它可能正好合适。同步之前必须先定义事件。",
    ],
    os.path.join(OUT, "05-event-definition.png"),
)

gen.figure_card(
    paths["trial"],
    "trial structure",
    [
        "神经科学里的试次是一串状态转移。",
        "一个简单任务可能包含 cue onset、delay、movement onset、press threshold、hold、reward 和 feedback。",
        "记录多个 TTL 的意义，是把连续行为切成可解释的神经计算阶段。即使事件都标好了，时间轴本身仍然会出现 delay、jitter 和 drift。",
    ],
    os.path.join(OUT, "06-trial-chain.png"),
)

gen.figure_card(
    paths["errors"],
    "误差性质",
    [
        "固定 delay 是偏移，jitter 和 drift 会制造模糊。",
        "Delay 是事件发生到被记录之间晚了多久；jitter 是这个延迟每次是否稳定；drift 是两个时钟长期慢慢走散。",
        "固定 delay 可以测量和校正，随机 jitter 会把事件附近的神经动态抹糊。工程上通常用三层同步方案来控制这些误差。",
    ],
    os.path.join(OUT, "07-errors.png"),
)

gen.figure_card(
    paths["sync"],
    "同步层级",
    [
        "Event TTL、periodic sync pulse 和 shared clock 解决三类问题。",
        "Event TTL 标记具体事件；periodic sync pulse 用共同脉冲估计 offset 和 drift；shared clock 让多个设备从同一个 reference clock 派生时间。",
        "这套原则也延伸到 Neuropixels 这类高通道采集系统内部。",
    ],
    os.path.join(OUT, "08-sync-layers.png"),
)

gen.figure_card(
    paths["mux"],
    "Neuropixels 例子",
    [
        "高通道电极用时间换硬件资源。",
        "Neuropixels 1.0 有 384 个 recording channels，可从 960 个电极位点中选择记录；其电路资料显示 384 通道由 32 个 ADC 处理，每 12 个通道共享 1 个 10-bit SAR ADC。¹, ²",
        "这种架构是组内串行、组间并行。对 50 ms spike count 解码通常问题不大；对毫秒级 spike timing、相位和短延迟因果分析，就要认真检查。",
    ],
    os.path.join(OUT, "09-neuropixels-skew.png"),
)

gen.figure_card(
    paths["software"],
    "软件对齐",
    [
        "软件对齐最终落在 event sample 和 spike sample 的相对位置。",
        "数字通道先被解析成边沿：0→1 就是 rising edge。事件样本点确定后，神经窗口可以直接在 sample index 上切。",
        "转换成秒只是展示给人看；sample index 才是神经数据的原生坐标。好的神经解码从模型之前开始：先让事件、神经信号和设备时钟站到同一条时间轴上。",
    ],
    os.path.join(OUT, "10-software-alignment.png"),
)

gen.tail_card(
    [
        "¹ Jun, J. J. et al. Fully integrated silicon probes for high-density recording of neural activity. Nature 551, 232–236 (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5955206/",
        "",
        "² Mora Lopez, C. et al. A neural probe with up to 966 electrodes and up to 384 configurable channels in 0.13 μm SOI CMOS. IEEE TBioCAS 11, 510–522 (2017). https://doi.org/10.1109/TBCAS.2016.2646901",
        "",
        "其他资料",
        "Open Ephys GUI Docs. Synchronizing Data Streams. https://open-ephys.github.io/gui-docs/Tutorials/Data-Synchronization.html",
        "",
        "老石谈芯｜揭秘时钟信号：计算机与芯片的心跳，是怎样产生的？https://www.bilibili.com/video/BV1q84y1g7no/",
        "",
        "风云小橙｜晶体管是如何工作的？它的工作原理是什么？https://www.bilibili.com/video/BV17uN9zyEsu/",
    ],
    os.path.join(OUT, "11-refs.png"),
    lead_paragraphs=[
        "时间对齐属于神经解码的因果边界，不能降级为后处理细节。",
        "事件定义、硬件同步和 sample index 三件事合在一起，才决定模型到底在预测意图，还是在解释已经发生的行为。",
    ],
)

print("OK ->", OUT)

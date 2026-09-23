# -*- coding: utf-8 -*-
"""2026-09-23 · 模拟输出（AO）接口，何时用和怎么用（电生理 IO 系列 ep05）—— 卡片生成"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
EP = os.path.join(PROJ, "output", "2026-09-13-electrophysiology-io",
                  "ep05-2026-09-23-analog-output")
OUT = os.path.join(EP, "cards")
FIG = os.path.join(EP, "figs")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

only = set(sys.argv[1:])
def want(name): return not only or name in only

gen = CardGenerator(date="2026.09.23")

if want("01-cover.png"):
    gen.cover_card(
        "模拟输出（AO）接口，",
        "何时用和怎么用",
        "送出去的电压，要么是信号，\n要么是指令。",
        o("01-cover.png"),
        concept_image=f("cover-concept"), concept_height=400,
        title_size=80, title_top=90,
        source="本期不解读文献，从基础原理梳理模拟输出。",
    )

if want("02-toc.png"):
    gen.figure_card(
        f("toc"), "本期路线",
        ["按输出的电压交给谁、代表什么，模拟输出的用途只有两类：监看与控制。",
         "本期分别讲这两类用途对应什么需求、怎样连接，以及什么情况下其实不需要模拟输出。"],
        o("02-toc.png"), figure_height=470,
    )

C = [
 dict(n="①", t="那排接口什么时候用得上", fig="fig1-two-uses", lab="图 1", fh=440,
      out="03-c1.png", a=[
   "电生理采集设备的面板上，通常有一排标着 Analog Out 的接口。很多人做了几年实验，从来没往上面接过线。",
   "它送出的电压只有两种含义：**已经发生的信号**，用于监看；**要执行的指令**，用于控制。"]),
 dict(n="②", t="监看：问题要在实验当下发现", fig=None, out="04-c2.png", a=[
   "**监看**指的是在实验进行的同时，用眼睛或耳朵直接跟踪信号：在示波器上看某个通道的波形，或者把信号接到音箱，听动作电位发出的声音。",
   "之所以要监看，是因为记录下来的数据事后可以分析，却不能重录。电极有没有落在神经元旁边、接触是否良好、有没有混进干扰，这些问题只有在实验当下发现，才能当下调整；等实验结束再从数据里发现问题，那段神经活动已经不可能再记一遍。",
   "**监看的作用，就是把「事后才发现」提前到「当下还能纠正」。**"]),
 dict(n="③", t="什么时候需要真正的电压", fig="fig2-paths", lab="图 2", fh=420,
      out="05-c3.png", a=[
   "看和听，多数时候在软件里就能完成。但示波器要长时间观察和测量某一个通道，另一台设备（比如行为控制系统）要同时记录这个信号，它们的输入口接的都是电压，不是数字文件。",
   "硬件输出还不受电脑卡顿影响，延迟也更低。"]),
 dict(n="④", t="数字怎样变回电压", fig="fig3-dac", lab="图 3", fh=430,
      out="06-c4.png", a=[
   "完成这一步的器件叫**数模转换器**（digital-to-analog converter，DAC），与 ADC 方向相反。每个整数对应一档电压，两个整数之间电压保持不变，最后用低通滤波把台阶削平，这个滤波称为**重建滤波**（reconstruction filter）。",
   "送出去的是经过放大和滤波之后的信号，并非电极上的原始电压。"]),
 dict(n="⑤", t="控制：同样 1 V，代表不同的量", fig="fig4-one-volt", lab="图 4", fh=440,
      out="07-c5.png", a=[
   "**控制**指的是用模拟输出送出的电压去指挥一台外部设备，电压的大小决定设备执行的强弱。",
   "监看送出的是已经发生的信号，电压本身就是答案；控制送出的是一条要去执行的指令，1 V 代表多少，要看接收端怎样换算。"]),
 dict(n="⑥", t="什么时候才需要模拟输出来控制", fig="fig5-three-modes", lab="图 5", fh=440,
      out="08-c6.png", a=[
   "判断只看一件事：作用量需不需要随时间变化。只有斜坡、正弦、任意波形，或者按记录到的信号实时调整强度时，才需要模拟输出。",
   "膜片钳是典型：电压钳的阶跃或斜坡指令，一般由采集设备（膜片钳领域常称**数字化仪**，digitizer）的模拟输出送给放大器。"]),
 dict(n="⑦", t="控制怎么连", fig="fig6-connect", lab="图 6", fh=400,
      out="09-c7.png", a=[
   "设备通常有面板手动设定、TTL 触发、外部模拟电压控制几种工作方式，要切到最后一种。每伏对应多少作用量由接收端决定，例如 MultiClamp 700B 在电压钳下可选 20 mV 或 100 mV¹。",
   "电压范围、驱动能力这些两端是否兼容的问题，见《电生理设备之间的电气连接》第二部分。"]),
 dict(n="⑧", t="你的需求，对应哪种口", fig="fig7-table", lab="表 1", fh=520,
      out="10-c8.png", a=[
   "弄清楚自己要的是信号还是指令，就知道那排接口该不该接、接到哪里。"]),
]

for c in C:
    if not want(c["out"]):
        continue
    if c["fig"]:
        gen.figure_card(f(c["fig"]), c["lab"], c["a"], o(c["out"]),
                        figure_height=c["fh"], title=c["t"], title_num=c["n"])
    else:
        gen.text_card(None, c["a"], o(c["out"]), heading_lines=[f'{c["n"]} {c["t"]}'])

REFS = [
  "1. Axon Instruments. (2005). MultiClamp 700B Computer-Controlled Microelectrode Amplifier: Theory and Operation. Part Number 2500-0157 Rev D.",
]

if want("11-tail.png"):
    gen.tail_card(REFS, o("11-tail.png"), lead_paragraphs=[
      "模拟输出送出的电压，要么是已经发生的信号，要么是一条要执行的指令。前者用于监看，多数时候软件就能替代；后者用于控制，只有当作用量本身需要连续变化时才用得上。",
      "只需要开和关的刺激，用数字输出的 TTL 就够了。数字输入输出怎样工作，留到后续一期。",
    ])
print("done")

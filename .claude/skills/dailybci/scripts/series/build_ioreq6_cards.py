# -*- coding: utf-8 -*-
"""2026-09-24 · 数字接口（DIO），怎样发指令和记事件（电生理 IO 系列 ep06）—— 卡片生成"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
EP = os.path.join(PROJ, "output", "2026-09-13-electrophysiology-io",
                  "ep06-2026-09-24-digital-io")
OUT = os.path.join(EP, "cards")
FIG = os.path.join(EP, "figs")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

only = set(sys.argv[1:])
def want(name): return not only or name in only

gen = CardGenerator(date="2026.09.24")

if want("01-cover.png"):
    gen.cover_card(
        "数字接口（DIO），",
        "怎样发指令和记事件",
        "一个事件，怎样被正确发出、\n正确记下？",
        o("01-cover.png"),
        concept_image=f("cover-concept"), concept_height=400,
        title_size=80, title_top=90,
        source="本期不解读文献，从基础原理梳理数字输入输出。",
    )

if want("02-toc.png"):
    gen.figure_card(
        f("toc"), "本期路线",
        ["先讲两类用途共用的基础：数字口传的是什么。",
         "再按用途分两块：用数字输出发指令，用数字输入记事件，各讲要满足什么、怎样连接。最后按现象倒查原因。"],
        o("02-toc.png"), figure_height=500,
    )

C = [
 dict(n="①", t="打 marker 和触发光刺激，走的是同一类口", fig=None, out="03-c1.png", a=[
   "做实验时，常要在神经数据里标出某件事发生的时刻：刺激何时出现，动物何时舔水，相机何时拍下一帧。脑电实验里，这一步通常叫打 marker，即事件标记（event marker）。另一些时候方向相反：检测到某个信号，要让光源在那一刻亮起。",
   "这两件事多半经过采集设备上的数字口。用得不对，就会出现事件漏记、多记、极性反了，或者光没有在预想的时刻亮起。",
   "本期先讲两类用途共用的基础：数字口传的是什么。然后按用途分两类，用数字口发指令和用数字口记事件，分别讲各自要满足什么、怎样连接。"]),
 dict(n="②", t="数字口只分高和低", fig="fig1-levels", lab="图 1", fh=400, out="04-c2.png", a=[
   "接收端把输入电压和阈值比较，高于上阈值判为高，低于下阈值判为低。一个事件，就是一次从一种状态到另一种状态的变化。",
   "常说的 **TTL 信号**，名字来自晶体管–晶体管逻辑（transistor-transistor logic，TTL）这类数字芯片¹。现在一般指按这套阈值收发、高电平约 5 V、低电平约 0 V 的数字信号。"]),
 dict(n="③", t="两端要约定哪种状态算有效", fig="fig2-polarity", lab="图 2", fh=400, out="05-c3.png", a=[
   "这叫**有效极性**（active polarity），说明书里一般写作高电平有效（active high）或低电平有效（active low）。约定反了，有效和空闲就整体对调。",
   "两端约定好电平和极性，一个事件就能被正确送达。先看第一类用途：用数字输出向另一台设备发指令。指令送到之后，接收端怎样执行它？"]),
 dict(n="④", t="只认开始，还是跟着脉冲走", fig="fig3-edge-gated", lab="图 3", fh=440, out="06-c4.png", a=[
   "电平跳变的那一刻叫**边沿**（edge），从低到高是上升沿，从高到低是下降沿。**边沿触发**（edge-triggered）只在边沿那一刻动作；**门控**（gated）则是有效状态持续多久，就执行多久。",
   "以 2014 年冷泉港实验室 Kepecs 组发布的开源脉冲发生器 Pulse Pal 为例，它的触发输入两种方式都提供²。边沿触发时，发送端只需把跳变时刻发准；门控时，还要把脉冲宽度发准。"]),
 dict(n="⑤", t="脉冲何时发出，由谁决定", fig="fig4-timing", lab="图 4", fh=400, out="07-c5.png", a=[
   "**硬件定时**（hardware timing）由设备上的时钟决定输出时刻；**软件定时**（software timing）由电脑上的程序和操作系统决定，每条命令实际到达设备的时刻都有波动³。",
   "以数据采集设备厂商 NI（美国国家仪器）为例，其驱动软件 DAQmx 的用户手册写明，硬件时钟比软件循环快得多，也准确得多³。"]),
 dict(n="⑥", t="发指令之前，核对四件事", fig=None, out="08-c6.png", a=[
   "定时波动对两种执行方式的影响不同。边沿触发只看跳变那一刻，波动只让开始时刻不准；门控时脉冲宽度就是作用时长，例如用 Pulse Pal 的门控模式控制光源，脉冲宽了几毫秒，光就多照几毫秒。有些设备不支持硬件定时，要查说明书³。",
   "接线之前，按顺序确认：",
   "1. **接收端切到外部触发**：接收端通常有多种工作方式，要切到由外部数字输入控制。",
   "2. **执行方式**：边沿触发还是门控；门控时，脉冲宽度按作用时长来设。",
   "3. **极性**：两端对高电平有效还是低电平有效的约定一致。",
   "4. **定时方式**：对时刻或宽度有要求时，确认发送端用的是硬件定时。",
   "发指令到这里讲完。反过来，用数字输入记下别的设备送来的事件，又要注意什么？"]),
 dict(n="⑦", t="记事件的目标：一次事件，恰好一条记录", fig=None, out="09-c7.png", a=[
   "记事件要达到的目标，可以归成一句话：真实发生一次事件，文件里就恰好留下一条记录，并且标对是哪一种事件。偏离这个目标有三种方式：",
   "- **没记下**：脉冲太窄，落在两次读取之间；",
   "- **记了不止一次**：机械开关接通时电平来回跳；",
   "- **次数对了，种类认错了**：事件种类多、需要编码时。",
   "下面依次看这三种，最后讲在软件里怎样设置，才能让三点都满足。"]),
 dict(n="⑧", t="采集设备按间隔读电平，窄脉冲会漏掉", fig="fig5-sampling", lab="图 5", fh=380, out="10-c8.png", a=[
   "以 Intan 的 RHD USB 接口板为例，它的 16 路数字输入与放大器同步采样⁴：放大器每采一个样本，数字输入的电平也读一次。读取间隔就是采样率的倒数，这块板支持 1–30 kHz⁵，对应每 33 µs 到每 1 ms 读一次（按采样率换算）。",
   "以手册中的例子 20 kHz 为准，即每 50 µs 读一次⁴。两次读取之间的电平不进入记录，因此脉冲宽度要明显大于读取间隔。"]),
 dict(n="⑨", t="一次按压，为什么记成好几次", fig="fig6-bounce", lab="图 6", fh=400, out="11-c9.png", a=[
   "按键、杠杆这类靠金属触点接通的开关，触点闭合的瞬间会弹开再碰上若干次，这叫**触点抖动**（contact bounce）。芯片厂商德州仪器（TI）的应用说明写明，许多机械开关按下后会抖动数百微秒⁶，每 50 µs 读一次就会读成好几次跳变。",
   "处理方法叫**去抖**（debouncing）。同一份说明提到，去抖时间常取 10 ms⁶。去抖可以在硬件电路上做，也可以在分析时做。"]),
 dict(n="⑩", t="事件种类多时，用几根线编号", fig=None, out="12-c10.png", a=[
   "最直接的做法是一根线对应一种事件。以神经记录系统厂商 Plexon 的 OmniPlex 为例，它的一个数字输入口有 16 根数据线，可以设成 16 路独立事件⁷。手册建议在需要记录的动作种类少时用这种方式，比如杠杆按压、红外光束被遮挡⁷。",
   "种类再多，线就不够了。这时把几根线合起来表示一个编号：每根线的高或低代表二进制的一位，N 根线可以表示 2 的 N 次方个编号。OmniPlex 的另一种模式用 15 根线组成编号，范围是 0 到 32767，手册写明适合要记录成百上千种条件的场合⁷。",
   "几根线一起编码，会出现单根线没有的问题：各根线不会在同一瞬间完成跳变。这会带来什么？"]),
 dict(n="⑪", t="选通线：等电平稳定了再读", fig="fig7-strobe", lab="图 7", fh=420, out="13-c11.png", a=[
   "编号 3 是「低、高、高」，编号 4 是「高、低、低」。线 3 先变高、另外两根稍后变低时，中间短暂出现编号 7。接收端恰好在这一刻读取，就会记下一个从未发生的事件。",
   "解决办法是另加一根**选通线**（strobe），接收端只在它出现脉冲时读数据线。OmniPlex 要求数据线在选通脉冲之前至少稳定 100 ns；它没接线的输入会被拉到 +5 V、算进编号，所以手册建议把不用的线接地⁷。"]),
 dict(n="⑫", t="开始记录前，在软件里确认四件事", fig=None, out="14-c12.png", a=[
   "1. **这一路有没有被记录。** 两家设备的做法相反：Intan 接口板的数字输入默认关闭，要在软件里启用⁴；Plexon OmniPlex 的数字输入始终记录，没有开关⁷。",
   "2. **线怎样对应事件。** 每根线对应哪种事件；或者几根线组成编号，并用选通线指示何时读取。",
   "3. **有效极性。** 按发送端的约定设为高电平有效或低电平有效。",
   "4. **事件以什么形式存下。** Intan 把数字输入当作波形，按采样率逐点存下每一刻的电平⁴；OmniPlex 只存检测到边沿的时刻，编号模式下另存编号⁷。前一种要在分析时自己找出跳变、做去抖，后一种存下来就已经是事件列表。"]),
 dict(n="⑬", t="出了问题，按现象倒查", fig="fig8-table", lab="表 1", fh=560, out="15-c13.png", a=[
   "数字口只传高、低两种状态。指令被正确执行、事件被正确记下，靠的是两端在极性、执行方式、定时、读取间隔、编号方式上约定一致。"]),
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
  "1. Texas Instruments. (2017). SNx400, SNx4LS00, and SNx4S00 Quadruple 2-Input Positive-NAND Gates Datasheet. SDLS025D.",
  "2. Sanders J. I., Kepecs A. (2014). A low-cost programmable pulse generator for physiology and behavior. Frontiers in Neuroengineering 7:43.",
  "3. National Instruments. (2026). Timing, Hardware Versus Software. NI-DAQmx User Manual.",
  "4. Intan Technologies. (2021). RHD2000 Evaluation System.",
  "5. Intan Technologies. RHD USB Interface Board. intantech.com (accessed 2026-09-24).",
  "6. Texas Instruments. (2020). Debounce a Switch. Application Brief SCEA094.",
  "7. Plexon Inc. (2013). OmniPlex Digital Input Guide. OPXTN0001a, v1.2.",
]

if want("16-tail.png"):
    gen.tail_card(REFS, o("16-tail.png"), lead_paragraphs=[
      "数字输出发指令，关心的是接收端怎样执行、由谁定时；数字输入记事件，关心的是一次事件是否恰好留下一条记录、种类是否标对。",
      "事件记下以后，它的时刻怎样和神经数据、视频对齐，留到后续一期讲。",
    ])
print("done")

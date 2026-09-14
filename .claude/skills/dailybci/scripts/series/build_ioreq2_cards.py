# -*- coding: utf-8 -*-
"""2026-09-14 · 电生理采集的信息通路概览（电生理 IO 系列 ep02）—— 卡片生成"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from card_generator import CardGenerator

PROJ = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
EP = os.path.join(PROJ, "output", "2026-09-13-electrophysiology-io", "ep02-2026-09-14-system-paths")
OUT = os.path.join(EP, "cards")
FIG = os.path.join(EP, "figs")
def f(n): return os.path.join(FIG, n + ".png")
def o(n): return os.path.join(OUT, n)

only = set(sys.argv[1:])
def want(name): return not only or name in only

gen = CardGenerator(date="2026.09.14")

if want("01-cover.png"):
    gen.cover_card(
        "电生理采集的",
        "信息通路概览",
        "闭环实验里，判断放在采集设备上\n还是电脑上，差别在哪里？",
        o("01-cover.png"),
        concept_image=f("cover-concept"), concept_height=440,
        title_size=112, title_top=60,
        source="本期以 Roux et al. 2017 的闭环光遗传实验为例。",
    )

if want("02-toc.png"):
    gen.figure_card(
        f("toc"), "本期路线",
        ["以「检测到涟漪即给光」的闭环实验为例，本期先拆出系统要完成的四项职责，再看这些职责分给哪些设备，以及分法不同会改变哪条连接的用途。",
         "最后讨论这条连接用于控制时要满足什么要求，比较判断放在采集设备上和放在电脑上的实现与差异。"],
        o("02-toc.png"), figure_height=520,
    )

C = [
 dict(n="①", t="以一个闭环实验为例", fig="fig1-loop", lab="图 1", fh=440, out="03-c1.png", a=[
   "Roux 等人 2017 年发表在《Nature Neuroscience》上的研究中，研究者在小鼠背侧海马 CA1 区植入硅探针，实时检测清醒期的尖波涟漪（sharp-wave ripple），每检出一次，就经光纤给一个 60 ms 的光脉冲¹。",
   "第一期写清了要测什么。这一期要问：这些事分别由哪台设备来做？"]),
 dict(n="①", t="系统要完成四项职责", fig="fig2-duties", lab="表 1", fh=400, out="04-c2.png", a=[
   "判断与保存都是从数值到数值：判断的结果会改变后续的生成，保存的结果不会。",
   "这里的判断指系统自动完成、全程无人参与，因此只有闭环实验才有判断。实验者看屏幕后手动调整刺激，属于系统外部的操作，改动的时刻与数值也要保存。"]),
 dict(n="②", t="哪些职责的位置可以选", fig=None, out="05-c3.png", a=[
   "四项职责按任务划分，一台设备可以同时承担多项。同一台设备完成的职责，信息在设备内部传递；分到两台设备上，信息就要跨设备传递。因此，职责放在哪里，决定了哪些信息需要连接。",
   "**生成和测量**需要一条物理通路连到实验对象，例如光纤、导线。作用点固定：光必须照到目标脑区，电位必须在电极处取得。设备本身可以放在远处。",
   "**判断和保存**只处理数值，可以放在任何一台收得到数据、算得了或存得下、并且处理得够快的设备上。",
   "两者中本期只挪判断：闭环的控制通路是测量 → 判断 → 生成，判断位于中间；保存不在这条通路上，本例固定在电脑上。"]),
 dict(n="②", t="只挪判断，比较两种方案", fig="fig3-ab", lab="表 2", fh=380, out="06-c4.png", a=[
   "两个方案里，神经数据都要送到电脑保存。区别在于给光这一步：要不要等数据先到电脑、判断完成，再把结果送回光源驱动。",
   "开头 Roux 等人的实验，神经信号由 Amplipex 系统记录，其中一个通道另外送入 TDT RX6 处理器完成检测¹，判断放在第三台设备上，与 A、B 都不同。"]),
 dict(n="②", t="分配方案改变了哪条连接的用途", fig="fig4-paths", lab="图 2", fh=500, out="07-c5.png", a=[
   "跨设备的连接有三条：神经数据、行为视频、给光指令。前两条的起点与终点在两个方案中相同，单看连线，A 与 B 几乎一样。",
   "判断挪到电脑上之后，采集设备到电脑这条原本只用于保存的连接，进入了控制通路。"]),
 dict(n="③", t="用途变了，要求随之改变", fig=None, out="08-c6.png", a=[
   "**用于保存时，要求事后能对齐。**延迟固定属于系统误差，测出后可以扣除；延迟每次不同属于随机误差，只能减小。数据晚到多少，只影响事后分析的对齐精度。",
   "**用于控制时，要求及时送达。**光照到组织的时刻已经发生，事后校正改变不了光落在事件的哪个时间点。要看两件事：",
   "**延迟多大**：参照被检测事件本身的持续时间。延迟超过事件持续时间，光就落在事件结束之后。",
   "**延迟是否稳定**：延迟固定，每次光落在事件内的相对位置相同；延迟波动，同一组试次混入了不同的刺激时机。"]),
 dict(n="③", t="两种实现的步骤与延迟构成", fig="fig5-steps", lab="图 3", fh=520, out="09-c7.png", a=[
   "电脑端的数据按块打包、缓冲后再处理²。采集端在现场可编程门阵列（FPGA）或数字信号处理器（DSP）上直接检测：FPGA 出厂后可重新配置内部逻辑电路，运算以电路形式执行，每个样本的处理时间固定。",
   "检测延迟来自算法需要一段足够长的信号才能判定，与判断放在哪台设备上无关。"]),
 dict(n="③", t="判断在采集设备上的系统", fig=None, out="10-c8.png", a=[
   "**Intan**：公开的接口方案 Rhythm USB-7310 用 Verilog 配置一块 Xilinx FPGA，控制前端芯片采样，再经 USB 3.0 送数据到电脑。选定通道可在 FPGA 内部直接送到模拟输出，不经过 USB 与电脑；FPGA 上还有阈值比较器，可先高通滤去局部场电位，波形越过阈值即由数字输出口给出高电平³。RHD 记录控制器同样提供这种输出⁴。这类判断限于阈值比较。",
   "**Müller 等人的系统**：高密度 CMOS 微电极阵列接到 FPGA，由 FPGA 完成动作电位检测与反馈刺激的生成；对象为大鼠胚胎皮层神经元的离体培养⁵。",
   "**TDT**：Synapse 中的功能模块编译后分配到处理器的 DSP 上运算⁶，可检测动作电位并控制脉冲输出⁷。Roux 等人的涟漪检测即由 TDT RX6 完成¹。"]),
 dict(n="③", t="判断在电脑上的系统", fig=None, out="11-c9.png", a=[
   "**Open Ephys GUI**：数据处理全部在软件中完成；官方闭环示例由外接 Arduino 配合 Arduino Output 插件输出反馈信号²。",
   "**Trodes**：Dutta 等人在这一开源软件中加入涟漪检测模块，检出后由经以太网连接的 BeagleBone Black 发出数字脉冲。前端为 Intan RHD2000 headstage，分别接入经 USB 2.0 传输的 Open Ephys 采集板与经千兆以太网传输的 SpikeGadgets 主控单元；对象为 1 只雄性大鼠⁸。",
   "**BRAND**：人体皮层内脑机接口平台，运行在带实时补丁的 Linux 上。BrainGate2 试验受试者 T11 用它完成光标控制，信号处理、循环神经网络（RNN）解码与任务控制由它执行⁹。"]),
 dict(n="③", t="两种实现各有长短", fig="fig6-compare", lab="表 3", fh=560, out="12-c10.png", a=[
   "数值出处：Müller 等⁵，Dutta 等⁸，Open Ephys 文档²，BRAND⁹。「实现难度」一行为按实现方式的推导。"]),
 dict(n="③", t="怎样选择判断的位置", fig=None, out="13-c11.png", a=[
   "选择看两件事：实验允许多大的延迟，算法有多复杂。",
   "电脑端的系统延迟已经远小于事件持续时间时，放在电脑上可以保留算法的灵活性；需要亚毫秒级延迟、抖动极小时，就要放在采集设备上。",
   "系统延迟也常常不是延迟的主要来源。Dutta 等人报告，涟漪持续约 100 ms；用以太网采集硬件、每分钟误检少于 10 次时，检测算法本身的延迟约 20–66 ms，并随阈值参数变化⁸。这部分延迟与判断放在哪里无关。"]),
 dict(n="③", t="每条连接可以用哪些接口", fig="fig7-interfaces", lab="表 4", fh=340, out="14-c12.png", a=[
   "**模拟**用连续变化的电压表示数值；**数字 IO** 用高低电平表示状态或事件；**通信接口**按约定协议传输数据包。输入与输出相对某台设备而言：同一条连接，在发送端是输出，在接收端是输入。",
   "候选不唯一：同一份神经数据，Intan 的设备既可经 USB 送到电脑，也可把选定通道重新转换为电压，从模拟输出口实时送出，用于声音监听⁴。"]),
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
  "1. Roux L., et al. (2017). Sharp wave ripples during learning stabilize the hippocampal spatial map. Nature Neuroscience 20(6):845–853.",
  "2. Open Ephys. (n.d.). Closed-Loop Latency. Open Ephys GUI Documentation.",
  "3. Intan Technologies. (2025). RHD XEM7310 Interface: Rhythm USB-7310.",
  "4. Intan Technologies. (2024). Intan Recording Controller User Guide.",
  "5. Müller J., et al. (2012). Sub-millisecond closed-loop feedback stimulation between arbitrary sets of individual neurons. Frontiers in Neural Circuits 6:121.",
  "6. Tucker-Davis Technologies. (n.d.). Synapse Manual – Troubleshooting.",
  "7. Tucker-Davis Technologies. (n.d.). Optogenetic Stimulation.",
  "8. Dutta S., et al. (2019). Analysis of an open source, closed-loop, realtime system for hippocampal sharp-wave ripple disruption. Journal of Neural Engineering 16(1):016009.",
  "9. Ali Y.H., et al. (2024). BRAND: a platform for closed-loop experiments with deep network models. Journal of Neural Engineering 21(2).",
]

if want("15-tail.png"):
    gen.tail_card(REFS, o("15-tail.png"), lead_paragraphs=[
      "从四项职责出发，本期比较了判断放在采集设备上与电脑上两种方案。两端怎样连接、每类接口怎样工作，留到后续各期。",
    ])
print("done")

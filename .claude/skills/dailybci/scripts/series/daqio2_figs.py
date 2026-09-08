# -*- coding: utf-8 -*-
"""series-daq-io-01 · 四种口 —— 自制示意图"""
import os, subprocess, tempfile, math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-daq-io-02-clock", "figs")
os.makedirs(OUT, exist_ok=True)

BG="#FAFAFA"; ACC="#2F6DB5"; TINT="#E9F0F8"; INK="#1A1A1A"; BODY="#4A4A4A"
GRAY="#8A8A8A"; LINE="#D6DBE2"; RED="#C0392B"; REDT="#F7E9E7"
GRN="#2E7D57"; GRNT="#E7F2EC"; CARD_L="#DCE5F0"; PANEL="#F3F5F8"

DEFS=('<defs>'
 f'<marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{ACC}"/></marker>'
 f'<marker id="ahr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{RED}"/></marker>'
 f'<marker id="ahk" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{INK}"/></marker>'
 f'<marker id="ahn" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{GRN}"/></marker>'
 '</defs>')

def T(x,y,s,size=24,fill=INK,anchor="middle",weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'
def box(x,y,w,h,fill=PANEL,stroke=CARD_L,rx=12,sw=1.6,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def line(x1,y1,x2,y2,stroke=INK,sw=2.2,dash=None,marker=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    m=f' marker-end="url(#{marker})"' if marker else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'
def path(d,stroke=INK,sw=2.4,fill="none",dash=None,marker=None):
    ds=f' stroke-dasharray="{dash}"' if dash else ""
    m=f' marker-end="url(#{marker})"' if marker else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}"{ds}{m}/>'
def circ(cx,cy,r,fill=TINT,stroke=ACC,sw=2):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def eeg(x0,y0,w,amp,pts=260,sw=2.4,stroke=ACC,seed=1.0):
    d=[]
    for i in range(pts+1):
        t=i/pts; x=x0+w*t
        y=(y0-amp*(0.62*math.sin(2*math.pi*3.1*t+seed)
                   +0.30*math.sin(2*math.pi*7.7*t+2.1*seed)
                   +0.16*math.sin(2*math.pi*15.3*t+0.7*seed)))
        d.append(("M" if i==0 else "L")+f"{x:.1f},{y:.1f}")
    return path(" ".join(d),stroke,sw)

def sq(x0,ylo,yhi,segs,sw=2.6,stroke=INK):
    """segs: [(x_start,x_end)] 高电平区间；其余为低"""
    d=[f"M{x0:.1f},{ylo:.1f}"]
    for a,b in segs:
        d+= [f"L{a:.1f},{ylo:.1f}",f"L{a:.1f},{yhi:.1f}",f"L{b:.1f},{yhi:.1f}",f"L{b:.1f},{ylo:.1f}"]
    return d

def render(name,w,h,inner,scale=2):
    svg=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*scale}" height="{h*scale}" '
         f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
         f'{DEFS}<rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')
    html=(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
          f'@font-face{{font-family:HeitiSC;src:url("file://{FONT}")}}'
          f'html,body{{margin:0;padding:0;background:{BG}}}</style></head><body>{svg}</body></html>')
    tf=tempfile.NamedTemporaryFile(suffix=".html",delete=False,mode="w",encoding="utf-8")
    tf.write(html); tf.close()
    out=os.path.join(OUT,name+".png")
    subprocess.run(["npx","playwright","screenshot","file://"+tf.name,out,
                    f"--viewport-size={w*scale},{h*scale}","--wait-for-timeout=600"],
                   check=True,capture_output=True,text=True)
    os.unlink(tf.name)
    print("  ->",name)




def ticks(x0, y, n, dx, h=14, stroke=INK, sw=2.0):
    """一列等间隔的时钟上升沿刻度"""
    o=[line(x0, y, x0+dx*(n-1), y, LINE, 1.4)]
    for i in range(n):
        o.append(line(x0+i*dx, y, x0+i*dx, y-h, stroke, sw))
    return "".join(o)

# ===== 封面概念图：基准时钟 → 分频 → 采样点 → 数据 =====
def fig_cover():
    W,H=900,440; s=[]
    x0,x1=70,830
    s.append(T(x0,50,"基准时钟",23,GRAY,anchor="start"))
    s.append(ticks(x0,92,39,20,16,ACC,1.8))
    # 分频带
    s.append(box(x0,116,760,48,PANEL,CARD_L,rx=10))
    s.append(T(W/2,148,"分频　÷ 10000",25,INK))
    s.append(line(W/2,164,W/2,194,GRAY,2.2,marker="ahg"))
    s.append(T(x0,232,"采样时刻",23,GRAY,anchor="start"))
    s.append(ticks(x0,268,9,95,20,INK,2.6))
    s.append(eeg(x0,352,760,40))
    for i in range(9):
        xx=x0+i*95; t=(i*95)/760
        yy=352-40*(0.62*math.sin(2*math.pi*3.1*t+1.0)
                   +0.30*math.sin(2*math.pi*7.7*t+2.1)
                   +0.16*math.sin(2*math.pi*15.3*t+0.7))
        s.append(line(xx,270,xx,yy,LINE,1.2,dash="4 5"))
        s.append(circ(xx,yy,7,"#FFFFFF",ACC,2.2))
    render("cover-concept",W,H,"".join(s))

# ===== 图1 分频器 =====
def fig_divider():
    W,H=900,400; s=[]
    x0=90; dx=19; n=37
    s.append(T(60,50,"基准时钟　10 MHz，每 100 ns 一个上升沿",23,BODY,anchor="start"))
    s.append(ticks(x0,104,n,dx,18,ACC,1.8))
    # 计数值：每 12 个复位一次
    for i in range(n):
        c=i%12+1
        if c in (1,12):
            s.append(T(x0+i*dx,132,str(c) if c==1 else "N",19,GRAY))
    s.append(T(60,132,"计数值",21,GRAY,anchor="start"))
    s.append(box(80,160,740,52,PANEL,CARD_L,rx=10))
    s.append(T(450,192,"每来一个上升沿加 1，加到 N 输出一个脉冲，然后清零重数",23,INK))
    s.append(T(60,258,"采样时钟",23,BODY,anchor="start"))
    segs=[(x0+11*dx,x0+12*dx),(x0+23*dx,x0+24*dx),(x0+35*dx,x0+36*dx)]
    d=sq(x0,330,286,segs); d.append(f"L{x0+dx*(n-1)},330")
    s.append(path(" ".join(d),INK,2.6))
    for a,b in segs:
        s.append(line(a,120,a,284,LINE,1.2,dash="4 4"))
    s.append(T(W/2,378,"输出周期 ＝ N × 100 ns。N ＝ 10000 时为 1 ms，即 1 kHz",23,BODY))
    render("fig1-divider",W,H,"".join(s))

# ===== 图2 恒定偏差 vs 随机抖动 =====
def fig_two_errors():
    W,H=900,420; s=[]
    x0=150; n=8; dx=78
    def panel(ytop, col, tint, title, actual, cap):
        s.append(box(40,ytop,820,150,"#FFFFFF",CARD_L))
        s.append(T(66,ytop+34,title,23,col,anchor="start"))
        ax=ytop+92
        s.append(line(x0-30,ax,x0+dx*(n-1)+70,ax,LINE,1.6))
        s.append(T(x0-46,ax-14,"理想",19,GRAY,anchor="end"))
        s.append(T(x0-46,ax+26,"实际",19,GRAY,anchor="end"))
        for i in range(n):
            s.append(line(x0+i*dx,ax-26,x0+i*dx,ax-4,GRAY,2.0,dash="3 3"))
        for i,xx in enumerate(actual):
            s.append(line(x0+xx,ax+4,x0+xx,ax+26,col,2.8))
        s.append(T(450,ytop+140,cap,21,col))
    drift=[i*dx*1.055 for i in range(n)]
    jit=[0,11,-8,6,-12,9,-5,13]
    rnd=[i*dx+jit[i] for i in range(n)]
    panel(26,ACC,TINT,"ppm 频率偏差 —— 恒定，可校正",drift,"每一拍都长同样一点，越走越开，但偏多少是已知的")
    panel(226,RED,REDT,"抖动 —— 随机，校正不了",rnd,"平均下来没变，但每一拍偏多少不可预测")
    render("fig2-two-errors",W,H,"".join(s))

# ===== 图3 抖动如何变成幅值误差 =====
def fig_jitter_amp():
    W,H=900,440; s=[]
    x0,w=90,730; y0=220; amp=110; f=1.15
    def yv(t): return y0-amp*math.sin(2*math.pi*f*t+0.5)
    d=[]
    for i in range(361):
        t=i/360; x=x0+w*t
        d.append(("M" if i==0 else "L")+f"{x:.1f},{yv(t):.1f}")
    s.append(path(" ".join(d),ACC,2.8))
    dt=0.035
    def mark(t, lab, labpos):
        x=x0+w*t; x2=x0+w*(t+dt)
        s.append(line(x,72,x,352,GRAY,1.6,dash="4 4"))
        s.append(line(x2,72,x2,352,RED,1.8,dash="4 4"))
        # Δt 横向标注
        s.append(line(x,86,x2,86,RED,2.0))
        s.append(T((x+x2)/2,78,"Δt",19,RED))
        ya,yb=yv(t),yv(t+dt)
        s.append(line(x2+18,min(ya,yb),x2+18,max(ya,yb),RED,4))
        s.append(line(x2+12,ya,x2+24,ya,RED,2))
        s.append(line(x2+12,yb,x2+24,yb,RED,2))
        s.append(T(x2+32,(ya+yb)/2+7,lab,22,RED,anchor="start"))
        s.append(circ(x,ya,7,"#FFFFFF",GRAY,2.0))
        s.append(circ(x2,yb,7,"#FFFFFF",RED,2.2))
    mark(0.366,"幅值误差大",1)
    mark(0.583,"幅值误差小",1)
    s.append(T(x0+w*0.366,52,"斜率最大处",21,BODY))
    s.append(T(x0+w*0.583+40,52,"斜率接近零处",21,BODY))
    s.append(T(W/2,H-16,"同样的时刻偏移 Δt，斜率越大，读出的幅值差越大",23,BODY))
    render("fig3-jitter-amp",W,H,"".join(s))

# ===== 图4 硬件定时 vs 软件定时 两条链 =====
def fig_two_chains():
    W,H=900,380; s=[]
    def chain(y, items, col, tint, tag, jit):
        s.append(T(70,y-46,tag,23,col,anchor="start"))
        x=70
        for k,it in enumerate(items):
            wbox=170
            s.append(box(x,y-30,wbox,60,tint,col,rx=10))
            s.append(T(x+wbox/2,y+8,it,23,col))
            x+=wbox
            if k<len(items)-1:
                s.append(line(x+6,y,x+42,y,INK,2.2,marker="ahk"))
                x+=48
        s.append(T(W-60,y+8,jit,26,col,anchor="end"))
    chain(112,["石英","分频器","ADC 取样"],GRN,GRNT,"硬件定时","≈ 100 ps")
    chain(292,["操作系统","总线传输","ADC 取样"],RED,REDT,"软件定时","≈ 10 µs")
    s.append(T(W/2,H-14,"差五个数量级。1 kHz 上折合 20.3 位 对 3.7 位",23,BODY))
    render("fig4-two-chains",W,H,"".join(s))

# ===== 图5 按频率的对照表 =====
def fig_freq_table():
    W,H=880,330; s=[]
    rows=[("100 Hz","23.6 位","远好于放大器，可忽略"),
          ("1 kHz","20.3 位","与放大器同量级"),
          ("10 kHz","17.0 位","已成为限制因素")]
    s.append(T(150,58,"信号频率",23,GRAY))
    s.append(T(400,58,"抖动限制的有效位数",23,GRAY))
    s.append(T(700,58,"与放大器噪声相比",23,GRAY))
    s.append(line(60,76,W-60,76,LINE,1.6))
    y=126
    for a,b,c in rows:
        s.append(T(150,y,a,27,INK))
        s.append(T(400,y,b,27,ACC,weight="600"))
        s.append(T(700,y,c,23,BODY))
        s.append(line(60,y+24,W-60,y+24,LINE,1.0))
        y+=68
    s.append(T(W/2,H-24,"同一个 100 ps 的时钟。放大器有效位数通常在 20 位上下",22,GRAY))
    render("fig5-freq-table",W,H,"".join(s))

# ===== 图6 三条通路共用同一基准 =====
def fig_shared_base():
    W,H=900,400; s=[]
    s.append(box(60,150,150,90,TINT,ACC,rx=12))
    s.append(T(135,192,"石英",26,ACC)); s.append(T(135,222,"10 MHz",21,GRAY))
    rows=[("AI 采样","÷ 10000","1 kHz  →  1 ms",92),
          ("AO 输出","÷ 10000","1 kHz",192),
          ("DI 锁存","÷ 1","10 MHz  →  100 ns",292)]
    for name,divi,res,y in rows:
        s.append(line(212,195,268,y+2,GRAY,2.0,marker="ahg"))
        s.append(box(272,y-26,150,54,PANEL,CARD_L,rx=10))
        s.append(T(347,y+8,divi,24,INK))
        s.append(line(424,y+2,466,y+2,INK,2.0,marker="ahk"))
        s.append(T(478,y-4,name,23,BODY,anchor="start"))
        s.append(T(478,y+24,res,21,GRAY,anchor="start"))
    s.append(T(W/2,H-24,"分频比是固定的整数，所以三条通路的相位关系不随时间改变",23,BODY))
    render("fig6-shared-base",W,H,"".join(s))

# ===== 目录 =====
def fig_toc():
    W,H=880,470; s=[]
    items=[("①","每个点都带着一个时刻","卡 1–2"),
           ("②","时刻从哪来","卡 3–6"),
           ("③","时刻错在哪：两种错法","卡 7–10"),
           ("④","错多少，看谁在定时刻","卡 11–13"),
           ("⑤","通路之间对得齐吗","卡 14–15")]
    y=56
    for n,t,r in items:
        s.append(T(72,y+8,n,32,ACC,anchor="start"))
        s.append(T(124,y+8,t,30,INK,anchor="start"))
        s.append(T(W-72,y+8,r,24,GRAY,anchor="end"))
        s.append(line(72,y+30,W-72,y+30,LINE,1.2))
        y+=86
    render("toc",W,H,"".join(s))

if __name__=="__main__":
    fig_toc(); fig_cover(); fig_divider(); fig_two_errors()
    fig_jitter_amp(); fig_two_chains(); fig_freq_table(); fig_shared_base()
    print("figs done")

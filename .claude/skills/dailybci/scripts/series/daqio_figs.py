# -*- coding: utf-8 -*-
"""series-daq-io-01 · 四种口 —— 自制示意图"""
import os, subprocess, tempfile, math

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-daq-io-01-four-ports", "figs")
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


# ===== 封面概念图：连续量穿过边界后变成有限个台阶 =====
def fig_cover():
    W,H=900,400; s=[]
    bx=450
    s.append(line(bx,40,bx,H-56,LINE,2.6,dash="8 8"))
    s.append(T(bx,H-24,"计算机的边界",24,GRAY))
    s.append(eeg(70,180,340,74))
    s.append(T(240,72,"连续",26,BODY))
    # 阶梯量化
    lv=[0,2,4,3,5,6,4,2]
    x=bx+30; step=48; d=[]
    for i,v in enumerate(lv):
        y=250-v*24
        d.append(("M" if i==0 else "L")+f"{x:.0f},{y:.0f}")
        d.append(f"L{x+step:.0f},{y:.0f}")
        x+=step
    s.append(path(" ".join(d),ACC,2.8))
    for i in range(8):
        yy=250-i*24
        s.append(line(bx+30,yy,bx+30+step*len(lv),yy,LINE,1.0))
    s.append(T(bx+200,72,"有限个取值",26,BODY))
    render("cover-concept",W,H,"".join(s))

# ===== 图1 示波器双通道：物理上是同一类东西 =====
def fig_scope():
    W,H=880,412; s=[]
    s.append(box(40,30,800,150,"#FFFFFF",CARD_L))
    s.append(box(40,205,800,150,"#FFFFFF",CARD_L))
    s.append(eeg(80,105,720,46))
    s.append(T(64,54,"CH1  EEG 前置放大器输出",22,GRAY,anchor="start"))
    s.append(T(64,229,"CH2  刺激器 TTL 线",22,GRAY,anchor="start"))
    segs=[(200,320),(430,470),(600,760)]
    d=sq(80,315,255,segs); d.append(f"L{800:.0f},315")
    s.append(path(" ".join(d),ACC,2.8))
    s.append(T(440,H-14,"两条都是随时间连续变化的电压，没有哪一条自带「我是数字的」",23,BODY))
    render("fig1-scope",W,H,"".join(s))

# ===== 图2 噪声容限 =====
def fig_noise():
    W,H=960,430; s=[]
    ax=300; top=60; bot=350
    def vy(v): return bot-(v/5.0)*(bot-top)
    s.append(line(ax,top-8,ax,bot,INK,2.2))
    for v in range(0,6):
        s.append(line(ax-7,vy(v),ax,vy(v),INK,1.8))
        s.append(T(ax-14,vy(v)+8,f"{v} V",22,GRAY,anchor="end"))
    bw=210
    gx=ax+40; rx=ax+300
    s.append(T(gx+bw/2,top-22,"发送端保证",23,BODY))
    s.append(T(rx+bw/2,top-22,"接收端判定",23,BODY))
    s.append(box(gx,vy(5),bw,vy(2.4)-vy(5),GRNT,GRN,rx=6,sw=1.4))
    s.append(box(gx,vy(0.4),bw,vy(0)-vy(0.4),GRNT,GRN,rx=6,sw=1.4))
    s.append(T(gx+bw/2,vy(3.6)+8,"输出高",22,GRN))
    s.append(T(gx+bw/2,vy(0.13)+8,"输出低",22,GRN))
    s.append(box(rx,vy(5),bw,vy(2.0)-vy(5),TINT,ACC,rx=6,sw=1.4))
    s.append(box(rx,vy(0.8),bw,vy(0)-vy(0.8),TINT,ACC,rx=6,sw=1.4))
    s.append(T(rx+bw/2,vy(3.5)+8,"判为高",22,ACC))
    s.append(T(rx+bw/2,vy(0.16)+8,"判为低",22,ACC))
    for a,b in [(2.0,2.4),(0.4,0.8)]:
        s.append(box(gx,vy(b),rx+bw-gx,vy(a)-vy(b),REDT,RED,rx=3,sw=1.2,dash="5 4"))
    s.append(T(rx+bw+14,vy(2.2)+8,"0.4 V",23,RED,anchor="start"))
    s.append(T(rx+bw+14,vy(0.6)+8,"0.4 V",23,RED,anchor="start"))
    s.append(T(ax+320,vy(1.4)+8,"未定义区",22,GRAY))
    for v,lab in [(2.4,"VOH 2.4"),(2.0,"VIH 2.0"),(0.8,"VIL 0.8"),(0.4,"VOL 0.4")]:
        s.append(line(ax,vy(v),ax+34,vy(v),GRAY,1.2,dash="3 3"))
        s.append(T(ax-52,vy(v)+7,lab,21,BODY,anchor="end"))
    s.append(T(W/2,H-18,"红色是噪声容限：这个范围内的干扰，判定结果完全不变",23,BODY))
    render("fig2-noise-margin",W,H,"".join(s))

# ===== 图3 两种离散化 =====
def fig_disc():
    W,H=900,420; s=[]
    s.append(box(30,26,840,170,"#FFFFFF",CARD_L))
    s.append(box(30,222,840,170,"#FFFFFF",CARD_L))
    s.append(T(52,52,"AI  被迫的离散化 · 有损",23,RED,anchor="start"))
    s.append(T(52,248,"DI  约定的离散化 · 无损",23,GRN,anchor="start"))
    # 上路
    s.append(eeg(70,130,200,38))
    s.append(line(290,130,350,130,INK,2.2,marker="ahk"))
    s.append(box(352,102,116,56,TINT,ACC,rx=8)); s.append(T(410,138,"ADC",24,ACC))
    s.append(line(478,130,538,130,INK,2.2,marker="ahk"))
    lv=[3,5,4,6,3,2,4,5]; x=548; d=[]
    for i,v in enumerate(lv):
        y=160-v*11
        d.append(("M" if i==0 else "L")+f"{x},{y}"); d.append(f"L{x+30},{y}"); x+=30
    s.append(path(" ".join(d),ACC,2.6))
    s.append(T(700,182,"压成有限个取值，细节丢了",21,GRAY))
    # 下路
    d=sq(70,318,278,[(120,180),(215,250)]); d.append("L280,318")
    s.append(path(" ".join(d),INK,2.6))
    s.append(T(175,352,"到达设备前已是两态",21,GRAY))
    s.append(line(290,326,350,326,INK,2.2,marker="ahk"))
    s.append(box(352,298,116,56,GRNT,GRN,rx=8)); s.append(T(410,334,"比较器",24,GRN))
    s.append(line(478,326,538,326,INK,2.2,marker="ahk"))
    s.append(T(640,334,"1 0 1 1 0 0 1 0",26,GRN,anchor="start"))
    s.append(T(700,372,"只是读出已有的状态",21,GRAY))
    render("fig3-two-discretizations",W,H,"".join(s))

# ===== 图4 四格表 =====
def fig_quad():
    W,H=880,400; s=[]
    x0,y0,cw,ch=250,90,290,120
    s.append(T(x0+cw/2,y0-22,"进 Input",26,BODY))
    s.append(T(x0+cw*1.5,y0-22,"出 Output",26,BODY))
    s.append(T(x0-20,y0+ch/2+8,"离散化在设备内",24,BODY,anchor="end"))
    s.append(T(x0-20,y0+ch/2+34,"Analog",22,GRAY,anchor="end"))
    s.append(T(x0-20,y0+ch*1.5+8,"离散化在信号源侧",24,BODY,anchor="end"))
    s.append(T(x0-20,y0+ch*1.5+34,"Digital",22,GRAY,anchor="end"))
    cells=[("AI",TINT,ACC),("AO",TINT,ACC),("DI",GRNT,GRN),("DO",GRNT,GRN)]
    for i,(lab,f,st) in enumerate(cells):
        r,c=divmod(i,2)
        s.append(box(x0+c*cw,y0+r*ch,cw-10,ch-10,f,st,rx=14,sw=2))
        s.append(T(x0+c*cw+(cw-10)/2,y0+r*ch+(ch-10)/2+16,lab,48,st,weight="600"))
    s.append(T(W/2,H-36,"两条轴各两个取值，穷举完就是四种。不多也不少。",24,BODY))
    render("fig4-quadrant",W,H,"".join(s))

# ===== 图5 SAR 排队 vs 比较器即时 =====
def fig_sar():
    W,H=900,470; s=[]
    s.append(T(230,44,"AI 侧：SAR 逐位逼近",24,ACC))
    s.append(T(680,44,"DI 侧：比较器",24,GRN))
    s.append(line(450,60,450,360,LINE,2,dash="7 7"))
    # 左：16 步
    bx,by=110,72
    tgt=0.63; lo,hi=0.0,1.0; est=[]
    for i in range(6):
        mid=(lo+hi)/2
        if tgt>mid: lo=mid
        else: hi=mid
        est.append(mid)
    gw,gh=330,140
    s.append(line(bx,by+gh,bx+gw,by+gh,LINE,1.6))
    ty=by+gh-tgt*gh
    s.append(line(bx,ty,bx+gw,ty,GRAY,1.8,dash="6 5"))
    s.append(T(bx-10,ty+7,"待测电压",20,GRAY,anchor="end"))
    d=[]; step=gw/len(est)
    for i,v in enumerate(est):
        y=by+gh-v*gh; x=bx+i*step
        d.append(("M" if i==0 else "L")+f"{x:.0f},{y:.0f}"); d.append(f"L{x+step:.0f},{y:.0f}")
    s.append(path(" ".join(d),ACC,2.6))
    for i in range(len(est)+1):
        s.append(line(bx+i*step,by+gh,bx+i*step,by+gh+8,GRAY,1.4))
    s.append(T(275,by+gh+46,"N 位就要比较 N 次",23,BODY))
    s.append(T(275,by+gh+78,"每次之间还要等电路稳定",22,GRAY))
    s.append(box(90,by+gh+108,280,58,PANEL,CARD_L,rx=10))
    s.append(T(230,by+gh+146,"转换时间固定，必须排队",23,INK))
    s.append(T(230,by+gh+192,"→ 采样时钟由此而来",23,ACC))
    # 右：比较器
    cx,cy=560,120
    s.append(path(f"M{cx},{cy} L{cx},{cy+80} L{cx+90},{cy+40} Z",GRN,2.4,fill=GRNT))
    s.append(line(cx-70,cy+22,cx,cy+22,INK,2.2,marker="ahk"))
    s.append(line(cx-70,cy+58,cx,cy+58,GRAY,2.0,dash="5 4"))
    s.append(T(cx-76,cy+28,"输入",21,BODY,anchor="end"))
    s.append(T(cx-76,cy+64,"阈值",21,GRAY,anchor="end"))
    s.append(line(cx+90,cy+40,cx+160,cy+40,INK,2.2,marker="ahk"))
    s.append(T(cx+170,cy+47,"0 / 1",24,GRN,anchor="start"))
    s.append(box(500,by+gh+108,320,58,PANEL,CARD_L,rx=10))
    s.append(T(660,by+gh+146,"传播延迟纳秒量级，连续工作",23,INK))
    s.append(T(660,by+gh+192,"→ 不需要谁来启动它",23,GRN))
    render("fig5-sar-vs-comparator",W,H,"".join(s))

# ===== 图6 DI 两条通路 =====
def fig_paths():
    W,H=900,440; s=[]
    x0,x1=70,830
    # 共同的输入脉冲
    s.append(T(52,44,"线上的信号：一个 200 µs 的短脉冲",23,BODY,anchor="start"))
    d=sq(x0,100,64,[(430,452)]); d.append(f"L{x1},100")
    s.append(path(" ".join(d),INK,2.6))
    # 通路一
    s.append(T(52,168,"通路一　按采样时钟定期读（1 kHz）",23,RED,anchor="start"))
    for i in range(11):
        xx=x0+i*76
        s.append(line(xx,186,xx,242,LINE,1.6,dash="4 4"))
        s.append(circ(xx,242,7,"#FFFFFF",RED,1.8))
    s.append(line(430,186,430,250,RED,2.0,dash="5 4"))
    s.append(T(452,214,"脉冲落在两次读之间",22,RED,anchor="start"))
    s.append(T(x0,278,"读到的全是 0，数据里什么都没有",23,BODY,anchor="start"))
    # 通路二
    s.append(T(52,336,"通路二　沿直接锁存",23,GRN,anchor="start"))
    s.append(line(430,352,430,392,GRN,2.4,marker="ahn"))
    s.append(box(452,356,250,40,GRNT,GRN,rx=8))
    s.append(T(577,383,"锁存计数器当前值",23,GRN))
    s.append(T(x0,424,"时刻精度由设备内部的高速时钟决定，纳秒量级",23,BODY,anchor="start"))
    render("fig6-two-paths",W,H,"".join(s))

# ===== 目录 =====
def fig_toc():
    W,H=880,470; s=[]
    items=[("①","一个真实的分歧","卡 1–2"),
           ("②","模拟与数字差在哪","卡 3–5"),
           ("③","四种口是怎么穷举出来的","卡 6–7"),
           ("④","硬件决定了谁能不排队","卡 8–9"),
           ("⑤","那我该接哪个口","卡 10–14")]
    y=56
    for n,t,r in items:
        s.append(T(72,y+8,n,32,ACC,anchor="start"))
        s.append(T(124,y+8,t,30,INK,anchor="start"))
        s.append(T(W-72,y+8,r,24,GRAY,anchor="end"))
        s.append(line(72,y+30,W-72,y+30,LINE,1.2))
        y+=86
    render("toc",W,H,"".join(s))

if __name__=="__main__":
    fig_toc(); fig_cover(); fig_scope(); fig_noise(); fig_disc(); fig_quad(); fig_sar(); fig_paths()
    print("figs done")

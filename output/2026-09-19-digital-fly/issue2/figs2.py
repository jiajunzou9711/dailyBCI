# -*- coding: utf-8 -*-
"""第二期自制示意图。viewBox 按 900 宽排版，以 2 倍像素输出（与图卡 2 倍渲染一致）。背景 #FAFAFA 与卡面一致。"""
import os, subprocess
BG="#FAFAFA"; INK="#1A1A1A"; BODY="#444444"; MUT="#888888"; ACC="#2F6DB5"; RED="#8A2B2B"; LINE="#D8D8D8"; PALE="#EEF3FA"; PALER="#F7ECEC"
FONT="-apple-system,'Helvetica Neue','Heiti SC','PingFang SC',sans-serif"
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"figs")

def t(x,y,s,size=22,fill=BODY,anchor="start",weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'
def rect(x,y,w,h,fill="#FFFFFF",stroke=INK,sw=2,rx=10,dash=False):
    d=' stroke-dasharray="7 5"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def line(x1,y1,x2,y2,color=INK,w=2.4,arrow=False,dash=False,head="ar"):
    d=' stroke-dasharray="6 5"' if dash else ''
    m=f' marker-end="url(#{head})"' if arrow else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}{m}/>'
def node(cx,cy,r,label,sub=None,lab_size=20,fill="#FFFFFF",stroke=INK):
    s=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'+t(cx,cy+7,label,lab_size,INK,"middle","700")
    if sub: s+=t(cx,cy+r+26,sub,18,MUT,"middle")
    return s
def inhib(x,y,color=INK):
    return line(x,y-16,x,y+16,color,3)
DEFS=('<defs>'+''.join(
    f'<marker id="{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="{c}"/></marker>'
    for i,c in [("ar",INK),("arA",ACC),("arR",RED),("arM",MUT)])+'</defs>')

def save(name,W,H,inner,scale=2):
    svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*scale}" height="{H*scale}" '
         f'font-family="{FONT}"><rect width="{W}" height="{H}" fill="{BG}"/>{DEFS}{inner}</svg>')
    sp=os.path.join(D,name+".svg"); hp=os.path.join(D,name+".html"); pp=os.path.join(D,name+".png")
    open(sp,"w").write(svg)
    open(hp,"w").write(f'<html><body style="margin:0">{svg}</body></html>')
    subprocess.run(["npx","playwright","screenshot","file://"+hp,pp,f"--viewport-size={W*scale},{H*scale}"],check=True,capture_output=True)
    os.remove(hp)

# ---------- 目录 ----------
def fig_toc():
    W,H=900,625
    items=[("①","数字实验用来做什么","在模型里先筛一遍，前提是预测可信"),
           ("②","模型的三项默认设定","连接、神经元、时间，各自简化了什么"),
           ("③","连接：强度与正负号","一个常数管全脑突触；递质定正负"),
           ("④","神经元：同一条发放规则","统一参数，没有自发放电"),
           ("⑤","时间：状态与经历","饱与饿，模型给同一个预测"),
           ("⑥","怎么补：反推与测量","用任务反推参数；把参数直接测出来"),
           ("⑦","结语","缺的是连接之外的参数")]
    s=[t(0,56,"本期路线",28,INK,"start","700")]; y=56
    for num,head,sub in items:
        y+=72
        s+= [t(4,y,num,30,ACC,"start","700"),t(54,y,head,27,INK,"start","700"),t(54,y+33,sub,21,MUT)]
    save("fig-toc2",W,H,"".join(s))

# ---------- ② 总览：三项设定 ----------
def fig_overview():
    W,H=900,470
    s=[t(0,34,"模型在连接组之外补的三项设定",25,INK,"start","700")]
    s+= [t(130,82,"模型怎么设",20,MUT,"start","700"), t(540,82,"省掉的",20,MUT,"start","700")]
    rows=[("连接",["强度 = 突触数 × 0.275 mV","每个神经元只有一个正负号"],["突触后受体的差异","电突触"]),
          ("神经元",["漏积分发放，全脑一组参数","没有输入时不放电"],["自发放电、树突计算","不发放动作电位的神经元"]),
          ("时间",["连接和参数全程固定"],["饥饿等内部状态","学习带来的突触变化"])]
    y=102
    for name,setv,miss in rows:
        s.append(rect(0,y,880,108,"#FFFFFF",LINE,1.5,12))
        s.append(t(24,y+62,name,26,ACC,"start","700"))
        for i,l in enumerate(setv): s.append(t(130,y+44+i*36,l,21,INK))
        for i,l in enumerate(miss): s.append(t(540,y+44+i*36,l,21,RED))
        y+=122
    save("fig-overview",W,H,"".join(s))

# ---------- ③-1 膜电位标尺 ----------
def fig_voltage():
    W,H=900,400
    s=[t(0,34,"一次上游发放，推动下游膜电位多少",25,INK,"start","700")]
    x0=150; k=100  # 1 mV = 100 px
    bars=[("1 个突触",0.275,"0.275 mV",ACC),("10 个突触",2.75,"2.75 mV",ACC),("静息 → 阈值",7.0,"7 mV：−52 → −45 mV",MUT)]
    y=90
    for lab,v,val,c in bars:
        s.append(t(x0-16,y+30,lab,21,INK,"end","700"))
        if c==MUT:
            s.append(rect(x0,y,v*k,44,"#FFFFFF",MUT,2,6,dash=True))
        else:
            s.append(rect(x0,y,max(v*k,6),44,c,c,0,6))
        s.append(t(x0+v*k+14 if v*k<600 else x0+v*k-14,y+30,val,21,c if c!=MUT else BODY,"start" if v*k<600 else "end","700"))
        y+=78
    # 刻度
    s.append(line(x0,y+6,x0+700,y+6,MUT,1.5))
    for mv in range(0,8):
        s.append(line(x0+mv*k,y+6,x0+mv*k,y+14,MUT,1.5)); s.append(t(x0+mv*k,y+38,str(mv),18,MUT,"middle"))
    s.append(t(x0+720,y+12,"mV",18,MUT))
    save("fig-voltage",W,H,"".join(s))

# ---------- ③-2 同样突触数，不同效力 ----------
def fig_efficacy():
    W,H=900,530
    s=[t(0,34,"两条连接都是 10 个突触",25,INK,"start","700")]
    def panel(y0,title,wA,wB,labA,labB,color,note):
        o=[t(0,y0,title,22,color,"start","700")]
        cy1,cy2=y0+56,y0+140
        o.append(node(80,cy1,40,"A",lab_size=22)); o.append(node(80,cy2,40,"B",lab_size=22))
        o.append(node(560,(cy1+cy2)/2,48,"C",lab_size=22))
        o.append(line(122,cy1,510,(cy1+cy2)/2-14,color,wA,True,head="arA" if color==ACC else "arR"))
        o.append(line(122,cy2,510,(cy1+cy2)/2+14,color,wB,True,head="arA" if color==ACC else "arR"))
        o.append(t(300,cy1-8,labA,19,BODY,"middle")); o.append(t(300,cy2+30,labB,19,BODY,"middle"))
        o.append(t(640,(cy1+cy2)/2-8,note[0],19,BODY)); o.append(t(640,(cy1+cy2)/2+22,note[1],19,BODY))
        return "".join(o)
    s.append(panel(84,"模型里",4,4,"10 × 0.275 mV","10 × 0.275 mV",ACC,["两条连接一样强","强弱只看突触数之比"]))
    s.append(line(0,268,880,268,LINE,1.5))
    s.append(panel(306,"真实大脑里",7,2,"10 个突触，效力未知","10 个突触，效力未知",RED,["还取决于受体种类与数量、","释放概率、树突上的位置"]))
    save("fig-efficacy",W,H,"".join(s))

# ---------- ③-3 正负号的来路 ----------
def fig_sign():
    W,H=900,520
    s=[t(0,34,"正负号怎样来到模型里",25,INK,"start","700")]
    bx=[(0,"电镜图像块","以突触前位点为中心"),(230,"三维卷积网络","Eckstein 2024"),(460,"六种递质之一","按神经元计票取多数"),(690,"正负号","Shiu 2024 的规则")]
    for i,(x,a,b) in enumerate(bx):
        s.append(rect(x,64,190,96,PALE if i<3 else "#FFFFFF",ACC if i<3 else INK,2,12))
        s.append(t(x+95,106,a,21,INK,"middle","700")); s.append(t(x+95,138,b,17,MUT,"middle"))
        if i<3: s.append(line(x+192,112,x+228,112,INK,2.4,True))
    s.append(t(0,212,"规则：GABA、谷氨酸 → 抑制；其余 → 兴奋",21,INK,"start","700"))
    s.append(line(0,236,880,236,LINE,1.5))
    s.append(t(0,280,"真实情形以谷氨酸为例：方向取决于突触后受体",22,INK,"start","700"))
    s.append(rect(0,306,190,70,"#FFFFFF",INK,2,12)); s.append(t(95,348,"谷氨酸",22,INK,"middle","700"))
    s.append(line(192,330,330,312,RED,2.4,True,head="arR")); s.append(line(192,352,330,398,ACC,2.4,True,head="arA"))
    s.append(t(342,318,"抑制性受体（如 GluCl）→ 抑制",21,RED,"start","700"))
    s.append(t(342,406,"兴奋性受体 → 兴奋",21,ACC,"start","700"))
    s.append(rect(0,436,880,64,PALER,RED,1.5,10))
    s.append(t(20,476,"模型：电镜看不到受体，谷氨酸能神经元的全部输出一律记为抑制",21,RED,"start","700"))
    save("fig-sign",W,H,"".join(s))

# ---------- ④-2 去抑制（第一期图的 2 倍重绘，真实一行标注为论文推测） ----------
def fig_disinhibition():
    W,H=900,580
    def row(y0,title,rates,tail,tail_color):
        o=[t(0,y0,title,23,INK,"start","700")]
        xs=[40,330,620]; names=["Phantom","Scapula","Roundup"]; cy=y0+74
        for i,(x,nm) in enumerate(zip(xs,names)):
            o.append(node(x+56,cy,52,nm,rates[i],19))
            if i<2:
                o.append(line(x+108,cy,xs[i+1]-16,cy)); o.append(inhib(xs[i+1]-16,cy))
        o.append(line(xs[2]+108,cy,xs[2]+178,cy,INK,2.4,True)); o.append(t(xs[2]+188,cy+8,"MN9",21,INK,"start","700"))
        o.append(t(0,y0+196,tail,20,tail_color,"start","700"))
        return "".join(o)
    s=[t(0,30,"激活 Phantom 之后，下游会怎样",25,INK,"start","700"),t(0,58,"横线末端的短竖杠表示抑制性连接",18,MUT)]
    s.append(row(96,"模型里（基础放电设为 0 Hz）",["驱动到 50 Hz","0 Hz → 仍为 0 Hz","0 Hz"],"没有可解除的抑制，MN9 不发放，模型判为「不会伸喙」",RED))
    s.append(line(0,330,880,330,LINE,1.5))
    s.append(row(368,"真实果蝇里（论文推测的机制）",["被激活","持续发放 → 被压低","抑制被解除"],"喙伸出，实验记为「会伸喙」",ACC))
    save("fig-disinhibition2",W,H,"".join(s))

# ---------- ⑤-2 饱与饿 ----------
def fig_hunger():
    W,H=900,470
    s=[t(0,34,"同一条通路，两种状态",25,INK,"start","700"),t(0,62,"示意图，曲线形状非实测数据",18,MUT)]
    # 左：通路
    s.append(node(70,200,52,"糖味觉",lab_size=19)); s.append(t(70,206+34,"神经元",17,MUT,"middle"))
    s.append(line(124,200,196,200,INK,2.4,True)); s.append(t(236,207,"…",26,INK,"middle","700"))
    s.append(line(262,200,318,200,INK,2.4,True)); s.append(node(360,200,40,"MN9",lab_size=19))
    s.append(line(70,98,70,142,RED,2.4,True,head="arR"))
    s.append(t(0,90,"饥饿时：多巴胺经 DopEcR 作用于这里",18,RED,"start","700"))
    s.append(t(210,300,"模型里强度只看突触数，",19,BODY,"middle")); s.append(t(210,328,"饱、饿都一样",19,BODY,"middle"))
    # 右：曲线
    ox,oy,w,h=500,380,360,270
    s.append(line(ox,oy,ox+w,oy,INK,2)); s.append(line(ox,oy,ox,oy-h,INK,2))
    s.append(t(ox+w/2,oy+34,"蔗糖浓度",18,MUT,"middle"))
    s.append(f'<text x="{ox-18}" y="{oy-h/2}" font-size="18" fill="{MUT}" text-anchor="middle" transform="rotate(-90 {ox-18} {oy-h/2})">伸喙比例</text>')
    def sig(shift,color,dash=False):
        import math
        pts=[]
        for i in range(0,61):
            x=i/60; y=1/(1+math.exp(-(x-shift)*12))
            pts.append(f"{ox+x*w:.1f},{oy-y*(h-20):.1f}")
        d=' stroke-dasharray="7 5"' if dash else ''
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="3.2"{d}/>'
    s.append(sig(0.35,RED)); s.append(sig(0.62,ACC))
    s.append(t(ox+95,oy-205,"饿",20,RED,"start","700")); s.append(t(ox+262,oy-120,"饱",20,ACC,"start","700"))
    s.append(t(ox+w,oy-h-6,"真实果蝇",19,INK,"end","700"))
    save("fig-hunger",W,H,"".join(s))

# ---------- ⑥-2 Mindspan 流程 ----------
def fig_mindspan():
    W,H=900,430
    s=[t(0,34,"Mindspan 公开的测量流程（据官网职位描述）",24,INK,"start","700")]
    boxes=[(0,"人脑组织",["固定与接收"]),(225,"膨胀显微镜",["分子与连接"]),(450,"光学生理 · 电生理",["电压成像、光遗传","配对膜片钳"]),(675,"值得模拟的重建",["a reconstruction","worth simulating"])]
    for i,(x,a,bs) in enumerate(boxes):
        last=i==3
        s.append(rect(x,80,205,150,"#FFFFFF" if not last else PALE,INK if not last else ACC,2,12))
        s.append(t(x+102,124,a,20,INK if not last else ACC,"middle","700"))
        for j,b in enumerate(bs): s.append(t(x+102,164+j*28,b,17,MUT,"middle"))
        if i<3: s.append(line(x+207,155,x+223,155,INK,2.4,True))
    s.append(t(0,286,"样本：人与小鼠脑片、人 iPSC 来源的神经元",20,BODY))
    s.append(rect(0,316,880,82,PALER,RED,1.5,10))
    s.append(t(20,352,"现阶段：仍在组建创始团队，尚无公开的研究成果",21,RED,"start","700"))
    s.append(t(20,382,"研究对象是人脑，与果蝇模型没有直接的数据联系",19,BODY))
    save("fig-mindspan",W,H,"".join(s))

# ---------- ⑦ 每个量的来路 ----------
def fig_closing():
    W,H=900,500
    s=[t(0,34,"模型里每一类量从哪里来",25,INK,"start","700")]
    rows=[("突触的位置与数量","电镜重建",ACC),("递质","由电镜图像预测",ACC),("正负号","按递质统一规定",RED),
          ("单个突触的强度","全脑一个常数，照一条通路拟合",RED),("神经元参数","全脑一组，没有自发放电",RED),("状态与经历","未纳入",MUT)]
    y=62
    for name,src,c in rows:
        s.append(rect(0,y,880,58,"#FFFFFF",LINE,1.5,10))
        s.append(t(22,y+37,name,21,INK,"start","700"))
        s.append(rect(330,y+12,12,34,c,c,0,3))
        s.append(t(358,y+37,src,21,c,"start","700"))
        y+=66
    s.append(t(0,y+20,"蓝：测得或由测量预测　红：统一规定　灰：未纳入",18,MUT))
    save("fig-closing",W,H,"".join(s))

if __name__=="__main__":
    for f in [fig_toc,fig_overview,fig_voltage,fig_efficacy,fig_sign,fig_disinhibition,fig_hunger,fig_mindspan,fig_closing]:
        f()
    print("ok")

# -*- coding: utf-8 -*-
"""第一期自制示意图。背景与卡面一致 #FAFAFA。"""
import os
BG="#FAFAFA"; INK="#1A1A1A"; BODY="#444444"; MUT="#888888"; ACC="#2F6DB5"; RED="#8A2B2B"; LINE="#D8D8D8"
FONT="-apple-system,'Helvetica Neue','Heiti SC','PingFang SC',sans-serif"

def wrap(w,h,inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="{FONT}"><rect width="{w}" height="{h}" fill="{BG}"/>{inner}</svg>')

def t(x,y,s,size=22,fill=BODY,anchor="start",weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def node(cx,cy,r,label,fill="#FFFFFF",stroke=INK,sub=None,lab_size=21):
    s=(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
       + t(cx,cy+7,label,lab_size,INK,"middle","700"))
    if sub: s+=t(cx,cy+r+26,sub,19,MUT,"middle")
    return s

def arrow(x1,y1,x2,y2,color=INK,dash=False,width=2.4,head="ar"):
    d=' stroke-dasharray="6 5"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d} marker-end="url(#{head})"/>'

DEFS=(f'<defs>'
      f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
      f'<path d="M0,1 L9,5 L0,9 z" fill="{INK}"/></marker>'
      f'<marker id="arR" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
      f'<path d="M0,1 L9,5 L0,9 z" fill="{RED}"/></marker>'
      f'</defs>')

def bar_t(x1,y,x2,color=INK):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="3"/>'

# ---------------- 图 A：零基础放电时去抑制算不出 ----------------
def fig_disinhibition(path):
    W,H=900,580
    s=[DEFS]
    def row(y0, title, rates, tail, tail_color):
        o=[t(0,y0,title,23,INK,"start","700")]
        xs=[40,330,620]
        names=["Phantom","Scapula","Roundup"]
        cy=y0+74
        for i,(x,nm) in enumerate(zip(xs,names)):
            o.append(node(x+56,cy,52,nm,"#FFFFFF",INK,sub=rates[i],lab_size=19))
            if i<2:
                o.append(f'<line x1="{x+108}" y1="{cy}" x2="{xs[i+1]-16}" y2="{cy}" stroke="{INK}" stroke-width="2.4"/>')
                o.append(f'<line x1="{xs[i+1]-16}" y1="{cy-18}" x2="{xs[i+1]-16}" y2="{cy+18}" stroke="{INK}" stroke-width="3"/>')
        o.append(f'<line x1="{xs[2]+108}" y1="{cy}" x2="{xs[2]+178}" y2="{cy}" stroke="{INK}" stroke-width="2.4" marker-end="url(#ar)"/>')
        o.append(t(xs[2]+188,cy+8,"MN9",21,INK,"start","700"))
        o.append(t(0,y0+196,tail,20,tail_color,"start","700"))
        return "".join(o)
    s.append(t(0,30,"激活 Phantom 之后，下游会怎样",25,INK,"start","700"))
    s.append(t(0,58,"横线末端的短竖杠表示抑制性连接",18,MUT))
    s.append(row(96,"模型里（基础放电设为 0 Hz）",["驱动到 50 Hz","0 Hz → 仍为 0 Hz","0 Hz"],"没有可解除的抑制，MN9 不发放，模型判为“不会伸喙”",RED))
    s.append(f'<line x1="0" y1="330" x2="880" y2="330" stroke="{LINE}" stroke-width="1.5"/>')
    s.append(row(368,"真实果蝇里（存在持续自发活动）",["被激活","持续发放 → 被压低","抑制被解除"],"喙伸出，实验记为“会伸喙”",ACC))
    open(path,"w").write(wrap(W,H,"".join(s)))

# ---------------- 图 B：基线与模型 ----------------
def fig_baseline(path):
    W,H=900,580
    s=[DEFS]
    s.append(t(40,44,"106 个细胞类型的预测成绩",26,INK,"start","700"))
    s.append(t(40,74,"纵轴为准确率；虚线为不做任何计算的基线",19,MUT))
    y0,y1=430,120           # 0% -> 100%
    def ypos(p): return y0-(y0-y1)*p/100.0
    # axis
    s.append(f'<line x1="150" y1="{y0}" x2="820" y2="{y0}" stroke="{INK}" stroke-width="2"/>')
    for p in (0,50,86.8,95.3,100):
        s.append(f'<line x1="144" y1="{ypos(p):.1f}" x2="150" y2="{ypos(p):.1f}" stroke="{MUT}" stroke-width="1.5"/>')
    for p in (0,50,100):
        s.append(t(136,ypos(p)+7,f"{p:.0f}%",19,MUT,"end"))
    # baseline dashed
    s.append(f'<line x1="150" y1="{ypos(86.8):.1f}" x2="820" y2="{ypos(86.8):.1f}" stroke="{MUT}" stroke-width="2" stroke-dasharray="7 6"/>')
    s.append(t(158,ypos(86.8)-14,"基线 86.8%",21,MUT,"start","700"))
    # bars
    for x,p,lab,col in ((260,86.8,"一律答“不会”","#BFBFBF"),(560,95.3,"模型","#2F6DB5")):
        s.append(f'<rect x="{x}" y="{ypos(p):.1f}" width="150" height="{y0-ypos(p):.1f}" fill="{col}"/>')
        s.append(t(x+75,ypos(p)-16,f"{p}%",26,INK,"middle","700"))
        s.append(t(x+75,y0+34,lab,21,BODY,"middle"))
    # delta annotation
    s.append(f'<line x1="470" y1="{ypos(86.8):.1f}" x2="470" y2="{ypos(95.3):.1f}" stroke="{INK}" stroke-width="2"/>')
    s.append(t(482,(ypos(86.8)+ypos(95.3))/2+7,"+9 题",21,INK,"start","700"))
    s.append(t(150,y0+84,"这 9 题的来源：14 个真阳性里抓到 10 个（+10），误报 1 个（−1）",21,BODY))
    s.append(t(150,y0+118,"数值由论文给出的 11／10／95／4 计算，论文未给出基线",19,MUT))
    open(path,"w").write(wrap(W,H,"".join(s)))

if __name__=="__main__":
    d=os.path.dirname(os.path.abspath(__file__))
    fig_disinhibition(os.path.join(d,"fig-disinhibition.svg"))
    fig_baseline(os.path.join(d,"fig-baseline.svg"))
    print("ok")

# ---------------- 图 C：目录 ----------------
def fig_toc(path):
    W,H=900,545
    s=[]
    items=[("①","三件事，两条线","刷屏的 DOOM、3 月的虚拟果蝇、2024 年的论文，分别是什么"),
           ("②","复制了连接之后，还补了什么","连接组是静态的；让它跑起来的规则由建模选定"),
           ("③","预测怎么做，又怎么被检验","106 个细胞类型，模型算一遍，真果蝇做一遍"),
           ("④","完整动作从哪里来","脑模型、人工接口、身体控制器各承担什么"),
           ("⑤","能主张什么，不能主张什么","这一期的落点")]
    y=64
    s.append(t(0,y,"本期路线",28,INK,"start","700"))
    y+=26
    for num,head,sub in items:
        y+=76
        s.append(t(4,y,num,30,ACC,"start","700"))
        s.append(t(54,y,head,27,INK,"start","700"))
        s.append(t(54,y+34,sub,21,MUT))
    open(path,"w").write(wrap(W,H,"".join(s)))

# ---------------- 图 D：两条血脉 ----------------
def fig_lineage(path):
    W,H=900,500
    s=[DEFS]
    def lane(y,title,sub,items,color):
        o=[t(0,y,title,24,INK,"start","700"), t(0,y+30,sub,20,MUT)]
        xs=[0,300,600]
        for i,(x,(yr,name,note)) in enumerate(zip(xs,items)):
            o.append(f'<rect x="{x}" y="{y+56}" width="252" height="120" rx="10" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>')
            o.append(t(x+18,y+92,yr,21,color,"start","700"))
            o.append(t(x+18,y+124,name,23,INK,"start","700"))
            o.append(t(x+18,y+154,note,19,MUT))
            if i<len(items)-1:
                o.append(f'<line x1="{x+252}" y1="{y+116}" x2="{x+292}" y2="{y+116}" stroke="{MUT}" stroke-width="2" marker-end="url(#ar)"/>')
        return "".join(o)
    s.append(lane(40,"连续切片透射电镜（ssTEM）","一次覆盖全脑，数据脏，当年算法分割不了",
                  [("2018","FAFB 全脑 EM","一只成年雌果蝇"),("—","等算法追上","卷积网络解决对齐"),("2024","FlyWire 连接组","139,255 神经元")],ACC))
    s.append(f'<line x1="0" y1="260" x2="852" y2="260" stroke="{LINE}" stroke-width="1.5"/>')
    s.append(lane(300,"聚焦离子束扫描电镜（FIB-SEM）","数据干净、机器可直接分割，一次只能处理很小一块",
                  [("2020","hemibrain","中央脑一部分，无视叶"),("2024","MANC","雄性腹神经索"),("2026","MaleCNS v1.0","雄性完整中枢")],"#8A5A1E"))
    open(path,"w").write(wrap(W,H,"".join(s)))

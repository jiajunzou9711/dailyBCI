# -*- coding: utf-8 -*-
"""Brosler 2026 裁图：页面 300 dpi 渲染 → 窗口内按墨迹投影求包围盒，窗口需大于内容（边界贴窗即报警）。"""
import fitz, numpy as np
from PIL import Image
PDF="papers/brosler-2026-speech-gesture.pdf"; OUT="output/2026-09-29-speech-gesture/figs"
doc=fitz.open(PDF)
pages={}
def page(n,dpi=600):
    if (n,dpi) not in pages:
        pix=doc[n-1].get_pixmap(dpi=dpi); pages[(n,dpi)]=Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
    return pages[(n,dpi)]
def box(n,win,dpi=600,pad=16,mask=None):
    """win 以 300dpi 坐标给出 (x0,y0,x1,y1)；返回 600dpi 下的裁图。"""
    k=dpi/300; im=page(n,dpi); x0,y0,x1,y1=[int(v*k) for v in win]
    a=np.array(im.convert("L"))[y0:y1,x0:x1]; ink=a<235
    if mask: 
        for (mx0,my0,mx1,my1) in mask: ink[int(my0*k)-y0:int(my1*k)-y0, int(mx0*k)-x0:int(mx1*k)-x0]=False
    r=np.where(ink.any(1))[0]; c=np.where(ink.any(0))[0]
    bx=(x0+c[0],y0+r[0],x0+c[-1],y0+r[-1])
    touch=[n_ for n_,v in zip("LTRB",[c[0]==0,r[0]==0,c[-1]==ink.shape[1]-1,r[-1]==ink.shape[0]-1]) if v]
    if touch: print("  !! touches window edge",touch,win)
    out=im.crop((bx[0]-pad,bx[1]-pad,bx[2]+pad,bx[3]+pad)).copy()
    if mask:  # 面板字母涂白
        from PIL import ImageDraw
        dr=ImageDraw.Draw(out)
        for (mx0,my0,mx1,my1) in mask:
            dr.rectangle([int(mx0*k)-bx[0]+pad,int(my0*k)-bx[1]+pad,int(mx1*k)-bx[0]+pad,int(my1*k)-bx[1]+pad],fill="white")
    return out
def white(w,h): return Image.new("RGB",(w,h),"white")
def hcat(ims,gap=40):
    H=max(i.height for i in ims); W=sum(i.width for i in ims)+gap*(len(ims)-1); o=white(W,H); x=0
    for i in ims: o.paste(i,(x,(H-i.height)//2)); x+=i.width+gap
    return o
def vcat(ims,gap=40):
    W=max(i.width for i in ims); H=sum(i.height for i in ims)+gap*(len(ims)-1); o=white(W,H); y=0
    for i in ims: o.paste(i,((W-i.width)//2,y)); y+=i.height+gap
    return o

if __name__=="__main__":
    # 封面：图 1a，去掉面板字母 a
    a=box(3,(170,225,1560,757),mask=[(170,225,270,290)]); a.save(f"{OUT}/fig1a.png"); print("fig1a",a.size)
    # 卡①：图 1b 三个大脑横排 + 图例
    b3=box(3,(1570,347,2400,942)); b6=box(3,(1570,942,2400,1470)); b1=box(3,(1570,1470,2400,2005))
    hexl=box(3,(1570,2005,2400,2273)); mk=box(3,(1570,2273,2400,2528))
    fb=vcat([hcat([b3,b6,b1],60),hcat([hexl,mk],120)],40); fb.save(f"{OUT}/fig1b.png"); print("fig1b",fb.size)
    L=lambda x,y:(x-32,y-32,x+32,y+32)
    # 卡②：图 2b+2c
    f2=box(4,(360,865,2130,1360),mask=[L(396,904),L(855,904)]); f2.save(f"{OUT}/fig2bc.png"); print("fig2bc",f2.size)
    # 卡③：图 3c
    f3c=box(6,(325,700,895,1268),mask=[L(363,803)]); f3c.save(f"{OUT}/fig3c.png"); print("fig3c",f3c.size)
    # 卡④：图 3e+3f 横排 + 重叠分数图例
    e=box(6,(1400,250,1835,715),mask=[L(1449,284)]); f=box(6,(1400,830,1835,1225))
    lg=box(6,(1400,715,1835,830),mask=[L(1449,803)])
    f3ef=vcat([hcat([e,f],80),lg],30); f3ef.save(f"{OUT}/fig3ef.png"); print("fig3ef",f3ef.size)
    # 卡⑤：图 3g+3h 横排
    g=box(6,(1830,250,2200,745),mask=[L(1865,284)]); h=box(6,(1830,770,2200,1268),mask=[L(1865,803)])
    f3gh=hcat([g,h],80); f3gh.save(f"{OUT}/fig3gh.png"); print("fig3gh",f3gh.size)
    # 卡⑥：图 4a+4b
    f4ab=box(7,(430,215,2100,1270),mask=[L(462,244),L(462,640)]); f4ab.save(f"{OUT}/fig4ab.png"); print("fig4ab",f4ab.size)
    # 卡⑦：图 4c
    f4c=box(7,(430,1275,2100,2030),mask=[L(462,1307)]); f4c.save(f"{OUT}/fig4c.png"); print("fig4c",f4c.size)
    # 卡⑧：图 5a + 5b–d
    a5=box(8,(150,215,2330,860),mask=[L(186,244)]); bcd=box(8,(150,875,1765,1590),mask=[L(186,911),L(693,911),L(1257,911)])
    f5=vcat([a5,bcd],40); f5.save(f"{OUT}/fig5abcd.png"); print("fig5abcd",f5.size)
    # 版面收紧：卡⑥只用 4b，卡⑧只用 5a
    f4b=box(7,(430,610,2100,1270),mask=[L(462,640)]); f4b.save(f"{OUT}/fig4b.png"); print("fig4b",f4b.size)
    a5.save(f"{OUT}/fig5a.png"); print("fig5a",a5.size)
    f2a=box(4,(440,200,2100,862),mask=[L(410,244)]); f2a.save(f"{OUT}/fig2a.png"); print("fig2a",f2a.size)

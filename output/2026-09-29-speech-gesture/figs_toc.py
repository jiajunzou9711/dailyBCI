# -*- coding: utf-8 -*-
"""目录卡 SVG。viewBox 900 宽，2 倍像素输出；背景 #FAFAFA 与卡面一致。"""
import os, subprocess
BG="#FAFAFA"; INK="#1A1A1A"; MUT="#888888"; ACC="#2F6DB5"
FONT="-apple-system,'Helvetica Neue','Heiti SC','PingFang SC',sans-serif"
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"figs")
def t(x,y,s,size=22,fill=INK,weight="400"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}">{s}</text>'
items=[("①","以前的问题","同时做两件事，解码会不会互相干扰"),
       ("②","两路信号在同一块阵列上","部分触点被说话和手势共用"),
       ("③","训练数据决定准不准","训练时见过的情境里最准"),
       ("④","并行解码的两类错误","误触发与漏检各自怎么压下去"),
       ("⑤","实时驱动化身","实时准确率与离线接近"),
       ("⑥","回到问题与局限","干扰存在，调整训练数据可以处理")]
W,H=900,590
s=[t(0,50,"本期路线",28,INK,"700")]; y=50
for num,head,sub in items:
    y+=78
    s+=[t(4,y,num,30,ACC,"700"),t(54,y,head,27,INK,"700"),t(54,y+34,sub,21,MUT)]
svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*2}" height="{H*2}" font-family="{FONT}">'
     f'<rect width="{W}" height="{H}" fill="{BG}"/>{"".join(s)}</svg>')
hp=os.path.join(D,"toc.html"); open(hp,"w").write(f'<html><body style="margin:0">{svg}</body></html>')
subprocess.run(["npx","playwright","screenshot","file://"+hp,os.path.join(D,"fig-toc.png"),f"--viewport-size={W*2},{H*2}"],check=True,capture_output=True)
os.remove(hp); print("toc ok")

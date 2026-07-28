"""专题：硬脑膜第 ② 期（series-dura-02，经硬膜植入的三个工程问题）自制示意图。
SVG → PNG via playwright chromium。
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "series-dura-02", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"
RED = "#C0392B"; CARD_L = "#DCE5F0"
BONE = "#E6E2D8"; BONE_E = "#A9A499"
PER = "#F0C478"; MEN = "#CE8C3C"; PERE = "#A87B32"
CSF = "#D9EAF6"; CSF_E = "#8FBADA"
ARA = "#BFD9EC"
CTX = "#E4E7E2"; CTX_E = "#AEB4AC"
TOOL = "#6A7382"
GOLD = "#8A6D1A"; GOLDB = "#FBF7E9"; GOLDE = "#D9C98A"

DEFS = ('<defs>'
        '<marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" '
        'markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
        '<marker id="ahr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" '
        'markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
        '<marker id="ahs" markerWidth="9" markerHeight="9" refX="1" refY="3" orient="auto" '
        'markerUnits="strokeWidth"><path d="M7,0 L0,3 L7,6 Z" fill="%s"/></marker>'
        '<marker id="ahb" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" '
        'markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="%s"/></marker>'
        '</defs>' % (INK, RED, RED, ACCD))


def T(x, y, s, size=23, fill=INK, anchor="middle", weight="400", ls=None):
    e = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{e}>{s}</text>')


def box(x, y, w, h, fill, stroke, rx=8, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(x1, y1, x2, y2, stroke=INK, sw=2, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}{m}/>')


def header(title, w=1080):
    return (box(20, 14, w - 40, 52, TINT, ACC, 10, 1.5)
            + T(w / 2, 48, title, 27, ACCD, weight="700"))


def concl(y, l1, l2, w=1080):
    s = box(20, y, w - 40, 92, GOLDB, GOLDE, 10, 1.5)
    s += T(w / 2, y + 36, l1, 26, GOLD, weight="700")
    s += T(w / 2, y + 68, l2, 21, GOLD)
    return s


# ---------------- 目录卡 ----------------
def toc():
    W, H = 1080, 1440
    BG = "#141A22"
    s = [f'<rect width="{W}" height="{H}" fill="{BG}"/>']
    s.append(T(96, 132, "本期路线", 34, "#FFFFFF", anchor="start", weight="700"))
    s.append(T(96, 176, "TRANSDURAL  INSERTION", 18, "#6E8095", anchor="start", ls="4"))
    AX = 128
    y0, dy = 268, 178
    items = [
        ("01", "硬膜第一次被完整留下", "2026 年 5 月，多伦多"),
        ("02", "膜留着，多出三个问题", "深度、穿透、血管"),
        ("03", "深度从哪里量到哪里", "窗内的硬膜已与颅骨分离"),
        ("04", "脑有三种运动", "心跳、呼吸、脑移位"),
        ("05", "针为什么要加粗", "屈曲的四次方标度"),
        ("06", "送丝的四件套", "针、套管、pincher、线性电机"),
    ]
    s.append(f'<line x1="{AX}" y1="{y0-58}" x2="{AX}" y2="{y0+dy*5+34}" '
             f'stroke="#2C3946" stroke-width="2"/>')
    for i, (n, t, sub) in enumerate(items):
        y = y0 + dy * i
        s.append(f'<circle cx="{AX}" cy="{y-14}" r="6" fill="#4E7FB8"/>')
        s.append(T(AX + 34, y + 4, n, 52, "#3C5A7C", anchor="start", weight="700"))
        s.append(T(AX + 128, y - 6, t, 36, "#FFFFFF", anchor="start", weight="700"))
        s.append(T(AX + 130, y + 38, sub, 22, "#8397AC", anchor="start"))
    return W, H, "".join(s)


# ---------------- 04 三个问题 ----------------
def fig_three():
    W = 1080
    s = [header("膜留着，插入端同时多出三个问题", W)]
    s.append(T(W / 2, 112, "官方把挑战分成两条：机械穿透，以及隔着硬膜获取信息", 22, BODY))
    rows = [
        ("①", "深　度", "目标是皮层表面，而它到硬膜顶面的距离在持续变化", ACC, "本篇"),
        ("②", "穿　透", "硬膜坚韧，而针是几十微米的细杆，先屈曲再说", ACC, "本篇"),
        ("③", "血　管", "硬膜不透明，原本靠直视避开的血管现在看不见", GRAY, "下期"),
    ]
    y = 154
    for num, name, desc, col, tag in rows:
        s.append(box(30, y, W - 60, 132, "#FFFFFF" if col == ACC else "#FAFAFA",
                     CARD_L if col == ACC else "#E4E4E4", 12, 1.6))
        s.append(T(92, y + 84, num, 54, col, weight="700"))
        s.append(T(150, y + 60, name, 32, INK if col == ACC else GRAY,
                   anchor="start", weight="700"))
        s.append(T(150, y + 104, desc, 22, BODY if col == ACC else GRAY, anchor="start"))
        tc = ACCD if tag == "本篇" else GRAY
        s.append(box(W - 148, y + 42, 88, 44, TINT if tag == "本篇" else "#F0F0F0",
                     tc, 22, 1.2))
        s.append(T(W - 104, y + 71, tag, 21, tc, weight="700"))
        y += 150
    return W, y + 16, "".join(s)


# ---------------- 06 深度从哪里量到哪里 ----------------
def fig_gap():
    W = 1080
    s = [header("这段深度，从硬膜顶面量到皮层表面", W)]

    XL, XR = 60, 600
    wl, wr = 230, 430
    LX = 648

    yb, bh = 170, 42
    ybb = yb + bh
    for x0, x1 in ((XL, wl), (wr, XR)):
        s.append(box(x0, yb, x1 - x0, bh, BONE, BONE_E, 5, 1.8))
        xx = x0 + 16
        while xx < x1 - 12:
            s.append(f'<ellipse cx="{xx}" cy="{yb+21}" rx="7" ry="5" fill="#CFC8B8"/>')
            xx += 28
    s.append(T(XL, yb - 16, "颅骨", 21, BODY, anchor="start"))
    s.append(T(330, yb - 16, "开颅窗", 21, GRAY, weight="700"))
    s.append(T(330, yb + 30, "窗内已与颅骨分离", 19, RED))
    s.append(f'<line x1="330" y1="{yb+42}" x2="330" y2="{ybb+14}" stroke="{RED}" '
             f'stroke-width="1.8" marker-end="url(#ahr)"/>')

    # 窗缘处硬膜与骨相连
    gap = 18
    for x0, x1 in ((XL, wl), (wr, XR)):
        s.append(f'<rect x="{x0}" y="{ybb}" width="{x1-x0}" height="{gap}" fill="{PER}"/>')

    yd = ybb + gap
    s.append(box(XL, yd, XR - XL, 22, PER, PERE, 3, 1.4))
    ya = yd + 22
    s.append(box(XL, ya, XR - XL, 11, ARA, CSF_E, 2, 1.0))
    yc = ya + 11
    s.append(box(XL, yc, XR - XL, 80, CSF, CSF_E, 3, 1.2))
    s.append(T(XL + 14, yc + 34, "蛛网膜下腔", 21, "#3D7CA8", anchor="start"))
    s.append(T(XL + 14, yc + 60, "（脑脊液）", 20, "#3D7CA8", anchor="start"))
    yp = yc + 80
    s.append(box(XL, yp, XR - XL, 9, "#8FB6D4", CSF_E, 2, 1.0))
    ycx = yp + 9
    s.append(box(XL, ycx, XR - XL, 96, CTX, CTX_E, 10, 1.6))
    s.append(T(XL + 26, ycx + 58, "皮层", 27, "#5A5F5A", anchor="start"))

    def lead(ysrc, ylab, txt, col, size=21):
        return (f'<polyline points="{XR},{ysrc} {LX-30},{ysrc} {LX-12},{ylab-7}" '
                f'fill="none" stroke="{col}" stroke-width="1.6"/>'
                + T(LX, ylab, txt, size, col, anchor="start", weight="700"))

    s.append(lead(yd + 11, yd + 16, "硬脑膜", PERE))
    s.append(T(LX, yd + 44, "窗缘处仍与颅骨附着", 19, PERE, anchor="start"))
    s.append(lead(ya + 5, ya + 60, "蛛网膜", "#3D7CA8"))
    s.append(lead(yp + 4, yp + 10, "软脑膜", "#3D7CA8"))

    xm = 500
    s.append(f'<line x1="{xm}" y1="{yd+2}" x2="{xm}" y2="{ycx-2}" stroke="{RED}" '
             f'stroke-width="3" marker-start="url(#ahs)" marker-end="url(#ahr)"/>')
    s.append(box(LX - 8, ycx + 14, 380, 68, "#FFFFFF", RED, 8, 2))
    s.append(T(LX + 182, ycx + 44, "针要走的这段", 23, RED, weight="700"))
    s.append(T(LX + 182, ycx + 70, "OCT 测的就是它", 20, RED))

    yz = ycx + 126
    s.append(concl(yz, "「保留硬膜」的含义是它没被切开、没被移除",
                   "窗内它已与颅骨分离；与皮层之间还隔着蛛网膜与脑脊液", W))
    return W, yz + 116, "".join(s)


# ---------------- 07 三种运动 ----------------
def fig_motion():
    W = 1080
    s = [header("植入过程中，脑有三种运动", W)]
    s.append(T(60, 112, "来源", 21, GRAY, anchor="start"))
    s.append(T(300, 112, "时间尺度", 21, GRAY, anchor="start"))
    s.append(T(470, 112, "量级", 21, GRAY, anchor="start"))
    s.append(T(760, 112, "出处", 21, GRAY, anchor="start"))
    s.append(line(56, 126, 1024, 126, "#DDDDDD", 1.5))

    rows = [
        ("心跳搏动", "约 1 秒", "0.1–0.5 mm", ACC, "Enzmann & Pelc 1992"),
        ("呼　　吸", "约 4 秒", "约为心跳的 1/3", "#7FA8C9", "Sloots 2020"),
        ("脑 移 位", "术中数十分钟", "数毫米", RED, "Hill 1998"),
    ]
    y = 158
    for name, ts, amp, col, src in rows:
        s.append(T(60, y + 26, name, 25, INK, anchor="start", weight="700"))
        s.append(T(300, y + 26, ts, 22, BODY, anchor="start"))
        s.append(T(470, y + 26, amp, 23, col, anchor="start", weight="700"))
        s.append(T(760, y + 26, src, 19, GRAY, anchor="start"))
        y += 74
    s.append(line(56, y + 2, 1024, y + 2, "#DDDDDD", 1.5))

    s.append(box(30, y + 26, W - 60, 78, "#F4F8FC", CARD_L, 10, 1.5))
    s.append(T(W / 2, y + 58, "对照：电极丝上相邻记录位点的间距 = 50 µm = 0.05 mm",
               24, ACCD, weight="700"))
    s.append(T(W / 2, y + 88, "心跳这一项，已经是位点间距的 2–10 倍", 21, BODY))

    yz = y + 128
    s.append(box(30, yz, W - 60, 96, "#FFFFFF", "#E0E0E0", 10, 1.4))
    s.append(T(W / 2, yz + 34, "呼吸那一栏测的是体积应变，不是位移", 22, BODY, weight="700"))
    s.append(T(W / 2, yz + 66, "7T MRI 下心跳引起的体积应变约为呼吸的 3 倍，两者不能直接换算",
               20, GRAY))
    return W, yz + 128, "".join(s)


# ---------------- 08 脑移位 ----------------
def fig_shift():
    W = 1080
    s = [header("毫米级的脑移位，只在切开硬膜之后出现", W)]
    s.append(T(W / 2, 110, "Hill 等 1998，21 名患者，骨内标记配准到术前 MRI", 21, GRAY))

    SC = 620.0 / 6.0
    X0 = 300
    rows = [
        ("硬　膜", "开硬膜前", 1.2, "#9AA7B4"),
        ("脑表面", "开硬膜后 第一次", 4.4, "#C0603B"),
        ("脑表面", "约一小时后 第二次", 5.6, RED),
    ]
    y = 152
    for name, when, val, col in rows:
        s.append(T(60, y + 30, name, 25, INK, anchor="start", weight="700"))
        s.append(T(60, y + 58, when, 19, GRAY, anchor="start"))
        s.append(f'<rect x="{X0}" y="{y+16}" width="{val*SC:.0f}" height="34" '
                 f'rx="5" fill="{col}"/>')
        s.append(T(X0 + val * SC + 14, y + 42, f"{val} mm", 25, col,
                   anchor="start", weight="700"))
        y += 92
    # 误差带
    s.append(f'<rect x="{X0}" y="150" width="{2*SC:.0f}" height="{y-158}" '
             f'fill="#000000" opacity="0.055"/>')
    s.append(f'<line x1="{X0+2*SC}" y1="150" x2="{X0+2*SC}" y2="{y-8}" '
             f'stroke="{GRAY}" stroke-width="1.6" stroke-dasharray="6,5"/>')
    s.append(T(X0 + 2 * SC + 10, y + 16, "测量误差 1–2 mm", 19, GRAY, anchor="start"))

    yy = y + 44
    s.append(box(30, yy, W - 60, 86, "#FDF3F1", "#E5B9AF", 10, 1.5))
    s.append(T(W / 2, yy + 36, "最大位移超过 10 mm：第一次测量约占 1/3 患者，第二次约占 1/2",
               23, "#A03A28", weight="700"))
    s.append(T(W / 2, yy + 66, "均值严重低估最坏情况；方向一致，全部是脑相对术前位置下沉",
               20, BODY))

    yz = yy + 106
    s.append(concl(yz, "推论：大位移主要由开硬膜后的脑脊液流失驱动",
                   "硬膜读数取自开膜前、脑表面取自开膜后；目前仅此一项间接证据", W))
    return W, yz + 116, "".join(s)


# ---------------- 11 钨铼 ----------------
def fig_material():
    W = 1080
    s = [header("用钨是为了刚度，加铼是为了不脆断", W)]
    s.append(T(W / 2, 108, "P_cr = π²EI/(KL)²　—　E 越大，同样几何下越难屈曲", 23, ACCD,
               weight="700"))

    SC = 560.0 / 420.0
    X0 = 330
    mats = [("钨　　W", 400, ACC), ("不锈钢", 200, "#9AA7B4"), ("钛　　Ti", 110, "#B9C2CB")]
    y = 148
    for name, e, col in mats:
        s.append(T(60, y + 34, name, 25, INK, anchor="start", weight="700"))
        s.append(f'<rect x="{X0}" y="{y+12}" width="{e*SC:.0f}" height="36" rx="5" fill="{col}"/>')
        s.append(T(X0 + e * SC + 14, y + 40, f"≈ {e} GPa", 24, col, anchor="start", weight="700"))
        y += 74
    s.append(T(60, y + 20, "弹性模量。同样直径换成不锈钢，抗屈曲能力直接减半。", 21, BODY,
               anchor="start"))

    yy = y + 48
    s.append(box(30, yy, 500, 190, "#FAFAFA", "#E0E0E0", 12, 1.5))
    s.append(T(280, yy + 44, "纯钨的代价", 26, INK, weight="700"))
    s.append(T(280, yy + 88, "室温下脆", 23, BODY))
    s.append(T(280, yy + 124, "韧脆转变温度高于室温", 21, GRAY))
    s.append(T(280, yy + 158, "细丝弯折、装配、插拔易脆性断裂", 20, GRAY))

    s.append(box(550, yy, 500, 190, TINT, ACC, 12, 1.5))
    s.append(T(800, yy + 44, "加铼：「铼效应」", 26, ACCD, weight="700"))
    s.append(T(800, yy + 88, "提高低温延展性", 23, ACCD))
    s.append(T(800, yy + 124, "W-3%Re：韧脆转变温度低约 100°C", 20, BODY))
    s.append(T(800, yy + 158, "总延伸率高 10–35%", 20, BODY))

    yz = yy + 212
    s.append(concl(yz, "工程上常用 5–26 at.% 铼改善低温延展性，断裂韧性最多提高一个数量级",
                   "铼效应随成分与温度变化，高铼含量下固溶强化反而可能抬高韧脆转变温度", W))
    return W, yz + 116, "".join(s)


# ---------------- 12 d⁴ ----------------
def fig_d4():
    W = 1080
    s = [header("直径加一点，抗屈曲能力涨的是四次方", W)]
    s.append(T(W / 2, 108, "I = πd⁴/64　代回　P_cr = π²EI/(KL)²　得　P_cr ∝ d⁴", 24, ACCD,
               weight="700"))

    # 坐标系
    OX, OY, PW, PH = 150, 620, 520, 420
    s.append(line(OX, OY, OX + PW, OY, INK, 2))
    s.append(line(OX, OY, OX, OY - PH, INK, 2))
    s.append(T(OX + PW / 2, OY + 46, "针的直径 d", 22, BODY))
    s.append(f'<text x="{OX-52}" y="{OY-PH/2}" font-size="22" fill="{BODY}" '
             f'text-anchor="middle" transform="rotate(-90 {OX-52} {OY-PH/2})">'
             f'临界屈曲载荷 P_cr</text>')
    pts = []
    for i in range(0, 101):
        t = i / 100.0
        x = OX + t * PW
        yv = OY - (t ** 4) * PH
        pts.append(f"{x:.1f},{yv:.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ACC}" stroke-width="3.5"/>')
    # 标注两点
    for t, lab, col in ((0.705, "旧", "#9AA7B4"), (1.0, "新", RED)):
        x = OX + t * PW; yv = OY - (t ** 4) * PH
        s.append(f'<circle cx="{x:.1f}" cy="{yv:.1f}" r="8" fill="{col}"/>')
        s.append(line(x, OY, x, yv, col, 1.6, "5,5"))
        s.append(T(x, OY + 28, lab, 22, col, weight="700"))
    s.append(T(OX + PW - 30, OY - PH + 62, "×4", 32, RED, anchor="end", weight="700"))

    # 右侧数据
    RX = 720
    s.append(box(RX, 190, 320, 250, "#FFFFFF", CARD_L, 12, 1.6))
    s.append(T(RX + 160, 232, "按 100 µm 标尺自测", 22, GRAY, weight="700"))
    s.append(T(RX + 160, 288, "旧针　约 43 µm", 26, "#7A8792", weight="700"))
    s.append(T(RX + 160, 336, "新针　约 61 µm", 26, RED, weight="700"))
    s.append(line(RX + 40, 362, RX + 280, 362, "#E0E0E0", 1.5))
    s.append(T(RX + 160, 396, "比值 1.42　→　P_cr 约 4 倍", 23, ACCD, weight="700"))

    s.append(box(RX, 462, 320, 158, "#FDF3F1", "#E5B9AF", 12, 1.5))
    s.append(T(RX + 160, 502, "这是本人在视频帧上", 20, "#A03A28", weight="700"))
    s.append(T(RX + 160, 532, "的像素测量，非公开数值", 20, "#A03A28", weight="700"))
    s.append(T(RX + 160, 570, "默认标尺对两幅图同时适用", 19, BODY))
    s.append(T(RX + 160, 600, "仅供量级参考", 19, BODY))

    yz = 700
    s.append(concl(yz, "43 µm 与 2019 年论文所说的 40 µm 线材原始直径吻合",
                   "官方措辞是「just slightly」；落到力学上是四次方", W))
    return W, yz + 116, "".join(s)


# ---------------- 14 自由长度 ----------------
def fig_len():
    W = 1080
    s = [header("套管的作用是缩短自由长度", W)]
    s.append(T(W / 2, 108, "P_cr = π²EI/(KL)²　—　L 是杆上没有横向支撑的那一段", 23, ACCD,
               weight="700"))
    s.append(T(W / 2, 142, "取钨铼 E ≈ 400 GPa，d = 24 µm，K = 1", 20, GRAY))

    s.append(T(90, 200, "自由长度 L", 21, GRAY, anchor="start"))
    s.append(T(400, 200, "临界屈曲载荷 P_cr", 21, GRAY, anchor="start"))
    s.append(T(740, 200, "约相当于压上", 21, GRAY, anchor="start"))
    s.append(line(80, 214, 1000, 214, "#DDDDDD", 1.5))

    rows = [("20 mm（整根裸露）", "0.16 mN", "16 mg", RED),
            ("2 mm", "16 mN", "1.6 g", "#B08A3A"),
            ("0.5 mm", "257 mN", "26 g", ACC)]
    y = 244
    for l, p, w8, col in rows:
        s.append(T(90, y + 34, l, 25, INK, anchor="start", weight="700"))
        s.append(T(400, y + 34, p, 28, col, anchor="start", weight="700"))
        s.append(T(740, y + 34, w8, 25, BODY, anchor="start"))
        y += 82
    s.append(line(80, y + 4, 1000, y + 4, "#DDDDDD", 1.5))

    yy = y + 30
    s.append(box(30, yy, W - 60, 86, "#FDF3F1", "#E5B9AF", 10, 1.5))
    s.append(T(W / 2, yy + 36, "一根 24 µm 的针若 20 mm 全裸露，16 毫克就能把它压弯",
               25, "#A03A28", weight="700"))
    s.append(T(W / 2, yy + 66, "L 减到 1/10，P_cr 涨 100 倍", 21, BODY))

    yz = yy + 106
    s.append(concl(yz, "官方只给过几何：套管外径 150 µm、内孔 60 µm",
                   "2019 年论文未描述套管功能，上述为力学推论；K 与 L 均为假设值", W))
    return W, yz + 116, "".join(s)


# ---------------- 15 四零件 ----------------
def fig_parts():
    W = 1080
    s = [header("四个部件各管一件事", W)]

    # 左侧示意
    CX = 228
    # 组织
    s.append(f'<rect x="80" y="500" width="420" height="60" rx="6" fill="{CTX}"/>')
    s.append(line(80, 500, 500, 500, CTX_E, 2.5))
    s.append(T(430, 534, "组织表面", 19, GRAY, anchor="start"))
    # 套管
    s.append(box(CX - 28, 150, 56, 240, "#C9D2DA", "#8B96A2", 5, 1.8))
    # 针
    s.append(f'<line x1="{CX}" y1="160" x2="{CX}" y2="480" stroke="#5A6570" stroke-width="7"/>')
    s.append(f'<path d="M{CX-4},480 L{CX+4},480 L{CX},504 Z" fill="#3E4750"/>')
    # 丝的环 + 丝
    s.append(f'<circle cx="{CX}" cy="462" r="10" fill="none" stroke="{ACC}" stroke-width="3.2"/>')
    s.append(f'<path d="M{CX+10},456 C330,430 300,250 420,196" fill="none" '
             f'stroke="{ACC}" stroke-width="3.2"/>')
    # pincher
    s.append(f'<path d="M272,210 L272,440 L238,440" fill="none" stroke="#B08A3A" '
             f'stroke-width="5.5" stroke-linejoin="round"/>')

    # 引线标签
    def lb(x1, y1, x2, y2, tx, ty, txt, col, anchor="start"):
        return (f'<polyline points="{x1},{y1} {x2},{y2}" fill="none" stroke="{col}" '
                f'stroke-width="1.5"/>' + T(tx, ty, txt, 21, col, anchor=anchor, weight="700"))

    s.append(lb(196, 250, 148, 250, 140, 256, "套管", "#4A5560", "end"))
    s.append(lb(222, 470, 148, 470, 140, 476, "针", "#3E4750", "end"))
    s.append(lb(272, 400, 340, 400, 348, 406, "pincher", "#8A6D1A"))
    s.append(T(348, 434, "50 µm 钨丝，末端折弯", 18, GRAY, anchor="start"))
    s.append(T(430, 190, "电极丝", 21, ACC, anchor="start", weight="700"))
    s.append(lb(238, 466, 320, 490, 328, 496, "丝末端的环", ACC))

    # 右侧分工
    RX = 540
    items = [
        ("针", "钩住丝末端 16×50 µm² 的环，并穿透硬膜", "#3E4750"),
        ("套管", "缩短自由长度，防止针屈曲；不进脑", "#5A6570"),
        ("pincher", "运送中托住丝，插入时约束丝沿针的路径", "#8A6D1A"),
        ("线性电机", "以最高 30,000 mm/s² 急退，让丝脱钩", ACC),
    ]
    y = 128
    for name, desc, col in items:
        s.append(box(RX, y, 510, 104, "#FFFFFF", CARD_L, 10, 1.5))
        s.append(T(RX + 24, y + 44, name, 26, col, anchor="start", weight="700"))
        s.append(T(RX + 24, y + 82, desc, 20, BODY, anchor="start"))
        y += 118
    return W, max(y + 16, 600), "".join(s)


FIGS = {"toc": toc, "fig-three": fig_three, "fig-gap": fig_gap,
        "fig-motion": fig_motion, "fig-shift": fig_shift,
        "fig-material": fig_material, "fig-d4": fig_d4,
        "fig-len": fig_len, "fig-parts": fig_parts}


def render(name, w, h, inner):
    bg = "" if name == "toc" else f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>'
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" font-family="HeitiSC,Helvetica,Arial,sans-serif">'
           f'{DEFS}{bg}{inner}</svg>')
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'@font-face{{font-family:"HeitiSC";src:url("file://{FONT}");}}'
            f'*{{margin:0;padding:0}}body{{width:{w}px;height:{h}px}}</style></head>'
            f'<body>{svg}</body></html>')
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, name + ".png")
    subprocess.run(["npx", "playwright", "screenshot", f"file://{tmp.name}", out,
                    f"--viewport-size={w},{h}", "--wait-for-timeout=600"],
                   check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    return out


if __name__ == "__main__":
    import sys
    only = sys.argv[1:] or list(FIGS)
    for name in only:
        w, h, inner = FIGS[name]()
        print("rendered", render(name, w, h, inner), f"({w}x{h})")

"""闭环图案化视网膜刺激（2026-08-13 日报）— 自制 SVG 示意图。
本期只需要目录卡；正文图卡全部使用论文原图裁图。
"""
import os, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
FONT = os.path.join(SKILL_DIR, "fonts", "HeitiSC-Subset.ttf")
PROJECT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
OUT = os.path.join(PROJECT, "output", "2026-08-13-retinal-closed-loop", "figs")
os.makedirs(OUT, exist_ok=True)

ACC = "#2F6DB5"; ACCD = "#1E4E86"; TINT = "#E9F0F8"
INK = "#1A1A1A"; BODY = "#4A4A4A"; GRAY = "#8A8A8A"
CARD_L = "#DCE5F0"
BG = "#FAFAFA"   # 必须与卡面一致,否则卡上出现白方块


def T(x, y, s, size=25, fill=INK, anchor="middle", weight="400"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}">{s}</text>')


def box(x, y, w, h, fill, stroke, rx=12, sw=1.5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def circ(cx, cy, r, fill, stroke, sw=1.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


def toc():
    s = []
    items = [
        ("1", "一个从没被核对的假设", "图案投进眼睛，落点无人核对"),
        ("2", "为什么这件事值得关心", "青光眼：细胞死掉之前，功能先坏吗"),
        ("3", "为什么必须在活体上做", "感受野需要空间结构；离体拿不到时间轴"),
        ("4", "三道障碍，合起来才是闭环", "看得见、切得动、机器判得准"),
        ("5", "活体上能看到多细", "30 µm，与视锥间距 9 µm 相比"),
        ("6", "局限性与落点", "写入端有多准，长期以假设的形式存在"),
    ]
    y = 30
    for n, title, sub in items:
        s.append(box(30, y, 900, 78, "#F7F9FC", CARD_L, 14, 1.5))
        s.append(circ(78, y + 39, 26, TINT, ACC, 1.5))
        s.append(T(78, y + 49, n, 30, ACCD, weight="700"))
        s.append(T(126, y + 34, title, 30, INK, anchor="start", weight="700"))
        s.append(T(126, y + 64, sub, 21, GRAY, anchor="start"))
        y += 92
    return 960, y, "".join(s)


def render(name, fn, scale=2):
    w, h, body = fn()
    W, H = w * scale, h * scale
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'viewBox="0 0 {w} {h}">'
           f'<rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')
    html = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'><style>"
        f"@font-face{{font-family:'HeitiSC';src:url('file://{FONT}') format('truetype');}}"
        f"html,body{{margin:0;padding:0;background:{BG};}}"
        "svg text{font-family:'HeitiSC','Helvetica Neue',Arial,sans-serif;}"
        f"</style></head><body>{svg}</body></html>"
    )
    tmp = tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8")
    tmp.write(html); tmp.close()
    out = os.path.join(OUT, f"{name}.png")
    subprocess.run(
        ["npx", "playwright", "screenshot", f"file://{tmp.name}", out,
         f"--viewport-size={W},{H}", "--wait-for-timeout=700"],
        check=True, capture_output=True, text=True)
    os.unlink(tmp.name)
    print("wrote", out)


if __name__ == "__main__":
    render("toc", toc)

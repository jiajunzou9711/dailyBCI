"""
DailyBCI Card Generator (HTML + Playwright renderer)
====================================================
Reusable template for generating 小红书 card images.

Style: Academic minimal (Nature Briefing inspired)
Renderer: HTML/CSS templates screenshotted by Chromium via `npx playwright`.
Fonts: system Latin (Helvetica/Arial) + bundled Heiti SC (CJK, subsetted ttf
       — GB2312 + knowledge-base glyphs, ~6MB).
Attribution: 小邹 × Claude (小红书) / xiaozou × Claude (X thread)

The public API is UNCHANGED from the previous Pillow implementation — same four
methods with the same signatures — so the daily-run workflow does not change:

    from card_generator import CardGenerator
    gen = CardGenerator(date="2026.06.07")
    gen.cover_card("标题第一行", "标题第二行", "一句话核心发现。", "output/01-cover.png", source="解读块…")
    gen.figure_card("papers/fig1.png", "Fig. 1", ["评注…"], "output/02-figure.png")
    gen.text_card("小标题", ["段落1…", "段落2…"], "output/03-text.png")
    gen.tail_card(["¹ Ref 1…", "² Ref 2…"], "output/05-tail.png")

Inline emphasis: wrap a key term/number in **double asterisks** inside any text
string to render it in the accent colour + bold (e.g. "样本为 **2 名** 参与者").
Plain strings without ** render exactly as before. Superscripts ¹²³⁴⁵ render
natively via the Latin font (no substitution table needed).

Requirements (one-time):
    npm install -g playwright   (or rely on `npx playwright`)
    npx playwright install chromium
"""

import os
import re
import html
import tempfile
import subprocess

# =============================================================================
# Constants
# =============================================================================

W, H = 1080, 1440          # 小红书 standard portrait ratio
MARGIN = 100               # generous side margins (px)
BG_COLOR = '#FAFAFA'       # near-white background

# Color palette (grayscale hierarchy + one restrained academic accent)
COLOR_TITLE = '#1A1A1A'     # darkest — titles
COLOR_BODY = '#444444'      # body text
COLOR_SUBTITLE = '#666666'  # subtitles / secondary text
COLOR_CAPTION = '#888888'   # figure captions, references
COLOR_MUTED = '#999999'     # tertiary text
COLOR_BRAND = '#BBBBBB'     # brand, date, signature
COLOR_LINE = '#E0E0E0'      # separator lines
COLOR_ACCENT = '#2F6DB5'    # single accent — used only for **highlighted** terms

# Font sizes (px) — mirror the previous Pillow hierarchy
SIZE_TITLE_LG = 64
SIZE_TITLE_MD = 52
SIZE_SUBTITLE = 34
SIZE_BODY = 32
SIZE_ANNOTATION = 30
SIZE_CAPTION = 26
SIZE_SMALL = 24
SIZE_BRAND = 22

# Bundled CJK font (Heiti SC, simplified). scripts/ and fonts/ are siblings.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_SKILL_DIR = os.path.dirname(_SCRIPT_DIR)            # .claude/skills/dailybci/
_FONTS_DIR = os.path.join(_SKILL_DIR, "fonts")
_CJK_FONT = os.path.join(_FONTS_DIR, "HeitiSC-Subset.ttf")


def _file_url(path):
    """Absolute file:// URL for a local asset (font / figure)."""
    return "file://" + os.path.abspath(path)


# =============================================================================
# Shared CSS
# =============================================================================

def _base_css():
    return f"""
    @font-face {{
        font-family: "HeitiSC";
        src: url("{_file_url(_CJK_FONT)}");
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    :root {{
        --title: {COLOR_TITLE}; --body: {COLOR_BODY}; --subtitle: {COLOR_SUBTITLE};
        --caption: {COLOR_CAPTION}; --muted: {COLOR_MUTED}; --brand: {COLOR_BRAND};
        --line: {COLOR_LINE}; --accent: {COLOR_ACCENT};
    }}
    body {{ width: {W}px; height: {H}px; overflow: hidden; }}
    .card {{
        position: relative; width: {W}px; height: {H}px; background: {BG_COLOR};
        font-family: "Helvetica Neue", "Arial", "HeitiSC", sans-serif;
        padding: 70px {MARGIN}px; color: var(--title);
    }}
    b {{ color: var(--accent); font-weight: 700; }}
    .brand {{ font-size: {SIZE_BRAND}px; font-weight: 700; letter-spacing: 1px; color: var(--brand); }}
    .footer {{
        position: absolute; left: {MARGIN}px; right: {MARGIN}px; bottom: 70px;
        display: flex; justify-content: space-between;
        font-size: {SIZE_BRAND}px; color: var(--brand);
    }}
    .sep {{ height: 1px; background: var(--line); }}

    /* cover */
    .title {{ margin-top: 200px; font-size: {SIZE_TITLE_LG}px; font-weight: 800;
              line-height: 1.45; letter-spacing: 1px; color: var(--title); }}
    .subtitle {{ margin-top: 56px; font-size: {SIZE_SUBTITLE}px; font-weight: 400;
                 line-height: 1.6; color: var(--subtitle); }}
    .read-label {{ margin-top: 30px; font-size: {SIZE_CAPTION}px; font-weight: 700;
                   letter-spacing: 2px; color: var(--muted); }}
    .read-body {{ margin-top: 14px; font-size: {SIZE_CAPTION}px; line-height: 1.55; color: var(--caption); }}
    .cover-sep {{ margin-top: 46px; }}

    /* figure */
    .figwrap {{ margin: 60px -36px 0; border: 1px solid var(--line); background: #fff;
                display: flex; align-items: center; justify-content: center; overflow: hidden; }}
    .figwrap img {{ max-width: 100%; width: auto; height: auto; display: block; }}
    .fig-sep {{ margin-top: 28px; }}
    .figlabel {{ margin-top: 24px; font-size: {SIZE_CAPTION}px; font-weight: 700;
                 letter-spacing: 1px; color: var(--muted); }}
    .annot {{ margin-top: 22px; font-size: {SIZE_ANNOTATION}px; line-height: 1.62; color: var(--body); }}

    /* text */
    .heading {{ margin-top: 90px; font-size: {SIZE_TITLE_MD}px; font-weight: 800;
                line-height: 1.4; color: var(--title); }}
    .para {{ margin-top: 26px; font-size: {SIZE_BODY}px; line-height: 1.65; color: var(--body); }}
    .heading + .para {{ margin-top: 36px; }}

    /* tail */
    .lead {{ margin-top: 90px; font-size: {SIZE_BODY}px; line-height: 1.6; color: var(--body); }}
    .lead + .lead {{ margin-top: 20px; }}
    .refs-heading {{ margin-top: 56px; font-size: {SIZE_SUBTITLE}px; font-weight: 800; color: var(--title); }}
    .ref {{ margin-top: 16px; font-size: {SIZE_SMALL}px; line-height: 1.45; color: var(--caption); }}
    .ref.spacer {{ margin-top: 8px; }}
    .sigblock {{ position: absolute; left: {MARGIN}px; right: {MARGIN}px; bottom: 150px; }}
    .sigblock .sig-sep {{ margin-bottom: 36px; }}
    .signame {{ font-size: {SIZE_BODY}px; font-weight: 700; color: var(--body); }}
    .sigtag {{ margin-top: 14px; font-size: {SIZE_SMALL}px; color: var(--muted); }}
    """


# =============================================================================
# CardGenerator
# =============================================================================

class CardGenerator:
    """Generate DailyBCI 小红书 card images via HTML templates + Chromium."""

    def __init__(self, date="", platform="xiaohongshu"):
        """
        Args:
            date: Display date string, e.g. "2026.06.07"
            platform: "xiaohongshu" or "x" — controls signature
        """
        self.date = date
        self.signature = "小邹 × Claude" if platform == "xiaohongshu" else "xiaozou × Claude"

    # ---- text helpers ----

    def _fmt(self, text):
        """HTML-escape a string, then turn **emphasis** into accent <b>, \\n into <br>."""
        s = html.escape(str(text))
        s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
        s = s.replace('\n', '<br>')
        return s

    def _page(self, body_html):
        """Wrap a card body in the shared page shell (brand + body + footer)."""
        return (
            "<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<style>{_base_css()}</style></head><body>"
            "<div class='card'>"
            "<div class='brand'>DailyBCI</div>"
            f"{body_html}"
            f"<div class='footer'><span>{html.escape(self.date)}</span>"
            f"<span>{html.escape(self.signature)}</span></div>"
            "</div></body></html>"
        )

    def _render(self, html_str, output_path):
        """Write HTML to a temp file and screenshot it to output_path at 1080×1440."""
        out_dir = os.path.dirname(output_path) or "."
        os.makedirs(out_dir, exist_ok=True)
        tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
        try:
            tmp.write(html_str)
            tmp.close()
            subprocess.run(
                ["npx", "playwright", "screenshot", _file_url(tmp.name), output_path,
                 f"--viewport-size={W},{H}", "--wait-for-timeout=700"],
                check=True, capture_output=True, text=True,
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"playwright screenshot failed for {output_path}:\n{e.stderr}"
            ) from e
        finally:
            os.unlink(tmp.name)
        return output_path

    # ---- card types ----

    def cover_card(self, title_line1, title_line2, subtitle, output_path, source=None):
        """Cover card: two-line Chinese title, one-sentence finding, optional 解读 block."""
        body = (
            f"<div class='title'>{self._fmt(title_line1)}<br>{self._fmt(title_line2)}</div>"
            f"<div class='subtitle'>{self._fmt(subtitle)}</div>"
        )
        if source:
            body += (
                "<div class='sep cover-sep'></div>"
                "<div class='read-label'>解读</div>"
                f"<div class='read-body'>{self._fmt(source)}</div>"
            )
        return self._render(self._page(body), output_path)

    def figure_card(self, figure_path_or_image, caption_label, annotation_paragraphs,
                    output_path, figure_height=560):
        """Figure card: a REAL paper figure (image) on top, caption label, annotations.

        figure_path_or_image may be a path str or a PIL.Image (saved to a temp PNG).
        Figures are embedded verbatim via <img> — never AI-generated.
        """
        fig_path = figure_path_or_image
        tmp_fig = None
        if not isinstance(figure_path_or_image, str):
            from PIL import Image  # lazy: only needed when a PIL image is passed
            tmp_fig = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
            tmp_fig.close()
            img = figure_path_or_image
            if not isinstance(img, Image.Image):
                raise TypeError("figure_path_or_image must be a path or PIL.Image")
            img.save(tmp_fig.name)
            fig_path = tmp_fig.name

        try:
            annots = "".join(
                f"<div class='annot'>{self._fmt(p)}</div>" for p in annotation_paragraphs
            )
            body = (
                f"<div class='figwrap' style='max-height:{figure_height}px'>"
                f"<img src='{_file_url(fig_path)}' style='max-height:{figure_height}px'>"
                "</div>"
                "<div class='sep fig-sep'></div>"
                f"<div class='figlabel'>{self._fmt(caption_label)}</div>"
                f"{annots}"
            )
            return self._render(self._page(body), output_path)
        finally:
            if tmp_fig is not None:
                os.unlink(tmp_fig.name)

    def text_card(self, heading, paragraphs, output_path, heading_lines=None):
        """Pure-text card: a heading (single or multi-line) + body paragraphs."""
        if heading_lines:
            head_html = "<br>".join(self._fmt(line) for line in heading_lines)
        else:
            head_html = self._fmt(heading)
        paras = "".join(f"<div class='para'>{self._fmt(p)}</div>" for p in paragraphs)
        body = f"<div class='heading'>{head_html}</div>{paras}"
        return self._render(self._page(body), output_path)

    def tail_card(self, references, output_path, lead_paragraphs=None):
        """Tail card: optional closing commentary, a reference list, and a signature block."""
        body = ""
        if lead_paragraphs:
            body += "".join(f"<div class='lead'>{self._fmt(p)}</div>" for p in lead_paragraphs)
        body += "<div class='refs-heading'>参考文献</div>"
        for ref in references:
            if ref == "":
                body += "<div class='ref spacer'></div>"
            else:
                body += f"<div class='ref'>{self._fmt(ref)}</div>"
        body += (
            "<div class='sigblock'>"
            "<div class='sep sig-sep'></div>"
            f"<div class='signame'>{html.escape(self.signature)}</div>"
            "<div class='sigtag'>DailyBCI · 每日脑机接口学术速递</div>"
            "</div>"
        )
        return self._render(self._page(body), output_path)


# =============================================================================
# CLI — quick test
# =============================================================================

if __name__ == "__main__":
    _PROJECT_DIR = os.path.abspath(os.path.join(_SKILL_DIR, "..", "..", ".."))
    gen = CardGenerator(date="2026.06.07")
    outdir = os.path.join(_PROJECT_DIR, "output", "template-test")

    gen.cover_card(
        "血管内脑机接口",
        "走进 FDA 关键性试验",
        "Synchron 的 Stentrode 成为**首个**进入 FDA 关键性临床试验的血管内脑机接口¹。",
        os.path.join(outdir, "01-cover.png"),
        source="2026 · Synchron COMMAND 试验 · 血管内支架电极(16 通道,经颈静脉植入运动皮层附近),无需开颅。",
    )

    gen.text_card(
        "16 通道够用吗？",
        [
            "这是所有人看到 Stentrode 参数时的第一反应。Neuralink 的 N1 有 **1,024** 个通道，Stentrode 只有 **16** 个，差了将近两个数量级³。",
            "但 Synchron 的逻辑是：对于 ALS 患者最迫切的需求——用意念点击、发消息、控制智能家居——16 个通道捕获的运动皮层信号已经够用了⁴。",
        ],
        os.path.join(outdir, "02-text.png"),
    )

    gen.tail_card(
        [
            "¹ Synchron COMMAND Trial, FDA IDE approval, 2025",
            "",
            "² Oxley et al., J NeuroIntervent Surg, 2021",
            "",
            "³ Musk & Neuralink, J Med Internet Res, 2019",
        ],
        os.path.join(outdir, "03-tail.png"),
    )

    print(f"Test cards saved to {outdir}/")

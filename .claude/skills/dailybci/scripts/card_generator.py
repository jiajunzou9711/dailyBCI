"""
DailyBCI Card Generator
=======================
Reusable template for generating 小红书 card images.

Style: Academic minimal (Nature Briefing inspired)
Fonts: Lato (Latin) + STHeiti SC (CJK)
Attribution: 小邹 × Claude (小红书) / xiaozou × Claude (X thread)

Usage:
    from card_generator import CardGenerator
    gen = CardGenerator(date="2026.06.07")
    gen.cover_card("标题第一行", "标题第二行", "一句话核心发现。", "output/01-cover.png")
    gen.figure_card(figure_path, "Fig. 1", "评注文字...", "output/02-figure.png")
    gen.text_card("小标题", ["段落1...", "段落2..."], "output/03-text.png")
    gen.tail_card(["¹ Ref 1...", "² Ref 2..."], "output/05-tail.png")
"""

import os
from PIL import Image, ImageDraw, ImageFont

# =============================================================================
# Constants
# =============================================================================

W, H = 1080, 1440          # 小红书 standard portrait ratio
MARGIN = 100                # generous margins
BG_COLOR = '#FAFAFA'        # near-white background

# Color palette (grayscale hierarchy)
COLOR_TITLE = '#1A1A1A'     # darkest — titles
COLOR_BODY = '#444444'      # body text
COLOR_SUBTITLE = '#666666'  # subtitles / secondary text
COLOR_CAPTION = '#888888'   # figure captions, references
COLOR_MUTED = '#999999'     # tertiary text
COLOR_BRAND = '#BBBBBB'     # brand, date, signature
COLOR_LINE = '#E0E0E0'      # separator lines

# Font sizes
SIZE_TITLE_LG = 64
SIZE_TITLE_MD = 52
SIZE_SUBTITLE = 36
SIZE_BODY = 32
SIZE_ANNOTATION = 30
SIZE_CAPTION = 26
SIZE_SMALL = 24
SIZE_BRAND = 22

# Font resolution — cross-platform with fallbacks.
# scripts/ and fonts/ are siblings under .claude/skills/dailybci/, so the bundled
# CJK font resolves relative to this script regardless of cwd or OS.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_SKILL_DIR = os.path.dirname(_SCRIPT_DIR)          # .claude/skills/dailybci/
_BUNDLED_FONTS = os.path.join(_SKILL_DIR, "fonts")


def _first_existing(paths, default=None):
    for p in paths:
        if p and os.path.exists(p):
            return p
    return default


# Latin: try Lato (Linux), then common macOS/Windows sans, then PIL default.
LATIN_REG = _first_existing([
    "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",      # Linux (apt fonts-lato)
    "/Library/Fonts/Lato-Regular.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",         # macOS
    "/System/Library/Fonts/Helvetica.ttc",                  # macOS
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",      # Linux fallback
    "C:/Windows/Fonts/arial.ttf",                           # Windows
])
LATIN_BOLD = _first_existing([
    "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
    "/Library/Fonts/Lato-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
], default=LATIN_REG)

# CJK: prefer bundled STHeiti, else macOS system STHeiti/Hiragino/PingFang, else Noto.
CJK_PATH = _first_existing([
    os.path.join(_BUNDLED_FONTS, "STHeiti Medium.ttc"),     # bundled
    os.path.join(_BUNDLED_FONTS, "Hiragino Sans GB.ttc"),   # bundled alt
    "/System/Library/Fonts/STHeiti Medium.ttc",             # macOS system
    "/System/Library/Fonts/PingFang.ttc",                   # macOS system
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc",# Linux (apt fonts-noto-cjk)
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
])
CJK_IDX = 1  # index=1 = Heiti SC (simplified Chinese); PingFang/Noto: try 0 if glyphs look wrong

# Superscript fallback map: characters STHeiti doesn't support
SUPERSCRIPT_MAP = {
    '⁴': '4',   # ⁴
    '⁵': '5',   # ⁵
    '⁶': '6',   # ⁶
    '⁷': '7',   # ⁷
    '⁸': '8',   # ⁸
    '⁹': '9',   # ⁹
    '⁰': '0',   # ⁰
}

# =============================================================================
# Unicode detection
# =============================================================================

def is_cjk(char):
    """Return True if char should use the CJK font."""
    cp = ord(char)
    return (
        0x4E00 <= cp <= 0x9FFF or    # CJK Unified Ideographs
        0x2460 <= cp <= 0x24FF or    # Enclosed Alphanumerics (①②③… — in STHeiti, not Arial)
        0x3400 <= cp <= 0x4DBF or    # CJK Extension A
        0x2E80 <= cp <= 0x2EFF or    # CJK Radicals Supplement
        0x3000 <= cp <= 0x303F or    # CJK Symbols and Punctuation
        0xFF00 <= cp <= 0xFFEF or    # Fullwidth Forms
        0xF900 <= cp <= 0xFAFF or    # CJK Compatibility Ideographs
        0xFE30 <= cp <= 0xFE4F or    # CJK Compatibility Forms
        0x20000 <= cp <= 0x2A6DF or  # CJK Extension B
        0x3040 <= cp <= 0x309F or    # Hiragana
        0x30A0 <= cp <= 0x30FF or    # Katakana
        # Smart quotes and special punctuation — render with CJK font
        cp in (0x2018, 0x2019, 0x201C, 0x201D,  # ''""
               0x2014, 0x2013,                    # — –
               0x00B7,                             # ·
               0x00B9, 0x00B2, 0x00B3)             # ¹²³
    )

# =============================================================================
# CardGenerator class
# =============================================================================

class CardGenerator:
    """Generate DailyBCI 小红书 card images."""

    def __init__(self, date="", platform="xiaohongshu"):
        """
        Args:
            date: Display date string, e.g. "2026.06.07"
            platform: "xiaohongshu" or "x" — controls signature
        """
        self.date = date
        self.signature = "小邹 × Claude" if platform == "xiaohongshu" else "xiaozou × Claude"
        self._font_cache = {}

    def _get_font(self, size, bold=False, force_latin=False):
        """Get font with caching."""
        key = (size, bold, force_latin)
        if key not in self._font_cache:
            if force_latin:
                self._font_cache[key] = ImageFont.truetype(
                    LATIN_BOLD if bold else LATIN_REG, size
                )
            else:
                # Returns (latin, cjk) tuple
                latin = ImageFont.truetype(LATIN_BOLD if bold else LATIN_REG, size)
                cjk = ImageFont.truetype(CJK_PATH, size, index=CJK_IDX)
                self._font_cache[key] = (latin, cjk)
        return self._font_cache[key]

    def _pick_font(self, char, size, bold=False):
        """Pick the right font for a character."""
        latin, cjk = self._get_font(size, bold)
        return cjk if is_cjk(char) else latin

    def _handle_superscript(self, char):
        """Convert unsupported superscript chars to supported form."""
        return SUPERSCRIPT_MAP.get(char, char)

    # ---- Drawing primitives ----

    def draw_mixed(self, d, pos, text, size, fill, bold=False):
        """Draw mixed Latin+CJK text at a fixed position. Returns end x."""
        x, y = pos
        for char in text:
            char = self._handle_superscript(char)
            font = self._pick_font(char, size, bold)
            bbox = d.textbbox((0, 0), char, font=font)
            cw = bbox[2] - bbox[0]
            d.text((x, y), char, font=font, fill=fill)
            x += cw + 1
        return x

    def draw_mixed_wrap(self, d, x_start, y_start, text, size, fill,
                        max_width, line_spacing=1.6, bold=False):
        """Draw mixed text with automatic line wrapping. Returns y after last line."""
        x = x_start
        y = y_start
        line_h = int(size * line_spacing)

        for char in text:
            char = self._handle_superscript(char)
            if char == '\n':
                x = x_start
                y += line_h
                continue

            font = self._pick_font(char, size, bold)
            bbox = d.textbbox((0, 0), char, font=font)
            cw = bbox[2] - bbox[0]

            if x + cw > x_start + max_width:
                x = x_start
                y += line_h

            d.text((x, y), char, font=font, fill=fill)
            x += cw + 1

        return y + line_h

    # ---- Shared card elements ----

    def _new_card(self):
        """Create a blank card with standard background."""
        img = Image.new('RGB', (W, H), BG_COLOR)
        d = ImageDraw.Draw(img)
        return img, d

    def _draw_header(self, d):
        """Draw 'DailyBCI' brand in top-left."""
        font = self._get_font(SIZE_BRAND, force_latin=True)
        d.text((MARGIN, 70), "DailyBCI", font=font, fill=COLOR_BRAND)

    def _draw_footer(self, d):
        """Draw date (left) and signature (right) at bottom."""
        font_latin = self._get_font(SIZE_BRAND, force_latin=True)
        d.text((MARGIN, H - 100), self.date, font=font_latin, fill=COLOR_BRAND)

        # Right-align signature
        sig_chars = list(self.signature)
        latin, cjk = self._get_font(SIZE_BRAND)
        total_w = 0
        for char in sig_chars:
            font = cjk if is_cjk(char) else latin
            bbox = d.textbbox((0, 0), char, font=font)
            total_w += (bbox[2] - bbox[0]) + 1
        self.draw_mixed(d, (W - MARGIN - total_w, H - 100),
                        self.signature, SIZE_BRAND, COLOR_BRAND)

    def _draw_separator(self, d, y):
        """Draw a thin horizontal separator line."""
        d.line([(MARGIN, y), (W - MARGIN, y)], fill=COLOR_LINE, width=1)

    # ---- Card types ----

    def cover_card(self, title_line1, title_line2, subtitle, output_path, source=None):
        """
        Generate a cover card.
        Args:
            title_line1: First line of title (Chinese)
            title_line2: Second line of title (Chinese)
            subtitle: One-sentence core finding
            output_path: Where to save the PNG
            source: Provenance block — which paper is being explained: date,
                platform/journal, title, method, and (if notable) authors/institution.
                Rendered as a muted "解读" block under the subtitle. Strongly
                recommended on every cover (see SKILL.md Step 7 cover rule).
        """
        img, d = self._new_card()
        self._draw_header(d)

        y = 330
        self.draw_mixed(d, (MARGIN, y), title_line1, SIZE_TITLE_LG, COLOR_TITLE, bold=True)
        y += 92
        self.draw_mixed(d, (MARGIN, y), title_line2, SIZE_TITLE_LG, COLOR_TITLE, bold=True)
        y += 140
        y = self.draw_mixed_wrap(d, MARGIN, y, subtitle, SIZE_SUBTITLE - 2,
                                 COLOR_SUBTITLE, W - 2 * MARGIN)

        if source:
            y += 55
            self._draw_separator(d, y)
            y += 34
            self.draw_mixed(d, (MARGIN, y), "解读", SIZE_CAPTION, COLOR_MUTED, bold=True)
            y += 44
            self.draw_mixed_wrap(d, MARGIN, y, source, SIZE_CAPTION,
                                 COLOR_CAPTION, W - 2 * MARGIN, line_spacing=1.55)

        self._draw_footer(d)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, quality=95)
        return output_path

    def figure_card(self, figure_path_or_image, caption_label, annotation_paragraphs,
                    output_path, figure_height=560):
        """
        Generate a figure + annotation card.
        Args:
            figure_path_or_image: Path to figure PNG, or PIL Image object
            caption_label: e.g. "Fig. 1"
            annotation_paragraphs: List of annotation strings
            output_path: Where to save
            figure_height: Height to resize the figure to (width fills card)
        """
        img, d = self._new_card()
        self._draw_header(d)

        # Load and resize figure
        if isinstance(figure_path_or_image, str):
            fig = Image.open(figure_path_or_image)
        else:
            fig = figure_path_or_image

        # Scale to fit within (available width x figure_height) WITHOUT
        # distorting: figure_height acts as a max height, aspect ratio preserved.
        # Figures use a smaller side inset than text so cropped key-panels render
        # large ("图满铺"), with a thin frame for definition ("加框").
        FIG_INSET = 64
        fig_w_max = W - 2 * FIG_INSET
        fig_h_max = figure_height
        ow, oh = fig.size
        scale = min(fig_w_max / ow, fig_h_max / oh)
        new_w, new_h = max(1, int(round(ow * scale))), max(1, int(round(oh * scale)))
        fig = fig.resize((new_w, new_h), Image.LANCZOS)
        paste_x = FIG_INSET + (fig_w_max - new_w) // 2  # center horizontally
        paste_y = 140
        img.paste(fig, (paste_x, paste_y))
        # thin frame around the figure
        d.rectangle([paste_x - 1, paste_y - 1, paste_x + new_w, paste_y + new_h],
                    outline=COLOR_LINE, width=1)

        # Separator under figure
        sep_y = paste_y + new_h + 24
        self._draw_separator(d, sep_y)

        # Caption label
        y = sep_y + 25
        self.draw_mixed(d, (MARGIN, y), caption_label, SIZE_CAPTION,
                        COLOR_MUTED, bold=True)
        y += 40

        # Annotation paragraphs
        for para in annotation_paragraphs:
            y = self.draw_mixed_wrap(d, MARGIN, y, para, SIZE_ANNOTATION,
                                     COLOR_BODY, W - 2 * MARGIN, line_spacing=1.6)
            y += 20

        self._draw_footer(d)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, quality=95)
        return output_path

    def text_card(self, heading, paragraphs, output_path, heading_lines=None):
        """
        Generate a pure text card.
        Args:
            heading: Card heading (can be short, displayed large)
            paragraphs: List of paragraph strings
            output_path: Where to save
            heading_lines: If heading is multi-line, pass as list of strings
        """
        img, d = self._new_card()
        self._draw_header(d)

        y = 160
        if heading_lines:
            for line in heading_lines:
                self.draw_mixed(d, (MARGIN, y), line, SIZE_TITLE_MD,
                                COLOR_TITLE, bold=True)
                y += 75
        else:
            self.draw_mixed(d, (MARGIN, y), heading, SIZE_TITLE_MD,
                            COLOR_TITLE, bold=True)
            y += 75

        y += 25  # space between heading and body

        for para in paragraphs:
            y = self.draw_mixed_wrap(d, MARGIN, y, para, SIZE_BODY,
                                     COLOR_BODY, W - 2 * MARGIN, line_spacing=1.65)
            y += 20

        self._draw_footer(d)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, quality=95)
        return output_path

    def tail_card(self, references, output_path):
        """
        Generate a tail card with references and prominent signature.
        Args:
            references: List of reference strings (each prefixed with ¹, ², etc.)
            output_path: Where to save
        """
        img, d = self._new_card()
        self._draw_header(d)

        y = 180
        self.draw_mixed(d, (MARGIN, y), "参考文献", SIZE_SUBTITLE,
                        COLOR_TITLE, bold=True)
        y += 70

        for ref in references:
            if ref == "":
                y += 12
                continue
            self.draw_mixed(d, (MARGIN, y), ref, SIZE_SMALL, COLOR_CAPTION)
            y += 36

        # Signature block
        sig_y = H - 220
        self._draw_separator(d, sig_y)
        sig_y += 40
        self.draw_mixed(d, (MARGIN, sig_y), self.signature, SIZE_BODY,
                        COLOR_BODY, bold=True)
        sig_y += 50
        self.draw_mixed(d, (MARGIN, sig_y), "DailyBCI · 每日脑机接口学术速递",
                        SIZE_SMALL, COLOR_MUTED)

        self._draw_footer(d)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, quality=95)
        return output_path


# =============================================================================
# CLI — quick test
# =============================================================================

if __name__ == "__main__":
    gen = CardGenerator(date="2026.06.07")
    outdir = os.path.join(_PROJECT_DIR, "output", "template-test")

    gen.cover_card(
        "血管内脑机接口",
        "走进 FDA 关键性试验",
        "Synchron 的 Stentrode 成为首个进入 FDA 关键性临床试验的血管内脑机接口。",
        os.path.join(outdir, "01-cover.png")
    )

    gen.text_card(
        "16 通道够用吗？",
        [
            "这是所有人看到 Stentrode 参数时的第一反应。Neuralink 的 N1 有 1,024 个通道，Stentrode 只有 16 个，差了将近两个数量级\xb3。",
            "但 Synchron 的逻辑是：对于 ALS 患者最迫切的需求——用意念点击、发消息、控制智能家居——16 个通道捕获的运动皮层信号已经够用了⁴。",
        ],
        os.path.join(outdir, "02-text.png")
    )

    gen.tail_card(
        [
            "\xb9 Synchron COMMAND Trial, FDA IDE approval, 2025",
            "",
            "\xb2 Oxley et al., J NeuroIntervent Surg, 2021",
            "",
            "\xb3 Musk & Neuralink, J Med Internet Res, 2019",
        ],
        os.path.join(outdir, "03-tail.png")
    )

    print(f"Test cards saved to {outdir}/")

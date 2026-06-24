"""figcrop.py — robust, fast figure cropping for DailyBCI 图卡 (added 2026-06-24).

Why this exists: hand-typing crop coordinates is slow and clips content (panel
letters, legends, colorbars get cut; neighbour panels bleed in). Let the image
report its own boundaries instead.

Pipeline (per figure):
  1. Render the PDF page to a hi-DPI PNG:  fitz page.get_pixmap(dpi=300).
  2. figure_box(): tight bounding box of all non-white content within a generous
     y-band, AFTER clipping the page side-margins (kills the bioRxiv side
     watermark) and cutting above the prose 'Figure N.' caption. Captures panel
     letters, legends, colorbars, axis labels, and dark 2P images alike — because
     anything that isn't page-white (gray < ink_thr) counts as content.
  3. split_panels(): if the figure is a wide multi-panel row you want to re-tile
     (see SKILL Step 8 黄金标准 ②(c)), split it at white gutters, each panel
     expanded to the gutter MIDPOINTS so nothing is clipped.

Thresholds tuned for bioRxiv 300-dpi renders: white page ≈ 255, ink < 235,
gutter brightness > ~248. 2P dark-background panels are dark (<235) so they
count as content and are framed fully.

Usage:
    import fitz, numpy as np
    from PIL import Image
    import sys; sys.path.insert(0, ".claude/skills/dailybci/scripts")
    import figcrop
    doc = fitz.open("papers/<slug>.pdf")
    doc[PAGE].get_pixmap(dpi=300).save("papers/hi_p.png")
    g = np.asarray(Image.open("papers/hi_p.png").convert("L"))
    box = figcrop.figure_box(g, y_band=(Y0, Y1))   # Y0/Y1 from the caption line in fulltext
    Image.open("papers/hi_p.png").crop(box).save("papers/fig.png")  # then Read to self-check
    # to re-tile a wide row:
    for (px0, px1) in figcrop.split_panels(g, box):
        ...  # crop (px0, box[1], px1, box[3]) and paste onto a near-square canvas
"""
import numpy as np


def content_bbox(gray, ink_thr=235, min_ink=2):
    """Tight (x0,y0,x1,y1) of all content (gray < ink_thr). min_ink = min dark
    pixels for a row/col to count (drops 1-px specks)."""
    ink = gray < ink_thr
    rows = ink.sum(1); cols = ink.sum(0)
    ys = np.where(rows >= min_ink)[0]; xs = np.where(cols >= min_ink)[0]
    if len(xs) == 0 or len(ys) == 0:
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


def _gutters(prof, white_thr, min_run):
    white = prof > white_thr; runs = []; s = None
    for i, w in enumerate(white):
        if w and s is None:
            s = i
        if (not w) and s is not None:
            if i - s >= min_run:
                runs.append((s, i))
            s = None
    if s is not None and len(white) - s >= min_run:
        runs.append((s, len(white)))
    return runs


def row_gutters(gray, white_thr=250, min_run=16):
    return _gutters(gray.mean(1), white_thr, min_run)


def col_gutters(gray, white_thr=248, min_run=14):
    return _gutters(gray.mean(0), white_thr, min_run)


def figure_box(gray, xclip=None, y_band=None, caption_min_offset=260):
    """Tight (x0,y0,x1,y1) of ONE figure, excluding page side-margins (watermark)
    and the prose caption beneath the panels.

    xclip=(XL,XR)  drop left/right page margins (default ~6% / 97% of width).
    y_band=(Y0,Y1) generous vertical window around the figure (read the
                   'Figure N.' line offset from the extracted fulltext).
    caption_min_offset  the panel block must be at least this many px tall before
                   a white horizontal gutter is treated as the panel/caption
                   divider (so an inter-panel gutter isn't mistaken for it)."""
    H, W = gray.shape
    XL, XR = xclip or (int(W * 0.06), int(W * 0.97))
    Y0, Y1 = y_band or (0, H)
    col = gray[Y0:Y1, XL:XR]
    bottom = Y1 - Y0
    for a, b in row_gutters(col, white_thr=250, min_run=18):
        if a > caption_min_offset:
            bottom = a
            break
    bb = content_bbox(gray[Y0:Y0 + bottom, XL:XR])
    if bb is None:
        return None
    x0, y0, x1, y1 = bb
    return (XL + x0, Y0 + y0, XL + x1, Y0 + y1)


def split_panels(gray, box, white_thr=243, min_run=20, pad=2):
    """Split a figure box horizontally at white gutters; each panel expanded to
    adjacent gutter midpoints so nothing is clipped. Returns [(x0,x1), ...] in
    page-x; crop each with box's y-range (box[1], box[3])."""
    x0, y0, x1, y1 = box
    runs = col_gutters(gray[y0:y1, x0:x1], white_thr=white_thr, min_run=min_run)
    centers = [(a + b) // 2 for a, b in runs]
    bounds = [0] + centers + [x1 - x0]
    return [(x0 + max(0, bounds[i] + pad), x0 + bounds[i + 1])
            for i in range(len(bounds) - 1)]

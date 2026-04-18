# /// script
# requires-python = ">=3.11"
# dependencies = ["fonttools>=4.50"]
# ///
"""
Generates print-ready business-card artwork under brand/print/.

Usage:
  uv run scripts/build-cards.py

Outputs:
  brand/print/business-card-helen-front.svg   — Helen Nash's front
  brand/print/business-card-back.svg          — symbol-only back (shared across cards)
  brand/print/business-card-template-front.svg — blank front for future hires
  brand/print/exports/business-card-helen-front.pdf
  brand/print/exports/business-card-back.pdf
  brand/print/exports/business-card-template-front.pdf
  brand/print/exports/business-card-helen-front.png  — low-fi preview
  brand/print/exports/business-card-back.png
  brand/print/exports/business-card-template-front.png

Spec
  Trim: 85×55mm (UK standard). Bleed: 3mm every side → PDF canvas 91×61mm.
  Crop marks rendered on every PDF.
  RGB colour space (Moo accepts; Ghostscript isn't available to produce CMYK locally).
  Text outlined to paths from Inter so the PDF is self-contained.
"""
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "brand" / "logo" / "fonts"
OUT = ROOT / "brand" / "print"
EXPORTS = OUT / "exports"

PRIMARY = "#8B3A2A"
WARM_BG = "#FDFBF7"
MUTED = "#6B6560"

# Dimensions in millimetres. SVG viewBox uses mm as user units; width="{...}mm" on
# the root makes the file physically print-accurate.
TRIM_W, TRIM_H = 85, 55
BLEED = 3
CARD_W, CARD_H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED  # 91 × 61

BARS = [
    (5, 10, 60, 10),
    (20, 24, 75, 10),
    (0, 38, 45, 10),
    (15, 52, 80, 10),
    (30, 66, 35, 10),
    (10, 80, 65, 10),
]

HELEN = {
    "name": "Helen Nash",
    "gdc": "GDC #176698",
    "email": "h.nash1@async-digital.com",
    "phone": "07397 516692",
}

TEMPLATE = {
    "name": "[Full name]",
    "gdc": "GDC #[number]",
    "email": "[email]",
    "phone": "[phone]",
}


@dataclass
class GlyphRun:
    paths: list[str]
    advance_mm: float  # scaled to card units (mm)


def build_run(font: TTFont, text: str, size_mm: float) -> GlyphRun:
    """Outline text at a physical cap-height in mm; advance returned in mm too."""
    cmap = font.getBestCmap()
    glyphs = font.getGlyphSet()
    hmtx = font["hmtx"]
    cap = font["OS/2"].sCapHeight or font["hhea"].ascender
    scale = size_mm / cap
    space_advance = (font["head"].unitsPerEm * 0.25) * scale

    x = 0.0
    paths: list[str] = []
    for ch in text:
        if ch == " ":
            x += space_advance
            continue
        name = cmap.get(ord(ch))
        if not name:
            continue
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        d = pen.getCommands()
        if d:
            paths.append(
                f'<path transform="translate({x:.3f},0) scale({scale:.6f},-{scale:.6f})" d="{d}"/>'
            )
        x += hmtx[name][0] * scale
    return GlyphRun(paths=paths, advance_mm=x)


def crop_marks() -> str:
    """Four L-shaped corner marks, 3mm long, 1mm clear of the trim edge."""
    marks = []
    m_len = 3
    gap = 1
    stroke = 0.2
    # Top-left
    marks += [
        f'<line x1="0" y1="-{gap}" x2="0" y2="-{gap + m_len}" stroke="#000" stroke-width="{stroke}"/>',
        f'<line x1="-{gap}" y1="0" x2="-{gap + m_len}" y2="0" stroke="#000" stroke-width="{stroke}"/>',
    ]
    # Top-right
    marks += [
        f'<line x1="{TRIM_W}" y1="-{gap}" x2="{TRIM_W}" y2="-{gap + m_len}" stroke="#000" stroke-width="{stroke}"/>',
        f'<line x1="{TRIM_W + gap}" y1="0" x2="{TRIM_W + gap + m_len}" y2="0" stroke="#000" stroke-width="{stroke}"/>',
    ]
    # Bottom-left
    marks += [
        f'<line x1="0" y1="{TRIM_H + gap}" x2="0" y2="{TRIM_H + gap + m_len}" stroke="#000" stroke-width="{stroke}"/>',
        f'<line x1="-{gap}" y1="{TRIM_H}" x2="-{gap + m_len}" y2="{TRIM_H}" stroke="#000" stroke-width="{stroke}"/>',
    ]
    # Bottom-right
    marks += [
        f'<line x1="{TRIM_W}" y1="{TRIM_H + gap}" x2="{TRIM_W}" y2="{TRIM_H + gap + m_len}" stroke="#000" stroke-width="{stroke}"/>',
        f'<line x1="{TRIM_W + gap}" y1="{TRIM_H}" x2="{TRIM_W + gap + m_len}" y2="{TRIM_H}" stroke="#000" stroke-width="{stroke}"/>',
    ]
    return "\n  ".join(marks)


def card_wrapper(inner: str) -> str:
    """Wrap inner artwork in the bleed-area viewBox with warm-bg bleed + crop marks.

    viewBox origin sits at the trim's top-left corner, so inner geometry is
    expressed in mm from (0,0) to (85,55). The bleed extends from (-3,-3) to
    (88,58).
    """
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{CARD_W}mm" height="{CARD_H}mm" '
        f'viewBox="{-BLEED} {-BLEED} {CARD_W} {CARD_H}">\n'
        # Full bleed bg so the trim can shift ±0.3mm without showing white.
        f'  <rect x="{-BLEED}" y="{-BLEED}" width="{CARD_W}" height="{CARD_H}" fill="{WARM_BG}"/>\n'
        f'{inner}\n'
        f'  {crop_marks()}\n'
        f'</svg>\n'
    )


def front_svg(font: TTFont, person: dict) -> str:
    """Left-aligned front: name big, then GDC / email / phone in Inter Regular,
    with a small symbol mark tagged in the top-right corner."""
    # Cap sizes in mm
    name_cap = 4.5
    meta_cap = 2.5
    leading_meta = 1.8  # gap between meta lines

    regular = TTFont(FONT_DIR / "Inter-Regular.ttf")
    bold = font  # passed-in

    name_run = build_run(bold, person["name"], name_cap)
    gdc_run = build_run(regular, person["gdc"], meta_cap)
    email_run = build_run(regular, person["email"], meta_cap)
    phone_run = build_run(regular, person["phone"], meta_cap)

    # Layout: left margin 6mm (safe 3mm + 3mm breathing)
    left = 6
    baseline_name = 18  # mm from top — above vertical centre
    # Stack of meta lines starts 9mm below name baseline
    baseline_gdc = baseline_name + 9
    baseline_email = baseline_gdc + (meta_cap + leading_meta)
    baseline_phone = baseline_email + (meta_cap + leading_meta)

    def render(run: GlyphRun, baseline: float) -> str:
        return (
            f'<g transform="translate({left},{baseline})" fill="{PRIMARY}">'
            f'{"".join(run.paths)}</g>'
        )

    # Top-right symbol tag — small mark so the brand is visible on the contact side,
    # not just the flip side. Right-aligned at the same 6mm safe margin.
    mark_w = 12
    mark_x = TRIM_W - 6 - mark_w
    mark_y = 6
    mark_scale = mark_w / 100
    mark_rects = "\n    ".join(
        f'<rect x="{x * mark_scale + mark_x:.3f}" y="{y * mark_scale + mark_y:.3f}" '
        f'width="{w * mark_scale:.3f}" height="{h * mark_scale:.3f}" '
        f'rx="{(h * mark_scale) / 2:.3f}"/>'
        for (x, y, w, h) in BARS
    )

    inner = (
        f'  {render(name_run, baseline_name)}\n'
        f'  {render(gdc_run, baseline_gdc)}\n'
        f'  {render(email_run, baseline_email)}\n'
        f'  {render(phone_run, baseline_phone)}\n'
        f'  <g fill="{PRIMARY}">\n    {mark_rects}\n  </g>'
    )
    return card_wrapper(inner)


def back_svg() -> str:
    """Back: symbol centred, filling ~28mm square within the card."""
    mark_w = 28
    cx = TRIM_W / 2
    cy = TRIM_H / 2
    scale = mark_w / 100  # BARS are authored in a 100-unit box
    x0 = cx - mark_w / 2
    y0 = cy - mark_w / 2
    rects = "\n    ".join(
        f'<rect x="{x * scale + x0:.3f}" y="{y * scale + y0:.3f}" '
        f'width="{w * scale:.3f}" height="{h * scale:.3f}" '
        f'rx="{(h * scale) / 2:.3f}"/>'
        for (x, y, w, h) in BARS
    )
    inner = f'  <g fill="{PRIMARY}">\n    {rects}\n  </g>'
    return card_wrapper(inner)


def render_pdf(svg_path: Path, pdf_path: Path) -> None:
    subprocess.run(
        ["rsvg-convert", "-f", "pdf", str(svg_path), "-o", str(pdf_path)],
        check=True,
    )
    print(f"wrote {pdf_path.relative_to(ROOT)}")


def render_png(svg_path: Path, png_path: Path, dpi: int = 300) -> None:
    # CARD_W mm at 300 dpi
    px_w = int(round(CARD_W * dpi / 25.4))
    subprocess.run(
        ["rsvg-convert", "-w", str(px_w), str(svg_path), "-o", str(png_path)],
        check=True,
    )
    print(f"wrote {png_path.relative_to(ROOT)}")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def main() -> None:
    bold = TTFont(FONT_DIR / "Inter-Bold.ttf")

    svgs = {
        "business-card-helen-front": front_svg(bold, HELEN),
        "business-card-template-front": front_svg(bold, TEMPLATE),
        "business-card-back": back_svg(),
    }
    for name, svg in svgs.items():
        write(OUT / f"{name}.svg", svg)

    EXPORTS.mkdir(parents=True, exist_ok=True)
    for name in svgs:
        src = OUT / f"{name}.svg"
        render_pdf(src, EXPORTS / f"{name}.pdf")
        render_png(src, EXPORTS / f"{name}.png")


if __name__ == "__main__":
    main()

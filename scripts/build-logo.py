# /// script
# requires-python = ">=3.11"
# dependencies = ["fonttools>=4.50", "pillow>=10.0"]
# ///
"""
Generates the full brand/logo/ set from scratch.

Usage:
  uv run scripts/build-logo.py

Outputs:
  brand/logo/{symbol,horizontal,stacked,wordmark,favicon-mark,clear-space}.svg
  brand/logo/{symbol,horizontal,stacked}-mono-{black,white}.svg
  brand/logo/exports/{symbol,horizontal,stacked}-{1x,2x,3x}.png
  brand/logo/exports/{symbol,horizontal,stacked}.pdf
  brand/logo/exports/favicon-{16,32,48}.png
  brand/logo/exports/favicon.ico
  brand/logo/exports/apple-touch-icon.png

Colour-neutral SVGs use `color="#8B3A2A"` (brick `--primary`) seeded via
`currentColor`, so any parent CSS `color:` override themes them without editing
the file. Mono variants hardcode `#000000` or `#FFFFFF` for print / dark-surface use.
"""
from __future__ import annotations

import io
import subprocess
from dataclasses import dataclass
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FONT_PATH = ROOT / "brand" / "logo" / "fonts" / "Inter-Bold.ttf"
OUT = ROOT / "brand" / "logo"
EXPORTS = OUT / "exports"
ASSETS = ROOT / "assets"

PRIMARY = "#8B3A2A"
WARM_BG = "#FDFBF7"
OG_WIDTH, OG_HEIGHT = 1200, 630

# Six-bar async-threads mark, coordinates in a 100x100 viewBox.
BARS = [
    (5, 10, 60, 10),
    (20, 24, 75, 10),
    (0, 38, 45, 10),
    (15, 52, 80, 10),
    (30, 66, 35, 10),
    (10, 80, 65, 10),
]

# Simplified favicon mark — three bars at wider proportions for legibility at 16-32px.
FAVICON_BARS = [
    (10, 15, 65, 18),
    (25, 41, 70, 18),
    (0, 67, 50, 18),
]


@dataclass
class GlyphRun:
    paths: list[str]
    advance: int


def build_run(font: TTFont, text: str) -> GlyphRun:
    """Convert a string into a list of SVGPathPen commands with translate() offsets."""
    cmap = font.getBestCmap()
    glyphs = font.getGlyphSet()
    hmtx = font["hmtx"]
    upem = font["head"].unitsPerEm
    space_advance = upem * 0.25

    x = 0.0
    paths: list[str] = []
    for ch in text:
        if ch == " ":
            x += space_advance
            continue
        glyph_name = cmap[ord(ch)]
        pen = SVGPathPen(glyphs)
        glyphs[glyph_name].draw(pen)
        d = pen.getCommands()
        if d:
            paths.append(f'<path transform="translate({x:.2f},0)" d="{d}"/>')
        x += hmtx[glyph_name][0]
    return GlyphRun(paths=paths, advance=int(round(x)))


def wrap_wordmark(run: GlyphRun, font: TTFont) -> tuple[str, int, int]:
    """Wrap a glyph run as a standalone SVG sized to the cap-box."""
    ascender = font["OS/2"].sCapHeight or font["hhea"].ascender
    descender = font["hhea"].descender
    width = run.advance
    height = ascender - descender
    # Glyph coordinates are Y-up; flip by scaling y by -1 with the baseline at y=ascender.
    flipped = f'<g transform="matrix(1 0 0 -1 0 {ascender})" fill="currentColor">{"".join(run.paths)}</g>'
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'color="{PRIMARY}" role="img" aria-label="Async Digital">{flipped}</svg>'
    )
    return svg, width, height


def bars_svg(viewbox: str, bars: list[tuple[int, int, int, int]]) -> str:
    rects = "\n  ".join(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}"/>'
        for (x, y, w, h) in bars
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" '
        f'color="{PRIMARY}" role="img" aria-label="Async Digital">\n'
        f'  <g fill="currentColor">\n  {rects}\n  </g>\n</svg>\n'
    )


def symbol_svg() -> str:
    return bars_svg("0 0 100 100", BARS)


def favicon_mark_svg() -> str:
    return bars_svg("0 0 100 100", FAVICON_BARS)


def horizontal_svg(font: TTFont) -> str:
    """Mark on the left, two-line wordmark ('Async' over 'Digital') on the right.

    The two-line wordmark gives the lockup a ~square text block that balances the
    square mark, matching the shape of the current Logo.jpg.
    """
    upem_ascender = font["OS/2"].sCapHeight or font["hhea"].ascender
    upem_descender = font["hhea"].descender
    font_height = upem_ascender - upem_descender

    run_async = build_run(font, "Async")
    run_digital = build_run(font, "Digital")
    widest_advance = max(run_async.advance, run_digital.advance)

    # Target layout: mark is 100 wide in logical units; render wordmark scaled so two
    # lines together roughly match the mark's 100-unit height.
    # Two lines at cap height ~42 with 16 leading → total ~100.
    target_line_cap = 42
    scale = target_line_cap / (font["OS/2"].sCapHeight or 1)
    line_h = 50  # baseline-to-baseline in lockup units

    wordmark_width = widest_advance * scale
    gap = 24

    total_width = 100 + gap + wordmark_width
    vb_h = 100

    # Baseline of first line sits so the cap-box is centred in the top half.
    baseline_y1 = 10 + target_line_cap  # y of baseline line 1
    baseline_y2 = baseline_y1 + line_h

    def flipped(run: GlyphRun, baseline_y: float) -> str:
        paths = "".join(run.paths)
        return (
            f'<g transform="translate({100 + gap},{baseline_y}) scale({scale},-{scale})" '
            f'fill="currentColor">{paths}</g>'
        )

    bars_rects = "\n  ".join(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}"/>'
        for (x, y, w, h) in BARS
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width:.2f} {vb_h}" '
        f'color="{PRIMARY}" role="img" aria-label="Async Digital">\n'
        f'  <g fill="currentColor">\n  {bars_rects}\n  </g>\n'
        f'  {flipped(run_async, baseline_y1)}\n'
        f'  {flipped(run_digital, baseline_y2)}\n'
        f'</svg>\n'
    )


def stacked_svg(font: TTFont) -> str:
    """Mark on top, single-line 'Async Digital' below, both horizontally centred."""
    run = build_run(font, "Async Digital")
    target_cap = 26  # smaller cap so wordmark fits under square mark
    scale = target_cap / (font["OS/2"].sCapHeight or 1)
    wordmark_w = run.advance * scale
    gap = 18
    mark_w = 100
    vb_w = max(mark_w, wordmark_w)
    mark_x = (vb_w - mark_w) / 2
    wordmark_x = (vb_w - wordmark_w) / 2
    baseline_y = 100 + gap + target_cap
    vb_h = baseline_y + 4  # a hair of descender space

    bars_rects = "\n  ".join(
        f'<rect x="{x + mark_x:.2f}" y="{y}" width="{w}" height="{h}" rx="{h / 2}"/>'
        for (x, y, w, h) in BARS
    )
    wordmark = (
        f'<g transform="translate({wordmark_x:.2f},{baseline_y}) scale({scale:.4f},-{scale:.4f})" '
        f'fill="currentColor">{"".join(run.paths)}</g>'
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.2f} {vb_h:.2f}" '
        f'color="{PRIMARY}" role="img" aria-label="Async Digital">\n'
        f'  <g fill="currentColor">\n  {bars_rects}\n  </g>\n'
        f'  {wordmark}\n'
        f'</svg>\n'
    )


def clear_space_svg() -> str:
    """Diagram showing the minimum clear-space rule: one bar-height of padding on each side."""
    # Render the symbol in a 140x140 field, with clear-space indicated by dashed outline.
    # Clear-space = one bar height (10 logical units) in mark coordinates = 10% of mark width.
    pad = 15  # clear-space padding in viewBox units (content width = 100)
    vb = 100 + 2 * pad
    bars_rects = "\n  ".join(
        f'<rect x="{x + pad}" y="{y + pad}" width="{w}" height="{h}" rx="{h / 2}"/>'
        for (x, y, w, h) in BARS
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb} {vb}" '
        f'color="{PRIMARY}" role="img" aria-label="Clear-space diagram">\n'
        f'  <rect x="0.5" y="0.5" width="{vb - 1}" height="{vb - 1}" fill="none" '
        f'stroke="#6B6560" stroke-dasharray="4 4" stroke-width="1"/>\n'
        f'  <rect x="{pad}" y="{pad}" width="100" height="100" fill="none" '
        f'stroke="#6B6560" stroke-dasharray="2 2" stroke-width="0.5"/>\n'
        f'  <g fill="currentColor">\n  {bars_rects}\n  </g>\n'
        f'</svg>\n'
    )


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def recolour(svg: str, new_hex: str) -> str:
    return svg.replace(f'color="{PRIMARY}"', f'color="{new_hex}"')


def rsvg_png(svg_path: Path, out_path: Path, width: int) -> None:
    subprocess.run(
        ["rsvg-convert", "-w", str(width), str(svg_path), "-o", str(out_path)],
        check=True,
    )
    print(f"wrote {out_path.relative_to(ROOT)}")


def rsvg_pdf(svg_path: Path, out_path: Path) -> None:
    subprocess.run(
        ["rsvg-convert", "-f", "pdf", str(svg_path), "-o", str(out_path)],
        check=True,
    )
    print(f"wrote {out_path.relative_to(ROOT)}")


def render_bar_canvas(svg_path: Path, size: int, bg: str | None) -> Image.Image:
    """Render an SVG to a square PNG of `size`px, optionally with a background colour."""
    raw = subprocess.check_output(
        ["rsvg-convert", "-w", str(size), "-h", str(size), str(svg_path)]
    )
    icon = Image.open(io.BytesIO(raw)).convert("RGBA")
    if bg is None:
        return icon
    canvas = Image.new("RGBA", (size, size), bg)
    canvas.alpha_composite(icon)
    return canvas.convert("RGBA")


def build_favicon_ico(source_svg: Path, out_path: Path) -> None:
    sizes = [16, 32, 48, 64]
    images = [render_bar_canvas(source_svg, s, None) for s in sizes]
    images[0].save(out_path, format="ICO", sizes=[(s, s) for s in sizes])
    print(f"wrote {out_path.relative_to(ROOT)}")


def main() -> None:
    EXPORTS.mkdir(parents=True, exist_ok=True)
    font = TTFont(FONT_PATH)

    run_wordmark, _, _ = wrap_wordmark(build_run(font, "Async Digital"), font)

    svgs: dict[str, str] = {
        "symbol": symbol_svg(),
        "horizontal": horizontal_svg(font),
        "stacked": stacked_svg(font),
        "wordmark": run_wordmark + "\n",
        "favicon-mark": favicon_mark_svg(),
        "clear-space": clear_space_svg(),
    }
    for name, svg in svgs.items():
        write(OUT / f"{name}.svg", svg)

    # Monochrome variants — black on transparent and white on transparent for the
    # three main lockups. The wordmark, favicon-mark, and clear-space diagram only
    # ship in primary form; downstream templates recolour them via currentColor.
    for name in ("symbol", "horizontal", "stacked"):
        write(OUT / f"{name}-mono-black.svg", recolour(svgs[name], "#000000"))
        write(OUT / f"{name}-mono-white.svg", recolour(svgs[name], "#FFFFFF"))

    # Raster + PDF exports for the three lockups.
    sizes_px = {"1x": 512, "2x": 1024, "3x": 1536}
    for name in ("symbol", "horizontal", "stacked"):
        src = OUT / f"{name}.svg"
        for suffix, width in sizes_px.items():
            rsvg_png(src, EXPORTS / f"{name}-{suffix}.png", width)
        rsvg_pdf(src, EXPORTS / f"{name}.pdf")

    # Favicons — use the simplified three-bar mark so the shape holds up at 16-48px.
    fav_src = OUT / "favicon-mark.svg"
    for sz in (16, 32, 48):
        rsvg_png(fav_src, EXPORTS / f"favicon-{sz}.png", sz)
    build_favicon_ico(fav_src, EXPORTS / "favicon.ico")

    # apple-touch-icon: iOS home-screen icon, 180x180, opaque warm-bg behind the mark
    # so it reads consistently under iOS's auto rounded-corner mask.
    apple = render_bar_canvas(fav_src, 180, WARM_BG)
    apple.save(EXPORTS / "apple-touch-icon.png", format="PNG")
    print(f"wrote {(EXPORTS / 'apple-touch-icon.png').relative_to(ROOT)}")

    # Site-facing assets/ — the /assets/ URL paths the live site serves. Regenerated
    # from the canonical brand/logo/ outputs so the two folders never drift.
    ASSETS.mkdir(parents=True, exist_ok=True)

    # Primary logo shown in the site header and four-blocker.
    (ASSETS / "logo.svg").write_text((OUT / "horizontal.svg").read_text(), encoding="utf-8")
    print(f"wrote {(ASSETS / 'logo.svg').relative_to(ROOT)}")

    # Favicons — renamed to the pattern already referenced by index.html / four-blocker/index.html.
    for src_name, dst_name in (
        ("favicon-16.png", "favicon-16x16.png"),
        ("favicon-32.png", "favicon-32x32.png"),
        ("apple-touch-icon.png", "apple-touch-icon.png"),
    ):
        (ASSETS / dst_name).write_bytes((EXPORTS / src_name).read_bytes())
        print(f"wrote {(ASSETS / dst_name).relative_to(ROOT)}")

    # OG / Twitter card image: 1200x630, horizontal lockup centred on warm bg.
    horizontal_raw = subprocess.check_output(
        ["rsvg-convert", "-w", "800", str(OUT / "horizontal.svg")]
    )
    lockup = Image.open(io.BytesIO(horizontal_raw)).convert("RGBA")
    og = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), WARM_BG)
    paste_x = (OG_WIDTH - lockup.width) // 2
    paste_y = (OG_HEIGHT - lockup.height) // 2
    og.alpha_composite(lockup, dest=(paste_x, paste_y))
    og.convert("RGB").save(ASSETS / "og-logo.jpg", format="JPEG", quality=90)
    print(f"wrote {(ASSETS / 'og-logo.jpg').relative_to(ROOT)}")


if __name__ == "__main__":
    main()

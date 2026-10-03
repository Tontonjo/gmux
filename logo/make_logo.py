# mumux logo generator - v2.0.0
# Builds the icon and the horizontal logo (icon + "mumux" wordmark) as SVG and PNG.
# The wordmark is converted to paths so it renders without any font installed.
# Requirements: pip install fonttools cairosvg, and the DejaVu fonts (fonts-dejavu-core).
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import cairosvg

YELLOW = "#F5C400"   # same yellow as the mumux active window / pane highlight
BG = "#16181D"
PANE = "#22262E"
BORDER = "#3A404C"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
NAME = "mumux"

# Mouse pointer (tip at 0,0), drawn in the large pane: mumux is driven by the mouse
POINTER = "M0 0 L0 112 L28 85 L48 128 L70 118 L50 76 L88 76 Z"


def icon_group():
    """Terminal tile: a large pane with a clicking mouse pointer, two stacked
    panes (top one active, yellow border) and the status bar."""
    return f"""
  <rect width="512" height="512" rx="112" fill="{BG}"/>
  <rect x="78" y="78" width="210" height="304" rx="22" fill="{PANE}" stroke="{BORDER}" stroke-width="12"/>
  <rect x="318" y="78" width="116" height="138" rx="22" fill="{PANE}" stroke="{YELLOW}" stroke-width="12"/>
  <rect x="318" y="244" width="116" height="138" rx="22" fill="{PANE}" stroke="{BORDER}" stroke-width="12"/>
  <g fill="none" stroke="{YELLOW}" stroke-width="12" stroke-linecap="round">
    <path d="M128 146 L114 132"/>
    <path d="M150 136 L150 116"/>
    <path d="M118 168 L98 168"/>
  </g>
  <path d="{POINTER}" transform="translate(150 166) scale(1.25)" fill="{YELLOW}"
        stroke="{BG}" stroke-width="7" stroke-linejoin="round"/>
  <rect x="72" y="410" width="368" height="30" rx="15" fill="#2B303A"/>
  <rect x="72" y="410" width="132" height="30" rx="15" fill="{YELLOW}"/>"""


def text_path(text, size, x, y):
    """Return an SVG path for `text` set in DejaVu Sans Mono Bold, baseline at (x, y)."""
    font = TTFont(FONT)
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    pen = SVGPathPen(glyphs)
    cursor = 0
    for ch in text:
        name = cmap[ord(ch)]
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x + cursor, y)))
        cursor += glyphs[name].width * scale
    return pen.getCommands(), cursor


def write(name, svg):
    with open(name, "w") as f:
        f.write(svg)
    cairosvg.svg2png(url=name, write_to=name.replace(".svg", ".png"), output_width=1024)


# Icon (square)
write(f"{NAME}-icon.svg",
      f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">{icon_group()}\n</svg>\n')

# Horizontal logo: icon scaled to 160 px + wordmark, for light and dark backgrounds
d, width = text_path(NAME, 118, 196, 108)
total = int(196 + width + 8)
for suffix, color in (("light", "#16181D"), ("dark", "#F2F3F5")):
    write(f"{NAME}-logo-{suffix}.svg",
          f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total} 160">\n'
          f'  <g transform="scale(0.3125)">{icon_group()}\n  </g>\n'
          f'  <path d="{d}" fill="{color}"/>\n</svg>\n')

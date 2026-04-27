"""Generate the site-level fallback Open Graph image (1200x630).

Run from the project root: python tools/generate_og_image.py

Produces static/images/og-default.png. Update if branding changes; the file
is referenced by config/_default/params.toml `defaultSocialImage`.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ICON_PATH = ROOT / "static" / "images" / "1024x1024bb.png"
OUT_PATH = ROOT / "static" / "images" / "og-default.png"

W, H = 1200, 630
BG = (28, 25, 23)            # stone-900 — matches theme-color dark
TITLE_COLOR = (250, 250, 249)
TAGLINE_COLOR = (214, 211, 209)
URL_COLOR = (168, 162, 158)
ACCENT = (249, 115, 22)      # orange-500 — Braun-ish accent

FONT_BOLD = r"C:\Windows\Fonts\msjhbd.ttc"   # Microsoft JhengHei Bold
FONT_REG = r"C:\Windows\Fonts\msjh.ttc"

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Subtle accent stripe along the left edge
draw.rectangle((0, 0, 8, H), fill=ACCENT)

# Icon: 420x420 on the left, vertically centered
icon = Image.open(ICON_PATH).convert("RGBA")
icon = icon.resize((420, 420), Image.LANCZOS)
icon_x, icon_y = 80, (H - 420) // 2
img.paste(icon, (icon_x, icon_y), icon)

# Right column text area
text_x = 560

# Title
font_title = ImageFont.truetype(FONT_BOLD, 76)
draw.text((text_x, 165), "QQder 核舟記", fill=TITLE_COLOR, font=font_title)

# Tagline
font_tagline = ImageFont.truetype(FONT_REG, 32)
draw.text((text_x, 285), "Free, ad-free iOS Apps", fill=TAGLINE_COLOR, font=font_tagline)
draw.text((text_x, 330), "+ AI dev journal", fill=TAGLINE_COLOR, font=font_tagline)

# Accent bar above URL
draw.rectangle((text_x, 410, text_x + 100, 416), fill=ACCENT)

# URL
font_url = ImageFont.truetype(FONT_REG, 24)
draw.text((text_x, 430), "ccqqder.github.io/PeachPitBoat", fill=URL_COLOR, font=font_url)

img.save(OUT_PATH, "PNG", optimize=True)
print(f"Saved: {OUT_PATH}")
print(f"Size: {OUT_PATH.stat().st_size:,} bytes ({W}x{H})")

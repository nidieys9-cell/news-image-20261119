#!/usr/bin/env python3
"""Draw the news-image-20261119 entry: one infographic summing up
Thursday, 19 November 2026 world news. Run: python3 draw.py
Writes entry.png (1024x1024) beside this file. Facts verified from
19 Nov 2026 reporting; sources are listed in README.md."""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

W = H = 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

BG = (243, 245, 248)
NAVY = (13, 33, 66)
GOLD = (245, 183, 49)
WHITE = (255, 255, 255)
INK = (22, 28, 38)
MUTED = (88, 98, 112)
CARD = (255, 255, 255)

def font(path, size):
    return ImageFont.truetype(path, size)

F_TITLE = font(BOLD, 56)
F_DATE = font(BOLD, 33)
F_SUB = font(REG, 19)
F_TAG = font(BOLD, 16)
F_HEAD = font(BOLD, 25)
F_HEAD_HERO = font(BOLD, 30)
F_BODY = font(REG, 19)
F_FOOT = font(REG, 16)

STORIES = [
    # tag, accent, headline, body
    ("POLITICS - SHENZHEN", (198, 40, 40),
     "Trump, Xi and Putin hold first-ever trilateral talks",
     "At APEC in Shenzhen the three leaders discuss nuclear arms, Ukraine, "
     "Iran, trade and AI. Analysts expect no immediate breakthroughs."),
    ("TECH - ECONOMY", (21, 101, 192),
     "Anthropic's $81.3B IPO is the biggest ever",
     "Priced at $83 a share, topping SpaceX. Nasdaq debut today as ANT, "
     "valued near $1.5 trillion fully diluted."),
    ("CLIMATE - COP31", (46, 125, 50),
     "COP31 deadlocked in Antalya",
     "Nearly 200 nations struggle for a climate deal in the final days, "
     "split over fossil fuels, finance and science."),
    ("LAW - THE HAGUE", (106, 27, 154),
     "World Court rules on Rohingya genocide case",
     "The ICJ delivers its judgment in Gambia v. Myanmar over the 2017 "
     "campaign against the Rohingya."),
    ("WEATHER - INDIA", (230, 126, 34),
     "Cyclone Akvan: mass evacuations in Odisha",
     "Tens of thousands moved to shelters as the severe storm nears "
     "Gopalpur, due to make landfall on Nov 20."),
    ("HUMANITARIAN", (0, 131, 143),
     "Record 589M children lived in conflict zones",
     "Save the Children: nearly 1 in 4 children worldwide lived in a "
     "conflict zone in 2025, a record since 1990."),
    ("CULTURE - NEW YORK", (173, 20, 87),
     "Van Gogh sells for a record $190.4M",
     "\"Blossoming Chestnut Trees\" (1890) sets an artist auction record "
     "at Sotheby's in New York."),
]

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def icon(draw, kind, cx, cy, color):
    """Simple geometric icons drawn with PIL shapes."""
    r = 26
    if kind == 0:  # globe
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
        draw.line([cx - r, cy, cx + r, cy], fill=color, width=3)
        draw.ellipse([cx - 11, cy - r, cx + 11, cy + r], outline=color, width=3)
    elif kind == 1:  # rising chart
        draw.line([cx - r, cy + r, cx - r, cy - r], fill=color, width=4)
        draw.line([cx - r, cy + r, cx + r, cy + r], fill=color, width=4)
        pts = [(cx - 18, cy + 12), (cx - 4, cy - 2), (cx + 8, cy + 4), (cx + 22, cy - 18)]
        draw.line(pts, fill=color, width=5, joint="curve")
    elif kind == 2:  # sun with rays (climate)
        draw.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], outline=color, width=4)
        for dx, dy in [(0, -24), (0, 24), (-24, 0), (24, 0),
                       (-17, -17), (17, -17), (-17, 17), (17, 17)]:
            draw.line([cx + dx * 3 // 4, cy + dy * 3 // 4, cx + dx, cy + dy],
                      fill=color, width=4)
    elif kind == 3:  # scales
        draw.line([cx, cy - r, cx, cy + r], fill=color, width=4)
        draw.line([cx - r, cy - 16, cx + r, cy - 16], fill=color, width=4)
        draw.polygon([(cx - r, cy - 16), (cx - r + 9, cy + 2), (cx - r + 18, cy - 16)], outline=color, width=3)
        draw.polygon([(cx + r - 18, cy - 16), (cx + r - 9, cy + 2), (cx + r, cy - 16)], outline=color, width=3)
    elif kind == 4:  # cyclone swirl
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=300, fill=color, width=5)
        draw.arc([cx - 15, cy - 15, cx + 15, cy + 15], start=200, end=120, fill=color, width=5)
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=color)
    elif kind == 5:  # heart
        draw.polygon([(cx, cy + 22), (cx - 24, cy - 2), (cx - 12, cy - 20),
                      (cx, cy - 8), (cx + 12, cy - 20), (cx + 24, cy - 2)], fill=color)
    else:  # palette / star for art
        draw.polygon([(cx, cy - r), (cx + 7, cy - 7), (cx + r, cy - 5), (cx + 10, cy + 5),
                      (cx + 15, cy + r), (cx, cy + 11), (cx - 15, cy + r), (cx - 10, cy + 5),
                      (cx - r, cy - 5), (cx - 7, cy - 7)], fill=color)

def card(draw, x, y, w, h, idx, hero=False):
    tag, accent, head, body = STORIES[idx]
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=CARD,
                           outline=(210, 216, 224), width=2)
    draw.rounded_rectangle([x, y, x + 10, y + h], radius=5, fill=accent)
    ix = x + 52
    icon(draw, idx, ix, y + h // 2, accent)
    tx = x + 96
    draw.text((tx, y + 10), tag, font=F_TAG, fill=accent)
    hf = F_HEAD_HERO if hero else F_HEAD
    lines = wrap(draw, head, hf, x + w - tx - 18)
    ly = y + 34
    for ln in lines[:2]:
        draw.text((tx, ly), ln, font=hf, fill=INK)
        ly += 34 if hero else 30
    for ln in wrap(draw, body, F_BODY, x + w - tx - 18)[:3]:
        draw.text((tx, ly + 2), ln, font=F_BODY, fill=MUTED)
        ly += 24

def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Header (deep teal-navy band, gold rule)
    d.rectangle([0, 0, W, 162], fill=(10, 42, 58))
    d.rectangle([0, 162, W, 170], fill=GOLD)
    d.text((40, 22), "THE WORLD TODAY", font=F_TITLE, fill=WHITE)
    d.text((40, 92), "Thursday, 19 November 2026", font=F_DATE, fill=GOLD)
    sub = "Seven stories that shaped the day - politics, tech, climate, law, weather, aid, art"
    d.text((40, 134), sub, font=F_SUB, fill=(190, 200, 218))
    # Hero card
    card(d, 32, 186, 960, 146, 0, hero=True)
    # 3 rows x 2 cards
    y = 346
    idx = 1
    for _ in range(3):
        card(d, 32, y, 472, 202, idx)
        card(d, 520, y, 472, 202, idx + 1)
        idx += 2
        y += 214
    d.text((40, 992), "Sources: Reuters - AFP - The Guardian - Save the Children - BusinessWorld - The Hindu BusinessLine",
           font=F_FOOT, fill=MUTED)
    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")

if __name__ == "__main__":
    main()

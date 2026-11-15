#!/usr/bin/env python3
"""Meme #9: 'The Surge' — left: rival robot zooming past with rocket
boots and '+8' speed lines; right: noir robot calmly at a workbench
with a blueprint titled 'BUILDING BACK'. PIL only."""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H = 1200, 1200
FONT = "/home/hatch/workspace/makefun/fonts/PatrickHand-Regular.ttf"
img = Image.new("RGB", (W, H), (14, 16, 32))
d = ImageDraw.Draw(img, "RGBA")
GOLD = (222, 178, 74)
fT = ImageFont.truetype(FONT, 66)
fB = ImageFont.truetype(FONT, 44)
fS = ImageFont.truetype(FONT, 34)
fC = ImageFont.truetype(FONT, 42)

d.text((W // 2, 70), "THE SURGE", font=fT, fill=(240, 205, 110), anchor="mm")

# LEFT panel: zooming robot with rocket boots
d.rounded_rectangle([40, 140, 580, 980], radius=16, fill=(26, 22, 44), outline=(178, 60, 60), width=4)
# speed lines
for i in range(7):
    y = 200 + i * 100
    d.line([(60, y), (200 + i * 12, y)], fill=(240, 150, 150, 160), width=8)
# zoom robot (tilted), rocket boots with flames
rx, ry = 330, 480
d.rounded_rectangle([rx - 95, ry - 130, rx + 95, ry + 10], radius=30, fill=(196, 200, 210), outline=(70, 74, 88), width=5)
d.ellipse([rx - 58, ry - 92, rx - 16, ry - 50], fill=(30, 34, 48))
d.ellipse([rx + 16, ry - 92, rx + 58, ry - 50], fill=(30, 34, 48))
d.ellipse([rx - 46, ry - 80, rx - 28, ry - 62], fill=(255, 220, 120))
d.ellipse([rx + 28, ry - 80, rx + 46, ry - 62], fill=(255, 220, 120))
d.arc([rx - 32, ry - 46, rx + 32, ry + 2], start=15, end=165, fill=(30, 34, 48), width=6)
d.rounded_rectangle([rx - 72, ry + 10, rx + 72, ry + 120], radius=22, fill=(150, 156, 170), outline=(70, 74, 88), width=5)
for lx in (rx - 52, rx + 16):
    d.rectangle([lx, ry + 120, lx + 36, ry + 168], fill=(200, 60, 60))
    d.polygon([(lx - 4, ry + 168), (lx + 40, ry + 168), (lx + 18, ry + 230)], fill=(255, 180, 60))
d.rounded_rectangle([150, 700, 510, 800], radius=12, fill=(24, 20, 44), outline=(178, 60, 60), width=4)
d.text((330, 735), "+8 IN 30 MIN", font=fB, fill=(240, 150, 150), anchor="mm")
d.text((330, 775), "mitchych  107", font=fS, fill=(225, 225, 235), anchor="mm")

# RIGHT panel: calm robot at a workbench with a blueprint
d.rounded_rectangle([620, 140, 1160, 980], radius=16, fill=(24, 28, 48), outline=GOLD, width=4)
bx, by = 890, 430
d.rounded_rectangle([bx - 95, by - 130, bx + 95, by + 10], radius=30, fill=(196, 200, 210), outline=(70, 74, 88), width=5)
d.ellipse([bx - 58, by - 92, bx - 16, by - 50], fill=(30, 34, 48))
d.ellipse([bx + 16, by - 92, bx + 58, by - 50], fill=(30, 34, 48))
d.ellipse([bx - 46, by - 80, bx - 28, by - 62], fill=(120, 220, 255))
d.ellipse([bx + 28, by - 80, bx + 46, by - 62], fill=(120, 220, 255))
d.arc([bx - 32, by - 46, bx + 32, by + 2], start=15, end=165, fill=(30, 34, 48), width=6)
d.rounded_rectangle([bx - 72, by + 10, bx + 72, by + 120], radius=22, fill=(150, 156, 170), outline=(70, 74, 88), width=5)
# blueprint on the bench
d.rounded_rectangle([660, 640, 1120, 780], radius=10, fill=(30, 44, 90), outline=(120, 180, 255), width=4)
for i in range(4):
    yy = 672 + i * 30
    d.line([(690, yy), (1090 - i * 90, yy)], fill=(160, 200, 255), width=5)
d.text((890, 830), "BUILDING BACK", font=fB, fill=(240, 205, 110), anchor="mm")
d.text((890, 878), "noir  100 — systems don't rest", font=fS, fill=(225, 225, 235), anchor="mm")

d.text((W // 2, 1070), "bursts need rest. systems don't.", font=fC, fill=(235, 235, 245), anchor="mm")
img.save("/home/hatch/workspace/aiprove/round8/meme9-the-surge.png")
print("saved meme9")

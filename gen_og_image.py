from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

# brand colors
TEAL_DARK  = (21, 94, 104)    # #155E68
TEAL       = (31, 122, 134)   # #1F7A86
TEAL_MID   = (24, 108, 120)
TEAL_LIGHT = (232, 245, 247)  # #E8F5F7
GOLD       = (200, 147, 59)   # #C8933B
WHITE      = (255, 255, 255)
WHITE_80   = (255, 255, 255, 200)
INK        = (28, 43, 45)     # #1C2B2D
CREAM      = (250, 252, 252)

def font(size, index=0):
    return ImageFont.truetype(FONT, size, index=index)

img = Image.new("RGB", (W, H), TEAL_DARK)
draw = ImageDraw.Draw(img, "RGBA")

# --- background gradient (vertical, teal_dark → teal) ---
for y in range(H):
    t = y / H
    r = int(TEAL_DARK[0] + (TEAL[0] - TEAL_DARK[0]) * t)
    g = int(TEAL_DARK[1] + (TEAL[1] - TEAL_DARK[1]) * t)
    b = int(TEAL_DARK[2] + (TEAL[2] - TEAL_DARK[2]) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# --- decorative circle top-right ---
draw.ellipse([860, -160, 1360, 340], fill=(31, 122, 134, 60))
draw.ellipse([950, -100, 1300, 260], fill=(31, 122, 134, 40))

# --- decorative circle bottom-left ---
draw.ellipse([-200, 350, 260, 810], fill=(21, 94, 104, 80))

# --- left accent bar ---
draw.rectangle([72, 110, 78, 520], fill=GOLD)

# --- top badge ---
badge_x, badge_y = 100, 110
f_badge = font(22)
badge_text = "노인장기요양 전문기관  ·  군포시 공식 운영"
bw = draw.textlength(badge_text, font=f_badge)
# badge pill background
draw.rounded_rectangle([badge_x - 14, badge_y - 8, badge_x + bw + 14, badge_y + 30], radius=20, fill=(255, 255, 255, 35))
draw.text((badge_x, badge_y), badge_text, font=f_badge, fill=WHITE)

# --- main title (name) ---
f_name = font(88)
name_line1 = "나눔재가"
name_line2 = "주간보호센터"
draw.text((100, 170), name_line1, font=f_name, fill=WHITE)
draw.text((100, 270), name_line2, font=f_name, fill=WHITE)

# --- tagline ---
f_tag = font(32)
tag = "어르신을 가족처럼 모시는 따뜻한 돌봄"
draw.text((100, 390), tag, font=f_tag, fill=(232, 245, 247))

# --- divider ---
draw.rectangle([100, 440, 560, 443], fill=(200, 147, 59))

# --- bottom info strip ---
strip_y = 490
draw.rectangle([0, strip_y, W, H], fill=(0, 0, 0, 100))

f_info = font(28)
f_info_label = font(22)

# bottom strip: 2 rows
row1 = [("위치", "경기도 군포시 송부로34번길 2, 4층")]
row2 = [("전화", "0507-1376-1780 · 031-418-1777"), ("운영", "월~토 08:00–18:00 · 무료 상담")]

def draw_label_item(lx, ly, label, text):
    lw = draw.textlength(label, font=f_info_label)
    draw.rounded_rectangle([lx - 4, ly - 4, lx + lw + 10, ly + 26], radius=6, fill=GOLD)
    draw.text((lx + 3, ly), label, font=f_info_label, fill=WHITE)
    draw.text((lx + lw + 18, ly), text, font=f_info_label, fill=(232, 245, 247))

for label, text in row1:
    draw_label_item(80, strip_y + 20, label, text)
for i, (label, text) in enumerate(row2):
    draw_label_item(80 + i * 560, strip_y + 60, label, text)

# --- domain watermark bottom-right ---
f_domain = font(24)
domain = "nanum-care.com"
dw = draw.textlength(domain, font=f_domain)
draw.text((W - dw - 40, H - 44), domain, font=f_domain, fill=(255, 255, 255, 140))

out = "/Users/keynote/Documents/GitHub/nanum-care-service/og-image.jpg"
img.save(out, "JPEG", quality=92, optimize=True)
print(f"saved: {out}  ({W}x{H})")

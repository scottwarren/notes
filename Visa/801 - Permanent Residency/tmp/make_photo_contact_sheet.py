from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


SOURCE = Path("/Users/scottwarren/Documents/Visas/Permanent Resident Visa/801 - Permanent Visa/Evidence/Relationship Photo Timeline - WaKr-2631-801-3")
OUTPUT = Path("/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency/tmp/photo-contact-sheet.jpg")


def natural_key(path: Path):
    return int(path.stem.rsplit("-", 1)[-1].strip())


paths = sorted(SOURCE.glob("*.jpeg"), key=natural_key)
thumb_w, thumb_h = 360, 270
caption_h = 38
cols = 3
rows = (len(paths) + cols - 1) // cols
sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + caption_h)), "white")
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default(size=18)

for idx, path in enumerate(paths):
    img = Image.open(path).convert("RGB")
    fitted = ImageOps.contain(img, (thumb_w - 12, thumb_h - 12))
    x0 = (idx % cols) * thumb_w
    y0 = (idx // cols) * (thumb_h + caption_h)
    x = x0 + (thumb_w - fitted.width) // 2
    y = y0 + (thumb_h - fitted.height) // 2
    sheet.paste(fitted, (x, y))
    draw.rectangle((x0, y0, x0 + thumb_w - 1, y0 + thumb_h + caption_h - 1), outline="#cccccc", width=1)
    draw.text((x0 + 10, y0 + thumb_h + 6), f"Photo {idx + 1}", fill="black", font=font)

sheet.save(OUTPUT, quality=90)
print(OUTPUT)

from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont

ROOT = Path("/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency/tmp")
for folder in ["render-relationship", "render-mum-review", "render-photo-timeline", "render-checklist"]:
    source = ROOT / folder
    pages = sorted(source.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
    if not pages:
        continue
    col_w = 1000
    label_h = 34
    thumb_h = 1294
    cols = 2
    rows = (len(pages) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * col_w, rows * (thumb_h + label_h)), "#d7d7d7")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=18)
    for i, page in enumerate(pages):
        image = Image.open(page).convert("RGB")
        thumb = ImageOps.contain(image, (col_w - 16, thumb_h - 16))
        x0 = (i % cols) * col_w
        y0 = (i // cols) * (thumb_h + label_h)
        x = x0 + (col_w - thumb.width) // 2
        y = y0 + 8
        sheet.paste(thumb, (x, y))
        draw.text((x0 + 12, y0 + thumb_h + 5), f"{folder} page {i+1}", fill="black", font=font)
    out = ROOT / f"{folder}-contact.jpg"
    sheet.save(out, quality=90)
    print(out)

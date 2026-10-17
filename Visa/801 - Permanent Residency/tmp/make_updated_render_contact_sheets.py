from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

ROOT = Path('/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency/tmp')
for name in ['render-checklist-updated', 'render-report-updated', 'render-photo-timeline-updated', 'render-relationship-updated']:
    paths = sorted((ROOT / name).glob('page-*.png'), key=lambda p: int(p.stem.split('-')[-1]))
    cols, tw, th, label = 3, 420, 594, 26
    rows = (len(paths) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * tw, rows * (th + label)), 'white')
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(paths):
        image = Image.open(path).convert('RGB')
        thumb = ImageOps.contain(image, (tw - 12, th - 12))
        x0, y0 = (i % cols) * tw, (i // cols) * (th + label)
        x, y = x0 + (tw - thumb.width)//2, y0 + (th - thumb.height)//2
        sheet.paste(thumb, (x, y))
        draw.rectangle((x0, y0, x0+tw-1, y0+th+label-1), outline='#bbbbbb')
        draw.text((x0+8, y0+th+5), f'Page {i+1}', fill='black')
    out = ROOT / f'{name}-contact.jpg'
    sheet.save(out, quality=88)
    print(out)

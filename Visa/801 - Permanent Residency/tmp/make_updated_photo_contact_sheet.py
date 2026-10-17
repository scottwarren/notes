from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

SOURCE = Path('/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency/tmp/photo-album-export-2026-10-18')
OUTPUT = Path('/Users/scottwarren/projects/notes/Personal/Visa/801 - Permanent Residency/tmp/photo-album-contact-sheet-2026-10-18.jpg')

dates = [
    '15 Aug 2025 2:08', '15 Aug 2025 2:54', '29 Aug 2025 5:14',
    '8 Nov 2025 6:11', '8 Nov 2025 6:11', '8 Nov 2025 7:13',
    '23 Dec 2025 6:18', '23 Dec 2025 8:58', '23 Dec 2025 11:00',
    '23 Dec 2025 11:00', '23 Dec 2025 11:28', '25 Dec 2025 7:49',
    '28 Dec 2025 4:32', '4 Jan 2026 2:24', '7 Jan 2026 10:01',
    '10 Jan 2026 3:38', '10 Jan 2026 3:38', '28 Feb 2026 9:46',
    '4 Jun 2026 1:01', '11 Jun 2026 3:11', '14 Jun 2026 2:35',
    '16 Jun 2026 1:48', '16 Jun 2026 2:27', '19 Jun 2026 7:58',
    '19 Jun 2026 7:58', '11 Jul 2026 2:40', '11 Jul 2026 2:40',
    '19 Jul 2026 3:45', '19 Jul 2026 3:45', '2 Aug 2026 10:59',
    '2 Aug 2026 10:59', '11 Aug 2026 8:02', '29 Aug 2026 3:59',
    '29 Aug 2026 4:14',
]

def key(p):
    return int(p.stem.rsplit('-', 1)[-1].strip())

paths = sorted(SOURCE.glob('*.jpeg'), key=key)
tw, th, ch, cols = 320, 240, 48, 4
rows = (len(paths) + cols - 1) // cols
sheet = Image.new('RGB', (cols * tw, rows * (th + ch)), 'white')
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default(size=15)
for i, p in enumerate(paths):
    img = Image.open(p).convert('RGB')
    img = ImageOps.exif_transpose(img)
    fit = ImageOps.contain(img, (tw - 10, th - 10))
    x0, y0 = (i % cols) * tw, (i // cols) * (th + ch)
    x, y = x0 + (tw-fit.width)//2, y0 + (th-fit.height)//2
    sheet.paste(fit, (x, y))
    draw.rectangle((x0, y0, x0+tw-1, y0+th+ch-1), outline='#bbbbbb')
    draw.text((x0+8, y0+th+5), f'{i+1}. {dates[i]}', fill='black', font=font)
sheet.save(OUTPUT, quality=92)
print(OUTPUT)

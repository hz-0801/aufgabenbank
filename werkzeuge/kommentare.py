"""Kommentare aus einem kommentierten PDF mit Stelle auslesen und je Kommentar einen Ausschnitt rendern.
Aufruf: python3 -I kommentare.py <kommentiert.pdf> <aus-ordner>
Schreibt <aus-ordner>/kommentare.csv (seite, kennung, nr, x0, y0, x1, y1, markiert, kommentar) und
<aus-ordner>/k-<seite>-<nr>.png (Ausschnitt um die Markierung, Markierung gelb). Koordinaten in pt, Ursprung unten links.
Warum: Ohne Stelle ist ein Kommentar wie „verzichte auf diese Aufgabe“ nicht zuzuordnen (Lehrer 15.10.)."""
import csv, re, subprocess, sys
from pathlib import Path
import pypdf
from PIL import Image, ImageDraw

pdf, aus = Path(sys.argv[1]), Path(sys.argv[2])
aus.mkdir(parents=True, exist_ok=True)
DPI, RAND, MINH = 130, 70, 170          # Rand ober-/unterhalb der Markierung (pt), Mindesthöhe (pt)
r = pypdf.PdfReader(str(pdf))

def text_in(seite, x0, y0, x1, y1, h):
    out = subprocess.run(['pdftotext', '-f', str(seite), '-l', str(seite), '-x', str(int(x0)), '-y', str(int(h - y1)),
                          '-W', str(int(x1 - x0) + 1), '-H', str(int(y1 - y0) + 1), '-r', '72', str(pdf), '-'],
                         capture_output=True, text=True).stdout
    return ' '.join(out.split())

zeilen = []
for i, p in enumerate(r.pages, 1):
    annots = [a.get_object() for a in (p.get('/Annots') or [])]
    annots = [a for a in annots if a.get('/Subtype') not in ('/Link', '/Popup')]
    if not annots:
        continue
    w, h = float(p.mediabox.width), float(p.mediabox.height)
    kopf = ' '.join(subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-y', '0', '-H', '60', '-W', str(int(w)),
                                   '-r', '72', str(pdf), '-'], capture_output=True, text=True).stdout.split())
    m = re.search(r'\b([PALFS][A-Z]\d{2,3}-\d+)\b', kopf)
    kennung = m.group(1) if m else ''
    for nr, a in enumerate(annots, 1):
        x0, y0, x1, y1 = (float(v) for v in a['/Rect'])
        oben, unten = min(h, y1 + RAND), max(0, y0 - RAND)
        if oben - unten < MINH:
            unten = max(0, oben - MINH)
        png = aus / f'k-{i:03d}-{nr}.png'
        s = DPI / 72
        subprocess.run(['pdftoppm', '-q', '-r', str(DPI), '-f', str(i), '-l', str(i), '-singlefile', '-png',
                        '-x', '0', '-y', str(int((h - oben) * s)), '-W', str(int(w * s)), '-H', str(int((oben - unten) * s)),
                        str(pdf), str(png.with_suffix(''))], check=True)
        bild = Image.open(png).convert('RGBA')
        lage = Image.new('RGBA', bild.size, (0, 0, 0, 0))
        ImageDraw.Draw(lage).rectangle([x0 * s - 3, (oben - y1) * s - 3, x1 * s + 3, (oben - y0) * s + 3],
                                       fill=(255, 210, 0, 70), outline=(230, 150, 0, 255), width=3)
        Image.alpha_composite(bild, lage).convert('RGB').save(png, optimize=True)
        zeilen.append([i, kennung, nr, round(x0), round(y0), round(x1), round(y1),
                       text_in(i, x0, y0, x1, y1, h), ' '.join(str(a.get('/Contents') or '').split())])

with open(aus / 'kommentare.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows([['seite', 'kennung', 'nr', 'x0', 'y0', 'x1', 'y1', 'markiert', 'kommentar']] + zeilen)
print(len(zeilen), 'Kommentare →', aus)

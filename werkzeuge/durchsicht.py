"""Durchsicht-Ansicht: Seite der Mappe links, Kommentare des Lehrers und Antwort rechts.
Aufruf: python3 durchsicht.py <antworten.json> <befunde-M3.md> <bilddir> <aus.html>
Bilder: <bilddir>/s-<mappenseite neu, dreistellig>.png (Seite alt + offset)."""
import base64, html, json, re, sys
from pathlib import Path

daten = json.loads(Path(sys.argv[1]).read_text())
befunde = Path(sys.argv[2]).read_text()
bilder, aus = Path(sys.argv[3]), Path(sys.argv[4])
kenn = daten['kennung'].split('-')[0]

kommentare = {}
for m in re.finditer(r'^- S\. (\d+) · ' + kenn + r'-\d+ · „[^“]*“ → (.*?)(?=^- S\. |\Z)', befunde, re.M | re.S):
    kommentare.setdefault(m.group(1), []).append(' '.join(m.group(2).split()))

CHIP = {'ändern': 'chg', 'entschieden': 'ok', 'Handwerk': 'hw', 'Querschnitt': 'qs', 'Antwort': 'ans', 'offen': 'qs'}
teile = []
for seite, liste in kommentare.items():
    antw = daten['antworten'].get(seite, [])
    if len(antw) != len(liste):
        sys.exit(f'S. {seite}: {len(liste)} Kommentare, {len(antw)} Antworten')
    png = bilder / f's-{int(seite) + daten["offset"]:03d}.png'
    b64 = base64.b64encode(png.read_bytes()).decode()
    items = ''.join(
        f'<li><p class="lehrer">{html.escape(k)}</p>'
        f'<p class="claude"><span class="chip {CHIP.get(a[0], "ans")}">{html.escape(a[0])}</span> {html.escape(a[1])}</p></li>'
        for k, a in zip(liste, antw))
    teile.append(f'<section id="s{seite}"><figure><img src="data:image/png;base64,{b64}" alt="Mappe S. {seite}">'
                 f'<figcaption>Mappe S. {seite} · {html.escape(daten["seiten"].get(seite, ""))}</figcaption></figure>'
                 f'<ol>{items}</ol></section>')

n = sum(len(v) for v in kommentare.values())
aus.write_text(f'''<title>Durchsicht {kenn} {html.escape(daten["name"])}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Serif:ital@1&display=swap">
<style>
/* Layout: je Mappenseite eine Zeile – Seite links, Kommentar und Antwort rechts; schmal untereinander */
:root {{ --bg:#f6f7f8; --fg:#1d2329; --muted:#5d6872; --line:#d9dee3; --paper:#ffffff;
  --chg:#1f5fa8; --ok:#2e7d4f; --hw:#9a5b00; --qs:#6b4fa0; --ans:#5d6872;
  --sans:"IBM Plex Sans",system-ui,sans-serif; --serif:"IBM Plex Serif",Georgia,serif; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#14181c; --fg:#e4e8ec; --muted:#9aa5b0; --line:#2c343c; --paper:#ffffff;
  --chg:#7fb0ea; --ok:#7cc79a; --hw:#e0a35a; --qs:#b9a2e6; --ans:#9aa5b0; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#14181c; --fg:#e4e8ec; --muted:#9aa5b0; --line:#2c343c; --paper:#ffffff;
  --chg:#7fb0ea; --ok:#7cc79a; --hw:#e0a35a; --qs:#b9a2e6; --ans:#9aa5b0; color-scheme:dark }}
body {{ background:var(--bg); color:var(--fg); font:15px/1.5 var(--sans);
  padding-left:max(16px,env(safe-area-inset-left,0px)); padding-right:max(16px,env(safe-area-inset-right,0px)); padding-block:20px 40px; }}
header {{ max-width:1200px; margin:0 auto 12px; }}
h1 {{ font-size:1.3rem; margin:0; text-wrap:balance; }}
header p {{ margin:2px 0 0; color:var(--muted); font-size:.9rem; }}
section {{ max-width:1200px; margin:0 auto; display:grid; grid-template-columns:minmax(0,560px) minmax(0,1fr);
  gap:24px; padding-block:20px; border-top:1px solid var(--line); align-items:start; }}
figure {{ margin:0; position:sticky; top:calc(env(safe-area-inset-top,0px) + 8px); }}
img {{ width:100%; display:block; background:var(--paper); border:1px solid var(--line); }}
figcaption {{ font-size:.8rem; color:var(--muted); margin-top:4px; }}
ol {{ margin:0; padding-left:1.4em; display:flex; flex-direction:column; gap:14px; min-width:0; }}
li p {{ margin:0; }}
.lehrer {{ font-family:var(--serif); font-style:italic; color:var(--muted); }}
.claude {{ margin-top:4px !important; }}
.chip {{ font-size:.72rem; font-weight:600; letter-spacing:.04em; text-transform:uppercase; border:1px solid currentColor;
  border-radius:3px; padding:0 5px; margin-right:4px; }}
.chg{{color:var(--chg)}} .ok{{color:var(--ok)}} .hw{{color:var(--hw)}} .qs{{color:var(--qs)}} .ans{{color:var(--ans)}}
@media (max-width:760px) {{ section {{ grid-template-columns:1fr; }} figure {{ position:static; }} }}
</style>
<header><h1>Durchsicht {kenn} · {html.escape(daten["name"])}</h1>
<p>{n} Kommentare aus der Mappe vom 15.10. mittags; kursiv dein Kommentar, darunter meine Antwort.
Die Stelle im PDF ging beim Auslesen verloren – die Kommentare stehen in ihrer Reihenfolge neben der Seite.</p></header>
{''.join(teile)}
''')
print(aus, n, 'Kommentare')

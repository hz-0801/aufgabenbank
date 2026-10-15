"""Durchsicht-Ansicht für einen kleinen Bildschirm: je Kommentar mit laufender Nummer (Lehrer 15.10.: ansprechen) der Ausschnitt der Seite (Markierung gelb),
darunter der Kommentar des Lehrers und die Antwort; eine Spalte.
Aufruf: python3 -I durchsicht.py <antworten.json> <kommentar-ordner> <aus.html>
<kommentar-ordner> kommt aus werkzeuge/kommentare.py (kommentare.csv, k-<seite>-<nr>.png).
antworten.json: {"kennung", "name", "seiten": {seite: Beschriftung}, "antworten": {seite: [[marke, text], …]}}
(Reihenfolge je Seite wie in kommentare.csv)."""
import base64, csv, html, json, sys
from pathlib import Path

daten = json.loads(Path(sys.argv[1]).read_text())
ordner, aus = Path(sys.argv[2]), Path(sys.argv[3])
zeilen = [z for z in csv.DictReader(open(ordner / 'kommentare.csv', encoding='utf-8'))
          if z['kennung'] == daten['kennung']]
CHIP = {'ändern': 'chg', 'entschieden': 'ok', 'Handwerk': 'hw', 'Querschnitt': 'qs', 'Antwort': 'ans', 'offen': 'qs'}
teile = []
for lfd, z in enumerate(zeilen, 1):
    antw = daten['antworten'].get(z['seite'], [])
    i = int(z['nr']) - 1
    if i >= len(antw):
        sys.exit(f"S. {z['seite']} Nr. {z['nr']}: keine Antwort")
    marke, text = antw[i]
    b64 = base64.b64encode((ordner / f"k-{int(z['seite']):03d}-{z['nr']}.png").read_bytes()).decode()
    ort = f"S. {z['seite']} · {daten['seiten'].get(z['seite'], '')}"
    teile.append(f'''<article><p class="ort"><b class="nr">{lfd}</b> {html.escape(ort)}</p>
<img src="data:image/png;base64,{b64}" alt="Ausschnitt {html.escape(ort)}">
<p class="lehrer">{html.escape(z['kommentar'] or '(ohne Text)')}</p>
<p class="claude"><span class="chip {CHIP.get(marke, 'ans')}">{html.escape(marke)}</span> {html.escape(text)}</p></article>''')

PRUEF = {'P': 'P10', 'A': 'Abitur GK', 'L': 'Abitur LK', 'F': 'FHR', 'S': 'Schulstoff'}
aus.write_text(f'''<title>Durchsicht {PRUEF.get(daten['kennung'][0], '')}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Serif:ital@1&display=swap">
<style>
/* Layout: eine Spalte für kleine Bildschirme; je Kommentar Ausschnitt, Kommentar, Antwort */
:root {{ --bg:#f6f7f8; --fg:#1d2329; --muted:#5d6872; --line:#d9dee3; --paper:#ffffff;
  --chg:#1f5fa8; --ok:#2e7d4f; --hw:#9a5b00; --qs:#6b4fa0; --ans:#5d6872;
  --sans:"IBM Plex Sans",system-ui,sans-serif; --serif:"IBM Plex Serif",Georgia,serif; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#14181c; --fg:#e4e8ec; --muted:#9aa5b0; --line:#2c343c;
  --chg:#7fb0ea; --ok:#7cc79a; --hw:#e0a35a; --qs:#b9a2e6; --ans:#9aa5b0; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#14181c; --fg:#e4e8ec; --muted:#9aa5b0; --line:#2c343c;
  --chg:#7fb0ea; --ok:#7cc79a; --hw:#e0a35a; --qs:#b9a2e6; --ans:#9aa5b0; color-scheme:dark }}
body {{ background:var(--bg); color:var(--fg); font:15px/1.5 var(--sans);
  padding-left:max(12px,env(safe-area-inset-left,0px)); padding-right:max(12px,env(safe-area-inset-right,0px)); padding-block:12px 32px; }}
main {{ max-width:720px; margin:0 auto; display:flex; flex-direction:column; gap:22px; }}
h1 {{ font-size:1.15rem; margin:0; }}
article {{ display:flex; flex-direction:column; gap:6px; padding-top:14px; border-top:1px solid var(--line); min-width:0; }}
.nr {{ font-size:1rem; color:var(--fg); margin-right:6px; }}
.ort {{ margin:0; font-size:.78rem; color:var(--muted); letter-spacing:.03em; }}
img {{ width:100%; display:block; background:var(--paper); border:1px solid var(--line); }}
p {{ margin:0; }}
.lehrer {{ font-family:var(--serif); font-style:italic; color:var(--muted); }}
.chip {{ font-size:.7rem; font-weight:600; letter-spacing:.04em; text-transform:uppercase; border:1px solid currentColor;
  border-radius:3px; padding:0 5px; margin-right:4px; }}
.chg{{color:var(--chg)}} .ok{{color:var(--ok)}} .hw{{color:var(--hw)}} .qs{{color:var(--qs)}} .ans{{color:var(--ans)}}
</style>
<main><h1>Durchsicht {html.escape(daten['kennung'])} · {html.escape(daten['name'])}</h1>
{''.join(teile)}
</main>
''')
print(aus, len(teile), 'Kommentare')

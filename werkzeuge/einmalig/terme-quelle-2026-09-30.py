#!/usr/bin/env python3
"""Einmalig, 2026-09-30: quelle-Nummern von bank/terme auf die Mappe
nachziehen. Anlass: der Katalog terme.md hat am 30.09. einen neuen
Erkennungsschritt (Zeile 37) bekommen, alle Zeilen danach rückten um
eins. Je Bankzeile wird sprosse_text in Teil 1 der Mappe gesucht;
steht er in der alten Zeile quelle, bleibt sie; sonst gilt die
nächstgelegene Zeile, die ihn enthält. Kein Treffer: Meldung, Zeile
bleibt. Aufruf aus der Wurzel des Repos: python3 werkzeuge/einmalig/
terme-quelle-2026-09-30.py [eintrag]"""
import json
import re
import sys
from pathlib import Path

eintrag = sys.argv[1] if len(sys.argv) > 1 else "terme"
wurzel = Path(__file__).resolve().parents[2]
mappe = wurzel / "mappen" / f"{eintrag}.md"
text = mappe.read_text(encoding="utf-8")
teil = text.split("## 1 Katalogeintrag", 1)[-1].split("\n## 2 ", 1)[0]
katalog = {}
for z in teil.split("\n"):
    m = re.match(r"\s*(\d+)  (.*)$", z)
    if m:
        katalog[int(m.group(1))] = m.group(2)

geaendert = offen = 0
for datei in sorted((wurzel / "bank" / eintrag).glob("*.jsonl")):
    aus = []
    for roh in datei.read_text(encoding="utf-8").split("\n"):
        if roh == "":
            continue
        a = json.loads(roh)
        alt = a["quelle"]
        treffer = [n for n, t in katalog.items() if a["sprosse_text"] in t]
        if alt in treffer:
            neu = alt
        elif treffer:
            neu = min(treffer, key=lambda n: (abs(n - alt), n))
        else:
            print(f"OFFEN {a['id']}: sprosse_text in keiner Zeile")
            offen += 1
            neu = alt
        if neu != alt:
            a["quelle"] = neu
            geaendert += 1
            aus.append(json.dumps(a, ensure_ascii=False))
        else:
            aus.append(roh)
    datei.write_text("\n".join(aus) + "\n", encoding="utf-8")
print(f"geändert {geaendert}, offen {offen}")

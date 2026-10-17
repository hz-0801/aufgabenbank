#!/usr/bin/env python3
"""Prüft VERA-Bankzeilen einer Proben-Datei mit bank-pruef.py (Zeile für Zeile).
  python3 vera-pruef.py <eintrag> <datei.jsonl>
Zusatzfelder fallen (Liste), vera_stufe, herkunft sind Pflicht; ruhende Zeilen nur gezählt."""
import importlib.util, json, sys, collections
from pathlib import Path
spec = importlib.util.spec_from_file_location('bp', '/home/claude/aufgabenbank/werkzeuge/bank-pruef.py')
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
eintrag, datei = sys.argv[1], sys.argv[2]
ctx, wg = bp.kontext(eintrag, Path('/home/claude/aufgabenbank'))
n = bad = ruht = 0; cnt = collections.Counter()
for l in open(datei, encoding='utf8'):
    a = json.loads(l)
    if a.get('eintrag') != eintrag: continue
    n += 1
    if a.get('ruht'): ruht += 1; continue
    fehl = [f for f in ('fallen', 'vera_stufe', 'herkunft') if f not in a]
    b = {k: v for k, v in a.items() if k not in ('fallen', 'vera_stufe')}
    key = (a['einheit'], a['kette_nr'], a['sprosse']); cnt[key] += 1
    b['variante'] = cnt[key]
    b['id'] = f"{eintrag}-e{a['einheit']}-k{a['kette_nr']}-s{a['sprosse']}-v{cnt[key]}"
    bf, w = bp.pruefe_zeile(b, eintrag, a['einheit'], ctx)
    if bf or fehl: bad += 1; print(a['id'], '|', fehl, bf, w)
print(f'{eintrag}: {n} Zeilen, {ruht} ruhend, {bad} mit Befund')

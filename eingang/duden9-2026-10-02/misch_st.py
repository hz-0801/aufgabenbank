#!/usr/bin/env python3
"""Mischlauf (Vorlage misch_pyt.py, ein Eintrag daten): Bank-Kopie +
neue Zeilen in st-pruefbaum/, Sprossen der betroffenen Ketten neu
nummeriert. Klone bleiben unverändert."""
import json, copy, shutil, os

S = 'aufgabenbank/'
Z = 'st-pruefbaum/'
E = 'daten'
NACH = {'NEU-alle-kenngroessen': 7, 'NEU-mittel-haeufigkeitstabelle': 8,
        'NEU-quartile-rangplatz': 5, 'NEU-mittlere-abweichung': 1,
        'NEU-histogramm-waehlen': 1, 'NEU-streifen-vergleich': 2}
if os.path.exists(Z):
    shutil.rmtree(Z)
shutil.copytree(S + 'werkzeuge', Z + 'werkzeuge',
                ignore=shutil.ignore_patterns('__pycache__'))
os.makedirs(Z + 'mappen')
if os.path.exists(S + 'mappen/_bausteine.md'):
    shutil.copy(S + 'mappen/_bausteine.md', Z + 'mappen/')
shutil.copy(S + f'mappen/{E}.md', Z + 'mappen/')
os.makedirs(Z + f'bank/{E}')
for x in ('zone.jsonl', 'stand.md'):
    shutil.copy(S + f'bank/{E}/{x}', Z + f'bank/{E}/')
neu = [json.loads(l) for l in open('neu-st-duden9.jsonl')]
for e in range(1, 8):
    d = f'e{e}'
    alt = [json.loads(l) for l in open(S + f'bank/{E}/{d}.jsonl')]
    mein = [r for r in neu if r['einheit'] == e]
    out = []
    for i, r in enumerate(alt):
        out.append(dict(r, _g=('alt', r['kette_nr'], r['sprosse'])))
        nxt = alt[i + 1] if i + 1 < len(alt) else None
        if nxt and nxt['kette_nr'] == r['kette_nr'] and nxt['sprosse'] == r['sprosse']:
            continue
        for n in mein:
            if n['kette_nr'] == r['kette_nr'] and n['sprosse'] == r['sprosse']:
                out.append(dict(copy.deepcopy(n), _g=('alt', r['kette_nr'], r['sprosse'])))
        for n in mein:
            if (isinstance(n['sprosse'], str) and n['kette_nr'] == r['kette_nr']
                    and NACH[n['sprosse']] == r['sprosse']):
                out.append(dict(copy.deepcopy(n), _g=('neu', n['sprosse'])))
    neuk = {n['kette_nr'] for n in mein if isinstance(n['sprosse'], str)}
    last, nr = {}, {}
    for r in out:
        k = r['kette_nr']
        if k in neuk:
            if r['_g'] != last.get(k):
                nr[k] = r['sprosse'] if k not in last else nr[k] + 1
                last[k] = r['_g']
            r['sprosse'] = nr[k]
        r['id'] = f"{E}-e{e}-k{k}-s{r['sprosse']}-v{r['variante']}"
        del r['_g']
    assert len(out) == len(alt) + len(mein)
    with open(Z + f'bank/{E}/{d}.jsonl', 'w', encoding='utf-8', newline='\n') as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(E, d, len(alt), '->', len(out))

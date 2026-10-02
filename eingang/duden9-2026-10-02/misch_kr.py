#!/usr/bin/env python3
"""Mischlauf kreis (Vorlage misch_pyt.py): Bank-Kopie + neue Zeilen in
kr-pruefbaum/, Sprossen der betroffenen Ketten neu nummeriert; eine
NEU-Sprosse in einer neuen Kette wird ans Ende der Einheit gehängt
(Sprosse 1). Klone bleiben unverändert."""
import json, copy, shutil, os

S = 'aufgabenbank/'
Z = 'kr-pruefbaum/'
E = 'kreis'
NACH = {'NEU-umfangsaenderung': 7, 'NEU-gerade-kreis': 1,
        'NEU-kreisabschnitt': 6, 'NEU-kreisring-rueckwaerts': 7}
if os.path.exists(Z):
    shutil.rmtree(Z)
shutil.copytree(S + 'werkzeuge', Z + 'werkzeuge',
                ignore=shutil.ignore_patterns('__pycache__'))
os.makedirs(Z + 'mappen')
if os.path.exists(S + 'mappen/_bausteine.md'):
    shutil.copy(S + 'mappen/_bausteine.md', Z + 'mappen/')
neu = [json.loads(l) for l in open('neu-kreis-duden9.jsonl')]
shutil.copy(S + f'mappen/{E}.md', Z + 'mappen/')
os.makedirs(Z + f'bank/{E}')
shutil.copy(S + f'bank/{E}/zone.jsonl', Z + f'bank/{E}/')
for e in (1, 2, 3):
    d = f'e{e}'
    alt = [json.loads(l) for l in open(S + f'bank/{E}/{d}.jsonl')]
    mein = [r for r in neu if r['einheit'] == e]
    altk = {r['kette_nr'] for r in alt}
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
    for n in mein:                      # neue Kette: ans Ende
        if n['kette_nr'] not in altk:
            out.append(dict(copy.deepcopy(n), _g=('neu', n['sprosse'])))
    neuk = {n['kette_nr'] for n in mein if isinstance(n['sprosse'], str)}
    last, nr = {}, {}
    for r in out:
        k = r['kette_nr']
        if k in neuk:
            if r['_g'] != last.get(k):
                if k not in last:
                    nr[k] = r['sprosse'] if isinstance(r['sprosse'], int) else 1
                else:
                    nr[k] += 1
                last[k] = r['_g']
            r['sprosse'] = nr[k]
        r['id'] = f"{E}-e{e}-k{k}-s{r['sprosse']}-v{r['variante']}"
        del r['_g']
    with open(Z + f'bank/{E}/{d}.jsonl', 'w', encoding='utf-8', newline='\n') as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(E, d, len(alt), '->', len(out))

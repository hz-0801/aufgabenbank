#!/usr/bin/env python3
"""Mischlauf strahlensaetze: Bank-Kopie + neue Zeilen in
pruefbaum-sts/, Sprossen je Kette neu nummeriert. Klone unverändert.
Vorlage: misch_qf.py, erweitert auf alle Ketten."""
import json, copy, shutil, os

S = 'aufgabenbank/'
Z = 'pruefbaum-sts/'
E = 'strahlensaetze'
if os.path.exists(Z):
    shutil.rmtree(Z)
shutil.copytree(S + 'werkzeuge', Z + 'werkzeuge')
os.makedirs(Z + 'mappen')
shutil.copy(S + f'mappen/{E}.md', Z + 'mappen/')
shutil.copy(S + 'mappen/_bausteine.md', Z + 'mappen/')
os.makedirs(Z + f'bank/{E}')
shutil.copy(S + f'bank/{E}/zone.jsonl', Z + f'bank/{E}/')

neu = [json.loads(l) for l in open(f'neu-{E}-duden9.jsonl')]
NACH = {'NEU-massstabsleiste': 8, 'NEU-volumen-k3': 11,
        'NEU-gleichung-ergaenzen': 2, 'NEU-teilung-mn': 1}

for d in ('e1', 'e2', 'e3'):
    e = int(d[1])
    alt = [json.loads(l) for l in open(S + f'bank/{E}/{d}.jsonl')]
    mein = [r for r in neu if r['einheit'] == e]
    out = []
    for i, r in enumerate(alt):
        r['_g'] = ('alt', r['sprosse'])
        out.append(r)
        nxt = alt[i + 1] if i + 1 < len(alt) else None
        if nxt and nxt['kette_nr'] == r['kette_nr'] and nxt['sprosse'] == r['sprosse']:
            continue
        kn, s = r['kette_nr'], r['sprosse']
        for n in mein:
            if n['kette_nr'] == kn and n['sprosse'] == s:
                n = copy.deepcopy(n); n['_g'] = r['_g']; out.append(n)
        for n in mein:
            if n['kette_nr'] == kn and NACH.get(n['sprosse']) == s:
                n = copy.deepcopy(n); n['_g'] = ('neu', n['sprosse']); out.append(n)
    lastk, last, nr = None, None, None
    for r in out:
        if r['kette_nr'] != lastk:
            lastk, last = r['kette_nr'], None
        if r['_g'] != last:
            nr = r['sprosse'] if last is None else nr + 1
            last = r['_g']
        r['sprosse'] = nr
        r['id'] = f"{E}-e{e}-k{r['kette_nr']}-s{r['sprosse']}-v{r['variante']}"
        del r['_g']
    with open(Z + f'bank/{E}/{d}.jsonl', 'w', encoding='utf-8',
              newline='\n') as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(d, len(alt), '->', len(out))

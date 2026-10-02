#!/usr/bin/env python3
"""Mischlauf: Bank-Kopie + neue Zeilen in pruefbaum/, Sprossen neu
nummeriert. Die Klone bleiben unverändert."""
import json, copy, shutil, os

S = 'aufgabenbank/'
Z = 'pruefbaum/'
E = 'quadratische-funktionen'
if os.path.exists(Z):
    shutil.rmtree(Z)
shutil.copytree(S + 'werkzeuge', Z + 'werkzeuge')
os.makedirs(Z + 'mappen')
shutil.copy(S + f'mappen/{E}.md', Z + 'mappen/')
if os.path.exists(S + 'mappen/_bausteine.md'):
    shutil.copy(S + 'mappen/_bausteine.md', Z + 'mappen/')
os.makedirs(Z + f'bank/{E}')
shutil.copy(S + f'bank/{E}/zone.jsonl', Z + f'bank/{E}/')

neu = [json.loads(l) for l in open(f'neu-{E}-duden9.jsonl')]


def ziel(r):
    """('add', alte Sprosse) oder ('new', nach alter Sprosse, Name)."""
    s, e = r['sprosse'], r['einheit']
    if isinstance(s, str):
        nach = {'NEU-tabelle-verschoben': 4, 'NEU-steigen-fallen': 4,
                'NEU-quadr-ergaenzung': 8, 'NEU-extremwert': 12}[s]
        return ('new', nach, s)
    if e == 4:                       # Katalogsprossen, in der Bank leer
        return ('new', 3, r['sprosse_text'])
    return ('add', s)


for d in ('e1', 'e2', 'e3', 'e4'):
    e = int(d[1])
    alt = [json.loads(l) for l in open(S + f'bank/{E}/{d}.jsonl')]
    mein = [r for r in neu if r['einheit'] == e]
    out = []
    for i, r in enumerate(alt):
        r['_g'] = ('alt', r['kette_nr'], r['sprosse'])
        out.append(r)
        nxt = alt[i + 1] if i + 1 < len(alt) else None
        if r['kette_nr'] != 1 or (nxt and nxt['kette_nr'] == 1
                                  and nxt['sprosse'] == r['sprosse']):
            continue
        s = r['sprosse']
        for n in mein:
            if ziel(n) == ('add', s):
                n = copy.deepcopy(n); n['_g'] = r['_g']; out.append(n)
        for n in mein:
            z = ziel(n)
            if z[0] == 'new' and z[1] == s:
                n = copy.deepcopy(n); n['_g'] = ('neu', z[2]); out.append(n)
    last, nr = None, None
    for r in out:
        if r['kette_nr'] == 1:
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

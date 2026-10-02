#!/usr/bin/env python3
"""Mischlauf rz: Bank-Kopie + neue Zeilen in rz-pruefbaum/, NEU-Sprossen
nach ihrer Vorgängersprosse eingeschoben und die Kette neu nummeriert.
Die Klone bleiben unverändert."""
import json, copy, shutil, os

S = 'aufgabenbank/'
Z = 'rz-pruefbaum/'
NACH = {'NEU-bruchexponent': 7, 'NEU-ausmultiplizieren': 11}
if os.path.exists(Z):
    shutil.rmtree(Z)
shutil.copytree(S + 'werkzeuge', Z + 'werkzeuge')
os.makedirs(Z + 'mappen')
neu = [json.loads(l) for l in open('neu-rz-duden9.jsonl', encoding='utf-8')]
for E in ('reelle-zahlen', 'potenzen-wurzeln'):
    for f in (f'mappen/{E}.md', 'mappen/_bausteine.md'):
        if os.path.exists(S + f):
            shutil.copy(S + f, Z + 'mappen/')
    os.makedirs(Z + f'bank/{E}')
    shutil.copy(S + f'bank/{E}/zone.jsonl', Z + f'bank/{E}/')
    for e in (1, 2, 3):
        alt = [json.loads(l) for l in open(S + f'bank/{E}/e{e}.jsonl', encoding='utf-8')]
        mein = [r for r in neu if r['eintrag'] == E and r['einheit'] == e]
        def ziel(r):
            s = r['sprosse']
            return (r['kette_nr'], NACH[s] if isinstance(s, str) else s)
        out = []
        for i, r in enumerate(alt):
            r['_g'] = ('alt', r['kette_nr'], r['sprosse'])
            out.append(r)
            nxt = alt[i + 1] if i + 1 < len(alt) else None
            if nxt and (nxt['kette_nr'], nxt['sprosse']) == (r['kette_nr'], r['sprosse']):
                continue
            here = (r['kette_nr'], r['sprosse'])
            for n in mein:             # erst Zusätze, dann neue Sprosse
                if not isinstance(n['sprosse'], str) and ziel(n) == here:
                    n = copy.deepcopy(n); n['_g'] = r['_g']; out.append(n)
            for n in mein:
                if isinstance(n['sprosse'], str) and ziel(n) == here:
                    n = copy.deepcopy(n); n['_g'] = ('neu', n['sprosse']); out.append(n)
        if any(isinstance(n['sprosse'], str) for n in mein):
            last, nr = {}, {}
            for r in out:
                k = r['kette_nr']
                if r['_g'] != last.get(k):
                    nr[k] = r['sprosse'] if k not in last else nr[k] + 1
                    last[k] = r['_g']
                r['sprosse'] = nr[k]
        for r in out:
            r['id'] = f"{E}-e{e}-k{r['kette_nr']}-s{r['sprosse']}-v{r['variante']}"
            del r['_g']
        with open(Z + f'bank/{E}/e{e}.jsonl', 'w', encoding='utf-8', newline='\n') as f:
            for r in out:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
        print(E, e, len(alt), '->', len(out))

#!/usr/bin/env python3
"""Mischlauf (Vorlage misch_pyt.py, verallgemeinert auf zwei Einträge
und Hauptketten mit kette_nr != 1): Bank-Kopie + neue Zeilen in
pz-pruefbaum/, Sprossen der Hauptkette neu nummeriert. Klone bleiben
unverändert."""
import json, copy, shutil, os

S = 'aufgabenbank/'
Z = 'pz-pruefbaum/'
NACH = {'NEU-umwandlungstabelle': 4, 'NEU-zinstabelle-gemischt': 4}
if os.path.exists(Z):
    shutil.rmtree(Z)
shutil.copytree(S + 'werkzeuge', Z + 'werkzeuge')
os.makedirs(Z + 'mappen')
if os.path.exists(S + 'mappen/_bausteine.md'):
    shutil.copy(S + 'mappen/_bausteine.md', Z + 'mappen/')
neu = [json.loads(l) for l in open('neu-pz-duden9.jsonl')]
for E in ('prozentrechnung', 'zinsrechnung'):
    shutil.copy(S + f'mappen/{E}.md', Z + 'mappen/')
    os.makedirs(Z + f'bank/{E}')
    shutil.copy(S + f'bank/{E}/zone.jsonl', Z + f'bank/{E}/')
    for e in sorted({r['einheit'] for r in neu if r['eintrag'] == E} | {1, 2, 3, 4, 5}):
        d = f'e{e}'
        if not os.path.exists(S + f'bank/{E}/{d}.jsonl'):
            continue
        alt = [json.loads(l) for l in open(S + f'bank/{E}/{d}.jsonl')]
        mein = [r for r in neu if r['eintrag'] == E and r['einheit'] == e]
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
        with open(Z + f'bank/{E}/{d}.jsonl', 'w', encoding='utf-8', newline='\n') as f:
            for r in out:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
        print(E, d, len(alt), '->', len(out))

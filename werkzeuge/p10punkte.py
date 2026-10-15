#!/usr/bin/env python3
"""p10punkte.py – Jahre einer P10-Stufe für die fünf Punkte und „zuletzt JJ“, eine Quelle für alle Skripte.

Anlass: plan.md § 10, 15.10. (i): Ein voller Punkt für Jahr J heißt „der Handgriff der Stufe wurde in J verlangt“ –
gezählt Hauptplatz, ganz auch und Zwischenschritt aus mathe-nachhilfe msa/handgriffe-p10.csv, nur P10-Hefte (OS, EBR,
FOR, MUSTER-*; kein GYM; 2026 FOR und EBR sind ein Jahr). Gilt gleich für Stufenkopf der Blätter (pruefheft.py),
Bestellkarte und Handreichung (bestellkarte.py) und „zuletzt JJ“.

Eine Stufe, die kein Platz nennt (Abschnitt „Gemischt: …“), nimmt die P10-Originale ihres Felds „Originale“ der
Gliederung.

  from p10punkte import jahre
  jahre('lineare', 'Punktprobe')            -> {2017, 2021, 2022, …}
"""
import csv
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from p10einheiten import MN_VORGABE  # noqa: E402

P10 = re.compile(r'^(\d{4})-(OS|EBR|FOR|MUSTER-[A-Za-z0-9]+)-')
SPALTEN = ('hauptplatz', 'ganz_auch', 'zwischenschritt')
_CACHE = {}


def _norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip())


def tabelle(mn=MN_VORGABE):
    """(kapitel, Stufe) -> Jahre, in denen der Handgriff der Stufe in einem P10-Heft verlangt wurde."""
    mn = os.path.abspath(mn)
    if mn in _CACHE:
        return _CACHE[mn]
    T = {}
    with open(os.path.join(mn, 'msa', 'handgriffe-p10.csv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter=';'):
            m = P10.match(r['id'].strip())
            for sp in SPALTEN:
                for w in (r.get(sp) or '').split('|'):
                    if ':' not in w:
                        continue
                    k, s = (_norm(x) for x in w.split(':', 1))
                    T.setdefault((k, s), set())
                    if m:
                        T[(k, s)].add(int(m.group(1)))
    _CACHE[mn] = T
    return T


def jahre(kapitel, stufe, mn=MN_VORGABE):
    """Jahre (int) der Stufe nach Handgriffen; ohne Platz („Gemischt: …“) die P10-Originale der Gliederung."""
    T = tabelle(mn)
    key = (_norm(kapitel), _norm(stufe))
    if key in T:
        return set(T[key])
    sys.path.insert(0, os.path.join(mn, 'werkzeuge'))
    import gliederung as GL
    G = GL.lies(os.path.join(mn, 'msa', 'gliederung', kapitel + '.md'))
    for s in G['stufen']:
        if _norm(s['name']) == key[1]:
            return {int(m.group(1)) for i in s['originale'] if (m := P10.match(i))}
    return set()


if __name__ == '__main__':
    J5 = {2026, 2025, 2024, 2023, 2022}
    for (k, s), j in sorted(tabelle().items()):
        print(f'{k}:{s}: {len(j & J5)} von 5, zuletzt {max(j) if j else "–"}')

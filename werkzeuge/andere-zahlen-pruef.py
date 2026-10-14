#!/usr/bin/env python3
"""andere-zahlen-pruef.py – trägt jede Mehr-Zeile andere Zahlen als ihr Original? Nur zählen, nichts ändern.

Anlass: pruefung.md § 5 „Andere Zahlen“ (Lehrer 11.10.) und Mappe P10 (plan.md § 10, 14.10. f). Vergleicht je Zeile
aus mathe-nachhilfe msa/mehr-p10/*.csv (Vorgabe: auf_blatt = nein) die Zahlen im Feld wortlaut mit den Zahlen im
Wortlaut des Originals (aufgabenbank-privat basis-originale.jsonl, hauptteil-originale.jsonl: stamm, aufgabe,
optionen; Original = eltern_id). Urteil je Zeile:
  anders        mindestens eine Zahl der Fassung steht nicht im Original
  gleich        alle Zahlen der Fassung stehen auch im Original (Verdacht: Originalzahlen)
  ohne Zahlen   die Fassung trägt keine Zahl (Begründen, Benennen) – zählt nicht als Verstoß
  ohne Original kein Wortlaut des Originals in aufgabenbank-privat
Ausgabe nur Kennungen und Zählung, nie Wortlaut (das Skript liegt im öffentlichen Repo).
  python3 werkzeuge/andere-zahlen-pruef.py [--alle] [--privat ../aufgabenbank-privat] [--mn ../mathe-nachhilfe]
"""
import argparse, csv, glob, json, os, re, sys
from collections import Counter

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELTERN = os.path.dirname(BANK)


def zahlen(s):
    s = s or ''
    s = s.replace('{,}', ',').replace('\\,', '').replace('~', ' ').replace('−', '-')
    s = re.sub(r'\\t?frac\{(\d+)\}\{(\d+)\}', r' \1/\2 ', s)
    s = re.sub(r'(?<=\d)\s(?=\d{3}\b)', '', s)   # Tausender 1 500
    out = set()
    for m in re.finditer(r'\d+(?:,\d+)?', s):
        z = m.group(0).rstrip('0').rstrip(',') if ',' in m.group(0) else m.group(0)
        out.add(z.lstrip('0') or '0')
    return out


def originale(privat):
    o = {}
    for n in ('basis-originale.jsonl', 'hauptteil-originale.jsonl'):
        p = os.path.join(privat, n)
        if not os.path.exists(p):
            continue
        stamm = {}
        for l in open(p, encoding='utf-8'):
            if not l.strip():
                continue
            z = json.loads(l)
            key = (z['jahr'], z['papier'], z.get('nummer'))
            if z.get('stamm'):
                stamm[key] = z['stamm']
            o[z['id']] = ' '.join([stamm.get(key, ''), z.get('aufgabe', ''), ' '.join(z.get('optionen') or []),
                                   z.get('antwort', '')])
    return o


def pruefe(mn, privat, alle=False):
    O = originale(privat)
    erg = []
    for f in sorted(glob.glob(os.path.join(mn, 'msa', 'mehr-p10', '*.csv'))):
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
            if not alle and r['auf_blatt'].strip() != 'nein':
                continue
            eid = r['eltern_id'].strip()
            m = zahlen(r['wortlaut'])
            if eid not in O:
                u = 'ohne Original'
            elif not m:
                u = 'ohne Zahlen'
            elif m <= zahlen(O[eid]):
                u = 'gleich'
            else:
                u = 'anders'
            erg.append((r['id'], eid, u))
    return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alle', action='store_true', help='auch auf_blatt = ja')
    ap.add_argument('--privat', default=os.environ.get('PRIVAT') or os.path.join(ELTERN, 'aufgabenbank-privat'))
    ap.add_argument('--mn', default=os.environ.get('MATHE_NACHHILFE') or os.path.join(ELTERN, 'mathe-nachhilfe'))
    ap.add_argument('--liste', action='store_true', help='Kennungen der Zeilen mit „gleich“ und „ohne Original“')
    a = ap.parse_args()
    erg = pruefe(a.mn, a.privat, a.alle)
    c = Counter(u for _, _, u in erg)
    print(f'{len(erg)} Zeilen: ' + ', '.join(f'{k} {v}' for k, v in sorted(c.items())))
    if a.liste:
        for i, e, u in erg:
            if u in ('gleich', 'ohne Original'):
                print(f'  {u}: {i} (Original {e})')


if __name__ == '__main__':
    main()

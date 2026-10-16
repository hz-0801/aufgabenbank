#!/usr/bin/env python3
"""loesung-pruef.py – prüft Lösungsfelder auf die Form der Lösung (gemeinsam.md „Form der Lösung“, Lehrer 16.10.).

Meldet je Zeile: SATZ (drei Wörter in Folge ohne Formel), DOPPELT (rechts steht dasselbe wie links),
GERUNDET (≈ ohne exakten Wert davor, obwohl eine Wurzel/ein Bruch im Weg steht), LANG (rechts mehr als
zwei Handgriffe). Felder: Mehr-CSV loesung (Ergebnis | Weg getrennt durch „⇒“/„;“), Katalog kurzloesung
und zwischenergebnis.
  python3 werkzeuge/loesung-pruef.py [--nh ../mathe-nachhilfe] [--nur dreiecke] [--liste]
Rückgabe 1, wenn etwas gemeldet wird."""
import argparse, csv, glob, os, re, sys

WORT = r'[A-Za-zÄÖÜäöüß]{3,}'
SATZ = re.compile(rf'(?<![\\$])\b{WORT}\s+{WORT}\s+{WORT}\b')
ERLAUBT = {'mit', 'und', 'oder'}


def satz(s):
    for m in SATZ.finditer(s or ''):
        w = m.group(0).split()
        if not all(x.lower() in ERLAUBT for x in w[1:]):
            return True
    return False


def norm(s):
    return re.sub(r'\s+', '', s or '').replace('\\', '')


def lies(pfad):
    with open(pfad, encoding='utf-8') as f:
        kopf = f.readline()
    d = ';' if kopf.count(';') > kopf.count(',') else ','
    return list(csv.DictReader(open(pfad, encoding='utf-8'), delimiter=d))


def pruefe(id_, links, rechts, aus):
    m = []
    if satz(links) or satz(rechts):
        m.append('SATZ')
    if rechts and norm(links) and (norm(rechts) == norm(links) or norm(links) in norm(rechts)):
        m.append('DOPPELT')
    if '≈' in links and not re.search(r'[√/]|frac|sqrt|π|pi', links) and re.search(r'√|sqrt|frac|/', rechts or ''):
        m.append('GERUNDET')
    if rechts and len([x for x in re.split(r';|\n', rechts) if x.strip()]) > 2:
        m.append('LANG')
    if m:
        aus.append((id_, m, links[:60], (rechts or '')[:60]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--nh', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'mathe-nachhilfe'))
    ap.add_argument('--nur', default='')
    ap.add_argument('--liste', action='store_true')
    a = ap.parse_args()
    aus = []
    for f in sorted(glob.glob(os.path.join(a.nh, 'msa', 'mehr-p10', '*.csv'))):
        if a.nur and a.nur not in f:
            continue
        for r in lies(f):
            l = r.get('loesung', '')
            teile = re.split(r'\s*⇒\s*', l, maxsplit=1)
            links, rechts = (teile[-1], teile[0]) if len(teile) == 2 else (l, '')
            pruefe(f'{os.path.basename(f)}:{r.get("id","")}', links, rechts, aus)
    if not a.nur:
        for f in sorted(glob.glob(os.path.join(a.nh, 'msa', 'msa-katalog-*.csv'))):
            if 'gym' in f:
                continue
            for r in lies(f):
                pruefe(f'{os.path.basename(f)}:{r.get("id","")}', r.get('kurzloesung', ''), r.get('zwischenergebnis', ''), aus)
    zaehl = {}
    for _, m, _, _ in aus:
        for x in m:
            zaehl[x] = zaehl.get(x, 0) + 1
    print('loesung-pruef:', len(aus), 'Zeilen gemeldet', zaehl)
    if a.liste:
        for i, m, l, r in aus:
            print(f'{i}\t{",".join(m)}\t{l}\t|\t{r}')
    return 1 if aus else 0


if __name__ == '__main__':
    sys.exit(main())

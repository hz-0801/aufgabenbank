#!/usr/bin/env python3
"""loesung-pruef.py – prüft Lösungsfelder auf die Form der Lösung (gemeinsam.md „Form der Lösung“, Lehrer 16.10.).

Meldet je Zeile: SATZ (drei Wörter in Folge ohne Formel), DOPPELT (rechts steht dasselbe wie links),
GERUNDET (≈ ohne exakten Wert davor, obwohl eine Wurzel/ein Bruch im Weg steht), LANG (rechts mehr als
zwei Handgriffe). Felder: Mehr-CSV loesung (Ergebnis | Weg getrennt durch „⇒“/„;“), Katalog kurzloesung
und zwischenergebnis.
  python3 werkzeuge/loesung-pruef.py [--nh ../mathe-nachhilfe] [--nur dreiecke] [--liste]
Rückgabe 1, wenn etwas gemeldet wird."""
import argparse, csv, glob, os, re, sys

OPTION = re.compile(r'\s*\((?:erste|zweite|dritte|vierte)\s+Option[^()]*\)')
WORT = re.compile(r'(?<![\\$\w])[A-Za-zÄÖÜäöüß]{3,}(?![\w])')
# Stichwort-Verbinder trennen eine Folge (Grenze: „viertes oder weiteres Kind“, „einmal pro Woche“ sind Stichwörter);
# Artikel zählen nicht und trennen nicht („Hypotenuse liegt dem rechten Winkel …“ bleibt ein Satz)
TRENNT = {'mit', 'und', 'oder', 'pro', 'je', 'bis', 'von', 'statt', 'bei', 'auf', 'ab', 'als', 'über', 'unter', 'vor', 'nach',
          'zum', 'zur', 'im', 'in', 'aus', 'ohne'}
ARTIKEL = {'der', 'die', 'das', 'dem', 'den', 'des', 'ein', 'eine', 'einen', 'einem', 'einer'}


def satz(s):
    """Satz = drei Inhaltswörter in Folge, nur durch Leerraum getrennt; Zitate „…“ (Wortlaut der Aufgabe) und der
    Vermerk „(… Option)“ zählen nicht."""
    s = OPTION.sub('', re.sub(r'„[^“]*“', ' 0 ', s or ''))
    folge, ende = 0, -1
    for m in WORT.finditer(s):
        w = m.group(0).lower()
        luecke = s[ende:m.start()] if ende >= 0 else ''
        if ende >= 0 and luecke.strip():
            folge = 0
        ende = m.end()
        if w in ARTIKEL:
            continue
        if w in TRENNT:
            folge = 0
            continue
        folge += 1
        if folge >= 3:
            return True
    return False




def mehr_teile(l):
    """Wie der Setzer (pruefheft.py p_ergebnis/p_ausgang, 16.10.): Teile durch „ | “; je Teil steht das Ergebnis
    nach dem letzten „⇒“ (links), davor der Ausgang (rechts, Handgriffe durch „;“); ohne „⇒“ ist der letzte
    Schritt nach „;“ das Ergebnis. Der Vermerk „(dritte Option)“ fällt weg (der Setzer druckt den Wert der Option)."""
    links, rechts = [], []
    for t in [x.strip() for x in re.split(r'\s\|\s', OPTION.sub('', l or '')) if x.strip()]:
        if '⇒' in t:
            v, e = t.rsplit('⇒', 1)
        else:
            st = [x.strip() for x in re.split(r'\s*;\s*', t) if x.strip()]
            v, e = '; '.join(st[:-1]), (st[-1] if st else '')
        links.append(e.strip())
        if v.strip():
            rechts.append(v.strip())
    return ' | '.join(links), '; '.join(rechts)


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
    if rechts and len(norm(links)) >= 3 and (norm(rechts) == norm(links) or norm(links) in norm(rechts)):
        m.append('DOPPELT')
    # gerundet ohne exakten Wert davor: „x ≈ 200,7 cm“, „≈ 28,7 m“ statt „x = √40289 ≈ 200,7 cm“ (16.10.)
    nur_name = any(re.search(r'(?:^|=)\s*(?:[A-Za-zα-ωΑ-Ω][\w₀-₉′]*(?:\([^()]*\))?)?\s*≈', t.strip())
                   for t in links.split('|'))
    if '≈' in links and (nur_name or (not re.search(r'[√/:]|frac|sqrt|π|pi|⁻¹', links)
                                      and re.search(r'√|sqrt|frac|/', rechts or ''))):
        m.append('GERUNDET')
    if rechts and len([x for x in re.split(r';|⇒|\n', rechts) if x.strip()]) > 3:
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
            links, rechts = mehr_teile(r.get('loesung', ''))
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

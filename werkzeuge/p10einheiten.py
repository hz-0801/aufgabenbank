#!/usr/bin/env python3
"""p10einheiten.py – die P10-Einheiten (Blätter) in Lernfolge, aus den Gliederungen, ohne Liste im Skript.

Anlass: plan.md § 7 (14.10., Schritt 2): Bestellkarte, Gesamtheft und Mappe lesen Folge und Ordner aus den
Daten. Quelle: mathe-nachhilfe msa/gliederung/*.md, Kopfzeilen
  Kennung: <Zuschnitt> = PG50      sprechende Kennung (plan.md § 10, 14.10. b): Sorte · Gebiet · Platz
  Ordner: <Zuschnitt> = pythagoras Ausgabeordner unter bau/pruefung/<datum>/
  Anzeigenamen: <Zuschnitt> = Pythagoras
Folge: Gebiete in der Folge ihres ersten Kapitels (Feld Folge), darin nach dem Platz der Kennung
(Lernfolge mit Zehnerlücken, über Kapitelgrenzen). Gebietsname aus „Gebiet:“, „+“ als „und“.

  from p10einheiten import einheiten   ->  [dict(gebiet, kapitel, kapitelname, einheit, anzeige, kennung,
                                              ordner, folge, stufen=[(name, anzeige)])]
"""
import glob
import os
import re

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MN_VORGABE = os.environ.get('MATHE_NACHHILFE') or os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe')


def _kopf(t):
    kopf = t.split('\n## ')[0]
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', kopf, re.M) or [None, ''])[1].strip()
    paare = lambda k: {a.strip(): b.strip() for z in re.findall(rf'^{k}:\s*(.+)$', kopf, re.M)
                       for teil in z.split('|') if '=' in teil for a, b in [teil.rsplit('=', 1)]}
    return g, paare


def _stufen(t):
    """Stufen der Gliederung mit Zuschnitt und Anzeigename, in Lernreihenfolge."""
    out = []
    a = t.find('\n## Stufen')
    if a < 0:
        return out
    teil = t[a + 1:]
    e = teil.find('\n## ', 3)
    teil = teil if e < 0 else teil[:e]
    for b in re.split(r'^(?=### )', teil, flags=re.M)[1:]:
        name = b.splitlines()[0][4:].strip()
        zu = re.search(r'^- \*\*Zuschnitt:\*\*\s*(.*)$', b, re.M)
        an = re.search(r'^- \*\*Anzeigename:\*\*\s*(.*)$', b, re.M)
        out.append((name, (zu.group(1).strip() if zu else ''), (an.group(1).strip() if an else name)))
    return out


def einheiten(mn=MN_VORGABE):
    eins, kap_folge = [], {}
    for f in sorted(glob.glob(os.path.join(mn, 'msa', 'gliederung', '*.md'))):
        if os.path.basename(f).lower() == 'readme.md':
            continue
        t = open(f, encoding='utf-8').read()
        g, paare = _kopf(t)
        kenn, ordner, anz = paare('Kennung'), paare('Ordner'), paare('Anzeigenamen')
        if not kenn:
            continue
        gebiet = g('Gebiet').replace(' + ', ' und ')
        folge = int(re.sub(r'\D', '', g('Folge')) or 99)
        kap_folge[gebiet] = min(kap_folge.get(gebiet, 99), folge)
        st = _stufen(t)
        for ein, k in kenn.items():
            if ein not in ordner:
                raise SystemExit(f'{os.path.basename(f)}: Feld „Ordner: {ein} = …“ fehlt')
            m = re.fullmatch(r'([PALFS]\d*)([GASZB])(\d{2,3})', k)
            if not m:
                raise SystemExit(f'{os.path.basename(f)}: Kennung „{k}“ verletzt das Muster (PG50)')
            eins.append(dict(gebiet=gebiet, kapitel=g('Kapitel'), kapitelname=g('Name'), einheit=ein,
                             anzeige=anz.get(ein, ein), kennung=k, ordner=ordner[ein], platz=int(m.group(3)),
                             kapitelfolge=folge,
                             stufen=[(n, a) for n, z, a in st if z == ein]))
    eins.sort(key=lambda e: (kap_folge[e['gebiet']], e['platz']))
    gebiete = []
    for e in eins:
        if e['gebiet'] not in gebiete:
            gebiete.append(e['gebiet'])
    for i, e in enumerate(eins):
        e['folge'] = i + 1
    return eins


def gebiete(eins):
    out = []
    for e in eins:
        if e['gebiet'] not in out:
            out.append(e['gebiet'])
    return out


if __name__ == '__main__':
    for e in einheiten():
        print(e['folge'], e['kennung'], e['gebiet'], '|', e['kapitel'], '|', e['einheit'], '->', e['ordner'],
              '|', ' · '.join(a for _, a in e['stufen']))

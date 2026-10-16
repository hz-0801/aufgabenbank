#!/usr/bin/env python3
"""regel-pruef.py – prüft je P10-Einheit die Pflichtteile eines P10-Blatts (mathe-nachhilfe pruefung.md § 5
„Pflichtteile eines P10-Blatts“, 16.10. n), soweit maschinell prüfbar. Liest nur.

Daten (Kopf von msa/gliederung/<kapitel>.md, alle Gebiete):
  1 Tafelwerk   genau eins von „Formelkasten: <Einheit> = <kasten-id>“ (id in aufgabenbank-privat
                formelsammlung/duden-sek1.json), „Formelsammlung: <Einheit> = <Zeile>“, „Tafelwerk: <Einheit> = keins –
                <Grund>“
  2 Kern        „Kern am Ende: <Einheit> = a | b | …“ mit 1–4 Aussagen
  3 Begriff     „- **Begriff:**“ einer Stufe der Einheit steht wortgleich im Kern
Gesetzt (mit --datum, Ordner bau/pruefung/<datum>/<ordner>/):
  1 Tafelwerk   kein „Schlag zuerst die Formel“ im Blatt
  4 Mehr        kein Blatt mit 1 Seite plus eigenem Mehr, das zusammen auf 2 Seiten passt
  5 Abschnitte  Stufenzeile ohne Buchstaben
  6 Lösung      loesung-pruef.py (je Kapitel) meldet nichts
Ausgabe: je Meldung „<Kennung> <Regel>: <was>“, am Ende „regel-pruef: n Meldungen“. Rückgabe 1 bei Meldungen.
  python3 werkzeuge/regel-pruef.py [--datum 2026-10-16] [--nur gleichungssysteme,dreiecke] [--ohne-loesung]
Anlass: plan.md § 10 16.10. n (der Setzer ließ fehlende Felder still weg)."""
import argparse
import json
import os
import re
import subprocess
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
from p10einheiten import einheiten, MN_VORGABE  # noqa: E402

PRIVAT = os.environ.get('PRIVAT') or os.path.join(os.path.dirname(BANK), 'aufgabenbank-privat')
TAFEL = ('Formelkasten', 'Formelsammlung', 'Tafelwerk')


def kopf_felder(pfad):
    """Kopfzeilen „<Feld>: <Einheit> = <Wert>“ vor „## “ -> {(Feld, Einheit): [Werte]}."""
    out = {}
    for z in open(pfad, encoding='utf-8').read().split('\n## ')[0].splitlines():
        m = re.match(r'^(Formelkasten|Formelsammlung|Tafelwerk|Kern am Ende):\s*(.*?)\s+=\s+(.*)$', z)
        if m:
            out.setdefault((m.group(1), m.group(2).strip()), []).append(m.group(3).strip())
    return out


def begriffe(pfad, stufen):
    """Begriff je Stufe der Einheit (Zeile „- **Begriff:**“, Fortsetzungszeilen eingerückt)."""
    t = open(pfad, encoding='utf-8').read()
    out = {}
    for b in re.split(r'^(?=### )', t, flags=re.M)[1:]:
        name = b.splitlines()[0][4:].strip()
        if name not in stufen:
            continue
        m = re.search(r'^- \*\*Begriff:\*\*\s*(.*(?:\n(?!- |\n|#).*)*)', b, re.M)
        if m:
            out[name] = re.sub(r'\s+', ' ', m.group(1)).strip()
    return out


def norm(s):
    return re.sub(r'[\s.;,:]+', ' ', s or '').strip().lower()


def seiten(pdf):
    r = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True)
    m = re.search(r'Pages:\s+(\d+)', r.stdout)
    return int(m.group(1)) if m else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mn', default=MN_VORGABE)
    ap.add_argument('--datum', default='')
    ap.add_argument('--nur', default='', help='Kapitel oder Ordner, durch Komma getrennt')
    ap.add_argument('--ohne-loesung', action='store_true', help='loesung-pruef.py nicht aufrufen')
    a = ap.parse_args()
    nur = {x for x in a.nur.split(',') if x}
    js = os.path.join(PRIVAT, 'formelsammlung', 'duden-sek1.json')
    kaesten = {e['id'] for e in json.load(open(js, encoding='utf-8'))['eintraege']} if os.path.exists(js) else None
    meld = []
    m = lambda k, regel, was: meld.append(f'{k} {regel}: {was}')
    if kaesten is None:
        m('–', '1 Tafelwerk', f'{js} fehlt – Kasten-ids nicht geprüft')
    kapitel = []
    for e in einheiten(a.mn):
        if nur and e['kapitel'] not in nur and e['ordner'] not in nur:
            continue
        if e['kapitel'] not in kapitel:
            kapitel.append(e['kapitel'])
        k, ein = e['kennung'], e['einheit']
        pf = os.path.join(a.mn, 'msa', 'gliederung', e['kapitel'] + '.md')
        f = kopf_felder(pf)
        # 1 Tafelwerk-Feld
        da = [(t, w) for t in TAFEL for w in f.get((t, ein), [])]
        if len(da) != 1:
            m(k, '1 Tafelwerk', f'{len(da)} Felder statt genau eins (Formelkasten | Formelsammlung | Tafelwerk: keins – '
                                f'Grund)' + (' – ' + ', '.join(t for t, _ in da) if da else ''))
        for t, w in da:
            if t == 'Formelkasten' and kaesten is not None and w not in kaesten:
                m(k, '1 Tafelwerk', f'Formelkasten „{w}“ nicht in formelsammlung/duden-sek1.json')
            if t == 'Tafelwerk' and not re.match(r'^keins\s*[–-]\s*\S', w):
                m(k, '1 Tafelwerk', f'„Tafelwerk: … = {w}“ – erwartet „keins – <Grund>“')
            if t == 'Formelsammlung' and not re.search(r'S\.\s*\d', w):
                m(k, '1 Tafelwerk', f'Formelsammlungs-Zeile ohne Seite („S. 15“): {w[:50]}')
        # 2 Kern am Ende
        kern = f.get(('Kern am Ende', ein), [])
        aussagen = [x for x in (re.split(r'\|(?![^()]*\))', kern[0]) if kern else []) if x.strip()]
        if len(kern) != 1:
            m(k, '2 Kern', f'{len(kern)} Zeilen „Kern am Ende: {ein} = …“ statt einer')
        elif not 1 <= len(aussagen) <= 4:
            m(k, '2 Kern', f'{len(aussagen)} Aussagen statt 1–4')
        # 3 Begriff wortgleich im Kern
        for st, b in begriffe(pf, {n for n, _ in e['stufen']}).items():
            if kern and norm(b) not in norm(kern[0]):
                m(k, '3 Begriff', f'Begriff der Stufe „{st}“ steht nicht wortgleich im Kern: „{b[:50]}…“')
        if not a.datum:
            continue
        o = os.path.join(BANK, 'bau', 'pruefung', a.datum, e['ordner'])
        tex = os.path.join(o, 'src', '2-blatt.tex')
        if not os.path.exists(tex):
            m(k, '0 Satz', f'kein Blatt unter bau/pruefung/{a.datum}/{e["ordner"]} (nicht gesetzt)')
            continue
        t = open(tex, encoding='utf-8').read()
        if 'Schlag zuerst die Formel' in t:
            m(k, '1 Tafelwerk', '„Schlag zuerst die Formel nach“ im Blatt')
        sz = re.search(r'\\pfstufenzeile\{(.*)\}', t)
        if sz and re.search(r'(?:^|\\pkt\{\} )[A-J]~', sz.group(1)):
            m(k, '5 Abschnitte', 'Buchstaben in der Stufenzeile')
        pdf = os.path.join(o, 'pdf', '2-blatt.pdf')
        mehr = os.path.join(o, 'pdf', '4-mehr.pdf')
        if not os.path.exists(mehr):
            mehr = os.path.join(o, 'mehr', 'pdf', 'mehr.pdf')
        if os.path.exists(pdf) and os.path.exists(mehr):
            sb, sm = seiten(pdf), seiten(mehr)
            if sb == 1 and sb + sm <= 2:
                m(k, '4 Mehr', f'Blatt 1 Seite plus eigenes Mehr ({sm} Seite) – passt zusammen auf 2 Seiten')
    if not a.ohne_loesung:
        for kap in kapitel:
            r = subprocess.run([sys.executable, os.path.join(HIER, 'loesung-pruef.py'), '--nh', a.mn, '--nur', kap,
                                '--liste'], capture_output=True, text=True)
            kenn = ' '.join(e['kennung'] for e in einheiten(a.mn) if e['kapitel'] == kap)
            for z in r.stdout.splitlines():
                if '\t' in z:
                    teile = z.split('\t')
                    m(kenn, '6 Lösung', f'{teile[0]} {teile[1]}: {teile[2][:40]} | {teile[-1][:40]}')
            if r.returncode not in (0, 1):
                m(kenn, '6 Lösung', 'loesung-pruef.py lief nicht: ' + r.stderr.strip()[-120:])
    for z in meld:
        print(z)
    print(f'regel-pruef: {len(meld)} Meldungen')
    return 1 if meld else 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Bestellkarte P10 je Gebiet (eine Seite), aus den gesetzten Blättern, ohne Modell.

Anlass: Lehrer 14.10. – je Gebiet eine Seite; Abschnitte eingerückt
unter dem Namen ihres Blatts, untereinander; Kästchen nur an Abschnitten, keine Kennung,
keine Seitenangaben; was sich lohnt; kein
erklärender Text. Liest Titel und Stufenköpfe (mit Jahren) aus
bau/pruefung/<datum>/<ordner>/src/2-blatt.tex.

Probe: python3 werkzeuge/bestellkarte.py --datum 2026-10-14 --gebiet Geometrie
"""
import argparse, os, re, shutil, subprocess, tempfile

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JUNG = [2026, 2025, 2024, 2023, 2022]

# Folge = Lernfolge (pruefung.md § 2 „Lernfolge“, Lehrer 11.10.): wer ein Blatt braucht, hat das vorige gehabt.
GEBIETE = [
    ('Geometrie', ['winkel', 'symmetrie', 'vierecke', 'flaechen', 'pythagoras', 'sin-cos-tan',
                   'sinussatz', 'koerper-netz', 'koerper-volumen']),
    ('Funktionen', ['lineare', 'parabel', 'qgleichung', 'gleichungssysteme', 'wachstum']),
    ('Daten und Zufall', ['prozent', 'grundwert', 'kenngroessen', 'diagramme', 'wahrscheinlichkeit']),
]


def gruppe(t, i):
    """Inhalt der geschweiften Klammer ab Index i (t[i] == '{'), mit Schachtelung."""
    tiefe = 0
    for j in range(i, len(t)):
        tiefe += {'{': 1, '}': -1}.get(t[j], 0)
        if tiefe == 0:
            return t[i + 1:j], j + 1
    return t[i + 1:], len(t)


def blatt(ordner):
    t = open(os.path.join(ordner, 'src', '2-blatt.tex'), encoding='utf-8').read()
    m = re.search(r'\\pflaufkopf\[[^]]*\]', t)
    titel, _ = gruppe(t, m.end())
    stufen, i = [], 0
    while (i := t.find('\\pfstufekopf{', i)) >= 0:
        name, k = gruppe(t, i + len('\\pfstufekopf'))
        jahre, i = gruppe(t, k)
        if jahre.startswith('\\pfjahre'):
            jung, _ = gruppe(jahre, len('\\pfjahre'))
            j = {2000 + int(x) for x in re.findall(r'\b\d\d\b', jung)}
            stufen.append((name, None, j))
        else:
            stufen.append((name, jahre.strip(), set()))
    pdf = os.path.join(ordner, 'pdf', '2-blatt.pdf')
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    return titel, stufen, n


KASTEN = r'\raisebox{-.15ex}{\framebox[1.8ex]{\rule{0pt}{1.1ex}}}'


def lohnt(wort, jahre):
    if wort:
        return r'\textbf{%s}' % wort
    return r'\,'.join(r'\textcolor{black!80}{$\bullet$}' if j in jahre else r'\textcolor{black!25}{$\circ$}'
                      for j in JUNG)


def seite(gebiet, eintraege):
    z = []
    for e in eintraege:
        z.append(r'\rule{0pt}{3.6ex}\hyperlink{%s.1}{\large\bfseries %s} & \\' % (e['ordner'], e['titel']))
        for name, wort, jahre in e['stufen']:
            z.append(r'\hspace*{1.2em}%s\enspace %s & %s\\' % (KASTEN, name, lohnt(wort, jahre)))
    return (r'{\LARGE\bfseries %s}\par\vspace{1ex}' % gebiet
            + r'\begin{tabular}{@{}p{0.7\textwidth}l@{}}'
            + '\n'.join(z) + r'\end{tabular}\clearpage')


PRAEAMBEL = r'''\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage[margin=18mm,top=16mm]{geometry}
\usepackage{xcolor}\usepackage{array}\usepackage[hidelinks]{hyperref}
\renewcommand{\familydefault}{\sfdefault}\pagestyle{empty}\setlength{\tabcolsep}{5pt}\renewcommand{\arraystretch}{1.18}
'''


def eintraege(ziel, ab_start):
    out, ab = [], ab_start
    for gebiet, ordner in GEBIETE:
        for o in ordner:
            titel, stufen, n = blatt(os.path.join(ziel, o))
            out.append(dict(gebiet=gebiet, ordner=o, titel=titel, stufen=stufen, n=n, ab=ab))
            ab += n
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--datum', required=True)
    ap.add_argument('--gebiet', help='nur dieses Gebiet (Probe)')
    a = ap.parse_args()
    ziel = os.path.join(BANK, 'bau', 'pruefung', a.datum)
    E = eintraege(ziel, len(GEBIETE) + 1)
    seiten = [seite(g, [e for e in E if e['gebiet'] == g]) for g, _ in GEBIETE if not a.gebiet or g == a.gebiet]
    tmp = tempfile.mkdtemp()
    open(os.path.join(tmp, 'k.tex'), 'w', encoding='utf-8').write(
        PRAEAMBEL + r'\begin{document}' + '\n'.join(seiten) + r'\end{document}')
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'k.tex'], cwd=tmp, capture_output=True, text=True)
    if not os.path.exists(os.path.join(tmp, 'k.pdf')):
        raise SystemExit(r.stdout[-2000:])
    aus = os.path.join(ziel, 'bestellkarte' + ('-' + a.gebiet.lower() if a.gebiet else '') + '.pdf')
    shutil.copy(os.path.join(tmp, 'k.pdf'), aus)
    print(aus)


if __name__ == '__main__':
    main()

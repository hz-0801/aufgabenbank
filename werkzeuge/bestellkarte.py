#!/usr/bin/env python3
"""Bestellkarte P10 je Gebiet (eine Seite), aus den gesetzten Blättern, ohne Modell.

Anlass: Lehrer 14.10. – je Gebiet eine Seite; Abschnitte eingerückt
unter dem Namen ihres Blatts, untereinander; Kästchen nur an Abschnitten, keine Kennung,
keine Seitenangaben; was sich lohnt; kein
erklärender Text. Liest Titel und Stufenköpfe (mit Jahren) aus
bau/pruefung/<datum>/<ordner>/src/2-blatt.tex.

Probe: python3 werkzeuge/bestellkarte.py --datum 2026-10-14 --gebiet Geometrie
Seit 14.10. (plan.md § 7 Schritt 2): Folge, Gebiete und Ordner aus den Gliederungen (werkzeuge/p10einheiten.py,
Felder Kennung und Ordner), keine Liste im Skript; Stufenkopf liest \\gpunkte[Jahre] bzw. \\gzuletzt (Setzer v0.14).
--handreichung: Muster Handreichung (plan.md § 10, 14.10. h) – alle Stufen der Gliederung; Stufen, die nicht auf
einem Blatt stehen, grau mit „nicht geprüft seit JJ“ bzw. „nie geprüft“; eigene Datei handreichung-muster.pdf.
"""
import argparse, os, re, shutil, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p10einheiten import einheiten as p10_einheiten, gebiete as p10_gebiete, MN_VORGABE  # noqa: E402

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JUNG = [2026, 2025, 2024, 2023, 2022]

# Folge = Lernfolge (pruefung.md § 2 „Lernfolge“, Lehrer 11.10.): aus den Gliederungen (Platz der Kennung).


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
        m = re.match(r'\\gpunkte\[([^\]]*)\]', jahre)
        if m:
            stufen.append((name, None, {2000 + int(x) for x in m.group(1).split()}))
        elif jahre.startswith('\\gzuletzt'):
            stufen.append((name, 'zuletzt ' + gruppe(jahre, len('\\gzuletzt'))[0], set()))
        else:
            stufen.append((name, jahre.strip(), set()))
    pdf = os.path.join(ordner, 'pdf', '2-blatt.pdf')
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    return titel, stufen, n


KASTEN = r'\raisebox{-.15ex}{\framebox[1.8ex]{\rule{0pt}{1.1ex}}}'


def lohnt(wort, jahre):
    if wort:
        return r'{\small\color{black!55}%s}' % wort
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


def eintraege(ziel, ab_start, mn=MN_VORGABE):
    out, ab = [], ab_start
    for e in p10_einheiten(mn):
        titel, stufen, n = blatt(os.path.join(ziel, e['ordner']))
        out.append(dict(gebiet=e['gebiet'], ordner=e['ordner'], titel=titel, stufen=stufen, n=n, ab=ab,
                        einheit=e))
        ab += n
    return out


def letzte_jahre(mn, kapitel):
    """Stufe -> Jahre, in denen ihr Handgriff in einem P10-Heft verlangt wurde (werkzeuge/p10punkte.py: Hauptplatz,
    ganz auch, Zwischenschritt; dieselbe Quelle wie der Stufenkopf der Blätter, plan.md § 10, 15.10. i)."""
    sys.path.insert(0, os.path.join(mn, 'werkzeuge'))
    import gliederung as GL
    from p10punkte import jahre
    G = GL.lies(os.path.join(mn, 'msa', 'gliederung', kapitel + '.md'))
    return {s['name']: jahre(kapitel, s['name'], mn) for s in G['stufen']}


GRAU = r'\textcolor{black!45}'


def grau_wort(j):
    """Rechte Spalte einer Stufe ohne Platz auf dem Blatt: Punkte, wenn ihr Handgriff in den letzten fünf Jahren
    verlangt wurde (nur als Zwischenschritt oder ganz auch), sonst „nicht geprüft seit JJ“ bzw. „nie geprüft“."""
    if j & set(JUNG):
        return lohnt(None, j).replace('black!80', 'black!45')
    return r'%s{\small %s}' % (GRAU, ('nicht geprüft seit %02d' % (max(j) % 100)) if j else 'nie geprüft')


def handreichung_seite(gebiet, eintraege, mn):
    """Alle Stufen der Gliederung unter ihrem Blatt; Stufen ohne Platz auf dem Blatt grau mit „nicht geprüft seit
    JJ“ bzw. „nie geprüft“ (Stufen ohne Original in den letzten fünf Jahren stehen schon auf dem Blatt mit
    „zuletzt JJ“)."""
    z = []
    for e in eintraege:
        z.append(r'\rule{0pt}{3.6ex}\hyperlink{%s.1}{\large\bfseries %s} & \\' % (e['ordner'], e['titel']))
        J = letzte_jahre(mn, e['einheit']['kapitel'])
        for (name, anz) in e['einheit']['stufen']:
            treffer = next((s for s in e['stufen'] if s[0] == anz), None)
            if treffer:
                z.append(r'\hspace*{1.2em}%s\enspace %s & %s\\' % (KASTEN, anz, lohnt(treffer[1], treffer[2])))
                continue
            z.append(r'\hspace*{1.2em}%s{%s\enspace %s} & %s\\' % (GRAU, KASTEN, anz, grau_wort(J.get(name, set()))))
    # Stufen der Gliederung ohne Blatt (kein Zuschnitt, z. B. Zinsen): grau unter „ohne Blatt“
    sys.path.insert(0, os.path.join(mn, 'werkzeuge'))
    import gliederung as GL
    ohne = []
    for kap in dict.fromkeys(e['einheit']['kapitel'] for e in eintraege):
        G = GL.lies(os.path.join(mn, 'msa', 'gliederung', kap + '.md'))
        for s in G['stufen']:
            if not s['abschnitt']:
                ohne.append(r'\hspace*{1.2em}%s{%s\enspace %s} & %s\\'
                            % (GRAU, KASTEN, s['felder'].get('Anzeigename') or s['name'],
                               grau_wort(letzte_jahre(mn, kap)[s['name']])))
    if ohne:
        z.append(r'\rule{0pt}{3.6ex}%s{\large\bfseries ohne Blatt} & \\' % GRAU)
        z += ohne
    return (r'{\LARGE\bfseries %s}\par\vspace{1ex}' % gebiet
            + r'\begin{tabular}{@{}p{0.66\textwidth}l@{}}'
            + '\n'.join(z) + r'\end{tabular}\clearpage')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--datum', required=True)
    ap.add_argument('--gebiet', help='nur dieses Gebiet (Probe)')
    ap.add_argument('--mn', default=MN_VORGABE)
    ap.add_argument('--handreichung', action='store_true', help='Muster Handreichung: alle Stufen der Gliederung')
    a = ap.parse_args()
    ziel = os.path.join(BANK, 'bau', 'pruefung', a.datum)
    GEB = p10_gebiete(p10_einheiten(a.mn))
    E = eintraege(ziel, len(GEB) + 1, a.mn)
    if a.handreichung:
        seiten = [handreichung_seite(g, [e for e in E if e['gebiet'] == g], a.mn) for g in GEB]
    else:
        seiten = [seite(g, [e for e in E if e['gebiet'] == g]) for g in GEB if not a.gebiet or g == a.gebiet]
    tmp = tempfile.mkdtemp()
    open(os.path.join(tmp, 'k.tex'), 'w', encoding='utf-8').write(
        PRAEAMBEL + r'\begin{document}' + '\n'.join(seiten) + r'\end{document}')
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'k.tex'], cwd=tmp, capture_output=True, text=True)
    if not os.path.exists(os.path.join(tmp, 'k.pdf')):
        raise SystemExit(r.stdout[-2000:])
    aus = os.path.join(ziel, 'handreichung-muster.pdf' if a.handreichung else
                       'bestellkarte' + ('-' + a.gebiet.lower() if a.gebiet else '') + '.pdf')
    shutil.copy(os.path.join(tmp, 'k.pdf'), aus)
    print(aus)


if __name__ == '__main__':
    main()

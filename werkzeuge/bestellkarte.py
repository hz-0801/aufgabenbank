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
--pruefung abi-gk (15.10.2026): Abitur GK aus mathe-nachhilfe abitur/gliederung (werkzeuge/p10einheiten.py
abi_einheiten), ohne gesetzte Blätter: Blattname, Kennung, Stufen mit fünf Punkten (2026 … 2022: Jahre der
Teilaufgaben der Stufe, Hauptplatz und neben, GK BB/BE); Handreichung dazu je Stufe die Fundstellen.
Ausgabe bau/pruefung/<datum>/abitur/bestellkarte-abi-gk.pdf bzw. handreichung-abi-gk.pdf. P10 unverändert.
  python3 werkzeuge/bestellkarte.py --datum 2026-10-15 --pruefung abi-gk [--handreichung]
"""
import argparse, os, re, shutil, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p10einheiten import einheiten as p10_einheiten, gebiete as p10_gebiete, abi_einheiten, MN_VORGABE  # noqa: E402
from sprungziele import slug  # noqa: E402

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


def kopfzeile(e):
    """Blattname (springt zum Blatt), dahinter die Kennung klein grau (plan.md § 10, 15.10. k)."""
    return (r'\rule{0pt}{3.6ex}\hyperlink{%s.1}{\large\bfseries %s}\enspace{\small\color{black!45}%s} & \\'
            % (e['ordner'], e['titel'], e['einheit']['kennung']))


def abschnitt(e, name):
    """Abschnitt springt zu seinem Stufenkopf im Blatt („<ordner>@<slug>“, aufgelöst von sprungziele.py)."""
    return r'\hyperlink{%s@%s}{%s}' % (e['ordner'], slug(name), name)


def seite(gebiet, eintraege):
    z = []
    for e in eintraege:
        z.append(kopfzeile(e))
        for name, wort, jahre in e['stufen']:
            z.append(r'\hspace*{1.2em}%s\enspace %s & %s\\' % (KASTEN, abschnitt(e, name), lohnt(wort, jahre)))
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
        z.append(kopfzeile(e))
        J = letzte_jahre(mn, e['einheit']['kapitel'])
        for (name, anz) in e['einheit']['stufen']:
            treffer = next((s for s in e['stufen'] if s[0] == anz), None)
            if treffer:
                z.append(r'\hspace*{1.2em}%s\enspace %s & %s\\' % (KASTEN, abschnitt(e, anz), lohnt(treffer[1], treffer[2])))
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


def abi_jahre(ids):
    return {int(i[:4]) for i in ids if re.match(r'\d{4}-', i)}


def abi_fundstellen(ids, neben):
    """„’26 B2.2g · ’25 A1.4a“, Nebenplätze mit „(auch)“; jüngste zuerst."""
    f = lambda i: '’%s %s' % (i[2:4], i.split('-gk-')[-1])
    return ' · '.join([f(i) for i in sorted(ids, reverse=True)] + [f(i) + ' (auch)' for i in sorted(neben, reverse=True)])


def abi_tex(s):
    return s.replace('′', "$'$")


def abi_seite(gebiet, eins, hand=False):
    """Eine Seite je Gebiet, zweispaltig (Analysis hat 16 Blätter); je Blatt ein ungeteilter Block."""
    bl = []
    for e in eins:
        z = [r'\multicolumn{2}{@{}l@{}}{\rule{0pt}{3ex}{\bfseries %s}\enspace{\footnotesize\color{black!45}%s}}\\'
             % (abi_tex(e['anzeige']), e['kennung'])]
        for name, _ in e['stufen']:
            ids, neben = e['ids'][name]
            z.append(r'\hspace*{1em}%s\enspace{\small %s} & %s\\' % (KASTEN, abi_tex(name), lohnt(None, abi_jahre(ids + neben))))
            if hand:
                z.append(r'\multicolumn{2}{@{}l@{}}{\hspace*{2.6em}{\scriptsize\color{black!50}%s}}\\'
                         % abi_fundstellen(ids, neben))
        bl.append(r'\begin{tabular}{@{}>{\raggedright\arraybackslash\hangindent=2.5em\hangafter=1}p{0.385\textwidth}@{\hspace{0.6em}}l@{}}' + '\n'.join(z) + r'\end{tabular}\par')
    return (r'{\LARGE\bfseries %s}\par\vspace{1ex}\begin{multicols}{2}\raggedcolumns ' % gebiet
            + '\n'.join(bl) + r'\end{multicols}\clearpage')


def abi_main(a):
    ziel = os.path.join(BANK, 'bau', 'pruefung', a.datum, 'abitur')
    os.makedirs(ziel, exist_ok=True)
    E = abi_einheiten(a.mn)
    GEB = p10_gebiete(E)
    seiten = [abi_seite(g, [e for e in E if e['gebiet'] == g], a.handreichung) for g in GEB
              if not a.gebiet or g == a.gebiet]
    praeambel = PRAEAMBEL.replace('12pt', '11pt') + r'\usepackage{multicol}\setlength{\columnsep}{8mm}' + (
        r'\renewcommand{\arraystretch}{1.05}' if a.handreichung else '')
    tmp = tempfile.mkdtemp()
    open(os.path.join(tmp, 'k.tex'), 'w', encoding='utf-8').write(
        praeambel + r'\begin{document}' + '\n'.join(seiten) + r'\end{document}')
    r = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'k.tex'], cwd=tmp, capture_output=True, text=True, errors='replace')
    if not os.path.exists(os.path.join(tmp, 'k.pdf')):
        raise SystemExit(r.stdout[-2000:])
    aus = os.path.join(ziel, ('handreichung' if a.handreichung else 'bestellkarte') + '-abi-gk.pdf')
    shutil.copy(os.path.join(tmp, 'k.pdf'), aus)
    print(aus)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--datum', required=True)
    ap.add_argument('--gebiet', help='nur dieses Gebiet (Probe)')
    ap.add_argument('--mn', default=MN_VORGABE)
    ap.add_argument('--handreichung', action='store_true', help='Muster Handreichung: alle Stufen der Gliederung')
    ap.add_argument('--pruefung', default='p10', choices=['p10', 'abi-gk'], help='Prüfung (Vorgabe p10)')
    a = ap.parse_args()
    if a.pruefung == 'abi-gk':
        return abi_main(a)
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

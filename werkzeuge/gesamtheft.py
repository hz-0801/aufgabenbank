#!/usr/bin/env python3
"""Gesamtheft aller P10-Blätter eines Datumsordners, ohne Modell.

Anlass: plan.md § 7 Schritt 1 (Lehrer 13.10. g, 14.10.: ohne Lösungen –
die bleiben bei den Einheiten). Setzt nichts neu, fügt nur zusammen:
Bestellkarte mit Inhalt (Gebiet, Kapitel, Einheit, Stufen, Kennung,
Seite – jede Zeile springt zum Blatt), dann alle Blätter (2-blatt.pdf)
in der Folge der Gliederung; auf jeder Blattseite oben rechts ein
Sprung zurück zur Karte; Lesezeichen je Kapitel und Blatt.

Aufruf (aus aufgabenbank):
  python3 werkzeuge/gesamtheft.py --datum 2026-10-14 [--markiert grundwert,kenngroessen]
Eingaben: bau/pruefung/<datum>/<ordner>/pdf/2-blatt.pdf,
mathe-nachhilfe msa/skript-zuschnitt-p10.csv (Stufen),
msa/gliederung/*.md (Folge, Ordner, Stufen: werkzeuge/p10einheiten.py, seit 14.10. keine Liste im Skript),
Kennung mit Fassung aus src/2-blatt.tex.
Ausgabe: bau/pruefung/<datum>/gesamtheft-p10.pdf
"""
import argparse, csv, glob, os, re, shutil, subprocess, sys, tempfile

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p10einheiten import einheiten as p10_einheiten  # noqa: E402  Folge und Ordner aus den Gliederungen (14.10.)
from sprungziele import slug, stufenziele, feste_ziele, pruefe  # noqa: E402


def tex(s):
    for a, b in [('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'),
                 ('$', r'\$'), ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}')]:
        s = s.replace(a, b)
    return s


def kopf(mn):
    """Kapitel-Schlüssel -> (Folge, Name, Gebiet) aus den Gliederungen."""
    out = {}
    for f in glob.glob(os.path.join(mn, 'msa', 'gliederung', '*.md')):
        t = open(f, encoding='utf-8').read()
        g = lambda k: (re.search(rf'^{k}:\s*(.+)$', t, re.M) or [None, ''])[1].strip()
        if g('Kapitel'):
            out[g('Kapitel')] = (int(g('Folge') or 99), g('Name'), g('Gebiet'))
    return out


def stufen(mn):
    """(Kapitelname, Abschnitt) -> Stufen in Folge, aus skript-zuschnitt-p10.csv."""
    out = {}
    with open(os.path.join(mn, 'msa', 'skript-zuschnitt-p10.csv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter=';'):
            l = out.setdefault((r['kapitel'], r['abschnitt']), [])
            if r['stufe'] not in l:
                l.append(r['stufe'])
    return out


def kennung(ordner):
    """Kennung mit Fassung, wie sie im Kopf des Blatts steht (\\pflaufkopf)."""
    t = open(os.path.join(ordner, 'src', '2-blatt.tex'), encoding='utf-8').read()
    m = re.search(r'\\pflaufkopf\[[^]]*\]\{[^}]*\}\{([^}]*)\}', t)
    return m.group(1) if m else '–'


def seiten(pdf):
    o = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', o).group(1))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--datum', required=True)
    ap.add_argument('--mn', default=os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe'))
    ap.add_argument('--markiert', default='', help='Ordner, die in der Karte als neu markiert werden')
    a = ap.parse_args()
    ziel = os.path.join(BANK, 'bau', 'pruefung', a.datum)
    neu = {x for x in a.markiert.split(',') if x}

    eintraege, fehlt = [], []
    for e in p10_einheiten(a.mn):
        pdf = os.path.join(ziel, e['ordner'], 'pdf', '2-blatt.pdf')
        if not os.path.exists(pdf):
            fehlt.append(e['ordner'])
            continue
        eintraege.append(dict(kap=e['kapitel'], name=e['kapitelname'], gebiet=e['gebiet'], ein=e['anzeige'],
                              ordner=e['ordner'], pdf=pdf, n=seiten(pdf),
                              kennung=kennung(os.path.join(ziel, e['ordner'])),
                              stufen=[s for _, s in e['stufen']], ziele=stufenziele(pdf)))
    if fehlt:
        raise SystemExit('Blatt fehlt: ' + ', '.join(fehlt))

    karte_seiten = 2  # Schätzung für die Seitenzahlen; wird nach dem ersten Lauf geprüft
    tmp = tempfile.mkdtemp()
    for e in eintraege:
        shutil.copy(e['pdf'], os.path.join(tmp, e['ordner'] + '.pdf'))

    def dokument(karte_seiten):
        z, seite = [], karte_seiten + 1
        for e in eintraege:
            e['ab'] = seite
            seite += e['n']
        zeilen, gebiet, kapitel = [], None, None
        for e in eintraege:
            if e['gebiet'] != gebiet:
                gebiet = e['gebiet']
                zeilen.append(r'\multicolumn{4}{@{}l}{\rule{0pt}{3.2ex}\large\bfseries ' + tex(gebiet) + r'}\\[0.3ex]')
            if e['name'] != kapitel:
                kapitel = e['name']
                zeilen.append(r'\multicolumn{4}{@{}l}{\rule{0pt}{2.4ex}\bfseries ' + tex(kapitel) + r'}\\')
            mark = r' \textcolor{red!70!black}{\small (neu)}' if e['ordner'] in neu else ''
            # Abschnitte springen zum Stufenkopf im Blatt (plan.md § 10, 15.10. k; sprungziele.py)
            st = (r'\newline{\footnotesize\color{black!65}' + ' · '.join(
                (r'\hyperlink{%s@%s}{%s}' % (e['ordner'], slug(s), tex(s)) if slug(s) in e['ziele'] else tex(s))
                for s in e['stufen']) + '}') if e['stufen'] else ''
            zeilen.append(r'\hyperlink{%s.1}{%s}%s%s & \hyperlink{%s.1}{\ttfamily %s} & %d & \hyperlink{%s.1}{S.~%d}\\'
                          % (e['ordner'], tex(e['ein']), mark, st, e['ordner'], e['kennung'],
                             e['n'], e['ordner'], e['ab']))
        includes, kapitel = [], None
        for e in eintraege:
            toc = []
            if e['name'] != kapitel:
                kapitel = e['name']
                toc.append('1,section,1,{%s},kap%s' % (tex(kapitel), e['kap']))
            toc.append('1,subsection,2,{%s (%s)},%s' % (tex(e['ein']), e['kennung'], e['ordner']))
            includes.append(r'\includepdf[pages=-,link,linkname=%s,addtotoc={%s},pagecommand={\zurueck}]{%s.pdf}'
                            % (e['ordner'], ','.join(toc), e['ordner']))
        return r'''\documentclass[a4paper,11pt]{article}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}
\usepackage[margin=18mm]{geometry}\usepackage{longtable,array}
\usepackage[table]{xcolor}\usepackage{pdfpages}\usepackage{eso-pic}
\usepackage[hidelinks,bookmarksopen,bookmarksopenlevel=1]{hyperref}
\pagestyle{empty}
\newcommand{\zurueck}{\AddToShipoutPictureFG*{\put(\LenToUnit{\paperwidth-14mm},\LenToUnit{7mm}){%%
\hyperlink{karte}{\large\color{blue!60!black}$\uparrow$}}}}
\begin{document}
\pdfbookmark[1]{Bestellkarte}{karte}\hypertarget{karte}{}
{\LARGE\bfseries Prüfung P10 -- alle Blätter}\par\smallskip
%%%s
\medskip
\renewcommand{\arraystretch}{1.15}
\begin{longtable}{@{}p{0.66\textwidth}lrr@{}}
\textbf{Einheit} \textcolor{black!60}{(Stufen)} & \textbf{Kennung} & \textbf{S.} & \textbf{ab}\\\hline\endhead
%s
\end{longtable}
\clearpage
%s
\end{document}
''' % (a.datum, '\n'.join(zeilen), '\n'.join(includes))

    def lauf(ks):
        open(os.path.join(tmp, 'g.tex'), 'w', encoding='utf-8').write(dokument(ks))
        for _ in range(2):
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'g.tex'], cwd=tmp,
                               capture_output=True, text=True)
        if not os.path.exists(os.path.join(tmp, 'g.pdf')):
            raise SystemExit(r.stdout[-3000:])
        return seiten(os.path.join(tmp, 'g.pdf')) - sum(e['n'] for e in eintraege)

    ist = lauf(karte_seiten)
    if ist != karte_seiten:
        ist = lauf(ist)
    aus = os.path.join(ziel, 'gesamtheft-p10.pdf')
    shutil.copy(os.path.join(tmp, 'g.pdf'), aus)
    # feste Seitenziele (Handy, Edge); Abschnitte auf der Seite ihres Stufenkopfs
    n, fehler = feste_ziele(aus, {e['ordner']: e['pdf'] for e in eintraege})
    if not fehler:
        erw = []
        for e in eintraege:
            for s, (sb, _) in stufenziele(e['pdf']).items():
                if s in {slug(x) for x in e['stufen']}:
                    erw.append((1 if ist == 1 else None, e['ab'] + sb, f'{e["ordner"]}@{s}'))
        n, fehler = pruefe(aus, erw)
    print(f'Sprungmarken {n}, Fehler {len(fehler)}' + (': ' + '; '.join(fehler[:8]) if fehler else ''))
    if fehler:
        raise SystemExit('Sprungmarken treffen nicht')
    print(f'{aus}: {seiten(aus)} Seiten, Karte {ist} S., {len(eintraege)} Blätter')
    shutil.rmtree(tmp)


if __name__ == '__main__':
    main()

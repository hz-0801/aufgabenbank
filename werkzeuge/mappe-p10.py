#!/usr/bin/env python3
"""mappe-p10.py – Mappe P10 für den Lehrer, ein Lauf, ohne Modell (plan.md § 10, 14.10. f; 15.10. i).

Folge: Bestellkarte (Gebiete, Blätter, Stufen mit fünf Punkten; jede Zeile springt zum Blatt) · Handreichung
(bestellkarte.py --handreichung: alle Stufen der Gliederung, nie geprüfte grau) · Inhalt (Gebiet -> Blatt mit den
Seiten von Blatt, Lösung, Mehr -> eingerückt die Abschnitte; Basiszettel, Original neu, Verzeichnisse) · je Einheit
in Lernfolge Blatt, Lösung, Mehr, Mehr-Lösung · Basiszettel BAS-Z1–Z10 (Aufgaben, Ergebnisse) · Original neu je
Jahr, jüngstes zuerst, mit Lösung (nur privat) · Stichwortverzeichnis (Blattnamen, Stufen, Fachwörter der
Gliederungen -> Seite) · Fundstellenregister („P10 ’JJ · Nr.“ -> „Blatt 115“ bzw. „Mehr 115“, privat auch
„Original neu“). Heftseiten (Original) stehen seit 15.10. in keiner Ausgabe. Alle Seitenangaben springen; der Lauf
prüft jede Sprungmarke gegen das fertige PDF.

Zwei Ausgaben aus einem Lauf:
  aufgabenbank-privat bau/mappe/<datum>/mappe-p10.pdf        mit Original neu (Wortlaut)
  aufgabenbank       bau/pruefung/<datum>/mappe-p10-ohne.pdf  ohne Original neu
Seit 16.10. (plan.md § 10, 16.10. g) kommen keine Lösungen in die Mappe – sie gehen nur mit der Bestellung
(<Kennung>-loesung.pdf, Mehr-Lösung hinten in <Kennung>-mehr.pdf).

Eingaben: Blätter bau/pruefung/<datum>/<ordner>/pdf/ (Neusatz: werkzeuge/neusatz-p10.py); Mehr wird hier gesetzt
(pruefheft.py --art mehr --alle, nach bau/pruefung/<datum>/<ordner>/mehr/); Original neu wird hier gesetzt
(originalneu.py, nach aufgabenbank-privat bau/original-neu/<heft>/); Einheiten, Folge, Ordner, Stufen aus den
Gliederungen (p10einheiten.py).

  python3 werkzeuge/mappe-p10.py --datum 2026-10-14 [--ohne-neubau]
"""
import argparse, csv, glob, json, os, re, shutil, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
from p10einheiten import einheiten as p10_einheiten, gebiete as p10_gebiete, MN_VORGABE  # noqa: E402
import bestellkarte as BK  # noqa: E402
from sprungziele import slug, stufenziele, feste_ziele, pruefe as pruefe_fest  # noqa: E402

PRIVAT_VORGABE = os.environ.get('PRIVAT') or os.path.join(os.path.dirname(BANK), 'aufgabenbank-privat')
HEFTE = ['2026-for', '2026-ebr', '2025-os', '2024-os', '2023-os', '2022-os', '2021-os', '2020-os', '2019-os',
         '2018-os', '2017-os', '2016-os', '2015-os', '2014-os']


def seiten(pdf):
    o = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    return int(re.search(r'Pages:\s+(\d+)', o).group(1))


def tex(s):
    for a, b in [('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'),
                 ('_', r'\_'), ('{', r'\{'), ('}', r'\}')]:
        s = s.replace(a, b)
    return s


def norm(s):
    return re.sub(r'\s+', '', s or '')


# --------------------------------------------------------------------------- Bausteine setzen

def baue_mehr(e, datum, mn):
    aus = os.path.join(BANK, 'bau', 'pruefung', datum, e['ordner'], 'mehr')
    for wunsch in (e['einheit'], e['anzeige']):
        r = subprocess.run([sys.executable, os.path.join(HIER, 'pruefheft.py'), '--kapitel', e['kapitel'],
                            '--art', 'mehr', '--alle', '--einheit', wunsch, '--datum', datum, '--aus', aus,
                            '--mn', mn], capture_output=True, text=True, cwd=BANK)
        if r.returncode == 0:
            break
    ok = r.returncode == 0 and 'Fehler 0' in r.stdout and not re.search(r'Fehler [1-9]', r.stdout)
    ids = re.search(r'^ids: (.*)$', r.stdout, re.M)
    print(f'Mehr {e["kennung"]} {e["ordner"]}: ' + (r.stdout.strip().splitlines()[-2] if ok else
                                                     'kein Mehr – ' + (r.stdout + r.stderr).strip()[-200:]))
    if not ok:
        return None
    return dict(blatt=os.path.join(aus, 'pdf', 'mehr.pdf'), loesung=os.path.join(aus, 'pdf', 'mehr-loesung.pdf'),
                ids=ids.group(1).split() if ids else [])


def baue_originalneu(heft, privat):
    r = subprocess.run([sys.executable, os.path.join(HIER, 'originalneu.py'), '--heft', heft, '--privat', privat],
                       capture_output=True, text=True, cwd=BANK)
    print(f'Original neu {heft}: ' + r.stdout.strip().splitlines()[-1][:60] if r.stdout.strip() else r.stderr[-300:])
    if r.returncode:
        raise SystemExit(f'Original neu {heft} gescheitert')


# --------------------------------------------------------------------------- Seiten finden

MARKE = re.compile(r'’(\d\d)·(\d)([a-j]?)')   # Aufgaben der P10 einstellig; die Nummer klebt sonst an der Marke („’25·38“, 16.10.)


def marken(pdf):
    """Seite (1-basiert) -> Fundstellen „JJ·Na“ aus den Randmarken des Satzes (’25 · 4a, nach P10 ’25 · 4a)."""
    import pypdf
    out = {}
    for i, p in enumerate(pypdf.PdfReader(pdf).pages, 1):
        out[i] = {f'{m.group(1)}·{m.group(2)}{m.group(3)}' for m in MARKE.finditer(norm(p.extract_text()))}
    return out


def stufenseiten(pdf, namen):
    """Stufenname -> erste Seite, auf der sein Kopf steht (Name, dahinter Punkte oder „zuletzt“)."""
    import pypdf
    txt = [norm(p.extract_text()) for p in pypdf.PdfReader(pdf).pages]
    out = {}
    for n in namen:
        k = norm(n)
        for i, t in enumerate(txt, 1):
            if re.search(re.escape(k) + r'(?=[•◦]|zuletzt)', t):
                out[n] = i
                break
    return out


def ziele(pdf):
    """Benannte Ziele (hypertarget) -> Seite (1-basiert)."""
    import pypdf
    r = pypdf.PdfReader(pdf)
    return {k: r.get_destination_page_number(v) + 1 for k, v in r.named_destinations.items()}


def fundstelle(iid):
    """2025-OS-K4a -> („P10 ’25 · 4a“, „25·4a“, Sortierschlüssel)."""
    m = re.match(r'^(\d{4})-([A-Z]+)-[BK](\d+)([a-z]?)$', iid)
    if not m:
        return None
    j, pap, n, t = m.groups()
    zusatz = '' if pap == 'OS' else f' {pap}'
    return (f'P10 ’{j[2:]}{zusatz} \\pkt{{}} {n}{t}', f'{j[2:]}·{n}{t}', (-int(j), pap, int(n), t))


# --------------------------------------------------------------------------- Dokument

PRAEAMBEL = BK.PRAEAMBEL.replace(r'\usepackage[hidelinks]{hyperref}', r'\usepackage{pdfpages}\usepackage{multicol}'
                                 r'\usepackage[hidelinks,bookmarksopen,bookmarksopenlevel=1]{hyperref}') + r'''
\newcommand{\pkt}{\textperiodcentered{}}
\newcommand{\regkopf}[1]{\clearpage{\LARGE\bfseries #1}\par\vspace{1ex}}
\usepackage{eso-pic}
\AddToShipoutPictureFG{\AtPageLowerLeft{\put(\LenToUnit{\paperwidth-13mm},\LenToUnit{7mm}){%
\hyperlink{inhaltsziel}{\Large\color{black!55}$\uparrow$}}}}
'''


def baue(teile, vorn, register, ziel_pdf):
    """teile: Liste dict(pdf, name, toc) in Folge; vorn (Karte, Handreichung, Inhalt), register: TeX-Text."""
    tmp = tempfile.mkdtemp(prefix='mappe-')
    for i, t in enumerate(teile):
        shutil.copy(t['pdf'], os.path.join(tmp, f't{i}.pdf'))
    inc = []
    for i, t in enumerate(teile):
        toc = ','.join(t['toc'])
        inc.append(r'\includepdf[pages=-,link,linkname=%s%s]{t%d.pdf}'
                   % (t['name'], (',addtotoc={' + toc + '}') if toc else '', i))
    # 15.10.: Zeichen aus Stufennamen und Daten, die pdflatex nicht kennt (Mappe Abitur: „f′“, „⅙“)
    uni = ''.join(r'\DeclareUnicodeCharacter{%s}{\texorpdfstring{\ensuremath{%s}}{%s}}' % (c, m, t) + '\n'
                  for c, m, t in [('2032', "{}'", "'"), ('2033', "{}''", "''"), ('2153', r'\tfrac13', '1/3'),
                                  ('2154', r'\tfrac23', '2/3'), ('2159', r'\tfrac16', '1/6')])
    doc = (PRAEAMBEL + uni + r'\begin{document}' + '\n' + vorn + '\n' + '\n'.join(inc) + '\n' + register
           + '\n\\end{document}\n')
    open(os.path.join(tmp, 'm.tex'), 'w', encoding='utf-8').write(doc)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'm.tex'], cwd=tmp, capture_output=True, text=True)
    if not os.path.exists(os.path.join(tmp, 'm.pdf')) or '! ' in r.stdout:
        raise SystemExit('pdflatex: ' + '\n'.join(l for l in r.stdout.splitlines() if l.startswith('!'))[:2000])
    os.makedirs(os.path.dirname(ziel_pdf), exist_ok=True)
    shutil.copy(os.path.join(tmp, 'm.pdf'), ziel_pdf)
    shutil.rmtree(tmp)


def kartenseiten(E):
    """Bestellkarte wie bestellkarte.py (eine Seite je Gebiet), Zeilen springen zu <ordner>.1."""
    G = p10_gebiete([e['einheit'] for e in E])
    return '\n'.join(BK.seite(g, [e for e in E if e['gebiet'] == g]) for g in G)


def handreichung(E, mn):
    """Handreichung wie bestellkarte.py --handreichung (plan.md § 10, 14.10. h), direkt hinter der Bestellkarte."""
    G = p10_gebiete([e['einheit'] for e in E])
    return '\n'.join(BK.handreichung_seite(g, [e for e in E if e['gebiet'] == g], mn) for g in G)


def links(lst):
    return ', '.join(r'\hyperlink{%s}{%d}' % (z, s) for z, s in lst)


def inhalt_tex(eins, A, S, teile, mit_original):
    """Inhalt (Auftrag 15.10. d): Gebiet -> Blatt (Seiten von Blatt, Lösung, Mehr) -> eingerückt die Abschnitte.
    A: Teilname -> erste Seite; S: Ordner -> {Anzeigename: Seite im Blatt}."""
    namen = {t['name'] for t in teile}
    out = [r'\clearpage\pdfbookmark[0]{Inhalt}{inhalt}\hypertarget{inhaltsziel}{}{\LARGE\bfseries Inhalt}\par\vspace{1ex}',
           r'{\small\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}']
    zeile = lambda links_, rechts: r'%s\nobreak\dotfill\nobreak %s\par' % (links_, rechts)
    gebiet = None
    for e in eins:
        o = e['ordner']
        if e['gebiet'] != gebiet:
            gebiet = e['gebiet']
            out.append(r'\vspace{1.4ex}{\large\bfseries %s}\par\vspace{.4ex}' % tex(gebiet))
        teile_r = [r'Blatt \hyperlink{%s.1}{%d}' % (o, A[o])]   # keine Lösungen in der Mappe (plan.md § 10, 16.10. g)
        if o + '-m' in namen:
            teile_r.append(r'Mehr \hyperlink{%s-m.1}{%d}' % (o, A[o + '-m']))
        out.append(r'\vspace{.5ex}' + zeile(r'\hyperlink{%s.1}{\bfseries %s} {\color{black!55}%s}'
                                             % (o, tex(e['anzeige']), e['kennung']), r' \enspace '.join(teile_r)))
        for _, anz in e['stufen']:
            if anz in S[o]:
                ziel = '%s@%s' % (o, slug(anz))   # Stufenkopf im Blatt (sprungziele.py), plan.md § 10, 15.10. k
                out.append(zeile(r'\hspace*{1.5em}\hyperlink{%s}{%s}' % (ziel, tex(anz)),
                                 r'\hyperlink{%s}{%d}' % (ziel, A[o] + S[o][anz] - 1)))
    out.append(r'\vspace{1.4ex}' + zeile(r'{\large\bfseries Basiszettel}', r'\hyperlink{basz1.1}{%d}' % A['basz1']))
    if mit_original:
        out.append(r'\vspace{1.4ex}{\large\bfseries Original neu}\par\vspace{.4ex}')
        for t in teile:
            if t['name'].startswith('neu') and not t['name'].startswith('neul'):
                out.append(zeile(r'\hspace*{1.5em}%s' % t['titel'], r'\hyperlink{%s.1}{%d}' % (t['name'], A[t['name']])))
    for marke, titel in (('stichwort', 'Stichwortverzeichnis'), ('fundstellen', 'Fundstellenregister')):
        out.append(r'\vspace{1.4ex}' + zeile(r'{\large\bfseries %s}' % titel,
                                             r'\hyperlink{%s}{\pageref*{%s}}' % (marke, marke)))
    out.append('}')
    return '\n'.join(out)


ORT = (('blatt', 'Blatt'), ('mehr', 'Mehr'), ('neu', 'Original neu'))


def register_tex(stich, fund):
    """stich: Liste (Wort, [(ziel, seite)]); fund: Liste (Marke, Schlüssel, {art: [(ziel, seite)]})."""
    out = [r'\clearpage\pdfbookmark[0]{Stichwortverzeichnis}{stichwort}\hypertarget{stichwort}{}\label{stichwort}'
           r'{\LARGE\bfseries Stichwortverzeichnis}\par\vspace{1ex}',
           r'\begin{multicols}{2}\small\raggedright\setlength{\parindent}{0pt}']
    buch = None
    for w, lst in stich:
        b = w[0].upper()
        if b != buch:
            buch = b
            out.append(r'\par\medskip{\bfseries %s}\par' % tex(b))
        out.append(r'\hangindent1em %s\enspace %s\par' % (tex(w), links(lst)))
    out.append(r'\end{multicols}')
    out.append(r'\clearpage\pdfbookmark[0]{Fundstellenregister}{fundstellen}\hypertarget{fundstellen}{}'
               r'\label{fundstellen}{\LARGE\bfseries Fundstellenregister}\par\vspace{1ex}')
    out.append(r'\begin{multicols}{2}\footnotesize\raggedright\setlength{\parindent}{0pt}')
    jahr = None
    for marke, schl, wo in fund:
        j = schl[0]
        if j != jahr:
            jahr = j
            out.append(r'\par\medskip{\bfseries %s}\par' % marke.split(r' \pkt{}')[0])
        teile = [r'{\color{black!55}%s} %s' % (name, links(wo[k])) for k, name in ORT if wo.get(k)]
        out.append(r'\hangindent1em %s\enspace %s\par' % (marke, r' \enspace '.join(teile) or '–'))
    out.append(r'\end{multicols}')
    return '\n'.join(out)


def pfeile(pdf, vorn):
    """„↑“ auf jeder Seite: ein Link unten rechts, der auf die Seite des Inhalts springt."""
    import pypdf
    r = pypdf.PdfReader(pdf)
    seite = {p.indirect_reference.idnum: i + 1 for i, p in enumerate(r.pages)}
    inhalt = None
    for i, p in enumerate(r.pages):
        if 'Inhalt' in (p.extract_text() or '')[:40] and i + 1 <= vorn:
            inhalt = i + 1
    fehler = []
    for i, p in enumerate(r.pages):
        ok = False
        for a in p.get('/Annots') or []:
            a = a.get_object()
            d = a.get('/Dest')
            rect = [float(x) for x in a.get('/Rect', [0, 0, 0, 0])]
            if a.get('/Subtype') == '/Link' and d is not None and rect[1] < 60 and rect[0] > float(p.mediabox.right) - 80:
                ok = seite.get(d[0].idnum) == inhalt
        if not ok:
            fehler.append(f'S. {i + 1}: kein ↑ zum Inhalt (S. {inhalt})')
    return fehler


def pruefe_sprungmarken(pdf, erwartet):
    """Jede Sprungmarke trifft: erwartet = {(ziel, angezeigte Seite)}; jedes Ziel muss im PDF stehen und auf der
    angezeigten Seite liegen; dazu jeder Link im PDF muss ein vorhandenes Ziel haben. Rückgabe Liste der Fehler."""
    import pypdf
    r = pypdf.PdfReader(pdf)
    Z = {k: r.get_destination_page_number(v) + 1 for k, v in r.named_destinations.items()}
    fehler = [f'{z}: zeigt {s}, liegt {Z.get(z, "fehlt")}' for z, s in sorted(erwartet) if Z.get(z) != s]
    n = 0
    for p in r.pages:
        for a in p.get('/Annots') or []:
            a = a.get_object()
            if a.get('/Subtype') != '/Link':
                continue
            d = a.get('/Dest') or (a.get('/A') or {}).get('/D')
            if d is None:
                continue
            n += 1
            if isinstance(d, (str, bytes)) or hasattr(d, 'original_bytes'):
                if str(d) not in Z:
                    fehler.append(f'Link ohne Ziel: {d}')
    return fehler, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--datum', required=True)
    ap.add_argument('--mn', default=MN_VORGABE)
    ap.add_argument('--privat', default=PRIVAT_VORGABE)
    ap.add_argument('--ohne-neubau', action='store_true', help='Mehr und Original neu nicht neu setzen')
    a = ap.parse_args()
    ziel = os.path.join(BANK, 'bau', 'pruefung', a.datum)
    eins = p10_einheiten(a.mn)

    # Bausteine
    mehr = {}
    for e in eins:
        if a.ohne_neubau:
            d = os.path.join(ziel, e['ordner'], 'mehr', 'pdf')
            mehr[e['ordner']] = dict(blatt=os.path.join(d, 'mehr.pdf'), loesung=os.path.join(d, 'mehr-loesung.pdf')) \
                if os.path.exists(os.path.join(d, 'mehr.pdf')) else None
        else:
            mehr[e['ordner']] = baue_mehr(e, a.datum, a.mn)
    if not a.ohne_neubau:
        for h in HEFTE:
            baue_originalneu(h, a.privat)

    # Teile in Folge
    def teil(pdf, name, toc=(), titel=''):
        return dict(pdf=pdf, name=name, toc=list(toc), n=seiten(pdf), titel=titel)
    gebiet, T_ein = None, []
    for e in eins:
        o = os.path.join(ziel, e['ordner'], 'pdf')
        toc = []
        if e['gebiet'] != gebiet:
            gebiet = e['gebiet']
            toc.append('1,section,1,{%s},geb%s' % (tex(gebiet), e['kennung']))
        toc.append('1,subsection,2,{%s (%s)},%s' % (tex(e['anzeige']), e['kennung'], e['ordner']))
        T_ein.append(teil(os.path.join(o, '2-blatt.pdf'), e['ordner'], toc))
        if mehr[e['ordner']]:
            T_ein.append(teil(mehr[e['ordner']]['blatt'], e['ordner'] + '-m'))
    T_bas = []
    for i in range(1, 11):
        T_bas.append(teil(os.path.join(BANK, 'bau', 'zettel', f'BAS-Z{i}', f'BAS-Z{i}.pdf'), f'basz{i}',
                          (['1,section,1,{Basiszettel},basis'] if i == 1 else []) + [f'1,subsection,2,{{BAS-Z{i}}},bz{i}']))
    T_neu = []
    for k, h in enumerate(HEFTE):
        d = os.path.join(a.privat, 'bau', 'original-neu', h, 'pdf')
        jj = h[2:4] + ('' if h.endswith('os') else ' ' + h[5:].upper())
        T_neu.append(teil(os.path.join(d, 'blatt.pdf'), f'neu{h}', (['1,section,1,{Original neu},origneu'] if k == 0 else [])
                          + [f'1,subsection,2,{{Original neu ’{jj}}},n{h}'], titel=f'P10 ’{jj}'))

    # Karte und Handreichung (TeX); die Seitenzahl des Vorspanns misst der erste Satz
    E = BK.eintraege(ziel, 0, a.mn)
    karte = r'\pdfbookmark[0]{Bestellkarte}{karte}\hypertarget{karte}{}' + kartenseiten(E)
    hand = r'\pdfbookmark[0]{Handreichung}{handreichung}' + handreichung(E, a.mn)
    # Seite je Stufenkopf: aus dem Sprungziel des Setzers (stufe-<slug>), sonst aus dem Text; T = nur Text (Prüfung)
    T = {e['ordner']: stufenseiten(os.path.join(ziel, e['ordner'], 'pdf', '2-blatt.pdf'), [x for _, x in e['stufen']])
         for e in eins}
    S = {}
    for e in eins:
        Z = stufenziele(os.path.join(ziel, e['ordner'], 'pdf', '2-blatt.pdf'))
        S[e['ordner']] = {x: (Z[slug(x)][0] + 1 if slug(x) in Z else T[e['ordner']][x])
                          for _, x in e['stufen'] if slug(x) in Z or x in T[e['ordner']]}

    def ab(teile, vorn):
        s, out = vorn + 1, {}
        for t in teile:
            out[t['name']] = s
            s += t['n']
        return out

    # Stichwörter: Blattname, Kapitel, Stufen (Anzeigename und Name der Gliederung) -> Seiten des Blatts
    sys.path.insert(0, os.path.join(a.mn, 'werkzeuge'))
    import gliederung as GL

    def stichwoerter(A):
        st = {}
        for e in eins:
            o = e['ordner']
            st.setdefault(e['anzeige'], []).append((f'{o}.1', A[o]))
            st.setdefault(e['kapitelname'], []).append((f'{o}.1', A[o]))
            for name, anz in e['stufen']:
                if anz in S[o]:
                    for w in {anz, name}:
                        st.setdefault(w, []).append((f'{o}.{S[o][anz]}', A[o] + S[o][anz] - 1))
            G = GL.lies(os.path.join(a.mn, 'msa', 'gliederung', e['kapitel'] + '.md'))
            for s in G['stufen']:
                b = s['felder'].get('Begriff') or ''
                m = re.match(r'^(?:Die\s+|Der\s+|Das\s+)?([A-ZÄÖÜ][\wäöüß]+)', b)
                if m and s['abschnitt'] == e['einheit'] and (s['felder'].get('Anzeigename') or s['name']) in S[o]:
                    p = S[o][s['felder'].get('Anzeigename') or s['name']]
                    st.setdefault(m.group(1), []).append((f'{o}.{p}', A[o] + p - 1))
        return sorted(((w, sorted(set(l), key=lambda x: x[1])) for w, l in st.items()), key=lambda x: x[0].casefold())

    # Fundstellen
    alle_ids = set()
    for f in glob.glob(os.path.join(a.mn, 'msa', 'mehr-p10', '*.csv')):
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
            alle_ids.add(r['eltern_id'].strip())
    for z in open(os.path.join(BANK, 'bau', 'register.csv'), encoding='utf-8').read().splitlines()[1:]:
        if ';2026-10-14;' in z or f';{a.datum};' in z:
            m = re.search(r'ids=([^,]*)', z)
            if m and 'art=p' in z:
                alle_ids |= {re.sub(r'-m\d+$', '', i) for i in m.group(1).split()}
    orig_daten = {}
    for n in ('basis-originale.jsonl', 'hauptteil-originale.jsonl'):
        for l in open(os.path.join(a.privat, n), encoding='utf-8'):
            if l.strip():
                z = json.loads(l)
                orig_daten[z['id']] = z
    marken_cache = {}

    def fund_liste(teile, A, mit_original):
        wo = {}
        for t in teile:
            ort = next((k for e in eins for k, nm in (('blatt', e['ordner']), ('mehr', e['ordner'] + '-m'))
                        if t['name'] == nm), None)
            if not ort:
                continue
            if t['pdf'] not in marken_cache:
                marken_cache[t['pdf']] = marken(t['pdf'])
            for s, ms in marken_cache[t['pdf']].items():
                for mk in ms:
                    wo.setdefault(mk, {}).setdefault(ort, []).append((f'{t["name"]}.{s}', A[t['name']] + s - 1))
        if mit_original:
            for h in HEFTE:
                Z = ziele(os.path.join(a.privat, 'bau', 'original-neu', h, 'pdf', 'blatt.pdf'))
                for iid, s in Z.items():
                    if iid in orig_daten:
                        wo.setdefault(iid, {}).setdefault('neu', []).append((f'neu{h}.{s}', A[f'neu{h}'] + s - 1))
        out, fehlt = [], []
        ids = (alle_ids | set(orig_daten)) if mit_original else alle_ids
        for iid in sorted(ids, key=lambda i: fundstelle(i)[2] if fundstelle(i) else (0,)):
            f = fundstelle(iid)
            if not f:
                continue
            w = {}
            # Marke im Satz trägt kein Papier; 2026 hat auf Blatt und Mehr nur FOR
            # seit 16.10. trägt eine Nummer mit Teilen desselben Originals die Marke einmal ohne Buchstaben („’25 · 3“)
            for key in (f[1], re.sub(r'[a-z]$', '', f[1])):
                if key in wo and iid.split('-')[1] != 'EBR':
                    for k in ('blatt', 'mehr'):
                        if k in wo[key] and k not in w:
                            w[k] = sorted(set(wo[key][k]), key=lambda x: x[1])
            if iid in wo and 'neu' in wo[iid]:
                w['neu'] = wo[iid]['neu']
            if iid in alle_ids and not (w.get('blatt') or w.get('mehr')):
                fehlt.append(iid)
            out.append((f[0], (iid[:4],) + f[2], w))
        return out, fehlt

    berichte = []
    for teile, mit_orig, ausgabe in (
            (T_ein + T_bas + T_neu, True, os.path.join(a.privat, 'bau', 'mappe', a.datum, 'mappe-p10.pdf')),
            (T_ein + T_bas, False, os.path.join(ziel, 'mappe-p10-ohne.pdf'))):
        vorn = 0
        for _ in range(3):
            A = ab(teile, vorn)
            fund, fehlt = fund_liste(teile, A, mit_orig)
            stich = stichwoerter(A)
            reg = register_tex(stich, fund)
            baue(teile, karte + '\n' + hand + '\n' + inhalt_tex(eins, A, S, teile, mit_orig), reg, ausgabe)
            echt = ziele(ausgabe)[teile[0]['name'] + '.1'] - 1
            if echt == vorn:
                break
            vorn = echt
        erwartet = set()
        for _, lst in stich:
            erwartet |= set(lst)
        for _, _, w in fund:
            for lst in w.values():
                erwartet |= set(lst)
        for e in eins:
            o = e['ordner']
            erwartet |= {(f'{o}.{p}', A[o] + p - 1) for p in S[o].values()}
        erwartet |= {(f'{t["name"]}.1', A[t['name']]) for t in teile}
        fehler, n_links = pruefe_sprungmarken(ausgabe, erwartet)
        # feste Seitenziele (Handy, Edge); Abschnittslinks müssen auf der Seite landen, auf der der Text des
        # Stufenkopfs steht (unabhängig vom Sprungziel gesucht)
        n_fest, f_fest = feste_ziele(ausgabe, {e['ordner']: os.path.join(ziel, e['ordner'], 'pdf', '2-blatt.pdf')
                                              for e in eins})
        fehler += f_fest
        if not f_fest:
            ab_erw = [(None, A[e['ordner']] + T[e['ordner']][x] - 1, f'Abschnitt {e["ordner"]}: {x}')
                      for e in eins for _, x in e['stufen'] if x in T[e['ordner']]]
            ab_erw += [(None, A[e['ordner']] + p - 1, f'Abschnitt {e["ordner"]}: {x} (Ziel)')
                       for e in eins for x, p in S[e['ordner']].items()]
            n_links, f2 = pruefe_fest(ausgabe, ab_erw)
            fehler += f2
            fehler += pfeile(ausgabe, vorn)
        berichte.append(f'{ausgabe}: {seiten(ausgabe)} Seiten (Vorspann {vorn}); Fundstellen {len(fund)}, ohne Seite '
                        f'auf Blatt/Mehr {len(fehlt)}' + (f' ({" ".join(fehlt[:12])}{" …" if len(fehlt) > 12 else ""})'
                                                           if fehlt else '')
                        + f'; Sprungmarken {n_links}, Fehler {len(fehler)}' + (': ' + '; '.join(fehler[:8]) if fehler else ''))
        if fehler:
            print('\n'.join(berichte))
            raise SystemExit('Sprungmarken treffen nicht')
    print('\n'.join(berichte))


if __name__ == '__main__':
    main()

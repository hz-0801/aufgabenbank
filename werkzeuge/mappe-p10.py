#!/usr/bin/env python3
"""mappe-p10.py – Mappe P10 für den Lehrer, ein Lauf, ohne Modell (plan.md § 10, 14.10. f).

Folge: Bestellkarte (Gebiete, Blätter, Stufen mit fünf Punkten; jede Zeile springt zum Blatt) · je Einheit in
Lernfolge Blatt, Lösung, Mehr, Mehr-Lösung · Basiszettel BAS-Z1–Z10 (Aufgaben, Ergebnisse) · Original neu je Jahr,
jüngstes zuerst, mit Lösung · Original (Heft wie vom Bildungsserver) je Jahr, jüngstes zuerst ·
Stichwortverzeichnis (Blattnamen, Stufen, Fachwörter der Gliederungen -> Seite) · Fundstellenregister („P10 ’JJ ·
Nr.“ -> Seiten auf Blatt oder Mehr, Original neu, Original). Alle Seitenangaben springen.

Zwei Ausgaben aus einem Lauf:
  aufgabenbank-privat bau/mappe/<datum>/mappe-p10.pdf        vollständig (Original neu und Original: Wortlaut)
  aufgabenbank       bau/pruefung/<datum>/mappe-p10-ohne.pdf  ohne Original neu und Original
Die Lösungen gehören zur Mappe; das Schülerheft (gesamtheft.py) bleibt ohne.

Eingaben: Blätter bau/pruefung/<datum>/<ordner>/pdf/ (Neusatz: werkzeuge/neusatz-p10.py); Mehr wird hier gesetzt
(pruefheft.py --art mehr --alle, nach bau/pruefung/<datum>/<ordner>/mehr/); Original neu wird hier gesetzt
(originalneu.py, nach aufgabenbank-privat bau/original-neu/<heft>/); Hefte aufgabenbank-privat hefte/; Einheiten,
Folge, Ordner, Stufen aus den Gliederungen (p10einheiten.py).

  python3 werkzeuge/mappe-p10.py --datum 2026-10-14 [--ohne-neubau]
"""
import argparse, csv, glob, json, os, re, shutil, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
from p10einheiten import einheiten as p10_einheiten, gebiete as p10_gebiete, MN_VORGABE  # noqa: E402
import bestellkarte as BK  # noqa: E402

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

MARKE = re.compile(r'’(\d\d)·(\d+)([a-j]?)')


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
'''


def baue(teile, karte, register, ziel_pdf):
    """teile: Liste dict(pdf, name, toc) in Folge; karte, register: TeX-Text. Erst Probe für die Kartenseiten."""
    tmp = tempfile.mkdtemp(prefix='mappe-')
    for i, t in enumerate(teile):
        shutil.copy(t['pdf'], os.path.join(tmp, f't{i}.pdf'))
    inc = []
    for i, t in enumerate(teile):
        toc = ','.join(t['toc'])
        inc.append(r'\includepdf[pages=-,link,linkname=%s%s]{t%d.pdf}'
                   % (t['name'], (',addtotoc={' + toc + '}') if toc else '', i))
    doc = (PRAEAMBEL + r'\begin{document}' + '\n\\pdfbookmark[0]{Bestellkarte}{karte}\\hypertarget{karte}{}\n'
           + karte + '\n' + '\n'.join(inc) + '\n' + register + '\n\\end{document}\n')
    open(os.path.join(tmp, 'm.tex'), 'w', encoding='utf-8').write(doc)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'm.tex'], cwd=tmp, capture_output=True, text=True)
    if not os.path.exists(os.path.join(tmp, 'm.pdf')) or '! ' in r.stdout:
        raise SystemExit('pdflatex: ' + '\n'.join(l for l in r.stdout.splitlines() if l.startswith('!'))[:2000])
    os.makedirs(os.path.dirname(ziel_pdf), exist_ok=True)
    shutil.copy(os.path.join(tmp, 'm.pdf'), ziel_pdf)
    shutil.rmtree(tmp)


def kartenseiten(E, ordner_pdf):
    """Bestellkarte wie bestellkarte.py (eine Seite je Gebiet), Zeilen springen zu <ordner>.1."""
    G = p10_gebiete([e['einheit'] for e in E])
    return '\n'.join(BK.seite(g, [e for e in E if e['gebiet'] == g]) for g in G), len(G)


def register_tex(stich, fund, mit_original):
    """stich: Liste (Wort, [(ziel, seite)]); fund: Liste (Marke, Schlüssel, {art: [(ziel, seite)]})."""
    def links(lst):
        return ', '.join(r'\hyperlink{%s}{%d}' % (z, s) for z, s in lst)
    out = [r'\regkopf{Stichwortverzeichnis}', r'\begin{multicols}{2}\small\raggedright\setlength{\parindent}{0pt}']
    buch = None
    for w, lst in stich:
        b = w[0].upper()
        if b != buch:
            buch = b
            out.append(r'\par\medskip{\bfseries %s}\par' % tex(b))
        out.append(r'\hangindent1em %s\enspace %s\par' % (tex(w), links(lst)))
    out.append(r'\end{multicols}')
    spalten = [('blatt', 'Blatt oder Mehr')] + ([('neu', 'Original neu'), ('orig', 'Original')] if mit_original else [])
    out.append(r'\regkopf{Fundstellenregister}')
    out.append(r'\begin{multicols}{2}\footnotesize\raggedright\setlength{\parindent}{0pt}')
    jahr = None
    for marke, schl, wo in fund:
        j = schl[0]
        if j != jahr:
            jahr = j
            out.append(r'\par\medskip{\bfseries %s}\par' % marke.split(r' \pkt{}')[0])
        teile = []
        for k, name in spalten:
            if wo.get(k):
                teile.append(r'{\color{black!55}%s} %s' % (name, links(wo[k])))
        out.append(r'\hangindent1em %s\enspace %s\par' % (marke, r' \enspace '.join(teile) or '–'))
    out.append(r'\end{multicols}')
    return '\n'.join(out)


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
    def teil(pdf, name, toc=()):
        return dict(pdf=pdf, name=name, toc=list(toc), n=seiten(pdf))
    gebiet, T_ein = None, []
    for e in eins:
        o = os.path.join(ziel, e['ordner'], 'pdf')
        toc = []
        if e['gebiet'] != gebiet:
            gebiet = e['gebiet']
            toc.append('1,section,1,{%s},geb%s' % (tex(gebiet), e['kennung']))
        toc.append('1,subsection,2,{%s (%s)},%s' % (tex(e['anzeige']), e['kennung'], e['ordner']))
        T_ein.append(teil(os.path.join(o, '2-blatt.pdf'), e['ordner'], toc))
        T_ein.append(teil(os.path.join(o, '3-loesungen.pdf'), e['ordner'] + '-l'))
        if mehr[e['ordner']]:
            T_ein.append(teil(mehr[e['ordner']]['blatt'], e['ordner'] + '-m'))
            T_ein.append(teil(mehr[e['ordner']]['loesung'], e['ordner'] + '-ml'))
    T_bas = []
    for i in range(1, 11):
        T_bas.append(teil(os.path.join(BANK, 'bau', 'zettel', f'BAS-Z{i}', f'BAS-Z{i}.pdf'), f'basz{i}',
                          (['1,section,1,{Basiszettel},basis'] if i == 1 else []) + [f'1,subsection,2,{{BAS-Z{i}}},bz{i}']))
    T_neu, T_orig = [], []
    for k, h in enumerate(HEFTE):
        d = os.path.join(a.privat, 'bau', 'original-neu', h, 'pdf')
        jj = h[2:4] + ('' if h.endswith('os') else ' ' + h[5:].upper())
        T_neu.append(teil(os.path.join(d, 'blatt.pdf'), f'neu{h}', (['1,section,1,{Original neu},origneu'] if k == 0 else [])
                          + [f'1,subsection,2,{{Original neu ’{jj}}},n{h}']))
        T_neu.append(teil(os.path.join(d, 'loesung.pdf'), f'neul{h}'))
        T_orig.append(teil(os.path.join(a.privat, 'hefte', h + '.pdf'), f'orig{h}',
                           (['1,section,1,{Original},orig'] if k == 0 else []) + [f'1,subsection,2,{{Original ’{jj}}},o{h}']))

    # Karte (Seiten zählen: eine je Gebiet)
    E = BK.eintraege(ziel, 0, a.mn)
    karte, n_karte = kartenseiten(E, ziel)

    def ab(teile):
        s, out = n_karte + 1, {}
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
            S = stufenseiten(os.path.join(ziel, o, 'pdf', '2-blatt.pdf'), [x for _, x in e['stufen']])
            for name, anz in e['stufen']:
                if anz in S:
                    for w in {anz, name}:
                        st.setdefault(w, []).append((f'{o}.{S[anz]}', A[o] + S[anz] - 1))
            G = GL.lies(os.path.join(a.mn, 'msa', 'gliederung', e['kapitel'] + '.md'))
            for s in G['stufen']:
                b = s['felder'].get('Begriff') or ''
                m = re.match(r'^(?:Die\s+|Der\s+|Das\s+)?([A-ZÄÖÜ][\wäöüß]+)', b)
                if m and s['abschnitt'] == e['einheit'] and (s['felder'].get('Anzeigename') or s['name']) in S:
                    p = S[s['felder'].get('Anzeigename') or s['name']]
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
    alle_ids_voll = alle_ids | set(orig_daten)

    def fund_liste(teile, A, mit_original):
        wo = {}
        for t in teile:
            if t['name'].endswith('-l') or t['name'].endswith('-ml') or not any(
                    t['name'] in (e['ordner'], e['ordner'] + '-m') for e in eins):
                continue
            for s, ms in marken(t['pdf']).items():
                for mk in ms:
                    wo.setdefault(mk, {}).setdefault('blatt', []).append((f'{t["name"]}.{s}', A[t['name']] + s - 1))
        if mit_original:
            for h in HEFTE:
                Z = ziele(os.path.join(a.privat, 'bau', 'original-neu', h, 'pdf', 'blatt.pdf'))
                for iid, s in Z.items():
                    if iid in orig_daten:
                        wo.setdefault(iid, {}).setdefault('neu', []).append((f'neu{h}.{s}', A[f'neu{h}'] + s - 1))
            for iid, z in orig_daten.items():
                h = f'{z["jahr"]}-{z["papier"].lower()}'
                s = z['quelle']['seite']
                wo.setdefault(iid, {}).setdefault('orig', []).append((f'orig{h}.{s}', A[f'orig{h}'] + s - 1))
        out, fehlt = [], []
        for iid in sorted(alle_ids_voll if mit_original else alle_ids, key=lambda i: fundstelle(i)[2] if fundstelle(i) else (0,)):
            f = fundstelle(iid)
            if not f:
                continue
            w = {}
            jahr_pap = iid.split('-')[1]
            # Marke im Satz trägt kein Papier; 2026 hat auf Blatt und Mehr nur FOR
            if f[1] in wo and (jahr_pap != 'EBR'):
                w['blatt'] = sorted(set(wo[f[1]]['blatt']), key=lambda x: x[1])
            for k in ('neu', 'orig'):
                if iid in wo and k in wo[iid]:
                    w[k] = wo[iid][k]
            if iid in alle_ids and 'blatt' not in w:
                fehlt.append(iid)
            out.append((f[0], (iid[:4],) + f[2], w))
        return out, fehlt

    berichte = []
    for name, teile, mit_orig, ausgabe in (
            ('mappe-p10.pdf', T_ein + T_bas + T_neu + T_orig, True,
             os.path.join(a.privat, 'bau', 'mappe', a.datum, 'mappe-p10.pdf')),
            ('mappe-p10-ohne.pdf', T_ein + T_bas, False, os.path.join(ziel, 'mappe-p10-ohne.pdf'))):
        A = ab(teile)
        fund, fehlt = fund_liste(teile, A, mit_orig)
        reg = register_tex(stichwoerter(A), fund, mit_orig)
        reg = r'\pdfbookmark[0]{Stichwortverzeichnis}{stichwort}' + reg.replace(
            r'\regkopf{Fundstellenregister}', r'\regkopf{Fundstellenregister}\pdfbookmark[0]{Fundstellenregister}{fundstellen}', 1)
        baue(teile, karte, reg, ausgabe)
        berichte.append(f'{ausgabe}: {seiten(ausgabe)} Seiten; Fundstellen {len(fund)}, ohne Seite auf Blatt/Mehr '
                        f'{len(fehlt)}' + (f' ({" ".join(fehlt[:12])}{" …" if len(fehlt) > 12 else ""})' if fehlt else ''))
    print('\n'.join(berichte))


if __name__ == '__main__':
    main()

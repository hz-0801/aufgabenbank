#!/usr/bin/env python3
"""mappe-abi.py – Mappe Abitur GK für den Lehrer, ein Lauf, ohne Modell (15.10.2026; Muster mappe-p10.py).

Folge: Bestellkarte (Gebiete, Blätter, Stufen mit fünf Punkten; Blatt und Stufe springen) · Handreichung (dazu die
Fundstellen je Stufe) · Inhalt (Gebiet -> Blatt mit den Seiten von Blatt, Lösung, Mehr -> eingerückt die Abschnitte;
Verzeichnisse) · je Einheit in Lernfolge Blatt, Lösung, Mehr, Mehr-Lösung (wie gesetzt von neusatz-abi.py) ·
Stichwortverzeichnis (Blattnamen, Kapitel, Stufen -> Seite) · Fundstellenregister („GK ’24 · B2.1a“ -> „Blatt 115“
bzw. „Mehr 115“). Alle Seitenangaben springen; der Lauf prüft jede Sprungmarke gegen das fertige PDF und stellt sie
auf feste Seitenziele um (sprungziele.py), Abschnittslinks auf die Seite des Stufenkopfs.

Zwei Ausgaben wie bei P10:
  aufgabenbank-privat bau/mappe/<datum>/mappe-abi-gk.pdf           privat
  aufgabenbank       bau/pruefung/<datum>/abitur/mappe-abi-gk-ohne.pdf  öffentlich
Die P10-Mappe trennt nach „Original neu“ (Wortlaut der Originale, nur privat). Für das Abitur gibt es noch kein
„Original neu“ (originalneu.py kennt nur P10-Hefte); beide Ausgaben haben darum heute denselben Inhalt, die private
bekommt den Teil, sobald es ihn gibt. Lösungen gehören zur Mappe.

Eingaben: bau/pruefung/<datum>/abitur/<ordner>/pdf/{2-blatt,3-loesungen,4-mehr,5-mehr-loesungen}.pdf
(werkzeuge/neusatz-abi.py); Einheiten, Folge, Ordner, Stufen aus mathe-nachhilfe abitur/gliederung
(p10einheiten.abi_einheiten); Fundstellen aus abitur/mehr-abi-gk/*.csv (eltern_id der GK-Hefte).

  python3 werkzeuge/mappe-abi.py --datum 2026-10-15 [--nur nullstellen,bedingt]   (--nur: Probe mit Teilmenge)
Prüfen: python3 werkzeuge/mappe-pruef.py <pdf> --pruefung abitur --fund [--oeffentlich]
"""
import argparse, csv, glob, importlib.util, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
from p10einheiten import abi_einheiten, gebiete, MN_VORGABE  # noqa: E402
import bestellkarte as BK  # noqa: E402
from sprungziele import slug, stufenziele, feste_ziele, pruefe as pruefe_fest  # noqa: E402

_sp = importlib.util.spec_from_file_location('mappe_p10', os.path.join(HIER, 'mappe-p10.py'))
MP = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(MP)
tex, seiten, norm = MP.tex, MP.seiten, MP.norm

PRIVAT_VORGABE = MP.PRIVAT_VORGABE
ABI_GK = re.compile(r'^(\d{4})-(?:bebb|bb|be)-gk(?:-cas)?-([AB]\d+(?:\.\d+)?[a-z]?)$')
MARKE = re.compile(r'GK’(\d\d)([AB]\d+(?:\.\d+)?[a-z]?)')
PRAEAMBEL_ABI = MP.PRAEAMBEL.replace('12pt', '11pt') + r'\setlength{\columnsep}{8mm}' + '\n'


def fundstelle(iid):
    """2024-bebb-gk-B2.1a -> („GK ’24 · B2.1a“, „24·B2.1a“, Sortierschlüssel)."""
    m = ABI_GK.match(iid)
    if not m:
        return None
    j, st = m.groups()
    zahlen = tuple(int(x) for x in re.findall(r'\d+', st[1:]))
    return (f'GK ’{j[2:]} \\pkt{{}} {st}', f'{j[2:]}·{st}', (-int(j), st[0], zahlen, st[-1] if st[-1].isalpha() else ''))


def marken(pdf, bekannt):
    """Seite -> Fundstellen „JJ·B2.1a“ aus den Randmarken (GK ’24 / B2.1a); nur bekannte (die Nummer der Aufgabe
    steht im Text direkt dahinter: „B2.11.“ = B2.1 und Nr. 1)."""
    import pypdf
    out = {}
    for i, p in enumerate(pypdf.PdfReader(pdf).pages, 1):
        t = norm(p.extract_text())
        s = set()
        for m in re.finditer(r'GK’(\d\d)([AB][\d.a-z]{1,8})', t):
            j, rest = m.groups()
            for n in range(len(rest), 1, -1):
                if f'{j}·{rest[:n]}' in bekannt:
                    s.add(f'{j}·{rest[:n]}')
                    break
        out[i] = s
    return out


def karte_seite(gebiet, eins, S, hand):
    """Wie bestellkarte.abi_seite, dazu Sprungmarken: Blatt -> erste Seite, Stufe -> Stufenkopf im Blatt."""
    bl = []
    for e in eins:
        o = e['ordner']
        z = [r'\multicolumn{2}{@{}l@{}}{\rule{0pt}{3ex}\hyperlink{%s.1}{\bfseries %s}\enspace{\footnotesize\color{black!45}%s}}\\'
             % (o, BK.abi_tex(e['anzeige']), e['kennung'])]
        for name, _ in e['stufen']:
            ids, neben = e['ids'][name]
            nm = r'{\small %s}' % BK.abi_tex(name)
            if name in S[o]:
                nm = r'\hyperlink{%s@%s}{%s}' % (o, slug(name), nm)
            z.append(r'\hspace*{1em}%s\enspace%s & %s\\' % (BK.KASTEN, nm, BK.lohnt(None, BK.abi_jahre(ids + neben))))
            if hand:
                z.append(r'\multicolumn{2}{@{}l@{}}{\hspace*{2.6em}{\scriptsize\color{black!50}%s}}\\'
                         % BK.abi_fundstellen(ids, neben))
        bl.append(r'\begin{tabular}{@{}>{\raggedright\arraybackslash\hangindent=2.5em\hangafter=1}p{0.385\textwidth}'
                  r'@{\hspace{0.6em}}l@{}}' + '\n'.join(z) + r'\end{tabular}\par')
    return (r'{\LARGE\bfseries %s}\par\vspace{1ex}\begin{multicols}{2}\raggedcolumns ' % tex(gebiet)
            + '\n'.join(bl) + r'\end{multicols}\clearpage')


def inhalt_tex(eins, A, S, namen):
    out = [r'\clearpage\pdfbookmark[0]{Inhalt}{inhalt}\hypertarget{inhaltsziel}{}{\LARGE\bfseries Inhalt}\par\vspace{1ex}',
           r'{\small\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}']
    zeile = lambda l, r: r'%s\nobreak\dotfill\nobreak %s\par' % (l, r)
    gebiet = None
    for e in eins:
        o = e['ordner']
        if e['gebiet'] != gebiet:
            gebiet = e['gebiet']
            out.append(r'\vspace{1.4ex}{\large\bfseries %s}\par\vspace{.4ex}' % tex(gebiet))
        rechts = [r'Blatt \hyperlink{%s.1}{%d}' % (o, A[o]), r'Lösung \hyperlink{%s-l.1}{%d}' % (o, A[o + '-l'])]
        if o + '-m' in namen:
            rechts.append(r'Mehr \hyperlink{%s-m.1}{%d}' % (o, A[o + '-m']))
        out.append(r'\vspace{.5ex}' + zeile(r'\hyperlink{%s.1}{\bfseries %s} {\color{black!55}%s}'
                                             % (o, BK.abi_tex(tex(e['anzeige'])), e['kennung']), r' \enspace '.join(rechts)))
        for name, _ in e['stufen']:
            if name in S[o]:
                ziel = '%s@%s' % (o, slug(name))
                out.append(zeile(r'\hspace*{1.5em}\hyperlink{%s}{%s}' % (ziel, BK.abi_tex(tex(name))),
                                 r'\hyperlink{%s}{%d}' % (ziel, A[o] + S[o][name] - 1)))
    for marke, titel in (('stichwort', 'Stichwortverzeichnis'), ('fundstellen', 'Fundstellenregister')):
        out.append(r'\vspace{1.4ex}' + zeile(r'{\large\bfseries %s}' % titel, r'\hyperlink{%s}{\pageref*{%s}}' % (marke, marke)))
    out.append('}')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--datum', required=True)
    ap.add_argument('--mn', default=MN_VORGABE)
    ap.add_argument('--privat', default=PRIVAT_VORGABE)
    ap.add_argument('--nur', default='', help='nur diese Ordner/Kennungen (Probe); Ausgabe mit Zusatz -probe')
    a = ap.parse_args()
    ziel = os.path.join(BANK, 'bau', 'pruefung', a.datum, 'abitur')
    nur = {x.strip() for x in a.nur.split(',') if x.strip()}
    eins = [e for e in abi_einheiten(a.mn) if not nur or e['ordner'] in nur or e['kennung'] in nur]
    fehlt = [e['ordner'] for e in eins if not os.path.exists(os.path.join(ziel, e['ordner'], 'pdf', '2-blatt.pdf'))]
    if fehlt:
        sys.exit(f'Blatt fehlt (erst neusatz-abi.py --datum {a.datum}): {" ".join(fehlt)}')

    def teil(pdf, name, toc=()):
        return dict(pdf=pdf, name=name, toc=list(toc), n=seiten(pdf), titel='')
    gebiet, T = None, []
    for e in eins:
        o = os.path.join(ziel, e['ordner'], 'pdf')
        toc = []
        if e['gebiet'] != gebiet:
            gebiet = e['gebiet']
            toc.append('1,section,1,{%s},geb%s' % (tex(gebiet), e['kennung']))
        toc.append('1,subsection,2,{%s (%s)},%s' % (tex(e['anzeige']), e['kennung'], e['ordner']))
        T.append(teil(os.path.join(o, '2-blatt.pdf'), e['ordner'], toc))
        T.append(teil(os.path.join(o, '3-loesungen.pdf'), e['ordner'] + '-l'))
        if os.path.exists(os.path.join(o, '4-mehr.pdf')):
            T.append(teil(os.path.join(o, '4-mehr.pdf'), e['ordner'] + '-m'))
            T.append(teil(os.path.join(o, '5-mehr-loesungen.pdf'), e['ordner'] + '-ml'))
    namen = {t['name'] for t in T}
    blatt = {e['ordner']: os.path.join(ziel, e['ordner'], 'pdf', '2-blatt.pdf') for e in eins}
    # Seite je Stufenkopf: Sprungziel des Setzers (stufe-<slug>), sonst Text; TX = nur Text (Prüfung)
    TX = {e['ordner']: MP.stufenseiten(blatt[e['ordner']], [n for n, _ in e['stufen']]) for e in eins}
    S = {}
    for e in eins:
        Z = stufenziele(blatt[e['ordner']])
        S[e['ordner']] = {n: (Z[slug(n)][0] + 1 if slug(n) in Z else TX[e['ordner']][n])
                          for n, _ in e['stufen'] if slug(n) in Z or n in TX[e['ordner']]}
    G = gebiete(eins)
    karte = r'\pdfbookmark[0]{Bestellkarte}{karte}\hypertarget{karte}{}' + '\n'.join(
        karte_seite(g, [e for e in eins if e['gebiet'] == g], S, False) for g in G)
    hand = r'\pdfbookmark[0]{Handreichung}{handreichung}' + '\n'.join(
        karte_seite(g, [e for e in eins if e['gebiet'] == g], S, True) for g in G)

    def ab(vorn):
        s, out = vorn + 1, {}
        for t in T:
            out[t['name']] = s
            s += t['n']
        return out

    def stichwoerter(A):
        st = {}
        for e in eins:
            o = e['ordner']
            st.setdefault(e['anzeige'], []).append((f'{o}.1', A[o]))
            st.setdefault(e['kapitelname'], []).append((f'{o}.1', A[o]))
            for name, _ in e['stufen']:
                if name in S[o]:
                    st.setdefault(name, []).append((f'{o}.{S[o][name]}', A[o] + S[o][name] - 1))
        return sorted(((w, sorted(set(l), key=lambda x: x[1])) for w, l in st.items()), key=lambda x: x[0].casefold())

    alle_ids = set()
    kap = {e['kapitel'] for e in eins}
    ein_namen = {(e['kapitel'], e['einheit']) for e in eins}
    for f in glob.glob(os.path.join(a.mn, 'abitur', 'mehr-abi-gk', '*.csv')):
        k = os.path.basename(f)[:-4]
        if k not in kap:
            continue
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
            if (k, (r.get('einheit') or '').strip()) in ein_namen and ABI_GK.match((r.get('eltern_id') or '').strip()):
                alle_ids.add(r['eltern_id'].strip())
    bekannt = {fundstelle(i)[1] for i in alle_ids}
    cache = {}

    def fund_liste(A):
        wo = {}
        for t in T:
            ort = next((k for e in eins for k, nm in (('blatt', e['ordner']), ('mehr', e['ordner'] + '-m'))
                        if t['name'] == nm), None)
            if not ort:
                continue
            if t['pdf'] not in cache:
                cache[t['pdf']] = marken(t['pdf'], bekannt)
            for s, ms in cache[t['pdf']].items():
                for mk in ms:
                    wo.setdefault(mk, {}).setdefault(ort, []).append((f'{t["name"]}.{s}', A[t['name']] + s - 1))
        out, ohne = [], []
        for iid in sorted(alle_ids, key=lambda i: fundstelle(i)[2]):
            f = fundstelle(iid)
            w = {k: sorted(set(wo[f[1]][k]), key=lambda x: x[1]) for k in ('blatt', 'mehr') if k in wo.get(f[1], {})}
            if not w:
                ohne.append(iid)
            out.append((f[0], (iid[:4],) + f[2], w))
        return out, ohne

    zusatz = '-probe' if nur else ''
    berichte = []
    for ausgabe in (os.path.join(a.privat, 'bau', 'mappe', a.datum, f'mappe-abi-gk{zusatz}.pdf'),
                    os.path.join(ziel, f'mappe-abi-gk-ohne{zusatz}.pdf')):
        vorn = 0
        for _ in range(3):
            A = ab(vorn)
            fund, ohne = fund_liste(A)
            stich = stichwoerter(A)
            MP.baue(T, karte + '\n' + hand + '\n' + inhalt_tex(eins, A, S, namen), MP.register_tex(stich, fund),
                    ausgabe)
            echt = MP.ziele(ausgabe)[T[0]['name'] + '.1'] - 1
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
            erwartet |= {(f'{e["ordner"]}.{p}', A[e['ordner']] + p - 1) for p in S[e['ordner']].values()}
        erwartet |= {(f'{t["name"]}.1', A[t['name']]) for t in T}
        fehler, n_links = MP.pruefe_sprungmarken(ausgabe, erwartet)
        n_fest, f_fest = feste_ziele(ausgabe, blatt)
        fehler += f_fest
        if not f_fest:
            ab_erw = [(None, A[e['ordner']] + TX[e['ordner']][x] - 1, f'Abschnitt {e["ordner"]}: {x}')
                      for e in eins for x, _ in e['stufen'] if x in TX[e['ordner']]]
            ab_erw += [(None, A[e['ordner']] + p - 1, f'Abschnitt {e["ordner"]}: {x} (Ziel)')
                       for e in eins for x, p in S[e['ordner']].items()]
            n_links, f2 = pruefe_fest(ausgabe, ab_erw)
            fehler += f2
            fehler += MP.pfeile(ausgabe, vorn)
        berichte.append(f'{ausgabe}: {seiten(ausgabe)} Seiten (Vorspann {vorn}); Blätter {len(eins)}; Fundstellen '
                        f'{len(fund)}, ohne Seite auf Blatt/Mehr {len(ohne)}'
                        + (f' ({" ".join(ohne[:12])}{" …" if len(ohne) > 12 else ""})' if ohne else '')
                        + f'; Sprungmarken {n_links}, Fehler {len(fehler)}' + (': ' + '; '.join(fehler[:8]) if fehler else ''))
        if fehler:
            print('\n'.join(berichte))
            raise SystemExit('Sprungmarken treffen nicht')
    print('\n'.join(berichte))


if __name__ == '__main__':
    main()

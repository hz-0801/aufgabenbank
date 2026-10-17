#!/usr/bin/env python3
"""kapitelblatt.py – Kapitelblatt P10 (Muster, plan.md § 10, 17.10. a und b): Abschnitt = Kapitel wie im Schulbuch,
darin alle Prüfungsoriginale 2014–2026, jede Formulierung einmal; wortgleiche einmal gedruckt, alle Jahre in der
Marke links („nach P10 ’26 · ’20 · ’17“). Kein Kern, kein Formelkasten, keine eigenen Aufgaben, kein Mehr, keine
Stufenpunkte. Jeder Abschnitt ist einzeln bestellbar (<Buchstabe>-blatt.pdf, <Buchstabe>-loesung.pdf).

  python3 werkzeuge/kapitelblatt.py --kapitel quadratische --datum 2026-10-17

Daten (nur gelesen):
  mathe-nachhilfe  msa/buchkapitel-p10.csv          blatt, Kapitel, Abschnitt, Folge, gleich_mit (Zuordnung, Prüfgrundlage;
                                                    gelesen nur Zeilen mit blatt = --kapitel)
                   msa/kapitel-p10/<kapitel>.csv    je gedruckte Aufgabe: Wortlaut (Original, Du-Form), grafik, form,
                                                    karo (Zeilen Rechenraum), loesung (Ergebnis nach „⇒“), deckt
                                                    (alle Zeilen der Zuordnung, die sie vertritt: Marke)
                   msa/msa-katalog-*.csv            stern, papier, hilfsmittel (über pruefheft.Daten)
Satz: Präambel, pfaufg, \\gtextks, \\gzwei, \\karo, Ankreuz- und Wahr/falsch-Zeilen, Lösungszeilen \\lzz aus
werkzeuge/pruefheft.py (unverändert). form (Teile mit „+“): ankreuzen, wahrfalsch, karo, zeichnen (das
Koordinatensystem ist das Antwortfeld), punkt:S₁,S₂ („S₁( __ | __ )“), werte:x₁,x₂ („x₁ = __“), linie:p(x)
(„p(x) = ____“, leer: nur Linie). Zeilen mit gleicher Spalte gruppe = Teile eines Originals: eine Nummer, a), b),
Vorspann und Grafik einmal.
Ausgabe: bau/kapitel/<datum>/<kapitel>/ (wird ersetzt) blatt.pdf, loesung.pdf, je Kapitel A-…, B-…, je Abschnitt B1-…, B2-…
(<Abschnitt>-blatt.pdf, <Abschnitt>-loesung.pdf), src/*.tex.
Prüfung im Lauf: jede Zeile der Zuordnung genau einmal vertreten, jede gedruckte Aufgabe genau einmal im Satz.
"""
import argparse, csv, os, re, shutil, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
import pruefheft as P   # noqa: E402

TITEL = {'quadratische': 'Quadratische Funktionen', 'trigonometrie': 'Trigonometrie', 'pythagoras': 'Satz des Pythagoras',
         'koerper': 'Körper', 'wachstum': 'Exponentielles Wachstum', 'potenzen': 'Potenzen und Wurzeln',
         'gleichungen': 'Gleichungen und Gleichungssysteme', 'daten': 'Daten', 'flaechen': 'Fläche und Umfang'}
KENN = {'quadratische': 'PA30', 'trigonometrie': 'PG60', 'pythagoras': 'PG50', 'koerper': 'PG90', 'wachstum': 'PA50',
        'potenzen': 'PZ15', 'gleichungen': 'PA20', 'daten': 'PS30', 'flaechen': 'PG40'}
# Kapitelblatt -> Kapitel der alten Daten (msa/zuordnung-<kapitel>.csv, FOR-Regel): 17.10. Durchsicht P10 6
DATEN = {'trigonometrie': 'dreiecke', 'pythagoras': 'dreiecke', 'potenzen': 'zahlen', 'gleichungen': 'gleichungssysteme'}   # 17.10.: Abschnitte bestellbar als „PA30 A“, „PA30 B1“, …

KAP_PRAEAMBEL = r"""
\newcommand{\gunter}[2]{\par\addvspace{6pt}\noindent{\bfseries #1\enspace #2}\par\nobreak\vspace{2pt}}
\newcommand{\gsternzeile}{\par\vspace{-4pt}\noindent{\footnotesize\color{mbgrau}* nur FOR}\par\medskip}
% 17.10.: Skizze oben bündig mit der ersten Textzeile (beide Spalten hängen an der Oberkante); der Rechenraum (Karo)
% beginnt direkt unter dem Text, links neben dem Graph, und läuft unter dem Graph über die ganze Zeile weiter
% (Streifen links = auf 5 mm aufgerundete Höhe des Graphen unter dem Text, Raster durchgehend; die Fläche des Streifens
% wird von der Karohöhe unter dem Graph abgezogen, auf 0,5 cm aufgerundet – die Gesamtfläche Rechenraum bleibt mindestens #3 × Zeile); #3 = Zeilen Karo in cm
% unter dem Graph (0 = kein Karo). Kein Verkleinern des Graphen.
\newsavebox{\gtbox}\newlength{\gWl}\newlength{\gDh}
\newcommand{\gkaroohne}[1]{\nointerlineskip\noindent\begin{tikzpicture}
  \clip (0,0) rectangle ({\linewidth-1mm},{#1*10mm});
  \draw[black!16,line width=0.3pt,step=5mm] (0,0) grid ({\linewidth},{#1*10mm});
  \end{tikzpicture}\par}
\newcommand{\gtextkaro}[3]{\sbox{\gbox}{#1}%
  \ifdim\wd\gbox>0.58\linewidth #2\par\smallskip\noindent\gpassend{\usebox{\gbox}}\par\ifnum#3>0 \karo{#3}\fi
  \else
    \setlength{\gWl}{\dimexpr\linewidth-\wd\gbox-5mm\relax}%
    \sbox{\gtbox}{\begin{minipage}[t]{\gWl}\raggedright #2\par\end{minipage}}%
    \setlength{\gDh}{\dimexpr\ht\gbox+\dp\gbox-\ht\gtbox-\dp\gtbox-6pt\relax}%
    \leavevmode
    \ifnum#3>0\ifdim\gDh>0pt
      \pgfmathsetmacro{\gxs}{floor(\gWl/5mm)*5mm}\pgfmathsetmacro{\gys}{ceil(\gDh/5mm)*5mm}%
      \begin{minipage}[t]{\gWl}\usebox{\gtbox}\par\vspace{6pt}\nointerlineskip\noindent
        \begin{tikzpicture}
        \clip (0,0) rectangle (\gxs pt,\gys pt);
        \draw[black!16,line width=0.3pt,step=5mm] (0,0) grid (\gxs pt,\gys pt);
        \end{tikzpicture}\par\end{minipage}%
    \else\usebox{\gtbox}\fi\else\usebox{\gtbox}\fi
    \hfill\begin{minipage}[t]{\wd\gbox}\vspace{-\dimexpr\ht\strutbox+2.4ex\relax}\usebox{\gbox}\end{minipage}\par
    \ifnum#3>0 \ifdim\gDh>0pt
      \pgfmathsetmacro{\gnn}{max(0,ceil(2*(#3-(\gys/28.4528)*(\gxs/\linewidth)))/2)}%
      \ifdim\gnn pt>0pt\gkaroohne{\gnn}\fi
    \else\karo{#3}\fi\fi
  \fi}
"""


# 17.10. c: Aufgabe ohne Koordinatensystem rückt innerhalb ihres Unterabschnitts vor eine Aufgabe mit Graph, damit sie das
# Seitenende füllt (Reihenfolge leicht -> schwer bleibt grob); (id, vor id)
VORZIEHEN = [('2026-FOR-K5d', '2023-OS-K4b-2'), ('2022-OS-K3b', '2023-OS-K4b-1'), ('2015-OS-B1i', '2023-OS-K4b-1')]


def vorziehen(zs):
    for i, v in VORZIEHEN:
        ids = [r['id'] for r in zs]
        if i in ids and v in ids and ids.index(i) > ids.index(v):
            r = zs.pop(ids.index(i))
            zs.insert([x['id'] for x in zs].index(v), r)
    return zs


def lies(p):
    return list(csv.DictReader(open(p, encoding='utf-8'), delimiter=';'))


def original(iid):
    return re.sub(r'-\d$', '', iid)


def jahre_marke(ids):
    js = sorted({int(i[:4]) for i in ids}, reverse=True)
    teile = [f'’{str(j)[2:]}' for j in js]
    # Rand 13 mm: je Zeile höchstens zwei Jahre
    zeilen = ['~\\pkt{}~'.join(teile[k:k + 2]) for k in range(0, len(teile), 2)]
    return 'nach~P10\\\\' + '\\\\'.join(zeilen)


def bedingungen(D, r):
    """Wie pruefheft.p_bedingungen; „FOR“ fällt weg (17.10.: Sternchen an der Nummer, siehe stern)."""
    return '\\\\'.join(x for x in P.p_bedingungen(D, {'eltern_id': original(r['id'])}) if x != 'FOR')


def stern(D, ids, eid):
    """Nur FOR: jede vertretene Aufgabe ist nur FOR (wie bisher „nur FOR“, jetzt als Sternchen an der Nummer)."""
    return all(P.stern_fuer(D, i) for i in set(ids) | {eid})


def antwort_teile(teil):
    if teil.startswith('punkt:'):
        return '\\quad '.join(P.tx(n) + '(\\linie{12mm}\\,|\\,\\linie{12mm})' for n in teil[6:].split(','))
    if teil.startswith('werte:'):
        return '\\quad '.join(P.tx(n) + ' $=$\\linie{25mm}' for n in teil[6:].split(','))
    if teil.startswith('linie:'):
        n = teil[6:].strip()
        if n.endswith('.'):   # Gleichung I., II. eines Systems: Nummer vor der Linie, kein „=“ (17.10. PA20)
            return P.tx(n) + '\\ \\linie{60mm}'
        return (P.tx(n) + ' $=$\\linie{45mm}') if n else '\\linie{60mm}'
    return ''


# 17.10. Punkt 1: Umbruch in einer Aussage, damit „wahr / falsch“ auf eigener Zeile steht (id, Wortende)
UMBRUCH = {('2018-OS-K5a', 'verschoben.')}


def inhalt(r):
    """(vorn, karo, nach, Fuß) einer Aufgabe ohne Rahmen. vorn = Text, Optionen, Wahr/falsch (links neben dem Graph, wenn
    es einen gibt); karo = Zeilen Rechenraum (0 = keiner); nach = Antwortzeilen am Ende des Rechenraums."""
    form = [t.strip() for t in (r['form'] or '').split('+') if t.strip()]
    w = r['wortlaut'].strip()
    text, optionen, rest = (P.p_wahrfalsch(w) if 'wahrfalsch' in form else P.p_kreuz(w))
    if optionen and not rest:
        optionen[-1] = re.sub(r'(\$)\.$', r'\1', optionen[-1])   # Satzpunkt nach der letzten Option weg
    t = P.tx(text)
    g = (r.get('grafik') or '').strip()
    bild = '||' in g
    kurz, lang, antw, karo = [], [], [], 0
    for teil in form:
        if teil == 'ankreuzen':
            if bild:
                lang += P.p_form_tex('', g, 'ankreuzen', [], [], 1, 1.0)
            else:
                kurz.append(''.join(f'\\pfkreuzab{{}}{{{P.tx(o)}}}' for o in optionen))
        elif teil == 'wahrfalsch':
            zs = []
            for i, o in enumerate(optionen):
                ot = P.tx(o)
                for uid, wort in UMBRUCH:
                    if uid == r['id'] and wort in ot:
                        ot = ot.replace(wort, wort + '\\\\')
                zs.append(f'\\gwahrfalsch{{{i + 1}}}{{{ot}}}')
            lang.append(''.join(zs))
            if rest:
                lang.append('\\par\\smallskip\\noindent ' + P.tx(rest))
                rest = ''
        elif teil == 'karo':
            if rest:
                lang.append('\\par\\smallskip\\noindent ' + P.tx(rest))
                rest = ''
            karo = int(r['karo'] or 3)
        elif teil == 'zeichnen':
            pass   # das Koordinatensystem ist das Antwortfeld (pruefung.md § 5)
        elif antwort_teile(teil):
            antw.append(antwort_teile(teil))
        else:
            sys.exit(f'{r["id"]}: form „{teil}“ unbekannt')
    if rest:
        kurz.append('\\par\\smallskip\\noindent ' + P.tx(rest))
    vorn = [t + ''.join(kurz)] + lang
    nach = []
    if g and not bild:
        if antw and not karo:
            vorn.append(''.join('\\par\\medskip\\noindent ' + a for a in antw))
        else:
            nach = ['\\par\\medskip\\noindent\\hfill ' + a for a in antw]
    else:
        nach = ['\\par\\medskip\\noindent\\hfill ' + a for a in antw]
    ergebnisse, _ = P.p_ergebnis(r)
    # Optionswert mit Formel ganz (p_fusswerte teilt am „=“ auch in $…$)
    return vorn, karo, nach, '; '.join(e if '$' in e else P.p_fusswerte([e], optionen, r)[0] for e in ergebnisse), g, bild


def zeilen_von(r, g_ausserhalb=None):
    """TeX-Zeilen einer Aufgabe (ohne Rahmen) und ihr Fuß."""
    vorn, karo, nach, fuss, g, bild = inhalt(r)
    if g and not bild:
        return ['\\gtextkaro{' + g + '}{' + ''.join(vorn) + '}{' + str(karo) + '}'] + nach, fuss
    out = vorn + ([f'\\karo{{{karo}}}'] if karo else []) + nach
    return out, fuss


def aufgabe_tex(D, posten, nr):
    """Ein Posten = eine Zeile oder die Teile eines Originals (gruppe)."""
    deckt = [i for r in posten for i in r['deckt'].split()] + [original(r['id']) for r in posten]
    kopf = [f'% DRUCK {r["id"]} deckt {r["deckt"] or "-"}' for r in posten]
    bed = bedingungen(D, posten[0])
    st = r'\textsuperscript{*}' if stern(D, deckt, original(posten[0]['id'])) else ''
    out = kopf + [f'\\begin{{pfaufg}}{{{jahre_marke(deckt)}}}{{{nr}.{st}}}{{{bed}}}']
    fuesse = []
    if len(posten) == 1:
        z, f = zeilen_von(posten[0])
        out += z
        fuesse.append(f)
    else:
        g = posten[0]['grafik'].strip()
        v = P.tx(posten[0]['vorspann'])
        erste = 0
        if g:
            vorn, karo, nach, f0, _, _ = inhalt(dict(posten[0], grafik=''))
            if karo:   # Teil a) mit Rechenraum: Vorspann und Teil a) links neben dem Graph, Rechenraum darunter
                erste = 1
                links = v + '\\begin{gbteil}{a)}{}{}' + ''.join(vorn) + '\\end{gbteil}'
                out += ['\\gtextkaro{' + g + '}{' + links + '}{' + str(karo) + '}'] + nach
                fuesse.append(f'a) {f0}')
            else:
                out.append('\\gtextkaro{' + g + '}{' + v + '}{0}')
        else:
            out.append(v)
        for i, r in enumerate(posten):
            if i < erste:
                continue
            z, f = zeilen_von(dict(r, grafik=''))
            b = 'abcdefgh'[i] + ')'
            out += [f'\\begin{{gbteil}}{{{b}}}{{}}{{}}'] + z + ['\\end{gbteil}']
            fuesse.append(f'{b} {f}')
    fuss = '; '.join(x for x in fuesse if x)
    if fuss:
        out.append(f'\\fusshilfe{{\\gfuss{{{nr}}}{{{fuss}}}}}')
    out.append('\\end{pfaufg}')
    return '\n'.join(out)


def posten_von(zeilen):
    out = []
    for r in zeilen:
        if r['gruppe'] and out and out[-1][0]['gruppe'] == r['gruppe']:
            out[-1].append(r)
        else:
            out.append([r])
    return out


def gliedern(zeilen, buch):
    """Kapitel in der Folge der Zuordnung -> [(Buchstabe, Kapitel, [(Unterkürzel, Abschnitt, [Zeilen])])]."""
    kapitel = list(dict.fromkeys(b['kapitel'] for b in buch))
    out = []
    for k, kap in enumerate(kapitel):
        bst = 'ABCDEFGH'[k]
        abschn = list(dict.fromkeys(b['abschnitt'] for b in buch if b['kapitel'] == kap))
        teile = []
        for j, ab in enumerate(abschn):
            zs = sorted([r for r in zeilen if r['kapitel'] == kap and r['abschnitt'] == ab],
                        key=lambda r: int(r['folge']))   # stabil: Dateifolge bei gleicher Folge
            teile.append((f'{bst}{j + 1}' if len(abschn) > 1 else '', ab, vorziehen(zs)))
        out.append((bst, kap, teile))
    return out


def kopf_tex(titel, kenn, zeile, loesung=False, stern=False):
    pre = P.KOPF.replace('\\begin{document}', P.P_PRAEAMBEL + KAP_PRAEAMBEL + '\\begin{document}')
    if loesung:
        return [pre, '\\pfheftstil',
                f'\\pflaufkopf[P10 \\pkt{{}} Prüfung]{{{P.tx(titel)} \\pkt{{}} Lösungen}}{{{kenn}}}\\pfseitevon',
                f'\\glkopf{{{P.tx(titel)}}}', '\\small']
    return [pre, '\\pfheftstil', f'\\pflaufkopf[P10 \\pkt{{}} Prüfung]{{{P.tx(titel)}}}{{{kenn}}}\\pfseitevon',
            f'\\pfheftkopf{{{P.tx(titel)}}}{{}}', '\\pfstufenzeile{' + zeile + '}'] + (['\\gsternzeile'] if stern else [])


def baue(D, titel, kenn, glied):
    """(Blatt-TeX, Lösungs-TeX) für die Kapitel in glied; Nummern ab 1."""
    zeile = ' \\pkt{} '.join(P.tx(kap) for _, kap, _ in glied)
    teile_tex, loes_tex = [], []
    nr, hat_stern = 0, False
    for bst, kap, teile in glied:
        teile_tex.append(f'\n% ===================== {bst} {kap} =====================')
        for j, (unter, ab, zs) in enumerate(teile):
            k = ''
            if j == 0:
                k += f'\\gbstvor{{{bst}}}\\pfstufekopf{{{P.tx(kap)}}}{{}}'
            if unter:
                k += f'\\gunter{{{unter}}}{{{P.tx(ab)}}}'
            teile_tex.append('\\gkopfvor{' + k + '}')
            for posten in posten_von(zs):
                nr += 1
                t = aufgabe_tex(D, posten, nr)
                hat_stern = hat_stern or '\\textsuperscript{*}' in t
                teile_tex.append(t + ('\\vspace{-6pt}' if bst == 'B' else ''))   # B enger gesetzt (17.10. c): 4 Seiten
                for i, r in enumerate(posten):
                    rr = dict(r, id='kapitel:' + r['id'])   # kein Stichwort der Mehr-Zeilen
                    b = 'abcdefgh'[i] + ')' if len(posten) > 1 else ''
                    loes_tex += P.lz_umgebung(zusammen(r, P.lz_zeilen(rr, f'{nr}.' if i == 0 else '', b)))
    blatt = kopf_tex(titel, kenn, zeile, stern=hat_stern) + teile_tex + ['\\end{document}']
    loes = kopf_tex(titel, kenn, zeile, True) + loes_tex + ['\\end{document}']
    return '\n'.join(blatt), '\n'.join(loes)


def lzz_args(z):
    """Die vier Argumente von \\lzz{…}{…}{…}{…} (Klammern verschachtelt)."""
    out, i = [], len('\\lzz')
    while i < len(z) and len(out) < 4:
        assert z[i] == '{', z
        d, j = 0, i
        while True:
            d += {'{': 1, '}': -1}.get(z[j], 0)
            j += 1
            if d == 0:
                break
        out.append(z[i + 1:j - 1])
        i = j
    return out


def zusammen(r, zeilen):
    """17.10. Punkt 8: zwei Ergebnisse einer Teilaufgabe (x₁ und x₂, S₁ und S₂, N₁ und N₂) stehen in einer Zeile mit „;“:
    die letzten k Lösungszeilen (k = Namen in werte:/punkt:) werden eine; der Ausgang rechts bleibt, gleiche entfallen."""
    k = max([len(t.split(':', 1)[1].split(',')) for t in (r['form'] or '').split('+') if t.startswith(('werte:', 'punkt:'))] or [1])
    if k < 2 or len(zeilen) < k:
        return zeilen
    a = [lzz_args(z) for z in zeilen[-k:]]
    ergs = '; '.join(x[2] for x in a)
    rechts = []
    for x in a:
        if x[3] and x[3] not in rechts:
            rechts.append(x[3])
    first = a[0]
    return zeilen[:-k] + [f'\\lzz{{{first[0]}}}{{{first[1]}}}{{{ergs}}}{{{"; ".join(rechts)}}}']


def pruefen(buch, zeilen, tex):
    """Jede Zeile der Zuordnung genau einmal vertreten (Kapitel und Abschnitt passend), jede gedruckte Aufgabe genau
    einmal im Satz. Rückgabe: Liste der Fehler."""
    fehler = []
    vertreten = {}
    for r in zeilen:
        for i in r['deckt'].split():
            vertreten.setdefault((i, r['kapitel'], r['abschnitt']), []).append(r['id'])
    for b in buch:
        n = vertreten.pop((b['id'], b['kapitel'], b['abschnitt']), [])
        if len(n) != 1:
            fehler.append(f'{b["id"]} ({b["kapitel"]}/{b["abschnitt"]}): {len(n)}-mal vertreten {n}')
    for k, v in vertreten.items():
        fehler.append(f'{k}: nicht in der Zuordnung, vertreten von {v}')
    gedruckt = re.findall(r'^% DRUCK (\S+)', tex, re.M)
    for r in zeilen:
        if gedruckt.count(r['id']) != 1:
            fehler.append(f'{r["id"]}: {gedruckt.count(r["id"])}-mal gedruckt')
    ids_satz = set(gedruckt) | {i for m in re.findall(r'^% DRUCK \S+ deckt (.*)$', tex, re.M) for i in m.split()}
    for b in buch:
        if b['id'] not in ids_satz and b['id'] not in {original(g) for g in gedruckt}:
            fehler.append(f'{b["id"]}: weder gedruckt noch in einer Marke')
    return fehler, len(gedruckt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--kapitel', required=True)
    ap.add_argument('--datum', required=True)
    ap.add_argument('--mn', default=os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe'))
    ap.add_argument('--bb', default=os.path.join(os.path.dirname(BANK), 'blattbau'))
    a = ap.parse_args()
    # Spalte blatt (17.10., Durchsicht P10 6): eine Zuordnung für alle Kapitelblätter, hier nur die eigenen Zeilen
    buch = [b for b in lies(os.path.join(a.mn, 'msa', 'buchkapitel-p10.csv')) if b.get('blatt', a.kapitel) == a.kapitel]
    zeilen = lies(os.path.join(a.mn, 'msa', 'kapitel-p10', f'{a.kapitel}.csv'))
    D = P.Daten(a.mn, DATEN.get(a.kapitel, a.kapitel))
    titel, kenn = TITEL.get(a.kapitel, a.kapitel.capitalize()), KENN.get(a.kapitel, '')
    glied = gliedern(zeilen, buch)
    ordner = os.path.join(BANK, 'bau', 'kapitel', a.datum, a.kapitel)
    shutil.rmtree(ordner, ignore_errors=True)   # Ausgabe ersetzen
    os.makedirs(os.path.join(ordner, 'src'), exist_ok=True)
    arbeit = tempfile.mkdtemp(prefix='kapitelblatt-')
    # je bestellbarem Abschnitt ein Blatt und eine Lösung: Kapitel (A, B, C, D) und Unterabschnitte (B1, B2) – 17.10. Punkt 9
    stuecke = [('', glied, kenn)] + [(g[0] + '-', [g], f'{kenn} {g[0]}') for g in glied]
    for g in glied:
        if len(g[2]) > 1:
            stuecke += [(u + '-', [(g[0], g[1], [t])], f'{kenn} {u}') for u, _, _ in g[2] for t in g[2] if t[0] == u]
    gesamt_tex, bericht, fehlerzahl = '', [], 0
    for vor, gl, kn in stuecke:
        blatt, loes = baue(D, titel, kn, gl)
        if not vor:
            gesamt_tex = blatt
        for nm, t in ((vor + 'blatt', blatt), (vor + 'loesung', loes)):
            e = P.xelatex(t, a.bb, nm, arbeit)
            open(os.path.join(ordner, 'src', nm + '.tex'), 'w', encoding='utf-8').write(t)
            if e['pdf']:
                shutil.copy(e['pdf'], os.path.join(ordner, nm + '.pdf'))
            fehlerzahl += len(e['fehler'])
            bericht.append(f'{nm}: {e["seiten"]} Seiten, Fehler {len(e["fehler"])}, Missing {e["missing"]}, '
                           f'Overfull {e["overfull"]} ({", ".join(f"{x:.0f}" for x in e["overfull_pt"] if x > 1)})'
                           + (' – ÜBER 3 SEITEN' if vor and nm.endswith('blatt') and e['seiten'] > (4 if vor == 'B-' else 3) else ''))
            bericht += ['   ' + f for f in e['fehler'][:3]]
    fehler, n = pruefen(buch, zeilen, gesamt_tex)
    print('\n'.join(bericht))
    print(f'Prüfung: {n} gedruckte Aufgaben für {len(buch)} Zeilen der Zuordnung; '
          + ('alles genau einmal' if not fehler else f'{len(fehler)} Fehler'))
    for f in fehler:
        print('  FEHLER', f)
    print('Ordner:', ordner)
    sys.exit(1 if fehler or fehlerzahl else 0)


if __name__ == '__main__':
    main()

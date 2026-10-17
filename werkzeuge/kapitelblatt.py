#!/usr/bin/env python3
"""kapitelblatt.py – Kapitelblatt P10 (Muster, plan.md § 10, 17.10. a und b): Abschnitt = Kapitel wie im Schulbuch,
darin alle Prüfungsoriginale 2014–2026, jede Formulierung einmal; wortgleiche einmal gedruckt, alle Jahre in der
Marke links („nach P10 ’26 · ’20 · ’17“). Kein Kern, kein Formelkasten, keine eigenen Aufgaben, kein Mehr, keine
Stufenpunkte. Jeder Abschnitt ist einzeln bestellbar (<Buchstabe>-blatt.pdf, <Buchstabe>-loesung.pdf).

  python3 werkzeuge/kapitelblatt.py --kapitel quadratische --datum 2026-10-17

Daten (nur gelesen):
  mathe-nachhilfe  msa/buchkapitel-p10.csv          Kapitel, Abschnitt, Folge, gleich_mit (Zuordnung, Prüfgrundlage)
                   msa/kapitel-p10/<kapitel>.csv    je gedruckte Aufgabe: Wortlaut (Original, Du-Form), grafik, form,
                                                    karo (Zeilen Rechenraum), loesung (Ergebnis nach „⇒“), deckt
                                                    (alle Zeilen der Zuordnung, die sie vertritt: Marke)
                   msa/msa-katalog-*.csv            stern, papier, hilfsmittel (über pruefheft.Daten)
Satz: Präambel, pfaufg, \\gtextks, \\gzwei, \\karo, Ankreuz- und Wahr/falsch-Zeilen, Lösungszeilen \\lzz aus
werkzeuge/pruefheft.py (unverändert). form (Teile mit „+“): ankreuzen, wahrfalsch, karo, zeichnen (das
Koordinatensystem ist das Antwortfeld), punkt:S₁,S₂ („S₁( __ | __ )“), werte:x₁,x₂ („x₁ = __“), linie:p(x)
(„p(x) = ____“, leer: nur Linie). Zeilen mit gleicher Spalte gruppe = Teile eines Originals: eine Nummer, a), b),
Vorspann und Grafik einmal.
Ausgabe: bau/kapitel/<datum>/<kapitel>/ blatt.pdf, loesung.pdf, A-blatt.pdf, A-loesung.pdf, …, src/*.tex.
Prüfung im Lauf: jede Zeile der Zuordnung genau einmal vertreten, jede gedruckte Aufgabe genau einmal im Satz.
"""
import argparse, csv, os, re, shutil, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
import pruefheft as P   # noqa: E402

TITEL = {'quadratische': 'Quadratische Funktionen'}
KENN = {'quadratische': 'QF'}

KAP_PRAEAMBEL = r"""
\newcommand{\gunter}[2]{\par\addvspace{6pt}\noindent{\bfseries #1\enspace #2}\par\nobreak\vspace{2pt}}
\newcommand{\gnurfor}{\textcolor{black}{\textbf{nur FOR}}}
"""


KARO_KLEIN = {'B': 0.35}   # Abschnitt -> Karo in cm statt 0,5 (nur Koordinatensysteme; Karo-Rechenzeilen bleiben)


def klein(g):
    """Karo-Kante je Koordinatensystem aus dem Wertebereich: Höhe höchstens ~3,4 cm, Kante zwischen 0,27 und 0,35 cm."""
    if not g:
        return g

    def ersetze(m):
        schl = m.group(1)
        y = re.search(r'ymin=(-?[\d.]+),ymax=(-?[\d.]+)', schl)
        if 'karo=0.45' in schl:
            k = 0.27
        elif y:
            k = min(0.35, max(0.27, 3.4 / (float(y.group(2)) - float(y.group(1)))))
        else:
            return m.group(0)
        return '\\begin{ksys}[' + re.sub(r'karo=[\d.]+', f'karo={k:.2f}', schl) + ']'
    return re.sub(r'\\begin\{ksys\}\[([^\]]*)\]', ersetze, g)


# 17.10. c: Aufgabe ohne Koordinatensystem rückt innerhalb ihres Unterabschnitts vor eine Aufgabe mit Graph, damit sie das
# Seitenende füllt (Reihenfolge leicht -> schwer bleibt grob); (id, vor id)
VORZIEHEN = [('2026-FOR-K5d', '2023-OS-K4b-2'), ('2015-OS-B1i', '2024-OS-K3b')]


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
    """Wie pruefheft.p_bedingungen; „FOR“ wird deutlich „nur FOR“, und nur, wenn jede vertretene Aufgabe nur FOR war."""
    eid = original(r['id'])
    b = [x for x in P.p_bedingungen(D, {'eltern_id': eid}) if x != 'FOR']
    ids = set(r['deckt'].split()) | {eid}
    if all(P.stern_fuer(D, i) for i in ids):
        b.append('\\gnurfor')
    return '\\\\'.join(b)


def antwort_teile(teil):
    if teil.startswith('punkt:'):
        return '\\quad '.join(P.tx(n) + '(\\linie{12mm}\\,|\\,\\linie{12mm})' for n in teil[6:].split(','))
    if teil.startswith('werte:'):
        return '\\quad '.join(P.tx(n) + ' $=$\\linie{25mm}' for n in teil[6:].split(','))
    if teil.startswith('linie:'):
        n = teil[6:].strip()
        return (P.tx(n) + ' $=$\\linie{45mm}') if n else '\\linie{60mm}'
    return ''


def inhalt(r):
    """(Zeilen, Fuß) einer Aufgabe ohne Rahmen."""
    form = [t.strip() for t in (r['form'] or '').split('+') if t.strip()]
    w = r['wortlaut'].strip()
    text, optionen, rest = (P.p_wahrfalsch(w) if 'wahrfalsch' in form else P.p_kreuz(w))
    if optionen and not rest:
        optionen[-1] = re.sub(r'(\$)\.$', r'\1', optionen[-1])   # Satzpunkt nach der letzten Option weg
    t = P.tx(text)
    g = (r.get('grafik') or '').strip()
    bild = '||' in g
    kurz, lang, antw = [], [], []
    for teil in form:
        if teil == 'ankreuzen':
            if bild:
                lang += P.p_form_tex('', g, 'ankreuzen', [], [], 1, 1.0)
            else:
                kurz.append(''.join(f'\\pfkreuzab{{}}{{{P.tx(o)}}}' for o in optionen))
        elif teil == 'wahrfalsch':
            lang.append(''.join(f'\\gwahrfalsch{{{i + 1}}}{{{P.tx(o)}}}' for i, o in enumerate(optionen)))
            if rest:
                lang.append('\\par\\smallskip\\noindent ' + P.tx(rest))
                rest = ''
        elif teil == 'karo':
            if rest:
                lang.append('\\par\\smallskip\\noindent ' + P.tx(rest))
                rest = ''
            lang.append(f'\\karo{{{int(r["karo"] or 3)}}}')
        elif teil == 'zeichnen':
            pass   # das Koordinatensystem ist das Antwortfeld (pruefung.md § 5)
        elif antwort_teile(teil):
            antw.append(antwort_teile(teil))
        else:
            sys.exit(f'{r["id"]}: form „{teil}“ unbekannt')
    if rest:
        kurz.append('\\par\\smallskip\\noindent ' + P.tx(rest))
    out = []
    if g and not bild:
        neben = t + ''.join(kurz)
        if antw and 'karo' not in form:
            neben += ''.join('\\par\\medskip\\noindent ' + a for a in antw)
            antw = []
        out.append('\\gtextks{' + g + '}{' + neben + '}')
    else:
        out.append(t + ''.join(kurz))
    out += lang
    out += ['\\par\\medskip\\noindent\\hfill ' + a for a in antw]
    ergebnisse, _ = P.p_ergebnis(r)
    # Optionswert mit Formel ganz (p_fusswerte teilt am „=“ auch in $…$)
    return out, '; '.join(e if '$' in e else P.p_fusswerte([e], optionen, r)[0] for e in ergebnisse)


def aufgabe_tex(D, posten, nr):
    """Ein Posten = eine Zeile oder die Teile eines Originals (gruppe)."""
    deckt = [i for r in posten for i in r['deckt'].split()] + [original(r['id']) for r in posten]
    kopf = [f'% DRUCK {r["id"]} deckt {r["deckt"] or "-"}' for r in posten]
    bed = bedingungen(D, dict(posten[0], deckt=' '.join(deckt)))
    out = kopf + [f'\\begin{{pfaufg}}{{{jahre_marke(deckt)}}}{{{nr}.}}{{{bed}}}']
    fuesse = []
    if len(posten) == 1:
        z, f = inhalt(posten[0])
        out += z
        fuesse.append(f)
    else:
        g = posten[0]['grafik'].strip()
        v = P.tx(posten[0]['vorspann'])
        out.append('\\gtextks{' + g + '}{' + v + '}' if g else v)
        for i, r in enumerate(posten):
            z, f = inhalt(dict(r, grafik=''))
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


def kopf_tex(titel, kenn, zeile, loesung=False):
    pre = P.KOPF.replace('\\begin{document}', P.P_PRAEAMBEL + KAP_PRAEAMBEL + '\\begin{document}')
    if loesung:
        return [pre, '\\pfheftstil',
                f'\\pflaufkopf[P10 \\pkt{{}} Prüfung]{{{P.tx(titel)} \\pkt{{}} Lösungen}}{{{kenn}}}\\pfseitevon',
                f'\\glkopf{{{P.tx(titel)}}}', '\\small']
    return [pre, '\\pfheftstil', f'\\pflaufkopf[P10 \\pkt{{}} Prüfung]{{{P.tx(titel)}}}{{{kenn}}}\\pfseitevon',
            f'\\pfheftkopf{{{P.tx(titel)}}}{{}}', '\\pfstufenzeile{' + zeile + '}']


def baue(D, titel, kenn, glied):
    """(Blatt-TeX, Lösungs-TeX) für die Kapitel in glied; Nummern ab 1."""
    zeile = ' \\pkt{} '.join(P.tx(kap) for _, kap, _ in glied)
    blatt = kopf_tex(titel, kenn, zeile)
    loes = kopf_tex(titel, kenn, zeile, True)
    nr = 0
    for bst, kap, teile in glied:
        blatt.append(f'\n% ===================== {bst} {kap} =====================')
        for j, (unter, ab, zs) in enumerate(teile):
            k = ''
            if j == 0:
                k += f'\\gbstvor{{{bst}}}\\pfstufekopf{{{P.tx(kap)}}}{{}}'
            if unter:
                k += f'\\gunter{{{unter}}}{{{P.tx(ab)}}}'
            blatt.append('\\gkopfvor{' + k + '}')
            for posten in posten_von(zs):
                if bst in KARO_KLEIN:   # 17.10. c: kleineres Karo, wo der Wertebereich klein ist (Rechenraum bleibt)
                    posten = [dict(r, grafik=klein(r['grafik'])) for r in posten]
                nr += 1
                blatt.append(aufgabe_tex(D, posten, nr) + ('\\vspace{-6pt}' if bst in KARO_KLEIN else ''))
                for i, r in enumerate(posten):
                    rr = dict(r, id='kapitel:' + r['id'])   # kein Stichwort der Mehr-Zeilen
                    b = 'abcdefgh'[i] + ')' if len(posten) > 1 else ''
                    loes += P.lz_umgebung(P.lz_zeilen(rr, f'{nr}.' if i == 0 else '', b))
    blatt.append('\\end{document}')
    loes.append('\\end{document}')
    return '\n'.join(blatt), '\n'.join(loes)


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
    buch = lies(os.path.join(a.mn, 'msa', 'buchkapitel-p10.csv'))
    zeilen = lies(os.path.join(a.mn, 'msa', 'kapitel-p10', f'{a.kapitel}.csv'))
    D = P.Daten(a.mn, a.kapitel)
    titel, kenn = TITEL.get(a.kapitel, a.kapitel.capitalize()), KENN.get(a.kapitel, '')
    glied = gliedern(zeilen, buch)
    ordner = os.path.join(BANK, 'bau', 'kapitel', a.datum, a.kapitel)
    os.makedirs(os.path.join(ordner, 'src'), exist_ok=True)
    arbeit = tempfile.mkdtemp(prefix='kapitelblatt-')
    stuecke = [('', glied)] + [(g[0] + '-', [g]) for g in glied]
    gesamt_tex, bericht, fehlerzahl = '', [], 0
    for vor, gl in stuecke:
        blatt, loes = baue(D, titel, kenn, gl)
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
                           + (' – ÜBER 3 SEITEN' if vor and nm.endswith('blatt') and e['seiten'] > 3 else ''))
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

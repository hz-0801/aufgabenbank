#!/usr/bin/env python3
"""pruefheft.py – setzt ein Prüfungsheft (Skript) aus Daten, ohne Modell (v0.2, 06.10.2026).

Bestellung auf der Befehlszeile, Ausgabe .tex und PDF (Heft und eigene Lösungsdatei) nach
bau/pruefheft/<kapitel>-<art>[-p<n>|-fokus-<wort>][-ebr]-<datum>/ (Unterordner src/ und pdf/).

  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal
  python3 werkzeuge/pruefheft.py --kapitel prozent --art schwach
  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --portion 1
  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --fokus grundwert
  --kurs EBR|FOR (Vorgabe FOR): Heft ab 2026 nach Kurs (Fundstellen), * an FOR-only-Aufgaben
  Pfade: --mn ../mathe-nachhilfe --bb ../blattbau (Voreinstellung: Nachbarordner des Repos)

Daten (alle gelesen; geschrieben wird nur bau/register.csv, eine Zeile je Bau):
  mathe-nachhilfe  msa/zuordnung-<kapitel>.csv     Stufen in Lernreihenfolge, Kern, Katalog-ids,
                                                  Bank-Sprossen
                   msa/wortlaut-eigen-<kapitel>.csv eigener Wortlaut (Du-Form), Abbildung, Punkte,
                                                  Fundstelle, Zwischenfragen
                   msa/skript-zuschnitt-p10.csv     Abschnitt, Neben-/Hauptplatz
                   msa/msa-katalog-*.csv            jahr, punkte, stern, kurzloesung, zwischenergebnis,
                                                  voraussetzungen, bemerkung (EBR-Zwilling)
                   msa/<kapitel>-zusatz.jsonl       Zusatzaufgaben (Bankformat)
                   katalog/prozentrechnung.md       nur die Zeilen „Vor Einheit …“ der Erkennungsschritte
  aufgabenbank     bank/<eintrag>/e*.jsonl, zone.jsonl   Aufgaben mit loesung (Feld bild: Aufgabenbild)
  blattbau         mathblatt.sty (ab 2026-10-06: pfnr, \\pfstufekopf, \\pfgruppe, \\pfab)

Regeln: Arbeitsliste bau/pruefheft/beschluesse-2026-10-06.md (Punkte 1–29), ziel.md § 2/§ 4,
bankblatt.md v5.6. Die Nummer des Beschlusses steht im Kommentar; was das Programm selbst
entscheidet, steht als „Entscheidung“ daneben.
"""
import argparse, csv, datetime, glob, json, os, re, shutil, subprocess, sys, tempfile
from collections import Counter, OrderedDict

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)

# ---------------------------------------------------------------------------
# Text: Katalog/Wortlaut sind Klartext mit $…$-Stellen; Bank ist LaTeX.
# ---------------------------------------------------------------------------
UNI_MATH = {'⇒': r'\Rightarrow', '≈': r'\approx', '−': '-', '≤': r'\le', '≥': r'\ge',
            'π': r'\pi', '≙': r'\mathrel{\widehat{=}}', 'α': r'\alpha', 'β': r'\beta', '→': r'\to', '⇔': r'\Leftrightarrow',
            '·': r'\cdot', '°': r'^\circ'}
SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')


def teile_math(s):
    """Zerlegt s in [(ist_math, text)] an $…$."""
    out, cur, m = [], '', False
    i = 0
    while i < len(s):
        c = s[i]
        if c == '$' and (i == 0 or s[i - 1] != '\\'):
            out.append((m, cur)); cur = ''; m = not m
        else:
            cur += c
        i += 1
    out.append((m, cur))
    return [(a, b) for a, b in out if b]


def textteil(t, latex):
    if not latex:
        t = re.sub(r'(?<!\\)%', r'\\%', t)
        t = t.replace('&', r'\&').replace('#', r'\#').replace('_', r'\_')
    # Brüche a/b in der Zeile gestapelt (ziel.md § 2: \tfrac)
    t = re.sub(r'(?<![\d,])(\d+)/(\d+)(?![\d,])', r'$\\tfrac{\1}{\2}$', t)
    # hochgestellte Ziffern
    t = re.sub(r'([⁰¹⁴⁵⁶⁷⁸⁹][⁰¹²³⁴⁵⁶⁷⁸⁹]*|[²³][⁰¹²³⁴⁵⁶⁷⁸⁹]+)',
               lambda m: '$^{%s}$' % m.group(1).translate(SUP), t)
    for k, v in UNI_MATH.items():
        if k == '·':
            continue  # Mittelpunkt hat die Schrift
        if k == '°':
            continue
        t = t.replace(k, '$' + v + '$')
    t = t.replace('$$', '')
    return t


def tx(s, latex=False):
    """Klartext (latex=False) oder Bank-LaTeX (latex=True) -> sicherer LaTeX-Text."""
    if not s:
        return ''
    res = []
    for m, t in teile_math(s):
        if m:
            for k, v in UNI_MATH.items():
                t = t.replace(k, ' ' + v + ' ')
            t = t.replace(r'\frac', r'\tfrac')
            res.append('$' + t + '$')
        else:
            res.append(textteil(t, latex))
    return ''.join(res).replace('$$', '')


# ---------------------------------------------------------------------------
# Daten laden
# ---------------------------------------------------------------------------
def lies_csv(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter=';'))


def lies_jsonl(p):
    with open(p, encoding='utf-8') as f:
        return [json.loads(l) for l in f if l.strip()]


class Daten:
    def __init__(self, mn, kapitel):
        self.mn = mn
        self.kapitel = kapitel
        self.kat = {}
        for p in sorted(glob.glob(os.path.join(mn, 'msa', 'msa-katalog-*.csv'))):
            for r in lies_csv(p):
                self.kat[r['id']] = r
        self.pruefjahre = sorted({(r['jahr']) for r in self.kat.values()
                                  if r['papier'] in ('OS', 'FOR')})
        self.zu = lies_csv(os.path.join(mn, 'msa', f'zuordnung-{kapitel}.csv'))
        self.zwilling_zu = {}
        for z in self.zu:
            for paar in (z.get('ebr_zwilling') or '').split():
                f, e = paar.split('=')
                self.zwilling_zu[f] = e
        wl = lies_csv(os.path.join(mn, 'msa', f'wortlaut-eigen-{kapitel}.csv'))
        self.wort = OrderedDict((r['id'], r) for r in wl)
        self.zuschnitt = lies_csv(os.path.join(mn, 'msa', 'skript-zuschnitt-p10.csv'))
        self.bank = {}
        self.zone = []
        for ein in ('prozentrechnung', 'zinsrechnung'):
            for p in sorted(glob.glob(os.path.join(BANK, 'bank', ein, 'e*.jsonl'))):
                for r in lies_jsonl(p):
                    self.bank[r['id']] = r
        zp = os.path.join(BANK, 'bank', 'prozentrechnung', 'zone.jsonl')
        self.zone = lies_jsonl(zp)
        self.zone_alle = []
        for ein in ('prozentrechnung', 'zinsrechnung'):
            zp = os.path.join(BANK, 'bank', ein, 'zone.jsonl')
            if os.path.exists(zp):
                self.zone_alle += lies_jsonl(zp)
        # Punkte der Bankzeilen, die eine ganze Original-Teilaufgabe abbilden (bank.md „Punkte“)
        self.punkte = {}
        pp = os.path.join(BANK, 'bank', '_punkte.csv')
        if os.path.exists(pp):
            for r in lies_csv(pp):
                if r['umfang'] == 'ganz' and r['punkte']:
                    self.punkte[r['id']] = r['punkte']
        # EBR-Zwilling eines FOR-Teils 2026 („Wortgleich mit 2026-FOR-…“ in bemerkung)
        self.ebr_zwilling = {}
        for r in self.kat.values():
            if r['papier'] == 'EBR':
                m = re.search(r'Wortgleich mit (\d{4}-FOR-\w+?)[.)\s]', r['bemerkung'] + ' ')
                if m:
                    self.ebr_zwilling[m.group(1)] = r['id']
        self.ebr_zwilling.update(self.zwilling_zu)   # Zuordnung geht vor (Reparatur Punkt 13)
        self.zusatz = {}
        for p in glob.glob(os.path.join(mn, 'msa', '*-zusatz.jsonl')):
            name = os.path.basename(p)
            self.zusatz['msa/' + name] = lies_jsonl(p)
        self.befunde = []   # Datenformat-Erkenntnisse während des Baus

    def befund(self, s):
        if s not in self.befunde:
            self.befunde.append(s)


# ---------------------------------------------------------------------------
# Abbildungen aus der Beschreibung (Feld abbildung) – Typ am Anfang erkannt
# ---------------------------------------------------------------------------
def zahl(s):
    return float(s.replace(',', '.'))


def abb_saeulen(desc, D, iid):
    kopf, _, rest = desc.partition(':')
    paare = re.findall(r'([A-Za-zÄÖÜäöü0-9]+):?\s+(\d+(?:,\d+)?)', rest)
    if len(paare) < 2:
        D.befund(f'{iid}: Säulendiagramm ohne lesbare Wertepaare')
        return ''
    ymin = 0
    m = re.search(r'Achse beginnt bei (\d+)', kopf)
    if m:
        ymin = int(m.group(1))
    ylabel = re.sub(r'Säulendiagramm|\(.*?\)|[,]', '', kopf).strip() or 'Anzahl'
    werte = [zahl(v) for _, v in paare]
    ymax = max(werte) * 1.2
    if ymin:
        ymax = ymin + (max(werte) - ymin) * 1.25
    coords = ' '.join(f'({k},{zahl(v)})' for k, v in paare)
    cats = ','.join(k for k, _ in paare)
    breite = min(15, 1.3 * len(paare) + 2)
    return (r'\begin{tikzpicture}\begin{axis}[ybar,width=%.1fcm,height=4.6cm,ymin=%s,ymax=%.2f,'
            r'symbolic x coords={%s},xtick=data,enlarge x limits=0.08,bar width=6mm,'
            r'ylabel={%s},ylabel style={font=\small},tick label style={font=\small},'
            r'nodes near coords,every node near coord/.append style={font=\scriptsize,'
            r'/pgf/number format/.cd,use comma,1000 sep={}},'
            r'ymajorgrids,grid style={mbgitter}]'
            r'\addplot[fill=mbkasten,draw=black] coordinates {%s};\end{axis}\end{tikzpicture}'
            % (breite, ymin, ymax, cats, tx(ylabel), coords))


def abb_tabelle_spalten(desc, D, iid):
    # „Tabelle (Spalten 11. bis 15. Geburtstag): Zinsen –, 4,00 €, …; Einzahlung je 200,00 €; …“
    m = re.match(r'Tabelle \(Spalten (\d+)\. bis (\d+)\. (\w+)\):\s*(.*)', desc)
    if not m:
        return None
    a, b, wort, rest = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    n = b - a + 1
    kopf = ' & '.join([wort] + [f'{k}.' for k in range(a, b + 1)])
    zeilen = []
    for teil in rest.split(';'):
        teil = teil.strip()
        mm = re.match(r'([A-Za-zÄÖÜäöüß ]+?)\s+(je\s+)?(.*)', teil)
        if not mm:
            continue
        name, je, werte = mm.group(1), mm.group(2), mm.group(3)
        if je:
            vals = [werte] * n
        else:
            vals = [v.strip() for v in werte.split(', ')]
        if len(vals) != n:
            D.befund(f'{iid}: Tabellenzeile „{name}“ mit {len(vals)} statt {n} Werten')
            return ''
        vals = [r'\leerzelle' if v == 'leer' else tx(v) for v in vals]
        zeilen.append(' & '.join([name] + vals))
    return r'\sachtabelle{l%s}{%s}{%s}' % ('r' * n, kopf, r'\\ '.join(zeilen))


def abb_dreieck(desc):
    w = re.search(r'waagerechte Kathete (\d+(?:,\d+)?) ?(\w+)', desc)
    s = re.search(r'senkrechte Kathete[^\d]*(\d+(?:,\d+)?) ?(\w+)', desc)
    h = re.search(r'Hypotenuse (\w+)', desc)
    a = re.search(r'Anstiegswinkel (\S+)', desc)
    lw = f'{w.group(1)} {w.group(2)}' if w else ''
    ls = f'{s.group(1)} {s.group(2)}' if s else ''
    lh = h.group(1) if h else ''
    la = a.group(1) if a else ''
    # nicht maßstabsgerecht: Höhe überzeichnet, damit die Stufe sichtbar bleibt
    return (r'\begin{tikzpicture}[line width=0.6pt]\draw (0,0) -- (6,0) -- (6,1.4) -- cycle;'
            r'\draw (5.7,0) -- (5.7,0.3) -- (6,0.3);'
            r'\node[below,font=\small] at (3,0) {%s};\node[right,font=\small] at (6,0.7) {%s};'
            r'\node[above left,font=\small] at (3,0.7) {%s};\node[font=\small] at (1.1,0.12) {%s};'
            r'\node[font=\scriptsize,mbgrau,anchor=west] at (0,-0.75) {nicht maßstabsgerecht};'
            r'\end{tikzpicture}' % (tx(lw), tx(ls), tx('$' + lh + '$' if lh else ''),
                                    tx(la)))


def abb_tabelle_zeilen(desc):
    # „Tabelle: Kopf | Kopf; Zeile | Wert; …“ (Reparatur 06.10., Punkt 10)
    teile = [t.strip() for t in desc.split(':', 1)[1].split(';') if t.strip()]
    zeilen = [[tx(z.strip()) for z in t.split(' | ')] for t in teile]
    n = max(len(z) for z in zeilen)
    zeilen = [z + [''] * (n - len(z)) for z in zeilen]
    return r'\sachtabelle{l%s}{%s}{%s}' % ('r' * (n - 1), ' & '.join(zeilen[0]),
                                          r'\\ '.join(' & '.join(z) for z in zeilen[1:]))


def abb_saeulenraster(desc):
    # „Säulenraster (14 Kästchen hoch): y-Achse …; x-Achse …; Spanisch 7,8; ___ 10,5; Arabisch –“
    h = int(re.search(r'\((\d+) Kästchen hoch\)', desc).group(1))
    teile = [t.strip() for t in desc.split(':', 1)[1].split(';')]
    ylab = re.sub(r'^y-Achse\s*|\s*ohne Einteilung', '', teile[0])
    xlab = re.sub(r'^x-Achse\s*', '', teile[1])
    saeulen = [re.match(r'(.*\S)\s+(\S+)$', t).groups() for t in teile[2:]]
    b = 5 * len(saeulen) + 1
    out = [r'\begin{tikzpicture}[x=0.45cm,y=0.45cm]',
           r'\draw[mbgitter,line width=0.3pt] (0,0) grid (%d,%d);' % (b, h),
           r'\draw[line width=0.7pt,->] (0,0) -- (0,%.1f) node[above,font=\small] {%s};' % (h + 0.6, tx(ylab)),
           r'\draw[line width=0.7pt,->] (0,0) -- (%.1f,0) node[right,font=\small] {%s};' % (b + 0.6, tx(xlab))]
    for i, (name, wert) in enumerate(saeulen):
        x = 2 + 5 * i
        if wert not in ('–', '-'):
            out.append(r'\fill[mbkasten,draw=black] (%d,0) rectangle (%d,%s);' % (x, x + 2, wert.replace(',', '.')))
        lab = r'\leerzelle' if name.startswith('_') else tx(name)
        out.append(r'\node[below=2pt,font=\small] at (%d,0) {%s};' % (x + 1, lab))
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


def abbildung(desc, D, iid, vorspann_abb=''):
    """Liefert (latex, ankreuztabelle?) zur Beschreibung; '' wenn keine nötig."""
    d = (desc or '').strip()
    if not d or d.startswith('keine'):
        return ''
    if d.startswith('Tabelle:'):
        return abb_tabelle_zeilen(d)
    if d.startswith('Säulenraster'):
        return abb_saeulenraster(d)
    if 'wie im Text' in d:
        return ''   # Werte stehen im Wortlaut; Entscheidung: keine zweite Darstellung
    if d.startswith('Tabelle aus dem Vorspann'):
        return vorspann_abb
    if d.startswith('Säulendiagramm'):
        return abb_saeulen(d, D, iid)
    if d.startswith('Tabelle (Spalten'):
        t = abb_tabelle_spalten(d, D, iid)
        if t is not None:
            return t
    if d.startswith('leerer Kreis'):
        return r'\kreisleer[2]'
    if d.startswith('rechtwinkliges Dreieck'):
        return abb_dreieck(d)
    if d.startswith('Ankreuztabelle'):
        return 'ANKREUZTABELLE'
    D.befund(f'{iid}: Abbildung „{d[:40]}…“ hat keinen bekannten Typ – nicht gesetzt')
    return ''


# ---------------------------------------------------------------------------
# Aufgaben
# ---------------------------------------------------------------------------
NIVEAU = {'I': 1.5, 'II': 2.5, 'III': 3.5}
HOEHE = {'vorstufe': 0.5, 'grundfall': 1.0, 'sprosse': 1.2, 'pruefung': 2.0, 'pflicht': 3.0}


class Aufgabe:
    def __init__(self):
        self.art = ''          # echt | bank | zone
        self.id = ''
        self.text = ''         # LaTeX
        self.optionen = []     # Ankreuzzeilen (LaTeX)
        self.optionen_kurz = False
        self.abb = ''
        self.punkte = ''
        self.fund = ''
        self.kurz = ''         # LaTeX
        self.zw = []           # LaTeX-Zwischenergebnisse
        self.zw_wort = []      # Wort je Zwischenergebnis (schwach)
        self.tipp = ''
        self.zf = []           # Zwischenfragen (Klartext -> LaTeX)
        self.rang = 1.0
        self.jahr = 0
        self.neben = ''        # „kennst du aus …“
        self.stichwoerter = []
        self.kreuz = False
        self.antwort = ''
        self.form = ''
        self.pflicht = ''
        self.loesung_roh = ''
        self.bild = ''
        self.orig = ''
        self.schritte = ''
        self.hrang = 2
        self.stern = False
        self.zw_roh = []


def ankreuz_zerlegen(text):
    """„… an: A / B / C.“ -> (Vortext, [A, B, C])"""
    if ' / ' not in text:
        return text, []
    i = text.rfind(': ', 0, text.find(' / '))
    if i < 0:
        return text, []
    vor, opt = text[:i + 1], text[i + 2:]
    opts = [o.strip() for o in opt.split(' / ')]
    if opts and opts[-1].endswith('.'):
        opts[-1] = opts[-1][:-1]
    return vor, opts


def aussagen_zerlegen(text):
    """„… Aussagen: „A“ „B“ Kreuzen Sie …“ -> (Vortext, [„A“, „B“], Nachtext)"""
    qs = list(re.finditer(r'„[^“]*“', text))
    if len(qs) < 2:
        return None
    vor = text[:qs[0].start()].rstrip()
    nach = text[qs[-1].end():].strip()
    return vor, [q.group(0) for q in qs], nach


WORT_SCHLUESSEL = [('Mittelpunktswinkel', 'Winkel'), ('wie viele', 'Anzahl'),
                   ('Wachstumsfaktor', 'Wachstumsfaktor'), ('Prozentpunkte', 'Prozentpunkte'),
                   ('Dezimalzahl', 'Dezimalzahl'), ('Nenner 100', 'Bruch'), ('Bruch', 'Bruch'),
                   ('Quotient', 'Anteil'), ('Anteil', 'Anteil'), ('Verhältnis', 'Verhältnis'),
                   ('Mittelpunktswinkel', 'Winkel'), ('ein Drittel', 'ein Drittel'),
                   ('Fläche', 'Fläche'), ('Summe', 'Summe'), ('Differenz', 'Unterschied'),
                   ('um wie viel', 'Unterschied'), ('um wie viele', 'Unterschied'),
                   ('Rabatt', 'Rabatt'), ('wie viele', 'Anzahl'), ('Prozent', 'Prozent'),
                   ('Verbrauch', 'Verbrauch'), ('Drittel', 'Drittel'), ('Betrag', 'Betrag'),
                   ('entspricht', 'Zuordnung')]


def wort_aus(frage, ersatz):
    for k, w in WORT_SCHLUESSEL:
        if k.lower() in (frage or '').lower():
            return w
    return ersatz


def hat_wort(z):
    """Beginnt das Zwischenergebnis mit einem Wort (nicht mit Zahl/Formel)?"""
    z = z.strip()
    if re.match(r'^[^$:]{0,25}[A-Za-zÄÖÜäöüß]{3,}[^$:]{0,10}:', z):
        return True   # Beschriftung vor dem Doppelpunkt („1 Karte: …“) ist schon das Wort
    m = re.match(r'([A-Za-zÄÖÜäöüß]{3,}(?: [a-zäöüß]{3,})?)\b', z)
    if not m:
        return False
    return not re.match(r'^[A-Z] =', z)


def wort_fuer(z, i, zf, n_zw, stufe):
    """Wort vor einem Zwischenergebnis („schwach“: Wort + Ansatz ⇒ Wert). Reihenfolge
    (Entscheidung): Formelbuchstabe, passende Zwischenfrage (nur bei gleicher Zahl), Wort der
    Stufe, Art der Rechnung."""
    m = re.match(r'\s*\$?\s*([GWp])\s*=', z)
    if m:
        return {'G': 'Grundwert', 'W': 'Prozentwert', 'p': 'Prozentsatz'}[m.group(1)]
    if zf and len(zf) == n_zw and i < len(zf):
        w = wort_aus(zf[i], '')
        if w:
            return w
    sw = stufenwort(stufe)
    if sw != 'Rechnung':
        return sw
    if 'frac' in z or '/' in z:
        return 'Bruch'
    if ':' in z:
        return 'Anteil'
    if '−' in z or ' - ' in z:
        return 'Unterschied'
    return 'Rechnung'


def stufenwort(stufe):
    for w in ('Grundwert', 'Prozentwert', 'Prozentsatz', 'Zinssatz', 'Zinsen', 'Zinseszins'):
        if w.lower() in stufe.lower():
            return w
    return 'Rechnung'


def vorspann_gilt(vs, teil):
    """Der Vorspann gilt nur für die Teilaufgaben, die seine Anmerkung nennt („Vorspann für 3a und
    3b“); ohne Angabe für alle. (Datenformat: ein eigenes Feld wäre sicherer.)"""
    m = re.search(r'Vorspann für ([^;]*)', vs.get('anmerkung', ''))
    if not m:
        return True
    return teil in re.findall(r'\d+([a-z])', m.group(1))


def echt_aufgabe(D, iid, stufe):
    w = D.wort.get(iid)
    k = D.kat.get(iid)
    if not w or not k:
        D.befund(f'{iid}: fehlt im Wortlaut oder Katalog – nicht gesetzt')
        return None
    a = Aufgabe()
    a.art, a.id = 'echt', iid
    pre = iid[:-1]
    vs = D.wort.get(pre)
    vs_abb = ''
    text = w['wortlaut']
    if vs and vs['teil'] == 'vorspann' and vorspann_gilt(vs, w['teil']):
        vs_abb = abbildung(vs['abbildung'], D, pre)
        text = vs['wortlaut'] + ' ' + text
        a.vorspann = vs
    antwort = k.get('antwort', '')
    abb = abbildung(w['abbildung'], D, iid, vs_abb)
    if abb == '' and vs_abb and 'wie im Text' not in (w['abbildung'] or '') and not w['abbildung']:
        abb = vs_abb
    if abb == 'ANKREUZTABELLE':
        vor, opts = ankreuz_zerlegen(text)
        zeilen = r' \\ '.join(f'{tx(o)} & $\\square$ & $\\square$' for o in opts)
        abb = (r'\begingroup\renewcommand{\arraystretch}{1.5}\begin{tabular}{|l|c|c|}\hline '
               r'Term & richtig & falsch\\ \hline %s \\ \hline\end{tabular}\endgroup' % zeilen)
        text = vor
    elif 'Kreuz' in antwort:
        vor, opts = ankreuz_zerlegen(text)
        if opts:
            text = vor
            a.optionen = [tx(o) for o in opts]
            a.optionen_kurz = all(len(o) < 14 for o in opts)
        else:
            z = aussagen_zerlegen(text)
            if z:
                vor, qs, nach = z
                text = vor + ' ' + nach
                a.optionen = [tx(q) for q in qs]
    a.text = tx(text)
    a.abb = abb
    a.kreuz = antwort.strip() == 'Kreuz'
    a.schritte = k.get('schritte', '') or '1'
    a.punkte = w['punkte'] or k['punkte']
    a.fund = w['fundstelle']
    a.jahr = int(k['jahr'])
    a.rang = NIVEAU.get(k['niveau_geschaetzt'], 2.5)
    teile, werte = [], set()
    for x in k['kurzloesung'].split(' | '):
        x = x.strip()
        wv = re.split(r'≈|=', x)[-1].strip()
        if x and wv not in werte:   # „Sektor ≈ 52° | ≈ 52°“ nur einmal (Reparatur Punkt 6)
            teile.append(x); werte.add(wv)
    a.kurz = '; '.join(tx(x) for x in teile)
    if not k['kurzloesung']:
        D.befund(f'{iid}: kurzloesung leer')
    zw = [x.strip() for x in k['zwischenergebnis'].split(' ; ') if x.strip()]
    a.zf = [x.strip() for x in w.get('zwischenfragen', '').split(' ; ') if x.strip()]
    a.zw = [tx(z) for z in zw]
    a.zw_roh = zw
    for i, z in enumerate(zw):
        a.zw_wort.append('' if hat_wort(z) else wort_fuer(z, i, a.zf, len(zw), stufe))
    a.stichwoerter = [s for s in k['stichwoerter'].split('|') if s]
    # Tipp: ein Stichwort, das nicht schon im Stufennamen steht
    for s in a.stichwoerter:
        if s.lower() not in stufe.lower() and s.lower() != 'prozent':
            a.tipp = s
            break
    if not a.tipp and a.stichwoerter:
        a.tipp = a.stichwoerter[0]
    return a


# --- Bank-Lösung zerlegen ---------------------------------------------------
def oben_split(s, sep):
    """Teilt s an sep außerhalb von $…$ und Klammern."""
    teile, cur, m, tiefe = [], '', False, 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == '$' and (i == 0 or s[i - 1] != '\\'):
            m = not m
        elif not m and c == '(':
            tiefe += 1
        elif not m and c == ')':
            tiefe = max(0, tiefe - 1)
        if not m and tiefe == 0 and s.startswith(sep, i):
            teile.append(cur); cur = ''; i += len(sep); continue
        cur += c
        i += 1
    teile.append(cur)
    return [t.strip() for t in teile if t.strip()]


def satz_split(s):
    """Teilt an Satzende („. “ vor Großbuchstaben) außerhalb von $…$."""
    teile, cur, m = [], '', False
    for i, c in enumerate(s):
        if c == '$' and (i == 0 or s[i - 1] != '\\'):
            m = not m
        cur += c
        if not m and c == '.' and re.match(r'\s+[A-ZÄÖÜ]', s[i + 1:i + 3] or ''):
            teile.append(cur); cur = ''
    teile.append(cur)
    return [x.strip() for x in teile if x.strip()]


def klammern_heraus(s):
    """Entfernt Klammern auf oberster Ebene außerhalb von $…$; gibt (rest, [inhalte])."""
    rest, inh, m, tiefe, cur = '', [], False, 0, ''
    for i, c in enumerate(s):
        if c == '$' and (i == 0 or s[i - 1] != '\\'):
            m = not m
        if not m and c == '(':
            tiefe += 1
            if tiefe == 1:
                cur = ''; continue
        if not m and c == ')' and tiefe > 0:
            tiefe -= 1
            if tiefe == 0:
                inh.append(cur); continue
        if tiefe > 0:
            cur += c
        else:
            rest += c
    return re.sub(r'\s+', ' ', rest).strip(), inh


FEHLERWORT = ('nicht ', 'wären', 'wäre ', 'Restpreis', 'Kontrolle', 'statt')


def bank_loesung(l):
    """Bank-loesung -> (kurz, [zwischen]); Fehlerhinweise und Antwortsätze fallen weg."""
    l = l.strip()
    rest, inh = klammern_heraus(l)
    extra = []
    for x in inh:
        for y in oben_split(x, ';'):
            if not any(f in y for f in FEHLERWORT):
                extra.append(y)
    seg = []
    for s in oben_split(rest, ';'):
        seg.extend(satz_split(s))
    seg = [s.rstrip('.').strip() for s in seg if s.strip().rstrip('.')]
    if not seg:
        return l, []
    # Schluss nach Gedankenstrich ist das Urteil
    letzte = oben_split(seg[-1], ' – ')
    urteil = ''
    if len(letzte) > 1:
        seg[-1] = letzte[0]
        urteil = ' – '.join(letzte[1:])
    # Antwortsatz ohne Rechnung am Ende weg (kein Antwortsatz auf dem Lösungsblatt)
    if len(seg) > 1 and not re.search(r'=|≈|\\approx|<|>|\\le|\\ge', seg[-1]) and \
            len(re.findall(r'[A-Za-zÄÖÜäöüß]{3,}', re.sub(r'\$[^$]*\$', '', seg[-1]))) >= 3:
        seg = seg[:-1]
    erste = seg[0]
    if re.match(r'^(Ja|Nein)\b', erste):
        kurz = erste
        zw = seg[1:]
        return kurz, zw + extra
    if urteil:
        return urteil, seg + extra
    last = seg[-1]
    m = re.match(r'(Ergebnis|Antwort):\s*(.*)', last)
    if m:
        return m.group(2), seg[:-1] + extra
    # letzte Relation in der letzten Rechnung
    teile = teile_math(last)
    kurz, vor = last, ''
    for idx in range(len(teile) - 1, -1, -1):
        mth, t = teile[idx]
        if mth:
            pos = max(t.rfind('='), t.rfind(r'\approx'))
            if pos >= 0:
                rel = '=' if t[pos] == '=' else r'\approx'
                lhs = t[:pos].strip()
                rhs = t[pos + len(rel):].strip()
                nach = ''.join(('$' + x + '$') if mm else x for mm, x in teile[idx + 1:])
                vorher = ''.join(('$' + x + '$') if mm else x for mm, x in teile[:idx])
                kurz = ('$\\approx ' if rel != '=' else '$') + rhs + '$' + nach
                vor = vorher + '$' + lhs + '$'
                if rel != '=' and '=' in lhs and re.search(r'\\(t?frac|pi|sqrt)', lhs.rsplit('=', 1)[1]):
                    ex = lhs.rsplit('=', 1)[1].strip()   # exakt vor gerundet (Beschluss 24)
                    kurz = '$' + ex + ' \\approx ' + rhs + '$' + nach
                    vor = vorher + '$' + lhs.rsplit('=', 1)[0].strip() + '$'
                break
    zw = seg[:-1] + ([vor.strip()] if vor.strip() and vor.strip() != '$$' else []) + extra
    return kurz.strip(), zw


def bank_aufgabe(D, r, stufe):
    a = Aufgabe()
    a.art, a.id = 'bank', r['id']
    t = r['aufgabe']
    m = re.search(r'\s*\(P10 (\d{4})(?: (\w+))?\)', t)
    nach = ''
    if m:
        nach = f' nach P10 {m.group(1)}'
        t = t[:m.start()] + t[m.end():]
    a.fund = 'eigene Aufgabe' + nach
    a.form = r.get('form', '')
    a.pflicht = r.get('pflicht', '')
    a.loesung_roh = r.get('loesung', '')
    a.bild = r.get('bild', '') or ''
    a.orig = (r.get('original') or {}).get('id', '') if isinstance(r.get('original'), dict) else ''
    a.hrang = HRANG.get(r.get('hoehe'), 2)
    # Ankreuzoptionen der Bank (\kreuz{…}) untereinander (Beschluss 11, layout-befunde 6/7)
    if a.form == 'ankreuzen' and '\\kreuz{' in t:
        i = t.find('\\kreuz{')
        vor = re.sub(r'(\\\\\s*)+$', '', t[:i].rstrip())
        opts = []
        for m in re.finditer(r'\\kreuz\{', t):
            j, tiefe = m.end(), 1
            while tiefe:
                tiefe += {'{': 1, '}': -1}.get(t[j], 0); j += 1
            opts.append(t[m.end():j - 1])
        t = vor
        a.optionen = [tx(o, latex=True) for o in opts]
    a.text = tx(t, latex=True)
    a.abb = r.get('grafik', '') or ''
    if '\\streifenfeld' in (r.get('grafik') or ''):
        pass   # \streifenfeld setzt sein Antwortfeld selbst – kein zweites (Reparatur Punkt 7)
    elif r.get('antwort') and r['antwort'].strip() and '__' in r['antwort']:
        s = r['antwort']
        teile = re.split(r'__ ?([^\s,;]+(?= |,|;|$))?', s)
        # teile: Text, Einheit, Text, Einheit, …
        out = ''
        for i in range(0, len(teile), 2):
            out += tx(teile[i])
            if i + 1 < len(teile):
                e = teile[i + 1] or ''
                out += ('\\leerfeld[%s]' % tx(e) if e else '\\leerfeld') + ' '
        a.antwort = out.replace('\\\\', '\\')
    a.kreuz = r.get('form') == 'ankreuzen'
    kurz, zw = bank_loesung(r['loesung'])
    a.kurz = tx(kurz, latex=True)
    a.zw = [tx(z, latex=True) for z in zw]
    a.zw_roh = zw
    a.zw_wort = ['' if hat_wort(z) and not z.startswith('$') else wort_fuer(z, i, [], len(zw), stufe)
                 for i, z in enumerate(zw)]
    a.rang = HOEHE.get(r.get('hoehe'), 1.2)
    return a


def zone_aufgabe(D, r):
    a = bank_aufgabe(D, r, '')
    a.art = 'zone'
    a.fund = 'Grundlage'
    return a




# ---------------------------------------------------------------------------
# Kennzahlen für die Reihenfolge (Beschlüsse 2, 3): Zahlklasse, Textlänge, Fragenzahl
# ---------------------------------------------------------------------------
KOPF_P = {1, 5, 10, 20, 25, 50, 75, 100, 200}   # im Kopf rechenbare Sätze (Beschluss 3: 10/50/25/20/1 %)
OPERATOR = r'(Berechne|Bestimme|Gib|Kreuze|Entscheide|Überprüfe|Weise|Formuliere|Berichtige|' \
           r'Vervollständige|Ermittle|Zeichne|Schreibe|Untersuche|Trage|Färbe|Fülle|Erkläre|Rechne|' \
           r'Teile|Finde|Markiere|Begründe|Prüfe|Runde|Erweitere|Lies)'


def klartext(s):
    """LaTeX/Klartext -> grober Klartext für Zählungen."""
    s = s or ''
    s = re.sub(r'\\(t?frac)\{(\d+)\}\{(\d+)\}', r'\2/\3', s)
    s = s.replace('{,}', ',').replace('\\,', '').replace('\\%', '%').replace('$', '')
    s = re.sub(r'\\(kreuz|leerfeld|text|mathrm)\b', ' ', s)
    s = re.sub(r'\\[A-Za-z]+', ' ', s)
    s = s.replace('{', '').replace('}', '').replace('\\\\', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def zahlen(s):
    """[(wert, ist_prozent)] aus Klartext; Jahreszahlen fallen weg."""
    t = klartext(s)
    t = re.sub(r'(?<=\d) (?=\d{3}\b)', '', t)          # 10 000 -> 10000
    out = []
    for m in re.finditer(r'(\d+(?:,\d+)?)\s*(%)?', t):
        v = m.group(1)
        if re.fullmatch(r'(19|20)\d\d', v) and not m.group(2):
            continue
        out.append((float(v.replace(',', '.')), bool(m.group(2)), v))
    return out


def zahlklasse(a):
    """0 kopfrechenbar, 1 glatt (Taschenrechner), 2 krumm wie in der Prüfung (Entscheidung, nach
    Beschluss 3): krumm, wenn gerundet wird (≈, „Runde“) oder ein Satz Nachkommastellen hat;
    kopfrechenbar, wenn alle Sätze in KOPF_P liegen, alle übrigen Zahlen ganz sind und höchstens zwei
    geltende Ziffern haben und das Ergebnis ganz ist oder eine Nachkommastelle hat."""
    erg = a.kurz + ' ' + ' '.join(a.zw)
    if '≈' in erg or 'approx' in erg or re.search(r'\bRunde\b|\brunde\b', klartext(a.text)):
        return 2
    zs = zahlen(a.text)
    if any(p and v != int(v) for v, p, _ in zs):
        return 2
    kopf = True
    for v, p, roh in zs:
        if p:
            kopf &= v == int(v) and (int(v) in KOPF_P or int(v) < 10)   # 1–9 % und 10/20/25/50/75 %
        else:
            kopf &= v == int(v) and len(str(int(v)).strip('0')) <= 2
    for v, p, roh in zahlen(a.kurz):
        if ',' in roh and len(roh.split(',')[1].rstrip('0')) > 1:
            kopf = False
    return 0 if kopf and zs else 1


SATZRANG = {10: 0, 50: 1, 25: 2, 1: 3, 20: 4, 5: 5, 75: 6, 100: 7}   # Muster Fokus Grundwert (6)


def satzrang(a):
    ps = [int(v) for v, p, _ in zahlen(a.text) if p and v == int(v)]
    if 1 in ps:
        return SATZRANG[1]
    return SATZRANG.get(ps[0], 8) if ps else 8


def textlaenge(a):
    n = len(klartext(a.text))
    return 0 if n <= 110 else (1 if n <= 240 else 2)


def fragenzahl(a):
    saetze = [x for x in re.split(r'(?<=[.?!])\s+', klartext(a.text))
              if not re.match(r'(Rechne nicht|Runde|Mache zuerst)', x)]
    n = sum(1 for x in saetze if x.endswith('?') or re.match(OPERATOR + r'\b', x))
    if re.search(r'\bjeweils\b', klartext(a.text)):
        n += 1   # „… 10 %, 20 % oder 50 % … jeweils“ sind mehrere Fragen (Entscheidung)
    return max(1, n)


GRUPPEN = ['rechnen', 'Ankreuzen', 'Sachaufgabe', 'Vergleich']   # Reihenfolge: Entscheidung


def gruppe_von(D, a):
    """Gruppe nach dem, was der Schüler sieht (Beschluss 8). Entscheidung zu den Grenzen:
    Ankreuzen = Kreuz-Antwort; Vergleich = Begründen, Nachweisen, Prüfen, Urteil; rechnen = kurzer
    Auftrag (bis 70 Zeichen, oder bis 95 Zeichen und mit Operator am Anfang) oder Streifen/Tabelle
    ohne Sachtext; sonst Sachaufgabe."""
    t = klartext(a.text)
    if a.kreuz or a.optionen:
        return 'Ankreuzen'
    if a.art != 'echt' and a.zk == 0 and a.tl == 0 and a.fz == 1 and a.form not in ('text',):
        return 'rechnen'   # kopfrechenbar, kurz, eine Frage: unten auf der Leiter (Beschlüsse 3, 6)
    if a.art == 'echt':
        k = D.kat[a.id]
        if 'Begründung' in k['format'] or re.search(r'Weise|Überprüfe|Begründ|Entscheide', a.text):
            return 'Vergleich'
    else:
        if a.pflicht in ('begruenden', 'fehler') or re.match(r'(Ja|Nein|Richtig|falsch)\b', a.loesung_roh):
            return 'Vergleich'
        if a.form in ('streifenfeld', 'streifenleer', 'tabelle') and len(t) <= 130:
            return 'rechnen'
    if a.tl == 0 and a.fz == 1:
        return 'rechnen'
    return 'Sachaufgabe'


def gesucht(a):
    """Gesuchte Größe der Aufgabe aus der letzten Frage (Reparatur Punkt 3): Prozentsatz, Prozentwert,
    Grundwert oder '' (unbestimmt)."""
    t = klartext(a.text)
    fr = [x for x in re.split(r'(?<=[.?!])\s+', t) if x.endswith('?') or re.match(OPERATOR, x)]
    q = ' '.join(fr[-2:]) if fr else t
    if re.search(r'[Ww]ie viel Prozent|Prozentsatz|Zinssatz|[Uu]m wie viel Prozent|in Prozent', q):
        return 'Prozentsatz'
    if re.search(r'ganze|Ganze|insgesamt|vorher|alte|ursprünglich|voller|gesamt|passen in|hat die|hatte|1\s*%|[Kk]apital', q):
        return 'Grundwert'
    if re.search(r'\d\s*% von|spart|Nachlass|Rabatt|Zinsen|kostet|bezahl|neue', q):
        return 'Prozentwert'
    return ''


HRANG = {'vorstufe': 0, 'grundfall': 1, 'sprosse': 2, 'pflicht': 2, 'pruefung': 3}


def schrittzahl(a):
    """Schritte: echte Aufgaben aus dem Katalogfeld schritte; Bankaufgaben = Zwischenergebnisse mit
    Rechnung (Operator) + 1, höchstens 4."""
    if a.art == 'echt':
        return max(1, int(re.sub(r'\D', '', a.schritte or '1') or 1))
    n = sum(1 for z in (a.zw_roh or []) if re.search(r'\s(:|·|-|−|\+)\s|\\cdot|frac', z))
    return min(4, max(1, n))


def schluessel(a):
    """Reihenfolge (Beschlüsse 2, 8; Reparatur 06.10.): Zahlklasse (kopfrechenbar, glatt, krumm),
    Schrittzahl, Fragenzahl, Höhe der Bank (Vorstufe, Grundfall, Sprosse, Prüfung), Textlänge,
    Prozentsatz-Muster (10, 50, 25, 1, 20 %), Punkte; die Prüfungsherkunft entscheidet erst danach
    (eigene vor echter bei Gleichstand, jüngere Prüfung zuerst)."""
    pkt = int(a.punkte) if a.art == 'echt' and str(a.punkte).isdigit() else 0
    unten = 0 if (a.zk == 0 and a.hrang <= 1) else 1   # Grundfall im Kopf zuerst (Muster 6)
    return (a.zk, unten, schrittzahl(a), min(a.fz, 2), min(a.hrang, 3), a.tl, a.sr, pkt,
            a.art == 'echt', -a.jahr, a.id)


# ---------------------------------------------------------------------------
# Heft-Modell: Stufe = Leiter aus Vorstufen und Gruppen
# ---------------------------------------------------------------------------
BEZEICHNUNG = {'Grundwert': 'Grundwert $G$', 'Prozentwert': 'Prozentwert $W$',
               'Prozentsatz': 'Prozentsatz $p$', 'Zinsen und Zinssatz': 'Zinsen $Z$ und Zinssatz $p$'}
FORMEL = {'Grundwert': '$G = W : p$', 'Prozentwert': '$W = G \\cdot p$', 'Prozentsatz': '$p = W : G$',
          'Zinsen und Zinssatz': '$Z = K \\cdot p$, $p = Z : K$'}   # Schreibweise wie im Katalog (zwischenergebnis)


class Stufe:
    def __init__(self, z):
        self.name = z['stufe']
        self.kern = z['kern'] == 'ja'
        self.ids = z['katalog_ids'].split()
        self.sprossen = [re.sub(r'\[.*\]', '', s) for s in z['bank_sprossen'].split()]
        self.ziel = 's' + re.sub(r'[^a-z]', '', self.name.lower())[:20]
        self.vor = []          # Vorstufen (Aufgabe)
        self.gruppen = []      # [(name, wort, [Aufgabe])]
        self.reserve = []
        self.luecken = []


def kopfname(st):
    return BEZEICHNUNG.get(st.name, tx(st.name))


def jahre_info(D, st):
    """Grau hinter dem Stufennamen (Beschluss 13): „in k der letzten 5 Prüfungen“, sonst „selten
    geprüft“. Prüfungsjahre: OS- und FOR-Hefte."""
    alle = sorted({int(j) for j in D.pruefjahre})
    letzte5 = alle[-5:]
    jahre = {int(D.kat[i]['jahr']) for i in st.ids if i in D.kat}
    k = len([j for j in letzte5 if j in jahre])
    if k == 0:
        return 'selten geprüft', True
    return f'in {k} der letzten 5 Prüfungen', False


def kette_von(iid):
    return re.sub(r'-s-?\d+(-v\d+)?$', '', iid)


def sprosse_von(iid):
    return re.sub(r'-v\d+$', '', iid)


def erkennung_einheiten(D):
    """Erkennungsschritte (eigene Ketten nur aus Vorstufen): für welche Einheiten sie gelten – aus den
    Zeilen „Vor Einheit …“ des Themenkatalogs (nur diese Zeilen werden gelesen)."""
    erg = {}
    for ein in ('prozentrechnung', 'zinsrechnung'):
        p = os.path.join(D.mn, 'katalog', ein + '.md')
        if not os.path.exists(p):
            continue
        zeilen = [l for l in open(p, encoding='utf-8') if 'Vor Einheit' in l and l.startswith('- ')]
        ketten = OrderedDict()
        for r in D.bank.values():
            if r['eintrag'] == ein:
                ketten.setdefault(kette_von(r['id']), []).append(r)
        for k, rs in ketten.items():
            if not all(r['hoehe'] == 'vorstufe' for r in rs):
                continue
            name = rs[0]['kette']
            for l in zeilen:
                if name.strip('„“?') in l:
                    m = re.search(r'Vor Einheit (\d+)(?: (bis|und) (\d+))?', l)
                    a = int(m.group(1)); b = int(m.group(3) or a)
                    erg[k] = (ein, set(range(a, b + 1)) if m.group(2) == 'bis' else {a, b}, name)
    return erg


# Fokus: Sprossen anderer Stufen, die das Muster der Stufe ausdrücklich nennt (Beschluss 6:
# „… → nach Rabatt (80 %) → …“ ist Grundwert rückwärts aus Einheit 5)
FOKUS_DAZU = {'Grundwert': ['prozentrechnung-e5-k2-s4']}
# … und die echte „nach Rabatt (80 %)“-Aufgabe als längere Prüfungsaufgabe am Schluss
FOKUS_ECHT = {'Grundwert': ['2015-OS-K2b']}


class Bau:
    """Wählt die Aufgaben je Stufe. Eine Bank-Aufgabe steht höchstens einmal im Heft; braucht eine
    spätere Stufe dieselbe Sprosse, nimmt sie die nächste Variante (Entscheidung)."""

    def __init__(self, D, args):
        self.D, self.args = D, args
        self.benutzt = set()
        self.erk = erkennung_einheiten(D)
        self.sprossen = OrderedDict()
        for r in D.bank.values():
            self.sprossen.setdefault(sprosse_von(r['id']), []).append(r)
        for v in self.sprossen.values():
            v.sort(key=lambda r: r['variante'])
        self.stern_orig = {}
        self.vor_sp = set()   # Vorstufen-Sprossen, die schon eine Stufe dieses Hefts trägt
        self.grund_k = set()  # Ketten, deren Grundfall schon eine Stufe dieses Hefts trägt

    def nimm(self, sp, n, stufe, kopf_zuerst=True):
        rs = [r for r in self.sprossen.get(sp, []) if r['id'] not in self.benutzt]
        aufg = [bank_aufgabe(self.D, r, stufe) for r in rs]
        for a in aufg:
            kennzahlen(self.D, a)
        if kopf_zuerst:
            aufg.sort(key=lambda a: (a.zk, a.sr, a.tl, a.fz, a.id))
        wahl = aufg[:n]
        for a in wahl:
            self.benutzt.add(a.id)
        return wahl


def kennzahlen(D, a):
    a.zk, a.tl, a.fz, a.sr = zahlklasse(a), textlaenge(a), fragenzahl(a), satzrang(a)
    a.gruppe = gruppe_von(D, a)
    if a.art == 'echt' and a.gruppe == 'rechnen' and a.zk == 0 and a.tl == 0:
        pass


def stern_fuer(D, iid):
    """* für Aufgaben, die nur FOR sind (Beschluss 26): Katalogfeld stern ja (Sternaufgabe der
    OS-Hefte = Niveaustufe G außerhalb der EBR-Liste) oder ein FOR-Heft-Teil ohne EBR-Zwilling."""
    k = D.kat.get(iid)
    if not k:
        return False
    if k.get('stern') == 'ja':
        return True
    return k['papier'] == 'FOR' and iid not in D.ebr_zwilling


def baue_modell(D, args):
    B = Bau(D, args)
    stufen = [Stufe(z) for z in D.zu]
    stufen = [s for s in stufen if s.kern] + [s for s in stufen if not s.kern]   # Kern zuerst
    if args.fokus:
        stufen = [s for s in stufen if args.fokus.lower() in s.name.lower()]
        if not stufen:
            sys.exit(f'Fokus „{args.fokus}“ trifft keine Stufe')
    ps = None if args.fokus else pruefstein_waehlen(D)
    ps_ids = set(ps[3]) if ps else set()
    tief = args.art == 'schwach' or bool(args.fokus)     # Leiter von ganz unten (Beschlüsse 1, 7, 29)
    for st in stufen:
        st.kd, st.selten = jahre_info(D, st)
        # echte Aufgaben (oben auf der Leiter)
        echte = []
        for i in st.ids:
            if i in ps_ids:
                continue
            a = echt_aufgabe(D, i, st.name)
            if a:
                a.hrang = 3
                a.stern = stern_fuer(D, i)
                kennzahlen(D, a)
                echte.append(a)
        # Ketten und Einheiten der Stufe
        ketten, einheiten = [], set()
        for sp in st.sprossen:
            if sp.startswith('msa/'):
                continue
            k = kette_von(sp)
            if k not in ketten:
                ketten.append(k)
            m = re.match(r'(\w+)-e(\d+)-', sp)
            einheiten.add((m.group(1), int(m.group(2))))
        # Vorstufen: eigene der Ketten zuerst, dann Erkennungsschritte der Einheit (engster Bereich
        # zuerst); normal zwei, schwach/Fokus alle Sprossen mit je zwei Varianten (Entscheidung).
        vsp = []
        for k in ketten:
            vsp += [sp for sp in self_sprossen(B, k) if B.sprossen[sp][0]['hoehe'] == 'vorstufe']
        erk = sorted([(len(e[1]), k) for k, e in B.erk.items()
                      if any((e[0], n) in einheiten for n in e[1])])
        if args.fokus:
            erk = []   # Fokus: nur die Vorstufen der eigenen Kette, wie Muster 6 (Entscheidung)
        for _, k in erk:
            vsp += [sp for sp in self_sprossen(B, k) if sp not in vsp]
        # Vorstufe = Vorstufe genau dieses Handgriffs: eine Sprosse, die schon eine frühere Stufe
        # des Hefts trägt, kommt nicht noch einmal (Reparatur Punkt 8)
        vsp = [sp for sp in vsp if sp not in B.vor_sp]
        vor = []
        if args.art == 'schwach':
            for sp in vsp:
                vor += B.nimm(sp, 1, st.name)   # schwach: alle Vorstufen von ganz unten, je eine (Punkt 9)
        elif tief:
            for sp in vsp:
                vor += B.nimm(sp, 2, st.name)
        else:
            runde = 0
            while len(vor) < 2 and runde < 3:
                for sp in vsp:
                    if len(vor) >= 2:
                        break
                    vor += B.nimm(sp, 1, st.name)
                runde += 1
        if len(vor) < 2:
            st.luecken.append(f'{st.name}: {len(vor)} Vorstufe(n) in der Bank'
                              + (' (Ketten ' + ', '.join(ketten) + ')' if ketten else ' (keine Bankkette)'))
        for a in vor:
            a.hrang = 0
            B.vor_sp.add(sprosse_von(a.id))
        st.vor = sorted(vor, key=lambda a: (a.zk, a.sr, a.tl, a.fz, a.id))
        # Mitte: Grundfall je Kette (kopfrechenbar zuerst), die genannten Sprossen der Zuordnung
        mitte = []
        n_grund = 4 if args.fokus else 1
        n_spr = 2 if args.fokus else 1
        for k in ketten:
            for sp in self_sprossen(B, k):
                h = B.sprossen[sp][0]['hoehe']
                if h == 'grundfall' and k not in B.grund_k:
                    mitte += B.nimm(sp, n_grund, st.name)   # Grundfall einer Kette nur in ihrer ersten Stufe
                    B.grund_k.add(k)
                elif args.fokus and h == 'sprosse' and sp not in st.sprossen:
                    mitte += B.nimm(sp, 1, st.name)   # Fokus: ganze Kette von unten (Beschluss 7)
        if args.fokus:
            for sp in FOKUS_DAZU.get(st.name, []):
                for a in B.nimm(sp, 1, st.name, kopf_zuerst=False):   # v1: „nach Rabatt (80 %)“
                    a.gruppe = 'Sachaufgabe'
                    mitte.append(a)
            for iid in FOKUS_ECHT.get(st.name, []):
                a = echt_aufgabe(D, iid, st.name)
                if a:
                    a.hrang = 3; a.stern = stern_fuer(D, iid); kennzahlen(D, a)
                    echte.append(a)
            # nur Aufgaben, die nach der Größe der Stufe fragen (Reparatur Punkt 3)
            weg = [a for a in mitte if gesucht(a) not in ('', st.name) and st.name in ('Grundwert', 'Prozentwert', 'Prozentsatz')]
            for a in weg:
                D.befund(f'Fokus {st.name}: {a.id} fragt nach {gesucht(a)} – nicht gesetzt')
            mitte = [a for a in mitte if a not in weg]
        for sp in st.sprossen:
            m = re.match(r'(msa/[\w-]+\.jsonl)\((\d+)\)', sp)
            if m:
                rs = [r for r in D.zusatz.get(m.group(1), []) if r['id'] not in B.benutzt]
                # eigene Aufgaben in Prüfungshöhe nur, wenn echte fehlen (Beschlüsse 21, 22)
                if len(echte) < 2:
                    for r in rs[:max(1, 2 - len(echte))]:
                        a = bank_aufgabe(D, r, st.name); kennzahlen(D, a); B.benutzt.add(a.id)
                        mitte.append(a)
                continue
            if sp not in B.sprossen:
                D.befund(f'{st.name}: Bank-Sprosse {sp} ohne Aufgaben')
                continue
            h = B.sprossen[sp][0]['hoehe']
            if h == 'pruefung' and len(echte) >= 2:
                continue
            if h in ('grundfall', 'vorstufe'):
                continue
            mitte += B.nimm(sp, n_spr, st.name)
        for a in mitte:
            a.stern = bool(a.orig and stern_fuer(D, a.orig))
        # Gruppen (Beschluss 8): je Gruppe leicht -> schwer; Aufgabenbild-Wort aus Feld bild
        alle = mitte + echte
        if args.fokus:
            # Fokus (Muster 6): oben nur echte Prüfungshöhe, längste zuletzt (Reparatur Punkt 3)
            gl_unten = sorted(mitte, key=schluessel)
            gl_oben = sorted(echte, key=lambda a: (a.tl, schrittzahl(a), int(a.punkte or 1), -a.jahr))
            st.gruppen = [(g, '', [a for a in gl_unten if a.gruppe == g]) for g in GRUPPEN]
            st.gruppen = [x for x in st.gruppen if x[2]]
            st.gruppen.sort(key=lambda x: (schluessel(x[2][0])[:5], GRUPPEN.index(x[0])))
            st.gruppen.append(('Prüfung', '', gl_oben))
            alle = []
        else:
            st.gruppen = []
        # Kleine Gruppen nach Form und Zahlklasse (Beschlüsse 2, 3, 8; Reparatur Punkt 2): die Leiter
        # geht über die ganze Stufe – erst alle kopfrechenbaren Gruppen, dann glatte, dann krumme;
        # in einer Zahlklasse Gruppen nach ihrer leichtesten Aufgabe, bei Gleichstand rechnen,
        # Ankreuzen, Sachaufgabe; Vergleich (Urteil) am Ende der Zahlklasse (Entscheidung)
        for zk in (0, 1, 2):
            for g in GRUPPEN:
                gl = sorted([a for a in alle if a.gruppe == g and a.zk == zk], key=schluessel)
                if gl:
                    wort = next((a.bild for a in gl if a.bild), '')
                    st.gruppen.append((g, wort, gl))
        if not args.fokus:
            st.gruppen.sort(key=lambda x: (x[2][0].zk, x[0] == 'Vergleich', schluessel(x[2][0])[:5],
                                           GRUPPEN.index(x[0])))
        if not echte:
            D.befund(f'{st.name}: keine echte Aufgabe – Prüfungshöhe nur aus der Bank')
        st.reserve = []
        for k in ketten:
            for sp in self_sprossen(B, k):
                st.reserve += [r for r in B.sprossen[sp] if r['id'] not in B.benutzt
                               and r['hoehe'] in ('grundfall', 'sprosse')]
        for l in st.luecken:
            D.befund('Lücke: ' + l)
    D.ohne_bild = sum(1 for r in D.bank.values() if not r.get('bild'))
    return stufen, ps, B


def self_sprossen(B, k):
    return [sp for sp in B.sprossen if kette_von(sp) == k]


def pruefstein_waehlen(D):
    """Prüfstein (Beschluss 20): ganze echte Aufgabe aus den letzten fünf Prüfungsjahren, deren
    Teilaufgaben alle eigenen Wortlaut haben; jüngste zuerst. Gibt es keine ganze, nimmt das Programm
    (Entscheidung) die jüngste Aufgabe der letzten fünf Jahre mit mindestens zwei Teilaufgaben im
    eigenen Wortlaut, nur diese Teilaufgaben, und meldet es als Datenbefund."""
    letzte5 = sorted({int(j) for j in D.pruefjahre})[-5:]
    gruppen = OrderedDict()
    for iid, w in D.wort.items():
        if w['teil'] != 'vorspann':
            gruppen.setdefault(iid[:-1], []).append(iid)
    ganz, teil, fehlt = [], [], []
    for pre, ids in gruppen.items():
        alle = sorted(k for k in D.kat if k.startswith(pre) and len(k) == len(pre) + 1)
        if not alle or D.kat[alle[0]]['block'] == 'Basis' or int(D.kat[alle[0]]['jahr']) not in letzte5:
            continue
        da = [a for a in alle if a in D.wort]
        if len(alle) >= 2 and len(da) == len(alle):
            ganz.append((int(D.kat[alle[0]]['jahr']), len(alle), pre, alle))
        elif len(da) >= 2:
            teil.append((int(D.kat[alle[0]]['jahr']), len(da), pre, da))
            fehlt.append(f'{pre} (ohne {"".join(a[-1] for a in alle if a not in D.wort)})')
    if ganz:
        return sorted(ganz, reverse=True)[0]
    if teil:
        w = sorted(teil, reverse=True)[0]
        D.befund(f'Prüfstein: keine ganze Aufgabe der letzten fünf Jahre im eigenen Wortlaut; gesetzt '
                 f'{w[2]} nur mit {", ".join(x[-1] for x in w[3])} (fehlend: {"; ".join(fehlt)})')
        return w
    D.befund('Prüfstein: keine Aufgabe der letzten fünf Jahre im eigenen Wortlaut – kein Prüfstein')
    return None


# ---------------------------------------------------------------------------
# LaTeX setzen
# ---------------------------------------------------------------------------
KOPF = r"""\documentclass[11pt]{article}
\usepackage{mathblatt}
\begin{document}
"""


def marke(a, kurs):
    """Grau links (Beschluss 14): „P10 ’26“ an echten Aufgaben, „eigene Aufgabe“ an Bankaufgaben,
    nichts im Rückblick (Entscheidung)."""
    if a.art == 'echt':
        return f'P10 ’{str(a.jahr)[2:]}'
    if a.art == 'zone':
        return ''
    return 'eigene Aufgabe'


def nummer(a, nr):
    return (r'\llap{\textasteriskcentered\,}' if getattr(a, 'stern', False) else '') + str(nr) + '.'


def punkte_von(D, a):
    if a.art == 'echt':
        return f'{a.punkte} BE' if a.punkte else ''
    p = D.punkte.get(a.id)
    return f'{p} BE' if p else ''


def optionen_tex(a):
    if not a.optionen:
        return ''
    return ''.join(f'\\pfkreuzzeile{{{o}}}' for o in a.optionen)   # untereinander (C 11)


def tipp_ansatz(a):
    """Tipp nur als Ansatz (Beschluss 23): Formel mit eingesetzten Zahlen aus dem ersten
    Zwischenergebnis, das mit einer Formel beginnt („G = W : p = 6 € : 0,2 = 30 €“ ->
    „G = 6 € : 0,2“); sonst keiner (Entscheidung)."""
    for z in a.zw_roh:
        t = z.replace('$', '').strip()
        m = re.match(r'([GWpZK])\s*=\s*([^=]+?)\s*=\s*([^=]+?)(\s*=\s*[^=]+)?$', t)
        if m and m.group(4):
            return f'${m.group(1)}$ = ' + tx(m.group(3).strip())
    return ''


def _rhs(z):
    """Wert hinter dem letzten = / ≈ eines rohen Zwischenergebnisses, als LaTeX; '' ohne Zahl."""
    t = z.replace('$', '')
    teile = re.split(r'=|\\approx|≈|\\Rightarrow|⇒', t)
    if len(teile) < 2:
        return ''
    w = teile[-1].strip()
    return _stueck(w) if re.search(r'\d', w) else ''


def kurz_kontrolle(a):
    """Kontrollwert (Reparatur Punkt 6): ein Urteil („Ja“) wird durch den Zahlwert ersetzt, auf den es
    sich stützt (letztes Zwischenergebnis mit Wert vor „vergleichen“); bei zwei Fragen steht zuerst der
    Wert der ersten Frage (letztes Zwischenergebnis mit eigenem Wert), dann der der zweiten."""
    k = a.kurz
    roh = a.zw_roh if a.art != 'echt' else []
    if roh and re.match(r'^\$?\s*(Ja|Nein|ja|nein)\b[^\d]*$', klartext(k) or ''):
        basis = [z for z in roh if not re.match(r'\s*(vergleichen|Rest)', klartext(z)) and _rhs(z)]
        if basis:
            k = _rhs(basis[-1])
    elif roh and a.fz >= 2 and klartext(k).count(', ') < 1 and ';' not in klartext(k):
        mit = [_rhs(z) for z in roh if _rhs(z)]
        mit = [m for m in mit if klartext(m) != klartext(k)]
        if mit:
            k = mit[-1] + '; ' + k
    return k if k and len(klartext(k)) <= 45 else ''


def fuss(a, nr):
    """Seitenfuß (Beschluss 23): Kontrollwert, wo kurz; Tipp nur als Ansatz."""
    k = kurz_kontrolle(a)
    t = tipp_ansatz(a)
    if not k and not t:
        return ''
    s = f'{nr}' + (f':~{k}' if k else '')
    s = f'\\mbox{{{s}}}'   # Nummer und Wert nie getrennt (Reparatur Punkt 5)
    if t:
        s += f', \\mbox{{Tipp: {t}}}'
    return f'\\fusshilfe{{{s}}}'


def platz(a, art):
    """Rechenplatz nach Schrittzahl (Beschluss 11): Ankreuzen und Ein-Wort-Antwort (kopfrechenbar,
    ohne Zwischenergebnis, kurze Antwort) ohne Platz; sonst Schritte = Katalogfeld schritte bzw.
    Zwischenergebnisse + 1; schwach eine Zeile je Schritt, mindestens zwei (H 29)."""
    if a.kreuz or (a.optionen and not a.zw):
        return 0
    if a.art != 'echt' and a.form in ('streifenleer',):
        return 0
    if a.art == 'echt':
        s = int(re.sub(r'\D', '', a.schritte) or 1)
    else:
        s = len(a.zw) + 1
    if not a.zw and a.zk == 0 and a.art != 'echt' and len(klartext(a.kurz)) <= 25:
        return 0
    return max(2, min(5, s)) if art == 'schwach' else max(1, min(4, s))


def zf_fuer(a, zaehler, art):
    """Zerlegung mit Ausblenden (H 29) nur bei echten Mehrschritt-Aufgaben (Beschluss 5): erste
    Aufgabe der Stufe mit Zwischenfragen bekommt alle, die zweite die erste, dann keine."""
    if art != 'schwach' or not a.zf or a.art != 'echt' or int(re.sub(r'\D', '', a.schritte) or 1) < 2:
        return []
    k = zaehler[0]
    zaehler[0] += 1
    return a.zf if k == 0 else (a.zf[:1] if k == 1 else [])


def aufgabe_tex(D, a, nr, art, zfs, kurs, mit_nr=True):
    out = [f'\\begin{{pfnr}}{{{marke(a, kurs)}}}{{{nummer(a, nr) if mit_nr else ""}}}{{{punkte_von(D, a)}}}',
           a.text, optionen_tex(a)]
    if a.abb:
        out.append('\\par\\smallskip\\noindent ' + a.abb + '\\par')
    if getattr(a, 'antwort', ''):
        out.append('\\par\\noindent ' + a.antwort + '\\par')
    for f in zfs:
        out.append(f'\\pfzwfrage{{{tx(f)}}}')
    n = platz(a, art)
    if n:
        out.append(f'\\rechenraster{{{n}}}' if art == 'schwach' else f'\\rechenplatz{{{n}}}')
    out.append(fuss(a, nr))
    out.append('\\end{pfnr}')
    return '\n'.join(x for x in out if x)


def braucht_formel(st, a):
    """Formel ab der ersten Aufgabe, die rechnet und nicht mehr im Kopf geht; in den Zins-Stufen ab der
    ersten Rechnung (Zinssatz und Kapital brauchen die umgestellte Formel; Reparatur Punkt 4)."""
    if st.name not in FORMEL or a.hrang == 0 or a.kreuz or a.optionen:
        return False
    return a.zk >= 1 or st.name.startswith('Zinsen')


def bloecke(st):
    """Eine Stufe als Folge von Blöcken; nach jedem Block darf eine Portion enden (Beschluss 19).
    Block 0: Stufenkopf + Vorstufen; dann je Gruppe ein Block."""
    bl = [('kopf', st.vor)]
    for g, wort, gl in st.gruppen:
        bl.append(('gruppe', (g, wort, gl)))
    return bl


def setze_bloecke(D, args, teile, nr, formel_da):
    """teile: [(stufe, [blockindex])] -> LaTeX, nr, Lösungseinträge."""
    out, loes = [], []
    for st, idx in teile:
        zaehler = [0]
        bl = bloecke(st)
        kopf_gesetzt = False
        for i in idx:
            art, inh = bl[i]
            if not kopf_gesetzt:
                fort = '' if i == 0 else ' (Fortsetzung)'
                info = st.kd
                out.append(f'\\pfstufekopf[{st.ziel}{"" if i == 0 else "f" + str(i)}]{{{kopfname(st)}{fort}}}{{{info}}}')
                kopf_gesetzt = True
            if art == 'kopf':
                if inh:
                    out.append('\\pfgruppe{}')
                aufg = inh
            else:
                g, wort, aufg = inh
                out.append(f'\\pfgruppe{{{tx(wort)}}}')
            for a in aufg:
                if braucht_formel(st, a) and st.name not in formel_da:
                    out.append(f'\\pfab{{{FORMEL[st.name]}}}')
                    formel_da.add(st.name)
                nr += 1
                out.append(aufgabe_tex(D, a, nr, args.art, zf_fuer(a, zaehler, args.art), args.kurs))
                loes.append((f'{nr}.', a))
    return '\n'.join(out), nr, loes


def setze_rueckblick(D, args, rb, nr):
    out = ['\\pfrueckblick']
    loes = []
    for a in rb:
        nr += 1
        out.append(aufgabe_tex(D, a, nr, args.art, [], args.kurs))
        loes.append((f'{nr}.', a))
    return '\n'.join(out), nr, loes


def setze_pruefstein(D, args, ps):
    """Prüfstein ohne laufende Nummer und ohne Hilfen (Beschluss 20): kein Seitenfuß, kein
    Zwischenfragen-Gerüst; Teilaufgaben a), b) … mit Punkten."""
    jahr, n, pre, ids = ps
    vs = D.wort.get(pre)
    fund = fundstelle(D, ids[0], args.kurs, ganz=True)
    out = [f'\\pfpruefstein{{P10 ’{str(jahr)[2:]}}}']
    vs_abb = ''
    if vs:
        vs_abb = abbildung(vs['abbildung'], D, pre)
        t = [f'\\begin{{pfnr}}{{}}{{}}{{}}', tx(vs['wortlaut'])]
        if vs_abb:
            t.append('\\par\\smallskip\\noindent ' + vs_abb + '\\par')
        t.append('\\end{pfnr}')
        out.append('\n'.join(t))
    loes = []
    for iid in ids:
        w = D.wort[iid]
        a = echt_aufgabe(D, iid, '')
        a.stern = stern_fuer(D, iid)
        txt = w['wortlaut']
        if a.optionen or (a.abb and a.abb.startswith('\\begingroup')):
            vor, opts = ankreuz_zerlegen(txt)
            if opts:
                txt = vor
            else:
                z = aussagen_zerlegen(txt)
                if z:
                    txt = z[0] + ' ' + z[2]
        t = [f'\\begin{{pfnr}}{{}}{{{(chr(0x2a) if a.stern else "")}{w["teil"]})}}{{{a.punkte} BE}}', tx(txt),
             optionen_tex(a)]
        if a.abb and a.abb != vs_abb:
            t.append('\\par\\smallskip\\noindent ' + a.abb + '\\par')
        if not a.kreuz:
            t.append('\\rechenplatz{3}')
        t.append('\\end{pfnr}')
        out.append('\n'.join(x for x in t if x))
        loes.append((w['teil'] + ')', a))
    return '\n'.join(out), (loes, fund)


def fundstelle(D, iid, kurs, ganz=False):
    """Genaue Fundstelle (Heft · Aufgabe) für die Lösungsdatei (Beschluss 14). Ab 2026 nach Kurs
    (Beschluss 27): EBR-Zwilling, wenn es ihn gibt."""
    w = D.wort.get(iid)
    f = w['fundstelle'] if w else iid
    if kurs == 'EBR' and iid in D.ebr_zwilling:
        e = D.ebr_zwilling[iid]
        f = f'P10 {e[:4]} EBR · {e.split("-")[2][1:]}'
    if ganz:
        f = re.sub(r'(\d)[a-z]$', r'\1', f)
    return f


def _num(t):
    """Rechenausdruck (LaTeX oder Klartext) -> Wert oder None."""
    t = t.replace('$', '').replace('\\,', '').replace('{,}', '.').replace('\\cdot', '*').replace('·', '*')
    t = t.replace('−', '-').replace(':', '/').replace('\\ldots', '')
    t = re.sub(r'\\t?frac\{([^}]*)\}\{([^}]*)\}', r'((\1)/(\2))', t)
    t = re.sub(r'(\d)\.(?=\d{3}\b)', r'\1', t) if re.search(r'\d,\d', t) else t
    t = t.replace(',', '.').replace('^', '**')
    t = re.sub(r'\s*(€|kg|km|cm|m|l|h|Stunden|Kinder|\\%|%|Mio\.?)\s*', ' ', t).strip()
    if not t or not re.fullmatch(r'[\d.+\-*/() ]+', t) or not re.search(r'[+\-*/]', t.strip('-')):
        return None
    try:
        return eval(t, {'__builtins__': {}})
    except Exception:
        return None


def _de(v):
    s = f'{v:.2f}'.rstrip('0').rstrip('.') if abs(v - round(v)) > 1e-9 else str(int(round(v)))
    return s.replace('.', '{,}')


WORT_GROESSE = {'G': 'Grundwert', 'W': 'Prozentwert', 'p': 'Prozentsatz', 'Z': 'Zinsen', 'K': 'Kapital'}


def _stueck(t):
    """Teil einer Rechnung setzen: mit LaTeX-Befehlen im Mathemodus, Klartext wie im Katalog."""
    t = t.strip()
    if not t:
        return ''
    if '\\' in t or '{' in t or '^' in t:
        t = re.sub(r'(?<!\\)%', r'\\%', t)
        if not re.search(r'\\(cdot|t?frac|pi|approx|text|sqrt|Rightarrow)|\^', t):
            return t   # Bank-LaTeX ohne Mathebefehl (30\,\%, 0{,}25) geht im Text
        m = re.match(r'^(.*?)(\s+[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß. ]*)$', t)
        if m:
            return tx('$' + m.group(1) + '$') + tx(m.group(2))   # Einheit/Wort hinter der Zahl aufrecht
        return tx('$' + t + '$')
    return tx(t)


OP = re.compile(r'\s(:|·|-|−|\+)\s|\\cdot|\\t?frac|\^|/|\bvon\b')


def schwach_zeile(z, a):
    """„schwach“ (Beschluss 29): Wort + Ansatz ⇒ Wert. Das Wort ist die gesuchte Größe der Zeile, aus
    dem Ansatz bestimmt; lässt sie sich nicht bestimmen, steht kein Wort (Reparatur Punkt 1).
    Reihenfolge (Entscheidung): Formelbuchstabe vorn (G, W, p, Z, K) -> Größe; Beschriftung vorn
    („Rabatt 64 : 4“, „1 Karte: …“) -> sie ist das Wort; sonst aus der Rechnung: a : b mit b gleich
    einem Prozentsatz der Aufgabe -> „1 %“; a : 1,x -> „alter Wert“; a : b < 1 -> „Anteil“;
    · 100 -> „100 %“; Faktor 0,5…1,9 mal Wert -> „neuer Wert“, 0,0x…0,4 -> „Prozentwert“; a − b ->
    „Unterschied“; sonst keins. Symbolische Teile („W : p“) fallen weg; fehlt der Wert, rechnet das
    Programm ihn aus."""
    s = z.strip().replace('$', '')
    wort = ''
    m = re.match(r'^([GWpZK])\s*=\s*(.*)$', s)
    if m:
        wort, s = WORT_GROESSE[m.group(1)], m.group(2)
    teile = re.split(r'\s*(=|\\approx|≈|\\Rightarrow|⇒)\s*', s)
    segs, seps = teile[0::2], teile[1::2]
    # Beschriftung vor der ersten Zahl
    lm = re.match(r'^([A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß .]*?)\s*:?\s+(?=[\d(\\]|$)', segs[0])
    if lm and (re.fullmatch(r'[A-Za-z]', lm.group(1).strip()) or re.search(r'\b(von|je|oder)$', lm.group(1).strip())):
        lm = None
    if lm:
        if not wort:
            wort = lm.group(1).strip().rstrip(':')
        segs[0] = segs[0][lm.end():]
    else:
        lm2 = re.match(r'^([^:$=]{0,28}[^\s:$=]):\s+(.*)$', segs[0])
        if lm2:
            wort = wort or lm2.group(1).strip()
            segs[0] = lm2.group(2)
    # symbolische Teile weg (nur Buchstaben und Zeichen, keine Zahl)
    paare = [(sg, seps[k - 1] if k else '') for k, sg in enumerate(segs)]
    paare = [(sg, sp) for sg, sp in paare if re.search(r'\d', sg)]
    if not paare:
        return (tx(wort) + ': ' if wort else '') + _stueck(z.replace('$', ''))
    ansatz = paare[0][0]
    rest = paare[1:]
    if not OP.search(' ' + ansatz + ' '):
        # nur ein Wert: Wort + Wert
        return (tx(wort) + ': ' if wort else '') + ' '.join(
            ([_stueck(ansatz)] + [(r'$\approx$ ' if sp in ('\\approx', '≈') else '= ') + _stueck(sg) for sg, sp in rest]))
    if not wort:
        ps = {v for v, p, _ in zahlen(a.text) if p}
        mm = re.match(r'^\s*([\d{},.\\ ]+)\s*:\s*([\d{},.\\ ]+)\s*$', ansatz)
        q = _num(ansatz)
        if mm:
            b = _num('(' + mm.group(2) + ')*1')
            if b in ps and q is not None and q >= 1:
                wort = '1 %'
            elif b is not None and any(abs(b - (1 + p / 100)) < 1e-9 or abs(b - (1 - p / 100)) < 1e-9 for p in ps):
                wort = 'alter Wert'
            elif q is not None and q < 1:
                wort = 'Anteil'
        elif re.search(r'(\\cdot|·)\s*100\s*$', ansatz):
            wort = '100 %'
        elif re.search(r'(^|\s)(0\{?,\}?0\d|0\{?,\}?[1-4]\d*)\s*(\\cdot|·)|(\\cdot|·)\s*0\{?,\}?(0\d|[1-4])', ansatz):
            wort = 'Prozentwert'
        elif re.search(r'(^|\s)(0\{?,\}?[5-9]|1\{?,\}?\d+)\s*(\\cdot|·)|(\\cdot|·)\s*(0\{?,\}?[5-9]|1\{?,\}?\d+)', ansatz) \
                and '^' not in ansatz:
            wort = 'neuer Wert'
        elif re.search(r'\s(-|−)\s', ansatz) and '(' not in ansatz:
            wort = 'Unterschied'
    if rest:
        wert = ''
        for k, (sg, sp) in enumerate(rest):
            wert += ('' if k == 0 else (r' $\approx$ ' if sp in ('\\approx', '≈') else ' = ')) + _stueck(sg)
        if rest[0][1] in ('\\approx', '≈'):
            wert = r'$\approx$ ' + wert
    else:
        v = _num(ansatz)
        wert = _stueck(_de(v)) if v is not None else ''
    return (tx(wort) + ': ' if wort else '') + _stueck(ansatz) + (r' $\Rightarrow$ ' + wert if wert else '')


def loesung_zeilen(D, a, art, kurs):
    if art == 'schwach':
        zw = '; '.join(schwach_zeile(z, a) for z in (a.zw_roh or a.zw))
    else:
        zw = '; '.join(a.zw)
    f = fundstelle(D, a.id, kurs) if a.art == 'echt' else ''
    return a.kurz, zw, tx(f)


def setze_loesung(D, args, titel, eintraege, ps_loes):
    """Lösungsdatei ohne Punkte (Beschluss 25); rechts klein die Fundstelle statt der BE."""
    out = [KOPF.replace('\\begin{document}', ''), f'\\blattfuss{{{titel}}}{{Lösungen}}',
           '\\begin{document}', f'\\noindent{{\\large\\bfseries {titel} \\textperiodcentered{{}} Lösungen}}\\par\\medskip']
    for nr, a in eintraege:
        k, z, f = loesung_zeilen(D, a, args.art, args.kurs)
        # Fundstelle (Heft · Aufgabe) grau im Kopf der Tabelle, nur an echten Aufgaben (Beschluss 14);
        # die vierte Spalte (früher BE) bleibt leer (Beschluss 25)
        kopf = f'{{\\small\\color{{mbgrau}}{f}}}' if f else ''
        out.append(f'\\begin{{pfloesung}}{{{kopf}}}')
        out.append(f'\\lz{{{nr}}}{{{k}}}{{{z}}}{{}}')
        out.append('\\end{pfloesung}')
    if ps_loes:
        teile, fund = ps_loes
        out.append(f'\\begin{{pfloesung}}{{\\textbf{{Prüfstein}} \\textperiodcentered{{}} {tx(fund)}}}')
        for t, a in teile:
            k, z, _ = loesung_zeilen(D, a, args.art, args.kurs)
            out.append(f'\\lz{{{t}}}{{{k}}}{{{z}}}{{}}')
        out.append('\\end{pfloesung}')
    out.append('\\end{document}')
    return '\n'.join(out)


# ---------------------------------------------------------------------------
# Rückblick (Beschluss 18)
# ---------------------------------------------------------------------------
def fertigkeit_einheiten(D):
    """Fertigkeiten (Zone) -> Einheiten, aus dem Block „Fertigkeiten:“ der Themenkataloge."""
    erg = {}
    for ein in ('prozentrechnung', 'zinsrechnung'):
        p = os.path.join(D.mn, 'katalog', ein + '.md')
        if not os.path.exists(p):
            continue
        im = False
        for l in open(p, encoding='utf-8'):
            if l.startswith('Fertigkeiten:'):
                im = True; continue
            if im and not l.startswith('- '):
                break
            if im:
                m = re.search(r' – Einheit (\d+)(?:,? (?:und|bis) (?:Einheit )?(\d+))?', l)
                if m:
                    a, b = int(m.group(1)), int(m.group(2) or m.group(1))
                    rng = set(range(a, b + 1)) if ' bis ' in m.group(0) else {a, b}
                    erg[(ein, l[2:].split(' – ')[0].strip())] = rng
    return erg


WORT_VORAUS = [('Bruch', 'Bruch'), ('Anteil', 'Bruch'), ('Dezimal', 'Dezimalzahl'), ('Runden', 'Runden'),
               ('runden', 'Runden'), ('Potenz', 'Potenz'), ('Tabelle', 'Tabelle'), ('Dreisatz', 'Dreisatz'),
               ('Prozentsatz', 'Prozentsatz'), ('Prozentwert', 'Prozentwert')]


def rueckblick_grundlagen(D, args, stufen, B):
    """Erste Portion bzw. ganzes Blatt (Beschluss 18): eine Aufgabe je Voraussetzung, mindestens drei;
    schwach zwei je Voraussetzung. Voraussetzungen = Zone-Fertigkeiten, deren Einheit eine Stufe des
    Blatts braucht (Themenkatalog), dazu die, auf die das Katalogfeld voraussetzungen der echten
    Aufgaben zeigt. Nicht zuordenbare Einträge des Katalogfelds meldet das Programm."""
    fe = fertigkeit_einheiten(D)
    einheiten = set()
    kern = [st for st in stufen if st.kern] or stufen
    for st in kern:
        for sp in st.sprossen:
            m = re.match(r'(\w+)-e(\d+)-', sp)
            if m:
                einheiten.add((m.group(1), int(m.group(2))))
    namen = {st.name for st in stufen}
    ketten = OrderedDict()
    for r in D.zone_alle:
        ketten.setdefault((r['eintrag'], r['kette']), []).append(r)
    wahl = []
    for (ein, k), rs in ketten.items():
        if ein == 'zinsrechnung' and re.match(r'(Prozentwert|Prozentsatz|Grundwert) berechnen|Erhöhung', k):
            continue   # das sind Stufen des Hefts selbst (Entscheidung)
        if any(k[:12] == w[1][:12] for w in wahl):
            continue   # dieselbe Fertigkeit aus dem anderen Eintrag (Entscheidung)
        rng = next((v for (e2, n), v in fe.items() if e2 == ein and k.startswith(n[:25])), set())
        if any((ein, n) in einheiten for n in rng):
            wahl.append((ein, k))
    voraus = set()
    for st in kern:
        for i in st.ids:
            for v in (D.kat.get(i, {}).get('voraussetzungen', '') or '').split('|'):
                if v:
                    voraus.add(v)
    for v in sorted(voraus):
        treffer = [kk for kk in ketten if any(w in v and w2 in kk[1] for w, w2 in WORT_VORAUS)]
        if treffer:
            for t in treffer[:1]:
                if t not in wahl:
                    wahl.append(t)
        else:
            D.befund(f'Rückblick: Voraussetzung „{v}“ (Katalogfeld) hat keine Zone-Aufgabe')
    je = 2 if args.art == 'schwach' else 1
    out = []
    while len(out) < 3 and wahl and je <= 4:   # mindestens drei: dann zwei je Voraussetzung (Entsch.)
        out = []
        for key in wahl:
            rs = sorted(ketten[key], key=lambda r: (r['hoehe'] != 'grundfall', r['variante']))
            for r in rs[:je]:
                a = zone_aufgabe(D, r); kennzahlen(D, a); a.hrang = 0
                out.append(a)
        je += 1
    out = out[:max(3, len(wahl) * (2 if args.art == 'schwach' else 1))]
    if len(out) < 3:
        D.befund(f'Rückblick: nur {len(out)} Grundlagen-Aufgaben gefunden')
    return out


def rueckblick_vorige(D, args, vorige_stufen, B):
    """Spätere Portionen (Beschluss 18): Rückblick auf die vorige – je Stufe der vorigen Portion eine
    noch nicht benutzte Aufgabe derselben Sprossen (kopfrechenbar zuerst), mindestens drei
    (Entscheidung)."""
    out, sp_da = [], set()
    runde = 0
    while len(out) < 3 and runde < 3:
        for st in vorige_stufen:
            for r in st.reserve:
                # je Sprosse höchstens eine, solange es andere gibt (Entscheidung)
                if r['id'] in B.benutzt or (runde == 0 and sprosse_von(r['id']) in sp_da):
                    continue
                a = bank_aufgabe(D, r, st.name); kennzahlen(D, a); a.hrang = 1
                B.benutzt.add(r['id']); sp_da.add(sprosse_von(r['id']))
                out.append(a)
                if runde == 0 and len(out) < 3:
                    continue
                break
            if len(out) >= 3:
                break
        runde += 1
    return sorted(out[:3], key=lambda a: (a.zk, a.sr, a.tl, a.id))


# ---------------------------------------------------------------------------
# Heft zusammensetzen
# ---------------------------------------------------------------------------
def heft_tex(D, args, titel, unter, rb, teile, ps):
    out = [KOPF.replace('\\begin{document}', ''), '\\begin{document}',
           f'\\pruefheftstil{{{titel}}}{{{unter}}}',
           f'\\noindent{{\\Large\\bfseries {titel}}}\\hfill{{\\small\\color{{mbgrau}}{unter}}}\\par\\medskip']
    nr, loes = 0, []
    if rb:
        t, nr, l = setze_rueckblick(D, args, rb, nr)
        out.append(t); loes += l
    t, nr, l = setze_bloecke(D, args, teile, nr, set())
    out.append(t); loes += l
    ps_loes = None
    if ps:
        t, ps_loes = setze_pruefstein(D, args, ps)
        out.append(t)
    out.append('\\end{document}')
    return '\n'.join(out), loes, ps_loes


# ---------------------------------------------------------------------------
# Exakt vor gerundet an Bank-Lösungen (Beschluss 24)
# ---------------------------------------------------------------------------
def exakt_vor(D, a, r):
    """Steht im Ergebnis nur ein gerundeter Wert („≈ 70,8 %“), setzt das Programm den exakten Wert
    aus dem Feld pruef davor (sympy, rational), wie im Katalog: Prozent als Bruch des Anteils
    („17/24 ≈ 70,8 %“), sonst der Bruch selbst; nur wenn der Nenner höchstens 1000 ist und der
    exakte Wert zum gerundeten passt. Sonst bleibt es und zählt als Befund (D.n_exakt_offen)."""
    if 'approx' not in a.kurz or not r.get('pruef'):
        return
    m = re.match(r'\$\\approx\s*([^$]*)\$(.*)$', a.kurz.strip())
    if not m:
        D.n_exakt_offen += 1
        return
    rhs, nach = m.group(1), m.group(2)
    try:
        import sympy
        w = sympy.sympify(r['pruef'].replace('math.pi', 'pi').replace('math.', ''), rational=True)
        if isinstance(w, (list, tuple)) or getattr(w, 'is_Tuple', False):
            w = list(w)[-1]
        w = sympy.nsimplify(w)
    except Exception:
        D.n_exakt_offen += 1
        return
    zt = re.match(r'\s*([\d{},\\ ]*\d)', rhs)
    if not zt:
        D.n_exakt_offen += 1
        return
    try:
        g = float(re.sub(r'[^\d,]', '', zt.group(1).replace('{,}', ',')).replace(',', '.'))
    except ValueError:
        D.n_exakt_offen += 1
        return
    prozent = '%' in rhs[zt.end():]
    if abs(float(w) - g) < 1e-9:
        return   # Überschlag oder glatter Wert: ≈ steht für das Schätzen, kein exakter Wert davor
    e = w / 100 if prozent else w
    if not e.is_Rational or e.q > 1000 or e.q == 1 or abs(float(w) - g) > 0.06 * max(1, abs(g) / 100):
        D.n_exakt_offen += 1
        return
    ex = sympy.latex(e).replace('\\frac', '\\tfrac')
    if not prozent:
        ex += rhs[zt.end():]
    a.kurz = f'${ex} \\approx {rhs}${nach}'


# ---------------------------------------------------------------------------
# Übersetzen
# ---------------------------------------------------------------------------
def xelatex(tex, bb, name, arbeit):
    os.makedirs(arbeit, exist_ok=True)
    shutil.copy(os.path.join(bb, 'mathblatt.sty'), arbeit)
    with open(os.path.join(arbeit, name + '.tex'), 'w', encoding='utf-8') as f:
        f.write(tex)
    alt = None
    for lauf in range(4):   # mindestens zwei Läufe (Fuß), bis die .aux steht
        subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', name + '.tex'],
                       cwd=arbeit, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        auxp = os.path.join(arbeit, name + '.aux')
        aux = open(auxp, encoding='utf-8', errors='replace').read() if os.path.exists(auxp) else ''
        if lauf >= 1 and aux == alt:
            break
        alt = aux
    log = open(os.path.join(arbeit, name + '.log'), encoding='utf-8', errors='replace').read()
    pdf = os.path.join(arbeit, name + '.pdf')
    fehler = [l for l in log.splitlines() if l.startswith('!')]
    seiten = 0
    if os.path.exists(pdf):
        info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
        m = re.search(r'Pages:\s+(\d+)', info)
        seiten = int(m.group(1)) if m else 0
    return {'pdf': pdf if os.path.exists(pdf) and not fehler else None, 'fehler': fehler,
            'missing': log.count('Missing character'),
            'overfull': len(re.findall(r'Overfull \\hbox \((\d+\.\d+)pt', log)), 'seiten': seiten}


def register(args, name, ordner, seiten):
    """Eine Zeile in bau/register.csv (Kennung PRZ-PH<n>, Rezept PH = Prüfungsheft)."""
    p = os.path.join(BANK, 'bau', 'register.csv')
    zeilen = open(p, encoding='utf-8').read().splitlines()
    pfad = os.path.relpath(ordner, BANK)
    alt = [z.split(';')[0] for z in zeilen if z.endswith(';' + pfad)]
    zeilen = [z for z in zeilen if not z.endswith(';' + pfad)]
    nrn = [int(z.split(';')[0][6:]) for z in zeilen if re.match(r'PRZ-PH\d+;', z)]
    kenn = alt[0] if alt else f'PRZ-PH{max(nrn + [0]) + 1}'   # Neubau behält seine Kennung
    best = (f'kapitel={args.kapitel}, art={args.art}, portion={args.portion or "–"}, '
            f'fokus={args.fokus or "–"}, kurs={args.kurs}, seiten={seiten}')
    try:
        commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=BANK, capture_output=True,
                                text=True).stdout.strip()
    except Exception:
        commit = ''
    zeilen.append(f'{kenn};{args.datum};prozentrechnung,zinsrechnung;PH;{best};{commit};'
                  f'pruefheft.py v0.2;Version 2026-10-06;{pfad}')
    open(p, 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')


def main():
    ap = argparse.ArgumentParser(description='Prüfungsheft aus Daten setzen')
    ap.add_argument('--kapitel', required=True)
    ap.add_argument('--art', choices=['normal', 'schwach'], default='normal')
    ap.add_argument('--portion', type=int)
    ap.add_argument('--fokus')
    ap.add_argument('--kurs', choices=['EBR', 'FOR'], default='FOR',
                    help='Heft ab 2026 nach Kurs (Beschluss 27); Vorgabe FOR')
    ap.add_argument('--seiten', type=int, default=2, help='Startmaß einer Portion in Seiten (Serie)')
    ap.add_argument('--mn', default=os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe'))
    ap.add_argument('--bb', default=os.path.join(os.path.dirname(BANK), 'blattbau'))
    ap.add_argument('--datum', default=datetime.date.today().isoformat())
    ap.add_argument('--aus', help='Ausgabeordner (Vorgabe bau/pruefheft/<name>)')
    ap.add_argument('--ohne-register', action='store_true')
    args = ap.parse_args()

    D = Daten(args.mn, args.kapitel)
    D.n_exakt_offen = 0
    stufen, ps, B = baue_modell(D, args)
    for st in stufen:
        for a in st.vor + [x for _, _, gl in st.gruppen for x in gl]:
            if a.art == 'bank':
                exakt_vor(D, a, D.bank.get(a.id) or {})
    kap = args.kapitel.capitalize()
    unter = 'Prüfungsheft P10' + (' \\textperiodcentered{} EBR' if args.kurs == 'EBR' else '') + \
            (' \\textperiodcentered{} schwach' if args.art == 'schwach' else '')
    name = f'{args.kapitel}-{args.art}'
    titel = kap
    arbeit = tempfile.mkdtemp(prefix='pruefheft-')
    folge = [(st, i) for st in stufen for i in range(len(bloecke(st)))]
    def teile_aus(fl):
        t = []
        for st, i in fl:
            if t and t[-1][0] is st:
                t[-1][1].append(i)
            else:
                t.append((st, [i]))
        return t
    if args.fokus:
        name += f'-fokus-{args.fokus.lower()}'
        titel = f'{kap} \\textperiodcentered{{}} {kopfname(stufen[0])}'
        unter = unter.replace('Prüfungsheft P10', 'Prüfungsheft P10 \\textperiodcentered{} Fokus')
        rb = rueckblick_grundlagen(D, args, stufen, B)
        tex, loes, ps_loes = heft_tex(D, args, titel, unter, rb, teile_aus(folge), None)
    elif args.portion:
        # Serie (Beschluss 19): Portion endet nach einer abgeschlossenen Gruppe (Block); Startmaß
        # --seiten Seiten, gemessen durch Probeläufe; mindestens ein Block je Portion.
        start, vorige, p = 0, None, 0
        while True:
            p += 1
            if start >= len(folge):
                sys.exit(f'Portion {p} ist leer – das Kapitel endet mit Portion {p - 1}')
            benutzt0 = set(B.benutzt)
            def rb_fuer():
                B.benutzt = set(benutzt0)
                return rueckblick_grundlagen(D, args, stufen, B) if p == 1 else \
                    rueckblick_vorige(D, args, vorige, B)
            ende = start + 1
            while ende < len(folge):
                rb = rb_fuer()
                tex, _, _ = heft_tex(D, args, f'{kap} \\textperiodcentered{{}} Portion {p}', unter, rb,
                                     teile_aus(folge[start:ende + 1]), None)
                if xelatex(tex, args.bb, 'probe', arbeit)['seiten'] > args.seiten:
                    break
                ende += 1
            rb = rb_fuer()
            if p == args.portion:
                letzte = ende >= len(folge)
                titel = f'{kap} \\textperiodcentered{{}} Portion {p}'
                tex, loes, ps_loes = heft_tex(D, args, titel, unter, rb, teile_aus(folge[start:ende]),
                                              ps if letzte else None)
                break
            vorige = list(OrderedDict((st, 1) for st, _ in folge[start:ende]))
            start = ende
        name += f'-p{args.portion}'
    else:
        rb = rueckblick_grundlagen(D, args, stufen, B)
        tex, loes, ps_loes = heft_tex(D, args, titel, unter, rb, teile_aus(folge), ps)
    if args.kurs == 'EBR':
        name += '-ebr'
    ltitel = titel
    ltex = setze_loesung(D, args, ltitel, loes, ps_loes)
    ordner = args.aus or os.path.join(BANK, 'bau', 'pruefheft', f'{name}-{args.datum}')
    os.makedirs(os.path.join(ordner, 'src'), exist_ok=True)
    os.makedirs(os.path.join(ordner, 'pdf'), exist_ok=True)
    bericht, seiten = [], 0
    for nm, t in ((name, tex), (name + '-loesung', ltex)):
        erg = xelatex(t, args.bb, nm, arbeit)
        with open(os.path.join(ordner, 'src', nm + '.tex'), 'w', encoding='utf-8') as f:
            f.write(t)
        if erg['pdf']:
            shutil.copy(erg['pdf'], os.path.join(ordner, 'pdf', nm + '.pdf'))
        if nm == name:
            seiten = erg['seiten']
        bericht.append(f'{nm}: {erg["seiten"]} Seiten, Fehler {len(erg["fehler"])}, '
                       f'Missing character {erg["missing"]}, Overfull {erg["overfull"]}')
        bericht += ['   ' + fl for fl in erg['fehler'][:5]]
    if not args.ohne_register:
        register(args, name, ordner, seiten)
    print('\n'.join(bericht))
    print('Ordner:', ordner)
    print('Stufen:', ', '.join(s.name for s in stufen))
    if ps_loes:
        print('Prüfstein:', ps[2])
    print(f'Aufgaben: {len(loes)}; Bankzeilen ohne Feld bild (Aufgabenbild): {D.ohne_bild} von {len(D.bank)}')
    if D.n_exakt_offen:
        print(f'Bank-Ergebnisse mit ≈ ohne kurzen exakten Wert: {D.n_exakt_offen}')
    if D.befunde:
        print('Datenbefunde:')
        for b in D.befunde:
            print(' -', b)


if __name__ == '__main__':
    main()

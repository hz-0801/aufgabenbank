#!/usr/bin/env python3
"""pruefheft.py – setzt ein Prüfungsheft (Skript) aus Daten, ohne Modell (v0.1, 05.10.2026).

Bestellung auf der Befehlszeile, Ausgabe .tex und PDF (Heft und eigene Lösungsdatei) nach
bau/pruefheft/<kapitel>-<art>[-p<n>|-fokus-<wort>]-<datum>/ (Unterordner src/ und pdf/).

  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal
  python3 werkzeuge/pruefheft.py --kapitel prozent --art schwach
  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --portion 1
  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --fokus grundwert
  Pfade: --mn ../mathe-nachhilfe --bb ../blattbau (Voreinstellung: Nachbarordner des Repos)

Daten (alle gelesen, nichts geschrieben):
  mathe-nachhilfe  msa/zuordnung-<kapitel>.csv     Stufen in Lernreihenfolge, Kern, Katalog-ids,
                                                  Bank-Sprossen
                   msa/wortlaut-eigen-<kapitel>.csv eigener Wortlaut, Abbildung (Beschreibung),
                                                  Punkte, Fundstelle, Zwischenfragen
                   msa/skript-zuschnitt-p10.csv     Abschnitt, Neben-/Hauptplatz
                   msa/msa-katalog-*.csv            jahr, punkte, kurzloesung, zwischenergebnis,
                                                  stichwoerter, niveau_geschaetzt, antwort
                   msa/<kapitel>-zusatz.jsonl       Zusatzaufgaben (Bankformat)
  aufgabenbank     bank/<eintrag>/e*.jsonl, zone.jsonl   Aufgaben mit loesung
  blattbau         mathblatt.sty (ab 2026-10-05b: Abschnitt P, Prüfungsheft)

Regeln (offen.html 04./05.10., ziel.md § 2, bankblatt.md v5.5) sind in den Funktionen
unten genannt. Was das Programm entscheidet, steht im Kommentar daneben.
"""
import argparse, csv, datetime, glob, json, os, re, shutil, subprocess, sys, tempfile
from collections import Counter, OrderedDict

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)

# ---------------------------------------------------------------------------
# Text: Katalog/Wortlaut sind Klartext mit $…$-Stellen; Bank ist LaTeX.
# ---------------------------------------------------------------------------
UNI_MATH = {'⇒': r'\Rightarrow', '≈': r'\approx', '−': '-', '≤': r'\le', '≥': r'\ge',
            'π': r'\pi', 'α': r'\alpha', 'β': r'\beta', '→': r'\to', '⇔': r'\Leftrightarrow',
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


def abbildung(desc, D, iid, vorspann_abb=''):
    """Liefert (latex, ankreuztabelle?) zur Beschreibung; '' wenn keine nötig."""
    d = (desc or '').strip()
    if not d or d.startswith('keine'):
        return ''
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
    a.punkte = w['punkte'] or k['punkte']
    a.fund = w['fundstelle']
    a.jahr = int(k['jahr'])
    a.rang = NIVEAU.get(k['niveau_geschaetzt'], 2.5)
    a.kurz = '; '.join(tx(x.strip()) for x in k['kurzloesung'].split(' | ') if x.strip())
    if not k['kurzloesung']:
        D.befund(f'{iid}: kurzloesung leer')
    zw = [x.strip() for x in k['zwischenergebnis'].split(' ; ') if x.strip()]
    a.zf = [x.strip() for x in w.get('zwischenfragen', '').split(' ; ') if x.strip()]
    a.zw = [tx(z) for z in zw]
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
    a.text = tx(t, latex=True)
    a.abb = r.get('grafik', '') or ''
    if r.get('antwort') and r['antwort'].strip() and '__' in r['antwort']:
        s = r['antwort']
        teile = re.split(r'__ ?(%|€|kg|km|cm|min|GB|g|m|l|h)?', s)
        # teile: Text, Einheit, Text, Einheit, …
        out = ''
        for i in range(0, len(teile), 2):
            out += tx(teile[i])
            if i + 1 < len(teile):
                e = teile[i + 1] or ''
                out += '\\leerfeld[%s]' % tx(e) if e else '\\leerfeld'
        a.antwort = out.replace('\\\\', '\\')
    a.kreuz = r.get('form') == 'ankreuzen'
    kurz, zw = bank_loesung(r['loesung'])
    a.kurz = tx(kurz, latex=True)
    a.zw = [tx(z, latex=True) for z in zw]
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
# Heft-Modell: Stufen mit Leitaufgabe und weiteren
# ---------------------------------------------------------------------------
class Stufe:
    def __init__(self, z):
        self.name = z['stufe']
        self.kern = z['kern'] == 'ja'
        self.ids = z['katalog_ids'].split()
        self.sprossen = z['bank_sprossen'].split()
        self.aufgaben = []
        self.ziel = 's' + re.sub(r'[^a-z]', '', self.name.lower())[:20]


def jahre_info(D, st):
    jahre = sorted({int(D.kat[i]['jahr']) for i in st.ids if i in D.kat}, reverse=True)
    be = [int(D.kat[i]['punkte']) for i in st.ids if i in D.kat and D.kat[i]['punkte']]
    alle = sorted({int(j) for j in D.pruefjahre})
    letzte5 = alle[-5:]
    in5 = [j for j in jahre if j in letzte5]
    # „selten geprüft“ (Entscheidung des Programms): in den letzten fünf Prüfungsjahren nie
    # oder insgesamt höchstens einmal.
    selten = (not in5) or len(jahre) <= 1
    if not jahre:
        return 'noch nie geprüft', True
    s = f'in {len(jahre)} von {len(alle)} Jahren ({", ".join(str(j) for j in sorted(jahre))})'
    s += f' \\textperiodcentered{{}} zuletzt {jahre[0]}'
    if be:
        s += f' \\textperiodcentered{{}} {min(be)} BE' if min(be) == max(be) else \
             f' \\textperiodcentered{{}} {min(be)}--{max(be)} BE'
    if selten:
        s += r' \textperiodcentered{} \textbf{selten geprüft}'
    return s, selten


def bank_kandidaten(D, st):
    ks = []
    for sp in st.sprossen:
        sp0 = re.sub(r'\[.*\]', '', sp)
        m = re.match(r'(msa/[\w-]+\.jsonl)\((\d+)\)', sp0)
        if m:
            ks.extend(D.zusatz.get(m.group(1), []))
            continue
        its = sorted([r for k, r in D.bank.items() if k.startswith(sp0 + '-v')],
                     key=lambda r: r['variante'])
        if not its:
            D.befund(f'{st.name}: Bank-Sprosse {sp0} ohne Aufgaben')
        ks.extend(its)
    return ks


def bank_wahl(D, st, n, schon=()):
    """n Bankaufgaben, reihum über die Sprossen, Prüfungshöhe zuerst (Entscheidung)."""
    ks = [r for r in bank_kandidaten(D, st) if r['id'] not in schon]
    prio = ['pruefung', 'pflicht', 'sprosse', 'grundfall', 'vorstufe']
    nach_sp = OrderedDict()
    for r in ks:
        key = re.sub(r'-v\d+$', '', r['id'])
        nach_sp.setdefault(key, []).append(r)
    order = sorted(nach_sp.keys(), key=lambda k: prio.index(nach_sp[k][0].get('hoehe', 'sprosse'))
                   if nach_sp[k][0].get('hoehe') in prio else 9)
    wahl = []
    runde = 0
    while len(wahl) < n and any(len(nach_sp[k]) > runde for k in order):
        for k in order:
            if len(wahl) >= n:
                break
            if len(nach_sp[k]) > runde:
                wahl.append(nach_sp[k][runde])
        runde += 1
    return wahl


def neben_info(D, iid, stufe_name):
    for z in D.zuschnitt:
        if iid in z['neben'].split() and z['stufe'] == stufe_name:
            for h in D.zuschnitt:
                if iid in h['ids'].split():
                    return f'kennst du aus {h["kapitel"]}: {h["stufe"]}'
    return ''


def pruefstein_waehlen(D):
    """Ganze echte Aufgabe, deren Teilaufgaben alle eigenen Wortlaut haben; jüngste zuerst."""
    gruppen = OrderedDict()
    D.zaehl = []
    for iid, w in D.wort.items():
        if w['teil'] == 'vorspann':
            continue
        gruppen.setdefault(iid[:-1], []).append(iid)
    kand = []
    for pre, ids in gruppen.items():
        alle = sorted(k for k in D.kat if k.startswith(pre) and len(k) == len(pre) + 1)
        if len(alle) >= 2 and all(a in D.wort for a in alle):
            kand.append((int(D.kat[alle[0]]['jahr']), len(alle), pre, alle))
        elif len(alle) >= 2 and D.kat[alle[0]]['block'] != 'Basis':
            fehlt = [a[-1] for a in alle if a not in D.wort]
            D.zaehl.append(f'{pre} (ohne {"".join(fehlt)})')
    kand = [k for k in kand if D.kat[k[3][0]]['block'] != 'Basis']   # Basisteil ist kein Prüfstein
    if D.zaehl:
        D.befund('Prüfstein: unvollständig im eigenen Wortlaut sind ' + ', '.join(D.zaehl))
    if not kand:
        return None
    kand.sort(reverse=True)
    return kand[0]


def baue_modell(D, args):
    stufen = [Stufe(z) for z in D.zu]
    # Kern zuerst (Reihenfolge innerhalb Kern/Rest bleibt die der Zuordnung)
    stufen = [s for s in stufen if s.kern] + [s for s in stufen if not s.kern]
    ps = None
    if not args.fokus:
        ps = pruefstein_waehlen(D)
    ps_ids = set(ps[3]) if ps else set()
    for st in stufen:
        echte = []
        for i in st.ids:
            a = echt_aufgabe(D, i, st.name)
            if a:
                a.neben = neben_info(D, i, st.name)
                echte.append(a)
        rest = [a for a in echte if a.id not in ps_ids]
        if rest:
            echte = rest   # Prüfstein-Teilaufgaben nicht doppelt (Entscheidung)
        echte.sort(key=lambda a: (a.rang, -a.jahr))
        n = args.bank if args.bank is not None else (3 if st.kern else 2)
        bank = [bank_aufgabe(D, r, st.name) for r in bank_wahl(D, st, n)]
        st.reserve = bank_wahl(D, st, 50, {b.id for b in bank})
        if not echte:
            D.befund(f'{st.name}: keine echte Aufgabe – Leitaufgabe aus der Bank')
            st.aufgaben = sorted(bank, key=lambda a: a.rang)
        else:
            weitere = sorted(echte[1:] + bank, key=lambda a: (a.rang, -a.jahr))
            st.aufgaben = [echte[0]] + weitere
        st.kd, st.selten = jahre_info(D, st)
        sw = Counter()
        for a in echte:
            for s in a.stichwoerter:
                sw[s] += 1
        st.stichwoerter = [s for s, _ in sw.most_common() if s.lower() != st.name.lower()][:5]
    return stufen, ps


# ---------------------------------------------------------------------------
# LaTeX setzen
# ---------------------------------------------------------------------------
KOPF = r"""\documentclass[11pt]{article}
\usepackage{mathblatt}
\begin{document}
"""


def meta(a):
    s = []
    if a.punkte:
        s.append(f'{a.punkte} BE')
    if a.fund:
        s.append(tx(a.fund))
    if a.neben:
        s.append(tx(a.neben))
    return r' \textperiodcentered{} '.join(s)


def optionen_tex(a):
    if not a.optionen:
        return ''
    if a.optionen_kurz:
        return '\\par\\noindent\\hspace*{1.6em}' + ' \\quad '.join(f'$\\square$ {o}' for o in a.optionen) + '\\par'
    return ''.join(f'\\pfkreuzzeile{{{o}}}' for o in a.optionen)


def fuss(a, nr):
    if not a.kurz:
        return ''
    s = f'{nr}: {a.kurz}'
    if a.tipp:
        s += f', Tipp: {tx(a.tipp)}'
    return f'\\fusshilfe{{{s}}}'


def zf_fuer(a, stufe_zaehler, art):
    """Zerlegung mit Ausblenden (schwach): erste Aufgabe mit Zwischenfragen bekommt alle, die
    zweite nur die erste, ab der dritten keine. Gezählt werden nur Aufgaben mit Zwischenfragen
    (Entscheidung: Bankaufgaben haben keine)."""
    if art != 'schwach' or not a.zf:
        return []
    k = stufe_zaehler[0]
    stufe_zaehler[0] += 1
    if k == 0:
        return a.zf
    if k == 1:
        return a.zf[:1]
    return []


def aufgabe_gross(a, nr, art, zfs, platz=True):
    out = [f'\\begin{{pfaufgabe}}{{{nr}.}}{{{meta(a)}}}', a.text]
    out.append(optionen_tex(a))
    if a.abb:
        out.append('\\par\\smallskip\\noindent ' + a.abb + '\\par')
    if getattr(a, 'antwort', '') and art != 'schwach':
        out.append('\\par\\noindent\\hfill ' + a.antwort + '\\par')
    for f in zfs:
        out.append(f'\\pfzwfrage{{{tx(f)}}}')
    if platz and not a.kreuz:
        n = max(2, min(6, len(a.zw) + 1)) if art == 'schwach' else max(2, min(4, len(a.zw) + 2))
        out.append(f'\\rechenplatz{{{n}}}')
    out.append(fuss(a, nr))
    out.append('\\end{pfaufgabe}')
    return '\n'.join(x for x in out if x)


def aufgabe_klein(a, nr):
    out = [f'\\pfkopfzeile{{{nr}.}}{{{meta(a)}}}', a.text, optionen_tex(a)]
    if getattr(a, 'antwort', ''):
        out.append('\\par\\noindent\\hfill ' + a.antwort)
    out.append(fuss(a, nr))
    return '\n'.join(x for x in out if x)


def breit(a):
    return bool(a.abb) or len(a.text) > 420 or (a.optionen and not a.optionen_kurz)


def setze_stufe(st, nr0, art, mit_kopf=True):
    out = []
    nr = nr0
    if mit_kopf:
        out.append(f'\\pfstufe[{st.ziel}]{{{tx(st.name)}}}')
        out.append(f'\\kommtdran{{{st.kd}}}')
    z = [0]
    loes = []
    if art == 'schwach':
        for a in st.aufgaben:
            nr += 1
            out.append(aufgabe_gross(a, nr, art, zf_fuer(a, z, art), platz=True))
            loes.append((nr, a))
        return '\n'.join(out), nr, loes
    leit = st.aufgaben[0]
    nr += 1
    out.append(aufgabe_gross(leit, nr, art, [], platz=True))
    loes.append((nr, leit))
    weitere = st.aufgaben[1:]
    if weitere:
        out.append('\\pfweiterekopf')
    puffer = None
    for a in weitere:
        nr += 1
        loes.append((nr, a))
        if breit(a):
            if puffer:
                out.append(f'\\pfpaar{{{puffer}}}{{}}')
                puffer = None
            out.append(aufgabe_gross(a, nr, art, [], platz=False).replace(
                '\\begin{pfaufgabe}', '{\\small\\begin{pfaufgabe}').replace(
                '\\end{pfaufgabe}', '\\end{pfaufgabe}}'))
            continue
        k = aufgabe_klein(a, nr)
        if puffer is None:
            puffer = k
        else:
            out.append(f'\\pfpaar{{{puffer}}}{{{k}}}')
            puffer = None
    if puffer:
        out.append(f'\\pfpaar{{{puffer}}}{{}}')
    return '\n'.join(out), nr, loes


def setze_pruefstein(D, ps, nr):
    jahr, n, pre, ids = ps
    nr += 1
    vs = D.wort.get(pre)
    fund = re.sub(r'\s*·\s*\w+$', '', D.wort[ids[0]]['fundstelle'])
    fund = re.sub(r'(\d)[a-z]$', r'\1', D.wort[ids[0]]['fundstelle'])
    out = [f'\\pfpruefstein{{{tx(fund)}}}']
    teile = []
    kopf = ''
    vs_abb = ''
    if vs:
        kopf = tx(vs['wortlaut'])
        vs_abb = abbildung(vs['abbildung'], D, pre)
    body = [f'\\begin{{pfaufgabe}}{{{nr}.}}{{{tx(fund)}}}', kopf]
    if vs_abb:
        body.append('\\par\\smallskip\\noindent ' + vs_abb + '\\par')
    body.append('\\end{pfaufgabe}')
    out.append('\n'.join(x for x in body if x))
    loes = []
    for iid in ids:
        w = D.wort[iid]
        a = echt_aufgabe(D, iid, '')
        # Wortlaut ohne Vorspann (der steht oben)
        a2text = tx(w['wortlaut'])
        if a.abb == 'ANKREUZTABELLE' or (a.abb and a.abb.startswith('\\begingroup')):
            vor, _ = ankreuz_zerlegen(w['wortlaut'])
            a2text = tx(vor)
        elif a.optionen:
            vor, opts = ankreuz_zerlegen(w['wortlaut'])
            if opts:
                a2text = tx(vor)
        t = [f'\\begin{{pfaufgabe}}{{{w["teil"]})}}{{{a.punkte} BE}}', a2text, optionen_tex(a)]
        if a.abb and a.abb != vs_abb:
            t.append('\\par\\smallskip\\noindent ' + a.abb + '\\par')
        t.append('\\rechenplatz{3}')
        t.append('\\end{pfaufgabe}')
        out.append('\n'.join(x for x in t if x))
        loes.append((w['teil'] + ')', a))
    return '\n'.join(out), nr, (nr, loes, fund)


def loesung_zeilen(a, art):
    if art == 'schwach':
        teile = []
        for z, w in zip(a.zw, a.zw_wort + [''] * len(a.zw)):
            teile.append((w + ': ' if w else '') + z)
        zw = '; '.join(teile)
    else:
        zw = '; '.join(a.zw)
    be = f'{a.punkte} BE' if a.punkte else ''
    return a.kurz, zw, be


def setze_loesung(titel, eintraege, ps_loes, art):
    out = [KOPF.replace('\\begin{document}', ''), f'\\blattfuss{{{titel}}}{{Lösungen}}',
           '\\begin{document}', f'\\noindent{{\\large\\bfseries {titel} \\textperiodcentered{{}} Lösungen}}\\par\\medskip']
    for nr, a in eintraege:
        k, z, be = loesung_zeilen(a, art)
        out.append('\\begin{pfloesung}{}')
        out.append(f'\\lz{{{nr}.}}{{{k}}}{{{z}}}{{{be}}}')
        out.append('\\end{pfloesung}')
    if ps_loes:
        nr, teile, fund = ps_loes
        out.append(f'\\begin{{pfloesung}}{{\\textbf{{{nr}.}} Prüfstein \\textperiodcentered{{}} {tx(fund)}}}')
        for t, a in teile:
            k, z, be = loesung_zeilen(a, art)
            out.append(f'\\lz{{{t}}}{{{k}}}{{{z}}}{{{be}}}')
        out.append('\\end{pfloesung}')
    out.append('\\end{document}')
    return '\n'.join(out)


def rueckblick_waehlen(D, stufen_portion, n=2):
    """Portion 1: Grundlagen aus der Bank-Zone, die zu den Stichwörtern/Voraussetzungen der
    Portion passen; je Fertigkeit höchstens eine (Entscheidung)."""
    woerter = set()
    for st in stufen_portion:
        for a in st.aufgaben:
            woerter.update(w.lower() for w in a.stichwoerter)
            if a.art == 'echt':
                woerter.update(x.lower() for x in re.split(r'[|; ]', D.kat[a.id].get('voraussetzungen', '')) if len(x) > 3)
        woerter.update(w.lower() for w in re.split(r'\W+', st.name) if len(w) > 3)
    ketten = OrderedDict()
    for r in D.zone:
        ketten.setdefault(r['kette'], []).append(r)
    wert = []
    for k, rs in ketten.items():
        s = sum(1 for w in woerter if w and w in k.lower())
        wert.append((-s, list(ketten).index(k), k))
    wert.sort()
    wahl = []
    for _, _, k in wert[:n]:
        rs = sorted(ketten[k], key=lambda r: (r['hoehe'] != 'sprosse', r['variante']))
        wahl.append(rs[0])
    return [zone_aufgabe(D, r) for r in wahl]


def setze_heft(D, args, stufen, ps, auswahl, rueckblick, titel, untertitel, mit_uebersicht):
    out = [KOPF.replace('\\begin{document}', ''), '\\begin{document}',
           f'\\pruefheftstil{{{titel}}}{{{untertitel}}}',
           f'\\noindent{{\\Large\\bfseries {titel}}}\\hfill{{\\small\\color{{mbgrau}}{untertitel}}}\\par\\medskip']
    if mit_uebersicht:
        out.append('\\begin{pfuebersicht}')
        for st in auswahl:
            sw = ', '.join(tx(s) for s in st.stichwoerter)
            out.append(f'\\pfuezeile{{{st.ziel}}}{{{tx(st.name)}}}{{{sw}}}')
        if ps:
            out.append('\\multicolumn{3}{@{}l}{\\hspace{1.4em}Prüfstein} & S.\\,\\pageref{pruefstein}\\\\')
        out.append('\\end{pfuebersicht}')
    nr = 0
    loes = []
    if rueckblick:
        out.append('\\pfrueckblick')
        puffer = []
        for a in rueckblick:
            nr += 1
            loes.append((nr, a))
            puffer.append(aufgabe_klein(a, nr))
        while len(puffer) < 2:
            puffer.append('')
        out.append(f'\\pfpaar{{{puffer[0]}}}{{{puffer[1]}}}')
    abschnitt = None
    for st in auswahl:
        ab = next((z['abschnitt'] for z in D.zuschnitt if z['stufe'] == st.name), None) \
            or next((z['abschnitt'] for z in D.zuschnitt if z['kapitel'].lower() == args.kapitel), args.kapitel.capitalize())
        if ab != abschnitt:
            out.append(f'\\pfabschnitt{{{tx(ab)}}}')
            abschnitt = ab
        t, nr, l = setze_stufe(st, nr, args.art)
        out.append(t)
        loes.extend(l)
    ps_loes = None
    if ps:
        out.append('\\label{pruefstein}')
        t, nr, ps_loes = setze_pruefstein(D, ps, nr)
        out.append(t)
    out.append('\\end{document}')
    return '\n'.join(out), loes, ps_loes


# ---------------------------------------------------------------------------
# Übersetzen
# ---------------------------------------------------------------------------
def xelatex(tex, bb, name, arbeit):
    os.makedirs(arbeit, exist_ok=True)
    shutil.copy(os.path.join(bb, 'mathblatt.sty'), arbeit)
    with open(os.path.join(arbeit, name + '.tex'), 'w', encoding='utf-8') as f:
        f.write(tex)
    alt = None
    for lauf in range(4):
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
    missing = log.count('Missing character')
    overfull = len(re.findall(r'Overfull \\hbox \((\d+\.\d+)pt', log))
    seiten = 0
    if os.path.exists(pdf):
        info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
        m = re.search(r'Pages:\s+(\d+)', info)
        seiten = int(m.group(1)) if m else 0
    return {'pdf': pdf if os.path.exists(pdf) and not fehler else None, 'fehler': fehler,
            'missing': missing, 'overfull': overfull, 'seiten': seiten}


def main():
    ap = argparse.ArgumentParser(description='Prüfungsheft aus Daten setzen')
    ap.add_argument('--kapitel', required=True)
    ap.add_argument('--art', choices=['normal', 'schwach'], default='normal')
    ap.add_argument('--portion', type=int)
    ap.add_argument('--fokus')
    ap.add_argument('--bank', type=int, help='Bankaufgaben je Stufe (Vorgabe: Kern 3, sonst 2)')
    ap.add_argument('--mn', default=os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe'))
    ap.add_argument('--bb', default=os.path.join(os.path.dirname(BANK), 'blattbau'))
    ap.add_argument('--datum', default=datetime.date.today().isoformat())
    ap.add_argument('--aus', help='Ausgabeordner (Vorgabe bau/pruefheft/<name>)')
    args = ap.parse_args()

    D = Daten(args.mn, args.kapitel)
    stufen, ps = baue_modell(D, args)
    kap = args.kapitel.capitalize()
    teil = args.art
    rueck = []
    mit_ue = True
    auswahl = stufen
    unter = 'Prüfungsheft P10' + (' \\textperiodcentered{} schwach' if args.art == 'schwach' else '')
    if args.fokus:
        auswahl = [s for s in stufen if args.fokus.lower() in s.name.lower()]
        if not auswahl:
            sys.exit(f'Fokus „{args.fokus}“ trifft keine Stufe')
        teil += f'-fokus-{args.fokus.lower()}'
        mit_ue = False
        unter = f'Fokus {args.fokus}' + (' \\textperiodcentered{} schwach' if args.art == 'schwach' else '')
    name = f'{args.kapitel}-{teil}'
    arbeit = tempfile.mkdtemp(prefix='pruefheft-')
    if args.portion:
        # Serie: eine Seite je Portion als Startmaß, Schnitt nur an Stufengrenzen, Kern zuerst.
        # Portionen nacheinander bestimmen (jede so viele Stufen, wie auf eine Seite passen).
        start = 0
        vorige = []
        for p in range(1, args.portion + 1):
            if start >= len(stufen):
                sys.exit(f'Portion {p} ist leer – das Kapitel endet mit Portion {p - 1}')
            if p == 1:
                rueck_fn = lambda sts: rueckblick_waehlen(D, sts)
            else:
                prev = vorige
                rueck_fn = lambda sts, prev=prev: [bank_aufgabe(D, r, prev[-1].name)
                                                   for r in (prev[-1].reserve[:1] + (prev[0].reserve[:1] if len(prev) > 1 else prev[-1].reserve[1:2]))]
            ende = start + 1
            while True:
                kand = stufen[start:ende]
                letzte = ende >= len(stufen)
                r = rueck_fn(kand)
                tex, _, _ = setze_heft(D, args, stufen, ps if letzte else None, kand, r,
                                       f'{kap} \\textperiodcentered{{}} Portion {p}', unter, False)
                erg = xelatex(tex, args.bb, 'probe', arbeit)
                if erg['seiten'] > 1 and ende > start + 1:
                    ende -= 1
                    break
                if erg['seiten'] > 1 or letzte:
                    break
                ende += 1
            vorige = stufen[start:ende]
            if p == args.portion:
                auswahl = vorige
                rueck = rueck_fn(auswahl)
                if ende < len(stufen):
                    ps = None
            start = ende
        teil = f'{args.art}-p{args.portion}'
        name = f'{args.kapitel}-{teil}'
        mit_ue = False
        titel = f'{kap} \\textperiodcentered{{}} Portion {args.portion}'
    else:
        titel = kap
    if args.fokus:
        ps = None
        titel = f'{kap} \\textperiodcentered{{}} Grundwert' if False else f'{kap} \\textperiodcentered{{}} {tx(auswahl[0].name)}'
    tex, loes, ps_loes = setze_heft(D, args, stufen, ps, auswahl, rueck, titel, unter, mit_ue)
    ltex = setze_loesung(titel.replace(' \\textperiodcentered{} ', ' · ').replace('·', '\\textperiodcentered{}'), loes, ps_loes, args.art)
    ordner = args.aus or os.path.join(BANK, 'bau', 'pruefheft', f'{name}-{args.datum}')
    os.makedirs(os.path.join(ordner, 'src'), exist_ok=True)
    os.makedirs(os.path.join(ordner, 'pdf'), exist_ok=True)
    bericht = []
    for nm, t in ((name, tex), (name + '-loesung', ltex)):
        erg = xelatex(t, args.bb, nm, arbeit)
        with open(os.path.join(ordner, 'src', nm + '.tex'), 'w', encoding='utf-8') as f:
            f.write(t)
        if erg['pdf']:
            shutil.copy(erg['pdf'], os.path.join(ordner, 'pdf', nm + '.pdf'))
        bericht.append(f'{nm}: {erg["seiten"]} Seiten, Fehler {len(erg["fehler"])}, '
                       f'Missing character {erg["missing"]}, Overfull {erg["overfull"]}')
        for fl in erg['fehler'][:5]:
            bericht.append('   ' + fl)
    print('\n'.join(bericht))
    print('Ordner:', ordner)
    print('Arbeitsordner:', arbeit)
    print('Stufen:', ', '.join(s.name for s in auswahl))
    if ps and (not args.portion or ps_loes):
        print('Prüfstein:', ps[2])
    if D.befunde:
        print('Datenbefunde:')
        for b in D.befunde:
            print(' -', b)


if __name__ == '__main__':
    main()

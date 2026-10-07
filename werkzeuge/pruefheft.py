#!/usr/bin/env python3
"""pruefheft.py – setzt ein Prüfungsheft (Skript) aus Daten, ohne Modell (v0.3, 06.10.2026).

Bestellung auf der Befehlszeile, Ausgabe .tex und PDF (Heft und eigene Lösungsdatei) nach
bau/pruefheft/<kapitel>-<art>[-p<n>|-fokus-<wort>][-ebr]-<datum>/ (Unterordner src/ und pdf/).

  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal
  python3 werkzeuge/pruefheft.py --kapitel prozent --art schwach
  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --portion 1
  python3 werkzeuge/pruefheft.py --kapitel prozent --art normal --fokus grundwert
  python3 werkzeuge/pruefheft.py --kapitel dreiecke --art normal --fokus pythagoras   (Steckbrief, 06.10. abends)
  Steckbrief mit Teil 5 „Arten“: Fokusblatt in Grundform G1 (Beschlüsse 07.10., g1_bau; v0.4)
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

Regeln: Arbeitsliste bau/pruefheft/beschluesse-2026-10-06.md (Punkte 1–29) und Nachtrag
beschluesse-2026-10-06b.md (N1–N4, geht vor), ziel.md § 2/§ 4, bankblatt.md v5.7. Neue Daten (v0.3, alle
optional – fehlen sie, baut das Programm wie bisher): msa/handgriffe-p10.csv, msa/herausgeloest-p10.csv,
msa/rueckblick-p10.csv, msa/erkennen-p10.csv, msa/fremd/*.csv (und fremd/*-erkennen.csv), Spalten
jahre_letzte5, nebenplaetze, verwechselbar der Zuordnung; Bankzeilen mit Feld ruht nie. Die Nummer des Beschlusses steht im Kommentar; was das Programm selbst
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
            '·': r'\cdot', '°': r'^\circ',
            # Lauf C (Geometrie, Funktionen): fehlten in der Schrift (Missing character)
            'γ': r'\gamma', 'δ': r'\delta', 'ε': r'\varepsilon', 'φ': r'\varphi', 'μ': r'\mu',
            '≠': r'\neq', '∠': r'\angle', '₁': r'_1', '₂': r'_2', '₃': r'_3', '₀': r'_0', '′': r"'",
            'ᵧ': r'_y',   # S_y (Bezeichnungen N4.18)
            # Zeichen der neuen Daten (fremd, herausgelöst; Nachtrag 06.10.), die der Schrift fehlen
            '▢': r'\square', '∢': r'\sphericalangle', '∛': r'\sqrt[3]{\;}', '∥': r'\parallel', 'ℓ': r'\ell',
            '↔': r'\leftrightarrow', '✓': r'\surd', '●': r'\bullet', '▲': r'\blacktriangle',
            '◼': r'\blacksquare', 'Δ': r'\Delta', 'ˣ': r'^{x}', '₅': r'_5', '₇': r'_7',
            '⅓': r'\tfrac{1}{3}', '⅔': r'\tfrac{2}{3}', '⅖': r'\tfrac{2}{5}'}
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


def text_lauf_c(t):
    """Klartext der neuen Kapitel (Lauf C): ⁻¹ (tan⁻¹) und a^b außerhalb von $…$ als Hochzahl;
    Wörter im Index ($h_{Deckfläche}$) als \\text. Nur wirksam, wenn das Zeichen vorkommt –
    Prozent-Texte enthalten keins (byte-gleich)."""
    if '⁻' in t:
        t = re.sub(r'⁻(\$\^\{(\d+)\}\$|([¹²³]))', lambda m: '$^{-' + (m.group(2) or m.group(3).translate(SUP)) + '}$', t)
        t = t.replace('⁻', '$^{-}$')
    return t


def _klammer_ende(t, i):
    tiefe = 0
    for j in range(i, len(t)):
        tiefe += {'(': 1, ')': -1}.get(t[j], 0)
        if tiefe == 0:
            return j
    return len(t) - 1


ABI_MATH = {'∞': r'\infty', '→': r'\to', '≠': r'\neq', '⊥': r'\perp', '∪': r'\cup', '±': r'\pm',
            '×': r'\times', '√': r'\sqrt{\,}'}


def abi_tx(s):
    """Klartext-Formeln der Abitur-Katalogfelder (kurzloesung, zwischenergebnis) -> LaTeX (Lauf B2):
    e^(…) und ^(…) als Hochzahl, √a und √(…) als Wurzel, ∞ → ≠ ⊥ ∪ ± im Mathemodus, ′ als Strich,
    ⇔ als ⇒ (nur ⇒, Lösungsblatt 05.10.)."""
    if not s:
        return ''
    t = s.replace('⇔', '⇒').replace('′', "'").replace('″', "''")
    out, i = '', 0
    while i < len(t):
        c = t[i]
        if c == '^':
            if i + 1 < len(t) and t[i + 1] == '(':
                j = _klammer_ende(t, i + 1)
                inner = t[i + 2:j]
                i = j + 1
            else:
                m = re.match(r'[\w,.−-]+', t[i + 1:])
                inner = m.group(0) if m else ''
                i += 1 + len(inner)
            inner = inner.replace('−', '-').replace('·', r'\cdot ').replace(',', '{,}')
            inner = re.sub(r'(\d+)/(\d+)', r'\\tfrac{\1}{\2}', inner)
            out += '$^{' + inner + '}$'
            continue
        if c == '√':
            if i + 1 < len(t) and t[i + 1] == '(':
                j = _klammer_ende(t, i + 1)
                inner, i = t[i + 2:j], j + 1
            else:
                m = re.match(r'[\d,]+', t[i + 1:])
                inner = m.group(0) if m else ''
                i += 1 + len(inner)
            out += '$\\sqrt{' + inner.replace(',', '{,}').replace('−', '-') + '}$'
            continue
        if c in ABI_MATH and c != '√':
            out += '$' + ABI_MATH[c] + '$'
            i += 1
            continue
        out += c
        i += 1
    return tx(out).replace('$$', '')


SUPZ = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}


def abi_formel(s):
    """Klartext-Formel (Katalog) ganz im Mathesatz (Lauf B3): f'(x) = 3x² − 24x + 45 ->
    $f'(x) = 3x^{2} - 24x + 45$. Nur für Zeilen ohne deutsches Wort; sonst abi_tx."""
    t = s.strip().replace('′', "'").replace('″', "''").replace('⇔', '⇒')
    if re.search(r'[A-Za-zÄÖÜäöüß]{3,}', re.sub(r'\b(exp|sin|cos|tan|ln)\b', '', t)):
        return abi_tx(s)
    t = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹]+)', lambda m: '^{' + ''.join(SUPZ[c] for c in m.group(1)) + '}', t)
    def hoch(t):
        out, i = '', 0
        while i < len(t):
            if t[i] in '^√' and i + 1 < len(t) and t[i + 1] == '(':
                j = _klammer_ende(t, i + 1)
                inner = hoch(t[i + 2:j])
                out += ('^{' + inner + '}') if t[i] == '^' else ('\\sqrt{' + inner + '}')
                i = j + 1
                continue
            if t[i] == '√':
                m = re.match(r'[\d,]+|[a-z]', t[i + 1:])
                w = m.group(0) if m else ''
                out += '\\sqrt{' + w + '}'
                i += 1 + len(w)
                continue
            out += t[i]
            i += 1
        return out
    t = hoch(t)
    t = re.sub(r'(?<![\d{])(\d+)/(\d+)(?![\d}])', r'\\tfrac{\1}{\2}', t)
    t = re.sub(r'(?<=\d),(?=\d)', '{,}', t)
    for k, v in (('₁', '_1'), ('₂', '_2'), ('₃', '_3'), ('ᵧ', '_y'), ('−', '-'), ('·', '\\cdot '), ('×', '\\times '), ('⇒', '\\Rightarrow '), ('≈', '\\approx '),
                 ('∞', '\\infty '), ('≠', '\\neq '), ('≤', '\\le '), ('≥', '\\ge '), ('±', '\\pm '),
                 ('π', '\\pi '), ('→', '\\to '), ('°', '^\\circ ')):
        t = t.replace(k, v)
    t = t.replace('|', '\\mid ').replace(';', ';\\ ')
    return '$' + t + '$'


def abi_zw(z, kurz=''):
    """Rechte Spalte der Lösung im Abitur (Lösungsblatt 05.10.; Lauf B3): je Handgriff ein kurzes
    Zwischenergebnis „Ansatz ⇒ Ergebnis“. Erklär-Etiketten („ersten Faktor null setzen:“) fallen weg,
    „, also“ wird ⇒; Einträge ohne Wert (nur „f′(x)“, „x“, „positiv“) und Wiederholungen des
    Ergebnisses fallen weg. Rückgabe Klartext/LaTeX oder ''."""
    t = z.strip()
    t = re.sub(r'^[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß ,()]{2,40}:\s+', '', t)   # Etikett vorn
    t = re.sub(r'^[A-Za-zÄÖÜäöüß]+ (\$[^$]*\$):\s+', '', t)   # „Bedingung $f(x) = 0$: …“ -> der Ansatz danach
    t = re.sub(r'(\$?),?\s*also\s*', r'\1 ⇒ ', t).replace('$ ⇒ $', ' \\Rightarrow ')
    t = t.replace(' ⇒ ', ' $\\Rightarrow$ ') if '$' in t else t
    kl = klartext(t)
    if not re.search(r'=|⇒|Rightarrow|≈|approx|<|>', t) or not re.search(r'\d', kl):
        return ''
    if kurz and klartext(kurz).replace(' ', '') in kl.replace(' ', '') and len(kl) < len(klartext(kurz)) + 6:
        return ''
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
            if re.search(r'[äöüÄÖÜß]', t):   # Wort im Index ($h_{Deckfläche}$; Lauf C)
                t = re.sub(r'_\{([^{}]*[äöüÄÖÜß][^{}]*)\}', r'_{\\text{\1}}', t)
            t = t.replace(r'\frac', r'\tfrac')
            res.append('$' + t + '$')
        else:
            if '^' in t and not latex:
                # a^b im Klartext (Katalog Wachstum: 1,4^24) -> Hochzahl (Lauf C)
                t = re.sub(r'(\d+(?:,\d+)?)\^(\d+|\(?[a-z]\)?)', lambda m: '$' + m.group(1).replace(',', '{,}') + '^{' + m.group(2).strip('()') + '}$', t)
                # Buchstabe als Basis (f(x) = b · a^x; neue Daten): ebenfalls Hochzahl
                t = re.sub(r'(?<![\\A-Za-z])([a-zA-Z])\^(\d+|\(?[a-z]\)?)', lambda m: '$' + m.group(1) + '^{' + m.group(2).strip('()') + '}$', t)
            res.append(text_lauf_c(textteil(t, latex)))
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


def ruht(r):
    """Stillgelegte Zeile (Nachtrag N1.3: Kopien, die sich nur in der Zahl unterscheiden): Feld „ruht“
    oder ein Feld gleicher Bedeutung („stillgelegt“), gesetzt und nicht leer/false/nein."""
    for f in ('ruht', 'stillgelegt'):
        v = r.get(f)
        if v not in (None, '', False, 0, 'nein', 'false', 'False'):
            return True
    return False


def kapitel_passt(k, kap):
    """kapitel-Spalte der neuen P10-Daten („prozent“, „Prozent“, „prozentrechnung“) gegen --kapitel."""
    k = (k or '').strip().lower()
    return bool(k) and (k == kap or k.startswith(kap) or kap.startswith(k))


# Prüfungsprofile (Lauf B2): Ordner, Kataloge, Zuschnitt, Marke, Prüfungsjahre
PROFIL = {
    'p10': dict(ordner='msa', kataloge='msa-katalog-*.csv', zuschnitt='skript-zuschnitt-p10.csv',
                marke='P10', titel='Prüfungsheft P10', kopf='P10', papiere=lambda r: r['papier'] in ('OS', 'FOR'),
                stern=True, pruefstein=True, kennung='PRZ-PH'),
    # Abitur GK: „in x der letzten 5 Prüfungen“ über die letzten fünf BB-Jahrgänge (Beschluss 13);
    # kein Stern; kein Prüfstein (je Gebiet offen)
    'abi-gk': dict(ordner='abitur', kataloge='abi-katalog.csv', zuschnitt='skript-zuschnitt-abi-gk.csv',
                   marke='Abi', titel='Probeheft Abitur GK', kopf='Abi GK',
                   papiere=lambda r: re.search(r'-(bebb|bb)-gk$', r['papier']) is not None,
                   stern=False, pruefstein=False, kennung='KUR-PH'),
}


class Daten:
    def __init__(self, mn, kapitel, pruefung='p10'):
        self.mn = mn
        self.kapitel = kapitel
        self.pr = PROFIL[pruefung]
        o = self.pr['ordner']
        self.kat = {}
        for p in sorted(glob.glob(os.path.join(mn, o, self.pr['kataloge']))):
            for r in lies_csv(p):
                self.kat[r['id']] = r
        self.pruefjahre = sorted({(r['jahr']) for r in self.kat.values() if self.pr['papiere'](r)})
        self.zu = lies_csv(os.path.join(mn, o, f'zuordnung-{kapitel}.csv'))
        self.zwilling_zu = {}
        for z in self.zu:
            for paar in (z.get('ebr_zwilling') or '').split():
                f, e = paar.split('=')
                self.zwilling_zu[f] = e
        wl = lies_csv(os.path.join(mn, o, f'wortlaut-eigen-{kapitel}.csv'))
        self.wort_eigen = {r['id'] for r in wl}
        # Teilaufgaben, die absichtlich nur einmal geschrieben sind, stehen in einer anderen
        # wortlaut-eigen-*.csv (Lauf C Nachbesserung): alle Dateien, eigene zuerst, erste gewinnt
        da = set(self.wort_eigen)
        for p in sorted(glob.glob(os.path.join(mn, o, 'wortlaut-eigen-*.csv'))):
            if p.endswith(f'wortlaut-eigen-{kapitel}.csv'):
                continue
            for r in lies_csv(p):
                if r['id'] not in da:
                    da.add(r['id'])
                    wl.append(r)
        for r in wl:   # Datenbefund B1: f\\'(x) und ′ in der Wortlaut-Datei
            for f in ('wortlaut', 'abbildung'):
                r[f] = (r.get(f) or '').replace("\\'", "'").replace('′', "'").replace('″', "''")
        self.wort = OrderedDict((r['id'], r) for r in wl)
        self.zuschnitt = lies_csv(os.path.join(mn, o, self.pr['zuschnitt']))
        # Bankeinträge = die, die die Zuordnung nennt (Prozent: wie bisher)
        ein_z = []
        for z in self.zu:
            for sp in z['bank_sprossen'].split():
                m = re.match(r'([a-z-]+?)-(e\d+|zone)-', sp)
                if m and m.group(1) not in ein_z:
                    ein_z.append(m.group(1))
        self.eintraege = ein_z or ['prozentrechnung', 'zinsrechnung']
        self.bank = {}
        self.zone = []
        self.n_ruht = 0
        for ein in self.eintraege:
            for p in sorted(glob.glob(os.path.join(BANK, 'bank', ein, 'e*.jsonl'))):
                for r in lies_jsonl(p):
                    if ruht(r):
                        self.n_ruht += 1   # stillgelegte Kopien nie verwenden (Nachtrag N1.3)
                        continue
                    self.bank[r['id']] = r
        zp = os.path.join(BANK, 'bank', self.eintraege[0], 'zone.jsonl')
        self.zone = [r for r in lies_jsonl(zp) if not ruht(r)]
        self.zone_alle = []
        for ein in self.eintraege[:2]:   # Zone der beiden Haupteinträge (Entscheidung)
            zp = os.path.join(BANK, 'bank', ein, 'zone.jsonl')
            if os.path.exists(zp):
                self.zone_alle += [r for r in lies_jsonl(zp) if not ruht(r)]
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
        for p in glob.glob(os.path.join(mn, o, '*-zusatz.jsonl')):
            name = os.path.basename(p)
            self.zusatz[o + '/' + name] = [r for r in lies_jsonl(p) if not ruht(r)]
        self.befunde = []   # Datenformat-Erkenntnisse während des Baus
        # Neue Daten des Nachtrags 06.10. (N1–N4), nur P10; fehlt eine Datei, baut das Programm wie bisher
        self.neu = OrderedDict()
        def opt(name):
            q = os.path.join(mn, o, name)
            if pruefung == 'p10' and os.path.exists(q):
                self.neu[name] = True
                return lies_csv(q)
            self.neu[name] = False
            return []
        kap = kapitel.lower()
        self.handgriffe = {r['id']: r for r in opt('handgriffe-p10.csv')}
        self.heraus = [r for r in opt('herausgeloest-p10.csv')]
        self.rueck = [r for r in opt('rueckblick-p10.csv') if kapitel_passt(r.get('kapitel', ''), kap)]
        self.erkennen = [r for r in opt('erkennen-p10.csv') if kapitel_passt(r.get('kapitel', ''), kap)]
        self.fremd = []
        fr = sorted(glob.glob(os.path.join(mn, o, 'fremd', '*.csv'))) if pruefung == 'p10' else []
        self.neu['fremd/*.csv'] = bool(fr)
        # Erkennen-Sätze der F-Agenten liegen als fremd/<gruppe>-erkennen.csv (Schema wie erkennen-p10.csv)
        for q in [q for q in fr if q.endswith('-erkennen.csv')]:
            self.erkennen += [r for r in lies_csv(q) if kapitel_passt(r.get('kapitel', ''), kap)]
        fr = [q for q in fr if not q.endswith('-erkennen.csv')]
        for q in fr:
            for r in lies_csv(q):
                if ruht(r):
                    continue
                r['_datei'] = os.path.basename(q)
                self.fremd.append(r)
        # herausgelöste Zeilen können auch in fremd/ stehen (art herausgeloest); beides nach Kapitel
        self.fremd = [r for r in self.fremd if kapitel_passt(r.get('kapitel', ''), kap)]
        self.heraus = [r for r in self.heraus if kapitel_passt(r.get('kapitel', ''), kap)] + \
            [r for r in self.fremd if (r.get('art') or '').strip() == 'herausgeloest']
        self.fremd = [r for r in self.fremd if (r.get('art') or 'ganz').strip() != 'herausgeloest']
        self.n_fremd = self.n_heraus = self.n_eigen_weg = self.n_buendel = 0
        self.sb = None   # Steckbrief des Fokus (werkzeuge/steckbrief.py), sonst None

    def befund(self, s):
        if s not in self.befunde:
            self.befunde.append(s)


# ---------------------------------------------------------------------------
# Abbildungen: werkzeuge/abbildung.py (Lauf C)
# ---------------------------------------------------------------------------
sys.path.insert(0, HIER)
import abbildung as AB
import steckbrief as SB
AB.einrichten(tx)
abbildung = AB.abbildung


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
        self.sicher = 'ja'
        self.hilfsmittel = ''
        self.abhaengig = ''
        self.marke_text = ''   # Herkunftsmarke außer P10 (Nachtrag N1.2/N4.17): „BY ’23“, „nach P10 ’15“
        self.fest = 0          # feste Stelle am Anfang der Stufe (Grundwert-Leiter N2.11), 0 = keine
        self.gebraucht = []    # Rückblick (N2.10): ids/Stufen, ab denen die Aufgabe gebraucht wird
        self.zahlart = ''      # fremde/herausgelöste: Zahlart aus den Daten
        self.woerter = 0


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
    tl = m.group(1)
    for x, y in re.findall(r'\d([a-z]) bis [\d.]*\d([a-z])', tl):   # „2.1a bis 2.1h“
        if x <= teil <= y:
            return True
    return teil in re.findall(r'\d+([a-z])', tl)


KREUZSPALTE = ('richtig', 'falsch', 'wahr', 'nicht entscheidbar', 'passt', 'passt nicht', 'ja', 'nein')


def ankreuz_tabelle(bild, text, kr, a):
    """Ankreuztabelle aus der Kennung ANKREUZ{Kopf}{Zeilen}{Art} (Lauf C). Art liste: gewöhnliche
    Ankreuzzeilen (Optionen aus dem Text); opt: Zeilen = Optionen bzw. zitierte Aussagen des Texts;
    fest: Zeilen aus der Beschreibung. Spalten richtig/falsch/wahr … als Kästchen, andere
    (Korrektur) als Schreibfeld; „+begruendung“: eine Schreibzeile unter jeder Zeile."""
    kopf, zeilen, art = kr
    if art == 'liste':
        vor, opts = ankreuz_zerlegen(text)
        if opts:
            a.optionen = [tx(o) for o in opts]
            return bild, vor
        return bild, text
    nach = ''
    if art.startswith('opt'):
        vor, opts = ankreuz_zerlegen(text)
        if opts:
            mm = re.search(r'\.\s+(?=[A-ZÄÖÜ])', opts[-1])
            if mm:   # „… / letzte Aussage. Gib eine Gleichung an.“ -> Auftrag danach in den Text
                opts[-1], nach = opts[-1][:mm.start()], opts[-1][mm.end():]
        else:
            z = aussagen_zerlegen(text)
            if not z:
                return bild, text
            vor, opts, nach = z
        if nach:
            # Auftrag nach den Aussagen („Gib eine Gleichung von f an.“) steht unter der Tabelle (Lauf C)
            a.nach_tabelle = tx(nach)
        text = vor
        reihen = opts
    else:
        reihen = [r for r in zeilen.split('|') if r]
        z = aussagen_zerlegen(text)
        if z and len(z[1]) == len(reihen):
            text = z[0] + ' ' + z[2]
    sp = kopf.split('|')
    def zelle(k):
        return '$\\square$' if k.strip() in KREUZSPALTE or k.strip().startswith('$') else ''
    breit_c = sum(0.45 + 0.2 * len(k) for k in sp[1:] if zelle(k))
    n_p = sum(1 for k in sp[1:] if not zelle(k))
    w_a = max(4.0, min(8.0, 13.0 - breit_c - 3.6 * n_p))
    form = '|p{%.1fcm}|' % w_a + ''.join('c|' if zelle(k) else 'p{3.4cm}|' for k in sp[1:])
    if any(k.strip().startswith('$') for k in sp[1:]):
        form = '|l|' + 'c|' * (len(sp) - 1)
    begr = art.endswith('+begruendung')
    z_tex = []
    for r in reihen:
        z_tex.append(' & '.join([tx(r)] + [zelle(k) for k in sp[1:]]) + r' \\ \hline')
        if begr:
            z_tex.append(r'\multicolumn{%d}{|l|}{\rule{0pt}{3.2ex}\footnotesize\color{mbgrau}Begründung:} \\ \hline' % len(sp))
    tab = (r'\begingroup\renewcommand{\arraystretch}{1.5}\begin{tabular}{%s}\hline %s \\ \hline %s\end{tabular}\endgroup'
           % (form, ' & '.join(tx(k) for k in sp), ' '.join(z_tex)))
    if getattr(a, 'nach_tabelle', ''):
        tab += '\n\\par\\smallskip\\noindent ' + a.nach_tabelle
    return (bild + '\n\\par\\smallskip\\noindent ' + tab) if bild else tab, text


def echt_aufgabe(D, iid, stufe):
    w = D.wort.get(iid)
    k = D.kat.get(iid)
    if not w or not k:
        D.befund(f'{iid}: fehlt im Wortlaut oder Katalog – nicht gesetzt')
        return None
    a = Aufgabe()
    a.art, a.id = 'echt', iid
    a.sicher = w.get('sicher', 'ja') or 'ja'
    a.hilfsmittel = k.get('hilfsmittel', '')
    a.abhaengig = k.get('abhaengig_von', '')
    pre = iid[:-1]
    if D.pr['ordner'] == 'abitur':
        # Vorspann-id im Abitur: Aufgabe ohne Buchstabe, bei zwei Aufgabenteilen -T1/-T2
        kand = [v for v in (pre, pre + '-T1', pre + '-T2') if v in D.wort]
        pre = next((v for v in kand if vorspann_gilt(D.wort[v], w['teil'])), kand[0] if kand else pre)
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
    if abb == 'TABELLENAUSWAHL':
        # Reparatur Punkt 7: „Tabelle 1: x = …; y = … Tabelle 2: …“ -> drei kleine Tabellen mit Ankreuzfeld
        tabs = re.findall(r'Tabelle (\d+): x = ([^;]*); y = ([^.]*(?:\.\d[^.]*)*)\.', text)
        if tabs:
            text = text[:text.find('Tabelle ' + tabs[0][0] + ':')].strip()
            bl = []
            for n, xs, ys in tabs:
                xs = [v.strip() for v in xs.split(',')]
                ys = [v.strip() for v in ys.split(',')]
                bl.append(r'\begin{tabular}[t]{@{}c@{}}\renewcommand{\arraystretch}{1.3}\begin{tabular}{|c|%s}\hline $x$ & %s \\ \hline $y$ & %s \\ \hline\end{tabular}\\[3pt]{\small Tabelle %s\enspace$\square$}\end{tabular}'
                          % ('c|' * len(xs), ' & '.join(tx(v) for v in xs), ' & '.join(tx(v) for v in ys), n))
            abb = r'\hspace{0.5cm}'.join(bl)
        else:
            abb = ''
    m_kr = re.search(r'ANKREUZ\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}$', abb or '')
    if m_kr:   # Ankreuztabellen der neuen Wortlautdateien (Lauf C)
        abb, text = ankreuz_tabelle(abb[:m_kr.start()].rstrip(), text, m_kr.groups(), a)
    elif abb == 'ANKREUZTABELLE':
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
    for x in oben_split(k['kurzloesung'], ' | '):   # Punkte (0 | −50) nicht zerschneiden (N4.18)
        x = x.strip()
        wv = re.split(r'≈|=', x)[-1].strip()
        if x and wv not in werte:   # „Sektor ≈ 52° | ≈ 52°“ nur einmal (Reparatur Punkt 6)
            teile.append(x); werte.add(wv)
    fx = abi_tx if D.pr['ordner'] == 'abitur' else tx
    a.kurz = '; '.join(fx(x) for x in teile)
    a.kurz_roh = teile   # Klartext der Teile (Ausweichwert im Fuß, Reparatur Punkt 2)
    if not k['kurzloesung']:
        D.befund(f'{iid}: kurzloesung leer')
    zw = [x.strip() for x in k['zwischenergebnis'].split(' ; ') if x.strip()]
    a.zf = [x.strip() for x in w.get('zwischenfragen', '').split(' ; ') if x.strip()]
    a.zw = [fx(z) for z in zw]
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
        if not m and c == '.' and re.match(r'\s+[A-ZÄÖÜ]', s[i + 1:i + 3] or '') \
                and not re.search(r'(^|[\s(])(z|d|u|v|bzw|ca|Nr|vgl|evtl|usw|S|B|h|a)\.$', cur):
            teile.append(cur); cur = ''   # Abkürzungen (z. B., d. h., bzw.) nicht zerreißen (Reparatur Punkt 8)
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
    # Mehrere Ergebnisse (x_1 = …, x_2 = …; Lauf B2): ab „Ergebnis:“ bzw. ab der ersten von mindestens
    # zwei indizierten Zuweisungen im letzten Abschnitt ist alles Ergebnis
    ie = next((i for i, x in enumerate(seg) if re.match(r'(Ergebnis|Antwort):', x)), None)
    if ie is not None and ie < len(seg) - 1:
        kurz = '; '.join(re.sub(r'^(Ergebnis|Antwort):\s*', '', x) for x in seg[ie:])
        return kurz, seg[:ie] + extra
    idx = list(re.finditer(r'\$?[A-Za-z]_\{?\d+\}?\s*=', seg[-1]))
    if len(idx) >= 2:
        vor = seg[-1][:idx[0].start()].rstrip(' :,')
        return seg[-1][idx[0].start():], seg[:-1] + ([vor + '$' if vor.count('$') % 2 else vor] if re.search(r'\d', vor) else []) + extra
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


DU = {'Berechnen': 'Berechne', 'Bestimmen': 'Bestimme', 'Zeigen': 'Zeige', 'Geben': 'Gib',
      'Weisen': 'Weise', 'Ermitteln': 'Ermittle', 'Untersuchen': 'Untersuche', 'Begründen': 'Begründe',
      'Skizzieren': 'Skizziere', 'Beschreiben': 'Beschreibe', 'Entscheiden': 'Entscheide',
      'Kreuzen': 'Kreuze', 'Prüfen': 'Prüfe', 'Überprüfen': 'Überprüfe', 'Zeichnen': 'Zeichne'}


def grafik_bank(D, g, iid):
    """Bank-Grafik (mathblatt-Makros) mit zwei Reparaturen beim Setzen (Lauf C; Bank unverändert,
    Zählung D.n_grafik_rep): Wörter mit Umlaut als Astname im Baum stehen im Mathemodus ($grün$ fehlt
    in der Schrift) -> \\text{grün}; ksys mit Jahreszahlen als x-Achse (xmin=2019) läuft in pgf über
    (Dimension too large) -> Achse ab 0, Beschriftung der Jahre bleibt über xlabel."""
    if not g:
        return g
    g0 = g
    if re.match(r'\\baum(zwei|drei)', g):
        g = re.sub(r'(?<=[{,])([A-Za-zÄÖÜäöüß]*[äöüÄÖÜß][A-Za-zÄÖÜäöüß]*)/', r'\\text{\1}/', g)
    m = re.match(r'\\begin\{ksys\}\[([^\]]*)\]((?:\s*\\punkt\{[^}]*\}\{[^}]*\}\{[^}]*\})+)\s*\\end\{ksys\}$', g)
    if m:
        o = dict(x.split('=', 1) if '=' in x else (x, '') for x in m.group(1).split(','))
        try:
            x0, x1, y0, y1 = (float(o[k]) for k in ('xmin', 'xmax', 'ymin', 'ymax'))
        except (KeyError, ValueError):
            x0 = y0 = 0
        if x0 > 100 or y0 > 0:
            # Achse beginnt nicht bei null bzw. Jahreszahlen: ksys zeichnet die Achsen durch den Ursprung
            # (läuft über); als pgfplots mit Achsen links/unten
            pts = re.findall(r'\\punkt\{([^}]*)\}\{([^}]*)\}', m.group(2))
            g = (r'\begin{tikzpicture}\begin{axis}[axis lines=left,width=9cm,height=6cm,xmin=%s,xmax=%s,ymin=%s,ymax=%s,'
                 r'xtick distance=%s,ytick distance=%s,grid=both,grid style={mbgitter},tick label style={font=\scriptsize},'
                 r'/pgf/number format/1000 sep={},xlabel={%s},ylabel={%s},label style={font=\small}]'
                 r'\addplot[only marks,mark=*,mark size=1.5pt] coordinates {%s};\end{axis}\end{tikzpicture}'
                 % (o['xmin'], o['xmax'], o['ymin'], o['ymax'], o.get('xstep', '1'), o.get('ystep', '1'),
                    o.get('xlabel', ''), o.get('ylabel', ''), ' '.join(f'({x},{y})' for x, y in pts)))
    m = re.search(r'\\wertetabelle(\[[^\]]*\])?\{([^{}]*)\}\{([^{}]*)\}\{([^{}]*)\}', g)
    if m:
        # Wertetabelle: Zeilennamen mit Wörtern im Mathemodus der Vorlage -> \text; breite Werte -> breitere Zelle
        k1, k2 = [('\\text{%s}' % x if re.search(r'[A-Za-zÄÖÜäöüß]{3,}', x) and '\\text' not in x else x)
                  for x in (m.group(2), m.group(3))]
        werte = re.split(r'(?<![{\\]),(?!\})', (m.group(1) or '').strip('[]')) + m.group(4).split(',')
        breit = max(len(re.sub(r'\\[,;]|[{}]', '', w)) for w in werte)
        neu = '\\wertetabelle%s{%s}{%s}{%s}' % (m.group(1) or '', k1, k2, m.group(4))
        if breit > 6:
            neu = '{\\setlength{\\mbzell}{%.1fcm}%s}' % (0.2 * breit + 0.3, neu)
        g = g[:m.start()] + neu + g[m.end():]
    if g != g0:
        D.n_grafik_rep = getattr(D, 'n_grafik_rep', 0) + 1
    return g


def bank_aufgabe(D, r, stufe):
    a = Aufgabe()
    a.art, a.id = 'bank', r['id']
    t = r['aufgabe']
    m = re.search(r'\s*\((?:P10|Abitur) (\d{4})(?: (\w+))?\)', t)
    nach = ''
    if m:
        nach = f' nach P10 {m.group(1)}'
        t = t[:m.start()] + t[m.end():]
        a.marke_text = f'nach {"Abi" if "Abitur" in m.group(0) else "P10"} ’{m.group(1)[2:]}'   # N1.4/N4.17
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
    if '\\wertetabelle' in a.text:
        a.text = grafik_bank(D, a.text, r['id'])   # Wertetabelle im Aufgabentext (Lauf C)
    a.abb = grafik_bank(D, r.get('grafik', '') or '', r['id'])
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
    lo = r['loesung']
    # Prüfungsheft ohne Siezen (Beschluss 17): zitierte Operatoren der Bank („Zeigen Sie, …“) beim
    # Setzen in Du-Form; die Bankzeile bleibt (Befund, Zählung D.n_sie)
    t0 = a.text
    a.text = re.sub(r'\b(' + '|'.join(DU) + r') Sie\b', lambda m: DU[m.group(1)], a.text)
    if a.text != t0:
        D.n_sie = getattr(D, 'n_sie', 0) + 1
    if D.pr['ordner'] == 'abitur':
        lo = lo.replace('\\Leftrightarrow', '\\Rightarrow').replace('⇔', '⇒')   # nur ⇒ (Lösungsblatt 05.10.)
        # Schlusssatz „…: die Gerade ist $y = -x$.“ -> Ergebnis ist der Ausdruck nach dem letzten „ist“
        lo = re.sub(r':\s*(die|der|das)\s+\w+\s+ist\s+(\$[^$]+\$)\.?\s*$', r'; Ergebnis: \2', lo)
    kurz, zw = bank_loesung(lo)
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
# Nachtrag 06.10. (beschluesse-2026-10-06b.md): fremde und herausgelöste Aufgaben, Vielfalt
# ---------------------------------------------------------------------------
def norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip().lower())


def stufe_trifft(wert, st_name):
    """Stufenangabe der neuen Daten trifft die Stufe der Zuordnung. Form „Stufe“ oder „kapitel:Stufe“ (dann
    nur im Kapitel des Baus), mehrere mit „|“. Gleich oder (ab sechs Zeichen) enthalten."""
    n = norm(st_name)
    for w in (wert or '').split('|'):
        w = norm(w)
        if ':' in w:
            k, w = w.split(':', 1)
            if D_AKT is not None and not kapitel_passt(k, D_AKT.kapitel):
                continue
            w = w.strip()
        if w and (w == n or (len(w) >= 6 and len(n) >= 6 and (w in n or n in w))):
            return True
    return False


ZAHLART = [('kopf', 0), ('ganz', 0), ('glatt', 1), ('krumm', 2), ('dezimal', 2), ('komma', 2),
           ('bruch', 2), ('rund', 2), ('wurzel', 2), ('pi', 2)]


def zahlart_wert(z, a=None):
    z = norm(z)
    for k, v in ZAHLART:
        if k in z:
            return v
    return zahlklasse(a) if a is not None else 1


def jahr_kurz(j):
    return '’' + str(j)[2:]


def daten_aufgabe(D, r, stufe, art):
    """Zeile aus msa/fremd/*.csv bzw. msa/herausgeloest-p10.csv -> Aufgabe (art fremd | heraus).
    wortlaut, abbildung und loesung sind Klartext mit $…$ wie der eigene Wortlaut; schritte ist eine Zahl
    oder eine Liste „a ; b“ (dann Zwischenergebnisse)."""
    a = Aufgabe()
    a.art, a.id = art, r.get('id', '')
    a.text = tx(r.get('wortlaut', ''))
    vor, opts = ankreuz_zerlegen(r.get('wortlaut', ''))
    if 'kreuz' in norm(r.get('darstellung', '') + r.get('fragerichtung', '')) and opts:
        a.text, a.optionen, a.kreuz = tx(vor), [tx(o) for o in opts], True
    a.abb = abbildung(r.get('abbildung', '') or '', D, a.id) if (r.get('abbildung') or '').strip() else ''
    lo = (r.get('loesung') or '').strip()
    a.kurz_roh = [x.strip() for x in lo.split(' | ') if x.strip()]
    a.kurz = '; '.join(tx(x) for x in a.kurz_roh)
    sch = (r.get('schritte') or '').strip()
    if re.fullmatch(r'\d+', sch):
        a.schritte = sch
        a.zw_roh = []
    else:
        a.zw_roh = [x.strip() for x in sch.split(' ; ') if x.strip()]
        a.schritte = str(max(1, len(a.zw_roh)))
    a.zw = [tx(z) for z in a.zw_roh]
    a.zw_wort = ['' if hat_wort(z) else wort_fuer(z, i, [], len(a.zw_roh), stufe) for i, z in enumerate(a.zw_roh)]
    m = (r.get('marke') or '').strip()
    el = (r.get('eltern_id') or '').strip()
    if art == 'heraus':
        a.orig = el
        if '-GYM-' in el and m:
            m = re.sub(r'P10', 'GYM', m)   # F2 (07.10.): GYM zählt nicht als P10, Marke ohne „P10“
        if not m and re.match(r'\d{4}', el):
            m = f'nach {D.pr["marke"]} {jahr_kurz(el[:4])}'   # Marke „nach P10 ’15“ (N1.4)
        elif m and not m.startswith('nach'):
            m = 'nach ' + m
    a.marke_text = m
    jm = re.search(r'(\d{4})', el or r.get('quelle', '') or '')
    a.jahr = int(jm.group(1)) if jm else 0
    a.fund = (r.get('quelle') or '').strip()   # nur in den Daten (N4.17), nie auf dem Blatt
    a.hrang = 3 if art == 'fremd' else 2
    a.rang = 2.0
    a.zahlart = r.get('zahlart', '')
    try:
        a.woerter = int(r.get('woerter') or 0)
    except ValueError:
        a.woerter = 0
    a.richtung_d = norm(r.get('fragerichtung', ''))
    a.darstellung_d = norm(r.get('darstellung', ''))
    a.stern = False
    return a


def woerter(a):
    return a.woerter or len(re.findall(r'[A-Za-zÄÖÜäöüß]{2,}', klartext(a.text)))


def darstellung(a):
    """Darstellung (N1.3, N2.8): text | tabelle | bild | diagramm."""
    d = getattr(a, 'darstellung_d', '')
    for k in ('tabelle', 'diagramm', 'bild', 'text'):
        if k in d:
            return k
    g = (a.abb or '') + ' ' + (a.text if '\\wertetabelle' in a.text else '')
    if re.search(r'tabular|sachtabelle|wertetabelle|dreisatz|leerzelle', g):
        return 'tabelle'
    if re.search(r'begin\{axis\}|ksys|saeule|säule|balken|kreisdiagramm|baum', g, re.I):
        return 'diagramm'
    if re.search(r'tikzpicture|streifen|includegraphics|dreieck|viereck', g):
        return 'bild'
    if a.art == 'bank' and a.form in ('streifenfeld', 'streifenleer'):
        return 'bild'
    if a.art == 'bank' and a.form in ('tabelle', 'dreisatz'):
        return 'tabelle'
    return 'text'


def richtung(a):
    """Fragerichtung (N1.3): aus den Daten, sonst Vergleich/Ankreuzen/gesuchte Größe (Prozent)."""
    d = getattr(a, 'richtung_d', '')
    if d:
        return d
    if getattr(a, 'gruppe', '') == 'Vergleich':
        return 'pruefen'
    if a.kreuz or a.optionen:
        return 'ankreuzen'
    return gesucht(a) or 'vorwaerts'


STOPP = set("""Prozent Prozentsatz Prozentwert Grundwert Menge Ganze Ganzen Ganzes Zahl Zahlen Aufgabe Ergebnis
Tabelle Streifen Rechne Berechne Bestimme Gib Wie Was Kreuze Trage Ermittle Begründe Prüfe Entscheide Schreibe
Runde Teil Teile Wert Werte Anteil Lösung Euro Stelle Stellen Rechnung Graph Funktion Gleichung Term
Abschnitt Ende Nachkommastelle Dezimalzahl Bruch Ist Sind Das Die Der Ein Eine Er Sie Es Im In Am Von Um Auf
Mit Zu Bei Nach Für Wenn Dann Hier Rechnet Erkläre Markiere Kästchen
Strecke Betrag Betrags Größe Länge Masse Gewicht Zahlenwert Anzahl Teils Mengen Strecken""".split())   # Einheit/Größe ist keine Sache


def sache(a):
    """Sache einer Aufgabe: Hauptwörter ohne Fachwörter der Rechnung (Entscheidung)."""
    return {w for w in re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]{3,}\b', klartext(a.text)) if w not in STOPP}


def gerippe(a):
    return re.sub(r'\d+(?:[,.]\d+)?', '#', klartext(a.text))


def gleichartig(a, b):
    """Zwei Aufgaben gleichen sich in Sache UND Darstellung UND Fragerichtung (N1.3). Sache gleich (Entscheidung):
    Text bis auf die Zahlen zu mindestens 85 % gleich (Kopien „Äpfel 10/50/25/20 %“), oder die Sachwörter decken
    sich mindestens zur Hälfte der kleineren Menge."""
    import difflib
    if darstellung(a) != darstellung(b) or richtung(a) != richtung(b):
        return False
    if difflib.SequenceMatcher(None, gerippe(a), gerippe(b)).ratio() >= 0.85:
        return True
    sa, sb = sache(a), sache(b)
    if a.art == 'bank' and b.art == 'bank' and not sa and not sb:
        # zwei eigene ohne Sache („9 % einer Menge sind 63 kg“, „64 % einer Strecke sind 52 m“): verschieden
        # nur in Zahl und Einheit – eine Einheit ist keine Sache (Sichtprüfung Fokus 06.10.)
        D_AKT.n_ohne_sache = getattr(D_AKT, 'n_ohne_sache', 0) + 1
        return True
    return bool(sa and sb) and 2 * len(sa & sb) >= min(len(sa), len(sb))


def eigene_sparsam(D, aufg):
    """N1.3: eine eigene (Bank-)Aufgabe, die einer echten, fremden, herausgelösten oder einer schon gewählten
    eigenen in Sache, Darstellung und Fragerichtung gleicht, fällt weg; Leiterplätze (fest) bleiben."""
    halten = [a for a in aufg if a.art in ('echt', 'fremd', 'heraus', 'zone', 'erkennen') or a.fest]
    eigene = []
    # je Gruppe gleichartiger bleibt die leichteste (passt unten in die Leiter; Entscheidung)
    for a in sorted(aufg, key=lambda x: (getattr(x, 'zk', 0), schrittzahl(x), getattr(x, 'tl', 0), x.id)):
        if any(a is h for h in halten):
            continue
        n0 = getattr(D, 'n_ohne_sache', 0)
        if any(gleichartig(a, b) for b in halten + eigene):
            if getattr(D, 'n_ohne_sache', 0) > n0:
                D.n_ohne_sache_weg = getattr(D, 'n_ohne_sache_weg', 0) + 1
            D.n_eigen_weg += 1
            D.eigen_weg = getattr(D, 'eigen_weg', []) + [a.id]
            continue
        eigene.append(a)
    return [a for a in aufg if any(a is x for x in halten + eigene)]


def schwerste_echt(echte):
    """Maßstab für fremde Aufgaben (N1.2): Schritte, Zahlart, Textlänge der BB/BE-Aufgaben der Stufe, je
    Merkmal das Maximum (Entscheidung: eine fremde darf in keinem Merkmal darüber liegen)."""
    bb = [a for a in echte if bbbe(a)]   # Maßstab: BB/BE ganz oder herausgelöst (N1.2, Fokus 06.10.)
    if not bb:
        return None
    return (max(schrittzahl(a) for a in bb), max(a.zk for a in bb), max(woerter(a) for a in bb))


UNSICHER = re.compile(r'unsicher|\?|erschlossen', re.I)


def kandidat(D, r, st, art, mass):
    """Zeile aus fremd/herausgelöst als Aufgabe, wenn sie zeichenbar und nicht schwerer als die BB/BE der
    Stufe ist (N1.2; herausgelöste aus P10 ohne Maßstab-Grenze); sonst None."""
    n_bef = len(D.befunde)
    try:
        a = daten_aufgabe(D, r, st.name, art)
    except Exception as e:   # Abbildungsbeschreibung, die das Zeichenprogramm nicht versteht: Zeile nicht setzen
        del D.befunde[n_bef:]
        D.fremd_ohne_bild = getattr(D, 'fremd_ohne_bild', []) + [r.get('id', '')]
        return None
    if (r.get('abbildung') or '').strip() and (not a.abb or len(D.befunde) > n_bef):
        del D.befunde[n_bef:]
        D.fremd_ohne_bild = getattr(D, 'fremd_ohne_bild', []) + [a.id]
        return None
    kennzahlen(D, a)
    if a.zahlart:
        a.zk = zahlart_wert(a.zahlart, a)
    p10 = art == 'heraus' and a.marke_text.startswith('nach ' + D.pr['marke'])
    if p10:
        a.schritte = str(rechenschritte(r.get('loesung') or '', schrittzahl(a)))
    if not p10:
        s_daten = schrittzahl(a)
        a.schritte = str(max(s_daten, schritte_geschaetzt(a, r)))
        if mass and int(a.schritte) > mass[0] and s_daten <= mass[0]:
            # erst die Schätzung macht sie zu schwer (Rückwärts vom vermehrten/verminderten Grundwert)
            D.n_zweischritt = getattr(D, 'n_zweischritt', 0) + 1
        if (mass and (schrittzahl(a) > mass[0] or a.zk > mass[1] or woerter(a) > mass[2])) \
                or (not mass and schrittzahl(a) > 2):
            D.fremd_zu_schwer = getattr(D, 'fremd_zu_schwer', 0) + 1
            return None
    a.unsicher = bool(UNSICHER.search(r.get('bemerkung') or ''))
    return a


def rechenschritte(lo, standard):
    """Schritte einer herausgelösten Aufgabe aus ihrer Lösung (Sichtprüfung 06.10.: „G = 4 : 2/3 = 6 Kugeln
    (1/3 sind 2 Kugeln)“ ist ein Schritt, auch wenn die Daten 2 sagen): Rechenzeichen der Lösung ohne
    Klammerzusätze, Brüche a/b nicht gezählt; höchstens die Zahl aus den Daten."""
    t = re.sub(r'\([^()]*[A-Za-zÄÖÜäöü]{3}[^()]*\)', '', lo)
    t = t.split('|')[0]
    n = len(re.findall(r'\s[:·×+−-]\s', t))
    return max(1, min(standard, n)) if n else standard


def schritte_geschaetzt(a, r):
    """Schritte einer fremden Aufgabe aus Text und Lösung (Sichtprüfung Fokus Grundwert 06.10.): Die Daten
    zählen „440 € : 1,1“ als einen Schritt; der Faktor 1 ± p/100 aus „10 % mehr“, „+20 %“, „20 % Rabatt“
    ist aber ein eigener Schritt (vermehrter/verminderter Grundwert, Prozentwert mit Veränderung). Erkannt:
    die Lösung teilt oder multipliziert mit einer Dezimalzahl 1 ± p/100 zu einem Prozentsatz p des Texts
    (p ≠ 100). Sonst die Zahl aus den Daten."""
    s = 1
    lo = (r.get('loesung') or '') + ' ' + (r.get('schritte') or '')
    ps = {v for v, pr, _ in zahlen(a.text) if pr and 0 < v < 100}
    for m in re.finditer(r'[:·]\s*(\d+,\d+)', lo):
        f = float(m.group(1).replace(',', '.'))
        if any(abs(f - (1 + p / 100)) < 1e-9 or abs(f - (1 - p / 100)) < 1e-9 for p in ps):
            s = 2
    return s


def bbbe(a):
    """BB/BE-Original: echt oder aus einem P10-Original herausgelöst („nach P10 ’15“)."""
    return a.art == 'echt' or (a.art == 'heraus' and (a.marke_text or '').startswith('nach ' + D_AKT.pr['marke']))


def merkmale(a):
    return (frozenset(sache(a)), darstellung(a), richtung(a))


def auffuellen(D, st, echte, steckt, B):
    """Ersetzt durch N5.20 (blatt_kandidaten, spruenge_fuellen); nicht mehr aufgerufen. Fremde und herausgelöste Aufgaben bis zur Zielzahl der Stufe (12 Kern, 6 sonst, zusammen mit den
    echten). Heft: leichtere fremde zuerst (N1.2), dann herausgelöste; Fokus: alle herausgelösten der
    BB/BE-Originale stehen schon (platz_ids), fremde bis zur Zielzahl. Vielfalt vor Menge: zuerst je neue
    Kombination aus Darstellung und Fragerichtung bzw. neue Sache, gleichartige (N1.3) gar nicht. Zeilen mit
    „unsicher“, „?“ oder „erschlossen“ in bemerkung nur, wenn sonst die Zielzahl fehlt (gezählt)."""
    soll = 12 if st.kern else 6
    frei = soll - len(echte)
    if frei <= 0:
        return []
    mass = schwerste_echt(echte)
    kand = []
    for r in D.fremd:
        if r.get('id') not in B.benutzt and stufe_trifft(r.get('stufe'), st.name):
            a = kandidat(D, r, st, 'fremd', mass)
            if a:
                kand.append((0, a))
    if not FOKUS_LAUF:
        for r in D.heraus:
            if r.get('id') in B.benutzt or not stufe_trifft(r.get('stufe'), st.name):
                continue
            if (r.get('eltern_id') or '').strip() in steckt:
                continue   # steht als „steckt auch in“ (N2.6)
            a = kandidat(D, r, st, 'heraus', mass)
            if a:
                kand.append((1, a))
    # leichte zuerst innerhalb der Herkunft (fremde vor herausgelösten), sichere vor unsicheren
    kand.sort(key=lambda x: (x[1].unsicher, x[0], x[1].zk, schrittzahl(x[1]), woerter(x[1])))
    wahl = []
    gesehen = {merkmale(a)[1:] for a in echte}
    for runde in (0, 1, 2):
        for _, a in kand:
            if len(wahl) >= frei:
                break
            if any(a is w for w in wahl) or (runde < 2 and a.unsicher):
                continue
            if any(gleichartig(a, b) for b in echte + wahl):
                continue
            if runde == 0 and merkmale(a)[1:] in gesehen:
                continue   # erst neue Darstellung/Fragerichtung (Vielfalt vor Menge)
            wahl.append(a)
            gesehen.add(merkmale(a)[1:])
    for a in wahl:
        B.benutzt.add(a.id)
        if a.art == 'fremd':
            D.n_fremd += 1
        else:
            D.n_heraus += 1
        if a.unsicher:
            D.n_unsicher = getattr(D, 'n_unsicher', 0) + 1
    return wahl


def blatt_kandidaten(D, st, echte, steckt, B):
    """N5.20 (Auffüllen B): (1) alle herausgelösten der P10-Originale der Stufe (ohne die, deren Original als
    „steckt auch in“ steht, N2.6; ohne unsichere) – sie stehen fest auf dem Blatt; (2) der Vorrat für die
    Sprünge: fremde und herausgelöste anderer Länder, nie schwerer als die BB/BE der Stufe, keine unsicheren
    („unsicher“, „?“, „erschlossen“ in bemerkung). Fokus: die herausgelösten stehen schon (platz_ids)."""
    heraus, pool = [], []
    if not FOKUS_LAUF:
        for r in D.heraus:
            if r.get('id') in B.benutzt or not stufe_trifft(r.get('stufe'), st.name):
                continue
            if (r.get('eltern_id') or '').strip() in steckt:
                continue
            a = kandidat(D, r, st, 'heraus', None)
            if a and bbbe(a) and not a.unsicher:
                B.benutzt.add(a.id); D.n_heraus += 1
                heraus.append(a)
    mass = schwerste_echt(echte + heraus)
    if not mass:
        return heraus, []
    for her, quelle in ((0, D.fremd), (1, D.heraus)):
        for r in quelle:
            if r.get('id') in B.benutzt or not stufe_trifft(r.get('stufe'), st.name):
                continue
            a = kandidat(D, r, st, 'fremd' if her == 0 else 'heraus', mass)
            if a and not a.unsicher and not bbbe(a):
                pool.append((her, a))
    return heraus, pool


def spruenge_fuellen(D, st, kern, basis, pool):
    """N5.20: Leiter = Vorstufen/Grundwert-Leiter (unten, bleiben) und die Aufgaben der Stufe, geordnet. Ein
    Sprung zwischen zwei aufeinanderfolgenden Aufgaben: Zahlklasse oder Schritte steigen um 2 oder mehr
    (ohne Vorstufe beginnt die Leiter bei Zahlklasse 0, 1 Schritt). Je Sprung höchstens eine Aufgabe aus dem
    Vorrat, die dazwischen liegt (beide Merkmale im Bereich, nicht gleich einem Ende) und den Sprung am
    besten teilt; bei Gleichstand fremde vor herausgelösten anderer Länder vor eigenen, dann kürzere.
    Gleichartige (N1.3) nie. Entscheidung: der Sprung wird zwischen den Aufgaben der Stufe gemessen,
    der Füller nicht erneut geprüft."""
    import functools
    def sk(a):
        return (a.zk, schrittzahl(a))
    leiter = sorted(kern, key=functools.cmp_to_key(vergleich))
    unten = sorted(basis, key=functools.cmp_to_key(vergleich))
    punkte = [sk(unten[-1]) if unten else (0, 1)] + [sk(a) for a in leiter]
    wahl = []
    for (z1, s1), (z2, s2) in zip(punkte, punkte[1:]):
        if z2 - z1 < 2 and s2 - s1 < 2:
            continue   # nur aufwärts (Entscheidung: ein Abstieg nach der Leiter ist keine Lücke)
        D.n_sprung = getattr(D, 'n_sprung', 0) + 1
        zl, zh = sorted((z1, z2))
        sl, sh = sorted((s1, s2))
        best = None
        for her, a in pool:
            if any(a is w for w in wahl):
                continue
            z, s = sk(a)
            if not (zl <= z <= zh and sl <= s <= sh) or (z, s) in ((z1, s1), (z2, s2)):
                continue
            if any(gleichartig(a, b) for b in kern + basis + wahl):
                continue
            g = max(max(abs(z - z1), abs(s - s1)), max(abs(z2 - z), abs(s2 - s)))
            k = (g, her, sb_raster_rang(D, a), woerter(a), a.id)
            if best is None or k < best[0]:
                best = (k, a)
        if best:
            wahl.append(best[1])
        else:
            D.n_sprung_offen = getattr(D, 'n_sprung_offen', 0) + 1
    return wahl


FOKUS_LAUF = False


def fremde_fuer(D, st, echte, B):
    """Fremde Aufgaben der Stufe (N1.1–2): nur, wenn BB/BE weniger als 12 (Kern) bzw. 6 echte hat; nie
    schwerer als die schwerste BB/BE-Aufgabe; höchstens bis zur Sollzahl. Ohne echte gibt es keinen
    Maßstab: dann nur Aufgaben mit höchstens zwei Schritten (Entscheidung)."""
    soll = 12 if st.kern else 6
    if len(echte) >= soll or not D.fremd:
        return []
    mass = schwerste_echt(echte)
    kand = []
    for r in D.fremd:
        if r.get('id') in B.benutzt or not stufe_trifft(r.get('stufe'), st.name):
            continue
        n_bef = len(D.befunde)
        a = daten_aufgabe(D, r, st.name, 'fremd')
        if (r.get('abbildung') or '').strip() and (not a.abb or len(D.befunde) > n_bef):
            # Abbildung nicht zeichenbar (unbekannter Typ oder nur Rahmen): fremde Aufgabe nicht ohne ihr Bild
            D.fremd_ohne_bild = getattr(D, 'fremd_ohne_bild', []) + [a.id]
            del D.befunde[n_bef:]
            continue
        kennzahlen(D, a)
        if a.zahlart:
            a.zk = zahlart_wert(a.zahlart, a)
        s_, z_, w_ = schrittzahl(a), a.zk, woerter(a)
        if (mass and (s_ > mass[0] or z_ > mass[1] or w_ > mass[2])) or (not mass and s_ > 2):
            D.fremd_zu_schwer = getattr(D, 'fremd_zu_schwer', 0) + 1
            continue
        kand.append(a)
    wahl = kand[:soll - len(echte)]
    for a in wahl:
        B.benutzt.add(a.id)
    D.n_fremd += len(wahl)
    return wahl




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
    if quadrat_drin(a.text + ' ' + erg + ' ' + ' '.join(getattr(a, 'zw_roh', []) or [])):
        return 1   # B10 (07.10.): 36² + 15² ist nicht „Kopf“, sondern Taschenrechner (glatt)
    zs = zahlen(a.text)
    if any(p and v != int(v) for v, p, _ in zs):
        return 2
    kopf = True
    for v, p, roh in zs:
        if p:
            kopf &= v == int(v) and (int(v) in KOPF_P or int(v) < 10 or int(v) % 10 == 0)   # 1–9 %, Zehnerschritte, 25/75 %
        else:
            kopf &= v == int(v) and len(str(int(v)).strip('0')) <= 2
    for v, p, roh in zahlen(a.kurz):
        if ',' in roh and len(roh.split(',')[1].rstrip('0')) > 1:
            kopf = False
    return 0 if kopf and zs else 1


def quadrat_drin(t):
    """B10: Quadrat oder Potenz einer Zahl über 12 oder mit Komma (36², 1,2², 85^2, 7\\,225) im Text oder in der
    Lösung – dann nicht im Kopf rechenbar."""
    t = (t or '').replace('{,}', ',').replace('\\,', '').replace('{', '').replace('}', '')
    for m in re.finditer(r'(\d+(?:,\d+)?)\s*(?:²|³|\^\s*\d)', t):
        v = m.group(1)
        if ',' in v or float(v) > 12:
            return True
    return bool(re.search(r'√\s*\(?\s*\d{3,}|\\sqrt\s*\d{3,}', t))


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
PH = ' (Prüfungshöhe)'   # Gruppen auf Prüfungshöhe stehen in jeder Stufe zuletzt (Reparatur Punkt 1)


def gruppen_schluessel(x):
    # leichteste Aufgabe: Zahlklasse, dann Grundfall im Kopf; bei Gleichstand Punkt 8 (Entscheidung)
    g = x[0].replace(PH, '')
    return (schluessel(x[2][0])[:2], GRUPPEN.index(g) if g in GRUPPEN else 9)


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
    if re.search(r'\d\s*% von|spart|Nachlass|Rabatt|Zinsen|kostet|bezahl|neue|% davon|Mehrwertsteuer', q):
        return 'Prozentwert'
    # Korrektur Lauf C: „40 % von 65 Kindern … Wie viele …?“ und Lösungshinweis „Prozentwert gesucht“
    if re.search(r'\d\s*% von \d', t) and re.search(r'[Ww]ie viele?\b', q):
        return 'Prozentwert'
    for z in getattr(a, 'zw_roh', []) or []:
        m = re.search(r'(Prozentwert|Grundwert|Prozentsatz) gesucht', z)
        if m:
            return m.group(1)
    return ''


HRANG = {'vorstufe': 0, 'grundfall': 1, 'sprosse': 2, 'pflicht': 2, 'pruefung': 3}


def schrittzahl(a):
    """Schritte: echte Aufgaben aus dem Katalogfeld schritte; Bankaufgaben = Zwischenergebnisse mit
    Rechnung (Operator) + 1, höchstens 4."""
    if a.art in ('echt', 'fremd', 'heraus') and re.sub(r'\D', '', a.schritte or ''):
        return max(1, int(re.sub(r'\D', '', a.schritte or '1') or 1))
    n = sum(1 for z in (a.zw_roh or []) if re.search(r'\s(:|·|-|−|\+)\s|\\cdot|frac', z))
    return min(4, max(1, n))


def schwierigkeit(a):
    """Schwierigkeit nach Korrektur Lauf C (Regel b): Zahlklasse (Kopf, glatt, krumm), Grundfall im
    Kopf zuerst (Muster 6), Schritte, Fragen, Textlänge, Satzmuster; Herkunft (echt/eigen) und
    Bank-Höhe zählen nicht. Danach nur noch zum festen Ordnen: Punkte, id."""
    pkt = int(a.punkte) if a.art == 'echt' and str(a.punkte).isdigit() else 0
    unten = 0 if (a.zk == 0 and a.hrang <= 1) else 1
    return (a.zk, unten, schrittzahl(a), min(a.fz, 2), a.tl, a.sr, pkt, a.id)


def prozentrang(a):
    """Leiter innerhalb der Zahlklasse für das Kapitel Prozent (Korrektur Lauf C Punkt 1): 100/50/10 %
    -> 25/20/75 % -> 1 % -> Zehnerschritte -> 5, 2 und andere ganze -> Kommaprozent; bei mehreren Sätzen
    zählt der schwerste. Andere Kapitel: 0."""
    if D_AKT is None or D_AKT.kapitel != 'prozent':
        return 0
    ps = [v for v, p, _ in zahlen(a.text) if p]
    if not ps:
        return 0
    def r(v):
        if v != int(v):
            return 5
        v = int(v)
        if v in (100, 50, 10):
            return 0
        if v in (25, 20, 75):
            return 1
        if v == 1:
            return 2
        if v % 10 == 0:
            return 3
        return 4
    return max(r(v) for v in ps)


def vergleich(a, b):
    """Reihenfolge zweier Aufgaben (Korrektur Lauf C): weichen die Schritte um 2 oder mehr ab, entscheiden
    die Schritte; sonst Zahlklasse, im Kapitel Prozent dann der Prozentsatz-Rang, dann die übrige
    Schwierigkeit (Grundfall im Kopf, Schritte, Fragen, Text, Satzmuster, Punkte, id)."""
    sa, sb = schrittzahl(a), schrittzahl(b)
    if abs(sa - sb) >= 2:
        return -1 if sa < sb else 1
    ka = (a.zk, prozentrang(a)) + schwierigkeit(a)[1:]
    kb = (b.zk, prozentrang(b)) + schwierigkeit(b)[1:]
    return (ka > kb) - (ka < kb)


def schluessel(a):
    """Reihenfolge (Beschlüsse 2, 8; Reparatur 06.10.): Zahlklasse (kopfrechenbar, glatt, krumm),
    Schrittzahl, Fragenzahl, Höhe der Bank (Vorstufe, Grundfall, Sprosse, Prüfung), Textlänge,
    Prozentsatz-Muster (10, 50, 25, 1, 20 %), Punkte; die Prüfungsherkunft entscheidet erst danach
    (eigene vor echter bei Gleichstand, jüngere Prüfung zuerst)."""
    pkt = int(a.punkte) if a.art == 'echt' and str(a.punkte).isdigit() else 0
    unten = 0 if (a.zk == 0 and a.hrang <= 1) else 1   # Grundfall im Kopf zuerst (Muster 6)
    return (a.zk, unten, schrittzahl(a), min(a.fz, 2), min(a.hrang, 3), a.tl, a.sr, pkt, a.id)


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
        # „(i)“ = innermathematisch markiert (zuordnung-stand.md); „[…]“ = Prüfungs-ids der Sprosse
        self.sprossen = [re.sub(r'\[.*\]|\(i\)$', '', s) for s in z['bank_sprossen'].split()]
        self.ziel = 's' + re.sub(r'[^a-z]', '', self.name.lower())[:20]
        self.vor = []          # Vorstufen (Aufgabe)
        self.gruppen = []      # [(name, wort, [Aufgabe])]
        self.reserve = []
        self.luecken = []
        # Nachtrag 06.10. (Zuordnung, neue Spalten): jahre_letzte5 (N2.7), nebenplaetze (N2.6),
        # verwechselbar (N4.19); leer = wie bisher
        self.jahre5 = (z.get('jahre_letzte5') or '').strip()
        self.neben_ids = [x for x in re.split(r'[\s|,]+', z.get('nebenplaetze') or '') if x]
        self.verwechselbar = [x.strip() for x in re.split(r'[|,]', z.get('verwechselbar') or '') if x.strip()]
        self.steckt = []       # [(id, Aufgabe)] „steckt auch in Nr. n“ (N2.6), Nr. beim Setzen
        self.erkennen = None   # Aufgabe (N4.19)
        self.leiter = []       # feste Grundwert-Leiter (N2.11)
        self.verst = []        # Verständnis-Sprosse aus dem Steckbrief (N6.27)
        self.merke = ''        # Merkkasten aus dem Steckbrief (LaTeX)
        self.sb_leiter = []


def kopfname(st):
    return BEZEICHNUNG.get(st.name, tx(st.name))


def jahre_info(D, st):
    """Grau hinter dem Stufennamen (Beschluss 13): „in k der letzten 5 Prüfungen“, sonst „selten
    geprüft“. Prüfungsjahre: OS- und FOR-Hefte. Zählung B (Nachtrag N2.7): steht in der Zuordnung
    jahre_letzte5 (Zahl oder Jahresliste; Jahre, in denen der Handgriff gebraucht wurde, auch als
    Zwischenschritt), gilt sie; sonst zählen die Hauptplätze und die Zwischenschritt-Plätze aus
    handgriffe-p10.csv."""
    alle = sorted({int(j) for j in D.pruefjahre})
    letzte5 = alle[-5:]
    if st.jahre5:
        js = re.findall(r'\d{4}', st.jahre5)
        k = len({int(j) for j in js} & set(letzte5)) if js else int(re.sub(r'\D', '', st.jahre5) or 0)
        D.zaehlung_b = True
        return (f'in {k} der letzten 5 Prüfungen', False) if k else ('selten geprüft', True)
    jahre = {int(D.kat[i]['jahr']) for i in st.ids if i in D.kat}
    for iid, h in D.handgriffe.items():
        if iid in D.kat and (stufe_trifft(h.get('zwischenschritt'), st.name) or stufe_trifft(h.get('ganz_auch'), st.name)):
            jahre.add(int(D.kat[iid]['jahr']))
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
    for ein in D.eintraege:
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
    if not D.pr['stern']:
        return False   # Abitur: kein Stern (Lauf B2)
    """* für Aufgaben, die nur FOR sind (Beschluss 26): Katalogfeld stern ja (Sternaufgabe der
    OS-Hefte = Niveaustufe G außerhalb der EBR-Liste) oder ein FOR-Heft-Teil ohne EBR-Zwilling."""
    k = D.kat.get(iid)
    if not k:
        return False
    if k.get('stern') == 'ja':
        return True
    return k['papier'] == 'FOR' and iid not in D.ebr_zwilling


def platz_ids(D, st, alle_namen, kap_ids, fokus):
    """Echte Aufgaben der Stufe (N2.5/N2.6). Ohne handgriffe-p10.csv: die Zuordnung. Mit: Aufgaben der
    Zuordnung bleiben, außer ihr Hauptplatz ist eine andere Stufe dieses Hefts; dazu Aufgaben mit Hauptplatz
    hier (nur Aufgaben dieses Kapitels) und ganz_auch hier (Zuordnung nebenplaetze bzw. handgriffe ganz_auch:
    der Handgriff ist die ganze Aufgabe – ganz in der Stufe). Entscheidung: liegt der Hauptplatz einer
    ganz_auch-Aufgabe selbst im Heft, steht sie dort ganz und hier nur „steckt auch in“ (jede Aufgabe einmal).
    Zwischenschritt-Aufgaben: im Heft „steckt auch in“ (nur mit Nummer im Heft), im Fokus herausgelöst.
    Rückgabe (ids ganz, ids „steckt auch in“, ids herauszulösen)."""
    if not D.handgriffe:
        return list(st.ids), [], []
    H = D.handgriffe
    def im_heft(feld):
        return any(stufe_trifft(feld, n) for n in alle_namen)
    def anderswo(i):
        h = H.get(i)
        if not h or not (h.get('hauptplatz') or '').strip():
            return False
        if stufe_trifft(h['hauptplatz'], st.name):
            return False
        if stufe_trifft(h.get('ganz_auch'), st.name) and (fokus or not im_heft(h['hauptplatz'])):
            return False
        return im_heft(h['hauptplatz'])
    ids = [i for i in st.ids if not anderswo(i)]
    steckt = [i for i in st.ids if i not in ids]
    ganz_auch = [i for i, h in H.items() if stufe_trifft(h.get('ganz_auch'), st.name)] + st.neben_ids
    for i, h in H.items():
        if i in ids or i not in D.kat:
            continue
        if stufe_trifft(h.get('hauptplatz'), st.name) and (fokus or i in kap_ids):
            ids.append(i)
    for i in ganz_auch:
        if i in ids or i in steckt or i not in D.kat:
            continue
        h = H.get(i, {})
        if not fokus and im_heft(h.get('hauptplatz')):
            steckt.append(i)
        else:
            ids.append(i)
    zw = [i for i, h in H.items() if i not in ids and i not in steckt and i in D.kat
          and stufe_trifft(h.get('zwischenschritt'), st.name)]
    if fokus:
        return ids, [], zw
    return ids, steckt + zw, []


# ---------------------------------------------------------------------------
# Steckbriefe (mathe-nachhilfe/katalog/steckbrief/*.md, werkzeuge/steckbrief.py; Lauf 06.10. abends)
# Gibt es zum Fokus einen Steckbrief, nimmt das Fokusblatt daraus: Verständnis-Sprosse als erste Sprosse
# der Leiter (N6.27), Merkkasten (Begriff, Merkregel), typische Fehler (Lösungsdatei), den unteren Teil der
# Leiter (Leiter-Bank), die Voraussetzungen des Rückblicks (N6.29.8) und Raster/Formulierungen als Vorzug
# bei eigenen Aufgaben in Sprüngen. Ohne Steckbrief: wie bisher.
# ---------------------------------------------------------------------------
VERSTAENDNIS = 'Verständnis'


def sb_schluessel(sp):
    m = re.match(r'[a-z-]+?-e(\d+)-k(\d+)-s(\d+)', sp)
    return tuple(int(x) for x in m.groups()) if m else (99, 99, 99)


def sb_stufenfolge(D, sb, stufen):
    """Stufen des Steckbriefs in der Folge seiner Leiter: nach der kleinsten Bank-Sprosse (Einheit, Kette,
    Sprosse) jeder Stufe (Entscheidung; Pythagoras: Hypotenuse/Kathete direkt vor Gleichung ankreuzen vor
    Teildreieck in Figur, wie Leiter (Katalog))."""
    def k(st):
        ks = [sb_schluessel(sp) for sp in st.sprossen if not re.match(r'(msa|abitur)/', sp)]
        return min(ks) if ks else (99, 99, 99)
    return sorted(stufen, key=k)


def sb_stufe_fuer(sp, stufen):
    s = sprosse_von(sp)
    for st in stufen:
        if s in st.sprossen:
            return st.name
    # sonst die Stufe, die die meisten Sprossen derselben Kette trägt (Teildreieck nachfahren -> Figur/Körper)
    n = [(sum(1 for x in st.sprossen if kette_von(x) == kette_von(s)), -i, st.name) for i, st in enumerate(stufen)]
    best = max(n)
    return best[2] if best[0] else stufen[0].name


def sb_zuteilen(D, sb, stufen):
    """Leiter-Bank und Verständnis-Bank des Steckbriefs auf die Stufen des Blatts: Verständnis in die erste
    Stufe; jede Leiter-Sprosse in die Stufe, die sie (oder ihre Kette) in der Zuordnung trägt."""
    D.sb_verst = SB.ids(sb['teil1'].get('Verständnis-Bank', ''))
    D.sb_leiter = OrderedDict((st.name, []) for st in stufen)
    for sp in SB.ids(sb['teil1'].get('Leiter-Bank', '')):
        D.sb_leiter[sb_stufe_fuer(sp, stufen)].append(sp)


def sb_nimm(D, B, sp, stufe):
    """Eine Bankaufgabe zur Sprosse (oder genau die Variante, wenn die id sie nennt); Prozent-Grundwert
    1 %-Weg wie bisher die erste kopfrechenbare in Euro (Prozent-Tabelle)."""
    if re.search(r'-v\d+$', sp):
        r = D.bank.get(sp)
        if not r or sp in B.benutzt:
            D.befund(f'Steckbrief: Bankaufgabe {sp} fehlt oder ruht – nicht gesetzt')
            return None
        a = bank_aufgabe(D, r, stufe); kennzahlen(D, a); B.benutzt.add(a.id)
        return a
    if sp not in B.sprossen:
        D.befund(f'Steckbrief: Bank-Sprosse {sp} fehlt – nicht gesetzt')
        return None
    if sp.endswith('prozentrechnung-e4-k2-s3'):
        rs = [r for r in B.sprossen[sp] if r['id'] not in B.benutzt]
        aufg = [bank_aufgabe(D, r, stufe) for r in rs]
        for a in aufg:
            kennzahlen(D, a)
        a = next((x for x in aufg if x.zk == 0 and '€' in x.text), aufg[0] if aufg else None)
        if a:
            B.benutzt.add(a.id)
        return a
    vorstufe = B.sprossen[sp][0].get('hoehe') == 'vorstufe'
    w = B.nimm(sp, 1, stufe, kopf_zuerst=not vorstufe)   # Vorstufe: erste Variante (Steckbrief-Beispiel 20 %)
    return w[0] if w else None


def sb_merke(D, a, sp):
    """Leiter-/Verständnis-Sprosse merken: Vorstufen und Grundfälle kommen in späteren Stufen nicht wieder."""
    h = (D.bank.get(a.id) or {}).get('hoehe', '')
    B = D.bau
    B.sb_sp.add(sprosse_von(a.id))
    if h == 'vorstufe':
        B.vor_sp.add(sprosse_von(a.id))
    if h == 'grundfall':
        B.grund_k.add(kette_von(a.id))


def sb_leiter(D, B, st, darstellung_tab):
    out = []
    for sp in D.sb_leiter.get(st.name, []):
        a = sb_nimm(D, B, sp, st.name)
        if not a:
            continue
        a.fest = len(out) + 1
        a.hrang = HRANG.get((D.bank.get(a.id) or {}).get('hoehe'), 2)
        if darstellung_tab and sprosse_von(a.id).endswith('prozentrechnung-e4-k2-s3'):
            prozent_tabelle(a)   # Prozent-Tabelle als Verfahren, ohne Streifen daneben (Steckbrief Darstellung)
        sb_merke(D, a, sp)
        out.append(a)
    return out


def sb_schaetzfrage(D, sb, stufe):
    """Schätzfrage des Steckbriefs als Ankreuzaufgabe – nur, wenn sie Zahlen und Vorschläge („Was kann passen:
    A · B · C“) hat und eine Lösung im Steckbrief steht (Schätzfrage-Lösung); sonst keine (Befund)."""
    q = SB.zitate(sb['teil1'].get('Schätzfrage', ''))
    lo = SB.schuelertext(sb['teil1'].get('Schätzfrage-Lösung', ''))
    if not q or not lo or not re.search(r'\d', q[0]) or 'passen:' not in q[0]:
        D.befund('Steckbrief: Schätzfrage ohne Zahlen, Vorschläge oder Lösung – keine Schätzaufgabe gesetzt')
        return None
    vor, opts = q[0].split('passen:', 1)
    a = Aufgabe()
    a.art, a.id = 'bank', 'steckbrief-' + sb['name'] + '-schaetzfrage'
    a.text = tx(vor.strip() + ' passen? Kreuze an, rechne nicht.')
    a.optionen = [tx(o.strip(' ?')) for o in opts.split('·') if o.strip(' ?')]
    a.kreuz, a.form = True, 'ankreuzen'
    a.kurz_roh = [lo]
    a.kurz = tx(lo)
    a.loesung_roh = lo
    kennzahlen(D, a)
    a.hrang = 0
    return a


def sb_verstaendnis(D, B, sb, st):
    """Erste Sprosse (N6.27): Verständnis-Bank des Steckbriefs (Erste Frage), dann die Schätzfrage."""
    out = []
    for sp in D.sb_verst:
        a = sb_nimm(D, B, sp, st.name)
        if a:
            a.hrang = 0
            sb_merke(D, a, sp)
            out.append(a)
    a = sb_schaetzfrage(D, sb, st.name)
    if a:
        out.append(a)
    for i, a in enumerate(out):
        a.fest = i + 1
    return out


def sb_merkkasten(sb):
    """Merkkasten: Begriff und Merkregel (zitierte Sätze im Feld Formel), Schülertext ohne Belege."""
    teile = []
    b = SB.schuelertext(sb['teil1'].get('Begriff', ''))
    if b:
        teile.append(tx(b))
    for z in SB.zitate(sb['teil1'].get('Formel', '')):
        teile.append(tx('Merkregel: ' + z + '.'))
    if not teile:
        return ''
    return ('\\par\\addvspace{4pt}{\\small\\uebersichtskasten{\\textbf{Merke:} ' + ' '.join(teile) + '}}\\par')


def sb_fehler_tex(sb):
    """Typische Fehler (Lösungsdatei, oben): Schülertext ohne Belege."""
    fs = sb['teil1'].get('Typische Fehler') or []
    if isinstance(fs, str):
        fs = [fs]
    fs = [SB.schuelertext(f) for f in fs if SB.schuelertext(f)]
    if not fs:
        return ''
    return ('{\\small\\noindent\\textbf{Typische Fehler}\\par\\smallskip\\noindent '
            + '\\par\\noindent '.join('\\textbullet\\ ' + tx(f) for f in fs) + '\\par}\\medskip')


SB_STOPP = {'Prozent', 'Tabelle', 'Kopf', 'Aufgabe', 'Rechnen', 'Ankreuzen', 'Kreuze', 'Berechne', 'Ergänze'}


def sb_nomen(t):
    return {w.lower() for w in re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]{4,}', t or '') if w not in SB_STOPP}


def sb_vorher(D, sb, rb):
    """N6.29.8: Rückblick nur zu Voraussetzungen des Steckbriefs („Vorher können“): eine Zeile der
    Rückblick-Datei bleibt, wenn ein Hauptwort ihrer Voraussetzung in einer Voraussetzung des Steckbriefs
    steckt (Teilwort genügt: „Winkel“ in „Rechtwinkelmarke“; Entscheidung). Voraussetzungen ohne Zeile:
    Befund."""
    vk = SB.schuelertext(sb['teil1'].get('Vorher können', ''))
    teile = [x.strip() for x in re.split(r';', vk) if x.strip()]
    if not teile:
        return rb
    raus, gedeckt = [], set()
    for a in rb:
        nv = sb_nomen(getattr(a, 'voraus', ''))
        hit = [i for i, t in enumerate(teile) if any(w in t.lower() for w in nv)]
        if hit:
            gedeckt.update(hit)
        else:
            raus.append(a)
            D.befund(f'Rückblick: „{getattr(a, "voraus", "")}“ ist keine Voraussetzung im Steckbrief – weggelassen')
    for i, t in enumerate(teile):
        if i not in gedeckt:
            D.befund(f'Rückblick: Voraussetzung „{t}“ (Steckbrief) hat keine Rückblick-Zeile')
    return [a for a in rb if all(a is not x for x in raus)]


def sb_raster_rang(D, a):
    """Vorzug eigener Aufgaben in Sprüngen (Steckbrief Teil 2/3): 0 = passt (Sache aus dem Raster oder die
    Darstellung der Raster-Lücke oder eine Frage wie in Teil 3), 1 = sonst. Ohne Steckbrief: 0."""
    sb = getattr(D, 'sb', None)
    if not sb or a.art != 'bank':
        return 0
    rs = sb_nomen(sb['teil2'].get('Sachen', ''))
    if rs & {w.lower() for w in sache(a)}:
        return 0
    lk = sb.get('luecke', '').lower()
    if lk and darstellung(a) in lk:
        return 0
    frage = klartext(a.text).split('. ')[-1][:18].lower()
    if any(f[:18].lower() == frage for f, _ in sb['kurz'] + sb['lang'] if f):
        return 0
    return 1


def zum_schluss(D, args, stufen, B, alle_namen):
    """N6.26 Behalten: „Zum Schluss“ (Fokus) zwei ältere Aufgaben – je eine echte BB/BE-Aufgabe der zwei
    Stufen, die im Kapitel vor der ersten Stufe des Blatts stehen (Zuordnung), die leichteste (Kopf oder
    glatt), nicht schon auf dem Blatt. Steht keine Stufe davor: keine (Befund)."""
    import functools
    namen = [st.name for st in stufen]
    erste = min(alle_namen.index(n) for n in namen if n in alle_namen)
    vorher = [z for z in D.zu[:erste] if z['stufe'] not in namen][-2:][::-1]
    if not vorher:
        D.befund('Zum Schluss: keine Stufe vor dem Fokus im Kapitel – keine ältere Aufgabe')
        return []
    auf_blatt = {x.id for st in stufen for _, _, gl in st.gruppen for x in gl} | \
        {g.id for st in stufen for _, _, gl in st.gruppen for x in gl for g in getattr(x, 'glieder', [])}
    out = []
    for z in vorher:
        ks = []
        for i in z['katalog_ids'].split():
            if i in auf_blatt or i in B.benutzt:
                continue
            a = echt_aufgabe(D, i, z['stufe'])
            if a and not a.abb:
                a.hrang = 3; a.stern = stern_fuer(D, i); kennzahlen(D, a)
                if a.zk <= 1:
                    ks.append(a)
        if ks:
            a = min(ks, key=functools.cmp_to_key(vergleich))
            B.benutzt.add(a.id)
            out.append(a)
    if len(out) < 2:
        D.befund(f'Zum Schluss: nur {len(out)} ältere Aufgabe(n) ohne Abbildung, Kopf oder glatt')
    return out


def baue_modell(D, args):
    B = Bau(D, args)
    stufen = [Stufe(z) for z in D.zu]
    stufen = [s for s in stufen if s.kern] + [s for s in stufen if not s.kern]   # Kern zuerst
    if args.fokus:
        # Steckbrief (mathe-nachhilfe/katalog/steckbrief/, Lauf 06.10. abends): nennt er Stufen, gelten sie;
        # sonst wie bisher die Stufen, deren Name das Fokuswort enthält
        sb = SB.finde(D.mn, D.kapitel, fokus=args.fokus)
        if not sb:
            sb = SB.finde(D.mn, D.kapitel, stufen=[s.name for s in stufen if args.fokus.lower() in s.name.lower()] or ['-'])
        if sb and sb['stufen']:
            stufen = [s for s in stufen if s.name in sb['stufen']]
        else:
            stufen = [s for s in stufen if args.fokus.lower() in s.name.lower()]
        if not stufen:
            sys.exit(f'Fokus „{args.fokus}“ trifft keine Stufe')
        D.sb = sb if sb and stufen else None
        if D.sb:
            stufen = sb_stufenfolge(D, D.sb, stufen)
    ps = None if (args.fokus or not D.pr['pruefstein']) else pruefstein_waehlen(D)
    ps_ids = set(ps[3]) if ps else set()
    tief = args.art == 'schwach' or bool(args.fokus)     # Leiter von ganz unten (Beschlüsse 1, 7, 29)
    alle_namen = [z['stufe'] for z in D.zu]
    kap_ids = {i for z in D.zu for i in z['katalog_ids'].split()} | set(D.wort_eigen)
    sb = getattr(D, 'sb', None)
    D.bau = B
    B.sb_sp = set()
    if sb:
        sb_zuteilen(D, sb, stufen)
    for st in stufen:
        st.verst = sb_verstaendnis(D, B, sb, st) if sb and st is stufen[0] else []
        st.merke = sb_merkkasten(sb) if sb and st is stufen[0] else ''
        st.sb_leiter = sb_leiter(D, B, st, D.kapitel == 'prozent') if sb else []
        st.kd, st.selten = jahre_info(D, st)
        # echte Aufgaben (oben auf der Leiter); Hauptplatz aus handgriffe-p10.csv (N2.5/N2.6)
        ids, steckt, heraus_ids = platz_ids(D, st, alle_namen, kap_ids, bool(args.fokus))
        echte = []
        for i in ids:
            if i in ps_ids:
                continue
            a = echt_aufgabe(D, i, st.name)
            if a:
                a.hrang = 3
                a.stern = stern_fuer(D, i)
                kennzahlen(D, a)
                echte.append(a)
        st.steckt = [i for i in steckt if i not in ps_ids]
        # Fokus (N2.5): Zwischenschritt-Aufgaben herausgelöst; fehlt die herausgelöste Fassung, ganz (Befund)
        for i in heraus_ids:
            rs = [r for r in D.heraus if (r.get('eltern_id') or '').strip() == i and stufe_trifft(r.get('stufe'), st.name)]
            if rs:
                for r in rs:
                    a = daten_aufgabe(D, r, st.name, 'heraus'); kennzahlen(D, a)
                    if UNSICHER.search(r.get('bemerkung') or ''):
                        D.n_unsicher = getattr(D, 'n_unsicher', 0) + 1
                    a.schritte = str(rechenschritte(r.get('loesung') or '', schrittzahl(a)))
                    if a.zahlart:
                        a.zk = zahlart_wert(a.zahlart, a)
                    B.benutzt.add(a.id); D.n_heraus += 1
                    echte.append(a)
            elif i not in ps_ids:
                a = echt_aufgabe(D, i, st.name)
                if a:
                    D.befund(f'Fokus {st.name}: {i} enthält den Handgriff als Zwischenschritt, herausgelöste '
                             f'Fassung fehlt in herausgeloest-p10.csv – ganz gesetzt')
                    a.hrang = 3; a.stern = stern_fuer(D, i); kennzahlen(D, a)
                    echte.append(a)
        # N5.20 (Auffüllen B): alle herausgelösten der P10-Originale gehören aufs Blatt; fremde und eigene nur
        # in Sprünge der Leiter (unten, spruenge_fuellen); die Zielzahl 12/6 gilt nicht mehr fürs Blatt
        heraus_p10, sprung_pool = blatt_kandidaten(D, st, echte, steckt, B)
        echte += heraus_p10
        st.mass = schwerste_echt(echte)
        # Ketten und Einheiten der Stufe
        ketten, einheiten = [], set()
        for sp in st.sprossen:
            if re.match(r'(msa|abitur)/', sp):
                continue
            k = kette_von(sp)
            if k not in ketten:
                ketten.append(k)
            m = re.match(r'([a-z-]+?)-e(\d+)-', sp)
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
        if sb:
            vsp = []   # Steckbrief: die Vorstufen stehen in seiner Leiter (Leiter-Bank), keine weiteren
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
        if len(vor) < 2 and not sb:
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
                if sp in B.sb_sp:
                    continue   # steht schon in der Steckbrief-Leiter
                if h == 'grundfall' and k not in B.grund_k:
                    mitte += B.nimm(sp, n_grund, st.name)   # Grundfall einer Kette nur in ihrer ersten Stufe
                    B.grund_k.add(k)
                elif args.fokus and h == 'sprosse' and sp not in st.sprossen:
                    mitte += B.nimm(sp, 1, st.name)   # Fokus: ganze Kette von unten (Beschluss 7)
        if args.fokus:
            for sp in (FOKUS_DAZU.get(st.name, []) if not D.handgriffe else []):
                for a in B.nimm(sp, 1, st.name, kopf_zuerst=False):   # v1: „nach Rabatt (80 %)“
                    a.gruppe = 'Sachaufgabe'
                    mitte.append(a)
            for iid in (FOKUS_ECHT.get(st.name, []) if not D.handgriffe else []):
                if any(x.id == iid for x in echte):
                    continue
                a = echt_aufgabe(D, iid, st.name)
                if a:
                    a.hrang = 3; a.stern = stern_fuer(D, iid); kennzahlen(D, a)
                    echte.append(a)
            # nur Aufgaben, die nach der Größe der Stufe fragen (Reparatur Punkt 3)
            pass   # Filter nach gesuchter Größe gilt jetzt für alle Fassungen (unten)
        for sp in st.sprossen:
            m = re.match(r'((?:msa|abitur)/[\w-]+\.jsonl)\((\d+)\)', sp)
            if m:
                rs = [r for r in D.zusatz.get(m.group(1), []) if r['id'] not in B.benutzt]
                # eigene Aufgaben in Prüfungshöhe nur, wenn echte fehlen (Beschlüsse 21, 22)
                if len(echte) < 2:
                    for r in rs[:max(1, 2 - len(echte))]:
                        a = bank_aufgabe(D, r, st.name); kennzahlen(D, a); B.benutzt.add(a.id)
                        a.zusatz = True   # Prüfungshöhe aus der Bank: bleibt (N5.20 gilt nur für Füller)
                        mitte.append(a)
                continue
            if sp not in B.sprossen:
                D.befund(f'{st.name}: Bank-Sprosse {sp} ohne Aufgaben')
                continue
            h = B.sprossen[sp][0]['hoehe']
            if h == 'pruefung' and len(echte) >= 2:
                continue
            if sp in B.sb_sp:
                continue
            if h in ('grundfall', 'vorstufe'):
                continue
            mitte += B.nimm(sp, n_spr, st.name)
        if st.name in ('Grundwert', 'Prozentwert', 'Prozentsatz'):
            # Korrektur Lauf C Punkt 2: in den Stufen G, W, p nur Aufgaben, die nach dieser Größe fragen
            # (eigene Aufgaben; echte ordnet die Zuordnung zu – Abweichung nur als Befund)
            weg = [a for a in mitte if gesucht(a) not in ('', st.name)]
            for a in weg:
                D.befund(f'Stufe {st.name}: {a.id} fragt nach {gesucht(a)} – nicht gesetzt')
                D.herausgefallen = getattr(D, 'herausgefallen', []) + [(st.name, a.id, gesucht(a), klartext(a.text)[:60])]
            mitte = [a for a in mitte if a not in weg]
            for a in echte:
                if gesucht(a) not in ('', st.name):
                    D.befund(f'Stufe {st.name}: echte {a.id} fragt laut Text nach {gesucht(a)} (bleibt, Zuordnung)')
        for a in mitte:
            a.stern = bool(a.orig and stern_fuer(D, a.orig))
        # Grundwert-Leiter (N2.11): 1 %-Schritt in der Prozent-Tabelle mit Streifen, dann 10/25/50 % als
        # Abkürzung; dann Formel (ab der ersten Aufgabe, die sie braucht), dann die übrigen
        if sb:
            # Steckbrief: Leiter-Bank in Katalog-Folge (N6.30: glatte Sätze vor dem 1 %-Weg)
            st.leiter = st.sb_leiter
            mitte = [a for a in mitte if all(sprosse_von(a.id) != sprosse_von(l.id) for l in st.leiter)]
        elif D.kapitel == 'prozent' and st.name == 'Grundwert':
            st.leiter = grundwert_leiter(D, B, st.name)
            mitte = [a for a in mitte if all(sprosse_von(a.id) != sprosse_von(l.id) for l in st.leiter)]
            if st.leiter:
                # Die Leiter beginnt mit dem 1 %-Schritt (N2.11); die Vorstufen (Streifen abtragen, Größe
                # ankreuzen) gehen in Tabelle mit Streifen und in der Erkennen-Aufgabe auf (Entscheidung)
                D.vor_weg = getattr(D, 'vor_weg', 0) + len(st.vor)
                st.vor = []
        # Eigene sparsam (N1.3): gleicht eine eigene einer echten/fremden/herausgelösten oder einer früheren
        # eigenen in Sache, Darstellung und Fragerichtung, fällt sie weg (Vorstufen untereinander ebenso)
        rest = eigene_sparsam(D, echte + st.verst + st.leiter + mitte)
        mitte = [a for a in mitte if any(a is x for x in rest)]
        st.vor = eigene_sparsam(D, st.vor)
        # N5.20: fremde und eigene nur, wo zwischen zwei aufeinanderfolgenden Aufgaben der Leiter ein Sprung
        # ist (je Sprung höchstens eine); ohne BB/BE-Aufgabe in der Stufe bleibt die Mitte wie bisher
        if any(bbbe(a) for a in echte):
            fest_m = [a for a in mitte if getattr(a, 'zusatz', False)]
            pool = sprung_pool + [(2, a) for a in mitte if not getattr(a, 'zusatz', False)]
            wahl = spruenge_fuellen(D, st, echte + fest_m, st.vor + st.leiter, pool)
            for a in mitte:
                if not any(a is w for w in wahl) and not getattr(a, 'zusatz', False):
                    B.benutzt.discard(a.id)
                    D.n_eigen_kein_sprung = getattr(D, 'n_eigen_kein_sprung', 0) + 1
            mitte = fest_m + [a for a in wahl if a.art == 'bank']
            for a in wahl:
                if a.art != 'bank':
                    B.benutzt.add(a.id)
                    if a.art == 'fremd':
                        D.n_fremd += 1
                    else:
                        D.n_heraus += 1
                    echte.append(a)
        # Gruppen (Beschluss 8): je Gruppe leicht -> schwer; Aufgabenbild-Wort aus Feld bild
        alle = mitte + echte
        # Oben steht die schwerste BB/BE-Aufgabe, ganz oder herausgelöst (Sichtprüfung Fokus 06.10.: sonst steht
        # „Quark 93 %“ vor dem einschrittigen glatten T-Shirt und die Leiter fällt am Ende ab)
        st.gruppen = buendeln(D, ordne_stufe(alle, [a for a in echte if bbbe(a)] or echte))
        if st.leiter:
            st.gruppen.insert(0, (LEITER, '', st.leiter))
        if st.verst:
            st.gruppen.insert(0, (VERSTAENDNIS, 'erst verstehen – nicht rechnen', st.verst))
        # Erkennen (N5.23, ändert N4.19): im Fokusblatt keine Erkennen-Aufgabe; im ganzen Heft eine kurze
        # Stufe nach allen Geschwistern (erkennen_stufen)
        if not echte:
            D.befund(f'{st.name}: keine echte Aufgabe – Prüfungshöhe nur aus der Bank')
        st.reserve = []
        for k in ketten:
            for sp in self_sprossen(B, k):
                st.reserve += [r for r in B.sprossen[sp] if r['id'] not in B.benutzt
                               and r['hoehe'] in ('grundfall', 'sprosse')]
        for l in st.luecken:
            D.befund('Lücke: ' + l)
    if not args.fokus:
        stufen = erkennen_stufen(D, stufen)
    D.ohne_bild = sum(1 for r in D.bank.values() if not r.get('bild'))
    return stufen, ps, B


def erkennen_stufen(D, stufen):
    """N4.19 im ganzen Heft: je Familie verwechselbarer Stufen (Zuordnung, Spalte verwechselbar) eine kurze
    Stufe „Was ist gesucht?“ nach der letzten Geschwister-Stufe. Ohne Spalte oder ohne Daten: keine."""
    namen = [s.name for s in stufen]
    fam = []
    for st in stufen:
        if not st.verwechselbar:
            continue
        f = {st.name} | {n for n in namen if any(stufe_trifft(v, n) for v in st.verwechselbar)}
        if len(f) >= 2 and f not in fam:
            fam.append(f)
    for f in fam:
        letzte = max(i for i, s in enumerate(stufen) if s.name in f)
        reihe = [n for n in namen if n in f]
        a = erkennen_aufgabe(D, reihe, ' / '.join(reihe))
        if not a:
            continue
        neu = Stufe({'stufe': 'Was ist gesucht?', 'kern': 'nein', 'katalog_ids': '', 'bank_sprossen': ''})
        neu.kd, neu.selten = '', False
        neu.gruppen = [(ERKENNEN, '', [a])]
        neu.ziel = 'serkennen' + str(len(fam))
        stufen = stufen[:letzte + 1] + [neu] + stufen[letzte + 1:]
        namen = [s.name for s in stufen]
    return stufen


LEITER = 'Leiter'     # feste Leiterplätze am Anfang der Stufe (Grundwert N2.11), nicht sortiert
ERKENNEN = 'Erkennen' # Erkennen-Aufgabe (N4.19)


def grundwert_leiter(D, B, stufe):
    """Grundwert-Leiter ohne Steckbrief (N2.11, geändert durch Punkt 30 in 06b): (1) glatte Sätze – erste Variante
    des Grundfalls „mal 2, 4, 5, 10“ (prozentrechnung-e4-k2-s1) mit Satz in {10, 20, 25, 50}; (2) 1 %-Weg – erste
    kopfrechenbare Variante in Euro von prozentrechnung-e4-k2-s3 als Prozent-Tabelle % | Größe (p → 1 → 100),
    ohne Streifen daneben (Satz 06.10. abends). Mit Steckbrief gilt dessen Leiter-Bank. Fehlt eine Sprosse:
    Befund."""
    out = []
    # Punkt 30 (06b, ändert N2.11): Katalog-Folge – glatte Sätze (Grundfall „mal 2, 4, 5, 10“) vor dem 1 %-Weg
    for sp, wahl in (('prozentrechnung-e4-k2-s1', lambda a: {int(v) for v, p, _ in zahlen(a.text) if p} <= {10, 20, 25, 50}),
                     ('prozentrechnung-e4-k2-s3', lambda a: a.zk == 0 and '€' in a.text)):
        rs = [r for r in B.sprossen.get(sp, []) if r['id'] not in B.benutzt]
        aufg = [bank_aufgabe(D, r, stufe) for r in rs]
        for a in aufg:
            kennzahlen(D, a)
        a = next((x for x in aufg if wahl(x)), aufg[0] if aufg else None)
        if not a:
            D.befund(f'Grundwert-Leiter: Sprosse {sp} fehlt in der Bank')
            continue
        B.benutzt.add(a.id)
        a.fest = len(out) + 1
        a.hrang = 1
        if sp.endswith('-s3'):
            prozent_tabelle(a)
        out.append(a)
    return out


def prozent_tabelle(a):
    """1 %-Schritt als Prozent-Tabelle (N2.11/N2.12): „p % einer Menge sind w E“ -> Tabelle % | E mit
    p → 1 → 100, Pfeilen :p und ·100, Streifen daneben."""
    m = re.search(r'\$?(\d+)\\?,?\\%\$?\s+(?:einer|eines|der|des)\s+\w+\s+sind\s+\$?([\d{},]+)\$?\s*(\\,)?\s*\$?(\S*?)\$?[.\s]', a.text)
    if not m:
        return
    p, w, e = m.group(1), m.group(2), m.group(4).strip('$.').replace('\\,', '')
    e_tx = e if e else ''
    a.abb = pfeiltabelle(['Prozent', e_tx or 'Wert'], [['$' + p + r'\,\%$', '$' + w + r'$\,' + e_tx],
                                                         [r'$1\,\%$', r'\leerzelle'], [r'$100\,\%$', r'\leerzelle']])
    # B5 (07.10.): der Text nennt den Weg nicht; Frage nach dem Ganzen bleibt
    a.text = a.text[:m.end()].rstrip() + ' Wie viel ist das Ganze?'
    a.form = 'tabelle'
    a.antwort = ''


def pfeiltabelle(kopf, zeilen):
    """Tabelle mit Pfeilen auf beiden Seiten, ohne Beschriftung, genau zwischen den Zeilen (B5, 07.10.): die
    Tabelle steht in einem TikZ-Knoten; je Zeilenpaar links und rechts ein Bogen von Zeilenmitte zu Zeilenmitte."""
    n = len(zeilen)
    z = r' \\ \hline '.join(' & '.join(x) for x in zeilen)
    tab = (r'\renewcommand{\arraystretch}{1.35}\begin{tabular}{|r|r|}\hline '
           r'\textbf{%s} & \textbf{%s} \\ \hline %s \\ \hline\end{tabular}' % (kopf[0], kopf[1], z))
    bs = []
    for i in range(1, n):
        f1, f2 = (i + 0.5) / (n + 1), (i + 1.5) / (n + 1)
        for a, b, w in (('north west', 'south west', 180), ('north east', 'south east', 0)):
            bs.append(r'\draw[->,mbgrau,line width=0.5pt] ($(T.%s)!%.4f!(T.%s)$) to[out=%d,in=%d,looseness=1.8] '
                      r'($(T.%s)!%.4f!(T.%s)$);' % (a, f1, b, w, w, a, f2, b))
    return (r'\begin{tikzpicture}[baseline=(T.north)]\node[inner sep=0,outer sep=1.5pt] (T) {' + tab + '};'
            + ''.join(bs) + r'\end{tikzpicture}')


GESUCHT_KAT = [(r'^(zinseszins|endkapital)', 'Zinseszins'), (r'^(zinsen|z\b)', 'Zinsen $Z$'),
               (r'^(vermehrt|vermindert|neuer wert|wert nach|w \(vermehrt)', 'neuer Wert'),
               (r'^(prozentwert|w\b)', 'Prozentwert $W$'), (r'^(grundwert|g\b)', 'Grundwert $G$'),
               (r'^(prozentsatz|zinssatz|p\b)', 'Prozentsatz $p$')]


def gesucht_kat(g):
    """Gesuchte Größe eines Erkennen-Satzes -> Spalte (Entscheidung: wenige Spalten, die Wörter der Stufen;
    sonst der Text bis zur Klammer, höchstens 25 Zeichen)."""
    t = norm(g)
    for rx, k in GESUCHT_KAT:
        if re.search(rx, t):
            return k
    t = re.split(r'\s*[(,;]', (g or '').strip())[0]
    return t if 2 <= len(t) <= 25 else ''


def erkennen_aufgabe(D, namen, stufe, n_max=6):
    """Erkennen (N4.19, vorläufig): 4–6 kurze Sätze aus echten Aufgaben (erkennen-p10.csv bzw.
    fremd/*-erkennen.csv) der Stufe und ihrer Geschwister, je Satz ankreuzen, was gesucht ist. Spalten = die
    gesuchten Größen (höchstens vier). Ohne Geschwister oder mit weniger als vier Sätzen bzw. zwei Größen
    keine (Befund). Sätze reihum aus den Stufen und Größen; kurze Sätze zuerst (bis 110 Zeichen)."""
    if not D.erkennen or len(namen) < 2:
        return None
    je, gesehen = OrderedDict(), set()
    for r in D.erkennen:
        satz = (r.get('satz') or '').strip()
        k = gesucht_kat(r.get('gesucht'))
        if not satz or not k or len(satz) > 110 or norm(satz) in gesehen:
            continue
        gesehen.add(norm(satz))
        for n in namen:
            if stufe_trifft(r.get('stufe'), n):
                je.setdefault(k, []).append(r)
                break
    for k in je:
        je[k].sort(key=lambda r: (0 if 'P10' in (r.get('quelle') or '') else 1, len(r['satz'])))
    kats = sorted(je, key=lambda k: -len(je[k]))[:4]
    wahl = []
    while len(wahl) < n_max and any(je[k] for k in kats):
        for k in kats:
            if je[k] and len(wahl) < n_max:
                r = je[k].pop(0)
                r['_kat'] = k
                wahl.append(r)
    if len(wahl) < 4 or len(kats) < 2:
        D.befund(f'Erkennen {stufe}: nur {len(wahl)} Sätze bzw. {len(kats)} gesuchte Größen – keine Aufgabe')
        return None
    reih = [k for k in kats if any(r['_kat'] == k for r in wahl)]
    a = Aufgabe()
    a.art, a.id = 'erkennen', 'erkennen-' + re.sub(r'[^a-z]', '', stufe.lower())[:20]
    a.text = 'Was ist gesucht? Kreuze an. Rechne nicht.'
    # Spalten der Größen je 1,9 cm mit Umbruch im Kopf; Satzspalte füllt die Textbreite (≈ 15,4 cm)
    kopf = ' & '.join('{\\scriptsize\\hspace{0pt}' + tx(k) + '}' for k in reih)   # \\hspace{0pt}: Trennung im Kopf
    zeilen = ' '.join(f'{tx(r["satz"])} & ' + ' & '.join('$\\square$' for _ in reih) + r' \\ \hline' for r in wahl)
    a.abb = (r'\begingroup\renewcommand{\arraystretch}{1.4}\begin{tabular}{|>{\raggedright\arraybackslash}p{%.1fcm}|%s}\hline  & %s \\ \hline %s\end{tabular}\endgroup'
             % (12.3 - 2.0 * len(reih), '>{\\centering\\arraybackslash\\hyphenpenalty=0}p{1.55cm}|' * len(reih), kopf, zeilen))
    a.kreuz = True
    def kurzwort(k):   # „Prozentsatz $p$“ -> „$p$“; sonst das Wort
        m = re.search(r'\$[^$]+\$', k)
        return m.group(0) if m else k
    a.kurz = ', '.join(f'{i + 1}~{tx(kurzwort(r["_kat"]))}' for i, r in enumerate(wahl))
    a.kurz_roh = [klartext(a.kurz)]
    a.schritte = '1'
    a.zk, a.tl, a.fz, a.sr, a.gruppe = 0, 0, 1, 8, 'Ankreuzen'
    a.erk_quellen = [r.get('quelle', '') for r in wahl]
    a.hrang = 2
    D.n_erkennen = getattr(D, 'n_erkennen', 0) + 1
    return a


SCHLUSS = 'Schluss'   # letzte Gruppe einer Stufe: schwerere eigene, dann die schwerste echte (Regel d)


def ordne_stufe(alle, echte):
    """Korrektur Lauf C: nach den Vorstufen alle Aufgaben nach vergleich() (Schritte bei großem Abstand,
    Zahlklasse, Prozentsatz-Rang, Schwierigkeit; Herkunft zählt nicht). Gruppen nach Form = Folgen
    gleicher Form in dieser Reihenfolge innerhalb einer Zahlklasse (keine Gruppe zieht eine schwerere
    Aufgabe vor eine leichtere). Die Stufe endet mit der schwersten echten Aufgabe, schwerere eigene
    stehen direkt davor."""
    import functools
    alle = sorted(alle, key=functools.cmp_to_key(vergleich))
    schluss = []
    if echte:
        top = max(echte, key=functools.cmp_to_key(vergleich))
        top.ist_top = True   # die Prüfung (sortierung_md) nimmt dieselbe, auch wenn Bündel Aufgaben herausnehmen
        schluss = [x for x in alle if x is not top and not bbbe(x) and x.art != 'echt' and vergleich(x, top) > 0] + [top]
        alle = [x for x in alle if all(x is not y for y in schluss)]
        if D_AKT is not None and (D_AKT.handgriffe or D_AKT.fremd):
            # Nachtrag N1.3/E22: oben auf der Leiter steht Echtes – eigene, die schwerer sind als die schwerste
            # echte Aufgabe, füllen keine Lücke und fallen weg; fremde und herausgelöste bleiben davor
            weg = [x for x in schluss if x.art == 'bank' and not x.fest]
            D_AKT.n_eigen_oben = getattr(D_AKT, 'n_eigen_oben', 0) + len(weg)
            schluss = [x for x in schluss if all(x is not y for y in weg)]
    gruppen = []
    for x in alle:
        if gruppen and gruppen[-1][0] == x.gruppe and gruppen[-1][2][-1].zk == x.zk:
            gruppen[-1][2].append(x)
        else:
            gruppen.append((x.gruppe, x.bild or '', [x]))
    if schluss:
        gruppen.append((SCHLUSS, '', schluss))
    return gruppen


class Buendel:
    """Bündel (N2.8): gleichartige BB/BE-Originale nach der ersten ihrer Art, im Rahmen, zweispaltig."""
    art = 'buendel'

    def __init__(self, kopf, glieder):
        self.kopf, self.glieder = kopf, glieder
        self.id = 'buendel-' + kopf.id
        self.zk = kopf.zk


def art_schluessel(D, a):
    """Gleiche Art (N2.8): gleiche Schrittzahl, Zahlart, Fragerichtung, Darstellung; dazu (Entscheidung) gleicher
    Katalogtyp, damit nur Sache und Zahlen verschieden sind."""
    typ = D.kat.get(a.id, {}).get('typ', '')
    return (schrittzahl(a), a.zk, richtung(a), darstellung(a), typ)


def buendeln(D, gruppen):
    """N2.8: in der geordneten Stufe folgen gleichartige BB/BE-Originale der ersten Aufgabe ihrer Art in einem
    Bündel. Die Schluss-Aufgabe (schwerste echte) bleibt allein am Ende; Aufgaben mit Abbildung bleiben
    einzeln (Entscheidung: zweispaltig passen Grafiken nicht)."""
    if not D.pr.get('buendel', True):
        return gruppen
    reihe = [x for g in gruppen if g[0] not in (LEITER, ERKENNEN, VERSTAENDNIS) for x in g[2]]
    schluss = gruppen[-1][2][-1] if gruppen and gruppen[-1][0] == SCHLUSS else None
    klassen = OrderedDict()
    for a in reihe:
        if a.art != 'echt' or a is schluss:
            continue   # Abbildung erlaubt, seit das Bündel einspaltig eingerückt steht (Lauf 06.10. abends)
        klassen.setdefault(art_schluessel(D, a), []).append(a)
    for k, al in klassen.items():
        if len(al) < 2:
            continue
        kopf, rest = al[0], al[1:]
        for g in gruppen:
            g[2][:] = [x for x in g[2] if all(x is not r for r in rest)]
        for g in gruppen:
            for i, x in enumerate(g[2]):
                if x is kopf:
                    g[2].insert(i + 1, Buendel(kopf, rest))
                    break
        for r in rest:
            r.im_buendel = True
        D.n_buendel += 1
    return [g for g in gruppen if g[2]]


def rueckblick_daten(D, args, stufen, alle):
    """Rückblick aus rueckblick-p10.csv (N2.10): je Stufe des Blatts die Zeilen der Datei; jede Aufgabe kommt
    in der Leiter wieder vor – gebraucht_ab (Freitext mit Katalog-ids, „Leiter …“, „erste Sprossen …“) wird
    auf die erste Aufgabe des Blatts aufgelöst, die er nennt; ohne Treffer fällt die Rückblick-Aufgabe weg
    (Befund). Dieselbe Aufgabe (gleicher Text) nur einmal. form „Tabelle A | B | C“: Eintragtabelle, Zeilen
    aus der Lösung („1 % = 1/100 = 0,01; …“: erste Spalte gegeben, die übrigen leer)."""
    namen = [st.name for st in stufen]
    out, da = [], set()
    for r in D.rueck:
        if not any(stufe_trifft(r.get('stufe'), n) for n in namen):
            continue
        t = (r.get('aufgabe') or '').strip()
        if norm(t) in da:
            continue
        ziel = ziel_von(r.get('gebraucht_ab', ''), stufen, alle)
        if ziel is None:
            D.befund(f'Rückblick: „{t[:40]}“ – gebraucht ab „{(r.get("gebraucht_ab") or "")[:60]}“ '
                     f'kommt im Blatt nicht vor – weggelassen')
            continue
        da.add(norm(t))
        a = Aufgabe()
        a.art, a.id = 'zone', 'rueckblick-' + str(len(out) + 1)
        a.voraus = (r.get('voraussetzung') or '').strip()
        form = (r.get('form') or '').strip()
        lo = (r.get('loesung') or '').strip()
        a.text = tx(t)
        mt = re.match(r'Tabelle\s+(.+)$', form)
        if mt:
            kopf = [k.strip() for k in mt.group(1).split('|')]
            zeilen = []
            for teil in [x.strip() for x in lo.split(';') if x.strip()]:
                w = [x.strip() for x in re.split(r'\s*(?:=|→|≈)\s*', teil)]
                zeilen.append([w[0]] + ['leer'] * (len(kopf) - 1))
            if zeilen:
                a.abb = linientabelle(kopf, zeilen)
                a.text = tx(re.sub(r'\s+für\s+.*$', '.', t)) if len(zeilen) >= 3 else a.text
                a.form = 'tabelle'
        a.kurz_roh = [lo]
        a.kurz = tx(lo)
        a.zw_roh, a.zw = [], []
        kennzahlen(D, a)
        a.hrang = 0
        a.gebraucht = [ziel]
        out.append(a)
    return out


def linientabelle(kopf, zeilen):
    """Tabelle mit Linien (N2.12): Kopf fett, jede Zeile mit Linie, „leer“ = Eintragfeld."""
    z = lambda x: r'\rule{0pt}{3ex}\hspace{1.6cm}' if x == 'leer' else tx(x)
    return (r'\begingroup\renewcommand{\arraystretch}{1.3}\begin{tabular}{|%s}\hline %s \\ \hline %s\end{tabular}\endgroup'
            % ('c|' * len(kopf), ' & '.join(r'\textbf{' + tx(k) + '}' for k in kopf),
               ' '.join(' & '.join(z(x) for x in r) + r' \\ \hline' for r in zeilen)))


def ziel_von(g, stufen, alle):
    """gebraucht_ab (Freitext) -> erste Aufgabe des Blatts, die er nennt, oder None. Gesucht werden
    Katalog-ids (2017-OS-B1b), Bank-Sprossen, „Leiter“/„erste Sprossen“ (feste Leiter bzw. erste Aufgabe
    der Stufe nach den Vorstufen) und Stufennamen."""
    g = (g or '').strip()
    if not g:
        return None
    treffer = []
    for i in re.findall(r'\d{4}-[A-Z]+-[A-Z]\d+[a-z]?|[a-z-]+-e\d+-k\d+-s\d+(?:-v\d+)?', g):
        for a in alle:
            if a.id == i or a.id.startswith(i) and re.fullmatch(r'[a-z]?', a.id[len(i):]) \
                    or (a.art == 'bank' and sprosse_von(a.id) == i) or getattr(a, 'orig', '') == i:
                treffer.append(a)
                break
    if re.search(r'Leiter|erste Sprosse|1 %-Schritt|Abkürzung', g):
        for st in stufen:
            if st.leiter:
                if re.search(r'1 %-Schritt|Anfang', g):
                    # Steckbrief-Leiter beginnt mit der Streifen-Vorstufe: der 1 %-Schritt ist die Prozent-Tabelle
                    treffer.append(next((x for x in st.leiter if x.form == 'tabelle'), st.leiter[0]))
                else:
                    # „Abkürzung 10/25/50 %“: mit Steckbrief der Grundfall (glatte Sätze), sonst das Ende
                    treffer.append(next((x for x in st.leiter if x.hrang == 1), st.leiter[-1]))
                break
            erste = [x for _, _, gl in st.gruppen for x in gl if not isinstance(x, Buendel)]
            if erste:
                treffer.append(erste[0])
                break
    if treffer:
        # die früheste genannte Aufgabe des Blatts (Reihenfolge von alle = Satzfolge)
        return min(treffer, key=lambda a: next((k for k, x in enumerate(alle) if x is a), 10 ** 6))
    for st in stufen:
        if stufe_trifft(g, st.name):
            erste = st.vor + [x for _, _, gl in st.gruppen for x in gl if not isinstance(x, Buendel)]
            if erste:
                return erste[0]
    return None


def rueckblick(D, args, stufen, B):
    """Rückblick (Nachtrag N2.10, ersetzt Beschluss 18): mit rueckblick-p10.csv aus der Datei, sonst höchstens
    zwei Aufgaben aus Sprossen der Leiter. Gilt für ganzes Heft, Fokus und jede Portion (Entscheidung: auch
    spätere Portionen blicken nur auf das zurück, was ihre Leiter gleich braucht)."""
    alle = [x for st in stufen for x in st.vor + [y for _, _, gl in st.gruppen for y in gl]
            if not isinstance(x, Buendel)]
    alle += [g for st in stufen for _, _, gl in st.gruppen for b in gl if isinstance(b, Buendel) for g in b.glieder]
    if D.rueck:
        rb = rueckblick_daten(D, args, stufen, alle)
        if rb and D.sb:
            rb = sb_vorher(D, D.sb, rb)   # N6.29.8: Voraussetzungen aus dem Steckbrief
            for i, a in enumerate(rb):
                a.id = 'rueckblick-' + str(i + 1)
            return rb
        if rb:
            return rb
    return rueckblick_ohne_datei(D, args, stufen, B)


def rueckblick_ohne_datei(D, args, stufen, B):
    """Ohne rueckblick-p10.csv (N2.10, Auftrag R): höchstens zwei Aufgaben, nur aus Sprossen, die in der
    Leiter vorkommen – je eine noch freie Variante der ersten zwei Grundfall-Sprossen des Blatts (aus
    verschiedenen Stufen, kopfrechenbar zuerst); gebraucht ab = die Leiteraufgabe derselben Sprosse
    (Entscheidung)."""
    out, st_da = [], set()
    for st in stufen:
        if len(out) >= 2:
            break
        for a in st.vor + [x for _, _, gl in st.gruppen for x in gl if not isinstance(x, Buendel)]:
            if a.art != 'bank' or st.name in st_da:
                continue
            sp = sprosse_von(a.id)
            h = B.sprossen.get(sp, [{}])[0].get('hoehe')
            if h != 'grundfall':
                continue
            frei = [r for r in B.sprossen.get(sp, []) if r['id'] not in B.benutzt]
            kand = [zone_aufgabe(D, r) for r in frei]
            for k in kand:
                kennzahlen(D, k)
            kand.sort(key=lambda k: (k.zk, k.tl, k.id))
            if not kand:
                continue
            r = kand[0]
            r.hrang, r.gebraucht = 0, [a]
            B.benutzt.add(r.id)
            out.append(r)
            st_da.add(st.name)
            break
    return out


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
    # Aufgabe des eigenen Kapitels: mindestens die Hälfte ihrer Teile steht in der eigenen Wortlautdatei
    # (Lauf C Nachbesserung; Teile aus anderen Dateien ergänzen sie, machen sie aber nicht zur eigenen)
    gruppen = OrderedDict((pre, ids) for pre, ids in gruppen.items()
                          if 2 * sum(1 for i in ids if i in D.wort_eigen) >= len(ids)
                          and any(i in D.wort_eigen for i in ids))
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


D_AKT = None   # Daten des laufenden Baus (für marke)


def marke(a, kurs):
    if a.art == 'echt' and D_AKT is not None and D_AKT.pr['ordner'] == 'abitur' and a.hilfsmittel == 'nein':
        # Rechner-Hinweis nur, wo der Katalog es verlangt (hilfsmittelfreier Teil; Lauf B2)
        return f'{D_AKT.pr["marke"]} ’{str(a.jahr)[2:]}\\\\ohne Hilfsmittel'
    """Grau links (Beschluss 14, Nachtrag N1.2/N3.15/N4.17): nur das Jahr – „P10 ’26“ an echten, die Marke
    der Daten an fremden („BY ’23“), „nach P10 ’15“ an herausgelösten und an Bankzeilen, die ein Original
    nennen („(P10 2015)“ im Text); eigene Aufgaben ohne Marke („eigene Aufgabe“ entfällt)."""
    if a.art == 'echt':
        return f'{D_AKT.pr["marke"]} ’{str(a.jahr)[2:]}'
    if a.marke_text:
        return tx(a.marke_text)
    return ''


def nummer(a, nr):
    return (r'\llap{\textasteriskcentered\,}' if getattr(a, 'stern', False) else '') + str(nr) + '.'


def punkte_von(D, a):
    """N5.21: auf dem Blatt Punkte nur beim Prüfstein (setze_pruefstein); in den Daten bleiben sie."""
    return ''
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
    if k and len(klartext(k)) <= 45:
        return k
    return ausweichwert(a) or kurzurteil(a)


def _wert_roh(t):
    """Wert eines Ergebnisteils (Klartext): hinter dem letzten = bzw. ≈, mit Einheit; ein kurzer
    exakter Wert (√, π, Bruch) vor dem ≈ bleibt davor. Ohne Relation: der Teil selbst."""
    # Klammerzusätze mit Wörtern weg („(Arabisch)“), Klammern in Formeln und Punkten bleiben
    t = re.sub(r'\s*\((?=[^()]*[A-Za-zÄÖÜäöüß]{3})(?:[^()]|\([^()]*\))*\)', '', t).strip()
    t = re.sub(r'(?<![A-Z][a-z])\.$', '', t) if not re.search(r'(Mio|Mrd|Tsd|ca)\.$', t) else t
    t = re.split(r'\s*(?:⇒|, also|, denn|→)\s*', t)[-1] if re.search(r'\d', re.split(r'\s*(?:⇒|, also|, denn|→)\s*', t)[-1]) else t
    pos = [m for m in re.finditer(r'≈|(?<![<>≤≥!])=', t)]
    if not pos:
        return t
    if re.match(r'^\s*[a-zA-Z](\(x\))?\s*=', t) and len(pos) == 1 and not re.search(r'\d\s*$', t[:pos[0].start()]):
        return t   # Gleichung „y = (x − 2)² − 4“ ist selbst der Wert
    last = pos[-1]
    if not re.search(r'\d', t[last.end():]) and len(pos) >= 2:   # „… ≈ 93,0 cm = AF“: Wert davor
        t = t[:last.start()].strip()
        pos = pos[:-1]
        last = pos[-1]
    wert = t[last.end():].strip()
    if last.group(0) == '≈':
        ex = t[pos[-2].end():last.start()].strip() if len(pos) >= 2 else ''
        if ex and len(ex) <= 12 and re.search(r'√|π|/', ex):
            return ex + ' ≈ ' + wert
        return '≈ ' + wert
    return wert


def ausweichwert(a):
    """Kontrollwert, wenn die Kurzlösung zu lang ist (Reparatur Punkt 2): je gefragtem Wert (Teile der
    Kurzlösung) der Wert nach dem letzten = bzw. ≈; alle Werte, solange zusammen bis 60 Zeichen, sonst
    der letzte allein (bis 45). Teile ohne Zahl nur, wenn sie kurz sind (Urteil wie „Aussage 2 falsch“)."""
    roh = getattr(a, 'kurz_roh', None)
    if not roh:
        return ''
    werte = []
    for x in roh:
        for y in [z for z in re.split(r';\s*', x) if z.strip()]:
            w = _wert_roh(y)
            if not w or (not re.search(r'\d', w) and len(w) > 25) or len(w) > 40 \
                    or not re.search(r'[\dA-Za-zÄÖÜäöü]', w) or re.match(r'^\s*[²³^]', w):
                continue
            if w not in werte:
                werte.append(w)
    if not werte:
        return ''
    fx = abi_tx if D_AKT is not None and D_AKT.pr['ordner'] == 'abitur' else tx
    alle = '; '.join(werte)
    if len(alle) <= 60:
        return fx(alle)
    mit_zahl = [w for w in werte if re.search(r'\d', w)]
    return fx(mit_zahl[-1]) if mit_zahl and len(mit_zahl[-1]) <= 45 else ''


def kurzurteil(a):
    """Letzter Ausweg für den Fuß (Reparatur Punkt 2): das erste Stück der Kurzlösung bis zum ersten
    Komma bzw. „⇒“, wenn es kurz ist (bis 45 Zeichen) – Urteil oder Kernaussage („genau ein gemeinsamer
    Punkt S(2|-2)“, „nein“)."""
    roh = getattr(a, 'kurz_roh', None) or []
    if not roh:
        return ''
    t = re.sub(r'^z\. ?B\.\s*', '', roh[0])
    teile = re.split(r'(,\s|\s⇒\s|\s\(|:\s)', t)
    t = teile[0].strip()
    rest = ''.join(teile[1:])
    if re.match(r',\s\d', rest) or (' ' not in t and not re.fullmatch(r'(ja|nein|wahr|falsch|richtig)', t, re.I)):
        return ''   # Aufzählung abgeschnitten („Streifen mit 1 cm, …“) oder ein einzelnes Wort ohne Urteil
    if 3 <= len(t) <= 45:
        fx = abi_tx if D_AKT is not None and D_AKT.pr['ordner'] == 'abitur' else tx
        return fx(t)
    return ''


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


def rechenaufgabe(a):
    """Muss gerechnet werden (Sichtprüfung Kurvenuntersuchung Nr. 12: Nullstellen von x² − 6x + 5 ohne
    Rechenplatz, weil die Bank kein Zwischenergebnis nennt)? Ja bei Nullstellen, Ableitung, Gleichung,
    Extrem-/Wende-/Schnittpunkt, Term mit Potenz, und wenn die Lösung mehrere Werte (x₁, x₂) hat."""
    t = klartext(a.text)
    if re.search(r'Nullstelle|Ableitung|Gleichung|lös|Extrem|Hochpunkt|Tiefpunkt|Wendepunkt|Schnittpunkt|'
                 r'Scheitel|Berechne|Bestimme|Ermittle|Rechne|Schreibe die Umkehrung|Schreibe an', t):
        return True
    if re.search(r'\^|²|³', t) or re.search(r'x_?\{?[12]', a.kurz or ''):
        return True
    return False


def platz(a, art):
    """Rechenplatz nach Schrittzahl (Beschluss 11): Ankreuzen und Ein-Wort-Antwort (kopfrechenbar,
    ohne Zwischenergebnis, kurze Antwort) ohne Platz; sonst Schritte = Katalogfeld schritte bzw.
    Zwischenergebnisse + 1; schwach eine Zeile je Schritt, mindestens zwei (H 29)."""
    if a.kreuz or (a.optionen and not a.zw):
        return 0
    if a.art != 'echt' and a.form in ('streifenleer',):
        return 0
    if a.art in ('echt', 'fremd', 'heraus'):
        s = int(re.sub(r'\D', '', a.schritte) or 1)
    else:
        s = len(a.zw) + 1
    if re.search(r'\b(Prüfe|Überprüfe|Entscheide|Begründe|Zeige|Weise)\b', klartext(a.text)) and not a.optionen:
        s = max(s, 1)   # Prüf- und Entscheidungsaufgaben brauchen eine Antwortzeile (Reparatur Punkt 9)
    elif not a.zw and a.art != 'echt' and len(klartext(a.kurz)) <= 25 and not rechenaufgabe(a):
        return 0   # Ein-Wort-, Ein-Zahl- und Rundungsaufgaben ohne Platz (Beschluss 11)
    if art == 'schwach':
        return max(1, min(5, schrittzahl(a)))   # eine Rasterzeile je Schritt (Beschluss 29)
    return max(1, min(4, s))


def zf_fuer(a, zaehler, art):
    """Zerlegung mit Ausblenden (H 29) nur bei echten Mehrschritt-Aufgaben (Beschluss 5): erste
    Aufgabe der Stufe mit Zwischenfragen bekommt alle, die zweite die erste, dann keine."""
    if art != 'schwach' or not a.zf or a.art != 'echt' or int(re.sub(r'\D', '', a.schritte) or 1) < 2:
        return []
    k = zaehler[0]
    zaehler[0] += 1
    return a.zf if k == 0 else (a.zf[:1] if k == 1 else [])


def aufgabe_tex(D, a, nr, art, zfs, kurs, mit_nr=True, mit_fuss=True):
    """Aufgabe in pfaufg (mathblatt 2026-10-06c): Marke im linken Rand auf der Grundlinie der Nummer
    (N3.15). Aufgaben mit Tabelle oder Antwortfeld bekommen keinen Rechenplatz darunter (N2.12)."""
    out = [f'\\begin{{{UMG}}}{{{marke(a, kurs)}}}{{{nummer(a, nr) if mit_nr else ""}}}{{{punkte_von(D, a)}}}',
           a.text, optionen_tex(a)]
    if a.abb:
        out.append('\\par\\smallskip\\noindent ' + a.abb + '\\par')
    if getattr(a, 'antwort', ''):
        out.append('\\par\\noindent ' + a.antwort + '\\par')
    for f in zfs:
        out.append(f'\\pfzwfrage{{{tx(f)}}}')
    n = platz(a, art)
    if n and UMG == 'pfaufg' and (getattr(a, 'antwort', '') or re.search(r'tabular|sachtabelle|wertetabelle|dreisatz|leerzelle|leerfeld', (a.abb or '') + a.text)):
        n = 0   # Tabelle oder Antwortfeld: keine Zusatzlinien (N2.12)
        D_AKT.n_ohne_linien = getattr(D_AKT, 'n_ohne_linien', 0) + 1
    if n:
        out.append(f'\\rechenraster{{{n}}}' if art == 'schwach' else f'\\rechenplatz{{{n}}}')
    if mit_fuss:
        out.append(fuss(a, nr))
    out.append(f'\\end{{{UMG}}}')
    return '\n'.join(x for x in out if x)


UMG = 'pfaufg'   # Aufgabenumgebung (mathblatt 2026-10-06c); Abitur-Profil ebenso


def buendel_tex(D, b, nrn, kurs):
    """Bündel (N2.8, Satz Lauf 06.10. abends): gleichartige BB/BE-Originale eingerückt statt gerahmt; einmal je
    Gruppe der graue Hinweis „gleiche Art · n× geprüft – kannst du überspringen“, je Aufgabe Marke im Rand,
    Nummer, Text und eine Antwortlinie; Fuß wie sonst. n = Zahl der Originale dieser Art (Kopf und Glieder).
    Entscheidung: einspaltig (eingerückt ist die Spalte schmaler; zweispaltig würde der Text umbrechen)."""
    n = 1 + len(b.glieder)
    out = ['\\par\\addvspace{4pt}\\Needspace*{0.3\\textheight}\\begin{list}{}{\\setlength{\\leftmargin}{8mm}\\setlength{\\topsep}{0pt}}\\item[]',
           f'\\noindent{{\\footnotesize\\color{{mbgrau}}gleiche Art \\textperiodcentered{{}} {n}$\\times$ geprüft – '
           f'kannst du überspringen}}\\par']
    for a, nr in zip(b.glieder, nrn):
        t = a.text + (optionen_tex(a) if a.optionen else '')
        if a.abb:
            t += '\\par\\smallskip\\noindent ' + a.abb + '\\par'
        linie = '' if a.optionen else '\\par\\vspace{7mm}\\noindent{\\color{black!45}\\rule{\\linewidth}{0.4pt}}'
        out.append(f'\\begin{{{UMG}}}{{{marke(a, kurs)}}}{{{nummer(a, nr)}}}{{{punkte_von(D, a)}}}\n{t}{linie}\n'
                   + fuss(a, nr) + f'\n\\end{{{UMG}}}')
    out.append('\\end{list}')
    return '\n'.join(out)


def braucht_formel(st, a):
    """Formel ab der ersten Aufgabe, die rechnet und nicht mehr im Kopf geht; in den Zins-Stufen ab der
    ersten Rechnung (Zinssatz und Kapital brauchen die umgestellte Formel; Reparatur Punkt 4)."""
    if st.name not in FORMEL or a.hrang == 0 or a.kreuz or a.optionen or a.form.startswith('streifen') \
            or (a.hrang == 1 and not any(re.search(r'\\cdot|·|: ?0', z) for z in a.zw_roh)):
        return False
    return gesucht(a) in ('', st.name) or st.name.startswith('Zinsen')   # zweite Reparatur Punkt 2


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
                    # Abitur (Lauf B3): Vorstufen sind Erkennungsaufgaben – klein und grau benannt
                    out.append('\\pfgruppe{Was ist zu tun? Ankreuzen, nicht rechnen}'
                               if D.pr['ordner'] == 'abitur' and all(x.kreuz or x.optionen for x in inh)
                               else '\\pfgruppe{}')
                aufg, g = inh, 'Vorstufe'
            else:
                g, wort, aufg = inh
                if st.merke and g != VERSTAENDNIS and not getattr(st, 'merke_da', False):
                    out.append(st.merke)   # Merkkasten (Steckbrief) nach der Verständnis-Sprosse
                    st.merke_da = True
                if g == ERKENNEN and st.name == 'Was ist gesucht?':
                    # eigene kurze Stufe (N4.19): Kopf nie allein unten auf der Seite
                    out[-1] = '\\par\\Needspace*{0.55\\textheight}' + out[-1]
                else:
                    out.append(f'\\pfgruppe{{{tx(wort)}}}')
            for a in aufg:
                if isinstance(a, Buendel):
                    nrn = list(range(nr + 1, nr + 1 + len(a.glieder)))
                    out.append(buendel_tex(D, a, nrn, args.kurs))
                    for x, n in zip(a.glieder, nrn):
                        loes.append((f'{n}.', x))
                        SORT.append((st.name, n, 'Bündel', x))
                        NR_VON[x.id] = n
                    nr = nrn[-1]
                    continue
                if braucht_formel(st, a) and st.name not in formel_da and g != LEITER:
                    out.append(f'\\pfab{{{FORMEL[st.name]}}}')
                    formel_da.add(st.name)
                nr += 1
                out.append(aufgabe_tex(D, a, nr, args.art, zf_fuer(a, zaehler, args.art), args.kurs))
                loes.append((f'{nr}.', a))
                SORT.append((st.name, nr, g, a))
                NR_VON[a.id] = nr
            if i == len(bl) - 1 and st.steckt:
                STECKT[st.ziel] = st
                out.append(f'%%STECKT {st.ziel}%%')   # „steckt auch in Nr. n“ nach dem Setzen aller Nummern (N2.6)
    return '\n'.join(out), nr, loes


NR_VON = {}    # id -> Nummer im Heft (für „steckt auch in“ und Rückblick)
STECKT = {}    # Ziel der Stufe -> Stufe


def steckt_text(D, st, kurs):
    """„steckt auch in Nr. 47 (P10 ’24)“ (N2.6) für die Zwischenschritt-Aufgaben der Stufe, die im Heft eine
    Nummer haben; mehrere durch Semikolon."""
    teile = []
    for i in st.steckt:
        n = NR_VON.get(i)
        if n and i in D.kat:
            teile.append(f'Nr. {n} ({D.pr["marke"]} ’{D.kat[i]["jahr"][2:]})')
    if not teile:
        return ''
    D.n_steckt = getattr(D, 'n_steckt', 0) + len(teile)
    return '\\pfsteckt{steckt auch in ' + '; '.join(teile) + '}' 


def setze_rueckblick(D, args, rb, nr):
    out = ['\\pfrueckblick']
    loes = []
    for a in rb:
        nr += 1
        out.append(aufgabe_tex(D, a, nr, args.art, [], args.kurs))
        loes.append((f'{nr}.', a))
        RUECK.append((nr, a))
    return '\n'.join(out), nr, loes


RUECK = []   # (Nr., Aufgabe) des Rückblicks: Prüfstein N2.10 – zu jeder die Nummer, ab der sie gebraucht wird


def setze_pruefstein(D, args, ps):
    """Prüfstein ohne laufende Nummer (Beschluss 20), mit Seitenfuß (Nachtrag N2.13): Kontrollwert je
    Teilaufgabe wie sonst; kein Zwischenfragen-Gerüst; Teilaufgaben a), b) … mit Punkten."""
    jahr, n, pre, ids = ps
    vs = D.wort.get(pre)
    fund = fundstelle(D, ids[0], args.kurs, ganz=True)
    out = [f'\\pfpruefstein{{P10 ’{str(jahr)[2:]}}}']
    vs_abb = ''
    if vs:
        vs_abb = abbildung(vs['abbildung'], D, pre)
        t = [f'\\begin{{{UMG}}}{{}}{{}}{{}}', tx(vs['wortlaut'])]
        if vs_abb:
            t.append('\\par\\smallskip\\noindent ' + vs_abb + '\\par')
        t.append(f'\\end{{{UMG}}}')
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
        t = [f'\\begin{{{UMG}}}{{}}{{{(chr(0x2a) if a.stern else "")}{w["teil"]})}}{{{a.punkte} BE}}', tx(txt),
             optionen_tex(a)]
        if a.abb and a.abb != vs_abb:
            t.append('\\par\\smallskip\\noindent ' + a.abb + '\\par')
        if not a.kreuz and not re.search(r'tabular|sachtabelle|leerzelle', a.abb or ''):
            t.append('\\rechenplatz{3}')
        kennzahlen(D, a)
        t.append(fuss(a, f'Prüfstein {w["teil"]})'))   # Prüfstein mit Fuß (N2.13)
        t.append(f'\\end{{{UMG}}}')
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
    if '\\' in t or '{' in t or '^' in t or '_' in t:
        t = re.sub(r'(?<!\\)%', r'\\%', t)
        if not re.search(r'\\(cdot|t?frac|pi|approx|text|sqrt|Rightarrow)|\^', t):
            if re.search(r'\\(mathrm|bar|pm|times|alpha|beta|gamma|delta|varepsilon|neq|le|ge|angle|circ)(?![A-Za-z])|_', t):
                # weitere Mathebefehle der neuen Kapitel (\mathrm, \bar, \pm, \times, x_1; Lauf C):
                # Wörter bleiben Text, der Rest Mathe
                return _mathe_stuecke(t)
            return t   # Bank-LaTeX ohne Mathebefehl (30\,\%, 0{,}25) geht im Text
        m = re.match(r'^(.*?)(\s+[A-Za-zÄÖÜäöüß][A-Za-zÄÖÜäöüß. ]*)$', t)
        rumpf = m.group(1) if m else t
        if re.search(r'(?<![\\A-Za-z])[A-Za-zÄÖÜäöüß]*[äöüÄÖÜß][A-Za-zÄÖÜäöüß]*|(?<![\\A-Za-z{])[A-Za-z]{4,}', rumpf):
            return _mathe_stuecke(t)   # Wörter mitten in der Rechnung (Lauf C) bleiben Text
        if m:
            return tx('$' + m.group(1) + '$') + tx(m.group(2))   # Einheit/Wort hinter der Zahl aufrecht
        return tx('$' + t + '$')
    return tx(t)


def _mathe_stuecke(t):
    """Teil mit Mathebefehlen außer \\cdot/\\frac (Lauf C): Wörter (drei Buchstaben und mehr,
    außerhalb von Befehlen) bleiben Text, alles zwischen ihnen wird Mathe."""
    toks = re.split(r'(\s+)', t)
    out, cur = [], []
    def wort(x):
        return (re.fullmatch(r'[A-Za-zÄÖÜäöüß.,:;()\-]*[A-Za-zÄÖÜäöüß]{3,}[A-Za-zÄÖÜäöüß.,:;()\-]*', x) is not None
                or re.fullmatch(r'[a-zäöüß]{2}', x) is not None) and '\\' not in x
    for x in toks:
        if x.strip() and wort(x):
            if ''.join(cur).strip():
                out.append('$' + ''.join(cur).strip() + '$ ')
            cur = []
            out.append(x + ' ')
        elif x.strip():
            cur.append(x + ' ')
    if ''.join(cur).strip():
        out.append('$' + ''.join(cur).strip() + '$')
    r = ''.join(out).strip().replace('$:', ':$').replace('$$', '')
    teile = re.split(r'((?<!\\)\$[^$]*(?<!\\)\$)', r)
    for i, x in enumerate(teile):
        if x.startswith('$'):
            for k, v in UNI_MATH.items():
                if k in x and k not in '·°':
                    x = x.replace(k, ' ' + v + ' ')
            teile[i] = x
    return ''.join(teile)


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
    if not wort and not re.search(r'(?<![\\A-Za-z])[a-z](?![A-Za-z])', ansatz.replace('cm', '').replace(' m ', ' ')):
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


def mathe_sicher(t):
    """Befehle, die nur im Mathemodus gehen, stehen außerhalb von $…$ (Lauf C, neue Kapitel):
    diese Stücke in $…$ setzen. Ohne solche Stücke unverändert (Prozent byte-gleich)."""
    teile = re.split(r'((?<!\\)\$[^$]*(?<!\\)\$)', t)
    neu = []
    for x in teile:
        if x.startswith('$') or not re.search(r'\\(mathrm|bar|pm|times|mid|sqrt|cdot|t?frac|alpha|beta|gamma|delta|varepsilon|pi|approx|neq|le|ge|angle|circ|Rightarrow)(?![A-Za-z])|[_^]', x):
            neu.append(x)
        else:
            neu.append(_mathe_stuecke(x) if x.strip() else x)
    return ''.join(neu)


def _ohne_leer(s):
    return re.sub(r'[\s{}$]|\\[,;!]', '', klartext(s))


def rechts_knapp(kurz, zws):
    """Rechte Spalte (N3.16): nur, was nicht schon links steht und zum Ergebnis führt. Weg fällt ein
    Zwischenergebnis, (1) das ganz links steht, (2) dessen linke Seite (vor dem ersten =) links schon mit
    Wert steht („f(2) = 2³ − 4·2² + 6“, wenn links „f(2) = −2“), (3) das nur den Endwert wiederholt."""
    kl = _ohne_leer(kurz)
    out = []
    for z in zws:
        zk = _ohne_leer(z)
        if not zk:
            continue
        if zk in kl:
            continue
        lhs = re.split(r'=|≈|approx', klartext(z), maxsplit=1)[0]
        lhs_k = _ohne_leer(lhs)
        if '=' in klartext(z) and lhs_k and re.search(r'[a-zA-Z]\(', lhs_k) and (lhs_k + '=') in kl:
            continue
        # „W = G · p = 70 € · 0,3 = 21 €“ mit 21 € links: der Schluss „= 21 €“ steht schon links
        teile = re.split(r'=', klartext(z))
        if len(teile) >= 3 and _ohne_leer(teile[-1]) and _ohne_leer(teile[-1]) == kl:
            i = z.rfind('=')
            z2 = z[:i].rstrip()
            if z2.count('$') % 2:
                z2 += '$'
            z = z2
        out.append(z)
    return out


URTEIL = re.compile(r'^\s*((?:[IVX]+|Aussage\s*\d+|\w)?\s*\b(?:ja|nein|richtig|falsch|wahr|stimmt nicht|stimmt|'
                    r'trifft zu|trifft nicht zu))\b\s*[;,:–]\s*(.+)$', re.I)


def urteil_kern(kurz_roh):
    """Begründen (N3.16): links nur das Urteil, rechts der Kern. „I falsch; Tiefpunkt … ⇒ …“ ->
    („I falsch“, „Tiefpunkt … ⇒ …“); sonst (kurz, '')."""
    t = ' | '.join(kurz_roh)
    m = URTEIL.match(t)
    if not m or len(m.group(1)) > 20:
        return None
    return m.group(1).strip(), m.group(2).strip()


PUNKTWORT = {'Hochpunkt': 'H', 'Tiefpunkt': 'T', 'Wendepunkt': 'W', 'Sattelpunkt': 'S'}


def bezeichnungen(s, frage=''):
    """Bezeichnungen in Lösungen (N4.18), Klartext: Punkte mit Buchstaben („Hochpunkt (1 | e)“ -> „H(1 | e)“,
    „Tiefpunkte (−2 | −4,5), (2 | −4,5)“ -> „T₁(…), T₂(…)“; Achsenschnitt (a | 0) -> N, (0 | b) -> S_y, wenn die
    Frage nach Achsen/Nullstellen fragt); Stellen als x-Werte („x = 0, x = 2, x = 6“ -> „x₁ = 0, x₂ = 2,
    x₃ = 6“); Bedeutungsindex nur bei zwei Arten von Stellen (x_E1 -> x₁, sonst bleibt). Ohne Treffer
    unverändert."""
    if not s:
        return s
    t = s
    P = r'\(\s*[^()|]+?\s*\|\s*[^()|]+?\s*\)'
    for wort, b in PUNKTWORT.items():
        def ein(m, b=b):
            pts = re.findall(P, m.group(2))
            if len(pts) == 1:
                return b + pts[0]
            return ', '.join(f'{b}{"₁₂₃₄"[i]}{p}' for i, p in enumerate(pts[:4]))
        t = re.sub(r'\b(' + wort + r'e?)\s*(' + P + r'(?:\s*(?:,|und)\s*' + P + r')*)', ein, t)
    if re.search(r'Achse|Nullstelle|schneidet', frage or '') and re.search(r'(?<![A-Za-z₀-₉_])' + P, t):
        def achse(m):
            x, y = [v.strip() for v in m.group(0)[1:-1].split('|')]
            if re.fullmatch(r'0', y) and not re.fullmatch(r'0', x):
                return 'N' + m.group(0)
            if re.fullmatch(r'0', x) and not re.fullmatch(r'0', y):
                return 'Sᵧ' + m.group(0)
            return m.group(0)
        t = re.sub(r'(?<![A-Za-z₀-₉ᵧ_)])(?<!≈ )' + P, achse, t)
        ns = re.findall(r'N\(', t)
        if len(ns) >= 2:
            k = iter('₁₂₃₄₅')
            t = re.sub(r'N\(', lambda m: 'N' + next(k, '') + '(', t)
    # Stellen als x-Werte, mehrere nummeriert
    xs = re.findall(r'(?<![\w_])x\s*=\s*(?!\s*[a-z(])', t)
    if len(xs) >= 2 and not re.search(r'x[₁₂₃_]', t):
        k = iter('₁₂₃₄₅₆')
        t = re.sub(r'(?<![\w_])x(\s*=)(?!\s*[a-z(])', lambda m: 'x' + next(k, '') + m.group(1), t)
    # Bedeutungsindex nur bei zwei Arten
    arten = set(re.findall(r'x_\{?([NEWHT])\d*\}?', t))
    if len(arten) == 1:
        t = re.sub(r'x_\{?[NEWHT](\d)\}?', lambda m: 'x' + '₀₁₂₃₄₅₆₇₈₉'[int(m.group(1))], t)
        t = re.sub(r'x_\{?[NEWHT]\}?', 'x', t)
    return t


def loesung_zeilen(D, a, art, kurs):
    """Lösungszeile (N3.16, N4.18): links das Ergebnis in der Form der Frage, rechts nur, was nicht links steht
    und zum Ergebnis führt; Begründen: links Urteil, rechts Kern. Keine Fundstelle (N4.17)."""
    fx = abi_tx if D.pr['ordner'] == 'abitur' else tx
    frage = klartext(a.text)
    kurz = a.kurz
    roh = getattr(a, 'kurz_roh', None)
    kern = ''
    if a.art in ('echt', 'fremd', 'heraus') and roh:
        uk = urteil_kern(roh)
        if uk:
            kurz, kern = fx(bezeichnungen(uk[0], frage)), fx(bezeichnungen(uk[1], frage))
        else:
            kurz = '; '.join(fx(bezeichnungen(x, frage)) for x in roh)
    if art == 'schwach':
        zws = [mathe_sicher(schwach_zeile(z, a)) for z in (a.zw_roh or a.zw)]
    elif a.art in ('echt', 'fremd', 'heraus') and a.zw_roh:
        zws = [fx(bezeichnungen(z, frage)) for z in a.zw_roh]
    else:
        zws = list(a.zw)
    zws = rechts_knapp(kurz, zws)
    if kern:
        zws = [kern] + zws
    return kurz, '; '.join(zws), ''


def setze_loesung(D, args, titel, eintraege, ps_loes, zweispaltig=False):
    """Lösungsdatei ohne Punkte (Beschluss 25), ohne Fundstellenzeile (Nachtrag N3.16, N4.17); Kopf nur
    der Name (N3.14), unten nur die Seitenzahl. zweispaltig: zwei Spalten (multicol) – nur, wenn dadurch
    eine Seite wegfällt (main probiert beides)."""
    out = [KOPF.replace('\\begin{document}', '').replace('\\usepackage{mathblatt}', '\\usepackage{mathblatt}\n\\usepackage{multicol}'),
           '\\begin{document}', '\\pfheftstil', f'\\pfheftkopf{{{titel} \\textperiodcentered{{}} Lösungen}}{{}}']
    if getattr(D, 'sb', None):
        out.append(sb_fehler_tex(D.sb))   # typische Fehler aus dem Steckbrief, über den Lösungen
    if zweispaltig:
        out.append('\\begin{multicols}{2}\\raggedcolumns')
    abi = D.pr['ordner'] == 'abitur'
    kopf_auf, kopf_da, nr_von = {}, set(), {}
    if abi:
        # Kopf der Aufgabe (Lösungsblatt 05.10. Punkt 4; Lauf B2): Ableitungen und Stammfunktion
        # (f′, f″, F …), einmal je Aufgabe untereinander, wo mindestens zwei ihrer Teilaufgaben im Heft
        # stehen; die Teilaufgaben verweisen darauf statt zu wiederholen
        gr = OrderedDict()
        for nr, a in eintraege:
            if a.art == 'echt':
                gr.setdefault(a.id[:-1], []).append(a)
                nr_von[a.id] = nr
        for auf, al in gr.items():
            defs = []
            for a in al:
                for z in a.zw_roh:
                    # nur Definitionen „f′(x) = Term“ der Funktion der Aufgabe, kein „= 0 ⇒ …“, keine Zahl
                    m = re.match(r"^\s*([a-z])('+|[′″]+)\(([a-z])\)\s*=\s*(.+)$", z)
                    if m and not re.search(r'⇒|⇔|=', m.group(4)) and re.search(m.group(3), m.group(4)) \
                            and z not in defs:
                        defs.append(z)
            if len(al) >= 2 and defs:
                kopf_auf[auf] = defs
    for nr, a in eintraege:
        k, z, f = loesung_zeilen(D, a, args.art, args.kurs)
        if abi and a.art == 'echt':
            auf = a.id[:-1]
            zr = [x for x in a.zw_roh if x not in kopf_auf.get(auf, [])]
            mit = [d[-1] + ')' for d in a.abhaengig.split('|') if d and d[:-1] == auf]
            frage = klartext(a.text)
            zf = rechts_knapp(k, [abi_formel(bezeichnungen(x, frage)) for x in zr])
            uk = urteil_kern(getattr(a, 'kurz_roh', []) or [])
            kern = [z.split('; ')[0]] if uk and z else []
            z = '; '.join((['mit ' + ', '.join(mit)] if mit else []) + kern + zf)
        elif abi:
            zs = [abi_zw(x, a.kurz) for x in (a.zw_roh or [])]
            zs = [x for x in zs if x]
            gesamt, z2 = 0, []
            for x in zs:   # kurz, eine Zeile: höchstens zwei Handgriffe, zusammen bis 70 Zeichen
                if len(z2) >= 2 or gesamt + len(klartext(x)) > 70:
                    break
                z2.append(x if '$' in x or '\\' not in x else '$' + x + '$')
                gesamt += len(klartext(x))
            z = '; '.join(rechts_knapp(k, [tx(x, latex=True) for x in z2]))
        # keine Fundstellenzeile (N3.16); die vierte Spalte (früher BE) bleibt leer (Beschluss 25)
        kopf = ''
        if abi and a.art == 'echt' and a.id[:-1] in kopf_auf and a.id[:-1] not in kopf_da:
            kopf_da.add(a.id[:-1])
            kopf = '\\par\\noindent'.join(
                r'{\small ' + abi_formel(d) + '}' for d in kopf_auf[a.id[:-1]])   # untereinander
        elif abi and a.art == 'echt' and a.id[:-1] in kopf_auf:
            z = f'Kopf bei Nr. {nr_von[min((x for x in nr_von if x[:-1] == a.id[:-1]), key=lambda x: int(nr_von[x][:-1]))].rstrip(".")}' \
                + ('; ' + z if z else '')
        out.append(f'\\begin{{pfloesung}}{{{kopf}}}')
        out.append(f'\\lz{{{nr}}}{{{k}}}{{{z}}}{{}}')
        out.append('\\end{pfloesung}')
    if ps_loes:
        teile, fund = ps_loes
        out.append('\\begin{pfloesung}{\\textbf{Prüfstein}}')
        for t, a in teile:
            k, z, _ = loesung_zeilen(D, a, args.art, args.kurs)
            out.append(f'\\lz{{{t}}}{{{k}}}{{{z}}}{{}}')
        out.append('\\end{pfloesung}')
    if zweispaltig:
        out.append('\\end{multicols}')
    out.append('\\end{document}')
    tex = '\n'.join(out)
    return tex   # pfloesung nimmt \\linewidth; in multicols ist das die Spaltenbreite


# ---------------------------------------------------------------------------
# Rückblick (Beschluss 18)
# ---------------------------------------------------------------------------
def fertigkeit_einheiten(D):
    """Fertigkeiten (Zone) -> Einheiten, aus dem Block „Fertigkeiten:“ der Themenkataloge."""
    erg = {}
    for ein in D.eintraege[:2]:
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


WORT_VORAUS = [('Ableitung', 'Ableitungen bilden'), ('Gleichung', 'Gleichungen lösen'),
               ('ausklammern', 'Gleichungen lösen'), ('pq-Formel', 'Gleichungen lösen'),
               ('Punktprobe', 'Funktionswerte'), ('Bruch', 'Bruch'), ('Anteil', 'Bruch'), ('Dezimal', 'Dezimalzahl'), ('Runden', 'Runden'),
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
            m = re.match(r'([a-z-]+?)-e(\d+)-', sp)
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
    if not wahl:
        # Abitur (Lauf B2): der Themenkatalog trägt keine Zeile „Fertigkeiten:“ mit Einheiten –
        # alle Zone-Fertigkeiten des Haupteintrags (Kapitel) sind Voraussetzungen (Entscheidung)
        wahl = [kk for kk in ketten if kk[0] == D.kapitel]
    voraus = set()
    for st in kern:
        for i in st.ids:
            for v in (D.kat.get(i, {}).get('voraussetzungen', '') or '').split('|'):
                if v:
                    voraus.add(v)
    ohne = []
    for v in sorted(voraus):
        treffer = [kk for kk in ketten if any(w in v and w2 in kk[1] for w, w2 in WORT_VORAUS)]
        if treffer:
            for t in treffer[:1]:
                if t not in wahl:
                    wahl.append(t)
        else:
            ohne.append(v)
    if ohne and len(ohne) <= 8:
        for v in ohne:
            D.befund(f'Rückblick: Voraussetzung „{v}“ (Katalogfeld) hat keine Zone-Aufgabe')
    elif ohne:
        D.befund(f'Rückblick: {len(ohne)} Einträge des Katalogfelds voraussetzungen ohne passende '
                 f'Zone-Fertigkeit (Wortliste WORT_VORAUS kennt die Abitur-Wörter nicht), z. B. '
                 + '; '.join(f'„{v}“' for v in ohne[:4]))
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
def uebung_waehlen(D, stufen, B):
    """N5.22: 4–8 fremde Aufgaben der Stufe(n) des Blatts, leicht -> schwer, verschiedene Sachen, je Stufe nie
    schwerer als deren schwerste BB/BE-Aufgabe (Stufen ohne BB/BE: keine), keine unsicheren, keine Kopien
    (gleichartig zu einer Aufgabe des Blatts oder einer schon gewählten). Weniger als 4: kein Anhang.
    Entscheidung: Verteilung reihum über die Stufen, damit nicht eine Stufe den Anhang füllt."""
    import functools
    auf_blatt = [x for st in stufen for _, _, gl in st.gruppen for x in gl] + [x for st in stufen for x in st.vor]
    auf_blatt = auf_blatt + [g for x in auf_blatt for g in getattr(x, 'glieder', [])]
    je = []
    for st in stufen:
        mass = getattr(st, 'mass', None)
        if not mass:
            continue
        ks = []
        for r in D.fremd:
            if r.get('id') in B.benutzt or not stufe_trifft(r.get('stufe'), st.name):
                continue
            a = kandidat(D, r, st, 'fremd', mass)
            if a and not a.unsicher and not any(gleichartig(a, b) for b in auf_blatt if not isinstance(b, Buendel)):
                ks.append(a)
        ks.sort(key=functools.cmp_to_key(vergleich))
        je.append(ks)
    wahl, i = [], 0
    while len(wahl) < 8 and any(je):
        ks = je[i % len(je)]
        while ks:
            a = ks.pop(0)
            if any(a.id == w.id or gleichartig(a, w) or (sache(a) & sache(w)) for w in wahl):
                continue
            wahl.append(a)
            break
        i += 1
    if not wahl:
        D.uebung_grund = 'keine passende'   # Punkt 31: keine Untergrenze; passt keine, entfällt der Anhang
        return []
    for a in wahl:
        B.benutzt.add(a.id)
    return sorted(wahl, key=functools.cmp_to_key(vergleich))


def heft_tex(D, args, titel, unter, rb, teile, ps, uebung=None, schluss=None):
    """Kopf nur der Name, die Prüfungsart klein (N3.14: „Grundwert G“ · „P10“); unten nur Seitenzahl und
    Fuß, keine laufende Titelzeile (\\pfheftstil, mathblatt 2026-10-06c)."""
    SORT.clear(); NR_VON.clear(); STECKT.clear(); RUECK.clear()
    out = [KOPF.replace('\\begin{document}', ''), '\\begin{document}', '\\pfheftstil',
           f'\\pfheftkopf{{{titel}}}{{{unter}}}']
    nr, loes = 0, []
    # Rückblick nur, was diese Leiter (dieses Blatt bzw. diese Portion) gleich braucht (N2.10)
    im_blatt = set()
    for st, idx in teile:
        bl = bloecke(st)
        for i in idx:
            art_, inh = bl[i]
            for x in (inh if art_ == 'kopf' else inh[2]):
                im_blatt.add(id(x))
                for g_ in getattr(x, 'glieder', []):
                    im_blatt.add(id(g_))
    rb = [a for a in (rb or []) if any(id(g) in im_blatt for g in a.gebraucht)]
    if rb:
        t, nr, l = setze_rueckblick(D, args, rb, nr)
        out.append(t); loes += l
    t, nr, l = setze_bloecke(D, args, teile, nr, set())
    out.append(t); loes += l
    if uebung:
        # N5.22: Anhang „Mehr zum Üben“ zwischen Kernteil und Prüfstein
        out.append('\\pfstufekopf[suebung]{Mehr zum Üben}{aus anderen Ländern, leicht $\\to$ schwer}')
        for a in uebung:
            nr += 1
            out.append(aufgabe_tex(D, a, nr, args.art, [], args.kurs))
            loes.append((f'{nr}.', a))
            SORT.append(('Mehr zum Üben', nr, 'Übung', a))
            NR_VON[a.id] = nr
    if schluss:
        # N6.26 Behalten: „Zum Schluss“ zwei ältere Aufgaben (Fokus), nach Kernteil und Anhang
        out.append('\\pfstufekopf[sschluss]{Zum Schluss}{zwei ältere Aufgaben, damit nichts verloren geht}')
        for a in schluss:
            nr += 1
            out.append(aufgabe_tex(D, a, nr, args.art, [], args.kurs))
            loes.append((f'{nr}.', a))
            SORT.append(('Zum Schluss', nr, 'Zum Schluss', a))
            NR_VON[a.id] = nr
    ps_loes = None
    if ps:
        t, ps_loes = setze_pruefstein(D, args, ps)
        out.append(t)
    out.append('\\end{document}')
    tex = '\n'.join(out)
    for z, st in STECKT.items():
        tex = tex.replace(f'%%STECKT {z}%%', steckt_text(D, st, args.kurs))
    return tex, loes, ps_loes


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
    try:
        float(w)
    except (TypeError, ValueError):   # Ausdruck mit Variable (Lauf C, Dreiecke): kein Zahlwert
        D.n_exakt_offen += 1
        return
    if abs(float(w) - g) < 1e-9:
        return   # Überschlag oder glatter Wert: ≈ steht für das Schätzen, kein exakter Wert davor
    e = w / 100 if prozent else w
    if not e.is_Rational and abs(float(w) - g) <= 0.06 * max(1, abs(g) / 100):
        # Vielfache von π bzw. Wurzeln (4π ≈ 12,6 cm; Reparatur Punkt 11)
        q = sympy.nsimplify(e / sympy.pi)
        if q.is_Rational and q.q <= 100 and len(sympy.latex(e)) <= 16 or \
                (e.is_Mul or e.is_Pow) and e.has(sympy.sqrt(2).func) and len(sympy.latex(e)) <= 16:
            ex = sympy.latex(e).replace('\\frac', '\\tfrac')
            if not prozent:
                ex += rhs[zt.end():]
            a.kurz = f'${ex} \\approx {rhs}${nach}'
            return
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


SORT = []   # (Stufe, Nr., Gruppe, Aufgabe) des zuletzt gesetzten Hefts


def sortierung_md(titel):
    """Tabelle der Reihenfolge und maschinelle Prüfung (zweite Reparatur Punkt 4): in jeder Gruppe
    steigt der Schlüssel (Zahlklasse, Grundfall, Schritte, Fragen, Höhe, Text, Satz, Punkte) nicht ab;
    die Gruppen einer Stufe stehen nach gruppen_schluessel ihrer leichtesten Aufgabe."""
    zl = [f'# Sortierung {titel}', '', 'Spalten: Zahlklasse 0 Kopf, 1 glatt, 2 krumm; Schritte; Fragen; '
          'Höhe 0 Vorstufe … 3 Prüfung; Herkunft.', '',
          '| Stufe | Nr. | Gruppe | Zahlkl. | Schritte | Fragen | Höhe | Herkunft | Aufgabe |',
          '|---|---|---|---|---|---|---|---|---|']
    fehler = []
    # Prüfung (Korrektur Lauf C): je Stufe ohne Vorstufen und Prüfstein: (b) Zahlklasse steigt nicht ab
    # (außer im Schluss); (c) in jeder Gruppe Schwierigkeit monoton, Gruppen einer Zahlklasse nach ihrer
    # leichtesten Aufgabe; (d) letzte Aufgabe ist die schwerste echte, davor nur schwerere eigene
    stufen = OrderedDict()
    for stn, nr, g, a in SORT:
        her = {'echt': a.id, 'zone': 'Rückblick', 'fremd': 'fremd ' + a.id, 'heraus': 'herausgelöst ' + a.id,
               'erkennen': 'Erkennen'}.get(a.art, 'eigene')
        zl.append(f'| {stn} | {nr} | {g} | {a.zk} | {schrittzahl(a)} | {a.fz} | {min(a.hrang, 3)} | {her} | '
                  f'{klartext(a.text)[:60].replace("|", "/")} |')
        if g in ('Vorstufe', 'Prüfung', 'Bündel', LEITER, ERKENNEN, 'Übung', VERSTAENDNIS, 'Zum Schluss'):
            continue   # Bündel folgt seiner ersten Aufgabe, Leiter und Erkennen haben feste Plätze (N2.8, N2.11, N4.19)
        stufen.setdefault(stn, []).append((nr, g, a))
    for stn, ls in stufen.items():
        haupt = [x for x in ls if x[1] != SCHLUSS]
        for (n1, g1, a1), (n2, g2, a2) in zip(haupt, haupt[1:]):
            if vergleich(a2, a1) < 0:
                fehler.append(f'{stn}: Nr. {n2} leichter als Nr. {n1}')
        echt = [a for _, _, a in ls if a.art == 'echt' or getattr(a, 'ist_top', False)]
        if echt:
            import functools
            top = next((a for a in echt if getattr(a, 'ist_top', False)), None)
            if top is None:
                if not any(g == SCHLUSS for _, g, _ in ls):
                    continue   # Portion endet vor dem Schluss der Stufe (Serie): keine Schlussprüfung
                top = max(echt, key=functools.cmp_to_key(vergleich))
            if ls[-1][2] is not top:
                fehler.append(f'{stn}: letzte Aufgabe Nr. {ls[-1][0]} ist nicht die schwerste echte')
            for nr, g, a in ls:
                if g == SCHLUSS and a is not top and (a.art == 'echt' or vergleich(a, top) <= 0):
                    fehler.append(f'{stn}: Nr. {nr} im Schluss, aber nicht schwerer als die schwerste echte')
    if RUECK:
        # Prüfstein N2.10: zu jeder Rückblick-Aufgabe die Nummer, ab der sie gebraucht wird
        zl += ['', '## Rückblick: gebraucht ab', '', '| Nr. | Aufgabe | gebraucht ab Nr. |', '|---|---|---|']
        for n, a in RUECK:
            ab = [NR_VON.get(g.id) for g in a.gebraucht if hasattr(g, 'id')]
            ab = [x for x in ab if x]
            zl.append(f'| {n} | {klartext(a.text)[:60].replace("|", "/")} | {", ".join(map(str, ab)) or "–"} |')
            if not ab:
                fehler.append(f'Rückblick Nr. {n}: kommt in der Leiter nicht wieder vor')
    zl += ['', '## Prüfung', ''] + (['- ' + f for f in fehler] if fehler else ['- keine Abweichung'])
    return '\n'.join(zl) + '\n', fehler


def register(args, name, ordner, seiten):
    """Eine Zeile in bau/register.csv (Kennung PRZ-PH<n>, Rezept PH = Prüfungsheft)."""
    p = os.path.join(BANK, 'bau', 'register.csv')
    zeilen = open(p, encoding='utf-8').read().splitlines()
    pfad = os.path.relpath(ordner, BANK)
    alt = [z.split(';')[0] for z in zeilen if z.endswith(';' + pfad)]
    zeilen = [z for z in zeilen if not z.endswith(';' + pfad)]
    kp = D_AKT.pr['kennung']
    if D_AKT.pr['ordner'] == 'msa':
        # Kennung je Kapitel (Lauf C): Kürzel des ersten Bankeintrags (katalog/_kuerzel.csv) + PH
        kz = os.path.join(D_AKT.mn, 'katalog', '_kuerzel.csv')
        if os.path.exists(kz):
            for z in open(kz, encoding='utf-8'):
                f = z.strip().split(';')
                if len(f) >= 2 and f[1] == D_AKT.eintraege[0]:
                    kp = f[0] + '-PH'
                    break
    nrn = [int(z.split(';')[0][len(kp):]) for z in zeilen if re.match(kp + r'\d+;', z)]
    kenn = alt[0] if alt else f'{kp}{max(nrn + [0]) + 1}'   # Neubau behält seine Kennung
    best = (f'kapitel={args.kapitel}, art={args.art}, portion={args.portion or "–"}, '
            f'fokus={args.fokus or "–"}, kurs={args.kurs}, seiten={seiten}')
    try:
        commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=BANK, capture_output=True,
                                text=True).stdout.strip()
    except Exception:
        commit = ''
    zeilen.append(f'{kenn};{args.datum};{",".join(D_AKT.eintraege)};PH;{best};{commit};'
                  f'pruefheft.py v0.3;Version 2026-10-06c;{pfad}')
    open(p, 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')


def anhang(D, args, stufen, B, titel, unter, teile, arbeit):
    """Punkt 31 (Lehrer 06.10. abends, ersetzt N5.22 teilweise): Anhang „Mehr zum Üben“ nie automatisch, nur
    auf Zuruf (--uebung); so viele passende Aufgaben, wie da sind, höchstens 8; passt keine, entfällt er.
    Serien-Portionen rufen ihn nie. --ohne-uebung bleibt (wirkungslos, alte Aufrufe)."""
    if not args.uebung or args.ohne_uebung:
        D.uebung_info = 'aus (nur auf Zuruf --uebung)'
        return []
    wahl = uebung_waehlen(D, stufen, B)
    D.uebung_info = f'{len(wahl)} von höchstens 8' if wahl else 'keine passende'
    return wahl


# ---------------------------------------------------------------------------
# Fokusblatt Grundform G1 (Beschlüsse 07.10., bau/pruefheft/beschluesse-2026-10-07.md)
# Gilt, wenn der Steckbrief des Fokus Teil 5 „Arten“ hat; sonst baut --fokus wie bisher.
# Aufbau: Kopf (B2) · Begriff erkennen (A1) · Merkkasten nur Formel (B7) · Formel aufstellen (A2) ·
# je Art (A3, Reihenfolge des Steckbriefs, versteckte zuletzt): Überschrift = Kurzname, kurze Leiter
# (Leiter-Bank, eigene mit glatten Zahlen B10), höchstens eine fremde Aufgabe mit genau dem Handgriff
# (F1, nur wenn die Art weniger als drei BB/BE-Aufgaben hat), dann die Gruppen (G1): je Gruppe eine
# Aufgabe normal, die übrigen BB/BE-Originale eingerückt, eine Schriftstufe kleiner (B6) · Schlusszeile
# (F3, F4). Kein Rückblick ohne Eintrag im Steckbrief (A1), kein „Zum Schluss“ (F5), kein Beispiel (F6),
# keine Kommentarzeilen (B1). Gekürzte Fassungen (T1–T6) stehen als Daten in msa/gekuerzt-p10.csv.
# ---------------------------------------------------------------------------
G1_PRAEAMBEL = r'''\makeatletter
% Überschrift (Art, Gruppe) im Kasten der nächsten Aufgabe: nie allein am Seitenende (wie \pfab)
\let\gkopf\empty
\newcommand{\gueber}[1]{\gdef\gkopf{#1}}
\newcommand{\gueberdazu}[1]{\ifx\gkopf\empty\gdef\gkopf{#1}\else\expandafter\gdef\expandafter\gkopf\expandafter{\gkopf#1}\fi}
% eingerückt (B6): \gEin Einzug, \gSchrift eine Stufe kleiner; die Überschrift bleibt ohne Einzug
\newlength{\gEin}\setlength{\gEin}{0pt}
\let\gSchrift\relax
% Ankreuzzeile mit hängendem Einzug (lange Aussagen brechen unter dem Text um, nicht unter dem Kästchen)
\renewcommand{\pfkreuzzeile}[1]{\par\noindent\hangindent3.2em\hangafter1\hspace*{1.6em}$\square$\ #1\par}
% Bauregeln 6.7: kurze Optionen in einer Zeile
\newcommand{\gkreuzreihe}[1]{\par\noindent\hspace*{1.6em}#1\par}
\newcommand{\gkreuz}[1]{$\square$\ #1\hspace{2.2em}}
% Bauregeln 6.6: links, was man ansieht, rechts, was man tut; Spaltengrenze auf dem ganzen Blatt an derselben
% Stelle (halbe Satzbreite vom linken Rand); untereinander, wenn die Skizze breiter als die linke Spalte ist
\newsavebox{\gbox}\newlength{\gLinks}
\newcommand{\gzwei}[2]{\par\smallskip\noindent\sbox{\gbox}{#1}%
  \setlength{\gLinks}{\dimexpr0.5\textwidth-\gEin-\mbpfnr\relax}%
  \ifdim\wd\gbox>\dimexpr\gLinks-4mm\relax
    \usebox{\gbox}\par\smallskip\noindent\begin{minipage}{\linewidth}#2\end{minipage}%
  \else
    \begin{minipage}[c]{\gLinks}\usebox{\gbox}\end{minipage}%
    \begin{minipage}[c]{\dimexpr\linewidth-\gLinks\relax}#2\end{minipage}%
  \fi\par}
\RenewDocumentEnvironment{pfaufg}{m m m}{%
  \begin{lrbox}{\mbaufgabebox}\begin{minipage}[t]{\linewidth}%
  \ifx\gkopf\empty\else\noindent\gkopf\par\global\let\gkopf\empty\fi
  \gSchrift\noindent\hspace*{\gEin}\mbpfrandmarke{#1}%
  \begin{minipage}[t]{\mbpfnr}\strut\textbf{#2}\end{minipage}%
  \begin{minipage}[t]{\dimexpr\linewidth-\gEin-\mbpfnr-\mbpfbe\relax}\raggedright\strut\ignorespaces}%
 {\end{minipage}%
  \begin{minipage}[t]{\mbpfbe}\raggedleft\small\color{mbgrau}\strut#3\end{minipage}%
  \end{minipage}\end{lrbox}%
  \setlength{\mbaufgabehoehe}{\dimexpr\ht\mbaufgabebox+\dp\mbaufgabebox\relax}%
  \par\addvspace{6pt}\Needspace*{\mbaufgabehoehe}%
  \noindent\usebox{\mbaufgabebox}\par\addvspace{6pt}}
\makeatother
'''
KENN_ZEICHEN = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ'   # B3: 2–9 und A–Z ohne I und O


def g1_kennung(pfad, schwach=False):
    """B3: drei Zeichen, eindeutig gegen bau/register.csv; ein Neubau desselben Ordners behält seine Kennung;
    schwache Fassung „ +“ dahinter."""
    import hashlib
    p = os.path.join(BANK, 'bau', 'register.csv')
    zeilen = open(p, encoding='utf-8').read().splitlines()[1:]
    for z in zeilen:
        f = z.split(';')
        if f[-1] == pfad and re.fullmatch(r'[2-9A-HJ-NP-Z]{3}( \+)?', f[0]):
            return f[0]
    belegt = {z.split(';')[0].replace(' +', '') for z in zeilen}
    h = int(hashlib.sha1(pfad.encode()).hexdigest(), 16)
    while True:
        k = ''.join(KENN_ZEICHEN[(h >> (5 * i)) % 32] for i in range(3))
        if k not in belegt:
            return k + (' +' if schwach else '')
        h += 1


def g1_register(args, kenn, ordner, seiten, n_aufg):
    p = os.path.join(BANK, 'bau', 'register.csv')
    zeilen = open(p, encoding='utf-8').read().splitlines()
    pfad = os.path.relpath(ordner, BANK)
    zeilen = [z for z in zeilen if not z.endswith(';' + pfad)]
    best = (f'kapitel={args.kapitel}, art={args.art}, fokus={args.fokus}, grundform=G1, kurs={args.kurs}, '
            f'seiten={seiten}, aufgaben={n_aufg}')
    commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=BANK, capture_output=True,
                            text=True).stdout.strip()
    zeilen.append(f'{kenn};{args.datum};{",".join(D_AKT.eintraege)};F;{best};{commit};'
                  f'pruefheft.py v0.5;Version 2026-10-06c;{pfad}')
    open(p, 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')


def ueberstrich(t):
    """B8: Strecke mit Überstrich ($\\overline{AB}$), auch im Quadrat; nur außerhalb von $…$ und nur bei zwei
    Großbuchstaben, die frei stehen (Dreieck ABC und Abkürzungen bleiben)."""
    if not t:
        return t
    aus = {'BB', 'BE', 'EU', 'OK', 'TV', 'CD', 'PC'}
    out = []
    for m, s in teile_math(t):
        if m:
            out.append('$' + s + '$')
            continue
        s = re.sub(r'(?<![A-Za-zÄÖÜäöüß\\])([A-Z])([A-Z])(?![A-Za-zÄÖÜäöüß])(²)?',
                   lambda x: x.group(0) if x.group(1) + x.group(2) in aus else
                   ('$\\overline{' + x.group(1) + x.group(2) + '}' + ('^2' if x.group(3) else '') + '$'), s)
        out.append(s)
    return ''.join(out).replace('$$', '')


def _de_num(v):
    return ('%g' % v).replace('.', '{,}')


def fall_dreieck(spec, massstab=1.0, marke=True, hoehe=False):
    """Dreieck im Fälle-Format des Steckbriefs bzw. der gekürzten Fassungen:
    „(x|y) (x|y) (x|y); Seiten a b c (oder a / b / c, – = ohne); Ecken A B C; rechter Winkel 1–3 oder 0;
    nicht maßstabsgerecht“. Seite i liegt Ecke i gegenüber. Beschriftung neben der Linie, nach außen (B9);
    Rechtwinkelmarke Bogen mit Punkt (Katalog)."""
    spec = spec.replace('−', '-')
    pts = [(float(a.replace(',', '.')) * massstab, float(b.replace(',', '.')) * massstab)
           for a, b in re.findall(r'\((-?[\d,]+)\|(-?[\d,]+)\)', spec)][:3]
    m = re.search(r'Seiten\s+([^;]+)', spec)
    seiten = []
    if m:
        s = m.group(1).strip()
        seiten = [x.strip() for x in (s.split(' / ') if ' / ' in s else s.split())]
    m = re.search(r'Ecken\s+([^;]+)', spec)
    ecken = m.group(1).split() if m else []
    m = re.search(r'rechter Winkel (\d)', spec)
    rw = int(m.group(1)) if m else 0
    gx, gy = sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3
    z = [r'\begin{tikzpicture}[line width=0.7pt,baseline=(current bounding box.north)]']
    for i, p in enumerate(pts):
        z.append(r'\coordinate (P%d) at (%.3f,%.3f);' % (i + 1, p[0], p[1]))
    z.append(r'\draw (P1) -- (P2) -- (P3) -- cycle;')
    if rw and marke:
        a, b = [k for k in (1, 2, 3) if k != rw]
        z.append(r'\mbrwmarke{(P%d)}{(P%d)}{(P%d)}' % (rw, a, b))
    for i in range(3):
        a, b = [k for k in range(3) if k != i]
        mx, my = (pts[a][0] + pts[b][0]) / 2, (pts[a][1] + pts[b][1]) / 2
        if i < len(seiten) and seiten[i] not in ('–', '-', ''):
            lab = seiten[i]
            lab = lab if '$' in lab or ' ' in lab else '$' + lab + '$'
            lab = tx(lab)
            dx, dy = pts[b][0] - pts[a][0], pts[b][1] - pts[a][1]
            n = (dx * dx + dy * dy) ** 0.5 or 1
            nx, ny = -dy / n, dx / n
            if nx * (mx - gx) + ny * (my - gy) < 0:
                nx, ny = -nx, -ny
            anker = ('west' if nx > 0.38 else 'east' if nx < -0.38 else '') if abs(nx) > 0.38 else ''
            anker = (('south ' if ny > 0.38 else 'north ' if ny < -0.38 else '') + anker).strip() or 'center'
            z.append(r'\node[font=\small,anchor=%s,inner sep=1.5pt] at (%.3f,%.3f) {%s};'
                     % (anker, mx + nx * 0.08, my + ny * 0.08, lab))
        if i < len(ecken):
            dx, dy = pts[i][0] - gx, pts[i][1] - gy
            n = (dx * dx + dy * dy) ** 0.5 or 1
            z.append(r'\node[font=\small] at (%.3f,%.3f) {$%s$};' % (pts[i][0] + dx / n * 0.3, pts[i][1] + dy / n * 0.3, ecken[i]))
    if hoehe:
        # Höhe von Ecke 3 auf die Seite P1P2 (gleichschenklig: Mitte), gestrichelt, rechter Winkel, „h“ rechts daneben
        fx, fy = (pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2
        z.append(r'\coordinate (H) at (%.3f,%.3f); \draw[dashed,line width=0.5pt] (P3) -- (H); \mbrwmarke{(H)}{(P2)}{(P3)}'
                 r'\node[font=\small,anchor=west] at ($(H)!0.45!(P3)+(0.06,0)$) {$h$};' % (fx, fy))
    if 'nicht maßstabsgerecht' in spec:
        z.append(r'\node[font=\scriptsize,mbgrau,anchor=north west] at ([yshift=-2pt]current bounding box.south west) {nicht maßstabsgerecht};')
    z.append(r'\end{tikzpicture}')
    return ''.join(z), rw, seiten


def g1_bankfigur(a):
    """\\dreieck der Bank (Beschriftung auf der Linie) -> fall_dreieck (B9: neben der Linie, nach außen); nennt der
    Text die Höhe h eines gleichschenkligen Dreiecks, wird sie gestrichelt mit rechtem Winkel eingezeichnet."""
    m = re.match(r'\\dreieck\{\(([-\d.]+),([-\d.]+)\)\}\{\(([-\d.]+),([-\d.]+)\)\}\{\(([-\d.]+),([-\d.]+)\)\}'
                 r'\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}',
                 (a.abb or '').strip())
    if not m:
        return
    v = [float(x) for x in m.groups()[:6]]
    labs = [re.sub(r'\\text\{\s*(.*?)\}', r' \1', x).strip() or '–' for x in m.groups()[6:9]]
    labs = [('$' + x.split(' ', 1)[0] + '$ ' + x.split(' ', 1)[1]) if ' ' in x and x != '–' else x for x in labs]
    pts = ' '.join('(%s|%s)' % (('%g' % v[i]).replace('.', ','), ('%g' % v[i + 1]).replace('.', ',')) for i in (0, 2, 4))
    spec = f'{pts}; Seiten {labs[0]} / {labs[1]} / {labs[2]}; Ecken A B C'
    hoehe = 'gleichschenklig' in klartext(a.text) and re.search(r'Höhe\s*\$?h', a.text)
    a.abb = fall_dreieck(spec, 1.0, hoehe=bool(hoehe))[0]


def g1_skizze(D, spec, iid):
    spec = (spec or '').strip()
    if not spec:
        return ''
    if spec.startswith('tikz:'):
        return spec[5:].strip()
    if spec.startswith('dreieck:'):
        return fall_dreieck(spec[8:], 1.0)[0]
    return abbildung(spec, D, iid)


def lies_gekuerzt(D):
    p = os.path.join(D.mn, D.pr['ordner'], 'gekuerzt-p10.csv')
    D.neu['gekuerzt-p10.csv'] = os.path.exists(p)
    return {r['id']: r for r in lies_csv(p)} if os.path.exists(p) else {}


def g1_echt(D, iid, art_name, voll, gk, sb_art):
    """Original der Art: voll (letzte echte der Art, T3) oder gekürzt (T1–T4); „Nur gekürzt“ ohne Zeile in
    gekuerzt-p10.csv: herausgelöste Fassung (T4); fehlt auch die: nicht gesetzt (Befund)."""
    r = gk.get(iid)
    heraus = [h for h in D.heraus if (h.get('eltern_id') or '').strip() == iid]
    if not voll and not (r and r.get('wortlaut_kurz')) and heraus:
        h = heraus[0]
        a = daten_aufgabe(D, h, art_name, 'heraus')
        kennzahlen(D, a)
        if not g1_sache(a):
            D.befund(f'{iid}: herausgelöste Fassung ohne Sache – nicht gesetzt (T4)')
            return None
        a.hrang = 3
        a.stern = stern_fuer(D, iid)
        a.g1_herkunft = 'nach P10'
        return a
    a = echt_aufgabe(D, iid, art_name)
    if not a:
        return None
    a.hrang = 3
    a.stern = stern_fuer(D, iid)
    a.g1_herkunft = 'BB/BE'
    if r:
        wl = r.get('wortlaut_voll' if voll else 'wortlaut_kurz') or ''
        sk = r.get('skizze_voll' if voll else 'skizze_kurz') or ''
        if wl:
            vor, opts = ankreuz_zerlegen(wl)
            if opts:
                a.text, a.optionen = tx(vor), [tx(o) for o in opts]
                a.kreuz = True
            else:
                a.text, a.optionen = tx(wl), []
            a.abb = g1_skizze(D, sk, iid) if sk else ('' if not voll else a.abb)
            if not voll:
                a.g1_herkunft = 'nach P10'
                a.marke_text = f'nach P10 {jahr_kurz(a.jahr)}'
        if r.get('ergebnis_kurz'):
            a.kurz_roh = [r['ergebnis_kurz']]
        if r.get('zwischen_kurz') or r.get('ergebnis_kurz'):
            a.zw_roh = [x.strip() for x in (r.get('zwischen_kurz') or '').split(';') if x.strip()]
            a.zw = [tx(x) for x in a.zw_roh]
    elif not voll:
        D.befund(f'{iid}: keine gekürzte Fassung in gekuerzt-p10.csv – ungekürzt gesetzt (T3 offen)')
    if not voll and iid in sb_art['nur_gekuerzt'] and not (r and r.get('wortlaut_kurz')):
        D.befund(f'{iid}: nur gekürzt erlaubt, aber keine gekürzte Fassung – nicht gesetzt')
        return None
    if a.kurz_roh:
        a.kurz = '; '.join(tx(x) for x in a.kurz_roh)
    kennzahlen(D, a)
    return a


G1_FACH = {'Dreieck', 'Dreiecks', 'Kathete', 'Katheten', 'Hypotenuse', 'Seite', 'Seiten', 'Länge', 'Strecke',
           'Winkel', 'Satz', 'Pythagoras', 'Höhe', 'Basis', 'Schenkel', 'Grundseite', 'Figur', 'Punkte', 'Punkt',
           'Diagonale', 'Quadrat', 'Rechteck', 'Seitenlänge', 'Flächeninhalt', 'Entfernung', 'Wurzel', 'Gleichung',
           'Rechnung', 'Betrag', 'Menge', 'Anteil'}


def g1_sache(a):
    return {w for w in sache(a) if w not in G1_FACH}


def g1_fremde(D, art, n, mass, gesehen):
    """F1: fremde Aufgaben nur mit genau dem Handgriff der Art (Feld handgriffe, eine Angabe = Stufe der Art);
    Lösung passt zum Fremd-Merkmal der Art; nicht die Merkmale der nicht geprüften Arten; mit Sache (T4); Bild
    zeichenbar; nie schwerer als die BB/BE-Aufgaben der Art (F2: GYM gilt wie ein anderes Land)."""
    if n <= 0:
        return []
    stufe = art.get('Stufe', '')
    fm = art.get('Fremd-Merkmal', '').strip()
    ng = D.sb['arten_kopf'].get('Nicht-geprüft-Merkmal', '').strip()
    kand = []
    for r in D.fremd + D.heraus:
        if r.get('id') in gesehen or not (r.get('id') or '').strip():
            continue
        hs = [h.split(':')[-1].strip() for h in (r.get('handgriffe') or r.get('stufe') or '').split('|') if h.strip()]
        if len(hs) != 1 or not stufe_trifft(hs[0], stufe):
            continue
        el = (r.get('eltern_id') or '')
        if re.match(r'\d{4}-(OS|EBR|FOR)-', el):
            continue   # herausgelöste BB/BE-Aufgaben stehen bei ihrer Art, nicht als fremde
        lo = (r.get('loesung') or '') + ' ' + (r.get('schritte') or '')
        if fm and not re.search(fm, lo):
            continue
        if ng and re.search(ng, r.get('wortlaut', '')):
            continue
        n_bef, n_sk = len(D.befunde), len(getattr(D, 'abb_skizze', []))
        a = daten_aufgabe(D, r, stufe, 'fremd' if not el else 'heraus')
        if (r.get('abbildung') or '').strip() and (not a.abb or len(D.befunde) > n_bef
                                                  or len(getattr(D, 'abb_skizze', [])) > n_sk):
            del D.befunde[n_bef:]
            continue   # Bild nicht zeichenbar (Beschreibungsrahmen): keine fremde Aufgabe ohne ihr Bild
        kennzahlen(D, a)
        if a.zahlart:
            a.zk = zahlart_wert(a.zahlart, a)
        if not g1_sache(a):
            continue
        if mass and (schrittzahl(a) > mass[0] or a.zk > mass[1] or woerter(a) > mass[2]):
            continue
        a.art = 'fremd'
        a.g1_herkunft = 'fremd'
        kand.append(a)
    kand.sort(key=lambda a: (a.zk, schrittzahl(a), woerter(a), a.id))
    for a in kand[:n]:
        gesehen.add(a.id)
    return kand[:n]


def g1_gruppen(art):
    """G1: Gruppen des Steckbriefs [(Name, ids, mit_ueberschrift)]. Eine Gruppe mit einer Aufgabe läuft ohne
    eigene Überschrift: steht sie vor der ersten Gruppe mit mehreren Aufgaben, als eigene Aufgabe normal (sie
    ist ihr eigener Pflichtweg); sonst unter der vorigen Gruppe, eingerückt (nächstverwandt, Entscheidung)."""
    roh = [[n, list(ids)] for n, ids in art['gruppen']] or [[art.get('Kurzname', art['name']), list(art['aufgaben'])]]
    out = []
    for n, ids in roh:
        if len(ids) == 1 and any(len(x[1]) > 1 for x in out):
            for x in reversed(out):
                if len(x[1]) > 1:
                    x[1] += ids
                    break
            continue
        out.append([n, ids])
    mehr = sum(1 for x in out if len(x[1]) > 1)
    return [(n, ids, len(ids) > 1 and (mehr > 1 or len(out) > 1)) for n, ids in out]


def g1_aufgabe_tex(D, a, nr, art, eingerueckt=False):
    """Satz einer Aufgabe (T6: Skizze vor den Antwortmöglichkeiten); Marke grau im Rand, ★ bei nur FOR (F4)."""
    mk = marke(a, 'FOR') if a.art == 'echt' and not a.marke_text else (tx(a.marke_text) if a.marke_text else '')
    if getattr(a, 'stern', False):
        mk = '$\\bigstar$\\,' + mk
    out = [f'\\begin{{{UMG}}}{{{mk}}}{{{nr}.}}{{}}', ueberstrich(a.text)]
    rechts = ''
    if a.optionen:
        kurz_opt = sum(len(klartext(o)) + 4 for o in a.optionen) <= 120
        if kurz_opt and not a.abb:
            rechts = '\\gkreuzreihe{' + ''.join(f'\\gkreuz{{{ueberstrich(o)}}}' for o in a.optionen) + '}'
        else:
            rechts = ''.join(f'\\pfkreuzzeile{{{ueberstrich(o)}}}' for o in a.optionen)
    if getattr(a, 'antwort', ''):
        rechts += '\\par\\noindent ' + a.antwort + '\\par'
    n = 0 if a.art in ('erkennen', 'abruf') else platz(a, art)
    if n and (getattr(a, 'antwort', '') or re.search(r'tabular|leerzelle|leerfeld', (a.abb or '') + a.text)):
        n = 0
    n = min(n, 2) if eingerueckt else n
    if a.abb and not rechts and n:
        rechts, n = f'\\rechenplatz{{{n}}}', 0   # Bauregeln 6.6: Rechenraum rechts neben der Skizze
    if a.abb and rechts:
        out.append('\\gzwei{' + a.abb + '}{' + rechts + '}')   # Bauregeln 6.6
    else:
        if a.abb:
            out.append('\\par\\smallskip\\noindent ' + a.abb + '\\par')
        if rechts:
            out.append(rechts)
    if n:
        out.append(f'\\rechenplatz{{{n}}}')
    k = kurz_kontrolle(a)
    if k:
        out.append(ueberstrich(f'\\fusshilfe{{\\mbox{{{nr}:~{k}}}}}'))
    out.append(f'\\end{{{UMG}}}')
    return '\n'.join(x for x in out if x)


def formel_tex(f):
    """Formel des Steckbriefs (Klartext „G = W · 100 : p“, „a² + b² = c²“) im Mathesatz."""
    f = f.replace('·', r'\cdot ').replace('²', '^2').replace('³', '^3').replace('−', '-')
    return '$' + f + '$'


def g1_synth(nr_text, kurz, zw=None, art='erkennen', aid=''):
    a = Aufgabe()
    a.art, a.id = art, aid
    a.text = nr_text
    a.kurz = kurz
    a.kurz_roh = []
    a.zw, a.zw_roh = list(zw or []), []
    a.hrang = 0
    a.zk, a.tl, a.fz, a.sr = 0, 0, 1, 8
    a.g1_herkunft = 'eigen'
    return a


def g1_zitat(t):
    """Satz in „…“; innere „…“ bleiben (äußeres Paar: erstes „ bis letztes “)."""
    t = (t or '').strip()
    i, j = t.find('„'), t.rfind('“')
    return t[i + 1:j].strip() if 0 <= i < j else t


def g1_erkennen(D, B, sb):
    """A1: erste Sprosse und Erkennungsschritt aus dem Steckbrief: Erkennen-Fälle (Dreiecke verschiedener Lage,
    mit wechselnden Buchstaben, ohne Längen; einer ohne rechten Winkel als Gegenfall) oder Erkennen-Bank (Sätze).
    P1: die Antworten dürfen nicht alle gleich sein."""
    k = sb['arten_kopf']
    frage = g1_zitat(k.get('Erkennen-Frage', ''))
    if not frage:
        return None   # Erkennen und Aufstellen in einer Aufgabe (Bauregeln 3.4)
    faelle = k.get('Erkennen-Fälle') or []
    if isinstance(faelle, str):
        faelle = [faelle] if faelle and not faelle.startswith('(') else []
    if faelle:
        bilder, loes, antw = [], [], []
        for i, f in enumerate(faelle):
            t, rw, seiten = fall_dreieck(f, 0.5, marke=True)
            bilder.append('\\begin{minipage}[t]{0.225\\linewidth}\\centering ' + t
                          + '\\par\\vspace{1mm}{\\small ' + 'abcd'[i] + ')}\\end{minipage}')
            h = seiten[rw - 1] if rw else 'keiner'
            antw.append(h if rw else 'keiner')
            loes.append(f'{"abcd"[i]}) ' + (f'H = ${h}$' if rw else 'kein rechter Winkel'))
        a = g1_synth(tx(frage) + '\\par\\smallskip\\noindent ' + '\\hfill'.join(bilder), '; '.join(loes),
                     aid='erkennen-faelle')
        a.antworten = antw
        return a
    ids = re.findall(r'[a-z-]+-e\d+-k\d+-s\d+-v\d+', k.get('Erkennen-Bank', ''))
    saetze, loes, antw = [], [], []
    for i, sp in enumerate(ids):
        r = D.bank.get(sp)
        if not r:
            D.befund(f'Erkennen-Bank: {sp} fehlt')
            continue
        B.benutzt.add(sp)
        t = re.sub(r'\s*(Welche[rs]?|Was)\b[^.?]*\?\s*$', '', r['aufgabe']).strip()
        saetze.append(f'{"abcdef"[i]}) ' + tx(t, latex=True))
        lo = re.sub(r'\s*\(.*\)\s*$', '', r['loesung']).strip()
        loes.append(f'{"abcdef"[i]}) ' + tx(lo, latex=True))
        antw.append(klartext(lo))
    a = g1_synth(tx(frage) + '\\par\\smallskip\\noindent ' + '\\par\\noindent '.join(saetze), '; '.join(loes),
                 aid='erkennen-bank')
    a.antworten = antw
    return a


def g1_formel(D, sb):
    """A2: Formel aufstellen – Rollen zuordnen, erst in Rollen, dann mit den Buchstaben der Aufgabe."""
    k = sb['arten_kopf']
    frage = g1_zitat(k.get('Formel-Frage', ''))
    faelle = k.get('Formel-Fälle') or []
    if isinstance(faelle, str):
        faelle = [faelle]
    if not frage or not faelle:
        return None
    if all(f.lstrip().startswith('(') for f in faelle):
        bilder, loes, antw = [], [], []
        n = len(faelle)
        breite = '%.3f' % (0.96 / n)
        for i, f in enumerate(faelle):
            t, rw, s = fall_dreieck(f, 0.5 if n > 3 else 0.62)
            h = s[rw - 1]
            kk = [s[j] for j in range(3) if j != rw - 1]
            bilder.append('\\begin{minipage}[t]{' + breite + '\\linewidth}\\raggedright{\\small ' + 'abcd'[i] + ')}\\par'
                          '\\begin{minipage}[b][1.8cm][b]{\\linewidth}\\centering ' + t + '\\end{minipage}\\par'
                          '\\vspace{7mm}\\noindent{\\color{black!45}\\rule{0.92\\linewidth}{0.4pt}}\\end{minipage}')
            loes.append(f'{"abcd"[i]}) ${h}^2 = {kk[0]}^2 + {kk[1]}^2$')
            antw.append(h)
        a = g1_synth(tx(frage) + '\\par\\smallskip\\noindent ' + '\\hfill'.join(bilder), '; '.join(loes),
                     aid='formel-faelle')
        a.antworten = antw
        return a
    saetze, loes, antw = [], [], []
    for i, f in enumerate(faelle):
        s, _, l = f.partition('→')
        saetze.append(f'{"abc"[i]}) ' + tx(s.strip()) + '\\par\\vspace{6mm}\\noindent{\\color{black!45}\\rule{\\linewidth}{0.4pt}}')
        loes.append(f'{"abc"[i]}) ' + tx(l.strip()))
        antw.append(l.strip())
    a = g1_synth(tx(frage) + '\\par\\smallskip\\noindent ' + '\\par\\smallskip\\noindent '.join(saetze),
                 '; '.join(loes), aid='formel-saetze')
    a.antworten = antw
    return a


def g1_schlusszeile(D, sb, mit_stern):
    """F3/F4: klein am Ende: P10-Zahl je Art seit dem ersten Prüfungsjahr (ohne GYM), „EBR und FOR“ oder „nur
    FOR“, nicht geprüfte Arten, ★-Erklärung nur bei Stern, Vorher/Weiter mit Kurznamen."""
    k = sb['arten_kopf']
    seit = min(int(j) for j in D.pruefjahre)
    teile = []
    for a in sb['arten']:
        m = re.match(r'(\d+)×\s*\(([^)]*)\)', a.get('Geprüft', ''))
        if m:
            teile.append((a.get('Kurzname', a['name']), m.group(1), m.group(2)))
    name = k.get('Kurzname', '')
    if len(teile) == 1:
        s = f'{name} in der P10: {teile[0][1]}× seit {seit} ({teile[0][2]}).'
    else:
        kurse = {t[2] for t in teile}
        s = (f'{name} in der P10 seit {seit}: ' + ' · '.join(f'{t[0]} {t[1]}×' + ('' if len(kurse) == 1 else f' ({t[2]})')
                                                        for t in teile)
             + (f' (je {kurse.pop()}).' if len(kurse) == 1 else '.'))
    ng = SB.schuelertext(k.get('Nicht geprüft', ''))
    if ng:
        s += f' Nicht geprüft: {ng}.'
    if mit_stern:
        s += ' \\mbox{$\\bigstar$ = nur FOR.}'
    vw = []
    if k.get('Vorher'):
        vw.append('Vorher: ' + k['Vorher'])
    if k.get('Weiter'):
        vw.append('Weiter: ' + k['Weiter'])
    s = tx(s).replace('\\$', '$').replace('\\mbox\\{', '\\mbox{').replace('.\\}', '.}')
    # zusammen halten: nie über den Seitenrand verteilt
    return ('\\par\\vfill\\noindent\\begin{minipage}{\\linewidth}{\\footnotesize\\color{black!70}' + s
            + (('\\par\\noindent ' + tx(' · '.join(vw))) if vw else '') + '\\par}\\end{minipage}')


def g1_pruefe(D, alle, eintraege):
    """Prüfschritte (T6, P1, B10, B1): kein Satz doppelt in einer Aufgabe; Erkennen/Formel-Antworten nicht alle
    gleich; eigene Aufgaben ohne krumme Zahlen außer „Wurzel geht nicht auf“; keine Kommentarzeilen."""
    fehler = []
    for nr, a in eintraege:
        s = [x.strip().lower() for x in re.split(r'(?<=[.?!])\s+', klartext(a.text)) if len(x.strip()) > 12]
        dop = [x for x, c in Counter(s).items() if c > 1]
        if dop:
            fehler.append(f'T6: Nr. {nr} Satz doppelt: {dop[0][:50]}')
        if getattr(a, 'antworten', None) is not None and len(set(a.antworten)) < 2:
            fehler.append(f'P1: Nr. {nr} Antwort immer gleich ({a.antworten[0] if a.antworten else "–"})')
        if a.art == 'bank' and a.zk == 2 and not re.search(r'[Rr]unde', klartext(a.text)):
            fehler.append(f'B10: Nr. {nr} eigene Aufgabe mit krummen Zahlen')
    return fehler


G1_IDRE = r'\d{4}-[A-Z]+-[A-Z]\d+[a-z]'


def g1_abruf(sb):
    """Bauregeln 3.2: Abruf statt Merkkasten – „Notiere …“ als erste Aufgabe, Lösung knapp im Fuß."""
    k = sb['arten_kopf']
    frage = g1_zitat(k.get('Abruf-Frage', ''))
    if not frage:
        return None
    loes = re.split(r'\s*\(', k.get('Abruf-Lösung', ''))[0].strip()
    a = g1_synth(tx(frage) + '\\hfill{\\color{black!45}\\rule[-1pt]{0.45\\linewidth}{0.4pt}}',
                 formel_tex(loes) if loes else '', aid='abruf')
    a.kurz_roh = [loes] if loes else []
    a.art = 'abruf'
    return a


def g1_art_erkennen(art):
    """Bauregeln 3.3: Erkennen vor einer Art, eine Entscheidung je Teil, beide Arten gemischt (Sätze
    „Text → Entscheidung; Gleichung“): je Fall eine Zeile zum Entscheiden und eine für die Gleichung."""
    frage = g1_zitat(art.get('Erkennen-Frage', ''))
    faelle = art.get('Erkennen-Fälle') or []
    if isinstance(faelle, str):
        faelle = [faelle] if faelle and not faelle.startswith('(') else []
    if not frage or not faelle:
        return None
    linie = '{\\color{black!45}\\rule{%s}{0.4pt}}'
    saetze, loes, antw = [], [], []
    for i, f in enumerate(faelle):
        t, _, l = f.partition('→')
        ent, _, gl = l.partition(';')
        saetze.append(f'{"abcdef"[i]}) ' + tx(t.strip()) + '\\par\\vspace{5mm}\\noindent '
                      + (linie % '0.28\\linewidth') + '\\hspace{1.5em}' + (linie % '0.55\\linewidth'))
        loes.append(f'{"abcdef"[i]}) ' + tx(ent.strip()) + (', $' + gl.strip().replace('²', '^2') + '$' if gl.strip() else ''))
        antw.append(ent.strip())
    a = g1_synth(tx(frage) + '\\par\\smallskip\\noindent ' + '\\par\\smallskip\\noindent '.join(saetze),
                 '; '.join(loes), aid='erkennen-art')
    a.antworten = antw
    return a


def g1_auswahl(art, ids, voll_id, n_max=None):
    """Bauregeln 2.1 (Richtung): aus einer Gruppe (Sorte) eine Aufgabe, aus häufigen (ab drei) zwei; zuerst die
    volle Prüfungsform der Art, dann die mit dem belegten Fehler aus dem Steckbrief, bei Gleichstand die
    jüngste. Reihenfolge des Steckbriefs (leicht → schwer) bleibt."""
    n = n_max or (2 if len(ids) >= 3 else 1)
    fehler = set(re.findall(G1_IDRE, str(art.get('Typischer Fehler', ''))))
    ids = list(dict.fromkeys(ids))
    rang = sorted(ids, key=lambda i: (i != voll_id, i not in fehler, -int(i[:4])))
    wahl = set(rang[:n])
    return [i for i in ids if i in wahl]


def g1_bau(D, args):
    """Bauregeln 2.1: erst alle Originale; füllen sie mehr als drei Seiten, neu mit Auswahl je Sorte."""
    fehler, seiten = g1_bau_einmal(D, args, False)
    if seiten > 3 and not getattr(args, 'alle', False):
        print(f'{seiten} Seiten mit allen Originalen – neu mit Auswahl je Sorte (Bauregeln 2.1)')
        fehler, seiten = g1_bau_einmal(D, args, True)
    return fehler


def g1_bau_einmal(D, args, auswahl):
    sb = D.sb
    B = Bau(D, args)
    D.bau = B
    B.sb_sp = set()
    gk = lies_gekuerzt(D)
    name = f'{args.kapitel}-{args.art}-fokus-{args.fokus.lower()}'
    ordner = args.aus or os.path.join(BANK, 'bau', 'pruefheft', f'{name}-{args.datum}')
    kenn = g1_kennung(os.path.relpath(ordner, BANK), args.art == 'schwach')
    titel = tx(sb['arten_kopf'].get('Kurzname') or sb['name'])
    unter = D.pr['kopf']
    fuss_kenn = ('\\fancyfoot[C]{\\parbox[t]{\\textwidth}{\\mbfhbox\\par\\vspace{1.5mm}{\\footnotesize\\color{mbgrau}'
                 '{\\scriptsize ' + kenn.replace('+', '{+}') + '}\\hfill\\thepage}}}')
    out = [KOPF.replace('\\begin{document}', '') + G1_PRAEAMBEL, '\\begin{document}', '\\pfheftstil', fuss_kenn,
           f'\\pfheftkopf{{{titel}}}{{{unter}}}']
    nr, eintraege, alle = 0, [], []
    herkunft = Counter()
    SORT.clear()

    def setze(a, eingerueckt=False, gruppe=''):
        nonlocal nr
        nr += 1
        eintraege.append((f'{nr}.', a))
        herkunft[getattr(a, 'g1_herkunft', 'eigen')] += 1
        SORT.append((gruppe or '–', nr, 'G1', a))
        a.g1_eingerueckt = eingerueckt
        return g1_aufgabe_tex(D, a, nr, args.art, eingerueckt)

    # Bauregeln 3.2: Abruf statt Merkkasten
    ab = g1_abruf(sb)
    if ab:
        out.append(setze(ab, gruppe='Abruf'))
    # 3.3 Begriff erkennen
    e = g1_erkennen(D, B, sb)
    if e:
        out.append(setze(e, gruppe='Erkennen'))
    # A2 Formel aufstellen
    fa = g1_formel(D, sb)
    if fa:
        out.append(setze(fa, gruppe='Formel aufstellen'))
    gesehen = set()
    mit_stern = False
    for art in sb['arten']:
        an = art.get('Kurzname', art['name'])
        out.append(f'\\par\\addvspace{{6pt}}\\gueber{{\\vspace{{10pt}}{{\\large\\bfseries {tx(an)}}}\\par\\vspace{{2pt}}}}')
        # 3.3 Erkennen vor der Art (gemischte Fälle), 3.5 Einstieg: Ankreuzaufgaben zum Rechenweg der Art
        ea = g1_art_erkennen(art)
        if ea:
            out.append(setze(ea, gruppe=an))
        ein = list(dict.fromkeys(re.findall(G1_IDRE, str(art.get('Einstieg', '')).split('(')[0])))
        if auswahl and ein:
            ein = g1_auswahl(art, ein, None, 1)
        for j, i in enumerate(ein):
            a = g1_echt(D, i, art.get('Stufe', an), False, gk, art)
            if a:
                if j == 1:
                    out.append('\\par\\setlength{\\gEin}{8mm}\\let\\gSchrift\\small')
                out.append(setze(a, j > 0, gruppe=an))
        if len(ein) > 1:
            out.append('\\par\\setlength{\\gEin}{0pt}\\let\\gSchrift\\relax')
        # kurze Leiter der Art (Leiter-Bank; eigene)
        for sp in SB.ids(art.get('Leiter-Bank', '')):
            a = sb_nimm(D, B, sp, art.get('Stufe', an))
            if not a:
                continue
            if D.kapitel == 'prozent' and sprosse_von(a.id).endswith('prozentrechnung-e4-k2-s3'):
                prozent_tabelle(a)
            a.g1_herkunft = 'eigen'
            if (D.bank.get(a.id) or {}).get('hoehe') == 'vorstufe' and not a.optionen:
                a.kurz, a.zw, a.zw_roh = tx(D.bank[a.id]['loesung'], latex=True), [], []   # Vorstufe: Lösung ganz
            g1_bankfigur(a)
            out.append(setze(a, gruppe=an))
        n_bb = len(art['aufgaben'])
        letzte_voll = [i for i in art['aufgaben'] if i not in art['nur_gekuerzt']]
        voll_id = letzte_voll[-1] if letzte_voll else None
        if auswahl:
            art = dict(art)
            roh = art['gruppen'] or [(an, list(art['aufgaben']))]
            art['gruppen'] = [(g, g1_auswahl(art, ids, voll_id)) for g, ids in roh]
            art['aufgaben'] = [i for i in art['aufgaben'] if any(i in ids for _, ids in art['gruppen'])]
        gruppen = g1_gruppen(art)
        echte = {}
        for i in art['aufgaben']:
            a = g1_echt(D, i, art.get('Stufe', an), i == voll_id, gk, art)
            if a:
                echte[i] = a
        mass = schwerste_echt([a for a in echte.values()])
        for a in g1_fremde(D, art, 3 - n_bb, mass, gesehen):
            out.append(setze(a, gruppe=an))
        for gname, ids, kopf in gruppen:
            ls = [echte[i] for i in ids if i in echte]
            if not ls:
                continue
            if kopf:
                # Gruppenüberschrift im Kasten der nächsten Aufgabe (mit der Art-Überschrift, wenn sie aussteht)
                out.append(f'\\gueberdazu{{\\vspace{{4pt}}{{\\bfseries\\small {tx(gname)}}}\\par}}')
            out.append(setze(ls[0], gruppe=gname))
            if len(ls) > 1:
                # B6: eingerückt, eine Schriftstufe kleiner, schwarz; Randmarke grau (Einzug über leftskip und
                # eine um 8 mm schmalere Zeile – pfaufg nimmt \\linewidth)
                out.append('\\par\\setlength{\\gEin}{8mm}\\let\\gSchrift\\small')
                for a in ls[1:]:
                    # Bauregeln 3.6: die volle Prüfungsform ist immer Pflicht
                    out.append(setze(a, a.id != voll_id, gruppe=gname))
                out.append('\\par\\setlength{\\gEin}{0pt}\\let\\gSchrift\\relax')
            mit_stern |= any(getattr(a, 'stern', False) for a in ls)
    out.append(g1_schlusszeile(D, sb, mit_stern))
    out.append('\\end{document}')
    tex = '\n'.join(out)
    # Lösung: wie bisher (typische Fehler oben), Überstrich, Kennung im Fuß
    for _, a in eintraege:
        if getattr(a, 'kurz_roh', None):
            a.kurz_roh = [ueberstrich(tx(x)) if False else x for x in a.kurz_roh]
    ltex = setze_loesung(D, args, titel, eintraege, None)
    ltex = ltex.replace('\\pfheftstil', '\\pfheftstil\n' + fuss_kenn, 1)
    ltex = '\n'.join(ueberstrich(z) if z.startswith('\\lz{') else z for z in ltex.split('\n'))
    # Rest „…, $c$“ am Ende der Zwischenergebnisse (Bank: „$c^2 = 97$, $c \\approx 9{,}8$“ halb abgeschnitten)
    ltex = re.sub(r',\s*\$[a-zA-Z]\$\}\{\}$', '}{}', ltex, flags=re.M)
    fehler = g1_pruefe(D, alle, eintraege)
    arbeit = tempfile.mkdtemp(prefix='pruefheft-')
    os.makedirs(os.path.join(ordner, 'src'), exist_ok=True)
    os.makedirs(os.path.join(ordner, 'pdf'), exist_ok=True)
    bericht, seiten = [], 0
    for nm, t in ((name, tex), (name + '-loesung', ltex)):
        erg = xelatex(t, args.bb, nm, arbeit)
        open(os.path.join(ordner, 'src', nm + '.tex'), 'w', encoding='utf-8').write(t)
        if erg['pdf']:
            shutil.copy(erg['pdf'], os.path.join(ordner, 'pdf', nm + '.pdf'))
        if nm == name:
            seiten = erg['seiten']
        bericht.append(f'{nm}: {erg["seiten"]} Seiten, Fehler {len(erg["fehler"])}, '
                       f'Missing character {erg["missing"]}, Overfull {erg["overfull"]}')
        bericht += ['   ' + fl for fl in erg['fehler'][:5]]
    if not args.ohne_register:
        g1_register(args, kenn, ordner, seiten, len(eintraege))
    zl = [f'# Aufbau {titel} (Grundform G1, Kennung {kenn})', '',
          '| Nr. | Abschnitt | eingerückt | Herkunft | Marke | id |', '|---|---|---|---|---|---|']
    for (n, a), (g, _, _, _) in zip(eintraege, SORT):
        zl.append(f'| {n} | {g} | {"ja" if getattr(a, "g1_eingerueckt", False) else ""} | '
                  f'{getattr(a, "g1_herkunft", "eigen")} | {klartext(marke(a, "FOR") if a.art == "echt" and not a.marke_text else a.marke_text)} | {a.id} |')
    zl += ['', '## Prüfung', ''] + (['- ' + x for x in fehler] if fehler else ['- keine Abweichung'])
    open(os.path.join(ordner, 'aufbau.md'), 'w', encoding='utf-8').write('\n'.join(zl) + '\n')
    print('Grundform G1 (Beschlüsse 07.10.), Kennung', kenn)
    print('\n'.join(bericht))
    print('Ordner:', ordner)
    pfl = sum(1 for _, a in eintraege if not getattr(a, 'g1_eingerueckt', False))
    print(f'Aufgaben: {len(eintraege)} (Pflichtweg {pfl}, eingerückt {len(eintraege) - pfl}); Herkunft: '
          + ', '.join(f'{k} {v}' for k, v in herkunft.items()))
    print('Prüfung:', 'keine Abweichung' if not fehler else '; '.join(fehler))
    if D.befunde:
        print('Datenbefunde:')
        for b in D.befunde:
            print(' -', b)
    return fehler, seiten



def main():
    ap = argparse.ArgumentParser(description='Prüfungsheft aus Daten setzen')
    ap.add_argument('--kapitel', required=True)
    ap.add_argument('--pruefung', choices=sorted(PROFIL), default='p10',
                    help='Prüfungsprofil: p10 (Vorgabe) oder abi-gk (Abitur Grundkurs)')
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
    ap.add_argument('--uebung', action='store_true', help='Anhang „Mehr zum Üben“ (nur auf Zuruf, Punkt 31)')
    ap.add_argument('--ohne-uebung', action='store_true', help='ohne Wirkung seit Punkt 31 (Anhang nie automatisch)')
    ap.add_argument('--ohne-register', action='store_true')
    ap.add_argument('--alle', action='store_true', help='Fokusblatt mit allen Originalen, ohne Auswahl je Sorte (Bauregeln 2.1)')
    ap.add_argument('--nur-register', action='store_true',
                    help='nichts setzen, nur die Registerzeile des schon gebauten Ordners schreiben (Lauf C: '
                         'parallele Bauten mit --ohne-register, danach je Bau einmal --nur-register)')
    args = ap.parse_args()

    global D_AKT, FOKUS_LAUF
    FOKUS_LAUF = bool(args.fokus)
    D = Daten(args.mn, args.kapitel, args.pruefung)
    D_AKT = D
    D.n_exakt_offen = 0
    if args.fokus and D.pr['ordner'] == 'msa':
        # Grundform G1 (Beschlüsse 07.10.): Steckbrief mit Teil 5 „Arten“
        sb = SB.finde(D.mn, D.kapitel, fokus=args.fokus)
        if sb and sb.get('arten'):
            D.sb = sb
            g1_bau(D, args)
            return
    stufen, ps, B = baue_modell(D, args)
    for st in stufen:
        for a in st.vor + [x for _, _, gl in st.gruppen for x in gl]:
            if a.art == 'bank':
                exakt_vor(D, a, D.bank.get(a.id) or {})
    kap = args.kapitel.capitalize()
    # Kopf (N3.14): nur der Name, die Prüfungsart klein; „schwach“ und „Fokus“ stehen nicht mehr im Kopf
    # (Entscheidung: der Name genügt, die Form zeigt das Heft); EBR bleibt, weil es ein anderes Heft ist
    unter = D.pr['kopf'] + (' EBR' if args.kurs == 'EBR' else '')
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
        titel = kopfname(stufen[0])
        if D.sb and len([s for s in stufen if s.gruppen]) > 1:
            # mehrere Stufen: Name aus dem Steckbrief-Titel ohne „Steckbrief“ und Klammer (Entscheidung)
            titel = tx(re.sub(r'^Steckbrief\s+|\s*\(.*$', '', D.sb['titel'])) or titel
        rb = rueckblick(D, args, stufen, B)
        ueb = anhang(D, args, stufen, B, titel, unter, teile_aus(folge), arbeit)
        schl = zum_schluss(D, args, stufen, B, [z['stufe'] for z in D.zu])
        tex, loes, ps_loes = heft_tex(D, args, titel, unter, rb, teile_aus(folge), None, ueb, schl)
    elif args.portion:
        # Serie (Beschluss 19): Portion endet nach einer abgeschlossenen Gruppe (Block); Startmaß
        # --seiten Seiten, gemessen durch Probeläufe; mindestens ein Block je Portion.
        start, vorige, p = 0, None, 0
        while True:
            p += 1
            if start >= len(folge):
                sys.exit(f'Portion {p} ist leer – das Kapitel endet mit Portion {p - 1}')
            benutzt0 = set(B.benutzt)
            def rb_fuer(e=None):
                B.benutzt = set(benutzt0)
                return rueckblick(D, args, [st for st, _ in teile_aus(folge[start:e or len(folge)])], B)
            # Endbau-Nachbesserung 4: binäre Suche über die Blockgrenzen, höchstens 6 Kompilierungen je
            # Portion; ende = größte Grenze, deren Satz in --seiten Seiten passt (mindestens ein Block)
            def passt(e):
                rb = rb_fuer(e)
                tex, _, _ = heft_tex(D, args, f'{kap} \\textperiodcentered{{}} Portion {p}', unter, rb,
                                     teile_aus(folge[start:e]), None)
                return xelatex(tex, args.bb, 'probe', arbeit)['seiten'] <= args.seiten
            lo, hi, n_k = start + 1, len(folge), 0
            if hi > lo:
                hi = min(hi, start + 40)   # obere Schranke: 40 Blöcke je Portion (Entscheidung)
                while lo < hi and n_k < 6:
                    mid = (lo + hi + 1) // 2
                    n_k += 1
                    if passt(mid):
                        lo = mid
                    else:
                        hi = mid - 1
            ende = lo
            rb = rb_fuer(ende)
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
        rb = rueckblick(D, args, stufen, B)
        ueb = anhang(D, args, stufen, B, titel, unter, teile_aus(folge), arbeit)
        tex, loes, ps_loes = heft_tex(D, args, titel, unter, rb, teile_aus(folge), ps, ueb)
    if args.kurs == 'EBR':
        name += '-ebr'
    ordner = args.aus or os.path.join(BANK, 'bau', 'pruefheft', f'{name}-{args.datum}')
    if args.nur_register:
        info = subprocess.run(['pdfinfo', os.path.join(ordner, 'pdf', name + '.pdf')], capture_output=True,
                              text=True).stdout
        register(args, name, ordner, int(re.search(r'Pages:\s+(\d+)', info).group(1)))
        print('Register:', name)
        return
    ltitel = titel
    ltex = setze_loesung(D, args, ltitel, loes, ps_loes)
    # zweispaltig nur, wenn dadurch eine Seite wegfällt; passt alles auf eine Seite, nie (N3.16)
    s1 = xelatex(ltex, args.bb, 'lprobe1', arbeit)['seiten']
    D.loesung_spalten = 1
    if s1 > 1:
        ltex2 = setze_loesung(D, args, ltitel, loes, ps_loes, zweispaltig=True)
        e2 = xelatex(ltex2, args.bb, 'lprobe2', arbeit)
        if e2['seiten'] and e2['seiten'] < s1 and not e2['fehler'] and not e2['overfull']:
            ltex, D.loesung_spalten = ltex2, 2
    D.loesung_seiten_einspaltig = s1
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
    # Sortiertabelle nur aus dem endgültigen Satz (Probeläufe der Serie zählen nicht)
    md, sfehler = sortierung_md(name)
    open(os.path.join(ordner, 'sortierung.md'), 'w', encoding='utf-8').write(md)
    print('Sortierung:', 'keine Abweichung' if not sfehler else '; '.join(sfehler))
    print('\n'.join(bericht))
    print('Ordner:', ordner)
    print('Stufen:', ', '.join(s.name for s in stufen))
    if ps_loes:
        print('Prüfstein:', ps[2])
    print(f'Aufgaben: {len(loes)}; Bankzeilen ohne Feld bild (Aufgabenbild): {D.ohne_bild} von {len(D.bank)}')
    # Nachtrag 06.10.: was an neuen Daten da war und was daraus wurde
    print('Neue Daten:', ', '.join(f'{k} {"ja" if v else "fehlt"}' for k, v in D.neu.items()))
    zahl = Counter(a.art for _, a in loes)
    print(f'Aufgaben nach Herkunft: echt {zahl["echt"]} · fremd {zahl["fremd"]} · herausgelöst {zahl["heraus"]} · '
          f'eigen {zahl["bank"]} · Rückblick {zahl["zone"]} · Erkennen {zahl["erkennen"]}')
    print(f'Herkunft: fremde {D.n_fremd}, herausgelöste {D.n_heraus}, Bündel {D.n_buendel}, '
          f'eigene weg (gleichartig) {D.n_eigen_weg}, eigene über der schwersten echten weg '
          f'{getattr(D, "n_eigen_oben", 0)}, fremde zu schwer/ohne Bild {getattr(D, "fremd_zu_schwer", 0)}/'
          f'{len(getattr(D, "fremd_ohne_bild", []))}, ruhende Bankzeilen {D.n_ruht}, „steckt auch in“ '
          f'{getattr(D, "n_steckt", 0)}, eigene ohne Sache weg {getattr(D, "n_ohne_sache_weg", 0)}, zweischrittig erkannt {getattr(D, "n_zweischritt", 0)}, unsichere gesetzt {getattr(D, "n_unsicher", 0)}, Erkennen {getattr(D, "n_erkennen", 0)}, Lösung {D.loesung_spalten}-spaltig '
          f'(einspaltig {D.loesung_seiten_einspaltig} S.)')
    print(f'Mehr zum Üben: {getattr(D, "uebung_info", "aus (Serie)")}')
    print(f'Sprünge {getattr(D, "n_sprung", 0)}, davon ohne Füller {getattr(D, "n_sprung_offen", 0)}; '
          f'eigene ohne Sprung weg {getattr(D, "n_eigen_kein_sprung", 0)}')
    if getattr(D, 'sb', None):
        print(f'Steckbrief: {os.path.relpath(D.sb["datei"], D.mn)} – Verständnis '
              f'{sum(len(st.verst) for st in stufen)}, Leiter {sum(len(st.sb_leiter) for st in stufen)}, '
              f'Merkkasten {"ja" if any(st.merke for st in stufen) else "nein"}, typische Fehler in der Lösung')
    else:
        print('Steckbrief: keiner')
    if seiten >= 30:
        # N2.9: keine Obergrenze; ab 30 Seiten nennt der Bau den Grund
        n_st = len(stufen)
        print(f'Länge {seiten} Seiten (≥ 30): {n_st} Stufen, {len(loes)} Aufgaben, davon echte '
              f'{sum(1 for _, a in loes if a.art == "echt")}, Vorstufen {sum(len(st.vor) for st in stufen)}')
    if D.n_exakt_offen:
        print(f'Bank-Ergebnisse mit ≈ ohne kurzen exakten Wert: {D.n_exakt_offen}')
    if D.befunde:
        print('Datenbefunde:')
        for b in D.befunde:
            print(' -', b)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Vielfalt der Bank-Aufgaben, die die P10-Prüfungshefte nutzen (ohne Modell).

v0.1, 2026-10-06 (Auftrag B; Regeln bau/pruefheft/beschluesse-2026-10-06b.md
N1 Punkt 3, bank.md „Mengen je Kette“ Zählregel). Anleitung: werkzeuge/vielfalt.md.

Sprossen: Spalte bank_sprossen aller msa/zuordnung-*.csv in mathe-nachhilfe
(„(i)“ und „[…]“ abgeschnitten; msa/prozent-zusatz.jsonl ist keine Sprosse).
Aufgaben: alle Zeilen bank/<eintrag>/e<n>.jsonl mit dieser Sprosse.

Je Aufgabe geschätzt:
  sache      erstes Kontextwort des Aufgabentexts (Hauptnomen ohne
             Mathe-Wortschatz, Operatoren, Namen); ohne Kontext „–“
             (innermathematisch)
  darst      text | tabelle | bild | diagramm | graph (form, grafik, Bausteine
             im Text)
  richtung   vorwaerts | rueckwaerts | vergleichen | pruefen | darstellen
             (Operator, Fragewort, merkmal)
  zahlart    kopf | glatt | krumm (Regel wie zahlklasse() in pruefheft.py,
             hier nachgebaut, damit das Skript nicht am Prüfheft hängt)
  schablone  Klartext von aufgabe + antwort, Bausteinnamen der grafik, alle
             Zahlen durch # ersetzt
Kopien: gleiche Schablone in derselben Sprosse.

Aufruf (Wurzel von aufgabenbank):
  python3 werkzeuge/vielfalt.py                 Bericht nach bau/vielfalt-p10-<datum>.md
  python3 werkzeuge/vielfalt.py --stilllegen    dazu Feld "ruht" in die Bank schreiben
  --mn PFAD  mathe-nachhilfe (Vorgabe ../mathe-nachhilfe)
  --aus DATEI  Berichtsdatei
"""
import argparse, csv, datetime, glob, json, os, re
from collections import Counter, OrderedDict, defaultdict

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)

KAPITEL = OrderedDict([
    ('prozent', 'Prozent'), ('lineare', 'Lineare Funktionen'),
    ('quadratische', 'Quadratische'), ('gleichungssysteme', 'Gleichungssysteme'),
    ('wachstum', 'Wachstum'), ('dreiecke', 'Dreiecke'), ('flaechen', 'Flächen'),
    ('koerper', 'Körper'), ('daten', 'Daten'), ('wahrscheinlichkeit', 'Wahrscheinlichkeit')])

# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------
def klartext(s):
    """LaTeX -> grober Klartext (wie pruefheft.klartext)."""
    s = s or ''
    s = re.sub(r'\\(t?frac)\{([^{}]*)\}\{([^{}]*)\}', r'\2/\3', s)
    s = s.replace('{,}', ',').replace('\\,', '').replace('\\%', '%').replace('$', '')
    s = re.sub(r'\\(kreuz|leerfeld|text|mathrm)\b', ' ', s)
    s = re.sub(r'\\[A-Za-z]+', ' ', s)
    s = s.replace('{', '').replace('}', '').replace('\\\\', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def zahlen(s):
    """[(wert, ist_prozent, roh)]; Jahreszahlen fallen weg (wie pruefheft.zahlen)."""
    t = klartext(s)
    t = re.sub(r'(?<=\d) (?=\d{3}\b)', '', t)
    out = []
    for m in re.finditer(r'(\d+(?:,\d+)?)\s*(%)?', t):
        v = m.group(1)
        if re.fullmatch(r'(19|20)\d\d', v) and not m.group(2):
            continue
        out.append((float(v.replace(',', '.')), bool(m.group(2)), v))
    return out


KOPF_P = {1, 5, 10, 20, 25, 50, 75, 100, 200}   # wie pruefheft.py (Beschluss 3)


def zahlart(r):
    """kopf | glatt | krumm nach pruefheft.zahlklasse: krumm, wenn gerundet wird (≈, „Runde“)
    oder ein Satz Nachkommastellen hat; kopf, wenn alle Sätze in KOPF_P liegen, alle übrigen
    Zahlen ganz mit höchstens zwei geltenden Ziffern sind und das Ergebnis höchstens eine
    Nachkommastelle hat. Abweichung: als Ergebnis gilt die ganze loesung (pruefheft nimmt das
    Kurzergebnis aus bank_loesung)."""
    t, lo = r.get('aufgabe', ''), r.get('loesung', '')
    if '≈' in lo or 'approx' in lo or re.search(r'\b[Rr]unde\b', klartext(t)):
        return 'krumm'
    zs = zahlen(t)
    if any(p and v != int(v) for v, p, _ in zs):
        return 'krumm'
    kopf = True
    for v, p, roh in zs:
        if p:
            kopf &= v == int(v) and (int(v) in KOPF_P or int(v) < 10 or int(v) % 10 == 0)
        else:
            kopf &= v == int(v) and len(str(int(v)).strip('0')) <= 2
    for v, p, roh in zahlen(lo):
        if ',' in roh and len(roh.split(',')[1].rstrip('0')) > 1:
            kopf = False
    return 'kopf' if kopf and zs else 'glatt'


def schablone(r):
    """aufgabe + antwort als Klartext, Bausteinnamen der grafik, Zahlen -> #."""
    t = klartext(r.get('aufgabe', '')) + ' | ' + klartext(r.get('antwort', ''))
    g = r.get('grafik') or ''
    if g:
        t += ' | ' + re.sub(r'\s+', ' ', g)    # Beschriftung und Form der Grafik zählen mit
    t = re.sub(r'\((P10|FHR|Abitur) \d{4}[^)]*\)', '', t)     # Prüfkennung zählt nicht
    t = re.sub(r'(?<=\d)[ .](?=\d{3}\b)', '', t)
    t = re.sub(r'\d+(?:[,.]\d+)?', '#', t)
    return re.sub(r'\s+', ' ', t).strip().lower()


# Wörter, die keine Sache sind: Operatoren, Satzanfänge, Mathe-Wortschatz, Einheiten
STOP = set('''
ein eine einer einen einem eines die der das den dem des wie was wer wo wann warum welche welcher
welches welchen welchem für von vom aus auf bei nach mit zu zum zur dann danach dabei dazu außerdem
jede jeder jedes jeden jetzt beide zwei drei vier fünf zusammen genau man er sie es ihr ihre sein seine
jemand gesucht gegeben gilt im in an am um ist sind hat haben mal nun so ohne also wenn
berechne bestimme gib stelle zeichne begründe kreuze schreibe prüfe rechne löse lies trage ergänze zeige
skizziere erkläre beschrifte weise setze nutze fülle addiere entscheide ordne wähle finde vergleiche
kontrolliere nenne vervielfache beschreibe färbe markiere unterstreiche kreise teile überprüfe
ermittle notiere miss verbinde runde
stelle stellen komma taste rechnung ergebnis ergebnisse lösung lösungen aussage aussagen behauptung
fehler satz sätze zeile zeilen spalte spalten feld felder feldern kästchen fragezeichen schritt reihenfolge
antwort rechenweg begründung wahl angabe angaben werte wert zahl zahlen ziffer ziffern bruch brüche
term terme formel potenz faktor summe anzahl hälfte viertel drittel teil teile rest mal
dreieck dreiecke dreiecks höhe höhen winkel radius koordinatensystem volumen gleichung gleichungen
fläche flächen flächeninhalt parabel figur figuren wahrscheinlichkeit wahrscheinlichkeiten tabelle
seite seiten gerade geraden hypotenuse prozent prozente prozentpunkte länge längen achse achsen grundfläche
punkt punkte punkten grundseite form umfang durchmesser gleichungssystem pyramide kegel kreis kreises
strecke strecken rechteck rechtecks rechtecken graph graphen gegenkathete ankathete kathete katheten
scheitel scheitelpunkt scheitelpunktform zylinder zylinders netz trapez trapezes quadrat quadrats
nullstelle nullstellen kugel kugeln diagonale diagonalen säulendiagramm säulendiagramms schenkel
mantellinie parallelogramm parallelogramms symmetrieachse symmetrieachsen baum baumdiagramm kegels
mittelpunktswinkel kreisdiagramm prisma prismas quader quaders schrägbild spitze funktion funktionen
seitenhöhe sektor steigung steigungsdreieck basiswinkel ecke ecken median mittelwert spannweite
modalwert kreisausschnitt normalparabel körper drachenviereck drachen raute viereck vierecks oberfläche
mantel mantels mantelfläche raumdiagonale grundkante kante kanten kantenlänge seitenlänge seitenfläche
schnittpunkt schnittpunkte wertepaar wertepaare wertetabelle verlängerung mitte mittelpunkt achsenabschnitt
diagramm diagramme säule säulen balken kurve lage symmetrie spiegelbild maße maßen minimum maximum
streifen ganzes ganze ganzen anteil anteile grundwert prozentwert prozentsatz zinssatz zinsen zins
zinseszins kapital wachstumsfaktor abnahme zunahme bestand ergebnisraum ereignis gegenereignis
zufallsexperiment häufigkeit häufigkeiten durchschnitt urliste stichprobe pfad pfade pfadregel
koordinaten koordinate fußpunkt basis bild bilder skizze vorlage abbildung zeichnung rechenplatz
meter zentimeter millimeter kilometer liter milliliter gramm kilogramm cent euro sekunden minute minuten
stunde stunden tag tage tagen woche wochen monat monaten monate jahr jahre jahren
beim kann gehe denke nimm lege bringe überlege subtrahiere verdopple doppelte doppelter einsetzen
schneiden drehen breite größe menge restmenge einheit quadratmeter abstand ausschnitt grundkreis
additionsverfahren einsetzungsverfahren faktorisieren normalform parabeln normalparabeln quadrate
quadratische pythagoras thales winkelsumme dreiecksprisma kästchenpapier äquator zufallsversuch
spiegelbilds scheitels ursprung klammer differenz quotienten lücke tangente hypotenusenquadrat
gleichschenkliges vierecke trapeze rechtecke fünfeck sechseck halbkreis viertelkreis kreisring
drachens drachenvierecks kreisausschnitts grundkanten oberflächen querschnitt großbuchstabe buchstaben
laut unter über weit mittel werten dieselbe darin daraus teils wird kein kleine frage trend
beginn anstieg rückgang unterschied einteilung datenreihe zahlenbeispiel beispiel sachverhalt
situation sachtext wachstum boxplot gewinnwahrscheinlichkeit modell block stück paare zeit
ellipse elf acht sieben mio millionen fünfzigerschritten hunderterschritten zwanzigerschritten
'''.split())

NAMEN = set('''Tom Tim Mia Lea Ole Ben Jonas Paul Lena Jan Jana Anna Lukas Emma Sara Emil Nora Lisa Ali
Kai Kim Lina Eva Mara Ida Nils Finn Leon Max Mila Lara Kaya Nina Paula Ina Pia Leo Can Lars Mo Noah Elif
Luca Lotta Ella Mats Hanna Hannah Jakob Ayla Deniz Malte Greta Frieda Theo Luis Amir Sophie Tilda
Nele Cem Tims Linas Herr Frau Familie Jemand'''.split())

_SACH_ALLE = Counter()


def kandidaten(r):
    t = klartext(r.get('aufgabe', ''))
    t = re.sub(r'\((P10|FHR|Abitur) [^)]*\)', ' ', t)
    out = []
    for i, m in enumerate(re.finditer(r'\b([A-ZÄÖÜ][a-zäöüß]{2,})\b', t)):
        w = m.group(1)
        if w in NAMEN:
            continue
        lw = w.lower()
        if lw in STOP:
            continue
        # zusammengesetzte Mathewörter (Kegeldach bleibt: Dach ist Sache)
        if any(lw.endswith(s) for s in ('winkel', 'fläche', 'dreieck', 'gleichung', 'diagramm',
                                         'tabelle', 'strecke', 'länge', 'höhe', 'wert', 'werte',
                                         'zahl', 'zahlen', 'punkt', 'punkte', 'achse', 'seite')):
            continue
        out.append(lw)
    return out


def norm(w):
    """Genitiv/Plural grob zusammenlegen, wenn der Stamm im Bestand vorkommt."""
    for suf in ('es', 's', 'en', 'n', 'e'):
        if w.endswith(suf) and len(w) - len(suf) >= 3 and _SACH_ALLE.get(w[:-len(suf)]):
            return w[:-len(suf)]
    return w


def sache(r):
    k = [norm(w) for w in kandidaten(r)]
    return k[0] if k else '–'


BAU_GRAPH = ('ksys', 'gerade', 'parabel', 'funktion', 'funktionab', 'punkt')
BAU_DIAGRAMM = ('saeulen', 'saeulenab', 'balkenab', 'kreisdiagramm', 'kreisdiagrammleer', 'liniendia',
                'baumzwei', 'baumdrei', 'baumdreigleich', 'streifen', 'streifenfeld', 'streifenleer',
                'boxplot', 'streifendia')
BAU_TABELLE = ('sachtabelle', 'wertetabelle', 'leerzelle', 'array', 'tabular')


def darstellung(r):
    g = (r.get('grafik') or '') + ' ' + (r.get('aufgabe') or '')
    namen = set(re.findall(r'\\(?:begin\{)?([A-Za-z]+)', g))
    if namen & set(BAU_GRAPH) and 'ksys' in g or namen & {'funktionab'}:
        return 'graph'
    if namen & set(BAU_DIAGRAMM):
        return 'diagramm'
    if r.get('form') == 'tabelle' or namen & set(BAU_TABELLE):
        return 'tabelle'
    gr = (r.get('grafik') or '').strip()
    gn = set(re.findall(r'\\(?:begin\{)?([A-Za-z]+)', gr)) - {'rechenplatz', 'frac', 'text', 'end'}
    if gn:
        return 'bild'
    return 'text'


def richtung(r):
    t = klartext(r.get('aufgabe', ''))
    m = (r.get('merkmal', '') + ' ' + r.get('sprosse_text', '')).lower()
    if r.get('pflicht') in ('fehler', 'begruenden') or re.search(
            r'\b(Prüfe|Überprüfe|Kontrolliere|Entscheide|stimmt|recht hat|wahr oder falsch|richtig gerechnet|'
            r'Fehler|können nicht stimmen|Reicht|reicht|Ist die Aussage|Begründe, ob|Stimmt)\b', t):
        return 'pruefen'
    if re.search(r'\b(Vergleiche|günstiger|teurer|lohnt|größer als|kleiner als|mehr als|weniger als|'
                 r'Unterschied|Welches Angebot|Welcher Tarif|Welche Bank|am größten|am kleinsten)\b', t):
        return 'vergleichen'
    if 'rückwärts' in m or 'umkehr' in m or 'rückwärts' in t.lower():
        return 'rueckwaerts'
    if r.get('form') in ('zeichnen', 'streifenleer') or r.get('pflicht') == 'darstellung' or re.search(
            r'\b(Zeichne|Skizziere|Trage|Beschrifte|Färbe|Markiere|Ordne|Schreibe [^.?]*als|'
            r'Stelle [^.?]*dar|Stelle [^.?]*auf|Ergänze die (Tabelle|Wertetabelle|Figur|Zeichnung))\b', t):
        return 'darstellen'
    if re.search(r'\b(vorher|ursprünglich|ursprüngliche|Wie viel kostete|so, dass|Gib (eine|ein|einen|zwei) '
                 r'[^.?]*an, (die|der|das|deren|dessen)|Finde|Erfinde|Wie (groß|hoch|lang|breit) muss|'
                 r'Welchen Wert muss|Wie viel(e)? muss)\b', t):
        return 'rueckwaerts'
    return 'vorwaerts'


# ---------------------------------------------------------------------------
# Daten
# ---------------------------------------------------------------------------
def lies_zuordnung(mn):
    """-> OrderedDict sprosse -> (kapitel, stufe, kern, innermath); Gegenprobe-Zahlen."""
    sp = OrderedDict()
    roh = 0
    for kap in KAPITEL:
        p = os.path.join(mn, 'msa', f'zuordnung-{kap}.csv')
        with open(p, encoding='utf-8') as f:
            for z in csv.DictReader(f, delimiter=';'):
                for t in z['bank_sprossen'].split():
                    roh += 1
                    if '.jsonl' in t:      # msa/prozent-zusatz.jsonl(5): keine Bank-Sprosse
                        continue
                    b = re.sub(r'\[.*?\]|\(i\)', '', t)
                    e = sp.setdefault(b, dict(kapitel=kap, stufen=[], kern=False, i=False, teil=False))
                    if z['stufe'] not in e['stufen']:
                        e['stufen'].append(z['stufe'])
                    e['kern'] |= z['kern'] == 'ja'
                    e['i'] |= '(i)' in t
                    e['teil'] |= '[' in t
    return sp, roh


def lies_bank():
    """-> {sprosse: [(pfad, zeilennr, zeile)]} aus bank/*/e*.jsonl."""
    out = defaultdict(list)
    for p in sorted(glob.glob(os.path.join(BANK, 'bank', '*', 'e*.jsonl'))):
        if not re.search(r'/e\d+\.jsonl$', p):
            continue
        with open(p, encoding='utf-8') as f:
            for i, l in enumerate(f):
                if l.strip():
                    r = json.loads(l)
                    out[re.sub(r'-v\d+$', '', r['id'])].append((p, i, r))
    return out


# ---------------------------------------------------------------------------
# Kopien
# ---------------------------------------------------------------------------
ZIEL_ZAHL = {'vorstufe': 'kopf', 'grundfall': 'kopf', 'sprosse': 'glatt', 'pflicht': 'glatt',
             'pruefung': 'krumm'}
RANG = {'kopf': 0, 'glatt': 1, 'krumm': 2}


def behalten(gruppe):
    """Welche Zeile einer Kopiengruppe aktiv bleibt: zuerst eine mit original, dann die Zahlart,
    die der hoehe am besten passt (bank.md „Zahlen wachsen mit der Leiter“), dann die erste."""
    def k(x):
        r, za = x['r'], x['zahlart']
        ziel = ZIEL_ZAHL.get(r.get('hoehe'), 'glatt')
        return (0 if r.get('original') else 1, abs(RANG[za] - RANG[ziel]), r['variante'])
    return min(gruppe, key=k)


def still_erlaubt(a, info):
    """Kopie, die ruhen soll (Entscheidung 06.10., Auftrag B): nur Sachaufgaben. Nicht stillgelegt
    werden (1) innermathematische Aufgaben und Sprossen mit (i) – Zählregel bank.md: „Innermathematisch
    genügen andere Zahlen“; (2) hoehe grundfall – das Päckchen (bank.md „Regeln für den Inhalt“)
    verlangt denselben Kontext mit einem wandernden Wert."""
    return a['sache'] != '–' and not info['i'] and a['r'].get('hoehe') != 'grundfall'


def auswerten(mn):
    zu, roh = lies_zuordnung(mn)
    bank = lies_bank()
    for s in zu:
        for _, _, r in bank.get(s, []):
            for w in kandidaten(r):
                _SACH_ALLE[w] += 1
    zeilen = []          # je Sprosse
    for s, info in zu.items():
        aufg = []
        for p, i, r in bank.get(s, []):
            aufg.append(dict(p=p, i=i, r=r, sache=sache(r), darst=darstellung(r), richtung=richtung(r),
                             zahlart=zahlart(r), schab=schablone(r), ruht_vorher=r.get('ruht', '')))
        grp = OrderedDict()
        for a in aufg:
            grp.setdefault(a['schab'], []).append(a)
        kopien, gleich = [], []
        for g in grp.values():
            if len(g) > 1:
                keep = behalten(g)
                for a in g:
                    if a is keep:
                        continue
                    a['gleich_wie'] = keep['r']['id']
                    gleich.append(a)
                    if still_erlaubt(a, info):
                        a['kopie_von'] = keep['r']['id']
                        kopien.append(a)
        aktiv = [a for a in aufg if 'kopie_von' not in a and not a['ruht_vorher']]
        zeilen.append(dict(sprosse=s, info=info, aufg=aufg, kopien=kopien, gleich=gleich, aktiv=aktiv))
    return zeilen, roh, len(zu), sum(len(bank.get(s, [])) for s in zu)


def kennzahlen(z, nur_aktiv=False):
    a = z['aktiv'] if nur_aktiv else z['aufg']
    return dict(n=len(a), sachen=len({x['sache'] for x in a}), darst=len({x['darst'] for x in a}),
                richt=len({x['richtung'] for x in a}), schab=len({x['schab'] for x in a}),
                zahlart=len({x['zahlart'] for x in a}))


def schwach(z):
    k = kennzahlen(z, nur_aktiv=True)
    gr = []
    if k['n'] < 3:
        gr.append(f"{k['n']} aktiv")
    if k['n'] and k['sachen'] == 1:
        s = z['aktiv'][0]['sache']
        gr.append('nur innermathematisch' if s == '–' else f'eine Sache ({s})')
    if k['n'] and k['darst'] == 1:
        gr.append(f"eine Darstellung ({z['aktiv'][0]['darst']})")
    return gr


def vielfalt_wert(k):
    """Sortierschlüssel „schlechteste Vielfalt zuerst“: Anteil verschiedener Schablonen, dann
    Summe der Merkmalszahlen."""
    if not k['n']:
        return (0, 0)
    return (k['schab'] / k['n'], k['sachen'] + k['darst'] + k['richt'])


# ---------------------------------------------------------------------------
# Ausgabe
# ---------------------------------------------------------------------------
def bericht(zeilen, roh, n_sp, n_aufg, datum, stillgelegt):
    L = []
    L.append(f'# Vielfalt der P10-Bankaufgaben ({datum})\n')
    L.append('Erzeugt von `werkzeuge/vielfalt.py` (ohne Modell; Merkmale geschätzt, Regeln in '
             '`werkzeuge/vielfalt.md`). Grundlage: Spalte bank_sprossen der zehn '
             '`msa/zuordnung-*.csv` in mathe-nachhilfe, Zeilen aus `bank/<eintrag>/e<n>.jsonl`.\n')
    L.append(f'Gegenprobe: {roh} Einträge in bank_sprossen, {n_sp} verschiedene Sprossen, '
             f'{n_aufg} Bankzeilen in diesen Sprossen.\n')
    L.append('Spalten: n = Aufgaben (vorher), Kop. = Kopien (gleiche Schablone wie eine aktive '
             'Aufgabe derselben Sprosse), akt. = aktiv nach dem Stilllegen, S = verschiedene Sachen '
             '(„–“ = innermathematisch zählt als eine), D = Darstellungen, R = Fragerichtungen, '
             'Sch = Schablonen, Z = Zahlarten; S/D/R/Z über die aktiven Aufgaben. (i) = in der '
             'Zuordnung als innermathematisch markiert, K = Kern-Stufe.\n')
    # Summen je Kapitel
    L.append('## Summen je Kapitel\n')
    L.append('Kopien = stillgelegt (Sachaufgabe, gleiche Schablone); gleich = alle Zeilen mit der Schablone '
             'einer anderen Zeile derselben Sprosse, auch die, die nach Entscheidung aktiv bleiben '
             '(innermathematisch, (i), Grundfall-Päckchen). schwach: < 3 aktiv | eine Sache | eine '
             'Darstellung (eine Sprosse kann mehrere Gründe haben).\n')
    L.append('| Kapitel | Sprossen | Aufgaben | gleich | Kopien | aktiv | Schablonen | schwach | < 3 | 1 Sache | 1 Darst. |')
    L.append('|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|')
    tot = Counter()
    for kap, name in KAPITEL.items():
        zs = [z for z in zeilen if z['info']['kapitel'] == kap]
        c = Counter(sp=len(zs), n=sum(len(z['aufg']) for z in zs), k=sum(len(z['kopien']) for z in zs),
                    a=sum(len(z['aktiv']) for z in zs), s=sum(kennzahlen(z)['schab'] for z in zs),
                    w=sum(1 for z in zs if schwach(z)), g=sum(len(z['gleich']) for z in zs),
                    w1=sum(1 for z in zs if any(x.endswith('aktiv') for x in schwach(z))),
                    w2=sum(1 for z in zs if any('Sache' in x or 'innermath' in x for x in schwach(z))),
                    w3=sum(1 for z in zs if any('Darstellung' in x for x in schwach(z))))
        tot += c
        L.append(f"| {name} | {c['sp']} | {c['n']} | {c['g']} | {c['k']} | {c['a']} | {c['s']} | {c['w']} | "
                 f"{c['w1']} | {c['w2']} | {c['w3']} |")
    L.append(f"| **Summe** | {tot['sp']} | {tot['n']} | {tot['g']} | {tot['k']} | {tot['a']} | {tot['s']} | "
             f"{tot['w']} | {tot['w1']} | {tot['w2']} | {tot['w3']} |\n")
    # Verteilung der Merkmale
    L.append('## Merkmale über alle aktiven Aufgaben\n')
    alle = [a for z in zeilen for a in z['aktiv']]
    for f, t in (('darst', 'Darstellung'), ('richtung', 'Fragerichtung'), ('zahlart', 'Zahlart')):
        c = Counter(a[f] for a in alle)
        L.append(f'- {t}: ' + ', '.join(f'{k} {v}' for k, v in c.most_common()))
    c = Counter(a['sache'] for a in alle)
    L.append(f"- Sache: innermathematisch {c.get('–', 0)}, mit Kontext {len(alle) - c.get('–', 0)} "
             f"({len(c) - ('–' in c)} verschiedene Kontextwörter); häufigste: "
             + ', '.join(f'{k} {v}' for k, v in c.most_common(16) if k != '–') + '\n')
    # Schwache Sprossen
    L.append('## Schwache Sprossen (Arbeitsliste)\n')
    L.append('Nach dem Stilllegen weniger als 3 aktive Aufgaben, nur eine Sache oder nur eine '
             'Darstellung. Arbeitsliste fürs Auffüllen aus Fremdprüfungen und fürs Herauslösen '
             '(N1 Punkte 2 und 4); hier wird nichts neu geschrieben.\n')
    for kap, name in KAPITEL.items():
        zs = [z for z in zeilen if z['info']['kapitel'] == kap and schwach(z)]
        if not zs:
            continue
        L.append(f'### {name} ({len(zs)})\n')
        L.append('| Sprosse | Stufe | akt. | Grund |')
        L.append('|---|---|--:|---|')
        for z in sorted(zs, key=lambda z: (len(z['aktiv']), z['sprosse'])):
            i = z['info']
            L.append(f"| {z['sprosse']}{' (i)' if i['i'] else ''} | {'; '.join(i['stufen'])}"
                     f"{' (K)' if i['kern'] else ''} | {len(z['aktiv'])} | {', '.join(schwach(z))} |")
        L.append('')
    # Tabelle je Sprosse
    L.append('## Tabelle je Sprosse (schlechteste Vielfalt zuerst)\n')
    for kap, name in KAPITEL.items():
        zs = [z for z in zeilen if z['info']['kapitel'] == kap]
        zs.sort(key=lambda z: (vielfalt_wert(kennzahlen(z)), z['sprosse']))
        L.append(f'### {name}\n')
        L.append('| Sprosse | n | gl. | Kop. | akt. | S | D | R | Sch | Z | Sachen | Darstellungen | Richtungen |')
        L.append('|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|---|---|')
        for z in zs:
            k, ka = kennzahlen(z), kennzahlen(z, True)
            fl = (' (i)' if z['info']['i'] else '') + (' K' if z['info']['kern'] else '')
            sa = ', '.join(sorted({a['sache'] for a in z['aktiv']}))
            da = ', '.join(sorted({a['darst'] for a in z['aktiv']}))
            ri = ', '.join(sorted({a['richtung'] for a in z['aktiv']}))
            L.append(f"| {z['sprosse']}{fl} | {k['n']} | {len(z['gleich'])} | {len(z['kopien'])} | {ka['n']} | {ka['sachen']} | "
                     f"{ka['darst']} | {ka['richt']} | {k['schab']} | {ka['zahlart']} | {sa} | {da} | {ri} |")
        L.append('')
    # Kopien
    L.append('## Gleiche Schablone, aktiv geblieben\n')
    L.append('Gleiche Schablone wie eine andere Zeile der Sprosse, aber nicht stillgelegt: '
             'innermathematisch oder Sprosse mit (i) (Zählregel bank.md: andere Zahlen genügen) oder '
             'hoehe grundfall (Päckchen: ein Wert wandert, der Kontext bleibt). Zahl je Kapitel: '
             + ', '.join(f"{n} {sum(1 for z in zeilen if z['info']['kapitel'] == k for a in z['gleich'] if 'kopie_von' not in a)}"
                         for k, n in KAPITEL.items()) + '.\n')
    L.append('## Stillgelegte Kopien\n')
    L.append('Feld `"ruht": "kopie von <id>"` in der Bankzeile (nicht gelöscht). Behalten wird je '
             'Gruppe die Zeile mit original, sonst die mit der Zahlart, die zur hoehe passt '
             '(Vorstufe/Grundfall kopf, Sprosse glatt, Prüfung krumm), sonst die erste.'
             + ('' if stillgelegt else ' (Dieser Lauf hat nichts geschrieben.)') + '\n')
    for kap, name in KAPITEL.items():
        ks = [a for z in zeilen if z['info']['kapitel'] == kap for a in z['kopien']]
        if not ks:
            continue
        L.append(f'### {name} ({len(ks)})\n')
        for a in ks:
            L.append(f"- {a['r']['id']} → kopie von {a['kopie_von']}")
        L.append('')
    return '\n'.join(L) + '\n'


def stilllegen(zeilen):
    """Schreibt "ruht" in die Bankzeilen der Kopien; Feldfolge bleibt, ruht kommt ans Ende."""
    je_datei = defaultdict(dict)
    for z in zeilen:
        for a in z['kopien']:
            je_datei[a['p']][a['i']] = f"kopie von {a['kopie_von']}"
    n = 0
    for p, ruht in je_datei.items():
        with open(p, encoding='utf-8') as f:
            zl = f.read().split('\n')
        for i, wert in ruht.items():
            r = json.loads(zl[i])
            if r.get('ruht') != wert:
                r['ruht'] = wert
                zl[i] = json.dumps(r, ensure_ascii=False)
                n += 1
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(zl))
    return n, sorted(je_datei)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mn', default=os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe'))
    ap.add_argument('--aus')
    ap.add_argument('--stilllegen', action='store_true')
    ap.add_argument('--datum', default=datetime.date.today().isoformat())
    a = ap.parse_args()
    zeilen, roh, n_sp, n_aufg = auswerten(a.mn)
    if a.stilllegen:
        n, dateien = stilllegen(zeilen)
        print(f'stillgelegt: {n} Zeilen in {len(dateien)} Dateien')
    aus = a.aus or os.path.join(BANK, 'bau', f'vielfalt-p10-{a.datum}.md')
    with open(aus, 'w', encoding='utf-8', newline='\n') as f:
        f.write(bericht(zeilen, roh, n_sp, n_aufg, a.datum, a.stilllegen))
    print(f'Gegenprobe: {roh} Einträge, {n_sp} Sprossen, {n_aufg} Aufgaben')
    print(f'Kopien: {sum(len(z["kopien"]) for z in zeilen)}, schwach: {sum(1 for z in zeilen if schwach(z))}')
    print('Bericht:', os.path.relpath(aus, BANK))


if __name__ == '__main__':
    main()

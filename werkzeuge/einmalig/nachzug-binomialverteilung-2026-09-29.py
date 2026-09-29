"""Nachzug bank/binomialverteilung auf Katalog f56cace (Mappe 29.09.)
und bank.md fünfte Fassung. Einmalig; Aufruf aus der Repo-Wurzel:
    python3 werkzeuge/einmalig/nachzug-binomialverteilung-2026-09-29.py e1|…|e5
Schreibt die Datei ganz (erster Wurf). Übernommene Zeilen bleiben
wortgleich bis auf id, sprosse, kette_nr, quelle, sprosse_text.

Änderungen:
- quelle: Katalogzeilen 125 → 122, 127 → 124 … 131 → 128 (drei
  Erkennungsschritte sind aus „Voraussetzungen“ gestrichen).
- Vorstufen e1–e4: sprosse_text wird der längere Sprossentext bis
  „nichts rechnen“.
- e2: neue Sprosse 2 „die ganze Verteilung für kleines n“ (3 Zeilen),
  die folgenden Sprossen rücken um eins.
- e3: Erkennungsschritt „Treffer oder Niete gezählt?“ (Zeile 43) als
  eigene Kette k1 (4 Zeilen); die übrigen Ketten rücken um eins.
- Grundfall e2–e5 als Päckchen (dieselben n und p, k oder die Frage
  wandert); e1 bleibt (Katalog verlangt vier Kontexte).
- Pflichtformen: fehler v2 → P2, v3 → P1 (e4: P3); begruenden
  v2 → P4, v3 → P6; eine anwendung je Einheit → P8.
"""
import json
import math
import sys

B = 'bank/binomialverteilung/'
E = 'binomialverteilung'
QMAP = {125: 122, 127: 124, 128: 125, 129: 126, 130: 127, 131: 128}

VOR = {
    1: ("„Bernoulli oder nicht?“ – zu Aufgabentexten ankreuzen: zwei "
        "Ausgänge? feste Anzahl? p bei jedem Versuch gleich (mit "
        "Zurücklegen oder sehr große Gesamtheit)? unabhängig? – und bei "
        "„nein“ die verletzte Bedingung nennen; nichts rechnen"),
    2: ("„Genau, höchstens oder mindestens?“ – zu Ereignissen die Grenze "
        "ankreuzen: genau k als Einzelwahrscheinlichkeit; höchstens, "
        "weniger als, mindestens, mehr als kumuliert, mit der richtigen "
        "ganzen Zahl k und mit oder ohne Gegenereignis; nichts rechnen"),
    4: ("„Was ist gesucht?“ – zu Aufgaben ankreuzen, ob eine "
        "Wahrscheinlichkeit gesucht ist oder n, p oder k, und welcher Weg "
        "passt: Logarithmus (Mindestanzahl bei „mindestens einmal“), "
        "Wurzel (p bei „kein Treffer“), Probieren mit Nachbarwerten am "
        "Rechner (Grenze k, Umgebung, n bei „mehr als k Treffern“); "
        "nichts rechnen"),
}
VOR[3] = VOR[2]
ERK = ("„Treffer oder Niete gezählt?“ – bei Summentermen und Diagrammen "
       "ankreuzen, ob p den Treffer oder die Niete des Sachzusammenhangs "
       "meint und ob X oder n − X gezählt wird; nichts rechnen")
E2_S2 = ("die ganze Verteilung für kleines n: alle Einzelwahrscheinlichkeiten "
         "P(X = k) von k gleich null bis k gleich n der Reihe nach, "
         "Kontrolle: die Summe ist eins")


def lade(f):
    return [json.loads(l) for l in open(B + f + '.jsonl', encoding='utf-8')]


def schreibe(f, rows):
    with open(B + f + '.jsonl', 'w', encoding='utf-8', newline='\n') as h:
        for r in rows:
            h.write(json.dumps(r, ensure_ascii=False) + '\n')


def kz(x, d):
    """Dezimalzahl mit {,} und d Stellen."""
    s = f"{x:.{d}f}"
    return s.replace('.', '{,}')


def pdf(n, p, k):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def neu_id(r):
    r['id'] = (f"{E}-e{r['einheit']}-k{r['kette_nr']}-s{r['sprosse']}"
               f"-v{r['variante']}")
    return r


def zeile(vorlage, **kw):
    """Neue Zeile in der Feldfolge der Bank."""
    felder = ['id', 'eintrag', 'einheit', 'kette', 'kette_nr', 'sprosse',
              'sprosse_text', 'merkmal', 'hoehe', 'pflicht', 'variante',
              'aufgabe', 'form', 'antwort', 'loesung', 'pruef', 'original',
              'grafik', 'loesungsgrafik', 'quelle']
    r = dict(vorlage)
    r.update(kw)
    if r.get('hoehe') != 'pflicht':
        r.pop('pflicht', None)
    out = {k: r[k] for k in felder if k in r}
    return out


def ersetze(rows, suffix, **kw):
    """Zeile mit id-Ende suffix umschreiben (Felder aus kw)."""
    for i, r in enumerate(rows):
        if r['id'].endswith(suffix):
            rows[i] = zeile(r, **kw)
            return
    raise KeyError(suffix)


def grundfall(rows, einheit, kette_nr, varianten):
    """Die fünf Grundfallzeilen durch das Päckchen ersetzen."""
    alt = [r for r in rows if r['hoehe'] == 'grundfall']
    assert len(alt) == 5
    for r, v in zip(alt, varianten):
        i = rows.index(r)
        rows[i] = zeile(r, **v)


def nachziehen(rows):
    for r in rows:
        r['quelle'] = QMAP.get(r['quelle'], r['quelle'])
        if r['hoehe'] == 'vorstufe' and r['einheit'] in VOR:
            r['sprosse_text'] = VOR[r['einheit']]


# --- Einheit 1 -----------------------------------------------------------

def e1():
    rows = lade('e1')
    nachziehen(rows)
    ersetze(rows, 'k2-s1-v2',
            aufgabe=("Ein Glücksrad zeigt Gelb mit der Wahrscheinlichkeit "
                     "$0{,}15$ und wird zweimal gedreht. Tim berechnet die "
                     "Wahrscheinlichkeit für genau einmal Gelb: "
                     "\\rechnung{P &= 2 \\cdot 0{,}15 \\cdot 0{,}85 = 0{,}255} "
                     "Prüfe, ob Tim richtig gerechnet hat."),
            loesung=("Richtig. Genau ein Treffer bei zwei Versuchen hat "
                     "zwei Pfade, erst Gelb oder erst nicht Gelb, mit "
                     "derselben Wahrscheinlichkeit – deshalb steht der "
                     "Faktor 2 vor dem Produkt."),
            pruef="")
    ersetze(rows, 'k2-s1-v3',
            aufgabe=("Ein Glücksrad zeigt Rot mit der Wahrscheinlichkeit "
                     "$0{,}4$ und wird zweimal gedreht. Vier Schüler geben "
                     "die Wahrscheinlichkeit für genau einmal Rot an: "
                     "$0{,}48$; $1{,}2$; $-0{,}24$; $0{,}96$. Welche "
                     "Ergebnisse können nicht stimmen? Begründe, ohne "
                     "genau zu rechnen."),
            loesung=("$1{,}2$: größer als eins, keine Wahrscheinlichkeit; "
                     "$-0{,}24$: negativ, keine Wahrscheinlichkeit; "
                     "$0{,}96$: für keinmal und zweimal Rot bliebe nur "
                     "$0{,}04$, aber schon zweimal nicht Rot hat "
                     "$0{,}6 \\cdot 0{,}6 = 0{,}36$. $0{,}48$ kann stimmen."),
            pruef="")
    ersetze(rows, 'k2-s2-v2',
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                     "falsch ist. Begründe. (1) Jedes Zufallsexperiment mit "
                     "genau zwei Ausgängen ist ein Bernoulli-Experiment. "
                     "(2) Zieht man immer mit Zurücklegen, bleibt die "
                     "Trefferwahrscheinlichkeit bei jedem Zug gleich. "
                     "(3) Eine Bernoulli-Kette hat nie mehr als zwei "
                     "Versuche."),
            loesung=("(1) wahr, denn ein Bernoulli-Experiment ist genau ein "
                     "Zufallsexperiment mit zwei Ausgängen; (2) wahr, denn "
                     "vor jedem Zug liegt derselbe Inhalt in der Urne; "
                     "(3) falsch, z. B. zehn Münzwürfe sind eine "
                     "Bernoulli-Kette der Länge zehn."),
            pruef="")
    ersetze(rows, 'k2-s2-v3',
            aufgabe=("Paul sagt: „Beim Elfmeter gibt es Tor, gehalten oder "
                     "vorbei. Zählt man bei zehn Schüssen nur die Tore, ist "
                     "das trotzdem eine Bernoulli-Kette, wenn der Schütze "
                     "immer gleich sicher und unabhängig schießt.“ "
                     "Begründe, ohne zu rechnen, ob Paul recht hat."),
            loesung=("Ja; mit dem Treffer „Tor“ und der Niete „kein Tor“ "
                     "hat jeder Schuss genau zwei Ausgänge, und bei gleicher "
                     "Trefferwahrscheinlichkeit und Unabhängigkeit liegt "
                     "eine Bernoulli-Kette vor."),
            pruef="")
    ersetze(rows, 'k2-s3-v3',
            aufgabe=("5\\,\\% der Schrauben einer großen Tagesproduktion "
                     "sind fehlerhaft. Ein Kunde prüft drei zufällig "
                     "entnommene Schrauben und nimmt die Lieferung an, wenn "
                     "höchstens eine fehlerhaft ist. Er will, dass eine "
                     "solche Lieferung mit mindestens 99,5\\,\\% "
                     "Wahrscheinlichkeit angenommen wird. Reicht das?"),
            loesung=("Nein; keine fehlerhaft: $0{,}95^3 \\approx 0{,}8574$; "
                     "genau eine fehlerhaft: $3 \\cdot 0{,}05 \\cdot "
                     "0{,}95^2 \\approx 0{,}1354$; addieren: "
                     "$P \\approx 0{,}9928$; Vergleich: "
                     "$0{,}9928 < 0{,}995$, die Forderung ist nicht "
                     "erfüllt."),
            pruef="0.95**3+3*0.05*0.95**2")
    return rows


# --- Einheit 2 -----------------------------------------------------------

def e2():
    rows = lade('e2')
    nachziehen(rows)
    # Päckchen: n = 6, p = 0,4 fest, k wandert
    pk = []
    for v, k in enumerate([2, 1, 4, 3, 5], 1):
        pk.append(dict(
            merkmal=("Term aufstellen: Anordnungen, Potenz der Treffer, "
                     "Potenz der Nieten; n und p bleiben, k wandert"),
            aufgabe=("Ein Glücksrad bleibt mit der Wahrscheinlichkeit "
                     "$0{,}4$ auf Blau stehen und wird 6-mal gedreht; X ist "
                     "die Anzahl der Drehungen mit Blau. Gib den Term für "
                     f"$P(X = {k})$ an, ohne ihn auszurechnen."),
            form="teil", antwort=f"P(X = {k}) = __",
            loesung=(f"Anordnungen: $(6 \\text{{ über }} {k}) = "
                     f"{math.comb(6, k)}$, so viele Pfade haben {k} "
                     f"Treffer; Treffer: $0{{,}}4^{{{k}}}$; Nieten: "
                     f"$0{{,}}6^{{{6 - k}}}$; Term: $P(X = {k}) = "
                     f"(6 \\text{{ über }} {k}) \\cdot 0{{,}}4^{{{k}}} "
                     f"\\cdot 0{{,}}6^{{{6 - k}}}$"),
            pruef=f"math.comb(6,{k})"))
    grundfall(rows, 2, 1, pk)
    # neue Sprosse 2; alte Sprossen ab 2 rücken
    for r in rows:
        if r['kette_nr'] == 1 and r['sprosse'] >= 2:
            r['sprosse'] += 1
    vor = next(r for r in rows if r['hoehe'] == 'grundfall')
    neu = []
    faelle = [
        (3, 0.2, "Ein Basketballspieler trifft von der Mittellinie mit der "
                 "Wahrscheinlichkeit $0{,}2$ und wirft dreimal; X ist die "
                 "Anzahl seiner Treffer."),
        (4, 0.1, "Ein Keimling geht mit der Wahrscheinlichkeit $0{,}1$ "
                 "ein. Vier Keimlinge werden gepflanzt; X ist die Anzahl "
                 "der eingegangenen."),
        (3, 0.4, "Eine Ampel zeigt bei Ankunft mit der Wahrscheinlichkeit "
                 "$0{,}4$ Grün. Lena kommt an drei solchen Ampeln vorbei; "
                 "X ist die Anzahl der grünen."),
    ]
    for v, (n, p, text) in enumerate(faelle, 1):
        q = round(1 - p, 1)
        werte = [pdf(n, p, k) for k in range(n + 1)]
        d = 4
        teile = []
        for k in range(n + 1):
            c = math.comb(n, k)
            fak = "" if c == 1 else f"{c} \\cdot "
            pt = "" if k == 0 else (f"{kz(p, 1)}" if k == 1
                                    else f"{kz(p, 1)}^{k}")
            qt = "" if n - k == 0 else (f"{kz(q, 1)}" if n - k == 1
                                        else f"{kz(q, 1)}^{n - k}")
            prod = " \\cdot ".join(x for x in (pt, qt) if x)
            teile.append(f"$k = {k}$: ${fak}{prod} = {kz(werte[k], d)}$")
        summe = " + ".join(kz(w, d) for w in werte)
        neu.append(zeile(
            vor, sprosse=2, sprosse_text=E2_S2, hoehe='sprosse',
            merkmal=("alle Werte von k der Reihe nach, mit der Summe als "
                     "Kontrolle"),
            variante=v,
            aufgabe=(text + f" Berechne $P(X = k)$ für alle k von 0 bis "
                     f"{n} und kontrolliere mit der Summe."),
            form='teil',
            antwort=", ".join(f"P(X = {k}) = __" for k in range(n + 1)),
            loesung="; ".join(teile) + f"; Kontrolle: ${summe} = 1$",
            pruef=f"[{', '.join(repr(round(w, 4)) for w in werte)}]",
            original=None, grafik="", loesungsgrafik="", quelle=125))
    i = max(j for j, r in enumerate(rows) if r['hoehe'] == 'grundfall')
    rows[i + 1:i + 1] = neu
    # Pflicht
    ersetze(rows, 'k2-s1-v2',
            aufgabe=("Ein Glücksrad zeigt Gold mit der Wahrscheinlichkeit "
                     "$0{,}35$ und wird 8-mal gedreht. Lea rechnet für genau "
                     "dreimal Gold: \\rechnung{P &= (8 \\text{ über } 3) "
                     "\\cdot 0{,}35^3 \\cdot 0{,}65^5 \\approx 0{,}2786} "
                     "Prüfe, ob Lea richtig gerechnet hat."),
            loesung=("Richtig. Zu den 3 Treffern gehört der Exponent 3 bei "
                     "$0{,}35$, zu den 5 Nieten der Exponent 5 bei "
                     "$0{,}65$, und $(8 \\text{ über } 3)$ zählt die "
                     "Anordnungen."),
            pruef="")
    ersetze(rows, 'k2-s1-v3',
            aufgabe=("Ein Glücksrad zeigt Rot mit der Wahrscheinlichkeit "
                     "$0{,}2$ und wird 6-mal gedreht; X zählt Rot. Vier "
                     "Schüler nennen Werte: $P(X = 2) \\approx 1{,}25$; "
                     "$P(X = 6) \\approx 0{,}2$; $P(X = 1) \\approx "
                     "-0{,}39$; $P(X = 0) \\approx 0{,}26$. Welche Ergebnisse "
                     "können nicht stimmen? Begründe, ohne genau zu "
                     "rechnen."),
            loesung=("$1{,}25$ bei $P(X = 2)$: größer als eins, keine "
                     "Wahrscheinlichkeit; $0{,}2$ bei $P(X = 6)$: sechs "
                     "Treffer hintereinander sind viel unwahrscheinlicher "
                     "als einer, der Wert liegt weit unter $0{,}2$; "
                     "$-0{,}39$ bei $P(X = 1)$: negativ, keine "
                     "Wahrscheinlichkeit. $0{,}26$ kann stimmen."),
            pruef="")
    ersetze(rows, 'k2-s2-v2',
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                     "falsch ist. Begründe. (1) Jeder Pfad mit genau k "
                     "Treffern hat dieselbe Wahrscheinlichkeit. (2) Der "
                     "Binomialkoeffizient $(n \\text{ über } k)$ ist immer "
                     "größer als eins. (3) Für „kein Treffer“ braucht man "
                     "nie einen Binomialkoeffizienten."),
            loesung=("(1) wahr, denn jeder dieser Pfade hat k Faktoren p "
                     "und n − k Faktoren 1 − p, nur in anderer "
                     "Reihenfolge; (2) falsch, z. B. "
                     "$(7 \\text{ über } 7) = 1$; (3) wahr, denn es gibt "
                     "nur einen Pfad ohne Treffer, "
                     "$(n \\text{ über } 0) = 1$."),
            pruef="")
    ersetze(rows, 'k2-s2-v3',
            aufgabe=("Jana sagt: „Die Wahrscheinlichkeit für genau eine "
                     "Sechs bei drei Würfen ist $\\frac{1}{6} \\cdot "
                     "\\left(\\frac{5}{6}\\right)^2$.“ Begründe, ohne zu "
                     "rechnen, ob Jana recht hat."),
            loesung=("Nein; das ist nur der Pfad mit der Sechs im ersten "
                     "Wurf. Die Sechs kann in jedem der drei Würfe fallen, "
                     "die Anordnungen fehlen: richtig ist "
                     "$(3 \\text{ über } 1) \\cdot \\frac{1}{6} \\cdot "
                     "\\left(\\frac{5}{6}\\right)^2$."),
            pruef="")
    ersetze(rows, 'k2-s3-v2',
            aufgabe=("Ein Quiz hat 10 Fragen mit je drei Antworten, eine "
                     "davon richtig. Wer mindestens 8 richtig hat, gewinnt. "
                     "Mila will nur mitmachen, wenn ihre Gewinnchance beim "
                     "reinen Raten mindestens 1\\,\\% beträgt. Macht sie "
                     "mit?"),
            loesung=("Nein; Treffer: richtige Antwort mit $p = "
                     "\\frac{1}{3}$; addieren: $P(X = 8) + P(X = 9) + "
                     "P(X = 10) \\approx 0{,}0034$; Vergleich: "
                     "$0{,}0034 < 0{,}01$, Raten bringt fast nie den "
                     "Gewinn."),
            pruef=("math.comb(10,8)*(1/3)**8*(2/3)**2+math.comb(10,9)*"
                   "(1/3)**9*(2/3)+(1/3)**10"))
    for r in rows:
        neu_id(r)
    return rows


# --- Einheit 3 -----------------------------------------------------------

def e3():
    rows = lade('e3')
    nachziehen(rows)
    for r in rows:
        r['kette_nr'] += 1
    # Päckchen: n = 40 und die Zahl 12 fest, das Wort wandert
    faelle = [
        ("höchstens 12 Treffer", "Bedingung: $X \\le 12$",
         "$P(X \\le 12)$", 12),
        ("weniger als 12 Treffer",
         "Bedingung: $X < 12$; ganze Zahl: $X \\le 11$",
         "$P(X \\le 11)$", 11),
        ("mindestens 12 Treffer",
         "Bedingung: $X \\ge 12$; Gegenereignis: $X \\le 11$",
         "$1 - P(X \\le 11)$", 11),
        ("mehr als 12 Treffer",
         "Bedingung: $X > 12$; Gegenereignis: $X \\le 12$",
         "$1 - P(X \\le 12)$", 12),
        ("nicht weniger als 12 Treffer",
         "Bedingung: $X \\ge 12$; Gegenereignis: $X \\le 11$",
         "$1 - P(X \\le 11)$", 11),
    ]
    pk = []
    for wort, schritte, ansatz, k in faelle:
        pk.append(dict(
            merkmal=("Wortlaut in eine kumulierte Wahrscheinlichkeit "
                     "übersetzen; n und die Zahl bleiben, das Wort wandert"),
            aufgabe=("Ein Glücksrad wird 40-mal gedreht; X ist die Anzahl "
                     f"der Treffer. Übersetze „{wort}“ in einen Ansatz mit "
                     "$P(X \\le \\ldots)$."),
            form="teil", antwort="P = __",
            loesung=f"{schritte}; Ansatz: {ansatz}; Ergebnis: Grenze $k = {k}$",
            pruef=str(k)))
    grundfall(rows, 3, 2, pk)
    # Erkennungsschritt als k1
    vor = next(r for r in rows if r['hoehe'] == 'vorstufe')
    erk = []
    daten = [
        ("90\\,\\% der Fahrgäste eines Zuges haben einen gültigen "
         "Fahrschein. Kontrolliert werden 40 Fahrgäste. Zu einem Ereignis "
         "gehört der Term $\\Sigma_{k=0}^{3}\\, (40 \\text{ über } k) "
         "\\cdot 0{,}1^k \\cdot 0{,}9^{40-k}$. Was zählt k? \\\\ "
         "\\kreuz{Fahrgäste mit Fahrschein} \\\\ \\kreuz{Fahrgäste ohne "
         "Fahrschein}",
         "Fahrgäste ohne Fahrschein – k steht als Exponent bei $0{,}1$, "
         "dem Anteil ohne Fahrschein", ""),
        ("Ein Basketballspieler trifft einen Freiwurf mit 75\\,\\%. Zu 20 "
         "Freiwürfen rechnet Can mit $P(X \\le 4)$ und der "
         "Wahrscheinlichkeit $0{,}25$. Was zählt sein X? \\\\ "
         "\\kreuz{Treffer} \\\\ \\kreuz{Fehlwürfe}",
         "Fehlwürfe – $0{,}25$ ist die Wahrscheinlichkeit für einen "
         "Fehlwurf", ""),
        ("Von einer Samensorte keimen 80\\,\\%. Zu 30 Samen rechnet Ina "
         "mit der Wahrscheinlichkeit $0{,}2$. Was zählt ihr X? \\\\ "
         "\\kreuz{gekeimte Samen} \\\\ \\kreuz{nicht gekeimte Samen}",
         "nicht gekeimte Samen – $0{,}2$ ist der Anteil, der nicht keimt",
         ""),
        ("65\\,\\% der Kunden eines Ladens zahlen mit Karte. Das "
         "Stabdiagramm zeigt die Verteilung einer Anzahl X unter 15 "
         "zufällig ausgewählten Kunden. Zählt X die Kartenzahler oder die "
         "Barzahler? \\\\ \\kreuz{Kartenzahler} \\\\ \\kreuz{Barzahler}",
         "Barzahler – die höchste Säule liegt bei 5, der Erwartungswert "
         "der Kartenzahler wäre fast 10",
         "\\binomialverteilung{15}{0.35}"),
    ]
    for v, (auf, loe, gr) in enumerate(daten, 1):
        erk.append(zeile(
            vor, kette="Treffer oder Niete gezählt?", kette_nr=1,
            sprosse=0, sprosse_text=ERK, hoehe='vorstufe', variante=v,
            merkmal=("entscheiden, ob Treffer oder Nieten gezählt werden, "
                     "ohne zu rechnen"),
            aufgabe=auf, form='ankreuzen', antwort='', loesung=loe,
            pruef='', original=None, grafik=gr, loesungsgrafik='',
            quelle=43))
    rows[0:0] = erk
    # Pflicht (alte ids k4, neue k5)
    ersetze(rows, 'k4-s1-v2',
            aufgabe=("3\\,\\% der Tassen einer Serie haben einen Sprung; X "
                     "ist die Anzahl solcher Tassen unter 200. Tina rechnet "
                     "für „mindestens 5\\,\\% der Tassen haben einen "
                     "Sprung“: \\rechnung{5\\,\\% \\text{ von } 200 &= 10 "
                     "\\\\ P(X \\ge 10) &= 1 - P(X \\le 9) \\approx "
                     "0{,}0808} Prüfe, ob Tina richtig gerechnet hat."),
            loesung=("Richtig. Der Anteil wird zuerst in eine Anzahl "
                     "übersetzt, 10 von 200, und „mindestens 10“ läuft über "
                     "das Gegenereignis „höchstens 9“."),
            pruef="")
    ersetze(rows, 'k4-s1-v3',
            aufgabe=("X ist binomialverteilt mit 30 Versuchen und der "
                     "Trefferwahrscheinlichkeit $0{,}35$. Vier Schüler "
                     "nennen: $P(X \\le 11) \\approx 0{,}6548$; "
                     "$P(X \\le 12) \\approx 0{,}5078$; $P(X \\ge 12) "
                     "\\approx 0{,}6548$; $P(X \\le 30) \\approx 0{,}98$. "
                     "Welche Ergebnisse können nicht stimmen? Begründe, "
                     "ohne genau zu rechnen."),
            loesung=("$0{,}5078$ bei $P(X \\le 12)$: mit größerer Grenze "
                     "kann die kumulierte Wahrscheinlichkeit nicht kleiner "
                     "werden als $P(X \\le 11)$; $0{,}6548$ bei "
                     "$P(X \\ge 12)$: zusammen mit $P(X \\le 11)$ muss 1 "
                     "herauskommen, zweimal $0{,}6548$ ist mehr; $0{,}98$ "
                     "bei $P(X \\le 30)$: X ist nie größer als 30, der Wert "
                     "ist 1. $P(X \\le 11) \\approx 0{,}6548$ kann "
                     "stimmen."),
            pruef="")
    ersetze(rows, 'k4-s2-v2',
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                     "falsch ist. Begründe. (1) Für eine Anzahl X sind "
                     "$P(X < k)$ und $P(X \\le k - 1)$ immer gleich. "
                     "(2) „Mehr als k“ und „mindestens k“ beschreiben immer "
                     "dasselbe Ereignis. (3) Es gibt ein k, für das "
                     "$P(X \\le k) = 1$ ist."),
            loesung=("(1) wahr, denn X nimmt nur ganze Zahlen an; "
                     "(2) falsch, z. B. gehört X = k zu „mindestens k“, "
                     "aber nicht zu „mehr als k“; (3) wahr, denn für k = n "
                     "sind alle möglichen Werte erfasst."),
            pruef="")
    ersetze(rows, 'k4-s2-v3',
            aufgabe=("Jonas sagt: „Mehr als 25\\,\\% von 60 Losen heißt "
                     "mindestens 15 Gewinne.“ Begründe, ohne den Rechner "
                     "zu benutzen, ob Jonas recht hat."),
            loesung=("Nein; 25\\,\\% von 60 sind 15, und „mehr als 15“ "
                     "beginnt erst bei 16, also X ≥ 16."),
            pruef="")
    ersetze(rows, 'k4-s3-v1',
            aufgabe=("Ein Hotel hat 120 Zimmer und nimmt 125 Buchungen an, "
                     "weil 6\\,\\% der Buchungen kurzfristig storniert "
                     "werden. Der Hotelchef nimmt so viele Buchungen nur an, "
                     "wenn die Zimmer mit mindestens 85\\,\\% "
                     "Wahrscheinlichkeit reichen. Darf er 125 Buchungen "
                     "annehmen?"),
            loesung=("Ja; Bedingung: mindestens 5 Stornos; Gegenereignis: "
                     "höchstens 4 Stornos; Rechner: $1 - P(X \\le 4) "
                     "\\approx 0{,}8757$; Vergleich: $0{,}8757 \\ge 0{,}85$ "
                     "(X: Anzahl der Stornos)."),
            pruef="1-(" + "+".join(
                f"math.comb(125,{k})*0.06**{k}*0.94**{125 - k}"
                for k in range(5)) + ")")
    for r in rows:
        neu_id(r)
    return rows


# --- Einheit 4 -----------------------------------------------------------

def e4():
    rows = lade('e4')
    nachziehen(rows)
    pk = []
    for s in ["0{,}9", "0{,}5", "0{,}95", "0{,}75", "0{,}99"]:
        proz = {"0{,}9": "90", "0{,}5": "50", "0{,}95": "95",
                "0{,}75": "75", "0{,}99": "99"}[s]
        pk.append(dict(
            merkmal=("Ungleichung mit dem Gegenereignis aufstellen, noch "
                     "nicht lösen; p bleibt, die Schranke wandert"),
            aufgabe=("In 8\\,\\% der Überraschungseier einer Sorte steckt "
                     "eine Sonderfigur. Stelle den Ansatz auf: Wie viele "
                     "Eier muss man öffnen, damit mit mindestens "
                     f"{proz}\\,\\% Wahrscheinlichkeit mindestens eine "
                     "Sonderfigur dabei ist?"),
            form="teil", antwort="1 − __^n ≥ __",
            loesung=("Gegenereignis: keine Sonderfigur, $P = 0{,}92^n$; "
                     f"Ansatz: $1 - 0{{,}}92^n \\ge {s}$"),
            pruef="0.92"))
    grundfall(rows, 4, 1, pk)
    ersetze(rows, 'k3-s1-v2',
            aufgabe=("Für $0{,}9^n \\le 0{,}15$ rechnet Mira: "
                     "\\rechnung{n \\cdot \\mathrm{ln}\\, 0{,}9 &\\le "
                     "\\mathrm{ln}\\, 0{,}15 \\\\ n &\\ge "
                     "\\frac{\\mathrm{ln}\\, 0{,}15}{\\mathrm{ln}\\, 0{,}9} "
                     "\\approx 18{,}006} Sie gibt als kleinste Anzahl "
                     "$n = 19$ an. Prüfe, ob Mira richtig gerechnet hat."),
            loesung=("Richtig. Beim Teilen durch den negativen Logarithmus "
                     "$\\mathrm{ln}\\, 0{,}9$ dreht sich das Zeichen, und n "
                     "wird aufgerundet, weil 18 knapp unter $18{,}006$ "
                     "liegt und die Ungleichung nicht erfüllt."),
            pruef="")
    ersetze(rows, 'k3-s1-v3',
            aufgabe=("Lea löst eine Ungleichung schrittweise: "
                     "\\rechnung{1 - 0{,}9^n &\\ge 0{,}88 \\\\ 0{,}9^n "
                     "&\\ge 0{,}12 \\\\ n \\cdot \\mathrm{ln}\\, 0{,}9 &\\ge "
                     "\\mathrm{ln}\\, 0{,}12 \\\\ n &\\le 20{,}12} Setze "
                     "$n = 30$ ein. In welcher Zeile stimmt es nicht mehr?"),
            loesung=("Fehler in Zeile 2: beim Umstellen von "
                     "$1 - 0{,}9^n \\ge 0{,}88$ wird mit −1 multipliziert, "
                     "das Zeichen muss sich drehen – für $n = 30$ gilt "
                     "Zeile 1 ($0{,}958 \\ge 0{,}88$), Zeile 2 nicht "
                     "($0{,}042 \\ge 0{,}12$ ist falsch). Richtig ist "
                     "$0{,}9^n \\le 0{,}12$, also $n \\ge 20{,}12$ und "
                     "$n = 21$."),
            pruef="")
    ersetze(rows, 'k3-s2-v2',
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                     "falsch ist. Begründe. (1) Für $0 < p < 1$ wird "
                     "$(1 - p)^n$ mit wachsendem n immer kleiner. "
                     "(2) Verdoppelt man n, halbiert sich $(1 - p)^n$ "
                     "immer. (3) Jede Schranke unter 1 erreicht man für "
                     "„mindestens ein Treffer“ mit genügend vielen "
                     "Versuchen."),
            loesung=("(1) wahr, denn jeder weitere Faktor $1 - p$ liegt "
                     "unter eins; (2) falsch, z. B. $0{,}8^1 = 0{,}8$, "
                     "aber $0{,}8^2 = 0{,}64$ statt $0{,}4$; (3) wahr, denn "
                     "$(1 - p)^n$ wird beliebig klein, "
                     "$1 - (1 - p)^n$ kommt beliebig nahe an 1."),
            pruef="")
    ersetze(rows, 'k3-s2-v3',
            aufgabe=("Ben löst $1 - 0{,}94^n \\ge 0{,}8$ und erhält "
                     "$n \\ge 26{,}01$. Ben sagt: „Die kleinste Anzahl ist "
                     "26, weil 26,01 fast 26 ist.“ Begründe, ohne genau zu "
                     "rechnen, ob Ben recht hat."),
            loesung=("Nein; 26 ist kleiner als 26,01 und erfüllt die "
                     "Ungleichung nicht, die kleinste ganze Zahl darüber "
                     "ist 27."),
            pruef="")
    ersetze(rows, 'k3-s3-v1',
            aufgabe=("Ein Raum hat drei Rauchmelder; jeder schlägt bei "
                     "Rauch unabhängig von den anderen mit der "
                     "Wahrscheinlichkeit $0{,}9$ an. Die Versicherung "
                     "verlangt, dass bei Rauch mit mindestens 99,9\\,\\% "
                     "Wahrscheinlichkeit mindestens einer anschlägt. "
                     "Reichen drei Melder?"),
            loesung=("Ja; Gegenereignis: keiner schlägt an, "
                     "$0{,}1^3 = 0{,}001$; mindestens einer: "
                     "$1 - 0{,}001 = 0{,}999$; Vergleich: "
                     "$0{,}999 \\ge 0{,}999$, die Forderung ist genau "
                     "erfüllt."),
            pruef="1-0.1**3")
    for r in rows:
        neu_id(r)
    return rows


# --- Einheit 5 -----------------------------------------------------------

def e5():
    rows = lade('e5')
    nachziehen(rows)
    gr = ("\\saeulenab[ymax=30,ystep=5,yfein=1,ylabel={$P(X = k)$ in "
          "\\%}]{0/3,1/14,2/26,3/28,4/19,5/8,6/2,7/0,8/0}")
    h = [3, 14, 26, 28, 19, 8, 2, 0, 0]
    kopf = ("Das Säulendiagramm zeigt die Verteilung der Anzahl X der "
            "Treffer bei 8 Versuchen (Werte gerundet). ")
    pk = []
    for a, b in [(2, 2), (1, 2), (4, 4), (3, 4), (4, 6)]:
        if a == b:
            auf = kopf + f"Lies $P(X = {a})$ ab."
            loe = f"$P(X = {a}) \\approx {h[a]}\\,\\%$"
            wert = h[a]
        else:
            ks = list(range(a, b + 1))
            auf = (kopf + "Mit welcher Wahrscheinlichkeit liegt X "
                   f"zwischen {a} und {b}, beide eingeschlossen?")
            wert = sum(h[k] for k in ks)
            loe = ("ablesen: " + ", ".join(
                f"$P(X = {k}) \\approx {h[k]}\\,\\%$" for k in ks)
                + "; addieren: $" + " + ".join(f"{h[k]}\\,\\%" for k in ks)
                + f" = {wert}\\,\\%$; Ergebnis: $P({a} \\le X \\le {b}) "
                f"\\approx {wert}\\,\\%$")
        pk.append(dict(
            merkmal=("am Säulendiagramm ablesen und benachbarte Säulen "
                     "addieren; das Diagramm bleibt, das Ereignis wandert"),
            aufgabe=auf, form="teil", antwort="__ %", loesung=loe,
            pruef=str(wert), grafik=gr))
    grundfall(rows, 5, 1, pk)
    ersetze(rows, 'k3-s1-v2',
            aufgabe=("Ein Diagramm zeigt die Verteilung von X bei 12 "
                     "Versuchen. $Y = 12 - X$ zählt die Nieten. Für $P(Y = 3)$ "
                     "nimmt Svenja die Höhe der Säule von X bei 9. Prüfe, "
                     "ob Svenja richtig gedacht hat."),
            loesung=("Richtig. Drei Nieten bei 12 Versuchen heißen neun "
                     "Treffer, also ist $P(Y = 3) = P(X = 12 - 3) = "
                     "P(X = 9)$."),
            pruef="")
    ersetze(rows, 'k3-s1-v3',
            aufgabe=("X ist binomialverteilt mit 24 Versuchen und der "
                     "Trefferwahrscheinlichkeit $0{,}25$. Vier Schüler "
                     "nennen die Stelle der höchsten Säule: 6; 12; 25; 18. "
                     "Welche Ergebnisse können nicht stimmen? Begründe, "
                     "ohne genau zu rechnen."),
            loesung=("12: das ist die Mitte, das Maximum liegt aber beim "
                     "Erwartungswert $24 \\cdot 0{,}25 = 6$; 25: X ist "
                     "höchstens 24; 18: das ist der Erwartungswert der "
                     "Nieten, nicht der Treffer. 6 kann stimmen."),
            pruef="")
    ersetze(rows, 'k3-s2-v2',
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                     "falsch ist. Begründe. (1) Ist der Erwartungswert "
                     "ganzzahlig, liegt die höchste Säule immer bei ihm. "
                     "(2) Das Diagramm einer Binomialverteilung ist immer "
                     "symmetrisch. (3) Alle Säulen zusammen ergeben nie "
                     "mehr als 1."),
            loesung=("(1) wahr, denn bei ganzzahligem Erwartungswert "
                     "$n \\cdot p$ ist er der Modalwert; (2) falsch, z. B. "
                     "liegt bei 10 Versuchen und $p = 0{,}2$ die höchste "
                     "Säule bei 2, rechts folgt ein langer Ausläufer; "
                     "(3) wahr, denn alle Säulen zusammen ergeben genau 1."),
            pruef="")
    ersetze(rows, 'k3-s2-v3',
            aufgabe=("Emil sagt: „Bei 30 Versuchen mit der "
                     "Trefferwahrscheinlichkeit $0{,}5$ liegt die höchste "
                     "Säule bei 15.“ Begründe, ohne Wahrscheinlichkeiten "
                     "zu rechnen, ob Emil recht hat."),
            loesung=("Ja; der Erwartungswert $30 \\cdot 0{,}5 = 15$ ist "
                     "ganzzahlig, und dort liegt die höchste Säule."),
            pruef="")
    ersetze(rows, 'k3-s3-v1',
            aufgabe=("Eine Bäckerei backt täglich 200 Brötchen; jedes "
                     "misslingt unabhängig mit 3\\,\\%. Der Bäcker plant "
                     "mit 5 misslungenen Brötchen, weil das die "
                     "wahrscheinlichste Anzahl sei. Stimmt das?"),
            loesung=("Nein; Erwartungswert: $200 \\cdot 0{,}03 = 6$; "
                     "Nachbarwerte: $P(X = 5) \\approx 0{,}1622$, "
                     "$P(X = 6) \\approx 0{,}1631$; Ergebnis: 6 ist am "
                     "wahrscheinlichsten, knapp vor 5."),
            pruef="6")
    for r in rows:
        neu_id(r)
    return rows


if __name__ == '__main__':
    f = sys.argv[1]
    schreibe(f, {'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5}[f]())

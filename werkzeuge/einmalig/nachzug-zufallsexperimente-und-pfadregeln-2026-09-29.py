"""Nachzug bank/zufallsexperimente-und-pfadregeln auf Katalog 2a296e5
(Mappe 29.09.) und bank.md fünfte Fassung (29b), Vorlage 29e.

Einmalig, 2026-09-29. Aufruf aus der Repo-Wurzel:
    python3 werkzeuge/einmalig/nachzug-zufallsexperimente-und-pfadregeln-2026-09-29.py e1 … e8
Liest den Bestand vom 27.09. (Katalog 95b0f8b), zieht quelle
(161–168 -> 155–162), sprosse, id und sprosse_text nach (Vorstufen und
Prüfungshöhen mit längerem Katalogtext, Pflichtzeilen mit einem Typ oder
einer Zeile des Katalogs), schreibt die Päckchen je Verfahrenskette, die
neue Sprosse e3 „Lückenterm“, je eine dritte Zeile an den Prüfungshöhen
ohne Original (e1, e2) und die Pflichtformen P1–P8; schreibt je Einheit
die ganze Datei. Zählt übernommen/neu/umgeschrieben/entfallen (stdout).
Übernommene Zeilen bleiben wortgleich bis auf id, sprosse, kette_nr,
quelle, sprosse_text.
"""
import copy
import json
import re
import sys

E = "zufallsexperimente-und-pfadregeln"
B = f"bank/{E}/"
MAPPE = f"mappen/{E}.md"
QMAP = {161 + i: 155 + i for i in range(8)}
INHALT = ("aufgabe", "form", "antwort", "loesung", "pruef", "original",
          "grafik", "loesungsgrafik", "merkmal", "hoehe")


def katalog():
    zeilen = {}
    for z in open(MAPPE, encoding="utf-8").read().split("\n## 2 ")[0] \
            .split("\n"):
        m = re.match(r"\s*(\d+)  (.*)$", z)
        if m:
            zeilen[int(m.group(1))] = m.group(2)
    return zeilen


KAT = katalog()


def glieder(q):
    """Sprossen der Kette in Zeile q (Trenner „ → “)."""
    return KAT[q].split(" → ")


def vorstufe(q):
    s = glieder(q)[0]
    s = s[s.index("): ") + 3:]
    return s[:s.index("nichts rechnen") + len("nichts rechnen")]


def glied(q, i):
    return glieder(q)[i].rstrip(".")


# Pflichtzeilen: sprosse_text (wortgleich) und quelle je Einheit
ANW = ("Anwendungssituationen mithilfe von Urnenmodellen untersuchen", 6)
DAR = {
    1: ("Symbolschreibweise der Ereignisse", 52),
    2: ("Laplace-Experiment: Urnenmodell zu einer vorgegebenen Verteilung "
        "beschreiben", 33),
    3: ("Baumdiagramm zweistufig darstellen", 34),
    4: ("Baumdiagramm mehrstufig ohne Zurücklegen darstellen", 35),
    5: ("Lotto-Modell: dieselbe Zahl als „günstige durch mögliche "
        "Auswahlen“", 103),
    6: ("Baumdiagramm zu einer zweistufigen Situation erstellen", 37),
    7: ("Term und Ereignis: Ereignis zu einem gegebenen "
        "Wahrscheinlichkeitsterm beschreiben", 38),
    8: ("die Pfade als Terme bilden und die Bedingung als Gleichung setzen",
        130),
}
M_FEHLER = ("drei Formen: Schülerrechnung mit Fehler, fehlerfreie Vorlage, "
            "Ergebnisse ohne Rechnung verwerfen")
M_FEHLER8 = ("drei Formen: Schülerrechnung mit Fehler, fehlerfreie Vorlage, "
             "Prüfzahl in der Umformung")
M_BEGR = ("drei Formen: Regel begründen, Aussagenserie, Aussage einer "
          "Person beurteilen")


def z(**k):
    """Neue oder umgeschriebene Zeile: Standardfelder."""
    d = {"form": "teil", "antwort": "", "pruef": "", "original": None,
         "grafik": "", "loesungsgrafik": ""}
    d.update(k)
    return d


# --- Päckchen je Verfahrenskette (Grundfall, fünf Zeilen) ---------------

def e1_gf():
    m = "Tupel in Reihenfolge aufschreiben, Laplace-Bedingung prüfen"
    aus = []
    namen = {2: "1, 2", 3: "1, 2, 3", 4: "1, 2, 3, 4", 5: "1, 2, 3, 4, 5",
             6: "1, 2, 3, 4, 5, 6"}
    for n in (2, 3, 4, 5, 6):
        tupel = ", ".join(f"({m_}; {i})" for m_ in "KZ"
                          for i in range(1, n + 1))
        aus.append(z(
            merkmal=m, form="text",
            aufgabe=(f"Eine Münze wird geworfen (K = Kopf, Z = Zahl). "
                     f"Danach wird ein Glücksrad mit {n} gleich großen "
                     f"Sektoren gedreht, sie tragen die Zahlen "
                     f"{namen[n]}. Gib die Ergebnismenge als Tupel an. "
                     f"Prüfe, ob ein Laplace-Experiment vorliegt."),
            loesung=(f"Tupel aufschreiben: {tupel}; Anzahl = {2 * n}; "
                     f"Laplace prüfen: ja, Münze und Sektoren sind gleich "
                     f"wahrscheinlich, also jedes Tupel mit "
                     f"$\\frac{{1}}{{{2 * n}}}$"),
            pruef=str(2 * n)))
    return aus


def e2_gf():
    m = "günstige durch alle abzählen"
    aus = []
    for g, (a, b) in ((6, (1, 10)), (15, (1, 4)), (20, (1, 3)),
                      (24, (2, 5)), (45, (3, 4))):
        aus.append(z(
            merkmal=m, antwort="P = __",
            aufgabe=(f"In einer Lostrommel liegen 60 Lose, {g} davon sind "
                     f"Gewinne. Tom zieht ein Los. Wie groß ist die "
                     f"Wahrscheinlichkeit für einen Gewinn?"),
            loesung=(f"günstige durch alle: $P = \\frac{{{g}}}{{60}}$; "
                     f"kürzen: $P = \\frac{{{a}}}{{{b}}}$"),
            pruef=f"[{a}, {b}]"))
    return aus


def e3_gf():
    m = "Baum mit gleichen Ästen, ein Pfad als Produkt"
    aus = []
    for p, q, r in (("0{,}3", "0{,}7", "0{,}21"), ("0{,}2", "0{,}8",
                                                    "0{,}16"),
                    ("0{,}5", "0{,}5", "0{,}25"), ("0{,}6", "0{,}4",
                                                    "0{,}24"),
                    ("0{,}9", "0{,}1", "0{,}09")):
        pp = p.replace("{,}", ",")
        proz = int(round(float(pp.replace(",", ".")) * 100))
        aus.append(z(
            merkmal=m, form="zeichnen",
            aufgabe=(f"Ein Glücksrad zeigt Rot (R) mit {proz}\\,\\%, sonst "
                     f"Blau (B). Es wird zweimal gedreht. Beschrifte den "
                     f"Baum. Wie groß ist die Wahrscheinlichkeit für erst "
                     f"Rot, dann Blau?"),
            loesung=(f"Äste beschriften: R ${p}$, B ${q}$ auf beiden "
                     f"Stufen; Pfad multiplizieren: $P = {p} \\cdot {q} = "
                     f"{r}$"),
            pruef=r.replace("{,}", "."),
            grafik="\\baumzwei{R/,B/}{R/,B/}{R/,B/}"))
    return aus


def e4_gf():
    m = "Nenner sinkt um eins, ein Pfad oder zwei Pfade"
    kopf = ("Eine Urne enthält 4 rote und 6 blaue Kugeln. Zwei Kugeln "
            "werden ohne Zurücklegen gezogen. ")
    aus = [
        z(merkmal=m, antwort="P = __",
          aufgabe=kopf + "Wie groß ist die Wahrscheinlichkeit, dass beide "
          "rot sind?",
          loesung=("ein Pfad: $P = \\frac{4}{10} \\cdot \\frac{3}{9}$; "
                   "ausrechnen: $P = \\frac{12}{90} = \\frac{2}{15}$"),
          pruef="[2, 15]"),
        z(merkmal=m, antwort="P = __",
          aufgabe=kopf + "Wie groß ist die Wahrscheinlichkeit, dass beide "
          "blau sind?",
          loesung=("ein Pfad: $P = \\frac{6}{10} \\cdot \\frac{5}{9}$; "
                   "ausrechnen: $P = \\frac{30}{90} = \\frac{1}{3}$"),
          pruef="[1, 3]"),
        z(merkmal=m, antwort="P = __",
          aufgabe=kopf + "Wie groß ist die Wahrscheinlichkeit, dass erst "
          "eine rote und dann eine blaue Kugel kommt?",
          loesung=("ein Pfad: $P = \\frac{4}{10} \\cdot \\frac{6}{9}$; "
                   "ausrechnen: $P = \\frac{24}{90} = \\frac{4}{15}$"),
          pruef="[4, 15]"),
        z(merkmal=m, antwort="P = __",
          aufgabe=kopf + "Wie groß ist die Wahrscheinlichkeit für zwei "
          "verschiedene Farben?",
          loesung=("zwei Pfade: $P = \\frac{4}{10} \\cdot \\frac{6}{9} + "
                   "\\frac{6}{10} \\cdot \\frac{4}{9}$; ausrechnen: $P = "
                   "\\frac{48}{90} = \\frac{8}{15}$"),
          pruef="[8, 15]"),
        z(merkmal=m, antwort="P = __",
          aufgabe=kopf + "Wie groß ist die Wahrscheinlichkeit für zwei "
          "Kugeln derselben Farbe?",
          loesung=("zwei Pfade: $P = \\frac{4}{10} \\cdot \\frac{3}{9} + "
                   "\\frac{6}{10} \\cdot \\frac{5}{9}$; ausrechnen: $P = "
                   "\\frac{42}{90} = \\frac{7}{15}$"),
          pruef="[7, 15]"),
    ]
    return aus


def e5_gf():
    m = "ein Pfad mal drei Positionen"
    aus = []
    # mit Zurücklegen: r rote unter 10
    for r, erg in ((2, "0{,}384"), (3, "0{,}441"), (5, "0{,}375")):
        p = f"0{{,}}{r}"
        q = f"0{{,}}{10 - r}"
        aus.append(z(
            merkmal=m, antwort="P = __",
            aufgabe=(f"Eine Urne enthält 10 Kugeln, {r} davon sind rot. Es "
                     f"wird dreimal mit Zurücklegen gezogen. Wie groß ist "
                     f"die Wahrscheinlichkeit für genau eine rote Kugel?"),
            loesung=(f"ein Pfad: ${p} \\cdot {q}^2$; mal drei Positionen: "
                     f"$P = 3 \\cdot {p} \\cdot {q}^2 = {erg}$"),
            pruef=erg.replace("{,}", ".")))
    for r, (a, b) in ((4, (1, 2)), (3, (21, 40))):
        s = 10 - r
        aus.append(z(
            merkmal=m, antwort="P = __",
            aufgabe=(f"Eine Urne enthält 10 Kugeln, {r} davon sind rot. Es "
                     f"wird dreimal ohne Zurücklegen gezogen. Wie groß ist "
                     f"die Wahrscheinlichkeit für genau eine rote Kugel?"),
            loesung=(f"ein Pfad: $\\frac{{{r}}}{{10}} \\cdot "
                     f"\\frac{{{s}}}{{9}} \\cdot \\frac{{{s - 1}}}{{8}}$; "
                     f"mal drei Positionen: $P = 3 \\cdot "
                     f"\\frac{{{r * s * (s - 1)}}}{{720}} = "
                     f"\\frac{{{a}}}{{{b}}}$"),
            pruef=f"[{a}, {b}]"))
    return aus


def e6_gf():
    m = "Gruppe auf die erste, Merkmal auf die zweite Stufe"
    aus = []
    for k, rest in ((20, "0{,}8"), (10, "0{,}9"), (25, "0{,}75"),
                    (35, "0{,}65"), (15, "0{,}85")):
        kk = f"0{{,}}{k}".rstrip("0")
        aus.append(z(
            merkmal=m, form="zeichnen",
            aufgabe=(f"30\\,\\% der Haushalte eines Orts haben einen Hund "
                     f"(H), die übrigen nicht (N). Unter den Hundehaltern "
                     f"haben 40\\,\\% auch eine Katze (K), unter den "
                     f"übrigen {k}\\,\\%. O heißt ohne Katze. Beschrifte "
                     f"den Baum."),
            loesung=(f"erste Stufe Gruppe: H $0{{,}}3$, N $0{{,}}7$; "
                     f"zweite Stufe unter H: K $0{{,}}4$, O $0{{,}}6$; "
                     f"zweite Stufe unter N: K ${kk}$, O ${rest}$"),
            grafik="\\baumzwei{H/,N/}{K/,O/}{K/,O/}"))
    return aus


def e7_gf():
    m = "Faktoren als Stufen einer festen Ergebnisfolge lesen"
    kopf = ("Eine Münze zeigt Kopf mit $0{,}6$ und Zahl mit $0{,}4$. Sie "
            "wird dreimal geworfen. Welches Ereignis hat die "
            "Wahrscheinlichkeit ")
    aus = []
    for term, erg in (("0{,}6^3", "dreimal Kopf"),
                      ("0{,}4^3", "dreimal Zahl"),
                      ("0{,}6 \\cdot 0{,}4 \\cdot 0{,}6",
                       "Kopf, Zahl, Kopf in dieser Reihenfolge"),
                      ("0{,}6^2 \\cdot 0{,}4",
                       "erst zweimal Kopf, dann Zahl"),
                      ("0{,}4 \\cdot 0{,}6^2",
                       "erst Zahl, dann zweimal Kopf")):
        aus.append(z(merkmal=m, form="text",
                     aufgabe=kopf + f"${term}$?", loesung=erg))
    return aus


def e8_gf():
    m = "Pfadsumme gleich Randwahrscheinlichkeit, linear"
    aus = []
    for ges, rest, a in (("0{,}44", "0{,}14", "0{,}35"),
                         ("0{,}41", "0{,}11", "0{,}275"),
                         ("0{,}5", "0{,}2", "0{,}5"),
                         ("0{,}38", "0{,}08", "0{,}2"),
                         ("0{,}56", "0{,}26", "0{,}65")):
        proz = ges.replace("0{,}", "")
        proz = str(int(proz.ljust(2, "0")))
        aus.append(z(
            merkmal=m, form="gleichungsraster", antwort="a = __",
            aufgabe=(f"60\\,\\% der Kunden eines Geschäfts sind Frauen, "
                     f"unter ihnen sind 50\\,\\% Stammkunden. Insgesamt "
                     f"sind {proz}\\,\\% der Kunden Stammkunden. Wie groß "
                     f"ist der Anteil a der Stammkunden unter den Männern?"),
            loesung=(f"Bedingung Pfadsumme = {ges.replace('{,}', ',')}: "
                     f"$0{{,}}6 \\cdot 0{{,}}5 + 0{{,}}4a = {ges}$; Pfad "
                     f"ausrechnen: $0{{,}}3 + 0{{,}}4a = {ges}$; nach a "
                     f"auflösen: $0{{,}}4a = {rest}$, also $a = {a}$"),
            pruef=a.replace("{,}", ".")))
    return aus


GRUNDFALL = {1: e1_gf, 2: e2_gf, 3: e3_gf, 4: e4_gf, 5: e5_gf, 6: e6_gf,
             7: e7_gf, 8: e8_gf}

# --- neue Sprosse e3 „Lückenterm“ ----------------------------------------

E3_LUECKE = [
    z(merkmal="Basis und Exponent eintragen, noch nicht ausrechnen",
      antwort="P = 1 − (__)^__",
      aufgabe=("Ein Glücksrad zeigt einen Gewinn mit $0{,}2$. Es wird "
               "fünfmal gedreht. Trage Basis und Exponent in den Term für "
               "die Wahrscheinlichkeit von mindestens einem Gewinn ein. "
               "Rechne noch nicht aus."),
      loesung=("Gegenereignis kein Gewinn: Basis $= 1 - 0{,}2 = 0{,}8$; "
               "Exponent $=$ Zahl der Drehungen $= 5$; Ergebnis: $P = 1 - "
               "(0{,}8)^{5}$"),
      pruef="[0.8, 5]"),
    z(merkmal="Basis und Exponent eintragen, noch nicht ausrechnen",
      antwort="P = 1 − (__)^__",
      aufgabe=("Ein Samenkorn keimt mit $0{,}85$. Acht Körner werden "
               "gesät. Trage Basis und Exponent in den Term für die "
               "Wahrscheinlichkeit ein, dass mindestens ein Korn nicht "
               "keimt. Rechne noch nicht aus."),
      loesung=("Gegenereignis alle keimen: Basis $= 0{,}85$; Exponent $=$ "
               "Zahl der Körner $= 8$; Ergebnis: $P = 1 - (0{,}85)^{8}$"),
      pruef="[0.85, 8]"),
    z(merkmal="Basis und Exponent eintragen, noch nicht ausrechnen",
      antwort="P = 1 − (__)^__",
      aufgabe=("Ein Würfel wird zehnmal geworfen. Trage Basis und "
               "Exponent in den Term für die Wahrscheinlichkeit von "
               "mindestens einer Sechs ein. Rechne noch nicht aus."),
      loesung=("Gegenereignis keine Sechs: Basis $= 1 - \\frac{1}{6} = "
               "\\frac{5}{6}$; Exponent $=$ Zahl der Würfe $= 10$; "
               "Ergebnis: $P = 1 - \\left(\\frac{5}{6}\\right)^{10}$"),
      pruef="[5, 6, 10]"),
]

# --- dritte Zeile an Prüfungshöhen ohne Original ------------------------

PRUEF_NEU = {
    1: z(merkmal="Prüfungsform: Termdeutung und Nachweis eines Schnitts",
         form="text",
         aufgabe=("In einer Kantine nehmen 40\\,\\% der Gäste eine Suppe "
                  "(S), 35\\,\\% einen Nachtisch (N) und 45\\,\\% keines "
                  "von beiden. Weise nach, dass 20\\,\\% der Gäste beides "
                  "nehmen. (Abitur 2023 GK)"),
         loesung=("Vereinigung über das Gegenereignis: $P(S \\cup N) = 1 - "
                  "0{,}45 = 0{,}55$; Additionssatz umstellen: $P(S \\cap "
                  "N) = 0{,}4 + 0{,}35 - 0{,}55 = 0{,}2$"),
         pruef="0.2"),
    2: z(merkmal="Prüfungsform: Term in n deuten und Differenz abschätzen",
         form="text",
         aufgabe=("Eine Dose enthält n Knöpfe, 10\\,\\% davon sind rot. "
                  "Zwei rote und ein weißer Knopf kommen dazu. Begründe, "
                  "dass $\\frac{0{,}1n + 2}{n + 3}$ die Wahrscheinlichkeit "
                  "für einen roten Knopf angibt. (Abitur 2019 GK)"),
         loesung=("Zähler: die roten Knöpfe von vorher plus die zwei neuen "
                  "roten; Nenner: alle Knöpfe von vorher plus die drei "
                  "neuen; Laplace: günstige durch alle.")),
}

# --- Pflichtformen: umgeschriebene Zeilen, Schlüssel (pflicht, variante) -

PFLICHT = {
    1: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Zwei Münzen werden geworfen. Mia schreibt die "
                     "Ergebnisse (K; K), (K; Z), (Z; K), (Z; Z) auf und "
                     "rechnet für „einmal Kopf, einmal Zahl“ $P = "
                     "\\frac{2}{4}$. Prüfe, ob Mia richtig gerechnet hat."),
            loesung=("Richtig. Die Reihenfolge zählt: (K; Z) und (Z; K) "
                     "sind zwei von vier gleich wahrscheinlichen "
                     "Ergebnissen.")),
        ("fehler", 3): z(
            form="text",
            aufgabe=("Es gilt $P(A) = 0{,}5$ und $P(B) = 0{,}4$. Für $P(A "
                     "\\cup B)$ nennen vier Schüler diese Werte: $0{,}3$; "
                     "$0{,}6$; $0{,}95$; $1{,}1$. Welche Ergebnisse können "
                     "nicht stimmen? Begründe, ohne genau zu rechnen."),
            loesung=("$0{,}3$ nicht, die Vereinigung ist mindestens so "
                     "wahrscheinlich wie A allein; $0{,}95$ nicht, sie ist "
                     "höchstens $P(A) + P(B) = 0{,}9$; $1{,}1$ nicht, eine "
                     "Wahrscheinlichkeit ist höchstens 1; $0{,}6$ kann "
                     "stimmen.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) $P(A "
                     "\\cap B)$ ist nie größer als $P(A)$.\\\\ (2) Das "
                     "Gegenereignis von „A oder B“ ist immer „nicht A oder "
                     "nicht B“.\\\\ (3) Es gibt Ereignisse A und B mit $P(A "
                     "\\cup B) = P(A) + P(B)$."),
            loesung=("(1) wahr, denn der Schnitt ist eine Teilmenge von A; "
                     "(2) falsch, z. B. „nicht Regen oder nicht Schnee“ "
                     "gilt auch bei Regen ohne Schnee, das Gegenereignis "
                     "ist „weder A noch B“, also $\\bar{A} \\cap \\bar{B}$; "
                     "(3) wahr, denn schließen sich A und B aus, ist der "
                     "Schnitt leer.")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("Lars sagt: „Beim Wurf zweier Würfel ist die "
                     "Augensumme 3 genauso wahrscheinlich wie die "
                     "Augensumme 2. Für beide gibt es nur eine Zerlegung.“ "
                     "Begründe, ob Lars recht hat."),
            loesung=("Nein; Augensumme 3 hat die zwei Ergebnisse (1; 2) und "
                     "(2; 1), also $\\frac{2}{36}$, Augensumme 2 nur (1; 1), "
                     "also $\\frac{1}{36}$ – die Reihenfolge zählt.")),
        ("anwendung", 1): z(
            aufgabe=("In einer Stadt haben 62\\,\\% der Haushalte ein "
                     "Fahrrad, 48\\,\\% ein Auto und 25\\,\\% beides. Ein "
                     "Carsharing-Anbieter startet nur, wenn mindestens "
                     "12\\,\\% der Haushalte weder Fahrrad noch Auto haben. "
                     "Startet er?"),
            loesung=("Ja; Vereinigung: $62\\,\\% + 48\\,\\% - 25\\,\\% = "
                     "85\\,\\%$; Gegenereignis: $100\\,\\% - 85\\,\\% = "
                     "15\\,\\%$, mehr als $12\\,\\%$."),
            pruef="15"),
    },
    2: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Ein Glücksrad hat Sektoren mit $150^\\circ$ (rot), "
                     "$120^\\circ$ (blau) und $90^\\circ$ (grün). Lea "
                     "rechnet für Grün $P = \\frac{90}{360} = \\frac{1}{4}$. "
                     "Prüfe, ob Lea richtig gerechnet hat."),
            loesung=("Richtig. Bei ungleichen Sektoren ist die "
                     "Wahrscheinlichkeit der Anteil des Winkels an "
                     "$360^\\circ$.")),
        ("fehler", 3): z(
            form="text",
            aufgabe=("Zwei Würfel werden geworfen. Für die "
                     "Wahrscheinlichkeit der Augensumme 9 nennen vier "
                     "Schüler diese Werte: $\\frac{4}{36}$; "
                     "$\\frac{1}{11}$; $1{,}2$; $-\\frac{1}{36}$. Welche "
                     "Ergebnisse können nicht stimmen? Begründe, ohne genau "
                     "zu rechnen."),
            loesung=("$\\frac{1}{11}$ nicht, der Nenner muss 36 oder ein "
                     "Teiler davon sein (36 gleich wahrscheinliche Paare, "
                     "nicht 11 Summen); $1{,}2$ nicht, eine "
                     "Wahrscheinlichkeit ist höchstens 1; "
                     "$-\\frac{1}{36}$ nicht, sie ist nie negativ; "
                     "$\\frac{4}{36}$ kann stimmen.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) Bei "
                     "einem Laplace-Experiment sind alle Ergebnisse gleich "
                     "wahrscheinlich.\\\\ (2) Jedes Glücksrad ist ein "
                     "Laplace-Experiment für seine Farben.\\\\ (3) Es gibt "
                     "Würfel, bei denen die Seiten gleich wahrscheinlich "
                     "sind, die Zahlen aber nicht."),
            loesung=("(1) wahr, denn das ist die Laplace-Bedingung; (2) "
                     "falsch, z. B. ein Rad mit $180^\\circ$ Rot und zweimal "
                     "$90^\\circ$ Blau und Grün; (3) wahr, z. B. ein Würfel, "
                     "der zweimal die 1 trägt – die 1 ist doppelt so "
                     "wahrscheinlich wie jede andere Zahl.")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("Ina sagt: „Beim Wurf zweier Würfel sind zwei Einsen "
                     "genauso wahrscheinlich wie eine Eins und eine Zwei. "
                     "Beides ist nur ein Ergebnis.“ Begründe, ob Ina recht "
                     "hat."),
            loesung=("Nein; zwei Einsen sind nur (1; 1), eine Eins und eine "
                     "Zwei sind zwei Ergebnisse, (1; 2) und (2; 1), also "
                     "doppelt so wahrscheinlich.")),
        ("anwendung", 2): z(
            aufgabe=("Eine Tombola hat 400 Lose: 1 Hauptgewinn, 15 "
                     "Sachpreise, 84 Trostpreise, der Rest sind Nieten. Der "
                     "Verein wirbt mit dem Satz „Jedes vierte Los "
                     "gewinnt“. Stimmt das?"),
            loesung=("Ja; Gewinnlose zählen: $1 + 15 + 84 = 100$; Laplace: "
                     "$P = \\frac{100}{400} = \\frac{1}{4}$, also genau "
                     "jedes vierte Los."),
            antwort="",
            pruef="[1, 4]"),
    },
    3: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Ein Versuch gelingt mit $0{,}2$. Sara rechnet für "
                     "„fünf Versuche, kein Erfolg“ $P = 0{,}8^5 \\approx "
                     "0{,}328$. Prüfe, ob Sara richtig gerechnet hat."),
            loesung=("Richtig. „Kein Erfolg“ ist ein Pfad aus lauter "
                     "Nieten; die Basis ist die Nietenwahrscheinlichkeit "
                     "$0{,}8$.")),
        ("fehler", 3): z(
            form="text",
            aufgabe=("Ein Würfel wird mehrmals geworfen. Für die "
                     "Wahrscheinlichkeit von mindestens einer Sechs nennen "
                     "vier Schüler diese Werte: bei vier Würfen "
                     "$\\frac{4}{6}$; bei sieben Würfen $\\frac{7}{6}$; bei "
                     "drei Würfen $0{,}42$; bei zwei Würfen $0{,}05$. "
                     "Welche Ergebnisse können nicht stimmen? Begründe, "
                     "ohne genau zu rechnen."),
            loesung=("$\\frac{7}{6}$ nicht, eine Wahrscheinlichkeit ist "
                     "höchstens 1 – wer die Würfe mal $\\frac{1}{6}$ "
                     "rechnet, käme bei sieben Würfen auf "
                     "$\\frac{7}{6} > 1$; $\\frac{4}{6}$ nicht, es ist nach "
                     "demselben falschen Muster gerechnet und zählt Pfade "
                     "mit zwei Sechsen doppelt; $0{,}05$ nicht, schon die "
                     "Sechs im ersten Wurf hat $\\frac{1}{6}$; $0{,}42$ "
                     "kann stimmen.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) Beim "
                     "Ziehen mit Zurücklegen stehen auf jeder Stufe "
                     "dieselben Astwahrscheinlichkeiten.\\\\ (2) „Mindestens "
                     "einmal“ bei n Versuchen ist immer n mal die "
                     "Trefferwahrscheinlichkeit.\\\\ (3) Es gibt Bäume mit "
                     "verschieden langen Pfaden, deren Pfade zusammen die "
                     "Wahrscheinlichkeit 1 haben."),
            loesung=("(1) wahr, denn nach dem Zurücklegen ist die Urne "
                     "wieder wie am Anfang; (2) falsch, z. B. zwei "
                     "Münzwürfe: $2 \\cdot \\frac{1}{2} = 1$, aber zweimal "
                     "Zahl ist möglich; richtig ist eins minus die "
                     "Nietenwahrscheinlichkeit hoch n; (3) wahr, denn bei einem Baum mit Abbruch "
                     "endet jeder Verlauf an genau einem Pfadende.")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("Tom sagt: „Wirft man eine Münze zweimal, ist ‚einmal "
                     "Kopf, einmal Zahl‘ genauso wahrscheinlich wie "
                     "‚zweimal Kopf‘.“ Begründe, ob Tom recht hat."),
            loesung=("Nein; zu „einmal Kopf, einmal Zahl“ gehören zwei "
                     "Pfade, KZ und ZK, zusammen $\\frac{1}{2}$, zu "
                     "„zweimal Kopf“ nur einer mit $\\frac{1}{4}$.")),
        ("anwendung", 1): z(
            aufgabe=("Ein Rauchmelder schlägt bei Rauch mit $0{,}95$ an. "
                     "Die Versicherung verlangt, dass im Flur mit "
                     "mindestens $0{,}99$ wenigstens ein Melder anschlägt. "
                     "Reichen zwei unabhängige Melder?"),
            loesung=("Ja; Gegenereignis keiner schlägt an: $0{,}05^2 = "
                     "0{,}0025$; mindestens einer: $1 - 0{,}0025 = "
                     "0{,}9975$, mehr als $0{,}99$."),
            antwort="",
            pruef="0.9975"),
    },
    4: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Eine Tüte enthält 6 rote und 4 gelbe Gummibärchen. "
                     "Zwei werden ohne Zurücklegen genommen. Pia rechnet "
                     "für verschiedene Farben $P = \\frac{6}{10} \\cdot "
                     "\\frac{4}{9} + \\frac{4}{10} \\cdot \\frac{6}{9} = "
                     "\\frac{8}{15}$. Prüfe, ob Pia richtig gerechnet hat."),
            loesung=("Richtig. Zu „verschiedene Farben“ gehören zwei Pfade, "
                     "rot-gelb und gelb-rot; beide werden addiert.")),
        ("fehler", 3): z(
            form="text",
            aufgabe=("Eine Urne enthält 5 rote und 3 blaue Kugeln. Zwei "
                     "werden ohne Zurücklegen gezogen. Für die "
                     "Wahrscheinlichkeit, dass beide rot sind, nennen vier "
                     "Schüler diese Werte: $\\frac{25}{64}$; "
                     "$\\frac{5}{14}$; $\\frac{5}{8}$; $\\frac{20}{56}$. "
                     "Welche Ergebnisse können nicht stimmen? Begründe, "
                     "ohne genau zu rechnen."),
            loesung=("$\\frac{25}{64}$ nicht, der Nenner $8 \\cdot 8$ zeigt "
                     "Zurücklegen, ohne Zurücklegen steht $8 \\cdot 7$ im "
                     "Nenner; $\\frac{5}{8}$ nicht, das ist schon der erste "
                     "Zug allein, zwei rote sind seltener; "
                     "$\\frac{5}{14}$ und $\\frac{20}{56}$ können stimmen, "
                     "sie sind gleich.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) Ohne "
                     "Zurücklegen sinkt der Nenner bei jedem Zug um "
                     "eins.\\\\ (2) Ohne Zurücklegen ändert sich auf der "
                     "zweiten Stufe immer auch der Zähler.\\\\ (3) Es gibt "
                     "ein Umlegen, nach dem die Wahrscheinlichkeit für Rot "
                     "in der zweiten Urne gleich bleibt."),
            loesung=("(1) wahr, denn nach jedem Zug fehlt eine Kugel; (2) "
                     "falsch, z. B. nach einer blauen Kugel bleibt die Zahl "
                     "der roten gleich, nur der Nenner sinkt; (3) wahr, "
                     "z. B. A mit 2 roten und 2 blauen, B mit 1 roten und 1 "
                     "blauen: danach $\\frac{1}{2} \\cdot \\frac{2}{3} + "
                     "\\frac{1}{2} \\cdot \\frac{1}{3} = \\frac{1}{2}$ wie "
                     "vorher.")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("In einer Lostrommel liegen 30 Lose, 3 davon gewinnen. "
                     "Jeder zieht ein Los, ohne es zurückzulegen. Emma zieht "
                     "als Zweite. Sie sagt: „Solange ich nicht weiß, was der "
                     "Erste gezogen hat, ist meine Chance genauso groß wie "
                     "seine.“ Begründe, ob Emma recht hat."),
            loesung=("Ja; über beide Pfade: $\\frac{3}{30} \\cdot "
                     "\\frac{2}{29} + \\frac{27}{30} \\cdot \\frac{3}{29} = "
                     "\\frac{3}{30}$, genau die Chance des Ersten – die "
                     "Position ändert nichts.")),
        ("anwendung", 1): z(
            aufgabe=("In einer Kiste mit 24 Akkus sind 2 defekt. Die "
                     "Kontrolle prüft 3 zufällig gewählte Akkus. Der Händler "
                     "will mit mindestens 25\\,\\% Wahrscheinlichkeit "
                     "wenigstens einen defekten entdecken. Reicht diese "
                     "Kontrolle?"),
            loesung=("Nein; Gegenereignis keiner defekt: "
                     "$\\frac{22}{24} \\cdot \\frac{21}{23} \\cdot "
                     "\\frac{20}{22} \\approx 0{,}761$; mindestens einer: "
                     "$1 - 0{,}761 \\approx 0{,}239$, weniger als "
                     "$25\\,\\%$."),
            antwort="",
            pruef="1-22*21*20/(24*23*22)"),
    },
    5: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Ein Versuch gelingt mit $\\frac{1}{2}$. Es gibt sechs "
                     "Versuche. Gesucht ist die Wahrscheinlichkeit für "
                     "genau drei Treffer, die unmittelbar hintereinander "
                     "liegen. Lena rechnet $4 \\cdot "
                     "\\left(\\frac{1}{2}\\right)^6 = \\frac{1}{16}$. Prüfe, "
                     "ob Lena richtig gerechnet hat."),
            loesung=("Richtig. Der Block aus drei Treffern hat unter sechs "
                     "Versuchen vier Lagen; jede Lage ist ein Pfad mit "
                     "$\\left(\\frac{1}{2}\\right)^6$.")),
        ("fehler", 3): z(
            form="text",
            aufgabe=("Ein Würfel wird dreimal geworfen. Für die "
                     "Wahrscheinlichkeit von genau zwei Sechsen nennen vier "
                     "Schüler diese Werte: $\\frac{5}{216}$; "
                     "$\\frac{15}{216}$; $\\frac{75}{216}$; "
                     "$\\frac{1}{2}$. Welche Ergebnisse können nicht "
                     "stimmen? Begründe, ohne genau zu rechnen."),
            loesung=("$\\frac{5}{216}$ nicht, das ist nur ein Pfad, der "
                     "Faktor 3 für die Reihenfolgen fehlt; "
                     "$\\frac{75}{216}$ nicht, der Zähler $3 \\cdot 5 "
                     "\\cdot 5$ gehört zu genau einer Sechs; "
                     "$\\frac{1}{2}$ nicht, zwei Sechsen verlangen zweimal "
                     "$\\frac{1}{6}$, das bleibt unter $3 \\cdot "
                     "\\frac{1}{36}$; $\\frac{15}{216}$ kann stimmen.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) Pfade "
                     "mit denselben Sorten in anderer Reihenfolge haben "
                     "immer dieselbe Wahrscheinlichkeit, auch ohne "
                     "Zurücklegen.\\\\ (2) Für k Treffer unmittelbar "
                     "hintereinander unter n Versuchen gibt es immer „n "
                     "über k“ Lagen.\\\\ (3) Es gibt Ereignisse, bei denen "
                     "man einen Pfad mit 6 multiplizieren muss."),
            loesung=("(1) wahr, denn die Faktoren tauschen nur den Platz, "
                     "Zähler und Nenner bleiben dieselben; (2) falsch, "
                     "z. B. drei Treffer hintereinander unter fünf "
                     "Versuchen haben 3 Lagen, „5 über 3“ ist aber 10; (3) "
                     "wahr, z. B. drei verschiedene Farben bei drei "
                     "Drehungen haben $3! = 6$ Reihenfolgen.")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("Jonas sagt: „Bei drei Münzwürfen ist ‚genau zweimal "
                     "Kopf‘ genauso wahrscheinlich wie ‚dreimal Kopf‘, denn "
                     "jeder Pfad hat $\\left(\\frac{1}{2}\\right)^3$.“ "
                     "Begründe, ob Jonas recht hat."),
            loesung=("Nein; zu „genau zweimal Kopf“ gehören drei Pfade (KKZ, "
                     "KZK, ZKK), also $\\frac{3}{8}$, zu „dreimal Kopf“ nur "
                     "einer mit $\\frac{1}{8}$.")),
        ("anwendung", 1): z(
            aufgabe=("Eine Bäckerei verkauft Körnerbrötchen mit $0{,}4$, "
                     "Weizenbrötchen mit $0{,}35$ und Roggenbrötchen mit "
                     "$0{,}25$. Drei Kunden kaufen nacheinander je ein "
                     "Brötchen. Der Bäcker legt ein Probierpaket aus, wenn "
                     "jede Sorte mit mindestens $0{,}2$ genau einmal gekauft "
                     "wird. Legt er es aus?"),
            loesung=("Ja; ein Pfad: $0{,}4 \\cdot 0{,}35 \\cdot 0{,}25 = "
                     "0{,}035$; Reihenfolgen: $3! = 6$; Ergebnis: $6 \\cdot "
                     "0{,}035 = 0{,}21$, mehr als $0{,}2$."),
            antwort="",
            pruef="0.21"),
    },
    6: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Werk A liefert 70\\,\\% der Teile mit 2\\,\\% "
                     "Ausschuss, Werk B 30\\,\\% mit 6\\,\\%. Ada rechnet "
                     "den Ausschuss insgesamt: $0{,}7 \\cdot 0{,}02 + 0{,}3 "
                     "\\cdot 0{,}06 = 0{,}032$. Prüfe, ob Ada richtig "
                     "gerechnet hat."),
            loesung=("Richtig. Die totale Wahrscheinlichkeit ist die Summe "
                     "der Pfade zum Ausschuss, jeder Anteil gewichtet mit "
                     "seiner Gruppe.")),
        ("fehler", 3): z(
            form="text",
            aufgabe=("In einer Firma arbeiten 70\\,\\% der Beschäftigten in "
                     "Vollzeit, von ihnen nutzen 20\\,\\% ein Dienstrad; von "
                     "den Teilzeitkräften 50\\,\\%. Für den Anteil aller "
                     "Beschäftigten mit Dienstrad nennen vier Schüler diese "
                     "Werte: 14\\,\\%; 29\\,\\%; 35\\,\\%; 55\\,\\%. Welche "
                     "Ergebnisse können nicht stimmen? Begründe, ohne genau "
                     "zu rechnen."),
            loesung=("14\\,\\% und 55\\,\\% nicht, der Anteil aller liegt "
                     "zwischen 20\\,\\% und 50\\,\\%; 35\\,\\% nicht, das "
                     "ist die ungewichtete Mitte, die größere Gruppe mit "
                     "20\\,\\% zieht den Wert darunter; 29\\,\\% kann "
                     "stimmen.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) Die "
                     "Äste an einem Knoten haben immer zusammen die "
                     "Wahrscheinlichkeit 1.\\\\ (2) Ein Anteil „aller "
                     "Befragten“ steht immer an einem Ast der zweiten "
                     "Stufe.\\\\ (3) Es gibt Situationen, in denen die "
                     "totale Wahrscheinlichkeit gleich einem der bedingten "
                     "Anteile ist."),
            loesung=("(1) wahr, denn die Äste an einem Knoten teilen "
                     "dieselbe Gruppe vollständig auf; (2) falsch, z. B. "
                     "„12 % aller sind Frauen mit Brille“ ist ein Pfad, kein "
                     "Ast; (3) wahr, z. B. wenn beide Gruppen denselben "
                     "Anteil haben, etwa je 30 %.").replace(" %", "\\,\\%")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("Mia liest: „Unter den Radfahrern tragen 80\\,\\% einen "
                     "Helm.“ Sie sagt: „Also sind 80\\,\\% aller "
                     "Verkehrsteilnehmer Radfahrer mit Helm.“ Begründe, ob "
                     "Mia recht hat."),
            loesung=("Nein; 80\\,\\% ist ein Anteil unter den Radfahrern, "
                     "ein Ast; der Anteil aller ist der Pfad, 80\\,\\% mal "
                     "dem Anteil der Radfahrer.")),
        ("anwendung", 1): z(
            aufgabe=("Ein Onlineshop verschickt 25\\,\\% der Bestellungen "
                     "per Express, davon kommen 4\\,\\% verspätet an; beim "
                     "Standardversand sind es 9\\,\\%. Der Shop verspricht: "
                     "höchstens 7\\,\\% aller Bestellungen kommen verspätet. "
                     "Hält er das ein?"),
            loesung=("Nein; Pfadsumme: $0{,}25 \\cdot 0{,}04 + 0{,}75 \\cdot "
                     "0{,}09 = 0{,}0775$; Ergebnis: $7{,}75\\,\\%$, mehr "
                     "als $7\\,\\%$."),
            antwort="",
            pruef="0.0775"),
    },
    7: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Ein Glücksrad trifft mit $0{,}2$ und wird dreimal "
                     "gedreht. Paul deutet den Term $3 \\cdot 0{,}2 \\cdot "
                     "0{,}8^2$: „genau ein Treffer; die 3 zählt die Stellen, "
                     "an denen der Treffer stehen kann.“ Prüfe, ob Paul "
                     "richtig gedeutet hat."),
            loesung=("Richtig. Ein Vorfaktor zählt die Reihenfolgen; "
                     "$0{,}2 \\cdot 0{,}8^2$ ist ein Pfad mit einem Treffer "
                     "und zwei Nieten."),
            pruef=""),
        ("fehler", 3): z(
            form="text",
            aufgabe=("Ein Glücksrad trifft mit $0{,}3$ und wird fünfmal "
                     "gedreht. Für genau zwei Treffer geben vier Schüler "
                     "diese Terme an: $10 \\cdot 0{,}3^2 \\cdot 0{,}7^3$; "
                     "$10 \\cdot 0{,}3^2 \\cdot 0{,}7^2$; $0{,}3^2 \\cdot "
                     "0{,}7^3$; $10 \\cdot 0{,}7^2 \\cdot 0{,}3^3$. Welche "
                     "Ergebnisse können nicht stimmen? Begründe, ohne genau "
                     "zu rechnen."),
            loesung=("$10 \\cdot 0{,}3^2 \\cdot 0{,}7^2$ nicht, die "
                     "Exponenten ergeben 4 statt 5 Versuche; $0{,}3^2 "
                     "\\cdot 0{,}7^3$ nicht, der Vorfaktor für die "
                     "Reihenfolgen fehlt; $10 \\cdot 0{,}7^2 \\cdot 0{,}3^3$ "
                     "nicht, das sind drei Treffer; $10 \\cdot 0{,}3^2 "
                     "\\cdot 0{,}7^3$ kann stimmen.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) Ein "
                     "Produktterm ohne Vorfaktor beschreibt immer genau "
                     "einen Pfad.\\\\ (2) Ein Term, der mit „1 −“ beginnt, "
                     "beschreibt immer „mindestens einmal“.\\\\ (3) Es gibt "
                     "Wahrscheinlichkeiten wie $\\frac{16}{81}$, die als "
                     "Potenz eine Ergebnisfolge verraten."),
            loesung=("(1) wahr, denn jeder Faktor ist eine Stufe eines "
                     "einzigen Pfads; (2) falsch, z. B. $1 - 0{,}7^4 - 4 "
                     "\\cdot 0{,}3 \\cdot 0{,}7^3$ ist „mindestens zwei“; "
                     "(3) wahr, denn $\\frac{16}{81} = "
                     "\\left(\\frac{2}{3}\\right)^4$ heißt viermal dasselbe "
                     "Ergebnis mit $\\frac{2}{3}$.")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("Ein Versuch gelingt mit $0{,}4$. Es gibt fünf "
                     "Versuche. Leon sagt: „$0{,}4^3 \\cdot 0{,}6^2$ heißt: "
                     "dreimal Erfolg, irgendwo unter den fünf Versuchen.“ "
                     "Begründe, ob Leon recht hat."),
            loesung=("Nein; ohne Vorfaktor ist es ein einziger Pfad, also "
                     "eine feste Reihenfolge, etwa erst drei Erfolge, dann "
                     "zwei Misserfolge; für „irgendwo“ fehlt der Faktor „5 "
                     "über 3“.")),
        ("anwendung", 3): z(
            aufgabe=("Ein Medikament hat mit 1\\,\\% eine bestimmte "
                     "Nebenwirkung. Eine Praxis behandelt 200 Patienten "
                     "damit. Der Beipackzettel sagt: „Bei 200 Patienten "
                     "tritt die Nebenwirkung mit mehr als 80\\,\\% "
                     "Wahrscheinlichkeit mindestens einmal auf.“ Stimmt "
                     "das?"),
            loesung=("Ja; Gegenereignis bei keinem: $0{,}99^{200} \\approx "
                     "0{,}134$; mindestens einmal: $1 - 0{,}99^{200} "
                     "\\approx 0{,}866$, mehr als $0{,}8$."),
            antwort="",
            pruef="1-0.99**200"),
    },
    8: {
        ("fehler", 2): z(
            form="text",
            aufgabe=("Ein Glücksrad hat zwei Sektoren. Die "
                     "Wahrscheinlichkeit, bei zwei Drehungen zweimal "
                     "dieselbe Farbe zu erhalten, ist $0{,}68$. Lara stellt "
                     "die Gleichung auf, erhält $p = 0{,}2$ oder $p = "
                     "0{,}8$ und gibt für den kleineren Sektor $0{,}2 "
                     "\\cdot 360^\\circ = 72^\\circ$ an. Prüfe, ob Lara "
                     "richtig gerechnet hat."),
            loesung=("Richtig. Beide Lösungen liegen zwischen 0 und 1; der "
                     "kleinere Sektor gehört zur kleineren Lösung.")),
        ("fehler", 3): z(
            form="text",
            aufgabe=("Tim löst $0{,}7 \\cdot 0{,}4 + 0{,}3a = 0{,}43$. "
                     "Zeile 1: $0{,}28 + 0{,}3a = 0{,}43$. Zeile 2: $0{,}3a "
                     "= 0{,}71$. Zeile 3: $a \\approx 2{,}37$. Setze $a = "
                     "0{,}5$ in jede Zeile ein. In welcher Zeile stimmt es "
                     "nicht mehr?"),
            loesung=("In Zeile 2 stimmt es nicht mehr: Tim addiert "
                     "$0{,}28$, statt es auf beiden Seiten abzuziehen. "
                     "Richtig ist $0{,}3a = 0{,}15$, also $a = 0{,}5$.")),
        ("begruenden", 2): z(
            form="text",
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe, ohne genau zu rechnen.\\\\ (1) Eine "
                     "Bedingung an eine Wahrscheinlichkeit führt immer auf "
                     "eine lineare Gleichung.\\\\ (2) Eine Lösung größer "
                     "als 1 ist nie ein zulässiger Anteil.\\\\ (3) Es gibt "
                     "Bedingungen, bei denen beide Lösungen einer "
                     "quadratischen Gleichung zulässig sind."),
            loesung=("(1) falsch, z. B. „zweimal dieselbe Farbe“ bei einem "
                     "Glücksrad mit unbekanntem Sektor führt auf eine "
                     "quadratische Gleichung; (2) wahr, denn ein Anteil "
                     "liegt zwischen 0 und 1; (3) wahr, z. B. beim Glücksrad "
                     "mit zwei Sektoren gehören p und die Gegenlösung zur "
                     "selben Aufteilung, erst die Frage entscheidet.")),
        ("begruenden", 3): z(
            form="text",
            aufgabe=("Ole sagt: „Die Gleichung für den gesuchten Anteil hat "
                     "die Lösungen $a = 0{,}3$ und $a = 1{,}7$. Also gibt es "
                     "zwei mögliche Anteile.“ Begründe, ob Ole recht hat."),
            loesung=("Nein; ein Anteil liegt zwischen 0 und 1, die Lösung "
                     "$1{,}7$ fällt weg, nur $a = 0{,}3$ bleibt.")),
        ("anwendung", 1): z(
            form="gleichungsraster",
            aufgabe=("In einer Fahrschule bestehen 75\\,\\% die Prüfung "
                     "beim ersten Mal; von den übrigen besteht der Anteil a "
                     "beim zweiten Mal. Insgesamt bestehen 93\\,\\% "
                     "spätestens beim zweiten Mal. Die Fahrschule wirbt: "
                     "„Mehr als 70\\,\\% derer, die beim ersten Mal "
                     "durchfallen, bestehen beim zweiten Mal.“ Stimmt das?"),
            loesung=("Ja; Bedingung Pfadsumme = 0,93: $0{,}75 + 0{,}25a = "
                     "0{,}93$; nach a auflösen: $0{,}25a = 0{,}18$, also $a "
                     "= 0{,}72$, mehr als $0{,}7$."),
            antwort="",
            pruef="0.72"),
    },
}


# --- Umbau ---------------------------------------------------------------

def gleich(a, b):
    return all(a.get(f) == b.get(f) for f in INHALT)


def baue(e):
    alt = [json.loads(x) for x in open(f"{B}e{e}.jsonl", encoding="utf-8")]
    q_kette = 154 + e
    zaehl = {"übernommen": 0, "neu": 0, "umgeschrieben": 0, "entfallen": 0}
    neu = []
    gf = GRUNDFALL[e]()
    kette_texte = glieder(q_kette)
    # erste Verfahrenskette: alte Sprossen -> neue Sprossen
    alte_k1 = [a for a in alt if a["kette_nr"] == 1]
    s_max_alt = max(a["sprosse"] for a in alte_k1)
    for a in alt:
        b = copy.deepcopy(a)
        status = "übernommen"
        if a["kette_nr"] == 1:
            b["quelle"] = q_kette
            s = a["sprosse"]
            if e == 3 and s >= 6:
                b["sprosse"] = s + 1
            # Übernahme: sprosse_text bleibt, wenn er wortgleich in der
            # Zeile steht; sonst der (längere) Katalogtext
            if a["sprosse_text"] not in KAT[q_kette]:
                if s == 0:
                    b["sprosse_text"] = vorstufe(q_kette)
                elif a["hoehe"] == "pruefung":
                    b["sprosse_text"] = glied(q_kette,
                                              len(kette_texte) - 1)
            if a["hoehe"] == "grundfall":
                g = gf[a["variante"] - 1]
                for f, w in g.items():
                    b[f] = w
                status = "übernommen" if gleich(a, b) else "umgeschrieben"
        elif a["hoehe"] == "pflicht":
            p = a["pflicht"]
            if p in ("fehler", "begruenden"):
                b["merkmal"] = M_FEHLER8 if (p, e) == ("fehler", 8) else \
                    (M_FEHLER if p == "fehler" else M_BEGR)
            if p == "anwendung":
                b["sprosse_text"], b["quelle"] = ANW
            elif p == "darstellung":
                b["sprosse_text"], b["quelle"] = DAR[e]
            ueber = PFLICHT[e].get((p, a["variante"]))
            if ueber:
                for f, w in ueber.items():
                    b[f] = w
            status = "übernommen" if gleich(a, b) else "umgeschrieben"
        zaehl[status] += 1
        neu.append(b)
        # neue Sprosse e3 s6 nach der letzten alten s5-Zeile
        if (e == 3 and a["kette_nr"] == 1 and a["sprosse"] == 5
                and a["variante"] == 3):
            vorlage = b
            for v, zeile in enumerate(E3_LUECKE, 1):
                c = copy.deepcopy(vorlage)
                c.update(zeile)
                c.update(sprosse=6, variante=v, hoehe="sprosse",
                         sprosse_text=glied(q_kette, 6), quelle=q_kette)
                neu.append(c)
                zaehl["neu"] += 1
        # dritte Zeile ohne Original an der Prüfungshöhe
        if (e in PRUEF_NEU and a["kette_nr"] == 1
                and a["hoehe"] == "pruefung" and a["sprosse"] == s_max_alt
                and a["variante"] == max(x["variante"] for x in alte_k1
                                         if x["sprosse"] == s_max_alt)):
            c = copy.deepcopy(b)
            c.update(PRUEF_NEU[e])
            c.update(variante=a["variante"] + 1, hoehe="pruefung")
            neu.append(c)
            zaehl["neu"] += 1
    for b in neu:
        b["id"] = (f"{E}-e{e}-k{b['kette_nr']}-s{b['sprosse']}"
                   f"-v{b['variante']}")
    with open(f"{B}e{e}.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for b in neu:
            f.write(json.dumps(b, ensure_ascii=False) + "\n")
    print(f"e{e}: {len(neu)} Zeilen; " + ", ".join(
        f"{k} {v}" for k, v in zaehl.items()))


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        baue(int(arg.lstrip("e")))

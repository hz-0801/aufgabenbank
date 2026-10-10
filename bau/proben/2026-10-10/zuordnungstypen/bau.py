#!/usr/bin/env python3
"""Bau FA5: Zuordnungen E4 – Bankzeilen und Lernweg-Block erzeugen."""
import json
import sys
from sympy import Rational as R

BANK = "/root/work/w8c/aufgabenbank/bank/zuordnungen/e4.jsonl"
KENN = "FA5"
ORD = "bau/proben/2026-10-10/zuordnungstypen"

alt = [json.loads(z) for z in open(BANK, encoding="utf-8") if z.strip()]
meta, vmax = {}, {}
for a in alt:
    k = (a["kette_nr"], a["sprosse"])
    meta.setdefault(k, a)
    vmax[k] = max(vmax.get(k, 0), a["variante"])


def tab(xs, ys, kx="x", ky="y", breite=60):
    return ("\\begin{tikzpicture}\\node[inner sep=0pt]{\\begin{minipage}{%dmm}"
            "\\centering \\wertetabelle[%s]{%s}{%s}{%s} \\end{minipage}};"
            "\\end{tikzpicture}" % (breite, ",".join(ys), kx, ky, ",".join(xs)))


def mini(dx, art, marke):
    """kleines Achsenkreuz bei x=dx mit Graph und Beschriftung."""
    s = (f"\\begin{{scope}}[xshift={dx}cm]"
         "\\draw[black!15,step=0.4] (0,0) grid (1.6,1.6);"
         "\\draw[-{Stealth[length=1.5mm]},line width=0.5pt] (0,0) -- (1.8,0);"
         "\\draw[-{Stealth[length=1.5mm]},line width=0.5pt] (0,0) -- (0,1.8);")
    if art == "p":
        s += "\\draw[line width=0.9pt] (0,0) -- (1.6,1.4);"
    elif art == "a":
        s += ("\\draw[line width=0.9pt,domain=0.24:1.6,samples=40] "
              "plot (\\x,{0.36/\\x});")
    elif art == "k":
        s += "\\draw[line width=0.9pt] (0,0.5) -- (1.6,1.5);"
    elif art == "kf":
        s += "\\draw[line width=0.9pt] (0,1.4) -- (1.4,0);"
    s += (f"\\node[below,font=\\scriptsize] at (0.8,-0.05) {{{marke}}};"
          "\\end{scope}")
    return s


def graphen(arten, marken, abst=2.3):
    return ("\\begin{tikzpicture}" + "".join(
        mini(i * abst, a, m) for i, (a, m) in enumerate(zip(arten, marken)))
        + "\\end{tikzpicture}")


KREUZ3 = ("\\kreuz{proportional} \\kreuz{antiproportional} "
          "\\kreuz{keins von beiden}")

zeilen = []   # (schluessel, felder)
block = {}    # abschnitt -> {beispiel, aufgaben, vorrat}


def neu(ab, rolle, k, s, **f):
    key = (k, s)
    vmax[key] += 1
    m = meta[key]
    a = dict(id=f"zuordnungen-e4-k{k}-s{s}-v{vmax[key]}",
             eintrag="zuordnungen", einheit=4, kette=m["kette"],
             kette_nr=k, sprosse=s, sprosse_text=m["sprosse_text"],
             merkmal=m["merkmal"], hoehe=m["hoehe"])
    if "pflicht" in m:
        a["pflicht"] = m["pflicht"]
    a.update(variante=vmax[key], aufgabe=f["aufgabe"],
             form=f.get("form", "teil"), antwort=f.get("antwort", ""),
             loesung=f["loesung"], pruef=f.get("pruef", ""), original=None,
             grafik=f.get("grafik", ""), loesungsgrafik="",
             quelle=m["quelle"])
    blatt = not rolle.startswith("vorrat")
    a["herkunft"] = (f"Bau 2026-10-10 ({ORD}), Blatt {KENN}" if blatt else
                     f"Vorrat 2026-10-10 zum Lernweg {KENN}, Abschnitt {ab}")
    a.update(sache=f.get("sache", ""), darstellung=f["darstellung"],
             frage=f["frage"], antwortform=f["antwortform"])
    if blatt:
        a["blatt"] = [KENN]
    a.update(abschnitt=f"L4-{ab}", rolle=rolle,
             modell_selbst_finden=f.get("msf", "nein"),
             ergebnis=f["ergebnis"])
    if rolle == "beispiel":
        a["schritte"] = f["schritte"]
    b = block.setdefault(ab, dict(beispiel="", aufgaben=[], vorrat=[]))
    if rolle == "beispiel":
        b["beispiel"] = a["id"]
    elif blatt:
        b["aufgaben"].append(a["id"])
    else:
        b["vorrat"].append(a["id"])
    zeilen.append(a)
    return a


def q(xs, ys):
    return [R(y) / R(x) for x, y in zip(xs, ys)]


def p(xs, ys):
    return [R(x) * R(y) for x, y in zip(xs, ys)]


# ---------------------------------------------------------------- A
assert set(p([2, 3, 4, 6], [12, 8, 6, 4])) == {24}
neu("A", "beispiel", 2, 5,
    aufgabe="Beim Aufbau für das Schulfest gilt: 2 Helfer brauchen "
    "12 Stunden, 3 Helfer 8 Stunden, 4 Helfer 6 Stunden und 6 Helfer "
    "4 Stunden. Welcher Zuordnungstyp ist das?",
    grafik="\\begin{tikzpicture}[scale=0.85,transform shape]"
    "\\node[inner sep=0pt] at (2.9,3.0) "
    "{\\begin{minipage}{52mm}\\centering \\setlength{\\mbzell}{0.8cm}"
    "\\wertetabelle[12,8,6,4]"
    "{\\text{Helfer}}{\\text{Stunden}}{2,3,4,6} \\end{minipage}};"
    + graphen("pak", ["proportional", "antiproportional", "keins"], 2.05)
    [len("\\begin{tikzpicture}"):],
    loesung="Quotienten $12 : 2 = 6$, $8 : 3 \\approx 2{,}7$ – nicht "
    "gleich. Produkte $2 \\cdot 12 = 3 \\cdot 8 = 4 \\cdot 6 = 6 \\cdot 4 "
    "= 24$ – immer gleich: antiproportional.", pruef="24",
    schritte=[
        "Schreib die Wertepaare in eine Tabelle: $x$ = Helfer, $y$ = "
        "Stunden (Bild rechts).",
        "Quotienten $y : x$: \\ $12 : 2 = 6$, \\ $8 : 3 \\approx 2{,}7$. "
        "Nicht gleich, also \\emph{nicht} proportional.",
        "Produkte $x \\cdot y$: \\ $2 \\cdot 12 = 24$, \\ $3 \\cdot 8 = 24$, "
        "\\ $4 \\cdot 6 = 24$, \\ $6 \\cdot 4 = 24$. Immer 24.",
        "Also \\textbf{antiproportional}. Am Graphen erkennst du die drei "
        "Typen wie unter der Tabelle.",
    ],
    ergebnis="antiproportional (Produkt immer 24)", sache="Helfer",
    darstellung="text", frage="erkennen", antwortform="begruenden")

assert set(q([2, 4, 5, 8], [6, 12, 15, 24])) == {3}
neu("A", "aufgabe", 2, 1,
    aufgabe="Hefte $x$ und Preis $y$ in €. Welcher Zuordnungstyp ist das? "
    + KREUZ3, form="ankreuzen",
    grafik=tab(["2", "4", "5", "8"], ["6", "12", "15", "24"]),
    loesung="proportional – $6 : 2 = 12 : 4 = 15 : 5 = 24 : 8 = 3$",
    ergebnis="proportional", darstellung="tabelle", frage="erkennen",
    antwortform="ankreuzen")
xs, ys = [1, 2, 3, 5], [30, 15, 10, 6]
assert len(set(q(xs, ys))) > 1 and set(p(xs, ys)) == {30}
neu("A", "aufgabe", 2, 2,
    aufgabe="Welcher Zuordnungstyp ist das? " + KREUZ3, form="ankreuzen",
    grafik=tab(["1", "2", "3", "5"], ["30", "15", "10", "6"]),
    loesung="antiproportional – Quotienten $30$, $7{,}5$, … nicht gleich; "
    "Produkte $1 \\cdot 30 = 2 \\cdot 15 = 3 \\cdot 10 = 5 \\cdot 6 = 30$",
    ergebnis="antiproportional", darstellung="tabelle", frage="erkennen",
    antwortform="ankreuzen")
xs, ys = [1, 2, 3, 4], [5, 7, 9, 11]
assert len(set(q(xs, ys))) > 1 and len(set(p(xs, ys))) > 1
neu("A", "aufgabe", 2, 5,
    aufgabe="Welcher Zuordnungstyp ist das? " + KREUZ3, form="ankreuzen",
    grafik=tab(["1", "2", "3", "4"], ["5", "7", "9", "11"]),
    loesung="keins von beiden – Quotienten $5 : 1 = 5$, $7 : 2 = 3{,}5$; "
    "Produkte $1 \\cdot 5 = 5$, $2 \\cdot 7 = 14$; beide nicht gleich",
    ergebnis="keins von beiden", darstellung="tabelle", frage="erkennen",
    antwortform="ankreuzen")
neu("A", "aufgabe", 2, 4,
    aufgabe="Schreib unter jeden Graphen: proportional, antiproportional "
    "oder keins von beiden.",
    form="text", antwort="(a) \\_\\_ \\ (b) \\_\\_ \\ (c) \\_\\_",
    grafik=graphen(["k", "p", "a"], ["(a)", "(b)", "(c)"]),
    loesung="(a) Gerade, aber nicht durch den Ursprung; (b) Gerade durch "
    "den Ursprung; (c) fallende Kurve",
    ergebnis="(a) keins \\ (b) proportional \\ (c) antiproportional",
    darstellung="graph", frage="zuordnung", antwortform="zuordnen")
assert R(9, 2) == R(9, 2) and R(13, 4) == R(13, 4) and 2 * 9 != 4 * 13
assert R(17, 6) != R(9, 2) and 6 * 17 != 18
neu("A", "ziel", 2, 6,
    aufgabe="Ein Fahrradverleih verlangt für 2 Stunden 9\\,€, für "
    "4 Stunden 13\\,€ und für 6 Stunden 17\\,€. Welcher Zuordnungstyp ist "
    "das? Kann Ole den Preis für 8 Stunden mit dem Dreisatz aus dem Preis "
    "für 2 Stunden berechnen? Begründe mit einer Rechnung.", form="text",
    loesung="Keins von beiden; Quotienten $9 : 2 = 4{,}5$, "
    "$13 : 4 = 3{,}25$ – nicht gleich; Produkte $2 \\cdot 9 = 18$, "
    "$4 \\cdot 13 = 52$ – nicht gleich. Also kein Dreisatz (der Verleih "
    "nimmt eine Grundgebühr von 5\\,€ und 2\\,€ je Stunde).",
    pruef="[4.5, 3.25, 18, 52]",
    ergebnis="keins von beiden; kein Dreisatz", msf="ja",
    sache="Fahrradverleih", darstellung="text", frage="entscheidung",
    antwortform="begruenden")
# Vorrat A
neu("A", "vorrat-leichter", 2, 1,
    aufgabe="Kilogramm $x$ und Preis $y$ in €. Welcher Zuordnungstyp ist "
    "das? " + KREUZ3, form="ankreuzen",
    grafik=tab(["1", "2", "3", "4"], ["4", "8", "12", "16"]),
    loesung="proportional – $4 : 1 = 8 : 2 = 12 : 3 = 16 : 4 = 4$",
    ergebnis="proportional", darstellung="tabelle", frage="erkennen",
    antwortform="ankreuzen")
assert set(p([2, 4, 6, 12], [18, 9, 6, 3])) == {36}
neu("A", "vorrat-gleich", 2, 2,
    aufgabe="Welcher Zuordnungstyp ist das? " + KREUZ3, form="ankreuzen",
    grafik=tab(["2", "4", "6", "12"], ["18", "9", "6", "3"]),
    loesung="antiproportional – Produkte $2 \\cdot 18 = 4 \\cdot 9 = "
    "6 \\cdot 6 = 12 \\cdot 3 = 36$",
    ergebnis="antiproportional", darstellung="tabelle", frage="erkennen",
    antwortform="ankreuzen")
xs, ys = [1, 2, 4, 5], [3, 5, 9, 11]
assert len(set(q(xs, ys))) > 1 and len(set(p(xs, ys))) > 1
neu("A", "vorrat-gleich", 2, 5,
    aufgabe="Welcher Zuordnungstyp ist das? " + KREUZ3, form="ankreuzen",
    grafik=tab(["1", "2", "4", "5"], ["3", "5", "9", "11"]),
    loesung="keins von beiden – Quotienten $3$, $2{,}5$; Produkte $3$, "
    "$10$; beide nicht gleich",
    ergebnis="keins von beiden", darstellung="tabelle", frage="erkennen",
    antwortform="ankreuzen")
neu("A", "vorrat-gleich", 2, 4,
    aufgabe="Schreib unter jeden Graphen: proportional, antiproportional "
    "oder keins von beiden.",
    form="text", antwort="(a) \\_\\_ \\ (b) \\_\\_ \\ (c) \\_\\_",
    grafik=graphen(["a", "kf", "p"], ["(a)", "(b)", "(c)"]),
    loesung="(a) fallende Kurve; (b) fallende Gerade, keine Kurve; "
    "(c) Gerade durch den Ursprung",
    ergebnis="(a) antiproportional \\ (b) keins \\ (c) proportional",
    darstellung="graph", frage="zuordnung", antwortform="zuordnen")
neu("A", "vorrat-gleich", 2, 6,
    aufgabe="Im Parkhaus kostet 1 Stunde 3\\,€, 2 Stunden kosten 5\\,€ und "
    "3 Stunden 7\\,€. Welcher Zuordnungstyp ist das? Begründe mit einer "
    "Rechnung.", form="text",
    loesung="Keins von beiden; Quotienten $3 : 1 = 3$, $5 : 2 = 2{,}5$; "
    "Produkte $1 \\cdot 3 = 3$, $2 \\cdot 5 = 10$; beide nicht gleich.",
    pruef="[3, 2.5, 3, 10]", ergebnis="keins von beiden", msf="ja",
    sache="Parkhaus", darstellung="text", frage="entscheidung",
    antwortform="begruenden")

# ---------------------------------------------------------------- B
assert R(320, 100) / 4 * 6 == R(480, 100) and R(4 * 9, 6) == 6
neu("B", "beispiel", 5, 3,
    aufgabe="(a) 4 Flaschen Wasser kosten 3{,}20\\,€. Was kosten "
    "6 Flaschen? \\ (b) Ein Wasservorrat reicht für 4 Wanderer 9 Tage. "
    "Wie lange reicht er für 6 Wanderer?",
    loesung="(a) proportional: $3{,}20 : 4 = 0{,}80$; $0{,}80 \\cdot 6 = "
    "4{,}80$\\,€. (b) antiproportional: $4 \\cdot 9 = 36$; $36 : 6 = 6$ "
    "Tage.", pruef="[0.8, 4.8, 36, 6]",
    schritte=[
        "(a) Doppelt so viele Flaschen kosten doppelt so viel: "
        "\\textbf{proportional}.",
        "Erst durch, dann mal: \\ $3{,}20 : 4 = 0{,}80$\\,€ für 1 Flasche; "
        "\\ $0{,}80 \\cdot 6 = 4{,}80$\\,€.",
        "(b) Doppelt so viele Wanderer: Der Vorrat reicht nur halb so "
        "lange: \\textbf{antiproportional}.",
        "Erst mal, dann durch: \\ $4 \\cdot 9 = 36$ Tage für 1 Wanderer; "
        "\\ $36 : 6 = 6$ Tage.",
    ],
    ergebnis="(a) 4{,}80\\,€ \\ (b) 6 Tage", sache="Wanderung",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(2, 5) * 8 == R(320, 100)
neu("B", "aufgabe", 5, 3,
    aufgabe="5 Brötchen kosten 2\\,€. Was kosten 8 Brötchen?",
    loesung="proportional: $2 : 5 = 0{,}40$; $0{,}40 \\cdot 8 = 3{,}20$\\,€",
    pruef="[0.4, 3.2]", ergebnis="3{,}20\\,€", sache="Brötchen",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(3 * 8, 4) == 6
neu("B", "aufgabe", 5, 3,
    aufgabe="3 gleiche Pumpen leeren einen Keller in 8 Stunden. Wie lange "
    "brauchen 4 solche Pumpen?",
    loesung="antiproportional: $3 \\cdot 8 = 24$; $24 : 4 = 6$\\,h",
    pruef="[24, 6]", ergebnis="6 Stunden", sache="Pumpen",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(12 * 20, 15) == 16
neu("B", "aufgabe", 5, 3,
    aufgabe="Mit 12\\,km/h braucht Lea für ihren Schulweg 20 Minuten. Wie "
    "lange braucht sie mit 15\\,km/h?",
    loesung="antiproportional (doppelt so schnell, halb so lange): "
    "$12 \\cdot 20 = 240$; $240 : 15 = 16$\\,min",
    pruef="[240, 16]", ergebnis="16 Minuten", sache="Schulweg",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(22, 4) * 6 == 33
neu("B", "aufgabe", 5, 3,
    aufgabe="Ein Läufer schafft 4\\,km in 22 Minuten. Wie lange braucht er "
    "bei gleichem Tempo für 6\\,km?",
    loesung="proportional (doppelt so weit, doppelt so lange): "
    "$22 : 4 = 5{,}5$; $5{,}5 \\cdot 6 = 33$\\,min",
    pruef="[5.5, 33]", ergebnis="33 Minuten", sache="Lauf",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(6 * 140, 8) == 105
neu("B", "ziel", 5, 4,
    aufgabe="Die Miete für ein Ferienhaus wird gleich aufgeteilt. Bei "
    "6 Freunden zahlt jeder 140\\,€. Nun kommen noch 2 Freunde mit. Lea hat "
    "100\\,€ gespart. Reicht das für ihren Anteil?",
    loesung="Nein; antiproportional: $6 \\cdot 140 = 840$; $840 : 8 = "
    "105$\\,€; $105 - 100 = 5$\\,€ fehlen.", pruef="[840, 105, 5]",
    ergebnis="Nein, ihr Anteil ist 105\\,€; es fehlen 5\\,€.", msf="ja",
    sache="Ferienhaus", darstellung="text", frage="entscheidung",
    antwortform="rechnen")
# Vorrat B
neu("B", "vorrat-leichter", 5, 3,
    aufgabe="3 Hefte kosten 6\\,€. Was kosten 6 Hefte?",
    loesung="proportional: doppelt so viele Hefte, $6 \\cdot 2 = 12$\\,€",
    pruef="12", ergebnis="12\\,€", sache="Hefte", darstellung="text",
    frage="laenge", antwortform="rechnen")
assert R(5 * 12, 6) == 10
neu("B", "vorrat-gleich", 5, 3,
    aufgabe="5 Bagger heben eine Baugrube in 12 Tagen aus. Wie lange "
    "brauchen 6 Bagger?",
    loesung="antiproportional: $5 \\cdot 12 = 60$; $60 : 6 = 10$ Tage",
    pruef="[60, 10]", ergebnis="10 Tage", sache="Bagger",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(1540, 100) / 7 * 3 == R(660, 100)
neu("B", "vorrat-gleich", 5, 3,
    aufgabe="7\\,kg Äpfel kosten 15{,}40\\,€. Was kosten 3\\,kg?",
    loesung="proportional: $15{,}40 : 7 = 2{,}20$; $2{,}20 \\cdot 3 = "
    "6{,}60$\\,€", pruef="[2.2, 6.6]", ergebnis="6{,}60\\,€",
    sache="Äpfel", darstellung="text", frage="laenge",
    antwortform="rechnen")
assert R(15, 10) / 6 * 10 == R(25, 10)
neu("B", "vorrat-gleich", 5, 3,
    aufgabe="Eine Wandergruppe schafft 6\\,km in 1{,}5 Stunden. Wie lange "
    "braucht sie bei gleichem Tempo für 10\\,km?",
    loesung="proportional: $1{,}5 : 6 = 0{,}25$; $0{,}25 \\cdot 10 = "
    "2{,}5$\\,h", pruef="[0.25, 2.5]", ergebnis="2{,}5 Stunden",
    sache="Wanderung", darstellung="text", frage="laenge",
    antwortform="rechnen")
assert R(25 * 18, 20) == R(45, 2)
neu("B", "vorrat-gleich", 5, 4,
    aufgabe="Der Bus zum Theater kostet für die Klasse einen festen Betrag, "
    "der gleich aufgeteilt wird. Bei 25 Schülern zahlt jeder 18\\,€. "
    "5 Schüler sind krank. Reichen 20\\,€ je Schüler?",
    loesung="Nein; antiproportional: $25 \\cdot 18 = 450$; $450 : 20 = "
    "22{,}50$\\,€; $22{,}50 > 20$.", pruef="[450, 22.5]",
    ergebnis="Nein, jeder zahlt 22{,}50\\,€.", msf="ja", sache="Bus",
    darstellung="text", frage="entscheidung", antwortform="rechnen")

# ---------------------------------------------------------------- C
assert 75 * 36 == 2700 and R(45 * 10, 5) == 90 and R(90, 60) == R(3, 2)
neu("C", "beispiel", 3, 5,
    aufgabe="(a) Ein Wasserkocher braucht im Jahr 75\\,kWh Strom. 1\\,kWh "
    "kostet 36\\,ct. Wie viel Euro kostet das? \\ (b) Eine Rolltreppe ist "
    "45\\,m lang und fährt 0{,}5\\,m/s. Wie viele Minuten dauert die Fahrt?",
    loesung="(a) $75 \\cdot 36 = 2700$\\,ct $= 27$\\,€. (b) $45 : 0{,}5 = "
    "90$\\,s $= 1{,}5$\\,min.", pruef="[2700, 27, 90, 1.5]",
    schritte=[
        "(a) Kosten = Menge $\\cdot$ Preis je kWh: \\ $75 \\cdot 36 = "
        "2700$\\,ct.",
        "100\\,ct sind 1\\,€: \\ $2700 : 100 = 27$. Das kostet 27\\,€.",
        "(b) Zeit = Weg $:$ Geschwindigkeit: \\ $45 : 0{,}5 = 90$\\,s.",
        "60\\,s sind 1\\,min: \\ $90 : 60 = 1{,}5$. Die Fahrt dauert "
        "1{,}5\\,min.",
    ],
    ergebnis="(a) 27\\,€ \\ (b) 1{,}5\\,min", sache="Strom, Rolltreppe",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert 12 * 35 == 420
neu("C", "aufgabe", 3, 5,
    aufgabe="Eine LED-Lampe braucht im Jahr 12\\,kWh. 1\\,kWh kostet "
    "35\\,ct. Wie viel Euro kostet der Strom im Jahr?",
    loesung="$12 \\cdot 35 = 420$\\,ct $= 4{,}20$\\,€", pruef="[420, 4.2]",
    ergebnis="4{,}20\\,€", sache="LED-Lampe", darstellung="text",
    frage="laenge", antwortform="rechnen")
assert R(900 * 10, 25) == 360 and R(360, 60) == 6
neu("C", "aufgabe", 3, 6,
    aufgabe="Ein Skilift ist 900\\,m lang und fährt 2{,}5\\,m/s. Wie viele "
    "Minuten dauert die Fahrt?",
    loesung="$900 : 2{,}5 = 360$\\,s; $360 : 60 = 6$\\,min",
    pruef="[360, 6]", ergebnis="6 Minuten", sache="Skilift",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert 4 * 4 == 16
neu("C", "aufgabe", 3, 3,
    aufgabe="Mila fährt mit dem Rad 4\\,km in 15 Minuten. Wie schnell fährt "
    "sie in km/h?",
    loesung="$15$\\,min $\\cdot 4 = 60$\\,min; $4$\\,km $\\cdot 4 = 16$\\,km "
    "in 1 Stunde", pruef="16", ergebnis="16\\,km/h", sache="Rad",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(18, 24) == R(3, 4) and R(3, 4) * 60 == 45
neu("C", "aufgabe", 3, 6,
    aufgabe="Ein Bus fährt 18\\,km mit durchschnittlich 24\\,km/h. Wie "
    "viele Minuten dauert die Fahrt?",
    loesung="$18 : 24 = 0{,}75$\\,h; $0{,}75 \\cdot 60 = 45$\\,min",
    pruef="[0.75, 45]", ergebnis="45 Minuten", sache="Bus",
    darstellung="text", frage="laenge", antwortform="rechnen")
alt_l, neu_l = R(12000, 100) * 6, R(12000, 100) * R(45, 10)
assert alt_l == 720 and neu_l == 540 and (alt_l - neu_l) * R(18, 10) == 324
neu("C", "ziel", 5, 4,
    aufgabe="Familie Berg fährt im Jahr 12\\,000\\,km. Ihr Auto braucht "
    "6\\,l Benzin auf 100\\,km, ein neues Auto nur 4{,}5\\,l. 1\\,l kostet "
    "1{,}80\\,€. Der Händler sagt: „Mit dem neuen Auto sparen Sie über "
    "300\\,€ im Jahr.“ Rechne nach und kreuze an. \\kreuz{Das stimmt.} "
    "\\kreuz{Das stimmt nicht.}", form="ankreuzen",
    loesung="Das stimmt. $12\\,000 : 100 = 120$; $120 \\cdot 6 = 720$\\,l; "
    "$120 \\cdot 4{,}5 = 540$\\,l; $720 - 540 = 180$\\,l; $180 \\cdot "
    "1{,}80 = 324$\\,€ $> 300$\\,€",
    pruef="[120, 720, 540, 180, 324]",
    ergebnis="Das stimmt: 324\\,€ gespart.", msf="ja", sache="Auto",
    darstellung="text", frage="entscheidung", antwortform="ankreuzen")
# Vorrat C
neu("C", "vorrat-leichter", 3, 1,
    aufgabe="Apfelsaft kostet 1{,}20\\,€ je Liter. Was kosten 5\\,l?",
    loesung="$5 \\cdot 1{,}20 = 6$\\,€", pruef="6", ergebnis="6\\,€",
    sache="Saft", darstellung="text", frage="laenge",
    antwortform="rechnen")
assert 150 * 34 == 5100
neu("C", "vorrat-gleich", 3, 5,
    aufgabe="Ein Kühlschrank braucht im Jahr 150\\,kWh. 1\\,kWh kostet "
    "34\\,ct. Wie viel Euro kostet der Strom im Jahr?",
    loesung="$150 \\cdot 34 = 5100$\\,ct $= 51$\\,€", pruef="[5100, 51]",
    ergebnis="51\\,€", sache="Kühlschrank", darstellung="text",
    frage="laenge", antwortform="rechnen")
assert R(1080, 4) == 270 and R(270, 60) == R(9, 2)
neu("C", "vorrat-gleich", 3, 6,
    aufgabe="Eine Seilbahn fährt 1\\,080\\,m mit 4\\,m/s. Wie viele Minuten "
    "dauert die Fahrt?",
    loesung="$1080 : 4 = 270$\\,s; $270 : 60 = 4{,}5$\\,min",
    pruef="[270, 4.5]", ergebnis="4{,}5 Minuten", sache="Seilbahn",
    darstellung="text", frage="laenge", antwortform="rechnen")
neu("C", "vorrat-gleich", 3, 3,
    aufgabe="Tom fährt mit dem Rad 5\\,km in 20 Minuten. Wie schnell fährt "
    "er in km/h?",
    loesung="$20$\\,min $\\cdot 3 = 60$\\,min; $5$\\,km $\\cdot 3 = 15$\\,km "
    "in 1 Stunde", pruef="15", ergebnis="15\\,km/h", sache="Rad",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(14, 21) * 60 == 40
neu("C", "vorrat-gleich", 3, 6,
    aufgabe="Eine Fähre fährt 14\\,km mit 21\\,km/h. Wie viele Minuten "
    "dauert die Überfahrt?",
    loesung="$14 : 21 = \\frac{2}{3}$\\,h; $\\frac{2}{3} \\cdot 60 = "
    "40$\\,min", pruef="40", ergebnis="40 Minuten", sache="Fähre",
    darstellung="text", frage="laenge", antwortform="rechnen")
gas, wp = 18000 * R(9, 100), 4500 * R(30, 100)
assert gas == 1620 and wp == 1350 and gas - wp == 270
neu("C", "vorrat-gleich", 5, 4,
    aufgabe="Ein Haus braucht im Jahr 18\\,000\\,kWh Gas zu 9\\,ct je kWh. "
    "Mit einer Wärmepumpe wären es 4\\,500\\,kWh Strom zu 30\\,ct je kWh. "
    "Der Installateur sagt: „Sie sparen über 250\\,€ im Jahr.“ Rechne nach "
    "und kreuze an. \\kreuz{Das stimmt.} \\kreuz{Das stimmt nicht.}",
    form="ankreuzen",
    loesung="Das stimmt. $18\\,000 \\cdot 9 = 162\\,000$\\,ct $= 1620$\\,€; "
    "$4500 \\cdot 30 = 135\\,000$\\,ct $= 1350$\\,€; $1620 - 1350 = "
    "270$\\,€ $> 250$\\,€", pruef="[1620, 1350, 270]",
    ergebnis="Das stimmt: 270\\,€ gespart.", msf="ja", sache="Heizung",
    darstellung="text", frage="entscheidung", antwortform="ankreuzen")

# ---------------------------------------------------------------- T
xs, ys = [10, 20, 40], [7, 9, 13]
assert len(set(q(xs, ys))) > 1 and len(set(p(xs, ys))) > 1
neu("T", "aufgabe", 2, 5,
    aufgabe="Ein Handytarif: Minuten $x$ und Preis $y$ in €. Welcher "
    "Zuordnungstyp ist das? " + KREUZ3, form="ankreuzen",
    grafik=tab(["10", "20", "40"], ["7", "9", "13"]),
    loesung="keins von beiden – Quotienten $0{,}7$, $0{,}45$; Produkte "
    "$70$, $180$; beide nicht gleich",
    ergebnis="keins von beiden", sache="Handytarif", darstellung="tabelle",
    frage="erkennen", antwortform="ankreuzen")
assert R(120, R(45, 3)) == 8
neu("T", "aufgabe", 5, 3,
    aufgabe="Ein Drucker druckt 45 Seiten in 3 Minuten. Wie lange braucht "
    "er für 120 Seiten?",
    loesung="proportional: $45 : 3 = 15$ Seiten je Minute; $120 : 15 = "
    "8$\\,min", pruef="[15, 8]", ergebnis="8 Minuten", sache="Drucker",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(8 * 15, 12) == 10
neu("T", "aufgabe", 5, 3,
    aufgabe="8 Maler streichen eine Schule in 15 Tagen. Wie viele Tage "
    "brauchen 12 Maler?",
    loesung="antiproportional: $8 \\cdot 15 = 120$; $120 : 12 = 10$ Tage",
    pruef="[120, 10]", ergebnis="10 Tage", sache="Maler",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(5400, 40) == 135
neu("T", "aufgabe", 3, 6,
    aufgabe="Ein Planschbecken fasst 5\\,400\\,l. Ein Schlauch füllt "
    "40\\,l je Minute. Wie lange dauert das Füllen in Stunden und Minuten?",
    loesung="$5400 : 40 = 135$\\,min; $135 - 120 = 15$, also 2\\,h 15\\,min",
    pruef="[135, 15]",
    ergebnis="2\\,h 15\\,min", sache="Planschbecken", darstellung="text",
    frage="laenge", antwortform="rechnen")
assert R(600, 25) == 24 and R(600, 30) == 20
neu("T", "ziel", 5, 4,
    aufgabe="Ein Verein fährt zum Spiel. Ein Bus kostet 600\\,€, die auf "
    "alle Mitfahrenden gleich verteilt werden. Mit der Bahn zahlt jeder "
    "22\\,€. Es fahren 25 Personen mit. Was ist für jeden günstiger? Ändert "
    "sich das, wenn 30 Personen mitfahren? Begründe mit einer Rechnung.",
    form="text",
    loesung="Bei 25: Bahn; Bus $600 : 25 = 24$\\,€ $> 22$\\,€. Bei 30: Bus; "
    "$600 : 30 = 20$\\,€ $< 22$\\,€.", pruef="[24, 20]",
    ergebnis="25 Personen: Bahn (Bus 24\\,€); 30 Personen: Bus (20\\,€)",
    msf="ja", sache="Bus und Bahn", darstellung="text",
    frage="entscheidung", antwortform="begruenden")
# Vorrat T
assert set(p([2, 3, 6], [15, 10, 5])) == {30}
neu("T", "vorrat-gleich", 2, 5,
    aufgabe="Welcher Zuordnungstyp ist das? " + KREUZ3, form="ankreuzen",
    grafik=tab(["2", "3", "6"], ["15", "10", "5"]),
    loesung="antiproportional – Produkte $2 \\cdot 15 = 3 \\cdot 10 = "
    "6 \\cdot 5 = 30$", ergebnis="antiproportional",
    darstellung="tabelle", frage="erkennen", antwortform="ankreuzen")
assert R(4 * 15, 6) == 10
neu("T", "vorrat-gleich", 5, 3,
    aufgabe="4 Lkw brauchen 15 Fahrten, um Erde abzufahren. Wie viele "
    "Fahrten brauchen 6 Lkw?",
    loesung="antiproportional: $4 \\cdot 15 = 60$; $60 : 6 = 10$ Fahrten",
    pruef="[60, 10]", ergebnis="10 Fahrten", sache="Lkw",
    darstellung="text", frage="laenge", antwortform="rechnen")
assert R(3600, 30) == 120
neu("T", "vorrat-gleich", 3, 6,
    aufgabe="Ein Tank fasst 3\\,600\\,l. Eine Pumpe schafft 30\\,l je "
    "Minute. Wie viele Stunden dauert das Füllen?",
    loesung="$3600 : 30 = 120$\\,min; $120 : 60 = 2$\\,h", pruef="[120, 2]",
    ergebnis="2 Stunden", sache="Tank", darstellung="text", frage="laenge",
    antwortform="rechnen")

if "--schreib" in sys.argv:
    roh = [z for z in open(BANK, encoding="utf-8").read().splitlines()
           if z.strip()]
    for a in zeilen:
        key = (a["kette_nr"], a["sprosse"], a["variante"])
        pos = len(roh)
        for i, z in enumerate(roh):
            b = json.loads(z)
            if (b["kette_nr"], b["sprosse"], b["variante"]) > key:
                pos = i
                break
        roh.insert(pos, json.dumps(a, ensure_ascii=False))
    open(BANK, "w", encoding="utf-8").write("\n".join(roh) + "\n")
json.dump(block, open("/root/work/w8c/tmp/block.json", "w"), indent=1)
print(len(zeilen), {k: (len(v["aufgaben"]), len(v["vorrat"]))
                    for k, v in block.items()})

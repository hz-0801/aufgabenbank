"""Nachzug bank/geraden auf die Mappe vom 29.09. (Katalog 2a296e5).

Einmalig. Liest den Bestand (27./28.09.), zieht quelle, sprosse,
id und sprosse_text nach, schreibt neue Vorstufen (e1 s-1, s0;
e3 s-1), die Grundfall-Päckchen und die Pflichtformen (P1, P2,
P4, P6, P8). Zählt je Einheit übernommen/neu/umgeschrieben/
entfallen und schreibt sie nach nachzug-zahlen.json (Scratch).

Aufruf: python3 werkzeuge/einmalig/nachzug-geraden-2026-09-29.py [e1 e2 …]
"""
import copy
import json
import sys
from pathlib import Path

B = Path(__file__).resolve().parents[2] / "bank" / "geraden"
E = "geraden"
QMAP = {40: 39, 103: 104, 101: 102, 104: 105, 105: 106, 106: 107}


def T(*k):
    """Tripel wie im Bestand: (2 | -1 | 0), Dezimalkomma {,}."""
    def f(x):
        s = f"{x:g}" if isinstance(x, float) else str(x)
        return s.replace(".", "{,}")
    return "(" + " | ".join(f(x) for x in k) + ")"


def M(s):
    return "$" + s + "$"


def lade(f):
    return [json.loads(l) for l in open(B / f"{f}.jsonl", encoding="utf-8")]


def schreibe(f, rows):
    with open(B / f"{f}.jsonl", "w", encoding="utf-8", newline="\n") as h:
        for r in rows:
            r = {k: v for k, v in r.items() if not k.startswith("_")}
            h.write(json.dumps(r, ensure_ascii=False) + "\n")


def reihe(rows, k, s):
    return [r for r in rows if r["kette_nr"] == k and r["sprosse"] == s]


def rid(r):
    s = r["sprosse"]
    st = f"s{s}" if s >= 0 else f"s-{-s}"
    return f"{E}-e{r['einheit']}-k{r['kette_nr']}-{st}-v{r['variante']}"


def neu(vorlage, art, **kw):
    r = copy.deepcopy(vorlage)
    r.update(kw)
    if vorlage["hoehe"] == "pflicht":
        r["merkmal"] = vorlage["merkmal"]
    r["_art"] = art
    r.setdefault("loesungsgrafik", "")
    r["id"] = rid(r)
    return r


def nachziehen(r, **kw):
    """Übernahme: nur id, sprosse, kette_nr, quelle, sprosse_text."""
    r = copy.deepcopy(r)
    r["quelle"] = QMAP.get(r["quelle"], r["quelle"])
    r.update(kw)
    r["_art"] = r.get("_art", "uebernommen")
    r["id"] = rid(r)
    return r


def fertig(rows):
    for r in rows:
        r["id"] = rid(r)
    return rows


# ---------------------------------------------------------------- e1
# Quader Q1 der Kette e1 k2 (Sek II: ein Körper mit festen Ecken).
Q1 = {"A": (1, 3, 0), "B": (6, 3, 0), "C": (6, 7, 0), "D": (1, 7, 0),
      "E": (1, 3, 3), "F": (6, 3, 3), "G": (6, 7, 3), "H": (1, 7, 3)}
Q1_TEXT = ("Der Quader $ABCDEFGH$ hat die Ecken " + ", ".join(
    f"${n}{T(*p)}$" for n, p in Q1.items()) + ".")
Q1_GRAFIK = ("\\begin{ksys3}[x1min=0,x1max=7,x2min=0,x2max=8,x3min=0,"
             "x3max=4] \\rquader{1,3,0}{5}{4}{3} " + " ".join(
                 f"\\rpunkt*{{{p[0]}}}{{{p[1]}}}{{{p[2]}}}{{{n}}}"
                 for n, p in Q1.items()) + " \\end{ksys3}")


def sub(p, q):
    return tuple(b - a for a, b in zip(p, q))


def e1():
    rows = lade("e1")
    out = []
    # k1 Erkennungsschritt: nur quelle
    out += [nachziehen(r) for r in reihe(rows, 1, 0)]
    # k2 s-2: alte Vorstufe „Punkt, Richtung, Parameter?“
    st_m2 = ("„Punkt, Richtung, Parameter?“ – an Parametergleichungen "
             "die drei Bauteile ankreuzen (wo steht der Stützpunkt, wo "
             "der Richtungsvektor, was läuft?); nichts rechnen")
    out += [nachziehen(r, sprosse=-2, sprosse_text=st_m2)
            for r in reihe(rows, 2, 0)]
    v0 = reihe(rows, 2, 0)[0]
    # k2 s-1 Wertetafel (neu)
    st_m1 = ("Wertetafel: zu fünf Parameterwerten (auch negativ und "
             "gebrochen) die Punkte ausrechnen und eintragen")
    werte = [-1, 0, 0.5, 1, 2]
    geraden = [("A", "G", "r"), ("B", "H", "s"), ("D", "F", "t"),
               ("E", "C", "r")]
    for v, (p, q, par) in enumerate(geraden, 1):
        st, u = Q1[p], sub(Q1[p], Q1[q])
        pkt = [tuple(a + w * b for a, b in zip(st, u)) for w in werte]
        pkt = [tuple(int(x) if float(x).is_integer() else x for x in pp)
               for pp in pkt]
        loes = "; ".join(
            f"Punkt für ${par} = {str(w).replace('.', '{,}')}$: {M(T(*pp))}"
            for w, pp in zip(werte, pkt))
        out.append(neu(v0, "neu", sprosse=-1, sprosse_text=st_m1,
            merkmal=("zu gegebenen Parameterwerten die Punkte "
                     "ausrechnen, auch für negative und gebrochene Werte"),
            variante=v, form="tabelle", antwort="",
            aufgabe=(Q1_TEXT + f" Die Gerade durch ${p}$ und ${q}$ hat "
                     f"die Gleichung $\\vec x = {T(*st)} + {par} \\cdot "
                     f"{T(*u)}$. Berechne die Punkte für die Parameterwerte "
                     "in der Tabelle und trage sie ein."),
            loesung=loes,
            pruef=json.dumps([x for pp in pkt for x in pp]),
            grafik=f"\\wertetabelle{{{par}}}{{Punkt}}{{-1,0,0{{,}}5,1,2}}",
            loesungsgrafik="", quelle=104, original=None))
    # k2 s0 Quaderkante (neu)
    st_0 = ("eine Gleichung lesen: zu welcher Kante oder Diagonale eines "
            "Quaders mit gegebenen Eckpunkten gehört sie?")
    fälle = [
        ("B", "G", ["Kante $BC$", "Flächendiagonale $BG$",
                    "Raumdiagonale $BH$"], "Flächendiagonale $BG$",
         "vom Stützpunkt $B$ aus ändern sich die zweite und die dritte "
         "Koordinate, die erste bleibt 6 – der Pfeil führt genau zu $G$"),
        ("H", "E", ["Kante $HE$", "Kante $HD$", "Flächendiagonale $HA$"],
         "Kante $HE$",
         "vom Stützpunkt $H$ aus ändert sich nur die zweite Koordinate, "
         "von 7 auf 3 – das ist die Kante zu $E$"),
        ("C", "E", ["Flächendiagonale $CA$", "Raumdiagonale $CE$",
                    "Flächendiagonale $CH$"], "Raumdiagonale $CE$",
         "vom Stützpunkt $C$ aus ändern sich alle drei Koordinaten – "
         "der Pfeil führt durch den Quader zur gegenüberliegenden Ecke $E$"),
        ("F", "H", ["Flächendiagonale $FH$", "Kante $FG$",
                    "Raumdiagonale $FD$"], "Flächendiagonale $FH$",
         "vom Stützpunkt $F$ aus bleibt die dritte Koordinate 3, die "
         "erste und die zweite ändern sich – der Pfeil führt in der "
         "Deckfläche zu $H$"),
    ]
    for v, (p, q, opt, rich, grund) in enumerate(fälle, 1):
        st, u = Q1[p], sub(Q1[p], Q1[q])
        out.append(neu(v0, "neu", sprosse=0, sprosse_text=st_0,
            merkmal=("an Stützpunkt und Richtungsvektor erkennen, welche "
                     "Kante oder Diagonale des Quaders die Gerade trägt"),
            variante=v, form="ankreuzen", antwort="",
            aufgabe=(Q1_TEXT + " Zu welcher Strecke des Quaders gehört die "
                     f"Gerade $\\vec x = {T(*st)} + t \\cdot {T(*u)}$? "
                     "Kreuze an. " + " \\\\ ".join(
                         f"\\kreuz{{{o}}}" for o in opt)),
            loesung=f"{rich} – {grund}", pruef="", grafik=Q1_GRAFIK,
            loesungsgrafik="", quelle=104, original=None))
    # k2 s1 Grundfall: Päckchen am Quader Q1, A bleibt, Ecke wandert
    g0 = reihe(rows, 2, 1)[0]
    for v, q in enumerate(["G", "C", "F", "H", "B"], 1):
        a, u = Q1["A"], sub(Q1["A"], Q1[q])
        out.append(neu(g0, "umgeschrieben", variante=v, sprosse=1,
            quelle=104,
            merkmal=("Stützpunkt A, Richtungsvektor als Verbindungsvektor; "
                     "der Quader und die Ecke A bleiben, die zweite Ecke "
                     "wandert"),
            aufgabe=(Q1_TEXT + " Stelle eine Gleichung der Geraden durch "
                     f"$A$ und ${q}$ auf."),
            loesung=(f"Stützpunkt: $A{T(*a)}$; Richtungsvektor: "
                     f"$\\overrightarrow{{A{q}}} = {T(*Q1[q])} - {T(*a)} = "
                     f"{T(*u)}$; Ergebnis: $\\vec x = {T(*a)} + r \\cdot "
                     f"{T(*u)}$"),
            pruef=json.dumps(list(a) + list(u)), grafik="",
            loesungsgrafik=""))
    for s in range(2, 7):
        out += [nachziehen(r) for r in reihe(rows, 2, s)]
    # k3 Pflicht
    f1, f2, f3 = reihe(rows, 3, 1)
    out.append(nachziehen(f1))
    out.append(neu(f2, "umgeschrieben", merkmal=(
        "fehlerfreie Vorlage: Teilpunkt aus dem Teilverhältnis richtig "
        "als Viertel gesetzt"),
        aufgabe=("Gesucht ist der Punkt $T$ auf der Strecke von "
                 "$A(1 | 3 | 0)$ nach $B(9 | -1 | 4)$ mit "
                 "$|AT| : |TB| = 1 : 3$. Nora rechnet: "
                 "$\\vec{OT} = (1 | 3 | 0) + \\tfrac{1}{4} \\cdot "
                 "(8 | -4 | 4) = (3 | 2 | 1)$. Prüfe, ob Nora richtig "
                 "gerechnet hat."),
        loesung=("Richtig. Das Verhältnis 1 : 3 teilt die Strecke in "
                 "$1 + 3 = 4$ gleiche Teile, $T$ liegt nach einem Viertel "
                 "des Verbindungsvektors."),
        pruef=""))
    out.append(neu(f3, "umgeschrieben", merkmal=(
        "Serie P1: an der gleichbleibenden Koordinate falsche Gleichungen "
        "erkennen, ohne genau zu rechnen"),
        aufgabe=("Vier Schüler haben eine Gleichung der Geraden durch "
                 "$A(2 | 5 | 1)$ und $B(2 | -1 | 4)$ aufgeschrieben: "
                 "(1) $\\vec x = (2 | 5 | 1) + r \\cdot (0 | -6 | 3)$; "
                 "(2) $\\vec x = (2 | 5 | 1) + r \\cdot (1 | -6 | 3)$; "
                 "(3) $\\vec x = (2 | -1 | 4) + r \\cdot (0 | 2 | -1)$; "
                 "(4) $\\vec x = (3 | 5 | 1) + r \\cdot (0 | -6 | 3)$. "
                 "Welche Ergebnisse können nicht stimmen? Begründe, ohne "
                 "genau zu rechnen."),
        loesung=("(2) kann nicht stimmen – $A$ und $B$ haben dieselbe "
                 "erste Koordinate, die erste Komponente des "
                 "Richtungsvektors muss 0 sein; (4) kann nicht stimmen – "
                 "jeder Punkt der Geraden hat die erste Koordinate 2, der "
                 "Stützpunkt hat 3."),
        pruef=""))
    b1, b2, b3 = reihe(rows, 3, 2)
    out.append(nachziehen(b1))
    out.append(neu(b2, "umgeschrieben", merkmal=(
        "Aussagenserie P4 zu Parametergleichungen, wahr oder falsch mit "
        "Gegenbeispiel"),
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. (1) Jede Gerade hat genau eine "
                 "Parametergleichung. (2) Durch zwei verschiedene Punkte "
                 "geht immer genau eine Gerade. (3) Eine Gerade, deren "
                 "Richtungsvektor eine Komponente null hat, geht nie durch "
                 "den Ursprung."),
        loesung=("(1) falsch, z. B. beschreiben $\\vec x = r \\cdot "
                 "(1 | 2 | 2)$ und $\\vec x = (1 | 2 | 2) + r \\cdot "
                 "(2 | 4 | 4)$ dieselbe Gerade; (2) wahr, denn der "
                 "Verbindungsvektor legt die Richtung fest und jeder der "
                 "beiden Punkte ist ein Stützpunkt; (3) falsch, z. B. geht "
                 "$\\vec x = r \\cdot (3 | 1 | 0)$ für $r = 0$ durch den "
                 "Ursprung."),
        pruef=""))
    out.append(neu(b3, "umgeschrieben", merkmal=(
        "Personenaussage P6: „liegt auf der Achse“ statt „parallel zur "
        "Achse“"),
        aufgabe=("Ole sagt: „Die Gerade durch $A(3 | -2 | 5)$ und "
                 "$B(3 | 4 | 5)$ liegt auf der $x_2$-Achse.“ Begründe, "
                 "ohne genau zu rechnen, ob Ole recht hat."),
        loesung=("Nein; $A$ und $B$ stimmen in der ersten und der dritten "
                 "Koordinate überein, die Gerade verläuft also parallel "
                 "zur $x_2$-Achse – auf der Achse liegen nur Punkte, deren "
                 "erste und dritte Koordinate null sind, $A$ hat aber 3 "
                 "und 5."),
        pruef=""))
    a1, a2, a3 = reihe(rows, 3, 3)
    out.append(nachziehen(a1))
    out.append(neu(a2, "umgeschrieben", merkmal=(
        "Anwendung P8: Entscheidung an einer Höhenmarke über den "
        "Parameter als Zeitanteil"),
        aufgabe=("Ein Kran hebt eine Last geradlinig und gleichmäßig in "
                 "8 s vom Boden bei $(6 | 2 | 0)$ auf ein Dach bei "
                 "$(2 | 10 | 16)$ (Angaben in m, $x_3$ ist die Höhe). "
                 "Neben dem Kran steht eine 9 m hohe Mauer. Ist die Last "
                 "nach 5 s schon höher als die Mauer?"),
        antwort="",
        loesung=("Ja; Anteil der Zeit: $t = \\tfrac{5}{8}$; Höhe: "
                 "$\\tfrac{5}{8} \\cdot 16 = 10$ m, und $10 > 9$ – die "
                 "Last ist 1 m höher als die Mauer."),
        pruef="10"))
    out.append(nachziehen(a3))
    out += [nachziehen(r) for r in reihe(rows, 3, 4)]
    return fertig(out), len(rows)


# ---------------------------------------------------------------- e2
def e2():
    rows = lade("e2")
    out = []
    st0 = ("„Aus welcher Koordinate der Parameter, an welcher die "
           "Probe?“ – zu Punktproben ankreuzen, welche Koordinate den "
           "Parameter liefert und welche den Widerspruch zeigen kann; "
           "nichts rechnen")
    out += [nachziehen(r, sprosse_text=st0) for r in reihe(rows, 1, 0)]
    g0 = reihe(rows, 1, 1)[0]
    # Päckchen: g bleibt, der Punkt wandert
    gl = "g\\colon \\vec x = (1 | 3 | -2) + r \\cdot (2 | -1 | 3)"
    punkte = [("P", (5, 1, 4)), ("Q", (7, 1, 7)), ("R", (-1, 4, -4)),
              ("S", (0, 3.5, -3.5)), ("U", (9, -1, 10))]
    for v, (n, p) in enumerate(punkte, 1):
        r = (p[0] - 1) / 2
        rs = f"{r:g}".replace(".", "{,}")
        y, z = 3 - r, -2 + 3 * r

        def zahl(x):
            return f"{x:g}".replace(".", "{,}")
        teil2 = (f"zweite Koordinate prüfen: $3 - {zahl(r) if r >= 0 else '(' + zahl(r) + ')'} = {zahl(y)}$")
        teil3 = (f"dritte Koordinate prüfen: $-2 + 3 \\cdot "
                 f"{zahl(r) if r >= 0 else '(' + zahl(r) + ')'} = {zahl(z)}$")
        ok2, ok3 = y == p[1], z == p[2]
        teil2 += " ✓" if ok2 else f", aber ${n}$ hat {zahl(p[1])} – Widerspruch"
        if ok2:
            teil3 += (" ✓" if ok3 else
                      f", aber ${n}$ hat {zahl(p[2])} – Widerspruch")
            teile = [teil2, teil3]
        else:
            teile = [teil2]
        erg = (f"${n}$ liegt auf $g$" if ok2 and ok3 else
               f"${n}$ liegt nicht auf $g$")
        loes = (f"Parameter aus der ersten Koordinate: $1 + 2r = "
                f"{zahl(p[0])}$, also $r = {rs}$; " + "; ".join(teile) +
                f"; Ergebnis: {erg}.")
        out.append(neu(g0, "umgeschrieben", variante=v, quelle=105,
            merkmal=("Parameter aus einer Koordinate, Probe in den "
                     "übrigen; die Gerade g bleibt, der Punkt wandert"),
            aufgabe=f"Prüfe, ob ${n}{T(*p)}$ auf ${gl}$ liegt.",
            loesung=loes, pruef=f"{r:g}", grafik="", loesungsgrafik=""))
    for s in range(2, 10):
        out += [nachziehen(r) for r in reihe(rows, 1, s)]
    out += [nachziehen(r) for r in reihe(rows, 2, 1)]
    f1, f2, f3 = reihe(rows, 3, 1)
    out.append(nachziehen(f1))
    out.append(neu(f2, "umgeschrieben", merkmal=(
        "fehlerfreie Vorlage: Abstand über die Länge des "
        "Richtungsvektors, nicht als Parameter"),
        aufgabe=("Gesucht ist ein Punkt auf $g\\colon \\vec x = "
                 "(4 | 0 | 1) + t \\cdot (-1 | 2 | 2)$, der vom Stützpunkt "
                 "den Abstand 6 hat. Jonas rechnet: "
                 "$|(-1 | 2 | 2)| = \\sqrt{1 + 4 + 4} = 3$, also "
                 "$t = 2$ und der Punkt $(2 | 4 | 5)$. Prüfe, ob Jonas "
                 "richtig gerechnet hat."),
        loesung=("Richtig. Ein Parameterschritt ist so lang wie der "
                 "Richtungsvektor, also 3; der Abstand 6 sind zwei "
                 "Schritte ($t = -2$ gäbe den zweiten solchen Punkt)."),
        pruef=""))
    out.append(neu(f3, "umgeschrieben", merkmal=(
        "Serie P1: an der konstanten Koordinate falsche Geradenpunkte "
        "erkennen, ohne genau zu rechnen"),
        aufgabe=("Vier Schüler haben einen Punkt der Geraden "
                 "$g\\colon \\vec x = (3 | -2 | 5) + r \\cdot (2 | 0 | -1)$ "
                 "angegeben: (1) $(7 | -2 | 3)$; (2) $(5 | -1 | 4)$; "
                 "(3) $(1 | -2 | 6)$; (4) $(3 | 2 | 5)$. Welche Ergebnisse "
                 "können nicht stimmen? Begründe, ohne genau zu rechnen."),
        loesung=("(2) kann nicht stimmen – die zweite Komponente des "
                 "Richtungsvektors ist 0, jeder Punkt von $g$ hat die "
                 "zweite Koordinate $-2$, der Punkt hat $-1$; (4) kann "
                 "nicht stimmen – zweite Koordinate 2 statt $-2$."),
        pruef=""))
    b1, b2, b3 = reihe(rows, 3, 2)
    out.append(nachziehen(b1))
    out.append(neu(b2, "umgeschrieben", merkmal=(
        "Aussagenserie P4 zu Punktprobe und Streckenparameter"),
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. (1) Jeder Punkt der Strecke von $A$ nach "
                 "$B$ hat in $\\vec x = \\vec{OA} + t \\cdot "
                 "\\overrightarrow{AB}$ einen Parameter zwischen null und "
                 "eins. (2) Liefert die erste Koordinate einen Parameter, "
                 "liegt der Punkt immer auf der Geraden. (3) Es gibt "
                 "Punktproben, bei denen eine Koordinate gar keinen "
                 "Parameter liefert."),
        loesung=("(1) wahr, denn $t = 0$ liefert $A$, $t = 1$ liefert $B$ "
                 "und die Werte dazwischen die Punkte dazwischen; "
                 "(2) falsch, z. B. liefert $P(2 | 0 | 0)$ an "
                 "$\\vec x = r \\cdot (1 | 1 | 1)$ aus der ersten "
                 "Koordinate $r = 2$, die zweite ergibt aber $2 \\ne 0$; "
                 "(3) wahr, denn ist eine Komponente des Richtungsvektors "
                 "null, fällt der Parameter in dieser Koordinate weg."),
        pruef=""))
    out.append(neu(b3, "umgeschrieben", merkmal=(
        "Personenaussage P6: aus einer Koordinate auf die Lage "
        "geschlossen, die konstante Koordinate übersehen"),
        aufgabe=("Emil sagt: „$P(5 | 10 | 3)$ liegt auf $g\\colon \\vec x = "
                 "(1 | 4 | 2) + r \\cdot (2 | 3 | 0)$, denn aus der ersten "
                 "Koordinate folgt $r = 2$, und die zweite passt auch.“ "
                 "Begründe, ohne genau zu rechnen, ob Emil recht hat."),
        loesung=("Nein; die dritte Komponente des Richtungsvektors ist 0, "
                 "jeder Punkt von $g$ hat die dritte Koordinate 2, $P$ hat "
                 "aber 3 – eine einzige Koordinate mit Widerspruch "
                 "genügt."),
        pruef=""))
    a1, a2, a3 = reihe(rows, 3, 3)
    out.append(neu(a1, "umgeschrieben", merkmal=(
        "Anwendung P8: Parameter aus der Bodenposition, Entscheidung an "
        "einer Höhenmarke"),
        aufgabe=("Ein Heißluftballon steigt geradlinig vom Startplatz im "
                 "Ursprung zum Punkt $B(300 | 400 | 1\\,200)$ (Angaben in "
                 "m, $x_3$ ist die Höhe). Im Punkt $(240 | 320 | 0)$ steht "
                 "ein 950 m hoher Sendemast. Fliegt der Ballon über die "
                 "Spitze des Masts hinweg?"),
        antwort="",
        loesung=("Ja; Parameter aus der ersten Koordinate: $300t = 240$, "
                 "also $t = 0{,}8$; zweite Koordinate prüfen: "
                 "$400 \\cdot 0{,}8 = 320$ ✓; Höhe über dem Mast: "
                 "$1\\,200 \\cdot 0{,}8 = 960$ m, und $960 > 950$ – der "
                 "Ballon ist dort 10 m über der Spitze."),
        pruef="[0.8, 960]"))
    out.append(nachziehen(a2))
    out.append(nachziehen(a3))
    return fertig(out), len(rows)


# ---------------------------------------------------------------- e3
Q3 = {"A": (1, 0, 0), "B": (5, 0, 0), "C": (5, 3, 0), "D": (1, 3, 0),
      "E": (1, 0, 4), "F": (5, 0, 4), "G": (5, 3, 4), "H": (1, 3, 4)}
Q3_TEXT = ("Der Quader $ABCDEFGH$ hat die Ecken " + ", ".join(
    f"${n}{T(*p)}$" for n, p in Q3.items()) + ".")
Q3_GRAFIK = ("\\begin{ksys3}[x1min=0,x1max=6,x2min=0,x2max=4,x3min=0,"
             "x3max=5] \\rquader{1,0,0}{4}{3}{4} " + " ".join(
                 f"\\rpunkt*{{{p[0]}}}{{{p[1]}}}{{{p[2]}}}{{{n}}}"
                 for n, p in Q3.items()) + " \\end{ksys3}")


def e3():
    rows = lade("e3")
    out = []
    v0 = reihe(rows, 1, 0)[0]
    st_m1 = ("Lagen am Quader: zu einer Kante je eine schneidende, eine "
             "parallele und eine windschiefe Kante zeigen, ohne Rechnung")
    lagen = [
        ("AB", "$AD$, $AE$, $BC$ oder $BF$", "$DC$, $EF$ oder $HG$",
         "$DH$, $CG$, $EH$ oder $FG$"),
        ("AE", "$AB$, $AD$, $EF$ oder $EH$", "$BF$, $CG$ oder $DH$",
         "$BC$, $CD$, $FG$ oder $GH$"),
        ("FG", "$FB$, $FE$, $GC$ oder $GH$", "$BC$, $AD$ oder $EH$",
         "$AB$, $DC$, $AE$ oder $DH$"),
        ("DH", "$DA$, $DC$, $HE$ oder $HG$", "$AE$, $BF$ oder $CG$",
         "$AB$, $BC$, $EF$ oder $FG$"),
    ]
    for v, (k, sch, par, wind) in enumerate(lagen, 1):
        out.append(neu(v0, "neu", sprosse=-1, sprosse_text=st_m1,
            merkmal=("die drei Lagen an Kanten eines Quaders zeigen, ohne "
                     "Rechnung"),
            variante=v, form="text", antwort="",
            aufgabe=(Q3_TEXT + f" Nenne zur Kante ${k}$ eine Kante, die "
                     f"${k}$ schneidet, eine, die zu ${k}$ parallel ist, "
                     f"und eine, die zu ${k}$ windschief ist."),
            loesung=(f"schneidend: {sch}; parallel: {par}; windschief: "
                     f"{wind}"),
            pruef="", grafik=Q3_GRAFIK, loesungsgrafik="", quelle=106,
            original=None))
    st0 = ("„Identisch, parallel, windschief oder schneidend?“ – zu "
           "Geradenpaaren ankreuzen, welche Merkmale zu prüfen sind "
           "(Richtungsvektoren, Stützpunktprobe, gemeinsame Ebene); "
           "nichts rechnen")
    out += [nachziehen(r, sprosse_text=st0) for r in reihe(rows, 1, 0)]
    g0 = reihe(rows, 1, 1)[0]
    a = Q3["A"]
    ug = sub(a, Q3["G"])
    for v, q in enumerate(["C", "H", "F", "E", "D"], 1):
        uh = sub(a, Q3[q])
        # Faktor aus der ersten Nicht-Null-Komponente von uh
        ks = []
        for j in range(3):
            ks.append(None if ug[j] == 0 else uh[j] / ug[j])
        zeilen = []
        namen = ["ersten", "zweiten", "dritten"]
        gesehen = []
        for j in range(3):
            k = ks[j]
            kstr = f"{k:g}".replace(".", "{,}") if k == int(k) else \
                f"\\tfrac{{{uh[j]}}}{{{ug[j]}}}"
            zeilen.append(f"Faktor aus der {namen[j]} Koordinate: "
                          f"${uh[j]} = k \\cdot {ug[j]}$, also $k = {kstr}$")
            gesehen.append(k)
            if len(set(gesehen)) > 1:
                break
        loes = ("; ".join(zeilen) +
                "; Ergebnis: verschiedene Faktoren, "
                f"${T(*uh)}$ ist kein Vielfaches von ${T(*ug)}$ – $g$ und "
                "$h$ sind nicht identisch, sie schneiden sich im "
                "gemeinsamen Stützpunkt $A$.")
        ks_p = [k for k in gesehen]
        out.append(neu(g0, "umgeschrieben", variante=v, quelle=106,
            merkmal=("gemeinsamer Stützpunkt, Richtungsvektoren nicht "
                     "kollinear; der Quader und g durch A und G bleiben, "
                     "die Richtung von h wandert"),
            aufgabe=(Q3_TEXT + f" Die Gerade $g$ geht durch $A$ und $G$, "
                     f"die Gerade $h$ durch $A$ und ${q}$: "
                     f"$g\\colon \\vec x = {T(*a)} + r \\cdot {T(*ug)}$, "
                     f"$h\\colon \\vec x = {T(*a)} + t \\cdot {T(*uh)}$. "
                     "Begründe, dass $g$ und $h$ nicht identisch sind."),
            loesung=loes, pruef=json.dumps(ks_p), grafik="",
            loesungsgrafik=""))
    for s in range(2, 7):
        out += [nachziehen(r) for r in reihe(rows, 1, s)]
    f1, f2, f3 = reihe(rows, 2, 1)
    out.append(nachziehen(f1))
    out.append(neu(f2, "umgeschrieben", merkmal=(
        "fehlerfreie Vorlage: Identität über kollineare Richtungen und "
        "Stützpunktprobe"),
        aufgabe=("Gegeben sind $g\\colon \\vec x = (2 | 0 | 1) + r \\cdot "
                 "(1 | -2 | 2)$ und $h\\colon \\vec x = (4 | -4 | 5) + t "
                 "\\cdot (-2 | 4 | -4)$. Paula schreibt: „$(-2 | 4 | -4) = "
                 "-2 \\cdot (1 | -2 | 2)$, die Richtungen sind kollinear. "
                 "$(4 | -4 | 5) - (2 | 0 | 1) = (2 | -4 | 4) = 2 \\cdot "
                 "(1 | -2 | 2)$, der Stützpunkt von $h$ liegt auf $g$. "
                 "Also sind $g$ und $h$ identisch.“ Prüfe, ob Paula richtig "
                 "gerechnet hat."),
        loesung=("Richtig. Kollineare Richtungsvektoren und ein Stützpunkt "
                 "der einen Geraden auf der anderen – das ist genau die "
                 "Bedingung für identische Geraden."),
        pruef=""))
    out.append(neu(f3, "umgeschrieben", merkmal=(
        "Serie P1: aus kollinearen Richtungen die unmöglichen Lagen "
        "erkennen, ohne genau zu rechnen"),
        aufgabe=("Vier Schüler haben die Lage von $g\\colon \\vec x = "
                 "(2 | 3 | 1) + r \\cdot (2 | 1 | 3)$ und $h\\colon \\vec x "
                 "= (0 | 5 | 1) + t \\cdot (4 | 2 | 6)$ angegeben: "
                 "(1) schneidend; (2) windschief; (3) echt parallel; "
                 "(4) identisch. Welche Ergebnisse können nicht stimmen? "
                 "Begründe, ohne genau zu rechnen."),
        loesung=("(1) kann nicht stimmen – $(4 | 2 | 6)$ ist das Doppelte "
                 "von $(2 | 1 | 3)$, parallele Geraden haben keinen "
                 "einzelnen Schnittpunkt; (2) kann nicht stimmen – "
                 "windschiefe Geraden haben nicht kollineare "
                 "Richtungsvektoren; (3) und (4) sind ohne Rechnung "
                 "möglich, erst die Stützpunktprobe entscheidet (hier: echt "
                 "parallel)."),
        pruef=""))
    b1, b2, b3 = reihe(rows, 2, 2)
    out.append(nachziehen(b1))
    out.append(neu(b2, "umgeschrieben", merkmal=(
        "Personenaussage P6: gleiche Richtungsvektoren als Identität "
        "gelesen"),
        aufgabe=("Mila sagt: „$g\\colon \\vec x = (1 | 0 | 2) + r \\cdot "
                 "(3 | 1 | 1)$ und $h\\colon \\vec x = (1 | 0 | 6) + t "
                 "\\cdot (3 | 1 | 1)$ haben denselben Richtungsvektor, also "
                 "sind sie identisch.“ Begründe, ohne genau zu rechnen, ob "
                 "Mila recht hat."),
        loesung=("Nein; gleiche Richtungsvektoren zeigen nur, dass die "
                 "Geraden parallel sind. Die Stützpunkte unterscheiden "
                 "sich nur in der dritten Koordinate, ihr "
                 "Verbindungsvektor $(0 | 0 | 4)$ ist kein Vielfaches von "
                 "$(3 | 1 | 1)$ – $g$ und $h$ sind echt parallel."),
        pruef=""))
    out.append(neu(b3, "umgeschrieben", merkmal=(
        "Aussagenserie P4 zu Parallelität, Schnitt und Windschiefe"),
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. (1) Zwei Geraden mit kollinearen "
                 "Richtungsvektoren sind nie windschief. (2) Zwei Geraden "
                 "ohne gemeinsamen Punkt sind immer parallel. (3) Es gibt "
                 "zwei verschiedene Geraden mit demselben Richtungsvektor, "
                 "die sich in genau einem Punkt schneiden."),
        loesung=("(1) wahr, denn kollineare Richtungen heißen parallel, "
                 "und windschief verlangt nicht parallele Richtungen; "
                 "(2) falsch, z. B. haben $\\vec x = r \\cdot (1 | 0 | 0)$ "
                 "und $\\vec x = (0 | 0 | 1) + t \\cdot (0 | 1 | 0)$ keinen "
                 "gemeinsamen Punkt und sind nicht parallel, also "
                 "windschief; (3) falsch, z. B. sind zwei Geraden mit "
                 "gleicher Richtung und einem gemeinsamen Punkt schon "
                 "identisch."),
        pruef=""))
    return fertig(out), len(rows)


# ---------------------------------------------------------------- e4
def e4():
    rows = lade("e4")
    out = []
    out += [nachziehen(r) for r in reihe(rows, 1, 0)]
    g0 = reihe(rows, 1, 1)[0]
    m = (0, 0, 12)
    anker = [(6, 8, 0), (-4, 3, 0), (9, -12, 0), (-5, -12, 0), (0, -7, 0)]
    for v, x in enumerate(anker, 1):
        u = sub(m, x)
        out.append(neu(g0, "umgeschrieben", variante=v, quelle=107,
            merkmal=("Sachpunkte als Stützpunkt und Richtungsvektor, "
                     "Strecke mit Parameterbereich; die Mastspitze bleibt, "
                     "der Bodenanker wandert"),
            aufgabe=("Von der Spitze $M(0 | 0 | 12)$ eines Masts führt ein "
                     f"gespanntes Seil zum Bodenanker $X{T(*x)}$ (1 LE = "
                     "1 m). Gib eine Gleichung der Seilstrecke an."),
            loesung=(f"Stützpunkt: $M(0 | 0 | 12)$; Richtungsvektor: "
                     f"$\\overrightarrow{{MX}} = {T(*x)} - (0 | 0 | 12) = "
                     f"{T(*u)}$; Parameterbereich: Mast bei $t = 0$, Anker "
                     f"bei $t = 1$; Ergebnis: $\\vec x = (0 | 0 | 12) + t "
                     f"\\cdot {T(*u)}$ mit $0 \\le t \\le 1$"),
            pruef=json.dumps(list(m) + list(u)), grafik="",
            loesungsgrafik=""))
    for s in range(2, 5):
        out += [nachziehen(r) for r in reihe(rows, 1, s)]
    out += [nachziehen(r) for r in reihe(rows, 2, 1)]
    f1, f2, f3 = reihe(rows, 3, 1)
    out.append(nachziehen(f1))
    out.append(neu(f2, "umgeschrieben", merkmal=(
        "fehlerfreie Vorlage: Neigung über den Horizontalabstand der "
        "Fußpunkte"),
        aufgabe=("Ein Seil ist an zwei Masten mit den Fußpunkten "
                 "$F_1(0 | 0 | 0)$ und $F_2(6 | 8 | 0)$ in 9 m und in 6 m "
                 "Höhe befestigt (1 LE = 1 m). Karl rechnet: "
                 "Horizontalabstand $\\sqrt{36 + 64} = 10$ m, "
                 "Höhendifferenz $9 - 6 = 3$ m, Neigung $\\frac{3}{10} = "
                 "30\\,\\%$. Prüfe, ob Karl richtig gerechnet hat."),
        loesung=("Richtig. Die Neigung ist die Höhendifferenz geteilt "
                 "durch den Horizontalabstand der Fußpunkte, nicht durch "
                 "die Seillänge."),
        pruef=""))
    out.append(neu(f3, "umgeschrieben", merkmal=(
        "Serie P1: Höhen außerhalb der Befestigungshöhen erkennen, ohne "
        "genau zu rechnen"),
        aufgabe=("Ein Seil ist geradlinig von $(0 | 0 | 20)$ nach "
                 "$(30 | 40 | 5)$ gespannt (1 LE = 1 m). Vier Schüler "
                 "geben an, wie hoch das Seil über dem Bodenpunkt "
                 "$(15 | 20 | 0)$ hängt: (1) $12{,}5$ m; (2) 25 m; "
                 "(3) 3 m; (4) 30 m. Welche Ergebnisse können nicht "
                 "stimmen? Begründe, ohne genau zu rechnen."),
        loesung=("(2) und (4) können nicht stimmen – kein Seilpunkt liegt "
                 "höher als der obere Befestigungspunkt in 20 m Höhe; "
                 "(3) kann nicht stimmen – kein Seilpunkt liegt tiefer als "
                 "der untere in 5 m Höhe."),
        pruef=""))
    b1, b2, b3 = reihe(rows, 3, 2)
    out.append(nachziehen(b1))
    out.append(neu(b2, "umgeschrieben", merkmal=(
        "Personenaussage P6: Maßstab und Neigung"),
        aufgabe=("Nils sagt: „Ein Seil hat 4 LE Höhendifferenz auf 16 LE "
                 "Horizontalabstand. Seine Neigung in Prozent hängt davon "
                 "ab, ob 1 LE 1 m oder 10 m ist.“ Begründe, ohne genau zu "
                 "rechnen, ob Nils recht hat."),
        loesung=("Nein; die Neigung ist Höhendifferenz durch "
                 "Horizontalabstand, beide Längen werden mit demselben "
                 "Maßstab umgerechnet, der Faktor kürzt sich – sie bleibt "
                 "25\\,\\%."),
        pruef=""))
    out.append(neu(b3, "umgeschrieben", merkmal=(
        "Aussagenserie P4 zu senkrecht übereinander, Neigung und "
        "waagerechten Seilen"),
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. (1) Zwei Punkte, die senkrecht "
                 "übereinander liegen, haben immer dieselbe erste und "
                 "dieselbe zweite Koordinate. (2) Die Neigung einer Strecke "
                 "ist nie größer als 100\\,\\%. (3) Es gibt Seilstrecken, "
                 "deren Punkte alle gleich hoch liegen."),
        loesung=("(1) wahr, denn nur die dritte Koordinate, die Höhe, "
                 "unterscheidet sie; (2) falsch, z. B. hat eine Strecke "
                 "mit 3 m Höhendifferenz auf 2 m Horizontalabstand die "
                 "Neigung 150\\,\\%; (3) wahr, denn hat der Richtungsvektor "
                 "die dritte Komponente null, etwa $(4 | 3 | 0)$, bleibt "
                 "die Höhe gleich."),
        pruef=""))
    a1, a2, a3 = reihe(rows, 3, 3)
    out.append(nachziehen(a1))
    out.append(nachziehen(a2))
    out.append(neu(a3, "umgeschrieben", merkmal=(
        "Anwendung P8: senkrecht übereinander, Entscheidung an einer "
        "Mindestdicke"),
        aufgabe=("Ein Tunnel soll geradlinig von $E(0 | 0 | 320)$ nach "
                 "$A(1\\,200 | 500 | 190)$ gebaut werden (Angaben in m, "
                 "$x_3$ ist die Höhe). Senkrecht über dem Tunnel liegt ein "
                 "Brunnen, dessen Sohle bei $(600 | 250 | 280)$ liegt. "
                 "Zwischen Brunnensohle und Tunnel müssen mindestens 20 m "
                 "Gestein bleiben. Ist das eingehalten?"),
        antwort="",
        loesung=("Ja; Parameter aus der ersten und zweiten Koordinate: "
                 "$1\\,200t = 600$ und $500t = 250$, also $t = 0{,}5$; "
                 "Tunnelhöhe: $320 - 130 \\cdot 0{,}5 = 255$ m; Abstand: "
                 "$280 - 255 = 25$ m, und $25 > 20$."),
        pruef="[0.5, 255, 25]"))
    return fertig(out), len(rows)


def zahlen(out, alt):
    z = {"uebernommen": 0, "neu": 0, "umgeschrieben": 0}
    for r in out:
        z[r["_art"]] += 1
    z["entfallen"] = alt - z["uebernommen"] - z["umgeschrieben"]
    return z


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["e1", "e2", "e3", "e4"]
    fn = {"e1": e1, "e2": e2, "e3": e3, "e4": e4}
    zf = B.parent.parent / "werkzeuge" / "einmalig" / "nachzug-geraden-zahlen.json"
    try:
        alle = json.loads(zf.read_text(encoding="utf-8"))
    except FileNotFoundError:
        alle = {}
    for e in wahl:
        out, alt = fn[e]()
        alle[e] = zahlen(out, alt)
        schreibe(e, out)
        print(e, len(out), alle[e])
    zf.write_text(json.dumps(alle, ensure_ascii=False, indent=1) + "\n",
                  encoding="utf-8")

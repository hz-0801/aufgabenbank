"""Nachzug bank/skalarprodukt-und-winkel auf die Mappe vom 29.09.
(Katalog 2a296e5).

Einmalig. Liest den Bestand vom 27.09., zieht quelle (96 -> 94,
97 -> 95, 98 -> 96, 99 -> 97, 41 -> 39), sprosse, id und
sprosse_text nach, schreibt die neue Vorstufe e1 s0 (Quader ohne
Koordinaten; die alte Vorstufe wird s-1), die vier Grundfall-
Päckchen (je ein Körper mit festen Ecken) und die Pflichtformen
(P1, P2, P3, P4, P6) durch Umschreiben vorhandener fehler- und
begruenden-Zeilen. Zählt je Einheit übernommen/neu/umgeschrieben/
entfallen und druckt die Zahlen.

Aufruf: python3 werkzeuge/einmalig/nachzug-skalarprodukt-und-winkel-2026-09-29.py [e1 e2 …]
"""
import copy
import json
import math
import sys
from pathlib import Path

E = "skalarprodukt-und-winkel"
B = Path(__file__).resolve().parents[2] / "bank" / E
QMAP = {96: 94, 97: 95, 98: 96, 99: 97, 41: 39}

ST = {
    ("e1", 1, -1): "„Zahl oder Vektor?“ – zu Ausdrücken mit "
    "Skalarprodukt ankreuzen, was herauskommt (Vektor, Zahl, nichts "
    "Definiertes); nichts rechnen",
    ("e1", 1, 0): "Skalarprodukt aus Längen und Winkel an einer Figur "
    "mit bekannten Winkeln (gleichseitiges Dreieck, Quader), ohne "
    "Koordinaten; das Vorzeichen aus dem Winkel ablesen",
    ("e2", 2, 6): "die Innenwinkel über die Gleichseitigkeit statt "
    "dreier Einzelrechnungen bestimmen (iqb 2023MerhoehtBAGLAA1WTR-2a, "
    "Niveau II) und den stumpfen Innenwinkel des Zelts über den "
    "Nebenwinkel der Normalenrechnung",
    ("e2", 3, 3): "Winkel zwischen zwei Kanten über das Skalarprodukt "
    "berechnen",
    ("e3", 1, 0): "„Kosinus oder Sinus?“ – ankreuzen, ob der Kosinus "
    "(Vektor gegen Vektor, Ebene gegen Ebene) oder der Sinus (Gerade "
    "gegen Ebene) gehört, dazu „Der Formelwinkel oder sein Nachbar?“ "
    "ankreuzen; nichts rechnen",
    ("e3", 1, 5): "den Grenzwinkel einer Drehung als Ebenenwinkel "
    "ansetzen und erläutern (iqb 2026MgrundlegendBAGLAA2WTR1-1e, "
    "Niveau III) und den stumpfen Zeltwinkel vollständig führen",
    ("e3", 2, 3): "Neigungswinkel einer Ebene gegen eine "
    "Koordinatenebene über die Normalenvektoren berechnen",
    ("e4", 1, 0): "„Kosinus oder Sinus?“ – ankreuzen, ob der Kosinus "
    "(Vektor gegen Vektor, Ebene gegen Ebene) oder der Sinus (Gerade "
    "gegen Ebene) gehört; nichts rechnen",
    ("e4", 3, 3): "Schnittwinkel zwischen Gerade und Ebene über "
    "Richtungs- und Normalenvektor berechnen",
}


def T(*k, a=False):
    """Tripel: in aufgabe mit \\mid, in loesung mit |."""
    def f(x):
        s = f"{x:g}" if isinstance(x, float) else str(x)
        return s.replace(".", "{,}")
    sep = " \\mid " if a else " | "
    return "(" + sep.join(f(x) for x in k) + ")"


def P(name, *k):
    return f"${name}{T(*k, a=True)}$"


def grad(w):
    return f"{w:.1f}".replace(".", "{,}")


def lade(f):
    return [json.loads(l) for l in open(B / f"{f}.jsonl", encoding="utf-8")]


def schreibe(f, rows):
    with open(B / f"{f}.jsonl", "w", encoding="utf-8", newline="\n") as h:
        for r in rows:
            r = {k: v for k, v in r.items() if not k.startswith("_")}
            h.write(json.dumps(r, ensure_ascii=False) + "\n")


def rid(r):
    s = r["sprosse"]
    st = f"s{s}" if s >= 0 else f"s-{-s}"
    return f"{E}-e{r['einheit']}-k{r['kette_nr']}-{st}-v{r['variante']}"


def nachziehen(r, f, **kw):
    """Übernahme: nur id, sprosse, kette_nr, quelle, sprosse_text."""
    r = copy.deepcopy(r)
    r["quelle"] = QMAP.get(r["quelle"], r["quelle"])
    r.update(kw)
    key = (f, r["kette_nr"], r["sprosse"])
    if key in ST:
        r["sprosse_text"] = ST[key]
    r.setdefault("_art", "uebernommen")
    r["id"] = rid(r)
    return r


def um(r, art="umgeschrieben", **kw):
    """Umschreiben: aufgabe/antwort/loesung/pruef/form neu."""
    r = copy.deepcopy(r)
    r.update(kw)
    r["_art"] = art
    r["id"] = rid(r)
    return r


def zaehle(f, alt, neu):
    z = {"uebernommen": 0, "neu": 0, "umgeschrieben": 0}
    for r in neu:
        z[r["_art"]] += 1
    z["entfallen"] = len(alt) - z["uebernommen"] - z["umgeschrieben"]
    print(f, z)
    return z


def wo(rows, k, s, v=None):
    out = [r for r in rows if r["kette_nr"] == k and r["sprosse"] == s]
    if v is None:
        return out
    return [r for r in out if r["variante"] == v][0]


def fertig(rows):
    for r in rows:
        r["id"] = rid(r)
    return rows


# ---------------------------------------------------------------- e1
# Quader Q1 (fest): A(1|2|0) … H(1|4|2), AB = 4, AD = 2, AE = 2.
Q1 = {"A": (1, 2, 0), "B": (5, 2, 0), "C": (5, 4, 0), "D": (1, 4, 0),
      "E": (1, 2, 2), "F": (5, 2, 2), "G": (5, 4, 2), "H": (1, 4, 2)}


def vek(p, q, K):
    return tuple(b - a for a, b in zip(K[p], K[q]))


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def betr(u):
    return math.sqrt(dot(u, u))


def k(x):
    """Negative Faktoren in Klammern: 4 · (-2)."""
    return f"({x})" if x < 0 else str(x)


def q1_text():
    e = Q1
    return ("Ein Quader hat die Ecken " + ", ".join(
        P(n, *e[n]) for n in "ABCD") + " und darüber " + ", ".join(
        P(n, *e[n]) for n in "EFG") + " und " + P("H", *e["H"]) + ".")


def e1(alt):
    neu = []
    for r in wo(alt, 1, 0):
        neu.append(nachziehen(r, "e1", sprosse=-1))
    # s0 neu: Quader ohne Koordinaten
    vor = wo(alt, 1, 0, 1)
    s0 = [
        ("AB", "AD", 4, 2, 90, "rechter Winkel, Skalarprodukt null"),
        ("AE", "DH", 2, 2, 0, "gleiche Richtung"),
        ("AB", "BA", 4, 4, 180, "Gegenrichtung"),
        ("AD", "CB", 2, 2, 180, "Gegenrichtung"),
    ]
    for i, (u, v, lu, lv, w, _) in enumerate(s0, 1):
        wert = round(lu * lv * math.cos(math.radians(w)))
        art = ("rechter Winkel" if wert == 0 else
               "spitzer Winkel" if wert > 0 else "stumpfer Winkel")
        vz = "null" if wert == 0 else "positiv" if wert > 0 else "negativ"
        r = um(vor, "neu", sprosse=0, variante=i, form="teil",
               sprosse_text=ST[("e1", 1, 0)],
               merkmal="Vorstufe: Skalarprodukt aus Längen und "
               "bekanntem Winkel, ohne Koordinaten",
               aufgabe=("Ein Quader ABCDEFGH hat die Kantenlängen "
                        "AB = 4, AD = 2 und AE = 2. Berechne ohne "
                        f"Koordinaten $\\overrightarrow{{{u}}} \\circ "
                        f"\\overrightarrow{{{v}}}$ und gib an, ob das "
                        "Skalarprodukt positiv, null oder negativ ist."),
               antwort="Skalarprodukt: \\leerfeld \\quad Vorzeichen: "
               "\\leerfeld",
               loesung=(f"Winkel zwischen den Pfeilen: ${w}^\\circ$; "
                        f"Winkelform: ${lu} \\cdot {lv} \\cdot "
                        f"\\mathrm{{cos}}\\,{w}^\\circ = {wert}$; "
                        f"Ergebnis: ${wert}$, {vz} ({art})"),
               pruef=str(wert), original=None, grafik="",
               loesungsgrafik="", quelle=94)
        neu.append(r)
    # s1 Grundfall: Päckchen am Quader Q1, AG fest, zweiter Vektor wandert
    g = wo(alt, 1, 1)
    zweite = [("D", "F"), ("D", "E"), ("B", "H"), ("C", "E"),
              ("B", "D")]
    u = vek("A", "G", Q1)
    for i, (p, q) in enumerate(zweite, 1):
        v = vek(p, q, Q1)
        s = dot(u, v)
        art = ("spitzer Winkel" if s > 0 else "rechter Winkel"
               if s == 0 else "stumpfer Winkel")
        rel = ">" if s > 0 else "=" if s == 0 else "<"
        prod = " + ".join(f"{k(a)} \\cdot {k(b)}" for a, b in zip(u, v))
        if i < 5:
            auf = (q1_text() + " Berechne $\\overrightarrow{AG} \\circ "
                   f"\\overrightarrow{{{p}{q}}}$ und gib an, ob der "
                   "Winkel zwischen den beiden Vektoren spitz, recht "
                   "oder stumpf ist.")
            erg = f"Ergebnis: ${s} {rel} 0$: {art}" if s else \
                f"Ergebnis: ${s}$: {art}"
            orig = None
            ant = "Skalarprodukt: \\leerfeld \\quad Winkel: \\leerfeld"
        else:
            auf = (q1_text() + " Berechne $\\overrightarrow{AG} \\circ "
                   f"\\overrightarrow{{{p}{q}}}$ und beurteile, ob der "
                   "Winkel zwischen $\\overrightarrow{AG}$ und "
                   f"$\\overrightarrow{{{p}{q}}}$ kleiner als $90^\\circ$ "
                   "ist. (Abitur 2024 LK)")
            erg = (f"Ergebnis: ${s} < 0$: der Winkel ist stumpf, also "
                   "nicht kleiner als $90^\\circ$")
            orig = g[4]["original"]
            ant = "Skalarprodukt: \\leerfeld"
        lo = (f"Vektoren: $\\overrightarrow{{AG}} = {T(*u)}$, "
              f"$\\overrightarrow{{{p}{q}}} = {T(*v)}$; Skalarprodukt: "
              f"${prod} = {s}$; {erg}")
        neu.append(um(g[i - 1], variante=i, aufgabe=auf, antwort=ant,
                      loesung=lo, pruef=str(s), original=orig,
                      quelle=94, form="teil"))
    for s in (2, 3, 4, 5):
        for r in wo(alt, 1, s):
            neu.append(nachziehen(r, "e1"))
    # Pflicht k2
    f1, f2, f3 = wo(alt, 2, 1)
    neu.append(nachziehen(f1, "e1"))
    neu.append(um(f2, aufgabe=(
        "Mia berechnet für $\\vec a = (2 \\mid -1 \\mid 1)$ und "
        "$\\vec b = (-1 \\mid 3 \\mid -1)$ das Skalarprodukt "
        "$\\vec a \\circ \\vec b = -2 - 3 - 1 = -6$ und schreibt: "
        "„Der Winkel zwischen $\\vec a$ und $\\vec b$ ist stumpf.“ "
        "Prüfe, ob Mia richtig gerechnet hat."),
        loesung=("Richtig. Die Beträge sind positiv, also hat das "
                 "Skalarprodukt das Vorzeichen von "
                 "$\\mathrm{cos}\\,\\varphi$; negativ heißt stumpf."),
        pruef=""))
    neu.append(um(f3, aufgabe=(
        "$\\vec u = (3 \\mid 1 \\mid 2)$ und $\\vec v = (-r \\mid 2 "
        "\\mid 2)$; gesucht sind alle r, für die der Winkel zwischen "
        "$\\vec u$ und $\\vec v$ mindestens $90^\\circ$ groß ist. Ole "
        "rechnet: \\rechnung{-3r + 6 &\\le 0 &&\\mid -6 \\\\ -3r &\\le "
        "-6 &&\\mid :(-3) \\\\ r &\\le 2} Setze $r = 3$ in jede Zeile "
        "ein. In welcher Zeile stimmt es nicht mehr?"),
        loesung=("In Zeile 3 ($3 \\le 2$ ist falsch, davor $-3 \\le 0$ "
                 "und $-9 \\le -6$ wahr): beim Teilen durch $-3$ muss "
                 "sich das Ungleichheitszeichen umdrehen (Division durch "
                 "eine negative Zahl dreht das Zeichen um). Richtig ist "
                 "$r \\ge 2$."),
        pruef=""))
    b1, b2, b3 = wo(alt, 2, 2)
    neu.append(nachziehen(b1, "e1"))
    neu.append(um(b2, aufgabe=(
        "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
        "Begründe. (1) Ist das Skalarprodukt zweier Vektoren null und "
        "keiner der Nullvektor, stehen sie immer senkrecht zueinander. "
        "(2) Ein negatives Skalarprodukt gehört immer zu einem Winkel "
        "unter $90^\\circ$. (3) Es gibt zwei Vektoren, deren "
        "Skalarprodukt größer ist als das Produkt ihrer Beträge."),
        loesung=("(1) wahr, denn dann ist $\\mathrm{cos}\\,\\varphi = "
                 "0$, also $\\varphi = 90^\\circ$; (2) falsch, z. B. "
                 "$(2 | 0 | 0) \\circ (-3 | 0 | 0) = -6$ bei "
                 "$180^\\circ$; (3) falsch, z. B. schon gleich "
                 "gerichtete Vektoren erreichen nur das Produkt der "
                 "Beträge, denn $\\mathrm{cos}\\,\\varphi$ ist "
                 "höchstens $1$"),
        pruef=""))
    neu.append(um(b3, aufgabe=(
        "Tim sagt: „Mache ich einen von zwei Pfeilen doppelt so lang, "
        "wird ihr Skalarprodukt doppelt so groß – also wird auch der "
        "Winkel zwischen den Pfeilen größer.“ Begründe, ohne genau zu "
        "rechnen, ob Tim recht hat."),
        loesung=("Nein; das Skalarprodukt verdoppelt sich, weil sich "
                 "ein Betrag verdoppelt, aber der Pfeil wird nicht "
                 "gedreht – der Winkel und sein Kosinus bleiben gleich "
                 "(Winkelform des Skalarprodukts)."),
        pruef=""))
    return fertig(neu)


# ---------------------------------------------------------------- e2
# Zeltpyramide Z2 (fest): A(5|3|0), B(3|7|0), C(-2|5|0), D(-3|1|0),
# S(1|2|6); die Kante SA bleibt, die zweite Kante wandert.
Z2 = {"A": (5, 3, 0), "B": (3, 7, 0), "C": (-2, 5, 0), "D": (-3, 1, 0),
      "S": (1, 2, 6)}


def z2_text():
    return ("Ein Zelt hat die Form einer Pyramide mit den Bodenecken "
            + ", ".join(P(n, *Z2[n]) for n in "ABC") + " und "
            + P("D", *Z2["D"]) + " und der Spitze " + P("S", *Z2["S"])
            + ".")


def wurzel(n):
    r = math.isqrt(n)
    return str(r) if r * r == n else f"\\sqrt{{{n}}}"


def winkel_loesung(sch, p, q, K, vorn="Vektoren vom Scheitel"):
    u, v = vek(sch, p, K), vek(sch, q, K)
    s = dot(u, v)
    nu, nv = dot(u, u), dot(v, v)
    w = math.degrees(math.acos(s / math.sqrt(nu * nv)))
    lo = (f"{vorn} {sch}: $\\overrightarrow{{{sch}{p}}} = {T(*u)}$, "
          f"$\\overrightarrow{{{sch}{q}}} = {T(*v)}$; Skalarprodukt: "
          f"${s}$; Beträge: ${wurzel(nu)}$ und ${wurzel(nv)}$; Kosinus: "
          f"$\\mathrm{{cos}}\\,\\varphi = \\frac{{{s}}}{{{wurzel(nu)} "
          f"\\cdot {wurzel(nv)}}}$; Ergebnis: $\\varphi \\approx "
          f"{grad(w)}^\\circ$")
    pr = (f"math.degrees(math.acos({s}/(math.sqrt({nu})*"
          f"math.sqrt({nv}))))")
    return lo, pr


def e2(alt):
    neu = []
    for r in wo(alt, 1, 0):
        neu.append(nachziehen(r, "e2"))
    for r in wo(alt, 2, 0):
        neu.append(nachziehen(r, "e2"))
    g = wo(alt, 2, 1)
    paare = [("S", "A", "B"), ("S", "A", "C"), ("S", "A", "D"),
             ("A", "S", "D"), ("A", "B", "S")]
    for i, (sch, p, q) in enumerate(paare, 1):
        lo, pr = winkel_loesung(sch, p, q, Z2)
        auf = (z2_text() + f" Berechne den Winkel zwischen den Kanten "
               f"{sch}{p} und {sch}{q}.")
        orig = None
        if i == 5:
            auf = (z2_text() + f" Berechne die Größe des Winkels "
                   f"zwischen den Kanten {sch}{p} und {sch}{q}. "
                   "(Abitur 2026 GK)")
            orig = g[4]["original"]
        neu.append(um(g[i - 1], variante=i, aufgabe=auf, loesung=lo,
                      pruef=pr, original=orig, quelle=95, form="teil"))
    for s in (2, 3, 4, 5, 6):
        for r in wo(alt, 2, s):
            neu.append(nachziehen(r, "e2"))
    f1, f2, f3 = wo(alt, 3, 1)
    neu.append(nachziehen(f1, "e2"))
    neu.append(um(f2, aufgabe=(
        "Lea berechnet den Schnittwinkel der Geraden g mit dem "
        "Richtungsvektor $(1 \\mid 2 \\mid 2)$ und der Geraden h mit "
        "dem Richtungsvektor $(-2 \\mid -1 \\mid -2)$: "
        "$\\mathrm{cos}\\,\\varphi = \\frac{\\lvert -2 - 2 - 4 "
        "\\rvert}{3 \\cdot 3} = \\frac{8}{9}$, $\\varphi \\approx "
        "27{,}3^\\circ$. Prüfe, ob Lea richtig gerechnet hat."),
        loesung=("Richtig. Der Betrag im Zähler liefert den spitzen "
                 "Schnittwinkel; ohne ihn käme der stumpfe Nebenwinkel "
                 "heraus."),
        pruef=""))
    neu.append(um(f3, aufgabe=(
        "Zu vier Aufgaben steht jeweils ein Ergebnis da. (1) "
        "Schnittwinkel zweier Geraden: $112^\\circ$. (2) Innenwinkel "
        "bei A mit $\\overrightarrow{AB} \\circ \\overrightarrow{AC} = "
        "5$: $104^\\circ$. (3) Winkel zweier Kanten mit "
        "$\\mathrm{cos}\\,\\varphi = \\frac{9}{7}$: $25^\\circ$. (4) "
        "Winkel zweier Kanten mit $\\mathrm{cos}\\,\\varphi = "
        "-\\frac{1}{3}$: $109{,}5^\\circ$. Welche Ergebnisse können "
        "nicht stimmen? Begründe, ohne genau zu rechnen."),
        loesung=("(1) kann nicht stimmen: ein Schnittwinkel zweier "
                 "Geraden ist höchstens $90^\\circ$; (2) kann nicht "
                 "stimmen: ein positives Skalarprodukt gehört zu einem "
                 "spitzen Winkel; (3) kann nicht stimmen: ein Kosinus "
                 "ist höchstens $1$; (4) kann stimmen"),
        pruef=""))
    b1, b2, b3 = wo(alt, 3, 2)
    neu.append(nachziehen(b1, "e2"))
    neu.append(um(b2, aufgabe=(
        "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
        "Begründe. (1) Der Winkel, den die Kosinusformel für zwei "
        "Kanten eines Dreiecks vom Scheitel aus liefert, ist immer "
        "kleiner als $180^\\circ$. (2) Nimmt man bei einem der beiden "
        "Vektoren die Gegenrichtung, bleibt der Winkel immer gleich. "
        "(3) Es gibt zwei sich schneidende Geraden, deren "
        "Schnittwinkel größer als $90^\\circ$ ist."),
        loesung=("(1) wahr, denn die Kanten eines Dreiecks zeigen nie "
                 "genau entgegengesetzt, der Kosinus ist also größer "
                 "als $-1$; (2) falsch, z. B. $(1 | 0 | 0)$ und "
                 "$(1 | 1 | 0)$ schließen $45^\\circ$ ein, "
                 "$(-1 | 0 | 0)$ und $(1 | 1 | 0)$ aber $135^\\circ$; "
                 "(3) falsch, z. B. schneiden sich zwei Geraden unter "
                 "$60^\\circ$ und $120^\\circ$ – Schnittwinkel ist "
                 "der kleinere, höchstens $90^\\circ$"),
        pruef=""))
    neu.append(um(b3, aufgabe=(
        "Ida sagt: „Für den Innenwinkel bei A ist es egal, ob ich "
        "$\\overrightarrow{AB}$ oder $\\overrightarrow{BA}$ nehme – das "
        "Skalarprodukt ist ja nur eine Zahl.“ Begründe, ohne genau zu "
        "rechnen, ob Ida recht hat."),
        loesung=("Nein; $\\overrightarrow{BA} = -\\overrightarrow{AB}$ "
                 "dreht das Vorzeichen des Skalarprodukts und damit des "
                 "Kosinus um, aus dem Innenwinkel wird sein Nebenwinkel "
                 "(Richtung zählt)."),
        pruef=""))
    for r in wo(alt, 3, 3):
        neu.append(nachziehen(r, "e2"))
    return fertig(neu)


# ---------------------------------------------------------------- e3
# Pavillondach P3 (fest): Spitze S(0|0|6), Boden A(4|0|0), B(0|2|0),
# C(-3|0|0), D(0|-4|0), E(2|-4|0); die xy-Ebene bleibt, die
# Dachfläche wandert.
P3 = [("ABS", (3, 6, 2), 12), ("CDS", (-4, -3, 2), 12),
      ("DES", (0, -3, 2), 12), ("EAS", (6, -3, 4), 24),
      ("BCS", (-2, 3, 1), 6)]


def gl(n, d):
    teile = []
    for k, v in zip(n, "xyz"):
        if k == 0:
            continue
        a = "" if abs(k) == 1 else str(abs(k))
        if not teile:
            teile.append(("-" if k < 0 else "") + a + v)
        else:
            teile.append(("- " if k < 0 else "+ ") + a + v)
    return " ".join(teile) + f" = {d}"


def e3(alt):
    neu = []
    for r in wo(alt, 1, 0):
        neu.append(nachziehen(r, "e3"))
    g = wo(alt, 1, 1)
    kopf = ("Ein Pavillondach ist eine Pyramide mit der Spitze "
            "$S(0 \\mid 0 \\mid 6)$ über dem Fünfeck ABCDE in der "
            "xy-Ebene; die xy-Ebene ist die Horizontale.")
    for i, (fl, n, d) in enumerate(P3, 1):
        nn = dot(n, n)
        w = math.degrees(math.acos(abs(n[2]) / math.sqrt(nn)))
        auf = (kopf + f" Die Dachfläche {fl} liegt in der Ebene "
               f"${gl(n, d)}$. Berechne den Neigungswinkel dieser "
               "Dachfläche gegen die xy-Ebene.")
        orig = None
        if i == 5:
            auf = auf[:-1] + ". (Abitur 2025 GK)"
            auf = auf.replace("xy-Ebene.. (", "xy-Ebene. (")
            orig = g[4]["original"]
        lo = (f"Normalenvektoren: $\\vec n = {T(*n)}$ und $(0 | 0 | 1)$; "
              f"Skalarprodukt im Betrag: ${abs(n[2])}$; Beträge: "
              f"${wurzel(nn)}$ und $1$; Kosinus: $\\mathrm{{cos}}\\,"
              f"\\varphi = \\frac{{{abs(n[2])}}}{{{wurzel(nn)}}}$; "
              f"Ergebnis: $\\varphi \\approx {grad(w)}^\\circ$")
        pr = f"math.degrees(math.acos({abs(n[2])}/math.sqrt({nn})))"
        neu.append(um(g[i - 1], variante=i, aufgabe=auf, loesung=lo,
                      pruef=pr, original=orig, quelle=96, form="teil"))
    for s in (2, 3, 4, 5):
        for r in wo(alt, 1, s):
            neu.append(nachziehen(r, "e3"))
    f1, f2, f3 = wo(alt, 2, 1)
    neu.append(nachziehen(f1, "e3"))
    neu.append(um(f2, aufgabe=(
        "Nina berechnet den Winkel zwischen der Ebene $2x + y + 2z = "
        "5$ und der xy-Ebene: $\\lvert\\vec n\\rvert = \\sqrt{4 + 1 + "
        "4} = 3$, $\\mathrm{cos}\\,\\varphi = \\frac{2}{3}$, "
        "$\\varphi \\approx 48{,}2^\\circ$. Prüfe, ob Nina richtig "
        "gerechnet hat."),
        loesung=("Richtig. Gegen die xy-Ebene steht im Zähler der "
                 "Betrag der dritten Koordinate des Normalenvektors, im "
                 "Nenner sein Betrag."),
        pruef=""))
    neu.append(um(f3, aufgabe=(
        "Zu vier Ebenen steht jeweils ein Ergebnis da. (1) Die Ebene "
        "$4x + 3y + z = 12$ ist gegen die xy-Ebene um $124^\\circ$ "
        "geneigt. (2) Die Ebene $z = 4$ ist gegen die xy-Ebene um "
        "$20^\\circ$ geneigt. (3) Eine Dachfläche hat den "
        "Neigungswinkel $30^\\circ$ und die Neigung $30\\,\\%$. (4) Die "
        "Ebene $x + y + 4z = 8$ ist gegen die xy-Ebene um "
        "$19{,}5^\\circ$ geneigt. Welche Ergebnisse können nicht "
        "stimmen? Begründe, ohne genau zu rechnen."),
        loesung=("(1) kann nicht stimmen: der Winkel zweier Ebenen ist "
                 "höchstens $90^\\circ$; (2) kann nicht stimmen: die "
                 "Ebene ist parallel zur xy-Ebene, der Winkel ist "
                 "$0^\\circ$; (3) kann nicht stimmen: die Neigung in "
                 "Prozent ist der Tangens mal hundert, bei $30^\\circ$ "
                 "etwa $58\\,\\%$; (4) kann stimmen"),
        pruef=""))
    b1, b2, b3 = wo(alt, 2, 2)
    neu.append(nachziehen(b1, "e3"))
    neu.append(um(b2, aufgabe=(
        "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
        "Begründe. (1) Haben zwei Ebenen gleiche Normalenvektoren, ist "
        "ihr Winkel immer $0^\\circ$. (2) Der Neigungswinkel einer "
        "Ebene gegen die xy-Ebene hängt nur von der dritten Koordinate "
        "ihres Normalenvektors ab. (3) Jede Ebene, in deren Gleichung "
        "z nicht vorkommt, steht senkrecht auf der xy-Ebene."),
        loesung=("(1) wahr, denn die Ebenen sind dann parallel oder "
                 "gleich; (2) falsch, z. B. $x + z = 1$ und $3x + z = "
                 "1$: gleiche dritte Koordinate, aber $45^\\circ$ und "
                 "etwa $71{,}6^\\circ$; (3) wahr, denn die dritte "
                 "Koordinate des Normalenvektors ist null, also auch "
                 "der Kosinus, der Winkel ist $90^\\circ$"),
        pruef=""))
    neu.append(um(b3, aufgabe=(
        "Ole sagt: „Der Winkel zwischen den Normalenvektoren ist immer "
        "schon der Winkel, den zwei Flächen eines Körpers innen "
        "einschließen.“ Begründe, ohne genau zu rechnen, ob Ole recht "
        "hat."),
        loesung=("Nein; die Formel mit Betrag im Zähler liefert den "
                 "spitzen Schnittwinkel der Ebenen, der Innenwinkel "
                 "eines Körpers kann der stumpfe Nebenwinkel sein, "
                 "etwa zwischen zwei Zeltwänden (der verlangte Winkel)."),
        pruef=""))
    for r in wo(alt, 2, 3):
        neu.append(nachziehen(r, "e3"))
    return fertig(neu)


# ---------------------------------------------------------------- e4
# Mast M4 (fest): Spitze S(2|3|8); der Seilanker wandert.
S4 = (2, 3, 8)
ANKER = [("A", (8, 3, 0)), ("B", (-2, 11, 0)), ("C", (3, -1, 0)),
         ("D", (-4, 0, 0))]


def e4(alt):
    neu = []
    for r in wo(alt, 1, 0):
        neu.append(nachziehen(r, "e4"))
    g = wo(alt, 1, 1)
    kopf = ("Ein Mast steht senkrecht auf dem Boden, seine Spitze ist "
            "$S(2 \\mid 3 \\mid 8)$; der Boden ist die xy-Ebene, 1 LE "
            "entspricht 1 m.")
    for i in range(1, 6):
        if i < 5:
            n, a = ANKER[i - 1]
            u = tuple(b - c for b, c in zip(a, S4))
            auf = (kopf + f" Ein Spannseil führt geradlinig von S zum "
                   f"Anker {P(n, *a)}. Berechne den Winkel zwischen "
                   "dem Seil und dem Boden.")
            vorn = (f"Richtungsvektor: $\\overrightarrow{{S{n}}} = "
                    f"{T(*u)}$")
            orig = None
        else:
            u = (3, -1, -4)
            auf = (kopf + " Ein weiteres Seil verläuft von S aus "
                   "geradlinig in Richtung $(3 \\mid -1 \\mid -4)$. "
                   "Berechne den Winkel, unter dem es auf den Boden "
                   "trifft. (Abitur 2023 GK)")
            vorn = f"Richtungsvektor: $\\vec u = {T(*u)}$"
            orig = g[4]["original"]
        nn = dot(u, u)
        w = math.degrees(math.asin(abs(u[2]) / math.sqrt(nn)))
        lo = (vorn + "; Normalenvektor des Bodens: $(0 | 0 | 1)$; "
              f"Skalarprodukt im Betrag: ${abs(u[2])}$; Beträge: "
              f"${wurzel(nn)}$ und $1$; Sinus: $\\mathrm{{sin}}\\,"
              f"\\varphi = \\frac{{{abs(u[2])}}}{{{wurzel(nn)}}}$; "
              f"Ergebnis: $\\varphi \\approx {grad(w)}^\\circ$")
        pr = f"math.degrees(math.asin({abs(u[2])}/math.sqrt({nn})))"
        neu.append(um(g[i - 1], variante=i, aufgabe=auf, loesung=lo,
                      pruef=pr, original=orig, quelle=97, form="teil"))
    for s in (2, 3, 4):
        for r in wo(alt, 1, s):
            neu.append(nachziehen(r, "e4"))
    for r in wo(alt, 2, 1):
        neu.append(nachziehen(r, "e4"))
    f1, f2, f3 = wo(alt, 3, 1)
    neu.append(nachziehen(f1, "e4"))
    neu.append(um(f2, aufgabe=(
        "Zu vier Geraden steht jeweils ihr Winkel gegen die xy-Ebene "
        "da. (1) Richtungsvektor $(3 \\mid 4 \\mid 0)$: $37^\\circ$. "
        "(2) Ein Seil steigt auf $5$ m waagerechter Strecke um $10$ m: "
        "$26{,}6^\\circ$. (3) Richtungsvektor $(0 \\mid 0 \\mid 7)$: "
        "$90^\\circ$. (4) Richtungsvektor $(1 \\mid 2 \\mid 2)$: "
        "$101{,}8^\\circ$. Welche Ergebnisse können nicht stimmen? "
        "Begründe, ohne genau zu rechnen."),
        loesung=("(1) kann nicht stimmen: die dritte Koordinate ist "
                 "null, die Gerade ist parallel zur xy-Ebene, der "
                 "Winkel ist $0^\\circ$; (2) kann nicht stimmen: das "
                 "Seil steigt mehr, als es waagerecht vorankommt, der "
                 "Winkel ist größer als $45^\\circ$ – $26{,}6^\\circ$ "
                 "ist der Winkel zur Senkrechten; (3) kann stimmen; (4) "
                 "kann nicht stimmen: ein Winkel zwischen Gerade und "
                 "Ebene ist höchstens $90^\\circ$"),
        pruef=""))
    neu.append(um(f3, aufgabe=(
        "Ein Bogen verläuft durch $A(-8 \\mid 5)$, $B(8 \\mid 5)$ und "
        "den tiefsten Punkt $C(0 \\mid 1)$, der Kreis hat den "
        "Mittelpunkt $M(0 \\mid 11)$; 1 LE entspricht 1 m. Tim "
        "rechnet: $r = 11 - 1 = 10$, $\\mathrm{tan}\\,\\frac{\\alpha}"
        "{2} = \\frac{8}{6}$, $\\alpha \\approx 106{,}3^\\circ$, $b = "
        "\\frac{106{,}3^\\circ}{360^\\circ} \\cdot 2\\pi \\cdot 10 "
        "\\approx 18{,}5$ m. Prüfe, ob Tim richtig gerechnet hat."),
        loesung=("Richtig. Der Radius ist der Abstand von M zum "
                 "Kreispunkt C, nicht die Höhe von M; der Bogen ist der "
                 "Anteil $\\frac{\\alpha}{360^\\circ}$ des Kreisumfangs."),
        pruef=""))
    b1, b2, b3 = wo(alt, 3, 2)
    neu.append(nachziehen(b1, "e4"))
    neu.append(um(b2, aufgabe=(
        "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
        "Begründe. (1) Eine Gerade, deren Richtungsvektor die dritte "
        "Koordinate null hat, verläuft immer parallel zur xy-Ebene "
        "oder in ihr. (2) Der Winkel zwischen einer Geraden und einer "
        "Ebene ist immer der Winkel zwischen Richtungsvektor und "
        "Normalenvektor. (3) Es gibt eine Gerade, die mit der xy-Ebene "
        "einen Winkel von $90^\\circ$ einschließt."),
        loesung=("(1) wahr, denn dann ist das Skalarprodukt mit "
                 "$(0 | 0 | 1)$ null, also auch der Sinus; (2) falsch, "
                 "z. B. Richtungsvektor $(2 | 0 | 1)$: zur Normalen "
                 "etwa $63{,}4^\\circ$, zur xy-Ebene etwa "
                 "$26{,}6^\\circ$, das Komplement; (3) wahr, z. B. die "
                 "z-Achse"),
        pruef=""))
    neu.append(um(b3, aufgabe=(
        "Lina sagt: „Für den Winkel zwischen einer Geraden und einer "
        "Ebene bekomme ich mit dem Kosinus statt dem Sinus dasselbe "
        "Ergebnis – die Formel ist ja sonst gleich.“ Begründe, ohne "
        "genau zu rechnen, ob Lina recht hat."),
        loesung=("Nein; mit dem Kosinus erhält sie den Winkel zwischen "
                 "Richtungs- und Normalenvektor, den Winkel zur "
                 "Normalen; der Winkel zur Ebene ist dessen Komplement, "
                 "deshalb gehört der Sinus in die Formel."),
        pruef=""))
    for r in wo(alt, 3, 3):
        neu.append(nachziehen(r, "e4"))
    return fertig(neu)


def main(argv):
    dateien = argv or ["e1", "e2", "e3", "e4"]
    fn = {"e1": e1, "e2": e2, "e3": e3, "e4": e4}
    for f in dateien:
        alt = lade(f)
        if any(r["sprosse"] < 0 for r in alt) and f == "e1":
            print(f, "schon nachgezogen, übersprungen")
            continue
        neu = fn[f](alt)
        zaehle(f, alt, neu)
        schreibe(f, neu)


if __name__ == "__main__":
    main(sys.argv[1:])

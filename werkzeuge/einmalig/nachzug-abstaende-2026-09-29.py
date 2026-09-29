"""Nachzug bank/abstaende auf die Mappe vom 29.09. (Katalog 2a296e5).

Einmalig. Liest den Bestand (27./28.09., samt Gegenlese-Korrektur),
zieht quelle, sprosse, id und sprosse_text nach, schreibt die neue
Vorstufe e2 s0 (Abstand des Ursprungs), die vier Grundfall-Päckchen
(fester Körper, ein Wert wandert) und die Pflichtformen (P1, P2, P4,
P6, P8). Zählt je Einheit übernommen/neu/umgeschrieben/entfallen und
schreibt sie nach nachzug-zahlen.json neben die Datei (nicht
committet; stand.md trägt die Zahlen).

Aufruf: python3 werkzeuge/einmalig/nachzug-abstaende-2026-09-29.py [e1 e2 …]
"""
import copy
import json
import math
import sys
from pathlib import Path

B = Path(__file__).resolve().parents[2] / "bank" / "abstaende"
E = "abstaende"
# Katalogzeilen: Sprossen je Verfahrenstyp 105–108 → 103–106
QMAP = {105: 103, 106: 104, 107: 105, 108: 106}
VORSTUFE_NEU = {
    3: "„Was sagt das Gleichungspaar?“ – zu vorgelegten Gleichungen "
       "ankreuzen, was jede leistet: Punkt auf der Geraden, "
       "Lotbedingung (Skalarprodukt null), Abstandsgleichheit; "
       "nichts rechnen",
    4: "„Senkrecht oder schräg?“ – zu einer eingezeichneten "
       "Verbindungsstrecke ankreuzen, ob sie senkrecht steht (dann ist "
       "sie der Abstand) oder schräg (dann ist sie länger); nichts "
       "rechnen",
}
LOT_NEU = ("die Lotgerade durch einen Punkt angeben (abi 2017-bb-ea-B3.2d), "
           "ihr Schnitt mit der Ebene ist der Lotfußpunkt; Probe: der "
           "Lotfußpunkt erfüllt die Ebenengleichung")
URSPRUNG = ("Abstand des Ursprungs: nur den Betrag der rechten Seite durch "
            "den Betrag des Normalenvektors teilen, noch keinen Punkt "
            "einsetzen")


def z(x):
    """Zahl für LaTeX: Dezimalkomma {,}, Minus als -."""
    if isinstance(x, float) and x.is_integer():
        x = int(x)
    s = f"{x:g}" if isinstance(x, float) else str(x)
    return s.replace(".", "{,}")


def T(*k):
    return "(" + " | ".join(z(x) for x in k) + ")"


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


def nachziehen(r, **kw):
    """Übernahme: nur id, sprosse, kette_nr, quelle, sprosse_text."""
    r = copy.deepcopy(r)
    r["quelle"] = QMAP.get(r["quelle"], r["quelle"])
    r.update(kw)
    r["_art"] = "uebernommen"
    r["id"] = rid(r)
    return r


def umschreiben(r, art="umgeschrieben", **kw):
    r = copy.deepcopy(r)
    r["quelle"] = QMAP.get(r["quelle"], r["quelle"])
    for f in ("antwort", "grafik", "loesungsgrafik"):
        r[f] = ""
    r.update(kw)
    r["_art"] = art
    r["id"] = rid(r)
    return r


def finde(rows, k, s, v):
    for r in rows:
        if (r["kette_nr"], r["sprosse"], r["variante"]) == (k, s, v):
            return r
    raise KeyError((k, s, v))


def ersetze(rows, neu):
    """neu: Liste umgeschriebener Zeilen, gleiche Stelle über id."""
    by = {(r["kette_nr"], r["sprosse"], r["variante"]): r for r in neu}
    return [by.get((r["kette_nr"], r["sprosse"], r["variante"]), r)
            for r in rows]


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def betrag(v):
    return math.sqrt(dot(v, v))


def wurzel(q):
    r = math.isqrt(q)
    return (True, r) if r * r == q else (False, q)


# --- e1 -------------------------------------------------------------------

QUADER1 = {"A": (2, 1, 1), "B": (4, 1, 1), "C": (4, 4, 1), "D": (2, 4, 1),
           "E": (2, 1, 7), "F": (4, 1, 7), "G": (4, 4, 7), "H": (2, 4, 7)}


def quader_text(q):
    ecken = ", ".join(f"${n}{T(*p)}$" for n, p in q.items())
    return f"Der Quader $ABCDEFGH$ hat die Ecken {ecken}."


def e1():
    rows = lade("e1")
    out = []
    vorlage_g = finde(rows, 2, 1, 1)
    for r in rows:
        if r["hoehe"] == "grundfall":
            continue
        out.append(nachziehen(r))
    # Päckchen: A bleibt, die zweite Ecke wandert
    gf = []
    for v, n in enumerate(["C", "G", "F", "H", "D"], 1):
        a, b = QUADER1["A"], QUADER1[n]
        d = sub(b, a)
        q = dot(d, d)
        ganz, w = wurzel(q)
        quad = " + ".join(f"{z(x)}^2" if x >= 0 else f"({z(x)})^2"
                          for x in d)
        los = (f"Verbindungsvektor: $\\overrightarrow{{A{n}}} = {T(*b)} - "
               f"{T(*a)} = {T(*d)}$; Betrag: $d = \\sqrt{{{quad}}} = "
               f"\\sqrt{{{q}}}$; ")
        if ganz:
            los += f"Ergebnis: $d = {w}$"
            ant = "d = __"
        else:
            los += f"Ergebnis: $d \\approx {z(round(math.sqrt(q), 2))}$"
            ant = "d ≈ __"
        gf.append(umschreiben(
            vorlage_g, variante=v,
            merkmal="Abstand der festen Ecke A zu einer anderen Ecke "
                    "desselben Quaders",
            aufgabe=f"{quader_text(QUADER1)} Berechne den Abstand der "
                    f"Ecken $A$ und ${n}$.",
            form="teil", antwort=ant, loesung=los,
            pruef=str(w) if ganz else f"math.sqrt({q})", original=None))
    i = next(i for i, r in enumerate(out)
             if r["kette_nr"] == 2 and r["sprosse"] == 2)
    out[i:i] = gf
    # Pflicht: fehler v1 → P1, v3 → P2; begruenden v2 → P4, v3 → P6
    neu = [
        umschreiben(
            finde(rows, 3, 1, 1),
            aufgabe="Vier Schüler berechnen den Abstand der Punkte "
                    "$A(1 | 2 | 3)$ und $B(4 | -2 | 15)$ und erhalten "
                    "(1) $11$, (2) $-13$, (3) $13$, (4) $20$. Welche "
                    "Ergebnisse können nicht stimmen? Begründe, ohne "
                    "genau zu rechnen.",
            form="text",
            loesung="(1) kann nicht stimmen – der Abstand ist mindestens "
                    "so groß wie der größte Koordinatenunterschied 12; "
                    "(2) kann nicht stimmen – ein Abstand ist nie "
                    "negativ; (4) kann nicht stimmen – der Abstand ist "
                    "höchstens die Summe $3 + 4 + 12 = 19$ der "
                    "Koordinatenunterschiede (Umweg entlang der Kanten)",
            pruef=""),
        umschreiben(
            finde(rows, 3, 1, 3),
            aufgabe="Ein Boot fährt in 40 s geradlinig von $P(20 | 10 | 0)$ "
                    "nach $Q(140 | 170 | 0)$; 1 LE = 1 m. Jana rechnet: "
                    "\\rechnung{\\overrightarrow{PQ} &= (120 | 160 | 0) \\\\ "
                    "|\\overrightarrow{PQ}| &= \\sqrt{14\\,400 + 25\\,600} "
                    "= 200 \\text{ m} \\\\ v &= \\tfrac{200}{40} = 5 "
                    "\\text{ m/s} = 5 \\cdot 3{,}6 \\text{ km/h} = 18 "
                    "\\text{ km/h}} Prüfe, ob Jana richtig gerechnet hat.",
            form="text",
            loesung="Richtig. Von m/s nach km/h wird mit 3,6 "
                    "multipliziert, weil in einer Stunde 3\\,600 s "
                    "vergehen und 1 km 1\\,000 m sind.",
            pruef=""),
        umschreiben(
            finde(rows, 3, 2, 2),
            aufgabe="Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                    "ist. Begründe. (1) Der Abstand zweier Punkte ist nie "
                    "negativ. (2) Vertauscht man die beiden Punkte, ändert "
                    "sich ihr Abstand. (3) Es gibt zwei Punkte, deren "
                    "Abstand kleiner ist als der Unterschied ihrer "
                    "x-Koordinaten.",
            form="text",
            loesung="(1) wahr, denn der Abstand ist eine Wurzel, und die "
                    "ist nie negativ; (2) falsch, z. B. haben "
                    "$\\overrightarrow{AB} = (1 | 2 | 2)$ und "
                    "$\\overrightarrow{BA} = (-1 | -2 | -2)$ beide den "
                    "Betrag 3 – beim Quadrieren fällt das Vorzeichen weg; "
                    "(3) falsch – unter der Wurzel steht das Quadrat des "
                    "x-Unterschieds plus zwei nicht negative Quadrate, "
                    "der Abstand ist also nie kleiner als der "
                    "x-Unterschied",
            pruef=""),
        umschreiben(
            finde(rows, 3, 2, 3),
            aufgabe="Nils sagt: „Beim Abstand zweier Punkte darf ich die "
                    "Koordinaten auch addieren, das Quadrieren macht "
                    "sowieso alles positiv.“ Begründe, ohne genau zu "
                    "rechnen, ob Nils recht hat.",
            form="text",
            loesung="Nein; der Abstand hängt nur von den Unterschieden "
                    "der Koordinaten ab (Spitze minus Fuß) – die Summe "
                    "gehört zum Vektor $\\overrightarrow{OA} + "
                    "\\overrightarrow{OB}$, nicht zur Verbindung von A "
                    "nach B; das Quadrieren beseitigt nur Vorzeichen, "
                    "keine falsche Rechenart.",
            pruef=""),
    ]
    return ersetze(out, neu)


# --- e2 -------------------------------------------------------------------

N2 = (2, -1, 2)          # Normalenvektor, Betrag 3
D2 = 6                   # E: 2x - y + 2z = 6


def e2():
    rows = lade("e2")
    out = []
    for r in rows:
        if r["hoehe"] == "grundfall":
            continue
        if r["hoehe"] == "vorstufe":
            out.append(nachziehen(r, sprosse=-1))
        elif r["kette_nr"] == 1 and r["sprosse"] == 2:
            out.append(nachziehen(r, sprosse_text=LOT_NEU))
        else:
            out.append(nachziehen(r))
    vorlage = finde(rows, 1, 1, 1)
    # neue Vorstufe s0: Abstand des Ursprungs, derselbe Normalenvektor
    s0 = []
    for v, rs in enumerate([6, -12, 15, 7.5], 1):
        d = abs(rs) / 3
        if rs < 0:
            teil = f"$d = \\tfrac{{|{z(rs)}|}}{{3}} = {z(d)}$"
        else:
            teil = f"$d = \\tfrac{{{z(rs)}}}{{3}} = {z(d)}$"
        s0.append(umschreiben(
            vorlage, art="neu", sprosse=0, hoehe="vorstufe", variante=v,
            sprosse_text=URSPRUNG,
            merkmal="Ursprung: nur die rechte Seite durch den Betrag des "
                    "Normalenvektors teilen",
            aufgabe=f"Welchen Abstand hat der Ursprung von der Ebene "
                    f"$E\\colon 2x - y + 2z = {z(rs)}$? Teile nur den "
                    f"Betrag der rechten Seite durch den Betrag des "
                    f"Normalenvektors.",
            form="teil", antwort="d = __",
            loesung=f"Normalenvektor: $|\\vec n| = \\sqrt{{4 + 1 + 4}} = "
                    f"3$; teilen: {teil}",
            pruef=z(d).replace("{,}", "."), original=None))
    # Päckchen: dieselbe Ebene, der Punkt wandert
    gf = []
    punkte = [(4, 0, 5), (1, 2, 6), (-1, 3, -2), (6, 3, 3), (3, 3, 3)]
    for v, p in enumerate(punkte, 1):
        glieder = [N2[0] * p[0], N2[1] * p[1], N2[2] * p[2]]
        wert = sum(glieder) - D2
        assert wert % 3 == 0
        h = wert // 3
        term = z(glieder[0])
        for g in glieder[1:]:
            term += f" - {z(-g)}" if g < 0 else f" + {z(g)}"
        term += f" - {D2}"
        los = (f"Normalenvektor: $\\vec n = {T(*N2)}$, $|\\vec n| = 3$; "
               f"HNF: $\\tfrac{{2x - y + 2z - 6}}{{3}} = 0$; einsetzen: "
               f"$\\tfrac{{{term}}}{{3}} = {z(h)}$; ")
        if h < 0:
            los += (f"Vorzeichen: negativ, P liegt auf der Seite des "
                    f"Ursprungs; Abstand: $d = |{z(h)}| = {z(-h)}$")
        else:
            los += (f"Vorzeichen: positiv, P liegt auf der dem Ursprung "
                    f"abgewandten Seite; Abstand: $d = {z(h)}$")
        gf.append(umschreiben(
            vorlage, variante=v,
            merkmal="Abstand Punkt–Ebene mit der Hesseschen Normalform: "
                    "dieselbe Ebene, der Punkt wandert",
            aufgabe=f"Die Ebene $E\\colon 2x - y + 2z = 6$ ist gegeben. "
                    f"Berechne den Abstand des Punktes $P{T(*p)}$ von "
                    f"$E$ mit der Hesseschen Normalform.",
            form="teil", antwort="d = __", loesung=los, pruef=str(abs(h)),
            original=None))
    i = next(i for i, r in enumerate(out)
             if r["kette_nr"] == 1 and r["sprosse"] == 2)
    out[i:i] = s0 + gf
    neu = [
        umschreiben(
            finde(rows, 2, 1, 2),
            aufgabe="Gesucht ist ein Punkt $P$, dessen Spiegelpunkt an der "
                    "Ebene $E\\colon 2x + 2y - z = 0$ von $P$ den Abstand "
                    "9 hat; der Ursprung liegt in $E$. Mia rechnet: "
                    "\\rechnung{|\\vec n| &= 3 \\\\ d &= \\tfrac{9}{2} = "
                    "4{,}5 \\\\ P &= 4{,}5 \\cdot \\tfrac{1}{3} \\cdot "
                    "(2 | 2 | -1) = (3 | 3 | -1{,}5)} Prüfe, ob Mia richtig "
                    "gerechnet hat.",
            form="text",
            loesung="Richtig. P und sein Spiegelpunkt liegen auf beiden "
                    "Seiten gleich weit von E entfernt, also hat P von E "
                    "den halben Abstand, abgetragen mit dem normierten "
                    "Normalenvektor.",
            pruef=""),
        umschreiben(
            finde(rows, 2, 1, 3),
            aufgabe="Der Punkt $P(3 | 2 | 4)$ hat vom Punkt $Q(1 | 1 | 2)$ "
                    "der Ebene $E\\colon x + 2y + 2z = 7$ den Abstand 3. "
                    "Vier Schüler geben den Abstand von $P$ zu $E$ an: "
                    "(1) $2{,}67$, (2) $-2{,}67$, (3) $3{,}4$, (4) $8$. "
                    "Welche Ergebnisse können nicht stimmen? Begründe, "
                    "ohne genau zu rechnen.",
            form="text",
            loesung="(2) kann nicht stimmen – ein Abstand ist nie negativ; "
                    "(3) kann nicht stimmen – der Abstand ist höchstens "
                    "$|\\overrightarrow{PQ}| = 3$, das Lot ist die kürzeste "
                    "Verbindung; (4) kann nicht stimmen – auch 8 ist "
                    "größer als 3 (eingesetzt, aber nicht durch den "
                    "Betrag des Normalenvektors geteilt)",
            pruef=""),
        umschreiben(
            finde(rows, 2, 2, 2),
            aufgabe="Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                    "ist. Begründe. (1) Auf der Lotgeraden gibt es immer "
                    "genau einen Punkt mit dem Abstand 6 zur Ebene. "
                    "(2) Jeder Punkt der Ebene hat von ihr den Abstand "
                    "null. (3) Setzt man einen Punkt in die Hessesche "
                    "Normalform ein, ist das Ergebnis nie negativ.",
            form="text",
            loesung="(1) falsch, z. B. haben die Punkte zu den Parametern "
                    "t und −t denselben Abstand, auf beiden Seiten der "
                    "Ebene – es sind zwei; (2) wahr, denn eingesetzt ergibt "
                    "die Hessesche Normalform null; (3) falsch, z. B. "
                    "ergibt der Ursprung in $\\tfrac{2x - y + 2z - 6}{3}$ "
                    "den Wert −2 – erst der Betrag ist der Abstand",
            pruef=""),
        umschreiben(
            finde(rows, 2, 2, 3),
            aufgabe="Lena sagt: „Wenn ich die Ebenengleichung vorher mit "
                    "−2 multipliziere, erhalte ich mit der Hesseschen "
                    "Normalform denselben Abstand.“ Begründe, ohne genau "
                    "zu rechnen, ob Lena recht hat.",
            form="text",
            loesung="Ja; der eingesetzte Wert im Zähler und der Betrag des "
                    "Normalenvektors im Nenner ändern sich beide um den "
                    "Faktor 2, das Vorzeichen verschwindet im Betrag – "
                    "der Abstand bleibt gleich.",
            pruef=""),
    ]
    return ersetze(out, neu)


# --- e3 -------------------------------------------------------------------

A3 = (1, 0, 2)
R3 = (2, 1, -2)           # |r|^2 = 9


def lin(a, r, name="t"):
    teile = []
    for x, y in zip(a, r):
        if y == 0:
            teile.append(z(x))
        else:
            k = "" if abs(y) == 1 else z(abs(y))
            if x == 0:
                teile.append(("-" if y < 0 else "") + f"{k}{name}")
            else:
                teile.append(f"{z(x)} {'-' if y < 0 else '+'} {k}{name}")
    return "(" + " | ".join(teile) + ")"


def e3():
    rows = lade("e3")
    out = []
    for r in rows:
        if r["hoehe"] == "grundfall":
            continue
        if r["hoehe"] == "vorstufe":
            out.append(nachziehen(r, sprosse_text=VORSTUFE_NEU[3]))
        else:
            out.append(nachziehen(r))
    vorlage = finde(rows, 1, 1, 1)
    gf = []
    wahl = [(1, (1, 2, 2)), (-2, (0, 2, 1)), (-1, (2, -2, 1)),
            (0, (1, 0, 1)), (3, (4, -4, 2))]
    for v, (t0, w) in enumerate(wahl, 1):
        assert dot(w, R3) == 0
        f = tuple(a + t0 * r for a, r in zip(A3, R3))
        p = tuple(a + b for a, b in zip(f, w))
        ap = sub(A3, p)              # PF_t = (A - P) + t r
        k0 = dot(ap, R3)
        vpf = lin(ap, R3)
        glei = f"9t {'-' if k0 < 0 else '+'} {abs(k0)}" if k0 else "9t"
        pf = sub(f, p)
        q = dot(pf, pf)
        ganz, wq = wurzel(q)
        los = (f"Laufpunkt: $F_t{lin(A3, R3)}$; Verbindungsvektor: "
               f"$\\overrightarrow{{PF_t}} = {vpf}$; Lotbedingung: "
               f"$\\overrightarrow{{PF_t}} \\circ {T(*R3)} = {glei} = 0$; "
               f"Parameter: $t = {t0}$; Lotfußpunkt: $F{T(*f)}$; "
               f"Abstand: $|\\overrightarrow{{PF}}| = |{T(*pf)}| = ")
        if ganz:
            los += f"{wq}$"
            ant, pd = "F(__ | __ | __), d = __", str(wq)
        else:
            los += f"\\sqrt{{{q}}} \\approx {z(round(math.sqrt(q), 2))}$"
            ant, pd = "F(__ | __ | __), d ≈ __", f"math.sqrt({q})"
        gf.append(umschreiben(
            vorlage, variante=v,
            merkmal="Lotfußpunkt und Abstand: dieselbe Gerade, der Punkt "
                    "wandert",
            aufgabe=f"Die Gerade $g\\colon \\vec x = {T(*A3)} + t \\cdot "
                    f"{T(*R3)}$ ist gegeben. Berechne den Lotfußpunkt $F$ "
                    f"von $P{T(*p)}$ auf $g$ und den Abstand von $P$ zu "
                    f"$g$.",
            form="teil", antwort=ant, loesung=los,
            pruef=f"[[{f[0]},{f[1]},{f[2]}],{pd}]", original=None))
    i = next(i for i, r in enumerate(out)
             if r["kette_nr"] == 1 and r["sprosse"] == 2)
    out[i:i] = gf
    neu = [
        umschreiben(
            finde(rows, 2, 1, 2),
            aufgabe="Gesucht ist der Lotfußpunkt $F$ von $P(4 | 1 | 6)$ auf "
                    "$g\\colon \\vec x = (1 | 2 | 0) + t \\cdot (1 | 0 | 2)$. "
                    "Ben rechnet: \\rechnung{F_t &= (1 + t | 2 | 2t) \\\\ "
                    "\\overrightarrow{PF_t} &= (t - 3 | 1 | 2t - 6) \\\\ "
                    "\\overrightarrow{PF_t} \\circ (1 | 0 | 2) &= 5t - 15 = "
                    "0 \\\\ t &= 3 \\\\ F &= (4 | 2 | 6)} Prüfe, "
                    "ob Ben richtig gerechnet hat.",
            form="text",
            loesung="Richtig. Der Verbindungsvektor zum Laufpunkt wird mit "
                    "dem Richtungsvektor der Geraden multipliziert und null "
                    "gesetzt – das ist die Lotbedingung.",
            pruef=""),
        umschreiben(
            finde(rows, 2, 1, 3),
            aufgabe="Drei Schüler geben den Lotfußpunkt von $P(5 | 4 | 4)$ "
                    "auf $g\\colon \\vec x = (2 | 1 | 3) + t \\cdot "
                    "(1 | 0 | 2)$ an: (1) $F(4 | 0 | 7)$, (2) "
                    "$F(3 | 1 | 5)$, (3) $F(1 | 1 | 2)$. Welche Ergebnisse "
                    "können nicht stimmen? Begründe, ohne genau zu rechnen.",
            form="text",
            loesung="(1) kann nicht stimmen – jeder Punkt von g hat die "
                    "zweite Koordinate 1; (3) kann nicht stimmen – zur "
                    "ersten Koordinate 1 gehört t = −1 und damit die "
                    "dritte Koordinate 1, der Punkt liegt nicht auf g",
            pruef=""),
        umschreiben(
            finde(rows, 2, 2, 2),
            aufgabe="Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                    "ist. Begründe. (1) Das Lot von einem Punkt auf eine "
                    "Ebene steht auf jeder Geraden der Ebene senkrecht, die "
                    "durch den Lotfußpunkt geht. (2) Der Lotfußpunkt von P "
                    "auf die Gerade AB liegt immer auf der Strecke AB. "
                    "(3) Es gibt Punkte, deren Abstand zu einer Geraden "
                    "null ist.",
            form="text",
            loesung="(1) wahr, denn das Lot hat die Richtung des "
                    "Normalenvektors, und der steht auf jedem "
                    "Richtungsvektor der Ebene senkrecht; (2) falsch, "
                    "z. B. hat P(5 | 1 | 0) auf der Geraden durch "
                    "A(0 | 0 | 0) und B(2 | 0 | 0) den Lotfußpunkt "
                    "(5 | 0 | 0) außerhalb der Strecke; (3) wahr, denn "
                    "jeder Punkt der Geraden hat von ihr den Abstand null",
            pruef=""),
        umschreiben(
            finde(rows, 2, 2, 3),
            aufgabe="Jonas sagt: „Liegt der Lotfußpunkt von P auf der "
                    "Geraden AB außerhalb der Strecke AB, dann hat die "
                    "Gerade keinen Punkt mit kleinstem Abstand zu P.“ "
                    "Begründe, ohne genau zu rechnen, ob Jonas recht hat.",
            form="text",
            loesung="Nein; der Lotfußpunkt ist immer der Punkt der Geraden "
                    "mit dem kleinsten Abstand zu P, auch wenn er außerhalb "
                    "der Strecke liegt – nur auf der Strecke selbst ist "
                    "dann ein Endpunkt am nächsten.",
            pruef=""),
    ]
    return ersetze(out, neu)


# --- e4 -------------------------------------------------------------------

N4 = (1, 2, 2)           # L1: x + 2y + 2z = 9, L2: x + 2y + 2z = 0
P4 = (3, 1, 2)
SCHEIBEN = ("Zwei parallele Glasscheiben eines Wintergartens liegen in "
            "den Ebenen $L_1\\colon x + 2y + 2z = 9$ und "
            "$L_2\\colon x + 2y + 2z = 0$; 1 LE = 1 dm. Der Punkt "
            "$P(3 | 1 | 2)$ liegt in $L_1$.")


def e4():
    rows = lade("e4")
    out = []
    for r in rows:
        if r["hoehe"] == "grundfall":
            continue
        if r["hoehe"] == "vorstufe":
            out.append(nachziehen(r, sprosse_text=VORSTUFE_NEU[4]))
        else:
            out.append(nachziehen(r))
    alt = {r["variante"]: r for r in rows if r["hoehe"] == "grundfall"}
    frage = ("Ist die Strecke $PQ$ kleiner, größer oder genauso groß wie "
             "der Abstand der Scheiben? Begründe.")

    def vergleich(q, kennung=""):
        assert dot(N4, q) == 0
        pq = sub(q, P4)
        qq = dot(pq, pq)
        return pq, qq

    gf = []
    # v1: schräg, größer (Original 2023-bebb-gk-B3c)
    q = (2, 1, -2)
    pq, qq = vergleich(q)
    gf.append(umschreiben(
        alt[1], variante=1,
        aufgabe=f"{SCHEIBEN} Der Punkt $Q{T(*q)}$ liegt in $L_2$. {frage} "
                f"(Abitur 2023 GK)",
        form="text",
        loesung=f"größer; Richtung: $\\overrightarrow{{PQ}} = {T(*pq)}$ ist "
                f"kein Vielfaches des Normalenvektors ${T(*N4)}$, $PQ$ "
                f"steht schräg; Regel: das Lot ist die kürzeste "
                f"Verbindung; Kontrolle: $|\\overrightarrow{{PQ}}| = "
                f"\\sqrt{{{qq}}} \\approx {z(round(math.sqrt(qq), 2))}$, "
                f"Abstand der Scheiben $\\tfrac{{9}}{{3}} = 3$",
        pruef=f"[math.sqrt({qq}),3]"))
    # v2: Schrägstrecke gegeben (Original 2023MgrundlegendBAGLAA2WTR2-1e)
    q = (4, -2, 0)
    pq, qq = vergleich(q)
    lang = z(round(math.sqrt(qq), 2))
    gf.append(umschreiben(
        alt[2], variante=2,
        aufgabe=f"{SCHEIBEN} Die Strecke von $P$ zum Punkt $Q{T(*q)}$ der "
                f"Scheibe $L_2$ ist etwa ${lang}$ dm lang und steht nicht "
                f"senkrecht auf den Scheiben. Begründe ohne "
                f"Abstandsrechnung, dass der Abstand von $P$ zur Scheibe "
                f"$L_2$ kleiner ist als $PQ$. (Abitur 2023 GK)",
        form="text",
        loesung="Der Abstand ist die Länge des Lots von P auf die Scheibe; "
                "PQ ist schräg und damit die Hypotenuse eines "
                "rechtwinkligen Dreiecks mit dem Lot als Kathete – das Lot "
                "ist kürzer als PQ.",
        pruef=""))
    # v3: horizontal gegen schräg (Original 2021-be-gk-B2.2h)
    q = (-2, 3, -2)
    vergleich(q)
    gf.append(umschreiben(
        alt[3], variante=3,
        aufgabe=f"{SCHEIBEN} Der Punkt $Q{T(*q)}$ liegt in $L_2$. Die "
                f"horizontale Entfernung von $P$ und $Q$ ist der Abstand "
                f"ihrer Grundrisspunkte in der $xy$-Ebene. Begründe ohne "
                f"Rechnung, dass sie kürzer ist als die Strecke $PQ$. "
                f"(Abitur 2021 GK)",
        form="text",
        loesung="Horizontale Entfernung und Höhenunterschied von P und Q "
                "sind die Katheten eines rechtwinkligen Dreiecks, PQ ist "
                "seine Hypotenuse und damit länger als jede Kathete.",
        pruef=""))
    # v4: senkrecht, genauso groß
    q = (2, -1, 0)
    pq, qq = vergleich(q)
    gf.append(umschreiben(
        alt[4], variante=4,
        aufgabe=f"{SCHEIBEN} Der Punkt $Q{T(*q)}$ liegt in $L_2$. {frage}",
        form="text",
        loesung=f"genauso groß; Richtung: $\\overrightarrow{{PQ}} = "
                f"{T(*pq)}$ ist das Gegenstück des Normalenvektors "
                f"${T(*N4)}$, $PQ$ steht senkrecht und ist das Lot; "
                f"Kontrolle: $|\\overrightarrow{{PQ}}| = 3$, Abstand der "
                f"Scheiben $\\tfrac{{9}}{{3}} = 3$",
        pruef="3"))
    # v5: schräg, größer
    q = (2, 0, -1)
    pq, qq = vergleich(q)
    gf.append(umschreiben(
        alt[5], variante=5,
        aufgabe=f"{SCHEIBEN} Der Punkt $Q{T(*q)}$ liegt in $L_2$. {frage}",
        form="text",
        loesung=f"größer; Richtung: $\\overrightarrow{{PQ}} = {T(*pq)}$ ist "
                f"kein Vielfaches des Normalenvektors ${T(*N4)}$, $PQ$ "
                f"steht schräg; Regel: das Lot ist die kürzeste "
                f"Verbindung; Kontrolle: $|\\overrightarrow{{PQ}}| = "
                f"\\sqrt{{{qq}}} \\approx {z(round(math.sqrt(qq), 2))}$, "
                f"Abstand der Scheiben $\\tfrac{{9}}{{3}} = 3$",
        pruef=f"[math.sqrt({qq}),3]"))
    for r in gf:
        r["merkmal"] = alt[1]["merkmal"]
    i = next(i for i, r in enumerate(out)
             if r["kette_nr"] == 1 and r["sprosse"] == 2)
    out[i:i] = gf
    neu = [
        umschreiben(
            finde(rows, 2, 1, 2),
            aufgabe="Eine Wand liegt in der Ebene $W\\colon 4y + 3z = 24$, "
                    "ihre Bodenkante bei $y = 6$; 1 LE = 1 m. Ein Rechteck "
                    "der Wand bis in 1,6 m Höhe wird zu einem Vordach "
                    "geklappt. Mia rechnet: \\rechnung{4y + 3 \\cdot 1{,}6 "
                    "&= 24 \\\\ y &= 4{,}8 \\\\ \\text{Vordach} &= "
                    "\\sqrt{(6 - 4{,}8)^2 + 1{,}6^2} = 2 \\text{ m}} Prüfe, "
                    "ob Mia richtig gerechnet hat.",
            form="text",
            loesung="Richtig. Das Vordach wird in der geneigten Wand "
                    "gemessen: waagerechter Versatz und Höhe sind die "
                    "Katheten, das Vordach ist die Hypotenuse.",
            pruef=""),
        umschreiben(
            finde(rows, 2, 1, 3),
            aufgabe="$A(1 | 1 | -1)$ liegt in der Ebene "
                    "$L_1\\colon 2x + y + 2z = 1$, $B(2 | 5 | 2)$ in der "
                    "parallelen Ebene $L_2\\colon 2x + y + 2z = 13$; "
                    "$|\\overrightarrow{AB}| \\approx 5{,}10$. Vier Schüler "
                    "geben den Abstand der Ebenen an: (1) $4$, (2) $5{,}10$, "
                    "(3) $5{,}4$, (4) $-4$. Welche Ergebnisse können nicht "
                    "stimmen? Begründe, ohne genau zu rechnen.",
            form="text",
            loesung="(2) kann nicht stimmen – $\\overrightarrow{AB} = "
                    "(1 | 4 | 3)$ ist kein Vielfaches des Normalenvektors "
                    "(2 | 1 | 2), AB ist schräg und damit länger als der "
                    "Abstand; (3) kann nicht stimmen – der Abstand ist "
                    "höchstens so lang wie AB, das Lot ist die kürzeste "
                    "Verbindung; (4) kann nicht stimmen – ein Abstand ist "
                    "nie negativ",
            pruef=""),
        umschreiben(
            finde(rows, 2, 2, 2),
            aufgabe="Paul sagt: „Die horizontale Entfernung zweier Punkte "
                    "ist nie größer als ihre Verbindungsstrecke.“ Begründe, "
                    "ohne genau zu rechnen, ob Paul recht hat.",
            form="text",
            loesung="Ja; horizontale Entfernung und Höhenunterschied sind "
                    "die Katheten eines rechtwinkligen Dreiecks, die "
                    "Verbindungsstrecke ist die Hypotenuse – sie liegt dem "
                    "rechten Winkel gegenüber und ist die längste Seite; "
                    "gleich lang sind beide nur ohne Höhenunterschied.",
            pruef=""),
        umschreiben(
            finde(rows, 2, 2, 3),
            aufgabe="Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                    "ist. Begründe. (1) Der Mittelpunkt der Hypotenuse "
                    "eines rechtwinkligen Dreiecks ist von allen drei Ecken "
                    "gleich weit entfernt. (2) Jeder Punkt der "
                    "Symmetrieachse einer geraden quadratischen Pyramide "
                    "hat von allen vier Seitenflächen denselben Abstand. "
                    "(3) Eine Strecke zwischen zwei parallelen Ebenen ist "
                    "immer so lang wie der Abstand der Ebenen.",
            form="text",
            loesung="(1) wahr, denn nach dem Satz des Thales liegt die "
                    "Ecke mit dem rechten Winkel auf dem Kreis über der "
                    "Hypotenuse, dessen Mittelpunkt der Mittelpunkt der "
                    "Hypotenuse ist; (2) wahr, denn Vierteldrehungen um die "
                    "Achse bilden die Pyramide auf sich ab und jede "
                    "Seitenfläche auf die nächste; (3) falsch, z. B. "
                    "verbindet die Strecke von (0 | 0 | 0) nach (3 | 0 | 4) "
                    "die Ebenen z = 0 und z = 4, ist aber 5 lang",
            pruef=""),
        umschreiben(
            finde(rows, 2, 3, 3),
            aufgabe="Zwischen zwei senkrechten Bäumen mit den Fußpunkten "
                    "$A(-1 | 2 | 0)$ und $B(5 | -1 | 0)$ soll auf der Linie "
                    "durch $A$ und $B$ eine Tränke stehen, die von $A$ "
                    "doppelt so weit entfernt ist wie von $B$; 1 LE = 1 m. "
                    "Die Weide reicht auf dieser Linie nur 6 m über $B$ "
                    "hinaus. Passt die Position außerhalb der Bäume noch "
                    "auf die Weide?",
            form="text", antwort="\\janein",
            loesung="Nein; Verbindungsvektor: $\\overrightarrow{AB} = "
                    "(6 | -3 | 0)$; äußere Teilung: $T = A + 2 \\cdot "
                    "\\overrightarrow{AB} = (11 | -4 | 0)$; Abstand zu B: "
                    "$|\\overrightarrow{BT}| = |\\overrightarrow{AB}| = "
                    "\\sqrt{45} \\approx 6{,}71$ m $> 6$ m",
            pruef="[[11,-4,0],math.sqrt(45)]"),
    ]
    return ersetze(out, neu)


def zahlen(rows):
    c = {"uebernommen": 0, "neu": 0, "umgeschrieben": 0, "entfallen": 0}
    for r in rows:
        c[r.get("_art", "uebernommen")] += 1
    return c


def main(args):
    einheiten = args or ["e1", "e2", "e3", "e4"]
    fn = {"e1": e1, "e2": e2, "e3": e3, "e4": e4}
    zf = B / "nachzug-zahlen.json"
    alle = json.loads(zf.read_text()) if zf.exists() else {}
    for e in einheiten:
        rows = fn[e]()
        alt = len(lade(e))
        c = zahlen(rows)
        c["entfallen"] = alt - c["uebernommen"] - c["umgeschrieben"]
        alle[e] = c
        schreibe(e, rows)
        print(e, len(rows), c)
    zf.write_text(json.dumps(alle, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python3
"""Nachzug bank/stammfunktion-und-hauptsatz auf Katalog f038ccb
(2026-09-29), bank.md fünfte Fassung, Vorlage auftrag-eintrag.md
2026-09-29d. Einmalig; liest den Bestand, schreibt e1–e4 neu.

Änderungen: quelle der Ketten 97–100 → 94–97; Vorstufentexte länger
(Aufgaben gleich); e1 neue Sprosse 4 „drei verschiedene
Stammfunktionen …“, alte s4–s6 → s5–s7; e2 alte s2 „nur einsetzen“ →
Vorstufe s0 (4 Zeilen), alte s3–s5 → s2–s4; Päckchen je Kette (5
Grundfallzeilen neu); Pflichtformen P1/P2/P4/P6 (v2, v3 der fehler-
und begruenden-Zeilen neu, v1 nur merkmal).

Aufruf: python3 werkzeuge/einmalig/nachzug-stammfunktion-und-hauptsatz-2026-09-29.py [e1 e2 e3 e4]
"""
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

E = "stammfunktion-und-hauptsatz"
ORD = Path(__file__).resolve().parents[2] / "bank" / E
ZAEHL = {}

QUELLE = {97: 94, 98: 95, 99: 96, 100: 97}
VORSTUFE = {
    1: "„Ableiten oder aufleiten?“ – zu Aufgabentexten ankreuzen, in "
       "welche Richtung gerechnet wird (F gesucht oder f gesucht); "
       "nichts rechnen",
    3: "„Wer ist hier F, wer ist f?“ – zu Bildpaaren und Termpaaren "
       "die Rollen ankreuzen; nichts rechnen",
    4: "„Wo ist das Integral null?“ – an Graphen ankreuzen, ob gleiche "
       "Grenzen oder ausgeglichene Flächenstücke vorliegen; nichts "
       "rechnen",
}
M_FEHLER = ("Fehler finden in drei Formen: Schülerrechnung mit Fehler, "
            "fehlerfreie Vorlage prüfen, Serie ohne genaue Rechnung")
M_BEGR = ("begründen in drei Formen: Warum-Frage, Aussagenserie, "
          "Personenaussage")


BESTAND = "945b26c"   # letzter Commit des Bestands vor dem Nachzug


def lade(n):
    """Bestand aus dem Commit vor dem Nachzug (wiederholbar)."""
    import subprocess
    t = subprocess.run(
        ["git", "-C", str(ORD), "show",
         f"{BESTAND}:bank/{E}/e{n}.jsonl"],
        capture_output=True, text=True, check=True).stdout
    return [json.loads(z) for z in t.splitlines()]


def mid(a):
    s = a["sprosse"]
    s = f"s{s}" if s >= 0 else f"s-{-s}"
    a["id"] = f"{E}-e{a['einheit']}-k{a['kette_nr']}-{s}-v{a['variante']}"
    return a


def zeile(n, k, s, v, kette, stext, merkmal, hoehe, aufgabe, form,
          antwort, loesung, pruef, quelle, original=None, grafik="",
          lgrafik="", pflicht=None):
    a = {"id": "", "eintrag": E, "einheit": n, "kette": kette,
         "kette_nr": k, "sprosse": s, "sprosse_text": stext,
         "merkmal": merkmal, "hoehe": hoehe}
    if pflicht:
        a["pflicht"] = pflicht
    a.update({"variante": v, "aufgabe": aufgabe, "form": form,
              "antwort": antwort, "loesung": loesung, "pruef": pruef,
              "original": original, "grafik": grafik,
              "loesungsgrafik": lgrafik, "quelle": quelle})
    return mid(a)


def zieh(a, **neu):
    """übernommen: nur id, sprosse, kette_nr, quelle, sprosse_text
    (und hoehe beim Wechsel zur Vorstufe)."""
    b = dict(a)
    b.update(neu)
    if b["quelle"] in QUELLE:
        b["quelle"] = QUELLE[b["quelle"]]
    return mid(b)


def pflicht_um(a, text=None):
    b = dict(a)
    b["merkmal"] = M_FEHLER if b["pflicht"] == "fehler" else M_BEGR
    if text:
        b.update(text)
    return mid(b)


def zaehle(n, alt, neu, zeilen):
    ZAEHL[n] = (len(zeilen) - neu - alt, neu, alt)


def txt(x):
    """Bruch als LaTeX."""
    x = Fr(x)
    if x.denominator == 1:
        return str(x.numerator)
    s = "-" if x < 0 else ""
    return f"{s}\\frac{{{abs(x.numerator)}}}{{{x.denominator}}}"


# --- e1 ----------------------------------------------------------------

def e1():
    alt = lade(1)
    aus, um, neu = [], 0, 0
    K = "Stammfunktion"
    for a in alt:
        k, s, v = a["kette_nr"], a["sprosse"], a["variante"]
        if k == 1 and s == 0:
            aus.append(zieh(a, sprosse_text=VORSTUFE[1]))
        elif k == 1 and s == 1:
            if v <= 4:
                r = [2, 3, 4, 5][v - 1]
                aus.append(zeile(
                    1, 1, 1, v, K, a["sprosse_text"],
                    "ganzrationaler Term mit Klammer: erst ausmultiplizieren, "
                    "dann gliedweise aufleiten; die Form r² − (r − x)² "
                    "bleibt, r wandert", "grundfall",
                    f"Gib eine Stammfunktion $F$ von "
                    f"$f(x) = {r*r} - ({r} - x)^2$ an.",
                    "teil", "$F(x) = $ __",
                    f"Klammer ausmultiplizieren: $f(x) = {r*r} - "
                    f"({r*r} - {2*r}x + x^2) = {2*r}x - x^2$; gliedweise "
                    f"aufleiten: $F(x) = {r}x^2 - \\frac{{1}}{{3}}x^3$; "
                    f"Ergebnis: $F(x) = {r}x^2 - \\frac{{1}}{{3}}x^3$",
                    str(r), 94))
                um += 1
            else:  # v5: Kugelschale, schon in der Form r² − (r − x)²
                b = zieh(a)
                b["loesung"] = (
                    "Klammer ausmultiplizieren: $q(x) = \\pi \\cdot (60x - "
                    "x^2)$; "
                    "gliedweise aufleiten: $Q(x) = \\pi \\cdot (30x^2 - "
                    "\\frac{1}{3}x^3)$; Ergebnis: $Q(x) = 30\\pi x^2 - "
                    "\\frac{\\pi}{3}x^3$")
                b["merkmal"] = ("ganzrationaler Term mit Klammer: erst "
                                "ausmultiplizieren, dann gliedweise "
                                "aufleiten; die Form r² − (r − x)² bleibt, "
                                "r wandert")
                aus.append(b)
                um += 1
        elif k == 1 and s in (2, 3):
            aus.append(zieh(a))
            if s == 3 and v == 3:
                aus += e1_s4()
                neu += 3
        elif k == 1 and s >= 4:
            aus.append(zieh(a, sprosse=s + 1))
        elif k == 2:
            aus.append(e1_pflicht(a))
            um += 1
    return aus, um, neu


def e1_s4():
    st = ("drei verschiedene Stammfunktionen angeben und in ein "
          "Koordinatensystem zeichnen; sagen, wie sie auseinander "
          "hervorgehen")
    m = ("neu: mehrere Stammfunktionen nebeneinander, die Konstante als "
         "Verschiebung in y-Richtung")
    fall = [
        ("2x + 4", "x^2 + 4x", "\\x^2+4*\\x", -5, 1, -7, 4),
        ("-x", "-\\frac{1}{2}x^2", "-0.5*\\x^2", -3, 3, -6, 4),
        ("x^2 - 1", "\\frac{1}{3}x^3 - x", "\\x^3/3-\\x", -3, 3, -5, 5),
    ]
    aus = []
    for v, (f, F, Fx, x0, x1, y0, y1) in enumerate(fall, 1):
        ks = f"xmin={x0},xmax={x1},ymin={y0},ymax={y1}"
        aus.append(zeile(
            1, 1, 4, v, "Stammfunktion", st, m, "sprosse",
            f"Gegeben ist $f(x) = {f}$. Gib drei verschiedene "
            f"Stammfunktionen von $f$ an und zeichne ihre Graphen in das "
            f"Koordinatensystem. Beschreibe, wie die Graphen auseinander "
            f"hervorgehen.",
            "zeichnen", "",
            f"aufleiten: $F(x) = {F} + c$; Konstante wählen: $c = 0$, "
            f"$c = 2$ und $c = -2$; Stammfunktionen: $F_1(x) = {F}$, "
            f"$F_2(x) = {F} + 2$, $F_3(x) = {F} - 2$; Ergebnis: Die "
            f"Graphen gehen durch Verschieben in y-Richtung auseinander "
            f"hervor, an jeder Stelle haben sie dieselbe Steigung $f(x)$.",
            "", 94,
            grafik=f"\\begin{{ksys}}[{ks}] \\end{{ksys}}",
            lgrafik=(f"\\begin{{ksys}}[{ks},klein] \\funktion{{{Fx}}}{{F_1}} "
                     f"\\funktion{{{Fx}+2}}{{F_2}} "
                     f"\\funktion{{{Fx}-2}}{{F_3}} \\end{{ksys}}")))
    return aus


def e1_pflicht(a):
    s, v = a["sprosse"], a["variante"]
    if v == 1:
        return pflicht_um(a)
    if s == 1 and v == 2:  # P2
        return pflicht_um(a, {
            "aufgabe": "Zu $f(x) = 6x^2 - 2x$ gibt Lea die Stammfunktion "
                       "$F(x) = 2x^3 - x^2 + 7$ an. Prüfe, ob Lea richtig "
                       "gerechnet hat.",
            "loesung": "Richtig. Ableiten ergibt $F'(x) = 6x^2 - 2x = "
                       "f(x)$; die Konstante $7$ fällt beim Ableiten weg.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 1 and v == 3:  # P1
        return pflicht_um(a, {
            "aufgabe": "Zu $f(x) = 8x^3 + 6x$ haben vier Schüler eine "
                       "Stammfunktion angegeben: (1) $2x^4 + 3x^2$ "
                       "(2) $24x^2 + 6$ (3) $2x^4 + 3x^2 - 5$ "
                       "(4) $2x^4 + 6x^2$. Welche Ergebnisse können nicht "
                       "stimmen? Begründe, ohne genau zu rechnen.",
            "loesung": "(2) nicht: Der Exponent ist kleiner geworden, "
                       "hier wurde abgeleitet statt aufgeleitet; (4) "
                       "nicht: Beim Aufleiten von $6x$ wird durch den neuen "
                       "Exponenten $2$ geteilt, der Vorfaktor von $x^2$ "
                       "muss $3$ sein.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 2 and v == 2:  # P4
        return pflicht_um(a, {
            "aufgabe": "Entscheide bei jeder Aussage, ob sie wahr oder "
                       "falsch ist. Begründe, ohne genau zu rechnen. "
                       "(1) Zu jeder ganzrationalen Funktion gibt es "
                       "unendlich viele Stammfunktionen. (2) Zwei "
                       "Stammfunktionen derselben Funktion haben immer "
                       "denselben Graphen. (3) Um nachzuweisen, dass $F$ "
                       "eine Stammfunktion von $f$ ist, leitet man immer "
                       "$F$ ab.",
            "loesung": "(1) wahr, denn mit $F$ ist auch $F + c$ für jede "
                       "Zahl $c$ eine Stammfunktion; (2) falsch, z. B. "
                       "sind $x^2$ und $x^2 + 4$ Stammfunktionen von $2x$ "
                       "mit verschiedenen Graphen; (3) wahr, denn "
                       "Stammfunktion heißt $F' = f$, und das prüft die "
                       "Ableitung von $F$.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 2 and v == 3:  # P6
        return pflicht_um(a, {
            "aufgabe": "Tim sagt: „$F(x) = x^3 + 5$ ist keine Stammfunktion "
                       "von $f(x) = 3x^2$, denn beim Aufleiten von $3x^2$ "
                       "kommt $x^3$ heraus.“ Begründe, ob Tim recht hat.",
            "loesung": "Nein; $F'(x) = 3x^2 = f(x)$, die Konstante $5$ "
                       "fällt beim Ableiten weg – jede Funktion $x^3 + c$ "
                       "ist eine Stammfunktion von $f$.",
            "pruef": "", "form": "text", "antwort": ""})
    raise ValueError(a["id"])


# --- e2 ----------------------------------------------------------------

def e2():
    alt = lade(2)
    aus, um, neu = [], 0, 0
    K = "Hauptsatz"
    st0 = ("mit vorgegebener Stammfunktion nur einsetzen: F(b) − F(a), "
           "auch mit negativem F(a)")
    vor = [a for a in alt if a["kette_nr"] == 1 and a["sprosse"] == 2]
    for a in vor:
        aus.append(zieh(a, sprosse=0, hoehe="vorstufe", sprosse_text=st0))
    aus.append(zeile(
        2, 1, 0, 4, K, st0, vor[0]["merkmal"], "vorstufe",
        "$F(x) = x^3 + 2x$ ist eine Stammfunktion von $f$. Berechne den "
        "Wert des Integrals von $-1$ bis $2$ über $f(x)$. Setze dazu nur "
        "die Grenzen ein.",
        "teil", "Wert: __",
        "Klammer: $\\left[x^3 + 2x\\right]_{-1}^{2}$; einsetzen: "
        "$F(2) - F(-1) = 12 - (-3) = 15$; Ergebnis: $15$",
        "15", 95))
    neu += 1
    for a in alt:
        k, s, v = a["kette_nr"], a["sprosse"], a["variante"]
        if k == 1 and s == 1:
            p = [2, 4, -2, -4, 6][v - 1]
            F2 = 8 + 2 * p
            Fm = Fr(-1) + Fr(p, 2)
            w = F2 - Fm
            h = Fr(p, 2)
            Ft = "x^3" + (f" + {txt(h)}x^2" if h > 0 else
                          f" - {txt(-h)}x^2").replace(" 1x", " x")
            fm = f"{txt(Fm)}" if Fm >= 0 else f"({txt(Fm)})"
            tag = {4: " (Abitur 2023 GK)", 5: " (Abitur 2018 GK)"}.get(v, "")
            ft = f"3x^2 + {p}x" if p > 0 else f"3x^2 - {-p}x"
            b = zeile(
                2, 1, 1, v, K, a["sprosse_text"],
                "Stammfunktion gliedweise bilden, obere Grenze einsetzen, "
                "untere abziehen; f(x) = 3x² + a · x auf [−1; 2] bleibt, "
                "a wandert", "grundfall",
                f"Berechne den Wert des Integrals von $-1$ bis $2$ über "
                f"$f(x) = {ft}$.{tag}",
                "teil", "Wert: __",
                f"Stammfunktion bilden: $F(x) = {Ft}$; Klammer: "
                f"$\\left[{Ft}\\right]_{{-1}}^{{2}}$; einsetzen: "
                f"$F(2) - F(-1) = {F2} - {fm} = {txt(w)}$; Ergebnis: "
                f"${txt(w)}$",
                str(w), 95, original=a["original"])
            aus.append(b)
            um += 1
        elif k == 1 and s == 2:
            continue
        elif k == 1 and s >= 3:
            aus.append(zieh(a, sprosse=s - 1))
        elif k == 2:
            aus.append(zieh(a))
        elif k == 3:
            aus.append(e2_pflicht(a))
            um += 1
    # Reihenfolge: Vorstufe vor Grundfall
    aus.sort(key=lambda a: (a["kette_nr"], a["sprosse"], a["variante"]))
    return aus, um, neu


def e2_pflicht(a):
    s, v = a["sprosse"], a["variante"]
    if s == 1 and v == 1:
        return pflicht_um(a)
    if s == 2 and v == 1:
        return pflicht_um(a)
    if s == 1 and v == 2:  # P2
        return pflicht_um(a, {
            "aufgabe": "Emil berechnet das Integral von $-2$ bis $1$ über "
                       "$f(x) = 2x + 3$ so: $F(x) = x^2 + 3x$; "
                       "$F(1) - F(-2) = 4 - (-2) = 6$. Prüfe, ob Emil "
                       "richtig gerechnet hat.",
            "loesung": "Richtig. Die obere Grenze kommt zuerst, und der "
                       "negative Wert $F(-2) = -2$ wird abgezogen: "
                       "$4 - (-2) = 6$.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 1 and v == 3:  # P1
        return pflicht_um(a, {
            "aufgabe": "Für das Integral von $0$ bis $2$ über "
                       "$f(x) = 3x^2 + 1$ haben vier Schüler einen Wert "
                       "angegeben: (1) $10$ (2) $-10$ (3) $30$ (4) $1$. "
                       "Welche Ergebnisse können nicht stimmen? Begründe, "
                       "ohne genau zu rechnen.",
            "loesung": "(2) nicht: $f$ ist zwischen $0$ und $2$ positiv, "
                       "der Wert muss positiv sein – die Grenzen sind "
                       "vertauscht; (3) nicht: $f$ ist dort höchstens "
                       "$13$, der Wert also höchstens $2 \\cdot 13 = 26$; "
                       "(4) nicht: $f$ ist dort mindestens $1$, der Wert "
                       "also mindestens $2 \\cdot 1 = 2$.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 2 and v == 2:  # P4
        return pflicht_um(a, {
            "aufgabe": "Entscheide bei jeder Aussage, ob sie wahr oder "
                       "falsch ist. Begründe, ohne genau zu rechnen. "
                       "(1) Vertauscht man die Grenzen eines Integrals, "
                       "ändert sich immer nur das Vorzeichen des Werts. "
                       "(2) Das Integral von $0$ bis $2\\pi$ über "
                       "$\\mathrm{cos}(x)$ ist null. (3) Ist eine Funktion "
                       "irgendwo zwischen den Grenzen negativ, ist ihr "
                       "Integral immer negativ.",
            "loesung": "(1) wahr, denn $F(a) - F(b) = -(F(b) - F(a))$; "
                       "(2) wahr, denn über eine volle Periode heben sich "
                       "die Flächenstücke über und unter der x-Achse auf; "
                       "(3) falsch, z. B. ist das Integral von $-1$ bis "
                       "$2$ über $x$ gleich $2 - \\frac{1}{2} = "
                       "\\frac{3}{2}$, obwohl $x$ für $x < 0$ negativ ist.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 2 and v == 3:  # P6
        return pflicht_um(a, {
            "aufgabe": "$F(x) = e^{x} + 2x$ ist eine Stammfunktion von $f$. "
                       "Nora sagt: „Das Integral von $0$ bis $1$ über "
                       "$f(x)$ ist einfach $F(1)$, weil die untere Grenze "
                       "$0$ ist.“ Begründe, ob Nora recht hat.",
            "loesung": "Nein; die untere Grenze $0$ macht $F(0)$ nicht zu "
                       "null: $F(0) = e^{0} + 0 = 1$, also ist der Wert "
                       "$F(1) - F(0) = e + 2 - 1 = e + 1$.",
            "pruef": "", "form": "text", "antwort": ""})
    raise ValueError(a["id"])


# --- e3 ----------------------------------------------------------------

def e3():
    alt = lade(3)
    aus, um, neu = [], 0, 0
    for a in alt:
        k, s, v = a["kette_nr"], a["sprosse"], a["variante"]
        if k == 1 and s == 0:
            aus.append(zieh(a, sprosse_text=VORSTUFE[3]))
        elif k == 1 and s == 1:
            aus.append(e3_grund(a))
            um += 1
        elif k == 1:
            aus.append(zieh(a))
        else:
            aus.append(e3_pflicht(a))
            um += 1
    return aus, um, neu


def e3_grund(a):
    import math
    v = a["variante"]
    e = [Fr(-2), Fr(-9, 8), Fr(1), Fr(-1, 2), Fr(0)][v - 1]
    tag = {3: " (Abitur 2023 GK)", 4: " (Abitur 2021 GK)",
           5: " (Abitur 2023 LK)"}.get(v, "")
    x0, x1, y0, y1 = -3, 5, -4, 4

    def F(x):
        return (x - 1) ** 3 / 6 + float(e) * x + 7 / 6
    xs = [x0 + i * 0.01 for i in range(int((x1 - x0) / 0.01) + 1)]
    innen = [x for x in xs if y0 + 0.2 <= F(x) <= y1 - 0.2]
    xa, xb = round(min(innen), 1), round(max(innen), 1)
    ef = f"{float(e):g}"
    Fx = (f"(\\x-1)*(\\x-1)*(\\x-1)/6" +
          ("" if e == 0 else (f"+{ef}*\\x" if e > 0 else f"{ef}*\\x")) +
          "+7/6")

    def dz(x):
        return f"{float(x):g}".replace(".", "{,}")
    if e < 0:
        r = math.sqrt(float(-2 * e))
        n1, n2 = 1 - r, 1 + r
        loes = (f"Nullstellen von $f$: $x = {dz(n1)}$ und $x = {dz(n2)}$; "
                f"Vorzeichen von $f$: plus, minus, plus; Extremstellen von "
                f"$F$: Hochpunkt bei $x = {dz(n1)}$, Tiefpunkt bei "
                f"$x = {dz(n2)}$; Wendestelle von $F$: $x = 1$, wo $f$ "
                f"seinen Tiefpunkt hat; Ergebnis: $F$ steigt bis "
                f"${dz(n1)}$, fällt bis ${dz(n2)}$, steigt dann wieder und "
                f"geht durch $P(0 | 1)$.")
        pruef = f"[{n1:g}, {n2:g}, 1]"
    elif e == 0:
        loes = ("Nullstellen von $f$: nur $x = 1$, ohne Vorzeichenwechsel; "
                "Monotonie: $F$ steigt überall, weil $f \\ge 0$ ist; "
                "Terrassenpunkt von $F$: bei $x = 1$, dort ist die "
                "Tangente waagerecht und zugleich die Wendestelle; "
                "Ergebnis: $F$ steigt, flacht bei $1$ bis zur Waagerechten "
                "ab, steigt dann wieder steiler und geht durch $P(0 | 1)$.")
        pruef = "[1]"
    else:
        loes = ("Nullstellen von $f$: keine, $f$ ist überall positiv; "
                "Monotonie: $F$ steigt überall, hat also keinen Hoch- oder "
                "Tiefpunkt; Wendestelle von $F$: $x = 1$, wo $f$ seinen "
                "Tiefpunkt hat, dort steigt $F$ am schwächsten; Ergebnis: "
                "$F$ steigt überall und geht durch $P(0 | 1)$.")
        pruef = "[1]"
    b = dict(a)
    b.update({
        "merkmal": "F aus dem Graphen von f skizzieren: Vorzeichen gibt "
                   "Monotonie, Nullstellen Extremstellen, Extremstellen "
                   "Wendestellen; die Parabel f(x) = ½(x − 1)² + e und "
                   "P(0 | 1) bleiben, e wandert",
        "aufgabe": "Das Bild zeigt den Graphen von $f$. Skizziere den "
                   "Graphen der Stammfunktion $F$ von $f$, die durch "
                   f"$P(0 | 1)$ geht.{tag}",
        "loesung": loes, "pruef": pruef,
        "grafik": (f"\\begin{{ksys}}[xmin={x0},xmax={x1},ymin={y0},"
                   f"ymax={y1}] \\parabel{{0.5}}{{1}}{{{ef}}}{{f}} "
                   f"\\punkt{{0}}{{1}}{{P}} \\end{{ksys}}"),
        "loesungsgrafik": (f"\\begin{{ksys}}[xmin={x0},xmax={x1},"
                           f"ymin={y0},ymax={y1},klein] "
                           f"\\parabel{{0.5}}{{1}}{{{ef}}}{{f}} "
                           f"\\funktionab{{{Fx}}}{{F}}{{{xa:g}}}{{{xb:g}}} "
                           f"\\end{{ksys}}"),
        "quelle": 96})
    return mid(b)


def e3_pflicht(a):
    s, v = a["sprosse"], a["variante"]
    if v == 1:
        return pflicht_um(a)
    if s == 1 and v == 2:  # P2
        return pflicht_um(a, {
            "aufgabe": "Für $f(x) = (x + 2) \\cdot (x - 4)$ schreibt Jana: "
                       "„Jede Stammfunktion von $f$ hat bei $x = -2$ einen "
                       "Hochpunkt und bei $x = 4$ einen Tiefpunkt.“ Prüfe, "
                       "ob Jana richtig entschieden hat.",
            "loesung": "Richtig. $f$ ist eine nach oben geöffnete Parabel: "
                       "bei $-2$ wechselt $f$ von plus nach minus, also hat "
                       "jede Stammfunktion dort einen Hochpunkt; bei $4$ "
                       "wechselt $f$ von minus nach plus, dort liegt ein "
                       "Tiefpunkt.",
            "pruef": "", "form": "text", "antwort": "", "grafik": "",
            "loesungsgrafik": ""})
    if s == 1 and v == 3:  # P1
        return pflicht_um(a, {
            "aufgabe": "Zu $f(x) = 2 - x$ haben vier Schüler den Graphen "
                       "einer Stammfunktion $F$ beschrieben: (1) Tiefpunkt "
                       "bei $x = 2$ (2) Hochpunkt bei $x = 2$ "
                       "(3) Hochpunkt bei $x = 0$ (4) Wendepunkt bei "
                       "$x = 2$. Welche Ergebnisse können nicht stimmen? "
                       "Begründe, ohne genau zu rechnen.",
            "loesung": "(1) nicht: $f$ wechselt bei $2$ von plus nach "
                       "minus, dort hat $F$ einen Hochpunkt; (3) nicht: bei "
                       "$0$ ist $f$ positiv, $F$ steigt dort; (4) nicht: "
                       "$f$ ist eine Gerade ohne Extrempunkt, also hat $F$ "
                       "keinen Wendepunkt.",
            "pruef": "", "form": "text", "antwort": "", "grafik": "",
            "loesungsgrafik": ""})
    if s == 2 and v == 2:  # P4
        return pflicht_um(a, {
            "aufgabe": "Entscheide bei jeder Aussage, ob sie wahr oder "
                       "falsch ist. Begründe, ohne genau zu rechnen. "
                       "(1) Wo $f$ positiv ist, steigt jede Stammfunktion "
                       "von $f$. (2) Hat $f$ bei $x = 1$ einen Hochpunkt, "
                       "dann hat jede Stammfunktion von $f$ dort einen "
                       "Hochpunkt. (3) Durch jeden Punkt geht der Graph "
                       "genau einer Stammfunktion von $f$.",
            "loesung": "(1) wahr, denn $F' = f > 0$ heißt, $F$ steigt; "
                       "(2) falsch, z. B. hat $f(x) = -x^2 + 2x$ bei $1$ "
                       "einen Hochpunkt, jede Stammfunktion hat dort eine "
                       "Wendestelle; (3) wahr, denn die Konstante "
                       "verschiebt den Graphen in y-Richtung und lässt "
                       "sich für jeden Punkt genau passend wählen.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 2 and v == 3:  # P6
        return pflicht_um(a, {
            "aufgabe": "Mara sagt: „$f(x) = (x - 2)^2$ wird bei $x = 2$ "
                       "null, also hat jede Stammfunktion von $f$ bei "
                       "$x = 2$ einen Extrempunkt.“ Begründe, ob Mara "
                       "recht hat.",
            "loesung": "Nein; $f$ wechselt bei $2$ das Vorzeichen nicht, "
                       "denn $f \\ge 0$; jede Stammfunktion steigt auf "
                       "beiden Seiten, bei $2$ liegt ein Terrassenpunkt.",
            "pruef": "", "form": "text", "antwort": ""})
    raise ValueError(a["id"])


# --- e4 ----------------------------------------------------------------

def e4():
    alt = lade(4)
    aus, um, neu = [], 0, 0
    for a in alt:
        k, s, v = a["kette_nr"], a["sprosse"], a["variante"]
        if k == 1 and s == 0:
            aus.append(zieh(a, sprosse_text=VORSTUFE[4]))
        elif k == 1 and s == 1:
            g = [2, -1, 3, -3, 1][v - 1]
            b = dict(a)
            b.update({
                "merkmal": "die untere Grenze ist Nullstelle von J, und J' "
                           "ist der Integrand; f(t) = t² − 2t bleibt, die "
                           "untere Grenze wandert",
                "aufgabe": f"$J(x)$ ist das Integral von ${g}$ bis $x$ über "
                           f"$f(t) = t^2 - 2t$. Gib eine Nullstelle von $J$ "
                           f"und den Term von $J'$ an.",
                "antwort": "Nullstelle: __, $J'(x) = $ __",
                "loesung": f"untere Grenze: $J({g}) = 0$, also Nullstelle "
                           f"$x = {g}$; Ableitung ist der Integrand: "
                           f"$J'(x) = x^2 - 2x$",
                "pruef": str(g), "quelle": 97})
            aus.append(mid(b))
            um += 1
        elif k == 1:
            aus.append(zieh(a))
        elif k in (2, 3):
            aus.append(zieh(a))
        else:
            aus.append(e4_pflicht(a))
            um += 1
    return aus, um, neu


def e4_pflicht(a):
    s, v = a["sprosse"], a["variante"]
    if v == 1:
        return pflicht_um(a)
    if s == 1 and v == 2:  # P2
        return pflicht_um(a, {
            "aufgabe": "$J(x)$ ist das Integral von $1$ bis $x$ über "
                       "$f(t) = 2t - 4$. Finn rechnet: $J(x) = x^2 - 4x + "
                       "3$, die Nullstellen sind $x = 1$ und $x = 3$. "
                       "Prüfe, ob Finn richtig gerechnet hat.",
            "loesung": "Richtig. Der Wert an der unteren Grenze wird "
                       "abgezogen: $J(x) = (x^2 - 4x) - (1 - 4) = x^2 - 4x "
                       "+ 3 = (x - 1) \\cdot (x - 3)$; die untere Grenze "
                       "$1$ ist wie immer eine Nullstelle.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 1 and v == 3:  # P1
        return pflicht_um(a, {
            "aufgabe": "$J(x)$ ist das Integral von $2$ bis $x$ über "
                       "$f(t) = 3t^2$. Vier Schüler geben Werte an: "
                       "(1) $J(2) = 12$ (2) $J(3) = 19$ (3) $J(0) = 8$ "
                       "(4) $J(1) = -7$. Welche Ergebnisse können nicht "
                       "stimmen? Begründe, ohne genau zu rechnen.",
            "loesung": "(1) nicht: An der unteren Grenze ist $J$ immer "
                       "null; (3) nicht: Für $x < 2$ läuft das Integral "
                       "rückwärts über ein positives $f$, der Wert muss "
                       "negativ sein.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 2 and v == 2:  # P4
        return pflicht_um(a, {
            "aufgabe": "Entscheide bei jeder Aussage, ob sie wahr oder "
                       "falsch ist. Begründe, ohne genau zu rechnen. "
                       "(1) Jede Integralfunktion hat mindestens eine "
                       "Nullstelle. (2) Jede Nullstelle des Integranden "
                       "ist auch eine Nullstelle der Integralfunktion. "
                       "(3) Ist der Integrand ganzrational vom Grad $2$, "
                       "hat die Integralfunktion höchstens drei "
                       "Nullstellen.",
            "loesung": "(1) wahr, denn an ihrer unteren Grenze ist sie "
                       "null; (2) falsch, z. B. hat $f(t) = t - 1$ die "
                       "Nullstelle $1$, das Integral von $0$ bis $1$ über "
                       "$f$ ist aber $-\\frac{1}{2}$; (3) wahr, denn die "
                       "Integralfunktion hat dann den Grad $3$.",
            "pruef": "", "form": "text", "antwort": ""})
    if s == 2 and v == 3:  # P6
        return pflicht_um(a, {
            "aufgabe": "$J(x)$ ist das Integral von $0$ bis $x$ über "
                       "$f(t) = t^2 - 9$. Lukas sagt: „$J$ hat die "
                       "Nullstellen $-3$ und $3$.“ Begründe, ob Lukas "
                       "recht hat.",
            "loesung": "Nein; $-3$ und $3$ sind Nullstellen des "
                       "Integranden, dort hat $J$ Extremstellen. Es ist "
                       "$J(x) = \\frac{1}{3}x^3 - 9x$ mit den Nullstellen "
                       "$0$ und $\\pm\\sqrt{27}$.",
            "pruef": "", "form": "text", "antwort": ""})
    raise ValueError(a["id"])


def schreibe(n, zeilen):
    (ORD / f"e{n}.jsonl").write_text(
        "".join(json.dumps(z, ensure_ascii=False) + "\n" for z in zeilen),
        encoding="utf-8")


if __name__ == "__main__":
    welche = sys.argv[1:] or ["e1", "e2", "e3", "e4"]
    for w in welche:
        n = int(w[1])
        alt = lade(n)
        zeilen, um, neu = {1: e1, 2: e2, 3: e3, 4: e4}[n]()
        schreibe(n, zeilen)
        ueb = len(zeilen) - um - neu
        ent = len(alt) - ueb - um
        print(f"e{n}: {len(zeilen)} Zeilen; übernommen {ueb}, neu {neu}, "
              f"umgeschrieben {um}, entfallen {ent}")

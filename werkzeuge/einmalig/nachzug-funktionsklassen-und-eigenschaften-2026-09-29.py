"""Nachzug bank/funktionsklassen-und-eigenschaften auf Katalog f56cace
(Mappe 29.09.) und bank.md fünfte Fassung (29b).

Einmalig, 2026-09-29. Aufruf aus der Repo-Wurzel:
    python3 werkzeuge/einmalig/nachzug-funktionsklassen-und-eigenschaften-2026-09-29.py e1 … e6
Liest den Bestand vom 27.09. (Katalog 95b0f8b), zieht quelle
(139–144 -> 135–140), sprosse, id und sprosse_text nach (Vorstufen mit
längerem Katalogtext), schreibt die Päckchen je Verfahrenskette, die
neuen Sprossen (e2 s6 „rückwärts“, e5 s0 „im Argument ausklammern“),
die Prüfungszeilen zu 2023-A-2d und die Pflichtformen P1–P8; schreibt
je Einheit die ganze Datei. Zählt übernommen/neu/umgeschrieben/
entfallen (Ausgabe auf stdout). Übernommene Zeilen bleiben wortgleich
bis auf id, sprosse, kette_nr, quelle, sprosse_text.
"""
import copy
import json
import sys

E = "funktionsklassen-und-eigenschaften"
B = f"bank/{E}/"
QMAP = {139: 135, 140: 136, 141: 137, 142: 138, 143: 139, 144: 140}

# Vorstufen: Katalogtext jetzt länger (wortgleich aus Zeile 135–139, ohne
# die Klammer „(Vorstufe …)“, wie die übrigen Sprossentexte)
VOR = {
    1: ("„Wert oder Stelle?“ – zu Aufgabentexten ankreuzen: Stelle gegeben "
        "und Wert gesucht (einsetzen) oder Wert gegeben und Stelle gesucht "
        "(ablesen oder Gleichung lösen); nichts rechnen"),
    2: ("„Welches Nullstellenverfahren?“ – zu Termen ankreuzen: Produktform "
        "(ablesen), ohne Absolutglied (ausklammern), biquadratisch "
        "(substituieren), Nullstelle bekannt (Polynomdivision), quadratisch "
        "(Lösungsformel); nichts rechnen"),
    4: ("„Gerade oder ungerade Exponenten?“ – zu Termen die Exponenten "
        "markieren, das Absolutglied als gerade zählen und ankreuzen: "
        "achsensymmetrisch, punktsymmetrisch, keines von beiden; nichts "
        "rechnen"),
    5: ("„Innen oder außen?“ – zu Termpaaren ankreuzen, ob die Änderung im "
        "Argument steht (x-Richtung, gegenläufig) oder außen am Term "
        "(y-Richtung); nichts rechnen"),
}
T_E5_S0 = ("im Argument ausklammern: bx + c als b · (x + c/b) schreiben, die "
           "Verschiebung um c/b ablesen, noch nichts zeichnen")
T_E2_S6 = ("rückwärts: einen Koeffizienten so bestimmen, dass eine gegebene "
           "Zahl Nullstelle ist; Kontrolle durch Faktorisieren")

M_FEHLER = ("Fehler finden in drei Formen: Schülerrechnung mit Fehler, "
            "fehlerfreie Vorlage prüfen, Serie ohne genaue Rechnung")
M_BEGR = ("begründen in drei Formen: Warum-Frage, Aussagenserie, "
          "Personenaussage")
SERIE = "Welche Ergebnisse können nicht stimmen? Begründe, ohne genau zu rechnen."
P4 = ("Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
      "Begründe, ohne genau zu rechnen.")


def lade(n):
    return [json.loads(z) for z in
            open(f"{B}e{n}.jsonl", encoding="utf-8").read().splitlines()]


def schreibe(n, rows):
    with open(f"{B}e{n}.jsonl", "w", encoding="utf-8", newline="\n") as h:
        for r in rows:
            h.write(json.dumps({k: v for k, v in r.items()
                                if not k.startswith("_")},
                               ensure_ascii=False) + "\n")


def setze(r, _st="um", **kw):
    r = copy.deepcopy(r)
    r.update(kw)
    r["_st"] = _st
    return r


def reihe(rows, k, s):
    return [r for r in rows if r["kette_nr"] == k and r["sprosse"] == s]


def ersetze(rows, k, s, neu):
    aus, drin = [], False
    for r in rows:
        if r["kette_nr"] == k and r["sprosse"] == s:
            if not drin:
                aus.extend(neu)
                drin = True
        else:
            aus.append(r)
    return aus


def nach(rows, k, s, neu):
    """neu hinter die letzte Zeile von Kette k, Sprosse s."""
    i = max(j for j, r in enumerate(rows)
            if r["kette_nr"] == k and r["sprosse"] == s)
    return rows[:i + 1] + neu + rows[i + 1:]


def nachziehen(rows, n):
    for r in rows:
        r["quelle"] = QMAP.get(r["quelle"], r["quelle"])
        if r["hoehe"] == "vorstufe" and n in VOR and r["sprosse"] == 0 \
                and r.get("_st") is None:
            r["sprosse_text"] = VOR[n]
        r["id"] = (f"{E}-e{n}-k{r['kette_nr']}-s{r['sprosse']}"
                   f"-v{r['variante']}")
    return rows


def zaehle(n, rows):
    z = {"übernommen": 0, "neu": 0, "umgeschrieben": 0}
    for r in rows:
        z[{"neu": "neu", "um": "umgeschrieben"}.get(r.get("_st"),
                                                     "übernommen")] += 1
    print(f"e{n}: {len(rows)} Zeilen, übernommen {z['übernommen']}, "
          f"neu {z['neu']}, umgeschrieben {z['umgeschrieben']}, "
          f"entfallen 0")


def pflicht(rows, k, fehler, begr, anw=None, dar=None):
    """fehler/begr/anw/dar: Liste von 3 dicts (None = Zeile bleibt)."""
    for s, daten, m in ((1, fehler, M_FEHLER), (2, begr, M_BEGR)):
        alt = reihe(rows, k, s)
        neu = [setze(a, merkmal=m, **(d or {})) for a, d in zip(alt, daten)]
        rows = ersetze(rows, k, s, neu)
    for typ, daten in (("anwendung", anw), ("darstellung", dar)):
        if not daten:
            continue
        alt = [r for r in rows if r["kette_nr"] == k
               and r.get("pflicht") == typ]
        s = alt[0]["sprosse"]
        neu = []
        for a, d in zip(alt, daten):
            neu.append(setze(a, **d) if d else a)
        rows = ersetze(rows, k, s, neu)
    return rows


# ---------------------------------------------------------------- e1
def e1():
    rows = lade(1)
    v = reihe(rows, 1, 1)[0]
    m = ("ganzrationaler Term, Ergebnis als Punkt; f(x) = x³ − 4x² + 6 "
         "bleibt, die Stelle wandert")
    gf = []
    for i, s in enumerate([2, 3, 1, 4, 5], 1):
        w = s ** 3 - 4 * s ** 2 + 6
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=(f"Gegeben ist $f(x) = x^3 - 4x^2 + 6$. Berechne den "
                     f"Funktionswert an der Stelle ${s}$ und schreibe den "
                     f"Punkt auf."),
            antwort=f"f({s}) = __, P( __ | __ )",
            loesung=(f"einsetzen: $f({s}) = {s}^3 - 4 \\cdot {s}^2 + 6$; "
                     f"ausrechnen: $f({s}) = {s**3} - {4*s*s} + 6 = {w}$; "
                     f"Punkt schreiben: $P({s} | {w})$; "
                     f"Ergebnis: $f({s}) = {w}$, $P({s} | {w})$"),
            pruef=str(w)))
    rows = ersetze(rows, 1, 1, gf)
    rows = pflicht(rows, 3,
        fehler=[None,
            dict(aufgabe=("Zu $f(x) = -x^3 + 3x$ berechnet Mia "
                          "$f(-2) = 8 - 6 = 2$ und schreibt $P(-2 | 2)$. "
                          "Prüfe, ob Mia richtig gerechnet hat."),
                 loesung=("Richtig. Eine negative Zahl hoch drei bleibt "
                          "negativ, $(-2)^3 = -8$, das Minus davor macht "
                          "daraus $8$; mit $3 \\cdot (-2) = -6$ ergibt sich "
                          "$2$."),
                 pruef=""),
            dict(aufgabe=("Zu $f(x) = x^2 - 3x$ haben vier Schüler $f(-4)$ "
                          "angegeben: (1) $28$ (2) $4$ (3) $-28$ (4) $-4$. "
                          + SERIE),
                 loesung=("(2) nicht: allein $(-4)^2$ ist schon $16$, und "
                          "$-3 \\cdot (-4)$ ist positiv; (3) nicht und "
                          "(4) nicht: an einer negativen Stelle sind "
                          "$x^2$ und $-3x$ beide positiv, das Ergebnis "
                          "muss positiv sein."),
                 pruef="")],
        begr=[None,
            dict(aufgabe=(P4 + " (1) Der Schnittpunkt eines Graphen mit der "
                          "y-Achse ist immer $(0 | f(0))$. (2) Liegt "
                          "$P(1 | 5)$ auf dem Graphen von $f$, dann ist immer "
                          "auch $f(5) = 1$. (3) Jede ganzrationale Funktion "
                          "ohne Absolutglied geht durch den Ursprung."),
                 loesung=("(1) wahr, denn auf der y-Achse ist die Stelle "
                          "null; (2) falsch, z. B. $f(x) = 5x$: "
                          "$f(1) = 5$, aber $f(5) = 25$; (3) wahr, denn "
                          "jeder Summand enthält $x$, also ist $f(0) = 0$."),
                 pruef=""),
            dict(aufgabe=("Lena sagt: „Der Graph von $f(x) = 4 \\cdot e^x$ "
                          "schneidet die y-Achse bei $0$, weil $e$ hoch "
                          "null null ist.“ Begründe, ob Lena recht hat."),
                 loesung=("Nein; jede Zahl hoch null ist $1$, also "
                          "$e^0 = 1$ und $f(0) = 4 \\cdot 1 = 4$; der "
                          "Schnittpunkt ist $(0 | 4)$."),
                 pruef="")],
        anw=[
            dict(loesung=("Nein; Wert berechnen: $K(5) = 45 \\cdot 5 + 30 "
                          "= 255$ €; vergleichen: $255 > 250$, es fehlen "
                          "$5$ €")),
            dict(loesung=("Ja; Wert berechnen: $s(50) = \\frac{50^2}{100} "
                          "+ 0{,}3 \\cdot 50 = 25 + 15 = 40$ m; vergleichen: "
                          "$40 < 45$, es bleiben $5$ m Abstand")),
            dict(loesung=("Nein; Wert berechnen: $c(6) = 48 \\cdot e^{-3} "
                          "\\approx 2{,}39$ mg pro Liter; vergleichen: "
                          "$2{,}39 < 4$, der Wirkstoff wirkt nicht mehr"))])
    return nachziehen(rows, 1)


# ---------------------------------------------------------------- e2
def e2():
    rows = lade(2)
    v = reihe(rows, 1, 1)[0]
    m = ("Produkt zweier Linearfaktoren; der Faktor (x − 3) bleibt, die Zahl "
         "im zweiten Faktor wandert")
    gf = []
    for i, a in enumerate([5, -7, 1, -4, 8], 1):
        f2 = f"x + {a}" if a > 0 else f"x - {-a}"
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"Berechne die Nullstellen von $f(x) = (x - 3)({f2})$.",
            antwort="x1 = __, x2 = __",
            loesung=(f"Bedingung $f(x) = 0$: $(x - 3)({f2}) = 0$; ersten "
                     f"Faktor null setzen: $x - 3 = 0$, also $x_1 = 3$; "
                     f"zweiten Faktor null setzen: ${f2} = 0$, also "
                     f"$x_2 = {-a}$; Ergebnis: $x_1 = 3$, $x_2 = {-a}$"),
            pruef=f"[3, {-a}]"))
    rows = ersetze(rows, 1, 1, gf)
    # neue Sprosse 6 „rückwärts“; alte 6–9 rücken auf 7–10
    for r in rows:
        if r["kette_nr"] == 1 and r["sprosse"] >= 6:
            r["sprosse"] += 1
    muster = reihe(rows, 1, 5)[0]
    mr = ("rückwärts: die Nullstelle ist gegeben, ein Koeffizient gesucht; "
          "Kontrolle durch Faktorisieren")
    daten = [
        ("Bestimme die Zahl $a$ so, dass $2$ eine Nullstelle von "
         "$f(x) = x^2 + ax - 10$ ist.", "a = __",
         "Nullstelle einsetzen: $2^2 + 2a - 10 = 0$; nach $a$ auflösen: "
         "$2a = 6$, also $a = 3$; Kontrolle: $x^2 + 3x - 10 = (x - 2)(x + 5)$, "
         "der Faktor $(x - 2)$ liefert die Nullstelle $2$; Ergebnis: $a = 3$",
         "3"),
        ("Bestimme die Zahl $a$ so, dass $3$ eine Nullstelle von "
         "$f(x) = x^3 - 4x^2 + ax + 6$ ist.", "a = __",
         "Nullstelle einsetzen: $27 - 36 + 3a + 6 = 0$; nach $a$ auflösen: "
         "$3a = 3$, also $a = 1$; Kontrolle: $x^3 - 4x^2 + x + 6 = "
         "(x - 3)(x^2 - x - 2)$, der Faktor $(x - 3)$ liefert die Nullstelle "
         "$3$; Ergebnis: $a = 1$", "1"),
        ("Bestimme die Zahl $c$ so, dass $4$ eine Nullstelle von "
         "$f(x) = 2x^2 - 7x + c$ ist.", "c = __",
         "Nullstelle einsetzen: $2 \\cdot 16 - 7 \\cdot 4 + c = 0$; nach $c$ "
         "auflösen: $4 + c = 0$, also $c = -4$; Kontrolle: $2x^2 - 7x - 4 = "
         "(x - 4)(2x + 1)$, der Faktor $(x - 4)$ liefert die Nullstelle $4$; "
         "Ergebnis: $c = -4$", "-4"),
    ]
    neu6 = [setze(muster, _st="neu", sprosse=6, variante=i,
                  sprosse_text=T_E2_S6, merkmal=mr, aufgabe=a, form="teil",
                  antwort=an, loesung=l, pruef=p, original=None, grafik="",
                  loesungsgrafik="")
            for i, (a, an, l, p) in enumerate(daten, 1)]
    rows = nach(rows, 1, 5, neu6)
    # Prüfungshöhe (jetzt s10): 2023-A-2d mit zwei Zeilen dazu
    p = reihe(rows, 1, 10)
    o = {"id": "2023-A-2d", "jahr": 2023, "papier": "A"}
    pr = [
        ("Die Funktion $g(x) = x^2 - 9$ hat die Nullstellen $-3$ und $3$, "
         "die Funktion $h(x) = x + 3$ die Nullstelle $-3$. Begründe, dass "
         "$f(x) = g(x) \\cdot h(x) = x^3 + 3x^2 - 9x - 27$ genau dieselben "
         "Nullstellen wie $g$ hat und keine weiteren (FHR 2023).",
         "Nullprodukt anwenden: $f(x) = 0$ genau dann, wenn $g(x) = 0$ oder "
         "$h(x) = 0$; Nullstellen sammeln: $g$ liefert $-3$ und $3$, $h$ nur "
         "$-3$, die schon dabei ist; es kommt keine hinzu; Ergebnis: "
         "$x_1 = -3$, $x_2 = 3$", "[-3, 3]"),
        ("Die Funktion $g(x) = 2x^2 - 8$ hat die Nullstellen $-2$ und $2$, "
         "die Funktion $h(x) = x - 2$ die Nullstelle $2$. Begründe, dass "
         "$f(x) = g(x) \\cdot h(x) = 2x^3 - 4x^2 - 8x + 16$ genau dieselben "
         "Nullstellen wie $g$ hat und keine weiteren (FHR 2023).",
         "Nullprodukt anwenden: $f(x) = 0$ genau dann, wenn $g(x) = 0$ oder "
         "$h(x) = 0$; Nullstellen sammeln: $g$ liefert $-2$ und $2$, $h$ nur "
         "$2$, die schon dabei ist; es kommt keine hinzu; Ergebnis: "
         "$x_1 = -2$, $x_2 = 2$", "[-2, 2]"),
    ]
    neup = [setze(p[0], _st="neu", variante=len(p) + i, aufgabe=a,
                  form="text", antwort="", loesung=l, pruef=q, original=o,
                  grafik="", loesungsgrafik="")
            for i, (a, l, q) in enumerate(pr, 1)]
    rows = nach(rows, 1, 10, neup)
    rows = pflicht(rows, 3,
        fehler=[None,
            dict(aufgabe=("Zu $f(x) = x^4 - 5x^2 + 4$ rechnet Ben: "
                          "\\rechnung{x^4 - 5x^2 + 4 &= 0 && z = x^2 \\\\ "
                          "z^2 - 5z + 4 &= 0 \\\\ z_1 = 1, \\ z_2 &= 4 \\\\ "
                          "x &= \\pm 1 \\text{ oder } x = \\pm 2} "
                          "Prüfe, ob Ben richtig gerechnet hat."),
                 loesung=("Richtig. Beide Hilfslösungen sind positiv, und "
                          "nach der Rücksubstitution gehören zu jeder beide "
                          "Wurzeln mit $\\pm$."),
                 pruef=""),
            dict(aufgabe=("Zu $f(x) = (x + 3)(x - 1)(x - 6)$ haben vier "
                          "Schüler die Nullstellen angegeben: (1) $-3$, $1$, "
                          "$6$ (2) $3$, $-1$, $-6$ (3) $-3$, $1$ (4) $0$, "
                          "$-3$, $1$, $6$. " + SERIE),
                 loesung=("(2) nicht: die Zahlen der Faktoren mit ihrem "
                          "Vorzeichen übernommen, aus $x + 3$ folgt $-3$; "
                          "(3) nicht: jeder der drei Faktoren liefert eine "
                          "Nullstelle, es müssen drei sein; (4) nicht: es "
                          "gibt keinen Faktor $x$, also ist $0$ keine "
                          "Nullstelle."),
                 pruef="")],
        begr=[None,
            dict(aufgabe=(P4 + " (1) Für jede Zahl $a$ hat "
                          "$f(x) = (x - a) \\cdot e^x$ genau eine Nullstelle. "
                          "(2) Ein Produkt aus drei Linearfaktoren hat immer "
                          "drei verschiedene Nullstellen. (3) Eine "
                          "ganzrationale Funktion ohne Absolutglied hat nie "
                          "die Nullstelle null."),
                 loesung=("(1) wahr, denn $e^x$ ist nie null, nur "
                          "$x - a$ wird null, bei $x = a$; (2) falsch, z. B. "
                          "hat $(x - 1)(x - 1)(x + 2)$ nur die Nullstellen "
                          "$1$ und $-2$; (3) falsch, z. B. ist bei "
                          "$x^2 - 4x$ der Wert an der Stelle null $0$."),
                 pruef=""),
            dict(aufgabe=("Emma sagt: „$x^4 - 13x^2 + 36 = 0$ hat die "
                          "Lösungen $2$ und $3$, denn $z = x^2$ ergibt "
                          "$z = 4$ und $z = 9$.“ Begründe, ob Emma recht "
                          "hat."),
                 loesung=("Nein; nach der Rücksubstitution gehören zu jedem "
                          "positiven $z$ zwei Wurzeln, $x^2 = 4$ und "
                          "$x^2 = 9$ ergeben $-3$, $-2$, $2$ und $3$."),
                 pruef="")],
        anw=[None, None,
            dict(aufgabe=("Ein Pfeil wird von einem Turm abgeschossen: "
                          "$h(x) = -0{,}02x^2 + 0{,}6x + 8$ ($h$ Höhe in m, "
                          "$x$ waagerechte Entfernung vom Turm in m). Ein "
                          "Zielfeld liegt zwischen $35$ m und $45$ m vom Turm "
                          "entfernt. Landet der Pfeil im Zielfeld?"),
                 loesung=("Ja; Bedingung $h(x) = 0$: $-0{,}02x^2 + 0{,}6x "
                          "+ 8 = 0$; mit $-50$ malnehmen: $x^2 - 30x - 400 "
                          "= 0$; Lösungsformel: $x = 15 \\pm 25$, also "
                          "$x = 40$, die Lösung $-10$ entfällt; vergleichen: "
                          "$40$ m liegt zwischen $35$ m und $45$ m"),
                 pruef="40")])
    return nachziehen(rows, 2)


# ---------------------------------------------------------------- e3
def e3():
    rows = lade(3)
    v = reihe(rows, 1, 1)[0]
    m = ("lineares Argument des Logarithmus; die Zahl 6 bleibt, der Faktor "
         "vor x wandert")
    gf = []
    for i, (b, t) in enumerate([("2", "3"), ("3", "2"), ("", "6"),
                                 ("6", "1"), ("0{,}5", "12")], 1):
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=(f"Gib den größtmöglichen Definitionsbereich von "
                     f"$f(x) = \\mathrm{{ln}}({b}x - 6)$ an."),
            antwort="D = __",
            loesung=(f"Bedingung Argument größer null: ${b}x - 6 > 0$; nach "
                     f"$x$ auflösen: " + (f"${b}x > 6$, also " if b else "")
                     + f"$x > {t}$; Ergebnis: "
                     f"$D = ]{t}; \\infty[$, die Stelle $x = {t}$ gehört "
                     f"nicht dazu"),
            pruef=t.replace("{,}", ".")))
    rows = ersetze(rows, 1, 1, gf)
    rows = pflicht(rows, 2,
        fehler=[None,
            dict(aufgabe=("Zu $f(x) = \\mathrm{ln}(8 - 2x)$ rechnet Nora: "
                          "\\rechnung{8 - 2x &> 0 \\\\ -2x &> -8 \\\\ "
                          "x &< 4} und schreibt $D = ]-\\infty; 4[$. Prüfe, "
                          "ob Nora richtig gerechnet hat."),
                 loesung=("Richtig. Beim Teilen durch die negative Zahl $-2$ "
                          "dreht sich das Zeichen um, und die Stelle $4$ "
                          "gehört nicht dazu, weil dort das Argument null "
                          "ist."),
                 pruef=""),
            dict(aufgabe=("Für $f(x) = 3 + e^{-x}$ haben vier Schüler die "
                          "Wertemenge angegeben: (1) $]3; \\infty[$ "
                          "(2) $[3; \\infty[$ (3) $]-\\infty; 3[$ "
                          "(4) $]0; \\infty[$. " + SERIE),
                 loesung=("(2) nicht: der Wert $3$ wird nie angenommen, weil "
                          "$e^{-x}$ nie null ist; (3) nicht: $e^{-x}$ ist "
                          "positiv, zu $3$ kommt also etwas hinzu; (4) nicht: "
                          "die Werte von $e^{-x}$ sind um $3$ nach oben "
                          "verschoben, Werte bis $3$ kommen nicht vor."),
                 pruef="")],
        begr=[None,
            dict(aufgabe=(P4 + " (1) Der Graph von $f(x) = e^x$ schneidet "
                          "nie die x-Achse. (2) $\\mathrm{sin}(x) + 3$ liegt "
                          "immer zwischen $2$ und $4$. (3) Der "
                          "Definitionsbereich von $\\mathrm{ln}(x^2)$ "
                          "besteht nur aus positiven Zahlen."),
                 loesung=("(1) wahr, denn $e^x$ ist immer positiv, nie null; "
                          "(2) wahr, denn der Sinus liegt zwischen $-1$ und "
                          "$1$; (3) falsch, z. B. ist für $x = -1$ das "
                          "Argument $x^2 = 1$ positiv, $\\mathrm{ln}(1)$ "
                          "gibt es."),
                 pruef=""),
            dict(aufgabe=("Paul sagt: „$f(x) = 5 - e^x$ nimmt jeden Wert "
                          "unter $5$ an, aber nie die $5$ selbst.“ Begründe, "
                          "ob Paul recht hat."),
                 loesung=("Ja; $e^x$ nimmt jeden positiven Wert an, "
                          "$5 - e^x$ also jeden Wert unter $5$; die $5$ "
                          "nicht, weil $e^x$ nie null ist."),
                 pruef="")],
        anw=[None,
            dict(loesung=("Nein; umformen: $c(t) = 12 - 12e^{-0{,}3t}$; "
                          "Schranke: $12e^{-0{,}3t}$ ist stets positiv, also "
                          "bleibt $c(t)$ unter $12$ und damit unter "
                          "$12{,}5$ mg pro Liter")),
            None])
    return nachziehen(rows, 3)


# ---------------------------------------------------------------- e4
def e4():
    rows = lade(4)
    v = reihe(rows, 1, 1)[0]
    m = ("ganzrationaler Term; −6x² + 1 bleibt, der erste Summand wandert "
         "(gerader oder ungerader Exponent)")
    gf = []
    for i, (lead, ex, art) in enumerate([
            ("x^4", "4", "achsensymmetrisch zur y-Achse"),
            ("x^3", "3", "keine der beiden Symmetrien"),
            ("2x^6", "6", "achsensymmetrisch zur y-Achse"),
            ("x^5", "5", "keine der beiden Symmetrien"),
            ("3x^8", "8", "achsensymmetrisch zur y-Achse")], 1):
        pr = ("nur gerade Exponenten" if int(ex) % 2 == 0 else
              "gerade und ungerade Exponenten gemischt")
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=(f"Untersuche $f(x) = {lead} - 6x^2 + 1$ auf Symmetrie. "
                     f"Begründe am Term."),
            loesung=(f"Exponenten ablesen: ${ex}$, $2$ und $0$ beim "
                     f"Absolutglied; prüfen: {pr}; Ergebnis: {art}"),
            pruef=f"[{ex}, 2, 0]"))
    rows = ersetze(rows, 1, 1, gf)
    rows = pflicht(rows, 2,
        fehler=[None,
            dict(aufgabe=("Zu $f(x) = 2x^5 - x^3 + 3x$ rechnet Jan: "
                          "\\rechnung{f(-x) &= 2(-x)^5 - (-x)^3 + 3(-x) \\\\ "
                          "&= -2x^5 + x^3 - 3x \\\\ &= -f(x)} und schreibt: "
                          "punktsymmetrisch zum Ursprung. Prüfe, ob Jan "
                          "richtig gerechnet hat."),
                 loesung=("Richtig. Eine ungerade Potenz von $-x$ behält das "
                          "Minus, daher ist $f(-x) = -f(x)$ für alle $x$."),
                 pruef=""),
            dict(aufgabe=("Vier Schüler geben die Symmetrie von "
                          "$f(x) = x^6 - 4x^2 + 3$ an: (1) achsensymmetrisch "
                          "zur y-Achse (2) punktsymmetrisch zum Ursprung "
                          "(3) keine Symmetrie, weil das Absolutglied stört "
                          "(4) achsen- und punktsymmetrisch. " + SERIE),
                 loesung=("(2) nicht: es kommen nur gerade Exponenten vor, "
                          "keine ungeraden; (3) nicht: das Absolutglied "
                          "zählt als gerader Exponent; (4) nicht: dann müsste "
                          "der Graph durch den Ursprung gehen, er schneidet "
                          "die y-Achse aber bei $3$."),
                 pruef="")],
        begr=[None,
            dict(aufgabe=(P4 + " (1) Ein Graph mit nur ungeraden Exponenten "
                          "geht immer durch den Ursprung. (2) Ist der Graph "
                          "von $f$ achsensymmetrisch zur y-Achse und "
                          "$f(2) = 5$, dann ist immer auch $f(-2) = 5$. "
                          "(3) Die Summe zweier achsensymmetrischer "
                          "Funktionen ist nie achsensymmetrisch."),
                 loesung=("(1) wahr, denn ohne Absolutglied ist "
                          "$f(0) = 0$; (2) wahr, denn aus $f(-x) = f(x)$ "
                          "folgt $f(-2) = f(2)$; (3) falsch, z. B. sind "
                          "$x^2$ und $x^4$ achsensymmetrisch und ihre Summe "
                          "$x^4 + x^2$ auch."),
                 pruef=""),
            dict(aufgabe=("Clara sagt: „$f(x) = x^3 - 5x + 2$ ist "
                          "punktsymmetrisch zum Ursprung, weil nur ungerade "
                          "Exponenten vorkommen.“ Begründe, ob Clara recht "
                          "hat."),
                 loesung=("Nein; das Absolutglied $2$ zählt als gerader "
                          "Exponent, die Exponenten sind gemischt, keine der "
                          "beiden Symmetrien; der Graph geht nicht durch den "
                          "Ursprung."),
                 pruef="")])
    return nachziehen(rows, 4)


# ---------------------------------------------------------------- e5
def e5():
    rows = lade(5)
    # alte Vorstufe s0 wird s−1; neue Vorstufe s0 „im Argument ausklammern“
    for r in rows:
        if r["kette_nr"] == 1 and r["sprosse"] == 0:
            r["sprosse"] = -1
            r["sprosse_text"] = VOR[5]
    muster = reihe(rows, 1, -1)[0]
    m0 = ("Faktor im Argument ausklammern, die Verschiebung als Bruch c/b "
          "ablesen, nichts zeichnen")
    daten = [
        ("f(2x + 8)", "2x + 8 = 2 \\cdot (x + 4)", "\\frac{8}{2} = 4",
         "das Plus heißt nach links", "um $4$ nach links", "4"),
        ("f(3x - 6)", "3x - 6 = 3 \\cdot (x - 2)", "\\frac{6}{3} = 2",
         "das Minus heißt nach rechts", "um $2$ nach rechts", "2"),
        ("f(0{,}5x + 1)", "0{,}5x + 1 = 0{,}5 \\cdot (x + 2)",
         "\\frac{1}{0{,}5} = 2", "das Plus heißt nach links",
         "um $2$ nach links", "2"),
        ("f(4x - 2)", "4x - 2 = 4 \\cdot (x - 0{,}5)",
         "\\frac{2}{4} = 0{,}5", "das Minus heißt nach rechts",
         "um $0{,}5$ nach rechts", "0.5"),
    ]
    vor0 = []
    for i, (g, aus, br, ri, erg, p) in enumerate(daten, 1):
        vor0.append(setze(muster, _st="neu", sprosse=0, variante=i,
            sprosse_text=T_E5_S0, merkmal=m0,
            aufgabe=(f"Gegeben ist $g(x) = {g}$. Klammere im Argument den "
                     f"Faktor vor $x$ aus und gib an, um wie viel der Graph "
                     f"in x-Richtung verschoben ist, ohne zu zeichnen."),
            form="teil", antwort="um __ nach __",
            loesung=(f"ausklammern: ${aus}$; Verschiebung ablesen: ${br}$, "
                     f"{ri}; Ergebnis: {erg}"),
            pruef=p, original=None, grafik="", loesungsgrafik=""))
    rows = nach(rows, 1, -1, vor0)
    v = reihe(rows, 1, 1)[0]
    m = ("Änderung außen am Term; der Faktor 3 bleibt, der Summand wandert")
    gf = []
    for i, e in enumerate([2, -4, 5, -1, 6], 1):
        t = f"+ {e}" if e > 0 else f"- {-e}"
        ri = "oben" if e > 0 else "unten"
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=(f"Beschreibe, wie der Graph von "
                     f"$g(x) = 3 \\cdot f(x) {t}$ aus dem Graphen von $f$ "
                     f"entsteht."),
            loesung=(f"Faktor ablesen: $a = 3$, Streckung in y-Richtung mit "
                     f"dem Faktor $3$; Summand ablesen: $e = {e}$, "
                     f"Verschiebung um ${abs(e)}$ nach {ri}; Ergebnis: erst "
                     f"mit $3$ in y-Richtung strecken, dann um ${abs(e)}$ "
                     f"nach {ri} verschieben"),
            pruef=f"[3, {e}]"))
    rows = ersetze(rows, 1, 1, gf)
    anw_m = ("Anwendung: Periode deuten, Stelle stärkster Zunahme am Graphen "
             "ablesen, an einem Grenzwert entscheiden")
    rows = pflicht(rows, 2,
        fehler=[None,
            dict(aufgabe=("Der Graph von $f$ hat den Hochpunkt $H(2 | 5)$, "
                          "und es ist $g(x) = f(x - 4) - 3$. Kim rechnet: "
                          "\\rechnung{x &= 2 + 4 = 6 \\\\ y &= 5 - 3 = 2} "
                          "und schreibt den Hochpunkt von $g$ als "
                          "$(6 | 2)$. Prüfe, ob Kim richtig gerechnet hat."),
                 loesung=("Richtig. $f(x - 4)$ verschiebt um $4$ nach rechts, "
                          "$-3$ außen um $3$ nach unten; der Hochpunkt wandert "
                          "mit."),
                 pruef=""),
            dict(aufgabe=("Der Graph von $f$ hat die Wertemenge $[-2; 6]$. "
                          "Vier Schüler geben die Wertemenge von "
                          "$g(x) = -f(x + 5)$ an: (1) $[-6; 2]$ "
                          "(2) $[2; -6]$ (3) $[3; 11]$ (4) $[-2; 6]$. "
                          + SERIE),
                 loesung=("(2) nicht: vorn muss das kleinere Ende stehen, die "
                          "Enden sind nach der Spiegelung nicht getauscht; "
                          "(3) nicht: eine Verschiebung in x-Richtung ändert "
                          "die Werte nicht; (4) nicht: die Spiegelung an der "
                          "x-Achse dreht die Vorzeichen, $6$ ist kein Wert "
                          "mehr."),
                 pruef="")],
        begr=[None,
            dict(aufgabe=(P4 + " (1) Eine Verschiebung in x-Richtung ändert "
                          "nie die Wertemenge. (2) Eine Streckung in "
                          "y-Richtung mit dem Faktor $2$ verdoppelt immer "
                          "jede Nullstelle. (3) Spiegeln an der x-Achse und "
                          "Verschieben in y-Richtung darf man immer "
                          "vertauschen."),
                 loesung=("(1) wahr, denn jeder Wert wird nur an einer "
                          "anderen Stelle angenommen; (2) falsch, z. B. haben "
                          "$x - 1$ und $2x - 2$ beide die Nullstelle $1$; "
                          "(3) falsch, z. B. ist $-f(x) + 3$ nicht dasselbe "
                          "wie $-(f(x) + 3) = -f(x) - 3$."),
                 pruef=""),
            dict(aufgabe=("Leon sagt: „Bei $g(x) = f(x - 1) + 4$ ist es "
                          "egal, ob ich zuerst nach rechts oder zuerst nach "
                          "oben verschiebe.“ Begründe, ob Leon recht hat."),
                 loesung=("Ja; die Verschiebung in x-Richtung ändert nur das "
                          "Argument, die in y-Richtung nur den Wert; beide "
                          "Reihenfolgen ergeben $f(x - 1) + 4$."),
                 pruef="")],
        dar=[None, None,
            dict(aufgabe=("Beschreibe in Worten, ohne zu zeichnen, wie der "
                          "Graph von $g(x) = -e^x + 2$ aus dem Graphen von "
                          "$f(x) = e^x$ entsteht, und gib die Wertemenge "
                          "von $g$ an."),
                 form="text", antwort="",
                 loesung=("Spiegelung ablesen: das Minus vor $e^x$, "
                          "Spiegelung an der x-Achse; Summand ablesen: um "
                          "$2$ nach oben; Wertemenge: $e^x > 0$, also "
                          "$-e^x + 2 < 2$; Ergebnis: an der x-Achse "
                          "gespiegelt, dann um $2$ nach oben verschoben, "
                          "$W = ]-\\infty; 2[$"),
                 pruef="2", grafik="")],
        anw=[
            dict(merkmal=anw_m,
                 aufgabe=("Der Wasserstand in einem Hafen ist "
                          "$h(t) = 2 \\cdot \\mathrm{cos}\\left(\\frac{\\pi}"
                          "{6}t\\right) + 5$ ($h$ in m, $t$ in Stunden ab "
                          "Mitternacht). Deute die Periode und lies am "
                          "Graphen ab, wann das Wasser am stärksten steigt. "
                          "Ein Schiff braucht $3{,}5$ m Wassertiefe. Kann es "
                          "um 6 Uhr einlaufen?"),
                 loesung=("Nein; Periode berechnen: "
                          "$\\frac{2\\pi}{\\pi/6} = 12$, alle $12$ Stunden "
                          "steht das Wasser wieder gleich hoch; am Graphen "
                          "ablesen: am stärksten steigt es bei $t = 9$ und "
                          "$t = 21$, um 9 und 21 Uhr; Wert berechnen: "
                          "$h(6) = 2 \\cdot \\mathrm{cos}(\\pi) + 5 = 3$; "
                          "vergleichen: $3 < 3{,}5$, das Wasser ist zu "
                          "flach"),
                 pruef="[12, 9, 3]",
                 grafik=("\\begin{ksys}[xmin=0,xmax=24,ymin=0,ymax=8,xstep=2,"
                         "ystep=1,xlabel=t in h,ylabel=h in m,ablesen]"
                         "\\funktion{2*cos(30*\\x)+5}{h}\\end{ksys}")),
            dict(merkmal=anw_m,
                 aufgabe=("Ein Riesenrad: Die Höhe einer Gondel ist "
                          "$h(t) = -20 \\cdot \\mathrm{cos}\\left(\\frac{\\pi}"
                          "{10}t\\right) + 22$ ($h$ in m, $t$ in Minuten). "
                          "Deute die Periode und lies am Graphen ab, wann die "
                          "Gondel am stärksten steigt. Sieht man nach "
                          "$8$ Minuten über eine $40$ m hohe Mauer?"),
                 loesung=("Nein; Periode berechnen: "
                          "$\\frac{2\\pi}{\\pi/10} = 20$, eine Umdrehung "
                          "dauert $20$ Minuten; am Graphen ablesen: am "
                          "stärksten steigt die Gondel bei $t = 5$; Wert "
                          "berechnen: $h(8) = -20 \\cdot \\mathrm{cos}"
                          "(0{,}8\\pi) + 22 \\approx 38{,}18$; vergleichen: "
                          "$38{,}18 < 40$, die Gondel bleibt unter der "
                          "Mauerkante"),
                 pruef="[20, 5, -20*math.cos(0.8*math.pi)+22]",
                 grafik=("\\begin{ksys}[xmin=0,xmax=40,ymin=0,ymax=45,xstep=5,"
                         "ystep=5,xlabel=t in min,ylabel=h in m,ablesen]"
                         "\\funktion{-20*cos(18*\\x)+22}{h}\\end{ksys}")),
            dict(merkmal=anw_m,
                 aufgabe=("Die Körpertemperatur im Tagesverlauf ist "
                          "$T(t) = 0{,}4 \\cdot \\mathrm{cos}\\left(\\frac{\\pi}"
                          "{12}(t - 17)\\right) + 36{,}8$ ($T$ in °C, $t$ "
                          "Uhrzeit in Stunden). Deute die Periode und lies am "
                          "Graphen ab, wann die Temperatur am stärksten "
                          "steigt. Liegt die Temperatur um 5 Uhr unter "
                          "$36{,}5$ °C?"),
                 loesung=("Ja; Periode berechnen: "
                          "$\\frac{2\\pi}{\\pi/12} = 24$, der Verlauf "
                          "wiederholt sich jeden Tag; am Graphen ablesen: am "
                          "stärksten steigt sie bei $t = 11$, um 11 Uhr; "
                          "Wert berechnen: $T(5) = 0{,}4 \\cdot \\mathrm{cos}"
                          "(-\\pi) + 36{,}8 = 36{,}4$; vergleichen: "
                          "$36{,}4 < 36{,}5$"),
                 pruef="[24, 11, 36.4]",
                 grafik=("\\begin{ksys}[xmin=0,xmax=24,ymin=36,ymax=37.4,"
                         "xstep=2,ystep=0.2,xlabel=t in h,ylabel=T in °C,"
                         "ablesen]\\funktion{0.4*cos(15*(\\x-17))+36.8}{T}"
                         "\\end{ksys}"))])
    return nachziehen(rows, 5)


# ---------------------------------------------------------------- e6
def e6():
    rows = lade(6)
    v = reihe(rows, 1, 1)[0]
    m = ("Wertetabelle an den Stellen −2 bis 2; f(x) = x³ − a·x bleibt, der "
         "Koeffizient a wandert")
    gf = []
    for i, a in enumerate([1, 3, 5, 6, 7], 1):
        term = "x^3 - x" if a == 1 else f"x^3 - {a}x"
        ws = [x ** 3 - a * x for x in (-2, -1, 0, 1, 2)]
        teile = ", ".join(f"$f({x}) = {w}$"
                          for x, w in zip((-2, -1, 0, 1, 2), ws))
        pkt = ", ".join(f"$({x} | {w})$"
                        for x, w in zip((-2, -1, 0, 1, 2), ws))
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=(f"Fülle die Wertetabelle von $f(x) = {term}$ aus und "
                     f"übertrage die Punkte ins Koordinatensystem."),
            loesung=(f"Werte berechnen: {teile}; Punkte eintragen: {pkt}; "
                     f"Ergebnis: die fünf Punkte liegen im "
                     f"Koordinatensystem"),
            pruef=str(ws),
            grafik=("\\wertetabelle{x}{f(x)}{-2,-1,0,1,2}\\begin{ksys}"
                    "[xmin=-3,xmax=3,ymin=-7,ymax=7]\\end{ksys}")))
    rows = ersetze(rows, 1, 1, gf)
    rows = pflicht(rows, 2,
        fehler=[None,
            dict(aufgabe=("Für die Wertetabelle von $f(x) = -x^3 + 2x^2$ "
                          "rechnet Sophie: \\rechnung{f(-1) &= -(-1)^3 + 2 "
                          "\\cdot (-1)^2 = 1 + 2 = 3} Prüfe, ob Sophie "
                          "richtig gerechnet hat."),
                 loesung=("Richtig. $(-1)^3 = -1$, das Minus davor macht "
                          "daraus $1$; $(-1)^2 = 1$, also $1 + 2 = 3$."),
                 pruef=""),
            dict(aufgabe=("Für $f(x) = x^4 - 3x$ haben vier Schüler $f(-2)$ "
                          "in die Wertetabelle eingetragen: (1) $22$ (2) $10$ "
                          "(3) $-10$ (4) $-22$. " + SERIE),
                 loesung=("(2) nicht: allein $(-2)^4$ ist schon $16$, und "
                          "$-3 \\cdot (-2)$ ist positiv; (3) nicht und "
                          "(4) nicht: an einer negativen Stelle sind $x^4$ "
                          "und $-3x$ beide positiv."),
                 pruef="")],
        begr=[None,
            dict(aufgabe=(P4 + " (1) Eine ganzrationale Funktion dritten "
                          "Grades hat immer mindestens eine Nullstelle. "
                          "(2) Ein Graph mit zwei Nullstellen gehört immer "
                          "zu einer Funktion zweiten Grades. (3) Eine "
                          "ganzrationale Funktion vierten Grades hat nie "
                          "mehr als drei Extrempunkte."),
                 loesung=("(1) wahr, denn ganz links und ganz rechts haben "
                          "die Werte verschiedene Vorzeichen, dazwischen "
                          "kreuzt der Graph die x-Achse; (2) falsch, z. B. "
                          "hat $x^3 - x^2$ die Nullstellen $0$ und $1$ und "
                          "Grad drei; (3) wahr, denn die Ableitung hat Grad "
                          "drei und höchstens drei Nullstellen."),
                 pruef=""),
            dict(aufgabe=("Mila sagt: „Der Graph geht durch den Punkt "
                          "$(0 | 5)$, also gehört er zu $f(x) = x^2 + 5$.“ "
                          "Begründe, ob Mila recht hat."),
                 loesung=("Nein; ein einzelnes Merkmal genügt zum "
                          "Ausschließen, nicht zum Auswählen; auch "
                          "$g(x) = x^3 + 5$ geht durch $(0 | 5)$, weitere "
                          "Merkmale müssen passen."),
                 pruef="")],
        dar=[None,
            dict(aufgabe=("Beschreibe den Graphen von "
                          "$f(x) = -(x - 1)(x + 3)$ in Worten, ohne ihn zu "
                          "zeichnen: Öffnung, Nullstellen und Schnittpunkt "
                          "mit der y-Achse."),
                 form="text", antwort="",
                 loesung=("Öffnung ablesen: das Minus vor dem Produkt, nach "
                          "unten geöffnet; Nullstellen ablesen: $x = 1$ und "
                          "$x = -3$; Schnittpunkt berechnen: "
                          "$f(0) = -(-1) \\cdot 3 = 3$; Ergebnis: nach unten "
                          "geöffnete Parabel durch $(-3 | 0)$, $(1 | 0)$ und "
                          "$(0 | 3)$"),
                 pruef="[1, -3, 3]", grafik=""),
            None],
        anw=[None, None,
            dict(aufgabe=("Der Graph zeigt den Pegel $h$ eines Flusses in m "
                          "nach einem Starkregen, $t$ in Tagen. Der Deich "
                          "hält bis zu einem Pegel von $10{,}5$ m. Lies den "
                          "Hochpunkt ab, deute beide Koordinaten und "
                          "entscheide, ob der Deich hält."),
                 loesung=("Ja; Hochpunkt ablesen: $H(4 | 10)$; deuten: nach "
                          "$4$ Tagen erreicht der Pegel mit $10$ m seinen "
                          "höchsten Stand; vergleichen: $10 < 10{,}5$, der "
                          "Deich hält"))])
    return nachziehen(rows, 6)


if __name__ == "__main__":
    F = {"e1": (1, e1), "e2": (2, e2), "e3": (3, e3), "e4": (4, e4),
         "e5": (5, e5), "e6": (6, e6)}
    for a in sys.argv[1:]:
        n, f = F[a]
        rows = f()
        zaehle(n, rows)
        schreibe(n, rows)

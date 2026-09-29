"""Nachzug bank/extremalprobleme auf Katalog 2a296e5 (Mappe 29.09.).

Einmalig, 2026-09-29. Liest den Bestand (27./28.09.), zieht quelle
(79 -> 76, 81-83 -> 78-80), sprosse, id und sprosse_text nach,
schreibt die Grundfall-Päckchen (Schrittnamen in der Lösung), die
neuen Sprossen (e2 s2 Zerlegung ohne Figur, e3 s4 Randmaximum), die
Pflichtformen P1, P2, P4, P6, P8 und schreibt je Einheit die ganze
Datei neu. Zählt je Einheit übernommen/neu/umgeschrieben/entfallen.
Aufruf aus der Wurzel des Repos:
    python3 werkzeuge/einmalig/nachzug-extremalprobleme-2026-09-29.py
"""
import copy
import json
import sys
from pathlib import Path

B = Path("bank/extremalprobleme")
QMAP = {79: 76, 81: 78, 82: 79, 83: 80}
ZAEHL = {}

T_E1_S0 = ("„Wo sitzen die Ecken?“ – zu Figuren am Graphen ankreuzen, "
           "welche Ecken auf dem Graphen, auf den Achsen oder fest liegen "
           "und welche Seite welche Koordinate oder welcher Funktionswert "
           "ist; nichts rechnen")
T_E2_S0 = ("„Was wird extremal, was ist fest?“ – Hauptbedingung und "
           "Nebenbedingung im Text markieren und ankreuzen, wonach "
           "umgestellt wird; nichts rechnen")
T_E3_S0 = ("„Stelle, Seiten oder Inhalt?“ – ankreuzen, was verlangt ist "
           "(die Stelle, die Maße, der Extremwert) und ob Art und "
           "Randwerte zu prüfen sind; nichts rechnen")
T_E2_NEU = ("eine feste Nebenbedingung, wechselnde Zielfunktion ohne "
            "Figur: eine Zahl in zwei Summanden zerlegen, einmal das "
            "Produkt, einmal die Summe der Quadrate als Zielfunktion "
            "aufstellen und ausmultiplizieren")
T_E3_NEU = ("Randmaximum: die Zielfunktion hat im Innern nur ein Minimum; "
            "das gesuchte Maximum über die Randwerte des "
            "Definitionsbereichs bestimmen")

M_FEHLER = ("Rechnung prüfen: Fehler finden, richtige Rechnung erkennen, "
            "unmögliche Ergebnisse erkennen")
M_BEGR = ("begründen: Regel beim Namen, Aussagen beurteilen, "
          "Behauptung beurteilen")

FELDER = ["id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
          "sprosse_text", "merkmal", "hoehe", "pflicht", "variante",
          "aufgabe", "form", "antwort", "loesung", "pruef", "original",
          "grafik", "loesungsgrafik", "quelle"]
NACHGEZOGEN = ("id", "sprosse", "kette_nr", "quelle", "sprosse_text",
               "_neu")


def lade(n):
    return [json.loads(z) for z in
            (B / f"e{n}.jsonl").read_text(encoding="utf-8").splitlines()]


def nimm(zeilen, k, s):
    return [copy.deepcopy(a) for a in zeilen
            if a["kette_nr"] == k and a["sprosse"] == s]


def neu_zeile(vorlage, **kw):
    a = copy.deepcopy(vorlage)
    a.pop("pflicht", None) if kw.get("hoehe", a["hoehe"]) != "pflicht" \
        else None
    a["_neu"] = True
    a.update(kw)
    return a


def varianten(zeilen):
    for i, a in enumerate(zeilen, 1):
        a["variante"] = i
    return zeilen


def ordne(zeilen, einheit):
    aus = []
    for a in zeilen:
        a["quelle"] = QMAP.get(a["quelle"], a["quelle"])
        a["id"] = (f"extremalprobleme-e{einheit}-k{a['kette_nr']}"
                   f"-s{a['sprosse']}-v{a['variante']}")
        aus.append({f: a[f] for f in FELDER if f in a})
    return aus


def kern(a):
    return json.dumps({k: v for k, v in a.items() if k not in NACHGEZOGEN},
                      sort_keys=True, ensure_ascii=False)


def zaehle(n, alt, zeilen):
    bestand = {kern(a) for a in alt}
    ueb = sum(1 for a in zeilen if not a.get("_neu") and kern(a) in bestand)
    neu = sum(1 for a in zeilen if a.get("_neu") == "sprosse")
    um = len(zeilen) - ueb - neu
    ZAEHL[f"e{n}"] = dict(uebernommen=ueb, neu=neu, umgeschrieben=um,
                          entfallen=len(alt) - ueb - um)


def schreibe(n, alt, zeilen):
    zaehle(n, alt, zeilen)
    fertig = ordne(zeilen, n)
    text = "".join(json.dumps(a, ensure_ascii=False) + "\n" for a in fertig)
    (B / f"e{n}.jsonl").write_text(text, encoding="utf-8")


def setze(gruppe, v, **kw):
    a = gruppe[v - 1]
    a.update(kw)
    a["_neu"] = True
    return a


def kz(x):
    """Dezimalkomma für LaTeX."""
    s = f"{x:g}"
    return s.replace(".", "{,}")


# ---------------------------------------------------------------- e1
def e1():
    alt = lade(1)
    vor = nimm(alt, 1, 0)
    for a in vor:
        a["sprosse_text"] = T_E1_S0
    g = nimm(alt, 1, 1)[0]
    m = ("Breite ist die Stelle, Höhe der Funktionswert; f(x) = 16 − x² "
         "bleibt, die Stelle wandert")
    paeck = []
    for u in (1, 2, 3, 1.5, 2.5):
        fu = 16 - u * u
        U, F, Q = kz(u), kz(fu), kz(u * u)
        paeck.append(neu_zeile(
            g, merkmal=m,
            aufgabe=(f"Der Punkt $P({U} | f({U}))$ auf dem Graphen von "
                     "$f(x) = 16 - x^2$ ist eine Ecke eines Rechtecks; die "
                     "gegenüberliegende Ecke liegt im Ursprung, die Seiten "
                     "liegen auf den Achsen. Gib Breite und Höhe des "
                     "Rechtecks an."),
            loesung=(f"Breite ablesen: die Stelle ${U}$; Höhe berechnen: "
                     f"$f({U}) = 16 - {Q} = {F}$; Ergebnis: Breite ${U}$, "
                     f"Höhe ${F}$"),
            pruef=f"[{u}, {fu}]"))
    varianten(paeck)
    rest = [a for a in alt if a["kette_nr"] == 1 and a["sprosse"] >= 2]
    rest = copy.deepcopy(rest)

    fe = nimm(alt, 2, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    setze(fe, 2,
          aufgabe=("Ein Rechteck liegt symmetrisch zur y-Achse; zwei Ecken "
                   "liegen auf der x-Achse bei $-u$ und $u$, zwei auf dem "
                   "Graphen von $f(x) = 12 - x^2$. Mira rechnet: $A(u) = "
                   "2u \\cdot (12 - u^2) = 24u - 2u^3$. Prüfe, ob Mira "
                   "richtig gerechnet hat."),
          loesung=("Richtig. Die Breite ist $2u$, weil beide Hälften "
                   "zählen, und die Höhe ist der Funktionswert $f(u) = "
                   "12 - u^2$, nicht die Stelle."),
          pruef="")
    setze(fe, 3,
          aufgabe=("Für $f(x) = 8 - x^2$ hat das Dreieck mit den Ecken "
                   "$(0 | 0)$, $(u | 0)$ und $(u | f(u))$ für $0 < u < "
                   "\\sqrt{8}$ einen Flächeninhalt. Vier Schüler haben "
                   "Ergebnisse angegeben. Welche Ergebnisse können nicht "
                   "stimmen? Begründe, ohne genau zu rechnen. \\\\ (1) Für "
                   "$u = 1$ ist $A = 3{,}5$. \\\\ (2) Für $u = 2$ ist "
                   "$A = -4$. \\\\ (3) Für $u = 2{,}5$ ist $A = 12$. \\\\ "
                   "(4) Für $u = 3$ ist $A = 2$."),
          loesung=("Nicht stimmen können (2), (3) und (4). (2): Ein "
                   "Flächeninhalt ist nie negativ. (3): Die Höhe ist "
                   "höchstens $f(0) = 8$, das Dreieck ist also höchstens "
                   "halb so groß wie ein Rechteck mit $2{,}5$ mal $8$, "
                   "das sind $10$. (4): $u = 3$ liegt nicht im Bereich "
                   "$0 < u < \\sqrt{8}$, dort liegt die Ecke unter der "
                   "x-Achse und es gibt kein Dreieck."),
          pruef="")
    be = nimm(alt, 2, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    setze(be, 2,
          aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   "ist. Begründe. \\\\ (1) Liegt ein Rechteck mit einer "
                   "Seite auf der x-Achse und hat es die Ecke $(u | f(u))$ "
                   "auf dem Graphen, so ist seine Höhe immer $f(u)$. \\\\ "
                   "(2) Ein Trapez mit den parallelen Seiten $a$ und $c$ "
                   "ist immer $a - c$ hoch. \\\\ (3) Es gibt Dreiecke unter "
                   "einem Graphen, deren Höhe gleich der Stelle $u$ ist."),
          loesung=("(1) wahr, denn die Seite reicht senkrecht von der "
                   "x-Achse bis zum Graphenpunkt, also bis zur Höhe "
                   "$f(u)$. (2) falsch, z. B. hat ein Trapez mit $a = 7$, "
                   "$c = 5$ die Höhe $4$ – die Höhe hat mit der Differenz "
                   "der parallelen Seiten nichts zu tun. (3) wahr, denn "
                   "bei $f(x) = x$ ist der Funktionswert $f(u) = u$."),
          pruef="")
    setze(be, 3,
          aufgabe=("Tim sagt: „Das Rechteck mit den Ecken $(-u | 0)$, "
                   "$(u | 0)$, $(u | f(u))$ und $(-u | f(u))$ hat den "
                   "Flächeninhalt $u \\cdot f(u)$.“ Begründe, ohne genau zu "
                   "rechnen, ob Tim recht hat."),
          loesung=("Nein; das Rechteck reicht von $-u$ bis $u$ und ist "
                   "deshalb $2u$ breit – bei einer Figur symmetrisch zur "
                   "y-Achse zählen beide Hälften, der Flächeninhalt ist "
                   "$2u \\cdot f(u)$."),
          pruef="")
    for a in fe + be:
        if a.get("_neu"):
            a["_neu"] = "um"
    da = nimm(alt, 2, 3)
    zeilen = vor + paeck + rest + fe + be + da
    for a in paeck:
        a["_neu"] = "um"
    schreibe(1, alt, zeilen)


# ---------------------------------------------------------------- e2
def e2():
    alt = lade(2)
    vor = nimm(alt, 1, 0)
    for a in vor:
        a["sprosse_text"] = T_E2_S0
    g = nimm(alt, 1, 1)[0]
    m = ("Hauptbedingung mit zwei Variablen, Nebenbedingung nach b "
         "umstellen; Beet an einer Mauer mit drei Seiten Zaun bleibt, die "
         "Zaunlänge wandert")
    paeck = []
    for L in (28, 36, 44, 52, 64):
        paeck.append(neu_zeile(
            g, merkmal=m, _neu="um",
            aufgabe=("An einer Mauer wird ein rechteckiges Beet an den drei "
                     f"übrigen Seiten mit ${L}$ m Zaun eingefasst; $a$ steht "
                     "senkrecht zur Mauer, $b$ parallel. Die Fläche soll "
                     "möglichst groß werden. Notiere Haupt- und "
                     "Nebenbedingung und stelle die Nebenbedingung nach $b$ "
                     "um."),
            loesung=("Hauptbedingung: $A = a \\cdot b$; Nebenbedingung: "
                     f"$2a + b = {L}$; nach $b$ umstellen: $b = {L} - 2a$"),
            pruef=f"[{L}]"))
    varianten(paeck)

    neu = []
    for z, ctx in ((14, "Die Zahl $14$ wird in zwei Summanden $x$ und $y$ "
                        "zerlegt."),
                   (20, "Zwei Zahlen $x$ und $y$ haben die Summe $20$."),
                   (9, "Zerlege die Zahl $9$ in zwei Summanden $x$ und $y$.")):
        neu.append(neu_zeile(
            g, sprosse=2, sprosse_text=T_E2_NEU, hoehe="sprosse",
            _neu="sprosse",
            merkmal=("ohne Figur: feste Summe als Nebenbedingung, Produkt "
                     "und Summe der Quadrate als Zielfunktion"),
            aufgabe=(f"{ctx} Stelle einmal das Produkt $P$ und einmal die "
                     "Summe $S$ der Quadrate der beiden Summanden als "
                     "Funktion von $x$ auf und multipliziere aus."),
            form="text", antwort="",
            loesung=(f"Nebenbedingung: $x + y = {z}$, also $y = {z} - x$; "
                     f"Produkt einsetzen: $P(x) = x \\cdot ({z} - x) = "
                     f"{z}x - x^2$; Summe der Quadrate einsetzen: $S(x) = "
                     f"x^2 + ({z} - x)^2 = 2x^2 - {2*z}x + {z*z}$; "
                     f"Ergebnis: $P(x) = {z}x - x^2$ und $S(x) = 2x^2 - "
                     f"{2*z}x + {z*z}$"),
            pruef=f"[{z}, 2]", original=None, grafik="", loesungsgrafik=""))
    varianten(neu)
    rest = copy.deepcopy([a for a in alt
                          if a["kette_nr"] == 1 and a["sprosse"] >= 2])
    for a in rest:
        a["sprosse"] += 1

    fe = nimm(alt, 2, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    setze(fe, 2,
          aufgabe=("Ein rechteckiges Gehege an einer Stallwand wird an den "
                   "drei übrigen Seiten mit $42$ m Zaun eingefasst; $a$ "
                   "steht senkrecht zur Wand, $b$ parallel. Nele stellt "
                   "auf: $2a + b = 42$, also $b = 42 - 2a$ und $A(a) = a "
                   "\\cdot (42 - 2a) = 42a - 2a^2$ für $0 < a < 21$. Prüfe, "
                   "ob Nele richtig gerechnet hat."),
          loesung=("Richtig. An der Wand braucht man keinen Zaun, also "
                   "zählen zwei Seiten $a$ und eine Seite $b$; umgestellt "
                   "wird nach $b$, weil die Zielfunktion von $a$ abhängen "
                   "soll, und $b > 0$ verlangt $a < 21$."),
          pruef="")
    setze(fe, 3,
          aufgabe=("An einer Mauer stehen für die drei übrigen Seiten eines "
                   "rechteckigen Beets $32$ m Zaun zur Verfügung; $a$ steht "
                   "senkrecht zur Mauer. Vier Schüler haben die "
                   "Zielfunktion angegeben. Welche Ergebnisse können nicht "
                   "stimmen? Begründe, ohne genau zu rechnen. \\\\ (1) "
                   "$A(a) = 32a - 2a^2$ für $0 < a < 16$ \\\\ (2) $A(a) = "
                   "32a - 2a^2$ für $0 < a < 32$ \\\\ (3) $A(a) = 32a + "
                   "2a^2$ für $0 < a < 16$ \\\\ (4) $A = a \\cdot b$"),
          loesung=("Nicht stimmen können (2), (3) und (4). (2): Für $a > "
                   "16$ wäre die zweite Seite $32 - 2a$ negativ, der "
                   "Bereich ist zu groß. (3): Je länger $a$, desto kürzer "
                   "$b$ – vor $a^2$ muss ein Minus stehen. (4): Die "
                   "Nebenbedingung ist nicht eingesetzt; eine Zielfunktion "
                   "hat nur eine Variable."),
          pruef="")
    be = nimm(alt, 2, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    setze(be, 2,
          aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   "ist. Begründe. \\\\ (1) Die Hauptbedingung enthält "
                   "immer genau zwei Variablen. \\\\ (2) Es gibt Aufgaben, "
                   "bei denen die Nebenbedingung schon nach einer Variablen "
                   "umgestellt ist. \\\\ (3) Beschreibt die Variable eine "
                   "Seitenlänge, ist der Definitionsbereich der "
                   "Zielfunktion nie ganz $\\mathbb{R}$."),
          loesung=("(1) falsch, z. B. hat das Volumen eines Quaders "
                   "$V = a \\cdot b \\cdot c$ drei Variablen. (2) wahr, "
                   "denn liegt eine Ecke auf dem Graphen, gilt schon "
                   "$y = f(x)$. (3) wahr, denn eine Seitenlänge muss "
                   "positiv sein, negative Werte gehören nicht dazu."),
          pruef="")
    setze(be, 3,
          aufgabe=("Ali sagt: „Bei $A(a) = a \\cdot (36 - 2a)$ darf $a$ "
                   "jede positive Zahl sein, weil eine Seitenlänge nur "
                   "positiv sein muss.“ Begründe, ohne genau zu rechnen, ob "
                   "Ali recht hat."),
          loesung=("Nein; auch die zweite Seite $36 - 2a$ muss positiv "
                   "sein, der Definitionsbereich gehört zur Figur – also "
                   "$0 < a < 18$."),
          pruef="")
    an = nimm(alt, 2, 3)
    setze(an, 3,
          aufgabe=("Aus einem quadratischen Karton mit 30 cm Seitenlänge "
                   "wird eine offene Schachtel gefaltet: an den Ecken "
                   "werden Quadrate der Seitenlänge $x$ ausgeschnitten und "
                   "die Ränder hochgeklappt. Stelle das Volumen als "
                   "Funktion von $x$ auf. Reicht die Schachtel mit $x = 4$ "
                   "cm für $1{,}5$ Liter Saatgut?"),
          loesung=("Ja; Volumen aufstellen: $V(x) = x \\cdot (30 - 2x)^2 = "
                   "4x^3 - 120x^2 + 900x$ mit $0 < x < 15$; einsetzen: "
                   "$V(4) = 4 \\cdot 22^2 = 1\\,936$ cm³; vergleichen: "
                   "$1\\,936$ cm³ $> 1\\,500$ cm³, die Schachtel reicht."),
          pruef="[4, 1936]")
    for a in fe + be + an:
        if a.get("_neu"):
            a["_neu"] = "um"
    zeilen = vor + paeck + neu + rest + fe + be + an
    schreibe(2, alt, zeilen)


# ---------------------------------------------------------------- e3
def e3():
    alt = lade(3)
    vor = nimm(alt, 1, 0)
    for a in vor:
        a["sprosse_text"] = T_E3_S0
    g = nimm(alt, 1, 1)[0]
    m = ("Ableitung null setzen, Lösung im Definitionsbereich wählen; der "
         "Term kx − x³ bleibt, der Faktor k wandert")
    paeck = []
    for k in (12, 27, 3, 48, 108):
        x = int(round((k / 3) ** 0.5))
        paeck.append(neu_zeile(
            g, merkmal=m, _neu="um",
            aufgabe=(f"Die Zielfunktion $A(x) = {k}x - x^3$, $0 < x < "
                     f"\\sqrt{{{k}}}$, beschreibt einen Flächeninhalt. "
                     "Bestimme die Stelle mit $A'(x) = 0$ im "
                     "Definitionsbereich."),
            antwort="x = __",
            loesung=(f"Ableitung bilden: $A'(x) = {k} - 3x^2$; Bedingung "
                     f"$A'(x) = 0$: ${k} - 3x^2 = 0$, also $x^2 = {x*x}$; "
                     f"Lösungen: $x = {x}$ oder $x = -{x}$; im "
                     f"Definitionsbereich wählen: $x = -{x}$ entfällt; "
                     f"Ergebnis: $x = {x}$"),
            pruef=f"[{x}]"))
    varianten(paeck)
    s23 = copy.deepcopy([a for a in alt if a["kette_nr"] == 1
                         and a["sprosse"] in (2, 3)])
    MR = ("Zielfunktion mit innerem Minimum: das Maximum über die "
          "Randwerte des abgeschlossenen Bereichs")
    rand = []
    for aufg, loes, pr in (
            ("Ein Draht von $20$ cm Länge wird in zwei Stücke geteilt, "
             "das erste ist $x$ cm lang; aus jedem Stück wird ein Quadrat "
             "gebogen. Die Summe der Quadratflächen ist $A(x) = "
             "\\frac{x^2}{16} + \\frac{(20 - x)^2}{16}$ für $0 \\le x \\le "
             "20$; bei $x = 0$ oder $x = 20$ entsteht nur ein Quadrat. "
             "Bestimme, wie der Draht geteilt werden muss, damit die "
             "Summe möglichst groß wird, und gib sie an.",
             "Ableitung bilden: $A'(x) = \\frac{x}{8} - \\frac{20 - x}{8} = "
             "\\frac{x - 10}{4}$; Bedingung $A'(x) = 0$: $x = 10$; Art: "
             "$A''(x) = \\frac{1}{4} > 0$, also im Innern nur ein Minimum; "
             "Randwerte: $A(0) = 25$, $A(20) = 25$; Ergebnis: Die Summe ist "
             "mit $25$ cm² am größten, wenn der ganze Draht ein Quadrat "
             "bildet.", "[10, 25]"),
            ("Für $1 \\le x \\le 4$ beschreibt $A(x) = x^2 - 6x + 12$ den "
             "Flächeninhalt einer Figur. Bestimme den größten "
             "Flächeninhalt und die zugehörige Stelle.",
             "Ableitung bilden: $A'(x) = 2x - 6$; Bedingung $A'(x) = 0$: "
             "$x = 3$; Art: $A''(x) = 2 > 0$, also im Innern nur ein "
             "Minimum; Randwerte: $A(1) = 7$, $A(4) = 4$; Ergebnis: Der "
             "größte Flächeninhalt ist $7$, an der Stelle $x = 1$.",
             "[3, 7, 1]"),
            ("Für $0 \\le x \\le 3$ liegt der Graph von $f(x) = x^2 - 2x + "
             "6$ oberhalb des Graphen von $g(x) = 2x + 1$. Bestimme den "
             "größten vertikalen Abstand der Graphen in diesem Bereich.",
             "Differenzfunktion: $d(x) = f(x) - g(x) = x^2 - 4x + 5$; "
             "Ableitung bilden: $d'(x) = 2x - 4$; Bedingung $d'(x) = 0$: "
             "$x = 2$; Art: $d''(x) = 2 > 0$, also im Innern nur ein "
             "Minimum; Randwerte: $d(0) = 5$, $d(3) = 2$; Ergebnis: Der "
             "größte vertikale Abstand ist $5$, an der Stelle $x = 0$.",
             "[2, 5, 0]")):
        rand.append(neu_zeile(
            g, sprosse=4, sprosse_text=T_E3_NEU, hoehe="sprosse",
            _neu="sprosse", merkmal=MR, aufgabe=aufg, form="text",
            antwort="", loesung=loes, pruef=pr, original=None, grafik="",
            loesungsgrafik=""))
    varianten(rand)
    rest = copy.deepcopy([a for a in alt
                          if a["kette_nr"] == 1 and a["sprosse"] >= 4])
    for a in rest:
        a["sprosse"] += 1
    k2 = nimm(alt, 2, 1)

    fe = nimm(alt, 3, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    setze(fe, 2,
          aufgabe=("Gefragt ist der größte Flächeninhalt für $A(a) = 28a - "
                   "2a^2$, $0 < a < 14$. Lina rechnet: $A'(a) = 28 - 4a = "
                   "0$ liefert $a = 7$; $A''(a) = -4 < 0$, also Maximum; "
                   "der größte Flächeninhalt ist $A(7) = 196 - 98 = 98$. "
                   "Prüfe, ob Lina richtig gerechnet hat."),
          loesung=("Richtig. Gefragt ist der Extremwert, nicht die Stelle: "
                   "Lina bestätigt das Maximum mit $A''(7) < 0$ und setzt "
                   "$a = 7$ in die Zielfunktion ein."),
          pruef="")
    setze(fe, 3,
          aufgabe=("Für die Rechtecke unter dem Graphen von $f(x) = 6 - "
                   "x^2$ mit einer Ecke im Ursprung gilt $A(x) = x \\cdot "
                   "(6 - x^2)$, $0 < x < \\sqrt{6}$. Vier Schüler haben "
                   "Ergebnisse angegeben. Welche Ergebnisse können nicht "
                   "stimmen? Begründe, ohne genau zu rechnen. \\\\ (1) Die "
                   "Maximalstelle ist $x = 3$. \\\\ (2) Die Maximalstelle "
                   "ist $x = \\sqrt{2} \\approx 1{,}41$. \\\\ (3) Der größte "
                   "Flächeninhalt ist $-4$. \\\\ (4) Die Maximalstelle ist "
                   "$x = 0$."),
          loesung=("Nicht stimmen können (1), (3) und (4). (1): $x = 3$ "
                   "liegt außerhalb von $0 < x < \\sqrt{6}$. (3): Ein "
                   "Flächeninhalt ist nie negativ. (4): Bei $x = 0$ hat das "
                   "Rechteck die Breite null, und $x = 0$ gehört nicht zum "
                   "Bereich – dort liegt kein Maximum."),
          pruef="")
    be = nimm(alt, 3, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    setze(be, 2,
          aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   "ist. Begründe. \\\\ (1) Der vertikale Abstand zweier "
                   "Graphen an der Stelle $x$ ist immer die Differenz der "
                   "Funktionswerte, oberer minus unterer. \\\\ (2) Ist "
                   "$A'(x_0) = 0$, so hat $A$ bei $x_0$ immer ein Maximum. "
                   "\\\\ (3) Es gibt Zielfunktionen, deren größter Wert am "
                   "Rand des Definitionsbereichs liegt."),
          loesung=("(1) wahr, denn beide Punkte liegen an derselben Stelle "
                   "senkrecht übereinander. (2) falsch, z. B. hat $A(x) = "
                   "x^2$ bei $0$ die Ableitung null, dort aber ein Minimum. "
                   "(3) wahr, denn z. B. ist $A(x) = x$ auf $[0; 2]$ bei "
                   "$x = 2$ am größten, obwohl $A'$ nie null ist."),
          pruef="")
    setze(be, 3,
          aufgabe=("Emil sagt: „Die Zielfunktion $A(x) = x \\cdot (10 - x)$ "
                   "hat im Bereich $0 < x < 10$ ihren größten Wert bei "
                   "$x = 5$; Randwerte muss ich hier nicht vergleichen.“ "
                   "Begründe, ohne genau zu rechnen, ob Emil recht hat."),
          loesung=("Ja; der Bereich ist offen, die Ränder gehören nicht "
                   "dazu, und dort entartet die Figur zum Flächeninhalt "
                   "null – der Graph ist eine nach unten geöffnete Parabel "
                   "mit dem Scheitel in der Mitte bei $x = 5$."),
          pruef="")
    an = nimm(alt, 3, 3)
    setze(an, 1,
          aufgabe=("Aus einem quadratischen Karton mit 30 cm Seitenlänge "
                   "wird eine offene Schachtel gefaltet, indem an den Ecken "
                   "Quadrate der Seitenlänge $x$ ausgeschnitten werden; ihr "
                   "Volumen ist $V(x) = 4x^3 - 120x^2 + 900x$, $0 < x < "
                   "15$. Ein Kunde möchte aus diesem Karton eine Schachtel, "
                   "die $2{,}1$ Liter fasst. Ist das möglich?"),
          loesung=("Nein; Ableitung bilden: $V'(x) = 12x^2 - 240x + 900$; "
                   "Bedingung $V'(x) = 0$: $x = 5$ oder $x = 15$ (Rand, "
                   "keine Schachtel); Art: $V''(5) = -120 < 0$, also "
                   "Maximum; größtes Volumen: $V(5) = 2\\,000$ cm³, das ist "
                   "weniger als $2\\,100$ cm³."),
          pruef="[5, -120, 2000]")
    for a in fe + be + an:
        if a.get("_neu"):
            a["_neu"] = "um"
    zeilen = vor + paeck + s23 + rand + rest + k2 + fe + be + an
    schreibe(3, alt, zeilen)


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["1", "2", "3"]
    for n in wahl:
        {"1": e1, "2": e2, "3": e3}[n]()
    print(json.dumps(ZAEHL, ensure_ascii=False))

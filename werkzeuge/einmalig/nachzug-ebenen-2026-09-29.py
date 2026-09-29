"""Nachzug bank/ebenen auf die Mappe vom 29.09. (Katalog 2a296e5).

Einmalig. Liest den Bestand (27./28.09. samt Gegenlese), zieht
quelle, sprosse, id und sprosse_text nach (Katalogzeilen um drei
verschoben, Vorstufentexte länger), schreibt die neue Sprosse
e2 k2 s2 (Punkt der Ebene durch Nullsetzen), die Grundfall-Päckchen
(Sek II: fester Körper oder feste Ebene, ein Wert wandert) und die
Pflichtformen (P1, P2, P4, P6, P8); e2 k1 s8 wird hoehe pruefung.
Zählt je Einheit übernommen/neu/umgeschrieben/entfallen und schreibt
sie nach bank/ebenen/_tmp/nachzug-zahlen.json (vor dem Commit
löschen).

Aufruf: python3 werkzeuge/einmalig/nachzug-ebenen-2026-09-29.py [e1 e2 …]
"""
import copy
import json
import re
import sys
from pathlib import Path

W = Path(__file__).resolve().parents[2]
B = W / "bank" / "ebenen"
E = "ebenen"
# Kettenzeilen „Sprossen je Verfahrenstyp“: alt -> neu
QMAP = {117: 114, 118: 115, 119: 116, 120: 117, 121: 118}


def ketten_aus_mappe():
    """{zeile: [sprossentext, …]} der Zeilen 114–118 der Mappe."""
    aus = {}
    for z in (W / "mappen" / "ebenen.md").read_text(
            encoding="utf-8").split("\n"):
        m = re.match(r"\s*(\d+)  - [^:]+ \(Einheit \d\): (.*)$", z)
        if m and 114 <= int(m.group(1)) <= 118:
            aus[int(m.group(1))] = m.group(2).split(" → ")
    return aus


K = ketten_aus_mappe()

# Pflichtsprossen anwendung/darstellung: sprosse_text wortgleich aus
# dem Katalog (Typen je Lerneinheit, Lerneinheiten, Verortung).
PFLICHT_TEXT = {
    (1, "anwendung"): (23, "Parametergleichung einer Ebene aus Punkten "
                           "angeben"),
    (1, "darstellung"): (11, "Parameterform einer Ebene – die Ebene als "
                             "Punktmenge aus einem Stützvektor und zwei "
                             "nicht kollinearen Spannvektoren"),
    (2, "anwendung"): (24, "Koordinatengleichung einer Ebene aus Punkten "
                           "oder Geraden bestimmen"),
    (2, "darstellung"): (6, "Zusammenhang zwischen Parameter-, Normalen- "
                            "und Koordinatengleichung von Geraden in der "
                            "Ebene und von Ebenen im Raum"),
    (3, "anwendung"): (15, "Ebenen im Koordinatensystem – die "
                           "Koordinatenebenen und ihre Gleichungen, "
                           "achsenparallele Ebenen (fehlende Variable)"),
    (3, "darstellung"): (6, "Darstellung von Punktmengen, Geraden, "
                            "Ebenen, ebenen Figuren und Körpern in zwei- "
                            "bzw. dreidimensionalen kartesischen "
                            "Koordinatensystemen"),
    (4, "anwendung"): (26, "Koordinatengleichung einer parallelen Ebene "
                           "durch einen Punkt aufstellen"),
}


def T(*k):
    """Tripel wie im Bestand: (2 | -1 | 0), Dezimalkomma {,}."""
    def f(x):
        if isinstance(x, float) and x.is_integer():
            x = int(x)
        s = f"{x:g}" if isinstance(x, float) else str(x)
        return s.replace(".", "{,}")
    return "(" + " | ".join(f(x) for x in k) + ")"


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


def nachziehen(r, art="uebernommen", **kw):
    """Übernahme: nur id, sprosse, kette_nr, quelle, sprosse_text
    (und hoehe, wo bank.md sie neu fasst)."""
    r = copy.deepcopy(r)
    if r["hoehe"] != "pflicht" and r["quelle"] in QMAP:
        r["quelle"] = QMAP[r["quelle"]]
    if r["hoehe"] == "pflicht" and (r["einheit"], r["pflicht"]) in \
            PFLICHT_TEXT:
        r["quelle"], r["sprosse_text"] = PFLICHT_TEXT[
            (r["einheit"], r["pflicht"])]
    r.update(kw)
    r["_art"] = art
    r.setdefault("loesungsgrafik", "")
    r["id"] = rid(r)
    return r


def um(r, **kw):
    """Umgeschrieben: Aufgabe/Lösung neu, Struktur nachgezogen."""
    return nachziehen(r, art="umgeschrieben", **kw)


def kettentext(r, index=None):
    """sprosse_text der Kettenzeile aus der Mappe."""
    q = QMAP[r["quelle"]] if r["quelle"] in QMAP else r["quelle"]
    i = r["sprosse"] if index is None else index
    return K[q][i]


def kette(rows, k):
    return [r for r in rows if r["kette_nr"] == k]


def zeile(rows, k, s, v):
    return next(r for r in rows if r["kette_nr"] == k
                and r["sprosse"] == s and r["variante"] == v)


# ---------------------------------------------------------------- e1
# Quader mit fester Ecke A und festen Kanten (Körperregel, Päckchen:
# Stützpunkt A und Spannvektor AB bleiben, der zweite wandert).
Q_A = (1, 1, 1)
Q_KANTEN = {"B": (5, 0, 0), "D": (0, 3, 0), "E": (0, 0, 2)}
Q_TEXT = ("Ein Quader $ABCDEFGH$ hat die Ecke $A(1 | 1 | 1)$ und die "
          "Kantenvektoren $\\overrightarrow{AB} = (5 | 0 | 0)$, "
          "$\\overrightarrow{AD} = (0 | 3 | 0)$ und "
          "$\\overrightarrow{AE} = (0 | 0 | 2)$.")


def e1():
    rows = lade("e1")
    out = []
    for r in kette(rows, 1):
        if r["hoehe"] == "grundfall":
            continue
        out.append(nachziehen(r, sprosse_text=kettentext(r)))
        if r["hoehe"] == "vorstufe" and r["variante"] == 4:
            out += e1_grundfall(zeile(rows, 1, 1, 1))
    for r in kette(rows, 2):
        n = (r["sprosse"], r["variante"])
        if n == (1, 2):
            out.append(um(r, aufgabe=(
                "Mia prüft, ob $P(3 | 4 | 3)$ in $E\\colon \\vec x = "
                "(1 | 0 | 1) + r \\cdot (1 | 1 | 0) + s \\cdot (1 | 0 | 1)$, "
                "$r, s \\in \\mathbb{R}$, liegt: \\rechnung{\\text{I: } "
                "1 + r + s &= 3 \\\\ \\text{II: } r &= 4 \\\\ s &= -2 \\\\ "
                "\\text{III: } 1 + s &= -1 \\ne 3} Sie schreibt: „Also "
                "liegt $P$ nicht in $E$.“ Prüfe, ob Mia richtig gerechnet "
                "hat."),
                loesung=("Richtig. Die Parameter aus zwei Gleichungen müssen "
                         "auch die dritte Gleichung erfüllen; III ergibt "
                         "$-1$ statt 3, also liegt $P$ nicht in $E$."),
                pruef=""))
        elif n == (1, 3):
            out.append(um(r, aufgabe=(
                "Vier Schüler geben eine Parametergleichung der Ebene durch "
                "$A(1 | 2 | 1)$, $B(4 | 2 | 2)$ und $C(1 | 5 | 3)$ an: "
                "(1) $\\vec x = (1 | 2 | 1) + r \\cdot (3 | 0 | 1) + s "
                "\\cdot (0 | 3 | 2)$; (2) $\\vec x = (1 | 2 | 1) + r \\cdot "
                "(3 | 0 | 1) + s \\cdot (-6 | 0 | -2)$; (3) $\\vec x = "
                "(4 | 2 | 2) + r \\cdot (-3 | 0 | -1) + s \\cdot (-3 | 3 | 1)"
                "$; (4) $\\vec x = (1 | 2 | 1) + r \\cdot (4 | 2 | 2) + s "
                "\\cdot (1 | 5 | 3)$. Welche Ergebnisse können nicht "
                "stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(2) kann nicht stimmen – der zweite Spannvektor ist "
                         "das $(-2)$-Fache des ersten, beide sind parallel "
                         "und spannen keine Ebene auf; (4) kann nicht stimmen "
                         "– dort stehen die Ortsvektoren von $B$ und $C$ als "
                         "Spannvektoren statt der Verbindungsvektoren "
                         "$\\overrightarrow{AB}$ und $\\overrightarrow{AC}$."),
                pruef=""))
        elif n == (2, 2):
            out.append(um(r, aufgabe=(
                "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
                "Begründe. (1) Durch drei verschiedene Punkte geht immer "
                "genau eine Ebene. (2) Jede Ebene hat unendlich viele "
                "Parametergleichungen. (3) Die zwei Spannvektoren einer "
                "Ebene sind nie parallel."),
                loesung=("(1) falsch, z. B. liegen $(0 | 0 | 0)$, "
                         "$(1 | 1 | 1)$ und $(2 | 2 | 2)$ auf einer Geraden, "
                         "und durch eine Gerade gehen unendlich viele "
                         "Ebenen; (2) wahr, denn jeder Punkt der Ebene kann "
                         "Stützpunkt sein und jedes Vielfache eines "
                         "Spannvektors ist wieder Spannvektor; (3) wahr, "
                         "denn parallele Vektoren spannen nur eine Gerade "
                         "auf, keine Ebene."),
                pruef=""))
        elif n == (2, 3):
            out.append(um(r, aufgabe=(
                "Emil sagt: „Durch $A(1 | 0 | 1)$, $B(2 | 2 | 2)$ und "
                "$C(4 | 6 | 4)$ geht genau eine Ebene, es sind ja drei "
                "verschiedene Punkte.“ Begründe, ohne genau zu rechnen, ob "
                "Emil recht hat."),
                loesung=("Nein; von $A$ nach $C$ geht es dreimal so weit in "
                         "dieselbe Richtung wie von $A$ nach $B$ "
                         "($\\overrightarrow{AC} = 3 \\cdot "
                         "\\overrightarrow{AB}$), die drei Punkte liegen auf "
                         "einer Geraden – und durch eine Gerade gehen "
                         "unendlich viele Ebenen."),
                pruef=""))
        elif n == (3, 1):
            out.append(um(r, aufgabe=(
                "Eine rechteckige Solarplatte hat die Ecken $A(0 | 0 | 3)$, "
                "$B(2 | 0 | 3)$, $C(2 | 1{,}5 | 5)$ und $D(0 | 1{,}5 | 5)$ "
                "(1 LE = 1 m). Ein Sensor soll bei $S(1{,}8 | 1{,}2 | 4{,}6)$ "
                "auf der Platte sitzen, nicht nur in ihrer Ebene. Sitzt er "
                "auf der Platte?"),
                loesung=("Ja; Ebene aufstellen: $\\vec x = (0 | 0 | 3) + r "
                         "\\cdot (2 | 0 | 0) + s \\cdot (0 | 1{,}5 | 2)$; "
                         "Parameter aus I: $2r = 1{,}8$, also $r = 0{,}9$; "
                         "Parameter aus II: $1{,}5s = 1{,}2$, also "
                         "$s = 0{,}8$; Probe mit III: $3 + 2 \\cdot 0{,}8 = "
                         "4{,}6$ ✓; Grenzen prüfen: $r = 0{,}9$ und "
                         "$s = 0{,}8$ liegen zwischen 0 und 1, der Sensor "
                         "sitzt auf der Platte."),
                pruef="[0.9, 0.8]"))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


def e1_grundfall(v0):
    st = kettentext(v0)
    aus = []
    wandert = [("D", (0, 3, 0)), ("E", (0, 0, 2)), ("H", (0, 3, 2)),
               ("C", (5, 3, 0)), ("G", (5, 3, 2))]
    u = Q_KANTEN["B"]
    for v, (p, w) in enumerate(wandert, 1):
        aus.append(um(v0, variante=v, sprosse_text=st,
            merkmal=("fester Quader: Stützpunkt A und Spannvektor AB "
                     "bleiben, der zweite Spannvektor wandert; nur "
                     "einsetzen"),
            aufgabe=(Q_TEXT + f" Gib eine Parametergleichung der Ebene "
                     f"mit dem Stützpunkt $A$ und den Spannvektoren "
                     f"$\\overrightarrow{{AB}} = {T(*u)}$ und "
                     f"$\\overrightarrow{{A{p}}} = {T(*w)}$ an."),
            form="teil", antwort="",
            loesung=(f"Stützvektor: ${T(*Q_A)}$; Spannvektoren: ${T(*u)}$ "
                     f"und ${T(*w)}$; Ergebnis: $E\\colon \\vec x = "
                     f"{T(*Q_A)} + r \\cdot {T(*u)} + s \\cdot {T(*w)}$, "
                     f"$r, s \\in \\mathbb{{R}}$"),
            pruef=json.dumps(list(Q_A) + list(u) + list(w)),
            grafik="", loesungsgrafik="", original=None))
    return aus


# ---------------------------------------------------------------- e2
# Pyramide mit festen Ecken (Kette k1): AS bleibt, der zweite
# Spannvektor wandert. Kette k2: feste Ebene 2x − 3y + 6z = 12, die
# vorgegebene Komponente wandert.
P_TEXT = ("Die Pyramide $ABCDS$ hat die Grundfläche $A(1 | 1 | 0)$, "
          "$B(7 | 1 | 0)$, $C(7 | 10 | 0)$, $D(1 | 10 | 0)$ und die Spitze "
          "$S(3 | 3 | 2)$.")


def e2():
    rows = lade("e2")
    out = []
    for r in kette(rows, 1):
        if r["hoehe"] == "grundfall":
            continue
        kw = {"sprosse_text": kettentext(r)}
        if r["sprosse"] == 8:
            kw["hoehe"] = "pruefung"
        out.append(nachziehen(r, **kw))
        if r["hoehe"] == "vorstufe" and r["variante"] == 4:
            out += e2_grundfall_k1(zeile(rows, 1, 1, 1))
    for r in kette(rows, 2):
        if r["hoehe"] == "grundfall":
            continue
        s = r["sprosse"] + (1 if r["sprosse"] >= 2 else 0)
        out.append(nachziehen(r, sprosse=s,
                              sprosse_text=kettentext(r, s)))
        if r["hoehe"] == "vorstufe" and r["variante"] == 4:
            g = zeile(rows, 2, 1, 1)
            out += e2_grundfall_k2(g)
            out += e2_nullsetzen(g)
    for r in kette(rows, 3):
        n = (r["sprosse"], r["variante"])
        if n == (1, 1):
            out.append(um(r, aufgabe=(
                "Die Ebene $E$ geht durch $A(1 | 2 | 3)$, $B(3 | 2 | 1)$ "
                "und $C(1 | 4 | 1)$. Vier Schüler geben eine "
                "Koordinatengleichung von $E$ an: (1) $x + y + z = 6$; "
                "(2) $3x + 3y + 3z = 18$; (3) $x + 2y + 2z = 11$; "
                "(4) $x + y + z = 0$. Welche Ergebnisse können nicht "
                "stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(3) kann nicht stimmen – $A$ und $B$ unterscheiden "
                         "sich nur in $x$ und $z$, um $+2$ und $-2$; das "
                         "gleicht sich nur aus, wenn vor $x$ und $z$ "
                         "dieselbe Zahl steht; (4) kann nicht stimmen – "
                         "rechts 0 hieße, der Ursprung liegt in $E$, aber "
                         "$A$ ergibt links $1 + 2 + 3 = 6$."),
                pruef=""))
        elif n == (1, 2):
            out.append(um(r, aufgabe=(
                "Tom eliminiert die Parameter aus $\\vec x = (1 | 3 | 0) + "
                "r \\cdot (1 | 0 | 1) + s \\cdot (0 | 1 | 1)$: "
                "\\rechnung{r &= x - 1 \\\\ s &= y - 3 \\\\ z &= (x - 1) + "
                "(y - 3) \\\\ x + y - z &= 4} Prüfe, ob Tom richtig "
                "gerechnet hat."),
                loesung=("Richtig. Aus der ersten und der zweiten Zeile "
                         "folgen $r$ und $s$; eingesetzt in die dritte Zeile "
                         "$z = r + s$ ergibt sich $x + y - z = 4$."),
                pruef=""))
        elif n == (2, 2):
            out.append(um(r, aufgabe=(
                "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
                "Begründe. (1) Jede Ebene hat genau einen Normalenvektor. "
                "(2) Ist $\\vec n$ ein Normalenvektor von $E$, dann ist "
                "auch $-\\vec n$ einer. (3) In einer Koordinatengleichung "
                "$ax + by + cz = d$ ist $(a | b | c)$ immer ein "
                "Normalenvektor der Ebene."),
                loesung=("(1) falsch, z. B. sind $(1 | 2 | 2)$ und "
                         "$(2 | 4 | 4)$ beide Normalenvektoren von "
                         "$x + 2y + 2z = 5$; (2) wahr, denn $-\\vec n$ steht "
                         "ebenso senkrecht auf beiden Spannvektoren, die "
                         "Skalarprodukte bleiben 0; (3) wahr, denn die "
                         "ausmultiplizierte Normalenform heißt "
                         "$\\vec n \\cdot \\vec x = d$, die Zahlen vor $x$, "
                         "$y$, $z$ sind die Komponenten von $\\vec n$."),
                pruef=""))
        elif n == (2, 3):
            out.append(um(r, aufgabe=(
                "Lukas sagt: „Multipliziert man die Normalenform "
                "$(\\vec x - \\vec p) \\cdot \\vec n = 0$ aus, steht rechts "
                "immer 0.“ Begründe, ohne genau zu rechnen, ob Lukas recht "
                "hat."),
                loesung=("Nein; ausmultipliziert heißt die Gleichung "
                         "$\\vec n \\cdot \\vec x = \\vec n \\cdot \\vec p$, "
                         "rechts steht die Zahl $\\vec n \\cdot \\vec p$ – "
                         "sie ist nur 0, wenn der Ursprung in der Ebene "
                         "liegt."),
                pruef=""))
        elif n == (3, 3):
            out.append(um(r, aufgabe=(
                "Eine Dachfläche geht durch $P(2 | 0 | 5)$, $Q(2 | 6 | 5)$ "
                "und $R(6 | 0 | 3)$ (1 LE = 1 m, $z$ zeigt nach oben). Eine "
                "Antenne endet im Punkt $T(4 | 3 | 4{,}5)$ über dem Dach. "
                "Sie muss senkrecht mindestens 0,4 m über die Dachfläche "
                "hinausragen. Reicht das?"),
                loesung=("Ja; Normalenvektor: $(1 | 0 | 2)$ steht senkrecht "
                         "auf $\\overrightarrow{PQ} = (0 | 6 | 0)$ und "
                         "$\\overrightarrow{PR} = (4 | 0 | -2)$; Konstante "
                         "mit $P$: $d = 2 + 2 \\cdot 5 = 12$, also "
                         "$E\\colon x + 2z = 12$; Dachhöhe unter $T$: "
                         "$4 + 2z = 12$, also $z = 4$; Überstand: "
                         "$4{,}5 - 4 = 0{,}5$ m, und $0{,}5 > 0{,}4$."),
                pruef="[12, 4, 0.5]"))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


def e2_grundfall_k1(g):
    st = kettentext(g)
    aus = []
    a, s_ = (1, 1, 0), (3, 3, 2)
    u = tuple(y - x for x, y in zip(a, s_))
    wandert = [("die Kante $AB$", "AB", (6, 0, 0), (0, 1, -1), "n_2"),
               ("die Kante $AD$", "AD", (0, 9, 0), (-1, 0, 1), "n_1"),
               ("die Diagonale $AC$", "AC", (6, 9, 0), (-3, 2, 1), "n_3"),
               ("den Punkt $M(7 | 7 | 0)$ auf der Kante $BC$", "AM",
                (6, 6, 0), (-1, 1, 0), "n_2"),
               ("den Punkt $N(4 | 10 | 0)$ auf der Kante $CD$", "AN",
                (3, 9, 0), (-3, 1, 2), "n_2")]
    for v, (wo, nm, w, n, frei) in enumerate(wandert, 1):
        n1, n2, n3 = n
        wahl = {"n_1": n1, "n_2": n2, "n_3": n3}[frei]
        g1 = f"2n_1 + 2n_2 + 2n_3 = 0"
        w1, w2, _ = w
        teile = [f"{w1}n_1" if w1 else "", f"{w2}n_2" if w2 else ""]
        g2 = " + ".join(t for t in teile if t) + " = 0"
        aus.append(um(g, variante=v, sprosse_text=st,
            merkmal=("feste Pyramide: Spannvektor AS bleibt, der zweite "
                     "Spannvektor wandert; zwei Skalarprodukte null, eine "
                     "Komponente frei wählen"),
            aufgabe=(P_TEXT + f" Die Ebene durch $A$, $S$ und {wo} hat die "
                     f"Spannvektoren $\\overrightarrow{{AS}} = {T(*u)}$ und "
                     f"$\\overrightarrow{{{nm}}} = {T(*w)}$. Bestimme einen "
                     f"Normalenvektor $\\vec n$ dieser Ebene."),
            form="teil", antwort="$\\vec n = ($__ | __ | __$)$",
            loesung=(f"Skalarprodukt mit $\\overrightarrow{{AS}}$: ${g1}$; "
                     f"Skalarprodukt mit $\\overrightarrow{{{nm}}}$: "
                     f"${g2}$; Komponente wählen: ${frei} = {wahl}$; "
                     f"ausrechnen: $n_1 = {n1}$, $n_2 = {n2}$, $n_3 = {n3}$; "
                     f"Ergebnis: $\\vec n = {T(*n)}$ (jedes Vielfache "
                     f"ebenso)"),
            pruef=json.dumps(list(n)), grafik="", loesungsgrafik="",
            original=None))
    return aus


def e2_grundfall_k2(g):
    st = kettentext(g)
    aus = []
    n0 = (2, -3, 6)
    faelle = [("erste", 2, 1), ("erste", 4, 2), ("zweite", 3, -1),
              ("dritte", 3, 0.5), ("erste", 6, 3)]
    for v, (welche, wert, f) in enumerate(faelle, 1):
        n = tuple(x * f for x in n0)
        fs = str(f).replace(".", "{,}")
        if f == 1:
            weg = f"ablesen: ${T(*n0)}$; Ergebnis: $\\vec n = {T(*n)}$"
        else:
            idx = {"erste": 0, "zweite": 1, "dritte": 2}[welche]
            weg = (f"ablesen: ${T(*n0)}$; Faktor: $\\frac{{{wert}}}"
                   f"{{{n0[idx]}}} = {fs}$; Vielfaches: ${fs} \\cdot "
                   f"{T(*n0)} = {T(*n)}$; Ergebnis: $\\vec n = {T(*n)}$")
        aus.append(um(g, variante=v, sprosse_text=st,
            merkmal=("feste Ebene $2x - 3y + 6z = 12$: die vorgegebene "
                     "Komponente wandert; Koeffizienten ablesen, Vielfache "
                     "gleichwertig"),
            aufgabe=(f"Gegeben ist $E\\colon 2x - 3y + 6z = 12$. Gib den "
                     f"Normalenvektor von $E$ an, dessen {welche} "
                     f"Komponente {wert} ist."),
            form="teil", antwort="$\\vec n = ($__ | __ | __$)$",
            loesung=weg, pruef=json.dumps(list(n)), grafik="",
            loesungsgrafik="", original=None))
    return aus


def e2_nullsetzen(g):
    st = kettentext(g, 2)
    aus = []
    faelle = [("2x - 3y + 6z = 12", ("x", "y"), "6z = 12", "z = 2",
               (0, 0, 2), "2 \\cdot 0 - 3 \\cdot 0 + 6 \\cdot 2 = 12"),
              ("3x + 5y - z = 15", ("x", "z"), "5y = 15", "y = 3",
               (0, 3, 0), "3 \\cdot 0 + 5 \\cdot 3 - 0 = 15"),
              ("4x + y - 2z = 20", ("y", "z"), "4x = 20", "x = 5",
               (5, 0, 0), "4 \\cdot 5 + 0 - 2 \\cdot 0 = 20")]
    for v, (gl, (a, b), rest, wert, p, probe) in enumerate(faelle, 1):
        r = copy.deepcopy(g)
        r.update(sprosse=2, variante=v, sprosse_text=st, hoehe="sprosse",
                 quelle=116,
                 merkmal=("einen Punkt der Ebene selbst erzeugen: zwei "
                          "Koordinaten null setzen, die dritte ausrechnen, "
                          "Probe durch Einsetzen"),
                 aufgabe=(f"Gegeben ist $E\\colon {gl}$. Bestimme einen "
                          f"Punkt $P$ von $E$, indem du ${a}$ und ${b}$ null "
                          f"setzt, und mache die Probe."),
                 form="teil", antwort="$P($__ | __ | __$)$",
                 loesung=(f"null setzen: ${a} = 0$, ${b} = 0$; dritte "
                          f"Koordinate ausrechnen: ${rest}$, also ${wert}$; "
                          f"Probe: ${probe}$ ✓; Ergebnis: $P{T(*p)}$"),
                 pruef=json.dumps(list(p)), grafik="", loesungsgrafik="",
                 original=None)
        r["_art"] = "neu"
        r["id"] = rid(r)
        aus.append(r)
    return aus


# ---------------------------------------------------------------- e3
# Quader mit festen Ecken; die Fläche wandert.
Q3 = ("Ein Quader hat die Ecken $O(0 | 0 | 0)$, $A(6 | 0 | 0)$, "
      "$B(6 | 7 | 0)$, $C(0 | 7 | 0)$, $P(0 | 0 | 3)$, $Q(6 | 0 | 3)$, "
      "$R(6 | 7 | 3)$ und $S(0 | 7 | 3)$.")


def e3():
    rows = lade("e3")
    out = []
    for r in kette(rows, 1):
        if r["hoehe"] == "grundfall":
            continue
        out.append(nachziehen(r, sprosse_text=kettentext(r)))
        if r["hoehe"] == "vorstufe" and r["variante"] == 4:
            out += e3_grundfall(zeile(rows, 1, 1, 1))
    for r in kette(rows, 2):
        n = (r["sprosse"], r["variante"])
        if n == (1, 1):
            out.append(um(r, aufgabe=(
                "Vier Schüler beschreiben die Lage von Ebenen: "
                "(1) $2x + 5y = 10$ ist parallel zur $z$-Achse; "
                "(2) $7x - 6y = 0$ enthält die $z$-Achse; "
                "(3) $3y - 7z = 21$ enthält die $x$-Achse; "
                "(4) $z = 4$ ist die $xy$-Ebene. Welche Ergebnisse können "
                "nicht stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(3) kann nicht stimmen – rechts steht nicht 0, "
                         "der Ursprung liegt nicht in der Ebene, sie ist "
                         "nur parallel zur $x$-Achse; (4) kann nicht "
                         "stimmen – die $xy$-Ebene ist $z = 0$, $z = 4$ "
                         "liegt parallel zu ihr, vier Einheiten darüber."),
                pruef=""))
        elif n == (1, 2):
            out.append(um(r, aufgabe=(
                "Max schreibt: „$E\\colon x = 5$ ist parallel zur "
                "$yz$-Ebene, aber nicht die $yz$-Ebene selbst, denn die "
                "hat die Gleichung $x = 0$.“ Prüfe, ob Max richtig "
                "überlegt hat."),
                loesung=("Richtig. Fehlen $y$ und $z$ in der Gleichung, ist "
                         "die Ebene parallel zur $yz$-Ebene; nur $x = 0$ ist "
                         "die $yz$-Ebene selbst."),
                pruef=""))
        elif n == (2, 2):
            out.append(um(r, aufgabe=(
                "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
                "Begründe. (1) Fehlt in einer Koordinatengleichung eine "
                "Variable, dann enthält die Ebene immer die zugehörige "
                "Achse. (2) Jede Ebene, deren Gleichung rechts 0 hat, geht "
                "durch den Ursprung. (3) Eine Ebene, die senkrecht auf der "
                "$xy$-Ebene steht, hat nie einen Normalenvektor mit einer "
                "dritten Komponente ungleich 0."),
                loesung=("(1) falsch, z. B. fehlt in $x + z = 4$ das $y$, "
                         "aber der Ursprung erfüllt die Gleichung nicht – "
                         "die Ebene ist nur parallel zur $y$-Achse; (2) "
                         "wahr, denn der Ursprung ergibt links immer 0; "
                         "(3) wahr, denn ihr Normalenvektor liegt waagerecht "
                         "in der $xy$-Ebene, seine dritte Komponente ist 0."),
                pruef=""))
        elif n == (2, 3):
            out.append(um(r, aufgabe=(
                "Pia sagt: „Die Ebene $4x - 5y = 20$ enthält die $z$-Achse, "
                "weil $z$ in der Gleichung fehlt.“ Begründe, ohne genau zu "
                "rechnen, ob Pia recht hat."),
                loesung=("Nein; weil $z$ fehlt, ist die Ebene nur parallel "
                         "zur $z$-Achse – der Ursprung erfüllt die Gleichung "
                         "nicht ($0 \\ne 20$), also enthält sie die "
                         "$z$-Achse nicht."),
                pruef=""))
        elif n == (3, 2):
            out.append(um(r, aufgabe=(
                "Ein Fußball fliegt auf der Bahn $X_t(4 + 14t | 8 | -5t^2 + "
                "9t)$; $X_t$ ist sein Ort nach $t$ Sekunden (1 LE = 1 m). "
                "Die Torebene ist $x = 25$, die Latte hängt in 2,44 m Höhe. "
                "Geht der Ball unter der Latte durch?"),
                loesung=("Ja; Torebene erreichen: $4 + 14t = 25$, also "
                         "$t = 1{,}5$; Höhe dort: $-5 \\cdot 1{,}5^2 + 9 "
                         "\\cdot 1{,}5 = 2{,}25$; Vergleich: $2{,}25 < "
                         "2{,}44$ – der Ball fliegt in der Ebene $y = 8$ "
                         "unter der Latte durch."),
                pruef="[1.5, 2.25]"))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


def e3_grundfall(g):
    st = kettentext(g)
    aus = []
    faelle = [("die Bodenfläche $OABC$", "z", 0, "$xy$-Ebene", True),
              ("die Deckfläche $PQRS$", "z", 3, "$xy$-Ebene", False),
              ("die Seitenfläche $OAQP$", "y", 0, "$xz$-Ebene", True),
              ("die Seitenfläche $CBRS$", "y", 7, "$xz$-Ebene", False),
              ("die Seitenfläche $ABRQ$", "x", 6, "$yz$-Ebene", False)]
    for v, (flaeche, k, wert, ke, selbst) in enumerate(faelle, 1):
        lage = (f"die {ke} selbst" if selbst
                else f"parallel zur {ke}, keine Koordinatenebene")
        aus.append(um(g, variante=v, sprosse_text=st,
            merkmal=("fester Quader: die Fläche wandert; Gleichung mit "
                     "nur einer Variablen hinschreiben und lesen"),
            aufgabe=(Q3 + f" Gib eine Gleichung der Ebene an, in der "
                     f"{flaeche} liegt. Ist sie eine Koordinatenebene?"),
            form="teil", antwort="",
            loesung=(f"gleiche Koordinate der Ecken: ${k} = {wert}$; "
                     f"Ergebnis: ${k} = {wert}$, {lage}"),
            pruef=json.dumps(wert), grafik="", loesungsgrafik="",
            original=None))
    return aus


# ---------------------------------------------------------------- e4
# Feste Ebene E: 2x − y + 4z = 3; der Punkt wandert.
def e4():
    rows = lade("e4")
    out = []
    for r in kette(rows, 1):
        if r["hoehe"] == "grundfall":
            continue
        out.append(nachziehen(r, sprosse_text=kettentext(r)))
        if r["hoehe"] == "vorstufe" and r["variante"] == 4:
            out += e4_grundfall(zeile(rows, 1, 1, 1))
    out += [nachziehen(r) for r in kette(rows, 2)]
    for r in kette(rows, 3):
        n = (r["sprosse"], r["variante"])
        if n == (1, 2):
            out.append(um(r, aufgabe=(
                "Sara prüft $E\\colon 3x + y - z = 2$ und "
                "$F\\colon 6x + 2y - 2z = 4$: „Die Normalenvektoren sind "
                "Vielfache voneinander. $(1 | 0 | 1)$ liegt in $E$, denn "
                "$3 + 0 - 1 = 2$, und erfüllt auch $F$, denn $6 + 0 - 2 = "
                "4$. Also sind $E$ und $F$ identisch.“ Prüfe, ob Sara "
                "richtig gerechnet hat."),
                loesung=("Richtig. Kollineare Normalenvektoren heißen "
                         "parallel oder identisch; erfüllt ein Punkt von "
                         "$E$ auch $F$, sind die Ebenen identisch."),
                pruef=""))
        elif n == (1, 3):
            out.append(um(r, aufgabe=(
                "Ein Prisma hat die Grundfläche in $z = 0$ und die "
                "Deckfläche in $z = 12$. Die Ebene $z = c$ soll es so "
                "teilen, dass der obere Teil dreimal so groß ist wie der "
                "untere. Vier Schüler geben an: (1) $z = 3$; (2) $z = 6$; "
                "(3) $z = 9$; (4) $z = 13$. Welche Ergebnisse können nicht "
                "stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(2) kann nicht stimmen – in halber Höhe wären "
                         "beide Teile gleich groß; (3) kann nicht stimmen – "
                         "dann wäre der untere Teil größer als der obere; "
                         "(4) kann nicht stimmen – $z = 13$ liegt über der "
                         "Deckfläche und schneidet das Prisma nicht."),
                pruef=""))
        elif n == (2, 2):
            out.append(um(r, aufgabe=(
                "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
                "Begründe. (1) Zwei Ebenen, deren Normalenvektoren "
                "Vielfache voneinander sind, haben nie einen gemeinsamen "
                "Punkt. (2) Sind die Normalenvektoren zweier Ebenen keine "
                "Vielfachen voneinander, dann schneiden sich die Ebenen. "
                "(3) Durch jeden Punkt geht genau eine Ebene mit dem "
                "Normalenvektor $(2 | 1 | 3)$."),
                loesung=("(1) falsch, z. B. sind $x + y + z = 1$ und "
                         "$3x + 3y + 3z = 3$ identisch, sie haben alle "
                         "Punkte gemeinsam; (2) wahr, denn nicht parallele "
                         "Ebenen schneiden sich in einer Geraden; (3) wahr, "
                         "denn der Normalenvektor legt die linke Seite fest "
                         "und der Punkt die Konstante."),
                pruef=""))
        elif n == (2, 3):
            out.append(um(r, aufgabe=(
                "Jan sagt: „$E\\colon 2x - y + z = 5$ und "
                "$F\\colon 4x - 2y + 2z = 10$ sind echt parallel, denn ihre "
                "Normalenvektoren sind Vielfache voneinander.“ Begründe, "
                "ohne genau zu rechnen, ob Jan recht hat."),
                loesung=("Nein; die Gleichung von $F$ ist das Doppelte der "
                         "Gleichung von $E$, beide beschreiben dieselben "
                         "Punkte – die Ebenen sind identisch, nicht echt "
                         "parallel."),
                pruef=""))
        elif n == (3, 3):
            out.append(um(r, aufgabe=(
                "Zwei Glasböden eines schrägen Regals liegen in "
                "$E\\colon x + 4z = 7$ und $F\\colon 2x + 8z = 30$ "
                "(1 LE = 1 dm, $z$ zeigt nach oben). Senkrecht übereinander "
                "sollen zwischen den Böden mindestens 1,8 dm Platz sein. "
                "Reicht das?"),
                loesung=("Ja; Gleichung von $F$ halbieren: $x + 4z = 15$, "
                         "also parallel zu $E$; Höhenunterschied bei "
                         "gleichem $x$: $\\frac{15 - 7}{4} = 2$ dm; "
                         "Vergleich: $2 > 1{,}8$, der Platz reicht."),
                pruef="[15, 2]"))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


def e4_grundfall(g):
    st = kettentext(g)
    aus = []
    for v, p in enumerate([(1, 1, 1), (3, 2, 1), (2, 1, 2), (1, -2, 3),
                           (0, -3, 1)], 1):
        x, y, z = p
        e = 2 * x - y + 4 * z
        ys = f"- {y}" if y >= 0 else f"+ {-y}"
        aus.append(um(g, variante=v, sprosse_text=st,
            merkmal=("feste Ebene $E$, der Punkt wandert: gleicher "
                     "Normalenvektor, neue Konstante aus dem Punkt"),
            aufgabe=(f"Gib eine Gleichung der Ebene $F$ an, die parallel "
                     f"zu $E\\colon 2x - y + 4z = 3$ ist und durch "
                     f"$P{T(*p)}$ geht."),
            form="teil", antwort="",
            loesung=(f"Normalenvektor übernehmen: $2x - y + 4z = e$; "
                     f"Punkt einsetzen: $e = 2 \\cdot {x} {ys} + 4 \\cdot "
                     f"{z} = {e}$; Ergebnis: $F\\colon 2x - y + 4z = {e}$"),
            pruef=str(e), grafik="", loesungsgrafik="", original=None))
    return aus


def zahlen(out, alt):
    z = {"uebernommen": 0, "neu": 0, "umgeschrieben": 0}
    for r in out:
        z[r["_art"]] += 1
    z["entfallen"] = alt - z["uebernommen"] - z["umgeschrieben"]
    return z


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["e1", "e2", "e3", "e4"]
    fn = {"e1": e1, "e2": e2, "e3": e3, "e4": e4}
    zf = B / "_tmp" / "nachzug-zahlen.json"
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

"""Nachzug bank/vektoren-und-rechenoperationen auf die Mappe vom 29.09.
(Katalog 2a296e5).

Einmalig. Liest den Bestand (27./28.09.), zieht quelle, sprosse, id
und sprosse_text nach, schreibt die neue Sprosse e2 s3 (zwei
Kantenwege), die Grundfall-Päckchen e1 und e3 (e2 hat schon einen
festen Quader) und die Pflichtformen (P1, P2, P4, P6, P8).
Zählt je Einheit übernommen/neu/umgeschrieben/entfallen und schreibt
sie nach bank/vektoren-und-rechenoperationen/_tmp/zahlen.json.

Aufruf: python3 werkzeuge/einmalig/nachzug-vektoren-und-rechenoperationen-2026-09-29.py [e1 e2 e3]
"""
import copy
import json
import sys
from pathlib import Path

E = "vektoren-und-rechenoperationen"
B = Path(__file__).resolve().parents[2] / "bank" / E
QMAP = {37: 35, 83: 81, 84: 82, 85: 83, 80: 78}
VORSTUFE = {
    81: ("„Zahl oder Pfeil?“ – zu Größen einer Aufgabe ankreuzen, ob eine "
         "Zahl (Länge, Faktor, Koordinate, Skalarprodukt) oder ein Vektor "
         "(Richtung, Verschiebung, Ortsvektor) gemeint ist; nichts rechnen"),
    82: ("„Wohin führt der Term?“ – zu Vektortermen den Weg am Schrägbild "
         "mit dem Finger nachfahren und ankreuzen, ob er an einer Ecke, "
         "einer Kantenmitte oder einer Flächenmitte endet; nichts rechnen"),
    83: ("„Zahl oder Pfeil?“ – zu Sachgrößen ankreuzen, ob eine Zahl oder "
         "ein Vektor gemeint ist; nichts rechnen"),
}


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
    if r["hoehe"] == "vorstufe" and r["quelle"] in VORSTUFE:
        r["sprosse_text"] = VORSTUFE[r["quelle"]]
    r.update(kw)
    r.setdefault("_art", "uebernommen")
    r["id"] = rid(r)
    return r


def um(r, **kw):
    """Umgeschrieben: Zeile bleibt an ihrem Platz, Inhalt neu."""
    r = nachziehen(r)
    r.update(kw)
    r["_art"] = "umgeschrieben"
    r["id"] = rid(r)
    return r


def neu(vorlage, **kw):
    r = nachziehen(vorlage)
    r.update(kw)
    r["_art"] = "neu"
    r["id"] = rid(r)
    return r


def T(*k):
    def f(x):
        s = f"{x:g}" if isinstance(x, float) else str(x)
        return s.replace(".", "{,}").replace("-", "-")
    return "(" + " | ".join(f(x) for x in k) + ")"


def sub(p, q):
    return tuple(b - a for a, b in zip(p, q))


def by(rows, k, s, v=None):
    out = [r for r in rows if r["kette_nr"] == k and r["sprosse"] == s]
    return out if v is None else [r for r in out if r["variante"] == v][0]


# ---------------------------------------------------------------- e1
Q1 = {"A": (2, 1, 0), "B": (6, 1, 0), "C": (6, 4, 0), "D": (2, 4, 0),
      "E": (2, 1, 3), "F": (6, 1, 3), "G": (6, 4, 3), "H": (2, 4, 3)}
Q1_TEXT = ("Der Quader $ABCDEFGH$ hat die Ecken " + ", ".join(
    f"${n}{T(*p)}$" for n, p in Q1.items()) + ".")


def e1():
    rows = lade("e1")
    out = []
    out += [nachziehen(r) for r in by(rows, 1, 0)]
    out += [nachziehen(r) for r in by(rows, 2, 0)]
    # Grundfall-Päckchen: fester Quader, A bleibt, die Zielecke wandert
    for v, x in enumerate(["C", "F", "G", "H", "B"], 1):
        alt = by(rows, 2, 1, v)
        ab = sub(Q1["A"], Q1[x])
        ga = tuple(-c for c in ab)
        zw = tuple(2 * c for c in ab)
        vx = f"\\overrightarrow{{A{x}}}"
        loes = (f"Spitze minus Fuß: ${vx} = {T(*Q1[x])} - {T(*Q1['A'])} "
                f"= {T(*ab)}$; Gegenvektor: $\\overrightarrow{{{x}A}} = "
                f"{T(*ga)}$; Vielfaches: $2 \\cdot {vx} = {T(*zw)}$; "
                f"Ergebnis: ${vx} = {T(*ab)}$, $\\overrightarrow{{{x}A}} = "
                f"{T(*ga)}$, $2 \\cdot {vx} = {T(*zw)}$")
        out.append(um(alt,
            merkmal=("Verbindungsvektor als Spitze minus Fuß, Gegenvektor "
                     "und Vielfaches daraus; fester Quader, die Zielecke "
                     "wandert"),
            aufgabe=(Q1_TEXT + f" Gib ${vx}$, den Gegenvektor "
                     f"$\\overrightarrow{{{x}A}}$ und $2 \\cdot {vx}$ an."),
            loesung=loes, pruef=json.dumps(list(ab) + list(ga) + list(zw)),
            antwort="", grafik="", loesungsgrafik="", original=None))
    for s in range(2, 7):
        out += [nachziehen(r) for r in by(rows, 2, s)]
    # Pflicht k3
    f = by(rows, 3, 1)
    out.append(nachziehen(f[0]))                       # Schülerrechnung
    out.append(um(f[1],                                # P2 fehlerfrei
        aufgabe=("Gesucht ist $a < 0$ mit $|(a | 4)| = 5$. Tim rechnet: "
                 "$a^2 + 16 = 25$, also $a^2 = 9$, also $a = 3$ oder "
                 "$a = -3$; wegen $a < 0$ ist $a = -3$. Prüfe, ob Tim "
                 "richtig gerechnet hat."),
        loesung=("Richtig. Die quadrierte Betragsgleichung liefert beide "
                 "Vorzeichen, und die Bedingung $a < 0$ wählt $a = -3$ aus."),
        pruef=""))
    out.append(um(f[2],                                # P1 Serie
        aufgabe=("Gesucht ist ein Vektor, der so lang ist wie "
                 "$\\vec v = (6 | 2 | 3)$, aber nicht kollinear zu "
                 "$\\vec v$. Vier Vorschläge: (1) $(-6 | -2 | -3)$; "
                 "(2) $(2 | 3 | 6)$; (3) $(12 | 4 | 6)$; (4) $(6 | 2 | 5)$. "
                 "Welche Ergebnisse können nicht stimmen? Begründe, ohne "
                 "genau zu rechnen."),
        loesung=("(1) kann nicht stimmen – das ist der Gegenvektor, das "
                 "$(-1)$-Fache, also kollinear; (3) kann nicht stimmen – "
                 "das Doppelte von $\\vec v$, kollinear und doppelt so "
                 "lang; (4) kann nicht stimmen – zwei Koordinaten gleich, "
                 "die dritte größer, also länger als $\\vec v$. (2) passt: "
                 "dieselben Zahlen in anderer Reihenfolge, gleich lang, "
                 "kein Vielfaches."),
        pruef=""))
    g = by(rows, 3, 2)
    out.append(um(g[0],                                # Begründe, warum
        aufgabe=("Begründe, warum die Gleichung $a^2 = 25$ zwei Werte "
                 "für $a$ liefert."),
        loesung=("Weil das Quadrieren das Vorzeichen löscht: $5^2$ und "
                 "$(-5)^2$ ergeben beide 25 – eine quadrierte "
                 "Betragsgleichung hat deshalb zwei Lösungen mit "
                 "entgegengesetztem Vorzeichen.")))
    out.append(um(g[1],                                # P6 Personenaussage
        aufgabe=("Ole sagt: „Zwei Vektoren mit derselben Koordinatensumme "
                 "können verschieden lang sein.“ Begründe, ohne genau zu "
                 "rechnen, ob Ole recht hat."),
        loesung=("Ja; die Länge hängt von den Quadraten der Koordinaten ab, "
                 "nicht von ihrer Summe: $(3 | 0 | 0)$ und $(1 | 1 | 1)$ "
                 "haben beide die Summe 3, aber der erste ist 3 lang, der "
                 "zweite nur $\\sqrt{3}$.")))
    out.append(um(g[2],                                # P4 Aussagenserie
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. (1) Jeder Vektor hat genau einen "
                 "Gegenvektor. (2) Zwei gleich lange Vektoren sind immer "
                 "kollinear. (3) Es gibt einen Vektor mit dem Betrag 0."),
        loesung=("(1) wahr, denn der Gegenvektor $-\\vec v$ ist der eine "
                 "Vektor, der $\\vec v$ zum Nullvektor ergänzt; (2) falsch, "
                 "z. B. sind $(5 | 0 | 0)$ und $(0 | 5 | 0)$ beide 5 lang, "
                 "aber keiner ist ein Vielfaches des anderen; (3) wahr, "
                 "denn der Nullvektor $(0 | 0 | 0)$ hat die Länge 0.")))
    for s in (3, 4):
        out += [nachziehen(r) for r in by(rows, 3, s)]
    return out, len(rows)


# ---------------------------------------------------------------- e2
UVW = ("Im Quader $ABCDEFGH$ (Grafik) ist $\\vec u = \\overrightarrow{AB}$, "
       "$\\vec v = \\overrightarrow{AD}$ und $\\vec w = \\overrightarrow{AE}$.")


def e2():
    rows = lade("e2")
    grafik_uvw = by(rows, 1, 3, 1)["grafik"]
    out = []
    for s in (0, 1, 2):
        out += [nachziehen(r) for r in by(rows, 1, s)]
    # neue Sprosse s3: zwei Kantenwege, ein Vektor
    st3 = ("denselben Verbindungsvektor auf zwei verschiedenen Kantenwegen "
           "schreiben und zeigen, dass beide dasselbe ergeben")
    vorlage = by(rows, 1, 2, 1)
    faelle = [
        ("\\overrightarrow{BH}", "über $A$ und $D$", "über $F$ und $E$",
         "\\overrightarrow{BA} + \\overrightarrow{AD} + \\overrightarrow{DH}"
         " = -\\vec u + \\vec v + \\vec w",
         "\\overrightarrow{BF} + \\overrightarrow{FE} + \\overrightarrow{EH}"
         " = \\vec w - \\vec u + \\vec v",
         "-\\vec u + \\vec v + \\vec w"),
        ("\\overrightarrow{DF}", "über $A$ und $B$", "über $H$ und $E$",
         "\\overrightarrow{DA} + \\overrightarrow{AB} + \\overrightarrow{BF}"
         " = -\\vec v + \\vec u + \\vec w",
         "\\overrightarrow{DH} + \\overrightarrow{HE} + \\overrightarrow{EF}"
         " = \\vec w - \\vec v + \\vec u",
         "\\vec u - \\vec v + \\vec w"),
        ("\\overrightarrow{MG}", "über $B$ und $C$",
         "über $A$, $E$ und $H$",
         "\\overrightarrow{MB} + \\overrightarrow{BC} + \\overrightarrow{CG}"
         " = \\frac{1}{2}\\vec u + \\vec v + \\vec w",
         "\\overrightarrow{MA} + \\overrightarrow{AE} + \\overrightarrow{EH}"
         " + \\overrightarrow{HG} = -\\frac{1}{2}\\vec u + \\vec w + \\vec v"
         " + \\vec u",
         "\\frac{1}{2}\\vec u + \\vec v + \\vec w"),
    ]
    for v, (vek, w1, w2, z1, z2, erg) in enumerate(faelle, 1):
        mz = " $M$ ist die Mitte der Kante $AB$." if "M" in vek else ""
        out.append(neu(vorlage, sprosse=3, sprosse_text=st3, variante=v,
            merkmal=("zwei Kantenwege für denselben Vektor: Glieder mit "
                     "Richtung sammeln, rückwärts mit Minus"),
            form="text", antwort="",
            aufgabe=(UVW + mz + f" Schreibe ${vek}$ einmal {w1} und einmal "
                     f"{w2} mit $\\vec u$, $\\vec v$, $\\vec w$. Zeige, dass "
                     "beide Wege dasselbe ergeben."),
            loesung=(f"erster Weg ({w1[5:]}): ${z1}$; zweiter Weg "
                     f"({w2[5:]}): ${z2}$; zusammenfassen: beide ergeben "
                     f"${erg}$; Ergebnis: ${vek} = {erg}$"),
            pruef=("[[1, 2]]" if "frac" in erg else ""), original=None,
            grafik=grafik_uvw, loesungsgrafik="", quelle=82))
    for s in range(3, 9):
        out += [nachziehen(r, sprosse=s + 1) for r in by(rows, 1, s)]
    # Pflicht k2
    f = by(rows, 2, 1)
    out.append(um(f[0],                                # P1 Serie
        aufgabe=("Der Quader $ABCDEFGH$ hat die Ecken $A(0 | 0 | 0)$, "
                 "$B(6 | 0 | 0)$, $D(0 | 4 | 0)$ und $E(0 | 0 | 3)$. Vier "
                 "Schüler geben den Punkt $P$ mit $\\overrightarrow{AP} = "
                 "\\overrightarrow{AB} + \\frac{1}{2} \\cdot "
                 "\\overrightarrow{AD} + \\frac{1}{2} \\cdot "
                 "\\overrightarrow{AE}$ an: (1) $P(6 | 2 | 1{,}5)$; "
                 "(2) $P(6 | 4 | 1{,}5)$; (3) $P(3 | 2 | 1{,}5)$; "
                 "(4) $P(6 | 2 | 3)$. Welche Ergebnisse können nicht "
                 "stimmen? Begründe, ohne genau zu rechnen."),
        loesung=("(2) kann nicht stimmen – die halbe Kante $AD$ gibt in "
                 "$x_2$ die 2, nicht die ganze 4; (3) kann nicht stimmen – "
                 "die ganze Kante $AB$ gibt in $x_1$ die 6, nicht die Hälfte; "
                 "(4) kann nicht stimmen – die halbe Kante $AE$ gibt in "
                 "$x_3$ die 1,5, nicht die ganze 3. (1) passt."),
        pruef=""))
    out.append(um(f[1],                                # P2 fehlerfrei
        aufgabe=(UVW + " Lea schreibt: $\\overrightarrow{CE} = "
                 "\\overrightarrow{CB} + \\overrightarrow{BA} + "
                 "\\overrightarrow{AE} = -\\vec v - \\vec u + \\vec w$. "
                 "Prüfe, ob Lea richtig gerechnet hat."),
        loesung=("Richtig. $\\overrightarrow{CB}$ und "
                 "$\\overrightarrow{BA}$ laufen gegen $\\vec v$ und "
                 "$\\vec u$ – Rückwärtsgehen wechselt das Vorzeichen –, "
                 "$\\overrightarrow{AE} = \\vec w$."),
        pruef="", grafik=grafik_uvw, loesungsgrafik=""))
    out.append(nachziehen(f[2]))                       # Schülerrechnung
    g = by(rows, 2, 2)
    out.append(um(g[0],                                # Begründe, warum
        aufgabe=("Begründe, warum jeder Weg über die Ecken des Quaders von "
                 "$A$ nach $G$ denselben Vektor liefert."),
        loesung=("Weil jeder solche Weg aus denselben Kantenvektoren "
                 "$\\vec u$, $\\vec v$, $\\vec w$ besteht, nur in anderer "
                 "Reihenfolge, und bei der Vektoraddition die Reihenfolge "
                 "der Summanden die Summe nicht ändert "
                 "(Kommutativgesetz).")))
    out.append(um(g[1],                                # P4 Aussagenserie
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. (1) Ein Einheitsvektor hat immer die "
                 "Länge 1. (2) Jeder Vektor wird zu einem Einheitsvektor, "
                 "wenn man ihn durch seinen Betrag teilt. (3) Der Vektor "
                 "$2 \\cdot \\vec r$ ist immer doppelt so lang wie "
                 "$\\vec r$."),
        loesung=("(1) wahr, denn so ist der Einheitsvektor erklärt: "
                 "Richtung von $\\vec r$, Länge 1; (2) falsch, z. B. hat "
                 "der Nullvektor den Betrag 0, und durch 0 kann man nicht "
                 "teilen; (3) wahr, denn jede Koordinate verdoppelt sich, "
                 "also $|2 \\cdot \\vec r| = 2 \\cdot |\\vec r|$.")))
    out.append(um(g[2],                                # P6 Personenaussage
        aufgabe=("Kai sagt: „Wenn $\\vec r$ schon die Länge 1 hat, liegt "
                 "der Punkt mit $\\overrightarrow{OL} + 5 \\cdot \\vec r$ "
                 "genau im Abstand 5 von $L$.“ Begründe, ohne zu rechnen, "
                 "ob Kai recht hat."),
        loesung=("Ja; $5 \\cdot \\vec r$ ist fünfmal so lang wie "
                 "$\\vec r$, also 5 lang – normieren ist nur nötig, wenn "
                 "$\\vec r$ nicht schon ein Einheitsvektor ist.")))
    out += [nachziehen(r) for r in by(rows, 2, 3)]
    a = by(rows, 2, 4)
    out.append(um(a[0],                                # P8 Grenzwert
        aufgabe=("Ein Raum ist 5 m lang ($x_1$), 4 m breit ($x_2$) und "
                 "2,5 m hoch ($x_3$), eine Bodenecke liegt im Ursprung. Eine "
                 "Lampe hängt an einem 0,7 m langen Kabel senkrecht unter "
                 "der Mitte der Decke. Kann ein 1,90 m großer Mensch "
                 "aufrecht unter der Lampe stehen, ohne sie zu berühren?"),
        antwort="",
        loesung=("Nein; Mitte der Decke: halbe Länge, halbe Breite, ganze "
                 "Höhe, also $(2{,}5 | 2 | 2{,}5)$; Kabel nach unten: "
                 "$(2{,}5 | 2 | 2{,}5 - 0{,}7) = (2{,}5 | 2 | 1{,}8)$; "
                 "vergleichen: die Lampe hängt in 1,8 m Höhe, "
                 "$1{,}8 < 1{,}9$."),
        pruef="[2.5, 2, 1.8]"))
    out += [nachziehen(r) for r in a[1:]]
    return out, len(rows)


# ---------------------------------------------------------------- e3
def e3():
    rows = lade("e3")
    out = [nachziehen(r) for r in by(rows, 1, 0)]
    tage = [("Montag", 36), ("Dienstag", 42), ("Mittwoch", 30),
            ("Donnerstag", 27), ("Freitag", 45)]
    for v, (tag, s) in enumerate(tage, 1):
        alt = by(rows, 1, 1, v)
        vek = T(24, s, 18)
        out.append(um(alt,
            merkmal=("Liste als Vektor, jede Komponente zählt eine Sorte; "
                     "dasselbe Eiscafé, eine Menge wandert"),
            aufgabe=(f"Ein Eiscafé verkauft am {tag} 24 Becher Vanille, "
                     f"{s} Becher Schoko und 18 Becher Erdbeere. Gib den "
                     "Absatzvektor (Vanille | Schoko | Erdbeere) an. Was "
                     "zählt die zweite Komponente?"),
            antwort="(__ | __ | __)",
            loesung=(f"Reihenfolge: Vanille, Schoko, Erdbeere; eintragen: "
                     f"${vek}$; zweite Komponente: die am {tag} verkauften "
                     f"Becher Schoko; Ergebnis: ${vek}$"),
            pruef=json.dumps([24, s, 18])))
    for s in (2, 3):
        out += [nachziehen(r) for r in by(rows, 1, s)]
    f = by(rows, 2, 1)
    out.append(um(f[0],                                # P1 Serie
        aufgabe=("Mengen $\\vec m = (3 | 5 | 2)$ in kg, Preise "
                 "$\\vec p = (2 | 4 | 1{,}5)$ in Euro je kg. Vier Schüler "
                 "geben $\\vec m \\circ \\vec p$ an: (1) 29 €; "
                 "(2) $(6 | 20 | 3)$ €; (3) 29,50 €; (4) 52 €. Welche "
                 "Ergebnisse können nicht stimmen? Begründe, ohne genau zu "
                 "rechnen."),
        loesung=("(2) kann nicht stimmen – das Skalarprodukt ist eine Zahl, "
                 "kein Vektor; (3) kann nicht stimmen – alle drei Produkte "
                 "sind ganze Zahlen ($2 \\cdot 1{,}5 = 3$), die Summe hat "
                 "keine Cent; (4) kann nicht stimmen – Überschlag: 10 kg zu "
                 "höchstens 4 € sind höchstens 40 €. (1) passt."),
        pruef=""))
    out.append(nachziehen(f[1]))                       # Schülerrechnung
    out.append(um(f[2],                                # P2 fehlerfrei
        aufgabe=("Karten $\\vec k = (30 | 12 | 5)$, Preise "
                 "$\\vec p = (9 | 6 | 7)$ in Euro. Tom rechnet: Einnahmen "
                 "$\\vec k \\circ \\vec p = 270 + 72 + 35 = 377$ €. Prüfe, "
                 "ob Tom richtig gerechnet hat."),
        loesung=("Richtig. Das Skalarprodukt ist die Summe der Produkte "
                 "gleichstelliger Komponenten, also eine Zahl: die "
                 "Einnahmen von 377 €."),
        pruef=""))
    g = by(rows, 2, 2)
    out.append(um(g[0],                                # Begründe, warum
        aufgabe=("Begründe, warum $\\vec m \\circ \\vec p$ eine Zahl und "
                 "kein Vektor ist."),
        loesung=("Weil beim Skalarprodukt die Produkte der Komponenten "
                 "addiert werden – übrig bleibt eine Summe, der "
                 "Gesamtpreis.")))
    out.append(um(g[1],                                # P4 Aussagenserie
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. (1) Das Skalarprodukt aus Mengen- und "
                 "Preisvektor ist immer eine Zahl. (2) Vertauscht man die "
                 "Reihenfolge der Sorten nur im Preisvektor, bleibt der "
                 "Gesamtpreis immer gleich. (3) Verdoppelt man jede Menge, "
                 "verdoppelt sich der Gesamtpreis."),
        loesung=("(1) wahr, denn es ist die Summe der Produkte; (2) falsch, "
                 "z. B. Mengen $(1 | 2)$ und Preise $(3 | 5)$ ergeben "
                 "$3 + 10 = 13$, vertauscht $(5 | 3)$ aber $5 + 6 = 11$; "
                 "(3) wahr, denn jeder Summand verdoppelt sich.")))
    out.append(um(g[2],                                # P6 Personenaussage
        aufgabe=("Paula sagt: „Kauft man von jeder Sorte gleich viel, darf "
                 "man den Gesamtpreis durch die Summe der Preise teilen und "
                 "erhält die Menge je Sorte.“ Begründe, ohne zu rechnen, ob "
                 "Paula recht hat."),
        loesung=("Ja; bei gleichen Mengen ist $\\vec m = t \\cdot "
                 "(1 | 1 | 1)$, und $\\vec m \\circ \\vec p$ ist $t$ mal die "
                 "Preissumme – nur dann, beim Verhältnis 1 : 1 : 1, "
                 "stimmt das Teilen.")))
    out += [nachziehen(r) for r in by(rows, 2, 3)]
    return out, len(rows)


def zahlen(out, alt):
    z = {"uebernommen": 0, "neu": 0, "umgeschrieben": 0}
    for r in out:
        z[r["_art"]] += 1
    z["entfallen"] = alt - z["uebernommen"] - z["umgeschrieben"]
    return z


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["e1", "e2", "e3"]
    fn = {"e1": e1, "e2": e2, "e3": e3}
    zf = B / "_tmp" / "zahlen.json"
    zf.parent.mkdir(exist_ok=True)
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

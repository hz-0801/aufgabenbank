#!/usr/bin/env python3
"""Baut neu-lineare-gleichungssysteme-duden9.jsonl (Kürzel lgs) und
rechnet jede Lösung mit sympy nach. Vom Buch nur Typ und Stufung;
Zahlen und Wortlaut eigen. Vorlage: baue_neu_qf.py."""
import json
import sympy as sp

x, y, z = sp.symbols("x y z")
E = "lineare-gleichungssysteme"
Q = "Duden WÜT Mathematik 9 (2017)"
R = sp.Rational
QU = {1: 125, 2: 126, 3: 127, 4: 128, 5: 132}   # wie die Bankzeilen
KE = {1: "Grafisch", 2: "Einsetzen", 3: "Addition", 4: "Sachaufgaben",
      5: "Drei Variablen und Lösungsvielfalt"}
zeilen = []
# Zusätze an vorhandenen Sprossen übernehmen sprosse_text, merkmal und
# hoehe der Bank (Prüfskript: je Sprosse einheitlich).
ALT = {}
for _e in range(1, 6):
    for _l in open(f"aufgabenbank/bank/{E}/e{_e}.jsonl", encoding="utf-8"):
        _r = json.loads(_l)
        if _r["kette_nr"] == 1:
            ALT.setdefault((_e, _r["sprosse"]),
                           (_r["sprosse_text"], _r["merkmal"], _r["hoehe"]))


def neu(einheit, sprosse, sprosse_text, merkmal, var, aufgabe, form,
        antwort, loesung, pruef, herkunft, grafik="", hoehe="sprosse"):
    if not isinstance(sprosse, str):
        sprosse_text, merkmal, hoehe = ALT[(einheit, sprosse)]
    zeilen.append({
        "id": f"{E}-e{einheit}-k1-s{sprosse}-v{var}",
        "eintrag": E, "einheit": einheit, "kette": KE[einheit],
        "kette_nr": 1, "sprosse": sprosse,
        "sprosse_text": sprosse_text, "merkmal": merkmal,
        "hoehe": hoehe, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": QU[einheit],
        "herkunft": f"{Q}, {herkunft}"})


def los(gl, var=(x, y)):
    s = sp.solve(gl, var, dict=True)
    assert len(s) == 1 and len(s[0]) == len(var), s
    return tuple(s[0][v] for v in var)


def anzahl(g1, g2):
    s = sp.solve([g1, g2], (x, y), dict=True)
    if not s:
        return "keine"
    return "genau eine" if len(s[0]) == 2 else "unendlich viele"


Eq = sp.Eq
KREUZ3 = ("\\\\ \\kreuz{genau eine}\\\\ \\kreuz{keine}\\\\ "
          "\\kreuz{unendlich viele}")

# ---------------- e1 ----------------
ST4 = "zwei Geraden zeichnen und Schnittpunkt ablesen"
assert los([Eq(x/2 + y, 3), Eq(x - y/2, 1)]) == (2, 2)
neu(1, 4, ST4, "Vorzahlen als Brüche: erst nach y umstellen, dann zeichnen", 4,
    "Zeichne die Geraden zu I: $\\frac{1}{2}x + y = 3$ und II: "
    "$x - \\frac{1}{2}y = 1$ in das Koordinatensystem. Stelle dazu "
    "zuerst beide Gleichungen nach $y$ um. Lies den Schnittpunkt ab.",
    "zeichnen", "",
    "I: $y = -\\frac{1}{2}x + 3$, II: $y = 2x - 2$; Schnittpunkt $(2|2)$",
    "[2, 2]", "S. 16 Nr. 7 – LGS grafisch lösen, Gleichungen in Form "
    "ax + by = c, auch mit Brüchen",
    grafik="\\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5]\n\\end{ksys}")

ST6 = "Lösung an einem gegebenen Bild ablesen"
assert los([Eq(y, -x/2 + 3), Eq(y, x)]) == (2, 2)
neu(1, 6, ST6, "Bild ohne Gleichungen: Gleichungen erst mit dem "
    "Steigungsdreieck bestimmen, dann den Punkt rechnerisch prüfen", 4,
    "Das Koordinatensystem zeigt die Geraden I und II. Lies den "
    "Schnittpunkt ab. Bestimme mit Steigungsdreiecken die Gleichungen "
    "der beiden Geraden. Prüfe durch Einsetzen, ob der abgelesene Punkt "
    "auf beiden Geraden liegt.", "teil",
    "S(__|__); I: y = __; II: y = __",
    "$S(2|2)$; I: $y = -\\frac{1}{2}x + 3$, II: $y = x$; Probe: "
    "$-\\frac{1}{2} \\cdot 2 + 3 = 2$ (wA), $2 = 2$ (wA)",
    "[2, 2]",
    "S. 16 Nr. 5 – Schnittpunkt ablesen, Gleichungen aus "
    "Steigungsdreiecken, Punkt rechnerisch prüfen",
    grafik="\\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5,ablesen]\n"
    "\\gerade{-0.5}{3}{I}\n\\gerade{1}{0}{II}\n\\end{ksys}")

ST7 = "Sonderfälle parallel und identisch"
MK7 = "erst nach y umstellen, dann Steigung und Achsenabschnitt vergleichen"
H = ("S. 16 Nr. 6 – nach y auflösen und Lösungsanzahl bestimmen, eine "
     "Gleichung mit Klammer oder Dezimalzahl")
for v, (t1, t2, g1, g2, l1, l2) in enumerate([
        ("3x - y = 2", "-9x = -(6 + 3y)", Eq(3*x - y, 2),
         Eq(-9*x, -(6 + 3*y)), "y = 3x - 2", "y = 3x - 2"),
        ("-4x + y = 3", "10x = 2{,}5y", Eq(-4*x + y, 3),
         Eq(10*x, R(5, 2)*y), "y = 4x + 3", "y = 4x"),
        ("2x + y = 1", "6x = 3y + 3", Eq(2*x + y, 1), Eq(6*x, 3*y + 3),
         "y = -2x + 1", "y = 2x - 1")], 4):
    a = anzahl(g1, g2)
    assert a == ["unendlich viele", "keine", "genau eine"][v - 4]
    neu(1, 7, ST7, MK7, v,
        f"Gegeben ist das Gleichungssystem I: ${t1}$ und II: ${t2}$. "
        "Stelle beide Gleichungen nach $y$ um. Kreuze dann an, wie viele "
        "Lösungen das System hat." + KREUZ3, "ankreuzen", "",
        f"{a} (I: ${l1}$, II: ${l2}$)", "", H)

STZ = ("NEU-zweite-gerade: zu einer gegebenen Gleichung die zweite so "
       "wählen, dass das System keine, unendlich viele oder eine "
       "vorgegebene Lösung hat (Vorschlag; nicht im Katalog)")
MKZ = "umgekehrt denken: aus der gewünschten Lösungsanzahl die Gerade bauen"
H = ("S. 16 Nr. 8 – zweite Gerade durch einen Punkt so legen, dass sie "
     "parallel ist oder die erste in einem vorgegebenen Punkt schneidet")
assert 2*1 + 2 == 4 and anzahl(Eq(y, 2*x - 1), Eq(y, 2*x + 2)) == "keine"
neu(1, "NEU-zweite-gerade", STZ, MKZ, 1,
    "Gegeben ist I: $y = 2x - 1$. Gib eine Gleichung II an, deren Gerade "
    "durch den Punkt $P(1|4)$ geht und für die das System keine Lösung "
    "hat.", "teil", "II: y = __",
    "gleiche Steigung, anderer Achsenabschnitt: $4 = 2 \\cdot 1 + n$, "
    "$n = 2$; II: $y = 2x + 2$", "[2, 2]", H)
assert los([Eq(x - y, 2), Eq(y, -x + 4)]) == (3, 1)
neu(1, "NEU-zweite-gerade", STZ, MKZ, 2,
    "Gegeben ist I: $x - y = 2$. Gib eine Gleichung II an, deren Gerade "
    "durch den Punkt $Q(0|4)$ geht und für die das System die Lösung "
    "$(3|1)$ hat.", "teil", "II: y = __",
    "II geht durch $(0|4)$ und $(3|1)$: $m = \\frac{1 - 4}{3 - 0} = -1$; "
    "II: $y = -x + 4$; Probe in I: $3 - 1 = 2$ (wA)", "[-1, 4]", H)
assert anzahl(Eq(2*x + y, 4), Eq(6*x + 3*y, 12)) == "unendlich viele"
neu(1, "NEU-zweite-gerade", STZ, MKZ, 3,
    "Gegeben ist I: $2x + y = 4$. Gib eine Gleichung II an, die mit "
    "$6x$ beginnt und für die das System unendlich viele Lösungen hat.",
    "teil", "II: 6x + __ y = __",
    "I mit $3$ malnehmen: II: $6x + 3y = 12$", "[3, 12]", H)

# ---------------- e2 ----------------
assert los([Eq(y - 4*x, R(3, 2)), Eq(3*x + 2*y, 14)]) == (1, R(11, 2))
neu(2, 6, "Dezimalzahlen (Geld)", "Dezimalzahl in der umzustellenden "
    "Gleichung, Lösung mit Komma", 4,
    "Löse das Gleichungssystem I: $y - 4x = 1{,}5$ und II: "
    "$5x + 2y = 16$ mit dem Einsetzungsverfahren.", "gleichungsraster",
    "", "I: $y = 4x + 1{,}5$; in II: $5x + 8x + 3 = 16$, $x = 1$; "
    "$y = 5{,}5$; Lösung $(1|5{,}5)$", "[1, 5.5]",
    "S. 18 Nr. 10 – Einsetzungsverfahren, Dezimalzahlen in den Gleichungen")

# ---------------- e3 ----------------
assert los([Eq(2*x + 3*y, R(5, 2)), Eq(-3*x + 2*y, 6)]) == (-1, R(3, 2))
neu(3, 4, "beide vervielfachen", "Dezimalzahl rechts, negative Lösung", 4,
    "Löse das Gleichungssystem I: $2x + 3y = 2{,}5$ und II: "
    "$-3x + 2y = 6$ mit dem Additionsverfahren. Vervielfache dazu beide "
    "Gleichungen.", "gleichungsraster", "",
    "I $\\cdot 3$, II $\\cdot 2$: $6x + 9y = 7{,}5$, $-6x + 4y = 12$; "
    "addieren: $13y = 19{,}5$, $y = 1{,}5$; $x = -1$; Lösung "
    "$(-1|1{,}5)$", "[-1, 1.5]",
    "S. 18 Nr. 9 – Additionsverfahren, beide Gleichungen vervielfachen, "
    "Dezimalzahl")

STO = ("NEU-ordnen: Gleichungen mit Klammern oder Variablen auf beiden "
       "Seiten erst auf die Form ax + by = c bringen, dann lösen "
       "(Vorschlag; nicht im Katalog)")
MKO = "erst ordnen: Klammern auflösen, x und y nach links, Zahlen nach rechts"
H = ("S. 18 Nr. 9c und Nr. 11 – Gleichungen ungeordnet, mit Klammern "
     "oder Brüchen; Verfahren wählen (auch S. 20 Nr. 17)")
g = [Eq(3*(x - 1) + 2*y, 10), Eq(2*(x + y) - 3, y + 5)]
assert los(g) == (3, 2) and sp.expand(3*(x-1) + 2*y - 10) == 3*x + 2*y - 13
neu(3, "NEU-ordnen", STO, MKO, 1,
    "Bringe beide Gleichungen zuerst auf die Form $ax + by = c$. Löse "
    "dann das System I: $3(x - 1) + 2y = 10$, II: $2(x + y) - 3 = y + 5$.",
    "gleichungsraster", "",
    "I: $3x + 2y = 13$, II: $2x + y = 8$; II $\\cdot 2$ und subtrahieren: "
    "$-x = -3$, $x = 3$; $y = 2$; Lösung $(3|2)$", "[3, 2]", H)
g = [Eq(y + 2*x - 9, 0), Eq(4*(x - y), x - 2*y - 4)]
assert los(g) == (2, 5)
neu(3, "NEU-ordnen", STO, MKO, 2,
    "Bringe beide Gleichungen zuerst auf die Form $ax + by = c$. Löse "
    "dann das System I: $y + 2x - 9 = 0$, II: $4(x - y) = x - 2y - 4$.",
    "gleichungsraster", "",
    "I: $2x + y = 9$, II: $3x - 2y = -4$; I $\\cdot 2$ und addieren: "
    "$7x = 14$, $x = 2$; $y = 5$; Lösung $(2|5)$", "[2, 5]", H)
g = [Eq(x/2 + y, 4), Eq(3*(x - y), 2*(x - 2*y) + 5)]
assert los(g) == (2, 3)
neu(3, "NEU-ordnen", STO, MKO, 3,
    "Bringe beide Gleichungen zuerst auf die Form $ax + by = c$. Löse "
    "dann das System I: $\\frac{x}{2} + y = 4$, II: "
    "$3(x - y) = 2(x - 2y) + 5$.", "gleichungsraster", "",
    "I: $\\frac{1}{2}x + y = 4$, II: $x + y = 5$; II $-$ I: "
    "$\\frac{1}{2}x = 1$, $x = 2$; $y = 3$; Lösung $(2|3)$", "[2, 3]", H)

# ---------------- e4 ----------------
assert los([Eq(x + y, 40), Eq(2*x - 3*y, 5)]) == (25, 15)
neu(4, 4, "Zahlenrätsel mit Summe und Differenz",
    "Differenz von Vielfachen statt einfacher Differenz", 4,
    "Die Summe zweier Zahlen ist $40$. Das Doppelte der ersten Zahl "
    "vermindert um das Dreifache der zweiten Zahl ergibt $5$. $x$ ist die "
    "erste Zahl, $y$ die zweite Zahl. Stelle die Gleichungen I und II auf.",
    "text", "I: __ \\quad II: __",
    "I: $x + y = 40$, II: $2x - 3y = 5$ (Lösung $x = 25$, $y = 15$)",
    "[40, 5]", "S. 18 Nr. 14 – Zahlenrätsel: Summe und Differenz aus "
    "Vielfachen")
assert los([Eq(x + y, 26), Eq(2*x + 4*y, 74)]) == (15, 11)
neu(4, 7, "aufstellen, lösen, zuordnen, Antwortsatz",
    "Anzahl und Beine: zwei Tierarten mit verschiedener Beinzahl", 4,
    "Auf einem Hof laufen Hühner und Ziegen herum. Es sind zusammen $26$ "
    "Tiere mit $74$ Beinen. Wie viele Hühner und wie viele Ziegen sind "
    "es? Stelle ein Gleichungssystem auf, löse es und schreibe einen "
    "Antwortsatz.", "gleichungsraster", "Hühner __, Ziegen __",
    "$x$ Hühner, $y$ Ziegen: I: $x + y = 26$, II: $2x + 4y = 74$; "
    "$x = 15$, $y = 11$. Es sind $15$ Hühner und $11$ Ziegen.",
    "[15, 11]", "S. 18 Nr. 13 – Tiere und Beine (Anzahl und Bestand), "
    "aufstellen und lösen")

# ---------------- e5 ----------------
S1 = ("eine vorgegebene Lösung in alle Gleichungen einsetzen und die "
      "Gültigkeit zeigen (Grundfall, viermal)")
I3 = [Eq(x + y + z, 6), Eq(x - y + 2*z, 5), Eq(2*x + y - z, 1)]
ok = [all(g.subs({x: a, y: b, z: c}) for g in I3)
      for a, b, c in [(3, 2, 1), (1, 2, 3), (2, 1, 3)]]
assert ok == [False, True, False]
neu(5, 1, S1, "aus mehreren Tripeln das passende durch Einsetzen finden", 6,
    "Gegeben ist das System I: $x + y + z = 6$, II: $x - y + 2z = 5$, "
    "III: $2x + y - z = 1$. Kreuze an, welches Zahlentripel die Lösung "
    "ist.\\\\ \\kreuz{$(3|2|1)$}\\\\ \\kreuz{$(1|2|3)$}\\\\ "
    "\\kreuz{$(2|1|3)$}", "ankreuzen", "",
    "$(1|2|3)$; $(3|2|1)$ scheitert an II ($3 \\neq 5$), $(2|1|3)$ an II "
    "($7 \\neq 5$)", "", "S. 20 Nr. 15 – Lösung aus mehreren "
    "Zahlentripeln durch Einsetzen auswählen")
S2 = ("ein gestaffeltes System durch Rückwärtseinsetzen lösen, auch nach "
      "dem Einsetzen eines Parameterwerts")
assert los([Eq(x + y + z, 10), Eq(3*y - z, 5), Eq(z, 4)], (x, y, z)) == (3, 3, 4)
neu(5, 2, S2, "ohne Parameter: unten anfangen, nach oben einsetzen", 4,
    "Löse das System I: $x + y + z = 10$, II: $3y - z = 5$, III: $z = 4$.",
    "gleichungsraster", "",
    "III: $z = 4$; II: $3y = 9$, $y = 3$; I: $x = 10 - 3 - 4 = 3$; "
    "Lösung $(3|3|4)$", "[3, 3, 4]",
    "S. 20 Nr. 16 – gestaffeltes System durch Rückwärtseinsetzen")

STD = ("NEU-dreiecksform: ein volles System (jede Gleichung mit allen drei "
       "Variablen) in zwei Schritten auf Dreiecksform bringen, lösen und "
       "die Probe machen (Vorschlag; nicht im Katalog)")
MKD = "zweimal eliminieren: erst x aus II und III, dann y aus III"
H = ("S. 20 Nr. 18 – Gaußverfahren ohne Koeffizientenmatrix, alle "
     "Variablen in allen Gleichungen, mit Probe (auch S. 19 Beispiel)")
for v, (gl, tx, sol, weg) in enumerate([
        ([Eq(-x + 2*y + 3*z, 5), Eq(2*x - 3*y + z, 10),
          Eq(3*x + y - 2*z, -1)],
         "I: $-x + 2y + 3z = 5$, II: $2x - 3y + z = 10$, III: "
         "$3x + y - 2z = -1$", (2, -1, 3),
         "II' = II $+ 2 \\cdot$ I: $y + 7z = 20$; III' = III $+ 3 \\cdot$ I: "
         "$7y + 7z = 14$; III' $- 7 \\cdot$ II': $-42z = -126$, $z = 3$; "
         "$y = -1$; $x = 2$; Lösung $(2|-1|3)$"),
        ([Eq(2*x + y + z, 4), Eq(x - y + 2*z, 11), Eq(3*x + 2*y - z, -5)],
         "I: $2x + y + z = 4$, II: $x - y + 2z = 11$, III: "
         "$3x + 2y - z = -5$", (1, -2, 4),
         "$2 \\cdot$ II $-$ I: $-3y + 3z = 18$; $3 \\cdot$ II $-$ III: "
         "$-5y + 7z = 38$; daraus $y = z - 6$, $-5z + 30 + 7z = 38$, "
         "$z = 4$; $y = -2$; $x = 1$; Lösung $(1|-2|4)$")], 1):
    assert los(gl, (x, y, z)) == sol
    neu(5, "NEU-dreiecksform", STD, MKD, v,
        f"Löse das System {tx}. Bringe es dazu auf Dreiecksform und mache "
        "die Probe in allen drei Gleichungen.", "gleichungsraster", "",
        weg, json.dumps(list(sol)), H)

STS = ("NEU-sach-drei-variablen: aus einem Text ein System mit drei "
       "Variablen aufstellen, lösen und die Lösung zuordnen (Vorschlag; "
       "nicht im Katalog)")
MKS = "drei Unbekannte benennen, drei Sätze in drei Gleichungen übersetzen"
gl = [Eq(x + y, 11), Eq(y + z, 17), Eq(x + z, 14)]
assert los(gl, (x, y, z)) == (4, 7, 10)
neu(5, "NEU-sach-drei-variablen", STS, MKS, 1,
    "Von drei Zahlen ist bekannt: Die erste und die zweite ergeben "
    "zusammen $11$, die zweite und die dritte $17$, die erste und die "
    "dritte $14$. Stelle ein Gleichungssystem auf und bestimme die drei "
    "Zahlen.", "gleichungsraster", "__, __, __",
    "I: $x + y = 11$, II: $y + z = 17$, III: $x + z = 14$; alle addiert: "
    "$2(x + y + z) = 42$, $x + y + z = 21$; $z = 10$, $x = 4$, $y = 7$",
    "[4, 7, 10]", "S. 21 Nr. 19 – drei Zahlen aus den Summen je zweier")
gl = [Eq(x + y + z, 91), Eq(y, 3*x + 2), Eq(z, y + 3)]
assert los(gl, (x, y, z)) == (12, 38, 41)
neu(5, "NEU-sach-drei-variablen", STS, MKS, 2,
    "Lena, ihre Mutter und ihr Vater sind zusammen $91$ Jahre alt. Die "
    "Mutter ist $2$ Jahre älter als das Dreifache von Lenas Alter. Der "
    "Vater ist $3$ Jahre älter als die Mutter. Wie alt sind die drei? "
    "Stelle ein Gleichungssystem auf und löse es.", "gleichungsraster",
    "Lena __, Mutter __, Vater __",
    "$x$ Lena, $y$ Mutter, $z$ Vater: I: $x + y + z = 91$, II: "
    "$y = 3x + 2$, III: $z = y + 3$; eingesetzt: $7x + 7 = 91$, $x = 12$, "
    "$y = 38$, $z = 41$. Lena ist $12$, die Mutter $38$, der Vater $41$ "
    "Jahre alt.", "[12, 38, 41]",
    "S. 21 Nr. 23 – Altersrätsel mit drei Personen")
gl = [Eq(2*x + 3*y + z, R(61, 10)), Eq(x + 2*y + 2*z, 5),
      Eq(3*x + y + z, R(11, 2))]
assert los(gl, (x, y, z)) == (R(6, 5), R(9, 10), 1)
neu(5, "NEU-sach-drei-variablen", STS, MKS, 3,
    "Im Schreibwarenladen zahlt Mia für $2$ Hefte, $3$ Stifte und $1$ "
    "Block $6{,}10\\,€$. Tom zahlt für $1$ Heft, $2$ Stifte und $2$ Blöcke "
    "$5{,}00\\,€$. Ali zahlt für $3$ Hefte, $1$ Stift und $1$ Block "
    "$5{,}50\\,€$. Was kostet ein Heft, ein Stift und ein Block?",
    "gleichungsraster", "Heft __ €, Stift __ €, Block __ €",
    "I: $2x + 3y + z = 6{,}10$, II: $x + 2y + 2z = 5$, III: "
    "$3x + y + z = 5{,}50$; III $-$ I: $x - 2y = -0{,}6$; "
    "$2 \\cdot$ I $-$ II: $3x + 4y = 7{,}2$; daraus $x = 1{,}20$, "
    "$y = 0{,}90$, $z = 1{,}00$. Ein Heft kostet $1{,}20\\,€$, ein Stift "
    "$0{,}90\\,€$, ein Block $1{,}00\\,€$.", "[1.2, 0.9, 1.0]",
    "S. 20 Wissen-Kasten Sachaufgabe – drei Artikel mit Anzahlen und "
    "Gesamtpreisen")

# Nachrechnen der Zwischenschritte in den Lösungstexten
assert sp.solve([y + 7*z - 20, 7*y + 7*z - 14]) == {y: -1, z: 3}
assert sp.solve([-3*y + 3*z - 18, -5*y + 7*z - 38]) == {y: -2, z: 4}
assert sp.solve([x - 2*y + R(3, 5), 3*x + 4*y - R(36, 5)]) == {x: R(6, 5), y: R(9, 10)}

with open(f"neu-{E}-duden9.jsonl", "w", encoding="utf-8", newline="\n") as f:
    for r in zeilen:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(zeilen), "Zeilen")

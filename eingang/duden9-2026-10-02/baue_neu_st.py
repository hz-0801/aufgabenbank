#!/usr/bin/env python3
"""Baut neu-st-duden9.jsonl (Eintrag daten) und rechnet jede Lösung
nach. Vorlage: baue_neu_pyt.py. Vom Buch nur Typ und Stufung; Zahlen
und Wortlaut eigen. Kette, sprosse_text, merkmal, hoehe, quelle werden
bei vorhandenen Sprossen aus der Bank übernommen."""
import json
import math
import statistics as st
from fractions import Fraction as Fr

Q = "Duden WÜT Mathematik 9 (2017)"
B = "aufgabenbank/bank/daten/"
E = "daten"
zeilen = []
_bank = {}


def bank(e):
    if e not in _bank:
        _bank[e] = [json.loads(l) for l in open(f"{B}e{e}.jsonl")]
    return _bank[e]


_zaehl = {}


def neu(e, k, s, aufgabe, form, antwort, loesung, pruef, herkunft,
        grafik="", neu_text=None, neu_merkmal=None):
    if neu_text is None:
        g = [r for r in bank(e) if r["kette_nr"] == k and r["sprosse"] == s]
        assert g, (e, k, s)
        v, n = g[0], len(g)
        kette, stx, mk, h, q = (v["kette"], v["sprosse_text"], v["merkmal"],
                                v["hoehe"], v["quelle"])
    else:
        v = next(r for r in bank(e) if r["kette_nr"] == k)
        kette, stx, mk, h, q, n = v["kette"], neu_text, neu_merkmal, \
            "sprosse", v["quelle"], 0
    key = (e, k, s)
    _zaehl[key] = _zaehl.get(key, n) + 1
    var = _zaehl[key]
    zeilen.append({
        "id": f"{E}-e{e}-k{k}-s{s}-v{var}", "eintrag": E, "einheit": e,
        "kette": kette, "kette_nr": k, "sprosse": s, "sprosse_text": stx,
        "merkmal": mk, "hoehe": h, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": q,
        "herkunft": f"{Q}, {herkunft}"})


def dz(x):
    s = f"{x:g}" if isinstance(x, float) else str(x)
    return s.replace(".", "{,}")


def liste(xs, sep=", "):
    return sep.join(f"${dz(x)}$" for x in xs)


def med(xs):
    return st.median(sorted(xs))


def quart(xs):
    """Halbierungsmethode wie in der Bank (ungerades n: Median ausgelassen)."""
    s = sorted(xs)
    n = len(s)
    lo, hi = s[:n // 2], s[(n + 1) // 2:]
    return med(lo), med(hi)


def quart_rang(xs, p):
    s = sorted(xs)
    k = p * len(s)
    if abs(k - round(k)) < 1e-9:
        k = int(round(k))
        return (s[k - 1] + s[k]) / 2
    return s[math.ceil(k) - 1]


# ===== Bank: e1 k4 s1 Klassen auszählen (Ü3 S. 117) ===================
w = [142, 128, 167, 150, 119, 175, 138, 160, 149, 183, 131, 156]
kl = [sum(x < 130 for x in w), sum(130 <= x < 150 for x in w),
      sum(150 <= x < 170 for x in w), sum(x >= 170 for x in w)]
assert kl == [2, 4, 4, 2] and sum(kl) == len(w)
neu(1, 4, 1,
    f"Äpfel werden nach Gewicht sortiert: klein unter $130$ g, mittel "
    f"$130$ g bis unter $150$ g, groß $150$ g bis unter $170$ g, sehr "
    f"groß ab $170$ g. Die Äpfel einer Kiste wiegen in g: {liste(w)}. "
    f"Zähle aus, wie viele Äpfel in jeder Klasse liegen.",
    "tabelle", "",
    "$2$; $4$; $4$; $2$ – ein Wert genau auf der Grenze gehört zur "
    "höheren Klasse",
    json.dumps(kl), "S. 117 Nr. 3 – Urliste in benannte Klassen mit "
    "„unter“-Grenzen und offener oberster Klasse einsortieren",
    grafik="\\sachtabelle{lc}{Klasse & Anzahl}{klein & \\leerzelle \\\\ "
    "mittel & \\leerzelle \\\\ groß & \\leerzelle \\\\ sehr groß & "
    "\\leerzelle}")

# ===== Bank: e4 k3 s1 Mittel und Median vergleichen (Ü6 S. 118) ======
f = [31, 28, 33, 29, 30, 52, 28, 32, 30]
m = sum(f) / len(f)
assert sum(f) == 293 and med(f) == 30 and round(m, 1) == 32.6
neu(4, 3, 1,
    f"Ole fährt mit dem Bus zur Schule. An neun Tagen hat er die Fahrzeit "
    f"in Minuten notiert: {liste(f)}. Berechne Median und Mittelwert. "
    f"Seine Oma fragt, wie lange die Fahrt dauert. Welchen Wert sollte "
    f"Ole nennen? Begründe.",
    "text", "",
    "sortiert $28$, $28$, $29$, $30$, $30$, $31$, $32$, $33$, $52$; "
    "Median $= 30$ min; Mittelwert $= 293 : 9 \\approx 32{,}6$ min; "
    "besser der Median: der eine Stautag mit $52$ min zieht den "
    "Mittelwert hoch",
    json.dumps([30, round(m, 1)]),
    "S. 118 Nr. 6 – Median und Mittel einer Zeitenliste vergleichen und "
    "den typischen Wert für eine Auskunft wählen")

# ===== Bank: e5 k2 s7 Boxplot aus unsortierter Liste, min/s (Ü12 S. 124)
t = [(1, 40), (0, 30), (2, 10), (1, 5), (3, 0), (1, 50), (0, 55),
     (2, 25), (1, 15), (1, 40)]
sek = [a * 60 + b for a, b in t]
qu, qo = quart(sek)
fuenf = [min(sek), qu, med(sek), qo, max(sek)]
mw = sum(sek) / len(sek)
assert fuenf == [30, 65, 100, 130, 180] and mw == 99
zt = "; ".join(f"${a}$ min ${b}$ s" for a, b in t)
neu(5, 2, 7,
    f"Mia wartet morgens an einer Ampel. Sie sagt: „Ich warte im Schnitt "
    f"etwa $2$ Minuten.“ Ihre Wartezeiten der letzten Tage: {zt}. Rechne "
    f"alle Zeiten in Sekunden um und sortiere sie. Bestimme die fünf "
    f"Kennwerte, zeichne den Boxplot und nimm Stellung zu Mias Aussage.",
    "zeichnen", "",
    "in s sortiert $30$, $55$, $65$, $75$, $100$, $100$, $110$, $130$, "
    "$145$, $180$; Minimum $= 30$, unteres Quartil $= 65$, Median "
    "$= 100$, oberes Quartil $= 130$, Maximum $= 180$ (alles in s); "
    "Mittelwert $= 990 : 10 = 99$ s, also $1$ min $39$ s; an der Hälfte "
    "der Tage wartet sie höchstens $100$ s, nur an einem Viertel länger "
    "als $130$ s; „etwa $2$ Minuten“ ist zu hoch geschätzt",
    json.dumps(fuenf + [99]),
    "S. 124 Nr. 12 – Zeiten in min und s umrechnen, Boxplot zeichnen und "
    "eine Schätzung zum Durchschnitt beurteilen",
    grafik="\\begin{boxplots}[xmin=0,xmax=200,xstep=20,xlabel=Sekunden] "
    "\\bp{}{Ampel} \\end{boxplots}")

# ===== Bank: e5 k2 s2 Quartilabstand (Wissen S. 119) ==================
bp = [12, 18, 24, 27, 40]
assert bp[4] - bp[0] == 28 and bp[3] - bp[1] == 9
neu(5, 2, 2,
    "Lies am Boxplot die nötigen Werte ab. Berechne die Spannweite und "
    "den Quartilabstand (oberes Quartil minus unteres Quartil, also die "
    "Breite der Box).",
    "teil", "__, __",
    "Spannweite $= 40 - 12 = 28$; Quartilabstand $= 27 - 18 = 9$",
    "[28, 9]", "S. 119 Wissen – Quartilabstand als Streuungsmaß",
    grafik="\\begin{boxplots}[xmin=10,xmax=45,xstep=5,xlabel=Jahre] "
    "\\bp{12,18,24,27,40}{Alter} \\end{boxplots}")

# ===== Bank: e4 k2 s1 Standardabweichung mit Hilfstabelle (Ü9 S. 121) =
x = [14, 18, 11, 20, 15, 12]
xq = Fr(sum(x), len(x))
var = sum((v - xq) ** 2 for v in x) / len(x)
assert xq == 15 and var == 10
sig = math.sqrt(var)
zeilenT = " \\\\ ".join(f"${i+1}$ & ${v}$ & \\leerzelle & \\leerzelle"
                        for i, v in enumerate(x))
neu(4, 2, 1,
    f"Sechs Pflanzen sind so viele cm gewachsen: {liste(x)}. Berechne "
    f"den Mittelwert. Fülle dann die Tabelle aus und berechne die "
    f"Varianz (Summe der Abweichungsquadrate durch $n$) und die "
    f"Standardabweichung.",
    "tabelle", "x̄ = __, σ² = __, σ ≈ __",
    "$\\bar{x} = 90 : 6 = 15$; Abweichungen $-1$, $3$, $-4$, $5$, $0$, "
    "$-3$; Quadrate $1$, $9$, $16$, $25$, $0$, $9$, Summe $60$; "
    "$\\sigma^2 = 60 : 6 = 10$; $\\sigma = \\sqrt{10} \\approx 3{,}16$ cm",
    json.dumps([15, 10, sig]),
    "S. 121 Nr. 9 – Varianz und Standardabweichung mit Hilfstabelle "
    "(Abweichung, Abweichungsquadrat), Nenner n",
    grafik="\\sachtabelle{cccc}{$i$ & $x_i$ & $x_i - \\bar{x}$ & "
    "$(x_i - \\bar{x})^2$}{" + zeilenT + "}")

# ===== Bank: e3 k1 s3 Rest zu hundert Prozent (Ü13 S. 124) ============
r23, r24 = 100 - 35 - 40, 100 - 42 - 36
assert (r23, r24) == (25, 22)
neu(3, 1, 3,
    "Eine Schule fragt jedes Jahr nach dem Schulweg. 2023 kamen "
    "$35\\,\\%$ mit dem Rad und $40\\,\\%$ mit dem Bus, der Rest zu Fuß. "
    "2024 stieg der Anteil Rad auf $42\\,\\%$, der Anteil Bus sank auf "
    "$36\\,\\%$, der Rest kam zu Fuß. Wie viel Prozent kamen in jedem "
    "Jahr zu Fuß?",
    "teil", "__, __",
    "2023: $100 - 35 - 40 = 25\\,\\%$; 2024: $100 - 42 - 36 = 22\\,\\%$",
    "[25, 22]", "S. 124 Nr. 13 – Anteile für ein Streifendiagramm aus "
    "einem Sachtext mit zwei Jahren entnehmen, Rest ergänzen")

# ===== Katalog: NEU-alle-kenngroessen, e4 k1 nach s7 (Ü1, Ü2 S. 117) ==
TX = ("alle Kenngrößen einer Liste in einer Aufgabe: sortieren, Umfang, "
      "Minimum, Maximum, Spannweite, Modalwert, Median, Mittelwert")
MK = ("eine Liste, alle Kenngrößen: erst die sortierte Liste notieren, "
      "dann jede Kenngröße daraus")
sp1 = [3.8, 4.2, 3.5, 4.0, 4.2, 3.9, 3.6, 4.4, 3.9, 4.2, 3.7]
m1 = sum(sp1) / len(sp1)
assert st.mode(sp1) == 4.2 and med(sp1) == 3.9 and round(m1, 2) == 3.95
assert round(max(sp1) - min(sp1), 1) == 0.9
neu(4, 1, "NEU-alle-kenngroessen",
    f"Elf Kinder springen weit, in m: {liste(sp1, '; ')}. Notiere zuerst "
    f"die sortierte Liste. Gib dann den Umfang $n$, das Minimum, das "
    f"Maximum, die Spannweite, den Modalwert, den Median und das "
    f"arithmetische Mittel an (auf zwei Stellen runden).",
    "text", "",
    "sortiert $3{,}5$; $3{,}6$; $3{,}7$; $3{,}8$; $3{,}9$; $3{,}9$; "
    "$4{,}0$; $4{,}2$; $4{,}2$; $4{,}2$; $4{,}4$; $n = 11$; Minimum "
    "$= 3{,}5$ m; Maximum $= 4{,}4$ m; Spannweite $= 0{,}9$ m; Modalwert "
    "$= 4{,}2$ m; Median $= 3{,}9$ m (der 6. Wert); Mittel $= 43{,}4 : 11 "
    "\\approx 3{,}95$ m",
    json.dumps([11, 3.5, 4.4, 0.9, 4.2, 3.9, round(m1, 2)]),
    "S. 117 Nr. 1 – zu einer Dezimalliste sortieren und alle Kenngrößen "
    "in einer Aufgabe angeben", neu_text=TX, neu_merkmal=MK)
to = [2, 0, 3, 1, 1, 4, 2, 0, 1, 2]
assert sorted(st.multimode(to)) == [1, 2] and med(to) == 1.5
assert sum(to) / len(to) == 1.6
neu(4, 1, "NEU-alle-kenngroessen",
    f"Ein Verein hat in zehn Spielen so viele Tore geschossen: "
    f"{liste(to)}. Notiere zuerst die sortierte Liste. Gib dann $n$, "
    f"Minimum, Maximum, Spannweite, Modalwert, Median und "
    f"arithmetisches Mittel an.",
    "text", "",
    "sortiert $0$, $0$, $1$, $1$, $1$, $2$, $2$, $2$, $3$, $4$; "
    "$n = 10$; Minimum $= 0$; Maximum $= 4$; Spannweite $= 4$; zwei "
    "Modalwerte: $1$ und $2$ (je dreimal); Median $= (1 + 2) : 2 = "
    "1{,}5$; Mittel $= 16 : 10 = 1{,}6$",
    json.dumps([10, 0, 4, 4, 1, 2, 1.5, 1.6]),
    "S. 117 Nr. 2 – alle Kenngrößen einer Liste, gerade Anzahl, zwei "
    "Modalwerte", neu_text=TX, neu_merkmal=MK)

# ===== Katalog: NEU-mittel-haeufigkeitstabelle, e4 k1 nach s8 (Ü4, Ü5)
TX = ("Mittelwert aus einer Häufigkeitstabelle (Notenspiegel): jeden "
      "Wert mal seine Anzahl, Summe durch die Gesamtzahl")
MK = ("die Werte kommen mit Anzahlen: Produkte addieren und durch die "
      "Gesamtzahl teilen, nicht durch die Zahl der Spalten")
an = {1: 4, 2: 6, 3: 7, 4: 5, 5: 2, 6: 1}
n_ = sum(an.values())
s_ = sum(k * v for k, v in an.items())
assert (n_, s_) == (25, 73) and Fr(s_, n_) == Fr(292, 100)
kopf = " & ".join(f"${k}$" for k in an)
anz = " & ".join(f"${v}$" for v in an.values())
neu(4, 1, "NEU-mittel-haeufigkeitstabelle",
    "Der Notenspiegel einer Klassenarbeit ist in der Tabelle. Berechne "
    "die Zahl der Schüler und den Notendurchschnitt.",
    "teil", "n = __, x̄ = __",
    "$n = 4 + 6 + 7 + 5 + 2 + 1 = 25$; $\\bar{x} = (1 \\cdot 4 + 2 \\cdot "
    "6 + 3 \\cdot 7 + 4 \\cdot 5 + 5 \\cdot 2 + 6 \\cdot 1) : 25 = 73 : 25 "
    "= 2{,}92$",
    "[25, 2.92]", "S. 118 Nr. 4 – Notendurchschnitt aus dem Notenspiegel",
    grafik="\\sachtabelle{lcccccc}{Note & " + kopf + "}{Anzahl & " + anz
    + "}", neu_text=TX, neu_merkmal=MK)
ge = {0: 5, 1: 9, 2: 4, 3: 1, 4: 1}
n_ = sum(ge.values())
s_ = sum(k * v for k, v in ge.items())
assert (n_, s_) == (20, 24)
kopf = " & ".join(f"${k}$" for k in ge)
anz = " & ".join(f"${v}$" for v in ge.values())
neu(4, 1, "NEU-mittel-haeufigkeitstabelle",
    "In einer Klasse wurde gefragt, wie viele Geschwister jedes Kind hat. "
    "Berechne, wie viele Geschwister ein Kind im Durchschnitt hat.",
    "teil", "",
    "$n = 5 + 9 + 4 + 1 + 1 = 20$ Kinder; Summe $= 0 \\cdot 5 + 1 \\cdot 9 "
    "+ 2 \\cdot 4 + 3 \\cdot 1 + 4 \\cdot 1 = 24$; $24 : 20 = 1{,}2$ "
    "Geschwister",
    "1.2", "S. 118 Nr. 5 – Mittelwert aus einer Häufigkeitstabelle "
    "(Werte mit Anzahlen)",
    grafik="\\sachtabelle{lccccc}{Geschwister & " + kopf + "}{Anzahl & "
    + anz + "}", neu_text=TX, neu_merkmal=MK)

# ===== Katalog: NEU-quartile-rangplatz, e5 k2 nach s5 (S. 119, Ü8) ====
TX = ("Quartile über den Rangplatz k = 0,25 · n bzw. 0,75 · n (zweite "
      "Methode) und mit der Halbierung vergleichen (Vorrat)")
MK = ("Rangplatz ausrechnen: ganzzahlig, dann Mittel aus k-tem und "
      "(k+1)-tem Wert; sonst aufrunden und den Wert ablesen")
l1 = [4, 5, 7, 8, 10, 11, 13, 14, 15, 17, 18, 20]
assert quart_rang(l1, 0.25) == 7.5 and quart_rang(l1, 0.75) == 16
neu(5, 2, "NEU-quartile-rangplatz",
    f"Die sortierte Liste lautet: {liste(l1)}. Bestimme das untere und "
    f"das obere Quartil über den Rangplatz: $k = 0{{,}}25 \\cdot n$ und "
    f"$k = 0{{,}}75 \\cdot n$.",
    "text", "q_u = __, q_o = __",
    "$n = 12$; $k = 0{,}25 \\cdot 12 = 3$ ganzzahlig: $q_u = (7 + 8) : 2 = "
    "7{,}5$; $k = 0{,}75 \\cdot 12 = 9$ ganzzahlig: $q_o = (15 + 17) : 2 "
    "= 16$",
    "[7.5, 16]", "S. 119 Wissen, S. 120 Nr. 8 – Quartile über den "
    "Rangplatz (zweite Methode)", neu_text=TX, neu_merkmal=MK)
l2 = [2, 4, 5, 8, 9, 11, 12, 15, 17]
r = [quart_rang(l2, .25), quart_rang(l2, .75)]
h = list(quart(l2))
assert r == [5, 12] and h == [4.5, 13.5]
neu(5, 2, "NEU-quartile-rangplatz",
    f"Die sortierte Liste lautet: {liste(l2)}. Bestimme beide Quartile "
    f"einmal über den Rangplatz ($k = 0{{,}}25 \\cdot n$, $k = 0{{,}}75 "
    f"\\cdot n$) und einmal als Median der unteren und der oberen Hälfte. "
    f"Vergleiche.",
    "text", "",
    "Rangplatz: $k = 2{,}25$, aufrunden auf $3$: $q_u = 5$; $k = 6{,}75$, "
    "aufrunden auf $7$: $q_o = 12$. Hälften ohne den Median $9$: unten "
    "$2$, $4$, $5$, $8$ → $q_u = 4{,}5$; oben $11$, $12$, $15$, $17$ → "
    "$q_o = 13{,}5$. Die beiden Methoden liefern hier leicht verschiedene "
    "Quartile.",
    json.dumps(r + h), "S. 119 Wissen „Beachte“ – beide Methoden der "
    "Quartilbestimmung vergleichen", neu_text=TX, neu_merkmal=MK)

# ===== Katalog: NEU-mittlere-abweichung, e4 k2 nach s1 (S. 120, Ü9, Ü14)
TX = ("mittlere Abweichung: Beträge der Abweichungen vom Mittelwert "
      "addieren, durch n teilen; Streuung zweier Gruppen damit "
      "vergleichen (nur Gymnasium)")
MK = ("Abstände zum Mittelwert ohne Vorzeichen addieren und durch die "
      "Anzahl teilen; gleiches Mittel, verschiedene Streuung")
A_ = [12, 15, 9, 14, 10]
B_ = [4, 20, 12, 18, 6]


def mabw(xs):
    mm = Fr(sum(xs), len(xs))
    return mm, sum(abs(v - mm) for v in xs) / len(xs)


(ma, aa), (mb, ab) = mabw(A_), mabw(B_)
assert (ma, aa, mb, ab) == (12, 2, 12, Fr(28, 5))
neu(4, 2, "NEU-mittlere-abweichung",
    f"Zwei Gruppen werfen Körbe. Gruppe A trifft {liste(A_)}-mal, Gruppe B "
    f"{liste(B_)}-mal. Berechne für jede Gruppe den Mittelwert und die "
    f"mittlere Abweichung (Summe der Abstände zum Mittelwert durch die "
    f"Anzahl). Welche Gruppe ist gleichmäßiger?",
    "text", "",
    "A: $\\bar{x} = 60 : 5 = 12$; Abstände $0$, $3$, $3$, $2$, $2$, Summe "
    "$10$; $a = 10 : 5 = 2$. B: $\\bar{x} = 60 : 5 = 12$; Abstände $8$, "
    "$8$, $0$, $6$, $6$, Summe $28$; $a = 28 : 5 = 5{,}6$. Gleiches "
    "Mittel, aber Gruppe A ist gleichmäßiger (kleinere mittlere "
    "Abweichung).",
    "[12, 2, 12, 5.6]", "S. 121 Nr. 9 – Mittelwert und mittlere "
    "Abweichung zweier Gruppen berechnen und vergleichen",
    neu_text=TX, neu_merkmal=MK)
neu(4, 2, "NEU-mittlere-abweichung",
    "Zwei Kurse haben in einer Arbeit beide den Notendurchschnitt "
    "$2{,}8$. Die mittlere Abweichung ist in Kurs A $0{,}4$ und in Kurs B "
    "$1{,}5$. In welchem Kurs gab es wohl eher sehr gute und sehr "
    "schlechte Noten? Begründe, ohne zu rechnen.",
    "text", "",
    "In Kurs B: Bei gleichem Mittelwert liegen die Noten dort im Schnitt "
    "weiter vom Mittelwert $2{,}8$ entfernt, also gibt es eher Einsen "
    "und Fünfen. In Kurs A liegen die meisten Noten nahe bei $2{,}8$.",
    "2.8", "S. 124 Nr. 14 – gleiches Mittel, verschiedene mittlere "
    "Abweichung deuten", neu_text=TX, neu_merkmal=MK)

# ===== Katalog: NEU-histogramm-waehlen, e1 k5 nach s1 (S. 122, Ü10b) ==
TX = ("Säulendiagramm der Einzelwerte oder Histogramm über Klassen "
      "wählen und begründen (Vorrat)")
MK = ("viele verschiedene Werte: Klassen und Histogramm; wenige Werte, "
      "die sich wiederholen: Säulen je Wert")
wz = [12, 47, 33, 8, 26, 51, 39, 18, 44, 29, 15, 36, 22, 57, 31, 41, 9,
      27, 35, 48]
hk = [sum(a <= v < a + 15 for v in wz) for a in (0, 15, 30, 45)]
assert hk == [3, 6, 7, 4] and len(set(wz)) == len(wz) == 20
neu(1, 5, "NEU-histogramm-waehlen",
    f"Die Wartezeiten von $20$ Kunden in s sind: {liste(wz)}. Begründe, "
    f"warum hier ein Histogramm besser passt als ein Säulendiagramm der "
    f"einzelnen Werte. Zeichne das Histogramm mit den Klassen $0$ bis "
    f"unter $15$, $15$ bis unter $30$, $30$ bis unter $45$, $45$ bis "
    f"unter $60$.",
    "zeichnen", "",
    "Jeder Wert kommt nur einmal vor; Säulen je Wert wären alle gleich "
    "hoch und zeigen nichts. Klassen: $3$, $6$, $7$, $4$ – lückenlose "
    "Säulen dieser Höhen über den Klassen",
    json.dumps(hk), "S. 123 Nr. 10 b – Säulendiagramm oder Histogramm "
    "wählen und begründen",
    grafik="\\histogramm[ymax=8,ystep=1,xstep=15]{0:15/, 15:30/, 30:45/, "
    "45:60/}", neu_text=TX, neu_merkmal=MK)
neu(1, 5, "NEU-histogramm-waehlen",
    "In einer Klasse wurde gezählt, wie viele Haustiere jedes Kind hat. "
    "Die Antworten sind nur $0$, $1$, $2$, $3$ oder $4$. Lina will die "
    "Antworten in Klassen einteilen und ein Histogramm zeichnen. Begründe, "
    "warum hier ein Säulendiagramm mit einer Säule je Anzahl besser passt.",
    "text", "",
    "Es gibt nur fünf verschiedene Werte, die sich oft wiederholen; jede "
    "Säule zeigt direkt, wie viele Kinder genau so viele Tiere haben. "
    "Klassen würden Werte zusammenwerfen und Information verschenken.",
    "", "S. 122 Wissen – Säulendiagramm für nicht klassierte Daten, "
    "Histogramm für Klassen", neu_text=TX, neu_merkmal=MK)

# ===== Katalog: NEU-streifen-vergleich, e3 k1 nach s2 (Ü13 c–e S. 124)
TX = ("zwei Streifendiagramme (zwei Jahre oder zwei Gruppen) "
      "untereinander zeichnen und vergleichen")
MK = ("gleich lange Streifen untereinander: Veränderung je Abschnitt in "
      "Prozentpunkten ablesen")
a23 = {"Rad": 30, "Bus": 50, "zu Fuß": 20}
a24 = {"Rad": 40, "Bus": 45, "zu Fuß": 15}
d = [a24[k] - a23[k] for k in a23]
assert sum(a23.values()) == sum(a24.values()) == 100 and d == [10, -5, -5]
neu(3, 1, "NEU-streifen-vergleich",
    "Schulweg einer Klasse: 2023 Rad $30\\,\\%$, Bus $50\\,\\%$, zu Fuß "
    "$20\\,\\%$; 2024 Rad $40\\,\\%$, Bus $45\\,\\%$, zu Fuß $15\\,\\%$. "
    "Stell dir beide Streifen gleich lang untereinander vor. Gib für "
    "Rad, Bus und zu Fuß an, um wie viele Prozentpunkte der Anteil "
    "gestiegen oder gesunken ist.",
    "text", "__, __, __",
    "$+10$; $-5$; $-5$ Prozentpunkte (Rad, Bus, zu Fuß)",
    "[10, -5, -5]", "S. 124 Nr. 13 c–e – zwei Streifendiagramme "
    "zeichnen und vergleichen", neu_text=TX, neu_merkmal=MK)

with open("neu-st-duden9.jsonl", "w", encoding="utf-8", newline="\n") as fh:
    for z in zeilen:
        fh.write(json.dumps(z, ensure_ascii=False) + "\n")
print(len(zeilen), "Zeilen")
for z in zeilen:
    print(z["id"])

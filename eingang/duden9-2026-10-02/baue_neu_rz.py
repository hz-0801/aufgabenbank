#!/usr/bin/env python3
"""Baut neu-rz-duden9.jsonl (Duden WÜT 9, Kap. 1) und rechnet jede
Lösung mit sympy nach. Vom Buch nur Typ und Form; Zahlen und Wortlaut
eigen. Kette, Sprossentext, Merkmal, Höhe, Quelle werden aus der
vorhandenen Bankzeile derselben Sprosse übernommen."""
import json
import sympy as sp

Q = "Duden WÜT Mathematik 9 (2017)"
R = sp.Rational
S = sp.sqrt
B = "aufgabenbank/bank/"
bank = {}
for e in ("reelle-zahlen", "potenzen-wurzeln"):
    for n in (1, 2, 3):
        for l in open(f"{B}{e}/e{n}.jsonl", encoding="utf-8"):
            r = json.loads(l)
            bank.setdefault((e, n, r["kette_nr"], r["sprosse"]), []).append(r)
zeilen = []
zaehl = {}


def neu(e, n, k, s, aufgabe, form, loesung, pruef, herkunft, grafik="",
        antwort="", neu_text=None, neu_merkmal=None, nach=None):
    if neu_text:                       # neue Sprosse (Vorschlag)
        vor = bank[(e, n, k, nach)][0]
        meta = dict(kette=vor["kette"], sprosse_text=neu_text,
                    merkmal=neu_merkmal, hoehe="sprosse",
                    quelle=vor["quelle"])
        start = 0
    else:
        alt = bank[(e, n, k, s)]
        meta = {f: alt[0][f] for f in
                ("kette", "sprosse_text", "merkmal", "hoehe", "quelle")}
        start = max(r["variante"] for r in alt)
        texte = {r["aufgabe"] for r in alt}
        assert aufgabe not in texte, ("Dublette", aufgabe)
    key = (e, n, k, s)
    zaehl[key] = zaehl.get(key, start) + 1
    v = zaehl[key]
    zeilen.append({
        "id": f"{e}-e{n}-k{k}-s{s}-v{v}", "eintrag": e, "einheit": n,
        "kette": meta["kette"], "kette_nr": k, "sprosse": s,
        "sprosse_text": meta["sprosse_text"], "merkmal": meta["merkmal"],
        "hoehe": meta["hoehe"], "variante": v, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": meta["quelle"],
        "herkunft": f"{Q}, {herkunft}"})


def gl(a, b):
    assert sp.simplify(sp.nsimplify(a) - sp.nsimplify(b)) == 0, (a, b)


RZ, PW = "reelle-zahlen", "potenzen-wurzeln"
x, y, a, b = sp.symbols("x y a b", positive=True)
KR = r" \\ \kreuz{rational} \\ \kreuz{irrational}"

# ---------- reelle-zahlen e1 ----------
H = "S. 7 Nr. 2 – gemischte Zahlenliste (Dezimal-, periodische Zahl, Wurzeln mit Minus, Wurzel aus null) als rational oder irrational ankreuzen"
for z, soll in [(-S(49), True), (S(0), True), (S(18), False), (R(27, 99), True), (-S(20), False)]:
    assert z.is_rational == soll
neu(RZ, 1, 1, 2,
    r"Kreuze für jede Zahl an, ob sie rational oder irrational ist: "
    r"$-\sqrt{49}$; $\sqrt{0}$; $\sqrt{18}$; $0{,}\overline{27}$; $-\sqrt{20}$."
    r"\\ \sachtabelle{lccccc}{ & $-\sqrt{49}$ & $\sqrt{0}$ & $\sqrt{18}$ & "
    r"$0{,}\overline{27}$ & $-\sqrt{20}$}{rational & & & & & \\ irrational & & & & & }",
    "ankreuzen",
    r"rational ($-7$); rational ($0$); irrational; rational (periodisch); irrational",
    "", H)
for z, soll in [(R(2718, 1000), True), (S(196), True), (-S(8), False), (R(3, 22), True), (S(1), True)]:
    assert z.is_rational == soll
assert sp.Rational(3, 22) == R(1, 10) + R(36, 990)          # 0,1(36)
neu(RZ, 1, 1, 2,
    r"Kreuze für jede Zahl an, ob sie rational oder irrational ist: "
    r"$2{,}718$; $\sqrt{196}$; $-\sqrt{8}$; $0{,}1\overline{36}$; $\sqrt{1}$."
    r"\\ \sachtabelle{lccccc}{ & $2{,}718$ & $\sqrt{196}$ & $-\sqrt{8}$ & "
    r"$0{,}1\overline{36}$ & $\sqrt{1}$}{rational & & & & & \\ irrational & & & & & }",
    "ankreuzen",
    r"rational (bricht ab); rational ($14$); irrational; rational (periodisch); rational ($1$)",
    "", H)

H = "S. 11 Nr. 11 – zwei Wurzeln malnehmen, Ergebnis wird rational"
gl(S(3) * S(27), 9)
neu(RZ, 1, 1, 8, r"Berechne $\sqrt{3} \cdot \sqrt{27}$ genau. Ist das Ergebnis rational oder irrational?",
    "teil", r"$\sqrt{3 \cdot 27} = \sqrt{81} = 9$ – rational", "9", H)

H = "S. 7 Nr. 3 und 5 – Einschachtelung von einem gegebenen Intervall aus fortsetzen, andere Wurzel"
assert R(244, 100)**2 == R(59536, 10000) and R(245, 100)**2 == R(60025, 10000)
assert R(244, 100) < S(6) < R(245, 100)
neu(RZ, 1, 1, 9,
    r"Du weißt schon: $2{,}4 < \sqrt{6} < 2{,}5$. Schachtle $\sqrt{6}$ weiter ein. "
    r"Fülle die Tabelle aus. Zwischen welchen zwei Hundertsteln liegt $\sqrt{6}$?",
    "tabelle", r"$5{,}9536$ und $6{,}0025$, also $2{,}44 < \sqrt{6} < 2{,}45$",
    "[5.9536, 6.0025]", H,
    grafik=r"\sachtabelle{cc}{$x$ & $x^2$}{$2{,}44$ & \\ $2{,}45$ & }")
vals = [R(33, 10)**2, R(34, 10)**2, R(331, 100)**2, R(332, 100)**2]
assert vals == [R(1089, 100), R(1156, 100), R(109561, 10000), R(110224, 10000)]
assert R(331, 100) < S(11) < R(332, 100)
neu(RZ, 1, 1, 9,
    r"Es gilt $3^2 = 9$ und $4^2 = 16$, also $3 < \sqrt{11} < 4$. Schachtle "
    r"$\sqrt{11}$ erst auf Zehntel, dann auf Hundertstel ein. Fülle die Tabelle aus.",
    "tabelle",
    r"$10{,}89$ und $11{,}56$, also $3{,}3 < \sqrt{11} < 3{,}4$; "
    r"$10{,}9561$ und $11{,}0224$, also $3{,}31 < \sqrt{11} < 3{,}32$",
    "[10.89, 11.56]", H,
    grafik=r"\sachtabelle{cc}{$x$ & $x^2$}{$3{,}3$ & \\ $3{,}4$ & \\ $3{,}31$ & \\ $3{,}32$ & }")

# ---------- reelle-zahlen e2 ----------
H = "S. 9 Nr. 8 – Potenzgesetz rückwärts: fehlenden Faktor in einer Lücke ergänzen"
gl(x**8 / x**3, x**5)
neu(RZ, 2, 1, 2, r"Ergänze die Lücke: $x^3 \cdot \square = x^8$.", "teil",
    r"$x^5$ (Exponent $5$)", "5", H)
gl(y**7 * y**2, y**9)
neu(RZ, 2, 1, 3, r"Ergänze die Lücke: $\square : y^2 = y^7$.", "teil",
    r"$9 - 2 = 7$, also $y^9$", "9", H)

H = "S. 9 Nr. 7 – gleicher Exponent mit Dezimalzahl als Basis, Produkt der Basen wird glatt"
gl(R(1, 2)**6 * 2**6, 1)
neu(RZ, 2, 1, 5, r"Berechne $0{,}5^6 \cdot 2^6$. Fasse zuerst die Basen zusammen.", "teil",
    r"$(0{,}5 \cdot 2)^6 = 1^6 = 1$", "1", H)
gl(R(5, 2)**4 * 4**4, 10000)
neu(RZ, 2, 1, 5, r"Berechne $2{,}5^4 \cdot 4^4$. Fasse zuerst die Basen zusammen.", "teil",
    r"$(2{,}5 \cdot 4)^4 = 10^4 = 10\,000$", "10**4", H)
H = "S. 9 Nr. 7 – gleicher Exponent beim Teilen, Quotient der Basen ist ein Bruch (Katalog: Bruchbasis)"
gl(R(4**3, 12**3), R(1, 27))
neu(RZ, 2, 1, 5, r"Berechne $4^3 : 12^3$. Fasse zuerst die Basen zusammen. Gib das Ergebnis als Bruch an.",
    "teil", r"$(4 : 12)^3 = \left(\frac{1}{3}\right)^3 = \frac{1}{27}$", "[1, 27]", H)

H = "S. 9 Nr. 7 – hoch null bei Dezimalzahl und negativer Basis im gemischten Term"
gl(sp.Float(7.25)**0 * (-sp.Float(1.9))**0 * 2**3, 8)
neu(RZ, 2, 1, 7, r"Berechne $7{,}25^0 \cdot (-1{,}9)^0 \cdot 2^3$.", "teil",
    r"$1 \cdot 1 \cdot 8 = 8$", "8", H)

H = "S. 9 Nr. 6 – Produkt mit negativen Faktoren und Potenz mit negativer Basis zusammenfassen"
X = sp.symbols("X")
gl(5 * X**2 * (-X)**3, -5 * X**5)
neu(RZ, 2, 1, 9, r"Vereinfache $5x^2 \cdot (-x)^3$.", "teil",
    r"$5x^2 \cdot (-x^3) = -5x^5$", "-5", H)
gl(-2 * X**3 * 3 * X * (-X**2), 6 * X**6)
neu(RZ, 2, 1, 9, r"Vereinfache $-2x^3 \cdot 3x \cdot (-x^2)$.", "teil",
    r"$(-2) \cdot 3 \cdot (-1) \cdot x^{3+1+2} = 6x^6$", "6", H)
A_, B_ = sp.symbols("A B")
gl(2 * A_ * B_ * A_ * A_ * B_, 2 * A_**3 * B_**2)
neu(RZ, 2, 1, 11, r"Schreibe kürzer mit Potenzen: $2 \cdot a \cdot b \cdot a \cdot a \cdot b$.", "teil",
    r"$2a^3b^2$", "2", "S. 9 Nr. 6 – ungeordnete Malkette mit zwei Variablen als Potenzen schreiben")
gl(-3 * A_ * 2 * A_ * B_ * (-4 * B_), 24 * A_**2 * B_**2)
neu(RZ, 2, 1, 11, r"Vereinfache $-3a \cdot 2ab \cdot (-4b)$.", "teil",
    r"$(-3) \cdot 2 \cdot (-4) \cdot a^2 b^2 = 24a^2b^2$", "24", H)

# ---------- reelle-zahlen e3 ----------
H = "S. 11 Nr. 11 – Quotient zweier Wurzeln als Wurzel aus dem Quotienten"
gl(S(98) / S(2), 7)
neu(RZ, 3, 1, 2, r"Berechne $\frac{\sqrt{98}}{\sqrt{2}}$.", "teil",
    r"$\sqrt{98 : 2} = \sqrt{49} = 7$", "7", H)
H = "S. 11 Wissen-Kasten „Wurzelterme“ (3) – teilweises Wurzelziehen mit Variable im Radikanden"
gl(S(18 * x), 3 * S(2 * x))
neu(RZ, 3, 1, 3, r"Ziehe aus $\sqrt{18x}$ teilweise die Wurzel ($x \geq 0$).", "teil",
    r"$\sqrt{9 \cdot 2x} = 3\sqrt{2x}$", "3", H)
H = "S. 11 Wissen-Kasten „Wurzelterme“ (1) – gleiche Wurzeln mit Variable zusammenfassen"
gl(3 * S(a) + 4 * S(a) - 2 * S(a), 5 * S(a))
neu(RZ, 3, 1, 4, r"Fasse zusammen: $3\sqrt{a} + 4\sqrt{a} - 2\sqrt{a}$ ($a \geq 0$).", "teil",
    r"$5\sqrt{a}$", "5", H)
H = "S. 11 Nr. 10 – Summe von Potenzen mit Stammbruch-Exponent in Wurzelschreibweise"
neu(RZ, 3, 1, 7, r"Schreibe in Wurzelschreibweise: $a^{\frac{1}{4}} + b^{\frac{1}{3}}$.", "teil",
    r"$\sqrt[4]{a} + \sqrt[3]{b}$", "4", H)

# NEU: Bruch-Exponent m/n <-> Wurzel (nach Sprosse 7)
NT = ("NEU-bruchexponent: Wurzel aus einer Potenz als Potenz mit Bruch-Exponent "
      "und zurück, auch negativer Bruch-Exponent und Summe als Basis "
      "(Vorschlag; nicht im Katalog; GYM)")
NM = "Zähler des Exponenten ist die Hochzahl, Nenner der Wurzelexponent"
H = "S. 11 Nr. 10 – Potenzschreibweise mit Bruch-Exponent und Wurzelschreibweise ineinander umformen"
gl(sp.root(5**2, 3), R(5)**R(2, 3))
neu(RZ, 3, 1, "NEU-bruchexponent", r"Schreibe als Potenz: $\sqrt[3]{5^2}$.", "teil",
    r"$5^{\frac{2}{3}}$", "5", H, neu_text=NT, neu_merkmal=NM, nach=7)
gl((a + b)**R(3, 4), sp.root((a + b)**3, 4))
neu(RZ, 3, 1, "NEU-bruchexponent", r"Schreibe als Wurzel: $(a + b)^{\frac{3}{4}}$.", "teil",
    r"$\sqrt[4]{(a + b)^3}$", "4", H, neu_text=NT, neu_merkmal=NM, nach=7)
gl(x**R(-1, 2), 1 / S(x))
neu(RZ, 3, 1, "NEU-bruchexponent", r"Schreibe als Bruch mit einer Wurzel: $x^{-\frac{1}{2}}$ ($x > 0$).",
    "teil", r"$\frac{1}{\sqrt{x}}$", "1", H, neu_text=NT, neu_merkmal=NM, nach=7)

H = "S. 11 Nr. 11 – Potenz einer n-ten Wurzel, Wurzel aus einer Wurzel, Produkt n-ter Wurzeln"
gl(sp.root(5, 3)**6, 25)
neu(RZ, 3, 1, 8, r"Berechne $\left(\sqrt[3]{5}\right)^6$.", "teil",
    r"$5^{\frac{6}{3}} = 5^2 = 25$", "25", H)
gl(S(S(81)), 3)
neu(RZ, 3, 1, 8, r"Berechne $\sqrt{\sqrt{81}}$.", "teil",
    r"$\sqrt[4]{81} = 81^{\frac{1}{4}} = 3$", "3", H)
gl(sp.root(2, 3) * sp.root(32, 3), 4)
neu(RZ, 3, 1, 8, r"Berechne $\sqrt[3]{2} \cdot \sqrt[3]{32}$.", "teil",
    r"$\sqrt[3]{2 \cdot 32} = \sqrt[3]{64} = 4$", "4", H)
gl((3 * a)**R(1, 2) * (12 * a**3)**R(1, 2), 6 * a**2)
neu(RZ, 3, 1, 8, r"Vereinfache $(3a)^{\frac{1}{2}} \cdot (12a^3)^{\frac{1}{2}}$ ($a \geq 0$).", "teil",
    r"$(36a^4)^{\frac{1}{2}} = 6a^2$", "6",
    "S. 9 Nr. 9 – gleicher Bruch-Exponent: Basen zusammenfassen, dann Wurzel ziehen")
gl(a / a**R(1, 3), a**R(2, 3))
neu(RZ, 3, 1, 8, r"Ergänze die Lücke: $a^{\frac{1}{3}} \cdot \square = a$.", "teil",
    r"$a^{\frac{2}{3}}$ (Exponent $\frac{2}{3}$)", "[2, 3]",
    "S. 9 Nr. 8 – Potenzgesetz mit Bruch-Exponenten rückwärts: Lücke ergänzen")

# NEU: Wurzelterme ausmultiplizieren (nach Sprosse 11)
NT = ("NEU-ausmultiplizieren: Wurzelterm mit dem Distributivgesetz oder einer "
      "binomischen Formel ausmultiplizieren (Vorschlag; nicht im Katalog; "
      "Vorrat, GYM)")
NM = "Wurzel mal Wurzel gibt den Radikanden; Rest bleibt als Wurzel stehen"
H = "S. 11 Nr. 13 und S. 9 Nr. 9 – Wurzelterme ausmultiplizieren, auch mit binomischer Formel"
gl(S(3) * (S(3) + 2), 3 + 2 * S(3))
neu(RZ, 3, 1, "NEU-ausmultiplizieren", r"Multipliziere aus: $\sqrt{3} \cdot (\sqrt{3} + 2)$.", "teil",
    r"$3 + 2\sqrt{3} \approx 6{,}46$", "3 + 2*3**0.5", H, neu_text=NT, neu_merkmal=NM, nach=11)
gl((S(5) + 1) * (S(5) - 1), 4)
neu(RZ, 3, 1, "NEU-ausmultiplizieren", r"Multipliziere aus: $(\sqrt{5} + 1)(\sqrt{5} - 1)$.", "teil",
    r"$(\sqrt{5})^2 - 1^2 = 5 - 1 = 4$", "4", H, neu_text=NT, neu_merkmal=NM, nach=11)
gl(sp.expand((S(x) + 3)**2), x + 6 * S(x) + 9)
neu(RZ, 3, 1, "NEU-ausmultiplizieren", r"Multipliziere aus: $(\sqrt{x} + 3)^2$ ($x \geq 0$).", "teil",
    r"$x + 6\sqrt{x} + 9$", "6", H, neu_text=NT, neu_merkmal=NM, nach=11)

# ---------- potenzen-wurzeln ----------
H = "S. 7 Nr. 1 – Quadrat einer negativen Dezimalzahl und einer kleinen Dezimalzahl"
gl(R(-3, 10)**2, R(9, 100)); gl(R(3, 100)**2, R(9, 10000))
neu(PW, 1, 3, 7, r"Berechne $(-0{,}3)^2$ und $0{,}03^2$.", "teil",
    r"$0{,}09$ und $0{,}0009$", "[0.09, 0.0009]", H)
H = "S. 7 Nr. 1 – Wurzel aus dem Quadrat einer negativen Dezimalzahl"
gl(S(R(-6, 10)**2), R(6, 10))
neu(PW, 3, 2, 7, r"Berechne $\sqrt{(-0{,}6)^2}$.", "teil",
    r"$(-0{,}6)^2 = 0{,}36$, $\sqrt{0{,}36} = 0{,}6$", "0.6", H)
H = "S. 11 Nr. 11 – Wurzel aus einer Dezimalzahl mit mehreren Nullen nach dem Komma"
gl(S(R(36, 10000)), R(6, 100))
neu(PW, 3, 2, 9, r"Berechne $\sqrt{0{,}0036}$.", "teil",
    r"$0{,}06$, denn $0{,}06 \cdot 0{,}06 = 0{,}0036$", "0.06", H)

with open("neu-rz-duden9.jsonl", "w", encoding="utf-8", newline="\n") as fh:
    for z in zeilen:
        fh.write(json.dumps(z, ensure_ascii=False) + "\n")
from collections import Counter
print(len(zeilen), "Zeilen, alle nachgerechnet")
for k, c in Counter((z["eintrag"][:2], z["einheit"], z["kette_nr"], z["sprosse"]) for z in zeilen).items():
    print(" ", k, c)

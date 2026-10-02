#!/usr/bin/env python3
"""Baut neu-pz-duden9.jsonl (prozentrechnung, zinsrechnung) aus Duden
WÜT 9, Kap. 9, und rechnet jede Lösung mit sympy nach. Vom Buch nur Typ
und Stufung; Zahlen und Wortlaut eigen. Vorlage: baue_neu_pyt.py."""
import json
import sympy as sp

Q = "Duden WÜT Mathematik 9 (2017)"
R = sp.Rational
B = "aufgabenbank/bank/"
zeilen, _bank, _zaehl = [], {}, {}


def bank(E, e):
    if (E, e) not in _bank:
        _bank[(E, e)] = [json.loads(l) for l in open(f"{B}{E}/e{e}.jsonl")]
    return _bank[(E, e)]


def neu(E, e, k, s, aufgabe, form, antwort, loesung, pruef, herkunft,
        grafik="", neu_text=None, neu_merkmal=None):
    if neu_text is None:
        g = [r for r in bank(E, e) if r["kette_nr"] == k and r["sprosse"] == s]
        assert g, (E, e, k, s)
        v, n = g[0], len(g)
        kette, st, mk, h, q = (v["kette"], v["sprosse_text"], v["merkmal"],
                               v["hoehe"], v["quelle"])
    else:
        v = next(r for r in bank(E, e) if r["kette_nr"] == k)
        kette, st, mk, h, q, n = (v["kette"], neu_text, neu_merkmal,
                                  "sprosse", v["quelle"], 0)
    key = (E, e, k, s)
    _zaehl[key] = _zaehl.get(key, n) + 1
    var = _zaehl[key]
    zeilen.append({
        "id": f"{E}-e{e}-k{k}-s{s}-v{var}", "eintrag": E, "einheit": e,
        "kette": kette, "kette_nr": k, "sprosse": s, "sprosse_text": st,
        "merkmal": mk, "hoehe": h, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": q, "herkunft": f"{Q}, {herkunft}"})


def eu(x, st=2):
    s = f"{float(x):,.{st}f}"
    return s.replace(",", "X").replace(".", "{,}").replace("X", "\\,")


def zt(x):  # Zahl ohne Nachkommanullen, deutsches Komma
    s = f"{float(x):.4f}".rstrip("0").rstrip(".")
    return s.replace(".", "{,}")


def tage(d1, m1, j1, d2, m2, j2):  # Bankmethode 30/360 wie Bank e1 k2 s3
    return (d2 - d1) + 30 * (m2 - m1) + 360 * (j2 - j1)


assert tage(11, 3, 0, 26, 5, 0) == 75 and tage(5, 6, 0, 25, 8, 0) == 80
P, Z = "prozentrechnung", "zinsrechnung"

# ===== P e1 NEU-umwandlungstabelle (A1) ================================
H = ("S. 111 Nr. 1 – Umwandlungstabelle gekürzter Bruch, Bruch mit Nenner "
     "100, Prozent, Dezimalbruch; Einstieg aus jeder Zeile")
NT = ("Umwandlungstabelle: gekürzter Bruch, Bruch mit Nenner hundert, "
      "Prozent und Dezimalzahl, Einstieg aus jeder Zeile (auch Prozent → "
      "gekürzter Bruch; Drittel und Sechstel nur gerundet)")
NM = "alle vier Darstellungen, gegeben ist je Spalte eine andere"
for spalten in (
        [("b", R(2, 5)), ("d", R(15, 100)), ("h", R(85, 100)),
         ("p", R(12, 100)), ("b", R(2, 3))],
        [("b", R(7, 20)), ("d", R(8, 100)), ("h", R(45, 100)),
         ("p", R(64, 100)), ("b", R(1, 6))]):
    zeil = {"b": [], "h": [], "p": [], "d": []}
    los = []
    for i, (art, w) in enumerate(spalten):
        g100 = (w * 100).is_integer
        txt = {"b": f"$\\frac{{{w.p}}}{{{w.q}}}$",
               "h": (f"$\\frac{{{int(w * 100)}}}{{100}}$" if g100
                     else "geht nicht genau"),
               "p": (f"${int(w * 100)}\\,\\%$" if g100
                     else f"$\\approx {zt(round(float(w) * 100, 1))}\\,\\%$"),
               "d": (f"${zt(w)}$" if g100
                     else f"$\\approx {zt(round(float(w), 3))}$")}
        for z in zeil:
            zeil[z].append(txt[z] if z == art else "")
        los.append(f"{chr(97 + i)}) " + "; ".join(
            txt[z] for z in ("b", "h", "p", "d") if z != art))
        assert sp.nsimplify(w) == w
    grafik = ("\\sachtabelle{lccccc}{ & a) & b) & c) & d) & e)}{"
              + "\\\\ ".join(f"{n} & " + " & ".join(zeil[z])
                             for n, z in (("gekürzter Bruch", "b"),
                                          ("Bruch mit Nenner 100", "h"),
                                          ("Prozent", "p"),
                                          ("Dezimalzahl", "d"))) + "}")
    neu(P, 1, 1, "NEU-umwandlungstabelle",
        "Fülle die Tabelle aus. In jeder Spalte steht dieselbe Zahl in "
        "vier Schreibweisen. Kürze die Brüche so weit wie möglich.",
        "tabelle", "", " · ".join(los),
        json.dumps([round(float(spalten[0][1]), 4), round(float(spalten[-1][1]) * 100, 1)]), H, grafik=grafik,
        neu_text=NT, neu_merkmal=NM)

# ===== P e3 k2 s1 Mehrwertsteuer (Bank) ================================
H = "S. 111 Nr. 2 – Mehrwertsteuer in Euro mit der Formel, Betrag nicht glatt"
for wer, g, p in (("Ein Malerbetrieb", 2485, 19), ("Ein Buchhändler", R(84630, 100), 7)):
    w = g * R(p, 100)
    neu(P, 3, 2, 1,
        f"{wer} stellt eine Rechnung über ${eu(g)}\\,€$ ohne "
        f"Mehrwertsteuer aus. Dazu kommen ${p}\\,\\%$ Mehrwertsteuer. Wie "
        "viel Euro Mehrwertsteuer fallen an? Runde auf Cent.", "teil",
        "__ €", f"$W = {eu(g)} \\cdot 0{{,}}{p:02d} \\approx {eu(w)}\\,€$",
        f"{float(g)}*{p}/100", H)

# ===== Z e1 k1 s0 Formeln übertragen (Bank) =============================
neu(Z, 1, 1, 0,
    "In der Prozentrechnung gilt $W = G \\cdot p\\,\\%$. Welche Formel "
    "gehört dazu in der Zinsrechnung? Kreuze an. Rechne nicht. \\\\ "
    "\\kreuz{$K = Z \\cdot p\\,\\%$} \\\\ \\kreuz{$Z = K \\cdot p\\,\\%$} "
    "\\\\ \\kreuz{$p\\,\\% = K \\cdot Z$}", "ankreuzen", "",
    "$Z = K \\cdot p\\,\\%$ (Zinsen = Prozentwert, Kapital = Grundwert)",
    "", "S. 111 Nr. 3 – Formeln der Prozentrechnung in die Zinsrechnung "
    "übertragen")

# ===== Z e1 k1 s6 Kapital rückwärts, Komma-Zinssatz (Bank) =============
H = "S. 112 Nr. 5 – Kapital aus Zinsen und Zinssatz mit Komma, zwei Konten vergleichen"
ka, kb = R(40) / R(25, 1000), R(448, 10) / R(32, 1000)
assert (ka, kb) == (1600, 1400)
neu(Z, 1, 1, 6,
    "Konto A bringt bei $2{,}5\\,\\%$ Zinsen nach einem Jahr $40{,}00\\,€$ "
    "Zinsen. Konto B bringt bei $3{,}2\\,\\%$ Zinsen nach einem Jahr "
    "$44{,}80\\,€$ Zinsen. Auf welchem Konto lag am Anfang mehr Geld?",
    "teil", "Konto __",
    "A: $40 : 0{,}025 = 1\\,600\\,€$; B: $44{,}80 : 0{,}032 = 1\\,400\\,€$; "
    "auf Konto A lag mehr, obwohl B mehr Zinsen bringt.",
    "[40/0.025, 44.8/0.032]", H)
k = R(3150, 100) / R(18, 1000)
assert k == 1750
neu(Z, 1, 1, 6,
    "Ein Sparkonto bringt bei $1{,}8\\,\\%$ Zinsen in einem Jahr "
    "$31{,}50\\,€$ Zinsen. Wie viel Euro lagen auf dem Konto?", "teil",
    "__ €", "$1\\,\\% = 31{,}50 : 1{,}8 = 17{,}50\\,€$; "
    "$K = 17{,}50 \\cdot 100 = 1\\,750\\,€$", "31.5/1.8*100", H)

# ===== Z e1 k2 s3 Laufzeit aus Daten, Jahreswechsel (Bank) ==============
H = "S. 112 Nr. 6 – Tageszinsen, Laufzeit aus zwei Daten, auch über den Jahreswechsel"
for kap, p, von, bis, vt, bt in (
        (4320, R(5, 2), (15, 11, 0), (10, 2, 1), "15. November",
         "10. Februar des nächsten Jahres"),
        (2880, 3, (3, 4, 0), (18, 9, 0), "3. April", "18. September")):
    t = tage(*von, *bis)
    zj = kap * p / 100
    zt_ = zj / 360 * t
    neu(Z, 1, 2, 3,
        f"Auf einem Konto liegen ${eu(kap, 0)}\\,€$ vom {vt} bis zum {bt}. "
        f"Die Bank zahlt ${zt(p)}\\,\\%$ Zinsen im Jahr. Rechne jeden Monat "
        "mit dreißig Tagen. Wie viel Euro Zinsen gibt es für diese Zeit?",
        "teil", "__ €",
        f"${eu(zt_)}\\,€$ ({t} Tage; Jahreszinsen ${eu(zj)}\\,€$, "
        f"${eu(zj)} : 360 \\cdot {t} = {eu(zt_)}$)",
        f"{kap}*{float(p)}/100/360*{t}", H)
    assert t == (85 if kap == 4320 else 165)

# ===== Z e1 k2 NEU-zinstabelle-gemischt (A3) ============================
H = ("S. 111 Nr. 4 – Zinstabelle mit gemischt fehlenden Größen, Laufzeit "
     "ein Jahr, Tage oder Monate")
NT = ("gemischte Zinstabelle: je Spalte erkennen, ob Kapital, Zinsen oder "
      "Zinssatz fehlt, Laufzeit ein Jahr, Monate oder Tage")
NM = "fehlende Größe wechselt von Spalte zu Spalte"
for sp_ in (
        [(2500, 60, None, "1 Jahr", 1), (9000, None, 2, "45 Tage", R(45, 360)),
         (None, 84, R(7, 2), "1 Jahr", 1), (1800, None, R(5, 2), "4 Monate", R(4, 12))],
        [(6400, None, R(3, 2), "1 Jahr", 1), (None, R(105, 2), R(21, 10), "1 Jahr", 1),
         (3600, None, R(5, 2), "72 Tage", R(72, 360)), (4800, 54, None, "9 Monate", R(9, 12))]):
    zeil = {"K": [], "Z": [], "p": [], "t": []}
    los, pr = [], []
    for i, (K, Zi, p, tt, f) in enumerate(sp_):
        K, Zi, p, f = [None if x is None else R(x) for x in (K, Zi, p, f)]
        if K is None:
            K_ = Zi / (p / 100 * f); los.append(f"{chr(97+i)}) $K = {eu(K_, 0)}\\,€$"); pr.append(K_)
        elif Zi is None:
            Z_ = K * p / 100 * f; los.append(f"{chr(97+i)}) $Z = {eu(Z_)}\\,€$"); pr.append(Z_)
        else:
            p_ = Zi / (K * f) * 100; los.append(f"{chr(97+i)}) $p = {zt(p_)}\\,\\%$"); pr.append(p_)
        zeil["K"].append(f"${eu(K, 0)}\\,€$" if K else "")
        zeil["Z"].append(f"${eu(Zi)}\\,€$" if Zi else "")
        zeil["p"].append(f"${zt(p)}\\,\\%$" if p else "")
        zeil["t"].append(tt)
    assert all(isinstance(x, sp.Rational) and (x * 100).is_integer for x in pr), pr
    grafik = ("\\sachtabelle{lcccc}{ & a) & b) & c) & d)}{" + "\\\\ ".join(
        f"{n} & " + " & ".join(zeil[z]) for n, z in (
            ("Kapital", "K"), ("Zinsen", "Z"), ("Zinssatz", "p"), ("Laufzeit", "t"))) + "}")
    neu(Z, 1, 2, "NEU-zinstabelle-gemischt",
        "Berechne die fehlenden Angaben. Rechne jeden Monat mit dreißig "
        "Tagen und das Jahr mit 360 Tagen.", "tabelle", "",
        " · ".join(los), json.dumps([float(x) for x in pr]), H,
        grafik=grafik, neu_text=NT, neu_merkmal=NM)

# ===== Z e2 k1 s6 Endkapital mit q^n, Komma-Zinssätze (Bank) ============
rows = [(5200, R(24, 10), 6), (8500, R(325, 100), 4), (2750, R(18, 10), 10)]
los, pr = [], []
for i, (k0, p, n) in enumerate(rows):
    q = 1 + p / 100
    kn = k0 * q ** n
    los.append(f"{chr(97+i)}) $q = {zt(q)}$, $K_{{{n}}} \\approx {eu(kn)}\\,€$")
    pr.append(round(float(kn), 2))
neu(Z, 2, 1, 6,
    "Berechne mit dem Taschenrechner den Zinsfaktor $q$ und das Kapital "
    "$K_n$ nach $n$ Jahren mit Zinseszins. Runde auf Cent.", "tabelle", "",
    " · ".join(los), json.dumps(pr),
    "S. 112 Nr. 7 – Tabelle K_0, p, n → q und K_n, Zinssätze mit Komma",
    grafik="\\sachtabelle{lrrrrr}{ & $K_0$ & $p\\,\\%$ & $n$ & $q$ & $K_n$}{"
    + "\\\\ ".join(f"{chr(97+i)}) & ${eu(k0, 0)}\\,€$ & ${zt(p)}\\,\\%$ & ${n}$ & & "
                   for i, (k0, p, n) in enumerate(rows)) + "}")
kn = 6300 * (1 + R(235, 10000)) ** 7
neu(Z, 2, 1, 6,
    "Frau Kaya legt $6\\,300\\,€$ für 7 Jahre zu $2{,}35\\,\\%$ mit "
    "Zinseszins an. Wie hoch ist das Guthaben am Ende? Runde auf Cent.",
    "teil", "__ €", f"≈ ${eu(kn)}\\,€$ ($6\\,300 \\cdot 1{{,}}0235^{{7}}$)",
    "6300*(1+2.35/100)**7", "S. 112 Nr. 8 – Endkapital nach n Jahren, Zinssatz mit zwei Dezimalen")

# pruef-Ausdrücke gegen die Lösungen gegenrechnen (wo Zahl)
for z in zeilen:
    if z["pruef"] and not z["pruef"].startswith("["):
        float(eval(z["pruef"]))
with open("neu-pz-duden9.jsonl", "w", encoding="utf-8", newline="\n") as fh:
    for z in zeilen:
        fh.write(json.dumps(z, ensure_ascii=False) + "\n")
from collections import Counter
print(len(zeilen), "Zeilen, nachgerechnet")
for kk, n in Counter((z["eintrag"], z["einheit"], z["kette_nr"], z["sprosse"]) for z in zeilen).items():
    print(kk, n)
for z in zeilen:
    print(z["id"], "|", z["loesung"][:150])

#!/usr/bin/env python3
"""Nachzug bank/bruchrechnung auf Katalog d78032a (29.09.2026).

Einmaliges Umbauskript (Auftrag auftrag-eintrag.md, Stand 29c).
Aufruf aus der Wurzel des Repos aufgabenbank:
    python3 werkzeuge/einmalig/nachzug-bruchrechnung-2026-09-29.py e1
schreibt bank/bruchrechnung/e1.jsonl neu (erster Wurf, eine Datei in
einem Schreibvorgang) und druckt die Zählung
übernommen/neu/umgeschrieben/entfallen. Liest den Bestand aus git
(HEAD vor dem Nachzug: 1e236dd), damit ein zweiter Lauf dasselbe
liefert.

Was geschieht (Katalog-Mappe mappen/bruchrechnung.md):
- quelle: Katalogzeilen 98–103 rücken auf 99–104.
- e1: neue Sprosse s5 „Hauptnenner und beide Erweiterungszahlen
  anschreiben“; s5–s6 rücken auf s6–s7; die Prüfungshöhe (s7 und
  „daneben“ s8) wird eine Sprosse s8 mit dem ganzen Text.
- e3: Erkennungsschritt „Von heißt mal“ entfällt (bank.md: wiederholt
  die Vorstufe „von“ markieren); Multiplizieren wird k1 mit neuer
  Sprosse s2 „Stammbruch von einem Bruch“; Dividieren wird k2 mit
  neuer Sprosse s2 „Kontrolle: Ergebnis mal Teiler“; Pflicht in einer
  Kette k3 „Multiplizieren“.
- e4, e5: Prüfungshöhe mit „daneben“ zu einer Sprosse.
- je Verfahrenskette Päckchen (fünf Grundfallzeilen), je Einheit
  Pflichtformen P1/P2 (fehler), P4/P6 (begruenden), P8 (anwendung).
"""
import copy
import json
import subprocess
import sys

E = "bruchrechnung"
BASIS = "1e236dd"
QMAP = {98: 99, 99: 100, 100: 101, 101: 102, 102: 103, 103: 104}


def mappe_zeilen():
    import re
    z = {}
    for l in open("mappen/bruchrechnung.md", encoding="utf-8"):
        m = re.match(r"\s*(\d+)  (.*)$", l.rstrip("\n"))
        if m:
            z[int(m.group(1))] = m.group(2)
    return z


ZEILEN = mappe_zeilen()


def pruefungstext(q):
    t = ZEILEN[q]
    return t[t.index("Prüfungshöhe:"):]


def lade(datei):
    txt = subprocess.run(["git", "show", f"{BASIS}:bank/{E}/{datei}.jsonl"],
                         capture_output=True, text=True, check=True).stdout
    return [json.loads(l) for l in txt.splitlines() if l.strip()]


def fr(z, n):
    return f"\\frac{{{z}}}{{{n}}}"


def mal(a, b):
    return f"{a} \\cdot {b}"


def dz(x):
    return str(x).replace(".", "{,}")


def rows(alt, k, s):
    return [copy.deepcopy(r) for r in alt if r["kette_nr"] == k and r["sprosse"] == s]


def neu(vorlage, **kw):
    r = copy.deepcopy(vorlage)
    r.pop("pflicht", None)
    r.update(kw)
    r["_art"] = "neu"
    return r


def um(r, **kw):
    r = copy.deepcopy(r)
    r.update(kw)
    r["_art"] = "um"
    return r


def ueber(r, **kw):
    r = copy.deepcopy(r)
    r.update(kw)
    r.setdefault("_art", "ueber")
    return r


def nummeriere(einheit, zeilen):
    """kette_nr, sprosse bleiben wie gesetzt; variante je Sprosse
    1..n; id und quelle nachziehen."""
    zaehl = {}
    for r in zeilen:
        key = (r["kette_nr"], r["sprosse"])
        zaehl[key] = zaehl.get(key, 0) + 1
        r["variante"] = zaehl[key]
        r["einheit"] = einheit
        r["id"] = f"{E}-e{einheit}-k{r['kette_nr']}-s{r['sprosse']}-v{r['variante']}"
        r["quelle"] = QMAP.get(r["quelle"], r["quelle"]) if not r.get("_q") else r["quelle"]
        r.pop("_q", None)
    return zeilen


MERK_FEHLER = "Rechnung prüfen: Fehler finden oder als richtig erkennen"
MERK_BEGR = "Behauptungen und Aussagen beurteilen, auch ohne Rechnung"
SERIE = "Welche Ergebnisse können nicht stimmen? Begründe, ohne genau zu rechnen."
AUSSAGEN = "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. Begründe."


def serie(einleitung, glieder):
    return einleitung + " " + SERIE + "".join(
        f" \\\\ ({i}) ${g}$" for i, g in enumerate(glieder, 1))


def aussagen(glieder):
    return AUSSAGEN + "".join(f" \\\\ ({i}) {g}" for i, g in enumerate(glieder, 1))


# ---------------------------------------------------------------- e1
def e1():
    alt = lade("e1")
    aus = []
    aus += [ueber(r) for r in rows(alt, 1, 0)]
    aus += [ueber(r) for r in rows(alt, 2, 0)]
    aus += [ueber(r) for r in rows(alt, 3, 0)]
    # Päckchen: 3/11 bleibt, Zähler des zweiten Bruchs wandert
    v = rows(alt, 3, 1)[0]
    m = ("gleiche Nenner: Zähler addieren, Nenner bleibt; der Summand "
         "3/11 bleibt, der Zähler des zweiten Bruchs wandert")
    for k in [1, 2, 4, 5, 7]:
        s = 3 + k
        aus.append(um(v, merkmal=m,
                      aufgabe=f"Berechne ${fr(3, 11)} + {fr(k, 11)}$.",
                      loesung=(f"Zähler addieren: $3 + {k} = {s}$; Nenner bleibt: $11$; "
                               f"Ergebnis: ${fr(3, 11)} + {fr(k, 11)} = {fr(s, 11)}$"),
                      pruef=f"[{s}, 11]"))
    aus += [ueber(r) for r in rows(alt, 3, 2)]
    aus += [ueber(r) for r in rows(alt, 3, 3)]
    aus += [ueber(r) for r in rows(alt, 3, 4)]
    # neue Sprosse s5
    st = ("Hauptnenner und beide Erweiterungszahlen anschreiben: zu zwei "
          "Nennern nur den Hauptnenner und die beiden Faktoren angeben, "
          "nichts addieren")
    assert st in ZEILEN[99]
    for (a, b), (c, d) in [((1, 6), (3, 8)), ((3, 4), (1, 10)), ((2, 9), (5, 6))]:
        import math
        hn = b * d // math.gcd(b, d)
        aus.append(neu(v, sprosse=5, sprosse_text=st, hoehe="sprosse", form="teil",
                       merkmal="nur Hauptnenner und beide Erweiterungszahlen angeben, nicht rechnen",
                       aufgabe=(f"Gegeben sind ${fr(a, b)}$ und ${fr(c, d)}$. Gib den "
                                "Hauptnenner an und die Zahl, mit der du jeden der beiden "
                                "Brüche erweitern musst. Rechne nicht weiter."),
                       antwort="Hauptnenner: __, erweitern mit __ und mit __",
                       loesung=(f"Hauptnenner: ${hn}$; Erweiterungszahl für ${fr(a, b)}$: "
                                f"${hn} : {b} = {hn // b}$; Erweiterungszahl für "
                                f"${fr(c, d)}$: ${hn} : {d} = {hn // d}$"),
                       pruef=f"[{hn}, {hn // b}, {hn // d}]", grafik="",
                       loesungsgrafik="", original=None, quelle=99, _q=True))
    for r in rows(alt, 3, 5):
        aus.append(ueber(r, sprosse=6))
    for r in rows(alt, 3, 6):
        aus.append(ueber(r, sprosse=7))
    # Prüfungshöhe: s7 und s8 zu s8
    pt = pruefungstext(99)
    pm = ("Prüfungshöhe: Pfadwahrscheinlichkeiten addieren oder Gegenereignis "
          "als Eins minus Bruch, Ergebnis gekürzt")
    for r in rows(alt, 3, 7) + rows(alt, 3, 8):
        aus.append(ueber(r, sprosse=8, sprosse_text=pt, merkmal=pm))
    aus += [ueber(r) for r in rows(alt, 4, 1)]
    # Pflicht k5
    f = rows(alt, 5, 1)
    f[0] = ueber(f[0], merkmal=MERK_FEHLER)
    f[1] = um(f[1], merkmal=MERK_FEHLER,
              aufgabe=(f"Ella soll ${fr(2, 3)} + {fr(1, 9)}$ ausrechnen. Sie rechnet so: "
                       f"${fr(2, 3)} + {fr(1, 9)} = {fr(6, 9)} + {fr(1, 9)} = {fr(7, 9)}$. "
                       "Prüfe, ob Ella richtig gerechnet hat."),
              loesung=(f"Richtig. Sie hat ${fr(2, 3)}$ mit $3$ erweitert, Zähler und "
                       "Nenner, und danach nur die Zähler addiert."),
              pruef="")
    f[2] = um(f[2], merkmal=MERK_FEHLER,
              aufgabe=serie("Lea hat Brüche addiert.",
                            [f"{fr(1, 3)} + {fr(1, 4)} = {fr(2, 7)}",
                             f"{fr(2, 5)} + {fr(1, 10)} = {fr(5, 10)}",
                             f"{fr(5, 8)} + {fr(1, 4)} = {fr(3, 8)}",
                             f"{fr(1, 6)} + {fr(1, 3)} = {fr(1, 2)}"]),
              loesung=(f"Nicht stimmen können (1) und (3). (1): ${fr(2, 7)}$ ist kleiner als "
                       f"${fr(1, 3)}$, eine Summe ist aber größer als jeder Summand. (3): "
                       f"${fr(3, 8)}$ ist kleiner als ${fr(5, 8)}$, auch hier wäre die Summe "
                       "kleiner als ein Summand."),
              pruef="")
    aus += f
    b = rows(alt, 5, 2)
    b[0] = ueber(b[0], merkmal=MERK_BEGR)
    b[1] = um(b[1], merkmal=MERK_BEGR,
              aufgabe=aussagen([
                  "Addiert man zwei Brüche mit gleichem Nenner, bleibt der Nenner immer gleich.",
                  "Die Summe zweier Brüche, die kleiner als $1$ sind, ist immer kleiner als $1$.",
                  "Es gibt zwei Brüche mit verschiedenen Nennern, deren Summe genau $1$ ist."]),
              loesung=("(1) wahr, denn man zählt nur gleich große Teile zusammen, ihre Größe "
                       f"ändert sich nicht. (2) falsch, z. B. ${fr(3, 4)} + {fr(3, 4)} = "
                       f"{fr(6, 4)} = 1{fr(1, 2)}$. (3) wahr, z. B. ${fr(1, 2)} + {fr(2, 4)} = 1$."),
              pruef="")
    b[2] = um(b[2], merkmal=MERK_BEGR,
              aufgabe=(f"Paul sagt: „${fr(3, 5)} + {fr(1, 4)} = {fr(4, 9)}$, man addiert oben "
                       "und unten.“ Begründe, ohne genau zu rechnen, ob Paul recht hat."),
              loesung=(f"Nein; ${fr(4, 9)}$ ist kleiner als ${fr(3, 5)}$, die Summe muss aber "
                       "größer sein als jeder Summand. Addieren darf man nur gleich große "
                       "Teile, also erst gleichnamig machen."),
              pruef="")
    aus += b
    a = rows(alt, 5, 3)
    a[0] = ueber(a[0])
    a[1] = um(a[1], loesung=(f"Ja; Rest berechnen: ${fr(6, 4)} - {fr(3, 4)} = {fr(3, 4)}$ Liter; "
                             f"drei Gläser: ${fr(1, 4)} + {fr(1, 4)} + {fr(1, 4)} = {fr(3, 4)}$ "
                             "Liter, das ist genau der Rest."))
    a[2] = ueber(a[2])
    aus += a
    aus += [ueber(r) for r in rows(alt, 5, 4)]
    return alt, nummeriere(1, aus)


# ---------------------------------------------------------------- e2
def e2():
    alt = lade("e2")
    aus = []
    aus += [ueber(r) for r in rows(alt, 1, 0)]
    v = rows(alt, 1, 1)[0]
    m = ("gleich viele Nachkommastellen, ohne Übertrag; der Summand 5,2 "
         "bleibt, der zweite Summand wandert")
    for x in ["1.3", "2.4", "3.7", "4.1", "0.6"]:
        e, z = x.split(".")
        s = round(5.2 + float(x), 1)
        aus.append(um(v, merkmal=m,
                      aufgabe=f"Berechne $5{{,}}2 + {dz(x)}$.",
                      loesung=(f"Komma unter Komma: $5{{,}}2 + {dz(x)}$; Zehntel addieren: "
                               f"$2 + {z} = {2 + int(z)}$; Einer addieren: $5 + {e} = {5 + int(e)}$; "
                               f"Ergebnis: $5{{,}}2 + {dz(x)} = {dz(s)}$"),
                      pruef=f"5.2+{x}"))
    for s in (2, 3, 4, 5):
        aus += [ueber(r) for r in rows(alt, 1, s)]
    aus += [ueber(r) for r in rows(alt, 2, 1)]
    aus += [ueber(r) for r in rows(alt, 3, 1)]
    f = rows(alt, 4, 1)
    f[0] = ueber(f[0], merkmal=MERK_FEHLER)
    f[1] = um(f[1], merkmal=MERK_FEHLER,
              aufgabe=("Mira soll $7{,}25 - 1{,}3$ ausrechnen. Sie rechnet so: "
                       "$7{,}25 - 1{,}30 = 5{,}95$. Prüfe, ob Mira richtig gerechnet hat."),
              loesung=("Richtig. Sie hat an $1{,}3$ eine Null angehängt; so stehen Zehntel "
                       "unter Zehnteln und Hundertstel unter Hundertsteln."),
              pruef="")
    f[2] = um(f[2], merkmal=MERK_FEHLER,
              aufgabe=serie("Jana hat Dezimalzahlen addiert und subtrahiert.",
                            ["6{,}4 + 0{,}35 = 0{,}99", "3{,}8 + 2{,}45 = 6{,}25",
                             "9{,}1 - 2{,}56 = 11{,}66", "5{,}07 + 1{,}6 = 6{,}67"]),
              loesung=("Nicht stimmen können (1) und (3). (1): Das Ergebnis ist kleiner als "
                       "$6{,}4$, beim Addieren wird es aber mehr. (3): Das Ergebnis ist größer "
                       "als $9{,}1$, beim Subtrahieren wird es aber weniger."),
              pruef="")
    aus += f
    b = rows(alt, 4, 2)
    b[0] = ueber(b[0], merkmal=MERK_BEGR)
    b[1] = um(b[1], merkmal=MERK_BEGR,
              aufgabe=aussagen([
                  "Hängt man an eine Dezimalzahl hinten nach dem Komma eine Null an, ändert sich ihr Wert nie.",
                  "Eine Dezimalzahl mit mehr Stellen nach dem Komma ist immer größer.",
                  "Es gibt zwei Dezimalzahlen mit je einer Stelle nach dem Komma, deren Summe eine ganze Zahl ist."]),
              loesung=("(1) wahr, denn null Hundertstel ändern nichts, z. B. $4{,}3 = 4{,}30$. "
                       "(2) falsch, z. B. ist $0{,}25$ kleiner als $0{,}3$. (3) wahr, z. B. "
                       "$1{,}4 + 2{,}6 = 4$."),
              pruef="")
    b[2] = um(b[2], merkmal=MERK_BEGR,
              aufgabe=("Tom sagt: „$20 + 0{,}4$ ist $2{,}4$.“ Begründe, ohne genau zu rechnen, "
                       "ob Tom recht hat."),
              loesung=("Nein; schon $20$ allein ist mehr als $2{,}4$, und es kommt noch etwas "
                       "dazu. Tom hat die Einer von $20$ nicht Komma unter Komma geschrieben."),
              pruef="")
    aus += b
    a = rows(alt, 4, 3)
    a[0] = ueber(a[0])
    a[1] = ueber(a[1])
    a[2] = um(a[2],
              aufgabe=("Beim Einkauf kosten Obst 4,67 €, Nudeln 1,29 €, Joghurt 2,45 € und "
                       "Saft 1,39 €. Du hast einen 10-€-Schein. Reicht er? Wenn ja, wie viel "
                       "Rückgeld bekommst du?"),
              loesung=("Ja; Summe: $4{,}67\\text{ €} + 1{,}29\\text{ €} + 2{,}45\\text{ €} + "
                       "1{,}39\\text{ €} = 9{,}80\\text{ €}$, das ist weniger als $10$ €; "
                       "Rückgeld: $10\\text{ €} - 9{,}80\\text{ €} = 0{,}20\\text{ €}$"),
              pruef="[4.67+1.29+2.45+1.39, 10-(4.67+1.29+2.45+1.39)]")
    aus += a
    return alt, nummeriere(2, aus)


# ---------------------------------------------------------------- e3
def e3():
    alt = lade("e3")
    aus = []
    # k1 (Erkennungsschritt „Von heißt mal“) entfällt
    for r in rows(alt, 2, 0):
        aus.append(ueber(r, kette_nr=1))
    v = rows(alt, 2, 1)[0]
    m = ("Bruch mal natürliche Zahl: Zähler mal Zahl, Nenner bleibt; der "
         "Bruch 2/13 bleibt, die Zahl wandert")
    for k in [2, 3, 4, 5, 6]:
        aus.append(um(v, kette_nr=1, merkmal=m,
                      aufgabe=f"Berechne ${fr(2, 13)} \\cdot {k}$.",
                      loesung=(f"Zähler mal Zahl: $2 \\cdot {k} = {2 * k}$; Nenner bleibt: $13$; "
                               f"Ergebnis: ${fr(2, 13)} \\cdot {k} = {fr(2 * k, 13)}$"),
                      pruef=f"[{2 * k}, 13]"))
    st = ("Stammbruch von einem Bruch: ein Fünftel von drei Viertel heißt "
          "drei Viertel in fünf gleiche Teile, Nenner mal fünf (Vorrat)")
    assert st in ZEILEN[102]
    for n, (z, d) in [(3, (2, 7)), (2, (3, 7)), (4, (5, 9))]:
        aus.append(neu(v, kette_nr=1, sprosse=2, sprosse_text=st, hoehe="sprosse",
                       form="teil",
                       merkmal="Stammbruch von einem Bruch: in gleiche Teile teilen, nur der Nenner wird malgenommen",
                       aufgabe=f"Berechne ${fr(1, n)}$ von ${fr(z, d)}$.",
                       antwort="",
                       loesung=(f"in {n} gleiche Teile teilen: Nenner mal {n}; rechnen: "
                                f"${fr(z, mal(d, n))} = {fr(z, d * n)}$; "
                                f"Ergebnis: ${fr(z, d * n)}$"),
                       pruef=f"[{z}, {d * n}]", grafik="", loesungsgrafik="",
                       original=None, quelle=102, _q=True))
    for s_alt, s_neu in [(2, 3), (3, 4), (4, 5)]:
        for r in rows(alt, 2, s_alt):
            aus.append(ueber(r, kette_nr=1, sprosse=s_neu))
    pt = pruefungstext(102)
    pm = "Prüfungshöhe: Brüche nach der Pfadregel multiplizieren, Ergebnis gekürzt"
    for r in rows(alt, 2, 5) + rows(alt, 2, 6):
        aus.append(ueber(r, kette_nr=1, sprosse=6, sprosse_text=pt, merkmal=pm))
    # k2 Dividieren
    v = rows(alt, 3, 1)[0]
    m = ("Bruch geteilt durch natürliche Zahl: Nenner mal Zahl; der Bruch "
         "3/5 bleibt, der Teiler wandert")
    for k in [2, 4, 5, 7, 8]:
        aus.append(um(v, kette_nr=2, merkmal=m,
                      aufgabe=f"Berechne ${fr(3, 5)} : {k}$.",
                      loesung=(f"Nenner mal Zahl: $5 \\cdot {k} = {5 * k}$; Zähler bleibt: $3$; "
                               f"Ergebnis: ${fr(3, 5)} : {k} = {fr(3, 5 * k)}$"),
                      pruef=f"[3, {5 * k}]"))
    st = "Kontrolle: Ergebnis mal Teiler gibt wieder die Ausgangszahl"
    assert st in ZEILEN[103]
    for (z, d), k in [((4, 9), 3), ((5, 8), 2), ((7, 10), 3)]:
        aus.append(neu(v, kette_nr=2, sprosse=2, sprosse_text=st, hoehe="sprosse",
                       form="teil",
                       merkmal="nach dem Teilen mit einer Malaufgabe kontrollieren",
                       aufgabe=(f"Berechne ${fr(z, d)} : {k}$. Kontrolliere dein Ergebnis "
                                "mit einer Malaufgabe."),
                       antwort="",
                       loesung=(f"Nenner mal {k}: ${fr(z, mal(d, k))} = {fr(z, d * k)}$; "
                                f"Kontrolle: Ergebnis mal Teiler $= {fr(z, d * k)} \\cdot {k} = "
                                f"{fr(z * k, d * k)} = {fr(z, d)}$, das ist die Ausgangszahl."),
                       pruef=f"[{z}, {d * k}]", grafik="", loesungsgrafik="",
                       original=None, quelle=103, _q=True))
    for s_alt, s_neu in [(2, 3), (3, 4), (4, 5), (5, 6)]:
        for r in rows(alt, 3, s_alt):
            aus.append(ueber(r, kette_nr=2, sprosse=s_neu))
    # Pflicht als eine Kette k3 „Multiplizieren“
    f = rows(alt, 4, 1) + rows(alt, 5, 1)
    st_f = f[0]["sprosse_text"]
    f[0] = ueber(f[0], kette_nr=3, merkmal=MERK_FEHLER)
    f[1] = um(f[1], kette_nr=3, merkmal=MERK_FEHLER,
              aufgabe=(f"Hanna soll ${fr(3, 4)} \\cdot {fr(2, 7)}$ ausrechnen. Sie rechnet so: "
                       f"${fr(3, 4)} \\cdot {fr(2, 7)} = {fr(6, 28)} = {fr(3, 14)}$. Prüfe, ob "
                       "Hanna richtig gerechnet hat."),
              loesung=("Richtig. Sie hat Zähler mal Zähler und Nenner mal Nenner gerechnet "
                       "und danach mit $2$ gekürzt."),
              pruef="")
    f[2] = um(f[2], kette_nr=3, sprosse=1, sprosse_text=st_f, merkmal=MERK_FEHLER,
              aufgabe=serie("Nora hat geteilt.",
                            [f"{fr(5, 8)} : 4 = {fr(5, 2)}", f"3 : {fr(1, 4)} = 12",
                             f"{fr(2, 3)} : 2 = {fr(1, 3)}", f"4 : {fr(1, 5)} = {fr(4, 5)}"]),
              loesung=(f"Nicht stimmen können (1) und (4). (1): ${fr(5, 2)}$ ist größer als "
                       f"${fr(5, 8)}$; teilt man durch $4$, wird es aber kleiner. (4): "
                       f"${fr(4, 5)}$ ist kleiner als $4$; teilt man durch einen Bruch kleiner "
                       "als $1$, wird es aber größer."),
              pruef="")
    aus += f
    b = rows(alt, 5, 2)
    b[0] = ueber(b[0], kette_nr=3, merkmal=MERK_BEGR)
    b[1] = um(b[1], kette_nr=3, merkmal=MERK_BEGR,
              aufgabe=(f"Mila sagt: „$6 : {fr(1, 3)}$ ist kleiner als $6$, denn Teilen macht "
                       "immer kleiner.“ Begründe, ohne genau zu rechnen, ob Mila recht hat."),
              loesung=(f"Nein; ${fr(1, 3)}$ passt in jedes Ganze dreimal, in $6$ also öfter "
                       "als sechsmal. Teilen durch einen Bruch kleiner als $1$ macht das "
                       "Ergebnis größer."),
              pruef="")
    b[2] = um(b[2], kette_nr=3, merkmal=MERK_BEGR,
              aufgabe=aussagen([
                  "Teilt man eine Zahl durch einen Bruch, wird das Ergebnis immer größer.",
                  f"Teilen durch ${fr(1, 4)}$ ist dasselbe wie malnehmen mit $4$.",
                  "Es gibt einen Bruch, mit dem man eine Zahl malnimmt und ein kleineres Ergebnis bekommt."]),
              loesung=(f"(1) falsch, z. B. $6 : {fr(3, 2)} = 6 \\cdot {fr(2, 3)} = 4$. (2) wahr, "
                       f"denn in jedes Ganze passen vier Viertel; der Kehrbruch von ${fr(1, 4)}$ "
                       f"ist $4$. (3) wahr, z. B. $8 \\cdot {fr(1, 2)} = 4$."),
              pruef="")
    aus += b
    a = rows(alt, 4, 2)
    a[0] = ueber(a[0], kette_nr=3, sprosse=3)
    a[1] = um(a[1], kette_nr=3, sprosse=3,
              aufgabe=(f"Ein Rezept braucht ${fr(3, 4)}$ kg Mehl. Du backst die doppelte Menge. "
                       f"Im Schrank steht eine Packung mit $1{fr(1, 2)}$ kg Mehl. Reicht das Mehl?"),
              loesung=(f"Ja; doppelte Menge: $2 \\cdot {fr(3, 4)} = {fr(6, 4)} = 1{fr(1, 2)}$ kg; "
                       "das ist genau die Packung."),
              pruef="[3, 2]")
    a[2] = ueber(a[2], kette_nr=3, sprosse=3)
    aus += a
    for r in rows(alt, 4, 3):
        aus.append(ueber(r, kette_nr=3, sprosse=4))
    return alt, nummeriere(3, aus)


# ---------------------------------------------------------------- e4
def e4():
    alt = lade("e4")
    aus = []
    aus += [ueber(r) for r in rows(alt, 1, 0)]
    v = rows(alt, 2, 1)[0]
    m = ("mal 10: Komma eine Stelle nach rechts; der Faktor 10 bleibt, die "
         "Dezimalzahl wandert")
    for x, erg in [("3.48", "34.8"), ("0.56", "5.6"), ("12.7", "127"),
                   ("0.093", "0.93"), ("7.05", "70.5")]:
        aus.append(um(v, merkmal=m,
                      aufgabe=f"Berechne ${dz(x)} \\cdot 10$.",
                      loesung=f"Komma eine Stelle nach rechts: ${dz(x)} \\cdot 10 = {dz(erg)}$",
                      pruef=f"{x}*10"))
    for s in range(2, 8):
        aus += [ueber(r) for r in rows(alt, 2, s)]
    pt = pruefungstext(103)
    pm = ("Prüfungshöhe: Menge mal Preis mit Wechsel zwischen Cent und Euro; "
          "daneben das Quadrat einer Dezimalzahl")
    for r in rows(alt, 2, 8) + rows(alt, 2, 9):
        aus.append(ueber(r, sprosse=8, sprosse_text=pt, merkmal=pm))
    f = rows(alt, 3, 1)
    f[0] = ueber(f[0], merkmal=MERK_FEHLER)
    f[1] = um(f[1], merkmal=MERK_FEHLER,
              aufgabe=("Leon soll $1{,}2 \\cdot 0{,}4$ ausrechnen. Er rechnet so: "
                       "$12 \\cdot 4 = 48$, zusammen zwei Kommastellen, also $0{,}48$. "
                       "Prüfe, ob Leon richtig gerechnet hat."),
              loesung=("Richtig. Beide Faktoren haben je eine Stelle nach dem Komma, das "
                       "Ergebnis hat zusammen zwei."),
              pruef="")
    f[2] = um(f[2], merkmal=MERK_FEHLER,
              aufgabe=serie("Aylin hat Dezimalzahlen multipliziert.",
                            ["0{,}6 \\cdot 0{,}7 = 4{,}2", "2{,}4 \\cdot 0{,}5 = 1{,}2",
                             "0{,}08 \\cdot 3 = 0{,}24", "0{,}9 \\cdot 0{,}2 = 1{,}8"]),
              loesung=("Nicht stimmen können (1) und (4). (1): Beide Faktoren sind kleiner "
                       "als $1$, also muss auch das Ergebnis kleiner als $1$ sein; es fehlt "
                       "eine Kommastelle. (4): Auch hier sind beide Faktoren kleiner als $1$, "
                       "$1{,}8$ ist aber größer als $1$."),
              pruef="")
    aus += f
    b = rows(alt, 3, 2)
    b[0] = ueber(b[0], merkmal=MERK_BEGR)
    b[1] = um(b[1], merkmal=MERK_BEGR,
              aufgabe=aussagen([
                  "Beim Teilen durch $100$ rückt das Komma immer zwei Stellen nach links.",
                  "Das Produkt zweier Dezimalzahlen ist immer größer als jeder der beiden Faktoren.",
                  "Es gibt zwei Dezimalzahlen mit je einer Stelle nach dem Komma, deren Produkt eine ganze Zahl ist."]),
              loesung=("(1) wahr, denn jede Ziffer ist danach nur noch ein Hundertstel so viel wert. (2) falsch, "
                       "z. B. ist $0{,}5 \\cdot 0{,}4 = 0{,}2$ kleiner als beide Faktoren. "
                       "(3) wahr, z. B. $2{,}5 \\cdot 0{,}4 = 1$."),
              pruef="")
    b[2] = um(b[2], merkmal=MERK_BEGR,
              aufgabe=("Jonas sagt: „$3{,}6 : 0{,}4$ ist dasselbe wie $3{,}6 : 4$.“ Begründe, "
                       "ohne genau zu rechnen, ob Jonas recht hat."),
              loesung=("Nein; $0{,}4$ ist zehnmal kleiner als $4$, passt also zehnmal so oft "
                       "in $3{,}6$. Verschiebt man das Komma beim Teiler, muss man es bei "
                       "$3{,}6$ genauso weit verschieben: $36 : 4$."),
              pruef="")
    aus += b
    a = rows(alt, 3, 3)
    a[0] = ueber(a[0])
    a[1] = um(a[1], loesung=("Nein; Seiten: $27 \\cdot 12 = 324$; Kosten: "
                             "$324 \\cdot 0{,}08\\text{ €} = 25{,}92\\text{ €}$, das ist mehr "
                             "als $25$ €."))
    a[2] = ueber(a[2])
    aus += a
    return alt, nummeriere(4, aus)


# ---------------------------------------------------------------- e5
def e5():
    alt = lade("e5")
    aus = []
    aus += [ueber(r) for r in rows(alt, 1, 0)]
    v = rows(alt, 1, 1)[0]
    m = ("erst mal, dann plus; 20 + 3 · … bleibt, der zweite Faktor wandert")
    for k in [2, 4, 5, 7, 9]:
        aus.append(um(v, merkmal=m,
                      aufgabe=f"Berechne $20 + 3 \\cdot {k}$.",
                      loesung=(f"Punkt zuerst: $3 \\cdot {k} = {3 * k}$; dann Strich: "
                               f"$20 + {3 * k} = {20 + 3 * k}$; Ergebnis: ${20 + 3 * k}$"),
                      pruef=f"20+3*{k}"))
    for s in range(2, 6):
        aus += [ueber(r) for r in rows(alt, 1, s)]
    pt = pruefungstext(104)
    pm = ("Prüfungshöhe: Bruchterm mit Klammer auswerten; daneben Terme zu "
          "einem Sachtext prüfen")
    for r in rows(alt, 1, 6):
        aus.append(ueber(r, sprosse=6, sprosse_text=pt, merkmal=pm))
    t = rows(alt, 1, 7)
    aus.append(um(t[0], sprosse=6, sprosse_text=pt, merkmal=pm,
                  loesung=("Ja, nein, ja. Erster Term richtig; zweiter Term falsch, die Oma "
                           "ist wie ein Kind gerechnet; dritter Term richtig.")))
    aus.append(um(t[1], sprosse=6, sprosse_text=pt, merkmal=pm,
                  loesung=("Nein, ja, ja. Erster Term falsch, der Opa ist wie ein Kind "
                           "gerechnet; zweiter und dritter Term richtig.")))
    aus += [ueber(r) for r in rows(alt, 2, 1)]
    aus += [ueber(r) for r in rows(alt, 3, 1)]
    f = rows(alt, 4, 1)
    f[0] = ueber(f[0], merkmal=MERK_FEHLER)
    f[1] = um(f[1], merkmal=MERK_FEHLER,
              aufgabe=(f"Eva soll ${fr(2, 5)} + {fr(1, 5)} \\cdot 3$ ausrechnen. Sie rechnet "
                       f"so: ${fr(2, 5)} + {fr(3, 5)} = 1$. Prüfe, ob Eva richtig gerechnet hat."),
              loesung=(f"Richtig. Sie hat zuerst malgenommen, ${fr(1, 5)} \\cdot 3 = {fr(3, 5)}$, "
                       "und danach addiert: Punkt vor Strich."),
              pruef="")
    f[2] = um(f[2], merkmal=MERK_FEHLER,
              aufgabe=serie("Leo hat gerechnet.",
                            ["4 + 6 \\cdot 5 = 50", "20 - 12 : 4 = 17",
                             "3 \\cdot 4 + 2 \\cdot 5 = 70", "18 - 2 \\cdot 3 = 12"]),
              loesung=("Nicht stimmen können (1) und (3). (1): $6 \\cdot 5$ endet auf $0$, "
                       "mit $4$ dazu muss das Ergebnis auf $4$ enden, nicht auf $0$. (3): "
                       "$3 \\cdot 4$ und $2 \\cdot 5$ sind beide kleiner als $15$, die Summe "
                       "ist also kleiner als $30$."),
              pruef="")
    aus += f
    b = rows(alt, 4, 2)
    b[0] = ueber(b[0], merkmal=MERK_BEGR)
    b[1] = um(b[1], merkmal=MERK_BEGR,
              aufgabe=aussagen([
                  "Eine Klammer um eine Malaufgabe in einer Summe ändert das Ergebnis nie.",
                  "Man rechnet immer von links nach rechts.",
                  "Es gibt Terme, bei denen eine Klammer das Ergebnis ändert."]),
              loesung=("(1) wahr, denn Punkt vor Strich rechnet die Malaufgabe ohnehin "
                       "zuerst, z. B. $(2 \\cdot 3) + 4 = 2 \\cdot 3 + 4$. (2) falsch, z. B. "
                       "ist $2 + 3 \\cdot 4 = 14$, von links nach rechts käme $20$ heraus. "
                       "(3) wahr, z. B. $(2 + 3) \\cdot 4 = 20$, aber $2 + 3 \\cdot 4 = 14$."),
              pruef="")
    b[2] = um(b[2], merkmal=MERK_BEGR,
              aufgabe=("Mia sagt: „Bei $10 - 4 : 2$ rechnet man zuerst $10 - 4$, weil es "
                       "vorne steht.“ Begründe, ohne genau zu rechnen, ob Mia recht hat."),
              loesung=("Nein; Punkt vor Strich: Die Division $4 : 2$ kommt zuerst, auch "
                       "wenn sie hinten steht."),
              pruef="")
    aus += b
    a = rows(alt, 4, 3)
    a[0] = um(a[0], loesung=("Nein; Hefte und Stifte: $3 \\cdot 1{,}20\\text{ €} + 2 \\cdot "
                             "0{,}85\\text{ €} = 3{,}60\\text{ €} + 1{,}70\\text{ €} = "
                             "5{,}30\\text{ €}$, das ist mehr als $5$ €."))
    a[1] = ueber(a[1])
    a[2] = ueber(a[2])
    aus += a
    return alt, nummeriere(5, aus)


def main():
    teil = sys.argv[1]
    alt, aus = {"e1": e1, "e2": e2, "e3": e3, "e4": e4, "e5": e5}[teil]()
    z = {"ueber": 0, "neu": 0, "um": 0}
    for r in aus:
        z[r.pop("_art")] += 1
    entfallen = len(alt) - z["ueber"] - z["um"]
    reihen = [json.dumps(r, ensure_ascii=False) for r in aus]
    with open(f"bank/{E}/{teil}.jsonl", "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(reihen) + "\n")
    print(f"{teil}: {len(aus)} Zeilen; übernommen {z['ueber']}, neu {z['neu']}, "
          f"umgeschrieben {z['um']}, entfallen {entfallen}")


if __name__ == "__main__":
    main()

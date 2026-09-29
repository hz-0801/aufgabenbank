"""Nachzug bank/flaecheninhalt-durch-integration auf Katalog 2a296e5.

Einmalig, 2026-09-29 (Mappe Schub 3). Liest den Bestand vom 27.09.,
zieht quelle (106–110 -> 102–106), sprosse, id und sprosse_text nach,
schreibt die Päckchen (je Verfahrenskette 5), die neue Sprosse e5 s3
(Wert und Fläche nebeneinander), die fehlenden Originale der
e5-Prüfungssprosse und die Pflichtformen P1–P8 und schreibt je
Einheit die ganze Datei neu. Zählt je Einheit übernommen/neu/
umgeschrieben/entfallen (Ausgabe am Ende).
Aufruf aus der Wurzel des Repos: python3 werkzeuge/einmalig/<datei>
"""
import copy
import json
import re
from pathlib import Path

E = "flaecheninhalt-durch-integration"
B = Path("bank") / E
MAPPE = Path("mappen") / f"{E}.md"
QMAP = {106: 102, 107: 103, 108: 104, 109: 105, 110: 106}
FELDER = ["id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
          "sprosse_text", "merkmal", "hoehe", "pflicht", "variante",
          "aufgabe", "form", "antwort", "loesung", "pruef", "original",
          "grafik", "loesungsgrafik", "quelle"]

M_FEHLER = ("Rechnung prüfen: Fehler finden, richtige Rechnung erkennen, "
            "unmögliche Ergebnisse erkennen")
M_BEGR = ("begründen: Regel beim Namen, Aussagen beurteilen, "
          "Behauptung beurteilen")


def katalog():
    kat = {}
    for z in MAPPE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*(\d+)  (.*)$", z)
        if m and int(m.group(1)) not in kat:
            kat[int(m.group(1))] = m.group(2)
    return kat


KAT = katalog()


def segmente(q):
    return KAT[q].split(": ", 1)[1].split(" → ")


def vorstufe_text(q):
    s = segmente(q)[0]
    i = s.find("nichts rechnen")
    return s[:i + len("nichts rechnen")] if i >= 0 else s


def pruef_text(q):
    return segmente(q)[-1].rstrip(".")


def lade(n):
    return [json.loads(z) for z in
            (B / f"e{n}.jsonl").read_text(encoding="utf-8").splitlines()]


def zeile(vorlage, **kw):
    a = copy.deepcopy(vorlage)
    a.update(kw)
    if a["hoehe"] != "pflicht":
        a.pop("pflicht", None)
    return a


def schreibe(n, zeilen):
    aus = []
    for a in zeilen:
        a["quelle"] = QMAP.get(a["quelle"], a["quelle"])
        a["id"] = (f"{E}-e{n}-k{a['kette_nr']}-s{a['sprosse']}"
                   f"-v{a['variante']}")
        aus.append({f: a[f] for f in FELDER if f in a})
    (B / f"e{n}.jsonl").write_text(
        "".join(json.dumps(a, ensure_ascii=False) + "\n" for a in aus),
        encoding="utf-8")
    return aus


def zaehle(n, alt, neu, neue_ids):
    """alt: Bestand; neu: Endstand; neue_ids: ids (Endstand) neuer
    Zeilen. Übernommen = aufgabe, loesung, merkmal wortgleich."""
    altkey = {(a["aufgabe"], a["loesung"], a["merkmal"]) for a in alt}
    ueb = um = nn = 0
    for a in neu:
        if a["id"] in neue_ids:
            nn += 1
        elif (a["aufgabe"], a["loesung"], a["merkmal"]) in altkey:
            ueb += 1
        else:
            um += 1
    ent = len(alt) - (ueb + um)
    print(f"e{n}: übernommen {ueb}, neu {nn}, umgeschrieben {um}, "
          f"entfallen {ent}, Zeilen {len(neu)}")


def ersetze(zeilen, k, s, neue):
    """Ersetzt die Gruppe (kette_nr k, sprosse s) durch neue Zeilen."""
    i = [j for j, a in enumerate(zeilen)
         if a["kette_nr"] == k and a["sprosse"] == s]
    vorlage = zeilen[i[0]]
    rows = [zeile(vorlage, variante=v + 1, **d) for v, d in
            enumerate(neue)]
    return zeilen[:i[0]] + rows + zeilen[i[-1] + 1:]


def setze(zeilen, k, s, v, **kw):
    for a in zeilen:
        if a["kette_nr"] == k and a["sprosse"] == s and a["variante"] == v:
            a.update(kw)
            return
    raise KeyError((k, s, v))


def merkmal(zeilen, k, s, text):
    for a in zeilen:
        if a["kette_nr"] == k and a["sprosse"] == s:
            a["merkmal"] = text


def texte(zeilen, q, vorstufe_neu=True):
    for a in zeilen:
        qq = QMAP.get(a["quelle"], a["quelle"])
        if a["hoehe"] == "vorstufe" and vorstufe_neu:
            a["sprosse_text"] = vorstufe_text(qq)
        if a["hoehe"] == "pruefung":
            a["sprosse_text"] = pruef_text(qq)


def zahl(x):
    s = f"{x:g}".replace(".", "{,}")
    return s


# ---------------------------------------------------------------- e1

def e1():
    alt = lade(1)
    z = copy.deepcopy(alt)
    texte(z, 102)
    pack = []
    for r in (1, 2, 3, 4, 5):
        c = 3 * r * r
        fr = r ** 3 - c * r
        pack.append(dict(
            merkmal=("Nullstellen als Grenzen, Integral negativ, Betrag als "
                     "eigene Zeile; der Faktor 3 vor x² bleibt, die Zahl "
                     "dahinter wandert"),
            aufgabe=(f"Der Graph von $f(x) = 3x^2 - {c}$ schließt mit der "
                     f"x-Achse eine Fläche ein. Berechne ihren Inhalt."),
            form="teil", antwort="",
            loesung=(f"Nullstellen: $3x^2 - {c} = 0$, $x = -{r}$ oder "
                     f"$x = {r}$; Grenzen: $-{r}$ und ${r}$; Stammfunktion: "
                     f"$F(x) = x^3 - {c}x$; Integral: $F({r}) - F(-{r}) = "
                     f"{fr} - {-fr} = {2 * fr}$; Betrag: $A = |{2 * fr}| = "
                     f"{-2 * fr}$"),
            pruef=str(-2 * fr), grafik="", loesungsgrafik=""))
    z = ersetze(z, 1, 1, pack)
    # Pflicht fehler
    merkmal(z, 2, 1, M_FEHLER)
    setze(z, 2, 1, 2,
          aufgabe=(r"Mia soll die Fläche berechnen, die der Graph von "
                   r"$f(x) = 2x^3 - 8x$ mit der x-Achse einschließt. Sie "
                   r"rechnet so: \rechnung{\text{Nullstellen: } & -2,\ 0,\ 2 "
                   r"\\ F(x) &= \tfrac{1}{2}x^4 - 4x^2 \\ F(2) - F(0) &= 8 - "
                   r"16 = -8 \\ A &= 2 \cdot |-8| = 16} Prüfe, ob Mia richtig "
                   r"gerechnet hat."),
          loesung=("Richtig. Sie trennt an der Nullstelle $0$, nimmt den "
                   "Betrag des Teilstücks und verdoppelt wegen der "
                   "Punktsymmetrie zum Ursprung."),
          pruef="")
    setze(z, 2, 1, 3,
          aufgabe=(r"Lena hat Flächen zwischen Graph und x-Achse berechnet. "
                   r"Welche Ergebnisse können nicht stimmen? Begründe, ohne "
                   r"genau zu rechnen. \\ (1) $f(x) = x^2 - 9$ zwischen den "
                   r"Nullstellen: $A = -36$ \\ (2) $f(x) = 4 - x^2$ zwischen "
                   r"den Nullstellen: $A = \frac{32}{3}$ \\ (3) $f(x) = x^3$ "
                   r"von $-1$ bis $1$: $A = 0$ \\ (4) $f(x) = x^2 + 1$ von "
                   r"$0$ bis $3$: $A = 2$"),
          loesung=("Nicht stimmen können (1), (3) und (4). (1): Ein "
                   "Flächeninhalt ist nie negativ. (3): Links und rechts "
                   "von $0$ liegt je ein Flächenstück, der Inhalt kann nicht "
                   "null sein. (4): Der Graph liegt überall mindestens bei "
                   "$1$, die Fläche ist also mindestens $1 \\cdot 3 = 3$. "
                   "(2) kann stimmen."),
          pruef="")
    # Pflicht begruenden
    merkmal(z, 2, 2, M_BEGR)
    setze(z, 2, 2, 2,
          aufgabe=(r"Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   r"ist. Begründe. \\ (1) Das Integral einer Funktion über "
                   r"einem Intervall ist immer der Inhalt der Fläche zwischen "
                   r"Graph und x-Achse. \\ (2) Liegt der Graph auf einem "
                   r"Intervall ganz oberhalb der x-Achse, ist das Integral "
                   r"dort gleich dem Flächeninhalt. \\ (3) Es gibt "
                   r"Funktionen, deren Integral von $-1$ bis $1$ null ist, "
                   r"obwohl der Graph mit der x-Achse Flächen einschließt."),
          loesung=("(1) falsch, z. B. $f(x) = x - 2$ von $0$ bis $1$: "
                   "Integral $-1{,}5$, Fläche $1{,}5$. (2) wahr, denn dort "
                   "sind alle Funktionswerte positiv, das Integral zählt "
                   "nichts negativ. (3) wahr, denn z. B. bei $f(x) = x$ "
                   "heben sich die Stücke links und rechts von $0$ auf "
                   "(orientierter Flächeninhalt)."),
          pruef="")
    setze(z, 2, 2, 3,
          aufgabe=(r"Tim sagt: „Das Integral von $-2$ bis $2$ über $x^3$ ist "
                   r"null, also schließt der Graph von $f(x) = x^3$ dort "
                   r"keine Fläche mit der x-Achse ein.“ Begründe, ob Tim "
                   r"recht hat. Begründe, ohne genau zu rechnen."),
          loesung=("Nein; die Stücke links und rechts von $0$ sind gleich "
                   "groß und liegen auf verschiedenen Seiten der x-Achse – "
                   "im Integral heben sie sich auf, der Flächeninhalt ist "
                   "aber positiv (Integralwert ist nicht Flächeninhalt)."),
          pruef="")
    # anwendung P8: Urteil zuerst
    setze(z, 2, 3, 3,
          loesung=("Ja; Nullstellen: $0$ und $4$; Integral: "
                   "$\\left[\\frac{1}{12}x^3 - \\frac{1}{2}x^2\\right]_0^4 = "
                   "-\\frac{8}{3}$; Betrag: $A = \\frac{8}{3} \\approx "
                   "2{,}67\\,\\text{m}^2$; Vergleich: $2{,}67\\,\\text{m}^2 > "
                   "2{,}5\\,\\text{m}^2$, das Rohr passt der Fläche nach."))
    neu = schreibe(1, z)
    zaehle(1, alt, neu, set())


# ---------------------------------------------------------------- e2

def e2():
    alt = lade(2)
    z = copy.deepcopy(alt)
    texte(z, 103)
    pack = []
    for b in (1, 2, 3, 4, 5):
        d = b ** 3 + b ** 2 + 2 * b
        pack.append(dict(
            merkmal=("Differenzfunktion über gegebenem Intervall; beide "
                     "Funktionen bleiben, die obere Grenze wandert"),
            aufgabe=(f"Gegeben sind $f(x) = 3x^2 + 2$ und $g(x) = -2x$. "
                     f"Berechne den Inhalt der Fläche zwischen den beiden "
                     f"Graphen von $x = 0$ bis $x = {b}$."),
            form="teil", antwort="",
            loesung=(f"Differenz: $f(x) - g(x) = 3x^2 + 2x + 2$; Lage: "
                     f"$3x^2 + 2x + 2 > 0$ für alle $x$, $f$ liegt oben; "
                     f"Stammfunktion: $D(x) = x^3 + x^2 + 2x$; Integral: "
                     f"$D({b}) - D(0) = {d} - 0 = {d}$; Ergebnis: "
                     f"$A = {d}$"),
            pruef=str(d), grafik="", loesungsgrafik=""))
    z = ersetze(z, 1, 1, pack)
    merkmal(z, 2, 1, M_FEHLER)
    setze(z, 2, 1, 2,
          aufgabe=(r"Ben soll die Fläche zwischen den Graphen von "
                   r"$f(x) = 7 - x^2$ und $g(x) = -2$ berechnen. Er rechnet "
                   r"so: \rechnung{7 - x^2 &= -2 \\ x &= -3 \text{ oder } "
                   r"x = 3 \\ f(x) - g(x) &= 9 - x^2 \\ A &= \left[9x - "
                   r"\tfrac{1}{3}x^3\right]_{-3}^{3} = 18 + 18 = 36} Prüfe, "
                   r"ob Ben richtig gerechnet hat."),
          loesung=("Richtig. Die Differenz obere minus untere Funktion ist "
                   "der senkrechte Abstand, die Schnittstellen sind die "
                   "Grenzen, und weil $f$ dazwischen oben liegt, ist der "
                   "Wert schon der Inhalt."),
          pruef="")
    setze(z, 2, 1, 3,
          aufgabe=(r"Jonas hat Flächen zwischen zwei Graphen berechnet. "
                   r"Welche Ergebnisse können nicht stimmen? Begründe, ohne "
                   r"genau zu rechnen. \\ (1) $f(x) = x^2 + 3$ und "
                   r"$g(x) = x^2$ von $0$ bis $2$: $A = 6$ \\ (2) "
                   r"$f(x) = x^2$ und die Gerade $y = 4$: $A = 40$ \\ (3) "
                   r"$f(x) = x$ und $g(x) = -x$ von $0$ bis $3$: $A = -9$ "
                   r"\\ (4) $f(x) = x^2$ und $g(x) = 4x - 3$ zwischen den "
                   r"Schnittstellen $1$ und $3$: $A = 0$"),
          loesung=("Nicht stimmen können (2), (3) und (4). (2): Die Fläche "
                   "liegt im Rechteck mit Breite $4$ und Höhe $4$, sie ist "
                   "kleiner als $16$. (3): Ein Flächeninhalt ist nie "
                   "negativ. (4): Zwischen zwei verschiedenen Schnittstellen "
                   "liegt ein Flächenstück mit positivem Inhalt. (1) kann "
                   "stimmen."),
          pruef="")
    merkmal(z, 2, 2, M_BEGR)
    setze(z, 2, 2, 2,
          aufgabe=(r"Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   r"ist. Begründe. \\ (1) Die Fläche zwischen zwei Graphen "
                   r"ist immer das Integral über $f - g$ zwischen den "
                   r"Schnittstellen. \\ (2) Liegt $f$ zwischen zwei "
                   r"Schnittstellen oben, ist das Integral über $f - g$ dort "
                   r"positiv. \\ (3) Die Lage der Graphen zur x-Achse spielt "
                   r"für die Fläche zwischen ihnen keine Rolle."),
          loesung=("(1) falsch, z. B. $f(x) = x^2$, $g(x) = 2x$ mit den "
                   "Schnittstellen $0$ und $2$: das Integral über $f - g$ "
                   "ist $-\\frac{4}{3}$, der Inhalt $\\frac{4}{3}$. (2) "
                   "wahr, denn dort ist $f - g > 0$. (3) wahr, denn nur der "
                   "senkrechte Abstand $f - g$ zählt (Differenzfunktion)."),
          pruef="")
    setze(z, 2, 2, 3,
          aufgabe=(r"Die Graphen von $f$ und $g$ kreuzen sich bei $0$, $1$ "
                   r"und $2$. Ella sagt: „Für die Fläche zwischen ihnen von "
                   r"$0$ bis $2$ muss ich bei $1$ teilen.“ Begründe, ob Ella "
                   r"recht hat. Begründe, ohne genau zu rechnen."),
          loesung=("Ja; an der Schnittstelle $1$ wechselt die obere "
                   "Funktion, in einem Zug würden sich die beiden Stücke im "
                   "Integral teilweise aufheben – jedes Stück braucht seinen "
                   "eigenen Betrag."),
          pruef="")
    setze(z, 2, 3, 2,
          aufgabe=(r"Ein Logo ist die Fläche zwischen den Graphen von "
                   r"$f(x) = 0{,}5x^2$ und $g(x) = 2x$ (Angaben in cm). Die "
                   r"Goldfolie kostet $0{,}40$ € je Quadratzentimeter. "
                   r"Reichen $2$ € für die Folie eines Logos?"),
          loesung=("Nein; Schnittstellen: $0{,}5x^2 = 2x$, $x = 0$ oder "
                   "$x = 4$; Integral: Integral von $0$ bis $4$ über "
                   "$(2x - 0{,}5x^2) = \\frac{16}{3} \\approx "
                   "5{,}33\\,\\text{cm}^2$; Kosten: $\\frac{16}{3} \\cdot "
                   "0{,}40 \\approx 2{,}13$ €; Vergleich: $2{,}13$ € $> 2$ "
                   "€, das Geld reicht nicht."))
    neu = schreibe(2, z)
    zaehle(2, alt, neu, set())


# ---------------------------------------------------------------- e3

def e3():
    alt = lade(3)
    z = copy.deepcopy(alt)
    texte(z, 104)
    pack = []
    for d in (1, 2, 3, 4, 5):
        pack.append(dict(
            merkmal=("gekrümmter Rand als Integral, gerader Rand als "
                     "Rechteck; Graph und Höhe 10 bleiben, die Breite des "
                     "Rechtecks wandert"),
            aufgabe=(f"Eine Fläche liegt über der x-Achse zwischen der "
                     f"y-Achse und der Geraden $x = {3 + d}$. Oben wird sie "
                     f"für $0 \\le x \\le 3$ vom Graphen von $f(x) = x^2 + 1$ "
                     f"begrenzt, danach von der waagerechten Strecke in Höhe "
                     f"$10$. Berechne ihren Inhalt."),
            form="teil", antwort="",
            loesung=(f"Zerlegen: Integral von $0$ bis $3$ und Rechteck von "
                     f"$3$ bis ${3 + d}$; Integral: $\\left[\\frac{{1}}{{3}}"
                     f"x^3 + x\\right]_0^3 = 9 + 3 = 12$; Rechteck: $10 "
                     f"\\cdot {d} = {10 * d}$; Ergebnis: $A = 12 + {10 * d} "
                     f"= {12 + 10 * d}$"),
            pruef=str(12 + 10 * d), grafik="", loesungsgrafik=""))
    z = ersetze(z, 1, 1, pack)
    merkmal(z, 2, 1, M_FEHLER)
    setze(z, 2, 1, 2,
          aufgabe=(r"Eine Fläche wird oben vom Graphen von $f(x) = x^2$ für "
                   r"$0 \le x \le 2$ und danach von der Strecke bis zum "
                   r"Punkt $(6|0)$ begrenzt, unten von der x-Achse. Nora "
                   r"rechnet so: \rechnung{\text{Integral von 0 bis 2 über } "
                   r"x^2 &= \tfrac{8}{3} \\ \text{Dreieck} &= \tfrac{1}{2} "
                   r"\cdot 4 \cdot 4 = 8 \\ A &= \tfrac{8}{3} + 8 = "
                   r"\tfrac{32}{3}} Prüfe, ob Nora richtig gerechnet hat."),
          loesung=("Richtig. Der gekrümmte Rand wird zum Integral, der "
                   "gerade zum Dreieck mit Grundseite $4$ und Höhe "
                   "$f(2) = 4$; die Stücke überlappen nicht, also addieren "
                   "sich die Inhalte."),
          pruef="")
    setze(z, 2, 1, 3,
          aufgabe=(r"Kim hat vier Ergebnisse notiert. Welche Ergebnisse "
                   r"können nicht stimmen? Begründe, ohne genau zu rechnen. "
                   r"\\ (1) Maßzahl $3$, eine Längeneinheit entspricht $2$ "
                   r"m: $A = 6\,\text{m}^2$ \\ (2) Kanal mit "
                   r"$2\,\text{m}^2$ Querschnitt und $10$ m Länge: "
                   r"$V = 20\,\text{m}^2$ \\ (3) Rinne mit "
                   r"$50\,\text{m}^3$ Volumen und $5\,\text{m}^2$ "
                   r"Querschnitt: Länge $250$ m \\ (4) Integral "
                   r"$\frac{8}{3}$ plus Dreieck $2$: $A = \frac{14}{3}$"),
          loesung=("Nicht stimmen können (1), (2) und (3). (1): Eine "
                   "Flächeneinheit ist $2\\,\\text{m} \\cdot 2\\,\\text{m} "
                   "= 4\\,\\text{m}^2$, drei davon sind mehr als "
                   "$6\\,\\text{m}^2$. (2): Ein Volumen hat die Einheit "
                   "$\\text{m}^3$, nicht $\\text{m}^2$. (3): $250$ m mal "
                   "$5\\,\\text{m}^2$ ist weit mehr als $50\\,\\text{m}^3$ – "
                   "multipliziert statt geteilt. (4) kann stimmen."),
          pruef="")
    merkmal(z, 2, 2, M_BEGR)
    setze(z, 2, 2, 2,
          aufgabe=(r"Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   r"ist. Begründe. \\ (1) Verdoppelt man den "
                   r"Längenmaßstab, verdoppelt sich die reale Fläche. \\ "
                   r"(2) Eine zusammengesetzte Fläche kann man immer in "
                   r"Stücke zerlegen, die sich nicht überlappen, und deren "
                   r"Inhalte addieren. \\ (3) Das Volumen eines Körpers mit "
                   r"überall gleichem Querschnitt ist Querschnittsfläche mal "
                   r"Länge."),
          loesung=("(1) falsch, z. B. bei $1$ LE $= 1$ m ist eine "
                   "Flächeneinheit $1\\,\\text{m}^2$, bei $1$ LE $= 2$ m "
                   "sind es $4\\,\\text{m}^2$ – die Fläche vervierfacht "
                   "sich. (2) wahr, denn Inhalte nicht überlappender Stücke "
                   "addieren sich (Additivität). (3) wahr, denn der Körper "
                   "besteht aus gleichen Scheiben, je Längeneinheit eine "
                   "mit dem Querschnitt als Volumen."),
          pruef="")
    setze(z, 2, 2, 3,
          aufgabe=(r"Paul sagt: „Ein Kanal mit doppeltem Querschnitt und "
                   r"halber Länge fasst gleich viel Wasser.“ Begründe, ob "
                   r"Paul recht hat. Begründe, ohne genau zu rechnen."),
          loesung=("Ja; das Volumen ist Querschnittsfläche mal Länge, und "
                   "das Doppelte mal die Hälfte ergibt wieder dasselbe "
                   "Produkt."),
          pruef="")
    setze(z, 2, 3, 3,
          aufgabe=(r"Ein Wall hat den Querschnitt zwischen dem Graphen von "
                   r"$f(x) = -0{,}5x^2 + 0{,}5$ und der x-Achse (Angaben in "
                   r"m) und ist $12$ m lang. Ein Kubikmeter Sand wiegt "
                   r"$1{,}5$ t, ein Lkw lädt $10$ t. Reicht eine Fahrt?"),
          loesung=("Nein; Nullstellen: $-1$ und $1$; Querschnitt: Integral "
                   "von $-1$ bis $1$ über $f(x) = \\frac{2}{3}\\,"
                   "\\text{m}^2$; Volumen: $\\frac{2}{3} \\cdot 12 = "
                   "8\\,\\text{m}^3$; Masse: $8 \\cdot 1{,}5 = 12$ t; "
                   "Vergleich: $12$ t $> 10$ t, es sind zwei Fahrten "
                   "nötig."),
          pruef="[8, 12]")
    setze(z, 2, 4, 3,
          aufgabe=(r"Die Abbildung zeigt den Graphen von $f(x) = 0{,}5x^2$ "
                   r"und die markierte Fläche zwischen dem Graphen, der "
                   r"y-Achse und der Geraden $y = 2$. Schreibe ihren Inhalt "
                   r"als Term aus Rechteck und Integral und berechne ihn."),
          form="text",
          loesung=("Term: $2 \\cdot 2$ minus Integral von $0$ bis $2$ über "
                   "$0{,}5x^2$; Integral: $\\left[\\frac{1}{6}x^3"
                   "\\right]_0^2 = \\frac{4}{3}$; Ergebnis: $A = 4 - "
                   "\\frac{4}{3} = \\frac{8}{3} \\approx 2{,}67$"),
          pruef="8/3",
          grafik=(r"\begin{ksys}[xmin=-1,xmax=4,ymin=-1,ymax=4,ablesen]"
                  r"\funktion{0.5*\x^2}{f}\flaechezwischen{2}{0.5*\x^2}{0}"
                  r"{2}{A}\end{ksys}"),
          loesungsgrafik="")
    merkmal(z, 2, 4, ("Term und Bild in beiden Richtungen: Teilflächen "
                      "markieren, markierte Fläche als Term schreiben"))
    neu = schreibe(3, z)
    zaehle(3, alt, neu, set())


# ---------------------------------------------------------------- e4

def e4():
    alt = lade(4)
    z = copy.deepcopy(alt)
    texte(z, 105, vorstufe_neu=False)
    pack = []
    for m, a_t, m3 in ((3, "18", "27"), (1, r"\frac{2}{3}", "1"),
                       (6, "144", "216"), (1.5, "2{,}25", "3{,}375"),
                       (2, r"\frac{16}{3}", "8")):
        mt = zahl(m)
        pack.append(dict(
            merkmal=("Flächenterm im Parameter gleich dem Inhalt setzen; "
                     "die Parabel f(x) = 0,5x² bleibt, der Inhalt wandert"),
            aufgabe=(f"Für $m > 0$ schließen die Gerade $y = m \\cdot x$ und "
                     f"der Graph von $f(x) = 0{{,}}5x^2$ eine Fläche mit dem "
                     f"Inhalt ${a_t}$ ein. Bestimme $m$."),
            form="teil", antwort="",
            loesung=(f"Schnittstellen: $0{{,}}5x^2 = m x$, $x = 0$ oder "
                     f"$x = 2m$; Flächenterm: Integral von $0$ bis $2m$ über "
                     f"$(m x - 0{{,}}5x^2) = \\frac{{2}}{{3}}m^3$; "
                     f"Bedingung: $\\frac{{2}}{{3}}m^3 = {a_t}$, also "
                     f"$m^3 = {m3}$; Ergebnis: $m = {mt}$"),
            pruef=repr(m), grafik="", loesungsgrafik=""))
    z = ersetze(z, 1, 1, pack)
    merkmal(z, 2, 1, M_FEHLER)
    setze(z, 2, 1, 2,
          aufgabe=(r"Die Fläche unter dem Graphen von $f(x) = 2x$ von $0$ "
                   r"bis $6$ soll durch die Gerade $x = k$ halbiert werden. "
                   r"Jana rechnet so: \rechnung{\text{Gesamt: } \left[x^2"
                   r"\right]_0^6 &= 36 \\ \text{Teilfläche bis } k &= k^2 "
                   r"\\ k^2 &= 18 \\ k &= \sqrt{18} \approx 4{,}24} Prüfe, "
                   r"ob Jana richtig gerechnet hat."),
          loesung=("Richtig. Die Teilfläche bis $x = k$ ist $k^2$, und "
                   "halbieren heißt: dieser Flächenterm ist gleich dem "
                   "halben Gesamtinhalt."),
          pruef="")
    setze(z, 2, 1, 3,
          aufgabe=(r"Emil hat vier Flächenbedingungen gelöst. Welche "
                   r"Ergebnisse können nicht stimmen? Begründe, ohne genau "
                   r"zu rechnen. \\ (1) $x = k$ halbiert die Fläche unter "
                   r"$f(x) = x + 1$ von $0$ bis $4$: $k = 5$ \\ (2) $x = k$ "
                   r"halbiert die Fläche unter $f(x) = x^2$ von $0$ bis $3$: "
                   r"$k = 1{,}5$ \\ (3) Für $m > 0$ schließen $y = m \cdot x$ "
                   r"und $f(x) = 2x^2$ die Fläche $9$ ein: $m = -6$ \\ (4) "
                   r"$x = k$ halbiert die Fläche unter $f(x) = 6 - x$ von "
                   r"$0$ bis $6$: $k \approx 1{,}76$"),
          loesung=("Nicht stimmen können (1), (2) und (3). (1): $k$ muss "
                   "zwischen $0$ und $4$ liegen. (2): $f$ wächst, rechts von "
                   "der Mitte $1{,}5$ liegt mehr Fläche als links, $k$ muss "
                   "größer sein. (3): Verlangt ist $m > 0$. (4) kann "
                   "stimmen, denn $f$ fällt und $k$ liegt links der Mitte."),
          pruef="")
    merkmal(z, 2, 2, M_BEGR)
    setze(z, 2, 2, 2,
          aufgabe=(r"Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   r"ist. Begründe. \\ (1) Die senkrechte Gerade durch die "
                   r"Mitte des Intervalls halbiert immer die Fläche unter "
                   r"einem Graphen. \\ (2) Ist $f$ positiv, wächst die "
                   r"Fläche unter dem Graphen von $0$ bis $b$ mit $b$. \\ "
                   r"(3) Es gibt ein $b > 0$, für das das Integral von $0$ "
                   r"bis $b$ über $(x - 3)$ null ist."),
          loesung=("(1) falsch, z. B. $f(x) = x^2$ von $0$ bis $2$: links "
                   "von $1$ liegt $\\frac{1}{3}$, rechts $\\frac{7}{3}$. (2) "
                   "wahr, denn mit größerem $b$ kommt ein Streifen mit "
                   "positivem Inhalt hinzu (Monotonie des Flächenterms). "
                   "(3) wahr, denn z. B. für $b = 6$ ist das Integral "
                   "$18 - 18 = 0$."),
          pruef="")
    setze(z, 2, 2, 3,
          aufgabe=(r"Kai sagt: „Die Gerade $x = 2$ halbiert die Fläche unter "
                   r"dem Graphen von $f(x) = 4 - x$ von $0$ bis $4$ nicht, "
                   r"links liegt mehr als rechts.“ Begründe, ob Kai recht "
                   r"hat. Begründe, ohne genau zu rechnen."),
          loesung=("Ja; $f$ fällt, links von $2$ sind die Streifen höher als "
                   "rechts – die Halbierungsgerade liegt links der Mitte."),
          pruef="")
    setze(z, 2, 3, 2,
          aufgabe=(r"Wasser fließt $8$ Minuten lang mit der Rate "
                   r"$r(t) = -0{,}5t^2 + 4t$ (in Liter je Minute) in ein "
                   r"Becken. Ist nach $3$ Minuten schon die Hälfte des "
                   r"Wassers eingeflossen?"),
          loesung=("Nein; Gesamtmenge: Integral von $0$ bis $8$ über "
                   "$r(t) = \\frac{128}{3} \\approx 42{,}67$ Liter; Hälfte: "
                   "$\\approx 21{,}33$ Liter; nach drei Minuten: Integral von "
                   "$0$ bis $3$ über $r(t) = 13{,}5$ Liter; Vergleich: "
                   "$13{,}5 < 21{,}33$, die Hälfte ist erst nach $4$ Minuten "
                   "erreicht."),
          pruef="[128/3, 13.5]")
    neu = schreibe(4, z)
    zaehle(4, alt, neu, set())


# ---------------------------------------------------------------- e5

def e5():
    alt = lade(5)
    z = copy.deepcopy(alt)
    texte(z, 106)
    werte = {1: (0, 1.5), 2: (0, 2), 3: (0.5, 2), 4: (2, 2), 5: (4.5, 2)}
    pack = []
    for b in (1, 2, 3, 4, 5):
        o, u = werte[b]
        w = o - u
        pack.append(dict(
            merkmal=("Kästchen über der Achse positiv, darunter negativ "
                     "zählen; der Graph bleibt, die obere Grenze wandert"),
            aufgabe=(f"Die Abbildung zeigt den Graphen von $f(x) = x - 2$; "
                     f"die Gitterlinien haben den Abstand $1$. Bestimme den "
                     f"Wert des Integrals von $0$ bis ${b}$ über $f(x)$, "
                     f"indem du Kästchen zählst."),
            form="teil", antwort="",
            loesung=(f"Über der Achse: ${zahl(o)}$ Kästchen; unter der "
                     f"Achse: ${zahl(u)}$ Kästchen; Bilanz: ${zahl(o)} - "
                     f"{zahl(u)} = {zahl(w)}$; Ergebnis: Wert $= {zahl(w)}$"),
            pruef=repr(w),
            grafik=(r"\begin{ksys}[xmin=-1,xmax=6,ymin=-3,ymax=4,xstep=1,"
                    r"ystep=1,ablesen]\funktion{\x-2}{f}\end{ksys}"),
            loesungsgrafik=""))
    z = ersetze(z, 1, 1, pack)
    # neue Sprosse s3, alte s3..s7 -> s4..s8
    for a in z:
        if a["kette_nr"] == 1 and a["sprosse"] >= 3:
            a["sprosse"] += 1
    s2 = [j for j, a in enumerate(z) if a["kette_nr"] == 1
          and a["sprosse"] == 2]
    vorlage = z[s2[0]]
    st = segmente(106)[3]
    neue = [
        dict(aufgabe=(r"Gegeben ist $f(x) = 2x - 2$. Berechne zu den "
                      r"Grenzen $0$ und $3$ den Wert des Integrals über "
                      r"$f(x)$ und den Inhalt der Fläche zwischen Graph und "
                      r"x-Achse. Nenne beide Ergebnisse nebeneinander."),
             loesung=(r"Nullstelle: $x = 1$ im Intervall; Stammfunktion: "
                      r"$F(x) = x^2 - 2x$; Wert: $F(3) - F(0) = 3 - 0 = 3$; "
                      r"Teilflächen: $|F(1) - F(0)| = |-1| = 1$ und "
                      r"$F(3) - F(1) = 3 + 1 = 4$; Fläche: $1 + 4 = 5$; "
                      r"Ergebnis: Wert $= 3$, Fläche $= 5$"),
             pruef="[3, 5]"),
        dict(aufgabe=(r"Gegeben ist $f(x) = x^2 - 4$. Berechne zu den "
                      r"Grenzen $0$ und $3$ den Wert des Integrals über "
                      r"$f(x)$ und den Inhalt der Fläche zwischen Graph und "
                      r"x-Achse. Nenne beide Ergebnisse nebeneinander."),
             loesung=(r"Nullstelle: $x = 2$ im Intervall; Stammfunktion: "
                      r"$F(x) = \frac{1}{3}x^3 - 4x$; Wert: $F(3) - F(0) = "
                      r"-3 - 0 = -3$; Teilflächen: $\left|F(2) - F(0)"
                      r"\right| = \frac{16}{3}$ und $F(3) - F(2) = "
                      r"\frac{7}{3}$; Fläche: $\frac{16}{3} + \frac{7}{3} = "
                      r"\frac{23}{3}$; Ergebnis: Wert $= -3$, Fläche "
                      r"$\approx 7{,}67$"),
             pruef="[-3, 23/3]"),
        dict(aufgabe=(r"Gegeben ist $f(x) = x^3 - x$. Berechne zu den "
                      r"Grenzen $-1$ und $2$ den Wert des Integrals über "
                      r"$f(x)$ und den Inhalt der Fläche zwischen Graph und "
                      r"x-Achse. Nenne beide Ergebnisse nebeneinander."),
             loesung=(r"Nullstellen: $x = 0$ und $x = 1$ im Intervall; "
                      r"Stammfunktion: $F(x) = \frac{1}{4}x^4 - "
                      r"\frac{1}{2}x^2$; Wert: $F(2) - F(-1) = 2 + "
                      r"\frac{1}{4} = 2{,}25$; Teilflächen: $\frac{1}{4}$, "
                      r"$\left|-\frac{1}{4}\right| = \frac{1}{4}$ und "
                      r"$F(2) - F(1) = 2{,}25$; Fläche: $0{,}25 + 0{,}25 + "
                      r"2{,}25 = 2{,}75$; Ergebnis: Wert $= 2{,}25$, Fläche "
                      r"$= 2{,}75$"),
             pruef="[2.25, 2.75]"),
    ]
    rows = [zeile(vorlage, sprosse=3, sprosse_text=st, variante=i + 1,
                  merkmal=("Wert und Fläche zu denselben Grenzen "
                           "nebeneinander, Nullstelle im Intervall"),
                  form="teil", antwort="Wert: __ Fläche: __", grafik="",
                  loesungsgrafik="", original=None, **d)
            for i, d in enumerate(neue)]
    z = z[:s2[-1] + 1] + rows + z[s2[-1] + 1:]
    # Prüfungssprosse (jetzt s8): fehlende Originale ergänzen
    pr = [j for j, a in enumerate(z) if a["hoehe"] == "pruefung"]
    pv = z[pr[0]]
    o1 = {"id": "2025MerhoehtBAnalysisMMS1-1c", "jahr": 2025,
          "papier": "2025-iqb-ea-mms"}
    o2 = {"id": "2024MerhoehtBAnalysisWTR1-1f", "jahr": 2024,
          "papier": "2024-iqb-ea"}
    zus = [
        dict(original=o1, form="text",
             aufgabe=(r"Für $k > 0$ ist $f_k(x) = k \cdot x^2 \cdot "
                      r"(x + k)^2$. Beurteile ohne Berechnung eines "
                      r"Integrals die Aussage: Für jeden Wert von $k$ gibt "
                      r"das Integral von $-2$ bis $2$ über $f_k(x)$ den "
                      r"Inhalt der Fläche zwischen Graph und x-Achse auf "
                      r"diesem Intervall an. (Abitur 2025 LK)"),
             loesung=(r"Richtig: $k$ ist positiv, $x^2$ und $(x + k)^2$ "
                      r"sind nie negativ, also ist $f_k(x)$ nie negativ; an "
                      r"der Nullstelle $-k$ berührt der Graph die x-Achse "
                      r"nur, das Integral zählt kein Stück negativ."),
             pruef=""),
        dict(original=o1, form="text",
             aufgabe=(r"Für $k > 0$ ist $f_k(x) = (x - k) \cdot x^2$. "
                      r"Beurteile ohne Berechnung eines Integrals die "
                      r"Aussage: Für jeden Wert von $k$ gibt das Integral "
                      r"von $-1$ bis $1$ über $f_k(x)$ den Inhalt der "
                      r"Fläche zwischen Graph und x-Achse auf diesem "
                      r"Intervall an. (Abitur 2025 LK)"),
             loesung=(r"Falsch: Für $x < k$ ist der Faktor $x - k$ negativ "
                      r"und $x^2$ nicht negativ; für große $k$ liegt der "
                      r"Graph auf dem ganzen Intervall unter der x-Achse, "
                      r"das Integral ist dann negativ und nicht der "
                      r"Inhalt."),
             pruef=""),
        dict(original=o2, form="text",
             aufgabe=(r"Der Graph von $f$ ist punktsymmetrisch zum Punkt "
                      r"$P(0|3)$. Begründe, dass sich das Integral von $-k$ "
                      r"bis $k$ über $f(x)$ für jedes $k > 0$ ohne "
                      r"Stammfunktion exakt angeben lässt, und gib seinen "
                      r"Wert an. (Abitur 2024 LK)"),
             loesung=(r"Symmetrie: die Stücke zwischen Graph und der "
                      r"Geraden $y = 3$ links und rechts von $0$ sind gleich "
                      r"groß und liegen auf verschiedenen Seiten der "
                      r"Geraden, sie heben sich auf; Rechteck: Höhe $3$, "
                      r"Breite $2k$; Ergebnis: Wert $= 6k$"),
             pruef="6"),
        dict(original=o2, form="text",
             aufgabe=(r"Der Graph von $f$ ist punktsymmetrisch zum Punkt "
                      r"$Q(0|-1)$. Begründe, dass sich das Integral von "
                      r"$-k$ bis $k$ über $f(x)$ für jedes $k > 0$ ohne "
                      r"Stammfunktion exakt angeben lässt, und gib seinen "
                      r"Wert an. (Abitur 2024 LK)"),
             loesung=(r"Symmetrie: die Stücke zwischen Graph und der "
                      r"Geraden $y = -1$ links und rechts von $0$ sind "
                      r"gleich groß und liegen auf verschiedenen Seiten der "
                      r"Geraden, sie heben sich auf; Rechteck: unter der "
                      r"x-Achse, Höhe $1$, Breite $2k$, zählt negativ; "
                      r"Ergebnis: Wert $= -2k$"),
             pruef="-2"),
    ]
    n0 = len(pr)
    zrows = [zeile(pv, variante=n0 + i + 1, antwort="", grafik="",
                   loesungsgrafik="", **d) for i, d in enumerate(zus)]
    z = z[:pr[-1] + 1] + zrows + z[pr[-1] + 1:]
    # Pflicht
    merkmal(z, 2, 1, M_FEHLER)
    setze(z, 2, 1, 2,
          aufgabe=(r"Im Gitter hat ein Kästchen den Inhalt $0{,}5$. Zwischen "
                   r"Graph und x-Achse liegen über der Achse $8$ Kästchen, "
                   r"unter der Achse $6$. Lukas rechnet so: "
                   r"\rechnung{\text{Integral} &\approx (8 - 6) \cdot 0{,}5 "
                   r"= 1} Prüfe, ob Lukas richtig gerechnet hat."),
          loesung=("Richtig. Das Integral zählt Stücke über der Achse "
                   "positiv und darunter negativ, und jedes Kästchen zählt "
                   "mit seinem Inhalt $0{,}5$."),
          pruef="")
    setze(z, 2, 1, 3,
          aufgabe=(r"Sara hat vier Werte angegeben. Welche Ergebnisse können "
                   r"nicht stimmen? Begründe, ohne genau zu rechnen. \\ (1) "
                   r"Integral von $0$ bis $2$ über $x^2$: "
                   r"$-\frac{8}{3}$ \\ (2) Integral von $-1$ bis $1$ über "
                   r"$x^3$: $0$ \\ (3) Mittelwert von $f(x) = x^2 + 1$ auf "
                   r"$[0; 3]$: $0{,}5$ \\ (4) Integral von $0$ bis $4$ über "
                   r"$(x - 2)$: $0$"),
          loesung=("Nicht stimmen können (1) und (3). (1): $x^2$ ist nie "
                   "negativ, das Integral von links nach rechts also auch "
                   "nicht. (3): $f$ ist überall mindestens $1$, der "
                   "Mittelwert also auch. (2) und (4) können stimmen."),
          pruef="")
    merkmal(z, 2, 2, M_BEGR)
    setze(z, 2, 2, 2,
          aufgabe=(r"Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                   r"ist. Begründe. \\ (1) Ein Integral ist nie negativ. "
                   r"\\ (2) Ist das Integral von $a$ bis $b$ null, schließt "
                   r"der Graph dort keine Fläche mit der x-Achse ein. \\ "
                   r"(3) Der Mittelwert einer stetigen Funktion auf einem "
                   r"Intervall liegt immer zwischen ihrem kleinsten und "
                   r"ihrem größten Wert dort."),
          loesung=("(1) falsch, z. B. ist das Integral von $0$ bis $1$ über "
                   "$(-x)$ gleich $-0{,}5$. (2) falsch, z. B. $f(x) = x$ "
                   "von $-1$ bis $1$: Integral $0$, Fläche $1$. (3) wahr, "
                   "denn das Rechteck mit dem Mittelwert als Höhe hat "
                   "denselben Inhalt wie die Fläche unter dem Graphen, es "
                   "kann nicht ganz über oder ganz unter dem Graphen "
                   "liegen."),
          pruef="")
    setze(z, 2, 2, 3,
          aufgabe=(r"Sophie sagt: „Das Integral von $0$ bis $4$ über "
                   r"$f(x) = x - 1$ ist $4$, also ist die Fläche zwischen "
                   r"Graph und x-Achse auf diesem Intervall $4$.“ Begründe, "
                   r"ob Sophie recht hat. Begründe, ohne genau zu rechnen."),
          loesung=("Nein; von $0$ bis $1$ liegt der Graph unter der "
                   "x-Achse, dieses Stück zählt im Integral negativ, in der "
                   "Fläche positiv – die Fläche ist größer als $4$ "
                   "(Integralwert ist nicht Flächeninhalt)."),
          pruef="")
    setze(z, 2, 3, 2,
          aufgabe=(r"Ein Fluss führt einem See $z(t) = 20 + 10e^{-0{,}1t}$ "
                   r"Kubikmeter Wasser je Sekunde zu ($t$ in Tagen). Liegt "
                   r"die mittlere Zuflussrate in den ersten $10$ Tagen über "
                   r"$25$ Kubikmeter je Sekunde?"),
          loesung=("Ja; Integral: Integral von $0$ bis $10$ über $z(t) = "
                   "200 + 100(1 - e^{-1}) \\approx 263{,}2$; Mittelwert: "
                   "$\\frac{263{,}2}{10} \\approx 26{,}32$ Kubikmeter je "
                   "Sekunde; Vergleich: $26{,}32 > 25$."),
          pruef="[200+100*(1-math.exp(-1)), (200+100*(1-math.exp(-1)))/10]")
    setze(z, 2, 4, 3,
          aufgabe=(r"Die Abbildung zeigt den Graphen von $f(x) = x^2$ und "
                   r"ein markiertes Flächenstück. Schreibe seinen Inhalt "
                   r"als Integral und berechne ihn."),
          form="text",
          loesung=("Term: Integral von $1$ bis $2$ über $x^2$; "
                   "Stammfunktion: $F(x) = \\frac{1}{3}x^3$; Ergebnis: "
                   "$A = \\frac{8}{3} - \\frac{1}{3} = \\frac{7}{3} \\approx "
                   "2{,}33$"),
          pruef="7/3",
          grafik=(r"\begin{ksys}[xmin=-1,xmax=4,ymin=-1,ymax=10,ablesen]"
                  r"\funktion{\x^2}{f}\flaeche{\x^2}{1}{2}{A}\end{ksys}"),
          loesungsgrafik="")
    merkmal(z, 2, 4, ("Inhalt und Bild in beiden Richtungen: Flächenstück "
                      "einzeichnen, markiertes Stück als Integral schreiben"))
    neu = schreibe(5, z)
    ids = {a["id"] for a in neu if (a["kette_nr"] == 1 and a["sprosse"] == 3)
           or (a["hoehe"] == "pruefung" and a["variante"] > n0)}
    zaehle(5, alt, neu, ids)


if __name__ == "__main__":
    e1()
    e2()
    e3()
    e4()
    e5()

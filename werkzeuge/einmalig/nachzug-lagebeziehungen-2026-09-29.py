"""Nachzug bank/lagebeziehungen auf die Mappe vom 29.09. (Katalog 2a296e5).

Einmalig. Liest den Bestand (27.09.), zieht quelle, sprosse, id und
sprosse_text nach, schreibt die neue Sprosse „Seite gegen den
Ursprung“ (e1), die Grundfall-Päckchen am festen Körper (e1–e4), die
Kontrollzeile der Geradenschar (e3 Prüfungshöhe) und die Pflichtformen
(P1, P2, P4, P6). Zählt je Einheit übernommen/neu/umgeschrieben/
entfallen und schreibt sie nach bank/lagebeziehungen/_tmp/zahlen.json.

Aufruf: python3 werkzeuge/einmalig/nachzug-lagebeziehungen-2026-09-29.py [e1 e2 …]
"""
import copy
import json
import sys
from fractions import Fraction
from pathlib import Path

B = Path(__file__).resolve().parents[2] / "bank" / "lagebeziehungen"
E = "lagebeziehungen"
QMAP = {96: 93, 97: 94, 98: 95, 99: 96}

TEXT = {
    # neue Sprossentexte (Zeilen 93, 95, 96 der Mappe)
    "e1s0": ("„Erfüllt, größer oder kleiner?“ – zu Punktproben ankreuzen, "
             "was das Einsetzen liefert und was es heißt (drin, diese "
             "Seite, jene Seite); nichts rechnen"),
    "e1neu": ("Seite gegen den Ursprung: den Punkt in die nach null "
              "umgestellte Gleichung einsetzen und das Vorzeichen mit dem "
              "des Ursprungs vergleichen"),
    "e3s0": ("„Fällt der Parameter heraus?“ – beim Einsetzen des "
             "allgemeinen Geradenpunkts ankreuzen, was gilt: fällt heraus "
             "und stimmt, dann liegt sie darin; fällt heraus und stimmt "
             "nicht, dann parallel; bleibt, dann ein Schnittpunkt; nichts "
             "rechnen"),
    "e3s6": ("die Lage einer Geradenschar zur Ebene mit Fallunterscheidung "
             "untersuchen und den parameterabhängigen Schnittpunkt angeben, "
             "Kontrolle: den Schnittpunkt in die Ebenengleichung einsetzen, "
             "sie muss erfüllt sein (abi 2024-bebb-lk-A1.8a, Niveau II, "
             "Teil A, LK) und die Parameterwerte gemeinsamer Punkte der "
             "Pyramidenschar bestimmen"),
    "e4s0": ("„Rechnung fertig – Frage beantwortet?“ – zu Sachaufgaben "
             "ankreuzen, ob nach dem Durchstoßpunkt noch ein Bereich zu "
             "prüfen ist (Wandmaße, Feldgrenzen, Netzhöhe); nichts rechnen"),
}


ALT = "8362b2d"   # Bestand vor dem Nachzug (27./28.09.)

# Pooldubletten: die Kennung, die in der Mappe zuerst steht (bank.md 29.09.)
DUBL = {
    "2022MerhoehtBAGLAA2WTR1-1e": ("2022-bebb-lk-B3h", 2022, "2022-bebb-lk"),
    "2024MgrundlegendAAGLAA213-a": ("2024-bebb-gk-A1.2a", 2024,
                                    "2024-bebb-gk"),
    "2025MgrundlegendAAGLAA213-b": ("2025-bebb-gk-A1.5b", 2025,
                                    "2025-bebb-gk"),
    "2026MgrundlegendAAGLAA211-a": ("2026-bb-gk-A1.2a", 2026, "2026-bb-gk"),
    "2026MerhoehtAAGLAA221-a": ("2026-bb-ea-A1.8a", 2026, "2026-bb-ea"),
    "2026MerhoehtBAGLAA2WTR2-1d": ("2026-bb-ea-B3d", 2026, "2026-bb-ea"),
}


def lade(f):
    import subprocess
    txt = subprocess.run(
        ["git", "-C", str(B), "show", f"{ALT}:bank/{E}/{f}.jsonl"],
        capture_output=True, text=True, check=True).stdout
    return [json.loads(l) for l in txt.split("\n") if l]


def dublette(r):
    o = r.get("original")
    if o and o["id"] in DUBL:
        i, j, p = DUBL[o["id"]]
        r["original"] = {"id": i, "jahr": j, "papier": p}
        r["_dubl"] = True


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
    r.update(kw)
    r["_art"] = "uebernommen"
    r["id"] = rid(r)
    return r


def umschreiben(r, **kw):
    r = copy.deepcopy(r)
    r["quelle"] = QMAP.get(r["quelle"], r["quelle"])
    r.update(kw)
    r["_art"] = "umgeschrieben"
    r["id"] = rid(r)
    return r


def neu(vorlage, **kw):
    r = copy.deepcopy(vorlage)
    r["quelle"] = QMAP.get(r["quelle"], r["quelle"])
    r.update(kw)
    r["original"] = kw.get("original")
    r["_art"] = "neu"
    r["id"] = rid(r)
    return r


def T(*k):
    def f(x):
        s = f"{x:g}" if isinstance(x, float) else str(x)
        return s.replace(".", "{,}").replace("-", "-")
    return "(" + " | ".join(f(x) for x in k) + ")"


def zahl(x):
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    return f"{float(x):g}".replace(".", "{,}")


def pz(x):
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):g}"


# --- e1 ------------------------------------------------------------------

PYR1 = {"A": (1, 1, 0), "B": (5, 1, 0), "C": (5, 4, 0), "D": (1, 4, 0),
        "S": (3, 2, 4)}
N1, D1 = (6, 8, 1), 38


def e1():
    rows = lade("e1")
    out = []
    by = {r["id"]: r for r in rows}
    k2 = [r for r in rows if r["kette_nr"] == 2]
    kopf = ("Die Pyramide $ABCDS$ hat die Grundfläche $A(1 | 1 | 0)$, "
            "$B(5 | 1 | 0)$, $C(5 | 4 | 0)$, $D(1 | 4 | 0)$ und die Spitze "
            "$S(3 | 2 | 4)$. Gegeben ist die Ebene $E: 6x + 8y + z = 38$. ")
    for r in rows:
        if r["kette_nr"] == 1:
            out.append(nachziehen(r))
    for r in k2:
        s = r["sprosse"]
        if s == 0:
            out.append(nachziehen(r, sprosse_text=TEXT["e1s0"]))
        elif s == 1:
            v = r["variante"]
            ecke = "BASCD"[v - 1]
            x, y, z = PYR1[ecke]
            w = 6 * x + 8 * y + z
            wort = "Spitze" if ecke == "S" else "Ecke"
            if w == D1:
                erg = (f"vergleichen: ${w} = {D1}$, die Gleichung ist "
                       f"erfüllt; Ergebnis: ${ecke}$ liegt in $E$.")
            else:
                erg = (f"vergleichen: ${w} \\neq {D1}$; Ergebnis: "
                       f"${ecke}$ liegt nicht in $E$.")
            out.append(umschreiben(
                r,
                merkmal=("Koordinaten einsetzen, erfüllt oder nicht, den "
                         "Befund benennen; Pyramide und E bleiben, die "
                         "Ecke wandert"),
                aufgabe=kopf + f"Prüfe, ob die {wort} ${ecke}$ in $E$ liegt.",
                loesung=(f"einsetzen: $6 \\cdot {x} + 8 \\cdot {y} + {z} = "
                         f"{w}$; " + erg),
                pruef=str(w)))
        elif s <= 5:
            out.append(nachziehen(r))
    # neue Sprosse s6
    vor = [r for r in k2 if r["sprosse"] == 6][0]
    neu_s6 = [
        (kopf + "Liegt die Ecke $A$ auf derselben Seite von $E$ wie der "
         "Ursprung? Begründe.",
         "umstellen: $6x + 8y + z - 38 = 0$; $A$ einsetzen: $6 + 8 + 0 - 38 "
         "= -24$; Ursprung einsetzen: $0 - 38 = -38$; Vorzeichen "
         "vergleichen: beide negativ; Ergebnis: Ja, $A$ liegt auf "
         "derselben Seite wie der Ursprung.", "[-24, -38]"),
        (kopf + "Liegt die Ecke $C$ auf derselben Seite von $E$ wie der "
         "Ursprung? Begründe.",
         "umstellen: $6x + 8y + z - 38 = 0$; $C$ einsetzen: $30 + 32 + 0 - "
         "38 = 24$; Ursprung einsetzen: $0 - 38 = -38$; Vorzeichen "
         "vergleichen: positiv gegen negativ; Ergebnis: Nein, $C$ liegt "
         "auf der anderen Seite als der Ursprung.", "[24, -38]"),
        ("Gegeben sind die Ebene $F: x + y - 2z = -4$ und der Punkt "
         "$P(1 | 1 | 2)$. Liegt $P$ auf derselben Seite von $F$ wie der "
         "Ursprung? Begründe.",
         "umstellen: $x + y - 2z + 4 = 0$; $P$ einsetzen: $1 + 1 - 4 + 4 = "
         "2$; Ursprung einsetzen: $0 + 4 = 4$; Vorzeichen vergleichen: "
         "beide positiv; Ergebnis: Ja, $P$ liegt auf derselben Seite wie "
         "der Ursprung.", "[2, 4]"),
    ]
    for i, (a, l, p) in enumerate(neu_s6, 1):
        out.append(neu(
            vor, sprosse=6, variante=i, sprosse_text=TEXT["e1neu"],
            merkmal=("die Seite über das Vorzeichen der nach null "
                     "umgestellten Gleichung, verglichen mit dem Ursprung"),
            hoehe="sprosse", aufgabe=a, loesung=l, pruef=p, form="text",
            antwort="", grafik="", loesungsgrafik=""))
    for r in k2:
        if r["sprosse"] >= 6:
            out.append(nachziehen(r, sprosse=r["sprosse"] + 1))
    # Pflicht k3
    for r in rows:
        if r["kette_nr"] != 3:
            continue
        key = (r["sprosse"], r["variante"])
        if key == (1, 2):   # P2 fehlerfreie Vorlage
            out.append(umschreiben(
                r,
                aufgabe=("Finn prüft, ob $P(2 | 9 | 1)$ in $E: 3x - 2z = 4$ "
                         "liegt. Finn rechnet: einsetzen: $3 \\cdot 2 - 2 "
                         "\\cdot 1 = 4$; vergleichen: $4 = 4$; also liegt "
                         "$P$ in $E$, die $9$ kommt in der Gleichung nicht "
                         "vor. Prüfe, ob Finn richtig gerechnet hat."),
                loesung=("Richtig. Eine fehlende Variable ist kein Fehler: "
                         "die y-Koordinate darf jeden Wert haben, "
                         "entscheidend sind x und z, und sie erfüllen die "
                         "Gleichung."),
                pruef=""))
        elif key == (1, 3):  # P1 Serie
            out.append(umschreiben(
                r,
                aufgabe=("Gegeben sind $E: 2x + y + 3z = 12$ und "
                         "$P(1 | 2 | 2)$. Vier Schüler haben $P$ in die "
                         "linke Seite eingesetzt und erhalten: (1) $10$; "
                         "(2) $10{,}5$; (3) $-10$; (4) $11$. Welche "
                         "Ergebnisse können nicht stimmen? Begründe, ohne "
                         "genau zu rechnen."),
                loesung=("(2) kann nicht stimmen – alle Koeffizienten und "
                         "Koordinaten sind ganze Zahlen, also auch das "
                         "Ergebnis; (3) kann nicht stimmen – alle Summanden "
                         "sind positiv; (4) kann nicht stimmen – $2 \\cdot "
                         "1$, $2$ und $3 \\cdot 2$ sind gerade, also auch "
                         "ihre Summe."),
                pruef=""))
        elif key == (2, 2):  # P4 Aussagenserie
            out.append(umschreiben(
                r,
                aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                         "falsch ist. Begründe. (1) Fehlt in einer "
                         "Koordinatengleichung eine Variable, darf die "
                         "zugehörige Koordinate eines Punkts der Ebene "
                         "jeden Wert haben. (2) Zwei Punkte, die beim "
                         "Einsetzen beide einen zu großen Wert liefern, "
                         "liegen immer auf verschiedenen Seiten der Ebene. "
                         "(3) Es gibt Punkte, deren Koordinaten die "
                         "Gleichung einer Ebene erfüllen und die trotzdem "
                         "nicht in der Ebene liegen."),
                loesung=("(1) wahr, denn die fehlende Koordinate kommt in "
                         "der Gleichung nicht vor und ändert den Wert der "
                         "linken Seite nicht; (2) falsch, z. B. liefern bei "
                         "$x + y + z = 3$ die Punkte $(2 | 2 | 0)$ und "
                         "$(0 | 0 | 5)$ die Werte $4$ und $5$, beide zu "
                         "groß – sie liegen auf derselben Seite; (3) falsch, "
                         "denn die Ebene ist genau die Menge der Punkte, "
                         "die ihre Gleichung erfüllen."),
                pruef=""))
        elif key == (2, 3):  # P6 Personenaussage
            out.append(umschreiben(
                r,
                aufgabe=("Lina sagt: „$P(3 | 5 | 1)$ kann nicht in "
                         "$E: x - 3z = 0$ liegen, weil die Gleichung kein "
                         "$y$ hat.“ Begründe, ohne genau zu rechnen, ob "
                         "Lina recht hat."),
                loesung=("Nein; eine fehlende Variable ist kein Fehler – "
                         "die y-Koordinate darf beliebig sein, und x und z "
                         "erfüllen die Gleichung, $P$ liegt in $E$."),
                pruef=""))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


# --- e2 ------------------------------------------------------------------

PYR2 = {"A": (1, 0, 0), "B": (3, 0, 0), "C": (3, 2, 0), "D": (1, 2, 0),
        "S": (2, 1, 4)}


def e2():
    rows = lade("e2")
    out = []
    kopf = ("Die Pyramide $ABCDS$ hat die Grundfläche $A(1 | 0 | 0)$, "
            "$B(3 | 0 | 0)$, $C(3 | 2 | 0)$, $D(1 | 2 | 0)$ und die Spitze "
            "$S(2 | 1 | 4)$. Für jede Zahl $k$ ist die Ebene "
            "$E_k: kx + 3y + z = 12$ gegeben. ")
    for r in rows:
        if r["kette_nr"] == 1 and r["sprosse"] == 1:
            v = r["variante"]
            ecke = "ABDSC"[v - 1]
            x, y, z = PYR2[ecke]
            rest = 3 * y + z
            k = Fraction(12 - rest, x)
            wort = "Spitze" if ecke == "S" else "Ecke"
            links = f"{x}k" if x != 1 else "k"
            zeilen = [f"${ecke}$ einsetzen: ${links} + 3 \\cdot {y} + {z} "
                      f"= 12$"]
            if rest:
                zeilen.append(f"zusammenfassen: ${links} + {rest} = 12$")
            zeilen.append(f"auflösen: $k = {zahl(k)}$")
            if v == 5:
                zeilen.append(f"Kontrolle: $2 \\cdot 3 + 3 \\cdot 2 + 0 = 12$, "
                              f"die Gleichung ist für $C$ erfüllt")
                auf = (kopf + "Die Ebene $E_k$ soll die Ecke $C$ enthalten, "
                       "nicht die Ecke $B$. Bestimme $k$. Zur Kontrolle: "
                       "$k = 2$. (Abitur 2022 LK)")
                zeilen[-2] = (f"auflösen: $3k = 6$, also $k = {zahl(k)}$")
            else:
                auf = (kopf + f"Bestimme $k$ so, dass $E_k$ die {wort} "
                       f"${ecke}$ enthält.")
            out.append(umschreiben(
                r,
                merkmal=("den Punkt einsetzen und die Gleichung nach dem "
                         "Parameter auflösen; Pyramide und E_k bleiben, die "
                         "Ecke wandert"),
                aufgabe=auf, loesung="; ".join(zeilen) + ".",
                pruef=pz(k)))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (1, 1):
            out.append(umschreiben(
                r,
                aufgabe=("Ein Körper hat die Ecken $P(2 | 4 | 1)$ und "
                         "$Q(1 | 2 | 2)$. Die Ebene $E_k: kx + y + 2z = 8$ "
                         "soll die Ecke $P$ enthalten. Jana rechnet: $P$ "
                         "einsetzen: $2k + 4 + 2 = 8$; auflösen: $2k = 2$, "
                         "also $k = 1$. Prüfe, ob Jana richtig gerechnet "
                         "hat."),
                loesung=("Richtig. Eingesetzt wird die Ecke, die in der "
                         "Ebene liegen soll, also $P$ und nicht $Q$; mit "
                         "$k = 1$ ist die Gleichung für $P$ erfüllt."),
                pruef=""))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (1, 3):
            out.append(umschreiben(
                r,
                aufgabe=("Die Ebene $E: 5x - 2y + z = 16$ enthält einen "
                         "Punkt, dessen drei Koordinaten übereinstimmen. "
                         "Vier Schüler geben ihn an: (1) $(4 | 4 | 4)$; "
                         "(2) $(4 | 2 | 4)$; (3) $(-4 | -4 | -4)$; "
                         "(4) $(4 | 4 | 0)$. Welche Ergebnisse können nicht "
                         "stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(2) kann nicht stimmen – die drei Koordinaten "
                         "sind nicht gleich; (3) kann nicht stimmen – "
                         "$5 - 2 + 1$ ist positiv und $16$ auch, also ist "
                         "die gemeinsame Koordinate positiv; (4) kann nicht "
                         "stimmen – die drei Koordinaten sind nicht "
                         "gleich."),
                pruef=""))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (2, 2):
            out.append(umschreiben(
                r,
                aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                         "falsch ist. Begründe. (1) Setzt man einen Punkt "
                         "in $E_k$ ein, erhält man immer genau einen Wert "
                         "für $k$. (2) In $r \\cdot y + s \\cdot z = 0$ "
                         "dürfen $r$ und $s$ nie beide null sein. (3) Es "
                         "gibt Ebenen, die keinen Punkt mit drei gleichen "
                         "Koordinaten enthalten."),
                loesung=("(1) falsch, z. B. fällt $k$ bei "
                         "$E_k: kx + y + z = 4$ und dem Punkt "
                         "$(0 | 1 | 3)$ heraus, $0 + 1 + 3 = 4$ gilt für "
                         "jedes $k$; (2) wahr, denn dann steht $0 = 0$ da, "
                         "das gilt für jeden Punkt – keine Ebene; (3) wahr, "
                         "denn z. B. ergäbe bei $x - y = 1$ ein Punkt mit "
                         "gleichen Koordinaten $0 = 1$."),
                pruef=""))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (2, 3):
            out.append(umschreiben(
                r,
                aufgabe=("Ole sagt: „$A(3 | 0 | 0)$ liegt in jeder Ebene "
                         "$E_k: 2x + ky - kz = 6$, also kann ich mit $A$ "
                         "den Wert von $k$ bestimmen.“ Begründe, ohne genau "
                         "zu rechnen, ob Ole recht hat."),
                loesung=("Nein; $k$ steht nur bei y und z, und diese "
                         "Koordinaten sind bei $A$ null – $k$ fällt heraus, "
                         "eingesetzt bleibt eine wahre Aussage für jedes "
                         "$k$, keine Gleichung für $k$."),
                pruef=""))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


# --- e3 ------------------------------------------------------------------

def e3():
    rows = lade("e3")
    out = []
    kopf = ("Die Dreieckspyramide $OABC$ hat die Ecken $O(0 | 0 | 0)$, "
            "$A(10 | 0 | 0)$, $B(0 | 5 | 0)$ und $C(0 | 0 | 10)$; ihre "
            "Seitenfläche $ABC$ liegt in $E: x + 2y + z = 10$. ")
    geraden = {
        1: ("durch $A$ und $B$", "g", "t", (10, 0, 0), (-2, 1, 0)),
        2: ("durch $A$ und $C$", "g", "t", (10, 0, 0), (-1, 0, 1)),
        3: ("durch $A$ und den Mittelpunkt $M(0 | 2{,}5 | 5)$ der Kante "
            "$BC$", "g", "t", (10, 0, 0), (-4, 1, 2)),
        4: ("durch $B$ und den Mittelpunkt $N(5 | 0 | 5)$ der Kante $CA$",
            "g", "t", (0, 5, 0), (1, -1, 1)),
        5: (None, "s", "r", (0, 5, 0), (0, -1, 2)),
    }

    def komp(p, u, par):
        out = []
        for a, b in zip(p, u):
            if b == 0:
                out.append(str(a))
            elif a == 0:
                out.append(f"{'' if b == 1 else '-' if b == -1 else b}{par}")
            else:
                sg = "+" if b > 0 else "-"
                bb = abs(b)
                out.append(f"{a} {sg} {'' if bb == 1 else bb}{par}")
        return out

    for r in rows:
        if r["kette_nr"] == 1 and r["sprosse"] == 0:
            out.append(nachziehen(r, sprosse_text=TEXT["e3s0"]))
        elif r["kette_nr"] == 1 and r["sprosse"] == 1:
            v = r["variante"]
            text, n, par, p, u = geraden[v]
            gl = f"${n}: \\vec{{x}} = {T(*p)} + {par} \\cdot {T(*u)}$"
            x, y, z = komp(p, u, par)
            gp = f"$({x} | {y} | {z})$"

            def kl(s):
                return f"({s})" if (" " in s or s.startswith("-")) else s
            eins = f"${kl(x)} + 2 \\cdot {kl(y)} + {kl(z)} = 10$"
            if v == 5:
                auf = (kopf + f"Die Gerade {gl} liegt in der Seitenfläche "
                       "$OBC$, also in der Ebene $x = 0$. Weise nach, dass "
                       "$s$ auch in $E$ liegt. (Abitur 2021 GK)")
                schluss = ("Ergebnis: $s$ liegt in $E$; der Stützpunkt "
                           "allein hätte nicht gereicht.")
            else:
                auf = kopf + f"Weise nach, dass die Gerade {gl} {text} in $E$ liegt."
                schluss = f"Ergebnis: ${n}$ liegt in $E$."
            out.append(umschreiben(
                r,
                merkmal=("den allgemeinen Geradenpunkt einsetzen: der "
                         "Parameter fällt heraus, die Gleichung stimmt; "
                         "Pyramide und E bleiben, die Gerade wandert"),
                aufgabe=auf,
                loesung=(f"Geradenpunkt: {gp}; einsetzen: {eins}; "
                         f"zusammenfassen: $10 = 10$ für jedes ${par}$; "
                         + schluss),
                pruef="10"))
        elif r["kette_nr"] == 1 and r["sprosse"] == 6:
            v = r["variante"]
            kw = {"sprosse_text": TEXT["e3s6"]}
            if v == 1:
                umschreiben_ = True
                kw["loesung"] = (
                    "Skalarprodukt: $\\vec{u} \\cdot \\vec{n} = 2a - 2$; "
                    "Fall $a = 1$: Skalarprodukt null, Stützpunkt "
                    "$(1 | 0 | 1)$ einsetzen: $2 - 1 = 1$ – $g_1$ liegt in "
                    "$E$; Fall $a \\neq 1$: einsetzen: $2(1 + ra) - (a + "
                    "2r) = 1$; auflösen: $r = \\frac{1}{2}$; Schnittpunkt: "
                    "$S_a(1 + \\frac{a}{2} | 1 | a + 1)$; Kontrolle: "
                    "$2(1 + \\frac{a}{2}) - (a + 1) = 1$, die "
                    "Ebenengleichung ist erfüllt.")
                out.append(umschreiben(r, **kw))
            elif v == 2:
                kw["loesung"] = (
                    "Skalarprodukt: $\\vec{u} \\cdot \\vec{n} = 2 - a - 2 = "
                    "-a$; Fall $a = 0$: Skalarprodukt null, Stützpunkt "
                    "einsetzen: $1 + 2 = 3 \\neq 5$ – $g_0$ ist echt "
                    "parallel; Fall $a \\neq 0$: einsetzen: $3 - ar = 5$; "
                    "auflösen: $r = -\\frac{2}{a}$; Schnittpunkt: "
                    "$S_a(1 - \\frac{4}{a} | -2 | 1 + \\frac{2}{a})$; "
                    "Kontrolle: $1 - \\frac{4}{a} + 2 + 2 + \\frac{4}{a} = "
                    "5$, die Ebenengleichung ist erfüllt.")
                out.append(umschreiben(r, **kw))
            else:
                out.append(nachziehen(r, **kw))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (1, 2):
            out.append(umschreiben(
                r,
                aufgabe=("Gegeben sind $g: \\vec{x} = (2 | 1 | 0) + t "
                         "\\cdot (2 | -1 | 3)$ und $E: x + 2y - z = 4$. "
                         "Vier Schüler geben die Lage an: (1) $g$ liegt in "
                         "$E$; (2) $g$ ist echt parallel zu $E$; (3) $g$ "
                         "schneidet $E$ im Punkt $(0 | 2 | -3)$; (4) $g$ "
                         "schneidet $E$ in genau einem Punkt. Welche "
                         "Ergebnisse können nicht stimmen? Begründe, ohne "
                         "genau zu rechnen."),
                loesung=("(1) und (2) können nicht stimmen – "
                         "$\\vec{u} \\cdot \\vec{n} = 2 - 2 - 3$ ist nicht "
                         "null, $g$ ist nicht parallel zu $E$; (3) kann "
                         "nicht stimmen – der Punkt erfüllt die Gleichung "
                         "von $E$ nicht, denn $0 + 4 + 3$ ist nicht $4$."),
                pruef=""))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (1, 3):
            out.append(umschreiben(
                r,
                aufgabe=("Für $t > 0$ hat die Pyramide die Grundfläche "
                         "$A(0 | 0 | 0)$, $B_t(t | 0 | 0)$, $C_t(t | t | 0)$, "
                         "$D_t(0 | t | 0)$ und die Spitze "
                         "$S_t(\\frac{t}{2} | \\frac{t}{2} | 2)$; "
                         "$E: x + z = 5$. Gesucht sind die $t$, für die "
                         "Pyramide und $E$ gemeinsame Punkte haben. Tom "
                         "rechnet: $A$ einsetzen: $0 < 5$; $B_t$ und $C_t$ "
                         "einsetzen: $t$; Spitze einsetzen: "
                         "$\\frac{t}{2} + 2$; die Grundfläche erreicht $5$ "
                         "bei $t = 5$, die Spitze erst bei $t = 6$; also "
                         "gemeinsame Punkte für $t \\ge 5$. Prüfe, ob Tom "
                         "richtig gerechnet hat."),
                loesung=("Richtig. Weil $A$ unter $E$ liegt, gibt es "
                         "gemeinsame Punkte, sobald eine Ecke $x + z \\ge 5$ "
                         "erreicht – Grundfläche und Spitze sind beide "
                         "geprüft."),
                pruef=""))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (2, 2):
            out.append(umschreiben(
                r,
                aufgabe=("Jonas sagt: „Bei $g$ und $E$ ist "
                         "$\\vec{u} \\cdot \\vec{n} = 0$, also ist $g$ echt "
                         "parallel zu $E$.“ Begründe, ohne genau zu "
                         "rechnen, ob Jonas recht hat."),
                loesung=("Nein; aus $\\vec{u} \\cdot \\vec{n} = 0$ folgt nur, "
                         "dass $g$ parallel zu $E$ ist oder in $E$ liegt – "
                         "erst die Punktprobe des Stützpunkts entscheidet."),
                pruef=""))
        elif r["kette_nr"] == 2 and (r["sprosse"], r["variante"]) == (2, 3):
            out.append(umschreiben(
                r,
                aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                         "falsch ist. Begründe. (1) Ist das Skalarprodukt "
                         "von Richtungs- und Normalenvektor nicht null, "
                         "schneidet die Gerade die Ebene immer in genau "
                         "einem Punkt. (2) Liegt der Stützpunkt einer "
                         "Geraden in der Ebene, liegt immer die ganze "
                         "Gerade in der Ebene. (3) Eine Gerade, die echt "
                         "parallel zu einer Ebene ist, hat nie einen Punkt "
                         "mit ihr gemeinsam."),
                loesung=("(1) wahr, denn beim Einsetzen bleibt der "
                         "Parameter stehen und liefert genau einen Wert; "
                         "(2) falsch, z. B. liegt der Stützpunkt von "
                         "$\\vec{x} = (1 | 1 | 0) + t \\cdot (0 | 0 | 1)$ in "
                         "der Ebene $z = 0$, die übrigen Punkte liegen "
                         "darüber; (3) wahr, denn beim Einsetzen fällt der "
                         "Parameter heraus und es bleibt eine falsche "
                         "Aussage."),
                pruef=""))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


# --- e4 ------------------------------------------------------------------

def e4():
    rows = lade("e4")
    out = []
    kopf = ("Die rechte Wand einer Bühnenkulisse liegt in der Ebene "
            "$y = 8$ und reicht von $x = 0$ bis $x = 5$ und von $z = 0$ bis "
            "$z = 3$ (1 LE = 1 m). Eine Lampe hängt in $L(1 | 0 | 6)$. ")
    L = (1, 0, 6)
    pkt = {1: ("P", (3, 4, 5), "die Spitze $P(3 | 4 | 5)$ einer Stange"),
           2: ("P", (1, 2, 5), "den Knauf $P(1 | 2 | 5)$ eines Stuhls"),
           3: ("P", (0, 4, 3), "die Ecke $P(0 | 4 | 3)$ eines Tisches"),
           4: ("P", (2, 2, 4), "die Spitze $P(2 | 2 | 4)$ einer Figur"),
           5: ("S", (2, 4, 4), "die Spitze $S(2 | 4 | 4)$ eines Aufbaus")}
    for r in rows:
        if r["kette_nr"] == 1 and r["sprosse"] == 0:
            out.append(nachziehen(r, sprosse_text=TEXT["e4s0"]))
        elif r["kette_nr"] == 1 and r["sprosse"] == 1:
            v = r["variante"]
            n, p, text = pkt[v]
            u = tuple(a - b for a, b in zip(p, L))
            t = Fraction(8, u[1])
            q = tuple(Fraction(a) + t * b for a, b in zip(L, u))
            qs = T(*[int(c) for c in q])
            prob = []
            if not 0 <= q[0] <= 5:
                prob.append(f"$x = {int(q[0])}$ liegt nicht zwischen $0$ "
                            "und $5$")
            if not 0 <= q[2] <= 3:
                prob.append(f"$z = {int(q[2])}$ liegt nicht zwischen $0$ "
                            "und $3$")
            if prob:
                pruefz = "Wandmaße prüfen: " + " und ".join(prob)
                erg = f"Ergebnis: Der Schatten von ${n}$ liegt nicht auf der Wand."
            else:
                pruefz = (f"Wandmaße prüfen: $0 \\le {int(q[0])} \\le 5$ und "
                          f"$0 \\le {int(q[2])} \\le 3$")
                erg = f"Ergebnis: Der Schatten von ${n}$ liegt auf der rechten Wand."
            frage = (f"Sie beleuchtet {text}. Untersuche rechnerisch, ob "
                     f"der Schatten von ${n}$ auf der rechten Wand liegt.")
            if v == 5:
                frage += " (Abitur 2020 LK)"
            out.append(umschreiben(
                r,
                merkmal=("Lichtgerade mit der Wandebene schneiden, dann die "
                         "Koordinaten gegen die Wandmaße prüfen; Wand und "
                         "Lampe bleiben, der Punkt wandert"),
                aufgabe=kopf + frage,
                loesung=(f"Lichtgerade: $\\vec{{x}} = {T(*L)} + t \\cdot "
                         f"{T(*u)}$; Bedingung $y = 8$: ${u[1]}t = 8$, also "
                         f"$t = {int(t)}$; Schattenpunkt: ${qs}$; "
                         f"{pruefz}; {erg}"),
                pruef=str([int(c) for c in q])))
        elif r["kette_nr"] == 3 and (r["sprosse"], r["variante"]) == (1, 2):
            out.append(umschreiben(
                r,
                aufgabe=("Ein Ball fliegt nach dem Schlag auf "
                         "$X_t(2 | 4t + 1 | -5t^2 + 9t + 2)$, $t$ in "
                         "Sekunden, die dritte Koordinate ist die Höhe über "
                         "dem Boden. Vier Schüler geben den Auftreffpunkt "
                         "auf dem Boden an: (1) $(2 | 9 | 0)$; "
                         "(2) $(2 | 9 | 0{,}5)$; (3) $(3 | 9 | 0)$; "
                         "(4) $(2 | 0{,}2 | 0)$. Welche Ergebnisse können "
                         "nicht stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(2) kann nicht stimmen – auf dem Boden ist die "
                         "Höhe null; (3) kann nicht stimmen – die erste "
                         "Koordinate ist immer $2$; (4) kann nicht stimmen – "
                         "nach dem Schlag ist $t > 0$, also die zweite "
                         "Koordinate $4t + 1$ größer als $1$."),
                pruef=""))
        elif r["kette_nr"] == 3 and (r["sprosse"], r["variante"]) == (1, 3):
            out.append(umschreiben(
                r,
                aufgabe=("Eine Hauswand liegt in der xz-Ebene mit "
                         "$-4 \\le x \\le 0$ und $0 \\le z \\le 3$. Schritt I "
                         "liefert den Schattenpunkt $(-2 | 0 | 1)$ einer "
                         "Ecke, Schritt II lautet: $-4 < -2 < 0$ und "
                         "$0 < 1 < 3$. Jan schreibt: Schritt II zeigt, dass "
                         "der Schatten der Ecke auf der Hauswand liegt. "
                         "Prüfe, ob Jan richtig gedeutet hat."),
                loesung=("Richtig. Schritt II vergleicht die Koordinaten "
                         "des Schattenpunkts mit den Maßen der Wand; beide "
                         "liegen innerhalb, also fällt der Schatten auf "
                         "die Wand."),
                pruef=""))
        elif r["kette_nr"] == 3 and (r["sprosse"], r["variante"]) == (2, 1):
            out.append(umschreiben(
                r,
                aufgabe=("Mara sagt: „Ob der Ball das Netz berührt, "
                         "entscheidet die größte Höhe seiner Bahn.“ "
                         "Begründe, ohne genau zu rechnen, ob Mara recht "
                         "hat."),
                loesung=("Nein; das Netz steht nur in der Netzebene – "
                         "entscheidend ist die Höhe des Balls im "
                         "Durchstoßpunkt der Bahn mit der Netzebene, "
                         "verglichen mit der Netzhöhe; wo die Bahn am "
                         "höchsten ist, spielt keine Rolle."),
                pruef=""))
        elif r["kette_nr"] == 3 and (r["sprosse"], r["variante"]) == (2, 3):
            out.append(umschreiben(
                r,
                aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                         "falsch ist. Begründe. (1) Hat die Lichtgerade "
                         "einen Durchstoßpunkt mit der Wandebene, liegt der "
                         "Schatten immer auf der Wand. "
                         "(2) Beginnt die Zeit beim Schlag, passt beim "
                         "Auftreffen eines Balls nie die negative Lösung "
                         "der quadratischen Gleichung. (3) Es gibt "
                         "Lichtgeraden, die eine Wandebene gar nicht "
                         "treffen."),
                loesung=("(1) falsch, z. B. liegt $(6 | 5 | 0)$ in der "
                         "Ebene $y = 5$, aber neben einer Wand mit "
                         "$0 \\le x \\le 4$ – die Ebene ist unbegrenzt, die "
                         "Wand nicht; (2) wahr, denn eine negative Zeit "
                         "läge vor dem Schlag; (3) wahr, denn fällt das "
                         "Licht parallel zur Wand, gibt es keinen "
                         "Durchstoßpunkt."),
                pruef=""))
        else:
            out.append(nachziehen(r))
    return out, len(rows)


def zahlen(out, alt):
    z = {"uebernommen": 0, "neu": 0, "umgeschrieben": 0, "dublette": 0}
    for r in out:
        z[r["_art"]] += 1
        z["dublette"] += 1 if r.get("_dubl") else 0
    z["entfallen"] = alt - z["uebernommen"] - z["umgeschrieben"]
    return z


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["e1", "e2", "e3", "e4"]
    fn = {"e1": e1, "e2": e2, "e3": e3, "e4": e4}
    tmp = B / "_tmp"
    tmp.mkdir(exist_ok=True)
    zf = tmp / "zahlen.json"
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

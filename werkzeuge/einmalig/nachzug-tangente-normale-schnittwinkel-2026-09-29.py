"""Nachzug bank/tangente-normale-schnittwinkel auf Katalog f038ccb (Mappe 29.09.).

Einmalig, 2026-09-29. Liest den Bestand (Katalog 95b0f8b, 27./28.09.),
zieht quelle (120–124 -> 117–121), sprosse, id und sprosse_text nach,
schreibt die Päckchen (je Verfahrenskette 5), die neuen Vorstufen
(e1 s0 „nur den Anstieg“, e4 s0 „Welcher Winkel?“; die alten s0 werden
s−1), die fehlenden Originalzeilen der Prüfungssprossen (e1, e3) und die
Pflichtformen (P1, P2, P4, P6) und schreibt je Einheit die ganze Datei
neu. Zählt je Einheit übernommen/neu/umgeschrieben/entfallen.
Aufruf aus der Wurzel des Repos:
    python3 werkzeuge/einmalig/nachzug-tangente-normale-schnittwinkel-2026-09-29.py [e1 …]
"""
import copy
import json
import sys
from pathlib import Path

E = "tangente-normale-schnittwinkel"
B = Path("bank") / E
QMAP = {120: 117, 121: 118, 122: 119, 123: 120, 124: 121}
ZAEHL = {}

M_FEHLER = ("Rechnung prüfen: Fehler finden, richtige Rechnung erkennen, "
            "unmögliche Ergebnisse erkennen")
M_BEGR = ("begründen: Regel beim Namen, Aussagen beurteilen, "
          "Behauptung beurteilen")

T_E1_SM1 = ("„Was ist gegeben?“ ankreuzen: Punkt gegeben (ableiten und "
            "einsetzen), Steigung gegeben (f'(x) = m lösen) oder Winkel "
            "gegeben oder gesucht (erst über den Tangens in eine Steigung "
            "übersetzen); nichts rechnen")
T_E1_S0 = ("nur den Anstieg: zu Funktion und Stelle f'(x₀) ausrechnen, "
           "Antwortgerüst m = (Lücke), keine Gerade aufstellen")
T_E2_S0 = ("„Berühren oder schneiden?“ – zu Gerade und Graph ankreuzen, ob "
           "die Gerade den Graphen berührt (Funktionswert und Steigung "
           "stimmen überein) oder nur schneidet (nur der Funktionswert), und "
           "welche der beiden Bedingungen im Text schon belegt ist; nichts "
           "rechnen")
T_E3_S0 = ("„Tangente oder Normale?“ – ankreuzen, welche Gerade gebraucht "
           "wird und welche Steigung sie hat: die Tangente den "
           "Ableitungswert, die Normale den negativen Kehrwert; nichts "
           "rechnen")
T_E4_S0 = ("„Welcher Winkel?“ – ankreuzen, ob der Steigungswinkel gegen die "
           "positive x-Richtung (null bis hundertachtzig Grad) oder der "
           "Schnittwinkel (höchstens neunzig Grad) gefragt ist; nichts "
           "rechnen")

FELDER = ["id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
          "sprosse_text", "merkmal", "hoehe", "pflicht", "variante",
          "aufgabe", "form", "antwort", "loesung", "pruef", "original",
          "grafik", "loesungsgrafik", "quelle"]
NACHGEZOGEN = ("id", "sprosse", "kette_nr", "quelle", "sprosse_text",
               "hoehe", "_neu")


def lade(n):
    return [json.loads(z) for z in
            (B / f"e{n}.jsonl").read_text(encoding="utf-8").splitlines()]


def nimm(zeilen, k, s):
    return [copy.deepcopy(a) for a in zeilen
            if a["kette_nr"] == k and a["sprosse"] == s]


def neu(vorlage, **kw):
    """Neue Zeile einer neuen Sprosse oder neue Variante (zählt als neu)."""
    a = copy.deepcopy(vorlage)
    if kw.get("hoehe", a["hoehe"]) != "pflicht":
        a.pop("pflicht", None)
    a.update(kw)
    a["_neu"] = True
    return a


def um(vorlage, **kw):
    """Bestandszeile umschreiben (ersetzt sie, zählt als umgeschrieben)."""
    a = copy.deepcopy(vorlage)
    a.update(kw)
    return a


def orig(i, j, p):
    return {"id": i, "jahr": j, "papier": p}


def varianten(zeilen):
    for i, a in enumerate(zeilen, 1):
        a["variante"] = i
    return zeilen


def ordne(zeilen, einheit):
    aus = []
    for a in zeilen:
        a["quelle"] = QMAP.get(a["quelle"], a["quelle"])
        a["id"] = (f"{E}-e{einheit}-k{a['kette_nr']}"
                   f"-s{a['sprosse']}-v{a['variante']}")
        aus.append({f: a[f] for f in FELDER if f in a} |
                   ({"_neu": True} if a.get("_neu") else {}))
    return aus


def zaehle(n, alt, zeilen):
    def kern(a):
        return json.dumps({k: v for k, v in a.items()
                           if k not in NACHGEZOGEN}, sort_keys=True,
                          ensure_ascii=False)
    bestand = {kern(a) for a in alt}
    ueb = sum(1 for a in zeilen if not a.get("_neu") and kern(a) in bestand)
    nn = sum(1 for a in zeilen if a.get("_neu"))
    umg = len(zeilen) - ueb - nn
    ZAEHL[f"e{n}"] = dict(uebernommen=ueb, neu=nn, umgeschrieben=umg,
                          entfallen=len(alt) - ueb - umg)


def schreibe(n, alt, zeilen):
    zeilen = ordne(zeilen, n)
    zaehle(n, alt, zeilen)
    for a in zeilen:
        a.pop("_neu", None)
    text = "".join(json.dumps(a, ensure_ascii=False) + "\n" for a in zeilen)
    (B / f"e{n}.jsonl").write_text(text, encoding="utf-8")


def rest(alt, *schluessel):
    """Bestandszeilen der Gruppen (k, s) unverändert (Kopie)."""
    aus = []
    for k, s in schluessel:
        aus += nimm(alt, k, s)
    return aus


def pflicht_merkmal(zeilen):
    for a in zeilen:
        a["merkmal"] = M_FEHLER if a["pflicht"] == "fehler" else M_BEGR
    return zeilen


# ---------------------------------------------------------------- e1
def e1():
    alt = lade(1)
    aus = []
    # s0 -> s-1, übernommen, sprosse_text vollständig
    for a in nimm(alt, 1, 0):
        a["sprosse"] = -1
        a["sprosse_text"] = T_E1_SM1
        aus.append(a)
    g = nimm(alt, 1, 1)[0]
    # neue Vorstufe s0: derselbe Term x³ + c·x² − 2 wie im Grundfall,
    # an der Stelle −1
    m0 = ("nur der Anstieg f'(−1) derselben Funktion x³ + c·x² − 2 wie im "
          "Grundfall, keine Gerade")
    s0 = []
    for c, term, abl, rech, m in [
            (1, "x^3 + x^2 - 2", "3x^2 + 2x", "3 - 2", 1),
            (2, "x^3 + 2x^2 - 2", "3x^2 + 4x", "3 - 4", -1),
            (-1, "x^3 - x^2 - 2", "3x^2 - 2x", "3 + 2", 5),
            (3, "x^3 + 3x^2 - 2", "3x^2 + 6x", "3 - 6", -3)]:
        s0.append(neu(
            g, sprosse=0, hoehe="vorstufe", sprosse_text=T_E1_S0, merkmal=m0,
            aufgabe=(f"Gegeben ist $f(x) = {term}$. Berechne den Anstieg des "
                     "Graphen von $f$ an der Stelle $x_0 = -1$."),
            form="teil", antwort="$m =$ __",
            loesung=(f"Ableitung bilden: $f'(x) = {abl}$; Stelle einsetzen: "
                     f"$m = f'(-1) = {rech} = {m}$"),
            pruef=str(m), original=None, grafik="", loesungsgrafik=""))
    aus += varianten(s0)
    # Grundfall als Päckchen: f(x) = x³ + c·x² − 2, Stelle 1 fest, c wandert
    m1 = ("Tangente an x³ + c·x² − 2 im Punkt an der Stelle 1: ableiten, "
          "einsetzen, n aus dem Punkt; die Stelle 1 bleibt, der Faktor c "
          "vor x² wandert")
    gf = []
    for c, term, abl, m, fw, nn, t, kenn in [
            (1, "x^3 + x^2 - 2", "3x^2 + 2x", 5, 0, -5, "5x - 5", None),
            (2, "x^3 + 2x^2 - 2", "3x^2 + 4x", 7, 1, -6, "7x - 6", None),
            (-1, "x^3 - x^2 - 2", "3x^2 - 2x", 1, -2, -3, "x - 3", None),
            (3, "x^3 + 3x^2 - 2", "3x^2 + 6x", 9, 2, -7, "9x - 7", None),
            (-2, "x^3 - 2x^2 - 2", "3x^2 - 4x", -1, -3, -2, "-x - 2",
             orig("2025-bebb-gk-A1.1a", 2025, "2025-bebb-gk"))]:
        auf = (f"Gegeben ist $f(x) = {term}$. Bestimme die Gleichung der "
               "Tangente an den Graphen von $f$ im Punkt $P(1 | f(1))$.")
        if kenn:
            auf += " (Abitur 2025 GK)"
        gf.append(um(
            g, merkmal=m1, aufgabe=auf, form="teil", antwort="$t(x) =$ __",
            loesung=(f"Anstieg: $f'(x) = {abl}$, $m = f'(1) = {m}$; "
                     f"n aus P: $f(1) = {fw}$, ${fw} = {m} \\cdot 1 + n$, "
                     f"also $n = {nn}$; Tangente: $t(x) = {t}$"),
            pruef=f"[{m}, {fw}, {nn}]", original=kenn, grafik="",
            loesungsgrafik=""))
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 10)])
    # Prüfungssprosse: Bestand v1–v6, dazu je Original zwei Zeilen
    pr = nimm(alt, 1, 10)
    v = pr[0]
    pr.append(neu(
        v, aufgabe=("Für $a > 0$ ist $f_a(x) = a \\cdot x^5$. Weise nach, "
                    "dass die Tangente an den Graphen von $f_a$ im Punkt "
                    "$(u | f_a(u))$ die $y$-Achse im Punkt $(0 | -4f_a(u))$ "
                    "schneidet. (Abitur 2024 LK)"),
        antwort="",
        loesung=("Anstieg: $m = f_a'(u) = 5au^4$; n aus P: $f_a(u) = m "
                 "\\cdot u + n$, also $n = au^5 - 5au^5 = -4au^5$; Ergebnis: "
                 "$n = -4f_a(u)$ – für jedes $u$, nicht nur an einem "
                 "Beispiel."),
        pruef="[5, -4]", original=orig("2024-bebb-lk-A1.5b", 2024,
                                       "2024-bebb-lk")))
    pr.append(neu(
        v, aufgabe=("Für $a > 0$ ist $f_a(x) = a \\cdot x^6$. Weise nach, "
                    "dass die Tangente an den Graphen von $f_a$ im Punkt "
                    "$(u | f_a(u))$ mit $u \\ne 0$ die $x$-Achse an der "
                    "Stelle $\\frac{5}{6}u$ schneidet. (Abitur 2024 LK)"),
        antwort="",
        loesung=("Anstieg: $m = f_a'(u) = 6au^5$; Tangente aus P: $t(x) = "
                 "6au^5 \\cdot (x - u) + au^6$; Nullstelle: $t(x) = 0 "
                 "\\Leftrightarrow x - u = -\\frac{au^6}{6au^5} = "
                 "-\\frac{u}{6}$, also $x = \\frac{5}{6}u$ – für jedes "
                 "$u \\ne 0$."),
        pruef="[6, 5]", original=orig("2024MerhoehtAAnalysis21-b", 2024,
                                      "2024-iqb-ea")))
    for term, a_, b_, punkt, probe, falsch, abl, mrech, m, nrech, nn, t, pz \
            in [("-x^3 + 2x^2 + 5x - 3", "A(2 | 7)", "B(-1 | 1)", "A",
                 "f(2) = -8 + 8 + 10 - 3 = 7", "f(-1) = -5 \\ne 1",
                 "-3x^2 + 4x + 5", "-12 + 8 + 5", 1, "7 = 1 \\cdot 2 + n",
                 5, "x + 5", "[7, -5, 1, 5]"),
                ("x^4 - 2x^3 + 3x - 1", "A(-1 | 1)", "B(2 | 5)", "B",
                 "f(2) = 16 - 16 + 6 - 1 = 5", "f(-1) = -1 \\ne 1",
                 "4x^3 - 6x^2 + 3", "32 - 24 + 3", 11,
                 "5 = 11 \\cdot 2 + n", -17, "11x - 17",
                 "[5, -1, 11, -17]")]:
        anders = "B" if punkt == "A" else "A"
        pr.append(neu(
            v, aufgabe=(f"Gegeben sind $f(x) = {term}$ und die Punkte "
                        f"${a_}$ und ${b_}$. Genau einer der Punkte liegt "
                        "auf dem Graphen von $f$. Welcher ist es? Bestimme "
                        "die Gleichung der Tangente an den Graphen in diesem "
                        "Punkt. (FHR 2026)"),
            antwort="Punkt: __, $t(x) =$ __",
            loesung=(f"Punktprobe: ${probe}$, ${punkt}$ liegt auf dem "
                     f"Graphen; ${falsch}$, ${anders}$ nicht; Anstieg: "
                     f"$f'(x) = {abl}$, $m = f'(2) = {mrech} = {m}$; n aus "
                     f"P: ${nrech}$, also $n = {nn}$; Tangente: "
                     f"$t(x) = {t}$"),
            pruef=pz, original=orig("2026-C-1d", 2026, "C")))
    aus += varianten(pr)
    aus += rest(alt, (2, 1), (3, 1))
    # Pflicht fehler: v1 Schülerrechnung (Bestand), v2 P2, v3 P1
    fe = pflicht_merkmal(nimm(alt, 4, 1))
    fe[1] = um(
        fe[1], aufgabe=("Zu $f(x) = x^3 - 4x$ und der Stelle $x_0 = 2$ "
                        "rechnet Ela die Tangente so: \\rechnung{f(2) &= 0 "
                        "\\\\ m &= f'(2) = 8 \\\\ 0 &= 8 \\cdot 2 + n \\\\ n "
                        "&= -16 \\\\ t(x) &= 8x - 16} Prüfe, ob Ela richtig "
                        "gerechnet hat."),
        loesung=("Richtig. Die Steigung ist der Ableitungswert $f'(2)$, "
                 "nicht der Funktionswert, und $n$ kommt aus der "
                 "Punktbedingung mit dem Berührpunkt."),
        pruef="")
    fe[2] = um(
        fe[2], aufgabe=("Drei Schüler haben die Tangente an den Graphen von "
                        "$f(x) = x^2 + 2x$ im Punkt $P(1 | 3)$ angegeben. "
                        "Welche Ergebnisse können nicht stimmen? Begründe, "
                        "ohne genau zu rechnen. \\\\ (1) $t(x) = 4x - 1$ "
                        "\\\\ (2) $t(x) = -4x + 7$ \\\\ (3) $t(x) = 4x + 3$"),
        loesung=("Nicht stimmen können (2) und (3). (2): Der Graph steigt "
                 "bei $x = 1$ (nach oben geöffnete Parabel, Scheitel links "
                 "davon), die Tangente kann dort nicht fallen. (3): Die "
                 "Tangente muss durch $P$ gehen, aber $4 \\cdot 1 + 3$ ist "
                 "nicht $3$. (1) kann stimmen."),
        pruef="")
    aus += fe
    # Pflicht begründen: v1 Begründe warum (Bestand), v2 P4, v3 P6
    be = pflicht_merkmal(nimm(alt, 4, 2))
    be[1] = um(
        be[1], aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                        "falsch ist. Begründe. \\\\ (1) Hat der Graph von "
                        "$f$ an der Stelle $x_0$ eine waagerechte Tangente, "
                        "so ist immer $f'(x_0) = 0$. \\\\ (2) Eine Tangente "
                        "hat mit dem Graphen immer genau einen gemeinsamen "
                        "Punkt. \\\\ (3) Parallele Tangenten an denselben "
                        "Graphen haben immer dieselbe Steigung."),
        loesung=("(1) wahr, denn eine waagerechte Gerade hat die Steigung "
                 "$0$, und die Tangentensteigung ist $f'(x_0)$. (2) falsch, "
                 "z. B. trifft die Tangente $y = 12x - 16$ an $f(x) = x^3$ "
                 "bei $x = 2$ den Graphen auch bei $x = -4$. (3) wahr, denn "
                 "parallele Geraden haben dieselbe Steigung."),
        pruef="")
    be[2] = um(
        be[2], aufgabe=("Tim sagt: „Die Tangente im Punkt $(2 | f(2))$ hat "
                        "die Steigung $f(2)$, weil sie durch diesen Punkt "
                        "geht.“ Begründe, ohne zu rechnen, ob Tim recht "
                        "hat."),
        loesung=("Nein; der Punkt legt nur fest, wo die Tangente liegt, "
                 "ihre Steigung ist die des Graphen an der Stelle $2$, also "
                 "der Ableitungswert $f'(2)$, nicht die Höhe $f(2)$."),
        pruef="")
    aus += be
    schreibe(1, alt, aus)


# ---------------------------------------------------------------- e2
def e2():
    alt = lade(2)
    aus = []
    for a in nimm(alt, 1, 0):
        a["sprosse_text"] = T_E2_S0
        aus.append(a)
    g = nimm(alt, 1, 1)[0]
    m1 = ("Gerade und Stelle 1 gegeben, f(x) = x³ + c·x − 1: Funktionswert "
          "und Steigung vergleichen; die Stelle 1 bleibt, der Faktor c vor "
          "x wandert")
    gf = []
    for term, gx, loes, pz, kenn in [
            ("x^3 + x - 1", "4x - 3",
             "Ja; Bedingung Funktionswert: $f(1) = 1 + 1 - 1 = 1 = g(1)$; "
             "Bedingung Steigung: $f'(x) = 3x^2 + 1$, $f'(1) = 4$ = Steigung "
             "von $g$; Ergebnis: beide Bedingungen erfüllt, $g$ ist "
             "Tangente.", "[1, 4]", None),
            ("x^3 - 2x - 1", "x - 1",
             "Nein; Bedingung Funktionswert: $f(1) = 1 - 2 - 1 = -2$, aber "
             "$g(1) = 0$; Bedingung Steigung: $f'(x) = 3x^2 - 2$, "
             "$f'(1) = 1$ = Steigung von $g$; Ergebnis: nur die Steigung "
             "stimmt, $g$ ist nur parallel zur Tangente.", "[-2, 0, 1]",
             None),
            ("x^3 + 2x - 1", "5x - 3",
             "Ja; Bedingung Funktionswert: $f(1) = 1 + 2 - 1 = 2 = g(1)$; "
             "Bedingung Steigung: $f'(x) = 3x^2 + 2$, $f'(1) = 5$ = Steigung "
             "von $g$; Ergebnis: beide Bedingungen erfüllt, $g$ ist "
             "Tangente.", "[2, 5]", None),
            ("x^3 - x - 1", "-x",
             "Nein; Bedingung Funktionswert: $f(1) = 1 - 1 - 1 = -1 = g(1)$; "
             "Bedingung Steigung: $f'(x) = 3x^2 - 1$, $f'(1) = 2$, aber $g$ "
             "hat die Steigung $-1$; Ergebnis: nur ein gemeinsamer Punkt, "
             "$g$ schneidet den Graphen.", "[-1, 2]", None),
            ("x^3 - 4x - 1", "-x - 3",
             "Ja; Bedingung Funktionswert: $f(1) = 1 - 4 - 1 = -4 = g(1)$; "
             "Bedingung Steigung: $f'(x) = 3x^2 - 4$, $f'(1) = -1$ = "
             "Steigung von $g$; Ergebnis: beide Bedingungen erfüllt (nicht "
             "nur den Anstieg prüfen), $g$ ist Tangente.", "[-4, -1]",
             orig("2026-B-1g", 2026, "B"))]:
        auf = (f"Ist $g(x) = {gx}$ Tangente an den Graphen von "
               f"$f(x) = {term}$ an der Stelle $x = 1$?")
        if kenn:
            auf += " Weise es rechnerisch nach. (FHR 2026)"
        gf.append(um(g, merkmal=m1, aufgabe=auf, loesung=loes, pruef=pz,
                     original=kenn))
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 10)])
    aus += rest(alt, (2, 1), (3, 1), (4, 1))
    fe = pflicht_merkmal(nimm(alt, 5, 1))
    fe[1] = um(
        fe[1], aufgabe=("Die Tangente an den Graphen von $f(x) = x^3 - 3x^2 "
                        "+ 4$ an der Stelle $x = 2$ ist $y = 0$. Nina sucht "
                        "weitere gemeinsame Punkte: \\rechnung{x^3 - 3x^2 + "
                        "4 &= 0 \\\\ (x - 2)^2 \\cdot (x + 1) &= 0} Sie "
                        "schreibt: „Außer der Berührstelle $2$ gibt es nur "
                        "noch die Stelle $-1$.“ Prüfe, ob Nina richtig "
                        "gerechnet hat."),
        loesung=("Richtig. Die Berührstelle $2$ ist doppelte Nullstelle der "
                 "Differenz $f(x) - t(x)$; die einzige weitere Nullstelle "
                 "$-1$ gibt den weiteren gemeinsamen Punkt."),
        pruef="")
    fe[2] = um(
        fe[2], aufgabe=("Drei Schüler haben untersucht, ob die Gerade "
                        "$g(x) = 2x$ den Graphen von $f(x) = x^2 + 1$ "
                        "berührt, und die Berührstelle angegeben. Welche "
                        "Ergebnisse können nicht stimmen? Begründe, ohne "
                        "genau zu rechnen. \\\\ (1) Berührstelle $x = 1$ "
                        "\\\\ (2) Berührstelle $x = -1$ \\\\ (3) "
                        "Berührstellen $x = 1$ und $x = 3$"),
        loesung=("Nicht stimmen können (2) und (3). (2): Bei $x = -1$ ist "
                 "$g$ negativ, $f$ aber nie kleiner als $1$ – dort gibt es "
                 "keinen gemeinsamen Punkt. (3): Die Differenz $f(x) - g(x)$ "
                 "ist quadratisch und hat höchstens eine doppelte "
                 "Nullstelle, also höchstens eine Berührstelle. (1) kann "
                 "stimmen."),
        pruef="")
    aus += fe
    be = pflicht_merkmal(nimm(alt, 5, 2))
    be[1] = um(
        be[1], aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                        "falsch ist. Begründe. \\\\ (1) Hat eine Gerade mit "
                        "dem Graphen genau einen gemeinsamen Punkt, so ist "
                        "sie immer Tangente. \\\\ (2) Ist eine Gerade "
                        "Tangente an der Stelle $x_0$, so stimmen dort "
                        "Funktionswert und Steigung immer überein. \\\\ (3) "
                        "Jede Tangente an eine Parabel hat mit ihr nur den "
                        "Berührpunkt gemeinsam."),
        loesung=("(1) falsch, z. B. trifft $g(x) = x + 6$ den Graphen von "
                 "$f(x) = x^3$ nur bei $x = 2$, aber $f'(2) = 12$ ist nicht "
                 "die Steigung $1$. (2) wahr, denn das ist die "
                 "Doppelbedingung der Tangente. (3) wahr, denn die Differenz "
                 "aus Parabel und Tangente ist quadratisch mit doppelter "
                 "Nullstelle an der Berührstelle, eine weitere Nullstelle "
                 "hat sie nicht."),
        pruef="")
    be[2] = um(
        be[2], aufgabe=("Mia sagt: „Die Gerade $g$ hat an der Stelle $2$ "
                        "dieselbe Steigung wie der Graph von $f$. Also ist "
                        "$g$ dort Tangente.“ Begründe, ohne zu rechnen, ob "
                        "Mia recht hat."),
        loesung=("Nein; es fehlt die zweite Bedingung, der gemeinsame Punkt "
                 "$f(2) = g(2)$ – gleiche Steigung allein ergibt auch eine "
                 "Parallele zur Tangente."),
        pruef="")
    aus += be
    schreibe(2, alt, aus)


# ---------------------------------------------------------------- e3
def e3():
    alt = lade(3)
    aus = []
    for a in nimm(alt, 1, 0):
        a["sprosse_text"] = T_E3_S0
        aus.append(a)
    g = nimm(alt, 1, 1)[0]
    m1 = ("Tangentensteigung und Punkt gegeben: negativen Kehrwert bilden, "
          "Gerade durch den Punkt; der Punkt P(4 | 3) bleibt, die "
          "Tangentensteigung wandert")
    gf = []
    for mt, mn_rech, br, b, nx, pz in [
            ("2", "-\\frac{1}{2} = -0{,}5", "3 = -0{,}5 \\cdot 4 + b", "5",
             "-0{,}5x + 5", "[-0.5, 5]"),
            ("-2", "-\\frac{1}{-2} = 0{,}5", "3 = 0{,}5 \\cdot 4 + b", "1",
             "0{,}5x + 1", "[0.5, 1]"),
            ("4", "-\\frac{1}{4} = -0{,}25", "3 = -0{,}25 \\cdot 4 + b", "4",
             "-0{,}25x + 4", "[-0.25, 4]"),
            ("-1", "-\\frac{1}{-1} = 1", "3 = 1 \\cdot 4 + b", "-1",
             "x - 1", "[1, -1]"),
            ("0{,}5", "-\\frac{1}{0{,}5} = -2", "3 = -2 \\cdot 4 + b", "11",
             "-2x + 11", "[-2, 11]")]:
        gf.append(um(
            g, merkmal=m1,
            aufgabe=("Die Tangente an den Graphen von $f$ im Punkt "
                     f"$P(4 | 3)$ hat die Steigung ${mt}$. Bestimme die "
                     "Gleichung der Normalen in $P$."),
            loesung=(f"Normalensteigung: $m_n = {mn_rech}$; b aus P: "
                     f"${br}$, also $b = {b}$; Normale: $n(x) = {nx}$"),
            pruef=pz))
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 7)])
    pr = nimm(alt, 1, 7)
    mpr = ("vorgelegte Gleichung als Normalenbedingung deuten; "
           "fhr-Zielmarke: Normalengleichung mit Funktionswert und Anstieg")
    for a in pr:
        a["merkmal"] = mpr
    v = pr[0]
    for term, st, yp, fw_rech, abl, a_rech, a_, mn_rech, br, b, nx, pz, \
            kenn, kt in [
            ("2x^3 - x^2 - 4x + 5", "-1", "y_P", "-2 - 1 + 4 + 5 = 6",
             "6x^2 - 2x - 4", "6 + 2 - 4 = 4", 4, "-\\frac{1}{4} = -0{,}25",
             "6 = -0{,}25 \\cdot (-1) + b", "5{,}75", "-0{,}25x + 5{,}75",
             "[6, 4, -0.25, 5.75]", orig("2022-B-1f", 2022, "B"),
             "(FHR 2022)"),
            ("x^3 - x^2 - 3x + 2", "2", "y_P", "8 - 4 - 6 + 2 = 0",
             "3x^2 - 2x - 3", "12 - 4 - 3 = 5", 5, "-\\frac{1}{5} = -0{,}2",
             "0 = -0{,}2 \\cdot 2 + b", "0{,}4", "-0{,}2x + 0{,}4",
             "[0, 5, -0.2, 0.4]", orig("2022-B-1f", 2022, "B"),
             "(FHR 2022)"),
            ("-x^3 + 2x^2 + 3x + 1", "1", None, "-1 + 2 + 3 + 1 = 5",
             "-3x^2 + 4x + 3", "-3 + 4 + 3 = 4", 4,
             "-\\frac{1}{4} = -0{,}25", "5 = -0{,}25 \\cdot 1 + b",
             "5{,}25", "-0{,}25x + 5{,}25", "[5, 4, -0.25, 5.25]",
             orig("2025-A-1h", 2025, "A"), "(FHR 2025)"),
            ("2x^3 - 3x^2 - 2x + 6", "-1", None, "-2 - 3 + 2 + 6 = 3",
             "6x^2 - 6x - 2", "6 + 6 - 2 = 10", 10,
             "-\\frac{1}{10} = -0{,}1", "3 = -0{,}1 \\cdot (-1) + b",
             "2{,}9", "-0{,}1x + 2{,}9", "[3, 10, -0.1, 2.9]",
             orig("2025-A-1h", 2025, "A"), "(FHR 2025)")]:
        if yp:
            auf = (f"Gegeben ist $f(x) = {term}$. Der Punkt $P({st} | y_P)$ "
                   "liegt auf dem Graphen von $f$. Berechne $y_P$ und den "
                   "Anstieg des Graphen in $P$, und bestimme die Gleichung "
                   f"der Normalen in $P$. {kt}")
            ant = "$y_P =$ __, Anstieg: __, $n(x) =$ __"
            fwn = "Funktionswert: $y_P = f"
        else:
            auf = (f"Gegeben ist $f(x) = {term}$. Bestimme die Gleichung der "
                   "Normalen an den Graphen von $f$ an der Stelle "
                   f"$x = {st}$. {kt}")
            ant = "$n(x) =$ __"
            fwn = "Funktionswert: $f"
        pr.append(neu(
            v, aufgabe=auf, antwort=ant,
            loesung=(f"{fwn}({st}) = {fw_rech}$; Anstieg: $f'(x) = {abl}$, "
                     f"$f'({st}) = {a_rech}$; Normalensteigung: "
                     f"$m_n = {mn_rech}$; b aus P: ${br}$, also $b = {b}$; "
                     f"Normale: $n(x) = {nx}$"),
            pruef=pz, original=kenn))
    aus += varianten(pr)
    fe = pflicht_merkmal(nimm(alt, 2, 1))
    fe[1] = um(
        fe[1], aufgabe=("Die Tangente an den Graphen von $f$ im Punkt "
                        "$P(2 | 1)$ hat die Steigung $-4$. Lars bestimmt die "
                        "Normale: \\rechnung{m_n &= -\\frac{1}{-4} = "
                        "\\frac{1}{4} \\\\ 1 &= \\frac{1}{4} \\cdot 2 + b "
                        "\\\\ b &= \\frac{1}{2} \\\\ n(x) &= \\frac{1}{4}x + "
                        "\\frac{1}{2}} Prüfe, ob Lars richtig gerechnet "
                        "hat."),
        loesung=("Richtig. Die Normale hat den negativen Kehrwert der "
                 "Tangentensteigung, und sie geht durch den Berührpunkt "
                 "$P$."),
        pruef="")
    fe[2] = um(
        fe[2], aufgabe=("Die Tangente an den Graphen von $f$ im Punkt "
                        "$P(3 | 2)$ hat die Steigung $2$. Vier Schüler geben "
                        "die Normale in $P$ an. Welche Ergebnisse können "
                        "nicht stimmen? Begründe, ohne genau zu rechnen. "
                        "\\\\ (1) $n(x) = 2x - 4$ \\\\ (2) $n(x) = -2x + 8$ "
                        "\\\\ (3) $n(x) = -\\frac{1}{2}x + \\frac{7}{2}$ \\\\ "
                        "(4) $n(x) = \\frac{1}{2}x + \\frac{1}{2}$"),
        loesung=("Nicht stimmen können (1), (2) und (4). (1): Die Steigung "
                 "$2$ ist die der Tangente, die Normale steht aber senkrecht "
                 "zu ihr. (2): Hier ist nur das Vorzeichen gedreht; das "
                 "Produkt der Steigungen ist dann nicht $-1$. (4): Die "
                 "Tangente steigt, also muss die Normale fallen. (3) kann "
                 "stimmen."),
        pruef="")
    aus += fe
    be = pflicht_merkmal(nimm(alt, 2, 2))
    be[1] = um(
        be[1], aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                        "falsch ist. Begründe. \\\\ (1) Die Normale in einem "
                        "Punkt steht immer senkrecht auf der Tangente in "
                        "diesem Punkt. \\\\ (2) Jede Normale hat eine "
                        "negative Steigung. \\\\ (3) Ist die Tangente "
                        "waagerecht, so ist die Normale immer senkrecht."),
        loesung=("(1) wahr, denn so ist die Normale festgelegt. (2) falsch, "
                 "z. B. hat die Normale zur Tangentensteigung $-2$ die "
                 "Steigung $\\frac{1}{2}$. (3) wahr, denn zu einer "
                 "waagerechten Geraden steht nur eine senkrechte Gerade "
                 "senkrecht; sie hat keine Steigung."),
        pruef="")
    be[2] = um(
        be[2], aufgabe=("Ole sagt: „Hat die Tangente die Steigung $1$, dann "
                        "hat die Normale die Steigung $-1$. Hier reicht es, "
                        "das Vorzeichen umzudrehen.“ Begründe, ohne genau zu "
                        "rechnen, ob Ole recht hat."),
        loesung=("Ja; der negative Kehrwert von $1$ ist $-1$, also dasselbe "
                 "wie das gedrehte Vorzeichen – das gilt aber nur für die "
                 "Tangentensteigungen $1$ und $-1$."),
        pruef="")
    aus += be
    schreibe(3, alt, aus)


# ---------------------------------------------------------------- e4
def e4():
    alt = lade(4)
    aus = []
    for a in nimm(alt, 1, 0):
        a["sprosse"] = -1
        a["sprosse_text"] = T_E1_SM1
        aus.append(a)
    g = nimm(alt, 1, 1)[0]
    m0 = ("erkennen, ob der Steigungswinkel (0° bis 180°) oder der "
          "Schnittwinkel (höchstens 90°) gefragt ist, ohne Rechnung")
    s0 = []
    for auf, loes in [
            ("Die Gerade $g$ geht durch den Punkt $P(1 | 2)$ und hat die "
             "Steigung $-3$. Gesucht ist ihr Winkel gegen die positive "
             "$x$-Richtung. Welcher Winkel ist gefragt? \\\\ "
             "\\kreuz{Steigungswinkel} \\\\ \\kreuz{Schnittwinkel}",
             "Steigungswinkel – er wird gegen die positive $x$-Richtung "
             "gemessen und liegt zwischen $0^\\circ$ und $180^\\circ$."),
            ("Zwei Graphen schneiden sich im Punkt $P(1 | 2)$. Gesucht ist "
             "der Winkel zwischen den beiden Graphen. Welcher Winkel ist "
             "gefragt? \\\\ \\kreuz{Steigungswinkel} \\\\ "
             "\\kreuz{Schnittwinkel}",
             "Schnittwinkel – der kleinere Winkel zwischen den Tangenten, "
             "höchstens $90^\\circ$."),
            ("Eine Straße steigt geradlinig an. Gesucht ist der Winkel, unter "
             "dem sie gegen die Waagerechte ansteigt. Welcher Winkel ist "
             "gefragt? \\\\ \\kreuz{Steigungswinkel} \\\\ "
             "\\kreuz{Schnittwinkel}",
             "Steigungswinkel – gemessen gegen die Waagerechte in "
             "Fahrtrichtung."),
            ("Der Graph von $f$ schneidet die $x$-Achse. Gesucht ist der "
             "Winkel zwischen Graph und $x$-Achse. Welcher Winkel ist "
             "gefragt? \\\\ \\kreuz{Steigungswinkel} \\\\ "
             "\\kreuz{Schnittwinkel}",
             "Schnittwinkel – der Winkel zwischen Graph und Achse, höchstens "
             "$90^\\circ$.")]:
        s0.append(neu(
            g, sprosse=0, hoehe="vorstufe", sprosse_text=T_E4_S0, merkmal=m0,
            aufgabe=auf, form="ankreuzen", antwort="", loesung=loes,
            pruef="", original=None, grafik="", loesungsgrafik=""))
    aus += varianten(s0)
    m1 = ("Gerade durch den festen Punkt P(1 | 2): Steigung in Winkel über "
          "den Arkustangens oder Winkel in Steigung über den Tangens, "
          "Grad-Modus; Steigung oder Winkel wandert (spitz, stumpf, 90°)")
    gf = []
    for auf, ant, loes, pz in [
            ("Die Gerade $g$ geht durch den Punkt $P(1 | 2)$ und hat die "
             "Steigung $2$. Berechne ihren Steigungswinkel.",
             "$\\alpha \\approx$ __°",
             "Ansatz: $\\mathrm{tan}\\,\\alpha = 2$; Arkustangens "
             "(Grad-Modus): $\\alpha = \\mathrm{tan}^{-1}(2) \\approx "
             "63{,}4^\\circ$", "math.degrees(math.atan(2))"),
            ("Die Gerade $g$ geht durch den Punkt $P(1 | 2)$ und hat die "
             "Steigung $-0{,}75$. Berechne ihren Steigungswinkel gegen die "
             "positive $x$-Richtung.", "$\\alpha \\approx$ __°",
             "Ansatz: $\\mathrm{tan}\\,\\alpha = -0{,}75$; Arkustangens "
             "(Grad-Modus): $\\mathrm{tan}^{-1}(-0{,}75) \\approx "
             "-36{,}9^\\circ$; stumpfer Steigungswinkel: $\\alpha = "
             "180^\\circ - 36{,}9^\\circ = 143{,}1^\\circ$",
             "180 + math.degrees(math.atan(-0.75))"),
            ("Die Gerade $g$ geht durch den Punkt $P(1 | 2)$ und hat den "
             "Steigungswinkel $30^\\circ$. Berechne ihre Steigung.",
             "$m \\approx$ __",
             "Ansatz: $m = \\mathrm{tan}(30^\\circ)$; Tangens (Grad-Modus): "
             "$m \\approx 0{,}58$", "math.tan(math.radians(30))"),
            ("Die Gerade $g$ geht durch den Punkt $P(1 | 2)$ und hat den "
             "Steigungswinkel $120^\\circ$. Berechne ihre Steigung.",
             "$m \\approx$ __",
             "Ansatz: $m = \\mathrm{tan}(120^\\circ)$; Tangens (Grad-Modus): "
             "$m \\approx -1{,}73$; Lage: stumpfer Winkel, die Gerade fällt",
             "math.tan(math.radians(120))"),
            ("Die Gerade $g$ geht durch den Punkt $P(1 | 2)$ und hat den "
             "Steigungswinkel $90^\\circ$. Welche Steigung hat sie?",
             "Steigung: __",
             "Keine Steigung: $\\mathrm{tan}(90^\\circ)$ ist nicht definiert; "
             "die Gerade durch $P$ ist senkrecht, ihre Gleichung ist "
             "$x = 1$.", "1")]:
        gf.append(um(g, merkmal=m1, aufgabe=auf, antwort=ant, loesung=loes,
                     pruef=pz, original=None))
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 11)])
    aus += rest(alt, (2, 1))
    fe = pflicht_merkmal(nimm(alt, 3, 1))
    fe[1] = um(
        fe[1], aufgabe=("Die Tangente an den Graphen von $f$ im Punkt $P$ hat "
                        "die Steigung $-2$. Jana bestimmt den Schnittwinkel "
                        "der Tangente mit der $x$-Achse: "
                        "\\rechnung{\\mathrm{tan}^{-1}(-2) &\\approx "
                        "-63{,}4^\\circ \\\\ \\text{Schnittwinkel} &\\approx "
                        "63{,}4^\\circ} Prüfe, ob Jana richtig gerechnet "
                        "hat."),
        loesung=("Richtig. Ein Schnittwinkel ist höchstens $90^\\circ$; bei "
                 "fallender Tangente zählt der Betrag des Winkels unter der "
                 "Waagerechten."),
        pruef="")
    fe[2] = um(
        fe[2], aufgabe=("Vier Schüler haben den Steigungswinkel einer "
                        "Geraden mit der Steigung $0{,}8$ berechnet. Welche "
                        "Ergebnisse können nicht stimmen? Begründe, ohne "
                        "genau zu rechnen. \\\\ (1) $38{,}7^\\circ$ \\\\ (2) "
                        "$0{,}67^\\circ$ \\\\ (3) $51{,}3^\\circ$ \\\\ (4) "
                        "$141{,}3^\\circ$"),
        loesung=("Nicht stimmen können (2), (3) und (4). (2): Der Rechner "
                 "stand im Bogenmaß; zu einer Steigung nahe $1$ gehört ein "
                 "Winkel nahe $45^\\circ$. (3): Die Steigung ist kleiner als "
                 "$1$, der Winkel also kleiner als $45^\\circ$. (4): Die "
                 "Gerade steigt, ihr Steigungswinkel ist spitz. (1) kann "
                 "stimmen."),
        pruef="")
    aus += fe
    be = pflicht_merkmal(nimm(alt, 3, 2))
    be[1] = um(
        be[1], aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                        "falsch ist. Begründe. \\\\ (1) Eine Gerade mit "
                        "negativer Steigung hat immer einen stumpfen "
                        "Steigungswinkel. \\\\ (2) Verdoppelt man die "
                        "Steigung, so verdoppelt sich immer auch der "
                        "Steigungswinkel. \\\\ (3) Zwei Geraden mit den "
                        "Steigungen $3$ und $-\\frac{1}{3}$ schneiden sich "
                        "senkrecht."),
        loesung=("(1) wahr, denn gegen die positive $x$-Richtung gemessen "
                 "liegt der Winkel einer fallenden Geraden zwischen "
                 "$90^\\circ$ und $180^\\circ$. (2) falsch, z. B. gehört zur "
                 "Steigung $1$ der Winkel $45^\\circ$, zur Steigung $2$ aber "
                 "etwa $63{,}4^\\circ$, nicht $90^\\circ$. (3) wahr, denn das "
                 "Produkt der Steigungen ist $-1$."),
        pruef="")
    be[2] = um(
        be[2], aufgabe=("Die Tangenten an zwei Graphen im gemeinsamen Punkt "
                        "haben die Steigungen $5$ und $2$. Leon sagt: „Der "
                        "Schnittwinkel ist $\\mathrm{tan}^{-1}(5 - 2)$.“ "
                        "Begründe, ob Leon recht hat."),
        loesung=("Nein; abgezogen werden die Steigungswinkel, nicht die "
                 "Steigungen: $\\mathrm{tan}^{-1}(5) - \\mathrm{tan}^{-1}(2) "
                 "\\approx 78{,}7^\\circ - 63{,}4^\\circ = 15{,}3^\\circ$, "
                 "nicht $\\mathrm{tan}^{-1}(3) \\approx 71{,}6^\\circ$."),
        pruef="")
    aus += be
    schreibe(4, alt, aus)


# ---------------------------------------------------------------- e5
def e5():
    alt = lade(5)
    aus = rest(alt, (1, 0))
    g = nimm(alt, 1, 1)[0]
    m1 = ("Gerade mit festem y-Achsenabschnitt 6: Nullstelle und "
          "y-Achsenabschnitt als Katheten, Fläche als halbes Produkt; die "
          "Steigung wandert")
    gf = []
    for gx, x0, fl, pz, kenn in [
            ("-3x + 6", "2", "$A = \\frac{1}{2} \\cdot 2 \\cdot 6 = 6$",
             "[2, 6, 6]", None),
            ("-2x + 6", "3", "$A = \\frac{1}{2} \\cdot 3 \\cdot 6 = 9$",
             "[3, 6, 9]", None),
            ("1{,}5x + 6", "-4", "$A = \\frac{1}{2} \\cdot 4 \\cdot 6 = 12$ "
             "(Beträge der Katheten)", "[-4, 6, 12]", None),
            ("-0{,}5x + 6", "12", "$A = \\frac{1}{2} \\cdot 12 \\cdot 6 = "
             "36$", "[12, 6, 36]", None),
            ("-4x + 6", "1{,}5", "$A = \\frac{1}{2} \\cdot 1{,}5 \\cdot 6 "
             "= 4{,}5$ – der Faktor $\\frac{1}{2}$ gehört dazu",
             "[1.5, 6, 4.5]", orig("2026-B-1h", 2026, "B"))]:
        auf = (f"Die Gerade $g(x) = {gx}$ schließt mit den Koordinatenachsen "
               "ein Dreieck ein. Berechne seinen Flächeninhalt.")
        if kenn:
            auf += " (FHR 2026)"
        loes = (f"Nullstelle: $0 = {gx}$, also $x = {x0}$; y-Achsenabschnitt: "
                f"$g(0) = 6$; Fläche: {fl}")
        gf.append(um(g, merkmal=m1, aufgabe=auf, antwort="$A =$ __",
                     loesung=loes, pruef=pz, original=kenn))
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 9)])
    fe = pflicht_merkmal(nimm(alt, 2, 1))
    fe[1] = um(
        fe[1], aufgabe=("Die Tangente $y = -\\frac{3}{2}x + 3$ bildet mit den "
                        "Koordinatenachsen ein Dreieck. Emma rechnet: "
                        "\\rechnung{\\text{Nullstelle: } x &= 2 \\\\ A &= "
                        "\\frac{1}{2} \\cdot 2 \\cdot 3 = 3} Prüfe, ob Emma "
                        "richtig gerechnet hat."),
        loesung=("Richtig. Die Katheten sind die Beträge von Nullstelle und "
                 "$y$-Achsenabschnitt, der Flächeninhalt ist ihr halbes "
                 "Produkt."),
        pruef="")
    fe[2] = um(
        fe[2], aufgabe=("Die Tangente $y = -2x + 8$ bildet mit den "
                        "Koordinatenachsen ein Dreieck. Vier Schüler geben "
                        "seinen Flächeninhalt an. Welche Ergebnisse können "
                        "nicht stimmen? Begründe, ohne genau zu rechnen. "
                        "\\\\ (1) $A = 16$ \\\\ (2) $A = -16$ \\\\ (3) "
                        "$A = 32$ \\\\ (4) $A = 40$"),
        loesung=("Nicht stimmen können (2), (3) und (4). (2): Ein "
                 "Flächeninhalt ist nie negativ. (3): $32$ ist das ganze "
                 "Rechteck aus beiden Katheten, der Faktor $\\frac{1}{2}$ "
                 "fehlt. (4): Das Dreieck passt in dieses Rechteck, mehr als "
                 "$32$ geht nicht. (1) kann stimmen."),
        pruef="")
    aus += fe
    be = pflicht_merkmal(nimm(alt, 2, 2))
    be[1] = um(
        be[1], aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                        "falsch ist. Begründe. \\\\ (1) Das Dreieck aus einer "
                        "Tangente und den beiden Koordinatenachsen ist immer "
                        "rechtwinklig. \\\\ (2) Jede Tangente bildet mit den "
                        "Koordinatenachsen ein Dreieck. \\\\ (3) Hat eine "
                        "Tangente, die nicht durch den Ursprung geht, die "
                        "Steigung $-1$, so ist ihr Achsendreieck "
                        "gleichschenklig."),
        loesung=("(1) wahr, denn zwei Seiten liegen auf den Achsen, und die "
                 "stehen im Ursprung senkrecht aufeinander. (2) falsch, z. B. "
                 "schließt die waagerechte Tangente $y = 2$ mit den Achsen "
                 "kein Dreieck ein. (3) wahr, denn bei Steigung $-1$ haben "
                 "Nullstelle und $y$-Achsenabschnitt denselben Betrag."),
        pruef="")
    be[2] = um(
        be[2], aufgabe=("Ben sagt: „Das Dreieck aus der Tangente $y = x + 3$ "
                        "und den beiden Koordinatenachsen ist "
                        "gleichschenklig.“ Begründe, ohne zu rechnen, ob Ben "
                        "recht hat."),
        loesung=("Ja; die Tangente hat die Steigung $1$, also haben "
                 "Nullstelle $-3$ und $y$-Achsenabschnitt $3$ denselben "
                 "Betrag – die Katheten sind gleich lang."),
        pruef="")
    aus += be
    schreibe(5, alt, aus)


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["e1", "e2", "e3", "e4", "e5"]
    for n in wahl:
        globals()[n]()
    for k, v in ZAEHL.items():
        print(k, v)

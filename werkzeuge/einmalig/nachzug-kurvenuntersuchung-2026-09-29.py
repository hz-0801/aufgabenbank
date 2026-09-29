"""Nachzug bank/kurvenuntersuchung auf Katalog 2a296e5 (Mappe 29.09.).

Einmalig, 2026-09-29. Liest den Bestand, zieht quelle (126–131 ->
124–129), sprosse, id und sprosse_text nach, schreibt die Päckchen,
die neuen Sprossen (e2 k1 s0, e2 k2 s6, e4 s4) und die Pflichtformen
P1–P8 und schreibt je Einheit die ganze Datei neu. Zählt je Einheit
übernommen/neu/umgeschrieben/entfallen (Ausgabe am Ende).
Aufruf aus der Wurzel des Repos: python3 werkzeuge/einmalig/<datei>
"""
import copy
import json
import sys
from pathlib import Path

B = Path("bank/kurvenuntersuchung")
QMAP = {126: 124, 127: 125, 128: 126, 129: 127, 130: 128, 131: 129}
ZAEHL = {}

# neue Sprossentexte (wortgleich aus der Mappe, Zeile quelle)
T_E2K1_SM1 = ("„gegeben oder gesucht“ und „welcher Nachweis“ ankreuzen, bei "
              "„welcher Nachweis“ die Art: Vorzeichen von f'', "
              "Vorzeichenwechsel von f', Begründung aus Abbildung oder "
              "Sachzusammenhang oder gar keiner; nichts rechnen (Vorstufe)")
T_E2K1_S0 = ("„Stelle, Wert oder Punkt?“ – zu Fragen und Antworten "
             "ankreuzen, ob die Stelle x₀, der Wert f(x₀) oder der Punkt "
             "(x₀ | f(x₀)) verlangt oder gegeben ist; nichts rechnen "
             "(Vorstufe)")
T_E2K2_S6 = ("„Ändert sich die Monotonie, ändert sich die Krümmung?“ – an "
             "Graphen ankreuzen: Monotonie ändert sich → Extrempunkt; "
             "Monotonie bleibt und Krümmung ändert sich → Sattelpunkt; "
             "nichts rechnen")
T_E3_S0 = ("„welcher Nachweis“ – ankreuzen, welcher Art-Nachweis verlangt "
           "oder möglich ist: rechnerisch über eine höhere Ableitung oder "
           "einen Vorzeichenwechsel, Begründung aus Abbildung oder "
           "Sachzusammenhang oder gar keiner; nichts rechnen (Vorstufe)")
T_E4_S4 = ("aus einer ausgefüllten Übersichtstabelle (Nullstellen, "
           "Extrempunkte, Monotonie, Verhalten im Unendlichen, "
           "Schnittpunkt mit der y-Achse) den Graphen skizzieren, nichts "
           "rechnen (GK)")
T_E5_S0 = ("„was heißt das mathematisch“ – Sachfragen übersetzen und "
           "ankreuzen: stärkste Zunahme oder Abnahme als Wendepunkt bzw. "
           "Extremum der Ableitung, größter oder kleinster Wert als "
           "globales Maximum oder Minimum einschließlich Rand, ändert sich "
           "gerade nicht als Ableitung null; nichts rechnen (Vorstufe)")

M_FEHLER = ("Rechnung prüfen: Fehler finden, richtige Rechnung erkennen, "
            "unmögliche Ergebnisse erkennen")
M_BEGR = ("begründen: Regel beim Namen, Aussagen beurteilen, "
          "Behauptung beurteilen")


def lade(n):
    return [json.loads(z) for z in
            (B / f"e{n}.jsonl").read_text(encoding="utf-8").splitlines()]


def nimm(zeilen, k, s):
    return [copy.deepcopy(a) for a in zeilen
            if a["kette_nr"] == k and a["sprosse"] == s]


def neu_zeile(vorlage, **kw):
    a = copy.deepcopy(vorlage)
    a["_neu"] = kw.get("sprosse", vorlage["sprosse"]) != vorlage["sprosse"]
    for f in ("pflicht",):
        if f in a and kw.get("hoehe", a["hoehe"]) != "pflicht":
            del a[f]
    a.update(kw)
    return a


def ordne(zeilen, einheit):
    """id, variante, quelle nachziehen; Schlüsselfolge wie Bestand."""
    felder = ["id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
              "sprosse_text", "merkmal", "hoehe", "pflicht", "variante",
              "aufgabe", "form", "antwort", "loesung", "pruef", "original",
              "grafik", "loesungsgrafik", "quelle"]
    aus = []
    for a in zeilen:
        a["quelle"] = QMAP.get(a["quelle"], a["quelle"])
        a["id"] = (f"kurvenuntersuchung-e{einheit}-k{a['kette_nr']}"
                   f"-s{a['sprosse']}-v{a['variante']}")
        aus.append({f: a[f] for f in felder if f in a})
    for a in zeilen:
        a.pop("_neu", None)
    return aus


def schreibe(n, zeilen):
    text = "".join(json.dumps(a, ensure_ascii=False) + "\n" for a in zeilen)
    (B / f"e{n}.jsonl").write_text(text, encoding="utf-8")


NACHGEZOGEN = ("id", "sprosse", "kette_nr", "quelle", "sprosse_text", "hoehe",
               "_neu")


def zaehle(n, alt, zeilen):
    """übernommen: bis auf die nachgezogenen Felder gleich einer
    Bestandszeile; neu: Zeile einer neuen Sprosse; sonst umgeschrieben
    (ersetzt eine Bestandszeile); entfallen: der Rest des Bestands."""
    def kern(a):
        return json.dumps({k: v for k, v in a.items()
                           if k not in NACHGEZOGEN}, sort_keys=True,
                          ensure_ascii=False)
    bestand = {kern(a) for a in alt}
    ueb = sum(1 for a in zeilen if kern(a) in bestand)
    neu = sum(1 for a in zeilen if a.get("_neu"))
    um = len(zeilen) - ueb - neu
    ZAEHL[f"e{n}"] = dict(uebernommen=ueb, neu=neu, umgeschrieben=um,
                          entfallen=len(alt) - ueb - um)


def varianten(zeilen, **kw):
    for i, a in enumerate(zeilen, 1):
        a["variante"] = i
        a.update(kw)
    return zeilen


def ersetze(gruppe, v, **kw):
    """Variante v einer Gruppe umschreiben (Felder aus kw)."""
    a = gruppe[v - 1]
    a.update(kw)
    return a


# ---------------------------------------------------------------- e1
def e1():
    alt = lade(1)
    g = nimm(alt, 1, 1)[0]
    m = ("Vorzeichen der gegebenen Ableitung auf einem Intervall, daraus "
         "steigt oder fällt; die Ableitung 2x − 6 bleibt, das Intervall "
         "wandert")
    paeck = []
    for iv, st, grund in [
            ("[4; 6]", True, "für $4 \\le x \\le 6$ liegt $f'(x) = 2x - 6$ "
             "zwischen $2$ und $6$, also positiv"),
            ("[0; 2]", False, "für $0 \\le x \\le 2$ liegt $f'(x)$ zwischen "
             "$-6$ und $-2$, also negativ"),
            ("[-2; 1]", False, "für $-2 \\le x \\le 1$ liegt $f'(x)$ zwischen "
             "$-10$ und $-4$, also negativ"),
            ("[5; 9]", True, "für $5 \\le x \\le 9$ liegt $f'(x)$ zwischen "
             "$4$ und $12$, also positiv"),
            ("[1; 2{,}5]", False, "für $1 \\le x \\le 2{,}5$ liegt $f'(x)$ "
             "zwischen $-4$ und $-1$, also negativ")]:
        wort = ("$f$ steigt auf diesem Intervall" if st
                else "$f$ fällt auf diesem Intervall")
        paeck.append(neu_zeile(
            g, merkmal=m,
            aufgabe=("Gegeben ist die Ableitung $f'(x) = 2x - 6$. Bestimme "
                     f"das Vorzeichen von $f'(x)$ auf dem Intervall ${iv}$ "
                     "und kreuze an. \\\\ \\kreuz{$f$ steigt auf diesem "
                     "Intervall} \\\\ \\kreuz{$f$ fällt auf diesem "
                     "Intervall}"),
            loesung=f"{wort} – {grund}.", pruef=""))
    varianten(paeck)

    fe = nimm(alt, 2, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    ersetze(fe, 2,
            aufgabe=("Tom soll die Monotonieintervalle von $f(x) = x^3 - "
                     "7{,}5x^2 + 18x$ bestimmen. Er rechnet so: "
                     "\\rechnung{f'(x) &= 3x^2 - 15x + 18 \\\\ 3x^2 - 15x + "
                     "18 &= 0 &&\\mid :3 \\\\ x^2 - 5x + 6 &= 0 \\\\ x_1 = 2, "
                     "\\quad x_2 &= 3} Antwort: $f$ steigt auf $]-\\infty; "
                     "2]$, fällt auf $[2; 3]$ und steigt auf $[3; \\infty[$. "
                     "Prüfe, ob Tom richtig gerechnet hat."),
            loesung=("Richtig. Die Grenzen der Monotonieintervalle sind die "
                     "Nullstellen von $f'$; $f'$ ist eine nach oben geöffnete "
                     "Parabel, also links von $2$ positiv, zwischen $2$ und "
                     "$3$ negativ und rechts von $3$ positiv."),
            pruef="")
    ersetze(fe, 3,
            aufgabe=("Jonas hat für vier Funktionen die Monotonie angegeben. "
                     "Welche Ergebnisse können nicht stimmen? Begründe, ohne "
                     "genau zu rechnen. \\\\ (1) $f(x) = x^2 + 4x$: $f$ fällt "
                     "auf $[-2; \\infty[$. \\\\ (2) $g(x) = x^3 + x$: $g$ "
                     "fällt auf $[0; 1]$. \\\\ (3) $h(x) = -x^2 + 6x$: $h$ "
                     "steigt auf $]-\\infty; 3]$. \\\\ (4) $k(x) = -2x^3 + "
                     "21x^2 - 60x$: $k$ steigt auf $]-\\infty; 2]$, fällt "
                     "auf $[2; 5]$ und steigt auf $[5; \\infty[$."),
            loesung=("Nicht stimmen können (1), (2) und (4). (1): Eine nach "
                     "oben geöffnete Parabel steigt rechts vom Scheitel, sie "
                     "fällt dort nicht. (2): $g'(x) = 3x^2 + 1$ ist immer "
                     "positiv, $g$ fällt nirgends. (4): Bei negativer "
                     "Vorzahl vor $x^3$ fällt der Graph ganz rechts, er kann "
                     "auf $[5; \\infty[$ nicht steigen. (3) kann stimmen."),
            pruef="")

    be = nimm(alt, 2, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    ersetze(be, 2,
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe. \\\\ (1) Ist $f'(x) > 0$ für alle $x$, "
                     "so hat der Graph von $f$ nie einen Hochpunkt. \\\\ (2) "
                     "Hat $f'$ eine Nullstelle, so hat der Graph von $f$ "
                     "dort immer einen Extrempunkt. \\\\ (3) Jede "
                     "ganzrationale Funktion dritten Grades fällt "
                     "irgendwo."),
            loesung=("(1) wahr, denn in einem Hochpunkt wäre die Tangente "
                     "waagerecht, also $f'(x_0) = 0$. (2) falsch, z. B. "
                     "$f(x) = x^3 - 1$: $f'(x) = 3x^2$ ist bei $0$ null, "
                     "wechselt aber das Vorzeichen nicht (Sattelpunkt). (3) "
                     "falsch, z. B. $f(x) = x^3 + x$: $f'(x) = 3x^2 + 1 > 0$, "
                     "der Graph steigt überall."),
            pruef="")
    ersetze(be, 3,
            aufgabe=("Lea sagt: „Die Gleichung $2x^2 + 5 = 0$ hat wie jede "
                     "quadratische Gleichung eine Lösung, also hat $f'(x) = "
                     "2x^2 + 5$ eine Nullstelle.“ Begründe, ob Lea recht "
                     "hat."),
            loesung=("Nein; $2x^2$ ist nie negativ, also ist $2x^2 + 5$ immer "
                     "mindestens $5$ – die Gleichung hat keine Lösung, $f'$ "
                     "hat keine Nullstelle."),
            pruef="")

    an = nimm(alt, 2, 3)
    ersetze(an, 1, loesung=(
        "wahr; Ableitung von $A$: $A'(t) = -0{,}3t^2 + 3t = 0$ für $t = 10$, "
        "$A$ nimmt auf $[0; 10]$ zu, also $10$ Tage; Ableitung von $B$: "
        "$B'(t) = -0{,}6t^2 + 4{,}8t = 0$ für $t = 8$, $B$ nimmt auf "
        "$[0; 8]$ zu, also $8$ Tage; Vergleich: $10 > 8$."))
    ersetze(an, 2, loesung=(
        "falsch; Ableitung von $P_1$: $P_1'(t) = -1{,}5t^2 + 12t = 0$ für "
        "$t = 8$, $P_1$ sinkt auf $[8; 12]$, also $4$ Stunden; Ableitung von "
        "$P_2$: $P_2'(t) = -3t^2 + 18t = 0$ für $t = 6$, $P_2$ sinkt auf "
        "$[6; 9]$, also $3$ Stunden; Vergleich: $3 < 4$."))
    ersetze(an, 3,
            aufgabe=("Die wöchentlichen Verkaufszahlen eines neuen Spiels (in "
                     "Tausend Stück) werden $t$ Wochen nach dem Start durch "
                     "$V(t) = -0{,}5t^3 + 6t^2$ mit $0 \\le t \\le 12$ "
                     "modelliert. Eine Werbeaktion läuft in den ersten $7$ "
                     "Wochen; die Firma will, dass die Verkaufszahlen "
                     "während der ganzen Aktion steigen. Gelingt das?"),
            loesung=("Ja; Ableitung bilden: $V'(t) = -1{,}5t^2 + 12t$; null "
                     "setzen: $-1{,}5t \\cdot (t - 8) = 0$ für $t = 0$ oder "
                     "$t = 8$; Monotonie: $V'(t) > 0$ für $0 < t < 8$, $V$ "
                     "steigt auf $[0; 8]$; Vergleich: $7 < 8$, die Zahlen "
                     "steigen während der ganzen Aktion."),
            pruef="8")

    k1 = nimm(alt, 1, 0) + paeck + [a for s in range(2, 8)
                                    for a in nimm(alt, 1, s)]
    zeilen = k1 + fe + be + an
    zaehle(1, alt, zeilen)
    schreibe(1, ordne(zeilen, 1))


# ---------------------------------------------------------------- e2
def e2():
    alt = lade(2)
    vor = nimm(alt, 1, 0)
    for a in vor:
        a["sprosse"] = -1
        a["sprosse_text"] = T_E2K1_SM1
    g = nimm(alt, 1, 1)[0]
    cs = [3, -5, -12, -21, -32]

    def fterm(c):
        return (f"\\frac{{1}}{{3}}x^3 - 2x^2 + {c}x" if c > 0
                else f"\\frac{{1}}{{3}}x^3 - 2x^2 - {-c}x")

    def fstrich(c):
        return f"x^2 - 4x + {c}" if c > 0 else f"x^2 - 4x - {-c}"

    # neue Vorstufe s0 „Stelle, Wert oder Punkt?“
    opt = ("\\\\ \\kreuz{Stelle $x_0$} \\\\ \\kreuz{Wert $f(x_0)$} \\\\ "
           "\\kreuz{Punkt $(x_0 | f(x_0))$}")
    s0 = []
    for c, frage, los in [
            (3, "„Berechnen Sie die Stellen, an denen der Graph von $f$ eine "
                "waagerechte Tangente hat.“ Kreuze an, was verlangt ist, "
                "ohne zu rechnen.",
             "Stelle $x_0$ – gefragt ist nur, wo die Tangente waagerecht "
             "ist."),
            (-5, "„Wie weit liegt der Hochpunkt des Graphen von $f$ über der "
                 "$x$-Achse?“ Kreuze an, was verlangt ist, ohne zu rechnen.",
             "Wert $f(x_0)$ – gefragt ist die Höhe, nicht die Lage."),
            (-12, "„Geben Sie die Koordinaten des Tiefpunkts des Graphen von "
                  "$f$ an.“ Kreuze an, was verlangt ist, ohne zu rechnen.",
             "Punkt $(x_0 | f(x_0))$ – Koordinaten heißt beide Zahlen."),
            (-21, "Eine Lösung zum Tiefpunkt des Graphen von $f$ endet mit "
                  "„Ergebnis: bei $x = 7$“. Kreuze an, was diese Antwort "
                  "angibt, ohne zu rechnen.",
             "Stelle $x_0$ – für den Punkt fehlt noch der Wert $f(7)$.")]:
        s0.append(neu_zeile(
            g, sprosse=0, hoehe="vorstufe", sprosse_text=T_E2K1_S0,
            merkmal="nur entscheiden: Stelle, Wert oder Punkt verlangt oder "
                    "gegeben",
            aufgabe=f"Gegeben ist $f(x) = {fterm(c)}$. {frage} {opt}",
            form="ankreuzen", antwort="", loesung=los, pruef="",
            grafik="", loesungsgrafik="", original=None, quelle=127))
    varianten(s0)

    m = ("f' = 0 mit quadratischer Ableitung über die Lösungsformel lösen; "
         "der Teil x³/3 − 2x² bleibt, der Faktor vor x wandert")
    paeck = []
    for c in cs:
        w = 4 - c
        r = int(w ** 0.5)
        paeck.append(neu_zeile(
            g, merkmal=m,
            aufgabe=("Berechne die Stellen, an denen der Graph von $f(x) = "
                     f"{fterm(c)}$ eine waagerechte Tangente hat."),
            loesung=(f"Ableitung bilden: $f'(x) = {fstrich(c)}$; null setzen: "
                     f"${fstrich(c)} = 0$; Lösungsformel: $x = 2 \\pm "
                     f"\\sqrt{{4 {'-' if c > 0 else '+'} {abs(c)}}} = 2 \\pm "
                     f"{r}$; Ergebnis: $x_1 = {2 + r}$; $x_2 = {2 - r}$"),
            pruef=f"[{2 + r}, {2 - r}]"))
    varianten(paeck)
    k1 = vor + s0 + paeck + [a for s in range(2, 11) for a in nimm(alt, 1, s)]

    # Kette 2 „Extrempunkte nachweisen“
    g2 = nimm(alt, 2, 1)[0]
    m2 = ("genannte Stelle in f' einsetzen; die Stelle 2 und der Term "
          "x³ − 12x bleiben, der Faktor davor wandert")
    paeck2 = []
    for k, term, ab, rech in [
            ("1", "x^3 - 12x", "3x^2 - 12", "3 \\cdot 4 - 12"),
            ("2", "2x^3 - 24x", "6x^2 - 24", "6 \\cdot 4 - 24"),
            ("-1", "-x^3 + 12x", "-3x^2 + 12", "-3 \\cdot 4 + 12"),
            ("0,5", "0{,}5x^3 - 6x", "1{,}5x^2 - 6", "1{,}5 \\cdot 4 - 6"),
            ("3", "3x^3 - 36x", "9x^2 - 36", "9 \\cdot 4 - 36")]:
        paeck2.append(neu_zeile(
            g2, merkmal=m2,
            aufgabe=("Zeige, dass $f'(2) = 0$ gilt, der Graph von $f(x) = "
                     f"{term}$ also bei $x = 2$ eine waagerechte Tangente "
                     "hat."),
            loesung=(f"Ableitung bilden: $f'(x) = {ab}$; Stelle einsetzen: "
                     f"$f'(2) = {rech} = 0$"),
            pruef="0"))
    varianten(paeck2)

    s6 = []
    for fkt, bereich, p, los in [
            ("(\\x-1)^3+2", "{-0.5}{2.5}", "\\punkt{1}{2}{P}",
             "Sattelpunkt – der Graph steigt vor und nach $P$, nur die "
             "Krümmung wechselt."),
            ("\\x^3/6-2*\\x", "{-4}{4}", "\\punkt{2}{-2.67}{P}",
             "Extrempunkt – der Graph fällt vor $P$ und steigt danach, die "
             "Monotonie ändert sich."),
            ("0.1*\\x^4-1", "{-2}{2}", "\\punkt{0}{-1}{P}",
             "Extrempunkt – der Graph fällt vor $P$ und steigt danach; dass "
             "er sehr flach ist, ändert daran nichts.")]:
        ks = {"(\\x-1)^3+2": "xmin=-1,xmax=3,ymin=-2,ymax=5",
              "\\x^3/6-2*\\x": "xmin=-4,xmax=4,ymin=-4,ymax=4",
              "0.1*\\x^4-1": "xmin=-2,xmax=2,ymin=-2,ymax=1"}[fkt]
        s6.append(neu_zeile(
            g2, sprosse=6, hoehe="sprosse", sprosse_text=T_E2K2_S6,
            merkmal="am Graphen entscheiden: Monotonie wechselt oder nur "
                    "die Krümmung",
            aufgabe=("Die Abbildung zeigt den Graphen von $f$; in $P$ ist die "
                     "Tangente waagerecht. Ändert sich in $P$ die Monotonie "
                     "oder nur die Krümmung? Kreuze an, ohne zu rechnen. "
                     "\\\\ \\kreuz{Extrempunkt} \\\\ \\kreuz{Sattelpunkt}"),
            form="ankreuzen", antwort="", loesung=los, pruef="",
            grafik=(f"\\begin{{ksys}}[{ks},ablesen] \\funktionab{{{fkt}}}"
                    f"{{f}}{bereich} {p} \\end{{ksys}}"),
            loesungsgrafik="", original=None, quelle=128))
    varianten(s6)

    k2 = nimm(alt, 2, 0) + paeck2 + [a for s in range(2, 6)
                                     for a in nimm(alt, 2, s)] + s6
    for s in range(6, 10):
        for a in nimm(alt, 2, s):
            a["sprosse"] = s + 1
            if s == 9:
                a["hoehe"] = "pruefung"
            k2.append(a)

    typen = [a for a in alt if 3 <= a["kette_nr"] <= 11]
    fe = nimm(alt, 12, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    ersetze(fe, 2,
            aufgabe=("Lina sucht die Extremstellen von $f(x) = (x - 2) \\cdot "
                     "\\mathrm{e}^{x}$. Sie rechnet so: \\rechnung{f'(x) &= 1 "
                     "\\cdot \\mathrm{e}^{x} + (x - 2) \\cdot \\mathrm{e}^{x} "
                     "= (x - 1) \\cdot \\mathrm{e}^{x} \\\\ (x - 1) \\cdot "
                     "\\mathrm{e}^{x} &= 0 \\\\ x - 1 &= 0 &&\\text{denn } "
                     "\\mathrm{e}^{x} \\ne 0 \\\\ x &= 1} Prüfe, ob Lina "
                     "richtig gerechnet hat."),
            loesung=("Richtig. Der Faktor $\\mathrm{e}^{x}$ wird nie null; "
                     "deshalb genügt es, den Polynomfaktor $x - 1$ null zu "
                     "setzen."),
            pruef="")
    ersetze(fe, 3,
            aufgabe=("Vier Schüler haben Extrempunkte angegeben. Welche "
                     "Ergebnisse können nicht stimmen? Begründe, ohne genau "
                     "zu rechnen. \\\\ (1) $f(x) = x^2 - 8x + 3$ hat bei "
                     "$x = 4$ einen Hochpunkt. \\\\ (2) $g(x) = x^3 - 5x^2 + "
                     "2x$ hat zwei Hochpunkte. \\\\ (3) $h(x) = -x^2 + 2x + "
                     "8$ hat den Hochpunkt $H(1 | 9)$. \\\\ (4) $k(x) = x^4 "
                     "+ 2x^2$ hat einen Hochpunkt bei $x = 1$."),
            loesung=("Nicht stimmen können (1), (2) und (4). (1): Eine nach "
                     "oben geöffnete Parabel hat nur einen Tiefpunkt. (2): "
                     "$g'$ ist quadratisch und hat höchstens zwei "
                     "Nullstellen; zwischen zwei Hochpunkten müsste ein "
                     "Tiefpunkt liegen. (4): Für $x > 0$ wachsen $x^4$ und "
                     "$2x^2$, $k$ steigt dort, es gibt keinen Hochpunkt. (3) "
                     "kann stimmen."),
            pruef="")
    be = nimm(alt, 12, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    ersetze(be, 2,
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe. \\\\ (1) Der größte Wert einer Funktion "
                     "auf einem Intervall liegt immer in einem Hochpunkt. "
                     "\\\\ (2) Ist $f'(x_0) = 0$ und $f''(x_0) < 0$, so hat "
                     "der Graph bei $x_0$ einen Hochpunkt. \\\\ (3) Es gibt "
                     "Funktionen mit $f'(x_0) = 0$, deren Graph bei $x_0$ "
                     "keinen Extrempunkt hat."),
            loesung=("(1) falsch, z. B. $f(x) = x$ auf $[0; 2]$: der größte "
                     "Wert $2$ liegt am Rand, einen Hochpunkt gibt es nicht. "
                     "(2) wahr, denn das ist die hinreichende Bedingung für "
                     "einen Hochpunkt. (3) wahr, z. B. $f(x) = x^3 + 1$ mit "
                     "$f'(0) = 0$ und dem Sattelpunkt $S(0 | 1)$."),
            pruef="")
    ersetze(be, 3,
            aufgabe=("Tim sagt: „Es gilt $f'(3) = 0$ und sonst überall "
                     "$f'(x) > 0$ – also hat $f$ bei $3$ einen Hochpunkt.“ "
                     "Begründe, ob Tim recht hat."),
            loesung=("Nein; $f'$ ist links und rechts von $3$ positiv, "
                     "wechselt also das Vorzeichen nicht – der Graph steigt "
                     "vor und nach $3$, bei $3$ liegt ein Sattelpunkt."),
            pruef="")
    an = nimm(alt, 12, 3)
    ersetze(an, 2,
            aufgabe=("Ein Stromkabel hängt über einem Fluss; seine Höhe über "
                     "dem Wasser ist $s(x) = 0{,}01x^2 - 0{,}8x + 30$ ($x$ "
                     "und $s(x)$ in m). Ein Segelboot hat einen $13{,}5$ m "
                     "hohen Mast, der mindestens $0{,}5$ m Abstand zum Kabel "
                     "halten muss. Kommt das Boot an der tiefsten Stelle des "
                     "Kabels vorbei?"),
            loesung=("Ja; Ableitung null setzen: $s'(x) = 0{,}02x - 0{,}8 = 0$ "
                     "für $x = 40$; tiefste Stelle: $s(40) = 14$; Abstand: "
                     "$14 - 13{,}5 = 0{,}5$, das reicht genau."),
            pruef="[40, 14, 0.5]")

    zeilen = k1 + k2 + typen + fe + be + an
    zaehle(2, alt, zeilen)
    schreibe(2, ordne(zeilen, 2))


# ---------------------------------------------------------------- e3
def e3():
    alt = lade(3)
    vor = nimm(alt, 1, 0)
    for a in vor:
        a["sprosse_text"] = T_E3_S0
    g = nimm(alt, 1, 1)[0]
    m = ("höhere Ableitungen bilden; x³ und −5x bleiben, der Faktor vor x² "
         "wandert")
    paeck = []
    for b in [3, -6, 9, -3, 12]:
        vz = "+" if b > 0 else "-"
        term = f"x^3 {vz} {abs(b)}x^2 - 5x"
        f1 = f"3x^2 {vz} {2 * abs(b)}x - 5"
        f2 = f"6x {vz} {2 * abs(b)}"
        paeck.append(neu_zeile(
            g, merkmal=m,
            aufgabe=("Bilde die erste, zweite und dritte Ableitung von "
                     f"$f(x) = {term}$."),
            loesung=(f"erste Ableitung: $f'(x) = {f1}$; zweite Ableitung: "
                     f"$f''(x) = {f2}$; dritte Ableitung: $f'''(x) = 6$"),
            pruef="[3, 6, 6]"))
    varianten(paeck)
    k1 = vor + paeck + [a for s in range(2, 11) for a in nimm(alt, 1, s)]
    typen = [a for a in alt if 2 <= a["kette_nr"] <= 6]

    fe = nimm(alt, 7, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    ersetze(fe, 2,
            aufgabe=("Max bestimmt den Wendepunkt des Graphen von $f(x) = x^3 "
                     "+ 3x^2 - 2$. Er rechnet so: \\rechnung{f''(x) &= 6x + 6 "
                     "= 0 &&\\Rightarrow x = -1 \\\\ f'''(-1) &= 6 \\ne 0 "
                     "\\\\ f(-1) &= -1 + 3 - 2 = 0} Antwort: $W(-1 | 0)$. "
                     "Prüfe, ob Max richtig gerechnet hat."),
            loesung=("Richtig. $f''' \\ne 0$ sichert den Wendepunkt, und die "
                     "zweite Koordinate kommt aus $f$, nicht aus $f''$."),
            pruef="")
    ersetze(fe, 3,
            aufgabe=("Vier Schüler haben Wendepunkte und Krümmung angegeben. "
                     "Welche Ergebnisse können nicht stimmen? Begründe, ohne "
                     "genau zu rechnen. \\\\ (1) $f(x) = x^2 + 5x$ hat einen "
                     "Wendepunkt bei $x = -2{,}5$. \\\\ (2) $g(x) = x^3 - "
                     "6x^2 + x$ hat zwei Wendepunkte. \\\\ (3) $h(x) = -x^2 + "
                     "4x$ ist überall rechtsgekrümmt. \\\\ (4) $k(x) = x^4 + "
                     "x^2$ hat bei $x = 0$ einen Wendepunkt."),
            loesung=("Nicht stimmen können (1), (2) und (4). (1): Bei einer "
                     "Parabel ist $f''$ konstant, die Krümmung wechselt "
                     "nie. (2): $g''$ ist linear und hat genau eine "
                     "Nullstelle, also genau einen Wendepunkt. (4): $k''(x) = "
                     "12x^2 + 2$ ist immer positiv, der Graph ist überall "
                     "linksgekrümmt. (3) kann stimmen."),
            pruef="")
    be = nimm(alt, 7, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    ersetze(be, 2,
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe. \\\\ (1) Jede ganzrationale Funktion "
                     "dritten Grades hat genau einen Wendepunkt. \\\\ (2) In "
                     "einem Wendepunkt ist die Tangente nie waagerecht. \\\\ "
                     "(3) Ist $f''(x) > 0$ für alle $x$, so ist der Graph "
                     "überall linksgekrümmt."),
            loesung=("(1) wahr, denn $f''$ ist linear, hat genau eine "
                     "Nullstelle und wechselt dort das Vorzeichen. (2) "
                     "falsch, z. B. $f(x) = x^3 + 2$: im Sattelpunkt $S(0 | "
                     "2)$ ist die Tangente waagerecht. (3) wahr, denn "
                     "$f'' > 0$ heißt linksgekrümmt."),
            pruef="")
    ersetze(be, 3,
            aufgabe=("Paul sagt: „Für $f(x) = x^4 + 3x$ ist $f''(0) = 0$, also "
                     "hat der Graph bei $0$ einen Wendepunkt.“ Begründe, ob "
                     "Paul recht hat."),
            loesung=("Nein; $f''(x) = 12x^2$ ist links und rechts von $0$ "
                     "positiv und wechselt das Vorzeichen nicht – der Graph "
                     "bleibt linksgekrümmt, bei $0$ liegt kein Wendepunkt."),
            pruef="")
    an = nimm(alt, 7, 3)
    ersetze(an, 3,
            aufgabe=("Eine Achterbahnschiene wird für $0 \\le x \\le 6$ durch "
                     "$f(x) = -0{,}1x^3 + 0{,}9x^2$ beschrieben ($x$ und "
                     "$f(x)$ in m). Auf dem linksgekrümmten Stück werden die "
                     "Fahrgäste in den Sitz gedrückt; dieses Stück soll in "
                     "$x$-Richtung mindestens $3$ m lang sein. Ist das "
                     "erfüllt?"),
            loesung=("Ja; zweite Ableitung: $f''(x) = -0{,}6x + 1{,}8$; "
                     "Bedingung $f''(x) = 0$: $x = 3$; Krümmung: $f''(x) > 0$ "
                     "für $0 \\le x < 3$, linksgekrümmt auf $[0; 3]$; "
                     "Vergleich: das Stück ist $3$ m lang, das reicht "
                     "genau."),
            pruef="3")

    zeilen = k1 + typen + fe + be + an
    zaehle(3, alt, zeilen)
    schreibe(3, ordne(zeilen, 3))


# ---------------------------------------------------------------- e4
def e4():
    alt = lade(4)
    g = nimm(alt, 1, 1)[0]
    m = ("Nullstellen und Vorzeichen von f' am Graphen von f; die Form des "
         "Graphen bleibt, er wandert nach links oder rechts")
    paeck = []
    for d in [1, -1, 2, 3, -2]:
        verschoben = f"(\\x-{d})" if d > 0 else f"(\\x+{-d})"
        a, b = d - 2, d + 2
        paeck.append(neu_zeile(
            g, merkmal=m,
            aufgabe=("Die Abbildung zeigt den Graphen von $f$. Gib die "
                     "Nullstellen von $f'$ an und trage das Vorzeichen von "
                     "$f'$ in jedem Abschnitt dazwischen ein."),
            loesung=(f"Nullstellen von $f'$: $x = {a}$ und $x = {b}$ (Hoch- "
                     f"und Tiefpunkt); $f' > 0$ für $x < {a}$, $f' < 0$ "
                     f"zwischen ${a}$ und ${b}$, $f' > 0$ für $x > {b}$"),
            pruef=f"[{a}, {b}]",
            grafik=(f"\\begin{{ksys}}[xmin={d - 4},xmax={d + 4},ymin=-5,"
                    f"ymax=5,ablesen] \\funktionab{{0.25*{verschoben}^3-3*"
                    f"{verschoben}}}{{f}}{{{d - 4}}}{{{d + 4}}} "
                    "\\end{ksys}")))
    varianten(paeck)

    s4 = []
    for tab, fkt, ks, ber, pkt, los in [
            ("Nullstellen & $-2$ und $4$ \\\\ Tiefpunkt & $T(-2 | 0)$ \\\\ "
             "Hochpunkt & $H(2 | 8)$ \\\\ Monotonie & fällt bis $-2$, steigt "
             "von $-2$ bis $2$, fällt ab $2$ \\\\ für $x \\to \\infty$ & "
             "$f(x) \\to -\\infty$ \\\\ Schnittpunkt mit der $y$-Achse & "
             "$(0 | 4)$",
             "-0.25*(\\x+2)^2*(\\x-4)", "xmin=-3,xmax=5,ymin=-3,ymax=9",
             "{-3}{4.8}", "\\tiefpunkt{-2}{0}{T} \\hochpunkt{2}{8}{H}",
             "Der Graph kommt von links oben, fällt bis zum Tiefpunkt "
             "$T(-2 | 0)$ auf der $x$-Achse, steigt durch $(0 | 4)$ bis zum "
             "Hochpunkt $H(2 | 8)$, fällt dann nach rechts unten und "
             "schneidet die $x$-Achse bei $4$."),
            ("Nullstellen & $0$ und $3$ \\\\ Hochpunkt & $H(0 | 0)$ \\\\ "
             "Tiefpunkt & $T(2 | -2)$ \\\\ Monotonie & steigt bis $0$, fällt "
             "von $0$ bis $2$, steigt ab $2$ \\\\ für $x \\to \\infty$ & "
             "$f(x) \\to \\infty$ \\\\ Schnittpunkt mit der $y$-Achse & "
             "$(0 | 0)$",
             "0.5*\\x^3-1.5*\\x^2", "xmin=-2,xmax=4,ymin=-3,ymax=4",
             "{-1}{3.5}", "\\hochpunkt{0}{0}{H} \\tiefpunkt{2}{-2}{T}",
             "Der Graph kommt von links unten, steigt bis zum Hochpunkt "
             "$H(0 | 0)$ im Ursprung, fällt bis zum Tiefpunkt $T(2 | -2)$, "
             "steigt dann nach rechts oben und schneidet die $x$-Achse bei "
             "$3$."),
            ("Nullstellen & $-3$ und $0$ \\\\ Tiefpunkt & $T(-3 | 0)$ \\\\ "
             "Hochpunkt & $H(-1 | 1)$ \\\\ Monotonie & fällt bis $-3$, "
             "steigt von $-3$ bis $-1$, fällt ab $-1$ \\\\ für $x \\to "
             "\\infty$ & $f(x) \\to -\\infty$ \\\\ Schnittpunkt mit der "
             "$y$-Achse & der Ursprung",
             "-0.25*\\x*(\\x+3)^2", "xmin=-5,xmax=2,ymin=-3,ymax=3",
             "{-4.5}{1.2}", "\\tiefpunkt{-3}{0}{T} \\hochpunkt{-1}{1}{H}",
             "Der Graph kommt von links oben, fällt bis zum Tiefpunkt "
             "$T(-3 | 0)$ auf der $x$-Achse, steigt bis zum Hochpunkt "
             "$H(-1 | 1)$, fällt dann durch den Ursprung nach rechts "
             "unten.")]:
        s4.append(neu_zeile(
            g, sprosse=4, hoehe="sprosse", sprosse_text=T_E4_S4,
            merkmal="Graph aus einer ausgefüllten Übersicht skizzieren, ohne "
                    "Rechnung",
            aufgabe=("Von einer ganzrationalen Funktion $f$ dritten Grades "
                     "kennst du diese Übersicht. \\sachtabelle{ll}{Eigenschaft "
                     f"& Angabe}}{{{tab}}} Skizziere den Graphen von $f$ in das "
                     "Koordinatensystem. Rechne nichts aus."),
            form="zeichnen", antwort="", loesung=los, pruef="",
            grafik=f"\\begin{{ksys}}[{ks}]  \\end{{ksys}}",
            loesungsgrafik=(f"\\begin{{ksys}}[{ks},klein] \\funktionab{{{fkt}}}"
                            f"{{f}}{ber} {pkt} \\end{{ksys}}"),
            original=None, quelle=130))
    varianten(s4)

    k1 = (nimm(alt, 1, 0) + paeck + nimm(alt, 1, 2) + nimm(alt, 1, 3) + s4)
    for s in range(4, 9):
        for a in nimm(alt, 1, s):
            a["sprosse"] = s + 1
            k1.append(a)
    typen = [a for a in alt if a["kette_nr"] in (2, 3)]

    fe = nimm(alt, 4, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    ersetze(fe, 2,
            aufgabe=("Die Abbildung zeigt den Graphen von $f'$. Ben liest ab: "
                     "„$f$ hat bei $x = 2$ einen Tiefpunkt, weil $f'$ dort von "
                     "minus nach plus wechselt.“ Prüfe, ob Ben richtig "
                     "abgelesen hat."),
            loesung=("Richtig. Eine Nullstelle von $f'$ mit Vorzeichenwechsel "
                     "von minus nach plus ist eine Tiefstelle von $f$."),
            pruef="",
            grafik=("\\begin{ksys}[xmin=-3,xmax=3,ymin=-3,ymax=3,ablesen] "
                    "\\funktionab{0.5*\\x^2-2}{f'}{-3}{3} \\end{ksys}"))
    ersetze(fe, 3,
            aufgabe=("Die Abbildung zeigt den Graphen von $f$ mit dem "
                     "Hochpunkt bei $x = -1$ und dem Tiefpunkt bei $x = 1$. "
                     "Vier Schüler haben Ableitungswerte notiert. Welche "
                     "Ergebnisse können nicht stimmen? Begründe, ohne genau "
                     "zu rechnen. \\\\ (1) $f'(-1) = 1$ \\\\ (2) $f'(0) = "
                     "-1{,}5$ \\\\ (3) $f'(2) = -4{,}5$ \\\\ (4) $f'(-2) = "
                     "4{,}5$"),
            loesung=("Nicht stimmen können (1) und (3). (1): Im Hochpunkt ist "
                     "die Tangente waagerecht, also $f'(-1) = 0$. (3): Bei "
                     "$x = 2$ steigt der Graph, $f'(2)$ muss positiv sein. "
                     "(2) und (4) können stimmen: bei $0$ fällt der Graph, "
                     "bei $-2$ steigt er."),
            pruef="",
            grafik=("\\begin{ksys}[xmin=-3,xmax=3,ymin=-3,ymax=3,ablesen] "
                    "\\funktionab{0.5*\\x^3-1.5*\\x}{f}{-2.3}{2.3} "
                    "\\end{ksys}"))
    be = nimm(alt, 4, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    ersetze(be, 2,
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe. \\\\ (1) Ist $f$ eine ganzrationale "
                     "Funktion dritten Grades, so ist der Graph von $f'$ eine "
                     "Parabel. \\\\ (2) Wo $f'$ eine Nullstelle hat, hat der "
                     "Graph von $f$ immer einen Hoch- oder Tiefpunkt. \\\\ "
                     "(3) Wo der Graph von $f'$ oberhalb der $x$-Achse "
                     "liegt, steigt der Graph von $f$."),
            loesung=("(1) wahr, denn beim Ableiten sinkt der Grad um eins, "
                     "aus $x^3$ wird ein $x^2$-Glied. (2) falsch, z. B. "
                     "$f(x) = x^3 + 1$: $f'(0) = 0$, aber ohne "
                     "Vorzeichenwechsel – Sattelpunkt. (3) wahr, denn "
                     "$f' > 0$ heißt, $f$ steigt."),
            pruef="")
    ersetze(be, 3,
            aufgabe=("Emma sagt: „Wo der Graph von $f'$ seinen Hochpunkt hat, "
                     "hat auch der Graph von $f$ einen Hochpunkt.“ Begründe, "
                     "ob Emma recht hat."),
            loesung=("Nein; im Hochpunkt von $f'$ ist die Steigung von $f$ am "
                     "größten, dort steigt $f$ am stärksten – das ist ein "
                     "Wendepunkt von $f$, kein Hochpunkt."),
            pruef="")
    da = nimm(alt, 4, 3)
    for a in da:
        a["merkmal"] = ("Darstellungswechsel in zwei Richtungen: vom Graphen "
                        "von f zum Graphen von f' und zurück")
    ersetze(da, 1,
            aufgabe=("Die Abbildung zeigt den Graphen von $f$. Zeichne den "
                     "Graphen von $f'$ in dasselbe Koordinatensystem."),
            loesung=("Der Tiefpunkt von $f$ bei $x = 2$ ist die Nullstelle von "
                     "$f'$; links davon fällt $f$ ($f' < 0$), rechts steigt "
                     "es ($f' > 0$). $f$ ist eine Parabel, also ist $f'$ eine "
                     "Gerade durch $(2 | 0)$, etwa auch durch $(0 | -1)$ und "
                     "$(4 | 1)$."),
            pruef="",
            grafik=("\\begin{ksys}[xmin=-2,xmax=6,ymin=-3,ymax=4] "
                    "\\funktionab{0.25*\\x^2-\\x}{f}{-2}{6} \\end{ksys}"),
            loesungsgrafik=("\\begin{ksys}[xmin=-2,xmax=6,ymin=-3,ymax=4,"
                            "klein] \\funktionab{0.25*\\x^2-\\x}{f}{-2}{6} "
                            "\\funktionab{0.5*\\x-1}{f'}{-2}{6} "
                            "\\end{ksys}"))

    zeilen = k1 + typen + fe + be + da
    zaehle(4, alt, zeilen)
    schreibe(4, ordne(zeilen, 4))


# ---------------------------------------------------------------- e5
def e5():
    alt = lade(5)
    vor = nimm(alt, 1, 0)
    for a in vor:
        a["sprosse_text"] = T_E5_S0
    g = nimm(alt, 1, 1)[0]
    m = ("Verlauf abschnittweise in Worten des Sachzusammenhangs; die "
         "Raumtemperatur 20 °C bleibt, die Anfangstemperatur wandert")
    paeck = []
    for t0 in [90, 60, 4, 45, 10]:
        if t0 > 20:
            los = (f"Die Temperatur fällt von ${t0}$ °C zunächst schnell, "
                   "dann immer langsamer und nähert sich $20$ °C, der "
                   "Raumtemperatur; sie sinkt nicht darunter.")
        else:
            los = (f"Die Temperatur steigt von ${t0}$ °C zunächst schnell, "
                   "dann immer langsamer und nähert sich $20$ °C, der "
                   "Raumtemperatur; sie steigt nicht darüber.")
        k = t0 - 20
        paeck.append(neu_zeile(
            g, merkmal=m,
            aufgabe=("Ein Getränk wird in einen Raum mit $20$ °C gebracht. Die "
                     "Abbildung zeigt seine Temperatur $T$ (in °C) $t$ Minuten "
                     "danach. Beschreibe den Verlauf im Sachzusammenhang."),
            loesung=los, pruef=str(t0),
            grafik=("\\begin{ksys}[xmin=0,xmax=40,ymin=0,ymax=100,xstep=10,"
                    "ystep=20,xlabel=t in min,ylabel=T in °C,ablesen] "
                    f"\\funktionab{{20{'+' if k > 0 else '-'}{abs(k)}*"
                    "exp(-0.1*\\x)}{T}{0}{40} \\end{ksys}")))
    varianten(paeck)
    k1 = vor + paeck + [a for s in range(2, 10) for a in nimm(alt, 1, s)]
    typen = [a for a in alt if a["kette_nr"] in (2, 3)]

    fe = nimm(alt, 4, 1)
    for a in fe:
        a["merkmal"] = M_FEHLER
    ersetze(fe, 1,
            aufgabe=("Der Graph der Höhe $h$ eines Ballons hat bei $t = 10$ "
                     "einen Wendepunkt und bei $t = 20$ seinen Hochpunkt ($t$ "
                     "in min); vorher steigt der Ballon. Tom schreibt: „Bei "
                     "$t = 10$ steigt der Ballon am schnellsten; bis $t = 20$ "
                     "steigt er weiter, aber langsamer.“ Prüfe, ob Tom "
                     "richtig gedeutet hat."),
            loesung=("Richtig. Im Wendepunkt im steigenden Bereich ist $h'$ "
                     "am größten; danach bleibt $h' > 0$ bis zum Hochpunkt, "
                     "der Ballon steigt also weiter, nur langsamer."),
            pruef="")
    ersetze(fe, 3,
            aufgabe=("Die Höhe $h(t)$ einer Pflanze (in cm) wird für die "
                     "ersten $30$ Tage modelliert, $0 \\le t \\le 30$. Vier "
                     "Schüler haben Ergebnisse notiert. Welche Ergebnisse "
                     "können nicht stimmen? Begründe, ohne genau zu rechnen. "
                     "\\\\ (1) Die Pflanze wächst am stärksten nach $-4$ "
                     "Tagen. \\\\ (2) Die größte Wachstumsrate beträgt $3$ "
                     "cm. \\\\ (3) Die größte Wachstumsrate beträgt $3$ cm "
                     "pro Tag. \\\\ (4) Nach $40$ Tagen ist die Pflanze am "
                     "höchsten."),
            loesung=("Nicht stimmen können (1), (2) und (4). (1): $-4$ liegt "
                     "außerhalb des Bereichs $0 \\le t \\le 30$. (2): Eine "
                     "Rate hat die Einheit cm pro Tag, nicht cm. (4): $40$ "
                     "liegt außerhalb des Modellbereichs. (3) kann "
                     "stimmen."),
            pruef="")
    be = nimm(alt, 4, 2)
    for a in be:
        a["merkmal"] = M_BEGR
    ersetze(be, 2,
            aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                     "ist. Begründe. \\\\ (1) Im Wendepunkt ändert sich immer "
                     "die Richtung: aus Zunahme wird Abnahme. \\\\ (2) Wo der "
                     "Graph von $f'$ seinen Hochpunkt hat, nimmt $f$ am "
                     "stärksten zu. \\\\ (3) Ist $B$ in Stück und $t$ in "
                     "Tagen gemessen, so hat $B'(t)$ die Einheit Stück pro "
                     "Tag."),
            loesung=("(1) falsch, z. B. ein Ballon, der bis zum Wendepunkt "
                     "immer schneller und danach langsamer steigt – er "
                     "steigt weiter. (2) wahr, denn $f'$ ist die Änderungsrate "
                     "von $f$, ihr größter Wert ist die stärkste Zunahme. "
                     "(3) wahr, denn $B'$ ist Änderung von $B$ pro "
                     "Zeiteinheit."),
            pruef="")
    ersetze(be, 3,
            aufgabe=("Nora sagt: „Wenn der Wasserstand eines Sees immer "
                     "langsamer steigt, dann ist $h'(t) > 0$ und $h''(t) < "
                     "0$.“ Begründe, ob Nora recht hat."),
            loesung=("Ja; der Wasserstand steigt, also $h'(t) > 0$, und die "
                     "Steigrate nimmt ab, also fällt $h'$ und es gilt "
                     "$h''(t) < 0$."),
            pruef="")
    an = nimm(alt, 4, 3)
    ersetze(an, 1, loesung=(
        "Nein; Ableitungen bilden: $f'(x) = -0{,}012x^2 + 0{,}18x$, $f''(x) = "
        "-0{,}024x + 0{,}18$; Bedingung $f''(x) = 0$: $x = 7{,}5$; Punkt: "
        "$f(7{,}5) \\approx 5{,}38$; Steigung: $f'(7{,}5) = 0{,}675$; Winkel: "
        "$\\mathrm{tan}\\,\\alpha = 0{,}675$, also $\\alpha \\approx 34{,}0° > "
        "30°$ – die Bedingung ist nicht erfüllt."))
    ersetze(an, 2, loesung=(
        "Ja; Bedingung $f''(x) = 0$: $x = 5$; Steigung: $f'(5) = -2{,}5\\,"
        "\\mathrm{e}^{-1} \\approx -0{,}92$; Winkel: $\\mathrm{tan}\\,\\alpha "
        "= 0{,}92$, also $\\alpha \\approx 42{,}6° < 45°$ – die Bedingung ist "
        "erfüllt; am Anfang ist $f'(0) = 0$, dort ist die Rutsche nicht am "
        "steilsten."))
    da = nimm(alt, 4, 4)
    for a in da:
        a["merkmal"] = ("Darstellungswechsel in zwei Richtungen: aus Graph "
                        "und Gerade den Bereich ablesen, aus Worten einen "
                        "Graphen skizzieren")
    ersetze(da, 3,
            aufgabe=("Die Temperatur in einem Raum steigt ab $6$ Uhr zuerst "
                     "langsam, dann immer schneller; ab $10$ Uhr steigt sie "
                     "langsamer und ist um $14$ Uhr mit gut $26$ °C am "
                     "höchsten; bis $18$ Uhr sinkt sie wieder auf $18$ °C, "
                     "den Wert von $6$ Uhr. Skizziere einen möglichen Graphen "
                     "in das Koordinatensystem und markiere den "
                     "Wendepunkt."),
            loesung=("Tiefster Wert $18$ °C um $6$ Uhr, Wendepunkt um $10$ Uhr "
                     "(dort steigt die Temperatur am schnellsten), Hochpunkt "
                     "um $14$ Uhr bei gut $26$ °C, danach fallend bis $18$ °C "
                     "um $18$ Uhr."),
            pruef="",
            grafik=("\\begin{ksys}[xmin=6,xmax=18,ymin=15,ymax=30,xstep=2,"
                    "ystep=5,xlabel=t in h,ylabel=T in °C]  \\end{ksys}"),
            loesungsgrafik=("\\begin{ksys}[xmin=6,xmax=18,ymin=15,ymax=30,"
                            "xstep=2,ystep=5,xlabel=t in h,ylabel=T in °C,"
                            "klein] \\funktionab{18+0.1*(4*(\\x-6)^2-(\\x-6)"
                            "^3/3)}{T}{6}{18} \\wendepunkt{10}{22.27}{W} "
                            "\\hochpunkt{14}{26.53}{H} \\end{ksys}"))

    zeilen = k1 + typen + fe + be + an + da
    zaehle(5, alt, zeilen)
    schreibe(5, ordne(zeilen, 5))


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["1", "2", "3", "4", "5"]
    for n in wahl:
        {"1": e1, "2": e2, "3": e3, "4": e4, "5": e5}[n]()
    print(json.dumps(ZAEHL, ensure_ascii=False))

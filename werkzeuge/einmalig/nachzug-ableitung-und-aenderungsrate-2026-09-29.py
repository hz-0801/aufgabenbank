"""Nachzug bank/ableitung-und-aenderungsrate auf Katalog 2a296e5 (Mappe 29.09.).

Einmalig, 2026-09-29. Liest den Bestand (Katalog 95b0f8b, 27./28.09.,
Gegenlese 28.09.) und zieht ihn auf bank.md fünfte Fassung und die
Vorlage 2026-09-29e nach:
- sprosse_text der Prüfungssprossen e1 s10, e2 s8, e4 s9 wortgleich
  zur Katalogzeile (die Sprossen fassen jetzt mehrere Originale);
- e3: neue Sprosse s2 „Tangente mit dem Lineal anlegen …“ (Grafik),
  die alten s2–s7 rücken auf s3–s8;
- Grundfall je Verfahrenskette als Päckchen (fünf Zeilen, ein Wert
  bleibt, einer wandert), Lösungen mit Schrittnamen;
- Pooldubletten: die Bankzeile trägt die Kennung, die in der Mappe
  zuerst steht (bank.md, 29.09.);
- Pflichtformen: fehler (Schülerrechnung, P2, P1), begruenden
  („Begründe, warum“, P4, P6), anwendung mit P8, darstellung mit
  einer Richtung rückwärts (e4).
Zählt je Einheit übernommen/neu/umgeschrieben/entfallen.
Aufruf aus der Wurzel des Repos:
    python3 werkzeuge/einmalig/nachzug-ableitung-und-aenderungsrate-2026-09-29.py [e1 …]
"""
import copy
import json
import sys
from pathlib import Path

E = "ableitung-und-aenderungsrate"
B = Path("bank") / E
ZAEHL = {}

FELDER = ["id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
          "sprosse_text", "merkmal", "hoehe", "pflicht", "variante",
          "aufgabe", "form", "antwort", "loesung", "pruef", "original",
          "grafik", "loesungsgrafik", "quelle"]
NACHGEZOGEN = ("id", "sprosse", "kette_nr", "quelle", "sprosse_text",
               "variante", "_neu", "_alt")

M_FEHLER = ("Rechnung prüfen: Fehler finden, richtige Rechnung erkennen, "
            "unmögliche Ergebnisse erkennen")
M_BEGR = ("begründen: Regel beim Namen, Aussagen beurteilen, "
          "Behauptung beurteilen")

# Pooldubletten: Kennung aus dem Pool -> Kennung, die in der Mappe
# (Abschnitt 2) zuerst steht.
DUBLETTE = {
    "2024MerhoehtBAnalysisWTR2-2a": ("2024-bebb-lk-B2.2f", 2024,
                                     "2024-bebb-lk"),
    "2024MgrundlegendAAnalysis13-a": ("2024-bebb-gk-A1.4a", 2024,
                                      "2024-bebb-gk"),
    "2023MerhoehtBAnalysisWTR1-1b": ("2023-bebb-lk-B2.2b", 2023,
                                     "2023-bebb-lk"),
    "2026MgrundlegendBAnalysisWTR2-2b": ("2026-bb-gk-B2.2h", 2026,
                                         "2026-bb-gk"),
    "2025MerhoehtAAnalysis23-b": ("2025-bebb-lk-A1.6b", 2025,
                                  "2025-bebb-lk"),
    "2026MgrundlegendBAnalysisWTR2-2c": ("2026-bb-gk-B2.2i", 2026,
                                         "2026-bb-gk"),
}
UMBENANNT = []          # ids, deren original umgestellt wurde

T_E1_PR = ("Zusatzkosten als Differenzen aufeinanderfolgender "
           "Funktionswerte mit einem Gegenbeispiel beurteilen (iqb "
           "2018MgrundlegendBAnalysisWTR-2c, Niveau III) und den "
           "Differenzenquotienten über Einheitsintervalle einer "
           "e-Funktion als Term nachweisen und den Zeitpunkt des "
           "Unterschreitens einer Schranke berechnen (iqb "
           "2019MgrundlegendBAnalysisWTR2-2d, Niveau III)")
T_E2_PR = ("eine Aussage über die Steigung in einem Intervall am Graphen "
           "beurteilen, indem die steilste Stelle gesucht wird (iqb "
           "2023MerhoehtAAnalysis13-a, Teil A, Niveau II), und eine "
           "Allaussage über die Steigungen zweier Graphen durch eine "
           "Stelle widerlegen, an der die Ableitungswerte sie verletzen "
           "(iqb 2020MgrundlegendBAnalysisWTR1-1c, Niveau II)")
T_E4_PR = ("die Zeitpunkte größter Differenz zweier Raten über die "
           "Extremstellen der Differenzfunktion berechnen (abi "
           "2019-be-gk-B2.1e, Niveau II) und eine Beziehung f − c = k · f' "
           "zwischen Bestand und Rate am Term nachweisen (abi "
           "2026-bb-gk-B2.2i; iqb 2026MgrundlegendBAnalysisWTR2-2c, "
           "Niveau III)")
T_E3_S2 = ("Tangente mit dem Lineal anlegen, Steigung am Steigungsdreieck "
           "messen, dann rechnen und vergleichen")


def lade(n):
    return [json.loads(z) for z in
            (B / f"e{n}.jsonl").read_text(encoding="utf-8").splitlines()]


def nimm(zeilen, k, s):
    aus = []
    for a in zeilen:
        if a["kette_nr"] == k and a["sprosse"] == s:
            b = copy.deepcopy(a)
            b["_alt"] = a["id"]
            aus.append(b)
    return aus


def neu(vorlage, **kw):
    a = copy.deepcopy(vorlage)
    a.pop("_alt", None)
    if kw.get("hoehe", a["hoehe"]) != "pflicht":
        a.pop("pflicht", None)
    a.update(kw)
    a["_neu"] = True
    return a


def um(vorlage, **kw):
    a = copy.deepcopy(vorlage)
    a.update(kw)
    return a


def varianten(zeilen):
    for i, a in enumerate(zeilen, 1):
        a["variante"] = i
    return zeilen


def dubletten(zeilen):
    for a in zeilen:
        o = a.get("original")
        if o and o["id"] in DUBLETTE:
            i, j, p = DUBLETTE[o["id"]]
            a["original"] = {"id": i, "jahr": j, "papier": p}
            UMBENANNT.append(a.get("_alt", "?"))
    return zeilen


def ordne(zeilen, einheit):
    aus = []
    for a in zeilen:
        a["id"] = (f"{E}-e{einheit}-k{a['kette_nr']}"
                   f"-s{a['sprosse']}-v{a['variante']}")
        extra = {k: a[k] for k in ("_neu", "_alt") if k in a}
        aus.append({f: a[f] for f in FELDER if f in a} | extra)
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
    ids_alt = {a["_alt"] for a in zeilen if "_alt" in a}
    ids_orig = sum(1 for a in zeilen if a.get("original") and "_alt" in a
                   and a["_alt"] != a["id"])
    ZAEHL[f"e{n}"] = dict(uebernommen=ueb, neu=nn, umgeschrieben=umg,
                          entfallen=len(alt) - len(ids_alt),
                          ids_mit_original_geaendert=ids_orig)


def schreibe(n, alt, zeilen):
    zeilen = ordne(dubletten(zeilen), n)
    zaehle(n, alt, zeilen)
    for a in zeilen:
        a.pop("_neu", None)
        a.pop("_alt", None)
    text = "".join(json.dumps(a, ensure_ascii=False) + "\n" for a in zeilen)
    (B / f"e{n}.jsonl").write_text(text, encoding="utf-8")


def rest(alt, *schluessel):
    aus = []
    for k, s in schluessel:
        aus += nimm(alt, k, s)
    return aus


def text_setzen(zeilen, text):
    for a in zeilen:
        a["sprosse_text"] = text
    return zeilen


def merkmal_setzen(zeilen, m):
    for a in zeilen:
        a["merkmal"] = m
    return zeilen


# ---------------------------------------------------------------- e1
def e1():
    alt = lade(1)
    aus = rest(alt, (1, 0))
    g = nimm(alt, 1, 1)
    m1 = ("Grundfall: Wassermenge zu Beginn 120 Liter und Zeitraum "
          "4 Stunden bleiben, die Menge am Ende wandert (auch kleiner als "
          "zu Beginn); Differenz durch Länge, Einheit „je“")
    gf = []
    for ende in (200, 260, 320, 100, 40):
        d = ende - 120
        r = d // 4
        gf.append(um(
            g[0], merkmal=m1,
            aufgabe=(f"Zu Beginn einer Messung sind $120$ Liter Wasser in "
                     f"einem Becken, $4$ Stunden später ${ende}$ Liter. "
                     "Berechne die mittlere Änderungsrate der Wassermenge "
                     "in diesem Zeitraum."),
            antwort="__ Liter je Stunde",
            loesung=(f"Differenz: ${ende} - 120 = {d}$; durch die Länge "
                     f"des Zeitraums teilen: $\\frac{{{d}}}{{4}} = {r}$; "
                     f"Ergebnis: ${r}$ Liter je Stunde"),
            pruef=f"({ende}-120)/4"))
    for i, a in enumerate(gf):
        a["_alt"] = g[i]["_alt"]
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 10)])
    aus += text_setzen(nimm(alt, 1, 10), T_E1_PR)
    # Pflicht fehler: v1 Schülerrechnung, v2 P2 fehlerfrei, v3 P1 Serie
    fe = merkmal_setzen(nimm(alt, 2, 1), M_FEHLER)
    fe[1] = um(
        fe[1],
        aufgabe=("Bei einer Messe werden um 13:30 Uhr $900$ Besucher "
                 "gezählt, um 15:00 Uhr $2\\,100$. Tom berechnet die "
                 "mittlere Änderungsrate der Besucherzahl: "
                 "\\rechnung{\\frac{2\\,100 - 900}{1{,}5} &= 800} Er "
                 "schreibt: „$800$ Besucher je Stunde.“ Prüfe, ob Tom "
                 "richtig gerechnet hat."),
        loesung=("Richtig. Tom teilt die Änderung durch die Länge des "
                 "Zeitraums in Stunden: von 13:30 bis 15:00 Uhr sind es "
                 "$1{,}5$ Stunden, und die Einheit ist Besucher je "
                 "Stunde."),
        pruef="")
    fe[2] = um(
        fe[2],
        aufgabe=("Der Wasserstand eines Sees sinkt in $5$ Tagen von "
                 "$3{,}40$ m auf $3{,}15$ m. Vier Schüler geben die "
                 "mittlere Änderungsrate an. Welche Ergebnisse können "
                 "nicht stimmen? Begründe, ohne genau zu rechnen. \\\\ "
                 "(1) $0{,}05$ m je Tag \\\\ (2) $-0{,}25$ m \\\\ "
                 "(3) $-0{,}05$ m je Tag \\\\ (4) $-1{,}25$ m je Tag"),
        loesung=("Nicht stimmen können (1), (2) und (4). (1): Der "
                 "Wasserstand sinkt, die Rate muss negativ sein. (2): Die "
                 "Einheit m gehört zu einer Differenz, eine Rate hat die "
                 "Einheit m je Tag. (4): Der Betrag ist größer als die "
                 "ganze Änderung von $0{,}25$ m in fünf Tagen, je Tag muss "
                 "er kleiner sein. (3) kann stimmen."),
        pruef="")
    aus += fe
    # Pflicht begruenden: v1 „Begründe, warum“, v2 P4, v3 P6
    be = merkmal_setzen(nimm(alt, 2, 2), M_BEGR)
    be[1] = um(
        be[1],
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. \\\\ (1) Die mittlere Änderungsrate auf "
                 "einem Intervall ist immer die Steigung der Sekante durch "
                 "die beiden Randpunkte des Graphen. \\\\ (2) Ist die "
                 "mittlere Änderungsrate auf einem Intervall null, so ist "
                 "die Größe in diesem Zeitraum nie gestiegen. \\\\ (3) Es "
                 "gibt Zeiträume, in denen die mittlere Änderungsrate "
                 "negativ ist, obwohl die Größe zwischendurch steigt."),
        loesung=("(1) wahr, denn die Sekantensteigung ist Höhenunterschied "
                 "durch waagerechten Unterschied, also genau der "
                 "Differenzenquotient. (2) falsch, z. B. steigt ein "
                 "Wasserstand von $40$ cm auf $55$ cm und fällt wieder auf "
                 "$40$ cm: die mittlere Rate ist null, obwohl er gestiegen "
                 "ist. (3) wahr, denn es zählen nur Anfangs- und Endwert: "
                 "steigt eine Größe von $10$ auf $30$ und fällt dann auf "
                 "$5$, ist die mittlere Rate negativ."),
        pruef="")
    be[2] = um(
        be[2],
        aufgabe=("Ein Wasserstand steigt zwischen der zweiten und der "
                 "fünften Stunde um $30$ cm, zwischen der fünften und der "
                 "sechsten Stunde um $12$ cm. Lukas sagt: „Im ersten "
                 "Zeitraum ist der Wasserstand stärker gestiegen, aber im "
                 "zweiten Zeitraum war die mittlere Änderungsrate größer.“ "
                 "Begründe, ohne genau zu rechnen, ob Lukas recht hat."),
        loesung=("Ja; die mittlere Änderungsrate ist die Änderung je "
                 "Stunde, nicht die Änderung selbst: $30$ cm verteilen sich "
                 "auf drei Stunden, also weniger als $12$ cm je Stunde, "
                 "$12$ cm stehen für eine einzige Stunde."),
        pruef="")
    aus += be
    # Pflicht anwendung: v1 und v2 mit dem Urteil zuerst (P8)
    an = nimm(alt, 2, 3)
    an[0] = um(
        an[0],
        loesung=("Nein; Differenzenquotient: $\\frac{380 - 800}{6} = -70$ "
                 "Liter je Stunde; Vergleich: der Verbrauch liegt im Mittel "
                 "bei $70$ Litern je Stunde und damit über $60$ Litern je "
                 "Stunde."))
    an[1] = um(
        an[1],
        loesung=("Nein; Differenzenquotient: $\\frac{E(10) - E(0)}{10} "
                 "\\approx 3167$ Einwohner je Jahr; Vergleich: im Mittel "
                 "kommen mehr als $3\\,000$ Einwohner je Jahr hinzu, die "
                 "Planung reicht knapp nicht."))
    aus += an
    aus += rest(alt, (2, 4))
    schreibe(1, alt, aus)


# ---------------------------------------------------------------- e2
def e2():
    alt = lade(2)
    aus = rest(alt, (1, 0))
    g = nimm(alt, 1, 1)
    m1 = ("Grundfall: Wasserstand w(t) = t³ − 6t² + c·t + 40 an der Stelle "
          "3; die Stelle bleibt, der Faktor c wandert; Ergebnis als Rate "
          "mit Einheit und Vorzeichen gedeutet")
    gf = []
    for c, w in ((12, 3), (5, -4), (9, 0), (15, 6), (20, 11)):
        if w > 0:
            deut = f"der Wasserstand steigt in diesem Moment um ${w}$ cm je Stunde"
        elif w < 0:
            deut = (f"der Wasserstand sinkt in diesem Moment um ${-w}$ cm "
                    "je Stunde")
        else:
            deut = "der Wasserstand ändert sich in diesem Moment nicht"
        gf.append(um(
            g[0], merkmal=m1,
            aufgabe=("Der Wasserstand in einem Hafenbecken wird durch "
                     f"$w(t) = t^3 - 6t^2 + {c}t + 40$ beschrieben ($t$ in "
                     "Stunden, $w(t)$ in cm). Berechne $w'(3)$ und gib an, "
                     "was die Zahl bedeutet."),
            antwort="w'(3) = __ cm je Stunde",
            loesung=(f"ableiten: $w'(t) = 3t^2 - 12t + {c}$; Stelle "
                     f"einsetzen: $w'(3) = 27 - 36 + {c} = {w}$; Ergebnis: "
                     f"$w'(3) = {w}$ cm je Stunde – {deut}"),
            pruef=str(w)))
    for i, a in enumerate(gf):
        a["_alt"] = g[i]["_alt"]
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 8)])
    aus += text_setzen(nimm(alt, 1, 8), T_E2_PR)
    aus += rest(alt, (2, 1), (3, 1))
    # fehler: v1 Schülerrechnung, v2 P2, v3 P1
    fe = merkmal_setzen(nimm(alt, 4, 1), M_FEHLER)
    fe[1] = um(
        fe[1],
        aufgabe=("Für $g(x) = 0{,}5\\mathrm{e}^x + 1$ rechnet Nina: "
                 "\\rechnung{g'(x) &= 0{,}5\\mathrm{e}^x \\\\ g'(0) &= "
                 "0{,}5} Sie schreibt: „Der Graph von $g$ steigt an der "
                 "Stelle $0$ mit der Steigung $0{,}5$.“ Prüfe, ob Nina "
                 "richtig gerechnet hat."),
        loesung=("Richtig. Die Konstante $1$ fällt beim Ableiten weg, denn "
                 "die Ableitung einer Konstanten ist null (Summenregel), "
                 "und $\\mathrm{e}^0 = 1$."),
        pruef="")
    fe[2] = um(
        fe[2],
        aufgabe=("Ein Ballon sinkt; seine Höhe wird durch $h(t) = 80 - "
                 "0{,}5t^2$ beschrieben ($t$ in s, $h(t)$ in m). Vier "
                 "Schüler geben die momentane Änderungsrate $h'(4)$ an. "
                 "Welche Ergebnisse können nicht stimmen? Begründe, ohne "
                 "genau zu rechnen. \\\\ (1) $4$ m je s \\\\ (2) $72$ m "
                 "\\\\ (3) $-4$ m je s \\\\ (4) $-4$ m"),
        loesung=("Nicht stimmen können (1), (2) und (4). (1): Die Höhe "
                 "nimmt ab, die Rate muss negativ sein. (2): $72$ m ist "
                 "eine Höhe, also ein Funktionswert und keine Steigung. "
                 "(4): Eine Rate hat die Einheit m je s, nicht m. (3) kann "
                 "stimmen."),
        pruef="")
    aus += fe
    # begruenden: v1 „Begründe, warum“, v2 P4, v3 P6
    be = merkmal_setzen(nimm(alt, 4, 2), M_BEGR)
    be[1] = um(
        be[1],
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. \\\\ (1) Ist der Funktionswert an einer "
                 "Stelle null, so ist dort immer auch die Ableitung null. "
                 "\\\\ (2) Es gibt Funktionen, deren Ableitung an einer "
                 "Stelle null ist, obwohl der Funktionswert dort nicht null "
                 "ist. \\\\ (3) Ist $f'(x_0)$ negativ, so ist immer auch "
                 "$f(x_0)$ negativ."),
        loesung=("(1) falsch, z. B. ist für $f(x) = 2x$ zwar $f(0) = 0$, "
                 "aber $f'(0) = 2$. (2) wahr, denn für $f(x) = x^2 + 3$ ist "
                 "$f'(0) = 0$ und $f(0) = 3$. (3) falsch, z. B. ist für "
                 "$f(x) = 10 - x^2$ an der Stelle $1$ die Ableitung "
                 "$f'(1) = -2$ negativ, der Funktionswert $f(1) = 9$ "
                 "positiv."),
        pruef="")
    be[2] = um(
        be[2],
        aufgabe=("Für eine Funktion $f$ gilt $f(1) = 3$ und $f(2) = 5$. "
                 "Emma sagt: „Dann ist der Graph von $f$ an der Stelle $2$ "
                 "steiler als an der Stelle $1$.“ Begründe, ohne zu "
                 "rechnen, ob Emma recht hat."),
        loesung=("Nein; Funktionswerte sagen, wie hoch der Graph liegt, "
                 "nicht wie steil er ist – über die Steigung an den Stellen "
                 "$1$ und $2$ entscheiden erst $f'(1)$ und $f'(2)$, und die "
                 "sind nicht gegeben."),
        pruef="")
    aus += be
    # anwendung: v1 mit Entscheidung am Grenzwert (P8)
    an = nimm(alt, 4, 3)
    an[0] = um(
        an[0],
        aufgabe=("Die Höhe eines Heißluftballons wird durch $h(t) = "
                 "-0{,}5t^2 + 12t$ beschrieben ($t$ in Minuten nach dem "
                 "Start, $h(t)$ in m). Der Pilot darf die Landeleine erst "
                 "auswerfen, wenn der Ballon höchstens noch mit $4$ m je "
                 "Minute steigt. Er plant den Wurf neun Minuten nach dem "
                 "Start. Darf er dann werfen?"),
        loesung=("Ja; ableiten: $h'(t) = -t + 12$; Stelle bestimmen: "
                 "$-t + 12 = 4$, also $t = 8$; Vergleich: ab der achten "
                 "Minute steigt der Ballon höchstens mit $4$ m je Minute, "
                 "neun Minuten nach dem Start darf er werfen."),
        pruef="8")
    aus += an
    aus += rest(alt, (4, 4))
    schreibe(2, alt, aus)


# ---------------------------------------------------------------- e3
def e3():
    alt = lade(3)
    aus = rest(alt, (1, 0))
    g = nimm(alt, 1, 1)
    m1 = ("Grundfall: f(x) = x² + c·x, fester Punkt an der Stelle 2, "
          "zweiter Punkt im Abstand h = 1; 0,5; 0,1; 0,01; die Stelle "
          "bleibt, der Faktor c wandert; Differenzenquotient aufstellen, "
          "umformen, Grenzwert")
    gf = []
    for c in (1, -1, 3, -3, -5):
        term = ("x^2 + x" if c == 1 else "x^2 - x" if c == -1 else
                f"x^2 + {c}x" if c > 0 else f"x^2 - {-c}x")
        fy = 4 + 2 * c
        k = 4 + c
        ms = [k + 1, k + 0.5, k + 0.1, k + 0.01]
        cm = ("" if c == 0 else f" + {c}h" if c > 0 else f" - {-c}h")
        cm = cm.replace(" + 1h", " + h").replace(" - 1h", " - h")

        def dez(x):
            s = f"{x:.2f}".rstrip("0").rstrip(".")
            return s.replace(".", "{,}")
        mtext = "; ".join(f"${dez(m)}$" for m in ms)
        gf.append(um(
            g[0], merkmal=m1,
            aufgabe=(f"Gegeben ist $f(x) = {term}$ mit dem Punkt "
                     f"$P(2 | {fy})$ auf dem Graphen. $Q(2 + h | f(2 + h))$ "
                     "ist ein zweiter Punkt des Graphen. Berechne für jedes "
                     "$h$ der Tabelle die Steigung $m$ der Sekante durch "
                     "$P$ und $Q$ und gib den Wert an, dem sich die "
                     "Steigungen nähern – die Tangentensteigung $f'(2)$."),
            antwort="f'(2) = __",
            loesung=(f"aufstellen: $m = \\frac{{f(2 + h) - f(2)}}{{h}}$; "
                     f"umformen: $m = \\frac{{4h + h^2{cm}}}{{h}} = "
                     f"{k} + h$; einsetzen: $m =$ {mtext}; Grenzwert: für "
                     f"$h \\to 0$ strebt $m$ gegen ${k}$; Ergebnis: "
                     f"$f'(2) = {k}$"),
            pruef=f"[{', '.join(repr(round(m, 2)) for m in ms)}, {k}]",
            grafik="\\wertetabelle{h}{m}{1,0{,}5,0{,}1,0{,}01}"))
    for i, a in enumerate(gf):
        a["_alt"] = g[i]["_alt"]
    aus += varianten(gf)
    # neue Sprosse s2: Tangente mit dem Lineal anlegen (Grafik)
    s2 = []
    m2 = ("Tangente mit dem Lineal an den Graphen von x² + c·x anlegen, "
          "Steigung am Steigungsdreieck messen, dann f'(1) rechnen und "
          "vergleichen")
    for c, term, tx, fy, abl, fs, rech, rng, dreieck in [
            (1, "x^2 + x", "\\x^2+\\x", 2, "2x + 1", 3, "2 + 1",
             "xmin=-3,xmax=2,ymin=-1,ymax=7", "1 nach rechts, 3 nach oben"),
            (-3, "x^2 - 3x", "\\x^2-3*\\x", -2, "2x - 3", -1, "2 - 3",
             "xmin=-1,xmax=4,ymin=-3,ymax=5", "1 nach rechts, 1 nach unten"),
            (3, "x^2 + 3x", "\\x^2+3*\\x", 4, "2x + 3", 5, "2 + 3",
             "xmin=-4,xmax=2,ymin=-3,ymax=11",
             "1 nach rechts, 5 nach oben")]:
        s2.append(neu(
            g[0], sprosse=2, hoehe="sprosse", sprosse_text=T_E3_S2,
            merkmal=m2,
            aufgabe=(f"Die Abbildung zeigt den Graphen von $f(x) = {term}$ "
                     f"und den Punkt $P(1 | {fy})$. Lege in $P$ mit dem "
                     "Lineal die Tangente an und miss ihre Steigung an "
                     "einem Steigungsdreieck. Berechne danach $f'(1)$ und "
                     "vergleiche mit deiner Messung."),
            form="zeichnen", antwort="gemessen: __, gerechnet: f'(1) = __",
            loesung=(f"Tangente anlegen: Steigungsdreieck {dreieck}, "
                     f"gemessen $m \\approx {fs}$; ableiten: $f'(x) = "
                     f"{abl}$; einsetzen: $f'(1) = {rech} = {fs}$; "
                     "vergleichen: Messung und Rechnung stimmen überein"),
            pruef=str(fs), original=None,
            grafik=(f"\\begin{{ksys}}[{rng},ablesen]\\funktion{{{tx}}}{{f}}"
                    f"\\punkt{{1}}{{{fy}}}{{P}}\\end{{ksys}}"),
            loesungsgrafik=(f"\\begin{{ksys}}[{rng},klein]"
                            f"\\funktion{{{tx}}}{{f}}"
                            f"\\tangentean{{{tx}}}{{1}}{{t}}\\end{{ksys}}")))
    aus += varianten(s2)
    # alte s2–s7 rücken auf s3–s8
    for s in range(2, 7):
        for a in nimm(alt, 1, s):
            a["sprosse"] = s + 1
            aus.append(a)
    # Prüfungssprosse: 2025-bebb-lk-A1.6b und 2025MerhoehtAAnalysis23-b
    # sind eine Pooldublette, also ein Original mit zwei Zeilen (v1, v4
    # bleiben; v2, v3 entfallen)
    pr = nimm(alt, 1, 7)
    pr = [pr[0], pr[3]]
    for a in pr:
        a["sprosse"] = 8
    aus += varianten(pr)
    # Typ ohne Kette: quelle ist die Zeile „Typen je Lerneinheit“ (25)
    for a in nimm(alt, 2, 1):
        a["quelle"] = 25
        aus.append(a)
    # fehler: v1 P1, v2 P2, v3 Schülerrechnung
    fe = merkmal_setzen(nimm(alt, 3, 1), M_FEHLER)
    fe[0] = um(
        fe[0],
        aufgabe=("Für $f(x) = \\sqrt{x}$ hat die Tangente im Punkt "
                 "$P(4 | 2)$ die Steigung $0{,}25$. Vier Schüler geben die "
                 "Steigung einer Geraden an, die mit dem Graphen $P$ und "
                 "einen weiteren Punkt gemeinsam hat. Welche Ergebnisse "
                 "können nicht stimmen? Begründe, ohne genau zu rechnen. "
                 "\\\\ (1) $0{,}3$ \\\\ (2) $0{,}25$ \\\\ (3) $-0{,}1$ \\\\ "
                 "(4) $0{,}2$"),
        loesung=("Nicht stimmen können (2) und (3). (2): $0{,}25$ ist die "
                 "Tangentensteigung – die Tangente hat mit dem Graphen nur "
                 "$P$ gemeinsam, sie ist keine Sekante. (3): Der Graph "
                 "steigt überall, jede Sekante durch zwei Graphenpunkte "
                 "steigt auch. (1) und (4) können stimmen: links von $P$ "
                 "liegen die Sekantensteigungen über $0{,}25$, rechts "
                 "darunter."),
        pruef="")
    fe[1] = um(
        fe[1],
        aufgabe=("Zu $g(x) = x^2 - 4x$ rechnet Tom: \\rechnung{"
                 "\\frac{g(5) - g(1)}{5 - 1} &= \\frac{5 - (-3)}{4} = 2 "
                 "\\\\ g'(x_0) = 2x_0 - 4 &= 2 \\\\ x_0 &= 3} Er schreibt: "
                 "„Bei $x_0 = 3$ ist die Tangente parallel zur Sekante "
                 "durch die Graphenpunkte bei $1$ und $5$.“ Prüfe, ob Tom "
                 "richtig gerechnet hat."),
        loesung=("Richtig. Die Gleichung setzt die Tangentensteigung an der "
                 "gesuchten Stelle gleich der Sekantensteigung, und gleiche "
                 "Steigung heißt parallel."),
        pruef="")
    aus += fe
    # begruenden: v1 „Begründe, warum“, v2 P6, v3 P4
    be = merkmal_setzen(nimm(alt, 3, 2), M_BEGR)
    be[1] = um(
        be[1],
        aufgabe=("Ein Wasserstand ändert sich ohne Sprünge und Knicke; "
                 "seine mittlere Änderungsrate über die ersten $4$ Stunden "
                 "beträgt $3$ cm je Stunde. Ole sagt: „Dann gibt es in "
                 "diesen $4$ Stunden einen Zeitpunkt, an dem der "
                 "Wasserstand momentan genau um $3$ cm je Stunde steigt.“ "
                 "Begründe, ohne zu rechnen, ob Ole recht hat."),
        loesung=("Ja; zwischen den beiden Randpunkten gibt es eine Stelle, "
                 "an der die Tangente parallel zur Sekante ist (dort, wo "
                 "der Graph am weitesten von der Sekante entfernt ist) – "
                 "dort ist die momentane Rate gleich der mittleren, "
                 "$3$ cm je Stunde."),
        pruef="")
    be[2] = um(
        be[2],
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. \\\\ (1) Die Tangente in einem Punkt $P$ "
                 "ist immer eine der Sekanten durch $P$. \\\\ (2) Ist der "
                 "Graph rechtsgekrümmt, so ist jede Sekante durch $P$ und "
                 "einen Graphenpunkt links von $P$ steiler als die Tangente "
                 "in $P$. \\\\ (3) Es gibt Graphen, bei denen alle Sekanten "
                 "durch $P$ dieselbe Steigung haben."),
        loesung=("(1) falsch, z. B. berührt die Tangente $y = 2x - 2$ den "
                 "Graphen von $h(x) = 0{,}5x^2$ nur im Punkt $(2 | 2)$; eine "
                 "Sekante braucht zwei gemeinsame Punkte. (2) wahr, denn "
                 "der rechtsgekrümmte Graph liegt unter seiner Tangente, "
                 "die Gerade von einem Punkt links darunter nach $P$ steigt "
                 "steiler. (3) wahr, denn bei einer Geraden ist jede "
                 "Sekante die Gerade selbst."),
        pruef="")
    aus += be
    # anwendung: v1 mit Entscheidung am Grenzwert (P8)
    an = nimm(alt, 3, 3)
    an[0] = um(
        an[0],
        aufgabe=("Der Ladestand eines Akkus wird durch $L(t) = 100 - 80 "
                 "\\cdot \\mathrm{e}^{-0{,}1t}$ beschrieben ($t$ in Minuten "
                 "seit Ladebeginn, $L(t)$ in Prozent). Der Hersteller "
                 "verspricht: Nach $10$ Minuten lädt der Akku noch mit "
                 "mindestens $60\\,\\%$ der mittleren Laderate der ersten "
                 "$10$ Minuten. Stimmt das?"),
        loesung=("Nein; mittlere Laderate: $\\frac{L(10) - L(0)}{10} "
                 "\\approx 5{,}06$ Prozent je min; momentane Laderate: "
                 "$L'(10) = 8 \\cdot \\mathrm{e}^{-1} \\approx 2{,}94$ "
                 "Prozent je min; Vergleich: $\\frac{2{,}94}{5{,}06} "
                 "\\approx 0{,}58$, also nur etwa $58\\,\\%$ der mittleren "
                 "Rate."),
        pruef=("[8*(1-math.exp(-1)), 8*math.exp(-1), "
               "math.exp(-1)/(1-math.exp(-1))]"))
    aus += an
    aus += rest(alt, (3, 4))
    schreibe(3, alt, aus)


# ---------------------------------------------------------------- e4
def e4():
    alt = lade(4)
    aus = rest(alt, (1, 0))
    g = nimm(alt, 1, 1)
    m1 = ("Grundfall: Zuflussrate mit r'(t) = (a − t) · e^(−0,5t); der "
          "e-Faktor bleibt, die Nullstelle a wandert; Nullstelle mit "
          "Vorzeichenwechsel als Zeitpunkt der größten Rate")
    gf = []
    for a_ in (3, 5, 2, 6, 8):
        gf.append(um(
            g[0], merkmal=m1,
            aufgabe=("Die Zuflussrate in ein Becken wird durch $r$ "
                     "beschrieben ($t$ in Stunden, $r(t)$ in Litern je "
                     f"Stunde); es gilt $r'(t) = ({a_} - t) \\cdot "
                     "\\mathrm{e}^{-0{,}5t}$. Gib an, zu welchem Zeitpunkt "
                     "die Zuflussrate am größten ist."),
            antwort="t = __",
            loesung=(f"Bedingung $r'(t) = 0$: $({a_} - t) \\cdot "
                     "\\mathrm{e}^{-0{,}5t} = 0$; Nullprodukt: der e-Faktor "
                     f"ist nie null, also $t = {a_}$; Vorzeichenwechsel: "
                     f"$r'$ wechselt bei ${a_}$ von plus nach minus; "
                     f"Ergebnis: nach ${a_}$ Stunden ist die Zuflussrate "
                     "am größten"),
            pruef=str(a_)))
    for i, a in enumerate(gf):
        a["_alt"] = g[i]["_alt"]
    aus += varianten(gf)
    aus += rest(alt, *[(1, s) for s in range(2, 9)])
    # Prüfungssprosse: v1–v3 ohne original (2019-be-gk-B2.1e fehlt in
    # Abschnitt 2), v4–v7 Pooldublette 2026-bb-gk-B2.2i /
    # 2026MgrundlegendBAnalysisWTR2-2c = ein Original: v4 und v7 bleiben
    pr = text_setzen(nimm(alt, 1, 9), T_E4_PR)
    aus += varianten(pr[:4] + [pr[6]])
    # fehler: v1 Schülerrechnung, v2 P2, v3 P1
    fe = merkmal_setzen(nimm(alt, 2, 1), M_FEHLER)
    fe[1] = um(
        fe[1],
        aufgabe=("Die Zuflussrate in ein Becken wird durch $r(t) = 8t "
                 "\\cdot \\mathrm{e}^{-0{,}5t}$ beschrieben ($t$ in "
                 "Stunden, $r(t)$ in m³ je Stunde). Sara rechnet: "
                 "\\rechnung{r'(t) = 8 \\cdot (1 - 0{,}5t) \\cdot "
                 "\\mathrm{e}^{-0{,}5t} &= 0 \\\\ t &= 2} Sie schreibt: "
                 "„Nach $2$ Stunden ist die Zuflussrate am größten.“ Prüfe, "
                 "ob Sara richtig gerechnet hat."),
        loesung=("Richtig. $r$ ist selbst die Rate; ihr Maximum liegt bei "
                 "$r'(t) = 0$, der e-Faktor ist nie null, und $r'$ wechselt "
                 "bei $2$ das Vorzeichen von plus nach minus."),
        pruef="")
    fe[2] = um(
        fe[2],
        aufgabe=("Die Zuflussrate in ein Becken wird für $0 \\le t \\le 6$ "
                 "durch $r(t) = -t^3 + 6t^2 + 15t$ beschrieben ($t$ in "
                 "Stunden, $r(t)$ in m³ je Stunde). Vier Schüler geben "
                 "Zeitpunkt und Wert der größten Zuflussrate an. Welche "
                 "Ergebnisse können nicht stimmen? Begründe, ohne genau zu "
                 "rechnen. \\\\ (1) $t = -1$ \\\\ (2) $t = 5$, $100$ m³ je "
                 "Stunde \\\\ (3) $t = 8$, $40$ m³ je Stunde \\\\ (4) "
                 "$t = 5$, $100$ m³"),
        loesung=("Nicht stimmen können (1), (3) und (4). (1) und (3): Die "
                 "Stellen liegen außerhalb des Zeitraums von $0$ bis $6$ "
                 "Stunden. (4): Eine Rate hat die Einheit m³ je Stunde, "
                 "m³ ist eine Wassermenge. (2) kann stimmen."),
        pruef="")
    aus += fe
    # begruenden: v1 „Begründe, warum“, v2 P6, v3 P4
    be = merkmal_setzen(nimm(alt, 2, 2), M_BEGR)
    be[1] = um(
        be[1],
        aufgabe=("Die Höhe einer Pflanze wird durch eine Funktion $h$ "
                 "beschrieben. Jonas sagt: „Die Pflanze wächst am "
                 "schnellsten, wenn sie am höchsten ist.“ Begründe, ohne "
                 "zu rechnen, ob Jonas recht hat."),
        loesung=("Nein; $h$ ist der Bestand, die Wachstumsgeschwindigkeit "
                 "ist $h'$. Am schnellsten wächst die Pflanze, wo $h'$ am "
                 "größten ist, an der Wendestelle von $h$; wo $h$ am "
                 "größten ist, gilt $h' = 0$, dort wächst sie gar nicht."),
        pruef="")
    be[2] = um(
        be[2],
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe. \\\\ (1) Die größte Rate auf einem "
                 "Zeitintervall liegt immer an einer Nullstelle der "
                 "Ableitung der Rate. \\\\ (2) Hat die Rate $r$ im Inneren "
                 "des Intervalls ein Maximum, so ist dort immer "
                 "$r'(t) = 0$. \\\\ (3) Es gibt Bestände, deren Rate nie "
                 "negativ ist."),
        loesung=("(1) falsch, z. B. ist für $r(t) = 2t$ auf $[0; 5]$ die "
                 "größte Rate $10$ am Rand, obwohl $r'$ nie null ist. "
                 "(2) wahr, denn an einem inneren Hochpunkt ist die "
                 "Tangente waagerecht. (3) wahr, denn die Gesamtzahl "
                 "verkaufter Geräte nimmt nie ab, ihre Rate ist nie "
                 "negativ."),
        pruef="")
    aus += be
    # anwendung: v3 mit Entscheidung am Grenzwert (P8)
    an = nimm(alt, 2, 3)
    an[2] = um(
        an[2],
        aufgabe=("Der Wasservorrat eines Stausees wird nach der "
                 "Schneeschmelze durch $S(t) = -0{,}05t^3 + 1{,}5t^2 + 100$ "
                 "beschrieben ($t$ in Tagen, $S(t)$ in Tausend m³, "
                 "$0 \\le t \\le 20$). Der Damm verkraftet einen Anstieg "
                 "von höchstens $18$ Tausend m³ je Tag. Hält der Damm in "
                 "diesen $20$ Tagen stand?"),
        loesung=("Ja; ableiten: $S'(t) = -0{,}15t^2 + 3t$, $S''(t) = "
                 "-0{,}3t + 3$; Bedingung $S''(t) = 0$: $t = 10$; Rate "
                 "einsetzen: $S'(10) = 15$; Ränder: $S'(0) = 0$, "
                 "$S'(20) = 0$; Vergleich: die größte Rate $15$ Tausend m³ "
                 "je Tag liegt unter $18$ Tausend m³ je Tag."),
        pruef="[10, 15]")
    aus += an
    # darstellung: v1 rückwärts (Term -> Graph)
    da = nimm(alt, 2, 4)
    rng = "xmin=0,xmax=8,ymin=-2,ymax=10,xstep=1,ystep=2"
    da[0] = um(
        da[0],
        aufgabe=("Die Änderungsrate eines Wasserstands ist $f'(t) = "
                 "-0{,}5t^2 + 4t$ ($t$ in Stunden, $f'(t)$ in cm je Stunde, "
                 "$0 \\le t \\le 8$). Zeichne den Graphen von $f'$ in das "
                 "Koordinatensystem und markiere den Punkt, an dem der "
                 "Wasserstand am schnellsten steigt."),
        form="zeichnen", antwort="",
        loesung=("Wertetabelle: $f'(0) = 0$, $f'(2) = 6$, $f'(4) = 8$, "
                 "$f'(6) = 6$, $f'(8) = 0$; Hochpunkt: $(4 | 8)$; Ergebnis: "
                 "nach $4$ Stunden steigt der Wasserstand mit $8$ cm je "
                 "Stunde am schnellsten"),
        pruef="[4, 8]",
        grafik=(f"\\begin{{ksys}}[{rng},xlabel=t in h,ylabel=f'(t)]"
                "\\end{ksys}"),
        loesungsgrafik=(f"\\begin{{ksys}}[{rng},klein]"
                        "\\funktion{-0.5*\\x^2+4*\\x}{f'}"
                        "\\hochpunkt{4}{8}{H}\\end{ksys}"))
    aus += da
    schreibe(4, alt, aus)


if __name__ == "__main__":
    wahl = sys.argv[1:] or ["e1", "e2", "e3", "e4"]
    for n in wahl:
        globals()[n]()
    print(json.dumps(ZAEHL, ensure_ascii=False))
    if UMBENANNT:
        print("original umgestellt (Dublette):", ", ".join(UMBENANNT))

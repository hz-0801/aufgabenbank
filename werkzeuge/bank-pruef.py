#!/usr/bin/env python3
"""Prüft die Bank eines Katalogeintrags (bank.md, Abschnitt „Prüfung").

v0.8, 2026-09-29 (Befund Prüfstein terme): pruef "" auch bei hoehe
pflicht fehler erlaubt – die Serie P1 („Welche Ergebnisse können
nicht stimmen?“) hat nach bank.md pruef "", ihre Lösung trägt aber
Ziffern; vorher erzwang das Skript eine Scheinprobe.

v0.7, 2026-09-29 (Vorstufen-Nummerierung, bank.md fünfte Fassung).
Änderung gegenüber v0.6 (kleinste Änderung, sonst nichts):
  – sprosse ≤ 0 genau dann, wenn hoehe vorstufe (statt = 0);
    eine Kette darf bei −1, −2 … beginnen, die Folge bleibt lückenlos.

v0.6, 2026-09-28 (Basisvorrat, bank.md „Basisvorrat“).
Änderung gegenüber v0.5 (kleinste Änderung, sonst nichts):
  a) `bank-pruef.py _basis` prüft den Ordner bank/_basis/: je Datei
     <eintrag>.jsonl, Sperre und Kennungsprobe aus mappen/<eintrag>.md;
     hoehe "basis" (nur dort), id "<eintrag>-basis-k<k>-v<v>",
     sprosse 1, original Pflicht, einheit aus der Zeile; Warnung,
     wenn eine Kette nicht zehn Varianten hat. Doppel über den ganzen
     Ordner. Die Prüfung je Zeile ist die von v0.5.

v0.5, 2026-09-27 (nach den Sek-II-Prüfsteinen; bank.md vierte Fassung).
Änderungen gegenüber v0.4:
  a) original: Kennung gilt, wenn sie als „### <id>“ in Abschnitt
     „2 Originale“ der Mappe steht; das Muster KENNUNG entfällt.
  b) Tripel (x|y|z): Ergebnisstelle, ksys3-Bereich und Sperre wie
     beim Paar, mit dritter Zahl.
  c) mathnorm: hochgestellte Ziffern ⁰–⁹ werden ^n (x⁴ = x^4).

Änderungen v0.4 gegenüber v0.3:
  a) Ausgabe still: nur ABWEICHUNG, WARNUNG und Summen; --alle
     druckt wie v0.3 auch die OK-Zeilen.
  b) original: Kennungen von MSA, FHR und Abitur gelten (in v0.5
     ersetzt durch den Abgleich mit der Mappe).
papier je Prüfung (Mappen, Abschnitt „2 Originale“, Zeile „jahr …
papier …“ unter der Kennung):
  MSA     2018-OS-K7a               papier OS, FOR oder GYM
  FHR     2025-C-2b                 papier A, B oder C (Buchstabe
                                    der Kennung)
  Abitur  2025MerhoehtAAGLAA121-a   papier <jahr>-iqb-ea (erhoeht)
          2025MgrundlegendAAGLAA12  oder <jahr>-iqb-ga (grundlegend)
Das Skript prüft die Kennung, nicht den Wert von papier (nur, dass
es gesetzt ist).

Änderungen v0.3 gegenüber v0.2:
  a) hoehe pruefung mit original null erlaubt; original an jeder
     hoehe, wenn vollständig; Menge Prüfungshöhe ohne Original 3.
  b) Zone: s1 hoehe grundfall, ab s2 sprosse; merkmal ab s3 beginnt
     mit „Fallstrick:“ (Zone-Paar ausgenommen); je Zeile Warnung.
  c) Grafik nur bei form zeichnen oder Ablese-/Zeichenauftrag,
     nicht mehr beim bloßen Wort „Graph“.
  d) Ankreuzen: Zahloptionen wie bisher; sonst nennt loesung genau
     eine Option wortgleich; dort ist pruef "" erlaubt.
  e) Sperre: Zahlterme aus Kasten, Variablenterme ab einer Zahl,
     gemischte Zahl, kein Paar aus Nenner und Faktor, einzelner
     Bruch kein Zahlenpaar.
  f) Ergebnisstelle: „-\\,6“ und „x^2 - 12x“ mit Vorzeichen;
     Exponent nach ^ zählt nicht als Lösungsziffer.
  g) Mengen: Grundfall je Kette (unverändert), keine Warnung je
     Einheit.

Aufruf:
    python3 werkzeuge/bank-pruef.py <eintrag> [--katalog DATEI] [--alle]
    python3 werkzeuge/bank-pruef.py _basis [--alle]
    python3 werkzeuge/bank-pruef.py --selbsttest

Liest bank/<eintrag>/zone.jsonl und e<n>.jsonl, dazu
mappen/<eintrag>.md (Sperrprobe) und mappen/_bausteine.md
(Bausteinprobe). Ausgabe je fehlerhafter Aufgabe eine Zeile
ABWEICHUNG (mit --alle je Aufgabe OK/ABWEICHUNG),
Warnungen als WARNUNG-Zeilen, Ketten- und Mengenbefunde als eigene
Zeilen, zuletzt je Datei und gesamt die Zahl der Abweichungen und
Warnungen. Rückgabewert 1 bei Abweichungen; Warnungen allein
ändern ihn nicht.

Abweichungen: Felder, id-Muster, Kettenfolge, pruef gegen die
Ergebnisstelle der Lösung, Ankreuzoptionen, Bausteine, Grafik,
Sperre, Doppel. Warnungen: Mengen aus bank.md, fehlendes Feld
loesungsgrafik, fehlende Mappe.

Mit --katalog wird zusätzlich geprüft, dass sprosse_text wortgleich
in der Katalogzeile quelle steht und kette wortgleich im Katalog.
"""

import json
import math
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

FELDER = ["id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
          "sprosse_text", "merkmal", "hoehe", "variante", "aufgabe",
          "form", "antwort", "loesung", "pruef", "original", "grafik",
          "quelle"]
FELDER_NEU = ["loesungsgrafik"]  # seit bank.md 2. Fassung
HOEHEN = ["vorstufe", "grundfall", "sprosse", "pruefung", "pflicht"]
PFLICHT = ["fehler", "begruenden", "darstellung", "anwendung"]
FORMEN = ["teil", "gleichungsraster", "dreisatz", "streifenfeld",
          "streifenleer", "ankreuzen", "tabelle", "zeichnen", "text"]
# bank.md „Mengen je Kette": Vorstufe und Erkennungsschritt 4,
# Grundfall 5, Sprosse und Typ ohne Kette 3, Prüfungshöhe 2 je
# Original, Pflichtelemente 3, Zone-Paar 2 (je Sprosse 1).
MENGE = {"vorstufe": 4, "grundfall": 5, "sprosse": 3}
MENGE_PFLICHT = 3
MENGE_ORIGINAL = 2
MENGE_OHNE_ORIGINAL = 3      # Prüfungshöhe mit original null
TOLERANZ = Decimal("0.005")

# Zahl mit Dezimalkomma; Tausender sind vorher zusammengezogen.
ZAHL = re.compile(r"(?<![\d,])[-−]?\d+(?:,\d+)?")
# Punkt (x|y) oder Tripel (x|y|z); Gruppe 3 leer beim Paar.
PUNKT = re.compile(r"\(\s*([-−]?\d+(?:,\d+)?)\s*\|\s*([-−]?\d+(?:,\d+)?)"
                   r"(?:\s*\|\s*([-−]?\d+(?:,\d+)?))?\s*\)")

# LaTeX- und amsmath-Befehle, die keine Bausteine der Vorlage sind.
STANDARD = set("""
frac dfrac tfrac cdot times div pm mp approx ne neq le leq ge geq lt gt
sqrt text textbf textit emph mathrm mathbf underline overline hat vec
bar ldots dots cdots vdots quad qquad hspace vspace phantom hphantom
vphantom left right big Big bigl bigr Bigl Bigr mid Rightarrow
Leftrightarrow Leftarrow rightarrow leftarrow to mapsto infty circ
degree cdotp colon sim equiv parallel perp angle triangle square
alpha beta gamma delta epsilon varepsilon pi rho sigma tau phi varphi
omega lambda mu Delta Omega Sigma displaystyle textstyle newline
linebreak par noindent small footnotesize large Large mathbb in notin
cup cap setminus emptyset subset subseteq wedge vee neg forall exists
overrightarrow widehat lvert rvert lceil rceil lfloor rfloor
begin end
""".split())
UMGEBUNG_STANDARD = {"array", "aligned", "cases", "tabular", "matrix",
                     "pmatrix", "center", "itemize", "enumerate"}


# --- Zahlen --------------------------------------------------------------

def normiert(text):
    """Lösungstext für den Zahlenfang: Tausender zusammen, Exponenten
    und Indizes weg, Klammern {} weg."""
    t = text.replace("{,}", ",")
    t = re.sub(r"(\d)\\,(?=\d{3}(?!\d))", r"\1", t)   # 1\,200
    t = re.sub(r"(\d)[  ](?=\d{3}(?!\d))", r"\1", t)  # 1 200 (schmal)
    t = gemischt(t)
    for leer in ("\\,", "\\;", "\\:", "\\ "):
        t = t.replace(leer, " ")
    t = t.replace("\\!", "").replace("\\%", "%")
    t = t.replace("\\approx", "≈").replace("−", "-")
    t = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)
    t = re.sub(r"\^\{[^}]*\}|\^-?\d", " ", t)          # x^2, 2^{10}
    t = re.sub(r"_\{[^}]*\}|_\d+", "", t)              # x_1, S_{12}
    t = re.sub(r"\\[A-Za-z]+", " ", t)                 # \frac, \cdot
    t = t.replace("{", "").replace("}", "")
    # Buchstaben mit angehängter Ziffer (x1, a2) sind keine Zahlen.
    t = re.sub(r"[A-Za-z]\d+", " ", t)
    return vorzeichen(t)


def gemischt(t):
    """Gemischte Zahl 3\\frac{3}{5} -> \\frac{18}{5} (nicht 33/5)."""
    def ein(m):
        g, z, n = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return f"\\frac{{{g * n + z}}}{{{n}}}"
    return re.sub(r"(?<![\d,.^_A-Za-z{])(\d+)\\[dt]?frac\{(\d+)\}\{(\d+)\}",
                  ein, t)


def vorzeichen(t):
    """Minus mit Abstand vor einer Zahl gehört zur Zahl („$- 6$“,
    „x - 12x“), außer nach einer Zahl, „)“ oder Einheitszeichen –
    dort ist es Rechenzeichen („20 - 5“, „100 % - 90 %“)."""
    return re.sub(r"(^|[^\d)%€°\s])(\s*)-\s+(?=\d)", r"\1\2-", t)


def zahl(s):
    s = s.replace("−", "-")
    stellen = len(s.split(",")[1]) if "," in s else 0
    return Decimal(s.replace(",", ".")), stellen


def zahlen_aus(text):
    """Zahlen aus einem Text: [(Decimal, Nachkommastellen)]."""
    return [zahl(m.group()) for m in ZAHL.finditer(normiert(text))]


# zwischen zwei Ergebnissen einer Aufzählung: Einheit, dann , ; und oder
FOLGE = re.compile(r"[\s$]*(?:[%€]|[A-Za-z]{1,3})?[\s$]*(?:[,;]|und|oder)"
                   r"[\s$]*")


def ergebnis_zahlen(text):
    """Zahlen an der Ergebnisstelle: die erste Zahl, jede Zahl direkt
    nach = oder ≈, alle Zahlen eines Punkts (x|y), Tripels (x|y|z)
    oder Bruchs a/b an der Ergebnisstelle, und die Glieder einer
    Aufzählung von Ergebnissen (4; 1; 0)."""
    t = normiert(text)
    aus = []
    treffer = list(ZAHL.finditer(t))
    vorige = None                 # Ende der letzten Ergebniszahl
    for i, m in enumerate(treffer):
        davor = t[:m.start()].rstrip(" $\t")
        luecke = t[vorige:m.start()] if vorige is not None else None
        if (i == 0 or davor.endswith(("=", "≈"))
                or (luecke is not None and (luecke == "/"
                                            or FOLGE.fullmatch(luecke)))):
            aus.append(zahl(m.group()))
            vorige = m.end()
        else:
            vorige = None
    for m in PUNKT.finditer(t):
        aus += [zahl(g) for g in m.groups() if g is not None]
    return aus


def gerundet(wert, stellen):
    q = Decimal(1).scaleb(-stellen)
    return Decimal(repr(float(wert))).quantize(q, rounding=ROUND_HALF_UP)


def passt(w, zahlen):
    return any(abs(gerundet(w, st) - z) <= TOLERANZ for z, st in zahlen)


def werte_aus(pruef):
    """pruef in leerem Namensraum plus math auswerten -> Liste."""
    w = eval(pruef, {"__builtins__": {}}, {"math": math})
    if isinstance(w, (list, tuple)):
        return list(w)
    return [w]


def vergleiche(pruef, loesung):
    """Jede pruef-Zahl an der Ergebnisstelle der Lösung. [] = passt."""
    try:
        werte = werte_aus(pruef)
    except Exception as e:  # noqa: BLE001
        return [f"pruef nicht auswertbar ({e})"]
    alle = zahlen_aus(loesung)
    if not alle:
        return ["loesung ohne Zahl"]
    stelle = ergebnis_zahlen(loesung)
    befunde = []
    for w in flach(werte):
        if not isinstance(w, (int, float)) or isinstance(w, bool):
            befunde.append(f"pruef-Wert keine Zahl: {w!r}")
        elif not passt(w, stelle):
            wo = "nur im Text" if passt(w, alle) else "nicht in loesung"
            gez = ", ".join(f"{z}" for z, _ in stelle)
            befunde.append(f"{w:g} nicht an der Ergebnisstelle ({wo}; "
                           f"Ergebnisstelle: {gez})")
    return befunde


def flach(werte):
    aus = []
    for w in werte:
        aus += list(w) if isinstance(w, (list, tuple)) else [w]
    return aus


# --- LaTeX-Aufrufe -------------------------------------------------------

def klammer(s, i):
    """Ende (Index nach der schließenden Klammer) der Gruppe ab s[i]."""
    auf = s[i]
    zu = "]" if auf == "[" else "}"
    tiefe = 0
    k = i
    while k < len(s):
        if s[k] == "\\":
            k += 2
            continue
        if s[k] == auf:
            tiefe += 1
        elif s[k] == zu:
            tiefe -= 1
            if tiefe == 0:
                return k + 1
        k += 1
    return len(s)


def argumente(s, i):
    """Pflicht- und optionale Argumente direkt ab s[i]: (opt, [pflicht])."""
    opt, pflicht = 0, []
    while i < len(s) and s[i] in "[{":
        e = klammer(s, i)
        if s[i] == "[":
            opt += 1
        else:
            pflicht.append(s[i + 1:e - 1])
        i = e
    return opt, pflicht


def aufrufe(s):
    """[(name, [Pflichtargumente])]; Umgebungen als 'begin:name'."""
    aus = []
    for m in re.finditer(r"\\(?:([A-Za-z]+)\*?|.)", s):
        name = m.group(1)
        if not name:
            continue
        _, pflicht = argumente(s, m.end())
        if name == "begin" and pflicht:
            aus.append(("begin:" + pflicht[0], pflicht[1:]))
        elif name != "end":
            aus.append((name, pflicht))
    return aus


def lade_bausteine(datei):
    """{name: {Argumentzahlen}} aus mappen/_bausteine.md."""
    text = datei.read_text(encoding="utf-8")
    teil = text.split("## Absätze")
    kurz, absatz = teil[0], teil[1] if len(teil) > 1 else ""
    sig = {}
    for name, pflicht in aufrufe(kurz):
        sig.setdefault(name, set()).add(len(pflicht))
    for name, pflicht in aufrufe(absatz):
        if name not in sig:
            sig.setdefault("~" + name, set()).add(len(pflicht))
    for name in [n for n in sig if n.startswith("~")]:
        sig[name[1:]] = sig.pop(name)
    for name, zahlen in sig.items():
        if len(zahlen) > 1:          # „\kreuz in eigener Zeile": Erwähnung
            zahlen.discard(0)
    return sig


def bausteinprobe(a, sig):
    b = []
    for feld in ("aufgabe", "loesung", "grafik", "loesungsgrafik"):
        for name, pflicht in aufrufe(a.get(feld, "")):
            if name.startswith("begin:"):
                if name[6:] in UMGEBUNG_STANDARD:
                    continue
            elif name in STANDARD:
                continue
            anzeige = ("\\begin{" + name[6:] + "}"
                       if name.startswith("begin:") else "\\" + name)
            if name not in sig:
                b.append(f"Baustein {anzeige} nicht in _bausteine.md "
                         f"({feld})")
            elif len(pflicht) not in sig[name]:
                soll = "/".join(str(n) for n in sorted(sig[name]))
                b.append(f"Baustein {anzeige} mit {len(pflicht)} "
                         f"Argumenten, Anleitung {soll} ({feld})")
    return b


# --- Grafik --------------------------------------------------------------

def ksys_bereiche(grafik):
    """[(xmin, xmax, ymin, ymax)] je ksys der Grafik."""
    aus = []
    for m in re.finditer(r"\\begin\{ksys\}", grafik):
        opt = ""
        if grafik[m.end():m.end() + 1] == "[":
            e = klammer(grafik, m.end())
            opt = grafik[m.end() + 1:e - 1]
        w = {"xmin": -4, "xmax": 4, "ymin": -4, "ymax": 4}
        for teil in opt.split(","):
            teil = teil.strip()
            if teil == "leit":
                w.update(xmin=-3, xmax=3, ymin=-3, ymax=3)
            k, _, v = teil.partition("=")
            if k.strip() in w:
                try:
                    w[k.strip()] = float(v)
                except ValueError:
                    pass
        aus.append((w["xmin"], w["xmax"], w["ymin"], w["ymax"]))
    return aus


def ksys3_bereiche(grafik):
    """[((x1min, x1max), (x2min, x2max), (x3min, x3max))] je ksys3;
    Voreinstellung nach _bausteine.md."""
    aus = []
    for m in re.finditer(r"\\begin\{ksys3\}", grafik):
        opt = ""
        if grafik[m.end():m.end() + 1] == "[":
            e = klammer(grafik, m.end())
            opt = grafik[m.end() + 1:e - 1]
        w = {"x1min": -2, "x1max": 6, "x2min": -3, "x2max": 6,
             "x3min": -2, "x3max": 5}
        for teil in opt.split(","):
            k, _, v = teil.strip().partition("=")
            if k.strip() in w:
                try:
                    w[k.strip()] = float(v)
                except ValueError:
                    pass
        aus.append(tuple((w[f"x{i}min"], w[f"x{i}max"]) for i in (1, 2, 3)))
    return aus


# Ablese- oder Zeichenauftrag: verlangt eine Grafik (das Wort
# „Graph“ allein nicht, etwa „Liegt P auf dem Graphen von f?“).
# Imperativ „lies“, „zeichne“; „liest“, „ohne zu zeichnen“ und ein
# Bild als Gegenstand („ein quadratisches Bild“) sind kein Auftrag.
AUFTRAG_GRAFIK = re.compile(
    r"\b(?:[Ll]ies|[Zz]eichne)\b"
    r"|\b(?:[Aa]blesen|abzulesen|abgelesen|eingezeichnet)\b"
    r"|\bAbbildung|\b(?:im|am|siehe)\s+Bild\b"
    r"|\bBild\s+(?:zeigt|unten|oben|rechts|links)\b"
    r"|\bim\s+Koordinatensystem\b")


def grafikprobe(a):
    b = []
    grafik = a.get("grafik", "")
    if (a["form"] == "zeichnen"
            or AUFTRAG_GRAFIK.search(a["aufgabe"])) and not grafik:
        b.append("grafik leer (form zeichnen oder Ablese-/Zeichenauftrag "
                 "in aufgabe)")
    bereiche = ksys_bereiche(grafik)
    raeume = ksys3_bereiche(grafik)
    if not bereiche and not raeume:
        return b
    # Paare gehören ins ksys, Tripel ins ksys3.
    punkte, tripel = [], []
    for m in PUNKT.finditer(normiert(a["loesung"])):
        k = [float(zahl(g)[0]) for g in m.groups() if g is not None]
        (tripel if len(k) == 3 else punkte).append(("loesung", *k))
    if a["pruef"]:
        try:
            for w in werte_aus(a["pruef"]):
                if isinstance(w, (list, tuple)) and len(w) == 2:
                    punkte.append(("pruef", float(w[0]), float(w[1])))
                elif isinstance(w, (list, tuple)) and len(w) == 3:
                    tripel.append(("pruef", *map(float, w)))
        except Exception:  # noqa: BLE001 – meldet vergleiche()
            pass
    if not bereiche:
        punkte = []
    for name, pflicht in aufrufe(grafik):
        try:
            if name == "parabel" and len(pflicht) == 4:
                punkte.append(("Scheitel", float(pflicht[1]),
                               float(pflicht[2])))
            elif name == "punkt" and len(pflicht) == 3:
                punkte.append(("\\punkt", float(pflicht[0]),
                               float(pflicht[1])))
        except ValueError:
            pass
    for wo, x, y in punkte:
        if not any(x0 <= x <= x1 and y0 <= y <= y1
                   for x0, x1, y0, y1 in bereiche):
            b.append(f"Punkt ({x:g}|{y:g}) aus {wo} außerhalb des ksys")
    for wo, *k in tripel if raeume else []:
        if not any(all(lo <= v <= hi for v, (lo, hi) in zip(k, r))
                   for r in raeume):
            b.append(f"Punkt ({k[0]:g}|{k[1]:g}|{k[2]:g}) aus {wo} "
                     f"außerhalb des ksys3")
    return b


# --- Ankreuzen -----------------------------------------------------------

def optionen(aufgabe):
    """Inhalte der \\kreuz{…} einer Aufgabe."""
    aus = []
    for m in re.finditer(r"\\kreuz(?=\{)", aufgabe):
        e = klammer(aufgabe, m.end())
        aus.append(aufgabe[m.end() + 1:e - 1])
    return aus


def reine_zahl(o):
    """Option ist eine Zahl, höchstens mit Einheit dahinter
    („$4$ cm“, „$12\\,\\%$“), nicht „4x“ oder „nur $5$“."""
    t = normiert(o).replace("$", " ").strip()
    return re.fullmatch(r"-?\d+(?:,\d+)?(?:\s+(?:%|€|[A-Za-zÄÖÜäöüß]+"
                        r"[²³]?(?:/[A-Za-z]+)?))?", t) is not None


def zahl_ankreuzen(a):
    """Mindestens zwei Optionen sind reine Zahlen."""
    return (a["form"] == "ankreuzen"
            and sum(map(reine_zahl, optionen(a["aufgabe"]))) >= 2)


def raumarm(text):
    """mathnorm, ohne Raum um Rechenzeichen, Wörter durch ein
    Leerzeichen getrennt (ohne_raum klebte „Berechne6²+8²“)."""
    t = mathnorm(text)
    t = re.sub(r"\s*([-+·:/=≈|²³^<>])\s*", r"\1", t)
    t = re.sub(r"\(\s+", "(", re.sub(r"\s+\)", ")", t))
    return re.sub(r"\s+", " ", t).strip()


def wortform(text):
    """Für den wortgleichen Vergleich: raumarm, ohne Satzzeichen am
    Ende."""
    return raumarm(text).rstrip(".,;!?").strip()


# Grenzen einer Option in der Lösung: kein Wort, keine Ziffer,
# kein Rechenzeichen daneben; ein Komma nur als Satzzeichen.
ANFANG_OPTION = r"(?<![\w²³\-+·/^])(?<!\d,)"
ENDE_OPTION = r"(?![\w²³^+\-·/])(?!,\d)"


def ankreuzprobe(a):
    """Zahloptionen (eine Zahl, ggf. Einheit): die Lösungszahl steht
    in genau einer. Sonst (Terme, Gleichungen, Wörter): loesung nennt
    genau eine Option wortgleich. Wiederholen sich Optionen (wahr/
    falsch je Aussage), ist die Aufgabe mehrteilig – keine Probe."""
    if a["form"] != "ankreuzen":
        return []
    opts = optionen(a["aufgabe"])
    if zahl_ankreuzen(a):
        if not a["pruef"]:
            return []
        zahlopt = [zahlen_aus(o) for o in opts if reine_zahl(o)]
        try:
            w = flach(werte_aus(a["pruef"]))[0]
        except Exception:  # noqa: BLE001 – meldet vergleiche()
            return []
        n = sum(1 for z in zahlopt if passt(w, z))
        if n != 1:
            return [f"Lösungszahl {w:g} in {n} von {len(zahlopt)} "
                    f"Ankreuzoptionen (soll 1)"]
        return []
    formen = [wortform(o) for o in opts]
    if len(opts) < 2 or len(set(formen)) < len(formen):
        return []
    loes = wortform(a["loesung"])
    # Beginnt die Lösung mit einer Option, ist sie die genannte; was
    # danach kommt, ist Begründung („zwei Lösungen – … eine …“).
    for f in sorted(formen, key=len, reverse=True):
        if f and re.match(re.escape(f) + ENDE_OPTION, loes):
            return []
    n = 0
    for f in sorted(formen, key=len, reverse=True):
        m = re.search(ANFANG_OPTION + re.escape(f) + ENDE_OPTION, loes)
        if f and m:
            n += 1
            loes = loes[:m.start()] + " ¦ " + loes[m.end():]
    if n != 1:
        return ["Ankreuzlösung nennt keine oder mehrere Optionen "
                f"({n} von {len(opts)})"]
    return []


# --- Sperre --------------------------------------------------------------

HOCH = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def hochzahlen(t):
    """Hochgestellte Ziffern zu ^{n} (x⁴ -> x^{4}); ² und ³ allein
    bleiben, sie sind die Zielform von ^2 und ^3."""
    return re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+",
                  lambda m: m.group() if m.group() in "²³"
                  else "^{" + m.group().translate(HOCH) + "}", t)


def mathnorm(text):
    """Text und LaTeX auf eine Schreibweise: 3/4, ·, ², ^n, -, ohne $."""
    t = gemischt(hochzahlen(text).replace("{,}", ",")).replace("\\%", "%")
    t = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", t)
    t = re.sub(r"\((\w+(?:,\d+)?)\)/\((\w+(?:,\d+)?)\)", r"\1/\2", t)
    t = re.sub(r"\^\{?2\}?", "²", t)
    t = re.sub(r"\^\{?3\}?", "³", t)
    for alt, neu in (("\\cdot", "·"), ("\\times", "·"), ("⋅", "·"),
                     ("\\approx", "≈"), ("−", "-"), ("\\left", ""),
                     ("\\right", ""), ("\\,", " "), ("\\;", " "),
                     ("\\mid", "|"), ("$", " "), ("{", ""), ("}", "")):
        t = t.replace(alt, neu)
    t = re.sub(r"(\d) (?=\d{3}(?!\d))", r"\1", t)     # 1 200
    return t


def ohne_raum(t):
    return re.sub(r"\s+", "", t)


# ein Token: Zahl, Wort, Zeichen
TOKEN = re.compile(r"\d+(?:,\d+)?|[A-Za-zÄÖÜäöüß]+|\S")
OPERATOR = set("+-·:/=≈()|²³√%^")


def gleichungen(text):
    """Gleichungen und Terme mit Variable aus einem Quelltext."""
    t = mathnorm(text)
    t = re.sub(r"(?<=\S):(?=\s)", " ¦ ", t)          # „Regel: …"
    t = re.sub(r"\s{2,}", " ¦ ", t)                   # Spalten im Kasten
    laeufe, lauf = [], []
    for m in TOKEN.finditer(t):
        tok = m.group()
        mathe = (tok[0].isdigit() or tok in OPERATOR
                 or (tok.isalpha() and len(tok) == 1))
        if mathe:
            lauf.append(tok)
        else:
            laeufe.append(lauf)
            lauf = []
    laeufe.append(lauf)
    aus = set()
    for lauf in laeufe:
        s = "".join(lauf)
        seiten = re.split(r"[=≈]", s)
        seiten = [ausgeglichen(s) for s in seiten]
        for i, seite in enumerate(seiten):
            zahlen = re.findall(r"\d+(?:,\d+)?", seite)
            rechnen = re.search(r"[\w)²³][-+·:/][\w(]", seite)
            if re.search(r"[a-z]", seite):
                if zahlen and rechnen:
                    aus.add(seite)   # Variablenterm ab einer Zahlbelegung
            elif (len(zahlen) >= 2 and rechnen
                  and not re.fullmatch(r"-?\d+(?:,\d+)?/\d+(?:,\d+)?",
                                       seite)):
                aus.add(seite)       # Zahlterm (6² + 8²), kein Einzelbruch
            if i + 1 < len(seiten):
                g = seite + "=" + seiten[i + 1]
                n = len(re.findall(r"\d+(?:,\d+)?", g))
                if (seite and seiten[i + 1]
                        and (n >= 2 or (n and re.search(r"[a-z]", g)))):
                    aus.add(g)       # Gleichung; mit Variable ab einer Zahl
    return {g for g in aus if len(g) >= 5}


def ausgeglichen(s):
    """Überzählige Klammern am Rand weg: „10(" -> „10", „x)" -> „x"."""
    while s:
        if s[-1] in "(|" or (s[-1] == ")" and s.count(")") > s.count("(")):
            s = s[:-1]
        elif s[0] in ")|" or (s[0] == "(" and s.count("(") > s.count(")")):
            s = s[1:]
        elif s[0] == "(" and s[-1] == ")" and klammer(s, 0) == len(s):
            s = s[1:-1]                        # ganz eingeklammert
        else:
            return s
    return s


def zahlenpaare(text):
    """Paare: Punkt (a|b), Tripel (a|b|c), Anteil (a von b, a : b),
    Produkt. Ein einzelner Bruch a/b ist kein Paar; Zähler oder Nenner
    eines Bruchs bilden mit einem Faktor daneben kein Paar (1/12 · 3);
    der Ursprung (0|0) bzw. (0|0|0) ist keine Zahlbelegung."""
    t = mathnorm(text)
    n = r"(-?\d+(?:,\d+)?)"
    aus = set()
    for a, b in re.findall(r"\(\s*" + n + r"\s*\|\s*" + n + r"\s*\)", t):
        if zahl(a)[0] or zahl(b)[0]:
            aus.add(("Punkt", zahl(a)[0], zahl(b)[0]))
    for a, b, c in re.findall(r"\(\s*" + n + r"\s*\|\s*" + n + r"\s*\|\s*"
                              + n + r"\s*\)", t):
        k = tuple(zahl(x)[0] for x in (a, b, c))
        if any(k):
            aus.add(("Tripel",) + k)
    for muster, art in ((n + r"\s*%?\s*von\s*" + n, "Anteil"),
                        (n + r"\s*:\s*" + n, "Anteil"),
                        (n + r"\s*·\s*" + n, "Produkt")):
        for a, b in re.findall(r"(?<![\d,|/])" + muster
                               + r"(?![\d,])(?!\s*/)", t):
            x, y = zahl(a)[0], zahl(b)[0]
            if abs(x) <= 9 and abs(y) <= 9 and x == int(x) and y == int(y):
                continue                          # kleine Zahlen frei
            if art == "Produkt":
                x, y = sorted((x, y))
            aus.add((art, x, y))
    return aus


def lade_sperre(mappe):
    """{('gleichung'|'paar', muster): herkunft} aus der Mappe."""
    return sperre_aus(mappe.read_text(encoding="utf-8"))


def originale_aus(text):
    """Kennungen der Überschriften „### <id> …“ in „## 2 Originale“."""
    if "## 2 Originale" not in text:
        return set()
    orig = text.split("## 2 Originale")[1].split("\n## ")[0]
    return {z[4:].split(" ")[0] for z in orig.split("\n")
            if z.startswith("### ")}


def sperre_aus(text):
    sperre = {}
    teil1 = text.split("## 2 Originale")[0]
    abschnitt = None
    for z in teil1.split("\n"):
        m = re.match(r"\s*(\d+)  (.*)$", z)
        if not m:
            continue
        inhalt = m.group(2)
        if inhalt.startswith("#"):
            k = inhalt.lstrip("#").strip()
            abschnitt = ("Merkkasten" if k.startswith("Merkkasten")
                         else "Typische Fehler"
                         if k.startswith("Typische Fehler") else None)
            continue
        if abschnitt:
            herkunft = f"{abschnitt}, Zeile {m.group(1)}"
            for g in gleichungen(inhalt):
                sperre.setdefault(("gleichung", g), herkunft)
            for p in zahlenpaare(inhalt):
                sperre.setdefault(("paar", p), herkunft)
    orig = text.split("## 2 Originale")[1].split("## 3 ")[0] \
        if "## 2 Originale" in text else ""
    kid = None
    for z in orig.split("\n"):
        if z.startswith("### "):
            kid = z[4:].split(" ")[0]
        m = re.match(r"- (gegeben|gesucht|verfahren|fehlerquelle): (.*)",
                     z)
        if m and kid:
            herkunft = f"Original {kid}"
            for g in gleichungen(m.group(2)):
                sperre.setdefault(("gleichung", g), herkunft)
            for p in zahlenpaare(m.group(2)):
                sperre.setdefault(("paar", p), herkunft)
    return sperre


def paar_text(p):
    art, *k = p
    if art in ("Punkt", "Tripel"):
        return "(" + "|".join(str(v) for v in k) + ")"
    x, y = k
    return f"{x} {'von' if art == 'Anteil' else '·'} {y}"


def sperrprobe(a, sperre):
    b = []
    aufgabe = raumarm(a["aufgabe"])
    frei = ohne_raum(mathnorm(a["sprosse_text"]))
    paare = zahlenpaare(a["aufgabe"])
    for (art, muster), herkunft in sperre.items():
        if art == "gleichung":
            if muster in frei:
                continue                    # Gegenstand der Kette
            if re.search(r"(?<![\w²³,+\-·/^(|])" + re.escape(muster)
                         + r"(?![\w²³,+\-·/^(])", aufgabe):
                b.append(f"Sperre: {muster} ({herkunft})")
        elif muster in paare:
            wort = "Tripel" if muster[0] == "Tripel" else "Zahlenpaar"
            b.append(f"Sperre: {wort} {paar_text(muster)} "
                     f"({herkunft})")
    return b


# --- Zeile ---------------------------------------------------------------

def pruef_leer_erlaubt(a):
    """pruef "" bei Begründen, Zeichnen, Ankreuzen ohne Zahloptionen
    und einer Lösung ohne Ziffer (Exponent und Index zählen nicht)."""
    return (a.get("pflicht") in ("begruenden", "fehler")
            or a["form"] == "zeichnen"
            or (a["form"] == "ankreuzen" and not zahl_ankreuzen(a))
            or not re.search(r"\d", normiert(a["loesung"])))


def pruefe_zeile(a, eintrag, einheit, ctx=None, basis=False):
    """Feld- und Rechenprüfung einer Zeile -> (Abweichungen, Warnungen).
    basis: Zeile aus bank/_basis/ (v0.6)."""
    ctx = ctx or {}
    b, w = [], []
    fehlt = [f for f in FELDER if f not in a]
    if fehlt:
        return ["Feld fehlt: " + ", ".join(fehlt)], w
    extra = set(a) - set(FELDER) - set(FELDER_NEU) - {"pflicht"}
    if extra:
        b.append("unbekanntes Feld: " + ", ".join(sorted(extra)))
    if a["eintrag"] != eintrag:
        b.append(f"eintrag {a['eintrag']!r} statt {eintrag!r}")
    if a["einheit"] != einheit:
        b.append(f"einheit {a['einheit']} statt {einheit}")
    for f in ("kette_nr", "sprosse", "variante", "quelle"):
        if not isinstance(a[f], int) or isinstance(a[f], bool):
            b.append(f"{f} keine ganze Zahl")
    if b:
        return b, w
    if basis:
        soll = f"{eintrag}-basis-k{a['kette_nr']}-v{a['variante']}"
    elif einheit == 0:
        soll = f"{eintrag}-zone-f{a['kette_nr']}-v{a['variante']}"
    else:
        soll = (f"{eintrag}-e{einheit}-k{a['kette_nr']}-s{a['sprosse']}"
                f"-v{a['variante']}")
    if a["id"] != soll:
        b.append(f"id {a['id']!r} statt {soll!r}")
    if basis:
        if a["hoehe"] != "basis":
            b.append(f"hoehe {a['hoehe']!r} statt 'basis'")
        if a["sprosse"] != 1:
            b.append("sprosse im Basisvorrat 1")
        if a["original"] is None:
            b.append("original fehlt (Pflicht im Basisvorrat)")
    elif a["hoehe"] not in HOEHEN:
        b.append(f"hoehe {a['hoehe']!r} unbekannt")
    if a["hoehe"] == "pflicht":
        if a.get("pflicht") not in PFLICHT:
            b.append(f"pflicht {a.get('pflicht')!r} unbekannt")
    elif "pflicht" in a:
        b.append("pflicht nur bei hoehe pflicht")
    if a["form"] not in FORMEN:
        b.append(f"form {a['form']!r} unbekannt")
    if not basis and (a["sprosse"] <= 0) != (a["hoehe"] == "vorstufe"):
        b.append("sprosse 0 oder kleiner genau dann, wenn hoehe vorstufe")
    o = a["original"]
    # original null auch bei pruefung (Zielmarke ohne P10-Original);
    # ein original an jeder hoehe, wenn vollständig: id, jahr, papier
    # gesetzt, id beginnt mit jahr und steht als „### <id>“ in
    # Abschnitt 2 der Mappe (ohne Mappe entfällt dieser Teil).
    if o is not None:
        if not (isinstance(o, dict) and set(o) == {"id", "jahr", "papier"}
                and isinstance(o["id"], str) and o["id"]
                and isinstance(o["jahr"], int)
                and not isinstance(o["jahr"], bool)
                and isinstance(o["papier"], str) and o["papier"]
                and o["id"].startswith(str(o["jahr"]))):
            b.append("original unvollständig")
        elif (ctx.get("originale") is not None
              and o["id"] not in ctx["originale"]):
            b.append(f"original {o['id']} nicht in der Mappe "
                     f"(Abschnitt 2 Originale)")
    for f in ("kette", "sprosse_text", "merkmal", "aufgabe", "loesung"):
        if not isinstance(a[f], str) or not a[f].strip():
            b.append(f"{f} leer")
    grafiken = a["grafik"] + a.get("loesungsgrafik", "")
    if re.search(r"(?<!\\)%", a["aufgabe"] + grafiken + a["loesung"]):
        b.append("nacktes % (LaTeX: \\%)")
    if "\\teil" in a["aufgabe"] or "\\begin{" in a["aufgabe"]:
        b.append("aufgabe mit \\teil oder Umgebung")
    if a["pruef"] == "":
        if not pruef_leer_erlaubt(a):
            b.append("pruef fehlt")
    else:
        b.extend(vergleiche(a["pruef"], a["loesung"]))
    b.extend(ankreuzprobe(a))
    b.extend(grafikprobe(a))
    if ctx.get("bausteine") is not None:
        b.extend(bausteinprobe(a, ctx["bausteine"]))
    if ctx.get("sperre") is not None:
        b.extend(sperrprobe(a, ctx["sperre"]))
    return b, w


# --- Ketten --------------------------------------------------------------

def pruefe_ketten(zeilen, datei, einheit):
    """Kettenfolge und Mengen einer Datei -> (Abweichungen, Warnungen)."""
    b, w = [], []
    ketten = []  # Reihenfolge des ersten Auftretens
    for a in zeilen:
        k = a["kette_nr"]
        if not ketten or ketten[-1][0] != k:
            if any(k == kk for kk, _ in ketten):
                b.append(f"{datei} k{k}: Kette nicht zusammenhängend")
            ketten.append((k, []))
        ketten[-1][1].append(a)
    nummern = [k for k, _ in ketten]
    if nummern != list(range(1, len(nummern) + 1)):
        b.append(f"{datei}: kette_nr nicht lückenlos ab 1: {nummern}")
    orig_gesamt = {}
    pflicht_zahl = {}
    for k, reihe in ketten:
        if len({a["kette"] for a in reihe}) > 1:
            b.append(f"{datei} k{k}: kette-Name wechselt")
        rang = -1
        sprossen = []
        for a in reihe:
            r = HOEHEN.index(a["hoehe"]) if a["hoehe"] in HOEHEN else -1
            zone_paar = einheit == 0 and rang == HOEHEN.index("pflicht")
            if r < rang and not zone_paar:
                b.append(f"{datei} {a['id']}: hoehe {a['hoehe']} "
                         f"nach höherer Stufe")
            rang = r if zone_paar else max(rang, r)
            if not sprossen or sprossen[-1][0] != a["sprosse"]:
                sprossen.append((a["sprosse"], []))
            sprossen[-1][1].append(a)
        snr = [s for s, _ in sprossen]
        start = snr[0] if snr else 0
        if start > 1 or snr != list(range(start,
                                                    start + len(snr))):
            b.append(f"{datei} k{k}: Sprossen nicht lückenlos: {snr}")
        grund = [s for s, g in sprossen if g[0]["hoehe"] == "grundfall"]
        if len(grund) > 1:
            b.append(f"{datei} k{k}: mehr als ein Grundfall")
        for s, gruppe in sprossen:
            v = [a["variante"] for a in gruppe]
            if v != list(range(1, len(v) + 1)) and einheit != 0:
                b.append(f"{datei} k{k} s{s}: Varianten nicht 1..n: {v}")
            for f in ("sprosse_text", "merkmal", "hoehe", "quelle"):
                if len({a[f] for a in gruppe}) > 1:
                    b.append(f"{datei} k{k} s{s}: {f} uneinheitlich")
            h = gruppe[0]["hoehe"]
            if einheit == 0:
                continue
            if h in MENGE and len(gruppe) != MENGE[h]:
                w.append(f"{datei} k{k} s{s}: {len(gruppe)} Zeilen, "
                         f"Menge {h} = {MENGE[h]}")
            if h == "pruefung":
                zahl_o = {}
                for a in gruppe:
                    oid = (a["original"] or {}).get("id")
                    zahl_o[oid] = zahl_o.get(oid, 0) + 1
                    if oid is not None:
                        orig_gesamt[oid] = orig_gesamt.get(oid, 0) + 1
                for oid, n in zahl_o.items():
                    if oid is None:
                        if n != MENGE_OHNE_ORIGINAL:
                            w.append(f"{datei} k{k} s{s}: Prüfungshöhe "
                                     f"ohne Original {n} Zeilen, Menge "
                                     f"{MENGE_OHNE_ORIGINAL}")
                    elif n != MENGE_ORIGINAL:
                        w.append(f"{datei} k{k} s{s}: Original {oid} "
                                 f"{n}×, Menge {MENGE_ORIGINAL}")
            if h == "pflicht":
                p = gruppe[0].get("pflicht")
                pflicht_zahl[p] = pflicht_zahl.get(p, 0) + len(gruppe)
        if einheit == 0:
            w.extend(pruefe_zone_kette(datei, k, sprossen))
    if einheit == 0:
        w.extend(pruefe_zone_paar(zeilen, datei))
    for oid, n in orig_gesamt.items():
        if n != MENGE_ORIGINAL:
            w.append(f"{datei}: Original {oid} {n}× in der Einheit")
    for p, n in pflicht_zahl.items():
        if n != MENGE_PFLICHT:
            w.append(f"{datei}: pflicht {p} {n}×, Menge {MENGE_PFLICHT}")
    return b, w


def pruefe_zone_kette(datei, k, sprossen):
    """Zone: s1 zwei sehr leichte, s2 eine mittlere, ab s3 je
    Fallstrick eine (auch das Paar); Varianten über die Fertigkeit."""
    w = []
    soll = {1: 2, 2: 1}
    for s, gruppe in sprossen:
        n = soll.get(s, 1)
        if len(gruppe) != n:
            w.append(f"{datei} f{k} s{s}: {len(gruppe)} Zeilen, Menge {n}")
    v = [a["variante"] for _, g in sprossen for a in g]
    if v != list(range(1, len(v) + 1)):
        w.append(f"{datei} f{k}: Varianten nicht 1..n: {v}")
    if [s for s, _ in sprossen][:2] != [1, 2]:
        w.append(f"{datei} f{k}: Zone braucht s1 (leicht) und s2 (mittel)")
    # bank.md „Mengen je Kette“, Zone: s1 grundfall, ab s2 sprosse,
    # merkmal ab s3 „Fallstrick:“; das Zone-Paar (pflicht fehler und
    # die Zeile danach) folgt seiner eigenen Regel.
    reihe = [a for _, g in sprossen for a in g]
    paar = set()
    for i, a in enumerate(reihe):
        if a["hoehe"] == "pflicht":
            paar.update(range(i, min(i + 2, len(reihe))))
    for i, a in enumerate(reihe):
        if i in paar:
            continue
        s = a["sprosse"]
        soll = "grundfall" if s == 1 else "sprosse"
        if a["hoehe"] != soll:
            w.append(f"{datei} {a['id']}: hoehe {a['hoehe']}, Zone s{s} "
                     f"hat hoehe {soll}")
        if s >= 3 and not str(a["merkmal"]).startswith("Fallstrick:"):
            w.append(f"{datei} {a['id']}: merkmal beginnt nicht mit "
                     f"„Fallstrick:“ (Zone s{s})")
    return w


def pruefe_zone_paar(zeilen, datei):
    """Einmal je Zone: Fehler finden (pflicht fehler), direkt danach
    in derselben Kette eine Rechenaufgabe (hoehe sprosse)."""
    paare = 0
    for i, a in enumerate(zeilen):
        if a["hoehe"] == "pflicht":
            n = zeilen[i + 1] if i + 1 < len(zeilen) else None
            if (a.get("pflicht") == "fehler" and n is not None
                    and n["kette_nr"] == a["kette_nr"]
                    and n["hoehe"] == "sprosse"):
                paare += 1
            else:
                return [f"{datei}: Zone-Paar unvollständig bei {a['id']}"]
    if paare != 1:
        return [f"{datei}: {paares(paare)}, Menge Zone-Paar 1"]
    return []


def paares(n):
    return "kein Zone-Paar" if n == 0 else f"{n} Zone-Paare"


def pruefe_katalog(a, katalog):
    b = []
    q = a["quelle"]
    if not 1 <= q <= len(katalog):
        return [f"quelle {q} außerhalb des Katalogs"]
    if a["sprosse_text"] not in katalog[q - 1]:
        b.append(f"sprosse_text nicht wortgleich in Zeile {q}")
    if a["kette"] not in "\n".join(katalog):
        b.append("kette nicht wortgleich im Katalog")
    return b


# --- Lauf ----------------------------------------------------------------

def lade(datei):
    zeilen = []
    for i, roh in enumerate(datei.read_text(encoding="utf-8")
                            .split("\n"), 1):
        if roh == "":
            continue
        try:
            zeilen.append(json.loads(roh))
        except json.JSONDecodeError as e:
            raise SystemExit(f"{datei}:{i}: kein JSON ({e})")
    return zeilen


def kontext(eintrag, wurzel):
    """Bausteine und Sperre aus den Mappen; fehlt eine, Warnung."""
    ctx, w = {}, []
    bs = wurzel / "mappen" / "_bausteine.md"
    if bs.exists():
        ctx["bausteine"] = lade_bausteine(bs)
    else:
        w.append("mappen/_bausteine.md fehlt – Bausteinprobe entfällt")
    mp = wurzel / "mappen" / f"{eintrag}.md"
    if mp.exists():
        ctx["sperre"] = lade_sperre(mp)
        ctx["originale"] = originale_aus(mp.read_text(encoding="utf-8"))
    else:
        w.append(f"mappen/{eintrag}.md fehlt – Sperrprobe und "
                 f"Kennungsprobe entfallen")
    return ctx, w


def pruefe_eintrag(eintrag, katalog=None, wurzel=Path("."), alle=False):
    ordner = wurzel / "bank" / eintrag
    dateien = sorted(ordner.glob("*.jsonl"),
                     key=lambda p: (p.stem != "zone", p.stem))
    if not dateien:
        raise SystemExit(f"keine jsonl in {ordner}")
    ctx, wg = kontext(eintrag, wurzel)
    for x in wg:
        print(f"WARNUNG {x}")
    abw, warn = 0, len(wg)
    summe = []
    ids = {}
    texte = {}
    for datei in dateien:
        da, dw = 0, 0
        roh = datei.read_text(encoding="utf-8")
        if roh.startswith("﻿") or "\r" in roh or "\n\n" in roh:
            print(f"ABWEICHUNG {datei.name}: BOM, CR oder Leerzeile")
            da += 1
        m = re.fullmatch(r"e(\d+)|zone", datei.stem)
        if not m:
            print(f"ABWEICHUNG {datei.name}: Dateiname")
            abw += da + 1
            summe.append((datei.name, da + 1, dw))
            continue
        einheit = int(m.group(1)) if m.group(1) else 0
        zeilen = lade(datei)
        for a in zeilen:
            befunde, warnungen = pruefe_zeile(a, eintrag, einheit, ctx)
            if not befunde and katalog is not None:
                befunde = pruefe_katalog(a, katalog)
            aid = a.get("id", "?")
            if aid in ids:
                befunde.append(f"id doppelt (auch {ids[aid]})")
            ids[aid] = datei.name
            # gleiche Aufgabe = gleicher Text und gleiche Grafik
            t = re.sub(r"\s+", " ", a.get("aufgabe", "") + " | "
                       + a.get("grafik", "")).strip()
            if t and t in texte:
                befunde.append(f"aufgabe doppelt (wie {texte[t]})")
            texte[t] = aid
            if befunde:
                da += 1
                print(f"ABWEICHUNG {aid}: " + "; ".join(befunde))
            elif alle:
                print(f"OK {aid}")
            for x in warnungen:
                dw += 1
                print(f"WARNUNG {aid}: {x}")
        for f in FELDER_NEU:
            n = sum(1 for a in zeilen if f not in a)
            if n:
                dw += 1
                print(f"WARNUNG {datei.name}: Feld {f} fehlt in {n} "
                      f"von {len(zeilen)} Zeilen")
        if all(set(FELDER) <= set(a) for a in zeilen):
            kb, kw = pruefe_ketten(zeilen, datei.name, einheit)
            for x in kb:
                da += 1
                print(f"ABWEICHUNG {x}")
            for x in kw:
                dw += 1
                print(f"WARNUNG {x}")
        abw += da
        warn += dw
        summe.append((datei.name, da, dw))
    for name, da, dw in summe:
        print(f"{name}: Abweichungen {da}, Warnungen {dw}")
    print(f"Abweichungen: {abw}, Warnungen: {warn}")
    return abw


MENGE_BASIS = 10


def pruefe_basis(wurzel=Path("."), alle=False):
    """bank/_basis/<eintrag>.jsonl (v0.6): Zeilenprüfung wie v0.5 mit
    basis=True; Ketten lückenlos, Varianten 1..n, Menge 10 je Kette."""
    ordner = wurzel / "bank" / "_basis"
    dateien = sorted(ordner.glob("*.jsonl"))
    if not dateien:
        raise SystemExit(f"keine jsonl in {ordner}")
    abw, warn, summe, ids, texte = 0, 0, [], {}, {}
    for datei in dateien:
        eintrag = datei.stem
        ctx, wg = kontext(eintrag, wurzel)
        da, dw = 0, 0
        for x in wg:
            dw += 1
            print(f"WARNUNG {x}")
        roh = datei.read_text(encoding="utf-8")
        if roh.startswith("\ufeff") or "\r" in roh or "\n\n" in roh:
            print(f"ABWEICHUNG {datei.name}: BOM, CR oder Leerzeile")
            da += 1
        zeilen = lade(datei)
        for a in zeilen:
            einheit = a.get("einheit")
            if not isinstance(einheit, int) or isinstance(einheit, bool) \
                    or einheit < 1:
                befunde = ["einheit keine Zahl ab 1"]
            else:
                befunde, _ = pruefe_zeile(a, eintrag, einheit, ctx, True)
            aid = a.get("id", "?")
            if aid in ids:
                befunde.append(f"id doppelt (auch {ids[aid]})")
            ids[aid] = datei.name
            t = re.sub(r"\s+", " ", a.get("aufgabe", "") + " | "
                       + a.get("grafik", "")).strip()
            if t and t in texte:
                befunde.append(f"aufgabe doppelt (wie {texte[t]})")
            texte[t] = aid
            if befunde:
                da += 1
                print(f"ABWEICHUNG {aid}: " + "; ".join(befunde))
            elif alle:
                print(f"OK {aid}")
        ketten = {}
        for a in zeilen:
            ketten.setdefault(a.get("kette_nr"), []).append(a)
        nr = [a.get("kette_nr") for a in zeilen]
        folge = [k for i, k in enumerate(nr) if i == 0 or nr[i - 1] != k]
        if folge != list(range(1, len(ketten) + 1)):
            da += 1
            print(f"ABWEICHUNG {datei.name}: kette_nr nicht lückenlos "
                  f"und zusammenhängend ab 1: {folge}")
        for k, reihe in sorted(ketten.items(), key=lambda x: str(x[0])):
            if len({a.get("kette") for a in reihe}) > 1:
                da += 1
                print(f"ABWEICHUNG {datei.name} k{k}: kette-Name wechselt")
            if len({(a.get("original") or {}).get("id") for a in reihe}) > 1:
                da += 1
                print(f"ABWEICHUNG {datei.name} k{k}: original wechselt")
            v = [a.get("variante") for a in reihe]
            if v != list(range(1, len(v) + 1)):
                da += 1
                print(f"ABWEICHUNG {datei.name} k{k}: Varianten nicht "
                      f"1..n: {v}")
            if len(reihe) != MENGE_BASIS:
                dw += 1
                print(f"WARNUNG {datei.name} k{k}: {len(reihe)} Zeilen, "
                      f"Menge basis = {MENGE_BASIS}")
        abw += da
        warn += dw
        summe.append((datei.name, da, dw))
    for name, da, dw in summe:
        print(f"{name}: Abweichungen {da}, Warnungen {dw}")
    print(f"Abweichungen: {abw}, Warnungen: {warn}")
    return abw


def selbsttest():
    """Sechs Beispielzeilen (drei richtige, drei falsche), dann je
    Änderung von v0.3, v0.4 und v0.5 ein Fall, der in der Vorfassung
    falsch lief, und einer, der richtig bleibt."""
    basis = {"eintrag": "test", "einheit": 2, "kette": "Prozentsatz",
             "kette_nr": 1, "merkmal": "Ganzes 100",
             "form": "teil", "antwort": "__ %", "original": None,
             "grafik": "", "loesungsgrafik": "", "quelle": 1,
             "sprosse_text": "Teil von 100", "hoehe": "grundfall",
             "sprosse": 1}
    z = [dict(basis, variante=1,
              aufgabe="$37$ von $100$ – wie viel Prozent?",
              loesung="$37\\,\\%$", pruef="37/100*100"),
         dict(basis, variante=2,
              aufgabe="$1\\,250$ von $4\\,000$ – wie viel Prozent?",
              loesung="$1\\,250 : 4\\,000 = 0{,}3125 \\approx "
                      "31{,}3\\,\\%$",
              pruef="[1250/4000, 1250/4000*100]"),
         dict(basis, variante=3, form="ankreuzen",
              aufgabe="$12$ von $48$ – wie viel Prozent? Kreuze an.\\\\ "
                      "\\kreuz{$12\\,\\%$}\\\\ \\kreuz{$25\\,\\%$}\\\\ "
                      "\\kreuz{$36\\,\\%$}",
              loesung="$12 : 48 = 0{,}25 = 25\\,\\%$", pruef="12/48*100"),
         dict(basis, variante=4,
              aufgabe="$9$ von $12$ – wie viel Prozent?",
              loesung="$70\\,\\%$", pruef="9/12*100"),
         dict(basis, variante=5,
              aufgabe="$3$ von $12$ – wie viel Prozent?",
              loesung="$3$ von $12$ sind ein Viertel, also $25\\,\\%$",
              pruef="3/12*100"),
         dict(basis, variante=6, form="ankreuzen",
              aufgabe="$6$ von $24$ – wie viel Prozent? Kreuze an.\\\\ "
                      "\\kreuz{$25\\,\\%$}\\\\ \\kreuz{$25\\,\\%$}",
              loesung="$25\\,\\%$", pruef="6/24*100")]
    erwartet = [True, True, True, False, False, False]
    ok = True
    for zeile, soll in zip(z, erwartet):
        zeile["id"] = f"test-e2-k1-s1-v{zeile['variante']}"
        befunde, _ = pruefe_zeile(zeile, "test", 2)
        ist = not befunde
        zeichen = "OK" if ist else "ABWEICHUNG"
        print(f"{zeichen} {zeile['id']}" + ("" if ist else ": "
                                           + "; ".join(befunde)))
        ok &= ist == soll
    for punkt, text, ist, soll in (faelle_v03(basis)
                                   + faelle_v04(basis)
                                   + faelle_v05(basis)):
        zeichen = "OK" if ist == soll else "FEHLER"
        print(f"{zeichen} {punkt}) {text}")
        ok &= ist == soll
    print("Selbsttest bestanden" if ok else "Selbsttest GESCHEITERT")
    return 0 if ok else 1


def faelle_v03(basis):
    """[(Punkt, Beschreibung, ist, soll)] für die Änderungen a–g.
    ist/soll: True = ohne Befund (Abweichung bzw. Warnung)."""
    def zeile(**k):
        z = dict(basis, variante=1, aufgabe="$3$ von $4$?",
                 loesung="$75\\,\\%$", pruef="75")
        z.update(k)
        if z["einheit"] == 0:
            z["id"] = f"test-zone-f{z['kette_nr']}-v{z['variante']}"
        else:
            z["id"] = (f"test-e{z['einheit']}-k{z['kette_nr']}-"
                       f"s{z['sprosse']}-v{z['variante']}")
        return z

    def ohne(z):
        return not pruefe_zeile(z, "test", z["einheit"])[0]

    def warnfrei(zeilen):
        return not pruefe_ketten(zeilen, "t.jsonl",
                                 zeilen[0]["einheit"])[1]

    def reihe(teile, **k):
        """Kette aus [(sprosse, hoehe, zahl, felder)]."""
        aus = []
        for s, h, n, extra in teile:
            for v in range(1, n + 1):
                aus.append(zeile(sprosse=s, hoehe=h, variante=v,
                                 aufgabe=f"k{k.get('kette_nr', 1)} s{s} "
                                         f"v{v}", **dict(k, **extra)))
        return aus

    def zone(s1="grundfall", merkmal3="Fallstrick: vertauscht"):
        teile = [(1, s1, 2, {}), (2, "sprosse", 1, {}),
                 (3, "sprosse", 1, {"merkmal": merkmal3}),
                 (4, "pflicht", 1, {"pflicht": "fehler",
                                    "merkmal": "Zone-Paar: Fehler finden"}),
                 (5, "sprosse", 1, {"merkmal": "Zone-Paar: selbst"})]
        z = []
        for s, h, n, extra in teile:
            for _ in range(n):
                z.append(zeile(einheit=0, sprosse=s, hoehe=h,
                               variante=len(z) + 1,
                               aufgabe=f"Zone {len(z) + 1}", **extra))
        return z

    orig = {"id": "2018-OS-K7a", "jahr": 2018, "papier": "OS"}
    pruef3 = (1, "grundfall", 5, {}), (2, "pruefung", 3, {})
    optionen_terme = ("Welcher Term? \\\\ \\kreuz{$4x$} \\\\ "
                      "\\kreuz{$x + 4$} \\\\ \\kreuz{$4 - x$}")
    optionen_pyth = ("Welche Gleichung gilt? \\\\ "
                     "\\kreuz{$c^2 = a^2 + b^2$} \\\\ "
                     "\\kreuz{$a^2 = b^2 + c^2$} \\\\ \\kreuz{$c = a + b$}")
    sperre = sperre_aus(
        "## 1 Katalogeintrag\n"
        " 40  ### Merkkasten\n"
        " 41  Beispiel 6² + 8² = 100; (x + 3)² = 25; x² = 36; "
        "Anteil \\frac{1}{10}; Punkt (12|5)\n"
        "## 2 Originale (1)\n"
        "### 2015-OS-K2a (test)\n"
        "- verfahren: 3 · 12 Kinder\n")

    def gesperrt(aufgabe, sprosse_text="Teil von 100"):
        z = zeile(aufgabe=aufgabe, sprosse_text=sprosse_text)
        return not sperrprobe(z, sperre)

    return [
        ("a", "pruefung mit original null ohne Abweichung",
         ohne(zeile(sprosse=2, hoehe="pruefung", original=None)), True),
        ("a", "vollständiges original an hoehe sprosse erlaubt",
         ohne(zeile(sprosse=2, hoehe="sprosse", original=orig)), True),
        ("a", "unvollständiges original bleibt Abweichung",
         ohne(zeile(sprosse=2, hoehe="sprosse",
                    original={"id": "2018-OS-K7a"})), False),
        ("a", "Prüfungshöhe ohne Original mit 3 Zeilen ohne Warnung",
         warnfrei(reihe(pruef3)), True),
        ("a", "Prüfungshöhe ohne Original mit 2 Zeilen warnt",
         warnfrei(reihe([pruef3[0], (2, "pruefung", 2, {})])), False),
        ("b", "Zone s1 hoehe sprosse warnt (zwei Zeilen)",
         len(pruefe_ketten(zone(s1="sprosse"), "zone.jsonl", 0)[1]) == 0,
         False),
        ("b", "Zone s3 ohne „Fallstrick:“ im merkmal warnt",
         warnfrei(zone(merkmal3="vertauscht")), False),
        ("b", "Zone nach Regel 4 samt Zone-Paar ohne Warnung",
         warnfrei(zone()), True),
        ("c", "„Liegt P auf dem Graphen von f?“ ohne grafik",
         ohne(zeile(aufgabe="Liegt $P(2|5)$ auf dem Graphen von "
                            "$f(x) = 2x + 1$?", loesung="ja, $f(2) = 5$",
                    pruef="2*2+1", form="text")), True),
        ("c", "„ohne zu zeichnen“ ist kein Zeichenauftrag",
         ohne(zeile(aufgabe="Beschreibe den Verlauf, ohne zu zeichnen.",
                    loesung="steigt", pruef="", form="text")), True),
        ("c", "„Lies … ab“ ohne grafik bleibt Abweichung",
         ohne(zeile(aufgabe="Lies den Schnittpunkt mit der y-Achse ab.",
                    loesung="$(0|3)$", pruef="[0, 3]", form="text")),
         False),
        ("c", "form zeichnen ohne grafik bleibt Abweichung",
         ohne(zeile(aufgabe="Zeichne die Gerade.", loesung="Gerade",
                    pruef="", form="zeichnen")), False),
        ("d", "Termoptionen 4x, x + 4, 4 − x: Lösung $4x$, pruef 4",
         ohne(zeile(aufgabe=optionen_terme, form="ankreuzen",
                    loesung="$4x$", pruef="4")), True),
        ("d", "Termoptionen: pruef \"\" erlaubt",
         ohne(zeile(aufgabe=optionen_terme, form="ankreuzen",
                    loesung="$4x$", pruef="")), True),
        ("d", "Formeln mit ²: Lösung nennt Option wortgleich",
         ohne(zeile(aufgabe=optionen_pyth, form="ankreuzen",
                    loesung="$c^2 = a^2 + b^2$ – c ist die Hypotenuse",
                    pruef="")), True),
        ("d", "Formeln mit ²: „Kreuz bei der ersten“ ist Abweichung",
         ohne(zeile(aufgabe=optionen_pyth, form="ankreuzen",
                    loesung="Kreuz bei der ersten Gleichung",
                    pruef="")), False),
        ("d", "Zahloptionen: Lösungszahl in zwei Optionen bleibt Abw.",
         ohne(zeile(aufgabe="\\kreuz{$4$ cm} \\\\ \\kreuz{$4$ cm} \\\\ "
                            "\\kreuz{$5$ cm}", form="ankreuzen",
                    loesung="$4$ cm", pruef="4")), False),
        ("e", "Zahlterm 6² + 8² aus dem Kasten gesperrt",
         gesperrt("Berechne $6^2 + 8^2$."), False),
        ("e", "(x + 3)² mit einer Zahl gesperrt",
         gesperrt("Löse $(x + 3)^2 = 16$."), False),
        ("e", "x² = 36 mit einer Zahl gesperrt",
         gesperrt("Löse $x^2 = 36$."), False),
        ("e", "(x + 3)² als Gegenstand der Kette frei",
         gesperrt("Löse $(x + 3)^2 = 16$.", "Klammer (x + 3)² lösen"),
         True),
        ("e", "\\frac{1}{12} \\cdot 3 ist kein Paar 3 · 12",
         gesperrt("Rechne $\\frac{1}{12} \\cdot 3$."), True),
        ("e", "12 · 3 bleibt als Paar gesperrt",
         gesperrt("Rechne $12 \\cdot 3$."), False),
        ("e", "einzelner Bruch 1/10 ist kein Zahlenpaar",
         gesperrt("$\\frac{1}{10}$ von $50$ € – wie viel?"), True),
        ("e", "Punkt (12|5) bleibt gesperrt",
         gesperrt("Liegt $(12|5)$ auf f?"), False),
        ("e", "gemischte Zahl 3\\frac{3}{5} als 18/5 gelesen",
         not vergleiche("[18, 5]", "$3\\frac{3}{5}$"), True),
        ("f", "„$-\\,6$“ als −6 gelesen",
         not vergleiche("-6", "$-\\,6$"), True),
        ("f", "„$-\\;6$“ als −6 gelesen",
         not vergleiche("-6", "$x = -\\;6$"), True),
        ("f", "in „x^2 - 12x“ ist −12 die Zahl",
         not vergleiche("-12", "$x^2 - 12x$"), True),
        ("f", "pruef \"\": 2 in x^2 keine Lösungsziffer",
         ohne(zeile(loesung="$z^2 = x^2 + y^2$", pruef="")), True),
        ("f", "„20 - 5 = 15“: 15 bleibt Ergebnis",
         not vergleiche("15", "$20 - 5 = 15$"), True),
        ("f", "„100 % - 90 % = 10 %“: 10 bleibt Ergebnis",
         not vergleiche("10", "$100\\,\\% - 90\\,\\% = 10\\,\\%$"), True),
        ("f", "pruef \"\" bei „x = 5“ bleibt „pruef fehlt“",
         ohne(zeile(loesung="$x = 5$", pruef="")), False),
        ("g", "zwei Verfahrensketten mit je 5 Grundfällen ohne Warnung",
         warnfrei(reihe([(1, "grundfall", 5, {})])
                  + reihe([(1, "grundfall", 5, {"kette": "Zweite"})],
                          kette_nr=2)), True),
        ("g", "Grundfall mit 4 Zeilen warnt weiter",
         warnfrei(reihe([(1, "grundfall", 4, {})])), False),
    ]


def faelle_v04(basis):
    """[(Punkt, Beschreibung, ist, soll)] für die Änderungen a–b der
    v0.4; je Punkt ein Fall, der in v0.3 falsch lief, und einer, der
    richtig bleibt. ist/soll: True = wie erwartet ohne Befund bzw.
    Zeile gedruckt."""
    import contextlib
    import io
    import tempfile

    def zeile(v, **k):
        z = dict(basis, eintrag="t", variante=v, sprosse=2,
                 hoehe="pruefung", aufgabe=f"$3$ von $4$? ({v})",
                 loesung="$75\\,\\%$", pruef="75",
                 id=f"t-e2-k1-s2-v{v}")
        z.update(k)
        return z

    # seit v0.5 gilt eine Kennung, wenn sie in der Mappe steht
    mappe = {"originale": {"2025-C-2b", "2025MerhoehtAAGLAA121-a",
                           "2018-OS-K7a"}}

    def ohne(o):
        return not pruefe_zeile(zeile(1, original=o), "t", 2, mappe)[0]

    with tempfile.TemporaryDirectory() as d:
        ordner = Path(d) / "bank" / "t"
        ordner.mkdir(parents=True)
        (ordner / "e2.jsonl").write_text(
            json.dumps(zeile(1), ensure_ascii=False) + "\n"
            + json.dumps(zeile(2, loesung="$70\\,\\%$"),
                         ensure_ascii=False) + "\n", encoding="utf-8")
        aus = {}
        for alle in (False, True):
            puffer = io.StringIO()
            with contextlib.redirect_stdout(puffer):
                pruefe_eintrag("t", None, Path(d), alle)
            aus[alle] = puffer.getvalue().split("\n")
    return [
        ("a", "ohne --alle keine OK-Zeile",
         "OK t-e2-k1-s2-v1" not in aus[False], True),
        ("a", "ohne --alle ABWEICHUNG und Summe gedruckt",
         any(x.startswith("ABWEICHUNG t-e2-k1-s2-v2") for x in aus[False])
         and any(x.startswith("e2.jsonl: Abweichungen") for x in aus[False])
         and any(x.startswith("Abweichungen:") for x in aus[False]), True),
        ("a", "--alle druckt die OK-Zeile",
         "OK t-e2-k1-s2-v1" in aus[True], True),
        ("b", "FHR-Kennung 2025-C-2b gilt",
         ohne({"id": "2025-C-2b", "jahr": 2025, "papier": "C"}), True),
        ("b", "Abitur-Kennung 2025MerhoehtAAGLAA121-a gilt",
         ohne({"id": "2025MerhoehtAAGLAA121-a", "jahr": 2025,
               "papier": "2025-iqb-ea"}), True),
        ("b", "MSA-Kennung 2018-OS-K7a gilt weiter",
         ohne({"id": "2018-OS-K7a", "jahr": 2018, "papier": "OS"}), True),
        ("b", "FHR-Kennung mit Heft D bleibt Abweichung",
         ohne({"id": "2025-D-2b", "jahr": 2025, "papier": "D"}), False),
    ]


def faelle_v05(basis):
    """[(Punkt, Beschreibung, ist, soll)] für die Änderungen a–c der
    v0.5; je Punkt Fälle, die in v0.4 falsch liefen, und Fälle, die
    richtig bleiben. ist/soll: True = ohne Befund."""
    import contextlib
    import io
    import tempfile

    mini = ("## 1 Katalogeintrag\n"
            " 40  ### Merkkasten\n"
            " 41  Punkt A(1 | 2 | 0); Beispiel f(x) = 2x⁴ − 5x; "
            "Punkt (12|5)\n"
            "## 2 Originale (3)\n"
            "### 2019-be-gk-A1.1a (abi-katalog.csv)\n"
            "- jahr 2019, papier 2019-be-gk\n"
            "### 2021MerhoehtAAnalysis12-a (iqb-katalog.csv)\n"
            "### 2017MgrundlegendBAnalysisWTR-1d (iqb-katalog.csv)\n"
            "## 3 Maßstab\n"
            "### 3.6\n")

    def zeile(v=1, **k):
        z = dict(basis, eintrag="t", variante=v, sprosse=2,
                 hoehe="sprosse", aufgabe=f"$3$ von $4$? ({v})",
                 loesung="$75\\,\\%$", pruef="75",
                 id=f"t-e2-k1-s2-v{v}")
        z.update(k)
        return z

    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "mappen").mkdir()
        (Path(d) / "mappen" / "t.md").write_text(mini, encoding="utf-8")
        ctx, _ = kontext("t", Path(d))
        # ohne Mappe: Warnung, Kennungsprobe ausgesetzt
        ordner = Path(d) / "bank" / "u"
        ordner.mkdir(parents=True)
        fremd = {"id": "2019-be-gk-Z9.9z", "jahr": 2019,
                 "papier": "2019-be-gk"}
        (ordner / "e2.jsonl").write_text(json.dumps(
            zeile(eintrag="u", id="u-e2-k1-s1-v1", sprosse=1,
                  hoehe="grundfall", original=fremd),
            ensure_ascii=False) + "\n", encoding="utf-8")
        puffer = io.StringIO()
        with contextlib.redirect_stdout(puffer):
            ohne_mappe = pruefe_eintrag("u", None, Path(d))
        druck = puffer.getvalue()

    def ohne(z, c=ctx):
        return not pruefe_zeile(z, "t", 2, c)[0]

    def orig(kid, jahr=None, papier="x"):
        return {"id": kid, "jahr": jahr or int(kid[:4]), "papier": papier}

    def gesperrt(aufgabe):
        return not sperrprobe(zeile(aufgabe=aufgabe), ctx["sperre"])

    def grafik(loesung, pruef, g):
        return not grafikprobe(zeile(loesung=loesung, pruef=pruef,
                                     grafik=g))

    ksys3 = "\\begin{ksys3}[x1max=4] \\end{ksys3}"
    return [
        ("a", "Landeskennung 2019-be-gk-A1.1a aus der Mappe gilt",
         ohne(zeile(original=orig("2019-be-gk-A1.1a"))), True),
        ("a", "IQB-Kennung 2021MerhoehtAAnalysis12-a gilt",
         ohne(zeile(original=orig("2021MerhoehtAAnalysis12-a"))), True),
        ("a", "Teil-B-Kennung 2017MgrundlegendBAnalysisWTR-1d gilt",
         ohne(zeile(original=orig("2017MgrundlegendBAnalysisWTR-1d"))),
         True),
        ("a", "2019-be-gk-Z9.9z fehlt in der Mappe: Abweichung",
         ohne(zeile(original=orig("2019-be-gk-Z9.9z"))), False),
        ("a", "id beginnt nicht mit jahr: Abweichung",
         ohne(zeile(original=orig("2019-be-gk-A1.1a", 2020))), False),
        ("a", "papier leer: Abweichung",
         ohne(zeile(original=orig("2019-be-gk-A1.1a", papier=""))), False),
        ("a", "Überschrift aus Abschnitt 3 ist keine Kennung",
         ohne(zeile(original=orig("3.6", 3))), False),
        ("a", "ohne Mappe Warnung, Kennung nicht geprüft",
         ohne_mappe == 0 and "Kennungsprobe entfallen" in druck, True),
        ("b", "Tripel (3 | -1 | 2): alle drei an der Ergebnisstelle",
         not vergleiche("[3, -1, 2]",
                        "$A(1 | 2 | 0)$, $B(3 | -1 | 2)$"), True),
        ("b", "Paar (4|-2) weiter mit beiden Zahlen gelesen",
         not vergleiche("[4, -2]", "Scheitel $S(4 | -2)$"), True),
        ("b", "Tripel A(1 | 2 | 0) aus dem Kasten gesperrt",
         gesperrt("Liegt $A(1 \\mid 2 \\mid 0)$ auf g?"), False),
        ("b", "anderes Tripel (1 | 2 | 5) frei",
         gesperrt("Liegt $P(1 | 2 | 5)$ auf g?"), True),
        ("b", "Tripel (12 | 5 | 1) ist nicht das Paar (12|5)",
         gesperrt("Liegt $Q(12 | 5 | 1)$ auf g?"), True),
        ("b", "Paar (12|5) bleibt gesperrt",
         gesperrt("Liegt $(12|5)$ auf f?"), False),
        ("b", "Ursprung (0 | 0 | 0) ist kein gesperrtes Tripel",
         not ("paar", ("Tripel", 0, 0, 0)) in sperre_aus(
             mini.replace("A(1 | 2 | 0)", "O(0 | 0 | 0)")), True),
        ("b", "Tripel außerhalb des ksys3: Abweichung",
         grafik("$P(5 | 1 | 1)$", "5", ksys3), False),
        ("b", "Tripel im ksys3 ohne Befund",
         grafik("$P(4 | -3 | 5)$", "4", ksys3), True),
        ("b", "Paar außerhalb des ksys bleibt Abweichung",
         grafik("$(9 | 1)$", "[9, 1]", "\\begin{ksys}\\end{ksys}"),
         False),
        ("c", "2x⁴ − 5x der Mappe sperrt 2x^4 - 5x",
         gesperrt("Leite $g(x) = 2x^4 - 5x$ ab."), False),
        ("c", "2x^4 - 7x bleibt frei",
         gesperrt("Leite $g(x) = 2x^4 - 7x$ ab."), True),
        ("c", "x¹⁰ und x^{10} gleich normiert, x² bleibt x²",
         mathnorm("x¹⁰") == mathnorm("x^{10}")
         and mathnorm("x²") == mathnorm("x^2") == "x²", True),
    ]


def main(argv):
    if argv[1:] == ["--selbsttest"]:
        return selbsttest()
    args = argv[1:]
    alle = "--alle" in args
    args = [x for x in args if x != "--alle"]
    if len(args) not in (1, 3) or (len(args) == 3
                                   and args[1] != "--katalog"):
        print(__doc__)
        return 2
    katalog = None
    if len(args) == 3:
        katalog = Path(args[2]).read_text(encoding="utf-8").split("\n")
    wurzel = Path(__file__).resolve().parent.parent
    if args[0] == "_basis" and katalog is None:
        return 1 if pruefe_basis(wurzel, alle) else 0
    return 1 if pruefe_eintrag(args[0], katalog, wurzel, alle) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

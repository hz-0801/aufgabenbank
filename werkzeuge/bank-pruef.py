#!/usr/bin/env python3
"""Prüft die Bank eines Katalogeintrags (bank.md, Abschnitt „Prüfung").

v0.2. Aufruf:
    python3 werkzeuge/bank-pruef.py <eintrag> [--katalog DATEI]
    python3 werkzeuge/bank-pruef.py --selbsttest

Liest bank/<eintrag>/zone.jsonl und e<n>.jsonl, dazu
mappen/<eintrag>.md (Sperrprobe) und mappen/_bausteine.md
(Bausteinprobe). Ausgabe je Aufgabe eine Zeile OK/ABWEICHUNG,
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
TOLERANZ = Decimal("0.005")

# Zahl mit Dezimalkomma; Tausender sind vorher zusammengezogen.
ZAHL = re.compile(r"(?<![\d,])[-−]?\d+(?:,\d+)?")
PUNKT = re.compile(r"\(\s*([-−]?\d+(?:,\d+)?)\s*\|\s*([-−]?\d+(?:,\d+)?)"
                   r"\s*\)")

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
    t = t.replace("\\,", " ").replace("\\%", "%")
    t = t.replace("\\approx", "≈").replace("−", "-")
    t = re.sub(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)
    t = re.sub(r"\^\{[^}]*\}|\^-?\d", " ", t)          # x^2, 2^{10}
    t = re.sub(r"_\{[^}]*\}|_\d+", "", t)              # x_1, S_{12}
    t = re.sub(r"\\[A-Za-z]+", " ", t)                 # \frac, \cdot
    t = t.replace("{", "").replace("}", "")
    # Buchstaben mit angehängter Ziffer (x1, a2) sind keine Zahlen.
    t = re.sub(r"[A-Za-z]\d+", " ", t)
    return t


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
    nach = oder ≈, beide Zahlen eines Punkts (x|y) oder Bruchs a/b an
    der Ergebnisstelle, und die Glieder einer Aufzählung von
    Ergebnissen (4; 1; 0)."""
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
        aus += [zahl(m.group(1)), zahl(m.group(2))]
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


def grafikprobe(a):
    b = []
    grafik = a.get("grafik", "")
    if (a["form"] == "zeichnen"
            or re.search(r"\bGraph(en)?\b", a["aufgabe"])) and not grafik:
        b.append("grafik leer (form zeichnen oder „Graph“ in aufgabe)")
    bereiche = ksys_bereiche(grafik)
    if not bereiche:
        return b
    punkte = [("loesung", float(zahl(x)[0]), float(zahl(y)[0]))
              for x, y in PUNKT.findall(normiert(a["loesung"]))]
    if a["pruef"]:
        try:
            for w in werte_aus(a["pruef"]):
                if isinstance(w, (list, tuple)) and len(w) == 2:
                    punkte.append(("pruef", float(w[0]), float(w[1])))
        except Exception:  # noqa: BLE001 – meldet vergleiche()
            pass
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
    return b


# --- Ankreuzen -----------------------------------------------------------

def ankreuzprobe(a):
    """Zahloptionen (eine Zahl, ggf. Einheit): die Lösungszahl steht
    in genau einer."""
    if a["form"] != "ankreuzen" or not a["pruef"]:
        return []
    optionen = []
    for m in re.finditer(r"\\kreuz(?=\{)", a["aufgabe"]):
        e = klammer(a["aufgabe"], m.end())
        optionen.append(a["aufgabe"][m.end() + 1:e - 1])
    zahlopt = []
    for o in optionen:
        z = zahlen_aus(o)
        rest = re.sub(ZAHL, "", normiert(o))
        if len(z) == 1 and not re.search(r"[=A-Za-z]{3,}|=", rest):
            zahlopt.append(z)
    if len(zahlopt) < 2:
        return []
    try:
        w = flach(werte_aus(a["pruef"]))[0]
    except Exception:  # noqa: BLE001 – meldet vergleiche()
        return []
    n = sum(1 for z in zahlopt if passt(w, z))
    if n != 1:
        return [f"Lösungszahl {w:g} in {n} von {len(zahlopt)} "
                f"Ankreuzoptionen (soll 1)"]
    return []


# --- Sperre --------------------------------------------------------------

def mathnorm(text):
    """Text und LaTeX auf eine Schreibweise: 3/4, ·, ², -, ohne $."""
    t = text.replace("{,}", ",").replace("\\%", "%")
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
OPERATOR = set("+-·:/=≈()|²³√%")


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
            if (re.search(r"[a-z]", seite)
                    and len(re.findall(r"\d+(?:,\d+)?", seite)) >= 2
                    and re.search(r"[\w)²][-+·:/][\w(]", seite)):
                aus.add(seite)       # Term mit Variable und Zahlbelegung
            if i + 1 < len(seiten):
                g = seite + "=" + seiten[i + 1]
                if (len(re.findall(r"\d+(?:,\d+)?", g)) >= 2
                        and seite and seiten[i + 1]):
                    aus.add(g)
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
    """Paare: Punkt (a|b), Anteil (a von b, a : b, a/b), Produkt."""
    t = mathnorm(text)
    n = r"(-?\d+(?:,\d+)?)"
    aus = set()
    for a, b in re.findall(r"\(\s*" + n + r"\s*\|\s*" + n + r"\s*\)", t):
        aus.add(("Punkt", zahl(a)[0], zahl(b)[0]))
    for muster, art in ((n + r"\s*%?\s*von\s*" + n, "Anteil"),
                        (n + r"\s*:\s*" + n, "Anteil"),
                        (n + r"\s*/\s*" + n, "Anteil"),
                        (n + r"\s*·\s*" + n, "Produkt")):
        for a, b in re.findall(r"(?<![\d,|])" + muster + r"(?![\d,])", t):
            x, y = zahl(a)[0], zahl(b)[0]
            if abs(x) <= 9 and abs(y) <= 9 and x == int(x) and y == int(y):
                continue                          # kleine Zahlen frei
            if art == "Produkt":
                x, y = sorted((x, y))
            aus.add((art, x, y))
    return aus


def lade_sperre(mappe):
    """{('gleichung'|'paar', muster): herkunft} aus der Mappe."""
    text = mappe.read_text(encoding="utf-8")
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
    art, x, y = p
    if art == "Punkt":
        return f"({x}|{y})"
    return f"{x} {'von' if art == 'Anteil' else '·'} {y}"


def sperrprobe(a, sperre):
    b = []
    aufgabe = ohne_raum(mathnorm(a["aufgabe"]))
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
            b.append(f"Sperre: Zahlenpaar {paar_text(muster)} "
                     f"({herkunft})")
    return b


# --- Zeile ---------------------------------------------------------------

def pruef_leer_erlaubt(a):
    return (a.get("pflicht") == "begruenden" or a["form"] == "zeichnen"
            or not re.search(r"\d", a["loesung"]))


def pruefe_zeile(a, eintrag, einheit, ctx=None):
    """Feld- und Rechenprüfung einer Zeile -> (Abweichungen, Warnungen)."""
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
    if einheit == 0:
        soll = f"{eintrag}-zone-f{a['kette_nr']}-v{a['variante']}"
    else:
        soll = (f"{eintrag}-e{einheit}-k{a['kette_nr']}-s{a['sprosse']}"
                f"-v{a['variante']}")
    if a["id"] != soll:
        b.append(f"id {a['id']!r} statt {soll!r}")
    if a["hoehe"] not in HOEHEN:
        b.append(f"hoehe {a['hoehe']!r} unbekannt")
    if a["hoehe"] == "pflicht":
        if a.get("pflicht") not in PFLICHT:
            b.append(f"pflicht {a.get('pflicht')!r} unbekannt")
    elif "pflicht" in a:
        b.append("pflicht nur bei hoehe pflicht")
    if a["form"] not in FORMEN:
        b.append(f"form {a['form']!r} unbekannt")
    if (a["sprosse"] == 0) != (a["hoehe"] == "vorstufe"):
        b.append("sprosse 0 genau dann, wenn hoehe vorstufe")
    o = a["original"]
    if a["hoehe"] == "pruefung":
        if not (isinstance(o, dict) and set(o) == {"id", "jahr", "papier"}
                and re.fullmatch(r"\d{4}-[A-Z]+-[A-Z]\d+[a-z]", o["id"])
                and o["id"].startswith(str(o["jahr"]))):
            b.append("original fehlt oder unvollständig")
    elif o is not None:
        b.append("original nur bei hoehe pruefung")
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
        if start not in (0, 1) or snr != list(range(start,
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
                    orig_gesamt[oid] = orig_gesamt.get(oid, 0) + 1
                for oid, n in zahl_o.items():
                    if n != MENGE_ORIGINAL:
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
    else:
        w.append(f"mappen/{eintrag}.md fehlt – Sperrprobe entfällt")
    return ctx, w


def pruefe_eintrag(eintrag, katalog=None, wurzel=Path(".")):
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
            else:
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


def selbsttest():
    """Sechs Beispielzeilen: drei richtige, drei falsche."""
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
    print("Selbsttest bestanden" if ok else "Selbsttest GESCHEITERT")
    return 0 if ok else 1


def main(argv):
    if argv[1:] == ["--selbsttest"]:
        return selbsttest()
    if len(argv) not in (2, 4) or (len(argv) == 4
                                   and argv[2] != "--katalog"):
        print(__doc__)
        return 2
    katalog = None
    if len(argv) == 4:
        katalog = Path(argv[3]).read_text(encoding="utf-8").split("\n")
    wurzel = Path(__file__).resolve().parent.parent
    return 1 if pruefe_eintrag(argv[1], katalog, wurzel) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

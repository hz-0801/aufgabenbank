#!/usr/bin/env python3
"""Setzer: ein Lernblatt ohne Modell aus Lernweg und Bankzeilen setzen.

    python3 werkzeuge/setzer.py <eintrag> <teil> --aus <ordner>
            [--sorte tisch-alt|tisch|selbst] [--kennung K]
            [--katalog DIR] [--kein-register] [--ohne-pdf]

Beispiele:
    python3 werkzeuge/setzer.py pythagoras 2k --aus /tmp/t6b --kennung T6B
    python3 werkzeuge/setzer.py pythagoras 1 --aus /tmp/h --sorte selbst

Liest den Lernweg-Block der Einheit aus
mathe-nachhilfe/katalog/<eintrag>.md (Abschnitt „Lernweg“) und die
Bankzeilen bank/<eintrag>/e*.jsonl. Gewählt wird der Block mit „Kennung
K“, wenn --kennung K ihn trifft, sonst der erste Block mit Zeilen
„| L<teil>-…“.

Zwei Blockformen:
- Schritte (bis 09.10.2026): Zeilen „| L<teil>-<n> | begreift | … |
  Aufgaben |“; Bankzeilen mit satz (bank.md „Felder für den Lernweg“).
- Abschnitte (Form 10.10.2026, bau/bauauftrag.md; Kopfzeile „Form:
  abschnitte“): Zeilen „| L<teil>-<B> | Name | Satz | Formel | Beispiel
  | Aufgaben | Vorrat |“ und Kopfzeilen Titel, Formel, In Worten,
  Vorgehen, Achtung, Bild, Fehler, Tisch; Bankzeilen mit rolle,
  ergebnis, schritte (bank.md). Die Kennung steht im Block; fehlt sie
  im Register, wird sie eingetragen.

Sorten (--sorte, Vorgabe tisch-alt):
- tisch-alt: wie bisher (Muster T6B/M74): Nummern, Lösungen im Fuß,
  Vorher/Weiter; 1-uebersicht, 2-blatt, 3-loesungen. Aus Abschnitten:
  das Beispiel als grau vorgerechnetes a) vor der ersten Aufgabe.
- tisch: kompakt je Abschnitt (Muster Prüfstein tisch.pdf), ohne
  Beispiel und Formel; 2-blatt, 3-loesungen.
- selbst: Übersicht mit „kann ich“, Formel auf einen Blick, je
  Abschnitt eine Seite (Satz, Formel, Beispiel, Aufgaben, Karo);
  Lösungen als eigenes PDF (Muster Prüfstein selbst.pdf); 2-blatt,
  3-loesungen.
tisch und selbst brauchen einen Block in Abschnittsform.

Kennung (Schrittform): neu nach bau/bauregeln.md „Kennung“ (drei Zeichen
aus 2–9 und A–Z ohne I und O, gegen bau/register.csv eindeutig) und eine
Zeile ins Register mit den gesetzten ids (Gruppen einer Nummer mit „+“).
Mit --kennung K wird ein Blatt aus dem Register wieder gesetzt: dieselben
ids, kein neuer Registereintrag.

mathblatt.sty liegt neben diesem Skript (nicht im Repo, .gitignore); fehlt
es, wird es von hz-0801/blattbau geholt.
"""
import argparse
import concurrent.futures as cf
import csv
import datetime
import json
import os
import random
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parent
STY_URL = ("https://raw.githubusercontent.com/hz-0801/blattbau/main/"
           "mathblatt.sty")
REGISTER = WURZEL / "bau" / "register.csv"
ZEICHEN = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
BUCHST = "abcdefghijklmnop"


# --- Eingaben ------------------------------------------------------------

def lies_lernweg(katalog, teil, kennung=None):
    """Kopf, Serie und Schritte (oder Abschnitte) des Lernweg-Blocks
    L<teil>; mit kennung der Block, der sie trägt."""
    text = katalog.read_text(encoding="utf-8")
    titel = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    serie = re.search(r"^Serie: (.+)$", text, re.M)
    praefix = f"L{teil}-"
    bloecke = [b for b in re.split(r"^(?=#### )", text, flags=re.M)
               if b.startswith("####") and f"| {praefix}" in b]
    block = next((b for b in bloecke if kennung and re.search(
        rf"Kennung {re.escape(kennung)}\b", b)), None)
    block = block or (bloecke[0] if bloecke else None)
    if block is None:
        sys.exit(f"Kein Lernweg-Block mit Schritten {praefix}… in {katalog}")
    if re.search(r"^Form: abschnitte\s*$", block, re.M):
        return lies_abschnitte(block, titel, serie, praefix)
    kopf = block.splitlines()[0]
    name = re.sub(r"^#### Lerneinheit \S+ – ", "", kopf)
    name = re.sub(r"\s*\(.*\)\s*$", "", name).strip()
    blatt = re.search(r"^Blatt: (.+)$", block, re.M)
    angaben = {}
    if blatt:
        teile = [t.strip() for t in blatt.group(1).split("·")]
        angaben["niveau"] = teile[0]
        for t in teile[1:]:
            k, _, v = t.partition(":")
            angaben[k.strip().lower()] = v.strip()
    schritte = []
    for z in block.splitlines():
        if not z.startswith(f"| {praefix}"):
            continue
        zellen = [c.strip() for c in z.strip().strip("|").split("|")]
        schritt, begreift, aufgaben = zellen[0], zellen[1], zellen[-1]
        blattteil = re.sub(r"\([^)]*\)", "", aufgaben)
        gruppen = [[i.strip() for i in g.split("+") if i.strip()]
                   for g in blattteil.split(",") if g.strip()]
        schritte.append((schritt, begreift, gruppen))
    return dict(titel=titel, name=name, serie=serie.group(1) if serie
                else "", schritte=schritte, **angaben)


def lies_abschnitte(block, titel, serie, praefix):
    """Lernweg-Block in Abschnittsform (bau/bauauftrag.md 10.10.2026)."""
    kopf = block.splitlines()[0]
    name = re.sub(r"^#### Lerneinheit \S+ – ", "", kopf)
    name = re.sub(r"\s*\(.*\)\s*$", "", name).strip()
    lw = dict(titel=titel, name=name, serie=serie.group(1) if serie else "",
              form="abschnitte", fehler=[], abschnitte=[], schritte=[])
    for z in block.splitlines():
        m = re.match(r"^(Titel|Formel|In Worten|Vorgehen|Achtung|Bild|"
                     r"Tisch|Fehler|Blatt|Stand): (.+)$", z)
        if m and m.group(1) == "Fehler":
            lw["fehler"].append(m.group(2).strip())
        elif m and m.group(1) == "Blatt":
            teile = [t.strip() for t in m.group(2).split("·")]
            lw["niveau"] = teile[0]
            for t in teile[1:]:
                k, _, v = t.partition(":")
                lw[k.strip().lower()] = v.strip()
        elif m and m.group(1) == "Stand":
            k = re.search(r"Kennung (\w+)", m.group(2))
            if k and k.group(1) not in ("–", "-"):
                lw["kennung"] = k.group(1)
        elif m and m.group(1) == "Titel":
            lw["titel_blatt"] = m.group(2).strip()
        elif m:
            lw[m.group(1).lower().replace(" ", "_")] = m.group(2).strip()
        elif z.startswith(f"| {praefix}"):
            c = [x.strip() for x in z.strip().strip("|").split("|")]
            leer = lambda s: "" if s in ("–", "-") else s  # noqa: E731
            ids = lambda s: [i for i in re.split(r"[,\s]+", leer(s)) if i]  # noqa: E731,E501
            lw["abschnitte"].append(dict(
                id=c[0], buchstabe=c[0][len(praefix):], name=c[1],
                satz=leer(c[2]), formel=leer(c[3]), beispiel=leer(c[4]),
                aufgaben=ids(c[5]), vorrat=ids(c[6]) if len(c) > 6 else []))
    if not lw["abschnitte"]:
        sys.exit(f"Block in Abschnittsform ohne Zeilen {praefix}…")
    return lw


def lies_bank(eintrag):
    zeilen = {}
    for datei in sorted((WURZEL / "bank" / eintrag).glob("e*.jsonl")):
        for z in datei.read_text(encoding="utf-8").splitlines():
            if z.strip():
                a = json.loads(z)
                zeilen[a["id"]] = a
    return zeilen


def register_zeilen():
    with REGISTER.open(encoding="utf-8") as f:
        return list(csv.reader(f, delimiter=";"))


def neue_kennung():
    vergeben = {r[0] for r in register_zeilen()}
    while True:
        k = "".join(random.choice(ZEICHEN) for _ in range(3))
        if k not in vergeben:
            return k


def gruppen_aus_register(kennung):
    for r in register_zeilen():
        if r and r[0] == kennung:
            m = re.search(r"ids=([^;,]+)", r[4])
            if m:
                return [g.split("+") for g in m.group(1).split()]
    sys.exit(f"Kennung {kennung} nicht im Register oder ohne ids")


# --- Satz einer Nummer ---------------------------------------------------

def bilder(grafik):
    return re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
                      grafik, re.S)


def kreuzzeilen(zeilen, trenner):
    return trenner.join("".join(f"\\kk{{{o}}}" for o in z) for z in zeilen)


def loesung_aus_bank(nr, a):
    """[[Ergebnis, Weg]] aus dem Feld loesung, wenn satz keine trägt
    (bank.md „Felder für den Lernweg“, satz): je offenem Teil der Text
    hinter „a)“, „b)“ …; ohne Teile die ganze loesung."""
    offen = [i for i, t in enumerate(a["satz"].get("teile", []))
             if not t.get("grau")]
    if not offen:
        return [[a["loesung"], ""]]
    stuecke = dict(re.findall(r"(?:^|;\s*)([a-z])\)\s*(.*?)(?=;\s*[a-z]\)|$)",
                              a["loesung"]))
    fehlt = [BUCHST[i] for i in offen if BUCHST[i] not in stuecke]
    if fehlt:
        sys.exit(f"Nr. {nr}: {a['id']} ohne satz.loesung, und loesung "
                 f"nennt die Teile {fehlt} nicht")
    return [[stuecke[BUCHST[i]], ""] for i in offen]


def setze_nummer(nr, zeilen, schritt_kommentar):
    """zeilen: Bankzeilen einer Nummer (zweite und weitere mit folgt)."""
    s0 = zeilen[0]["satz"]
    form = s0["form"]
    text = s0.get("text") or zeilen[0]["aufgabe"]   # aufgabe ist Quelle
    teile, grafiken, fuss, loes = [], [], [], []
    for a in zeilen:
        s = a["satz"]
        teile += s.get("teile", [])
        grafiken += bilder(a.get("grafik", ""))
        lz = s.get("loesung") or loesung_aus_bank(nr, a)
        f = s.get("fuss", [e for e, _ in lz])
        fuss += f if isinstance(f, list) else [f]
        loes += lz
    for i, t in enumerate(teile):
        t["_b"] = BUCHST[i]
    offen = [t for t in teile if not t.get("grau")]    # Fuß und Lösung
    marken = [t["_b"] + ")" for t in offen] if offen else [""] * len(fuss)
    if len(marken) != len(fuss) or len(marken) != len(loes):
        sys.exit(f"Nr. {nr}: Teile/fuss/loesung passen nicht "
                 f"({len(marken)}/{len(fuss)}/{len(loes)})")
    out = [f"% {schritt_kommentar}",
           f"\\begin{{pfaufg}}{{{s0.get('marke', '')}}}{{{nr}.}}{{}}"]

    if form == "zwei":
        rechts = []
        if teile:
            rechts.append("\\par\\bigskip\n".join(
                f"\\textbf{{{t['_b']})}}\\ {t['text']}"
                f"\\linie{{14mm}}{t.get('luecke', '')}" for t in teile))
        if s0.get("karo"):
            rechts.append(f"\\karo{{{s0['karo']}}}")
        if s0.get("kreuz"):
            k = kreuzzeilen(s0["kreuz"], "\\par\\medskip\n")
            rechts.append(f"\\par\\smallskip\\hfill{k}" if s0.get("karo")
                          else k)
        out.append(text)
        out.append(f"\\gzwei{{{grafiken[0]}}}{{%\n" + "".join(rechts) + "}")
    elif form == "reihe":
        breite = {2: "0.48", 3: "0.32", 4: "0.245"}[len(teile)]
        spalten = []
        for t, g in zip(teile, grafiken):
            if t.get("kreuz"):
                inhalt = (f"{{\\small {t['_b']})\\ "
                          + kreuzzeilen(t["kreuz"], "\\par\\hspace*{1.1em}")
                          + "}")
            else:
                kopf = f"{{\\small {t['_b']})\\ {t['text']}}}\\par\\smallskip\n"
                if t.get("grau"):
                    inhalt = ("\\grau{" + kopf
                              + "\\par\\smallskip ".join(t["zeilen"]) + "}")
                else:
                    inhalt = kopf + "\\par\\medskip".join(
                        ["\\linie{30mm}"] * t.get("linien", 1))
            spalten.append(f"\\begin{{minipage}}[b]{{{breite}\\linewidth}}"
                           f"\\centering\n{g}\\par\\smallskip\n{inhalt}\n"
                           "\\end{minipage}")
        out.append(text + "\\par\\medskip\\noindent")
        out.append("\\hfill\n".join(spalten))
    elif form == "paeckchen":
        if text:
            out.append(text + "\\par\\medskip" if teile[0].get("grau")
                       else text + "\\par\\smallskip")
        for t in [t for t in teile if t.get("grau")]:
            out.append(f"\\grau{{{t['_b']})\\ {t['text']}\\quad "
                       + "\\quad ".join(t["zeilen"]) + "}\\par\\medskip")
        karos = [t for t in teile if not t.get("grau")]
        for i in range(0, len(karos), 2):
            paar = [f"\\begin{{minipage}}[t]{{0.48\\linewidth}}\n"
                    f"{t['_b']})\\ {t['text']}\n\\karo{{{t.get('karo', 3)}}}"
                    "\n\\end{minipage}" for t in karos[i:i + 2]]
            out.append("\\noindent" + "\\hfill\n".join(paar))
        nach = next((a["satz"]["nach"] for a in reversed(zeilen)
                     if a["satz"].get("nach")), None)
        if nach:
            out.append(f"\\par {nach}")
    elif form == "frei":
        out.append(text + "\\par")
        if s0.get("nach"):
            out.append(s0["nach"])
        if s0.get("karo"):
            out.append(f"\\karo{{{s0['karo']}}}")
    else:
        sys.exit(f"Nr. {nr}: satz.form {form!r} unbekannt")

    fz = "; ".join(f"{m} {f}".strip() for m, f in zip(marken, fuss))
    out.append(f"\\fusshilfe{{\\mbox{{{nr}:~{fz}}}}}")
    out.append("\\end{pfaufg}")

    lz = []
    for i, (m, (erg, weg)) in enumerate(zip(marken, loes)):
        marke = (f"{nr}{m}" if m else f"{nr}.") if i == 0 else m
        lz.append(f"\\lz{{{marke}}}{{{erg}}}{{{weg}}}{{}}")
    loesung = "\\begin{pfloesung}{}\n" + "\n".join(lz) + "\n\\end{pfloesung}"
    return "\n".join(out), loesung


# --- Abschnittsform (bau/bauauftrag.md 10.10.2026) -----------------------

def optionen(text):
    """Kopf und Optionen \\kreuz{…} eines Ankreuzauftrags (Klammern
    gezählt)."""
    aus, i = [], text.find("\\kreuz{")
    kopf = text if i < 0 else text[:i].rstrip()
    while i >= 0:
        j, tiefe = i + 7, 1
        while tiefe:
            tiefe += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        aus.append(text[i + 7:j - 1])
        i = text.find("\\kreuz{", j)
    return kopf, aus


def lang(opts):
    return any(len(re.sub(r"\\[a-z]+|[${}]", "", o)) > 40 for o in opts)


def kurz(ergebnis):
    """Ergebnis für den Fuß: kurz, sonst bis zum ersten „:“ oder „.“."""
    if len(ergebnis) <= 45:
        return ergebnis
    return re.split(r":\s|\.\s|;\s", ergebnis, maxsplit=1)[0]


def weg(a):
    """loesung für die Lösungsseite; beginnt sie mit der gewählten
    Ankreuzoption (bank-pruef), fällt die Option weg."""
    _, opts = optionen(a["aufgabe"])
    for o in sorted(opts, key=len, reverse=True):
        if a["loesung"].startswith(o):
            return a["loesung"][len(o):].lstrip(" :")
    return a["loesung"]


def gruppen_abschnitte(lw):
    """Nummern für tisch-alt: Beispiel + erste Aufgabe, dann je eine."""
    gruppen, von = [], {}
    for ab in lw["abschnitte"]:
        for k, i in enumerate(ab["aufgaben"]):
            g = [ab["beispiel"], i] if k == 0 and ab["beispiel"] else [i]
            gruppen.append(g)
            for x in g:
                von[x] = f"{ab['id']}: {ab['name']}"
    return gruppen, von


def setze_nummer_neu(nr, zeilen, kommentar):
    """Nummer aus Bankzeilen ohne satz (tisch-alt): ein Beispiel wird
    grau vorgerechnetes a), die Aufgabe b) mit Karo."""
    bsp = [a for a in zeilen if a.get("rolle") == "beispiel"]
    auf = [a for a in zeilen if a.get("rolle") != "beispiel"]
    out = [f"% {kommentar}", f"\\begin{{pfaufg}}{{}}{{{nr}.}}{{}}"]
    marke = ""
    if bsp:
        b = bsp[0]
        grau = ("\\grau{a)\\ " + b["aufgabe"] + "\\par\\smallskip "
                + "\\par ".join(b.get("schritte", [])) + "}")
        g = bilder(b.get("grafik", ""))
        out.append(f"\\gzwei{{{g[0]}}}{{{grau}}}" if g else grau)
        out.append("\\par\\medskip")
        marke = "b)"
    fuss, lz = [], []
    for a in auf:
        kopf, opts = optionen(a["aufgabe"])
        rechts = (f"{marke}\\ " if marke else "") + kopf
        if opts:
            if lang(opts):
                rechts += "".join(f"\\pfkreuzzeile{{{o}}}" for o in opts)
            else:
                rechts += "\\par\\smallskip " + "\\par ".join(
                    "".join(f"\\gkreuz{{{o}}}" for o in opts[i:i + 2])
                    for i in range(0, len(opts), 2))
        else:
            rechts += "\\karo{3}"
        g = bilder(a.get("grafik", ""))
        out.append(f"\\gzwei{{{g[0]}}}{{%\n{rechts}}}" if g else rechts)
        fuss.append(f"{marke} {kurz(a.get('ergebnis', a['loesung']))}"
                    .strip())
        lz.append(f"\\lz{{{nr}{marke or '.'}}}{{{a.get('ergebnis', '')}}}"
                  f"{{{weg(a)}}}{{}}")
    out.append(f"\\fusshilfe{{\\mbox{{{nr}:~{'; '.join(fuss)}}}}}")
    out.append("\\end{pfaufg}")
    return ("\n".join(out),
            "\\begin{pfloesung}{}\n" + "\n".join(lz) + "\n\\end{pfloesung}")


PRAEAMBEL_NEU = r"""\documentclass[11pt]{article}
\usepackage{mathblatt}
%% gesetzt von werkzeuge/setzer.py (Sorte %(sorte)s) aus dem Lernweg %(kennung)s
%% und den Bankzeilen; Muster bau/proben/2026-10-09/hypotenuse-muster.
\usepackage{enumitem}
\newgeometry{a4paper,margin=18mm,top=15mm,bottom=20mm,footskip=9mm}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\footnotesize\color{mbgrau}%(fuss)s}
\fancyfoot[R]{\footnotesize\color{mbgrau}\thepage}
\setlength{\parskip}{3pt}
\renewcommand{\kreuz}[1]{\mbox{$\square$\ #1}\quad}
\newcommand{\kreuzl}[1]{\par\hangindent1.4em\hangafter1\noindent$\square$\ #1}
\newcommand{\aufg}[3]{\par\noindent\makebox[0pt][r]{#3}\begin{minipage}[t]{\linewidth}#1\end{minipage}\par}
\newcommand{\aufgg}[4]{\par\noindent\makebox[0pt][r]{#4}\begin{minipage}[t]{0.6\linewidth}\vspace{0pt}#1\end{minipage}\hfill
  \begin{minipage}[t]{0.37\linewidth}\vspace{0pt}\centering #2\end{minipage}\par}
\newcommand{\nr}[1]{\makebox[7mm][l]{\textbf{#1}}}
\newcommand{\lsg}[3]{\par\noindent\begin{minipage}[t]{9mm}\textbf{#1}\end{minipage}%%
  \begin{minipage}[t]{52mm}\raggedright\bfseries\boldmath #2\end{minipage}\hspace{3mm}%%
  \begin{minipage}[t]{\dimexpr\linewidth-64mm\relax}\raggedright\small #3\end{minipage}\par\vspace{4pt}}
\newlength{\kr}
\begin{document}
"""
ZIEL = "{\\scriptsize\\color{mbgrau}Ziel\\hspace{2mm}}"
KARO_REST = (
    "\\par\\vspace{3mm}\\setlength{\\kr}{\\dimexpr\\pagegoal-\\pagetotal-10mm"
    "\\relax}%\n\\ifdim\\kr>12mm\\noindent{\\scriptsize\\color{mbgrau}Platz "
    "zum Rechnen}\\par\\nointerlineskip\\vspace{1mm}\\noindent\n"
    "\\begin{tikzpicture}\\clip (0,0) rectangle ({\\linewidth-0.5mm},\\kr);"
    "\\draw[black!16,line width=0.3pt,step=5mm] (0,0) grid (\\linewidth,"
    "\\kr);\\end{tikzpicture}\\fi\\par")


def praeambel(sorte, kennung, fuss):
    return PRAEAMBEL_NEU % dict(sorte=sorte, kennung=kennung, fuss=fuss)


def aufgabe_tex(a, nummer):
    """Eine Aufgabe als \\aufg / \\aufgg (Prüfstein-Satz)."""
    kopf, opts = optionen(a["aufgabe"])
    text = kopf
    if opts:
        if lang(opts):
            text += "\\par\\smallskip\\leftskip7mm " + "".join(
                f"\\kreuzl{{{o}}}" for o in opts)
        else:
            text += "\\par\\smallskip\\leftskip7mm " + "\\par".join(
                "\\ ".join(f"\\kreuz{{{o}}}" for o in opts[i:i + 2])
                for i in range(0, len(opts), 2))
    links = f"\\hangindent7mm\\hangafter1\\nr{{{nummer}}}{text}"
    ziel = ZIEL if a.get("rolle") == "ziel" else ""
    g = bilder(a.get("grafik", ""))
    if g:
        return f"\\aufgg{{{links}}}{{{g[0]}}}{{}}{{{ziel}}}\n\\medskip"
    return f"\\aufg{{{links}}}{{}}{{{ziel}}}\n\\medskip"


def zeilen_von(ab, bank):
    fehlt = [i for i in ab["aufgaben"] + ([ab["beispiel"]] if ab["beispiel"]
                                          else []) if i not in bank]
    if fehlt:
        sys.exit(f"{ab['id']}: Bankzeile fehlt: {fehlt}")
    schwach = [i for i in ab["aufgaben"]
               if bank[i].get("status") in ("schwach", "ruht")]
    if schwach:
        sys.exit(f"{ab['id']}: schwach/ruht auf dem Blatt: {schwach}")
    return [bank[i] for i in ab["aufgaben"]]


def titel_von(lw):
    return lw.get("titel_blatt") or \
        f"{lw['titel']}: {lw['name']}"


def tex_tisch(lw, kennung, bank):
    titel = titel_von(lw)
    t = [praeambel("tisch", kennung,
                   f"{kennung} \\textperiodcentered{{}} {titel} "
                   "\\textperiodcentered{} Tischblatt"),
         f"\\noindent{{\\Large\\bfseries {titel}}}\\hfill{{\\small Name: "
         "\\rule{40mm}{0.4pt}}\\par\\smallskip",
         "\\noindent{\\small\\color{mbgrau}Rechne auf einem extra Blatt. "
         + (lw.get("tisch", "") + " " if lw.get("tisch") else "")
         + "\\emph{Ziel} = Aufgabe am Ende eines Abschnitts.}"
         "\\par\\medskip"]
    for ab in lw["abschnitte"]:
        t.append("\\par\\Needspace{25mm}\\noindent\\colorbox{black!12}{"
                 f"\\makebox[7mm]{{\\bfseries\\strut {ab['buchstabe']}}}}}"
                 f"\\hspace{{2mm}}{{\\bfseries {ab['name']}}}\\par\\smallskip")
        for k, a in enumerate(zeilen_von(ab, bank), 1):
            t.append(aufgabe_tex(a, f"{ab['buchstabe']}{k}"))
    return "\n".join(t) + "\n\\end{document}\n"


def tex_selbst(lw, kennung, bank):
    titel = titel_von(lw)
    b0 = lw["abschnitte"][1]["buchstabe"] if len(lw["abschnitte"]) > 1 \
        else lw["abschnitte"][0]["buchstabe"]
    t = [praeambel("selbst", kennung,
                   f"{kennung} \\textperiodcentered{{}} {titel}"),
         f"\\noindent{{\\LARGE\\bfseries {titel}}}\\par\\smallskip",
         "\\noindent{\\small\\color{mbgrau}Selbstlernheft "
         f"{lw.get('niveau', '')} \\textperiodcentered{{}} mit Lösungsheft "
         f"\\textperiodcentered{{}} Kennung {kennung}}}\\par\\medskip",
         "\\noindent\\textbf{So nutzt du das Heft:} Lies im Abschnitt das "
         "Beispiel. Rechne dann die Aufgaben der Reihe nach und vergleiche "
         "jede sofort mit dem Lösungsheft. Kreuze „kann ich“ an, wenn du die "
         "letzte Aufgabe (\\emph{Ziel}) allein schaffst.\\par",
         "\\noindent Mehr Aufgaben zu einem Abschnitt: Kennung deinem "
         f"Nachhilfelehrer schicken (z.\\,B. „{kennung} mehr {b0}“).\\par"
         "\\medskip",
         "{\\arrayrulecolor{mbgrau}\\renewcommand{\\arraystretch}{1.3}",
         "\\noindent\\begin{tabular}{|>{\\bfseries}p{10mm}|p{112mm}|"
         ">{\\raggedleft\\arraybackslash}p{10mm}|>{\\centering\\arraybackslash}"
         "p{14mm}|}\\hline",
         "\\rowcolor{black!8} & \\textbf{Abschnitt} & \\textbf{Seite} & "
         "\\textbf{kann ich}\\\\\\hline"]
    for ab in lw["abschnitte"]:
        t.append(f"{ab['buchstabe']} & {ab['name']} & \\pageref{{s:"
                 f"{ab['buchstabe']}}} & $\\square$\\\\\\hline")
    t.append("\\end{tabular}}\\par\\bigskip\n")
    if lw.get("formel"):
        links = [f"{{\\Large {lw['formel']}}}\\par\\medskip"]
        if lw.get("in_worten"):
            links.append(f"In Worten: {lw['in_worten']}\\par\\medskip")
        if lw.get("vorgehen"):
            links.append("\\textbf{So gehst du vor}\\par")
            links += [f"\\nr{{{i}}}{s.strip()}\\par" for i, s in
                      enumerate(lw["vorgehen"].split(";"), 1)]
            links.append("\\medskip")
        if lw.get("achtung"):
            links.append(f"{{\\small {lw['achtung']}}}")
        bild = bilder(bank.get(lw.get("bild", ""), {}).get("grafik", ""))
        box = ["\\begin{tcolorbox}[colback=mbkasten,colframe=mbgrau,"
               "boxrule=0.5pt,arc=1mm,left=3mm,right=3mm,top=2mm,bottom=2mm,"
               "title={\\bfseries Formel auf einen Blick},coltitle=black,"
               "colbacktitle=black!10]"]
        if bild:
            box += ["\\begin{minipage}[t]{0.58\\linewidth}\\vspace{0pt}"]
            box += links + ["\\end{minipage}\\hfill",
                            "\\begin{minipage}[t]{0.38\\linewidth}"
                            "\\vspace{2mm}\\centering", bild[0],
                            "\\end{minipage}"]
        else:
            box += links
        t += box + ["\\end{tcolorbox}"]
    if lw["fehler"]:
        t.append("\\medskip\\noindent\\textbf{Typische Fehler – so nicht}"
                 "\\par\\smallskip")
        t += [f"\\noindent\\nr{{$\\times$}}{f}\\par" for f in lw["fehler"]]
    for ab in lw["abschnitte"]:
        bu = ab["buchstabe"]
        t.append(f"\\clearpage\\label{{s:{bu}}}\\noindent\\colorbox{{black!12}}"
                 f"{{\\makebox[10mm]{{\\Large\\bfseries\\strut {bu}}}}}"
                 f"\\hspace{{3mm}}{{\\Large\\bfseries {ab['name']}}}"
                 "\\par\\smallskip")
        if ab["satz"]:
            t.append(f"\\noindent {ab['satz']}\\par\\medskip")
        if ab["formel"]:
            t.append("\\noindent\\textbf{Formel}\\par\\nopagebreak\\noindent"
                     "\\hspace*{4mm}\\begin{minipage}{\\dimexpr\\linewidth-4mm"
                     f"\\relax}}{ab['formel']}\\end{{minipage}}\\par\\medskip")
        if ab["beispiel"]:
            b = bank[ab["beispiel"]]
            t.append(f"\\noindent\\textbf{{Beispiel}}\\quad {b['aufgabe']}"
                     "\\par\\smallskip")
            schritte = "".join(
                "\\par\\noindent\\hangindent6mm\\hangafter1\\makebox[6mm][l]"
                f"{{\\textbf{{{i}}}}}{s}\\par\\smallskip"
                for i, s in enumerate(b.get("schritte", []), 1))
            g = bilder(b.get("grafik", ""))
            if g:
                t.append("\\noindent\\begin{minipage}[t]{0.6\\linewidth}"
                         f"\\vspace{{0pt}}{schritte}\\end{{minipage}}\\hfill")
                t.append("\\begin{minipage}[t]{0.37\\linewidth}\\vspace{0pt}"
                         f"\\centering {g[0]}\\end{{minipage}}\\par\\medskip")
            else:
                t.append(f"\\noindent{schritte}\\par\\medskip")
        t.append("\\noindent\\textbf{Aufgaben}\\hspace{1em}{\\small\\color"
                 "{mbgrau}Rechne unten im Karo. Vergleiche jede Aufgabe gleich "
                 "mit dem Lösungsheft.}\\par\\smallskip")
        for k, a in enumerate(zeilen_von(ab, bank), 1):
            t.append(aufgabe_tex(a, f"{k}."))
        t.append(KARO_REST)
    return "\n".join(t) + "\n\\end{document}\n"


def tex_loesungen_neu(lw, kennung, bank, sorte):
    titel = titel_von(lw)
    zusatz = " \\textperiodcentered{} Tischblatt" if sorte == "tisch" else ""
    t = [praeambel(sorte, kennung, f"{kennung} \\textperiodcentered{{}} "
                   f"Lösungen \\textperiodcentered{{}} {titel}{zusatz}"),
         "\\noindent{\\Large\\bfseries Lösungen}\\hspace{1em}{\\color{mbgrau}"
         f"{titel}}}\\par\\smallskip",
         "\\noindent{\\small Links das Ergebnis, rechts der Weg in kurzen "
         "Schritten. Stimmt dein Ergebnis nicht, such den ersten Schritt, der "
         "anders ist.}\\par"]
    for ab in lw["abschnitte"]:
        bu = ab["buchstabe"]
        t.append("\\par\\Needspace{25mm}\\vspace{6pt}\\noindent\\colorbox"
                 f"{{black!12}}{{\\makebox[7mm]{{\\bfseries\\strut {bu}}}}}"
                 f"\\hspace{{2mm}}{{\\bfseries {ab['name']}}}\\par\\vspace{{4pt}}")
        for k, a in enumerate(zeilen_von(ab, bank), 1):
            nummer = f"{bu}{k}" if sorte == "tisch" else f"{k}."
            t.append(f"\\lsg{{{nummer}}}{{{a.get('ergebnis', '')}}}"
                     f"{{{weg(a)}}}")
    return "\n".join(t) + "\n\\end{document}\n"


def register_neu(kennung, lw, eintrag, teil, gruppen, sorte):
    """Registerzeile für einen Lernweg in Abschnittsform (einmal je
    Kennung)."""
    if any(r and r[0] == kennung for r in register_zeilen()):
        return
    ids = " ".join("+".join(g) for g in gruppen)
    ab = lw["abschnitte"]
    einheit = re.match(r"\d+", teil).group()
    zeile = [kennung, datetime.date.today().isoformat(), eintrag, "L",
             f"lerneinheit={einheit} {lw['name']}, klasse="
             f"{lw.get('niveau', '').replace('Klasse ', '')}, form=abschnitte,"
             f" abschnitte={ab[0]['id']}..{ab[-1]['id']}, sorten=tisch-alt "
             f"tisch selbst, ids={ids}",
             subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                            cwd=WURZEL, capture_output=True,
                            text=True).stdout.strip(),
             "setzer.py", sty_version(),
             f"– (aus Lernweg gesetzt, zuerst als {sorte})"]
    with REGISTER.open("a", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter=";", lineterminator="\n").writerow(zeile)


# --- Dateien -------------------------------------------------------------

KOPF = "\\documentclass[11pt]{article}\n\\usepackage{mathblatt}\n"
FUSS_EINFACH = ("\\fancyfoot[C]{{\\footnotesize\\color{mbgrau}\\kennung"
                "\\hfill\\thepage}}")
FUSS_HILFE = ("\\fancyfoot[C]{\\parbox[t]{\\textwidth}{\\mbfhbox\\par"
              "\\vspace{1.5mm}{\\footnotesize\\color{mbgrau}{\\scriptsize "
              "\\kennung}\\hfill\\thepage}}}")


def tex_uebersicht(lw, kennung):
    zeilen = [KOPF + f"% gesetzt von werkzeuge/setzer.py; Übersicht nach "
              "bau/bauregeln.md „Übersicht und Serie“.",
              f"\\newcommand{{\\kennung}}{{{kennung}}}",
              "\\newcommand{\\bereich}[1]{\\par\\addvspace{14pt}\\noindent"
              "{\\large\\bfseries #1}\\par\\nobreak\\vspace{4pt}}",
              "\\newcommand{\\bl}[1]{\\par\\noindent #1\\par\\vspace{3pt}}",
              "\\newcommand{\\blrand}[1]{\\par\\noindent{\\color{mbgrau}#1}"
              "\\par\\vspace{3pt}}",
              "\\newcommand{\\blhier}[1]{\\par\\noindent\\llap{$\\blacktri"
              "angleright$\\hspace{0.5em}}\\textbf{#1}\\par\\vspace{3pt}}",
              "\\begin{document}", "\\pfheftstil", FUSS_EINFACH,
              f"\\pfheftkopf{{{lw['titel']}}}{{{lw.get('niveau', '')}}}"]
    for bereich in lw["serie"].split("|"):
        name, _, blaetter = bereich.strip().partition(":")
        zeilen.append(f"\n\\bereich{{{name.strip()}}}")
        for b in blaetter.split(";"):
            b = b.strip().replace("·", "\\textperiodcentered{}")
            if b.startswith("(") and b.endswith(")"):
                zeilen.append(f"\\blrand{{{b[1:-1]}}}")
            elif b == lw["name"]:
                zeilen.append(f"\\blhier{{{b}}}")
            else:
                zeilen.append(f"\\bl{{{b}}}")
    zeilen.append("\\end{document}\n")
    return "\n".join(zeilen)


def tex_blatt(lw, kennung, nummern):
    weg = " · ".join(s for s, _, _ in lw["schritte"])
    kopf = [KOPF + f"% gesetzt von werkzeuge/setzer.py aus dem Lernweg "
            f"({weg}) und den Bankzeilen; Muster T6B.",
            "\\input{praeambel}",
            f"\\newcommand{{\\kennung}}{{{kennung}}}",
            "\\newcommand{\\grau}[1]{{\\color{mbgrau}#1}}",
            "", "\\begin{document}", "\\pfheftstil", FUSS_HILFE,
            f"\\pfheftkopf{{{lw['name']}}}{{{lw.get('niveau', '')}}}", ""]
    # Lernblatt: keine Originalliste (die steht nur auf Prüfungsblättern).
    ende = ("\\par\\vfill\\noindent{\\footnotesize "
            f"Vorher: {lw.get('vorher', '–')}\\quad\\textbullet\\quad "
            f"Weiter: {lw.get('weiter', '–')}\\par}}")
    return "\n".join(kopf) + "\n\n".join(nummern) + "\n\n" + ende + \
        "\n\\end{document}\n"


def tex_loesungen(lw, kennung, loesungen):
    return "\n".join([
        KOPF + "% gesetzt von werkzeuge/setzer.py; Lösungen nach "
        "bau/bauregeln.md „Lösungen“.",
        f"\\newcommand{{\\kennung}}{{{kennung}}}",
        "\\begin{document}", "\\pfheftstil", FUSS_EINFACH,
        f"\\pfheftkopf{{{lw['name']}}}{{{lw.get('niveau', '')} "
        "\\textperiodcentered{} Lösungen}", ""] + loesungen
        + ["\\end{document}\n"])


def kompiliere(aus, name, laeufe=2):
    env = dict(os.environ, TEXINPUTS=f"{HIER}{os.pathsep}")
    for _ in range(laeufe):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode",
                            "-halt-on-error", name + ".tex"], cwd=aus,
                           env=env, capture_output=True, text=True,
                           errors="replace")
        if r.returncode != 0:
            fehler = [z for z in r.stdout.splitlines() if z.startswith("!")]
            return f"{name}: xelatex-Fehler {fehler[:3]}"
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("eintrag")
    ap.add_argument("teil", help="Lernweg-Teil, z. B. 2k für L2k-1 …")
    ap.add_argument("--aus", required=True)
    ap.add_argument("--sorte", default="tisch-alt",
                    choices=["tisch-alt", "tisch", "selbst"])
    ap.add_argument("--kennung")
    ap.add_argument("--katalog",
                    default=str(WURZEL.parent / "mathe-nachhilfe" / "katalog"))
    ap.add_argument("--kein-register", action="store_true")
    ap.add_argument("--ohne-pdf", action="store_true")
    arg = ap.parse_args()
    start = time.perf_counter()

    lw = lies_lernweg(Path(arg.katalog) / f"{arg.eintrag}.md", arg.teil,
                      arg.kennung)
    bank = lies_bank(arg.eintrag)
    abschnitte = lw.get("form") == "abschnitte"
    if arg.sorte != "tisch-alt" and not abschnitte:
        sys.exit(f"--sorte {arg.sorte} braucht einen Lernweg-Block in "
                 "Abschnittsform (Form: abschnitte)")
    schritt_von = {}
    gruppen = []
    if abschnitte:
        gruppen, schritt_von = gruppen_abschnitte(lw)
        lw["schritte"] = [(ab["id"], ab["name"], []) for ab in
                          lw["abschnitte"]]
        if arg.kennung and lw.get("kennung") not in (None, arg.kennung):
            sys.exit(f"Block trägt Kennung {lw['kennung']}, nicht "
                     f"{arg.kennung}")
    else:
        for schritt, begreift, gs in lw["schritte"]:
            for g in gs:
                gruppen.append(g)
                for i in g:
                    schritt_von[i] = f"{schritt}: {begreift}"
        if arg.kennung:
            gruppen = gruppen_aus_register(arg.kennung)
    neu = not arg.kennung and not abschnitte
    kennung = arg.kennung or lw.get("kennung") or neue_kennung()

    aus = Path(arg.aus)
    aus.mkdir(parents=True, exist_ok=True)
    if arg.sorte == "tisch-alt":
        nummern, loesungen = [], []
        for nr, g in enumerate(gruppen, 1):
            fehlt = [i for i in g if i not in bank]
            ohne = [i for i in g if i in bank and "satz" not in bank[i]
                    and "rolle" not in bank[i]]
            if fehlt or ohne:
                sys.exit(f"Nr. {nr}: Zeile fehlt oder ohne satz: "
                         f"{fehlt + ohne}")
            zeilen = [bank[i] for i in g]
            if "satz" in zeilen[0]:
                n, l = setze_nummer(nr, zeilen, schritt_von.get(g[0], g[0]))
            else:
                n, l = setze_nummer_neu(nr, zeilen,
                                        schritt_von.get(g[0], g[0]))
            nummern.append(n)
            loesungen.append(l)
        shutil.copy(HIER / "setzer-praeambel.tex", aus / "praeambel.tex")
        dateien = {"1-uebersicht": tex_uebersicht(lw, kennung),
                   "2-blatt": tex_blatt(lw, kennung, nummern),
                   "3-loesungen": tex_loesungen(lw, kennung, loesungen)}
        laeufe = {"1-uebersicht": 1, "2-blatt": 2, "3-loesungen": 1}
    else:
        blatt = (tex_tisch if arg.sorte == "tisch" else tex_selbst)(
            lw, kennung, bank)
        dateien = {"2-blatt": blatt,
                   "3-loesungen": tex_loesungen_neu(lw, kennung, bank,
                                                    arg.sorte)}
        laeufe = {"2-blatt": 2 if arg.sorte == "selbst" else 1,
                  "3-loesungen": 1}
    for name, inhalt in dateien.items():
        (aus / f"{name}.tex").write_text(inhalt, encoding="utf-8")

    fehler = []
    if not arg.ohne_pdf:
        sty = HIER / "mathblatt.sty"
        if not sty.exists():
            urllib.request.urlretrieve(STY_URL, sty)
        with cf.ThreadPoolExecutor(3) as pool:
            fehler = [f for f in pool.map(
                lambda n: kompiliere(aus, n, laeufe[n]), dateien) if f]
        for p in aus.iterdir():
            if p.suffix in (".aux", ".log", ".out", ".abh"):
                p.unlink()

    if abschnitte and not arg.kein_register and not fehler:
        register_neu(kennung, lw, arg.eintrag, arg.teil, gruppen, arg.sorte)
    if neu and not arg.kein_register and not fehler:
        ids = " ".join("+".join(g) for g in gruppen)
        schritte = lw["schritte"]
        einheit = re.match(r"\d+", arg.teil).group()
        zeile = [kennung, datetime.date.today().isoformat(), arg.eintrag, "L",
                 f"lerneinheit={einheit} {lw['name']}, klasse="
                 f"{lw.get('niveau', '').replace('Klasse ', '')}, schritte="
                 f"{schritte[0][0]}..{schritte[-1][0]}, ids={ids}",
                 subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                                cwd=WURZEL, capture_output=True,
                                text=True).stdout.strip(),
                 "setzer.py", sty_version(), "– (aus Lernweg gesetzt)"]
        with REGISTER.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f, delimiter=";", lineterminator="\n").writerow(zeile)

    dauer = time.perf_counter() - start
    for f in fehler:
        print(f)
    print(f"{kennung} ({arg.sorte}): {len(gruppen)} Nummern, {aus} – "
          f"{dauer:.1f} s")
    sys.exit(1 if fehler else 0)


def sty_version():
    sty = HIER / "mathblatt.sty"
    if sty.exists():
        m = re.search(r"Version (\S+)", sty.read_text(encoding="utf-8",
                                                      errors="replace")[:400])
        if m:
            return "Version " + m.group(1)
    return "–"


if __name__ == "__main__":
    main()

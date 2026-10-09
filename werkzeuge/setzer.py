#!/usr/bin/env python3
"""Setzer: ein Lernblatt ohne Modell aus Lernweg und Bankzeilen setzen.

    python3 werkzeuge/setzer.py <eintrag> <teil> --aus <ordner>
            [--kennung K] [--katalog DIR] [--kein-register] [--ohne-pdf]

Beispiel: python3 werkzeuge/setzer.py pythagoras 2k --aus /tmp/t6b

Liest den Lernweg-Block der Einheit („| L<teil>-<n> |“) aus
mathe-nachhilfe/katalog/<eintrag>.md (Vorlage katalog/_vorlage.md,
Abschnitt „Lernweg“) und die Bankzeilen bank/<eintrag>/e*.jsonl (Felder
aufgabe, loesung, grafik, satz; bank.md „Felder für den Lernweg“). Quelle
für Auftrag und Lösung sind aufgabe und loesung; satz.text, satz.loesung
und satz.fuss gelten nur, wo die Zeile sie trägt. Keine Originalliste auf
dem Lernblatt (die gehört nur auf Prüfungsblätter). Schreibt
1-uebersicht.tex, 2-blatt.tex, 3-loesungen.tex und praeambel.tex
(werkzeuge/setzer-praeambel.tex) nach <ordner> und kompiliert jede Datei
zweimal mit xelatex (Fußhilfe braucht den zweiten Lauf).

Kennung: neu nach bau/bauregeln.md „Kennung“ (drei Zeichen aus 2–9 und A–Z
ohne I und O, gegen bau/register.csv eindeutig) und eine Zeile ins Register
mit den gesetzten ids (Gruppen einer Nummer mit „+“). Mit --kennung K wird
ein Blatt aus dem Register wieder gesetzt: dieselben ids, kein neuer
Registereintrag.

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

def lies_lernweg(katalog, teil):
    """Kopf, Serie und Schritte des Lernweg-Blocks L<teil>."""
    text = katalog.read_text(encoding="utf-8")
    titel = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    serie = re.search(r"^Serie: (.+)$", text, re.M)
    praefix = f"L{teil}-"
    bloecke = re.split(r"^(?=#### )", text, flags=re.M)
    block = next((b for b in bloecke if b.startswith("####")
                  and f"| {praefix}" in b), None)
    if block is None:
        sys.exit(f"Kein Lernweg-Block mit Schritten {praefix}… in {katalog}")
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


def kompiliere(aus, name):
    env = dict(os.environ, TEXINPUTS=f"{HIER}{os.pathsep}")
    for _ in range(2):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode",
                            "-halt-on-error", name + ".tex"], cwd=aus,
                           env=env, capture_output=True, text=True,
                           errors="replace")
        if r.returncode != 0:
            fehler = [z for z in r.stdout.splitlines() if z.startswith("!")]
            return f"{name}: xelatex-Fehler {fehler[:3]}"
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("eintrag")
    ap.add_argument("teil", help="Lernweg-Teil, z. B. 2k für L2k-1 …")
    ap.add_argument("--aus", required=True)
    ap.add_argument("--kennung")
    ap.add_argument("--katalog",
                    default=str(WURZEL.parent / "mathe-nachhilfe" / "katalog"))
    ap.add_argument("--kein-register", action="store_true")
    ap.add_argument("--ohne-pdf", action="store_true")
    arg = ap.parse_args()
    start = time.perf_counter()

    lw = lies_lernweg(Path(arg.katalog) / f"{arg.eintrag}.md", arg.teil)
    bank = lies_bank(arg.eintrag)
    schritt_von = {}
    gruppen = []
    for schritt, begreift, gs in lw["schritte"]:
        for g in gs:
            gruppen.append(g)
            for i in g:
                schritt_von[i] = f"{schritt}: {begreift}"
    neu = not arg.kennung
    if arg.kennung:
        gruppen = gruppen_aus_register(arg.kennung)
    kennung = arg.kennung or neue_kennung()

    nummern, loesungen = [], []
    for nr, g in enumerate(gruppen, 1):
        fehlt = [i for i in g if i not in bank or "satz" not in bank[i]]
        if fehlt:
            sys.exit(f"Nr. {nr}: Zeile fehlt oder ohne satz: {fehlt}")
        zeilen = [bank[i] for i in g]
        n, l = setze_nummer(nr, zeilen, schritt_von.get(g[0], g[0]))
        nummern.append(n)
        loesungen.append(l)

    aus = Path(arg.aus)
    aus.mkdir(parents=True, exist_ok=True)
    shutil.copy(HIER / "setzer-praeambel.tex", aus / "praeambel.tex")
    dateien = {"1-uebersicht": tex_uebersicht(lw, kennung),
               "2-blatt": tex_blatt(lw, kennung, nummern),
               "3-loesungen": tex_loesungen(lw, kennung, loesungen)}
    for name, inhalt in dateien.items():
        (aus / f"{name}.tex").write_text(inhalt, encoding="utf-8")

    fehler = []
    if not arg.ohne_pdf:
        sty = HIER / "mathblatt.sty"
        if not sty.exists():
            urllib.request.urlretrieve(STY_URL, sty)
        with cf.ThreadPoolExecutor(3) as pool:
            fehler = [f for f in pool.map(lambda n: kompiliere(aus, n),
                                          dateien) if f]
        for p in aus.iterdir():
            if p.suffix in (".aux", ".log", ".out", ".abh"):
                p.unlink()

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
    print(f"{kennung}: {len(gruppen)} Nummern, {aus} – {dauer:.1f} s")
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

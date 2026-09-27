#!/usr/bin/env python3
"""Render-Probe: je Grafikbaustein aus mappen/_bausteine.md ein kleines
.tex mit bis zu fünf verschiedenen grafik-Feldern der Bank, mit xelatex
kompilieren, Fehler je Zeilen-id nach befunde.md.

Aufruf (Repo-Wurzel): python3 bau/render-probe/probe.py [--grenze 280]
Braucht xelatex im PATH und mathblatt.sty (Kopie aus bau/…/lernblatt).
"""
import argparse
import collections
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

WURZEL = pathlib.Path(__file__).resolve().parents[2]
HIER = WURZEL / "bau" / "render-probe"
AUS = HIER / "bausteine"
STY = WURZEL / "bau" / "prozentrechnung" / "2026-09-27" / "lernblatt" / "mathblatt.sty"

spec = importlib.util.spec_from_file_location(
    "bp", WURZEL / "werkzeuge" / "bank-pruef.py")
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

# Kein Baustein: Mathematik und die pgf-Variable \x.
KEIN_BAUSTEIN = {"x"}

KOPF = r"""\documentclass[11pt]{article}
\usepackage{mathblatt}
\begin{document}
\weit
"""


def grafik_bausteine():
    sig = bp.lade_bausteine(WURZEL / "mappen" / "_bausteine.md")
    namen = []
    for n in sig:
        if "\n" in n or "`" in n:
            continue                      # Parser-Rest aus dem Kopftext
        if n.startswith("begin:"):
            if n[6:] in bp.UMGEBUNG_STANDARD:
                continue
        elif n in bp.STANDARD or n in KEIN_BAUSTEIN:
            continue
        namen.append(n)
    return namen


def bank():
    zeilen = []
    for f in sorted((WURZEL / "bank").glob("*/*.jsonl")):
        for l in f.open(encoding="utf-8"):
            if l.strip():
                zeilen.append(json.loads(l))
    return zeilen


def auswahl(name, zeilen, n=5):
    """Bis zu n Zeilen mit verschiedenem grafik-Text, reihum über die
    Einträge verteilt."""
    je = collections.OrderedDict()
    for z in zeilen:
        g = z.get("grafik", "")
        if g and any(a == name for a, _ in bp.aufrufe(g)):
            je.setdefault(z["eintrag"], []).append(z)
    gesehen, aus = set(), []
    runde = 0
    while len(aus) < n and any(len(v) > runde for v in je.values()):
        for v in je.values():
            if len(v) > runde and v[runde]["grafik"] not in gesehen:
                gesehen.add(v[runde]["grafik"])
                aus.append(v[runde])
                if len(aus) == n:
                    break
        runde += 1
    treffer = sum(len(v) for v in je.values())
    return aus, treffer


def tex_datei(zeilen):
    teile = [KOPF]
    for z in zeilen:
        i = z["id"]
        teile.append(
            f"\\typeout{{PROBE-BEGIN {i}}}\n"
            f"\\begin{{aufgabe}}{{\\detokenize{{{i}}}}}\n"
            f"\\begin{{teile}}\n\\teil Probe\n\n{z['grafik']}\n"
            f"\\end{{teile}}\n\\end{{aufgabe}}\n"
            f"\\typeout{{PROBE-END {i}}}\n")
    teile.append("\\end{document}\n")
    return "".join(teile)


def kompiliere(stamm, arbeit):
    env = dict(os.environ, max_print_line="10000", error_line="254",
               half_error_line="238")
    try:
        r = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", f"{stamm}.tex"],
            cwd=arbeit, env=env, capture_output=True, timeout=180)
        rc = r.returncode
    except subprocess.TimeoutExpired:
        rc = "timeout"
    log = arbeit / f"{stamm}.log"
    text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    return rc, text


def auswerten(log, ids):
    """{id: [Befund]} und Menge der ids mit PROBE-END."""
    bef = collections.defaultdict(list)
    fertig = set()
    akt = None
    zeilen = log.splitlines()
    for k, l in enumerate(zeilen):
        m = re.match(r"PROBE-(BEGIN|END) (\S+)", l)
        if m:
            if m.group(1) == "BEGIN":
                akt = m.group(2)
            else:
                fertig.add(m.group(2))
                akt = None
            continue
        schluessel = akt or "(außerhalb)"
        if l.startswith("! "):
            ctx = " ".join(x.strip() for x in zeilen[k + 1:k + 3] if x.strip())
            bef[schluessel].append(f"Fehler: {l[2:].strip()} | {ctx[:200]}")
        elif l.startswith("Missing character"):
            bef[schluessel].append("Zeichen fehlt: " + l.strip())
        else:
            m = re.match(r"Overfull \\hbox \(([\d.]+)pt too wide\)", l)
            if m and float(m.group(1)) > 5:
                bef[schluessel].append(f"zu breit: {m.group(1)} pt")
    return bef, fertig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grenze", type=int, default=280)
    a = ap.parse_args()
    if not shutil.which("xelatex"):
        sys.exit("xelatex fehlt")
    AUS.mkdir(parents=True, exist_ok=True)
    shutil.copy(STY, AUS / "mathblatt.sty")
    zeilen = bank()
    namen = grafik_bausteine()
    laeufe = 0
    ergebnis = []          # (name, treffer, [ids], {id: befunde}, notiz)
    for name in namen:
        wahl, treffer = auswahl(name, zeilen)
        stamm = name.replace("begin:", "env-")
        if not wahl:
            ergebnis.append((name, 0, [], {}, "in keinem grafik-Feld"))
            continue
        offen = list(wahl)
        befunde, notiz, teil = {}, "", 0
        while offen:
            if laeufe >= a.grenze:
                notiz += f" Zählgrenze erreicht, {len(offen)} ungeprüft."
                for z in offen:
                    befunde[z["id"]] = ["ungeprüft (Zählgrenze)"]
                break
            s = stamm if teil == 0 else f"{stamm}-r{teil}"
            (AUS / f"{s}.tex").write_text(tex_datei(offen), encoding="utf-8")
            rc, log = kompiliere(s, AUS)
            laeufe += 1
            bef, fertig = auswerten(log, [z["id"] for z in offen])
            for z in offen:
                if z["id"] in fertig or bef.get(z["id"]):
                    befunde[z["id"]] = bef.get(z["id"], [])
            if bef.get("(außerhalb)"):
                notiz += " außerhalb: " + "; ".join(bef["(außerhalb)"][:3])
            rest = [z for z in offen if z["id"] not in befunde]
            if rc == "timeout":
                notiz += f" Lauf {s}: Zeitüberschreitung."
            if len(rest) == len(offen):
                # nichts erreicht: erste Zeile als Abbruchursache werten
                befunde[rest[0]["id"]] = [f"Abbruch (rc {rc}) vor PROBE-END"]
                rest = rest[1:]
            elif rest:
                # Lauf brach ab; letzte begonnene Zeile trägt die Schuld
                pass
            offen = rest
            teil += 1
        ergebnis.append((name, treffer, [z["id"] for z in wahl], befunde,
                         notiz.strip()))
        print(f"{name}: {sum(1 for v in befunde.values() if v)} von "
              f"{len(wahl)} mit Befund, Läufe gesamt {laeufe}", flush=True)
    (HIER / "ergebnis.json").write_text(
        json.dumps({"laeufe": laeufe, "ergebnis": ergebnis},
                   ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()

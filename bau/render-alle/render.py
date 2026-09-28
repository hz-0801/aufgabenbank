#!/usr/bin/env python3
"""render.py – Render-Lauf über alle Einträge unter bau/_alle/.

Kompiliert je Eintrag und Lauf (lernblatt, schwach) die Datei gesamt.tex
(dazu loesungen.tex als Zusatz) mit xelatex in einer Arbeitskopie außerhalb
des Repos, höchstens 3 Versuche je Datei (1. Lauf; 2. Lauf für Abhakseite
und Sprungziele; 3. Lauf nur, wenn die .log „Rerun“ verlangt). Je Versuch
werden die ersten Fehlerzeilen der .log nach logs/ gesichert. Danach prüft
pdfinfo/pdftotext Seitenzahl und Textgehalt.

Aufruf (aus der Wurzel des Repos aufgabenbank):

    python3 bau/render-alle/render.py [--arbeit <ordner>] [--nur <eintrag>]

Ergebnis: bau/render-alle/ergebnis.json (alle Messwerte, Fehlerstellen mit
Bankzeile-id) und bau/render-alle/logs/<eintrag>-<lauf>-<datei>.txt.
Der Bericht (bericht.md) wird aus ergebnis.json von bericht.py gebaut.
PDFs bleiben in der Arbeitskopie, nichts davon kommt ins Repo.
"""
import argparse
import difflib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
ALLE = WURZEL / "bau" / "_alle"
HIER = Path(__file__).resolve().parent
LOGS = HIER / "logs"
MAX_VERSUCHE = 3
ZEITGRENZE = 300  # Sekunden je xelatex-Aufruf
DATEIEN = ["gesamt.tex", "loesungen.tex"]

FEHLERZEILE = re.compile(r"^\./([\w.-]+\.tex):(\d+): (.*)$")
RERUN = re.compile(r"Rerun to get|Label\(s\) may have changed|rerun LaTeX", re.I)
FEHLENDES_ZEICHEN = re.compile(r"^Missing character: There is no (.) \(U\+([0-9A-F]+)\)")
UEBERBREIT = re.compile(r"^Overfull \\hbox \(([\d.]+)pt too wide\)")
TEIL_START = re.compile(r"^\\(teil|steil|tz|stz|swz|swa|swfrage|gl|sgl|erg)\b")
BEFEHL = re.compile(r"\\([A-Za-z]+)")
GERUEST = {"teil", "steil", "tz", "stz", "swz", "swa", "swfrage", "gl", "sgl",
           "erg", "leerfeld", "feld", "kreuz", "janein", "hfill", "text",
           "quad", "qquad", "frac", "cdot", "ldots", "begin", "end", "par",
           "rechenplatz", "teile", "aufgabe", "swz", "textbf", "emph",
           "verzeichniszeile", "verz", "verztrenn", "einheitenkopf",
           "zweigzeile", "blattkopf", "weit", "setcounter", "input",
           "clearpage", "mitzone", "def", "usepackage", "documentclass",
           "abhakauto", "verfahren", "merkkasten", "uebersichtskasten"}


def lade_bausteine():
    spec = importlib.util.spec_from_file_location(
        "bank_pruef", WURZEL / "werkzeuge" / "bank-pruef.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return set(modul.lade_bausteine(WURZEL / "mappen" / "_bausteine.md"))


def lies_bank(eintrag):
    zeilen = []
    for pfad in sorted((WURZEL / "bank" / eintrag).glob("*.jsonl")):
        with open(pfad, encoding="utf-8") as f:
            for nr, z in enumerate(f, 1):
                z = z.strip()
                if not z:
                    continue
                d = json.loads(z)
                d["_datei"] = f"bank/{eintrag}/{pfad.name}"
                d["_zeile"] = nr
                zeilen.append(d)
    return zeilen


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"\\[A-Za-z]+\*?|[{}$\\]", " ", s)).strip().lower()


def finde_bankzeile(bank, tex_zeilen, zeile_nr):
    """Bankzeile zu einer Fehlerstelle (datei, zeile): erst wörtlich
    (die Fehlerzeile als Teil eines Feldes), dann Ähnlichkeit des Teil-
    aufgabentexts mit aufgabe/loesung."""
    i = zeile_nr - 1
    if i < 0 or i >= len(tex_zeilen):
        return None, "außerhalb"
    zeile = tex_zeilen[i].strip()
    # 1. wörtlich: die Zeile steht in grafik/loesungsgrafik/aufgabe/loesung
    if len(zeile) >= 12:
        treffer = [b for b in bank
                   if any(zeile in (b.get(f) or "") for f in
                          ("grafik", "loesungsgrafik", "aufgabe", "loesung"))]
        if len(treffer) == 1:
            return treffer[0], "wörtlich"
        if len(treffer) > 1:
            # mehrere: nimm die, deren Text am ehesten der Teilaufgabe entspricht
            bank = treffer
    # 2. Teilaufgabe suchen (rückwärts bis \teil o. ä.)
    j = i
    while j >= 0 and not TEIL_START.match(tex_zeilen[j]):
        if tex_zeilen[j].startswith("\\begin{aufgabe}") or tex_zeilen[j].startswith("\\erg{"):
            break
        j -= 1
    if j < 0:
        j = i
    block = " ".join(tex_zeilen[j:i + 1])
    kandidat = norm(block)
    if not kandidat:
        return None, "leer"
    best, wert = None, 0.0
    for b in bank:
        for f in ("aufgabe", "loesung"):
            t = norm(b.get(f) or "")
            if not t:
                continue
            if t in kandidat and len(t) >= 8:
                r = 0.95 + min(len(t), 200) / 4000
            else:
                r = difflib.SequenceMatcher(None, kandidat[:300], t[:300]).ratio()
            if r > wert:
                best, wert = b, r
    if best is None or wert < 0.45:
        return None, f"unsicher ({wert:.2f})"
    return best, f"ähnlich ({wert:.2f})"


def bausteine_in(text, bausteine):
    aus = []
    for m in BEFEHL.finditer(text):
        n = m.group(1)
        if n in bausteine and n not in GERUEST and n not in aus:
            aus.append(n)
    m = re.search(r"\\begin\{(\w+)\}", text)
    if m and ("begin:" + m.group(1)) in bausteine and \
            m.group(1) not in ("aufgabe", "teile", "teilezwei"):
        aus.insert(0, "begin{" + m.group(1) + "}")
    return aus


def baustein_der_stelle(tex_zeilen, zeile_nr, bausteine):
    i = zeile_nr - 1
    if i < 0 or i >= len(tex_zeilen):
        return ""
    direkt = bausteine_in(tex_zeilen[i], bausteine)
    if direkt:
        return "\\" + direkt[0]
    j = i
    while j >= 0 and not TEIL_START.match(tex_zeilen[j]) and \
            not tex_zeilen[j].startswith("\\begin{aufgabe}"):
        j -= 1
    block = "\n".join(tex_zeilen[max(j, 0):i + 1])
    im_block = bausteine_in(block, bausteine)
    if im_block:
        return "\\" + im_block[0]
    m = TEIL_START.match(tex_zeilen[j]) if j >= 0 else None
    return "\\" + m.group(1) if m else "(Rahmen)"


def xelatex(arbeit, datei):
    try:
        p = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-file-line-error",
             "-no-shell-escape", datei],
            cwd=arbeit, capture_output=True, text=True, errors="replace",
            timeout=ZEITGRENZE)
        return p.returncode, False
    except subprocess.TimeoutExpired:
        return -1, True


def lies_log(arbeit, datei):
    pfad = arbeit / (Path(datei).stem + ".log")
    if not pfad.exists():
        return []
    with open(pfad, encoding="utf-8", errors="replace") as f:
        return f.read().split("\n")


def werte_log(log):
    """Fehlerstellen (datei, zeile, meldung) in Logreihenfolge, Warnungen."""
    stellen = []
    fehlend = Counter()
    ueberbreit = 0
    mathblatt_warn = 0
    fatal = False
    rerun = False
    for i, z in enumerate(log):
        m = FEHLERZEILE.match(z)
        if m:
            stellen.append((m.group(1), int(m.group(2)), m.group(3).strip(), i))
            continue
        if z.startswith("! "):
            stellen.append(("(ohne Datei)", 0, z[2:].strip(), i))
            continue
        m = FEHLENDES_ZEICHEN.match(z)
        if m:
            fehlend[f"{m.group(1)} (U+{m.group(2)})"] += 1
            continue
        m = UEBERBREIT.match(z)
        if m and float(m.group(1)) > 5:
            ueberbreit += 1
            continue
        if "Package mathblatt Warning" in z:
            mathblatt_warn += 1
        if "Fatal error occurred" in z or "Emergency stop" in z or \
                "TeX capacity exceeded" in z:
            fatal = True
        if RERUN.search(z):
            rerun = True
    return stellen, fehlend, ueberbreit, mathblatt_warn, fatal, rerun


def pdf_mass(arbeit, datei):
    pdf = arbeit / (Path(datei).stem + ".pdf")
    if not pdf.exists():
        return None, 0
    seiten = None
    p = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
    m = re.search(r"^Pages:\s+(\d+)", p.stdout, re.M)
    if m:
        seiten = int(m.group(1))
    p = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                       capture_output=True, text=True, errors="replace")
    zeichen = len(re.sub(r"\s+", "", p.stdout))
    return seiten, zeichen


def sichere_log(eintrag, lauf, datei, versuch, log, stellen, n=60):
    LOGS.mkdir(parents=True, exist_ok=True)
    ziel = LOGS / f"{eintrag}-{lauf}-{Path(datei).stem}.txt"
    modus = "a" if versuch > 1 else "w"
    with open(ziel, modus, encoding="utf-8") as f:
        f.write(f"=== Versuch {versuch}: xelatex {datei} "
                f"({len(stellen)} Fehlerzeilen in der .log) ===\n")
        gezeigt = 0
        for (d, zl, msg, idx) in stellen:
            if gezeigt >= n:
                f.write(f"... weitere {len(stellen) - n} Fehlerzeilen "
                        "nicht gesichert\n")
                break
            f.write(f"{d}:{zl}: {msg}\n")
            for k in range(idx + 1, min(idx + 4, len(log))):
                if log[k].strip():
                    f.write("    " + log[k].rstrip() + "\n")
            gezeigt += 1
        if not stellen:
            f.write("keine Fehlerzeilen\n")
        f.write("\n")


def lauf(eintrag, laufname, arbeitswurzel, bausteine, bank):
    quelle = ALLE / eintrag / laufname
    arbeit = arbeitswurzel / eintrag / laufname
    if arbeit.exists():
        shutil.rmtree(arbeit)
    shutil.copytree(quelle, arbeit)
    ergebnis = {}
    for datei in DATEIEN:
        if not (quelle / datei).exists():
            ergebnis[datei] = {"vorhanden": False}
            continue
        e = {"vorhanden": True, "versuche": []}
        stellen = []
        for versuch in range(1, MAX_VERSUCHE + 1):
            rc, zeitueberschreitung = xelatex(arbeit, datei)
            log = lies_log(arbeit, datei)
            stellen, fehlend, ueberbreit, mb_warn, fatal, rerun = werte_log(log)
            sichere_log(eintrag, laufname, datei, versuch, log, stellen)
            e["versuche"].append({"rc": rc, "zeit": zeitueberschreitung,
                                  "fehlerzeilen": len(stellen), "fatal": fatal,
                                  "rerun": rerun})
            if zeitueberschreitung or fatal:
                break
            if versuch == 1:
                continue  # zweiter Lauf immer (Abhakseite, Sprungziele)
            if not rerun:
                break
        seiten, zeichen = pdf_mass(arbeit, datei)
        # Fehlerstellen: je (datei, zeile) die erste Meldung, in Logreihenfolge
        gesehen = {}
        for d, zl, msg, _ in stellen:
            if (d, zl) not in gesehen:
                gesehen[(d, zl)] = msg
        fehler = []
        tex_cache = {}
        for (d, zl), msg in gesehen.items():
            if d not in tex_cache:
                p = arbeit / d
                tex_cache[d] = p.read_text(encoding="utf-8").split("\n") \
                    if p.exists() else []
            tz = tex_cache[d]
            b, art = finde_bankzeile(bank, tz, zl) if zl else (None, "ohne Zeile")
            fehler.append({
                "datei": d, "zeile": zl, "meldung": msg,
                "baustein": baustein_der_stelle(tz, zl, bausteine) if zl else "",
                "zeilentext": tz[zl - 1].strip()[:160] if 0 < zl <= len(tz) else "",
                "id": b["id"] if b else None,
                "bankdatei": f"{b['_datei']}:{b['_zeile']}" if b else None,
                "zuordnung": art,
            })
        e.update({
            "kompiliert": bool(seiten) and not fehler,
            "pdf": bool(seiten), "seiten": seiten, "zeichen": zeichen,
            "fehlerstellen": len(fehler), "fehlerzeilen_log": len(stellen),
            "fehler": fehler,
            "fehlende_zeichen": dict(fehlend), "ueberbreit": ueberbreit,
            "mathblatt_warnungen": mb_warn,
        })
        ergebnis[datei] = e
        print(f"  {laufname}/{datei}: {'ok' if e['kompiliert'] else 'FEHLER'} "
              f"Seiten={seiten} Fehlerstellen={len(fehler)} "
              f"Versuche={len(e['versuche'])}", flush=True)
    return ergebnis


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--arbeit", default=os.environ.get("RENDER_ARBEIT", "/tmp/render-alle"))
    ap.add_argument("--nur", default=None)
    args = ap.parse_args(argv)
    arbeitswurzel = Path(args.arbeit)
    arbeitswurzel.mkdir(parents=True, exist_ok=True)
    bausteine = lade_bausteine()
    eintraege = sorted(p.name for p in ALLE.iterdir() if p.is_dir())
    if args.nur:
        eintraege = [e for e in eintraege if e == args.nur]
    if LOGS.exists() and not args.nur:
        shutil.rmtree(LOGS)
    ergebnis = {"xelatex": subprocess.run(["xelatex", "--version"],
                                          capture_output=True, text=True).stdout.split("\n")[0],
                "eintraege": {}}
    for eintrag in eintraege:
        print(eintrag, flush=True)
        bank = lies_bank(eintrag)
        ergebnis["eintraege"][eintrag] = {}
        for laufname in ("lernblatt", "schwach"):
            if not (ALLE / eintrag / laufname / "gesamt.tex").exists():
                continue
            ergebnis["eintraege"][eintrag][laufname] = lauf(
                eintrag, laufname, arbeitswurzel, bausteine, bank)
        with open(HIER / "ergebnis.json", "w", encoding="utf-8") as f:
            json.dump(ergebnis, f, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())

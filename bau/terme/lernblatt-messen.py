#!/usr/bin/env python3
"""Messlauf für ein Lernblatt aus zusammenbau.py (v0.9).

Aufruf aus der Repo-Wurzel:
    python3 bau/terme/lernblatt-messen.py bau/terme/TER-L4

Kompiliert <K>-gesamt, <K>, <K>-blatt0, <K>-loesungen und je Einheit
<K>-e<n> je zweimal mit xelatex (-interaction=nonstopmode
-file-line-error), zählt je Dokument Seiten, Fehler (erste Meldung je
Datei und Zeile), „Missing character“, Overfull-Boxen, prüft den
PDF-Text (pdftotext: nicht leer, kein „TODO“, kein Bank-Wort nach
BANKWORT aus zusammenbau.py), setzt PNG je Seite des Gesamt
(pdftoppm -r 80) und schreibt die Messwerte in bau.json (Feld
messwerte und die Kurzfelder seiten, seiten_loesungen,
fehlende_zeichen, overfull, bankwort, hauptnummern_je_einheit,
teilaufgaben_je_einheit). Hilfsdateien (.aux, .out, .abh, .log der
Läufe) werden danach gelöscht.
"""

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "zusammenbau", WURZEL / "werkzeuge" / "zusammenbau.py")
ZB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ZB)


def lauf(ordner, name, n=2):
    for _ in range(n):
        subprocess.run(["xelatex", "-interaction=nonstopmode",
                        "-file-line-error", f"{name}.tex"], cwd=ordner,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = (ordner / f"{name}.log").read_text(encoding="utf-8",
                                             errors="replace")
    fehler = sorted({m.group(1) for m in re.finditer(
        r"^(\./[^:\n]+:\d+):", log, re.M)})
    if not fehler:
        fehler = [z for z in log.splitlines() if z.startswith("! ")][:5]
    pdf = ordner / f"{name}.pdf"
    seiten = 0
    text = ""
    if pdf.exists():
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                              text=True).stdout
        m = re.search(r"^Pages:\s+(\d+)", info, re.M)
        seiten = int(m.group(1)) if m else 0
        text = subprocess.run(["pdftotext", str(pdf), "-"],
                              capture_output=True, text=True).stdout
    bank = sorted({m.group(0) for m in ZB.BANKWORT.finditer(text)})
    return {
        "seiten": seiten,
        "fehler": fehler,
        "fehlende_zeichen": log.count("Missing character"),
        "overfull": log.count("Overfull"),
        "text_zeichen": len(text.strip()),
        "todo_im_pdf": text.count("TODO"),
        "bankwort_im_pdf": bank,
    }


def main(ordner):
    ordner = Path(ordner)
    bau = json.loads((ordner / "bau.json").read_text(encoding="utf-8"))
    k = bau["kennung"]
    doks = [f"{k}-gesamt", k, f"{k}-blatt0", f"{k}-loesungen"]
    doks += sorted(p.stem for p in ordner.glob(f"{k}-e*.tex"))
    werte = {}
    for d in doks:
        if (ordner / f"{d}.tex").exists():
            werte[d] = lauf(ordner, d)
            print(d, werte[d])
    for p in ordner.glob(f"{k}-gesamt-*.png"):
        p.unlink()
    subprocess.run(["pdftoppm", "-r", "80", "-png", f"{k}-gesamt.pdf",
                    f"{k}-gesamt"], cwd=ordner)
    for muster in ("*.aux", "*.out", "*.abh", f"{k}*.log"):
        for p in ordner.glob(muster):
            p.unlink()
    je = bau.get("je_datei", {})
    bau["messwerte"] = werte
    bau["seiten"] = werte[f"{k}-gesamt"]["seiten"]
    bau["seiten_loesungen"] = werte[f"{k}-loesungen"]["seiten"]
    bau["seiten_je_einheit"] = {d[len(k) + 1:]: w["seiten"]
                                for d, w in werte.items()
                                if re.fullmatch(rf"{k}-e\d+", d)}
    bau["fehlende_zeichen"] = sum(w["fehlende_zeichen"] for w in werte.values())
    bau["overfull"] = sum(w["overfull"] for w in werte.values())
    bau["kompilierfehler"] = sum(len(w["fehler"]) for w in werte.values())
    bau["bankwort"] = sorted({b for w in werte.values()
                              for b in w["bankwort_im_pdf"]})
    bau["hauptnummern_je_einheit"] = {e: v["hauptnummern"]
                                      for e, v in je.items()}
    bau["teilaufgaben_je_einheit"] = {e: v["teilaufgaben"]
                                      for e, v in je.items()}
    (ordner / "bau.json").write_text(
        json.dumps(bau, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    print(f"{k}: {bau['seiten']} Seiten, Lösungen {bau['seiten_loesungen']}, "
          f"Fehler {bau['kompilierfehler']}, fehlende Zeichen "
          f"{bau['fehlende_zeichen']}, Overfull {bau['overfull']}, "
          f"Bank-Wörter {bau['bankwort'] or '–'}")
    return 1 if bau["kompilierfehler"] or bau["fehlende_zeichen"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

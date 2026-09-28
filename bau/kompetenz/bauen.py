#!/usr/bin/env python3
"""bauen.py – baut und rendert Kompetenzblätter (Rezept K, zusammenbau v0.7).

Aufruf (aus der Repo-Wurzel):
    python3 bau/kompetenz/bauen.py            # die fünf Blätter des Prüfsteins
    python3 bau/kompetenz/bauen.py <eintrag> "<kette>" <einheit> [...]

Je Bestellung:
1. Probe mit --ohne-register in einen Scratch-Ordner, rendern (xelatex
   zweimal). Kompilierfehler in einer Teilaufgabe: die Bankzeile fällt mit
   --ohne weg (Buchstaben neu, nie „ausgelassen“ auf dem Blatt), höchstens
   zwei Runden. Mehr als vier Seiten: zweite Probe mit --dicht.
2. Bau mit Registerzeile (Kennung XXX-K<n>) nach bau/kompetenz/<K>/ mit den
   Schaltern der Probe, rendern, PNG je Seite (pdftoppm -r 80).
3. bau.json bekommt: seiten, seiten_loesungen, fehlende_zeichen (Missing
   character in beiden .log), overfull, ersatzschrift (pdffonts),
   ersatzzeichen_im_text (pdftotext findet jedes Ersatzzeichen im PDF).
Ergebnis: ergebnis.json neben diesem Skript.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parent.parent
ZB = WURZEL / "werkzeuge" / "zusammenbau.py"
SCRATCH = Path("/tmp/claude-0/kompetenz-probe")
FEHLER = re.compile(r"^\./([^:]+\.tex):(\d+): (.*)$")
BESTELLUNG = [
    ("quadratische-gleichungen", "p-q-Formel", 3),
    ("potenz-exponentialfunktionen", "Wachstumstabelle fortschreiben", 2),
    ("lineare-funktionen", "Graph zeichnen", 2),
    ("prozentrechnung", "Prozentsatz", 2),
    ("trigonometrie", "Sinussatz", 4),
]
AUFRAEUMEN = (".aux", ".log", ".out", ".abh", ".toc")


def zb(eintrag, kette, einheit, extra):
    cmd = [sys.executable, str(ZB), eintrag, "--kompetenz", kette,
           "--einheiten", str(einheit), "--niveau", "for"] + extra
    r = subprocess.run(cmd, cwd=WURZEL, capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode not in (0, 1):
        print(r.stderr)
        sys.exit(f"zusammenbau brach ab: {' '.join(cmd)}")
    m = re.search(r"KENNUNG (\S+)", r.stdout)
    return m.group(1)


def xelatex(ordner, datei):
    for _ in range(2):
        subprocess.run(["xelatex", "-interaction=nonstopmode",
                        "-file-line-error", datei], cwd=ordner,
                       capture_output=True, timeout=600)
    log = (ordner / datei).with_suffix(".log")
    return log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""


def seiten(pdf):
    if not pdf.exists():
        return 0
    r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
    m = re.search(r"Pages:\s+(\d+)", r.stdout)
    return int(m.group(1)) if m else 0


def fehler_ids(ordner, k, log):
    """Bankzeilen, in deren Satz ein Kompilierfehler liegt: die Kommentarzeile
    „% lage: id, …“ über der Fehlerzeile."""
    ids = set()
    for z in log.splitlines():
        m = FEHLER.match(z)
        if not m or not m.group(1).startswith(k):
            continue
        zeilen = (ordner / m.group(1)).read_text(encoding="utf-8").splitlines()
        for i in range(int(m.group(2)) - 1, -1, -1):
            mm = re.match(r"^% (zone|leiter|pruefung): (.+?)( \(Paar.*)?$",
                          zeilen[i])
            if mm:
                ids |= {x.strip() for x in mm.group(2).split(",")}
                break
    return ids


def rendern(ordner, k):
    la = xelatex(ordner, f"{k}.tex")
    ll = xelatex(ordner, f"{k}-loesungen.tex")
    return la, ll


def probe(eintrag, kette, einheit):
    extra, ohne, notiz = [], set(), []
    for runde in range(4):
        ziel = SCRATCH / f"{eintrag}-{runde}"
        shutil.rmtree(ziel, ignore_errors=True)
        args = extra + (["--ohne", ",".join(sorted(ohne))] if ohne else [])
        k = zb(eintrag, kette, einheit, args + ["--ohne-register", "--aus",
                                                str(ziel)])
        la, ll = rendern(ziel, k)
        neu = fehler_ids(ziel, k, la + ll)
        n = seiten(ziel / f"{k}.pdf")
        if neu and len(ohne) < 6:
            ohne |= neu
            notiz.append(f"Kompilierfehler in {sorted(neu)} – weggelassen")
            continue
        if n > 4 and "--dicht" not in extra:
            extra.append("--dicht")
            notiz.append(f"{n} Seiten – zweite Probe mit --dicht")
            continue
        return extra, ohne, notiz, n
    return extra, ohne, notiz, n


def main():
    argv = sys.argv[1:]
    bestellung = BESTELLUNG
    if argv:
        bestellung = [(argv[i], argv[i + 1], int(argv[i + 2]))
                      for i in range(0, len(argv), 3)]
    ergebnis = []
    for eintrag, kette, einheit in bestellung:
        extra, ohne, notiz, n_probe = probe(eintrag, kette, einheit)
        args = extra + (["--ohne", ",".join(sorted(ohne))] if ohne else [])
        k = zb(eintrag, kette, einheit, args)
        ordner = HIER / k
        la, ll = rendern(ordner, k)
        for p in ordner.glob("*.png"):
            p.unlink()
        subprocess.run(["pdftoppm", "-r", "80", "-png", f"{k}.pdf", k],
                       cwd=ordner, check=True)
        subprocess.run(["pdftoppm", "-r", "80", "-png", f"{k}-loesungen.pdf",
                        f"{k}-loesungen"], cwd=ordner, check=True)
        fehlend = sorted(set(re.findall(r"Missing character: There is no (.)",
                                        la + ll)))
        overfull = len(re.findall(r"Overfull \\vbox", la))
        fonts = subprocess.run(["pdffonts", f"{k}.pdf"], cwd=ordner,
                               capture_output=True, text=True).stdout
        bj = json.loads((ordner / "bau.json").read_text(encoding="utf-8"))
        text = "".join(subprocess.run(["pdftotext", f"{d}.pdf", "-"],
                                      cwd=ordner, capture_output=True,
                                      text=True).stdout
                       for d in (k, f"{k}-loesungen"))
        ersatz = bj.get("ersatzzeichen", "")
        im_text = {c: (c in text) for c in ersatz}
        schrift = sorted({m.split("+", 1)[-1].split("-")[0] for m in
                          re.findall(r"^\S+", fonts, re.M)
                          if "+" in m})
        fehler = [z for z in (la + ll).splitlines() if FEHLER.match(z)]
        bj.update({"seiten": seiten(ordner / f"{k}.pdf"),
                   "seiten_loesungen": seiten(ordner / f"{k}-loesungen.pdf"),
                   "fehlende_zeichen": fehlend, "overfull": overfull,
                   "kompilierfehler": fehler[:10],
                   "schriften_im_pdf": schrift,
                   "ersatzzeichen_im_text": im_text,
                   "probe": notiz})
        (ordner / "bau.json").write_text(
            json.dumps(bj, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8", newline="\n")
        for d in (k, f"{k}-loesungen"):
            for suffix in AUFRAEUMEN:
                (ordner / (d + suffix)).unlink(missing_ok=True)
        ergebnis.append({"kennung": k, "eintrag": eintrag, "kette": kette,
                         "seiten": bj["seiten"],
                         "seiten_loesungen": bj["seiten_loesungen"],
                         "teilaufgaben": bj["teilaufgaben"],
                         "hauptnummern": bj["hauptnummern"],
                         "pruefungshoehe": bj["pruefungshoehe"],
                         "fehlende_zeichen": fehlend, "overfull": overfull,
                         "kompilierfehler": len(fehler), "probe": notiz,
                         "dicht": "--dicht" in extra,
                         "ohne": sorted(ohne)})
        print(f"{k}: {bj['seiten']} + {bj['seiten_loesungen']} Seiten, "
              f"fehlende Zeichen {fehlend or 0}, Overfull {overfull}")
    (HIER / "ergebnis.json").write_text(
        json.dumps(ergebnis, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

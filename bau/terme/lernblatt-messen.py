#!/usr/bin/env python3
"""Messlauf für ein Lernblatt aus zusammenbau.py (v0.9, ab v1.0 mit den
Prüfungen des Auftrags auftrag-lernblatt-v10.md).

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

Ab zusammenbau v1.0 dazu (Feld pruefungen_v10 in bau.json): im PDF-Text
des Gesamt kein „Ich kann“, kein „weiter“ außer in „Dann weiter zu“, kein
„Einheit n von“, kein „Hier lernst du“; Folge der Einheiten im Gesamt;
erste Hauptnummer jeder Einheit „Kannst du das schon“ und ihre
Teilaufgaben je Kette; Pflicht-Teilaufgaben je Einheit; Teilaufgaben mit
Sachkontext je Kette (Heuristik hat_sachkontext aus zusammenbau.py,
ohne den Test); Ketten, deren Teilaufgabe in Einheit 1 zuerst steht.
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


def pruefungen_v10(ordner, bau, text):
    """Prüfungen des Auftrags vom 01.10. (Lernblatt v1.0)."""
    k = bau["kennung"]
    g = (ordner / f"{k}-gesamt.tex").read_text(encoding="utf-8")
    folge = [int(m) for m in re.findall(r"\\input\{e(\d+)_a\}", g)]
    flach = re.sub(r"\s+", " ", text)
    weiter = [m.group(0) for m in re.finditer(r".{0,25}\bweiter\b.{0,15}",
                                              flach)
              if "Dann weiter zu" not in m.group(0)]
    ids = {}
    for p in (WURZEL / "bank" / bau["eintraege"][0]).glob("e*.jsonl"):
        for z in p.read_text(encoding="utf-8").splitlines():
            if z.strip():
                d = json.loads(z)
                ids[d["id"]] = d
    je = {}
    for a in bau["aufgaben"]:
        if not a.get("id") or not a["datei"].startswith("e"):
            continue
        n = int(re.match(r"e(\d+)_", a["datei"]).group(1))
        je.setdefault(n, []).append(a)
    test, pflicht, sach, erste = {}, {}, {}, {}
    for n, aa in je.items():
        hn1 = min((a["hauptnummer"] for a in aa if a["hauptnummer"]),
                  default=None)
        e_text = (ordner / f"e{n}_a.tex").read_text(encoding="utf-8")
        titel = re.search(r"\\begin\{kbaufgabe\}\{([^\n]*)\}|"
                          r"\\lbtest\{([^\n]*)\}\{", e_text)
        if titel and titel.group(2):
            titel = re.search(r"\\lbtest\{(.*)\}\{", e_text)
        tt = [a for a in aa if a.get("lage") == "test"] or \
            [a for a in aa if a["hauptnummer"] == hn1]
        test[n] = {"titel": titel.group(1) if titel else None,
                   "beginnt_mit_test": bool(titel and titel.group(1)
                                            .startswith("Kannst du das schon")),
                   "ohne_nummer": all(a["hauptnummer"] is None for a in tt),
                   "teilaufgaben": [ids[a["id"]]["kette"] for a in tt]}
        pflicht[n] = sum(1 for a in aa if a.get("lage") == "pflicht")
        for a in aa:
            z = ids[a["id"]]
            if a.get("lage") in ("leiter", "pruefung") and \
                    ZB.hat_sachkontext(z):
                sach.setdefault(f"e{n} {z['kette']}", []).append(a["id"])
        reihe = []
        for a in sorted(aa, key=lambda a: (a["hauptnummer"] or 0, a["teilaufgabe"])):
            if a.get("lage") == "test":
                continue
            kette = ids[a["id"]]["kette"]
            if kette not in reihe:
                reihe.append(kette)
        erste[n] = reihe
    return {
        "einheiten_folge": folge,
        "ich_kann_im_pdf": flach.count("Ich kann"),
        "weiter_im_pdf": weiter,
        "einheit_n_von_im_pdf": len(re.findall(r"Einheit \d+ von", flach)),
        "hier_lernst_du_im_pdf": flach.count("Hier lernst du"),
        "kannst_du_im_pdf": flach.count("Kannst du das schon"),
        "test": test,
        "pflicht_je_einheit": pflicht,
        "sachkontext_je_kette": sach,
        "ketten_folge_je_einheit": erste,
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
    gesamt_text = subprocess.run(["pdftotext", str(ordner / f"{k}-gesamt.pdf"),
                                  "-"], capture_output=True, text=True).stdout
    if bau.get("zusammenbau", "v0.9") >= "v1.0":
        bau["pruefungen_v10"] = pruefungen_v10(ordner, bau, gesamt_text)
        print(json.dumps(bau["pruefungen_v10"], ensure_ascii=False,
                         indent=1))
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
    if f"{k}-loesungen" in werte:
        bau["seiten_loesungen"] = werte[f"{k}-loesungen"]["seiten"]
    else:
        # ab v1.1: Lösungen am Ende des Gesamt – Seiten ab „Lösungen“
        n = bau["seiten"]
        for s in range(1, n + 1):
            seite = subprocess.run(["pdftotext", "-f", str(s), "-l", str(s),
                                    str(ordner / f"{k}-gesamt.pdf"), "-"],
                                   capture_output=True, text=True).stdout
            if re.search(r"^Lösungen\s*$", seite, re.M):
                bau["seiten_loesungen"] = n - s + 1
                break
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

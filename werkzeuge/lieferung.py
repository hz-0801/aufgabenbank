#!/usr/bin/env python3
"""Lieferliste: wer welches Blatt bekommen hat (eingang/gebaut.csv).

Die eine Stelle für Lieferungen je Schüler (Lehrer 10.10.2026). Die
Zeile schreibt dieses Skript, nie das Modell von Hand. Im Repo steht
nur die Nummer (S01 …), nie der Name.

  python3 werkzeuge/lieferung.py --zeige S02
      die Lieferungen dieses Schülers, neueste zuerst
  python3 werkzeuge/lieferung.py --nummer S02 --eintrag pythagoras \
      --ordner eingang/pythagoras-2026-10-11 [--kennung H7U] \
      [--zusaetze "p10"] [--datum 2026-10-11]
      hängt eine Zeile an; dieselbe Nummer + Ordner nur einmal
"""
import argparse
import csv
import datetime
import pathlib
import re
import sys

WURZEL = pathlib.Path(__file__).resolve().parent.parent
LISTE = WURZEL / "eingang" / "gebaut.csv"
SPALTEN = ["nummer", "datum", "eintrag", "zusaetze", "ordner", "kennung"]


def lesen():
    if not LISTE.exists():
        return []
    with LISTE.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def schreiben(zeilen):
    with LISTE.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, SPALTEN, delimiter=";", lineterminator="\n",
                           extrasaction="ignore")
        w.writeheader()
        for z in zeilen:
            w.writerow({k: (z.get(k) or "") for k in SPALTEN})


def nummer(text):
    m = re.fullmatch(r"[Ss]?0*(\d{1,2})", text.strip())
    if not m or not 1 <= int(m.group(1)) <= 99:
        sys.exit(f"Nummer „{text}“ ungültig (erwartet S01 … S99)")
    return f"S{int(m.group(1)):02d}"


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--zeige")
    a.add_argument("--nummer")
    a.add_argument("--eintrag")
    a.add_argument("--ordner")
    a.add_argument("--kennung", default="")
    a.add_argument("--zusaetze", default="")
    a.add_argument("--datum", default=datetime.date.today().isoformat())
    x = a.parse_args()
    zeilen = lesen()
    if x.zeige:
        n = nummer(x.zeige)
        eigene = sorted((z for z in zeilen if z["nummer"] == n),
                        key=lambda z: z["datum"], reverse=True)
        if not eigene:
            print(f"{n}: noch keine Lieferung")
        for z in eigene:
            print(";".join(z.get(k) or "" for k in SPALTEN))
        return
    if not (x.nummer and x.eintrag and x.ordner):
        sys.exit("--nummer, --eintrag und --ordner sind nötig")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", x.datum):
        sys.exit("--datum als JJJJ-MM-TT")
    n = nummer(x.nummer)
    if any(z["nummer"] == n and z["ordner"] == x.ordner for z in zeilen):
        print(f"{n} {x.ordner} steht schon in der Liste")
        return
    zeilen.append({"nummer": n, "datum": x.datum, "eintrag": x.eintrag,
                   "zusaetze": x.zusaetze, "ordner": x.ordner,
                   "kennung": x.kennung})
    schreiben(zeilen)
    print(f"LIEFERUNG {n} {x.datum} {x.eintrag} angehängt")


if __name__ == "__main__":
    main()

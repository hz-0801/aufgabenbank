#!/usr/bin/env python3
"""Punkte-Zuordnung der Prüfungszeilen (bank/_punkte.csv).

Für jede Bankzeile mit `original` (alle Einträge, auch _basis) holt das
Skript Punkte und Stern des Originals aus den Prüfungskatalogen in
mathe-nachhilfe und führt sie mit dem Urteil `umfang` zusammen:

  ganz    die Bankzeile bildet die ganze Original-Teilaufgabe ab
          (gleiche Zahl verlangter Ergebnisse wie `gesucht`, gleiche
          Handlung wie `format`/`verfahren`; Verfremdung erlaubt)
  teil    das Original hat mehrere Leistungen (typ_neben oder
          gesucht mit „|"), die Bankzeile übt nur einen Teil
  unklar  alles andere (nur Vorschritt einer Einzelleistung, andere
          Handlung, deutlich mehr als das Original, nicht entscheidbar)

Das Urteil trifft ein Modell, das jede Zeile liest, nicht dieses
Skript. Das Skript liefert dafür den Lesestoff und prüft das Ergebnis.

Aufrufe (aus der Wurzel von aufgabenbank):

  python werkzeuge/punkte.py --lesestoff DIR [--nur-neu]
      schreibt DIR/bNN.txt: je Original die Katalogfelder, darunter
      die Bankzeilen (aufgabe, antwort, loesung, pruef); --nur-neu nur
      Zeilen, die in bank/_punkte.csv noch fehlen
  python werkzeuge/punkte.py --urteile DATEI [DATEI ...]
      liest Urteile (id;umfang;grund, ohne Kopfzeile), übernimmt für
      alle übrigen Zeilen das Urteil aus bank/_punkte.csv und schreibt
      die Datei neu (Punkte und Stern immer frisch aus den Katalogen)
  python werkzeuge/punkte.py
      nur Gegenprobe und Zählung, schreibt nichts

Gegenprobe: jede Bankzeile mit original hat genau eine Zeile, keine
Zeile ohne Bankzeile, jedes original steht in einem Katalog, umfang
aus ganz|teil|unklar, grund nicht leer. Fehler → Abbruch ohne
Schreiben (Exit 1).

Katalogpfad: --mn PFAD (Wurzel von mathe-nachhilfe), Vorgabe
../mathe-nachhilfe neben aufgabenbank.
"""
import argparse
import csv
import glob
import json
import os
import sys
from collections import Counter, defaultdict

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIEL = os.path.join(WURZEL, "bank", "_punkte.csv")
KATALOGE = [
    ("msa/msa-katalog-basis.csv", "MSA"),
    ("msa/msa-katalog-kontext.csv", "MSA"),
    ("msa/msa-katalog-gym.csv", "MSA"),
    ("fhr/fhr-katalog.csv", "FHR"),
    ("abitur/abi-katalog.csv", "Abitur"),
    ("abitur/iqb-katalog.csv", "Abitur"),
]
UMFANG = ("ganz", "teil", "unklar")
KOPF = ["id", "original", "punkte", "stern", "umfang", "grund"]
LESEFELDER = ["punkte", "stern", "format", "operator", "gesucht",
              "verfahren", "typ", "typ_neben", "gegeben", "ergebnis",
              "bemerkung"]


def kataloge_laden(mn):
    kat = {}
    for datei, pruefung in KATALOGE:
        pfad = os.path.join(mn, datei)
        with open(pfad, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter=";"):
                kat[r["id"]] = (pruefung, r)
    return kat


def bank_laden():
    zeilen = []
    for pfad in sorted(glob.glob(os.path.join(WURZEL, "bank", "**", "*.jsonl"),
                            recursive=True)):
        with open(pfad, encoding="utf-8") as f:
            for l in f:
                if not l.strip():
                    continue
                d = json.loads(l)
                if d.get("original"):
                    zeilen.append(d)
    zeilen.sort(key=lambda d: (d["original"]["id"], d["id"]))
    return zeilen


def urteile_lesen(pfad, mit_kopf):
    u = {}
    if not os.path.exists(pfad):
        return u
    with open(pfad, encoding="utf-8", newline="") as f:
        for i, l in enumerate(f):
            l = l.rstrip("\n")
            if not l or (mit_kopf and i == 0):
                continue
            p = l.split(";")
            if mit_kopf:
                if len(p) != len(KOPF):
                    sys.exit(f"{pfad}:{i+1}: {len(p)} Felder statt {len(KOPF)}")
                u[p[0]] = (p[4], p[5])
            else:
                if len(p) != 3:
                    sys.exit(f"{pfad}:{i+1}: {len(p)} Felder statt 3")
                if p[0] in u:
                    sys.exit(f"{pfad}:{i+1}: {p[0]} doppelt")
                u[p[0]] = (p[1], p[2])
    return u


def lesestoff(zeilen, kat, ziel, nur, je=115):
    os.makedirs(ziel, exist_ok=True)
    auswahl = [d for d in zeilen if nur is None or d["id"] not in nur]
    stuecke, last = [[]], None
    for d in auswahl:  # nach Original gruppiert, Stücke nicht mitten im Original teilen
        o = d["original"]["id"]
        if len(stuecke[-1]) >= je and o != last:
            stuecke.append([])
        stuecke[-1].append(d)
        last = o
    for n, st in enumerate(stuecke):
        aus, prev = [], None
        for d in st:
            o = d["original"]["id"]
            if o != prev:
                r = kat[o][1] if o in kat else {}
                aus.append(f"\n######## ORIGINAL {o}\n" + "\n".join(
                    f"  {k}: {r.get(k, '(nicht im Katalog)')}" for k in LESEFELDER))
                prev = o
            aus.append(
                f"--- BANK {d['id']}  [hoehe {d.get('hoehe')}, form {d.get('form')}]\n"
                f"  sprosse_text: {d.get('sprosse_text', '')}\n"
                f"  aufgabe: {d.get('aufgabe')}\n  antwort: {d.get('antwort')}\n"
                f"  loesung: {d.get('loesung')}\n  pruef: {d.get('pruef')}")
        with open(os.path.join(ziel, f"b{n:02d}.txt"), "w", encoding="utf-8",
                  newline="\n") as f:
            f.write("\n".join(aus) + "\n")
    print(f"{len(auswahl)} Zeilen in {len(stuecke) if auswahl else 0} Dateien unter {ziel}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mn", default=os.path.join(os.path.dirname(WURZEL), "mathe-nachhilfe"))
    ap.add_argument("--lesestoff")
    ap.add_argument("--nur-neu", action="store_true")
    ap.add_argument("--urteile", nargs="+")
    a = ap.parse_args()

    kat = kataloge_laden(a.mn)
    zeilen = bank_laden()
    bestand = urteile_lesen(ZIEL, mit_kopf=True)

    if a.lesestoff:
        lesestoff(zeilen, kat, a.lesestoff, set(bestand) if a.nur_neu else None)
        return

    urteil = dict(bestand)
    for p in a.urteile or []:
        urteil.update(urteile_lesen(p, mit_kopf=False))

    fehler = []
    ids = Counter(d["id"] for d in zeilen)
    fehler += [f"Bank-id doppelt: {i}" for i, c in ids.items() if c > 1]
    ohne_katalog = sorted({d["original"]["id"] for d in zeilen
                           if d["original"]["id"] not in kat})
    fehler += [f"original ohne Katalogzeile: {o}" for o in ohne_katalog]
    fehler += [f"Urteil ohne Bankzeile: {i}" for i in sorted(set(urteil) - set(ids))]
    aus, zahl = [], defaultdict(Counter)
    for d in zeilen:
        o = d["original"]["id"]
        u = urteil.get(d["id"])
        if u is None:
            fehler.append(f"ohne Urteil: {d['id']}")
            continue
        umfang, grund = u
        if umfang not in UMFANG:
            fehler.append(f"umfang {umfang!r}: {d['id']}")
        if not grund.strip() or ";" in grund:
            fehler.append(f"grund leer oder mit Semikolon: {d['id']}")
        pruefung, r = kat.get(o, ("?", {"punkte": "", "stern": ""}))
        aus.append([d["id"], o, r["punkte"], r["stern"], umfang, grund.strip()])
        zahl[pruefung][umfang] += 1

    print(f"Bankzeilen mit original: {len(zeilen)}, Originale: "
          f"{len({d['original']['id'] for d in zeilen})}, Zeilen: {len(aus)}")
    for p in ("MSA", "FHR", "Abitur"):
        c = zahl[p]
        print(f"  {p:7s} ganz {c['ganz']:5d}  teil {c['teil']:4d}  unklar {c['unklar']:4d}  "
              f"zusammen {sum(c.values())}")
    print(f"Originale ohne Katalogzeile: {len(ohne_katalog)}"
          + ("" if not ohne_katalog else ": " + ", ".join(ohne_katalog)))
    if fehler:
        print(f"{len(fehler)} Fehler, nichts geschrieben:")
        for e in fehler[:40]:
            print("  " + e)
        sys.exit(1)
    if a.urteile:
        with open(ZIEL, "w", encoding="utf-8", newline="\n") as f:
            f.write(";".join(KOPF) + "\n")
            for z in aus:
                f.write(";".join(z) + "\n")
        print(f"geschrieben: {os.path.relpath(ZIEL, WURZEL)}")
    else:
        print("Gegenprobe bestanden.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Prüfstein zusammenbau v0.3 (Kennung, Register, Bauzettel).

Aufruf aus der Repo-Wurzel:
    python3 bau/prozentrechnung/kennung-probe.py PRZ-L1 PRZ-L2 PRZ-F1

Prüft je Kennung:
1. bau/register.csv hat genau eine Zeile mit der Kennung, ihr pfad ist
   der Ordner, Datum/Commit/Versionen stimmen mit bau.json überein.
2. bau.json: jede Aufgabennummer (A<n> + Teilaufgabe) kommt genau einmal
   vor und zeigt auf genau eine Bankzeile; jede id steht in bank/.
3. Die Quelltexte tragen dieselben Nummern: je Hauptnummer so viele
   Teilaufgaben (\\teil, \\gl, \\swz, \\swa, \\swfrage; ab zusammenbau v0.9
   \\kbteil in kbaufgabe) wie bau.json.
4. Die Kennung steht in der Fußzeile jedes Dokuments und in den
   Dateinamen (<kennung>.tex, <kennung>-loesungen.tex).
Dazu: zwei Kennungen mit gleicher Bestellung haben wortgleiche
Aufgabendateien (Kennung ändert nur Rahmen und Namen).
Rückgabe 1 bei einem Fehler.
"""

import csv
import json
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
TEIL = re.compile(r"\\(teil|steil|gl|sgl|tz|stz|swz|swa|swfrage|kbteil)\b")


def bankzeilen(eintrag):
    ids = {}
    for p in (WURZEL / "bank" / eintrag).glob("*.jsonl"):
        for z in p.read_text(encoding="utf-8").splitlines():
            if z.strip():
                d = json.loads(z)
                ids[d["id"]] = p.name
    return ids


def pruefe(kennung, register, fehler):
    zeilen = [z for z in register if z["kennung"] == kennung]
    if len(zeilen) != 1:
        fehler.append(f"{kennung}: {len(zeilen)} Registerzeilen statt 1")
        return None
    reg = zeilen[0]
    ordner = WURZEL / reg["pfad"]
    zettel = json.loads((ordner / "bau.json").read_text(encoding="utf-8"))
    for feld in ("kennung", "datum", "rezept", "bank_commit", "zusammenbau",
                 "vorlage", "pfad"):
        if str(zettel[feld]) != reg[feld]:
            fehler.append(f"{kennung}: {feld} Register „{reg[feld]}“ ≠ "
                          f"bau.json „{zettel[feld]}“")
    # 2. Nummer -> genau eine Bankzeile
    ids = bankzeilen(zettel["eintraege"][0])
    gesehen = {}
    for a in zettel["aufgaben"]:
        nr = f"{a['aufgabe']}{a['teilaufgabe']}"
        if nr in gesehen:
            fehler.append(f"{kennung}: {nr} doppelt")
        gesehen[nr] = a["id"]
        if a["id"] is None:
            fehler.append(f"{kennung}: {nr} ohne Bankzeile")
        elif a["id"] not in ids:
            fehler.append(f"{kennung}: {nr} → {a['id']} nicht in bank/")
    doppelt = {i for i in gesehen.values()
               if list(gesehen.values()).count(i) > 1}
    if doppelt:
        fehler.append(f"{kennung}: Bankzeilen mehrfach: {sorted(doppelt)}")
    # 3. Quelltexte: Teilaufgaben je Hauptnummer
    soll = {}
    for a in zettel["aufgaben"]:
        soll.setdefault((a["datei"], a["hauptnummer"]), 0)
        soll[(a["datei"], a["hauptnummer"])] += 1
    ist = {}
    for datei in sorted({d for d, _ in soll}):
        text = (ordner / datei).read_text(encoding="utf-8")
        text = "\n".join(z for z in text.splitlines() if not z.startswith("%"))
        m = re.search(r"\\setcounter\{aufgabe\}\{(\d+)\}", text)
        nr = int(m.group(1)) if m else 0
        # zusammenbau bis v0.8: aufgabe; ab v0.9 (Lernblatt): kbaufgabe
        for block in re.split(r"\\begin\{(?:kb)?aufgabe\}", text)[1:]:
            nr += 1
            rumpf = re.split(r"\\end\{(?:kb)?aufgabe\}", block)[0]
            ist[(datei, nr)] = len(TEIL.findall(rumpf))
    if ist != soll:
        for k in sorted(set(ist) | set(soll)):
            if ist.get(k) != soll.get(k):
                fehler.append(f"{kennung}: {k[0]} Nr. {k[1]}: Quelltext "
                              f"{ist.get(k)} Teilaufgaben, bau.json {soll.get(k)}")
    # 4. Kennung in Namen und Fußzeile
    for name in (f"{kennung}.tex", f"{kennung}-loesungen.tex"):
        if not (ordner / name).exists():
            fehler.append(f"{kennung}: {name} fehlt")
    doks = sorted(ordner.glob(f"{kennung}*.tex"))
    for d in doks:
        kopf = [z for z in d.read_text(encoding="utf-8").splitlines()
                if z.startswith("\\blattkopf")]
        # bis v0.8 „Thema · Blatt · Kennung“, ab v0.9 nur die Kennung (Befund 2)
        if len(kopf) != 1 or not (kopf[0].endswith(f" · {kennung}}}")
                                  or kopf[0].endswith(f"{{{kennung}}}")):
            fehler.append(f"{kennung}: {d.name} ohne Kennung in der Fußzeile")
    haupt = len({a["hauptnummer"] for a in zettel["aufgaben"]})
    print(f"{kennung}: Register 1 Zeile; bau.json {len(zettel['aufgaben'])} "
          f"Teilaufgaben in {haupt} Hauptnummern → {len(set(gesehen.values()))} "
          f"verschiedene Bankzeilen; Quelltext = bau.json: "
          f"{'ja' if ist == soll else 'nein'}; {len(doks)} Dokumente mit "
          "Kennung in der Fußzeile")
    return ordner, zettel


def main(kennungen):
    with open(WURZEL / "bau" / "register.csv", encoding="utf-8",
              newline="") as f:
        register = list(csv.DictReader(f, delimiter=";"))
    fehler = []
    gebaut = {k: pruefe(k, register, fehler) for k in kennungen}
    # gleiche Bestellung → gleiche Aufgabendateien
    nach_bestellung = {}
    for k, v in gebaut.items():
        if v:
            b = json.dumps(v[1]["bestellung"], sort_keys=True)
            nach_bestellung.setdefault(b, []).append(v)
    for gruppe in nach_bestellung.values():
        for (o1, z1), (o2, z2) in zip(gruppe, gruppe[1:]):
            gleich = all((o1 / d).read_text(encoding="utf-8")
                         == (o2 / d).read_text(encoding="utf-8")
                         for d in sorted({a["datei"] for a in z1["aufgaben"]}))
            same = z1["aufgaben"] == z2["aufgaben"]
            print(f"{z1['kennung']} / {z2['kennung']}: gleiche Bestellung, "
                  f"Aufgabendateien wortgleich: {'ja' if gleich else 'nein'}, "
                  f"Aufgabenliste gleich: {'ja' if same else 'nein'}")
            if not (gleich and same):
                fehler.append(f"{z1['kennung']}/{z2['kennung']}: Inhalt weicht ab")
    print(f"{len(fehler)} Fehler")
    for f_ in fehler:
        print("FEHLER " + f_)
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["PRZ-L1", "PRZ-L2", "PRZ-F1"]))

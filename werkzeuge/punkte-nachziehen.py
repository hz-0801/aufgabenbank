#!/usr/bin/env python3
"""Zieht bank/_punkte.csv nach einem Nachzug der Bank nach.

Aufruf (aus der Wurzel von aufgabenbank):

    python3 werkzeuge/punkte-nachziehen.py <commit> <eintrag> [<eintrag> ...]

<commit> ist der Stand der Bank vor dem Nachzug (etwa der Commit,
mit dem die Mappen gebaut wurden). Für jede Zeile der Punktedatei,
deren id es in der Bank nicht mehr gibt, sucht das Skript die alte
Zeile im alten Stand und dann die neue Zeile mit demselben Eintrag,
demselben Aufgabentext und demselben Original; ist sie eindeutig,
wird die id umbenannt. Zeilen ohne Entsprechung und Zeilen, deren
Aufgabentext sich unter gleicher id geändert hat, werden entfernt;
sie brauchen ein neues Urteil (`punkte.py --lesestoff DIR --nur-neu`,
dann `punkte.py --urteile DATEI`). Grund: Neue Sprossen verschieben
die Nummern der folgenden Sprossen, und damit die ids (29.09.,
Schub 1–3: 102, 36 und 36 Zeilen).

Schreibt bank/_punkte.csv neu und meldet: umbenannt, entfernt
(ohne Entsprechung), entfernt (Aufgabe geändert), mehrdeutig.
"""
import collections
import csv
import glob
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
CSV = WURZEL / "bank" / "_punkte.csv"


def bank_neu():
    neu = {}
    for f in glob.glob(str(WURZEL / "bank" / "*" / "*.jsonl")):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                a = json.loads(l)
                if a.get("original"):
                    neu[a["id"]] = a
    return neu


def bank_alt(commit, eintraege):
    alt = {}
    for e in eintraege:
        aus = subprocess.run(["git", "ls-tree", "--name-only", commit,
                              f"bank/{e}/"], capture_output=True,
                             text=True, cwd=WURZEL).stdout.split()
        for f in aus:
            if not f.endswith(".jsonl"):
                continue
            txt = subprocess.run(["git", "show", f"{commit}:{f}"],
                                 capture_output=True, text=True,
                                 cwd=WURZEL).stdout
            for l in txt.splitlines():
                if l.strip():
                    a = json.loads(l)
                    if a.get("original"):
                        alt[a["id"]] = a
    return alt


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    commit, eintraege = argv[1], argv[2:]
    zeilen = list(csv.reader(open(CSV, encoding="utf-8"), delimiter=";"))
    kopf, zeilen = zeilen[0], zeilen[1:]
    neu, alt = bank_neu(), bank_alt(commit, eintraege)
    ids_csv = {z[0] for z in zeilen}
    fehlend = {i for i in neu if i not in ids_csv}
    schl = lambda a: (a["eintrag"], a["aufgabe"], a["original"]["id"])
    neu_nach = collections.defaultdict(list)
    for i, a in neu.items():
        neu_nach[schl(a)].append(i)
    umben, mehrdeutig, ohne, geaendert = {}, [], [], []
    for z in zeilen:
        if z[0] in neu:
            a_alt = alt.get(z[0])
            if a_alt and a_alt["aufgabe"] != neu[z[0]]["aufgabe"]:
                geaendert.append(z[0])
            continue
        a = alt.get(z[0])
        k = [x for x in neu_nach.get(schl(a), [])] if a else []
        k = [x for x in k if x in fehlend]
        if len(k) == 1:
            umben[z[0]] = k[0]
        elif k:
            mehrdeutig.append(z[0])
        else:
            ohne.append(z[0])
    aus = [kopf]
    for z in zeilen:
        if z[0] in umben:
            z[0] = umben[z[0]]
        if z[0] in neu and z[0] not in geaendert:
            aus.append(z)
    with open(CSV, "w", encoding="utf-8", newline="\n") as f:
        csv.writer(f, delimiter=";", lineterminator="\n").writerows(aus)
    print(f"umbenannt {len(umben)}, entfernt ohne Entsprechung "
          f"{len(ohne) + len(mehrdeutig)} (davon mehrdeutig "
          f"{len(mehrdeutig)}), entfernt Aufgabe geändert "
          f"{len(geaendert)}; jetzt punkte.py --lesestoff --nur-neu")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

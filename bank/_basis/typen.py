#!/usr/bin/env python3
"""Basis-Typen der Bank bestimmen (Teil 1 des Auftrags vom 28.09.).

Liest alle Bankzeilen mit hoehe pruefung, deren original.id ein
Basisteil-Original ist (Muster JJJJ-PAPIER-B…), holt den Typ jedes
Originals aus den MSA-Katalogen von hz-0801/mathe-nachhilfe
(msa/msa-katalog-basis.csv, msa/msa-katalog-gym.csv) und schreibt
bank/_basis/typen.csv und bank/_basis/typen.md.

Jahrgänge eines Typs: verschiedene Jahre, in denen der Typ im
Basisteil eines MSA-Papiers (OS, EBR, FOR, GYM) vorkommt, 2014–2026
(dreizehn Jahrgänge). Eintrag des Typs: der Eintrag, in dem das
jüngste Original des Typs als Prüfungshöhe steht; steht es in mehreren,
der mit den meisten Originalen des Typs, dann alphabetisch.

Erweitert am 02.10.2026 (Lehrer): Basis-Typen sind alle Typen des
Basisteils der P10 (msa-katalog-basis.csv, Spalte typ) und dazu die
Typen der Basisteil-Originale in der Bank (zwei GYM-Typen). Für einen
Typ ohne Prüfungshöhe in der Bank: Eintrag = Katalogeintrag, der das
Thema des Typs trägt (themen.csv, Profil msa); einheit aus NEU_EINHEIT
(von Hand nach den Einheiten des Katalogeintrags); quelle = häufigste
quelle der Bankzeilen dieser Einheit. Original jedes Typs: das
jüngste Basisteil-Original des Typs im Katalog, das in der Mappe des
Eintrags steht (mappen/<eintrag>.md, „### <id>“). kette_nr bleibt für
schon vorhandene Typen stehen; neue Typen hängen sich je Eintrag
alphabetisch hinten an (die ids des Vorrats bleiben gleich).

Aufruf: python3 bank/_basis/typen.py [<pfad zu mathe-nachhilfe>]
"""
import csv
import json
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
MN = Path(sys.argv[1]) if len(sys.argv) > 1 else WURZEL.parent / "mathe-nachhilfe"
BASIS = re.compile(r"^\d{4}-[A-Z]+-B")
PAPIERFOLGE = {"FOR": 0, "EBR": 1, "OS": 2, "GYM": 3}
# Einheit des Katalogeintrags je Typ ohne Prüfungshöhe in der Bank
NEU_EINHEIT = {
    "Arithmetisches Mittel berechnen": 4,
    "Fehlenden Wert aus Mittelwert bestimmen": 4,
    "Median bestimmen": 4,
    "Spannweite berechnen": 4,
    "Eigenschaft einer Figur zuordnen": 3,
    "Winkel über Scheitel- oder Nebenwinkel bestimmen": 2,
    "Ergebnismenge aufzählen": 1,
    "Zufallsgerät zu Wahrscheinlichkeit entwerfen": 2,
    "Größen vergleichen": 1,
    "Zeiteinheiten umrechnen": 2,
    "Portionen aus Gesamtmenge berechnen": 4,
    "Strecke aus Teilstrecken berechnen": 4,
    "Körper aus Netz oder Schrägbild benennen": 1,
    "Parabel verschieben": 2,
    "Scheitelpunkt ablesen": 2,
    "Scheitelpunktform aufstellen": 2,
    "Proportionale Zuordnung Dreisatz": 2,
    "Pythagoras Gleichung zuordnen": 1,
    "Satz des Pythagoras formulieren": 1,
    "Quadratseite aus Fläche berechnen": 1,
    "Rechteckseite aus Fläche berechnen": 1,
    "Umfang Rechteck berechnen": 1,
    "Term zu Figur angeben": 1,
}


def mappe_ids(ein):
    return set(re.findall(r"^### (\S+)", (WURZEL / "mappen" / f"{ein}.md")
                          .read_text(encoding="utf-8"), re.M))


def katalog():
    k = {}
    for f in ("msa-katalog-basis.csv", "msa-katalog-gym.csv"):
        with open(MN / "msa" / f, encoding="utf-8", newline="") as h:
            for z in csv.DictReader(h, delimiter=";"):
                z["datei"] = f
                k[z["id"]] = z
    return k


def jung(oid, kat):
    z = kat[oid]
    return (-int(z["jahr"]), PAPIERFOLGE.get(z["papier"], 9), oid)


def main():
    kat = katalog()
    orig = {}  # id -> {eintrag: [bankzeilen]}
    for f in sorted((WURZEL / "bank").glob("*/*.jsonl")):
        if f.parent.name.startswith("_"):
            continue
        for roh in f.read_text(encoding="utf-8").splitlines():
            if not roh:
                continue
            a = json.loads(roh)
            o = a.get("original")
            if a.get("hoehe") == "pruefung" and o and BASIS.match(o["id"]):
                orig.setdefault(o["id"], {}).setdefault(a["eintrag"], []).append(a)
    jahre = {}
    for z in kat.values():
        if z["block"] == "Basis":
            jahre.setdefault(z["typ"], set()).add(int(z["jahr"]))
    alle_ids = {}
    for oid, z in kat.items():
        if z["block"] == "Basis":
            alle_ids.setdefault(z["typ"], []).append(oid)
    for ids in alle_ids.values():
        ids.sort(key=lambda i: jung(i, kat))
    typen = {}
    for oid in orig:
        typen.setdefault(kat[oid]["typ"], []).append(oid)
    zeilen = []
    for typ, ids in typen.items():
        ids.sort(key=lambda i: jung(i, kat))
        j = ids[0]
        ein = sorted(orig[j], key=lambda e: (-sum(e in orig[i] for i in ids), e))[0]
        quelle_zeile = orig[j][ein][0]
        m = mappe_ids(ein)
        j = next((i for i in alle_ids[typ] if i in m), j)
        zeilen.append({
            "typ": typ,
            "thema": kat[j]["thema"],
            "jahrgaenge": len(jahre[typ]),
            "jahre": " ".join(str(x) for x in sorted(jahre[typ])),
            "originale_bank": " ".join(sorted(ids)),
            "zahl_originale": len(ids),
            "eintraege": " ".join(sorted({e for i in ids for e in orig[i]})),
            "eintrag": ein,
            "original": j,
            "jahr": int(kat[j]["jahr"]),
            "papier": kat[j]["papier"],
            "einheit": quelle_zeile["einheit"],
            "quelle": quelle_zeile["quelle"],
        })
    for z in zeilen:
        z["grundlage"] = "bank"
    # Typen des Basisteils ohne Prüfungshöhe in der Bank (02.10.2026)
    with open(MN / "themen.csv", encoding="utf-8", newline="") as h:
        th_ein = {t["thema"]: t["kanonisch"] for t in
                  csv.DictReader(h, delimiter=";") if t["profil"] == "msa"}
    basis_typen = {z["typ"] for z in kat.values()
                   if z["datei"] == "msa-katalog-basis.csv"
                   and z["block"] == "Basis"}
    for typ in sorted(basis_typen - set(typen)):
        ids = alle_ids[typ]
        ein = th_ein[kat[ids[0]]["thema"]]
        m = mappe_ids(ein)
        # steht kein Original in der Mappe (02.10.: Proportionale
        # Zuordnung Dreisatz in zuordnungen), das jüngste des Katalogs;
        # bank-pruef meldet es, bis der Katalogeintrag es nennt
        j = next((i for i in ids if i in m), ids[0])
        e = NEU_EINHEIT[typ]
        qs = [json.loads(r)["quelle"] for r in
              (WURZEL / "bank" / ein / f"e{e}.jsonl").read_text(
                  encoding="utf-8").splitlines() if r]
        zeilen.append({
            "typ": typ, "thema": kat[j]["thema"],
            "jahrgaenge": len(jahre[typ]),
            "jahre": " ".join(str(x) for x in sorted(jahre[typ])),
            "originale_bank": "", "zahl_originale": 0, "eintraege": ein,
            "eintrag": ein, "original": j, "jahr": int(kat[j]["jahr"]),
            "papier": kat[j]["papier"], "einheit": e,
            "quelle": max(sorted(set(qs)), key=qs.count),
            "grundlage": "katalog"})
    zeilen.sort(key=lambda z: (-z["jahrgaenge"], z["typ"]))
    # kette_nr je Eintragsdatei: bisherige Nummer bleibt, neue Typen
    # alphabetisch dahinter
    alt = {}
    try:
        with open(WURZEL / "bank" / "_basis" / "typen.csv", encoding="utf-8",
                  newline="") as h:
            alt = {t["typ"]: int(t["kette_nr"])
                   for t in csv.DictReader(h, delimiter=";")}
    except FileNotFoundError:
        pass
    for z in sorted(zeilen, key=lambda z: (z["typ"] not in alt, z["typ"])):
        if z["typ"] in alt:
            z["kette_nr"] = alt[z["typ"]]
        else:
            belegt = [y["kette_nr"] for y in zeilen
                      if y["eintrag"] == z["eintrag"] and "kette_nr" in y]
            z["kette_nr"] = max(belegt, default=0) + 1
    felder = list(zeilen[0])
    with open(WURZEL / "bank" / "_basis" / "typen.csv", "w", encoding="utf-8",
              newline="") as h:
        w = csv.DictWriter(h, felder, delimiter=";", lineterminator="\n")
        w.writeheader()
        w.writerows(zeilen)
    md = ["# Basis-Typen", "",
          "Erzeugt von bank/_basis/typen.py (nicht von Hand ändern).",
          "Grundlage: alle Typen des Basisteils der P10",
          "(msa-katalog-basis.csv) und die Typen der Bankzeilen mit hoehe",
          "pruefung und Basisteil-Original (id JJJJ-PAPIER-B…); Typ aus msa/msa-katalog-basis.csv bzw.",
          "msa/msa-katalog-gym.csv (hz-0801/mathe-nachhilfe). Jahrgänge:",
          "verschiedene Jahre 2014–2026 (13), in denen der Typ im Basisteil",
          "eines MSA-Papiers vorkommt – im ganzen Katalog, nicht nur in der",
          "Bank. Eintrag: Datei bank/_basis/<eintrag>.jsonl.", "",
          f"{len(zeilen)} Typen, {sum(z['zahl_originale'] for z in zeilen)} "
          f"Originale in der Bank; "
          f"{sum(z['grundlage'] == 'katalog' for z in zeilen)} Typen ohne "
          "Prüfungshöhe in der Bank (Originale in der Bank: 0).", "",
          "| Typ | Jahrgänge | Originale in der Bank | Eintrag | jüngstes Original |",
          "| --- | --- | --- | --- | --- |"]
    for z in zeilen:
        md.append(f"| {z['typ']} | {z['jahrgaenge']} ({z['jahre']}) | "
                  f"{z['zahl_originale']}: {z['originale_bank']} | "
                  f"{z['eintrag']} (k{z['kette_nr']}) | {z['original']} |")
    (WURZEL / "bank" / "_basis" / "typen.md").write_text("\n".join(md) + "\n",
                                                        encoding="utf-8")
    print(f"{len(zeilen)} Typen geschrieben")


if __name__ == "__main__":
    main()

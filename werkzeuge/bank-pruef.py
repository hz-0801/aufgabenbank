#!/usr/bin/env python3
"""Prüft die Bank eines Katalogeintrags (bank.md, Abschnitt „Prüfung").

Aufruf:
    python3 werkzeuge/bank-pruef.py <eintrag> [--katalog DATEI]
    python3 werkzeuge/bank-pruef.py --selbsttest

Liest bank/<eintrag>/zone.jsonl und e<n>.jsonl, prüft die Felder
(Pflichtfelder, id-Muster, Kettenfolge, Mengen), wertet jedes pruef
aus und vergleicht mit den Zahlen in loesung. Ausgabe je Aufgabe eine
Zeile OK/ABWEICHUNG, Ketten- und Mengenbefunde als eigene Zeilen,
zuletzt die Zahl der Abweichungen. Rückgabewert 1 bei Abweichungen.

Mit --katalog wird zusätzlich geprüft, dass sprosse_text wortgleich
in der Katalogzeile quelle steht und kette wortgleich im Katalog.
"""

import json
import math
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

FELDER = ["id", "eintrag", "einheit", "kette", "kette_nr", "sprosse",
          "sprosse_text", "merkmal", "hoehe", "variante", "aufgabe",
          "form", "antwort", "loesung", "pruef", "original", "grafik",
          "quelle"]
HOEHEN = ["vorstufe", "grundfall", "sprosse", "pruefung", "pflicht"]
PFLICHT = ["fehler", "begruenden", "darstellung", "anwendung"]
FORMEN = ["teil", "gleichungsraster", "dreisatz", "streifenfeld",
          "streifenleer", "ankreuzen", "tabelle", "zeichnen", "text"]
MENGE = {"vorstufe": 4, "grundfall": 5, "sprosse": 3}
MENGE_PFLICHT = 3
MENGE_ORIGINAL = 2
TOLERANZ = Decimal("0.005")

# Zahl mit Dezimalkomma; Tausender sind vorher zusammengezogen.
ZAHL = re.compile(r"(?<![\d,])[-−]?\d+(?:,\d+)?")


def zahlen_aus(text):
    """Zahlen aus einer Lösung ziehen: [(Decimal, Nachkommastellen)]."""
    t = text.replace("{,}", ",")
    t = re.sub(r"(\d)\\,(?=\d{3}(?!\d))", r"\1", t)   # 1\,200
    t = re.sub(r"(\d)[  ](?=\d{3}(?!\d))", r"\1", t)  # 1 200 (schmal)
    t = t.replace("\\,", " ").replace("\\%", "%")
    # Buchstaben mit angehängter Ziffer (x1, a2) sind keine Zahlen.
    t = re.sub(r"[A-Za-z]\d+", " ", t)
    aus = []
    for m in ZAHL.finditer(t):
        s = m.group().replace("−", "-")
        stellen = len(s.split(",")[1]) if "," in s else 0
        aus.append((Decimal(s.replace(",", ".")), stellen))
    return aus


def gerundet(wert, stellen):
    q = Decimal(1).scaleb(-stellen)
    return Decimal(repr(float(wert))).quantize(q, rounding=ROUND_HALF_UP)


def werte_aus(pruef):
    """pruef in leerem Namensraum plus math auswerten -> Liste."""
    w = eval(pruef, {"__builtins__": {}}, {"math": math})
    if isinstance(w, (list, tuple)):
        return list(w)
    return [w]


def vergleiche(pruef, loesung):
    """Leere Liste = passt; sonst Befunde."""
    try:
        werte = werte_aus(pruef)
    except Exception as e:  # noqa: BLE001
        return [f"pruef nicht auswertbar ({e})"]
    zahlen = zahlen_aus(loesung)
    if not zahlen:
        return ["loesung ohne Zahl"]
    befunde = []
    for w in werte:
        if not isinstance(w, (int, float)):
            befunde.append(f"pruef-Wert keine Zahl: {w!r}")
            continue
        treffer = any(abs(gerundet(w, st) - z) <= TOLERANZ
                      for z, st in zahlen)
        if not treffer:
            gez = ", ".join(str(z) for z, _ in zahlen)
            befunde.append(f"{w:g} nicht in loesung ({gez})")
    return befunde


def pruef_leer_erlaubt(a):
    return (a.get("pflicht") == "begruenden" or a["form"] == "zeichnen"
            or not re.search(r"\d", a["loesung"]))


def pruefe_zeile(a, eintrag, einheit):
    """Feld- und Rechenprüfung einer Zeile -> Befunde."""
    b = []
    fehlt = [f for f in FELDER if f not in a]
    if fehlt:
        return ["Feld fehlt: " + ", ".join(fehlt)]
    extra = set(a) - set(FELDER) - {"pflicht"}
    if extra:
        b.append("unbekanntes Feld: " + ", ".join(sorted(extra)))
    if a["eintrag"] != eintrag:
        b.append(f"eintrag {a['eintrag']!r} statt {eintrag!r}")
    if a["einheit"] != einheit:
        b.append(f"einheit {a['einheit']} statt {einheit}")
    for f in ("kette_nr", "sprosse", "variante", "quelle"):
        if not isinstance(a[f], int) or isinstance(a[f], bool):
            b.append(f"{f} keine ganze Zahl")
    if b:
        return b
    if einheit == 0:
        soll = f"{eintrag}-zone-f{a['kette_nr']}-v{a['variante']}"
    else:
        soll = (f"{eintrag}-e{einheit}-k{a['kette_nr']}-s{a['sprosse']}"
                f"-v{a['variante']}")
    if a["id"] != soll:
        b.append(f"id {a['id']!r} statt {soll!r}")
    if a["hoehe"] not in HOEHEN:
        b.append(f"hoehe {a['hoehe']!r} unbekannt")
    if a["hoehe"] == "pflicht":
        if a.get("pflicht") not in PFLICHT:
            b.append(f"pflicht {a.get('pflicht')!r} unbekannt")
    elif "pflicht" in a:
        b.append("pflicht nur bei hoehe pflicht")
    if a["form"] not in FORMEN:
        b.append(f"form {a['form']!r} unbekannt")
    if (a["sprosse"] == 0) != (a["hoehe"] == "vorstufe"):
        b.append("sprosse 0 genau dann, wenn hoehe vorstufe")
    o = a["original"]
    if a["hoehe"] == "pruefung":
        if not (isinstance(o, dict) and set(o) == {"id", "jahr", "papier"}
                and re.fullmatch(r"\d{4}-[A-Z]+-[A-Z]\d+[a-z]", o["id"])
                and o["id"].startswith(str(o["jahr"]))):
            b.append("original fehlt oder unvollständig")
    elif o is not None:
        b.append("original nur bei hoehe pruefung")
    for f in ("kette", "sprosse_text", "merkmal", "aufgabe", "loesung"):
        if not isinstance(a[f], str) or not a[f].strip():
            b.append(f"{f} leer")
    if re.search(r"(?<!\\)%", a["aufgabe"] + a["grafik"] + a["loesung"]):
        b.append("nacktes % (LaTeX: \\%)")
    if "\\teil" in a["aufgabe"] or "\\begin{" in a["aufgabe"]:
        b.append("aufgabe mit \\teil oder Umgebung")
    if a["pruef"] == "":
        if not pruef_leer_erlaubt(a):
            b.append("pruef fehlt")
    else:
        b.extend(vergleiche(a["pruef"], a["loesung"]))
    return b


def pruefe_ketten(zeilen, datei, einheit):
    """Kettenfolge und Mengen einer Datei -> Befundzeilen."""
    b = []
    ketten = []  # Reihenfolge des ersten Auftretens
    for a in zeilen:
        k = a["kette_nr"]
        if not ketten or ketten[-1][0] != k:
            if any(k == kk for kk, _ in ketten):
                b.append(f"{datei} k{k}: Kette nicht zusammenhängend")
            ketten.append((k, []))
        ketten[-1][1].append(a)
    nummern = [k for k, _ in ketten]
    if nummern != list(range(1, len(nummern) + 1)):
        b.append(f"{datei}: kette_nr nicht lückenlos ab 1: {nummern}")
    orig_gesamt = {}
    pflicht_zahl = {}
    for k, reihe in ketten:
        if len({a["kette"] for a in reihe}) > 1:
            b.append(f"{datei} k{k}: kette-Name wechselt")
        rang = -1
        sprossen = []
        for a in reihe:
            r = HOEHEN.index(a["hoehe"]) if a["hoehe"] in HOEHEN else -1
            if r < rang:
                b.append(f"{datei} {a['id']}: hoehe {a['hoehe']} "
                         f"nach höherer Stufe")
            rang = max(rang, r)
            if not sprossen or sprossen[-1][0] != a["sprosse"]:
                sprossen.append((a["sprosse"], []))
            sprossen[-1][1].append(a)
        snr = [s for s, _ in sprossen]
        start = snr[0] if snr else 0
        if start not in (0, 1) or snr != list(range(start,
                                                    start + len(snr))):
            b.append(f"{datei} k{k}: Sprossen nicht lückenlos: {snr}")
        grund = [s for s, g in sprossen if g[0]["hoehe"] == "grundfall"]
        if len(grund) > 1:
            b.append(f"{datei} k{k}: mehr als ein Grundfall")
        for s, gruppe in sprossen:
            v = [a["variante"] for a in gruppe]
            if v != list(range(1, len(v) + 1)) and einheit != 0:
                b.append(f"{datei} k{k} s{s}: Varianten nicht 1..n: {v}")
            for f in ("sprosse_text", "merkmal", "hoehe", "quelle"):
                if len({a[f] for a in gruppe}) > 1:
                    b.append(f"{datei} k{k} s{s}: {f} uneinheitlich")
            h = gruppe[0]["hoehe"]
            if einheit == 0:
                continue
            if h in MENGE and len(gruppe) != MENGE[h]:
                b.append(f"{datei} k{k} s{s}: {len(gruppe)} Zeilen, "
                         f"Menge {h} = {MENGE[h]}")
            if h == "pruefung":
                zahl = {}
                for a in gruppe:
                    oid = (a["original"] or {}).get("id")
                    zahl[oid] = zahl.get(oid, 0) + 1
                    orig_gesamt[oid] = orig_gesamt.get(oid, 0) + 1
                for oid, n in zahl.items():
                    if n != MENGE_ORIGINAL:
                        b.append(f"{datei} k{k} s{s}: Original {oid} "
                                 f"{n}×, Menge {MENGE_ORIGINAL}")
            if h == "pflicht":
                p = gruppe[0].get("pflicht")
                pflicht_zahl[p] = pflicht_zahl.get(p, 0) + len(gruppe)
        if einheit == 0:
            b.extend(pruefe_zone_kette(datei, k, sprossen))
    for oid, n in orig_gesamt.items():
        if n != MENGE_ORIGINAL:
            b.append(f"{datei}: Original {oid} {n}× in der Einheit")
    for p, n in pflicht_zahl.items():
        if n != MENGE_PFLICHT:
            b.append(f"{datei}: pflicht {p} {n}×, Menge {MENGE_PFLICHT}")
    return b


def pruefe_zone_kette(datei, k, sprossen):
    """Zone: s1 zwei sehr leichte, s2 eine mittlere, ab s3 je
    Fallstrick eine; Varianten laufen über die Fertigkeit."""
    b = []
    soll = {1: 2, 2: 1}
    for s, gruppe in sprossen:
        n = soll.get(s, 1)
        if len(gruppe) != n:
            b.append(f"{datei} f{k} s{s}: {len(gruppe)} Zeilen, Menge {n}")
    v = [a["variante"] for _, g in sprossen for a in g]
    if v != list(range(1, len(v) + 1)):
        b.append(f"{datei} f{k}: Varianten nicht 1..n: {v}")
    if [s for s, _ in sprossen][:2] != [1, 2]:
        b.append(f"{datei} f{k}: Zone braucht s1 (leicht) und s2 (mittel)")
    return b


def pruefe_katalog(a, katalog):
    b = []
    q = a["quelle"]
    if not 1 <= q <= len(katalog):
        return [f"quelle {q} außerhalb des Katalogs"]
    if a["sprosse_text"] not in katalog[q - 1]:
        b.append(f"sprosse_text nicht wortgleich in Zeile {q}")
    if a["kette"] not in "\n".join(katalog):
        b.append("kette nicht wortgleich im Katalog")
    return b


def lade(datei):
    zeilen = []
    for i, roh in enumerate(datei.read_text(encoding="utf-8")
                            .split("\n"), 1):
        if roh == "":
            continue
        try:
            zeilen.append(json.loads(roh))
        except json.JSONDecodeError as e:
            raise SystemExit(f"{datei}:{i}: kein JSON ({e})")
    return zeilen


def pruefe_eintrag(eintrag, katalog=None, wurzel=Path(".")):
    ordner = wurzel / "bank" / eintrag
    dateien = sorted(ordner.glob("*.jsonl"),
                     key=lambda p: (p.stem != "zone", p.stem))
    if not dateien:
        raise SystemExit(f"keine jsonl in {ordner}")
    abw = 0
    ids = {}
    texte = {}
    for datei in dateien:
        roh = datei.read_text(encoding="utf-8")
        if roh.startswith("﻿") or "\r" in roh or "\n\n" in roh:
            print(f"ABWEICHUNG {datei.name}: BOM, CR oder Leerzeile")
            abw += 1
        m = re.fullmatch(r"e(\d+)|zone", datei.stem)
        if not m:
            print(f"ABWEICHUNG {datei.name}: Dateiname")
            abw += 1
            continue
        einheit = int(m.group(1)) if m.group(1) else 0
        zeilen = lade(datei)
        for a in zeilen:
            befunde = pruefe_zeile(a, eintrag, einheit)
            if not befunde and katalog is not None:
                befunde = pruefe_katalog(a, katalog)
            aid = a.get("id", "?")
            if aid in ids:
                befunde.append(f"id doppelt (auch {ids[aid]})")
            ids[aid] = datei.name
            t = re.sub(r"\s+", " ", a.get("aufgabe", "")).strip()
            if t and t in texte:
                befunde.append(f"aufgabe doppelt (wie {texte[t]})")
            texte[t] = aid
            if befunde:
                abw += 1
                print(f"ABWEICHUNG {aid}: " + "; ".join(befunde))
            else:
                print(f"OK {aid}")
        if all(set(FELDER) <= set(a) for a in zeilen):
            for befund in pruefe_ketten(zeilen, datei.name, einheit):
                abw += 1
                print(f"ABWEICHUNG {befund}")
    print(f"Abweichungen: {abw}")
    return abw


def selbsttest():
    """Drei Beispielzeilen: zwei richtige, eine falsche."""
    basis = {"eintrag": "test", "einheit": 2, "kette": "Prozentsatz",
             "kette_nr": 1, "merkmal": "Ganzes 100",
             "form": "teil", "antwort": "__ %", "original": None,
             "grafik": "", "quelle": 1}
    z1 = dict(basis, id="test-e2-k1-s1-v1", sprosse=1, variante=1,
              sprosse_text="Teil von 100", hoehe="grundfall",
              aufgabe="$37$ von $100$ – wie viel Prozent?",
              loesung="$37\\,\\%$", pruef="37/100*100")
    z2 = dict(basis, id="test-e2-k1-s1-v2", sprosse=1, variante=2,
              sprosse_text="Teil von 100", hoehe="grundfall",
              aufgabe="$1\\,250$ von $4\\,000$ – wie viel Prozent?",
              loesung="$1\\,250 : 4\\,000 = 0{,}3125 \\approx "
                      "31{,}3\\,\\%$",
              pruef="[1250/4000, 1250/4000*100]")
    z3 = dict(basis, id="test-e2-k1-s1-v3", sprosse=1, variante=3,
              sprosse_text="Teil von 100", hoehe="grundfall",
              aufgabe="$9$ von $12$ – wie viel Prozent?",
              loesung="$70\\,\\%$", pruef="9/12*100")
    erwartet = [True, True, False]
    ok = True
    for z, soll in zip((z1, z2, z3), erwartet):
        befunde = pruefe_zeile(z, "test", 2)
        ist = not befunde
        zeichen = "OK" if ist else "ABWEICHUNG"
        print(f"{zeichen} {z['id']}" + ("" if ist else ": "
                                        + "; ".join(befunde)))
        ok &= ist == soll
    print("Selbsttest bestanden" if ok else "Selbsttest GESCHEITERT")
    return 0 if ok else 1


def main(argv):
    if argv[1:] == ["--selbsttest"]:
        return selbsttest()
    if len(argv) not in (2, 4) or (len(argv) == 4
                                   and argv[2] != "--katalog"):
        print(__doc__)
        return 2
    katalog = None
    if len(argv) == 4:
        katalog = Path(argv[3]).read_text(encoding="utf-8").split("\n")
    wurzel = Path(__file__).resolve().parent.parent
    return 1 if pruefe_eintrag(argv[1], katalog, wurzel) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

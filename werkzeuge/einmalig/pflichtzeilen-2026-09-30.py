#!/usr/bin/env python3
"""Einmalig (Auftrag bank-pruef v0.11, 2026-09-30): sammelt alle
Zeilen mit hoehe "pflicht" aus bank/<eintrag>/e<n>.jsonl (ohne
_basis, ohne zone) als Bestandsaufnahme für die Formprobe.

Aufruf:  python3 werkzeuge/einmalig/pflichtzeilen-2026-09-30.py [AUSGABE]
Ausgabe je Zeile: id | pflicht | aufgabe (120 Zeichen) |
loesung (60 Zeichen) | pruef; Standard nach stdout.
"""
import json
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent


def kurz(t, n):
    t = re.sub(r"\s+", " ", t).strip()
    return t[:n]


def main(argv):
    aus = []
    for ordner in sorted((WURZEL / "bank").iterdir()):
        if not ordner.is_dir() or ordner.name.startswith("_"):
            continue
        for datei in sorted(ordner.glob("e*.jsonl")):
            if not re.fullmatch(r"e\d+", datei.stem):
                continue
            for z in datei.read_text(encoding="utf-8").split("\n"):
                if not z.strip():
                    continue
                a = json.loads(z)
                if a.get("hoehe") != "pflicht":
                    continue
                aus.append(" | ".join([
                    a["id"], a.get("pflicht", "?"),
                    kurz(a["aufgabe"], 120), kurz(a["loesung"], 60),
                    a["pruef"]]))
    text = "\n".join(aus) + "\n"
    if len(argv) > 1:
        Path(argv[1]).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    print(f"{len(aus)} Pflichtzeilen", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)

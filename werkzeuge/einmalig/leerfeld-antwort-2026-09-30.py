#!/usr/bin/env python3
"""Einmalig (30.09.2026): Antwortgerüst vereinheitlichen.

Ersetzt im Feld `antwort` (nur dort) aller Bankzeilen
  \\leerfeld[X]  ->  __ X
  \\leerfeld     ->  __
wie bank.md (Feld antwort) es vorschreibt. Alle übrigen Felder,
die Feldreihenfolge und alle anderen Zeilen bleiben unverändert.
Gibt Zählungen vorher/nachher aus (Gegenprobe).

Aufruf aus der Wurzel des Repos:
  python3 werkzeuge/einmalig/leerfeld-antwort-2026-09-30.py
"""
import glob
import json
import re
import sys

MUSTER = re.compile(r"\\leerfeld(?:\[([^\]]*)\])?")


def ersetze(text):
    return MUSTER.sub(lambda m: "__ " + m.group(1) if m.group(1) is not None else "__", text)


def zaehle(pfade):
    antwort = andere = zeilen = 0
    for p in pfade:
        with open(p, encoding="utf-8", newline="") as f:
            for z in f:
                if not z.strip():
                    continue
                zeilen += 1
                d = json.loads(z)
                if "\\leerfeld" in d.get("antwort", ""):
                    antwort += 1
                andere += sum(1 for k, v in d.items() if k != "antwort"
                              and isinstance(v, str) and "\\leerfeld" in v)
    return antwort, andere, zeilen


def main():
    pfade = sorted(glob.glob("bank/*/*.jsonl"))
    vorher = zaehle(pfade)
    geaendert = {}
    for p in pfade:
        with open(p, encoding="utf-8", newline="") as f:
            alt = f.read().split("\n")
        neu = []
        n = 0
        for z in alt:
            if z.strip():
                d = json.loads(z)
                a = d.get("antwort", "")
                if "\\leerfeld" in a:
                    d["antwort"] = ersetze(a)
                    z = json.dumps(d, ensure_ascii=False)
                    n += 1
            neu.append(z)
        if n:
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write("\n".join(neu))
            geaendert[p] = n
    nachher = zaehle(pfade)
    for p, n in geaendert.items():
        print(f"{p}: {n} Zeilen")
    print(f"antwort mit \\leerfeld: {vorher[0]} -> {nachher[0]}")
    print(f"andere Felder mit \\leerfeld: {vorher[1]} -> {nachher[1]}")
    print(f"Zeilen gesamt: {vorher[2]} -> {nachher[2]}")
    if nachher[0] or vorher[1] != nachher[1] or vorher[2] != nachher[2]:
        sys.exit(1)


if __name__ == "__main__":
    main()

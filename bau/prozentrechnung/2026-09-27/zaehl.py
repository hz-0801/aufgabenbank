#!/usr/bin/env python3
"""Zählt je Aufgabendatei Hauptnummern, Teilaufgaben, Merkkästen,
Grafiken und Zeilen – für vergleich.md (Prüfstein prozentrechnung).

Aufruf: python3 zaehl.py <datei.tex> [<von-Muster> <bis-Muster>]
Mit den beiden Mustern (Regex) zählt es nur den Ausschnitt ab der
ersten Zeile, die <von> trifft, bis vor die erste, die <bis> trifft.
"""
import re
import sys

TEIL = re.compile(r"\\(teil|steil|tz|stz|swz|swa|swfrage|gl|sgl)\b")
GRAFIK = re.compile(r"\\(streifen\w*|sachtabelle|bruchrechteck|bruchkreis|"
                    r"zahlenstrahl|kreisdiagramm\w*|kreisleer|kreissektor|"
                    r"saeulen\w*|balkenab|liniendia|baum\w+|wertetabelle\w*|"
                    r"vierfeldertafel|histogramm|strichliste)\b|"
                    r"\\begin\{(ksys3?|dreisatz|kreis|zahlengerade|boxplots)\}")


def zaehle(zeilen):
    text = "\n".join(z for z in zeilen if not z.lstrip().startswith("%"))
    return {
        "haupt": len(re.findall(r"\\begin\{aufgabe\}", text)),
        "teil": len(TEIL.findall(text)),
        "kasten": len(re.findall(r"\\uebersichtskasten\b", text)),
        "grafik": len(GRAFIK.findall(text)),
        "zeilen": len(zeilen),
        "ohne_kommentar": sum(1 for z in zeilen
                              if not z.lstrip().startswith("%")),
    }


def main():
    zeilen = open(sys.argv[1], encoding="utf-8").read().splitlines()
    if len(sys.argv) == 4:
        von, bis = re.compile(sys.argv[2]), re.compile(sys.argv[3])
        a = next(i for i, z in enumerate(zeilen) if von.search(z))
        e = next((i for i, z in enumerate(zeilen) if i > a and bis.search(z)),
                 len(zeilen))
        zeilen = zeilen[a:e]
    z = zaehle(zeilen)
    print(" ".join(f"{k}={v}" for k, v in z.items()))


if __name__ == "__main__":
    main()

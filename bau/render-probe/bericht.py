#!/usr/bin/env python3
"""befunde.md aus ergebnis.json (probe.py) und den Lernblatt-Logs."""
import importlib.util
import json
import pathlib
import re

HIER = pathlib.Path(__file__).resolve().parent
WURZEL = HIER.parents[1]
spec = importlib.util.spec_from_file_location(
    "bp", WURZEL / "werkzeuge" / "bank-pruef.py")
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

# Ursache je Baustein, per Gegenprobe (bau/render-probe/gegenprobe/) bestätigt.
DEUTUNG = [
    "## Deutung", "",
    "Beide Fehlerbilder liegen in den Bankzeilen, nicht in der Vorlage. "
    "Gegenprobe je Fall ein eigenes .tex in gegenprobe/ (6 Läufe, damit 105 Kompilierläufe insgesamt).", "",
    "1. `\\dreieck`: Die Vorlage setzt alle sechs Labels (#4–#9) selbst in "
    "`$…$`. Bankzeilen schreiben `{$62^\\circ$}` – daraus wird `$$62^\\circ$$`, "
    "`^` steht im Textmodus → Abbruch. Ohne `^` gibt es keinen Fehler, aber "
    "falschen Satz: `{$41$ cm}` erscheint als „41cm“ (Leerzeichen weg, cm "
    "kursiv), `{$g$}` als aufrechtes g. Gegenprobe: `{62^\\circ}` und "
    "`{41\\text{ cm}}` setzen richtig. Betroffen: 25 Bankzeilen "
    "(Suche über alle grafik- und loesungsgrafik-Felder): flaechen-e3-k1-s0-v1…v4, "
    "-s3-v1…v3, flaechen-e3-k4-s4-v1 (loesungsgrafik), pythagoras-e1-k1-s0-v2…v4, "
    "-e1-k2-s0-v2…v4, -e1-k2-s2-v1…v3, -e3-k1-s0-v4, -e3-k2-s1-v1…v5, "
    "pythagoras-zone-f3-v2, -v4. bank-pruef.py prüft das nicht.",
    "2. `\\saeulenab`: `ylabel=$P(X = k)$ in \\%` – das `=` im Wert zerlegt "
    "die Option (key=value). Mit Klammern `ylabel={$P(X = k)$ in \\%}` "
    "fehlerfrei; `$P(X \\le k)$` ohne `=` geht auch ohne Klammern. Betroffen: "
    "9 Zeilen, binomialverteilung-e5-k1-s1-v1…v5, -s5-v1, -s5-v2, -e5-k3-s4-v2, "
    "kenngroessen-von-verteilungen-e1-k5-s3-v2. Andere Optionswerte mit `=` "
    "gibt es in der Bank nicht.",
    "3. `\\saeulen` ist selbst fehlerfrei: Die eine Zeile mit Befund "
    "(binomialverteilung-e5-k1-s5-v2) trägt daneben das `\\saeulenab` aus 2.",
    "4. Lernblatt: `↔` fehlt in Latin Modern und bleibt leer – im Titel "
    "„Bruch ↔ Dezimalzahl …“ (prozentrechnung-e1-k1-s4-*, -zone-f2-*). "
    "Kein Abbruch, im PDF fehlt nur das Zeichen.", "",
    "Nicht geprüft: loesungsgrafik-Felder (außer den gezählten Mustern), "
    "Seitenbild und Lage der Grafiken (nur Log, kein Blick aufs PDF).", ""]

GERUEST_ABSCHNITTE = ("Grundgerüst", "Option schwach", "Die Umgebung")


def geruest_namen():
    text = (WURZEL / "mappen" / "_bausteine.md").read_text(encoding="utf-8")
    text = text.split("## Absätze")[0]
    namen, grafik = set(), set()
    for teil in text.split("\n### ")[1:]:
        ziel = namen if teil.startswith(GERUEST_ABSCHNITTE) else grafik
        ziel.update(n for n, _ in bp.aufrufe(teil))
    return namen - grafik


def lernblatt():
    aus = []
    for log in sorted((HIER / "lernblatt").glob("*.log")):
        t = log.read_text(encoding="utf-8", errors="replace")
        seiten = re.search(r"Output written on .*?\((\d+) pages?", t, re.S)
        fehler = len(re.findall(r"^! ", t, re.M))
        fehlt = sorted(set(re.findall(r"Missing character: There is no (\S+ \(U\+\w+\))", t)))
        aus.append(f"| {log.stem}.tex | {seiten.group(1) if seiten else '–'} | "
                   f"{fehler} | {', '.join(fehlt) or '–'} |")
    return aus


def main():
    d = json.loads((HIER / "ergebnis.json").read_text(encoding="utf-8"))
    erg = d["ergebnis"]
    geprueft = [e for e in erg if e[2]]
    gs = geruest_namen()
    ohne = [e for e in erg if not e[2] and e[0] not in gs]
    geruest = [e for e in erg if not e[2] and e[0] in gs]
    sauber = [e for e in geprueft if not any(e[3].values())]
    mit = [e for e in geprueft if any(e[3].values())]

    def anz(n):
        return "\\begin{" + n[6:] + "}" if n.startswith("begin:") else "\\" + n

    z = ["# Render-Probe: Befunde", "",
         "Stand 2026-09-27. xelatex (TeX Live 2023, Ubuntu-Paket) mit "
         "mathblatt.sty = hz-0801/blattbau@36b7b12. Weg und Einrichtung: "
         "werkzeuge/render.md.", "",
         "## Lernblatt Prozentrechnung (Zusammenbau v0.1)", "",
         "bau/prozentrechnung/2026-09-27/lernblatt/, je Datei zwei Läufe; "
         "PDFs in bau/render-probe/lernblatt/.", "",
         "| Datei | Seiten | Fehler | fehlende Zeichen |",
         "| --- | --- | --- | --- |", *lernblatt(), "",
         "## Grafikbausteine", "",
         f"Je Baustein bis zu fünf verschiedene grafik-Felder der Bank, "
         f"reihum über die Einträge; Satz wie im Zusammenbau "
         f"(aufgabe → teile → \\teil, darunter die Grafik). "
         f"Kompilierläufe der Probe: {d['laeufe']} (dazu 16 für Lernblatt "
         f"und Einrichtung). Gezählt: Fehler (`!`), fehlende Zeichen, "
         f"Überbreite über 5 pt. Quelltexte und PDFs in "
         f"bau/render-probe/bausteine/.", "",
         f"- geprüft: {len(geprueft)} Bausteine, "
         f"fehlerfrei {len(sauber)}, mit Befund {len(mit)}",
         f"- Grafikbausteine ohne Bankzeile (nicht prüfbar): {len(ohne)}",
         f"- Gerüstbausteine (aufgabe, teile, feld …): {len(geruest)}, "
         f"stecken nicht in grafik-Feldern; die im Lernblatt benutzten "
         f"sind mit ihm fehlerfrei durchgelaufen", "", *DEUTUNG]

    z += ["## Einzelbefunde", "", "### Mit Befund", ""]
    for n, treffer, ids, bef, notiz in mit:
        schlecht = [i for i in ids if bef.get(i)]
        z.append(f"#### `{anz(n)}` – {len(schlecht)} von {len(ids)} "
                 f"(Bank: {treffer} Zeilen mit dem Baustein)")
        z.append("")
        for i in schlecht:
            b = bef[i]
            erste = [x for x in b if x.startswith("Fehler")][:2] or b[:2]
            z.append(f"- `{i}`: {len(b)} Meldungen; " + " // ".join(
                x.replace("|", "\\|") for x in erste))
        if notiz:
            z.append("- Folgefehler nach der kaputten Zeile bis "
                     "\\end{document} (offene minipage), hier nicht gezählt")
        z.append("")

    z += ["### Fehlerfrei", "",
          ", ".join(f"`{anz(e[0])}` ({len(e[2])})" for e in sauber), "",
          "### Grafikbausteine ohne Bankzeile", "",
          ", ".join(f"`{anz(e[0])}`" for e in ohne), "",
          "### Gerüstbausteine (nicht Gegenstand der Grafikprobe)", "",
          ", ".join(f"`{anz(e[0])}`" for e in geruest), ""]
    (HIER / "befunde.md").write_text("\n".join(z), encoding="utf-8")


if __name__ == "__main__":
    main()

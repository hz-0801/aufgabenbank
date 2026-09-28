#!/usr/bin/env python3
"""bericht.py – baut bau/fokus/bericht.md aus bau.json und ergebnis.json.

Aufruf (aus der Repo-Wurzel, nach render.py):
    python3 bau/fokus/bericht.py
Überlauf: Zahl der „Overfull \\vbox“ in der .log der Aufgaben
(Arbeitskopie von render.py); leere Seiten: Seiten ohne Text außer
Kopf und Fuß (pdftotext).
"""

import collections
import json
import re
import subprocess
from pathlib import Path

HIER = Path(__file__).resolve().parent
ARBEIT = Path("/tmp/claude-0/fokus-arbeit")

# Reihenfolge wie im Auftrag vom 28.09. (MSA 1–18, dann Abitur GK nach Rang)
FOLGE = ["DEZ-P1", "QGL-P1", "PRZ-P1", "TRI-P1", "LIN-P1", "TRI-P2", "WUR-P1",
         "POT-P1", "PRZ-P2", "PRZ-P3", "TRI-P3", "DEZ-P2", "LIN-P2", "LIN-P3",
         "BRU-P1", "TRI-P4", "PRZ-P4", "LGL-P1",
         "PUN-P1", "PUN-P2", "PUN-P3", "GER-P1", "PUN-P4", "PUN-P5", "GRE-P1",
         "GLE-P1", "AEN-P1", "AEN-P2", "VOL-P1", "EXT-P1"]


ENTSCHEIDUNGEN = """## Entscheidungen dieses Laufs

1. MSA: alle 18 Kettennamen stimmen wortgleich mit dem Feld kette der
   genannten Einheit; „p-q-Formel“ liegt in quadratische-gleichungen e3.
   Kein Ersatz nötig.
2. Abitur GK: gezählt je (Eintrag, Einheit, Kette) die Zeilen, die
   zum Profil abitur-gk gehören (`profil_von`, dieselbe Regel wie im
   Heft und im Bau: Papier mit -ga/-gk, sonst Prüfkennung
   „(Abitur … GK)“ im Text), gleich welche hoehe. Nur mit Originalfeld
   gezählt (Papier mit gk/ga oder id mit „grundlegend“) liegen die
   ersten zehn gleich, danach fünf Ketten mit je 11 Zeilen gleichauf
   (tangente-normale-schnittwinkel e4 Winkel, stammfunktion-und-hauptsatz
   e1 Stammfunktion, geraden e1, geraden e3, flaecheninhalt-und-volumen-
   im-raum e4) für zwei Plätze; „Die Rate als Funktion“ (13 Zeilen, davon
   drei nur mit Prüfkennung im Text) fiele heraus. Mit der Bauregel ist
   die Liste ohne Gleichstand und zählt dasselbe, was im Fokus steht.
   Rang: PUN e4 Vierecke nachweisen 27, PUN e3 Dreiecke nachweisen 25,
   PUN e5 Körper und Drehungen 23, geraden e2 Punktprobe 21, PUN e1
   Darstellen und Lage lesen 17, PUN e2 Streckenlänge 17, grenzwerte e2
   Produkte aus Polynom und e-Funktion 15, gleichungen-loesen e1
   Schnittpunkte und Stellen 15, ableitung e4 Die Rate als Funktion 13,
   ableitung e1 Mittlere Änderungsrate 12, flaecheninhalt e4
   Zusammengesetzt und Verhältnisse 12, extremalprobleme e3 Maximum
   bestimmen 12. Fünf der zwölf sind aus punkte-und-strecken-im-
   koordinatensystem.
3. Merkkasten: `--kasten` gab es schon; der Kasten steht in allen 30
   Fokus am Ende (\\uebersichtskasten). Acht Kästen haben mehr als fünf
   Zeilen; sie stehen ungekürzt, mit Kommentar im Quelltext.
4. Zweigzeile: Prüfungswort nur für das Profil des Fokus, gezählt über
   die Typen der Originale dieser Kette (nicht der ganzen Einheit);
   Zeitmarke nur bei MSA.
5. Anlauf: Regel des Hefts. In PUN-P1, PUN-P2, PUN-P3 nur die
   Vorstufe: Grundfall und alle Sprossen dieser Ketten tragen ein
   Original und stehen damit unter den Prüfungsaufgaben.
6. Umfang: sechs Fokus liegen außerhalb von 2–4 Seiten (fünf mit einer
   Seite: wenige Originale, kurze Sachaufgaben; PUN-P4 mit sechs: große
   3D-Koordinatensysteme, Seite 1 bleibt leer, weil Kopf und Anlauf
   zusammen nicht auf eine Seite passen, und Grafiken laufen über den
   Fuß). Nicht nachgebessert: Die Ursache liegt in Bank bzw. Vorlage,
   dieser Auftrag schreibt nur Zusammenbau und bau/.
7. Die Registerzeilen tragen bank_commit b78e6d9 (Commit von
   zusammenbau v0.6 vor dem Bau).
"""


def leere_seiten(pdf, n):
    aus = []
    for i in range(1, (n or 0) + 1):
        t = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), str(pdf),
                            "-"], capture_output=True, text=True).stdout
        rest = [z for z in t.splitlines() if z.strip()
                and "Prüfungs-Fokus" not in z and not z.startswith("Seite")]
        if sum(len(z) for z in rest) < 40:
            aus.append(i)
    return aus


def main():
    erg = json.loads((HIER / "ergebnis.json").read_text(encoding="utf-8"))
    zeilen, je = [], []
    summe = collections.Counter()
    fehlerarten = collections.Counter()
    fehler_wo = collections.defaultdict(list)
    for k in FOLGE:
        b = json.loads((HIER / k / "bau.json").read_text(encoding="utf-8"))
        e = erg[k]
        log = ARBEIT / k / f"{k}.log"
        ueber = (log.read_text(encoding="utf-8", errors="replace")
                 .count("Overfull \\vbox") if log.exists() else None)
        leer = leere_seiten(HIER / k / f"{k}.pdf", e["seiten"])
        summe["seiten"] += e["seiten"] or 0
        summe["loesungen"] += e["seiten_loesungen"] or 0
        summe["anlauf"] += b["anlauf"]
        summe["pruef"] += b["pruefungshoehe"]
        summe["orig"] += len(b["originale"])
        summe["aus"] += len(e["ausgelassen"])
        summe["fz"] += e["fehlende_zeichen"]
        stern = sum(1 for a in b["aufgaben"] if a.get("stern"))
        jahre = ", ".join(j[2:] for j in b["jahrgaenge"])
        zeilen.append(
            f"| {k} | {b['eintraege'][0]} | e{b['einheit']} {b['kette']} | "
            f"{b['anlauf']} | {b['pruefungshoehe']} | {len(b['originale'])} | "
            f"{len(b['jahrgaenge'])} ({jahre}) | {b['pruefwort']} | "
            f"{e['seiten']}+{e['seiten_loesungen']} | {len(e['ausgelassen'])} | "
            f"{e['fehlende_zeichen']}"
            + (f" ({' '.join(e['fehlende_zeichen_art'])})"
               if e["fehlende_zeichen"] else "")
            + f" | {stern} | {b['kasten']} | {ueber}"
            + (f", leer S. {', '.join(map(str, leer))}" if leer else "") + " |")
        art_k = ("Kompilierfehler, Teilaufgabe ausgelassen (Lückensatz: __ "
                 "im Aufgabentext außerhalb Mathe)")
        for a in e["ausgelassen"]:
            fehlerarten[art_k] += 1
            fehler_wo[art_k].append(f"{k} Nr. {a['nr']} {a['id']} "
                                    f"({re.sub(r'[.]$', '', a['grund'])})")
        art_z = "fehlende Zeichen in der Schrift (leer im PDF)"
        if e["fehlende_zeichen_art"]:
            fehlerarten[art_z] += 1
            fehler_wo[art_z].append(f"{k} {' '.join(e['fehlende_zeichen_art'])}")
        if ueber:
            fehlerarten["Überlauf (Overfull \\vbox)"] += 1
            fehler_wo["Überlauf (Overfull \\vbox)"].append(f"{k} ({ueber}×)")
        if leer:
            fehlerarten["leere Seite"] += 1
            fehler_wo["leere Seite"].append(f"{k} S. {leer}")
        if e["seiten"] and not 2 <= e["seiten"] <= 4:
            summe["ausser"] += 1
            je.append(f"{k} {e['seiten']} S.")
        if e["ausgelassen"] or e.get("folgefehler_verschont"):
            pass
    t = []
    t.append("# Prüfungs-Fokus (Rezept P)\n")
    t.append("Stand: siehe Commit „bau/fokus: 30 Prüfungs-Fokus“. Gebaut mit "
             "werkzeuge/zusammenbau.py v0.6 (`--fokus-pruefung`, Rezept P), "
             "Vorlage mathblatt.sty aus hz-0801/blattbau, gerendert mit "
             "bau/fokus/render.py (xelatex, je Dokument zwei Läufe, höchstens "
             "3 Versuche). Diese Datei baut bau/fokus/bericht.py.\n")
    t.append("## Übersicht\n")
    t.append("Anlauf und Prüfungshöhe in Teilaufgaben; Originale: verschiedene "
             "Originalkennungen hinter den Prüfungshöhen; Jahrgänge: "
             "verschiedene Jahre dieser Originale (in Klammern); Zweigzeile: "
             "Prüfungswort im Kopf (Jahrgänge, in denen einer der Typen dieser "
             "Originale im Profil vorkommt, aus den Prüfungskatalogen); Seiten "
             "Aufgaben+Lösungen (pdfinfo); ausgelassen: Teilaufgaben, die "
             "render.py auskommentiert hat; fehlende Zeichen: „Missing "
             "character“ in Aufgaben und Lösungen; ⋆: Teilaufgaben mit "
             "Sternchen; Kasten: Merkkasten der Einheit aus der Mappe; "
             "Überlauf: Overfull \\vbox in den Aufgaben.\n")
    t.append("| Kennung | Eintrag | Kette | Anlauf | Prüfungshöhe | Originale | "
             "Jahrgänge | Zweigzeile | Seiten | ausgelassen | fehlende Zeichen "
             "| ⋆ | Kasten | Überlauf |")
    t.append("| --- | --- | --- | --: | --: | --: | --- | --- | --: | --: | --- "
             "| --: | --- | --- |")
    t += zeilen
    t.append(f"| Summe | | | {summe['anlauf']} | {summe['pruef']} | "
             f"{summe['orig']} | | | {summe['seiten']}+{summe['loesungen']} | "
             f"{summe['aus']} | {summe['fz']} | | | |")
    t.append("")
    t.append(f"Seiten gesamt: {summe['seiten']} Aufgabenseiten und "
             f"{summe['loesungen']} Lösungsseiten, zusammen "
             f"{summe['seiten'] + summe['loesungen']}. Außerhalb von 2–4 Seiten: "
             f"{summe['ausser']} ({'; '.join(je)}).\n")
    t.append("## Die drei häufigsten Fehler\n")
    t.append("Gezählt je Fokus, Kompilierfehler je ausgelassener Teilaufgabe.\n")
    for i, (art, n) in enumerate(fehlerarten.most_common(3), 1):
        t.append(f"{i}. {art}: {n}× – {'; '.join(fehler_wo[art])}")
    t.append("")
    rest = [(a, n) for a, n in fehlerarten.most_common()[3:]]
    if rest:
        t.append("Weitere: " + "; ".join(f"{a} {n}×" for a, n in rest) + ".\n")
    t.append(ENTSCHEIDUNGEN)
    (HIER / "bericht.md").write_text("\n".join(t) + "\n", encoding="utf-8",
                                     newline="\n")
    print("\n".join(t[:3]))


if __name__ == "__main__":
    main()

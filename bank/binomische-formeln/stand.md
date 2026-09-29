# Stand: binomische-formeln

Katalog-Commit: cebfd509ea71ae238b589537bd00b7fc306df06f
(2026-09-28, aus dem Kopf von mappen/binomische-formeln.md)
Datum: 2026-09-29 11:19 (date, UTC)
Grundlage: bank.md fünfte Fassung, werkzeuge/bank-pruef.py v0.8,
Auftragsvorlage 2026-09-29b; Nachzug des Bestands vom 27./28.09.
Endstand Prüfskript: 0 Abweichungen, 0 Warnungen in allen
Dateien, auch mit --katalog (Teil 1 der Mappe als Katalog).
Frühere Stände: git log dieser Datei (Stand 2026-09-27 mit
Nachbesserungen 27. und 28.09.).

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      30         0        14      15        0       1
    e1.jsonl        48         4         5      30        3       6
    e2.jsonl        50         8         5      27        4       6
    e3.jsonl        45         4         5      27        3       6

Pflicht je Einheit: fehler 3, begruenden 3 · Zone fehler 1
(Paar). darstellung und anwendung fehlen (Befund 5).

## Nachzug je Einheit

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         30      0              0          0
    e1           37      0             11          0
    e2           44      0              6          0
    e3           29      7              9          4

Übernommen heißt: Aufgabe wortgleich, nur id, sprosse,
sprosse_text, kette_nr, quelle nachgezogen. Umgeschrieben: e1
Grundfall (Päckchen) und je Einheit die sechs Pflichtzeilen
(Pflichtformen; Zeile fehler v1 nur merkmal); e3 dazu die Sprosse
„kein Binom begründen“ (Urteil zuerst, Schrittnamen). Neu in e3:
Vorstufe mit drei Fragen (4) und Sprosse „Mittelglied prüfen“
(3); entfallen die alte Vorstufe (4).

## Originale je Einheit

- e1: keins; Prüfungshöhe als Zielmarke, original null, 3 Zeilen.
- e2: 2017-OS-K5d, 2022-OS-K3c (je 2 Zeilen, k2 s10).
- e3: keins; Prüfungshöhe als Zielmarke, original null, 3 Zeilen.

## Prüfskript vor der Korrektur

- zone.jsonl: 0 / 0 (unverändert).
- e1.jsonl: 0 / 0.
- e2.jsonl: 1 / 0 – Sperre (x + 5)² (Merkkasten) in der P1-Serie;
  dazu eigene Probe: Kastenzahl 12 in derselben Zeile. Beide
  Glieder getauscht.
- e3.jsonl: 1 / 0 – pruef nicht an der Ergebnisstelle; doppeltes
  Produkt in der Lösung falsch (7x statt 14x) geschrieben.
Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. Grundfall-Päckchen: e1 fester Teil „4x + 3y + 2x“, es wandert
   die y-Zahl; e2 und e3 galten schon als Päckchen (a = x bzw. x²
   fest, es wandert die Zahl) und bleiben wortgleich.
2. Vorstufe e3 (drei Fragen): v1 und v4 „Ist das ein Quadrat?“
   (ja/nein), v2 einkreisen und unterstreichen, v3 streichen; je
   Frage mindestens eine Zeile.
3. Vorstufe e1: sprosse_text ist der neue Katalogtext mit
   „Was mal was?“; die vier Aufgaben bleiben, weil der Handgriff
   gleich ist (Pfeile, nichts ausrechnen).
4. Prüfungshöhe e2: sprosse_text endet jetzt auf „Einheit 2)“
   wie im Katalog; Aufgaben unverändert.
5. P1-Serien nummerieren die Rechnungen (1)–(4); die Lösung nennt
   „Rechnungen 2 und 3“ (wie terme).
6. e3 Sprosse „Mittelglied prüfen“: Antwortgerüst in antwort
   („Wurzeln: __ und __; doppeltes Produkt: __; passt: __“),
   Urteil Ja/Nein als erstes Wort; pruef Wurzel und Vorzahl des
   doppelten Produkts.
7. Die Formelgestalt (2x)² + 2·2x·3 + 3² bleibt Zwischenzeile der
   Lösung, keine eigene Sprosse (Hinweis der Übergabe).

## Befunde

1. Katalog: Die Erkennungsschritte „Was ist a, was ist b?“ und
   „Welche Formel?“ (Zeilen 34, 35) wiederholen den Handgriff der
   e2-Vorstufe „Formel erkennen und a, b einkreisen“ und entfallen;
   „Was mal was?“ und die e3-Schritte stehen jetzt in den
   Vorstufen selbst.
2. Katalog: Die Prüfungshöhe e2 verweist auf
   quadratische-gleichungen.md Einheit 2, die e3-Sprosse
   „Anwendung“ auf Einheit 3 – einer der Verweise ist falsch.
3. Katalog: Vorrat mitten in der Kette (e2 s3, s6 vor den
   P10-tragenden s7–s9); ein Blatt für den Mindeststoff überspringt.
4. Prüfskript: Termlösungen bleiben über eine Zahl prüfbar;
   Gleichwertigkeit von Aufgabe und Lösungsterm prüft es nicht.
5. Katalog: Kein Typ trägt Sachanwendung oder Darstellungswechsel;
   anwendung und darstellung fehlen im ganzen Eintrag.
6. Prüfskript: Ein Zeichenauftrag ohne grafik (e1-Vorstufe
   „Verbinde mit Pfeilen“) wird nicht gemeldet; kein Baustein
   trägt Pfeile zwischen Termgliedern.
7. Auftrag: Die Gegenprobe „Kastenzahlen in keiner aufgabe“ trifft
   „P10“ in der Prüfkennung; hier als nicht getroffen gewertet.

## Offene Punkte

- Schrittnamen nur in neuen und umgeschriebenen Zeilen; der
  übernommene Bestand zeigt reine Ergebnisse.
- LaTeX nicht kompiliert (\rechnung mit Zeilenwechsel, \janein
  am Satzende, Listen mit \\ in der P1-Serie).
- Pfeile über dem gedruckten Term (e1-Vorstufe) mit dem
  Zusammenbau klären.
- Grundvorstellung (Zeile 81) steht nicht in der Bank.

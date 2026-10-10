# Füllauftrag – eine Treppe mit neuen Aufgaben füllen

Stand 10.10.2026 (Lehrer: Aufgabe und Treppe getrennt). Für ganze
Lerneinheiten gilt weiter `bau/bauauftrag.md`; hier entstehen nur
Aufgaben für die Bank.

## Maß

Die Lehrer-Vorlage `bau/proben/2026-10-10/vorlage-holger/` (README und
.tex). So sollen die Aufgaben sein:
- knapper Auftrag, ein Verb vorn („Finde“, „Stelle auf“, „Berechne“);
- die Schwierigkeit steckt in der Figur und den Zahlen, nicht im Text;
- Gegenbeispiel und Falle statt Hinweis: kein Tipp, keine Warnung;
- glatt vor krumm; Lage und Buchstaben wechseln;
- der Schüler tut selbst etwas (einkreisen, notieren, nachschlagen);
- Sache steigend, die stärkste zuletzt; kein fertiges Dreieck mit
  bloßer Geschichte drumherum.
Nicht: Rätsel- oder Herleitungsbilder, Fehler-finden, Kästchen zählen.

## Eingaben (eng lesen)

- Die Treppe `bank/<eintrag>/treppe-e<n>-<name>.md` und die Liste
  `bank/<eintrag>/merkmale.md` (Abschnitt der Einheit) – ganz.
- Die Vorlage – ganz (klein).
- Katalog `mathe-nachhilfe/katalog/<eintrag>.md`: nur „Typische
  Fehler“ und die Zeile der Einheit unter „Typen je Lerneinheit“.
- Alte Bankzeilen nicht lesen; alles ist neu.

## Vorgehen

1. Je Stufe der Treppe so viele Aufgaben, wie Blatt plus Vorrat
   verlangen; jede trägt die Pflichtmerkmale und deckt die Wahlmerkmale
   über die Stufe verteilt ab. Zwei Aufgaben derselben Stufe
   unterscheiden sich in Lage, Buchstaben oder Zahlen sichtbar.
2. Zeilen nach bank.md „Aufgaben ohne Treppe“ in `bank/<eintrag>/a<n>.jsonl`.
   Merkmale nur aus der Liste; fehlt ein Wert, nicht erfinden, sondern
   im Bericht nennen.
3. Jede Zahl und Lösung mit sympy; Skizze passt zu den Zahlen
   (Hypotenuse sichtbar die längste Seite).
4. Probesatz: alle Aufgaben einer Stufe als ein PDF nebeneinander
   (Skript im Arbeitsordner), als Bild ansehen (`pdftoppm -r 60`).
5. `python3 werkzeuge/bank-pruef.py <eintrag>` ohne Meldung für a*.jsonl.

## Bericht (höchstens 200 Wörter)

Aufgaben je Stufe; fehlende Merkmalwerte; Prüfmeldungen; Pfad des
Probesatzes; Commits.

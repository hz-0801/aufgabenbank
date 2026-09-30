# Stand: binomische-formeln

Katalog-Commit: db8d2a3f9f6ed0e6490a4087e3eaff2cbc8a9b19
(2026-09-30, aus dem Kopf von mappen/binomische-formeln.md)
Datum: 2026-09-30 08:44 (date, UTC)
Grundlage: bank.md Stand 2026-09-30b, werkzeuge/bank-pruef.py
v0.12, Auftragsvorlage 2026-09-29e; Nachzug des Stands vom
29.09. nach den Katalogänderungen vom 30.09. (Kopfzeile
„Änderungen 2026-09-30“ des Katalogeintrags).
Endstand Prüfskript: 0 Abweichungen, 0 Warnungen, Formprobe
0 Hinweise in allen Dateien, mit --katalog.
Frühere Stände: git log dieser Datei.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      30         0        14      15        0       1
    e1.jsonl        48         4         5      30        3       6
    e2.jsonl        53         8         5      27        4       9
    e3.jsonl        45         4         5      27        3       6

Pflicht je Einheit: fehler 3, begruenden 3; e2 dazu
darstellung 3 (neu, Typ „Darstellung: Term ↔ Flächenbild“).
Zone fehler 1 (Paar). anwendung fehlt weiter (kein Typ trägt sie).

## Nachzug je Einheit (30.09.)

    Datei  übernommen  neu  umgeschrieben  entfallen
    zone         30      0              0          0
    e1           44      0              4          0
    e2           50      3              0          0
    e3           45      0              0          0

Übernommen heißt: Aufgabe wortgleich; in e2 wurde bei der Sprosse
„dritte Formel“ (3 Zeilen) nur sprosse_text nachgezogen, jetzt
„(kein P10-Stoff)“ statt „(Vorrat: kein P10-Original)“.
Umgeschrieben e1: die vier Vorstufenzeilen „Was mal was?“, nur
der Satz mit den Pfeilen (siehe Entscheidung 1). Neu e2: die drei
darstellung-Zeilen (k4 s3).

## Originale je Einheit

- e1: keins; Prüfungshöhe als Zielmarke, original null, 3 Zeilen.
- e2: 2017-OS-K5d, 2022-OS-K3c (je 2 Zeilen, k2 s10).
- e3: keins; Prüfungshöhe als Zielmarke, original null, 3 Zeilen.

## Prüfskript vor der Korrektur

Bestand vom 29.09. gegen die neue Mappe und Skript v0.12:
- zone.jsonl: 0 / 0.
- e1.jsonl: 4 / 0 – „grafik leer“ bei den vier Vorstufenzeilen
  („Verbinde … mit Pfeilen“ gilt seit v0.9 als Zeichenauftrag).
- e2.jsonl: 3 / 0 – sprosse_text der Sprosse „dritte Formel“ nicht
  mehr wortgleich (Marke geändert).
- e3.jsonl: 0 / 0.
Erster Wurf der drei darstellung-Zeilen: 3 Abweichungen (zwei
pruef-Zahlen nicht an der Ergebnisstelle, merkmal uneinheitlich),
1 Formprobe-Hinweis (nur eine Richtung erkannt); alles in einem
zweiten Durchgang bereinigt. Keine Einheit ist zweimal gescheitert.

## Entscheidungen

1. e1-Vorstufe: Die Schüler ziehen die Pfeile über dem gedruckten
   Term; es gibt keinen Baustein dafür, also bleibt grafik leer.
   Der Satz heißt jetzt „Ziehe Pfeile „jedes mit jedem“: von jedem
   Glied der ersten Klammer zu jedem Glied der zweiten.“ statt
   „Verbinde mit Pfeilen …“, damit das Prüfskript nicht eine Grafik
   verlangt, die keine Vorlage liefert. Sachlich unverändert.
2. Darstellung e2: kein Baustein zeichnet ein zerlegtes Quadrat
   (\rechteck kennt keine Teilung und keine Seitenbeschriftung),
   darum form text ohne grafik; v1 lässt den Schüler skizzieren
   (Term → Bild), v2 gibt die vier Teilflächen in Worten und fragt
   Seite und Klammerquadrat (Bild → Term), v3 gibt Term und
   Zerlegung und lässt die Glieder den Stücken zuordnen (Term →
   Bild, in Worten). Quelle Zeile 20 (Typ), da die Sprossenkette
   den Typ nicht führt.
3. Die darstellung-Zeilen stehen als s3 der Pflichtkette k4 hinter
   fehler (s1) und begruenden (s2), wie in bruchrechnung.
4. „Welche Formel?“ (Zeile 34, jetzt nur „Vor Einheit 2“) und
   „Was ist a, was ist b?“ (Zeile 35) entfallen nach bank.md
   (Erkennungsschritte): die e2-Vorstufe „Formel erkennen und a, b
   einkreisen“ (Zeile 84, k2 s0) trifft dieselbe Entscheidung an
   derselben Vorlage (welche Formel, was ist a und b, nichts
   rechnen); Einheit 2 ist die einzige Einheit des Bereichs.
   „Gleiche Klammer zweimal?“ (Zeile 33) bleibt als k1: andere
   Entscheidung (Quadrat einer Klammer oder nicht).
5. Sprosse „dritte Formel (kein P10-Stoff)“: Zeilen unverändert,
   nur sprosse_text; die Marke steuert den Zusammenbau (bank.md).
6. ids wurden nicht umbenannt; punkte-nachziehen.py nicht nötig.
   Neu: e2-k4-s3-v1 bis v3 (ohne original). Umgeschrieben:
   e1-k1-s0-v1 bis v4 (ohne original).

Frühere Entscheidungen (29.09., Päckchen e1, Vorstufe e3 mit drei
Fragen, Antwortgerüst „Mittelglied prüfen“, Formelgestalt als
Zwischenzeile) gelten weiter; siehe git log.

## Befunde

1. Katalog (Erkennungsschritte, bank.md-Regel): Zeile 34 „Welche
   Formel?“ und Zeile 35 „Was ist a, was ist b?“ gegen Zeile 84
   e2-Vorstufe „Formel erkennen und a, b einkreisen“ – derselbe
   Handgriff, beide Erkennungsschritte stehen nicht in der Bank.
2. Prüfskript / Vorlage: Ein Pfeil-Auftrag über einem gedruckten
   Term (e1-Vorstufe) und ein zerlegtes Quadrat (e2 Darstellung)
   haben keinen Baustein; das Skript verlangt bei „Verbinde“ und
   „Zeichne“ trotzdem eine Grafik. Entweder ein Baustein für Pfeile
   am Term und für das zerlegte Quadrat (Seiten a, b beschriftet,
   vier Teilflächen) oder eine Ausnahme im Skript für Aufträge, die
   der Schüler auf dem Papier über dem Term ausführt.
3. Katalog: Die Prüfungshöhe e2 verweist auf
   quadratische-gleichungen.md Einheit 2, die e3-Sprosse
   „Anwendung“ auf Einheit 3 – einer der Verweise ist falsch
   (unverändert seit 29.09.).
4. Katalog: „zwei Variablen (Vorrat)“ steht weiter mitten in der
   Kette (e2 s6 vor den P10-tragenden s7–s9); ein Blatt für den
   Mindeststoff überspringt.
5. Katalog: Kein Typ trägt eine Sachanwendung; anwendung fehlt im
   ganzen Eintrag (darstellung ist seit 30.09. in e2 gedeckt, in
   e1 und e3 nicht).
6. Prüfskript: Termlösungen bleiben über eine Zahl prüfbar;
   Gleichwertigkeit von Aufgabe und Lösungsterm prüft es nicht.

## Offene Punkte

- Schrittnamen nur in neuen und umgeschriebenen Zeilen; der
  übernommene Bestand zeigt reine Ergebnisse.
- LaTeX nicht kompiliert (\rechnung mit Zeilenwechsel, \janein
  am Satzende, Listen mit \\ in der P1-Serie).
- Pfeile über dem gedruckten Term (e1-Vorstufe) und die Skizze
  des zerlegten Quadrats (e2 Darstellung v1) brauchen Platz auf
  dem Blatt; mit dem Zusammenbau klären.
- Grundvorstellung (Zeile 81) steht nicht in der Bank.

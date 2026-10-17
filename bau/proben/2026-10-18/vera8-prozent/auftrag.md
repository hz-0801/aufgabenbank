# Auftrag: VERA-8-Teilaufgaben als Bankzeilen – Pilot Prozentrechnung

Zweck: Allgemeine Blätter sollen Originalaufgaben ziehen können, ohne
dass ein Modell sie neu schreibt. VERA-8 (IQB) steht unter CC BY 4.0:
Wortlaut darf übernommen werden, mit Quellenangabe. Du überführst die
VERA-Teilaufgaben eines Katalogeintrags in die Zeilenform der Bank.

## Lies (nur das)

1. `/home/claude/aufgabenbank/bank.md` – Abschnitte „Felder je
   Aufgabe“ und „Ablage“ (Form der Zeile).
2. `/home/claude/aufgabenbank/bank/prozentrechnung/e1.jsonl`, nur die
   ersten 3 Zeilen (Beispiel der Form).
3. `/home/claude/mathe-nachhilfe/katalog/prozentrechnung.md` –
   Lerneinheiten, Ketten („Sprossen je Verfahrenstyp“), Sprossen.
4. `/home/claude/aufgabenbank-privat/buecher/vera8/register.csv` – nur
   Zeilen mit einheit „prozentrechnung/…“ (grep), dazu
   `buecher/vera8/stufen.csv` und `buecher/vera8/fehler.csv` für diese
   Kennungen (grep).
5. Je Kennung den Abschnitt „===== <kennung>“ in
   `/home/claude/mathe-nachhilfe/quellen/quelle-fremd-iqb-vera8-pool-l<n>.txt`
   und in `…-l<n>-loesungen.txt` (n = kapitel aus dem Register; grep -n,
   dann gezielt lesen).

## Schreib

Eine Datei `/home/claude/aufgabenbank/bau/proben/2026-10-18/vera8-prozent/prozentrechnung.jsonl`,
eine Zeile je Teilaufgabe, Felder wie bank.md, dazu:

- `aufgabe`: Wortlaut der Teilaufgabe aus dem IQB-Text, mit dem nötigen
  Stamm davor. OCR-Fehler (Umlaute, Zeichen) berichtigen, sonst
  wortgleich; nichts umformulieren.
- `loesung`, `pruef`: aus der Auswertung des IQB; `pruef` so, dass
  `werkzeuge/bank-pruef.py` nachrechnen kann.
- `einheit`, `kette`, `kette_nr`, `sprosse`, `hoehe`: nach dem Katalog
  zugeordnet (passt keine Sprosse genau, die nächste und im Feld
  `merkmal` „VERA, ersatzweise“).
- `herkunft`: „IQB VERA-8 <kennung> Tlg. <nr>, CC BY 4.0“.
- `original`: null.
- `stufe`: AFB und Kompetenzstufe aus stufen.csv („I/2“).
- `fallen`: Liste der Denkfehler aus fehler.csv zu dieser Teilaufgabe
  (Feld `denkfehler`, bei falschwahl mit der Antwort davor), sonst [].
- Braucht die Aufgabe ein Bild, das kein Baustein der Vorlage zeichnen
  kann: `ruht`: „Bild fehlt (Original-Abbildung)“; `bild` ein Wort.
- `id`: „prozentrechnung-e<n>-k<k>-s<s>-vera-<kennung>-<nr>“.

## Prüfen

`python3 /home/claude/aufgabenbank/werkzeuge/bank-pruef.py` auf die
Datei (Aufruf steht im Kopf des Skripts). Fehler beheben, bis es
durchläuft; was nicht geht, im Bericht.

## Grenzen

Nur diese Datei schreiben; keine Bankdatei unter bank/ ändern; keine
Commits. Antwort höchstens 6 Zeilen: Zahl der Zeilen, davon ruhend,
Ergebnis von bank-pruef, Teilaufgaben ohne passende Sprosse.

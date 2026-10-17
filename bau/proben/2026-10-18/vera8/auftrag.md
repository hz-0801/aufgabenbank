# Auftrag: VERA-8-Teilaufgaben als Bankzeilen – Einträge laut Aufruf

Zweck: Allgemeine Blätter sollen Originalaufgaben mit geprüfter Lösung
ziehen können, ohne dass ein Modell sie neu schreibt. VERA-8 (IQB)
steht unter CC BY (Jahrgang ≤ 2013: 3.0, sonst 4.0): Wortlaut darf mit
Quellenangabe übernommen werden. Muster: `../vera8-prozent/` (Pilot).

## Lies (nur das)

1. `/home/claude/aufgabenbank/bank.md` – Abschnitte „Felder je
   Aufgabe“ und „Ablage“.
2. `/home/claude/aufgabenbank/bank/<eintrag>/e1.jsonl`, nur die ersten
   2 Zeilen (Form), falls vorhanden.
3. `/home/claude/mathe-nachhilfe/katalog/<eintrag>.md` – Einheiten,
   Ketten („Sprossen je Verfahrenstyp“), Sprossen.
4. `/home/claude/aufgabenbank-privat/buecher/vera8/register.csv` – nur
   Zeilen, deren einheit mit „<eintrag>/“ beginnt (grep); dazu
   `stufen.csv` und `fehler.csv` dort für diese Kennungen (grep).
5. Je Kennung den WORTLAUT aus dem Original-PDF (Read-Tool, PDF):
   `/home/claude/arbeit/verabuch/pdf5/L<n>/<kennung>_Aufgabe.pdf` und
   die Lösung aus `…/<kennung>_Auswertung.pdf` (n = kapitel im
   Register; liegt die Datei nicht dort, unter L1–L5 suchen). Nicht
   aus OCR-Text abschreiben; nichts erschließen, was nicht dasteht.

## Schreib

Je Eintrag eine Datei
`/home/claude/aufgabenbank/bau/proben/2026-10-18/vera8/<eintrag>.jsonl`,
eine Zeile je Teilaufgabe, Felder wie bank.md, dazu:

- `aufgabe`: Wortlaut der Teilaufgabe mit nötigem Stamm, wortgleich.
- `loesung`, `pruef`: aus der Auswertung; `pruef` so, dass die Prüfung
  unten nachrechnen kann.
- `einheit`, `kette`, `kette_nr`, `sprosse`, `hoehe`: nach dem Katalog;
  passt keine Sprosse genau, die nächste und `merkmal` „VERA, ersatzweise“.
- `herkunft`: „IQB VERA-8 <kennung> Tlg. <nr>, CC BY 3.0|4.0“ (nach Jahrgang).
- `original`: null. `vera_stufe`: aus stufen.csv („I/2“).
- `fallen`: Denkfehler aus fehler.csv zu dieser Teilaufgabe (bei
  falschwahl mit der Antwort in Klammern), sonst [].
- Braucht die Aufgabe ein Bild, das kein Baustein der Vorlage zeichnet:
  `ruht`: „Bild fehlt (Original-Abbildung)“, `bild` ein Wort.
- `id`: „<eintrag>-e<n>-k<k>-s<s>-vera-<kennung>-<nr>“.

## Prüfen

`python3 /home/claude/aufgabenbank/bau/proben/2026-10-18/vera8/vera-pruef.py <eintrag> <datei>`
bis „0 mit Befund“; was nicht geht, im Bericht.

## Grenzen

Nur die eigenen Dateien schreiben; nichts unter bank/ ändern; keine
Commits; Zwischendateien nur in /home/claude/arbeit/vera/bank/<eintrag>/.
Antwort höchstens 6 Zeilen: je Eintrag Zeilen, ruhend, Befunde,
ersatzweise Sprossen.

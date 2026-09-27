# Gegenlese: zinsrechnung

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 165
Korrekturen: 0

## 2 Eindeutig lösbar

- zinsrechnung-e2-k4-s3-v1: Mit „kostet etwa 2 250 €“ ist die Entscheidung bei 2 251,02 € (1,02 € Abstand) nicht eindeutig. – „etwa“ streichen oder die Zahlen so wählen, dass der Abstand deutlich ist.

## 3 Sprosse und Merkmal

- zinsrechnung-zone-f4-v2: Die Aufgabe ist eine Multiplikation (4,20 € · 3), merkmal und Schwestervariante v1 verlangen aber „Euro-Beträge addieren“. – Durch eine Addition zweier Cent-Beträge ersetzen, z. B. 3,40 € + 1,85 €.
- zinsrechnung-zone-f5-v2: „Pro Tag 4 € – 9 Tage“ ist ein reiner fester Faktor ohne Teilschritt, merkmal und v1 verlangen einen Dreisatz mit glattem Teiler (erst teilen, dann malnehmen). – Wie v1 formulieren, z. B. „4 Tage kosten 32 € – wie viel kosten 9 Tage?“.
- zinsrechnung-zone-f8-v2: Die Aufgabe liest nur ein Feld ab (Dienstag nachmittags = 19), merkmal und v1 verlangen, die Tabelle um eine Zeile fortzuschreiben. – Durch eine Tabelle mit fester Zunahme und leerer letzter Zeile ersetzen wie in v1.
- zinsrechnung-e2-k3-s1-v1: Gefragt ist die Rückzahlung (ein Schritt K · qⁿ), die Schwestervarianten v2/v3 und merkmal „Kosten“ fragen nach den Zinsen (Rückzahlung minus Kredit), also nach einem Schritt mehr. – Frage auf „Wie viel Euro Zinsen kostet der Kredit?“ umstellen (Lösung dann 955,08 €).
- zinsrechnung-e2-k4-s3-v2: Eine eingekleidete Startkapital-Rückrechnung (Struktur wie e2-k1-s9-v1) ohne Entscheidung im Kontext; passt weder zum merkmal „Sparziel oder Angebot entscheiden“ noch zum sprosse_text „mal q hoch n“. – Als Entscheidungsfrage stellen, z. B. „Reichen 4 500 € heute, um in 5 Jahren 5 000 € zu haben?“.

## 5 Ankreuzen

- zinsrechnung-e1-k1-s0-v1: Die Frage „Wie viel Euro Zinsen bekommt sie?“ nennt das Gesuchte wortgleich wie die richtige Option, die Distraktoren sind so ohne Nachdenken ausgeschlossen. – Frage ohne das Wort „Zinsen“ stellen, etwa „Wie viel Euro gibt die Bank ihr nach einem Jahr dazu?“.
- zinsrechnung-e1-k1-s0-v2: Die Frage „Wie hoch ist der Zinssatz?“ nennt das Gesuchte wortgleich wie die richtige Option, die Distraktoren sind so ohne Nachdenken ausgeschlossen. – Frage ohne das Wort „Zinssatz“ stellen, etwa „Wie viel Prozent zahlt die Bank?“.

Sauber: 157 Zeilen ohne Befund

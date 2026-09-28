# Regal – Plan aller Kompetenzblätter

Stand 2026-09-28. Gebaut mit `python3 werkzeuge/regal.py` (Anleitung im
Kopf des Skripts). Dateien: regal.csv (eine Zeile je geplantem
Kompetenzblatt), regal.html (eine selbständige Seite, kein externes
Skript: Ansichten „nach Prüfung“ und „nach Klasse und Thema“, Suchfeld,
Filter „nur gebaute“, Link aufs PDF über
raw.githubusercontent.com/hz-0801/aufgabenbank/main/<pfad>), ich-kann.csv
(Titel, gemeinsam mit werkzeuge/zusammenbau.py v0.7).

## Zahlen

424 geplante Kompetenzblätter: 301 Verfahrensketten (Ketten mit
Grundfall) und 123 Einheiten mit Typen ohne Kette (je Einheit ein Blatt,
kette „*“). Kein eigenes Blatt: Erkennungsschritte (nur Vorstufe, 76) und
reine Pflichtketten (272; sie gehören zur gleichnamigen Verfahrenskette).
Sek I 213, Sek II 211. Gebaut: 5 (QGL-K1, POT-K1, LIN-K1, PRZ-K1, TRI-K1).
Ohne Prüfungswort (kein Original in der Kette): 115.

| Prüfungsbereich | Blätter | Verfahrensketten | Typen ohne Kette | mit Prüfungswort |
| --- | --: | --: | --: | --: |
| Abitur GK: Analysis I | 44 | 30 | 14 | 40 |
| Abitur GK: Analysis II | 43 | 32 | 11 | 42 |
| Abitur GK: Geometrie | 63 | 54 | 9 | 61 |
| Abitur GK: Stochastik | 53 | 41 | 12 | 50 |
| MSA: Daten | 22 | 15 | 7 | 13 |
| MSA: Funktionen | 58 | 43 | 15 | 33 |
| MSA: Geometrie | 62 | 36 | 26 | 31 |
| MSA: Zahlen | 79 | 50 | 29 | 39 |

Häufigste P10-Kompetenzen (Jahrgänge, in denen ein Typ der Originale der
Kette vorkommt): DAT-K8: Ich kann Minimum, Maximum, Spannweite, Mittelwert und Median bestimmen. P10 ×12; LIN-K6: Ich kann Funktionswerte einer linearen Funktion berechnen. P10 ×12; WUR-K4: Ich kann Quadratwurzeln ziehen. P10 ×12; TRI-K6: Ich kann in Teildreiecken und bei Vermessungen rechnen. P10 ×12; DAT-K6: Ich kann Anteile in Streifen und Kreis darstellen. P10 ×11.

## Entscheidungen (vom Auftrag nicht geregelt)

1. Kennung: Kürzel aus katalog/_kuerzel.csv, K-Nummer je Eintrag in der
   Folge Bankeinheit → Kette (kette_nr) → zuletzt das Blatt „Typen ohne
   Kette“ der Einheit. Die fünf gebauten Blätter behalten ihre Kennung
   (QGL-K1 ist im Plan die dritte Kette von quadratische-gleichungen);
   die übrigen Nummern zählen um belegte herum. Der Zusammenbau vergibt
   bisher die nächste freie Nummer (höchste + 1); wer nach dem Regal
   baut, gibt `--nummer n` aus regal.csv mit, sonst weichen Plan und
   Register auseinander.
2. Ich-kann-Titel: Der Katalog trägt keine. Alle 424 Titel sind in
   ich-kann.csv aus Kettenname, merkmal des Grundfalls, den Typen ohne
   Kette und der Mappe umformuliert (Spalte quelle „umformuliert …“);
   regal.py meldet fehlende Titel auf der Konsole (Lauf: keiner).
3. einheit: die Katalogeinheit (Nummer und Titel aus der Mappe), gefunden
   wie im Zusammenbau v0.7 über „Sprossen je Verfahrenstyp“; Titel ohne
   Erläuterung nach „:“ oder „(“. Die Nummer der Bankdatei steht daneben
   (einheit_bank), weil beide Zählungen auseinanderlaufen können.
4. klasse_os, klasse_gym aus der Marken-Zeile der Katalogeinheit; Sek II:
   Halbjahr aus „BE Qn“ in klasse_gym. Ohne Marken bleiben beide leer
   (4 Blätter: gleichungen-loesen Einheit 4, matrizen-und-uebergangs-
   prozesse Einheit 5).
5. pruefung: je Profil der Originale der Kette „P10 ×n“, „Abi GK ×n“,
   „Abi LK ×n“, „FHR ×n“ (wie die Zweigzeile, zusammenbau.pruefwort_zahl);
   ein Abitur-Blatt kann mehrere tragen.
6. Prüfungsbereich (Spalte gruppe) nach den Heften in bau/hefte/ (Aufruf-
   zeilen von bau/hefte/bericht.md): msa-funktionen, -geometrie, -daten,
   -zahlen und abi-gk-analysis-1/-2, -stochastik, -geometrie. Einträge in
   keinem Heft nach Leitidee (Analysis → Analysis II, Stochastik,
   Analytische Geometrie → Geometrie; Sek I entsprechend). Sek-II-Ketten
   in Sek-I-Einträgen („Häufigkeiten, Sek II“) bleiben im Bereich des
   Eintrags, tragen aber bereich Sek II.
7. „nach Klasse und Thema“: Klasse = erste Klasse der Oberschule, sonst
   des Gymnasiums; Sek II nach Halbjahr. „nach Prüfung“: im Bereich nach
   der Zahl hinter × absteigend, ohne Prüfungswort zuletzt.
8. Doppelte Kompetenzen über Einträge hinweg (Befund 33: „eine Kompetenz
   steht einmal im Regal“) sind nicht zusammengelegt: gleichlautende Titel
   gibt es z. B. bei „Ich kann eine Vierfeldertafel ausfüllen.“ (daten e7
   und vierfeldertafel e1) und „Ich kann Wahrscheinlichkeiten beim Ziehen
   ohne Zurücklegen berechnen.“ (wahrscheinlichkeit e4 und
   hypergeometrische-verteilung e1) – das
   Zusammenlegen ist eine Katalogentscheidung, keine des Regals.

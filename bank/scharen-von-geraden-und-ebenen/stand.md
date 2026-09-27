# Stand: scharen-von-geraden-und-ebenen

Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08
Datum: 2026-09-27
Prüfskript: werkzeuge/bank-pruef.py v0.5, 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | vorstufe | grundfall | sprosse | pruefung | pflicht | Summe |
|-------|---------:|----------:|--------:|---------:|--------:|------:|
| zone  |        – |        12 |      15 |        – |       1 |    28 |
| e1    |        8 |         5 |      18 |        6 |       6 |    43 |
| e2    |        4 |         5 |      15 |        2 |       6 |    32 |
| e3    |        4 |         5 |       6 |        2 |       6 |    23 |
| e4    |        4 |         5 |      12 |        4 |       6 |    31 |
| alle  |       20 |        32 |      66 |       14 |      25 |   157 |

## Originale je Einheit

- e1: 2024-bebb-lk-B3e, 2018MgrundlegendBAGLAA2WTR1-1e,
  2022-bebb-lk-A1.6a, 2024-bebb-lk-A1.3b, 2024MerhoehtAAGLAA223-a,
  2025-bebb-lk-A1.7b, 2025MerhoehtAAGLAA221-b,
  2025MerhoehtBAGLAA2MMS-1b, 2022MerhoehtAAGLAA222-a,
  2025-bebb-lk-A1.8a; Prüfungshöhe 2025-bebb-lk-A1.8b,
  2023-bebb-lk-A1.5b, 2024-bebb-lk-B3f
- e2: 2024-bebb-lk-A1.3a, 2021MerhoehtAAGLAA213-a, 2023-bebb-lk-B3h,
  2018-bb-ea-B3.2b, 2017-bb-ea-B3.1f; Prüfungshöhe
  2024MerhoehtAAGLAA223-b
- e3: 2018MerhoehtBAGLAA2WTR1-1c, 2026MerhoehtBAGLAA2MMS2-1e,
  2022-bebb-lk-B3d, 2023-bebb-lk-B3j; Prüfungshöhe 2025-bebb-lk-B3e
- e4: 2025-bebb-lk-B3d, 2022-bebb-lk-B3i, 2018MerhoehtBAGLAA2WTR1-1f,
  2023-bebb-lk-B3e, 2023MerhoehtBAGLAA2WTR2-1e, 2024-bebb-lk-B3g;
  Prüfungshöhe 2023-bebb-lk-B3k, 2026MerhoehtBAGLAA2MMS2-1f

## Prüfskript vor der Korrektur

- zone: 0 Abweichungen, 0 Warnungen
- e1: 0 Abweichungen, 0 Warnungen
- e2: 2 Abweichungen (Sperre: Tripel aus einem Original), 0 Warnungen
- e3: 0 Abweichungen, 0 Warnungen
- e4: 0 Abweichungen, 0 Warnungen
- Von Hand nach der Gegenprobe: 7 Zeilen (e1 3, e2 1, e4 3) wegen
  Kastenzahlen 12, 0,5 und 2,5 in aufgabe; 1 Zeile (e1) wegen einer
  Geraden über den ksys3-Bereich hinaus.

## Entscheidungen

- Zone: kette und sprosse_text reichen bis zum Gedankenstrich, nicht
  bis zum Doppelpunkt – die Fertigkeitszeilen trennen mit „–“.
- Zone: ein Fallstrick je Fertigkeit, bei den Gleichungen im
  Parameter zwei (Betrag, Vorzeichenfall); Zone-Paar bei den
  Paarregeln (Skalarprodukt null statt Kollinearität).
- Zone-Reihenfolge nach erster Verwendung: Gleichungen im Parameter
  („alle Einheiten“) vor Winkeln (e3) und Körperschnitten (e4).
- Pflichtelemente nur fehler und begruenden: die Typen nennen unter
  „Dazu“ nur diese; Anwendung und Darstellung tragen sie nicht.
- Originale an Kettensprossen: je Original eine Variante mit Kennung
  im Feld original und Prüfkennung im Text.
- Wortgleiche Pooldubletten zählen als ein Original; die
  Prüfungshöhe trägt zweimal die Landesheft-Kennung (e1: 3 Originale,
  6 Zeilen; e4: 2 Originale, 4 Zeilen).
- Kettensprossen, deren Katalog-Originale nicht in Abschnitt 2 der
  Mappe stehen (e2 s3, s6; e4 s2), tragen original null.
- sprosse_text von Vorstufe und Prüfungshöhe ohne die Klammerbelege
  des Katalogs.
- Der Scharparameter heißt in allen Einheiten k (Originale: a, t, d,
  m), Geradenparameter r und s.
- Rechnerergebnisse (Wurzeln, gerundet) nur in e3, wo der Bestand
  Teil B mit Rechner prüft.

## Befunde

- Katalog: „Für alle oder für eins?“ und „Beispiel oder Beweis?“
  (Zeilen 38, 40) sind zugleich die Vorstufe der Kette e1 (Zeile 98);
  die Erkennungsschritte entfallen in e1.
- Katalog: „Wo sind die Übergänge?“ (Zeile 41) ist zugleich die
  Vorstufe der Kette e4 (Zeile 101); der Erkennungsschritt entfällt.
- Katalog: „Was wählt der Parameter?“ steht als Erkennungsschritt in
  e1 (Zeile 39) und als Vorstufe in e2 (Zeile 99) – derselbe Handgriff
  zweimal; bank.md regelt den Fall nur innerhalb einer Einheit.
- Katalog: Zeilen 27 und 107 nennen einen Nachzug „2026-09-28“, der
  nach dem Katalog-Commit (26.09.) liegt.
- Katalog: Zeile 106 zählt „13 der 22 Zeilen“, der Abschnitt nennt
  23 abi-Zeilen.
- bank.md: „bis zum Doppelpunkt“ passt nicht auf Fertigkeitszeilen
  mit Doppelpunkten in der Klammer (Zeile 32).
- bank.md und Prüfskript: „2 je Original“ zählt wortgleiche
  Pooldubletten als eigene Originale; Dubletten sind nicht geregelt.
- Prüfskript: die Sperrprobe erfasst einzelne mehrstellige
  Kastenzahlen (12, 0,5, 2,5) nicht, die Gegenprobe verlangt es.
- Prüfskript: der Parameterbereich von \rgerade wird nicht gegen den
  ksys3-Bereich geprüft.

## Offene Punkte

- Schnittfiguren im Schrägbild haben keine loesungsgrafik; die
  Vorlage kennt keinen Vieleck-Baustein für ksys3.
- Die Zone übt „Schrägbilder lesen“ nicht eigens; die Körperaufgaben
  in e4 nennen die Koordinaten im Text.

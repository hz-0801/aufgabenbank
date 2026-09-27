# Stand: unabhaengigkeit

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25,
aus dem Kopf der Mappe)
Datum: 2026-09-27 15:23 UTC
Prüfskript: bank-pruef.py v0.5, am Ende 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     26 |        – |        12 |      13 |        – |       1 |
| e1    |     39 |        8 |         5 |      12 |        2 |      12 |
| e2    |     34 |        4 |         5 |      12 |        4 |       9 |
| e3    |     17 |        4 |         5 |       – |        2 |       6 |
| Summe |    116 |       16 |        27 |      37 |        8 |      28 |

## Originale je Einheit

- E1: 2024-bebb-gk-B4.1d (Grundfall), 2024-B-3e und 2026-C-3e (s2,
  fhr-Kette), 2019-be-gk-B4.1d (s3), 2022-bebb-gk-B4i (s4),
  2018MerhoehtAStochastik12-b und 2023MerhoehtBStochastikWTR1-2 (s5),
  2022-bebb-lk-B4c (Prüfung, 2 Zeilen)
- E2: 2023-bebb-lk-B4e (Grundfall), 2021MerhoehtAStochastik11-b (s2),
  2023MerhoehtAStochastik12-b (s3), 2024-bebb-lk-A1.9b (s5),
  2025-bebb-lk-A1.10a und 2025MerhoehtAStochastik23 (Prüfung, je 2)
- E3: 2017MerhoehtAStochastik11-c (Grundfall), 2021-be-gk-B4c
  (Prüfung, 2 Zeilen)

## Prüfskript vor der Korrektur

| Datei | Abweichungen | Warnungen | häufigster Grund |
|-------|-------------:|----------:|------------------|
| zone  |            0 |         0 | – |
| e1    |            1 |         0 | pruef-Zahl nicht an der Ergebnisstelle |
| e2    |            1 |         0 | pruef-Zahl nicht an der Ergebnisstelle |
| e3    |            1 |         0 | pruef fehlt (Ziffer in einer Begründung) |

Dazu zwei Korrekturen, die das Skript nicht meldet: in e2 (k1-s2-v3)
ein Randeintrag der Parametertafel, der nicht zur Spaltensumme passte;
in e1 vor dem Commit drei Grundfall-Tafeln mit gleichen Rändern
entzerrt.

## Entscheidungen

1. Zone: kette und sprosse_text enden am Gedankenstrich der
   Fertigkeitszeile; Folge nach erster Verwendung (Tafel, bedingte
   Wahrscheinlichkeit, Anteile: E1; Pfadterme, Gleichungen: E2;
   Pfadregeln: E3), quelle bleibt die Katalogzeile.
2. Zone-Paar in der Fertigkeit „Vierfeldertafel füllen“ zum
   Kernfehlmuster der fhr-Kette (bedingter Anteil auf die falsche
   Gesamtheit bezogen).
3. Der Erkennungsschritt „Prüfen oder nutzen?“ steht als eigene Kette
   k1 in E1 (4 Zeilen); in E2 ist er die Vorstufe der Kette und
   bleibt dort als Vorstufe.
4. Die Vorstufe von E1 trägt beide Ankreuzfragen des Katalogs in
   einer Sprosse (je zwei Zeilen „drei Zahlen“ und „unabhängig oder
   unvereinbar“), da der Katalog sie als eine Vorstufe führt.
5. Originale stehen an der Sprosse, die sie nennt (auch am Grundfall
   und mitten in der Kette, je eine Zeile); die Prüfungshöhe trägt nur
   ihre eigenen Originale, je 2 Zeilen – E2 hat zwei (Pooldublette),
   also 4 Zeilen.
6. Prüfkennung: fhr als „(FHR Jahr)“ mit papier B bzw. C wie in der
   Mappe; be-gk und bebb-gk als GK; bebb-lk und iqb erhöht als LK.
7. E1 hat alle vier Pflichtelemente (darstellung als Wechsel Tafel,
   Baum, Text; anwendung mit Entscheidung im Kontext); E2 fehler,
   begruenden, anwendung (kein Typ trägt einen Darstellungswechsel);
   E3 nur fehler und begruenden (reiner Deutungstyp).
8. Vierfeldertafeln stehen in grafik (\vierfeldertafel), gefüllte
   Tafeln der Lösung in loesungsgrafik; Tafellösungen als Zahlenliste
   mit Zeilen- und Spaltenangabe.
9. E3-Lösungen ohne Ziffern (Wahrscheinlichkeiten in Worten), damit
   pruef leer bleiben kann.
10. Parametertafeln (E2 s2) tragen Terme in p als Tafeleinträge.

## Befunde

- Katalog: Die Erkennungsschritte „Welche drei Zahlen braucht die
  Produktregel?“ und „Unabhängig oder unvereinbar?“ (Z. 35–36) sind
  wortgleich die Vorstufe der Kette „Unabhängigkeit prüfen“ (Z. 79);
  sie entfallen, der Katalog führt beide.
- Katalog: Der Erkennungsschritt „Prüfen oder nutzen?“ (Z. 37) ist
  zugleich die Vorstufe der Kette „Rückwärts“ (Z. 80); er steht hier
  in E1 als Kette und in E2 als Vorstufe.
- Katalog: Die Sprossen der E1-Kette nennen elf Originale, von denen
  fünf nicht in Abschnitt 2 der Mappe stehen (2023-A-3e, 2025-A-3d,
  2018MerhoehtBStochastikWTR2-1c und weitere); original bleibt dort
  null.
- Prüfskript: Relationen in Lösungen (<, >, ≠) und die Randsummen einer
  Vierfeldertafel werden nicht geprüft; beide Fehler traten auf und
  wurden von Hand gefunden.
- Gegenprobe Kastenzahlen: der Merkkasten trägt sein Zahlenbeispiel in
  Zahlwörtern, Ist 0.

## Offene Punkte

- \vierfeldertafel mit Termen in p und mit Prozentangaben als
  Einträgen ist nicht gerendert geprüft.
- Die Ankreuzoptionen mit Termen in p (Zone f4, E2 s0) sind in
  Mathe-Modus gesetzt; Rendering im Zusammenbau prüfen.

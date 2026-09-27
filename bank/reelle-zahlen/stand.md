# Stand: reelle-zahlen

Katalog-Commit: 99da6894e7ec588195ab9928aa32d68f2b09c9fa
(2026-09-25, katalog/reelle-zahlen.md)
Datum: 2026-09-27 12:17 UTC
Prüfskript: werkzeuge/bank-pruef.py, 0 Abweichungen, 0 Warnungen

## Zeilen

| Datei       | Zeilen | vorst. | grundf. | sprosse | pruef. | pflicht |
|-------------|-------:|-------:|--------:|--------:|-------:|--------:|
| zone.jsonl  |     33 |      0 |      14 |      18 |      0 |       1 |
| e1.jsonl    |     54 |      4 |       5 |      30 |      3 |      12 |
| e2.jsonl    |     54 |      4 |       5 |      33 |      3 |       9 |
| e3.jsonl    |     54 |      4 |       5 |      30 |      3 |      12 |

## Originale je Einheit

- Einheit 1: 2014-OS-B1h (Sprosse 6), 2025-OS-K5c (Sprosse 7)
- Einheit 2: keins
- Einheit 3: 2022-OS-K2d (Sprosse 2), 2026-FOR-K4a (Sprosse 5)

Prüfungshöhe aller drei Einheiten: Zielmarke ohne Original
(hoehe pruefung, original null, 3 Zeilen).

## Prüfskript vor der Korrektur

| Datei      | Abw. | Warn. | häufigster Grund                  |
|------------|-----:|------:|-----------------------------------|
| zone.jsonl |    9 |     0 | merkmal uneinheitlich (6)         |
| e1.jsonl   |    0 |     0 | –                                 |
| e2.jsonl   |    6 |     0 | pruef fehlt (6); danach 1 weitere |
| e3.jsonl   |    2 |     0 | pruef fehlt (1), \ell (1)         |

e2 brauchte zwei Korrekturrunden (zweite: Ergebnisstelle nach
„das sind“); keine Einheit blieb liegen.

## Entscheidungen

1. Nebenleistungs-Originale stehen an der Kettensprosse, die sie
   verlangen (Feld original); die Prüfungshöhe bleibt Zielmarke,
   weil der Katalog kein Original als Hauptleistung nennt.
2. 2015-OS-K3c (Einheit 2) ist nicht verfremdet: Es braucht
   Zehnerpotenzen, und 10 ist Kastenzahl (10⁴ : 5⁴).
3. Darstellung entfällt in Einheit 2; die Typen der Einheit
   tragen keinen Darstellungswechsel außerhalb der Kette.
4. sprosse_text der Pflichtelemente: Fehler und Begründen aus der
   Typenzeile, Darstellung und Anwendung nach dem Typ, auf dem
   sie aufsetzen (Zeilen 19–21).
5. Zone-Reihenfolge: Einheit 1 nach Lehrplanfolge (Brüche,
   Zahlengerade, Quadratwurzel), Taschenrechner ohne Thema
   zuletzt; dann Terme vor Potenz; dann Bruchrechnung.
6. Zone-Fertigkeiten ohne Doppelpunkt heißen bis „– Einheit“.
7. Zone-Paar zum Fallstrick negative Hochzahl (Fertigkeit 6).
8. Die Marken „(4×)“ und „(Vorstufe)“ stehen nicht im
   sprosse_text; sonst ist er wortgleich.
9. Potenzergebnisse tragen Zahlenwert oder Vorzahl, damit pruef
   greift; reine Variablenpotenzen haben pruef "".
10. Sprosse „Zahlbereiche einordnen“ nur als Tabelle; für ein
    Venn-Diagramm gibt es keinen Baustein.

## Befunde

- Katalog: Alle fünf Erkennungsschritte (Z. 33–37) verlangen
  denselben Handgriff wie die Vorstufen (Z. 80–82); sie
  entfallen, die Vorstufen bleiben.
- Prüfskript: Exponenten zählen nicht als Zahl (5^{11} ergibt
  nur 5, x^{7} „ohne Zahl“), der Wurzelexponent in \sqrt[3]
  dagegen schon; Potenzergebnisse sind so nicht prüfbar.
- Prüfskript: \ell fehlt in der Liste erlaubter LaTeX-Befehle.
- Auftrag/bank.md: Die Kastenzahlregel sperrt mit 10 jede
  Zehnerpotenz und damit das einzige Potenzgesetz-Original.

## Offene Punkte

- Einheit 2 hat kein Original; 2015-OS-K3c bliebe verfremdbar,
  wenn Zehnerpotenzen von der Kastenzahlregel ausgenommen würden.
- Venn-Diagramm-Baustein fehlt in der Vorlage.

## Nachbesserung 2026-09-27

Prüfskript v0.5, bank.md Stand 2026-09-27b. Vorher und nachher 0
Abweichungen, 0 Warnungen in allen vier Dateien; keine Zeile
geändert oder gestrichen.

- Prüfungshöhe ohne Original: e1, e2, e3 stehen schon als hoehe
  pruefung, original null, 3 Zeilen; nichts nachzuziehen.
- Erkennungsschritte: alle fünf sind schon entfallen (Befund
  Katalog); keine Kette zu streichen.
- Befunde „Exponenten zählen nicht als Zahl“ und „\ell fehlt“ gegen
  v0.5 geprüft: beide bestehen fort und bleiben offen.

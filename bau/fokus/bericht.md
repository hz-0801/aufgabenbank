# Prüfungs-Fokus (Rezept P)

Stand: siehe Commit „bau/fokus: 30 Prüfungs-Fokus“. Gebaut mit werkzeuge/zusammenbau.py v0.6 (`--fokus-pruefung`, Rezept P), Vorlage mathblatt.sty aus hz-0801/blattbau, gerendert mit bau/fokus/render.py (xelatex, je Dokument zwei Läufe, höchstens 3 Versuche). Diese Datei baut bau/fokus/bericht.py.

## Übersicht

Anlauf und Prüfungshöhe in Teilaufgaben; Originale: verschiedene Originalkennungen hinter den Prüfungshöhen; Jahrgänge: verschiedene Jahre dieser Originale (in Klammern); Zweigzeile: Prüfungswort im Kopf (Jahrgänge, in denen einer der Typen dieser Originale im Profil vorkommt, aus den Prüfungskatalogen); Seiten Aufgaben+Lösungen (pdfinfo); ausgelassen: Teilaufgaben, die render.py auskommentiert hat; fehlende Zeichen: „Missing character“ in Aufgaben und Lösungen; ⋆: Teilaufgaben mit Sternchen; Kasten: Merkkasten der Einheit aus der Mappe; Überlauf: Overfull \vbox in den Aufgaben.

| Kennung | Eintrag | Kette | Anlauf | Prüfungshöhe | Originale | Jahrgänge | Zweigzeile | Seiten | ausgelassen | fehlende Zeichen | ⋆ | Kasten | Überlauf |
| --- | --- | --- | --: | --: | --: | --- | --- | --: | --: | --- | --: | --- | --- |
| DEZ-P1 | brueche-dezimalzahlen | e1 Anteil bestimmen | 3 | 18 | 9 | 9 (14, 17, 19, 21, 22, 23, 24, 25, 26) | P10 ×9 | 3+2 | 0 | 0 | 0 | 5 Zeilen | 1 |
| QGL-P1 | quadratische-gleichungen | e3 p-q-Formel | 3 | 14 | 7 | 7 (17, 20, 21, 22, 23, 24, 25) | P10 ×7 | 2+1 | 0 | 8 (₁ ₂ ≈) | 14 | 4 Zeilen | 0 |
| PRZ-P1 | prozentrechnung | e1 Umwandeln | 2 | 12 | 6 | 6 (17, 19, 20, 21, 22, 23) | P10 ×6 | 3+1 | 0 | 0 | 2 | 4 Zeilen | 1 |
| TRI-P1 | trigonometrie | e4 Sinussatz | 3 | 14 | 8 | 8 (14, 15, 18, 19, 20, 21, 24, 25) | P10 ×9 | 2+1 | 0 | 18 (α β γ ≈) | 14 | 4 Zeilen | 0 |
| LIN-P1 | lineare-funktionen | e3 Funktionswert | 2 | 16 | 8 | 6 (17, 19, 21, 22, 23, 26) | P10 ×12 | 3+1 | 0 | 0 | 0 | 3 Zeilen | 1 |
| TRI-P2 | trigonometrie | e1 Seite berechnen | 3 | 19 | 10 | 7 (17, 18, 19, 20, 21, 22, 25) | P10 ×11 | 4+1 | 0 | 13 (α ≈) | 0 | 5 Zeilen | 2 |
| WUR-P1 | potenzen-wurzeln | e3 Quadratwurzeln | 3 | 15 | 7 | 6 (14, 15, 20, 22, 24, 25) | P10 ×12 | 2+1 | 0 | 1 (≈) | 6 | 4 Zeilen | 0 |
| POT-P1 | potenz-exponentialfunktionen | e3 Wert und Schwellenwert berechnen | 3 | 10 | 5 | 5 (16, 17, 18, 20, 25) | P10 ×7 | 1+1 | 0 | 11 (ᵗ ⁴ ₀ ≈) | 6 | 4 Zeilen | 0 |
| PRZ-P2 | prozentrechnung | e5 Veränderung | 3 | 12 | 6 | 6 (15, 16, 22, 24, 25, 26) | P10 ×7 | 1+1 | 0 | 0 | 0 | 5 Zeilen | 0 |
| PRZ-P3 | prozentrechnung | e2 Prozentsatz | 3 | 10 | 5 | 5 (14, 15, 18, 23, 25) | P10 ×5 | 1+1 | 0 | 0 | 0 | 2 Zeilen | 0 |
| TRI-P3 | trigonometrie | e3 Teildreiecke und Vermessung | 3 | 12 | 6 | 6 (15, 16, 18, 20, 23, 26) | P10 ×12 | 3+1 | 0 | 10 (≈) | 2 | 5 Zeilen | 0 |
| DEZ-P2 | brueche-dezimalzahlen | e5 Vergleichen und Ordnen | 3 | 10 | 5 | 5 (14, 15, 18, 20, 23) | P10 ×8 | 1+1 | 2 | 2 (≈) | 0 | 4 Zeilen | 0 |
| LIN-P2 | lineare-funktionen | e5 Anwendung | 3 | 18 | 9 | 4 (16, 21, 22, 23) | P10 ×6 | 3+1 | 0 | 0 | 6 | 2 Zeilen | 1 |
| LIN-P3 | lineare-funktionen | e2 Ablesen | 2 | 10 | 5 | 4 (16, 19, 24, 25) | P10 ×4 | 3+1 | 0 | 0 | 0 | 3 Zeilen | 1 |
| BRU-P1 | bruchrechnung | e1 Addieren/Subtrahieren | 3 | 12 | 6 | 5 (14, 15, 17, 20, 26) | P10 ×10 | 2+1 | 0 | 0 | 8 | 3 Zeilen | 0 |
| TRI-P4 | trigonometrie | e2 Winkel berechnen | 3 | 12 | 6 | 5 (19, 22, 24, 25, 26) | P10 ×9 | 3+1 | 0 | 18 (α β ⁻ ≈) | 0 | 5 Zeilen | 1 |
| PRZ-P4 | prozentrechnung | e3 Prozentwert | 2 | 10 | 5 | 5 (14, 17, 19, 21, 26) | P10 ×7 | 1+1 | 0 | 0 | 0 | 2 Zeilen | 0 |
| LGL-P1 | lineare-gleichungen | e4 Aufstellen | 2 | 8 | 4 | 4 (16, 18, 20, 21) | P10 ×7 | 3+1 | 0 | 0 | 2 | 3 Zeilen | 0 |
| PUN-P1 | punkte-und-strecken-im-koordinatensystem | e4 Vierecke nachweisen | 1 | 27 | 15 | 8 (18, 19, 20, 21, 22, 23, 25, 26) | Abi GK ×9 | 2+1 | 0 | 3 (∘ ≠) | 0 | 5 Zeilen | 0 |
| PUN-P2 | punkte-und-strecken-im-koordinatensystem | e3 Dreiecke nachweisen | 1 | 25 | 11 | 6 (18, 19, 20, 22, 23, 24) | Abi GK ×7 | 2+1 | 0 | 0 | 0 | 6 Zeilen (über fünf) | 0 |
| PUN-P3 | punkte-und-strecken-im-koordinatensystem | e5 Körper und Drehungen | 1 | 23 | 10 | 6 (18, 19, 20, 23, 24, 26) | Abi GK ×7 | 3+1 | 0 | 0 | 0 | 5 Zeilen | 0 |
| GER-P1 | geraden | e2 Punktprobe und Punkte auf der Geraden | 2 | 21 | 7 | 5 (18, 19, 20, 23, 26) | Abi GK ×7 | 2+1 | 0 | 8 (✓) | 0 | 7 Zeilen (über fünf) | 0 |
| PUN-P4 | punkte-und-strecken-im-koordinatensystem | e1 Darstellen und Lage lesen | 3 | 17 | 8 | 5 (18, 19, 24, 25, 26) | Abi GK ×6 | 6+8 | 0 | 1 (′) | 0 | 5 Zeilen | 4, leer S. 1 |
| PUN-P5 | punkte-und-strecken-im-koordinatensystem | e2 Streckenlänge, Mittelpunkt, Teilpunkte | 3 | 17 | 7 | 6 (18, 19, 20, 23, 24, 26) | Abi GK ×6 | 2+1 | 0 | 7 (₁ ₂ ₃ ≈) | 0 | 6 Zeilen (über fünf) | 0 |
| GRE-P1 | grenzwerte-und-verhalten-im-unendlichen | e2 Produkte aus Polynom und e-Funktion | 2 | 15 | 9 | 7 (18, 19, 20, 21, 22, 23, 25) | Abi GK ×7 | 2+1 | 0 | 0 | 0 | 8 Zeilen (über fünf) | 0 |
| GLE-P1 | gleichungen-loesen | e1 Schnittpunkte und Stellen | 2 | 15 | 6 | 3 (18, 19, 20) | Abi GK ×4 | 2+1 | 0 | 12 (⁴ ⁿ ₁ ⇔ ≥) | 0 | 8 Zeilen (über fünf) | 0 |
| AEN-P1 | ableitung-und-aenderungsrate | e4 Die Rate als Funktion | 3 | 13 | 8 | 4 (18, 19, 22, 26) | Abi GK ×5 | 2+1 | 0 | 17 (⇔) | 0 | 8 Zeilen (über fünf) | 0 |
| AEN-P2 | ableitung-und-aenderungsrate | e1 Mittlere Änderungsrate | 3 | 12 | 10 | 4 (18, 19, 25, 26) | Abi GK ×5 | 2+1 | 0 | 0 | 0 | 7 Zeilen (über fünf) | 0 |
| VOL-P1 | flaecheninhalt-und-volumen-im-raum | e4 Zusammengesetzt und Verhältnisse | 3 | 12 | 8 | 5 (18, 21, 22, 23, 26) | Abi GK ×5 | 3+1 | 0 | 0 | 0 | 6 Zeilen (über fünf) | 1 |
| EXT-P1 | extremalprobleme | e3 Maximum bestimmen | 3 | 12 | 6 | 5 (18, 19, 21, 22, 24) | Abi GK ×7 | 2+1 | 0 | 8 (ℓ ⇔) | 0 | 5 Zeilen | 0 |
| Summe | | | 76 | 441 | 222 | | | 71+38 | 2 | 137 | | | |

Seiten gesamt: 71 Aufgabenseiten und 38 Lösungsseiten, zusammen 109. Außerhalb von 2–4 Seiten: 6 (POT-P1 1 S.; PRZ-P2 1 S.; PRZ-P3 1 S.; DEZ-P2 1 S.; PRZ-P4 1 S.; PUN-P4 6 S.).

## Die drei häufigsten Fehler

Gezählt je Fokus, Kompilierfehler je ausgelassener Teilaufgabe.

1. fehlende Zeichen in der Schrift (leer im PDF): 15× – QGL-P1 ₁ ₂ ≈; TRI-P1 α β γ ≈; TRI-P2 α ≈; WUR-P1 ≈; POT-P1 ᵗ ⁴ ₀ ≈; TRI-P3 ≈; DEZ-P2 ≈; TRI-P4 α β ⁻ ≈; PUN-P1 ∘ ≠; GER-P1 ✓; PUN-P4 ′; PUN-P5 ₁ ₂ ₃ ≈; GLE-P1 ⁴ ⁿ ₁ ⇔ ≥; AEN-P1 ⇔; EXT-P1 ℓ ⇔
2. Überlauf (Overfull \vbox): 9× – DEZ-P1 (1×); PRZ-P1 (1×); LIN-P1 (1×); TRI-P2 (2×); LIN-P2 (1×); LIN-P3 (1×); TRI-P4 (1×); PUN-P4 (4×); VOL-P1 (1×)
3. Kompilierfehler, Teilaufgabe ausgelassen (Lückensatz: __ im Aufgabentext außerhalb Mathe): 2× – DEZ-P2 Nr. 2h brueche-dezimalzahlen-e5-k2-s9-v8 (LaTeX Error: Command \item invalid in math mode); DEZ-P2 Nr. 2g brueche-dezimalzahlen-e5-k2-s9-v7 (Missing $ inserted)

Weitere: leere Seite 1×.

## Entscheidungen dieses Laufs

1. MSA: alle 18 Kettennamen stimmen wortgleich mit dem Feld kette der
   genannten Einheit; „p-q-Formel“ liegt in quadratische-gleichungen e3.
   Kein Ersatz nötig.
2. Abitur GK: gezählt je (Eintrag, Einheit, Kette) die Zeilen, die
   zum Profil abitur-gk gehören (`profil_von`, dieselbe Regel wie im
   Heft und im Bau: Papier mit -ga/-gk, sonst Prüfkennung
   „(Abitur … GK)“ im Text), gleich welche hoehe. Nur mit Originalfeld
   gezählt (Papier mit gk/ga oder id mit „grundlegend“) liegen die
   ersten zehn gleich, danach fünf Ketten mit je 11 Zeilen gleichauf
   (tangente-normale-schnittwinkel e4 Winkel, stammfunktion-und-hauptsatz
   e1 Stammfunktion, geraden e1, geraden e3, flaecheninhalt-und-volumen-
   im-raum e4) für zwei Plätze; „Die Rate als Funktion“ (13 Zeilen, davon
   drei nur mit Prüfkennung im Text) fiele heraus. Mit der Bauregel ist
   die Liste ohne Gleichstand und zählt dasselbe, was im Fokus steht.
   Rang: PUN e4 Vierecke nachweisen 27, PUN e3 Dreiecke nachweisen 25,
   PUN e5 Körper und Drehungen 23, geraden e2 Punktprobe 21, PUN e1
   Darstellen und Lage lesen 17, PUN e2 Streckenlänge 17, grenzwerte e2
   Produkte aus Polynom und e-Funktion 15, gleichungen-loesen e1
   Schnittpunkte und Stellen 15, ableitung e4 Die Rate als Funktion 13,
   ableitung e1 Mittlere Änderungsrate 12, flaecheninhalt e4
   Zusammengesetzt und Verhältnisse 12, extremalprobleme e3 Maximum
   bestimmen 12. Fünf der zwölf sind aus punkte-und-strecken-im-
   koordinatensystem.
3. Merkkasten: `--kasten` gab es schon; der Kasten steht in allen 30
   Fokus am Ende (\uebersichtskasten). Acht Kästen haben mehr als fünf
   Zeilen; sie stehen ungekürzt, mit Kommentar im Quelltext.
4. Zweigzeile: Prüfungswort nur für das Profil des Fokus, gezählt über
   die Typen der Originale dieser Kette (nicht der ganzen Einheit);
   Zeitmarke nur bei MSA.
5. Anlauf: Regel des Hefts. In PUN-P1, PUN-P2, PUN-P3 nur die
   Vorstufe: Grundfall und alle Sprossen dieser Ketten tragen ein
   Original und stehen damit unter den Prüfungsaufgaben.
6. Umfang: sechs Fokus liegen außerhalb von 2–4 Seiten (fünf mit einer
   Seite: wenige Originale, kurze Sachaufgaben; PUN-P4 mit sechs: große
   3D-Koordinatensysteme, Seite 1 bleibt leer, weil Kopf und Anlauf
   zusammen nicht auf eine Seite passen, und Grafiken laufen über den
   Fuß). Nicht nachgebessert: Die Ursache liegt in Bank bzw. Vorlage,
   dieser Auftrag schreibt nur Zusammenbau und bau/.
7. Die Registerzeilen tragen bank_commit b78e6d9 (Commit von
   zusammenbau v0.6 vor dem Bau).


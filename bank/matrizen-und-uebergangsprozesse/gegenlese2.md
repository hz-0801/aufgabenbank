# Zweitlesung matrizen-und-uebergangsprozesse

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 215
(zone 27, e1 34, e2 36, e3 37, e4 39, e5 42)

Prüfung: Alle 215 Zeilen einzeln gelesen (Skript-Ausgabe je Zeile
mit id, Sprosse, Merkmal, Höhe, Form, Aufgabe, Antwort, Lösung,
pruef, Grafik, Original). 110 Zeilen mit Rechenkern (Matrix mal
Vektor, Quadrate, Inverse, Fixvektoren, Parameter, Gleichungs-
systeme, Rückrechnung, Potenzen, Exponentialungleichungen) mit
sympy nachgerechnet; die Zonezeilen und die Sachaufgaben im Kopf
oder mit Python; Begründungszeilen inhaltlich gelesen. 25 Ankreuz-
zeilen: Optionen gezählt, richtige Option gegen die Lösung
(wortgleich) geprüft, Distraktoren auf Falschheit. 16 Fehler-
finden-Zeilen: eingebauter Fehler nachvollzogen, Richtigrechnung
nachgerechnet. Nebenprüfung mit Skript: $-Zeichen und Klammern
paarig in aufgabe und loesung, kein Aufgabentext doppelt, Formen
und pflicht-Schlüssel stimmig, Zeichnen-Zeilen mit Grafik. Die 13
Originale gegen Abschnitt 2 der Mappe gehalten (Kennung, Papier,
Verfremdung: gleiches Verfahren, andere Zahlen). bank-pruef.py:
Abweichungen 0, Warnungen 0 in allen sechs Dateien.

## Befunde

matrizen-und-uebergangsprozesse-zone-f1-v7: Das Antwortgerüst
fragt x und y, die Lösung nennt für t = 3 nur y = 4 – „x = 3“
ergänzen.

matrizen-und-uebergangsprozesse-e5-k1-s0-v2: doppelt zu
e4-k1-s0-v3 – dieselbe Frage (zwei Schritte rückwärts, einmal als
M⁻¹·M⁻¹·v, einmal als (M⁻¹)²·v), dieselben drei Optionen, dieselbe
Lösung; Regel „keine Aufgabe doppelt, auch nicht über Ketten
hinweg“ – in e5 einen anderen Term nehmen (etwa (M⁻¹)³·v, drei
Schritte rückwärts).

matrizen-und-uebergangsprozesse-e1-k1-s2-v2: fraglich: „sie
(links) mit einem Vektor multiplizieren“ hat zwei Lesarten
(Matrix links: 3×2 mal 3-Vektor, nicht bildbar – die Lösung;
Vektor links als Zeile: 1×3 mal 3×2, bildbar) – „Matrix mal
Vektor“ ausschreiben.

matrizen-und-uebergangsprozesse-e4-k1-s5-v2: fraglich: Die Lösung
nennt den Zugang z ohne Wert, die Aufgabe gibt 50 Tiere im ersten
Gebiet vor – z = (50 | 0) in die Lösung schreiben.

Sauber: 211 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e4-k1-s5-v2: Zugang z in der Lösung ohne Wert.
- e5-k1-s0-v2: doppelt zu e4-k1-s0-v3 (der Erstleser führt beide
  ids, ich nur die e5-Zeile als die zu ändernde).

Nur Zweitleser:
- zone-f1-v7: Lösung nennt für t = 3 kein x.
- e1-k1-s2-v2 (fraglich): „(links)“ mit zwei Lesarten.

Nur Erstleser:
- e2-k1-s7-v3, e2-k1-s7-v4: M^T unerklärt – Zustimmung: die
  Regel verlangt erklärte Symbole, und in e2-k1-s5-v2 steht der
  Klammersatz schon; ich habe ihn überlesen.
- e3-k1-s7-v1: B ohne Zeilen- und Spaltennamen, Tisch ohne
  Platte – teils: die Lesart ist durch „Zwischenprodukte je
  Endprodukt“ und die Reihenfolge Z1, Z2 / E1, E2 festgelegt wie
  in allen anderen Zeilen, die Namen schaden aber nicht; der
  Tisch mit 0 Platten ist im Kontext unsinnig, da stimme ich zu.
- e5-k3-s3-v3: Anwendung ohne Entscheidung – teils: „ab wann muss
  die Gemeinde handeln“ ist eine im Kontext sinnvolle Frage, aber
  der Handgriff ist derselbe wie in e5-k1-s6-v2 (Schwelle über
  Exponentialungleichung) und es wird nichts abgewogen; eine
  Entscheidungsfrage wäre die stärkere Anwendungszeile.
- e4-k1-s7-v3, e4-k1-s7-v4: Diagonalmatrix D in der Lösung ohne
  Sprosse, die sie einführt – teils: die Lösungen definieren D
  selbst, und das Original 2022 verlangt genau diese Form
  (Mappe: „Abgang als Diagonalmatrix“); die Lücke liegt in der
  Kette (e4-k1-s5 übt nur Zugang und Rückrechnung), nicht in der
  Zeile – eine Variante mit prozentualem Abgang in e4-k1-s5 wäre
  die richtige Ergänzung.
- e3-k1-s0-v3: Distraktor „von Z3 nach E2“ mit nicht vorhandenem
  Knoten – Zustimmung: der Distraktor fällt ohne Verständnis weg;
  ich hatte es beim Lesen bemerkt und nicht als Befund gewertet,
  „von Z1 nach E3“ wäre besser.

Zahlen: Zweitleser 4 Befunde, Erstleser 7, gemeinsam 2, nur
Zweitleser 2. Gezählt je Befund-Absatz, nicht je id: das Paar
e4-k1-s0-v3/e5-k1-s0-v2 ist bei beiden ein Befund, die Paare
e2-k1-s7-v3/v4 und e4-k1-s7-v3/v4 des Erstlesers je einer; der
Erstleser kommt so auf 7 Absätze zu 10 ids (Sauber 205), ich auf 4
Absätze zu 4 ids (Sauber 211).

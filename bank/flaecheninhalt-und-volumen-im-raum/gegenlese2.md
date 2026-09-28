# Zweitlesung flaecheninhalt-und-volumen-im-raum

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 197
(zone 29, e1 46, e2 43, e3 35, e4 44)

Prüfung: Jede Zeile wurde per Skript ausgegeben und gelesen. Für
alle Koordinatenaufgaben wurden die Größen aus dem Aufgabentext
neu gerechnet (numpy): Beträge, Skalarprodukte für behauptete
rechte Winkel, Kreuzprodukt für Dreiecks- und Vierecksflächen,
Seitengleichheit bei gleichschenkligen Dreiecken, Rauten und
Quadraten, Parallelität und Diagonalenschnitt bei Trapezen und
Rauten, Spurpunkte aus Ebenengleichungen, Schattenpunkte aus
Lichtrichtung, Spurpunkt einer Geraden in z = 0, Pyramidenhöhe als
Abstand der Spitze von der Grundebene, Differenz ähnlicher
Pyramiden mit dem Kubus des Streckfaktors, Rotationskörper,
Behälter und die Parameteraufgaben der Prüfungshöhe. Ergebnisse
mit loesung und pruef verglichen (Rundung, Einheit, Stellen): keine
Abweichung. Ankreuzaufgaben: alle Optionen durchgegangen;
Fehler-finden: Fehlrechnung reproduziert und Richtigrechnung
geprüft; Begründen: Kern geprüft. 159 Zeilen mit Zahl in pruef,
38 ohne (Ankreuzen, Begründen, Zeichnen). Nebenprüfungen:
Prüfkennung im Text gegen Feld original (Jahr, GK/LK), $- und
Klammerbalance, Doppelungen (aufgabe + grafik) – nur der Befund zu
e4-k1-s3-v2. `python3 werkzeuge/bank-pruef.py
flaecheninhalt-und-volumen-im-raum`: zone, e1, e2, e3, e4 je
„Abweichungen 0, Warnungen 0"; gesamt „Abweichungen: 0,
Warnungen: 0".

## Befunde

e4-k1-s3-v2: Text trägt die Prüfkennung „(Abitur 2023 GK)", das
Feld original ist null – Widerspruch; entweder original mit
Kennung aus der Mappe eintragen oder die Kennung im Fragesatz
streichen.

e2-k1-s0-v3: Ankreuzen mit zwei richtigen Optionen – für das
Quadrat gilt „Seite mal Seite" und „halbes Diagonalenprodukt"
(d²/2); die Einheit selbst lehrt das in k1-s4 und k3-s2-v3 –
dritte Option durch eine falsche ersetzen (z. B. „Seite mal
Diagonale") oder fragen, welche Formel nur die Seitenlänge braucht.

fraglich: e2-k1-s0-v1: für die Raute liefert auch „halbe Summe der
parallelen Seiten mal Höhe" den richtigen Wert (Raute ist ein
Parallelogramm, ½·(a + a)·h = a·h), wenn Trapez inklusiv
definiert wird, wie in den meisten Lehrwerken – Option gegen eine
klar falsche tauschen, wenn die Vorstufe eindeutig sein soll.

fraglich: e3-k2-s3-v1, e2-k3-s4-v2, e4-k2-s4-v2, e4-k2-s4-v3:
sprosse_text nennt einen bestimmten Körper oder eine bestimmte
Figur (Haus als Quader plus Dachprisma; Trapez im Raum; Differenz
zweier Pyramiden), die Aufgabe rechnet einen anderen (Pyramide;
Rechteck; Summe Zylinder + Kegel bzw. Quader + Pyramide); merkmal
(„Sachkontext …") passt – entweder ist das gewollt (Anwendung als
Typ, Kontext frei), dann kein Befund, oder die Varianten sollen
bei der Figur der Sprosse bleiben.

Sauber: 190 Zeilen ohne Befund

## Abgleich

Gelesen nach dem eigenen Befundteil: gegenlese.md vom 2026-09-27
(Erstleser, 5 Befundzeilen, je eine id, alle unter „Punkt 3 –
Sprosse, Merkmal, Kennung"; „Sauber: 192").

- Beide Leser: e4-k1-s3-v2 (Kennung ohne original) sowie
  e3-k2-s3-v1, e2-k3-s4-v2, e4-k2-s4-v2, e4-k2-s4-v3
  (Anwendungsvariante rechnet einen anderen Körper oder eine
  andere Figur als sprosse_text). Der Erstleser führt die vier
  Anwendungszeilen als feste Befunde mit Umbauvorschlag, ich als
  „fraglich"; dass beide unabhängig darauf stoßen, spricht für
  den Befund – ob sprosse_text die Varianten bindet, bleibt eine
  Entscheidung für den Chat (bank.md, „Varianten … nicht im
  Merkmal").
- Nur Zweitleser: e2-k1-s0-v3 (Quadrat: zwei richtige Optionen,
  fest) und e2-k1-s0-v1 (Raute: Trapezformel gilt auch, fraglich).
- Nur Erstleser: keine.

Zahlen: Zweitleser 4 Befunde, Erstleser 5, gemeinsam 5, nur
Zweitleser 2. Gezählt: „Befund" = Zeile im Befundteil; meine
4 Zeilen nennen 7 ids (2 feste, 5 als fraglich), die 5 Zeilen des
Erstlesers je eine id; „gemeinsam", „nur Zweitleser" und „nur
Erstleser" zählen ids (5 + 2 + 0). Nach ids: Zweitleser 7,
Erstleser 5.

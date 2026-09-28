# Zweitlesung quadratische-funktionen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 257
(zone 46, e1 49, e2 60, e3 42, e4 60)

Prüfung: Jede Zeile von zone, e1–e4 gelesen (weg.jsonl ist keine
Aufgabendatei und nicht geprüft) und aus dem Aufgabentext selbst
nachgerechnet. Mit sympy (Skript im Scratchpad): jede Gleichheit
zwischen Termen in loesung (Ausmultiplizieren, Nachweise,
Scheitelpunktform ↔ Normalform) – alle Identitäten stimmen, die
übrigen „Ungleichungen“ sind die gewollten Ansätze beim Gleichsetzen;
jede Grafik mit \parabel oder \gerade gegen f(x) bzw. g(x) der
Aufgabe – alle passen, einzige Abweichung e2-k2-s3-v1 ist gewollt
(falsche Aussage zum Ankreuzen). Nullstellen, Schnittpunkte,
Näherungswerte (Rundung auf zwei Stellen) und Sachaufgaben von Hand
bzw. mit Python nachgerechnet; alle 257 pruef-Ausdrücke auswertbar,
alle Lösungszahlen stimmen. Ankreuzzeilen (e1 s0, s6, s7, s9, s10,
s11; e2-k2-s3; e3 s0, s8) Option für Option gegen Text und Grafik
geprüft; Fehler-finden-Zeilen (zone-f4-v5, e1-k2-s1, e2-k2-s1,
e3-k2-s1, e4-k2-s1) – eingebauter Fehler jeweils wirklich falsch und
nach dem Muster aus „Typische Fehler“, Richtigrechnung stimmt.
`bank-pruef.py quadratische-funktionen`: zone, e1–e4 je 0
Abweichungen, 0 Warnungen (1 Abweichung „Dateiname“ nur für
weg.jsonl).

## Befunde

e1-k1-s6-v1, e1-k1-s6-v2, e1-k1-s6-v3: [A] vier Kästchen, von denen
zwei richtig sind (Öffnung und Breite); loesung nennt eine
Kombination, keine Option wortgleich – in zwei Ankreuzfragen je
Zeile teilen (zwei Kästchen „nach oben/nach unten“, zwei
„schmaler/breiter“) oder loesung als „nach unten; schmaler“ je
Zeile der Optionen fassen und bank.md die Doppelfrage erlauben.

e1-k1-s8-v2, e1-k1-s8-v3: [M] Sprosse verlangt „verdoppelt oder
halbiert“, die Varianten vierteln (0,25x²) bzw. vervierfachen (4x²)
– bekannt aus stand.md (Entscheidung 6, 2x² gesperrt); im Chat
entscheiden, ob 2x² als Gegenstand der Sprosse frei ist, sonst
Sprossentext im Katalog auf „mit a malgenommen“ weiten.

e2-k1-s15-v2: [M] Sprosse und Original 2018-OS-K5d verlangen eine
Parabel ohne Nullstellen; die Variante verlangt zwei Nullstellen –
damit fällt die Falle des Originals (Scheitel im Ursprung, nach
unten geöffnet mit Scheitel über der Achse) weg. Vorschlag: „nach
oben geöffnet, keine Nullstelle“ (etwa f(x) = x² + 3, g(x) = −x² − 3)
oder wie v1 mit anderem Scheitel.

e3-k1-s4-v2, e3-k1-s4-v3: [M] Sprosse „d negativ (Plus in der
Klammer)“, die Varianten machen zusätzlich e negativ ((x + 2)² − 5,
(x + 6)² − 10) – zwei Änderungen gegenüber s3 statt einer. Vorschlag:
e positiv lassen (etwa (x + 2)² + 5, (x + 6)² + 1); negatives e
kommt ohnehin in s10.

Sauber: 249 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k1-s15-v2 – die Variante verlangt zwei Nullstellen,
Sprosse und Original 2018-OS-K5d verlangen „ohne Nullstellen“.

Nur Erstleser:
- zone-f4-v5, e3-k2-s1-v1 (pruef nur die Zahl aus der Klammer):
  nicht bestätigt als Rechenfehler – loesung stimmt, pruef an der
  ersten Zahl ist die in stand.md (Nachbesserung, Befund N6)
  dokumentierte Konvention; als Schwäche der pruef-Abdeckung
  berechtigt.
- zone-f7-v3, e4-k1-s4-v1 bis v3, e4-k1-s14-v1 und v2 („auf zwei
  Stellen“): bestätigt als leichte Unschärfe – „auf zwei
  Nachkommastellen“ ist eindeutig; habe ich als übliche
  Schulsprache durchgehen lassen.
- e1-k2-s2-v3 (Breite bei 4x² statt eines der beiden im
  sprosse_text genannten Gründe): bestätigt, übersehen.
- e1-k2-s3-v3 (nur Graph → Tabelle, merkmal verlangt die
  Gleichung): teilweise bestätigt – zum sprosse_text „Wertetabelle
  … ausfüllen“ passt sie, zum merkmal nicht; die Gleichung steht
  nur in Klammern in der loesung.
- e2-k1-s10-v3 (Scheitel nicht auf einer Achse): nicht bestätigt –
  die Klammer der Sprosse nennt Beispiele für Eigenschaften, „keine
  Nullstellen“ ist eine davon und wird verlangt.
- e3-k2-s2-v3 (Gleichheit der Formen statt q oder Öffnung, Lösung
  rechnet): bestätigt, übersehen.
- zone-f4-v5, e4-k2-s1-v3 (Fehler x² − 25 bzw. x² − 16 enthält auch
  das falsche Vorzeichen, Lösung nennt nur das Mittelglied):
  bestätigt als Verbesserung der loesung; der eingebaute Fehler
  selbst folgt dem Muster „(x − 2)² = x² − 4“ aus „Typische Fehler“
  und ist richtig gebaut.

Nur Zweitleser:
- e1-k1-s6-v1 bis v3: vier Kästchen mit zwei richtigen Kreuzen,
  loesung nennt keine Option wortgleich.
- e1-k1-s8-v2, v3: vierteln bzw. vervierfachen statt verdoppeln
  oder halbieren (bekannt aus stand.md, Entscheidung 6).
- e3-k1-s4-v2, v3: neben d wird auch e negativ – zwei Änderungen
  gegenüber s3.

Widersprüche: Der Erstleser meldet bei Ankreuzen „keine“, ich
e1-k1-s6 (zwei richtige Kreuze je Zeile). e2-k1-s10-v3 hält der
Erstleser für unpassend, ich für sauber.

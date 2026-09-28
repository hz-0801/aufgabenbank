# Zweitlesung zufallsexperimente-und-pfadregeln

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 368
(zone 41, e1 40, e2 46, e3 54, e4 32, e5 38, e6 38, e7 41, e8 38)

Prüfung: Jede Zeile aller neun jsonl-Dateien gelesen und aus dem Aufgabentext selbst nachgerechnet – Brüche, Pfadsummen, Gegenereignisse, Gleichungen und Ungleichungen von Hand und mit einem sympy-Skript im Scratchpad (Würfel- und Glücksradverteilungen ausgezählt, Blocklagen und Farbfolgen durch vollständige Aufzählung, zufällige Urnenzusammensetzung über die Binomialgewichte, die Summenverteilungen der Term-Platzhalter in e7 s8, die quadratischen Bedingungen in e8, die Mindestanzahlen über Logarithmus und Einsetzen). Alle 256 Zeilen mit pruef-Zahl stimmen mit meiner Rechnung und mit der Lösung überein (Rundung eingeschlossen); auch die Zeilen ohne pruef (Deutungen, Aufzählungen, Bäume) sind inhaltlich richtig, die Lösungsbäume passen zu den Aufgabenwerten. Die 33 Ankreuzzeilen haben je genau eine richtige Option, die Lösung nennt sie wortgleich. Die 25 Fehler-finden-Zeilen enthalten jeweils einen echten Fehler aus „Typische Fehler“, die Richtigrechnung stimmt. `werkzeuge/bank-pruef.py`: 0 Abweichungen, 2 Warnungen (e1 k1 s7 und e2 k1 s8: Prüfungshöhe ohne Original 2 statt 3 Zeilen). Dazu ein Hinweis ohne Zeilenbefund: e1-k1-s7-v3/v4 und e2-k1-s8-v3/v4 tragen eine Prüfkennung („Abitur 2023 GK“, „Abitur 2019 GK“) bei original null – die zugehörigen iqb-Originale (2023MgrundlegendBStochastikWTR1-2d, 2019MgrundlegendBStochastikWTR2-3a) stehen nicht in Abschnitt 2 der Mappe; das ist ein Mappen- bzw. Katalogbefund, keine falsche Zeile.

## Befunde

e3-k1-s5-v3: [E] Der Buchstabe B steht zweimal für Verschiedenes – „Becher (B)“ als Ast und „B: ohne Sahne“ als Ereignis – Ereignisse E und F nennen oder den Becher anders abkürzen.

e3-k1-s6-v2: [M] „höchstens eine defekt“ wird als direkte Summe zweier Pfade gerechnet; das Merkmal der Sprosse (Gegenereignis „keinmal“ statt langer Summe) kommt nicht vor – etwa „höchstens zwei defekt“ fragen, $1 - 0{,}1^3 = 0{,}999$, oder „mindestens eine defekt“.

e4-k1-s2-v1: [E] „Die ersten drei werden betrachtet“ sagt nicht, dass die Reihenfolge zufällig ist; ohne Zufall ist keine Wahrscheinlichkeit definiert – „Drei der Befragten werden nacheinander zufällig ausgewählt.“

e4-k2-s1-v3: [E] „P(alle roten)“ ist mehrdeutig (alle roten Äpfel des Korbs oder alle entnommenen rot) – „P(alle vier genommenen Äpfel sind rot)“.

e5-k2-s4-v2: [E] Dieselbe Aufgabe wie e5-k1-s1-v1 (Glücksrad 0,2, dreimal, Term $3 \cdot 0{,}2 \cdot 0{,}8^2$) in derselben Einheit, einmal zu rechnen, einmal zu deuten; auf einem Blatt verrät die eine die andere (Regel „keine Aufgabe doppelt“; kein eigenes Kennzeichen, unter E geführt) – andere Zahlen, etwa $3 \cdot 0{,}1 \cdot 0{,}9^2$ bei einer Ausschussquote.

e6-k1-s1-v2: [E] „P heißt pünktlich“ kollidiert mit P als Zeichen für Wahrscheinlichkeit (P(P) wäre die Folge) – Buchstabe Ü oder R („rechtzeitig“) wählen.

e7-k1-s7-v1: [E] Der Platzhalter a ist nicht eindeutig: „12 über 5“ = „12 über 7“, also ist auch a = 7 richtig – Platzhalter am Exponenten statt im Binomialkoeffizienten setzen oder „a ≤ 6“ bzw. „a ist die Zahl der Erfolge“ ergänzen.

e7-k1-s8-v1, e7-k1-s8-v2: [E] v und w sind als natürliche Zahlen nicht eindeutig: $v \cdot \left(\frac{1}{2}\right)^w$ = 6 erlaubt auch v = 12, w = 1 oder v = 48, w = 3; ebenso $v \cdot \left(\frac{1}{18}\right)^w$ (v = 432, w = 3). Das Original 2026-bb-ea-A1.10b hat dieselbe Lücke – „v ist die Zahl der Reihenfolgen“ ergänzen.

e8-k2-s4-v2: [E] Gleiche Gleichung wie e8-k1-s1-v5 ($0{,}5 \cdot 0{,}2 + 0{,}5a = 0{,}35$, a = 0,5) in derselben Einheit (Regel „keine Aufgabe doppelt“; unter E geführt) – andere Werte im Baum, etwa X unter B $0{,}3$ und P(X) $= 0{,}45$ (a = 0,6).

Sauber: 358 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e3-k1-s5-v3: B steht für „Becher“ und für das Ereignis „ohne Sahne“.
- e3-k1-s6-v2: „höchstens eine defekt“ wird direkt summiert, das Merkmal (Gegenereignis „keinmal“) fehlt.
- e4-k2-s1-v3: „P(alle roten)“ ist mehrdeutig, gemeint sind alle vier genommenen Äpfel.
- e7-k1-s8-v1, e7-k1-s8-v2: v und w sind als natürliche Zahlen nicht eindeutig; v als Zahl der Reihenfolgen festlegen.

Nur Erstleser:
- e1-k2-s3-v1 („ohne beides“ auch als „nicht beides“ lesbar): bestätigt, schwach – die übliche Lesart ist „weder – noch“, aber „weder ein Fahrrad noch ein Auto“ kostet nichts und schließt die 75-%-Lesart aus.
- e2-k1-s2-v2 („Gewinn/Niete“ ohne Anzahlen): bestätigt – ohne Zahl der Gewinne ist die Teilfrage nicht entscheidbar, die Lösung weicht auf „meist“ aus.
- e3-k4-s4-v2 (Term symmetrisch, A und B vertauschbar): bestätigt als Lösungsfrage – die Aufgabe bleibt lösbar, die Lösung sollte die vertauschte Beschriftung zulassen; ich hatte das gesehen und für unerheblich gehalten.
- e4-k1-s0-v1 (P(Mädchen) beim zweiten Losen bleibt unbedingt gleich): bestätigt – ohne Kenntnis des ersten Loses ist die Chance gleich (genau das lehrt e4-k1-s5), „p ändert sich“ stimmt nur bedingt; dasselbe Muster steckt in e3-k1-s0-v2 (Kekse, „Bleibt P(Schoko) gleich?“), das keiner der beiden Leser gemeldet hat – beide bedingt fragen („wenn der erste … war“) oder nach dem Ast fragen.
- e4-k1-s0-v4 (Umlegen ohne Urneninhalte): bestätigt – bei gleichem Rotanteil in A und B bleibt P(rot aus B) gleich; Inhalte nennen oder bedingt fragen.
- e8-k1-s3-v2 (x im Text nicht eingeführt, Gerüst ohne Platz für den Vergleich): bestätigt – Regel „Buchstaben nur, wenn im Text erklärt“.
- e8-k1-s3-v3 (k = 3/7 periodisch ohne Hinweis): bestätigt – Regel „periodische Dezimalbrüche tragen einen Hinweis“; ich hatte nur die Rechnung geprüft.
- e8-k2-s4-v1 (x = 0,5428… ohne Rundungshinweis): bestätigt aus demselben Grund; der Vorschlag „insgesamt 59 %, x = 0,5“ rechnet sich (0,24 + 0,35 = 0,59).
- e6-k1-s6-v3 (J und N im Text nicht erklärt): bestätigt, klein – v1 erklärt sie, v3 nicht.
- e6-k2-s4-v2 (offene Formulieraufgabe mit festgelegter Lösung und pruef): bestätigt – mehrere Sätze sind richtig; Lösung als Beispiel kennzeichnen, pruef leeren oder die Sätze vorgeben.
- e7-k1-s1-v2, e7-k1-s1-v4, e7-k1-s1-v5 (derselbe Wert gehört zu mehreren festen Reihenfolgen): bestätigt – v3 fasst die Lösung als „etwa …“, die drei anderen nennen eine Folge als einzige; die Lösung sollte die gleichwertigen Folgen zulassen.
- e1-k1-s0-v3, e1-k1-s0-v4 („Welche Verknüpfung?“ statt „Ergebnis oder Ereignis?“): nicht bestätigt – der Erkennungsschritt des Katalogs und das merkmal nennen ausdrücklich auch „und / oder / nicht / genau eines“; die Varianten decken diesen zweiten Teil ab.
- e1-k1-s5-v2 („berechne“ statt „weise nach“): nicht bestätigt – derselbe Handgriff (Gegenereignis der Vereinigung über den Additionssatz), nur ohne Zielwert; angleichen schadet nicht.
- e1-k1-s7-v1 bis v4 und e2-k1-s8-v3, v4 (Prüfungssprosse auf Varianten verteilt): nicht bestätigt – die Prüfsprosse nennt zwei Originale, bank.md sieht zwei Zeilen je Original vor; die Aufteilung ist so gewollt. Die Prüfkennung bei original null ist ein Mappenbefund (Originale fehlen in Abschnitt 2), keine Zeilenfrage.
- e2-k1-s2-v2 (kein weiteres Beispiel verlangt): bestätigt, klein – die Sprosse sagt „und weitere Beispiele nennen“.
- e2-k1-s4-v2 (rechnen statt nachweisen): nicht bestätigt – das Abzählen der Paare ist dieselbe Handlung; der Operator weicht ab, das Merkmal nicht.
- e4-k1-s3-v1 (nur ein Pfad, kein „spätestens“): nicht bestätigt – die Sprosse nennt beides mit Semikolon, v1 deckt den ersten Teil.
- e4-k1-s4-v2 (mögliche Anzahlen statt Wahrscheinlichkeit, n ungenutzt): nicht bestätigt – das ist der Katalogtyp „Mögliche Anzahlen nach dem Umlegen zweier Kugeln angeben“ der Einheit, die Fälle nach der Farbe sind das Merkmal; das freie n stört nicht.
- e5-k1-s5-v3 (nur Farbfolgen zählen): nicht bestätigt – die Sprosse nennt „alle Farbfolgen zählen“ ausdrücklich.
- e8-k1-s6-v3 (lineare Laplace-Ungleichung): nicht bestätigt – der Katalog führt den Typ „Mindestanzahl beim Ziehen ohne Zurücklegen über das Gegenereignis“; ohne Zurücklegen wird die Ungleichung linear.
- e6-k1-s4-v2 (drei Lieferanten): nicht bestätigt – die totale Wahrscheinlichkeit als Pfadsumme ist dieselbe Handlung, eine dritte Gruppe ändert das Merkmal nicht.
- e6-k1-s6-v2 (nur deuten, v1/v3 nur vervollständigen): nicht bestätigt – die Sprosse nennt beide Handgriffe, die Varianten verteilen sie.
- e7-k1-s3-v3 (Summanden und Vorfaktor zugleich): nicht bestätigt – die Sprosse heißt „Vorfaktor und Summanden“.
- e7-k1-s4-v2, e7-k1-s4-v3 (Experiment vorgegeben): bestätigt, schwach – die Sprosse sagt „samt Experiment beschreiben“, nur v1 verlangt das; der Kern „1 −“ als Gegenereignis ist da.

Nur Zweitleser:
- e4-k1-s2-v1: „Die ersten drei werden betrachtet“ nennt keinen Zufall.
- e5-k2-s4-v2: dieselbe Aufgabe wie e5-k1-s1-v1 (Glücksrad 0,2, dreimal) in derselben Einheit.
- e6-k1-s1-v2: „P heißt pünktlich“ kollidiert mit P für Wahrscheinlichkeit.
- e7-k1-s7-v1: a = 5 und a = 7 sind wegen „12 über 5“ = „12 über 7“ beide richtig.
- e8-k2-s4-v2: dieselbe Gleichung wie e8-k1-s1-v5 in derselben Einheit.

Widersprüche: Der Erstleser wertet die auf Varianten verteilten Prüfungs- und Mehrteil-Sprossen (e1-k1-s7-v1 bis v4, e2-k1-s8-v3, v4, e1-k1-s0-v3, v4, e4-k1-s3-v1, e6-k1-s6-v2, e7-k1-s3-v3) als Merkmalsverstoß, ich als gewollte Aufteilung nach Sprossentext und Mengenregel. Bei e4-k1-s4-v2, e5-k1-s5-v3 und e8-k1-s6-v3 sieht der Erstleser andere Struktur, ich einen eigenen Katalogtyp bzw. den Wortlaut der Sprosse.

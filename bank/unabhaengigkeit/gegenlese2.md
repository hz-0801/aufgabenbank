# Zweitlesung unabhaengigkeit

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 116 (zone 26, e1 39,
e2 34, e3 17)

Prüfung: Jede Zeile wurde einzeln gelesen und die Lösung aus dem
Aufgabentext nachgerechnet: alle 17 Vierfeldertafeln (grafik und
loesungsgrafik, auch die drei mit Termen in p und die Prozenttafel)
mit sympy auf Zeilen- und Spaltensummen; jede Produktregel, jeder
bedingte Anteil und jede Tafelzahl mit Fractions; die Gleichungen
in p bzw. x (Zone f5, E2 s2/s3/s5/s6, Anwendung E2) mit sympy
gelöst, Nulllösungen und Randlösungen gegen den Text geprüft; die
Abzählaufgaben (E1 s5) durch Aufzählen der Ergebnispaare; alle 90
pruef-Ausdrücke ausgewertet und mit der Lösungszahl verglichen.
Keine falsche Lösungszahl, keine falsche Tafel, kein pruef, der
nicht zur Lösung passt. `python3 werkzeuge/bank-pruef.py
unabhaengigkeit`: zone 0/0, e1 0/0, e2 0/0, e3 0/0, gesamt 0
Abweichungen, 0 Warnungen. 19 Ankreuzzeilen (zone 3, e1 8, e2 4,
e3 4): überall genau eine Option richtig, loesung beginnt mit ihr
wortgleich. 10 Fehler-finden-Zeilen (zone 1, e1 3, e2 3, e3 3): der
eingebaute Fehler ist jedes Mal wirklich falsch, die Berichtigung
stimmt. Zusätzlich: Renderprobe eines Umlauts im Mathe-Modus mit
xelatex (die Vorlage läuft auf xelatex), Vergleich der Kontexte mit
Abschnitt 2 der Mappe, Suche nach gleichen Tafeln und Zahlensätzen
über alle vier Dateien. Bei Dubletten zählt die Zeile, die
geändert werden soll, als Zeile mit Befund.

## Befunde

e1-k2-s3-v1: In der Lösung steht `$P_{Ä}(S) = …$`; im Mathe-Modus
fällt das Ä unter xelatex stumm weg (Probe: „Missing character Ä
in font cmmi7“, gedruckt wird „P(S) = 0,7“), unter pdflatex gibt es
eine Warnung und ein leeres Zeichen. Der Leser sieht dann zweimal
„P(S)“ mit verschiedenen Werten. – Vorschlag: `P_{\text{Ä}}(S)`
oder das Ereignis A nennen (in aufgabe und loesung).

e1-k2-s5-v2: Die Verfremdung liegt zu nah am Original
2023MerhoehtBStochastikWTR1-2: gleiches Rad mit 1, 2, 3, Ereignis C
„Summe höchstens 3“ ist wortgleich zum Original „Summe kleiner als
4“, D „Produkt ist 2“ ist das Original „Produkt 2 oder 3“ um ein
Ergebnis gekürzt; die Falle (1-2 und 2-1 doppelt zählen) bleibt
dieselbe, die Zahlen aber auch. – Vorschlag: andere Ereignisse, etwa
Rad 1–4, C „Summe höchstens 4“ (6 von 16), D „Produkt ist 3“ (2 von
16), Schnitt 2 von 16, 6/16 · 2/16 ≠ 2/16 – abhängig, gleiche
Falle.

e1-k2-s2-v2, e1-k2-s3-v1, e1-k2-s4-v1, e2-k1-s5-v1: Der Kontext ist
dem Original entnommen, nur die Zahlen sind neu (bank.md: „andere
Zahlen, anderer Kontext“): Schulweg kurz/lang und Bus wie 2024-B-3e
(Schulweg und ÖPNV); Fahrprüfung einer Region mit „mindestens 30
Jahre“ wie 2019-be-gk-B4.1d; schwere Pakete und Ausland wie
2022-bebb-gk-B4i (schwere Pakete, Ziel A); Gerät defekt bei Fehler
A oder B wie 2024-bebb-lk-A1.9b. – Vorschlag: Kontext tauschen
(z. B. Vereinsmitglieder mit kurzer/langer Anfahrt und Training;
Sprachprüfung und Altersgruppe; Bestellungen mit Retoure und
Zahlungsart; Lieferung verspätet durch Wetter oder Streik).

e1-k3-s4-v2: Trägt dieselben Zahlen wie e1-k2-s6-v1 (Kundenkarte
0,7; online unter Karteninhabern 0,4; ohne Karte und online 0,15;
P(O) = 0,43) im selben Kontext; wer die eine Zeile gelöst hat, hat
die andere. – Vorschlag: für den Baum andere Zahlen (z. B. K 0,6;
O|K 0,3; O|nicht K 0,45; dann P(O) = 0,36, P(K) · P(O) = 0,216 ≠
0,18).

e2-k2-s1-v2: Fehler-finden mit genau den Zahlen von e2-k1-s5-v1
(defekt 0,3; Fehler A 0,2; Ergebnis 0,125) im selben Kontext. –
Vorschlag: andere Zahlen, z. B. defekt 0,4 und Fehler A 0,25 (Tom:
x = 0,15; richtig x = 0,2).

e2-k2-s1-v3: Fehler-finden am selben Szenario mit demselben Ergebnis
wie e2-k1-s3-v2 (Rot mit p, E erste Drehung Rot, G genau einmal Rot,
p = 0,5). – Vorschlag: den Fehler am Rad mit drei Feldern (wie
e2-k1-s3-v1) einbauen oder G „beide gleich“ nehmen.

e2-k1-s4-v1: Dieselben Zahlen wie zone-f2-v3 (P(A) = 0,4, P(A ∩ B)
= 0,1, Quotient 0,25) – dort als P_A(B), hier als P(B) bei
Unabhängigkeit; auf einem Blatt mit Blatt 0 zweimal dieselbe
Rechnung. – Vorschlag: e2-k1-s4-v1 auf andere Zahlen setzen, z. B.
P(A) = 0,5 und P(A ∩ B) = 0,15, dann P(B) = 0,3.

e1-k3-s1-v3: Dasselbe Fehlmuster mit denselben Rahmenzahlen wie das
Zone-Paar zone-f1-v5 (50 Personen, 20 in der Teilgruppe, Prozent
der Teilgruppe auf alle 50 bezogen, falsches Feld = Gesamtzahl des
Merkmals). – Vorschlag: andere Zahlen, z. B. 80 Gäste, 30 Kinder,
40 % der Kinder (12 statt 32), 32 Gäste mit Eis.

e1-k3-s1-v1, e1-k3-s4-v1: Beide zeigen die Tafel von e1-k2-s1-v1
(M/F, 20, 30, 50, 20, 30, 50, 40, 60, 100) unverändert; dieselbe
Tafel steht damit dreimal in E1 (Grundfall, Fehler finden,
Darstellung), und das Ergebnis „unabhängig“ ist nach der ersten
bekannt. – Vorschlag: für die beiden Pflichtzeilen eine eigene
Tafel, etwa 80 Schüler: 12, 18, 30; 20, 30, 50; 32, 48, 80 (bleibt
unabhängig: 0,4 · 0,375 = 0,15 = 12/80).

e2-k1-s2-v2: Das Merkmal der Sprosse („Ränder in p ausdrücken,
Gleichung ansetzen, Nulllösung verwerfen“) kommt hier nicht vor:
beide Ränder stehen als Zahlen, p = 0,4 · 0,5 ist eine Multiplikation
ohne Gleichung und ohne Nulllösung. – Vorschlag: einen Rand in p
setzen, z. B. Felder P(A ∩ B) = p, P(A ∩ nicht B) = p, P(nicht A ∩
B) = 0,3; dann P(A) = 2p, P(B) = p + 0,3, Gleichung 2p(p + 0,3) =
p, Lösungen 0 und 0,2.

e2-k2-s3-v2: sprosse_text nennt den Typ „Wahrscheinlichkeit eines
Fehlers aus der Vereinigung zweier unabhängiger Fehler berechnen“,
die Aufgabe ist aber der Divisionstyp (P(B) aus Schnitt und
Unabhängigkeit, 0,06 : 0,4). – Vorschlag: sprosse_text auf den Typ
„Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer
Schnittwahrscheinlichkeit bestimmen“ setzen oder die Aufgabe als
Vereinigung bauen.

e2-k1-s3-v3: Die Buchstaben sind gegen v2 vertauscht – in v2 (und in
e2-k2-s1-v3) ist E „erste Drehung Rot“ und G das zweite Ereignis, in
v3 heißt „erste Drehung Rot“ F und „beide gleich“ E (bank.md: ein
Buchstabe je Einheit für eine Sache). – Vorschlag: in v3 E und G
wie in v2.

e1-k2-s2-v2: N steht für „fährt mit dem Bus“; N liest sich wie
„nicht“, und in derselben Datei ist N schon „App-Nutzer“
(e1-k2-s3-v2). – Vorschlag: B für Bus.

e1-k2-s1-v5: Der Fragesatz steht doppelt („Sind S und H unabhängig?
Prüfe mit der Produktregel, ob S und H stochastisch unabhängig
sind.“), und die Prüfkennung steht nach dem Punkt statt am Ende des
Fragesatzes wie in allen anderen Zeilen. – Vorschlag: ersten
Fragesatz streichen, „(Abitur 2024 GK)“ vor den Punkt.

zone-f2-v4: 8/30 ist nicht endlich (≈ 0,267); die Zone soll im Kopf
gehen. – Vorschlag: 32 Männer statt 30, dann 8/32 = 0,25 und 8/20 =
0,4.

e1-k3-s2-v2: „unter den Vielleser“ – Vorschlag: „unter den
Viellesern“.

e1-k3-s3-v2, e1-k3-s3-v3: Die Lösung rechnet mit F, N bzw. E, B, die
Aufgabe führt nur „Frau“, „Nebenwirkung“, „Express“, „beschädigt“
in Anführungszeichen ein (v1 löst das mit \text{Öko}). – Vorschlag:
in der Aufgabe „(F)“, „(N)“ bzw. „(E)“, „(B)“ anhängen.

Sauber: 96 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k2-s1-v5 (Fragesatz doppelt); e1-k3-s4-v2 (gleiche
Zahlen und Kontext wie e1-k2-s6-v1); e2-k1-s2-v2 (Merkmal der
Sprosse fehlt); e2-k2-s3-v2 (Divisionstyp unter Vereinigungs-Typ);
e1-k3-s2-v2 („Vielleser“).
Nur Zweitleser: e1-k2-s3-v1 (Ä im Mathe-Modus fällt weg; Kontext
Fahrprüfung aus dem Original); e1-k2-s5-v2 (Ereignisse fast
wortgleich zum Original); e1-k2-s2-v2, e1-k2-s4-v1, e2-k1-s5-v1
(Kontext aus dem Original; in s2-v2 dazu N für Bus); e2-k2-s1-v2
(Zahlen wie e2-k1-s5-v1); e2-k2-s1-v3 (Szenario und Ergebnis wie
e2-k1-s3-v2); e2-k1-s4-v1 (Zahlen wie zone-f2-v3); e1-k3-s1-v3
(Rahmenzahlen und Muster wie zone-f1-v5); e1-k3-s1-v1 und
e1-k3-s4-v1 (Tafel von e1-k2-s1-v1 dreimal); e2-k1-s3-v3
(Buchstaben E/F gegen v2 vertauscht); e1-k2-s1-v5 (Kennung nach dem
Punkt); zone-f2-v4 (8/30 nicht endlich); e1-k3-s3-v2, e1-k3-s3-v3
(Buchstaben in der Lösung nicht eingeführt).
Nur Erstleser: e1-k3-s3-v1 (Entscheidung „Werbung sinnvoll?“ nicht
eindeutig) – richtig, übersehen; die Frage schärfen ist der bessere
Weg als beide Antworten gelten zu lassen. e2-k2-s1-v2 (x in Toms
Rechnung nicht erklärt) – richtig, übersehen, Kleinkram. e3-k2-s1-v3
(„jede sechste Zahl eine Sechs“) – richtig, übersehen. e2-k1-s2-v3
(Gleichung linear, keine Nulllösung) – richtig, übersehen; das
Original trägt die Nulllösung als Falle, mit meinem Vorschlag für v2
hätte die Sprosse sie in zwei von drei Zeilen. e1-k3-s4-v2 (Lösung
nennt nur drei Werte statt der ganzen Tafel) – richtig, übersehen;
mit voller Liste muss auch pruef die neun Werte tragen. e2-k1-s5-v1,
e2-k1-s5-v2, e2-k1-s5-v3, e2-k2-s3-v1 (x in der Lösung nicht
eingeführt) – richtig, übersehen, Kleinkram; „Mit x = …:“ wie in
k1-s6 genügt. e2-k1-s1-v2, e2-k1-s1-v5 (Anzahl statt Anteil bei
„ohne Rechnung“) – stimme nicht zu, siehe Widerspruch.
Widerspruch: e2-k1-s1-v2 und v5 – der Erstleser sieht in „wie viele
Frauen“ (ein Viertel von 80) einen Verstoß gegen „ohne Rechnung
angeben“, ich halte den Schritt vom Gesamtanteil zur Anzahl für
keine Rechnung im Sinn der Sprosse und würde beide Zeilen lassen;
der Erstleser bietet „hinnehmen“ selbst an.

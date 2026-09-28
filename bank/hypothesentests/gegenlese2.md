# Zweitlesung hypothesentests

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 113 (zone 23, e1 27,
e2 25, e3 38)

Prüfung: Jede Zeile gelesen; jede Lösung unabhängig nachgerechnet
(scipy.stats.binom: alle Ablehnungsgrenzen als kleinstes bzw.
größtes k samt Nachbarwert, alle Fehler erster und zweiter Art,
die Schwellen-p in e3-k1-s4, die Umfänge 99/100/101 und
103/104/105 in e3-k1-s5, die erwarteten Kosten in e3-k3-s3-v2);
die in den Aufgaben genannten Regeln (etwa „ab 76 Treffern",
„höchstens 203") daraufhin geprüft, dass sie das Niveau 5 %
einhalten – alle tun es; die Gütekurven der Grafiken gegen die
Binomialkoeffizienten und die logarithmierten Koeffizienten
(ln C(150,1) = 5,0106 … ln C(300,8) = 34,9315) geprüft – alle
stimmen; die Tabellenwerte in e3-k3-s4 nachgerechnet. Ankreuzen:
in allen 12 Zeilen genau eine Option richtig. Fehler finden: in
allen 10 Zeilen ist der eingebaute Fehler wirklich falsch (Lisas
k = 67 ist tatsächlich das rechtsseitige Ergebnis, Pauls 0,0532
und Annas 0,0347/0,0199 stimmen als Zahlen, Toms 0,9937 und Saras
0,5419 ebenso). Die Originale in Abschnitt 2 der Mappe mit den
Aufgaben verglichen (Kontext, Zahlen, Richtung).
`python3 werkzeuge/bank-pruef.py hypothesentests`: 0 Abweichungen,
0 Warnungen.

## Befunde

e2-k1-s2-v1: Der Kontext des Originals 2024-bebb-lk-B4d ist
unverändert (Verlag, Algorithmus, zufriedene Abonnenten, 60 → 65 %),
nur die Zahl ist neu; bank.md verlangt anderen Kontext. Dazu kehrt
die Zeile die Figur des Originals um: Die Mappe gibt für B4d
$H_0$ „Anteil höchstens 60 %" und die Entscheidung über den
dauerhaften Einsatz – das ist die Figur „nur bei nachgewiesener
Verbesserung handeln" (s1), nicht „Abschalten nur bei Einbruch"
(s2). Die Zeile trägt also Kennung und Original einer Aufgabe mit
anderer Richtung. – Vorschlag: neuen Kontext (etwa eine
Nachtbuslinie, die nur bei nachgewiesenem Rückgang eingestellt
wird) und original null, weil B4d die s2-Figur nicht belegt; die
Zuordnung von B4d zur s2-Sprosse als Katalogbefund in stand.md.

e1-k1-s2-v1, e1-k3-s3-v2, e3-k1-s1-v1: Gewinnspiel, Buchungen,
Verlängerung – der Kontext der Originale 2023-bebb-lk-B4i/B4j (die
Mappe nennt „Gewinnspiel-Buchungen" als einen der fünf
abi-Kontexte); geändert sind nur die Zahlen (3 → 4 %, 800 → 650
bzw. 600 → 500). bank.md: „anderer Kontext". Rechnungen stimmen.
– Vorschlag: einen anderen Kontext mit derselben Figur (eine
Aktion, die sich nur ab einem Mindestanteil lohnt: Probeabo,
Rabattgutschein, Kundenkarte).

e1-k1-s2-v2: „Pkw, die nur mit dem Fahrer besetzt sind" ist der
Kontext des Originals 2026MerhoehtBStochastikWTR2-2a
(„Alleinfahrende"), 75 → 80 %, 400 → 300. Rechnung stimmt. –
Vorschlag: anderer Kontext (etwa „Mindestens 80 % der Fahrgäste
haben ein gültiges Ticket").

e1-k1-s3-v1, e3-k1-s4-v1: Radausflügler mit zusätzlichem Verkehr
(Fähre statt Bus) liegt nahe am Kontext der Originale
2025-bebb-lk-B4e/B4f; Zahlen geändert (14 → 12 %, 500 → 400 bzw.
300, Schranke 15 → 10 %). Vertretbar als Verfremdung, aber
knapper als sonst in der Bank. – Vorschlag: hinnehmen oder
Kontext tauschen (Fahrgäste mit Hund, Kinderwagen).

Sauber: 106 Zeilen ohne Befund

## Abgleich

Beide Leser: kein gemeinsamer Befund; beide ohne rechnerische
Abweichung.

Nur Zweitleser: die Kontexte der Originale in e2-k1-s2-v1 (samt
umgekehrter Figur und Katalogfrage zu 2024-bebb-lk-B4d),
e1-k1-s2-v1 / e1-k3-s3-v2 / e3-k1-s1-v1 (Gewinnspiel-Buchungen),
e1-k1-s2-v2 (Alleinfahrende), e1-k1-s3-v1 / e3-k1-s4-v1
(Radausflügler, knapp). Der Erstleser hat die Originale der Mappe
nicht gegen die Kontexte gehalten.

Nur Erstleser: Y ohne Einführung in e1-k2-s1-v1 bis v3 und
e3-k1-s5-v1 bis v4 (richtig – ich habe das Y gelesen und nicht
angeschlagen, bank.md verlangt die Erklärung im Text); X ohne
Einführung in zone-f2-v1/v2/v4 (richtig, klein); fehlende
Rundungsvorgabe in zone-f5-v1 bis v4 (richtig); fehlender
Kontext in e2-k2-s1-v1 und e2-k2-s1-v3, weil die Zeilen sich auf
andere Zeilen stützen (richtig – auf einem Blatt steht die
Bezugszeile nicht unbedingt daneben); die Formulierung in
e2-k2-s2-v3 (richtig, die bedingte Lesart liegt nahe).

Widerspruch: keiner; die Befunde ergänzen sich. Zusammen: 7 Zeilen
mit Kontextbefund (Zweitleser), 17 Zeilen mit Text- und
Formbefunden (Erstleser), 89 Zeilen bei beiden ohne Befund.

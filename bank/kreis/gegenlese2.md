# Zweitlesung kreis

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 174
(zone 26, e1 55, e2 49, e3 44)

Prüfung: Alle 174 Zeilen mit einem Skript ausgegeben und einzeln
gelesen. Für jede Zeile mit Zahl in der Lösung wurde der Wert aus dem
Aufgabentext neu berechnet (eigene Formel je id, math.pi, kaufmännische
Rundung auf die Stellen der Lösung) und mit loesung und pruef
verglichen: 154 Zeilen tragen eine Zahl in pruef, 20 keine (Ankreuzen
mit Wortoptionen, Zeichnen, Begründen). Alle Ergebnisse stimmen; 22
Werte liegen nahe an einer Rundungsgrenze und wurden einzeln geprüft,
keiner kippt. Bei den neun Fehler-finden-Zeilen wurde nachgerechnet,
dass die vorgelegte falsche Rechnung die angegebenen Zahlen wirklich
ergibt und die Richtigrechnung stimmt (alle ja). Bei den 13
Ankreuzzeilen wurden alle Optionen durchgerechnet: je genau eine
richtig. Keine doppelte Aufgabe, alle $ und Klammern ausgeglichen,
Bausteinaufrufe gegen mappen/_bausteine.md gelesen (rechenplatz-Höhe
reicht für die verlangten Kreise; kreisdiagramm normiert auf die
Summe, Grad- und Prozentwerte sind daher beide zulässig). Die drei
P10-Originale in der Mappe nachgesehen (2016-OS-K3b, 2024-OS-K4a,
2025-OS-B1e); die Verfremdungen halten Verfahren und Falle.
`python3 werkzeuge/bank-pruef.py kreis`: zone.jsonl, e1.jsonl,
e2.jsonl, e3.jsonl je „Abweichungen 0, Warnungen 0“; gesamt
„Abweichungen: 0, Warnungen: 0“.

## Befunde

kreis-e2-k1-s5-v3: Rundungskette in der Tabelle – die Lösung nennt
r ≈ 8,0 cm und A ≈ 198,9 cm²; wer mit dem Tabellenwert r = 8,0
weiterrechnet, erhält π · 8² ≈ 201,1 cm², mit r ≈ 7,96 ergibt sich
199,1; 198,9 folgt nur aus dem ungerundeten r – Vorschlag: r in der
Lösung mit zwei Stellen (7,96) führen und die Toleranz nennen, oder
u so wählen, dass r glatt ist (u = 44 cm → r ≈ 7,0).

kreis-e1-k2-s7-v1: Rundungskette – mit dem angezeigten u ≈ 207,3 cm
ergibt 250 · 207,3 = 51 825 cm ≈ 518,3 m; die Lösung 518,4 m folgt
nur aus dem ungerundeten u – Vorschlag: u in der Lösung mit zwei
Stellen (207,35) führen oder 100 Umdrehungen (beide Wege 207,3 m).

kreis-e3-k1-s6-v3: Rundungskette – 56,55 + 24 = 80,55, nach der
angezeigten Zwischenzahl gerundet 80,6 cm; die Lösung 80,5 cm folgt
nur aus dem ungerundeten Bogen 56,549 – Vorschlag: Bogen in der
Lösung auf 56,5 runden (dann 80,5) oder Winkel ändern.

kreis-e2-k1-s7-v3, kreis-e2-k1-s7-v4: fraglich: Sprossentext
verlangt „Kreisfläche aus dem Durchmesser …, erst halbieren“, beide
Aufgaben geben den Radius (Kegel r = 45 cm bzw. 1,65 m); sie folgen
der Form 2024-OS-K4a, die die Sprosse selbst nennt und die den
Radius gibt – kein Fehler der Zeilen, Wortlaut der Sprosse im
Katalog passt nur zur Hälfte („aus Durchmesser oder Radius“).

kreis-e3-k3-s2-v3: fraglich: Sprosse „Begründen (warum der Halbkreis
zu 180° gehört)“, die Aufgabe begründet die Verdopplung des Anteils
bei doppeltem Winkel; Merkmal „ohne Rechnung begründen“ erfüllt, der
Inhalt der Sprosse nicht (v1 und v2 bleiben beim Halbkreis) –
Vorschlag: Variante zum Halbkreis oder Sprossentext weiter fassen.

kreis-e1-k6-s4-v3: fraglich: „Diesmal ist der Umfang gegeben“ setzt
v1 voraus; die Zeile steht in der Bank allein und wird einzeln
gezogen – Vorschlag: „Diesmal“ streichen.

Sauber: 167 Zeilen ohne Befund

## Abgleich

Beide Leser: kreis-e1-k2-s7-v1 (Erstleser: keine π-Regel, 518,4 gegen
518,1; Zweitleser: Rundungskette 518,4 gegen 518,3 – beides trifft
dieselbe Zeile, „π-Taste“ einfügen behebt die Kette nicht),
kreis-e2-k1-s7-v3 und kreis-e2-k1-s7-v4 (Sprosse „aus dem
Durchmesser, erst halbieren“, Aufgabe gibt den Radius; der Erstleser
schlägt Durchmesser-Zahlen vor, der Zweitleser hält den Sprossentext
für die Ursache – beide Wege sind gangbar, der Katalogbefund ist der
ehrlichere, weil 2024-OS-K4a den Radius gibt).

Nur Zweitleser: kreis-e2-k1-s5-v3 (Rundungskette Tabelle, 201,1
gegen 198,9), kreis-e3-k1-s6-v3 (Rundungskette 80,6 gegen 80,5),
kreis-e3-k3-s2-v3 (Inhalt der Begründen-Sprosse verfehlt, fraglich),
kreis-e1-k6-s4-v3 („Diesmal“, fraglich).

Nur Erstleser: kreis-e1-k6-s3-v3 (weder π-Regel noch Rundung genannt;
nachgerechnet: mit 3,14 ergibt 190 + 50 · 3,14 = 347,0 statt 347,1 –
Zustimmung, der Zusatz „Rechne mit der π-Taste und runde auf eine
Stelle“ ist nötig). kreis-e2-k1-s7-v3, zweiter Befund (π-Regel;
nachgerechnet: 3,14 · 45² = 6 358,5 → 6 359 statt 6 362 – Zustimmung,
auch wenn die P10-Form den Rechner voraussetzt, sagt der Text es
nicht). kreis-e3-k1-s8-v1 und -v2 (α für den weißen Restwinkel,
sonst in Einheit 3 der Winkel des Ausschnitts – Zustimmung nach der
Regel „ein Buchstabe je Einheit für eine Sache“; Gegensicht: das
Original 2025-OS-B1e nennt den Restwinkel α, β ändert die Falle
aber nicht, also β). kreis-e3-k3-s3-v3 (π-Regel; nachgerechnet:
110/360 · 3,14 · 2240 = 2 149,2 → 2 149 statt 2 150 – Zustimmung).
Anmerkung: Das Kriterium des Erstlesers („beide Wege geben
verschiedene gerundete Ergebnisse“) trifft, konsequent angewandt,
auch die Richtigrechnungen der Fehler-finden-Zeilen ohne π-Regel:
kreis-e1-k6-s1-v3 (188,4 statt 188,5), kreis-e2-k5-s1-v1 und -v2
(113,0 statt 113,1), kreis-e2-k5-s1-v3 (379,9 statt 380,1); dort
lässt die π-Taste-Zahl in der vorgelegten Rechnung den Rechner
erkennen, weshalb der Zweitleser sie nicht als Befund führt.

Zahlen: Zweitleser 6 Befunde, Erstleser 8, gemeinsam 3, nur
Zweitleser 4. Gezählt wurden Befundzeilen (Zweitleser: 6 Zeilen über
7 ids, eine Zeile fasst e2-k1-s7-v3 und -v4; Erstleser: 6 Zeilen
unter Punkt 2 und 2 unter Punkt 3, davon e2-k1-s7-v3 in beiden
Punkten, also 7 ids); „gemeinsam“ und „nur“ zählen ids
(gemeinsam 3, nur Zweitleser 4, nur Erstleser 4 ids plus der
zweite Befund zu e2-k1-s7-v3). Beide Leser: Sauber 167.

# Zweitlesung gleichungen-loesen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 223
(zone 38, e1 56, e2 50, e3 47, e4 32)

Prüfung: Jede Zeile gelesen und aus dem Aufgabentext neu gerechnet.
Mit sympy (Skripte im Scratchpad) nachgerechnet: alle Schnittpunkt-,
Polynomdivisions-, Substitutions-, Hyperbel- und Termgleichheitszeilen
aus e1, die Flächen der Prüfungshöhe (63/16 LE² → 3,94 km²; 32 LE² →
2 km²), die Faktorisierungen in e4, dazu numerisch mit nsolve die
Rechnerzeilen (f(t) = f(t − c) in e3-k1-s5, Schnittpunkte in e3-k2,
Intervalle in e4-k2), alle Nullstellen der Differenz auch außerhalb
des gefragten Bereichs. Log-, e- und Sinuszeilen (e2, e3-k1-s6/s7,
zone-f7) mit math nachgerechnet, einschließlich Rundung auf zwei
Stellen und Umrechnung in Minuten. Alle 193 Zeilen mit pruef-Zahl
stimmen mit der eigenen Rechnung und der Rundung der Lösung überein;
die 30 Zeilen ohne pruef (Begründen, Ankreuzen ohne Zahloption, eine
Zeile ohne Lösung) sind inhaltlich geprüft. 17 Ankreuzzeilen: je
genau eine Option richtig, loesung wortgleich. 13 Fehler-finden-
Zeilen (Zone-Paar und je drei je Einheit): eingebauter Fehler jeweils
wirklich falsch und in sich folgerichtig weitergerechnet,
Richtigrechnung stimmt. Grafiken: Parabel- und Geradenparameter gegen
die abgelesenen Werte gerechnet, alle passend und im Achsenbereich.
`werkzeuge/bank-pruef.py gleichungen-loesen`: 0 Abweichungen,
0 Warnungen. Ohne Befund gezählt, nur als Hinweis: e3-k1-s2-v3 ist
e3-k1-s2-v1 um 1 nach oben verschoben (gleiche Lösungen −2, 0, 2) –
zulässig, aber eine schwache Variante.

## Befunde

e1-k1-s6-v1, e1-k1-s6-v2, e1-k1-s6-v3: [M] Der Sprossentext verlangt
„Lösung an der Abbildung prüfen“; keine der drei Varianten hat eine
Abbildung oder eine Auswahl unter den Lösungen, gefragt sind stets
beide weiteren Schnittpunkte – der zweite Teil der Sprosse wird nicht
geübt. – Eine Variante mit Abbildung (ksys) und Frage nach dem einen
Schnittpunkt im gezeigten Bereich, oder merkmal und Sprossenwahl als
Befund in stand.md vermerken.

e1-k1-s7-v2: [E] Der untere Bogen g(x) = 0,5x² − 5x + 12 hat sein
Minimum −0,5 bei x = 5 und liegt zwischen x = 4 und x = 6 unter dem
Boden (y = 0) – ein Gartentor, dessen Kante in den Boden reicht, und
„der untere Teil“ ist nicht mehr klar begrenzt. – g anheben, z. B.
g(x) = 0,5x² − 5x + 13 und f entsprechend, oder andere Zahlen mit
g > 0 zwischen den Schnittstellen.

e2-k1-s6-v2: [M] Die Variante fragt „Zeige, dass sich die Graphen
von f und f′ bei x = 4,5 schneiden“; das lässt sich durch Einsetzen
beider Werte zeigen, ohne den e-Faktor zu kürzen – das ist genau der
Handgriff von Sprosse 8, nicht das Merkmal von Sprosse 6 (e-Faktor
kürzen, Rest lösen). – Frage offen stellen: „Berechne die Schnittstelle
der Graphen von f und f′.“

e3-k2-s1-v3: [E] Die Differenz 0,2x⁴ − x² − 0,5x + 0,5 hat bei
x ≈ −1,44 ein Minimum von nur 0,0064; am Rechnergraphen sieht das wie
ein dritter (Berühr-)Schnittpunkt (−1,44 | 0,78) aus, und „alle
Schnittpunkte auf zwei Stellen“ ist dort nicht sicher entscheidbar. –
Zahlen ändern, so dass die Graphen links deutlich getrennt bleiben
oder sich klar schneiden (z. B. g(x) = 0,5x + 1).

Sauber: 217 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k1-s6-v1, e1-k1-s6-v2, e1-k1-s6-v3 – „Lösung an der
Abbildung prüfen“ wird ohne Abbildung nicht geübt. e1-k1-s7-v2 – der
untere Bogen g reicht zwischen x = 4 und x = 6 unter den Boden.
e2-k1-s6-v2 – die „Zeige“-Fassung an genannter Stelle weicht von
v1/v3 ab (Erstleser: Form; Zweitleser: sie ist durch Einsetzen lösbar
und übt damit Sprosse 8, nicht das Kürzen). e3-k2-s1-v3 – Beinahe-
Berührung bei x ≈ −1,44, beide schlagen g(x) = 0,5x + 1 vor
(nachgerechnet: Minimum der Differenz dann 0,51, zwei klare
Schnittpunkte).

Nur Erstleser:
- e1-k3-s3-v1, e1-k3-s3-v3 (pruef ohne Gerüstzahlen 200/800 bzw.
  10/14): bestätigt als Prüflücke, nicht als Fehler – Lösung richtig,
  pruef prüft nur die Zwischenzahlen; Ergänzung sinnvoll.
- e3-k3-s1-v1 (pruef [0, 4] aus der falschen Gleichung): bestätigt –
  pruef prüft die Zahlen des Schülerfehlers, nicht die Richtigstellung.
- e3-k3-s1-v1, e3-k1-s0-v2 (Bedingung ohne Bezugszeitpunkt, „ab
  jetzt“ macht p(4) = p(0) + 30 bzw. w(2) = w(0) + 30 vertretbar):
  bestätigt, schwach – die Schreibweise p(x)/w(t) deutet auf einen
  beliebigen Zeitpunkt, der Kasten übersetzt ebenso knapp; „zu jedem
  Zeitpunkt“ macht Fehler und Ankreuzen eindeutig.
- e1-k1-s9-v1, v2, v3 (Funktionsname u neben u = x² derselben
  Einheit): bestätigt – bank.md „ein Buchstabe je Einheit für eine
  Sache“, u steht in e1 für die Substitution (s0-v3, s5, k3); von mir
  übersehen.
- zone-f5-v2 (e^x = 0 unter dem Merkmal „e hoch null direkt“):
  bestätigt – die Aufgabe passt zur Fertigkeit („nie null“), aber
  nicht zum Merkmal der Zeile; Aufgabe oder merkmal angleichen.
- e1-k1-s0-v1 (Polynomdivision führt ebenfalls zum Ziel): bestätigt,
  schwach – der Kasten erlaubt Polynomdivision mit einer „durch
  Probieren“ gefundenen Lösung, x = 1 ist ratbar; Substitution ist der
  passende Weg, ein anderer Distraktor macht die Option eindeutig.
- e4-k1-s1-v5 (einzige Grundfall-Variante mit ≥, isolierte Lösung
  x = −6): bestätigt – die Variante ändert neben den Zahlen auch den
  Gleichheitsfall, also mehr als das Merkmal.
- e4-k2-s1-v2 (ohne Rechner- und Rundungsangabe, von Hand lösbar):
  bestätigt für die fehlende Rundungsangabe (Lösung auf zwei Stellen
  gerundet, Aufgabe sagt es nicht); die Handlösbarkeit selbst ist kein
  Fehler.
- e3-k1-s0-v4 (Maßstab in der Vorstufe): nicht bestätigt – der
  Erkennungsschritt „Was heißt die Bedingung?“ nennt ausdrücklich
  „s(x) − s(x − d) = h in Längeneinheiten“; die Umrechnung 20 m → 2 LE
  gehört zur Übersetzung, die er erkennen lassen soll.
- e2-k3-s1-v1 (Benennung „mitgezogen“ statt „übergangen“): nicht
  bestätigt – „mitgezogen“ ist die Wortwahl der Typischen Fehler der
  Mappe, der Fehler ist klar benannt und die Richtigrechnung stimmt;
  höchstens eine Stilfrage.

Nur Zweitleser: keine – alle vier Befunde des Zweitlesers hat auch
der Erstleser (e2-k1-s6-v2 mit anderer Begründung).

Widersprüche: e3-k1-s0-v4 – Erstleser sieht das Merkmal von s3
vorweggenommen, Zweitleser hält die Maßstabsumrechnung für Teil des
Erkennungsschritts. e2-k3-s1-v1 – Erstleser hält die Benennung des
Fehlers für falsch, Zweitleser nicht.

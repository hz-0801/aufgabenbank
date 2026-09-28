# Zweitlesung abstaende

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 174
(zone 31, e1 41, e2 29, e3 39, e4 34)

Prüfung: Jede Zeile wurde aus dem Aufgabentext neu gerechnet, mit
einem eigenen sympy-Skript (Scratchpad, nicht im Repo): Beträge,
Hessesche Normalform, Lotfußpunkte über Laufpunkt und Skalarprodukt,
Spiegel- und Abstandspunkte auf Lotgeraden und Strecken, Ebenen- und
Geradenabstände, Teilungspunkte, Sinus-Strecken; dazu die
Lagebedingungen (Punkt in Ebene, Richtung parallel, rechter Winkel,
Symmetrie) als Zusicherungen. 135 Zeilen tragen eine Zahl in
`pruef`; alle 135 stimmen mit meiner Rechnung und mit `loesung`
überein (Rundung inbegriffen). 39 Zeilen sind ohne Zahl (20
Ankreuzen, 12 Begründen, 7 Deuten/Beschreiben); sie wurden gelesen
und auf Eindeutigkeit und richtige Option geprüft. Alle 13
Fehler-finden-Zeilen: der eingebaute Fehler ist falsch und
reproduziert die vorgelegten Zahlen, die Richtigrechnung stimmt.
`python3 werkzeuge/bank-pruef.py abstaende`: alle fünf Dateien
Abweichungen 0, Warnungen 0. Keine doppelte id, keine doppelte
Aufgabe, $ und Klammern in allen Feldern ausgeglichen.

## Befunde

e3-k1-s6-v1, e3-k1-s6-v2, e3-k1-s6-v3: Die Bewegungsrichtung ist
nur bis auf das Vorzeichen bestimmt. „fährt auf der Geraden g mit
Richtungsvektor (3 | 4 | 0) auf k zu" legt nicht fest, ob der
Roboter in Richtung +(3 | 4 | 0) oder −(3 | 4 | 0) fährt; die
Lösung wählt stillschweigend die Seite Q − 0,6·(3 | 4 | 0)/5, die
Seite Q + … (6,36 | 8,48 | 0) ist ebenso richtig. Dasselbe in v2
und v3. – Vorschlag: einen Startpunkt nennen („startet in
(0 | 0 | 0)" bzw. „bewegt sich in Richtung (3 | 4 | 0)") oder
sagen, auf welcher Seite von k die Rasenfläche, das Wasser liegt.

e4-k1-s2-v1, e4-k1-s2-v2: Die Begründung trägt nicht, solange der
Abstand nur „etwa 3,1" (tatsächlich √9,8 ≈ 3,13) bzw. „etwa 3,5"
(2,5·√2 ≈ 3,54) beträgt: Ist der wahre Abstand größer als 3,1, hat
ohnehin kein Punkt von t den Abstand 3,1 – der Lotfußpunkt spielt
dann keine Rolle. Die Lösung argumentiert aber „nur L hat den
Abstand 3,1". – Vorschlag: wie v3 formulieren („dass jeder Punkt
der Strecke weiter als 3 von F entfernt ist") mit exaktem Abstand,
etwa F so legen, dass der Abstand genau 3 ist, oder die
Zahlenangabe streichen und nur „Begründe mit einer Zeichnung, dass
der Punkt kleinsten Abstands nicht auf GJ liegt" verlangen.

e1-k2-s7-v2: Die Sprosse nennt „widerlegen" und „untere Schranke
nachweisen"; v2 ist die einzige Variante mit wahrer Aussage und
löst eine quadratische Gleichung, statt eine Schranke zu zeigen.
Als Kontrastvariante zum Raten-Verhindern vertretbar, dann aber
ist das Merkmal („Schranke über ein nichtnegatives Quadrat") für
diese Zeile nicht erfüllt. – Vorschlag: Radius auf 4 senken (dann
9 + 9 = 18 > 16, Aussage falsch, Schranke √18) oder die Zeile als
bewusste Gegenprobe im Merkmal kennzeichnen.

e1-k2-s2-v2: „30 % länger als deren Abstand" – „deren" kann auf
die Mittelpunkte (7 m, so die Lösung) oder auf die Kanten bezogen
werden; die parallelen Kanten AB und CD haben den Abstand √45 ≈
6,71 m, das gäbe 8,72 m. – Vorschlag: „30 % länger als der Abstand
der beiden Mittelpunkte".

e3-k2-s3-v2: „Wie hoch über dem Boden" – der Boden ist nicht
festgelegt (andere Zeilen sagen „die xy-Ebene ist der Boden").
– Vorschlag: „; die xy-Ebene ist der Boden" ergänzen.

e3-k1-s7-v3, e3-k1-s7-v4: „BC verläuft in der Höhe 3 genau über
der z-Achse" ist schief – eine waagerechte Strecke kann nicht über
der senkrechten z-Achse verlaufen; gemeint ist, dass BC die
z-Achse in der Höhe 3 kreuzt (Mittelpunkt (0 | 0 | 3)). Die
Rechnung III stimmt. – Vorschlag: „BC kreuzt die z-Achse in der
Höhe 3" oder „der Mittelpunkt von BC ist (0 | 0 | 3)".

e2-k1-s0-v2: nahezu wortgleich mit e1-k1-s0-v2 („Auf der
Lotgeraden durch F … Punkt gesucht, der von E den Abstand … hat");
nur Zahl und Optionen unterscheiden sich. Keine Dublette im Sinn
des Skripts, aber dieselbe Situation zweimal in der Vorstufe. –
Vorschlag: in e2 eine andere Rückwärts-Situation (Spiegelpunkt,
Punkt auf einer Strecke) wählen.

Sauber: 163 Zeilen ohne Befund

## Abgleich

Beide Leser: keine – die Befundlisten sind disjunkt.

Nur Erstleser (11 Befunde auf 10 Zeilen), nach Prüfung:
- e1-k3-s3-v1 (pruef ohne Minutenwert): bestätigt, 6,4 min steht
  in Antwortgerüst und Lösung, aber nicht in pruef.
- e4-k1-s5-v3 (pruef nur z statt Tripel): bestätigt als
  Uneinheitlichkeit gegenüber v1; rechnerisch ist pruef richtig.
- e1-k2-s3-v3 (Rundung 559 m nicht verlangt): bestätigt, klein.
- e1-k3-s3-v1 (Rundung 6,4 min nicht verlangt): bestätigt, klein.
- e1-k3-s3-v2 (Bezugspunkt der Funkreichweite): bestätigt, der
  Bezug auf S ist nur naheliegend, nicht gesagt.
- e2-k1-s3-v2 (unendlich viele P): bestätigt in der Form „Lösung
  als Beispiel kennzeichnen"; der Aufgabentext („Gib einen solchen
  Punkt an") ist selbst in Ordnung.
- e3-k1-s2-v1 (A, B, E nicht eingeführt, E sonst Ebene): bestätigt,
  bank.md verlangt erklärte Buchstaben.
- e3-k1-s2-v3 („Welcher Punkt ist F?" unscharf): bestätigt, klein;
  Lösung verlangt Deutung und Koordinaten, die Frage nur eines.
- zone-f1-v2 (nur Betrag, kein Verbindungsvektor): bestätigt gegen
  das Merkmal; als eine von zwei sehr leichten Zeilen vertretbar.
- zone-f5-v1 (kein Test auf senkrecht): nicht als Befund
  bestätigt – v1 und v2 decken die Fertigkeit gemeinsam ab, das
  Merkmal nennt beides als Paar; „– senkrecht?" schadet aber nicht.
- e3-k1-s4-v3 (Erläutern mit form teil): bestätigt für das Feld
  form (gehört auf „text"); die Tätigkeit „Erläutern" ist die des
  Originals 2021-be-gk-B3g und sollte bleiben, nicht in eine
  Rechenaufgabe umgebaut werden.

Nur Zweitleser (7 Befunde auf 11 Zeilen):
- e3-k1-s6-v1/v2/v3: Bewegungsrichtung nur bis auf das Vorzeichen.
- e4-k1-s2-v1/v2: „etwa 3,1"/„etwa 3,5" trägt die Begründung nicht.
- e1-k2-s7-v2: wahre Aussage statt Widerlegung/Schranke der Sprosse.
- e1-k2-s2-v2: „deren Abstand" zweideutig (Mittelpunkte/Kanten).
- e3-k2-s3-v2: Boden nicht als xy-Ebene festgelegt.
- e3-k1-s7-v3/v4: „genau über der z-Achse" schief formuliert.
- e2-k1-s0-v2: Beinahe-Dublette zu e1-k1-s0-v2.

Widersprüche: keine. Einziger Unterschied in der Bewertung:
e3-k1-s4-v3 – der Erstleser stellt Umbau zur Rechenaufgabe zur
Wahl, der Zweitleser hält die Erläuterform des Originals für
richtig und würde nur form auf „text" setzen.

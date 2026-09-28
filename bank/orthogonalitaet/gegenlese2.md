# Zweitlesung orthogonalitaet

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 164
(zone 26, e1 43, e2 35, e3 34, e4 26)

Prüfung: Jede Zeile mit Zahl in `pruef` wurde aus dem Aufgabentext
mit sympy nachgerechnet (Skript im Scratchpad: Skalarprodukte,
Beträge, Gleichungen und Gleichungssysteme, Lotfußpunkte, Kreuzprodukt
für die Schnittgeraden, Oberflächen der Pyramiden über die
Dreiecksflächen); 122 Zeilen mit Zahl, alle stimmen mit `pruef` und
mit dem Ergebnis in `loesung` überein. Die 42 Zeilen ohne Zahl
(Ankreuzen, Begründen, drei Fehler-finden ohne Ergebniszahl) wurden
gelesen und auf Logik geprüft. `python3 werkzeuge/bank-pruef.py
orthogonalitaet`: Abweichungen 0, Warnungen 0 in allen fünf Dateien.
Geprüft: 33 Ankreuzen-Zeilen (je genau eine Option richtig, Lösung
nennt sie wortgleich), 13 Fehler-finden-Zeilen (eingebauter Fehler
falsch, angegebene Berichtigung richtig – alle in Ordnung), 39
Originale gegen Abschnitt 2 der Mappe (Zahlen überall verfremdet,
Prüfkennung GK/LK passt zum Papier).

## Befunde

e2-k2-s3-v3: nicht eindeutig lösbar. Mit A(0|0|3), B(6|0|3),
C(6|y|5) ist BA∘BC = (−6|0|0)∘(0|y|2) = 0 für jedes y; „Bestimme y“
hat keine Antwort, die Lösung wählt willkürlich y = 4 und rechnet
damit |BC|. – Vorschlag: A(0|4|3), B(6|0|3), C(8|y|5): BA∘BC =
−12 + 4y = 0, also y = 3, |BC| = √17 ≈ 4,1 m; pruef [3, 4.1231].

e2-k1-s5-v2, e2-k1-s5-v3: Lösung in Schablonenschreibweise mit
Vorzeichenmüll: „$1(x - 0) + 3(y - 1) + -1 \cdot -3 = 1x + 3y +0 =
0$“ bzw. „$3(x - 2) + -2(y - 0) + 0 \cdot 2 = 3x + -2y -6 = 0$“. –
Vorschlag: „$x + 3(y - 1) + (-1) \cdot (-3) = x + 3y = 0$“ und
„$3(x - 2) - 2y + 0 = 3x - 2y - 6 = 0$“.

e4-k1-s1-v2, e4-k1-s1-v3: „$\sqrt{25} \approx 5$“ und „$\sqrt{9}
\approx 3$“ sind exakt, also „=“; in v2 außerdem „$3 - 1\lambda = 0$“
statt „$3 - \lambda = 0$“ (Schablone).

e4-k3-s3-v2, e4-k3-s3-v3, e2-k2-s3-v1: Anwendung ist eine
eingekleidete Kettenzeile mit denselben Zahlen: Kamera = e4-k1-s2-v1
(C, D, F_k und k = 4 identisch), Pipeline = e4-k1-s1-v4 (P(4|0|1),
g durch O mit (2|2|1), Ergebnis identisch), Regal = e2-k1-s4-v3
(9 × 12, h = 15, V = 1620, nur Länge und Breite vertauscht). Auf
einem Blatt stehen so zwei Aufgaben mit gleicher Rechnung. –
Vorschlag: eigene Zahlen für die drei Anwendungszeilen.

e2-k1-s0-v2: die zitierte Aufgabenstellung „Zeige, dass das Dreieck
$ABC_t$ für jedes $t$ bei $A$ rechtwinklig ist.“ steht wortgleich in
e1-k3-s0-v1; ebenso sind e3-k1-s0-v1 (Gerade h senkrecht E) und
e3-k1-s0-v2 (Ebenen E, F_a senkrecht) nur umformulierte e1-k1-s0-v1
und e1-k1-s0-v3. Grund ist die Katalogstruktur (Erkennungsschritte
vor E1 und noch einmal als Vorstufe vor E2/E3); dennoch Dubletten im
Sinn von „keine Aufgabe doppelt“. – Vorschlag: in e2 und e3 andere
Situationen zitieren (Lot, Mittelsenkrechte, Quaderdiagonalen,
Prisma-Kante).

e1-k5-s2-v2: „$6t - 6t = 0$“ ist der Term des Merkkastens Einheit 1
(Mappe Zeile 46: „6t − 6t + 0 = 0“); Sperre auf Terme aus dem
Kasten. – Vorschlag: „$10t - 10t = 0$“.

e1-k4-s5-v3, e1-k4-s5-v4: prüfen nur die Ecke B („bei B nicht
rechtwinklig“), sprosse_text und merkmal verlangen „an allen drei
Ecken“. Die Zeilen folgen dem Original 2019MgrundlegendAAGLAA212-a,
das der Katalog unter dieser Prüfungshöhe führt – Katalogbefund für
stand.md, nicht Zeilenfehler; merkmal könnte „oder an der behaupteten
Ecke“ ergänzen.

e2-k1-s2-v3: die Verfremdung verlegt den Scheitel. Im Original
2024MgrundlegendBAGLAA2WTR2-1f sitzt der rechte Winkel bei M, das
Skalarprodukt ist linear (25 − 3t); die Bankzeile setzt ihn bei S_t
und wird so quadratisch, wie die Sprosse es verlangt. Die Zeile ist in
sich richtig, aber nicht „gleiches Verfahren“ wie das Original; der
Katalog ordnet ein lineares Original der quadratischen Sprosse zu –
Katalogbefund für stand.md.

e3-k2-s3-v1: der „Mast“ zeigt in Richtung (2|0|−8), also nach unten
(z fällt); als stehender Mast liest sich (−2|0|8). Realismus schwach:
ein Mast steht lotrecht, nicht senkrecht zum Hang – eher „Anker“ oder
„Stützstrebe“.

e3-k2-s3-v3: nutzt die Regel Ebene gegen Ebene (Skalarprodukt der
Normalenvektoren), sprosse_text nennt die Kollinearität mit dem
Normalenvektor. Kleine Abweichung vom Typnamen; inhaltlich richtig.

e1-k5-s3-v1, e1-k5-s3-v3: berechnen die Hypotenuse (Stange AC,
Strebe AC), sprosse_text nennt „Kathetenlängen“. Klein; v2 passt.

e4-k3-s3-v1: pruef trägt 268 (gerundet) statt des ungerundeten Werts
268,33 (bank.md: „bei Rundungsaufgaben der ungerundete Wert“);
rundet gleich, also nur formal.

e2-k1-s3-v2: die auszusiebende Lösung q = 11 ist zugleich die des
Originals 2023-bebb-lk-B3f („Lösung 11 nicht ausschließen“); ein
Ergebnis des Originals, das die Sperre eigentlich meidet. Klein.

Hinweis (nicht als Befund gezählt): Alle neun Fehler-finden-Zeilen
mit Zahlen übernehmen die Punkte einer Kettenzeile derselben Einheit
(e1-k5-s1-v1 = e1-k4-s1-v2, e1-k5-s1-v2 = e1-k4-s3-v1, e1-k5-s1-v3 =
e1-k4-s5-v2, e2-k2-s1-v1 = e2-k1-s1-v1, e2-k2-s1-v2 = e2-k1-s3-v1,
e2-k2-s1-v3 = e2-k1-s4-v1, e3-k2-s1-v1 = e3-k1-s1-v1, e3-k2-s1-v2 ≈
e3-k1-s3-v1, e3-k2-s1-v3 = e3-k1-s5-v1). Kein Regelverstoß, aber auf
einem Blatt liefert die Kettenzeile die Berichtigung vorweg.

Sauber: 143 Zeilen ohne Befund

## Abgleich

Beide Leser (17 Zeilen): e2-k2-s3-v3: y beliebig, nicht lösbar
(Vorschläge verschieden, beide nachgerechnet richtig) · e2-k1-s5-v2,
e2-k1-s5-v3: Vorzeichenmüll in der Lösung · e4-k1-s1-v2, e4-k1-s1-v3:
„≈“ bei exaktem Wert, „1λ“ · e4-k3-s3-v2, e4-k3-s3-v3, e2-k2-s3-v1:
Anwendung mit den Zahlen einer Kettenzeile · Dubletten e1-k1-s0-v1/
e3-k1-s0-v1, e1-k1-s0-v3/e3-k1-s0-v2, e1-k3-s0-v1/e2-k1-s0-v2 ·
e1-k4-s5-v3, e1-k4-s5-v4: nur Ecke B statt drei Ecken · e3-k2-s3-v1:
Mastrichtung nach unten · e3-k2-s3-v3: Ebene gegen Ebene statt
Kollinearität · e1-k5-s3-v1, e1-k5-s3-v3: Hypotenuse statt Katheten.

Nur Erstleser (8 Zeilen):
- e1-k5-s1-v1 (Korrektur der Vektoren): bestätigt – die vorliegende
  Datei trägt schon den korrigierten Stand (1|2|2)∘(2|−1|0) = 0, den
  ich nachgerechnet habe.
- zone-f4-v1, zone-f4-v2, zone-f4-v3 („Faktor“ ohne Richtung):
  bestätigt – 1/2, −1/3 und 2/3 sind ebenso richtig wie 2, −3 und
  1,5; der
  Fragesatz sollte die Richtung festlegen; übersehen.
- e1-k3-s0-v3 (Option „Skalarprodukt muss für jeden Wert null sein“
  für Gerade gegen Ebene): bestätigt – die richtige Option trägt für
  dieses Paar die falsche Prüfregel, Stamm auf zwei Richtungen
  ändern; übersehen.
- e4-k3-s1-v1 (Kims „Fehler“): bestätigt – ohne Gleichschenkligkeit
  ist auch die als richtig angegebene Höhe |MT_λ| falsch (Höhe ist
  der Abstand zur Geraden RS), mit Gleichschenkligkeit ist Kims
  Aussage richtig (|RT|² = |RM|² + |MT|², |RM| fest); die Aufgabe ist
  so nicht stimmig; übersehen.
- e2-k2-s3-v2 (Zeltseile statt Quader): teilweise bestätigt – die
  Abweichung vom Typnamen stimmt; ob alle drei Anwendungen Quader
  sein müssen oder die Einheit auch ihre anderen Typen einkleiden
  darf, ist Ermessen des Chats (Typtreue gegen Vielfalt).
- e4-k3-s3-v1 (Zufahrt: Abstand statt Spitzenwinkel): teilweise
  bestätigt wie e2-k2-s3-v2 – Typname verfehlt, aber die Lotbedingung
  ist der Kern der Einheit; die Zeile ist in sich richtig.

Nur Zweitleser (4 Zeilen): e1-k5-s2-v2 (Term „6t − 6t“ aus dem
Merkkasten, Sperre) · e2-k1-s2-v3 (Verfremdung verlegt den Scheitel;
Original linear, Sprosse quadratisch – Katalogbefund) · e4-k3-s3-v1
(pruef 268 gerundet statt 268,33) · e2-k1-s3-v2 (auszusiebende Lösung
11 wie im Original). Der Hinweis zur Zahlenübernahme in den
Fehler-finden-Zeilen deckt sich mit der Entscheidung des Erstlesers,
sie nicht als Befund zu führen.

Widersprüche: keine in der Sache. Bei den drei Dubletten setzt der
Erstleser die Änderung in e1 an, der Zweitleser in e2/e3 – weil der
Erkennungsschritt laut bank.md einmal in der ersten Einheit steht und
die Vorstufen von e2/e3 die Wiederholung sind; eine Ortsfrage für den
Chat, kein Gegensatz im Befund.

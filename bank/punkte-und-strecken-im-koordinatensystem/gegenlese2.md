# Zweitlesung punkte-und-strecken-im-koordinatensystem

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 255
(zone 43, e1 37, e2 42, e3 43, e4 47, e5 43)

Prüfung: Jede Zeile gelesen (aufgabe, antwort, loesung, pruef, grafik,
loesungsgrafik, merkmal). Rechnungen mit einem eigenen Skript (sympy)
nachgerechnet: alle Verbindungsvektoren und Längen, Skalarprodukte der
Rechteck-, Winkel-, Thales- und Inkreiszeilen, Parallelogramm-, Trapez-
und Drachennachweise (Gegenseitenvektoren, Faktoren, Seitenlängen),
Teilpunkte, Umkreismittelpunkte, Wurzelgleichungen, Lotfußpunkte und
Radien der Drehungen, Würfel in der Pyramide, Punkt-in-Dreieck-Probe
der Höhenfußpunkte (e1 s8), die Kantenzüge der Lösungsgrafiken
(Stützpunkt plus Richtung trifft die nächste Ecke) und die Ebenheit der
Vierecke (Determinante). Alle 190 Zeilen mit pruef-Zahl stimmen mit der
eigenen Rechnung überein; kein Rechenfehler in loesung. 29
Ankreuzzeilen je Option gegen Text und Sonderfälle geprüft (davon 2 mit
Befund), 16 Fehler-finden-Zeilen: jeder eingebaute Fehler ist falsch,
jede Richtigrechnung stimmt. bank-pruef.py: 0 Abweichungen, 1 Warnung
(e4 k1 s10: Prüfungshöhe ohne Original 2 Zeilen statt 3). Hinweis ohne
Kennzeichen: e4-k1-s10-v7/v8 und e5-k1-s3-v1–v3 tragen eine
Prüfkennung („(Abitur 2022 GK)“, „(Abitur 2024 GK)“), aber original
null, weil das Original nicht in der Mappe steht (stand.md nennt es).

## Befunde

zone-f7-v2: [A] „Welches Dreieck hat zwei gleich lange Seiten?“ – auch
das gleichseitige Dreieck hat zwei gleich lange Seiten (Sonderfall), zwei
Optionen stimmen – „genau zwei gleich lange Seiten“ schreiben.

zone-f7-v3: [A] Ein Viereck mit zwei Paaren paralleler Gegenseiten ist
nach der Schuldefinition (mindestens ein Paar paralleler Seiten) auch
ein Trapez; zwei Optionen stimmen – Option „Trapez“ durch „Rechteck“
ersetzen oder „welches Viereck genau?“ fragen.

e1-k1-s2-v1, e1-k1-s2-v2, e1-k1-s2-v3: [E] Die vier Punkte liegen je
auf Würfelkanten, aber nicht in einer Ebene (Determinante 4, 6, −6);
„das Viereck PQRS“ ist damit kein ebenes Viereck, anders als im
Original (I, J, K, L dort eben, ein Trapez) – Punkte so wählen, dass
sie in einer Ebene liegen (z. B. zwei Gegenseiten parallel wie in
e4-k1-s5-v2).

e1-k1-s4-v1, e1-k1-s4-v3: [E] loesung: „ein Drittel ihrer Länge von
vorn“ – die Kante mit $x_1$ und $x_3$ fest läuft in $x_2$-Richtung
(im Schrägbild von links nach rechts), „von vorn“ passt nicht – „ein
Drittel der Kantenlänge von $(5 | 0 | 3)$ bzw. $(3 | 0 | 3)$ aus“.

e1-k1-s6-v2, e1-k1-s6-v3: [E] Sprachfehler im Aufgabentext: „Der
Beet“, „Der Bodenplatte“ – „Das Beet“, „Die Bodenplatte“.

e1-k1-s8-v3, e1-k1-s8-v4: [M] merkmal „Projektion und Punktspiegelung
kombinieren“, die Aufgaben (Höhenfußpunkt über die Projektion, Original
2018MgrundlegendAAGLAA212-b) enthalten keine Punktspiegelung – merkmal
für diese Hälfte der Sprosse anpassen („Projektion der Spitze
entscheidet über die Lage des Höhenfußpunkts“).

e3-k1-s0-v4: [E] „Viereck $KLMN$: Welcher Vektor liegt
$\overrightarrow{KL}$ gegenüber und zeigt in dieselbe Richtung?“ – in
einem beliebigen Viereck zeigt kein Gegenseitenvektor in dieselbe
Richtung – „Parallelogramm $KLMN$“.

e3-k1-s3-v3: [E] Für $p = 2$ ist $C(1 | 2 | 0)$ der Mittelpunkt von
$AB$, das Dreieck entartet; „für jedes $p$ gleichschenklig“ stimmt dann
nicht – „für jedes $p \ne 2$“ (wie in v2 „$p \ne 3$“).

e3-k1-s10-v1, e3-k1-s10-v2: [E] „Koordinaten von $D$?“ unterstellt
einen einzigen Punkt; im Raum erfüllen alle Punkte eines Kreises
(Mittelsenkrechtebene von $AB$ geschnitten mit der Kugel um $A$) die
beiden Bedingungen, das Original fragt nach „einem solchen Punkt“ –
„Gib einen solchen Punkt $D$ an.“

e3-k2-s2-v1: [E] „Für gleichschenklig genügt es, zwei Seitenlängen zu
vergleichen. Welche?“ – ohne gegebene Basis oder Spitze lässt sich
„welche“ nicht beantworten (man muss dann bis zu drei Längen
vergleichen) – „wenn die Basis genannt ist“ ergänzen.

e4-k1-s3-v2: [M] $A(0 | 1 | 1)$, $B(4 | 1 | 4)$, $C(4 | 6 | 4)$,
$D(0 | 6 | 1)$ ist sogar ein Quadrat ($\overrightarrow{AB} \circ
\overrightarrow{AD} = 0$); der Nachweis „Raute“ stimmt, als Beispiel
der Sprosse ist der Sonderfall ungünstig – eine Ecke so ändern, dass
kein rechter Winkel entsteht.

e5-k1-s3-v1, e5-k1-s3-v2, e5-k1-s3-v3: [E] „Welche Ecke hat danach …?“
mit Gerüst „(__ | __ | __)“ – offen, ob die Ecke vor der Verschiebung
(loesung zuerst: $(0 | 2 | 2)$) oder ihr Bild (pruef: $(-1 | 1 | 3)$)
einzutragen ist – „Gib die Koordinaten der Ecke nach der Verschiebung
an“ oder Gerüst „vorher (__|__|__), nachher (__|__|__)“.

e5-k1-s6-v1, e5-k1-s6-v2, e5-k1-s6-v3: [E] Der Text sagt nicht, über
welcher Seite des Rechtecks der First verläuft; der Anteil (30 %,
20 %, 24 %) hängt davon nicht ab, die Streifenbreite $d$ der loesung
(1,2 m, 1 m, 1,2 m) schon (bei der anderen Lage 1,5 m, 1,4 m, 1,8 m) –
„der First verläuft parallel zur 10-m-Seite“ (bzw. 14 m, 15 m)
ergänzen.

Sauber: 232 Zeilen ohne Befund

## Abgleich

Beide Leser:
- zone-f7-v2: „gleichseitig“ erfüllt auch „zwei gleich lange Seiten“,
  zwei Optionen richtig.
- e1-k1-s2-v1–v3: die vier Punkte liegen nicht in einer Ebene (gleiche
  Determinanten 4, 6, −6), anders als das Original.
- e1-k1-s4-v1, v3: „ein Drittel … von vorn“ beschreibt die Lage auf
  der Kante in $x_2$-Richtung falsch.
- e1-k1-s6-v2, v3: „Der Beet“, „Der Bodenplatte“.
- e1-k1-s8-v3, v4: merkmal nennt eine Punktspiegelung, die diese
  Varianten nicht haben.
- e3-k1-s3-v3: für $p = 2$ entartet das Dreieck, „$p \ne 2$“ fehlt.
- e3-k1-s10-v1, v2: $D$ ist im Raum nicht eindeutig (ein ganzer Kreis
  erfüllt die Bedingungen).

Nur Erstleser:
- e3-k1-s9-v1–v3 (loesung ohne „z. B.“ bei offener Frage nach $T$):
  bestätigt – z. B. erfüllt auch das Spiegelbild von $P$ an der
  Mittelsenkrechtebene von $OQ$ oder jedes Drehbild von $P$ um die
  Gerade $OQ$ die Bedingungen; die gerechnete Wahl stimmt, es fehlt nur der
  Hinweis auf weitere Lösungen (Form der loesung, kein Rechenfehler).
- e3-k1-s10-v3, v4 (loesung ohne „z. B.“ bei zwei frei wählbaren
  Punkten): bestätigt – die Aufgabe fragt nach „zwei möglichen“
  Punkten, die loesung zeigt eine Wahl; gleicher Formbefund wie oben.
- e4-k1-s9-v1, v2 (vier richtige Ecken, loesung nennt zwei):
  bestätigt – nachgerechnet, $Q \pm (4 | -3 | 0)$ bzw. $Q \pm
  (3 | 0 | 4)$ ergeben $(6 | -2 | 5)$, $(-2 | 4 | 5)$ bzw.
  $(6 | 6 | 8)$, $(0 | 6 | 0)$, alle in der Ebene und im Abstand 5.
- e5-k1-s8-v3 (Drehsinn offen, $C^*$ kann auch unter der Ebene
  liegen): bestätigt – der Text sagt „gedreht“, nicht „gekippt“, und
  schließt die Gegenrichtung nicht aus; ich hatte das gesehen, aber
  wegen der naheliegenden Deutung (Kippen über die Kante) nicht als
  Befund geführt – der Erstleser hat recht, v4 formuliert es sauberer.
- e5-k1-s2-v2, v3 (Lage im Text vorgegeben, merkmal „Lage selbst
  festlegen“ nicht geübt): bestätigt – mit „Ecke im Ursprung, Kanten
  auf den positiven Achsen“ bleibt nur Ablesen wie in s1; nur v1 lässt
  die Wahl.
- e5-k1-s8-v5, v6 (Ebenengleichungen, die der Eintrag nicht
  einführt): bestätigt als Schreibform-Befund, nicht als Rechenfehler
  – die Ungleichungen stimmen (Ecke $(k | k | k)$ ergibt genau 12 bzw.
  6); der vorgeschlagene Querschnitt (Seite $4 - \frac23 z \ge 2{,}4$
  für $z \le 2{,}4$) ist nachgerechnet und kommt ohne Ebenen aus.
- e5-k1-s8-v7, v8 (Eckenzahl „für jedes $s$ ein Dreieck“, vom
  Erstleser korrigiert): nicht mehr sichtbar, ich habe die korrigierte
  Fassung gelesen; sie stimmt (Dreieck für $2 \le s \le 5$ bzw.
  $3 \le s \le 6$, sonst Trapez) – die Korrektur ist bestätigt.

Nur Zweitleser:
- zone-f7-v3: „Trapez“ ist nach der Schuldefinition auch richtig
  (Parallelogramm als Sonderfall des Trapezes).
- e3-k1-s0-v4: in einem beliebigen Viereck $KLMN$ zeigt kein
  Gegenseitenvektor in dieselbe Richtung; „Parallelogramm“ fehlt.
- e3-k2-s2-v1: „Welche zwei Seiten?“ ist ohne gegebene Basis nicht
  beantwortbar.
- e4-k1-s3-v2: das Rautenbeispiel ist ein Quadrat (Skalarprodukt 0).
- e5-k1-s3-v1–v3: offen, ob die Ecke vor oder nach der Verschiebung
  einzutragen ist (loesung nennt beide, pruef nur das Bild).
- e5-k1-s6-v1–v3: die Lage des Firsts fehlt; der Anteil bleibt gleich,
  die Streifenbreite der loesung nicht.

Widersprüche: keine – die Prüfkennung bei original null werten beide
nicht als Befund; die Einordnung von e1-k1-s4 (Erstleser: Lösung,
Zweitleser: Eindeutigkeit) unterscheidet sich nur im Abschnitt.

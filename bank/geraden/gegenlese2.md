# Zweitlesung geraden

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 173
(zone 30, e1 39, e2 44, e3 29, e4 31)

Prüfung: Jede Zeile gelesen; jede Lösung mit Ziffern in einem
sympy-Skript (Scratchpad, nicht im Repo) aus dem Aufgabentext
nachgerechnet: Verbindungsvektoren, Beträge, Skalarprodukte,
Punktproben, Teilpunkte, Lagebeziehungen (Rang der Richtungsvektoren
plus Gleichsetzen), Schnitt- und Lotpunkte, quadratische
Abstandsgleichungen, Scharen, Neigungen, Maßstäbe; dazu die
Konsistenz der Körper (Würfel, Quader, Pyramide) und der
Sachgeometrie in e4-k1-s4. Alle 173 Zahlwerte stimmen mit loesung
und pruef überein. `python3 werkzeuge/bank-pruef.py geraden`:
0 Abweichungen, 0 Warnungen in allen fünf Dateien. 20
Ankreuzen-Zeilen (genau eine richtige Option, loesung wortgleich)
und 13 Fehler-finden-Zeilen (Fehler ist falsch, Korrektur ist
richtig) einzeln geprüft, alle in Ordnung.

## Befunde

e2-k1-s1-v1, -v2, -v3, -v4, -v5, e2-k1-s5-v3, e2-k1-s8-v1, -v2, -v3,
e2-k3-s1-v1, e2-k3-s1-v3 (11 Zeilen, 16 Stellen): das Zeichen „✓"
(U+2713) in loesung fehlt in Latin Modern und bleibt im PDF leer
(bau/render-alle/bericht.md, „Fehlende Zeichen", geraden 1) – durch
„stimmt" ersetzen (wie zone-f4-v5: `\text{stimmt}`), oder ein
Baustein `\haken` in der Vorlage.

e2-k1-s9-v1, -v2: die „Schar" ist keine – der Stützpunkt
$(2 + 4k | -2k | 3 + 6k)$ läuft längs $(4 | -2 | 6) = -2 \cdot
(-2 | 1 | -3)$, also sind alle $g_k$ dieselbe Gerade; ebenso v2
($(-2 | 1 | 3)$ und $(4 | -2 | -6)$). Das Original 2025-bebb-lk-A1.7a
hat dieselbe Eigenschaft ($(5 - 6k | 3k | 4 - 9k)$, $(2 | -1 | 3)$),
die Bank hat sie treu übernommen; der Nachweis bleibt richtig.
Ermessen: treu lassen oder eine echte Schar bauen, etwa v1
$(2 | -2k | 3 + 6k) + r \cdot (-2 | 1 | -3)$ (zweite Koordinate
$r = 2k$, dritte $3 + 6k - 6k = 3 \ne 0$, pruef 3) und v2
$(6 | 1 + k | -4 + 3k) + r \cdot (4 | -2 | -6)$ (zweite
$r = \tfrac{1 + k}{2}$, dritte $-4 + 3k - 3 - 3k = -7 \ne 0$,
pruef -7); beide mit sympy geprüft, keine Lösung für alle k.

e4-k3-s3-v2: Drachenflieger mit $(40 | 30 | -5)$ je Sekunde fliegt
50 m/s = 180 km/h waagerecht und sinkt 5 m/s – ein Drachen fliegt
30–60 km/h und sinkt etwa 1 m/s. Vorschlag: $(12 | 9 | -1)$ je
Sekunde, dann $t = 500$, Landepunkt $(6\,000 | 4\,500 | 400)$,
waagerecht $7\,500$ m; pruef [500, 6000, 4500, 400, 7500].

e4-k1-s1-v5: Segelflugzeug legt je Minute $(1{,}5 | 2 | -0{,}4)$
LE bei 1 LE = 100 m zurück, also 250 m/min = 15 km/h – ein
Segelflugzeug fliegt 80–100 km/h. Zahlen passen zu einem
Heißluftballon im Wind (15 km/h, Sinken 0,67 m/s); Kontext
tauschen, Zahlen und Lösung bleiben.

e1-k3-s3-v2: die Sprosse verlangt „Gleichung einer Strecke mit
Parameterbereich angeben", die Frage verlangt nur die Höhe nach 5 s;
die Gleichung steht nur in der Lösung. Vorschlag: „Gib eine
Gleichung der Hubstrecke an und bestimme, in welcher Höhe die Last
nach 5 s ist."

e1-k2-s2-v2, -v3: die Sprosse heißt „schreiben und deuten", v1 tut
beides, v2 und v3 geben die Gleichung vor und verlangen nur die
Deutung – Varianten sollen den Handgriff nicht ändern. Vorschlag:
wie v1 Start- und Zielpunkt nennen und die Gleichung verlangen
(v2: Start $(0 | 5 | 12)$, Ziel $(15 | -5 | 2)$; v3: $(3 | 1 | 0)$,
$(9 | 4 | 6)$), Lösung bleibt.

e2-k1-s7-v1: „die Talstation liegt im Ursprung", der Lift beginnt
aber in $A(1 | 20 | 2)$, also 10 m höher und rund 100 m entfernt;
Rechnung und Ergebnis (46 m) stimmen. Vorschlag: Formulierung wie
v2, „der Ursprung liegt auf Höhe der Talstation".

e2-k3-s3-v1: die Sprosse lautet „Höhe aus der Entfernung vom
Anfang", die Aufgabe geht umgekehrt (Punkt aus der Höhe); merkmal
„Parameter als Anteil" passt, der Handgriff ist gespiegelt. Gering;
lassen oder fragen „Wie weit vom Start ist der Ballon, wenn er
900 m hoch ist?" (Antwort $0{,}75 \cdot 1\,300 = 975$ m).

e1-k3-s1-v2, e2-k3-s2-v2, e4-k1-s4-v3, e4-k3-s1-v3: Ortsvektoren
als `\vec{OT}`, `\vec{OA}`, `\vec{OK_t}`, alle anderen Zeilen
schreiben `\overrightarrow{AB}` – im selben Blatt zwei Schreibweisen.
Vorschlag: überall `\overrightarrow`.

Sauber: 149 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k2-s2-v2/-v3: Gleichung vorgegeben, „schreiben"
fehlt · e1-k3-s3-v2: Frage verlangt die Gleichung nicht ·
e2-k3-s3-v1: Richtung der Sprosse gespiegelt (Punkt aus Höhe).
(3 Befunde, 4 Zeilen)

Nur Erstleser (15 Befunde, 20 Zeilen):
- e2-k2-s1-v1 pruef [0.6, 3, 2]: bestätigt als Kosmetik, wirkt nur,
  wenn bank-pruef.py die 2 nach „:" als Ergebnisstelle liest.
- e4-k1-s4-v1 Zusatz „kein Lotabstand": bestätigt – beim
  waagerechten Dach ist die Höhendifferenz genau der Lotabstand
  zur Dachebene.
- e1-k1-s0-v1 „am Boden" ohne Bodenangabe: bestätigt, Lösung auf
  „Anfang/Ende" kürzen.
- e2-k3-s3-v3 Rundung fehlt: bestätigt – irrationales Ergebnis ohne
  Rundungsanweisung, verstößt auch gegen „Ergebnisse endlich".
- zone-f2-v2, zone-f6-v2, zone-f7-v2 merkmal passt nicht: als
  Unstimmigkeit bestätigt, anderer Vorschlag – das Skript verlangt je
  Sprosse ein einheitliches merkmal, die zwei sehr leichten Zeilen
  dürfen aber zwei Handgriffe der Fertigkeit abdecken; also das
  merkmal weiten („Verbindungsvektor oder Betrag", „Anstieg aus
  Gleichung oder aus zwei Punkten", „Steigung in Prozent oder
  Maßstab") statt die Aufgabe zu ersetzen.
- e2-k3-s3-v3 Richtung gespiegelt: bestätigt, gleicher Befund wie
  bei v1, dort habe ich v3 nicht mitgezählt.
- e3-k1-s0-v3, -v4 fragen die Lage statt den nächsten Prüfschritt:
  als Uneinheitlichkeit bestätigt; sie passen zum sprosse_text
  („… ankreuzen"), nicht zum merkmal – merkmal weiten oder Frage
  umstellen, beides möglich.
- e4-k1-s4-v1 bis -v4 jede Variante mit beiden Teilen: nicht
  bestätigt – stand.md Entscheidung 3 legt fest: zwei Originale,
  je Original zwei Zeilen; jede Zeile verfremdet ihr Original ganz,
  ein Doppelauftrag je Zeile wäre keine Verfremdung mehr.
- e4-k3-s1-v1, -v3 Fehler finden ohne Zahlen: bestätigt – bank.md
  verlangt eigene Zahlen und eine richtige Rechnung in der Lösung;
  beide Zeilen haben keine Rechnung.
- e2-k3-s3-v3 Schreibform 200,2 / 200,25: bestätigt.
- e3-k2-s1-v3 Tims Ergebnis stimmt: die Aufgabe ist nicht falsch
  (der Fehler ist der Schluss, nicht das Ergebnis), der Vorschlag
  macht den Fehler folgenreich – als Verbesserung bestätigt; das
  vorgeschlagene h schneidet g in (2 | 3 | 1), nachgerechnet.

Nur Zweitleser (6 Befunde, 20 Zeilen): ✓ (U+2713) fehlt im PDF
(11 Zeilen in e2) · e2-k1-s9-v1/-v2 Schar degeneriert (wie das
Original) · e4-k3-s3-v2 Drachenflieger 180 km/h · e4-k1-s1-v5
Segelflugzeug 15 km/h · e2-k1-s7-v1 Talstation im Ursprung, Lift
beginnt 10 m höher · Ortsvektor-Schreibweise `\vec{OA}` in vier
Zeilen.

Widersprüche: e4-k1-s4: der Erstleser will in jede der vier Zeilen
Beschreiben und Deuten legen, ich halte die Aufteilung je Original
(stand.md Entscheidung 3) für richtig und die Zeilen für sauber.
zone-f2-v2/f6-v2/f7-v2: der Erstleser ersetzt die Aufgabe, ich
weite das merkmal – gleiche Unstimmigkeit, verschiedene Reparatur.

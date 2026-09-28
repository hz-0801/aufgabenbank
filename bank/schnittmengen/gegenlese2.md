# Zweitlesung schnittmengen

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 125 (zone 26, e1 36,
e2 31, e3 32)

Prüfung: Jede Lösung wurde mit sympy nachgerechnet (Skript im
Scratchpad): Schnittpunkte Gerade–Ebene über den Parameter, Schnitt
Gerade–Gerade als Gleichungssystem in zwei Parametern mit Probe der
dritten Koordinate, die Parameter b und z_U rückwärts, die
Scharparameter r mit beiden Kantenparametern w, Spurpunkte, die
Schnittgeraden zweier Ebenen samt Punktprobe in beiden Ebenen, die
Abstandsgleichungen für h, die Ebenen durch drei Punkte für die
Schnittfiguren und Schnittstrecken (Planarität der Vierecke, Lage
der Endpunkte auf den Kanten, Kantenmitten), die Verlängerung der
Schnittkante bis zur Geraden h; Skalarprodukte, Punktproben und
Gleichungssysteme der Zone im Kopf und mit sympy. Die
ksys3-Grafiken wurden Aufruf für Aufruf gegen die Aufgabenwerte
geprüft (Stützpunkt, Richtungsvektor mal Bereich = Endpunkt,
Achsenbereich). Alle 125 Lösungen sind rechnerisch richtig; kein
pruef-Wert weicht ab. bank-pruef.py v0.5: zone 0/0, e1 0/0, e2 0/0,
e3 0/0 (Abweichungen/Warnungen), gesamt 0 und 0. Ankreuzen: 16
Zeilen (e1 8, e2 4, e3 4), in jeder genau eine Option richtig und
in loesung wortgleich genannt. Fehler finden: 10 Zeilen (zone 1,
e1 3, e2 3, e3 3), der eingebaute Fehler ist jeweils wirklich
falsch und die richtige Rechnung in loesung stimmt. Die Kontexte
wurden gegen Abschnitt 2 der Mappe gelesen.

## Befunde

e1-k2-s6-v1, e1-k2-s6-v2: Die Buchstaben G, B, E, H (v2: C, F, G,
H) sind im Text nicht erklärt; Gerätehaus und Container haben keine
Lage und keine Koordinaten, die Kante BE bzw. FG ist nur ein Name.
Für die Beschreibung des Rechenwegs genügt das knapp, verletzt aber
die Regel „Buchstaben nur, wenn im Text erklärt" – Vorschlag: einen
Satz ergänzen „Die Koordinaten der Ecken B und E sind bekannt" oder
zwei Eckpunkte angeben. v1 übernimmt zudem die Buchstaben GBH und
BE wortgleich aus dem Original 2023MerhoehtBAGLAA2WTR1-1e.

e1-k2-s2-v1, e1-k2-s2-v2, e1-k2-s2-v3: Die drei Varianten teilen
das Merkmal statt es zu wiederholen. v1 stellt die Gerade aus zwei
Punkten auf, hat aber keinen Kontrollwert, obwohl sprosse_text und
merkmal ihn nennen; v2 und v3 geben die Gerade fertig vor (nur
einsetzen) und tragen den Kontrollwert samt der Falle μ außerhalb
[0; 1] – Vorschlag: v1 „(zur Kontrolle: Q(1,5|0,5|1,5))" anhängen;
in v2 und v3 die Geradengleichung streichen und aus D und C
aufstellen lassen, dann bleibt die Falle (Richtungsvektor ein
Drittel von DC) als Aufgabe des Schülers.

e1-k2-s4-v2: Die Lichtrichtung ist gegeben und die Auffangebene ist
z = 6, nicht die Grundebene; das Merkmal „Lichtrichtung aus Punkt
und Schattenpunkt" fehlt, die Variante übt nur die zweite Hälfte –
Vorschlag: die Richtung über ein Punktepaar geben (etwa: der
Schatten von I(0|0|13) liegt in (3|-1,5|10)) oder die Zeile als
Original-Form belassen und das im merkmal sagen.

e3-k1-s2-v3: Die Sprosse verlangt Spurgeraden in zwei
Koordinatenebenen, die Variante nur eine (yz) – Vorschlag: die
Spurgerade in der xz-Ebene dazu ((6|0|0) und (0|0|3)); dann
x1max=7, oder eine Ebene mit kleineren Abschnitten wählen.

e1-k2-s4-v1, e1-k3-s1-v2, e2-k1-s1-v5, e2-k1-s3-v1, e2-k1-s4-v1,
e2-k2-s1-v1, e3-k1-s2-v1, e3-k1-s2-v2 (und e1-k2-s6-v1, oben): Der
Kontext ist derselbe wie im Original – Sonnensegel mit Schatten von
A und B (2020 WTR-1d), Obelisk mit Schattenabstand (2018 CAS2-1g),
Mähroboter mit Rand BC und Kontrollwert (2021 WTR2-1c),
Kletteranlage mit Netz, Pfählen und Plattformkante RT (2018
WTR2-1f), Museum als Körper ABCDEF mit abgedruckter Rechnung
(2018-bb-ea-B3.1a), Spielturm mit Stange und Dachkante EF (2017
CAS1-1e), Holzkörper als Pyramide mit Spitze über D und Ebene L
(2021-be-gk-B3h, 2021 WTR1-1e). Die Zahlen sind überall neu; die
Regel „anderer Kontext" aus bank.md ist aber nicht erfüllt, und die
Aufgaben sind an der Erzählung wiedererkennbar – Vorschlag: je Zeile
den Kontext tauschen (Museum → Bahnhofshalle, Sonnensegel →
Zeltdach, Mähroboter → Saugroboter in einer Halle, Kletternetz →
Seilbahn-Tragseil, Spielturm → Pavillon, Holzkörper → Briefbeschwerer
aus Glas). Nur umbenannt sind e1-k2-s3-v1 (Ausstellungsgebäude für
Museum) und e1-k2-s3-v3 (Versorgungsstollen für Autotunnel); das
reicht knapp.

e3-k1-s4-v3: E, F (Aufgabe) und H, G (Lösung) sind nicht
eingeführt, der Würfel hat keine Buchstabenfolge – Vorschlag:
„Gegeben ist der Würfel ABCDEFGH mit der Kantenlänge 5 …"

e2-k1-s5-v1 bis v4: Der Schnittpunkt heißt in antwort und loesung
Q, in aufgabe kommt Q nicht vor – Vorschlag: „… schneidet g_r die
Kante GH im Punkt Q."

e2-k1-s3-v1, v2, v3: Alle drei Varianten treffen die Kante RT bei
t = μ = 0,5, also in beiden Mitten; wer das Muster einmal kennt,
rechnet nicht mehr. Ebenso e2-k1-s2-v1 und v3 (beide b = 2,5) und
e3-k1-s5-v1 und v3 (beide z = 4) – Vorschlag: je eine Variante mit
anderem Teilpunkt bzw. anderem Ergebnis.

e2-k1-s5-v2, e3-k1-s3-v3: Die Lösung schreibt 0,3333 und 0,6667
statt 1/3 und 2/3; auf dem Lösungsblatt ist das eine Rundung ohne
Hinweis – Vorschlag: \frac{1}{3} und \frac{2}{3}.

e3-k1-s6-v2: E_2: x − y = 0 ist bis aufs Vorzeichen die Gleichung
−x + y = 0 des Originals 2021-be-gk-B3e (dieselbe Diagonalebene);
die Sperre greift hier nicht, weil nur Zahlen unter 10 vorkommen –
Vorschlag: die andere Diagonale nehmen (x + y = 5), wie in v1 und
v3.

Sauber: 95 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k2-s2-v1 bis v3 (Merkmal unter den Varianten
aufgeteilt, Kontrollwert und Kantengerade), e1-k2-s4-v2
(Lichtrichtung vorgegeben, Auffangebene z = 6), e2-k1-s5-v2 und
e3-k1-s3-v3 (gerundete Dezimalzahlen statt Brüche).
Nur Zweitleser: e1-k2-s6-v1, v2 (Buchstaben G, B, E, H bzw. C, F,
G, H unerklärt); e3-k1-s2-v3 (nur eine Spurgerade statt zwei);
e1-k2-s4-v1, e1-k3-s1-v2, e2-k1-s1-v5, e2-k1-s3-v1, e2-k1-s4-v1,
e2-k2-s1-v1, e3-k1-s2-v1, v2 (Kontext wie im Original, dazu
e1-k2-s3-v1, v3 nur umbenannt); e3-k1-s4-v3 (Würfel ohne
Buchstabenfolge); e2-k1-s5-v1 bis v4 (Q nicht in aufgabe);
e2-k1-s3-v1 bis v3, e2-k1-s2-v1, v3, e3-k1-s5-v1, v3 (gleiche
Parameter oder Ergebnisse über die Varianten); e3-k1-s6-v2
(Gleichung x − y = 0 wie −x + y = 0 des Originals).
Nur Erstleser: e1-k4-s2-v3 (Begründen zum echt parallelen Fall
steht nicht im Sprossentext) – richtig, übersehen; der Ersatz
kann eine zweite Variante zum ersten genannten Punkt sein, etwa
„warum bei x gleich Konstante nur die erste Koordinate zählt".
e2-k1-s1-v5 (λ in der Lösung ohne die Bahngleichung) – richtig,
übersehen; ich hatte nur gesehen, dass λ in der Aufgabe fehlt, und
es der Lösung durchgehen lassen.
Widerspruch: keiner.

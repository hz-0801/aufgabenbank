# Zweitlesung normalverteilung-und-sigma-regeln

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 104 (zone 27, e1 23,
e2 28, e3 26)

Prüfung: Jede Zeile gelesen; jede Lösung unabhängig nachgerechnet
(scipy.stats: alle Normalverteilungs-Wahrscheinlichkeiten,
Quantile für μ, σ und Grenzen, die Rechnungen mit und ohne halbe
Schritte, Binomialwerte und kumulierte Werte der Zone,
Erwartungswerte, Sigma-Regeln); Dichteterme gegen
1/(σ√(2π))·e^{−(x−μ)²/(2σ²)} geprüft (e3-k1-s1-v3, e3-k3-s1-v1:
Nenner 8 bzw. 18 = 2σ²); die Verteilungsfunktions-Grafiken
(logistische Näherung, F(μ+σ) ≈ 0,846) und die Rechteck-Näherungen
(Dichtemaximum von N(50; 4) ≈ 0,0997, von N(12; 2) ≈ 0,1995) gegen
die Werte im Text gehalten; Säulendiagramme der Zone (Modus von
B(4; 0,25) bei 1, von B(10; 0,2) bei 2) nachgerechnet. Ankreuzen:
in allen 13 Zeilen genau eine Option richtig. Fehler finden: in
allen 10 Zeilen ist der eingebaute Fehler wirklich falsch.
`python3 werkzeuge/bank-pruef.py normalverteilung-und-sigma-regeln`:
0 Abweichungen, 0 Warnungen.

## Befunde

e1-k1-s1-v1 bis v5, e2-k1-s1-v1 bis v5, e3-k1-s1-v1 bis v5,
e3-k1-s2-v1 bis v3, e3-k1-s3-v1 bis v3 (21 Zeilen): Der Fragesatz
endet mit einer Prüfkennung „(Abitur 2022/2023/2024/2025 LK)", das
Feld original ist null, und die Mappe führt zu diesen Sprossen kein
Original (die zwölf Originale von Abschnitt 2 sind anderswo
verbaut). stand.md kennt den Fall (Entscheidung 5, Befund „Neun
Kennungen", Offenes „Feld original nachtragen"): der Katalog nennt
die Kennungen, die Mappe hat sie nicht aufgenommen. Damit bleibt
offen, was das Prüfskript sonst leistet – die Sperre gegen diese
neun Originale ist nie geprüft worden, weil ihre Zahlen nirgends in
der Bank stehen. – Vorschlag: die neun Kennungen in die Mappe
aufnehmen (mappe.py), dann original setzen und bank-pruef.py laufen
lassen; bis dahin ist die Kennung im Text ein Versprechen ohne
Beleg.

e2-k1-s4-v1: „Ein Laden gibt je volle 4 € Einkaufswert einen
Punkt; die Zahl C der Punkte bei einem Einkauf von 60 bis 63,99 €"
– nach der Regel sind das immer genau 15 Punkte; dass C streut,
erklärt der Text nicht, das Modell N(15; 2,5) steht unbegründet
neben einer festen Regel. Rechnung und Urteil stimmen. –
Vorschlag: ein Halbsatz, warum die Anzahl streut („der Automat
vergibt die Punkte fehleranfällig"), wie es das Original 2026-bb-ea
voraussetzt.

e3-k1-s3-v2, e3-k1-s3-v3: Die Lösung schreibt $P(M < c)$ bzw.
$P(V > c)$; die Buchstaben M und V führt die Aufgabe nicht ein (sie
spricht von Masse und Verspätung). bank.md: Buchstaben nur, wenn im
Text erklärt. – Vorschlag: in der Aufgabe „die Masse M" bzw. „die
Verspätung V" nennen, oder in der Lösung ohne Buchstaben „für Sorte
B liegen etwa 2,8 % unter c".

zone-f2-v1, zone-f2-v2: Die Frage lautet „Fläche unter dem Graphen
– was bedeutet sie?", das Antwortgerüst ist „__ l" bzw. „__ m", die
Lösung gibt Zahl und Bedeutung. Frage und Feld passen nicht
zusammen. – Vorschlag: „Berechne die Fläche unter dem Graphen. Was
bedeutet sie?" (wie v3/v4 mit Zahl im Feld, Bedeutung im Text).

e2-k1-s2-v1, e2-k1-s3-v3, e2-k2-s1-v2: Der Buchstabe A steht in
Einheit 2 für drei Sachen (die normalverteilte Zufallsgröße selbst,
die Zahl der Anmeldungen, die Zahl der Anrufe); ebenso L in Einheit
1 (e1-k1-s2-v3 Nagellänge, e1-k2-s1-v3 Laufleistung). bank.md: „ein
Buchstabe je Einheit für eine Sache". Klein, weil jede Aufgabe
ihren Buchstaben erklärt. – Vorschlag: in e2-k1-s3-v3 „die Zahl N
der Anmeldungen", in e2-k2-s1-v2 „die Zahl R der Anrufe"; in
e1-k2-s1-v3 „die Laufleistung R".

Sauber: 73 Zeilen ohne Befund

## Abgleich

Beide Leser: e3-k1-s3-v2/v3 (M und V in der Lösung nicht
eingeführt; der Erstleser hat zusätzlich v1 mit L – richtig, das
habe ich übersehen, „Laufleistung" steht dort ohne Buchstaben).
e2-k1-s4-v1 – aus verschiedenen Gründen: ich sehe die feste
Punkteregel, die das streuende Modell unerklärt lässt; der
Erstleser sieht den Kontext des Originals samt Buchstabe C
unverändert übernommen (bank.md: anderer Kontext). Sein Grund ist
der stärkere; ein Kontextwechsel wie in v2/v3 behebt beides.

Nur Zweitleser: zone-f2-v1/v2 (Frage nach der Bedeutung,
Antwortfeld für eine Zahl).

Nur Erstleser: zone-f3-v3 (n und p ohne Verteilung genannt –
richtig, übersehen); e3-k1-s1-v4/v5 (woher 0,84 kommt, fehlt in
der Lösung – richtig); e1-k1-s0-v2 („am höchsten" verrät die
Option – ich hatte es gesehen und durchgelassen, sein Einwand
trägt); e3-k1-s4-v1 bis v4 (Merkmal „eingeführte Merkmale
kombinieren" trifft nicht, die Prüfungshöhe führt Neues ein –
richtig, ein Katalogbefund); e3-k1-s4-v2 (Konfitüre womöglich der
Kontext des Originals – plausibel, nicht geprüft).

Widerspruch: Die 21 Prüfkennungen ohne original – der Erstleser
wertet sie nach stand.md Entscheidung 5 als geregelt, kein Befund;
ich halte den Posten für offen, weil die Sperre gegen die neun
Originale ungeprüft bleibt, solange die Mappe sie nicht führt – die
Regelung erklärt den Zustand, hebt ihn nicht auf. Die Buchstaben
A und L für mehrere Sachen je Einheit – der Erstleser entscheidet
„als Einzelaufgaben der Bank kein Befund"; ich halte es für einen
kleinen Befund, weil bank.md die Regel je Einheit ausspricht und
ein Blatt Zeilen einer Einheit nebeneinanderstellt. Beides sind
Ermessensfragen für den Chat, keine Rechenfehler.

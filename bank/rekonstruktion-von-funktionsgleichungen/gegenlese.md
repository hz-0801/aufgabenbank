# Gegenlese rekonstruktion-von-funktionsgleichungen

Datum: 2026-09-27
Modell: claude-opus-5-5
Geprüfte Zeilen: 146
Korrekturen: 0

## Entscheidungen

pruef-Listen, die neben der gefragten Zahl Zwischenwerte der Lösung tragen (Periode, Nullstellen, Koeffizient, etwa zone-f5-v2 [2, 10]), gelten als passend, solange jede Zahl an einer Ergebnisstelle der Lösung steht.

Die Regel „ein Buchstabe je Einheit für eine Sache“ (bank.md) gilt auch dann, wenn der Buchstabe in der Aufgabe erklärt ist; die Doppelbelegungen in Einheit 3 stehen deshalb unter 2 (Nachtrag bei der Durchsicht des Auftraggebers).

## 1 Rechnung

keine

## 2 Eindeutigkeit

rekonstruktion-von-funktionsgleichungen-e2-k2-s1-v1: Der Text legt nicht fest, dass das Abkühlen bzw. Erwärmen bei t = 5 (v2: t = 2, v3: t = 4) beginnt; „Zu Beginn des Abkühlens“ kann als t = 0 gelesen werden (dann b = 60 statt ≈ 98,92), und bei v1/v2 bleibt offen, was t = 0 ist (alle Varianten v1–v3) – den Beginn ausdrücklich an die Startstelle des Modells binden, etwa „Zum Zeitpunkt t = 5 wird die Suppe vom Herd genommen“ bzw. „Zu Beginn des Abkühlens (t = 5)“.

rekonstruktion-von-funktionsgleichungen-e3-k1-s4-v1: $p$ ist in Einheit 3 die Periode (e3-k1-s1, e3-k5-s1) und hier Funktionsname, ebenso in e3-k1-s5-v1–v3 und e3-k3-s1-v1–v3 – die Funktionen umbenennen (etwa $E$ für die Einwohnerzahl, $h$ für die Parabel), $p$ bleibt der Periode

rekonstruktion-von-funktionsgleichungen-e3-k1-s4-v3: $b$ ist in Einheit 3 der Parameter in $a \cdot \mathrm{sin}(b \cdot x)$ und hier Funktionsname – die Funktion umbenennen (etwa $B$ oder $h$)

## 3 Merkmal

rekonstruktion-von-funktionsgleichungen-e2-k1-s2-v1: Ansatz h(t) = at³ + bt² mit nur zwei Koeffizienten, Wert und Steigung an derselben Stelle t = 4; merkmal verlangt „Wert- und Steigungsbedingungen an verschiedenen Stellen, vier Koeffizienten“, v2 und v3 setzen das um – Ansatz auf vier Koeffizienten erweitern (etwa h(0) = 0 und h'(0) = 0 als Bedingungen im Text) oder die Variante gegen eine mit Bedingungen an verschiedenen Stellen tauschen.

rekonstruktion-von-funktionsgleichungen-e2-k1-s5-v3: Steigungswinkel 0° („läuft waagerecht aus“) macht den Tangens-Schritt, das Merkmal der Sprosse, überflüssig, und der Ansatz ist vierten statt wie in v1/v2 zweiten Grades (nimmt die Prüfungssprosse s8 vorweg) – quadratischen Ansatz mit einem Randwinkel ungleich 0° wählen.

## 4 Schreibform

rekonstruktion-von-funktionsgleichungen-e3-k1-s5-v1: Die Flächenformel „$\frac{2}{3} c \cdot x_0$“ steht ohne das Integral, aus dem sie folgt; der Schritt über $\int_0^{x_0} (ax^2 + c)\,dx = \frac{a}{3}x_0^3 + c x_0$ mit $a = -\frac{c}{x_0^2}$ fehlt (alle Varianten v1–v3) – das Integral und das Einsetzen von $a$ als Zwischenschritt in die Lösung aufnehmen.

## 5 Ankreuzen

keine

## 6 Fehler finden

keine

Sauber: 133 Zeilen ohne Befund

# Gegenlese: kurvenuntersuchung

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 335 (zone 29, e1 39, e2 106, e3 63, e4 46, e5 52)
Korrekturen: 1

Jede Lösung aus der Aufgabe neu gerechnet (Python/sympy): Terme,
Ableitungen, Nullstellen, Punkte, Winkel, Rundungen. Alle Zahlen
stimmen; korrigiert ist eine falsche Aussage in einer Lösung.

Selbst entschieden (nicht geregelt): Eine sachlich falsche Aussage
in der loesung bei richtigem Zahlenergebnis gilt als Punkt 1 und
wird korrigiert, wenn die Korrektur eindeutig ist; ist die Aussage
nur nicht belegt (kann stimmen), bleibt sie Befund. Ein gerundeter
pruef-Wert (statt des ungerundeten, bank.md) ist Befund, keine
Korrektur, weil die Lösung stimmt. Die Modellkennung steht nicht
im Kopf, weil die Sitzung keine Modellkennung in Repo-Dateien
schreiben darf.

## Punkt 1 – Lösung und pruef

kurvenuntersuchung-e3-k6-s1-v3: korrigiert – „die Wendetangente ist die steilste Gerade“ war falsch: f(x) − (−1) − m(x − 1) = −½u(u² + 2m − 4) mit u = x − 1 hat für jedes m ≥ 2 nur u = 0; die Wendetangente ist die flachste solche Gerade. Jetzt „flachste“; pruef unverändert (2).
kurvenuntersuchung-e3-k5-s1-v1: pruef [4.71] ist schon gerundet – pruef [3*math.pi/2].
kurvenuntersuchung-e3-k5-s1-v2: pruef [2.09] ist schon gerundet – pruef [2*math.pi/3].
kurvenuntersuchung-e3-k5-s1-v3: pruef [1.57] ist schon gerundet – pruef [math.pi/2].
kurvenuntersuchung-e4-k4-s1-v2: loesung behauptet „ist dort am steilsten“; aus W(1 | 4) und f'(1) = 3 folgt nur ein Extremum von f' bei 1, es kann ein Minimum sein (dann am flachsten) – „ist dort am steilsten und“ streichen. Die Ungenauigkeit steht schon im Merkkasten E3 („Wendetangente … die steilste Stelle“).

## Punkt 2 – eindeutig lösbar

kurvenuntersuchung-e1-k1-s1-v1: Fragesatz „Welches Vorzeichen hat f'(x) auf …?“, die Optionen sind aber „f steigt“ / „f fällt“ – Fragesatz „Welches Vorzeichen hat f'(x) auf [4; 6], und was folgt daraus für f? Kreuze an.“ oder Optionen „f'(x) > 0, f steigt“ / „f'(x) < 0, f fällt“.
kurvenuntersuchung-e1-k1-s1-v2: wie v1 (Intervall [2; 5]).
kurvenuntersuchung-e1-k1-s1-v3: wie v1 (Intervall [−1; 1]).
kurvenuntersuchung-e1-k1-s1-v4: wie v1 (Intervall [1; 3]).
kurvenuntersuchung-e1-k1-s1-v5: wie v1 (Intervall [−2; 2]).
kurvenuntersuchung-e1-k1-s7-v4: y-Werte −22/3 und 10/3 periodisch, kein Rundungshinweis in der Aufgabe; der Hochpunkt steht nur gerundet in der Lösung – „Runde auf zwei Nachkommastellen“ in die Aufgabe, in der Lösung „$H(2 | \frac{10}{3})$, also $H(2 | 3{,}33)$“.
kurvenuntersuchung-e1-k1-s7-v6: Extrempunkte irrational (±√3, 4 ± 2√3), keine Rundungsangabe; Lösung nur gerundet – Rundungsangabe in die Aufgabe, exakte Werte $4 \pm 2\sqrt{3}$ in die Lösung.
kurvenuntersuchung-e2-k11-s1-v3: „Tiefpunkt T(−1 | 4) und keinen weiteren Extrempunkt“ schließt einen Sattelpunkt bei −0,9 nicht aus (f'(x) = (x + 1)(x + 0,9)² gibt f'(−0,9) = 0), „wahr“ ist nicht eindeutig – „… und keine weitere Stelle mit waagerechter Tangente“ ergänzen wie in e1-k1-s4-v2.
kurvenuntersuchung-e3-k7-s2-v3: Die zu begründende Aussage „in W am steilsten“ ist falsch, wenn f'(W) < 0 (f(x) = −x − x³/3: in W(0 | 0) Steigung −1, daneben steiler) – „in $W$ die größte Steigung“ oder „… und steigt dort, so ist er in $W$ am steilsten“.
kurvenuntersuchung-e4-k2-s1-v1: Stetigkeit von f und g fehlt, die Lösung stützt sich darauf (v2 nennt „stetige Funktionen“) – „Die Graphen der stetigen Funktionen $f$ und $g$ …“.
kurvenuntersuchung-e5-k1-s9-v2: „Zug $A$“ nicht eingeführt, Zuordnung Zug ↔ f/g fehlt; die Lösung setzt f = Zug A voraus – „Zwei Züge $A$ und $B$ …; $f(t)$ und $g(t)$ sind die zurückgelegten Wege von $A$ bzw. $B$ …“.

## Punkt 3 – Sprosse und Merkmal

kurvenuntersuchung-e2-k1-s3-v1: sprosse_text endet mit offener Klammer „… (ganzrational vierten Grades“ – Klammer schließen (Katalogtext prüfen).
kurvenuntersuchung-e2-k1-s3-v2: wie v1.
kurvenuntersuchung-e2-k1-s3-v3: wie v1.
kurvenuntersuchung-e2-k10-s1-v3: v1/v2 fragen zusätzlich nach der Stelle mit dem kleinsten senkrechten Abstand zu g_u und diesem Abstand, v3 nicht; hier wäre der kleinste Abstand im Inneren 0 bei x = 2 (Berührung) – andere Zahlen mit innerem Minimum > 0 wählen und den Teil ergänzen.
kurvenuntersuchung-e3-k1-s6-v3: x·e^(−x) statt ganzrational, Nachweis über Vorzeichenwechsel statt f''', kein Wendepunkt zum Bestätigen vorgegeben („Gib ihn an“) – ganzrationale Funktion mit vorgegebenem W(x₀ | y₀) wie v1/v2.
kurvenuntersuchung-e3-k1-s9-v3: Anders als v1/v2 kein Funktionsterm, kein Wendepunktnachweis, form text statt teil – wie v1/v2 bauen (punktsymmetrisch, Grad 5, W nachweisen, zweiten W angeben).
kurvenuntersuchung-e3-k1-s10-v3: sprosse_text „Existenz eines Wendepunkts ohne Rechnung … mit einer Skizze begründen“ passt nicht zur fhr-Zielmarke (Wendepunkte fünften Grades mit Polynomdivision, Sattelpunkt) – passenden sprosse_text aus dem Katalog setzen oder die Zielmarke als eigene Sprosse führen.
kurvenuntersuchung-e3-k1-s10-v4: wie v3.
kurvenuntersuchung-e3-k1-s10-v5: sprosse_text passt nicht (Krümmungsintervalle, fhr 2020-C-1d); merkmal sagt „fünften Grades“, x⁴ − 24x² + 10 ist vierten Grades – sprosse_text wie v3, merkmal ohne Grad oder „vierten/fünften Grades“.
kurvenuntersuchung-e3-k1-s10-v6: wie v5 (−x⁴ + 6x² vierten Grades).
kurvenuntersuchung-e3-k3-s1-v3: v1/v2 ankreuzen „welcher von vier Punkten ist der Wendepunkt“, v3 prüft einen einzelnen Punkt (form teil) – v3 als Ankreuzen mit vier Kandidaten.
kurvenuntersuchung-e4-k1-s8-v3: sprosse_text „Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen“ passt nicht zu Skizze plus Aussage über gemeinsame Punkte von Tangente und Graph (2023-bebb-gk-B2.2e) – sprosse_text um den zweiten Teil der Katalog-Prüfungshöhe ergänzen.
kurvenuntersuchung-e4-k1-s8-v4: wie v3 (Tangente im Hochpunkt, Skizze).
kurvenuntersuchung-e5-k1-s9-v3: sprosse_text „einen fremden Lösungsweg … deuten oder dazu die Aufgabenstellung formulieren“ passt nicht zur fhr-Zielmarke „steilster Anstieg eines Dachs“ (kein Lösungsweg zum Deuten) – sprosse_text der Zielmarke setzen oder eigene Sprosse.
kurvenuntersuchung-e5-k1-s9-v4: wie v3.

## Punkt 4 – Schreibform

kurvenuntersuchung-e1-k1-s7-v3: Einheit 1 (Monotonie), die Lösung bestimmt die Art der Extrempunkte über f''; das f''-Kriterium kommt erst in Einheit 2 – Art aus dem Monotoniewechsel begründen („f fällt vor 1 und steigt danach → Tiefpunkt“) oder Katalogbefund (fhr-Zielmarke 2021-A-1c in Einheit 1).
kurvenuntersuchung-e1-k1-s7-v4: wie v3 (f''(−2), f''(2)).
kurvenuntersuchung-e1-k1-s7-v5: wie v3 (Zielmarke 2024-C-1d).
kurvenuntersuchung-e1-k1-s7-v6: wie v3.
kurvenuntersuchung-e2-k12-s1-v1: Lösung begründet mit „f''(2) > 0 bedeutet Linkskrümmung“, Krümmung kommt erst in Einheit 3 – „$f''(2) > 0$ zeigt nach der hinreichenden Bedingung einen Tiefpunkt“.
kurvenuntersuchung-e3-k1-s6-v3: Produktregel mit e-Funktion, die erst Sprosse s8 einführt – ganzrationale Funktion (siehe Punkt 3).

## Punkt 5 – Ankreuzen

kurvenuntersuchung-e3-k1-s0-v1: „welcher Nachweis … verlangt oder möglich ist“ – der Vorzeichenwechsel von f'' ist immer möglich, zwei Optionen vertretbar; gemeint ist der Nachweis mit der Angabe f'''(1) = 6 – „welcher Nachweis mit der gegebenen Angabe direkt geführt werden kann“ (Fragesatz gilt für v1 bis v4; nur in v1 sind wirklich zwei Optionen vertretbar).

## Punkt 6 – Fehler finden

kurvenuntersuchung-e3-k7-s1-v3: Gesucht waren „die besonderen Punkte“, die vorgelegte Rechnung lässt aber auch die zweite Wendestelle x = 1/3 (f''(x) = 12(3x − 1)(x − 1)) und den Tiefpunkt T(0 | 0) aus; die Lösung korrigiert nur den Sattelpunkt, ihr „Richtig:“ ist unvollständig – Aufgabe eingrenzen: „Gesucht war die Art des Punktes bei x = 1“.

Sauber: 299 Zeilen ohne Befund

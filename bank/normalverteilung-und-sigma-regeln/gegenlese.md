# Gegenlese: normalverteilung-und-sigma-regeln

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 104 (zone 27, e1 23, e2 26, e3 28)
Korrekturen: 0
Grundlage: Aufgaben selbst nachgerechnet (Python/sympy); bank.md für die Felder; mappen/normalverteilung-und-sigma-regeln.md für Sprossenfolge, Schreibform und Typische Fehler.

## Befunde

### 1 Lösung und pruef
keine
### 2 Eindeutigkeit und Angaben
normalverteilung-und-sigma-regeln-zone-f3-v3: „$n = 20$, $p = 0{,}3$: Erwartungswert und Standardabweichung?“ sagt nicht, dass eine binomialverteilte Zufallsgröße gemeint ist, und erklärt $n$ und $p$ nicht; die Lösung führt dazu $\mu$ und $\sigma$ ein – ergänzen: „$X$ ist binomialverteilt mit $n = 20$ und $p = 0{,}3$.“
### 3 Sprosse und Merkmal
normalverteilung-und-sigma-regeln-e2-k1-s4-v1: verfremdetes Original 2026-bb-ea-B4h behält den Kontext des Originals (Treuepunkte je voller Euro-Betrag beim Einkauf, sogar derselbe Buchstabe $C$), nur die Zahlen sind neu; bank.md verlangt anderen Kontext – Kontext wechseln wie in v2 und v3 (Schrauben, Eier).
normalverteilung-und-sigma-regeln-e3-k1-s4-v1, normalverteilung-und-sigma-regeln-e3-k1-s4-v2, normalverteilung-und-sigma-regeln-e3-k1-s4-v3, normalverteilung-und-sigma-regeln-e3-k1-s4-v4: merkmal „eingeführte Merkmale kombinieren“ stimmt nicht – die σ-Schranke mit Monotonie in σ und das beste Intervall fester Länge kommen in s1–s3 nicht vor (nur später in den Pflichtzeilen k3), die Prüfungshöhe führt sie neu ein (unterrichtsblatt 2.4 c) – Zwischensprosse vor der Prüfungshöhe oder als Katalogbefund in stand.md vermerken.
normalverteilung-und-sigma-regeln-e3-k1-s4-v2: verfremdet 2025MerhoehtBStochastikWTR1-2b im Kontext Konfitüre-Füllmenge; die Mappe nennt Konfitüre als Kontext der Füllmengen-Ketten, beim Original mit $\mu = 250$ g also sehr wahrscheinlich derselbe Kontext – anderes Füllgut wählen (wie v1, Dosen).
### 4 Schreibform
normalverteilung-und-sigma-regeln-e3-k1-s1-v4, normalverteilung-und-sigma-regeln-e3-k1-s1-v5: die Lösung liest $\sigma$ an der Stelle mit $F \approx 0{,}84$ ab, ohne zu sagen, woher $0{,}84$ kommt; der Schüler kennt nur die Halbwertsstelle – Schritt ergänzen: „$F(\mu + \sigma) \approx 0{,}5 + 0{,}683 : 2 \approx 0{,}84$ (σ-Regel)“.
normalverteilung-und-sigma-regeln-e3-k1-s3-v1, normalverteilung-und-sigma-regeln-e3-k1-s3-v2, normalverteilung-und-sigma-regeln-e3-k1-s3-v3: die Lösung benutzt die Zufallsgrößen $L$, $M$, $V$, die in der Aufgabe nicht eingeführt sind – in der Aufgabe benennen („Laufleistung $L$“, „Masse $M$“, „Verspätung $V$“) oder in der Lösung ausschreiben.
### 5 Ankreuzen
normalverteilung-und-sigma-regeln-e1-k1-s0-v2: die Frage „An welcher Stelle ist der Graph … am höchsten?“ nennt die richtige Option („Höhe des Graphen“) schon selbst, die Einordnung wird nicht geübt – Frage ohne das Signalwort „am höchsten“ stellen, etwa über einen Sachkontext wie in v1 und v3.
### 6 Fehler finden
keine

## Entscheidungen

- Die Prüfkennung „(Abitur Jahr LK)“ in den Grundfällen (e1 s1, e2 s1, e3 s1) und in e3 s2–s3 bei original null ist in stand.md (Entscheidung 5, Befund „Neun Kennungen“) begründet; kein Befund.
- pruef mit gerundeten Literalen (etwa 6.71, 38592.0) und Folgerechnungen mit dem gerundeten Zwischenwert (e3 s2, s3; stand.md Entscheidung 6) gelten als richtig, wenn der ungerundete Wert dieselbe Rundung ergibt; e3-k1-s3-v3 gibt mit ungerundetem $c$ $0{,}247$ statt $0{,}248$, mit $c = 5{,}68$ aber $0{,}248$ – kein Befund, das Urteil „ja“ bleibt.
- e3-k1-s4-v1: „$\sigma_{\text{max}} = 3{,}65$“ rundet die Schranke $3{,}6477$ auf; die Prüfung mit dem etwas größeren σ ist aber konservativ, das Argument bleibt richtig – kein Befund.
- Rechteck-Näherungen in e2 s5 (Höhe = Maximum der Dichte) sind grob, aber die Aufgabe verlangt nur das Erläutern der vorgelegten Rechnung – kein Befund.
- Buchstaben wie $X$, $A$, $L$ werden in verschiedenen Aufgaben einer Einheit für verschiedene Größen verwendet, jeweils im Aufgabentext erklärt; als Einzelaufgaben der Bank kein Befund.
- e3-k3-s1-v1: 18 steht im Vorfaktor und im Exponenten; Janas $\sigma = 18$ ist das Muster „Parameter falsch am Dichteterm abgelesen“ – als passend gewertet.

Sauber: 92 Zeilen ohne Befund

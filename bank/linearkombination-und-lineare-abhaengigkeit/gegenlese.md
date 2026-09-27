# Gegenlese: linearkombination-und-lineare-abhaengigkeit

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 58 (zone 18, e1 18, e2 22)
Korrekturen: 0
Grundlage: Aufgaben selbst nachgerechnet (Python/sympy); bank.md für die Felder; mappen/linearkombination-und-lineare-abhaengigkeit.md für Sprossenfolge, Schreibform und Typische Fehler.

## Befunde

### 1 Lösung und pruef
keine
### 2 Eindeutigkeit und Angaben
linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v3, linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v5: „Gib gegebenenfalls den Faktor an“ legt die Richtung nicht fest; $\vec{u} = 3 \cdot \vec{v}$ bzw. $\vec{u} = 2 \cdot \vec{v}$ (Faktor 3 bzw. 2) ist ebenso richtig, die Lösung nennt nur $\frac{1}{3}$ bzw. $0{,}5$ – in der Aufgabe „Gib den Faktor $k$ mit $\vec{v} = k \cdot \vec{u}$ an“ fordern oder beide Faktoren in der Lösung nennen.
linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v1, linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v2, linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v3, linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v4, linearkombination-und-lineare-abhaengigkeit-e2-k1-s1-v5: Welcher Koeffizient ersetzt wird, ist offen; mit $q = 1 - p$ entsteht die ebenso richtige Parameterform $\vec{OB} + p \cdot (\vec{OA} - \vec{OB})$ (bzw. mit $C$, $D$), Lösung und pruef kennen nur die Form mit $q$ – „Setze $p = 1 - q$ ein“ in die Aufgabe schreiben oder beide Formen in der Lösung zulassen.
### 3 Sprosse und Merkmal
linearkombination-und-lineare-abhaengigkeit-zone-f4-v3, linearkombination-und-lineare-abhaengigkeit-zone-f4-v4: Vielfachenprüfung an Vektortripeln mit Faktor ist inhaltlich der Grundfall von e1 (f4-v4 sogar dessen nicht kollinearer Fall wie e1-k1-s1-v4), nur ohne das Wort „kollinear“ – die Zone nimmt das Lernblatt vorweg statt eine Stufe zurückzugehen; Sek-I-Form wählen (Zahlenpaare/Verhältnistabelle: proportional oder nicht).
linearkombination-und-lineare-abhaengigkeit-e1-k1-s0-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s0-v3: Beide Ja-Fälle der Vorstufe haben einen negativen Faktor (−2 bzw. −5), also den Sonderfall Gegenrichtung, den die Kette erst in Sprosse 2 einführt – mindestens einen Ja-Fall mit positivem Faktor nehmen.
linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v3, linearkombination-und-lineare-abhaengigkeit-e1-k1-s1-v5: Bruch- bzw. Dezimalfaktor ($\frac{1}{3}$, $0{,}5$) ist ein eigenes Merkmal (unterrichtsblatt 2.4 b), die Grundfall-Varianten sollen sich nur in den Zahlen unterscheiden – ganzzahlige Faktoren wählen.
linearkombination-und-lineare-abhaengigkeit-e1-k1-s2-v1, linearkombination-und-lineare-abhaengigkeit-e1-k1-s2-v2, linearkombination-und-lineare-abhaengigkeit-e1-k1-s2-v3: Die Varianten ändern verschiedene Merkmale – v1 und v3 nur Gegenrichtung, v2 nur Nullvektor; v3 bringt zusätzlich Dezimalkomponenten – jede Variante beide Fälle tragen lassen (Gegenrichtung plus Frage zum Nullvektor) und ganzzahlig bleiben.
linearkombination-und-lineare-abhaengigkeit-e2-k1-s2-v1, linearkombination-und-lineare-abhaengigkeit-e2-k1-s2-v2, linearkombination-und-lineare-abhaengigkeit-e2-k1-s2-v3: Drei verschiedene Aufgabentypen in einer Sprosse (v1 Punkte an den Parametergrenzen, v2 Punktprobe mit $q$ außerhalb, v3 Teilverhältnis $AX : XB$); das Teilverhältnis in v3 steht weder im Sprossentext noch im Merkmal – alle drei als Endpunkte/Grenzen plus ein Punkt außerhalb anlegen, v3 ohne Teilverhältnis.
### 4 Schreibform
linearkombination-und-lineare-abhaengigkeit-zone-f1-v5: Fehler finden bei einer Umformung einzeilig statt senkrecht mit \rechnung (unterrichtsblatt 2.3 c); der Zwischenschritt $\vec{a} - t \cdot \vec{a} + t \cdot \vec{b}$, an dem der Fehler sitzt, fehlt – als senkrechte Rechnung mit diesem Zwischenschritt setzen.
linearkombination-und-lineare-abhaengigkeit-e1-k1-s3-v2: Aus „keine Lösung“ folgt „linear unabhängig“ nur, weil $\vec{a}$ und $\vec{b}$ nicht kollinear sind; der Merkkasten deckt nur die Richtung „geht es auf, sind sie abhängig“ – Halbsatz „$\vec{a}$ und $\vec{b}$ sind nicht kollinear“ in der Lösung ergänzen.
linearkombination-und-lineare-abhaengigkeit-e1-k1-s4-v2: $r$ erscheint in der Lösung ohne Ansatz – „Ansatz $\vec{AC} = r \cdot \vec{AB}$:“ voranstellen.
### 5 Ankreuzen
keine
### 6 Fehler finden
keine

## Entscheidungen

- Keine Korrektur: alle 58 Lösungen und pruef-Werte sind rechnerisch richtig (nachgerechnet, u. a. Kreuzprodukt für Kollinearität, Determinante für e1-k1-s3, Punktprobe und Teilverhältnis in e2-k1-s2).
- pruef-Werte, die bei Lösungen ohne eigentliche Lösungszahl (etwa „keine Lösung“, Fehler finden) eine Zahl aus dem Lösungstext tragen, gelten als passend, nicht als Befund.
- Fehlende Pflichtelemente in e1 und fehlende Erkennungsschritte sind Fragen des Bestands (stand.md), keine Zeilenbefunde.
- Zwei verschiedene sehr leichte Teilaufgaben in einer Zone-Fertigkeit (z. B. f2-v1 Ablesen, f2-v2 Einsetzen) gelten als zulässig (unterrichtsblatt 2.2 verlangt nur „zwei sehr leichte“).
- Die Verfremdung von 2017-bb-ea-B3.1d als Pyramide $ABCDS$ (e2-k1-s3-v1, Dachstuhl statt Zelt, andere Zahlen, Kante $BS$) gilt als ausreichend.

Sauber: 38 Zeilen ohne Befund

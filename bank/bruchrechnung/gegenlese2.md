# Zweitlesung bruchrechnung

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 263
(zone 26, e1 59, e2 35, e3 59, e4 42, e5 42)

Prüfung: Alle 263 Zeilen gelesen (Aufgabe, Grafik, Antwortgerüst, Lösung, pruef, Sprosse, Merkmal). Die 115 reinen Rechenaufgaben (form teil, Aufgabe nur ein Term) hat ein eigenes Skript aus dem LaTeX in sympy-Rationals übersetzt und ausgewertet; alle 115 stimmen mit pruef überein. Die Sach-, Wahrscheinlichkeits- und Prüfungsaufgaben (Pfadsummen und -produkte, Gegenereignis, Flaschen/Seil/Netze, Rezept, Kosten mit Cent und Euro, Kassenzettel, Rabattterme, Punkt vor Strich im Sachkontext) wurden mit sympy einzeln nachgerechnet, dazu die Wahrscheinlichkeiten aus den Angaben (Glücksrad, Bonbons, Losreihenfolge, Freiwürfe, Codes) selbst hergeleitet; kein rechnerischer Fehler, jede pruef-Zahl steht mit richtiger Rundung in der Lösung. Ankreuzen: 11 Zeilen (zone-f4-v4, vier \janein-Zeilen in e1-k1, vier „von“-Zeilen in e3-k2, zwei Rabatt-Termprüfungen mit je drei Termen in e5) – jede Option einzeln geprüft, je genau eine richtige Antwort bzw. je Term das richtige Ja/Nein. Fehler finden: 16 Zeilen (Zone-Paar und je Einheit drei) – jeder eingebaute Fehler ist wirklich falsch und aus dem genannten Fehlverhalten erklärbar, jede Richtigrechnung stimmt. Streifen- und Tabellengrafiken passen zu den Werten. `werkzeuge/bank-pruef.py bruchrechnung`: 0 Abweichungen, 0 Warnungen in allen Dateien. Die Befunde unten betreffen nur das Merkmal.

## Befunde

e1-k4-s1-v3: [M] $2 + \frac{7}{4}$ verlangt zusätzlich, den unechten Bruch in eine gemischte Zahl umzuwandeln; v1 und v2 hängen nur an („ganze Zahl plus Bruch“). Die Variante ändert mehr als das Merkmal – Vorschlag: echter Bruch, etwa $4 + \frac{3}{8}$.

e1-k5-s1-v2: [M] Sprosse „Fehler finden (Zähler und Nenner addiert)“, eingebaut ist aber „beim Erweitern nur den Nenner geändert“ (ein anderes Muster aus Typische Fehler) – Vorschlag: ungleichnamige Addition mit Zähler plus Zähler, Nenner plus Nenner, etwa $\frac{2}{3} + \frac{1}{4} = \frac{3}{7}$, oder die Zeile als Zone-Fallstrick führen.

e3-k2-s0-v1, e3-k2-s0-v2, e3-k2-s0-v3, e3-k2-s0-v4: [M] Die Vorstufe heißt „„von“ markieren“, die Zeilen verlangen aber ein Ja/Nein, ob „von“ hier mal heißt (zwei davon mit Sätzen ohne Zahl); markiert wird nichts. Das Markieren leistet schon der Erkennungsschritt k1 („von“ unterstreichen, Malaufgabe aufschreiben) – Vorschlag: bank.md-Regel „gleicher Handgriff → Erkennungsschritt entfällt“ anwenden (wie in e5 geschehen) und die Vorstufe als „von“ unterstreichen in Anteilssätzen fassen, oder die Ja/Nein-Deutung in stand.md als Abweichung vom Sprossentext ausweisen.

e3-k3-s4-v3: [M] Sprosse „kürzen“ (Merkmal: vor dem Ausrechnen kürzen) in der Kette nach „Bruch geteilt durch Bruch mit Kehrbruch“; $\frac{8}{15} : 4$ ist wieder Bruch geteilt durch Zahl, und die Lösung $\frac{8}{60} = \frac{2}{15}$ kürzt erst nach dem Ausrechnen – Vorschlag: Bruch durch Bruch mit kürzbarem Kreuzpaar, etwa $\frac{4}{9} : \frac{8}{15}$ mit $\frac{4}{9} \cdot \frac{15}{8} = \frac{1 \cdot 5}{3 \cdot 2} = \frac{5}{6}$.

e4-k3-s1-v3: [M] Sprosse „Fehler finden (Kommastellen nicht gezählt)“, eingebaut ist aber „Komma nur beim Teiler verschoben“ bei einer Division (eigenes Muster in Typische Fehler) – Vorschlag: eine dritte Multiplikation mit falsch gezählten Kommastellen, etwa $0{,}6 \cdot 0{,}05 = 0{,}3$ (richtig $0{,}03$).

Sauber: 255 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k4-s1-v3 – der unechte Bruch 7/4 verlangt einen Umwandlungsschritt, den v1 und v2 nicht haben.
Beide Leser: e3-k3-s4-v3 – Bruch geteilt durch Zahl statt durch Bruch, und das Kürzen kommt erst nach dem Ausrechnen (Erstleser unter Merkmal und Schreibform, Zweitleser als ein Merkmalsbefund).
Beide Leser: e1-k5-s1-v2 – eingebaut ist „nur den Nenner erweitert“ statt „Zähler und Nenner addiert“ (Erstleser unter F, Zweitleser unter M; gleicher Inhalt).
Beide Leser: e4-k3-s1-v3 – eingebaut ist eine Division mit „Komma nur beim Teiler verschoben“ statt „Kommastellen nicht gezählt“ (Erstleser unter F, Zweitleser unter M).

Nur Erstleser: e1-k3-s6-v3 (ungleichnamige gemischte Zahlen, schwerer als v1/v2) – nicht bestätigt: die Sprosse steht in der Kette nach „beide erweitern (Hauptnenner)“, ein früheres Merkmal mitzunehmen ist zulässig und die Aufgabe verfehlt das eigene Merkmal nicht; höchstens als Hinweis auf ungleich schwere Geschwister.
Nur Erstleser: e1-k3-s7-v5, e1-k3-s7-v6 (zwei Pfade mit gleichem Nenner) – nicht bestätigt: sie verfremden 2020-OS-K6c (15/216 + 1/216, zwei Pfade, gleicher Nenner), das der Katalog ausdrücklich dieser Sprosse zuordnet; die Unschärfe liegt im Sprossentext (Katalogbefund), nicht in der Bank.
Nur Erstleser: e1-k3-s7-v7, e1-k3-s7-v8 (nur zwei Pfade) – nicht bestätigt: Verfremdung von 2017-OS-K6b (1/6 + 5/6 · 1/5, zwei Pfade), vom Katalog dieser Sprosse zugeordnet; Nenner sind verschieden.
Nur Erstleser: e3-k2-s5-v3, e3-k2-s5-v4 (zwei statt drei Brüche) – nicht bestätigt: Verfremdung von 2018-OS-K7c (14/16 · 13/15), das der Katalog unter „drei Brüche …; ebenso 2018-OS-K7c“ führt; die Falle „Nenner weiterzählen“ bleibt erhalten.
Nur Erstleser: e4-k2-s8-v3, e4-k2-s8-v4 (kein Wechsel zwischen Cent und Euro) – nicht bestätigt: sie verfremden 2024-OS-K2d, bei dem laut Katalog „die Einheit Cent bleiben muss“ (16 · 0,14 ct = 2,24 ct); das Merkmal „Ergebnis in der verlangten Einheit“ ist erfüllt. Die Formulierung des merkmal-Felds („mit Wechsel“) passt nur auf v1/v2 – dort wäre nachzuschärfen, nicht an der Aufgabe.
Nur Erstleser: e4-k3-s3-v3 (Preis geteilt durch Anzahl, keine Entscheidung) – bestätigt: Sprosse „Preis mal Anzahl“ und merkmal „… Entscheidung“ werden verfehlt; die Aufgabe ist eine Division mit Differenz. Von mir übersehen.
Nur Erstleser: e5-k1-s0-v4 (Klammer in der Vorstufe) – bestätigt, leicht: das merkmal nennt Punkt vor Strich mit natürlichen Zahlen, die Klammer ist erst Sprosse s4; ich hatte es gesehen und zu Unrecht verworfen.
Nur Erstleser: e5-k1-s6-v3, e5-k1-s6-v4 (sichtbare Klammer statt Bruchterm) – nicht bestätigt: sie verfremden 2016-OS-B1i, dessen Term im Original selbst „(a + b) : c“ lautet; der Sprossentext „erst die Klammer, dann die Division“ ist erfüllt. Die Bruchstrich-Falle tragen v1/v2 (2021-OS-B1g).
Nur Erstleser: e1-k5-s4-v1 (4/10 ungekürzt) – nicht bestätigt: Darstellungsaufgabe, gefragt ist die Minusaufgabe zum Bild, und 4/10 ist genau der gezeigte Anteil; „= 2/5“ zu ergänzen schadet nicht, ist aber kein Fehler.
Nur Erstleser: e3-k4-s1-v2 („gleichnamig gemacht, Nenner behalten“ beim Multiplizieren) – bestätigt, schwach: das Muster steht in Typische Fehler („Beim Multiplizieren gleichnamig gemacht“), aber nicht im Sprossentext „Kehrbruch beim Multiplizieren; beim Teilen den Zähler geteilt“; gleiche Messlatte wie bei e1-k5-s1-v2 und e4-k3-s1-v3, von mir nicht konsequent angewandt.
Nur Erstleser: e3-k5-s1-v1 („Nenner geteilt“ statt „Zähler geteilt“) – nicht bestätigt als Bankbefund: die Aufgabe folgt dem Katalogbeispiel 3/4 : 2 = 3/2, der Widerspruch steckt im Katalog selbst (stand.md Befund 5); zu klären im Katalog, nicht in der Zeile.

Nur Zweitleser: e3-k2-s0-v1 bis v4 – die Vorstufe „„von“ markieren“ wird als Ja/Nein-Entscheidung umgesetzt, markiert wird nichts; das Markieren liegt schon im Erkennungsschritt k1.

Widersprüche: keine – die Leser urteilen nirgends gegensätzlich über dieselbe Aussage; Unterschiede sind Befunde, die nur einer führt (oben mit Urteil).

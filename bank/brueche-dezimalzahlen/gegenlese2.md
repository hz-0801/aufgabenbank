# Zweitlesung brueche-dezimalzahlen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 311
(zone 30, e1 79, e2 47, e3 41, e4 49, e5 65)

Prüfung: Jede Zeile aller sechs Dateien gelesen (Aufgabe, Grafik,
Lösung, pruef, Merkmal gegen sprosse_text und Mappe). Brüche,
Vergleiche, Ordnungen, Sektorwinkel, Dreiecksflächen in den
ksys-Figuren, Prozentanteile, Wurzelvergleiche und Rundungen mit
einem eigenen sympy/Fraction-Skript nachgerechnet (49 Prüfsätze,
alle bestätigt); jede pruef-Zahl passt zur Lösung (Rundung der
Rundungsaufgaben und von 1,69 : 1,5 ≈ 1,13 nachgesehen). 27
Ankreuzzeilen (einschließlich ja/nein) Option für Option gegen Text
und Grafik geprüft, in jeder genau eine Option richtig und wortgleich
in loesung. 16 Fehler-finden-Zeilen (einschließlich Zone-Paar): der
eingebaute Fehler ist jeweils wirklich falsch und entspricht dem
Muster aus „Typische Fehler“, die Richtigrechnung stimmt.
`werkzeuge/bank-pruef.py brueche-dezimalzahlen`: Abweichungen 0,
Warnungen 0. Rechnerisch falsch ist keine Zeile; die Befunde betreffen
Merkmal, Darstellung und eine Ankreuzfrage.

## Befunde

e1-k1-s3-v3, e1-k1-s6-v3, e1-k1-s6-v4: [E] Die Kästchenfigur ist als
Koordinatensystem (`ksys` mit Achsen und Zahlen) gesetzt, das Dreieck
ist nicht grau, der Rechteckrand oben und rechts ist nur Gitterlinie;
bei s6 fehlt damit auch die „graue Fläche“ der P10-Form 2024-OS-B1b –
Dreieck grau füllen und die Achsen ausblenden (oder eine
Kästchen-Grafik ohne Achsen verwenden).

e1-k3-s1-v3: [M] Variante ändert mehr als die Zahlen: v1 und v2
haben einen Stammbruch (Teil mal Nenner), v3 mit 2/3 verlangt einen
zusätzlichen Schritt (erst durch den Zähler teilen) – v3 ebenfalls
mit Stammbruch (z. B. ein Sechstel sind 5 Stück), oder die
Zähler-größer-1-Form als eigene Sprosse führen.

e3-k1-s0-v2: [A] Bei 4/7 und 4/9 führt auch „mit einem Halben
vergleichen“ sofort zum Ziel (4/9 < 1/2 < 4/7); welcher Weg „am
schnellsten“ ist, ist dann Ermessen – ein Paar wählen, bei dem beide
Brüche auf derselben Seite von 1/2 liegen (z. B. 5/7 und 5/9).

e4-k1-s8-v1, e4-k1-s8-v2: [M] Wurzeloptionen (√5, √3) in Einheit 4
(Kl. 5/6, Umwandeln); Wurzeln sind im Katalog erst Vorrat in Einheit 5
(potenzen-wurzeln.md), und der Sprossentext nennt Bruch und
Prozentangabe, nicht Wurzel – die dritte Option durch eine
Prozentangabe ersetzen (z. B. 26 % > 5/2 bzw. 18 % > 7/4 als falsche
Aussage), die Wurzelform bleibt e5-k2-s9-v5/v6 vorbehalten.

e5-k6-s4-v1: [M] sprosse_text ist „runden auf Zehntel und Hundertstel
(auch Größen mit Einheit)“, die Aufgabe verlangt nur Ordnen, kein
Runden – Frage um einen Rundungsauftrag ergänzen (z. B. Zeiten auf
Zehntel für die Anzeigetafel) oder eine Rundungssituation wählen.

e5-k6-s4-v2: [M] Der Preis je Liter verlangt 1,69 : 1,5, also Division
durch eine Dezimalzahl, die weder in diesem Eintrag noch in den
Voraussetzungen (Division natürlicher Zahlen) steht – Packungsgröße
2 l wählen (z. B. 2,29 € → 1,145 € ≈ 1,15 €) oder 0,5 l.

Sauber: 302 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k3-s1-v3: v3 mit Zähler 2 ändert mehr als Zahlen und
Kontext (Stammbruch nehmen). e5-k6-s4-v2: der Literpreis verlangt eine
Division durch eine Dezimalzahl (mit periodischem Ergebnis), die der
Eintrag nicht kennt; der Vorschlag des Erstlesers (Vergleich über 3 l)
ist besser als meiner, weil er ganz ohne Division auskommt.

Nur Erstleser: e1-k1-s6-v17, e1-k1-s6-v18 (pruef [1, 6] bzw. [1, 5]
bei Buchstabenoptionen) – bestätigt als Formfehler gegen bank.md
(„pruef trägt die Zahl, wenn die Optionen Zahlen sind, sonst ""“);
die Lösung selbst stimmt, bank-pruef.py prüft den Fall nicht.
e1-k1-s0-v4 (Frage „Darf man hier einfach die Teile zählen?“ ohne
Zweck) – nicht bestätigt: der Wortlaut ist der des Katalogs
(Erkennungsschritt „ob man die Teile einfach zählen darf“) und steht
nach v1–v3 im selben Zusammenhang; die Ergänzung schadet aber nicht.
e1-k1-s6-v13, e1-k1-s6-v14 (einzeiliger Streifen mit Nenner-vielen
Teilen, Spaltenfalle von 2021-OS-B1b fehlt) – bestätigt: die
Verfremdung verlangt „gleiche Falle“, und mit 12 bzw. 9 Einzelteilen
ist die Aufgabe nur Sprosse 2 (Anteil einzeichnen); ich hatte die
Zeilen durchgelassen. e3-k2-s1-v3 (2/3 und 3/4 ungleichnamig, v1/v2
gleichnamig) – bestätigt: v3 verlangt vor dem Verfeinern das
Gleichnamigmachen, ein zusätzlicher Schritt; von mir übersehen.
e2-k4-s1-v3 („nur den Nenner erweitert“ nicht im Muster) – nicht
bestätigt: „Typische Fehler“ (Zeile 96) nennt ausdrücklich „Nur der
Zähler erweitert (oder nur der Nenner)“; das Muster ist gedeckt.

Nur Zweitleser: e1-k1-s3-v3, e1-k1-s6-v3, e1-k1-s6-v4 – Kästchenfigur
als ksys mit Achsen, Dreieck nicht grau. e3-k1-s0-v2 – bei 4/7 und
4/9 ist „mit einem Halben vergleichen“ ebenso schnell wie „gleicher
Zähler“. e4-k1-s8-v1, e4-k1-s8-v2 – Wurzeloptionen in Einheit 4.
e5-k6-s4-v1 – Aufgabe ordnet nur, sprosse_text verlangt Runden.

Widersprüche: e1-k1-s0-v4 und e2-k4-s1-v3 – der Erstleser sieht einen
Befund, ich nicht (Gründe oben). Sonst keine: die übrigen Befunde des
Erstlesers habe ich übersehen, nicht anders beurteilt.

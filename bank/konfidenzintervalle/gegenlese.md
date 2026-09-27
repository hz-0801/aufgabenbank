# Gegenlese: konfidenzintervalle

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 98 (zone 26, e1 25, e2 25, e3 22)
Korrekturen: 0

Jede Lösung aus der Aufgabe neu gerechnet (Python/sympy/scipy):
Grenzgleichung (Wilson-Grenzen), Binomialwerte, n-Schwellen,
μ ± 1,96σ, Überdeckungsbereiche der Intervalldiagramme. Alle
Lösungen und pruef-Werte stimmen, auch nach Rundung auf die
Stellen der Lösung.

Selbst entschieden (nicht geregelt): Die sprosse_text der
Pflichtzeilen melde ich unter Punkt 3, weil bank.md für
Pflichtzeilen keinen Sprossentext festlegt und der Grundfalltext
nicht zu Fehler-finden- und Begründen-Zeilen passt. Die
Modellkennung steht nicht im Kopf, weil die Sitzung keine
Modellkennung in Repo-Dateien schreiben darf.

## Punkt 1 – Lösung und pruef

(keine Befunde)

## Punkt 2 – eindeutig lösbar

konfidenzintervalle-e1-k1-s2-v1: Die Entscheidung „überdeckt 0,50“ hängt an der oberen Grenze 0,518; 0,018 sind auf der Grafik 0…1 mit Karo 0,1 nicht sicher ablesbar – Zahlen so wählen, dass die Grenze mindestens 0,03 von der Vermutung liegt, oder Achsenausschnitt mit feinerem xstep.
konfidenzintervalle-e1-k1-s2-v3: Obere Grenze 0,287 liegt nur 0,013 unter der Vermutung 0,30; „nicht verträglich“ ist grafisch nicht entscheidbar – andere Zahlen oder Ausschnitt (etwa xmin=0.1, xmax=0.4).
konfidenzintervalle-e1-k1-s4-v4: Obere Grenze 0,483 liegt nur 0,013 über der Vermutung 0,47; grafisch nicht sicher beurteilbar – Vermutung weiter vom Rand (etwa 0,44) oder Ausschnitt.
konfidenzintervalle-e2-k1-s3-v3: Richtiges Intervall 3 [28,6; 37,8] und Intervall 1 [28,4; 37,6] liegen auf der Zahlengeraden 25–42 nur 0,2 Prozentpunkte auseinander, \intervall trägt nur die Nummer – Grenzen beschriften oder Maßstab stark vergrößern.
konfidenzintervalle-e2-k1-s3-v4: Intervall 2 [63,0; 72,6] und Intervall 1 [63,2; 72,8] auf der Zahlengeraden 58–76 nicht unterscheidbar – Grenzen beschriften oder Maßstab vergrößern.
konfidenzintervalle-e2-k2-s1-v1: μ und σ nicht erklärt (das Original nennt „μ und σ von B(50; 0,6)“) – ergänzen: „μ und σ: Erwartungswert und Standardabweichung der Binomialverteilung mit n = 80 und p = 0,7“.
konfidenzintervalle-e2-k2-s1-v2: μ und σ nicht erklärt – ergänzen wie v1 (n = 120, p = 0,25).
konfidenzintervalle-e2-k2-s1-v3: μ und σ nicht erklärt – ergänzen wie v1 (n = 200, p = 0,45).
konfidenzintervalle-e3-k2-s2-v3: „die eine wird früher unverträglich“ gilt nicht, wenn der Stichprobenanteil 0,5 ist (dann gleiches p(1 − p), gleiche Schwelle) – „Der Stichprobenanteil ist nicht 0,5.“ ergänzen.
konfidenzintervalle-zone-f4-v1: μ und σ im Text nicht erklärt – „μ: Erwartungswert, σ: Standardabweichung“ ergänzen.
konfidenzintervalle-zone-f4-v2: Keine Verteilung genannt („der Werte“ wovon?), μ und σ nicht erklärt – „einer Binomialverteilung“ einfügen, μ und σ benennen.
konfidenzintervalle-zone-f4-v3: „Berechne μ, σ“ ohne Erklärung der Symbole – „Berechne den Erwartungswert μ, die Standardabweichung σ …“.

## Punkt 3 – Sprosse und Merkmal

konfidenzintervalle-e1-k1-s1-v4: Einzige Grundfall-Variante mit zwei Kurvenpaaren (äußere Graphen wählen), ändert mehr als Zahlen und Kontext – alle Grundfall-Varianten mit zwei Paaren bauen oder merkmal „äußere Graphen zur höheren Sicherheit“ für alle.
konfidenzintervalle-e1-k1-s4-v1: merkmal nennt „grafisches Intervall mit Beurteilung“, die Aufgabe hat keins – merkmal auf „Überdeckungszahl als Binomialgröße mit Nachweis“ kürzen.
konfidenzintervalle-e1-k1-s4-v2: wie v1 – merkmal kürzen.
konfidenzintervalle-e1-k1-s4-v3: Grafisches Intervall mit Beurteilung (2025-3-2c) unter sprosse_text „Überdeckungszahl … binomialverteilt“; der Katalog (Z. 77) hängt 2025-3-2c an die Sprosse s2, die Zielmarke (Z. 84) an die Prüfungshöhe; außerdem Vermutung 20 % mit Sicherheit 90 % wie im Original – als Katalogbefund klären, dann umhängen zu s2 oder ersetzen; Vermutung ändern (etwa 21 %).
konfidenzintervalle-e1-k1-s4-v4: wie v3 (grafische Beurteilung unter Überdeckungszahl-Sprosse) – umhängen oder ersetzen.
konfidenzintervalle-e1-k2-s1-v1: Pflicht fehler mit dem Grundfall-sprosse_text („Intervall … ablesen“) – sprosse_text aus „Typen je Lerneinheit“ Z. 21 (Fehler finden …), sobald bank.md die Pflicht-Sprossentexte regelt.
konfidenzintervalle-e1-k2-s1-v2: wie e1-k2-s1-v1.
konfidenzintervalle-e1-k2-s1-v3: Binomialrechnung „genau/mindestens“ unter sprosse_text „Intervall ablesen“ – wie e1-k2-s1-v1.
konfidenzintervalle-e1-k2-s2-v1: Pflicht begruenden (Überdeckungszahl) unter Grundfall-sprosse_text – sprosse_text „Begründen (…)“ aus Z. 21.
konfidenzintervalle-e1-k2-s2-v2: wie e1-k2-s2-v1.
konfidenzintervalle-e1-k2-s2-v3: wie e1-k2-s2-v1.
konfidenzintervalle-e2-k1-s3-v1: merkmal nennt „Grenzen auf Tausendstel und das passende Intervall im Bild“, die Aufgabe hat das nicht – merkmal auf die Ungleichung in n kürzen.
konfidenzintervalle-e2-k1-s3-v2: wie v1 – merkmal kürzen.
konfidenzintervalle-e2-k1-s3-v3: Grenzen berechnen und Intervall zuordnen (MMS3-2a, laut Katalog Z. 78 Grundfall) unter sprosse_text „kleinsten Umfang … ermitteln“ – umhängen oder durch Mindestumfang-Aufgabe ersetzen.
konfidenzintervalle-e2-k1-s3-v4: wie v3.
konfidenzintervalle-e2-k2-s1-v3: Weicht von v1/v2 in der Form ab (keine Sicherheitswahrscheinlichkeit, keine Verträglichkeitsdefinition) und verrät mit „vergleiche die Anzahl, nicht den Anteil“ die Falle – Text wie v1/v2, Hinweis streichen, „95 %“ ergänzen.
konfidenzintervalle-e2-k3-s1-v1: Pflicht fehler unter Grundfall-sprosse_text – sprosse_text „Fehler finden (…)“ aus Z. 22.
konfidenzintervalle-e2-k3-s1-v2: wie e2-k3-s1-v1.
konfidenzintervalle-e2-k3-s1-v3: wie e2-k3-s1-v1.
konfidenzintervalle-e2-k3-s2-v1: Pflicht begruenden unter Grundfall-sprosse_text – sprosse_text „Begründen (…)“ aus Z. 22.
konfidenzintervalle-e2-k3-s2-v2: wie e2-k3-s2-v1.
konfidenzintervalle-e2-k3-s2-v3: wie e2-k3-s2-v1.
konfidenzintervalle-e3-k1-s2-v3: Umkehrung („um welchen Faktor den Umfang vergrößern“) statt Vorwärtsfrage wie v1/v2, also eigenes Merkmal – vorwärts formulieren oder als eigene Sprosse führen.
konfidenzintervalle-e3-k1-s3-v1: merkmal nennt „Längenfaktor begründen“, die Aufgabe hat das nicht – merkmal kürzen.
konfidenzintervalle-e3-k1-s3-v2: Anders als v1 und das Original gibt v2 die Rechnungen I/II nicht vor, der Schüler stellt beide Schwellen selbst auf; merkmal nennt „Längenfaktor“ – Rechnungen wie in v1 vorgeben, merkmal kürzen.
konfidenzintervalle-e3-k1-s3-v3: Längenfaktor 1/√2 (2018-2-1g, laut Katalog Z. 79 Sprosse s2) unter sprosse_text „n-Schwellen“ – umhängen oder durch n-Schwellen-Aufgabe ersetzen.
konfidenzintervalle-e3-k1-s3-v4: wie v3 (Längenfaktor 1/√3).
konfidenzintervalle-e3-k2-s1-v1: Pflicht fehler unter Grundfall-sprosse_text – sprosse_text „Fehler finden (…)“ aus Z. 23.
konfidenzintervalle-e3-k2-s1-v2: wie e3-k2-s1-v1.
konfidenzintervalle-e3-k2-s1-v3: wie e3-k2-s1-v1.
konfidenzintervalle-e3-k2-s2-v1: Pflicht begruenden unter Grundfall-sprosse_text – sprosse_text „Begründen (…)“ aus Z. 23.
konfidenzintervalle-e3-k2-s2-v2: wie e3-k2-s2-v1.
konfidenzintervalle-e3-k2-s2-v3: wie e3-k2-s2-v1.

## Punkt 4 – Schreibform

(keine Befunde)

## Punkt 5 – Ankreuzen

(keine Befunde)

## Punkt 6 – Fehler finden

(keine Befunde)

Sauber: 58 Zeilen ohne Befund

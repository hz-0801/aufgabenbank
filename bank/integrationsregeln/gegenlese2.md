# Zweitlesung integrationsregeln

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne Kenntnis
von gegenlese.md) · geprüfte Zeilen: 56 (e1 18, e2 23, zone 15)

Prüfung: jede Lösung mit sympy nachgerechnet (Stammfunktionen durch
Ableiten, Integrale numerisch), bank-pruef.py 0 Abweichungen, 0
Warnungen; dazu Lesbarkeit, Eindeutigkeit, Passung zu sprosse_text
und merkmal, Ankreuzoptionen, eingebaute Fehler.

## Befunde

integrationsregeln-e1-k1-s0-v1 bis v4: Der Sprossentext des Katalogs
nennt fünf Möglichkeiten (Potenz-, Faktor-, Summen-, Konstantenregel,
lineare innere Funktion); die Optionen tragen nur vier, die
Summenregel fehlt in allen vier Varianten und wird nirgends
abgefragt – Vorschlag: fünfte Option `\kreuz{Summenregel}` in alle
vier Zeilen, und eine Variante (etwa v4) mit einer Summe wie
$x^3 + x$ auf die Summenregel legen.

integrationsregeln-e1-k1-s0-v3: „für die Zahl 5 als Funktion" ist
holprig – Vorschlag: „für $f(x) = 5$".

integrationsregeln-e1-k1-s1-v1, -v5: Sprosse „Potenzen gliedweise
aufleiten" mit merkmal „Glied für Glied" – $x^4$ und $x^9$ haben
nur ein Glied, zwei der fünf Grundfälle üben das Merkmal nicht –
Vorschlag: je ein zweites Glied ($x^4 + x^2$, $x^9 + x^5$).

integrationsregeln-e1 (Einheit gesamt): keine Pflichtelemente
(fehler, begruenden) – bank.md verlangt sie je Einheit, „wo die
Typen sie tragen"; Fehler finden trägt der Regelsatz sicher
(Potenzregel ohne Teilen, lineare Substitution ohne Faktor) –
Vorschlag: Kette k2 mit 3 fehler und 3 begruenden ergänzen.

integrationsregeln-e2-k1-s0-v2, -s1-v3, -s3-v3: derselbe Integrand
$\mathrm{cos}(x) \cdot e^{\mathrm{sin}(x)}$ in drei Zeilen dreier
Sprossen; dazu $2x \cdot e^{x^2 + 1}$ in e2-k1-s0-v1 wortgleich das
Ergebnis von zone-f2-v3 – kein Verstoß gegen „keine Aufgabe
doppelt", aber der Schüler sieht dreimal dasselbe Paar g, g' –
Vorschlag: in s1-v3 einen anderen Integranden, etwa
$(3x^2 + 2) \cdot e^{x^3 + 2x}$; in s0-v1 etwa $2x \cdot e^{x^2 - 4}$.

integrationsregeln-e2-k2-s1-v2: Die Grenzen 0 und 1 stehen nur in
Jans Rechnung, nicht in der Aufgabe („Für $f(x) = \dots$ setzt Jan
…"); die Lösung rechnet mit ihnen – Vorschlag: „Für das Integral
von 0 bis 1 über $3x^2 \cdot e^{x^3 + 2}$ setzt Jan …" wie in v1
und v3. Der Fehler selbst ist echt (Jan verliert den Faktor $e^2$).

integrationsregeln-e2-k2-s1-v2, -v3: „Typische Fehler" des Katalogs
kennt nur das Vorzeichen der inneren Ableitung; v2 (g falsch
abgeschrieben) und v3 (Faktor ½ vergessen) sind eigene Muster –
vertretbar, weil nur ein Muster belegt ist, aber stand.md sollte
das unter Befunde nennen.

integrationsregeln-zone-f1-v1: „Schreibe als eine Potenz:
$x^2 \cdot x$" ist ein Potenzgesetz, nicht „Exponenten erhöhen,
durch Brüche teilen" (Fertigkeitstext) – Vorschlag: „Erhöhe den
Exponenten von $x^2$ um eins" oder „$x^3 : 3$" als Vorbereitung
der Potenzregel rückwärts. Außerdem pruef "" bei Lösung mit
Ziffer ($x^3$) – Vorschlag pruef "3".

integrationsregeln-zone-f1-v4: pruef "" bei Lösung $x^{-2}$ –
Vorschlag pruef "-2" (bank.md: "" nur ohne Ziffer).

Sauber: 42 Zeilen ohne Befund (alle Rechnungen stimmen; alle
Ankreuzzeilen haben genau eine richtige Option; alle drei
Fehler-finden-Zeilen und das Zone-Paar tragen einen echten Fehler;
beide Prüfungshöhen verfremden das Original mit anderen Zahlen und
gleicher Falle).

## Abgleich mit gegenlese.md

Erstleser: 2 Befunde (e2-k2-s2-v3, e2-k2-s1-v2). Zweitleser: 14
Zeilen mit Befund.

Beide: integrationsregeln-e2-k2-s1-v2 – Jans Fehler ist nicht das
Muster aus „Typische Fehler". Der Erstleser will die Zeile durch
ein Vorzeichen-Muster ersetzen; der Zweitleser hält das zweite
Muster für vertretbar, weil nur eines belegt ist, und fordert vor
allem die fehlenden Grenzen im Aufgabentext nach – die Ersetzung
des Erstlesers erledigt beides, ihr ist zu folgen.

Nur Erstleser: integrationsregeln-e2-k2-s2-v3 („mit dieser Regel"
ohne die Regel in der Zeile) – zutreffend, vom Zweitleser
übersehen; übernehmen.

Nur Zweitleser: e1-k1-s0-v1 bis v4 (Summenregel fehlt als Option),
e1-k1-s0-v3 (Wortlaut), e1-k1-s1-v1 und -v5 (nur ein Glied),
Einheit 1 ohne Pflichtelemente, e2-k1-s0-v1/-s0-v2/-s1-v3/-s3-v3
(wiederholte Integranden), e2-k2-s1-v3 (eigenes Muster),
zone-f1-v1 (Potenzgesetz statt Fertigkeit; pruef ""), zone-f1-v4
(pruef "").

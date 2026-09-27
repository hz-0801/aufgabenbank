# Zweitlesung hypergeometrische-verteilung

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne Kenntnis
von gegenlese.md) · geprüfte Zeilen: 62 (e1 26, e2 17, zone 19)

Prüfung: jede Wahrscheinlichkeit mit Python exakt nachgerechnet
(Fraction, math.comb: Bruchketten, Quotienten von
Binomialkoeffizienten, alle kumulierten Tabellen samt beiden
Nachbarwerten, die falschen Binomialrechnungen der
Fehler-finden-Zeilen), bank-pruef.py 0 Abweichungen, 0 Warnungen;
dazu Eindeutigkeit, Passung zu sprosse_text und merkmal,
Ankreuzoptionen, eingebaute Fehler, Verfremdung der Originale.

## Befunde

hypergeometrische-verteilung-zone-f4-v2, -v3: Die Bruchketten
$\frac{4}{7} \cdot \frac{3}{6} = \frac{2}{7}$ und
$\frac{5}{8} \cdot \frac{4}{7} \cdot \frac{3}{6} = \frac{5}{28}$ sind
Ziffer für Ziffer die Rechnungen von e1-k1-s1-v2 und e1-k1-s1-v1
(dort das verfremdete Original 2022-bebb-gk-A1.6a); die Zone
rechnet dem Schüler den Grundfall vor – Vorschlag: andere Brüche
($\frac{3}{8} \cdot \frac{4}{9}$, $\frac{2}{5} \cdot \frac{5}{6} \cdot
\frac{3}{4}$).

hypergeometrische-verteilung-zone-f2-v6: dieselbe Urne „$5$ weiße
und $3$ schwarze Kugeln" wie e1-k1-s1-v1 (Prüfkennung Abitur 2022
GK) – Vorschlag: andere Farben und Zahlen ($4$ rote, $2$ grüne
sind gesperrt, also etwa $6$ blaue, $2$ gelbe – die stehen aber in
f2-v7; dann $7$ und $3$).

hypergeometrische-verteilung-zone-f2-v2, -v4: zweimal dieselbe
Rechnung $\frac{2}{5} \cdot \frac{1}{4} = \frac{1}{10}$ (blaue Kugeln,
saure Bonbons) – Vorschlag: v4 mit $6$ Bonbons, $2$ sauer
($\frac{2}{6} \cdot \frac{1}{5} = \frac{1}{15}$).

hypergeometrische-verteilung-e2-k1-s0-v3: fragt den kumulierten
Ansatz $P(X \le 1) = P(X = 0) + P(X = 1)$; merkmal sagt „Ansatz für
eine Einzelwahrscheinlichkeit erkennen" – inhaltlich die bessere
Vorstufe zum Kumulieren, aber dann merkmal anpassen („Ansatz für
Einzel- und kumulierte Wahrscheinlichkeit erkennen") oder die Zeile
auf $P(X = 1)$ stellen.

hypergeometrische-verteilung-e2-k1-s0-v1, -v2, -v4: dieselben
Parametersätze wie der Grundfall und die Fehler-finden-Zeilen –
$(10, 4, 3)$ in s0-v1, s1-v1, k2-s1-v1; $(12, 5, 4)$ in s0-v2,
s1-v3, k2-s1-v3; $(16, 6, 5)$ in s0-v4, s1-v4; dazu $(18, 7, 5)$ in
s1-v5 und k2-s1-v2. Bei Fehler finden ist die Wiederverwendung
vertretbar (die richtigen Werte stehen im Grundfall), in der
Vorstufe nicht nötig – Vorschlag: eigene Zahlen in s0-v1, -v2,
-v4.

hypergeometrische-verteilung-e2-k1-s2-v2: Schranke $35\,\%$ ist die
Zahl des Originals 2023-bebb-lk-B4l (dort $30$, $12$, $5$,
$< 35\,\%$) – Vorschlag: $30\,\%$ oder $45\,\%$ (bei $45\,\%$
bleibt $n = 1$, weil $P(X \le 2) \approx 0{,}507$).

hypergeometrische-verteilung-e1-k1-s2-v1: der Anteil $\frac{9}{60}
= 0{,}15$ ist der Anteil des Originals ($\frac{12}{80}$); Rechnung
und Nachweis ($0{,}2534 \approx 25{,}3\,\%$) stimmen, die Binomial-
Falle liefert $0{,}2376$ – Vorschlag: $60$ Mitglieder, $12$ E-Bikes
($p = 0{,}2$; genau $2$ von $8$: $\approx 0{,}3165$, also
$31{,}7\,\%$).

hypergeometrische-verteilung-e1-k2-s3-v1 bis v3: sprosse_text
„Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das
Gegenereignis berechnen" statt des Typnamens „Anwendung" wie bei
„Fehler finden" und „Begründen" der Nachbarketten – Vorschlag:
„Anwendung (…)" nach dem Muster der anderen Pflichtzeilen. Die
drei Anwendungen sind sonst gut: realistische Größen, sinnvolle
Frage, Deutung des Ergebnisses.

Sauber: 48 Zeilen ohne Befund (alle Wahrscheinlichkeiten und alle
Nachbarwerte stimmen; alle zwölf Ankreuzzeilen haben genau eine
richtige Option; alle sieben Fehler-finden-Zeilen tragen echte
Fehler aus den Mustern der „Typischen Fehler", in e2-k2-s1-v1
kippt der Binomialfehler sogar das Ergebnis von $k = 1$ auf
$k = 0$; die Originale 2022-bebb-gk-A1.6a, 2017-bb-ea-B4.2e und
2023-bebb-lk-B4l (v1) sind mit anderen Zahlen und Kontexten bei
gleicher Falle verfremdet).

## Abgleich mit gegenlese.md

Erstleser: 8 Zeilen mit Befund, keine Korrektur. Zweitleser: 14
Zeilen mit Befund. Beide: alle Rechnungen richtig, Ankreuzen
eindeutig.

Beide: e2-k1-s0-v3 (kumulierter Ansatz gegen merkmal
„Einzelwahrscheinlichkeit"; der Erstleser will die Zeile umstellen,
der Zweitleser lässt auch die Anpassung des merkmals zu);
zone-f4-v2 mit e1-k1-s1-v2 (dieselbe Bruchkette – der Erstleser
hängt den Befund an e1-k1-s1-v2 und will dort „mindestens ein
Kirschbonbon" fragen, was zugleich seinen Merkmalbefund erledigt;
der Zweitleser ändert die Zone – der Weg des Erstlesers ist besser,
weil er zwei Befunde mit einer Änderung löst); zone-f4-v3 (der
Erstleser: Lösung kürzt nicht vor dem Multiplizieren; der
Zweitleser: dieselbe Kette wie e1-k1-s1-v1 – beides gilt).

Nur Erstleser, zutreffend und zu übernehmen: e2-k2-s2-v2 („größer
als" stimmt für $k = 0$ nicht – scharf gesehen); e1-k2-s2-v2 (der
Zufallsversuch fehlt in der Aufgabe); e1-k2-s2-v3 (Näherung bei
großer Gesamtheit ist keines der beiden Begründungsthemen der
Sprosse); e2-k2-s2-v2 (fragt Einzelwert statt Summe, Sprosse
verlangt die beiden Nachbarwerte).

Nur Zweitleser: zone-f2-v6 (Urne des Originals), zone-f2-v2/-v4
(gleiche Rechnung), e2-k1-s0-v1/-v2/-v4 (Parametersätze des
Grundfalls), e2-k1-s2-v2 (Schranke $35\,\%$ aus dem Original),
e1-k1-s2-v1 (Anteil $0{,}15$ aus dem Original), e1-k2-s3
(sprosse_text ohne Typnamen).

Widerspruch: e2-k2-s1-v2 (Ali vergleicht $P(X = 2)$ statt der
Summe) – der Erstleser sieht kein Muster der Sprosse und will die
Zeile umbauen; der Zweitleser hält sie für richtig gebaut, weil
„Typische Fehler" des Katalogs genau dieses Muster nennt („nur ein
Wert geprüft", fehlerquelle des Originals 2023-bebb-lk-B4l:
„$n = 2$ wegen $P(Y = 2) < 0{,}35$") – zu ändern wäre dann der
Sprossentext der Fehlerkette, nicht die Zeile.

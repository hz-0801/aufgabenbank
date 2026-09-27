# Zweitlesung uneigentliche-integrale

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne Kenntnis
von gegenlese.md) · geprüfte Zeilen: 59 (e1 23, e2 20, zone 16)

Prüfung: jede Rechnung mit sympy nachgerechnet (Flächenterme A(w),
Grenzwerte, Stammfunktionen durch Ableiten, Restflächen und ihre
Schranken, Anteile der schraffierten Restflächen für die Vorstufe,
Näherungsgüte der Prüfungshöhe: 37,49993 zu 37,5 und 11 999,94 zu
12 000), bank-pruef.py 0 Abweichungen, 0 Warnungen; dazu
Eindeutigkeit, Passung zu sprosse_text und merkmal, Ankreuzoptionen,
eingebaute Fehler, Verfremdung der Originale.

## Befunde

uneigentliche-integrale-e1-k1-s3-v1 bis v5, -e2-k1-s3-v1, -v2:
sprosse_text ist nur „Prüfungshöhe"; bank.md verlangt die Sprosse
wortgleich aus dem Katalog („Prüfungshöhe: die Existenzfrage an
einem schnell und einem langsam fallenden Graphen vergleichen"
bzw. „Prüfungshöhe: die vollständige Deutung der Näherungsaussage
im Sachzusammenhang") – Vorschlag: vollen Text eintragen; das
Prüfskript mit --katalog würde die Kürzung melden.

uneigentliche-integrale-e1-k1-s3-v1 bis v3, -e2-k1-s3-v1, -v2,
-e2-k2-s1-v1, -v3, -e2-k2-s2-v3, -zone-f2-v1 bis v4, -zone-f3-v1
bis v4 (16 Zeilen): Integralzeichen als Unicode „∫" im
Mathemodus, weil das Prüfskript `\int` ablehnt (stand.md). Mit
xelatex ohne unicode-math ist das Zeichen nicht gesetzt oder
kommt aus der Textschrift, und die Grenzen sitzen als Hoch- und
Tiefstellung falsch – in befunde.md als Z-067 offen. Vorschlag:
`\int` in bank-pruef.py als Baustein zulassen und die 16 Zeilen
umstellen; bis dahin gilt der Eintrag als nicht setzbar.

uneigentliche-integrale-e1-k1-s0-v1 bis v4: Der Erkennungsschritt
des Katalogs fragt zweierlei – „endet oder läuft aus" und „ob sie
trotzdem endlich sein kann"; die Zeilen fragen nur das Erste, und
v2 ($3e^{-x}$, endlich) und v4 ($\frac{2}{x+1}$, nicht endlich)
bekommen dieselbe Antwort – Vorschlag: dritte Option „läuft aus,
Inhalt trotzdem endlich" oder die zweite Frage als eigene Zeile
mit dem Graphen von v2 gegen v4.

uneigentliche-integrale-e1-k1-s1-v3 bis v5: drei der fünf
Grundfälle haben denselben Grenzterm $2 - 2e^{\dots}$
($e^{-0{,}5x}$, $4e^{-2x}$, $6e^{-3x}$) – kein Fehler, aber
die Varianten sollen sich in Zahlen unterscheiden – Vorschlag: v4
zu $5e^{-x}$ oder $2e^{-4x}$.

uneigentliche-integrale-e1-k1-s2-v1, -e2-k1-s1-v1, -e2-k1-s2-v2:
dieselbe Funktion $2e^{-0{,}5x}$ in drei Zeilen dreier Sprossen
(dazu $e^{-0{,}5x}$ in e1-k1-s1-v3 und e1-k2-s2-v2) – Vorschlag:
in e2 andere Vorfaktoren und Exponenten.

uneigentliche-integrale-e2-k1-s1-v1 bis v5: pruef "0", "1", "2",
"0", "5" sind die unteren Grenzen, keine Lösungszahl; die Lösung
ist ein Satz – Vorschlag: "" (bank.md-Regel für „Lösung ohne
Ziffer" um „Ziffern nur als Grenzen oder Bezeichner" erweitern,
wie schon bei linearkombination vermerkt).

uneigentliche-integrale-e2-k1-s2-v2: „$f(10) \approx 0{,}01$" –
genauer $0{,}013$ (zwei signifikante Stellen wie in v3 mit
$0{,}015$) – Vorschlag: „$\approx 0{,}013$".

uneigentliche-integrale-zone-f2-v3: $f(x) = e^{-x}$ mit
$F(w) - F(0)$-Blick ist die Funktion des Merkkastens (Einheit 1,
„Integral ab null über e^(−x)"); die Sperre gilt nach bank.md
auch für die Zone – Vorschlag: $f(x) = 2e^{-x}$ oder $e^{-2x}$.

Katalogbefund (keine Zeile): zone-f2-v5 und -v7 („Welche Fläche
beschreibt $F(5) - F(1)$?") und der Grundfall e2-k1-s1 („Was
bedeutet $F(w) - F(2)$ geometrisch?") sind derselbe Handgriff;
nur der Buchstabe $w$ unterscheidet sie. Entweder trägt die Zone
den Hauptsatz nur als Rechnung (f2-v1 bis v4) oder der Grundfall
bekommt ein eigenes Merkmal (etwa: $F(w) - F(0)$ mit dem Term
$1 - e^{-w}$ als wachsende Fläche deuten) – für stand.md, Befunde.

Sauber: 27 Zeilen ohne Befund (alle Rechnungen stimmen; alle acht
Ankreuzzeilen haben genau eine richtige Option, die
Restflächenanteile in e2-k1-s0 sind 0,7 %, 92 %, 0,2 % und 49 %
und trennen sauber; alle sechs Fehler-finden-Zeilen und das
Zone-Paar tragen echte Fehler; die vier Prüfungszeilen mit
Original verfremden mit anderen Funktionen, Grenzen und
Schranken bei gleichem Verfahren).

## Abgleich mit gegenlese.md

Erstleser: 6 Zeilen mit Befund, keine Korrektur. Zweitleser: 32
Zeilen mit Befund, davon 16 allein durch das Unicode-∫ (Z-067) und
7 durch den gekürzten sprosse_text. Beide: alle Rechnungen richtig,
Ankreuzen eindeutig.

Beide: uneigentliche-integrale-e2-k1-s2-v2 – aus verschiedenen
Gründen: der Erstleser beanstandet die Schranke $4e^{-5}$ ohne
Herleitung, der Zweitleser die Rundung $f(10) \approx 0{,}01$; beide
gelten.

Nur Erstleser, alle zutreffend und zu übernehmen: e1-k2-s1-v3
(kein Satz mit dem Gesuchten); e1-k1-s2-v3 ($w$ und $E(w)$ in der
Lösung ohne Einführung); e2-k1-s2-v1 und -v3 (Schranke aus der
Stammfunktion statt aus dem Abfallen des Graphen – der wichtigste
Befund des Erstlesers, weil er die Sprosse trifft); e2-k2-s1-v3
(Jans Fehler passt zu keinem Muster des merkmals).

Nur Zweitleser: sprosse_text „Prüfungshöhe" gekürzt (7 Zeilen);
Unicode-∫ (16 Zeilen, Z-067); e1-k1-s0-v1 bis v4 (zweite Frage des
Erkennungsschritts fehlt); e1-k1-s1-v3 bis v5 (gleicher Grenzterm);
Wiederholung von $2e^{-0{,}5x}$; pruef-Platzhalter in e2-k1-s1;
zone-f2-v3 (Merkkastenfunktion); Katalogbefund Zone f2 gegen
Grundfall e2.

Kein Widerspruch in der Sache.

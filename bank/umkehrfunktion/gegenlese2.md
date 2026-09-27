# Zweitlesung umkehrfunktion

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 91 (e1 32, e2 34,
zone 25)

Prüfung: Jede Zeile gelesen; jede Lösung mit sympy nachgerechnet
(Umkehrterme durch Auflösen nach x, Definitions- und Wertebereiche
über Randwerte und Grenzwerte, Ableitungen und Extremstellen,
Tangentensteigungen, Trapezflächen zusätzlich über die
Schnürsenkelformel, Integrale, Schnittpunkte mit y = x); das Feld
pruef gegen die Ergebnisstelle der Lösung gehalten; alle 23
Grafikfelder (grafik, loesungsgrafik) mit der Vorlage mathblatt.sty
aus bau/ kompiliert und als Bild angesehen – alle bauen, der
ksys-Clip schneidet Überstände ab, die Potenz mit Bruchexponent
(9x)^(1/3) ab 0 läuft (der offene Punkt in stand.md kann zu).
`python3 werkzeuge/bank-pruef.py umkehrfunktion`: zone 0/0, e1 0/0,
e2 0/0 – Abweichungen 0, Warnungen 0. Mengen je Kette stimmen
(Zone 5 Fertigkeiten mit 2+1+Fallstricke und dem Paar; e1 4+5+3+3+2,
Typ ohne Kette 3, Pflicht 12; e2 4+5+3+3+3+4, Pflicht 12).
Sperre gegen Merkkasten, Typische Fehler und Originale von Hand
verglichen (2·e^x − 2, ]−2; ∞[, x²/√x, y = 4, P(1 | 3), Steigung 4
→ 1/4, 5/e, 5e^{−3/5 x} − 5, 4/3 x², 1/2 √(3h)).

## Befunde

e1-k1-s0-v4: Der Text sagt „auf dem Intervall $[-2;\, 2]$", die
Grafik zeichnet $x^3 - 3x$ mit `\funktion` über $[-3;\, 3]$; der
Clip greift erst bei $y = \pm 4$, also bei $x \approx \pm 2{,}2$ –
der Schüler sieht den Graphen über das genannte Intervall hinaus
(im Bild sichtbar). – Vorschlag: `\funktionab{\x^3-3*\x}{f}{-2}{2}`;
bei v1 (`0.5*\x^3`) fällt der Clip zufällig genau auf $\pm 2$,
dort derselbe Griff nur der Gleichförmigkeit halber.

e1-k1-s2-v3: $f(x) = \sqrt{x} + 1$ auf $[0;\, 9]$ hat den
Wertebereich $[1;\, 4]$ – beide Grenzen werden angenommen, es gibt
keinen Grenzwert und keine offene Grenze. Die Sprosse heißt aber
„… offene Grenze bei einem Grenzwert", das Merkmal „eine nicht
angenommene Grenze bleibt offen"; v3 trägt das Merkmal nicht und
fällt damit auf die Zone (f2-v1/v2) zurück. – Vorschlag:
$f(x) = 1 + \frac{4}{x}$ auf $[1;\, \infty[$ (streng fallend,
$f(1) = 5$, Grenzwert 1): Definitionsbereich von g $]1;\, 5]$,
Wertebereich $[1;\, \infty[$; pruef `[1, 5]`.

e1-k1-s4-v1, e1-k1-s4-v2: Der Buchstabe h steht in Einheit 1
zweimal für verschiedene Dinge – hier für die eingeschränkte
Funktion („h ist f, eingeschränkt auf …"), in e1-k2-s1-v1 bis v3
für die Füllhöhe ($r(h)$). bank.md: „ein Buchstabe je Einheit für
eine Sache". Beide Namen kommen aus den Originalen, die Verfremdung
darf aber umbenennen. – Vorschlag: in s4-v1 und s4-v2 „k ist f,
eingeschränkt auf $[2;\, \infty[$" und „Umkehrfunktion von k"; k
ist in e1 sonst frei.

e1-k3-s1-v1: Ergebnis $]-2;\, \infty[$ ist wortgleich der
Definitionsbereich des Merkkasten-Beispiels ($f(x) = 2 \cdot e^x - 2$,
„g(x) = ln((x + 2)/2) mit Definitionsbereich ]−2; ∞["); die
Funktion $e^x - 2$ ist nur um den Faktor 2 vom Kastenbeispiel
entfernt. bank.md sperrt „Ergebnisse" aus dem Kasten. –
Vorschlag: $f(x) = e^x - 3$, richtig $]-3;\, \infty[$, pruef `-3`
(kollidiert mit keiner anderen Zeile; $e^x + 3$ in s1-v4/s2-v1 ist
eine andere Funktion).

e2-k2-s1-v2: „Steigung 4 im Punkt (2 | 5), richtig $\frac{1}{4}$"
ist das Zahlenbeispiel des Merkkastens („Steigung 4 in P → Steigung
1/4 in P'") – Sperre. Dazu ist Bens Fehler (Gegenzahl −4 statt
Kehrwert) kein Muster aus „Typische Fehler" (dort: Symmetrieachse
nicht erkannt, Bereiche verwechselt, Trapezhöhe falsch; in der
Typenzeile: „Tangente neu berechnet statt gespiegelt"), sondern der
Zone-Fallstrick f5-v4. Rechnung selbst richtig. – Vorschlag:
Steigung 5 im Punkt (2 | 7), Ben nennt −5, richtig $\frac{1}{5}$,
pruef `[1, 5]`; das Muster bleibt dann Ermessen, aber ohne
Kastenzahl.

e2-k2-s1-v3: Dieselben Punkte A(0 | 4), B(1 | 7) wie in
e2-k1-s4-v1, dieselbe Rechnung (Mittelpunkte (2 | 2), (4 | 4), Höhe
$2\sqrt{2} \approx 2{,}83$) – die Fehler-finden-Zeile wiederholt die
Sprossenzeile. Nachgerechnet: $|AB| = \sqrt{10} \approx 3{,}16$,
Höhe $2\sqrt{2}$, Fläche 20. Außerdem nimmt Lara $|AB|$ (einen
Schenkel), das Muster in „Typische Fehler" ist „Höhe als Abstand
zweier Spiegelpunkte |PS|", also eine der parallelen Seiten. –
Vorschlag: A(1 | 3), B(2 | 8); Lara nimmt als Höhe $|AA'|$;
richtig: Mittelpunkte (2 | 2) und (5 | 5), $h = 3\sqrt{2}
\approx 4{,}24$ (zur Probe: $|AA'| = 2\sqrt{2}$, $|BB'| = 6\sqrt{2}$,
Fläche 24), pruef `3*math.sqrt(2)`.

e2-k1-s3-v1: „… gib den Berührpunkt an" – Q ist im Text nur ein
Name ohne Koordinaten, die Lösung kann deshalb nur „Spiegelpunkt von
Q" sagen und schreibt ihn nicht einmal als $Q'(y_Q \,|\, x_Q)$; es
gibt nichts Prüfbares. Nachgerechnet: $f'(x) = -3e^{-\frac{1}{2}x}
= -1 \Leftrightarrow x = 2\,\mathrm{ln}\,3$, $f(2\,\mathrm{ln}\,3)
= 0$, also Q$(2\,\mathrm{ln}\,3 \,|\, 0)$. – Vorschlag: „im Punkt
Q$(2\,\mathrm{ln}\,3 \,|\, 0)$" in den Text; Lösung ergänzt
„Berührpunkt $(0 \,|\, 2\,\mathrm{ln}\,3)$". (v2 sagt „beschreibe"
und passt so; dort wäre der Punkt $(2 \,|\, \tfrac{13}{3})$ →
$(\tfrac{13}{3} \,|\, 2)$.)

e2-k2-s4-v2: $f(x) = x^2$ ist die Funktion des Merkkastens
(„f(x) = x² … auf [0; ∞[ schon: g(x) = √x"), und die Lösungsgrafik
zeichnet genau $\sqrt{x}$. Die Ausnahme in bank.md (x² als Form
frei) gilt für Sprossentexte, die die Form nennen; dieser nennt sie
nicht. Ermessensfall, das Skript lässt es durch. – Vorschlag:
$f(x) = x^3$ (umkehrbar auf ℝ, $f'(1) = 3$): grafik
`\funktionab{\x^3}{f}{0}{1.7} \gerade{3}{-2}{t}`, Lösung Steigung 3
abgelesen, Spiegeltangente Steigung $\frac{1}{3}$ durch (1 | 1):
`\gerade{0.3333}{0.6667}{t'}`, g als `\funktionab{\x^(1/3)}{g}{0}{4.8}`.

zone-f5-v4: „Eine Gerade mit der Steigung 3 wird an $y = x$
gespiegelt. Welche Steigung hat das Bild?" ist bis auf die Zahl und
die Form die Vorstufe e2-k1-s0-v2 („… Steigung 2 …", Ankreuzen).
Auf einem Blatt stünden beide. Die Wurzel liegt im Katalog
(Fertigkeit 5 „Ermessen" und Erkennungsschritt „Wer spiegelt wohin?"
decken sich), der Katalogbefund in stand.md nennt das nicht. –
Vorschlag: Zone-Zeile mit Rechnung statt Kopfzahl: „Steigung
$-0{,}4$" → $m = -2{,}5$, nicht $0{,}4$; pruef `-2.5`; dazu eine
Zeile unter „Befunde" in stand.md.

Sauber: 81 Zeilen ohne Befund (alle 91 Lösungen rechnen richtig,
kein pruef-Feld weicht ab, alle Grafiken bauen; die zehn Befunde
sind ein fehlendes Sprossenmerkmal, ein Buchstabe doppelt, drei
Sperre- bzw. Sperre-nahe Zahlen aus dem Merkkasten, eine
Zahlen-Dublette, eine nicht prüfbare Antwort, eine Grafik über das
genannte Intervall hinaus und eine Zone-Zeile, die die Vorstufe
wiederholt. Nicht gezählt, nur zur Kenntnis: die Form $c - e^{-x}$
auf $[0;\, \infty[$ trägt drei Zeilen (e1-k1-s2-v2, e1-k3-s1-v2,
zone-f2-v6) und $e^x + c$ fünf; der Punkt (2 | 5) steht in
zone-f3-v1, e2-k1-s0-v1 und e2-k2-s1-v2 – jeweils andere
Handgriffe, keine Dubletten.)

## Abgleich mit gegenlese.md

Befundzeilen: Erstleser 17 (91 − 74), Zweitleser 10; gemeinsam 7,
nur Erstleser 10, nur Zweitleser 3.

Beide haben: e2-k1-s3-v1 (Berührpunkt Q$(2\,\mathrm{ln}\,3 \,|\, 0)$,
gleiche Zahlen), e1-k1-s4-v1 und v2 (h doppelt, beide schlagen k
vor), e1-k1-s2-v3 (kein Grenzwert; Erstleser $\frac{1}{x} + 1$ auf
$[1;\, \infty[$ → $]1;\, 2]$, ich $1 + \frac{4}{x}$ → $]1;\, 5]$,
beides trägt), zone-f5-v4 (Vorstufe vorweggenommen), e2-k2-s1-v2
(Steigung 4 → 1/4 aus dem Kasten, Muster nicht aus der Mappe),
e2-k2-s1-v3 (Punkte A(0 | 4), B(1 | 7) doppelt mit e2-k1-s4-v1).

Nur der Erstleser, mit meinem Urteil:
- e2-k1-s4-v2 (Begründungssatz zum Trapez fehlt in der Lösung):
  zutreffend, übersehen.
- e2-k1-s3-v3 (Steigung −2: Lösung „nur dieses Spiegelbild berührt"
  zu stark, Frage „Muss sie …?"): zutreffend – die Gerade kann g
  anderswo berühren; der zweite Einwand (Gegenfall ändert das
  Merkmal) ist Ermessen, ein Gegenfall unter drei Begründen-Zeilen
  ist vertretbar.
- e1-k1-s3-v3 („Bestimme" statt „weise nach", kein Faktor vor dem
  ln): zutreffend, ich hatte es als Zahlenvariante durchgehen
  lassen; v3 liegt so nur einen Faktor über s1-v4.
- e1-k3-s3-v1, v2, v3 (sprosse_text verlangt den Definitionsbereich,
  keine Variante fragt ihn): zutreffend, kleiner Zusatz je Zeile.
- e2-k2-s3-v1, v2 („Tage je Zentimeter" als eingekleideter
  Kehrwert): zutreffend nach bank.md „eine eingekleidete Rechnung
  ist keine Anwendung"; v3 (Wechselkurs) hält.
- zone-f5-v5 (Steigung −1 in sich = e2-k1-s0-v3): zutreffend,
  dieselbe Erkenntnis in anderer Form; ich hatte nur v4 gezählt.
  Der Vorschlag des Erstlesers (Steigung über das Umstellen nach x)
  nimmt der Zone die Spiegelfrage ganz und ist besser als meine
  Bruchsteigung.
- e1-k3-s1-v3 (Pauls „Fehler" ist keiner): zutreffend – $g(y) =
  \frac{y}{4} + 2$ mit y nach rechts ist der richtige Graph; ich
  hatte es als Schreibweisen-Fehler angenommen. Die Fassung des
  Erstlesers (Paul zeichnet $x = \frac{y}{4} + 2$ ins xy-System und
  erhält f) trägt das Muster „Variablen nicht getauscht" wirklich.

Nur ich: e1-k1-s0-v4 (Graph über das genannte Intervall hinaus
gezeichnet, am Render gesehen), e1-k3-s1-v1 ($]-2;\, \infty[$ ist
das Kastenergebnis), e2-k2-s4-v2 ($x^2$/$\sqrt{x}$ aus dem Kasten).

Widerspruch: e2-k2-s4-v2 – der Erstleser lässt $x^2$ als
Grundfunktion nur in der Grafik ausdrücklich durch, ich sperre sie
als wörtliche Kastenfunktion; da der Term nur im Feld grafik steht
und der Schüler allein den Graphen sieht, hat der Erstleser das
bessere Argument, mein Befund ist Ermessen und kann fallen.

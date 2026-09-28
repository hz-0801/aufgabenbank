# Zweitlesung lineare-funktionen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 306
(zone 26, e1 45, e2 82, e3 58, e4 41, e5 54)

Prüfung: Jede Zeile gelesen (Aufgabe, Antwortgerüst, Lösung, pruef, Grafik, sprosse_text, merkmal). Nachgerechnet mit sympy (Skript im Scratchpad): alle Nullstellen und Argumente (e3), Funktionswerte mit Bruch-m, die beiden Gerade-Parabel-Schnitte (e3-k2-s7-v7/v8, zweiter Schnitt jeweils außerhalb des Bildes), alle 18 Zweipunkt- bzw. Messwert-Gleichungen (e4), die drei Schnittpunkte (e4-k3), alle Tarif-, Endwert- und Mindestzahl-Rechnungen (e5); die einfachen Einsetz-, Tabellen- und Ableseaufgaben im Kopf, Grafiken gegen die Werte (Gitterpunkte, Achsenbereich, Lage der Punkte). Alle 306 Lösungen stimmen mit der eigenen Rechnung; jede pruef-Zahl steht an der Ergebnisstelle, Rundungen (19,1 → 20 Monate, 12,1 → 13 Monate, 221,05 → höchstens 221 km) sind richtig gerichtet. Ankreuzzeilen (20: e2-k2-s0 ×4, e2-k5-s5 ×3, e2-k5-s6-v5/v6/v9/v10, e3-k2-s7-v13 bis v16, e5-k1-s1 ×5) Option für Option geprüft: jede hat genau die geforderte Zahl richtiger Optionen (e3-k2-s7-v13/v14 verlangen wie das Original 2021-OS-K2b zwei). Fehler-finden-Zeilen (19: zone-f3-v5, e1-k1-s7 ×3, e1-k3-s1 ×3, e2-k7-s1 ×3, e3-k5-s1 ×3, e4-k4-s1 ×3, e5-k4-s1 ×3): jeder eingebaute Fehler ist wirklich falsch, jede Richtigrechnung stimmt. Zusätzlich die Funktionen aus grafik und loesung gegen Merkkasten, Typische Fehler und Originale der Mappe abgeglichen (bank-pruef.py prüft die Sperre nur in aufgabe). `python3 werkzeuge/bank-pruef.py lineare-funktionen`: Abweichungen 0, Warnungen 0.

## Befunde

e3-k2-s7-v14: [A] Die Lösung nennt die zweite richtige Option nicht wortgleich („die Aussage zum Punkt R“) – schreiben: „Die Gerade f fällt.“ und „Der Punkt $R(2|3)$ liegt auf der Geraden f.“

e1-k3-s4-v3: [M] merkmal „Anwendung mit Entscheidung im Sachkontext“, die Aufgabe fragt aber nur nach der Dauer (x zum Wert, keine Entscheidung; v1/v2 entscheiden ja/nein) – als Entscheidung fassen, z. B. „Ist die Wanne nach 12 Minuten voll?“ (Nein, 144 l).

e3-k3-s1-v3: [M] merkmal „Wertetabelle mit Bruch- oder Dezimalsteigung und negativen x“, aber $f(x) = -3x + 7$ hat eine ganzzahlige Steigung – Steigung als Dezimalzahl oder Bruch wählen, z. B. $f(x) = -2{,}5x + 4$ zu $x = -2, 0, 2$.

Sauber: 303 Zeilen ohne Befund

### Weitere Hinweise (kein Kennzeichen, nicht gezählt)

Sperre, nur in grafik oder loesung und deshalb vom Prüfskript nicht gesehen – die gezeichnete Gerade ist eine Funktion aus einem Original der Mappe; Vorschlag jeweils: n oder m um eins verschieben.
e2-k5-s2-v2, e2-k5-s6-v3 (Distraktor g), e4-k1-s1-v3 (auch in loesung „f(x) = 3x + 1“), e5-k2-s1-v3 (Distraktor A): $y = 3x + 1$ aus 2021-OS-K2a/K2b.
e2-k5-s2-v3: $y = x + 2$ (g aus 2019-OS-K2a/K2c).
e2-k5-s4-v1: $y = \frac{1}{2}x + 1$ aus 2017-OS-K5a/K5b.
e2-k7-s1-v3: $y = 0{,}5x - 1$ aus 2024-OS-B1i, dazu dieselben Punkte (0|−1) und (2|0), die dort die Fehlerquelle sind.
e3-k5-s3-v2: $y = -2x + 3$ aus 2022-OS-K3a.
e2-k5-s6-v5 (Gerade g), e3-k2-s7-v6: $y = -\frac{1}{2}x + 2$ aus der Auswahlliste von 2019-OS-K2c.
e2-k5-s6-v8: $y = -1{,}5x + 3$ steht sogar im Aufgabentext; es ist die Ergebnisgleichung von 2025-OS-K5a (die Mappe führt sie nur in der Zielmarke, daher schlägt das Prüfskript nicht an).

Verfremdung knapp: e2-k5-s6-v4 behält die Eigenschaft „Anstieg −2“ des Originals 2019-OS-K2b (einzige Zahl der Aufgabe); e4-k1-s6-v1 behält m = −1,5, den Punkt mit x = −2 und das Wahrheitsmuster (falsch, wahr) von 2025-OS-K5a.

Prüfungshöhen bündeln alle Originale der Einheit unter einer Sprosse, deren sprosse_text nur zu einem Teil passt (Katalogbefund, keine Zeilenfrage): e2-k4-s8 „m Bruch und n negativ“ – keine der 8 Varianten hat ein Bruch-m, v1/v5/v7 haben n positiv (die Originale 2026-FOR-K5a, 2024-OS-K3a, 2022-OS-K3a, 2021-OS-K2a sind ganzzahlig); e2-k5-s6 „unter vier Geraden die richtige“ – nur v9/v10 zeigen vier Graphen; e3-k2-s7 „Punktprobe mit Bruch-m“ – nur v11/v12; e4-k1-s6 „zwei Punkte mit Bruch-m“ – v3/v4 ganzzahlig; e5-k1-s5 „ab wann günstiger“ – keine Variante fragt die Grenze direkt. Das merkmal „Merkmale der Kette kombiniert“ bzw. „Geraden Gleichungen zuordnen“ trägt diese Mischung nicht.

## Abgleich

Beide Leser: e3-k2-s7-v14 – die Lösung nennt die zweite richtige Option nicht wortgleich. e3-k3-s1-v3 – ganzzahlige Steigung trotz merkmal „Bruch- oder Dezimalsteigung“. e2-k4-s8-v1 bis v8 und e2-k5-s6-v1 bis v10 – sprosse_text bzw. merkmal der Prüfungshöhe passt nicht zu den Varianten (Katalogbefund); der Erstleser zählt das je Zeile, ich habe es als Strukturhinweis ohne Zählung geführt und dazu e3-k2-s7, e4-k1-s6 und e5-k1-s5 genannt. e2-k5-s6-v1 und e5-k2-s1-v3 – beide Leser haben dort eine Sperre bemerkt, aber verschiedene Funktionen (siehe unten).

Nur Erstleser:
e2-k5-s5-v1 bis v3 (pruef bei Gleichungsoptionen): bestätigt – bank.md verlangt bei Nicht-Zahl-Optionen pruef "", die Lösung selbst stimmt.
zone-f6-v4 (pruef nur [-5]): bestätigt, rein formal – die 7 der Lösung fehlt, f6-v3 führt beide Zahlen.
e2-k3-s0-v1 bis v4 (Steigungsdreieck beschriftet): bestätigt – mathblatt.sty setzt die Höhe #3 als Beschriftung an die senkrechte Kathete, die gesuchte Zahl steht also im Bild; das habe ich übersehen.
e2-k5-s4-v1 bis v3 („bis du wieder auf einer Gitterlinie bist“): bestätigt – gemeint ist ein Gitterpunkt (Kästchenecke) auf der Geraden, nach einem Schritt steht man schon auf einer Gitterlinie.
e2-k7-s3-v1, e4-k1-s1-v1 bis v5, e4-k4-s3-v1 (Gerade g, Antwortgerüst f(x)): bestätigt – f ist dort nicht eingeführt; leicht zu heilen mit „g(x) = __“.
e5-k1-s4-v1, e5-k1-s4-v3, e5-k4-s2-v1, e5-k4-s2-v2 (Tarif/Studio A/B neben Graphen A–D der Einheit): bestätigt nach bank.md („ein Buchstabe je Einheit für eine Sache“), im Blatt geringes Risiko, weil die Zeilen selten auf demselben Blatt stehen.
e5-k2-s1-v3 (A = 3x + 1 und B = 3x bei ystep 5 kaum unterscheidbar): bestätigt – der Abstand ist 1/40 der Bildhöhe; zugleich ist 3x + 1 gesperrt (2021-OS-K2a), der Vorschlag \gerade{3}{5}{A} heilt beides.
e2-k5-s6-v1 (Distraktor y = 2x − 3 aus dem Katalogbeispiel des Erkennungsschritts): bestätigt, und weiter als gemeldet – dieselbe Gerade 2x − 3 zeichnen e2-k5-s2-v1, e2-k5-s6-v6 (Gerade g) und e4-k1-s1-v1, die Gerade −x + 4 aus demselben Beispiel e4-k1-s1-v2; das Prüfskript sieht Erkennungsschritt-Beispiele und Grafiken nicht.
e3-k2-s4-v3 (Bruch-m in einer Sprosse mit sonst ganzzahligem m): bestätigt – die Variante ändert mehr als die Zahlen.
e3-k5-s4-v2 (Nullstelle-Sprosse, Lösung über f(700)): bestätigt, schwach – die Frage ist über die Nullstelle (750 km) wie über f(700) lösbar; ich hatte das als zulässig gewertet, der Vorschlag macht die Sprosse eindeutig.
e4-k1-s3-v3 (negative Steigung vor der Sprosse „negative Steigung“): bestätigt – v1/v2 steigen, v3 nimmt das Merkmal von s5 vorweg.
e3-k5-s1-v2, e3-k5-s1-v3 (Fehlermuster nicht aus „Typische Fehler“): bestätigt – Vorzeichenregel und „mal statt geteilt“ stehen dort nicht; Rechnungen richtig.

Nur Zweitleser:
e1-k3-s4-v3 – merkmal verlangt eine Entscheidung, die Aufgabe fragt nur nach der Dauer.
Sperre in grafik/loesung (nicht gezählt): e2-k5-s2-v2, e2-k5-s6-v3, e4-k1-s1-v3 (3x + 1), e2-k5-s2-v3 (x + 2), e2-k5-s4-v1 (½x + 1), e2-k7-s1-v3 (0,5x − 1 mit den Fehlerquellen-Punkten von 2024-OS-B1i), e3-k5-s3-v2 (−2x + 3), e2-k5-s6-v5 und e3-k2-s7-v6 (−½x + 2), e2-k5-s6-v8 (−1,5x + 3 im Aufgabentext, Ergebnis von 2025-OS-K5a).
Verfremdung knapp (nicht gezählt): e2-k5-s6-v4 (Anstieg −2 wie 2019-OS-K2b), e4-k1-s6-v1 (m = −1,5 und Wahrheitsmuster wie 2025-OS-K5a).

Widersprüche: keine in der Sache. Unterschied nur in der Zählung: Der Erstleser zählt die Prüfungshöhen-Befunde (18 Zeilen) je Zeile, ich führe sie als einen Katalogbefund; beide halten die Rechnungen aller 306 Zeilen für richtig.

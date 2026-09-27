# Gegenlese – strahlensaetze

Datum: 2026-09-27 21:50 UTC
Modell: claude-opus-5-5
Geprüfte Zeilen: 226
Korrekturen: 0

## Entscheidungen

- Befunde stehen je Prüfpunkt unter einer Überschrift, eine Zeile je id; derselbe
  Befund an mehreren Zeilen steht je id einmal.
- Korrekturen stehen unter Punkt 1 mit „korrigiert:“ statt eines Vorschlags.
- Alle Zahlen wurden unabhängig nachgerechnet (Skripte check.py, geo.py, ss.py im
  Scratch-Ordner strahlensaetze/): Lösungszahlen, Bildpunkte der Streckungen in e2,
  Zentren aus Original und Bild, Verhältnisse der \strahlensatz-Grafiken. Keine Lösung
  ist rechnerisch falsch, daher keine Korrektur.
- Größe eines leeren ksys: eine Einheit ist ein Karo à 8 mm (_bausteine.md,
  „Zeichenfläche (Karo 8 mm)“). Ein Feld 10 × 6 ist also 8 cm × 4,8 cm. Zeichenaufgaben
  in cm werden daran gemessen; Befund, wenn die verlangte Zeichnung nicht hineinpasst.
- \strahlensatz{ZA}{ZA′}{Winkel} zeichnet in cm (_bausteine.md). Eine Grafik, die die
  Textmaße im selben Verhältnis verkleinert, gilt als widerspruchsfrei (kein Befund, auch
  ohne „nicht maßstabsgerecht“); Befund nur bei anderem Verhältnis ZA′ : ZA als im Text.
  Lösungsskizzen (loesungsgrafik) zu „Fertige eine Skizze an“ müssen nicht maßstäblich
  sein.
- Nicht prüfbar aus _bausteine.md und daher kein Befund je Zeile: die
  Standardbeschriftung von \strahlensatz ohne punkte= (stehen dort Z, A, A′, B, B′, wie
  die Texte voraussetzen?) und ob die Parallelen bei Baum-/Schattenaufgaben senkrecht
  auf dem ersten Strahl stehen. Beides beim Zusammenbau ansehen (stand.md, Offene Punkte).
- Ein Zahlensatz, der in einer Rechenaufgabe und in einer Fehler-finden-Aufgabe mit
  demselben Ergebnis steht, gilt als doppelte Aufgabe; Befund unter 6.

## 1 Lösung und pruef

- keine

## 2 Eindeutig lösbar

- strahlensaetze-zone-f5-v4: Kreis mit d = 7 cm passt nicht ins Feld ksys 9 × 6
  (7,2 cm × 4,8 cm; auch bei 1 cm je Karo nur 6 cm hoch) – Feld mindestens 10 × 10 Karo.
- strahlensaetze-e1-k3-s4-v1: Kreis d = 6 cm, Feld ksys 10 × 6 ist nur 4,8 cm hoch –
  ymax ≥ 8.
- strahlensaetze-e1-k3-s4-v2: Kreis d = 7 cm, Feld 10 × 6 (4,8 cm hoch, auch bei 1 cm je
  Karo nur 6 cm) – ymax ≥ 9.
- strahlensaetze-e1-k3-s4-v3: Kreis d = 5 cm, Feld 10 × 6 ist 4,8 cm hoch – ymax ≥ 7.
- strahlensaetze-e1-k3-s6-v1: Quadrat 6 cm passt nicht in Feld 10 × 6 (8 × 4,8 cm) –
  ymax ≥ 8.
- strahlensaetze-e1-k3-s6-v2: Rechteck 8 cm × 5 cm passt nicht in Feld 10 × 6
  (8 × 4,8 cm) – xmax ≥ 11, ymax ≥ 7.
- strahlensaetze-e1-k3-s7-v1: Text nennt Zeichenfeld 15 cm × 9 cm, grafik ist ksys
  10 × 6 (8 × 4,8 cm); Musterlösung 10 × 5 cm passt nicht hinein – ksys auf 15 × 9 cm
  (etwa xmax = 19, ymax = 11) oder Feldmaße im Text an die Grafik anpassen.
- strahlensaetze-e1-k3-s7-v2: dasselbe; Musterlösung 8 × 4 cm liegt randgenau im Feld
  8 × 4,8 cm, Text sagt 15 × 9 cm – Feld und Text angleichen.
- strahlensaetze-e1-k3-s7-v3: dasselbe; Musterlösung 14 × 8 cm passt nicht in 8 × 4,8 cm
  – Feld und Text angleichen.
- strahlensaetze-e3-k1-s1-v2: Grafik \strahlensatz{2}{7}: ZA′ : ZA = 3,5, Text 8 : 2 = 4
  – grafik {2}{8}{35}.
- strahlensaetze-e3-k1-s1-v3: Grafik {3}{7}: Verhältnis 2,33, Text 15 : 5 = 3 – grafik
  z. B. {2}{6}{35}.
- strahlensaetze-e3-k1-s1-v4: Grafik {3}{7}: Verhältnis 2,33, Text 9 : 3 = 3 – grafik
  {3}{9}{35} oder {2}{6}{35}.
- strahlensaetze-e3-k1-s1-v5: Grafik {3}{7}: Verhältnis 2,33, Text 16 : 4 = 4 – grafik
  z. B. {2}{8}{35}.
- strahlensaetze-e3-k1-s8-v2: „In einer V-Figur“ setzt nach dem Merkkasten Parallelen
  voraus, die Antwort ist aber „nicht parallel“ – „Zwei Geraden schneiden sich in Z;
  A, A′ liegen auf der einen, B, B′ auf der anderen“.
- strahlensaetze-e3-k2-s1-v2: „In einer V-Figur“ widerspricht der Antwort „nein“
  (V-Figur heißt schon: Parallelen) – Formulierung wie bei e3-k1-s8-v2.
- strahlensaetze-e3-k3-s1-v1: 7 : 3 ist periodisch, die Aufgabe trägt keinen Hinweis und
  keine Rundungsangabe – „auf Millimeter gerundet“ ergänzen.
- strahlensaetze-e3-k3-s1-v3: Strecke 11 cm plus Hilfsstrahl passt nicht in ksys 12 × 6
  (9,6 cm breit) – xmax ≥ 15.
- strahlensaetze-e3-k4-s2-v2: Die Aufgabe sagt nicht, dass Stab- und Baumschatten am
  selben Punkt enden; die Lösung setzt das voraus – Kern um „die Sonnenstrahlen sind
  parallel (gleiche Winkel)“ ergänzen oder das gemeinsame Schattenende in die Aufgabe.
- strahlensaetze-e3-k4-s3-v3: „Wand 2 m hinter der Lampe“ ist unmöglich (der Schatten
  fällt hinter die Figur); gelesen als „2 m hinter der Figur“ ergäbe 48 cm statt 40 cm –
  „Die Wand ist 2 m von der Lampe entfernt, die Figur steht dazwischen“.

## 3 Sprosse und Merkmal

- strahlensaetze-e1-k1-s0-v1: Sprosse verlangt bei verschiedenen Einheiten, die
  umzurechnende Einheit einzukreisen; die Aufgabe fragt nur „gleiche Einheit?“ –
  „… sonst kreise die Einheit ein, die du umrechnen musst“ ergänzen.
- strahlensaetze-e1-k1-s0-v3: dasselbe (km gegen cm, Einkreisen fehlt).
- strahlensaetze-e2-k1-s5-v3: Merkmal „Eigenschaften prüfen statt rechnen“, die Aufgabe
  verlangt aber drei Seitenverhältnisse (2; 2; 2,25) – das ist s7 (Seiten paaren,
  Verhältnis prüfen); Aussage zu Winkeln oder Parallelität wählen.
- strahlensaetze-e3-k1-s2-v3: Ergebnis 4,8 cm nimmt die Dezimalzahlen von s4 vorweg (v1,
  v2 ganzzahlig) – Zahlen mit ganzzahligem Ergebnis.
- strahlensaetze-e3-k1-s3-v2: Ergebnis 4,8 cm, Dezimalzahl vor s4 – ganzzahliges
  Ergebnis wählen.
- strahlensaetze-e3-k1-s3-v3: gegebenes ZB′ = 4,5 cm, Dezimalzahl vor s4 – ganze Zahlen.

## 4 Schreibform

- keine

## 5 Ankreuzen

- strahlensaetze-e1-k3-s0-v1: „Welcher Maßstab passt?“ – 1 : 1 000 (4 mm × 2 mm) passt
  auch ins Feld, nur winzig – „Welcher Maßstab füllt das Feld gut aus?“
- strahlensaetze-e1-k3-s0-v2: dasselbe, 1 : 500 passt ebenfalls ins Feld.
- strahlensaetze-e1-k3-s0-v3: dasselbe, 1 : 2 000 passt ebenfalls ins Feld.
- strahlensaetze-e1-k3-s0-v4: dasselbe, 1 : 300 passt ebenfalls ins Feld.
- strahlensaetze-e3-k1-s0-v3: Lösung am Namen ablesbar (nur ZA′ beginnt mit Z), die
  Grafik wird nicht gebraucht – Strecken in der Grafik nummerieren oder färben und
  danach fragen.
- strahlensaetze-e3-k1-s0-v4: dasselbe (nur BB′ enthält kein Z).

## 6 Fehler finden

- strahlensaetze-e3-k4-s1-v1: Jans Fehler (AA′ statt ZA′ neben den Parallelen) ist
  derselbe Handgriff wie Mias in v2 (AA′ statt ZA) – Muster „nicht vom Zentrum aus“ in
  einer Gleichung des ersten Strahlensatzes (etwa ZB′ : ZB = AA′ : ZA) zeigen.
- strahlensaetze-e3-k4-s1-v2: Zahlen und Ergebnis wie e3-k1-s2-v2 (ZA = 3, ZA′ = 5,
  AB = 6 → 10 cm) – andere Zahlen.
- strahlensaetze-e3-k4-s1-v3: Zahlen und Ergebnis wie e3-k1-s1-v2 (2, 8, 5 → 20 cm);
  außerdem benennt „ZB′ wird mit 5 malgenommen“ den Fehler falsch – andere Zahlen und
  „Zum Umstellen beide Seiten mal 5 nehmen: ZB′ = 5 · 8 : 2“.

Sauber: 192 Zeilen ohne Befund

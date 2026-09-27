# Gegenlese – symmetrie-abbildungen

Datum: 2026-09-27 21:51 UTC
Modell: claude-opus-5-5
Geprüfte Zeilen: 225
Korrekturen: 0

## Entscheidungen

- Befunde stehen je Prüfpunkt unter einer Überschrift, eine Zeile je id; derselbe
  Befund an mehreren Zeilen steht je id einmal.
- Korrekturen stehen unter Punkt 1 mit „korrigiert:“ statt eines Vorschlags.
- Alle Bildpunkte (Spiegeln, Drehen, Verschieben, Punktspiegeln, Bandornament) sind mit
  einem Skript aus den \punkt-Koordinaten der Grafik neu berechnet und gegen pruef und
  loesung verglichen; Seitenlängen aller \dreieck- und \viereck-Grafiken nachgerechnet.
- Was ein Baustein zeichnet, ist am Quelltext der Vorlage geprüft
  (bau/prozentrechnung/2026-09-27/lernblatt/mathblatt.sty): \drachen beschriftet
  A unten, B rechts, C oben, D links, [diagonalen] setzt dazu e und f; \dreieckrw zeichnet
  das Zeichen für den rechten Winkel bei C selbst; \punkt beschriftet oben rechts, und
  alles im ksys wird am Rand des Achsenbereichs abgeschnitten.
- Beschriftungen, die ein Baustein von sich aus setzt (e, f, α–δ, a–c), sind nur dann
  Befund, wenn sie dem Aufgabentext widersprechen.
- Gleiche Punktnamen für verschiedene Punkte in verschiedenen Zeilen sind kein Befund:
  Das Blatt wählt aus der Bank aus, eine Zeile für sich ist eindeutig.
- e3-k1-s3 (halbe Drehung) und e3-k1-s6 (Figur am Zentrum spiegeln) verlangen dieselbe
  Konstruktion; das ist die Kette des Katalogs, kein Befund der Bank.
- Der Verschiebungspfeil in e3-k1-s1 steht nur als Punktpaar P, Q in der Grafik (die
  Vorlage hat im ksys keinen Pfeilbaustein); der Text erklärt ihn, daher kein Befund.
- Anwendungen nahe an einer eingekleideten Rechnung (e1-k6-s4, e2-k6-s4) sind kein Befund:
  Größen und Frage sind im Kontext sinnvoll.

## 1 Lösung und pruef

keine

## 2 Eindeutig lösbar

- symmetrie-abbildungen-zone-f6-v2: \dreieckrw zeichnet den rechten Winkel bei C schon
  ein, die Aufgabe „Markiere den rechten Winkel“ ist damit vorgelöst – Grafik ohne
  Winkelzeichen, z. B. \dreieck{(0,0)}{(4,0)}{(0,3)}{a}{b}{c}{}{}{}, Lösung „bei A“.
- symmetrie-abbildungen-e2-k2-s4-v3: Grafik \dreieck{(0,0)}{(5,0)}{(1,3)} ist
  gleichschenklig (AB = BC = 5), hat also eine Achse; Text sagt „drei verschieden lange
  Seiten“, Lösung 0 – C z. B. auf (1.5,3) legen (Seiten 5; 4,61; 3,35).
- symmetrie-abbildungen-e2-k2-s10-v1: \drachen beschriftet die lange senkrechte Diagonale
  als AC, der Text nennt AC = 40 cm (die kurze) und BD = 70 cm; dazu stehen e, f an den
  Diagonalen, im Text nicht erklärt – z. B. \drachen[diagonalen={,},punkte={B,C,D,A}]
  (B unten, D oben wie im Original) oder die Zahlen im Text tauschen.
- symmetrie-abbildungen-e2-k2-s10-v2: wie e2-k2-s10-v1: Grafik-AC ist die senkrechte
  4,8, Text AC = 30 cm, BD = 48 cm; e, f unerklärt – Beschriftung wie dort anpassen.
- symmetrie-abbildungen-e2-k3-s6-v3: C(2|8) liegt auf ymax = 8, die Beschriftung „C“
  (oben rechts) wird abgeschnitten, der Bildpunkt C'(8|2) liegt auf dem Rand –
  xmax = 9, ymax = 9.
- symmetrie-abbildungen-e2-k3-s8-v1: ohne Grafik ist offen, an welcher Seite gespiegelt
  wird; liegt ein rechter Winkel an a, entsteht ein Dreieck (vgl. e2-k3-s7-v1), bei
  stumpfem Winkel an a ein konkaves Viereck – „Dreieck mit nur spitzen Winkeln“ ergänzen
  oder Seitenlängen wie in e2-k3-s8-v2 angeben.
- symmetrie-abbildungen-e3-k1-s9-v1: zweite richtige Antwort: die halbe Drehung um eine
  Seitenmitte legt das Parallelogramm auf denselben Nachbarn, im Fischgrätmuster ist es
  eine Spiegelung – Lösung „z. B. Verschiebung“ und die Alternativen nennen.
- symmetrie-abbildungen-e3-k1-s9-v2: Abbildung hängt vom gelegten Parkett ab; legt man
  Dreieck und Spiegelbild zum Drachen zusammen, ist der Nachbar gespiegelt – Lösung als
  Beispiel kennzeichnen oder die Anordnung vorgeben.

## 3 Sprosse und Merkmal

- symmetrie-abbildungen-zone-f3-v4: Fallstrick-Zeile verlangt dasselbe wie die mittlere
  f3-v3 (halbe Einheit links von 0 ablesen), nur die Zahl ist anders – eine Falle, die
  nur die falsche Richtung trifft, z. B. −1,5 eintragen (falsch: zwischen −1 und 0).
- symmetrie-abbildungen-e2-k2-s0-v1: beide „passt die Faltung“-Zeilen (v1, v2) haben die
  Antwort ja; der Nein-Fall, auf den es ankommt (Parallelogramm an der Diagonale), fehlt –
  eine der beiden mit einer Nicht-Achse (z. B. Rechteck mit Diagonale), Antwort nein.
- symmetrie-abbildungen-e2-k2-s0-v2: wie e2-k2-s0-v1 (nur Ja-Fälle).
- symmetrie-abbildungen-e2-k2-s1-v1: dieselbe Figur \drachen{4}{3}{0.3} steht in
  e2-k2-s0-v1 mit eingezeichneter Achse (und fast gleich in e2-k1-s0-v3), die Vorstufe
  verrät die Lösung – andere Maße wählen.
- symmetrie-abbildungen-e2-k2-s1-v3: Aufgabe doppelt: gleiche Grafik \trapez{5}{3}{2.5}
  und gleiche Achse wie e2-k1-s0-v4 – andere Maße wählen.
- symmetrie-abbildungen-e2-k2-s3-v3: gleichseitiges Dreieck hat keine Diagonalen, trägt
  das Merkmal „Diagonalen mitzählen“ nicht und nimmt s6 vorweg (gleiche Frage wie
  e2-k2-s6-v1) – Viereck mit Diagonalachsen, z. B. Quadrat anderer Größe oder Raute.

## 4 Schreibform

- symmetrie-abbildungen-e1-k5-s1-v2: Lösung „5 − (−2) = 7“ setzt Subtraktion negativer
  Zahlen voraus, die weder Zone noch Merkkasten führen; der Typ heißt „abzählen“ –
  „2 bis zur Achse, 5 darüber: 2 + 5 = 7 Kästchen“.
- symmetrie-abbildungen-e1-k5-s1-v3: wie e1-k5-s1-v2: „5 − (−3)“ –
  „3 + 5 = 8 Kästchen“.
- symmetrie-abbildungen-e1-k6-s4-v3: wie e1-k5-s1-v2: „3 − (−4) = 7 Kästchen“ –
  „4 + 3 = 7 Kästchen“, dann 7 · 100 = 700 m.

## 5 Ankreuzen

- symmetrie-abbildungen-zone-f2-v4: Distraktor „die längste Strecke von P zu g“ gibt es
  nicht (absurd), und keine Option nennt senkrecht/schräg, obwohl der Fallstrick die
  schräge Strecke ist – Optionen „die senkrechte Strecke“, „eine schräge Strecke“,
  „die waagerechte Strecke“.

## 6 Fehler finden

keine

Sauber: 207 Zeilen ohne Befund

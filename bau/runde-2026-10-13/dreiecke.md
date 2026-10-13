# Runde 13.10. Schritt B – Kapitel Dreiecke (Agent dreiecke)

Daten: mathe-nachhilfe msa/gliederung/dreiecke.md, msa/mehr-p10/dreiecke.csv,
msa/zuordnung-dreiecke.csv (neu aus zuordnung.py). Alle Originale 2022–2026 auf
dem Blatt, Skizzen als TikZ (`grafik`), Lösungen mit sympy nachgerechnet,
mehr-pruef.py ohne Meldung; Setzer meldet nichts als fehlend.
- Pythagoras (P4Z, 3 S.): neu ’24 · 1f, ’26 · 2c, ’25 · 4a (ohne α). Der Schüler
  entscheidet zuerst Hypotenuse oder Kathete (Leiter: abziehen, Rampe: addieren)
  und sucht in Kegel und Becher das Dreieck (beim Stab der Durchmesser). Endet mit
  dem Becher ’22 · 2c. Anstöße neu: 2.
- sin, cos, tan (GYW, 3 S.): neu ’22 · 5b, ’26 · 4c. Er benennt die Seiten aus
  Sicht von α, wählt sin oder cos an der Leiter, stellt sin α = a : c nach a und
  nach c um (beide Lagen kommen in ’23 · 7b vor). Schlussstufe „Pythagoras oder
  sin, cos, tan?“ mit drei Lagen und ’19 · 2d (BC und β, ungekürzt). Anstöße neu: 4.
- Winkel (T2U, 2 S.): neu ’23 · 2a; ’18 · 4b in den Mehr-Block. Stufen Winkel
  gesucht · gleichschenklig · rechter Winkel; Anstöße 180° im Dreieck und an
  Parallelen, gleiche Winkel → gleiche Seiten, gleiche Katheten → 45°. Neu: 3.
- Sinussatz (LXA, 1 S.): Anstoß dritter Winkel zuerst, dann Paar Seite–
  Gegenwinkel, ohne Zahlen; ’24 · 6d, ’25 · 4c (stumpf) am Ende. Neu: 1.
- Vierecke (22A, 1 S.) und Symmetrie (NUB, 1 S.): ’26 · 1c auf dem Blatt;
  Anstöße „Rechteck und Parallelogramm sind auch Trapeze“, „Diagonale ist keine
  Faltachse“. ’25 · 2a (Drachen) ungekürzt nur auf Symmetrie. Neu: 2.
- Gestrichen: die Hand-Einstiege der freien Blätter (Päckchen, Markieren);
  Stufenname „gemischt, ohne Überschrift“ ist jetzt „erst entscheiden, dann rechnen“.

Nicht gebaut: Gemischt Geometrie (’22 · 5e, ’23 · 2c). Beide stehen gekürzt in
flaechen.csv; mehr-pruef.py will jedes Original genau einmal, der Setzer nimmt
Gemischt-Zeilen aus den Stufen heraus. flaechen.md unverändert.

Wünsche an den Setzer:
1. Eine Zeile an zwei Orten: gekürzt (`*_einheit`) in ihrer Stufe, ungekürzt im
   Gemischt-Abschnitt oder in einer Nebenstufe (’22 · 5e, ’23 · 2c; Rampe ’25 · 4a
   ungekürzt bei „Pythagoras oder sin, cos, tan?“); mehr-pruef.py nachziehen.
2. Formel-Frage nicht bei Symmetrie (kam wegen √ in ’25 · 2a).
3. Schülerfrage-Form antwort mit nur einem Fall: Labels rücken neben den Text
   (GYW Nr. 1 unruhig).

Fragen an den Lehrer: Vierecke hat nur ein junges Original (1 Seite), Symmetrie
zwei – zusammenlegen (Grenze „höchstens vier Originale“)? Ist ’19 · 2d am Ende
von sin, cos, tan recht, solange die Rampe ’25 · 4a dort nicht stehen kann?

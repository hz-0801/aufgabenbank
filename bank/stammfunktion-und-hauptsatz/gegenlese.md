# Gegenlese – stammfunktion-und-hauptsatz

Datum: 2026-09-27 21:51 UTC
Modell: claude-opus-5-5
Geprüfte Zeilen: 150
Korrekturen: 0

## Entscheidungen

- Befunde stehen je Prüfpunkt unter einer Überschrift, eine Zeile je id; derselbe
  Befund an mehreren Zeilen steht je id einmal.
- Korrekturen stehen unter Punkt 1 mit „korrigiert:“ statt eines Vorschlags.
- Jede Lösung ist mit sympy bzw. mpmath nachgerechnet (Skripte zone.py, e1.py … e4.py
  im Scratch-Ordner); alle Zahlen, Terme, Nachweise, Kurvenlängen und Grafikwerte
  stimmen. Daher keine Korrektur.
- Verstöße gegen die Sperre (Funktion aus einem Original) und Überschneidungen zweier
  Zeilen, bei denen eine die Lösung der anderen zeigt, stehen unter 3.
- Offene Aufgaben mit „z. B.“-Lösung (e3 s6 v1–v3: irgendein Grenzenpaar mit
  gleichem f'-Wert) gelten als eindeutig, weil die Aufgabe ausdrücklich ein beliebiges
  passendes Paar verlangt.
- Nicht als Befund gewertet: „auf zwei Stellen“ (e2-k1-s2-v1) als übliche Kurzform für
  zwei Nachkommastellen; F ohne eigene Erklärung in den Fehler-finden-Zeilen der e2,
  weil der Hauptsatz-Kontext F als Stammfunktion festlegt.
- zone-f3-v4 steht unter 1 als Befund ohne Korrektur: die Lösung ist richtig, nur pruef
  fehlt, und welche Zahl eines Terms pruef trägt, ist Ermessen.

## 1 Lösung und pruef

- stammfunktion-und-hauptsatz-zone-f3-v4: pruef ist "", obwohl die Lösung $x^5$ eine
  Ziffer trägt (bank.md: "" nur bei Lösung ohne Ziffer) – pruef 5 setzen.

## 2 Eindeutig lösbar

- stammfunktion-und-hauptsatz-zone-f3-v1: „Welche Funktion hat die Ableitung …?“ legt
  eine einzige Antwort nahe, richtig ist jede Funktion + c – „Gib eine Funktion an,
  deren Ableitung … ist.“
- stammfunktion-und-hauptsatz-zone-f3-v2: wie f3-v1 – „Gib eine Funktion an, …“
- stammfunktion-und-hauptsatz-zone-f3-v3: wie f3-v1 – „Gib eine Funktion an, …“
- stammfunktion-und-hauptsatz-zone-f3-v4: wie f3-v1 – „Gib eine Funktion an, …“
- stammfunktion-und-hauptsatz-zone-f3-v5: wie f3-v1 – „Gib eine Funktion an, …“
- stammfunktion-und-hauptsatz-e2-k1-s2-v2: es fehlt die Angabe, dass die abgegebene
  Energie das Integral der Leistung über die Zeit ist (das Original nennt sie) – Satz
  ergänzen.
- stammfunktion-und-hauptsatz-e2-k2-s1-v3: Startpunkt des Balls fehlt; ab x = 0 ist der
  Weg ≈ 7,24 m, ab dem Boden (x ≈ −1,21) ≈ 9,17 m – „wird bei x = 0 abgeworfen“
  ergänzen.
- stammfunktion-und-hauptsatz-e4-k1-s1-v1: „eine Nullstelle“ lässt auch x = −1 zu
  (J(x) = (x − 2)(x + 1)²/3), die Lösung nennt nur 2 – „die Nullstelle, die ohne
  Rechnung feststeht“ fragen.
- stammfunktion-und-hauptsatz-e4-k1-s1-v2: J hat auch die Nullstelle −5/3 – wie v1
  fragen.
- stammfunktion-und-hauptsatz-e4-k1-s1-v3: J hat auch eine Nullstelle bei x ≈ 1,26
  (e^x = 1 + 2x) – wie v1 fragen.
- stammfunktion-und-hauptsatz-e4-k1-s1-v4: J(x) = −cos(x) − 1 ist auch bei −π, 3π …
  null – wie v1 fragen.
- stammfunktion-und-hauptsatz-e4-k1-s5-v3: D ist über x erklärt, gefragt wird „bei
  t = 4“; x ist nicht erklärt, t steht für zwei Dinge – D(x) mit „x in Stunden nach
  6 Uhr“ erklären und „bei x = 4“ fragen.
- stammfunktion-und-hauptsatz-e4-k1-s5-v4: wie s5-v3 („bei t = 6“) – x erklären,
  „bei x = 6“ fragen.

## 3 Sprosse und Merkmal

- stammfunktion-und-hauptsatz-zone-f1-v2: merkmal „Bruch mal Potenz“, die Aufgabe ist
  eine Bruchaddition; die Rechenart weicht von v1 ab – Aufgabe der Form Bruch mal
  Potenz (etwa 1/2 · 3²) oder merkmal für beide Varianten weiter fassen.
- stammfunktion-und-hauptsatz-zone-f1-v6: merkmal nennt gerade und ungerade Potenz,
  die Aufgabe hat nur ungerade ((−3)³, (−2)³) – eine gerade Potenz einbauen, etwa
  1/4 · (−2)⁴ − (−3)³.
- stammfunktion-und-hauptsatz-e1-k1-s3-v2: F(x) = (x² − 4x + 4)·e^x = (x − 2)²·e^x ist
  die Funktion f_0 aus 2025-bebb-lk-B2.2b (Sperre) – andere Zahlen, etwa
  F(x) = (x² − 6x + 9)·e^x zu f(x) = (x − 1)(x − 3)·e^x.
- stammfunktion-und-hauptsatz-e2-k3-s2-v3: cos über [0; π] ist keine volle Periode, der
  Sprossentext nennt „volle Sinusperiode“ – etwa sin(x) von −π bis π.
- stammfunktion-und-hauptsatz-e3-k1-s0-v4: das Bild zeigt u = −x²/2 + 2 und
  v = −x³/6 + 2x, genau die Lösung von e3-k1-s1-v2 – in einer der beiden Zeilen andere
  Zahlen.
- stammfunktion-und-hauptsatz-e3-k1-s1-v2: die Lösungsgrafik (F durch den Ursprung zu
  f = −x²/2 + 2) steht schon als Bild in e3-k1-s0-v4 – andere Zahlen.

## 4 Schreibform

- stammfunktion-und-hauptsatz-e1-k1-s6-v5: der Weg braucht die Stammfunktion −e^(−x)
  von e^(−x), die keine Sprosse übt (Kasten E1: ganzrational) – die Vorgabe um
  „Eine Stammfunktion von e^(−x) ist −e^(−x).“ ergänzen.

## 5 Ankreuzen

- keine

## 6 Fehler finden

- keine

Sauber: 130 Zeilen ohne Befund

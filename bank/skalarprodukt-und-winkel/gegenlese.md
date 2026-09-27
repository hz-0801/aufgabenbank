# Gegenlese – skalarprodukt-und-winkel

Datum: 2026-09-27 21:50 UTC
Modell: claude-opus-5-5
Geprüfte Zeilen: 155
Korrekturen: 0

## Entscheidungen

- Befunde stehen je Prüfpunkt unter einer Überschrift, eine Zeile je id; derselbe
  Befund an mehreren Zeilen steht je id einmal.
- Korrekturen stehen unter Punkt 1 mit „korrigiert:“ statt eines Vorschlags.
- Alle Rechnungen mit sympy nachgerechnet (Skalarprodukte, Beträge, Winkel, Schnittpunkte
  der Geraden in e2 s5, Kreis- und Trapezprobe, Innenwinkel der Zeltwände direkt über die
  Lote auf die gemeinsame Kante statt über die Normalen). Keine Lösung ist falsch.
- Rundungsketten: loesung und pruef rechnen nach bank.md mit dem ungerundeten
  Zwischenwinkel; das ist richtig. Wo der in der loesung gedruckte gerundete
  Zwischenwinkel eine andere letzte Stelle ergibt, steht ein Hinweis unter 1 (keine
  Korrektur).
- „Einen Normalenvektor angeben“ (zone f2) lässt Vielfache zu; die Lösung nennt den
  abgelesenen Vektor. Das gilt als eindeutig genug, kein Befund.
- $\vec a \circ \vec b + \vec c$ (e1 s0 v4) lese ich nach „Punkt vor Strich“ als
  $(\vec a \circ \vec b) + \vec c$; kein Befund.
- Befunde, deren Ursache der Katalog ist (stand.md, Befunde 4 und 5), stehen trotzdem hier,
  weil sie den Schüler treffen; der Vorschlag nennt dann den Katalog.
- Fehlender Satzpunkt oder überzähliger Punkt mitten im Aufgabensatz zählt unter 2, weil
  er auf dem Blatt steht.

## 1 Lösung und pruef

- skalarprodukt-und-winkel-e3-k1-s4-v1: mit dem gedruckten $\varphi \approx 2{,}9^\circ$
  ergibt $\mathrm{tan}\,\varphi$ 5,1 %, die Lösung sagt 5,0 % – Neigung exakt angeben:
  $\mathrm{tan}\,\varphi = \frac{1}{20} = 5\,\%$ (ohne Umweg über das Gradmaß)
- skalarprodukt-und-winkel-e3-k1-s4-v3: mit gedrucktem $20{,}6^\circ$ ergibt sich 37,6 %,
  die Lösung sagt 37,5 % – exakt $\mathrm{tan}\,\varphi = \frac{3}{8} = 37{,}5\,\%$ angeben
- skalarprodukt-und-winkel-e4-k1-s4-v1: mit gedrucktem $\alpha \approx 73{,}7^\circ$ ergibt
  sich 64,3 m, die Lösung sagt 64,4 m – „mit ungerundetem α“ ergänzen
- skalarprodukt-und-winkel-e4-k1-s4-v2: mit gedrucktem $\alpha \approx 106{,}3^\circ$ ergibt
  sich 92,8 m, die Lösung sagt 92,7 m – „mit ungerundetem α“ ergänzen
- skalarprodukt-und-winkel-e4-k3-s1-v3: mit gedrucktem $\alpha \approx 106{,}3^\circ$ ergibt
  sich 18,6 m, die Lösung sagt 18,5 m – „mit ungerundetem α“ ergänzen

## 2 Eindeutig lösbar

- skalarprodukt-und-winkel-e2-k2-s1-v3: S steht unter den „Grundecken“, ist aber die Spitze
  (z = 6) – „hat die Grundecken K(…) und L(…) und die Spitze S(…)“
- skalarprodukt-und-winkel-e2-k2-s1-v5: S steht unter den „Bodenecken“, ist aber die
  Zeltspitze (z = 6) – „hat die Bodenecken K(…) und L(…) und die Spitze S(…)“
- skalarprodukt-und-winkel-e2-k2-s2-v1: Satzbruch „$D(2 \mid 3 \mid 2)$. ist ein Trapez“ –
  Punkt vor „ist“ streichen
- skalarprodukt-und-winkel-e2-k2-s2-v2: Satzbruch „$T(2 \mid 5 \mid 3)$. ist ein Trapez“ –
  Punkt vor „ist“ streichen
- skalarprodukt-und-winkel-e4-k2-s1-v3: „also parallel zu einer Diagonalen“ folgt nur, wenn
  die Grundseiten parallel zu den Achsen liegen; das steht nicht da – Angabe ergänzen
  („Grundseiten parallel zur x- und y-Achse“) oder „also“ durch „und“ ersetzen

## 3 Sprosse und Merkmal

- skalarprodukt-und-winkel-e1-k1-s0-v3: die Vorstufe prüft schon einen zweistufigen
  Ausdruck $(\vec a \circ \vec b) \cdot \vec c$; damit bringt s2 („verschachtelte Ausdrücke
  von innen nach außen“) nichts Neues – Vorstufe auf eine Rechenart (z. B.
  $r \cdot \vec a$, $\vec a - \vec b$), Verschachtelung erst ab s2
- skalarprodukt-und-winkel-e1-k1-s0-v4: wie v3, $\vec a \circ \vec b + \vec c$ ist schon
  verschachtelt (fast gleich e1-k2-s1-v1) – Vorstufe auf eine Rechenart
- skalarprodukt-und-winkel-e3-k1-s2-v3: F ist die Ebene x = 0, also eine Koordinatenebene;
  das widerspricht dem merkmal „keine davon eine Koordinatenebene“ (die Variante folgt dem
  Original 2024-bebb-gk-B3e) – merkmal der Sprosse anders fassen (etwa „zwei
  Seitenflächen, zweiter Normalenvektor nicht (0 | 0 | 1)“) oder andere Ebene F
- skalarprodukt-und-winkel-e4-k1-s2-v3: der Richtungsvektor steht in der Geradengleichung,
  das merkmal „Richtungsvektor erst bilden“ fehlt; die Aufgabe unterscheidet sich vom
  Grundfall nur im Kontext – Dachkante über zwei Punkte (Traufecke, Spitze) angeben

## 4 Schreibform

- skalarprodukt-und-winkel-e2-k2-s6-v3: Winkel zweier Ebenen über die Normalenvektoren
  (und dass der Innenwinkel der Nebenwinkel des Normalenwinkels ist) bringt erst der
  Merkkasten von e3 – Katalogbefund (stand.md Befund 5); in e2 den Satz „Der Winkel
  zweier Ebenen ist der Winkel ihrer Normalenvektoren“ in die Aufgabe setzen oder den
  Zelt-Teil nur in e3 führen
- skalarprodukt-und-winkel-e2-k2-s6-v4: wie v3 (Normalen-Ansatz aus e3) – wie v3
- skalarprodukt-und-winkel-e3-k1-s0-v2: „Gerade gegen Ebene → Sinus“ setzt die Sinusformel
  aus e4 voraus; in e3 ist sie unbekannt, der Schüler kann nur raten – Katalogbefund
  (Erkennungsschritt „vor Einheit 3 und 4“); in e3 streichen oder als Vorgriff mit
  Hinweis auf das Komplement stellen (e4-k1-s0 fragt dasselbe an der richtigen Stelle)

## 5 Ankreuzen

- skalarprodukt-und-winkel-e4-k1-s0-v3: „Winkel, unter dem ein Lichtstrahl auf eine
  Glasscheibe trifft“ ist in der Physik der Einfallswinkel zum Lot – dann wäre „Kosinus“
  ebenfalls richtig – „Winkel zwischen dem Lichtstrahl und der Scheibe“ schreiben

## 6 Fehler finden

keine

Sauber: 137 Zeilen ohne Befund

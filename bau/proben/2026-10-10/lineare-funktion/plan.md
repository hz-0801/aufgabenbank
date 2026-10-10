# Plan: Lineare Funktion f(x) = m·x + n (lineare Funktionen, Lerneinheit 2), NKP

Bau 10.10.2026 nach `bau/bauauftrag.md`, Standardlage: Klasse 8,
Oberschule, allein; sicher: proportionale Funktion y = m·x (E1, VUC),
Koordinaten in vier Quadranten, Brüche als Anteil. Ziel P10.
Heft höchstens 6 Seiten: Übersicht + vier Abschnitte + Probetest.

## 1 Rückwärts von den Zielaufgaben (P10, Katalog „Zielmarke“)

| Zielaufgabe | braucht |
|---|---|
| Gerade aus der Gleichung zeichnen, auch m negativ (2026-FOR-K5a, 2024-OS-K3a, 2021-OS-K2a) | (0\|n) markieren, Steigungsdreieck 1 nach rechts, m nach oben/unten (A) |
| y-Achsenabschnitt von y = 0,5x − 1 markieren (2024-OS-B1i) | Dezimal- und Bruchsteigung: Nenner nach rechts, Zähler nach oben (B) |
| drei Geraden sechs Gleichungen zuordnen, mit y = −2 (2019-OS-K2c) | n und m am Graphen ablesen, auch Bruch und m = 0; Falle m/n vertauscht (C) |
| Graph nach Eigenschaft wählen: Anstieg −2, parallel zur x-Achse (2019-OS-K2b); fallende Gerade (2016-OS-B1c) | m deuten ohne Zeichnen: steigt, fällt, waagerecht, steiler, parallel (D) |

Darunter liegt überall: m und n in der Gleichung finden → (0|n) →
Steigungsdreieck → Gerade; rückwärts: Gerade → n → Steigungsdreieck → m.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Gerade zeichnen mit n und m | Kern der Einheit; m ganzzahlig, erst positiv, dann negativ |
| B | Steigung als Bruch oder Dezimalzahl | eigener Handgriff (Nenner nach rechts); P10-Zahlen 0,5 und ½ |
| C | Gleichung am Graphen ablesen | Umkehrung von A/B; Ankreuz- und Zuordnungsform der P10 |
| D | Was m und n verraten | ohne Zeichnen deuten; Ankreuz- und Auswahlform der P10 |
| T | Probetest | je Abschnitt eine Rechenart, Ziel verbindet A, C, D |

Ziel je Abschnitt (Modell selbst finden, Antwortform wechselt):
A Liegt P auf der Geraden? (ja/nein) · B Wo schneidet sie die x-Achse?
(Punkt) · C Drei Geraden zuordnen (zuordnen) · D Gleichung einer
Parallelen, schneiden sie sich? (Gleichung + Urteil) · T Ist g steiler
als h? (Vergleich).

## 3 Änderungen gegenüber Katalog und Thema-Weg

- Thema-Weg bleibt; Ergänzung: E2 übt das Steigungsdreieck in beide
  Richtungen (zeichnen A/B, ablesen C) und bereitet mit „Liegt P auf
  der Geraden?“ (A) und „Schnitt mit der x-Achse“ (B) Einheit 3 vor.
- Wertetabelle als Zeichenweg (k4-s1 bis s3) gestrichen: E1 hat sie;
  hier nur n und Steigungsdreieck, wie die P10 es verlangt.
- Fehler finden (k7-s1) gestrichen (Bauauftrag); die Falle m/n
  vertauscht steht als Distraktor in C3, C4, T2 und in der Fehlerliste.
- Sonderfall m = 0 nicht als eigener Schritt: zuerst in C4 (y = −2
  ablesen: 0 nach oben), dann benannt in D.
- Zwei Geraden in einem Koordinatensystem (Päckchen), damit das Heft
  auf 6 Seiten bleibt.

## 4 Feste Zahlen (sympy, `pruef` je Zeile)

A: Bsp 2x − 1; 3x − 1, x + 2; −2x + 4, −x − 1; Ziel −3x + 2, f(2) = −4
→ ja. B: Bsp ⅔x + 1; ½x − 2, −⅔x + 2; 1,5x − 3; Ziel −¾x + 3 → (4|0).
C: Bsp −½x + 2; 2x − 3, −x + 1; ¾x − 1; −2x − 1; Ziel ½x − 1, −x + 3,
y = −2 (Buchstaben A–F statt Nummern, damit bank-pruef die
Zahlen prüft). D: Bsp −2x + 1, 3x + 1, −2x − 4, −4; Päckchen; −3x + 1 steiler
als 2x + 5; a/b/c/d; Ziel 3x + 4, parallel. T: −3x + 4 und ¾x − 2;
⅓x + 2; parallel zu 4x − 1 ist 4x + 3; Ziel g durch (0|5) und
B(2|1): −2x + 5, steiler als 1,5x + 2 (Betrag 2 > 1,5).

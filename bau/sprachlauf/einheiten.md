# Sprachlauf einheiten

Stand 2026-09-28 (Gruppe 4). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 70f059c. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py einheiten`: Abweichungen: 0, Warnungen: 0

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 84 | 3 | 87 |
| e2.jsonl | 55 | 4 | 59 |
| e3.jsonl | 58 | 10 | 68 |
| e4.jsonl | 68 | 6 | 74 |
| zone.jsonl | 45 | 1 | 46 |
| gesamt | 310 | 24 | 334 |

Geänderte Sprossen: 124. Die Beispiele sind je Sprosse
die erste geänderte Zeile, gleichmäßig über die Sprossen verteilt.

## Entscheidungen

- Umrechnen ohne Sachlage einheitlich „Rechne <Wert> in <Einheit> um.“; bei
  Zeiteinheiten mit ausgeschriebener Zieleinheit („in Sekunden“), weil s, h,
  min für schwache Leser weniger sprechend sind als m oder kg.
- Ankreuzen: Frage und „Kreuze an.“ zu einem Satz „Kreuze an, …“ gezogen;
  die Optionen sind wortgleich übernommen.
- Maßstab: „Eine Längeneinheit entspricht …“ bleibt als Satz (das Wort
  Längeneinheit übt die Kette). „Maßstabssatz“ wird „der Satz mit dem
  Maßstab“; „Wirkliche Länge?“ wird „Wie lang ist … in Wirklichkeit?“.
- Klammerlegenden ($x$: …) sind zwei Sätze „Dabei ist $x$ … $f(x)$ ist …“.
- Fehler finden: „<Name> soll … Er/Sie schreibt/rechnet so: … Finde den
  Fehler und rechne richtig.“; „Durchschnittspreis“ wird „mittlerer Preis“.
- Division als Bruch in den Rechnungen der Fehleraufgaben (e4-k1-s9-v3,
  e4-k1-s12) und in zone-f3-v2, zone-f10-v2.
- Originale mit langer Satzkette (FHR 2022/2025, P10 2015/2016) nur in
  Sätze geteilt; Wortlaut und Kennung bleiben. Kurze Originale unverändert.
- Unverändert geblieben sind Zeilen, die schon ganze Sätze mit Bezug hatten
  (z. B. „Gib die Höhe in einer handlicheren Einheit an.“, Originale).

## 10 Beispiele

1. `einheiten-e1-k1-s0-v1` – Repräsentanten zuordnen: welche Größenangabe gehört zu welchem Gegenst

   vorher: Wie hoch ist eine Zimmertür? Kreuze an.\\ \kreuz{$2$ m}\\ \kreuz{$9$ m}\\ \kreuz{$25$ cm}

   nachher: Kreuze an, wie hoch eine Zimmertür ist.\\ \kreuz{$2$ m}\\ \kreuz{$9$ m}\\ \kreuz{$25$ cm}

2. `einheiten-e1-k3-s3-v1` – einen Funktionswert als Höhe in der Wirklichkeit deuten, die Stelle au

   vorher: Ein Ball fliegt auf der Bahn $f(x) = -0{,}25x^2 + 2x + 1{,}5$ ($x$: waagerechter Abstand vom Abwurf in m, $f(x)$: Höhe in m). Ein Zaun steht $3$ m vom Abwurf entfernt. In welcher Höhe fliegt der Ball über den Zaun?

   nachher: Ein Ball fliegt auf der Bahn $f(x) = -0{,}25x^2 + 2x + 1{,}5$. Dabei ist $x$ der waagerechte Abstand vom Abwurf in m. $f(x)$ ist die Höhe in m. Ein Zaun steht $3$ m vom Abwurf entfernt. In welcher Höhe fliegt der Ball über den Zaun?

3. `einheiten-e1-k9-s6-v1` – Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten 

   vorher: Schreibe die Länge aus der Stellenwerttafel als Kommazahl in m und als Angabe in m und cm.

   nachher: Die Stellenwerttafel zeigt eine Länge. Schreibe sie als Kommazahl in m und als Angabe in m und cm.

4. `einheiten-e2-k4-s1-v1` – Fahrplan: nächste Abfahrt, Fahrzeit

   vorher: Mia ist um 7:25 Uhr an der Haltestelle Rathaus. Mit welchem Bus fährt sie, und wie lange braucht sie bis zur Schule?

   nachher: Die Tabelle zeigt den Fahrplan der Busse. Mia ist um 7:25 Uhr an der Haltestelle Rathaus. Mit welchem Bus fährt sie? Wie lange braucht sie bis zur Schule?

5. `einheiten-e3-k1-s8-v1` – Vorsätze als Namen lesen (Vorrat: Nano bis Tera)

   vorher: Was bedeutet „Kilo“ in Kilowatt? Kreuze an.\\ \kreuz{tausend}\\ \kreuz{hundert}\\ \kreuz{ein Tausendstel}

   nachher: Kreuze an, was „Kilo“ im Wort Kilowatt bedeutet.\\ \kreuz{tausend}\\ \kreuz{hundert}\\ \kreuz{ein Tausendstel}

6. `einheiten-e4-k1-s1-v1` – zwei Angaben verschiedener Einheit angleichen und addieren

   vorher: $1{,}4$ km $+ 650$ m – wie viel km?

   nachher: Berechne $1{,}4$ km $+ 650$ m. Gib das Ergebnis in km an.

7. `einheiten-e4-k2-s4-v1` – den Verschnitt zweier Leisten aus einem Ausgangsstück als Anteil in Pr

   vorher: Aus einer $2{,}4$ m langen Latte werden zwei Leisten gesägt, $5$ und $3$ Längeneinheiten lang; eine Längeneinheit entspricht $25$ cm. Wie viel Prozent der Latte sind Verschnitt? (FHR 2022)

   nachher: Aus einer $2{,}4$ m langen Latte werden zwei Leisten gesägt. Sie sind $5$ und $3$ Längeneinheiten lang. Eine Längeneinheit entspricht $25$ cm. Der Rest ist Verschnitt. Wie viel Prozent der Latte sind Verschnitt? (FHR 2022)

8. `einheiten-zone-f2-v3` – Stellenwerttafel lesen und schreiben, Nullen an der richtigen Stelle e

   vorher: $16$ Hundertstel als Dezimalzahl?

   nachher: Schreibe $16$ Hundertstel als Dezimalzahl.

9. `einheiten-zone-f6-v4` – Längen im Koordinatensystem als Differenz von Koordinaten lesen (Absta

   vorher: Schnittstellen bei $x = -1{,}4$ und $x = 2{,}6$ – Abstand?

   nachher: Zwei Schnittstellen liegen bei $x = -1{,}4$ und $x = 2{,}6$. Wie weit liegen sie auseinander?

10. `einheiten-zone-f11-v4` – Fläche eines Rechtecks und eines Dreiecks berechnen (für den Materialb

   vorher: Dreieck, Grundseite $3$ m, Höhe $1{,}2$ m – Fläche?

   nachher: Ein Dreieck hat die Grundseite $3$ m und die Höhe $1{,}2$ m. Berechne seine Fläche.

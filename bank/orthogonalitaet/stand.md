# Stand: orthogonalitaet

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26,
aus dem Kopf der Mappe)
Datum: 2026-09-27 15:45 UTC
Prüfskript: bank-pruef.py v0.5, am Ende 0 Abweichungen, 0 Warnungen

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     26 |        – |        12 |      13 |        – |       1 |
| e1    |     43 |       16 |         5 |       9 |        4 |       9 |
| e2    |     35 |        4 |         5 |      15 |        2 |       9 |
| e3    |     34 |        4 |         5 |      12 |        4 |       9 |
| e4    |     26 |        4 |         5 |       6 |        2 |       9 |
| Summe |    164 |       28 |        32 |      55 |       12 |      37 |

## Originale je Einheit

- E1: 2026MgrundlegendAAGLAA111-a, 2021-be-gk-B3a,
  2021MgrundlegendBAGLAA2WTR1-1a (s2); 2026-bb-gk-A1.5a,
  2026-bb-ea-A1.7a, 2018MgrundlegendAAGLAA22-a (s3);
  2024MerhoehtBAGLAA1WTR-2a (s4); 2018-bb-ea-B3.1b und
  2019MgrundlegendAAGLAA212-a (Prüfung, je 2)
- E2: 2021MgrundlegendAAGLAA112-b (Grundfall); 2024-bebb-gk-A1.2b,
  2021MerhoehtAAGLAA112-b, 2024MgrundlegendBAGLAA2WTR2-1f (s2);
  2023-bebb-lk-B3f, 2023MerhoehtBAGLAA2WTR2-1f (s3);
  2026MerhoehtBAGLAA1WTR-1b, 2026MerhoehtBAGLAA1MMS-1b (s4);
  2026-bb-gk-A1.8a, 2026MgrundlegendAAGLAA221 (s5);
  2021MerhoehtAAGLAA121-b (s6); 2023MerhoehtAAGLAA221 (Prüfung, 2)
- E3: 2022-bebb-lk-A1.5a, 2026-bb-ea-A1.3a, 2018MerhoehtAAGLAA211-b,
  2022MerhoehtAAGLAA211-a, 2026MerhoehtAAGLAA211-a (Grundfall, je 1);
  2020MgrundlegendAAGLAA211-a (s2); 2025-bebb-gk-A1.8a,
  2022-bebb-gk-B3c, 2025MgrundlegendAAGLAA221-a (s3);
  2025-bebb-gk-A1.2b, 2018MerhoehtAAGLAA212-a,
  2025MgrundlegendAAGLAA211-b (s4); 2022-bebb-gk-A1.4c,
  2022MgrundlegendAAGLAA211-c (s5); 2021-be-gk-A1.4c und
  2022MerhoehtAAGLAA213 (Prüfung, je 2)
- E4: 2025MerhoehtBAGLAA2MMS-1e (s2); 2022MerhoehtAAGLAA221-a
  (Prüfung, 2); 2020MgrundlegendBAGLAA2WTR-2 (Typ ohne Kette)

## Prüfskript vor der Korrektur

| Datei | Abw. | Warn. | häufigster Grund |
|-------|-----:|------:|------------------|
| zone  |    2 |     0 | Sperre: Tripel aus der Mappe (2) |
| e1    |    8 |     0 | Sperre: Tripel aus der Mappe (7) |
| e2    |    5 |     0 | Sperre: Tripel aus der Mappe (4) |
| e3    |    2 |     0 | Sperre: Tripel (1), Artefakt „+r·(1“ (1) |
| e4    |    3 |     0 | Sperre Tripel, pruef fehlt, Ergebnisstelle |

Keine Einheit scheiterte zweimal. Die Sperre greift bei diesem
Eintrag auf viele Achsenpunkte ((6|0|0), (0|0|5), (0|4|0) …), weil
die 46 Originale fast alle einfachen Koordinaten belegen.

## Entscheidungen

1. Zone: kette und sprosse_text enden am Gedankenstrich der
   Fertigkeitszeile; Folge nach erster Verwendung (Skalarprodukt,
   Richtungsvektoren: E1; Gleichungen: E2; Kollinearität,
   Normalenvektor: E3; Ähnlichkeit: E4), quelle bleibt die
   Katalogzeile.
2. Zone-Paar in der Fertigkeit „Richtungsvektoren bilden“ zum
   Fallstrick „Start minus Ziel“ (Typische Fehler, falscher Vektor).
3. Drei Erkennungsschritte stehen als eigene Ketten in E1 („Welches
   Paar ist senkrecht“, „Null zeigen oder null setzen“, „Für alle oder
   für eins“); der vierte („Wo sitzt der rechte Winkel?“) ist die
   Vorstufe der E1-Kette und entfällt als eigene Kette. In E2 und E3
   sind die ersten drei wortgleich Vorstufen der Ketten und bleiben
   dort nur als Vorstufe.
4. Originale stehen an der Sprosse, die sie nennt (je eine Zeile);
   Pooldubletten (abi und iqb) tragen je eine eigene Zeile derselben
   Sprosse. Die Prüfungshöhe trägt nur ihre eigenen Originale, je 2
   Zeilen; E1 und E3 haben zwei Prüfungshöhen-Originale, also 4.
5. Prüfkennung: iqb grundlegend, be-gk, bebb-gk, bb-gk als GK; iqb
   erhöht (auch MMS und CAS), bebb-lk, bb-ea als LK.
6. Vektoren und Punkte als $(a | b | c)$ mit einfachem Strich (wie in
   geraden, ebenen), Skalarprodukt mit \circ, Verbindungsvektoren mit
   \overrightarrow; Koordinaten x, y, z statt x1, x2, x3.
7. E4: Der Typ „Gleichung für den Parameter des flächenkleinsten
   Dreiecks begründen“ steht in keiner Sprosse der Kette; er ist Typ
   ohne Kette (k2, 3 Zeilen, hoehe sprosse), eine Zeile mit dem
   Original 2020MgrundlegendBAGLAA2WTR-2.
8. Pflicht: fehler, begruenden und anwendung in allen Einheiten;
   darstellung nirgends, weil kein Typ einen Darstellungswechsel
   trägt.
9. Die Sprossentexte der Prüfungshöhen stehen ohne den Zusatz
   „Prüfungshöhe:“; in E3 sind die beiden Prüfungshöhen-Aufgaben
   („Ebene senkrecht zu zwei Ebenen“, „Mittelsenkrechte“) eine Sprosse
   mit zusammengesetztem sprosse_text.
10. Lösungen der Begründungsaufgaben in E1 s4 und E4 ohne Ziffern,
    damit pruef leer bleiben kann; wo eine Zahl unvermeidlich ist
    (Verhältnis 2 : 1), trägt pruef diese Zahl.

## Befunde

- Katalog: Die Erkennungsschritte (Z. 38–41) sind sämtlich wortgleich
  Vorstufen der Ketten (Z. 96–99); der Katalog führt beide.
- Katalog: 2018MerhoehtBAGLAA2CAS1-1b (Museum, CAS-Fassung) steht in
  Abschnitt 2, aber in keiner Sprosse; es blieb ohne Zeile.
- Katalog: Die Sprossen nennen 2017MgrundlegendAAGLAA211-b und
  2017MgrundlegendAAGLAA22-a nicht, obwohl beide in Abschnitt 2 stehen
  (Nachzug 2026-09-28); sie blieben ohne Zeile.
- Prüfskript: Die Sperre liest aus „x = OP + r · (1; 3; 0)“ den Term
  „+r·(1“ und meldet jede Parameterform mit „+ r · (1 | …“; hier
  umgangen durch Tausch der Spannvektoren.
- Prüfskript: Zahlenpaare mit Semikolon in den Originalen („(3; 5;
  −4)“) werden von der Sperre nicht erfasst; die Sperre greift nur bei
  Tripeln mit senkrechtem Strich. Die Semikolon-Tripel wurden von Hand
  gemieden.
- Gegenprobe Kastenzahlen: einzige mehrstellige Kastenzahl ist 35
  (Z. 56); sie kommt in keiner aufgabe vor, Ist 0.

## Offene Punkte

- Keine Grafik gesetzt (kein ksys3); die Körperaufgaben (Holzkörper,
  Kirchturm, Quader) tragen nur Koordinaten. Beim Zusammenbau
  prüfen, ob eine Skizze nötig ist.
- Die Prüfungshöhe von E4 (Ähnlichkeitsargument) hat pruef „2“ als
  Verhältniszahl; das Prüfskript kann die Begründung nicht messen.

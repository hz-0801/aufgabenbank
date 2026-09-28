# Zweitlesung kurvenuntersuchung

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 335
(zone 29, e1 39, e2 106, e3 63, e4 46, e5 52)

Prüfung: Jede Zeile gelesen. Alle Funktionen mit Extrem-, Sattel- oder
Wendepunkten (rund 90 Terme, ganzrational bis Grad 5, Produkte mit
e-Funktion, ln, sin) mit sympy nachgerechnet: Ableitungen faktorisiert,
Nullstellen von f' und f'', Werte von f, f'', f''' an den Stellen, Rand-
und Probestellenwerte, Differenzfunktionen, Schnittstellen Kosten/Erlös,
Winkel über atan; die übrigen Zeilen (Kopfrechnungen, Ablesen, Deutung)
von Hand. Bei Grafiken Punkte gegen den Funktionsterm und den
Achsenbereich geprüft, bei Lösungsgrafiken den Term gegen die
geforderten Eigenschaften. Alle Zeilen mit pruef-Zahl stimmen mit meiner
Rechnung überein (auch nach Rundung); kein rechnerischer Fehler
gefunden. Ankreuzzeilen (zone 3, e1 9, e2 11, e3 6, e5 4) Option für
Option gegen Text und Grafik geprüft; Fehler-finden-Zeilen (zone 1, je
Einheit 3) auf echten Fehler und vollständige Richtigrechnung geprüft.
Originale stichprobenweise gegen Abschnitt 2 der Mappe auf Verfremdung
gesehen. `bank-pruef.py kurvenuntersuchung`: 0 Abweichungen,
0 Warnungen.

## Befunde

zone-f6-v1, zone-f6-v2, e1-k1-s0-v1, e1-k1-s0-v2, e1-k1-s0-v3,
e1-k1-s0-v4: [A] Die drei Optionen stehen hintereinander in einer Zeile
(`\kreuz{…} \kreuz{…} \kreuz{…}`), bank.md verlangt je `\kreuz` eine
Zeile; inhaltlich richtig. – `\\` vor jedes `\kreuz` setzen.

e1-k1-s1-v1, e1-k1-s1-v2, e1-k1-s1-v3, e1-k1-s1-v4, e1-k1-s1-v5: [E]
Frage und Optionen passen nicht zusammen: gefragt ist „Welches
Vorzeichen hat f'(x) auf dem Intervall?“, angekreuzt wird aber „f
steigt / f fällt“; das Vorzeichen, das die Sprosse zuerst verlangt,
wird nirgends angegeben. – Frage als Zweischritt: „Gib das Vorzeichen
von f'(x) auf […] an und kreuze an:“, antwort „f'(x) __ 0“.

e2-k2-s9-v1, e2-k2-s9-v2, e2-k2-s9-v3: [M] Die Sprosse ist im Katalog
die Prüfungshöhe der Kette „Extrempunkte nachweisen“, steht aber mit
hoehe sprosse; ihre Originale (2023-bebb-lk-A1.2b, fhr 2020-C-1c,
2019-A-1c) stehen nicht in Abschnitt 2 der Mappe, also nach bank.md
hoehe pruefung, original null, 3 Zeilen. Außerdem ändern die Varianten
verschiedene Merkmale: v1 und v2 ln-Funktion, v3 allgemeine Aussage zur
waagerechten Tangente. – hoehe auf pruefung; merkmal so fassen, dass es
beide Teile trägt, oder die Aussagen-Beurteilung als eigene Zeile
ausweisen.

e2-k11-s1-v3: [A] „wahr“ ist nicht gesichert: „keinen weiteren
Extrempunkt“ schließt eine Sattelstelle nicht aus; mit f'(x) =
(x + 1)(x + 0,9)² hat f den Tiefpunkt bei −1 und f'(−0,9) = 0, die
Aussage „f'(−0,9) > 0“ ist dann falsch. – In v1 bis v3 ergänzen: „und
keine weitere Stelle mit waagerechter Tangente“ (wie e1-k1-s4-v2); die
Begründung in v1 („f'(1,9) < 0“) wird damit ebenfalls sauber.

e3-k1-s0-v1, e3-k1-s0-v2: [A] „welcher Nachweis … verlangt oder
möglich ist“ lässt zwei Kreuze zu: in v1 ist bei f'''(1) = 6 auch der
Vorzeichenwechsel von f'' möglich, in v2 ist bei vorgegebener Existenz
auch f''' ≠ 0 möglich. – „oder möglich“ streichen („welcher Nachweis
verlangt ist“, wie e2-k1-s0-v3/v4) oder „am einfachsten“.

e3-k1-s10-v3: [E] Hinweis „eine davon ist ganzzahlig und positiv“ ist
irreführend: alle drei Wendestellen −1, 1, 2 sind ganzzahlig, zwei
davon positiv. Lösbar bleibt es (jede passt für die Polynomdivision). –
„eine davon ist ganzzahlig und größer als 1“ (analog zu v4).

e3-k7-s1-v3: [F] Gefragt sind „die besonderen Punkte“ von
f(x) = 3x⁴ − 8x³ + 6x²; die Richtigrechnung nennt nur S(1 | 1). Es
fehlen der zweite Wendepunkt W(1/3 | 11/27) (f'''(1/3) = −24 ≠ 0) und
der Tiefpunkt T(0 | 0). Der eingebaute Fehler (f'(1) nicht geprüft)
ist echt. – Frage einengen: „Gesucht war die Art des Punkts bei x = 1“.

e3-k7-s2-v3: [E] Die Behauptung „in W am steilsten“ gilt nur, wenn der
Graph in W steigt: bei f(x) = −x³ − 5x (links linksgekrümmt, rechts
rechtsgekrümmt) ist f'(0) = −5 das lokale Maximum von f', daneben ist
der Graph steiler. Die Lösung beweist korrekt „Steigung am größten“,
nicht „am steilsten“. – Aussage auf „hat die Steigung in W ihren
größten Wert“ ändern oder „und steigt in W“ ergänzen.

e3-k7-s3-v3: [E] „ab x = 2, also nach 200 m“: x misst die Draufsicht
in x-Richtung, nicht die gefahrene Strecke, und ein Startpunkt der
Straße ist nicht genannt. – Lösung: „ab der Stelle x = 2 (200 m in
x-Richtung)“, oder im Text Start bei x = 0 und „200 m in x-Richtung“
nennen.

Sauber: 314 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e1-k1-s1-v1 bis v5: Fragesatz nach dem Vorzeichen, Optionen nach
  steigt/fällt.
- e2-k11-s1-v3: Sattelstelle bei −0,9 nicht ausgeschlossen, „wahr“ nicht
  gesichert; beide schlagen den Zusatz „keine weitere Stelle mit
  waagerechter Tangente“ vor.
- e3-k7-s2-v3: „in W am steilsten“ falsch bei fallendem Graphen, gemeint
  ist die größte Steigung.
- e3-k1-s0-v1: „verlangt oder möglich“ lässt zwei Kreuze zu.
- e3-k7-s1-v3: Richtigrechnung zu „die besonderen Punkte“ unvollständig
  (W bei 1/3, T(0 | 0)); beide schlagen vor, die Frage auf x = 1
  einzuengen.

Nur Erstleser:
- e3-k6-s1-v3 („steilste“ → „flachste“, vom Erstleser schon
  korrigiert): bestätigt; die Zeile lag mir bereits korrigiert vor.
- e3-k5-s1-v1 bis v3, pruef gerundet (4.71 usw.): bestätigt; nach
  bank.md gehört der ungerundete Wert in pruef. Von mir übersehen, weil
  das Ergebnis stimmt.
- e4-k4-s1-v2, „ist dort am steilsten“: bestätigt; aus W und f'(1) = 3
  folgt nur ein Extremum von f', es kann ein Minimum sein. Derselbe Fehler
  wie in e3-k7-s2-v3; von mir übersehen.
- e1-k1-s7-v4 und v6, keine Rundungsangabe bei periodischen bzw.
  irrationalen Koordinaten: bestätigt (bank.md: periodische
  Dezimalbrüche tragen einen Hinweis); in v4 steht der Hochpunkt nur
  gerundet.
- e4-k2-s1-v1, Stetigkeit fehlt: bestätigt, aber leicht; ich hatte es
  gesehen und als schulüblich übergangen. Da v2 „stetig“ nennt, ist die
  Ergänzung billig.
- e5-k1-s9-v2, „Zug A“ nicht eingeführt: bestätigt; die Zuordnung
  f ↔ Zug A fehlt im Text.
- e2-k1-s3-v1 bis v3, offene Klammer in sprosse_text: bestätigt (Form);
  die Klammer fehlt im Katalogtext der Mappe, also Katalogbefund.
- e2-k10-s1-v3, anderer Aufgabenumfang als v1/v2 (kein kleinster
  Abstand; der wäre 0 wegen Berührung bei x = 2): bestätigt; das Merkmal
  ist gleich, der Umfang nicht.
- e3-k1-s6-v3, e-Funktion und keine vorgegebenen Koordinaten, nur die
  Stelle: bestätigt; die Sprosse verlangt „den Funktionswert
  bestätigen“, v3 lässt ihn berechnen.
- e3-k1-s9-v3, kein Term: nicht bestätigt; die Sprosse heißt „zweiten
  Wendepunkt über die Punktsymmetrie angeben“, und v3 tut genau das,
  ohne Rechnung, wie es das merkmal sagt. v1/v2 gehen darüber hinaus.
- e3-k1-s10-v3 bis v6, sprosse_text nennt nur den abi-Teil der
  Prüfungshöhe: als Form bestätigt, betrifft aber gleichermaßen
  e1-k1-s7-v3 bis v6 und e2-k1-s10-v3/v4 (die der Erstleser nicht
  nennt); dort steht die fhr-Zielmarke ebenfalls nur im merkmal. Für v5
  und v6 bestätigt ohne Einschränkung: merkmal „fünften Grades“, die
  Funktionen sind vierten Grades.
- e3-k3-s1-v3, einzelner Punkt statt vier Kandidaten: nicht bestätigt;
  der Typ heißt „Punktprobe am Graphen“, v3 ist genau das (fhr
  2023-C-1d), das Merkmal bleibt gleich.
- e4-k1-s8-v3/v4 und e5-k1-s9-v3/v4, sprosse_text passt nur zum ersten
  Teil der Prüfungshöhe bzw. zur Zielmarke nicht: als Form bestätigt,
  gleiches Muster wie oben.
- e1-k1-s7-v3 bis v6, f''-Kriterium in Einheit 1: nicht bestätigt als
  Fehler der Bank; die fhr-Zielmarke des Katalogs verlangt „Monotonie im
  Anschluss an die Extrempunktberechnung“, das Original rechnet über
  f''. Allenfalls Katalogbefund zur Reihenfolge.
- e2-k12-s1-v1, „Linkskrümmung“ vor Einheit 3: nur teilweise bestätigt;
  die Aussage ist richtig, das Wort ist entbehrlich, der Vorschlag
  („nach der hinreichenden Bedingung“) ist besser.

Nur Zweitleser:
- zone-f6-v1/v2, e1-k1-s0-v1 bis v4: Ankreuzoptionen in einer Zeile
  statt je `\kreuz` eine Zeile.
- e2-k2-s9-v1 bis v3: Prüfungshöhe der Kette „Extrempunkte nachweisen“
  steht mit hoehe sprosse (Originale nicht in der Mappe → pruefung,
  original null); v3 ändert ein anderes Merkmal als v1/v2.
- e3-k1-s0-v2: auch hier sind bei „verlangt oder möglich“ zwei Kreuze
  vertretbar (kein Nachweis nötig, f''' ≠ 0 möglich).
- e3-k1-s10-v3: Hinweis „eine davon ist ganzzahlig und positiv“ trifft
  auf zwei der drei Stellen zu.
- e3-k7-s3-v3: „nach 200 m“ verwechselt die x-Koordinate mit der
  gefahrenen Strecke.

Widersprüche:
- e3-k1-s0-v2: Der Erstleser hält nur v1 für mehrdeutig, ich auch v2;
  bei vorgegebener Existenz ist f''' ≠ 0 zwar nicht verlangt, aber
  „möglich“. Mit dem gemeinsamen Vorschlag (Fragesatz ohne „oder
  möglich“) ist die Frage für alle vier Zeilen erledigt.
- Sonst keine: Kein Leser hat eine Zeile für richtig erklärt, die der
  andere rechnerisch für falsch hält. Der Unterschied bei „Sauber“
  (299 gegen 314) kommt aus der Zählung der Form- und Sprossenbefunde,
  nicht aus der Rechnung.

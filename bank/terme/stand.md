# Stand: terme

Katalog-Commit: de503c9cea3976774daeb6c514adb85829d8df2e
(2026-09-25, aus dem Kopf von mappen/terme.md)
Datum: 2026-09-27 (date, UTC)
Prüfskript: werkzeuge/bank-pruef.py v0.2, Endstand 0 Abweichungen,
0 Warnungen in allen Dateien.

## Zahlen je Datei

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      18         0         8       9        0       1
    e1.jsonl        39         0         5      21        4       9
    e2.jsonl        81        12        10      45        2      12
    e3.jsonl        36         4         5      18        0       9
    e4.jsonl        29         0         5      21        0       3

Pflicht je Einheit: e1 fehler 3, darstellung 3, anwendung 3 ·
e2 fehler 3, begruenden 3, darstellung 3, anwendung 3 · e3 fehler 3,
begruenden 3, darstellung 3 · e4 fehler 3 · Zone fehler 1 (Paar).

## Originale je Einheit

- e1: 2023-OS-B1h (2 Zeilen), 2017-OS-B1i (2 Zeilen), beide an der
  Prüfungssprosse der Kette Term aufstellen.
- e2: 2025-GYM-B2a (2 Zeilen), an der Kette Zusammenfassen.
- e3: keins (siehe Entscheidungen); Decke ist die Zielmarke.
- e4: keins (Katalog: kein P10-Original); Decke ist die Zielmarke.

## Prüfskript vor der Korrektur

- zone.jsonl: 4 Abweichungen, 0 Warnungen – merkmal je Sprosse
  uneinheitlich (k1–k4 s1). Eine Korrekturrunde.
- e1.jsonl: 8 Abweichungen, 0 Warnungen – 5× „Lösungszahl in 3 von
  3 Ankreuzoptionen" (k1 s1), 3× „pruef fehlt" (k3, Situation zu
  Term). Eine Korrekturrunde.
- e2.jsonl: 2 Abweichungen, 0 Warnungen – „original fehlt" bei
  hoehe pruefung ohne Original (k5 s7). Eine Korrekturrunde.
  Danach ein Nachtrag (Buchstabe, siehe Entscheidungen), 0/0.
- e3.jsonl: 0 Abweichungen, 0 Warnungen.
- e4.jsonl: 0 Abweichungen, 0 Warnungen.

Keine Einheit ist zweimal gescheitert. Vor jedem Schreiben lief
eine eigene Sperrprobe (Teilzeichenketten aus Kasten, Fehlern,
Originalen, Kettenbeispielen); sie fand in e2 „3x + 4" in
„2x + 3x + 4x" und in e4 „6x + 9" in „3x² + 6x + 9"; beide
Aufgaben vor dem ersten Skriptlauf geändert.

## Entscheidungen

- sprosse_text ist das ganze Segment zwischen zwei Pfeilen der
  Kettenzeile, wortgleich samt Mengenangabe („(4×)"), ohne
  Schlusspunkt. Erkennungsschritte: Zeile bis vor „Vor Einheit".
  Zone: Fertigkeitszeile bis vor dem Gedankenstrich; kette ist
  die Fertigkeit ohne Klammerbeispiel.
- Prüfungssprosse ohne Original (Malnehmen e2, Klammern e3,
  Ausklammern e4): hoehe sprosse, 3 Zeilen, merkmal „Zielmarke
  ohne Original". Grund: Das Skript verlangt bei hoehe pruefung
  ein Original; bank.md kennt nur „2 je Original".
- e2 hat zwei Verfahrensketten (Zusammenfassen k4, Malnehmen k5),
  daher 10 Grundfallzeilen. Das Original 2025-GYM-B2a hängt an
  Zusammenfassen, weil es inhaltlich dorthin gehört, nicht an die
  letzte Kette (2.4 c). Die Pflichtkette heißt Zusammenfassen.
- 2022-GYM-B2b (Zuordnung e3) nicht verfremdet: Verfahren und
  Falle sind die binomische Formel, die dieser Eintrag nicht lehrt
  (→ binomische-formeln.md); eine Verfremdung ohne sie wäre ein
  anderes Verfahren. 2019-GYM-B1f ist keiner Einheit zugeordnet
  und fehlt ebenso.
- e1, Grundfall „passenden Term ankreuzen": Wortterme aus zwei
  Anweisungen mit drei Optionen. Ein Grundfall mit einer Anweisung
  (4x, x + 4, 4 − x) scheitert an der Ankreuzprobe (siehe Befunde).
- e1, Situation zu Term: Aufgabe fragt zusätzlich nach der
  Bedeutung eines Termwerts, damit pruef rechenbar ist.
- Pflichtelemente nach den Typen: e1 ohne begruenden (Typenzeile
  nennt es nicht), Fehler finden mit dem Muster „Punkt vor Strich
  in Termen missachtet" (Zeile 65) am Termwert; darstellung am
  Termbaum (Zeile 6, LISUM „Rechen- und Termbäume"). e3 ohne
  anwendung, darstellung am Flächenbild (Zeile 74, Tabelle als
  Bild). e4 nur fehler, Muster „Vorzeichen verloren" beim
  Ausklammern; die Kettensprosse „Fehler finden: Faktor nur aus
  einem Glied gezogen" bleibt hoehe sprosse in der Kette.
- quelle der Pflichtzeilen: die Typenzeile der Einheit (22–24),
  sonst die Zeile, aus der der sprosse_text stammt.
- pruef bei Termergebnissen: erste Vorzahl oder Zahl nach „=".
  Die Gleichwertigkeit von Aufgabe und Lösungsterm habe ich
  zusätzlich mit einem eigenen Skript geprüft (Einsetzen
  zufälliger Werte, nicht im Repo).
- Zone: sprosse 1 = zwei sehr leichte (hoehe grundfall), 2 =
  mittlere, 3 = Fallstrick (hoehe sprosse); Paar in f1 (sprosse 4
  pflicht fehler, sprosse 5 Rechnung), Fallstrick „minus minus"
  bei negativen Zahlen als häufigster. f3 (Dezimalzahlen, Brüche)
  aufgenommen, weil Zusammenfassen s10 Dezimal-Vorzahlen braucht.
- Buchstaben: reine Terme mit x, y, z, a, b, c (Erkennung auch
  m, k, w, d); Sachaufgaben mit eigenen, im Text erklärten
  Buchstaben, je Einheit einmal belegt (e1 a, b, e, k, p, q, m, n,
  d, t; e2 p, s, n). In e2 stand n zuerst auch in einer
  Vorzahlaufgabe; auf w geändert (Commit „e2 (Buchstabe …)").
- e4 Zielmarke „dreigliedrig mit Zahl- und Variablenfaktor" mit
  zwei Variablen umgesetzt (aus e2 bekannt), nicht mit x³.
- „Scheitert zweimal" gelesen als: zwei Korrekturrunden ohne
  null Abweichungen. Trat nicht ein.

## Befunde

- Prüfskript, Ankreuzprobe: „Lösungszahl in genau einer
  Zahloption" ist bei Termoptionen mit je einer Zahl (4x, x + 4,
  4 − x) nie erfüllbar; Optionen mit mehreren Zahlen werden
  offenbar übergangen. Ein Term-Ankreuzen prüft das Skript damit
  entweder falsch oder gar nicht. Vorschlag: Ankreuzprobe nur für
  reine Zahloptionen, für Termoptionen Gleichwertigkeit prüfen.
- Prüfskript: Bei Termlösungen prüft pruef nur eine Zahl an der
  Ergebnisstelle, nicht, ob der Lösungsterm zur Aufgabe
  gleichwertig ist. Vorschlag: optionales Feld mit Aufgabenterm
  und Lösungsterm, Vergleich durch Einsetzen.
- Auftrag, Gegenprobe: „Zahl der Zeilen mit hoehe grundfall ist 5"
  je Einheit setzt eine Verfahrenskette je Einheit voraus; e2 hat
  zwei (Ist 10). bank.md „Pflichtelemente als eigene Kette mit dem
  Namen der Verfahrenskette" ist bei zwei Ketten nicht eindeutig.
- bank.md: keine Regel für die Prüfungssprosse ohne Original
  (Zielmarke); Vorschlag: „hoehe sprosse, 3 Zeilen".
- Katalog, Zuordnung: 2022-GYM-B2b steht bei Einheit 3, braucht
  aber die binomische Formel (Kl. 8, binomische-formeln.md); für
  diesen Eintrag ist es kein verfremdbares Original.
- Katalog, Kette Ausklammern: Die Zielmarke verlangt einen
  dreigliedrigen Term mit Zahl- und Variablenfaktor; keine Sprosse
  führt den dafür nötigen zweiten Buchstaben oder x³ ein
  (Zwischensprosse fehlt, 2.4 b).
- Katalog, Typen e1: kein Typ Fehler finden, obwohl der
  LISUM-Befund (Zeile 6) Fehlerzeilen ausdrücklich belegt.

## Offene Punkte

- Grundvorstellung (Zeile 70, „Was bedeutet eine Vorzahl vor
  x?", Blatt 0) steht nicht in der Bank: keine Fertigkeitszeile,
  kein Erkennungsschritt. Einordnung klären.
- hoehe der Zonezeilen (grundfall/sprosse) mit den anderen
  Einträgen abgleichen; bank.md legt sie nicht fest.
- Grafiken nicht gerendert (kein LaTeX): \viereck mit Seitenlabels
  wie „x+2", \dreieck mit leeren Winkellabels, \sachtabelle mit
  $\cdot$ und \leerzelle im Kopf, \termbaum mit leeren Knoten.
- Termbaum als Darstellung in e1: klären, ob die Lerngruppe ihn
  kennt; sonst Figur-Aufgaben mit Zeichnen.

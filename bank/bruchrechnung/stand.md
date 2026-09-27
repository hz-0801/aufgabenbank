# Stand: bruchrechnung

Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5
(hz-0801/mathe-nachhilfe, katalog/bruchrechnung.md, laut Kopf der
Mappe mappen/bruchrechnung.md vom 2026-09-26 20:21 UTC)
Datum: 2026-09-27 05:29 UTC
Prüfskript: werkzeuge/bank-pruef.py v0.2, Endstand 0 Abweichungen,
0 Warnungen in allen Dateien.

## Dateien

    Datei       Zeilen  vorstufe grundfall sprosse pruefung pflicht
    zone.jsonl      26         –        12      13        –       1
    e1.jsonl        59        12         5      18       12      12
    e2.jsonl        35         4         5      15        2       9
    e3.jsonl        59         8        10      18       11      12
    e4.jsonl        42         4         5      18        6       9
    e5.jsonl        42         4         5      18        6       9
    gesamt         263

Pflicht je Einheit (fehler/begruenden/anwendung/darstellung):
e1 3/3/3/3 · e2 3/3/3/– · e3 3/3/3/3 · e4 3/3/3/– · e5 3/3/3/–;
Zone: 1 fehler (Zone-Paar).

## Originale je Einheit (je 2 Zeilen, verfremdet)

- e1: 2014-OS-K6c, 2015-OS-K7d, 2020-OS-K6c, 2017-OS-K6b,
  2026-FOR-K6c, 2014-OS-B1d
- e2: 2014-OS-K4d
- e3: 2019-OS-K6c, 2018-OS-K7c, 2019-OS-K6b, 2024-OS-K5c
- e4: 2014-OS-K4c, 2024-OS-K2d, 2023-OS-B1f
- e5: 2021-OS-B1g, 2016-OS-B1i, 2015-OS-K2a

## Prüfskript vor der Korrektur (erster Lauf je Datei)

- zone.jsonl: 0 Abweichungen, 0 Warnungen.
- e1.jsonl: 13 Abweichungen, 0 Warnungen. 7 Zeilen Sperre (Brüche
  2/14, 5/12, 9/10, 1/25, 1/36, 1/10, 9/64 und 1/64 aus Kasten und
  Originalen); 6 Zeilen „nicht an der Ergebnisstelle“ (gemischte
  Zahl ohne unechten Bruch in der Lösung, siehe Befund 2).
- e2.jsonl: 0 Abweichungen, 0 Warnungen.
- e3.jsonl: 8 Abweichungen, 1 Warnung. 4 × „pruef fehlt“
  (Erkennungsschritt „Von heißt mal“); 2 × nacktes % (davon 1 mit
  Sperre „2 · 12“, siehe Befund 3); 2 × „original fehlt“
  (Flaschen-Sprosse als pruefung ohne Original). Warnung: pflicht
  fehler 6×, Menge 3.
- e4.jsonl: 0 Abweichungen, 0 Warnungen.
- e5.jsonl: 1 Abweichung, 0 Warnungen (Sperre „3 · 12“, Befund 3).

Keine Einheit ist zweimal gescheitert; jede war nach einer
Korrektur fehlerfrei.

## Entscheidungen

1. Zone: hoehe „sprosse“ für alle Zeilen außer dem Fehler-finden
   des Zone-Paars (pflicht fehler). sprosse 1 = sehr leicht,
   2 = mittel, 3 = Fallstrick, 4/5 = Zone-Paar. Die Zone-id hat
   keine Sprosse, daher zählt variante je Fertigkeit durch.
   kette und sprosse_text = Fertigkeitszeile bis vor „– Einheit“.
2. Zone-Paar bei „Kürzen und Erweitern“, Fallstrick „nur den
   Nenner erweitert“ (Typische Fehler Z. 83); Einheit 1 und 3
   hängen daran. Je Fertigkeit genau ein Fallstrick.
3. Zone „Schriftliches Rechnen“: Einmaleins und schriftliches
   Addieren/Subtrahieren, keine schriftliche Multiplikation
   (unterrichtsblatt 2.2; siehe Befund 6).
4. Bruchstreifen als `\bruchrechteck{gefüllt}{gesamt}`, Ablesen
   mit form streifenfeld, Einfärben mit form streifenleer und
   loesungsgrafik. Stellenwerttafel als `\sachtabelle` mit
   ausgeschriebenen Stellen (keine unerklärten Buchstaben).
5. Erkennungsschritte: kette = Frage ohne Anführungszeichen,
   sprosse_text = Katalogzeile bis vor „Vor Einheit“. Ja/nein- und
   Wortantworten ohne Ziffern haben pruef leer; bei „Von heißt
   mal“ ist pruef der Bruch der Malaufgabe (das Skript verlangt
   pruef, sobald die Lösung Ziffern hat).
6. Einheit 3 hat zwei Verfahrensketten (Multiplizieren,
   Dividieren). Grundfall je Kette 5 („Mengen je Kette“), also 10
   in e3. Pflichtelemente einmal je Einheit, verteilt nach
   Zugehörigkeit: Multiplizieren fehler 2, anwendung 3,
   darstellung 3; Dividieren fehler 1, begruenden 3.
7. Dividieren: Die Prüfungshöhe hat kein P10-Original (Z. 101,
   Lehrwerksmaßstab). Sie steht als höchste Sprosse (hoehe
   sprosse, 3 Zeilen), weil das Skript bei pruefung ein Original
   verlangt und „2 je Original“ hier 0 ergibt.
8. „(4×)“ im Katalog ist Blattmenge; in der Bank gilt „Grundfall
   5, jede weitere Sprosse 3“, auch für „ein Nenner Vielfaches des
   anderen (4×)“. sprosse_text ohne „(4×)“.
9. Prüfungshöhe mit „daneben …“: eigene Sprosse je Satzteil, je
   Original 2 Zeilen.
10. Wahrscheinlichkeits-Originale als Nebenleistung verfremdet: in
    e1 sind die Pfadwahrscheinlichkeiten gegeben (nur addieren,
    kürzen; Multiplikation kommt erst in Einheit 3); in e3 stellen
    die Schüler die Produkte bei 2019-OS-K6c und 2018-OS-K7c
    selbst auf, damit die Falle „Nenner nicht weiterzählen“
    bleibt.
11. 2021-OS-B1g und 2016-OS-B1i mit positiven Zahlen verfremdet:
    negative Zahlen sind in diesem Eintrag nicht eingeführt, die
    Vorzeichenfalle gehört zu rationale-zahlen.md. Falle hier: die
    Klammer (der Bruchstrich) wird übergangen.
12. Typen ohne Kette: e1 „ganze Zahl plus Bruch“; e2 „ganze Zahl
    plus Dezimalzahl“, „Überschlag vorab“; e5 „Distributivgesetz
    (Ausklammern bei Dezimalzahlen)“, „Überschlag und Prüfen“.
    Sachaufgaben- und Größentypen (e1, e3, e4) sind die Pflicht
    anwendung; e2 anwendung ist die Kassenzettel-Aufgabe mit
    Rückgeld (Z. 99), e3 anwendung enthält „Bruch von Bruch in
    einer Sachaufgabe“ (Z. 100).
13. darstellung nur in e1 (Bruchstreifen, RLP Z. 6) und e3 (Anteil
    am Streifen ↔ Malaufgabe, RLP Z. 6); die Typen von e2, e4, e5
    tragen keinen Darstellungswechsel.
14. anwendung in e5, obwohl die Typen keine Sachaufgabe nennen:
    RLP Z. 6 („Verknüpfen mehrerer Grundrechenoperationen …“) und
    die Prüfungshöhe 2015-OS-K2a verlangen Terme zu Sachtexten.
15. Erkennungsschritt und gleichlautende Vorstufe (e3, e5)
    verschieden umgesetzt: Erkennungsschritt = Malaufgabe
    aufschreiben bzw. erste Rechnung benennen (Brüche,
    Dezimalzahlen); Vorstufe = entscheiden, ob „von“ einen Anteil
    meint, bzw. einkreisen mit natürlichen Zahlen.
16. Gemischte Zahlen stehen in der Lösung zusätzlich als unechter
    Bruch; pruef ist dessen [Zähler, Nenner] (Befund 2).
17. Mehrere Ergebnisse in pruef als Liste, zwei Brüche als Liste
    von Listen ([[1, 13], [2, 91]]).
18. Termprüfung 2015-OS-K2a als ankreuzen mit `\janein` je Term;
    Lösung ohne Ziffern, pruef leer.
19. Dezimalzahlen im Mathemodus als `{,}`, Prozent als `\,\%`.
20. Neben dem Prüfskript (prüft nur, ob pruef in der Lösung steht)
    wurden alle reinen Rechenaufgaben mit Fraction nachgerechnet
    und die Sachaufgaben von Hand; kein Fehler.

## Befunde

1. (erledigt v0.5) bank.md, „Mengen je Kette“ und Gegenprobe im Auftrag: „je
   Einheit genau der Grundfall der Kette 5 Zeilen“ setzt eine
   Verfahrenskette je Einheit voraus. Einheit 3 hat zwei; e3 hat
   daher 10 Grundfallzeilen. bank.md sollte „je Verfahrenskette“
   sagen und festlegen, wie zwei Ketten einer Einheit die
   Pflichtelemente teilen.
2. (erledigt v0.5) Prüfskript: Eine gemischte Zahl `3\frac{3}{5}` wird als Bruch
   33/5 gelesen (Ziffern verkettet). Eine Lösung, die nur die
   gemischte Zahl nennt, scheitert. Umgangen nach Entscheidung 16.
3. (erledigt v0.5) Prüfskript, Sperre: Es verbindet den Nenner eines Bruchs mit
   dem folgenden Faktor (`\frac{1}{12} \cdot 3` → „3 · 12“,
   `\frac{3}{12} \cdot \frac{2}{11}` → „2 · 12“) und meldet ein
   Zahlenpaar aus 2015-OS-K2a. Zu breit.
4. (erledigt v0.5) Prüfskript, Sperre: Jeder einzelne Bruch aus Kasten und
   Originalen mit einer Zahl ab 10 gilt als Zahlenpaar (1/10,
   9/10, 1/36, 5/12 …). bank.md nennt „kleine Grundfallzahlen“
   frei; ob ein Bruch wie 1/10 dazugehört, regelt es nicht.
5. Katalog Z. 86 (und Z. 25): „Zähler geteilt statt Nenner mal“,
   das Beispiel 3/4 : 2 = 3/2 zeigt aber den Nenner geteilt. Den
   Zähler zu teilen ist, wo es aufgeht, richtig (4/5 : 2 = 2/5).
   Die Bank folgt dem Beispiel (Nenner geteilt).
6. Katalog Z. 35 „Schriftliches Rechnen mit natürlichen Zahlen“
   gegen unterrichtsblatt 2.2 „Schriftliche Multiplikation ist
   keine Fertigkeit der Zone“.
7. Katalog: Erkennungsschritt „Von heißt mal“ (Z. 40) und Vorstufe
   „„von“ markieren“ (Z. 100), ebenso „Was rechne ich zuerst?“
   (Z. 42) und „Rechnung einkreisen“ (Z. 103), beschreiben
   denselben Schritt; die Bank führt beide (Entscheidung 15).
   (erledigt v0.5 für „Was rechne ich zuerst?“, siehe
   Nachbesserung; „Von heißt mal“ siehe Befund 9.)
8. (erledigt v0.5) bank.md regelt nicht die Prüfungshöhe ohne P10-Original
   (Z. 101) und nicht die hoehe der Zonenzeilen (Entscheidungen 1
   und 7).
9. Erkennungsschritt „Von heißt mal“ (Z. 40, e3 k1) bleibt stehen:
   Er verlangt „von“ unterstreichen und die Malaufgabe
   aufschreiben, die Vorstufe „„von“ markieren“ (Z. 100) nur das
   Markieren. Der Handgriff überschneidet sich, ist aber nicht
   derselbe; ob bank.md „denselben Handgriff“ so eng meint, ist
   offen. Wird er gestrichen, rücken e3 k2–k5 auf k1–k4.

## Offene Punkte

- Kein LaTeX-Lauf: `\bruchrechteck{0}{n}` (leerer Streifen),
  `\sachtabelle` mit Ziffernzeile und drei `\janein` untereinander
  im Aufgabentext sind ungerendert.
- Gegenprobe e3: 10 statt 5 Grundfallzeilen (Befund 1).
- Die Prüfungshöhen in e1 und e3 setzen Pfadwahrscheinlichkeiten
  voraus, die Klasse 6 nicht kennt; beim Blattbau als Zielmarke
  kennzeichnen oder auslassen.

## Nachbesserung 2026-09-27

Nach bank.md Stand 2026-09-27b und Prüfskript v0.5; vorher
1 Abweichung, 12 Warnungen, danach 0 Abweichungen, 0 Warnungen in
allen Dateien.

- zone.jsonl: Die zwölf sehr leichten Zeilen (sprosse 1) tragen
  hoehe grundfall statt sprosse (Entscheidung 1 überholt).
- e1.jsonl: e1-k5-s1-v2 (Fehler finden) rechnet 1/3 + 1/9 statt
  1/2 + 1/8, weil „1/8 + 1/8“ als Fehlerquelle von 2025-OS-K3d
  gesperrt ist.
- e3.jsonl: Die Prüfungshöhe Dividieren (e3-k3-s5, Z. 101, drei
  Zeilen) trägt hoehe pruefung mit original null statt sprosse
  (Entscheidung 7 überholt).
- e5.jsonl: Der Erkennungsschritt „Was rechne ich zuerst?“ (vier
  Zeilen) ist gestrichen, weil er denselben Handgriff verlangt wie
  die Vorstufe „Rechnung einkreisen“; die Ketten k2–k5 rücken auf
  k1–k4, ids mit (Entscheidung 15 für e5 überholt).
- Tabelle „Dateien“ auf die neuen Zahlen gebracht.

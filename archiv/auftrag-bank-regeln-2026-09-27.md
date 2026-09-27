# Auftrag: Bank-Regeln nachziehen, Prüfskript v0.3

Modell: Opus. Web-Sitzung, Repo aufgabenbank, main. Commit je Teil,
vor jedem Push `git pull --rebase`, main pushen, kein eigener
Branch. Geschrieben wird nur in bank.md, auftrag-eintrag.md,
werkzeuge/bank-pruef.py und in diesen Auftrag (Verschieben am
Ende). Kein Eintrag unter bank/ wird geändert.

## Ausgangslage

Acht Einträge liegen in bank/, sechs davon aus parallelen
Sitzungen vom 27.09. Alle sechs sind an denselben vier Lücken von
bank.md hängen geblieben und haben sie je für sich entschieden;
ihre stand.md nennen außerdem Fehler des Prüfskripts. Vier Regeln
sind entschieden (unten), die Skriptfehler sind belegt. Beides
kommt jetzt in die Regeln und das Skript, bevor 19 weitere
Einträge starten. Die Nachbesserung der acht Einträge ist ein
eigener späterer Auftrag; dieser hier ändert keine Aufgabe.

## Teil 1: bank.md

Vier Regeln, je als Absatz an der genannten Stelle; Wortlaut
sinngemäß so, in der Sprache der Datei, je Zeile höchstens 72
Zeichen. Kopfzeile von bank.md: Stand 2026-09-27, „nach acht
Einträgen".

1. Abschnitt „Mengen je Kette": Der Grundfall (5 Zeilen) gilt je
   Verfahrenskette, nicht je Einheit. Hat eine Einheit zwei
   Verfahrensketten, hat sie zwei Grundfälle. Die Pflichtelemente
   stehen je Einheit einmal; ihre Kette heißt nach der ersten
   Verfahrenskette der Einheit. Den Klammersatz „(nicht grundfall,
   damit je Einheit genau der Grundfall der Kette 5 Zeilen hat)"
   anpassen: „(nicht grundfall; der Grundfall gehört der
   Verfahrenskette)".

2. Abschnitt „Mengen je Kette", nach der Prüfungshöhe: Eine
   Prüfungshöhe ohne P10-Original (Zielmarke aus Rahmenlehrplan
   oder Lehrwerk) trägt hoehe pruefung, original null, 3 Zeilen.
   Bei „Felder je Aufgabe", original: das Feld darf an jeder
   hoehe stehen, wenn die Sprosse ein Original des Katalogs
   verfremdet (P10-Form-Sprossen mitten in der Kette); hoehe
   pruefung bleibt der letzten Sprosse vorbehalten.

3. Abschnitt „Mengen je Kette", beim Erkennungsschritt: Verlangt
   ein Erkennungsschritt denselben Handgriff wie die Vorstufe
   einer Kette derselben Einheit, entfällt der Erkennungsschritt;
   die Vorstufe bleibt. stand.md nennt den Fall unter „Befunde"
   als Katalogbefund (der Katalog führt beide).

4. Abschnitt „Mengen je Kette", Zone: Die zwei sehr leichten
   Zeilen (s1) tragen hoehe grundfall, die mittlere (s2) und jeder
   Fallstrick hoehe sprosse; merkmal jedes Fallstricks beginnt mit
   „Fallstrick:". kette und sprosse_text der Zone sind die
   Fertigkeit bis zum Doppelpunkt; variante zählt je Fertigkeit
   durch (das id-Muster der Zone trägt keine Sprosse).

Dazu zwei Klarstellungen im Abschnitt „Regeln für den Inhalt":
- Ankreuzen: Die loesung nennt die richtige Option wortgleich
  (Zahl, Term oder Gleichung wie in der Option); pruef trägt die
  Zahl, wenn die Optionen Zahlen sind, sonst "".
- Sperre: Ein einzelner Bruch ist kein Zahlenpaar; frei sind
  einzelne Ziffern und Zahlen unter 10.

Commit „bank.md: vier Regeln nach acht Einträgen", push.

## Teil 2: werkzeuge/bank-pruef.py v0.3

Jede Änderung mit einem Fall im Selbsttest (Funktion selbsttest),
je eine Zeile, die vorher falsch lief, und eine, die weiter
richtig läuft.

a) Regel 2: hoehe pruefung mit original null ist erlaubt (kein
   „original fehlt"); original an anderer hoehe ist erlaubt, wenn
   es vollständig ist (id, jahr, papier, Muster wie bisher). Die
   Prüfung „hoehe steigt in der Kette" bleibt. Mengenwarnung:
   Prüfungshöhe ohne Original 3 Zeilen.
b) Regel 4: Zone s1 muss hoehe grundfall haben, s2 und folgende
   hoehe sprosse (Warnung); merkmal einer Zone-Zeile ab s3 beginnt
   mit „Fallstrick:" (Warnung).
c) grafikprobe: Das Wort „Graph" allein verlangt keine Grafik
   mehr. Grafik verlangen: form zeichnen, oder aufgabe enthält
   einen Ablese- oder Zeichenauftrag (Wortstämme lies/ablesen/
   abgelesen, zeichne/eingezeichnet, Abbildung, Bild, „im
   Koordinatensystem" als Ort einer Zeichnung). Probe aus
   lineare-funktionen: „Liegt P auf dem Graphen von f?" ohne
   grafik → OK.
d) ankreuzprobe: Sind mindestens zwei Optionen reine Zahlen, wie
   bisher (Lösungszahl in genau einer). Sonst: nach mathnorm und
   ohne_raum steht genau eine Option wortgleich in loesung; sonst
   Abweichung „Ankreuzlösung nennt keine oder mehrere Optionen".
   Proben aus terme (4x, x + 4, 4 − x) und pythagoras (Formeln
   mit ²).
e) Sperre: Kastenterme ohne Variable mit mindestens zwei Zahlen
   und einem Rechenzeichen (6² + 8²) werden gesperrt; Terme mit
   Variable schon ab einer Zahlbelegung ((x + 3)², −x² + 6x + 7,
   −3x + 1); gemischte Zahl `3\frac{3}{5}` wird als 18/5 gelesen,
   nicht als 33/5; `\frac{1}{12} \cdot 3` verbindet Nenner und
   Faktor nicht zu einem Paar; ein einzelner Bruch ist kein
   Zahlenpaar (Regel oben). Die Ausnahme „Gegenstand der Kette"
   (muster in sprosse_text) bleibt. Proben aus quadratische-
   gleichungen Befund 4, bruchrechnung Befund 2–4, pythagoras
   Befund 2.
f) Ergebnisstelle: „$-\,6$" und „$-\;6$" werden als −6 gelesen;
   in „x^2 - 12x" ist −12 die Zahl; bei pruef "" zählt die 2 in
   x^2 (Exponent nach ^) nicht als Lösungsziffer.
g) Regel 1: Die Warnung „Mengen" prüft den Grundfall je Kette
   (tut sie schon); keine Warnung je Einheit einführen.

Kopf des Skripts: v0.3, Datum aus `date`, die Liste der Änderungen
a–g in einer Zeile je Punkt. Selbsttest laufen lassen; er muss
durchlaufen.

Commit „bank-pruef v0.3: Regeln 2 und 4, Graph, Ankreuzen,
Sperre, Ergebnisstelle", push.

## Teil 3: auftrag-eintrag.md

Die Datei 2 dieses Blocks ersetzt sie wortgleich. Commit
„auftrag-eintrag: Regeln vom 27.09.", push.

## Gegenprobe

`python3 werkzeuge/bank-pruef.py <eintrag>` für alle acht
Einträge, vor und nach Teil 2, Zahlen je Eintrag (Abweichungen,
Warnungen). Erwartung: Die sechs Einträge vom 27.09. bleiben bei
0 Abweichungen, außer neuen Treffern der Sperre (e) und der
Ankreuzprobe (d) – die sind Befund, nicht Fehler des Skripts, und
werden je Eintrag mit Zeilen-id gelistet, nicht behoben.
prozentrechnung und quadratische-funktionen haben vorher 47 und
36 Abweichungen; nachher darf die Zahl nur durch (c), (e), (f)
sinken oder steigen, jede Änderung je Grund gezählt. Das Wort
„Graph" in lineare-funktionen e3 (Punktprobe ohne Grafik) darf
nach (c) keine Abweichung mehr auslösen; Zone lineare-funktionen
darf nach (b) 0 Warnungen haben, die fünf anderen Zonen bekommen
je Fertigkeit zwei Warnungen (s1 nicht grundfall).

## Regeln

- Kein Eintrag unter bank/ wird geändert; jede Abweichung, die
  das neue Skript dort findet, kommt in den Bericht.
- Zeilen in md höchstens 72 Zeichen.
- Was der Auftrag nicht regelt, entscheidest du und schreibst es
  in den Bericht.
- Am Ende diesen Auftrag nach archiv/auftrag-bank-regeln-
  2026-09-27.md verschieben (git mv), Commit „archiv: auftrag-
  bank-regeln", push.

## Bericht

Im Chat, am Ende. Erste Zeile das Modell. Dann: die vier Absätze
aus bank.md wortgleich; je Änderung a–g der Selbsttestfall in
einem Satz; die Gegenprobe als Tabelle (Eintrag, Abweichungen
vorher/nachher, Warnungen vorher/nachher) und darunter je Eintrag
die neuen Treffer der Sperre und der Ankreuzprobe mit Zeilen-id;
Entscheidungen, die der Auftrag offenließ. Letzte Zeile:
„gepusht auf main, Commit <hash>".

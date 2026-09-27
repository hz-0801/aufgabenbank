# Auftrag: Sek II in Skript und bank.md – Prüfskript v0.5

Modell: Opus. Web-Sitzung, Repo aufgabenbank, main. Commit je Teil,
vor jedem Push `git pull --rebase`, `git push origin main`, kein
eigener Branch, kein Pull Request. Geschrieben wird nur in
werkzeuge/bank-pruef.py, bank.md, bank/ableitungsregeln/,
bank/vektoren-und-rechenoperationen/ und in diesen Auftrag
(Verschieben am Ende).

## Ausgangslage

Zwei Sek-II-Prüfsteine liegen in bank/: ableitungsregeln (138
Zeilen, 37 Abweichungen) und vektoren-und-rechenoperationen (134
Zeilen, 0 Abweichungen, 2 Warnungen). Ihre stand.md nennen unter
„Befunde“ dieselben Lücken für Sek II; 41 weitere Sek-II-Einträge
warten. Die Lücken:
- Das Muster KENNUNG in bank-pruef.py kennt nur MSA-, FHR- und
  IQB-Kennungen in Großbuchstaben. Landesabitur (2019-be-gk-A1.1a,
  2018-bb-ea-cas-B2.1e), IQB mit Kleinbuchstaben
  (2021MerhoehtAAnalysis12-a) und Teil-B-Kennungen
  (2017MgrundlegendBAnalysisWTR-1d) fallen durch. ableitungsregeln
  hat die Originale behalten (37 Abweichungen), vektoren hat 14
  Felder original auf null gesetzt.
- Ergebnisstelle und Sperre kennen nur Paare (a | b); Tripel
  (a | b | c) werden nicht gelesen und nicht gesperrt.
- Die Sperre vergleicht x⁴, x⁵ der Mappe nicht mit x^4, x^5 der
  Bank.
- bank.md beschreibt Prüfkennung und Feld original nur für die
  P10. Beide Sitzungen haben dieselbe Sek-II-Form gewählt.

## Teil 1: werkzeuge/bank-pruef.py v0.5

a) Kennung gegen die Mappe statt gegen ein Muster: Ein original
   ist vollständig, wenn id, jahr, papier gesetzt sind, id mit
   jahr beginnt und id in mappen/<eintrag>.md als Überschrift
   „### <id>“ im Abschnitt „2 Originale“ steht. Das Muster
   KENNUNG entfällt. Fehlt die Mappe, wie bisher Warnung und
   Prüfung aussetzen.
b) Tripel: PUNKT liest zwei oder drei Koordinaten; Ergebnisstelle
   (ergebnis_zahlen, grafikprobe) und zahlenpaare behandeln ein
   Tripel wie ein Paar mit dritter Zahl; Sperre meldet Tripel aus
   Kasten und Originalen.
c) mathnorm: hochgestellte Ziffern ⁰–⁹ werden zu ^n, damit x⁴
   der Mappe gegen x^4 der Bank greift.
d) Selbsttest: je Änderung ein Fall, der vorher falsch lief, und
   einer, der weiter richtig läuft; für (a) mit einer temporären
   Mini-Mappe.
Kopf: v0.5, Datum aus `date`, Änderungen a–c je eine Zeile.
Commit „bank-pruef v0.5: Kennung gegen Mappe, Tripel,
Hochzahlen“, push.

## Teil 2: bank.md

Abschnitt „Felder je Aufgabe“, original: „Kennung wortgleich aus
der Mappe (Abschnitt 2 Originale); papier wie dort“. Abschnitt
mit der Prüfkennung: nach „(P10 Jahr Papier)“ ergänzen: FHR
„(FHR Jahr)“; Abitur „(Abitur Jahr GK)“ für grundlegendes und
„(Abitur Jahr LK)“ für erhöhtes Niveau – iqb grundlegend und
be-gk sind GK, iqb erhöht, bebb-lk und bb-ea sind LK; CAS/MMS-
Fassung und Teil A/B stehen nicht in der Prüfkennung. Abschnitt
„Regeln für den Inhalt“: Punkte und Vektoren als Zeilentupel mit
senkrechtem Strich, A(1 | 2 | 0); sin, cos, ln als \mathrm{…}.
Kopfzeile: Stand 2026-09-27b, vierte Fassung (nach den Sek-II-
Prüfsteinen). Commit „bank.md: Sek II“, push.

## Teil 3: die zwei Prüfsteine nachziehen

- ableitungsregeln: Prüfskript laufen lassen; die 37
  Kennungs-Abweichungen müssen weg sein. Bleiben andere, je
  gemeldete Zeile korrigieren (Edit, nie die ganze Datei).
- vektoren-und-rechenoperationen: die 14 Zeilen mit original null
  und Prüfkennung im Text (stand.md, Entscheidung 4 und Offene
  Punkte) bekommen ihr original aus der Mappe zurück; Prüfskript
  bis 0 Abweichungen.
- In beiden stand.md unter „Offene Punkte“ die erledigten Punkte
  streichen, unter „Befunde“ die Skriptbefunde mit „(v0.5)“
  markieren. Commit je Eintrag „<eintrag>: Originale nach v0.5“,
  push.

## Gegenprobe

- Alle 29 Einträge unter bank/ mit v0.5 prüfen; Tabelle
  Abweichungen/Warnungen vorher (v0.4) und nachher. Die 27 Sek-I-
  Einträge dürfen sich nur durch (b) und (c) ändern, je Grund
  gezählt; ableitungsregeln 37 → 0; vektoren 0/2 → 0/0.
- Selbsttest bestanden.
- Probe (a): eine Zeile mit original id 2019-be-gk-A1.1a in
  ableitungsregeln ist OK; dieselbe Zeile mit id 2019-be-gk-Z9.9z
  ist Abweichung.

## Regeln

- Kein anderer Eintrag unter bank/ wird geändert.
- Zeilen in md höchstens 72 Zeichen.
- Was der Auftrag nicht regelt, entscheidest du und schreibst es
  in den Bericht.
- Am Ende diesen Auftrag nach archiv/auftrag-bank-sek2-regeln-
  2026-09-27.md verschieben (git mv), Commit „archiv: auftrag-
  bank-sek2-regeln“, push.

## Bericht

Im Chat, am Ende, kurz. Erste Zeile das Modell. Dann: die neuen
Absätze aus bank.md wortgleich; Tabelle der 29 Einträge
vorher/nachher; neue Treffer der Sperre in Sek I mit Zeilen-id;
Entscheidungen, die der Auftrag offenließ. Letzte Zeile:
„gepusht auf main, Commit <hash>“.

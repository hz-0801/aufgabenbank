# Auftrag: Mappen Sek II (43 Einträge) und [RLP]-Schutz

Modell: Sonnet. Web-Sitzung, Repo aufgabenbank, main. Commit je
Teil, vor jedem Push `git pull --rebase`, main pushen, kein
eigener Branch. Geschrieben wird nur in werkzeuge/mappe.py,
mappen/ und in diesen Auftrag (Verschieben am Ende). Nichts unter
bank/, nicht bank.md, nicht auftrag-eintrag.md.

## Ausgangslage

27 Mappen liegen unter mappen/, gebaut mit werkzeuge/mappe.py aus
dem Katalog in hz-0801/mathe-nachhilfe (Aufruf steht im Kopf des
Skripts). Als Nächstes bekommt die Bank die Sek-II-Einträge; dafür
fehlen ihre Mappen. Außerdem hat der Sparauftrag von heute die
[RLP]-Zeilen der Verortung gekürzt, aus denen Sitzungen die
Sprossentexte der Pflichtelemente nehmen; sie werden wieder
geschützt.

## Teil 1: mappe.py, [RLP]-Zeilen schützen

Zeilen des Katalogteils, die „[RLP]“ oder „LISUM“ enthalten,
sind von der Kürzung ausgenommen, auch in Verortung und
Lerneinheiten. Die Kürzungszeile im Kopf der Mappe nennt das.
Die 27 vorhandenen Mappen neu bauen (dieselben Namen wie unter
mappen/, ohne _bausteine). Commit „mappe.py: [RLP]-Zeilen
geschützt; 27 Mappen“, push.

## Teil 2: 43 Sek-II-Mappen bauen

Mit demselben Skript, in einem Aufruf oder in Gruppen, diese 43
Einträge (Dateinamen ohne .md in katalog/ von mathe-nachhilfe):

ableitung-und-aenderungsrate ableitungsregeln abstaende
bedingte-wahrscheinlichkeit-und-bayes binomialverteilung ebenen
extremalprobleme flaecheninhalt-durch-integration
flaecheninhalt-und-volumen-im-raum funktionsklassen-und-eigenschaften
funktionsscharen-und-ortskurven geraden gleichungen-loesen
grenzwerte-und-verhalten-im-unendlichen hypergeometrische-verteilung
hypothesentests integrationsregeln kenngroessen-von-verteilungen
kombinatorik konfidenzintervalle kurvenuntersuchung lagebeziehungen
linearkombination-und-lineare-abhaengigkeit
matrizen-und-uebergangsprozesse normalverteilung-und-sigma-regeln
orthogonalitaet punkte-und-strecken-im-koordinatensystem
rekonstruktion-von-bestaenden rekonstruktion-von-funktionsgleichungen
rotationsvolumen scharen-von-geraden-und-ebenen schnittmengen
skalarprodukt-und-winkel spiegelung stammfunktion-und-hauptsatz
tangente-normale-schnittwinkel umkehrfunktion unabhaengigkeit
uneigentliche-integrale vektoren-und-rechenoperationen
vierfeldertafel zufallsexperimente-und-pfadregeln
zufallsgroessen-und-verteilungen

Nicht dabei, absichtlich: ableitungsgraph-und-funktionsgraph
(keine Sprossenzeile im Katalog), daten und
potenz-exponentialfunktionen (warten auf den Katalogauftrag).

Scheitert ein Eintrag (Skriptfehler, fehlender Abschnitt),
zweiter Anlauf; scheitert er wieder, bleibt er weg und steht mit
Fehlertext im Bericht. Commit „mappen: Sek II (<n> Mappen)“,
push.

## Gegenprobe

- Zahl der Dateien unter mappen/ nach Teil 2: 27 + Zahl der
  gebauten Sek-II-Mappen + _bausteine.md.
- Je Sek-II-Mappe: Abschnitt „Für schwache Schüler“ nicht leer,
  Abschnitt „2 Originale“ mit mindestens einem Original; Mappen,
  die eines von beidem nicht haben, stehen im Bericht mit Namen.
- Die sieben Schreibabschnitte und die [RLP]-/LISUM-Zeilen der 27
  Sek-I-Mappen sind gegen den Stand vor Teil 1 unverändert bzw.
  wieder ganz; Zeichen je Mappe vorher/nachher als Tabelle.
- mappen/pythagoras.md, Abschnitt „Für schwache Schüler“: längste
  Zeile 2 996 Zeichen, wie vor dem Sparauftrag.

## Regeln

- Nichts unter bank/, nicht bank.md, nicht auftrag-eintrag.md
  ändern; keine Mappe von Hand ändern.
- Zeilen in md höchstens 72 Zeichen (Mappen ausgenommen).
- Was der Auftrag nicht regelt, entscheidest du und schreibst es
  in den Bericht.
- Am Ende diesen Auftrag nach archiv/auftrag-bank-mappen-sek2-
  2026-09-27.md verschieben (git mv), Commit „archiv: auftrag-
  bank-mappen-sek2“, push.

## Bericht

Im Chat, am Ende. Erste Zeile das Modell. Dann: Zahl der
gebauten Sek-II-Mappen; Tabelle je Sek-II-Mappe (Name, Zeichen,
Zahl der Originale, Zahl der Einheiten); Mappen ohne
Sprossenkette oder ohne Original; gescheiterte Einträge mit
Fehlertext; Tabelle der 27 Sek-I-Mappen vorher/nachher;
Entscheidungen, die der Auftrag offenließ. Letzte Zeile:
„gepusht auf main, Commit <hash>“.

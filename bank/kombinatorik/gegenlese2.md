# Zweitlesung kombinatorik

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 132 (zone 22, e1 35,
e2 40, e3 35)

Prüfung: Jede Zeile mit pruef ist im Scratchpad-Skript aus dem
Aufgabentext neu modelliert worden, nicht aus pruef abgeschrieben:
Abstands-, Zerlegungs- und Wurfaufgaben per Brute-Force (alle
Auswahlen, Permutationen bzw. Wurffolgen aufgezählt), Fakultäten,
Binomialkoeffizienten und Potenzquotienten mit math und Fraction;
alle 100 Zahlwerte stimmen mit pruef und loesung überein, auch die
Rundungen (18!, 42!, 0,225^6, 15120/279936, 1 − 2520/65536).
`python3 werkzeuge/bank-pruef.py kombinatorik`: „Abweichungen: 0,
Warnungen: 0“; der Render-Lauf (bau/render-alle) kompiliert den
Eintrag mit 0 Fehlern und 0 fehlenden Zeichen. 12 Ankreuzen-Zeilen
(je zwei Optionen, loesung nennt genau eine wortgleich), 10
Fehler-finden-Zeilen (Zone-Paar, e1–e3 je drei: eingebauter Fehler
falsch, richtige Rechnung richtig) und 9 Begründen-Zeilen sind
inhaltlich geprüft; alle 20 Zeilen mit original sind gegen
Abschnitt 2 der Mappe abgeglichen.

## Befunde

e2-k2-s2-v1: Der Buchstabe $n$ ist im Text nicht erklärt („aus
einer Gruppe $k$ Personen auszuwählen wie $n - k$ Personen“) –
„aus einer Gruppe von $n$ Personen $k$ auszuwählen wie $n - k$“.

e3-k1-s3-v1, e3-k2-s3-v1: Die Lösung setzt die Muster über die
Lückenformel $(5 \text{ über } 2)$ bzw. $(5 \text{ über } 3)$, ohne
zu sagen, woher die 5 kommt; die Sprosse heißt „Sortenmuster
aufzählen“, und die Kette kennt die Lückenmethode nicht – Muster
nennen (Lagen der Reden 1-3, 1-4, 1-5, 1-6, 2-4, 2-5, 2-6, 3-5, 3-6,
4-6: zehn) oder „15 Paare minus 5 benachbarte = 10“; bei k2-s3-v1
die zehn Dreiermuster wie in e3-k1-s1-v2.

e3-k2-s3-v1, e3-k1-s3-v3: fast dieselbe Aufgabe (Foto-Reihe, drei
bzw. vier Erwachsene, drei Kinder, keine zwei Kinder nebeneinander);
die Anwendung ist damit die eingekleidete Rechnung der Sprosse,
keine Frage aus dem Sachzusammenhang (bank.md „Anwendung“) –
k2-s3-v1 durch eine echte Anwendung ersetzen, etwa: neun freie
Plätze in einer Kinoreihe, vier Freunde wollen mit mindestens einem
freien Platz zwischen je zweien sitzen; 15 Muster mal 4! = 360
Sitzordnungen (Brute-Force geprüft).

e3-k2-s3-v3: sprosse_text „Muster mal Anordnungen“ und merkmal
„Anzahl unter einer Bedingung zählen“ passen nicht zu einer
Wahrscheinlichkeit $4!/4^4$ (das ist Sprosse 5) – merkmal auf
„Anzahl im Wahrscheinlichkeitsterm“ setzen oder die Aufgabe gegen
eine Bedingungsaufgabe tauschen.

e3-k1-s1-v4, e3-k1-s2-v2: Ergebnisse und Kontext wie Original und
Kasten – „vier Möglichkeiten“ und $4 \cdot 3! = 24$ stehen so im
Merkkasten („Drei Schüler auf die vier Stuhlmuster: 4 · 3! = 24“),
Stühle in einer Reihe und drei Schüler wie 2024-bebb-gk-A1.3a/b;
geändert sind nur Stuhlzahl und Abstand – andere Zahlen und anderen
Kontext, etwa acht Haken an einer Garderobe (oder Plätze im
Fahrradständer), vier Personen, zwischen je zweien mindestens ein
freier: fünf Muster 1-3-5-7, 1-3-5-8, 1-3-6-8, 1-4-6-8, 2-4-6-8, in
s2-v2 dann $5 \cdot 4! = 120$ (Brute-Force geprüft).

e3-k1-s3-v3: Die Muster 1-3-5, 1-3-6, 1-4-6, 2-4-6 sind wortgleich
das Kastenbeispiel „drei von sechs Stühlen mit mindestens einem
freien dazwischen“ – andere Zahlen: vier Erwachsene und vier Kinder
(fünf Muster, $5 \cdot 4! \cdot 4! = 2\,880$) oder, wenn k2-s3-v1 wie
oben ersetzt wird, vier Erwachsene und drei Kinder (zehn Muster,
$10 \cdot 4! \cdot 3! = 1\,440$).

e3-k1-s4-v2: dieselbe Struktur und dasselbe Ergebnis wie das
Kastenbeispiel (eine symmetrische Zerlegung einmal, eine mit
$3! = 6$ Zuordnungen, zusammen 7; dort 15 Tulpen 4–6, hier 9 Bonbons
2–4) – Grenzen ändern, etwa zehn Bonbons, je Sorte zwei bis fünf:
2 + 3 + 5 in 6, 2 + 4 + 4 in 3, 3 + 3 + 4 in 3 Zuordnungen, zusammen
12 (Brute-Force geprüft).

e2-k1-s1-v5, e1-k1-s6-v3, e2-k1-s8-v1: Kontext wie das Original,
nur Objekt und Zahlen getauscht – Händler, Handys in Farben,
Schaufenster (2017-be-gk-B3.1a: Händler, Smartphones in Farben,
Schaufenster); Verkostung, drei probieren und Reihenfolge festlegen
(2023MgrundlegendBStochastikWTR1-1a: Röstgrade, wörtlich dieselbe
Aufgabe); sehr große Kiste, Kunde greift rein zufällig heraus
(2026-B-3d: sehr große Lieferung, Kunde greift rein zufällig
heraus). bank.md verlangt „anderer Kontext“ – andere Geschichte,
etwa fünf Trikotfarben, vier fürs Mannschaftsfoto; drei von sieben
Fahrgeschäften im Freizeitpark in selbst gewählter Reihenfolge;
sechs Bäume aus vier Baumarten für einen Garten, nur die Anzahl je
Art zählt. Leichter, aber gleiche Art: e2-k1-s4-v1, e2-k1-s4-v2,
e2-k1-s7-v1, e3-k1-s4-v1, e2-k1-s8-v3, e2-k1-s8-v4 folgen der
Geschichte des Originals mit anderem Objekt (Wochenwerbung im
Laden, Geschenke an Befragte, Strauß in Farben mit Rosen statt
Tulpen, Spielkarten mit zwei Symbolgruppen) – zulässig, aber näher
am Original als nötig; bei Gelegenheit umerzählen.

e3-k1-s1-v1, e3-k1-s1-v2, e3-k1-s1-v3, e3-k1-s1-v4, e3-k1-s1-v5:
antwort „__“, aber die Aufgabe fragt keine Zahl („Schreibe alle
Auswahlen auf. Begründe, dass keine fehlt.“ bzw. „Gib diese vier
Möglichkeiten an“) – antwort „“ (form text, wie die übrigen
Textaufgaben) oder die Frage „Wie viele sind es?“ anhängen und
antwort „Anzahl: __“.

Sauber: 111 Zeilen ohne Befund

## Abgleich

Beide Leser: keine – die Erstlesung meldet 132 Zeilen ohne
Befund (rechnerisch: math.comb/factorial und vollständiges
Aufzählen, deckungsgleich mit der Zweitlesung).
Nur Zweitleser: e2-k2-s2-v1 (Buchstabe n unerklärt); e3-k1-s3-v1,
e3-k2-s3-v1 (Lückenformel statt Muster aufzählen); e3-k2-s3-v1,
e3-k1-s3-v3 (Anwendung fast doppelt zur Sprosse); e3-k2-s3-v3
(merkmal passt nicht zur Wahrscheinlichkeit); e3-k1-s1-v4,
e3-k1-s2-v2 (Ergebnis 4 und 4 · 3! = 24 samt Kontext wie Original
und Kasten); e3-k1-s3-v3 (Muster wortgleich Kasten); e3-k1-s4-v2
(Zerlegungsstruktur und Ergebnis 7 wie Kasten); e2-k1-s1-v5,
e1-k1-s6-v3, e2-k1-s8-v1 (Kontext wie Original; leichter
e2-k1-s4-v1, e2-k1-s4-v2, e2-k1-s7-v1, e3-k1-s4-v1, e2-k1-s8-v3,
e2-k1-s8-v4); e3-k1-s1-v1 bis e3-k1-s1-v5 (antwort „__“ ohne
Zahlfrage).
Nur Erstleser: keine.
Widerspruch: keiner – die Erstlesung hat nur gerechnet und nennt
die Schreibweise „(n über k)“ als bekannten Befund aus stand.md;
die 21 ids der Zweitlesung betreffen Eindeutigkeit, Passung und
Regeln, zu denen die Erstlesung kein Urteil abgibt.

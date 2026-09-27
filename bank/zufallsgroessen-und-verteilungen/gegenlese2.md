# Zweitlesung zufallsgroessen-und-verteilungen

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 70 (e1 33, e2 23,
zone 14)

Prüfung: Jede Lösung mit Python (fractions, itertools) aus dem
Aufgabentext neu gerechnet – Ergebnismengen aufgezählt, Werte
gesammelt, Brüche exakt; Diagrammhöhen in grafik und
loesungsgrafik gegen die Rechnung, Säulenverhältnisse und
Summen der Diagramme nachgerechnet, Binomialwerte für
e2-k1-s2-v1 mit math.comb. Jedes Feld pruef gegen die
nachgerechnete Zahl. Alle 70 Lösungszahlen stimmen; kein Feld
pruef weicht von der Lösung ab. `python3 werkzeuge/bank-pruef.py
zufallsgroessen-und-verteilungen`: zone 0/0, e1 0/0, e2 0/0 –
Abweichungen 0, Warnungen 0. Mengen je Kette stimmen (e1: 4 +
4/5/3/3/2 + 12; e2: 4/5/2 + 12; Zone 6/4/4 mit Zone-Paar).
Sperre gegen Merkkasten (zahlenfrei), Typische Fehler
(zahlenfrei) und die vier Originale von Hand geprüft. Die
Befunde unten betreffen Form, Sprossenpassung, Fehlerbeschreibung
und Dubletten, nicht die Rechnung.

## Befunde

e1-k2-s1-v5: Die Zufallsgröße ist „größere minus kleinere
Augenzahl“, also eine Differenz; sprosse_text heißt „die Tabelle
einer Summe durch Abzählen füllen“. Der Handgriff (zählen,
teilen) ist derselbe, die Zuordnungsregel aber eine andere als
in v1–v4 – mehr als Zahlen und Kontext. Rechnung stimmt
($\frac{4}{16}$; $\frac{6}{16}$; $\frac{4}{16}$; $\frac{2}{16}$).
– Vorschlag: eine Summe nehmen, etwa Glücksrad $1$, $2$, $3$
zweimal gedreht, Summe $2$ bis $6$: $\frac{1}{9}$; $\frac{2}{9}$;
$\frac{3}{9}$; $\frac{2}{9}$; $\frac{1}{9}$ (kein Tetraeder, den
trägt v1 schon).

e1-k2-s3-v1, e1-k2-s3-v2, e1-k2-s3-v3: Das Original
2021MerhoehtAStochastik13-a gibt die Wahrscheinlichkeiten als
Säulen eines Diagramms („$p$, $3p$, $2p$ aus dem Diagramm“),
Fehlerquelle „die Säulenhöhen als Auszahlungen lesen“. Alle drei
Varianten nennen die Vielfachen von $p$ im Text; Form (Diagramm)
und Falle des Originals sind weg, obwohl das Feld original und
die Kennung „(Abitur 2021 LK)“ stehen (bank.md: „gleiches
Verfahren, gleiche Falle, gleiche Form“). Die Rechnung selbst
stimmt ($8p = 1$, $4p = 1$, $10p = 1$). – Vorschlag: je Variante
ein Diagramm mit Achse ohne Zahlen, etwa für v1
`\saeulenab[ymax=6,ystep=1,yfein=1,ylabel=Wahrscheinlichkeit,ohnezahlen]{0/2,2/5,10/1}`
und im Text „Das Diagramm zeigt die Verteilung der Auszahlung in
Euro; die Säulen sind $2p$, $5p$ und $p$ hoch.“ – dann liegt die
Falle (Höhen als Beträge lesen) wieder in der Aufgabe.

e1-k3-s1-v1: Die Fehlerrechnung listet „Werte: 4, 7, 7, 10“ und
$P(X = 7) = \tfrac{1}{4}$ – der Schüler hält die beiden $7$ für
zwei verschiedene Werte (Muster „spiegelbildliche Ergebnisfolgen
als verschiedene Beträge“). Die Lösung beschreibt es umgekehrt:
„er wird einmal gelistet und doppelt gezählt“ – in der Rechnung
steht die $7$ zweimal und wird je einmal gezählt. Richtiger Wert
$\frac{2}{4} = \frac{1}{2}$ stimmt. – Vorschlag: „Fehler: die
beiden $7$ (aus 2-5 und 5-2) sind ein Wert mit zwei günstigen
Folgen, nicht zwei Werte. Richtig: Werte $4$, $7$, $10$;
$P(X = 7) = \frac{2}{4} = \frac{1}{2}$.“

e1-k3-s1-v2: Dieselbe Rechnung wie e1-k2-s1-v1 – zwei
Tetraederwürfel, Augensumme, $P(X = 5) = \frac{4}{16}$; der
Grundfall v1 lässt genau diesen Tabelleneintrag füllen, das
Fehler-finden rechnet ihn noch einmal. – Vorschlag: anderes
Gerät, etwa Glücksrad $1$ bis $5$ zweimal gedreht, Summe $6$:
falsch „1 und 5, 2 und 4, 3 und 3“ $\to \tfrac{3}{25}$, richtig
$\frac{5}{25} = \frac{1}{5}$ (3 und 3 zählt einmal, die anderen
doppelt).

e1-k3-s1-v3: Die falsche Rechnung $P(X = 2) = 0{,}3$,
$P(X = 3) = 0{,}3$ ergibt mit $0{,}1 + 0{,}3$ die Summe
$1{,}0$ – die Summe eins ist eingehalten, verletzt ist nur das
Verhältnis „doppelt so groß“. Die Lösung nennt aber als Fehler
„die Werte geraten statt über die Summe eins bestimmt“; das
passt nicht zur gezeigten Rechnung. Richtige Werte $0{,}2$ und
$0{,}4$ stimmen. – Vorschlag: Fehlerrechnung so setzen, dass die
Summe kippt und das Verhältnis stimmt, z. B. $P(X = 2) = 0{,}3$,
$P(X = 3) = 0{,}6$ (Summe $1{,}3$); Lösung „Fehler: Summe $1{,}3$
statt $1$ – das Verhältnis wurde ohne den Rest gesetzt. Richtig:
Rest $0{,}6$ im Verhältnis 1 zu 2, also $0{,}2$ und $0{,}4$.“

e1-k3-s3-v2: hoehe pflicht anwendung, aber „Ein Spieler würfelt
zweimal; jede Sechs bringt $3$ €, Einsatz $1$ € – wie ist der
Gewinn verteilt?“ ist eine eingekleidete Rechnung ohne Frage aus
dem Kontext (bank.md: „eine eingekleidete Rechnung ist keine
Anwendung“). Die Lösung schreibt $P(-1)$, $P(2)$, $P(5)$ ohne
eingeführte Größe. Werte $\frac{25}{36}$, $\frac{10}{36}$,
$\frac{1}{36}$ stimmen. – Vorschlag: Kontextfrage anhängen, etwa
„Wie wahrscheinlich geht der Spieler mit Verlust nach Hause?“
($\frac{25}{36}$) oder „Ist das Spiel für den Anbieter günstig?“;
in der Lösung $X$ benennen ($P(X = -1)$ …).

e1-k3-s3-v3: Kiosk mit zwei Kunden – realistische Größen, aber
die Frage „Wie ist $X$ verteilt?“ ist keine Frage aus dem
Kontext. Werte $0{,}49$; $0{,}42$; $0{,}09$ stimmen. –
Vorschlag: „Wie wahrscheinlich verkauft der Kiosk in dieser
Stunde mindestens eine Zeitung?“ ($0{,}51$) oder „… genau eine?“
($0{,}42$), Verteilung als Zwischenergebnis.

e2-k1-s0-v1, e2-k1-s0-v2, e2-k1-s0-v4: merkmal „am Diagramm
prüfen, ob die Säulen zusammen eins ergeben, nichts rechnen“ –
die Frage „Kann das Diagramm die vollständige Verteilung zeigen?“
verlangt aber genau das Rechnen: $0{,}2 + 0{,}5 + 0{,}3 = 1$;
$0{,}3 + 0{,}5 + 0{,}4 = 1{,}2$; $3 \cdot 0{,}3 = 0{,}9$
(Ablesen am Feinraster $0{,}05$ und Addieren). Der
Erkennungsschritt des Katalogs (Zeile 30) heißt „ankreuzen,
welche Werte sich zu eins summieren müssen und welcher fehlt;
nichts rechnen“ – das trägt nur v3. Lösungen sind richtig. –
Vorschlag: entweder merkmal ehrlich machen („die Säulenhöhen
überschlagen und mit eins vergleichen“) oder die drei Zeilen in
die Form von v3 bringen (fehlende Säule, „welche trägt den
Rest?“) mit anderen Höhen als e1-k1-s0-v2.

e2-k1-s1-v1: Die Aufgabe ist das Original 2022-bebb-lk-A1.8a mit
einer geänderten Zahl – Werte $0$ bis $4$, symmetrisch,
$P(X = 2)$ gegeben, $P(X \le 2)$ gesucht; nur $0{,}6 \to 0{,}4$,
und $0{,}4$ ist zugleich die Restwahrscheinlichkeit des Originals.
Das Feld original ist null, eine Kennung fehlt. Zugleich trägt
keine der 70 Zeilen das Katalog-Original 2022-bebb-lk-A1.8a
(Zielmarke Einheit 2, abi) im Feld original – bank.md verlangt
„Prüfungshöhe 2 je Original des Katalogs (verfremdet)“, und das
Feld darf an jeder hoehe stehen. Rechnung $0{,}3 + 0{,}4 = 0{,}7$
stimmt. – Vorschlag: v1 anders belegen (etwa Werte $3$ bis $7$,
$P(X = 5) = 0{,}3$, Ergebnis $0{,}65$) und zwei Zeilen mit
original {"id": "2022-bebb-lk-A1.8a", "jahr": 2022, "papier":
"2022-bebb-lk"} und Kennung „(Abitur 2022 LK)“ ergänzen – als
eigene Sprosse vor der Zuordnung oder als zwei Grundfall-Zeilen
mit Feld original; welcher Weg, entscheidet der Chat.

e2-k2-s1-v1: Gleiche Rechnung wie e2-k1-s1-v2 –
$P = \frac{1 - 0{,}2}{2} + 0{,}2 = 0{,}4 + 0{,}2 = 0{,}6$, nur
der Wertebereich anders ($0$ bis $4$ statt $1$ bis $5$); dazu
wieder der Rahmen des Originals ($0$ bis $4$, $X = 2$). Das
Fehlermuster (Einzelwert als kumulierter Wert) ist richtig
gewählt. – Vorschlag: anderen Einzelwert, z. B. $P(X = 2) =
0{,}16$, richtig $0{,}42 + 0{,}16 = 0{,}58$, und Werte $1$ bis
$5$ oder $-2$ bis $2$ (dann v5 des Grundfalls anpassen, s. u.).

e2-k2-s1-v2, e2-k2-s3-v1: Die Rechnung $0{,}25 + 0{,}5 = 0{,}75$
steht dreimal im Eintrag – e2-k1-s1-v4 (Werte $10$, $20$, $30$),
e2-k2-s1-v2 (Werte $1$ bis $5$, Fehler finden) und e2-k2-s3-v1
(Saftflasche, $P(X \ge 500)$). Alle drei richtig, aber dieselbe
Zahl. – Vorschlag: e2-k2-s1-v2 mit $P(X = 3) = 0{,}7$ (falsch
„$0{,}3 + 0{,}7 = 1$“, richtig $0{,}15 + 0{,}7 = 0{,}85$; nicht
$0{,}6$, das wäre die Zahl des Originals 2022-bebb-lk-A1.8a);
e2-k2-s3-v1 mit „genau $500$ ml enthalten $44\,\%$ der
Flaschen“, richtig $0{,}28 + 0{,}44 = 0{,}72$.

e2-k2-s4-v1: Die Lösung ist zeichengleich mit e1-k3-s4-v1 –
loesungsgrafik in beiden Zeilen
`\saeulen{0/0.125,1/0.375,2/0.375,3/0.125}{0.5}{0.125}{$P(X = k)$}`,
gleiche Achsen; einmal aus der Tabelle, einmal aus „Anzahl Kopf
bei drei Münzwürfen“. Das Skript prüft nur aufgabe und grafik,
darum kein Alarm. Rechnung ($\frac{1}{8}$, $\frac{3}{8}$,
$\frac{3}{8}$, $\frac{1}{8}$) stimmt. – Vorschlag: e2-k2-s4-v1
auf vier Münzwürfe stellen (Höhen $\frac{1}{16}$, $\frac{4}{16}$,
$\frac{6}{16}$, $\frac{4}{16}$, $\frac{1}{16}$, Achse
$0$ bis $4$, ystep $0{,}125$) oder in e1-k3-s4-v1 eine andere
Tabelle ($0{,}2$; $0{,}3$; $0{,}4$; $0{,}1$).

Hinweise ohne Befundzählung: (a) e2-k1-s2-v1 und -v2 setzen drei
`\saeulenab` mit `\quad` nebeneinander in ein grafik-Feld; bei
sieben Säulen je Diagramm (v1) wird das breiter als der Satz-
spiegel – der Zusammenbau sollte die drei untereinander oder in
zwei Reihen setzen (Maßstab 2.4 b nennt höchstens zwei Grafiken
je Hauptnummer; das Original hatte ebenfalls drei). (b) Fünf
Zeilen nutzen zwei Tetraederwürfel (e1-k2-s1-v1, -v5,
e1-k3-s1-v2, e2-k1-s2-v2, e2-k2-s4-v3); Kontextmonotonie, kein
Regelverstoß. (c) e1-k2-s1-v1 lässt nur $k = 2$ bis $5$ füllen,
die Einträge summieren sich zu $\frac{10}{16}$ – die Kontrolle
„Summe eins“ aus dem Merkkasten greift nicht; lösbar, aber
verwirrend. (d) e2-k2-s3-v1 bis -v3 und e1-k3-s3-v2 verwenden
$X$ in der Lösung, ohne dass die Aufgabe den Buchstaben
einführt.

Sauber: 53 Zeilen ohne Befund (alle 70 Rechnungen richtig, pruef
überall passend, bank-pruef.py ohne Abweichung und Warnung;
Zone vollständig sauber; die 17 Befundzeilen betreffen die Form
des Originals 2021 an drei Zeilen, ein fehlendes Original 2022
abi, zwei unpassende Fehlerbeschreibungen, drei Zeilen mit
Merkmal „nichts rechnen“, zwei schwache Anwendungen, eine
Differenz in der Summen-Sprosse und fünf Dublettenzeilen).

## Abgleich mit gegenlese.md

Befundzeilen: Erstleser 7 (Sauber 63), Zweitleser 17 (Sauber 53).
Beide Leser: alle 70 Rechnungen richtig, bank-pruef.py ohne
Abweichung.

Beide haben (4): e1-k2-s1-v5 (Differenz statt Summe),
e1-k3-s1-v3 (Fehlerrechnung hält die Summe eins ein, Lösung nennt
„geraten statt Summe eins“), e1-k3-s3-v2 und e1-k3-s3-v3
(Anwendung ohne Kontextfrage). Die Vorschläge decken sich; beim
Ersatz für e1-k2-s1-v5 schlägt der Erstleser „Tetraederwürfel
und Münze 0/1, Summe“ vor – das liegt dicht an e1-k2-s1-v4
(Würfel und Münze 0/1, Summe), darum besser das Glücksrad
$1$, $2$, $3$ (oben).

Nur der Erstleser (3): e1-k1-s0-v3 „die Tabelle nennt …“ ohne
abgebildete Tabelle – zutreffend, übersehen; die Aufgabe bleibt
lösbar, der Satz sollte ohne Tabellenbezug stehen oder eine
\sachtabelle bekommen. zone-f1-v2 (Pasch zählen ist schon
„günstige Fälle zählen“, Merkmal der Sprosse 2) – zutreffend,
kleines Gewicht; eine Frage nach allen Ergebnissen (Würfel und
Münze: $12$) passt besser zum Merkmal „alle Paare aufzählen“.
e1-k2-s2-v3 (kein Einsatz, Schritt „minus Einsatz“ fehlt) –
nicht zutreffend als Befund: sprosse_text heißt „die möglichen
Werte einer Auszahlung … nachweisen“, v3 ist die reine Form,
v1/v2 rechnen zusätzlich den Gewinn; eine Angleichung ist
Ermessen, kein Verstoß.

Nur der Zweitleser (13): e1-k2-s3-v1/-v2/-v3 (Original 2021 ohne
Diagramm, Form und Falle verloren), e1-k3-s1-v1 (Lösungstext
beschreibt den Fehler umgekehrt), e1-k3-s1-v2 (Rechnung wie
e1-k2-s1-v1), e2-k1-s0-v1/-v2/-v4 (Merkmal „nichts rechnen“,
Aufgabe verlangt Addieren), e2-k1-s1-v1 (Original 2022-bebb fast
unverfremdet; das abi-Original fehlt im Feld original in allen
70 Zeilen), e2-k2-s1-v1, e2-k2-s1-v2, e2-k2-s3-v1 (Dubletten der
Rechnungen $0{,}4 + 0{,}2$ und $0{,}25 + 0{,}5$), e2-k2-s4-v1
(Lösungsgrafik zeichengleich mit e1-k3-s4-v1).

Widerspruch (1): e1-k2-s2-v3 – der Erstleser hält die fehlende
Einsatzrechnung für ein anderes Merkmal, ich halte die reine
Auszahlung für die Sprosse selbst und v1/v2 für die Erweiterung.

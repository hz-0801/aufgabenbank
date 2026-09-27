# Mappe: hypergeometrische-verteilung

Eintrag: hz-0801/mathe-nachhilfe, katalog/hypergeometrische-verteilung.md
Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25T11:16:56+02:00, „katalog: Marken-Zeilen je Lerneinheit, drei Einheiten ergänzt, marken-bau.py“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:42 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Hypergeometrische Verteilung
 3
 4  ### Verortung
 5  Das Ziehen ohne Zurücklegen aus einer kleinen Gesamtheit: die Wahrscheinlichkeit für genau k Treffer als Quotient von Binomialkoeffizienten (günstige durch mögliche Teilmengen, gleichwertig das Produk … (gekürzt, 1378 Zeichen)
 6  [GOST] Q2 (BB S. 26–27): L5-Zeile „Anwendungssituationen mithilfe von Urnenmodellen untersuchen“ mit dem Inhalt „Zufallsexperimente mit nur zwei möglichen Ausgängen im Urnenmodell: Ziehen ohne Zurückl … (gekürzt, 1387 Zeichen)
 7  [FOS] Kein Bestand: der RLP FOS 2019 kennt die hypergeometrische Verteilung nicht; keine fhr-Zeile.
 8  [LS-AA] Kein eigenes Kapitel – das Lehrwerk behandelt das Ziehen ohne Zurücklegen in den Urnen- und Pfadregel-Einheiten (Kl. 8 VIII, QP VIII 1–2); die Kapitelsuche „hypergeo“ hat im Fahrplan keinen Treffer. Zuordnung: beide Einheiten = Rohdatei plus Urnenmodell-Vorläufer (Ermessen). Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Genau k Treffer ohne Zurücklegen: die Situation erkennen (feste kleine Gesamtheit, Ziehen ohne Zurücklegen – das Binomialmodell ist ungeeignet), die Wahrscheinlichkeit als günstige durch mögliche Teilmengen (Quotient von Binomialkoeffizienten), gleichwertig die Bruchkette der Pfadregel; Mindestens- und Höchstens-Ereignisse über das Gegenereignis (statt viele Fälle zu addieren). (Q2, GK-Kern „Ziehen ohne Zurücklegen“; OHiMi 2.4 „Ansätze“; IQB-VER 4 vorausgesetzt) ← Eingabe „ohne zurücklegen“, „hypergeometrisch“, „lotto-prinzip“, „mindestens eine ohne zurücklegen“
12    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK
13  2. Kumulieren gegen eine Schranke: hypergeometrische Einzelwahrscheinlichkeiten aufsummieren und die größte (oder kleinste) Trefferzahl gegen eine Schranke bestimmen – Nachbarwerte prüfen wie beim Binomialmodell. (Q2; Prüfungshöhe) ← Eingabe „kumuliert ohne zurücklegen“, „größtes n schranke“
14    Marken: BE Q2 · BB Q2 · GK · Abitur LK
15  Warum Kurzform: sieben Zeilen, drei Typen – die Substanz trägt zwei Einheiten (die Formel mit Gegenereignis, das Kumulieren); die Modellabgrenzung ist die gemeinsame Vorstufe mit binomialverteilung.md. Niveaustufung: fhr = kein Bestand; GK und LK = beide Einheiten (kein LK-Zusatz; die Kumulierungsaufgabe liegt im lk-Heft). Geltungsbesonderheit: Berlin führt das Thema in beiden Geltungsdateien mit „nein“, Brandenburg mit „ja“ – für Berliner Zielprüfungen ist es kein Blattstoff (Entscheidung 30: das einzige Thema mit Länderunterschied).
16
17  ### Typen je Lerneinheit
18  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen; Nebentypen der Rohdatei sind nicht zugeordnet.
19  Einheit 1: Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen (3) — Nachweis: Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen (3; Ermessen, siehe Offene Punkte) — kein Deutungstyp. Dazu: Fehler finden (binomial mit fester Trefferwahrscheinlichkeit gerechnet, obwohl ohne Zurücklegen gezogen wird – das Kernfehlmuster; mit Zurücklegen gerechnet; die Bruchkette mit gleichbleibendem Nenner) · Begründen (warum sich p von Zug zu Zug ändert; warum günstige durch mögliche Teilmengen dasselbe liefert wie die Bruchkette).
20  Einheit 2: Größte Trefferzahl, bis zu der die kumulierte hypergeometrische Wahrscheinlichkeit unter einer Schranke bleibt, ermitteln (1) — kein Nachweistyp — kein Deutungstyp. Dazu: Fehler finden (mit der Binomialverteilung kumuliert; die Schranke am falschen Nachbarwert festgemacht) · Begründen (warum beide Nachbarwerte zu belegen sind).
21  Zählung: 2 + 1 = 3 Haupttypen, 6 + 1 = 7 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal.
22
23  ### Voraussetzungen (Blatt 0)
24  Fertigkeiten (je Zeile: was, wofür):
25  - Binomialkoeffizient (n über k) als Anzahl der Auswahlen, Rechnertaste und kleine Werte im Kopf – Zähler und Nenner der Formel. Thema kombinatorik.md Einheit 2. [GOST Eingangsvoraussetzung L5 „Binomialkoeffizienten“; GOST-OHiMi 2.4; FS-IQB 1.4]
26  - Pfadregeln ohne Zurücklegen (Bruchkette mit schrumpfendem Nenner) und das Gegenereignis – der zweite Weg und die Mindestens-Fälle. Sek-II-Nachbarthema zufallsexperimente-und-pfadregeln.md Einheit 4 und 5 (Bruchkette und Gegenereignis; ein Pfad mal Anzahl der Reihenfolgen, Übergang zum Lotto-Bruch). [GOST Q2 L5 „Ziehen ohne Zurücklegen“; RLP G „mit und ohne Zurücklegen“]
27  - Das Binomialmodell und seine Bedingungen (zur Abgrenzung: wann es ungeeignet ist) – die Modellwahl. Sek-II-Nachbarthema binomialverteilung.md Einheit 1. [GOST Q2 L5 beide Urnenmodelle]
28  - Brüche multiplizieren und kürzen – die Bruchkette. Sek-I-Thema bruchrechnung.md. [GOST-OHiMi 2.1]
29  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
30  - „Mit oder ohne Zurücklegen?“ – zu Aufgabentexten ankreuzen, ob die Gesamtheit beim Ziehen schrumpft (feste kleine Gruppe, Auslosung, Auswahl) oder gleich bleibt – und welches Modell folgt; nichts rechnen. Vor Einheit 1. [GOST Q2 L5; Rohdatei-Fehlerquelle „binomial rechnen“; abi 2017-bb-ea-B4.2e, iqb 2023MgrundlegendBStochastikWTR1-1b]
31  - „Direkt oder übers Gegenereignis?“ – ankreuzen, ob „genau k“ gefragt ist (Formel) oder „mindestens/höchstens“ (Gegenereignis statt Fallsummen); nichts rechnen. Vor Einheit 1 und 2. [Rohdatei; abi 2022-bebb-gk-A1.6a, 2018-bb-ea-B4.1d]
32
33  ### Merkkasten
34  Einheit 1 (Genau k Treffer ohne Zurücklegen):
35      Erkennen: aus einer festen kleinen Gesamtheit wird ohne Zurücklegen gezogen – die Trefferwahrscheinlichkeit ändert sich von Zug zu Zug, das Binomialmodell ist ungeeignet.
36      Formel: P(genau k Treffer) = (günstige Auswahlen) / (mögliche Auswahlen) – im Zähler das Produkt der Binomialkoeffizienten für Treffer und Nieten, im Nenner der Binomialkoeffizient aller Auswahlen.
37      Bruchkette: gleichwertig die Pfadregel mit schrumpfendem Nenner – für kleine Fälle oft schneller; beide Wege müssen dasselbe liefern.
38      Gegenereignis: „mindestens einer“ rechnet sich als eins minus „keiner“ – der Fall „keiner“ ist eine einzige Auswahl-Quote statt vieler Summanden.
39      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] „Ansätze zur Berechnung von Wahrscheinlichkeiten für … hypergeometrisch verteilte Zufallsgrößen“, „Kombinationen ohne Wiederholung“; [IQB-VER 4] setzt den Binomialkoeffizienten-Weg ausdrücklich voraus (Teil-A-Beleg 2022-bebb-gk-A1.6a).
40      Formelsammlung: [FS-IQB 1.4] führt den Binomialkoeffizienten; eine hypergeometrische Formel steht nicht darin – der Ansatz muss sitzen – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
41  Quelle: eigene Formulierung nach [GOST Q2 L5] „Ziehen ohne Zurücklegen (hypergeometrische Verteilung)“, [GOST-OHiMi 2.4] und [IQB-VER 4]; ohne Zahlenbeispiel (die Poolbeispiele sind kontextgebunden; Ermessen); [LS-AA Urnenmodell-Einheiten als Vorläufer].
42
43  Einheit 2 (Kumulieren gegen eine Schranke):
44      Aufsummieren: kumulierte hypergeometrische Werte entstehen durch Addieren der Einzelwahrscheinlichkeiten – eine Rechnerfunktion wie beim Binomialmodell gibt es in der Prüfung nicht als Anlage, die Summe wird ausgeschrieben.
45      Schranke: für „größte Trefferzahl unter der Schranke“ beide Nachbarwerte belegen – den letzten, der die Schranke unterschreitet, und den ersten, der sie reißt (dieselbe Arbeitsregel wie bei binomialverteilung.md Einheit 4).
46      Auswendig (Teil A): keine – die Kumulierungsaufgabe ist Teil-B-Arbeit mit Rechner; sitzen muss der Ansatz aus Kasten eins.
47      Formelsammlung: keine – [FS] offen
48  Quelle: eigene Formulierung nach der Poolpraxis und [GOST-OHiMi 2.4]; ohne Zahlenbeispiel; Arbeitsregel aus binomialverteilung.md Einheit 4 übernommen.
49
50  ### Typische Fehler
51  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 7 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet.
52  - Binomial statt hypergeometrisch – das Kernfehlmuster: mit einer festen Trefferwahrscheinlichkeit gerechnet, obwohl aus einer kleinen Gesamtheit ohne Zurücklegen gezogen wird; mit Zurücklegen gerechnet; die Binomialverteilung auch beim Kumulieren verwendet. [abi 2018-bb-ea-B4.1d, 2017-bb-ea-B4.2e, 2022-bebb-gk-A1.6a, 2023-bebb-lk-B4k, 2023-bebb-lk-B4l; iqb 2024MerhoehtBStochastikWTR2-1e, 2023MgrundlegendBStochastikWTR1-1b]
53  - An der Schranke: den falschen Nachbarwert angegeben, weil nur ein Wert geprüft wurde. [abi 2023-bebb-lk-B4l]
54
55  ### Für schwache Schüler
56  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q2: das Urnenmodell ohne Zurücklegen und der Ansatz über Binomialkoeffizienten (Einheit 1); kein LK-Zusatz. Ohne Hilfsmittel (Anlage OHiMi 2.4, Prüfungsteil A): der Ansatz – Kasten eins vollständig. Vorrat (Ermessen): die Kumulierung gegen eine Schranke (Einheit 2, eine Zeile, lk-Heft). RLP FOS (fhr): kein Bestand. Geltungshinweis fürs Blatt: für Berliner Zielprüfungen (be-gk, be-lk) ist das Thema laut Geltungsdateien kein Stoff – Blätter dafür lassen es aus; für Brandenburger Zielprüfungen gilt es. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung keine hypergeometrische Verteilung – kein zusätzlicher Posten.
57  Grundvorstellung (Blatt 0) [GOST Q2 L5, MO]: Wer ohne Zurücklegen zieht, verändert die Urne – die zweite Ziehung findet eine andere Welt vor. „Hier sind sechs Kugeln in einem Beutel, vier rote und zwei grüne, kein Term. Ziehe eine Kugel und lege sie NICHT zurück: wie stehen die Chancen für Grün jetzt – besser oder schlechter als vorhin, und wovon hängt das ab? Und wenn du die gezogene Kugel zurücklegst: was ist dann bei der zweiten Ziehung anders? Bei welcher Spielart bleibt die Welt gleich, bei welcher schrumpft sie?“ Wer beiden Spielarten dieselben Chancen gibt, braucht das vor jeder Formel: Ohne Zurücklegen ändert jede Ziehung die Wahrscheinlichkeiten – deshalb zählt man Auswahlen statt unabhängige Wiederholungen. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q2 L5, beide Urnenmodelle nebeneinander), die Aufgabenform Ermessen; sie ist das Gegenstück zur Bernoulli-Prüfliste von binomialverteilung.md. [GOST Q2 L5; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „binomial rechnen“, abi 2018-bb-ea-B4.1d; BASICS nur als Strukturvorbild, keine Inhalte]
58  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [Rohdatei; Sprossenfolge Ermessen]:
59  - Genau k ohne Zurücklegen (Einheit 1): „Mit oder ohne Zurücklegen?“ und „Direkt oder übers Gegenereignis?“ ankreuzen (Vorstufe, Grundvorstellung) → kleine Fälle über die Bruchkette und das Gegenereignis (Grundfall, viermal; abi 2022-bebb-gk-A1.6a, Teil A) → „genau k“ über günstige durch mögliche Teilmengen (abi 2023-bebb-lk-B4k; iqb 2024MerhoehtBStochastikWTR2-1e, 2023MgrundlegendBStochastikWTR1-1b) → „höchstens k“ über das Gegenereignis statt Fallsummen (abi 2018-bb-ea-B4.1d) → Prüfungshöhe: die Auslosung mit Gegenereignis und die Ungeeignetheit des Binomialmodells begründen (abi 2017-bb-ea-B4.2e, Niveau II – der Begründungsteil gehört als Typ zu binomialverteilung.md).
60  - Kumulieren (Einheit 2): den Ansatz aus Einheit eins als Vorstufe → Einzelwahrscheinlichkeiten aufsummieren und beide Nachbarwerte gegen die Schranke belegen (Grundfall; abi 2023-bebb-lk-B4l, Niveau II – Prüfungshöhe zugleich, der Bestand trägt eine Zeile).
61  Hinweis: die Sprossenkette der Einheit zwei ist mit einer Zeile die kürzeste des Sek-II-Katalogs; hinführende Aufgaben kommen beim Blattbau aus Einheit eins.
62
63  ### Prüfungsform (fhr / abi / iqb)
64  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – mit der Besonderheit dieses Themas: die Geltungsdateien führen es für bb-gk und bb-ea mit „ja“, für be-gk und be-lk mit „nein“ (das einzige Thema, bei dem sich die Länder unterscheiden; Entscheidung 30). Für fhr ist der Pool keine Vorgabe; kein Bestand. Die Rohdatei zählt 7 Zeilen mit 3 Haupttypen (abi 5 Zeilen, 3 Typen; iqb 2 Zeilen, 1 Typ; 1 Typ in beiden Profilen), Jahre 2017–2024. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
65  fhr: kein Bestand, keine Zeile.
66  abi (5 Zeilen, 3 Typen; Landeshefte bb-ea, bebb-gk, bebb-lk 2017–2023) [abi-Katalog]: Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen (3, E1) · je 1: Größte Trefferzahl, bis zu der die kumulierte hypergeometrische Wahrscheinlichkeit unter einer Schranke bleibt, ermitteln (E2) · Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen (E1). Muster: Ungewöhnlich für das Bündel trägt hier der Landesbestand das Thema – keine der fünf Zeilen ist eine Pooldublette; die Brandenburger Hefte stellen die Auslosungs- und Auswahlkontexte (Freikarten 2017, Arztpraxis 2018, Urne in Teil A 2022, Reisegruppe 2023 mit zwei Zeilen im lk-Heft). Teil B vier Zeilen (zwei bis vier Punkte), Teil A eine (2022-bebb-gk-A1.6a, zwei Punkte). Niveau I 1, II 4.
67  iqb (2 Zeilen, 1 Typ; Pool 2023–2024, grundlegend 1 und erhöht 1 Zeile, beide Teil B) [iqb-Katalog]: Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen (2, E1). Muster: der Pool prüft das Thema selten und nur als „genau k“ über Teilmengen-Quotienten (Probepackungen 2023, Lastenrad-Kinder 2024, je drei Punkte, Anforderungsbereich I bis II) – die Landeshefte prüfen es häufiger als der Pool (Gegenstück zur üblichen Poolbindung des Bündels). Amtlicher Anforderungsbereich in beiden Zeilen (höchster Bereich: I 1, II 1); Niveau II 2. Keine Dubletten.
68  Zielmarke: Einheit 1 – abi: die Auslosung mit Gegenereignis und Modellbegründung (2017-bb-ea-B4.2e, Niveau II) und die Urne in Teil A (2022-bebb-gk-A1.6a, Niveau I); iqb: der Teilmengen-Nachweis (2024MerhoehtBStochastikWTR2-1e, Niveau II). Einheit 2 – abi: die Schrankenaufgabe (2023-bebb-lk-B4l, Niveau II).
````

## 2 Originale (4)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2022-bebb-gk-A1.6a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Urne mit vier roten und zwei grünen Kugeln; drei Kugeln werden ohne Zurücklegen gezogen
- gesucht: Wahrscheinlichkeit, dass mindestens eine gezogene Kugel grün ist
- verfahren: 1 − P(alle rot)
- fehlerquelle: mit Zurücklegen rechnen (1 − (2/3)³)

### 2017-bb-ea-B4.2e (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 4 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: An der Lesung nehmen 174 Besucher teil, darunter ein Deutschkurs und dessen Lehrerin. Aus den Teilnehmern werden fünf Personen ausgelost, die je eine Freikarte für die nächste Veranstaltung erhalten.
- gesucht: Wahrscheinlichkeit dafür, dass die Lehrerin unter den fünf Gewinnern ist; Begründung, dass das Modell der Binomialverteilung dafür ungeeignet ist
- verfahren: Ziehen ohne Zurücklegen: über das Gegenereignis P = 1 − C(173; 5)/C(174; 5) = 1 − 169/174, gleichwertig zur Überlegung, dass jede der 174 Personen dieselbe Chance hat, unter den fünf Gezogenen zu sein. Die Binomialverteilung setzt unabhängige Wiederholungen mit gleichbleibender Trefferwahrscheinlichkeit voraus.
- fehlerquelle: mit fünf unabhängigen Zügen und der festen Wahrscheinlichkeit 1/174 rechnen

### 2024MerhoehtBStochastikWTR2-1e (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: 80 Kinder, 12 davon mit Lastenrad gebracht; 10 zufällig ausgewählt
- gesucht: Nachweis P(genau zwei mit Lastenrad) ≈ 29,6 %
- verfahren: günstige durch mögliche Teilmengen
- fehlerquelle: binomial mit p = 0,15 rechnen (≈ 27,6 %)

### 2023-bebb-lk-B4l (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 4 · format Rechnung · antwort Zahl
- gegeben: 30 Personen, 12 weiblich, 5 ausgewählt; P(höchstens n weiblich) < 35 %
- gesucht: größtmögliches n
- verfahren: Kumulierte hypergeometrische Wahrscheinlichkeiten aufsummieren, bis 0,35 überschritten wird
- fehlerquelle: Binomialverteilung verwenden; n = 2 wegen P(Y = 2) < 0,35 angeben

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2023MgrundlegendBStochastikWTR1-1b, 2018-bb-ea-B4.1d, 2023-bebb-lk-B4k

## 3 Maßstab (unterrichtsblatt.md, wortgleich)

### 2.2

````text
2.2 Zone „kennst du schon" – die Voraussetzungen, eine Stufe
zurück. Zweck: ins Thema hineinführen, sehen, ob der Schüler so
weit ist, an Vergessenes erinnern. Die Zone lehrt nichts Neues
und nennt keinen Begriff des Themas. Sie ist auf der Zeitachse
die Zone hinter dem Schüler, kein eigenes Blatt; bereitgestellt
wird sie trotzdem zuerst als eigenes PDF (2.7). Untertitel auf
dem Blatt: „Das kennst du schon". Hängt der Schüler hier, ist
die Lücke älter als das Thema – das zeigt das Blatt durch die
Zone selbst, ohne Kennzeichnung.
- Je Fertigkeit des Abschnitts eine Hauptnummer mit eigener
  Anweisung; Titel ist die Fertigkeit als Ich-kann-Satz mit dem
  Wort, das die Klasse kennt („Ich kann die Nullstelle einer
  Geraden berechnen", nicht „wo eine Gerade die x-Achse
  schneidet"). Die Nummern der Zone sind die ersten Nummern des
  Blatts (1, 2, 3 …), keine eigene Zählung (Z1) und kein
  Neubeginn im Lernblatt; die Nummer ist die Adresse.
- Breite nach Bestellung (1.1): mit Wiederholung alle
  Fertigkeiten, die das Lernblatt braucht, dazu die Zweige des
  Themas, die die Zeitmarke vor die Eingabeklasse legt, als je
  eine Fertigkeit mit dem Grundfall des Zweigs; „wiederholung
  kurz" je Fertigkeit eine leichte und eine Fallstrick-
  Teilaufgabe; „nur das neue" keine Zone.
- Reihenfolge nach erster Verwendung im Lernblatt: die Angabe
  „– Einheit n" der Fertigkeitszeile, kleinste Einheit zuerst;
  bei gleicher Einheit die Lehrplanfolge der Voraussetzungs-
  themen; ohne Angabe die Reihenfolge des Eintrags. Innerhalb
  der Hauptnummer leicht → Fallstrick.
- Je Fertigkeit: zwei sehr leichte Teilaufgaben (im Kopf lösbar),
  eine mittlere (negative Zahl, Dezimalzahl, Bruch, Einheit) und
  je eine für jeden Fallstrick der Fertigkeit, an dem das
  Lernblatt hängt. Du planst rückwärts: erst die Stellen des
  Lernblatts, die die Fertigkeit brauchen, daraus die
  Fallstricke. Eine Fertigkeit, die das Lernblatt nirgends
  braucht, entfällt – auch eine, die nur ein abgewählter Zweig
  gebraucht hätte. Dazu einmal je Zone eine Fehler-finden-
  Aufgabe zum häufigsten Fallstrick, unmittelbar darauf als
  eigene Hauptnummer eine gleichartige zum selbst Rechnen – das
  Paar gibt es nur in der Zone (2.3 c).
- Schreibform aus dem Eintrag: Nennt die Fertigkeitszeile eine
  Form (Tabelle, Dreisatz, Streifen), setzt du sie; ein Dreisatz
  steht im zweispaltigen Schema mit den Operationen am Pfeil, nie
  als Zeile mit Doppelpunkt (3.2). Die Zahlen eines Dreisatzes
  der Zone sind so gewählt, dass beide Schritte im Kopf gehen:
  glatter Teiler, Produkt ohne Übertrag (4 Hefte 6 €; nicht 3 m
  7,50 €). Schriftliche Multiplikation ist keine Fertigkeit der
  Zone, sondern ein eigenes Thema.
- Kein Kasten, keine Stufenmarkierung, keine Prüfungshöhe: die
  Zone hat keine Decke.
- Lösungen in der Lösungsdatei (3.4), dazu die Zeile, welche
  Hauptnummer welchen Zweig trägt („1–2 → Einheit 1 und 2 ·
  3 → Einheit 3").
Beim Fokus trägt die Zone nur die Fertigkeiten, die der Typ
braucht, je zwei Teilaufgaben, als erste Seite des Fokus.
````

### 2.3 c

````text
c) Pflichtelemente je Zweig, aus den Typen des Zweigs: Fehler
   finden – Muster aus „Typische Fehler", eigene Zahlen, in der
   Schreibform des Verfahrens (bei Umformungen senkrecht mit
   `\rechnung`), Fehler benennen und korrigieren; Begründen
   oder Entscheiden ohne Rechnung; Darstellungswechsel in beide
   Richtungen, soweit die Typen es tragen; eine Anwendung, deren
   Mathematik vom Kontext getragen wird (realistische Größen, im
   Kontext sinnvolle Frage). Typen des Zweigs, die in keiner
   Kette stehen (Ordnen, Ergänzen, Aussagen prüfen, Umkehrung),
   bekommen eine eigene Hauptnummer. Gemischte Aufgaben, deren
   Punkt die Zuordnung ist („erst zuordnen, dann rechnen"),
   verraten das Verfahren nicht.

   Eine Hauptnummer, eine Fertigkeit, eine Antwortform: Nach
   „Ich finde den Fehler" folgt in derselben Nummer keine
   Rechenaufgabe; Ankreuzen und Begründen stehen nicht in
   derselben Nummer; wechselt die Anweisung so, dass eine andere
   Fertigkeit gefragt ist, beginnt eine neue Hauptnummer. Die
   Zone ist die Ausnahme mit ihrem Paar aus Fehler finden und
   gleichartiger Rechenaufgabe (2.2), und dort sind es zwei
   Nummern.
````

### 2.4 b–c

````text
b) Die Kette. Maßstab ist das strukturelle Merkmal, nicht die
   Stückzahl: Ein Merkmal ist ein Fall, der eine andere
   Entscheidung oder einen anderen Schritt verlangt – anderer
   gegebener Wert, andere Einheit, Dezimalzahl oder Bruch statt
   ganzer Zahl, negatives Vorzeichen, Sonderfall, typischer
   Fallstrick, Umkehrung des Verfahrens. Die Sprossen kommen aus
   dem Eintrag; fehlt zwischen zwei Sprossen ein Schritt, den die
   Prüfungshöhe verlangt, schließt du ihn mit einer Zwischen-
   sprosse und sagst es im Ausgabeblock. Zwei Teilaufgaben, die
   sich nur in den Zahlen unterscheiden, sind dieselbe Sprosse
   und kommen nur beim Grundfall vor. Aufwandsmerkmale (Rundung,
   krumme Zahlen) kommen nach allen Strukturmerkmalen, nie
   zwischen die glatten Fälle. Ein Schüler, der das Thema gerade
   beginnt, schafft die ersten sechs Teilaufgaben jeder
   Verfahrens-Hauptnummer, ohne die Sprossen ab der Mitte zu
   können. Ablesetypen zählen als Verfahrenstypen, die Grafik ist
   nur der Träger: mehrere Objekte je Grafik, höchstens zwei
   Grafiken je Hauptnummer. Aufwandsintensive Typen (Wertetabelle,
   Zeichnen, Konstruktion): mindestens drei Teilaufgaben, die
   erste sehr leicht. Konzept- und Kontexttypen (Begründen,
   Entscheiden, Fehler finden, Textaufgaben mit einer Situation):
   eine bis drei Teilaufgaben, gestuft wie in einer Prüfung –
   Vorbereitungsschritt, Rechnung, Deutung; bei Begründen erst der
   klare Fall, dann der subtile. Bei Entscheidungstypen mit
   Ja/Nein-Antwort liegen richtig und falsch etwa halbe-halbe in
   gemischter Reihenfolge.

c) Prüfungshöhe. Jede Verfahrens-Hauptnummer endet mit genau einer
   Teilaufgabe in Form und Anspruch der zentralen Prüfung nach 1.5
   (P10, Abitur Teil A oder B, FHR). Nennt der Eintrag für die
   Einheit ein Original, ist das die Teilaufgabe – verfremdet, mit
   Jahr (3.6); sie darf eingeführte Merkmale kombinieren, führt
   aber kein neues ein. Zerfällt die Einheit in mehrere Haupt-
   nummern, trägt die letzte das Original, die anderen enden auf
   ihrer höchsten Sprosse. Prüfungsniveau wird in einer Stunde
   nicht erreicht; die Aufgabe ist Zielmarke und bleibt stehen.
   Trägt der Zweig „keine P10-Aufgabe", ist die Decke die
   Prüfungsaufgabe, in der er gebraucht wird, sonst die
   Lehrwerk-Konvention (1.5).
````

### 3.6

````text
3.6 Zahlen, Verfremdung, Formulierung. Zahlenwerte so gewählt,
dass Ergebnisse endlich sind und leichte Aufgaben im Kopf
rechenbar; periodische Dezimalbrüche tragen einen Hinweis. Keine
Aufgabe erscheint doppelt. Keine ganze Gleichung, kein Term,
kein Zahlenpaar und keine Funktion aus Kasten, Beispiel oder
Original des Eintrags in einer Teilaufgabe (2.1). Verfremdetes
Original: gleiches Verfahren, gleiche Falle, gleiche Form
(Ankreuzen, Lückensatz, Rechnung mit Rundung), andere Zahlen,
anderer Kontext; am Ende des Aufgabentexts in Klammern Prüfung,
Jahr und Papier, wie der Eintrag es nennt: „(P10 2018 FOR)",
„(P10 2025 GYM)", „(Abitur 2022 GK)", „(FHR 2024)".
Formulierungen eindeutig. Buchstaben und Symbole, die im Aufgaben-
text nicht erklärt sind, werden nicht verwendet, auch nicht T für
Term oder L für Lösungsmenge. Ein Buchstabe steht auf einem Blatt
für genau eine Sache: Seitenlabels verschiedener Figuren und
Variablen in Textaufgaben überschneiden sich nicht.
````

# Mappe: kombinatorik

Eintrag: hz-0801/mathe-nachhilfe, katalog/kombinatorik.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:08 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Kombinatorik
 3
 4  ### Verortung
 5  Das Zählen der Oberstufe: das Zählprinzip und seine Umkehrung, Anordnungen (Permutationen ohne und mit Wiederholung), geordnete Auswahlen (Variationen mit Wiederholung als Potenz, ohne Wiederholung al … (gekürzt, 2684 Zeichen)
 6  [GOST] Q2, 2. Kurshalbjahr „Analysis; Stochastik“ (BB S. 26), Grund- und Leistungskursfach: L5-Zeile „Anwendungssituationen mithilfe von Urnenmodellen untersuchen“ mit dem Inhalt „kombinatorische Abzä … (gekürzt, 3613 Zeichen)
 7  [FOS] Kap. 3 Leitidee L5 (S. 24, Zeilen 998–1009): „In Ausweitung und Vertiefung stochastischer Vorstellungen der Sekundarstufe I umfasst diese Leitidee insbesondere den Umgang mit mehrstufigen Zufall … (gekürzt, 1648 Zeichen)
 8  [LS-AA] Qualifikationsphase Kapitel VIII „Grundlagen der Wahrscheinlichkeitsrechnung“: 1 Elementare Kombinatorik (Zeilen 1567 und 1763 der Textfassung) – die einzige Lerneinheit des Lehrwerks zum Them … (gekürzt, 1836 Zeichen)
 9
10  ### Lerneinheiten
11  1. Zählprinzip und Anordnungen – das Produkt der Wahlmöglichkeiten bei mehrteiligen Zusammenstellungen und seine Umkehrung (fehlende Anzahl durch Division), Permutationen ohne Wiederholung als Fakultä … (gekürzt, 825 Zeichen)
12    Marken: BE Q2 · BB Q2 · GK · Abitur LK · FHR
13  2. Auswahlen und Binomialkoeffizient – (n über k) als Anzahl der Auswahlen ohne Reihenfolge (Rechnertaste nCr, Formel mit Fakultäten, kleine Werte im Kopf), die Eigenschaften der Anlage und die Symmet … (gekürzt, 791 Zeichen)
14    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK · FHR
15  3. Zählen mit Bedingungen und Wahrscheinlichkeitsterme – systematisches Aufzählen unter einer Bedingung (Abstand, „nicht nacheinander“) mit Begründung der Vollständigkeit, Muster mal Anordnungen inner … (gekürzt, 872 Zeichen)
16    Marken: BE Q2 · BB Q2 · GK · Abitur GK
17  Warum drei: Die Rohdatei trägt 32 Zeilen in 18 Haupttypen; Anlage und RLP FOS gliedern nach Permutation, Variation und Kombination – die Einheiten 1 und 2 folgen dieser Gliederung mit der Trennung „Re … (gekürzt, 1176 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; fhr-Typen wörtlich aus fhr/fhr-typen.csv, abitur-Typen aus abitur/abitur-typen.csv (das Thema Kombinatorik trägt keine Gegenstandsklasse, daher kein Präfix). Nebentypen der Rohdatei sind nicht zugeordnet.
21  Einheit 1: Permutation ohne Wiederholung berechnen (2; fhr) · Anzahl geordneter Auswahlen ohne Wiederholung berechnen (1) · Anzahl über das Zählprinzip berechnen (1; fhr) · Fehlende Anzahl aus der Gesamtzahl der Möglichkeiten bestimmen (1; fhr) · Permutation mit Wiederholung berechnen (1; fhr) — Nachweis: Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen (2; Operator „Zeigen Sie“, Ermessen, siehe Offene Punkte) — kein Deutungstyp. Dazu: Fehler finden (Fakultät statt Potenz, wo jede Kette mehrfach vergeben werden darf; nur die Fakultät der Gesamtzahl genommen und die gleichartigen Gruppen nicht herausdividiert; Produkt statt Potenz bei Zeichenfolgen mit Wiederholung; die Grundmenge falsch – alle Gäste statt der Kinder; durch die Summe statt durch das Produkt der bekannten Anzahlen geteilt; den Binomialkoeffizienten genommen, obwohl die Reihenfolge festgelegt wird) · Begründen (warum eine Anordnung jede Reihenfolge zählt und deshalb die Fakultät entsteht; warum bei Wiederholung die Zahl der Möglichkeiten je Platz gleich bleibt und eine Potenz entsteht).
22  Einheit 2: Kombination ohne Wiederholung berechnen (9; fhr) · Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen (2) · Anzahl ungeordneter Auswahlen ohne Wiederholung über den Binomialkoeffizienten berechnen (2; Ermessen, siehe Offene Punkte) · Anzahl der Kombinationen aus zwei getrennten Auswahlgruppen ermitteln (1) · Anzahl der Zahlenkombinationen mit einer vierfachen Ziffer aus drei Ziffern berechnen (1) · Kombination mit Wiederholung berechnen (1; fhr) — kein Nachweistyp — Deutung: Faktoren eines kombinatorischen Terms im Sachzusammenhang deuten (1). Dazu: Fehler finden (die Reihenfolge mitgezählt und eine Variation statt des Binomialkoeffizienten gerechnet – der häufigste Fehler des Themas; bei der Kombination mit Wiederholung die Potenz genommen; die Reihenfolge der beiden übrigen Ziffern vergessen; Wiederholung der Zusatzzeichen zugelassen oder die festen Buchstaben nicht ausgeschlossen; bei getrennten Gruppen die Fälle multipliziert statt addiert; einen Faktor des Terms als Restanzahl gedeutet) · Begründen (warum (n über k) gleich (n über n − k) ist – auswählen heißt liegen lassen; warum Auswahl mal Anordnung dasselbe ergibt wie die geordnete Auswahl).
23  Einheit 3: Anzahl der Sitzordnungen mit Abstandsbedingung berechnen (3) · Anzahl der Zusammensetzungen mit Mengenbedingungen je Sorte bestimmen (1) · Kleinstes n, für das die Wahrscheinlichkeit lauter verschiedener Ergebnisse unter eine Schranke fällt, ermitteln (1) — kein Nachweistyp — Deutung: Auswahlen mit Abstandsbedingung aufzählen (2) · Term für das Gegenereignis einer festen Häufigkeitsverteilung bei mehreren Würfen angeben (1) · Term für die Wahrscheinlichkeit aufstellen, dass jede Zahl mindestens einmal fällt (1). Dazu: Fehler finden (eine Auswahl vergessen, weil immer mit dem ersten Platz begonnen wurde, oder eine benachbarte mitgezählt; die Muster gezählt und die Anordnungen der Personen oder Lieder vergessen; die Zuordnungen einer Zerlegung vergessen oder die Sorten als Potenz gezählt; die Anordnungen im Term weggelassen oder die Fakultät statt des Binomialkoeffizienten genommen; die Binomialverteilung für eine einzelne Zahl angesetzt, wo alle Zahlen zugleich verteilt sind; die Zahl der Folgen ohne Wiederholung als Potenz minus n geschrieben) · Begründen (warum die Muster erst aufgezählt und dann multipliziert werden; warum „jede Zahl mindestens einmal“ bei einem Wurf mehr als Zahlen genau eine Wiederholung heißt).
24  Zählung: 6 + 7 + 6 = 19 Haupttypen, 8 + 17 + 9 = 34 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27.09.2026: Heft 2017-be-gk und Pool 2017 grundlegend Teil B).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür; der Sek-I-Eintrag wird verwiesen, nicht wiederholt):
28  - Möglichkeiten vollständig aufzählen (Liste, Tabelle, Baum ohne Wahrscheinlichkeiten), Zählprinzip „mal“ bei zwei Auswahlen, Anordnungen einer kleinen Menge auflisten und als Produkt zählen, Ergebnismenge als geordnete Paare – alle Einheiten; Einheit 3 setzt das geordnete Aufzählen mit Begründung der Vollständigkeit voraus. Sek-I-Thema wahrscheinlichkeit.md Einheit 1. [RLP D/E „systematisches Durcharbeiten und Begründen der Vollständigkeit einer Lösung zu kombinatorischen Fragestellungen“; GOST Eingangsvoraussetzung L5; LISUM-PH Block „Kombinatorik / Anzahl an Möglichkeiten bestimmen“ (systematisches Aufschreiben von Anordnungen, Produktregel)]
29  - Potenzen mit natürlichen Exponenten, Produkte großer Zahlen mit dem Rechner, Ergebnisse in Zehnerpotenzschreibweise lesen und angeben, die Rechnertasten für Fakultät und Binomialkoeffizient (n!, nCr; gerätabhängig) – Einheit 1 und 2. Sek-I-Thema potenzen-wurzeln.md Einheit 1 und 2. [GOST Eingangsvoraussetzung L1 „Zehnerpotenzschreibweise“; Rohdatei: Ergebnisse als Zehnerpotenz in fhr 2023-A-3f, 2026-B-3e, 2021-B-3a]
30  - Brüche und Quotienten kürzen (Fakultätenquotienten, Anteile aus zwei Anzahlen), Anteil als Dezimalzahl und Prozent, Vergleich mit einer Schranke – Einheit 1 (Potenzquotient), Einheit 2 (Formel des Binomialkoeffizienten) und Einheit 3 (Terme, Schranke). Sek-I-Themen bruchrechnung.md, brueche-dezimalzahlen.md, prozentrechnung.md. [GOST Eingangsvoraussetzung L1 „Brüche, Dezimalzahlen, Prozentzahlen“; RLP D]
31  - Pfadregeln: die feste Ergebnisfolge als Produkt, das Gegenereignis als eins minus, „ein Pfad mal Anzahl der Reihenfolgen“ – Einheit 3 (die Anzahl steht als Faktor im Term). Sek-II-Nachbarthema zufallsexperimente-und-pfadregeln.md Einheit 3 und 5 (dort die Anwendung, hier die Anzahl); Sek-I-Thema wahrscheinlichkeit.md Einheit 3. [GOST Eingangsvoraussetzung L5 „Baumdiagrammen sowie Pfadregeln“; GOST-OHiMi 2.4 Pfadregeln]
32  - Werte einer Folge mit dem Rechner berechnen und gegen eine Schranke prüfen (beide Nachbarwerte belegen) – Einheit 3 (kleinstes n). Sek-II-Nachbarthema binomialverteilung.md Einheit 4 (dieselbe Arbeitsregel beim Probieren mit Nachbarwerten). [Rohdatei; iqb 2023MerhoehtBStochastikWTR3-3]
33  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt): keine eigenen – seit 27.09.2026 gestrichen, weil die Vorstufen der Ketten denselben Handgriff verlangen.
34
35  ### Merkkasten
36  Einheit 1 (Zählprinzip und Anordnungen):
37      Zählprinzip: wird eine Zusammenstellung Teil für Teil gewählt, ist die Zahl der Möglichkeiten das Produkt der Wahlmöglichkeiten je Teil; fehlt ein Faktor, liefert ihn die Division durch die übrigen.
38        Sechs Vorspeisen und fünfzehn Hauptgänge: 6 · 15 = 90 Menüs; mit Getränk 720 Möglichkeiten, also 720 : 90 = 8 Getränke.
39      Permutation ohne Wiederholung: n verschiedene Dinge in eine Reihe – n! = n · (n − 1) · … · 1 Anordnungen (0! = 1, 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720).
40        Sieben verschiedene Ketten an sieben Freundinnen, jede genau eine: 7! = 5040.
41      Permutation mit Wiederholung: sind darunter Gruppen gleicher Dinge, teilt man die Fakultät der Gesamtzahl durch die Fakultäten der Gruppen – Vertauschungen innerhalb einer Gruppe ändern die Reihe nicht.
42        Kette aus dreißig Streuern, drei Sorten zu je zehn: 30! / (10! · 10! · 10!) ≈ 5,55 · 10¹².
43      Variation mit Wiederholung: k Plätze, an jedem alle n Zeichen erlaubt – n^k Folgen; der Anteil einer Zeichen-Teilmenge ist ein Quotient zweier Potenzen.
44        Kennwort aus acht von achtzig Zeichen: 80⁸ Möglichkeiten; nur Kleinbuchstaben 26⁸, Anteil (26/80)⁸ ≈ 0,00012.
45      Variation ohne Wiederholung: k Plätze nacheinander aus n verschiedenen Dingen besetzen, jedes höchstens einmal – n · (n − 1) · … · (n − k + 1) = n! / (n − k)!.
46        Drei von fünf Röstgraden in festgelegter Reihenfolge: 5 · 4 · 3 = 60.
47      Auswendig (Teil A): Zählprinzip, n! mit der Fakultät bis sechs und n^k – [GOST-OHiMi 2.4] „Permutationen ohne Wiederholung: n!“ mit „Berechnung der Fakultät für n ≤ 6“ und „Variationen mit Wiederholung: n^k“; Permutation mit Wiederholung und Variation ohne Wiederholung stehen nicht in der Anlage (fhr-Formen mit Hilfsmitteln; der Pool prüft sie nur in Teil B, 2023MgrundlegendBStochastikWTR1-1a) – keine Teil-A-Zeile in dieser Einheit, die Anlage verlangt den Kern trotzdem.
48      Formelsammlung: [FS-IQB 1.4] führt weder die Fakultät noch eine Permutations- oder Variationsformel, nur den Binomialkoeffizienten (Kasten 2) – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
49  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] Kombinatorik und [FOS Pflichtthema 4] „Permutationen, Kombinationen, Variationen (jeweils mit und ohne Wiederholung)“; Zahlenbeispiele aus fhr 2021-B-3a und 2021-B-3b (Zählprinzip), 2020-A-3e (Fakultät), 2026-B-3e (mit Wiederholung), abi 2024-bebb-lk-B4g (Potenzquotient) und iqb 2023MgrundlegendBStochastikWTR1-1a (geordnete Auswahl); [LS-AA QP VIII 1].
50
51  Einheit 2 (Auswahlen und Binomialkoeffizient):
52      Binomialkoeffizient: (n über k) zählt die Auswahlen von k aus n ohne Reihenfolge – Rechnertaste nCr, Formel (n über k) = n! / (k! · (n − k)!): die geordneten Auswahlen, geteilt durch die k! Reihenfolgen innerhalb einer Auswahl.
53        Vier von sieben Kugeln: (7 über 4) = 35; drei von fünf Farben: (5 über 3) = 10.
54      Eigenschaften: (n über 0) = (n über n) = 1, (n über 1) = (n über n − 1) = n, (n über k) = (n über n − k) – zwei aus sieben auswählen heißt fünf aus sieben liegen lassen: (7 über 2) = (7 über 5) = 21.
55      Auswahl, dann Anordnung: erst die Gruppe ohne Reihenfolge, dann ihre Reihenfolge – Binomialkoeffizient mal Fakultät. Fünf von zehn Sorten und ihre Verteilung auf fünf Tage: (10 über 5) = 252 und 5! = 120.
56      Plätze wählen: wo Dinge gleich sind, wählt der Binomialkoeffizient ihre Plätze, die übrigen Plätze werden dann besetzt – zwei Zusatzzeichen in einem Kennwort aus acht Stellen: (8 über 2) Lagen mal 74 · 73 Zeichen = 151 256; eine vierfache Ziffer aus drei Ziffern auf sechs Stellen: 3 · (6 über 2) · 2 = 90.
57      Getrennte Gruppen: wird aus mehreren Gruppen unabhängig gewählt, multipliziert man die Anzahlen und addiert die Fälle – zwei von drei Landschaften und ein oder zwei von zwei Tieren: (3 über 2) · (2 + 1) = 9.
58      Mit Wiederholung: k Dinge aus n Sorten ohne Reihenfolge, Sorten dürfen mehrfach – (n + k − 1 über k). Fünf Streuer aus drei Sorten: (7 über 5) = 21.
59      Term deuten: jeder Faktor eines Anzahlterms ist eine Wahl – (3 über 2) · 14: zwei der drei Farben wählen, dann die Anzahl der ersten Farbe unter vierzehn Möglichkeiten.
60      Auswendig (Teil A): (n über k) als Anzahl der Auswahlen mit den Eigenschaften und kleinen Werten im Kopf, Auswahl-dann-Anordnung, Plätze wählen – [GOST-OHiMi 2.4] „Kombinationen ohne Wiederholung: (n über k)“ mit Eigenschaften; [IQB-VER 4] setzt den Binomialkoeffizienten voraus; Teil-A-Beleg 2020MerhoehtAStochastik22-a (Termdeutung). Große Binomialkoeffizienten, die Formel mit Fakultäten und die Kombination mit Wiederholung sind Rechnerarbeit ([FS-IQB 1.4] in Teil B; fhr mit Hilfsmitteln).
61      Formelsammlung: [FS-IQB 1.4] Binomialkoeffizient (n über k) = n! / (k! · (n − k)!) – der einzige kombinatorische Eintrag der Formelsammlung; Eigenschaften und (n + k − 1 über k) stehen nicht darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
62  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] und [FS-IQB 1.4]; Zahlenbeispiele aus fhr 2023-C-3d, 2021-A-3c, 2020-A-3d, 2019-A-3d und 2026-B-3d, iqb 2024MerhoehtBStochastikWTR1-3b, 2022MerhoehtBStochastikWTR2-2, 2025MgrundlegendBStochastikWTR2-1e und 2020MerhoehtAStochastik22-a; [LS-AA EP V 2, QP VIII 1].
63
64  Einheit 3 (Zählen mit Bedingungen und Wahrscheinlichkeitsterme):
65      Aufzählen mit System: bei einer Bedingung (Abstand, „nicht nacheinander“) erst alle zulässigen Muster aufschreiben – geordnet nach dem ersten Element, damit keines fehlt –, dann zählen. Drei von sechs Stühlen mit mindestens einem freien dazwischen: 1-3-5, 1-3-6, 1-4-6, 2-4-6 – vier Muster.
66      Muster mal Anordnungen: sind die Personen oder Dinge unterscheidbar, wird jedes Muster mit den Anordnungen innerhalb der Sorten multipliziert. Drei Schüler auf die vier Stuhlmuster: 4 · 3! = 24; fünf Lieder, zwei kurze nie nacheinander: sechs Muster mal 2! · 3! = 72.
67      Zerlegen mit Grenzen: eine feste Gesamtzahl auf Sorten mit Unter- und Obergrenze – die zulässigen Zerlegungen aufzählen und je Zerlegung die Zuordnungen zählen. Fünfzehn Tulpen in drei Farben, je Farbe vier bis sechs: 5 + 5 + 5 einmal, 4 + 5 + 6 in 3! = 6 Zuordnungen – zusammen 7.
68      Anzahl im Wahrscheinlichkeitsterm: lauter verschiedene Ergebnisse bei n Zügen aus n Möglichkeiten haben die Wahrscheinlichkeit n! / nⁿ (günstige Folgen durch alle Folgen); „jede Zahl mindestens einmal“ bei einem Wurf mehr als Zahlen heißt genau eine Wiederholung – Lagen des Paars mal Pfadwahrscheinlichkeit; eine feste Häufigkeitsverteilung zählt ihre Anordnungen als Produkt von Binomialkoeffizienten, ihr Gegenereignis ist eins minus.
69        Motive: 6! / 6⁶ ≈ 0,015 und 7! / 7⁷ ≈ 0,006 – ab n = 7 unter einem Prozent. Tetraeder fünfmal, jede Zahl mindestens einmal: (5 über 2) · 1 · 1/4 · 3/4 · 2/4 · 1/4 = 15/64. Jede Zahl genau zweimal bei sechs Würfen mit drei Zahlen: (6 über 2) · (4 über 2) · (1/3)⁶ = 10/81, Gegenereignis 71/81.
70      Auswendig (Teil A): der ganze Kasten bis auf die Schrankensuche – die Prüfform des Pools: sieben der neun Zeilen dieser Einheit sind hilfsmittelfrei (2024MgrundlegendAStochastik13-a, 2024MgrundlegendAStochastik13-b, 2020MerhoehtAStochastik22-b, 2022MerhoehtAStochastik22-b, 2023MerhoehtAStochastik21-b und die beiden Landesdubletten); inhaltlich sind es [GOST-OHiMi 2.4] Kombinatorik und Pfadregeln zusammen; die Schrankensuche (kleinstes n) ist Rechnerarbeit (2023MerhoehtBStochastikWTR3-3, Teil B).
71      Formelsammlung: keine – Zählstrategien stehen in keiner Formelsammlung; für die Terme hilft [FS-IQB 1.4] nur mit dem Binomialkoeffizienten – [FS] offen
72  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] und [RLP E] „systematisches Durcharbeiten und Begründen der Vollständigkeit einer Lösung zu kombinatorischen Fragestellungen“; Zahlenbeispiele aus iqb 2024MgrundlegendAStochastik13-a, 2024MgrundlegendAStochastik13-b, 2026MgrundlegendBStochastikWTR2-1f, 2020MerhoehtAStochastik22-b, 2023MerhoehtBStochastikWTR3-3, 2023MerhoehtAStochastik21-b und 2022MerhoehtAStochastik22-b; ohne Lehrwerkskapitel (Ermessen).
73
74  ### Typische Fehler
75  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 32 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet; die Muster sind allein aus den Katalogzeilen belegt.
76  - Reihenfolge mitgezählt, wo sie nicht zählt: für eine Auswahl ohne Reihenfolge eine Variation gerechnet (das fallende Produkt statt des Binomialkoeffizienten – doppelt so viele Hauptgangpaare, sechsmal so viele Farbauswahlen), Auswahl und Anordnung vermischt; bei der Kombination mit Wiederholung die Potenz genommen – das häufigste Muster des Themas, in elf der fünfzehn fhr-Zeilen die dokumentierte Fehlerquelle. [fhr 2025-C-3d, 2025-A-3a, 2024-B-3c, 2023-C-3d, 2023-A-3c, 2022-C-3a, 2021-B-3a, 2021-A-3c, 2020-A-3d, 2019-A-3d, 2026-B-3d]
77  - Reihenfolge vergessen, wo sie zählt: den Binomialkoeffizienten genommen, obwohl die Reihenfolge festgelegt wird; die Muster gezählt und die Anordnungen der Schüler oder Lieder darauf nicht mehr multipliziert (vier statt vierundzwanzig, sechs statt zweiundsiebzig); den Faktor für die Reihenfolge der beiden übrigen Ziffern oder die Zuordnungen einer Zerlegung vergessen; im Wahrscheinlichkeitsterm die Anordnungen weggelassen oder die volle Fakultät statt des Binomialkoeffizienten der Paarlagen genommen; ein Ergebnis ohne Begründung hingeschrieben. [iqb 2023MgrundlegendBStochastikWTR1-1a, 2024MgrundlegendAStochastik13-b, 2026MgrundlegendBStochastikWTR2-1f, 2022MerhoehtBStochastikWTR2-2, 2020MerhoehtAStochastik22-b, 2023MerhoehtAStochastik21-b; abi 2024-bebb-gk-A1.3b]
78  - Gleichartiges nicht herausgerechnet, Mehrfachvergabe übersehen: nur die Fakultät der Gesamtzahl angegeben und die gleichen Streuer je Sorte nicht herausdividiert; mit der Fakultät statt mit der Potenz gerechnet, weil jede Freundin mehrere Ketten bekommen darf. [fhr 2026-B-3e, 2020-A-3e]
79  - Potenz und Produkt verwechselt: bei Zeichenfolgen mit Wiederholung Anzahl mal Länge statt Anzahl hoch Länge; Wiederholung der Zusatzzeichen zugelassen (Quadrat statt fallendes Produkt) oder die festen Buchstaben nicht aus der Zeichenwahl ausgeschlossen. [abi 2024-bebb-lk-B4g, 2024-bebb-lk-B4h; iqb 2024MerhoehtBStochastikWTR1-3a, 2024MerhoehtBStochastikWTR1-3b]
80  - Grundmenge oder Zählmodell falsch: mit allen Gästen statt mit den Kindern gerechnet; durch die Summe statt durch das Produkt der bekannten Anzahlen geteilt; bei getrennten Gruppen die Fälle multipliziert statt addiert (ein Tier zweimal); die Zahl der Folgen ohne Wiederholung als Potenz minus n angesetzt. [fhr 2023-A-3f, 2021-B-3b; iqb 2025MgrundlegendBStochastikWTR2-1e, 2023MerhoehtBStochastikWTR3-3]
81  - Aufzählen unvollständig oder Bedingung verletzt: eine zulässige Auswahl vergessen, weil immer mit dem ersten Stuhl begonnen wurde; eine Auswahl mit benachbarten Stühlen mitgezählt. [iqb 2024MgrundlegendAStochastik13-a; abi 2024-bebb-gk-A1.3a]
82  - Term oder Modell falsch gedeutet: einen Faktor als Anzahl der übrigen Tulpen statt als Anzahl der Aufteilungen gelesen; die Binomialverteilung für eine einzelne Zahl angesetzt, wo alle Zahlen zugleich eine feste Häufigkeit haben. [iqb 2020MerhoehtAStochastik22-a, 2022MerhoehtAStochastik22-b]
83
84  ### Für schwache Schüler
85  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q2 Brandenburg und Berlin (Grund- und Leistungskursfach, kein LK-Zusatz): „kombinatorische Abzählverfahren“ ohne Aufzählung der Verfahren – die Anlage konkretisiert sie: Einheit 1 mit n! (Fakultät bis sechs) und n^k, Einheit 2 mit (n über k) samt Eigenschaften (Anlage OHiMi 2.4, Prüfungsteil A: Kasten 1 ohne die Formen mit Wiederholung und die geordnete Auswahl, Kasten 2 bis zum Plätzewählen). Einführungsphase, Niveaustufe H [RLP H]: „Bestimmen von Anzahlen mithilfe von Fakultäten und Binomialkoeffizienten“ – Einheit 1 und 2 in ihrer Grundform. Einheit 3 nennt kein Plan; sie ist die Prüfform des Pools (sieben von neun Zeilen in Teil A) und damit Mindeststoff der Prüfungsvorbereitung beider Abiturprofile, nicht des Plans (Ermessen, siehe Offene Punkte). Vorrat für den GK (Ermessen nach dem Niveau der Rohdatei): die Zerlegungen mit Grenzen, die Terme mit Produkten von Binomialkoeffizienten und die Schrankensuche – alle erhöht oder Anforderungsbereich III. RLP FOS (fhr): Pflicht- und Prüfstoff sind Einheit 1 und 2 vollständig – „Berechnung von Fakultät und Binomialkoeffizient“, „Permutationen, Kombinationen, Variationen (jeweils mit und ohne Wiederholung)“ – mit der Jahresform „Auswahl, dann Anordnung“; Einheit 3 ist für fhr Vorrat (kein FHR-Heft zählt unter einer Bedingung oder stellt eine Anzahl in einen Wahrscheinlichkeitsterm). COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung unter Stochastik einfache Abzählungen mit Fakultät und Binomialkoeffizient – deckt sich mit den Einheiten 1 und 2, kein zusätzlicher Posten.
86  Grundvorstellung (Blatt 0) [GOST Eingangsvoraussetzung L5, RLP E, MO]: Zählen heißt ordnen, und die Frage vor jeder Formel ist, ob die Reihenfolge zählt. „Anna, Ben und Cem stellen sich an einer Kasse an. Schreibe alle Reihenfolgen auf, in denen sie stehen können – wie viele sind es, und woran siehst du, dass keine fehlt? Jetzt sollen zwei von den dreien ein Team bilden: schreibe alle Teams auf. Warum sind es weniger Teams als Reihenfolgen, obwohl dieselben drei Kinder da sind? Welche deiner Reihenfolgen gehören zum selben Team?“ Wer die Teams „Anna und Ben“ und „Ben und Anna“ doppelt zählt, wer beim Aufzählen ohne Ordnung anfängt und eine Möglichkeit vergisst oder wer Fakultät und Binomialkoeffizient nur als Rechnertasten kennt, braucht das vor jeder Formel: eine Anordnung zählt jede Reihenfolge, eine Auswahl fasst alle Reihenfolgen derselben Gruppe zu einer zusammen – der Binomialkoeffizient ist nichts anderes als „geordnete Auswahlen geteilt durch die Reihenfolgen innerhalb der Auswahl“. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Eingangsvoraussetzung L5 „Binomialkoeffizienten und Fakultäten“, RLP E „systematisches Durcharbeiten und Begründen der Vollständigkeit“), die Aufgabenform Ermessen. [GOST Eingangsvoraussetzung L5; RLP E/H Zählstrategien; LISUM-PH Block „Kombinatorik / Anzahl an Möglichkeiten bestimmen“ (systematisches Aufschreiben von Anordnungen); MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Reihenfolge mitgezählt“ – der häufigste Fehler des Themas, fhr 2021-A-3c, 2023-C-3d; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
87  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, FOS, Rohdatei; Sprossenfolge Ermessen, wo Anlage, RLP FOS und Rohdatei keine Reihenfolge vorgeben]:
88  - Zählprinzip und Anordnungen (Einheit 1): „Zählt die Reihenfolge?“ – ankreuzen, ob eine Anordnung oder geordnete Auswahl gemeint ist (Sitzordnung, Reihenfolge der Gespräche, Kennwort) oder eine Auswahl ohne Reihenfolge (Gruppe, Menü, Farben eines Straußes); „Mit oder ohne Wiederholung?“ – ankreuzen, ob ein Element mehrfach vorkommen darf (Zeichen im Kennwort, Sorten im Streuerpaket, Ketten je Freundin) oder jedes nur einmal (Personen, Plätze, verschiedene Farben); „Mal oder plus?“ – ankreuzen, ob die Teile nacheinander gewählt werden (Produkt) oder Fälle nebeneinander stehen (Summe), und welche Faktoren gleich bleiben; nichts rechnen (Vorstufe, Grundvorstellung) → eine zweiteilige Zusammenstellung als Produkt der Wahlmöglichkeiten zählen (Grundfall, viermal; fhr 2021-B-3a) → die fehlende Anzahl aus der Gesamtzahl durch Division (fhr 2021-B-3b) → Anordnungen einer kleinen Menge als Fakultät, dann große Fakultäten mit dem Rechner und als Zehnerpotenz (fhr 2023-A-3f) → Anordnungen mit gleichartigen Gruppen: die Fakultäten der Gruppen herausdividieren (fhr 2026-B-3e) → Zeichenfolgen mit Wiederholung als Potenz und der Anteil einer Zeichen-Teilmenge als Potenzquotient (abi 2024-bebb-lk-B4g; iqb 2024MerhoehtBStochastikWTR1-3a) → geordnete Auswahl ohne Wiederholung als fallendes Produkt (iqb 2023MgrundlegendBStochastikWTR1-1a) → Prüfungshöhe: dieselben Ketten unter drei Bedingungen verteilen – jede Freundin genau eine, mehrere oder keine, höchstens eine bei mehr Freundinnen als Ketten: Fakultät, Potenz, Fakultätenquotient (fhr 2020-A-3e, sechs Punkte, Niveau III).
89  - Auswahlen und Binomialkoeffizient (Einheit 2): „Zählt die Reihenfolge?“ – ankreuzen, ob eine Anordnung oder geordnete Auswahl gemeint ist (Sitzordnung, Reihenfolge der Gespräche, Kennwort) oder eine Auswahl ohne Reihenfolge (Gruppe, Menü, Farben eines Straußes); „Mit oder ohne Wiederholung?“ – ankreuzen, ob ein Element mehrfach vorkommen darf (Zeichen im Kennwort, Sorten im Streuerpaket, Ketten je Freundin) oder jedes nur einmal (Personen, Plätze, verschiedene Farben); nichts rechnen (Vorstufe) → eine kleine Auswahl ohne Reihenfolge aufzählen und mit dem Binomialkoeffizienten vergleichen (Grundfall, viermal; fhr 2021-A-3c) → große Binomialkoeffizienten mit der Rechnertaste (fhr 2023-A-3c, 2024-B-3c, 2025-A-3a) → zwei Binomialkoeffizienten über die Symmetrie vergleichen (fhr 2020-A-3d) → die fhr-Jahresform: erst die Auswahl ohne Reihenfolge, dann die Anordnung der Ausgewählten (fhr 2019-A-3d, 2022-C-3a, 2023-C-3d, 2025-C-3d) → Auswahlen aus getrennten Gruppen als Produkt mit Fallsumme (iqb 2025MgrundlegendBStochastikWTR2-1e) → Plätze für gleiche Dinge wählen und mit der Besetzung der übrigen Plätze multiplizieren (abi 2024-bebb-lk-B4h; iqb 2024MerhoehtBStochastikWTR1-3b) [Kennung mit Ziffernende, deshalb in der Belegklammer: iqb 2022MerhoehtBStochastikWTR2-2] → die Faktoren eines Anzahlterms im Sachzusammenhang deuten (iqb 2020MerhoehtAStochastik22-a) → Prüfungshöhe: die Kombination mit Wiederholung über den Binomialkoeffizienten von n plus k minus eins über k (fhr 2026-B-3d, Niveau II – die jüngste Form des fhr-Katalogs) und die Höchstzahl verschiedener Plättchen aus zwei Symbolgruppen mit Fallsumme (iqb 2025MgrundlegendBStochastikWTR2-1e, vier Punkte, Anforderungsbereich III).
90  - Zählen mit Bedingungen und Wahrscheinlichkeitsterme (Einheit 3): „Mal oder plus?“ – ankreuzen, ob die Teile nacheinander gewählt werden (Produkt) oder Fälle nebeneinander stehen (Summe), und welche Faktoren gleich bleiben; „Anzahl oder Wahrscheinlichkeit?“ – ankreuzen, ob eine Anzahl gesucht ist oder ein Term, in dem die Anzahl als Faktor neben einer Pfadwahrscheinlichkeit steht; nichts rechnen (Vorstufe) → alle Auswahlen unter einer Abstandsbedingung geordnet aufzählen und die Vollständigkeit begründen (Grundfall, viermal; abi 2024-bebb-gk-A1.3a; iqb 2024MgrundlegendAStochastik13-a) → die Muster mit den Anordnungen der Personen multiplizieren (abi 2024-bebb-gk-A1.3b; iqb 2024MgrundlegendAStochastik13-b) → Sortenmuster aufzählen und mit den Anordnungen innerhalb der Sorten multiplizieren (iqb 2026MgrundlegendBStochastikWTR2-1f) → eine Gesamtzahl mit Unter- und Obergrenzen zerlegen und je Zerlegung die Zuordnungen zählen (iqb 2020MerhoehtAStochastik22-b) → die Anzahl in einen Wahrscheinlichkeitsterm einbauen: lauter verschiedene Ergebnisse als Fakultät durch Potenz, dann das kleinste n gegen eine Schranke [Kennung mit Ziffernende, deshalb in der Belegklammer: iqb 2023MerhoehtBStochastikWTR3-3] → „jede Zahl mindestens einmal“ als genau eine Wiederholung: Lagen des Paars mal Pfadwahrscheinlichkeit (iqb 2023MerhoehtAStochastik21-b) → Prüfungshöhe: den Term für das Gegenereignis einer festen Häufigkeitsverteilung mit einem Produkt von Binomialkoeffizienten angeben (iqb 2022MerhoehtAStochastik22-b, Teil A, Anforderungsbereich III).
91
92  ### Prüfungsform (fhr / abi / iqb)
93  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema Kombinatorik für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; maßgeblich sind RLP FOS 2019 (Pflichtthema 4, Baustein Kombinatorische Abzählverfahren) und der fhr-Katalog mit seinem Thema Kombinatorische Abzählverfahren (Prüfungsschwerpunkte: nur 2026/27 markiert, fhr.md § 6). Die Rohdatei zählt 34 Zeilen mit 19 Haupttypen (fhr 15 Zeilen, 6 Typen; abi 5 Zeilen, 5 Typen; iqb 14 Zeilen, 13 Typen; 5 abitur-Typen in beiden Abiturprofilen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (Thema ohne Gegenstandsklassen, daher ohne Präfix).
94  fhr (15 Zeilen, 6 Typen; FHR-Prüfungen 2019–2026, alle drei Vorschlagsbuchstaben) [fhr-Katalog]: Kombination ohne Wiederholung berechnen (9, E2) · Permutation ohne Wiederholung berechnen (2, E1) · je 1: Anzahl über das Zählprinzip berechnen (E1) · Fehlende Anzahl aus der Gesamtzahl der Möglichkeiten bestimmen (E1) · Kombination mit Wiederholung berechnen (E2) · Permutation mit Wiederholung berechnen (E1). Muster: Elf der sechzehn Hefte 2019–2026 – in jedem Jahrgang mindestens eines – stellen in Aufgabe 3 (Stochastik) ein bis zwei Kombinatorik-Teilaufgaben mit zwei bis sechs Punkten – fast immer den Zweierschritt „Auswahl ohne Reihenfolge (Binomialkoeffizient), dann Anordnung (Fakultät)“, den 2019-A-3d, 2022-C-3a, 2023-C-3d und 2025-C-3d als eine Zeile mit dem Nebentyp Permutation tragen, 2021-B-3a als Dreierschritt (Zählprinzip, Binomialkoeffizient, Fakultät, fünf Punkte); die Formen mit Wiederholung kommen erst 2026 (2026-B-3d, 2026-B-3e), die Variation ohne Wiederholung nur als Nebentyp in der Dreierkette 2020-A-3e (sechs Punkte, das einzige Niveau III des Themas). Neun der fünfzehn Zeilen tragen den Haupttyp Kombination ohne Wiederholung, fünf davon den Nebentyp Permutation. Niveau I 3, II 11, III 1; Punkte zwei bis sechs; Hilfsmittel immer ja (die Erwartungshorizonte lassen große Ergebnisse als Zehnerpotenz zu: 2023-A-3f, 2026-B-3e). Kontexte: Speisekarte, Gewürzstreuer, Eissorten, Ketten, Rosenfarben, Supermarktbefragung, Happy-Hour-Gäste, Billardkugeln, FOS-Klasse, Fußgängerzone, Bewerbungsgespräche.
95  abi (5 Zeilen, 5 Typen; Landeshefte 2017-be-gk, 2024-bebb-gk und 2024-bebb-lk) [abi-Katalog]: je 1: Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen (E1) · Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen (E2) · Anzahl der Sitzordnungen mit Abstandsbedingung berechnen (E3) · Anzahl ungeordneter Auswahlen ohne Wiederholung über den Binomialkoeffizienten berechnen (E2) · Auswahlen mit Abstandsbedingung aufzählen (E3). Muster: Alle fünf Zeilen sind wortgleiche Pooldubletten – vier aus dem Jahrgang 2024 (2024-bebb-gk-A1.3a und 2024-bebb-gk-A1.3b von 2024MgrundlegendAStochastik13-a und 2024MgrundlegendAStochastik13-b – die Stühle in Teil A des Grundkurshefts; 2024-bebb-lk-B4g und 2024-bebb-lk-B4h von 2024MerhoehtBStochastikWTR1-3a und 2024MerhoehtBStochastikWTR1-3b – die Kennwörter in Teil B des Leistungskurshefts), seit dem Nachzug 2026-09-28 dazu die Farbauswahl für die Smartphone-Auslage im Berliner Grundkursheft 2017 (2017-be-gk-B3.1a von 2017MgrundlegendBStochastikWTR1-1a, zwei Punkte, Teil B, Niveau I: vier aus sechs Farben über den Binomialkoeffizienten); landeseigene Zeilen gibt es nicht, die Landeshefte 2018–2023 und 2025–2026 tragen keine Zeile dieses Themas – Anzahlen kommen dort nur eingebettet in Wahrscheinlichkeitsaufgaben vor, geführt bei zufallsexperimente-und-pfadregeln.md Einheit 5. Teil A zwei Zeilen (zwei und drei Punkte), Teil B drei (zwei und drei Punkte). Amtlicher Anforderungsbereich in allen fünf Zeilen (höchster Bereich: I 2, II 3); Niveau I 2, II 3. Kontexte: Klassenzimmer, Kennwörter eines Streamingdienstes, Smartphone-Farben.
96  iqb (14 Zeilen, 13 Typen; Pool 2017 und 2020–2026 ohne 2021, grundlegend 6 und erhöht 8 Zeilen, Teil A 6 und Teil B 8 Zeilen) [iqb-Katalog]: Anzahl der Sitzordnungen mit Abstandsbedingung berechnen (2, E3) · je 1: Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen (E1) · Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen (E2) · Anzahl der Kombinationen aus zwei getrennten Auswahlgruppen ermitteln (E2) · Anzahl der Zahlenkombinationen mit einer vierfachen Ziffer aus drei Ziffern berechnen (E2) · Anzahl der Zusammensetzungen mit Mengenbedingungen je Sorte bestimmen (E3) · Anzahl geordneter Auswahlen ohne Wiederholung berechnen (E1) · Anzahl ungeordneter Auswahlen ohne Wiederholung über den Binomialkoeffizienten berechnen (E2) · Auswahlen mit Abstandsbedingung aufzählen (E3) · Faktoren eines kombinatorischen Terms im Sachzusammenhang deuten (E2) · Kleinstes n, für das die Wahrscheinlichkeit lauter verschiedener Ergebnisse unter eine Schranke fällt, ermitteln (E3) · Term für das Gegenereignis einer festen Häufigkeitsverteilung bei mehreren Würfen angeben (E3) · Term für die Wahrscheinlichkeit aufstellen, dass jede Zahl mindestens einmal fällt (E3). Muster: Der Pool prüft das Zählen selten für sich – drei Zeilen fragen eine nackte Anzahl mit Formel (2023MgrundlegendBStochastikWTR1-1a, 2022MerhoehtBStochastikWTR2-2 und seit dem Nachzug 2026-09-28 die Smartphone-Farben 2017MgrundlegendBStochastikWTR1-1a, vier aus sechs ohne Reihenfolge, zwei Punkte, Niveau I), alle übrigen koppeln die Anzahl an eine Bedingung (Stühle 2024, Lieder 2026, Tulpen 2020, Plättchen 2025), an eine Deutung (2020MerhoehtAStochastik22-a) oder an einen Wahrscheinlichkeitsterm (2022MerhoehtAStochastik22-b, 2023MerhoehtAStochastik21-b, 2023MerhoehtBStochastikWTR3-3). Teil A (sechs Zeilen, zwei bis drei Punkte; Prüfungsteile nach [IQB-STR 1]) trägt fünf der neun Zeilen der Einheit 3 – die Kurzaufgaben mit Stühlen, Tulpen, Würfel und Tetraeder –, Teil B (acht Zeilen, zwei bis vier Punkte) die Smartphone-Farben, Kennwörter, Röstgrade, Ziffernfolgen, Plättchen, Lieder und Motive als Auftakt einer Stochastik-Aufgabe. Grundlegend 6 (2017MgrundlegendBStochastikWTR1-1a, 2023MgrundlegendBStochastikWTR1-1a, 2024MgrundlegendAStochastik13-a, 2024MgrundlegendAStochastik13-b, 2025MgrundlegendBStochastikWTR2-1e, 2026MgrundlegendBStochastikWTR2-1f), erhöht 8 – die Term-Typen und die Zerlegung liegen ausschließlich in den erhöhten Pools. Amtlicher Anforderungsbereich in allen 14 Zeilen (höchster Bereich: I 3, II 5, III 6); Niveau I 3, II 5, III 6. Fünf Poolzeilen kehren wortgleich in Landesheften wieder (die Dublettenliste der abi-Zeile), keine abgewandelt. Kontexte: Smartphone-Farben, Klassenzimmer, Kennwörter, Tulpensträuße, Playlist, Brettspiel-Plättchen, Kaffee-Röstgrade, Olivenöl-Motive, Telefontarife, Würfel und Tetraeder.
97  Zielmarke: Einheit 1 – fhr: die drei Verteilungsbedingungen für sieben Ketten (2020-A-3e, sechs Punkte, Niveau III) und die Warteschlange aus fünfzig Kindern als Zehnerpotenz (2023-A-3f, Niveau II); abi und iqb: der Anteil der Kleinbuchstaben-Kennwörter als Potenzquotient unter einem Tausendstel (2024-bebb-lk-B4g, 2024MerhoehtBStochastikWTR1-3a, Teil B, Niveau I) und die geordnete Auswahl dreier Röstgrade (2023MgrundlegendBStochastikWTR1-1a, Niveau I). Einheit 2 – fhr: Auswahl und Verteilung von fünf aus zehn Eissorten (2019-A-3d, drei Punkte, Niveau II) und die Kombination mit Wiederholung der Gewürzstreuer (2026-B-3d, Niveau II); abi und iqb: die Kennwörter mit fester Buchstabenfolge (2024-bebb-lk-B4h, 2024MerhoehtBStochastikWTR1-3b, drei Punkte, Niveau II), die Plättchen aus zwei Symbolgruppen (2025MgrundlegendBStochastikWTR2-1e, vier Punkte, Niveau III) und die Termdeutung in Teil A (2020MerhoehtAStochastik22-a, Niveau II). Einheit 3 – abi und iqb: die vier Stuhlauswahlen und ihre Sitzordnungen (2024-bebb-gk-A1.3a und 2024-bebb-gk-A1.3b, 2024MgrundlegendAStochastik13-a und 2024MgrundlegendAStochastik13-b, Teil A, Niveau II), die Tulpensträuße mit Grenzen (2020MerhoehtAStochastik22-b, Niveau III), der Term mit dem Produkt von Binomialkoeffizienten (2022MerhoehtAStochastik22-b, Anforderungsbereich III) und das kleinste n gegen die Schranke (2023MerhoehtBStochastikWTR3-3, vier Punkte, Niveau III); fhr: keine Zeile.
````

## 2 Originale (34)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2019-A-3d (fhr-katalog.csv)

jahr 2019 · papier A · punkte 3 · format Rechnung · antwort Zahl
- gegeben: im Fabrikverkauf werden 10 Eissorten angeboten; für die Wochenwerbung werden 5 verschiedene Sorten ausgewählt; pro Tag soll eine der 5 Sorten besonders präsentiert werden, verteilt auf 5 Arbeitstage
- gesucht: Anzahl der Möglichkeiten, 5 aus 10 Sorten zusammenzustellen|Anzahl der Möglichkeiten, die 5 Sorten auf 5 Arbeitstage zu verteilen
- verfahren: für die Auswahl den Binomialkoeffizienten von 5 aus 10 berechnen, für die Verteilung die Fakultät von 5 bilden
- fehlerquelle: bei der Auswahl die Reihenfolge mitzählen und mit einer Variation rechnen

### 2022-C-3a (fhr-katalog.csv)

jahr 2022 · papier C · punkte 4 · format Rechnung · antwort Zahl
- gegeben: vor einem Supermarkt wurden 60 Personen befragt; fünf von ihnen erhalten als Dank ein Geschenk; die fünf Geschenke sind verschieden
- gesucht: Anzahl der Möglichkeiten, fünf Personen aus allen Befragten auszuwählen|Anzahl der Möglichkeiten, die fünf verschiedenen Geschenke an die fünf Ausgewählten zu vergeben
- verfahren: für die Auswahl den Binomialkoeffizienten 60 über 5 berechnen, weil die Reihenfolge keine Rolle spielt; für die Verteilung die Fakultät von 5 bilden, weil die Reihenfolge zählt
- fehlerquelle: für die Auswahl die Reihenfolge mitzählen und statt des Binomialkoeffizienten eine Variation berechnen

### 2023-C-3d (fhr-katalog.csv)

jahr 2023 · papier C · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Poolbillard mit 16 Kugeln: dem weißen Spielball und 15 durchnummerierten Objektbällen; die Bälle 1 bis 8 sind vollständig gefärbt und heißen die Vollen, dazu gehört auch die schwarze Kugel; die Halben mit den Nummern 9 bis 15 tragen nur einen farbigen Ring; alle Kugeln sind gleich groß und gleich schwer; Klaus wählt für einen Trick vier Kugeln von den sieben Halben aus; jede der vier Kugeln muss einmal gestoßen werden
- gesucht: Anzahl der Möglichkeiten für die Auswahl der vier Kugeln|Anzahl aller möglichen Varianten für die Reihenfolge des Stoßens
- verfahren: den Binomialkoeffizienten 7 über 4 berechnen, weil die Reihenfolge bei der Auswahl keine Rolle spielt; für die Reihenfolge die Fakultät von 4 bilden
- fehlerquelle: Auswahl und Reihenfolge vermischen und mit der Variation 7 · 6 · 5 · 4 rechnen

### 2025-C-3d (fhr-katalog.csv)

jahr 2025 · papier C · punkte 3 · format Rechnung · antwort Zahl
- gegeben: alle Personen aus Neustadt mit besseren Noten als 4, das sind 3 Personen mit Note 1, 5 mit Note 2 und 4 mit Note 3, also 12 Personen, werden in Vierergruppen zu Einstellungsgesprächen eingeladen
- gesucht: Anzahl der Möglichkeiten für die Zusammenstellung der ersten Vierergruppe|Anzahl der Möglichkeiten, vier Personen nacheinander zu Einzelgesprächen in den Raum zu bitten
- verfahren: die Zahl der Auswahlen von 4 aus 12 ohne Beachtung der Reihenfolge über den Binomialkoeffizienten berechnen; für die Reihenfolge der vier Gespräche 4 Fakultät bilden
- fehlerquelle: bei der Zusammenstellung der Gruppe die Reihenfolge mitzählen und 11 880 angeben

### 2021-B-3a (fhr-katalog.csv)

jahr 2021 · papier B · punkte 5 · format Rechnung · antwort Zahl
- gegeben: auf einer Speisekarte werden 6 Vorspeisen und 15 Hauptgänge angeboten
- gesucht: Anzahl der Möglichkeiten für ein zweigängiges Menü|Anzahl der Möglichkeiten, zwei verschiedene Hauptgänge auszuwählen|Anzahl der Möglichkeiten, alle Vorspeisen und anschließend alle Hauptgänge auf der Karte anzuordnen
- verfahren: für das Menü die beiden Anzahlen multiplizieren, für die zwei Hauptgänge den Binomialkoeffizienten 15 über 2 bilden und für die Anordnung die Fakultäten von 6 und 15 multiplizieren
- fehlerquelle: bei der Auswahl zweier Hauptgänge die Reihenfolge mitzählen und 210 statt 105 erhalten

### 2026-B-3d (fhr-katalog.csv)

jahr 2026 · papier B · punkte 2 · format Rechnung · antwort Zahl
- gegeben: eine sehr große Lieferung mit drei Gewürzsorten; ein Kunde greift rein zufällig fünf Gewürzstreuer heraus
- gesucht: Anzahl aller möglichen Zusammenstellungen
- verfahren: Kombination mit Wiederholung für n = 3 Sorten und k = 5 Streuer über den Binomialkoeffizienten von n + k − 1 über k berechnen
- fehlerquelle: die Reihenfolge mitzählen und 3^5 = 243 angeben

### 2026-B-3e (fhr-katalog.csv)

jahr 2026 · papier B · punkte 2 · format Rechnung · antwort Zahl
- gegeben: eine Kette aus 30 Gewürzstreuern für die Schaufensterdekoration, von jeder der drei Sorten 10 Stück
- gesucht: Anzahl der unterschiedlichen Reihenfolgen für die Kette
- verfahren: 30 Fakultät durch das Produkt aus dreimal 10 Fakultät teilen
- fehlerquelle: nur 30 Fakultät angeben und die gleichartigen Streuer je Sorte nicht herausdividieren

### 2020-A-3e (fhr-katalog.csv)

jahr 2020 · papier A · punkte 6 · format Rechnung · antwort Zahl
- gegeben: ein Set enthält sieben farblich unterscheidbare Ketten; sie sollen unter Berücksichtigung der Farbe verteilt werden; Bedingung I jede von sieben Freundinnen bekommt genau eine Kette, Bedingung II jede von sieben Freundinnen kann mehrere oder auch gar keine Kette bekommen, Bedingung III jede von 10 Freundinnen bekommt höchstens eine Kette
- gesucht: Anzahl der Möglichkeiten für jede der drei Bedingungen
- verfahren: für I die Fakultät von sieben bilden; für II jeder der sieben Ketten eine von sieben Freundinnen zuordnen und die sieben Wahlmöglichkeiten multiplizieren; für III die geordnete Auswahl von sieben aus zehn Freundinnen als Fakultät von zehn geteilt durch die Fakultät von drei berechnen
- fehlerquelle: bei II mit der Fakultät statt mit der Potenz rechnen, weil die Mehrfachvergabe übersehen wird

### 2023-A-3f (fhr-katalog.csv)

jahr 2023 · papier A · punkte 2 · format Rechnung · antwort Zahl
- gegeben: unter den 80 Happy-Hour-Gästen sind 30 Erwachsene und der Rest Kinder; zur Einweihung der Wasserrutsche stellen sich alle Kinder zum Rutschen an
- gesucht: Anzahl der verschiedenen Warteschlangen, die sich ergeben können
- verfahren: die 50 Kinder aus dem Aufgabenstamm bestimmen und 50 Fakultät berechnen, weil alle Kinder unterscheidbar sind und jede Reihenfolge zählt
- fehlerquelle: mit allen 80 Gästen statt mit den 50 Kindern rechnen

### 2024-bebb-gk-A1.3a (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 3 · format Kurzantwort · antwort Text
- gegeben: sechs Stühle in einer Reihe; es gibt vier Möglichkeiten, drei so auszuwählen, dass zwischen je zwei ausgewählten mindestens ein weiterer steht
- gesucht: diese vier Möglichkeiten
- verfahren: Systematisch von links beginnend aufzählen
- fehlerquelle: 1, 3, 4 (benachbart) mitzählen

### 2024-bebb-gk-A1.3b (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: sechs Stühle, die vier zulässigen Auswahlen aus a; Aaron, Bert und Can setzen sich so, dass zwischen je zwei Schülern mindestens ein Stuhl frei bleibt
- gesucht: Anzahl der Möglichkeiten
- verfahren: 4 · 3!
- fehlerquelle: die Reihenfolge der Schüler nicht berücksichtigen (4)

### 2024MgrundlegendAStochastik13-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Kurzantwort · antwort Text
- gegeben: sechs Stühle in einer Reihe; es gibt vier Möglichkeiten, drei Stühle so auszuwählen, dass zwischen je zwei ausgewählten mindestens ein weiterer steht
- gesucht: diese vier Möglichkeiten
- verfahren: mit dem ersten Stuhl beginnen und die Lücken systematisch verteilen
- fehlerquelle: die Auswahl 2, 4, 6 vergessen, weil man immer mit Stuhl 1 beginnt

### 2024MgrundlegendAStochastik13-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: sechs Stühle, vier zulässige Auswahlen von drei Stühlen (aus a); Aaron, Bert und Can setzen sich so, dass zwischen je zwei Schülern mindestens ein Stuhl frei bleibt
- gesucht: Anzahl der Möglichkeiten
- verfahren: je Stuhlauswahl die drei Schüler in 3! Reihenfolgen verteilen
- fehlerquelle: 4 · 3 = 12 rechnen

### 2024-bebb-lk-B4g (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 2 · format Rechnung · antwort Text
- gegeben: 80 Zeichen (26 Groß-, 26 Kleinbuchstaben, 10 Ziffern, 18 Sonderzeichen); Kennwörter aus genau acht Zeichen, Wiederholung erlaubt
- gesucht: Nachweis, dass Kennwörter nur aus Kleinbuchstaben weniger als ein Tausendstel ausmachen
- verfahren: Potenzen bilden, Quotient
- fehlerquelle: 8 · 26 statt 26⁸

### 2024-bebb-lk-B4h (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: acht verschiedene Zeichen; Buchstaben von Niclas in Reihenfolge und Schreibung enthalten; Beispiele Nic4+las, nNicl*as
- gesucht: Anzahl solcher Kennwörter
- verfahren: Lagen der zwei freien Stellen mal Zeichenwahl
- fehlerquelle: 74² (Wiederholung) oder 80 · 79 (Buchstaben von Niclas nicht ausschließen)

### 2024MerhoehtBStochastikWTR1-3a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 2 · format Rechnung · antwort Text
- gegeben: 80 Zeichen (26 Groß-, 26 Kleinbuchstaben, 10 Ziffern, 18 Sonderzeichen); Kennwörter aus genau acht Zeichen, Wiederholung erlaubt
- gesucht: Nachweis, dass Kennwörter nur aus Kleinbuchstaben weniger als ein Tausendstel ausmachen
- verfahren: Potenzen bilden, Quotient
- fehlerquelle: 8 · 26 statt 26⁸

### 2024MerhoehtBStochastikWTR1-3b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: acht verschiedene Zeichen; Buchstaben von Niclas in Reihenfolge und Schreibung enthalten; Beispiele Nic4+las, nNicl*as
- gesucht: Anzahl solcher Kennwörter
- verfahren: Lagen der zwei freien Stellen mal Zeichenwahl
- fehlerquelle: 74² (Wiederholung) oder 80 · 79 (Buchstaben von Niclas nicht ausschließen)

### 2017-be-gk-B3.1a (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ein Händler erhält eine Lieferung neuer Smartphones in sechs verschiedenen Farben. Für die Auslage einiger Geräte im Schaufenster sollen vier Farben ausgewählt werden.
- gesucht: Anzahl der Möglichkeiten für diese Auswahl
- verfahren: Ungeordnete Auswahl von 4 aus 6 ohne Wiederholung: Binomialkoeffizient (6 über 4).
- fehlerquelle: geordnet zählen (6 · 5 · 4 · 3 = 360)

### 2017MgrundlegendBStochastikWTR1-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; ein Händler erhält eine Lieferung dieser Smartphones; die gelieferten Geräte haben sechs verschiedene Farben; für die Auslage einiger Geräte im Schaufenster sollen vier Farben ausgewählt werden
- gesucht: Anzahl der Möglichkeiten für diese Auswahl
- verfahren: Ungeordnete Auswahl von 4 aus 6 ohne Wiederholung: Binomialkoeffizient
- fehlerquelle: geordnet zählen (6 · 5 · 4 · 3 = 360)

### 2023MgrundlegendBStochastikWTR1-1a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: fünf Röstgrade; jeder Besucher probiert drei verschiedene und legt die Reihenfolge fest
- gesucht: Anzahl der Möglichkeiten
- verfahren: Produkt 5 · 4 · 3
- fehlerquelle: Binomialkoeffizient ohne Reihenfolge (10)

### 2022MerhoehtBStochastikWTR2-2 (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: sechsstellige Kombination aus den Ziffern 1, 5, 9, alle kommen vor, eine Ziffer viermal
- gesucht: Anzahl der möglichen Kombinationen
- verfahren: Vierfache Ziffer wählen, Plätze der beiden übrigen wählen, deren Reihenfolge
- fehlerquelle: Reihenfolge der beiden Einzelziffern (Faktor 2) vergessen

### 2020MerhoehtAStochastik22-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Sträuße mit 15 Tulpen in Gelb, Orange, Rot; Strauß mit genau zwei Farben; Term (3 über 2) · 14
- gesucht: Bedeutung beider Faktoren im Sachzusammenhang
- verfahren: Auswahl der Farben und Aufteilung der Anzahl deuten
- fehlerquelle: 14 als Anzahl der übrigen Tulpen deuten

### 2022MerhoehtAStochastik22-b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Kurzantwort · antwort Term
- gegeben: Würfel mit 1, 2, 3 je zweimal; sechsmal geworfen
- gesucht: Term für die Wahrscheinlichkeit, dass nicht jede Zahl genau zweimal erzielt wird
- verfahren: über das Gegenereignis „jede Zahl genau zweimal“ mit Auswahl der Positionen
- fehlerquelle: Binomialverteilung mit n = 6, p = 1/3 für eine einzelne Zahl ansetzen

### 2023MerhoehtAStochastik21-b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Kurzantwort · antwort Term
- gegeben: Tetraeder mit 1 bis 4, fünfmal geworfen
- gesucht: Term für die Wahrscheinlichkeit, dass jede Zahl mindestens einmal erzielt wird
- verfahren: genau eine Zahl fällt zweimal; Anzahl der Anordnungen mal Pfadwahrscheinlichkeit
- fehlerquelle: (3/4 · 2/4 · 1/4) ohne die Anordnungen oder mit 5! statt (5 über 2)

### 2023MerhoehtBStochastikWTR3-3 (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: n verschiedene Motive, je Flasche zufällig eines; bei n Flaschen sind alle Motive verschieden mit Wahrscheinlichkeit unter 1 %
- gesucht: kleinster möglicher Wert von n
- verfahren: n!/nⁿ für wachsendes n berechnen, bis der Wert unter 1 % fällt
- fehlerquelle: Anzahl der Folgen ohne Wiederholung als nⁿ − n

### 2025MgrundlegendBStochastikWTR2-1e (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: drei Landschaftssymbole, zwei Tiersymbole; je Plättchen genau zwei Landschaften und ein oder zwei Tiere, kein Symbol doppelt
- gesucht: Höchstzahl verschiedener Plättchen
- verfahren: Landschaftspaare mal Tierauswahlen
- fehlerquelle: Tiere als 2 · 1 = 2 Möglichkeiten (ein Tier zweimal) statt 2 + 1

### 2026MgrundlegendBStochastikWTR2-1f (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: fünf Lieder mit Längen aus der Tabelle (zwei unter 4 Minuten); jedes genau einmal; kurze Lieder nicht direkt nacheinander
- gesucht: Anzahl der zulässigen Reihenfolgen
- verfahren: Muster der Sorten aufzählen, mit den Anordnungen innerhalb der Sorten multiplizieren
- fehlerquelle: Muster zählen und die 2! · 3! vergessen (6) oder 5! − 4! · 2 = 72 ohne Begründung

### 2020MerhoehtAStochastik22-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Strauß mit 15 Tulpen; je Farbe mindestens vier und höchstens sechs
- gesucht: Anzahl der Möglichkeiten, den Strauß zusammenzustellen
- verfahren: Zerlegungen von 15 in drei Zahlen aus {4, 5, 6} und ihre Farbzuordnungen zählen
- fehlerquelle: 3! = 6 für die Zerlegung 4, 5, 6 vergessen oder 3³ = 27 zählen

### 2021-A-3c (fhr-katalog.csv)

jahr 2021 · papier A · punkte 2 · format Rechnung · antwort Zahl
- gegeben: es sind fünf Rosenfarben erhältlich; für einen Strauß werden drei davon ausgewählt
- gesucht: Anzahl der Möglichkeiten, drei der erhältlichen Farben auszuwählen
- verfahren: den Binomialkoeffizienten 5 über 3 berechnen, weil die Reihenfolge der ausgewählten Farben keine Rolle spielt
- fehlerquelle: die Reihenfolge mitzählen und 60 statt 10 Möglichkeiten angeben

### 2021-B-3b (fhr-katalog.csv)

jahr 2021 · papier B · punkte 2 · format Rechnung · antwort Zahl
- gegeben: es gibt 6 Vorspeisen und 15 Hauptgänge; insgesamt gibt es 720 Möglichkeiten, ein zweigängiges Menü und ein Getränk aus der Karte zusammenzustellen
- gesucht: Anzahl der auf der Karte angebotenen Getränke
- verfahren: die Gesamtzahl der Möglichkeiten durch das Produkt der beiden bekannten Anzahlen teilen
- fehlerquelle: durch die Summe 21 statt durch das Produkt 90 teilen

### 2023-A-3c (fhr-katalog.csv)

jahr 2023 · papier A · punkte 2 · format Rechnung · antwort Zahl
- gegeben: von allen 80 Happy-Hour-Gästen erhalten drei Personen ein kostenloses Mittagessen
- gesucht: Anzahl der Möglichkeiten, aus 80 Gästen drei Personen auszuwählen
- verfahren: den Binomialkoeffizienten 80 über 3 berechnen, weil die Reihenfolge der drei Personen keine Rolle spielt
- fehlerquelle: die Reihenfolge mitzählen und 492 960 angeben

### 2024-B-3c (fhr-katalog.csv)

jahr 2024 · papier B · punkte 2 · format Rechnung · antwort Zahl
- gegeben: FOS-Klasse mit 24 Personen, ein Viertel davon mit kurzem Schulweg von unter 20 min, alle anderen mit langem Schulweg; drei ausgewählte Personen sollen die Ergebnisse der Untersuchung vor der Schulleitung präsentieren
- gesucht: Anzahl der Auswahlmöglichkeiten an vortragenden Personen aus der Klasse
- verfahren: den Binomialkoeffizienten 24 über 3 berechnen, da die Reihenfolge der drei Personen keine Rolle spielt und keine Person zweimal vorträgt
- fehlerquelle: die Reihenfolge berücksichtigen und mit 24 · 23 · 22 rechnen

### 2025-A-3a (fhr-katalog.csv)

jahr 2025 · papier A · punkte 2 · format Rechnung · antwort Zahl
- gegeben: eine Lokalredaktion befragt in einer Fußgängerzone insgesamt 50 Personen; von diesen 50 werden acht zufällig ausgewählt und nach der Konsumhäufigkeit im letzten Jahr befragt
- gesucht: Anzahl der Auswahlmöglichkeiten für acht Personen aus 50
- verfahren: den Binomialkoeffizienten 50 über 8 berechnen, weil die Reihenfolge der Auswahl keine Rolle spielt
- fehlerquelle: die Reihenfolge mitzählen und mit dem Produkt 50 · 49 · … · 43 rechnen

### 2020-A-3d (fhr-katalog.csv)

jahr 2020 · papier A · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Ketten werden nur noch in 7er-Sets mit je einer Kette pro Farbe angeboten; eine Frau will zwei oder fünf Ketten aus einem Set gleichzeitig tragen
- gesucht: Vergleich der Anzahl an Möglichkeiten, zwei oder fünf Ketten aus einem Set auszuwählen
- verfahren: für beide Fälle den Binomialkoeffizienten von 5 aus 7 beziehungsweise 2 aus 7 berechnen und die Ergebnisse gegenüberstellen
- fehlerquelle: die Reihenfolge mitzählen und mit Variationen statt mit Kombinationen rechnen

Nicht in den Prüfungsdateien gefunden: 2017-be-gk, 2024-bebb-gk, 2024-bebb-lk

Nur außerhalb von „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ genannt, nicht aufgenommen: 2022MgrundlegendAStochastik2, 2023MerhoehtBStochastikWTR1-2

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

# Mappe: bedingte-wahrscheinlichkeit-und-bayes

Eintrag: hz-0801/mathe-nachhilfe, katalog/bedingte-wahrscheinlichkeit-und-bayes.md
Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26T16:47:30+02:00, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:40 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Bedingte Wahrscheinlichkeit und Bayes
 3
 4  ### Verortung
 5  Die bedingte Wahrscheinlichkeit als Begriff und der Weg gegen die Baumrichtung: der Quotient aus Schnittanteil und Bedingungsanteil (aus Text, Vierfeldertafel oder absoluten Häufigkeiten), der Bayes-Q … (gekürzt, 1569 Zeichen)
 6  [GOST] Q2, 2. Kurshalbjahr (BB S. 27), Grund- und Leistungskursfach: L5-Zeile „Sachverhalte mithilfe von Baumdiagrammen oder Vierfeldertafeln untersuchen und damit Problemstellungen im Kontext bedingt … (gekürzt, 1238 Zeichen)
 7  [FOS] Pflichtthema 4 „Stochastik“ (S. 28): „bedingte Wahrscheinlichkeiten (Unabhängigkeit von Ereignissen, Vierfeldertafel/Doppelbaum)“ (Zeilen 1185–1187) – Pflichtstoff; die zentralen FHR-Prüfungen stellen die bedingten Anteile im Rahmen der Unabhängigkeitsaufgaben (Zeilen bei unabhaengigkeit.md), themen.csv führt hier keine fhr-Zeile.
 8  [LS-AA] Qualifikationsphase Kapitel VIII 3 „Bedingte Wahrscheinlichkeit“ – die eine Lerneinheit des Lehrwerks zum Thema. Zuordnung: Einheit 1 und 2 = QP VIII 3; Einheit 3 (Parameterformen) hat kein Lehrwerkskapitel und folgt der Rohdatei (Ermessen). Stundenangaben stehen nicht im Fahrplan.
 9
10  ### Lerneinheiten
11  1. Der Quotient – bedingte Wahrscheinlichkeit vorwärts: P_B(A) als Schnittanteil geteilt durch Bedingungsanteil, aus dem Text, aus der Vierfeldertafel (auch mit absoluten Häufigkeiten) und im Vergleich (zwei bedingte Anteile aus derselben Tafel berechnen und vergleichen); die Richtung der Bedingung lesen („unter den …“, „von den …“, „ein zufällig ausgewählter …“). (Q2, GK-Kern „bedingte Wahrscheinlichkeit“; OHiMi 2.4 Quotient) ← Eingabe „bedingte wahrscheinlichkeit“, „unter der bedingung“, „anteil unter den“
12    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK
13  2. Bayes – gegen die Baumrichtung: die bedingte Wahrscheinlichkeit gegen die Richtung des Baumdiagramms als ein Pfad geteilt durch die Summe der Pfade zum Ereignis (der Nenner ist die totale Wahrscheinlichkeit), Bayes-Terme im Sachzusammenhang deuten (Zähler ein Pfad, Nenner die Pfadsumme), vorgegebene Terme nachweisen und Werte daraus bestimmen, Ergebnisse mit Schranken vergleichen. (Q2, GK-Kern „Satz von der totalen Wahrscheinlichkeit“, „Satz von Bayes“ – nur Brandenburg nennt die Namen) ← Eingabe „bayes“, „baum rückwärts“, „wie wahrscheinlich war“, „totale wahrscheinlichkeit“
14    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK
15  3. Mit Parameter – Terme, Monotonie, Graphen: den Bayes-Quotienten mit einem Parameter aufstellen (ohne auszurechnen), die Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils begründen (Zähler konstant, Nenner fällt – der Bruch wächst), Graphen einer bedingten Wahrscheinlichkeit über Randwerte zuordnen, am Graphen ablesen und Parameter samt Funktionswert deuten, Mindestwerte aus einer Schranke an die bedingte Wahrscheinlichkeit berechnen. (Q2; Prüfungshöhe des Pools) ← Eingabe „bedingte wahrscheinlichkeit parameter“, „monotonie bedingte“, „graph bedingte wahrscheinlichkeit“
16    Marken: BE Q2 · BB Q2 · GK · Abitur GK · Abitur LK
17  Warum drei: Der Plan nennt Begriff, totale Wahrscheinlichkeit und Bayes, das Lehrwerk eine Einheit – die Rohdatei trennt die Richtung (vorwärts als Quotient, rückwärts als Bayes) und trägt daneben ein … (gekürzt, 675 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; die Rohdatei führt keine Nebentypen.
21  Einheit 1: Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen (16) · Bedingte Anteile aus der Vierfeldertafel vergleichen (3) — kein Nachweistyp — Deutung: Bedingte Wahrscheinlichkeit aus der Vierfeldertafel mit absoluten Häufigkeiten angeben (1). Dazu: Fehler finden (die Bedingung vertauscht – durch den falschen Rand geteilt, das Kernfehlmuster des Themas; den Quotienten auf die Gesamtheit statt auf die Bedingungsgruppe bezogen; Schnittanteile direkt verglichen statt bedingte Anteile; absolute statt bedingte Anteile verglichen) · Begründen (warum der Nenner der Anteil der Bedingung ist; warum bedingte Anteile vergleichbar machen, was Schnittanteile nicht leisten).
22  Einheit 2: Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen (11) · Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen (1) — Nachweis: Bayes-Term für drei Behälter nachweisen und Kugelzahl bestimmen (1) — Deutung: Bayes-Term im Sachzusammenhang deuten (2). Dazu: Fehler finden (die Richtung der Bedingung umgekehrt – P(B ¦ A) statt P(A ¦ B) angegeben, obwohl der Baum die erste Richtung liefert; den Nenner nur aus einem Ast gebildet; im Nenner zusammengehörige Pfade nicht zusammengefasst; eine Pfadwahrscheinlichkeit mit einer bedingten verwechselt) · Begründen (warum der Nenner die Summe aller Pfade zum eingetretenen Ereignis ist; warum sich die Richtung der Bedingung gegen die Baumrichtung dreht).
23  Einheit 3: Mindestwert einer Erkennungswahrscheinlichkeit aus einer Bedingung an eine bedingte Wahrscheinlichkeit bestimmen (1) · Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten (2; Ermessen, siehe Offene Punkte) — kein Nachweistyp — Deutung: Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen (6) · Graph einer bedingten Wahrscheinlichkeit in Abhängigkeit von einem Parameter über Randwerte ohne Rechnung zuordnen (1) · Term für eine bedingte Wahrscheinlichkeit mit Parameter aufstellen (1). Dazu: Fehler finden (mit einem Zahlenbeispiel statt allgemein argumentiert; den Zähler für parameterabhängig gehalten, obwohl er konstant ist; die Deutung der Bedingung umgekehrt; den Graphen gewählt, ohne die Randwerte zu prüfen; die Bedingung im Term übersehen) · Begründen (warum ein Bruch mit konstantem Zähler wächst, wenn der Nenner fällt; warum die Randwerte des Parameterbereichs den Graphen festlegen).
24  Zählung: 3 + 4 + 5 = 12 Haupttypen, 20 + 15 + 11 = 46 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: Heft 2017-be-gk, Pool 2017 grundlegend Teil A und B, erhöht Teil B, WTR und CAS; nachgezogen 2026-09-29 um die Katalogzeilen des CAS-Nachtrags (Pool 2017 grundlegend Teil B CAS)).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Vierfeldertafel füllen und lesen (Rand, Feld, bedingte Angabe unterscheiden) – die Anteile der Einheit 1. Sek-II-Nachbarthema vierfeldertafel.md (dasselbe Bündel). [GOST Q2 L5 „Vierfeldertafel“; GOST-OHiMi 2.4]
29  - Baumdiagramm und Pfadregeln (Produkt entlang des Pfades, Summe über Pfade) – Zähler und Nenner der Einheit 2. Sek-II-Nachbarthema zufallsexperimente-und-pfadregeln.md Einheit 6 (Situationsbaum, totale Wahrscheinlichkeit als Pfadsumme). [GOST Eingangsvoraussetzung L5 „Baumdiagrammen sowie Pfadregeln“]
30  - Anteile und Prozentsätze umrechnen, Quotienten von Anteilen bilden und kürzen – jede Rechnung. Sek-I-Themen prozentrechnung.md, bruchrechnung.md. [GOST Eingangsvoraussetzung L4 „Prozentdarstellungen“]
31  - Brüche mit Termen vergleichen (Zähler konstant, Nenner ändert sich) und einfache Bruchungleichungen lösen – die Monotonie- und Schrankenaufgaben der Einheit 3. Sek-I-Themen bruchrechnung.md, lineare-gleichungen.md; Sek-II-Thema gleichungen-loesen.md. [GOST-OHiMi 2.1]
32  - Graphen lesen (Funktionswert zu Stelle, Stelle zu Funktionswert, Randwerte) – die Graphaufgaben der Einheit 3. Sek-I-Thema lineare-funktionen.md (Graphenlesen); daten.md. [GOST Eingangsvoraussetzung L4 sinngemäß]
33  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
34  - „Was ist die Bedingung?“ – zu Aufgabentexten die Bedingungsgruppe unterstreichen („unter den …“, „ein zufällig ausgewählter Kunde mit …“, „die Person hat …“) und ankreuzen, durch wessen Anteil geteilt wird; nichts rechnen. Vor Einheit 1 und 2. [GOST-OHiMi 2.4; Rohdatei: das Kernfehlmuster (Bedingung vertauscht); abi 2023-bebb-gk-B4.1c, iqb 2018MgrundlegendBStochastikWTR1-1c]
35  - „Mit dem Baum oder gegen den Baum?“ – ankreuzen, ob die gefragte Bedingung der ersten Stufe des Baums entspricht (Pfadregeln genügen) oder der zweiten (Bayes: Pfad durch Pfadsumme); nichts rechnen. Vor Einheit 2. [GOST Q2 L5 „Satz von Bayes“ (BB); abi 2022-bebb-lk-B4b, iqb 2018MgrundlegendBStochastikWTR3-1c]
36  - „Was ändert der Parameter?“ – zu Parametertermen ankreuzen, ob der Parameter im Zähler, im Nenner oder in beiden steht, und was daraus für das Wachsen des Bruchs folgt; nichts rechnen. Vor Einheit 3. [Rohdatei-Fehlerquelle „Zähler für abhängig von a halten“; abi 2026-bb-ea-B4e, iqb 2026MgrundlegendBStochastikWTR1-2c]
37
38  ### Merkkasten
39  Einheit 1 (Der Quotient):
40      Definition: P_B(A) = P(A ∩ B) / P(B) – der Anteil von A innerhalb der Gruppe B; der Nenner ist immer der Anteil der Bedingung.
41        20 Personen mit allgemeiner Frage, davon 5 Männer: P(Mann ¦ allgemeine Frage) = 5/20 = 0,25 – nicht 5/80.
42      Aus der Tafel: Feld geteilt durch Rand; mit absoluten Häufigkeiten: Anzahl im Feld geteilt durch Anzahl in der Gruppe.
43      Multiplikationssatz: P(A ∩ B) = P(B) · P_B(A) – die Umkehrung des Quotienten; so wird aus einer bedingten Angabe ein Feld (→ vierfeldertafel.md).
44      Vergleichen: ob ein Merkmal in zwei Gruppen verschieden häufig ist, entscheiden die bedingten Anteile beider Gruppen – nie die Schnittanteile.
45      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.4] „bedingte Wahrscheinlichkeit: P_B(A) = P(A ∩ B)/P(B)“, „Multiplikationssatz“ (Teil-A-Beleg 2022MgrundlegendAStochastik12-a).
46      Formelsammlung: [FS-IQB 1.4] „Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit“ führt P_A(B) = P(A ∩ B)/P(A) – die Anlage verlangt die Formel dennoch auswendig – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
47  Quelle: eigene Formulierung nach [GOST-OHiMi 2.4] und [GOST Q2 L5] „bedingte Wahrscheinlichkeit“; Zahlenbeispiel aus abi 2017-bb-ea-B4.1b (wörtlich); [LS-AA QP VIII 3].
48
49  Einheit 2 (Bayes – gegen die Baumrichtung):
50      Der Bayes-Quotient: ist B eingetreten und war A eine Ursache der ersten Stufe, gilt P_B(A) = Pfad(A und B) / Summe aller Pfade zu B – der Nenner ist die totale Wahrscheinlichkeit von B.
51        Ein Drittel weiblich; unzufrieden sind wenige der Frauen und mehr der anderen: P(nicht weiblich ¦ unzufrieden) ist der Pfad „nicht weiblich und unzufrieden“ geteilt durch die Summe beider Unzufrieden-Pfade.
52      Deuten: in einem vorgelegten Quotienten ist der Zähler ein Pfad, der Nenner die Pfadsumme – Zähler und Nenner benennen, dann die Bedingung („geteilt durch die Wahrscheinlichkeit des Eingetretenen“) aussprechen.
53      Richtung: der Baum gibt P_A(B) (zweite Stufe nach erster); gefragt ist bei Bayes P_B(A) – die Richtung dreht sich, die Antwort „steht schon am Ast“ ist falsch.
54      Nachweisen: einen vorgegebenen Bayes-Term bestätigt man, indem man alle Pfade benennt und einsetzt; unbekannte Größen folgen aus einem vorgegebenen Wert durch Auflösen.
55      Auswendig (Teil A): „Der Bayes-Quotient“ und „Richtung“ – die Anlage nennt Bayes nicht, der Plan (BB) schon; begründetes Ermessen: der Pool prüft den Quotienten in Teil A (Belege 2020MgrundlegendAStochastik12-b, 2021MgrundlegendAStochastik11-b, 2026MgrundlegendAStochastik13-b, 2024MerhoehtAStochastik21), die Bausteine (Pfadregeln, Quotient) stehen in [GOST-OHiMi 2.4].
56      Formelsammlung: keine – weder Bayes noch die totale Wahrscheinlichkeit stehen in [FS-IQB 1.4] – [FS] offen
57  Quelle: eigene Formulierung nach [GOST Q2 L5] „Satz von der totalen Wahrscheinlichkeit“, „Satz von Bayes“ (nur BB) und [GOST-OHiMi 2.4]; Zahlenbeispiel sinngemäß aus abi 2020-be-gk-B4.2f (Struktur, ohne Zahlen); [LS-AA QP VIII 3].
58
59  Einheit 3 (Mit Parameter):
60      Term aufstellen: den Bayes-Quotienten mit dem Parameter hinschreiben, ohne auszurechnen – Zähler ein Pfad, Nenner die Pfadsumme, der Parameter steht, wo der Text ihn hinsetzt.
61      Monotonie: hängt nur der Nenner vom Parameter ab, wächst der Bruch genau dann, wenn der Nenner fällt (Zähler konstant); das trägt die Begründung „die Unzufriedenen der anderen Gruppe werden weniger, also wächst der Anteil der eigenen“ – allgemein, nicht am Zahlenbeispiel.
62      Graphen: den richtigen Graphen wählen die Randwerte des Parameterbereichs (Werte an den Enden überlegen, mit den Kurven vergleichen); am Graphen löst die Waagerechte zum Funktionswert die Gleichung grafisch.
63      Schranken: eine Bedingung an die bedingte Wahrscheinlichkeit wird zur Ungleichung im Parameter – auflösen und den kleinsten zulässigen Wert angeben.
64      Auswendig (Teil A): keine – die Parameterformen sind Prüfungshöhe (Teil B und erhöhte Teil-A-Aufgaben); sitzen müssen Quotient und Bayes-Quotient der Kästen eins und zwei.
65      Formelsammlung: keine – [FS] offen
66  Quelle: eigene Formulierung nach der Poolpraxis (die Parameterformen haben weder Plan- noch Lehrwerkszeile; Ermessen); ohne Zahlenbeispiel; [LS-AA QP VIII 3 als Basis].
67
68  ### Typische Fehler
69  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 39 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Stochastikdidaktik, die Muster sind allein aus den Katalogzeilen belegt.
70  - Bedingung vertauscht – das Kernfehlmuster: durch den falschen Rand geteilt, die Richtung der Bedingung umgekehrt (P(B ¦ A) statt P(A ¦ B), „Test positiv, wenn krank“ statt „krank, wenn Test positiv“), die am Ast stehende bedingte Wahrscheinlichkeit als Antwort genommen, die Deutung eines Terms in der falschen Richtung. [abi 2018-be-gk-B3.2f, 2023-bebb-gk-B4.1c, 2022-bebb-gk-A1.7a, 2025-bebb-gk-B4e, 2022-bebb-lk-B4b, 2024-bebb-lk-B4b, 2023-bebb-lk-B4f; iqb 2022MgrundlegendAStochastik12-a, 2021MgrundlegendAStochastik11-b, 2020MgrundlegendAStochastik12-b, 2026MgrundlegendBStochastikWTR2-1b, 2025MgrundlegendBStochastikWTR1-1e, 2024MgrundlegendBStochastikWTR2-1c, 2024MerhoehtBStochastikWTR1-1b, 2023MgrundlegendBStochastikWTR3-1c, 2023MerhoehtBStochastikWTR2-1d, 2022MerhoehtBStochastikWTR1-1b, 2022MerhoehtBStochastikWTR2-1b, 2018MgrundlegendBStochastikWTR1-1c, 2018MgrundlegendBStochastikWTR2-1f, 2018MgrundlegendBStochastikWTR3-1c, 2018MerhoehtBStochastikWTR2-1e, 2022MgrundlegendBStochastikWTR2-1c, 2026MgrundlegendAStochastik13-b]
71  - Auf die falsche Gesamtheit bezogen: den Quotienten durch alle geteilt statt durch die Bedingungsgruppe; einen Anteil unter den Frauen als Anteil an allen gelesen. [abi 2017-bb-ea-B4.1b; iqb 2019MgrundlegendBStochastikWTR3-1c]
72  - Nenner falsch gebaut: die totale Wahrscheinlichkeit nur aus einem Ast gebildet; zusammengehörige Pfade nicht zusammengefasst; Gruppen mitgezählt, die die Bedingung nicht erfüllen können. [abi 2020-be-gk-B4.2f; iqb 2020MgrundlegendBStochastikWTR1-2b, 2024MerhoehtAStochastik21, 2021MgrundlegendBStochastikWTR3-1g]
73  - Schnitt- statt bedingte Anteile verglichen, absolute statt bedingte: Schnittanteile direkt verglichen; absolute Anteile an der Gesamtheit gegeneinander gehalten. [iqb 2026MerhoehtBStochastikWTR2-1c, 2024MerhoehtBStochastikWTR2-1b, 2021MgrundlegendBStochastikWTR3-1b]
74  - Mit Parameter verfehlt: mit einem Zahlenbeispiel statt allgemein argumentiert; den Zähler für parameterabhängig gehalten; den Graphen ohne Prüfung der Randwerte gewählt; die Bedingung im Term übersehen und nur den Zähler angegeben. [abi 2026-bb-gk-B4f, 2026-bb-ea-B4e; iqb 2026MgrundlegendBStochastikWTR1-2c, 2026MerhoehtBStochastikWTR1-2c, 2020MgrundlegendBStochastikWTR2-2c, 2026MerhoehtAStochastik22-b, 2018MerhoehtBStochastikWTR2-1e]
75  Hinweis: 2018MerhoehtBStochastikWTR2-1e trägt beide Muster (Richtung und Schranke); die Schrankenrechnung selbst ist Einheit 3.
76
77  ### Für schwache Schüler
78  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q2 Brandenburg und Berlin: Einheit 1 („bedingte Wahrscheinlichkeit“) und Einheit 2 („Satz von der totalen Wahrscheinlichkeit“, „Satz von Bayes“ – die Namen nur in Brandenburg, die Sache in beiden Ländern); kein LK-Zusatz. Ohne Hilfsmittel (Anlage OHiMi 2.4, Prüfungsteil A): der Quotient und der Multiplikationssatz – Kasten eins vollständig, Kasten zwei als Ansatz. Vorrat (Ermessen nach dem Niveau der Rohdatei): die Parameterformen der Einheit 3 (Monotonie, Graphen, Schranken). Niveaustufe H der E-Phase [RLP]: die Sek-I-Pläne führen Pfadregeln und Vierfeldertafel, keine bedingte Wahrscheinlichkeit als Begriff – Blatt-0-Stoff sind die Pfade, der Begriff ist Q2-Stoff. RLP FOS (fhr): bedingte Wahrscheinlichkeiten sind Pflichtstoff; die Prüfungszeilen liegen bei unabhaengigkeit.md. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung bedingte Wahrscheinlichkeiten – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
79  Grundvorstellung (Blatt 0) [GOST Q2 L5, MO]: Die Bedingung schrumpft die Welt – gezählt wird nur noch innerhalb der Gruppe, von der man schon etwas weiß. „Hier sind die zwanzig Spielkarten aus der Vierfeldertafel-Übung, in vier Häufchen sortiert (rot/schwarz, markiert/unmarkiert), kein Term. Ich habe verdeckt eine Karte gezogen und verrate dir: sie ist markiert. Welche Häufchen kommen jetzt überhaupt noch infrage – lege die anderen beiseite. Wie wahrscheinlich ist jetzt ‚rot‘? Und warum ist das eine andere Zahl als vorhin, als noch alle zwanzig Karten im Spiel waren? Was wäre anders, wenn ich stattdessen verraten hätte: sie ist rot – welche Frage beantwortet dann ‚wie wahrscheinlich ist markiert‘?“ Wer die beiseitegelegten Karten weiterzählt oder die beiden Richtungen für dieselbe Frage hält, braucht das vor jeder Formel: Die Bedingung bestimmt den Nenner, und die Richtung der Frage entscheidet, welche Gruppe schrumpft. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q2-Kern „bedingte Wahrscheinlichkeit“), die Aufgabenform ist Ermessen. [GOST Q2 L5; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Bedingung vertauschen“, abi 2023-bebb-gk-B4.1c; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
80  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
81  - Der Quotient (Einheit 1): „Was ist die Bedingung?“ ankreuzen (Vorstufe, Grundvorstellung) → den Quotienten aus Text oder Tafel bilden: Feld durch Rand (Grundfall, viermal; abi 2022-bebb-gk-A1.7a, Teil A; iqb 2022MgrundlegendAStochastik12-a, Teil A; abi 2023-bebb-gk-B4.1c, 2018-be-gk-B3.2f; iqb 2023MgrundlegendBStochastikWTR3-1c, 2018MgrundlegendBStochastikWTR2-1f, 2026MgrundlegendBStochastikWTR2-1b, 2024MgrundlegendBStochastikWTR2-1c, 2022MerhoehtBStochastikWTR2-1b) → mit absoluten Häufigkeiten (abi 2017-bb-ea-B4.1b; iqb 2019MgrundlegendBStochastikWTR3-1c, 2018MgrundlegendBStochastikWTR1-1c) → zwei bedingte Anteile vergleichen (iqb 2021MgrundlegendBStochastikWTR3-1b, 2024MerhoehtBStochastikWTR2-1b, 2026MerhoehtBStochastikWTR2-1c) → Prüfungshöhe: den Unterschied der Richtungen an einer Tafel erklären (Vorstufe zu Einheit zwei; Rohdatei-Fehlmuster als Aufgabe).
82  - Bayes (Einheit 2): „Mit dem Baum oder gegen den Baum?“ ankreuzen (Vorstufe) → den Bayes-Quotienten aus dem Baum bilden: ein Pfad durch die Pfadsumme (Grundfall, viermal; abi 2020-be-gk-B4.2f, 2022-bebb-lk-B4b, 2024-bebb-lk-B4b; iqb 2020MgrundlegendBStochastikWTR1-2b, 2022MerhoehtBStochastikWTR1-1b, 2024MerhoehtBStochastikWTR1-1b, 2018MgrundlegendBStochastikWTR3-1c, 2022MgrundlegendBStochastikWTR2-1c) → einen vorgelegten Term deuten: Zähler als Pfad, Nenner als Pfadsumme benennen (iqb 2020MgrundlegendAStochastik12-b, 2021MgrundlegendAStochastik11-b, Teil A) → mit einer Schranke vergleichen (iqb 2026MgrundlegendAStochastik13-b, Teil A) → mit besonderen Bäumen: nur ein Teil der Gruppe kann die Bedingung erfüllen (iqb 2021MgrundlegendBStochastikWTR3-1g, Niveau III) → Prüfungshöhe: den Behälter-Term nachweisen und die Kugelzahl aus einem Wert bestimmen (iqb 2024MerhoehtAStochastik21, Teil A, Niveau III).
83  - Mit Parameter (Einheit 3): „Was ändert der Parameter?“ ankreuzen (Vorstufe) → den Term mit Parameter aufstellen, ohne zu rechnen (iqb 2026MerhoehtAStochastik22-b, Teil A; Grundfall, viermal) → die Monotonie begründen: Zähler konstant, Nenner fällt (abi 2023-bebb-lk-B4f, 2026-bb-gk-B4f, 2026-bb-ea-B4e; iqb 2023MerhoehtBStochastikWTR2-1d, 2026MgrundlegendBStochastikWTR1-2c, 2026MerhoehtBStochastikWTR1-2c, Niveau III) → den Graphen über die Randwerte zuordnen (iqb 2020MgrundlegendBStochastikWTR2-2c, Niveau III) → am Graphen ablesen und Parameter samt Funktionswert deuten (abi 2025-bebb-gk-B4e, iqb 2025MgrundlegendBStochastikWTR1-1e, Niveau III) → Prüfungshöhe: den Mindestwert aus der Schranke an die bedingte Wahrscheinlichkeit berechnen (iqb 2018MerhoehtBStochastikWTR2-1e, Niveau III).
84
85  ### Prüfungsform (fhr / abi / iqb)
86  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; die bedingten Anteile der FHR-Prüfungen liegen bei unabhaengigkeit.md, themen.csv führt hier keine fhr-Zeile. Die Rohdatei zählt 46 Zeilen mit 12 Haupttypen (abi 12 Zeilen, 4 Typen; iqb 34 Zeilen, 12 Typen; 4 Typen in beiden Profilen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
87  fhr: kein eigener Bestand – die bedingten Anteile laufen in den Unabhängigkeitsaufgaben der FHR-Prüfungen (Zeilen bei unabhaengigkeit.md).
88  abi (12 Zeilen, 4 Typen; Landeshefte bb-ea, be-gk, bebb-gk, bebb-lk, bb-gk 2017–2026) [abi-Katalog]: Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen (5, E1) · Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen (3, E2) · Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen (3, E3) · Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten (1, E3). Muster: Elf der zwölf Zeilen liegen in Teil B (zwei bis vier Punkte) als Fortsetzung der Vierfeldertafel- oder Baumaufgabe; die eine Teil-A-Zeile ist der Tafelquotient 2022-bebb-gk-A1.7a. 10 der 12 Zeilen sind wortgleiche Pooldubletten (2017-be-gk-B3.1d – seit dem Nachzug 2026-09-28: die Wahrscheinlichkeit für Werk A bei einem fehlerhaften Smartphone im Berliner Grundkursheft, Dublette von 2017MgrundlegendBStochastikWTR1-2b –, 2018-be-gk-B3.2f, 2022-bebb-gk-A1.7a, 2022-bebb-lk-B4b, 2023-bebb-gk-B4.1c, 2023-bebb-lk-B4f, 2024-bebb-lk-B4b, 2025-bebb-gk-B4e, 2026-bb-gk-B4f, 2026-bb-ea-B4e), eine abgewandelt (2020-be-gk-B4.2f – das Heft gibt einen Vierfeldertafel-Hinweis, der Pool nicht), Landeszusatz die Häufigkeitsaufgabe 2017-bb-ea-B4.1b. Niveau I 2, II 6, III 4.
89  iqb (34 Zeilen, 12 Typen; Pool 2017–2026, grundlegend 21 und erhöht 13 Zeilen, Teil A 7 und Teil B 27 Zeilen, davon 3 CAS) [iqb-Katalog]: Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen (11, E1) · Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen (8, E2) · Bedingte Anteile aus der Vierfeldertafel vergleichen (3, E1) · Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen (3, E3) · Bayes-Term im Sachzusammenhang deuten (2, E2) · je 1: Bayes-Term für drei Behälter nachweisen und Kugelzahl bestimmen (E2) · Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten (E3) · Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen (E2) · Bedingte Wahrscheinlichkeit aus der Vierfeldertafel mit absoluten Häufigkeiten angeben (E1) · Graph einer bedingten Wahrscheinlichkeit in Abhängigkeit von einem Parameter über Randwerte ohne Rechnung zuordnen (E3) · Mindestwert einer Erkennungswahrscheinlichkeit aus einer Bedingung an eine bedingte Wahrscheinlichkeit bestimmen (E3) · Term für eine bedingte Wahrscheinlichkeit mit Parameter aufstellen (E3). Muster: In Teil B folgt der Quotient fast immer unmittelbar auf die Vierfeldertafel- oder Baumzeile derselben Kontextaufgabe (zwei bis fünf Punkte, Anforderungsbereich II); die Parameterformen tragen den Anforderungsbereich III (2018MerhoehtBStochastikWTR2-1e, 2020MgrundlegendBStochastikWTR2-2c, 2025MgrundlegendBStochastikWTR1-1e, die Monotonie-Zeilen 2023–2026); Teil A prüft Termdeutungen und kleine Quotienten (2020MgrundlegendAStochastik12-b, 2021MgrundlegendAStochastik11-b, 2022MgrundlegendAStochastik12-a, 2026MgrundlegendAStochastik13-b, 2024MerhoehtAStochastik21, 2026MerhoehtAStochastik22-b, seit dem Nachzug 2026-09-28 auch der Bayes-Quotient am Urnenexperiment 2017MgrundlegendAStochastik2-b, drei Punkte, Niveau III). Der Jahrgang 2017 (seit dem Nachzug) stellt beide Richtungen in Teil B: den Quotienten vorwärts an den Smartphones (2017MgrundlegendBStochastikWTR1-2b; seit dem Nachzug 2026-09-29 auch die wortgleiche Teilaufgabe der grundlegenden CAS-Fassung 2017MgrundlegendBStochastikCAS-2b, drei Punkte, Niveau II, gleicher Typ, kein CAS-Anteil) und an der Haushaltsstatistik der CAS-Fassung (2017MerhoehtBStochastikCAS1-2), Bayes gegen den Baum am Saatgut (2017MerhoehtBStochastikWTR-1b) und am Schnelltest der CAS-Fassung (2017MerhoehtBStochastikCAS2-1c), je drei Punkte. Amtlicher Anforderungsbereich in allen 34 Zeilen (höchster Bereich: I 2, II 23, III 9); Niveau I 6, II 19, III 9. Kontexte: Bildschirme, Heuschnupfen-Test, Hundefutter, Unternehmen, Briefe, Wohnungen, Behälter, Sendungen, Smartphones, Saatgut, Haushalte, Schnelltest. 10 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste), eine abgewandelt.
90  Zielmarke: Einheit 1 – abi: der Tafelquotient in Teil A (2022-bebb-gk-A1.7a, Niveau I) und der Quotient nach der Tafel (2023-bebb-gk-B4.1c, Niveau II); iqb: der Vergleich zweier bedingter Anteile (2021MgrundlegendBStochastikWTR3-1b, 2026MerhoehtBStochastikWTR2-1c, Niveau II). Einheit 2 – abi: Bayes nach dem Baum (2024-bebb-lk-B4b, Niveau II) und die abgewandelte Fassung mit Tafelhinweis (2020-be-gk-B4.2f, Niveau II); iqb: der Behälter-Term (2024MerhoehtAStochastik21, Teil A, Niveau III) und der besondere Baum (2021MgrundlegendBStochastikWTR3-1g, Niveau III). Einheit 3 – abi: die Monotonie-Beurteilung (2026-bb-ea-B4e, Niveau III) und das grafische Lösen (2025-bebb-gk-B4e, Niveau III); iqb: der Mindestwert aus der Schranke (2018MerhoehtBStochastikWTR2-1e, Niveau III) und die Graphenzuordnung über Randwerte (2020MgrundlegendBStochastikWTR2-2c, Niveau III).
````

## 2 Originale (30)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2022-bebb-gk-A1.7a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: 60 % der Kunden reisen gerne in Region A, 30 % in Region B, 20 % in beide
- gesucht: Wahrscheinlichkeit, dass ein zufällig ausgewählter A-Kunde auch gerne nach B reist
- verfahren: Schnittanteil durch Randanteil
- fehlerquelle: durch 0,3 teilen

### 2017-be-gk-B3.1d (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Der Anteil fehlerhafter Geräte unter allen hergestellten beträgt 3 %. Ein unter allen hergestellten Geräten zufällig ausgewähltes Gerät ist fehlerhaft.
- gesucht: Wahrscheinlichkeit dafür, dass es im Werk A hergestellt wurde
- verfahren: Schnittanteil 0,1 · 0,05 durch den Gesamtanteil 0,03 teilen (Satz von Bayes).
- fehlerquelle: den Fehleranteil 5 % im Werk A angeben (Bedingung vertauscht)

### 2017MgrundlegendBStochastikWTR1-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; Anteil fehlerhafter Geräte insgesamt 3 %; ein unter allen hergestellten Geräten zufällig ausgewähltes Gerät ist fehlerhaft
- gesucht: Wahrscheinlichkeit dafür, dass es im Werk A hergestellt wurde
- verfahren: Schnittanteil 0,1 · 0,05 durch den Gesamtanteil 0,03 teilen (Satz von Bayes)
- fehlerquelle: den Fehleranteil 5 % im Werk A angeben (Bedingung vertauscht)

### 2018-be-gk-B3.2f (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Vierfeldertafel mit den Werten: Display und Netzteil defekt 1,0 Prozent, nur Display defekt 9,7 Prozent, nur Netzteil defekt 2,0 Prozent, keines defekt 87,3 Prozent; der Rand für ein defektes Display beträgt 10,7 Prozent.
- gesucht: Wahrscheinlichkeit dafür, dass ein Bildschirm mit defektem Display auch ein defektes Netzteil hat
- verfahren: Den Quotienten aus dem Feld beide defekt und dem Rand defektes Display bilden: 0,010 geteilt durch 0,107.
- fehlerquelle: durch den Rand für das defekte Netzteil statt für das defekte Display teilen und die Bedingung damit vertauschen

### 2022-bebb-lk-B4b (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Person nutzt ein Fitnessarmband
- gesucht: Wahrscheinlichkeit für Datenschutzbedenken
- verfahren: Pfad D–F durch Summe der Pfade zu F
- fehlerquelle: P(F | D) = 23 % als Antwort

### 2023-bebb-gk-B4.1c (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Von den Lehrkräften eines Landes arbeiten 25 % an einem Gymnasium; 15 % der Lehrkräfte sind weiblich und arbeiten an einem Gymnasium; insgesamt sind 72 % der Lehrkräfte weiblich. Eine zufällig ausgewählte Lehrkraft ist weiblich.
- gesucht: Wahrscheinlichkeit, dass sie an einem Gymnasium arbeitet
- verfahren: Schnittanteil durch Randanteil.
- fehlerquelle: Bedingung vertauschen (0,15/0,25 = 0,6)

### 2023-bebb-lk-B4f (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 3 · format Begründung · antwort Text
- gegeben: Person war nicht zufrieden; a wächst
- gesucht: Begründung im Sachzusammenhang, dass P(weiblich | nicht zufrieden) mit a zunimmt
- verfahren: Unzufriedene unter ¬W nehmen ab, unter W bleiben sie konstant, also wächst der Anteil der Weiblichen unter den Unzufriedenen
- fehlerquelle: mit P(¬Z | W) statt P(W | ¬Z) argumentieren

### 2024-bebb-lk-B4b (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Baumdiagramm aus a; Person mit Komplettpaket
- gesucht: P(höchstens 40 Jahre | Komplettpaket)
- verfahren: Bayes-Quotient
- fehlerquelle: P(B | A) = 80 % als Antwort

### 2025-bebb-gk-B4e (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 4 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: zwei Jahre später unverändert: 28,5 % mit Kind, 6,5 % überbelegt ohne Kind; f(x) = 0,285 · (0,159 − x) / (0,285 · (0,159 − x) + 0,715 · 0,065), 0 ≤ x ≤ 0,159; Graph in der Abbildung
- gesucht: x mit f(x) = 0,4 grafisch; Deutung von x und f(x)
- verfahren: Waagerechte bei 0,4 schneiden, Zähler und Nenner deuten
- fehlerquelle: f(x) als Anteil der überbelegten an den Haushalten mit Kind deuten (Richtung der Bedingung)

### 2026-bb-gk-B4f (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 3 · format Begründung · antwort Text
- gegeben: ein Jahr später: weiterhin 75 % Sammler, 80 % davon weiblich, a gestiegen; Aussage: P(T | nicht weiblich) ist größer als vor einem Jahr
- gesucht: Beurteilung der Aussage
- verfahren: Term in a aufstellen und Monotonie begründen
- fehlerquelle: mit Zahlenbeispiel statt allgemein argumentieren; Zähler für abhängig von a halten

### 2026-bb-ea-B4e (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: ein Jahr später: 75 % Sammler, 80 % davon weiblich, a gestiegen; Aussage: P(T | nicht weiblich) größer als vor einem Jahr
- gesucht: Beurteilung
- verfahren: Term in a aufstellen, Monotonie begründen
- fehlerquelle: Zähler für abhängig von a halten

### 2020-be-gk-B4.2f (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Befragung: 3,5 % der weiblichen und 10,5 % der anderen Beschäftigten sind unzufrieden; Baumdiagramm mit erster Stufe w / nicht w, zweiter Stufe u / nicht u, an den Ästen x (nicht w, dann nicht u) und y (Pfad w und u); 1/3 weiblich; die ausgewählte Person ist unzufrieden (Hinweis: Vierfeldertafel)
- gesucht: Wahrscheinlichkeit, dass sie nicht weiblich ist
- verfahren: P(nicht w ∩ u) durch P(u), etwa aus der Vierfeldertafel
- fehlerquelle: P(u) nur aus einem Ast bilden

### 2017-bb-ea-B4.1b (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Unter den 80 Personen, die je eine Frage eingereicht haben (30 Frauen, 50 Männer), wird eine Jahreskarte verlost. 20 der Fragen sind eher allgemeiner Natur, davon 15 von Frauen und 5 von Männern. Bekannt ist bereits, dass der Gewinner eine eher allgemeine Frage gestellt hat.
- gesucht: Wahrscheinlichkeit dafür, dass die Jahreskarte von einem Mann gewonnen wird
- verfahren: Bedingte Wahrscheinlichkeit: Anteil der Männer unter den 20 Personen mit allgemeiner Frage, also 5/20.
- fehlerquelle: die Wahrscheinlichkeit auf alle 80 Personen beziehen und 5/80 angeben

### 2018MerhoehtBStochastikWTR2-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Flachbildschirme, im Mittel einer von fünf fehlerhaft; alle fehlerfreien werden als fehlerfrei eingestuft, ein fehlerhafter mit Wahrscheinlichkeit x als fehlerhaft; ein als fehlerfrei eingestufter Bildschirm wird ausgewählt
- gesucht: kleinstmögliches x, sodass P(fehlerhaft | als fehlerfrei eingestuft) ≤ 5 %
- verfahren: Bedingte Wahrscheinlichkeit über den Baum aufstellen und die Ungleichung nach x auflösen
- fehlerquelle: Bedingung umgekehrt ansetzen (als fehlerfrei eingestuft | fehlerhaft)

### 2020MgrundlegendBStochastikWTR2-2c (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 4 · format Begründung · antwort Text
- gegeben: Große Firma versendet einen Teil ihrer Briefe mit Q (95 % am ersten Werktag zugestellt), den anderen Teil mit einem anderen Unternehmen; Baumdiagramm (Abb. 1): Q mit 0,6, dann E (zugestellt) 0,95 und Ē 0,05; nicht Q mit 0,4, dann E und Ē mit a; ein Brief wird zufällig ausgewählt; der ausgewählte Brief wurde nicht am ersten Werktag zugestellt; Abb. 2 zeigt vier Graphen A bis D in Abhängigkeit von a
- gesucht: der Graph, der P(Q | nicht zugestellt) in Abhängigkeit von a darstellt, mit Begründung ohne Rechnung
- verfahren: Werte für a = 0 (sicher Q, also 1) und a = 1 (größer als 0) überlegen und mit den Graphen vergleichen
- fehlerquelle: Graph B wählen, weil die Wahrscheinlichkeit mit a fällt, ohne den Wert bei a = 1 zu prüfen

### 2025MgrundlegendBStochastikWTR1-1e (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 4 · format Rechnung|Kurzantwort · antwort Zahl
- gegeben: zwei Jahre später unverändert: 28,5 % mit Kind, 6,5 % überbelegt ohne Kind; f(x) = 0,285 · (0,159 − x) / (0,285 · (0,159 − x) + 0,715 · 0,065), 0 ≤ x ≤ 0,159; Graph in der Abbildung
- gesucht: x mit f(x) = 0,4 grafisch; Deutung von x und f(x)
- verfahren: Waagerechte bei 0,4 schneiden, Zähler und Nenner deuten
- fehlerquelle: f(x) als Anteil der überbelegten an den Haushalten mit Kind deuten (Richtung der Bedingung)

### 2020MgrundlegendAStochastik12-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Term 0,12/(0,12 + 0,75 · 0,4)
- gesucht: Bedeutung des Terms im Sachzusammenhang
- verfahren: Zähler und Nenner deuten
- fehlerquelle: Anteil der Verkleideten unter den Erwachsenen (Bedingung vertauscht)

### 2021MgrundlegendAStochastik11-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Kurzantwort · antwort Text
- gegeben: Term 0,15 · 0,9 / (0,15 · 0,9 + 0,85 · 0,02)
- gesucht: Deutung des Terms im Sachzusammenhang
- verfahren: Zähler und Nenner als Pfade lesen
- fehlerquelle: Bedingung umkehren (Test positiv, wenn Heuschnupfen)

### 2022MgrundlegendAStochastik12-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: 60 % der Kunden reisen gerne in Region A, 30 % in Region B, 20 % in beide
- gesucht: Wahrscheinlichkeit, dass eine zufällig gewählte Person aus den A-Kunden auch gerne nach B reist
- verfahren: Schnittanteil durch Anteil A
- fehlerquelle: 20 %/30 % rechnen (Bedingung vertauscht)

### 2026MgrundlegendAStochastik13-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Rechnung · antwort Zahl|Text
- gegeben: Baumdiagramm: P(A) = 0,4, P(A und verspätet) = 0,08, P(nicht A und verspätet) = 0,18; eine zufällig ausgewählte Sendung wird verspätet zugestellt
- gesucht: Untersuchung, ob die Wahrscheinlichkeit, dass diese Sendung nicht mit A verschickt wurde, größer als 50 % ist
- verfahren: P(nicht A | verspätet) = 0,18/(0,08 + 0,18) berechnen und mit 0,5 vergleichen
- fehlerquelle: mit 0,3 (Anteil unter den nicht mit A verschickten) statt mit der bedingten Wahrscheinlichkeit unter der Bedingung verspätet antworten

### 2024MerhoehtAStochastik21 (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 5 · format Rechnung · antwort Text|Zahl
- gegeben: Behälter A (dreimal so viele weiße wie schwarze Kugeln), B (12 weiße, 4 schwarze), C (3 schwarze, w weiße); Behälter zufällig wählen, Kugel ziehen; Term (1/3 · 3/(w + 3)) / (1/3 · 3/(w + 3) + 2/3 · 1/4) für P(Behälter C | schwarz)
- gesucht: Nachweis des Terms|w, wenn diese Wahrscheinlichkeit 1/5 beträgt
- verfahren: P(C) = 1/3, P_C(S) = 3/(w + 3), P_(nicht C)(S) = 1/4, weil A und B beide Schwarzanteil 1/4 haben; Bayes-Formel; dann 1/5 setzen und nach w auflösen
- fehlerquelle: A und B im Nenner getrennt mit je 1/3 · 1/4 ansetzen und die Zusammenfassung 2/3 · 1/4 nicht erkennen

### 2026MerhoehtAStochastik22-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Kurzantwort · antwort Term
- gegeben: jeder von zwei erzeugten Zahlencodes enthält die Ziffernfolge mit Wahrscheinlichkeit p, 0 < p < 1; mindestens einer der beiden Codes enthält die Ziffernfolge
- gesucht: Term in p für die Wahrscheinlichkeit, dass die Ziffernfolge nicht in beiden Codes enthalten ist
- verfahren: unter der Bedingung mindestens einer ist nicht in beiden gleichbedeutend mit genau einer: Zähler p · (1 − p) + (1 − p) · p, Nenner 1 − (1 − p)^2
- fehlerquelle: die Bedingung übersehen und nur 2p(1 − p) angeben

### 2017MgrundlegendAStochastik2-b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Urne U1 mit vier roten und zwei gelben Kugeln, Urne U2 mit zwei roten, einer gelben und einer blauen Kugel; eine der Urnen wurde zufällig ausgewählt und daraus eine Kugel gezogen; die Kugel ist gelb oder blau
- gesucht: Wahrscheinlichkeit, dass die Kugel aus der Urne U1 stammt
- verfahren: Pfad U1 und „gelb oder blau“ durch die Summe beider Pfade zu „gelb oder blau“ teilen
- fehlerquelle: P(gelb oder blau | U1) = 1/3 statt der umgekehrten bedingten Wahrscheinlichkeit angeben

### 2017MgrundlegendBStochastikCAS-2b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %; Anteil fehlerhafter Geräte insgesamt 3 %; ein unter allen hergestellten Geräten zufällig ausgewähltes Gerät ist fehlerhaft
- gesucht: Wahrscheinlichkeit dafür, dass es im Werk A hergestellt wurde
- verfahren: Schnittanteil 0,1 · 0,05 durch den Gesamtanteil 0,03 teilen (Satz von Bayes)
- fehlerquelle: den Fehleranteil 5 % im Werk A angeben (Bedingung vertauscht)

### 2017MerhoehtBStochastikCAS1-2 (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Anteile der Haushalte in Deutschland 2013 nach Größe: 1-Personen-Haushalte 40,5 %, 2-Personen-Haushalte 34,5 %, 3-Personen-Haushalte 12,5 %, 4-Personen-Haushalte 9,2 %, Haushalte mit mindestens 5 Personen 3,3 %; ein 2013 zufällig ausgewählter Mehrpersonenhaushalt
- gesucht: Wahrscheinlichkeit, dass es sich um einen 3-Personen-Haushalt handelte
- verfahren: 0,125/(1 − 0,405) berechnen
- fehlerquelle: 12,5 % ohne Bedingung angeben

### 2017MerhoehtBStochastikWTR-1b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ein Großhändler bietet Samenkörner für Salatgurken in zwei Qualitätsstufen an: ein Samenkorn der Stufe A keimt mit 95 %, eines der Stufe B mit 70 %; ein Gemüseanbaubetrieb kauft Samenkörner beider Stufen, davon 65 % der Stufe A, und sät alle; ein keimendes Samenkorn wird zufällig ausgewählt
- gesucht: Wahrscheinlichkeit dafür, dass es sich um ein Samenkorn der Qualitätsstufe B handelt
- verfahren: P_K(B) = P(B ∩ K)/P(K) mit P(K) als Summe der beiden Keimpfade
- fehlerquelle: P(B) · P_B(K) = 24,5 % statt der bedingten Wahrscheinlichkeit angeben

### 2017MerhoehtBStochastikCAS2-1c (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 3 · format Rechnung · antwort Zahl
- gegeben: In Deutschland liegt bei 1 % der Bevölkerung eine Glutenunverträglichkeit vor; ein Schnelltest heißt positiv, wenn er die Unverträglichkeit anzeigt; liegt sie vor, ist er mit 98 % positiv; liegt sie nicht vor, ist er mit 4 % dennoch positiv; der Test wird bei einer zufällig ausgewählten Person durchgeführt
- gesucht: Wahrscheinlichkeit, dass eine Glutenunverträglichkeit vorliegt, wenn das Testergebnis positiv ist
- verfahren: P(G | P) = P(G ∩ P)/P(P) mit P(P) = 0,01 · 0,98 + 0,99 · 0,04
- fehlerquelle: P(P | G) = 98 % angeben

### 2021MgrundlegendBStochastikWTR3-1b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Rechnung · antwort Text
- gegeben: Großes Unternehmen: 77 % aller Beschäftigten sind mit ihrem Gehalt zufrieden; 5 % aller Beschäftigten sind in der Werbeabteilung und nicht zufrieden; 12 % aller Beschäftigten gehören zur Werbeabteilung
- gesucht: ob der Anteil der Unzufriedenen in der Werbeabteilung größer ist als im übrigen Unternehmen
- verfahren: Beide bedingten Anteile aus der Vierfeldertafel bilden und vergleichen
- fehlerquelle: 5 % mit 18 % vergleichen (absolute statt bedingte Anteile)

### 2026MerhoehtBStochastikWTR2-1c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 3 · format Rechnung · antwort Text
- gegeben: Vierfeldertafel aus b
- gesucht: ob der Anteil der mindestens fünf Jahre alten Fahrzeuge unter den Pkw größer ist als unter den übrigen
- verfahren: beide bedingten Anteile berechnen
- fehlerquelle: Schnittanteile 0,552 und 0,156 direkt vergleichen

### 2021MgrundlegendBStochastikWTR3-1g (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Befragung zur Absicht, das Unternehmen in zwölf Monaten zu verlassen: 70 % erhalten Frage A (Absicht, das Unternehmen zu verlassen), 30 % Frage B (Absicht zu bleiben); nur die Person kennt ihre Frage und antwortet wahrheitsgemäß; Baumdiagramm mit A (Ja mit x, Nein mit y) und B; 1024 von 2700 antworten Ja; Anteil der Gehwilligen 20 %; eine Person mit Antwort Ja wird zufällig ausgewählt
- gesucht: Wahrscheinlichkeit, dass sie das Unternehmen verlassen will
- verfahren: Pfad A → Ja (gehen) durch die Gesamtwahrscheinlichkeit für Ja teilen
- fehlerquelle: alle Gehwilligen (20 %) durch den Ja-Anteil teilen, obwohl Gehwillige mit Frage B Nein antworten

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2018MgrundlegendBStochastikWTR1-1c, 2018MgrundlegendBStochastikWTR3-1c, 2026MgrundlegendBStochastikWTR1-2c, 2026MgrundlegendBStochastikWTR2-1b, 2024MgrundlegendBStochastikWTR2-1c, 2024MerhoehtBStochastikWTR1-1b, 2023MgrundlegendBStochastikWTR3-1c, 2023MerhoehtBStochastikWTR2-1d, 2022MerhoehtBStochastikWTR1-1b, 2022MerhoehtBStochastikWTR2-1b, 2018MgrundlegendBStochastikWTR2-1f, 2022MgrundlegendBStochastikWTR2-1c, 2019MgrundlegendBStochastikWTR3-1c, 2020MgrundlegendBStochastikWTR1-2b, 2024MerhoehtBStochastikWTR2-1b, 2026MerhoehtBStochastikWTR1-2c

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

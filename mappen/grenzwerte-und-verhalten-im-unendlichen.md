# Mappe: grenzwerte-und-verhalten-im-unendlichen

Eintrag: hz-0801/mathe-nachhilfe, katalog/grenzwerte-und-verhalten-im-unendlichen.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:07 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Grenzwerte und Verhalten im Unendlichen
 3
 4  ### Verortung
 5  Das Verhalten der Funktionswerte für x → +∞ und x → −∞ als Funktionseigenschaft: bei ganzrationalen Funktionen aus Grad und Vorzeichen des Leitkoeffizienten, bei der e-Funktion und ihren Verwandten au … (gekürzt, 3050 Zeichen)
 6  [GOST] Q1, 1. Kurshalbjahr „Analysis; Lineare Algebra“ (BB S. 23–25), Grund- und Leistungskursfach, Funktionsklassen Potenzfunktionen mit ganzzahligem Exponenten, ganzrationale Funktionen, natürliche  … (gekürzt, 3760 Zeichen)
 7  [FOS] L1 (S. 23): „die Grundidee des Grenzwertbegriffs verstehen“; Wahlthema Zahlenfolgen: „die Grenzwertdefinition auf Zahlenfolgen anwenden“ (S. 30, Wahlthema 6, „Grenzwert einer Zahlenfolge“, „Gren … (gekürzt, 1254 Zeichen)
 8  [LS-AA] Einführungsphase Kapitel I „Funktionen und ihre Graphen“: 4 Ganzrationale Funktionen und ihr Verhalten für x → +∞ bzw. x → −∞ · 5 Symmetrie von Graphen (1 Funktionen, 2 Verschieben und Strecke … (gekürzt, 2203 Zeichen)
 9
10  ### Lerneinheiten
11  1. Ganzrationale Funktionen – der Leitterm entscheidet: bei geradem Grad laufen beide Seiten in dieselbe Richtung (Vorzeichen des Leitkoeffizienten), bei ungeradem Grad in entgegengesetzte; Schreibwei … (gekürzt, 852 Zeichen)
12    Marken: BE Q1/2 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
13  2. Produkte aus Polynom und e-Funktion – das Grenzverhalten von e^x, e^(−x) und e^(kx) (gegen null auf der einen, gegen unendlich auf der anderen Seite); die e-Funktion wächst schneller als jedes Poly … (gekürzt, 1012 Zeichen)
14    Marken: BE Q1/2 · BB Q1 · GK · Abitur GK · Abitur LK
15  3. Waagerechte Asymptoten – verschobene und gestreckte e-Funktionen a · e^(−kx) + c mit dem Grenzwert c (waagerechte Asymptote y = c), ihre Monotonie (Streckung und Verschiebung ändern sie nicht) und  … (gekürzt, 771 Zeichen)
16    Marken: BE Q1 · BB Q1 · GK (BE nur LK) · keine Prüfungsaufgabe
17  Warum drei: Der Plan nennt das Verhalten im Unendlichen als eine Funktionseigenschaft für alle Funktionsklassen; das Lehrwerk trennt ganzrationale Funktionen (EP I 4), Exponentialfunktionen (QP II) un … (gekürzt, 1120 Zeichen)
18
19  ### Typen je Lerneinheit
20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
21  Einheit 1: kein Berechnungstyp — Nachweis: Symmetrie am Funktionsterm beurteilen (3; Ermessen, siehe Offene Punkte – drei fhr-Zeilen, deren Punkt-Schwerpunkt beim Verhalten im Unendlichen liegt, der Typ gehört zum fhr-Thema „Symmetrie nachweisen“ bei funktionsklassen-und-eigenschaften.md) — Deutung: Grenzverhalten einer ganzrationalen Funktion angeben (4) · Verhalten im Unendlichen bestimmen (1). Dazu: Fehler finden (bei ungeradem Grad beide Seiten gleich angegeben; das Vorzeichen des Leitkoeffizienten übersehen; am Summanden 2x statt am Leitterm abgelesen; das Absolutglied als ungeraden Exponenten gewertet; das Verhalten von f statt von f' angegeben) · Begründen (warum nur der Leitterm zählt; warum ein negativer Leitkoeffizient bei geradem Grad beide Seiten nach unten schickt).
22  Einheit 2: kein Berechnungs- und kein Nachweistyp — Deutung: Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (6) · Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (5) · Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben (3). Dazu: Fehler finden (aus dem wachsenden Polynomfaktor auf +∞ geschlossen, obwohl der e-Faktor gegen null geht; das Vorzeichen des Polynomfaktors auf der Seite übersehen, auf der die e-Funktion wächst; „unbestimmt“ statt null, weil ein Faktor wächst und einer fällt; die Fallunterscheidung nach dem Parameter vergessen; den konstanten Summanden nicht als Grenzwert stehen gelassen) · Begründen (warum die e-Funktion gegen jedes Polynom gewinnt; warum e^x nie null ist und die Nullstellen allein aus dem Polynomfaktor kommen).
23  Einheit 3: kein Berechnungstyp — Nachweis: Monotonie, Nullstelle und Grenzwert einer e-Funktion am Term begründen (1) · Nullstellenfreiheit und Grenzwerte eines Bruchs mit e-Funktion am Term begründen (1). Dazu: Fehler finden (Grenzwert null statt der Verschiebung c; die beiden Grenzwerte des Bruchs vertauscht; den Nenner null gesetzt und eine Nullstelle gefunden; die Monotonie bei negativem Streckfaktor nicht umgedreht) · Begründen (warum die Verschiebung um c die Asymptote auf y = c legt; warum ein Bruch mit konstantem Zähler keine Nullstelle hat).
24  Zählung: 3 + 3 + 2 = 8 Haupttypen, 8 + 14 + 2 = 24 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeile vom 28.09.2026: Pool 2017 erhöht Teil B; nachgezogen 2026-09-29 um die Katalogzeile des CAS-Nachtrags: Berliner CAS-Heft 2018 GK).
25
26  ### Voraussetzungen (Blatt 0)
27  Fertigkeiten (je Zeile: was, wofür):
28  - Potenzen mit geradem und ungeradem Exponenten bei negativer Basis: gerade Hochzahl macht positiv, ungerade behält das Vorzeichen; große Zahlen einsetzen und die Größenordnung vergleichen (x⁴ gegen x²) – der Leitterm-Gedanke in Einheit 1. Sek-I-Themen potenzen-wurzeln.md, reelle-zahlen.md. [GOST Eingangsvoraussetzung L4 „verwenden … Potenzen“; RLP F Potenzen mit negativer Basis; FOS Pflichtthema 1 ganzrationale Funktionen]
29  - Öffnung einer Parabel und Verlauf der Normalparabel dritten Grades nach oben und unten: der Streckfaktor a > 0 oder a < 0 entscheidet – der Sonderfall von Einheit 1 für Grad zwei und drei, aus dem die Regel wächst. Sek-I-Thema quadratische-funktionen.md. [RLP G „Öffnungsrichtung, Scheitelpunkt“; GOST Eingangsvoraussetzung L4 „quadratische Zusammenhänge“; FOS Pflichtthema 1 „Lage von Parabeln im Koordinatensystem“]
30  - Exponentialfunktion y = a · qˣ: für einen Wachstumsfaktor größer eins wächst sie unbeschränkt und nähert sich nach links der Rechtsachse, für einen Faktor zwischen null und eins umgekehrt; e als Basis größer eins; e^(−x) als Spiegelbild von e^x – Grundlage von Einheit 2 und 3. Sek-I-Thema potenz-exponentialfunktionen.md (Einheit Exponentialfunktion aufstellen und deuten, Schwellenwert); Sek-II-Nachbar funktionsklassen-und-eigenschaften.md. [GOST Eingangsvoraussetzung L4 „charakterisieren und interpretieren die Verläufe der Funktionen … f(x) = aˣ“; RLP G–H Exponentialfunktion; BE Einführungsphase „beschreiben die Eigenschaften der Exponentialfunktion“]
31  - Achsen- und Punktsymmetrie am Graphen erkennen und f(−x) bilden (Vorzeichen bei geraden und ungeraden Potenzen) – die fhr-Auftaktzeilen in Einheit 1. Sek-I-Thema symmetrie-abbildungen.md; Sek-II-Nachbar funktionsklassen-und-eigenschaften.md (Typ „Symmetrie am Funktionsterm beurteilen“ mit eigenen Sprossen). [GOST Q1 L4 „Punktsymmetrie bzgl. des Koordinatenursprungs und Axialsymmetrie bzgl. der Ordinatenachse“; GOST-OHiMi 2.2 „Symmetrie“; FOS Pflichtthema 1 „Symmetrie bezüglich y-Achse und Koordinatenursprung“]
32  - Satz vom Nullprodukt und die Regel, dass e^x nie null und immer positiv ist – Nullstellen eines Produkts in Einheit 2, Nullstellenfreiheit eines Bruchs in Einheit 3. Sek-I-Thema quadratische-gleichungen.md (Nullprodukt); Sek-II-Nachbar gleichungen-loesen.md. [GOST Q1 L1 „Gleichungen … unter Verwendung … der Linearfaktorzerlegung“; GOST-OHiMi 2.1 „Gleichungen durch Faktorisieren lösen“; FOS Pflichtthema 1 „Zerlegung in Linearfaktoren“]
33  - Verschiebung und Streckung eines Graphen an der Gleichung lesen (f(x) + c verschiebt nach oben, a · f(x) streckt, negatives a spiegelt) und Monotonie als „steigt“ oder „fällt“ – Einheit 3. Sek-I-Thema quadratische-funktionen.md (Scheitelpunktform); Sek-II-Nachbar funktionsklassen-und-eigenschaften.md. [GOST-OHiMi 2.2 „Zusammenhang zwischen Funktionsgraph und Funktionsgleichung nach … Verschiebung …, Streckung“; RLP G Parabeln verschieben und strecken]
34  - Vorzeichen eines Produkts und eines Bruchs aus den Vorzeichen der Faktoren bestimmen (plus mal minus, Zähler positiv durch Nenner positiv) – „von oben oder von unten gegen null“ in Einheit 2 und 3. Sek-I-Thema rationale-zahlen.md. **Ermessen:** keine amtliche Eingangsvoraussetzung nennt die Vorzeichenregel als Werkzeug für Grenzwerte; gesetzt, weil sechs Fehlerquellen der Rohdatei das Vorzeichen des Polynomfaktors betreffen. [Ermessen; RLP E Rechnen mit rationalen Zahlen]
35  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
36  - „Wer gewinnt?“ – zu Funktionstermen ankreuzen, welcher Teil das Verhalten im Unendlichen bestimmt: bei einer Summe von Potenzen der Leitterm (höchster Exponent), bei einem Produkt mit e-Funktion der e-Faktor, bei einer Summe mit e-Funktion der konstante Summand als Grenzwert auf der Seite, auf der die e-Funktion verschwindet; nichts rechnen. Vor Einheit 1 bis 3. [GOST Q1 L4 „Verhalten im Unendlichen“; FS-IQB 1.2 Grenzwerte; Rohdatei-Fehlerquellen „am Summanden 2x −∞ ablesen“ (2022-bebb-lk-B2.1a), „Grenzwert ∞ wegen des Faktors x + 2“ (2022-bebb-gk-B2.1b), „Grenzwert 0 statt −5“ (2026MerhoehtBAnalysisWTR3-1a)]
37
38  ### Merkkasten
39  Einheit 1 (Ganzrationale Funktionen):
40      Leitterm: Für sehr große und sehr kleine x verhält sich eine ganzrationale Funktion wie ihr Summand mit dem höchsten Exponenten – alle anderen Summanden spielen keine Rolle mehr.
41      Gerader Grad: beide Seiten laufen in dieselbe Richtung – nach oben, wenn der Leitkoeffizient positiv ist, nach unten, wenn er negativ ist. Ungerader Grad: die Seiten laufen entgegengesetzt – bei positivem Leitkoeffizienten links nach unten und rechts nach oben, bei negativem umgekehrt.
42        f(x) = −2x⁴ + 3x² − 1: für x → +∞ gilt f(x) → −∞ und für x → −∞ gilt f(x) → −∞ (gerader Grad, Leitkoeffizient −2).
43        g(x) = x³ − 4x: für x → +∞ gilt g(x) → +∞, für x → −∞ gilt g(x) → −∞ (ungerader Grad, Leitkoeffizient 1).
44      Schreibweise: „für x → +∞ gilt f(x) → −∞“ oder lim f(x) = −∞ für x → +∞; beide Richtungen getrennt angeben.
45      Symmetrie am Term: nur gerade Exponenten (das Absolutglied zählt als x⁰) → Graph achsensymmetrisch zur y-Achse, f(−x) = f(x); nur ungerade Exponenten → punktsymmetrisch zum Ursprung, f(−x) = −f(x); gemischt → keine dieser beiden Symmetrien.
46        f(x) = −2x⁴ + 3x² − 1: alle Exponenten gerade → achsensymmetrisch. g(x) = x³ − 4x: alle ungerade → punktsymmetrisch.
47      Auswendig (Teil A): „Leitterm“, „Gerader Grad“, „Ungerader Grad“ und „Symmetrie am Term“ – [GOST-OHiMi 2.2] „Verhalten im Unendlichen“, „Symmetrie“; die „Schreibweise“ ist Konvention ([GOST Q1 L1] „Schreibweise „lim“ ohne formale Definition“) – die Hefte nehmen beide Formen an.
48      Formelsammlung: keine Regel für ganzrationale Funktionen in [FS-IQB 1.2] (die Grenzwerte dort betreffen e^x und ln x) – [FS] offen
49  Quelle: eigene Formulierung nach [GOST Q1 L4] „Verhalten im Unendlichen“, „Axialsymmetrie bzgl. der Ordinatenachse“, „Punktsymmetrie bzgl. des Koordinatenursprungs“ und [FOS] „Verhalten im Unendlichen“, „Symmetrie bezüglich y-Achse und Koordinatenursprung“; Zahlenbeispiele eigen (Ermessen; keine Zahl aus einer Rohdateizeile übernommen); [LS-AA EP I 4–5].
50
51  Einheit 2 (Produkte aus Polynom und e-Funktion):
52      e-Funktion: e^x geht für x → −∞ gegen null und für x → +∞ gegen +∞; e^(−x) umgekehrt; bei e^(kx) entscheidet das Vorzeichen von k, auf welcher Seite die Werte gegen null gehen.
53      Die e-Funktion gewinnt: In einem Produkt p(x) · e^x aus Polynom und e-Funktion bestimmt die e-Funktion das Verhalten. Auf der Seite, auf der e^x gegen null geht, geht das Produkt gegen null – der Graph nähert sich der x-Achse (von oben, wenn p dort positiv ist, von unten, wenn negativ). Auf der anderen Seite geht das Produkt gegen +∞ oder −∞, je nach Vorzeichen von p(x) dort.
54        f(x) = (x − 3) · e^x: für x → −∞ gilt f(x) → 0, der Graph nähert sich von unten der x-Achse (x − 3 < 0); für x → +∞ gilt f(x) → +∞.
55        g(x) = (5 − x) · e^(−x): für x → +∞ gilt g(x) → 0 (von unten, 5 − x < 0); für x → −∞ gilt g(x) → +∞ (beide Faktoren positiv und wachsend).
56      Konstanter Summand: bei p(x) · e^(−kx) + c bleibt c als Grenzwert stehen, wenn das Produkt verschwindet.
57      Nullstellen: e^x ist nie null – die Nullstellen von p(x) · e^x sind genau die Nullstellen von p.
58        f(x) = (x − 3) · e^x hat die einzige Nullstelle 3.
59      Parameter: bei (x + a) · e^(−x) oder k · p(x) · e^x hängt das Vorzeichen auf der wachsenden Seite vom Parameter ab – Fallunterscheidung nach dem Vorzeichen von k.
60      Auswendig (Teil A): „e-Funktion“, „Die e-Funktion gewinnt“ und „Nullstellen“ – [GOST-OHiMi 2.2] „Verhalten im Unendlichen“, „Nullstellen“, „Ableitungsfunktionen der zu behandelnden Funktionsklassen“ (e^x als Klasse); „Konstanter Summand“ und „Parameter“ sind Anwendungen; die Dominanzregel steht als Formel in [FS-IQB 1.2] (Teil B), muss in Teil A aber ohne Formelsammlung sitzen.
61      Formelsammlung: Analysis – Grenzwerte [FS-IQB 1.2] „Ist p(x) ein Polynom, so gilt lim p(x)/eˣ = 0 für x → +∞“ (die Dominanz der e-Funktion als Formel; dazu „lim ln x / p(x) = 0“ und „lim p(x) · ln x = 0 für x → 0“ für den LK) – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
62  Quelle: eigene Formulierung nach [GOST Q1 L1] „Grenzwertverhalten von Funktionsgraphen (x → ±∞)“, [GOST Q1 L4] „Verhalten im Unendlichen“, „Nullstellen“, „multiplikative Verknüpfungen zweier Funktionen“ und [FS-IQB 1.2] Grenzwerte; Regeln zu Seite und Vorzeichen aus den Rohdateizeilen (Landeshefte 2018–2026, Pool 2020–2025); Zahlenbeispiele eigen (Ermessen); [LS-AA QP II 1, 3–4].
63
64  Einheit 3 (Waagerechte Asymptoten):
65      Verschobene e-Funktion: f(x) = a · e^(−kx) + c mit k > 0 geht für x → +∞ gegen c – die Gerade y = c ist waagerechte Asymptote; für x → −∞ gehen die Werte gegen +∞ (a > 0) oder −∞ (a < 0). Streckung mit a und Verschiebung um c ändern die Monotonie von e^(−kx) nicht: für a > 0 fällt f streng monoton, für a < 0 steigt f.
66        f(x) = 3 · e^(−2x) − 3: für x → +∞ gilt f(x) → −3; streng monoton fallend; Nullstelle bei e^(−2x) = 1, also x = 0.
67      Bruch mit e-Funktion im Nenner: h(x) = c/(1 + e^x) geht für x → +∞ gegen null (Nenner wächst unbeschränkt) und für x → −∞ gegen c (e^x verschwindet, Nenner wird 1); der Bruch hat keine Nullstelle, weil der Zähler nie null ist.
68        h(x) = 6/(1 + e^x): Grenzwerte 0 und 6, keine Nullstelle, Wertebereich zwischen 0 und 6.
69      Sättigung: Im Sachzusammenhang ist der Grenzwert der Wert, dem sich die Größe auf Dauer nähert (Umgebungstemperatur, Kapazität).
70      Auswendig (Teil A): „Verschobene e-Funktion“ und „Bruch mit e-Funktion im Nenner“ – [GOST-OHiMi 2.2] „Verhalten im Unendlichen“, „Monotonie“, „Zusammenhang zwischen Funktionsgraph und Funktionsgleichung nach … Verschiebung entlang der Ordinatenachse, Streckung parallel zur Ordinatenachse“; das Wort Asymptote nennt die Anlage nicht, der Pool prüft die Regel in Teil B; „Sättigung“ ist Deutung.
71      Formelsammlung: keine Regel zu Asymptoten in [FS-IQB 1.2]; „eˣ → eˣ“ und die Grenzwertformel wie in Kasten 2 – [FS] offen
72  Quelle: eigene Formulierung nach [GOST Q1 L1] „Grenzwertverhalten von Funktionsgraphen“, [GOST Q1 L4] „Monotonie“, „Verhalten im Unendlichen“ und [GOST-OHiMi 2.2] Verschiebung und Streckung; Bruch und verschobene e-Funktion aus den beiden Poolzeilen (2024MerhoehtBAnalysisWTR1-1a, 2026MerhoehtBAnalysisWTR3-1a); Zahlenbeispiele eigen (Ermessen); [LS-AA QP IV 5].
73
74  ### Typische Fehler
75  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 22 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Didaktik des Grenzwertbegriffs, die Muster sind allein aus den Katalogzeilen belegt.
76  - Polynomfaktor statt e-Funktion: aus x² − 4 → ∞ auf f(x) → ∞ geschlossen, obwohl e^x gegen null geht; Grenzwert ∞ wegen des Faktors x + 2; wegen des Faktors 8t Wachstum gegen unendlich angenommen; aus x · (3 − x) → −∞ auf f → −∞ geschlossen; aus dem Produkt aus wachsendem und fallendem Faktor auf einen unbestimmten Grenzwert geschlossen; nur den wachsenden Summanden betrachtet – das häufigste Muster in abi und iqb. [abi 2023-bebb-gk-B2.1a, 2022-bebb-gk-B2.1b, 2019-be-gk-B2.2a, 2018-be-gk-B1.2a, 2017-bb-ea-B2.2a; iqb 2022MgrundlegendBAnalysisWTR2-1b, 2020MgrundlegendBAnalysisWTR2-1b]
77  - Vorzeichen auf der wachsenden Seite übersehen: das Verhalten für x → +∞ als +∞, obwohl 2 − x negativ wird; das Vorzeichen des quadratischen Terms für x → −∞ übersehen; bei e^(−x) → ∞ das Vorzeichen des ersten Faktors übersehen; das Vorzeichen des Parameters a auf der falschen Seite eingebracht oder die Fallunterscheidung nach k vergessen. [abi 2025-bebb-gk-B2.2a, 2021-be-gk-B2.2b, 2020-be-gk-B2.1b, 2023-bebb-lk-B2.1b; iqb 2025MgrundlegendBAnalysisWTR2-1a, 2024MerhoehtBAnalysisWTR3-2a]
78  - Leitterm falsch gelesen: bei ungeradem Grad für beide Richtungen dasselbe Vorzeichen; das Verhalten einer Funktion geraden Grades unterstellt und beide Grenzwerte gleich angegeben; das negative Vorzeichen der höchsten Potenz übersehen und beide Grenzwerte gegen plus unendlich; am Summanden 2x statt am Leitterm abgelesen; wegen des Minuszeichens im mittleren Glied auf entgegengesetztes Verhalten geschlossen; das Verhalten von f statt von f' angegeben. [fhr 2024-C-1a, 2023-A-1a, 2020-C-1a, 2022-B-1a, 2021-A-1a; abi 2022-bebb-gk-B2.2a, 2022-bebb-lk-B2.1a, 2026-bb-gk-B2.1a]
79  - Symmetrie am Term: das Absolutglied 20 als ungeraden Exponenten gewertet und Punktsymmetrie vermutet. [fhr 2021-B-1a]
80  - Asymptote und Bruch: Grenzwert 0 statt −5 (die Verschiebung um −5 vergessen); die beiden Grenzwerte des Bruchs vertauscht. [iqb 2026MerhoehtBAnalysisWTR3-1a, 2024MerhoehtBAnalysisWTR1-1a]
81
82  ### Für schwache Schüler
83  Mindeststoff (GK-Kern Q1 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q1 (Funktionsklassen ganzrational, Potenz- und natürliche Exponentialfunktionen): Einheit 1 „Verhalten im Unendlichen“, „Axialsymmetrie bzgl. der Ordinatenachse“, „Punktsymmetrie bzgl. des Koordinatenursprungs“; Einheit 2 „Grenzwertverhalten von Funktionsgraphen (x → ±∞)“, „Nullstellen“, „multiplikative Verknüpfungen zweier Funktionen“, e-Funktion als Klasse; Einheit 3 „Monotonie“, Verschiebung und Streckung (Anlage). Ohne Hilfsmittel (Anlage OHiMi 2.2, Prüfungsteil A): Verhalten im Unendlichen, Symmetrie, Monotonie, Nullstellen, qualitative Beschreibung des Verlaufs, Verschiebung und Streckung – nicht: die Schreibweise lim (Plan), das Wort Asymptote (nirgends amtlich in Brandenburg). LK-Zusatz (für GK Vorrat): Wurzel-, ln-, sin/cos-Funktionen; Berlin „Asymptoten ermitteln“ bei gebrochenrationalen Funktionen, x → x₀ (Polstellen) – kein Original in beiden Katalogen. Niveaustufe H der E-Phase [RLP H]: Potenzfunktionen y = a · xᵏ + b und Exponentialfunktion y = a · bˣ + c – der Sek-I-Plan führt das Verhalten im Unendlichen nicht als Begriff, nur die Verläufe; Blatt-0-Stoff (Voraussetzungen zwei und drei). RLP FOS (fhr) [FOS Pflichtthema 1 „Ganzrationale Funktionen bis 5. Grades“]: „Symmetrie bezüglich y-Achse und Koordinatenursprung“, „Verhalten im Unendlichen“ – Einheit 1 vollständig; Einheit 2 und 3 kein Stoff (keine Exponentialfunktion im Pflichtbereich). Vorrat: alles außerhalb dieser Listen, für fhr insbesondere alle Zeilen mit e-Funktion (18 der 22), für GK die Parameterzeilen (2023-bebb-lk-B2.1b, 2024MerhoehtBAnalysisWTR3-2a) und die Zeilen der Einheit 3 (beide erhöht). COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung das Verhalten im Unendlichen und Asymptoten unter Funktionen – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
84  Grundvorstellung (Blatt 0) [GOST Eingangsvoraussetzung L4, GOST Q1 L1, MO]: „Gegen unendlich“ heißt: Ich darf x so groß wählen, wie ich will, und schaue, wohin die Werte dann laufen – nicht: Ich setze unendlich ein. „Hier sind zwei Terme, eine Summe aus einer vierten und einer zweiten Potenz mit verschiedenen Vorzeichen und ein Produkt aus einer Klammer und einer e-Funktion. Setze für x nacheinander zehn, hundert, tausend ein – nur mit dem Rechner, ohne Regel – und schreibe die Werte in eine Tabelle. Wer wird größer, wer kleiner? Ab wann spielt der kleinere Summand keine Rolle mehr? Jetzt dieselben Zahlen mit Minus: Was passiert mit dem Vorzeichen bei der vierten Potenz, was bei der e-Funktion? Zeichne den Graphen grob und markiere mit einem Pfeil, wohin er rechts und links läuft.“ Wer „unendlich“ einsetzt und „unendlich minus unendlich“ hinschreibt, wer am Produkt einen Faktor wachsen sieht und deshalb „unendlich“ antwortet, ohne den anderen zu prüfen, oder wer bei negativem x die vierte Potenz negativ erwartet, braucht das vor jeder Regel: Das Verhalten im Unendlichen ist eine Beobachtung an großen Zahlen, die Regel fasst sie nur zusammen. Verständnis, nicht Verfahren; Ermessen in der Aufgabenform, amtlich in der Vorstellung (propädeutischer Grenzwertbegriff). [GOST Q1 L1 „Grenzwerte auf der Grundlage eines propädeutischen Grenzwertbegriffs“, „Schreibweise „lim“ ohne formale Definition“; GOST Eingangsvoraussetzung L4 „charakterisieren und interpretieren die Verläufe der Funktionen … f(x) = aˣ“; GOST Eingangsvoraussetzung L1 „Einschachtelung einer irrationalen Zahl“ als Vorläufer eines Grenzprozesses; MO-Logik: Vorstellung vor Verfahren; abi 2018-be-gk-B1.2a Fehlerquelle „aus dem Produkt aus wachsendem und fallendem Faktor auf einen unbestimmten Grenzwert schließen“; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
85  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
86  - Ganzrationale Funktionen (Einheit 1): „Gerade oder ungerade, plus oder minus?“ – zu ganzrationalen Termen ankreuzen, ob der Grad gerade oder ungerade und der Leitkoeffizient positiv oder negativ ist, und daraus die beiden Richtungen; nichts rechnen (Vorstufe, Grundvorstellung) → zu einer Parabel und einer Funktion dritten Grades mit positivem Leitkoeffizienten beide Richtungen angeben (Grundfall, viermal) → negativer Leitkoeffizient bei geradem und ungeradem Grad (fhr 2023-A-1a, 2021-A-1a; abi 2022-bebb-gk-B2.2a) → Bruchkoeffizient und Grad vier oder fünf, der Leitterm steht nicht vorn (fhr 2024-C-1a, 2020-C-1a, 2021-B-1a, 2022-B-1a; abi 2022-bebb-lk-B2.1a) → das Verhalten einer Ableitungsfunktion angeben, wenn f' als Term gegeben ist (abi 2026-bb-gk-B2.1a) → die Symmetrie am Term als Auftakt begründen: gerade Exponenten oder f(−x) bilden, das Absolutglied als geraden Exponenten lesen (fhr 2020-C-1a, 2021-B-1a, 2023-A-1a) → Prüfungshöhe: Symmetrie und Verhalten im Unendlichen in einer Teilaufgabe mit drei Punkten, Schreibweise mit lim oder Pfeil (fhr 2023-A-1a, Niveau I); abi: kein Original über Niveau I; fhr-Zielmarke: die Teilaufgabe a jeder Kurvenuntersuchung (fhr 2024-C-1a, 2023-A-1a, Niveau I).
87  - Produkte aus Polynom und e-Funktion (Einheit 2): „Wer gewinnt?“ und „Welche Seite, welches Vorzeichen?“ ankreuzen, bei „Welche Seite, welches Vorzeichen?“ die Seite, auf der der e-Faktor gegen null geht, und das Vorzeichen von p(x) auf der anderen Seite; nichts rechnen (Vorstufe, Grundvorstellung) → zu e^x, e^(−x) und e^(kx) die beiden Richtungen angeben (Grundfall, viermal) → linearer Faktor mal e^x: Seite der Annäherung an die x-Achse und Vorzeichen auf der anderen Seite (abi 2025-bebb-gk-B2.2a; iqb 2025MgrundlegendBAnalysisWTR2-1a) → linearer Faktor mal e^(−x) oder e^(−0,5x), Verlauf in Worten (abi 2022-bebb-gk-B2.1b, 2018-be-gk-B1.2a; iqb 2022MgrundlegendBAnalysisWTR2-1b) → quadratischer Faktor: Vorzeichen des Polynoms auf der wachsenden Seite (abi 2023-bebb-gk-B2.1a, 2021-be-gk-B2.2b, 2020-be-gk-B2.1b; iqb 2020MgrundlegendBAnalysisWTR2-1b mit Begründung am Term) → konstanter Summand als Grenzwert im Sachzusammenhang (abi 2019-be-gk-B2.2a) → Nullstelle aus dem Polynomfaktor mit dem Grenzverhalten zusammen angeben (abi 2025-bebb-gk-B2.2a, 2018-be-gk-B1.2a) → Prüfungshöhe: Fallunterscheidung nach dem Vorzeichen eines Parameters (abi 2023-bebb-lk-B2.1b; iqb 2024MerhoehtBAnalysisWTR3-2a, Niveau I) und eine Summe zweier e-Funktionen mit Parameter samt Nullstellenfreiheit und Symmetrie (abi 2017-bb-ea-B2.2a, Niveau II); fhr-Zielmarke: keine – e-Funktionen sind kein FOS-Stoff.
88  - Waagerechte Asymptoten (Einheit 3): „Wer gewinnt?“ ankreuzen (Vorstufe) → zu a · e^(−kx) + c den Grenzwert für x → +∞ ablesen (Grundfall, viermal) → Monotonie und Nullstelle derselben Funktion am Term begründen (iqb 2026MerhoehtBAnalysisWTR3-1a) → Bruch mit konstantem Zähler und e-Funktion im Nenner: beide Grenzwerte, keine Nullstelle (iqb 2024MerhoehtBAnalysisWTR1-1a) → Prüfungshöhe: die Grenzwerte als Wertebereich und als Sättigung im Sachzusammenhang deuten (Vorrat, kein Original – der Pool fragt den Wertebereich bei kurvenuntersuchung.md); beide Originale Niveau I; fhr-Zielmarke: keine.
89
90  ### Prüfungsform (fhr / abi / iqb)
91  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen (be-gk, be-lk, bb-gk, bb-ea) mit „ja“ führen und in Zeile 72 festhalten, dass Grenzwerte bei der Bestimmung von Ableitung oder Integral (h-Methode, Ober- und Untersumme) in keiner Zeile verlangt werden. Für fhr ist der Pool keine Vorgabe: dort gelten RLP FOS 2019 und der fhr-Katalog – nur ganzrationale Funktionen. Die Rohdatei zählt 24 Zeilen mit 8 Haupttypen (fhr 4 Zeilen, 2 Typen; abi 13 Zeilen, 4 Typen; iqb 7 Zeilen, 5 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
92  fhr (4 Zeilen; fhr-Thema „Verhalten im Unendlichen“ 4) [FOS, fhr-Katalog]: Symmetrie am Funktionsterm beurteilen (3, E1) · Verhalten im Unendlichen bestimmen (1, E1). Muster: die Teilaufgabe a der Kurvenuntersuchung in vier Heften 2020–2024 – „Begründen Sie, dass der Graph achsensymmetrisch zur y-Achse verläuft. Geben Sie das Verhalten der Funktion im Unendlichen an.“ (drei Punkte, Symmetrie ein Punkt, Grenzverhalten zwei; fhr 2020-C-1a, 2021-B-1a, 2023-A-1a) oder nur das Grenzverhalten (zwei Punkte; fhr 2024-C-1a), immer an einer ganzrationalen Funktion vierten Grades mit geraden Exponenten oder dritten Grades, Niveau I; in den Heften 2021-A und 2022-B steht dieselbe Frage vor den drei Ableitungen und wird bei ableitungsregeln.md gezählt (2021-A-1a, 2022-B-1a). Die drei Symmetriezeilen tragen den Typ des fhr-Themas „Symmetrie nachweisen“ und stehen hier nach dem Punkt-Schwerpunkt zwei zu eins.
93  abi (13 Zeilen, 4 Typen; Landeshefte bb-ea, be-gk, bb-gk, bebb-gk, bebb-lk 2017–2026, davon 1 aus der Berliner CAS-Fassung 2018) [abi-Katalog]: Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (5, E2) · Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (4, E2) · Grenzverhalten einer ganzrationalen Funktion angeben (3, E1) · Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben (1, E2). Muster: Teil B (mit Hilfsmitteln) trägt alle 13 Zeilen – in fast jedem Heft die Teilaufgabe a oder b der Analysisaufgabe, „Geben Sie das Verhalten der Funktionswerte für x → +∞ und x → −∞ an“, zwei bis drei Punkte, Niveau I, an einem Produkt aus Polynom und e-Funktion (2018-be-gk-B1.2a, 2020-be-gk-B2.1b, 2021-be-gk-B2.2b, 2022-bebb-gk-B2.1b, 2023-bebb-gk-B2.1a, 2023-bebb-lk-B2.1b, 2025-bebb-gk-B2.2a) oder an einer ganzrationalen Funktion (2022-bebb-gk-B2.2a, 2022-bebb-lk-B2.1a, 2026-bb-gk-B2.1a – dort an f'), einmal im Sachzusammenhang mit konstantem Summand (2019-be-gk-B2.2a, Hormonspiegel) und einmal mit Parameter, Nullstellenfreiheit und Symmetrie (2017-bb-ea-B2.2a, sechs Punkte, Niveau II); die Berliner CAS-Fassung 2018 stellt dieselbe Funktion wie 2018-be-gk-B1.2a mit erweitertem Auftrag – beide Richtungen, als „Untersuchen Sie“, vier statt zwei Punkte, das Ergebnis mit dem CAS bestätigt (2018-be-gk-cas-B1.2a, Niveau I). Kein Teil A – obwohl die Anlage das Verhalten im Unendlichen als Teil-A-Stoff führt, stellen die Hefte es nur als Auftakt der Teil-B-Aufgabe. 2 der 13 Zeilen sind wortgleiche Pooldubletten (2022-bebb-gk-B2.1b aus 2022MgrundlegendBAnalysisWTR2-1b, 2025-bebb-gk-B2.2a aus 2025MgrundlegendBAnalysisWTR2-1a); die übrigen elf sind Landeszusätze, die Landeshefte fragen das Grenzverhalten häufiger als der Pool. Niveau I 12, II 1.
94  iqb (7 Zeilen, 5 Typen; Pool 2017–2026, grundlegend 3 und erhöht 4 Zeilen, alle Teil B) [iqb-Katalog]: Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben (2, E2) · Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (2, E2) · je 1: Grenzverhalten einer ganzrationalen Funktion angeben (E1) · Monotonie, Nullstelle und Grenzwert einer e-Funktion am Term begründen (E3) · Nullstellenfreiheit und Grenzwerte eines Bruchs mit e-Funktion am Term begründen (E3). Muster: der Pool stellt das Grenzverhalten seltener und nur in Teil B (Prüfungsteile nach [IQB-STR 1]), als Teilaufgabe a der Analysisaufgabe mit zwei bis vier Punkten und Anforderungsbereich I (einmal II: die Begründung am Term 2020MgrundlegendBAnalysisWTR2-1b); zweimal zusammen mit der Nullstelle (2025MgrundlegendBAnalysisWTR2-1a, 2024MerhoehtBAnalysisWTR3-2a mit Parameter), zweimal mit dem Verlauf in Worten (2022MgrundlegendBAnalysisWTR2-1b, 2020MgrundlegendBAnalysisWTR2-1b) und in den jüngsten Jahrgängen an verschobenen e-Funktionen und Brüchen (2026MerhoehtBAnalysisWTR3-1a, 2024MerhoehtBAnalysisWTR1-1a) – die beiden Zeilen der Einheit 3 sind beide erhöht; dazu seit dem Nachzug die einzige ganzrationale Poolzeile, das Grenzverhalten einer Schar dritten Grades mit positivem Leitkoeffizienten k² (2017MerhoehtBAnalysisWTR2-1a, zwei Punkte, Anforderungsbereich I). Amtlicher Anforderungsbereich in allen 7 Zeilen (höchster Bereich: I 6, II 1); Niveau I 6, II 1. Kontexte: keine (alle sieben ohne Sachzusammenhang). 2 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste).
95  Zielmarke: Einheit 1 – fhr: Symmetrie und Verhalten im Unendlichen als Teilaufgabe a (2023-A-1a, 2020-C-1a, Niveau I); abi: Grenzverhalten einer ganzrationalen Funktion, auch der Ableitungsfunktion (2022-bebb-gk-B2.2a, 2026-bb-gk-B2.1a, Niveau I); iqb: Grenzverhalten einer Schar dritten Grades (2017MerhoehtBAnalysisWTR2-1a, Niveau I). Einheit 2 – fhr: kein Stoff; abi: Grenzverhalten eines Produkts mit quadratischem Faktor (2023-bebb-gk-B2.1a, 2021-be-gk-B2.2b) und mit Parameter (2023-bebb-lk-B2.1b), Nullstelle und Grenzverhalten (2025-bebb-gk-B2.2a), Summe zweier e-Funktionen mit Parameter (2017-bb-ea-B2.2a, Niveau II); iqb: Nullstelle und Grenzverhalten mit Parameter (2024MerhoehtBAnalysisWTR3-2a), Begründung am Term (2020MgrundlegendBAnalysisWTR2-1b, Niveau II). Einheit 3 – fhr: kein Stoff; abi: kein Original; iqb: verschobene e-Funktion mit Monotonie und Nullstelle (2026MerhoehtBAnalysisWTR3-1a) und Bruch mit e-Funktion (2024MerhoehtBAnalysisWTR1-1a), beide Niveau I.
````

## 2 Originale (26)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2020-C-1a (fhr-katalog.csv)

jahr 2020 · papier C · punkte 3 · format Begründung|Kurzantwort · antwort Text
- gegeben: f(x) = x^4 − (82/9)x^2 + 1; x aus IR; der Graph der Funktion heißt Gf
- gesucht: Begründung, dass Gf achsensymmetrisch zur y-Achse verläuft|Verhalten der Funktion f im Unendlichen
- verfahren: die Achsensymmetrie über die ausschließlich geraden Exponenten oder über den Nachweis f(−x) = f(x) begründen und für beide Richtungen den Grenzwert am Summanden höchsten Grades angeben
- fehlerquelle: wegen des Minuszeichens im mittleren Glied auf entgegengesetztes Verhalten in beiden Richtungen schließen

### 2021-B-1a (fhr-katalog.csv)

jahr 2021 · papier B · punkte 3 · format Begründung|Kurzantwort · antwort Text
- gegeben: f(x) = 0,2x^4 − 4,45x^2 + 20; x aus IR
- gesucht: Begründung, dass Gf symmetrisch zur y-Achse verläuft|Verhalten der Funktion im Unendlichen
- verfahren: am Term zeigen, dass alle Exponenten gerade sind beziehungsweise f(x) = f(−x) gilt, dann am Summanden höchsten Grades für beide Richtungen den Grenzwert angeben
- fehlerquelle: das Absolutglied 20 als ungeraden Exponenten werten und Punktsymmetrie vermuten

### 2023-A-1a (fhr-katalog.csv)

jahr 2023 · papier A · punkte 3 · format Begründung|Kurzantwort · antwort Text
- gegeben: f(x) = −(1/8)x^4 + 4x^2 + 8; x aus IR; der Graph heißt Gf; der Punkt Q(2; 22) liegt auf Gf
- gesucht: Begründung für die Achsensymmetrie von Gf zur y-Achse|Verhalten der Funktionswerte von f im Unendlichen
- verfahren: an den ausschließlich geraden Exponenten die Achsensymmetrie erkennen oder f(−x) = f(x) zeigen; am geraden Grad und am negativen Koeffizienten der höchsten Potenz beide Grenzwerte ablesen
- fehlerquelle: beim Verhalten im Unendlichen das negative Vorzeichen der höchsten Potenz übersehen und beide Grenzwerte gegen plus unendlich angeben

### 2024-C-1a (fhr-katalog.csv)

jahr 2024 · papier C · punkte 2 · format Kurzantwort · antwort Text
- gegeben: f(x) = (1/4)x^3 − (23/4)x + 7; x aus IR
- gesucht: Verhalten der Funktion f im Unendlichen
- verfahren: am ungeraden Grad und am positiven Koeffizienten der höchsten Potenz die beiden Grenzwerte ablesen
- fehlerquelle: das Verhalten einer Funktion geraden Grades unterstellen und beide Grenzwerte gleich angeben

### 2021-A-1a (fhr-katalog.csv)

jahr 2021 · papier A · punkte 5 · format Kurzantwort|Rechnung · antwort Text|Term
- gegeben: f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR
- gesucht: Verhalten der Funktion f im Unendlichen|erste, zweite und dritte Ableitung von f
- verfahren: am Summanden höchsten Grades für beide Richtungen den Grenzwert angeben, dann die Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden
- fehlerquelle: das Vorzeichen des negativen Leitkoeffizienten übersehen und beide Grenzwerte vertauschen

### 2022-B-1a (fhr-katalog.csv)

jahr 2022 · papier B · punkte 5 · format Kurzantwort|Rechnung · antwort Text|Term
- gegeben: f(x) = 3x^3 − x^2 − 20x − 12; x aus IR
- gesucht: Verhalten der Funktionswerte im Unendlichen|erste, zweite und dritte Ableitung von f
- verfahren: am Summanden höchsten Grades das Verhalten für beide Richtungen ablesen, dann die Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden
- fehlerquelle: bei ungeradem Grad für beide Richtungen dasselbe Vorzeichen angeben

### 2018-be-gk-B1.2a (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 2 · format Begründung · antwort Text
- gegeben: Funktion f mit f(x) = (x + 1) · e^(−0,5x).
- gesucht: Verhalten der Funktionswerte von f für x → +∞
- verfahren: Der Faktor x + 1 wächst über alle Grenzen, der Faktor e^(−0,5x) fällt gegen null; die Exponentialfunktion ist dabei stärker, also gehen die Funktionswerte gegen null.
- fehlerquelle: aus dem Produkt aus wachsendem und fallendem Faktor auf einen unbestimmten Grenzwert schließen, statt das stärkere Wachstum der Exponentialfunktion zu nutzen

### 2020-be-gk-B2.1b (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: f(x) = (6x − 3) · e^(−x), x ∈ IR
- gesucht: Verhalten der Funktionswerte für x → +∞ und x → −∞
- verfahren: Dominanz des Exponentialfaktors
- fehlerquelle: für x → −∞ wegen e^(−x) → ∞ das Vorzeichen des ersten Faktors übersehen

### 2021-be-gk-B2.2b (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: f(x) = (−1/10 x² + 2x) · e^(−0,1x) und h(x) = −3/4 x · e^(−0,1x), beide in IR; Graphen G und H
- gesucht: Verhalten von f für x → +∞ und x → −∞
- verfahren: Grenzwertbetrachtung
- fehlerquelle: Vorzeichen des quadratischen Terms für x → −∞ übersehen

### 2022-bebb-gk-B2.1b (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Kurzantwort · antwort Zahl|Text
- gegeben: f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x)
- gesucht: Grenzwert von f für x → +∞; Verlauf des Graphen dort
- verfahren: e^(−x) fällt schneller als x + 2 wächst
- fehlerquelle: Grenzwert ∞ wegen des Faktors x + 2

### 2023-bebb-gk-B2.1a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Die in IR definierte Funktion f mit f(x) = 0,5 · (x² − 4) · e^x, ihr Graph G; die erste Ableitung ist f'(x) = (0,5x² + x − 2) · e^x.
- gesucht: Verhalten der Funktionswerte für x → +∞ und für x → −∞
- verfahren: Für x → +∞ wachsen beide Faktoren, für x → −∞ geht e^x schneller gegen 0, als x² − 4 wächst.
- fehlerquelle: für x → −∞ aus x² − 4 → ∞ auf f(x) → ∞ schließen

### 2023-bebb-lk-B2.1b (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: f_a(x) = (4a − x) · e^(x/2), definiert in IR, a ≠ 0, Graph G_a
- gesucht: Verhalten von f_a(x) für x → +∞ und x → −∞
- verfahren: Faktoren einzeln betrachten
- fehlerquelle: für x → −∞ das Vorzeichen von a einbringen

### 2025-bebb-gk-B2.2a (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 3 · format Kurzantwort · antwort Zahl
- gegeben: f(x) = (2 − x) · e^x in IR; Graph in Abbildung 1
- gesucht: Nullstelle und Verhalten für x → −∞ und x → +∞
- verfahren: Faktoren betrachten
- fehlerquelle: Verhalten für x → +∞ als +∞ (Vorzeichen von 2 − x übersehen)

### 2022-bebb-gk-B2.2a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: f(x) = −1/6 x³ + 1/2 x², x ∈ IR
- gesucht: Verhalten der Funktionswerte für x → +∞ und x → −∞
- verfahren: Leitterm betrachten
- fehlerquelle: Vorzeichen des Leitkoeffizienten übersehen

### 2022-bebb-lk-B2.1a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: f_a(x) = 1/8 x⁴ − a/12 x³ + 2x, definiert in IR, a ∈ IR, Graph G_a; f_a'(x) = 1/2 x³ − a/4 x² + 2
- gesucht: Verhalten von f_0(x) für x → +∞ und x → −∞
- verfahren: Grad 4, Leitkoeffizient positiv
- fehlerquelle: am Summanden 2x −∞ für x → −∞ ablesen

### 2026-bb-gk-B2.1a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Kurzantwort · antwort Text
- gegeben: f'(x) = x² · (1/3 x + 1) = 1/3 x³ + x², Ableitung der in IR definierten Funktion f mit f(x) = 1/12 (x⁴ + 4x³ + 24); Abbildung 1 zeigt den Graphen von f'
- gesucht: Verhalten von f' für x → −∞ und x → +∞
- verfahren: Grad 3, Leitkoeffizient positiv
- fehlerquelle: Verhalten von f statt f' angeben

### 2019-be-gk-B2.2a (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 3 · format Begründung · antwort Text
- gegeben: Hormonspiegel h(t) = 8t · e^(−0,04t) + 50, t ≥ 0 Zeit in Tagen ab Behandlungsbeginn, h(t) Anteil am Sollwert in Prozent (Ausgangswert 50 %)
- gesucht: Verhalten der Funktionswerte von h für t → +∞
- verfahren: Der Faktor e^(−0,04t) geht schneller gegen 0, als t wächst; der Summand 50 bleibt
- fehlerquelle: wegen des Faktors 8t Wachstum gegen unendlich annehmen

### 2017-bb-ea-B2.2a (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 6 · format Kurzantwort|Begründung · antwort Term|Text
- gegeben: Funktionenschar f_a mit f_a(x) = e^(2ax) + e^(−2ax); x ∈ IR, a ∈ IR, a ≠ 0. Die zugehörigen Graphen sind G_a.
- gesucht: Verhalten der Funktionswerte für a > 0 bei x → +∞ und bei x → −∞; Begründung, dass keine Funktion f_a eine Nullstelle hat; Nachweis, dass alle Graphen G_a achsensymmetrisch zur y-Achse verlaufen
- verfahren: Für a > 0 wächst e^(2ax) bei x → +∞ unbeschränkt, während e^(−2ax) gegen null geht; bei x → −∞ vertauschen sich die Rollen. Beide Summanden sind stets positiv, also ist f_a(x) > 0. Für die Symmetrie f_a(−x) bilden und mit f_a(x) vergleichen.
- fehlerquelle: beim Grenzverhalten nur den wachsenden Summanden betrachten und das Vorzeichen von a außer Acht lassen

### 2018-be-gk-cas-B1.2a (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk-cas · punkte 4 · format Begründung · antwort Text
- gegeben: Funktionen f mit f(x) = (x + 1) · e^(−0,5x) und g mit g(x) = x + 1.
- gesucht: Verhalten der Funktionswerte von f für x → −∞ und für x → ∞
- verfahren: Für x → ∞ wächst x + 1 über alle Grenzen, e^(−0,5x) fällt gegen null; die Exponentialfunktion ist stärker, also f(x) → 0. Für x → −∞ geht x + 1 gegen −∞ und e^(−0,5x) gegen +∞, das Produkt also gegen −∞ (mit dem CAS bestätigen).
- fehlerquelle: für x → −∞ nur den Faktor e^(−0,5x) betrachten und auf +∞ schließen

### 2022MgrundlegendBAnalysisWTR2-1b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Kurzantwort · antwort Zahl|Text
- gegeben: f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x)
- gesucht: Grenzwert von f für x → +∞; Verlauf des Graphen dort
- verfahren: e^(−x) fällt schneller als x + 2 wächst
- fehlerquelle: Grenzwert ∞ wegen des Faktors x + 2

### 2025MgrundlegendBAnalysisWTR2-1a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 3 · format Kurzantwort · antwort Zahl
- gegeben: f(x) = (2 − x) · e^x in IR; Graph in Abbildung 1
- gesucht: Nullstelle und Verhalten für x → −∞ und x → +∞
- verfahren: Faktoren betrachten
- fehlerquelle: Verhalten für x → +∞ als +∞ (Vorzeichen von 2 − x übersehen)

### 2020MgrundlegendBAnalysisWTR2-1b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: f(x) = 1/10 · x · (3 − x) · eˣ, x ∈ IR; Abbildung 1 zeigt den Graphen von f; f'(x) = −1/10 · (x² − x − 3) · eˣ
- gesucht: Verlauf des Graphen für x → −∞ mit Begründung am Term
- verfahren: Grenzwert von eˣ nennen und den Faktor x · (3 − x) als untergeordnet begründen
- fehlerquelle: aus x · (3 − x) → −∞ auf f → −∞ schließen

### 2024MerhoehtBAnalysisWTR3-2a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Begründung|Kurzantwort · antwort Text
- gegeben: f_k(x) = k · (x + 10) · e^{−0,1x}, k ≠ 0
- gesucht: Begründung der einzigen Nullstelle −10; Verhalten für x → −∞ nach k
- verfahren: Faktoren betrachten, Fallunterscheidung nach dem Vorzeichen von k
- fehlerquelle: Fallunterscheidung nach k vergessen

### 2026MerhoehtBAnalysisWTR3-1a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Begründung|Kurzantwort · antwort Text
- gegeben: f(x) = 5 · e^{−3/5 x} − 5 in IR
- gesucht: Begründung: streng monoton fallend und durch den Ursprung; Grenzwert für x → +∞
- verfahren: Term als Transformation von e^−x lesen
- fehlerquelle: Grenzwert 0 statt −5

### 2024MerhoehtBAnalysisWTR1-1a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 3 · format Begründung|Kurzantwort · antwort Zahl
- gegeben: f(x) = 4/(1 + e^x) in IR; Graph symmetrisch zum Wendepunkt (0 | 2)
- gesucht: Begründung ohne Nullstelle; Grenzwerte für x → ±∞
- verfahren: Zähler betrachten, Nenner für beide Grenzfälle
- fehlerquelle: Grenzwerte vertauschen

### 2017MerhoehtBAnalysisWTR2-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Für jedes k ∈ IR+ ist die Funktion f_k mit f_k(x) = k^2x^3 − 6kx^2 + 9x, x ∈ IR, gegeben; ihr Graph heißt G_k
- gesucht: Verhalten von f_k für x → −∞ und x → +∞
- verfahren: Der Leitterm k^2x^3 hat ungeraden Grad und positiven Koeffizienten
- fehlerquelle: den Leitkoeffizienten k^2 für negativ halten, weil k gesucht ist

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

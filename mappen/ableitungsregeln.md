# Mappe: ableitungsregeln

Eintrag: hz-0801/mathe-nachhilfe, katalog/ableitungsregeln.md
Katalog-Commit: f56cacecc590f51abf34cf81948a0d2b751d7d33 (2026-09-28T22:13:08Z, „Katalog-Nachzug Teil 5: Abschluss“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-29 12:26 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Ableitungsregeln
  3
  4  ### Verortung
  5  Das Bilden der Ableitungsfunktion nach Regeln: Potenz-, Faktor-, Summen- und Konstantenregel für ganzrationale Funktionen bis zur dritten Ableitung, auch mit Parameter und in vorgegebener faktorisiert … (gekürzt, 2907 Zeichen)
  6  [GOST] Q1, 1. Kurshalbjahr „Analysis; Lineare Algebra“ (BB S. 23–25), Grund- und Leistungskursfach, Funktionsklassen Potenzfunktionen mit ganzzahligem Exponenten, ganzrationale Funktionen, natürliche  … (gekürzt, 3870 Zeichen)
  7  [FOS] L4 (S. 24): „Ableitungsfunktionen ganzrationaler Funktionen unter Verwendung der Konstanten-, Potenz-, Faktor- und Summenregel bestimmen und interpretieren“. Pflichtthema 2 „Differentialrechnung … (gekürzt, 1332 Zeichen)
  8  [LS-AA] Einführungsphase Kapitel II „Schlüsselkonzept: Ableitung – Differenzialrechnung“: 5 Die Ableitung von Potenzfunktionen – Potenzregel · 6 Faktor- und Summenregel (1–4 → ableitung-und-aenderungs … (gekürzt, 2213 Zeichen)
  9
 10  ### Lerneinheiten
 11  1. Potenz-, Faktor- und Summenregel – ganzrationale Funktionen ableiten: Exponent als Faktor davor, Exponent um eins senken; Vorfaktor bleibt, Konstante fällt weg; Summanden einzeln; Bruch- und Dezima … (gekürzt, 972 Zeichen)
 12    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR
 13  2. Kettenregel – Verkettungen mit linearer oder quadratischer innerer Funktion: innere und äußere Funktion erkennen, äußere Ableitung an der inneren Funktion mal innere Ableitung; e^(kx) und e^(ax + b … (gekürzt, 818 Zeichen)
 14    Marken: BE Q1 · BB Q1 · GK · keine Prüfungsaufgabe
 15  3. Produktregel – Produkte aus Polynom und e-Funktion: (u · v)' = u' · v + u · v', fast immer mit der Kettenregel für den e-Faktor zusammen; den e-Term ausklammern und den Polynomfaktor zusammenfassen … (gekürzt, 788 Zeichen)
 16    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK
 17  Warum drei: Der Plan nennt die Regeln in einer Zeile, das Lehrwerk trennt Potenz-, Faktor- und Summenregel (EP II 5–6), Verkettung und Kettenregel (QP I 2–3) und Produktregel (QP I 4); die Rohdatei tr … (gekürzt, 1334 Zeichen)
 18
 19  ### Typen je Lerneinheit
 20  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
 21  Einheit 1: Ableitung ganzrationale Funktion (6) — Nachweis: Ableitung mit Parameter in faktorisierter Form nachweisen (3) · Ableitung als Quadrat eines Produkts von Linearfaktoren nachweisen (1) — Deutung: Verhalten im Unendlichen bestimmen (2; Ermessen, siehe Offene Punkte – zwei fhr-Zeilen, deren Punkt-Schwerpunkt bei den drei Ableitungen liegt, der Typ gehört zu grenzwerte-und-verhalten-im-unendlichen.md) · Ableitungsfunktion und Stammfunktion einer ganzrationalen Funktion angeben (1). Dazu: Fehler finden (der Exponent nicht gesenkt; der Vorfaktor nicht mit dem Exponenten multipliziert; die Konstante beim Ableiten mitgeführt; der Parameter wie eine Variable abgeleitet; beim Aufleiten der Exponent nicht erhöht) · Begründen (warum die Konstante beim Ableiten wegfällt; warum ein Parameter beim Ableiten nach x eine Zahl ist).
 22  Einheit 2: Tangente an eine Verkettung aus zwei abgebildeten Graphen über die Kettenregel bestimmen (1) · Verschiebung zwischen Graph und hundertster Ableitung berechnen (1) — Deutung: Term einer höheren Ableitung einer Sinusfunktion über die Periodizität der Ableitungen angeben (1; Ermessen, siehe Offene Punkte). Dazu: Fehler finden (die innere Ableitung vergessen; die äußere Ableitung an x statt an der inneren Funktion gebildet; bei e^(kx) den Faktor k als Exponent behandelt; die wiederholte Ableitung von e^(2x) als Streckung statt als Verschiebung gedeutet) · Begründen (warum die Ableitung von e^(kx) den Faktor k trägt; warum der Graph von c · e^(2x) eine Verschiebung des Graphen von e^(2x) ist).
 23  Einheit 3: Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden (3) · Ableitung eines Produkts aus Graphenwerten mit der Produktregel bestimmen (1) — Nachweis: Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen (8) · Bedingung für eine waagerechte Tangente eines Produkts mit e^x nachweisen (1). Dazu: Fehler finden (nur die Faktoren einzeln abgeleitet und multipliziert; die innere Ableitung des e-Terms vergessen; der Vorfaktor nur bei einem Summanden; nach dem Ausklammern nicht zusammengefasst und die vorgegebene Form nicht erreicht; am Extrempunkt f'(x₀) = 0 nicht erkannt) · Begründen (warum man den e-Term ausklammern kann und warum er die Nullstellen nicht ändert; warum g'(a) = 0 für g = f · e^x auf f'(a) = −f(a) führt).
 24  Zählung: 5 + 3 + 4 = 12 Haupttypen, 13 + 3 + 13 = 29 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: CAS-Nachtrag 2018, Pool 2017 grundlegend und erhöht Teil B; nachgezogen 2026-09-29 um die Katalogzeile des CAS-Nachtrags: Berliner CAS-Heft 2017 GK).
 25
 26  ### Voraussetzungen (Blatt 0)
 27  Fertigkeiten (je Zeile: was, wofür):
 28  - Potenzen mit natürlichem Exponenten lesen und schreiben, Vorfaktor und Exponent unterscheiden, Potenzgesetze (Produkt gleicher Basen, Potenz einer Potenz), negative Exponenten als Kehrwert, Wurzel als Potenz mit Exponent ein Halb – die Potenzregel in Einheit 1 hängt am Unterschied zwischen Vorfaktor und Exponent; negative und rationale Exponenten für den Vorrat. Sek-I-Themen potenzen-wurzeln.md, reelle-zahlen.md. [GOST Eingangsvoraussetzung L1 „lösen Potenz- und Wurzelgleichungen unter Nutzung der entsprechenden Gesetze“, L4 „verwenden … Potenzen, Wurzeln“; RLP G Potenzgesetze; FOS Pflichtthema 2 „Potenzregel (auch mit negativen Exponenten)“]
 29  - Terme umformen: ausmultiplizieren, zusammenfassen, ausklammern (auch einen gemeinsamen e-Faktor), binomische Formeln vorwärts und rückwärts, Produkt von Linearfaktoren ausmultiplizieren – jeder Nachweis in vorgegebener Form in Einheit 1 und 3. Sek-I-Themen terme.md, binomische-formeln.md. [GOST Eingangsvoraussetzung L4 „wechseln zwischen unterschiedlichen Darstellungen quadratischer Funktionen, u. a. als Produkt von Linearfaktoren“; RLP F–G Terme, binomische Formeln; FOS Pflichtthema 1 „Zerlegung in Linearfaktoren“]
 30  - Bruch- und Dezimalkoeffizienten multiplizieren (ein Viertel mal fünf, null Komma vier mal vier), mit Brüchen kürzen – die fhr-Terme tragen fast alle solche Koeffizienten, Einheit 1. Sek-I-Themen bruchrechnung.md, brueche-dezimalzahlen.md. [RLP D–E Bruchrechnung; FOS Pflichtthema 1 ganzrationale Funktionen]
 31  - Die e-Funktion als Funktion, die sich selbst als Ableitung hat; e^(kx) als Verkettung lesen; e^x ist nie null und immer positiv – Grundlage von Einheit 2 und 3 und des Ausklammerns. Thema potenz-exponentialfunktionen.md (Sek I, e als Vorrat) und funktionsklassen-und-eigenschaften.md. [GOST Q1 L4 „natürliche Exponentialfunktion als Funktion charakterisieren, die sich selbst als Ableitung hat“; GOST-OHiMi 2.2 „Ableitungsfunktionen der zu behandelnden Funktionsklassen“; FS-IQB 1.2 Tabelle der Ableitungen]
 32  - Ableitung als Tangentensteigung und Änderungsrate deuten, Ableitungswert an einer Stelle als Steigung lesen, Extrempunkt als Stelle mit waagerechter Tangente – für die Graphenaufgaben in Einheit 2 und 3 (Werte am Graphen ablesen, die Steigung null am Tiefpunkt erkennen). Thema ableitung-und-aenderungsrate.md (dasselbe Kurshalbjahr, im Lehrwerk EP II 1–4 vor den Regeln). [GOST Q1 L4 „lokale Änderungsrate und Anstieg der Tangente“; GOST-OHiMi 2.2 „Ableitung an einer Stelle, momentane Änderungsrate, Tangentensteigung“; FOS „Tangentenanstieg“]
 33  - Funktionswerte berechnen und Punktprobe, Anstieg an einer Stelle als Wert der ersten Ableitung – die Anschlussleistungen der fhr-Zeilen (Punkt auf dem Graphen, Anstieg im Achsenschnittpunkt, Anstiege vergleichen). Sek-I-Thema lineare-funktionen.md; fhr-Typ „Anstieg des Graphen an einer Stelle berechnen“ bei tangente-normale-schnittwinkel.md. [GOST Eingangsvoraussetzung L4; FOS Pflichtthema 1 „Anstieg“, „Funktionsdarstellungen“]
 34  - Verschiebung und Streckung eines Graphen an der Gleichung erkennen (f(x − c) verschiebt nach rechts, c · f(x) streckt) – nur für die Prüfungshöhe von Einheit 2 (hundertste Ableitung als Verschiebung). Thema funktionsklassen-und-eigenschaften.md; Sek-I-Vorläufer quadratische-funktionen.md (Scheitelpunktform). **Ermessen:** die Eingangsvoraussetzung nennt Verschiebungen nur für quadratische Funktionen; gesetzt, weil die eine Poolzeile 2024MerhoehtAAnalysis23 genau daran scheitert („als Streckung deuten und keine Verschiebung finden“). [Ermessen; GOST-OHiMi 2.2 „Zusammenhang zwischen Funktionsgraph und Funktionsgleichung nach … Verschiebung“, „Streckung“; RLP G Scheitelpunktform]
 35  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 36  - „Welche Regel?“ – zu Funktionstermen ankreuzen, was zu tun ist: Summe von Potenzen (Potenz-, Faktor-, Summenregel), Verkettung mit e-Funktion oder Klammer hoch n (Kettenregel), Produkt aus zwei Faktoren mit x (Produktregel, meist mit Kettenregel), oder eine Mischung – und in welcher Reihenfolge; nichts rechnen. Vor Einheit 1 bis 3. [GOST Q1 L4 „Funktionen ableiten, auch unter Verwendung der Konstanten-, Potenz-, Faktor-, Summen-, Produkt- und Kettenregel“; Rohdatei-Fehlerquelle „g' = f' · e^x ohne Produktregel ansetzen“ (2025MerhoehtAAnalysis21-a); fhr 2024-C-1c, abi 2022-bebb-lk-B2.2b]
 37  - „Zahl oder Variable?“ – zu Termen mit Buchstaben ankreuzen, nach welcher Variablen abgeleitet wird und welche Buchstaben dabei Zahlen sind (Parameter a, k; Werte f(x₀), g'(x₀) aus einer Abbildung); nichts rechnen. Vor Einheit 1 und 3. [GOST Q1 L4 LK „Scharen mit einem Parameter“; Rohdatei-Fehlerquellen „k beim Ableiten wie eine Variable behandeln“ (2021MerhoehtAAnalysis12-a), „Ableitung von (1 − ax) als −ax“ (2022-bebb-lk-A1.4a)]
 38
 39  ### Merkkasten
 40  Einheit 1 (Potenz-, Faktor- und Summenregel):
 41      Potenzregel: xⁿ wird abgeleitet zu n · xⁿ⁻¹ – der Exponent kommt als Faktor nach vorn, der Exponent wird um eins kleiner. Faktorregel: ein Vorfaktor bleibt stehen und wird mit dem Exponenten multipliziert. Summenregel: jeder Summand einzeln. Konstantenregel: eine Zahl ohne x fällt weg.
 42        f(x) = 2x⁵ − 3x² + 7: f'(x) = 10x⁴ − 6x.
 43      Höhere Ableitungen: dieselben Regeln noch einmal auf f', dann auf f''.
 44        f''(x) = 40x³ − 6, f'''(x) = 120x².
 45      Brüche und Dezimalzahlen als Vorfaktor: der Exponent wird mit dem Vorfaktor multipliziert, das Ergebnis gekürzt.
 46        g(x) = 1/4 · x⁴ − 0,5x: g'(x) = x³ − 0,5.
 47      Parameter: ein Buchstabe, der nicht x ist, wird wie eine Zahl behandelt.
 48        f_k(x) = x³ − k · x: f_k'(x) = 3x² − k.
 49      Vorgegebene Form: erst ableiten, dann ausklammern oder mit binomischen Formeln faktorisieren; oder die vorgegebene Form ausmultiplizieren und mit der eigenen Ableitung vergleichen – beides gilt als Nachweis.
 50        p(x) = x⁴ − 2x²: p'(x) = 4x³ − 4x = 4x · (x² − 1) = 4x · (x − 1) · (x + 1). h'(x) = x⁴ − 2x² + 1 = (x² − 1)² = ((x − 1) · (x + 1))².
 51      Stammfunktion (Umkehrung): Exponent um eins erhöhen, durch den neuen Exponenten teilen; eine Stammfunktion ohne Konstante genügt, wenn nur „eine“ verlangt ist.
 52        F(x) = 2/6 · x⁶ − x³ + 7x = 1/3 · x⁶ − x³ + 7x zu f(x) = 2x⁵ − 3x² + 7.
 53      Auswendig (Teil A): „Potenzregel“, „Faktorregel“, „Summenregel“, „Konstantenregel“ und „Höhere Ableitungen“ – [GOST-OHiMi 2.2] „Ableitungsregeln: Konstantenregel, Faktorregel, Potenzregel, Summenregel“; „Brüche und Dezimalzahlen“ und „Parameter“ sind Anwendung derselben Regeln, „Vorgegebene Form“ ist Termumformung; die „Stammfunktion“ steht in der Anlage unter Integrationsregeln (Potenzregel) und gehört zu stammfunktion-und-hauptsatz.md.
 54      Formelsammlung: Analysis – Ableitungen ausgewählter Funktionen [FS-IQB 1.2] „xʳ → r · xʳ⁻¹“ und Ableitungsregeln „k · u(x) → k · u'(x)“, „u(x) + v(x) → u'(x) + v'(x)“; die Konstantenregel steht nicht eigens darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 55  Quelle: eigene Formulierung nach [GOST Q1 L4] „Funktionen ableiten, auch unter Verwendung der Konstanten-, Potenz-, Faktor-, Summen- … regel“, [GOST-OHiMi 2.2] und [FOS] „Ableitungsregeln: Konstanten-, Faktor-, Summen- und Potenzregel“, „höhere Ableitungen“; Formeln in der Notation von [FS-IQB 1.2]; Zahlenbeispiele eigen (Ermessen; keine Zahl aus einer Rohdateizeile übernommen); [LS-AA EP II 5–6, QP I 1].
 56
 57  Einheit 2 (Kettenregel):
 58      Kettenregel: Ist f(x) = u(v(x)) eine Verkettung mit äußerer Funktion u und innerer Funktion v, dann ist f'(x) = u'(v(x)) · v'(x) – äußere Ableitung an der inneren Funktion, mal innere Ableitung.
 59      Lineare innere Funktion: e^(kx) hat die Ableitung k · e^(kx); e^(ax + b) die Ableitung a · e^(ax + b); (ax + b)ⁿ die Ableitung n · a · (ax + b)ⁿ⁻¹.
 60        f(x) = e^(3x): f'(x) = 3 · e^(3x). g(x) = (2x − 1)⁴: g'(x) = 4 · 2 · (2x − 1)³ = 8 · (2x − 1)³.
 61      Quadratische innere Funktion: e^(x²) hat die Ableitung 2x · e^(x²); e^(−x²/2) die Ableitung −x · e^(−x²/2).
 62        h(x) = e^(−x²/2): h'(x) = −x · e^(−x²/2).
 63      Wiederholt ableiten: bei e^(kx) kommt mit jeder Ableitung ein Faktor k dazu – die n-te Ableitung ist kⁿ · e^(kx). Der Graph von c · e^(kx) ist der Graph von e^(kx), in x-Richtung verschoben (c = e^(k · d) ⇔ Verschiebung um d nach links).
 64        f(x) = e^(3x): f''(x) = 9 · e^(3x), f'''(x) = 27 · e^(3x).
 65      Am Graphen: Sind f und g nur als Graphen gegeben und h = g(f(x)), dann ist h'(x₀) = g'(f(x₀)) · f'(x₀) – erst f(x₀) ablesen, dann die Steigung von g an dieser Stelle und die Steigung von f an x₀; an einem Extrempunkt ist die Steigung null.
 66      Auswendig (Teil A): „Kettenregel“, „Lineare innere Funktion“ und „Quadratische innere Funktion“ – [GOST-OHiMi 2.2] „Kettenregel“, [GOST Q1 L4] „Kettenregel mit linearer bzw. quadratischer innerer Funktion“, „natürliche Exponentialfunktion als Funktion …, die sich selbst als Ableitung hat“; „Wiederholt ableiten“ und „Am Graphen“ sind Anwendungen, die der Pool in Teil A auf erhöhtem Niveau prüft (2024MerhoehtAAnalysis23, 2020MerhoehtAAnalysis22).
 67      Formelsammlung: Analysis – Ableitungsregeln [FS-IQB 1.2] „u(v(x)) → u'(v(x)) · v'(x)“ und „eˣ → eˣ“; die Sonderfälle e^(kx) stehen nicht eigens darin – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 68  Quelle: eigene Formulierung nach [GOST Q1 L4] „Kettenregel mit linearer bzw. quadratischer innerer Funktion“, „Verkettungen von ganzrationalen Funktionen und natürlichen Exponentialfunktionen“ und [GOST-OHiMi 2.2]; Formel in der Notation von [FS-IQB 1.2]; Verschiebungsregel und Graphenfall aus den Rohdateizeilen (2024MerhoehtAAnalysis23, 2020MerhoehtAAnalysis22); Zahlenbeispiele eigen (Ermessen); [LS-AA QP I 2–3, QP II 1].
 69
 70  Einheit 3 (Produktregel):
 71      Produktregel: (u · v)' = u' · v + u · v' – jeden Faktor einmal ableiten, den anderen stehen lassen, beides addieren. Bei einem e-Faktor mit Exponent kx kommt die Kettenregel dazu.
 72        f(x) = x · e^(−x): f'(x) = 1 · e^(−x) + x · (−1) · e^(−x) = (1 − x) · e^(−x).
 73      Ausklammern: den e-Term ausklammern und den Polynomfaktor zusammenfassen – so entsteht die Form, die die Aufgabe vorgibt; der e-Term ist nie null, die Nullstellen von f' sind die des Polynomfaktors.
 74        f(x) = (x² + 1) · e^(2x): f'(x) = 2x · e^(2x) + (x² + 1) · 2 · e^(2x) = (2x² + 2x + 2) · e^(2x) = 2 · (x² + x + 1) · e^(2x).
 75      Nachweis einer vorgegebenen Ableitung: eigene Ableitung bilden, ausklammern, zusammenfassen und mit der Vorgabe vergleichen – oder die Vorgabe ausmultiplizieren; bei f'' die Produktregel auf f' noch einmal anwenden.
 76      Allgemeines f: Für g(x) = f(x) · eˣ gilt g'(x) = f'(x) · eˣ + f(x) · eˣ = (f'(x) + f(x)) · eˣ; aus g'(a) = 0 folgt f'(a) + f(a) = 0, weil eᵃ ≠ 0.
 77      Am Graphen: h = f · g mit abgelesenen Werten: h'(x₀) = f'(x₀) · g(x₀) + f(x₀) · g'(x₀); an einem Tief- oder Hochpunkt von f ist f'(x₀) = 0, die Steigung einer Geraden liest man am Steigungsdreieck ab.
 78      Auswendig (Teil A): „Produktregel“, „Ausklammern“ und „Allgemeines f“ – [GOST-OHiMi 2.2] „Produktregel“, „Kettenregel“; der Pool prüft die Regel mit allgemeinem f und mit Graphenwerten in Teil A (2025MerhoehtAAnalysis21-a, 2026MgrundlegendAAnalysis21-b); „Nachweis einer vorgegebenen Ableitung“ und „Am Graphen“ sind Arbeitsregeln.
 79      Formelsammlung: Analysis – Ableitungsregeln [FS-IQB 1.2] „u(x) · v(x) → u'(x) · v(x) + u(x) · v'(x)“ – die Formelsammlung ist in Teil B zugelassen, die Anlage verlangt die Regel in Teil A auswendig – [FS] Wortlaut am PDF geprüft: nein, nur Textfassung
 80  Quelle: eigene Formulierung nach [GOST Q1 L4] „Produktregel“, „multiplikative Verknüpfungen zweier Funktionen“ und [GOST-OHiMi 2.2]; Formel in der Notation von [FS-IQB 1.2]; Nachweisweg und Graphenfall aus den Rohdateizeilen (Landeshefte: „Weisen Sie nach“, Pool: „Zeigen Sie“, 2026MgrundlegendAAnalysis21-b); Zahlenbeispiele eigen (Ermessen); [LS-AA QP I 4].
 81
 82  ### Typische Fehler
 83  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 24 Zeilen des Themas in fhr/fhr-katalog.csv, abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nur, wo die Kataloge das Muster stützen.
 84  - Innere Ableitung vergessen: bei e^(−x), e^(−0,2x), e^(−t/100) und e^(−x²/2) den Faktor −1, −0,2, −1/100 bzw. −x nicht gebildet – das häufigste Muster in abi und iqb, in jeder zweiten Produktzeile. [abi 2022-bebb-lk-B2.2b, 2020-be-gk-B2.1c, 2024-bebb-lk-B2.1d; iqb 2022MerhoehtBAnalysisWTR2-1b, 2021MerhoehtAAnalysis13-a]
 85  - Potenzregel unvollständig: den Exponenten nicht gesenkt oder den Vorfaktor nicht mit dem Exponenten multipliziert (18,75 mal 4, ein Viertel mal 5), das absolute Glied beim ersten Ableiten mitgeführt, den Bruchkoeffizienten falsch behandelt, beim Aufleiten den Exponenten nicht erhöht oder den Faktor 1/2 bei x²/2 vergessen. [fhr 2026-C-1c, 2025-C-1c, 2026-B-1c, 2021-A-1a; abi 2019-be-gk-A1.1a; FD Potenz als Produkt von Basis und Exponent, Malle]
 86  - Produktregel weggelassen oder verkürzt: g' = f' · e^x ohne Produktregel angesetzt, h'(3) als f'(3) · g'(3) gebildet, die Ableitung von (1 − ax) als −ax, den Faktor 2 beim zweiten Summanden vergessen, den Parameter k wie eine Variable abgeleitet. [iqb 2025MerhoehtAAnalysis21-a, 2026MgrundlegendAAnalysis21-b, 2024MgrundlegendBAnalysisWTR1-1a, 2021MerhoehtAAnalysis12-a; abi 2022-bebb-lk-A1.4a]
 87  - Vorgegebene Form nicht erreicht: die Produktregel am faktorisierten Term angewendet und nicht zusammengefasst, Vorzeichen beim Faktorisieren, x⁴ − 8x² + 16 nicht als Quadrat erkannt (das Ausmultiplizieren der Vorgabe ist gleichwertig), die hundertste Ableitung 2¹⁰⁰ · e^(2x) als Streckung gedeutet und keine Verschiebung gefunden. [abi 2025-bebb-lk-B2.1b; iqb 2022MgrundlegendBAnalysisWTR1-1c, 2024MerhoehtAAnalysis23]
 88  - Am Graphen falsch gelesen: f'(4) am Graphen geschätzt und mit einer geschätzten Steigung von g gerechnet, statt den Tiefpunkt mit g' = 0 zu erkennen; f'(3) am Tiefpunkt nicht als null erkannt. [iqb 2020MerhoehtAAnalysis22, 2026MgrundlegendAAnalysis21-b]
 89  - Anschluss an die Kurvenuntersuchung: aus der Punktprobe allein auf einen Extrempunkt geschlossen, ohne f'(3) zu prüfen; den Anstieg über f(0) statt über f'(0) angegeben; die Beträge der Anstiege verglichen und −16 für größer gehalten; die Nullstelle von f'' als Wendestelle gedeutet, ohne den Vorzeichenwechsel zu prüfen (Quadrat); die Extremstellen zusätzlich mit f'' geprüft, obwohl nur die möglichen Stellen verlangt waren. [fhr 2024-B-1d, 2024-C-1c, 2023-C-1b; abi 2018-bb-ea-B2.1e, 2024-bebb-lk-B2.1d]
 90  - Verhalten im Unendlichen an der fhr-Auftaktaufgabe: bei ungeradem Grad für beide Richtungen dasselbe Vorzeichen, den negativen Leitkoeffizienten übersehen und beide Grenzwerte vertauscht – gehört zu grenzwerte-und-verhalten-im-unendlichen.md, steht hier, weil die Zeilen hier geführt werden. [fhr 2022-B-1a, 2021-A-1a]
 91
 92  ### Für schwache Schüler
 93  Mindeststoff (GK-Kern Q1 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q1 (Funktionsklassen ganzrational, Potenz- und natürliche Exponentialfunktionen): Einheit 1 „Konstanten-, Potenz-, Faktor-, Summenregel“; Einheit 2 „Kettenregel mit linearer bzw. quadratischer innerer Funktion“, „Verkettungen von ganzrationalen Funktionen und natürlichen Exponentialfunktionen“, e-Funktion als ihre eigene Ableitung; Einheit 3 „Produktregel“, „multiplikative Verknüpfungen zweier Funktionen“. Ohne Hilfsmittel (Anlage OHiMi 2.2, Prüfungsteil A): alle sechs Regeln und die Ableitungsfunktionen der Funktionsklassen. LK-Zusatz (für GK Vorrat): Kettenregel für alle Klassen, Ableitungen von Wurzel-, ln-, Sinus- und Kosinusfunktionen (kein Original in der Rohdatei), Berlin zusätzlich die Quotientenregel (im Pool nicht vorausgesetzt, kein Original). Niveaustufe H der E-Phase [RLP H]: keine Ableitungsregel – der Sek-I-Plan führt nur „Beschreiben des Änderungsverhaltens … durch eine Skizze der Ableitungsfunktion“; die Regeln beginnen in der Q1 (Berlin: Einführungsphase nur „grafisches Differenzieren“). RLP FOS (fhr) [FOS Pflichtthema 2 „Ableitungsbegriff“]: „Ableitungsregeln: Konstanten-, Faktor-, Summen- und Potenzregel (auch mit negativen Exponenten)“, „höhere Ableitungen“ – Einheit 1 vollständig mit ganzrationalen Funktionen bis zum fünften Grad; negative Exponenten ohne Original; Einheit 2 und 3 kein Stoff. Vorrat: alles außerhalb dieser Listen, für fhr insbesondere alle e-Funktions-Produkte (Einheit 2 und 3, 12 der 24 Zeilen), für GK die Teil-A-Zeilen mit Anforderungsbereich III (allgemeines f, hundertste Ableitung, Verkettung am Graphen) und die Wurzelfunktion. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung Potenz-, Summen-, Faktor-, Produkt-, Quotienten- und Kettenregel – für fhr reicht der RLP FOS darunter (keine Produkt- und Kettenregel), ein Posten, der die Lücke zwischen FHR und Hochschulerwartung markiert, für den Katalog aber keine Vorgabe.
 94  Grundvorstellung (Blatt 0) [GOST Eingangsvoraussetzung L4, GOST Q1 L4, MO]: Die Ableitungsfunktion ist die Steigungsfunktion – zu jeder Stelle die Steigung dort –, und eine Regel ist nur der schnelle Weg, sie hinzuschreiben. „Hier ist der Graph von f(x) = x² auf Kästchenpapier, kein Term für f'. Lege an fünf markierten Stellen das Lineal als Tangente an und schätze die Steigung am Steigungsdreieck. Trage die fünf Steigungen als Punkte in ein zweites Koordinatensystem ein. Welche Form hat das? Wie lautet die Gleichung der Geraden, die du siehst? Vergleiche sie mit dem, was die Potenzregel für x² liefert. Und jetzt dieselbe Aufgabe für den um drei Einheiten nach oben verschobenen Graphen: Was ändert sich am Graphen, was an den Steigungen?“ Wer beim verschobenen Graphen andere Steigungen erwartet, wer die Steigungsfunktion einer Parabel für eine Parabel hält oder wer die Potenzregel anwendet, ohne zu wissen, dass sie Steigungen liefert, braucht das vor jeder Regelübung: Die Regel ersetzt das Lineal, aber sie berechnet dasselbe – Steigungen, keine Höhen. Verständnis, nicht Verfahren; Ermessen in der Aufgabenform, amtlich in der Vorstellung. [GOST Eingangsvoraussetzung L4 „beschreiben qualitativ das Änderungsverhalten eines Funktionsgraphen durch eine Skizze des Graphen der Änderungsfunktion“; GOST Q1 L4 „Änderungsraten funktional beschreiben“, „Ableitungsfunktion“; BE Einführungsphase „ermitteln Ableitungsfunktionen durch grafisches Differenzieren“; MO-Logik: Vorstellung vor Verfahren; fhr 2026-B-1c Fehlerquelle „das absolute Glied 5 beim ersten Ableiten mitführen, obwohl es wegfällt“; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
 95  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
 96  - Potenz-, Faktor- und Summenregel (Einheit 1): „Welche Regel?“ ankreuzen (Vorstufe, Grundvorstellung) → eine ganzrationale Funktion dritten Grades mit ganzen Koeffizienten einmal ableiten, Konstante fällt weg (Grundfall, viermal) → Bruch- und Dezimalkoeffizienten: den Vorfaktor mit dem Exponenten multiplizieren und kürzen (fhr 2025-C-1c, 2026-B-1c, 2021-A-1a) → erste bis dritte Ableitung eines Terms vierten oder fünften Grades hintereinander (fhr 2026-C-1c, 2022-B-1a, 2023-C-1b) → Ableitung und Stammfunktion nebeneinander, Potenzregel in beide Richtungen (abi 2019-be-gk-A1.1a, Teil A) → aus f' den Anstieg an einer Stelle oder im Achsenschnittpunkt berechnen (fhr 2024-C-1c) → mit einem Parameter ableiten und ausklammern (iqb 2021MerhoehtAAnalysis12-a, Teil A) → die Ableitung in eine vorgegebene faktorisierte Form bringen oder die Vorgabe ausmultiplizieren (abi 2025-bebb-lk-B2.1b) → die Ableitung als Quadrat eines Produkts von Linearfaktoren über binomische Formeln nachweisen (iqb 2022MgrundlegendBAnalysisWTR1-1c) → Prüfungshöhe: die drei Ableitungen mit Anschluss – Punktprobe und Prüfung auf einen Extrempunkt über f'(x₀) (fhr 2024-B-1d, Niveau II) und der Anstiegsvergleich an zwei Stellen mit negativen Werten (fhr 2023-C-1b, Niveau II); fhr-Zielmarke: Notieren der ersten drei Ableitungen einer Funktion fünften Grades mit Bruchkoeffizienten, drei Punkte (fhr 2025-C-1c, 2026-C-1c, Niveau I) – der Auftakt jeder fhr-Kurvenuntersuchung.
 97  - Kettenregel (Einheit 2): „Innen und außen?“ – zu Verkettungen ankreuzen, welcher Teil die innere Funktion ist (der Exponent, die Klammer) und was ihre Ableitung ist (eine Zahl, ein Vielfaches von x); nichts rechnen (Vorstufe) → innere und äußere Funktion hinschreiben, nicht ableiten: z = v(x) und u(z) als zwei Zeilen; rückwärts aus u und v die Verkettung bilden (Vorstufe) → e^(kx) mit ganzem und mit negativem k ableiten (Grundfall, viermal) → Potenz eines linearen Terms (ax + b)ⁿ → e mit quadratischem Exponenten: innere Ableitung als Vielfaches von x → wiederholt ableiten und den Faktor kⁿ erkennen; die n-te Ableitung als verschobenen Graphen deuten und die Verschiebung über eine Exponentialgleichung berechnen (iqb 2024MerhoehtAAnalysis23, Teil A, Niveau III) → Prüfungshöhe: die Tangente an eine Verkettung zweier nur abgebildeter Graphen über die Kettenregel bestimmen, den Tiefpunkt als Stelle mit Steigung null nutzen (iqb 2020MerhoehtAAnalysis22, Teil A, Niveau III); fhr-Zielmarke: keine – die Kettenregel ist kein FOS-Stoff.
 98  - Produktregel (Einheit 3): „Welche Regel?“ und „Innen und außen?“ ankreuzen, bei „Innen und außen?“ die innere Funktion und ihre Ableitung; nichts rechnen (Vorstufe) → x · eˣ und x² · eˣ ableiten, e-Term ausklammern (Grundfall, viermal) → mit der Kettenregel im e-Faktor: x · e^(−x), t · e^(−t/hundert), x mal e mit quadratischem Exponenten (abi 2022-bebb-lk-B2.2b; iqb 2022MerhoehtBAnalysisWTR2-1b, 2021MerhoehtAAnalysis13-a) → Polynom mal eˣ oder mal e^(kx), ausklammern und in die vorgegebene Form zusammenfassen (iqb 2024MgrundlegendBAnalysisWTR1-1a; abi 2022-bebb-lk-A1.4a mit Parameter, Teil A; abi 2020-be-gk-B2.1c mit anschließendem Extrempunkt) → den Polynomfaktor in Linearfaktoren zerlegen und die möglichen Extremstellen ablesen (abi 2024-bebb-lk-B2.1d) → die zweite Ableitung eines Produkts nachweisen und als Quadrat mal e-Term deuten (abi 2018-bb-ea-B2.1e, Niveau III) → die Produktregel mit Werten aus zwei Graphen, Steigung null am Tiefpunkt (iqb 2026MgrundlegendAAnalysis21-b, Teil A) → Prüfungshöhe: die Bedingung für eine waagerechte Tangente von f · eˣ mit allgemeinem f nachweisen (iqb 2025MerhoehtAAnalysis21-a, Teil A, Niveau III); fhr-Zielmarke: keine – die Produktregel ist kein FOS-Stoff.
 99
100  ### Prüfungsform (fhr / abi / iqb)
101  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen (be-gk, be-lk, bb-gk, bb-ea) mit „ja“ führen. Für fhr ist der Pool keine Vorgabe: dort gelten RLP FOS 2019 und der fhr-Katalog – und der RLP FOS kennt keine Produkt- und keine Kettenregel. Die Rohdatei zählt 29 Zeilen mit 12 Haupttypen (fhr 8 Zeilen, 2 Typen; abi 9 Zeilen, 4 Typen; iqb 12 Zeilen, 9 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus fhr/fhr-typen.csv bzw. abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
102  fhr (8 Zeilen; fhr-Thema „Ableitungen bilden“ 8) [FOS, fhr-Katalog]: Ableitung ganzrationale Funktion (6, E1) · Verhalten im Unendlichen bestimmen (2, E1). Muster: in jedem Jahrgang 2021–2026 eine Teilaufgabe „Notieren Sie die erste, zweite und dritte Ableitung“ an der ganzrationalen Funktion dritten bis fünften Grades der Kurvenuntersuchung, drei Punkte, Niveau I, mit Bruch- oder Dezimalkoeffizienten (fhr 2025-C-1c, 2026-B-1c, 2026-C-1c) und je nach Heft mit einem Anhang: Anstieg im Achsenschnittpunkt (2024-C-1c), Punktprobe und Extrempunktprüfung (2024-B-1d), Anstiegsvergleich (2023-C-1b) oder das Verhalten im Unendlichen davor (2021-A-1a, 2022-B-1a – dort ist der Haupttyp das Grenzverhalten, die Zeile steht hier nach dem Punkt-Schwerpunkt drei zu zwei). Kein Produkt, keine Verkettung, keine e-Funktion; die Regeln werden nie isoliert, immer als Auftakt der Funktionsuntersuchung geprüft.
103  abi (9 Zeilen, 4 Typen; Landeshefte bb-ea, be-gk, bebb-lk 2017–2025, davon 2 aus den CAS-Fassungen bb-ea 2018 und be-gk 2017) [abi-Katalog]: Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen (5, E3) · Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden (2, E3) · je 1: Ableitung mit Parameter in faktorisierter Form nachweisen (E1) · Ableitungsfunktion und Stammfunktion einer ganzrationalen Funktion angeben (E1). Muster: die Landeshefte prüfen die Regeln fast nur als „Weisen Sie nach, dass f'(x) = …“ an einem Produkt aus Polynom und e-Funktion mit vorgegebenem Ergebnis, zwei bis vier Punkte, Niveau I bis II, als Auftakt einer Extrempunkt- oder Wendepunktaufgabe (2020-be-gk-B2.1c mit Extrempunkt, 2024-bebb-lk-B2.1d mit möglichen Extremstellen, 2018-bb-ea-B2.1e mit der zweiten Ableitung als Quadrat und einer Deutung, acht Punkte, Niveau III, und dieselbe Teilaufgabe in der CAS-Fassung ohne vorgegebene erste Ableitung, 2018-bb-ea-cas-B2.1e, sieben Punkte, Niveau III); die Berliner CAS-Fassung 2017 streicht dagegen die Kontrollangabe von 2017-be-gk-B1.2a und verlangt die erste Ableitung eines Produkts aus quadratischem Polynom und e^(−x) mit Angabe der verwendeten Regeln, dazu Extrem- und Wendepunkte eines Dachprofils, neun Punkte (2017-be-gk-cas-B1.2b, Niveau II); Teil A (2 Zeilen, zwei Punkte) prüft die Produktregel mit Parameter (2022-bebb-lk-A1.4a) und die Potenzregel in beide Richtungen (2019-be-gk-A1.1a). 1 der 9 Zeilen ist wortgleiche Pooldublette (2022-bebb-lk-B2.2b aus 2022MerhoehtBAnalysisWTR2-1b); 2025-bebb-lk-B2.1b ist Landeszusatz zu einer MMS-Poolaufgabe, die die Ableitung dem Rechner überlässt. Niveau I 3, II 4, III 2.
104  iqb (12 Zeilen, 9 Typen; Pool 2017–2026, grundlegend 4 und erhöht 8 Zeilen, Teil A 6 und Teil B 6 Zeilen) [iqb-Katalog]: Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen (3, E3) · Ableitung mit Parameter in faktorisierter Form nachweisen (2, E1) · je 1: Ableitung als Quadrat eines Produkts von Linearfaktoren nachweisen (E1) · Ableitung eines Produkts aus Graphenwerten mit der Produktregel bestimmen (E3) · Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden (E3) · Bedingung für eine waagerechte Tangente eines Produkts mit e^x nachweisen (E3) · Tangente an eine Verkettung aus zwei abgebildeten Graphen über die Kettenregel bestimmen (E2) · Term einer höheren Ableitung einer Sinusfunktion über die Periodizität der Ableitungen angeben (E2) · Verschiebung zwischen Graph und hundertster Ableitung berechnen (E2). Muster: Teil B (6 Zeilen, zwei bis drei Punkte) prüft wie die Landeshefte den Nachweis einer vorgegebenen Ableitung (2024MgrundlegendBAnalysisWTR1-1a, 2022MerhoehtBAnalysisWTR2-1b, 2022MgrundlegendBAnalysisWTR1-1c, Anforderungsbereich I; aus den Stapeln 2017 mit Bereich II das Produkt an der Flusssenke 2017MgrundlegendBAnalysisWTR-1d und die Scharableitung in faktorisierter Form 2017MerhoehtBAnalysisWTR2-1d) und einmal strukturell die 103. Ableitung von c · sin(cx) über die Periodizität der Ableitungsfolge (2017MerhoehtBAnalysisWTR1-3d, Niveau III) – die bis dahin einzige Sinusableitung des Themas; Teil A (6 Zeilen, ein bis fünf Punkte) prüft die Regeln ohne Rechner und in drei Zeilen auf erhöhtem Niveau strukturell: mit allgemeinem f (2025MerhoehtAAnalysis21-a), mit Werten aus Graphen (2026MgrundlegendAAnalysis21-b, 2020MerhoehtAAnalysis22) und als wiederholte Ableitung mit Verschiebung (2024MerhoehtAAnalysis23) – dort liegen vier der fünf Zeilen mit Anforderungsbereich III; dazu die kurzen Nachweise mit Parameter (2021MerhoehtAAnalysis12-a, ein Punkt) und mit Produkt- und Kettenregel (2021MerhoehtAAnalysis13-a). Amtlicher Anforderungsbereich in allen 12 Zeilen (höchster Bereich: I 4, II 3, III 5); Niveau I 6, II 2, III 4. Kontexte: nur 2021MerhoehtAAnalysis13-a (Computervirus), sonst ohne. 1 Poolzeile kehrt wortgleich im Landesheft wieder (2022MerhoehtBAnalysisWTR2-1b).
105  Zielmarke: Einheit 1 – fhr: erste bis dritte Ableitung eines Terms fünften Grades mit Bruchkoeffizienten (2025-C-1c, 2026-C-1c, Niveau I) und mit Anschluss an Punktprobe und Extrempunkt (2024-B-1d, Niveau II); abi: Ableitung und Stammfunktion in Teil A (2019-be-gk-A1.1a, Niveau I) und Ableitung mit Parameter in faktorisierter Form (2025-bebb-lk-B2.1b, Niveau II); iqb: Ableitung als Quadrat von Linearfaktoren (2022MgrundlegendBAnalysisWTR1-1c, Niveau I). Einheit 2 – fhr: kein Stoff; iqb: Tangente an eine Verkettung am Graphen (2020MerhoehtAAnalysis22, Niveau III) und hundertste Ableitung als Verschiebung (2024MerhoehtAAnalysis23, Niveau III), 103. Ableitung einer Sinusfunktion (2017MerhoehtBAnalysisWTR1-3d, Niveau III); abi: kein eigenes Original. Einheit 3 – fhr: kein Stoff; abi: Nachweis einer vorgegebenen Ableitung mit Extrempunkt (2020-be-gk-B2.1c, Niveau II) und der zweiten Ableitung als Quadrat (2018-bb-ea-B2.1e, Niveau III); iqb: Nachweis in Teil B (2024MgrundlegendBAnalysisWTR1-1a, Niveau I), Produktregel mit Graphenwerten (2026MgrundlegendAAnalysis21-b, Niveau II) und mit allgemeinem f (2025MerhoehtAAnalysis21-a, Niveau III).
````

## 2 Originale (30)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2025-C-1c (fhr-katalog.csv)

jahr 2025 · papier C · punkte 3 · format Rechnung · antwort Term
- gegeben: f(x) = −(1/4)x^5 + 2x^3; x aus IR
- gesucht: erste, zweite und dritte Ableitung von f
- verfahren: Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden
- fehlerquelle: den Bruch 1/4 nicht mit dem Exponenten 5 multiplizieren

### 2026-B-1c (fhr-katalog.csv)

jahr 2026 · papier B · punkte 3 · format Rechnung · antwort Term
- gegeben: f(x) = 0,4x^4 − 3,5x^2 + 5; x aus IR
- gesucht: erste, zweite und dritte Ableitung von f
- verfahren: Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden
- fehlerquelle: das absolute Glied 5 beim ersten Ableiten mitführen, obwohl es wegfällt

### 2026-C-1c (fhr-katalog.csv)

jahr 2026 · papier C · punkte 3 · format Rechnung · antwort Term
- gegeben: f(x) = −6x^5 + 18,75x^4 + 20x^3 − 90x^2; x aus IR
- gesucht: erste, zweite und dritte Ableitung von f
- verfahren: Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden
- fehlerquelle: Exponenten nicht um eins senken oder den Faktor 18,75 nicht mit 4 multiplizieren

### 2024-C-1c (fhr-katalog.csv)

jahr 2024 · papier C · punkte 4 · format Rechnung · antwort Term|Zahl
- gegeben: f(x) = (1/4)x^3 − (23/4)x + 7; x aus IR
- gesucht: Gleichungen der ersten drei Ableitungsfunktionen|Anstieg des Graphen im Schnittpunkt mit der y-Achse
- verfahren: dreimal hintereinander die Potenz-, Faktor- und Summenregel anwenden und dann x = 0 in die erste Ableitung einsetzen
- fehlerquelle: den Anstieg über den Funktionswert f(0) statt über f'(0) angeben

### 2024-B-1d (fhr-katalog.csv)

jahr 2024 · papier B · punkte 5 · format Rechnung|Begründung · antwort Term|Text
- gegeben: f(x) = 1/5 x^5 − 1/5 x^4 − 2x^3; x aus IR; Punkt P(3; −21,6)
- gesucht: Gleichungen der ersten drei Ableitungsfunktionen von f|Prüfung, ob P auf Gf liegt|Prüfung, ob P ein Extrempunkt ist
- verfahren: dreimal Potenz-, Faktor- und Summenregel anwenden; f(3) berechnen und mit der y-Koordinate von P vergleichen; f'(3) berechnen und mit null vergleichen
- fehlerquelle: aus der Punktprobe allein auf einen Extrempunkt schließen, ohne f'(3) zu prüfen

### 2023-C-1b (fhr-katalog.csv)

jahr 2023 · papier C · punkte 5 · format Rechnung|Begründung · antwort Term|Text
- gegeben: f(x) = x^5 − 3x^4 − 9x^3 + 27x^2; x aus IR; die Stellen x1 = 1 und x2 = 2
- gesucht: Gleichungen der ersten drei Ableitungen von f|Entscheidung mit rechnerischer Begründung, an welcher der beiden Stellen Gf den größeren Anstieg besitzt
- verfahren: dreimal Potenz-, Faktor- und Summenregel anwenden; f'(1) und f'(2) berechnen und die beiden Werte vergleichen
- fehlerquelle: den Betrag der Anstiege vergleichen und −16 für größer halten

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

### 2020-be-gk-B2.1c (abi-katalog.csv)

jahr 2020 · papier 2020-be-gk · punkte 4 · format Rechnung · antwort Term|Zahl
- gegeben: f(x) = (6x − 3) · e^(−x), x ∈ IR; der Graph hat genau einen lokalen Extrempunkt
- gesucht: Nachweis von f'(x) = (−6x + 9) · e^(−x); Koordinaten des Extrempunkts
- verfahren: Produktregel anwenden und ausklammern; f' = 0 lösen, Funktionswert berechnen (Art nicht verlangt)
- fehlerquelle: innere Ableitung −1 von e^(−x) vergessen

### 2024-bebb-lk-B2.1d (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 4 · format Rechnung|Kurzantwort · antwort Term
- gegeben: f_{−0,2}(x) = (−0,2x² + x − 5) · e^(−0,2x); Behauptung f'_{−0,2}(x) = 0,04(x − 5)(x − 10) · e^(−0,2x)
- gesucht: Nachweis der Ableitung; mögliche lokale Extremstellen ohne weitere Rechnung
- verfahren: Produktregel, e-Term ausklammern, quadratischen Faktor in Linearfaktoren zerlegen; Nullstellen der Ableitung ablesen
- fehlerquelle: innere Ableitung −0,2 vergessen; Extremstellen zusätzlich mit f'' prüfen (nicht verlangt)

### 2018-bb-ea-B2.1e (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 8 · format Rechnung|Begründung · antwort Term|Text
- gegeben: Die Funktion f_2 mit f_2(x) = (x² + 2) · e^(0,5 − x) aus der Schar f_a; ihre erste Ableitung ist f_2′(x) = (−x² + 2x − 2) · e^(0,5 − x).
- gesucht: Nachweis von f_2″(x) = (x − 2)² · e^(0,5 − x); Schlussfolgerungen über den Verlauf von G_2
- verfahren: f_2′ nochmals mit Produkt- und Kettenregel ableiten und den Term als vollständiges Quadrat zusammenfassen. Dann das Vorzeichen beurteilen: Quadrat und Exponentialfaktor sind nicht negativ, die Nullstelle bei x = 2 ist doppelt, also ohne Vorzeichenwechsel.
- fehlerquelle: die Nullstelle von f_2″ bei x = 2 als Wendestelle deuten, ohne den Vorzeichenwechsel zu prüfen

### 2018-bb-ea-cas-B2.1e (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea-cas · punkte 7 · format Rechnung|Begründung · antwort Term|Text
- gegeben: Die Funktion f_2 mit f_2(x) = (x² + 2) · e^(0,5 − x) aus der Schar f_a mit f_a(x) = (x² + a) · e^(0,5 − x), a ∈ IR.
- gesucht: Nachweis von f_2″(x) = (x − 2)² · e^(0,5 − x); Schlussfolgerungen über den Verlauf von G_2
- verfahren: f_2 zweimal ableiten (mit dem CAS oder mit Produkt- und Kettenregel, die erste Ableitung aus d) und den Term als vollständiges Quadrat zusammenfassen. Dann das Vorzeichen beurteilen: Quadrat und Exponentialfaktor sind nicht negativ, die Nullstelle bei x = 2 ist doppelt, also ohne Vorzeichenwechsel.
- fehlerquelle: die Nullstelle von f_2″ bei x = 2 als Wendestelle deuten, ohne den Vorzeichenwechsel zu prüfen

### 2017-be-gk-B1.2a (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 11 · format Rechnung · antwort Zahl
- gegeben: Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. Kontrollangabe: f′(x) = (−x² + 4x − 3) · e^(−x).
- gesucht: Koordinaten der Schnittpunkte des Graphen von f mit den Koordinatenachsen; Art und Lage aller Extrempunkte des Graphen von f
- verfahren: f(0) = 1 liefert den y-Achsenschnittpunkt; da e^(−x) > 0, ist f(x) = 0 genau für (x − 1)² = 0. Für die Extrempunkte −x² + 4x − 3 = 0 lösen (x = 1, x = 3) und die Art mit f″(x) = (x² − 6x + 7) · e^(−x) oder über den Vorzeichenwechsel von f′ bestimmen.
- fehlerquelle: eine Nullstelle des Faktors e^(−x) suchen oder die Nullstelle x = 1 wegen des Berührens nicht als Tiefpunkt erkennen

### 2017-be-gk-cas-B1.2b (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk-cas · punkte 9 · format Rechnung|Kurzantwort · antwort Term|Text|Zahl
- gegeben: Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. Der Graph von f hat zwei Wendepunkte.
- gesucht: erste Ableitung von f mit Angabe der verwendeten Ableitungsregeln; Art und Lage aller Extrempunkte des Graphen von f; Koordinaten der beiden Wendepunkte
- verfahren: Mit Produkt- und Kettenregel: f′(x) = (2x − 2) · e^(−x) − (x² − 2x + 1) · e^(−x) = (−x² + 4x − 3) · e^(−x). f′(x) = 0 liefert x = 1 und x = 3; die Art über f″(x) = (x² − 6x + 7) · e^(−x) oder über den Vorzeichenwechsel von f′. Die Wendestellen aus f″(x) = 0: x = 3 ± √2 (mit dem CAS), Funktionswerte einsetzen.
- fehlerquelle: beim Ableiten von e^(−x) die innere Ableitung −1 vergessen oder nur die Wendestelle im Modellintervall [0; 2] angeben, obwohl beide Wendepunkte verlangt sind

### 2022-bebb-lk-A1.4a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 2 · format Rechnung · antwort Term
- gegeben: f_a(x) = eˣ · (1 − ax), definiert in IR, a ∈ IR
- gesucht: Nachweis, dass f_a'(x) = eˣ · (1 − ax − a)
- verfahren: Produktregel anwenden und eˣ ausklammern
- fehlerquelle: Ableitung von (1 − ax) als −ax

### 2019-be-gk-A1.1a (abi-katalog.csv)

jahr 2019 · papier 2019-be-gk · punkte 2 · format Kurzantwort · antwort Term
- gegeben: f(x) = −5x⁴ − 3x² + x, definiert in IR
- gesucht: Gleichung der Ableitungsfunktion f'; Gleichung einer Stammfunktion F
- verfahren: Summandenweise mit der Potenzregel ableiten und aufleiten; eine Stammfunktion ohne Konstante genügt
- fehlerquelle: beim Aufleiten den Exponenten nicht erhöhen oder den Faktor 1/2 bei x²/2 vergessen

### 2022-bebb-lk-B2.2b (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 2 · format Rechnung · antwort Term
- gegeben: f wie in a; Kontrolle f'(x) = (1 − x²) · e^(−x²/2 + 1/2)
- gesucht: Term von f'
- verfahren: Produkt- und Kettenregel, ausklammern
- fehlerquelle: innere Ableitung −x vergessen

### 2022MerhoehtBAnalysisWTR2-1b (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 2 · format Rechnung · antwort Term
- gegeben: f wie in a; Kontrolle f'(x) = (1 − x²) · e^(−x²/2 + 1/2)
- gesucht: Term von f'
- verfahren: Produkt- und Kettenregel, ausklammern
- fehlerquelle: innere Ableitung −x vergessen

### 2025-bebb-lk-B2.1b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-lk · punkte 3 · format Rechnung · antwort Term
- gegeben: Schar f_k wie in a; Behauptung f_k'(x) = 1/k · x · (x − 2k) · (2x − 2k)
- gesucht: Nachweis der Ableitung in der angegebenen Form
- verfahren: ausmultiplizierte Form ableiten und faktorisieren, oder die angegebene Form ausmultiplizieren und vergleichen
- fehlerquelle: Produktregel am faktorisierten Term ohne Zusammenfassen; Vorzeichen beim Faktorisieren

### 2024MgrundlegendBAnalysisWTR1-1a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Rechnung · antwort Term
- gegeben: f(x) = 2 · (x² − 1) · e^x in IR; Behauptung f'(x) = 2 · (x² + 2x − 1) · e^x
- gesucht: Nachweis der Ableitung
- verfahren: Produktregel, zusammenfassen
- fehlerquelle: Faktor 2 beim zweiten Summanden vergessen

### 2022MgrundlegendBAnalysisWTR1-1c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 3 · format Rechnung · antwort Term
- gegeben: f(x) = 1/80 x⁵ − 1/6 x³ + x, definiert in IR; Abbildung 1 zeigt G_f; W(2 | f(2)) ist Wendepunkt; Behauptung f'(x) = 1/16 (x − 2)² (x + 2)²
- gesucht: Nachweis der Ableitung in der faktorisierten Form
- verfahren: Ableiten, 1/16 ausklammern, binomische Formeln
- fehlerquelle: x⁴ − 8x² + 16 nicht als Quadrat erkennen; stattdessen die rechte Seite ausmultiplizieren ist gleichwertig

### 2017MgrundlegendBAnalysisWTR-1d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 3 · format Rechnung · antwort Term
- gegeben: f(x) = −5x^2 · e^x + 1; angegebene Ableitung f'(x) = −5x · (2 + x) · e^x
- gesucht: Herleitung der angegebenen Gleichung von f' aus der Funktionsgleichung von f
- verfahren: Produktregel auf −5x^2 · e^x anwenden, die Konstante fällt weg, und −5x · e^x ausklammern
- fehlerquelle: die Ableitung von e^x als x · e^(x − 1) bilden oder die Konstante 1 mitableiten

### 2017MerhoehtBAnalysisWTR2-1d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Für jedes k ∈ IR+ ist die Funktion f_k mit f_k(x) = k^2x^3 − 6kx^2 + 9x, x ∈ IR, gegeben; ihr Graph heißt G_k
- gesucht: Nachweis, dass f_k'(x) = 3 · (kx − 1) · (kx − 3) eine Gleichung der ersten Ableitungsfunktion ist
- verfahren: f_k ableiten und den vorgegebenen Term ausmultiplizieren, beide stimmen überein
- fehlerquelle: k beim Ableiten wie eine Variable behandeln

### 2017MerhoehtBAnalysisWTR1-3d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 3 · format Kurzantwort · antwort Term
- gegeben: Für jeden Wert c ∈ IR+ ist die in IR definierte Funktion h_c mit h_c(x) = c · sin(cx) gegeben
- gesucht: ein Term der 103. Ableitung von h_c
- verfahren: Die ersten Ableitungen bilden: c^2 · cos(cx), −c^3 · sin(cx), −c^4 · cos(cx), c^5 · sin(cx); das Muster wiederholt sich nach vier Schritten, jede Ableitung liefert einen Faktor c; 103 lässt bei Division durch 4 den Rest 3
- fehlerquelle: den Exponenten von c als 103 statt 104 angeben oder das Vorzeichen aus dem falschen Rest bestimmen

### 2025MerhoehtAAnalysis21-a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: f und g in IR definiert und differenzierbar mit g(x) = f(x) · e^x; Aussage: hat der Graph von g im Punkt (a; g(a)) eine waagerechte Tangente, dann gilt f'(a) = −f(a)
- gesucht: Nachweis, dass die Aussage wahr ist
- verfahren: g' mit der Produktregel bilden, g'(a) = 0 setzen, durch e^a ≠ 0 teilen
- fehlerquelle: g' = f' · e^x ohne Produktregel ansetzen

### 2026MgrundlegendAAnalysis21-b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 4 · format Rechnung · antwort Zahl
- gegeben: Abbildung mit dem Graphen der linearen Funktion g (Steigung 2, g(3) = 4) und dem Graphen der differenzierbaren Funktion f (Tiefpunkt (3; −6)); h(x) = f(x) · g(x), definiert in IR
- gesucht: Steigung der Tangente an den Graphen von h im Punkt (3; h(3))
- verfahren: h'(3) = f'(3) · g(3) + f(3) · g'(3) mit der Produktregel; f'(3) = 0 (Tiefpunkt), g(3) = 4, f(3) = −6 und g'(3) = 2 aus der Abbildung einsetzen
- fehlerquelle: h'(3) als f'(3) · g'(3) bilden oder f'(3) nicht als null erkennen

### 2020MerhoehtAAnalysis22 (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 5 · format Rechnung · antwort Term
- gegeben: Graphen der ganzrationalen Funktionen f und g in der Abbildung; f(4) = −2, g hat den Tiefpunkt (−2; 1); h(x) = g(f(x))
- gesucht: Gleichung der Tangente an den Graphen von h in (4; h(4))
- verfahren: Kettenregel an der Stelle 4, g'(−2) = 0 am Tiefpunkt erkennen, h(4) ablesen
- fehlerquelle: f'(4) am Graphen schätzen und mit einer geschätzten Steigung von g rechnen

### 2024MerhoehtAAnalysis23 (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: f in IR definiert mit f'(x) = 2 · e^(2x) und f(0) = 1; f^(100) ist die hundertste Ableitungsfunktion; der Graph von f^(100) entsteht aus dem Graphen von f durch eine Verschiebung in x-Richtung
- gesucht: um wie viele Einheiten der Graph von f dazu in x-Richtung zu verschieben ist
- verfahren: f = e^(2x) rekonstruieren, f^(100) = 2^100 · e^(2x) erkennen, die Verschiebungsgleichung f(x − c) = f^(100)(x) nach c auflösen
- fehlerquelle: f^(100) = 2^100 · e^(2x) als Streckung deuten und keine Verschiebung finden

### 2021MerhoehtAAnalysis12-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 1 · format Rechnung · antwort Text
- gegeben: f(x) = x⁴ − k · x² in IR mit k > 0; Graph in der Abbildung
- gesucht: Nachweis, dass f'(x) = 2x · (2x² − k) gilt
- verfahren: ableiten und ausklammern
- fehlerquelle: k beim Ableiten wie eine Variable behandeln

### 2021MerhoehtAAnalysis13-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 2 · format Rechnung · antwort Text
- gegeben: f(t) = 2 · t · e^(−t/100), t in Tagen, f(t) Rate in Tausend Computern pro Tag
- gesucht: Nachweis, dass 2 · (1 − t/100) · e^(−t/100) ein Term von f' ist
- verfahren: Produktregel anwenden und zusammenfassen
- fehlerquelle: innere Ableitung −1/100 vergessen

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2024MgrundlegendAAnalysis22, 2022MerhoehtBAnalysisWTR1-2c

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

# Mappe: integrationsregeln

Eintrag: hz-0801/mathe-nachhilfe, katalog/integrationsregeln.md
Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25T11:16:56+02:00, „katalog: Marken-Zeilen je Lerneinheit, drei Einheiten ergänzt, marken-bau.py“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:42 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Integrationsregeln
 3
 4  ### Verortung
 5  Die Integrationsregeln als Regelwerk: Potenzregel rückwärts (Exponent um eins erhöhen, durch den neuen Exponenten teilen), Faktor-, Summen- und Konstantenregel, die Integration durch Substitution bei  … (gekürzt, 1274 Zeichen)
 6  [GOST] Q2, 2. Kurshalbjahr „Analysis; Stochastik“ (BB S. 26): L4-Zeile „Integrale von Funktionen mittels Stammfunktionen bilden“ mit den Inhalten „Regeln des Vertauschens und der Additivität von Integ … (gekürzt, 1019 Zeichen)
 7  [FOS] Pflichtthema 3 „Integralrechnung“, Thema „Unbestimmtes und bestimmtes Integral“: „Integrationsregeln (Potenz-, Faktor-, Konstanten- und Summenregel)“ (Zeilen 1131–1132 der Textfassung) – ohne Substitution. Kein eigenes fhr-Thema in themen.csv; die Regeln laufen in den fhr-Flächenaufgaben mit (→ flaecheninhalt-durch-integration.md).
 8  [LS-AA] Qualifikationsphase Kapitel III „Integralrechnung“: 4 Bestimmen von Stammfunktionen (Zeile 294 der Textfassung) – die Regeln haben im Fahrplan keine eigene Lerneinheit neben dem Stammfunktionskapitel. Zuordnung: beide Einheiten = QP III 4. Suchprotokoll `_suche_quelle.py --datei ../quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt`: Stammfunktion 7 Treffer (294, 295, 1600, 1601, 1687, 1702, 1704), Integrationsregel 0 – das Lehrwerk fasst die Regeln unter dem Bestimmen von Stammfunktionen.
 9
10  ### Lerneinheiten
11  1. Der Regelsatz – gliedweise integrieren: Potenzregel rückwärts, Faktor vor das Integral, Summen Glied für Glied, Konstante wird lineares Glied; die Substitution bei linearer innerer Funktion (innere … (gekürzt, 640 Zeichen)
12    Marken: BE Q2 · BB Q2 · GK · keine Prüfungsaufgabe
13  2. Vorgegebene Regeln anwenden – die Struktur erkennen: eine in der Aufgabe mitgelieferte Regel (∫ g' · e^g dx = [e^g]) auf einen Integranden anwenden, der erst passend gemacht werden muss – g identifizieren, g' ableiten, Vorzeichen und Faktoren anpassen, dann den Hauptsatz an den Grenzen führen. (kein Planinhalt – Prüfungsform des Pools, die Regel wird vorgegeben; beide Zeilen erhöht) ← Eingabe „vorgegebene regel“, „g strich mal e hoch g“, „struktur erkennen integral“
14    Marken: BE Q2 · BB Q2 · GK · Abitur LK
15  Warum zwei: der amtliche Regelsatz (Plan und Anlage) und die einzige eigene Prüfungsform des Themas (Regel vorgegeben, Struktur gesucht) sind verschiedene Fertigkeiten – auswendig können gegen umformen können. Niveaustufung: fhr = Einheit 1 ohne Substitution, angewendet in den Flächenaufgaben; GK = Einheit 1 vollständig (Teil-A-Stoff der Anlage); LK = dazu Einheit 2 (beide Originale erhöht, amtlicher Anforderungsbereich III).
16
17  ### Typen je Lerneinheit
18  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
19  Einheit 1: kein Typ – die Rohdatei enthält kein Original, das den Regelsatz selbst abfragt; er wird bei stammfunktion-und-hauptsatz.md in jeder Kalkülzeile mitgeprüft (Vermerk „kein Original“).
20  Einheit 2: Integral über eine vorgegebene Regel für g' · e^g berechnen (2). Dazu: Fehler finden (das Vorzeichen der inneren Ableitung übersehen; g aus dem Exponenten falsch abgeschrieben; die Regel angewendet, ohne den Faktor anzupassen) · Begründen (warum die Regel nur für die Struktur g' · e^g gilt; warum das Anpassen des Vorzeichens ein Ausklammern von minus eins ist).
21  Zählung: 0 + 1 = 1 Haupttypen, 0 + 2 = 2 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal.
22
23  ### Voraussetzungen (Blatt 0)
24  Fertigkeiten (je Zeile: was, wofür):
25  - Ableitungsregeln vorwärts, besonders die Kettenregel an e-Termen – das Erkennen von g' in Einheit zwei. Sek-II-Nachbarthema ableitungsregeln.md. [Klarstellung Geometrie sinngemäß: Blatt-0-Fertigkeit aus dem Sek-II-Nachbarthema derselben Stufe; iqb 2022MerhoehtBAnalysisWTR2-1d]
26  - Potenzen mit Brüchen: Exponenten erhöhen, durch Brüche teilen – die Potenzregel rückwärts in Einheit eins. Sek-I-Themen potenzen-wurzeln.md, rationale-zahlen.md. [GOST-OHiMi 2.1 Algebra]
27  - Terme umformen: ausklammern, Vorzeichen ziehen – das Passendmachen in Einheit zwei. Sek-I-Thema terme.md. [Rohdatei-Fehlerquelle „Vorzeichen: g' ist minus x, nicht x“, abi 2022-bebb-lk-B2.2g]
28  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
29  - „Welche Regel passt?“ – zu Integranden ankreuzen, ob Potenz-, Faktor-, Summen- oder Konstantenregel greift oder eine lineare innere Funktion vorliegt; nichts rechnen. Vor Einheit eins. [GOST-OHiMi „Integrationsregeln“]
30  - „Was ist hier g?“ – zu Termen der Form Faktor mal e-Term den Exponenten als g markieren und g' daneben schreiben; nichts rechnen. Vor Einheit zwei. [Rohdatei-Fehlerquelle „Vorzeichen der inneren Ableitung“, iqb 2022MerhoehtBAnalysisWTR2-1d]
31
32  ### Merkkasten
33  Einheit 1 (Der Regelsatz):
34      Potenzregel rückwärts: Exponent um eins erhöhen, durch den neuen Exponenten teilen.
35        Aus x² wird x³/3.
36      Faktor bleibt stehen, Summen gliedweise, eine Konstante wird zum linearen Glied.
37      Lineare Substitution: innere Funktion beibehalten, durch die innere Ableitung teilen.
38        Aus e^(5x) wird e^(5x)/5.
39      Grenzen: Vertauschen wechselt das Vorzeichen; Additivität zerlegt das Intervall.
40      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi] „Integrationsregeln: Faktorregel, Potenzregel, Konstantenregel, Summenregel, Integration durch Substitution (lineare innere Funktion)“.
41      Formelsammlung: [FS-IQB 1.2] führt die Stammfunktionspaare tabelliert, nicht die Regeln – [FS] offen
42  Quelle: eigene Formulierung nach [GOST Q2 L4] „Integrationsregeln“ und [GOST-OHiMi]; Zahlenbeispiele eigen (Ermessen); [LS-AA QP III 4].
43
44  Einheit 2 (Vorgegebene Regeln anwenden):
45      Erst die Struktur, dann die Regel: prüfen, ob der Integrand die Form g' · e^g hat – g aus dem Exponenten ablesen, g' ableiten und mit dem Vorfaktor vergleichen.
46      Passend machen: fehlt ein Vorzeichen oder ein Faktor, wird er ausgeklammert und vor das Integral gezogen; erst dann die Regel [e^g] an den Grenzen auswerten.
47        f(x) = x · e^(−x²/2 + 1/2): mit g(x) = −x²/2 + 1/2 ist g'(x) = −x, also f = −g' · e^g.
48      Auswendig (Teil A): keine – die Regel wird in der Aufgabe vorgegeben (Teil B mit Rechner); sitzen muss das Ableiten von g (Kasten der ableitungsregeln.md).
49      Formelsammlung: keine – die vorgegebene Regel steht in der Aufgabe, nicht in der Formelsammlung – [FS] offen
50  Quelle: eigene Formulierung nach den beiden Originalen (Regelwortlaut aus der Aufgabe); Zahlenbeispiel wörtlich aus iqb 2022MerhoehtBAnalysisWTR2-1d; kein Lehrwerks- und kein Anlagenbeleg (Prüfungsform, siehe Offene Punkte).
51
52  ### Typische Fehler
53  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 2 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: die Muster sind allein aus den Katalogzeilen belegt.
54  - Das Vorzeichen der inneren Ableitung übersehen: g' als x statt −x angesetzt und die Regel ohne den Ausgleichsfaktor angewendet. [abi 2022-bebb-lk-B2.2g; iqb 2022MerhoehtBAnalysisWTR2-1d]
55
56  ### Für schwache Schüler
57  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: der ganze Regelsatz der Einheit 1 – Potenz-, Faktor-, Summen-, Konstantenregel und die lineare Substitution stehen im GK-Kern der Q2 und vollständig in der Anlage ohne Hilfsmittel (Prüfungsteil A). RLP FOS (fhr): dieselben vier Regeln ohne Substitution (Pflichtthema 3), angewendet in den Flächenaufgaben. Niveaustufe H der E-Phase [RLP H]: kein Posten – die Sek-I-Pläne kennen das Integral nicht. Vorrat: Einheit 2 (beide Originale erhöht, amtlicher Anforderungsbereich III) – für GK-Schüler nur als Ausblick. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog verlangt die Grundregeln des Integrierens – deckt sich mit dem GK-Kern, kein zusätzlicher Posten.
58  Grundvorstellung (Blatt 0) [GOST Q2 L4, MO]: Jede Integrationsregel ist eine Ableitungsregel rückwärts. „Hier sind Kärtchen mit den Ableitungsregeln, die du kennst – Potenzregel, Faktorregel, Summenregel, Kettenregel mit linearer innerer Funktion. Drehe jedes Kärtchen um: was sagt die Regel, wenn man sie von rechts nach links liest? Welche Zahl wird beim Rückwärtslesen aus dem Herunterziehen des Exponenten?“ Wer die Potenzregel in beide Richtungen gleich anwendet oder beim Rückwärtslesen das Teilen vergisst, braucht das vor jeder Rechnung: erst die Richtung, dann die Regel. Verständnis, nicht Verfahren; amtlich in der Vorstellung („Integrieren als Umkehrung des Differenzierens“, Q2 GK-Kern), Ermessen in der Aufgabenform. [MO-Logik: Vorstellung vor Verfahren; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
59  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [Rohdatei; Sprossenfolge Ermessen – Lehrwerk und Rohdatei geben keine Reihenfolge vor]:
60  - Der Regelsatz (Einheit 1): „Welche Regel passt?“ ankreuzen (Vorstufe, Grundvorstellung) → Potenzen gliedweise aufleiten (Grundfall, viermal) → Faktoren und Konstanten mitführen → die lineare Substitution an e-Termen und Sinus-Termen → Prüfungshöhe: einen gemischten Term mit allen vier Regeln und einer linearen inneren Funktion aufleiten (kein Original – Vermerk; die Anwendung wird bei stammfunktion-und-hauptsatz.md geprüft, dort Einheit eins und zwei); fhr-Zielmarke: die Regeln innerhalb einer Flächenaufgabe (→ flaecheninhalt-durch-integration.md).
61  - Vorgegebene Regeln anwenden (Einheit 2): „Was ist hier g?“ ankreuzen (Vorstufe) → g und g' zu einem e-Term aufschreiben (Grundfall, viermal) → den Integranden durch Ausklammern eines Vorzeichens passend machen → die Regel an den Grenzen auswerten → Prüfungshöhe: das Integral über die vorgegebene Regel vollständig führen (abi 2022-bebb-lk-B2.2g; iqb 2022MerhoehtBAnalysisWTR2-1d, Niveau II, amtlich III); fhr-Zielmarke: keine – kein Stoff.
62
63  ### Prüfungsform (fhr / abi / iqb)
64  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md. Für fhr ist der Pool keine Vorgabe; ein eigenes fhr-Thema existiert nicht. Die Rohdatei zählt 2 Zeilen mit 1 Haupttyp (abi 1 Zeile, 1 Typ; iqb 1 Zeile, 1 Typ), Jahr 2022. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typname wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
65  fhr: kein eigenes Thema, keine Zeile – die Integrationsregeln laufen in den fhr-Flächenaufgaben mit (→ flaecheninhalt-durch-integration.md).
66  abi (1 Zeile, 1 Typ; Landesheft bebb-lk 2022) [abi-Katalog]: je 1: Integral über eine vorgegebene Regel für g' · e^g berechnen (E2). Muster: eine einzige Zeile, wortgleiche Pooldublette (2022-bebb-lk-B2.2g aus 2022MerhoehtBAnalysisWTR2-1d) in Teil B des Leistungskurshefts, drei Punkte, Niveau II (amtlicher Anforderungsbereich III) – die Regel steht im Aufgabentext, geprüft wird das Strukturieren.
67  iqb (1 Zeile, 1 Typ; Pool 2022, erhöht, Teil B) [iqb-Katalog]: je 1: Integral über eine vorgegebene Regel für g' · e^g berechnen (E2). Muster: eine Teil-B-Zeile innerhalb der Analysis-Aufgabe zur Exponentialschar (2022MerhoehtBAnalysisWTR2-1d, drei Punkte, amtlicher Anforderungsbereich III): die Regel ∫ g'(x) · e^(g(x)) dx = [e^(g(x))] wird vorgegeben, der Integrand muss mit einem Vorzeichen passend gemacht werden. 1 Poolzeile kehrt wortgleich im Landesheft wieder (Dublette der abi-Liste).
68  Zielmarke: Einheit 1 – kein Original (der Regelsatz wird bei stammfunktion-und-hauptsatz.md mitgeprüft); Einheit 2 – abi/iqb: das Integral über die vorgegebene Regel (2022-bebb-lk-B2.2g, 2022MerhoehtBAnalysisWTR2-1d, Niveau II, amtlich III); fhr: keine.
````

## 2 Originale (2)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2022-bebb-lk-B2.2g (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Rechnung · antwort Term
- gegeben: Regel ∫ g'(x) · e^(g(x)) dx = [e^(g(x))] über [u; v]
- gesucht: Wert von ∫₀¹ f(x) dx
- verfahren: f als −g' · e^g mit g = −x²/2 + 1/2 schreiben, Regel anwenden
- fehlerquelle: Vorzeichen: g'(x) = −x, nicht x

### 2022MerhoehtBAnalysisWTR2-1d (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung · antwort Term
- gegeben: Regel ∫ g'(x) · e^(g(x)) dx = [e^(g(x))] über [u; v]
- gesucht: Wert von ∫₀¹ f(x) dx
- verfahren: f als −g' · e^g mit g = −x²/2 + 1/2 schreiben, Regel anwenden
- fehlerquelle: Vorzeichen: g'(x) = −x, nicht x

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

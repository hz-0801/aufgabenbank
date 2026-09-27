# Mappe: uneigentliche-integrale

Eintrag: hz-0801/mathe-nachhilfe, katalog/uneigentliche-integrale.md
Katalog-Commit: 3e956a51fa1ee14a19c2abebef1852436e3d9d08 (2026-09-26T13:40:25+02:00, „katalog: Sek-II-Einträge auf die Katalogzeilen vom 27.09.“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 12:44 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Uneigentliche Integrale
 3
 4  ### Verortung
 5  Das uneigentliche Integral: der Inhalt einer unbegrenzten Fläche als Grenzwert bestimmter Integrale – die obere Grenze wächst über alle Schranken (oder der Integrand ist an einer Stelle unbeschränkt), … (gekürzt, 1306 Zeichen)
 6  [GOST] Q2, Zusatz Leistungskursfach (BB, Zeilen 1174–1179 der Textfassung): innerhalb der LK-Flächenzeile „Inhalte unbegrenzter Flächen mittels uneigentlicher Integrale: Integral über einen unbeschrän … (gekürzt, 655 Zeichen)
 7  [FOS] Kein Stoff: der RLP FOS 2019 kennt uneigentliche Integrale nicht (Nulltreffer uneigentlich); das Pflichtthema 3 endet bei Rotationsvolumina. themen.csv führt keine fhr-Zeile.
 8  [LS-AA] Qualifikationsphase Kapitel III „Integralrechnung“: 8 Uneigentliche Integrale (Zeilen 298 und 1605 der Textfassung) – eine eigene Lehrwerkseinheit am Kapitelende. Zuordnung: beide Einheiten = QP III 8. Suchprotokoll `_suche_quelle.py --datei ../quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt`: uneigentliche 2 Treffer (298, 1605).
 9
10  ### Lerneinheiten
11  1. Der Begriff – Grenzwert statt Grenze: das uneigentliche Integral als Grenzwert bestimmter Integrale, wenn die obere Grenze über alle Schranken wächst oder der Integrand an einer Stelle unbeschränkt … (gekürzt, 685 Zeichen)
12    Marken: BE Q2/4 · BB Q2 · nur LK · keine Prüfungsaufgabe
13  2. Die Näherungsdeutung – Restfläche vernachlässigen: die Aussage, dass F(w) − F(0) für jedes große w näherungsweise ein festes Integral ist, geometrisch deuten – die Differenz ist die Fläche bis w, der Graph läuft gegen null, die Zusatzfläche jenseits der festen Grenze fällt nicht mehr ins Gewicht. (Prüfungsform des Pools 2022, beide Zeilen erhöht) ← Eingabe „restfläche“, „näherung großes w“, „fläche fast vollständig“
14    Marken: BE Q2/4 · BB Q2 · nur LK · Abitur LK
15  Warum zwei: der amtliche LK-Begriff (Planzeile, Lehrwerkseinheit) und die einzige Prüfungsform des Bestands (Deutung der Näherung) sind verschiedene Fertigkeiten – definieren können gegen deuten können. Niveaustufung: fhr = kein Stoff; GK = kein Planstoff (der Eintrag setzt trotzdem keine Decke); LK = beide Einheiten (beide Originale erhöht, Niveau II).
16
17  ### Typen je Lerneinheit
18  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
19  Einheit 1: — Nachweis: Beschränktheit eines Flächeninhalts mit variabler Grenze über den Integralterm nachweisen (1). Dazu: Fehler finden (nur den Grenzwert angegeben, ohne zu zeigen, dass er nicht erreicht wird) · Begründen (warum ein stets positiver Abzug die Schranke sichert). Bis zum Nachzug 2026-09-28 ohne Typ (Vermerk „kein Original“).
20  Einheit 2: — Deutung: Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten (2). Dazu: Fehler finden (die Aussage als Gleichheit von Stammfunktionen gelesen; die Restfläche für null statt für vernachlässigbar erklärt) · Begründen (warum die Differenz zweier Stammfunktionswerte eine Fläche ist; warum ein gegen null laufender Graph die Restfläche klein hält).
21  Zählung: 1 + 1 = 2 Haupttypen, 1 + 2 = 3 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeile vom 28.09.2026: Pool 2017 erhöht Teil B, CAS).
22
23  ### Voraussetzungen (Blatt 0)
24  Fertigkeiten (je Zeile: was, wofür):
25  - Hauptsatz lesen: F(b) − F(a) als Integral und als Fläche – die Deutungszeile in Einheit zwei. Sek-II-Nachbarthema stammfunktion-und-hauptsatz.md. [GOST Q2 L4; Rohdatei-Fehlerquelle „Aussage als Gleichheit von Stammfunktionen gedeutet“, abi 2022-bebb-lk-B2.2h]
26  - Grenzverhalten erkennen: e-Funktionen laufen gegen null, waagerechte Asymptoten – der Grund der Näherung in beiden Einheiten. Sek-II-Nachbarthema grenzwerte-und-verhalten-im-unendlichen.md. [GOST Q1 GK-Kern „Verhalten im Unendlichen“]
27  - Flächen unter Graphen als Integrale deuten – der Bilanzblick in Einheit zwei. Sek-II-Nachbarthema flaecheninhalt-durch-integration.md Einheit fünf. [GOST-OHiMi „Ermittlung von Flächeninhalten“]
28  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
29  - „Endet die Fläche?“ – zu Graphen ankreuzen, ob die Fläche an einer Grenze endet oder ausläuft, und ob sie trotzdem endlich sein kann; nichts rechnen. Vor Einheit eins. [GOST Q2 LK „Inhalte unbegrenzter Flächen“]
30  - „Wie groß ist der Rest?“ – an Graphen, die gegen null laufen, die Fläche jenseits einer Marke schraffieren und ankreuzen, ob sie ins Gewicht fällt; nichts rechnen. Vor Einheit zwei. [Rohdatei-Fehlerquelle „Restfläche für null erklärt“, iqb 2022MerhoehtBAnalysisWTR2-1e]
31
32  ### Merkkasten
33  Einheit 1 (Der Begriff):
34      Uneigentlich heißt: eine Grenze ist keine Zahl – die obere Grenze wächst über alle Schranken (oder der Integrand hat eine Polstelle). Der Wert ist der Grenzwert der bestimmten Integrale.
35        Integral ab null über e^(−x): F(w) − F(0) = 1 − e^(−w), Grenzwert 1 – die unbegrenzte Fläche hat den Inhalt eins.
36      Existenz: der Grenzwert muss existieren – der Graph muss schnell genug gegen null fallen.
37      Auswendig (Teil A): keine – uneigentliche Integrale stehen weder im GK-Kern noch in der Anlage; der Begriff ist LK-Stoff für Teil B.
38      Formelsammlung: keine – uneigentliche Integrale stehen nicht in der Formelsammlung – [FS] offen
39  Quelle: eigene Formulierung nach [GOST Q2 LK] „Integral über einen unbeschränkten Intervall, Integral einer unbeschränkten Funktion“; Zahlenbeispiel eigen (Ermessen); [LS-AA QP III 8].
40  Einheit 2 (Die Näherungsdeutung):
41      F(w) − F(0) ist die Fläche unter dem Graphen bis w. Läuft der Graph gegen null, ändert sich diese Fläche ab einer festen Grenze kaum noch – jedes große w liefert näherungsweise denselben Wert wie das feste Integral.
42      Deuten heißt: Differenz als Fläche benennen, Restfläche zeigen, ihre Kleinheit mit dem Abfallen des Graphen begründen – „vernachlässigbar“, nicht „null“.
43      Auswendig (Teil A): keine – die einzige Prüfungszeile liegt in Teil B mit Rechner; sitzen muss der Hauptsatzblick (Kasten zwei von stammfunktion-und-hauptsatz.md).
44      Formelsammlung: keine – [FS] offen
45  Quelle: eigene Formulierung nach den beiden Originalen (2022-bebb-lk-B2.2h, 2022MerhoehtBAnalysisWTR2-1e); ohne weiteres Zahlenbeispiel (Bildarbeit); [LS-AA QP III 8 sinngemäß].
46
47  ### Typische Fehler
48  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 2 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: die Muster sind allein aus den Katalogzeilen belegt.
49  - Die Aussage als Gleichheit von Stammfunktionen gedeutet statt als Flächennäherung: die Differenz F(w) − F(0) nicht als Fläche erkannt, die Restfläche für exakt null erklärt. [abi 2022-bebb-lk-B2.2h; iqb 2022MerhoehtBAnalysisWTR2-1e]
50
51  ### Für schwache Schüler
52  Mindeststoff (GK-Kern Q2 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: Kein GK-Kern, kein FOS-Stoff, keine Anlagenzeile – das Thema ist vollständig Leistungskursstoff („Inhalte unbegrenzter Flächen mittels uneigentlicher Integrale“); für GK-Schüler ist es Vorrat, für fhr-Schüler kein Stoff. LK-Mindeststoff: der Grenzwertbegriff der Einheit 1 am e-Funktions-Beispiel und die Näherungsdeutung der Einheit 2. Niveaustufe H der E-Phase [RLP H]: kein Posten. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog nennt uneigentliche Integrale nicht – kein zusätzlicher Posten.
53  Grundvorstellung (Blatt 0) [GOST Q2 LK, MO]: Eine Fläche ohne Ende kann trotzdem einen endlichen Inhalt haben – wenn der Graph schnell genug fällt. „Hier ist ein Graph, der nach rechts gegen null läuft, auf Kästchenpapier. Schraffiere die Fläche bis zu einer Marke und zähle grob die Kästchen. Schiebe die Marke ein Stück nach rechts: wie viele Kästchen kommen dazu? Und noch ein Stück? Werden die Zuwächse größer oder kleiner? Worauf läuft die Gesamtfläche zu – und warum wird sie nicht unendlich, obwohl die Fläche nie endet?“ Wer glaubt, unbegrenzt heiße unendlich groß, oder wer die Restfläche für exakt null hält, braucht das vor jeder Rechnung: erst die schrumpfenden Zuwächse sehen, dann der Grenzwert. Verständnis, nicht Verfahren; Ermessen in der Aufgabenform, amtlich im Begriff (LK-Planzeile). [MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „Restfläche für null erklärt“, iqb 2022MerhoehtBAnalysisWTR2-1e; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
54  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen – Lehrwerk und Rohdatei geben keine Reihenfolge vor]:
55  - Der Begriff (Einheit 1): „Endet die Fläche?“ ankreuzen (Vorstufe, Grundvorstellung) → das bestimmte Integral mit wandernder oberer Grenze als Term aufschreiben (Grundfall, viermal) → den Grenzwert an e-Funktionen bilden und als Inhalt der unbegrenzten Fläche deuten → Prüfungshöhe: die Existenzfrage an einem schnell und einem langsam fallenden Graphen vergleichen (kein Original – Vermerk; der Bestand prüft den Begriff nicht direkt); fhr-Zielmarke: keine – kein Stoff.
56  - Die Näherungsdeutung (Einheit 2): „Wie groß ist der Rest?“ ankreuzen (Vorstufe, Grundvorstellung) → die Differenz zweier Stammfunktionswerte als Fläche bis zur wandernden Grenze benennen (Grundfall, viermal) → die Restfläche markieren und ihre Kleinheit über das Abfallen des Graphen begründen → Prüfungshöhe: die vollständige Deutung der Näherungsaussage im Sachzusammenhang (abi 2022-bebb-lk-B2.2h; iqb 2022MerhoehtBAnalysisWTR2-1e, Niveau II); fhr-Zielmarke: keine.
57
58  ### Prüfungsform (fhr / abi / iqb)
59  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md. Für fhr ist der Pool keine Vorgabe; das Thema ist dort kein Stoff, themen.csv führt keine fhr-Zeile. Die Rohdatei zählt 3 Zeilen mit 2 Haupttypen (abi 1 Zeile, 1 Typ; iqb 2 Zeilen, 2 Typen), Jahre 2017–2022. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typname wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
60  fhr: kein Stoff, keine Zeile – der RLP FOS 2019 kennt uneigentliche Integrale nicht.
61  abi (1 Zeile, 1 Typ; Landesheft bebb-lk 2022) [abi-Katalog]: je 1: Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten (E2). Muster: eine einzige Zeile, wortgleiche Pooldublette (2022-bebb-lk-B2.2h aus 2022MerhoehtBAnalysisWTR2-1e) in Teil B des Leistungskurshefts, drei Punkte, Niveau II – die Landeshefte stellen das Thema sonst nicht.
62  iqb (2 Zeilen, 2 Typen; Pool 2017–2022, erhöht, Teil B, davon 1 CAS) [iqb-Katalog]: je 1: Beschränktheit eines Flächeninhalts mit variabler Grenze über den Integralterm nachweisen (E1) · Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten (E2). Muster: eine Teil-B-Zeile innerhalb der Analysis-Aufgabe zur Exponentialschar (2022MerhoehtBAnalysisWTR2-1e, drei Punkte, amtlicher Anforderungsbereich II): die Näherungsaussage F(w) − F(0) ≈ festes Integral ist geometrisch zu deuten; dazu seit dem Nachzug die CAS-Fassung 2017 mit der Schar x² · e^(−a · x): die Fläche bis zur wandernden Grenze als Term und der Nachweis, dass sie unter einer festen Schranke bleibt (2017MerhoehtBAnalysisCAS1-1e, vier Punkte, amtlicher Anforderungsbereich II und III) – der Begriff der Einheit 1 ohne das Wort „uneigentlich“. 1 Poolzeile kehrt wortgleich im Landesheft wieder (Dublette der abi-Liste). Niveau II 1, III 1.
63  Zielmarke: Einheit 1 – iqb: die Beschränktheit der Fläche mit wandernder Grenze (2017MerhoehtBAnalysisCAS1-1e, Niveau III); abi: kein Original; Einheit 2 – abi/iqb: die vollständige Näherungsdeutung (2022-bebb-lk-B2.2h, 2022MerhoehtBAnalysisWTR2-1e, Niveau II); fhr: keine.
````

## 2 Originale (3)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2022-bebb-lk-B2.2h (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Begründung · antwort Text
- gegeben: Für jede Stammfunktion F und jedes w > 2022 gilt F(w) − F(0) ≈ ∫₀²⁰²² f(x) dx
- gesucht: geometrische Deutung
- verfahren: Differenz als Integral, Integral als Flächeninhalt, Zusatzfläche jenseits von 2022 vernachlässigbar
- fehlerquelle: Aussage als Gleichheit von Stammfunktionen deuten

### 2022MerhoehtBAnalysisWTR2-1e (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Für jede Stammfunktion F und jedes w > 2022 gilt F(w) − F(0) ≈ ∫₀²⁰²² f(x) dx
- gesucht: geometrische Deutung
- verfahren: Differenz als Integral, Integral als Flächeninhalt, Zusatzfläche jenseits von 2022 vernachlässigbar
- fehlerquelle: Aussage als Gleichheit von Stammfunktionen deuten

### 2017MerhoehtBAnalysisCAS1-1e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Rechnung|Begründung · antwort Term|Text
- gegeben: Für a ∈ IR+ ist die Schar der in IR definierten Funktionen f_a mit f_a(x) = x^2 · e^(−a · x) gegeben; der Graph von f_a heißt G_a; G_a, die x-Achse und die Gerade x = p mit p ∈ IR+ schließen ein Flächenstück ein; a = 0,2
- gesucht: die Größe dieses Flächenstücks für a = 0,2 (als Term in p); Nachweis, dass der Inhalt auch für beliebig große p kleiner als 250 ist
- verfahren: Wegen f_0,2(x) >= 0 ist der Inhalt ∫ von 0 bis p f_0,2(x) dx = 250 − 5 · (p^2 + 10p + 50) · e^(−p/5); da p^2 + 10p + 50 > 0 und e^(−p/5) > 0, wird von 250 stets eine positive Zahl abgezogen
- fehlerquelle: nur den Grenzwert 250 angeben, ohne zu zeigen, dass er nicht erreicht wird

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

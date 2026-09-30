# Mappe: linearkombination-und-lineare-abhaengigkeit

Eintrag: hz-0801/mathe-nachhilfe, katalog/linearkombination-und-lineare-abhaengigkeit.md
Katalog-Commit: c651dc47624a28a96eb6724ed3e4864024a7bab4 (2026-09-27T22:25:43Z, „katalog: Erkennungsschritte“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:09 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
 1  # Linearkombination und lineare Abhängigkeit
 3
 4  ### Verortung
 5  Die Begriffe hinter dem Vektorrechnen: Kollinearität (ein Vektor als Vielfaches eines anderen), lineare Abhängigkeit und Unabhängigkeit, die Darstellung eines Vektors als Linearkombination anderer Vek … (gekürzt, 1408 Zeichen)
 6  [GOST] Q3, 3. Kurshalbjahr „Analytische Geometrie“ (BB S. 29–30), Grund- und Leistungskursfach: L3-Zeile „elementare Operationen mit geometrischen Vektoren ausführen und Vektoren auf Kollinearität unt … (gekürzt, 1264 Zeichen)
 7  [FOS] Kap. 4 Wahlthema 5 „Analytische Geometrie“ (S. 29): Thema „Vektoren“ mit „lineare Abhängigkeit, Kollinearität“ (Zeile 1205 der Textfassung). Befund wie bei den Nachbarthemen: Wahlstoff ohne Prüfungsbeleg – kein fhr-Bestand, keine fhr-Zeile in themen.csv.
 8  [LS-AA] Einführungsphase Kapitel III 3 „Rechnen mit Vektoren“ (Zeile 274 der Textfassung), Qualifikationsphase Kapitel VI 1 „Vektoren im Raum“ – eine eigene Lehrwerkseinheit zur linearen Abhängigkeit gibt es nicht (Nulltreffer Linearkombination, Abhängigkeit in den Kapitelüberschriften). Zuordnung: beide Einheiten = EP III 3 und QP VI 1.
 9
10  ### Lerneinheiten
11  1. Kollinearität und lineare Abhängigkeit – die Begriffe: kollinear als Vielfaches (gleiche oder Gegenrichtung), linear abhängig als „einer ist Linearkombination der anderen“ (zwei Vektoren: kollinear … (gekürzt, 888 Zeichen)
12    Marken: BE Q3 · BB Q3 · GK · keine Prüfungsaufgabe
13  2. Linearkombination mit Nebenbedingung – die Strecke im Term: OP = r · OC + s · OS mit r + s = 1 und r, s zwischen null und eins beschreibt die Strecke von C nach S – Nachweis durch Umformen (r = 1 − s einsetzen, ausklammern, Parameterform der Strecke lesen); ohne die Intervallbedingung die ganze Gerade. (Q3, GK-Kern „Darstellung von Vektoren als Linearkombinationen anderer Vektoren“; die Deutung als Strecke ist Prüfungspraxis ohne eigenen Plansatz) ← Eingabe „linearkombination strecke“, „r plus s gleich eins“, „konvexkombination“
14    Marken: BE Q3 · BB Q3 · GK · Abitur LK
15  Warum zwei: der amtliche Begriffssatz (Plan und Anlage, Teil A) und die einzige eigene Prüfungsform des Themas (Nebenbedingung als Strecke, Teil B) sind verschiedene Fertigkeiten – erkennen und benennen gegen umformen und nachweisen; dieselbe Lage wie bei integrationsregeln.md. Niveaustufung: fhr = kein Bestand; GK = Einheit 1 (Teil-A-Stoff der Anlage); LK = dazu Einheit 2 (das Original steht im Heft des erhöhten Anforderungsniveaus 2017-bb-ea und wortgleich im erhöhten Pool 2017, CAS-Fassung).
16
17  ### Typen je Lerneinheit
18  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen führt die Rohdatei nicht.
19  Einheit 1: kein Typ – die Rohdatei enthält kein Original, das die Begriffe selbst abfragt; sie werden bei den Nachbarthemen in jeder Kollinearitäts- und Spannvektorzeile mitgeprüft (Vermerk „kein Original“).
20  Einheit 2: Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen (2). Dazu: Fehler finden (die Behauptung an einem einzelnen Zahlenbeispiel geprüft statt allgemein umgeformt; die Intervallbedingung vergessen und die ganze Gerade erhalten) · Begründen (warum r = 1 − s die Kombination auf eine Parameterform bringt; warum die Grenzen des Parameters die Endpunkte der Strecke liefern).
21  Zählung: 0 + 1 = 1 Haupttypen, 0 + 2 = 2 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeile vom 28.09.2026: Pool 2017 erhöht Teil B, CAS).
22
23  ### Voraussetzungen (Blatt 0)
24  Fertigkeiten (je Zeile: was, wofür):
25  - Vektoren addieren, vervielfachen und ausklammern – das Umformen in beiden Einheiten. Sek-II-Nachbarthema vektoren-und-rechenoperationen.md (dasselbe Kurshalbjahr; Klarstellung Geometrie: Fertigkeit aus dem Nachbarthema derselben Stufe). [GOST Q3 L3 „Vektoraddition“, „Multiplikation eines Vektors mit einer reellen Zahl“, „Distributivgesetz“; GOST-OHiMi 2.3]
26  - Die Parameterform einer Geraden und Strecke lesen (Stützpunkt plus Parameter mal Richtungsvektor, Parameter im Intervall) – das Ziel der Umformung in Einheit zwei. Sek-II-Nachbarthema geraden.md (dasselbe Kurshalbjahr). [GOST Q3 L3 „analytische Beschreibung von Geraden …: Parameterform“; GOST-OHiMi 2.3 „Geraden: Parameterform“]
27  - Lineare Gleichungssysteme mit zwei und drei Unbekannten lösen – die Abhängigkeitsprüfung dreier Vektoren in Einheit eins. Sek-I-Thema lineare-gleichungssysteme.md (kanonisch auch für die Sek-II-Zeilen). [GOST Eingangsvoraussetzung L1 „lösen lineare (2,2)- und (3,3)-Gleichungssysteme“; GOST-OHiMi 2.1]
28  - Vielfache und Verhältnisse erkennen – der Kollinearitätsblick in Einheit eins. Sek-I-Thema zuordnungen.md. [RLP Zuordnungen; GOST Q3 L3 „Vektoren auf Kollinearität untersuchen“]
29  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt): keine eigenen – seit 27.09.2026 gestrichen, weil die Vorstufen der Ketten denselben Handgriff verlangen.
30
31  ### Merkkasten
32  Einheit 1 (Kollinearität und lineare Abhängigkeit):
33      Kollinear: einer ist ein Vielfaches des anderen – alle Komponenten mit demselben Faktor, auch negativ; kollineare Vektoren spannen nur eine Gerade auf.
34        u = (2 | 1 | 0) und v = (4 | 2 | 0): v = 2 · u, also kollinear; w = (4 | 2 | 3) ist kein Vielfaches von u.
35      Linear abhängig: einer lässt sich als Linearkombination der anderen schreiben – zwei Vektoren: kollinear; drei Vektoren: sie liegen in einer Ebene (komplanar). Linear unabhängig: nur die Kombination mit lauter Nullen ergibt den Nullvektor.
36      Prüfen: Vielfachenansatz bei zweien; bei dreien den Ansatz r · u + s · v = w als Gleichungssystem lösen – geht es auf, sind sie abhängig.
37      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.3] „Darstellung von Vektoren als Linearkombinationen anderer Vektoren“, „Untersuchung von Vektoren auf lineare Abhängigkeit bzw. Unabhängigkeit“.
38      Formelsammlung: keine – die Begriffe stehen nicht in [FS-IQB 1.3] – [FS] offen
39  Quelle: eigene Formulierung nach [GOST Q3 L3] „lineare Abhängigkeit und lineare Unabhängigkeit von Vektoren“, „Vektoren auf Kollinearität untersuchen“ und [GOST-OHiMi 2.3]; Zahlenbeispiele eigen (Ermessen); [LS-AA EP III 3, QP VI 1].
40
41  Einheit 2 (Linearkombination mit Nebenbedingung):
42      Die Strecke im Term: OP = r · OC + s · OS mit r + s = 1 und r, s zwischen null und eins beschreibt genau die Strecke von C nach S.
43      Nachweis durch Umformen: r = 1 − s einsetzen und ausklammern – OP = OC + s · (OS − OC) = OC + s · CS; das ist die Parameterform der Strecke, die Grenzen des Parameters liefern die Endpunkte.
44      Ohne Intervall: lässt man r und s alle Werte mit r + s = 1 durchlaufen, entsteht die ganze Gerade durch C und S.
45      Auswendig (Teil A): keine – die Umformung ist Teil-B-Stoff (Heft und Pool stellen sie mit Hilfsmitteln); sitzen müssen die Bausteine Linearkombination (Kasten der Einheit oben) und Parameterform (geraden.md).
46      Formelsammlung: keine – die Nebenbedingungsform steht nicht in der Formelsammlung – [FS] offen
47  Quelle: eigene Formulierung nach [GOST Q3 L3] „Darstellung von Vektoren als Linearkombinationen anderer Vektoren“ und dem Original (abi 2017-bb-ea-B3.1d); ohne Zahlenbeispiel (Termarbeit); [LS-AA QP VI 1 sinngemäß].
48
49  ### Typische Fehler
50  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 1 Zeile des Themas in abitur/abi-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: die Muster sind allein aus der Katalogzeile belegt.
51  - Am Beispiel statt allgemein: die Behauptung an einem einzelnen Zahlenbeispiel geprüft, statt mit r = 1 − s allgemein in die Parameterform umzuformen; die Intervallbedingung nicht erwähnt und damit nur die Gerade statt der Strecke erhalten. [abi 2017-bb-ea-B3.1d]
52
53  ### Für schwache Schüler
54  Mindeststoff (GK-Kern Q3 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern: der ganze Begriffssatz der Einheit 1 – Kollinearität, Linearkombination, lineare Abhängigkeit und Unabhängigkeit stehen im GK-Kern der Q3 und vollständig in der Anlage ohne Hilfsmittel (Prüfungsteil A). Niveaustufe H der E-Phase [RLP]: kein Posten – die Sek-I-Pläne kennen keine Vektoren. RLP FOS (fhr): Wahlstoff ohne Prüfungsbeleg – kein Bestand, keine Zeile. Vorrat: Einheit 2 (das eine Original in Heft und Pool des erhöhten Anforderungsniveaus, Niveau II bis III) – für GK-Schüler als Ausblick. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung lineare Abhängigkeit unter Analytische Geometrie – wenn das zutrifft, deckt es sich mit dem GK-Kern, kein zusätzlicher Posten.
55  Grundvorstellung (Blatt 0) [GOST Q3 L3, MO]: Linear abhängige Vektoren sind gefangen – sie kommen aus ihrem Gebilde nicht heraus. „Hier sind zwei Pfeile in dieselbe Richtung, verschieden lang. Welche Punkte erreichst du vom Start aus, wenn du beide beliebig oft vorwärts und rückwärts aneinanderhängst – ein Strich, eine Fläche oder der ganze Raum? Nun drehe den zweiten Pfeil schräg: was erreichst du jetzt? Und wie viele Pfeile in verschiedene Richtungen brauchst du, um jeden Punkt des Raums zu erreichen?“ Wer glaubt, zwei kollineare Pfeile könnten eine Fläche füllen, oder wer den dritten Pfeil in der Ebene der ersten beiden für einen Gewinn hält, braucht das vor jeder Rechnung: Abhängig heißt, der neue Pfeil bringt keine neue Richtung. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q3-Kern „lineare Abhängigkeit“), liegt aber im Kurshalbjahr selbst, nicht in den Eingangsvoraussetzungen (Klarstellung Geometrie); die Aufgabenform ist Ermessen. [GOST Q3 L3; MO-Logik: Vorstellung vor Verfahren; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
56  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [Rohdatei; Sprossenfolge Ermessen – Lehrwerk und Rohdatei geben keine Reihenfolge vor]:
57  - Kollinearität und lineare Abhängigkeit (Einheit 1): „Vielfaches oder nicht?“ – zu Vektorpaaren ankreuzen, ob eines ein Vielfaches des anderen ist (alle Komponenten mit demselben Faktor); nichts rechnen (Vorstufe, Grundvorstellung) → Vektorpaare auf Kollinearität prüfen, den Faktor angeben (Grundfall, viermal) → den Sonderfall Gegenrichtung und den Nullvektor einordnen → drei Vektoren über den Ansatz als Gleichungssystem prüfen → Prüfungshöhe: die Begriffe in den Nachbarthemen anwenden – nicht kollineare Spannvektoren einer Ebene, kollineare Trapezseiten (kein eigenes Original – Vermerk; geprüft bei ebenen.md Einheit eins und punkte-und-strecken-im-koordinatensystem.md Einheit vier); fhr-Zielmarke: keine – kein Bestand.
58  - Linearkombination mit Nebenbedingung (Einheit 2): „Summe der Koeffizienten?“ – zu Linearkombinationen zweier Ortsvektoren ankreuzen, ob die Koeffizienten zusammen eins ergeben und ob sie zwischen null und eins liegen; nichts rechnen (Vorstufe) → eine Kombination mit r plus s gleich eins in die Parameterform umformen (Grundfall, viermal) → die Intervallbedingung als Streckeneigenschaft deuten (Endpunkte an den Parametergrenzen) → Prüfungshöhe: den Nachweis vollständig führen – umformen, Parameterform benennen, Intervall begründen (abi 2017-bb-ea-B3.1d, Niveau II); fhr-Zielmarke: keine – kein Bestand.
59
60  ### Prüfungsform (fhr / abi / iqb)
61  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md. Für fhr ist der Pool keine Vorgabe; ein fhr-Bestand existiert nicht. Die Rohdatei zählt 2 Zeilen mit 1 Haupttyp (abi 1 Zeile, 1 Typ; iqb 1 Zeile, 1 Typ; der Typ in beiden Profilen), Jahr 2017. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typname wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; Thema ohne Gegenstandsklassen, daher ohne Präfix).
62  fhr: kein Bestand, keine Zeile – das Wahlthema 5 des RLP FOS 2019 nennt „lineare Abhängigkeit, Kollinearität“, die zentralen FHR-Prüfungen stellen es nicht.
63  abi (1 Zeile, 1 Typ; Landesheft bb-ea 2017) [abi-Katalog]: je 1: Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen (E2). Muster: eine einzige Landeszeile in Teil B des Brandenburger Hefts auf erhöhtem Anforderungsniveau (2017-bb-ea-B3.1d, drei Punkte, Niveau III): die Kombination r · OC + s · OS mit r + s = 1 ist als Strecke CS nachzuweisen – Begründungsaufgabe am Pyramidenzelt. Seit Abgleichlauf 25 als wortgleiche Pooldublette geführt (Dublette von 2017MerhoehtBAGLAA2CAS2-1d, der CAS-Fassung des erhöhten Pools 2017; vorher „Landesaufgabe ohne Poolzwilling“, weil der Pool-Abgleich nur die WTR-Dateien durchsucht hatte), die Schätzung nach dem amtlichen Bereich der Poolzeile von II auf III nachgezogen. Sonst prüfen die Landeshefte die Begriffe nur eingebettet (Spannvektoren, Trapezseiten); die Geltungsdateien führen das Thema für alle vier Zielprüfungen mit „ja“.
64  iqb (1 Zeile, 1 Typ; Pool 2017, erhöht, Teil B, CAS) [iqb-Katalog]: je 1: Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen (E2). Muster: eine einzige Poolzeile, seit dem Nachzug 2026-09-28 im Eintrag – die CAS-Fassung der Zeltaufgabe des erhöhten Pools 2017 (2017MerhoehtBAGLAA2CAS2-1d, drei Punkte, Anforderungsbereich III, Niveau II): dieselbe Nebenbedingungsform wie das Landesheft, das sie wortgleich übernimmt (Dublette der abi-Liste). Sonst prüft der Pool Kollinearität und Linearkombinationen nur eingebettet (der Vielfachenansatz und die Kantenterme liegen bei vektoren-und-rechenoperationen.md, die Spannvektoren bei ebenen.md); ein eigener Pooltyp zu den Begriffen selbst ist bisher nicht gestellt. Amtlicher Anforderungsbereich: III; Niveau II.
65  Zielmarke: Einheit 1 – kein Original (die Begriffe werden bei den Nachbarthemen mitgeprüft); Einheit 2 – abi: der Streckennachweis über die Nebenbedingung (2017-bb-ea-B3.1d, Niveau III); iqb: dieselbe Aufgabe in der Poolfassung (2017MerhoehtBAGLAA2CAS2-1d, Niveau II, Anforderungsbereich III); fhr: keine.
````

## 2 Originale (2)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2017-bb-ea-B3.1d (abi-katalog.csv)

jahr 2017 · papier 2017-bb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Pyramide ABCDS mit C(5 | 5 | 0) und S(2,5 | 2,5 | 3,9). Der Ortsvektor eines Punktes P lässt sich in der Form OP = r · OC + s · OS mit r, s ∈ [0; 1] und r + s = 1 darstellen.
- gesucht: Nachweis, dass P auf der Strecke CS liegt
- verfahren: r = 1 − s einsetzen und umformen: OP = (1 − s) · OC + s · OS = OC + s · (OS − OC) = OC + s · CS. Das ist die Parameterdarstellung der Strecke von C nach S, die für s ∈ [0; 1] genau diese Strecke durchläuft.
- fehlerquelle: an einem einzelnen Zahlenbeispiel prüfen, statt allgemein mit r = 1 − s umzuformen

### 2017MerhoehtBAGLAA2CAS2-1d (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Ein geschlossenes Zelt auf horizontalem Untergrund hat die Form einer Pyramide mit quadratischer Grundfläche; die seitlichen Kanten bilden vier gleich lange Stangen; das Zelt ist 3,90 m hoch, die Seitenlänge des Zeltbodens beträgt 5,00 m; Modell: Pyramide ABCDS mit Spitze S, A im Koordinatenursprung, B auf dem positiven Teil der x-Achse, D auf dem positiven Teil der y-Achse, C(5; 5; 0), M Mittelpunkt der Grundfläche; das Dreieck ABS liegt in der Ebene E: −39y + 25z = 0; 1 LE = 1 m; der Ortsvektor eines Punkts P lässt sich als OP = r · OC + s · OS mit r, s ∈ [0; 1] und r + s = 1 darstellen
- gesucht: Nachweis, dass P auf der Strecke CS liegt
- verfahren: r = 1 − s einsetzen und umformen: OP = OC + s · (OS − OC) = OC + s · CS; wegen s ∈ [0; 1] liegt P auf der Strecke
- fehlerquelle: nur die Gerade CS zeigen und die Einschränkung s ∈ [0; 1] nicht nutzen

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

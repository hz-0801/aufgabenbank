# Aufgabenbank – Form und Regeln

Stand 2026-10-02, siebte Fassung (Leiterregeln 02.10.: Rückwärts-
und Mischsprosse vor der Prüfungssprosse, krumme Zahlen oben,
Zusatzzeilen über der Sollmenge, herkunft „Regel 02.10.“; vorher
sechste Fassung 01.10.: Feld herkunft für Zeilen aus Blatt-Chats, Übernahme durch den Blatt-Chat 01.10.; Vorstufen-Nummerierung, eine
Prüfungssprosse je Kette, Körperregel beim Nachzug; Pflichtformen
und Päckchen seit 28.09.; Körperregel der Sperre für Punkte 30.09.;
Erkennungsschritte und Vorstufen, Marke „kein P10-Stoff“ 30.09.b).

## Zweck

Die Bank hält je Sprosse des Themenkatalogs
(hz-0801/mathe-nachhilfe, katalog/) geprüfte Aufgaben mit
Lösung. Blätter entstehen später durch Auswahl aus der Bank, nicht
durch Erzeugung. Der Katalog bleibt die einzige Quelle der
Struktur (Einheiten, Sprossen, Voraussetzungen, Originale); die
Bank erfindet Zahlen, Kontexte und Formulierungen, nie die
Struktur.

## Ablage

    bank/<eintrag>/e<n>.jsonl     eine Datei je Lerneinheit
    bank/<eintrag>/zone.jsonl     die Voraussetzungen (Blatt 0)
    bank/<eintrag>/stand.md       Katalog-Commit, Datum, Zahlen
    bank/<eintrag>/muster.md      Musterbeispiel je Verfahrenskette
    werkzeuge/bank-pruef.py       rechnet jede Lösung nach
    werkzeuge/mappe.py            baut die Mappe eines Eintrags
    mappen/<eintrag>.md           Quellen eines Eintrags in einer Datei
    mappen/_bausteine.md          Bausteine der Vorlage (Kurzreferenz)
    eingang/gebaut.csv            gebaute Blätter je Schülernummer (S01 …;
                                  Namen nur in der privaten Projektdatei)
    bau/zettel/vorlage-2026-10-03/ Vorlage Basiszettel (Lehrer 03.10.)

`<eintrag>` ist der Dateiname des Katalogeintrags ohne `.md`.
JSONL: eine Aufgabe je Zeile, ein JSON-Objekt, UTF-8, keine
Leerzeilen. Reihenfolge der Zeilen = Reihenfolge der Kette.

## Felder je Aufgabe

    id            "<eintrag>-e<n>-k<k>-s<s>-v<v>" (Einheit, Kette,
                  Sprosse, Variante); Zone: "<eintrag>-zone-f<f>-v<v>"
    eintrag       Katalogdatei ohne .md
    einheit       Nummer (0 = Zone)
    kette         Name des Verfahrenstyps wortgleich aus der Zeile
                  „Sprossen je Verfahrenstyp" (Zone: Fertigkeit
                  wortgleich aus „Voraussetzungen (Blatt 0)")
    kette_nr      laufende Nummer der Kette in der Einheit
    sprosse       Nummer in der Kette; 0 = die Vorstufe vor dem
                  Grundfall; hat die Kette weitere Vorstufen davor,
                  zählen sie rückwärts: −1, −2 (id s-1, s-2). Der
                  Grundfall ist immer Sprosse 1 (Beschluss 29.09.)
    sprosse_text  die Sprosse wortgleich aus dem Katalog
    merkmal       was diese Sprosse gegenüber der vorigen ändert,
                  ein Halbsatz
    hoehe         "vorstufe" | "grundfall" | "sprosse" |
                  "pruefung" | "pflicht"
    pflicht       nur bei hoehe pflicht: "fehler" | "begruenden" |
                  "darstellung" | "anwendung"; bei jeder anderen
                  hoehe fehlt der Schlüssel
    variante      1, 2, 3 …
    aufgabe       der Aufgabentext, LaTeX-fähig, mit den Bausteinen
                  der Vorlage hz-0801/blattbau (Anleitung_mathblatt.md),
                  ohne \teil und ohne Umgebung – die setzt der
                  Zusammenbau
    form          "teil" | "gleichungsraster" | "dreisatz" |
                  "streifenfeld" | "streifenleer" | "ankreuzen" |
                  "tabelle" | "zeichnen" | "text"; "streifenfeld"
                  für jedes Ablesen am Streifen mit Eintrag, auch
                  wenn die Grafik `\streifen` ist; "streifenleer"
                  für Einzeichnen oder Einteilen in einen leeren
                  Streifen
    antwort       Antwortgerüst wie auf dem Blatt ("__ %",
                  "x1 = __, x2 = __") oder ""; antwort trägt das
                  Gerüst, aufgabe kein `\leerfeld` – außer in einem
                  Lückensatz, wo die Lücke Teil des Satzes ist.
                  Ankreuzoptionen stehen in aufgabe, je `\kreuz`
                  eine Zeile
    loesung       die Lösung, wie sie in der Lösungsdatei steht
                  (Rechen- und Ablesetypen: Ergebnis; Sachaufgabe:
                  mit Zwischenergebnis und einem Antwortsatz, der
                  das Gefragte mit Einheit nennt, nicht nur die
                  Stelle; Original: knapper Weg; Begründen: Kern in
                  einem Satz, der die Regel beim Namen nennt
                  („gleiche Stufenwinkel“, „Division durch eine
                  negative Zahl dreht das Zeichen um“); Fehler
                  finden: Fehler benannt und richtige Rechnung;
                  Urteilen (recht, wahr, möglich, reicht): Urteil
                  als erstes Wort („Ja;“, „Nein;“, „falsch;“),
                  dann der Grund als Halbsatz oder Rechnung –
                  Urteile vom 28.09.);
                  verlangt die Sprosse Probe, Kontrolle oder
                  Überschlag, steht sie als eigene, beschriftete
                  Zeile: Gleichung „Probe: linke Seite … = …,
                  rechte Seite …, beide gleich“; Teilen
                  „Kontrolle: Ergebnis mal Teiler = …“;
                  Ausklammern „Probe: ausmultipliziert …“;
                  Prozentsatz „Überschlag: … ≈ …“ vor der
                  Rechnung (Beschluss 28.09. abends);
                  LaTeX-fähig wie aufgabe (für \erg), Tausender
                  mit `\,`, das Prüfskript zieht sie zusammen
    pruef         Python-Ausdruck, der die Lösungszahl ergibt
                  (mehrere: Liste); bei Rundungsaufgaben der
                  ungerundete Wert, das Skript rundet kaufmännisch
                  auf die Stellen der Lösung; bei Brüchen Zähler
                  und Nenner als Liste; "" nur bei Begründen,
                  Zeichnen oder einer Lösung ohne Ziffer
    original      null oder {"id": "2018-OS-K7a", "jahr": 2018,
                  "papier": "OS"}; Kennung wortgleich aus der
                  Mappe (Abschnitt 2 Originale); papier wie dort.
                  Das Feld darf an jeder hoehe stehen, wenn die
                  Sprosse ein Original des Katalogs verfremdet
                  (P10-Form-Sprossen mitten in der Kette); hoehe
                  pruefung bleibt der letzten Sprosse
                  vorbehalten. Prüfungshöhe ohne P10-Original:
                  null („Mengen je Kette")
    grafik        "" oder der Bausteinaufruf der Grafik, aus den
                  Aufgabenwerten berechnet
    loesungsgrafik "" oder der Bausteinaufruf der Lösungsgrafik –
                  für Skizzieraufgaben, deren Lösung nicht durch
                  zwei bis drei Punkte beschreibbar ist
    quelle        Zeile des Katalogeintrags, aus der die Sprosse
                  stammt (Zeilennummer beim Stand-Commit)
    herkunft      nur bei Zeilen, die ein Blatt-Chat erfunden hat:
                  „Blatt <eintrag> <JJJJ-MM-TT>[b], Nr. <n>“ (Ordner
                  in eingang/ und Nummer auf dem Blatt), und bei
                  Zeilen, die nach den Leiterregeln vom 02.10.2026
                  gebaut sind (Rückwärts-, Mischsprosse, krumme
                  Zahlen oben, Zusatzzeilen): „Regel 02.10.“; sonst
                  fehlt das Feld. Der Blatt-Chat (bankblatt.md v5.2) prüft
                  seine Erfindungen gegen die Bank (Prüfskript,
                  Doppelte, Sprosse) und trägt sie selbst ein; der
                  Lehrer streicht, was ihm auf dem Blatt nicht
                  gefällt (Beschluss 01.10.).

Eine Pooldublette (derselbe Text in zwei Heften, im Katalog als
„Dublette von“ vermerkt) zählt als ein Original; die Bankzeile trägt
die Kennung des Katalogs, die in der Mappe zuerst steht (29.09.).

Prüfkennung „(P10 Jahr Papier)"; FHR „(FHR Jahr)"; Abitur
„(Abitur Jahr GK)" für grundlegendes und „(Abitur Jahr LK)" für
erhöhtes Niveau – iqb grundlegend und be-gk sind GK, iqb erhöht,
bebb-lk und bb-ea sind LK; CAS/MMS-Fassung und Teil A/B stehen
nicht in der Prüfkennung. Sie steht am Ende des Fragesatzes
(unterrichtsblatt 3.6), vor den Ankreuzoptionen.

## Mengen je Kette

Vorstufe 4, jede Vorstufe der Kette (0, −1, −2 …) für sich;
Grundfall 5; jede weitere Sprosse 3; Prüfungshöhe 2
je Original des Katalogs (verfremdet); Pflichtelemente je
Einheit: fehler 3, begruenden 3, anwendung 3, darstellung 3, wo
die Typen der Einheit sie tragen. In Sek-II-Einträgen tragen die
Deutungstypen (Baumdiagramm darstellen, Term deuten, Ereignis
beschreiben) die Pflichtelemente darstellung und anwendung, auch
wenn die Typzeilen diese Wörter nicht nennen. Zone: je Fertigkeit
2 sehr leichte, 1 mittlere, je Fallstrick 1.

Die drei fehler-Zeilen einer Einheit tragen verschiedene Formen:
Schülerrechnung mit Fehler; fehlerfreie Vorlage (P2); Serie
„Welche Ergebnisse können nicht stimmen?“ (P1) oder, bei
Gleichungen und Ungleichungen, Prüfzahl (P3). Die drei
begruenden-Zeilen ebenso: „Begründe, warum …“; Aussagenserie
wahr/falsch (P4); Personenaussage zum häufigsten Fallstrick (P6).
Die Formen P1–P8 stehen unter „Regeln für den Inhalt“ (Urteile vom
28.09., urteil-einbindung-2026-09-28.md im Repo mathe-nachhilfe).

Der Grundfall (5 Zeilen) gilt je Verfahrenskette, nicht je
Einheit. Hat eine Einheit zwei Verfahrensketten, hat sie zwei
Grundfälle. „(4×)“ oder „viermal“ am Grundfall im Katalog ist
die Zahl der Grundfall-Aufgaben auf dem Blatt; die Bank hält fünf
Zeilen, damit die Auswahl wechseln kann. Die Pflichtelemente
stehen je Einheit einmal; ihre Kette heißt nach der ersten
Verfahrenskette der Einheit.

Rückwärts- und Mischsprosse (Leiterregeln 02.10.2026, Katalog
konzept.md Entscheidung 38) sind gewöhnliche Sprossen: je 3 Zeilen,
hoehe sprosse, beide unmittelbar vor der Prüfungssprosse – erst
Rückwärts, dann Gemischt. Hat die Kette sie schon, wird nichts
ergänzt; nennt der Katalog unter „Offene Punkte“ einen Grund
gegen die Umkehrung, fehlt die Rückwärtssprosse.

Zusatzzeilen über der Sollmenge werden dazugeschrieben, nicht
gegen vorhandene getauscht; der Lehrer streicht am Blatt
(Beschluss 02.10.). Die Sollmenge ist eine Untergrenze.

Eine Prüfungshöhe ohne P10-Original (Zielmarke aus
Rahmenlehrplan oder Lehrwerk) trägt hoehe pruefung, original
null, 3 Zeilen.

Je Verfahrenskette gibt es genau eine Prüfungssprosse, die letzte
der Kette; nennt die Katalogzeile mehrere Originale („dazu …“,
„daneben …“, „höhere Marke“), stehen sie alle an dieser einen
Sprosse, je Original zwei Zeilen (Beschluss 29.09., Schub 1 und
2: fünf Einträge haben so zusammengelegt, bis zwölf Zeilen an
einer Sprosse). Grund: das Blatt zieht an der Prüfungshöhe „was
die Prüfung fragt“, nicht ein bestimmtes Original.
Ein Original, das zwei Einheiten durchläuft (Ansatz in der einen,
Rechnung in der nächsten; der Katalog nennt es an beiden Stellen,
etwa „als Ansatz“), bekommt seine zwei Zeilen an der
Prüfungssprosse der späteren Einheit; in der früheren steht es nur
als Verweis in sprosse_text.

Erkennungsschritt 4 Zeilen: eigene Kette, nur Sprosse 0
(unterrichtsblatt 2.3 a). Er wird einmal angelegt, in der ersten
Einheit seines Bereichs („Vor Einheit …“ im Katalog), in der keine
Kette eine Vorstufe mit demselben Handgriff hat; hat jede Einheit
des Bereichs eine solche Vorstufe, entfällt er. Derselbe Handgriff
heißt: dieselbe Entscheidung an derselben Art Vorlage (ankreuzen,
ob eine Stelle gegeben oder gesucht ist; „von“ im Text markieren),
gleich, wie die Frage heißt und ob die Ankreuzzeilen anders lauten.
Eine andere Entscheidung oder eine andere Vorlage ist ein anderer
Handgriff (Länge wählen gegen Dreieck finden; was fehlt gegen was
gemeint ist), auch wenn beide nach Zahl oder Richtung fragen. Zwei
Ketten mit Vorstufen desselben Handgriffs, auch in verschiedenen
Einheiten: die Zeilen stehen einmal, bei der ersten Kette in der
Reihenfolge der Datei; die zweite Kette beginnt mit dem Grundfall.
Jeder dieser Fälle steht in stand.md unter „Befunde“ als
Katalogbefund mit beiden Stellen (Erkennungsschritt oder erste
Vorstufe; zweite Vorstufe); der Katalog bleibt unverändert.

Typ ohne Kette 3 Zeilen: eine Sprosse, hoehe sprosse (nicht
grundfall; der Grundfall gehört der Verfahrenskette).

Zone: Die zwei sehr leichten Zeilen (sprosse 1) tragen hoehe
grundfall, die mittlere (sprosse 2) und jeder Fallstrick (ab
sprosse 3, je Fallstrick eine) hoehe sprosse; merkmal jedes
Fallstricks beginnt mit „Fallstrick:". kette und sprosse_text der
Zone sind die Fertigkeit bis zum Doppelpunkt; variante zählt je
Fertigkeit durch (das id-Muster der Zone trägt keine Sprosse).
Das Zone-Paar (nächster Absatz) folgt seiner eigenen Regel.

Zone-Paar: einmal je Zone ein Paar aus Fehler finden und
gleichartiger Rechenaufgabe zum häufigsten Fallstrick
(unterrichtsblatt 2.2), 2 Zeilen – Fehler finden mit hoehe
pflicht, pflicht fehler, danach die Rechenaufgabe mit hoehe
sprosse; beide als Sprossen in der Kette der Fertigkeit, zu der
der Fallstrick gehört.

## Reihenfolge je Datei

Erkennungsschritte (eigene Ketten, nur Sprosse 0) →
Verfahrenskette des Katalogs → Typen ohne Kette →
Pflichtelemente als eigene Kette mit dem Namen der (ersten)
Verfahrenskette. kette_nr zählt in dieser Folge; die
Verfahrenskette ist daher nicht immer k1.

## Regeln für den Inhalt

- Krumme Zahlen (Dezimal, Bruch, negativ, gemischte Einheiten)
  stehen auf den oberen Sprossen einer Kette, für alle Schüler und
  ohne Gymnasialmarke; Grundfall und Vorstufen bleiben glatt
  (Beschluss 02.10.). Sparsam (Lehrer 02.10.): je Kette höchstens
  eine Sprosse mit krummen Zahlen, am Ende vor Rückwärts-, Misch-
  und Prüfungssprosse; das Blatt nimmt eine Aufgabe daraus, beim
  Blatt „schwach“ keine, außer auf Zuruf. Eine Mischsprosse mischt Fälle oder
  Verfahren der Kette, ohne Überschrift oder Reihenfolge, die den
  Fall verrät; eine Rückwärtssprosse gibt Ergebnis oder
  Eigenschaft vor und fragt nach der Aufgabe.
- Die Kette kommt aus dem Katalog; jede Variante einer Sprosse
  ändert genau das Merkmal der Sprosse, sonst nichts. Varianten
  derselben Sprosse unterscheiden sich in Zahlen und Kontext,
  nicht im Merkmal.
- Die fünf Grundfall-Zeilen einer Kette sind ein Päckchen: ein
  Wert bleibt in allen fünf gleich (dasselbe Ganze, derselbe
  Nenner, derselbe Teiler), genau ein Wert wandert, der Kontext
  bleibt. Gilt, wo der Grundfall Zahlen wandern lässt (Beschluss
  28.09. abends, Quelle altlehrwerke-formen.md).
- Analytische Geometrie (Sek II): Die Sprossen einer Kette nutzen
  denselben Körper mit festen Eckpunkten, je Variante ein Körper;
  neu ist je Sprosse nur das Merkmal. Das ist die Sek-II-Form des
  Päckchens (Urteile vom 28.09., altlehrwerke-formen-sek2.md).
  Analysis: derselbe Funktionsterm je Variante durch die Kette, es
  wandert ein Koeffizient (ableitungsregeln 29.09.). Beim Nachzug
  eines bestehenden Ordners gilt die Übernahme vor der Körperregel:
  der Körper trägt Vorstufen und Grundfall, übernommene Sprossen
  behalten ihre Zahlen (geraden 29.09.).
- Keine ganze Gleichung, kein Term, kein Zahlenpaar und keine
  Funktion aus Merkkasten, Beispiel oder Original des Eintrags.
  Ein einzelner Bruch ist kein Zahlenpaar; frei sind einzelne
  Ziffern und Zahlen unter 10. Ein einzelnes Zahlenpaar oder
  Tripel als Punkt ist frei; gesperrt sind zwei oder mehr Punkte
  derselben Quelle (ein Original, der Kasten) in einer Zeile
  (Körperregel der Sperre, 30.09.).
  Ausnahme: Frei sind der Gegenstand der Kette und die Form, die
  der Sprossentext selbst nennt (x², 2x², (x − d)² + e als Form).
  Gesperrt bleiben konkrete Zahlbelegungen aus Kasten und
  Original (etwa (x − 3)² + 1), Zahlenpaare und Ergebnisse.
- Ein Original wird verfremdet: gleiches Verfahren, gleiche
  Falle, gleiche Form, andere Zahlen, anderer Kontext; das Feld
  original trägt Kennung, Jahr und Papier.
- Eine Sprosse mit der Katalogmarke „(kein P10-Stoff)“ bekommt
  Bankzeilen wie jede andere; die Marke steuert nur den Zusammenbau
  (das Prüfungsheft lässt sie aus, das Unterrichtsblatt führt sie).
- Zahlen so, dass Ergebnisse endlich sind und leichte Aufgaben im
  Kopf gehen; periodische Dezimalbrüche tragen einen Hinweis.
  Dreisatz-Zahlen der Zone im Kopf rechenbar.
- Keine Aufgabe doppelt, auch nicht über Ketten hinweg.
- Ankreuzen: Die loesung nennt die richtige Option wortgleich
  (Zahl, Term oder Gleichung wie in der Option); pruef trägt die
  Zahl, wenn die Optionen Zahlen sind, sonst "".
- Buchstaben und Symbole nur, wenn im Text erklärt; ein
  Buchstabe je Einheit für eine Sache.
- Fehler-finden-Aufgaben: das Muster aus „Typische Fehler" mit
  eigenen Zahlen, in der Schreibform des Verfahrens; nie die
  Zahlen des Katalogs.
- P1 fehler: Trägt die Kette ein Kennzeichen (Endziffer,
  Kommastelle, Vorzeichen, Überschlag), ist eine der drei eine
  Serie mit 3–4 fertigen Ergebnissen: „Welche Ergebnisse können
  nicht stimmen? Begründe, ohne genau zu rechnen.“; loesung je
  falschem Ergebnis das Kennzeichen in einem Halbsatz; pruef "".
- P2 fehler: Je Einheit ist eine der drei Vorlagen fehlerfrei
  („Prüfe, ob <Name> richtig gerechnet hat.“); loesung „Richtig.“
  und die Regel des entscheidenden Schritts in einem Satz.
  Dieselbe Form in der Mehrzahl: eine der drei darf vier
  Rechnungen untereinander zeigen, genau eine davon mit dem Muster
  aus „Typische Fehler“; gefragt ist, welche falsch ist und wie sie
  richtig heißt – so erkennt der Schüler auch die richtigen als
  richtig.
- P3 fehler bei Gleichungen und Ungleichungen: eine der drei nennt
  eine Prüfzahl („Setze 0 ein. In welcher Zeile stimmt es nicht
  mehr?“); loesung in zwei Sätzen: der Fehler mit der verletzten
  Regel, dann die richtige Zeile. Nur Umformungsketten.
- P4 begruenden: eine der drei ist eine Aussagenserie mit 3
  Aussagen, mindestens eine wahr und eine falsch, mit
  Alltagsquantoren (immer, jede, nie, es gibt); „Entscheide bei
  jeder Aussage, ob sie wahr oder falsch ist. Begründe.“; form
  text; loesung je Aussage „wahr, denn …“ bzw. „falsch, z. B. …“
  mit Gegenbeispiel; pruef "".
- P5 Begründen nennt die Regel beim Namen (Feld loesung).
- P6 begruenden: eine der drei ist eine Personenaussage zum
  häufigsten Fallstrick der Zone („<Name> sagt: „…“ Begründe, ob
  <Name> recht hat.“); „Das kann man nicht entscheiden, weil …“ ist
  eine zugelassene loesung.
- P7 darstellung: der Operator nennt die Zieldarstellung („Schreibe
  als Gleichung.“, „Beschreibe den Graphen in Worten, ohne ihn zu
  zeichnen.“); die drei Aufgaben je Einheit decken mindestens zwei
  Richtungen, davon eine rückwärts.
- P8 anwendung: eine der drei endet mit einer Entscheidung an einem
  Grenzwert („Reicht das Geld?“, „Darf der Wagen über die
  Brücke?“); loesung: Urteil zuerst, dann die Rechnung.
- Urteilsfragen (recht, wahr, stimmt, reicht) einer Einheit haben
  etwa gleich viele Ja- und Nein-Lösungen; das Urteil ist das erste
  Wort der Lösung (Feld loesung). Mindestens eine der drei
  begruenden lässt sich ohne Rechnung entscheiden und sagt es
  („Begründe, ohne genau zu rechnen.“).
- rationale-zahlen: Das Antwortgerüst „Vorzeichen: __ Betrag: __
  Ergebnis: __“ steht nur in den ersten zwei Varianten der Sprossen
  „Zeichen zusammenfassen gemischt“ (e2) und „plus mal minus“ (e3);
  die Bankzeilen selbst ändert der Bank-Auftrag des Eintrags
  (Urteile vom 28.09.).
- Anwendung: realistische Größen, eine im Kontext sinnvolle
  Frage; eine eingekleidete Rechnung ist keine Anwendung.
- Fragewort je Aufgabe: was gefragt ist, in wenigen Wörtern,
  nicht der ganze Anweisungssatz („13 von 25 – wie viel
  Prozent?").
- Streifen, Tabelle, Skizze nur, wenn an ihr gelesen, gefärbt
  oder eingeteilt wird.
- Operatoren in KMK-Bedeutung; Formulierungen eindeutig.
- Punkte und Vektoren als Zeilentupel mit senkrechtem Strich,
  A(1 | 2 | 0).
- sin, cos, ln als \mathrm{…}.

## Musterbeispiel

bank/<eintrag>/muster.md (seit 29.09.) hält je Verfahrenskette ein
vorgerechnetes Beispiel für die Option „schwach“ (ziel.md: vorn am
Grundfall ein Musterbeispiel): Abschnitt „## e<n> k<k> <kette>“, die
Aufgabe des Grundfalls mit eigenen Zahlen (nicht aus dem Päckchen),
darunter eine Tabelle Schritt | Zeile, eine Zeile je Umformung, das
Ergebnis als letzte Zeile. Reine Daten ohne Bausteine; die Form auf
dem Blatt (Schrittname links, Gleichheitszeichen untereinander,
Ergebnis abgesetzt) setzt der Zusammenbau nach layout-befunde 55.
Liefert der Lehrer ein Beispiel, gilt seins (ziel.md). Annahme
29.09.: je Verfahrenskette statt „einmal je Eintrag“ (ziel.md), weil
jedes Blatt am Grundfall seiner Einheit beginnt; Prüfstein terme
(TER-S1, TER-S2 des Lehrers).

## Basisvorrat

bank/_basis/ (seit 28.09.) hält den Vorrat für die Basiszettel:
Basisaufgaben (Teil A der P10) werden getrennt geübt, am
Stundenanfang ein Zettel. Hilfsmittel: Aufgabe 1 der P10 wird bis 2027
mit Taschenrechner und Formelsammlung geschrieben (msa/msa-vorgaben.md
in mathe-nachhilfe; „ohne Rechner“ bis 02.10. war falsch); ab 2028
kommt ein hilfsmittelfreier Teil (10 BE) dazu – dafür später eine
eigene Zettelsorte. Ein Basis-Typ
ist seit 02.10.2026 jeder Typ des ganzen Basisteils der P10
(msa/msa-katalog-basis.csv, Spalte typ: 62 Typen) und dazu der Typ
jedes Basisteil-Originals, das in der Bank als Prüfungshöhe steht (zwei
GYM-Typen); bank/_basis/typen.md listet sie mit Zahl der Jahrgänge
(Stand 02.10.: 64 Typen, 640 Aufgaben). Ein Typ ohne Prüfungshöhe in der
Bank liegt im Eintrag, der sein Thema trägt (themen.csv). Je Typ 5, 10
oder 20 Aufgaben (Ziel nach Jahrgängen, Lehrer 02.10.) in Prüfungsform in
bank/_basis/<eintrag>.jsonl – Felder wie oben, hoehe "basis" (nur
hier), id "<eintrag>-basis-k<k>-v<v>", kette = sprosse_text =
Typname, sprosse 1, variante 1–n, original = das jüngste Original
des Typs, das in der Mappe des Eintrags steht (Pflicht), Form wie im Original, im Kopf rechenbar; die
Regeln für den Inhalt gelten (Sperre gegen die Mappe des Eintrags,
Verfremdung, keine Aufgabe doppelt). Die Aufgaben stehen in
bank/_basis/vorrat.py, das die jsonl schreibt; geprüft mit
`werkzeuge/bank-pruef.py _basis` (v0.6, Menge 10 je Kette als
Warnung). Seit 02.10. abends: keine Prüfkennung im Aufgabentext; bei
sechs Typen ist die Hälfte der Varianten (1, 3, 5, …) ein Bündel – eine
Vorgabe, Teile a), b), c), wo der Vergleich etwas lehrt (Winkelfunktion
sin/cos/tan, Mittelwert/Median/Spannweite, Prozenttabelle mit je Zeile
anderem gesuchten Wert, Wahrscheinlichkeit einstufig, Winkel an
Parallelen, eine Dauer in zwei Einheiten); „Term zu Figur“ nur Rechteck,
Quadrat, Dreieck; die trigonometrische Gleichung wird nur umgestellt.
Das Zettel-Rezept (`zusammenbau.py --zettel basis`, v0.7, Kennung
BAS-S<n>, auf dem Blatt „Basis n“) baut eine feste Serie ohne
Rückmeldung: Wiederkehr nach 2, 5, 10 Zetteln, leichte und häufige Typen
zuerst, keine Variante doppelt, eine Spalte, eine volle Seite; der
Vorrat trägt 33 Zettel (werkzeuge/zusammenbau.md, „Rezept Zettel“).
Seit 03.10. (v1.7) liegt daneben bank/_basis/schwierigkeit.csv
(typ;stufe;grund), das Urteil des Lehrers je Typ – 1 leicht, 2 mittel,
3 schwer –, von Hand gepflegt und einzige Quelle für „leicht“: der
Zettel ordnet danach, beginnt mit zwei Aufgaben der Stufe 1 und nimmt
schwach Stufe 3 nur als Vorstufe.

Original-Zettel (seit 03.10., zusammenbau.py v1.8, Probe des Lehrers):
Aufgabe 1 eines P10-Hefts wortgetreu (Du-Form) in der Form des
Basiszettels, Teilaufgaben in der Heftreihenfolge. Der Wortlaut der
Prüfungsoriginale liegt nur im privaten Repo hz-0801/aufgabenbank-privat
(`basis-originale.jsonl`, eine Zeile je Teilaufgabe, Felder in
werkzeuge/zusammenbau.md „Original-Zettel“), nie in diesem Repo; auch der
gebaute Zettel bleibt draußen. Aufruf: `python3 werkzeuge/zusammenbau.py
--zettel original --heft 2026-FOR --ohne-register --pdf --aus <ordner>`
(Kennung ORG-2026-FOR). Erfasst: 2026 FOR.

## Punkte

bank/_punkte.csv (seit 28.09., Semikolon, UTF-8, LF) hat je
Bankzeile mit original genau eine Zeile:
id;original;punkte;stern;umfang;grund. punkte und stern sind die
des Originals aus den Prüfungskatalogen in mathe-nachhilfe (msa/,
fhr/, abitur/). umfang sagt, ob die Bankzeile die ganze
Original-Teilaufgabe abbildet: ganz (gleiche Zahl verlangter
Ergebnisse wie gesucht, gleiche Handlung wie format/verfahren,
Verfremdung erlaubt), teil (das Original hat mehrere Leistungen,
die Bankzeile übt nur einen Teil) oder unklar (alles andere);
grund nennt den Anlass in einem Halbsatz. Das Urteil trifft ein
Modell, das jede Zeile liest; `werkzeuge/punkte.py` liefert den
Lesestoff (--lesestoff DIR --nur-neu), führt die Urteile mit den
Katalogpunkten zusammen (--urteile) und prüft ohne Argument, dass
jede Bankzeile mit original genau eine Zeile hat und jedes
original im Katalog steht. Regel (Beschluss 28.09.): Punkte
stehen nur im Prüfungsheft und im Prüfungs-Fokus, und dort immer,
als Punkte des Originals; ins Heft kommen nur Zeilen mit umfang
ganz. Zeilen mit teil oder unklar bleiben auf Lernblättern und
stehen dort ohne Punkte. Verlangt die Bankzeile mehr als das
Original (eine Frage dazu), ist sie ganz (29.09.). Nach einem
Nachzug der Bank zieht `werkzeuge/punkte-nachziehen.py <commit>
<eintrag> …` die ids nach; Zeilen ohne Entsprechung bekommen ein
neues Urteil.

## Quellen je Sitzung

Eine Sitzung liest nur mappen/<eintrag>.md, mappen/_bausteine.md
und bank.md; Katalog, Anleitung, Prompt und CSV liest sie nicht
selbst. Grund: Kosten.

## Befunde

Was eine Sitzung am Katalog, an bank.md oder am Prüfskript für
falsch hält, steht in stand.md unter „Befunde"; sie ändert es
nicht.

## Prüfung

`werkzeuge/bank-pruef.py <eintrag>` (v0.5) liest alle jsonl des
Eintrags, dazu mappen/<eintrag>.md und mappen/_bausteine.md.
Ausgabe je Aufgabe eine Zeile OK/ABWEICHUNG, Warnungen als
WARNUNG-Zeilen, zuletzt je Datei und gesamt die Zahl der
Abweichungen und Warnungen.

Abweichungen: Pflichtfelder, id-Muster, Kettenfolge lückenlos;
jede pruef-Zahl steht an der Ergebnisstelle der Lösung – erste
Zahl, nach „=" oder „≈", ein Punkt (x|y), ein Tripel (x|y|z)
oder Bruch dort, oder ein Glied einer Aufzählung von Ergebnissen
–, nach Rundung auf die Stellen der Lösung, Toleranz 0,005; ein
Minus mit Abstand gehört zur Zahl („$-\,6$", „x^2 - 12x"), außer
nach Zahl, „)" oder Einheit; eine gemischte Zahl gilt als unechter
Bruch; original, wo es steht, vollständig (id, jahr, papier
gesetzt, id beginnt mit jahr und steht als „### <id>" in
Abschnitt 2 der Mappe); bei form ankreuzen mit mindestens zwei
Zahloptionen steht die Lösungszahl in genau einer, sonst nennt
die Lösung genau eine Option wortgleich; jeder Baustein in aufgabe,
loesung, grafik, loesungsgrafik steht in mappen/_bausteine.md mit
passender Argumentzahl; bei ksys-Grafiken liegen die Punkte der
Lösung, jeder Scheitel einer \parabel und jeder \punkt im
Achsenbereich, bei ksys3 die Tripel der Lösung; form zeichnen
oder ein Ablese- oder Zeichenauftrag in aufgabe verlangt grafik
(das Wort „Graph" allein nicht); kein Zahlenpaar (Anteil,
Produkt), keine zwei Punkte oder Tripel derselben Quelle (ein
Original; Merkkasten und Typische Fehler zusammen als Kasten),
keine Gleichung, kein Zahlterm und kein Term mit Variable und
Zahl aus Merkkasten, Typische Fehler und den Originalen der Mappe
in aufgabe (Sperre, Ausnahme nach „Regeln für den Inhalt"; ein
einzelner Bruch ist kein Paar, ein einzelner Punkt ist frei, der
Ursprung zählt nicht als Punkt; x⁴ der Mappe gilt wie x^4); keine
Aufgabe doppelt (aufgabe und grafik zusammen).

Warnungen: Mengen aus „Mengen je Kette" (Grundfall je Kette,
Prüfungshöhe ohne Original 3), das Zone-Paar, hoehe und merkmal
der Zone je Zeile, ein fehlendes Feld loesungsgrafik, eine
fehlende Mappe (dann entfallen Sperre und Kennungsprobe).

Erst bei null Abweichungen wird committet. Weicht eine Lösung ab,
wird die Aufgabe korrigiert, nicht das Skript – außer das Skript
hat erkennbar falsch modelliert; das steht dann unter „Befunde".

## Sprache der Aufgaben (vorläufig, 28.09.2026)

Aufgabentexte folgen bau/sprachlauf/regeln.md: ganze, kurze Sätze;
erst die Lage, dann genau eine Aufforderung; die Frage nennt ihren
Bezug; keine Stichwörter mit Doppelpunkt; Division als Bruch.
Gilt für neue und geänderte Zeilen. Abnahme durch den Lehrer
offen (mathe-nachhilfe uebergabe.md § 5, K2).

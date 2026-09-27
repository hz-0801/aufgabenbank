# Aufgabenbank – Form und Regeln

Stand 2026-09-27b, vierte Fassung (nach den Sek-II-Prüfsteinen).

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
    werkzeuge/bank-pruef.py       rechnet jede Lösung nach
    werkzeuge/mappe.py            baut die Mappe eines Eintrags
    mappen/<eintrag>.md           Quellen eines Eintrags in einer Datei
    mappen/_bausteine.md          Bausteine der Vorlage (Kurzreferenz)

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
    sprosse       Nummer in der Kette; 0 = Vorstufe
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
                  mit Zwischenergebnis; Original: knapper Weg;
                  Begründen: Kern in einem Satz; Fehler finden:
                  Fehler benannt und richtige Rechnung);
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

Prüfkennung „(P10 Jahr Papier)"; FHR „(FHR Jahr)"; Abitur
„(Abitur Jahr GK)" für grundlegendes und „(Abitur Jahr LK)" für
erhöhtes Niveau – iqb grundlegend und be-gk sind GK, iqb erhöht,
bebb-lk und bb-ea sind LK; CAS/MMS-Fassung und Teil A/B stehen
nicht in der Prüfkennung. Sie steht am Ende des Fragesatzes
(unterrichtsblatt 3.6), vor den Ankreuzoptionen.

## Mengen je Kette

Vorstufe 4; Grundfall 5; jede weitere Sprosse 3; Prüfungshöhe 2
je Original des Katalogs (verfremdet); Pflichtelemente je
Einheit: fehler 3, begruenden 3, anwendung 3, darstellung 3, wo
die Typen der Einheit sie tragen. Zone: je Fertigkeit 2 sehr
leichte, 1 mittlere, je Fallstrick 1.

Der Grundfall (5 Zeilen) gilt je Verfahrenskette, nicht je
Einheit. Hat eine Einheit zwei Verfahrensketten, hat sie zwei
Grundfälle. Die Pflichtelemente stehen je Einheit einmal; ihre
Kette heißt nach der ersten Verfahrenskette der Einheit.

Eine Prüfungshöhe ohne P10-Original (Zielmarke aus
Rahmenlehrplan oder Lehrwerk) trägt hoehe pruefung, original
null, 3 Zeilen.

Erkennungsschritt 4 Zeilen: eigene Kette, nur Sprosse 0; er
steht einmal, in der ersten Einheit seines Bereichs
(unterrichtsblatt 2.3 a).

Verlangt ein Erkennungsschritt denselben Handgriff wie die
Vorstufe einer Kette derselben Einheit, entfällt der
Erkennungsschritt; die Vorstufe bleibt. stand.md nennt den Fall
unter „Befunde" als Katalogbefund (der Katalog führt beide).

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

- Die Kette kommt aus dem Katalog; jede Variante einer Sprosse
  ändert genau das Merkmal der Sprosse, sonst nichts. Varianten
  derselben Sprosse unterscheiden sich in Zahlen und Kontext,
  nicht im Merkmal.
- Keine ganze Gleichung, kein Term, kein Zahlenpaar und keine
  Funktion aus Merkkasten, Beispiel oder Original des Eintrags.
  Ein einzelner Bruch ist kein Zahlenpaar; frei sind einzelne
  Ziffern und Zahlen unter 10.
  Ausnahme: Frei sind der Gegenstand der Kette und die Form, die
  der Sprossentext selbst nennt (x², 2x², (x − d)² + e als Form).
  Gesperrt bleiben konkrete Zahlbelegungen aus Kasten und
  Original (etwa (x − 3)² + 1), Zahlenpaare und Ergebnisse.
- Ein Original wird verfremdet: gleiches Verfahren, gleiche
  Falle, gleiche Form, andere Zahlen, anderer Kontext; das Feld
  original trägt Kennung, Jahr und Papier.
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
(das Wort „Graph" allein nicht); kein Zahlenpaar, kein Tripel,
keine Gleichung, kein Zahlterm und kein Term mit Variable und
Zahl aus Merkkasten, Typische Fehler und den Originalen der Mappe
in aufgabe (Sperre, Ausnahme nach „Regeln für den Inhalt"; ein
einzelner Bruch ist kein Paar, der Ursprung kein Punkt; x⁴ der
Mappe gilt wie x^4); keine Aufgabe doppelt (aufgabe und grafik
zusammen).

Warnungen: Mengen aus „Mengen je Kette" (Grundfall je Kette,
Prüfungshöhe ohne Original 3), das Zone-Paar, hoehe und merkmal
der Zone je Zeile, ein fehlendes Feld loesungsgrafik, eine
fehlende Mappe (dann entfallen Sperre und Kennungsprobe).

Erst bei null Abweichungen wird committet. Weicht eine Lösung ab,
wird die Aufgabe korrigiert, nicht das Skript – außer das Skript
hat erkennbar falsch modelliert; das steht dann unter „Befunde".

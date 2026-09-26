# Aufgabenbank – Form und Regeln

Stand 2026-09-26, erste Fassung (Prüfstein prozentrechnung).

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
                  "darstellung" | "anwendung"
    variante      1, 2, 3 …
    aufgabe       der Aufgabentext, LaTeX-fähig, mit den Bausteinen
                  der Vorlage hz-0801/blattbau (Anleitung_mathblatt.md),
                  ohne \teil und ohne Umgebung – die setzt der
                  Zusammenbau
    form          "teil" | "gleichungsraster" | "dreisatz" |
                  "streifenfeld" | "streifenleer" | "ankreuzen" |
                  "tabelle" | "zeichnen" | "text"
    antwort       Antwortgerüst wie auf dem Blatt ("__ %",
                  "x1 = __, x2 = __") oder ""
    loesung       die Lösung, wie sie in der Lösungsdatei steht
                  (Rechen- und Ablesetypen: Ergebnis; Sachaufgabe:
                  mit Zwischenergebnis; Original: knapper Weg;
                  Begründen: Kern in einem Satz; Fehler finden:
                  Fehler benannt und richtige Rechnung)
    pruef         Python-Ausdruck, der die Lösungszahl ergibt
                  (mehrere: Liste); "" bei Begründen und Zeichnen
    original      null oder {"id": "2018-OS-K7a", "jahr": 2018,
                  "papier": "FOR"} – nur bei hoehe pruefung
    grafik        "" oder der Bausteinaufruf der Grafik, aus den
                  Aufgabenwerten berechnet
    quelle        Zeile des Katalogeintrags, aus der die Sprosse
                  stammt (Zeilennummer beim Stand-Commit)

## Mengen je Kette

Vorstufe 4; Grundfall 5; jede weitere Sprosse 3; Prüfungshöhe 2
je Original des Katalogs (verfremdet); Pflichtelemente je
Einheit: fehler 3, begruenden 3, anwendung 3, darstellung 3, wo
die Typen der Einheit sie tragen. Zone: je Fertigkeit 2 sehr
leichte, 1 mittlere, je Fallstrick 1.

## Regeln für den Inhalt

- Die Kette kommt aus dem Katalog; jede Variante einer Sprosse
  ändert genau das Merkmal der Sprosse, sonst nichts. Varianten
  derselben Sprosse unterscheiden sich in Zahlen und Kontext,
  nicht im Merkmal.
- Keine ganze Gleichung, kein Term, kein Zahlenpaar und keine
  Funktion aus Merkkasten, Beispiel oder Original des Eintrags;
  einzelne Ziffern und kleine Grundfallzahlen sind frei.
- Ein Original wird verfremdet: gleiches Verfahren, gleiche
  Falle, gleiche Form, andere Zahlen, anderer Kontext; das Feld
  original trägt Kennung, Jahr und Papier.
- Zahlen so, dass Ergebnisse endlich sind und leichte Aufgaben im
  Kopf gehen; periodische Dezimalbrüche tragen einen Hinweis.
  Dreisatz-Zahlen der Zone im Kopf rechenbar.
- Keine Aufgabe doppelt, auch nicht über Ketten hinweg.
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

## Prüfung

`werkzeuge/bank-pruef.py <eintrag>` liest alle jsonl des
Eintrags, prüft die Felder (Pflichtfelder, id-Muster,
Kettenfolge lückenlos, Mengen), wertet jedes pruef aus und
vergleicht mit den Zahlen in loesung (Zahlenwerte, nicht
Schreibweisen); Ausgabe je Aufgabe eine Zeile OK/ABWEICHUNG und
zuletzt die Zahl der Abweichungen. Erst bei null wird
committet. Weicht eine Lösung ab, wird die Aufgabe korrigiert,
nicht das Skript – außer das Skript hat erkennbar falsch
modelliert.

# Stand: prozentrechnung

Katalog: hz-0801/mathe-nachhilfe, katalog/prozentrechnung.md,
Commit 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25, letzter
Commit auf der Datei). Alle Werte in quelle sind Zeilennummern dieses
Stands.
Datum: 2026-09-26 (date: 2026-09-26 19:59 UTC).
Prüfung: `python3 werkzeuge/bank-pruef.py prozentrechnung` –
275 Zeilen, 0 Abweichungen; mit `--katalog` (sprosse_text wortgleich
in Zeile quelle) ebenfalls 0.

## Zahlen

    Datei       Zeilen  vorstufe  grundfall  sprosse  pruefung  pflicht
    zone.jsonl      32         0         12       19         0        1
    e1.jsonl        47         0          5       18        12       12
    e2.jsonl        57        12          5       18        10       12
    e3.jsonl        48         0          5       21        10       12
    e4.jsonl        41         8          5       12         4       12
    e5.jsonl        52         8          5       18        12        9
    gesamt         277        28         37      106        48       58

Zone: grundfall = sehr leicht, sprosse = mittel und Fallstricke.
Pflicht je Einheit: fehler 3, begruenden 3, anwendung 3; darstellung
3 in e1 bis e4, in e5 keine.

Prüfläufe: Abweichungen des Prüfskripts vor Korrektur je Datei 0
(zone, e1 bis e5); keine Einheit scheiterte. Nach dem Commit der Zone
fand die Sperrprobe dort das Paar 2/16 (2018-OS-K7a); korrigiert im
Commit e1. In e5 dasselbe Paar vor dem Commit korrigiert.

## Originale

Verfremdet, je 2 Zeilen:
- e1: 2020-OS-B1a, 2022-OS-B1f, 2023-OS-K6b, 2019-OS-K5b,
  2017-OS-K2b, 2021-OS-K5b
- e2: 2018-OS-K7a, 2023-OS-K6a, 2015-OS-K7c, 2014-OS-B1e,
  2025-OS-K6b
- e3: 2021-OS-B1c, 2017-OS-B1b, 2014-OS-B1a, 2026-FOR-B1a,
  2019-OS-K5a
- e4: 2025-OS-B1a, 2023-OS-B1b
- e5: 2026-FOR-K3c, 2022-OS-K4b, 2016-OS-K2c, 2024-OS-B1e,
  2015-OS-K2b, 2025-OS-K4b

Nicht gebaut: 2015-OS-B1e und 2014-OS-K3a (Jahreszinsen; Katalog
10i: „gebaut wird der Kontext in zinsrechnung.md“); 2015-OS-K2a (in
keiner Prüfungshöhe und keiner Zielmarke; seine Lesart „20 %, ein
Fünftel, 20/100“ steht als Begründen-Aufgabe e3-k3-s2-v3).

## Entscheidungen

1. Reihenfolge je Datei = kette_nr: Erkennungsschritte (eigene
   Ketten, nur Sprosse 0), dann die Verfahrenskette des Katalogs,
   dann Typen ohne Kette, zuletzt die Pflichtelemente als eigene
   Kette. Die Verfahrenskette ist daher nicht immer k1 (e2: k3,
   e4 und e5: k2).
2. kette bei Ketten, die nicht in „Sprossen je Verfahrenstyp“
   stehen: Erkennungsschritt oder Typ wortgleich aus der Zeile
   quelle. Die Pflichtkette trägt den Namen der Verfahrenskette
   (bank.md wörtlich); ihr sprosse_text ist der Typ aus „Typen je
   Lerneinheit“ (fehler, begruenden, e1 darstellung) oder die
   Wendung aus „Lerneinheiten“ (sonst darstellung, anwendung).
3. Erkennungsschritte stehen einmal, in der ersten Einheit ihres
   Bereichs (unterrichtsblatt 2.3 a): „Was ist das Ganze?“ und
   „Streifen einteilen“ in e2, „Was ist gegeben, was gesucht?“ in
   e4, „Welcher Wert ist der alte?“ in e5; „um oder auf?“ ist in e5
   schon Vorstufe der Kette. Menge je Erkennungsschritt 4.
4. Typen ohne Kette: e1 „Prozentangaben ordnen“, e2 „Umkehrung: zu
   einem Prozentsatz ein Zahlenpaar angeben“, e3 „Mehrwertsteuer in
   Euro“ – je eine Sprosse, hoehe sprosse, 3 Varianten (nicht
   grundfall, damit je Einheit genau der Grundfall der Kette 5
   Zeilen hat).
5. Prüfungshöhe: eine Sprosse je Abschnitt der Katalogzeile
   (Hauptform, „höhere Marke“, „dazu …“), darin 2 Varianten je
   Original; original steht je Variante. Die Zielmarke 2025-OS-K4b
   (Steigung) ist eigene Sprosse von e5 mit quelle 124, weil der
   Auftrag die Originale aus Prüfungsform und Zielmarke verlangt.
6. 2014-OS-B1e (Zinssatz) ist gebaut, ohne Zinskontext – die
   Verfremdung verlangt einen anderen Kontext; die Falle (kleiner
   Prozentsatz mit Komma) bleibt.
7. Kreisdiagramm- und Sektorteile von 2015-OS-K7c, 2025-OS-K6b und
   2021-OS-K5b sind nicht gebaut (Typen bei daten.md), nur der
   Prozentteil.
8. Zone: s1 sehr leicht (2 Zeilen, hoehe grundfall), s2 mittel (1,
   hoehe sprosse), ab s3 je Fallstrick eine (hoehe sprosse); variante
   läuft über die Fertigkeit, wie das id-Muster f<f>-v<v> es
   verlangt. Zwei Fallstricke je Fertigkeit, rückwärts aus den
   Stellen des Lernblatts geplant. Reihenfolge nach erster
   Verwendung (2.2), bei gleicher Einheit Folge des Eintrags: f1
   Bruch als Anteil, f2 Bruch ↔ Dezimalzahl, f3 durch hundert, f4
   Dreisatz, f5 Runden, f6 Bruchteil einer Größe. sprosse_text =
   Fertigkeit. Kein Wort „Prozent“ in der Zone.
9. Der Schlüssel pflicht steht nur bei hoehe pflicht.
10. loesung ist LaTeX-fähig wie aufgabe (für \erg); Tausender mit
    `\,`, das Prüfskript zieht sie zusammen.
11. pruef gibt bei Rundungsaufgaben den ungerundeten Wert; das Skript
    rundet kaufmännisch auf die Stellen der Lösung. pruef "" nur bei
    Begründen, Zeichnen oder einer Lösung ohne Ziffer. Bei Brüchen
    gibt pruef Zähler und Nenner als Liste.
12. form „streifenfeld“ für jedes Ablesen am Streifen mit Eintrag,
    auch wenn die Grafik `\streifen` ist; „streifenleer“ für
    Einzeichnen oder Einteilen in einen leeren Streifen.
13. antwort trägt das Gerüst, aufgabe kein `\leerfeld` – außer im
    Lückensatz zu 2025-OS-K4b, wo die Lücke Teil des Satzes ist.
    Ankreuzoptionen stehen in aufgabe, je `\kreuz` eine Zeile.
14. Prüfkennung „(P10 Jahr Papier)“ am Ende des Fragesatzes
    (unterrichtsblatt 3.6), vor den Ankreuzoptionen.
15. Keine Skizze bei den Steigungsaufgaben: `\dreieckrw` beschriftet
    mit Buchstaben, und welche Kathete waagerecht liegt, legt die
    Anleitung nicht fest.
16. Prüfskript: Die Doppelprüfung vergleicht aufgabe und grafik
    zusammen (dieselbe Frage an einem anderen Streifen ist eine
    andere Aufgabe); das war beim ersten Stand falsch modelliert und
    ist vor e1 korrigiert. Option `--katalog` prüft die Wortgleichheit.
17. Bausteinprobe (Name und Argumentzahl gegen die Anleitung) und
    Sperrprobe (Kastenzeilen, Zahlenpaare aus Originalen und
    „Typische Fehler“) liefen als Hilfsskripte außerhalb des Repos:
    je 0 Befunde. Die jsonl wurden mit einem Python-Erzeuger
    außerhalb des Repos geschrieben; maßgeblich ist die jsonl.

## Nachbesserung 2026-09-27

- Prüfskript v0.5 vorher: 46 Abweichungen, 7 Warnungen; nachher 0
  Abweichungen, 0 Warnungen in allen sechs Dateien; keine Zeile
  gestrichen.
- Alle 275 Zeilen tragen jetzt das Feld loesungsgrafik (leer),
  eingefügt vor quelle.
- Zone: Das Zone-Paar steht neu an f6 (f6-v6 Fehler finden, hoehe
  pflicht, pflicht fehler; f6-v7 gleichartige Rechenaufgabe, hoehe
  sprosse), zum Fallstrick „gefragt ist der Rest, nicht der Teil“ –
  gewählt, weil ihm „Ersparnis und neuer Preis verwechselt“ (Typische
  Fehler Z. 85) mit drei P10-Originalen entspricht, mehr als jedem
  anderen Fallstrick der Zone.
- Zone f4 v1–v5 und f6 v4: die Lösung zeigt jetzt die Rechnung mit
  „=“, damit Zwischenwert und Ergebnis an der Ergebnisstelle stehen;
  Zahlen und pruef unverändert.
- Bei 28 Lösungen in e1 bis e5 steht ein geprüfter Zwischen- oder
  Endwert jetzt nach „=“ oder vorn (e1 k1 s6 v3, s8 v3–v4, k2 s1
  v1–v3; e2 k5 s3 v1–v3, s4 v1; e3 k3 s3 v1–v3, s4 v2–v3; e4 k3 s3
  v1–v3, s4 v2–v3; e5 k2 s1 v1–v5, s11 v1, k3 s3 v1–v2); Zahlen und
  pruef unverändert.
- Aus pruef entfernt, weil kein Ergebnis, sondern Distraktor oder
  gegebene Größe: der Restpreis (e3 k1 s8 v3–v4), der Aufschlag
  allein (e5 k2 s9 v1–v2), der Rabatt in Euro (e5 k2 s10 v1–v2) und
  die gegebenen Werte bei „Was ist gesucht?“ (e4 k1 s0 v1–v4, pruef
  jetzt "").
- e1 k1 s7 v1–v2 (Ankreuzen mit Aussagen): die Lösung beginnt jetzt
  mit der Option wortgleich, pruef "" (Optionen sind keine Zahlen).
- e1 k1 s7 v2: 6 % durch 8 % ersetzt (Optionen und Lösung), weil
  „6 von 100“ das Zahlenpaar aus 2025-OS-K4b ist (Sperre).
- Kein Erkennungsschritt zu streichen: „Was ist das Ganze?“ und
  „Streifen einteilen“ (e2), „Was ist gegeben, was gesucht?“ (e4),
  „Welcher Wert ist der alte?“ (e5) verlangen einen anderen
  Handgriff als die Vorstufe ihrer Einheit.
- Keine Prüfungshöhe ohne Original: alle Prüfungssprossen tragen
  P10-Originale und stehen als hoehe pruefung.

## Befunde

1. bank.md: „hoehe pruefung bleibt der letzten Sprosse
   vorbehalten“; hier verteilt sich die Prüfungshöhe nach
   Entscheidung 5 auf mehrere Sprossen je Kette (e1 s7–s9, e2
   s7–s9, e3 s8–s10, e5 s8–s11). Nicht geändert: als hoehe sprosse
   mit original gälte die Menge 3 je Sprosse statt 2 je Original,
   das hieße Zeilen streichen oder ergänzen; das Skript meldet den
   Fall nicht.

## Offene Punkte

- (erledigt v0.5) Zone ohne Fehler-finden-Paar: unterrichtsblatt
  2.2 verlangt es einmal je Zone, die Mengen in bank.md nennen es
  nicht. Seit der Nachbesserung steht es an f6.
- (erledigt v0.5) Mengen für Erkennungsschritte (4) und Typen ohne
  Kette (3) sind hier gesetzt; bank.md regelt sie nicht. bank.md
  nennt jetzt dieselben Mengen.
- Das id-Muster der Zone trägt keine Sprosse; die Stufe steht nur
  im Feld sprosse.
- Befund für den Katalog: Die Vorstufe von Einheit 4 („wie viel ist
  das Ganze?“) verlangt eine Zahl; unterrichtsblatt 2.3 a lässt
  Vorstufen ohne Zahlergebnis.
- `\bruchrechteck[5]{0}{20}` (e1, leeres Rechteck): Die Anleitung
  zeigt 0 gefüllte Teile nur für `\bruchkreis`. Kein LaTeX
  kompiliert.
- Einzelstreifen mit `\streifen`/`\streifenfeld` statt
  `\streifenwertreihe`; Reihen bildet der Zusammenbau.
- Der Rechenweg von „Steigung in Prozent berechnen“ hat weiter kein
  eigenes Original (Katalog 10i); die Sprosse steht mit 3 Varianten.

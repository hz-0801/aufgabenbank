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
    zone.jsonl      30         0         12       18         0        0
    e1.jsonl        47         0          5       18        12       12
    e2.jsonl        57        12          5       18        10       12
    e3.jsonl        48         0          5       21        10       12
    e4.jsonl        41         8          5       12         4       12
    e5.jsonl        52         8          5       18        12        9
    gesamt         275        28         37      105        48       57

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

## Offene Punkte

- Zone ohne Fehler-finden-Paar: unterrichtsblatt 2.2 verlangt es
  einmal je Zone, die Mengen in bank.md nennen es nicht.
- Mengen für Erkennungsschritte (4) und Typen ohne Kette (3) sind
  hier gesetzt; bank.md regelt sie nicht.
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

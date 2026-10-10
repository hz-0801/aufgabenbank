# Befunde M3 – Bau von Lerneinheiten

Je Zeile ein Befund aus einem Bau, der über die Einheit hinausgeht; Entscheidung des Agenten in Klammern.

## Prozentrechnung E1 „Prozente als Anteile“ (3Y5, 09.10.2026)

- Setzer: `satz.form` „reihe“ setzt die Bilder aller Teile gleich breit nebeneinander; bei Hunderterfeldern musste die Grafik selbst klein (2,4 cm) sein, sonst ragt sie über die Spalte. Keine Breitenangabe je Teil im Satz-Objekt. (Grafik klein gebaut; setzer.py nicht geändert.)
- Setzer: In „reihe“ steht die Antwortlinie unter dem Text, eine Einheit hinter der Linie (luecke) kennt nur „zwei“; „Anteil in Prozent: ___“ ohne „%“. (Hingenommen.)
- Setzer: Eine Tabelle mit grau vorgerechneter Spalte gibt es nur als freies LaTeX im satz.text (form „frei“); \sachtabelle kennt keine graue Spalte. (Tabelle als tabular in satz.text; grafik behält \sachtabelle für andere Wege.)
- Setzer: Ankreuzoptionen in „frei“ nur über \kk im Text; satz.kreuz greift nur in „zwei“. (So gesetzt.)
- Bank-Ketten passen wieder nicht zum Lernweg: L1-2 (Streifen mit 4/5/20 Teilen) liegt in der Pflichtkette k3-s3 (darstellung), die Zielaufgabe in k1-s8. Mengenwarnungen des Prüfers (k1 s2/s3/s5/s6/s7, pflicht darstellung 6×, 2019-OS-K5b 3×) entstehen aus den Zusatzzeilen, die der Bauauftrag verlangt. (Hingenommen; Vorschlag wie M2: Mengenregel für Zeilen mit schritt aussetzen.)
- Prüfer: Lösungen mit mehreren Ergebnissen (Päckchen, Tabelle) müssen jede pruef-Zahl direkt nach „=“ tragen; „a) jeder fünfte $= 20\,\%$“ statt „a) $20\,\%$ …“. Die Sperre meldet „4 von 100“ als Zahlenpaar aus 2020-OS-B1a, obwohl es die Kernaussage der Einheit ist. (Zahlen gewechselt: 5 von 100, 8 von 100.)
- Bestand E1: Die Grundfälle k1-s1 (Streifen mit zehn Teilen, fünfmal dieselbe Aufgabe) und k1-s2 (ein Bruch je Zeile) sind Einzelaufgaben ohne Päckchen; neue Päckchen-Zeilen gebaut, die alten nicht als schwach markiert, weil sie als Zusatz dienen.
- Thema-Weg: Probetest aus den Hauptoriginalen aller fünf Einheiten gesetzt, bevor E2–E5 gebaut sind; spätere Baue prüfen, ob die Reihenfolge (schwerste zuletzt: 2026-FOR-K3c) trägt.

## Pythagoras E1 „Hypotenuse berechnen“ (M74, 09.10.2026)

- Kritiker (Fable) wollte die drei Sachaufgaben (Bild, Karte, Text) hinter
  die Zielaufgaben schieben, weil die Zielaufgaben das Dreieck fertig
  zeigen und darum leichter wirken. (Nicht übernommen: Bauauftrag
  „Sache steigern, fertige Skizze → Bild → Karte → Text“ und Lernblatt
  endet mit der schwersten Aufgabe des Lernwegs. Der Einwand zeigt aber
  einen Widerspruch: die P10-Zielaufgabe ist oft leichter als die Sache
  davor. Zu klären am Ende von M3, ob „Ziel“ die Prüfungshöhe oder die
  schwerste Aufgabe heißt.)
- Zehn ältere E1-Zeilen (Grundfall, Runden, Dezimal) geben die Antwortform
  „c² = __, c = __“ vor (Bauregel 6.9) und sind darum schwach markiert;
  dasselbe gilt vermutlich für weitere Einträge aus dem Füllauf vor dem
  08.10. (Nicht gesucht; Vorschlag: bank-pruef warnt bei „² = __“.)
- Setzer: setzt die Originalliste am Blattende auch im Lernblatt (bekannt,
  plan.md § 7 „erste Setzerrunde“); sonst setzte er E1 ohne Eingriff
  (11 Nummern, 3,8 s). Form „reihe“ mit leeren Teiltexten (Gleichung unter
  dem Bild) und „paeckchen“ mit folgt über zwei Sprossen trugen.
- Leitertext und Skizze: bank-pruef verlangt bei „Skizziere/Zeichne“ ein
  grafik-Feld, auch wenn der Schüler selbst zeichnet. (\rechenplatz als
  grafik eingetragen; der Setzer liest bei form frei nur karo.)
- bank-pruef warnt bei jeder Zusatzzeile über der Menge (je Sprosse 3,
  Original 2). Der Bauauftrag verlangt je Schritt mindestens drei Zusätze;
  die Warnungen sind gewollt, verdecken aber echte. (Vorschlag: Zeilen mit
  schritt aus der Mengenwarnung nehmen.)

## Prozentrechnung E2 „Prozentsatz berechnen“ (4NT, 09.10.2026)

- Kritiker (Fable) wollte das Erkennen des Ganzen (L2-2) hinter die Taschenrechner-Stufe schieben und dort ausrechnen lassen, weil es die sichere Folge Streifen → Erweitern unterbricht. (Nicht übernommen: Bauauftrag „Erkennen vor Rechnen“; die Falle „Teil zu Rest“ soll vor dem ersten Rechnen sichtbar sein. Zu prüfen am ersten Einsatz.)
- Setzer: Form „frei“ kennt keine Teile; eine Tabelle mit zwei Fragen (L2-6) braucht die Antwortzeilen als freies LaTeX in satz.text, Fuß und Lösung dann als ein Eintrag „a) …; b) …“. (So gesetzt.)
- Setzer: In „reihe“ ohne Teiltext steht unter dem Bild nur eine Linie ohne Einheit „%“ (wie E1). (Hingenommen.)
- Bank-Kette E2: Die Erkennen-Kette k1-s0 („Was ist das Ganze?“) ist als Vorstufe einzeln je Zeile gebaut; das Päckchen mit gemischten Fallen (Summe, Differenz, alter Preis) fehlte. Die Grundfall-Zeilen k3-s1 sind fünfmal dieselbe Sache (Instrument) und darum bis auf v1 schwach markiert.
- Prüfer: Mengenwarnungen durch die vom Bauauftrag verlangten Zusatzzeilen (k1-s0, k3-s0/s2/s4/s5/s6/s7, Originale 2015-OS-K7c und 2018-OS-K7a je 3×, pflicht anwendung 4×) – wie bei E1; verdecken echte Warnungen.
- Thema-Weg: Der Probetest nennt 2018-OS-K7a für E2; der Bau zeigt, dass 2015-OS-K7c (Rest bilden, runden) die eigentliche Decke ist. Reihenfolge des Probetests unverändert.
## Pythagoras E2 zweiter Teil „Ist der Winkel recht?“ (P9H, 09.10.2026)

- Kritiker (Schritt 6) nicht gelaufen: Der Bau-Agent hatte kein Werkzeug,
  um einen Unteragenten (Fable) zu starten. (Im Katalog „offen“; der Chat
  holt ihn nach. Vorschlag: Kritiker vom Chat aus starten, nicht vom
  Bau-Agenten.)
- Setzer: Ankreuzen mit mehreren Teilen in einer Zeile (a, b, c je drei
  Optionen) gibt es nicht; „reihe“ verlangt je Teil ein Bild, „zwei“ kennt
  satz.kreuz nur für die ganze Nummer. (Als form „frei“ mit \kk im
  satz.text und Teilen nur für Fuß und Lösung gesetzt.)
- Setzer: In „reihe“ steht der Teiltext unter dem Bild; bei der
  Knotenschnur wäre der Text über dem Bild natürlicher. (Hingenommen.)
- Bank-Ketten: Die Umkehrung liegt als Sprossen 8–10 in der Kathete-Kette
  (k3), die Knotenschnur in der Pflichtkette begruenden (k6), die
  Zielaufgabe in k3-s12 neben der Seilbahn. Die Kette mischt zwei Blätter;
  Lernweg-Feld schritt trennt sie (L2k/L2u). (Hingenommen; bei der
  Katalogüberarbeitung eine eigene Kette „Umkehrung“ erwägen.)
- Die Zielaufgabe nach 2025-OS-K2c (Drachenfenster) hatte keine Skizze;
  das Original zeigt eine. TikZ-Skizze ergänzt und den Prüfungssatz „Nutze
  dazu die Umkehrung“ im satz.text weggelassen (Bauregel 4.1).

## Prozentrechnung E3 „Prozentwert berechnen“ (E5F, 09.10.2026)

- Kritiker (Schritt 6) nicht gelaufen: wieder kein Werkzeug für einen
  Unteragenten im Bau-Agenten (wie P9H). (Im Katalog „offen“; Vorschlag
  wie dort: Kritiker vom Chat aus.)
- Erkennen (Teil oder Prozentsatz gesucht?) steht als L3-5 nach den
  Rechenwegen, nicht vorn: Die Entscheidung „mal oder Teil : Ganzes“ setzt
  voraus, dass beide Wege bekannt sind; vorn stünde nur der Weg aus E2.
  Widerspricht dem Wortlaut „Erkennen vor Rechnen“; beim Mischen zweier
  Verfahren gilt eher „Erkennen vor dem gemischten Rechnen“. (So gebaut;
  am Ende von M3 klären. Kritiker bestätigt (Fable, 09.10.): Reihenfolge
  bleibt; nach dem Ankreuzen jetzt eine kurze Mischnummer mit Rechnen.)
- Setzer: Form „frei“ mit Ankreuzzeilen je Teil (L3-5) geht nur über \kk
  im satz.text; die graue Musterzeile a) mit angekreuztem Kästchen
  ($\boxtimes$) steht von Hand im Text. (Wie P9H; hingenommen.)
- Setzer: Päckchen mit Tabelle (Zielaufgabe L3-7) nur, indem die Tabelle
  in satz.text steht; grafik behält \sachtabelle für andere Wege. (Wie E1.)
- Bestand E3: Grundfall k1-s1 war fünfmal dieselbe Aufgabe (25 % am
  Streifen); v3–v5 schwach. Die Kette hatte keine Erkennen-Vorstufe; neu
  als k1-s0 (4 Zeilen). Die Prüfungssprosse nennt 2019-OS-K5a nur als
  „Zunahme“; die Zielaufgabe hängt eine Prozentsatz-Frage an (Ganzes erst
  bilden), weil der Bauauftrag hier E2 einmischt.
- Prüfer: Mengenwarnungen (k1 s1/s2/s4/s5/s7/s10, k2 s1, Originale
  2021-OS-B1c und 2019-OS-K5a je 3×) entstehen aus den verlangten
  Zusatzzeilen, wie E1/E2.

## Pythagoras E3 „Das Dreieck erst finden“ (UV3, 09.10.2026)

- Kritiker (Schritt 6) nicht gelaufen: auch dieser Bau-Agent hatte kein
  Werkzeug für einen Unteragenten. (Im Katalog „offen“; Chat holt nach.)
- Setzer: Körperskizzen mit benannten Punkten (S, M, P, H) und
  Rechtwinkelmarke gibt es in mathblatt.sty nicht; \kegel und \pyramide
  setzen keine Punktnamen, \zylinder keinen Stab. (Als freies TikZ im
  Feld grafik gezeichnet; Vorschlag: \kegel/\pyramide/\zylinder mit
  optionalen Punktnamen und Stab.)
- Setzer: form „reihe“ setzt unter jedes Bild eine Antwortlinie auch
  bei „Fahre nach“-Aufgaben; ein Teil ohne Linie fehlt. (Hingenommen.)
- Setzer: form „frei“ hat keine Antwortzeile mit Einheit; Nr. 7 endet
  im Karo. (Hingenommen.)
- Bank-Kette E3: Die Grundfälle k2-s1 geben „h² = __“ vor und sind
  fünfmal derselbe Schenkel 65 cm; v1, v3–v5 schwach, besser k2-s1-v7.
  Weitere E3-Zeilen (s10–s12, s16) tragen „h_s = __“; nicht geändert.
- Breite: Raumdiagonale, Trapez, Parallelogramm, Raute, Horizont und
  Rückwärts-Sprossen stehen nicht auf dem Blatt (Zusatz oder ohne
  Lernweg). Der Katalog nennt noch „Schräge Strecken im Körper“ als
  zweites Blatt; im Thema-Weg gestrichen, Serie angepasst. Zu
  entscheiden, ob ein zweites E3-Blatt (Quader, Pyramide) nötig ist.
- Prüfer: Mengenwarnungen durch Zusatzzeilen wie bei E1/E2.

## Prozentrechnung E4 „Grundwert berechnen“ (WFW, 09.10.2026)

- Kritiker (Schritt 6) nicht vom Bau-Agenten gestartet (Auftrag: der
  Chat startet ihn). Im Katalog „offen“.
- Bestand E4: Grundfall k2-s1 war fünfmal dieselben 24 kg Äpfel, nur der
  Satz wanderte, ohne Streifen; v1–v5 schwach, besser k2-s1-v6 (neu,
  Streifen rückwärts). Die Ketten-Vorstufe k1-s0 fragte „Grundwert
  ankreuzen“ unter einer Frage, die das Ganze schon nennt (Bauregel
  „Erkennen“); neu k1-s0-v5–v7 stellen „p % von“ gegen „p % sind“.
- Zielaufgabe: Die Originale (2025-OS-B1a, 2023-OS-B1b) sind
  Kurzantworten; die Einheit soll alle drei Fragerichtungen mischen.
  Darum eine Rabatt-Tabelle mit wechselnder Frage je Zeile („nach
  P10 ’25“), nicht das Original selbst.
- Setzer: Tabelle im Päckchen wieder nur über satz.text (wie E1/E3).
  Fußhilfe zu Nr. 2 zeigt Rechenterme statt Ergebnisse; hingenommen,
  weil die Aufgabe nichts ausrechnet.
- Prüfer: Mengenwarnungen (k1 s0, k2 s1/s3/s5/s7, 2025-OS-B1a 5×,
  pflicht anwendung 4×) aus den verlangten Zusatzzeilen, wie E1–E3.
- Nach Kritik (09.10.): 1 %-Weg und Taschenrechner in einer Nummer;
  der Lernweg hat jetzt sechs Schritte (L4-1..L4-6, Felder schritt der
  Bank nachgezogen). k2-s5-v4 schwach, besser k2-s3-v6.

## Prozentrechnung E5 „Prozentuale Veränderung“ (S2L, 09.10.2026)

- Kritiker (Schritt 6) nicht vom Bau-Agenten gestartet (Auftrag: der
  Chat startet ihn). Im Katalog „offen“.
- Breite: Die Einheit trägt sieben Sorten (Faktor, Veränderung in
  Prozent, alter Wert, Brutto/Netto, Prozentpunkte, Steigung, gemischt).
  Das Blatt nimmt nur, was die Zielaufgabe (Preistabelle nach
  2026-FOR-K3c) trägt; alter Wert, Brutto/Netto, Prozentpunkte und
  Steigung stehen als Zusatz (neu je eine Zeile mit Streifen bzw.
  Skizze). Zu entscheiden, ob ein zweites E5-Blatt („Rückwärts und
  Sonderfälle“: alter Wert, Brutto/Netto, Prozentpunkte, Steigung nach
  2025-OS-K4b) nötig ist – die drei Sorten sind P10-Stoff.
- Bestand E5: Grundfall k2-s1 war fünfmal dieselben 70 €, der Streifen
  zeigte nur den Prozentwert; v1–v5 schwach, besser k2-s1-v6 (Streifen
  über oder unter 100 % verlängert). Keine E5-Zeile hatte satz; alle
  Blattzeilen neu.
- Setzer: kein Baustein „Streifen über 100 %“ in mathblatt.sty; die
  verlängerten Streifen stehen als TikZ in grafik (Katalog 27.09.
  nannte ihn Baustein-Wunsch). Tabelle im Päckchen wieder nur über
  satz.text. form „frei“ für Ankreuzen mit grauem a) wie E4.
- Prüfer: Mengenwarnungen (k1 s0, k2 s0–s8, 2026-FOR-K3c 5×) aus den
  verlangten Zusatzzeilen, wie E1–E4.
- Nach Kritik (09.10.): Der gemeldete Rechenfehler in Nr. 2 c) war
  keiner – dort stand „auf 90 % gesenkt“ → 0,9. Umgestellt auf „um 90 %
  gesenkt“ → 0,1 mit „sinkt auf 70 %“ daneben. Übrige e5-Zeilen auf
  um/auf/Faktor gegengelesen: kein Fehler.

## Lineare Funktionen E1 „Proportionale Funktion“ (VUC, 10.10.2026)

- Setzer: `bilder()` findet nur `\begin{tikzpicture}`; ein `ksys` oder
  eine `\wertetabelle` in grafik fiele stumm vom Blatt (erster Bau in
  Abschnittsform mit Koordinatensystemen). Umgangen: beide in einen
  tikzpicture-Knoten gewickelt. Vorschlag: `bilder()` auch `ksys` und
  Tabellen erkennen lassen. (setzer.py nicht geändert.) – *erledigt 10.10.: setzer.py, Bausteine aus mathblatt.sty werden gesetzt, Unbekanntes bricht mit id ab*
- Setzer: Die Kopfzeile „Blatt:“ wird an „·“ geteilt; „Weiter: Lineare
  Funktion f(x) = m·x + n“ wurde abgeschnitten. (Im Block „mx + n“.) – *erledigt 10.10.: setzer.py, geteilt nur an „ · “ vor einem Schlüssel*
- mathblatt.sty: `\wertetabelle` mit leerem x-Eintrag ergibt `$$` und
  bricht ab; nur y-Einträge dürfen leer sein. (Leerer x-Eintrag als
  `{\ }`.) – *erledigt 10.10.: setzer.py, der Setzer macht leere Einträge zu `{\ }`*
- Prüfer: merkmal muss je Sprosse gleich sein, kann also an
  Abschnittszeilen nicht sagen, was die Aufgabe ändert. (merkmal aus
  dem Bestand übernommen.) Mengenwarnungen (k1 s2–s8, k2 s1, pflicht
  darstellung 17×) aus den verlangten Vorratszeilen, wie E1–E5 Prozent. – *erledigt 10.10.: bank-pruef.py prüft merkmal an Zeilen mit rolle nicht mehr*
- Bestand E1: Die Ketten passen nur grob zum Lernweg; Abschnitt C
  (Gleichung am Graphen) und Teile von D liegen in Pflichtketten (k3).
  Fehler-finden (k1-s7) nicht auf dem Blatt (Bauauftrag 4).
- Kritiker (Schritt 6) offen; der Chat startet ihn.
## Wahrscheinlichkeit E2 „Wahrscheinlichkeit einstufig“ (KUV, 10.10.2026)

- Erster Bau des Themas in Abschnittsform: Thema-Weg und Lernweg-Block
  neu im Katalog (vor „Prüfliste“, Zeilennummern für quelle bleiben).
  Kritiker offen.
- Breite: Die Einheit trägt fünf Fertigkeiten (Laplace, Gesamtzahl und
  Prozent, Gegenereignis, veränderte Grundmenge, Zufallsgerät und
  Vorhersage) – fünf Abschnitte plus Probetest, 7 Seiten. Zu
  entscheiden, ob das für Klasse 7 zu viel für ein Heft ist (Teilung
  nach C möglich: „Wahrscheinlichkeit berechnen“ / „Grundmenge und
  Vorhersage“).
- Setzer: `bilder()` nimmt nur `tikzpicture`; der Baustein
  `\kreisdiagramm` aus mathblatt.sty (Bestand E2) wird in tisch/selbst
  nicht gesetzt. Glücksräder darum als TikZ in grafik. Wunsch: Setzer
  nimmt auch Bausteinaufrufe als Bild. – *erledigt 10.10.: setzer.py, Bausteine werden gesetzt*
- Setzer: Registerzeile trägt das Systemdatum (2026-10-09, Container in
  UTC) und keinen Pfad; in der KUV-Zeile von Hand auf 2026-10-10 und
  den Bauordner gesetzt. – *erledigt 10.10.: setzer.py, Datum aus --datum oder Europe/Berlin, Pfad aus --aus/--pfad*
- Kennung: Erst VUC gezogen, zeitgleich auch von lineare-funktionen E1
  vergeben (paralleler Bau, Register erst beim Satz). Umbenannt in KUV;
  im Katalog-Commit be8c06c steht noch VUC, berichtigt im Folgecommit.
  Vorschlag: Kennung beim Start des Baus ins Register schreiben. – *erledigt 10.10.: setzer.py, --reserviere; Bauauftrag „Ablage“*
- Prüfer: merkmal muss je Sprosse gleich sein – neue Zeilen tragen das
  merkmal der Sprosse; das Feld sagt so nichts über die neue Stufe.
  Mengenwarnungen (k3 s1–s13, k4, k5) aus dem verlangten Vorrat, wie E1–E5
  Prozent. – *erledigt 10.10.: bank-pruef.py prüft merkmal an Zeilen mit rolle nicht mehr*
- duplikate.py: neue Zeilen nur als Zahlvarianten in derselben Sprosse
  (Lostrommel, Würfel, Münze) und in C-Gruppen „Glücksrad, 1/2“.

## Quadratische Funktionen E1 „Normalparabel und Streckfaktor“ (GHQ, 10.10.2026)

- Setzer (Abschnittsform): loesungsgrafik wird nicht gesetzt; die
  Zeichenaufgaben (A3, B2) zeigen im Lösungsheft nur die Punkte als
  Text. (loesungsgrafik trotzdem gefüllt; setzer.py nicht geändert.) – *erledigt 10.10.: setzer.py, loesungsgrafik unter dem Weg, alle Sorten*
- Setzer: nimmt aus grafik nur `\begin{tikzpicture}…`; die
  mathblatt-Umgebung `ksys` (Bestand der Kette) wird nicht erkannt.
  Graphen darum als pgfplots-Achse in tikzpicture; die ksys-Proben
  von bank-pruef greifen an diesen Zeilen nicht. – *erledigt 10.10.: setzer.py, ksys wird gesetzt*
- Setzer tisch-alt: Die rechte Spalte neben dem Bild ist schmal; eine
  Wertetabelle mit sieben Spalten im grauen Beispiel ragt über den
  Rand. (Beispieltabelle auf fünf Spalten gekürzt.) – *erledigt 10.10.: setzer.py, Tabellen werden in die Spaltenbreite eingepasst*
- Setzer: schreibt das Registerdatum nach Systemzeit (UTC, 09.10.);
  von Hand auf 10.10. gesetzt. – *erledigt 10.10.: setzer.py, Europe/Berlin*
- Prüfer: merkmal muss je Sprosse gleich sein; was eine neue Zeile
  gegenüber der vorigen ändert, lässt sich bei Lernweg-Zeilen darum
  nicht festhalten. (merkmal aus dem Bestand übernommen.) – *erledigt 10.10.: bank-pruef.py prüft merkmal an Zeilen mit rolle nicht mehr*
- Prüfer: Mengenwarnungen (k1 s0–s12, 2015-OS-K4b 5×, 2026-FOR-B1e
  4×, pflicht anwendung 15×) aus den verlangten Vorratszeilen, wie
  bei allen Bauen; dazu „Prüfungshöhe ohne Original“ für das Beispiel
  D (k1-s14, keine Prüfaufgabe). Hingenommen.
- Katalog: Die Hauptmarke 2015-OS-K4b braucht den Startwert e; E1
  führt darum a·x² + e (Abschnitte C, D). Der Thema-Weg vermerkt es;
  E2 kann auf „Scheitel auf der y-Achse“ aufbauen.
- Ziel bei Funktionen: „keine vorgegebene Gleichung“ heißt hier, der
  Schüler stellt h(x) aus Breite und Höhe (Tor, Tunnel, Halfpipe) oder
  aus dem Fallgesetz in Worten selbst auf. Zu prüfen am Kritiker, ob
  der Sprung von C4 zu C5 (Ursprung selbst legen) zu groß ist; der
  Tipp „Ursprung in die Mitte“ steht nur in C5.

## Trigonometrie E1 „Seite berechnen mit sin, cos und tan“ (N9M, 10.10.2026)

- Erster Bau des Themas; Thema-Weg und Lernweg-Block im Katalog neu
  (vor der Prüfliste, Zeilennummern für quelle bleiben). Abschnitte
  A Seiten benennen, B Kathete: mal, C Seite im Nenner: geteilt,
  D Welche Funktion?, T Probetest. Mal und geteilt als eigene Abschnitte
  statt der Kettenfolge sin → cos → sin geteilt …: eine Rechenregel je
  Seite, die Funktion wechselt darin.
- Kritiker (Schritt 6) startet der Chat; im Block „offen“.
- Setzer: Ankreuzoptionen mit `\dfrac` überlappen sich zeilenweise
  (Zeilen ohne Zusatzabstand); darum `\frac` wie im Prüfstein, klein.
  Registerzeile nennt immer „sorten=tisch-alt tisch selbst“, auch wenn
  nur zwei gesetzt sind, und das Datum der Systemuhr (2026-10-09). – *erledigt 10.10.: setzer.py, Register nennt nur gesetzte Sorten, Datum Europe/Berlin*
- Prüfer: Mengenwarnungen k3 s0–s15, k4 s1 aus Blatt- und
  Vorratszeilen, wie bei den anderen Bauten. Bestehende Bankzeilen
  tragen quelle 102 (älterer Katalogstand); neue übernehmen den Wert
  der Sprosse, weil der Prüfer ihn je Sprosse einheitlich verlangt.
- Probetest ohne Vorrat-leichter (kein Beispiel im Abschnitt); Vorrat
  dort nur gleichwertig.

## Brüche und Dezimalzahlen E1 „Bruch als Anteil“ (QG4, 10.10.2026, Fable-Bau)

- Lage: Der Katalog nennt an der Einheit OS Kl. 5, die P10-Form fragt
  aber fünf von neun Flächen-Originalen in Prozent (Voraussetzung
  „Prozent als Hundertstel“, Kl. 7). Blatt auf Klasse 7 gesetzt (Verortung:
  Oberschule 7–8 regulär). (Entscheidung des Agenten; Lehrer prüft, ob
  Abschnitt E auf einem Kl.-5-Blatt wegfällt – dann „QG4 ohne E“.)
- Setzer: `bilder()` nimmt nur ganze tikzpicture-Blöcke; die Bausteine der
  alten Zeilen (\bruchrechteck, \bruchkreis, \kreisdiagramm) erscheinen in
  den Sorten tisch/selbst nicht. Die alten E1-Zeilen sind darum in
  Abschnittsform nicht setzbar, ohne grafik neu zu schreiben. (Alle 67
  Zeilen mit eigenem TikZ gebaut; setzer.py nicht geändert.) – *erledigt 10.10.: setzer.py, Bausteine werden gesetzt*
- Setzer: Bei TikZ-Gittern mit `x=0.5cm` braucht `grid` die Angabe
  `step=1`, sonst liegen die Linien bei 1 cm (jedes zweite Kästchen) –
  Bildkontrolle fing es. Für bauauftrag.md „Zerlegen“ als Hinweis geeignet.
- Setzer: Die Lösungsseite druckt links ergebnis und rechts loesung;
  beginnt loesung mit dem Ergebnis (nötig für die Ergebnisstelle des
  Prüfers), steht es doppelt. (Hingenommen; Vorschlag: weg() schneidet
  ein führendes ergebnis ab, wie bei Ankreuzoptionen.) – *erledigt 10.10.: setzer.py, führendes ergebnis fällt im Weg weg*
- Prüfer: Mengenwarnungen wie in M2/3Y5 (k1 s6 trägt jetzt 40 Varianten,
  Originale bis 10×), weil alle P10-Formen – Prozent, Schraffieren,
  Sektoren – an einer Prüfungssprosse hängen. Ein Abschnitt „Anteil in
  Prozent“ hat keine eigene Sprosse; die Lernweg-Felder tragen die
  Struktur. (Hingenommen.)
- Katalog: Kein Thema-Weg vorhanden; angelegt mit der Katalogfolge 1–5 und
  Begründung. Einheit 2 (Kürzen) wird auf diesem Blatt umgangen: Prozent
  aus der Figur über „Figur : 4 = ein Viertel“ statt Kürzen (9/15 = 3/5).
  Beim Bau von E2 prüfen, ob 2014-OS-B1i dort die Zielmarke bleibt.
- Gestrichen aus dem Katalog-Typenvorrat: „Figur mit gegebenem Anteil
  auswählen“ (2026-FOR-B1b) – kein eigener Abschnitt, keine neue Zeile;
  die Bank hat drei alte (k1-s4). Beim Nachbestellen „mehr“ fehlt diese
  Form in TikZ.

## Wahrscheinlichkeit E3 „Baumdiagramm und Pfadregeln“ (6KD, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten. Roter Faden:
  dasselbe Glücksrad in allen Beispielen, nur das Ereignis ändert sich.
  Kritiker offen.
- Zielaufgaben wechseln die Antwortform: belegen (A), fair? (B), um wie
  viel daneben? (C), welches Spiel? (D), wie viele Kugeln? (T).
- Bäume als TikZ in grafik (eigener Erzeuger im Bauskript): `\baumzwei`
  aus mathblatt.sty trägt keine fetten Pfade und keine Kästchen zum
  Eintragen in Schreibgröße; Kästchen 7 × 4 mm, Astwerte in
  footnotesize. Wunsch (Später): Baum-Baustein mit Kästchen und
  fettem Pfad in mathblatt.sty.
- tisch-alt: 7 Seiten, die letzte trägt nur T5 – die Bäume sind höher als
  die Skizzen anderer Einheiten. selbst hält 6 Seiten.
- Lösungsheft selbst 3 Seiten wegen der Lösungsbäume (max. 4 cm); ohne
  loesungsgrafik wären es 2.
- duplikate.py: erste Fassung von D1 (Münze dreimal, 1/8) war A-Dublette
  zu kombinatorik-zone-f4-v2; ersetzt durch Stern-Rad (1/64).
- Prüfer: Mengenwarnungen k3 s1–s11 aus dem verlangten Vorrat, wie E2.
## Brüche E2 „Kürzen und Erweitern“ (A5D, 10.10.2026)

- Lage: Standardlage Klasse 6 laut Katalog; E1 (QG4) steht auf Klasse 7.
  Die Serie hat damit zwei Klassen. Abschnitt C nutzt Prozent über den
  Nenner 100 mit der Hilfe „1/100 = 1 %“ in der Aufgabe. (Nicht
  geändert; Lehrer entscheidet, ob die Brüche-Serie einheitlich Kl. 6
  oder Kl. 7 heißt.)
- Satz: Brüche im Fließtext (\frac) sind für Kl. 6 in Päckchen zu klein
  (zweistellige Zähler). Päckchen nach \par als \dfrac, davor
  \vspace{3pt}; \smallskip lehnt bank-pruef ab (nicht in STANDARD).
  (So gesetzt; Vorschlag: smallskip/medskip in STANDARD.)
- Setzer: Die Ergebnisspalte der Lösungen ist schmal; Päckchen-Ergebnisse
  mit zwei Brüchen je Teil brechen um. ergebnis kurz gefasst („Nenner
  12; 15; 24“), die Brüche stehen im Weg. (Hingenommen.)
- Ablauf: Parallele Bau-Agenten teilen sich das Scratchpad; ein gleich
  benanntes Bauskript (bau_e2.py) wurde von einem anderen Bau (BP8)
  überschrieben und einmal ausgeführt (schreibt nur in dessen Klon
  /root/work/w2b, wiederholbar). (Eigene Skripte danach in einem
  Unterordner je Kennung; Vorschlag für bauauftrag.md: Hilfsdateien im
  Scratchpad unter <Kennung>/.)
- Prüfer: Mengenwarnungen wie bei QG4 (k1 s3 13 Zeilen, s4 10), weil der
  Bauauftrag Vorrat verlangt. (Hingenommen.)
- Thema-Weg trägt: Gleichnamigmachen gehört in E2 (E3 wendet es nur an);
  2014-OS-B1i bleibt Zielmarke – als Probetest-Aufgabe (14/40 = 7/20 =
  35 %), nicht als Ziel, weil die Figur das Modell vorgibt.

## Quadratische Funktionen E2 „Scheitelpunktform“ (BP8, 10.10.2026)

- Setzer: Ein „|“ in Satz oder Formel einer Lernweg-Zeile (S(d|e)) zerschneidet die Tabellenzelle; der Setzer bricht mit KeyError ab statt mit der Zeile. (Im Block {\vert} geschrieben wie in E1.)
- Setzer: Alle Sorten schreiben 1-uebersicht/2-blatt/3-loesungen in denselben --aus-Ordner und überschreiben sich; je Sorte ein eigener Ordner, dann umbenannt. (So gemacht.) – *erledigt 10.10.: setzer.py, Dateinamen je Sorte (selbst, tisch-alt …), Register ergänzt sorten=*
- Setzer (selbst): „Rechne unten im Karo“ steht auch auf Seiten, auf denen kein Karo mehr Platz hat (A, B). Der Schüler sucht das Karo. (Hingenommen.)
- Achsenzahlen: Bei Parabeln nah an der y-Achse liegt der Bogen auf den Zahlen neben dem Scheitel. Die Zahlen sind dort weggelassen (Prüfung im Bauskript); der Schüler zählt dann Kästchen. Vorschlag: Achsenzahlen mit weißem Grund über dem Bogen als Baustein in mathblatt.sty.
- bank-pruef: Ein Ergebnis „f(x) = (x − 4)² + 1“ hat keine Zahl an der Ergebnisstelle; Behelf wie im Bestand: Scheitel als Punkt in die Lösung, pruef [d, e].
- Thema-Weg: „Was der Scheitel verrät“ (Nullstellen zählen, steigen/fallen, Lage) steht vor „Verschieben und spiegeln“, weil die Hauptmarke 2018-OS-K5d beides verlangt; im Thema-Weg ergänzt.

## Lineare Funktionen E2 „Lineare Funktion f(x) = m·x + n“ (NKP, 10.10.2026)

- Setzer: Der Name der Einheit wird aus der Kopfzeile bis zur ersten Klammer genommen; „f(x) = m·x + n (Abschnitte …)“ wird zu „Lineare Funktion f“ (Register lerneinheit=, Titel von tisch-alt). Das Selbstlernheft trägt den Titel aus „Titel:“ richtig. (setzer.py nicht geändert; Vorschlag: nur die letzte Klammer abschneiden.)
- Heft auf 6 Seiten nur mit kleinen Koordinatensystemen (Karo 4 mm) und zwei Geraden je Päckchen in einem System; die Seiten A–C haben darum keinen „Platz zum Rechnen“. Für Zeichenabschnitte trägt die Seitengrenze (eine Seite je Abschnitt) höchstens drei Zeichenaufgaben plus Beispiel.
- Prüfer: Zuordnen mit nummerierten Gleichungen „(1) … (6)“ findet die Lösungszahlen nicht an der Ergebnisstelle; mit Buchstaben (A)–(F) und Zahlen nach „=“ in der Begründung geht es. Sperre trifft gewollt kurze Distraktoren (y = −2x, y = x − 2, 3x + 1 aus 2019-OS-K2c/2021-OS-K2a); Zahlen gewechselt.
- Prüfer: Tabellen- oder Ankreuzzeilen mit mehreren Teilen (steigt/fällt/waagerecht für a–d) gibt es nicht; \begin{tabular}, \hfill, \smallskip sind in aufgabe verboten. (Als Zeilen mit \par und $\square$ gesetzt.)
- Beschriftung von Geraden am Rand des Systems lässt ein kurzes Linienstück zwischen Rand und weißem Etikett stehen; Etiketten mindestens eine Einheit nach innen gesetzt.
- Bestand E2: Wertetabelle als Zeichenweg (k4-s1 bis s3) und Fehler finden (k7-s1) nicht genommen; m = 0 hat keine eigene Sprosse (steht in k5-s6 und k6-s1).
- Mengenwarnungen wie bisher durch die Vorratszeilen (k4-s4/s5/s6/s8, k5-s2 bis s6, k6-s1, pflicht begruenden/darstellung).

## Trigonometrie E2 „Winkel berechnen“ (LT3, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, Lösungen 2.
  A Winkel aus zwei Seiten, B Steigungswinkel in Sachen, C Winkel in
  Figuren und Nachweis, D Seite oder Winkel? (mischt mal und geteilt aus
  E1 mit der Umkehrtaste), T. Thema-Weg Punkt 2 ergänzt. Kritiker offen.
- Zielaufgaben wechseln die Antwortform: im Bereich? (A), um wie viel
  steiler? (B), Behauptung prüfen (C), Mindestlänge und erlaubt? (D),
  um wie viel länger? (T). Probetest prüft cos⁻¹, sin⁻¹, tan⁻¹, mal und
  geteilt je einmal.
- Jeder Hinweis einmal: SHIFT nur in Formel A, RAD nur bei den Fehlern,
  90° − α nur in B; Formelkasten S. 1 ohne die Regel aus D.
- Bank: neue Zeilen nach kette, sprosse, variante einsortiert; ans Ende
  angehängt meldet der Prüfer „hoehe nach höherer Stufe“ (68×).
  Mengenwarnungen k1 s1–s12 aus dem verlangten Vorrat, wie E1.
- Setzer: Sorte selbst schreibt 2-blatt.pdf und 3-loesungen.pdf; von
  Hand in selbst.pdf, selbst-loesungen.pdf (tisch-alt ebenso) umbenannt
  wie in den anderen Probeordnern, .tex gelöscht.
- duplikate.py: nur D-Beispiel und D-Vorrat-leichter (gleicher Auftrag,
  andere Zahlen), gewollt.
- Skizzen klein (D: drei Dreiecke in 6,4 cm Spalte): steile Dreiecke
  (7 : 4) waren zu schmal für Winkelmarke und Fragezeichen; Zahlen auf
  flache Dreiecke geändert.

## Brüche E3 „Brüche vergleichen“ (FS9, 10.10.2026)

- Lage: Standardlage Klasse 6 laut Katalog (wie A5D). Heft 6 Seiten:
  Übersicht, A–D, Probetest; jede Seite mit Rechenplatz.
- Satz: Ankreuzoptionen mit \dfrac stoßen im Setzer zeilenweise
  aneinander (zwei Optionen je Zeile, kein Zeilenabstand für hohe
  Brüche). In \kreuz daher \frac. (Vorschlag Setzer: \kreuz-Zeilen mit
  \strut oder größerem Abstand, wenn eine Option \dfrac trägt.) – *erledigt 10.10.: setzer.py, Ankreuzbrüche als \dfrac in einer Zeile mit Abstand*
- Setzer: Mehrdeutige Ankreuzaufgabe („alle ankreuzen, die …“) lässt
  bank-pruef nicht zu (genau eine Option); D4 und T5 deshalb mit genau
  einer richtigen Option. (Hingenommen.)
- Prüfer: Päckchen „Setze < oder >“ haben kein Ergebnis an der
  Ergebnisstelle; pruef trägt den ersten Bruch, die eigentliche Prüfung
  lief mit Fraction im Bauskript. Mengenwarnungen wie bei QG4/A5D.
- duplikate.py: B-119 (Päckchen „Setze < oder >“) sind gewollte
  Zahlvarianten.
- Thema-Weg trägt: Vergleich mit 1/2 und 1 steht beim Zahlenstrahl (C),
  nicht als eigener Abschnitt; die Zielmarke 2014-OS-B1c ist Abschnitt
  D und T4.

## Wahrscheinlichkeit E4 „Ohne Zurücklegen“ (XKT, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, tisch-alt 6
  Seiten. Roter Faden: derselbe Beutel (3 rot, 2 blau) in allen vier
  Beispielen. Kritiker offen.
- Thema-Weg ergänzt: Abschnitt D „Mit oder ohne Zurücklegen?“ mischt
  beide Fälle (am Text erkennen, beide rechnen, vergleichen); steht
  zuletzt, weil man erst unterscheiden kann, was man beides kennt. Die
  Vorstufe „mit oder ohne ankreuzen“, in E3 gestrichen, steht jetzt hier
  (D1).
- Zielaufgaben wechseln die Antwortform: Beutel wählen (A), Zweite im
  Nachteil? (B), wievielmal statt doppelt? (C), um wie viele
  Prozentpunkte? (D), aufzählen + rechnen + Behauptung (T, nach
  2018-OS-K7c).
- Neue Baumform dreistufig mit aufgebrauchter Sorte (ein Ast) im
  C-Beispiel vorgegeben. Bei 0,62 cm Blattabstand überdeckten sich
  Kästchen und Astwerte der 3. Stufe; 0,75 cm und 3. Stufe 0,5 cm
  länger trägt es.
- Probetest verlangt „Ergebnisse aufzählen“ und „Gegenteil in drei
  Zügen“ nur, weil B2 (Pfade aufschreiben) und C3 (unter den ersten
  drei) sie üben; „Rechnung → Ereignis“ als B1 b).
- Prüfer: 0 Abweichungen; Mengenwarnungen k1 s0–s10 aus dem verlangten
  Vorrat, wie E2/E3. duplikate.py: keine Gruppe mit e4.

## Lineare Funktionen E3 „Punkte und Werte“ (ZLZ, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, Lösungen 2:
  A Funktionswert, B Punktprobe, C x zum Funktionswert, D Nullstelle und
  Achsenschnittpunkte (mit Schnittpunkt zweier Geraden am Graphen), T.
  24 Aufgaben auf dem Blatt, 23 im Vorrat. Thema-Weg Punkt 3 ergänzt.
  Kritiker offen.
- Zielaufgaben wechseln die Antwortform: reicht es? (A), ankreuzen (B),
  aufrunden auf ganze Wochen (C), Reserve als Unterschied (D), welche
  Kerze länger und um wie viel? (T).
- Achsen: Bei karo unter 0,5 cm beziffert ksys die x-Achse nur jede
  zweite Zahl, sobald dort negative Zahlen stehen (die breiteste Zahl
  bestimmt die Ausdünnung; NKP-Bilder mit 0,36 sind betroffen). Hier
  überall karo 0,5. Eine Gerade mit positiver Steigung und negativem n
  läuft links über die y-Zahlen; im Beispiel D darum xmin = 0.
- Prüfer: Ankreuzen mit zwei richtigen Optionen geht nicht („genau eine
  Option“); Ziel B auf eine Option umgestellt. Punkte mit `\mid` und
  negativer Koordinate erkennt er nicht als Ergebnis; in loesung und
  ergebnis als `(0|{-8})` geschrieben (setzt sauber, ohne Abstand).
- Setzer: Ein `|` in einer Zelle des Lernweg-Blocks (Formel
  `\big|\,-n`) zerlegt die Zeile; Abbruch mit KeyError statt Meldung.
  Formel mit `\xrightarrow{-n}` geschrieben. Ankreuzlösung „Option.
  Text“ lässt im Lösungsheft „. Text“ stehen; mit „Option: Text“ geht es.
  (setzer.py nicht geändert.)
- Mengenwarnungen k2 s1–s7, k3 s1, pflicht anwendung aus dem verlangten
  Vorrat, wie bisher. duplikate.py: nur gewollte Zahlvarianten
  (Vorrat zu Blattzeilen; Wertetabelle in Form wie e2-k4-s1).

## Trigonometrie E3 „Teildreiecke in Figuren und Vermessung“ (56N, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, Lösungen 2.
  A Teildreieck in der Figur, B Hilfslinie: Kathete als Unterschied,
  C Vermessung: Höhenwinkel und Gerätehöhe, D Zwei Schritte (Teilwinkel,
  zwei Dreiecke an derselben Höhe), T. Thema-Weg Punkt 3 ergänzt.
  Kritiker offen.
- Parallelogramm, Stützdreieck (Pyramide, Kegel), zweiter Weg mit
  Pythagoras nicht aufs Blatt: sonst sieben Seiten; Bestand bleibt.
- „Höhenwinkel“ führt kein früherer Abschnitt und kein Formelkasten
  ein; steht jetzt im Satz von C. begriffe.md prüfen, ob das Wort dort
  fehlt. (Nicht geändert, nicht meine Datei.)
- Teilwinkel-Skizze: Zwei Bögen am selben Punkt mit zwei Zahlen lesen
  sich mehrdeutig (die Zahl des großen Winkels landet im kleinen Feld).
  Darum nur der Teilwinkel mit Zahl, der große Winkel steht im Text.
- Seiten C und D waren mit fünf Skizzen ohne Rechenplatz; Skizzen auf
  höchstens 2,2 cm Höhe begrenzt, dann bleiben vier bis fünf Karozeilen.
- Prüfer: Mengenwarnungen k1 s0–s18 aus Blatt- und Vorratszeilen, wie
  bei den anderen Bauten. duplikate.py: nur Vorrat gegen Blattzeile
  (gleicher Auftrag, andere Zahlen), gewollt.

## Quadratische Funktionen E3 „Normalform“ (7P7, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, Lösungen 2.
  A Normalform lesen und einsetzen, B Von der Scheitelpunktform zur
  Normalform, C Scheitelpunktform aus dem Graphen, D Die passende Form
  wählen, T. Thema-Weg Punkt 3 ergänzt. Kritiker offen.
- Ziele wechseln die Antwortform: liegt Q darauf? (A), hat Lena recht?
  (B), um wie viel über (0|10)? (C), alle Gleichungen angeben (D),
  Halfpipe am Rand zu hoch? (T).
- Achsenzahlen: eigene TikZ-Graphen (ksys setzt die Zahlen unter den
  Bogen). Jede ganze Zahl beziffert; kreuzt der Graph die Zahl, wechselt
  sie auf die andere Seite der Achse (x auch leicht seitlich); nur am
  y-Achsenabschnitt bleibt sie mit weißem Grund, der Bogen hat dort eine
  kleine Lücke. Vorschlag wie bei BP8: diese Wahl als Baustein in
  mathblatt.sty.
- Seitengrenze: Mit drei Graphen trug C keinen Platz zum Rechnen mehr;
  die Ankreuzaufgabe „welche Scheitelpunktform passt?“ steht darum in D
  (Paare vergleichen). Raster 3,2 mm je Einheit für Aufgabengraphen.
- Sperre: Normalformen der Originale (x² − 6x + 7, x² − 2x − 3,
  x² − 4x + 2, x² + 2x − 1, x² + 4x + 3 u. a.) und Terme der Typischen
  Fehler ((x + 3)² − 2, x² + 4x) treffen naheliegende eigene Zahlen;
  Zahlen gewechselt.
- bank-pruef: Bei „Weise nach“ und Päckchen von Normalformen steht an
  der Ergebnisstelle nur die erste Zahl; pruef trägt wie im Bestand nur
  sie, die übrigen Werte prüft das Bauskript mit sympy.
- Setzer: Bei Ankreuzaufgaben bleibt ein „;“ nach der Option am Anfang
  des Wegs stehen (weg() streicht nur Leerzeichen und „:“); Option mit
  „:“ abgetrennt. Mehrteilige Ergebnisse brechen in der 52-mm-Spalte
  mitten im Term um; je Teil \mbox{…}.
- duplikate.py: nur gewollte Zahlvarianten (Ziel D und Vorrat, T5 und
  Bestand k1-s10-v1).

## Brüche E4 „Dezimalzahlen“ (DXZ, 10.10.2026)

- Lage: Standardlage Klasse 6 laut Katalog (wie A5D, FS9; Katalog-Marke
  OS Kl. 5, GYM Kl. 5–6). Heft 6 Seiten: Übersicht, A–D, Probetest;
  jede Seite mit Rechenplatz.
- Setzer: Ein zweiter Satz mit `--kennung` (tisch-alt nach selbst)
  ergänzt sorten= im Register nicht; von Hand nachgetragen. (Vorschlag
  Setzer: sorten= auch beim Neusatz mit --kennung ergänzen.) – *erledigt 10.10.: setzer.py, Dateinamen je Sorte (selbst, tisch-alt …), Register ergänzt sorten=*
- Setzer: tisch-alt legt praeambel.tex in den Probenordner (von
  tisch-alt-blatt.tex eingebunden); FS9 hat sie nicht. (Belassen.)
- Satz: Ankreuzoptionen mit \frac sind bei Kl. 6 kaum lesbar; T5 mit
  \dfrac gesetzt – die Zeilen liegen dicht, aber getrennt. D4 statt
  Ankreuzen als Päckchen „ja oder nein“. (Vorschlag wie bei FS9:
  \kreuz-Zeilen mit mehr Abstand.) – *erledigt 10.10.: setzer.py, Ankreuzbrüche als \dfrac in einer Zeile mit Abstand*
- Prüfer: pruef muss ein String sein (Zahl führt zu „nicht
  auswertbar“); periodische Ergebnisse brauchen pruef (hier „1/3“,
  „4/9“). Ergebnis einer Differenz nur an der Ergebnisstelle, wenn es
  hinter „=“ steht („750 − 700 = 50 g“). Mengenwarnungen wie bei
  QG4/A5D/FS9.
- duplikate.py: nur gewollte Zahlvarianten (Aufgabe und Vorrat
  derselben Sprosse; A1/A2 gleicher Auftrag „Schreibe als
  Dezimalzahl“).
- Thema-Weg trägt: Zehnerbruch vor Zahlenstrahl vor Erweitern vor
  Teilen. Achtel über Division statt Erweitern auf 1000; Vergleichen
  bleibt in E5 und kommt in E4 nur über die Sache (Gramm, Zeiten) vor.
## Daten E2 „Säulen-, Balken- und Liniendiagramme“ (T74, 10.10.2026)

- Erster Bau des Themas: Thema-Weg und Lernweg in katalog/daten.md neu.
  A Säulen ablesen, B Werte vergleichen und auswählen, C Liniendiagramme
  lesen, D Säulen zeichnen und Achse einteilen, T. Selbstlernheft
  6 Seiten, Lösungen 2. Kritiker offen.
- Ziele wechseln die Antwortform: Preis ja/nein (A), Betrag aus Anzahl
  Tage (B), welcher Monat? (C), zuordnen und zeichnen (D), zeichnen und
  um wie viel (T).
- Rechenplatz: Mit Diagrammen von 3 cm hatten A, C, D keinen Karo mehr
  (9 Seiten). Säulen und Linien auf 1,9 cm, höchstens 12 Hilfslinien;
  Kästchenwert-Aufgaben als einzeilige Päckchen ohne Bild.
- `\balkenab` (mathblatt.sty) setzt je Kategorie mindestens 0,73 cm und
  ordnet die erste Kategorie unten an; in der rechten Spalte zu hoch,
  und „Mo“ unten liest sich verkehrt. Balken darum als eigenes TikZ
  (0,55 cm je Zeile, erste oben). Vorschlag: Schlüssel zeilenhoehe und
  Reihenfolge oben→unten in `\balkenab`.
- Setzer: Jede Sorte schreibt 1-uebersicht/2-blatt/3-loesungen in
  denselben Ordner; die zweite Sorte überschreibt die erste. Umbenannt
  nach dem Satz. – *erledigt 10.10.: setzer.py, Dateinamen je Sorte (selbst, tisch-alt …), Register ergänzt sorten=*
- bank-pruef: 0 Abweichungen (Mengenwarnungen k2 s0–s12 aus Blatt- und
  Vorratszeilen wie bei den anderen Bauten); duplikate.py: keine neue
  id betroffen.

## Quadratische Funktionen E4 „Nullstellen und Schnittpunkte“ (GHD, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, Lösungen 2.
  A Nullstellen aus der Scheitelpunktform, B mit der p-q-Formel, C Zu
  einem y-Wert die x-Werte, D Schnittpunkte von Parabel und Gerade, T.
  Thema-Weg endgültig (Punkt 4 innen, Probetest um 2023-OS-K4c,
  2014-OS-K7a/b ergänzt). Kritiker offen.
- Ziele wechseln die Antwortform: Tom hat recht? (A), Ball landet
  drüben, um wie viel? (B), Schild passt, wie viel Platz? (C), Gerade
  angeben und nachrechnen (D), welcher Schnittpunkt höher? (T).
- Setzer, tisch-alt: Der Fuß kürzt ein Ergebnis über 45 Zeichen am
  ersten „: “, „. “ oder „; “ – auch innerhalb von \mbox{…} und nach
  „z.\,B.“; dann bricht xelatex ab (\fusshilfe nicht geschlossen).
  Ergebnisse darum nur mit Komma getrennt. Vorschlag: kurz() nur auf
  Klammerebene 0 schneiden. – *erledigt 10.10.: setzer.py, kurz() schneidet nur auf Klammerebene 0 außerhalb $…$, nicht nach z.\,B.*
- Sperre traf naheliegende Zahlen: x² − 4x und (x + 3)² (Typische
  Fehler), −2x + 3, 2x − 3, x² − 4x + 2, (x − 1)² − 3 (Originale);
  gewechselt.
- Prüfer: Mengenwarnungen k1 s1–s21 und pflicht anwendung aus Blatt-
  und Vorratszeilen, wie bei den anderen Bauten. duplikate.py: nur
  gewollte Zahlvarianten (T1 gegen k1-s1-v1/v3/v5).


## Lineare Funktionen E5 „Anwendungen“ (PRC, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, Lösungen 2:
  A Gleichung aus dem Text, B Graph und Gleichung in der Sache, C
  Endwert und rückwärts, D Tarife vergleichen, T. 21 Aufgaben auf dem
  Blatt, 23 im Vorrat. Thema-Weg Punkt 5 ergänzt. Kritiker offen.
- E4 (Gleichsetzen) ist noch nicht gebaut; „ab wann günstiger“ ist darum
  in D vollständig vorgerechnet und in B am Graphen vorbereitet. Wird E4
  gebaut, kann D kürzer werden. (So gebaut.)
- Graphen kosten Platz: Mit vier Sachgraphen auf Seite B (Karo 0,5)
  fiel das Rechenkaro weg. „Graph zu Tarif zuordnen“ darum in den
  Vorrat, auf dem Blatt eine Deute-Aufgabe ohne Bild; y-Achsen in 2er-,
  4er-, 15er-Schritten, damit die Bilder höchstens 8 Kästchen hoch sind.
  Zuordnen steckt nur noch im Ziel B (welche Gerade ist das Abo?).
- Ziele wechseln die Antwortform: Unterschied von m (A), Schnittpunkt
  ablesen und entscheiden (B), reicht es / wie viel länger (C), wer ist
  günstiger und ab wann der andere (D, T).
- Prüfer: Ergebnisstelle verlangt jede pruef-Zahl nach „=“; bei
  Rundungsaufgaben die gerundete ganze Zahl („nach 22 Minuten“) aus
  pruef genommen, der ungerundete Wert bleibt; die Rundung steht in
  tmp-sympy. Zuordnen ohne Zahl: pruef aus „bei $y = 8$“ gebildet.
  Setzer schreibt 2-blatt.pdf/3-loesungen.pdf, im Probenordner von
  Hand umbenannt.
- Mengenwarnungen k1 s0–s5, k2 s1, pflicht aus dem verlangten Vorrat,
  wie bisher. duplikate.py: keine neue id betroffen.

## Trigonometrie E4 „Sinussatz“ (XAD, 10.10.2026)

- Vier Abschnitte plus Probetest, Selbstlernheft 6 Seiten, Lösungen 2.
  A Seite aus einem ganzen Paar, B Erst den dritten Winkel, C Winkel aus
  der Figur (Nebenwinkel, Teilwinkel, stumpfer Winkel), D Ergebnis
  weitergeben (Weg, Rest, Nachweis), T. Thema-Weg Punkt 4 ergänzt, Stand
  und Probetest des Themas endgültig (2025-OS-K4c dazu). Kritiker offen.
- Kosinussatz und Winkel mit dem Sinussatz nicht aufs Blatt: kein
  P10-Original, nur RLP G; die Bank hat die Sprossen 12–14. Will der
  Lehrer den Kosinussatz für FOR oder GYM, wäre das ein eigenes Blatt.
  (Linie des Lehrers, nicht entschieden.)
- Setzer: weg() streift nach der Ankreuzoption nur „ :“ ab; eine Lösung
  „Option; …“ zeigt im Lösungsheft „; a ≈ 8,1“. Ankreuzlösungen darum
  mit „:“ nach der Option geschrieben. (setzer.py nicht geändert.)
- Skizzen: Viereck mit Diagonale und einem Winkel über die Diagonale
  (140° bei C) erst lesbar, wenn die Figur gedreht ist (AC waagerecht);
  je Ecke höchstens ein Winkel mit Zahl.
- Prüfer: quelle muss je Sprosse einheitlich sein; neue Zeilen tragen
  die alte Zeilennummer der Sprosse (105, 100), nicht die heutige.
  Mengenwarnungen k1 s0–s10 aus dem Vorrat, wie bei den anderen Bauten.
  duplikate.py: nur D3 gegen seinen Vorrat (Nachweis, andere Zahlen),
  gewollt.

## Terme E5 „Termwerte berechnen“ (MZE, 10.10.2026)

- Erster Bau des Themas: Thema-Weg und Lernweg in katalog/terme.md neu.
  Der Thema-Weg stellt Termwerte (E5) und Aufstellen (E6) vor das
  Zusammenfassen (E1), weil die Variable als Platzhalter die
  Grundvorstellung ist und die Lehrwerke sie in Kl. 6–7 bringen; die
  Blattfolge „terme“ (Muster 4, Lehrer 01.10.) ist nicht geändert.
  (Linie des Lehrers, offen.)
- Katalogkette Termwert ohne Bruchstrich, obwohl 2016-OS-B1i und
  2021-OS-B1g ihn verlangen; Sprossen 7–13 ergänzt (Zeile 110).
- Abschnitte A–D plus T, Heft 6 Seiten, Lösungen 2. Schritt-Zuordnung
  jeder Aufgabe zu einem Beispiel in plan.md des Probenordners.
- Prüfer: Sperre trifft Merkkastenzahlen (2·(x+5), 3x² bei x = −2) –
  gewechselt. \smallskip ist kein Baustein; \vspace{3pt} genommen.
  Mengenwarnungen aus dem Vorrat wie bisher. duplikate.py: keine neue
  id betroffen.
- Setzer tisch-alt: Wertetabelle steht über dem Auftragstext (Grafik vor
  Text). Hingenommen.
## Daten E3 „Streifen- und Kreisdiagramm“ (FWE, 10.10.2026)

- Setzer: Die Bildspalte (0,37 Zeilenbreite ≈ 6,4 cm) verkleinert einen
  10-cm-Streifen; zum Zeichnen muss er aber echt 10 cm lang sein
  (1 % = 1 mm). Streifen darum in aufgabe gesetzt (volle Breite, ohne
  grafik). Der Prüfer verlangt bei „Zeichne“ eine grafik; Wortlaut darum
  „Trage ein“ / „Stelle dar“. (Vorschlag: grafik-Option „breit“ – Bild
  unter dem Text in voller Breite; setzer.py nicht geändert.)
- Setzer: Im Beispiel setzt die Bildspalte \streifenvoll so klein, dass
  „Auto“ (10 %) kaum lesbar ist; Streifen darum im letzten Schritt
  (schritte) in voller Breite. In tisch-alt bleibt er klein, aber lesbar.
- Seitenmaß: Mit Kreisen r = 2 cm (\kreisleer) und vier Aufgaben liefen C
  und D über (8 Seiten). Auf drei Aufgaben je Abschnitt, Zeichenkreise
  r = 1,6 cm und Lesediagramme r = 1,1–1,6 cm gekürzt; je eine Aufgabe in
  den Vorrat. Heft 6 Seiten, jede Aufgabenseite mit Rechenplatz.
- Lösungsheft: \mbox um lange Zuordnungsergebnisse läuft über die
  52-mm-Spalte; lange Ergebnisse ohne \mbox schreiben.
- Prüfer: Mengenwarnungen k1 s1–s12 und k2 s1 aus dem Vorrat, wie bei den
  anderen Bauten; duplikate.py nur B-Treffer (gewollte Zahlvarianten).
## Flächen E1 – Rechteck, Quadrat, Umfang (9WQ, 10.10.)

- Term zu Figur (Zielmarke 2025-OS-B1i, 2014-OS-B1g) nicht ins Heft:
  Der Katalog nennt Klasse 5, dort gibt es noch keine Variablen. Der
  Typ bleibt im Bestand (k2-s8, k5-s4); wenn der Lehrer ihn will, ein
  eigenes Blatt ab Klasse 7. (Linie des Lehrers, nicht entschieden.)
- Quadratseite aus der Fläche braucht die Wurzel (Kl. 8 laut Katalog);
  im Heft nur als „Zahl, die mal sich selbst A ergibt“ mit
  Quadratzahlen, das Zeichen √ einmal in der Formel erklärt.
- Einheiten wechseln (cm und m gemischt) nicht im Heft: kein Beispiel
  auf 6 Seiten frei; gehört zum Thema Einheiten.
- Prüfer: Ergebnisstelle verlangt Unterschiede als Rechnung
  („$32 - 30 = 2$ m² mehr“), nicht nur als Zahl im Satz.
- Mengenwarnungen k2/k3 aus dem Vorrat wie bei den anderen Bauten;
  duplikate.py ohne Treffer an den neuen Zeilen.



## Brüche E5 „Vergleichen, Ordnen, Runden“ (HMF, 10.10.2026)

- Lage: Standardlage Klasse 6 laut Katalog (wie DXZ). Heft 6 Seiten:
  Übersicht, A Vergleichen und ordnen, B Runden, C Dazwischen und Mitte,
  D Bruch, Prozent, Quadrat erst umwandeln, T. Jede Zielaufgabe und
  jede T-Aufgabe Schritt für Schritt einem Beispielschritt zugeordnet
  (plan.md § 3); dabei fiel auf, dass das Mitte-Beispiel „Komma zwei
  Stellen zurück“ für 0,04/0,05 (Tausendstel) nicht passte – Schritt
  allgemein gefasst. Kritiker offen.
- Thema-Weg endgültig: Vorher-Check (Zone, je Feld eine Zeile) und
  Probetest mit allen 17 Originalen des Themas nachgetragen (Form wie
  trigonometrie.md, quadratische-funktionen.md).
- Mitte über „ohne Komma rechnen, halber Abstand“ statt (a + b) : 2:
  Kl. 6 halbiert eine Dezimalzahl allein noch nicht sicher.
- Bank: Die alten E5-Zeilen (v1–v3) tragen schon die naheliegenden
  Zahlen (3,864 runden; 7,06/7,6/7,006 ordnen; 0,64/0,68); duplikate.py
  fand zwei wörtliche Treffer, Zahlen geändert. Neue Zeilen nur noch
  gewollte Zahlvarianten derselben Sprosse.
- Prüfer: Sperre greift auf „0,4² = 0,8“ auch als falsche
  Ankreuzoption (D4 nun 0,3² = 0,6). Ankreuzen mit Zahloptionen
  verlangt pruef = Zahl einer Option (bei „0,2²“ also 0,2, nicht
  0,04). Ordnen: Lösung als Liste „a; b; c; d“, sonst steht nur die
  erste Zahl an der Ergebnisstelle. Mengenwarnungen aus dem Vorrat wie
  bei DXZ.
- Satz: \leerfeld-Reihen mit vier Teilen umbrechen nach c); lesbar,
  aber unruhig. (Belassen; Vorschlag Setzer: Vergleichszeichen-Päckchen
  in zwei Spalten.)

## Winkel und Dreiecke E2 „Winkel an Geradenkreuzungen und Parallelen“ (FP6, 10.10.2026)

- Seitengrenze: Sechs Seiten mit Karo auf jeder Aufgabenseite tragen bei
  Figuraufgaben nur drei Aufgaben je Abschnitt (Skizze rechts bestimmt die
  Zeilenhöhe). B und C von vier auf drei gekürzt, das Gekürzte im Vorrat.
  (Vorschlag: Bauauftrag nennt „3 Aufgaben, wenn jede eine Skizze hat“.)
- Erster Bau des Themas: Thema-Weg (vorläufig) und Lernweg-Abschnitt neu
  angelegt; Teilwinkel und verlängerte Seiten als eigener Abschnitt B vor
  den Parallelen (beides braucht nur Scheitel- und Nebenwinkel).
- Katalogtext „drei Geraden durch einen Punkt“ (Typen Einheit 2): Eine
  volle dritte Gerade teilt beide Scheitelwinkel, der Winkel α wäre dann
  selbst geteilt. Auf dem Blatt ist k ein Strahl ab dem Schnittpunkt.
  (Katalog nicht geändert; beim Abgleich „Strahl“ statt „Gerade“ erwägen.)
- Setzer: mathblatt-Bausteine \geradenkreuzung/\parallelenpaar setzen die
  Beschriftung fest auf Radius 1,05; bei spitzen Winkeln unter 40° liegt die
  Zahl auf der Linie. Alle Figuren als eigene TikZ mit Abstand nach
  Winkelgröße gebaut. (Hingenommen; Vorschlag: Bausteine rechnen den
  Abstand aus der Winkelgröße.)
- bank-pruef: Mengenwarnungen durch die Vorratszeilen (k2 s1–s10) wie bei
  allen Bauten; neu „s11 Prüfungshöhe ohne Original“ – zwei neue
  Prüfungszeilen nach 2015-OS-B1d ohne original-Feld, weil Zahlen und
  Wortlaut neu sind. (Hingenommen.)

## Terme E6 „Terme aufstellen“ (BGG, 10.10.2026)

- Thema-Weg aus MZE gehalten; bei Schritt 2 ergänzt, dass Umfang und
  Fläche des Rechtecks vorausgesetzt sind und x + x = 2x nur als
  „gleiche Seiten mit Malpunkt“ vorkommt (Zusammenfassen folgt in E1).
- Abschnitte A Rechenwörter · B Klammer · C Term zur Figur · D Sachterme
  · T; Heft 6 Seiten, Lösungen 2; 26 Zeilen auf dem Blatt, 19 Vorrat.
  Schritt-Zuordnung jeder Aufgabe in plan.md des Probenordners.
- Neue Sprosse 11 „Sachterm mit Klammer: mehrere gleiche Pakete“ (Kino,
  Zug, Busse): die Klammer kommt in der P10 nicht nur aus Rechenwörtern.
  hoehe pflicht/anwendung, weil sie hinter der Prüfungshöhe steht.
- Setzer: Text nach den \kreuz-Optionen fällt im Satz still weg (Ziel B
  zuerst mit Teil b nach den Optionen – Teil b fehlte). Optionen ans
  Ende gestellt. Kandidat für bank.md: „\kreuz steht am Ende von
  aufgabe“ oder Prüfer-Warnung.
- Prüfer-Sperre traf 3·(x + 4) (Merkkasten E3) – auf x + 5 gewechselt.
- e6.jsonl nach Kette, Sprosse, Variante sortiert (angehängte Zeilen
  ergaben sonst „Varianten nicht 1..n“). duplikate.py: s2-v4 ist
  gewollte Zahlvariante von s2-v2.
- Setzer tisch-alt: Tabelle steht über dem Auftragstext (wie MZE).
## Daten E4 „Kenngrößen“ (4CR, 10.10.2026)

- bank-pruef: \smallskip ist kein Baustein; Tabellen im Aufgabentext mit
  \par\vspace{3pt} absetzen (wie E2). Bei „Aussage prüfen“ (ankreuzen)
  muss die berichtigte Zahl hinter „=“ stehen, sonst gilt sie nicht als
  Ergebnisstelle. (Hingenommen.)
- Formel-Zeile im Kopf und im Abschnitt: zwei lange Formeln mit \qquad
  brechen mitten in der Formel um; \newline zwischen ihnen hilft.
  (Vorschlag: Bauauftrag nennt „je Formel eine Zeile“.)
- Notenspiegel (gewichtetes Mittel) und Ausreißer passen nicht in sechs
  Seiten; sie bleiben Bank. (Vorschlag: eigener Zusatzabschnitt zum
  Nachbestellen, wenn der Lehrer ihn will.)
## Flächen E3 – Dreieck (SC4, 10.10.)

- Lage: Klasse 7 laut Katalog. Das Parallelogramm (E2) ist ungebaut und
  ohne P10-Typ; das Heft führt die Höhe darum selbst ein (A, B), statt
  sie vorauszusetzen. Thema-Weg ergänzt.
- Term zu Figur ins Heft (D, T3): ab Klasse 7 gibt es Variablen; damit
  ist die Zielmarke 2024-OS-B1c/2022-OS-B1e abgedeckt, die 9WQ ausließ.
- Setzer: weg() streicht vor der Lösung nur „ “ und „:“ nach der
  Ankreuzoption, nicht „;“ – bei „Option; Grund“ stand „; …“ auf der
  Lösungsseite. (Lösungen als „Option: Grund“ geschrieben.)
- Skizzen: Beschriftungen an schrägen Linien mit Gradanker überschnitten
  die Linie; mit Eckankern (south west …) liegt der Kasten ganz auf
  einer Seite. Bei stumpfen Dreiecken die schräge Seite innen
  beschriften, sonst trifft sie die Höhe außen. (Eigener Helfer, nicht
  im Setzer; Vorschlag: Baustein für Dreieck mit Höhe in abbildung.py.)
- Sperre: 9·4:2 (Drachen im Merkkasten) traf eine eigene Ankreuzaufgabe;
  Zahlen gewechselt.
- Mengenwarnungen k1/k2/k3, 2020-OS-K7b 6× und pflicht anwendung 7× aus
  Blatt und Vorrat wie bei den anderen Bauten; duplikate.py nur die
  gewollte Zahlvariante des Päckchens (k1-s4 v4/v5).
- Kritiker: offen (startet der Chat).
## Körper E1 „Körper erkennen, Netze, Schrägbilder“ (L75, 10.10.2026)

- Setzer: Bilder stehen immer in der rechten Spalte (37 %, höchstens
  6,4 cm) und werden nur verkleinert; ein Netz in wahrer Größe (2
  Kästchen = 1 cm) passt nur bis 6 cm Breite. Das Karo am Abschnittsende
  fällt weg, sobald die Seite voll ist – bei Netz- und Schrägbildseiten
  immer. (Zeichenaufgaben tragen ein eigenes Kästchenfeld als grafik;
  Bilder mit scale 0,5–0,8 gesetzt; Abschnitt C ohne Formel, damit er auf
  eine Seite passt. Vorschlag: grafik mit Breitenwunsch „voll“ unter dem
  Text.)
- bank-pruef: „aufgabe mit Umgebung“ verbietet ein Bild im Text; ein
  Kästchenfeld ohne Inhalt muss darum als grafik stehen. Ziffern als
  Bildmarken (1, 2, 3) verlangen pruef; Buchstaben genommen.
- Würfelnetze mit einem kleinen Faltprogramm geprüft (Rollen des Würfels
  über die Quadrate); lohnt als Werkzeug für alle Netzaufgaben der Bank
  (Gegenflächen, gültig/ungültig). (Nur in tmp; nicht ins Repo.)
- Lernweg: Die Regel „genau eine Fläche dazwischen“ trägt nur Netze mit
  einer Reihe aus drei; Treppennetze (2-2-2) bleiben draußen. Körperhöhe
  der Pyramide (2015-OS-K6b) hängt als Schritt 5 am Quader-Beispiel – ein
  zweites Beispiel je Abschnitt kennt der Setzer nicht. Kegel im Quader
  (2024-OS-K4b) nur im Bestand, nicht auf dem Blatt.
- Mengenwarnungen (k1 s1–s10, Originale 2016-OS-B1j 5×, 2019-OS-B1f 6×)
  aus den Zusatzzeilen, wie bei M74 und 3Y5 gewollt.
## Winkel und Dreiecke E3 „Winkelsummen, Dreiecke und Vierecke“ (HDK, 10.10.2026)

- Setzer: Winkelzahlen in \small passen in schmale Winkel nur, wenn die
  Figur groß ist; mit \footnotesize und Platzprobe auf der
  Winkelhalbierenden (Hilfsskript im Bau) standen alle Zahlen frei.
  Eine Figur-Hilfe für Winkelbögen fehlt in mathblatt.sty. (Selbst gebaut;
  Vorschlag: Baustein „winkelbogen mit freiem Label“.)
- Eine gezeichnete Symmetrieachse im Drachen legt die Winkelzahlen an
  den Achsenenden genau auf die Linie. (Achse weggelassen, Striche zeigen
  den Drachen; Achse steht im Text.)
- bank-pruef verlangt pruef auch bei Begründen-Zeilen außerhalb von
  hoehe pflicht (s9 „rechten Winkel begründen“). (pruef mit den Zahlen
  45 und 90 gesetzt.)
- Mengenwarnungen wie bei allen Bauten (Zusatzzeilen je Sprosse).
- Vierecks-Eigenschaft (C3, T4) ist Wissen, kein Rechenschritt; der
  Schritt-Beispiel-Abgleich ordnet sie der Formelzeile zu, nicht einem
  Beispielschritt. (Zu klären: reicht die Formelzeile als „Beispiel“?)
## Körper E2 „Quader und Würfel“ (FEU, 10.10.2026)

- Einheit „l“ hinter einer Zahl liest sich im Satz wie eine 1 („45 l“
  sieht aus wie 451). Im ganzen Heft „Liter“ ausgeschrieben, auch in
  Formel und Kopf. (Vorschlag für bauregeln: Liter ausschreiben.)
- Teilaufgaben mit eigenen Buchstaben a) b) kollidieren in tisch-alt mit
  den Buchstaben des Setzers („b) Rechne um. a) …“). Umrechnen als Liste
  mit Semikolon gesetzt.
- Lernweg: „aus zwei Quadern zusammengesetzt“ an Einheit 5 abgegeben
  (dort „zwei Quader (4×)“); Würfelkante aus V und Maßzahlvergleich
  bleiben Bestand. Heft so in 6 Seiten (A–D, T), Karo auf jeder Seite.
- Schritt-Beispiel-Abgleich: „Wasserhöhe = Gefäßhöhe minus Abstand zum
  Rand“ (T5) brauchte Schritt 5 im D-Beispiel („bis zum Rand“); ohne ihn
  fehlte er. Einheit dm³ (A-Ziel) als Satz im A-Beispiel ergänzt.
- bank-pruef will jede pruef-Zahl an einer Ergebnisstelle („= …“);
  Differenzen darum ausgeschrieben („90 − 80 = 10“).
- Mengenwarnungen (k1 s1–s10, k2, k4, k5; 2026-FOR-B1f 4×) aus den
  Zusatzzeilen, wie bei L75 gewollt.

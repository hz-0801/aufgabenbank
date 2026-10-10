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
- Setzer: Alle Sorten schreiben 1-uebersicht/2-blatt/3-loesungen in denselben --aus-Ordner und überschreiben sich; je Sorte ein eigener Ordner, dann umbenannt. (So gemacht.)
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
  \strut oder größerem Abstand, wenn eine Option \dfrac trägt.)
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

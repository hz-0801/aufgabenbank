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
  Tabellen erkennen lassen. (setzer.py nicht geändert.)
- Setzer: Die Kopfzeile „Blatt:“ wird an „·“ geteilt; „Weiter: Lineare
  Funktion f(x) = m·x + n“ wurde abgeschnitten. (Im Block „mx + n“.)
- mathblatt.sty: `\wertetabelle` mit leerem x-Eintrag ergibt `$$` und
  bricht ab; nur y-Einträge dürfen leer sein. (Leerer x-Eintrag als
  `{\ }`.)
- Prüfer: merkmal muss je Sprosse gleich sein, kann also an
  Abschnittszeilen nicht sagen, was die Aufgabe ändert. (merkmal aus
  dem Bestand übernommen.) Mengenwarnungen (k1 s2–s8, k2 s1, pflicht
  darstellung 17×) aus den verlangten Vorratszeilen, wie E1–E5 Prozent.
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
  nimmt auch Bausteinaufrufe als Bild.
- Setzer: Registerzeile trägt das Systemdatum (2026-10-09, Container in
  UTC) und keinen Pfad; in der KUV-Zeile von Hand auf 2026-10-10 und
  den Bauordner gesetzt.
- Kennung: Erst VUC gezogen, zeitgleich auch von lineare-funktionen E1
  vergeben (paralleler Bau, Register erst beim Satz). Umbenannt in KUV;
  im Katalog-Commit be8c06c steht noch VUC, berichtigt im Folgecommit.
  Vorschlag: Kennung beim Start des Baus ins Register schreiben.
- Prüfer: merkmal muss je Sprosse gleich sein – neue Zeilen tragen das
  merkmal der Sprosse; das Feld sagt so nichts über die neue Stufe.
  Mengenwarnungen (k3 s1–s13, k4, k5) aus dem verlangten Vorrat, wie E1–E5
  Prozent.
- duplikate.py: neue Zeilen nur als Zahlvarianten in derselben Sprosse
  (Lostrommel, Würfel, Münze) und in C-Gruppen „Glücksrad, 1/2“.

## Quadratische Funktionen E1 „Normalparabel und Streckfaktor“ (GHQ, 10.10.2026)

- Setzer (Abschnittsform): loesungsgrafik wird nicht gesetzt; die
  Zeichenaufgaben (A3, B2) zeigen im Lösungsheft nur die Punkte als
  Text. (loesungsgrafik trotzdem gefüllt; setzer.py nicht geändert.)
- Setzer: nimmt aus grafik nur `\begin{tikzpicture}…`; die
  mathblatt-Umgebung `ksys` (Bestand der Kette) wird nicht erkannt.
  Graphen darum als pgfplots-Achse in tikzpicture; die ksys-Proben
  von bank-pruef greifen an diesen Zeilen nicht.
- Setzer tisch-alt: Die rechte Spalte neben dem Bild ist schmal; eine
  Wertetabelle mit sieben Spalten im grauen Beispiel ragt über den
  Rand. (Beispieltabelle auf fünf Spalten gekürzt.)
- Setzer: schreibt das Registerdatum nach Systemzeit (UTC, 09.10.);
  von Hand auf 10.10. gesetzt.
- Prüfer: merkmal muss je Sprosse gleich sein; was eine neue Zeile
  gegenüber der vorigen ändert, lässt sich bei Lernweg-Zeilen darum
  nicht festhalten. (merkmal aus dem Bestand übernommen.)
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
  nur zwei gesetzt sind, und das Datum der Systemuhr (2026-10-09).
- Prüfer: Mengenwarnungen k3 s0–s15, k4 s1 aus Blatt- und
  Vorratszeilen, wie bei den anderen Bauten. Bestehende Bankzeilen
  tragen quelle 102 (älterer Katalogstand); neue übernehmen den Wert
  der Sprosse, weil der Prüfer ihn je Sprosse einheitlich verlangt.
- Probetest ohne Vorrat-leichter (kein Beispiel im Abschnitt); Vorrat
  dort nur gleichwertig.

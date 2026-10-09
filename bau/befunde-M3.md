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
  am Ende von M3 klären.)
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

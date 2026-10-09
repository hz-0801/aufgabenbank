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

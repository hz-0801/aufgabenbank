# Gegenlese: prozentrechnung

Datum: Sun Sep 27 21:40:59 UTC 2026
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 277
Korrekturen: 0

## Punkt 1 – Lösung und pruef
- keine

## Punkt 2 – Eindeutigkeit und Angaben
- prozentrechnung-e2-k5-s2-v3: „Kann ein Teil mehr als 100 % seines Ganzen sein?“ – Lösung „Nein, höchstens 100 %“ widerspricht e3-k1-s7 (150 % von 40 kg = 60 kg, merkmal „der Prozentwert ist größer als das Ganze“) und e4-k3-s2-v3 („bei mehr als 100 % ist der Prozentwert größer als das Ganze“); „Teil“ ist nicht als Teilmenge festgelegt – Frage auf eine Teilmenge festlegen (etwa „Können mehr als 100 % der 28 Kinder einer Klasse ein Rad haben?“) oder durch eine Frage zum Merkmal ersetzen (siehe Punkt 3).
- prozentrechnung-e4-k2-s0-v1, prozentrechnung-e4-k2-s0-v2, prozentrechnung-e4-k2-s0-v3, prozentrechnung-e4-k2-s0-v4: Text spricht von Kästchen, die Grafik `\streifen[0]{…}` zeigt keine Teilung – am Streifen ist nichts abzuzählen, die Vorstufe wird reine Rechnung; sind Karokästchen gemeint (10-cm-Streifen = 20 Kästchen à 5 mm), passt nur v1 (30 % = 6), bei v2–v4 hätte der graue Teil 10, 5 und 12 Kästchen statt 7, 3 und 9 – Teilstriche nach dem Prozentsatz setzen (v1 `\streifen[10]{30}…`, v2 `[2]`, v3 `[4]`, v4 `[5]`), damit abzählbar ist, wie oft ein graues Teilstück ins Ganze passt.

## Punkt 3 – Sprosse und Merkmal
- prozentrechnung-e2-k5-s2-v3: merkmal „begründen, warum durch das Ganze geteilt wird“, die Frage (Teil über 100 %?) fragt nicht danach – ersetzen, etwa „Warum rechnet man bei 9 von 36 Kindern 9 : 36 und nicht 36 : 9?“.
- prozentrechnung-e3-k3-s2-v3: merkmal „begründen, warum der Weg über 1 % geht“, die Aufgabe (Ole: 20 %, ein Fünftel und 20/100 sind dasselbe) handelt von gleichwertigen Schreibweisen, nicht vom 1-%-Weg – ersetzen, etwa „Warum rechnet man für 7 % von 300 € zuerst 300 : 100?“.
- prozentrechnung-e3-k3-s4-v3: sprosse_text „Rabatt und Mehrwertsteuer in Euro“, die Aufgabe (Grippewelle, 15 % von 840 Schülern, Mensaessen) enthält weder Rabatt noch Mehrwertsteuer; v1 (Rabatt) und v2 (Mehrwertsteuer) passen – Kontext auf Rabatt oder Mehrwertsteuer umstellen, etwa Klassenkasse mit 500 € für ein Gerät zu 440 € netto zuzüglich 19 % (523,60 € – reicht nicht).
- prozentrechnung-e4-k3-s2-v3: merkmal „begründen, warum am Ende mal 100 gerechnet wird“, die Aufgabe (Mo: das Ganze ist immer größer als der Prozentwert) fragt nicht danach – ersetzen, etwa „3 % sind 12 kg. Warum rechnet man 12 : 3 und danach noch mal 100?“.

## Punkt 4 – Schreibform
- prozentrechnung-e2-k5-s3-v3: Die Dreisatz-Grafik verlangt die Zeile „1 Teilnehmer“, das ergibt 100 : 120 = 0,8333… % (periodisch); die Lösung weicht auf den Bruch 100/120 % aus und rechnet 54 · 100/120 %, was die Einheit nicht vorbereitet – wer mit dem Taschenrechner 0,83 % einträgt, kommt auf 44,82 %. Mittelzeile 6 statt 1 (: 20 → 6 ≙ 5 %, · 9 → 54 ≙ 45 %) oder Zahlen, bei denen 1 % glatt ist (etwa 125 Teilnehmer, 45 Frauen: 0,8 % je Teilnehmer, 36 %).
- prozentrechnung-e3-k1-s10-v1, prozentrechnung-e3-k1-s10-v2: Die Lösung nennt „17 Prozentpunkte“ / „18 Prozentpunkte“, der Begriff kommt erst in e5-k2-s6 – in Einheit 3 schreiben: „52 % − 35 % = 17 %; 17 % von 800 = 0,17 · 800 = 136 Haushalte“ (entsprechend 18 % von 650 = 117).

## Punkt 5 – Ankreuzen
- keine

## Punkt 6 – Fehler finden
- prozentrechnung-e2-k5-s1-v2: Pauls Rechnung „45 : 18 = 2,5 = 2,5 %“ enthält zwei Fehler (Ganzes und Teil vertauscht und dazu die Dezimalzahl als Prozentzahl gelesen); auf die Frage „Fehler?“ benennen Schüler leicht nur den auffälligeren zweiten – nur den genannten Fehler einbauen: „45 : 18 = 2,5 = 250 %“.
- prozentrechnung-e3-k3-s1-v2: Aylins Rechnung „85 : 20 = 4,25 €“ ist das Muster „Grundwert und Prozentwert vertauscht: 70 : 30 statt 0,3 · 70“ (Typische Fehler, Zeile 82), nicht eines der beiden Muster der Sprosse (30 % als 0,03; Restpreis statt Ersparnis); die Lösung nennt selbst „das Ganze durch die Prozentzahl geteilt“ – Fehler nach dem Muster der Sprosse bauen, etwa „20 % von 85 €: 0,02 · 85 = 1,70 €“.

## Entscheidungen
- Stimmt das Ergebnis einer Prüfungsaufgabe zufällig mit dem Ergebnis ihres Originals überein, ohne dass Zahlenpaar oder Term übernommen sind (e2-k3-s7-v1: 3 : 24 = 12,5 % wie im Original 2 : 16), werte ich das nicht als Sperrverstoß.
- Prüfungsvarianten ohne Rundung (e2-k3-s7-v1, e5-k2-s8-v5, e5-k2-s8-v6) werte ich nicht als Abweichung vom Merkmal „mit Runden“, weil ihre Originale (2018-OS-K7a, 2016-OS-K2c) glatte Ergebnisse haben und die Sprosse mehrere Originale zusammenfasst.
- Prüfungsvarianten, die der Form ihres Originals folgen statt dem Wortlaut der Sprosse (e3-k1-s8-v3/v4 Kurzantwort statt Ankreuzen nach 2017-OS-B1b; e1-k1-s8-v5/v6 Begründung nach 2017-OS-K2b), sind ohne Befund.

Sauber: 264 Zeilen ohne Befund

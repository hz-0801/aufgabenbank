# Zweitlesung prozentrechnung

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 277
(zone 32, e1 47, e2 57, e3 48, e4 41, e5 52)

Prüfung: Jede Zeile gelesen und die Lösung aus dem Aufgabentext selbst
nachgerechnet. 256 Zeilen tragen eine pruef-Zahl; ihre Werte stimmen mit
der eigenen Rechnung und mit loesung überein. Die 28 Zeilen mit Runden,
Tabellensummen oder mehrstufiger Rechnung (Runden auf eine Stelle in
e2 und e5, Tabellen in e1-k1-s8, Auszählen der Listen in e2-k3-s9,
Anwendungen in e3, e5) zusätzlich mit sympy (exakte Brüche, kaufmännisch
gerundet) nachgerechnet: keine Abweichung. 14 Ankreuzzeilen je Option
geprüft (genau eine richtig, loesung wortgleich), 16 Fehler-finden-Zeilen
(eingebauter Fehler wirklich falsch, Richtigrechnung stimmt), dazu Merkmal
und Sprossentext jeder Zeile und die Grafikwerte (Streifenteilung,
Tabellensummen 100 % bzw. Gesamtzahl). `werkzeuge/bank-pruef.py
prozentrechnung`: 0 Abweichungen, 0 Warnungen. Hinweis ohne Befund:
zone-f1-v4 (3 von 12 = 1/4) nimmt das Zahlenpaar aus dem Klammerbeispiel
der Fertigkeit selbst; die Sperre der Bank nennt nur Merkkasten, Typische
Fehler und Originale, darum kein Befund.

## Befunde

e3-k3-s1-v2: [M] Aylins Fehler „85 : 20 = 4,25 €" (Ganzes durch die
Prozentzahl geteilt) ist keines der beiden Muster, die Sprosse und
Merkmal nennen (30 % als 0,03; Restpreis statt Ersparnis) – Fehler auf
eines der beiden Muster umstellen, etwa „15 % von 80 € = 0,015 · 80".

e2-k5-s2-v3: [E] Die Lösung „Nein, ein Teil ist höchstens 100 %" steht
ohne Einschränkung und widerspricht der nächsten Einheit (e3-k1-s7
„Prozentsatz über 100 %", e4-k3-s2-v3 „bei mehr als 100 % ist der
Prozentwert größer als das Ganze") – die Frage an eine Teil-vom-Ganzen-
Situation binden („Können mehr als 100 % der Kinder einer Klasse einen
Hund haben?") oder die Lösung auf „Teil einer Menge" einschränken.

e4-k2-s0-v1, e4-k2-s0-v2, e4-k2-s0-v3, e4-k2-s0-v4: [E] Der Text zählt
Kästchen („das sind 6 Kästchen"), die Grafik `\streifen[0]{…}` zeigt aber
keine Teilstriche, also keine Kästchen; ein Schüler sucht im Bild, was
nicht da ist – „Teile" statt „Kästchen" schreiben oder im Text sagen,
dass die Kästchen nicht eingezeichnet sind.

Sauber: 271 Zeilen ohne Befund

## Abgleich

Beide Leser: e3-k3-s1-v2 – Aylins Fehler (85 : 20) folgt nicht einem der
beiden Muster der Sprosse; beide schlagen ein 0,0p-Muster vor.
e2-k5-s2-v3 – die Lösung „höchstens 100 %" widerspricht e3-k1-s7 und
e4-k3-s2-v3; beide schlagen vor, die Frage an eine Teilmenge zu binden.
e4-k2-s0-v1 bis v4 – der Text zählt Kästchen, die Grafik `\streifen[0]`
zeigt keine.

Nur Erstleser:
e2-k5-s2-v3 [M] – die Frage (Teil über 100 %?) begründet nicht, warum
durch das Ganze geteilt wird: bestätigt, das Merkmal der Sprosse wird
nicht bedient; von mir übersehen, weil ich nur die Aussage geprüft habe.
e3-k3-s2-v3 [M] – Ole (20 % = ein Fünftel = 20/100) handelt von
gleichwertigen Schreibweisen, nicht vom Ein-Prozent-Weg: bestätigt.
e4-k3-s2-v3 [M] – Mo („das Ganze ist immer größer") fragt nicht, warum
am Ende mal 100 gerechnet wird: bestätigt.
e3-k3-s4-v3 [M] – Grippewelle ohne Rabatt oder Mehrwertsteuer: nicht
bestätigt als Befund; das Merkmal der Zeile nennt „Kauf- oder
Planungsentscheidung", die Mensaplanung erfüllt es, und der sprosse_text
ist die Einheitsbeschreibung des Katalogs für die Anwendung. Ein Kontext
mit Rabatt oder Steuer wäre näher an der Einheit, ist aber nicht nötig.
e2-k5-s3-v3 [E] – die Dreisatz-Mittelzeile „1 Teilnehmer" ergibt
100/120 % = 0,833… % periodisch, ohne Hinweis: bestätigt; bank.md
verlangt bei periodischen Dezimalbrüchen einen Hinweis, glattere Zahlen
oder eine andere Mittelzeile sind besser.
e3-k1-s10-v1, e3-k1-s10-v2 [E] – „Prozentpunkte" in der Lösung, bevor
der Begriff in e5-k2-s6 eingeführt ist: bestätigt, als Schreibform der
Lösung; die Rechnung selbst stimmt.
e2-k5-s1-v2 [F] – Pauls Rechnung enthält zwei Fehler (vertauscht und
2,5 als 2,5 %): bestätigt als schwacher Befund; die Lösung benennt beide,
aber ein Fehler-finden mit zwei Fehlern trennt das Muster der Sprosse
nicht sauber.

Nur Zweitleser: keine (alle drei Befunde hat auch der Erstleser).

Widersprüche: keine. Beim Kästchen-Befund schlägt der Erstleser
Teilstriche nach dem Prozentsatz vor, ich „Teile" statt „Kästchen" –
zwei Wege zum selben Ziel; der Vorschlag des Erstlesers ist besser, weil
dann am Streifen abgezählt wird, wie es die Vorstufe will.

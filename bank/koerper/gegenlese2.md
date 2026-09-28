# Zweitlesung koerper

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 290
(zone 28, e1 52, e2 56, e3 47, e4 57, e5 50)

Prüfung: Jede Zeile gelesen (Aufgabe, Antwortgerüst, Lösung, pruef,
Grafik, Merkmal). Alle Rechnungen mit π, Wurzeln und Rundungen
(Zone f2/f5, e3 Prüfungshöhe, e4 vollständig, e5 Halbzylinder,
Restvolumen, Prüfungshöhe, Fehler-finden-Zeilen) mit sympy im Scratchpad
nachgerechnet, die ganzzahligen und Dezimalrechnungen von Hand; alle
216 Zeilen mit pruef-Zahl stimmen mit der eigenen Rechnung und der
Rundung der Lösung überein. Alle 14 Würfelnetze aus e1 (gültig/ungültig,
Gegenflächen, Spielwürfel-Augen) mit einem Faltskript geprüft: alle
Lösungen stimmen. 23 Ankreuzzeilen (davon 3 ja/nein) einzeln gegen jede Option
geprüft (je genau eine richtig, Lösung wortgleich), 16 Fehler-finden-Zeilen
(eingebauter Fehler wirklich falsch, Richtigrechnung stimmt). Maße in
den Grafiken (\prismadreieck g/h/l, \quader, \netzquader, \netzzylinder)
gegen die Aufgabenwerte gehalten. `werkzeuge/bank-pruef.py koerper`:
0 Abweichungen, 0 Warnungen.

## Befunde

e2-k1-s0-v1, e2-k1-s0-v2, e2-k1-s0-v3, e2-k1-s0-v4: [A] Der Artikel vor
den Kästchen verrät die Lösung („Gefragt ist das …“ → Volumen, „Gefragt
ist die …“ → Oberfläche); die Vorstufe prüft damit Grammatik statt
Inhalt/Hülle – Satz ohne Artikel: „Was ist gefragt?“ oder „Gefragt ist:“.

e2-k1-s8-v4: [E] „Terrarium mit Wasserteil“: Wasser steht nur in einem
Teil, die Frage „Wie viele Liter Wasser passen hinein?“ rechnet aber mit
dem ganzen Innenraum – Kontext „Aquarium“ oder „Wasserbecken“ nehmen.

e3-k1-s8-v1, e3-k1-s8-v2, e3-k1-s8-v3: [E] Der Text spricht von einem
schon gezeichneten Teilnetz („sind … gezeichnet“, „Zeichne das Netz
ab“), die Grafik ist aber nur \rechenplatz; abzeichnen und ergänzen
geht nicht, die Aufgabe schrumpft auf „fehlende Fläche nennen“ –
Teilnetz als Grafik (Kästchenraster) beigeben oder Wortlaut „Zeichne
das vollständige Netz“.

e1-k3-s1-v1, e1-k3-s1-v2, e1-k3-s1-v3: [E] „Schrägbild lesen“ ohne
Schrägbild: Die Aufgabe beschreibt das Bild nur in Worten, dass die
Tiefe halb gezeichnet ist, steht nirgends, und die Zahl der
gestrichelten Kanten ist ohne Bild eine Wissensfrage – \quader-Grafik
mit beschrifteter Vorder- und Schrägkante beigeben.

e5-k1-s4-v3: [M] Merkmal „auf die Klammer achten“, aber keine der drei
Optionen enthält eine Klammer; die Ablenker prüfen nur „halb“ und
„Radius statt Durchmesser“ – einen Ablenker mit fehlender oder falsch
gesetzter Klammer aufnehmen (etwa $(6 \cdot 4 + \tfrac{1}{2} \cdot \pi
\cdot 2^2) \cdot 3$).

e5-k1-s7-v3: [E] Die Ausrichtung ist nur für die Bücher entlang der
65 cm genannt, nicht „alle gleich ausgerichtet“ wie in v1; im
Reststreifen 65 − 46 = 19 cm passen gedreht (15 cm entlang der 65 cm,
23 cm entlang der 35 cm) noch 11 Bücher, zusammen 55 statt 44 –
„alle gleich ausgerichtet“ ergänzen.

Sauber: 277 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k1-s0-v1 bis v4 – der Artikel im Lückensatz („das …“ /
„die …“) verrät die richtige Option; beide schlagen einen Fragesatz ohne
Artikel vor.

Nur Erstleser: keiner (der Zusatz des Erstlesers, die zwei Optionen je
in eine eigene Zeile zu setzen, ist kein eigener Befund; die Vorlage
verlangt eigene Zeilen erst ab drei Kästchen oder langen Aussagen).

Nur Zweitleser: e2-k1-s8-v4 – „Terrarium mit Wasserteil“ passt nicht
zur Frage nach dem ganzen Innenraum als Wasser. e3-k1-s8-v1 bis v3 –
der Text verweist auf ein gezeichnetes Teilnetz, das in der Grafik
fehlt. e1-k3-s1-v1 bis v3 – „Schrägbild lesen“ ohne Schrägbild. e5-k1-
s4-v3 – Merkmal „Klammer“ wird von keiner Option geprüft. e5-k1-s7-v3 –
ohne „alle gleich ausgerichtet“ passen mit gedrehten Büchern 55 statt 44.

Widersprüche: keine (der Erstleser nennt keine rechnerische Abweichung,
der Zweitleser auch nicht; die Netzprüfungen beider stimmen überein).

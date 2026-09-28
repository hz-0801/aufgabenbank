# Zweitlesung pyramide-kegel-kugel

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 246
(zone 48, e1 77, e2 63, e3 58)

Prüfung: Jede Zeile einzeln gelesen (Aufgabe, Antwortgerüst, Lösung,
pruef, Grafik, Lösungsgrafik, Original) und die Lösung aus dem
Aufgabentext neu gerechnet – Kugelteil (Volumen, Oberfläche,
Halbkugel, Masse, Radius aus O, Würfelschachtel, zusammengesetzte
Körper, Prüfungshöhe, Fehler finden, Anwendung) mit sympy (exakte
Brüche, π symbolisch), Pyramide und Kegel mit Nebenrechnung einzeln
(Stützdreiecke, Mantel, Oberfläche, Kegeldach mit Kosten und
Gesamthöhe, Umkehrungen, Faktoraussagen (6r)² und (1,5r)²). Alle 193
Zeilen mit pruef-Zahl stimmen mit der eigenen Rechnung und der
gerundeten Lösung überein; auch die übrigen 53 (Begründen, Zeichnen,
Ankreuzen ohne Zahl) sind inhaltlich richtig. Die 20
Ankreuz-Zeilen haben genau eine richtige Option, die Lösung nennt
sie wortgleich. Die 10 Fehler-finden-Zeilen (Zone 1, je Einheit 3)
enthalten einen echten Fehler aus „Typische Fehler“, die vorgegebene
Falschrechnung ist in sich richtig gerechnet, die Richtigrechnung
stimmt. Die Proportionen der Grafiken passen zu den Werten (Netz- und
Schrägbildmaße, Kegel mit h = √65 bzw. √32 als Lösungsgrafik).
`werkzeuge/bank-pruef.py pyramide-kegel-kugel`: 0 Abweichungen,
0 Warnungen. Rechnerisch ist nichts falsch; die Befunde betreffen
Eindeutigkeit und Merkmal.

## Befunde

e1-k6-s3-v2: [E] Text sagt nur „Die Pyramide hat die Seitenhöhe
7 cm“; dass die Grundfläche quadratisch ist, muss der Schüler aus dem
Schrägbild schließen, in dem nur eine Grundkante (5 cm) steht – das
Netz (Quadrat mit vier gleichen Dreiecken) folgt so nicht sicher. –
„Die quadratische Pyramide hat …“ schreiben.

e2-k2-s10-v1, e2-k2-s10-v2, e2-k2-s10-v3: [M] Sprosse „Netz erkennen
und beschriften“, aber es gibt kein Netz zu sehen und nichts zu
beschriften; die Aufgabe nennt r und s und fragt sie als Radien von
Kreis und Kreisausschnitt zurück (Lösung = gegebene Zahlen). – Netz
als Grafik zeigen und die Radien eintragen lassen; einen
Kegelnetz-Baustein gibt es in mappen/_bausteine.md nicht, daher als
Befund in stand.md aufnehmen.

e2-k2-s10-v2, e2-k2-s10-v3: [E] Partyhütchen und Schultüte sind
unten offen; „Sein Netz besteht aus einem Kreis und einem
Kreisausschnitt“ stimmt für diese Gegenstände nicht (nur der
Kreisausschnitt). Bei v3 zudem „Sein Netz“ statt „Ihr Netz“
(die Schultüte). – Geschlossenen Kegel als Kontext wählen („ein
Kegel aus Pappe“, „ein Modellkegel“) oder vom Kegel mit dem Maß
des Hütchens sprechen.

e2-k2-s13-v1: [E] „Wie oft passt der Kegel in den Zylinder?“ –
körperlich passt ein Kegel nur einmal hinein; gemeint ist das
Umfüllen. – Wie v2/v3: „Wie oft musst du den Kegel füllen, bis der
Zylinder voll ist?“

e2-k3-s3-v1: [E] Aufgabe verlangt die Waffeltüte „mit der Spitze
unten“; die Lösungsgrafik \kegel{1.25}{2.75}{…} zeichnet einen
Kegel mit der Spitze oben (der Baustein kennt keine Lage) und im
falschen Verhältnis (2,5 : 11 wäre 1.25 : 5.5). – Lösungsgrafik
weglassen (die Lösung beschreibt die Skizze) oder mit
\kegel{1.25}{5.5}{…} und Hinweis „Spitze unten“ in der Lösung.

e3-k2-s3-v3: [E] Text: „Eine Eiskugel … sitzt zur Hälfte in einer
Waffeltüte“ – also untere Halbkugel in der Tüte; die Lösung zeichnet
aber „darauf eine Halbkugel“ (Halbkugel auf dem Tütenrand). Beides
widerspricht sich, und eine Kugel mit dem Randradius kann nicht zur
Hälfte im Kegel stecken. – „Auf der Tüte sitzt eine Halbkugel Eis
mit dem Radius 2 cm“ schreiben.

Sauber: 239 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k6-s3-v2 – „quadratisch“ fehlt im Text, das Netz
folgt nur aus der Grafik. e2-k2-s10-v3 – „Sein Netz“ statt „Ihr
Netz“ (der Zweitleser rügt dazu den Kontext, siehe unten).

Nur Erstleser:
- e1-k1-s0-v3 (Globus, „färbe die Grundfläche“): bestätigt, aber nur
  als Formulierungsfrage – die Kugel hat keine Grundfläche, der
  Auftrag ist so nicht erfüllbar; die Lösung fängt das ab, „falls es
  eine gibt“ in allen vier Varianten macht es sauber.
- e3-k1-s13-v3 (Boule-Kugel): bestätigt – Pétanque-Kugeln sind hohl
  (rund 71–80 mm Durchmesser), 700 g : 7,85 ≈ 89,2 cm³ ist nur das
  Stahlvolumen; als „Volumen der Kugel“ sachlich falsch. Massive
  Kugel als Kontext wählen. Vom Zweitleser übersehen.
- e1-k5-s13-v2 (Zeltdach mit Dachhöhe statt Seitenhöhe): bestätigt –
  die Variante braucht einen Stützdreieck-Schritt, den v1 und v3
  nicht haben; damit ändert sie mehr als Zahlen und Kontext
  (bank.md, Regeln für den Inhalt). Vom Zweitleser gesehen, aber zu
  Unrecht als vom Merkmal gedeckt gewertet.
- e1-k6-s2-v2 (Seitenhöhe länger als Höhe): bestätigt – der
  Sprossentext nennt als Begründung nur das Drittel; die Variante
  begründet etwas anderes (Hypotenuse im Stützdreieck). Inhaltlich
  richtig, aber außerhalb der Sprosse.
- e2-k2-s8-v2 (Oberfläche 320,4 gegen gezeigte Zwischenwerte
  113,10 + 207,35 = 320,45 → 320,5): bestätigt – kleiner
  Schreibform-Befund, die Endzahl aus ungerundeten Werten ist
  richtig; Zwischenwerte mit drei Stellen oder beide Werte zulassen.
- e2-k2-s12-v1, v2, v3 (Kosten aus ungerundetem M, eurogenau):
  bestätigt als Schreibform – mit dem gezeigten M weicht der Betrag
  um 1–2 € ab; Kosten auf Zehner runden, wie der Erstleser
  vorschlägt, passt auch zur „sinnvollen Genauigkeit“ der Mappe.

Nur Zweitleser:
- e2-k2-s10-v1, v2, v3 [M]: kein Netz zu erkennen oder zu
  beschriften, die Aufgabe fragt nur die gegebenen Radien zurück.
- e2-k2-s10-v2, v3 [E]: Partyhütchen und Schultüte sind unten offen,
  ihr Netz hat keinen Grundkreis.
- e2-k2-s13-v1 [E]: „Wie oft passt der Kegel in den Zylinder?“ statt
  „füllen“ wie in v2/v3.
- e2-k3-s3-v1 [E]: Lösungsgrafik mit der Spitze oben und im falschen
  Verhältnis, die Aufgabe verlangt die Spitze unten.
- e3-k2-s3-v3 [E]: „zur Hälfte in der Tüte“ widerspricht der Lösung
  „darauf eine Halbkugel“.

Widersprüche: keine – der Erstleser wertet den Darstellungswechsel
in beide Richtungen und die Aufteilung der Prüfungshöhen auf zwei
Originale als gedeckt, der Zweitleser ebenso; bei e1-k5-s13-v2
folgt der Zweitleser nach Prüfung dem Erstleser.

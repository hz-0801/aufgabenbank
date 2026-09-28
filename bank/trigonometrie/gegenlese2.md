# Zweitlesung trigonometrie

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 342
(zone 38, e1 91, e2 63, e3 78, e4 72)

Prüfung: Jede Zeile gelesen und die Lösung aus dem Aufgabentext selbst
aufgestellt (Funktion bzw. Sinussatz/Kosinussatz, Lage der gesuchten
Größe, Teilwinkel, Zusatzhöhen); jeder pruef-Ausdruck mit diesem
eigenen Ansatz verglichen, Grenzfälle der Rundung (z. B. 33,749°,
34,850°, 7,505 m, 455,64 m, 248,45 m, 214,46 m) mit sympy nachgerechnet.
Alle Zeilen mit pruef-Zahl stimmen mit der eigenen Rechnung und der
Rundung der Lösung überein. Jede \dreieck-Grafik (35) über die
Koordinaten auf Lage des rechten Winkels und Zuordnung der Seiten
(a = BC, b = CA, c = AB) geprüft, dazu die Beschriftungen H/G/A, die
Brüche der Basisaufgaben und die drei ksys-Ablesegrafiken; alle
passen zum Text. 30 Ankreuzzeilen: jeweils genau eine Option richtig,
loesung wortgleich (auch die drei Gleichungsoptionen in e1-k3-s2 je
einzeln geprüft). 13 Fehler-finden-Zeilen: eingebauter Fehler
rechnerisch nachvollzogen (auch der RAD-Wert −6,8 und die
Nebenwinkel-Summe 105°), Richtigrechnung stimmt. bank-pruef.py:
0 Abweichungen, 0 Warnungen. Hinweis ohne Befund: gleiche Zahlen in
verschiedenen Sprossen (e2-k1-s1-v4 und e2-k1-s10-v2 beide 7 und 10;
e2-k1-s3-v1 und e3-k1-s4-v1 beide tan α = 5/8) – Aufgabentexte
verschieden, daher keine Dublette nach bank.md.

## Befunde

e1-k3-s16-v7, e1-k3-s16-v8: [E] Text sagt „die Höhe von C auf AB ist
eingezeichnet“, die Grafik (\dreieck) zeigt keine Höhe und keinen
Fußpunkt; bei v7 ist zudem der als 57° beschriftete Winkel bei B mit
etwa 50° gezeichnet – „eingezeichnet“ streichen und die Höhe im Text
benennen (Fußpunkt H), oder die Grafik weglassen, da alle Werte im
Text stehen.

e1-k7-s3-v3: [M] Merkmal „Entscheidung im Sachkontext“, die Aufgabe
fragt nur die Höhe des Drachens ab (eingekleidete Rechnung) –
Entscheidungsfrage ergänzen, etwa „Fliegt er über einen 38 m hohen
Mast?“.

e3-k1-s9-v1: [E] „Wie hoch ist es?“ passt nicht zu „Kirchturm“ (der
Bezug bleibt unklar) – „Wie hoch ist der Kirchturm?“.

e3-k1-s9-v3: [E] „Höhenwinkel zur Spitze eines Windrads bis zur Nabe“
ist widersprüchlich, und „Wie hoch ist es?“ lässt offen, ob Nabe oder
Flügelspitze gemeint ist – „Höhenwinkel zur Nabe eines Windrads … Wie
hoch liegt die Nabe?“.

e3-k1-s17-v1: [E] „ein 9 m hoher Aussichtsplattform – … seine
Oberkante“ grammatisch falsch – „eine 9 m hohe Aussichtsplattform –
… ihre Oberkante“.

e3-k3-s3-v3: [M] sprosse_text verlangt Vermessung (Höhe aus Abstand
und Höhenwinkel, Gerätehöhe oder Sockel addieren); die Sparrenlänge
am Satteldach ist keine Vermessung (v2 trägt mit Winkel und Sockel
noch den Kern) – durch eine Vermessungsaufgabe mit Entscheidung
ersetzen.

Sauber: 335 Zeilen ohne Befund

## Abgleich

Beide Leser:
- e1-k3-s16-v7, e1-k3-s16-v8: „Höhe eingezeichnet“, die Grafik zeigt
  keine Höhe; in v7 ist der 57°-Winkel bei B mit etwa 50° gezeichnet.
- e1-k7-s3-v3: Anwendungszeile ohne Entscheidung, eingekleidete
  Rechnung.
- e3-k1-s9-v1: „Wie hoch ist es?“ passt nicht zum Kirchturm.
- e3-k1-s9-v3: „Spitze eines Windrads bis zur Nabe“ unklar, Frage
  offen zwischen Nabe und Flügelspitze.
- e3-k1-s17-v1: „ein 9 m hoher Aussichtsplattform – seine Oberkante“
  grammatisch falsch.
- e3-k3-s3-v3: Sparrenlänge am Satteldach ist keine Vermessung nach
  sprosse_text.

Nur Erstleser:
- e4-k1-s0-v1 (Ankreuzen): bestätigt – mit β = 90° gilt der Sinussatz
  ebenfalls (b = a · sin 90° : sin α), die Option „Sinussatz“ ist
  mathematisch auch richtig; die Frage braucht „am einfachsten“ oder
  eine andere Option. Diesen Sonderfall habe ich übersehen.
- e2-k1-s0-v1 bis v4: bestätigt – der Text nennt das Gesuchte schon
  („Gesucht: der Winkel α“), die Frage „Was ist gesucht?“ ist damit
  beantwortet; eine Skizze mit Fragezeichen oder die Frage „Wie
  rechnest du?“ ohne Benennung des Gesuchten.
- e4-k2-s2-v2: bestätigt – sprosse_text verlangt die Begründung, warum
  der Sinussatz gilt (Höhe als gemeinsame Kathete); „warum ein
  vollständiges Paar nötig ist“ begründet etwas anderes.
- zone-f7-v4: bestätigt – 180° − 124° − 31° legt keinen Nebenwinkel
  nahe, der Fallstrick ist nicht angelegt.
- e3-k3-s3-v2: bestätigt – Drehleiter rechnet mit dem Sinus aus der
  Länge statt aus Abstand und Höhenwinkel; ich hatte die Zeile als
  Grenzfall stehen lassen, das Urteil des Erstlesers ist genauer.
- e2-k1-s1-v2, e2-k1-s11-v5: bestätigt – mit den gezeigten gerundeten
  Zwischenwerten ergibt die Umkehrtaste 33,75° ≈ 33,8° bzw.
  69,76° ≈ 69,8° (nachgerechnet); die Lösung soll den Bruch in die
  Umkehrtaste geben oder beide Werte zulassen.
- e3-k1-s12-v2, e3-k1-s17-v5, e3-k1-s17-v6: bestätigt – mit h ≈ 4,79,
  BF ≈ 63,0 und BF ≈ 46,8 ergeben sich 6,5 cm, 115,7 cm und 99,7 cm
  (nachgerechnet); Vermerk „mit ungerundetem Zwischenwert“ und
  Toleranz in der Lösung.
- e3-k1-s14-v1 bis v3 (Buchstaben G, A im Gerüst): bestätigt – in e3
  steht A zugleich für die Ecke A und in s15 für den Flächeninhalt;
  „ein Buchstabe je Einheit für eine Sache“ ist verletzt, Gerüst mit
  ausgeschriebenen Wörtern.
- Rundungsstellen ohne Angabe (e1-k3-s16-v5, v6; e2-k1-s11-v11, v12;
  e3-k1-s14-v1 bis v3; e3-k1-s17-v9, v10): nicht als Befund
  bestätigt – die Aufgaben sind eindeutig lösbar, die Stellen folgen
  dem Original (1,72 m; 502 m) oder dem Zweck (zwei Stellen für die
  Pythagoras-Probe); eine Stellenangabe in der Aufgabe wäre ein
  Gewinn, aber kein Fehler.
- e2-k1-s10-v1 (bereits korrigiert): im jetzigen Stand richtig
  (49,46° → rund 49°), kein Befund.

Nur Zweitleser: keine – alle meine Befunde hat auch der Erstleser.

Widersprüche: keine in der Sache; bei e3-k3-s3-v2 hatte ich die Zeile
ausdrücklich ohne Befund gelassen, der Erstleser beanstandet sie – nach
Prüfung schließe ich mich ihm an. Die Rundungsstellen wertet der
Erstleser als Befund, ich nur als Hinweis.

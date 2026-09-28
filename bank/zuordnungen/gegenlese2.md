# Zweitlesung zuordnungen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 260
(zone 23, e1 64, e2 60, e3 38, e4 75)

Prüfung: Jede Zeile gelesen. 190 Zeilen tragen eine pruef-Angabe. Davon
wurden 148 Zahlenergebnisse aus dem Aufgabentext eigens nachgerechnet
(Skript mit sympy-Rationals, unabhängig vom Feld pruef), alle 148 stimmen
mit pruef und loesung überein, Rundung eingeschlossen (8,3 min). Die
übrigen 42 sind Punktlisten (Zeichnen, Tabelle, Ablesen); sie wurden von
Hand gegen Tabelle, Geradenaufruf bzw. Funktionsterm der Grafik und den
Achsenbereich geprüft. Die Grafiken wurden gegen die Makrodefinition in
mathblatt.sty gelesen (ksys: ein Kästchen = xstep bzw. ystep). 40
Ankreuzzeilen wurden Option für Option geprüft, 16 Fehler-finden-Zeilen
auf den eingebauten Fehler und die Richtigrechnung. Ergebnis von
`werkzeuge/bank-pruef.py zuordnungen`: 0 Abweichungen, 1 Warnung (e4 k3 s5
hat 8 Zeilen statt 3, weil dort vier Originale verfremdet werden – eine
Mengenfrage, kein Inhaltsbefund).

## Befunde

zone-f4-v4: [M] Das Merkmal nennt einen Fallstrick („geteilt, nicht mal
gerechnet“), die Aufgabe „Ein Drittel von 15 kg“ ist aber baugleich mit
dem Grundfall v2 („Ein Viertel von 20 m“) und fordert den Fallstrick
nicht heraus – eine Form wählen, bei der das Malnehmen naheliegt (z. B.
„ein Drittel von 15 kg – rechnest du 15 · 3 oder 15 : 3?“ oder
Bruchteil als „\frac13 · 15 kg“).

e1-k1-s5-v1: [E] Ein Eimer ist meist oben weiter; bei gleichmäßigem
Zufluss steigt die Füllhöhe dann nicht linear, die „richtige“ Option
„steigende Gerade durch den Ursprung“ gilt nur für ein zylindrisches
Gefäß – „ein zylindrischer Eimer“ oder „eine gerade Regentonne“ schreiben.

e1-k1-s7-v1, e1-k1-s7-v2: [E] Text und Grafik widersprechen sich: die
Aufgabe sagt „ein Kästchen steht für 10“, die Grafik hat ystep=50, also
ist ein Kästchen 50 wert (Gitter und Zahlen je 50). – Entweder den Satz
auf „ein Kästchen steht für 50; Werte dazwischen schätzen“ ändern (passt
zum Merkmal und zur Falle des Originals 2025-OS-K7a) oder ystep=10 setzen
und den Satz über die Beschriftung streichen.

e1-k2-s1-v3: [A] Nach dem Kriterium der Sprosse („passt der größte Wert
ins Raster?“) passen beide Optionen: 9 l passen auch bei 10 l je Kästchen
aufs Raster; die Lösung wechselt stillschweigend zum Kriterium
„sinnvoll ausnutzen“. – Zweite Option durch eine nicht passende ersetzen,
z. B. „1 Kästchen = 0,25 l“ (36 Kästchen).

e1-k4-s1-v2: [M] Die Sprosse heißt „Fehler finden (Achsen vertauscht,
Punkt falsch gesetzt)“; Bens Fehler (Formel additiv y = x + 4 aus nur
einem Wertepaar) gehört zu keinem der beiden genannten Muster (v1 und v3,
Skala als Kästchen gelesen, sind als „Punkt falsch abgelesen“ noch
vertretbar). – Durch einen falsch gesetzten Punkt ersetzen oder die
Formelaufgabe in die Kette „Formel aus Tabelle“ verschieben.

e2-k1-s0-v2, e2-k1-s0-v4: [E] Ohne gesuchte Größe ist „Was ist hier eine
Portion?“ bei einer Rate doppeldeutig: beim Drucker kann eine Minute oder
eine Seite, beim Auto eine Stunde oder ein Kilometer die Portion sein,
je nachdem, was gefragt wird. – Frage mitgeben („… Wie viele Seiten in
7 Minuten? Was ist hier eine Portion?“) oder Lösung mit beiden Lesarten.

e3-k2-s1-v3: [E] Der Kontext trägt nicht: eine Fahrt dauert nicht kürzer,
weil mehr Boote fahren; „Anzahl Boote → Zeit“ ist ohne weitere Angabe
(z. B. Transport einer festen Ladung in mehreren Fahrten) nicht
antiproportional. – Kontext ändern, etwa „Anzahl Boote → Zeit, um 180
Kisten überzusetzen“, oder Pumpen/Helfer/Maschinen nehmen.

e3-k3-s2-v3: [M] Die Sprosse verlangt den Grund für das gleichbleibende
Produkt; v3 fragt nach dem fehlenden Wert bei null Arbeitern – anderes
Thema (Definitionsbereich). – Durch eine Frage zum Produkt ersetzen (z. B.
Kinder teilen Bonbons: warum bleibt Anzahl · Stück je Kind gleich?).

e3-k3-s3-v1: [E] Die Aufgabe verlangt, die Punkte „Anzahl Kinder → Stück
je Kind“ zu einer Kurve zu verbinden; e1-k1-s4 lehrt ausdrücklich, dass
Punkte bei Anzahlen (Kinokarten, Busse) nicht verbunden werden dürfen. –
Nur Punkte eintragen lassen und die Kurve gestrichelt als Hilfslinie
nennen, oder eine stetige Größe nehmen (Geschwindigkeit → Fahrzeit).

Sauber: 249 Zeilen ohne Befund

## Abgleich

Beide Leser:
- zone-f4-v4: Fallstrick-Variante baugleich mit dem Grundfall, lockt das Malnehmen nicht hervor.
- e1-k1-s5-v1: Eimer ist nicht zylindrisch, die Gerade gilt nur für senkrechte Wände.
- e1-k1-s7-v1, e1-k1-s7-v2: ystep=50 widerspricht „ein Kästchen steht für 10“; der Erstleser vermutet es, mathblatt.sty bestätigt es (Gitter = ystep).
- e1-k2-s1-v3: beide Einteilungen passen nach dem Kriterium der Sprosse, die Lösung wechselt das Kriterium.
- e1-k4-s1-v2: Formelfehler (additiv) ist nicht das Muster des Sprossentexts.
- e2-k1-s0-v2, e2-k1-s0-v4: ohne Zielfrage ist die Portion bei einer Rate doppeldeutig.
- e3-k2-s1-v3: Anzahl Boote → Fahrzeit trägt ohne Ladung nicht.
- e3-k3-s2-v3: fragt nach dem Nullwert statt nach dem gleichbleibenden Produkt.
- e3-k3-s3-v1: Punkte einer Anzahl-Zuordnung sollen verbunden werden.

Nur Erstleser:
- e2-k8-s2-v3 (Lösung): bestätigt – „jede Rechnung, die links und rechts gleich ist, führt zum Ziel“ ist falsch (links und rechts „+ 3“) und widerspricht e2-k8-s2-v2; von mir übersehen.
- e4-k3-s5-v7 (eindeutig): bestätigt – „10 s nach dem Start in 150 m Höhe“ und „fährt gleichmäßig“ mit 4 m/s widersprechen sich, wenn der Aufzug am Boden startet (15 m/s); die Starthöhe fehlt, 310 : 50 ist eine Lesart. Beim Original rechtfertigt der Freifall vor dem Öffnen die andere Geschwindigkeit, beim Aufzug nicht; von mir übersehen.
- e1-k4-s1-v1, e1-k4-s1-v3 (Fehler finden): bestätigt – bank.md verlangt das Muster aus „Typische Fehler“; „Kästchen gezählt statt Skalenwert“ steht dort nicht und ist auch nicht das Muster des Sprossentexts. Ich hatte beide in der Befundliste als „Punkt falsch abgelesen“ noch für vertretbar gehalten.
- e3-k1-s6-v1 (Verfremdung): bestätigt – Futtervorrat für Ziegen statt für Pferde ist derselbe Kontext; bank.md verlangt einen anderen.
- e4-k2-s1-v3 (periodischer Quotient): bestätigt, leicht – 2 : 3 = 0,6… ohne Hinweis verstößt gegen die Regel für periodische Dezimalbrüche, auch wenn die Lösung „zwei Drittel“ schreibt.
- e4-k2-s0-v3 (Ankreuzen): bestätigt, leicht – bei Kindern ist „mehr“ vertretbar, und e4-k4-s1-v1 nutzt Alter → Größe selbst als „je mehr, desto mehr“; ein Kontext ohne jeden Zusammenhang ist sauberer.
- e1-k4-s2-v1 (eindeutig): bestätigt als Schärfung – über mehrere Tage wäre „ja“ vertretbar; „Messreihe an einem Tag“ zu ergänzen kostet nichts.
- e3-k1-s6-v2 (Schreibform „Wandertage“): bestätigt – gemeint sind Wanderertage.
- e2-k4-s7-v2 (Merkmal): nicht bestätigt – die Prüfungshöhe verlangt einen nicht ganzzahligen Wert je Portion ohne Taschenrechner; 5,70 : 3 = 1,90 erfüllt das, ganzzahlige Ausgangswerte fordert der Sprossentext nicht.
- e3-k1-s5-v3 (Merkmal): nicht bestätigt – Varianten dürfen sich in den Zahlen unterscheiden; 42 : 5 = 8,40 € geht im Kopf, ein zweites Merkmal entsteht dadurch nicht.
- e4-k5-s3-v3 (doppelt): nicht bestätigt – dieselbe Gerade y = x + 2 wie in e4-k2-s4-v3, aber anderer Auftrag (Wertepaare ablesen und Quotienten prüfen statt Typ ankreuzen), andere Form und anderer Achsenbereich; keine doppelte Aufgabe, eine andere Gerade wäre nur schöner.

Nur Zweitleser: keine.

Widersprüche: keine in der Sache. Unterschiedlich gewichtet: e1-k4-s1-v1 und v3 (in meiner Befundliste vertretbar, nach Prüfung gegen bank.md folge ich dem Erstleser); e2-k4-s7-v2, e3-k1-s5-v3 und e4-k5-s3-v3 hält der Erstleser für Befunde, ich nicht (Gründe oben).

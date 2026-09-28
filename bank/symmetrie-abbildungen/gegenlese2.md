# Zweitlesung symmetrie-abbildungen

Datum: 2026-09-28 · Modell: claude-opus-5-5
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 225
(zone 30, e1 54, e2 87, e3 54)

Prüfung: Jede Zeile gelesen, Aufgabe gegen Grafik, loesung, pruef,
sprosse_text und merkmal gehalten. Alle Abbildungsaufgaben mit
Koordinaten (Spiegeln an senkrechter, waagerechter, schräger Achse
und an den Koordinatenachsen, halbe Figur ergänzen, Verschieben mit
Pfeil, Verschiebung beschreiben, halbe Drehung, Vierteldrehung,
Punktspiegelung von Punkt und Figur; zusammen 40 Zeilen) mit einem
Skript aus den \punkt-Aufrufen der Grafik nachgerechnet – alle 40
stimmen mit pruef und loesung überein; Seitenlängen der
\dreieck-Grafiken mit sympy (gleichschenklig/gleichseitig/
ungleichseitig), Bandornamente, Kontextzahlen (Riesenrad, Fliesen,
Uhr, Lageplan, Seekarte, Stadtplan, Drachen, Beet) und die übrigen
pruef-Zahlen von Hand nachgerechnet; alle pruef-Zahlen stimmen mit der
Lösung. 36 Ankreuzzeilen geprüft: jeweils genau eine Option richtig,
loesung nennt sie wortgleich. 10 Fehler-finden-Zeilen (zone-Paar,
je 3 in e1–e3): eingebauter Fehler jeweils wirklich falsch,
Richtigstellung stimmt. bank-pruef.py symmetrie-abbildungen:
0 Abweichungen, 0 Warnungen.

## Befunde

e2-k2-s4-v3: [E] Der Text sagt „Dreieck mit drei verschieden langen
Seiten“, die Grafik \dreieck{(0,0)}{(5,0)}{(1,3)} hat aber AB = BC = 5
(gleichschenklig, eine Achse) – Bild und Lösung „0“ widersprechen
sich. – Dritte Ecke verlegen, z. B. (1.5,3) (Seiten 5; 3,35; 4,61).

e2-k2-s6-v1, e2-k2-s6-v2: [M] Die Sprosse „Dreiecksarten prüfen“
stellt nur Fragen, die in derselben Kette schon stehen: v1 („Wie viele
Symmetrieachsen hat ein gleichseitiges Dreieck?“, 3) ist wortgleich
bis auf den Artikel mit e2-k2-s3-v3, v2 (gleichschenklig, nicht
gleichseitig, 1) wiederholt e2-k2-s0-v4 und e2-k2-s2-v3 – „keine Aufgabe
doppelt“, und die Sprosse ändert gegenüber den Vorgängern nichts. –
Dreiecksarten als Vergleich stellen (etwa ungleichseitig,
gleichschenklig, gleichseitig in einer Tabelle zuordnen, wie s5 für
Vierecke) oder eine noch nicht vorkommende Art (stumpfwinklig-
gleichschenklig) nehmen; s3-v3 dann durch eine Viereckfigur ersetzen.

Sauber: 222 Zeilen ohne Befund

## Abgleich

Beide Leser: e2-k2-s4-v3 – die Grafik zeigt ein gleichschenkliges
Dreieck (AB = BC = 5), der Text verlangt ein ungleichseitiges, beide
schlagen C auf (1.5,3) vor. Die Doppelung gleichseitiges Dreieck
zwischen e2-k2-s3-v3 und e2-k2-s6-v1 haben beide gesehen (Erstleser
unter s3-v3, Zweitleser unter s6-v1).

Nur Erstleser:
- zone-f6-v2: bestätigt – am mathblatt.sty nachgesehen, \dreieckrw
  zeichnet das Winkelzeichen bei C selbst, die Aufgabe ist vorgelöst;
  von mir übersehen, weil ich den Baustein nicht am Quelltext geprüft
  hatte.
- e2-k2-s10-v1, e2-k2-s10-v2: bestätigt – \drachen ruft \viereck mit A
  unten, C oben auf, die lange senkrechte Diagonale heißt also AC, der
  Text gibt AC als die kurze an; e, f stehen unerklärt dabei.
- e2-k3-s6-v3: bestätigt – C(2|8) liegt auf ymax, die Beschriftung
  oben rechts fällt aus dem Bereich; Rechnung selbst stimmt.
- e2-k3-s8-v1: bestätigt – ohne Angabe der Winkel an a kann ein
  Dreieck (rechter Winkel an a) oder ein konkaves Viereck entstehen;
  Lösung „Drachenviereck“ ist nur für spitze Winkel an a eindeutig.
- e3-k1-s9-v1: bestätigt – das Parallelogramm ist punktsymmetrisch,
  dasselbe Parkett entsteht auch durch halbe Drehungen um
  Seitenmitten; die Frage hat mehr als eine richtige Antwort.
- e3-k1-s9-v2: bestätigt – welche Abbildung zum Nachbarn führt,
  hängt vom gelegten Parkett ab; Lösung ist nur ein Beispiel.
- zone-f3-v4: bestätigt mit Einschränkung – die Zeile unterscheidet
  sich von f3-v3 nur durch die Zahl und einen Hinweissatz; die Falle
  „falsche Richtung“ wird nicht gezielt ausgelöst.
- e2-k2-s0-v1, e2-k2-s0-v2: bestätigt – beide Faltungszeilen haben
  „ja“, der Nein-Fall der Vorstufe fehlt.
- e2-k2-s1-v1: teilweise bestätigt – keine Doppelung im Sinne von
  bank.md (andere Aufgabe), aber dieselbe Figur steht in der Vorstufe
  mit eingezeichneter Achse; andere Maße sind billig und besser.
- e2-k2-s1-v3: bestätigt – gleiche Grafik \trapez{5}{3}{2.5} und
  gleicher Handgriff wie e2-k1-s0-v4.
- e1-k5-s1-v2, e1-k5-s1-v3, e1-k6-s4-v3: nachvollziehbar, nicht
  zwingend – die Rechnung stimmt; die Schreibform „5 − (−2)“ setzt
  Subtraktion negativer Zahlen voraus, die der Typ „abzählen“ nicht
  braucht; Abzählen über die Achse ist die passendere Lösungsform.
- zone-f2-v4: teilweise bestätigt – die richtige Option ist eindeutig
  (kein Ankreuzfehler), aber die Ablenker treffen den Fallstrick
  „schräge Strecke“ nicht.

Nur Zweitleser: e2-k2-s6-v2 wiederholt die Frage nach dem
gleichschenkligen Dreieck aus e2-k2-s0-v4 und e2-k2-s2-v3, sodass die
Sprosse „Dreiecksarten prüfen“ nichts Neues bringt.

Widersprüche: keine in der Sache; beim Doppel gleichseitiges Dreieck
unterscheidet sich nur der Vorschlag – der Erstleser ersetzt
e2-k2-s3-v3 und lässt s6 stehen, der Zweitleser baut s6 um; beides
löst die Doppelung, der Weg des Erstlesers ist kleiner, solange
e2-k2-s6-v2 zusätzlich geändert wird.

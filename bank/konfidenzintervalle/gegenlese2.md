# Zweitlesung konfidenzintervalle

Datum: 2026-09-28 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 98 (zone 26, e1 27,
e2 27, e3 18)

Prüfung: Jede Zeile gelesen; jede Lösung unabhängig nachgerechnet
(Wilson-Grenzen aus der Grenzgleichung mit p unter der Wurzel für
alle 22 Intervalle, die bequeme Rechnung mit h unter der Wurzel für
die Fehler- und Bildaufgaben, Rückwärtsrechnung h aus einer Grenze,
Schwellen für n, Punkt- und Summenwahrscheinlichkeiten der
Binomialverteilung, Sigma-Grenzen, quadratische und
Wurzelgleichungen der Zone); die Ablesegrafiken der Zone gegen
\gerade{m}{b} gerechnet; in den drei Intervalldiagrammen (e1-k1-s3)
die Überdeckungszahl über den ganzen Zahlenstrahl gezählt – die in
der Lösung genannten Bereiche sind vollständig und richtig; die
Zuordnung der Intervallnummern in e2-k1-s3-v3/v4 mit beiden
Rechnungen (Grenzgleichung → 3 bzw. 2, bequem → 1) bestätigt.
Ankreuzen: in allen 12 Zeilen genau eine Option richtig.
Fehler finden: in allen 10 Zeilen ist der eingebaute Fehler
wirklich falsch (die falschen Ergebnisse der Schüler ergeben sich
aus dem benannten Fehler, die richtigen Werte stimmen).
`python3 werkzeuge/bank-pruef.py konfidenzintervalle`: 0
Abweichungen, 0 Warnungen.

## Befunde

e1-k1-s4-v1: „Aus 25 weiteren Stichproben" – „weiteren" hat
keinen Bezug, vorher ist keine Stichprobe genannt. – Vorschlag:
„Aus 25 Stichproben vom Umfang 400".

e2-k1-s1-v1 bis v5: Die Sprosse heißt „… berechnen und im
Diagramm zuordnen"; keine der fünf Grundfall-Zeilen hat ein
Diagramm, die Zuordnung kommt erst in der Prüfungshöhe
(e2-k1-s3-v3/v4). Rechnung und Lösung stimmen. – Vorschlag: in
zwei Varianten (v1, v4) eine zahlengerade mit drei Intervallen
anhängen und „gib seine Nummer in der Grafik an" ergänzen; oder
als Katalogbefund in stand.md, wenn der Grundfall bewusst ohne
Bild bleibt.

e2-k1-s3-v1, e2-k1-s3-v2: „genau 25 % der Drehungen" bzw. „genau
46 %" – zum Ergebnis n = 246 gehören 61,5 Treffer, zu n = 421
193,66 Treffer; einen Umfang mit genau diesem Anteil gibt es dort
nicht. Der Rechenweg (Ungleichung in n mit Anteilen) und die Zahl
sind richtig. – Vorschlag: „genau" streichen („ein Anteil von
25 %"), die Lösung bleibt.

e1-k1-s4-v3, e1-k1-s4-v4: Die Sprosse heißt „die Überdeckungszahl
als binomialverteilt begründen …"; v3/v4 verlangen das grafische
Intervall mit Beurteilung – derselbe Handgriff wie e1-k1-s2, nur
mit Kontext und Prüfkennung. Das Merkmal deckt es („grafisches
Intervall mit Beurteilung"), der Sprossentext nicht. Kein
Rechenfehler. – Vorschlag: hinnehmen (zwei Originale, eine
Sprosse) oder Sprossentext im Katalog um „; grafisches Intervall
beurteilen" ergänzen.

Sauber: 90 Zeilen ohne Befund

## Abgleich

Beide Leser: e1-k1-s4-v3/v4 (grafische Beurteilung unter der
Sprosse „Überdeckungszahl"; der Erstleser hängt sie mit Katalog
Z. 77 an s2, ich schlug hinnehmen oder Sprossentext ergänzen vor –
sein Vorschlag ist der bessere, weil der Katalog die Struktur
vorgibt). e2-k1-s3-v3/v4 sehen beide als Fremdkörper der Sprosse
„kleinster Umfang" (bei mir nur mittelbar über den Befund zu
e2-k1-s1: die Zuordnung im Bild fehlt dem Grundfall und steht
stattdessen in der Prüfungshöhe).

Nur Zweitleser: e1-k1-s4-v1 („weiteren" ohne Bezug); e2-k1-s1-v1
bis v5 (Sprosse verlangt Zuordnung im Diagramm, Grundfall hat
keins); e2-k1-s3-v1/v2 („genau 25 %" bzw. „genau 46 %" bei
Umfängen ohne ganzzahlige Trefferzahl).

Nur Erstleser: die Ablesbarkeit in e1-k1-s2-v1, e1-k1-s2-v3,
e1-k1-s4-v4 (Grenze 0,013–0,018 von der Vermutung auf Karo 0,1);
die unerklärten Symbole μ und σ in zone-f4-v1 bis v3 und
e2-k2-s1-v1 bis v3 (bank.md: Buchstaben nur, wenn erklärt);
e3-k2-s2-v3 (Sonderfall Stichprobenanteil 0,5); e2-k2-s1-v3
(Hinweis verrät die Falle, Form abweichend); e3-k1-s2-v3
(Umkehrfrage); e1-k1-s1-v4 (einzige Grundfall-Variante mit zwei
Paaren); die zu breiten Merkmale der Prüfungshöhen (e1-k1-s4-v1/v2,
e2-k1-s3-v1/v2, e3-k1-s3-v1/v2); die Aufhängung von e3-k1-s3-v3/v4
an der falschen Sprosse (Katalog Z. 79); die Pflicht-Sprossentexte
(18 Zeilen, Regel in bank.md offen). Ich habe die μ/σ-Regel und
die Katalogzeilen nicht geprüft; diese Befunde halte ich nach
Nachlesen für richtig.

Widerspruch: e2-k1-s3-v3/v4 – ich habe die Zuordnung rechnerisch
bestätigt (Grenzgleichung → Intervall 3 bzw. 2, bequeme Rechnung
→ Intervall 1) und für gut gehalten; der Erstleser sieht, dass 0,2
Prozentpunkte auf einer Zahlengeraden von 17 bzw. 18 Einheiten
nicht unterscheidbar sind – er hat recht, die Aufgabe ist so nur
mit beschrifteten Grenzen lösbar, mein „bestätigt" gilt für die
Zahlen, nicht für das Bild. e1-k1-s1-v4: ich sah die zwei Paare
als Vorgriff auf den Sprossentext („äußere Graphen zur höheren
Sicherheit") und ließ es durch; der Erstleser wertet es als
Merkmalwechsel innerhalb des Grundfalls – beides vertretbar,
seine Lösung (alle fünf mit zwei Paaren oder keine) macht die
Varianten gleichförmig.

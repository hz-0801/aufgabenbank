# Zweitlesung terme

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 203
(zone 18, e1 39, e2 81, e3 36, e4 29)

Prüfung: Alle 203 Zeilen mit einem Skript ausgegeben und einzeln
gelesen. 115 Zeilen mit Rechenauftrag im Aufgabentext („Rechne",
„Fasse zusammen", „Multipliziere", „Löse die Klammer auf",
„Klammere … aus") wurden mit sympy aus dem Aufgabentext neu
gerechnet: Gleichheit von Aufgabe und Lösung (expand/simplify),
beim Zusammenfassen und Auflösen die Gliederzahl der Lösung gegen
die des ausmultiplizierten Terms (vollständig zusammengefasst),
beim Ausklammern der herausgezogene Faktor gegen den größten
gemeinsamen Faktor. Die 9 Ankreuzaufgaben: jede Option als Term
gegen den aus dem Wortlaut aufgestellten Term geprüft, jeweils genau
eine passt, keine zwei Optionen gleichwertig. Termwerte, Sachterme,
Termbäume, Tabellen, Figuren (Seitenlängen, Dreiecksungleichung,
Zuordnung der Labels zu den gezeichneten Seiten nach
_bausteine.md), Fehler-finden-Zeilen (Fehler nicht äquivalent,
Richtigrechnung stimmt) und Begründungen von Hand nachgerechnet.
Nebenprüfung: keine doppelte Aufgabe, $-Zeichen und Klammern
überall paarig, Originale 2017-OS-B1i, 2023-OS-B1h, 2025-GYM-B2a in
der Mappe nachgesehen (Verfremdung passt). pruef: 193 Zeilen mit
Zahl, 10 ohne (Begründen, Zeichnen, Lösung ohne Ziffer).
`python3 werkzeuge/bank-pruef.py terme`: je Datei „Abweichungen 0,
Warnungen 0", gesamt „Abweichungen: 0, Warnungen: 0".

## Befunde

terme-e2-k6-s3-v2: Dreieck mit den Seiten 2a, a, 4a gibt es nicht
(2a + a = 3a < 4a, Dreiecksungleichung verletzt); die Zeichnung
(0,0),(6,0),(2,3) hat die Seiten 6 : 5 : 3,6, passt also auch nicht
zu 4 : 2 : 1 – Seiten z. B. 3a, 2a, 4a mit Zeichnung
\dreieck{(0,0)}{(4.8,0)}{(1.65,1.75)}{3a}{2a}{4a}{}{}{} (BC = 3,6,
CA = 2,4, AB = 4,8, also 3 : 2 : 4 wie die Labels), Lösung
$4a + 3a + 2a = 9a$, pruef 9.
terme-e2-k1-s0-v2: fraglich: „Unterstreiche, was zusammengehört"
bei zwei Gruppen (2a, a und 6, 8) – mit einer Unterstreichung sind
alle vier Glieder markiert, die Zuordnung ist nicht ablesbar –
entweder eine Gruppe (wie in den drei Schwesterzeilen) oder
„Verbinde/markiere mit zwei Farben".
terme-e3-k1-s0-v4: fraglich: „$2y - 6 \cdot (y + 1)$ – was steht
vor der Klammer?" hat zwei Lesarten (Faktor −6 wie in der Lösung,
oder „Minus" bzw. „die Zahl 6" nach der Dreiteilung der Sprosse
„+ oder − oder eine Zahl"); ein Schüler mit „Minus" wäre nach der
Lösung falsch – Frage schärfen („Welche Zahl wird mit der Klammer
malgenommen, mit Vorzeichen?") oder Lösung um „Minus und Faktor 6"
erweitern.

Sauber: 200 Zeilen ohne Befund

## Abgleich

- Beide Leser: terme-e2-k1-s0-v2 (zwei Gruppen beim Unterstreichen),
  terme-e2-k6-s3-v2 (Dreieck a, 2a, 4a unmöglich), terme-e3-k1-s0-v4
  (Minus und Zahl vor der Klammer zugleich).
- Nur Zweitleser: keiner.
- Nur Erstleser:
  - terme-e3-k2-s6-v1 bis v3 („Löse die Klammer auf" verlangt kein
    Zusammenfassen): Zustimmung – $5x + 2x + 12$ wäre eine richtige
    Antwort auf den Wortlaut, die Lösung nennt nur $7x + 12$.
  - terme-e3-k2-s7-v1 bis v3 (Singular, Zusammenfassen nicht
    verlangt): Zustimmung, gleicher Grund.
  - terme-e4-k1-s6-v1 bis v3 („Klammere aus" ohne „größten
    gemeinsamen Faktor"): Zustimmung – $2 \cdot (3x + 15)$ erfüllt den
    Wortlaut; ich hatte nur den ggT geprüft, nicht den Wortlaut.
  - terme-e1-k1-s7-v3, v4 (Form 2017-OS-B1i mit zwei Anweisungen unter
    einem sprosse_text, der drei Anweisungen mit Klammer nennt):
    Zustimmung als Katalogbefund für stand.md, nicht als Zeilenfehler –
    ich hatte die Mappe nachgesehen, die Verfremdung des 2017-Originals
    stimmt, und bank.md gibt 2 Zeilen je Original; der sprosse_text
    passt trotzdem nur auf v1, v2.
  - terme-e4-k1-s8-v1 bis v3 (zweite Variable erst an der
    Prüfungshöhe): teils – der Erstleser sieht ein neues Merkmal ohne
    Sprosse, ich sehe die zweite Variable als die kleinste Änderung,
    mit der ein dreigliedriger Term einen Variablenfaktor haben kann,
    ohne dass die Glieder zusammenfallen oder x³ auftritt; der
    sprosse_text („Zahl- und Variablenfaktor, dreigliedrig") erzwingt
    so eine der beiden Neuerungen. Ob eine Zwischensprosse kommt,
    entscheidet der Katalog; als Zeilenbefund halte ich es für offen.
  - terme-e3-k3-s3-v3 (dieselben Zahlen wie terme-e3-k2-s2-v2,
    $4 \cdot (\ldots + 7) = \ldots + 28$): Zustimmung – meine
    Doppelprüfung verglich nur ganze Aufgabentexte, nicht die Zahlen.
  - terme-e1-k1-s3-v2, v3 (Hauptlösung $2x + 6$ bzw. $2x + 14$ setzt
    Zusammenfassen voraus, das erst s5 einführt): Zustimmung zur
    Reihenfolge – beide Formen stehen schon in der Lösung, die
    unzusammengefasste gehört nach vorn; kein Rechenfehler.

Zahlen: Zweitleser 3 Befunde, Erstleser 10, gemeinsam 3, nur
Zweitleser 0. Gezählt: je Zeile im Befundteil (bei mir 3 Zeilen für
3 ids; in gegenlese.md die 10 Aufzählungszeilen mit ids in den
Abschnitten 2 bis 4, die 20 ids nennen; die drei Zeilen unter
„Entscheidungen" sind dort keine Befunde). Der Erstleser nennt
„Sauber: 182", nach seinen 20 ids wären es 183.

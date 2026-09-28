# Zweitlesung ebenen

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 208
(zone 30, e1 37, e2 63, e3 46, e4 32)

Prüfung: Alle 208 Zeilen einzeln gelesen (Skript gibt id,
Sprosse, Merkmal, Aufgabe, Antwort, Lösung, pruef, Grafik aus).
Die 168 Zeilen mit pruef-Wert wurden mit sympy nachgerechnet
(Verbindungsvektoren, Kreuzprodukte für Normalenvektoren,
Konstanten aus Punktproben, Parameter aus zwei Zeilen mit Probe
der dritten, Spurpunkte, Gleichungssysteme, Schrägbild-Vektoren);
Lösung und pruef stimmen überall überein. Die 21 Ankreuzzeilen:
je Option geprüft, ob sie zutrifft – überall genau eine richtig,
Lösung nennt sie wortgleich. Die 13 Fehler-finden-Zeilen: die
vorgeführte Rechnung nachvollzogen (Fehler ist jeweils echt) und
die Richtigrechnung der Lösung nachgerechnet. Nebenprüfung per
Skript: $-Zeichen und Klammern paarig, keine doppelte Aufgabe,
keine doppelte id; Grafikwerte (rpunkt, rebene, rebenepar) mit
den Aufgabenwerten verglichen und im Achsenbereich. Originale
nicht gegen die Mappe gelesen (Sperre prüft das Skript).
bank-pruef.py ebenen (lesend): 0 Abweichungen, 1 Warnung
(e2 k1 s8: 4 Zeilen statt 3, in stand.md begründet).

## Befunde

ebenen-e1-k2-s2-v3: fraglich: Lösung sagt „beide zeigen in
dieselbe Richtung“, der zweite Vektor ist aber das (−2)-Fache,
zeigt also entgegengesetzt – Vorschlag: „sind parallel (Vielfache)
und spannen nur eine Gerade auf“.

ebenen-e4-k3-s3-v1: fraglich: „Wie weit liegt sie über x = 0
senkrecht unter dem Dach?“ hat zwei Lesarten – lotrecht (Lösung:
1 m) oder als Abstand der parallelen Ebenen (3/√10 ≈ 0,95 m);
„über x = 0“ ist außerdem unklar – Vorschlag: „Wie tief liegt sie
an der Stelle x = 0 lotrecht unter dem Dach?“.

ebenen-e4-k3-s3-v3: fraglich: „wie viel höher liegt der obere
senkrecht über dem unteren“ – gleiche Doppeldeutigkeit (lotrecht
2 dm, Ebenenabstand 8/√17 ≈ 1,94 dm) – Vorschlag: „lotrecht (bei
gleichem x)“.

ebenen-e1-k1-s6-v3, ebenen-e2-k1-s3-v3, ebenen-e2-k1-s4-v2,
ebenen-e2-k2-s3-v1, ebenen-e4-k1-s3-v1, ebenen-e4-k1-s5-v1,
ebenen-e4-k1-s4-v1: fraglich: bank.md „ein Buchstabe je Einheit
für eine Sache“ – E ist in diesen Zeilen ein Punkt, in den
Nachbarzeilen derselben Einheit die Ebene; in e4-k1-s4-v1 ist P
die Ebene, in e4-k1-s1 der Punkt. Innerhalb jeder Aufgabe
eindeutig, auf einem Blatt nebeneinander verwechselbar –
Vorschlag: Punkt E umbenennen (etwa K, Q, T), Ebene P → Q.

Sauber: 198 Zeilen ohne Befund

## Abgleich

- Beide Leser: ebenen-e1-k2-s2-v3 („dieselbe Richtung“ beim
  Faktor −2; gleicher Vorschlag).
- Nur Zweitleser: ebenen-e4-k3-s3-v1 („senkrecht unter dem Dach“
  zweideutig), ebenen-e4-k3-s3-v3 („senkrecht über“ zweideutig),
  Buchstabenregel (E als Punkt in e1-k1-s6-v3, e2-k1-s3-v3,
  e2-k1-s4-v2, e2-k2-s3-v1, e4-k1-s3-v1, e4-k1-s5-v1; P als
  Ebene in e4-k1-s4-v1).
- Nur Erstleser:
  - ebenen-e1-k2-s3-v2 („1 dm über der Scheibenebene“ ist nur der
    z-Unterschied, Ebenenabstand 0,6 dm): teils – die Lösung
    rechnet III sichtbar in z, ich hatte den Halbsatz als
    lotrechte Lesart durchgehen lassen; dass z nach oben nicht
    genannt ist, stimmt, der Vorschlag (Halbsatz streichen oder
    „in z-Richtung“) ist besser als der Bestand.
  - ebenen-e2-k3-s3-v3 („über oder unter“ ohne „xy-Ebene ist der
    Boden“, anders als v1 und v2): Zustimmung, übersehen – der
    Zusatz macht die Varianten gleich und die Frage eindeutig.
  - ebenen-e3-k1-s5-v3 (Drohne auf einer Geraden, „in welcher
    Ebene“ nicht eindeutig): Zustimmung, übersehen – eine Gerade
    liegt in unendlich vielen Ebenen; erst „waagerecht“ oder eine
    gekrümmte Bahn macht z = 7 zur einzigen Antwort.
  - ebenen-e2-k1-s8-v1 bis -v4 (hoehe sprosse statt pruefung an
    der letzten Sprosse von k1): teils – der Erstleser folgt dem
    sprosse_text „Prüfungshöhe“, ich der Entscheidung in stand.md,
    die bank.md („pruefung bleibt der letzten Sprosse vorbehalten“,
    eine je Einheit) mit zwei Prüfungshöhen in Einheit 2 in
    Einklang bringt und die Warnung bewusst trägt; welche Seite
    kippt, ist ein bank.md-Befund für den Chat, keine Korrektur
    der Zeilen.

Zahlen: Zweitleser 4 Befunde, Erstleser 8, gemeinsam 1, nur
Zweitleser 3. Gezählt sind Befund-Absätze, nicht ids: mein
Buchstaben-Befund ist ein Absatz mit sieben ids, die vier
Erstleser-Absätze zu e2-k1-s8 sind vier; „Sauber“ oben zählt
dagegen ids (208 minus 10 ids mit Befund).

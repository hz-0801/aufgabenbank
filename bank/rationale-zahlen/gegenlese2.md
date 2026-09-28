# Zweitlesung rationale-zahlen

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 209
(zone 23, e1 46, e2 59, e3 44, e4 37)

Prüfung: Alle 209 Zeilen einzeln gelesen (Ausgabe über ein kleines
Skript im Scratchpad). 77 Zeilen mit einem Rechenterm im Aufgabentext
(„Berechne", „Rechne geschickt", „Löse die Klammer auf", Termwert
mit Einsetzung) hat ein Skript mit sympy aus dem Aufgabentext neu
gerechnet und gegen pruef und die Ergebniszahl in loesung gehalten:
0 Differenzen. Die übrigen Rechenzeilen (Mitte, Runden, Gegenzahl,
Unterschied, Sach- und Preisaufgaben, Umkehrung, Zone) von Hand;
Ordnen-Zeilen zusätzlich per Skript auf aufsteigende Folge. Bei den
7 Ankreuzzeilen: genau eine Option richtig, loesung wortgleich. Bei
den 13 Fehler-finden-Zeilen: eingebauter Fehler wirklich falsch,
Richtigrechnung nachgerechnet. $-Zeichen, Klammern und geschweifte
Klammern paarig, keine doppelte Aufgabe, keine doppelte id (Skript).
Grafiken gegen die Vorlage geprüft: mathblatt.sty aus hz-0801/blattbau
(Stand main, 2026-09-28) frisch geklont und `\zahlenstrahl` gelesen.
werkzeuge/bank-pruef.py rationale-zahlen (nur lesend): 0 Abweichungen,
0 Warnungen in allen fünf Dateien.

## Befunde

e1-k1-s0-v1, e1-k1-s0-v2, e1-k1-s0-v3, e1-k1-s0-v4: Die Vorlage
beschriftet jeden Strich des `\zahlenstrahl` selbst mit seiner Zahl
(mathblatt.sty, Umgebung zahlengerade: an jedem Strich ein
`node[below]` mit `\pgfmathprintnumber`, ausgedünnt nur bei Platznot,
hier nicht). „Schreibe an jeden Strich seine Zahl" steht damit schon
gelöst auf dem Blatt; `{0/0}` setzt zusätzlich einen Punkt mit „0"
darüber, die Null steht doppelt. – Vorschlag: Befund an blattbau
(Schlüssel „ohne Zahlen" oder „nur Null" für `\zahlenstrahl`, wie
`ohnezahlen` bei `\saeulenab`); bis dahin die vier Zeilen nicht aufs
Blatt nehmen. Der offene Punkt in stand.md ist damit entschieden.

e1-k5-s1-v3: Der eingebaute Fehler (Mitte von $-0{,}8$ und $-0{,}7$
in die falsche Richtung, $-0{,}85$) ist ein anderes Muster als die
Sprosse „Fehler finden (Betrag statt Wert verglichen)"; die Variante
ändert das Merkmal, nicht nur Zahlen und Kontext. Rechnung selbst
stimmt ($-0{,}75$). – Vorschlag: Vergleichs- oder Ordnungsfehler mit
Beträgen wie in v1/v2, z. B. „$-2{,}7 < -2{,}9$, weil $2{,}7 < 2{,}9$".

fraglich: zone-f2-v4 (auch zone-f2-v3): Weil die Vorlage jeden Strich
beschriftet (0; 0,25; 0,5; 0,75 …), steht die gesuchte Zahl schon
unter dem Punkt D; der Fallstrick „ein Strich ist nicht 0,1"
verpufft, v3 ebenso (1,3 steht unter C). Lösung und Grafik stimmen.
– Vorschlag: hängt am selben Vorlagen-Schlüssel wie oben; bis dahin
gilt die Zeile als sehr leicht, nicht als Fallstrick.

fraglich: e1-k1-s4-v1, e1-k1-s4-v2, e1-k1-s4-v3: gleiche Ursache –
jeder Zwischenstrich trägt seine Dezimalzahl ($-2{,}5$; $-0{,}4$ …),
so bleibt nur der Bruch zu übersetzen. Lösung und Grafik stimmen. –
Vorschlag: xstep 1 mit Zwischenstrichen kann die Vorlage nicht;
Vorlagen-Schlüssel oder so hinnehmen.

fraglich: e1-k1-s7-v1, e1-k1-s7-v2: sprosse_text nennt eine Wurzel,
die Aufgabe hat keine (Katalog Z. 87 „hier nur der negative Teil",
stand.md Entscheidung 8). Rechnung stimmt. – Vorschlag: merkmal oder
sprosse_text sollte die Kürzung nennen, damit der Blattbau die
Wurzel nicht vermisst.

fraglich: zone-f4-v3: „Punkt vor Strich und Klammern mit
natürlichen Zahlen", Aufgabe mit $0{,}5$ und $2{,}5$ (stand.md
Entscheidung 2 nennt das bewusst). Rechnung stimmt. – Vorschlag:
entweder natürliche Zahlen (z. B. $6 + 3 \cdot 7$) oder das
merkmal sagt, dass die Zone hier absichtlich über den Text hinaus
geht.

fraglich: e3-k3-s1-v3: „$-3^2 = 9$" ist ein Potenzfehler (Minus zur
Basis gezogen), die Sprosse heißt „Vorzeichen des Produkts
vergessen"; v1 und v2 tragen Produkt und Quotient. Richtigrechnung
stimmt. – Vorschlag: dritte Zeile als Produkt- oder Quotientenfehler
oder die Sprosse trägt den Potenzfall bewusst (Kette hat Sprosse 5
„Potenz mit Klammer und ohne").

fraglich: e3-k3-s3-v3: Kühlkammer und Stunden unter sprosse_text
„Einfluss der Vorzeichen an Geldfluss über mehrere Monate". Rechnung
und Entscheidung stimmen ($-7$ °C). – Vorschlag: Geldkontext (z. B.
Sparplan mit Abbuchung je Monat) oder so lassen und im merkmal
nennen.

fraglich: e2-k7-s3-v1, e2-k7-s3-v3: Die Labels „Start" und „Ende"
setzt die Vorlage im Mathemodus (`{$\l$}`), also kursiv als
Buchstabenfolge. Lesbar, aber nicht wie Text. – Vorschlag:
`\text{Start}` und `\text{Ende}` in grafik.

Sauber: 192 Zeilen ohne Befund

(17 ids mit Befund, die „fraglich"-Zeilen mitgezählt; 209 − 17 = 192.)

## Abgleich

Gelesen nach dem Schreiben der Befunde: gegenlese.md (Erstleser
claude-opus-5-5, 2026-09-27, 15 ids, 194 sauber).

- Beide Leser: zone-f2-v3, zone-f2-v4 (Vorlage beschriftet jeden
  Strich, Ablesen wird Abschreiben); e1-k1-s0-v1 bis v4 (Beschriften
  ist in der Grafik gelöst, Befund an die Vorlage); e1-k5-s1-v3
  (Zweitleser: Fehlermuster passt nicht zur Sprosse; Erstleser:
  Lösung addiert negative Zahlen vor Einheit 2 – beides trifft zu,
  ein Tausch der Zeile erledigt beides); e3-k3-s1-v3 (Potenzmuster
  statt Produkt – Erstleser als Befund, Zweitleser als fraglich, ich
  schließe mich an); e2-k7-s3-v1, e2-k7-s3-v3 (Zweitleser: Labels im
  Mathemodus; Erstleser: kein Pfeil in der Grafik, Start und Ende
  schon im Text – der Punkt des Erstlesers wiegt schwerer, die
  Grafik trägt nichts; einen Pfeil von a nach b hat die Vorlage
  nicht, `\intervall` zeichnet Strecken ohne Spitze).
- Nur Zweitleser: e1-k1-s4-v1 bis v3 (Zwischenstriche beschriftet,
  fraglich); e1-k1-s7-v1, v2 (Wurzel im sprosse_text fehlt in der
  Aufgabe, fraglich); zone-f4-v3 (Dezimalzahl unter „natürliche
  Zahlen", fraglich); e3-k3-s3-v3 (Kühlkammer unter „Geldfluss",
  fraglich).
- Nur Erstleser:
  - zone-f2-v1 (Strichzahlen, 7 steht unter A): Zustimmung, gleiche
    Ursache wie f2-v3/v4; ich hatte die sehr leichte Zeile
    durchgehen lassen, weil bei Schritt 1 das Ablesen ohnehin kaum
    mehr als Lesen ist – der Erstleser hat recht, dass es dann
    nichts prüft.
  - e4-k2-s1-v3 (Produkt statt Summe): teils – der Erstleser liest
    das merkmal („Gegenzahlen und glatte Summen"), das die Aufgabe
    nicht trifft; ich lese den sprosse_text („Tauschen, geschickt
    zusammenfassen"), den $2 \cdot 50$ genau trifft. Eher das
    merkmal weiten („glatte Summen oder Produkte") als die Aufgabe
    tauschen.
  - e2-k7-s1-v2 (Minus in der Klammer übersehen statt
    $-2 - 3 = -1$): Zustimmung mit Grund – bank.md erlaubt jedes
    Muster aus „Typische Fehler", aber Varianten einer Sprosse
    sollen nur Zahlen und Kontext ändern; mit derselben Regel habe
    ich e1-k5-s1-v3 beanstandet, also gilt sie auch hier.
  - e2-k7-s1-v3 (Beträge subtrahiert bei $9 - (-5)$): Zustimmung,
    wie v2.
  - e3-k3-s1-v2 (minus durch minus als minus): teils – ein
    Vorzeichenfehler derselben Kette, aber die Sprosse sagt
    „Produkt"; strenge Lesart wie beim Erstleser, ich hatte den
    Quotienten als Produkt-Verwandten durchgehen lassen.

Zahlen: Zweitleser 17 Befunde, Erstleser 15, gemeinsam 10, nur
Zweitleser 7. Gezählt nach ids, jede id einmal, „fraglich"-Zeilen
mitgezählt (meine 17 ids stehen in 9 Befundzeilen); gemeinsam heißt
dieselbe id bei beiden, auch wenn das Stichwort verschieden ist.

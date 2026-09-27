# Zweitlesung vierfeldertafel

Datum: 2026-09-27 · Modell: claude-fable-5-1 (Zweitleser, ohne
Kenntnis von gegenlese.md) · geprüfte Zeilen: 78 (e1 33, e2 23,
zone 22)

Prüfung: Jede Lösung mit Python (fractions, sympy) aus dem
Aufgabentext nachgerechnet; jede pruef-Liste ausgewertet und mit
den Lösungszahlen verglichen (alle 60 Zeilen mit pruef stimmen).
Für jede \vierfeldertafel und \sachtabelle in loesungsgrafik die
Zeilen- und Spaltensummen geprüft (16 Tafeln, alle stimmig; die
Parametertafeln symbolisch, Ausschlusswerte −1/6 und −1/4
bestätigt). Sperre: alle Zahlen, Zahlenpaare und p-Terme aus
Merkkasten, Typischen Fehlern und den zwölf Originalen der Mappe
gegen aufgabe und loesung gelegt; Kontexte der verfremdeten
Originale gegen die Kontextliste der Mappe. Mengen je Kette,
Zone-Paar, Ankreuzoptionen, id-Muster und quelle von Hand
durchgesehen. `python3 werkzeuge/bank-pruef.py vierfeldertafel`:
zone 0/0, e1 0/0, e2 0/0 – Abweichungen 0, Warnungen 0.

## Befunde

vierfeldertafel-e1-k2-s2-v1: Die zweite Frage („mit welcher
Wahrscheinlichkeit nutzt eine Person, die nicht studiert, vor allem
das Rad?“) ist eine bedingte Wahrscheinlichkeit aus der Tafel,
$P_{\overline{S}}(R) = \frac{17}{60}$ – ein Handgriff, der in
keiner Kette des Eintrags steht (die Mappe verweist ihn auf das
Nachbarthema); die Sprosse verlangt nur „Rand mal bedingter
Anteil“. Dazu ist $\frac{17}{60} = 0{,}28\overline{3}$ periodisch,
die Aufgabe trägt keinen Rundungshinweis, obwohl antwort „__ %“
eine Zahl verlangt. Der Satz mischt Aufforderung und Frage. –
Vorschlag: zweite Frage auf ein Feld beziehen: „Welcher Anteil
aller Einwohner studiert nicht und nutzt vor allem das Rad?“
(Lösung $\overline{S} \cap R = 17\,\%$, letzter pruef-Wert 17);
soll die bedingte Frage bleiben, dann „Runde auf eine
Nachkommastelle“ in den Text.

vierfeldertafel-e1-k2-s5-v1: Der Kontext (Kunden eines Anbieters,
Tarife, „darunter die Hälfte der Plus-Kunden“) ist der Kontext des
Originals 2022MerhoehtBStochastikWTR2-1a (Mappe: „20 % Tarif S,
25 % L; … darunter die Hälfte der M-Kunden“, Kontextliste „Tarife
2022“). Zahlen sind anders, der Kontext nicht; Verfremdung
verlangt beides. – Vorschlag: gleiche Zahlen, anderer Kontext,
etwa: „Von den Gästen eines Hotels reisen $30\,\%$ mit dem Auto und
$20\,\%$ mit der Bahn an, alle übrigen mit dem Flugzeug. $55\,\%$
aller Gäste buchen Frühstück, darunter die Hälfte der Fluggäste;
$10\,\%$ aller Gäste reisen mit dem Auto und buchen kein
Frühstück.“ Lösung und Tabelle bleiben (Flugzeug 50, Frühstück
und Flugzeug 25, Frühstück und Auto 20, Frühstück und Bahn 10).

vierfeldertafel-e2-k1-s4-v1: Der Kontext „Bevölkerung einer
Großstadt“ ist der Kontext, den die Mappe für die
Pool-Aufgaben 2025 nennt („Großstadt 2025“); das verfremdete
Original 2025MerhoehtBStochastikWTR1-1b ist eine davon, und $H$
„Haus mit Garten“ liegt nahe an dessen Ereignis $G$. Zahlen und
Rechnung stimmen ($27$, $18 + 33 = 51$, $\frac{27}{51} \approx
0{,}53$). – Vorschlag: anderer Kontext bei gleicher Tafel, etwa
Beschäftigte eines Unternehmens ($S$: arbeitet teils im
Homeoffice, $H$: kommt mit dem Rad).

vierfeldertafel-e2-k1-s3-v2: Die Angaben $40\,\%$ Barzahler und
$25\,\%$ Kundenkarte ergeben in der Lösung das Produkt
$0{,}4 \cdot 0{,}25$, das im Lösungsweg des Originals derselben
Sprosse steht (2020MgrundlegendAStochastik12-a: „0,48 + 0,25 ·
0,4“); auch $60\,\%$ steht dort als Rand. Das ist ein Zahlenpaar
aus einem Original der Mappe. – Vorschlag: $25\,\%$ durch $35\,\%$
ersetzen: $0{,}4 \cdot 0{,}35 + 0{,}6 \cdot 0{,}6 = 0{,}14 + 0{,}36
= 0{,}5$, also $50\,\%$; pruef `0.4*0.35+0.6*0.6`.

vierfeldertafel-e1-k2-s2-v2 (schwach): $20\,\%$ und $25\,\%$ sind
die ersten beiden Zahlen des Originals 2022MerhoehtBStochastikWTR2-1a
(„20 % Tarif S, 25 % L“), hier in anderen Rollen (Rand und
bedingter Anteil). Nach dem Wortlaut der Sperre ein Zahlenpaar aus
einem Original. – Vorschlag: $25\,\%$ → $35\,\%$: $E \cap V =
7\,\%$, $E \cap \overline{V} = 13\,\%$, $\overline{E} \cap V =
5\,\%$, $\overline{E} \cap \overline{V} = 75\,\%$; pruef
`[7, 13, 5, 75, 80, 88]`; loesungsgrafik
`\vierfeldertafel{V}{E}{7,13,20,5,75,80,12,88,100}`.

vierfeldertafel-zone-f5-v1: Der Term $1 - 3p$ ist wörtlich der
Term des Originals 2021MerhoehtAStochastik11-a ($P(\overline{A})
= 1 - 3p$) und der Typischen Fehler („1 − 3p − 3p falsch als
1 − 3p“); die Sperre nennt „Term mit Variable und Zahl“. Das
Skript findet ihn nicht (anderes Minuszeichen in der Mappe). –
Vorschlag: $1 - 2p = 0{,}3$ → $2p = 0{,}7$, $p = 0{,}35$; pruef
`0.7/2`.

vierfeldertafel-zone-f5-v4: Dieselbe Sperre trifft die Lösung
$1 - 3p$; die Aufgabe $1 - (2p + p)$ führt zwangsläufig dorthin.
– Vorschlag: $1 - (4p + 3p)$ – zusammengefasst $1 - 7p$ (nicht
$1 - 4p + 3p$); pruef bleibt 1. Nicht $1 - 6p$ wählen, das steht
ebenfalls im Original.

vierfeldertafel-e2-k1-s1-v3: „Online-Bewerbungen“ sind im Text
nicht eingeführt; er sagt nur „$300$ kamen per Post“. Dass alle
übrigen online kamen, muss der Schüler annehmen. Rechnung stimmt
($800 - 300 - 330 = 170$). – Vorschlag: „… kamen $300$ per Post,
die übrigen online; …“.

vierfeldertafel-zone-f4-v1: Einzige Tabellenaufgabe des Eintrags
ohne loesungsgrafik, obwohl die Lösung fünf Einträge in eine
Tabelle setzt und e1 für jede Tafel eine Lösungsgrafik führt.
Werte stimmen ($16$, $25$, $27$, $26$, $53$). – Vorschlag:
`\sachtabelle{lccc}{ & ja & nein & Summe}{Klasse 7a & 12 & 16 & 28 \\ Klasse 7b & 15 & 10 & 25 \\ Summe & 27 & 26 & 53}`.

Einheitsebene e1 und e2 (nicht je Zeile gezählt): Die Regel „ein
Buchstabe je Einheit für eine Sache“ ist in e1 mehrfach verletzt:
$S$ steht für Seniorenhaushalte (s1-v1), Studierende (s2-v1),
Sopran (s2-v3) und Stammkunden (k3-s1-v1); $A$ für abends
(s1-v5), Akkuschaden (k3-s1-v2) und das Ereignis $A$ (s6); $J$
für jünger (s1-v3, s4-v3) und Jahresvertrag (s1-v5); $L$ für
geleast und Licht; $V$ für verspätet, Vereinssport und Vorspeise.
In e2: $A$ für das Ereignis $A$ und Auto (s2-v3), $H$ für
Halbpension (s1-v1) und Haus mit Garten (s4-v1). Bei über zwanzig
Buchstabenaufgaben je Einheit ist die Regel in der Bank nicht
haltbar; sie gehört zum Blatt. – Vorschlag: bank.md-Befund in
stand.md: die Buchstabenprobe in den Zusammenbau verlegen (der
wählt je Blatt aus); alternativ in e1 nur die Vierfach-Kollision
$S$ entschärfen: s1-v1 „Seniorenhaushalte ($H$)“ – $H$ ist in e1
noch frei (frei sind nur noch C, G, H, N, O, Q, U, X, Y).

Sauber: 69 Zeilen ohne Befund (alle 60 Rechenlösungen richtig,
alle 16 Lösungstafeln summenstimmig, alle 12 Ankreuzzeilen mit
genau einer richtigen, wortgleich genannten Option, alle 6
Fehler-finden-Zeilen mit echtem Fehler aus „Typische Fehler“ und
eigenen Zahlen, keine Dublette; Mengen je Kette, Zone-Paar und
quelle-Zeilen stimmen). Zwei Anmerkungen ohne Änderungsbedarf:
e2-k2-s2-v3 begründet den Additionssatz, den der Sprossentext
nicht nennt (Merkkasten E2 nennt ihn; das Merkmal passt); die
Vorstufe e1-k2-s0 stellt „Anteil oder Anzahl?“ nur einmal (v4),
die Antwort ist damit ohne Gegenstück – Folge der Menge 4 für
zwei Handgriffe, in stand.md als Katalogbefund 3 schon benannt.

## Abgleich mit gegenlese.md

Befundzeilen: Erstleser 18 (17 Tafeln transponiert, 1 Textlücke;
Sauber 60), Zweitleser 9 Zeilen und ein Einheitsbefund (Sauber 69).

Beide: keine Zeile deckungsgleich – die 17 Tafelbefunde des
Erstlesers waren im jsonl schon berichtigt (Commit 4414eb0), als
die Zweitlesung begann. Die Zweitlesung hat genau diesen Stand
geprüft: mit der Lesart „erstes Argument Spalte, zweites Zeile,
Werte zeilenweise“ aus mappen/_bausteine.md passen alle 16
Aufgaben- und Lösungstafeln und die beiden Tafeln in e2 k1-s4 zu
Text und Lösung, alle Summen gehen auf. Die Korrektur des
Erstlesers ist damit unabhängig bestätigt, einschließlich der
Entscheidung, Merkmalsnamen zu tauschen statt Lösungen zu ändern
(e2-k1-s4-v1: 27/51, nicht 22/51).

Nur der Erstleser: (2) e2-k1-s1-v4, „alle 1 000 Lose verkauft“ steht
nicht im Text – zutreffend; derselbe Befundtyp wie meine
Online-Bewerbungen (e2-k1-s1-v3), dort vom Erstleser nicht
bemerkt.

Nur der Zweitleser: e1-k2-s2-v1 (bedingte Wahrscheinlichkeit als
zweite Frage, periodisches Ergebnis ohne Rundungshinweis),
e1-k2-s5-v1 (Kontext Tarife = Original 2022), e2-k1-s4-v1 (Kontext
Großstadt = Pool 2025), e2-k1-s3-v2 (Produkt 0,4 · 0,25 aus dem
Original 2020), e1-k2-s2-v2 (Zahlenpaar 20/25, schwach),
zone-f5-v1 und zone-f5-v4 (Term 1 − 3p aus Original und Typischen
Fehlern), e2-k1-s1-v3 (Online-Bewerbungen), zone-f4-v1 (fehlende
loesungsgrafik), Einheitsbefund Buchstabenregel. Der Erstleser hat
Verfremdung und Sperre nicht gegen die Mappe gelegt („bank.md nur
für die Felder“); daher fehlen ihm die Kontext- und Sperrbefunde.

Widersprüche: keine. Der Erstleser meldet „Punkte 3 bis 6 ohne
Befund“; die Zweitlesung teilt das für Merkmal, Ankreuzen und
Fehler finden, nicht für Sperre und Verfremdung (fünf Zeilen, dazu
eine schwache).

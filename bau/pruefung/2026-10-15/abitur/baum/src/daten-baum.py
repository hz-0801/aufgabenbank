import sys; sys.path.insert(0, '/tmp/claude-0/-home-claude/bcbd1387-cd54-5434-8598-ae959779249b/scratchpad/as')
from gen import zeile, schreibe
K = 'baum-bedingte-wahrscheinlichkeit'
Z = []
rang = [0]
def z(einheit, stufe, eid, w, l, za, sw, bem, grafik='', form='', **kw):
    rang[0] += 1
    Z.append(zeile(K, einheit, stufe, eid, w, l, za, sw, rang[0], bem, grafik, form, **kw))

HH = 'In einer Stadt haben 31,5 % der Haushalte mindestens ein Kind. Von diesen Haushalten sind 14,2 % überbelegt, von den Haushalten ohne Kind sind es 5,5 %.'
RAD = 'Ein Glücksrad hat Sektoren mit der Zahl 4 und Sektoren mit der Zahl 2. Es wird zweimal gedreht; der Rabatt in Prozent ist das Produkt der beiden Zahlen. Die Wahrscheinlichkeit, zweimal die 4 zu drehen, beträgt $\\frac{1}{16}$.'
BEF = 'Bei einer Befragung erhalten 70 % der Jugendlichen die Frage F1 „Hast du schon einmal unentschuldigt gefehlt?“, die übrigen die Frage F2 „Hast du noch nie unentschuldigt gefehlt?“. Alle antworten wahrheitsgemäß mit Ja oder Nein. Der Anteil $p$ derer, die schon einmal gefehlt haben, ist unter den F1-Befragten so groß wie unter allen.'
GLITZ = 'Bei einer Werbeaktion erhält jedes Kind einen verpackten Ball; mit einer Wahrscheinlichkeit von 30 % ist er glitzernd gefärbt.'
TREUE = 'In einem Supermarkt sammeln 80 % der Kundschaft Treuepunkte ($T$). Unter den Sammelnden sind 70 % weiblich ($w$), unter den übrigen ist der Anteil weiblicher Personen $a$.'
BAUM_T = '\\baumabi{T/{0,8}/{w/{0,7},\\overline{w}/},\\overline{T}//{w/{a},\\overline{w}/}}'
PAKET = 'In einem Paketzentrum haben 12 % der Pakete das Ziel A und 8 % das Ziel B; 6 % aller Pakete sind schwer ($S$).'
RAD8 = 'Ein Glücksrad hat acht gleich große Sektoren: fünfmal die 3, zweimal die 2 und einmal die 1.'
RAD8_G = '\\kreisdiagramm[1.1]{3/1,2/1,3/1,3/1,2/1,3/1,1/1,3/1}'
LEHR = 'Von den Lehrkräften eines Landes arbeiten 30 % an einem Gymnasium ($G$). 20 % der Lehrkräfte sind weiblich ($W$) und arbeiten an einem Gymnasium; insgesamt sind 65 % der Lehrkräfte weiblich.'
FORT = 'An einer Fortbildung nehmen 24 Lehrkräfte teil, davon 14 Frauen. Für eine Präsentation werden 5 von ihnen zufällig ausgewählt.'
TM = 'Von der Kundschaft eines Baumarkts sind 70 % Treuekunden ($T$) und 30 % Morgenkunden ($M$), die vor 9 Uhr einkaufen. Es gilt $P(\\overline{T} \\cap M) = 0{,}06$.'
REISE = 'Von den Kunden eines Reisebüros reisen 50 % gerne in die Region A, 40 % gerne in die Region B und 15 % gerne in beide Regionen.'
URNE32 = 'In einer Urne liegen drei rote und zwei grüne Kugeln.'
SCHW = 'Eine Schwimmgruppe hat 16 Kinder; 6 von ihnen haben das Abzeichen Bronze.'

# ===================== AS10 Baumdiagramm =====================
E = 'Baumdiagramm'
z(E, 'Baum zeichnen', '2025-bebb-gk-B4a', HH + ' Ein Haushalt wird zufällig ausgewählt. Stelle den Sachverhalt in einem beschrifteten Baumdiagramm dar.',
  'K 0,315, nicht K 0,685 | B unter K 0,142, nicht B 0,858 | B unter nicht K 0,055, nicht B 0,945', 'dezimal', 'I',
  'andere Zahlen (Original 28,5 %, 15,9 %, 6,5 %)', form='zeichnen')
z(E, 'Baum zeichnen', '2024-bebb-gk-A1.9a', BEF + ' Vervollständige das Baumdiagramm.',
  'F1 0,7: Ja p, Nein 1 − p | F2 0,3: Ja 1 − p, Nein p', 'ganz', 'I',
  'andere Zahlen (Original 60 % / 40 %); Baum mit 0,7 und p vorgegeben wie im Original',
  grafik='\\baumabi{F_1/{0,7}/{\\text{Ja}/{p},\\text{Nein}/},F_2//{\\text{Ja}/,\\text{Nein}/}}', form='einzeichnen')
z(E, 'Baum zeichnen', '2024-bebb-gk-B4.2a', RAD + ' Stelle das Zufallsexperiment in einem beschrifteten Baumdiagramm dar.',
  'P(4)² = 1/16 ⇒ P(4) = 1/4 ⇒ P(2) = 1 − 1/4 = 3/4 | Baum: auf beiden Stufen 4 mit 1/4 und 2 mit 3/4', 'bruch', 'II',
  'andere Zahlen (Original Sektoren 5 und 2, 1/36; P(5) = 1/6)', form='zeichnen')
z(E, 'Pfadwahrscheinlichkeit gesucht', '2024-bebb-gk-A1.6a', GLITZ + ' Drei Kinder erhalten je einen Ball. Zeige, dass die Wahrscheinlichkeit, dass jedes der drei Kinder einen glitzernden Ball erhält, kleiner als 3 % ist.',
  '0,3³ = 0,027 < 0,03', 'dezimal', 'I', 'andere Zahlen (Original 40 %, 0,064 < 10 %)')
z(E, 'Pfadwahrscheinlichkeit gesucht', '2026-bb-gk-B4d', TREUE + ' Es sei $a = 0{,}3$. Untersuche, ob die Wahrscheinlichkeit, dass eine zufällig ausgewählte Person weiblich ist und Treuepunkte sammelt, viermal so groß ist wie die Wahrscheinlichkeit, dass sie nicht weiblich ist und keine Treuepunkte sammelt.',
  'P(w ∩ T) = 0,8 · 0,7 = 0,56; P(nicht w ∩ nicht T) = 0,2 · 0,7 = 0,14 ⇒ 0,56 = 4 · 0,14 ⇒ ja', 'dezimal', 'II',
  'andere Zahlen (Original 75 %, 80 %, a = 0,6, sechsmal)', grafik=BAUM_T)
z(E, 'Summe von Pfaden gesucht', '2023-bebb-gk-A1.6a', 'In einer Urne liegen sechs Kugeln, vier rote und zwei weiße. Es werden zwei Kugeln mit Zurücklegen gezogen. Ermittle die Wahrscheinlichkeit, dass beide Kugeln dieselbe Farbe haben.',
  '(2/3)² + (1/3)² = 4/9 + 1/9 = 5/9', 'bruch', 'I', 'andere Zahlen (Original 3 rot, 2 weiß; 13/25)')
z(E, 'Summe von Pfaden gesucht', '2025-bebb-gk-B4b', HH + ' Zeige, dass etwa 8,24 % aller Haushalte überbelegt sind.',
  '0,315 · 0,142 + 0,685 · 0,055 ≈ 0,0824 ⇒ etwa 8,24 %', 'dezimal', 'I', 'andere Zahlen (Original 9,18 %)')
z(E, 'Summe von Pfaden gesucht', '2025-bebb-gk-A1.3b', RAD8 + ' Es wird zweimal gedreht. Berechne die Wahrscheinlichkeit, dass die Summe der beiden Zahlen ungerade ist.',
  'P(2) = 2/8, P(ungerade) = 6/8 ⇒ P = 2/8 · 6/8 + 6/8 · 2/8 = 24/64 = 3/8', 'bruch', 'II',
  'andere Zahlen (Original viermal 7, dreimal 6, einmal 5; 15/32)', grafik=RAD8_G)
z(E, 'Summe von Pfaden gesucht', '2024-bebb-gk-B4.2b', RAD + ' Sechs Personen drehen nacheinander. Berechne die Wahrscheinlichkeit, dass genau viermal der kleinstmögliche Rabatt erzielt wird, und zwar bei vier Personen unmittelbar hintereinander.',
  'P(kleinster Rabatt) = 9/16; drei Lagen des Viererblocks ⇒ P = 3 · (9/16)⁴ · (7/16)² ≈ 0,0575', 'dezimal', 'III',
  'andere Zahlen (Original sieben Personen, 25/36; 2,7 %)')
z(E, 'Summe von Pfaden gesucht', '2022-bebb-gk-B4f', PAKET + ' Zwei Paketboten erhalten je 12 zufällig ausgewählte Pakete. Bestimme die Wahrscheinlichkeit, dass mindestens einer der beiden kein Paket mit dem Ziel A erhält.',
  '0,88¹² ≈ 0,216 ⇒ P = 1 − (1 − 0,88¹²)² ≈ 0,385', 'dezimal', 'III',
  'andere Zahlen (Original 10 %, je 10 Pakete; 57,6 %)')
# Mehr AS10
z(E, 'Baum zeichnen', '2025MgrundlegendAStochastik11-a', 'In einem Computerspiel wird der Startpunkt A mit 30 % zugewiesen, sonst B. Wer bei A startet, trifft mit 60 % auf einen bestimmten Charakter. Bei 49 % aller Spiele startet man bei B und trifft auf den Charakter. Stelle den Sachverhalt in einem beschrifteten Baumdiagramm dar.',
  'A 0,3: C 0,6, nicht C 0,4 | B 0,7: C 0,49/0,7 = 0,7, nicht C 0,3', 'dezimal', 'I', 'andere Zahlen (Original 40 %, 80 %, 42 %)', form='zeichnen', iqb_stelle='A11a')
z(E, 'Baum zeichnen', '2020-be-gk-B4.1b', 'Ein Würfel trägt auf zwei seiner sechs gleich wahrscheinlichen Seiten eine 6. Wer mit höchstens vier Würfen eine 6 wirft, darf anfangen. Erstelle ein Baumdiagramm und ermittle die Wahrscheinlichkeit, anfangen zu dürfen.',
  'je Stufe 6 mit 1/3, keine 6 mit 2/3, Abbruch nach der 6 ⇒ P = 1 − (2/3)⁴ = 65/81 ≈ 0,802', 'bruch', 'II', 'andere Zahlen (Original höchstens dreimal; 19/27)', form='zeichnen')
z(E, 'Pfadwahrscheinlichkeit gesucht', '2019-be-gk-B4.2a', 'Zwei Personen würfeln mit einem fairen Würfel, erst die eine, dann die andere. Ist die erste Augenzahl kleiner als die zweite, bringt die erste Person den Müll hinunter, sonst die zweite. Bestimme die Wahrscheinlichkeit, dass die erste Person eine 3 würfelt und den Müll hinunterbringen muss.',
  '1/6 · 3/6 = 1/12', 'bruch', 'I', 'herausgelöst; andere Zahlen (Original Augenzahl 4; 1/18)')
z(E, 'Pfadwahrscheinlichkeit gesucht', '2021-be-gk-B4g', 'Beim täglichen Start eines Spiels gibt es 10 Bonuspunkte mit 60 %, 20 Bonuspunkte mit 30 % und 50 Bonuspunkte mit 10 %. Jemand startet an drei aufeinanderfolgenden Tagen. Bestimme die Wahrscheinlichkeit, von Tag zu Tag weniger Bonuspunkte zu erhalten.',
  'einzige Folge 50, 20, 10 ⇒ P = 0,1 · 0,3 · 0,6 = 0,018', 'dezimal', 'I', 'andere Zahlen (Original 50 %, 40 %, 10 %; 0,02)')
z(E, 'Pfadwahrscheinlichkeit gesucht', '2021MgrundlegendBStochastikWTR1-1a', 'Unter jedem Deckel eines Joghurtbechers ist zufällig eines von acht Motiven, jedes mit gleicher Wahrscheinlichkeit. Drei Becher werden nacheinander geöffnet. Berechne die Wahrscheinlichkeit, dass nur im ersten und im dritten Becher das Motiv 1 ist.',
  '(1/8)² · 7/8 = 7/512 ≈ 0,0137', 'bruch', 'I', 'andere Zahlen (Original sechs Motive; 5/216)', iqb_stelle='B1.1a')
z(E, 'Pfadwahrscheinlichkeit gesucht', '2020-be-gk-B4.2e', 'In einem Betrieb ist ein Viertel der Beschäftigten weiblich ($w$). 4 % der weiblichen und 12 % der übrigen Beschäftigten sind unzufrieden ($u$). Im Baumdiagramm steht $x$ am Ast von $\\overline{w}$ nach $\\overline{u}$, $y$ am Ende des Pfads $w$, $u$. Ermittle $x$ und $y$.',
  'x = 1 − 0,12 = 0,88 | y = 0,25 · 0,04 = 0,01', 'dezimal', 'I', 'andere Zahlen (Original 1/3, 3,5 %, 10,5 %)',
  grafik='\\baumabi{w/{0,25}/{u/,\\overline{u}/},\\overline{w}//{u/,\\overline{u}/{x}}}')
z(E, 'Pfadwahrscheinlichkeit gesucht', '2026MgrundlegendAStochastik13-a', 'Ein Versandhändler verschickt 50 % seiner Sendungen mit dem Unternehmen A. 12 % aller Sendungen werden mit A verschickt und verspätet zugestellt; von den übrigen Sendungen werden 25 % verspätet zugestellt. Ermittle den Anteil $x$ der verspäteten unter den mit A verschickten Sendungen und weise nach, dass 12,5 % aller Sendungen nicht mit A verschickt und verspätet zugestellt werden.',
  'x = 0,12/0,5 = 0,24 | 0,5 · 0,25 = 0,125', 'dezimal', 'II', 'andere Zahlen (Original 40 %, 8 %, 30 %; x = 20 %, y = 18 %)', iqb_stelle='A13a')
z(E, 'Summe von Pfaden gesucht', '2017-be-gk-B3.1c', 'Ein Gerät wird in vier Werken hergestellt: Werk A liefert 20 %, B 30 %, C 10 % und D 40 % aller Geräte. Fehlerhaft sind in A 4 %, in B 2 %, in C 5 % und in D 3 % der dort hergestellten Geräte. Weise nach, dass 3,1 % aller Geräte fehlerhaft sind.',
  '0,2 · 0,04 + 0,3 · 0,02 + 0,1 · 0,05 + 0,4 · 0,03 = 0,031 = 3,1 %', 'dezimal', 'I', 'andere Zahlen (Original 10/30/20/40 %, 5/3/4/2 %; 3 %)')
z(E, 'Summe von Pfaden gesucht', '2021-be-gk-A1.7a', 'In einer Urne liegen 7 weiße und 3 schwarze Kugeln. Zehn Bewerber ziehen nacheinander je eine Kugel ohne Zurücklegen; wer weiß zieht, ist ausgewählt. Zeige, dass der zweite Bewerber mit 70 % ausgewählt wird.',
  '7/10 · 6/9 + 3/10 · 7/9 = 63/90 = 7/10 = 70 %', 'bruch', 'II', 'andere Zahlen (Original 6 weiß, 4 schwarz; 60 %)')
z(E, 'Summe von Pfaden gesucht', '2021-be-gk-B4h', 'Beim täglichen Start eines Spiels gibt es 10 Bonuspunkte mit 60 %, 20 Bonuspunkte mit 30 % und 50 Bonuspunkte mit 10 %. Jemand startet an vier Tagen. Bestimme die Wahrscheinlichkeit, insgesamt 80 Bonuspunkte zu erhalten.',
  '80 = 50 + 10 + 10 + 10 (vier Reihenfolgen) oder 20 + 20 + 20 + 20 ⇒ P = 4 · 0,1 · 0,6³ + 0,3⁴ = 0,0945', 'dezimal', 'III', 'andere Zahlen (Original 50/40/10 %; 0,0756)')

# ===================== AS20 Ziehen ohne Zurücklegen =====================
E = 'Ziehen ohne Zurücklegen'
ST = 'Acht Stühle stehen in einer Reihe. Es gibt fünf Möglichkeiten, vier Stühle so auszuwählen, dass zwischen je zwei ausgewählten mindestens ein weiterer Stuhl steht.'
z(E, 'Ergebnisse aufzählen', '2024-bebb-gk-A1.3a', ST + ' Gib diese fünf Möglichkeiten an.',
  'Stühle (1, 3, 5, 7), (1, 3, 5, 8), (1, 3, 6, 8), (1, 4, 6, 8), (2, 4, 6, 8)', 'ganz', 'I', 'andere Zahlen (Original sechs Stühle, drei, vier Möglichkeiten)', form='karo')
z(E, 'Ergebnisse aufzählen', '2024-bebb-gk-A1.3b', ST + ' Vier Freunde setzen sich so, dass zwischen je zweien mindestens ein Stuhl frei bleibt. Berechne die Anzahl der Möglichkeiten.',
  '5 Auswahlen, je 4! Anordnungen ⇒ 5 · 24 = 120', 'ganz', 'I', 'andere Zahlen (Original 4 · 3! = 24)')
z(E, 'Ergebnisse aufzählen', '2026-bb-gk-A1.3b', 'Eine Münze wird fünfmal geworfen; die Ergebnisse sind Abfolgen von Z (Zahl) und W (Wappen). A: höchstens einmal Zahl; B: bei den letzten beiden Würfen mindestens einmal Zahl. Gib alle Ergebnisse an, bei denen weder A noch B eintritt.',
  'nicht B: letzte zwei Würfe WW; nicht A: mindestens zweimal Z ⇒ ZZZWW, ZZWWW, ZWZWW, WZZWW', 'ganz', 'II',
  'andere Zahlen (Original A: höchstens einmal W, B: erste zwei Würfe)', form='karo')
z(E, 'Wahrscheinlichkeit gesucht', '2025-bebb-gk-A1.6a', SCHW + ' Zwei Kinder werden zufällig ausgewählt. Berechne die Wahrscheinlichkeit, dass beide das Abzeichen Bronze haben.',
  '6/16 · 5/15 = 30/240 = 1/8', 'bruch', 'I', 'andere Zahlen (Original 20 Kinder, 9; 72/380)')
z(E, 'Wahrscheinlichkeit gesucht', '2023-bebb-gk-B4.1g', FORT + ' Ermittle die Wahrscheinlichkeit, dass alle Ausgewählten Frauen sind.',
  '(14 über 5)/(24 über 5) = 2002/42504 = 13/276 ≈ 0,047', 'dezimal', 'I', 'andere Zahlen (Original 20, 12, 6; 2,4 %)')
z(E, 'Wahrscheinlichkeit gesucht', '2022-bebb-gk-A1.6a', URNE32 + ' Drei Kugeln werden ohne Zurücklegen gezogen. Ermittle die Wahrscheinlichkeit, dass mindestens eine gezogene Kugel grün ist.',
  'P(keine grün) = 3/5 · 2/4 · 1/3 = 1/10 ⇒ P = 1 − 1/10 = 9/10', 'bruch', 'II', 'andere Zahlen (Original 4 rot, 2 grün; 4/5)')
z(E, 'Wahrscheinlichkeit gesucht', '2023-bebb-gk-A1.6b', 'In einer Urne liegen vier rote und zwei weiße Kugeln. Drei Kugeln werden nacheinander ohne Zurücklegen gezogen. Ermittle die Wahrscheinlichkeit, dass mehr rote als weiße Kugeln gezogen werden.',
  'P(3 rote) = 4/6 · 3/5 · 2/4 = 1/5; P(genau 2 rote) = 3 · 4/6 · 3/5 · 2/4 = 3/5 ⇒ P = 4/5', 'bruch', 'II', 'andere Zahlen (Original 3 rot, 2 weiß; 7/10)')
z(E, 'Wahrscheinlichkeit gesucht', '2023-bebb-gk-B4.1h', FORT + ' Bestimme die Wahrscheinlichkeit, dass weniger als zwei Frauen ausgewählt werden.',
  'P(0) = (10 über 5)/(24 über 5) = 252/42504 ≈ 0,0059; P(1) = 14 · (10 über 4)/(24 über 5) = 2940/42504 ≈ 0,0692 ⇒ P = 19/253 ≈ 0,075', 'dezimal', 'III',
  'andere Zahlen (Original 20, 12, 6; 1,8 %)')
z(E, 'Wahrscheinlichkeit gesucht', '2022-bebb-gk-A1.6b', URNE32 + ' Eine Kugel wird entfernt. Danach ist die Wahrscheinlichkeit, beim Ziehen von zwei Kugeln ohne Zurücklegen zwei verschiedene Farben zu erhalten, $\\frac{2}{3}$. Entscheide, ob die entfernte Kugel rot oder grün ist, und begründe.',
  'rot entfernt: 2 rot, 2 grün ⇒ 2 · 2/4 · 2/3 = 2/3; grün entfernt: 3 rot, 1 grün ⇒ 2 · 3/4 · 1/3 = 1/2 ⇒ rote Kugel entfernt', 'bruch', 'III',
  'andere Zahlen (Original 4 rot, 2 grün, 60 %)')
# Mehr AS20
z(E, 'Ergebnisse aufzählen', '2023MgrundlegendAStochastik12-a', 'Ein Würfel (1 bis 6) und eine Münze (Zahl, Wappen) werden je einmal geworfen. A: ungerade Zahl und Wappen; B: Zahl größer als 2. Gib die Ergebnisse an, die zu $A \\cap B$ gehören.',
  '(3; W), (5; W)', 'ganz', 'I', 'andere Zahlen (Original gerade, größer als 3)', form='karo', iqb_stelle='A12a')
z(E, 'Ergebnisse aufzählen', '2017-be-gk-B3.1a', 'Ein Händler hat Geräte in sieben Farben. Für das Schaufenster sollen drei Farben ausgewählt werden. Bestimme die Anzahl der Möglichkeiten.',
  '(7 über 3) = 35', 'ganz', 'I', 'andere Zahlen (Original sechs Farben, vier; 15)')
z(E, 'Wahrscheinlichkeit gesucht', '2018-be-gk-B3.1a', 'In einem Topf liegen 3 schwarze und 5 weiße Kugeln. Zwei Kugeln werden mit einem Griff gezogen; man gewinnt, wenn keine schwarze dabei ist. Weise nach, dass die Gewinnwahrscheinlichkeit $\\frac{5}{14}$ beträgt.',
  '5/8 · 4/7 = 20/56 = 5/14', 'bruch', 'I', 'andere Zahlen (Original 2 schwarz, 4 weiß; 0,4)')
z(E, 'Wahrscheinlichkeit gesucht', '2020-be-gk-A1.5a', 'In einem Behälter liegen vier blaue und zwei rote Kugeln. Zwei Kugeln werden ohne Zurücklegen entnommen. Berechne die Wahrscheinlichkeit für zwei verschiedene Farben.',
  '4/6 · 2/5 + 2/6 · 4/5 = 16/30 = 8/15', 'bruch', 'I', 'andere Zahlen (Original 3 blau, 2 rot; 3/5)')
z(E, 'Wahrscheinlichkeit gesucht', '2018MgrundlegendAStochastik11-a', 'Zehn Karten, je zwei mit 1, 2, 3, 4 und 5, werden gemischt und nacheinander abgelegt. Bestimme die Wahrscheinlichkeit, dass die beiden ersten Karten mit 1 beschriftet sind.',
  '2/10 · 1/9 = 1/45', 'bruch', 'I', 'andere Zahlen (Original acht Karten, 1 bis 4; 1/28)', iqb_stelle='A11a')
z(E, 'Wahrscheinlichkeit gesucht', '2019-be-gk-A1.4c', 'Aus 12 Frauen und 8 Männern eines Chors werden zwei Personen zufällig ausgewählt. Gib einen Term für die Wahrscheinlichkeit an, dass eine Frau und ein Mann ausgewählt werden, und berechne sie.',
  '12/20 · 8/19 + 8/20 · 12/19 = 192/380 = 48/95 ≈ 0,505', 'bruch', 'II', 'andere Zahlen (Original 11 Frauen, 9 Männer; 99/190)')
z(E, 'Wahrscheinlichkeit gesucht', '2018MgrundlegendAStochastik11-b', 'Zehn Karten, vier mit gerader und sechs mit ungerader Zahl, werden nacheinander aufgedeckt. Bestimme die Wahrscheinlichkeit, dass spätestens die dritte Karte eine gerade Zahl trägt.',
  '1 − 6/10 · 5/9 · 4/8 = 1 − 1/6 = 5/6', 'bruch', 'II', 'andere Zahlen (Original acht Karten, 4 und 4; 13/14)', iqb_stelle='A11b')
z(E, 'Wahrscheinlichkeit gesucht', '2017-be-gk-B3.1b', 'Eine Lieferung umfasst 40 Geräte, davon sind vier fehlerhaft. Zehn Geräte werden zufällig ausgewählt. A: Keines der zehn ist fehlerhaft. B: Mindestens eines ist fehlerhaft. Berechne $P(A)$ und $P(B)$.',
  'P(A) = (36 über 10)/(40 über 10) ≈ 0,393 | P(B) = 1 − P(A) ≈ 0,607', 'dezimal', 'II', 'andere Zahlen (Original 50 Geräte, drei fehlerhaft; 0,504)')
z(E, 'Wahrscheinlichkeit gesucht', '2021-be-gk-A1.7b', 'In einer Urne liegen 7 weiße und 3 schwarze Kugeln. Bewerber ziehen nacheinander ohne Zurücklegen; wer weiß zieht, ist ausgewählt. Entscheide, ob der erste oder der dritte Bewerber die größere Chance hat, und begründe.',
  'P(W₁) = 7/10; P(W₃) = 7/10 · 6/9 · 5/8 + 2 · 7/10 · 3/9 · 6/8 + 3/10 · 2/9 · 7/8 = 7/10 ⇒ gleiche Chance', 'bruch', 'III', 'andere Zahlen (Original 6 weiß, 4 schwarz; 3/5)')
z(E, 'Wahrscheinlichkeit gesucht', '2019MgrundlegendAStochastik2-b', 'Jemand hat acht Bonbons gewonnen, Zitrone oder Orange. Zwei werden zufällig ausgewählt und verschenkt. Die Wahrscheinlichkeit, dass ein Zitronen- und ein Orangenbonbon verschenkt werden, ist $\\frac{4}{7}$. Ermittle die Anzahl der Orangenbonbons.',
  '2 · k/8 · (8 − k)/7 = 4/7 ⇒ k² − 8k + 16 = 0 ⇒ k = 4', 'ganz', 'III', 'andere Zahlen (Original sechs Bonbons, 3/5; k = 3)', iqb_stelle='A2b')
z(E, 'Wahrscheinlichkeit gesucht', '2019-be-gk-B4.2f', 'In einer Urne liegen 6 schwarze und 4 weiße Kugeln; 6 werden mit einem Griff gezogen. Die Zahl der schwarzen Kugeln gibt an, an wie vielen Tagen der Woche jemand den Müll hinunterbringt. Bestimme die Wahrscheinlichkeit, dass das weniger als viermal ist, und begründe den Ansatz.',
  'höchstens 4 weiße ⇒ mindestens 2 schwarze ⇒ P = [(6 über 2) · (4 über 4) + (6 über 3) · (4 über 3)]/(10 über 6) = 95/210 = 19/42 ≈ 0,452', 'bruch', 'III',
  'andere Zahlen (Original 5 und 5, sieben Kugeln; 1/2)')

# ===================== AS30 Vierfeldertafel =====================
E = 'Vierfeldertafel'
VF = lambda a, b: '\\vierfeldertafel{%s}{%s}{}' % (a, b)
z(E, 'Tafel ausfüllen', '2023-bebb-gk-B4.1a', LEHR + ' Stelle den Sachverhalt in einer vollständig ausgefüllten Vierfeldertafel dar.',
  'W ∩ G 0,20; W ∩ nicht G 0,45; nicht W ∩ G 0,10; nicht W ∩ nicht G 0,25 | Ränder W 0,65, nicht W 0,35, G 0,30, nicht G 0,70', 'dezimal', 'I',
  'andere Zahlen (Original 25 %, 15 %, 72 %)', grafik=VF('G', 'W'), form='einzeichnen')
z(E, 'Tafel ausfüllen', '2024-bebb-gk-B4.1b', TM + ' Stelle den Sachverhalt in einer vollständigen Vierfeldertafel dar.',
  'T ∩ M 0,24; nicht T ∩ M 0,06; T ∩ nicht M 0,46; nicht T ∩ nicht M 0,24 | Ränder T 0,7, nicht T 0,3, M 0,3, nicht M 0,7', 'dezimal', 'I',
  'andere Zahlen (Original 60 %, 20 %, 0,05)', grafik=VF('T', 'M'), form='einzeichnen')
z(E, 'Tafel ausfüllen', '2022-bebb-gk-B4h', PAKET + ' Unter den Paketen mit dem Ziel A ($Z$) sind 10 % schwer. Stelle den Sachverhalt in einer vollständigen Vierfeldertafel dar.',
  'S ∩ Z = 0,12 · 0,10 = 0,012; S ∩ nicht Z 0,048; nicht S ∩ Z 0,108; nicht S ∩ nicht Z 0,832 | Ränder S 0,06, nicht S 0,94, Z 0,12, nicht Z 0,88', 'dezimal', 'II',
  'andere Zahlen (Original 5 %, 10 %, 8 %)', grafik=VF('Z', 'S'), form='einzeichnen')
z(E, 'Wahrscheinlichkeit aus der Tafel gesucht', '2023-bebb-gk-B4.1b', LEHR + ' Ermittle mit deiner Vierfeldertafel die Wahrscheinlichkeit, dass eine zufällig ausgewählte Lehrkraft weiblich ist oder an einem Gymnasium arbeitet.',
  'P(nicht W ∩ nicht G) = 0,25 ⇒ P(W ∪ G) = 1 − 0,25 = 0,75 = 75 %', 'dezimal', 'I', 'andere Zahlen (Original 82 %)')
z(E, 'Wahrscheinlichkeit aus der Tafel gesucht', '2024-bebb-gk-B4.1c', TM + ' Ermittle mit deiner Vierfeldertafel die Wahrscheinlichkeit, dass eine zufällig ausgewählte Person entweder Treuekunde oder Morgenkunde ist.',
  '0,46 + 0,06 = 0,52 = 52 %', 'dezimal', 'I', 'andere Zahlen (Original 50 %)')
z(E, 'Wahrscheinlichkeit aus der Tafel gesucht', '2022-bebb-gk-A1.7b', REISE + ' Berechne den Anteil der Kunden, die entweder nach A oder nach B gerne reisen.',
  '0,5 + 0,4 − 2 · 0,15 = 0,6 = 60 %', 'dezimal', 'II', 'andere Zahlen (Original 60 %, 30 %, 20 %; 50 %)')
z(E, 'Unabhängigkeit prüfen', '2024-bebb-gk-B4.1d', TM + ' Untersuche, ob $T$ und $M$ stochastisch unabhängig sind.',
  'P(T) · P(M) = 0,7 · 0,3 = 0,21 ≠ 0,24 = P(T ∩ M) ⇒ nicht unabhängig', 'dezimal', 'II', 'andere Zahlen (Original 0,12 ≠ 0,15)')
z(E, 'Unabhängigkeit prüfen', '2022-bebb-gk-B4i', PAKET + ' Unter den Paketen mit dem Ziel A ($Z$) sind 10 % schwer. Untersuche, ob der Anteil der Pakete mit Ziel A unter den schweren Paketen ebenso groß ist wie unter den nicht schweren.',
  'P_S(Z) = 0,012/0,06 = 0,2; P_nicht S(Z) = 0,108/0,94 ≈ 0,115 ⇒ nicht gleich ⇒ S und Z nicht unabhängig', 'dezimal', 'III',
  'Nebenplatz (Hauptplatz Bedingte Wahrscheinlichkeit, Gliederung „neben“); andere Zahlen (Original 0,16 und 0,097)', nr=2)
# Mehr AS30
z(E, 'Tafel ausfüllen', '2026MgrundlegendBStochastikWTR2-1a', 'Von den Songs einer Playlist sind 35 % Hip-Hop ($H$), 45 % sind mindestens 4 Minuten lang ($L$), und $P(H \\cap L) = 0{,}15$. Ergänze die fehlenden Wahrscheinlichkeiten der Vierfeldertafel.',
  'H ∩ L 0,15; nicht H ∩ L 0,30; H ∩ nicht L 0,20; nicht H ∩ nicht L 0,35', 'dezimal', 'I', 'andere Zahlen (Original 32 %, 40 %, 0,14)', grafik=VF('H', 'L'), form='einzeichnen', iqb_stelle='B2.1a')
z(E, 'Tafel ausfüllen', '2018-be-gk-B3.2e', 'Bei einem Bildschirm ist das Display mit 12,4 % defekt ($D$), das Netzteil mit 3,5 % ($N$); mit 85,4 % ist keines von beiden defekt. Stelle den Sachverhalt in einer vollständigen Vierfeldertafel dar.',
  'D ∩ N 0,013; D ∩ nicht N 0,111; nicht D ∩ N 0,022; nicht D ∩ nicht N 0,854', 'dezimal', 'I', 'andere Zahlen (Original 10,7 %, 3,0 %, 87,3 %)', grafik=VF('D', 'N'), form='einzeichnen')
z(E, 'Tafel ausfüllen', '2025MgrundlegendBStochastikWTR3-1a', 'Von den Mitgliedern eines Vereins sind 70 % jünger als 50 Jahre ($J$); 20 % sind jünger als 50 und leben nicht in einer Großstadt; 68 % leben in einer Großstadt ($G$). Stelle den Sachverhalt in einer vollständigen Vierfeldertafel dar.',
  'G ∩ J 0,50; nicht G ∩ J 0,20; G ∩ nicht J 0,18; nicht G ∩ nicht J 0,12', 'dezimal', 'I', 'andere Zahlen (Original 72 %, 18 %, 75 %)', grafik=VF('G', 'J'), form='einzeichnen', iqb_stelle='B3.1a')
z(E, 'Tafel ausfüllen', '2024MgrundlegendBStochastikWTR2-1b', '60 % der Schüler besitzen einen Laptop ($L$), 30 % einen Desktop-PC ($D$), 25 % keines von beiden. Stelle die Vierfeldertafel auf und gib die Wahrscheinlichkeit an, dass jemand einen Laptop, aber keinen Desktop-PC besitzt.',
  'L ∩ D 0,15; L ∩ nicht D 0,45; nicht L ∩ D 0,15; nicht L ∩ nicht D 0,25 | P(L ∩ nicht D) = 0,45', 'dezimal', 'II', 'andere Zahlen (Original 56 %, 33 %, 28 %)', grafik=VF('L', 'D'), form='einzeichnen', iqb_stelle='B2.1b')
z(E, 'Tafel ausfüllen', '2019-be-gk-B4.1c', 'Von 12 500 Prüflingen einer Fahrprüfung waren 2 600 mindestens 30 Jahre alt ($A$); 10 000 haben bestanden ($B$), davon 7 700 jünger als 30. Bestimme die Anzahl der Prüflinge, die jünger als 30 waren und nicht bestanden haben.',
  'jünger als 30: 12 500 − 2 600 = 9 900 ⇒ 9 900 − 7 700 = 2 200', 'ganz', 'I', 'andere Zahlen (Original 13 879, 2 482, 11 104, 8 870; 2 527)')
z(E, 'Wahrscheinlichkeit aus der Tafel gesucht', '2020MgrundlegendAStochastik12-a', 'Bei einem Fest sind 50 % der Gäste Erwachsene; 15 % aller Gäste sind verkleidete Erwachsene, und 70 % der Jugendlichen sind verkleidet. Bestimme den Anteil der nicht Verkleideten unter allen Gästen.',
  'verkleidet: 0,15 + 0,7 · 0,5 = 0,5 ⇒ nicht verkleidet 0,5 = 50 %', 'dezimal', 'I', 'andere Zahlen (Original 60 %, 12 %, 75 %; 58 % verkleidet)', iqb_stelle='A12a')
z(E, 'Wahrscheinlichkeit aus der Tafel gesucht', '2025MgrundlegendBStochastikWTR3-1b', 'Von den Mitgliedern eines Vereins sind 70 % jünger als 50 Jahre ($J$); 20 % sind jünger als 50 und leben nicht in einer Großstadt; 68 % leben in einer Großstadt ($G$). Beurteile die Aussage: Weniger als 60 % leben entweder in einer Großstadt oder sind nicht jünger als 50.',
  'entweder G oder nicht J: G ∩ J + nicht G ∩ nicht J = 0,50 + 0,12 = 0,62 > 0,6 ⇒ falsch', 'dezimal', 'II', 'andere Zahlen (Original 0,61)', iqb_stelle='B3.1b')
z(E, 'Unabhängigkeit prüfen', '2019-be-gk-B4.1d', 'Von 12 500 Prüflingen einer Fahrprüfung waren 2 600 mindestens 30 Jahre alt ($A$); 10 000 haben bestanden ($B$), davon 7 700 jünger als 30. Untersuche, ob $P_A(B)$ und $P(B)$ übereinstimmen, ob $A$ und $B$ stochastisch unabhängig sind, und deute das Ergebnis.',
  'bestanden ab 30: 10 000 − 7 700 = 2 300 ⇒ P_A(B) = 2 300/2 600 ≈ 0,885 ≠ P(B) = 0,8 ⇒ abhängig; Ältere bestehen häufiger', 'dezimal', 'II', 'andere Zahlen (Original 0,900 und 0,800)')
z(E, 'Unabhängigkeit prüfen', '2023MgrundlegendBStochastikWTR1-2e', 'Ein Kaffeesack hat zu viele Verunreinigungen ($M_1$) mit 2 % und wiegt weniger als 60 kg ($M_2$); beide Mängel sind unabhängig. $P(\\overline{M_1} \\cap M_2) = 4{,}9\\,\\%$. Ermittle $P(M_2)$.',
  '0,98 · P(M₂) = 0,049 ⇒ P(M₂) = 0,05 = 5 %', 'dezimal', 'III', 'andere Zahlen (Original 1 %, 3 %; 3,03 %)', iqb_stelle='B1.2e')

# ===================== AS40 Bedingte Wahrscheinlichkeit =====================
E = 'Bedingte Wahrscheinlichkeit'
FX = '\\begin{abiksys}[xmin=0,xmax=0.16,ymin=0,ymax=0.6,xstep=0.02,ystep=0.1,le=50,yle=8]\\funktion[0.03]{0.315*(0.142-\\x)/(0.315*(0.142-\\x)+0.685*0.055)}{G_f}\\end{abiksys}'
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2022-bebb-gk-A1.7a', REISE + ' Bestimme die Wahrscheinlichkeit, dass ein zufällig ausgewählter A-Kunde auch gerne nach B reist.',
  '0,15/0,5 = 0,3', 'dezimal', 'I', 'andere Zahlen (Original 0,2/0,6 = 1/3)')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2023-bebb-gk-B4.1c', LEHR + ' Eine zufällig ausgewählte Lehrkraft ist weiblich. Bestimme die Wahrscheinlichkeit, dass sie an einem Gymnasium arbeitet.',
  '0,20/0,65 ≈ 0,308 ≈ 31 %', 'dezimal', 'I', 'andere Zahlen (Original 0,15/0,72 ≈ 21 %)')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2022-bebb-gk-B4i', PAKET + ' Unter den Paketen mit dem Ziel A ($Z$) sind 10 % schwer. Untersuche, ob der Anteil der Pakete mit Ziel A unter den schweren Paketen ebenso groß ist wie unter den nicht schweren.',
  'S ∩ Z = 0,012; nicht S ∩ Z = 0,108 ⇒ P_S(Z) = 0,012/0,06 = 0,2; P_nicht S(Z) = 0,108/0,94 ≈ 0,115 ⇒ nicht gleich', 'dezimal', 'II',
  'andere Zahlen (Original 0,16 und 0,097)')
z(E, 'bedingte Wahrscheinlichkeit mit Parameter', '2025-bebb-gk-B4e', HH + ' Zwei Jahre später sind die Anteile ohne Kind unverändert; unter den Haushalten mit Kind ist der Anteil der überbelegten um $x$ gesunken. Die Funktion $f$ mit $f(x) = \\frac{0{,}315 \\cdot (0{,}142 - x)}{0{,}315 \\cdot (0{,}142 - x) + 0{,}685 \\cdot 0{,}055}$, $0 \\le x \\le 0{,}142$, ist abgebildet. Bestimme grafisch $x$ mit $f(x) = 0{,}4$ und deute $x$ und $f(x)$ im Sachzusammenhang.',
  'x ≈ 0,06 (grafisch, rechnerisch 0,062) | x: Rückgang des Anteils überbelegter Haushalte unter denen mit Kind; f(x) = P_B(K) = 40 %: Anteil der Haushalte mit Kind unter den überbelegten', 'dezimal', 'III',
  'andere Zahlen (Original 0,285, 0,159, 0,065; x ≈ 0,05); Graph wie im Original, Fenster bis 0,16', grafik=FX, form='karo')
z(E, 'bedingte Wahrscheinlichkeit mit Parameter', '2026-bb-gk-B4f', TREUE + ' Ein Jahr später sammeln weiterhin 80 % Treuepunkte, davon 70 % weiblich; der Anteil $a$ ist gestiegen. Beurteile die Aussage: Die Wahrscheinlichkeit, dass eine nicht weibliche Person Treuepunkte sammelt, ist größer als vor einem Jahr.',
  'P_nicht w(T) = 0,8 · 0,3/(0,8 · 0,3 + 0,2 · (1 − a)); a steigt ⇒ Nenner fällt ⇒ Quotient steigt ⇒ wahr', 'dezimal', 'III',
  'andere Zahlen (Original 75 %, 80 %)', grafik=BAUM_T, form='karo')
z(E, 'Terme deuten', '2022-bebb-gk-B4g', PAKET + ' Unter den Paketen mit dem Ziel A ($Z$) sind 10 % schwer. Gib die Bedeutung der Terme $P_Z(S)$ und $P(S \\cap Z)$ im Sachzusammenhang an.',
  'P_Z(S): Wahrscheinlichkeit, dass ein Paket mit Ziel A schwer ist (10 %) | P(S ∩ Z): Wahrscheinlichkeit, dass ein Paket schwer ist und Ziel A hat (0,12 · 0,10 = 1,2 %)', 'dezimal', 'I',
  'andere Zahlen (Original 8 %, 0,8 %)', form='karo')
z(E, 'Terme deuten', '2024-bebb-gk-B4.1a', TM + ' Deute die Gleichung im Sachzusammenhang.',
  'Die Wahrscheinlichkeit, dass eine zufällig ausgewählte Person Morgenkunde und kein Treuekunde ist, beträgt 6 %', 'dezimal', 'I',
  'andere Zahlen (Original 0,05)', form='karo')
# Mehr AS40
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2018-be-gk-B3.2f', 'Bei einem Bildschirm sind Display und Netzteil mit 1,3 % beide defekt; das Display ist mit 12,4 % defekt. Berechne die Wahrscheinlichkeit, dass ein Bildschirm mit defektem Display auch ein defektes Netzteil hat.',
  'P_D(N) = 0,013/0,124 ≈ 0,105 ≈ 10,5 %', 'dezimal', 'I', 'andere Zahlen (Original 1,0 %, 10,7 %; 9,3 %)')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2026MgrundlegendBStochastikWTR2-1b', 'Von den Songs einer Playlist sind 35 % Hip-Hop ($H$); $P(H \\cap L) = 0{,}15$, wobei $L$ heißt: mindestens 4 Minuten lang. Berechne $P_H(L)$.',
  '0,15/0,35 ≈ 0,429 ≈ 42,9 %', 'dezimal', 'I', 'andere Zahlen (Original 0,14/0,32 ≈ 43,8 %)', iqb_stelle='B2.1b')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2024MgrundlegendBStochastikWTR2-1c', '60 % der Schüler besitzen einen Laptop ($L$), 30 % einen Desktop-PC ($D$), 15 % beides. Berechne $P_D(L)$.',
  '0,15/0,3 = 0,5', 'dezimal', 'I', 'andere Zahlen (Original 0,17/0,33 ≈ 0,52)', iqb_stelle='B2.1c')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2017-be-gk-B3.1d', 'Ein Gerät wird in vier Werken hergestellt: Werk A liefert 20 %, B 30 %, C 10 % und D 40 % aller Geräte; in A sind 4 % fehlerhaft. Insgesamt sind 3,1 % aller Geräte fehlerhaft. Ein zufällig ausgewähltes Gerät ist fehlerhaft. Berechne die Wahrscheinlichkeit, dass es aus Werk A stammt.',
  'P(A ∩ F) = 0,2 · 0,04 = 0,008 ⇒ P_F(A) = 0,008/0,031 ≈ 0,258', 'dezimal', 'II', 'andere Zahlen (Original 10 %, 5 %, 3 %; 1/6)')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2026MgrundlegendAStochastik13-b', 'Ein Versandhändler verschickt 50 % seiner Sendungen mit dem Unternehmen A; 12 % aller Sendungen gehen mit A und kommen verspätet, 12,5 % gehen nicht mit A und kommen verspätet. Eine Sendung kommt verspätet. Untersuche, ob die Wahrscheinlichkeit, dass sie nicht mit A verschickt wurde, größer als 50 % ist.',
  '0,125/(0,12 + 0,125) = 0,125/0,245 ≈ 0,51 > 0,5 ⇒ ja', 'dezimal', 'II', 'andere Zahlen (Original 0,08 und 0,18; 0,69)', iqb_stelle='A13b')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2020-be-gk-B4.2f', 'In einem Betrieb ist ein Viertel der Beschäftigten weiblich ($w$); 4 % der weiblichen und 12 % der übrigen Beschäftigten sind unzufrieden ($u$). Eine zufällig ausgewählte Person ist unzufrieden. Bestimme die Wahrscheinlichkeit, dass sie nicht weiblich ist.',
  'P(nicht w ∩ u) = 0,75 · 0,12 = 0,09; P(u) = 0,01 + 0,09 = 0,1 ⇒ P_u(nicht w) = 0,9', 'dezimal', 'II', 'andere Zahlen (Original 1/3, 3,5 %, 10,5 %; 0,857)')
z(E, 'bedingte Wahrscheinlichkeit gesucht', '2022MgrundlegendBStochastikWTR2-1c', 'Ein Viertel aller Menschen infiziert sich im Laufe des Lebens mit einem Bakterium; bei 10 % der Infizierten bricht die Krankheit aus, bei Nichtinfizierten nie. Bei einer Person bricht die Krankheit nicht aus. Bestimme die Wahrscheinlichkeit, dass sie sich infiziert hat.',
  '0,25 · 0,9/(0,25 · 0,9 + 0,75) = 0,225/0,975 ≈ 0,231', 'dezimal', 'II', 'andere Zahlen (Original 1/3, 8 %; 31,5 %)', iqb_stelle='B2.1c')
z(E, 'Terme deuten', '2020MgrundlegendAStochastik12-b', 'Bei einem Fest sind 50 % der Gäste Erwachsene; 15 % aller Gäste sind verkleidete Erwachsene, 70 % der Jugendlichen sind verkleidet. Beschreibe die Bedeutung des Terms $\\frac{0{,}15}{0{,}15 + 0{,}7 \\cdot 0{,}5}$ im Sachzusammenhang.',
  'Anteil der Erwachsenen unter allen Verkleideten (Wert 0,3)', 'dezimal', 'I', 'andere Zahlen (Original 0,12/(0,12 + 0,75 · 0,4))', form='karo', iqb_stelle='A12b')
z(E, 'Terme deuten', '2021MgrundlegendAStochastik11-b', '20 % der Menschen haben Heuschnupfen; ein Test ist bei ihnen mit 90 % positiv, bei den übrigen mit 3 %. Deute den Term $\\frac{0{,}2 \\cdot 0{,}9}{0{,}2 \\cdot 0{,}9 + 0{,}8 \\cdot 0{,}03}$ im Sachzusammenhang.',
  'Wahrscheinlichkeit, dass eine Person mit positivem Test tatsächlich Heuschnupfen hat (Wert ≈ 0,882)', 'dezimal', 'II', 'andere Zahlen (Original 15 %, 90 %, 2 %)', form='karo', iqb_stelle='A11b')

# ===================== AS50 Term und Anteil am Baum =====================
E = 'Term und Anteil am Baum'
z(E, 'Ereignis zum Term gesucht', '2025-bebb-gk-A1.3a', RAD8 + ' Es wird zweimal gedreht. Deute den Term $\\left(\\frac{2}{8}\\right)^2$ im Sachzusammenhang.',
  'Wahrscheinlichkeit, bei zweimaligem Drehen zweimal die 2 zu erhalten', 'bruch', 'I', 'andere Zahlen (Original (3/8)², zweimal die 6)', grafik=RAD8_G, form='karo')
z(E, 'Ereignis zum Term gesucht', '2024-bebb-gk-A1.6b', GLITZ + ' Beschreibe ein Zufallsexperiment und ein Ereignis, dessen Wahrscheinlichkeit der Term $\\left(\\frac{7}{10}\\right)^4 + 4 \\cdot \\left(\\frac{7}{10}\\right)^3 \\cdot \\frac{3}{10}$ angibt.',
  'vier Kinder erhalten je einen Ball; Ereignis: mindestens drei Bälle sind nicht glitzernd', 'bruch', 'II', 'andere Zahlen (Original 40 %, (3/5)⁴ + 4 · (3/5)³ · 2/5)', form='karo')
z(E, 'Ereignis zum Term gesucht', '2025-bebb-gk-A1.6b', SCHW + ' Gib die Bedeutung des Terms $\\frac{\\binom{6}{2} \\cdot \\binom{10}{3}}{\\binom{16}{5}}$ im Sachzusammenhang an.',
  'Wahrscheinlichkeit, dass unter fünf zufällig ausgewählten Kindern genau zwei das Abzeichen Bronze haben', 'bruch', 'II', 'andere Zahlen (Original (9 über 2)(11 über 4)/(20 über 6))', form='karo')
z(E, 'unbekannter Anteil gesucht', '2024-bebb-gk-A1.9b', BEF + ' Von 1 000 Befragten antworten 360 mit Ja. Berechne auf dieser Grundlage den Anteil $p$.',
  '0,7p + 0,3 · (1 − p) = 0,36 ⇒ 0,4p = 0,06 ⇒ p = 0,15', 'dezimal', 'II', 'andere Zahlen (Original 60 %, 420; p = 0,1)',
  grafik='\\baumabi{F_1/{0,7}/{\\text{Ja}/{p},\\text{Nein}/{1-p}},F_2/{0,3}/{\\text{Ja}/{1-p},\\text{Nein}/{p}}}')
z(E, 'unbekannter Anteil gesucht', '2026-bb-gk-B4e', TREUE + ' Der Anteil der nicht weiblichen Personen in der Kundschaft beträgt 34 %. Berechne $a$.',
  '0,8 · 0,3 + 0,2 · (1 − a) = 0,34 ⇒ 0,44 − 0,2a = 0,34 ⇒ a = 0,5', 'dezimal', 'II', 'andere Zahlen (Original 75 %, 80 %, 30 %; a = 0,4)', grafik=BAUM_T)
z(E, 'unbekannter Anteil gesucht', '2022-bebb-gk-B4j', PAKET + ' Unter den Paketen mit Ziel A sind 10 % schwer, unter denen mit Ziel B 2,5 %. Untersuche, ob der Anteil schwerer Pakete unter denen mit anderem Ziel kleiner, gleich oder größer als 6 % ist.',
  '0,06 = 0,12 · 0,10 + 0,08 · 0,025 + 0,80 · x ⇒ x = 0,046/0,8 = 0,0575 < 0,06 ⇒ kleiner', 'dezimal', 'III', 'andere Zahlen (Original 5 %, 10 %, 8 %, 7 %, 2 %; x ≈ 0,049)')
# Mehr AS50
z(E, 'Ereignis zum Term gesucht', '2025MgrundlegendAStochastik11-b', 'In einem Computerspiel wird der Startpunkt A mit 30 % zugewiesen, sonst B. Wer bei A startet, trifft mit 60 % auf einen bestimmten Charakter; bei 49 % aller Spiele startet man bei B und trifft auf ihn. Gib ein Ereignis an, dessen Wahrscheinlichkeit der Term $1 - (0{,}3 \\cdot 0{,}6 + 0{,}49)$ angibt.',
  'Man trifft im Spiel nicht auf den Charakter (Wert 0,33)', 'dezimal', 'I', 'andere Zahlen (Original 1 − (0,4 · 0,8 + 0,42))', form='karo', iqb_stelle='A11b')
z(E, 'Ereignis zum Term gesucht', '2019MgrundlegendBStochastikWTR3-2a', 'In einer Urne liegen fünf Kugeln: zwei mit der Zahl 4, drei mit einer anderen Zahl. Gib ein Zufallsexperiment und ein Ereignis an, dessen Wahrscheinlichkeit der Term $1 - 0{,}4^3$ angibt.',
  'dreimal mit Zurücklegen ziehen; Ereignis: nicht jedes Mal die 4 (Wert 0,936)', 'dezimal', 'II', 'andere Zahlen (Original drei mit 4; 1 − 0,6³)', form='karo', iqb_stelle='B3.2a')
z(E, 'Ereignis zum Term gesucht', '2021-be-gk-B4f', 'Bei einem Spiel gibt es je Versuch mit 30 % einen Stern; $X$ ist die Anzahl der Sterne bei zwölf Versuchen. Gib Werte für $a$ und $b$ an, sodass $1 - (a^{12} + 12 \\cdot 0{,}3 \\cdot a^b)$ eine Wahrscheinlichkeit im Sachzusammenhang ist, und beschreibe das Ereignis.',
  'a = 0,7, b = 11; Ereignis: mindestens zwei Sterne bei zwölf Versuchen (≈ 0,915)', 'dezimal', 'III', 'andere Zahlen (Original 40 %, zehn Versuche)', form='karo')
z(E, 'unbekannter Anteil gesucht', '2020-be-gk-B4.2g', 'In einer Abteilung sind 5 % der weiblichen und 10 % der übrigen Beschäftigten unzufrieden. Der Anteil der unzufriedenen nicht weiblichen Beschäftigten ist dreimal so groß wie der der unzufriedenen weiblichen. Bestimme den Anteil der weiblichen Beschäftigten.',
  '3 · a · 0,05 = (1 − a) · 0,1 ⇒ 0,25a = 0,1 ⇒ a = 0,4', 'dezimal', 'II', 'andere Zahlen (Original 4 %, 10 %, fünfmal; 1/3)')
z(E, 'unbekannter Anteil gesucht', '2019-be-gk-B4.1e', 'Der Anteil der Prüflinge, die beim ersten Mal bestehen, ist $q$. Wer nicht besteht, tritt ein zweites Mal an und besteht dann mit dem Anteil $\\frac{q}{2}$. Insgesamt bestehen 84 % spätestens beim zweiten Mal. Berechne $q$.',
  'q + (1 − q) · q/2 = 0,84 ⇒ q² − 3q + 1,68 = 0 ⇒ q ≈ 0,745 (zweite Lösung ≈ 2,255 entfällt)', 'dezimal', 'III', 'andere Zahlen (Original 90 %; q ≈ 0,829)')
schreibe(sys.argv[1], Z)
print(len(Z), 'Zeilen')

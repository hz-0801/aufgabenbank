#!/usr/bin/env python3
"""Erzeugt mathe-nachhilfe/abitur/mehr-abi-gk/binomialverteilung.csv (AS60, AS70, AS80).
Säulenhöhen aus scipy; Kontrolle der Lösungen in src/rechne.py der Blätter."""
import csv, sys
from scipy.stats import binom as B

ZIEL = sys.argv[1]
SP = ('id;marke;quelle;kapitel;einheit;stufe;art;eltern_id;auf_blatt;wortlaut;abbildung;loesung;pruef;zahlart;'
      'schwere;rang;bemerkung;grafik;form;buendel;wortlaut_einheit;loesung_einheit;pruef_einheit;grafik_einheit;'
      'form_einheit').split(';')
NR = 'nachgerechnet (sympy, src/rechne.py)'


def saeulen(n, p, kmax=None, kmin=0, ymax=0.3, ystep=0.05, yfein=0.01, hoehe=2.8, breite=0.5, ohne=False, faktor=1.0):
    kmax = n if kmax is None else kmax
    werte = ','.join(f'{k}/{min(B.pmf(k, n, p) * faktor, ymax):.4f}' for k in range(kmin, kmax + 1))
    return (f'\\saeulenab[ymax={ymax},ystep={ystep},yfein={yfein},ylabel={{$P(X=k)$}},hoehe={hoehe},breite={breite}'
            + (',ohnezahlen' if ohne else '') + f']{{{werte}}}')


def tabelle(n, p, ks):
    """Ausschnitt der Tabelle der summierten Binomialverteilung (wie die Anlage im Heft)."""
    kopf = ' & '.join(str(k) for k in ks)
    werte = ' & '.join(f'{B.cdf(k, n, p):.4f}'.replace('.', ',') for k in ks)
    return ('{\\small\\begin{tabular}{|l|' + 'c|' * len(ks) + '}\\hline '
            + f'\\multicolumn{{{len(ks) + 1}}}{{|c|}}{{$n = {n}$, $p = {str(p).replace(".", "{,}")}$}}\\\\\\hline '
            + f'$k$ & {kopf}\\\\\\hline $P(X \\le k)$ & {werte}\\\\\\hline\\end{{tabular}}}}')


Z = []


def z(eid, einheit, stufe, auf_blatt, wortlaut, loesung, schwere, rang, bemerkung, zahlart='dezimal', grafik='',
      form='', marke=None, quelle=None, id_=None):
    if 'Mgrundlegend' in eid:   # IQB-Pool: 2021MgrundlegendAStochastik2-a -> 2021-iqb-ga-A2a
        import re
        j = eid[:4]
        m = re.match(r'^\d{4}Mgrundlegend([AB])(?:Stochastik)(?:WTR|CAS)?(\d+)-?(\d*)-?([a-z]?)$', eid)
        a, x, y, t = m.groups()
        stelle = f'{a}{x}{"." + y if y else ""}{t}' if a == 'B' else f'{a}{x}{y}{t}'
        id_ = id_ or f'{j}-iqb-ga-{stelle}-m1'
        marke = marke or f'IQB ’{j[2:]}'
        quelle = quelle or f'IQB GK {j} · {stelle}'
    else:
        j, stelle = eid[:4], eid.split('-gk-')[1]
        id_ = id_ or f'{eid}-m1'
        marke = marke or f'GK ’{j[2:]}'
        quelle = quelle or f'Abi GK {j} · {stelle}'
    Z.append({'id': id_, 'marke': marke, 'quelle': quelle, 'kapitel': 'binomialverteilung', 'einheit': einheit,
              'stufe': stufe, 'art': 'mehr', 'eltern_id': eid, 'auf_blatt': auf_blatt, 'wortlaut': wortlaut,
              'abbildung': '', 'loesung': loesung, 'pruef': '', 'zahlart': zahlart, 'schwere': schwere,
              'rang': str(rang), 'bemerkung': bemerkung, 'grafik': grafik, 'form': form})


# Gemeinsame Vorspänne (eine Zahlenwahl je Original-Aufgabe, pruefung.md § 5 „Andere Zahlen“)
TREUE = ('In einem Supermarkt sammeln 80 % der Kundschaft Treuepunkte. Es werden 12 Personen aus der Kundschaft '
         'zufällig ausgewählt; die Zufallsgröße $X$ gibt an, wie viele davon Treuepunkte sammeln. $X$ wird als '
         'binomialverteilt angenommen. ')
PAKET = ('In einem Paketzentrum werden täglich mehrere Millionen Pakete umgeschlagen. Von allen Paketen gehen 12 % '
         'zum Ziel A und 8 % zum Ziel B, die übrigen an andere Ziele. ')
LEHR = ('In einem Land arbeiten 30 % aller Lehrkräfte an einem Gymnasium; 20 % aller Lehrkräfte sind weiblich und '
        'arbeiten an einem Gymnasium, insgesamt sind 65 % der Lehrkräfte weiblich. ')
HAUS = ('In einer Großstadt gelten 8,24 % aller Haushalte als überbelegt. Es werden 800 Haushalte zufällig '
        'ausgewählt; die Zufallsgröße $X$ gibt die Anzahl der überbelegten Haushalte unter ihnen an und wird als '
        'binomialverteilt angenommen. ')
SYM19 = ('Die Abbildung zeigt die Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße $X$ mit der '
         'Trefferwahrscheinlichkeit $p = 0{,}5$ und unbekanntem $n$. Die beiden höchsten Säulen bei $k = 9$ und '
         '$k = 10$ sind gleich hoch. ')
D16 = ('Die Abbildung zeigt die Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße $X$ mit '
       '$n = 16$ und unbekannter Trefferwahrscheinlichkeit $p$. ')

# ---------------------------------------------------------------- AS60 Bernoulli-Kette
E, S1, S2 = 'Bernoulli-Kette', 'Bernoulli-Kette erkennen', 'Term deuten'
z('2026-bb-gk-A1.3a', E, S1, 'ja',
  'Eine Münze mit den Seiten Zahl (Z) und Wappen (W) wird sechsmal geworfen; ein Ergebnis ist eine Abfolge wie '
  'ZWZZWZ. Ereignis $A$: Es wird höchstens einmal Wappen geworfen. Gib einen Term an, mit dem man $P(A)$ berechnen '
  'kann.',
  'höchstens einmal W = keinmal oder genau einmal ⇒ P(A) = (1/2)⁶ + 6 · (1/2) · (1/2)⁵ = 7/64',
  'I', 1, f'andere Zahlen (Original fünf Würfe, 3/16); {NR}', 'bruch')
z('2026-bb-gk-B4a', E, S1, 'ja',
  TREUE + 'Für ein Ereignis gilt $P(X = a) = \\binom{b}{4} \\cdot c^4 \\cdot 0{,}2^8$. Gib die Werte von $a$, $b$ und '
  '$c$ an und beschreibe das Ereignis im Sachzusammenhang.',
  'n = 12, Treffer = sammelt, p = 0,8 ⇒ a = 4 | b = 12 | c = 0,8 | Ereignis: genau 4 der 12 Personen sammeln '
  'Treuepunkte',
  'I', 2, f'andere Zahlen (Original 75 %, n = 10, (b über 3) · c³ · 0,25⁷); {NR}')
z('2022-bebb-gk-B4a', E, S1, 'ja',
  PAKET + 'Es werden 100 Pakete zufällig ausgewählt und darauf untersucht, ob sie das Ziel B haben. Begründe, dass '
  'man die Anzahl der Pakete mit dem Ziel B als binomialverteilt annehmen kann.',
  'je Paket zwei Ausgänge (Ziel B oder nicht); feste Anzahl n = 100; p = 0,08 bleibt bei Millionen Paketen praktisch '
  'gleich, die Pakete sind unabhängig ⇒ Bernoulli-Kette, also binomialverteilt',
  'II', 3, f'andere Zahlen (Original 10 % und 7 %); {NR}', 'ganz')
z('2023-bebb-gk-B4.1e', E, S2, 'ja',
  LEHR + 'Es werden 100 Lehrkräfte zufällig ausgewählt; $X$ ist die Anzahl derer, die nicht an einem Gymnasium '
  'arbeiten. Gib an, was mit dem Term $\\sum_{k=70}^{100} \\binom{100}{k} \\cdot 0{,}7^k \\cdot 0{,}3^{100-k}$ '
  'im Sachzusammenhang berechnet wird.',
  'Summe von k = 70 bis 100 mit p = 0,7 ⇒ P(X ≥ 70) ≈ 0,549 | Wahrscheinlichkeit, dass höchstens 30 der 100 '
  'Lehrkräfte an einem Gymnasium arbeiten',
  'II', 4, f'andere Zahlen (Original 25 % Gymnasium, Summe ab 75 mit 0,75); {NR}', 'ganz')
z('2023-bebb-gk-B4.1d', E, S2, 'ja',
  LEHR + 'Es werden 100 Lehrkräfte zufällig ausgewählt; $X$ ist die Anzahl derer, die nicht an einem Gymnasium '
  'arbeiten. Bestimme die Wahrscheinlichkeit dafür, dass unter den 100 die Anzahl derer, die nicht an einem '
  'Gymnasium arbeiten, mindestens dreimal so groß ist wie die Anzahl derer, die an einem Gymnasium arbeiten.',
  'X ~ B(100; 0,7); X ≥ 3 · (100 − X) ⇔ 4X ≥ 300 ⇔ X ≥ 75 ⇒ P(X ≥ 75) = 1 − P(X ≤ 74) ≈ 0,163',
  'II', 5, f'andere Zahlen (Original 25 %, „viermal“, X ≥ 80, ≈ 0,149); {NR}')
# Mehr AS60
z('2017-be-gk-B3.1f', E, S2, 'nein',
  'In einem Werk sind 3 % der hergestellten Smartphones fehlerhaft. Gegeben ist der Term '
  '$150 \\cdot 0{,}97^s \\cdot 0{,}03 + 0{,}97^{150}$. Gib einen Wert von $s$ an, für den der Term im '
  'Sachzusammenhang die Wahrscheinlichkeit eines Ereignisses angibt, und beschreibe dieses Ereignis.',
  '0,97¹⁵⁰ = P(X = 0) und 150 · 0,03 · 0,97¹⁴⁹ = P(X = 1) bei n = 150 ⇒ s = 149 | Ereignis: unter 150 zufällig '
  'ausgewählten Geräten ist höchstens eines fehlerhaft',
  'II', 6, f'herausgelöst (Original mit Tabelle der Werke); andere Zahlen (Original 2 %, 200, s = 199); {NR}',
  'ganz', marke='nach GK ’17')
z('2019-be-gk-B4.2e', E, S2, 'nein',
  'Zwei Geschwister würfeln jeden Tag einmal mit je einem fairen Würfel. Ist die Augenzahl des älteren kleiner als '
  'die des jüngeren, bringt der ältere den Müll hinunter; das geschieht mit der Wahrscheinlichkeit '
  '$\\frac{5}{12}$. $X$ ist die Anzahl der Tage, an denen der ältere den Müll hinunterbringt, in 24 Tagen. Gib die '
  'Bedeutung des Terms $\\binom{24}{8} \\cdot \\left(\\frac{5}{12}\\right)^8 \\cdot \\left(\\frac{7}{12}\\right)^{16}'
  ' + \\binom{24}{9} \\cdot \\left(\\frac{5}{12}\\right)^9 \\cdot \\left(\\frac{7}{12}\\right)^{15} + '
  '\\binom{24}{10} \\cdot \\left(\\frac{5}{12}\\right)^{10} \\cdot \\left(\\frac{7}{12}\\right)^{14}$ im '
  'Sachzusammenhang an.',
  'Summe P(X = 8) + P(X = 9) + P(X = 10) ⇒ P(8 ≤ X ≤ 10) ≈ 0,436 | der ältere bringt in 24 Tagen mindestens 8-mal '
  'und höchstens 10-mal den Müll hinunter',
  'II', 7, f'andere Zahlen (Original 30 Tage, 10 bis 12); {NR}', 'ganz')
z('2020-be-gk-B4.2b', E, S2, 'nein',
  'In einem großen Unternehmen ist ein Drittel der Beschäftigten weiblich. Es werden 40 Beschäftigte zufällig '
  'ausgewählt; $X$ ist die Anzahl der weiblichen darunter. Gib die Bedeutung der Aussage '
  '$\\binom{40}{12} \\cdot \\left(\\frac{1}{3}\\right)^{12} \\cdot \\left(\\frac{2}{3}\\right)^{28} + '
  '\\binom{40}{13} \\cdot \\left(\\frac{1}{3}\\right)^{13} \\cdot \\left(\\frac{2}{3}\\right)^{27} \\approx 0{,}256$'
  ' im Sachzusammenhang an.',
  'P(12 oder 13) ≈ 0,256 | Die Wahrscheinlichkeit, dass unter den 40 genau 12 oder genau 13 weiblich '
  'sind, beträgt etwa 25,6 %',
  'II', 8, f'andere Zahlen (Original 50 Beschäftigte, 13 und 14, ≈ 0,158); {NR}')
z('2018-be-gk-B3.2g', E, S1, 'nein',
  'Von 30 geprüften Bildschirmen sind 5 fehlerhaft. Aus diesen 30 werden nacheinander 8 zufällig ausgewählt, ohne '
  'sie zurückzulegen. Beurteile, ob die Anzahl der fehlerhaften Bildschirme unter den 8 ausgewählten '
  'binomialverteilt ist.',
  'nein: ohne Zurücklegen ändert sich die Trefferwahrscheinlichkeit von Zug zu Zug (erster Zug 5/30, danach 4/29 '
  'oder 5/29) ⇒ keine Bernoulli-Kette',
  'II', 9, f'andere Zahlen (Original 40, 6, 10); {NR}', 'bruch')
z('2023MgrundlegendBStochastikWTR2-1a', E, S1, 'nein',
  'Ein Würfel trägt auf zwei Seitenflächen die Zahl 5 und auf den übrigen vier Seitenflächen die Zahl 1. Er wird '
  '24-mal geworfen; $X$ ist die Anzahl der Würfe mit einer 5. Begründe, dass $X$ binomialverteilt ist mit '
  '$p = \\frac{1}{3}$.',
  'jeder Wurf hat zwei Ausgänge (5 oder nicht); die Würfe sind unabhängig; n = 24 fest; p = 2/6 = 1/3 bei jedem '
  'Wurf gleich ⇒ Bernoulli-Kette, also binomialverteilt',
  'I', 10, f'IQB-Pool, nicht BB; andere Zahlen (Original Netz mit 2 und 4, 30 Würfe); {NR}', 'bruch')
z('2020MgrundlegendBStochastikWTR2-1a', E, S1, 'nein',
  'Ein Postunternehmen befördert jährlich etwa 50 Millionen Briefe und stellt 92 % davon am ersten Werktag nach '
  'der Einlieferung zu. Für 1500 zufällig ausgewählte Briefe wird untersucht, ob sie am ersten Werktag zugestellt '
  'werden. Begründe, dass man die Anzahl der am ersten Werktag zugestellten Briefe mit der Binomialverteilung '
  'beschreiben kann.',
  'je Brief zwei Ausgänge (zugestellt oder nicht); n = 1500 fest; bei 50 Millionen Briefen ändert die Auswahl '
  'p = 0,92 praktisch nicht, die Briefe sind unabhängig ⇒ Bernoulli-Kette ⇒ Binomialverteilung',
  'II', 11, f'IQB-Pool, nicht BB; andere Zahlen (Original 60 Millionen, 95 %, 2000); {NR}', 'ganz')
z('2021MgrundlegendAStochastik2-a', E, S1, 'nein',
  'Die Zufallsgröße $X$ ist binomialverteilt mit $p = \\frac{1}{3}$. Vervollständige die Gleichung '
  '$P(X = \\square) = \\binom{\\square}{4} \\cdot \\left(\\square\\right)^3 \\cdot \\left(\\frac{1}{3}\\right)^4$.',
  'Hochzahl von 1/3 = Trefferzahl ⇒ X = 4; Hochzahlen 4 + 3 = n ⇒ n = 7; Nieten mit 1 − 1/3 ⇒ Basis 2/3 ⇒ '
  'Kästchen der Reihe nach 4, 7 und 2/3',
  'II', 12, f'IQB-Pool, nicht BB; andere Zahlen (Original p = 1/4, Hochzahlen 2 und 3); {NR}', 'bruch')
z('2024MgrundlegendAStochastik12-a', E, S1, 'nein',
  'Ein Glücksrad hat gleich große Sektoren, 20 % davon sind grün. Es wird zweimal gedreht. Weise nach, dass die '
  'Wahrscheinlichkeit dafür, genau einmal Grün zu erzielen, 32 % beträgt.',
  'zwei Pfade (grün, nicht grün) und (nicht grün, grün) ⇒ P = 2 · 0,2 · 0,8 = 0,32',
  'I', 13, f'IQB-Pool, nicht BB; andere Zahlen (Original 10 %, 18 %); {NR}')
z('2026MgrundlegendBStochastikWTR2-1d', E, S2, 'nein',
  'In einer Musik-Sammlung sind 28 % der Lieder Hip-Hop-Songs. Es werden 25 Lieder zufällig ausgewählt; $X$ ist '
  'die Anzahl der Hip-Hop-Songs darunter. Gib die Bedeutung der Aussage '
  '$\\sum_{k=0}^{9} \\binom{25}{k} \\cdot 0{,}28^k \\cdot 0{,}72^{25-k} \\approx 0{,}866$ im Sachzusammenhang an.',
  'Summe von 0 bis 9 ⇒ P(X ≤ 9) ≈ 0,866 | Mit etwa 86,6 % Wahrscheinlichkeit sind unter den 25 Liedern höchstens '
  '9 Hip-Hop-Songs',
  'II', 14, f'IQB-Pool, nicht BB; andere Zahlen (Original 20 Lieder, 0,32, bis 8, ≈ 0,843); {NR}')
z('2020MgrundlegendAStochastik2-b', E, S2, 'nein',
  'Die Zufallsgröße $X$ ist binomialverteilt mit unbekanntem $n$ und $p = 0{,}25$. Formuliere eine '
  'Aufgabenstellung im Sachzusammenhang, die mit dem Ansatz $1 - 0{,}75^n < 0{,}5$ gelöst wird, und gib die Lösung '
  'an.',
  'z. B. Glücksrad mit Gewinn 25 %: Wie oft darf man höchstens drehen, damit die Wahrscheinlichkeit für mindestens '
  'einen Gewinn unter 50 % bleibt? | 1 − 0,75² = 0,4375 < 0,5; 1 − 0,75³ ≈ 0,578 ⇒ höchstens n = 2',
  'III', 15, f'IQB-Pool, nicht BB; andere Zahlen (Original 1 − 0,8^n < 0,3); {NR}', 'ganz')

# ---------------------------------------------------------------- AS70 Binomialwahrscheinlichkeit
E, S1, S2 = 'Binomialwahrscheinlichkeit', 'Wahrscheinlichkeit gesucht', 'n, p oder k gesucht'
z('2026-bb-gk-B4b', E, S1, 'ja',
  TREUE + 'Ermittle die Wahrscheinlichkeit dafür, dass weniger als 10 der 12 Personen Treuepunkte sammeln.',
  'X ~ B(12; 0,8); weniger als 10 ⇒ P(X < 10) = P(X ≤ 9) ≈ 0,442',
  'I', 1, f'andere Zahlen (Original 75 %, n = 10, P(X < 8) ≈ 0,474); Rechner wie im Original; {NR}')
z('2022-bebb-gk-B4b', E, S1, 'ja',
  PAKET + 'Es werden 100 Pakete zufällig ausgewählt; $X$ ist die Anzahl der Pakete mit dem Ziel B. Bestimme mit '
  'dem Tabellenausschnitt die Wahrscheinlichkeit dafür, dass genau zehn der Pakete das Ziel B haben, und die '
  'Wahrscheinlichkeit dafür, dass weniger als zehn das Ziel B haben.',
  'P(genau 10) = P(X ≤ 10) − P(X ≤ 9) = 0,8243 − 0,7220 ≈ 0,102 | weniger als zehn ⇒ P(X < 10) = P(X ≤ 9) ≈ 0,722',
  'I', 2, f'andere Zahlen (Original 7 %, genau neun, 0,104 und 0,734); Tabelle wie die Anlage, nur Ausschnitt; {NR}',
  grafik=tabelle(100, 0.08, [8, 9, 10, 11]))
z('2023-bebb-gk-B4.1f', E, S2, 'ja',
  LEHR + 'Es werden Lehrkräfte zufällig ausgewählt. Ermittle, wie viele Lehrkräfte man mindestens auswählen muss, '
  'damit mit einer Wahrscheinlichkeit von mindestens 95 % mindestens eine davon an einem Gymnasium arbeitet.',
  'P(mindestens eine) = 1 − 0,7^n ≥ 0,95 ⇒ 0,7^n ≤ 0,05 ⇒ n ≥ ln 0,05 / ln 0,7 ≈ 8,4 ⇒ n = 9',
  'II', 3, f'andere Zahlen (Original 25 %, n = 11); {NR}', 'ganz')
z('2022-bebb-gk-B4d', E, S2, 'ja',
  PAKET + 'Ermittle, wie viele Pakete man mindestens zufällig auswählen muss, damit mit einer Wahrscheinlichkeit '
  'von mindestens 90 % mindestens eines davon das Ziel B hat.',
  '1 − 0,92^n ≥ 0,9 ⇒ 0,92^n ≤ 0,1 ⇒ n ≥ ln 0,1 / ln 0,92 ≈ 27,6 ⇒ n = 28',
  'II', 4, f'andere Zahlen (Original 7 %, 32 Pakete); {NR}', 'ganz')
z('2022-bebb-gk-B4e', E, S2, 'ja',
  PAKET + 'Ein Teil der Pakete hat das Ziel C. Wählt man 20 Pakete zufällig aus, so hat mit einer '
  'Wahrscheinlichkeit von etwa 67 % keines davon das Ziel C. Ermittle den Anteil der Pakete mit dem Ziel C an allen '
  'Paketen.',
  '(1 − p)²⁰ = 0,67 ⇒ 1 − p = $\\sqrt[20]{0{,}67}$ ≈ 0,9802 ⇒ p ≈ 0,020 = 2 %',
  'II', 5, f'andere Zahlen (Original 54 %, 3 %); {NR}')
z('2025-bebb-gk-B4d', E, S2, 'ja',
  HAUS + 'Ermittle den kleinstmöglichen Wert von $k$, für den $P(X \\le k)$ mehr als 90 % beträgt.',
  'P(X ≤ 75) ≈ 0,8895 < 0,9; P(X ≤ 76) ≈ 0,9110 > 0,9 ⇒ k = 76',
  'II', 6, f'andere Zahlen (Original 1000 Haushalte, 9,18 %, k = 104); Rechner wie im Original; {NR}', 'ganz')
# Mehr AS70
z('2021-be-gk-B4a', E, S1, 'nein',
  'Bei einem Handyspiel hat man jeden Sonntag zehn Versuche; bei jedem Versuch gewinnt man mit 35 % '
  'Wahrscheinlichkeit einen Stern. $X$ ist die Anzahl der Sterne bei zehn Versuchen. Berechne mit dem '
  'Tabellenausschnitt die Wahrscheinlichkeiten der Ereignisse $A$: „mehr als sechs Sterne“ und $B$: „mindestens '
  'vier, höchstens sieben Sterne“.',
  'P(A) = P(X > 6) = 1 − P(X ≤ 6) = 1 − 0,9740 = 0,026 | P(B) = P(X ≤ 7) − P(X ≤ 3) = 0,9952 − 0,5138 ≈ 0,481',
  'I', 7, f'andere Zahlen (Original 40 %, fünf bis acht Sterne); Tabelle als Ausschnitt; {NR}',
  grafik=tabelle(10, 0.35, [3, 4, 5, 6, 7]))
z('2020-be-gk-B4.2a', E, S1, 'nein',
  'In einem großen Unternehmen ist ein Drittel der Beschäftigten weiblich. Es werden 40 Beschäftigte zufällig '
  'ausgewählt; $X$ ist die Anzahl der weiblichen darunter. Ermittle die Wahrscheinlichkeit dafür, dass mindestens '
  '15 der Ausgewählten weiblich sind.',
  'P(X ≥ 15) = 1 − P(X ≤ 14) = 1 − 0,6578 ≈ 0,342',
  'I', 8, f'andere Zahlen (Original 50 Beschäftigte, mindestens 17); Rechner statt Tabelle; {NR}')
z('2019-be-gk-B4.1a', E, S1, 'nein',
  'In einem Land besitzen 75 % der Erwachsenen einen Führerschein. Es werden 100 Erwachsene zufällig ausgewählt; '
  '$X$ ist die Anzahl der Führerscheinbesitzer darunter. Berechne die Wahrscheinlichkeit dafür, dass genau 75 einen '
  'Führerschein besitzen, und mit dem Tabellenausschnitt die Wahrscheinlichkeit dafür, dass höchstens 70 einen '
  'Führerschein besitzen.',
  'P(genau 75) = (100 über 75) · 0,75⁷⁵ · 0,25²⁵ ≈ 0,092 | Gegenzahl Y = 100 − X hat p = 0,25 ⇒ P(X ≤ 70) = '
  'P(Y ≥ 30) = 1 − P(Y ≤ 29) = 1 − 0,8505 ≈ 0,150',
  'II', 9, f'andere Zahlen (Original 80 %, genau 80, höchstens 75); Tabelle mit p ≤ 0,5 wie im Original; {NR}',
  grafik=tabelle(100, 0.25, [28, 29, 30, 31]))
z('2018-be-gk-B3.2a', E, S1, 'nein',
  'Im Mittel sind 15 % der Bildschirme einer Sorte fehlerhaft. Es werden 50 Bildschirme zufällig ausgewählt; $X$ '
  'ist die Anzahl der fehlerhaften. Bestimme mit dem Tabellenausschnitt die Wahrscheinlichkeiten der Ereignisse '
  '$A$: „höchstens 6 fehlerhaft“ und $B$: „mehr als 7 und weniger als 12 fehlerhaft“.',
  'P(A) = P(X ≤ 6) ≈ 0,361 | P(B) = P(8 ≤ X ≤ 11) = P(X ≤ 11) − P(X ≤ 7) = 0,9372 − 0,5188 ≈ 0,418',
  'II', 10, f'andere Zahlen (Original 20 %, höchstens 8, 11 bis 14); {NR}',
  grafik=tabelle(50, 0.15, [6, 7, 8, 11]))
z('2019-be-gk-B4.1b', E, S2, 'nein',
  'In einem Land besitzen 75 % der Erwachsenen einen Führerschein. Ermittle, wie viele Erwachsene man mindestens '
  'zufällig auswählen muss, damit mit einer Wahrscheinlichkeit von mindestens 99 % mindestens eine Person ohne '
  'Führerschein darunter ist.',
  '1 − 0,75^n ≥ 0,99 ⇒ 0,75^n ≤ 0,01 ⇒ n ≥ ln 0,01 / ln 0,75 ≈ 16,008 ⇒ n = 17',
  'II', 11, f'andere Zahlen (Original 80 %, n = 21); {NR}', 'ganz')
z('2020-be-gk-B4.1c', E, S2, 'nein',
  'Ein Glücksrad hat fünf gleich große Sektoren, einer davon ist rot. Ermittle, wie oft man mindestens drehen muss, '
  'um mit einer Wahrscheinlichkeit von mindestens 95 % mindestens einmal Rot zu erhalten.',
  '1 − 0,8^n ≥ 0,95 ⇒ 0,8^n ≤ 0,05 ⇒ n ≥ ln 0,05 / ln 0,8 ≈ 13,4 ⇒ n = 14',
  'II', 12, f'andere Zahlen (Original Würfel mit P(6) = 1/3, 8 Würfe); {NR}', 'ganz')
z('2021-be-gk-B4e', E, S2, 'nein',
  'Bei einem Handyspiel gewinnt man bei jedem Versuch mit 35 % Wahrscheinlichkeit einen Stern. Ermittle, wie viele '
  'Versuche man mindestens braucht, um mit einer Wahrscheinlichkeit von mindestens 95 % mindestens einen Stern zu '
  'gewinnen.',
  '1 − 0,65^n ≥ 0,95 ⇒ 0,65^n ≤ 0,05 ⇒ n ≥ ln 0,05 / ln 0,65 ≈ 6,95 ⇒ n = 7',
  'II', 13, f'andere Zahlen (Original 40 %, n = 6); {NR}', 'ganz')
z('2018-be-gk-B3.2d', E, S2, 'nein',
  'Nach einer Verbesserung der Fertigung soll die Wahrscheinlichkeit dafür, dass unter 30 zufällig ausgewählten '
  'Bildschirmen keiner fehlerhaft ist, mindestens 20 % betragen. Ermittle den höchsten Anteil fehlerhafter '
  'Bildschirme, der dafür zulässig ist.',
  '(1 − p)³⁰ ≥ 0,2 ⇒ 1 − p ≥ $\\sqrt[30]{0{,}2}$ ≈ 0,9478 ⇒ p ≤ 0,052 ⇒ höchstens etwa 5,2 %',
  'III', 14, f'andere Zahlen (Original 25 Bildschirme, 10 %, 8,8 %); {NR}')
z('2021MgrundlegendBStochastikWTR2-1d', E, S2, 'nein',
  'Bei einem Handyspiel hat man zehn Versuche; $X$ ist die Anzahl der gewonnenen Sterne. Nach einer Änderung der '
  'Gewinnwahrscheinlichkeit $p$ je Versuch beträgt die Wahrscheinlichkeit, höchstens zwei Sterne zu gewinnen, etwa '
  '62 %. Ermittle $p$ auf ganze Prozent.',
  'Probieren mit dem Rechner: p = 0,21 ⇒ P(X ≤ 2) ≈ 0,647; p = 0,22 ⇒ P(X ≤ 2) ≈ 0,617; p = 0,23 ⇒ ≈ 0,586 ⇒ p ≈ 22 %',
  'II', 15, f'IQB-Pool, nicht BB; andere Zahlen (Original höchstens drei Sterne); {NR}')
z('2022MgrundlegendBStochastikWTR2-2a', E, S2, 'nein',
  'In einer Studie ist die Anzahl der Infizierten unter den Teilnehmenden binomialverteilt mit $p = \\frac{1}{5}$; '
  'der Erwartungswert beträgt 150. Berechne die Anzahl der Teilnehmenden und die Wahrscheinlichkeit für genau 150 '
  'Infizierte.',
  'n · 1/5 = 150 ⇒ n = 750 | P(genau 150) ≈ 0,036',
  'I', 16, f'IQB-Pool, nicht BB; andere Zahlen (Original p = 1/3, Erwartungswert 200); {NR}')
z('2026MgrundlegendBStochastikWTR2-1c', E, S1, 'nein',
  'In einer Musik-Sammlung sind 28 % der Lieder Hip-Hop-Songs. Es werden 25 Lieder zufällig ausgewählt. Ermittle '
  'die Wahrscheinlichkeit dafür, dass mehr als 6 Hip-Hop-Songs darunter sind.',
  'P(X > 6) = 1 − P(X ≤ 6) ≈ 0,575',
  'I', 17, f'IQB-Pool, nicht BB; andere Zahlen (Original 20 Lieder, 0,32, mehr als 5); {NR}')
z('2019MgrundlegendBStochastikWTR1-1a', E, S1, 'nein',
  'In einem Land besitzen 60 % der Jugendlichen ein Fahrrad mit Elektromotor. Es werden 250 Jugendliche zufällig '
  'ausgewählt; $X$ ist die Anzahl derer mit einem solchen Fahrrad. Berechne die Wahrscheinlichkeit dafür, dass $X$ '
  'um höchstens 5 % vom Erwartungswert abweicht.',
  'E(X) = 250 · 0,6 = 150; 5 % von 150 = 7,5 ⇒ 143 ≤ X ≤ 157 ⇒ P = P(X ≤ 157) − P(X ≤ 142) ≈ 0,667',
  'II', 18, f'IQB-Pool, nicht BB; andere Zahlen (Original Führerschein 80 %, 200 Erwachsene); {NR}')

# ---------------------------------------------------------------- AS80 Säulendiagramm und Erwartungswert
E, S1, S2, S3 = ('Säulendiagramm und Erwartungswert', 'Wahrscheinlichkeit ablesen', 'Erwartungswert am Diagramm',
                 'Erwartungswert berechnen')
G16 = saeulen(16, 0.25, kmax=12, ymax=0.25)
G19 = saeulen(19, 0.5, kmin=2, kmax=17, ymax=0.2, ystep=0.05, yfein=0.05, ohne=True)
z('2023-bebb-gk-A1.7a', E, S1, 'ja',
  'Die Abbildung zeigt die Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße $X$. Bestimme mit '
  'der Abbildung einen Näherungswert für $P(4 < X < 7)$.',
  'P(4 < X < 7) = P(X = 5) + P(X = 6) ≈ 0,20 + 0,11 ≈ 0,31',
  'I', 1, f'andere Zahlen (Original B(12; 0,25), P(3 < X < 6) ≈ 0,29); Verteilung B(10; 0,4), Ablesewerte 0,30 bis '
  f'0,32 vertretbar; {NR}', grafik=saeulen(10, 0.4, ymax=0.3, hoehe=2.8, breite=0.55))
z('2026-bb-gk-A1.6b', E, S1, 'ja',
  D16 + 'Gib mit der Abbildung die natürlichen Zahlen $v$ und $w$ an, für die gilt: $P(X = v) \\approx 0{,}18$ und '
  '$0{,}15 < P(X \\le w) < 0{,}25$.',
  'Säule mit Höhe 0,18 bei k = 5 ⇒ v = 5 | P(X ≤ 1) ≈ 0,01 + 0,05 = 0,06; P(X ≤ 2) ≈ 0,06 + 0,13 = 0,19; '
  'P(X ≤ 3) ≈ 0,40 ⇒ w = 2',
  'II', 2, f'andere Zahlen (Original n = 20, p = 0,2, 0,175; v = 5, w = 2); Verteilung B(16; 0,25); {NR}',
  'ganz', grafik=G16)
z('2026-bb-gk-B4c', E, S1, 'ja',
  TREUE + 'Die Abbildung zeigt die Wahrscheinlichkeitsverteilung der Zufallsgröße $Y$ mit $n = 12$ und '
  '$p = 0{,}2$. Erläutere, wie man mit der Abbildung die Wahrscheinlichkeit $P(X = 8)$ ermitteln kann.',
  'Y = 12 − X zählt die Personen, die nicht sammeln, p = 0,2 ⇒ genau 8 sammeln ⇔ genau 4 sammeln nicht, '
  'P(X = 8) = P(Y = 4) ⇒ Säule von Y bei vier ablesen | Wert ≈ 0,13',
  'II', 3, f'andere Zahlen (Original n = 10, p = 0,25, P(X = 6) = P(Y = 4)); {NR}',
  grafik=saeulen(12, 0.2, ymax=0.3, ystep=0.1, yfein=0.05, hoehe=2.8, breite=0.5))
z('2025-bebb-gk-A1.9b', E, S1, 'ja',
  SYM19 + 'Es gilt $P(X \\ge 8) \\approx 0{,}82$ und $P(X = 11) \\approx 0{,}14$. Berechne mit diesen Werten einen '
  'Näherungswert für $P(X = 9)$.',
  'symmetrisch um 9,5 ⇒ P(X = 8) = P(X = 11) ≈ 0,14 und P(X ≥ 10) = 0,5 ⇒ P(genau 9) ≈ 0,82 − 0,14 − 0,5 = 0,18',
  'III', 4, f'andere Zahlen (Original Symmetrie um 10,5, 0,81 und 0,14, P(X = 10) ≈ 0,17); Verteilung B(19; 0,5); '
  f'{NR}', grafik=G19)
z('2026-bb-gk-A1.6a', E, S2, 'ja',
  D16 + 'Der Erwartungswert von $X$ ist ganzzahlig. Ermittle mit der Abbildung den Wert von $p$.',
  'höchste Säule bei k = 4 und E(X) ganzzahlig ⇒ E(X) = 4 ⇒ 16 · p = 4 ⇒ p = 0,25',
  'I', 5, f'andere Zahlen (Original n = 20, höchste Säule 4, p = 0,2); {NR}', grafik=G16)
OPT = ' || '.join('\\resizebox{0.92\\gbildbreite}{!}{\\raisebox{\\depth}{' + g + '}}' for g in (
    saeulen(15, 1 / 3, ymax=0.3, ystep=0.1, yfein=0.05, hoehe=2.8, breite=0.5),
    saeulen(15, 0.2, ymax=0.3, ystep=0.1, yfein=0.05, hoehe=2.8, breite=0.5),
    saeulen(15, 0.2, ymax=0.6, ystep=0.1, yfein=0.05, hoehe=2.8, breite=0.5, faktor=2.0)))
z('2023-bebb-gk-A1.7b', E, S2, 'ja',
  'Die Zufallsgröße $Y$ ist binomialverteilt mit $n = 15$ und $p = 0{,}2$. Genau eine der Abbildungen A, B und C '
  'zeigt die Wahrscheinlichkeitsverteilung von $Y$. Entscheide begründet, welche.',
  'Abbildung B (zweite Option) | E(Y) = 15 · 0,2 = 3 ⇒ B hat die höchste Säule bei 3, A bei 5, und bei C ist die '
  'Summe der Säulen größer als 1',
  'II', 6, f'andere Zahlen (Original n = 12, p = 0,25, Abb. 2); A = B(15; 1/3), C = doppelte Höhen; {NR}',
  grafik=OPT, form='ankreuzen+karo')
z('2025-bebb-gk-A1.9a', E, S2, 'ja',
  SYM19 + 'Begründe, dass $n$ keine gerade Zahl ist.',
  'zwei gleich hohe höchste Säulen bei 9 und 10 ⇒ E(X) = n · 0,5 = 9,5 nicht ganzzahlig ⇒ n = 19 ungerade',
  'II', 7, f'andere Zahlen (Original Säulen bei 10 und 11, n = 21); {NR}', 'ganz', grafik=G19)
z('2025-bebb-gk-B4c', E, S2, 'ja',
  HAUS + 'Beurteile ohne Berechnung von Wahrscheinlichkeiten die Aussage: „Die Wahrscheinlichkeitsverteilung von '
  '$X$ nimmt für $k = 64$ ihren größten Wert an.“',
  'falsch: E(X) = 800 · 0,0824 = 65,92 ⇒ größter Wert bei 66 (Nachbar von 65,92), nicht bei 64',
  'II', 8, f'andere Zahlen (Original 1000, 9,18 %, Aussage 90, Maximum 92); {NR}')
z('2022-bebb-gk-B4c', E, S3, 'ja',
  PAKET + 'Unter 100 zufällig ausgewählten Paketen haben genau zehn das Ziel B. Berechne, um wie viel Prozent '
  'diese Anzahl vom Erwartungswert abweicht.',
  'E(X) = 100 · 0,08 = 8 ⇒ Abweichung = (10 − 8) / 8 = 1/4 = 25 %',
  'I', 9, f'andere Zahlen (Original 7 %, genau neun, 2/7 ≈ 28,6 %); {NR}')
z('2026-bb-gk-A1.9a', E, S3, 'ja',
  'Die Zufallsgröße $X$ ist binomialverteilt mit dem Erwartungswert $\\mu = 36$ und der Standardabweichung '
  '$\\sigma = 3$. Bestimme einen Term ohne Parameter, mit dem man $P(X = 37)$ berechnen kann.',
  '$\\sigma^2$ = n · p · (1 − p) = μ · (1 − p) ⇒ 9 = 36 · (1 − p) ⇒ 1 − p = 0,25 ⇒ p = 0,75; n = μ / p = 36 / 0,75 = 48 ⇒ '
  'Term (48 über 37) · 0,75³⁷ · 0,25¹¹ | Wert ≈ 0,128',
  'III', 10, f'andere Zahlen (Original μ = 20, σ = 2, n = 25, p = 0,8); Schwere III (5 BE, AFB II|III, schwerste am '
  f'Ende); {NR}')
# Mehr AS80
z('2020-be-gk-B4.2d', E, S2, 'nein',
  'In einem großen Unternehmen ist ein Drittel der Beschäftigten weiblich. Es werden 40 Beschäftigte zufällig '
  'ausgewählt; $X$ ist die Anzahl der weiblichen darunter. Begründe ohne Berechnung von Wahrscheinlichkeiten, dass '
  'die Wahrscheinlichkeitsverteilung von $X$ für 13 oder 14 ihren größten Wert hat.',
  'E(X) = 40 · 1/3 ≈ 13,3 ⇒ größter Wert bei einem Nachbarn des Erwartungswerts, also 13 oder 14',
  'II', 11, f'andere Zahlen (Original 50 Beschäftigte, 16 oder 17); {NR}', 'ganz')
z('2018-be-gk-B3.2b', E, S2, 'nein',
  'Die Anzahl $X$ der fehlerhaften Geräte unter 240 zufällig ausgewählten Bildschirmen ist binomialverteilt mit '
  '$p = 0{,}15$. Gib die Anzahl fehlerhafter Bildschirme an, die mit der größten Wahrscheinlichkeit auftritt.',
  'E(X) = 240 · 0,15 = 36 ganzzahlig ⇒ größte Wahrscheinlichkeit bei 36',
  'I', 12, f'andere Zahlen (Original 250, 0,2, 50); {NR}', 'ganz')
z('2019-be-gk-B4.2c', E, S3, 'nein',
  'Zwei Geschwister würfeln jeden Tag einmal; mit der Wahrscheinlichkeit $\\frac{5}{12}$ bringt der ältere den Müll '
  'hinunter. Berechne den Erwartungswert dafür, wie oft der ältere in 24 Tagen den Müll hinunterbringt.',
  'E(X) = 24 · 5/12 = 10',
  'I', 13, f'andere Zahlen (Original 30 Tage, 12,5); {NR}', 'ganz')
z('2017MgrundlegendAStochastik11-a', E, S1, 'nein',
  'Die Abbildung zeigt die Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße $X$. Ermittle mit '
  'der Abbildung einen Näherungswert für $P(4 \\le X \\le 6)$.',
  'P(4 ≤ X ≤ 6) = P(X = 4) + P(X = 5) + P(X = 6) ≈ 0,11 + 0,17 + 0,19 ≈ 0,47',
  'I', 14, f'IQB-Pool, nicht BB; andere Zahlen (Original P(5 ≤ X ≤ 7)); Verteilung B(18; 0,35); {NR}',
  grafik=saeulen(18, 0.35, kmax=14, ymax=0.25, hoehe=2.8, breite=0.5))
z('2021MgrundlegendAStochastik2-b', E, S1, 'nein',
  'Die Abbildung zeigt die Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße $Y$ mit '
  '$p = 0{,}5$; sie ist symmetrisch zu $k = 11{,}5$. Es gilt $P(Y \\le 13) \\approx 0{,}80$ und '
  '$P(Y = 10) \\approx 0{,}14$. Berechne mit diesen Werten einen Näherungswert für $P(Y = 12)$.',
  'symmetrisch ⇒ P(Y ≤ 11) = 0,5 und P(Y = 13) = P(Y = 10) ≈ 0,14 ⇒ P(genau 12) ≈ 0,80 − 0,5 − 0,14 = 0,16',
  'III', 15, f'IQB-Pool, nicht BB; andere Zahlen (Original Symmetrie um 13,5, 0,78 und 0,13); Verteilung '
  f'B(23; 0,5); {NR}', grafik=saeulen(23, 0.5, kmin=4, kmax=19, ymax=0.2, ystep=0.05, yfein=0.05, ohne=True, hoehe=2.8, breite=0.5))
z('2019MgrundlegendAStochastik12-b', E, S2, 'nein',
  'In einer Urne liegen 4 rote und 6 weiße Kugeln. Es wird zehnmal mit Zurücklegen gezogen; $X$ ist die Anzahl der '
  'weißen Kugeln. Begründe ohne Berechnung von Wahrscheinlichkeiten, dass keines der Diagramme A und B die '
  'Verteilung von $X$ zeigt.',
  'E(X) = 10 · 0,6 = 6 | A: höchste Säule bei 4 statt bei 6 | B: Säulen summieren sich auf etwa 2 > 1',
  'II', 16, f'IQB-Pool, nicht BB; andere Zahlen (Original 3 rote, 7 weiße; Maximum bei 3); A = B(10; 0,4), B = '
  f'doppelte Höhen; {NR}', 'ganz',
  grafik=' || '.join((saeulen(10, 0.4, ymax=0.3, ystep=0.1, yfein=0.05, hoehe=2.8, breite=0.5),
                      saeulen(10, 0.6, ymax=0.6, ystep=0.1, yfein=0.05, hoehe=2.8, breite=0.5, faktor=2.0))))
z('2020MgrundlegendAStochastik2-a', E, S3, 'nein',
  'Die Zufallsgröße $X$ ist binomialverteilt mit $n = 6$ und dem Erwartungswert 2. Berechne $P(X = 6)$.',
  '6 · p = 2 ⇒ p = 1/3 ⇒ P(genau 6) = (1/3)⁶ = 1/729',
  'II', 17, f'IQB-Pool, nicht BB; andere Zahlen (Original n = 4, E = 2, 1/16); {NR}', 'bruch')

with open(ZIEL, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=SP, delimiter=';', lineterminator='\n')
    w.writeheader()
    for r in Z:
        w.writerow({k: r.get(k, '') for k in SP})
print(len(Z), 'Zeilen')

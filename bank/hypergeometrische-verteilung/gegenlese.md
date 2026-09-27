# Gegenlese: hypergeometrische-verteilung

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung), unabhängige Gegenlese
Geprüfte Zeilen: 62 (zone 19, e1 26, e2 17)
Korrekturen: 0

Alle Lösungszahlen und pruef-Werte mit Python/sympy aus der Aufgabe
nachgerechnet; bank-pruef.py: 0 Abweichungen.

## Entscheidungen

- Korrigiert wird nur eine falsche Zahl mit eindeutiger Korrektur;
  eine falsche Aussage in einer Begründen-Lösung steht als Befund
  unter Punkt 1.
- Eine Aufgabe, die eine andere Zeile wörtlich wiederholt, steht
  unter Punkt 3 (Variante ändert mehr/anderes als das Merkmal).

## Befunde

### Punkt 1 – Lösung rechnerisch richtig

- hypergeometrische-verteilung-e2-k2-s2-v2: „P(X ≤ k) … damit größer als P(X = k) allein“ stimmt für k = 0 nicht (dort gleich) – „mindestens so groß wie $P(X = k)$ allein“.

### Punkt 2 – eindeutig lösbar

- hypergeometrische-verteilung-e1-k2-s2-v2: Aufgabe nennt nur die beiden Terme, keinen Zufallsversuch; die Lösung setzt „zwei Treffer aus drei Treffern bei fünf Kugeln“ voraus – Lage in die Aufgabe schreiben (Urne mit 5 Kugeln, 3 rot, 2 ohne Zurücklegen gezogen, P(beide rot)).

### Punkt 3 – passt zu sprosse_text und merkmal

- hypergeometrische-verteilung-e1-k1-s1-v2: fragt „beide Kirsche“ (reine Bruchkette), das Merkmal verlangt „mindestens eins über das Gegenereignis“; zudem dieselben Brüche wie zone-f4-v2 ($\frac{4}{7} \cdot \frac{3}{6}$) – nach „mindestens ein Kirschbonbon“ fragen ($1 - \frac{3}{7} \cdot \frac{2}{6} = \frac{6}{7}$).
- hypergeometrische-verteilung-e1-k2-s2-v3: fragt, wann das Binomialmodell bei großer Gesamtheit als Näherung taugt – keines der beiden Themen der Sprosse (p ändert sich; Teilmengen = Bruchkette) – durch eine Begründung zu einem der beiden Themen ersetzen.
- hypergeometrische-verteilung-e2-k1-s0-v3: fragt nach $P(X \le 1)$ (kumuliert), Merkmal ist „Ansatz für eine Einzelwahrscheinlichkeit erkennen“ – auf eine Einzelwahrscheinlichkeit wie $P(X = 1)$ mit Distraktoren wie v1/v2 umstellen.
- hypergeometrische-verteilung-e2-k2-s2-v2: fragt „Einzelwert statt Summe“, die Sprosse verlangt „warum beide Nachbarwerte zu belegen sind“ – etwa „Warum reicht es nicht, nur $P(X \le k) < s$ zu zeigen?“.

### Punkt 4 – Schreibform

- hypergeometrische-verteilung-zone-f4-v3: Merkmal „vor dem Multiplizieren kürzen“, die Lösung $\frac{60}{336} = \frac{5}{28}$ multipliziert erst aus – Lösung mit Kürzen vor dem Ausmultiplizieren zeigen, etwa $\frac{5 \cdot 4 \cdot 3}{8 \cdot 7 \cdot 6} = \frac{5}{28}$ mit sichtbarem Kürzen (pruef bleibt).

### Punkt 5 – Ankreuzen

keine

### Punkt 6 – Fehler finden

- hypergeometrische-verteilung-e2-k2-s1-v2: Alis Fehler (Einzelwert $P(X = 2)$ statt Summe verglichen) ist falsch, gehört aber zu keinem der beiden Muster der Sprosse (binomial kumuliert; Schranke am falschen Nachbarwert), sondern zur Falle aus e2-k1-s2 – Fehler nach einem der genannten Muster bauen, etwa $n = 2$, weil $P(X \le 2)$ der erste Wert über der Schranke ist.

Sauber: 55 Zeilen ohne Befund

# Zweitlesung zinsrechnung

Datum: 2026-09-28 · Modell: claude-fable-5-1
(Zweitleser, ohne Kenntnis von gegenlese.md) · geprüfte Zeilen: 165
(zone 35, e1 75, e2 55)

Prüfung: Jede Zeile mit eigenem Skript im Scratchpad nachgerechnet:
pruef ausgewertet und gegen die Ergebniszahlen der loesung gehalten
(0 Abweichungen), dazu für 146 Zeilen eine eigene Formel aus dem
Aufgabentext (einfache Zinsen K·p·t/100, Monate durch zwölf, Tage
durch dreihundertsechzig mit 30-Tage-Monaten, Zinseszins K·qⁿ,
Tabellen Jahr für Jahr mit Cent-Rundung); alle Werte treffen die
Lösung, auch die Tabellen mit Zwischenrundung (e2-k1-s4, e2-k1-s10,
e2-k2). Die 19 Zeilen ohne Ziffer im Ergebnis (12 Ankreuzen, 6
Begründen, 1 Tabelle mit Cent-Zeilen) sind von Hand gelesen.
`python3 werkzeuge/bank-pruef.py zinsrechnung`: zone, e1, e2 je 0
Abweichungen, 0 Warnungen. 12 Ankreuzen-Zeilen: je genau eine Option
wortgleich mit loesung. 7 Fehler-finden-Zeilen (zone 1, e1 3, e2 3):
die eingebaute Rechnung ist jeweils arithmetisch richtig und im
Verfahren falsch, die angegebene richtige Rechnung stimmt. Keine
Dublette; keine Kastenzahl (12, 30, 100, 360 sowie die Zahlbelegungen
aus Merkkasten, Typische Fehler und Originalen) in einer aufgabe.
Zinssätze (Sparen 1–4 %, Kredit 5–11 %) und Beträge sind realistisch.

## Befunde

e1-k1-s9-v1: „Für ein Motorroller" – Akkusativ fehlt; „Für einen
Motorroller". (v3 „Für ein Laptop" ist nach Duden zulässig, einheitlich
wäre „einen Laptop".)

e1-k4-s2-v1: „Begründe ohne genau zu rechnen." – Komma vor der
Infinitivgruppe mit „ohne" ist Pflicht: „Begründe, ohne genau zu
rechnen." Die Lösung rechnet zwar 200 € und 24 € aus, das geht im
Kopf und trägt die Begründung; kein Änderungsbedarf dort.

e2-k2-s1-v1, -v2, -v3: „Fülle die Tabelle aus" verlangt auch die
Spalte Zinsen, die loesung nennt nur die Guthaben – Zinsen ergänzen
(v1: 12,00 €; 14,64 €; 17,33 € · v2: 60,00 €; 69,30 € · v3: 48,00 €;
61,92 €), sonst fehlt der Lösungsdatei die halbe Tabelle.

e2-k1-s4-v1, -v2, -v3: Text „jedes Jahr 120 € Einzahlung", die
Tabelle zeigt in Jahr 1 aber Einzahlung „–" und ein Startguthaben –
„ab Jahr 2 jedes Jahr 120 € Einzahlung" oder die erste Zeile „Start"
nennen (wie in e2-k2). Rechnung und Lösung stimmen.

e1-k1-s1-v2 und -v4 gegen e1-k1-s0-v3 und -v4: dieselben Zahlenpaare
(700 € zu 3 %, 900 € zu 2 %) stehen in Vorstufe und Grundfall
derselben Kette; auf einem Blatt liest der Schüler beide – keine
Dublette im Regelsinn, aber im Grundfall andere Zahlen wählen (etwa
800 € zu 3 %, 1 100 € zu 2 %).

e2-k3-s1-v1, -v2, -v3: sprosse_text „Ratenkauf und Kredit mit
Zinseszins", alle drei Varianten sind Kredit oder Zahlungsziel, keine
Rate – eine Variante als Ratenkauf, oder hinnehmen (Ratenkauf mit
Zinseszins trägt auf dieser Höhe kaum).

zone-f8-v2: merkmal „Tabelle um eine Zeile fortschreiben, im Kopf",
die Aufgabe ist reines Ablesen eines Feldes – merkmal „Feld aus Zeile
und Spalte lesen" (derselbe Fall wie f4-v2 und f5-v2, die stand.md
schon nennt).

Sauber: 151 Zeilen ohne Befund

## Abgleich

Beide Leser: zone-f8-v2: Ablesen statt Fortschreiben, merkmal passt
nicht.

Nur Erstleser:
- e2-k4-s3-v1 („etwa 2 250 €" gegen 2 251,02 €): bestätigt – nach
  Prüfung liegt die Entscheidung 1,02 € neben einer ungefähren Angabe;
  „etwa" streichen genügt.
- zone-f4-v2 (Multiplikation statt Addition): bestätigt, stand.md führt
  den Fall schon unter „Offene Punkte".
- zone-f5-v2 (fester Faktor statt Dreisatz mit Teiler): bestätigt,
  ebenfalls in stand.md genannt.
- e2-k3-s1-v1 (Rückzahlung statt Zinsen gefragt): bestätigt – die
  Schwestervarianten fragen nach Kosten, v1 nach der Rückzahlung;
  Varianten einer Sprosse sollen sich nur in Zahlen und Kontext
  unterscheiden.
- e2-k4-s3-v2 (Startkapital rückwärts als Anwendung): in der Sache
  bestätigt – merkmal „entscheiden" trifft die Frage nicht; im Urteil
  „eingekleidete Rechnung" nicht bestätigt, siehe Widersprüche.
- e1-k1-s0-v1, e1-k1-s0-v2 (Frage nennt das Gesuchte wortgleich wie
  die Option): bestätigt – die Option koppelt Zinswort und
  Prozentbegriff, so ist nichts zuzuordnen; neben der Umformulierung
  der Frage geht auch: Optionen nur mit den Prozentbegriffen
  („der Grundwert", „der Prozentsatz", „der Prozentwert").

Nur Zweitleser:
- e1-k1-s9-v1: „Für ein Motorroller" (Akkusativ).
- e1-k4-s2-v1: Komma vor „ohne genau zu rechnen".
- e2-k2-s1-v1 bis -v3: Lösung ohne die Spalte Zinsen.
- e2-k1-s4-v1 bis -v3: „jedes Jahr Einzahlung" gegen Jahr 1 ohne
  Einzahlung.
- e1-k1-s1-v2, -v4: Zahlenpaare der Vorstufe (e1-k1-s0-v3, -v4)
  wiederholen sich im Grundfall.
- e2-k3-s1: kein Ratenkauf, obwohl sprosse_text ihn nennt (anderer
  Punkt als der Erstleser-Befund zu v1, dieselben Zeilen).

Widersprüche: e2-k4-s3-v2 – der Erstleser hält die Frage „Wie viel
Euro muss er heute anlegen?" für eine eingekleidete Rechnung ohne
Anwendung; der Zweitleser hält sie für eine im Kontext sinnvolle Frage
(Sparziel mit Zieltermin), die als Anwendung trägt, und sieht nur das
merkmal „entscheiden" als unpassend – die vorgeschlagene
Entscheidungsfrage wäre trotzdem eine saubere Lösung. Sonst keine.

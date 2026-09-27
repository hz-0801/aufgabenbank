# Gegenlese rekonstruktion-von-bestaenden

Datum: 2026-09-27
Modell: claude-opus-5-5
Geprüfte Zeilen: 122
Korrekturen: 0

## Entscheidungen

Widersprüchliche oder unrealistische Modellangaben (Anwendung) stehen unter 2 Eindeutigkeit, nicht unter 3.

Sprossen, deren Katalogtext mehrere Teilaspekte aufzählt (e1-k1-s4 Einheiten/konstante Phase, e1-k1-s5 Zielbestand/Woche/Abpumpphase), gelten als erfüllt, wenn die Varianten die Aspekte unter sich aufteilen; kein Befund unter 3.

## 1 Rechnung

keine

## 2 Eindeutigkeit

rekonstruktion-von-bestaenden-e1-k3-s4-v3: Modellbereich $0 \le t \le 5$ führt zu $15 + ∫_0^5 r(t)\,\mathrm{d}t = 115\,\%$ Ladestand (über 100 % schon ab $t \approx 3{,}1$) – Bereich auf $0 \le t \le 3$ begrenzen oder Rate so wählen, dass 100 % nicht überschritten wird

rekonstruktion-von-bestaenden-e2-k3-s4-v2: $t$ ist nicht erklärt (Einheit Tage und Startpunkt fehlen), und „Welcher Tag?“ passt nicht eindeutig zu $t = 4$ (Ende des vierten oder Beginn des fünften Tages) – „$t$ in Tagen seit Messbeginn“ ergänzen und „Nach wie vielen Tagen …?“ fragen

rekonstruktion-von-bestaenden-e3-k2-s3-v3: die Hochachse der Grafik trägt die Beschriftung $r$, die im Text nicht vorkommt (Graphen heißen $e$ und $a$) – ylabel leer lassen oder passend benennen

rekonstruktion-von-bestaenden-e3-k2-s4-v2: für $t < 3 - \sqrt{7}$ und $t > 3 + \sqrt{7}$ liegt die Erzeugung unter 2 kW; „wie viel Strom bleibt übrig“ ist damit mehrdeutig (Nettobilanz 24 kWh gegen tatsächlichen Überschuss $\approx 24{,}7$ kWh) – nach der Differenz aus Erzeugung und Verbrauch von 9 bis 15 Uhr fragen oder den Verbrauch so wählen, dass er nie über der Erzeugung liegt

## 3 Merkmal

rekonstruktion-von-bestaenden-e1-k1-s6-v3: Bestandsfunktion direkt gegeben, kein Integral, kein Tabellen-/Messwert und keine prozentuale Abweichung – passt nicht zu „Modellwert gegen Tabellenwert mit prozentualer Abweichung“ und weicht im Merkmal von v1/v2 ab – durch eine Variante nach dem Muster v1/v2 ersetzen

rekonstruktion-von-bestaenden-e1-k1-s6-v4: wie v3 (Bestandsfunktion, mittlere Änderungsrate, kein Tabellenwert, keine Abweichung) – durch eine Variante nach dem Muster v1/v2 ersetzen

rekonstruktion-von-bestaenden-e1-k1-s6-v5: wie v3 (Bestandsfunktion, mittlere Änderungsrate, kein Tabellenwert, keine Abweichung) – durch eine Variante nach dem Muster v1/v2 ersetzen

rekonstruktion-von-bestaenden-e3-k1-s4-v3: Nullstelle des Differenzintegrals gegen Schnittpunkt statt Flächengleichheit unter Eingangs- und Ausgangsrate über die Gesamtzahlen – passt nicht zum Sprossentext, anderes Merkmal als v1/v2 – als eigene Sprosse führen oder durch eine Ein-/Ausgangsraten-Variante ersetzen

rekonstruktion-von-bestaenden-e3-k1-s4-v4: wie v3 (z gegen $t_s$ statt Flächengleichheit über Gesamtzahlen) – als eigene Sprosse führen oder durch eine Ein-/Ausgangsraten-Variante ersetzen

## 4 Schreibform

keine

## 5 Ankreuzen

keine

## 6 Fehler finden

keine

Sauber: 113 Zeilen ohne Befund

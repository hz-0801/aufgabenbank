# Gegenlese: hypothesentests

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 113 (zone 22, e1 29, e2 23, e3 39)
Korrekturen: 0

Alle Lösungen mit scipy.stats.binom nachgerechnet, dazu die
Koeffizienten der Gütekurven (\funktion, \funktionab); keine
rechnerische Abweichung.

## Punkt 1 – Lösung richtig

hypothesentests-e2-k2-s2-v3: „der Test begrenzt nur, wie oft man beim Ablehnen irrt“ legt die bedingte Lesart nahe (Anteil falscher Ablehnungen), begrenzt ist aber die Wahrscheinlichkeit einer Ablehnung bei zutreffender Nullhypothese – „der Test begrenzt nur, wie wahrscheinlich eine Ablehnung ist, wenn die Nullhypothese zutrifft“.

## Punkt 2 – eindeutig lösbar

hypothesentests-zone-f2-v1, hypothesentests-zone-f2-v2, hypothesentests-zone-f2-v4: $X$ wird nicht eingeführt; der Schritt $P(X \ge 6) = 1 - P(X \le 5)$ gilt nur für ganzzahliges $X$ – Vorsatz „$X$ ist die Anzahl der Treffer.“
hypothesentests-zone-f5-v1, hypothesentests-zone-f5-v2, hypothesentests-zone-f5-v3, hypothesentests-zone-f5-v4: keine Rundungsvorgabe, die Lösung ist vierstellig (f1-v3/v4 sagen „auf vier Stellen“) – „auf vier Stellen“ ergänzen.
hypothesentests-e2-k2-s1-v1: Dass bei Ablehnung die Lieferung angenommen wird, steht nur in e2-k1-s3-v1; ohne diese Zeile ist Mias Aussage nicht beurteilbar – Halbsatz „der Händler nimmt die Lieferung nur bei Ablehnung an“ ergänzen.
hypothesentests-e2-k2-s1-v3: Die Lösung stützt sich auf den teuren Dünger, der im Aufgabentext fehlt – „Ein teurer Dünger soll die Keimquote erhöhen.“ voranstellen.

## Punkt 4 – Schreibform

hypothesentests-e1-k2-s1-v1, hypothesentests-e1-k2-s1-v2, hypothesentests-e1-k2-s1-v3: Die Lösung rechnet mit $Y$, das die Aufgabe nicht einführt; die Einheit nennt die Trefferzahl sonst $X$ – $X$ verwenden oder „$Y$ Anzahl der …“ in die Aufgabe.
hypothesentests-e3-k1-s5-v1, hypothesentests-e3-k1-s5-v2, hypothesentests-e3-k1-s5-v3, hypothesentests-e3-k1-s5-v4: dasselbe: $Y$ in der Lösung ohne Einführung, e3 sonst $X$ – vereinheitlichen.

Sauber: 96 Zeilen ohne Befund
